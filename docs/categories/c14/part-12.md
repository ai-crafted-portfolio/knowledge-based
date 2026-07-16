---
search:
  exclude: true
---

# IBM Spectrum Protect 8.1 — 詳細 (12/12)

[← IBM Spectrum Protect 8.1 の概要へ戻る](index.md)


## IBM Spectrum Protect 8.1 > 複製・保護

### 複製・保護 Storage Pool Protection and Node Replication 再始動後の確認 REPL15 {#c14-i0580}
*分類: 複製・保護*  ・  難易度: 上級

再始動後の確認では 複製・保護 の 検証 を主操作として REPL15 を判定します。再開点と未処理データへの注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL15 に残します。再始動後の確認を補助する プール保護 では ANR0984I を補助値として REPL15 へ保存します。主判定の再始動後の確認では複製・保護の 検証 から ANR3730I を読み REPL15 へ残します。証跡照合の再始動後の確認では複製・保護の ANR3730I と ANR0984I を REPL15 に保存します。記録対応の再始動後の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL15 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationの設定や表示を読む前に役割を確認します。ポリシーと管理クラス Policy Set 0047ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。
    - B. 状態を読み取るための働きはDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - C. 状態を読み取るための働きはStorage Poolで再始動後の確認では複製・保護の 検証からANR3730Iを読み・再始動確認に使うである。 ✅
    - D. 状態を読み取るための働きはバックアップ版数と保存先を定めるコピー規則をノード割当確認する。backup copy group ノード割当確認 再同期判断固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 上級

    **解説:** 再始動確対象StoraでCの記述「Storage Poolで再始動後の確認では複製・保護の」に対応する項目は再始動後の確認 REPL15（Storag・再始動・再始動後）です。保護・再始動に関する複製・保護の仕様は「Storage Poolで再始動後の確認では複製・保護の」で、確認対象はStora・再始動・再始動後です。Polic・復旧のA:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・復旧・ディレク）です。保護対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databa・保護・期限切れ）です。backをノード割当のD:は「バックアップ版数と保存先を定めるコピー規則をノード割当確認する」を述べ、対象はノード割当確認 再同期判断（backup・ノード・再同期判）です。Storを再始動確認という用語は「Storage Poolで再始動後の確認では複製」を指し、再始動後の確認 REPL15（Storag・再始動・再始動後）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 再始動後の確認 REPL15**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて再始動結果を検証し、REPL15のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE15を指定し、REPL15の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE15
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE15 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL15を指定し、REPL15のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL15
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 15 for PROTECT STORAGE POOL started. ANR0985I Process 15 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE15を指定し、REPL15の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE15
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE15 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ANR3730I が画面・出力に表示されること
    ② ステップ2 の ANR0984I が画面・出力に表示されること
    ③ ステップ3 の Node が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 変更前の確認 REPL02 {#c14-i0581}
*分類: 複製・保護*  ・  難易度: 上級

変更前の確認では 複製・保護 の 複製状態 を主操作として REPL02 を判定します。変更対象と非対象の境界への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL02 に残します。変更前の確認を補助する 検証 では ANR3730I を補助値として REPL02 へ保存します。主判定の変更前の確認では複製・保護の 複製状態 から TargetServer を読み REPL02 へ残します。証跡照合の変更前の確認では複製・保護の TargetServer と ANR3730I を REPL02 に保存します。記録対応の変更前の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL02 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationの役割を調べています。クライアントスケジュール Association 0060の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。クライアントスケジュール Association 0060固有の属性も確認対象に含める。
    - B. 障害切り分けに用いる役割はStorage Poolで変更前の確認では複製・保護の 複製状態からTargetServerを読みである。 ✅
    - C. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - D. 障害切り分けに用いる役割はバックアップ版数と保存先を定めるコピー規則を容量監視として確認する。

    正解: **B** ／ 難易度: 上級

    **解説:** 変更確認対象StoraでBの記述「Storage Poolで変更前の確認では複製・保護の」に対応する項目は変更前の確認 REPL02（Storag・変更確・変更前の）です。保護・変更前に関する複製・保護の仕様は「Storage Poolで変更前の確認では複製・保護の」で、確認対象はStora・変更確・変更前のです。Assoc・監査のA:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・監査・関連ノー）です。切替時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・切替・管理クラ）です。backをコピーグルのD:は「バックアップ版数と保存先を定めるコピー規則を容量監視として確認する」を述べ、対象は容量監視 復元前提（backup・コピー・復元前提）です。Storを変更確認という用語は「Storage Poolで変更前の確認では複製」を指し、変更前の確認 REPL02（Storag・変更確・変更前の）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 変更前の確認 REPL02**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて変更前の証跡を保存し、REPL02のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE02を指定し、REPL02の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE02
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE02 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE02を指定し、REPL02の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE02
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE02 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL02を指定し、REPL02のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL02
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 02 for PROTECT STORAGE POOL started. ANR0985I Process 02 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Node が画面・出力に表示されること
    ② ステップ2 の ANR3730I が画面・出力に表示されること
    ③ ステップ3 の ANR0984I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 変更後の確認 REPL03 {#c14-i0582}
*分類: 複製・保護*  ・  難易度: 上級

変更後の確認では 複製・保護 の 検証 を主操作として REPL03 を判定します。反映値と残存値への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL03 に残します。変更後の確認を補助する プール保護 では ANR0984I を補助値として REPL03 へ保存します。主判定の変更後の確認では複製・保護の 検証 から ANR3730I を読み REPL03 へ残します。証跡照合の変更後の確認では複製・保護の ANR3730I と ANR0984I を REPL03 に保存します。記録対応の変更後の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL03 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationについて構成や状態を確認します。クライアントスケジュール Start Time 0048ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - B. 状態を読み取るための働きはAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。
    - C. 状態を読み取るための働きはサーバー操作とメッセージを追跡するログを復元前確認する。activity log 復元前確認 管理クラス固有の属性も確認対象に含める。
    - D. 状態を読み取るための働きはStorage Poolで変更後の確認では複製・保護の 検証からANR3730Iを読み・変更確認に使うである。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更確認対象StoraでDの記述「Storage Poolで変更後の確認では複製・保護の」に対応する項目は変更後の確認 REPL03（Storag・変更確・変更後の）です。保護・変更後に関する複製・保護の仕様は「Storage Poolで変更後の確認では複製・保護の」で、確認対象はStora・変更確・変更後のです。Start・復旧のA:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・復旧・失敗理由）です。確認対象AssocのB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・確認・関連ノー）です。復元前確時のactivのC:は「サーバー操作とメッセージを追跡するログを復元前確認する」を述べ、対象は復元前確認 管理クラス（activi・復元前・管理クラ）です。Storを変更確認という用語は「Storage Poolで変更後の確認では複製」を指し、変更後の確認 REPL03（Storag・変更確・変更後の）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 変更後の確認 REPL03**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて変更結果を検証し、REPL03のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE03を指定し、REPL03の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE03
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE03 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL03を指定し、REPL03のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL03
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 03 for PROTECT STORAGE POOL started. ANR0985I Process 03 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE03を指定し、REPL03の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE03
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE03 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ANR3730I が画面・出力に表示されること
    ② ステップ2 の ANR0984I が画面・出力に表示されること
    ③ ステップ3 の Node が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 引継ぎ記録 REPL09 {#c14-i0583}
*分類: 複製・保護*  ・  難易度: 上級

引継ぎ記録では 複製・保護 の 検証 を主操作として REPL09 を判定します。次担当者が追跡できる証跡への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL09 に残します。引継ぎ記録を補助する プール保護 では ANR0984I を補助値として REPL09 へ保存します。主判定の引継ぎ記録では複製・保護の 検証 から ANR3730I を読み REPL09 へ残します。証跡照合の引継ぎ記録では複製・保護の ANR3730I と ANR0984I を REPL09 に保存します。記録対応の引継ぎ記録では複製・保護の Replication StatusとTarget Server の証跡へ REPL09 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「複製・保護 Storage Pool Protection and Node Replication」を「サーバーDB・DR Server Database Backup 構成監査」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はDBで構成監査ではサーバーの DBバックアップからANR4550Iを読み・構成監査に使うである。
    - B. 運用時に利用する技術的役割はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。サーバー日次運用 Node Name 0208固有の属性も確認対象に含める。
    - C. 運用時に利用する技術的役割はStorage Poolで引継ぎ記録では複製・保護の 検証からANR3730Iを読み・複製・保護に使うである。 ✅
    - D. 運用時に利用する技術的役割はストレージプール内の空き領域を回収する処理である。

    正解: **C** ／ 難易度: 上級

    **解説:** 複製対象StoraでCの記述「Storage Poolで引継ぎ記録では複製・保護の」に対応する項目は引継ぎ記録 REPL09（Storag・複製・引継ぎ記）です。保護・引継ぎに関する複製・保護の仕様は「Storage Poolで引継ぎ記録では複製・保護の」で、確認対象はStora・複製・引継ぎ記です。構成監査対象構成監査でのA:は「DBで構成監査ではサーバーの DBバックアップからANR4550Iを」を述べ、対象は構成監査 DBBK08（DB・構成監・構成監査）です。登録対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・登録・運用状態）です。reclを保存期間確のD:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は保存期間確認 画面タグ（reclam・保存期・画面タグ）です。Storを複製・保護という用語は「Storage Poolで引継ぎ記録では複製」を指し、引継ぎ記録 REPL09（Storag・複製・引継ぎ記）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 引継ぎ記録 REPL09**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて再現可能な記録を作成し、REPL09のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE09を指定し、REPL09の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE09
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE09 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL09を指定し、REPL09のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL09
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 09 for PROTECT STORAGE POOL started. ANR0985I Process 09 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE09を指定し、REPL09の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE09
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE09 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ANR3730I が画面・出力に表示されること
    ② ステップ2 の ANR0984I が画面・出力に表示されること
    ③ ステップ3 の Node が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 復旧後の確認 REPL06 {#c14-i0584}
*分類: 複製・保護*  ・  難易度: 上級

復旧後の確認では 複製・保護 の 検証 を主操作として REPL06 を判定します。再発していないことを示す値への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL06 に残します。復旧後の確認を補助する プール保護 では ANR0984I を補助値として REPL06 へ保存します。主判定の復旧後の確認では複製・保護の 検証 から ANR3730I を読み REPL06 へ残します。証跡照合の復旧後の確認では複製・保護の ANR3730I と ANR0984I を REPL06 に保存します。記録対応の復旧後の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL06 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationに関する障害切り分けの前提を確認しています。クライアントスケジュール Schedule Name 0069の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはSchedule Nameのスケジュール定義と取得時刻を記録し・関連付け漏れを防ぐである。
    - B. 機能の説明としてはStorage Poolで復旧後の確認では複製・保護の 検証からANR3730Iを読み・復旧確認に使うである。 ✅
    - C. 機能の説明としてはPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。
    - D. 機能の説明としてはクライアントに適用するバックアップとアーカイブの規則を束ねる単位を復元前確認する。policy domain 復元前確認 統合管理固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 上級

    **解説:** 復旧確認対象StoraでBの記述「Storage Poolで復旧後の確認では複製・保護の」に対応する項目は復旧後の確認 REPL06（Storag・復旧確・復旧後の）です。保護・復旧後に関する複製・保護の仕様は「Storage Poolで復旧後の確認では複製・保護の」で、確認対象はStora・復旧確・復旧後のです。Sched・監査のA:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・監査・スケジュ）です。登録時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・登録・管理クラ）です。poliを復元前確認のD:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を復」を述べ、対象は復元前確認 統合管理（policy・復元前・統合管理）です。Storを復旧確認という用語は「Storage Poolで復旧後の確認では複製」を指し、復旧後の確認 REPL06（Storag・復旧確・復旧後の）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 復旧後の確認 REPL06**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて復旧後の安定性を確認し、REPL06のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE06を指定し、REPL06の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE06
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE06 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL06を指定し、REPL06のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL06
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 06 for PROTECT STORAGE POOL started. ANR0985I Process 06 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE06を指定し、REPL06の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE06
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE06 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ANR3730I が画面・出力に表示されること
    ② ステップ2 の ANR0984I が画面・出力に表示されること
    ③ ステップ3 の Node が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 復旧準備 REPL05 {#c14-i0585}
*分類: 複製・保護*  ・  難易度: 上級

復旧準備では 複製・保護 の 複製状態 を主操作として REPL05 を判定します。再開前に必要な整合性への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL05 に残します。復旧準備を補助する 検証 では ANR3730I を補助値として REPL05 へ保存します。主判定の復旧準備では複製・保護の 複製状態 から TargetServer を読み REPL05 へ残します。証跡照合の復旧準備では複製・保護の TargetServer と ANR3730I を REPL05 に保存します。記録対応の復旧準備では複製・保護の Replication StatusとTarget Server の証跡へ REPL05 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationを保守記録に説明する必要があります。ポリシーと管理クラス Policy Set 0032と取り違えない説明はどれですか。

    - A. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。
    - B. 仕様上の役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。
    - C. 仕様上の役割はPolicy Domainで障害切り分けではポリシードメインの ドメイン照会からPolicyDomainを読である。
    - D. 仕様上の役割はStorage Poolで復旧準備では複製・保護の 複製状態からTargetServerを読みである。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 復旧準備対象StoraでDの記述「Storage Poolで復旧準備では複製・保護の」に対応する項目は復旧準備 REPL05（Storag・復旧準・復旧準備）です。保護・復旧準に関する複製・保護の仕様は「Storage Poolで復旧準備では複製・保護の」で、確認対象はStora・復旧準・復旧準備です。Polic・棚卸のA:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・棚卸・ディレク）です。保護対象PolicのB:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・保護・管理クラ）です。ポリシー時のPolicのC:は「Policy Domainで障害切り分けではポリシードメインの」を述べ、対象は障害切り分け DOM04（Policy・ポリシ・障害切り）です。Storを復旧準備という用語は「Storage Poolで復旧準備では複製・保護の」を指し、復旧準備 REPL05（Storag・復旧準・復旧準備）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 復旧準備 REPL05**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて復旧条件を確認し、REPL05のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE05を指定し、REPL05の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE05
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE05 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE05を指定し、REPL05の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE05
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE05 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL05を指定し、REPL05のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL05
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 05 for PROTECT STORAGE POOL started. ANR0985I Process 05 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Node が画面・出力に表示されること
    ② ステップ2 の ANR3730I が画面・出力に表示されること
    ③ ステップ3 の ANR0984I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 性能影響の確認 REPL11 {#c14-i0586}
*分類: 複製・保護*  ・  難易度: 上級

性能影響の確認では 複製・保護 の 複製状態 を主操作として REPL11 を判定します。処理時間と滞留箇所への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL11 に残します。性能影響の確認を補助する 検証 では ANR3730I を補助値として REPL11 へ保存します。主判定の性能影響の確認では複製・保護の 複製状態 から TargetServer を読み REPL11 へ残します。証跡照合の性能影響の確認では複製・保護の TargetServer と ANR3730I を REPL11 に保存します。記録対応の性能影響の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL11 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationについて構成や状態を確認します。クライアントスケジュール Event Status 0012ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。クライアントスケジュール Event Status 0012固有の属性も確認対象に含める。
    - B. 一次資料が示す主目的はStorage Poolで性能影響の確認では複製・保護の 複製状態からTargetServerを読みである。 ✅
    - C. 一次資料が示す主目的はSchedule Nameのスケジュール定義と取得時刻を記録し・関連付け漏れを防ぐである。
    - D. 一次資料が示す主目的はクライアントに適用するバックアップとアーカイブの規則を束ねる単位を容量監視として確認する。

    正解: **B** ／ 難易度: 上級

    **解説:** 性能影響対象StoraでBの記述「Storage Poolで性能影響の確認では複製・保護の」に対応する項目は性能影響の確認 REPL11（Storag・性能影・性能影響）です。保護・性能影に関する複製・保護の仕様は「Storage Poolで性能影響の確認では複製・保護の」で、確認対象はStora・性能影・性能影響です。Event・巡回のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・巡回・イベント）です。保護時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・保護・スケジュ）です。poliを保護設定のD:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を容」を述べ、対象は容量監視 保護設定（policy・保護設・保護設定）です。Storを性能影響確という用語は「Storage Poolで性能影響の確認では複製」を指し、性能影響の確認 REPL11（Storag・性能影・性能影響）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 性能影響の確認 REPL11**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて負荷と待ちを確認し、REPL11のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE11を指定し、REPL11の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE11
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE11 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE11を指定し、REPL11の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE11
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE11 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL11を指定し、REPL11のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL11
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 11 for PROTECT STORAGE POOL started. ANR0985I Process 11 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Node が画面・出力に表示されること
    ② ステップ2 の ANR3730I が画面・出力に表示されること
    ③ ステップ3 の ANR0984I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 構成監査 REPL08 {#c14-i0587}
*分類: 複製・保護*  ・  難易度: 上級

構成監査では 複製・保護 の 複製状態 を主操作として REPL08 を判定します。定義値と稼働値の一致への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL08 に残します。構成監査を補助する 検証 では ANR3730I を補助値として REPL08 へ保存します。主判定の構成監査では複製・保護の 複製状態 から TargetServer を読み REPL08 へ残します。証跡照合の構成監査では複製・保護の TargetServer と ANR3730I を REPL08 に保存します。記録対応の構成監査では複製・保護の Replication StatusとTarget Server の証跡へ REPL08 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationを同一分類のクライアントスケジュール Schedule Name 0039と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - B. コマンドまたは機能の用途はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - C. コマンドまたは機能の用途はPolicy Domainでログとの照合ではポリシードメインの ドメイン照会からPolicyDomainを読である。
    - D. コマンドまたは機能の用途はStorage Poolで構成監査では複製・保護の 複製状態からTargetServerを読みである。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 構成監査対象StoraでDの記述「Storage Poolで構成監査では複製・保護の」に対応する項目は構成監査 REPL08（Storag・構成監・構成監査）です。保護・構成監に関する複製・保護の仕様は「Storage Poolで構成監査では複製・保護の」で、確認対象はStora・構成監・構成監査です。Sched・棚卸のA:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・棚卸・スケジュ）です。収集対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manage・収集・ドメイン）です。ログとの時のPolicのC:は「Policy Domainでログとの照合ではポリシードメインの」を述べ、対象はログとの照合 DOM07（Policy・ログと・ログとの）です。Storを構成監査という用語は「Storage Poolで構成監査では複製・保護の」を指し、構成監査 REPL08（Storag・構成監・構成監査）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 構成監査 REPL08**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて構成差分を監査し、REPL08のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE08を指定し、REPL08の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE08
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE08 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE08を指定し、REPL08の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE08
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE08 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL08を指定し、REPL08のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL08
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 08 for PROTECT STORAGE POOL started. ANR0985I Process 08 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Node が画面・出力に表示されること
    ② ステップ2 の ANR3730I が画面・出力に表示されること
    ③ ステップ3 の ANR0984I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 権限境界の確認 REPL12 {#c14-i0588}
*分類: 複製・保護*  ・  難易度: 上級

権限境界の確認では 複製・保護 の 検証 を主操作として REPL12 を判定します。参照操作と変更操作の分離への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL12 に残します。権限境界の確認を補助する プール保護 では ANR0984I を補助値として REPL12 へ保存します。主判定の権限境界の確認では複製・保護の 検証 から ANR3730I を読み REPL12 へ残します。証跡照合の権限境界の確認では複製・保護の ANR3730I と ANR0984I を REPL12 に保存します。記録対応の権限境界の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL12 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationの技術的な意味を資料で確認するとき、クライアントスケジュール Action 0021との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。クライアントスケジュール Action 0021固有の属性も確認対象に含める。
    - B. 構成を確認する際の意味はServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - C. 構成を確認する際の意味はStorage Poolで権限境界の確認では複製・保護の 検証からANR3730Iを読み・権限境界確認に使うである。 ✅
    - D. 構成を確認する際の意味は保存期間を過ぎた版やアーカイブを期限切れにする処理である。

    正解: **C** ／ 難易度: 上級

    **解説:** 権限境界対象StoraでCの記述「Storage Poolで権限境界の確認では複製・保護の」に対応する項目は権限境界の確認 REPL12（Storag・権限境・権限境界）です。保護・権限境に関する複製・保護の仕様は「Storage Poolで権限境界の確認では複製・保護の」で、確認対象はStora・権限境・権限境界です。Actio・棚卸のA:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・棚卸・開始時刻）です。保護対象ServeのB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・保護・DBバッ）です。expiを保存期間確のD:は「保存期間を過ぎた版やアーカイブを期限切れにする処理」を述べ、対象は保存期間確認 同期範囲（expira・保存期・同期範囲）です。Storを権限境界確という用語は「Storage Poolで権限境界の確認では複製」を指し、権限境界の確認 REPL12（Storag・権限境・権限境界）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 権限境界の確認 REPL12**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて実行権限を点検し、REPL12のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE12を指定し、REPL12の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE12
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE12 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL12を指定し、REPL12のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL12
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 12 for PROTECT STORAGE POOL started. ANR0985I Process 12 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE12を指定し、REPL12の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE12
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE12 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ANR3730I が画面・出力に表示されること
    ② ステップ2 の ANR0984I が画面・出力に表示されること
    ③ ステップ3 の Node が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 通常状態の確認 REPL01 {#c14-i0589}
*分類: 複製・保護*  ・  難易度: 上級

通常状態の確認では 複製・保護 の プール保護 を主操作として REPL01 を判定します。基準値と現在値の差への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL01 に残します。通常状態の確認を補助する 複製状態 では TargetServer を補助値として REPL01 へ保存します。主判定の通常状態の確認では複製・保護の プール保護 から ANR0984I を読み REPL01 へ残します。証跡照合の通常状態の確認では複製・保護の ANR0984I と TargetServer を REPL01 に保存します。記録対応の通常状態の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL01 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「複製・保護 Storage Pool Protection and Node Replication」を「サーバーDB・DR Server Database Backup 権限境界の確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はDBで権限境界の確認ではサーバーの 履歴照会からBACKUPFULLを読み・権限境界確認に使うである。
    - B. 保守作業で参照する機能はStorage Poolで通常状態の確認では複製・保護の プール保護からANR0984Iを読みである。 ✅
    - C. 保守作業で参照する機能はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - D. 保守作業で参照する機能はサーバー操作とメッセージを追跡するログをノード割当確認する。

    正解: **B** ／ 難易度: 上級

    **解説:** 通常状態対象StoraでBの記述「Storage Poolで通常状態の確認では複製・保護の」に対応する項目は通常状態の確認 REPL01（Storag・通常状・通常状態）です。保護・通常状に関する複製・保護の仕様は「Storage Poolで通常状態の確認では複製・保護の」で、確認対象はStora・通常状・通常状態です。権限境界対象権限境界ののA:は「DBで権限境界の確認ではサーバーの 履歴照会からBACKUPFULL」を述べ、対象は権限境界の確認 DBBK12（DB・権限境・権限境界）です。収集時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・収集・イベント）です。actiをノード割当のD:は「サーバー操作とメッセージを追跡するログをノード割当確認する」を述べ、対象はノード割当確認 セッション上限（activi・ノード・セッショ）です。Storを通常状態確という用語は「Storage Poolで通常状態の確認では複製」を指し、通常状態の確認 REPL01（Storag・通常状・通常状態）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 通常状態の確認 REPL01**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて通常状態を確定し、REPL01のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL01を指定し、REPL01のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL01
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 01 for PROTECT STORAGE POOL started. ANR0985I Process 01 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE01を指定し、REPL01の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE01
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE01 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE01を指定し、REPL01の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE01
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE01 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ANR0984I が画面・出力に表示されること
    ② ステップ2 の Node が画面・出力に表示されること
    ③ ステップ3 の ANR3730I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 障害切り分け REPL04 {#c14-i0590}
*分類: 複製・保護*  ・  難易度: 上級

障害切り分けでは 複製・保護 の プール保護 を主操作として REPL04 を判定します。最初に失敗した処理への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL04 に残します。障害切り分けを補助する 複製状態 では TargetServer を補助値として REPL04 へ保存します。主判定の障害切り分けでは複製・保護の プール保護 から ANR0984I を読み REPL04 へ残します。証跡照合の障害切り分けでは複製・保護の ANR0984I と TargetServer を REPL04 に保存します。記録対応の障害切り分けでは複製・保護の Replication StatusとTarget Server の証跡へ REPL04 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationの技術的な意味を資料で確認するとき、クライアントスケジュール Schedule Name 0054との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はSchedule Nameのスケジュール定義と取得時刻を記録し・開始時刻誤設定を防ぐである。
    - B. 管理対象との関係を表す説明はStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - C. 管理対象との関係を表す説明はバックアップや管理コマンドを決めた時刻に実行する定義をノード割当確認する。
    - D. 管理対象との関係を表す説明はStorage Poolで障害切り分けでは複製・保護の プール保護からANR0984Iを読み・複製である。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 複製対象StoraでDの記述「Storage Poolで障害切り分けでは複製・保護の」に対応する項目は障害切り分け REPL04（Storag・複製・障害切り）です。保護・障害切に関する複製・保護の仕様は「Storage Poolで障害切り分けでは複製・保護の」で、確認対象はStora・複製・障害切りです。Sched・復旧のA:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・復旧・スケジュ）です。切替対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storag・切替・ストレー）です。ノード割時のschedのC:は「バックアップや管理コマンドを決めた時刻に実行する定義をノード割当確認」を述べ、対象はノード割当確認 変換規則（schedu・ノード・変換規則）です。Storを複製・保護という用語は「Storage Poolで障害切り分けでは複製」を指し、障害切り分け REPL04（Storag・複製・障害切り）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 障害切り分け REPL04**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて障害範囲を限定し、REPL04のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL04を指定し、REPL04のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL04
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 04 for PROTECT STORAGE POOL started. ANR0985I Process 04 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE04を指定し、REPL04の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE04
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE04 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE04を指定し、REPL04の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE04
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE04 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ANR0984I が画面・出力に表示されること
    ② ステップ2 の Node が画面・出力に表示されること
    ③ ステップ3 の ANR3730I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


