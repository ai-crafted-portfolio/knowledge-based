---
search:
  exclude: true
---

# IBM IIDR 11.4 — 詳細 (10/11)

[← IBM IIDR 11.4 の概要へ戻る](index.md)


## IBM IIDR 11.4 > リフレッシュ制御

### リフレッシュ制御 CDC Refresh 再始動後の確認 REF15 {#c11-i0485}
*分類: リフレッシュ制御*  ・  難易度: 中級

再始動後の確認では リフレッシュ制御 の 完了確認 を主操作として REF15 を判定します。再開点と未処理データへの注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF15 に残します。再始動後の確認を補助する 方式表示 では Refreshing を補助値として REF15 へ保存します。主判定の再始動後の確認ではリフレッシュ制御の 完了確認 から Rowsapplied を読み REF15 へ残します。証跡照合の再始動後の確認ではリフレッシュ制御の Rowsapplied と Refreshing を REF15 に保存します。記録対応の再始動後の確認ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF15 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 再始動後の確認 REF15について構成や状態を確認します。性能統計 CDC Communications Activity 依存関係の確認ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは通信統計からSendsを読むことで通信統計を確認し・送信回数だけでターゲット適用を防ぐ。
    - B. 状態を読み取るための働きは変更確認操作で採取欄を棚卸することで戻り値を確認し・重複反映を防ぐ。複製位置管理 Instance 0078固有の属性も確認対象に含める。
    - C. 状態を読み取るための働きは調査操作で保守欄を引き継ぎすることでサブスクリプを確認し・ログ先頭未到達の見落としを防ぐ。
    - D. 状態を読み取るための働きは完了確認からRowsappliedを読むことで完了確認を確認し・初期ロード未完了でMirroを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能完了確・初期ロでDの記述「変更データ取得 初期ロードで完了確認から」に対応する項目は再始動後の確認 REF15（変更デ・完了確・再始動）です。照合完了確・再始動に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで完了確認から Rowsapplied」で、確認対象は完了確・再始動・初期ロです。比較リフレ・再始動でA:の依存関係の確認 STAT13は「変更データ取得 通信で通信統計から」を述べるため、正答側の照合軸は変更デ・再始動・完了確です。運用再始動・変更デでB:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は完了確・リフレ・再始動です。項目完了確・再始動でC:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は初期ロ・リフレ・完了確です。用語完了確・再始動という用語は「変更データ取得 初期ロードで完了確認から」を指し、照合する値と誤認リスクの組合せはリフレ・完了確・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 再始動後の確認 REF15**

    - 検証目的: リフレッシュ制御のCDC Refreshについて再始動結果を検証し、REF15のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB15を指定し、REF15の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB15
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF15 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB15を指定し、REF15の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB15
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB15 Replication method Refresh Table APP.REF15 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB15 -t APP.REF15 -mを指定し、REF15の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB15 -t APP.REF15 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF15 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Table が画面・出力に表示されること
    ② ステップ2 の Refreshing が画面・出力に表示されること
    ③ ステップ3 の Replication が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 変更前の確認 REF02 {#c11-i0486}
*分類: リフレッシュ制御*  ・  難易度: 中級

変更前の確認では リフレッシュ制御 の 方式変更 を主操作として REF02 を判定します。変更対象と非対象の境界への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF02 に残します。変更前の確認を補助する 完了確認 では Rowsapplied を補助値として REF02 へ保存します。主判定の変更前の確認ではリフレッシュ制御の 方式変更 から Returnvalue を読み REF02 へ残します。証跡照合の変更前の確認ではリフレッシュ制御の Returnvalue と Rowsapplied を REF02 に保存します。記録対応の変更前の確認ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF02 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 変更前の確認 REF02に関する障害切り分けの前提を確認しています。性能統計 CDC Communications Activity 権限境界の確認の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は変更確認で方式変更を証跡に残し・変更データ取得 初期ロードで方式変更から。 ✅
    - B. 障害切り分けに用いる役割は権限境界確認でログ依存を証跡に残し・変更データ取得 通信でログ依存から Oldestdepend。
    - C. 障害切り分けに用いる役割は変更で再開条件を証跡に残し・後の表定義更新の項目の再開条件と取得時刻を記録し。
    - D. 障害切り分けに用いる役割は保護で複製位置を証跡に残し・Bookmarkの複製位置と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能方式変・初期ロでAの記述「変更データ取得 初期ロードで方式変更から」に対応する項目は変更前の確認 REF02（変更デ・方式変・変更確）です。照合方式変・変更確に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで方式変更から Returnvalue」で、確認対象は方式変・変更確・初期ロです。運用変更確・変更デでB:の権限境界の確認 STAT12は「変更データ取得 通信でログ依存から」を述べるため、正答側の照合軸は方式変・リフレ・変更確です。項目方式変・変更確でC:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は初期ロ・リフレ・方式変です。仕様方式変・変更確でD:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸は変更確・初期ロ・方式変です。用語方式変・変更確という用語は「変更データ取得 初期ロードで方式変更から」を指し、照合する値と誤認リスクの組合せはリフレ・方式変・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 変更前の確認 REF02**

    - 検証目的: リフレッシュ制御のCDC Refreshについて変更前の証跡を保存し、REF02のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB02 -t APP.REF02 -mを指定し、REF02の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB02 -t APP.REF02 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF02 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB02を指定し、REF02の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB02
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF02 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB02を指定し、REF02の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB02
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB02 Replication method Refresh Table APP.REF02 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Replication が画面・出力に表示されること
    ② ステップ2 の Table が画面・出力に表示されること
    ③ ステップ3 の Refreshing が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 変更後の確認 REF03 {#c11-i0487}
*分類: リフレッシュ制御*  ・  難易度: 中級

変更後の確認では リフレッシュ制御 の 完了確認 を主操作として REF03 を判定します。反映値と残存値への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF03 に残します。変更後の確認を補助する 方式表示 では Refreshing を補助値として REF03 へ保存します。主判定の変更後の確認ではリフレッシュ制御の 完了確認 から Rowsapplied を読み REF03 へ残します。証跡照合の変更後の確認ではリフレッシュ制御の Rowsapplied と Refreshing を REF03 に保存します。記録対応の変更後の確認ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF03 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 変更後の確認 REF03の設定や表示を読む前に役割を確認します。capture service 遅延監視 警告行ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは変更確認で完了確認を証跡に残し・変更データ取得 初期ロードで完了確認から。 ✅
    - B. 状態を読み取るための働きはリフレッシュで警告行を証跡に残し・ソース変更を読み取りサブスクリプションへ渡す処理を遅延監視と。
    - C. 状態を読み取るための働きは移行でインスタンスを証跡に残し・Hex Positionのインスタンス名と取得時刻を記録し。
    - D. 状態を読み取るための働きは解析で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能完了確・初期ロでAの記述「変更データ取得 初期ロードで完了確認から」に対応する項目は変更後の確認 REF03（変更デ・完了確・変更確）です。照合完了確・変更確に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで完了確認から Rowsapplied」で、確認対象は完了確・変更確・初期ロです。運用変更確・変更デでB:の遅延監視 警告行は「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸は完了確・リフレ・変更確です。項目完了確・変更確でC:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は初期ロ・リフレ・完了確です。仕様完了確・変更確でD:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は変更確・初期ロ・完了確です。用語完了確・変更確という用語は「変更データ取得 初期ロードで完了確認から」を指し、照合する値と誤認リスクの組合せはリフレ・完了確・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 変更後の確認 REF03**

    - 検証目的: リフレッシュ制御のCDC Refreshについて変更結果を検証し、REF03のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB03を指定し、REF03の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF03 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB03を指定し、REF03の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB03 Replication method Refresh Table APP.REF03 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB03 -t APP.REF03 -mを指定し、REF03の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB03 -t APP.REF03 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF03 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Table が画面・出力に表示されること
    ② ステップ2 の Refreshing が画面・出力に表示されること
    ③ ステップ3 の Replication が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 引継ぎ記録 REF09 {#c11-i0488}
*分類: リフレッシュ制御*  ・  難易度: 中級

引継ぎ記録では リフレッシュ制御 の 完了確認 を主操作として REF09 を判定します。次担当者が追跡できる証跡への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF09 に残します。引継ぎ記録を補助する 方式表示 では Refreshing を補助値として REF09 へ保存します。主判定の引継ぎ記録ではリフレッシュ制御の 完了確認 から Rowsapplied を読み REF09 へ残します。証跡照合の引継ぎ記録ではリフレッシュ制御の Rowsapplied と Refreshing を REF09 に保存します。記録対応の引継ぎ記録ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF09 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 引継ぎ記録 REF09を保守記録に説明する必要があります。bookmark マッピング検査 対象表と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は複製状態監視で対象表を確認することで対象表を確認し・対象表の誤読を防ぐ。
    - B. 運用時に利用する技術的役割は記録操作で証跡欄を照合することでサブスクリプを確認し・初期ロード未完了の見落としを防ぐ。CDCミラーリング Replication Method 0133固有の属性も確認対象に含める。
    - C. 運用時に利用する技術的役割は完了確認からRowsappliedを読むことで完了確認を確認し・初期ロード未完了でMirroを防ぐ。 ✅
    - D. 運用時に利用する技術的役割は調査操作で保守欄を引き継ぎすることでサブスクリプを確認し・ログ先頭未到達の見落としを防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能完了確・初期ロでCの記述「変更データ取得 初期ロードで完了確認から」に対応する項目は引継ぎ記録 REF09（変更デ・完了確・リフレ）です。照合完了確・リフレに関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで完了確認から Rowsapplied」で、確認対象は完了確・リフレ・初期ロです。比較リフレ・リフレでA:のマッピング検査 対象表は「ログ上の適用位置と時刻を追跡する複製の進行点」を述べるため、正答側の照合軸は変更デ・リフレ・完了確です。運用リフレ・変更デでB:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸は完了確・リフレ・リフレです。仕様完了確・リフレでD:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はリフレ・初期ロ・完了確です。用語完了確・リフレという用語は「変更データ取得 初期ロードで完了確認から」を指し、照合する値と誤認リスクの組合せはリフレ・完了確・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 引継ぎ記録 REF09**

    - 検証目的: リフレッシュ制御のCDC Refreshについて再現可能な記録を作成し、REF09のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB09を指定し、REF09の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF09 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB09を指定し、REF09の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB09 Replication method Refresh Table APP.REF09 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB09 -t APP.REF09 -mを指定し、REF09の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB09 -t APP.REF09 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF09 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Table が画面・出力に表示されること
    ② ステップ2 の Refreshing が画面・出力に表示されること
    ③ ステップ3 の Replication が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 復旧後の確認 REF06 {#c11-i0489}
*分類: リフレッシュ制御*  ・  難易度: 中級

復旧後の確認では リフレッシュ制御 の 完了確認 を主操作として REF06 を判定します。再発していないことを示す値への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF06 に残します。復旧後の確認を補助する 方式表示 では Refreshing を補助値として REF06 へ保存します。主判定の復旧後の確認ではリフレッシュ制御の 完了確認 から Rowsapplied を読み REF06 へ残します。証跡照合の復旧後の確認ではリフレッシュ制御の Rowsapplied と Refreshing を REF06 に保存します。記録対応の復旧後の確認ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF06 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 復旧後の確認 REF06の役割を調べています。refresh 失敗時切り分け 詳細表示の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては初期ロード未完了でMirrorへを避けるため・完了確認からRowsappliedを読むして完了確認を照合する。 ✅
    - B. 機能の説明としては詳細表示の誤読を避けるため・詳細表示で詳細表示を確認するして詳細表示を照合する。refresh 失敗時切り分け 詳細表示固有の属性も確認対象に含める。
    - C. 機能の説明としてはベンダー指示なしの位置変更を避けるため・主操作で出力欄を評価するしてサブスクリプを照合する。
    - D. 機能の説明としては表定義未更新を避けるため・点検操作で判定欄を記録するしてデータ定義対を照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能完了確・初期ロでAの記述「変更データ取得 初期ロードで完了確認から」に対応する項目は復旧後の確認 REF06（変更デ・完了確・復旧確）です。照合完了確・復旧確に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで完了確認から Rowsapplied」で、確認対象は完了確・復旧確・初期ロです。運用復旧確・変更デでB:の失敗時切り分け 詳細表示は「対象表を初期同期または再同期する複製操作を失」を述べるため、正答側の照合軸は完了確・リフレ・復旧確です。項目完了確・復旧確でC:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は初期ロ・リフレ・完了確です。仕様完了確・復旧確でD:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸は復旧確・初期ロ・完了確です。用語完了確・復旧確という用語は「変更データ取得 初期ロードで完了確認から」を指し、照合する値と誤認リスクの組合せはリフレ・完了確・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 復旧後の確認 REF06**

    - 検証目的: リフレッシュ制御のCDC Refreshについて復旧後の安定性を確認し、REF06のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB06を指定し、REF06の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF06 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB06を指定し、REF06の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB06 Replication method Refresh Table APP.REF06 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB06 -t APP.REF06 -mを指定し、REF06の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB06 -t APP.REF06 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF06 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Table が画面・出力に表示されること
    ② ステップ2 の Refreshing が画面・出力に表示されること
    ③ ステップ3 の Replication が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 復旧準備 REF05 {#c11-i0490}
*分類: リフレッシュ制御*  ・  難易度: 中級

復旧準備では リフレッシュ制御 の 方式変更 を主操作として REF05 を判定します。再開前に必要な整合性への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF05 に残します。復旧準備を補助する 完了確認 では Rowsapplied を補助値として REF05 へ保存します。主判定の復旧準備ではリフレッシュ制御の 方式変更 から Returnvalue を読み REF05 へ残します。証跡照合の復旧準備ではリフレッシュ制御の Returnvalue と Rowsapplied を REF05 に保存します。記録対応の復旧準備ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF05 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「リフレッシュ制御 CDC Refresh 復旧準備 REF05」を「エラー処理 CDC Event Log ログとの照合 ERR07」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はログとの照合でイベント一覧を証跡に残し・変更データ取得 イベントログでイベント一覧から 2931。
    - B. 仕様上の役割は診断で16進ブックを証跡に残し・サブスクリプションの16進ブックマークと取得時刻を記録し。
    - C. 仕様上の役割は解析で再開条件を証跡に残し・後の表定義更新の項目の再開条件と取得時刻を記録し。
    - D. 仕様上の役割は復旧準備で方式変更を証跡に残し・変更データ取得 初期ロードで方式変更から。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能方式変・初期ロでDの記述「変更データ取得 初期ロードで方式変更から」に対応する項目は復旧準備 REF05（変更デ・方式変・復旧準）です。照合方式変・復旧準に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで方式変更から Returnvalue」で、確認対象は方式変・復旧準・初期ロです。比較リフレ・復旧準でA:のログとの照合 ERR07は「変更データ取得 イベントログでイベント一覧か」を述べるため、正答側の照合軸は変更デ・復旧準・方式変です。運用復旧準・変更デでB:の複製位置管理 Subscriptは「サブスクリプションの16進ブックマークと取得」を述べるため、正答側の照合軸は方式変・リフレ・復旧準です。項目方式変・復旧準でC:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は初期ロ・リフレ・方式変です。用語方式変・復旧準という用語は「変更データ取得 初期ロードで方式変更から」を指し、照合する値と誤認リスクの組合せはリフレ・方式変・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 復旧準備 REF05**

    - 検証目的: リフレッシュ制御のCDC Refreshについて復旧条件を確認し、REF05のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB05 -t APP.REF05 -mを指定し、REF05の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB05 -t APP.REF05 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF05 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB05を指定し、REF05の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF05 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB05を指定し、REF05の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB05 Replication method Refresh Table APP.REF05 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Replication が画面・出力に表示されること
    ② ステップ2 の Table が画面・出力に表示されること
    ③ ステップ3 の Refreshing が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 性能影響の確認 REF11 {#c11-i0491}
*分類: リフレッシュ制御*  ・  難易度: 中級

性能影響の確認では リフレッシュ制御 の 方式変更 を主操作として REF11 を判定します。処理時間と滞留箇所への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF11 に残します。性能影響の確認を補助する 完了確認 では Rowsapplied を補助値として REF11 へ保存します。主判定の性能影響の確認ではリフレッシュ制御の 方式変更 から Returnvalue を読み REF11 へ残します。証跡照合の性能影響の確認ではリフレッシュ制御の Returnvalue と Rowsapplied を REF11 に保存します。記録対応の性能影響の確認ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF11 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 性能影響の確認 REF11の設定や表示を読む前に役割を確認します。エラー処理 CDC Event Log 代替経路の確認 ERR10ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は情報イベントと停止を伴うエラーをを避けるため・イベント一覧から2931を読むしてイベント一覧を照合する。
    - B. 一次資料が示す主目的は初期ロード未完了でMirrorへを避けるため・方式変更からReturnvalueを読むして方式変更を照合する。 ✅
    - C. 一次資料が示す主目的は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてミラー開始を照合する。CDCミラーリング Event Severity 0064固有の属性も確認対象に含める。
    - D. 一次資料が示す主目的は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてサブスクリプを照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能方式変・初期ロでBの記述「変更データ取得 初期ロードで方式変更から」に対応する項目は性能影響の確認 REF11（変更デ・方式変・性能影）です。照合方式変・性能影に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで方式変更から Returnvalue」で、確認対象は方式変・性能影・初期ロです。比較リフレ・性能影でA:の代替経路の確認 ERR10は「変更データ取得 イベントログでイベント一覧か」を述べるため、正答側の照合軸は変更デ・性能影・方式変です。項目方式変・性能影でC:のEvent Severityは「変更データ取得のミラー開始と取得時刻を記録し」を述べるため、正答側の照合軸は初期ロ・リフレ・方式変です。仕様方式変・性能影でD:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸は性能影・初期ロ・方式変です。用語方式変・性能影という用語は「変更データ取得 初期ロードで方式変更から」を指し、照合する値と誤認リスクの組合せはリフレ・方式変・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 性能影響の確認 REF11**

    - 検証目的: リフレッシュ制御のCDC Refreshについて負荷と待ちを確認し、REF11のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB11 -t APP.REF11 -mを指定し、REF11の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB11 -t APP.REF11 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF11 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB11を指定し、REF11の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB11
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF11 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB11を指定し、REF11の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB11
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB11 Replication method Refresh Table APP.REF11 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Replication が画面・出力に表示されること
    ② ステップ2 の Table が画面・出力に表示されること
    ③ ステップ3 の Refreshing が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 構成監査 REF08 {#c11-i0492}
*分類: リフレッシュ制御*  ・  難易度: 中級

構成監査では リフレッシュ制御 の 方式変更 を主操作として REF08 を判定します。定義値と稼働値の一致への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF08 に残します。構成監査を補助する 完了確認 では Rowsapplied を補助値として REF08 へ保存します。主判定の構成監査ではリフレッシュ制御の 方式変更 から Returnvalue を読み REF08 へ残します。証跡照合の構成監査ではリフレッシュ制御の Returnvalue と Rowsapplied を REF08 に保存します。記録対応の構成監査ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF08 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 構成監査 REF08の技術的な意味を資料で確認するとき、ログ依存・サポート Log Dependency 代替経路の確認 LOG10との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は構成監査で方式変更を証跡に残し・変更データ取得 初期ロードで方式変更から。 ✅
    - B. コマンドまたは機能の用途は代替経路確認で依存表示を証跡に残し・ログ依存で依存表示から Oldestrequired。
    - C. コマンドまたは機能の用途は保守で遅延確認を証跡に残し・変更データ取得の遅延確認と取得時刻を記録し。
    - D. コマンドまたは機能の用途は計画で初期ロード状を証跡に残し・変更データ取得の初期ロード状態と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能方式変・初期ロでAの記述「変更データ取得 初期ロードで方式変更から」に対応する項目は構成監査 REF08（変更デ・方式変・構成監）です。照合方式変・構成監に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで方式変更から Returnvalue」で、確認対象は方式変・構成監・初期ロです。運用構成監・変更デでB:の代替経路の確認 LOG10は「ログ依存で依存表示から Oldestrequ」を述べるため、正答側の照合軸は方式変・リフレ・構成監です。項目方式変・構成監でC:のCDCミラーリングは「変更データ取得の遅延確認と取得時刻を記録し」を述べるため、正答側の照合軸は初期ロ・リフレ・方式変です。仕様方式変・構成監でD:のTable Statusは「変更データ取得の初期ロード状態と取得時刻を記」を述べるため、正答側の照合軸は構成監・初期ロ・方式変です。用語方式変・構成監という用語は「変更データ取得 初期ロードで方式変更から」を指し、照合する値と誤認リスクの組合せはリフレ・方式変・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 構成監査 REF08**

    - 検証目的: リフレッシュ制御のCDC Refreshについて構成差分を監査し、REF08のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB08 -t APP.REF08 -mを指定し、REF08の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB08 -t APP.REF08 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF08 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB08を指定し、REF08の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF08 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB08を指定し、REF08の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB08 Replication method Refresh Table APP.REF08 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Replication が画面・出力に表示されること
    ② ステップ2 の Table が画面・出力に表示されること
    ③ ステップ3 の Refreshing が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 権限境界の確認 REF12 {#c11-i0493}
*分類: リフレッシュ制御*  ・  難易度: 中級

権限境界の確認では リフレッシュ制御 の 完了確認 を主操作として REF12 を判定します。参照操作と変更操作の分離への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF12 に残します。権限境界の確認を補助する 方式表示 では Refreshing を補助値として REF12 へ保存します。主判定の権限境界の確認ではリフレッシュ制御の 完了確認 から Rowsapplied を読み REF12 へ残します。証跡照合の権限境界の確認ではリフレッシュ制御の Rowsapplied と Refreshing を REF12 に保存します。記録対応の権限境界の確認ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF12 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 権限境界の確認 REF12を同一分類のrefresh 遅延監視 入力欄と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は対象表を初期同期または再同期する複製操作を遅延監視として確認する。マッピングで入力欄を確認するときは入力欄の誤読を防ぐ。
    - B. 構成を確認する際の意味は変更データ取得 初期ロードで完了確認から Rowsapplied を読み・Rowsapplied とである。完了確認からRowsappliedをときは初期ロード未完了でMirroを防ぐ。 ✅
    - C. 構成を確認する際の意味は後の表定義更新の項目のサブスクリプション記述と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。DDL後の表定義更新 Head of Log 0116固有の属性も確認対象に含める。
    - D. 構成を確認する際の意味は後の表定義更新の項目のログ先頭到達と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能完了確・初期ロでBの記述「変更データ取得 初期ロードで完了確認から」に対応する項目は権限境界の確認 REF12（変更デ・完了確・権限境）です。照合完了確・権限境に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで完了確認から Rowsapplied」で、確認対象は完了確・権限境・初期ロです。比較リフレ・権限境でA:の遅延監視 入力欄は「対象表を初期同期または再同期する複製操作を遅」を述べるため、正答側の照合軸は変更デ・権限境・完了確です。項目完了確・権限境でC:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は初期ロ・リフレ・完了確です。仕様完了確・権限境でD:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は権限境・初期ロ・完了確です。用語完了確・権限境という用語は「変更データ取得 初期ロードで完了確認から」を指し、照合する値と誤認リスクの組合せはリフレ・完了確・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 権限境界の確認 REF12**

    - 検証目的: リフレッシュ制御のCDC Refreshについて実行権限を点検し、REF12のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB12を指定し、REF12の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB12
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF12 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB12を指定し、REF12の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB12
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB12 Replication method Refresh Table APP.REF12 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB12 -t APP.REF12 -mを指定し、REF12の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB12 -t APP.REF12 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF12 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Table が画面・出力に表示されること
    ② ステップ2 の Refreshing が画面・出力に表示されること
    ③ ステップ3 の Replication が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 通常状態の確認 REF01 {#c11-i0494}
*分類: リフレッシュ制御*  ・  難易度: 中級

通常状態の確認では リフレッシュ制御 の 方式表示 を主操作として REF01 を判定します。基準値と現在値の差への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF01 に残します。通常状態の確認を補助する 方式変更 では Returnvalue を補助値として REF01 へ保存します。主判定の通常状態の確認ではリフレッシュ制御の 方式表示 から Refreshing を読み REF01 へ残します。証跡照合の通常状態の確認ではリフレッシュ制御の Refreshing と Returnvalue を REF01 に保存します。記録対応の通常状態の確認ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF01 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 通常状態の確認 REF01を保守記録に説明する必要があります。エラー処理 CDC Event Log 障害切り分け ERR04と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はエラー処理でイベント一覧を証跡に残し・変更データ取得 イベントログでイベント一覧から 2931。
    - B. 保守作業で参照する機能は保守で遅延確認を証跡に残し・変更データ取得の遅延確認と取得時刻を記録し。
    - C. 保守作業で参照する機能は保護でサブスクリプを証跡に残し・変更データ取得のサブスクリプション状態と取得時刻を記録し。
    - D. 保守作業で参照する機能は通常状態確認で方式表示を証跡に残し・変更データ取得 初期ロードで方式表示から 初期ロードing。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能方式表・初期ロでDの記述「変更データ取得 初期ロードで方式表示から」に対応する項目は通常状態の確認 REF01（変更デ・方式表・通常状）です。照合方式表・通常状に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで方式表示から 初期ロードing を読み」で、確認対象は方式表・通常状・初期ロです。比較リフレ・通常状でA:の障害切り分け ERR04は「変更データ取得 イベントログでイベント一覧か」を述べるため、正答側の照合軸は変更デ・通常状・方式表です。運用通常状・変更デでB:のCDCミラーリングは「変更データ取得の遅延確認と取得時刻を記録し」を述べるため、正答側の照合軸は方式表・リフレ・通常状です。項目方式表・通常状でC:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸は初期ロ・リフレ・方式表です。用語方式表・通常状という用語は「変更データ取得 初期ロードで方式表示から」を指し、照合する値と誤認リスクの組合せはリフレ・方式表・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 通常状態の確認 REF01**

    - 検証目的: リフレッシュ制御のCDC Refreshについて通常状態を確定し、REF01のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB01を指定し、REF01の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB01 Replication method Refresh Table APP.REF01 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB01 -t APP.REF01 -mを指定し、REF01の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB01 -t APP.REF01 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF01 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB01を指定し、REF01の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF01 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Refreshing が画面・出力に表示されること
    ② ステップ2 の Replication が画面・出力に表示されること
    ③ ステップ3 の Table が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 障害切り分け REF04 {#c11-i0495}
*分類: リフレッシュ制御*  ・  難易度: 中級

障害切り分けでは リフレッシュ制御 の 方式表示 を主操作として REF04 を判定します。最初に失敗した処理への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF04 に残します。障害切り分けを補助する 方式変更 では Returnvalue を補助値として REF04 へ保存します。主判定の障害切り分けではリフレッシュ制御の 方式表示 から Refreshing を読み REF04 へ残します。証跡照合の障害切り分けではリフレッシュ制御の Refreshing と Returnvalue を REF04 に保存します。記録対応の障害切り分けではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF04 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 障害切り分け REF04を同一分類のエラー処理 CDC Event Log 権限境界の確認 ERR12と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は変更データ取得 初期ロードで方式表示から 初期ロードing を読み・初期ロードing とである。方式表示から初期ロードingを読むときは初期ロード未完了でMirroを防ぐ。 ✅
    - B. 管理対象との関係を表す説明は変更データ取得 イベントログでサポート収集から Support を読み・Support と 2931である。サポート収集からSupportを読むときは情報イベントと停止を伴うエラを防ぐ。
    - C. 管理対象との関係を表す説明は変更データ取得の初期ロード状態と取得時刻を記録し・初期ロード未完了の見落としを防ぐである。記録操作で証跡欄を照合するときは初期ロード未完了の見落としを防ぐ。
    - D. 管理対象との関係を表す説明はBookmarkの複製位置と取得時刻を記録し・重複反映を防ぐである。変更確認操作で採取欄を棚卸するときは重複反映を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能方式表・初期ロでAの記述「変更データ取得 初期ロードで方式表示から」に対応する項目は障害切り分け REF04（変更デ・方式表・リフレ）です。照合方式表・リフレに関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで方式表示から 初期ロードing を読み」で、確認対象は方式表・リフレ・初期ロです。運用リフレ・変更デでB:の権限境界の確認 ERR12は「変更データ取得 イベントログでサポート収集か」を述べるため、正答側の照合軸は方式表・リフレ・リフレです。項目方式表・リフレでC:のTable Statusは「変更データ取得の初期ロード状態と取得時刻を記」を述べるため、正答側の照合軸は初期ロ・リフレ・方式表です。仕様方式表・リフレでD:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸はリフレ・初期ロ・方式表です。用語方式表・リフレという用語は「変更データ取得 初期ロードで方式表示から」を指し、照合する値と誤認リスクの組合せはリフレ・方式表・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 障害切り分け REF04**

    - 検証目的: リフレッシュ制御のCDC Refreshについて障害範囲を限定し、REF04のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB04を指定し、REF04の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB04 Replication method Refresh Table APP.REF04 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB04 -t APP.REF04 -mを指定し、REF04の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB04 -t APP.REF04 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF04 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB04を指定し、REF04の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF04 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Refreshing が画面・出力に表示されること
    ② ステップ2 の Replication が画面・出力に表示されること
    ③ ステップ3 の Table が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting




## IBM IIDR 11.4 > ログ依存・サポート

### ログ依存・サポート Log Dependency ログとの照合 LOG07 {#c11-i0496}
*分類: ログ依存・サポート*  ・  難易度: 上級

ログとの照合では ログ依存・サポート の 依存表示 を主操作として LOG07 を判定します。時刻と対象識別子への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG07 に残します。ログとの照合を補助する 購読確認 では Inactive を補助値として LOG07 へ保存します。主判定のログとの照合ではログ依存・サポートの 依存表示 から Oldestrequired を読み LOG07 へ残します。証跡照合のログとの照合ではログ依存・サポートの Oldestrequired と Inactive を LOG07 に保存します。記録対応のログとの照合ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG07 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency ログとの照合 LOG07を同一分類のcapture service マッピング検査 接続認証と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は接続認証の誤読を避けるため・エラー処理で接続認証を確認するして接続認証を照合する。
    - B. 管理対象との関係を表す説明は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてサブスクリプを照合する。
    - C. 管理対象との関係を表す説明は休止購読を見落として必要ログを削を避けるため・依存表示からOldestrequiredして依存表示を照合する。 ✅
    - D. 管理対象との関係を表す説明は別サブスクリプションを停止またはを避けるため・イベント表示からSeverityを読むしてイベント表示を照合する。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能依存表・休止購でCの記述「ログ依存で依存表示から Oldestrequired」に対応する項目はログとの照合 LOG07（ログ依・依存表・ログと）です。照合依存表・ログとに関するログ依存・サポートの仕様は「ログ依存で依存表示から Oldestrequired を読み」で、確認対象は依存表・ログと・休止購です。比較サポー・ログとでA:のマッピング検査 接続認証は「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸はログ依・ログと・依存表です。運用ログと・ログ依でB:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸は依存表・サポー・ログとです。仕様依存表・ログとでD:の停止前の確認 SUB14は「変更データ取得 サブスクリプションでイベント」を述べるため、正答側の照合軸はログと・休止購・依存表です。用語依存表・ログとという用語は「ログ依存で依存表示から Oldestrequired」を指し、照合する値と誤認リスクの組合せはサポー・依存表・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency ログとの照合 LOG07**

    - 検証目的: ログ依存・サポートのLog Dependencyについて操作とログを対応し、LOG07のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG07の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB07 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB07を指定し、LOG07の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB07
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB07 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG07.zipを指定し、LOG07の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG07.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG07.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Inactive が画面・出力に表示されること
    ③ ステップ3 の Support が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 代替経路の確認 LOG10 {#c11-i0497}
*分類: ログ依存・サポート*  ・  難易度: 上級

代替経路の確認では ログ依存・サポート の 依存表示 を主操作として LOG10 を判定します。主経路との役割差への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG10 に残します。代替経路の確認を補助する 購読確認 では Inactive を補助値として LOG10 へ保存します。主判定の代替経路の確認ではログ依存・サポートの 依存表示 から Oldestrequired を読み LOG10 へ残します。証跡照合の代替経路の確認ではログ依存・サポートの Oldestrequired と Inactive を LOG10 に保存します。記録対応の代替経路の確認ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG10 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 代替経路の確認 LOG10について構成や状態を確認します。apply task マッピング検査 保存場所ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはログ依存で依存表示から Oldestrequired を読み・Oldestrequired とである。依存表示からOldestrequirときは休止購読を見落として必要ログを防ぐ。 ✅
    - B. 対象資源に対する働きはターゲットへ変更を反映し適用済み位置を記録する処理をマッピング検査として確認する。データストアで保存場所を確認するときは保存場所の誤読を防ぐ。
    - C. 対象資源に対する働きは変更データ取得のイベントログと取得時刻を記録し・初期ロード未完了の見落としを防ぐである。記録操作で証跡欄を照合するときは初期ロード未完了の見落としを防ぐ。
    - D. 対象資源に対する働きはInstanceの戻り値と取得時刻を記録し・ベンダー指示なしの位置変更を防ぐである。主操作で出力欄を評価するときはベンダー指示なしの位置変更を防ぐ。複製位置管理 Instance 0333固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能依存表・休止購でAの記述「ログ依存で依存表示から Oldestrequired」に対応する項目は代替経路の確認 LOG10（ログ依・依存表・代替経）です。照合依存表・代替経に関するログ依存・サポートの仕様は「ログ依存で依存表示から Oldestrequired を読み」で、確認対象は依存表・代替経・休止購です。運用代替経・ログ依でB:のマッピング検査 保存場所は「ターゲットへ変更を反映し適用済み位置を記録す」を述べるため、正答側の照合軸は依存表・サポー・代替経です。項目依存表・代替経でC:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸は休止購・サポー・依存表です。仕様依存表・代替経でD:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は代替経・休止購・依存表です。用語依存表・代替経という用語は「ログ依存で依存表示から Oldestrequired」を指し、照合する値と誤認リスクの組合せはサポー・依存表・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 代替経路の確認 LOG10**

    - 検証目的: ログ依存・サポートのLog Dependencyについて代替手段の成立を確認し、LOG10のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG10の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB10 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB10を指定し、LOG10の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB10
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB10 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG10.zipを指定し、LOG10の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG10.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG10.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Inactive が画面・出力に表示されること
    ③ ステップ3 の Support が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 依存関係の確認 LOG13 {#c11-i0498}
*分類: ログ依存・サポート*  ・  難易度: 上級

依存関係の確認では ログ依存・サポート の 依存表示 を主操作として LOG13 を判定します。前提資源と後続処理の順序への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG13 に残します。依存関係の確認を補助する 購読確認 では Inactive を補助値として LOG13 へ保存します。主判定の依存関係の確認ではログ依存・サポートの 依存表示 から Oldestrequired を読み LOG13 へ残します。証跡照合の依存関係の確認ではログ依存・サポートの Oldestrequired と Inactive を LOG13 に保存します。記録対応の依存関係の確認ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG13 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 依存関係の確認 LOG13に関する障害切り分けの前提を確認しています。performance statistics ログ位置照合 集約結果の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はサブスクリプションやデータストアの処理量と遅延を測る情報である。ログ位置照合で集約結果を確認するときは集約結果の誤読を防ぐ。
    - B. 表示や設定で扱う内容はサブスクリプションの16進ブックマークと取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。複製位置管理 Subscription 0120固有の属性も確認対象に含める。
    - C. 表示や設定で扱う内容は変更データ取得 データストアでイベント確認から communication を読みである。イベント確認からcommunicatときはホスト名変更後の購読構成を更を防ぐ。
    - D. 表示や設定で扱う内容はログ依存で依存表示から Oldestrequired を読み・Oldestrequired とである。依存表示からOldestrequirときは休止購読を見落として必要ログを防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能依存表・休止購でDの記述「ログ依存で依存表示から Oldestrequired」に対応する項目は依存関係の確認 LOG13（ログ依・依存表・依存関）です。照合依存表・依存関に関するログ依存・サポートの仕様は「ログ依存で依存表示から Oldestrequired を読み」で、確認対象は依存表・依存関・休止購です。比較サポー・依存関でA:のログ位置照合 集約結果は「サブスクリプションやデータストアの処理量と遅」を述べるため、正答側の照合軸はログ依・依存関・依存表です。運用依存関・ログ依でB:の複製位置管理 Subscriptは「サブスクリプションの16進ブックマークと取得」を述べるため、正答側の照合軸は依存表・サポー・依存関です。項目依存表・依存関でC:の変更後の確認 STORE03は「変更データ取得 データストアでイベント確認か」を述べるため、正答側の照合軸は休止購・サポー・依存表です。用語依存表・依存関という用語は「ログ依存で依存表示から Oldestrequired」を指し、照合する値と誤認リスクの組合せはサポー・依存表・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 依存関係の確認 LOG13**

    - 検証目的: ログ依存・サポートのLog Dependencyについて依存資源を点検し、LOG13のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG13の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB13 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB13を指定し、LOG13の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB13
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB13 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG13.zipを指定し、LOG13の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG13.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG13.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Inactive が画面・出力に表示されること
    ③ ステップ3 の Support が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 停止前の確認 LOG14 {#c11-i0499}
*分類: ログ依存・サポート*  ・  難易度: 上級

停止前の確認では ログ依存・サポート の 購読確認 を主操作として LOG14 を判定します。処理中資源と未完了要求への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG14 に残します。停止前の確認を補助する 支援情報 では Returnvalue を補助値として LOG14 へ保存します。主判定の停止前の確認ではログ依存・サポートの 購読確認 から Inactive を読み LOG14 へ残します。証跡照合の停止前の確認ではログ依存・サポートの Inactive と Returnvalue を LOG14 に保存します。記録対応の停止前の確認ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG14 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 停止前の確認 LOG14の設定や表示を読む前に役割を確認します。replication mapping ログ位置照合 接続先ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はソース表とターゲット表の対応および列変換を示す定義である。ログ位置照合で接続先を確認するときは接続先の誤読を防ぐ。
    - B. 一次資料が示す主目的は変更データ取得のミラー開始と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。CDCミラーリング Event Severity 0124固有の属性も確認対象に含める。
    - C. 一次資料が示す主目的は後の表定義更新の項目の表定義再読込と取得時刻を記録し・初期ロード中の再開を防ぐである。表示操作で対象欄を追跡するときは初期ロード中の再開を防ぐ。
    - D. 一次資料が示す主目的はログ依存で購読確認から Inactive を読み・Inactive と Returnvalue を照合する。購読確認からInactiveを読むときは休止購読を見落として必要ログを防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能購読確・休止購でDの記述「ログ依存で購読確認から Inactive を読み」に対応する項目は停止前の確認 LOG14（ログ依・購読確・停止確）です。照合購読確・停止確に関するログ依存・サポートの仕様は「ログ依存で購読確認から Inactive を読み、Inactive」で、確認対象は購読確・停止確・休止購です。比較サポー・停止確でA:のログ位置照合 接続先は「ソース表とターゲット表の対応および列変換を示」を述べるため、正答側の照合軸はログ依・停止確・購読確です。運用停止確・ログ依でB:のEvent Severityは「変更データ取得のミラー開始と取得時刻を記録し」を述べるため、正答側の照合軸は購読確・サポー・停止確です。項目購読確・停止確でC:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は休止購・サポー・購読確です。用語購読確・停止確という用語は「ログ依存で購読確認から Inactive を読み」を指し、照合する値と誤認リスクの組合せはサポー・購読確・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 停止前の確認 LOG14**

    - 検証目的: ログ依存・サポートのLog Dependencyについて安全な停止条件を確認し、LOG14のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB14を指定し、LOG14の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB14
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB14 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG14.zipを指定し、LOG14の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG14.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG14.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG14の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB14 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Inactive が画面・出力に表示されること
    ② ステップ2 の Support が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 再始動後の確認 LOG15 {#c11-i0500}
*分類: ログ依存・サポート*  ・  難易度: 上級

再始動後の確認では ログ依存・サポート の 支援情報 を主操作として LOG15 を判定します。再開点と未処理データへの注意として「休止購読を見落として必要ログを削除する危険があります」を LOG15 に残します。再始動後の確認を補助する 依存表示 では Oldestrequired を補助値として LOG15 へ保存します。主判定の再始動後の確認ではログ依存・サポートの 支援情報 から Returnvalue を読み LOG15 へ残します。証跡照合の再始動後の確認ではログ依存・サポートの Returnvalue と Oldestrequired を LOG15 に保存します。記録対応の再始動後の確認ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG15 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 再始動後の確認 LOG15を同一分類のcapture service 開始位置指定 検査エンジンと比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はログ依存で支援情報から Returnvalue を読み・Returnvalue とである。支援情報からReturnvalueをときは休止購読を見落として必要ログを防ぐ。 ✅
    - B. 構成を確認する際の意味はソース変更を読み取りサブスクリプションへ渡す処理である。マッピングで検査エンジンを確認するときは検査エンジンの誤読を防ぐ。
    - C. 構成を確認する際の意味は後の表定義更新の項目のサブスクリプション記述と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。
    - D. 構成を確認する際の意味は変更データ取得 データストアでイベント確認から communication を読みである。イベント確認からcommunicatときはホスト名変更後の購読構成を更を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能支援情・休止購でAの記述「ログ依存で支援情報から Returnvalue を読み」に対応する項目は再始動後の確認 LOG15（ログ依・支援情・再始動）です。照合支援情・再始動に関するログ依存・サポートの仕様は「ログ依存で支援情報から Returnvalue を読み」で、確認対象は支援情・再始動・休止購です。運用再始動・ログ依でB:の開始位置指定 検査エンジンは「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸は支援情・サポー・再始動です。項目支援情・再始動でC:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は休止購・サポー・支援情です。仕様支援情・再始動でD:の引継ぎ記録 STORE09は「変更データ取得 データストアでイベント確認か」を述べるため、正答側の照合軸は再始動・休止購・支援情です。用語支援情・再始動という用語は「ログ依存で支援情報から Returnvalue」を指し、照合する値と誤認リスクの組合せはサポー・支援情・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 再始動後の確認 LOG15**

    - 検証目的: ログ依存・サポートのLog Dependencyについて再始動結果を検証し、LOG15のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG15.zipを指定し、LOG15の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG15.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG15.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG15の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB15 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB15を指定し、LOG15の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB15
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB15 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Support が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Inactive が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 変更前の確認 LOG02 {#c11-i0501}
*分類: ログ依存・サポート*  ・  難易度: 上級

変更前の確認では ログ依存・サポート の 購読確認 を主操作として LOG02 を判定します。変更対象と非対象の境界への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG02 に残します。変更前の確認を補助する 支援情報 では Returnvalue を補助値として LOG02 へ保存します。主判定の変更前の確認ではログ依存・サポートの 購読確認 から Inactive を読み LOG02 へ残します。証跡照合の変更前の確認ではログ依存・サポートの Inactive と Returnvalue を LOG02 に保存します。記録対応の変更前の確認ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG02 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 変更前の確認 LOG02について構成や状態を確認します。ログ依存・サポート Log Dependency 代替経路の確認 LOG10ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は代替経路確認で依存表示を証跡に残し・ログ依存で依存表示から Oldestrequired。
    - B. 一次資料が示す主目的は移行でサブスクリプを証跡に残し・変更データ取得のサブスクリプション状態と取得時刻を記録し。
    - C. 一次資料が示す主目的は変更確認で購読確認を証跡に残し・ログ依存で購読確認から Inactive を読み。 ✅
    - D. 一次資料が示す主目的は解析で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し・重複反映を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能購読確・休止購でCの記述「ログ依存で購読確認から Inactive を読み」に対応する項目は変更前の確認 LOG02（ログ依・購読確・変更確）です。照合購読確・変更確に関するログ依存・サポートの仕様は「ログ依存で購読確認から Inactive を読み、Inactive」で、確認対象は購読確・変更確・休止購です。比較サポー・変更確でA:の代替経路の確認 LOG10は「ログ依存で依存表示から Oldestrequ」を述べるため、正答側の照合軸はログ依・変更確・購読確です。運用変更確・ログ依でB:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸は購読確・サポー・変更確です。仕様購読確・変更確でD:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は変更確・休止購・購読確です。用語購読確・変更確という用語は「ログ依存で購読確認から Inactive を読み」を指し、照合する値と誤認リスクの組合せはサポー・購読確・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 変更前の確認 LOG02**

    - 検証目的: ログ依存・サポートのLog Dependencyについて変更前の証跡を保存し、LOG02のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB02を指定し、LOG02の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB02
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB02 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG02.zipを指定し、LOG02の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG02.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG02.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG02の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB02 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Inactive が画面・出力に表示されること
    ② ステップ2 の Support が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 変更後の確認 LOG03 {#c11-i0502}
*分類: ログ依存・サポート*  ・  難易度: 上級

変更後の確認では ログ依存・サポート の 支援情報 を主操作として LOG03 を判定します。反映値と残存値への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG03 に残します。変更後の確認を補助する 依存表示 では Oldestrequired を補助値として LOG03 へ保存します。主判定の変更後の確認ではログ依存・サポートの 支援情報 から Returnvalue を読み LOG03 へ残します。証跡照合の変更後の確認ではログ依存・サポートの Returnvalue と Oldestrequired を LOG03 に保存します。記録対応の変更後の確認ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG03 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 変更後の確認 LOG03の技術的な意味を資料で確認するとき、DDL後の表定義更新 Subscription 0002との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は点検操作で判定欄を記録することでログ先頭到達を確認し・表定義未更新を防ぐ。
    - B. 構成を確認する際の意味は主操作で出力欄を評価することで16進ブックを確認し・ベンダー指示なしの位置変更を防ぐ。複製位置管理 Subscription 0105固有の属性も確認対象に含める。
    - C. 構成を確認する際の意味は点検操作で判定欄を記録することでサブスクリプを確認し・表定義未更新を防ぐ。
    - D. 構成を確認する際の意味は支援情報からReturnvalueを読むことで支援情報を確認し・休止購読を見落として必要ログを防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能支援情・休止購でDの記述「ログ依存で支援情報から Returnvalue を読み」に対応する項目は変更後の確認 LOG03（ログ依・支援情・変更確）です。照合支援情・変更確に関するログ依存・サポートの仕様は「ログ依存で支援情報から Returnvalue を読み」で、確認対象は支援情・変更確・休止購です。比較サポー・変更確でA:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸はログ依・変更確・支援情です。運用変更確・ログ依でB:の複製位置管理 Subscriptは「サブスクリプションの16進ブックマークと取得」を述べるため、正答側の照合軸は支援情・サポー・変更確です。項目支援情・変更確でC:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は休止購・サポー・支援情です。用語支援情・変更確という用語は「ログ依存で支援情報から Returnvalue」を指し、照合する値と誤認リスクの組合せはサポー・支援情・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 変更後の確認 LOG03**

    - 検証目的: ログ依存・サポートのLog Dependencyについて変更結果を検証し、LOG03のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG03.zipを指定し、LOG03の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG03.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG03.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG03の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB03 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB03を指定し、LOG03の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB03 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Support が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Inactive が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 引継ぎ記録 LOG09 {#c11-i0503}
*分類: ログ依存・サポート*  ・  難易度: 上級

引継ぎ記録では ログ依存・サポート の 支援情報 を主操作として LOG09 を判定します。次担当者が追跡できる証跡への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG09 に残します。引継ぎ記録を補助する 依存表示 では Oldestrequired を補助値として LOG09 へ保存します。主判定の引継ぎ記録ではログ依存・サポートの 支援情報 から Returnvalue を読み LOG09 へ残します。証跡照合の引継ぎ記録ではログ依存・サポートの Returnvalue と Oldestrequired を LOG09 に保存します。記録対応の引継ぎ記録ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG09 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 引継ぎ記録 LOG09の役割を調べています。refresh 遅延監視 入力欄の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては支援情報からReturnvalueを読むことで支援情報を確認し・休止購読を見落として必要ログを防ぐ。 ✅
    - B. 機能の説明としてはマッピングで入力欄を確認することで入力欄を確認し・入力欄の誤読を防ぐ。
    - C. 機能の説明としては復旧操作で点検欄を確認することで再開条件を確認し・データ定義対象表の漏れを防ぐ。
    - D. 機能の説明としては記録操作で証跡欄を照合することでイベントログを確認し・初期ロード未完了の見落としを防ぐ。CDCミラーリング Subscription 0301固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能支援情・休止購でAの記述「ログ依存で支援情報から Returnvalue を読み」に対応する項目は引継ぎ記録 LOG09（ログ依・支援情・ログ依）です。照合支援情・ログ依に関するログ依存・サポートの仕様は「ログ依存で支援情報から Returnvalue を読み」で、確認対象は支援情・ログ依・休止購です。運用ログ依・ログ依でB:の遅延監視 入力欄は「対象表を初期同期または再同期する複製操作を遅」を述べるため、正答側の照合軸は支援情・サポー・ログ依です。項目支援情・ログ依でC:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は休止購・サポー・支援情です。仕様支援情・ログ依でD:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸はログ依・休止購・支援情です。用語支援情・ログ依という用語は「ログ依存で支援情報から Returnvalue」を指し、照合する値と誤認リスクの組合せはサポー・支援情・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 引継ぎ記録 LOG09**

    - 検証目的: ログ依存・サポートのLog Dependencyについて再現可能な記録を作成し、LOG09のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG09.zipを指定し、LOG09の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG09.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG09.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG09の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB09 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB09を指定し、LOG09の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB09 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Support が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Inactive が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 復旧後の確認 LOG06 {#c11-i0504}
*分類: ログ依存・サポート*  ・  難易度: 上級

復旧後の確認では ログ依存・サポート の 支援情報 を主操作として LOG06 を判定します。再発していないことを示す値への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG06 に残します。復旧後の確認を補助する 依存表示 では Oldestrequired を補助値として LOG06 へ保存します。主判定の復旧後の確認ではログ依存・サポートの 支援情報 から Returnvalue を読み LOG06 へ残します。証跡照合の復旧後の確認ではログ依存・サポートの Returnvalue と Oldestrequired を LOG06 に保存します。記録対応の復旧後の確認ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG06 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 復旧後の確認 LOG06の設定や表示を読む前に役割を確認します。refresh マッピング検査 管理レポートではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは復旧確認で支援情報を証跡に残し・ログ依存で支援情報から Returnvalue を読み。 ✅
    - B. 状態を読み取るための働きはリフレッシュで管理レポートを証跡に残し・対象表を初期同期または再同期する複製操作をマッピング検査とし。
    - C. 状態を読み取るための働きは収集で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し・データ欠落を防ぐ。
    - D. 状態を読み取るための働きは依存関係確認で定義表示を証跡に残し・変更データ取得 サブスクリプションで定義表示から。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能支援情・休止購でAの記述「ログ依存で支援情報から Returnvalue を読み」に対応する項目は復旧後の確認 LOG06（ログ依・支援情・復旧確）です。照合支援情・復旧確に関するログ依存・サポートの仕様は「ログ依存で支援情報から Returnvalue を読み」で、確認対象は支援情・復旧確・休止購です。運用復旧確・ログ依でB:のマッピング検査 管理レポートは「対象表を初期同期または再同期する複製操作をマ」を述べるため、正答側の照合軸は支援情・サポー・復旧確です。項目支援情・復旧確でC:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は休止購・サポー・支援情です。仕様支援情・復旧確でD:の依存関係の確認 SUB13は「変更データ取得 サブスクリプションで定義表示」を述べるため、正答側の照合軸は復旧確・休止購・支援情です。用語支援情・復旧確という用語は「ログ依存で支援情報から Returnvalue」を指し、照合する値と誤認リスクの組合せはサポー・支援情・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 復旧後の確認 LOG06**

    - 検証目的: ログ依存・サポートのLog Dependencyについて復旧後の安定性を確認し、LOG06のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG06.zipを指定し、LOG06の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG06.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG06.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG06の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB06 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB06を指定し、LOG06の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB06 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Support が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Inactive が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 復旧準備 LOG05 {#c11-i0505}
*分類: ログ依存・サポート*  ・  難易度: 上級

復旧準備では ログ依存・サポート の 購読確認 を主操作として LOG05 を判定します。再開前に必要な整合性への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG05 に残します。復旧準備を補助する 支援情報 では Returnvalue を補助値として LOG05 へ保存します。主判定の復旧準備ではログ依存・サポートの 購読確認 から Inactive を読み LOG05 へ残します。証跡照合の復旧準備ではログ依存・サポートの Inactive と Returnvalue を LOG05 に保存します。記録対応の復旧準備ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG05 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 復旧準備 LOG05に関する障害切り分けの前提を確認しています。datastore マッピング検査 オンライン表示の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はオンライン表でオンライン表を証跡に残し・CDC Replication が接続するソースまたはターゲ。
    - B. 障害切り分けに用いる役割は保守でログ先頭到達を証跡に残し・後の表定義更新の項目のログ先頭到達と取得時刻を記録し。
    - C. 障害切り分けに用いる役割は性能影響確認でイベント表示を証跡に残し・変更データ取得 サブスクリプションでイベント表示から。
    - D. 障害切り分けに用いる役割は復旧準備で購読確認を証跡に残し・ログ依存で購読確認から Inactive を読み。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能購読確・休止購でDの記述「ログ依存で購読確認から Inactive を読み」に対応する項目は復旧準備 LOG05（ログ依・購読確・復旧準）です。照合購読確・復旧準に関するログ依存・サポートの仕様は「ログ依存で購読確認から Inactive を読み、Inactive」で、確認対象は購読確・復旧準・休止購です。比較サポー・復旧準でA:のマッピング検査 オンライン表示は「CDC Replication」を述べるため、正答側の照合軸はログ依・復旧準・購読確です。運用復旧準・ログ依でB:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は購読確・サポー・復旧準です。項目購読確・復旧準でC:の性能影響の確認 SUB11は「変更データ取得 サブスクリプションでイベント」を述べるため、正答側の照合軸は休止購・サポー・購読確です。用語購読確・復旧準という用語は「ログ依存で購読確認から Inactive を読み」を指し、照合する値と誤認リスクの組合せはサポー・購読確・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 復旧準備 LOG05**

    - 検証目的: ログ依存・サポートのLog Dependencyについて復旧条件を確認し、LOG05のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB05を指定し、LOG05の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB05 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG05.zipを指定し、LOG05の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG05.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG05.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG05の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB05 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Inactive が画面・出力に表示されること
    ② ステップ2 の Support が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 性能影響の確認 LOG11 {#c11-i0506}
*分類: ログ依存・サポート*  ・  難易度: 上級

性能影響の確認では ログ依存・サポート の 購読確認 を主操作として LOG11 を判定します。処理時間と滞留箇所への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG11 に残します。性能影響の確認を補助する 支援情報 では Returnvalue を補助値として LOG11 へ保存します。主判定の性能影響の確認ではログ依存・サポートの 購読確認 から Inactive を読み LOG11 へ残します。証跡照合の性能影響の確認ではログ依存・サポートの Inactive と Returnvalue を LOG11 に保存します。記録対応の性能影響の確認ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG11 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 性能影響の確認 LOG11の技術的な意味を資料で確認するとき、datastore 状態確認 イベント識別との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は状態確認でイベント識別を証跡に残し・CDC Replication が接続するソースまたはターゲ。
    - B. コマンドまたは機能の用途は切替でサブスクリプを証跡に残し・後の表定義更新の項目のサブスクリプション記述と取得時刻を記録。
    - C. コマンドまたは機能の用途は性能影響確認で購読確認を証跡に残し・ログ依存で購読確認から Inactive を読み。 ✅
    - D. コマンドまたは機能の用途は変更確認でイベント表示を証跡に残し・変更データ取得 サブスクリプションでイベント表示から。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能購読確・休止購でCの記述「ログ依存で購読確認から Inactive を読み」に対応する項目は性能影響の確認 LOG11（ログ依・購読確・性能影）です。照合購読確・性能影に関するログ依存・サポートの仕様は「ログ依存で購読確認から Inactive を読み、Inactive」で、確認対象は購読確・性能影・休止購です。比較サポー・性能影でA:の状態確認 イベント識別は「CDC Replication」を述べるため、正答側の照合軸はログ依・性能影・購読確です。運用性能影・ログ依でB:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は購読確・サポー・性能影です。仕様購読確・性能影でD:の変更前の確認 SUB02は「変更データ取得 サブスクリプションでイベント」を述べるため、正答側の照合軸は性能影・休止購・購読確です。用語購読確・性能影という用語は「ログ依存で購読確認から Inactive を読み」を指し、照合する値と誤認リスクの組合せはサポー・購読確・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 性能影響の確認 LOG11**

    - 検証目的: ログ依存・サポートのLog Dependencyについて負荷と待ちを確認し、LOG11のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB11を指定し、LOG11の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB11
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB11 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG11.zipを指定し、LOG11の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG11.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG11.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG11の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB11 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Inactive が画面・出力に表示されること
    ② ステップ2 の Support が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 構成監査 LOG08 {#c11-i0507}
*分類: ログ依存・サポート*  ・  難易度: 上級

構成監査では ログ依存・サポート の 購読確認 を主操作として LOG08 を判定します。定義値と稼働値の一致への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG08 に残します。構成監査を補助する 支援情報 では Returnvalue を補助値として LOG08 へ保存します。主判定の構成監査ではログ依存・サポートの 購読確認 から Inactive を読み LOG08 へ残します。証跡照合の構成監査ではログ依存・サポートの Inactive と Returnvalue を LOG08 に保存します。記録対応の構成監査ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG08 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「ログ依存・サポート Log Dependency 構成監査 LOG08」を「refresh 開始位置指定 同期範囲」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はサブスクリプで同期範囲を証跡に残し・対象表を初期同期または再同期する複製操作。
    - B. 仕様上の役割は構成監査で購読確認を証跡に残し・ログ依存で購読確認から Inactive を読み。 ✅
    - C. 仕様上の役割は診断でイベントログを証跡に残し・変更データ取得のイベントログと取得時刻を記録し。
    - D. 仕様上の役割は計画で複製位置を証跡に残し・Bookmarkの複製位置と取得時刻を記録し。複製位置管理 Bookmark 0339固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能購読確・休止購でBの記述「ログ依存で購読確認から Inactive を読み」に対応する項目は構成監査 LOG08（ログ依・購読確・構成監）です。照合購読確・構成監に関するログ依存・サポートの仕様は「ログ依存で購読確認から Inactive を読み、Inactive」で、確認対象は購読確・構成監・休止購です。比較サポー・構成監でA:の開始位置指定 同期範囲は「対象表を初期同期または再同期する複製操作」を述べるため、正答側の照合軸はログ依・構成監・購読確です。項目購読確・構成監でC:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸は休止購・サポー・購読確です。仕様購読確・構成監でD:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸は構成監・休止購・購読確です。用語購読確・構成監という用語は「ログ依存で購読確認から Inactive を読み」を指し、照合する値と誤認リスクの組合せはサポー・購読確・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 構成監査 LOG08**

    - 検証目的: ログ依存・サポートのLog Dependencyについて構成差分を監査し、LOG08のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB08を指定し、LOG08の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB08 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG08.zipを指定し、LOG08の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG08.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG08.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG08の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB08 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Inactive が画面・出力に表示されること
    ② ステップ2 の Support が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 権限境界の確認 LOG12 {#c11-i0508}
*分類: ログ依存・サポート*  ・  難易度: 上級

権限境界の確認では ログ依存・サポート の 支援情報 を主操作として LOG12 を判定します。参照操作と変更操作の分離への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG12 に残します。権限境界の確認を補助する 依存表示 では Oldestrequired を補助値として LOG12 へ保存します。主判定の権限境界の確認ではログ依存・サポートの 支援情報 から Returnvalue を読み LOG12 へ残します。証跡照合の権限境界の確認ではログ依存・サポートの Returnvalue と Oldestrequired を LOG12 に保存します。記録対応の権限境界の確認ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG12 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 権限境界の確認 LOG12を保守記録に説明する必要があります。CDCミラーリング Event Severity 0004と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてミラー開始を照合する。
    - B. 運用時に利用する技術的役割は休止購読を見落として必要ログを削を避けるため・支援情報からReturnvalueを読むして支援情報を照合する。 ✅
    - C. 運用時に利用する技術的役割は表定義未更新を避けるため・点検操作で判定欄を記録するしてデータ定義対を照合する。
    - D. 運用時に利用する技術的役割は別サブスクリプションを停止またはを避けるため・イベント表示からSeverityを読むしてイベント表示を照合する。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能支援情・休止購でBの記述「ログ依存で支援情報から Returnvalue を読み」に対応する項目は権限境界の確認 LOG12（ログ依・支援情・権限境）です。照合支援情・権限境に関するログ依存・サポートの仕様は「ログ依存で支援情報から Returnvalue を読み」で、確認対象は支援情・権限境・休止購です。比較サポー・権限境でA:のEvent Severityは「変更データ取得のミラー開始と取得時刻を記録し」を述べるため、正答側の照合軸はログ依・権限境・支援情です。項目支援情・権限境でC:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸は休止購・サポー・支援情です。仕様支援情・権限境でD:の変更前の確認 SUB02は「変更データ取得 サブスクリプションでイベント」を述べるため、正答側の照合軸は権限境・休止購・支援情です。用語支援情・権限境という用語は「ログ依存で支援情報から Returnvalue」を指し、照合する値と誤認リスクの組合せはサポー・支援情・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 権限境界の確認 LOG12**

    - 検証目的: ログ依存・サポートのLog Dependencyについて実行権限を点検し、LOG12のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG12.zipを指定し、LOG12の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG12.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG12.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG12の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB12 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB12を指定し、LOG12の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB12
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB12 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Support が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Inactive が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 通常状態の確認 LOG01 {#c11-i0509}
*分類: ログ依存・サポート*  ・  難易度: 上級

通常状態の確認では ログ依存・サポート の 依存表示 を主操作として LOG01 を判定します。基準値と現在値の差への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG01 に残します。通常状態の確認を補助する 購読確認 では Inactive を補助値として LOG01 へ保存します。主判定の通常状態の確認ではログ依存・サポートの 依存表示 から Oldestrequired を読み LOG01 へ残します。証跡照合の通常状態の確認ではログ依存・サポートの Oldestrequired と Inactive を LOG01 に保存します。記録対応の通常状態の確認ではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG01 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 通常状態の確認 LOG01の役割を調べています。複製位置管理 Instance 0003の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はInstanceの戻り値と取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。
    - B. 表示や設定で扱う内容はログ依存で依存表示から Oldestrequired を読み・Oldestrequired とである。依存表示からOldestrequirときは休止購読を見落として必要ログを防ぐ。 ✅
    - C. 表示や設定で扱う内容はBookmarkの複製位置と取得時刻を記録し・重複反映を防ぐである。変更確認操作で採取欄を棚卸するときは重複反映を防ぐ。
    - D. 表示や設定で扱う内容は変更データ取得 サブスクリプションで版数表示から Replication を読み・Replicationである。版数表示からReplicationをときは別サブスクリプションを停止まを防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能依存表・休止購でBの記述「ログ依存で依存表示から Oldestrequired」に対応する項目は通常状態の確認 LOG01（ログ依・依存表・通常状）です。照合依存表・通常状に関するログ依存・サポートの仕様は「ログ依存で依存表示から Oldestrequired を読み」で、確認対象は依存表・通常状・休止購です。比較サポー・通常状でA:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸はログ依・通常状・依存表です。項目依存表・通常状でC:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸は休止購・サポー・依存表です。仕様依存表・通常状でD:の再始動後の確認 SUB15は「変更データ取得 サブスクリプションで版数表示」を述べるため、正答側の照合軸は通常状・休止購・依存表です。用語依存表・通常状という用語は「ログ依存で依存表示から Oldestrequired」を指し、照合する値と誤認リスクの組合せはサポー・依存表・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 通常状態の確認 LOG01**

    - 検証目的: ログ依存・サポートのLog Dependencyについて通常状態を確定し、LOG01のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG01の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB01 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB01を指定し、LOG01の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB01 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG01.zipを指定し、LOG01の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG01.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG01.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Inactive が画面・出力に表示されること
    ③ ステップ3 の Support が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### ログ依存・サポート Log Dependency 障害切り分け LOG04 {#c11-i0510}
*分類: ログ依存・サポート*  ・  難易度: 上級

障害切り分けでは ログ依存・サポート の 依存表示 を主操作として LOG04 を判定します。最初に失敗した処理への注意として「休止購読を見落として必要ログを削除する危険があります」を LOG04 に残します。障害切り分けを補助する 購読確認 では Inactive を補助値として LOG04 へ保存します。主判定の障害切り分けではログ依存・サポートの 依存表示 から Oldestrequired を読み LOG04 へ残します。証跡照合の障害切り分けではログ依存・サポートの Oldestrequired と Inactive を LOG04 に保存します。記録対応の障害切り分けではログ依存・サポートの Oldest LogとSubscription の証跡へ LOG04 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** ログ依存・サポート Log Dependency 障害切り分け LOG04を保守記録に説明する必要があります。apply task 初期同期判定 応答行と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は応答行の誤読を避けるため・初期同期判定で応答行を確認するして応答行を照合する。
    - B. 保守作業で参照する機能は休止購読を見落として必要ログを削を避けるため・依存表示からOldestrequiredして依存表示を照合する。 ✅
    - C. 保守作業で参照する機能はログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするしてデータ定義対を照合する。
    - D. 保守作業で参照する機能は重複反映を避けるため・変更確認操作で採取欄を棚卸するして複製位置を照合する。複製位置管理 Bookmark 0354固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能依存表・休止購でBの記述「ログ依存で依存表示から Oldestrequired」に対応する項目は障害切り分け LOG04（ログ依・依存表・ログ依）です。照合依存表・ログ依に関するログ依存・サポートの仕様は「ログ依存で依存表示から Oldestrequired を読み」で、確認対象は依存表・ログ依・休止購です。比較サポー・ログ依でA:の初期同期判定 応答行は「ターゲットへ変更を反映し適用済み位置を記録す」を述べるため、正答側の照合軸はログ依・ログ依・依存表です。項目依存表・ログ依でC:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸は休止購・サポー・依存表です。仕様依存表・ログ依でD:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸はログ依・休止購・依存表です。用語依存表・ログ依という用語は「ログ依存で依存表示から Oldestrequired」を指し、照合する値と誤認リスクの組合せはサポー・依存表・休止購です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **ログ依存・サポート Log Dependency 障害切り分け LOG04**

    - 検証目的: ログ依存・サポートのLog Dependencyについて障害範囲を限定し、LOG04のOldest LogとSubscriptionを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象LOG04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、LOG04の依存表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription | Oldest required log | Reason
    SUB04 | S0001842.LOG | Mirroring stopped
    TESTSUB | S0001720.LOG | Inactive subscription
    ```

    画面・出力にあるSubscriptionを読み、Oldest LogとSubscriptionと対象LOG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB04を指定し、LOG04の購読確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB04 Replication method Mirror Status Inactive Mapped tables 24
    ```

    画面・出力にあるInactiveを読み、Oldest LogとSubscriptionと対象LOG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のログ依存・サポートを確認する入力画面です。COMMAND入力口へdmsupportinfo -I SRC1 -o /tmp/LOG04.zipを指定し、LOG04の支援情報を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsupportinfo -I SRC1 -o /tmp/LOG04.zip
    → Enter を押す
    ```

    画面・出力:
    ```text
    Support information collection completed: /tmp/LOG04.zip Return value 0.
    ```

    画面・出力にあるSupportを読み、Oldest LogとSubscriptionと対象LOG04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Inactive が画面・出力に表示されること
    ③ ステップ3 の Support が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting




## IBM IIDR 11.4 > 性能統計

### CHC0368I マッピング検査 セッション上限 {#c11-i0511}
*分類: 性能統計*  ・  難易度: 上級

IBM IIDR 11.4 の 性能統計 で扱う「CHC0368I マッピング検査 セッション上限」は、bookmark まで適用したことを示す CDC Replication メッセージをマッピング検査の観点で確認する技術項目です。replication mapping 名とDS070を同じ記録で見比べることで、開始位置の取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** CHC0368I マッピング検査 セッション上限に関する障害切り分けの前提を確認しています。複製位置管理 Instance 0048の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は対象インスタンスの取り違えを避けるため・照合操作で確認欄を採取するして戻り値を照合する。
    - B. 障害切り分けに用いる役割は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてサブスクリプを照合する。
    - C. 障害切り分けに用いる役割は情報イベントと停止を伴うエラーをを避けるため・サポート収集からSupportを読むしてサポート収集を照合する。
    - D. 障害切り分けに用いる役割はセッション上の誤読を避けるため・性能統計でセッション上を確認するしてセッション上を照合する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 性能・セッシ・セッショでDの記述「bookmark まで適用したことを示す CDC」に対応する項目はマッピング検査 セッション上限（マッピ・セッシ・セッショ・性能統）です。性能統計時のセッションに関する性能統計の仕様は「bookmark まで適用したことを示す CDC」で、確認対象はマッピ・セッシ・セッショ・性能統です。In・復旧・戻り値のA:は「Instanceの戻り値と取得時刻を記録し」を述べ、対象は複製位置管理 Instance（Ins・戻り値・対象イン・復旧）です。切替・サブス・遅延ゼロのB:は「CDCのサブスクリプション状態と取得時刻を記録し」を述べ、対象はReplication Method（ミラー・サブス・遅延ゼロ・切替）です。エラー処時のサポート収のC:は「CDC Event Logでサポート収集からSupportを読み」を述べ、対象は引継ぎ記録 ERR09（CDC・サポー・情報イベ・エラー）です。セッションを性能統計という用語は「bookmark まで適用したことを示す CDC」を指し、マッピング検査 セッション上限（マッピ・セッシ・セッショ・性能統）で照合する値はセッション上です。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **CHC0368I マッピング検査 セッション上限**

    - 検証目的: 性能統計のCHC0368I マッピング検査 セッション上限について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、性能統計の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。replication mapping 名を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB070           DS070          Mirroring   BMK070
    ```

    画面・出力には Subscription が含まれ、CHC0368I マッピング検査 セッション上限の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、開始位置の取り違えを切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB070           DS070          BMK070
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### CHC0368I 統計採取 統計値 {#c11-i0512}
*分類: 性能統計*  ・  難易度: 中級

IBM IIDR 11.4 の 性能統計 で扱う「CHC0368I 統計採取 統計値」は、bookmark まで適用したことを示す CDC Replication メッセージを統計採取の観点で確認する技術項目です。replication mapping 名とDS030を同じ記録で見比べることで、開始位置の取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** CHC0368I 統計採取 統計値に関する障害切り分けの前提を確認しています。apply task 失敗時切り分け 例外記録の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は複製状態監視で例外記録を確認することで例外記録を確認し・例外記録の誤読を防ぐ。
    - B. 表示や設定で扱う内容は調査操作で保守欄を引き継ぎすることで表定義再読込を確認し・ログ先頭未到達の見落としを防ぐ。
    - C. 表示や設定で扱う内容は変更確認で確認ではサブを確認することで確認ではサブを確認し・別サブスクリプションを停止まを防ぐ。
    - D. 表示や設定で扱う内容は統計採取で統計値を確認することで統計値を確認し・統計値の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 統計採取対象統計採取でDの記述「bookmark まで適用したことを示す CDC」に対応する項目は統計採取 統計値（統計採取・統計採・統計値・統計値の）です。統計採取時の統計採取に関する性能統計の仕様は「bookmark まで適用したことを示す CDC」で、確認対象は統計採取・統計採・統計値・統計値のです。apply・複製状態監のA:は「ターゲットへ変更を反映し適用済み位置を記録する処理を失敗時切り分けと」を述べ、対象は失敗時切り分け 例外記録（apply・複製状・例外記・例外記録）です。登録対象後の表定義のB:は「DDLの表定義再読込と取得時刻を記録し、ログ先頭未到達の見落としを防」を述べ、対象はSource Table（後の表定義・登録・表定義・ログ先頭）です。変更確認時のCDCのC:は「CDC Subscriptionで変更後の確認ではサブスクリプション」を述べ、対象は変更後の確認 SUB03（CDC・変更確・確認で・別サブス）です。統計採取を統計採取という用語は「bookmark まで適用したことを示す CDC」を指し、統計採取 統計値（統計採取・統計採・統計値・統計値の）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **CHC0368I 統計採取 統計値**

    - 検証目的: 性能統計のCHC0368I 統計採取 統計値について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、性能統計の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。replication mapping 名を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB030           DS030          Mirroring   BMK030
    ```

    画面・出力には Subscription が含まれ、CHC0368I 統計採取 統計値の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、開始位置の取り違えを切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB030           DS030          BMK030
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### apply task 初期同期判定 応答行 {#c11-i0513}
*分類: 性能統計*  ・  難易度: 初級

IBM IIDR 11.4 の 性能統計 で扱う「apply task 初期同期判定 応答行」は、ターゲットへ変更を反映し適用済み位置を記録する処理を初期同期判定の観点で確認する技術項目です。list subscriptions の表とBMK006を同じ記録で見比べることで、適用遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** apply task 初期同期判定 応答行に関する障害切り分けの前提を確認しています。capture service ログ位置照合 キーマップの機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はキーマップの誤読を避けるため・ログ位置照合でキーマップを確認するしてキーマップを照合する。
    - B. 表示や設定で扱う内容はRefresh中の再開を避けるため・表示操作で対象欄を追跡するしてDDL対象表を照合する。
    - C. 表示や設定で扱う内容はIBM指示なしの位置変更を避けるため・主操作で出力欄を評価するして複製位置を照合する。
    - D. 表示や設定で扱う内容は応答行の誤読を避けるため・初期同期判定で応答行を確認するして応答行を照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 初期同期対象applyでDの記述「ターゲットへ変更を反映し適用済み位置を記録する処理を初期同期判定とし」に対応する項目は初期同期判定 応答行（apply・初期同・応答行・応答行の）です。初期同期時のapplyに関する性能統計の仕様は「ターゲットへ変更を反映し適用済み位置を記録する処理を初期同期判定とし」で、確認対象はappl・初期同・応答行・応答行のです。captu・ログ位置照のA:は「ソース変更を読み取りサブスクリプションへ渡す処理」を述べ、対象はログ位置照合 キーマップ（captu・ログ位・キーマ・キーマッ）です。切替対象後の表定義のB:は「DDLのDDL対象表と取得時刻を記録し、Refresh中の再開を防ぐ」を述べ、対象はTable Definition（後の表定義・切替・DDL・Refr）です。解析時のBookmのC:は「Bookmarkの複製位置と取得時刻を記録し」を述べ、対象は複製位置管理 Bookmark（Bookm・解析・複製位・IBM指）です。applを初期同期判という用語は「ターゲットへ変更を反映し適用済み位置を記録する処理を」を指し、初期同期判定 応答行（apply・初期同・応答行・応答行の）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **apply task 初期同期判定 応答行**

    - 検証目的: 性能統計のapply task 初期同期判定 応答行について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、性能統計の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。list subscriptions の表を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB006           DS006          Mirroring   BMK006
    ```

    画面・出力には Subscription が含まれ、apply task 初期同期判定 応答行の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、適用遅延を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB006           DS006          BMK006
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### apply task 開始位置指定 活動ログ {#c11-i0514}
*分類: 性能統計*  ・  難易度: 中級

IBM IIDR 11.4 の 性能統計 で扱う「apply task 開始位置指定 活動ログ」は、ターゲットへ変更を反映し適用済み位置を記録する処理を開始位置指定の観点で確認する技術項目です。list subscriptions の表とBMK046を同じ記録で見比べることで、適用遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** apply task 開始位置指定 活動ログに関する障害切り分けの前提を確認しています。DDL後の表定義更新 Subscription 0032の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は調査操作で保守欄を引き継ぎすることでログ先頭到達を確認し・ログ先頭未到達の見落としを防ぐ。
    - B. 障害切り分けに用いる役割は性能統計で活動ログを確認することで活動ログを確認し・活動ログの誤読を防ぐ。 ✅
    - C. 障害切り分けに用いる役割は調査操作で保守欄を引き継ぎすることで再開条件を確認し・ログ先頭未到達の見落としを防ぐ。
    - D. 障害切り分けに用いる役割は構成監査で構成監査ではを確認することで構成監査ではを確認し・Refresh未完了でMirを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 性能統計対象applyでBの記述「ターゲットへ変更を反映し適用済み位置を記録する処理である」に対応する項目は開始位置指定 活動ログ（apply・性能統・活動ロ・活動ログ）です。性能統計時のapplyに関する性能統計の仕様は「ターゲットへ変更を反映し適用済み位置を記録する処理」で、確認対象はappl・性能統・活動ロ・活動ログです。後の表定義・棚卸のA:は「DDLのログ先頭到達と取得時刻を記録し、ログ先頭未到達の見落としを防」を述べ、対象はDDL後の表定義更新（後の表定義・棚卸・ログ先・ログ先頭）です。収集時の後の表定義のC:は「DDLの再開条件と取得時刻を記録し、ログ先頭未到達の見落としを防ぐ」を述べ、対象はRefresh Table（後の表定義・収集・再開条・ログ先頭）です。構成監査でを構成監査のD:は「CDC Refreshで構成監査ではリフレッシュ制御の」を述べ、対象は構成監査 REF08（CDC・構成監・構成監・Refr）です。applを性能統計という用語は「ターゲットへ変更を反映し適用済み位置を記録する処理」を指し、開始位置指定 活動ログ（apply・性能統・活動ロ・活動ログ）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **apply task 開始位置指定 活動ログ**

    - 検証目的: 性能統計のapply task 開始位置指定 活動ログについて、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、性能統計の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。list subscriptions の表を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB046           DS046          Mirroring   BMK046
    ```

    画面・出力には Subscription が含まれ、apply task 開始位置指定 活動ログの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、適用遅延を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB046           DS046          BMK046
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### bookmark ログ位置照合 伝搬経路 {#c11-i0515}
*分類: 性能統計*  ・  難易度: 中級

IBM IIDR 11.4 の 性能統計 で扱う「bookmark ログ位置照合 伝搬経路」は、ログ上の適用位置と時刻を追跡する複製の進行点をログ位置照合の観点で確認する技術項目です。target datastore の統計とSUB054を同じ記録で見比べることで、再同期範囲の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** bookmark ログ位置照合 伝搬経路に関する障害切り分けの前提を確認しています。複製位置管理 Locale 0027の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はログ位置照合で伝搬経路を確認することで伝搬経路を確認し・伝搬経路の誤読を防ぐ。 ✅
    - B. 表示や設定で扱う内容は監査操作で記録欄を比較することでサブスクリプを確認し・データ欠落を防ぐ。
    - C. 表示や設定で扱う内容は確認操作で状態欄を整理することでサブスクリプを確認し・遅延ゼロ確認の欠落を防ぐ。
    - D. 表示や設定で扱う内容は状態表示からLatencyを読むことで状態表示を確認し・Refresh中の表をMirを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** ログ・伝搬経・伝搬経路でAの記述「ログ上の適用位置と時刻を追跡する複製の進行点である」に対応する項目はログ位置照合 伝搬経路（boo・伝搬経・伝搬経路・ログ位）です。ログ位置時の伝搬経路に関する性能統計の仕様は「ログ上の適用位置と時刻を追跡する複製の進行点」で、確認対象はboo・伝搬経・伝搬経路・ログ位です。棚卸・サブス・データ欠のB:は「Localeのサブスクリプション名と取得時刻を記録し」を述べ、対象は複製位置管理 Locale（Loc・サブス・データ欠・棚卸）です。切替時のサブスクリのC:は「CDCのサブスクリプション状態と取得時刻を記録し」を述べ、対象はReplication Method（ミラー・サブス・遅延ゼロ・切替）です。状態表示を通常状態確のD:は「Mirror Statusで状態表示からLatencyを読み」を述べ、対象は通常状態の確認 MIR01（Mir・状態表・Refr・通常状）です。伝搬経路をログ位置照という用語は「ログ上の適用位置と時刻を追跡する複製の進行点」を指し、ログ位置照合 伝搬経路（boo・伝搬経・伝搬経路・ログ位）で照合する値は伝搬経路です。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **bookmark ログ位置照合 伝搬経路**

    - 検証目的: 性能統計のbookmark ログ位置照合 伝搬経路について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、性能統計の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。target datastore の統計を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB054           DS054          Mirroring   BMK054
    ```

    画面・出力には Subscription が含まれ、bookmark ログ位置照合 伝搬経路の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、再同期範囲の誤認を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB054           DS054          BMK054
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### bookmark 失敗時切り分け 実行結果 {#c11-i0516}
*分類: 性能統計*  ・  難易度: 初級

IBM IIDR 11.4 の 性能統計 で扱う「bookmark 失敗時切り分け 実行結果」は、ログ上の適用位置と時刻を追跡する複製の進行点を失敗時切り分けの観点で確認する技術項目です。target datastore の統計とSUB014を同じ記録で見比べることで、再同期範囲の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** bookmark 失敗時切り分け 実行結果に関する障害切り分けの前提を確認しています。subscription 開始位置指定 遅延表示の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては遅延表示の誤読を避けるため・遅延表示で遅延表示を確認するして遅延表示を照合する。
    - B. 機能の説明としては対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてミラー開始を照合する。
    - C. 機能の説明としては実行結果の誤読を避けるため・性能統計で実行結果を確認するして実行結果を照合する。 ✅
    - D. 機能の説明としてはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてサブスクリプを照合する。

    正解: **C** ／ 難易度: 初級

    **解説:** 性能統計対象bookmでCの記述「ログ上の適用位置と時刻を追跡する複製の進行点を失敗時切り分けとして確」に対応する項目は失敗時切り分け 実行結果（bookm・性能統・実行結・実行結果）です。性能統計時のbookmに関する性能統計の仕様は「ログ上の適用位置と時刻を追跡する複製の進行点を失敗時切り分けとして確」で、確認対象はbook・性能統・実行結・実行結果です。subsc・遅延表示のA:は「複製対象の表対応と開始位置をまとめる管理単位」を述べ、対象は開始位置指定 遅延表示（subsc・遅延表・遅延表・遅延表示）です。収集対象ミラーリンのB:は「CDCのミラー開始と取得時刻を記録し、対象サブスクリプションの取り違」を述べ、対象はEvent Severity（ミラーリン・収集・ミラー・対象サブ）です。ミラーリを解除のD:は「CDCのサブスクリプション状態と取得時刻を記録し」を述べ、対象はReplication Method（ミラーリン・解除・サブス・イベント）です。bookを性能統計という用語は「ログ上の適用位置と時刻を追跡する複製の進行点を失敗時」を指し、失敗時切り分け 実行結果（bookm・性能統・実行結・実行結果）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **bookmark 失敗時切り分け 実行結果**

    - 検証目的: 性能統計のbookmark 失敗時切り分け 実行結果について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、性能統計の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。target datastore の統計を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB014           DS014          Mirroring   BMK014
    ```

    画面・出力には Subscription が含まれ、bookmark 失敗時切り分け 実行結果の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、再同期範囲の誤認を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB014           DS014          BMK014
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### datastore マッピング検査 オンライン表示 {#c11-i0517}
*分類: 性能統計*  ・  難易度: 中級

IBM IIDR 11.4 の 性能統計 で扱う「datastore マッピング検査 オンライン表示」は、CDC Replication が接続するソースまたはターゲットの接続定義をマッピング検査の観点で確認する技術項目です。bookmark valueとLOG062を同じ記録で見比べることで、対象表の不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** datastore マッピング検査 オンライン表示に関する障害切り分けの前提を確認しています。DDL後の表定義更新 Head of Log 0041の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはDDLのサブスクリプション記述と取得時刻を記録し・DDL対象表の漏れを防ぐである。復旧操作で点検欄を確認するときはDDL対象表の漏れを防ぐ。DDL後の表定義更新 Head of Log 0041固有の属性も確認対象に含める。
    - B. 機能の説明としてはInstanceの戻り値と取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。
    - C. 機能の説明としてはCDC Replication が接続するソースまたはターゲットの接続定義をマッピング検査として確認する。オンライン表でオンライン表を確認するときはオンライン表の誤読を防ぐ。 ✅
    - D. 機能の説明としてはTable Mappingで表再読込からrefreshedを読みである。表再読込からrefreshedを読むときはDDL変更後に古い列定義で複を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** オン・オンラ・オンライでCの記述「CDC Replication が接続するソースまたはターゲットの接」に対応する項目はマッピング検査 オンライン表示（dat・オンラ・オンライ・オンラ）です。オンライ時のオンラインに関する性能統計の仕様は「CDC Replication が接続するソースまたはターゲットの接」で、確認対象はdat・オンラ・オンライ・オンラです。後の・復旧・サブスクのA:は「DDLのサブスクリプション記述と取得時刻を記録し」を述べ、対象はof Log（後の表・サブス・DDL対・復旧）です。切替・戻り値・対象インのB:は「Instanceの戻り値と取得時刻を記録し」を述べ、対象は複製位置管理 Instance（Ins・戻り値・対象イン・切替）です。表再読込を停止確認のD:は「Table Mappingで表再読込からrefreshedを読み」を述べ、対象は停止前の確認 MAP14（Tab・表再読・DDL変・停止確）です。オンラインをオンラインという用語は「CDC Replication」を指し、マッピング検査 オンライン表示（dat・オンラ・オンライ・オンラ）で照合する値はオンライン表です。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **datastore マッピング検査 オンライン表示**

    - 検証目的: 性能統計のdatastore マッピング検査 オンライン表示について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、性能統計の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。bookmark valueを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB062           DS062          Mirroring   BMK062
    ```

    画面・出力には Subscription が含まれ、datastore マッピング検査 オンライン表示の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、対象表の不一致を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB062           DS062          BMK062
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### datastore 統計採取 転送条件 {#c11-i0518}
*分類: 性能統計*  ・  難易度: 中級

IBM IIDR 11.4 の 性能統計 で扱う「datastore 統計採取 転送条件」は、CDC Replication が接続するソースまたはターゲットの接続定義を統計採取の観点で確認する技術項目です。bookmark valueとLOG022を同じ記録で見比べることで、対象表の不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** datastore 統計採取 転送条件に関する障害切り分けの前提を確認しています。CHC0368I 失敗時切り分け アーカイブの機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はブックマークでアーカイブを確認することでアーカイブを確認し・アーカイブの誤読を防ぐ。
    - B. 障害切り分けに用いる役割は確認操作で状態欄を整理することでイベントログを確認し・遅延ゼロ確認の欠落を防ぐ。
    - C. 障害切り分けに用いる役割は代替経路確認で代替経路の確を確認することで代替経路の確を確認し・ホスト名変更後の購読構成を更を防ぐ。
    - D. 障害切り分けに用いる役割は統計採取で転送条件を確認することで転送条件を確認し・転送条件の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 統計採取対象datasでDの記述「CDC Replication が接続するソースまたはターゲットの接」に対応する項目は統計採取 転送条件（datas・統計採・転送条・転送条件）です。統計採取時のdatasに関する性能統計の仕様は「CDC Replication が接続するソースまたはターゲットの接」で、確認対象はdata・統計採・転送条・転送条件です。失敗時切り・ブックマーのA:は「bookmark まで適用したことを示す CDC」を述べ、対象は失敗時切り分け アーカイブ（失敗時切り・ブック・アーカ・アーカイ）です。切替対象ミラーリンのB:は「CDCのイベントログと取得時刻を記録し、遅延ゼロ確認の欠落を防ぐ」を述べ、対象はCDCミラーリング Subscrip（ミラーリン・切替・イベン・遅延ゼロ）です。代替経路時のCDCのC:は「CDC Datastoreで代替経路の確認ではデータストア接続の」を述べ、対象は代替経路の確認 STORE10（CDC・代替経・代替経・ホスト名）です。dataを統計採取という用語は「CDC Replication」を指し、統計採取 転送条件（datas・統計採・転送条・転送条件）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **datastore 統計採取 転送条件**

    - 検証目的: 性能統計のdatastore 統計採取 転送条件について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、性能統計の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。bookmark valueを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB022           DS022          Mirroring   BMK022
    ```

    画面・出力には Subscription が含まれ、datastore 統計採取 転送条件の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、対象表の不一致を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB022           DS022          BMK022
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### performance statistics 状態確認 承認待ち {#c11-i0519}
*分類: 性能統計*  ・  難易度: 中級

IBM IIDR 11.4 の 性能統計 で扱う「performance statistics 状態確認 承認待ち」は、サブスクリプションやデータストアの処理量と遅延を測る情報を状態確認の観点で確認する技術項目です。CHC0368I メッセージとMAP038を同じ記録で見比べることで、データストア接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** performance statistics 状態確認 承認待ちに関する障害切り分けの前提を確認しています。subscription 初期同期判定 統合管理の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては初期同期判定で統合管理を確認することで統合管理を確認し・統合管理の誤読を防ぐ。
    - B. 機能の説明としては状態確認で承認待ちを確認することで承認待ちを確認し・承認待ちの誤読を防ぐ。 ✅
    - C. 機能の説明としては記録操作で証跡欄を照合することで遅延確認を確認し・Refresh未完了の見落とを防ぐ。
    - D. 機能の説明としては復旧操作で点検欄を確認することでサブスクリプを確認し・DDL対象表の漏れを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 状態確認対象perfoでBの記述「サブスクリプションやデータストアの処理量と遅延を測る情報である」に対応する項目は状態確認 承認待ち（perfo・状態確・承認待・承認待ち）です。状態確認時のperfoに関する性能統計の仕様は「サブスクリプションやデータストアの処理量と遅延を測る情報」で、確認対象はperf・状態確・承認待・承認待ちです。subsc・初期同期判のA:は「複製対象の表対応と開始位置をまとめる管理単位を初期同期判定として確認」を述べ、対象は初期同期判定 統合管理（subsc・初期同・統合管・統合管理）です。登録時のミラーリンのC:は「CDCの遅延確認と取得時刻を記録し、Refresh未完了の見落としを」を述べ、対象はCDCミラーリング Latency（ミラーリン・登録・遅延確・Refr）です。後の表定を解除のD:は「DDLのサブスクリプション記述と取得時刻を記録し」を述べ、対象はof Log（後の表定義・解除・サブス・DDL対）です。perfを状態確認という用語は「サブスクリプションやデータストアの処理量と遅延を測る」を指し、状態確認 承認待ち（perfo・状態確・承認待・承認待ち）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **performance statistics 状態確認 承認待ち**

    - 検証目的: 性能統計のperformance statistics 状態確認 承認待ちについて、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、性能統計の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。CHC0368I メッセージを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB038           DS038          Mirroring   BMK038
    ```

    画面・出力には Subscription が含まれ、performance statistics 状態確認 承認待ちの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、データストア接続失敗を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB038           DS038          BMK038
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### performance statistics 遅延監視 診断採取 {#c11-i0520}
*分類: 性能統計*  ・  難易度: 上級

IBM IIDR 11.4 の 性能統計 で扱う「performance statistics 遅延監視 診断採取」は、サブスクリプションやデータストアの処理量と遅延を測る情報を遅延監視の観点で確認する技術項目です。CHC0368I メッセージとMAP078を同じ記録で見比べることで、データストア接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** performance statistics 遅延監視 診断採取に関する障害切り分けの前提を確認しています。CDCミラーリング Event Severity 0004の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてミラー開始を照合する。
    - B. 表示や設定で扱う内容はRefresh中の再開を避けるため・表示操作で対象欄を追跡するしてDDL対象表を照合する。
    - C. 表示や設定で扱う内容は診断採取の誤読を避けるため・診断採取で診断採取を確認するして診断採取を照合する。 ✅
    - D. 表示や設定で扱う内容は情報イベントと停止を伴うエラーをを避けるため・イベント一覧から2931を読むしてイベント一覧を照合する。

    正解: **C** ／ 難易度: 上級

    **解説:** 診断・診断採・診断採取でCの記述「サブスクリプションやデータストアの処理量と遅延を測る情報を遅延監視と」に対応する項目は遅延監視 診断採取（per・診断採・診断採取・診断採）です。診断採取時の診断採取に関する性能統計の仕様は「サブスクリプションやデータストアの処理量と遅延を測る情報を遅延監視と」で、確認対象はper・診断採・診断採取・診断採です。ミラ・巡回・ミラー開のA:は「CDCのミラー開始と取得時刻を記録し、対象サブスクリプションの取り違」を述べ、対象はEvent Severity（ミラー・ミラー・対象サブ・巡回）です。確認・DDL・RefrのB:は「DDLのDDL対象表と取得時刻を記録し、Refresh中の再開を防ぐ」を述べ、対象はTable Definition（後の表・DDL・Refr・確認）です。イベント一をログとの照のD:は「CDC Event Logでイベント一覧から2931を読み」を述べ、対象はログとの照合 ERR07（CDC・イベン・情報イベ・ログと）です。診断採取を診断採取という用語は「サブスクリプションやデータストアの処理量と遅延を測る」を指し、遅延監視 診断採取（per・診断採・診断採取・診断採）で照合する値は診断採取です。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **performance statistics 遅延監視 診断採取**

    - 検証目的: 性能統計のperformance statistics 遅延監視 診断採取について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、性能統計の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。CHC0368I メッセージを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB078           DS078          Mirroring   BMK078
    ```

    画面・出力には Subscription が含まれ、performance statistics 遅延監視 診断採取の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、データストア接続失敗を切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB078           DS078          BMK078
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### 性能統計 CDC Communications Activity ログとの照合 STAT07 {#c11-i0521}
*分類: 性能統計*  ・  難易度: 中級

ログとの照合では 性能統計 の 通信統計 を主操作として STAT07 を判定します。時刻と対象識別子への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT07 に残します。ログとの照合を補助する 遅延表示 では Bytespersecond を補助値として STAT07 へ保存します。主判定のログとの照合では性能統計の 通信統計 から Sends を読み STAT07 へ残します。証跡照合のログとの照合では性能統計の Sends と Bytespersecond を STAT07 に保存します。記録対応のログとの照合では性能統計の SendsとRecvs の証跡へ STAT07 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity ログとの照合 STAT07の役割を調べています。エラー処理 CDC Event Log 障害切り分け ERR04の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は通信統計からSendsを読むことで通信統計を確認し・送信回数だけでターゲット適用を防ぐ。 ✅
    - B. 表示や設定で扱う内容はイベント一覧から2931を読むことでイベント一覧を確認し・情報イベントと停止を伴うエラを防ぐ。
    - C. 表示や設定で扱う内容は変更確認操作で採取欄を棚卸することで16進ブックを確認し・重複反映を防ぐ。
    - D. 表示や設定で扱う内容は照合操作で確認欄を採取することで複製位置を確認し・対象インスタンスの取り違えを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能通信統・送信回でAの記述「変更データ取得 通信で通信統計から Sends を読み」に対応する項目はログとの照合 STAT07（変更デ・通信統・ログと）です。照合通信統・ログとに関する性能統計の仕様は「変更データ取得 通信で通信統計から Sends を読み、Sends」で、確認対象は通信統・ログと・送信回です。運用ログと・変更デでB:の障害切り分け ERR04は「変更データ取得 イベントログでイベント一覧か」を述べるため、正答側の照合軸は通信統・性能統・ログとです。項目通信統・ログとでC:の複製位置管理 Subscriptは「サブスクリプションの16進ブックマークと取得」を述べるため、正答側の照合軸は送信回・性能統・通信統です。仕様通信統・ログとでD:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸はログと・送信回・通信統です。用語通信統・ログとという用語は「変更データ取得 通信で通信統計から Sends」を指し、照合する値と誤認リスクの組合せは性能統・通信統・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity ログとの照合 STAT07**

    - 検証目的: 性能統計のCDC Communications Activityについて操作とログを対応し、STAT07のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT07の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB07を指定し、STAT07の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB07
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB07 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT07のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB07 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Sends が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 代替経路の確認 STAT10 {#c11-i0522}
*分類: 性能統計*  ・  難易度: 中級

代替経路の確認では 性能統計 の 通信統計 を主操作として STAT10 を判定します。主経路との役割差への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT10 に残します。代替経路の確認を補助する 遅延表示 では Bytespersecond を補助値として STAT10 へ保存します。主判定の代替経路の確認では性能統計の 通信統計 から Sends を読み STAT10 へ残します。証跡照合の代替経路の確認では性能統計の Sends と Bytespersecond を STAT10 に保存します。記録対応の代替経路の確認では性能統計の SendsとRecvs の証跡へ STAT10 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 代替経路の確認 STAT10を保守記録に説明する必要があります。エラー処理 CDC Event Log 停止前の確認 ERR14と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は通信統計からSendsを読むことで通信統計を確認し・送信回数だけでターゲット適用を防ぐ。 ✅
    - B. 保守作業で参照する機能は通信エラーからERRORを読むことで通信エラーを確認し・情報イベントと停止を伴うエラを防ぐ。
    - C. 保守作業で参照する機能は記録操作で証跡欄を照合することで遅延確認を確認し・初期ロード未完了の見落としを防ぐ。
    - D. 保守作業で参照する機能は表示操作で対象欄を追跡することでログ先頭到達を確認し・初期ロード中の再開を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能通信統・送信回でAの記述「変更データ取得 通信で通信統計から Sends を読み」に対応する項目は代替経路の確認 STAT10（変更デ・通信統・代替経）です。照合通信統・代替経に関する性能統計の仕様は「変更データ取得 通信で通信統計から Sends を読み、Sends」で、確認対象は通信統・代替経・送信回です。運用代替経・変更デでB:の停止前の確認 ERR14は「変更データ取得 イベントログで通信エラーから」を述べるため、正答側の照合軸は通信統・性能統・代替経です。項目通信統・代替経でC:のCDCミラーリングは「変更データ取得の遅延確認と取得時刻を記録し」を述べるため、正答側の照合軸は送信回・性能統・通信統です。仕様通信統・代替経でD:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は代替経・送信回・通信統です。用語通信統・代替経という用語は「変更データ取得 通信で通信統計から Sends」を指し、照合する値と誤認リスクの組合せは性能統・通信統・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 代替経路の確認 STAT10**

    - 検証目的: 性能統計のCDC Communications Activityについて代替手段の成立を確認し、STAT10のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT10の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB10を指定し、STAT10の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB10
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB10 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT10のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB10 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Sends が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 依存関係の確認 STAT13 {#c11-i0523}
*分類: 性能統計*  ・  難易度: 中級

依存関係の確認では 性能統計 の 通信統計 を主操作として STAT13 を判定します。前提資源と後続処理の順序への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT13 に残します。依存関係の確認を補助する 遅延表示 では Bytespersecond を補助値として STAT13 へ保存します。主判定の依存関係の確認では性能統計の 通信統計 から Sends を読み STAT13 へ残します。証跡照合の依存関係の確認では性能統計の Sends と Bytespersecond を STAT13 に保存します。記録対応の依存関係の確認では性能統計の SendsとRecvs の証跡へ STAT13 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 依存関係の確認 STAT13を同一分類のログ依存・サポート Log Dependency 通常状態の確認 LOG01と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は送信回数だけでターゲット適用完了を避けるため・通信統計からSendsを読むして通信統計を照合する。 ✅
    - B. 管理対象との関係を表す説明は休止購読を見落として必要ログを削を避けるため・依存表示からOldestrequiredして依存表示を照合する。
    - C. 管理対象との関係を表す説明はベンダー指示なしの位置変更を避けるため・主操作で出力欄を評価するしてサブスクリプを照合する。
    - D. 管理対象との関係を表す説明は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するしてサブスクリプを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能通信統・送信回でAの記述「変更データ取得 通信で通信統計から Sends を読み」に対応する項目は依存関係の確認 STAT13（変更デ・通信統・依存関）です。照合通信統・依存関に関する性能統計の仕様は「変更データ取得 通信で通信統計から Sends を読み、Sends」で、確認対象は通信統・依存関・送信回です。運用依存関・変更デでB:の通常状態の確認 LOG01は「ログ依存で依存表示から Oldestrequ」を述べるため、正答側の照合軸は通信統・性能統・依存関です。項目通信統・依存関でC:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は送信回・性能統・通信統です。仕様通信統・依存関でD:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸は依存関・送信回・通信統です。用語通信統・依存関という用語は「変更データ取得 通信で通信統計から Sends」を指し、照合する値と誤認リスクの組合せは性能統・通信統・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 依存関係の確認 STAT13**

    - 検証目的: 性能統計のCDC Communications Activityについて依存資源を点検し、STAT13のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT13の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB13を指定し、STAT13の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB13
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB13 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT13のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB13 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Sends が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 停止前の確認 STAT14 {#c11-i0524}
*分類: 性能統計*  ・  難易度: 中級

停止前の確認では 性能統計 の 遅延表示 を主操作として STAT14 を判定します。処理中資源と未完了要求への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT14 に残します。停止前の確認を補助する ログ依存 では Oldestdependency を補助値として STAT14 へ保存します。主判定の停止前の確認では性能統計の 遅延表示 から Bytespersecond を読み STAT14 へ残します。証跡照合の停止前の確認では性能統計の Bytespersecond と Oldestdependency を STAT14 に保存します。記録対応の停止前の確認では性能統計の SendsとRecvs の証跡へ STAT14 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「性能統計 CDC Communications Activity 停止前の確認 STAT14」を「CHC0368I 統計採取 統計値」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は統計採取で統計値を証跡に残し・bookmark まで適用したことを示す CDC。CHC0368I 統計採取 統計値固有の属性も確認対象に含める。
    - B. 仕様上の役割は変更で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - C. 仕様上の役割は計画でサブスクリプを証跡に残し・変更データ取得のサブスクリプション状態と取得時刻を記録し。
    - D. 仕様上の役割は停止確認で遅延表示を証跡に残し・変更データ取得 通信で遅延表示から Bytesperseco。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能遅延表・送信回でDの記述「変更データ取得 通信で遅延表示から」に対応する項目は停止前の確認 STAT14（変更デ・遅延表・停止確）です。照合遅延表・停止確に関する性能統計の仕様は「変更データ取得 通信で遅延表示から Bytespersecond」で、確認対象は遅延表・停止確・送信回です。比較性能統・停止確でA:の統計採取 統計値は「bookmark まで適用したことを示す」を述べるため、正答側の照合軸は変更デ・停止確・遅延表です。運用停止確・変更デでB:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は遅延表・性能統・停止確です。項目遅延表・停止確でC:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸は送信回・性能統・遅延表です。用語遅延表・停止確という用語は「変更データ取得 通信で遅延表示から」を指し、照合する値と誤認リスクの組合せは性能統・遅延表・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 停止前の確認 STAT14**

    - 検証目的: 性能統計のCDC Communications Activityについて安全な停止条件を確認し、STAT14のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB14を指定し、STAT14の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB14
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB14 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT14のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB14 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT14の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Sends が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 再始動後の確認 STAT15 {#c11-i0525}
*分類: 性能統計*  ・  難易度: 中級

再始動後の確認では 性能統計 の ログ依存 を主操作として STAT15 を判定します。再開点と未処理データへの注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT15 に残します。再始動後の確認を補助する 通信統計 では Sends を補助値として STAT15 へ保存します。主判定の再始動後の確認では性能統計の ログ依存 から Oldestdependency を読み STAT15 へ残します。証跡照合の再始動後の確認では性能統計の Oldestdependency と Sends を STAT15 に保存します。記録対応の再始動後の確認では性能統計の SendsとRecvs の証跡へ STAT15 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 再始動後の確認 STAT15の役割を調べています。capture service 遅延監視 警告行の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては警告行の誤読を避けるため・リフレッシュで警告行を確認するして警告行を照合する。
    - B. 機能の説明としては送信回数だけでターゲット適用完了を避けるため・ログ依存からOldestdependenしてログ依存を照合する。 ✅
    - C. 機能の説明としては遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するして初期ロード状を照合する。CDCミラーリング Table Status 0130固有の属性も確認対象に含める。
    - D. 機能の説明としては遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてサブスクリプを照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ログ依・送信回でBの記述「変更データ取得 通信でログ依存から」に対応する項目は再始動後の確認 STAT15（変更デ・ログ依・再始動）です。照合ログ依・再始動に関する性能統計の仕様は「変更データ取得 通信でログ依存から Oldestdependency」で、確認対象はログ依・再始動・送信回です。比較性能統・再始動でA:の遅延監視 警告行は「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸は変更デ・再始動・ログ依です。項目ログ依・再始動でC:のTable Statusは「変更データ取得の初期ロード状態と取得時刻を記」を述べるため、正答側の照合軸は送信回・性能統・ログ依です。仕様ログ依・再始動でD:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸は再始動・送信回・ログ依です。用語ログ依・再始動という用語は「変更データ取得 通信でログ依存から」を指し、照合する値と誤認リスクの組合せは性能統・ログ依・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 再始動後の確認 STAT15**

    - 検証目的: 性能統計のCDC Communications Activityについて再始動結果を検証し、STAT15のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT15のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB15 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT15の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB15を指定し、STAT15の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB15
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB15 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Sends が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 変更前の確認 STAT02 {#c11-i0526}
*分類: 性能統計*  ・  難易度: 中級

変更前の確認では 性能統計 の 遅延表示 を主操作として STAT02 を判定します。変更対象と非対象の境界への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT02 に残します。変更前の確認を補助する ログ依存 では Oldestdependency を補助値として STAT02 へ保存します。主判定の変更前の確認では性能統計の 遅延表示 から Bytespersecond を読み STAT02 へ残します。証跡照合の変更前の確認では性能統計の Bytespersecond と Oldestdependency を STAT02 に保存します。記録対応の変更前の確認では性能統計の SendsとRecvs の証跡へ STAT02 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 変更前の確認 STAT02を保守記録に説明する必要があります。refresh 遅延監視 入力欄と取り違えない説明はどれですか。

    - A. 仕様上の役割は入力欄の誤読を避けるため・マッピングで入力欄を確認するして入力欄を照合する。refresh 遅延監視 入力欄固有の属性も確認対象に含める。
    - B. 仕様上の役割は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてイベントログを照合する。
    - C. 仕様上の役割は送信回数だけでターゲット適用完了を避けるため・遅延表示からBytespersecondして遅延表示を照合する。 ✅
    - D. 仕様上の役割はイベント重大度の誤読を避けるため・採取操作で照合欄を点検するして初期ロード状を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能遅延表・送信回でCの記述「変更データ取得 通信で遅延表示から」に対応する項目は変更前の確認 STAT02（変更デ・遅延表・変更確）です。照合遅延表・変更確に関する性能統計の仕様は「変更データ取得 通信で遅延表示から Bytespersecond」で、確認対象は遅延表・変更確・送信回です。比較性能統・変更確でA:の遅延監視 入力欄は「対象表を初期同期または再同期する複製操作を遅」を述べるため、正答側の照合軸は変更デ・変更確・遅延表です。運用変更確・変更デでB:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸は遅延表・性能統・変更確です。仕様遅延表・変更確でD:のTable Statusは「変更データ取得の初期ロード状態と取得時刻を記」を述べるため、正答側の照合軸は変更確・送信回・遅延表です。用語遅延表・変更確という用語は「変更データ取得 通信で遅延表示から」を指し、照合する値と誤認リスクの組合せは性能統・遅延表・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 変更前の確認 STAT02**

    - 検証目的: 性能統計のCDC Communications Activityについて変更前の証跡を保存し、STAT02のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB02を指定し、STAT02の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB02
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB02 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT02のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB02 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT02の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Sends が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 変更後の確認 STAT03 {#c11-i0527}
*分類: 性能統計*  ・  難易度: 中級

変更後の確認では 性能統計 の ログ依存 を主操作として STAT03 を判定します。反映値と残存値への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT03 に残します。変更後の確認を補助する 通信統計 では Sends を補助値として STAT03 へ保存します。主判定の変更後の確認では性能統計の ログ依存 から Oldestdependency を読み STAT03 へ残します。証跡照合の変更後の確認では性能統計の Oldestdependency と Sends を STAT03 に保存します。記録対応の変更後の確認では性能統計の SendsとRecvs の証跡へ STAT03 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 変更後の確認 STAT03に関する障害切り分けの前提を確認しています。エラー処理 CDC Event Log 変更後の確認 ERR03の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては送信回数だけでターゲット適用完了を避けるため・ログ依存からOldestdependenしてログ依存を照合する。 ✅
    - B. 機能の説明としては情報イベントと停止を伴うエラーをを避けるため・サポート収集からSupportを読むしてサポート収集を照合する。エラー処理 CDC Event Log 変更後の確認 ERR03固有の属性も確認対象に含める。
    - C. 機能の説明としては初期ロード中の再開を避けるため・表示操作で対象欄を追跡するして表定義再読込を照合する。
    - D. 機能の説明としては対象インスタンスの取り違えを避けるため・照合操作で確認欄を採取するしてインスタンスを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ログ依・送信回でAの記述「変更データ取得 通信でログ依存から」に対応する項目は変更後の確認 STAT03（変更デ・ログ依・変更確）です。照合ログ依・変更確に関する性能統計の仕様は「変更データ取得 通信でログ依存から Oldestdependency」で、確認対象はログ依・変更確・送信回です。運用変更確・変更デでB:の変更後の確認 ERR03は「変更データ取得 イベントログでサポート収集か」を述べるため、正答側の照合軸はログ依・性能統・変更確です。項目ログ依・変更確でC:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は送信回・性能統・ログ依です。仕様ログ依・変更確でD:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は変更確・送信回・ログ依です。用語ログ依・変更確という用語は「変更データ取得 通信でログ依存から」を指し、照合する値と誤認リスクの組合せは性能統・ログ依・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 変更後の確認 STAT03**

    - 検証目的: 性能統計のCDC Communications Activityについて変更結果を検証し、STAT03のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT03のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB03 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT03の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB03を指定し、STAT03の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB03
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB03 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Sends が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 引継ぎ記録 STAT09 {#c11-i0528}
*分類: 性能統計*  ・  難易度: 中級

引継ぎ記録では 性能統計 の ログ依存 を主操作として STAT09 を判定します。次担当者が追跡できる証跡への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT09 に残します。引継ぎ記録を補助する 通信統計 では Sends を補助値として STAT09 へ保存します。主判定の引継ぎ記録では性能統計の ログ依存 から Oldestdependency を読み STAT09 へ残します。証跡照合の引継ぎ記録では性能統計の Oldestdependency と Sends を STAT09 に保存します。記録対応の引継ぎ記録では性能統計の SendsとRecvs の証跡へ STAT09 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 引継ぎ記録 STAT09の技術的な意味を資料で確認するとき、CHC0368I 初期同期判定 管理クラスとの境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は初期同期判定で管理クラスを確認することで管理クラスを確認し・管理クラスの誤読を防ぐ。
    - B. 構成を確認する際の意味は確認操作で状態欄を整理することでミラー開始を確認し・遅延ゼロ確認の欠落を防ぐ。CDCミラーリング Event Severity 0094固有の属性も確認対象に含める。
    - C. 構成を確認する際の意味は監査操作で記録欄を比較することでインスタンスを確認し・データ欠落を防ぐ。
    - D. 構成を確認する際の意味はログ依存からOldestdependenことでログ依存を確認し・送信回数だけでターゲット適用を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ログ依・送信回でDの記述「変更データ取得 通信でログ依存から」に対応する項目は引継ぎ記録 STAT09（変更デ・ログ依・性能統）です。照合ログ依・性能統に関する性能統計の仕様は「変更データ取得 通信でログ依存から Oldestdependency」で、確認対象はログ依・性能統・送信回です。比較性能統・性能統でA:の初期同期判定 管理クラスは「bookmark まで適用したことを示す」を述べるため、正答側の照合軸は変更デ・性能統・ログ依です。運用性能統・変更デでB:のEvent Severityは「変更データ取得のミラー開始と取得時刻を記録し」を述べるため、正答側の照合軸はログ依・性能統・性能統です。項目ログ依・性能統でC:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は送信回・性能統・ログ依です。用語ログ依・性能統という用語は「変更データ取得 通信でログ依存から」を指し、照合する値と誤認リスクの組合せは性能統・ログ依・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 引継ぎ記録 STAT09**

    - 検証目的: 性能統計のCDC Communications Activityについて再現可能な記録を作成し、STAT09のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT09のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB09 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT09の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB09を指定し、STAT09の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB09
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB09 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Sends が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 復旧後の確認 STAT06 {#c11-i0529}
*分類: 性能統計*  ・  難易度: 中級

復旧後の確認では 性能統計 の ログ依存 を主操作として STAT06 を判定します。再発していないことを示す値への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT06 に残します。復旧後の確認を補助する 通信統計 では Sends を補助値として STAT06 へ保存します。主判定の復旧後の確認では性能統計の ログ依存 から Oldestdependency を読み STAT06 へ残します。証跡照合の復旧後の確認では性能統計の Oldestdependency と Sends を STAT06 に保存します。記録対応の復旧後の確認では性能統計の SendsとRecvs の証跡へ STAT06 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「性能統計 CDC Communications Activity 復旧後の確認 STAT06」を「ログ依存・サポート Log Dependency 権限境界の確認 LOG12」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はログ依存で支援情報から Returnvalue を読み・Returnvalue とである。支援情報からReturnvalueをときは休止購読を見落として必要ログを防ぐ。
    - B. 運用時に利用する技術的役割は変更データ取得 通信でログ依存から Oldestdependency を読みである。ログ依存からOldestdependときは送信回数だけでターゲット適用を防ぐ。 ✅
    - C. 運用時に利用する技術的役割は後の表定義更新の項目のログ先頭到達と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。
    - D. 運用時に利用する技術的役割はInstanceの戻り値と取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ログ依・送信回でBの記述「変更データ取得 通信でログ依存から」に対応する項目は復旧後の確認 STAT06（変更デ・ログ依・復旧確）です。照合ログ依・復旧確に関する性能統計の仕様は「変更データ取得 通信でログ依存から Oldestdependency」で、確認対象はログ依・復旧確・送信回です。比較性能統・復旧確でA:の権限境界の確認 LOG12は「ログ依存で支援情報から Returnvalu」を述べるため、正答側の照合軸は変更デ・復旧確・ログ依です。項目ログ依・復旧確でC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は送信回・性能統・ログ依です。仕様ログ依・復旧確でD:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は復旧確・送信回・ログ依です。用語ログ依・復旧確という用語は「変更データ取得 通信でログ依存から」を指し、照合する値と誤認リスクの組合せは性能統・ログ依・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 復旧後の確認 STAT06**

    - 検証目的: 性能統計のCDC Communications Activityについて復旧後の安定性を確認し、STAT06のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT06のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB06 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT06の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB06を指定し、STAT06の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB06
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB06 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Sends が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 復旧準備 STAT05 {#c11-i0530}
*分類: 性能統計*  ・  難易度: 中級

復旧準備では 性能統計 の 遅延表示 を主操作として STAT05 を判定します。再開前に必要な整合性への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT05 に残します。復旧準備を補助する ログ依存 では Oldestdependency を補助値として STAT05 へ保存します。主判定の復旧準備では性能統計の 遅延表示 から Bytespersecond を読み STAT05 へ残します。証跡照合の復旧準備では性能統計の Bytespersecond と Oldestdependency を STAT05 に保存します。記録対応の復旧準備では性能統計の SendsとRecvs の証跡へ STAT05 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 復旧準備 STAT05を同一分類のcapture service 状態確認 スケジュールと比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は状態確認でスケジュールを証跡に残し・ソース変更を読み取りサブスクリプションへ渡す処理。capture service 状態確認 スケジュール固有の属性も確認対象に含める。
    - B. コマンドまたは機能の用途は監査で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し・重複反映を防ぐ。
    - C. コマンドまたは機能の用途は計画で複製位置を証跡に残し・Bookmarkの複製位置と取得時刻を記録し。
    - D. コマンドまたは機能の用途は復旧準備で遅延表示を証跡に残し・変更データ取得 通信で遅延表示から Bytesperseco。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能遅延表・送信回でDの記述「変更データ取得 通信で遅延表示から」に対応する項目は復旧準備 STAT05（変更デ・遅延表・復旧準）です。照合遅延表・復旧準に関する性能統計の仕様は「変更データ取得 通信で遅延表示から Bytespersecond」で、確認対象は遅延表・復旧準・送信回です。比較性能統・復旧準でA:の状態確認 スケジュールは「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸は変更デ・復旧準・遅延表です。運用復旧準・変更デでB:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は遅延表・性能統・復旧準です。項目遅延表・復旧準でC:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸は送信回・性能統・遅延表です。用語遅延表・復旧準という用語は「変更データ取得 通信で遅延表示から」を指し、照合する値と誤認リスクの組合せは性能統・遅延表・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 復旧準備 STAT05**

    - 検証目的: 性能統計のCDC Communications Activityについて復旧条件を確認し、STAT05のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB05を指定し、STAT05の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB05
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB05 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT05のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB05 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT05の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Sends が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 性能影響の確認 STAT11 {#c11-i0531}
*分類: 性能統計*  ・  難易度: 中級

性能影響の確認では 性能統計 の 遅延表示 を主操作として STAT11 を判定します。処理時間と滞留箇所への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT11 に残します。性能影響の確認を補助する ログ依存 では Oldestdependency を補助値として STAT11 へ保存します。主判定の性能影響の確認では性能統計の 遅延表示 から Bytespersecond を読み STAT11 へ残します。証跡照合の性能影響の確認では性能統計の Bytespersecond と Oldestdependency を STAT11 に保存します。記録対応の性能影響の確認では性能統計の SendsとRecvs の証跡へ STAT11 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 性能影響の確認 STAT11に関する障害切り分けの前提を確認しています。CHCCLP 失敗時切り分け 履歴行の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は履歴行の誤読を避けるため・リフレッシュで履歴行を確認するして履歴行を照合する。
    - B. 障害切り分けに用いる役割は送信回数だけでターゲット適用完了を避けるため・遅延表示からBytespersecondして遅延表示を照合する。 ✅
    - C. 障害切り分けに用いる役割は表定義未更新を避けるため・点検操作で判定欄を記録するしてログ先頭到達を照合する。
    - D. 障害切り分けに用いる役割は初期ロード中の再開を避けるため・表示操作で対象欄を追跡するして再開条件を照合する。DDL後の表定義更新 Refresh Table 0263固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能遅延表・送信回でBの記述「変更データ取得 通信で遅延表示から」に対応する項目は性能影響の確認 STAT11（変更デ・遅延表・性能影）です。照合遅延表・性能影に関する性能統計の仕様は「変更データ取得 通信で遅延表示から Bytespersecond」で、確認対象は遅延表・性能影・送信回です。比較性能統・性能影でA:の失敗時切り分け 履歴行は「CDC Replication」を述べるため、正答側の照合軸は変更デ・性能影・遅延表です。項目遅延表・性能影でC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は送信回・性能統・遅延表です。仕様遅延表・性能影でD:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は性能影・送信回・遅延表です。用語遅延表・性能影という用語は「変更データ取得 通信で遅延表示から」を指し、照合する値と誤認リスクの組合せは性能統・遅延表・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 性能影響の確認 STAT11**

    - 検証目的: 性能統計のCDC Communications Activityについて負荷と待ちを確認し、STAT11のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB11を指定し、STAT11の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB11
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB11 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT11のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB11 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT11の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Sends が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 構成監査 STAT08 {#c11-i0532}
*分類: 性能統計*  ・  難易度: 中級

構成監査では 性能統計 の 遅延表示 を主操作として STAT08 を判定します。定義値と稼働値の一致への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT08 に残します。構成監査を補助する ログ依存 では Oldestdependency を補助値として STAT08 へ保存します。主判定の構成監査では性能統計の 遅延表示 から Bytespersecond を読み STAT08 へ残します。証跡照合の構成監査では性能統計の Bytespersecond と Oldestdependency を STAT08 に保存します。記録対応の構成監査では性能統計の SendsとRecvs の証跡へ STAT08 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 構成監査 STAT08について構成や状態を確認します。エラー処理 CDC Event Log 構成監査 ERR08ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は構成監査で通信エラーを証跡に残し・変更データ取得 イベントログで通信エラーから ERROR。
    - B. 一次資料が示す主目的は保守でミラー開始を証跡に残し・変更データ取得のミラー開始と取得時刻を記録し。CDCミラーリング Event Severity 0154固有の属性も確認対象に含める。
    - C. 一次資料が示す主目的は構成監査で遅延表示を証跡に残し・変更データ取得 通信で遅延表示から Bytesperseco。 ✅
    - D. 一次資料が示す主目的は解析で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し・重複反映を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能遅延表・送信回でCの記述「変更データ取得 通信で遅延表示から」に対応する項目は構成監査 STAT08（変更デ・遅延表・構成監）です。照合遅延表・構成監に関する性能統計の仕様は「変更データ取得 通信で遅延表示から Bytespersecond」で、確認対象は遅延表・構成監・送信回です。比較性能統・構成監でA:の構成監査 ERR08は「変更データ取得 イベントログで通信エラーから」を述べるため、正答側の照合軸は変更デ・構成監・遅延表です。運用構成監・変更デでB:のEvent Severityは「変更データ取得のミラー開始と取得時刻を記録し」を述べるため、正答側の照合軸は遅延表・性能統・構成監です。仕様遅延表・構成監でD:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は構成監・送信回・遅延表です。用語遅延表・構成監という用語は「変更データ取得 通信で遅延表示から」を指し、照合する値と誤認リスクの組合せは性能統・遅延表・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 構成監査 STAT08**

    - 検証目的: 性能統計のCDC Communications Activityについて構成差分を監査し、STAT08のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB08を指定し、STAT08の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB08
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB08 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT08のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB08 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT08の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Sends が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 権限境界の確認 STAT12 {#c11-i0533}
*分類: 性能統計*  ・  難易度: 中級

権限境界の確認では 性能統計 の ログ依存 を主操作として STAT12 を判定します。参照操作と変更操作の分離への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT12 に残します。権限境界の確認を補助する 通信統計 では Sends を補助値として STAT12 へ保存します。主判定の権限境界の確認では性能統計の ログ依存 から Oldestdependency を読み STAT12 へ残します。証跡照合の権限境界の確認では性能統計の Oldestdependency と Sends を STAT12 に保存します。記録対応の権限境界の確認では性能統計の SendsとRecvs の証跡へ STAT12 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 権限境界の確認 STAT12の設定や表示を読む前に役割を確認します。capture service 状態確認 スケジュールではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはソース変更を読み取りサブスクリプションへ渡す処理である。状態確認でスケジュールを確認するときはスケジュールの誤読を防ぐ。
    - B. 状態を読み取るための働きはサブスクリプションの16進ブックマークと取得時刻を記録し・ベンダー指示なしの位置変更を防ぐである。主操作で出力欄を評価するときはベンダー指示なしの位置変更を防ぐ。
    - C. 状態を読み取るための働きは変更データ取得のサブスクリプション状態と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。
    - D. 状態を読み取るための働きは変更データ取得 通信でログ依存から Oldestdependency を読みである。ログ依存からOldestdependときは送信回数だけでターゲット適用を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ログ依・送信回でDの記述「変更データ取得 通信でログ依存から」に対応する項目は権限境界の確認 STAT12（変更デ・ログ依・権限境）です。照合ログ依・権限境に関する性能統計の仕様は「変更データ取得 通信でログ依存から Oldestdependency」で、確認対象はログ依・権限境・送信回です。比較性能統・権限境でA:の状態確認 スケジュールは「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸は変更デ・権限境・ログ依です。運用権限境・変更デでB:の複製位置管理 Subscriptは「サブスクリプションの16進ブックマークと取得」を述べるため、正答側の照合軸はログ依・性能統・権限境です。項目ログ依・権限境でC:のReplicationは「変更データ取得のサブスクリプション状態と取得」を述べるため、正答側の照合軸は送信回・性能統・ログ依です。用語ログ依・権限境という用語は「変更データ取得 通信でログ依存から」を指し、照合する値と誤認リスクの組合せは性能統・ログ依・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 権限境界の確認 STAT12**

    - 検証目的: 性能統計のCDC Communications Activityについて実行権限を点検し、STAT12のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT12のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB12 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT12の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB12を指定し、STAT12の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB12
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB12 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Subscription が画面・出力に表示されること
    ② ステップ2 の Sends が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 通常状態の確認 STAT01 {#c11-i0534}
*分類: 性能統計*  ・  難易度: 中級

通常状態の確認では 性能統計 の 通信統計 を主操作として STAT01 を判定します。基準値と現在値の差への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT01 に残します。通常状態の確認を補助する 遅延表示 では Bytespersecond を補助値として STAT01 へ保存します。主判定の通常状態の確認では性能統計の 通信統計 から Sends を読み STAT01 へ残します。証跡照合の通常状態の確認では性能統計の Sends と Bytespersecond を STAT01 に保存します。記録対応の通常状態の確認では性能統計の SendsとRecvs の証跡へ STAT01 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 通常状態の確認 STAT01の技術的な意味を資料で確認するとき、apply task 失敗時切り分け 例外記録との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はターゲットへ変更を反映し適用済み位置を記録する処理を失敗時切り分けとして確認する。複製状態監視で例外記録を確認するときは例外記録の誤読を防ぐ。
    - B. 管理対象との関係を表す説明は後の表定義更新の項目のログ先頭到達と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。
    - C. 管理対象との関係を表す説明は変更データ取得の遅延確認と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。CDCミラーリング Latency 0292固有の属性も確認対象に含める。
    - D. 管理対象との関係を表す説明は変更データ取得 通信で通信統計から Sends を読み・Sends と Bytespersecondである。通信統計からSendsを読むときは送信回数だけでターゲット適用を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能通信統・送信回でDの記述「変更データ取得 通信で通信統計から Sends を読み」に対応する項目は通常状態の確認 STAT01（変更デ・通信統・通常状）です。照合通信統・通常状に関する性能統計の仕様は「変更データ取得 通信で通信統計から Sends を読み、Sends」で、確認対象は通信統・通常状・送信回です。比較性能統・通常状でA:の失敗時切り分け 例外記録は「ターゲットへ変更を反映し適用済み位置を記録す」を述べるため、正答側の照合軸は変更デ・通常状・通信統です。運用通常状・変更デでB:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は通信統・性能統・通常状です。項目通信統・通常状でC:のCDCミラーリングは「変更データ取得の遅延確認と取得時刻を記録し」を述べるため、正答側の照合軸は送信回・性能統・通信統です。用語通信統・通常状という用語は「変更データ取得 通信で通信統計から Sends」を指し、照合する値と誤認リスクの組合せは性能統・通信統・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 通常状態の確認 STAT01**

    - 検証目的: 性能統計のCDC Communications Activityについて通常状態を確定し、STAT01のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT01の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB01を指定し、STAT01の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB01
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB01 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT01のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB01 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Sends が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### 性能統計 CDC Communications Activity 障害切り分け STAT04 {#c11-i0535}
*分類: 性能統計*  ・  難易度: 中級

障害切り分けでは 性能統計 の 通信統計 を主操作として STAT04 を判定します。最初に失敗した処理への注意として「送信回数だけでターゲット適用完了を判断する危険があります」を STAT04 に残します。障害切り分けを補助する 遅延表示 では Bytespersecond を補助値として STAT04 へ保存します。主判定の障害切り分けでは性能統計の 通信統計 から Sends を読み STAT04 へ残します。証跡照合の障害切り分けでは性能統計の Sends と Bytespersecond を STAT04 に保存します。記録対応の障害切り分けでは性能統計の SendsとRecvs の証跡へ STAT04 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 性能統計 CDC Communications Activity 障害切り分け STAT04の設定や表示を読む前に役割を確認します。ログ依存・サポート Log Dependency 依存関係の確認 LOG13ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはログ依存で依存表示から Oldestrequired を読み・Oldestrequired とである。依存表示からOldestrequirときは休止購読を見落として必要ログを防ぐ。
    - B. 対象資源に対する働きは後の表定義更新の項目の再開条件と取得時刻を記録し・初期ロード中の再開を防ぐである。表示操作で対象欄を追跡するときは初期ロード中の再開を防ぐ。
    - C. 対象資源に対する働きは変更データ取得の初期ロード状態と取得時刻を記録し・遅延ゼロ確認の欠落を防ぐである。確認操作で状態欄を整理するときは遅延ゼロ確認の欠落を防ぐ。
    - D. 対象資源に対する働きは変更データ取得 通信で通信統計から Sends を読み・Sends と Bytespersecondである。通信統計からSendsを読むときは送信回数だけでターゲット適用を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能通信統・送信回でDの記述「変更データ取得 通信で通信統計から Sends を読み」に対応する項目は障害切り分け STAT04（変更デ・通信統・性能統）です。照合通信統・性能統に関する性能統計の仕様は「変更データ取得 通信で通信統計から Sends を読み、Sends」で、確認対象は通信統・性能統・送信回です。比較性能統・性能統でA:の依存関係の確認 LOG13は「ログ依存で依存表示から Oldestrequ」を述べるため、正答側の照合軸は変更デ・性能統・通信統です。運用性能統・変更デでB:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は通信統・性能統・性能統です。項目通信統・性能統でC:のTable Statusは「変更データ取得の初期ロード状態と取得時刻を記」を述べるため、正答側の照合軸は送信回・性能統・通信統です。用語通信統・性能統という用語は「変更データ取得 通信で通信統計から Sends」を指し、照合する値と誤認リスクの組合せは性能統・通信統・送信回です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **性能統計 CDC Communications Activity 障害切り分け STAT04**

    - 検証目的: 性能統計のCDC Communications Activityについて障害範囲を限定し、STAT04のSendsとRecvsを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象STAT04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へF CHCCDC1,DSPACT=COMMを指定し、STAT04の通信統計を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> F CHCCDC1,DSPACT=COMM
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHC9788I Datastore name = TGT1, Medium = TCP/IP, Paths = 1, Sends = 18420, Recvs = 18398
    ```

    画面・出力にあるSendsを読み、SendsとRecvsと対象STAT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB04を指定し、STAT04の遅延表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB04
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB04 Status Mirroring Latency 3 seconds Bytes per second 842120
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の性能統計を確認する入力画面です。COMMAND入力口へdmshowlogdependency -I SRC1を指定し、STAT04のログ依存を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmshowlogdependency -I SRC1
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB04 requires log file S0001842.LOG Oldest dependency 2026-07-15 13:55
    ```

    画面・出力にあるSubscriptionを読み、SendsとRecvsと対象STAT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Sends が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の Subscription が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting




## IBM IIDR 11.4 > 複製状態監視

### CHC0368I 状態確認 高速伝搬 {#c11-i0536}
*分類: 複製状態監視*  ・  難易度: 中級

IBM IIDR 11.4 の 複製状態監視 で扱う「CHC0368I 状態確認 高速伝搬」は、bookmark まで適用したことを示す CDC Replication メッセージを状態確認の観点で確認する技術項目です。replication mapping 名とDS060を同じ記録で見比べることで、開始位置の取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** CHC0368I 状態確認 高速伝搬の技術的な意味を資料で確認するとき、複製位置管理 Instance 0018との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は変更確認操作で採取欄を棚卸することで戻り値を確認し・重複反映を防ぐ。
    - B. 管理対象との関係を表す説明は状態確認で高速伝搬を確認することで高速伝搬を確認し・高速伝搬の誤読を防ぐ。 ✅
    - C. 管理対象との関係を表す説明は確認操作で状態欄を整理することでRefresを確認し・遅延ゼロ確認の欠落を防ぐ。
    - D. 管理対象との関係を表す説明は方式変更からReturnvalueを読むことで方式変更を確認し・Refresh未完了でMirを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 状態・高速伝・高速伝搬でBの記述「bookmark まで適用したことを示す CDC」に対応する項目は状態確認 高速伝搬（状態確・高速伝・高速伝搬・状態確）です。状態確認時の高速伝搬に関する複製状態監視の仕様は「bookmark まで適用したことを示す CDC」で、確認対象は状態確・高速伝・高速伝搬・状態確です。In・巡回・戻り値のA:は「Instanceの戻り値と取得時刻を記録し、重複反映を防ぐ」を述べ、対象は複製位置管理 Instance（Ins・戻り値・重複反映・巡回）です。収集時のRefreのC:は「CDCのRefresh状態と取得時刻を記録し」を述べ、対象はTable Status（ミラー・Ref・遅延ゼロ・収集）です。方式変更を変更確認のD:は「CDC Refreshで方式変更からReturnvalueを読み」を述べ、対象は変更前の確認 REF02（CDC・方式変・Refr・変更確）です。高速伝搬を状態確認という用語は「bookmark まで適用したことを示す CDC」を指し、状態確認 高速伝搬（状態確・高速伝・高速伝搬・状態確）で照合する値は高速伝搬です。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **CHC0368I 状態確認 高速伝搬**

    - 検証目的: 複製状態監視のCHC0368I 状態確認 高速伝搬について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、複製状態監視の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。replication mapping 名を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB060           DS060          Mirroring   BMK060
    ```

    画面・出力には Subscription が含まれ、CHC0368I 状態確認 高速伝搬の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、開始位置の取り違えを切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB060           DS060          BMK060
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### CHC0368I 遅延監視 識別列 {#c11-i0537}
*分類: 複製状態監視*  ・  難易度: 中級

IBM IIDR 11.4 の 複製状態監視 で扱う「CHC0368I 遅延監視 識別列」は、bookmark まで適用したことを示す CDC Replication メッセージを遅延監視の観点で確認する技術項目です。replication mapping 名とDS020を同じ記録で見比べることで、開始位置の取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** CHC0368I 遅延監視 識別列の技術的な意味を資料で確認するとき、CHCCLP 開始位置指定 レビュー結果との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はエラー処理でレビュー結果を証跡に残し・CDC Replication のスクリプト操作に使うコマン。
    - B. 構成を確認する際の意味は登録で表定義再読込を証跡に残し・DDLの表定義再読込と取得時刻を記録し。
    - C. 構成を確認する際の意味は解除でログ先頭到達を証跡に残し・DDLのログ先頭到達と取得時刻を記録し。
    - D. 構成を確認する際の意味は複製状態監視で識別列を証跡に残し・bookmark まで適用したことを示す CDC。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 複製状態対象遅延監視でDの記述「bookmark まで適用したことを示す CDC」に対応する項目は遅延監視 識別列（遅延監視・複製状・識別列・識別列の）です。複製状態時の遅延監視に関する複製状態監視の仕様は「bookmark まで適用したことを示す CDC」で、確認対象は遅延監視・複製状・識別列・識別列のです。開始位置指・エラー処理のA:は「CDC Replication のスクリプト操作に使うコマンドライン」を述べ、対象は開始位置指定 レビュー結果（開始位置指・エラー・レビュ・レビュー）です。登録対象後の表定義のB:は「DDLの表定義再読込と取得時刻を記録し、Refresh中の再開を防ぐ」を述べ、対象はSource Table（後の表定義・登録・表定義・Refr）です。解除時の後の表定義のC:は「DDLのログ先頭到達と取得時刻を記録し、Refresh中の再開を防ぐ」を述べ、対象はDDL後の表定義更新（後の表定義・解除・ログ先・Refr）です。遅延監視を複製状態監という用語は「bookmark まで適用したことを示す CDC」を指し、遅延監視 識別列（遅延監視・複製状・識別列・識別列の）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **CHC0368I 遅延監視 識別列**

    - 検証目的: 複製状態監視のCHC0368I 遅延監視 識別列について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、複製状態監視の対象へ進みます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help;
    → Enter を押す
    ```

    画面・出力:
    ```text
    CHCCLP> help;
    Available commands include connect datastore, list subscriptions, monitor replication and help "<command>".
    ```

    画面・出力には CHCCLP が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面です。replication mapping 名を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> list subscriptions;
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription    Datastore    State       Bookmark
    SUB020           DS020          Mirroring   BMK020
    ```

    画面・出力には Subscription が含まれ、CHC0368I 遅延監視 識別列の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の詳細確認画面です。表示名とメッセージ形式を照合し、開始位置の取り違えを切り分けます。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> help "list subscriptions";
    → Enter を押す
    ```

    画面・出力:
    ```text
    ResultStringTable
    Name            Datastore      Bookmark
    SUB020           DS020          BMK020
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


