---
search:
  exclude: true
---

# IBM IIDR 11.4 — 詳細 (5/6)

[← IBM IIDR 11.4 の概要へ戻る](index.md)


## IBM IIDR 11.4 > ミラーリング

### CDCミラーリング Replication Method 0013 {#c11-i0399}
*分類: ミラーリング*  ・  難易度: 初級

灰N巡回0014ではIBM IIDR 11.4 の ミラーリングを扱う採取票灰N巡回0014です。灰N巡回0014は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録灰N巡回0014です。灰N巡回0014ではサブスクリプション状態と取得時刻を採取票灰N巡回0014へ残します。灰N巡回0014ではRefresh未完了の見落としを避けるため補助資料も照合する判断灰N巡回0014です。灰N巡回0014の用語整理では複製ミラーリングの対象値を実在出力で比較する記録灰N巡回0014です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0013を保守記録に説明する必要があります。複製位置管理 Subscription 0015と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は監査操作で記録欄を比較することで16進ブックを確認し・データ欠落を防ぐ。
    - B. 保守作業で参照する機能は記録操作で証跡欄を照合することでイベントログを確認し・Refresh未完了の見落とを防ぐ。
    - C. 保守作業で参照する機能は遅延表示からBytespersecondことで遅延表示を確認し・送信回数だけでターゲット適用を防ぐ。
    - D. 保守作業で参照する機能は記録操作で証跡欄を照合することでサブスクリプを確認し・Refresh未完了の見落とを防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 巡回・サブス・RefrでDの記述「CDCのサブスクリプション状態と取得時刻を記録し」に対応する項目はReplication Method（ミラー・サブス・Refr・巡回）です。巡回時のサブスクリに関するミラーリングの仕様は「CDCのサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・Refr・巡回です。Su・巡回・16進ブのA:は「Subscriptionの16進ブックマークと取得時刻を記録し」を述べ、対象は複製位置管理 Subscriptio（Sub・16進・データ欠・巡回）です。保護・イベン・RefrのB:は「CDCのイベントログと取得時刻を記録し、Refresh未完了の見落と」を述べ、対象はCDCミラーリング Subscrip（ミラー・イベン・Refr・保護）です。性能影響時の遅延表示のC:は「CDC Communicationsで遅延表示からBytespers」を述べ、対象は性能影響の確認 STAT11（CDC・遅延表・送信回数・性能影）です。サブスクリを巡回という用語は「CDCのサブスクリプション状態と取得時刻を記録し」を指し、Replication Method（ミラー・サブス・Refr・巡回）で照合する値はサブスクリプです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0013**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0013について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE013
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0013A
    ```

    画面・出力には IIDR114DD0013A が表示され、CDCミラーリング Replication Method 0013 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE013
    Mirroring request accepted
    確認コード IIDR114DD0013B
    ```

    画面・出力には IIDR114DD0013B が表示され、CDCミラーリング Replication Method 0013 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0013C
    ```

    画面・出力には IIDR114DD0013C が表示され、CDCミラーリング Replication Method 0013 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0013A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0013B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0013C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0028 {#c11-i0400}
*分類: ミラーリング*  ・  難易度: 中級

黄I棚卸0029ではIBM IIDR 11.4 の ミラーリングを扱う採取票黄I棚卸0029です。黄I棚卸0029は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録黄I棚卸0029です。黄I棚卸0029ではサブスクリプション状態と取得時刻を採取票黄I棚卸0029へ残します。黄I棚卸0029では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断黄I棚卸0029です。黄I棚卸0029の用語整理では複製ミラーリングの対象値を実在出力で区別する記録黄I棚卸0029です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0028の技術的な意味を資料で確認するとき、DDL後の表定義更新 Source Table 0095との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は棚卸でサブスクリプを証跡に残し・ミラーリングの項目のサブスクリプション状態と取得時刻を記録し。 ✅
    - B. 管理対象との関係を表す説明は変更で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - C. 管理対象との関係を表す説明は保護でログ先頭到達を証跡に残し・後の表定義更新の項目のログ先頭到達と取得時刻を記録し。DDL後の表定義更新 Subscription 0242固有の属性も確認対象に含める。
    - D. 管理対象との関係を表す説明は監査証跡で監査証跡を証跡に残し・bookmark まで適用したことを示す CDC。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能サブス・対象サでAの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・棚卸）です。照合サブス・対象サに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・対象サです。運用棚卸・ミラーでB:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はサブス・ミラー・棚卸です。項目ミラー・対象サでC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は対象サ・ミラー・サブスです。仕様ミラー・サブスでD:の開始位置指定 監査証跡は「bookmark まで適用したことを示す」を述べるため、正答側の照合軸は棚卸・対象サ・サブスです。用語サブス・棚卸という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・棚卸です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0028**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0028について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE028
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0028A
    ```

    画面・出力には IIDR114DD0028A が表示され、CDCミラーリング Replication Method 0028 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE028
    Mirroring request accepted
    確認コード IIDR114DD0028B
    ```

    画面・出力には IIDR114DD0028B が表示され、CDCミラーリング Replication Method 0028 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0028C
    ```

    画面・出力には IIDR114DD0028C が表示され、CDCミラーリング Replication Method 0028 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0028A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0028B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0028C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0043 {#c11-i0401}
*分類: ミラーリング*  ・  難易度: 中級

藍D復旧0044ではIBM IIDR 11.4 の ミラーリングを扱う採取票藍D復旧0044です。藍D復旧0044は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録藍D復旧0044です。藍D復旧0044ではサブスクリプション状態と取得時刻を採取票藍D復旧0044へ残します。藍D復旧0044ではイベント重大度の誤読を避けるため補助資料も照合する判断藍D復旧0044です。藍D復旧0044の用語整理では複製ミラーリングの対象値を実在出力で評価する記録藍D復旧0044です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0043について構成や状態を確認します。CDCミラーリング Subscription 0091ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてイベントログを照合する。
    - B. 対象資源に対する働きはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するして遅延確認を照合する。
    - C. 対象資源に対する働きはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてサブスクリプを照合する。 ✅
    - D. 対象資源に対する働きは送信回数だけでターゲット適用完了を避けるため・通信統計からSendsを読むして通信統計を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能サブス・イベンでCの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・復旧）です。照合サブス・イベンに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・イベンです。比較ミラー・復旧でA:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸はミラー・イベン・復旧です。運用復旧・ミラーでB:のCDCミラーリングは「ミラーリングの項目の遅延確認と取得時刻を記録」を述べるため、正答側の照合軸はサブス・ミラー・復旧です。仕様ミラー・サブスでD:の依存関係の確認 STAT13は「CDC Communicationsで通信統」を述べるため、正答側の照合軸は復旧・イベン・サブスです。用語サブス・復旧という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・イベン・復旧です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0043**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0043について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE043
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0043A
    ```

    画面・出力には IIDR114DD0043A が表示され、CDCミラーリング Replication Method 0043 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE043
    Mirroring request accepted
    確認コード IIDR114DD0043B
    ```

    画面・出力には IIDR114DD0043B が表示され、CDCミラーリング Replication Method 0043 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0043C
    ```

    画面・出力には IIDR114DD0043C が表示され、CDCミラーリング Replication Method 0043 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0043A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0043B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0043C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0058 {#c11-i0402}
*分類: ミラーリング*  ・  難易度: 中級

黒S復旧0059ではIBM IIDR 11.4 の ミラーリングを扱う採取票黒S復旧0059です。黒S復旧0059は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録黒S復旧0059です。黒S復旧0059ではサブスクリプション状態と取得時刻を採取票黒S復旧0059へ残します。黒S復旧0059では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断黒S復旧0059です。黒S復旧0059の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録黒S復旧0059です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0058の役割を調べています。CDCミラーリング Event Severity 0154の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は確認操作で状態欄を整理することでミラー開始を確認し・遅延ゼロ確認の欠落を防ぐ。
    - B. 表示や設定で扱う内容は復旧操作で点検欄を確認することでサブスクリプを確認し・データ定義対象表の漏れを防ぐ。
    - C. 表示や設定で扱う内容は支援情報からReturnvalueを読むことで支援情報を確認し・休止購読を見落として必要ログを防ぐ。
    - D. 表示や設定で扱う内容は確認操作で状態欄を整理することでサブスクリプを確認し・遅延ゼロ確認の欠落を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能サブス・遅延ゼでDの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・復旧）です。照合サブス・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・遅延ゼです。比較ミラー・復旧でA:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸はミラー・遅延ゼ・復旧です。運用復旧・ミラーでB:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はサブス・ミラー・復旧です。項目ミラー・遅延ゼでC:の再始動後の確認 LOG15は「Log Dependencyで支援情報からR」を述べるため、正答側の照合軸は遅延ゼ・ミラー・サブスです。用語サブス・復旧という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・復旧です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0058**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0058について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE058
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0058A
    ```

    画面・出力には IIDR114DD0058A が表示され、CDCミラーリング Replication Method 0058 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE058
    Mirroring request accepted
    確認コード IIDR114DD0058B
    ```

    画面・出力には IIDR114DD0058B が表示され、CDCミラーリング Replication Method 0058 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0058C
    ```

    画面・出力には IIDR114DD0058C が表示され、CDCミラーリング Replication Method 0058 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0058A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0058B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0058C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0073 {#c11-i0403}
*分類: ミラーリング*  ・  難易度: 中級

灰N監査0074ではIBM IIDR 11.4 の ミラーリングを扱う採取票灰N監査0074です。灰N監査0074は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録灰N監査0074です。灰N監査0074ではサブスクリプション状態と取得時刻を採取票灰N監査0074へ残します。灰N監査0074ではRefresh未完了の見落としを避けるため補助資料も照合する判断灰N監査0074です。灰N監査0074の用語整理では複製ミラーリングの対象値を実在出力で比較する記録灰N監査0074です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Replication Method 0073」を「複製位置管理 Subscription 0075」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はデータ欠落を避けるため・監査操作で記録欄を比較するして16進ブックを照合する。
    - B. 保守作業で参照する機能は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてイベントログを照合する。
    - C. 保守作業で参照する機能は情報イベントと停止を伴うエラーをを避けるため・通信エラーからERRORを読むして通信エラーを照合する。
    - D. 保守作業で参照する機能は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するしてサブスクリプを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能サブス・初期ロでDの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・監査）です。照合サブス・初期ロに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・初期ロです。比較ミラー・監査でA:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はミラー・初期ロ・監査です。運用監査・ミラーでB:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸はサブス・ミラー・監査です。項目ミラー・初期ロでC:の停止前の確認 ERR14は「CDC Event Logで通信エラーからE」を述べるため、正答側の照合軸は初期ロ・ミラー・サブスです。用語サブス・監査という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・監査です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0073**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0073について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE073
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0073A
    ```

    画面・出力には IIDR114DD0073A が表示され、CDCミラーリング Replication Method 0073 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE073
    Mirroring request accepted
    確認コード IIDR114DD0073B
    ```

    画面・出力には IIDR114DD0073B が表示され、CDCミラーリング Replication Method 0073 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0073C
    ```

    画面・出力には IIDR114DD0073C が表示され、CDCミラーリング Replication Method 0073 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0073A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0073B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0073C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0088 {#c11-i0404}
*分類: ミラーリング*  ・  難易度: 中級

黄I変更0089ではIBM IIDR 11.4 の ミラーリングを扱う採取票黄I変更0089です。黄I変更0089は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録黄I変更0089です。黄I変更0089ではサブスクリプション状態と取得時刻を採取票黄I変更0089へ残します。黄I変更0089では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断黄I変更0089です。黄I変更0089の用語整理では複製ミラーリングの対象値を実在出力で区別する記録黄I変更0089です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0088を同一分類のCDCミラーリング Subscription 0181と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は収集でイベントログを証跡に残し・ミラーリングの項目のイベントログと取得時刻を記録し。
    - B. 管理対象との関係を表す説明は変更でサブスクリプを証跡に残し・ミラーリングの項目のサブスクリプション状態と取得時刻を記録し。 ✅
    - C. 管理対象との関係を表す説明は抑止で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し。
    - D. 管理対象との関係を表す説明は再始動確認でサポート収集を証跡に残し・CDC Event Logでサポート収集からSupportを。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能サブス・対象サでBの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・変更）です。照合サブス・対象サに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・対象サです。比較ミラー・変更でA:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸はミラー・対象サ・変更です。項目ミラー・対象サでC:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は対象サ・ミラー・サブスです。仕様ミラー・サブスでD:の再始動後の確認 ERR15は「CDC Event Logでサポート収集から」を述べるため、正答側の照合軸は変更・対象サ・サブスです。用語サブス・変更という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・変更です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0088**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0088について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE088
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0088A
    ```

    画面・出力には IIDR114DD0088A が表示され、CDCミラーリング Replication Method 0088 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE088
    Mirroring request accepted
    確認コード IIDR114DD0088B
    ```

    画面・出力には IIDR114DD0088B が表示され、CDCミラーリング Replication Method 0088 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0088C
    ```

    画面・出力には IIDR114DD0088C が表示され、CDCミラーリング Replication Method 0088 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0088A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0088B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0088C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0103 {#c11-i0405}
*分類: ミラーリング*  ・  難易度: 上級

藍D移行0104ではIBM IIDR 11.4 の ミラーリングを扱う採取票藍D移行0104です。藍D移行0104は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録藍D移行0104です。藍D移行0104ではサブスクリプション状態と取得時刻を採取票藍D移行0104へ残します。藍D移行0104ではイベント重大度の誤読を避けるため補助資料も照合する判断藍D移行0104です。藍D移行0104の用語整理では複製ミラーリングの対象値を実在出力で評価する記録藍D移行0104です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0103の設定や表示を読む前に役割を確認します。CDCミラーリング Subscription 0196ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはミラーリングの項目のイベントログと取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。
    - B. 対象資源に対する働きはミラーリングの項目のサブスクリプション状態と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。 ✅
    - C. 対象資源に対する働きは後の表定義更新の項目のサブスクリプション記述と取得時刻を記録し・データ定義対象表の漏れを防ぐである。復旧操作で点検欄を確認するときはデータ定義対象表の漏れを防ぐ。
    - D. 対象資源に対する働きは複製対象の表対応と開始位置をまとめる管理単位である。ログ位置照合でプロファイルを確認するときはプロファイルの誤読を防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能サブス・イベンでBの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・移行）です。照合サブス・イベンに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・イベンです。比較ミラー・移行でA:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸はミラー・イベン・移行です。項目ミラー・イベンでC:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はイベン・ミラー・サブスです。仕様ミラー・サブスでD:のログ位置照合 プロファイルは「複製対象の表対応と開始位置をまとめる管理単位」を述べるため、正答側の照合軸は移行・イベン・サブスです。用語サブス・移行という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・イベン・移行です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0103**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0103について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE103
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0103A
    ```

    画面・出力には IIDR114DD0103A が表示され、CDCミラーリング Replication Method 0103 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE103
    Mirroring request accepted
    確認コード IIDR114DD0103B
    ```

    画面・出力には IIDR114DD0103B が表示され、CDCミラーリング Replication Method 0103 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0103C
    ```

    画面・出力には IIDR114DD0103C が表示され、CDCミラーリング Replication Method 0103 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0103A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0103B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0103C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0118 {#c11-i0406}
*分類: ミラーリング*  ・  難易度: 上級

黒S移行0119ではIBM IIDR 11.4 の ミラーリングを扱う採取票黒S移行0119です。黒S移行0119は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録黒S移行0119です。黒S移行0119ではサブスクリプション状態と取得時刻を採取票黒S移行0119へ残します。黒S移行0119では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断黒S移行0119です。黒S移行0119の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録黒S移行0119です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0118に関する障害切り分けの前提を確認しています。CDCミラーリング Latency 0157の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は記録操作で証跡欄を照合することで遅延確認を確認し・初期ロード未完了の見落としを防ぐ。
    - B. 表示や設定で扱う内容は表再読込から初期ロードedを読むことで表再読込を確認し・データ定義変更後に古い列定義を防ぐ。
    - C. 表示や設定で扱う内容は初期同期判定で統合管理を確認することで統合管理を確認し・統合管理の誤読を防ぐ。
    - D. 表示や設定で扱う内容は確認操作で状態欄を整理することでサブスクリプを確認し・遅延ゼロ確認の欠落を防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能サブス・遅延ゼでDの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・移行）です。照合サブス・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・遅延ゼです。比較ミラー・移行でA:のCDCミラーリングは「ミラーリングの項目の遅延確認と取得時刻を記録」を述べるため、正答側の照合軸はミラー・遅延ゼ・移行です。運用移行・ミラーでB:の構成監査 MAP08は「Table Mappingで表再読込から初期」を述べるため、正答側の照合軸はサブス・ミラー・移行です。項目ミラー・遅延ゼでC:の初期同期判定 統合管理は「複製対象の表対応と開始位置をまとめる管理単位」を述べるため、正答側の照合軸は遅延ゼ・ミラー・サブスです。用語サブス・移行という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・移行です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0118**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0118について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE118
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0118A
    ```

    画面・出力には IIDR114DD0118A が表示され、CDCミラーリング Replication Method 0118 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE118
    Mirroring request accepted
    確認コード IIDR114DD0118B
    ```

    画面・出力には IIDR114DD0118B が表示され、CDCミラーリング Replication Method 0118 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0118C
    ```

    画面・出力には IIDR114DD0118C が表示され、CDCミラーリング Replication Method 0118 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0118A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0118B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0118C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0133 {#c11-i0407}
*分類: ミラーリング*  ・  難易度: 初級

灰N診断0134ではIBM IIDR 11.4 の ミラーリングを扱う採取票灰N診断0134です。灰N診断0134は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録灰N診断0134です。灰N診断0134ではサブスクリプション状態と取得時刻を採取票灰N診断0134へ残します。灰N診断0134ではRefresh未完了の見落としを避けるため補助資料も照合する判断灰N診断0134です。灰N診断0134の用語整理では複製ミラーリングの対象値を実在出力で比較する記録灰N診断0134です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0133を保守記録に説明する必要があります。DDL後の表定義更新 Source Table 0155と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は保守で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - B. 保守作業で参照する機能は診断でサブスクリプを証跡に残し・ミラーリングの項目のサブスクリプション状態と取得時刻を記録し。 ✅
    - C. 保守作業で参照する機能は代替経路確認で定義表示を証跡に残し・CDC Subscriptionで定義表示からSubscri。
    - D. 保守作業で参照する機能は統計採取でマクロ実行を証跡に残し・ターゲットへ変更を反映し適用済み位置を記録する処理を統計採取。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能サブス・初期ロでBの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・診断）です。照合サブス・初期ロに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・初期ロです。比較ミラー・診断でA:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・初期ロ・診断です。項目ミラー・初期ロでC:の代替経路の確認 SUB10は「CDC Subscriptionで定義表示か」を述べるため、正答側の照合軸は初期ロ・ミラー・サブスです。仕様ミラー・サブスでD:の統計採取 マクロ実行は「ターゲットへ変更を反映し適用済み位置を記録す」を述べるため、正答側の照合軸は診断・初期ロ・サブスです。用語サブス・診断という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・診断です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0133**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0133について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE013
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0133A
    ```

    画面・出力には IIDR114DD0133A が表示され、CDCミラーリング Replication Method 0133 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE013
    Mirroring request accepted
    確認コード IIDR114DD0133B
    ```

    画面・出力には IIDR114DD0133B が表示され、CDCミラーリング Replication Method 0133 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0133C
    ```

    画面・出力には IIDR114DD0133C が表示され、CDCミラーリング Replication Method 0133 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0133A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0133B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0133C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0148 {#c11-i0408}
*分類: ミラーリング*  ・  難易度: 中級

黄I保守0149ではIBM IIDR 11.4 の ミラーリングを扱う採取票黄I保守0149です。黄I保守0149は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録黄I保守0149です。黄I保守0149ではサブスクリプション状態と取得時刻を採取票黄I保守0149へ残します。黄I保守0149では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断黄I保守0149です。黄I保守0149の用語整理では複製ミラーリングの対象値を実在出力で区別する記録黄I保守0149です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0148の技術的な意味を資料で確認するとき、CDCミラーリング Event Severity 0199との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてミラー開始を照合する。CDCミラーリング Event Severity 0199固有の属性も確認対象に含める。
    - B. 管理対象との関係を表す説明はログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするしてデータ定義対を照合する。
    - C. 管理対象との関係を表す説明は表定義未更新を避けるため・点検操作で判定欄を記録するして再開条件を照合する。
    - D. 管理対象との関係を表す説明は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてサブスクリプを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能サブス・対象サでDの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・保守）です。照合サブス・対象サに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・対象サです。比較ミラー・保守でA:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸はミラー・対象サ・保守です。運用保守・ミラーでB:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はサブス・ミラー・保守です。項目ミラー・対象サでC:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は対象サ・ミラー・サブスです。用語サブス・保守という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・保守です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0148**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0148について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE028
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0148A
    ```

    画面・出力には IIDR114DD0148A が表示され、CDCミラーリング Replication Method 0148 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE028
    Mirroring request accepted
    確認コード IIDR114DD0148B
    ```

    画面・出力には IIDR114DD0148B が表示され、CDCミラーリング Replication Method 0148 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0148C
    ```

    画面・出力には IIDR114DD0148C が表示され、CDCミラーリング Replication Method 0148 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0148A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0148B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0148C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0163 {#c11-i0409}
*分類: ミラーリング*  ・  難易度: 中級

藍D切替0164ではIBM IIDR 11.4 の ミラーリングを扱う採取票藍D切替0164です。藍D切替0164は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録藍D切替0164です。藍D切替0164ではサブスクリプション状態と取得時刻を採取票藍D切替0164へ残します。藍D切替0164ではイベント重大度の誤読を避けるため補助資料も照合する判断藍D切替0164です。藍D切替0164の用語整理では複製ミラーリングの対象値を実在出力で評価する記録藍D切替0164です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0163について構成や状態を確認します。複製位置管理 Subscription 0255ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはSubscriptionの16進ブックマークと取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。
    - B. 対象資源に対する働きはMirror Statusで通信活動からCHC9788Iを読み・CHC9788IとLatencyを照合する。通信活動からCHC9788Iを読むときは初期ロード中の表をMirroを防ぐ。
    - C. 対象資源に対する働きはBookmarkの複製位置と取得時刻を記録し・ベンダー指示なしの位置変更を防ぐである。主操作で出力欄を評価するときはベンダー指示なしの位置変更を防ぐ。
    - D. 対象資源に対する働きはミラーリングの項目のサブスクリプション状態と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能サブス・イベンでDの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・切替）です。照合サブス・イベンに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・イベンです。比較ミラー・切替でA:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はミラー・イベン・切替です。運用切替・ミラーでB:の引継ぎ記録 MIR09は「Mirror Statusで通信活動からCH」を述べるため、正答側の照合軸はサブス・ミラー・切替です。項目ミラー・イベンでC:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸はイベン・ミラー・サブスです。用語サブス・切替という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・イベン・切替です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0163**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0163について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE043
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0163A
    ```

    画面・出力には IIDR114DD0163A が表示され、CDCミラーリング Replication Method 0163 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE043
    Mirroring request accepted
    確認コード IIDR114DD0163B
    ```

    画面・出力には IIDR114DD0163B が表示され、CDCミラーリング Replication Method 0163 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0163C
    ```

    画面・出力には IIDR114DD0163C が表示され、CDCミラーリング Replication Method 0163 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0163A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0163B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0163C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0178 {#c11-i0410}
*分類: ミラーリング*  ・  難易度: 中級

黒S切替0179ではIBM IIDR 11.4 の ミラーリングを扱う採取票黒S切替0179です。黒S切替0179は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録黒S切替0179です。黒S切替0179ではサブスクリプション状態と取得時刻を採取票黒S切替0179へ残します。黒S切替0179では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断黒S切替0179です。黒S切替0179の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録黒S切替0179です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0178の役割を調べています。CDCミラーリング Subscription 0271の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は確認操作で状態欄を整理することでサブスクリプを確認し・遅延ゼロ確認の欠落を防ぐ。 ✅
    - B. 表示や設定で扱う内容は採取操作で照合欄を点検することでイベントログを確認し・イベント重大度の誤読を防ぐ。
    - C. 表示や設定で扱う内容は通信活動からCHC9788Iを読むことで通信活動を確認し・ホスト名変更後の購読構成を更を防ぐ。
    - D. 表示や設定で扱う内容は復旧操作で点検欄を確認することで表定義再読込を確認し・データ定義対象表の漏れを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能サブス・遅延ゼでAの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・切替）です。照合サブス・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・遅延ゼです。運用切替・ミラーでB:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸はサブス・ミラー・切替です。項目ミラー・遅延ゼでC:の性能影響の確認 STORE11は「CDC Datastoreで通信活動からCH」を述べるため、正答側の照合軸は遅延ゼ・ミラー・サブスです。仕様ミラー・サブスでD:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は切替・遅延ゼ・サブスです。用語サブス・切替という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・切替です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0178**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0178について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE058
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0178A
    ```

    画面・出力には IIDR114DD0178A が表示され、CDCミラーリング Replication Method 0178 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE058
    Mirroring request accepted
    確認コード IIDR114DD0178B
    ```

    画面・出力には IIDR114DD0178B が表示され、CDCミラーリング Replication Method 0178 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0178C
    ```

    画面・出力には IIDR114DD0178C が表示され、CDCミラーリング Replication Method 0178 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0178A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0178B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0178C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0193 {#c11-i0411}
*分類: ミラーリング*  ・  難易度: 中級

灰N収集0194ではIBM IIDR 11.4 の ミラーリングを扱う採取票灰N収集0194です。灰N収集0194は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録灰N収集0194です。灰N収集0194ではサブスクリプション状態と取得時刻を採取票灰N収集0194へ残します。灰N収集0194ではRefresh未完了の見落としを避けるため補助資料も照合する判断灰N収集0194です。灰N収集0194の用語整理では複製ミラーリングの対象値を実在出力で比較する記録灰N収集0194です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Replication Method 0193」を「複製位置管理 Subscription 0255」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は収集でサブスクリプを証跡に残し・ミラーリングの項目のサブスクリプション状態と取得時刻を記録し。 ✅
    - B. 保守作業で参照する機能は保護で16進ブックを証跡に残し・Subscriptionの16進ブックマークと取得時刻を記録。
    - C. 保守作業で参照する機能は代替経路確認でイベント一覧を証跡に残し・CDC Event Logでイベント一覧から2931を読み。
    - D. 保守作業で参照する機能は巡回でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能サブス・初期ロでAの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・収集）です。照合サブス・初期ロに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・初期ロです。運用収集・ミラーでB:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はサブス・ミラー・収集です。項目ミラー・初期ロでC:の代替経路の確認 ERR10は「CDC Event Logでイベント一覧から」を述べるため、正答側の照合軸は初期ロ・ミラー・サブスです。仕様ミラー・サブスでD:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸は収集・初期ロ・サブスです。用語サブス・収集という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・収集です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0193**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0193について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE073
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0193A
    ```

    画面・出力には IIDR114DD0193A が表示され、CDCミラーリング Replication Method 0193 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE073
    Mirroring request accepted
    確認コード IIDR114DD0193B
    ```

    画面・出力には IIDR114DD0193B が表示され、CDCミラーリング Replication Method 0193 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0193C
    ```

    画面・出力には IIDR114DD0193C が表示され、CDCミラーリング Replication Method 0193 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0193A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0193B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0193C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0208 {#c11-i0412}
*分類: ミラーリング*  ・  難易度: 中級

黄I登録0209ではIBM IIDR 11.4 の ミラーリングを扱う採取票黄I登録0209です。黄I登録0209は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録黄I登録0209です。黄I登録0209ではサブスクリプション状態と取得時刻を採取票黄I登録0209へ残します。黄I登録0209では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断黄I登録0209です。黄I登録0209の用語整理では複製ミラーリングの対象値を実在出力で区別する記録黄I登録0209です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0208を同一分類の複製位置管理 Bookmark 0249と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は主操作で出力欄を評価することで複製位置を確認し・ベンダー指示なしの位置変更を防ぐ。
    - B. 管理対象との関係を表す説明は遅延表示からBytespersecondことで遅延表示を確認し・送信回数だけでターゲット適用を防ぐ。
    - C. 管理対象との関係を表す説明は保守操作で監査欄を保存することで遅延確認を確認し・対象サブスクリプションの取りを防ぐ。
    - D. 管理対象との関係を表す説明は保守操作で監査欄を保存することでサブスクリプを確認し・対象サブスクリプションの取りを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能サブス・対象サでDの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・登録）です。照合サブス・対象サに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・対象サです。比較ミラー・登録でA:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・対象サ・登録です。運用登録・ミラーでB:の構成監査 STAT08は「CDC Communicationsで遅延表」を述べるため、正答側の照合軸はサブス・ミラー・登録です。項目ミラー・対象サでC:のCDCミラーリングは「ミラーリングの項目の遅延確認と取得時刻を記録」を述べるため、正答側の照合軸は対象サ・ミラー・サブスです。用語サブス・登録という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・登録です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0208**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0208について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE088
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0208A
    ```

    画面・出力には IIDR114DD0208A が表示され、CDCミラーリング Replication Method 0208 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE088
    Mirroring request accepted
    確認コード IIDR114DD0208B
    ```

    画面・出力には IIDR114DD0208B が表示され、CDCミラーリング Replication Method 0208 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0208C
    ```

    画面・出力には IIDR114DD0208C が表示され、CDCミラーリング Replication Method 0208 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0208A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0208B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0208C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0223 {#c11-i0413}
*分類: ミラーリング*  ・  難易度: 上級

藍D確認0224ではIBM IIDR 11.4 の ミラーリングを扱う採取票藍D確認0224です。藍D確認0224は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録藍D確認0224です。藍D確認0224ではサブスクリプション状態と取得時刻を採取票藍D確認0224へ残します。藍D確認0224ではイベント重大度の誤読を避けるため補助資料も照合する判断藍D確認0224です。藍D確認0224の用語整理では複製ミラーリングの対象値を実在出力で評価する記録藍D確認0224です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0223の設定や表示を読む前に役割を確認します。DDL後の表定義更新 Subscription 0257ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは保護でログ先頭到達を証跡に残し・後の表定義更新の項目のログ先頭到達と取得時刻を記録し。
    - B. 対象資源に対する働きは統計採取で転送条件を証跡に残し・CDC Replication が接続するソースまたはターゲ。
    - C. 対象資源に対する働きは確認でサブスクリプを証跡に残し・ミラーリングの項目のサブスクリプション状態と取得時刻を記録し。 ✅
    - D. 対象資源に対する働きは棚卸で複製位置を証跡に残し・Bookmarkの複製位置と取得時刻を記録し。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能サブス・イベンでCの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・確認）です。照合サブス・イベンに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・イベンです。比較ミラー・確認でA:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸はミラー・イベン・確認です。運用確認・ミラーでB:の統計採取 転送条件は「CDC Replication」を述べるため、正答側の照合軸はサブス・ミラー・確認です。仕様ミラー・サブスでD:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸は確認・イベン・サブスです。用語サブス・確認という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・イベン・確認です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0223**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0223について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE103
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0223A
    ```

    画面・出力には IIDR114DD0223A が表示され、CDCミラーリング Replication Method 0223 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE103
    Mirroring request accepted
    確認コード IIDR114DD0223B
    ```

    画面・出力には IIDR114DD0223B が表示され、CDCミラーリング Replication Method 0223 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0223C
    ```

    画面・出力には IIDR114DD0223C が表示され、CDCミラーリング Replication Method 0223 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0223A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0223B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0223C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0238 {#c11-i0414}
*分類: ミラーリング*  ・  難易度: 上級

黒S確認0239ではIBM IIDR 11.4 の ミラーリングを扱う採取票黒S確認0239です。黒S確認0239は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録黒S確認0239です。黒S確認0239ではサブスクリプション状態と取得時刻を採取票黒S確認0239へ残します。黒S確認0239では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断黒S確認0239です。黒S確認0239の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録黒S確認0239です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0238に関する障害切り分けの前提を確認しています。DDL後の表定義更新 Table Definition 0329の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は計画でデータ定義対を証跡に残し・後の表定義更新の項目のデータ定義対象表と取得時刻を記録し。
    - B. 表示や設定で扱う内容は確認でサブスクリプを証跡に残し・ミラーリングの項目のサブスクリプション状態と取得時刻を記録し。 ✅
    - C. 表示や設定で扱う内容は停止確認で方式変更を証跡に残し・CDC Refreshで方式変更からReturnvalueを。リフレッシュ制御 CDC Refresh 停止前の確認 REF14固有の属性も確認対象に含める。
    - D. 表示や設定で扱う内容は診断で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し・データ欠落を防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能サブス・遅延ゼでBの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・確認）です。照合サブス・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・遅延ゼです。比較ミラー・確認でA:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はミラー・遅延ゼ・確認です。項目ミラー・遅延ゼでC:の停止前の確認 REF14は「CDC Refreshで方式変更からRetu」を述べるため、正答側の照合軸は遅延ゼ・ミラー・サブスです。仕様ミラー・サブスでD:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は確認・遅延ゼ・サブスです。用語サブス・確認という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・確認です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0238**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0238について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE118
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0238A
    ```

    画面・出力には IIDR114DD0238A が表示され、CDCミラーリング Replication Method 0238 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE118
    Mirroring request accepted
    確認コード IIDR114DD0238B
    ```

    画面・出力には IIDR114DD0238B が表示され、CDCミラーリング Replication Method 0238 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0238C
    ```

    画面・出力には IIDR114DD0238C が表示され、CDCミラーリング Replication Method 0238 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0238A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0238B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0238C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0253 {#c11-i0415}
*分類: ミラーリング*  ・  難易度: 初級

灰N保護0254ではIBM IIDR 11.4 の ミラーリングを扱う採取票灰N保護0254です。灰N保護0254は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録灰N保護0254です。灰N保護0254ではサブスクリプション状態と取得時刻を採取票灰N保護0254へ残します。灰N保護0254ではRefresh未完了の見落としを避けるため補助資料も照合する判断灰N保護0254です。灰N保護0254の用語整理では複製ミラーリングの対象値を実在出力で比較する記録灰N保護0254です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0253を保守記録に説明する必要があります。DDL後の表定義更新 Table Definition 0314と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は表定義未更新を避けるため・点検操作で判定欄を記録するしてデータ定義対を照合する。
    - B. 保守作業で参照する機能は送信回数だけでターゲット適用完了を避けるため・通信統計からSendsを読むして通信統計を照合する。
    - C. 保守作業で参照する機能はデータ欠落を避けるため・監査操作で記録欄を比較するしてサブスクリプを照合する。
    - D. 保守作業で参照する機能は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するしてサブスクリプを照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能サブス・初期ロでDの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・保護）です。照合サブス・初期ロに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・初期ロです。比較ミラー・保護でA:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はミラー・初期ロ・保護です。運用保護・ミラーでB:の障害切り分け STAT04は「CDC Communicationsで通信統」を述べるため、正答側の照合軸はサブス・ミラー・保護です。項目ミラー・初期ロでC:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は初期ロ・ミラー・サブスです。用語サブス・保護という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・保護です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0253**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0253について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE013
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0253A
    ```

    画面・出力には IIDR114DD0253A が表示され、CDCミラーリング Replication Method 0253 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE013
    Mirroring request accepted
    確認コード IIDR114DD0253B
    ```

    画面・出力には IIDR114DD0253B が表示され、CDCミラーリング Replication Method 0253 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0253C
    ```

    画面・出力には IIDR114DD0253C が表示され、CDCミラーリング Replication Method 0253 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0253A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0253B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0253C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0268 {#c11-i0416}
*分類: ミラーリング*  ・  難易度: 中級

黄I照合0269ではIBM IIDR 11.4 の ミラーリングを扱う採取票黄I照合0269です。黄I照合0269は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録黄I照合0269です。黄I照合0269ではサブスクリプション状態と取得時刻を採取票黄I照合0269へ残します。黄I照合0269では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断黄I照合0269です。黄I照合0269の用語整理では複製ミラーリングの対象値を実在出力で区別する記録黄I照合0269です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0268の技術的な意味を資料で確認するとき、複製位置管理 Instance 0348との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は照合操作で確認欄を採取することで戻り値を確認し・対象インスタンスの取り違えを防ぐ。
    - B. 管理対象との関係を表す説明は状態確認で開始時刻を確認することで開始時刻を確認し・開始時刻の誤読を防ぐ。
    - C. 管理対象との関係を表す説明は記録操作で証跡欄を照合することで遅延確認を確認し・初期ロード未完了の見落としを防ぐ。CDCミラーリング Latency 0097固有の属性も確認対象に含める。
    - D. 管理対象との関係を表す説明は保守操作で監査欄を保存することでサブスクリプを確認し・対象サブスクリプションの取りを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能サブス・対象サでDの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・照合）です。照合サブス・対象サに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・対象サです。比較ミラー・照合でA:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・対象サ・照合です。運用照合・ミラーでB:の状態確認 開始時刻は「複製対象の表対応と開始位置をまとめる管理単位」を述べるため、正答側の照合軸はサブス・ミラー・照合です。項目ミラー・対象サでC:のCDCミラーリングは「ミラーリングの項目の遅延確認と取得時刻を記録」を述べるため、正答側の照合軸は対象サ・ミラー・サブスです。用語サブス・照合という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・照合です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0268**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0268について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE028
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0268A
    ```

    画面・出力には IIDR114DD0268A が表示され、CDCミラーリング Replication Method 0268 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE028
    Mirroring request accepted
    確認コード IIDR114DD0268B
    ```

    画面・出力には IIDR114DD0268B が表示され、CDCミラーリング Replication Method 0268 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0268C
    ```

    画面・出力には IIDR114DD0268C が表示され、CDCミラーリング Replication Method 0268 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0268A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0268B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0268C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0283 {#c11-i0417}
*分類: ミラーリング*  ・  難易度: 中級

藍D抑止0284ではIBM IIDR 11.4 の ミラーリングを扱う採取票藍D抑止0284です。藍D抑止0284は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録藍D抑止0284です。藍D抑止0284ではサブスクリプション状態と取得時刻を採取票藍D抑止0284へ残します。藍D抑止0284ではイベント重大度の誤読を避けるため補助資料も照合する判断藍D抑止0284です。藍D抑止0284の用語整理では複製ミラーリングの対象値を実在出力で評価する記録藍D抑止0284です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0283について構成や状態を確認します。CDCミラーリング Table Status 0340ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはミラーリングの項目の初期ロード状態と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。
    - B. 対象資源に対する働きはログ上の適用位置と時刻を追跡する複製の進行点を初期同期判定として確認する。初期同期判定で送信操作を確認するときは送信操作の誤読を防ぐ。
    - C. 対象資源に対する働きは後の表定義更新の項目の表定義再読込と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。
    - D. 対象資源に対する働きはミラーリングの項目のサブスクリプション状態と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能サブス・イベンでDの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・抑止）です。照合サブス・イベンに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・イベンです。比較ミラー・抑止でA:のTable Statusは「ミラーリングの項目の初期ロード状態と取得時刻」を述べるため、正答側の照合軸はミラー・イベン・抑止です。運用抑止・ミラーでB:の初期同期判定 送信操作は「ログ上の適用位置と時刻を追跡する複製の進行点」を述べるため、正答側の照合軸はサブス・ミラー・抑止です。項目ミラー・イベンでC:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はイベン・ミラー・サブスです。用語サブス・抑止という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・イベン・抑止です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0283**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0283について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE043
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0283A
    ```

    画面・出力には IIDR114DD0283A が表示され、CDCミラーリング Replication Method 0283 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE043
    Mirroring request accepted
    確認コード IIDR114DD0283B
    ```

    画面・出力には IIDR114DD0283B が表示され、CDCミラーリング Replication Method 0283 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0283C
    ```

    画面・出力には IIDR114DD0283C が表示され、CDCミラーリング Replication Method 0283 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0283A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0283B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0283C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0298 {#c11-i0418}
*分類: ミラーリング*  ・  難易度: 中級

黒S抑止0299ではIBM IIDR 11.4 の ミラーリングを扱う採取票黒S抑止0299です。黒S抑止0299は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録黒S抑止0299です。黒S抑止0299ではサブスクリプション状態と取得時刻を採取票黒S抑止0299へ残します。黒S抑止0299では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断黒S抑止0299です。黒S抑止0299の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録黒S抑止0299です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0298の役割を調べています。複製位置管理 Bookmark 0324の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は計画で複製位置を証跡に残し・Bookmarkの複製位置と取得時刻を記録し。
    - B. 表示や設定で扱う内容はオンライン表でオンライン表を証跡に残し・CDC Replication が接続するソースまたはターゲ。
    - C. 表示や設定で扱う内容は収集でインスタンスを証跡に残し・Hex Positionのインスタンス名と取得時刻を記録し。
    - D. 表示や設定で扱う内容は抑止でサブスクリプを証跡に残し・ミラーリングの項目のサブスクリプション状態と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能サブス・遅延ゼでDの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・抑止）です。照合サブス・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・遅延ゼです。比較ミラー・抑止でA:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・遅延ゼ・抑止です。運用抑止・ミラーでB:のマッピング検査 オンライン表示は「CDC Replication」を述べるため、正答側の照合軸はサブス・ミラー・抑止です。項目ミラー・遅延ゼでC:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は遅延ゼ・ミラー・サブスです。用語サブス・抑止という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・抑止です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0298**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0298について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE058
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0298A
    ```

    画面・出力には IIDR114DD0298A が表示され、CDCミラーリング Replication Method 0298 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE058
    Mirroring request accepted
    確認コード IIDR114DD0298B
    ```

    画面・出力には IIDR114DD0298B が表示され、CDCミラーリング Replication Method 0298 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0298C
    ```

    画面・出力には IIDR114DD0298C が表示され、CDCミラーリング Replication Method 0298 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0298A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0298B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0298C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0313 {#c11-i0419}
*分類: ミラーリング*  ・  難易度: 中級

灰N解析0314ではIBM IIDR 11.4 の ミラーリングを扱う採取票灰N解析0314です。灰N解析0314は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録灰N解析0314です。灰N解析0314ではサブスクリプション状態と取得時刻を採取票灰N解析0314へ残します。灰N解析0314ではRefresh未完了の見落としを避けるため補助資料も照合する判断灰N解析0314です。灰N解析0314の用語整理では複製ミラーリングの対象値を実在出力で比較する記録灰N解析0314です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Replication Method 0313」を「DDL後の表定義更新 Table Definition 0344」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は解除でデータ定義対を証跡に残し・後の表定義更新の項目のデータ定義対象表と取得時刻を記録し。
    - B. 保守作業で参照する機能は解析でサブスクリプを証跡に残し・ミラーリングの項目のサブスクリプション状態と取得時刻を記録し。 ✅
    - C. 保守作業で参照する機能はマッピングで変換規則を証跡に残し・CDC Replication のスクリプト操作に使うコマン。
    - D. 保守作業で参照する機能は切替で16進ブックを証跡に残し・Subscriptionの16進ブックマークと取得時刻を記録。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能サブス・初期ロでBの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・解析）です。照合サブス・初期ロに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はミラー・サブス・初期ロです。比較ミラー・解析でA:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はミラー・初期ロ・解析です。項目ミラー・初期ロでC:のマッピング検査 変換規則は「CDC Replication」を述べるため、正答側の照合軸は初期ロ・ミラー・サブスです。仕様ミラー・サブスでD:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸は解析・初期ロ・サブスです。用語サブス・解析という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・解析です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0313**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0313について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE073
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0313A
    ```

    画面・出力には IIDR114DD0313A が表示され、CDCミラーリング Replication Method 0313 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE073
    Mirroring request accepted
    確認コード IIDR114DD0313B
    ```

    画面・出力には IIDR114DD0313B が表示され、CDCミラーリング Replication Method 0313 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0313C
    ```

    画面・出力には IIDR114DD0313C が表示され、CDCミラーリング Replication Method 0313 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0313A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0313B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0313C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0328 {#c11-i0420}
*分類: ミラーリング*  ・  難易度: 中級

黄I計画0329ではIBM IIDR 11.4 の ミラーリングを扱う採取票黄I計画0329です。黄I計画0329は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録黄I計画0329です。黄I計画0329ではサブスクリプション状態と取得時刻を採取票黄I計画0329へ残します。黄I計画0329では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断黄I計画0329です。黄I計画0329の用語整理では複製ミラーリングの対象値を実在出力で区別する記録黄I計画0329です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0328を同一分類の複製状態監視 Mirror Status 代替経路の確認 MIR10と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は代替経路確認で状態表示を証跡に残し・Mirror Statusで状態表示からLatencyを読み。
    - B. 管理対象との関係を表す説明は計画でサブスクリプを証跡に残し・ミラーリングの項目のサブスクリプション状態と取得時刻を記録し。 ✅
    - C. 管理対象との関係を表す説明は容量表示で容量表示を証跡に残し・複製対象の表対応と開始位置をまとめる管理単位を遅延監視として。
    - D. 管理対象との関係を表す説明は登録でイベントログを証跡に残し・ミラーリングの項目のイベントログと取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能サブス・対象サでBの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・計画）です。照合サブス・対象サに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はサブス・計画・対象サです。比較ミラー・計画でA:の代替経路の確認 MIR10は「Mirror Statusで状態表示からLa」を述べるため、正答側の照合軸はミラー・計画・サブスです。項目ミラー・対象サでC:の遅延監視 容量表示は「複製対象の表対応と開始位置をまとめる管理単位」を述べるため、正答側の照合軸は対象サ・ミラー・サブスです。仕様ミラー・サブスでD:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸は計画・対象サ・サブスです。用語サブス・計画という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・サブス・対象サです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0328**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0328について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE088
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0328A
    ```

    画面・出力には IIDR114DD0328A が表示され、CDCミラーリング Replication Method 0328 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE088
    Mirroring request accepted
    確認コード IIDR114DD0328B
    ```

    画面・出力には IIDR114DD0328B が表示され、CDCミラーリング Replication Method 0328 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0328C
    ```

    画面・出力には IIDR114DD0328C が表示され、CDCミラーリング Replication Method 0328 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0328A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0328B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0328C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0343 {#c11-i0421}
*分類: ミラーリング*  ・  難易度: 上級

藍D解除0344ではIBM IIDR 11.4 の ミラーリングを扱う採取票藍D解除0344です。藍D解除0344は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録藍D解除0344です。藍D解除0344ではサブスクリプション状態と取得時刻を採取票藍D解除0344へ残します。藍D解除0344ではイベント重大度の誤読を避けるため補助資料も照合する判断藍D解除0344です。藍D解除0344の用語整理では複製ミラーリングの対象値を実在出力で評価する記録藍D解除0344です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0343の設定や表示を読む前に役割を確認します。サブスクリプション管理 CDC Subscription 引継ぎ記録 SUB09ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはサブスクリプで版数表示を証跡に残し・CDC Subscriptionで版数表示からReplica。
    - B. 対象資源に対する働きはリフレッシュで管理レポートを証跡に残し・対象表を初期同期または再同期する複製操作をマッピング検査とし。
    - C. 対象資源に対する働きは登録で16進ブックを証跡に残し・Subscriptionの16進ブックマークと取得時刻を記録。
    - D. 対象資源に対する働きは解除でサブスクリプを証跡に残し・ミラーリングの項目のサブスクリプション状態と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能サブス・イベンでDの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・解除）です。照合サブス・イベンに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はサブス・解除・イベンです。比較ミラー・解除でA:の引継ぎ記録 SUB09は「CDC Subscriptionで版数表示か」を述べるため、正答側の照合軸はミラー・解除・サブスです。運用解除・ミラーでB:のマッピング検査 管理レポートは「対象表を初期同期または再同期する複製操作をマ」を述べるため、正答側の照合軸はサブス・ミラー・解除です。項目ミラー・イベンでC:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はイベン・ミラー・サブスです。用語サブス・解除という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・サブス・イベンです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0343**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0343について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE103
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0343A
    ```

    画面・出力には IIDR114DD0343A が表示され、CDCミラーリング Replication Method 0343 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE103
    Mirroring request accepted
    確認コード IIDR114DD0343B
    ```

    画面・出力には IIDR114DD0343B が表示され、CDCミラーリング Replication Method 0343 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0343C
    ```

    画面・出力には IIDR114DD0343C が表示され、CDCミラーリング Replication Method 0343 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0343A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0343B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0343C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Replication Method 0358 {#c11-i0422}
*分類: ミラーリング*  ・  難易度: 上級

黒S解除0359ではIBM IIDR 11.4 の ミラーリングを扱う採取票黒S解除0359です。黒S解除0359は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録黒S解除0359です。黒S解除0359ではサブスクリプション状態と取得時刻を採取票黒S解除0359へ残します。黒S解除0359では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断黒S解除0359です。黒S解除0359の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録黒S解除0359です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Replication Method 0358に関する障害切り分けの前提を確認しています。サブスクリプション管理 CDC Subscription 権限境界の確認 SUB12の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は版数表示からReplicationを読むことで版数表示を確認し・別サブスクリプションを停止まを防ぐ。
    - B. 表示や設定で扱う内容は点検操作で判定欄を記録することでデータ定義対を確認し・表定義未更新を防ぐ。
    - C. 表示や設定で扱う内容は確認操作で状態欄を整理することでサブスクリプを確認し・遅延ゼロ確認の欠落を防ぐ。 ✅
    - D. 表示や設定で扱う内容は確認操作で状態欄を整理することでミラー開始を確認し・遅延ゼロ確認の欠落を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能サブス・遅延ゼでCの記述「ミラーリングの項目のサブスクリプション状態と取得時刻を記」に対応する項目はReplication Method（ミラー・サブス・解除）です。照合サブス・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のサブスクリプション状態と取得時刻を記録し」で、確認対象はサブス・解除・遅延ゼです。比較ミラー・解除でA:の権限境界の確認 SUB12は「CDC Subscriptionで版数表示か」を述べるため、正答側の照合軸はミラー・解除・サブスです。運用解除・ミラーでB:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はサブス・ミラー・解除です。仕様ミラー・サブスでD:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸は解除・遅延ゼ・サブスです。用語サブス・解除という用語は「ミラーリングの項目のサブスクリプション状態と取得時刻」を指し、照合する値と誤認リスクの組合せはミラー・サブス・遅延ゼです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Replication Method 0358**

    - 検証目的: CDCミラーリングのCDCミラーリング Replication Method 0358について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Replication Method と サブスクリプション状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> Management Console event log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE118
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0358A
    ```

    画面・出力には IIDR114DD0358A が表示され、CDCミラーリング Replication Method 0358 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE118
    Mirroring request accepted
    確認コード IIDR114DD0358B
    ```

    画面・出力には IIDR114DD0358B が表示され、CDCミラーリング Replication Method 0358 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Replication Method を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0358C
    ```

    画面・出力には IIDR114DD0358C が表示され、CDCミラーリング Replication Method 0358 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0358A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0358B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0358C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0001 {#c11-i0423}
*分類: ミラーリング*  ・  難易度: 初級

橙B巡回0002ではIBM IIDR 11.4 の ミラーリングを扱う採取票橙B巡回0002です。橙B巡回0002は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録橙B巡回0002です。橙B巡回0002ではイベントログと取得時刻を採取票橙B巡回0002へ残します。橙B巡回0002ではRefresh未完了の見落としを避けるため補助資料も照合する判断橙B巡回0002です。橙B巡回0002の用語整理では複製ミラーリングの対象値を実在出力で比較する記録橙B巡回0002です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Subscription 0001」を「CDCミラーリング Table Status 0085」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は記録操作で証跡欄を照合することでRefresを確認し・Refresh未完了の見落とを防ぐ。
    - B. 保守作業で参照する機能は記録操作で証跡欄を照合することで遅延確認を確認し・Refresh未完了の見落とを防ぐ。
    - C. 保守作業で参照する機能は記録操作で証跡欄を照合することでイベントログを確認し・Refresh未完了の見落とを防ぐ。 ✅
    - D. 保守作業で参照する機能は接続表示からDatastoreを読むことで接続表示を確認し・ホスト名変更後の購読構成を更を防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 巡回・イベン・RefrでCの記述「CDCのイベントログと取得時刻を記録し、Refresh未完了の見落と」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・Refr・巡回）です。巡回時のイベントロに関するミラーリングの仕様は「CDCのイベントログと取得時刻を記録し、Refresh未完了の見落と」で、確認対象はミラー・イベン・Refr・巡回です。ミラ・変更・RefrのA:は「CDCのRefresh状態と取得時刻を記録し」を述べ、対象はTable Status（ミラー・Ref・Refr・変更）です。照合・遅延確・RefrのB:は「CDCの遅延確認と取得時刻を記録し、Refresh未完了の見落としを」を述べ、対象はCDCミラーリング Latency（ミラー・遅延確・Refr・照合）です。接続表示をデータストのD:は「CDC Datastoreで接続表示からDatastoreを読み」を述べ、対象は障害切り分け STORE04（CDC・接続表・ホスト名・データ）です。イベントロを巡回という用語は「CDCのイベントログと取得時刻を記録し」を指し、CDCミラーリング Subscrip（ミラー・イベン・Refr・巡回）で照合する値はイベントログです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0001**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0001について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE001
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0001A
    ```

    画面・出力には IIDR114DD0001A が表示され、CDCミラーリング Subscription 0001 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE001
    Mirroring request accepted
    確認コード IIDR114DD0001B
    ```

    画面・出力には IIDR114DD0001B が表示され、CDCミラーリング Subscription 0001 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0001C
    ```

    画面・出力には IIDR114DD0001C が表示され、CDCミラーリング Subscription 0001 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0001A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0001B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0001C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0016 {#c11-i0424}
*分類: ミラーリング*  ・  難易度: 初級

青Q巡回0017ではIBM IIDR 11.4 の ミラーリングを扱う採取票青Q巡回0017です。青Q巡回0017は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録青Q巡回0017です。青Q巡回0017ではイベントログと取得時刻を採取票青Q巡回0017へ残します。青Q巡回0017では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断青Q巡回0017です。青Q巡回0017の用語整理では複製ミラーリングの対象値を実在出力で区別する記録青Q巡回0017です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0016を同一分類のDDL後の表定義更新 Subscription 0107と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてイベントログを照合する。 ✅
    - B. 管理対象との関係を表す説明はRefresh中の再開を避けるため・表示操作で対象欄を追跡するしてログ先頭到達を照合する。
    - C. 管理対象との関係を表す説明は対象インスタンスの取り違えを避けるため・照合操作で確認欄を採取するして複製位置を照合する。
    - D. 管理対象との関係を表す説明は送信回数だけでターゲット適用完了を避けるため・遅延表示からBytespersecondして遅延表示を照合する。

    正解: **A** ／ 難易度: 初級

    **解説:** 巡回・イベン・対象サブでAの記述「CDCのイベントログと取得時刻を記録し、対象サブスクリプションの取り」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・対象サブ・巡回）です。巡回時のイベントロに関するミラーリングの仕様は「CDCのイベントログと取得時刻を記録し、対象サブスクリプションの取り」で、確認対象はミラー・イベン・対象サブ・巡回です。移行・ログ先・RefrのB:は「DDLのログ先頭到達と取得時刻を記録し、Refresh中の再開を防ぐ」を述べ、対象はDDL後の表定義更新（後の表・ログ先・Refr・移行）です。照合時の複製位置のC:は「Bookmarkの複製位置と取得時刻を記録し」を述べ、対象は複製位置管理 Bookmark（Boo・複製位・対象イン・照合）です。遅延表示を復旧準備のD:は「CDC Communicationsで遅延表示からBytespers」を述べ、対象は復旧準備 STAT05（CDC・遅延表・送信回数・復旧準）です。イベントロを巡回という用語は「CDCのイベントログと取得時刻を記録し」を指し、CDCミラーリング Subscrip（ミラー・イベン・対象サブ・巡回）で照合する値はイベントログです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0016**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0016について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE016
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0016A
    ```

    画面・出力には IIDR114DD0016A が表示され、CDCミラーリング Subscription 0016 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE016
    Mirroring request accepted
    確認コード IIDR114DD0016B
    ```

    画面・出力には IIDR114DD0016B が表示され、CDCミラーリング Subscription 0016 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0016C
    ```

    画面・出力には IIDR114DD0016C が表示され、CDCミラーリング Subscription 0016 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0016A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0016B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0016C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0031 {#c11-i0425}
*分類: ミラーリング*  ・  難易度: 中級

白L棚卸0032ではIBM IIDR 11.4 の ミラーリングを扱う採取票白L棚卸0032です。白L棚卸0032は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録白L棚卸0032です。白L棚卸0032ではイベントログと取得時刻を採取票白L棚卸0032へ残します。白L棚卸0032ではイベント重大度の誤読を避けるため補助資料も照合する判断白L棚卸0032です。白L棚卸0032の用語整理では複製ミラーリングの対象値を実在出力で評価する記録白L棚卸0032です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0031の設定や表示を読む前に役割を確認します。DDL後の表定義更新 Table Definition 0089ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは復旧操作で点検欄を確認することでデータ定義対を確認し・データ定義対象表の漏れを防ぐ。
    - B. 対象資源に対する働きは復旧操作で点検欄を確認することでサブスクリプを確認し・データ定義対象表の漏れを防ぐ。
    - C. 対象資源に対する働きは採取操作で照合欄を点検することでイベントログを確認し・イベント重大度の誤読を防ぐ。 ✅
    - D. 対象資源に対する働きは完了確認からRowsappliedを読むことで完了確認を確認し・初期ロード未完了でMirroを防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能イベン・イベンでCの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・棚卸）です。照合イベン・イベンに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・イベンです。比較ミラー・棚卸でA:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はミラー・イベン・棚卸です。運用棚卸・ミラーでB:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はイベン・ミラー・棚卸です。仕様ミラー・イベンでD:の復旧後の確認 REF06は「CDC Refreshで完了確認からRows」を述べるため、正答側の照合軸は棚卸・イベン・イベンです。用語イベン・棚卸という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・棚卸です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0031**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0031について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE031
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0031A
    ```

    画面・出力には IIDR114DD0031A が表示され、CDCミラーリング Subscription 0031 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE031
    Mirroring request accepted
    確認コード IIDR114DD0031B
    ```

    画面・出力には IIDR114DD0031B が表示され、CDCミラーリング Subscription 0031 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0031C
    ```

    画面・出力には IIDR114DD0031C が表示され、CDCミラーリング Subscription 0031 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0031A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0031B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0031C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0046 {#c11-i0426}
*分類: ミラーリング*  ・  難易度: 中級

紫G復旧0047ではIBM IIDR 11.4 の ミラーリングを扱う採取票紫G復旧0047です。紫G復旧0047は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紫G復旧0047です。紫G復旧0047ではイベントログと取得時刻を採取票紫G復旧0047へ残します。紫G復旧0047では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紫G復旧0047です。紫G復旧0047の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紫G復旧0047です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0046に関する障害切り分けの前提を確認しています。DDL後の表定義更新 Subscription 0077の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は監査でログ先頭到達を証跡に残し・後の表定義更新の項目のログ先頭到達と取得時刻を記録し。
    - B. 表示や設定で扱う内容は解析でデータ定義対を証跡に残し・後の表定義更新の項目のデータ定義対象表と取得時刻を記録し。
    - C. 表示や設定で扱う内容は復旧でイベントログを証跡に残し・ミラーリングの項目のイベントログと取得時刻を記録し。 ✅
    - D. 表示や設定で扱う内容は状態確認で文字変換を証跡に残し・ソース表とターゲット表の対応および列変換を示す定義。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能イベン・遅延ゼでCの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・復旧）です。照合イベン・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・遅延ゼです。比較ミラー・復旧でA:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸はミラー・遅延ゼ・復旧です。運用復旧・ミラーでB:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はイベン・ミラー・復旧です。仕様ミラー・イベンでD:の状態確認 文字変換は「ソース表とターゲット表の対応および列変換を示」を述べるため、正答側の照合軸は復旧・遅延ゼ・イベンです。用語イベン・復旧という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・復旧です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0046**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0046について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE046
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0046A
    ```

    画面・出力には IIDR114DD0046A が表示され、CDCミラーリング Subscription 0046 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE046
    Mirroring request accepted
    確認コード IIDR114DD0046B
    ```

    画面・出力には IIDR114DD0046B が表示され、CDCミラーリング Subscription 0046 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0046C
    ```

    画面・出力には IIDR114DD0046C が表示され、CDCミラーリング Subscription 0046 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0046A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0046B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0046C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0061 {#c11-i0427}
*分類: ミラーリング*  ・  難易度: 中級

橙B監査0062ではIBM IIDR 11.4 の ミラーリングを扱う採取票橙B監査0062です。橙B監査0062は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録橙B監査0062です。橙B監査0062ではイベントログと取得時刻を採取票橙B監査0062へ残します。橙B監査0062ではRefresh未完了の見落としを避けるため補助資料も照合する判断橙B監査0062です。橙B監査0062の用語整理では複製ミラーリングの対象値を実在出力で比較する記録橙B監査0062です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0061を保守記録に説明する必要があります。DDL後の表定義更新 Refresh Table 0143と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は後の表定義更新の項目の再開条件と取得時刻を記録し・初期ロード中の再開を防ぐである。表示操作で対象欄を追跡するときは初期ロード中の再開を防ぐ。
    - B. 保守作業で参照する機能はミラーリングの項目のイベントログと取得時刻を記録し・初期ロード未完了の見落としを防ぐである。記録操作で証跡欄を照合するときは初期ロード未完了の見落としを防ぐ。 ✅
    - C. 保守作業で参照する機能は後の表定義更新の項目の表定義再読込と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。DDL後の表定義更新 Source Table 0290固有の属性も確認対象に含める。
    - D. 保守作業で参照する機能はCDC Replication のスクリプト操作に使うコマンドライン機能である。復旧手掛かりで復旧手掛かりを確認するときは復旧手掛かりの誤読を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能イベン・初期ロでBの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・監査）です。照合イベン・初期ロに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・初期ロです。比較ミラー・監査でA:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸はミラー・初期ロ・監査です。項目ミラー・初期ロでC:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は初期ロ・ミラー・イベンです。仕様ミラー・イベンでD:の状態確認 復旧手掛かりは「CDC Replication」を述べるため、正答側の照合軸は監査・初期ロ・イベンです。用語イベン・監査という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・監査です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0061**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0061について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE061
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0061A
    ```

    画面・出力には IIDR114DD0061A が表示され、CDCミラーリング Subscription 0061 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE061
    Mirroring request accepted
    確認コード IIDR114DD0061B
    ```

    画面・出力には IIDR114DD0061B が表示され、CDCミラーリング Subscription 0061 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0061C
    ```

    画面・出力には IIDR114DD0061C が表示され、CDCミラーリング Subscription 0061 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0061A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0061B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0061C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0076 {#c11-i0428}
*分類: ミラーリング*  ・  難易度: 中級

青Q監査0077ではIBM IIDR 11.4 の ミラーリングを扱う採取票青Q監査0077です。青Q監査0077は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録青Q監査0077です。青Q監査0077ではイベントログと取得時刻を採取票青Q監査0077へ残します。青Q監査0077では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断青Q監査0077です。青Q監査0077の用語整理では複製ミラーリングの対象値を実在出力で区別する記録青Q監査0077です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0076の技術的な意味を資料で確認するとき、複製位置管理 Bookmark 0159との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はBookmarkの複製位置と取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。複製位置管理 Bookmark 0159固有の属性も確認対象に含める。
    - B. 管理対象との関係を表す説明は後の表定義更新の項目のサブスクリプション記述と取得時刻を記録し・初期ロード中の再開を防ぐである。表示操作で対象欄を追跡するときは初期ロード中の再開を防ぐ。
    - C. 管理対象との関係を表す説明はターゲットへ変更を反映し適用済み位置を記録する処理である。性能統計で活動ログを確認するときは活動ログの誤読を防ぐ。
    - D. 管理対象との関係を表す説明はミラーリングの項目のイベントログと取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能イベン・対象サでDの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・監査）です。照合イベン・対象サに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・対象サです。比較ミラー・監査でA:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・対象サ・監査です。運用監査・ミラーでB:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はイベン・ミラー・監査です。項目ミラー・対象サでC:の開始位置指定 活動ログは「ターゲットへ変更を反映し適用済み位置を記録す」を述べるため、正答側の照合軸は対象サ・ミラー・イベンです。用語イベン・監査という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・監査です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0076**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0076について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE076
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0076A
    ```

    画面・出力には IIDR114DD0076A が表示され、CDCミラーリング Subscription 0076 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE076
    Mirroring request accepted
    確認コード IIDR114DD0076B
    ```

    画面・出力には IIDR114DD0076B が表示され、CDCミラーリング Subscription 0076 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0076C
    ```

    画面・出力には IIDR114DD0076C が表示され、CDCミラーリング Subscription 0076 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0076A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0076B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0076C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0091 {#c11-i0429}
*分類: ミラーリング*  ・  難易度: 中級

白L変更0092ではIBM IIDR 11.4 の ミラーリングを扱う採取票白L変更0092です。白L変更0092は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録白L変更0092です。白L変更0092ではイベントログと取得時刻を採取票白L変更0092へ残します。白L変更0092ではイベント重大度の誤読を避けるため補助資料も照合する判断白L変更0092です。白L変更0092の用語整理では複製ミラーリングの対象値を実在出力で評価する記録白L変更0092です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0091について構成や状態を確認します。複製位置管理 Hex Position 0186ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは変更確認操作で採取欄を棚卸することでインスタンスを確認し・重複反映を防ぐ。
    - B. 対象資源に対する働きは監査操作で記録欄を比較することでサブスクリプを確認し・データ欠落を防ぐ。
    - C. 対象資源に対する働きは診断採取で診断採取を確認することで診断採取を確認し・診断採取の誤読を防ぐ。performance statistics 遅延監視 診断採取固有の属性も確認対象に含める。
    - D. 対象資源に対する働きは採取操作で照合欄を点検することでイベントログを確認し・イベント重大度の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能イベン・イベンでDの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・変更）です。照合イベン・イベンに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・イベンです。比較ミラー・変更でA:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸はミラー・イベン・変更です。運用変更・ミラーでB:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸はイベン・ミラー・変更です。項目ミラー・イベンでC:の遅延監視 診断採取は「サブスクリプションやデータストアの処理量と遅」を述べるため、正答側の照合軸はイベン・ミラー・イベンです。用語イベン・変更という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・変更です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0091**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0091について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE091
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0091A
    ```

    画面・出力には IIDR114DD0091A が表示され、CDCミラーリング Subscription 0091 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE091
    Mirroring request accepted
    確認コード IIDR114DD0091B
    ```

    画面・出力には IIDR114DD0091B が表示され、CDCミラーリング Subscription 0091 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0091C
    ```

    画面・出力には IIDR114DD0091C が表示され、CDCミラーリング Subscription 0091 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0091A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0091B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0091C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0106 {#c11-i0430}
*分類: ミラーリング*  ・  難易度: 上級

紫G移行0107ではIBM IIDR 11.4 の ミラーリングを扱う採取票紫G移行0107です。紫G移行0107は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紫G移行0107です。紫G移行0107ではイベントログと取得時刻を採取票紫G移行0107へ残します。紫G移行0107では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紫G移行0107です。紫G移行0107の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紫G移行0107です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0106の役割を調べています。複製位置管理 Subscription 0165の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は移行でイベントログを証跡に残し・ミラーリングの項目のイベントログと取得時刻を記録し。 ✅
    - B. 表示や設定で扱う内容は切替で16進ブックを証跡に残し・Subscriptionの16進ブックマークと取得時刻を記録。
    - C. 表示や設定で扱う内容は解除でサブスクリプを証跡に残し・後の表定義更新の項目のサブスクリプション記述と取得時刻を記録。
    - D. 表示や設定で扱う内容は巡回で初期ロード状を証跡に残し・ミラーリングの項目の初期ロード状態と取得時刻を記録し。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能イベン・遅延ゼでAの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・移行）です。照合イベン・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・遅延ゼです。運用移行・ミラーでB:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はイベン・ミラー・移行です。項目ミラー・遅延ゼでC:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は遅延ゼ・ミラー・イベンです。仕様ミラー・イベンでD:のTable Statusは「ミラーリングの項目の初期ロード状態と取得時刻」を述べるため、正答側の照合軸は移行・遅延ゼ・イベンです。用語イベン・移行という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・移行です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0106**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0106について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE106
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0106A
    ```

    画面・出力には IIDR114DD0106A が表示され、CDCミラーリング Subscription 0106 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE106
    Mirroring request accepted
    確認コード IIDR114DD0106B
    ```

    画面・出力には IIDR114DD0106B が表示され、CDCミラーリング Subscription 0106 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0106C
    ```

    画面・出力には IIDR114DD0106C が表示され、CDCミラーリング Subscription 0106 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0106A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0106B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0106C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0121 {#c11-i0431}
*分類: ミラーリング*  ・  難易度: 初級

橙B診断0122ではIBM IIDR 11.4 の ミラーリングを扱う採取票橙B診断0122です。橙B診断0122は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録橙B診断0122です。橙B診断0122ではイベントログと取得時刻を採取票橙B診断0122へ残します。橙B診断0122ではRefresh未完了の見落としを避けるため補助資料も照合する判断橙B診断0122です。橙B診断0122の用語整理では複製ミラーリングの対象値を実在出力で比較する記録橙B診断0122です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Subscription 0121」を「CDCミラーリング Event Severity 0169」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は診断でイベントログを証跡に残し・ミラーリングの項目のイベントログと取得時刻を記録し。 ✅
    - B. 保守作業で参照する機能は切替でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。
    - C. 保守作業で参照する機能は復旧準備でイベント表示を証跡に残し・CDC Subscriptionでイベント表示からSever。
    - D. 保守作業で参照する機能は巡回で16進ブックを証跡に残し・Subscriptionの16進ブックマークと取得時刻を記録。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能イベン・初期ロでAの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・診断）です。照合イベン・初期ロに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・初期ロです。運用診断・ミラーでB:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸はイベン・ミラー・診断です。項目ミラー・初期ロでC:の復旧準備 SUB05は「CDC Subscriptionでイベント表」を述べるため、正答側の照合軸は初期ロ・ミラー・イベンです。仕様ミラー・イベンでD:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸は診断・初期ロ・イベンです。用語イベン・診断という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・診断です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0121**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0121について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE001
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0121A
    ```

    画面・出力には IIDR114DD0121A が表示され、CDCミラーリング Subscription 0121 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE001
    Mirroring request accepted
    確認コード IIDR114DD0121B
    ```

    画面・出力には IIDR114DD0121B が表示され、CDCミラーリング Subscription 0121 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0121C
    ```

    画面・出力には IIDR114DD0121C が表示され、CDCミラーリング Subscription 0121 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0121A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0121B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0121C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0136 {#c11-i0432}
*分類: ミラーリング*  ・  難易度: 初級

青Q診断0137ではIBM IIDR 11.4 の ミラーリングを扱う採取票青Q診断0137です。青Q診断0137は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録青Q診断0137です。青Q診断0137ではイベントログと取得時刻を採取票青Q診断0137へ残します。青Q診断0137では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断青Q診断0137です。青Q診断0137の用語整理では複製ミラーリングの対象値を実在出力で区別する記録青Q診断0137です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0136を同一分類の複製位置管理 Locale 0147と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はLocaleのサブスクリプション名と取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。
    - B. 管理対象との関係を表す説明はミラーリングの項目のイベントログと取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。 ✅
    - C. 管理対象との関係を表す説明はCDC Subscriptionで版数表示からReplicationを読みである。版数表示からReplicationをときは別サブスクリプションを停止まを防ぐ。サブスクリプション管理 CDC Subscription固有の属性も確認対象に含める。
    - D. 管理対象との関係を表す説明は後の表定義更新の項目の表定義再読込と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能イベン・対象サでBの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・診断）です。照合イベン・対象サに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・対象サです。比較ミラー・診断でA:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸はミラー・対象サ・診断です。項目ミラー・対象サでC:の再始動後の確認 SUB15は「CDC Subscriptionで版数表示か」を述べるため、正答側の照合軸は対象サ・ミラー・イベンです。仕様ミラー・イベンでD:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は診断・対象サ・イベンです。用語イベン・診断という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・診断です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0136**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0136について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE016
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0136A
    ```

    画面・出力には IIDR114DD0136A が表示され、CDCミラーリング Subscription 0136 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE016
    Mirroring request accepted
    確認コード IIDR114DD0136B
    ```

    画面・出力には IIDR114DD0136B が表示され、CDCミラーリング Subscription 0136 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0136C
    ```

    画面・出力には IIDR114DD0136C が表示され、CDCミラーリング Subscription 0136 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0136A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0136B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0136C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0151 {#c11-i0433}
*分類: ミラーリング*  ・  難易度: 中級

白L保守0152ではIBM IIDR 11.4 の ミラーリングを扱う採取票白L保守0152です。白L保守0152は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録白L保守0152です。白L保守0152ではイベントログと取得時刻を採取票白L保守0152へ残します。白L保守0152ではイベント重大度の誤読を避けるため補助資料も照合する判断白L保守0152です。白L保守0152の用語整理では複製ミラーリングの対象値を実在出力で評価する記録白L保守0152です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0151の設定や表示を読む前に役割を確認します。DDL後の表定義更新 Subscription 0227ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは表示操作で対象欄を追跡することでログ先頭到達を確認し・初期ロード中の再開を防ぐ。
    - B. 対象資源に対する働きはイベント表示からheadoflogを読むことでイベント表示を確認し・初期ロード中の表をMirroを防ぐ。
    - C. 対象資源に対する働きは採取操作で照合欄を点検することでイベントログを確認し・イベント重大度の誤読を防ぐ。 ✅
    - D. 対象資源に対する働きはオンライン表でオンライン表を確認することでオンライン表を確認し・オンライン表の誤読を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能イベン・イベンでCの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・保守）です。照合イベン・イベンに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・イベンです。比較ミラー・保守でA:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸はミラー・イベン・保守です。運用保守・ミラーでB:の停止前の確認 MIR14は「Mirror Statusでイベント表示から」を述べるため、正答側の照合軸はイベン・ミラー・保守です。仕様ミラー・イベンでD:のマッピング検査 オンライン表示は「CDC Replication」を述べるため、正答側の照合軸は保守・イベン・イベンです。用語イベン・保守という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・保守です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0151**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0151について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE031
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0151A
    ```

    画面・出力には IIDR114DD0151A が表示され、CDCミラーリング Subscription 0151 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE031
    Mirroring request accepted
    確認コード IIDR114DD0151B
    ```

    画面・出力には IIDR114DD0151B が表示され、CDCミラーリング Subscription 0151 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0151C
    ```

    画面・出力には IIDR114DD0151C が表示され、CDCミラーリング Subscription 0151 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0151A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0151B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0151C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0166 {#c11-i0434}
*分類: ミラーリング*  ・  難易度: 中級

紫G切替0167ではIBM IIDR 11.4 の ミラーリングを扱う採取票紫G切替0167です。紫G切替0167は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紫G切替0167です。紫G切替0167ではイベントログと取得時刻を採取票紫G切替0167へ残します。紫G切替0167では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紫G切替0167です。紫G切替0167の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紫G切替0167です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0166に関する障害切り分けの前提を確認しています。複製位置管理 Instance 0198の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は変更確認操作で採取欄を棚卸することで戻り値を確認し・重複反映を防ぐ。
    - B. 表示や設定で扱う内容はイベント確認からcommunicatioことでイベント確認を確認し・ホスト名変更後の購読構成を更を防ぐ。
    - C. 表示や設定で扱う内容はブックマークで分散定義を確認することで分散定義を確認し・分散定義の誤読を防ぐ。
    - D. 表示や設定で扱う内容は確認操作で状態欄を整理することでイベントログを確認し・遅延ゼロ確認の欠落を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能イベン・遅延ゼでDの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・切替）です。照合イベン・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・遅延ゼです。比較ミラー・切替でA:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・遅延ゼ・切替です。運用切替・ミラーでB:の変更後の確認 STORE03は「CDC Datastoreでイベント確認から」を述べるため、正答側の照合軸はイベン・ミラー・切替です。項目ミラー・遅延ゼでC:の失敗時切り分け 分散定義は「CDC Replication」を述べるため、正答側の照合軸は遅延ゼ・ミラー・イベンです。用語イベン・切替という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・切替です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0166**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0166について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE046
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0166A
    ```

    画面・出力には IIDR114DD0166A が表示され、CDCミラーリング Subscription 0166 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE046
    Mirroring request accepted
    確認コード IIDR114DD0166B
    ```

    画面・出力には IIDR114DD0166B が表示され、CDCミラーリング Subscription 0166 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0166C
    ```

    画面・出力には IIDR114DD0166C が表示され、CDCミラーリング Subscription 0166 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0166A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0166B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0166C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0181 {#c11-i0435}
*分類: ミラーリング*  ・  難易度: 中級

橙B収集0182ではIBM IIDR 11.4 の ミラーリングを扱う採取票橙B収集0182です。橙B収集0182は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録橙B収集0182です。橙B収集0182ではイベントログと取得時刻を採取票橙B収集0182へ残します。橙B収集0182ではRefresh未完了の見落としを避けるため補助資料も照合する判断橙B収集0182です。橙B収集0182の用語整理では複製ミラーリングの対象値を実在出力で比較する記録橙B収集0182です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0181を保守記録に説明する必要があります。複製位置管理 Subscription 0225と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はSubscriptionの16進ブックマークと取得時刻を記録し・ベンダー指示なしの位置変更を防ぐである。主操作で出力欄を評価するときはベンダー指示なしの位置変更を防ぐ。
    - B. 保守作業で参照する機能はCDC Event Logで通信エラーからERRORを読み・ERRORとSupportを照合する。通信エラーからERRORを読むときは情報イベントと停止を伴うエラを防ぐ。
    - C. 保守作業で参照する機能は後の表定義更新の項目のログ先頭到達と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。
    - D. 保守作業で参照する機能はミラーリングの項目のイベントログと取得時刻を記録し・初期ロード未完了の見落としを防ぐである。記録操作で証跡欄を照合するときは初期ロード未完了の見落としを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能イベン・初期ロでDの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・収集）です。照合イベン・初期ロに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・初期ロです。比較ミラー・収集でA:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はミラー・初期ロ・収集です。運用収集・ミラーでB:の性能影響の確認 ERR11は「CDC Event Logで通信エラーからE」を述べるため、正答側の照合軸はイベン・ミラー・収集です。項目ミラー・初期ロでC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は初期ロ・ミラー・イベンです。用語イベン・収集という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・収集です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0181**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0181について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE061
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0181A
    ```

    画面・出力には IIDR114DD0181A が表示され、CDCミラーリング Subscription 0181 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE061
    Mirroring request accepted
    確認コード IIDR114DD0181B
    ```

    画面・出力には IIDR114DD0181B が表示され、CDCミラーリング Subscription 0181 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0181C
    ```

    画面・出力には IIDR114DD0181C が表示され、CDCミラーリング Subscription 0181 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0181A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0181B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0181C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0196 {#c11-i0436}
*分類: ミラーリング*  ・  難易度: 中級

青Q収集0197ではIBM IIDR 11.4 の ミラーリングを扱う採取票青Q収集0197です。青Q収集0197は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録青Q収集0197です。青Q収集0197ではイベントログと取得時刻を採取票青Q収集0197へ残します。青Q収集0197では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断青Q収集0197です。青Q収集0197の用語整理では複製ミラーリングの対象値を実在出力で区別する記録青Q収集0197です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0196の技術的な意味を資料で確認するとき、複製位置管理 Locale 0282との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は抑止でサブスクリプを証跡に残し・Localeのサブスクリプション名と取得時刻を記録し。
    - B. 管理対象との関係を表す説明は収集でイベントログを証跡に残し・ミラーリングの項目のイベントログと取得時刻を記録し。 ✅
    - C. 管理対象との関係を表す説明はリフレッシュで完了確認を証跡に残し・CDC Refreshで完了確認からRowsappliedを。
    - D. 管理対象との関係を表す説明は復旧で再開条件を証跡に残し・後の表定義更新の項目の再開条件と取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能イベン・対象サでBの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・収集）です。照合イベン・対象サに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・対象サです。比較ミラー・収集でA:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸はミラー・対象サ・収集です。項目ミラー・対象サでC:の引継ぎ記録 REF09は「CDC Refreshで完了確認からRows」を述べるため、正答側の照合軸は対象サ・ミラー・イベンです。仕様ミラー・イベンでD:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は収集・対象サ・イベンです。用語イベン・収集という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・収集です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0196**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0196について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE076
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0196A
    ```

    画面・出力には IIDR114DD0196A が表示され、CDCミラーリング Subscription 0196 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE076
    Mirroring request accepted
    確認コード IIDR114DD0196B
    ```

    画面・出力には IIDR114DD0196B が表示され、CDCミラーリング Subscription 0196 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0196C
    ```

    画面・出力には IIDR114DD0196C が表示され、CDCミラーリング Subscription 0196 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0196A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0196B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0196C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0211 {#c11-i0437}
*分類: ミラーリング*  ・  難易度: 中級

白L登録0212ではIBM IIDR 11.4 の ミラーリングを扱う採取票白L登録0212です。白L登録0212は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録白L登録0212です。白L登録0212ではイベントログと取得時刻を採取票白L登録0212へ残します。白L登録0212ではイベント重大度の誤読を避けるため補助資料も照合する判断白L登録0212です。白L登録0212の用語整理では複製ミラーリングの対象値を実在出力で評価する記録白L登録0212です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0211について構成や状態を確認します。DDL後の表定義更新 Source Table 0290ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてイベントログを照合する。 ✅
    - B. 対象資源に対する働きは表定義未更新を避けるため・点検操作で判定欄を記録するして表定義再読込を照合する。
    - C. 対象資源に対する働きは休止購読を見落として必要ログを削を避けるため・支援情報からReturnvalueを読むして支援情報を照合する。
    - D. 対象資源に対する働きは表定義未更新を避けるため・点検操作で判定欄を記録するしてサブスクリプを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能イベン・イベンでAの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・登録）です。照合イベン・イベンに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・イベンです。運用登録・ミラーでB:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はイベン・ミラー・登録です。項目ミラー・イベンでC:の引継ぎ記録 LOG09は「Log Dependencyで支援情報からR」を述べるため、正答側の照合軸はイベン・ミラー・イベンです。仕様ミラー・イベンでD:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は登録・イベン・イベンです。用語イベン・登録という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・登録です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0211**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0211について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE091
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0211A
    ```

    画面・出力には IIDR114DD0211A が表示され、CDCミラーリング Subscription 0211 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE091
    Mirroring request accepted
    確認コード IIDR114DD0211B
    ```

    画面・出力には IIDR114DD0211B が表示され、CDCミラーリング Subscription 0211 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0211C
    ```

    画面・出力には IIDR114DD0211C が表示され、CDCミラーリング Subscription 0211 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0211A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0211B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0211C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0226 {#c11-i0438}
*分類: ミラーリング*  ・  難易度: 上級

紫G確認0227ではIBM IIDR 11.4 の ミラーリングを扱う採取票紫G確認0227です。紫G確認0227は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紫G確認0227です。紫G確認0227ではイベントログと取得時刻を採取票紫G確認0227へ残します。紫G確認0227では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紫G確認0227です。紫G確認0227の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紫G確認0227です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0226の役割を調べています。DDL後の表定義更新 Subscription 0302の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は表定義未更新を避けるため・点検操作で判定欄を記録するしてログ先頭到達を照合する。
    - B. 表示や設定で扱う内容は復旧手掛かりの誤読を避けるため・復旧手掛かりで復旧手掛かりを確認するして復旧手掛かりを照合する。
    - C. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてイベントログを照合する。 ✅
    - D. 表示や設定で扱う内容は表定義未更新を避けるため・点検操作で判定欄を記録するしてデータ定義対を照合する。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能イベン・遅延ゼでCの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・確認）です。照合イベン・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・遅延ゼです。比較ミラー・確認でA:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸はミラー・遅延ゼ・確認です。運用確認・ミラーでB:の状態確認 復旧手掛かりは「CDC Replication」を述べるため、正答側の照合軸はイベン・ミラー・確認です。仕様ミラー・イベンでD:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸は確認・遅延ゼ・イベンです。用語イベン・確認という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・確認です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0226**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0226について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE106
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0226A
    ```

    画面・出力には IIDR114DD0226A が表示され、CDCミラーリング Subscription 0226 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE106
    Mirroring request accepted
    確認コード IIDR114DD0226B
    ```

    画面・出力には IIDR114DD0226B が表示され、CDCミラーリング Subscription 0226 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0226C
    ```

    画面・出力には IIDR114DD0226C が表示され、CDCミラーリング Subscription 0226 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0226A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0226B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0226C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0241 {#c11-i0439}
*分類: ミラーリング*  ・  難易度: 初級

橙B保護0242ではIBM IIDR 11.4 の ミラーリングを扱う採取票橙B保護0242です。橙B保護0242は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録橙B保護0242です。橙B保護0242ではイベントログと取得時刻を採取票橙B保護0242へ残します。橙B保護0242ではRefresh未完了の見落としを避けるため補助資料も照合する判断橙B保護0242です。橙B保護0242の用語整理では複製ミラーリングの対象値を実在出力で比較する記録橙B保護0242です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Subscription 0241」を「複製位置管理 Hex Position 0246」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は重複反映を避けるため・変更確認操作で採取欄を棚卸するしてインスタンスを照合する。
    - B. 保守作業で参照する機能は取得間隔の誤読を避けるため・初期同期判定で取得間隔を確認するして取得間隔を照合する。
    - C. 保守作業で参照する機能は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するしてミラー開始を照合する。CDCミラーリング Event Severity 0109固有の属性も確認対象に含める。
    - D. 保守作業で参照する機能は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するしてイベントログを照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能イベン・初期ロでDの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・保護）です。照合イベン・初期ロに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・初期ロです。比較ミラー・保護でA:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸はミラー・初期ロ・保護です。運用保護・ミラーでB:の初期同期判定 取得間隔は「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸はイベン・ミラー・保護です。項目ミラー・初期ロでC:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸は初期ロ・ミラー・イベンです。用語イベン・保護という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・保護です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0241**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0241について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE001
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0241A
    ```

    画面・出力には IIDR114DD0241A が表示され、CDCミラーリング Subscription 0241 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE001
    Mirroring request accepted
    確認コード IIDR114DD0241B
    ```

    画面・出力には IIDR114DD0241B が表示され、CDCミラーリング Subscription 0241 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0241C
    ```

    画面・出力には IIDR114DD0241C が表示され、CDCミラーリング Subscription 0241 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0241A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0241B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0241C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0256 {#c11-i0440}
*分類: ミラーリング*  ・  難易度: 初級

青Q保護0257ではIBM IIDR 11.4 の ミラーリングを扱う採取票青Q保護0257です。青Q保護0257は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録青Q保護0257です。青Q保護0257ではイベントログと取得時刻を採取票青Q保護0257へ残します。青Q保護0257では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断青Q保護0257です。青Q保護0257の用語整理では複製ミラーリングの対象値を実在出力で区別する記録青Q保護0257です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0256を同一分類のCDCミラーリング Table Status 0340と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するして初期ロード状を照合する。
    - B. 管理対象との関係を表す説明は送信回数だけでターゲット適用完了を避けるため・通信統計からSendsを読むして通信統計を照合する。
    - C. 管理対象との関係を表す説明は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するして遅延確認を照合する。
    - D. 管理対象との関係を表す説明は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてイベントログを照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能イベン・対象サでDの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・保護）です。照合イベン・対象サに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・対象サです。比較ミラー・保護でA:のTable Statusは「ミラーリングの項目の初期ロード状態と取得時刻」を述べるため、正答側の照合軸はミラー・対象サ・保護です。運用保護・ミラーでB:のログとの照合 STAT07は「CDC Communicationsで通信統」を述べるため、正答側の照合軸はイベン・ミラー・保護です。項目ミラー・対象サでC:のCDCミラーリングは「ミラーリングの項目の遅延確認と取得時刻を記録」を述べるため、正答側の照合軸は対象サ・ミラー・イベンです。用語イベン・保護という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・保護です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0256**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0256について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE016
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0256A
    ```

    画面・出力には IIDR114DD0256A が表示され、CDCミラーリング Subscription 0256 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE016
    Mirroring request accepted
    確認コード IIDR114DD0256B
    ```

    画面・出力には IIDR114DD0256B が表示され、CDCミラーリング Subscription 0256 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0256C
    ```

    画面・出力には IIDR114DD0256C が表示され、CDCミラーリング Subscription 0256 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0256A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0256B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0256C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0271 {#c11-i0441}
*分類: ミラーリング*  ・  難易度: 中級

白L照合0272ではIBM IIDR 11.4 の ミラーリングを扱う採取票白L照合0272です。白L照合0272は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録白L照合0272です。白L照合0272ではイベントログと取得時刻を採取票白L照合0272へ残します。白L照合0272ではイベント重大度の誤読を避けるため補助資料も照合する判断白L照合0272です。白L照合0272の用語整理では複製ミラーリングの対象値を実在出力で評価する記録白L照合0272です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0271の設定や表示を読む前に役割を確認します。DDL後の表定義更新 Head of Log 0296ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするしてサブスクリプを照合する。
    - B. 対象資源に対する働きは外部連携の誤読を避けるため・状態確認で外部連携を確認するして外部連携を照合する。
    - C. 対象資源に対する働きは初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するしてミラー開始を照合する。
    - D. 対象資源に対する働きはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてイベントログを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能イベン・イベンでDの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・照合）です。照合イベン・イベンに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・イベンです。比較ミラー・照合でA:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はミラー・イベン・照合です。運用照合・ミラーでB:の状態確認 外部連携は「対象表を初期同期または再同期する複製操作」を述べるため、正答側の照合軸はイベン・ミラー・照合です。項目ミラー・イベンでC:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸はイベン・ミラー・イベンです。用語イベン・照合という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・照合です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0271**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0271について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE031
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0271A
    ```

    画面・出力には IIDR114DD0271A が表示され、CDCミラーリング Subscription 0271 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE031
    Mirroring request accepted
    確認コード IIDR114DD0271B
    ```

    画面・出力には IIDR114DD0271B が表示され、CDCミラーリング Subscription 0271 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0271C
    ```

    画面・出力には IIDR114DD0271C が表示され、CDCミラーリング Subscription 0271 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0271A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0271B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0271C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0286 {#c11-i0442}
*分類: ミラーリング*  ・  難易度: 中級

紫G抑止0287ではIBM IIDR 11.4 の ミラーリングを扱う採取票紫G抑止0287です。紫G抑止0287は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紫G抑止0287です。紫G抑止0287ではイベントログと取得時刻を採取票紫G抑止0287へ残します。紫G抑止0287では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紫G抑止0287です。紫G抑止0287の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紫G抑止0287です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0286に関する障害切り分けの前提を確認しています。DDL後の表定義更新 Source Table 0290の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は表定義未更新を避けるため・点検操作で判定欄を記録するして表定義再読込を照合する。
    - B. 表示や設定で扱う内容は実行結果の誤読を避けるため・性能統計で実行結果を確認するして実行結果を照合する。bookmark 失敗時切り分け 実行結果固有の属性も確認対象に含める。
    - C. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてイベントログを照合する。 ✅
    - D. 表示や設定で扱う内容は初期ロード中の再開を避けるため・表示操作で対象欄を追跡するしてサブスクリプを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能イベン・遅延ゼでCの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・抑止）です。照合イベン・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・遅延ゼです。比較ミラー・抑止でA:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・遅延ゼ・抑止です。運用抑止・ミラーでB:の失敗時切り分け 実行結果は「ログ上の適用位置と時刻を追跡する複製の進行点」を述べるため、正答側の照合軸はイベン・ミラー・抑止です。仕様ミラー・イベンでD:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は抑止・遅延ゼ・イベンです。用語イベン・抑止という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・抑止です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0286**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0286について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE046
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0286A
    ```

    画面・出力には IIDR114DD0286A が表示され、CDCミラーリング Subscription 0286 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE046
    Mirroring request accepted
    確認コード IIDR114DD0286B
    ```

    画面・出力には IIDR114DD0286B が表示され、CDCミラーリング Subscription 0286 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0286C
    ```

    画面・出力には IIDR114DD0286C が表示され、CDCミラーリング Subscription 0286 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0286A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0286B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0286C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0301 {#c11-i0443}
*分類: ミラーリング*  ・  難易度: 中級

橙B解析0302ではIBM IIDR 11.4 の ミラーリングを扱う採取票橙B解析0302です。橙B解析0302は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録橙B解析0302です。橙B解析0302ではイベントログと取得時刻を採取票橙B解析0302へ残します。橙B解析0302ではRefresh未完了の見落としを避けるため補助資料も照合する判断橙B解析0302です。橙B解析0302の用語整理では複製ミラーリングの対象値を実在出力で比較する記録橙B解析0302です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0301を保守記録に説明する必要があります。DDL後の表定義更新 Head of Log 0356と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は後の表定義更新の項目のサブスクリプション記述と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。
    - B. 保守作業で参照する機能はミラーリングの項目のイベントログと取得時刻を記録し・初期ロード未完了の見落としを防ぐである。記録操作で証跡欄を照合するときは初期ロード未完了の見落としを防ぐ。 ✅
    - C. 保守作業で参照する機能はサブスクリプションやデータストアの処理量と遅延を測る情報を初期同期判定として確認する。初期同期判定で出力見出しを確認するときは出力見出しの誤読を防ぐ。
    - D. 保守作業で参照する機能はSubscriptionの16進ブックマークと取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能イベン・初期ロでBの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・解析）です。照合イベン・初期ロに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・初期ロです。比較ミラー・解析でA:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はミラー・初期ロ・解析です。項目ミラー・初期ロでC:の初期同期判定 出力見出しは「サブスクリプションやデータストアの処理量と遅」を述べるため、正答側の照合軸は初期ロ・ミラー・イベンです。仕様ミラー・イベンでD:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸は解析・初期ロ・イベンです。用語イベン・解析という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・解析です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0301**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0301について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE061
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0301A
    ```

    画面・出力には IIDR114DD0301A が表示され、CDCミラーリング Subscription 0301 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE061
    Mirroring request accepted
    確認コード IIDR114DD0301B
    ```

    画面・出力には IIDR114DD0301B が表示され、CDCミラーリング Subscription 0301 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0301C
    ```

    画面・出力には IIDR114DD0301C が表示され、CDCミラーリング Subscription 0301 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0301A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0301B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0301C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0316 {#c11-i0444}
*分類: ミラーリング*  ・  難易度: 中級

青Q解析0317ではIBM IIDR 11.4 の ミラーリングを扱う採取票青Q解析0317です。青Q解析0317は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録青Q解析0317です。青Q解析0317ではイベントログと取得時刻を採取票青Q解析0317へ残します。青Q解析0317では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断青Q解析0317です。青Q解析0317の用語整理では複製ミラーリングの対象値を実在出力で区別する記録青Q解析0317です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0316の技術的な意味を資料で確認するとき、マッピング管理 Table Mapping 依存関係の確認 MAP13との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はデータ定義変更後に古い列定義で複を避けるため・購読記述からSourceTableを読むして購読記述を照合する。
    - B. 管理対象との関係を表す説明はデータソースの誤読を避けるため・ログ位置照合でデータソースを確認するしてデータソースを照合する。
    - C. 管理対象との関係を表す説明はログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするしてログ先頭到達を照合する。
    - D. 管理対象との関係を表す説明は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてイベントログを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能イベン・対象サでDの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・解析）です。照合イベン・対象サに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はミラー・イベン・対象サです。比較ミラー・解析でA:の依存関係の確認 MAP13は「Table Mappingで購読記述からSo」を述べるため、正答側の照合軸はミラー・対象サ・解析です。運用解析・ミラーでB:のログ位置照合 データソースは「ターゲットへ変更を反映し適用済み位置を記録す」を述べるため、正答側の照合軸はイベン・ミラー・解析です。項目ミラー・対象サでC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は対象サ・ミラー・イベンです。用語イベン・解析という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・解析です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0316**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0316について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE076
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0316A
    ```

    画面・出力には IIDR114DD0316A が表示され、CDCミラーリング Subscription 0316 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE076
    Mirroring request accepted
    確認コード IIDR114DD0316B
    ```

    画面・出力には IIDR114DD0316B が表示され、CDCミラーリング Subscription 0316 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0316C
    ```

    画面・出力には IIDR114DD0316C が表示され、CDCミラーリング Subscription 0316 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0316A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0316B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0316C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0331 {#c11-i0445}
*分類: ミラーリング*  ・  難易度: 中級

白L計画0332ではIBM IIDR 11.4 の ミラーリングを扱う採取票白L計画0332です。白L計画0332は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録白L計画0332です。白L計画0332ではイベントログと取得時刻を採取票白L計画0332へ残します。白L計画0332ではイベント重大度の誤読を避けるため補助資料も照合する判断白L計画0332です。白L計画0332の用語整理では複製ミラーリングの対象値を実在出力で評価する記録白L計画0332です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0331について構成や状態を確認します。データストア接続 CDC Datastore 復旧後の確認 STORE06ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはミラーリングの項目のイベントログと取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。 ✅
    - B. 対象資源に対する働きはCDC Datastoreでイベント確認からcommunicationを読みである。イベント確認からcommunicatときはホスト名変更後の購読構成を更を防ぐ。
    - C. 対象資源に対する働きはサブスクリプションやデータストアの処理量と遅延を測る情報である。複製状態監視で画面タグを確認するときは画面タグの誤読を防ぐ。
    - D. 対象資源に対する働きはLocaleのサブスクリプション名と取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能イベン・イベンでAの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・計画）です。照合イベン・イベンに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はイベン・計画・イベンです。運用計画・ミラーでB:の復旧後の確認 STORE06は「CDC Datastoreでイベント確認から」を述べるため、正答側の照合軸はイベン・ミラー・計画です。項目ミラー・イベンでC:の開始位置指定 画面タグは「サブスクリプションやデータストアの処理量と遅」を述べるため、正答側の照合軸はイベン・ミラー・イベンです。仕様ミラー・イベンでD:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は計画・イベン・イベンです。用語イベン・計画という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・イベンです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0331**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0331について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE091
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0331A
    ```

    画面・出力には IIDR114DD0331A が表示され、CDCミラーリング Subscription 0331 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE091
    Mirroring request accepted
    確認コード IIDR114DD0331B
    ```

    画面・出力には IIDR114DD0331B が表示され、CDCミラーリング Subscription 0331 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0331C
    ```

    画面・出力には IIDR114DD0331C が表示され、CDCミラーリング Subscription 0331 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0331A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0331B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0331C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Subscription 0346 {#c11-i0446}
*分類: ミラーリング*  ・  難易度: 上級

紫G解除0347ではIBM IIDR 11.4 の ミラーリングを扱う採取票紫G解除0347です。紫G解除0347は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紫G解除0347です。紫G解除0347ではイベントログと取得時刻を採取票紫G解除0347へ残します。紫G解除0347では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紫G解除0347です。紫G解除0347の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紫G解除0347です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Subscription 0346の役割を調べています。DDL後の表定義更新 Head of Log 0356の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするしてサブスクリプを照合する。
    - B. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてイベントログを照合する。 ✅
    - C. 表示や設定で扱う内容はベンダー指示なしの位置変更を避けるため・主操作で出力欄を評価するしてサブスクリプを照合する。
    - D. 表示や設定で扱う内容は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてサブスクリプを照合する。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能イベン・遅延ゼでBの記述「ミラーリングの項目のイベントログと取得時刻を記録し」に対応する項目はCDCミラーリング Subscrip（ミラー・イベン・解除）です。照合イベン・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目のイベントログと取得時刻を記録し」で、確認対象はイベン・解除・遅延ゼです。比較ミラー・解除でA:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はミラー・解除・イベンです。項目ミラー・遅延ゼでC:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は遅延ゼ・ミラー・イベンです。仕様ミラー・イベンでD:のReplicationは「ミラーリングの項目のサブスクリプション状態と」を述べるため、正答側の照合軸は解除・遅延ゼ・イベンです。用語イベン・解除という用語は「ミラーリングの項目のイベントログと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・遅延ゼです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Subscription 0346**

    - 検証目的: CDCミラーリングのCDCミラーリング Subscription 0346について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Subscription と イベントログ
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE106
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0346A
    ```

    画面・出力には IIDR114DD0346A が表示され、CDCミラーリング Subscription 0346 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE106
    Mirroring request accepted
    確認コード IIDR114DD0346B
    ```

    画面・出力には IIDR114DD0346B が表示され、CDCミラーリング Subscription 0346 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Subscription を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0346C
    ```

    画面・出力には IIDR114DD0346C が表示され、CDCミラーリング Subscription 0346 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0346A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0346B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0346C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0010 {#c11-i0447}
*分類: ミラーリング*  ・  難易度: 初級

紺K巡回0011ではIBM IIDR 11.4 の ミラーリングを扱う採取票紺K巡回0011です。紺K巡回0011は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紺K巡回0011です。紺K巡回0011ではRefresh状態と取得時刻を採取票紺K巡回0011へ残します。紺K巡回0011では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紺K巡回0011です。紺K巡回0011の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紺K巡回0011です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0010の役割を調べています。複製位置管理 Hex Position 0066の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は監査でインスタンスを証跡に残し・Hex Positionのインスタンス名と取得時刻を記録し。
    - B. 表示や設定で扱う内容は登録でイベントログを証跡に残し・CDCのイベントログと取得時刻を記録し。
    - C. 表示や設定で扱う内容は復旧準備で遅延表示を証跡に残し・CDC Communicationsで遅延表示からBytes。
    - D. 表示や設定で扱う内容は巡回でRefresを証跡に残し・CDCのRefresh状態と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 巡回・Ref・遅延ゼロでDの記述「CDCのRefresh状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・Ref・遅延ゼロ・巡回）です。巡回時のRefreに関するミラーリングの仕様は「CDCのRefresh状態と取得時刻を記録し」で、確認対象はミラー・Ref・遅延ゼロ・巡回です。He・監査・インスタのA:は「Hex Positionのインスタンス名と取得時刻を記録し」を述べ、対象はHex Position（Hex・インス・重複反映・監査）です。登録・イベン・イベントのB:は「CDCのイベントログと取得時刻を記録し、イベント重大度の誤読を防ぐ」を述べ、対象はCDCミラーリング Subscrip（ミラー・イベン・イベント・登録）です。復旧準備時の遅延表示のC:は「CDC Communicationsで遅延表示からBytespers」を述べ、対象は復旧準備 STAT05（CDC・遅延表・送信回数・復旧準）です。Refreを巡回という用語は「CDCのRefresh状態と取得時刻を記録し」を指し、Table Status（ミラー・Ref・遅延ゼロ・巡回）で照合する値はRefresです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0010**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0010について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE010
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0010A
    ```

    画面・出力には IIDR114DD0010A が表示され、CDCミラーリング Table Status 0010 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE010
    Mirroring request accepted
    確認コード IIDR114DD0010B
    ```

    画面・出力には IIDR114DD0010B が表示され、CDCミラーリング Table Status 0010 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0010C
    ```

    画面・出力には IIDR114DD0010C が表示され、CDCミラーリング Table Status 0010 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0010A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0010B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0010C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0025 {#c11-i0448}
*分類: ミラーリング*  ・  難易度: 中級

銀F棚卸0026ではIBM IIDR 11.4 の ミラーリングを扱う採取票銀F棚卸0026です。銀F棚卸0026は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録銀F棚卸0026です。銀F棚卸0026ではRefresh状態と取得時刻を採取票銀F棚卸0026へ残します。銀F棚卸0026ではRefresh未完了の見落としを避けるため補助資料も照合する判断銀F棚卸0026です。銀F棚卸0026の用語整理では複製ミラーリングの対象値を実在出力で比較する記録銀F棚卸0026です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Table Status 0025」を「DDL後の表定義更新 Source Table 0080」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は調査操作で保守欄を引き継ぎすることで表定義再読込を確認し・ログ先頭未到達の見落としを防ぐ。
    - B. 保守作業で参照する機能は保守操作で監査欄を保存することでイベントログを確認し・対象サブスクリプションの取りを防ぐ。
    - C. 保守作業で参照する機能は記録操作で証跡欄を照合することで初期ロード状を確認し・初期ロード未完了の見落としを防ぐ。 ✅
    - D. 保守作業で参照する機能は方式表示から初期ロードingを読むことで方式表示を確認し・初期ロード未完了でMirroを防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能初期ロ・初期ロでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・棚卸）です。照合初期ロ・初期ロに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・初期ロです。比較ミラー・棚卸でA:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・初期ロ・棚卸です。運用棚卸・ミラーでB:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸は初期ロ・ミラー・棚卸です。仕様ミラー・初期ロでD:の代替経路の確認 REF10は「CDC Refreshで方式表示から初期ロー」を述べるため、正答側の照合軸は棚卸・初期ロ・初期ロです。用語初期ロ・棚卸という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・棚卸です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0025**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0025について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE025
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0025A
    ```

    画面・出力には IIDR114DD0025A が表示され、CDCミラーリング Table Status 0025 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE025
    Mirroring request accepted
    確認コード IIDR114DD0025B
    ```

    画面・出力には IIDR114DD0025B が表示され、CDCミラーリング Table Status 0025 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0025C
    ```

    画面・出力には IIDR114DD0025C が表示され、CDCミラーリング Table Status 0025 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0025A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0025B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0025C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0040 {#c11-i0449}
*分類: ミラーリング*  ・  難易度: 中級

蒼A復旧0041ではIBM IIDR 11.4 の ミラーリングを扱う採取票蒼A復旧0041です。蒼A復旧0041は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録蒼A復旧0041です。蒼A復旧0041ではRefresh状態と取得時刻を採取票蒼A復旧0041へ残します。蒼A復旧0041では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断蒼A復旧0041です。蒼A復旧0041の用語整理では複製ミラーリングの対象値を実在出力で区別する記録蒼A復旧0041です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0040を同一分類のCDCミラーリング Latency 0082と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するして遅延確認を照合する。
    - B. 管理対象との関係を表す説明は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するして初期ロード状を照合する。 ✅
    - C. 管理対象との関係を表す説明は表定義未更新を避けるため・点検操作で判定欄を記録するしてログ先頭到達を照合する。
    - D. 管理対象との関係を表す説明は休止購読を見落として必要ログを削を避けるため・購読確認からInactiveを読むして購読確認を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能初期ロ・対象サでBの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・復旧）です。照合初期ロ・対象サに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・対象サです。比較ミラー・復旧でA:のCDCミラーリングは「ミラーリングの項目の遅延確認と取得時刻を記録」を述べるため、正答側の照合軸はミラー・対象サ・復旧です。項目ミラー・対象サでC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は対象サ・ミラー・初期ロです。仕様ミラー・初期ロでD:の復旧準備 LOG05は「Log Dependencyで購読確認からI」を述べるため、正答側の照合軸は復旧・対象サ・初期ロです。用語初期ロ・復旧という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・復旧です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0040**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0040について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE040
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0040A
    ```

    画面・出力には IIDR114DD0040A が表示され、CDCミラーリング Table Status 0040 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE040
    Mirroring request accepted
    確認コード IIDR114DD0040B
    ```

    画面・出力には IIDR114DD0040B が表示され、CDCミラーリング Table Status 0040 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0040C
    ```

    画面・出力には IIDR114DD0040C が表示され、CDCミラーリング Table Status 0040 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0040A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0040B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0040C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0055 {#c11-i0450}
*分類: ミラーリング*  ・  難易度: 中級

金P復旧0056ではIBM IIDR 11.4 の ミラーリングを扱う採取票金P復旧0056です。金P復旧0056は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録金P復旧0056です。金P復旧0056ではRefresh状態と取得時刻を採取票金P復旧0056へ残します。金P復旧0056ではイベント重大度の誤読を避けるため補助資料も照合する判断金P復旧0056です。金P復旧0056の用語整理では複製ミラーリングの対象値を実在出力で評価する記録金P復旧0056です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0055の設定や表示を読む前に役割を確認します。複製位置管理 Locale 0087ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはミラーリングの項目の初期ロード状態と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。 ✅
    - B. 対象資源に対する働きはLocaleのサブスクリプション名と取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。
    - C. 対象資源に対する働きは後の表定義更新の項目のログ先頭到達と取得時刻を記録し・データ定義対象表の漏れを防ぐである。復旧操作で点検欄を確認するときはデータ定義対象表の漏れを防ぐ。
    - D. 対象資源に対する働きはCDC Replication が接続するソースまたはターゲットの接続定義である。データストアで停止時刻を確認するときは停止時刻の誤読を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能初期ロ・イベンでAの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・復旧）です。照合初期ロ・イベンに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・イベンです。運用復旧・ミラーでB:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は初期ロ・ミラー・復旧です。項目ミラー・イベンでC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸はイベン・ミラー・初期ロです。仕様ミラー・初期ロでD:の開始位置指定 停止時刻は「CDC Replication」を述べるため、正答側の照合軸は復旧・イベン・初期ロです。用語初期ロ・復旧という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・復旧です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0055**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0055について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE055
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0055A
    ```

    画面・出力には IIDR114DD0055A が表示され、CDCミラーリング Table Status 0055 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE055
    Mirroring request accepted
    確認コード IIDR114DD0055B
    ```

    画面・出力には IIDR114DD0055B が表示され、CDCミラーリング Table Status 0055 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0055C
    ```

    画面・出力には IIDR114DD0055C が表示され、CDCミラーリング Table Status 0055 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0055A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0055B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0055C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0070 {#c11-i0451}
*分類: ミラーリング*  ・  難易度: 中級

紺K監査0071ではIBM IIDR 11.4 の ミラーリングを扱う採取票紺K監査0071です。紺K監査0071は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紺K監査0071です。紺K監査0071ではRefresh状態と取得時刻を採取票紺K監査0071へ残します。紺K監査0071では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紺K監査0071です。紺K監査0071の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紺K監査0071です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0070に関する障害切り分けの前提を確認しています。複製位置管理 Instance 0123の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はデータ欠落を避けるため・監査操作で記録欄を比較するして戻り値を照合する。
    - B. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するして初期ロード状を照合する。 ✅
    - C. 表示や設定で扱う内容は重複反映を避けるため・変更確認操作で採取欄を棚卸するしてサブスクリプを照合する。
    - D. 表示や設定で扱う内容は休止購読を見落として必要ログを削を避けるため・支援情報からReturnvalueを読むして支援情報を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能初期ロ・遅延ゼでBの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・監査）です。照合初期ロ・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・遅延ゼです。比較ミラー・監査でA:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・遅延ゼ・監査です。項目ミラー・遅延ゼでC:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は遅延ゼ・ミラー・初期ロです。仕様ミラー・初期ロでD:の再始動後の確認 LOG15は「Log Dependencyで支援情報からR」を述べるため、正答側の照合軸は監査・遅延ゼ・初期ロです。用語初期ロ・監査という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・監査です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0070**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0070について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE070
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0070A
    ```

    画面・出力には IIDR114DD0070A が表示され、CDCミラーリング Table Status 0070 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE070
    Mirroring request accepted
    確認コード IIDR114DD0070B
    ```

    画面・出力には IIDR114DD0070B が表示され、CDCミラーリング Table Status 0070 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0070C
    ```

    画面・出力には IIDR114DD0070C が表示され、CDCミラーリング Table Status 0070 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0070A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0070B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0070C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0085 {#c11-i0452}
*分類: ミラーリング*  ・  難易度: 中級

銀F変更0086ではIBM IIDR 11.4 の ミラーリングを扱う採取票銀F変更0086です。銀F変更0086は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録銀F変更0086です。銀F変更0086ではRefresh状態と取得時刻を採取票銀F変更0086へ残します。銀F変更0086ではRefresh未完了の見落としを避けるため補助資料も照合する判断銀F変更0086です。銀F変更0086の用語整理では複製ミラーリングの対象値を実在出力で比較する記録銀F変更0086です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0085を保守記録に説明する必要があります。DDL後の表定義更新 Head of Log 0116と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は調査操作で保守欄を引き継ぎすることでサブスクリプを確認し・ログ先頭未到達の見落としを防ぐ。
    - B. 保守作業で参照する機能は復旧操作で点検欄を確認することで再開条件を確認し・データ定義対象表の漏れを防ぐ。
    - C. 保守作業で参照する機能は記録操作で証跡欄を照合することで初期ロード状を確認し・初期ロード未完了の見落としを防ぐ。 ✅
    - D. 保守作業で参照する機能は複製状態監視で例外記録を確認することで例外記録を確認し・例外記録の誤読を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能初期ロ・初期ロでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・変更）です。照合初期ロ・初期ロに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・初期ロです。比較ミラー・変更でA:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はミラー・初期ロ・変更です。運用変更・ミラーでB:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は初期ロ・ミラー・変更です。仕様ミラー・初期ロでD:の失敗時切り分け 例外記録は「ターゲットへ変更を反映し適用済み位置を記録す」を述べるため、正答側の照合軸は変更・初期ロ・初期ロです。用語初期ロ・変更という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・変更です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0085**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0085について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE085
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0085A
    ```

    画面・出力には IIDR114DD0085A が表示され、CDCミラーリング Table Status 0085 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE085
    Mirroring request accepted
    確認コード IIDR114DD0085B
    ```

    画面・出力には IIDR114DD0085B が表示され、CDCミラーリング Table Status 0085 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0085C
    ```

    画面・出力には IIDR114DD0085C が表示され、CDCミラーリング Table Status 0085 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0085A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0085B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0085C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0100 {#c11-i0453}
*分類: ミラーリング*  ・  難易度: 上級

蒼A移行0101ではIBM IIDR 11.4 の ミラーリングを扱う採取票蒼A移行0101です。蒼A移行0101は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録蒼A移行0101です。蒼A移行0101ではRefresh状態と取得時刻を採取票蒼A移行0101へ残します。蒼A移行0101では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断蒼A移行0101です。蒼A移行0101の用語整理では複製ミラーリングの対象値を実在出力で区別する記録蒼A移行0101です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0100の技術的な意味を資料で確認するとき、複製位置管理 Locale 0102との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は移行でサブスクリプを証跡に残し・Localeのサブスクリプション名と取得時刻を記録し。
    - B. 管理対象との関係を表す説明は解除で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し。
    - C. 管理対象との関係を表す説明は再始動確認で支援情報を証跡に残し・Log Dependencyで支援情報からReturnval。
    - D. 管理対象との関係を表す説明は移行で初期ロード状を証跡に残し・ミラーリングの項目の初期ロード状態と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能初期ロ・対象サでDの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・移行）です。照合初期ロ・対象サに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・対象サです。比較ミラー・移行でA:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸はミラー・対象サ・移行です。運用移行・ミラーでB:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は初期ロ・ミラー・移行です。項目ミラー・対象サでC:の再始動後の確認 LOG15は「Log Dependencyで支援情報からR」を述べるため、正答側の照合軸は対象サ・ミラー・初期ロです。用語初期ロ・移行という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・移行です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0100**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0100について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE100
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0100A
    ```

    画面・出力には IIDR114DD0100A が表示され、CDCミラーリング Table Status 0100 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE100
    Mirroring request accepted
    確認コード IIDR114DD0100B
    ```

    画面・出力には IIDR114DD0100B が表示され、CDCミラーリング Table Status 0100 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0100C
    ```

    画面・出力には IIDR114DD0100C が表示され、CDCミラーリング Table Status 0100 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0100A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0100B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0100C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0115 {#c11-i0454}
*分類: ミラーリング*  ・  難易度: 上級

金P移行0116ではIBM IIDR 11.4 の ミラーリングを扱う採取票金P移行0116です。金P移行0116は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録金P移行0116です。金P移行0116ではRefresh状態と取得時刻を採取票金P移行0116へ残します。金P移行0116ではイベント重大度の誤読を避けるため補助資料も照合する判断金P移行0116です。金P移行0116の用語整理では複製ミラーリングの対象値を実在出力で評価する記録金P移行0116です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0115について構成や状態を確認します。CDCミラーリング Event Severity 0139ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは診断でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。
    - B. 対象資源に対する働きは解析でインスタンスを証跡に残し・Hex Positionのインスタンス名と取得時刻を記録し。
    - C. 対象資源に対する働きは移行で初期ロード状を証跡に残し・ミラーリングの項目の初期ロード状態と取得時刻を記録し。 ✅
    - D. 対象資源に対する働きは初期同期判定で送信操作を証跡に残し・ログ上の適用位置と時刻を追跡する複製の進行点を初期同期判定と。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能初期ロ・イベンでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・移行）です。照合初期ロ・イベンに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・イベンです。比較ミラー・移行でA:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸はミラー・イベン・移行です。運用移行・ミラーでB:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は初期ロ・ミラー・移行です。仕様ミラー・初期ロでD:の初期同期判定 送信操作は「ログ上の適用位置と時刻を追跡する複製の進行点」を述べるため、正答側の照合軸は移行・イベン・初期ロです。用語初期ロ・移行という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・移行です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0115**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0115について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE115
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0115A
    ```

    画面・出力には IIDR114DD0115A が表示され、CDCミラーリング Table Status 0115 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE115
    Mirroring request accepted
    確認コード IIDR114DD0115B
    ```

    画面・出力には IIDR114DD0115B が表示され、CDCミラーリング Table Status 0115 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0115C
    ```

    画面・出力には IIDR114DD0115C が表示され、CDCミラーリング Table Status 0115 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0115A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0115B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0115C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0130 {#c11-i0455}
*分類: ミラーリング*  ・  難易度: 初級

紺K診断0131ではIBM IIDR 11.4 の ミラーリングを扱う採取票紺K診断0131です。紺K診断0131は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紺K診断0131です。紺K診断0131ではRefresh状態と取得時刻を採取票紺K診断0131へ残します。紺K診断0131では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紺K診断0131です。紺K診断0131の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紺K診断0131です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0130の役割を調べています。複製位置管理 Instance 0213の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はベンダー指示なしの位置変更を避けるため・主操作で出力欄を評価するして戻り値を照合する。
    - B. 表示や設定で扱う内容は別サブスクリプションを停止またはを避けるため・版数表示からReplicationを読むして版数表示を照合する。
    - C. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するして初期ロード状を照合する。 ✅
    - D. 表示や設定で扱う内容は一覧画面の誤読を避けるため・データストアで一覧画面を確認するして一覧画面を照合する。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能初期ロ・遅延ゼでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・診断）です。照合初期ロ・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・遅延ゼです。比較ミラー・診断でA:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・遅延ゼ・診断です。運用診断・ミラーでB:の権限境界の確認 SUB12は「CDC Subscriptionで版数表示か」を述べるため、正答側の照合軸は初期ロ・ミラー・診断です。仕様ミラー・初期ロでD:の失敗時切り分け 一覧画面は「サブスクリプションやデータストアの処理量と遅」を述べるため、正答側の照合軸は診断・遅延ゼ・初期ロです。用語初期ロ・診断という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・診断です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0130**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0130について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE010
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0130A
    ```

    画面・出力には IIDR114DD0130A が表示され、CDCミラーリング Table Status 0130 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE010
    Mirroring request accepted
    確認コード IIDR114DD0130B
    ```

    画面・出力には IIDR114DD0130B が表示され、CDCミラーリング Table Status 0130 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0130C
    ```

    画面・出力には IIDR114DD0130C が表示され、CDCミラーリング Table Status 0130 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0130A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0130B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0130C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0145 {#c11-i0456}
*分類: ミラーリング*  ・  難易度: 中級

銀F保守0146ではIBM IIDR 11.4 の ミラーリングを扱う採取票銀F保守0146です。銀F保守0146は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録銀F保守0146です。銀F保守0146ではRefresh状態と取得時刻を採取票銀F保守0146へ残します。銀F保守0146ではRefresh未完了の見落としを避けるため補助資料も照合する判断銀F保守0146です。銀F保守0146の用語整理では複製ミラーリングの対象値を実在出力で比較する記録銀F保守0146です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Table Status 0145」を「DDL後の表定義更新 Refresh Table 0218」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は表定義未更新を避けるため・点検操作で判定欄を記録するして再開条件を照合する。
    - B. 保守作業で参照する機能はデータ定義対象表の漏れを避けるため・復旧操作で点検欄を確認するしてサブスクリプを照合する。
    - C. 保守作業で参照する機能は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するして初期ロード状を照合する。 ✅
    - D. 保守作業で参照する機能はイベント重大度の誤読を避けるため・採取操作で照合欄を点検するしてイベントログを照合する。CDCミラーリング Subscription 0031固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能初期ロ・初期ロでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・保守）です。照合初期ロ・初期ロに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・初期ロです。比較ミラー・保守でA:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸はミラー・初期ロ・保守です。運用保守・ミラーでB:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は初期ロ・ミラー・保守です。仕様ミラー・初期ロでD:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸は保守・初期ロ・初期ロです。用語初期ロ・保守という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・保守です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0145**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0145について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE025
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0145A
    ```

    画面・出力には IIDR114DD0145A が表示され、CDCミラーリング Table Status 0145 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE025
    Mirroring request accepted
    確認コード IIDR114DD0145B
    ```

    画面・出力には IIDR114DD0145B が表示され、CDCミラーリング Table Status 0145 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0145C
    ```

    画面・出力には IIDR114DD0145C が表示され、CDCミラーリング Table Status 0145 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0145A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0145B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0145C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0160 {#c11-i0457}
*分類: ミラーリング*  ・  難易度: 中級

蒼A切替0161ではIBM IIDR 11.4 の ミラーリングを扱う採取票蒼A切替0161です。蒼A切替0161は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録蒼A切替0161です。蒼A切替0161ではRefresh状態と取得時刻を採取票蒼A切替0161へ残します。蒼A切替0161では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断蒼A切替0161です。蒼A切替0161の用語整理では複製ミラーリングの対象値を実在出力で区別する記録蒼A切替0161です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0160を同一分類の複製位置管理 Locale 0162と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は切替でサブスクリプを証跡に残し・Localeのサブスクリプション名と取得時刻を記録し。
    - B. 管理対象との関係を表す説明は切替で初期ロード状を証跡に残し・ミラーリングの項目の初期ロード状態と取得時刻を記録し。 ✅
    - C. 管理対象との関係を表す説明は解除で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し。
    - D. 管理対象との関係を表す説明は性能統計でセッション上を証跡に残し・bookmark まで適用したことを示す CDC。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能初期ロ・対象サでBの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・切替）です。照合初期ロ・対象サに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・対象サです。比較ミラー・切替でA:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸はミラー・対象サ・切替です。項目ミラー・対象サでC:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は対象サ・ミラー・初期ロです。仕様ミラー・初期ロでD:のマッピング検査 セッション上限は「bookmark まで適用したことを示す」を述べるため、正答側の照合軸は切替・対象サ・初期ロです。用語初期ロ・切替という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・切替です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0160**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0160について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE040
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0160A
    ```

    画面・出力には IIDR114DD0160A が表示され、CDCミラーリング Table Status 0160 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE040
    Mirroring request accepted
    確認コード IIDR114DD0160B
    ```

    画面・出力には IIDR114DD0160B が表示され、CDCミラーリング Table Status 0160 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0160C
    ```

    画面・出力には IIDR114DD0160C が表示され、CDCミラーリング Table Status 0160 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0160A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0160B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0160C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0175 {#c11-i0458}
*分類: ミラーリング*  ・  難易度: 中級

金P切替0176ではIBM IIDR 11.4 の ミラーリングを扱う採取票金P切替0176です。金P切替0176は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録金P切替0176です。金P切替0176ではRefresh状態と取得時刻を採取票金P切替0176へ残します。金P切替0176ではイベント重大度の誤読を避けるため補助資料も照合する判断金P切替0176です。金P切替0176の用語整理では複製ミラーリングの対象値を実在出力で評価する記録金P切替0176です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0175の設定や表示を読む前に役割を確認します。DDL後の表定義更新 Head of Log 0236ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするしてサブスクリプを照合する。
    - B. 対象資源に対する働きは初期ロード中の表をMirror完を避けるため・イベント表示からheadoflogを読むしてイベント表示を照合する。
    - C. 対象資源に対する働きはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するして初期ロード状を照合する。 ✅
    - D. 対象資源に対する働きは対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてミラー開始を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能初期ロ・イベンでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・切替）です。照合初期ロ・イベンに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・イベンです。比較ミラー・切替でA:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はミラー・イベン・切替です。運用切替・ミラーでB:の構成監査 MIR08は「Mirror Statusでイベント表示から」を述べるため、正答側の照合軸は初期ロ・ミラー・切替です。仕様ミラー・初期ロでD:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸は切替・イベン・初期ロです。用語初期ロ・切替という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・切替です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0175**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0175について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE055
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0175A
    ```

    画面・出力には IIDR114DD0175A が表示され、CDCミラーリング Table Status 0175 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE055
    Mirroring request accepted
    確認コード IIDR114DD0175B
    ```

    画面・出力には IIDR114DD0175B が表示され、CDCミラーリング Table Status 0175 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0175C
    ```

    画面・出力には IIDR114DD0175C が表示され、CDCミラーリング Table Status 0175 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0175A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0175B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0175C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0190 {#c11-i0459}
*分類: ミラーリング*  ・  難易度: 中級

紺K収集0191ではIBM IIDR 11.4 の ミラーリングを扱う採取票紺K収集0191です。紺K収集0191は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紺K収集0191です。紺K収集0191ではRefresh状態と取得時刻を採取票紺K収集0191へ残します。紺K収集0191では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紺K収集0191です。紺K収集0191の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紺K収集0191です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0190に関する障害切り分けの前提を確認しています。DDL後の表定義更新 Source Table 0200の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は登録で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - B. 表示や設定で扱う内容は収集で初期ロード状を証跡に残し・ミラーリングの項目の初期ロード状態と取得時刻を記録し。 ✅
    - C. 表示や設定で扱う内容はログとの照合で状態表示を証跡に残し・Mirror Statusで状態表示からLatencyを読み。
    - D. 表示や設定で扱う内容は棚卸でインスタンスを証跡に残し・Hex Positionのインスタンス名と取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能初期ロ・遅延ゼでBの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・収集）です。照合初期ロ・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・遅延ゼです。比較ミラー・収集でA:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・遅延ゼ・収集です。項目ミラー・遅延ゼでC:のログとの照合 MIR07は「Mirror Statusで状態表示からLa」を述べるため、正答側の照合軸は遅延ゼ・ミラー・初期ロです。仕様ミラー・初期ロでD:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は収集・遅延ゼ・初期ロです。用語初期ロ・収集という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・収集です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0190**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0190について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE070
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0190A
    ```

    画面・出力には IIDR114DD0190A が表示され、CDCミラーリング Table Status 0190 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE070
    Mirroring request accepted
    確認コード IIDR114DD0190B
    ```

    画面・出力には IIDR114DD0190B が表示され、CDCミラーリング Table Status 0190 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0190C
    ```

    画面・出力には IIDR114DD0190C が表示され、CDCミラーリング Table Status 0190 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0190A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0190B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0190C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0205 {#c11-i0460}
*分類: ミラーリング*  ・  難易度: 中級

銀F登録0206ではIBM IIDR 11.4 の ミラーリングを扱う採取票銀F登録0206です。銀F登録0206は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録銀F登録0206です。銀F登録0206ではRefresh状態と取得時刻を採取票銀F登録0206へ残します。銀F登録0206ではRefresh未完了の見落としを避けるため補助資料も照合する判断銀F登録0206です。銀F登録0206の用語整理では複製ミラーリングの対象値を実在出力で比較する記録銀F登録0206です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0205を保守記録に説明する必要があります。CDCミラーリング Latency 0247と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は採取操作で照合欄を点検することで遅延確認を確認し・イベント重大度の誤読を防ぐ。
    - B. 保守作業で参照する機能は遅延表示からBytespersecondことで遅延表示を確認し・送信回数だけでターゲット適用を防ぐ。
    - C. 保守作業で参照する機能は監査操作で記録欄を比較することで複製位置を確認し・データ欠落を防ぐ。
    - D. 保守作業で参照する機能は記録操作で証跡欄を照合することで初期ロード状を確認し・初期ロード未完了の見落としを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能初期ロ・初期ロでDの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・登録）です。照合初期ロ・初期ロに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・初期ロです。比較ミラー・登録でA:のCDCミラーリングは「ミラーリングの項目の遅延確認と取得時刻を記録」を述べるため、正答側の照合軸はミラー・初期ロ・登録です。運用登録・ミラーでB:の停止前の確認 STAT14は「CDC Communicationsで遅延表」を述べるため、正答側の照合軸は初期ロ・ミラー・登録です。項目ミラー・初期ロでC:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸は初期ロ・ミラー・初期ロです。用語初期ロ・登録という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・登録です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0205**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0205について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE085
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0205A
    ```

    画面・出力には IIDR114DD0205A が表示され、CDCミラーリング Table Status 0205 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE085
    Mirroring request accepted
    確認コード IIDR114DD0205B
    ```

    画面・出力には IIDR114DD0205B が表示され、CDCミラーリング Table Status 0205 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0205C
    ```

    画面・出力には IIDR114DD0205C が表示され、CDCミラーリング Table Status 0205 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0205A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0205B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0205C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0220 {#c11-i0461}
*分類: ミラーリング*  ・  難易度: 上級

蒼A確認0221ではIBM IIDR 11.4 の ミラーリングを扱う採取票蒼A確認0221です。蒼A確認0221は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録蒼A確認0221です。蒼A確認0221ではRefresh状態と取得時刻を採取票蒼A確認0221へ残します。蒼A確認0221では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断蒼A確認0221です。蒼A確認0221の用語整理では複製ミラーリングの対象値を実在出力で区別する記録蒼A確認0221です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0220の技術的な意味を資料で確認するとき、CDCミラーリング Subscription 0271との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は採取操作で照合欄を点検することでイベントログを確認し・イベント重大度の誤読を防ぐ。
    - B. 管理対象との関係を表す説明は支援情報からReturnvalueを読むことで支援情報を確認し・休止購読を見落として必要ログを防ぐ。
    - C. 管理対象との関係を表す説明は保守操作で監査欄を保存することでサブスクリプを確認し・対象サブスクリプションの取りを防ぐ。
    - D. 管理対象との関係を表す説明は保守操作で監査欄を保存することで初期ロード状を確認し・対象サブスクリプションの取りを防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能初期ロ・対象サでDの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・確認）です。照合初期ロ・対象サに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・対象サです。比較ミラー・確認でA:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸はミラー・対象サ・確認です。運用確認・ミラーでB:の再始動後の確認 LOG15は「Log Dependencyで支援情報からR」を述べるため、正答側の照合軸は初期ロ・ミラー・確認です。項目ミラー・対象サでC:のReplicationは「ミラーリングの項目のサブスクリプション状態と」を述べるため、正答側の照合軸は対象サ・ミラー・初期ロです。用語初期ロ・確認という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・確認です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0220**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0220について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE100
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0220A
    ```

    画面・出力には IIDR114DD0220A が表示され、CDCミラーリング Table Status 0220 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE100
    Mirroring request accepted
    確認コード IIDR114DD0220B
    ```

    画面・出力には IIDR114DD0220B が表示され、CDCミラーリング Table Status 0220 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0220C
    ```

    画面・出力には IIDR114DD0220C が表示され、CDCミラーリング Table Status 0220 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0220A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0220B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0220C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0235 {#c11-i0462}
*分類: ミラーリング*  ・  難易度: 上級

金P確認0236ではIBM IIDR 11.4 の ミラーリングを扱う採取票金P確認0236です。金P確認0236は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録金P確認0236です。金P確認0236ではRefresh状態と取得時刻を採取票金P確認0236へ残します。金P確認0236ではイベント重大度の誤読を避けるため補助資料も照合する判断金P確認0236です。金P確認0236の用語整理では複製ミラーリングの対象値を実在出力で評価する記録金P確認0236です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0235について構成や状態を確認します。DDL後の表定義更新 Head of Log 0266ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは点検操作で判定欄を記録することでサブスクリプを確認し・表定義未更新を防ぐ。
    - B. 対象資源に対する働きは方式変更からReturnvalueを読むことで方式変更を確認し・初期ロード未完了でMirroを防ぐ。
    - C. 対象資源に対する働きは採取操作で照合欄を点検することで初期ロード状を確認し・イベント重大度の誤読を防ぐ。 ✅
    - D. 対象資源に対する働きは採取操作で照合欄を点検することでサブスクリプを確認し・イベント重大度の誤読を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能初期ロ・イベンでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・確認）です。照合初期ロ・イベンに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・イベンです。比較ミラー・確認でA:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はミラー・イベン・確認です。運用確認・ミラーでB:の構成監査 REF08は「CDC Refreshで方式変更からRetu」を述べるため、正答側の照合軸は初期ロ・ミラー・確認です。仕様ミラー・初期ロでD:のReplicationは「ミラーリングの項目のサブスクリプション状態と」を述べるため、正答側の照合軸は確認・イベン・初期ロです。用語初期ロ・確認という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・確認です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0235**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0235について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE115
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0235A
    ```

    画面・出力には IIDR114DD0235A が表示され、CDCミラーリング Table Status 0235 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE115
    Mirroring request accepted
    確認コード IIDR114DD0235B
    ```

    画面・出力には IIDR114DD0235B が表示され、CDCミラーリング Table Status 0235 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0235C
    ```

    画面・出力には IIDR114DD0235C が表示され、CDCミラーリング Table Status 0235 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0235A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0235B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0235C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0250 {#c11-i0463}
*分類: ミラーリング*  ・  難易度: 初級

紺K保護0251ではIBM IIDR 11.4 の ミラーリングを扱う採取票紺K保護0251です。紺K保護0251は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紺K保護0251です。紺K保護0251ではRefresh状態と取得時刻を採取票紺K保護0251へ残します。紺K保護0251では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紺K保護0251です。紺K保護0251の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紺K保護0251です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0250の役割を調べています。DDL後の表定義更新 Table Definition 0314の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は解析でデータ定義対を証跡に残し・後の表定義更新の項目のデータ定義対象表と取得時刻を記録し。
    - B. 表示や設定で扱う内容はマッピングで入力欄を証跡に残し・対象表を初期同期または再同期する複製操作を遅延監視として確認。
    - C. 表示や設定で扱う内容は移行でログ先頭到達を証跡に残し・後の表定義更新の項目のログ先頭到達と取得時刻を記録し。
    - D. 表示や設定で扱う内容は保護で初期ロード状を証跡に残し・ミラーリングの項目の初期ロード状態と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能初期ロ・遅延ゼでDの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・保護）です。照合初期ロ・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・遅延ゼです。比較ミラー・保護でA:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はミラー・遅延ゼ・保護です。運用保護・ミラーでB:の遅延監視 入力欄は「対象表を初期同期または再同期する複製操作を遅」を述べるため、正答側の照合軸は初期ロ・ミラー・保護です。項目ミラー・遅延ゼでC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は遅延ゼ・ミラー・初期ロです。用語初期ロ・保護という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・保護です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0250**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0250について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE010
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0250A
    ```

    画面・出力には IIDR114DD0250A が表示され、CDCミラーリング Table Status 0250 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE010
    Mirroring request accepted
    確認コード IIDR114DD0250B
    ```

    画面・出力には IIDR114DD0250B が表示され、CDCミラーリング Table Status 0250 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0250C
    ```

    画面・出力には IIDR114DD0250C が表示され、CDCミラーリング Table Status 0250 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0250A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0250B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0250C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0265 {#c11-i0464}
*分類: ミラーリング*  ・  難易度: 中級

銀F照合0266ではIBM IIDR 11.4 の ミラーリングを扱う採取票銀F照合0266です。銀F照合0266は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録銀F照合0266です。銀F照合0266ではRefresh状態と取得時刻を採取票銀F照合0266へ残します。銀F照合0266ではRefresh未完了の見落としを避けるため補助資料も照合する判断銀F照合0266です。銀F照合0266の用語整理では複製ミラーリングの対象値を実在出力で比較する記録銀F照合0266です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Table Status 0265」を「DDL後の表定義更新 Table Definition 0284」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするしてデータ定義対を照合する。
    - B. 保守作業で参照する機能は休止購読を見落として必要ログを削を避けるため・依存表示からOldestrequiredして依存表示を照合する。
    - C. 保守作業で参照する機能は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するして初期ロード状を照合する。 ✅
    - D. 保守作業で参照する機能は表定義未更新を避けるため・点検操作で判定欄を記録するしてサブスクリプを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能初期ロ・初期ロでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・照合）です。照合初期ロ・初期ロに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・初期ロです。比較ミラー・照合でA:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はミラー・初期ロ・照合です。運用照合・ミラーでB:の依存関係の確認 LOG13は「Log Dependencyで依存表示からO」を述べるため、正答側の照合軸は初期ロ・ミラー・照合です。仕様ミラー・初期ロでD:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は照合・初期ロ・初期ロです。用語初期ロ・照合という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・照合です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0265**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0265について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE025
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0265A
    ```

    画面・出力には IIDR114DD0265A が表示され、CDCミラーリング Table Status 0265 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE025
    Mirroring request accepted
    確認コード IIDR114DD0265B
    ```

    画面・出力には IIDR114DD0265B が表示され、CDCミラーリング Table Status 0265 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0265C
    ```

    画面・出力には IIDR114DD0265C が表示され、CDCミラーリング Table Status 0265 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0265A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0265B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0265C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0280 {#c11-i0465}
*分類: ミラーリング*  ・  難易度: 中級

蒼A抑止0281ではIBM IIDR 11.4 の ミラーリングを扱う採取票蒼A抑止0281です。蒼A抑止0281は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録蒼A抑止0281です。蒼A抑止0281ではRefresh状態と取得時刻を採取票蒼A抑止0281へ残します。蒼A抑止0281では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断蒼A抑止0281です。蒼A抑止0281の用語整理では複製ミラーリングの対象値を実在出力で区別する記録蒼A抑止0281です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0280を同一分類のデータストア接続 CDC Datastore 変更前の確認 STORE02と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は保守操作で監査欄を保存することで初期ロード状を確認し・対象サブスクリプションの取りを防ぐ。 ✅
    - B. 管理対象との関係を表す説明は通信活動からCHC9788Iを読むことで通信活動を確認し・ホスト名変更後の購読構成を更を防ぐ。
    - C. 管理対象との関係を表す説明はサブスクリプで翻訳表を確認することで翻訳表を確認し・翻訳表の誤読を防ぐ。
    - D. 管理対象との関係を表す説明は主操作で出力欄を評価することで16進ブックを確認し・ベンダー指示なしの位置変更を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能初期ロ・対象サでAの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・抑止）です。照合初期ロ・対象サに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・対象サです。運用抑止・ミラーでB:の変更前の確認 STORE02は「CDC Datastoreで通信活動からCH」を述べるため、正答側の照合軸は初期ロ・ミラー・抑止です。項目ミラー・対象サでC:の失敗時切り分け 翻訳表は「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸は対象サ・ミラー・初期ロです。仕様ミラー・初期ロでD:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸は抑止・対象サ・初期ロです。用語初期ロ・抑止という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・抑止です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0280**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0280について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE040
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0280A
    ```

    画面・出力には IIDR114DD0280A が表示され、CDCミラーリング Table Status 0280 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE040
    Mirroring request accepted
    確認コード IIDR114DD0280B
    ```

    画面・出力には IIDR114DD0280B が表示され、CDCミラーリング Table Status 0280 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0280C
    ```

    画面・出力には IIDR114DD0280C が表示され、CDCミラーリング Table Status 0280 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0280A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0280B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0280C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0295 {#c11-i0466}
*分類: ミラーリング*  ・  難易度: 中級

金P抑止0296ではIBM IIDR 11.4 の ミラーリングを扱う採取票金P抑止0296です。金P抑止0296は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録金P抑止0296です。金P抑止0296ではRefresh状態と取得時刻を採取票金P抑止0296へ残します。金P抑止0296ではイベント重大度の誤読を避けるため補助資料も照合する判断金P抑止0296です。金P抑止0296の用語整理では複製ミラーリングの対象値を実在出力で評価する記録金P抑止0296です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0295の設定や表示を読む前に役割を確認します。DDL後の表定義更新 Head of Log 0356ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするしてサブスクリプを照合する。
    - B. 対象資源に対する働きは接続認証の誤読を避けるため・エラー処理で接続認証を確認するして接続認証を照合する。
    - C. 対象資源に対する働きはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するして初期ロード状を照合する。 ✅
    - D. 対象資源に対する働きはデータ欠落を避けるため・監査操作で記録欄を比較するしてインスタンスを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能初期ロ・イベンでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・抑止）です。照合初期ロ・イベンに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・イベンです。比較ミラー・抑止でA:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はミラー・イベン・抑止です。運用抑止・ミラーでB:のマッピング検査 接続認証は「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸は初期ロ・ミラー・抑止です。仕様ミラー・初期ロでD:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は抑止・イベン・初期ロです。用語初期ロ・抑止という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・抑止です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0295**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0295について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE055
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0295A
    ```

    画面・出力には IIDR114DD0295A が表示され、CDCミラーリング Table Status 0295 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE055
    Mirroring request accepted
    確認コード IIDR114DD0295B
    ```

    画面・出力には IIDR114DD0295B が表示され、CDCミラーリング Table Status 0295 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0295C
    ```

    画面・出力には IIDR114DD0295C が表示され、CDCミラーリング Table Status 0295 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0295A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0295B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0295C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0310 {#c11-i0467}
*分類: ミラーリング*  ・  難易度: 中級

紺K解析0311ではIBM IIDR 11.4 の ミラーリングを扱う採取票紺K解析0311です。紺K解析0311は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録紺K解析0311です。紺K解析0311ではRefresh状態と取得時刻を採取票紺K解析0311へ残します。紺K解析0311では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断紺K解析0311です。紺K解析0311の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録紺K解析0311です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0310に関する障害切り分けの前提を確認しています。サブスクリプション管理 CDC Subscription 通常状態の確認 SUB01の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はCDC Subscriptionで定義表示からSubscriptionを読みである。定義表示からSubscriptionときは別サブスクリプションを停止まを防ぐ。
    - B. 表示や設定で扱う内容は複製対象の表対応と開始位置をまとめる管理単位を初期同期判定として確認する。初期同期判定で統合管理を確認するときは統合管理の誤読を防ぐ。
    - C. 表示や設定で扱う内容はミラーリングの項目の初期ロード状態と取得時刻を記録し・遅延ゼロ確認の欠落を防ぐである。確認操作で状態欄を整理するときは遅延ゼロ確認の欠落を防ぐ。 ✅
    - D. 表示や設定で扱う内容はHex Positionのインスタンス名と取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能初期ロ・遅延ゼでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・解析）です。照合初期ロ・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象はミラー・初期ロ・遅延ゼです。比較ミラー・解析でA:の通常状態の確認 SUB01は「CDC Subscriptionで定義表示か」を述べるため、正答側の照合軸はミラー・遅延ゼ・解析です。運用解析・ミラーでB:の初期同期判定 統合管理は「複製対象の表対応と開始位置をまとめる管理単位」を述べるため、正答側の照合軸は初期ロ・ミラー・解析です。仕様ミラー・初期ロでD:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は解析・遅延ゼ・初期ロです。用語初期ロ・解析という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・解析です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0310**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0310について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE070
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0310A
    ```

    画面・出力には IIDR114DD0310A が表示され、CDCミラーリング Table Status 0310 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE070
    Mirroring request accepted
    確認コード IIDR114DD0310B
    ```

    画面・出力には IIDR114DD0310B が表示され、CDCミラーリング Table Status 0310 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0310C
    ```

    画面・出力には IIDR114DD0310C が表示され、CDCミラーリング Table Status 0310 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0310A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0310B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0310C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0325 {#c11-i0468}
*分類: ミラーリング*  ・  難易度: 中級

銀F計画0326ではIBM IIDR 11.4 の ミラーリングを扱う採取票銀F計画0326です。銀F計画0326は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録銀F計画0326です。銀F計画0326ではRefresh状態と取得時刻を採取票銀F計画0326へ残します。銀F計画0326ではRefresh未完了の見落としを避けるため補助資料も照合する判断銀F計画0326です。銀F計画0326の用語整理では複製ミラーリングの対象値を実在出力で比較する記録銀F計画0326です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0325を保守記録に説明する必要があります。複製状態監視 Mirror Status 性能影響の確認 MIR11と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は性能影響確認でイベント表示を証跡に残し・Mirror Statusでイベント表示からheadoflo。
    - B. 保守作業で参照する機能は巡回で複製位置を証跡に残し・Bookmarkの複製位置と取得時刻を記録し。
    - C. 保守作業で参照する機能は計画で初期ロード状を証跡に残し・ミラーリングの項目の初期ロード状態と取得時刻を記録し。 ✅
    - D. 保守作業で参照する機能は保守でサブスクリプを証跡に残し・後の表定義更新の項目のサブスクリプション記述と取得時刻を記録。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能初期ロ・初期ロでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・計画）です。照合初期ロ・初期ロに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象は初期ロ・計画・初期ロです。比較ミラー・計画でA:の性能影響の確認 MIR11は「Mirror Statusでイベント表示から」を述べるため、正答側の照合軸はミラー・計画・初期ロです。運用計画・ミラーでB:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸は初期ロ・ミラー・計画です。仕様ミラー・初期ロでD:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は計画・初期ロ・初期ロです。用語初期ロ・計画という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0325**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0325について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE085
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0325A
    ```

    画面・出力には IIDR114DD0325A が表示され、CDCミラーリング Table Status 0325 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE085
    Mirroring request accepted
    確認コード IIDR114DD0325B
    ```

    画面・出力には IIDR114DD0325B が表示され、CDCミラーリング Table Status 0325 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0325C
    ```

    画面・出力には IIDR114DD0325C が表示され、CDCミラーリング Table Status 0325 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0325A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0325B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0325C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0340 {#c11-i0469}
*分類: ミラーリング*  ・  難易度: 上級

蒼A解除0341ではIBM IIDR 11.4 の ミラーリングを扱う採取票蒼A解除0341です。蒼A解除0341は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録蒼A解除0341です。蒼A解除0341ではRefresh状態と取得時刻を採取票蒼A解除0341へ残します。蒼A解除0341では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断蒼A解除0341です。蒼A解除0341の用語整理では複製ミラーリングの対象値を実在出力で区別する記録蒼A解除0341です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0340の技術的な意味を資料で確認するとき、サブスクリプション管理 CDC Subscription 性能影響の確認 SUB11との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は性能影響確認でイベント表示を証跡に残し・CDC Subscriptionでイベント表示からSever。
    - B. 管理対象との関係を表す説明は巡回でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。
    - C. 管理対象との関係を表す説明は解除で初期ロード状を証跡に残し・ミラーリングの項目の初期ロード状態と取得時刻を記録し。 ✅
    - D. 管理対象との関係を表す説明は保護で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し・データ欠落を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能初期ロ・対象サでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・解除）です。照合初期ロ・対象サに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象は初期ロ・解除・対象サです。比較ミラー・解除でA:の性能影響の確認 SUB11は「CDC Subscriptionでイベント表」を述べるため、正答側の照合軸はミラー・解除・初期ロです。運用解除・ミラーでB:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸は初期ロ・ミラー・解除です。仕様ミラー・初期ロでD:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は解除・対象サ・初期ロです。用語初期ロ・解除という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・対象サです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0340**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0340について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE100
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0340A
    ```

    画面・出力には IIDR114DD0340A が表示され、CDCミラーリング Table Status 0340 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE100
    Mirroring request accepted
    確認コード IIDR114DD0340B
    ```

    画面・出力には IIDR114DD0340B が表示され、CDCミラーリング Table Status 0340 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0340C
    ```

    画面・出力には IIDR114DD0340C が表示され、CDCミラーリング Table Status 0340 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0340A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0340B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0340C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Table Status 0355 {#c11-i0470}
*分類: ミラーリング*  ・  難易度: 上級

金P解除0356ではIBM IIDR 11.4 の ミラーリングを扱う採取票金P解除0356です。金P解除0356は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録金P解除0356です。金P解除0356ではRefresh状態と取得時刻を採取票金P解除0356へ残します。金P解除0356ではイベント重大度の誤読を避けるため補助資料も照合する判断金P解除0356です。金P解除0356の用語整理では複製ミラーリングの対象値を実在出力で評価する記録金P解除0356です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Table Status 0355について構成や状態を確認します。データストア接続 CDC Datastore 権限境界の確認 STORE12ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはイベント確認からcommunicatioことでイベント確認を確認し・ホスト名変更後の購読構成を更を防ぐ。
    - B. 対象資源に対する働きは保守操作で監査欄を保存することでミラー開始を確認し・対象サブスクリプションの取りを防ぐ。
    - C. 対象資源に対する働きは採取操作で照合欄を点検することで初期ロード状を確認し・イベント重大度の誤読を防ぐ。 ✅
    - D. 対象資源に対する働きは照合操作で確認欄を採取することでサブスクリプを確認し・対象インスタンスの取り違えを防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能初期ロ・イベンでCの記述「ミラーリングの項目の初期ロード状態と取得時刻を記録し」に対応する項目はTable Status（ミラー・初期ロ・解除）です。照合初期ロ・イベンに関するミラーリングの仕様は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」で、確認対象は初期ロ・解除・イベンです。比較ミラー・解除でA:の権限境界の確認 STORE12は「CDC Datastoreでイベント確認から」を述べるため、正答側の照合軸はミラー・解除・初期ロです。運用解除・ミラーでB:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸は初期ロ・ミラー・解除です。仕様ミラー・初期ロでD:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は解除・イベン・初期ロです。用語初期ロ・解除という用語は「ミラーリングの項目の初期ロード状態と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・イベンです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Table Status 0355**

    - 検証目的: CDCミラーリングのCDCミラーリング Table Status 0355について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Table Status と Refresh状態
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE115
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0355A
    ```

    画面・出力には IIDR114DD0355A が表示され、CDCミラーリング Table Status 0355 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE115
    Mirroring request accepted
    確認コード IIDR114DD0355B
    ```

    画面・出力には IIDR114DD0355B が表示され、CDCミラーリング Table Status 0355 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Table Status を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmstartmirror -I instance -s subscription
    → Enter を押す
    ```

    画面・出力:
    ```text
    Management Console event log
    Severity INFO
    Component Capture
    Subscription event recorded
    確認コード IIDR114DD0355C
    ```

    画面・出力には IIDR114DD0355C が表示され、CDCミラーリング Table Status 0355 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0355A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0355B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0355C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting




## IBM IIDR 11.4 > リフレッシュ制御

### CHCCLP ログ位置照合 ホスト検査 {#c11-i0471}
*分類: リフレッシュ制御*  ・  難易度: 上級

IBM IIDR 11.4 の リフレッシュ制御 で扱う「CHCCLP ログ位置照合 ホスト検査」は、CDC Replication のスクリプト操作に使うコマンドライン機能をログ位置照合の観点で確認する技術項目です。target datastore の統計とSUB069を同じ記録で見比べることで、再同期範囲の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** CHCCLP ログ位置照合 ホスト検査を保守記録に説明する必要があります。CDCミラーリング Replication Method 0028と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてサブスクリプを照合する。
    - B. 保守作業で参照する機能は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてイベントログを照合する。
    - C. 保守作業で参照する機能はホスト名変更後の購読構成を更新せを避けるため・接続表示からDatastoreを読むして接続表示を照合する。
    - D. 保守作業で参照する機能はホスト検査の誤読を避けるため・ログ位置照合でホスト検査を確認するしてホスト検査を照合する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** ログ・ホスト・ホスト検でDの記述「CDC Replication のスクリプト操作に使うコマンドライン」に対応する項目はログ位置照合 ホスト検査（ログ位・ホスト・ホスト検・ログ位）です。ログ位置時のホスト検査に関するリフレッシュ制御の仕様は「CDC Replication のスクリプト操作に使うコマンドライン」で、確認対象はログ位・ホスト・ホスト検・ログ位です。ミラ・棚卸・サブスクのA:は「CDCのサブスクリプション状態と取得時刻を記録し」を述べ、対象はReplication Method（ミラー・サブス・対象サブ・棚卸）です。確認・イベン・遅延ゼロのB:は「CDCのイベントログと取得時刻を記録し、遅延ゼロ確認の欠落を防ぐ」を述べ、対象はCDCミラーリング Subscrip（ミラー・イベン・遅延ゼロ・確認）です。依存関係時の接続表示のC:は「CDC Datastoreで接続表示からDatastoreを読み」を述べ、対象は依存関係の確認 STORE13（CDC・接続表・ホスト名・依存関）です。ホスト検査をログ位置照という用語は「CDC Replication」を指し、ログ位置照合 ホスト検査（ログ位・ホスト・ホスト検・ログ位）で照合する値はホスト検査です。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **CHCCLP ログ位置照合 ホスト検査**

    - 検証目的: リフレッシュ制御のCHCCLP ログ位置照合 ホスト検査について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リフレッシュ制御の対象へ進みます。
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
    SUB069           DS069          Mirroring   BMK069
    ```

    画面・出力には Subscription が含まれ、CHCCLP ログ位置照合 ホスト検査の証跡を確認できます。

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
    SUB069           DS069          BMK069
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### CHCCLP 失敗時切り分け 履歴行 {#c11-i0472}
*分類: リフレッシュ制御*  ・  難易度: 中級

IBM IIDR 11.4 の リフレッシュ制御 で扱う「CHCCLP 失敗時切り分け 履歴行」は、CDC Replication のスクリプト操作に使うコマンドライン機能を失敗時切り分けの観点で確認する技術項目です。target datastore の統計とSUB029を同じ記録で見比べることで、再同期範囲の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** CHCCLP 失敗時切り分け 履歴行を保守記録に説明する必要があります。CDCミラーリング Event Severity 0004と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は巡回でミラー開始を証跡に残し・CDCのミラー開始と取得時刻を記録し。
    - B. 運用時に利用する技術的役割は確認でインスタンスを証跡に残し・Hex Positionのインスタンス名と取得時刻を記録し。
    - C. 運用時に利用する技術的役割は停止確認で確認ではサブを証跡に残し・CDC Subscriptionで停止前の確認ではサブスクリ。
    - D. 運用時に利用する技術的役割はリフレッシュで履歴行を証跡に残し・CDC Replication のスクリプト操作に使うコマン。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** リフレッ対象失敗時切りでDの記述「CDC Replication のスクリプト操作に使うコマンドライン」に対応する項目は失敗時切り分け 履歴行（失敗時切り・リフレ・履歴行・履歴行の）です。リフレッ時の失敗時切りに関するリフレッシュ制御の仕様は「CDC Replication のスクリプト操作に使うコマンドライン」で、確認対象は失敗時切・リフレ・履歴行・履歴行のです。ミラーリン・巡回のA:は「CDCのミラー開始と取得時刻を記録し、対象サブスクリプションの取り違」を述べ、対象はEvent Severity（ミラーリン・巡回・ミラー・対象サブ）です。確認対象HexのB:は「Hex Positionのインスタンス名と取得時刻を記録し」を述べ、対象はHex Position（Hex・確認・インス・データ欠）です。停止確認時のCDCのC:は「CDC Subscriptionで停止前の確認ではサブスクリプション」を述べ、対象は停止前の確認 SUB14（CDC・停止確・確認で・別サブス）です。失敗時切をリフレッシという用語は「CDC Replication」を指し、失敗時切り分け 履歴行（失敗時切り・リフレ・履歴行・履歴行の）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **CHCCLP 失敗時切り分け 履歴行**

    - 検証目的: リフレッシュ制御のCHCCLP 失敗時切り分け 履歴行について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リフレッシュ制御の対象へ進みます。
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
    SUB029           DS029          Mirroring   BMK029
    ```

    画面・出力には Subscription が含まれ、CHCCLP 失敗時切り分け 履歴行の証跡を確認できます。

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
    SUB029           DS029          BMK029
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### capture service 状態確認 スケジュール {#c11-i0473}
*分類: リフレッシュ制御*  ・  難易度: 中級

IBM IIDR 11.4 の リフレッシュ制御 で扱う「capture service 状態確認 スケジュール」は、ソース変更を読み取りサブスクリプションへ渡す処理を状態確認の観点で確認する技術項目です。replication mapping 名とDS045を同じ記録で見比べることで、開始位置の取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** capture service 状態確認 スケジュールを保守記録に説明する必要があります。複製位置管理 Hex Position 0051と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は状態確認でスケジュールを証跡に残し・ソース変更を読み取りサブスクリプションへ渡す処理。 ✅
    - B. 保守作業で参照する機能は復旧でインスタンスを証跡に残し・Hex Positionのインスタンス名と取得時刻を記録し。
    - C. 保守作業で参照する機能は切替でミラー開始を証跡に残し・CDCのミラー開始と取得時刻を記録し。
    - D. 保守作業で参照する機能は権限境界確認で権限境界の確を証跡に残し・Mirror Statusで権限境界の確認では複製状態監視の。

    正解: **A** ／ 難易度: 中級

    **解説:** 状態確認対象captuでAの記述「ソース変更を読み取りサブスクリプションへ渡す処理である」に対応する項目は状態確認 スケジュール（captu・状態確・スケジ・スケジュ）です。状態確認時のcaptuに関するリフレッシュ制御の仕様は「ソース変更を読み取りサブスクリプションへ渡す処理」で、確認対象はcapt・状態確・スケジ・スケジュです。復旧対象HexのB:は「Hex Positionのインスタンス名と取得時刻を記録し」を述べ、対象はHex Position（Hex・復旧・インス・データ欠）です。切替時のミラーリンのC:は「CDCのミラー開始と取得時刻を記録し、Refresh未完了の見落とし」を述べ、対象はEvent Severity（ミラーリン・切替・ミラー・Refr）です。Mirrを権限境界確のD:は「Mirror Statusで権限境界の確認では複製状態監視の」を述べ、対象は権限境界の確認 MIR12（Mirro・権限境・権限境・Refr）です。captを状態確認という用語は「ソース変更を読み取りサブスクリプションへ渡す処理」を指し、状態確認 スケジュール（captu・状態確・スケジ・スケジュ）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **capture service 状態確認 スケジュール**

    - 検証目的: リフレッシュ制御のcapture service 状態確認 スケジュールについて、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リフレッシュ制御の対象へ進みます。
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
    SUB045           DS045          Mirroring   BMK045
    ```

    画面・出力には Subscription が含まれ、capture service 状態確認 スケジュールの証跡を確認できます。

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
    SUB045           DS045          BMK045
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### capture service 遅延監視 警告行 {#c11-i0474}
*分類: リフレッシュ制御*  ・  難易度: 初級

IBM IIDR 11.4 の リフレッシュ制御 で扱う「capture service 遅延監視 警告行」は、ソース変更を読み取りサブスクリプションへ渡す処理を遅延監視の観点で確認する技術項目です。replication mapping 名とDS005を同じ記録で見比べることで、開始位置の取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** capture service 遅延監視 警告行を保守記録に説明する必要があります。CDCミラーリング Latency 0007と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はイベント重大度の誤読を避けるため・採取操作で照合欄を点検するして遅延確認を照合する。
    - B. 運用時に利用する技術的役割は対象インスタンスの取り違えを避けるため・照合操作で確認欄を採取するしてインスタンスを照合する。
    - C. 運用時に利用する技術的役割は警告行の誤読を避けるため・リフレッシュで警告行を確認するして警告行を照合する。 ✅
    - D. 運用時に利用する技術的役割はRefresh未完了の見落としを避けるため・記録操作で証跡欄を照合するしてミラー開始を照合する。

    正解: **C** ／ 難易度: 初級

    **解説:** リフレッ対象captuでCの記述「ソース変更を読み取りサブスクリプションへ渡す処理を遅延監視として確認」に対応する項目は遅延監視 警告行（captu・リフレ・警告行・警告行の）です。リフレッ時のcaptuに関するリフレッシュ制御の仕様は「ソース変更を読み取りサブスクリプションへ渡す処理を遅延監視として確認」で、確認対象はcapt・リフレ・警告行・警告行のです。ミラーリン・巡回のA:は「CDCの遅延確認と取得時刻を記録し、イベント重大度の誤読を防ぐ」を述べ、対象はCDCミラーリング Latency（ミラーリン・巡回・遅延確・イベント）です。保守対象HexのB:は「Hex Positionのインスタンス名と取得時刻を記録し」を述べ、対象はHex Position（Hex・保守・インス・対象イン）です。ミラーリを解除のD:は「CDCのミラー開始と取得時刻を記録し、Refresh未完了の見落とし」を述べ、対象はEvent Severity（ミラーリン・解除・ミラー・Refr）です。captをリフレッシという用語は「ソース変更を読み取りサブスクリプションへ渡す処理を遅」を指し、遅延監視 警告行（captu・リフレ・警告行・警告行の）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **capture service 遅延監視 警告行**

    - 検証目的: リフレッシュ制御のcapture service 遅延監視 警告行について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リフレッシュ制御の対象へ進みます。
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
    SUB005           DS005          Mirroring   BMK005
    ```

    画面・出力には Subscription が含まれ、capture service 遅延監視 警告行の証跡を確認できます。

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
    SUB005           DS005          BMK005
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### refresh マッピング検査 管理レポート {#c11-i0475}
*分類: リフレッシュ制御*  ・  難易度: 上級

IBM IIDR 11.4 の リフレッシュ制御 で扱う「refresh マッピング検査 管理レポート」は、対象表を初期同期または再同期する複製操作をマッピング検査の観点で確認する技術項目です。bookmark valueとLOG077を同じ記録で見比べることで、対象表の不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** refresh マッピング検査 管理レポートを保守記録に説明する必要があります。CHC0368I 失敗時切り分け アーカイブと取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はリフレッシュで管理レポートを証跡に残し・対象表を初期同期または再同期する複製操作をマッピング検査とし。 ✅
    - B. 運用時に利用する技術的役割はブックマークでアーカイブを証跡に残し・bookmark まで適用したことを示す CDC。CHC0368I 失敗時切り分け アーカイブ固有の属性も確認対象に含める。
    - C. 運用時に利用する技術的役割は登録で表定義再読込を証跡に残し・DDLの表定義再読込と取得時刻を記録し。
    - D. 運用時に利用する技術的役割は構成監査で通信エラーを証跡に残し・CDC Event Logで通信エラーからERRORを読み。

    正解: **A** ／ 難易度: 上級

    **解説:** リフ・管理レ・管理レポでAの記述「対象表を初期同期または再同期する複製操作をマッピング検査として確認す」に対応する項目はマッピング検査 管理レポート（ref・管理レ・管理レポ・リフレ）です。リフレッ時の管理レポーに関するリフレッシュ制御の仕様は「対象表を初期同期または再同期する複製操作をマッピング検査として確認す」で、確認対象はref・管理レ・管理レポ・リフレです。ブッ・アーカ・アーカイのB:は「bookmark まで適用したことを示す CDC」を述べ、対象は失敗時切り分け アーカイブ（失敗時・アーカ・アーカイ・ブック）です。登録時の表定義再読のC:は「DDLの表定義再読込と取得時刻を記録し、Refresh中の再開を防ぐ」を述べ、対象はSource Table（後の表・表定義・Refr・登録）です。通信エラーを構成監査のD:は「CDC Event Logで通信エラーからERRORを読み」を述べ、対象は構成監査 ERR08（CDC・通信エ・情報イベ・構成監）です。管理レポーをリフレッシという用語は「対象表を初期同期または再同期する複製操作をマッピング」を指し、マッピング検査 管理レポート（ref・管理レ・管理レポ・リフレ）で照合する値は管理レポートです。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **refresh マッピング検査 管理レポート**

    - 検証目的: リフレッシュ制御のrefresh マッピング検査 管理レポートについて、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リフレッシュ制御の対象へ進みます。
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
    SUB077           DS077          Mirroring   BMK077
    ```

    画面・出力には Subscription が含まれ、refresh マッピング検査 管理レポートの証跡を確認できます。

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
    SUB077           DS077          BMK077
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### refresh 統計採取 サインオフ {#c11-i0476}
*分類: リフレッシュ制御*  ・  難易度: 中級

IBM IIDR 11.4 の リフレッシュ制御 で扱う「refresh 統計採取 サインオフ」は、対象表を初期同期または再同期する複製操作を統計採取の観点で確認する技術項目です。bookmark valueとLOG037を同じ記録で見比べることで、対象表の不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** refresh 統計採取 サインオフを保守記録に説明する必要があります。複製位置管理 Instance 0048と取り違えない説明はどれですか。

    - A. 仕様上の役割は復旧で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し。
    - B. 仕様上の役割は統計採取でサインオフを証跡に残し・対象表を初期同期または再同期する複製操作を統計採取として確認。 ✅
    - C. 仕様上の役割は保守でサブスクリプを証跡に残し・DDLのサブスクリプション記述と取得時刻を記録し。
    - D. 仕様上の役割は性能影響確認で性能影響の確を証跡に残し・Table Mappingで性能影響の確認ではマッピング管理。

    正解: **B** ／ 難易度: 中級

    **解説:** 統計採取対象refreでBの記述「対象表を初期同期または再同期する複製操作を統計採取として確認する」に対応する項目は統計採取 サインオフ（refre・統計採・サイン・サインオ）です。統計採取時のrefreに関するリフレッシュ制御の仕様は「対象表を初期同期または再同期する複製操作を統計採取として確認する」で、確認対象はrefr・統計採・サイン・サインオです。Insta・復旧のA:は「Instanceの戻り値と取得時刻を記録し」を述べ、対象は複製位置管理 Instance（Insta・復旧・戻り値・対象イン）です。保守時の後の表定義のC:は「DDLのサブスクリプション記述と取得時刻を記録し、表定義未更新を防ぐ」を述べ、対象はof Log（後の表定義・保守・サブス・表定義未）です。Tablを性能影響確のD:は「Table Mappingで性能影響の確認ではマッピング管理の」を述べ、対象は性能影響の確認 MAP11（Table・性能影・性能影・DDL変）です。refrを統計採取という用語は「対象表を初期同期または再同期する複製操作を統計採取と」を指し、統計採取 サインオフ（refre・統計採・サイン・サインオ）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **refresh 統計採取 サインオフ**

    - 検証目的: リフレッシュ制御のrefresh 統計採取 サインオフについて、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リフレッシュ制御の対象へ進みます。
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
    SUB037           DS037          Mirroring   BMK037
    ```

    画面・出力には Subscription が含まれ、refresh 統計採取 サインオフの証跡を確認できます。

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
    SUB037           DS037          BMK037
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### replication mapping 初期同期判定 承認履歴 {#c11-i0477}
*分類: リフレッシュ制御*  ・  難易度: 初級

IBM IIDR 11.4 の リフレッシュ制御 で扱う「replication mapping 初期同期判定 承認履歴」は、ソース表とターゲット表の対応および列変換を示す定義を初期同期判定の観点で確認する技術項目です。CHC0368I メッセージとMAP013を同じ記録で見比べることで、データストア接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** replication mapping 初期同期判定 承認履歴を保守記録に説明する必要があります。capture service マッピング検査 接続認証と取り違えない説明はどれですか。

    - A. 仕様上の役割はソース変更を読み取りサブスクリプションへ渡す処理をマッピング検査として確認する。エラー処理で接続認証を確認するときは接続認証の誤読を防ぐ。
    - B. 仕様上の役割はCDCのイベントログと取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。
    - C. 仕様上の役割はInstanceの戻り値と取得時刻を記録し・重複反映を防ぐである。変更確認操作で採取欄を棚卸するときは重複反映を防ぐ。
    - D. 仕様上の役割はソース表とターゲット表の対応および列変換を示す定義を初期同期判定として確認する。初期同期判定で承認履歴を確認するときは承認履歴の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 初期同期対象repliでDの記述「ソース表とターゲット表の対応および列変換を示す定義を初期同期判定とし」に対応する項目は初期同期判定 承認履歴（repli・初期同・承認履・承認履歴）です。初期同期時のrepliに関するリフレッシュ制御の仕様は「ソース表とターゲット表の対応および列変換を示す定義を初期同期判定とし」で、確認対象はrepl・初期同・承認履・承認履歴です。captu・エラー処理のA:は「ソース変更を読み取りサブスクリプションへ渡す処理をマッピング検査とし」を述べ、対象はマッピング検査 接続認証（captu・エラー・接続認・接続認証）です。収集対象ミラーリンのB:は「CDCのイベントログと取得時刻を記録し、対象サブスクリプションの取り」を述べ、対象はCDCミラーリング Subscrip（ミラーリン・収集・イベン・対象サブ）です。解析時のInstaのC:は「Instanceの戻り値と取得時刻を記録し、重複反映を防ぐ」を述べ、対象は複製位置管理 Instance（Insta・解析・戻り値・重複反映）です。replを初期同期判という用語は「ソース表とターゲット表の対応および列変換を示す定義を」を指し、初期同期判定 承認履歴（repli・初期同・承認履・承認履歴）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **replication mapping 初期同期判定 承認履歴**

    - 検証目的: リフレッシュ制御のreplication mapping 初期同期判定 承認履歴について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リフレッシュ制御の対象へ進みます。
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
    SUB013           DS013          Mirroring   BMK013
    ```

    画面・出力には Subscription が含まれ、replication mapping 初期同期判定 承認履歴の証跡を確認できます。

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
    SUB013           DS013          BMK013
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### replication mapping 開始位置指定 ルール読替 {#c11-i0478}
*分類: リフレッシュ制御*  ・  難易度: 中級

IBM IIDR 11.4 の リフレッシュ制御 で扱う「replication mapping 開始位置指定 ルール読替」は、ソース表とターゲット表の対応および列変換を示す定義を開始位置指定の観点で確認する技術項目です。CHC0368I メッセージとMAP053を同じ記録で見比べることで、データストア接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** replication mapping 開始位置指定 ルール読替を保守記録に説明する必要があります。DDL後の表定義更新 Table Definition 0059と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は表示操作で対象欄を追跡することでDDL対象表を確認し・Refresh中の再開を防ぐ。
    - B. 運用時に利用する技術的役割はリフレッシュでルール読替を確認することでルール読替を確認し・ルール読替の誤読を防ぐ。 ✅
    - C. 運用時に利用する技術的役割は点検操作で判定欄を記録することで表定義再読込を確認し・表定義未更新を防ぐ。
    - D. 運用時に利用する技術的役割は完了確認からRowsappliedを読むことで完了確認を確認し・Refresh未完了でMirを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** リフ・ルール・ルール読でBの記述「ソース表とターゲット表の対応および列変換を示す定義である」に対応する項目は開始位置指定 ルール読替（rep・ルール・ルール読・リフレ）です。リフレッ時のルール読替に関するリフレッシュ制御の仕様は「ソース表とターゲット表の対応および列変換を示す定義」で、確認対象はrep・ルール・ルール読・リフレです。後の・復旧・DDL対のA:は「DDLのDDL対象表と取得時刻を記録し、Refresh中の再開を防ぐ」を述べ、対象はTable Definition（後の表・DDL・Refr・復旧）です。切替時の表定義再読のC:は「DDLの表定義再読込と取得時刻を記録し、表定義未更新を防ぐ」を述べ、対象はSource Table（後の表・表定義・表定義未・切替）です。完了確認を再始動確認のD:は「CDC Refreshで完了確認からRowsappliedを読み」を述べ、対象は再始動後の確認 REF15（CDC・完了確・Refr・再始動）です。ルール読替をリフレッシという用語は「ソース表とターゲット表の対応および列変換を示す定義」を指し、開始位置指定 ルール読替（rep・ルール・ルール読・リフレ）で照合する値はルール読替です。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **replication mapping 開始位置指定 ルール読替**

    - 検証目的: リフレッシュ制御のreplication mapping 開始位置指定 ルール読替について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リフレッシュ制御の対象へ進みます。
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
    SUB053           DS053          Mirroring   BMK053
    ```

    画面・出力には Subscription が含まれ、replication mapping 開始位置指定 ルール読替の証跡を確認できます。

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
    SUB053           DS053          BMK053
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### subscription ログ位置照合 プロファイル {#c11-i0479}
*分類: リフレッシュ制御*  ・  難易度: 中級

IBM IIDR 11.4 の リフレッシュ制御 で扱う「subscription ログ位置照合 プロファイル」は、複製対象の表対応と開始位置をまとめる管理単位をログ位置照合の観点で確認する技術項目です。list subscriptions の表とBMK061を同じ記録で見比べることで、適用遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** subscription ログ位置照合 プロファイルを保守記録に説明する必要があります。DDL後の表定義更新 Refresh Table 0068と取り違えない説明はどれですか。

    - A. 仕様上の役割は監査で再開条件を証跡に残し・DDLの再開条件と取得時刻を記録し・ログ先頭未到達の見落とし。
    - B. 仕様上の役割は収集で遅延確認を証跡に残し・CDCの遅延確認と取得時刻を記録し・イベント重大度の誤読を防。
    - C. 仕様上の役割はログ位置照合でプロファイルを証跡に残し・複製対象の表対応と開始位置をまとめる管理単位。 ✅
    - D. 仕様上の役割は依存関係確認で接続表示を証跡に残し・CDC Datastoreで接続表示からDatastoreを。

    正解: **C** ／ 難易度: 中級

    **解説:** ログ・プロフ・プロファでCの記述「複製対象の表対応と開始位置をまとめる管理単位である」に対応する項目はログ位置照合 プロファイル（sub・プロフ・プロファ・ログ位）です。ログ位置時のプロファイに関するリフレッシュ制御の仕様は「複製対象の表対応と開始位置をまとめる管理単位」で、確認対象はsub・プロフ・プロファ・ログ位です。後の・監査・再開条件のA:は「DDLの再開条件と取得時刻を記録し、ログ先頭未到達の見落としを防ぐ」を述べ、対象はRefresh Table（後の表・再開条・ログ先頭・監査）です。収集・遅延確・イベントのB:は「CDCの遅延確認と取得時刻を記録し、イベント重大度の誤読を防ぐ」を述べ、対象はCDCミラーリング Latency（ミラー・遅延確・イベント・収集）です。接続表示を依存関係確のD:は「CDC Datastoreで接続表示からDatastoreを読み」を述べ、対象は依存関係の確認 STORE13（CDC・接続表・ホスト名・依存関）です。プロファイをログ位置照という用語は「複製対象の表対応と開始位置をまとめる管理単位」を指し、ログ位置照合 プロファイル（sub・プロフ・プロファ・ログ位）で照合する値はプロファイルです。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **subscription ログ位置照合 プロファイル**

    - 検証目的: リフレッシュ制御のsubscription ログ位置照合 プロファイルについて、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リフレッシュ制御の対象へ進みます。
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
    SUB061           DS061          Mirroring   BMK061
    ```

    画面・出力には Subscription が含まれ、subscription ログ位置照合 プロファイルの証跡を確認できます。

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
    SUB061           DS061          BMK061
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### subscription 失敗時切り分け 保護設定 {#c11-i0480}
*分類: リフレッシュ制御*  ・  難易度: 中級

IBM IIDR 11.4 の リフレッシュ制御 で扱う「subscription 失敗時切り分け 保護設定」は、複製対象の表対応と開始位置をまとめる管理単位を失敗時切り分けの観点で確認する技術項目です。list subscriptions の表とBMK021を同じ記録で見比べることで、適用遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I

??? question "確認問題（1問）"
    **問題.** subscription 失敗時切り分け 保護設定を保守記録に説明する必要があります。DDL後の表定義更新 Refresh Table 0008と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はDDLの再開条件と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。
    - B. 保守作業で参照する機能はInstanceの戻り値と取得時刻を記録し・IBM指示なしの位置変更を防ぐである。主操作で出力欄を評価するときはIBM指示なしの位置変更を防ぐ。
    - C. 保守作業で参照する機能は複製対象の表対応と開始位置をまとめる管理単位を失敗時切り分けとして確認する。保護設定で保護設定を確認するときは保護設定の誤読を防ぐ。 ✅
    - D. 保守作業で参照する機能はCDCのミラー開始と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 保護設定対象subscでCの記述「複製対象の表対応と開始位置をまとめる管理単位を失敗時切り分けとして確」に対応する項目は失敗時切り分け 保護設定（subsc・保護設・保護設・保護設定）です。保護設定時のsubscに関するリフレッシュ制御の仕様は「複製対象の表対応と開始位置をまとめる管理単位を失敗時切り分けとして確」で、確認対象はsubs・保護設・保護設・保護設定です。後の表定義・巡回のA:は「DDLの再開条件と取得時刻を記録し、ログ先頭未到達の見落としを防ぐ」を述べ、対象はRefresh Table（後の表定義・巡回・再開条・ログ先頭）です。登録対象InstaのB:は「Instanceの戻り値と取得時刻を記録し」を述べ、対象は複製位置管理 Instance（Insta・登録・戻り値・IBM指）です。ミラーリを解析のD:は「CDCのミラー開始と取得時刻を記録し、イベント重大度の誤読を防ぐ」を述べ、対象はEvent Severity（ミラーリン・解析・ミラー・イベント）です。subsを保護設定という用語は「複製対象の表対応と開始位置をまとめる管理単位を失敗時」を指し、失敗時切り分け 保護設定（subsc・保護設・保護設・保護設定）に該当します。

    **出典:** IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I


??? note "検証手順（1件）"
    **subscription 失敗時切り分け 保護設定**

    - 検証目的: リフレッシュ制御のsubscription 失敗時切り分け 保護設定について、IBM IIDR 11.4の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM IIDR 11.4の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リフレッシュ制御の対象へ進みます。
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
    SUB021           DS021          Mirroring   BMK021
    ```

    画面・出力には Subscription が含まれ、subscription 失敗時切り分け 保護設定の証跡を確認できます。

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
    SUB021           DS021          BMK021
    ```

    画面・出力には ResultStringTable が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の CHCCLP が画面・出力に表示されること
    ② ステップ2 の Subscription が画面・出力に表示されること
    ③ ステップ3 の ResultStringTable が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_IIDR_11.4_CHCCLP_Commands / IBM IIDR 11.4 Capture service (CECC) / CDC Replication messages CHC0368I



### リフレッシュ制御 CDC Refresh ログとの照合 REF07 {#c11-i0481}
*分類: リフレッシュ制御*  ・  難易度: 中級

ログとの照合では リフレッシュ制御 の 方式表示 を主操作として REF07 を判定します。時刻と対象識別子への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF07 に残します。ログとの照合を補助する 方式変更 では Returnvalue を補助値として REF07 へ保存します。主判定のログとの照合ではリフレッシュ制御の 方式表示 から Refreshing を読み REF07 へ残します。証跡照合のログとの照合ではリフレッシュ制御の Refreshing と Returnvalue を REF07 に保存します。記録対応のログとの照合ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF07 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh ログとの照合 REF07について構成や状態を確認します。datastore 開始位置指定 停止時刻ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは停止時刻の誤読を避けるため・データストアで停止時刻を確認するして停止時刻を照合する。datastore 開始位置指定 停止時刻固有の属性も確認対象に含める。
    - B. 対象資源に対する働きは遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてミラー開始を照合する。
    - C. 対象資源に対する働きは初期ロード未完了でMirrorへを避けるため・方式表示から初期ロードingを読むして方式表示を照合する。 ✅
    - D. 対象資源に対する働きは対象インスタンスの取り違えを避けるため・照合操作で確認欄を採取するしてインスタンスを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能方式表・初期ロでCの記述「変更データ取得 初期ロードで方式表示から」に対応する項目はログとの照合 REF07（変更デ・方式表・ログと）です。照合方式表・ログとに関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで方式表示から 初期ロードing を読み」で、確認対象は方式表・ログと・初期ロです。比較リフレ・ログとでA:の開始位置指定 停止時刻は「CDC Replication」を述べるため、正答側の照合軸は変更デ・ログと・方式表です。運用ログと・変更デでB:のEvent Severityは「変更データ取得のミラー開始と取得時刻を記録し」を述べるため、正答側の照合軸は方式表・リフレ・ログとです。仕様方式表・ログとでD:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸はログと・初期ロ・方式表です。用語方式表・ログとという用語は「変更データ取得 初期ロードで方式表示から」を指し、照合する値と誤認リスクの組合せはリフレ・方式表・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh ログとの照合 REF07**

    - 検証目的: リフレッシュ制御のCDC Refreshについて操作とログを対応し、REF07のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB07を指定し、REF07の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB07
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB07 Replication method Refresh Table APP.REF07 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB07 -t APP.REF07 -mを指定し、REF07の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB07 -t APP.REF07 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF07 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB07を指定し、REF07の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB07
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF07 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Refreshing が画面・出力に表示されること
    ② ステップ2 の Replication が画面・出力に表示されること
    ③ ステップ3 の Table が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 代替経路の確認 REF10 {#c11-i0482}
*分類: リフレッシュ制御*  ・  難易度: 中級

代替経路の確認では リフレッシュ制御 の 方式表示 を主操作として REF10 を判定します。主経路との役割差への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF10 に残します。代替経路の確認を補助する 方式変更 では Returnvalue を補助値として REF10 へ保存します。主判定の代替経路の確認ではリフレッシュ制御の 方式表示 から Refreshing を読み REF10 へ残します。証跡照合の代替経路の確認ではリフレッシュ制御の Refreshing と Returnvalue を REF10 に保存します。記録対応の代替経路の確認ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF10 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 代替経路の確認 REF10に関する障害切り分けの前提を確認しています。capture service 統計採取 接続状態の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は接続状態の誤読を避けるため・統計採取で接続状態を確認するして接続状態を照合する。
    - B. 表示や設定で扱う内容は初期ロード未完了でMirrorへを避けるため・方式表示から初期ロードingを読むして方式表示を照合する。 ✅
    - C. 表示や設定で扱う内容は初期ロード中の再開を避けるため・表示操作で対象欄を追跡するしてログ先頭到達を照合する。DDL後の表定義更新 Subscription 0107固有の属性も確認対象に含める。
    - D. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するしてミラー開始を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能方式表・初期ロでBの記述「変更データ取得 初期ロードで方式表示から」に対応する項目は代替経路の確認 REF10（変更デ・方式表・代替経）です。照合方式表・代替経に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで方式表示から 初期ロードing を読み」で、確認対象は方式表・代替経・初期ロです。比較リフレ・代替経でA:の統計採取 接続状態は「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸は変更デ・代替経・方式表です。項目方式表・代替経でC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は初期ロ・リフレ・方式表です。仕様方式表・代替経でD:のEvent Severityは「変更データ取得のミラー開始と取得時刻を記録し」を述べるため、正答側の照合軸は代替経・初期ロ・方式表です。用語方式表・代替経という用語は「変更データ取得 初期ロードで方式表示から」を指し、照合する値と誤認リスクの組合せはリフレ・方式表・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 代替経路の確認 REF10**

    - 検証目的: リフレッシュ制御のCDC Refreshについて代替手段の成立を確認し、REF10のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB10を指定し、REF10の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB10
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB10 Replication method Refresh Table APP.REF10 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB10 -t APP.REF10 -mを指定し、REF10の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB10 -t APP.REF10 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF10 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB10を指定し、REF10の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB10
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF10 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Refreshing が画面・出力に表示されること
    ② ステップ2 の Replication が画面・出力に表示されること
    ③ ステップ3 の Table が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 依存関係の確認 REF13 {#c11-i0483}
*分類: リフレッシュ制御*  ・  難易度: 中級

依存関係の確認では リフレッシュ制御 の 方式表示 を主操作として REF13 を判定します。前提資源と後続処理の順序への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF13 に残します。依存関係の確認を補助する 方式変更 では Returnvalue を補助値として REF13 へ保存します。主判定の依存関係の確認ではリフレッシュ制御の 方式表示 から Refreshing を読み REF13 へ残します。証跡照合の依存関係の確認ではリフレッシュ制御の Refreshing と Returnvalue を REF13 に保存します。記録対応の依存関係の確認ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF13 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「リフレッシュ制御 CDC Refresh 依存関係の確認 REF13」を「ログ依存・サポート Log Dependency 復旧準備 LOG05」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は購読確認からInactiveを読むことで購読確認を確認し・休止購読を見落として必要ログを防ぐ。
    - B. 保守作業で参照する機能は採取操作で照合欄を点検することで遅延確認を確認し・イベント重大度の誤読を防ぐ。
    - C. 保守作業で参照する機能は方式表示から初期ロードingを読むことで方式表示を確認し・初期ロード未完了でMirroを防ぐ。 ✅
    - D. 保守作業で参照する機能は点検操作で判定欄を記録することで再開条件を確認し・表定義未更新を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能方式表・初期ロでCの記述「変更データ取得 初期ロードで方式表示から」に対応する項目は依存関係の確認 REF13（変更デ・方式表・依存関）です。照合方式表・依存関に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで方式表示から 初期ロードing を読み」で、確認対象は方式表・依存関・初期ロです。比較リフレ・依存関でA:の復旧準備 LOG05は「ログ依存で購読確認から Inactive」を述べるため、正答側の照合軸は変更デ・依存関・方式表です。運用依存関・変更デでB:のCDCミラーリングは「変更データ取得の遅延確認と取得時刻を記録し」を述べるため、正答側の照合軸は方式表・リフレ・依存関です。仕様方式表・依存関でD:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は依存関・初期ロ・方式表です。用語方式表・依存関という用語は「変更データ取得 初期ロードで方式表示から」を指し、照合する値と誤認リスクの組合せはリフレ・方式表・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 依存関係の確認 REF13**

    - 検証目的: リフレッシュ制御のCDC Refreshについて依存資源を点検し、REF13のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB13を指定し、REF13の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB13
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB13 Replication method Refresh Table APP.REF13 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB13 -t APP.REF13 -mを指定し、REF13の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB13 -t APP.REF13 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF13 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB13を指定し、REF13の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB13
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF13 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Refreshing が画面・出力に表示されること
    ② ステップ2 の Replication が画面・出力に表示されること
    ③ ステップ3 の Table が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### リフレッシュ制御 CDC Refresh 停止前の確認 REF14 {#c11-i0484}
*分類: リフレッシュ制御*  ・  難易度: 中級

停止前の確認では リフレッシュ制御 の 方式変更 を主操作として REF14 を判定します。処理中資源と未完了要求への注意として「Refresh未完了でMirrorへ戻して欠落行を残す危険があります」を REF14 に残します。停止前の確認を補助する 完了確認 では Rowsapplied を補助値として REF14 へ保存します。主判定の停止前の確認ではリフレッシュ制御の 方式変更 から Returnvalue を読み REF14 へ残します。証跡照合の停止前の確認ではリフレッシュ制御の Returnvalue と Rowsapplied を REF14 に保存します。記録対応の停止前の確認ではリフレッシュ制御の Refresh ProgressとRows Applied の証跡へ REF14 を結びます。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** リフレッシュ制御 CDC Refresh 停止前の確認 REF14の役割を調べています。datastore 統計採取 転送条件の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は統計採取で転送条件を確認することで転送条件を確認し・転送条件の誤読を防ぐ。
    - B. 障害切り分けに用いる役割は方式変更からReturnvalueを読むことで方式変更を確認し・初期ロード未完了でMirroを防ぐ。 ✅
    - C. 障害切り分けに用いる役割は採取操作で照合欄を点検することでイベントログを確認し・イベント重大度の誤読を防ぐ。CDCミラーリング Subscription 0151固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割は調査操作で保守欄を引き継ぎすることでログ先頭到達を確認し・ログ先頭未到達の見落としを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能方式変・初期ロでBの記述「変更データ取得 初期ロードで方式変更から」に対応する項目は停止前の確認 REF14（変更デ・方式変・停止確）です。照合方式変・停止確に関するリフレッシュ制御の仕様は「変更データ取得 初期ロードで方式変更から Returnvalue」で、確認対象は方式変・停止確・初期ロです。比較リフレ・停止確でA:の統計採取 転送条件は「CDC Replication」を述べるため、正答側の照合軸は変更デ・停止確・方式変です。項目方式変・停止確でC:のCDCミラーリングは「変更データ取得のイベントログと取得時刻を記録」を述べるため、正答側の照合軸は初期ロ・リフレ・方式変です。仕様方式変・停止確でD:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は停止確・初期ロ・方式変です。用語方式変・停止確という用語は「変更データ取得 初期ロードで方式変更から」を指し、照合する値と誤認リスクの組合せはリフレ・方式変・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **リフレッシュ制御 CDC Refresh 停止前の確認 REF14**

    - 検証目的: リフレッシュ制御のCDC Refreshについて安全な停止条件を確認し、REF14のRefresh ProgressとRows Appliedを実出力で確認する。
    - 前提条件: IBM IIDR 11.4の参照権限を持ち、対象REF14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM IIDR 11.4の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmsetreplicationmethod -I SRC1 -s SUB14 -t APP.REF14 -mを指定し、REF14の方式変更を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmsetreplicationmethod -I SRC1 -s SUB14 -t APP.REF14 -m
    → Enter を押す
    ```

    画面・出力:
    ```text
    Replication method for APP.REF14 changed to Mirror. Return value 0.
    ```

    画面・出力にあるReplicationを読み、Refresh ProgressとRows Appliedと対象REF14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へManagement Console > Monitoring > SUB14を指定し、REF14の完了確認を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> Management Console > Monitoring > SUB14
    → Enter を押す
    ```

    画面・出力:
    ```text
    Table APP.REF14 Status Mirroring Rows applied 184220 Latency 0 seconds
    ```

    画面・出力にあるTableを読み、Refresh ProgressとRows Appliedと対象REF14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4のリフレッシュ制御を確認する入力画面です。COMMAND入力口へdmdescribe -I SRC1 -s SUB14を指定し、REF14の方式表示を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面
    COMMAND ===> dmdescribe -I SRC1 -s SUB14
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription SUB14 Replication method Refresh Table APP.REF14 Status Refreshing
    ```

    画面・出力にあるRefreshingを読み、Refresh ProgressとRows Appliedと対象REF14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Replication が画面・出力に表示されること
    ② ステップ2 の Table が画面・出力に表示されること
    ③ ステップ3 の Refreshing が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



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


