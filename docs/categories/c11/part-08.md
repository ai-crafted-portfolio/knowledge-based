---
search:
  exclude: true
---

# IBM IIDR 11.4 — 詳細 (8/11)

[← IBM IIDR 11.4 の概要へ戻る](index.md)


## IBM IIDR 11.4 > ミラーリング

### CDCミラーリング Latency 0052 {#c11-i0378}
*分類: ミラーリング*  ・  難易度: 中級

桃M復旧0053ではIBM IIDR 11.4 の ミラーリングを扱う採取票桃M復旧0053です。桃M復旧0053は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録桃M復旧0053です。桃M復旧0053では遅延確認と取得時刻を採取票桃M復旧0053へ残します。桃M復旧0053では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断桃M復旧0053です。桃M復旧0053の用語整理では複製ミラーリングの対象値を実在出力で区別する記録桃M復旧0053です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0052の技術的な意味を資料で確認するとき、CDCミラーリング Subscription 0061との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は初期ロード未完了の見落としを避けるため・記録操作で証跡欄を照合するしてイベントログを照合する。
    - B. 管理対象との関係を表す説明はベンダー指示なしの位置変更を避けるため・主操作で出力欄を評価するしてサブスクリプを照合する。
    - C. 管理対象との関係を表す説明は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するして遅延確認を照合する。 ✅
    - D. 管理対象との関係を表す説明は送信回数だけでターゲット適用完了を避けるため・通信統計からSendsを読むして通信統計を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能遅延確・対象サでCの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・復旧）です。照合遅延確・対象サに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・対象サです。比較ミラー・復旧でA:のCDCミラーリングは「ミラーリングの項目のイベントログと取得時刻を」を述べるため、正答側の照合軸はミラー・対象サ・復旧です。運用復旧・ミラーでB:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は遅延確・ミラー・復旧です。仕様ミラー・遅延確でD:の依存関係の確認 STAT13は「CDC Communicationsで通信統」を述べるため、正答側の照合軸は復旧・対象サ・遅延確です。用語遅延確・復旧という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・復旧です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0052**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0052について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE052
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0052A
    ```

    画面・出力には IIDR114DD0052A が表示され、CDCミラーリング Latency 0052 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE052
    Mirroring request accepted
    確認コード IIDR114DD0052B
    ```

    画面・出力には IIDR114DD0052B が表示され、CDCミラーリング Latency 0052 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0052C
    ```

    画面・出力には IIDR114DD0052C が表示され、CDCミラーリング Latency 0052 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0052A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0052B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0052C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0067 {#c11-i0379}
*分類: ミラーリング*  ・  難易度: 中級

茶H監査0068ではIBM IIDR 11.4 の ミラーリングを扱う採取票茶H監査0068です。茶H監査0068は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録茶H監査0068です。茶H監査0068では遅延確認と取得時刻を採取票茶H監査0068へ残します。茶H監査0068ではイベント重大度の誤読を避けるため補助資料も照合する判断茶H監査0068です。茶H監査0068の用語整理では複製ミラーリングの対象値を実在出力で評価する記録茶H監査0068です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0067について構成や状態を確認します。CDCミラーリング Replication Method 0148ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するしてサブスクリプを照合する。
    - B. 対象資源に対する働きはイベント重大度の誤読を避けるため・採取操作で照合欄を点検するして遅延確認を照合する。 ✅
    - C. 対象資源に対する働きはデータ定義対象表の漏れを避けるため・復旧操作で点検欄を確認するしてログ先頭到達を照合する。
    - D. 対象資源に対する働きは休止購読を見落として必要ログを削を避けるため・依存表示からOldestrequiredして依存表示を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能遅延確・イベンでBの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・監査）です。照合遅延確・イベンに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・イベンです。比較ミラー・監査でA:のReplicationは「ミラーリングの項目のサブスクリプション状態と」を述べるため、正答側の照合軸はミラー・イベン・監査です。項目ミラー・イベンでC:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸はイベン・ミラー・遅延確です。仕様ミラー・遅延確でD:のログとの照合 LOG07は「Log Dependencyで依存表示からO」を述べるため、正答側の照合軸は監査・イベン・遅延確です。用語遅延確・監査という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・監査です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0067**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0067について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE067
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0067A
    ```

    画面・出力には IIDR114DD0067A が表示され、CDCミラーリング Latency 0067 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE067
    Mirroring request accepted
    確認コード IIDR114DD0067B
    ```

    画面・出力には IIDR114DD0067B が表示され、CDCミラーリング Latency 0067 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0067C
    ```

    画面・出力には IIDR114DD0067C が表示され、CDCミラーリング Latency 0067 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0067A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0067B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0067C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0082 {#c11-i0380}
*分類: ミラーリング*  ・  難易度: 中級

緑C変更0083ではIBM IIDR 11.4 の ミラーリングを扱う採取票緑C変更0083です。緑C変更0083は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録緑C変更0083です。緑C変更0083では遅延確認と取得時刻を採取票緑C変更0083へ残します。緑C変更0083では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断緑C変更0083です。緑C変更0083の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録緑C変更0083です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0082の役割を調べています。DDL後の表定義更新 Subscription 0122の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は後の表定義更新の項目のログ先頭到達と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。
    - B. 表示や設定で扱う内容は後の表定義更新の項目の再開条件と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。
    - C. 表示や設定で扱う内容はミラーリングの項目の遅延確認と取得時刻を記録し・遅延ゼロ確認の欠落を防ぐである。確認操作で状態欄を整理するときは遅延ゼロ確認の欠落を防ぐ。 ✅
    - D. 表示や設定で扱う内容はCDC Replication のスクリプト操作に使うコマンドライン機能である。復旧手掛かりで復旧手掛かりを確認するときは復旧手掛かりの誤読を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能遅延確・遅延ゼでCの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・変更）です。照合遅延確・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・遅延ゼです。比較ミラー・変更でA:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸はミラー・遅延ゼ・変更です。運用変更・ミラーでB:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は遅延確・ミラー・変更です。仕様ミラー・遅延確でD:の状態確認 復旧手掛かりは「CDC Replication」を述べるため、正答側の照合軸は変更・遅延ゼ・遅延確です。用語遅延確・変更という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・変更です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0082**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0082について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE082
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0082A
    ```

    画面・出力には IIDR114DD0082A が表示され、CDCミラーリング Latency 0082 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE082
    Mirroring request accepted
    確認コード IIDR114DD0082B
    ```

    画面・出力には IIDR114DD0082B が表示され、CDCミラーリング Latency 0082 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0082C
    ```

    画面・出力には IIDR114DD0082C が表示され、CDCミラーリング Latency 0082 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0082A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0082B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0082C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0097 {#c11-i0381}
*分類: ミラーリング*  ・  難易度: 中級

藤R変更0098ではIBM IIDR 11.4 の ミラーリングを扱う採取票藤R変更0098です。藤R変更0098は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録藤R変更0098です。藤R変更0098では遅延確認と取得時刻を採取票藤R変更0098へ残します。藤R変更0098ではRefresh未完了の見落としを避けるため補助資料も照合する判断藤R変更0098です。藤R変更0098の用語整理では複製ミラーリングの対象値を実在出力で比較する記録藤R変更0098です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Latency 0097」を「DDL後の表定義更新 Table Definition 0194」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は収集でデータ定義対を証跡に残し・後の表定義更新の項目のデータ定義対象表と取得時刻を記録し。
    - B. 保守作業で参照する機能は計画で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - C. 保守作業で参照する機能はリフレッシュで履歴行を証跡に残し・CDC Replication のスクリプト操作に使うコマン。
    - D. 保守作業で参照する機能は変更で遅延確認を証跡に残し・ミラーリングの項目の遅延確認と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能遅延確・初期ロでDの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・変更）です。照合遅延確・初期ロに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・初期ロです。比較ミラー・変更でA:のTable Definitionは「後の表定義更新の項目のデータ定義対象表と取得」を述べるため、正答側の照合軸はミラー・初期ロ・変更です。運用変更・ミラーでB:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は遅延確・ミラー・変更です。項目ミラー・初期ロでC:の失敗時切り分け 履歴行は「CDC Replication」を述べるため、正答側の照合軸は初期ロ・ミラー・遅延確です。用語遅延確・変更という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・変更です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0097**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0097について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE097
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0097A
    ```

    画面・出力には IIDR114DD0097A が表示され、CDCミラーリング Latency 0097 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE097
    Mirroring request accepted
    確認コード IIDR114DD0097B
    ```

    画面・出力には IIDR114DD0097B が表示され、CDCミラーリング Latency 0097 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0097C
    ```

    画面・出力には IIDR114DD0097C が表示され、CDCミラーリング Latency 0097 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0097A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0097B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0097C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0112 {#c11-i0382}
*分類: ミラーリング*  ・  難易度: 上級

桃M移行0113ではIBM IIDR 11.4 の ミラーリングを扱う採取票桃M移行0113です。桃M移行0113は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録桃M移行0113です。桃M移行0113では遅延確認と取得時刻を採取票桃M移行0113へ残します。桃M移行0113では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断桃M移行0113です。桃M移行0113の用語整理では複製ミラーリングの対象値を実在出力で区別する記録桃M移行0113です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0112を同一分類の複製位置管理 Bookmark 0144と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はBookmarkの複製位置と取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。
    - B. 管理対象との関係を表す説明は後の表定義更新の項目の表定義再読込と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。
    - C. 管理対象との関係を表す説明はミラーリングの項目の遅延確認と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。 ✅
    - D. 管理対象との関係を表す説明は対象表を初期同期または再同期する複製操作をマッピング検査として確認する。リフレッシュで管理レポートを確認するときは管理レポートの誤読を防ぐ。refresh マッピング検査 管理レポート固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能遅延確・対象サでCの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・移行）です。照合遅延確・対象サに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・対象サです。比較ミラー・移行でA:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・対象サ・移行です。運用移行・ミラーでB:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は遅延確・ミラー・移行です。仕様ミラー・遅延確でD:のマッピング検査 管理レポートは「対象表を初期同期または再同期する複製操作をマ」を述べるため、正答側の照合軸は移行・対象サ・遅延確です。用語遅延確・移行という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・移行です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0112**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0112について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE112
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0112A
    ```

    画面・出力には IIDR114DD0112A が表示され、CDCミラーリング Latency 0112 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE112
    Mirroring request accepted
    確認コード IIDR114DD0112B
    ```

    画面・出力には IIDR114DD0112B が表示され、CDCミラーリング Latency 0112 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0112C
    ```

    画面・出力には IIDR114DD0112C が表示され、CDCミラーリング Latency 0112 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0112A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0112B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0112C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0127 {#c11-i0383}
*分類: ミラーリング*  ・  難易度: 初級

茶H診断0128ではIBM IIDR 11.4 の ミラーリングを扱う採取票茶H診断0128です。茶H診断0128は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録茶H診断0128です。茶H診断0128では遅延確認と取得時刻を採取票茶H診断0128へ残します。茶H診断0128ではイベント重大度の誤読を避けるため補助資料も照合する判断茶H診断0128です。茶H診断0128の用語整理では複製ミラーリングの対象値を実在出力で評価する記録茶H診断0128です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0127の設定や表示を読む前に役割を確認します。DDL後の表定義更新 Refresh Table 0158ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは後の表定義更新の項目の再開条件と取得時刻を記録し・表定義未更新を防ぐである。点検操作で判定欄を記録するときは表定義未更新を防ぐ。
    - B. 対象資源に対する働きはミラーリングの項目の遅延確認と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。 ✅
    - C. 対象資源に対する働きはSubscriptionの16進ブックマークと取得時刻を記録し・重複反映を防ぐである。変更確認操作で採取欄を棚卸するときは重複反映を防ぐ。複製位置管理 Subscription 0330固有の属性も確認対象に含める。
    - D. 対象資源に対する働きはソース変更を読み取りサブスクリプションへ渡す処理をマッピング検査として確認する。エラー処理で接続認証を確認するときは接続認証の誤読を防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能遅延確・イベンでBの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・診断）です。照合遅延確・イベンに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・イベンです。比較ミラー・診断でA:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸はミラー・イベン・診断です。項目ミラー・イベンでC:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸はイベン・ミラー・遅延確です。仕様ミラー・遅延確でD:のマッピング検査 接続認証は「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸は診断・イベン・遅延確です。用語遅延確・診断という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・診断です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0127**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0127について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE007
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0127A
    ```

    画面・出力には IIDR114DD0127A が表示され、CDCミラーリング Latency 0127 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE007
    Mirroring request accepted
    確認コード IIDR114DD0127B
    ```

    画面・出力には IIDR114DD0127B が表示され、CDCミラーリング Latency 0127 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0127C
    ```

    画面・出力には IIDR114DD0127C が表示され、CDCミラーリング Latency 0127 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0127A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0127B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0127C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0142 {#c11-i0384}
*分類: ミラーリング*  ・  難易度: 初級

緑C保守0143ではIBM IIDR 11.4 の ミラーリングを扱う採取票緑C保守0143です。緑C保守0143は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録緑C保守0143です。緑C保守0143では遅延確認と取得時刻を採取票緑C保守0143へ残します。緑C保守0143では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断緑C保守0143です。緑C保守0143の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録緑C保守0143です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0142に関する障害切り分けの前提を確認しています。DDL後の表定義更新 Source Table 0170の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は表定義未更新を避けるため・点検操作で判定欄を記録するして表定義再読込を照合する。
    - B. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するして遅延確認を照合する。 ✅
    - C. 表示や設定で扱う内容は別サブスクリプションを停止またはを避けるため・版数表示からReplicationを読むして版数表示を照合する。
    - D. 表示や設定で扱う内容は詳細タブの誤読を避けるため・統計採取で詳細タブを確認するして詳細タブを照合する。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能遅延確・遅延ゼでBの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・保守）です。照合遅延確・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・遅延ゼです。比較ミラー・保守でA:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・遅延ゼ・保守です。項目ミラー・遅延ゼでC:の復旧後の確認 SUB06は「CDC Subscriptionで版数表示か」を述べるため、正答側の照合軸は遅延ゼ・ミラー・遅延確です。仕様ミラー・遅延確でD:の統計採取 詳細タブは「CDC Replication」を述べるため、正答側の照合軸は保守・遅延ゼ・遅延確です。用語遅延確・保守という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・保守です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0142**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0142について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE022
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0142A
    ```

    画面・出力には IIDR114DD0142A が表示され、CDCミラーリング Latency 0142 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE022
    Mirroring request accepted
    確認コード IIDR114DD0142B
    ```

    画面・出力には IIDR114DD0142B が表示され、CDCミラーリング Latency 0142 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0142C
    ```

    画面・出力には IIDR114DD0142C が表示され、CDCミラーリング Latency 0142 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0142A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0142B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0142C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0157 {#c11-i0385}
*分類: ミラーリング*  ・  難易度: 中級

藤R保守0158ではIBM IIDR 11.4 の ミラーリングを扱う採取票藤R保守0158です。藤R保守0158は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録藤R保守0158です。藤R保守0158では遅延確認と取得時刻を採取票藤R保守0158へ残します。藤R保守0158ではRefresh未完了の見落としを避けるため補助資料も照合する判断藤R保守0158です。藤R保守0158の用語整理では複製ミラーリングの対象値を実在出力で比較する記録藤R保守0158です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0157を保守記録に説明する必要があります。複製位置管理 Subscription 0240と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はミラーリングの項目の遅延確認と取得時刻を記録し・初期ロード未完了の見落としを防ぐである。記録操作で証跡欄を照合するときは初期ロード未完了の見落としを防ぐ。 ✅
    - B. 保守作業で参照する機能はSubscriptionの16進ブックマークと取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。
    - C. 保守作業で参照する機能はCDC Datastoreで通信活動からCHC9788Iを読み・CHC9788Iとcommunicationである。通信活動からCHC9788Iを読むときはホスト名変更後の購読構成を更を防ぐ。
    - D. 保守作業で参照する機能はミラーリングの項目のミラー開始と取得時刻を記録し・遅延ゼロ確認の欠落を防ぐである。確認操作で状態欄を整理するときは遅延ゼロ確認の欠落を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能遅延確・初期ロでAの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・保守）です。照合遅延確・初期ロに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・初期ロです。運用保守・ミラーでB:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸は遅延確・ミラー・保守です。項目ミラー・初期ロでC:の停止前の確認 STORE14は「CDC Datastoreで通信活動からCH」を述べるため、正答側の照合軸は初期ロ・ミラー・遅延確です。仕様ミラー・遅延確でD:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸は保守・初期ロ・遅延確です。用語遅延確・保守という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・保守です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0157**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0157について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE037
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0157A
    ```

    画面・出力には IIDR114DD0157A が表示され、CDCミラーリング Latency 0157 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE037
    Mirroring request accepted
    確認コード IIDR114DD0157B
    ```

    画面・出力には IIDR114DD0157B が表示され、CDCミラーリング Latency 0157 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0157C
    ```

    画面・出力には IIDR114DD0157C が表示され、CDCミラーリング Latency 0157 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0157A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0157B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0157C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0172 {#c11-i0386}
*分類: ミラーリング*  ・  難易度: 中級

桃M切替0173ではIBM IIDR 11.4 の ミラーリングを扱う採取票桃M切替0173です。桃M切替0173は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録桃M切替0173です。桃M切替0173では遅延確認と取得時刻を採取票桃M切替0173へ残します。桃M切替0173では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断桃M切替0173です。桃M切替0173の用語整理では複製ミラーリングの対象値を実在出力で区別する記録桃M切替0173です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0172の技術的な意味を資料で確認するとき、DDL後の表定義更新 Subscription 0242との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は対象サブスクリプションの取り違えを避けるため・保守操作で監査欄を保存するして遅延確認を照合する。 ✅
    - B. 管理対象との関係を表す説明は表定義未更新を避けるため・点検操作で判定欄を記録するしてログ先頭到達を照合する。
    - C. 管理対象との関係を表す説明はホスト名変更後の購読構成を更新せを避けるため・イベント確認からcommunicatioしてイベント確認を照合する。
    - D. 管理対象との関係を表す説明はデータ欠落を避けるため・監査操作で記録欄を比較するして16進ブックを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能遅延確・対象サでAの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・切替）です。照合遅延確・対象サに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・対象サです。運用切替・ミラーでB:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は遅延確・ミラー・切替です。項目ミラー・対象サでC:の引継ぎ記録 STORE09は「CDC Datastoreでイベント確認から」を述べるため、正答側の照合軸は対象サ・ミラー・遅延確です。仕様ミラー・遅延確でD:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸は切替・対象サ・遅延確です。用語遅延確・切替という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・切替です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0172**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0172について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE052
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0172A
    ```

    画面・出力には IIDR114DD0172A が表示され、CDCミラーリング Latency 0172 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE052
    Mirroring request accepted
    確認コード IIDR114DD0172B
    ```

    画面・出力には IIDR114DD0172B が表示され、CDCミラーリング Latency 0172 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0172C
    ```

    画面・出力には IIDR114DD0172C が表示され、CDCミラーリング Latency 0172 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0172A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0172B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0172C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0187 {#c11-i0387}
*分類: ミラーリング*  ・  難易度: 中級

茶H収集0188ではIBM IIDR 11.4 の ミラーリングを扱う採取票茶H収集0188です。茶H収集0188は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録茶H収集0188です。茶H収集0188では遅延確認と取得時刻を採取票茶H収集0188へ残します。茶H収集0188ではイベント重大度の誤読を避けるため補助資料も照合する判断茶H収集0188です。茶H収集0188の用語整理では複製ミラーリングの対象値を実在出力で評価する記録茶H収集0188です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0187について構成や状態を確認します。複製位置管理 Instance 0228ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは確認で戻り値を証跡に残し・Instanceの戻り値と取得時刻を記録し。
    - B. 対象資源に対する働きは収集で遅延確認を証跡に残し・ミラーリングの項目の遅延確認と取得時刻を記録し。 ✅
    - C. 対象資源に対する働きは再始動確認でイベント確認を証跡に残し・CDC Datastoreでイベント確認からcommunic。
    - D. 対象資源に対する働きは変更でミラー開始を証跡に残し・ミラーリングの項目のミラー開始と取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能遅延確・イベンでBの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・収集）です。照合遅延確・イベンに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・イベンです。比較ミラー・収集でA:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・イベン・収集です。項目ミラー・イベンでC:の再始動後の確認 STORE15は「CDC Datastoreでイベント確認から」を述べるため、正答側の照合軸はイベン・ミラー・遅延確です。仕様ミラー・遅延確でD:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸は収集・イベン・遅延確です。用語遅延確・収集という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・収集です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0187**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0187について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE067
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0187A
    ```

    画面・出力には IIDR114DD0187A が表示され、CDCミラーリング Latency 0187 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE067
    Mirroring request accepted
    確認コード IIDR114DD0187B
    ```

    画面・出力には IIDR114DD0187B が表示され、CDCミラーリング Latency 0187 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0187C
    ```

    画面・出力には IIDR114DD0187C が表示され、CDCミラーリング Latency 0187 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0187A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0187B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0187C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0202 {#c11-i0388}
*分類: ミラーリング*  ・  難易度: 中級

緑C登録0203ではIBM IIDR 11.4 の ミラーリングを扱う採取票緑C登録0203です。緑C登録0203は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録緑C登録0203です。緑C登録0203では遅延確認と取得時刻を採取票緑C登録0203へ残します。緑C登録0203では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断緑C登録0203です。緑C登録0203の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録緑C登録0203です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0202の役割を調べています。DDL後の表定義更新 Source Table 0290の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は抑止で表定義再読込を証跡に残し・後の表定義更新の項目の表定義再読込と取得時刻を記録し。
    - B. 表示や設定で扱う内容は復旧準備でイベント表示を証跡に残し・Mirror Statusでイベント表示からheadoflo。
    - C. 表示や設定で扱う内容は変更でインスタンスを証跡に残し・Hex Positionのインスタンス名と取得時刻を記録し。
    - D. 表示や設定で扱う内容は登録で遅延確認を証跡に残し・ミラーリングの項目の遅延確認と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能遅延確・遅延ゼでDの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・登録）です。照合遅延確・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・遅延ゼです。比較ミラー・登録でA:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸はミラー・遅延ゼ・登録です。運用登録・ミラーでB:の復旧準備 MIR05は「Mirror Statusでイベント表示から」を述べるため、正答側の照合軸は遅延確・ミラー・登録です。項目ミラー・遅延ゼでC:のHex Positionは「Hex Positionのインスタンス名と取」を述べるため、正答側の照合軸は遅延ゼ・ミラー・遅延確です。用語遅延確・登録という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・登録です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0202**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0202について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE082
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0202A
    ```

    画面・出力には IIDR114DD0202A が表示され、CDCミラーリング Latency 0202 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE082
    Mirroring request accepted
    確認コード IIDR114DD0202B
    ```

    画面・出力には IIDR114DD0202B が表示され、CDCミラーリング Latency 0202 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0202C
    ```

    画面・出力には IIDR114DD0202C が表示され、CDCミラーリング Latency 0202 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0202A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0202B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0202C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0217 {#c11-i0389}
*分類: ミラーリング*  ・  難易度: 中級

藤R登録0218ではIBM IIDR 11.4 の ミラーリングを扱う採取票藤R登録0218です。藤R登録0218は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録藤R登録0218です。藤R登録0218では遅延確認と取得時刻を採取票藤R登録0218へ残します。藤R登録0218ではRefresh未完了の見落としを避けるため補助資料も照合する判断藤R登録0218です。藤R登録0218の用語整理では複製ミラーリングの対象値を実在出力で比較する記録藤R登録0218です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Latency 0217」を「CDCミラーリング Replication Method 0268」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はミラーリングの項目の遅延確認と取得時刻を記録し・初期ロード未完了の見落としを防ぐである。記録操作で証跡欄を照合するときは初期ロード未完了の見落としを防ぐ。 ✅
    - B. 保守作業で参照する機能はミラーリングの項目のサブスクリプション状態と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。
    - C. 保守作業で参照する機能はMirror Statusでイベント表示からheadoflogを読みである。イベント表示からheadoflogをときは初期ロード中の表をMirroを防ぐ。
    - D. 保守作業で参照する機能は後の表定義更新の項目のサブスクリプション記述と取得時刻を記録し・データ定義対象表の漏れを防ぐである。復旧操作で点検欄を確認するときはデータ定義対象表の漏れを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能遅延確・初期ロでAの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・登録）です。照合遅延確・初期ロに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・初期ロです。運用登録・ミラーでB:のReplicationは「ミラーリングの項目のサブスクリプション状態と」を述べるため、正答側の照合軸は遅延確・ミラー・登録です。項目ミラー・初期ロでC:の構成監査 MIR08は「Mirror Statusでイベント表示から」を述べるため、正答側の照合軸は初期ロ・ミラー・遅延確です。仕様ミラー・遅延確でD:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は登録・初期ロ・遅延確です。用語遅延確・登録という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・登録です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0217**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0217について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE097
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0217A
    ```

    画面・出力には IIDR114DD0217A が表示され、CDCミラーリング Latency 0217 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE097
    Mirroring request accepted
    確認コード IIDR114DD0217B
    ```

    画面・出力には IIDR114DD0217B が表示され、CDCミラーリング Latency 0217 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0217C
    ```

    画面・出力には IIDR114DD0217C が表示され、CDCミラーリング Latency 0217 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0217A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0217B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0217C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0232 {#c11-i0390}
*分類: ミラーリング*  ・  難易度: 上級

桃M確認0233ではIBM IIDR 11.4 の ミラーリングを扱う採取票桃M確認0233です。桃M確認0233は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録桃M確認0233です。桃M確認0233では遅延確認と取得時刻を採取票桃M確認0233へ残します。桃M確認0233では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断桃M確認0233です。桃M確認0233の用語整理では複製ミラーリングの対象値を実在出力で区別する記録桃M確認0233です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0232を同一分類の複製位置管理 Locale 0327と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はLocaleのサブスクリプション名と取得時刻を記録し・データ欠落を防ぐである。監査操作で記録欄を比較するときはデータ欠落を防ぐ。複製位置管理 Locale 0327固有の属性も確認対象に含める。
    - B. 管理対象との関係を表す説明はミラーリングの項目の遅延確認と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。 ✅
    - C. 管理対象との関係を表す説明はLog Dependencyで購読確認からInactiveを読みである。購読確認からInactiveを読むときは休止購読を見落として必要ログを防ぐ。
    - D. 管理対象との関係を表す説明は後の表定義更新の項目の表定義再読込と取得時刻を記録し・ログ先頭未到達の見落としを防ぐである。調査操作で保守欄を引き継ぎするときはログ先頭未到達の見落としを防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能遅延確・対象サでBの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・確認）です。照合遅延確・対象サに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・対象サです。比較ミラー・確認でA:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸はミラー・対象サ・確認です。項目ミラー・対象サでC:の復旧準備 LOG05は「Log Dependencyで購読確認からI」を述べるため、正答側の照合軸は対象サ・ミラー・遅延確です。仕様ミラー・遅延確でD:のSource Tableは「後の表定義更新の項目の表定義再読込と取得時刻」を述べるため、正答側の照合軸は確認・対象サ・遅延確です。用語遅延確・確認という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・確認です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0232**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0232について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE112
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0232A
    ```

    画面・出力には IIDR114DD0232A が表示され、CDCミラーリング Latency 0232 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE112
    Mirroring request accepted
    確認コード IIDR114DD0232B
    ```

    画面・出力には IIDR114DD0232B が表示され、CDCミラーリング Latency 0232 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0232C
    ```

    画面・出力には IIDR114DD0232C が表示され、CDCミラーリング Latency 0232 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0232A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0232B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0232C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0247 {#c11-i0391}
*分類: ミラーリング*  ・  難易度: 初級

茶H保護0248ではIBM IIDR 11.4 の ミラーリングを扱う採取票茶H保護0248です。茶H保護0248は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録茶H保護0248です。茶H保護0248では遅延確認と取得時刻を採取票茶H保護0248へ残します。茶H保護0248ではイベント重大度の誤読を避けるため補助資料も照合する判断茶H保護0248です。茶H保護0248の用語整理では複製ミラーリングの対象値を実在出力で評価する記録茶H保護0248です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0247の設定や表示を読む前に役割を確認します。複製位置管理 Instance 0318ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは変更確認操作で採取欄を棚卸することで戻り値を確認し・重複反映を防ぐ。
    - B. 対象資源に対する働きはログ依存からOldestdependenことでログ依存を確認し・送信回数だけでターゲット適用を防ぐ。
    - C. 対象資源に対する働きは採取操作で照合欄を点検することで遅延確認を確認し・イベント重大度の誤読を防ぐ。 ✅
    - D. 対象資源に対する働きは保守操作で監査欄を保存することで初期ロード状を確認し・対象サブスクリプションの取りを防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能遅延確・イベンでCの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・保護）です。照合遅延確・イベンに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・イベンです。比較ミラー・保護でA:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸はミラー・イベン・保護です。運用保護・ミラーでB:の権限境界の確認 STAT12は「CDC Communicationsでログ依」を述べるため、正答側の照合軸は遅延確・ミラー・保護です。仕様ミラー・遅延確でD:のTable Statusは「ミラーリングの項目の初期ロード状態と取得時刻」を述べるため、正答側の照合軸は保護・イベン・遅延確です。用語遅延確・保護という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・保護です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0247**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0247について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE007
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0247A
    ```

    画面・出力には IIDR114DD0247A が表示され、CDCミラーリング Latency 0247 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE007
    Mirroring request accepted
    確認コード IIDR114DD0247B
    ```

    画面・出力には IIDR114DD0247B が表示され、CDCミラーリング Latency 0247 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0247C
    ```

    画面・出力には IIDR114DD0247C が表示され、CDCミラーリング Latency 0247 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0247A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0247B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0247C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0262 {#c11-i0392}
*分類: ミラーリング*  ・  難易度: 初級

緑C照合0263ではIBM IIDR 11.4 の ミラーリングを扱う採取票緑C照合0263です。緑C照合0263は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録緑C照合0263です。緑C照合0263では遅延確認と取得時刻を採取票緑C照合0263へ残します。緑C照合0263では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断緑C照合0263です。緑C照合0263の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録緑C照合0263です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0262に関する障害切り分けの前提を確認しています。DDL後の表定義更新 Head of Log 0356の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするしてサブスクリプを照合する。
    - B. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するして遅延確認を照合する。 ✅
    - C. 表示や設定で扱う内容は接続認証の誤読を避けるため・エラー処理で接続認証を確認するして接続認証を照合する。
    - D. 表示や設定で扱う内容はデータ定義対象表の漏れを避けるため・復旧操作で点検欄を確認するして再開条件を照合する。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能遅延確・遅延ゼでBの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・照合）です。照合遅延確・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・遅延ゼです。比較ミラー・照合でA:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はミラー・遅延ゼ・照合です。項目ミラー・遅延ゼでC:のマッピング検査 接続認証は「ソース変更を読み取りサブスクリプションへ渡す」を述べるため、正答側の照合軸は遅延ゼ・ミラー・遅延確です。仕様ミラー・遅延確でD:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は照合・遅延ゼ・遅延確です。用語遅延確・照合という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延ゼ・照合です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0262**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0262について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE022
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0262A
    ```

    画面・出力には IIDR114DD0262A が表示され、CDCミラーリング Latency 0262 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE022
    Mirroring request accepted
    確認コード IIDR114DD0262B
    ```

    画面・出力には IIDR114DD0262B が表示され、CDCミラーリング Latency 0262 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0262C
    ```

    画面・出力には IIDR114DD0262C が表示され、CDCミラーリング Latency 0262 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0262A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0262B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0262C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0277 {#c11-i0393}
*分類: ミラーリング*  ・  難易度: 中級

藤R照合0278ではIBM IIDR 11.4 の ミラーリングを扱う採取票藤R照合0278です。藤R照合0278は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録藤R照合0278です。藤R照合0278では遅延確認と取得時刻を採取票藤R照合0278へ残します。藤R照合0278ではRefresh未完了の見落としを避けるため補助資料も照合する判断藤R照合0278です。藤R照合0278の用語整理では複製ミラーリングの対象値を実在出力で比較する記録藤R照合0278です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0277を保守記録に説明する必要があります。DDL後の表定義更新 Refresh Table 0338と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は点検操作で判定欄を記録することで再開条件を確認し・表定義未更新を防ぐ。
    - B. 保守作業で参照する機能は記録操作で証跡欄を照合することで遅延確認を確認し・初期ロード未完了の見落としを防ぐ。 ✅
    - C. 保守作業で参照する機能はサポート収集からSupportを読むことでサポート収集を確認し・情報イベントと停止を伴うエラを防ぐ。
    - D. 保守作業で参照する機能は点検操作で判定欄を記録することでログ先頭到達を確認し・表定義未更新を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能遅延確・初期ロでBの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・照合）です。照合遅延確・初期ロに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・初期ロです。比較ミラー・照合でA:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸はミラー・初期ロ・照合です。項目ミラー・初期ロでC:の再始動後の確認 ERR15は「CDC Event Logでサポート収集から」を述べるため、正答側の照合軸は初期ロ・ミラー・遅延確です。仕様ミラー・遅延確でD:のDDL後の表定義更新は「後の表定義更新の項目のログ先頭到達と取得時刻」を述べるため、正答側の照合軸は照合・初期ロ・遅延確です。用語遅延確・照合という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・初期ロ・照合です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0277**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0277について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE037
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0277A
    ```

    画面・出力には IIDR114DD0277A が表示され、CDCミラーリング Latency 0277 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE037
    Mirroring request accepted
    確認コード IIDR114DD0277B
    ```

    画面・出力には IIDR114DD0277B が表示され、CDCミラーリング Latency 0277 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0277C
    ```

    画面・出力には IIDR114DD0277C が表示され、CDCミラーリング Latency 0277 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0277A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0277B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0277C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0292 {#c11-i0394}
*分類: ミラーリング*  ・  難易度: 中級

桃M抑止0293ではIBM IIDR 11.4 の ミラーリングを扱う採取票桃M抑止0293です。桃M抑止0293は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録桃M抑止0293です。桃M抑止0293では遅延確認と取得時刻を採取票桃M抑止0293へ残します。桃M抑止0293では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断桃M抑止0293です。桃M抑止0293の用語整理では複製ミラーリングの対象値を実在出力で区別する記録桃M抑止0293です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0292の技術的な意味を資料で確認するとき、CDCミラーリング Event Severity 0319との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はミラーリングの項目の遅延確認と取得時刻を記録し・対象サブスクリプションの取り違えを防ぐである。保守操作で監査欄を保存するときは対象サブスクリプションの取りを防ぐ。 ✅
    - B. 管理対象との関係を表す説明はミラーリングの項目のミラー開始と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。
    - C. 管理対象との関係を表す説明はLocaleのサブスクリプション名と取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。
    - D. 管理対象との関係を表す説明はInstanceの戻り値と取得時刻を記録し・重複反映を防ぐである。変更確認操作で採取欄を棚卸するときは重複反映を防ぐ。複製位置管理 Instance 0138固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能遅延確・対象サでAの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・抑止）です。照合遅延確・対象サに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・対象サです。運用抑止・ミラーでB:のEvent Severityは「ミラーリングの項目のミラー開始と取得時刻を記」を述べるため、正答側の照合軸は遅延確・ミラー・抑止です。項目ミラー・対象サでC:の複製位置管理 Localeは「Localeのサブスクリプション名と取得時刻」を述べるため、正答側の照合軸は対象サ・ミラー・遅延確です。仕様ミラー・遅延確でD:の複製位置管理 Instanceは「Instanceの戻り値と取得時刻を記録し」を述べるため、正答側の照合軸は抑止・対象サ・遅延確です。用語遅延確・抑止という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・対象サ・抑止です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0292**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0292について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE052
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0292A
    ```

    画面・出力には IIDR114DD0292A が表示され、CDCミラーリング Latency 0292 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE052
    Mirroring request accepted
    確認コード IIDR114DD0292B
    ```

    画面・出力には IIDR114DD0292B が表示され、CDCミラーリング Latency 0292 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0292C
    ```

    画面・出力には IIDR114DD0292C が表示され、CDCミラーリング Latency 0292 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0292A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0292B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0292C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0307 {#c11-i0395}
*分類: ミラーリング*  ・  難易度: 中級

茶H解析0308ではIBM IIDR 11.4 の ミラーリングを扱う採取票茶H解析0308です。茶H解析0308は複製ミラーリングの採取操作で複製ミラーリングの照合欄を点検する記録茶H解析0308です。茶H解析0308では遅延確認と取得時刻を採取票茶H解析0308へ残します。茶H解析0308ではイベント重大度の誤読を避けるため補助資料も照合する判断茶H解析0308です。茶H解析0308の用語整理では複製ミラーリングの対象値を実在出力で評価する記録茶H解析0308です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0307について構成や状態を確認します。サブスクリプション管理 CDC Subscription 停止前の確認 SUB14ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはミラーリングの項目の遅延確認と取得時刻を記録し・イベント重大度の誤読を防ぐである。採取操作で照合欄を点検するときはイベント重大度の誤読を防ぐ。 ✅
    - B. 対象資源に対する働きはCDC Subscriptionでイベント表示からSeverityを読みである。イベント表示からSeverityを読ときは別サブスクリプションを停止まを防ぐ。
    - C. 対象資源に対する働きは後の表定義更新の項目のサブスクリプション記述と取得時刻を記録し・初期ロード中の再開を防ぐである。表示操作で対象欄を追跡するときは初期ロード中の再開を防ぐ。
    - D. 対象資源に対する働きはBookmarkの複製位置と取得時刻を記録し・対象インスタンスの取り違えを防ぐである。照合操作で確認欄を採取するときは対象インスタンスの取り違えを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能遅延確・イベンでAの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・解析）です。照合遅延確・イベンに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象はミラー・遅延確・イベンです。運用解析・ミラーでB:の停止前の確認 SUB14は「CDC Subscriptionでイベント表」を述べるため、正答側の照合軸は遅延確・ミラー・解析です。項目ミラー・イベンでC:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸はイベン・ミラー・遅延確です。仕様ミラー・遅延確でD:の複製位置管理 Bookmarkは「Bookmarkの複製位置と取得時刻を記録し」を述べるため、正答側の照合軸は解析・イベン・遅延確です。用語遅延確・解析という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・イベン・解析です。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0307**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0307について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE067
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0307A
    ```

    画面・出力には IIDR114DD0307A が表示され、CDCミラーリング Latency 0307 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC03
    Subscription FINANCE067
    Mirroring request accepted
    確認コード IIDR114DD0307B
    ```

    画面・出力には IIDR114DD0307B が表示され、CDCミラーリング Latency 0307 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0307C
    ```

    画面・出力には IIDR114DD0307C が表示され、CDCミラーリング Latency 0307 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0307A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0307B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0307C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0322 {#c11-i0396}
*分類: ミラーリング*  ・  難易度: 中級

緑C計画0323ではIBM IIDR 11.4 の ミラーリングを扱う採取票緑C計画0323です。緑C計画0323は複製ミラーリングの確認操作で複製ミラーリングの状態欄を整理する記録緑C計画0323です。緑C計画0323では遅延確認と取得時刻を採取票緑C計画0323へ残します。緑C計画0323では遅延ゼロ確認の欠落を避けるため補助資料も照合する判断緑C計画0323です。緑C計画0323の用語整理では複製ミラーリングの対象値を実在出力で読み分けする記録緑C計画0323です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0322の役割を調べています。データストア接続 CDC Datastore 構成監査 STORE08の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は遅延ゼロ確認の欠落を避けるため・確認操作で状態欄を整理するして遅延確認を照合する。 ✅
    - B. 表示や設定で扱う内容はホスト名変更後の購読構成を更新せを避けるため・通信活動からCHC9788Iを読むして通信活動を照合する。
    - C. 表示や設定で扱う内容はログ先頭未到達の見落としを避けるため・調査操作で保守欄を引き継ぎするして再開条件を照合する。
    - D. 表示や設定で扱う内容はデータ欠落を避けるため・監査操作で記録欄を比較するして16進ブックを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能遅延確・遅延ゼでAの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・計画）です。照合遅延確・遅延ゼに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象は遅延確・計画・遅延ゼです。運用計画・ミラーでB:の構成監査 STORE08は「CDC Datastoreで通信活動からCH」を述べるため、正答側の照合軸は遅延確・ミラー・計画です。項目ミラー・遅延ゼでC:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は遅延ゼ・ミラー・遅延確です。仕様ミラー・遅延確でD:の複製位置管理 Subscriptは「Subscriptionの16進ブックマーク」を述べるため、正答側の照合軸は計画・遅延ゼ・遅延確です。用語遅延確・計画という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延確・遅延ゼです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0322**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0322について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE082
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 1
    確認コード IIDR114DD0322A
    ```

    画面・出力には IIDR114DD0322A が表示され、CDCミラーリング Latency 0322 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC02
    Subscription FINANCE082
    Mirroring request accepted
    確認コード IIDR114DD0322B
    ```

    画面・出力には IIDR114DD0322B が表示され、CDCミラーリング Latency 0322 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0322C
    ```

    画面・出力には IIDR114DD0322C が表示され、CDCミラーリング Latency 0322 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0322A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0322B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0322C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0337 {#c11-i0397}
*分類: ミラーリング*  ・  難易度: 中級

藤R計画0338ではIBM IIDR 11.4 の ミラーリングを扱う採取票藤R計画0338です。藤R計画0338は複製ミラーリングの記録操作で複製ミラーリングの証跡欄を照合する記録藤R計画0338です。藤R計画0338では遅延確認と取得時刻を採取票藤R計画0338へ残します。藤R計画0338ではRefresh未完了の見落としを避けるため補助資料も照合する判断藤R計画0338です。藤R計画0338の用語整理では複製ミラーリングの対象値を実在出力で比較する記録藤R計画0338です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** 「CDCミラーリング Latency 0337」を「データストア接続 CDC Datastore 障害切り分け STORE04」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は接続表示からDatastoreを読むことで接続表示を確認し・ホスト名変更後の購読構成を更を防ぐ。
    - B. 保守作業で参照する機能は調査操作で保守欄を引き継ぎすることで再開条件を確認し・ログ先頭未到達の見落としを防ぐ。
    - C. 保守作業で参照する機能は記録操作で証跡欄を照合することで初期ロード状を確認し・初期ロード未完了の見落としを防ぐ。
    - D. 保守作業で参照する機能は記録操作で証跡欄を照合することで遅延確認を確認し・初期ロード未完了の見落としを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能遅延確・初期ロでDの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・計画）です。照合遅延確・初期ロに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象は遅延確・計画・初期ロです。比較ミラー・計画でA:の障害切り分け STORE04は「CDC Datastoreで接続表示からDa」を述べるため、正答側の照合軸はミラー・計画・遅延確です。運用計画・ミラーでB:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は遅延確・ミラー・計画です。項目ミラー・初期ロでC:のTable Statusは「ミラーリングの項目の初期ロード状態と取得時刻」を述べるため、正答側の照合軸は初期ロ・ミラー・遅延確です。用語遅延確・計画という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延確・初期ロです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0337**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0337について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE097
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 7
    確認コード IIDR114DD0337A
    ```

    画面・出力には IIDR114DD0337A が表示され、CDCミラーリング Latency 0337 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC01
    Subscription FINANCE097
    Mirroring request accepted
    確認コード IIDR114DD0337B
    ```

    画面・出力には IIDR114DD0337B が表示され、CDCミラーリング Latency 0337 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0337C
    ```

    画面・出力には IIDR114DD0337C が表示され、CDCミラーリング Latency 0337 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0337A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0337B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0337C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



### CDCミラーリング Latency 0352 {#c11-i0398}
*分類: ミラーリング*  ・  難易度: 上級

桃M解除0353ではIBM IIDR 11.4 の ミラーリングを扱う採取票桃M解除0353です。桃M解除0353は複製ミラーリングの保守操作で複製ミラーリングの監査欄を保存する記録桃M解除0353です。桃M解除0353では遅延確認と取得時刻を採取票桃M解除0353へ残します。桃M解除0353では対象サブスクリプションの取り違えを避けるため補助資料も照合する判断桃M解除0353です。桃M解除0353の用語整理では複製ミラーリングの対象値を実在出力で区別する記録桃M解除0353です。

**出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting

??? question "確認問題（1問）"
    **問題.** CDCミラーリング Latency 0352を同一分類のリフレッシュ制御 CDC Refresh 再始動後の確認 REF15と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は完了確認からRowsappliedを読むことで完了確認を確認し・初期ロード未完了でMirroを防ぐ。
    - B. 管理対象との関係を表す説明は保守操作で監査欄を保存することで遅延確認を確認し・対象サブスクリプションの取りを防ぐ。 ✅
    - C. 管理対象との関係を表す説明は調査操作で保守欄を引き継ぎすることでサブスクリプを確認し・ログ先頭未到達の見落としを防ぐ。
    - D. 管理対象との関係を表す説明は表示操作で対象欄を追跡することで再開条件を確認し・初期ロード中の再開を防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能遅延確・対象サでBの記述「ミラーリングの項目の遅延確認と取得時刻を記録し」に対応する項目はCDCミラーリング Latency（ミラー・遅延確・解除）です。照合遅延確・対象サに関するミラーリングの仕様は「ミラーリングの項目の遅延確認と取得時刻を記録し」で、確認対象は遅延確・解除・対象サです。比較ミラー・解除でA:の再始動後の確認 REF15は「CDC Refreshで完了確認からRows」を述べるため、正答側の照合軸はミラー・解除・遅延確です。項目ミラー・対象サでC:のof Logは「後の表定義更新の項目のサブスクリプション記述」を述べるため、正答側の照合軸は対象サ・ミラー・遅延確です。仕様ミラー・遅延確でD:のRefresh Tableは「後の表定義更新の項目の再開条件と取得時刻を記」を述べるため、正答側の照合軸は解除・対象サ・遅延確です。用語遅延確・解除という用語は「ミラーリングの項目の遅延確認と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはミラー・遅延確・対象サです。

    **出典:** IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting


??? note "検証手順（1件）"
    **CDCミラーリング Latency 0352**

    - 検証目的: CDCミラーリングのCDCミラーリング Latency 0352について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Latency と 遅延確認
    - セッション環境: 机上検証。IBM IIDR 11.4のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmshowevents
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subscription FINANCE112
    Replication Method Mirror
    Table Status Refresh then Active
    Latency seconds 4
    確認コード IIDR114DD0352A
    ```

    画面・出力には IIDR114DD0352A が表示され、CDCミラーリング Latency 0352 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
    操作（入力）:
    ```text
    IBM IIDR 11.4 操作画面またはコマンド環境
    COMMAND ===> dmsupportinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    dmstartmirror instance CDC00
    Subscription FINANCE112
    Mirroring request accepted
    確認コード IIDR114DD0352B
    ```

    画面・出力には IIDR114DD0352B が表示され、CDCミラーリング Latency 0352 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM IIDR 11.4の確認画面またはコマンド結果です。Latency を読むため、CDCミラーリング の対象値を表示します。
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
    確認コード IIDR114DD0352C
    ```

    画面・出力には IIDR114DD0352C が表示され、CDCミラーリング Latency 0352 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の IIDR114DD0352A が画面・出力に表示されること
    ② ステップ2 の IIDR114DD0352B が画面・出力に表示されること
    ③ ステップ3 の IIDR114DD0352C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IIDR_11.4_CDC_Replication_commands / IIDR_11.4_Management_Console / IIDR_11.4_Access_Server / IIDR_11.4_Troubleshooting



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


