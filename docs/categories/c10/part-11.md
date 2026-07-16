---
search:
  exclude: true
---

# IBM Guardium Data Protection 12.x — 詳細 (11/12)

[← IBM Guardium Data Protection 12.x の概要へ戻る](index.md)


## IBM Guardium Data Protection 12.x > レポート

### 監査レポート Server IP 0182 {#c10-i0489}
*分類: レポート*  ・  難易度: 中級

緑C収集0183ではIBM Guardium Data Protection 12.x の レポートを扱う採取票緑C収集0183です。緑C収集0183は監査レポートの点検操作で監査レポートの判定欄を記録する記録緑C収集0183です。緑C収集0183ではデータソースと取得時刻を採取票緑C収集0183へ残します。緑C収集0183ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断緑C収集0183です。緑C収集0183の用語整理では監査レポートの対象値を実在出力で保管する記録緑C収集0183です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0182に関する障害切り分けの前提を確認しています。ロールと権限 Application Access 0270の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては照合でユーザー有効を証跡に残し・Application Accessのユーザー有効化と取得時。
    - B. 機能の説明としては遅延表示で遅延表示を証跡に残し・監査要件に沿ってレポート実行とレビューを束ねる処理を実行結果。
    - C. 機能の説明としては収集でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。 ✅
    - D. 機能の説明としては復旧で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能データ・照会文でCの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・収集）です。照合データ・収集に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・収集・照会文です。比較監査レ・収集でA:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はSer・収集・データです。運用収集・SerでB:の実行結果照合 遅延表示は「監査要件に沿ってレポート実行とレビューを束ね」を述べるため、正答側の照合軸はデータ・監査レ・収集です。仕様データ・収集でD:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸は収集・照会文・データです。用語データ・収集という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0182**

    - 検証目的: 監査レポートの監査レポート Server IP 0182について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.72
    Server IP 198.51.100.22
    Count 72
    確認コード GDP12DD0182A
    ```

    画面・出力には GDP12DD0182A が表示され、監査レポート Server IP 0182 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0182
    Process Type Report
    Status completed
    確認コード GDP12DD0182B
    ```

    画面・出力には GDP12DD0182B が表示され、監査レポート Server IP 0182 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor08
    Action required review
    Task result pending
    確認コード GDP12DD0182C
    ```

    画面・出力には GDP12DD0182C が表示され、監査レポート Server IP 0182 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0182A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0182B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0182C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0197 {#c10-i0490}
*分類: レポート*  ・  難易度: 中級

藤R収集0198ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藤R収集0198です。藤R収集0198は監査レポートの復旧操作で監査レポートの点検欄を確認する記録藤R収集0198です。藤R収集0198ではデータソースと取得時刻を採取票藤R収集0198へ残します。藤R収集0198では監査タスク未レビューを避けるため補助資料も照合する判断藤R収集0198です。藤R収集0198の用語整理では監査レポートの対象値を実在出力で点検する記録藤R収集0198です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0197を保守記録に説明する必要があります。監査レポート SQL Verb 0221と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するしてジョブキューを照合する。
    - B. 運用時に利用する技術的役割は廃止サーバーの参照を残して監査対を避けるため・参照箇所からUsedByを読むして参照箇所を照合する。
    - C. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するしてデータソースを照合する。 ✅
    - D. 運用時に利用する技術的役割は最終応答停止の見落としを避けるため・確認操作で状態欄を整理するして暗号化表示を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能データ・監査タでCの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・収集）です。照合データ・収集に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・収集・監査タです。比較監査レ・収集でA:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はSer・収集・データです。運用収集・SerでB:の世代整合の確認 DSRC17は「Guardiumで参照箇所から」を述べるため、正答側の照合軸はデータ・監査レ・収集です。仕様データ・収集でD:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は収集・監査タ・データです。用語データ・収集という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0197**

    - 検証目的: 監査レポートの監査レポート Server IP 0197について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.87
    Server IP 198.51.100.37
    Count 87
    確認コード GDP12DD0197A
    ```

    画面・出力には GDP12DD0197A が表示され、監査レポート Server IP 0197 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0197
    Process Type Report
    Status completed
    確認コード GDP12DD0197B
    ```

    画面・出力には GDP12DD0197B が表示され、監査レポート Server IP 0197 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor05
    Action required review
    Task result pending
    確認コード GDP12DD0197C
    ```

    画面・出力には GDP12DD0197C が表示され、監査レポート Server IP 0197 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0197A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0197B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0197C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0212 {#c10-i0491}
*分類: レポート*  ・  難易度: 中級

桃M登録0213ではIBM Guardium Data Protection 12.x の レポートを扱う採取票桃M登録0213です。桃M登録0213は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録桃M登録0213です。桃M登録0213ではデータソースと取得時刻を採取票桃M登録0213へ残します。桃M登録0213では対象データソースの取り違えを避けるため補助資料も照合する判断桃M登録0213です。桃M登録0213の用語整理では監査レポートの対象値を実在出力で整理する記録桃M登録0213です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0212の技術的な意味を資料で確認するとき、S-TAP監視 Last Response 0232との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は確認でカーネル監視を証跡に残し・監視エージェントのカーネル監視有無と取得時刻を記録し。
    - B. 構成を確認する際の意味は登録でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。 ✅
    - C. 構成を確認する際の意味は権限境界確認で報告上限を証跡に残し・Audit Processで報告上限から。
    - D. 構成を確認する際の意味は変更でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能データ・対象デでBの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・登録）です。照合データ・登録に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・登録・対象デです。比較監査レ・登録でA:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はSer・登録・データです。項目データ・登録でC:の権限境界の確認 AUDIT12は「Audit Processで報告上限から」を述べるため、正答側の照合軸は対象デ・監査レ・データです。仕様データ・登録でD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は登録・対象デ・データです。用語データ・登録という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0212**

    - 検証目的: 監査レポートの監査レポート Server IP 0212について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.22
    Server IP 198.51.100.52
    Count 102
    確認コード GDP12DD0212A
    ```

    画面・出力には GDP12DD0212A が表示され、監査レポート Server IP 0212 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0212
    Process Type Report
    Status completed
    確認コード GDP12DD0212B
    ```

    画面・出力には GDP12DD0212B が表示され、監査レポート Server IP 0212 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor02
    Action required review
    Task result pending
    確認コード GDP12DD0212C
    ```

    画面・出力には GDP12DD0212C が表示され、監査レポート Server IP 0212 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0212A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0212B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0212C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0227 {#c10-i0492}
*分類: レポート*  ・  難易度: 上級

茶H確認0228ではIBM Guardium Data Protection 12.x の レポートを扱う採取票茶H確認0228です。茶H確認0228は監査レポートの表示操作で監査レポートの対象欄を追跡する記録茶H確認0228です。茶H確認0228ではデータソースと取得時刻を採取票茶H確認0228へ残します。茶H確認0228ではジョブ失敗の見落としを避けるため補助資料も照合する判断茶H確認0228です。茶H確認0228の用語整理では監査レポートの対象値を実在出力で照合する記録茶H確認0228です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0227について構成や状態を確認します。監査レポート SQL Verb 0251ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはServer IPのデータソースと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。 ✅
    - B. 状態を読み取るための働きは照会文 Verbのジョブキューと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。
    - C. 状態を読み取るための働きはCentral Managerで保守後の確認では中央管理サーバーの 例外レポートから Exceptionである。保守確認で保守後の確認を確認するときはmanaged unitからを防ぐ。
    - D. 状態を読み取るための働きはApplication Accessのユーザー有効化と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能データ・ジョブでAの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・確認）です。照合データ・確認に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・確認・ジョブです。運用確認・SerでB:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はデータ・監査レ・確認です。項目データ・確認でC:の保守後の確認 CM20は「Central Managerで保守後の確認」を述べるため、正答側の照合軸はジョブ・監査レ・データです。仕様データ・確認でD:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は確認・ジョブ・データです。用語データ・確認という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0227**

    - 検証目的: 監査レポートの監査レポート Server IP 0227について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.37
    Server IP 198.51.100.67
    Count 117
    確認コード GDP12DD0227A
    ```

    画面・出力には GDP12DD0227A が表示され、監査レポート Server IP 0227 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0227
    Process Type Report
    Status completed
    確認コード GDP12DD0227B
    ```

    画面・出力には GDP12DD0227B が表示され、監査レポート Server IP 0227 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor08
    Action required review
    Task result pending
    確認コード GDP12DD0227C
    ```

    画面・出力には GDP12DD0227C が表示され、監査レポート Server IP 0227 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0227A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0227B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0227C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0242 {#c10-i0493}
*分類: レポート*  ・  難易度: 初級

緑C保護0243ではIBM Guardium Data Protection 12.x の レポートを扱う採取票緑C保護0243です。緑C保護0243は監査レポートの点検操作で監査レポートの判定欄を記録する記録緑C保護0243です。緑C保護0243ではデータソースと取得時刻を採取票緑C保護0243へ残します。緑C保護0243ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断緑C保護0243です。緑C保護0243の用語整理では監査レポートの対象値を実在出力で保管する記録緑C保護0243です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0242の役割を調べています。ロールと権限 Role 0291の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては抑止でディレクトリを証跡に残し・Roleのディレクトリー取込と取得時刻を記録し。
    - B. 機能の説明としては保護でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。 ✅
    - C. 機能の説明としては通常状態確認でデータソースを証跡に残し・Guardiumでデータソース一覧から。
    - D. 機能の説明としては監査で承認クライアを証跡に残し・監視エージェントの承認クライアントと取得時刻を記録し。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能データ・照会文でBの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・保護）です。照合データ・保護に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・保護・照会文です。比較監査レ・保護でA:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸はSer・保護・データです。項目データ・保護でC:の通常状態の確認 DSRC01は「Guardiumでデータソース一覧から」を述べるため、正答側の照合軸は照会文・監査レ・データです。仕様データ・保護でD:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は保護・照会文・データです。用語データ・保護という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0242**

    - 検証目的: 監査レポートの監査レポート Server IP 0242について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.12
    Server IP 198.51.100.22
    Count 12
    確認コード GDP12DD0242A
    ```

    画面・出力には GDP12DD0242A が表示され、監査レポート Server IP 0242 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0242
    Process Type Report
    Status completed
    確認コード GDP12DD0242B
    ```

    画面・出力には GDP12DD0242B が表示され、監査レポート Server IP 0242 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor02
    Action required review
    Task result pending
    確認コード GDP12DD0242C
    ```

    画面・出力には GDP12DD0242C が表示され、監査レポート Server IP 0242 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0242A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0242B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0242C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0257 {#c10-i0494}
*分類: レポート*  ・  難易度: 初級

藤R保護0258ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藤R保護0258です。藤R保護0258は監査レポートの復旧操作で監査レポートの点検欄を確認する記録藤R保護0258です。藤R保護0258ではデータソースと取得時刻を採取票藤R保護0258へ残します。藤R保護0258では監査タスク未レビューを避けるため補助資料も照合する判断藤R保護0258です。藤R保護0258の用語整理では監査レポートの対象値を実在出力で点検する記録藤R保護0258です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート Server IP 0257」を「監査レポート SQL Verb 0266」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は点検操作で判定欄を記録することでジョブキューを確認し・照会文動詞集計の期間誤りを防ぐ。
    - B. 運用時に利用する技術的役割は復旧操作で点検欄を確認することでデータソースを確認し・監査タスク未レビューを防ぐ。 ✅
    - C. 運用時に利用する技術的役割はDB処理一覧からTURBINEを読むことでデータベースを確認し・ディスク逼迫中に検査データ流を防ぐ。
    - D. 運用時に利用する技術的役割は変更確認操作で採取欄を棚卸することでGuardAを確認し・ディレクトリー取込対象の誤りを防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能データ・監査タでBの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・保護）です。照合データ・保護に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・保護・監査タです。比較監査レ・保護でA:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はSer・保護・データです。項目データ・保護でC:の復旧準備 APP05は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸は監査タ・監査レ・データです。仕様データ・保護でD:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は保護・監査タ・データです。用語データ・保護という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0257**

    - 検証目的: 監査レポートの監査レポート Server IP 0257について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.27
    Server IP 198.51.100.37
    Count 27
    確認コード GDP12DD0257A
    ```

    画面・出力には GDP12DD0257A が表示され、監査レポート Server IP 0257 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0257
    Process Type Report
    Status completed
    確認コード GDP12DD0257B
    ```

    画面・出力には GDP12DD0257B が表示され、監査レポート Server IP 0257 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor08
    Action required review
    Task result pending
    確認コード GDP12DD0257C
    ```

    画面・出力には GDP12DD0257C が表示され、監査レポート Server IP 0257 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0257A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0257B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0257C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0272 {#c10-i0495}
*分類: レポート*  ・  難易度: 中級

桃M照合0273ではIBM Guardium Data Protection 12.x の レポートを扱う採取票桃M照合0273です。桃M照合0273は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録桃M照合0273です。桃M照合0273ではデータソースと取得時刻を採取票桃M照合0273へ残します。桃M照合0273では対象データソースの取り違えを避けるため補助資料も照合する判断桃M照合0273です。桃M照合0273の用語整理では監査レポートの対象値を実在出力で整理する記録桃M照合0273です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0272を同一分類のS-TAP監視 KTAP Installed 0289と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は調査操作で保守欄を引き継ぎすることでデータソースを確認し・対象データソースの取り違えを防ぐ。 ✅
    - B. 構成を確認する際の意味は記録操作で証跡欄を照合することで監視エージェを確認し・未承認監視エージェント接続を防ぐ。
    - C. 構成を確認する際の意味は依存関係確認で確認では中央を確認することで確認では中央を確認し・managed unitからを防ぐ。
    - D. 構成を確認する際の意味は調査操作で保守欄を引き継ぎすることで照会文動詞集を確認し・対象データソースの取り違えを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能データ・対象デでAの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・照合）です。照合データ・照合に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・照合・対象デです。運用照合・SerでB:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はデータ・監査レ・照合です。項目データ・照合でC:の依存関係の確認 CM13は「Central Managerで依存関係の確」を述べるため、正答側の照合軸は対象デ・監査レ・データです。仕様データ・照合でD:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は照合・対象デ・データです。用語データ・照合という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0272**

    - 検証目的: 監査レポートの監査レポート Server IP 0272について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.42
    Server IP 198.51.100.52
    Count 42
    確認コード GDP12DD0272A
    ```

    画面・出力には GDP12DD0272A が表示され、監査レポート Server IP 0272 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0272
    Process Type Report
    Status completed
    確認コード GDP12DD0272B
    ```

    画面・出力には GDP12DD0272B が表示され、監査レポート Server IP 0272 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor05
    Action required review
    Task result pending
    確認コード GDP12DD0272C
    ```

    画面・出力には GDP12DD0272C が表示され、監査レポート Server IP 0272 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0272A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0272B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0272C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0287 {#c10-i0496}
*分類: レポート*  ・  難易度: 中級

茶H抑止0288ではIBM Guardium Data Protection 12.x の レポートを扱う採取票茶H抑止0288です。茶H抑止0288は監査レポートの表示操作で監査レポートの対象欄を追跡する記録茶H抑止0288です。茶H抑止0288ではデータソースと取得時刻を採取票茶H抑止0288へ残します。茶H抑止0288ではジョブ失敗の見落としを避けるため補助資料も照合する判断茶H抑止0288です。茶H抑止0288の用語整理では監査レポートの対象値を実在出力で照合する記録茶H抑止0288です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0287の設定や表示を読む前に役割を確認します。監査レポート Client IP 0290ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはClient IPの監査タスクと取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。
    - B. 状態を読み取るための働きはAppliance Monitoriでデータベース処理一覧から TURBINE を読み・TURBINE とである。DB処理一覧からTURBINEを読むときはディスク逼迫中に検査データ流を防ぐ。
    - C. 状態を読み取るための働きはServer IPのデータソースと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。 ✅
    - D. 状態を読み取るための働きはディレクトリー UserのGuardAPI権限と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能データ・ジョブでCの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・抑止）です。照合データ・抑止に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・抑止・ジョブです。比較監査レ・抑止でA:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸はSer・抑止・データです。運用抑止・SerでB:の性能影響の確認 APP11は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸はデータ・監査レ・抑止です。仕様データ・抑止でD:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は抑止・ジョブ・データです。用語データ・抑止という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0287**

    - 検証目的: 監査レポートの監査レポート Server IP 0287について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.57
    Server IP 198.51.100.67
    Count 57
    確認コード GDP12DD0287A
    ```

    画面・出力には GDP12DD0287A が表示され、監査レポート Server IP 0287 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0287
    Process Type Report
    Status completed
    確認コード GDP12DD0287B
    ```

    画面・出力には GDP12DD0287B が表示され、監査レポート Server IP 0287 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor02
    Action required review
    Task result pending
    確認コード GDP12DD0287C
    ```

    画面・出力には GDP12DD0287C が表示され、監査レポート Server IP 0287 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0287A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0287B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0287C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0302 {#c10-i0497}
*分類: レポート*  ・  難易度: 中級

緑C解析0303ではIBM Guardium Data Protection 12.x の レポートを扱う採取票緑C解析0303です。緑C解析0303は監査レポートの点検操作で監査レポートの判定欄を記録する記録緑C解析0303です。緑C解析0303ではデータソースと取得時刻を採取票緑C解析0303へ残します。緑C解析0303ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断緑C解析0303です。緑C解析0303の用語整理では監査レポートの対象値を実在出力で保管する記録緑C解析0303です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0302に関する障害切り分けの前提を確認しています。ロールと権限 LDAP User 0327の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはディレクトリー UserのGuardAPI権限と取得時刻を記録し・GuardAPI実行権限不足を防ぐである。監査操作で記録欄を比較するときはGuardAPI実行権限不足を防ぐ。
    - B. 機能の説明としてはServer IPのデータソースと取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。 ✅
    - C. 機能の説明としてはInspection Engineでポリシー変更から Policy を読み・Policy とである。ポリシー変更からPolicyを読むときはInspectionを防ぐ。
    - D. 機能の説明としてはPermissionの表示可能レポートと取得時刻を記録し・ディレクトリー取込対象の誤りを防ぐである。変更確認操作で採取欄を棚卸するときはディレクトリー取込対象の誤りを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能データ・照会文でBの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・解析）です。照合データ・解析に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・解析・照会文です。比較監査レ・解析でA:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸はSer・解析・データです。項目データ・解析でC:の変更前の確認 IE02は「Inspection Engineでポリシー」を述べるため、正答側の照合軸は照会文・監査レ・データです。仕様データ・解析でD:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸は解析・照会文・データです。用語データ・解析という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0302**

    - 検証目的: 監査レポートの監査レポート Server IP 0302について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.72
    Server IP 198.51.100.22
    Count 72
    確認コード GDP12DD0302A
    ```

    画面・出力には GDP12DD0302A が表示され、監査レポート Server IP 0302 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0302
    Process Type Report
    Status completed
    確認コード GDP12DD0302B
    ```

    画面・出力には GDP12DD0302B が表示され、監査レポート Server IP 0302 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor08
    Action required review
    Task result pending
    確認コード GDP12DD0302C
    ```

    画面・出力には GDP12DD0302C が表示され、監査レポート Server IP 0302 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0302A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0302B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0302C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0317 {#c10-i0498}
*分類: レポート*  ・  難易度: 中級

藤R解析0318ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藤R解析0318です。藤R解析0318は監査レポートの復旧操作で監査レポートの点検欄を確認する記録藤R解析0318です。藤R解析0318ではデータソースと取得時刻を採取票藤R解析0318へ残します。藤R解析0318では監査タスク未レビューを避けるため補助資料も照合する判断藤R解析0318です。藤R解析0318の用語整理では監査レポートの対象値を実在出力で点検する記録藤R解析0318です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0317を保守記録に説明する必要があります。監査レポート Audit Task Status 0323と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はAudit Task Statusのユーザー活動と取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。
    - B. 運用時に利用する技術的役割はServer IPのデータソースと取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。 ✅
    - C. 運用時に利用する技術的役割はInspection Engineでエージェント変更から InspectionEngine を読みである。エージェント変更からInspectiときはInspectionを防ぐ。
    - D. 運用時に利用する技術的役割はApplication Accessのユーザー有効化と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能データ・監査タでBの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・解析）です。照合データ・解析に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・解析・監査タです。比較監査レ・解析でA:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸はSer・解析・データです。項目データ・解析でC:の引継ぎ記録 IE09は「Inspection Engineでエージェ」を述べるため、正答側の照合軸は監査タ・監査レ・データです。仕様データ・解析でD:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は解析・監査タ・データです。用語データ・解析という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0317**

    - 検証目的: 監査レポートの監査レポート Server IP 0317について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.87
    Server IP 198.51.100.37
    Count 87
    確認コード GDP12DD0317A
    ```

    画面・出力には GDP12DD0317A が表示され、監査レポート Server IP 0317 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0317
    Process Type Report
    Status completed
    確認コード GDP12DD0317B
    ```

    画面・出力には GDP12DD0317B が表示され、監査レポート Server IP 0317 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor05
    Action required review
    Task result pending
    確認コード GDP12DD0317C
    ```

    画面・出力には GDP12DD0317C が表示され、監査レポート Server IP 0317 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0317A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0317B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0317C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0332 {#c10-i0499}
*分類: レポート*  ・  難易度: 中級

桃M計画0333ではIBM Guardium Data Protection 12.x の レポートを扱う採取票桃M計画0333です。桃M計画0333は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録桃M計画0333です。桃M計画0333ではデータソースと取得時刻を採取票桃M計画0333へ残します。桃M計画0333では対象データソースの取り違えを避けるため補助資料も照合する判断桃M計画0333です。桃M計画0333の用語整理では監査レポートの対象値を実在出力で整理する記録桃M計画0333です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0332の技術的な意味を資料で確認するとき、S-TAP監視 KTAP Installed 0349との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてデータソースを照合する。 ✅
    - B. 構成を確認する際の意味は未承認監視エージェント接続を避けるため・記録操作で証跡欄を照合するして監視エージェを照合する。
    - C. 構成を確認する際の意味はディスク逼迫中に検査データ流入をを避けるため・監視プロセスからApplianceを読むして監視プロセスを照合する。
    - D. 構成を確認する際の意味は監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するして表示可能レポを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能データ・対象デでAの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・計画）です。照合データ・計画に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・計画・対象デです。運用計画・SerでB:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はデータ・監査レ・計画です。項目データ・計画でC:の容量余力の確認 APP16は「Appliance Monitoriで監視プ」を述べるため、正答側の照合軸は対象デ・監査レ・データです。仕様データ・計画でD:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸は計画・対象デ・データです。用語データ・計画という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0332**

    - 検証目的: 監査レポートの監査レポート Server IP 0332について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.22
    Server IP 198.51.100.52
    Count 102
    確認コード GDP12DD0332A
    ```

    画面・出力には GDP12DD0332A が表示され、監査レポート Server IP 0332 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0332
    Process Type Report
    Status completed
    確認コード GDP12DD0332B
    ```

    画面・出力には GDP12DD0332B が表示され、監査レポート Server IP 0332 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor02
    Action required review
    Task result pending
    確認コード GDP12DD0332C
    ```

    画面・出力には GDP12DD0332C が表示され、監査レポート Server IP 0332 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0332A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0332B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0332C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0347 {#c10-i0500}
*分類: レポート*  ・  難易度: 上級

茶H解除0348ではIBM Guardium Data Protection 12.x の レポートを扱う採取票茶H解除0348です。茶H解除0348は監査レポートの表示操作で監査レポートの対象欄を追跡する記録茶H解除0348です。茶H解除0348ではデータソースと取得時刻を採取票茶H解除0348へ残します。茶H解除0348ではジョブ失敗の見落としを避けるため補助資料も照合する判断茶H解除0348です。茶H解除0348の用語整理では監査レポートの対象値を実在出力で照合する記録茶H解除0348です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0347について構成や状態を確認します。datasource 障害時切り分け 再同期判断ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはServer IPのデータソースと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。 ✅
    - B. 状態を読み取るための働きは監視対象データベースやサービスを表す Guardium の登録単位を障害時切り分けとして確認する。データソースで再同期判断を確認するときは再同期判断の誤読を防ぐ。
    - C. 状態を読み取るための働きはAppliance Monitoriでデータベース処理一覧から TURBINE を読み・TURBINE とである。DB処理一覧からTURBINEを読むときはディスク逼迫中に検査データ流を防ぐ。
    - D. 状態を読み取るための働きは監視エージェントのカーネル監視有無と取得時刻を記録し・最終応答停止の見落としを防ぐである。確認操作で状態欄を整理するときは最終応答停止の見落としを防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能データ・ジョブでAの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・解除）です。照合データ・解除に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・解除・ジョブです。運用解除・SerでB:の障害時切り分け 再同期判断は「監視対象データベースやサービスを表す」を述べるため、正答側の照合軸はデータ・監査レ・解除です。項目データ・解除でC:の構成監査 APP08は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸はジョブ・監査レ・データです。仕様データ・解除でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は解除・ジョブ・データです。用語データ・解除という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0347**

    - 検証目的: 監査レポートの監査レポート Server IP 0347について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Server IP と データソース
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Activity Audit Trail report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.37
    Server IP 198.51.100.67
    Count 117
    確認コード GDP12DD0347A
    ```

    画面・出力には GDP12DD0347A が表示され、監査レポート Server IP 0347 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0347
    Process Type Report
    Status completed
    確認コード GDP12DD0347B
    ```

    画面・出力には GDP12DD0347B が表示され、監査レポート Server IP 0347 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Server IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process To Do List
    Login Name auditor08
    Action required review
    Task result pending
    確認コード GDP12DD0347C
    ```

    画面・出力には GDP12DD0347C が表示され、監査レポート Server IP 0347 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0347A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0347B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0347C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring




## IBM Guardium Data Protection 12.x > レポート管理

### Approved TAP Clients 対象絞り込み イベント識別 {#c10-i0501}
*分類: レポート管理*  ・  難易度: 上級

IBM Guardium Data Protection 12.x の レポート管理 で扱う「Approved TAP Clients 対象絞り込み イベント識別」は、接続を許可された S-TAP と状態を確認する管理レポートを対象絞り込みの観点で確認する技術項目です。Guardium Job QueueとCOL052を同じ記録で見比べることで、監査タスク未完了を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** Approved TAP Clients 対象絞り込み イベント識別の技術的な意味を資料で確認するとき、Central Manager 中央管理サーバー ログとの照合 CM07との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はレポートでイベント識別を証跡に残し・接続を許可された S-TAP と状態を確認する管理レポートを。 ✅
    - B. コマンドまたは機能の用途はログとの照合でログとの照合を証跡に残し・Central Managerでログとの照合では中央管理サー。
    - C. コマンドまたは機能の用途は復旧で照会文動詞集を証跡に残し・データベース User Nameの照会文動詞集計と取得時刻を。
    - D. コマンドまたは機能の用途は保護でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能イベン・イベンでAの記述「接続を許可された S-TAP と状態を確認する管理レポー」に対応する項目は対象絞り込み イベント識別（App・イベン・レポー）です。照合イベン・レポーに関するレポート管理の仕様は「接続を許可された S-TAP と状態を確認する管理レポートを対象絞り」で、確認対象はイベン・レポー・イベンです。運用レポー・AppでB:のログとの照合 CM07は「Central Managerでログとの照合」を述べるため、正答側の照合軸はイベン・対象絞・レポーです。項目イベン・レポーでC:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸はイベン・対象絞・イベンです。仕様イベン・レポーでD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸はレポー・イベン・イベンです。用語イベン・レポーという用語は「接続を許可された S-TAP と状態を確認する管理レ」を指し、照合する値と誤認リスクの組合せは対象絞・イベン・イベンです。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **Approved TAP Clients 対象絞り込み イベント識別**

    - 検証目的: レポート管理のApproved TAP Clients 対象絞り込み イベント識別について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、レポート管理の対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL052.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Guardium Job Queueを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP052     Approved    COL052
    ```

    画面・出力には Approved が含まれ、Approved TAP Clients 対象絞り込み イベント識別の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、監査タスク未完了を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP052            Completed   DSRC052
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### Approved TAP Clients 障害時切り分け 転送条件 {#c10-i0502}
*分類: レポート管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の レポート管理 で扱う「Approved TAP Clients 障害時切り分け 転送条件」は、接続を許可された S-TAP と状態を確認する管理レポートを障害時切り分けの観点で確認する技術項目です。Guardium Job QueueとCOL022を同じ記録で見比べることで、監査タスク未完了を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** Approved TAP Clients 障害時切り分け 転送条件に関する障害切り分けの前提を確認しています。sign-off trail 障害時切り分け 管理クラスの機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は管理クラスの誤読を避けるため・S-TAPで管理クラスを確認するして管理クラスを照合する。
    - B. 障害切り分けに用いる役割はジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するしてデータソースを照合する。
    - C. 障害切り分けに用いる役割は転送条件の誤読を避けるため・レポートで転送条件を確認するして転送条件を照合する。 ✅
    - D. 障害切り分けに用いる役割は監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するしてユーザー有効を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能転送条・転送条でCの記述「接続を許可された S-TAP と状態を確認する管理レポー」に対応する項目は障害時切り分け 転送条件（App・転送条・レポー）です。照合転送条・レポーに関するレポート管理の仕様は「接続を許可された S-TAP と状態を確認する管理レポートを障害時切」で、確認対象は転送条・レポー・転送条です。比較障害時・レポーでA:の障害時切り分け 管理クラスは「監査結果のレビューと承認の履歴を障害時切り分」を述べるため、正答側の照合軸はApp・レポー・転送条です。運用レポー・AppでB:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は転送条・障害時・レポーです。仕様転送条・レポーでD:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はレポー・転送条・転送条です。用語転送条・レポーという用語は「接続を許可された S-TAP と状態を確認する管理レ」を指し、照合する値と誤認リスクの組合せは障害時・転送条・転送条です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **Approved TAP Clients 障害時切り分け 転送条件**

    - 検証目的: レポート管理のApproved TAP Clients 障害時切り分け 転送条件について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、レポート管理の対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL022.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Guardium Job Queueを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP022     Approved    COL022
    ```

    画面・出力には Approved が含まれ、Approved TAP Clients 障害時切り分け 転送条件の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、監査タスク未完了を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP022            Completed   DSRC022
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### Central Manager 承認履歴確認 構成配布 {#c10-i0503}
*分類: レポート管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の レポート管理 で扱う「Central Manager 承認履歴確認 構成配布」は、管理対象システムの構成と配布を統制する管理点を承認履歴確認の観点で確認する技術項目です。Approved TAP Clients レポートとDSRC016を同じ記録で見比べることで、collector と aggregator の時刻差を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** Central Manager 承認履歴確認 構成配布を同一分類のcollector 状態確認 適用位置と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は状態確認で適用位置を確認することで適用位置を確認し・適用位置の誤読を防ぐ。
    - B. コマンドまたは機能の用途は保守操作で監査欄を保存することで暗号化表示を確認し・ローカル通信制御監視の未確認を防ぐ。
    - C. コマンドまたは機能の用途は承認履歴確認で構成配布を確認することで構成配布を確認し・構成配布の誤読を防ぐ。 ✅
    - D. コマンドまたは機能の用途は記録操作で証跡欄を照合することで承認クライアを確認し・未承認監視エージェント接続を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能構成配・構成配でCの記述「管理対象システムの構成と配布を統制する管理点を承認履歴確」に対応する項目は承認履歴確認 構成配布（Cen・構成配・承認履）です。照合構成配・承認履に関するレポート管理の仕様は「管理対象システムの構成と配布を統制する管理点を承認履歴確認する」で、確認対象は構成配・承認履・構成配です。比較承認履・承認履でA:の状態確認 適用位置は「S-TAP や外部接続から監査データを受け取」を述べるため、正答側の照合軸はCen・承認履・構成配です。運用承認履・CenでB:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は構成配・承認履・承認履です。仕様構成配・承認履でD:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は承認履・構成配・構成配です。用語構成配・承認履という用語は「管理対象システムの構成と配布を統制する管理点を承認履」を指し、照合する値と誤認リスクの組合せは承認履・構成配・構成配です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **Central Manager 承認履歴確認 構成配布**

    - 検証目的: レポート管理のCentral Manager 承認履歴確認 構成配布について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、レポート管理の対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL016.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Approved TAP Clients レポートを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP016     Approved    COL016
    ```

    画面・出力には Approved が含まれ、Central Manager 承認履歴確認 構成配布の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、collector と aggregator の時刻差を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP016            Completed   DSRC016
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### Central Manager 証跡採取 活動ログ {#c10-i0504}
*分類: レポート管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の レポート管理 で扱う「Central Manager 証跡採取 活動ログ」は、管理対象システムの構成と配布を統制する管理点を証跡採取の観点で確認する技術項目です。Approved TAP Clients レポートとDSRC046を同じ記録で見比べることで、collector と aggregator の時刻差を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** Central Manager 証跡採取 活動ログに関する障害切り分けの前提を確認しています。Central Manager 中央管理サーバー 世代整合の確認 CM17の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は世代整合確認で確認では中央を証跡に残し・Central Managerで世代整合の確認では中央管理サ。
    - B. 障害切り分けに用いる役割は証跡採取で活動ログを証跡に残し・管理対象システムの構成と配布を統制する管理点を証跡採取として。 ✅
    - C. 障害切り分けに用いる役割は復旧で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。
    - D. 障害切り分けに用いる役割は解析でディレクトリを証跡に残し・Roleのディレクトリー取込と取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能活動ロ・活動ロでBの記述「管理対象システムの構成と配布を統制する管理点を証跡採取と」に対応する項目は証跡採取 活動ログ（Cen・活動ロ・証跡採）です。照合活動ロ・証跡採に関するレポート管理の仕様は「管理対象システムの構成と配布を統制する管理点を証跡採取として確認する」で、確認対象は活動ロ・証跡採・活動ロです。比較証跡・証跡採でA:の世代整合の確認 CM17は「Central Managerで世代整合の確」を述べるため、正答側の照合軸はCen・証跡採・活動ロです。項目活動ロ・証跡採でC:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸は活動ロ・証跡・活動ロです。仕様活動ロ・証跡採でD:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は証跡採・活動ロ・活動ロです。用語活動ロ・証跡採という用語は「管理対象システムの構成と配布を統制する管理点を証跡採」を指し、照合する値と誤認リスクの組合せは証跡・活動ロ・活動ロです。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **Central Manager 証跡採取 活動ログ**

    - 検証目的: レポート管理のCentral Manager 証跡採取 活動ログについて、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、レポート管理の対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL046.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Approved TAP Clients レポートを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP046     Approved    COL046
    ```

    画面・出力には Approved が含まれ、Central Manager 証跡採取 活動ログの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、collector と aggregator の時刻差を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP046            Completed   DSRC046
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### collector 実行結果照合 対象表 {#c10-i0505}
*分類: レポート管理*  ・  難易度: 初級

IBM Guardium Data Protection 12.x の レポート管理 で扱う「collector 実行結果照合 対象表」は、S-TAP や外部接続から監査データを受け取る Guardium 装置を実行結果照合の観点で確認する技術項目です。Data Sources 欄とAP004を同じ記録で見比べることで、サインオフ不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** collector 実行結果照合 対象表の技術的な意味を資料で確認するとき、監査プロセス Audit Process Builder ログとの照合との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は対象表の誤読を避けるため・実行結果照合で対象表を確認するして対象表を照合する。 ✅
    - B. コマンドまたは機能の用途は実行間隔より短いFROM/TO範を避けるため・プロセス一覧からScheduleを読むしてプロセス一覧を照合する。
    - C. コマンドまたは機能の用途はGuardAPI実行権限不足を避けるため・監査操作で記録欄を比較するしてロール割当を照合する。
    - D. コマンドまたは機能の用途はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして承認クライアを照合する。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能対象表・対象表でAの記述「S-TAP や外部接続から監査データを受け取る」に対応する項目は実行結果照合 対象表（col・対象表・実行結）です。照合対象表・実行結に関するレポート管理の仕様は「S-TAP や外部接続から監査データを受け取る Guardium」で、確認対象は対象表・実行結・対象表です。運用実行結・colでB:のログとの照合 AUDIT07は「Audit Processでプロセス一覧から」を述べるため、正答側の照合軸は対象表・実行結・実行結です。項目対象表・実行結でC:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は対象表・実行結・対象表です。仕様対象表・実行結でD:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は実行結・対象表・対象表です。用語対象表・実行結という用語は「S-TAP や外部接続から監査データを受け取る」を指し、照合する値と誤認リスクの組合せは実行結・対象表・対象表です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **collector 実行結果照合 対象表**

    - 検証目的: レポート管理のcollector 実行結果照合 対象表について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、レポート管理の対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL004.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Data Sources 欄を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP004     Approved    COL004
    ```

    画面・出力には Approved が含まれ、collector 実行結果照合 対象表の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、サインオフ不備を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP004            Completed   DSRC004
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### collector 状態確認 適用位置 {#c10-i0506}
*分類: レポート管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の レポート管理 で扱う「collector 状態確認 適用位置」は、S-TAP や外部接続から監査データを受け取る Guardium 装置を状態確認の観点で確認する技術項目です。Data Sources 欄とAP034を同じ記録で見比べることで、サインオフ不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** collector 状態確認 適用位置の役割を調べています。Central Manager 中央管理サーバー 復旧後の確認 CM06の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はmanaged unitからのデを避けるため・復旧確認で復旧後の確認を確認するして復旧後の確認を照合する。
    - B. 障害切り分けに用いる役割は適用位置の誤読を避けるため・状態確認で適用位置を確認するして適用位置を照合する。 ✅
    - C. 障害切り分けに用いる役割はローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するして監視エージェを照合する。
    - D. 障害切り分けに用いる役割は過剰ロール付与を避けるため・主操作で出力欄を評価するしてGuardAを照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能適用位・適用位でBの記述「S-TAP や外部接続から監査データを受け取る」に対応する項目は状態確認 適用位置（col・適用位・状態確）です。照合適用位・状態確に関するレポート管理の仕様は「S-TAP や外部接続から監査データを受け取る Guardium」で、確認対象は適用位・状態確・適用位です。比較状態・状態確でA:の復旧後の確認 CM06は「Central ManagerでCentra」を述べるため、正答側の照合軸はcol・状態確・適用位です。項目適用位・状態確でC:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸は適用位・状態・適用位です。仕様適用位・状態確でD:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は状態確・適用位・適用位です。用語適用位・状態確という用語は「S-TAP や外部接続から監査データを受け取る」を指し、照合する値と誤認リスクの組合せは状態・適用位・適用位です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **collector 状態確認 適用位置**

    - 検証目的: レポート管理のcollector 状態確認 適用位置について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、レポート管理の対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL034.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Data Sources 欄を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP034     Approved    COL034
    ```

    画面・出力には Approved が含まれ、collector 状態確認 適用位置の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、サインオフ不備を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP034            Completed   DSRC034
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### sign-off trail 実行結果照合 監査証跡 {#c10-i0507}
*分類: レポート管理*  ・  難易度: 初級

IBM Guardium Data Protection 12.x の レポート管理 で扱う「sign-off trail 実行結果照合 監査証跡」は、監査結果のレビューと承認の履歴を実行結果照合の観点で確認する技術項目です。support gather_io_metrics 出力とSTAP010を同じ記録で見比べることで、S-TAP 未承認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** sign-off trail 実行結果照合 監査証跡の役割を調べています。データソース管理 Guardiumデータソース 復旧準備 DSRC05の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は参照箇所からUsedByを読むことで参照箇所を確認し・廃止サーバーの参照を残して監を防ぐ。
    - B. 障害切り分けに用いる役割は確認操作で状態欄を整理することで監視エージェを確認し・最終応答停止の見落としを防ぐ。
    - C. 障害切り分けに用いる役割は監査証跡で監査証跡を確認することで監査証跡を確認し・監査証跡の誤読を防ぐ。 ✅
    - D. 障害切り分けに用いる役割は照合操作で確認欄を採取することでロール割当を確認し・監査担当者の閲覧範囲不足を防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能監査証・監査証でCの記述「監査結果のレビューと承認の履歴を実行結果照合として確認す」に対応する項目は実行結果照合 監査証跡（sig・監査証・監査証）です。照合監査証・監査証に関するレポート管理の仕様は「監査結果のレビューと承認の履歴を実行結果照合として確認する」で、確認対象は監査証・監査証・監査証です。比較実行結・監査証でA:の復旧準備 DSRC05は「Guardiumで参照箇所から」を述べるため、正答側の照合軸はsig・監査証・監査証です。運用監査証・sigでB:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸は監査証・実行結・監査証です。仕様監査証・監査証でD:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は監査証・監査証・監査証です。用語監査証・監査証という用語は「監査結果のレビューと承認の履歴を実行結果照合として確」を指し、照合する値と誤認リスクの組合せは実行結・監査証・監査証です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **sign-off trail 実行結果照合 監査証跡**

    - 検証目的: レポート管理のsign-off trail 実行結果照合 監査証跡について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、レポート管理の対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL010.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。support gather_io_metrics 出力を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP010     Approved    COL010
    ```

    画面・出力には Approved が含まれ、sign-off trail 実行結果照合 監査証跡の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、S-TAP 未承認を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP010            Completed   DSRC010
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### sign-off trail 状態確認 キュー状態 {#c10-i0508}
*分類: レポート管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の レポート管理 で扱う「sign-off trail 状態確認 キュー状態」は、監査結果のレビューと承認の履歴を状態確認の観点で確認する技術項目です。support gather_io_metrics 出力とSTAP040を同じ記録で見比べることで、S-TAP 未承認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** sign-off trail 状態確認 キュー状態を同一分類のAggregator Guardium Aggregator 通常状態の確認と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は集約遅延中の期間を監査完了としてを避けるため・集約エラーからAggregationを読して集約エラーを照合する。
    - B. コマンドまたは機能の用途はキュー状態の誤読を避けるため・状態確認でキュー状態を確認するしてキュー状態を照合する。 ✅
    - C. コマンドまたは機能の用途はディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてロール割当を照合する。
    - D. コマンドまたは機能の用途はローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するして監視エージェを照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能キュー・キューでBの記述「監査結果のレビューと承認の履歴である」に対応する項目は状態確認 キュー状態（sig・キュー・状態確）です。照合キュー・状態確に関するレポート管理の仕様は「監査結果のレビューと承認の履歴」で、確認対象はキュー・状態確・キューです。比較状態・状態確でA:の通常状態の確認 AGG01は「Aggregatorで集約エラーから」を述べるため、正答側の照合軸はsig・状態確・キューです。項目キュー・状態確でC:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸はキュー・状態・キューです。仕様キュー・状態確でD:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸は状態確・キュー・キューです。用語キュー・状態確という用語は「監査結果のレビューと承認の履歴」を指し、照合する値と誤認リスクの組合せは状態・キュー・キューです。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **sign-off trail 状態確認 キュー状態**

    - 検証目的: レポート管理のsign-off trail 状態確認 キュー状態について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、レポート管理の対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL040.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。support gather_io_metrics 出力を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP040     Approved    COL040
    ```

    画面・出力には Approved が含まれ、sign-off trail 状態確認 キュー状態の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、S-TAP 未承認を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP040            Completed   DSRC040
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### support gather_io_metrics 対象絞り込み 一覧画面 {#c10-i0509}
*分類: レポート管理*  ・  難易度: 上級

IBM Guardium Data Protection 12.x の レポート管理 で扱う「support gather_io_metrics 対象絞り込み 一覧画面」は、I/O 指標を収集するサポートCLIコマンドを対象絞り込みの観点で確認する技術項目です。audit process logとRUN058を同じ記録で見比べることで、データソース指定漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** support gather_io_metrics 対象絞り込み 一覧画面の役割を調べています。Aggregator Guardium Aggregator 構成監査 AGG08の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は構成監査で監査タスクを証跡に残し・Aggregatorで監査タスクから。
    - B. 障害切り分けに用いる役割は保守で表示可能レポを証跡に残し・Permissionの表示可能レポートと取得時刻を記録し。ロールと権限 Permission 0153固有の属性も確認対象に含める。
    - C. 障害切り分けに用いる役割はレポートで一覧画面を証跡に残し・I/O 指標を収集するサポートCLIコマンドを対象絞り込みと。 ✅
    - D. 障害切り分けに用いる役割は保護でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能一覧画・一覧画でCの記述「I/O 指標を収集するサポートCLIコマンドを対象絞り込」に対応する項目は対象絞り込み 一覧画面（sup・一覧画・レポー）です。照合一覧画・レポーに関するレポート管理の仕様は「I/O 指標を収集するサポートCLIコマンドを対象絞り込みとして確認」で、確認対象は一覧画・レポー・一覧画です。比較対象絞・レポーでA:の構成監査 AGG08は「Aggregatorで監査タスクから」を述べるため、正答側の照合軸はsup・レポー・一覧画です。運用レポー・supでB:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸は一覧画・対象絞・レポーです。仕様一覧画・レポーでD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸はレポー・一覧画・一覧画です。用語一覧画・レポーという用語は「I/O 指標を収集するサポートCLIコマンドを対象絞」を指し、照合する値と誤認リスクの組合せは対象絞・一覧画・一覧画です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **support gather_io_metrics 対象絞り込み 一覧画面**

    - 検証目的: レポート管理のsupport gather_io_metrics 対象絞り込み 一覧画面について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、レポート管理の対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL058.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。audit process logを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP058     Approved    COL058
    ```

    画面・出力には Approved が含まれ、support gather_io_metrics 対象絞り込み 一覧画面の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、データソース指定漏れを切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP058            Completed   DSRC058
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### support gather_io_metrics 障害時切り分け 出力見出し {#c10-i0510}
*分類: レポート管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の レポート管理 で扱う「support gather_io_metrics 障害時切り分け 出力見出し」は、I/O 指標を収集するサポートCLIコマンドを障害時切り分けの観点で確認する技術項目です。audit process logとRUN028を同じ記録で見比べることで、データソース指定漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** support gather_io_metrics 障害時切り分け 出力見出しの技術的な意味を資料で確認するとき、監査プロセス Audit Process Builder 変更後の確認との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は変更確認で報告上限を証跡に残し・Audit Processで報告上限から。監査プロセス Audit Process Builder 変更後の確認固有の属性も確認対象に含める。
    - B. コマンドまたは機能の用途は変更でロール割当を証跡に残し・Login Nameのロール割当と取得時刻を記録し。
    - C. コマンドまたは機能の用途は確認でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。
    - D. コマンドまたは機能の用途はレポートで出力見出しを証跡に残し・I/O 指標を収集するサポートCLIコマンドを障害時切り分け。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能出力見・出力見でDの記述「I/O 指標を収集するサポートCLIコマンドを障害時切り」に対応する項目は障害時切り分け 出力見出し（sup・出力見・レポー）です。照合出力見・レポーに関するレポート管理の仕様は「I/O 指標を収集するサポートCLIコマンドを障害時切り分けとして確」で、確認対象は出力見・レポー・出力見です。比較障害時・レポーでA:の変更後の確認 AUDIT03は「Audit Processで報告上限から」を述べるため、正答側の照合軸はsup・レポー・出力見です。運用レポー・supでB:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は出力見・障害時・レポーです。項目出力見・レポーでC:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は出力見・障害時・出力見です。用語出力見・レポーという用語は「I/O 指標を収集するサポートCLIコマンドを障害時」を指し、照合する値と誤認リスクの組合せは障害時・出力見・出力見です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **support gather_io_metrics 障害時切り分け 出力見出し**

    - 検証目的: レポート管理のsupport gather_io_metrics 障害時切り分け 出力見出しについて、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、レポート管理の対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL028.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。audit process logを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP028     Approved    COL028
    ```

    画面・出力には Approved が含まれ、support gather_io_metrics 障害時切り分け 出力見出しの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、データソース指定漏れを切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP028            Completed   DSRC028
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide




## IBM Guardium Data Protection 12.x > 監査プロセス

### Guardium Job Queue 実行結果照合 サインオフ {#c10-i0511}
*分類: 監査プロセス*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の 監査プロセス で扱う「Guardium Job Queue 実行結果照合 サインオフ」は、処理ID、状態、開始終了時刻、Data Sources を示すジョブ一覧を実行結果照合の観点で確認する技術項目です。Guardium Job QueueとCOL037を同じ記録で見比べることで、監査タスク未完了を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** Guardium Job Queue 実行結果照合 サインオフを保守記録に説明する必要があります。監査プロセス Audit Process Builder 障害切り分けと取り違えない説明はどれですか。

    - A. 仕様上の役割は監査プロセスでプロセス一覧を証跡に残し・Audit Processでプロセス一覧から。
    - B. 仕様上の役割は診断で監視エージェを証跡に残し・監視エージェントの監視エージェント状態と取得時刻を記録し。S-TAP監視 KTAP Installed 0124固有の属性も確認対象に含める。
    - C. 仕様上の役割は保護で暗号化表示を証跡に残し・監視エージェントの暗号化表示と取得時刻を記録し。
    - D. 仕様上の役割は実行結果照合でサインオフを証跡に残し・処理ID・状態・開始終了時刻・Data Sources。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能サイン・サインでDの記述「処理ID、状態、開始終了時刻、Data Sources」に対応する項目は実行結果照合 サインオフ（Gua・サイン・実行結）です。照合サイン・実行結に関する監査プロセスの仕様は「処理ID、状態、開始終了時刻、Data Sources」で、確認対象はサイン・実行結・サインです。比較実行結・実行結でA:の障害切り分け AUDIT04は「Audit Processでプロセス一覧から」を述べるため、正答側の照合軸はGua・実行結・サインです。運用実行結・GuaでB:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はサイン・実行結・実行結です。項目サイン・実行結でC:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はサイン・実行結・サインです。用語サイン・実行結という用語は「処理ID、状態、開始終了時刻、Data」を指し、照合する値と誤認リスクの組合せは実行結・サイン・サインです。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **Guardium Job Queue 実行結果照合 サインオフ**

    - 検証目的: 監査プロセスのGuardium Job Queue 実行結果照合 サインオフについて、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、監査プロセスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL037.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Guardium Job Queueを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP037     Approved    COL037
    ```

    画面・出力には Approved が含まれ、Guardium Job Queue 実行結果照合 サインオフの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、監査タスク未完了を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP037            Completed   DSRC037
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### Guardium Job Queue 状態確認 詳細表示 {#c10-i0512}
*分類: 監査プロセス*  ・  難易度: 初級

IBM Guardium Data Protection 12.x の 監査プロセス で扱う「Guardium Job Queue 状態確認 詳細表示」は、処理ID、状態、開始終了時刻、Data Sources を示すジョブ一覧を状態確認の観点で確認する技術項目です。Guardium Job QueueとCOL007を同じ記録で見比べることで、監査タスク未完了を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** Guardium Job Queue 状態確認 詳細表示の設定や表示を読む前に役割を確認します。support gather_io_metrics 実行結果照合 プール宛先ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は処理ID・状態・開始終了時刻・Data Sources を示すジョブ一覧である。詳細表示で詳細表示を確認するときは詳細表示の誤読を防ぐ。 ✅
    - B. 一次資料が示す主目的はI/O 指標を収集するサポートCLIコマンドを実行結果照合として確認する。実行結果照合でプール宛先を確認するときはプール宛先の誤読を防ぐ。
    - C. 一次資料が示す主目的はRoleのディレクトリー取込と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。
    - D. 一次資料が示す主目的はデータベース User Nameの照会文動詞集計と取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能詳細表・詳細表でAの記述「処理ID、状態、開始終了時刻、Data Sources」に対応する項目は状態確認 詳細表示（Gua・詳細表・詳細表）です。照合詳細表・詳細表に関する監査プロセスの仕様は「処理ID、状態、開始終了時刻、Data Sources」で、確認対象は詳細表・詳細表・詳細表です。運用詳細表・GuaでB:の実行結果照合 プール宛先は「I/O 指標を収集するサポートCLIコマンド」を述べるため、正答側の照合軸は詳細表・状態・詳細表です。項目詳細表・詳細表でC:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は詳細表・状態・詳細表です。仕様詳細表・詳細表でD:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は詳細表・詳細表・詳細表です。用語詳細表・詳細表という用語は「処理ID、状態、開始終了時刻、Data」を指し、照合する値と誤認リスクの組合せは状態・詳細表・詳細表です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **Guardium Job Queue 状態確認 詳細表示**

    - 検証目的: 監査プロセスのGuardium Job Queue 状態確認 詳細表示について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、監査プロセスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL007.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Guardium Job Queueを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP007     Approved    COL007
    ```

    画面・出力には Approved が含まれ、Guardium Job Queue 状態確認 詳細表示の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、監査タスク未完了を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP007            Completed   DSRC007
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### aggregator 対象絞り込み キーマップ {#c10-i0513}
*分類: 監査プロセス*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の 監査プロセス で扱う「aggregator 対象絞り込み キーマップ」は、複数 collector の監査情報を集約しレポートへ渡す装置を対象絞り込みの観点で確認する技術項目です。support gather_io_metrics 出力とSTAP025を同じ記録で見比べることで、S-TAP 未承認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** 「aggregator 対象絞り込み キーマップ」を「collector 状態確認 適用位置」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は適用位置の誤読を避けるため・状態確認で適用位置を確認するして適用位置を照合する。
    - B. 仕様上の役割は監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するしてユーザー有効を照合する。
    - C. 仕様上の役割は未承認監視エージェント接続を避けるため・記録操作で証跡欄を照合するして最終応答を照合する。
    - D. 仕様上の役割はキーマップの誤読を避けるため・監査プロセスでキーマップを確認するしてキーマップを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能キーマ・キーマでDの記述「複数 collector の監査情報を集約しレポートへ渡」に対応する項目は対象絞り込み キーマップ（agg・キーマ・監査プ）です。照合キーマ・監査プに関する監査プロセスの仕様は「複数 collector の監査情報を集約しレポートへ渡す装置を対象」で、確認対象はキーマ・監査プ・キーマです。比較対象絞・監査プでA:の状態確認 適用位置は「S-TAP や外部接続から監査データを受け取」を述べるため、正答側の照合軸はagg・監査プ・キーマです。運用監査プ・aggでB:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はキーマ・対象絞・監査プです。項目キーマ・監査プでC:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はキーマ・対象絞・キーマです。用語キーマ・監査プという用語は「複数 collector の監査情報を集約しレポート」を指し、照合する値と誤認リスクの組合せは対象絞・キーマ・キーマです。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **aggregator 対象絞り込み キーマップ**

    - 検証目的: 監査プロセスのaggregator 対象絞り込み キーマップについて、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、監査プロセスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL025.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。support gather_io_metrics 出力を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP025     Approved    COL025
    ```

    画面・出力には Approved が含まれ、aggregator 対象絞り込み キーマップの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、S-TAP 未承認を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP025            Completed   DSRC025
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### aggregator 障害時切り分け 接続認証 {#c10-i0514}
*分類: 監査プロセス*  ・  難易度: 上級

IBM Guardium Data Protection 12.x の 監査プロセス で扱う「aggregator 障害時切り分け 接続認証」は、複数 collector の監査情報を集約しレポートへ渡す装置を障害時切り分けの観点で確認する技術項目です。support gather_io_metrics 出力とSTAP055を同じ記録で見比べることで、S-TAP 未承認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** aggregator 障害時切り分け 接続認証の設定や表示を読む前に役割を確認します。Central Manager 中央管理サーバー 依存関係の確認 CM13ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は依存関係確認で確認では中央を確認することで確認では中央を確認し・managed unitからを防ぐ。
    - B. 一次資料が示す主目的は監査プロセスで接続認証を確認することで接続認証を確認し・接続認証の誤読を防ぐ。 ✅
    - C. 一次資料が示す主目的は採取操作で照合欄を点検することで監視エージェを確認し・カーネル監視導入状態の誤読を防ぐ。
    - D. 一次資料が示す主目的は調査操作で保守欄を引き継ぎすることで監査タスクを確認し・対象データソースの取り違えを防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能接続認・接続認でBの記述「複数 collector の監査情報を集約しレポートへ渡」に対応する項目は障害時切り分け 接続認証（agg・接続認・監査プ）です。照合接続認・監査プに関する監査プロセスの仕様は「複数 collector の監査情報を集約しレポートへ渡す装置を障害」で、確認対象は接続認・監査プ・接続認です。比較障害時・監査プでA:の依存関係の確認 CM13は「Central Managerで依存関係の確」を述べるため、正答側の照合軸はagg・監査プ・接続認です。項目接続認・監査プでC:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸は接続認・障害時・接続認です。仕様接続認・監査プでD:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸は監査プ・接続認・接続認です。用語接続認・監査プという用語は「複数 collector の監査情報を集約しレポート」を指し、照合する値と誤認リスクの組合せは障害時・接続認・接続認です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **aggregator 障害時切り分け 接続認証**

    - 検証目的: 監査プロセスのaggregator 障害時切り分け 接続認証について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、監査プロセスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL055.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。support gather_io_metrics 出力を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP055     Approved    COL055
    ```

    画面・出力には Approved が含まれ、aggregator 障害時切り分け 接続認証の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、S-TAP 未承認を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP055            Completed   DSRC055
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### audit process 実行結果照合 遅延表示 {#c10-i0515}
*分類: 監査プロセス*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の 監査プロセス で扱う「audit process 実行結果照合 遅延表示」は、監査要件に沿ってレポート実行とレビューを束ねる処理を実行結果照合の観点で確認する技術項目です。Approved TAP Clients レポートとDSRC031を同じ記録で見比べることで、collector と aggregator の時刻差を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** audit process 実行結果照合 遅延表示の設定や表示を読む前に役割を確認します。Central Manager 中央管理サーバー 容量余力の確認 CM16ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はmanaged unitからのデを避けるため・容量余力確認で確認では中央を確認するして確認では中央を照合する。
    - B. 一次資料が示す主目的はジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するして監査タスクを照合する。
    - C. 一次資料が示す主目的はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして最終応答を照合する。
    - D. 一次資料が示す主目的は遅延表示の誤読を避けるため・遅延表示で遅延表示を確認するして遅延表示を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能遅延表・遅延表でDの記述「監査要件に沿ってレポート実行とレビューを束ねる処理を実行」に対応する項目は実行結果照合 遅延表示（aud・遅延表・遅延表）です。照合遅延表・遅延表に関する監査プロセスの仕様は「監査要件に沿ってレポート実行とレビューを束ねる処理を実行結果照合とし」で、確認対象は遅延表・遅延表・遅延表です。比較実行結・遅延表でA:の容量余力の確認 CM16は「Central Managerで容量余力の確」を述べるため、正答側の照合軸はaud・遅延表・遅延表です。運用遅延表・audでB:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸は遅延表・実行結・遅延表です。項目遅延表・遅延表でC:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は遅延表・実行結・遅延表です。用語遅延表・遅延表という用語は「監査要件に沿ってレポート実行とレビューを束ねる処理を」を指し、照合する値と誤認リスクの組合せは実行結・遅延表・遅延表です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **audit process 実行結果照合 遅延表示**

    - 検証目的: 監査プロセスのaudit process 実行結果照合 遅延表示について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、監査プロセスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL031.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Approved TAP Clients レポートを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP031     Approved    COL031
    ```

    画面・出力には Approved が含まれ、audit process 実行結果照合 遅延表示の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、collector と aggregator の時刻差を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP031            Completed   DSRC031
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### audit process 状態確認 開始時刻 {#c10-i0516}
*分類: 監査プロセス*  ・  難易度: 初級

IBM Guardium Data Protection 12.x の 監査プロセス で扱う「audit process 状態確認 開始時刻」は、監査要件に沿ってレポート実行とレビューを束ねる処理を状態確認の観点で確認する技術項目です。Approved TAP Clients レポートとDSRC001を同じ記録で見比べることで、collector と aggregator の時刻差を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** 「audit process 状態確認 開始時刻」を「Central Manager 障害時切り分け 応答行」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は管理対象システムの構成と配布を統制する管理点を障害時切り分けとして確認する。Aggregで応答行を確認するときは応答行の誤読を防ぐ。
    - B. 仕様上の役割は監査要件に沿ってレポート実行とレビューを束ねる処理である。状態確認で開始時刻を確認するときは開始時刻の誤読を防ぐ。 ✅
    - C. 仕様上の役割はデータベース User Nameの照会文動詞集計と取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。
    - D. 仕様上の役割は監視エージェントのカーネル監視有無と取得時刻を記録し・カーネル監視導入状態の誤読を防ぐである。採取操作で照合欄を点検するときはカーネル監視導入状態の誤読を防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能開始時・開始時でBの記述「監査要件に沿ってレポート実行とレビューを束ねる処理である」に対応する項目は状態確認 開始時刻（aud・開始時・状態確）です。照合開始時・状態確に関する監査プロセスの仕様は「監査要件に沿ってレポート実行とレビューを束ねる処理」で、確認対象は開始時・状態確・開始時です。比較状態・状態確でA:の障害時切り分け 応答行は「管理対象システムの構成と配布を統制する管理点」を述べるため、正答側の照合軸はaud・状態確・開始時です。項目開始時・状態確でC:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は開始時・状態・開始時です。仕様開始時・状態確でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は状態確・開始時・開始時です。用語開始時・状態確という用語は「監査要件に沿ってレポート実行とレビューを束ねる処理」を指し、照合する値と誤認リスクの組合せは状態・開始時・開始時です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **audit process 状態確認 開始時刻**

    - 検証目的: 監査プロセスのaudit process 状態確認 開始時刻について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、監査プロセスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL001.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Approved TAP Clients レポートを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP001     Approved    COL001
    ```

    画面・出力には Approved が含まれ、audit process 状態確認 開始時刻の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、collector と aggregator の時刻差を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP001            Completed   DSRC001
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### datasource 承認履歴確認 復元前提 {#c10-i0517}
*分類: 監査プロセス*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の 監査プロセス で扱う「datasource 承認履歴確認 復元前提」は、監視対象データベースやサービスを表す Guardium の登録単位を承認履歴確認の観点で確認する技術項目です。audit process logとRUN043を同じ記録で見比べることで、データソース指定漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** datasource 承認履歴確認 復元前提について構成や状態を確認します。データソース管理 Guardiumデータソース 停止前の確認 DSRC14ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は廃止サーバーの参照を残して監査対を避けるため・参照箇所からUsedByを読むして参照箇所を照合する。
    - B. 一次資料が示す主目的は復元前提の誤読を避けるため・承認履歴確認で復元前提を確認するして復元前提を照合する。 ✅
    - C. 一次資料が示す主目的は未承認監視エージェント接続を避けるため・記録操作で証跡欄を照合するして暗号化表示を照合する。
    - D. 一次資料が示す主目的はディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてディレクトリを照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能復元前・復元前でBの記述「監視対象データベースやサービスを表す Guardium」に対応する項目は承認履歴確認 復元前提（dat・復元前・承認履）です。照合復元前・承認履に関する監査プロセスの仕様は「監視対象データベースやサービスを表す Guardium」で、確認対象は復元前・承認履・復元前です。比較承認履・承認履でA:の停止前の確認 DSRC14は「Guardiumで参照箇所から」を述べるため、正答側の照合軸はdat・承認履・復元前です。項目復元前・承認履でC:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は復元前・承認履・復元前です。仕様復元前・承認履でD:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は承認履・復元前・復元前です。用語復元前・承認履という用語は「監視対象データベースやサービスを表す」を指し、照合する値と誤認リスクの組合せは承認履・復元前・復元前です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **datasource 承認履歴確認 復元前提**

    - 検証目的: 監査プロセスのdatasource 承認履歴確認 復元前提について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、監査プロセスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL043.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。audit process logを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP043     Approved    COL043
    ```

    画面・出力には Approved が含まれ、datasource 承認履歴確認 復元前提の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、データソース指定漏れを切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP043            Completed   DSRC043
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### datasource 証跡採取 承認履歴 {#c10-i0518}
*分類: 監査プロセス*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の 監査プロセス で扱う「datasource 証跡採取 承認履歴」は、監視対象データベースやサービスを表す Guardium の登録単位を証跡採取の観点で確認する技術項目です。audit process logとRUN013を同じ記録で見比べることで、データソース指定漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** datasource 証跡採取 承認履歴を保守記録に説明する必要があります。データソース管理 Guardiumデータソース 代替経路の確認 DSRC10と取り違えない説明はどれですか。

    - A. 仕様上の役割はデータソース一覧からServiceNamことでデータソースを確認し・廃止サーバーの参照を残して監を防ぐ。
    - B. 仕様上の役割は証跡採取で承認履歴を確認することで承認履歴を確認し・承認履歴の誤読を防ぐ。 ✅
    - C. 仕様上の役割は照合操作で確認欄を採取することでロール割当を確認し・監査担当者の閲覧範囲不足を防ぐ。
    - D. 仕様上の役割は記録操作で証跡欄を照合することでカーネル監視を確認し・未承認監視エージェント接続を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能承認履・承認履でBの記述「監視対象データベースやサービスを表す Guardium」に対応する項目は証跡採取 承認履歴（dat・承認履・証跡採）です。照合承認履・証跡採に関する監査プロセスの仕様は「監視対象データベースやサービスを表す Guardium」で、確認対象は承認履・証跡採・承認履です。比較証跡・証跡採でA:の代替経路の確認 DSRC10は「Guardiumでデータソース一覧から」を述べるため、正答側の照合軸はdat・証跡採・承認履です。項目承認履・証跡採でC:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は承認履・証跡・承認履です。仕様承認履・証跡採でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は証跡採・承認履・承認履です。用語承認履・証跡採という用語は「監視対象データベースやサービスを表す」を指し、照合する値と誤認リスクの組合せは証跡・承認履・承認履です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **datasource 証跡採取 承認履歴**

    - 検証目的: 監査プロセスのdatasource 証跡採取 承認履歴について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、監査プロセスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL013.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。audit process logを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP013     Approved    COL013
    ```

    画面・出力には Approved が含まれ、datasource 証跡採取 承認履歴の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、データソース指定漏れを切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP013            Completed   DSRC013
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### inspection engine 承認履歴確認 ドメイン値 {#c10-i0519}
*分類: 監査プロセス*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の 監査プロセス で扱う「inspection engine 承認履歴確認 ドメイン値」は、データベース通信を解析し監査レコードを作る処理を承認履歴確認の観点で確認する技術項目です。Data Sources 欄とAP049を同じ記録で見比べることで、サインオフ不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** 「inspection engine 承認履歴確認 ドメイン値」を「監査プロセス Audit Process Builder 世代整合の確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は世代整合確認で作業一覧を証跡に残し・Audit Processで作業一覧から Status。
    - B. 仕様上の役割は診断で承認クライアを証跡に残し・監視エージェントの承認クライアントと取得時刻を記録し。
    - C. 仕様上の役割は承認履歴確認でドメイン値を証跡に残し・データベース通信を解析し監査レコードを作る処理を承認履歴確認。 ✅
    - D. 仕様上の役割は抑止でジョブキューを証跡に残し・照会文 Verbのジョブキューと取得時刻を記録し。監査レポート SQL Verb 0281固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ドメイ・ドメイでCの記述「データベース通信を解析し監査レコードを作る処理を承認履歴」に対応する項目は承認履歴確認 ドメイン値（ins・ドメイ・承認履）です。照合ドメイ・承認履に関する監査プロセスの仕様は「データベース通信を解析し監査レコードを作る処理を承認履歴確認する」で、確認対象はドメイ・承認履・ドメイです。比較承認履・承認履でA:の世代整合の確認 AUDIT17は「Audit Processで作業一覧から」を述べるため、正答側の照合軸はins・承認履・ドメイです。運用承認履・insでB:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はドメイ・承認履・承認履です。仕様ドメイ・承認履でD:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は承認履・ドメイ・ドメイです。用語ドメイ・承認履という用語は「データベース通信を解析し監査レコードを作る処理を承認」を指し、照合する値と誤認リスクの組合せは承認履・ドメイ・ドメイです。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **inspection engine 承認履歴確認 ドメイン値**

    - 検証目的: 監査プロセスのinspection engine 承認履歴確認 ドメイン値について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、監査プロセスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL049.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Data Sources 欄を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP049     Approved    COL049
    ```

    画面・出力には Approved が含まれ、inspection engine 承認履歴確認 ドメイン値の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、サインオフ不備を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP049            Completed   DSRC049
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### inspection engine 証跡採取 変換規則 {#c10-i0520}
*分類: 監査プロセス*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の 監査プロセス で扱う「inspection engine 証跡採取 変換規則」は、データベース通信を解析し監査レコードを作る処理を証跡採取の観点で確認する技術項目です。Data Sources 欄とAP019を同じ記録で見比べることで、サインオフ不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** inspection engine 証跡採取 変換規則について構成や状態を確認します。datasource 状態確認 文字変換ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は状態確認で文字変換を確認することで文字変換を確認し・文字変換の誤読を防ぐ。
    - B. 一次資料が示す主目的は監査操作で記録欄を比較することでユーザー有効を確認し・GuardAPI実行権限不足を防ぐ。
    - C. 一次資料が示す主目的は調査操作で保守欄を引き継ぎすることでデータソースを確認し・対象データソースの取り違えを防ぐ。
    - D. 一次資料が示す主目的は証跡採取で変換規則を確認することで変換規則を確認し・変換規則の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能変換規・変換規でDの記述「データベース通信を解析し監査レコードを作る処理を証跡採取」に対応する項目は証跡採取 変換規則（ins・変換規・証跡採）です。照合変換規・証跡採に関する監査プロセスの仕様は「データベース通信を解析し監査レコードを作る処理を証跡採取として確認す」で、確認対象は変換規・証跡採・変換規です。比較証跡・証跡採でA:の状態確認 文字変換は「監視対象データベースやサービスを表す」を述べるため、正答側の照合軸はins・証跡採・変換規です。運用証跡採・insでB:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は変換規・証跡・証跡採です。項目変換規・証跡採でC:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は変換規・証跡・変換規です。用語変換規・証跡採という用語は「データベース通信を解析し監査レコードを作る処理を証跡」を指し、照合する値と誤認リスクの組合せは証跡・変換規・変換規です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **inspection engine 証跡採取 変換規則**

    - 検証目的: 監査プロセスのinspection engine 証跡採取 変換規則について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、監査プロセスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support gather_io_metrics
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium CLI
    support gather_io_metrics
    I/O metrics collection request accepted for appliance COL019.
    ```

    画面・出力には Guardium が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面です。Data Sources 欄を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Reports > Predefined Admin Reports
    → Enter を押す
    ```

    画面・出力:
    ```text
    Approved TAP Clients
    S-TAP       Status      Collector
    STAP019     Approved    COL019
    ```

    画面・出力には Approved が含まれ、inspection engine 証跡採取 変換規則の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの詳細確認画面です。表示名とメッセージ形式を照合し、サインオフ不備を切り分けます。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> ?S Monitor and Audit > Audit Process Log
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Log
    Process Run ID  Status      Data Sources
    AP019            Completed   DSRC019
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### 監査プロセス Audit Process Builder ログとの照合 AUDIT07 {#c10-i0521}
*分類: 監査プロセス*  ・  難易度: 初級

ログとの照合では 監査プロセス の プロセス一覧 を主操作として AUDIT07 を判定します。時刻と対象識別子への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT07 に残します。ログとの照合を補助する 作業一覧 では Status を補助値として AUDIT07 へ保存します。主判定のログとの照合では監査プロセスの プロセス一覧 から Schedule を読み AUDIT07 へ残します。証跡照合のログとの照合では監査プロセスの Schedule と Status を AUDIT07 に保存します。記録対応のログとの照合では監査プロセスの ScheduleとTask Status の証跡へ AUDIT07 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder ログとの照合 AUDIT07について構成や状態を確認します。Aggregator Guardium Aggregator 復旧準備 AGG05ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は復旧準備で監査タスクを証跡に残し・Aggregatorで監査タスクから。
    - B. 一次資料が示す主目的は診断でGuardAを証跡に残し・ディレクトリー UserのGuardAPI権限と取得時刻を記。
    - C. 一次資料が示す主目的はログとの照合でプロセス一覧を証跡に残し・Audit Processでプロセス一覧から。 ✅
    - D. 一次資料が示す主目的は解析でジョブキューを証跡に残し・照会文 Verbのジョブキューと取得時刻を記録し。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能プロセ・実行間でCの記述「Audit Processでプロセス一覧から」に対応する項目はログとの照合 AUDIT07（Aud・プロセ・ログと）です。照合プロセ・ログとに関する監査プロセスの仕様は「Audit Processでプロセス一覧から Schedule」で、確認対象はプロセ・ログと・実行間です。比較監査プ・ログとでA:の復旧準備 AGG05は「Aggregatorで監査タスクから」を述べるため、正答側の照合軸はAud・ログと・プロセです。運用ログと・AudでB:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸はプロセ・監査プ・ログとです。仕様プロセ・ログとでD:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はログと・実行間・プロセです。用語プロセ・ログとという用語は「Audit Processでプロセス一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・プロセ・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder ログとの照合 AUDIT07**

    - 検証目的: 監査プロセスのAudit Process Builderについて操作とログを対応し、AUDIT07のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT07のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT07 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT07の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT07 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT07の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Schedule が画面・出力に表示されること
    ② ステップ2 の Status が画面・出力に表示されること
    ③ ステップ3 の audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 世代整合の確認 AUDIT17 {#c10-i0522}
*分類: 監査プロセス*  ・  難易度: 初級

世代整合の確認では 監査プロセス の 作業一覧 を主操作として AUDIT17 を判定します。定義と実行モジュールの版への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT17 に残します。世代整合の確認を補助する 報告上限 では max_audit_reporting を補助値として AUDIT17 へ保存します。主判定の世代整合の確認では監査プロセスの 作業一覧 から Status を読み AUDIT17 へ残します。証跡照合の世代整合の確認では監査プロセスの Status と max_audit_reporting を AUDIT17 に保存します。記録対応の世代整合の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT17 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 世代整合の確認 AUDIT17を保守記録に説明する必要があります。ポリシー・検査エンジン Inspection Engine ログとの照合 IE07と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は作業一覧からStatusを読むことで作業一覧を確認し・実行間隔より短いFROM/Tを防ぐ。 ✅
    - B. 運用時に利用する技術的役割は検査状態からLastResponseを読ことで検査状態を確認し・Inspectionを防ぐ。
    - C. 運用時に利用する技術的役割は点検操作で判定欄を記録することでジョブキューを確認し・照会文動詞集計の期間誤りを防ぐ。
    - D. 運用時に利用する技術的役割は変更確認操作で採取欄を棚卸することでGuardAを確認し・ディレクトリー取込対象の誤りを防ぐ。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能作業一・実行間でAの記述「Audit Processで作業一覧から Status」に対応する項目は世代整合の確認 AUDIT17（Aud・作業一・世代整）です。照合作業一・世代整に関する監査プロセスの仕様は「Audit Processで作業一覧から Status を読み」で、確認対象は作業一・世代整・実行間です。運用世代整・AudでB:のログとの照合 IE07は「Inspection Engineで検査状態」を述べるため、正答側の照合軸は作業一・監査プ・世代整です。項目作業一・世代整でC:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は実行間・監査プ・作業一です。仕様作業一・世代整でD:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は世代整・実行間・作業一です。用語作業一・世代整という用語は「Audit Processで作業一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・作業一・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 世代整合の確認 AUDIT17**

    - 検証目的: 監査プロセスのAudit Process Builderについて世代差を検出し、AUDIT17のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT17と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT17の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT17 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT17の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT17のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT17 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Status が画面・出力に表示されること
    ② ステップ2 の audit が画面・出力に表示されること
    ③ ステップ3 の Schedule が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 代替経路の確認 AUDIT10 {#c10-i0523}
*分類: 監査プロセス*  ・  難易度: 初級

代替経路の確認では 監査プロセス の プロセス一覧 を主操作として AUDIT10 を判定します。主経路との役割差への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT10 に残します。代替経路の確認を補助する 作業一覧 では Status を補助値として AUDIT10 へ保存します。主判定の代替経路の確認では監査プロセスの プロセス一覧 から Schedule を読み AUDIT10 へ残します。証跡照合の代替経路の確認では監査プロセスの Schedule と Status を AUDIT10 に保存します。記録対応の代替経路の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT10 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 代替経路の確認 AUDIT10に関する障害切り分けの前提を確認しています。Aggregator Guardium Aggregator 引継ぎ記録 AGG09の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はAggregで保持設定を証跡に残し・Aggregatorで保持設定から drop_ad_hoc_。
    - B. 障害切り分けに用いる役割は移行で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。
    - C. 障害切り分けに用いる役割は解除で最終応答を証跡に残し・監視エージェントの最終応答と取得時刻を記録し。
    - D. 障害切り分けに用いる役割は代替経路確認でプロセス一覧を証跡に残し・Audit Processでプロセス一覧から。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能プロセ・実行間でDの記述「Audit Processでプロセス一覧から」に対応する項目は代替経路の確認 AUDIT10（Aud・プロセ・代替経）です。照合プロセ・代替経に関する監査プロセスの仕様は「Audit Processでプロセス一覧から Schedule」で、確認対象はプロセ・代替経・実行間です。比較監査プ・代替経でA:の引継ぎ記録 AGG09は「Aggregatorで保持設定から」を述べるため、正答側の照合軸はAud・代替経・プロセです。運用代替経・AudでB:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸はプロセ・監査プ・代替経です。項目プロセ・代替経でC:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は実行間・監査プ・プロセです。用語プロセ・代替経という用語は「Audit Processでプロセス一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・プロセ・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 代替経路の確認 AUDIT10**

    - 検証目的: 監査プロセスのAudit Process Builderについて代替手段の成立を確認し、AUDIT10のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT10のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT10 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT10の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT10 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT10の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Schedule が画面・出力に表示されること
    ② ステップ2 の Status が画面・出力に表示されること
    ③ ステップ3 の audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 依存関係の確認 AUDIT13 {#c10-i0524}
*分類: 監査プロセス*  ・  難易度: 初級

依存関係の確認では 監査プロセス の プロセス一覧 を主操作として AUDIT13 を判定します。前提資源と後続処理の順序への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT13 に残します。依存関係の確認を補助する 作業一覧 では Status を補助値として AUDIT13 へ保存します。主判定の依存関係の確認では監査プロセスの プロセス一覧 から Schedule を読み AUDIT13 へ残します。証跡照合の依存関係の確認では監査プロセスの Schedule と Status を AUDIT13 に保存します。記録対応の依存関係の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT13 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査プロセス Audit Process Builder 依存関係の確認 AUDIT13」を「Aggregator Guardium Aggregator 変更前の確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は変更確認で監査タスクを証跡に残し・Aggregatorで監査タスクから。
    - B. 仕様上の役割は変更でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。
    - C. 仕様上の役割は照合でカーネル監視を証跡に残し・監視エージェントのカーネル監視有無と取得時刻を記録し。
    - D. 仕様上の役割は依存関係確認でプロセス一覧を証跡に残し・Audit Processでプロセス一覧から。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能プロセ・実行間でDの記述「Audit Processでプロセス一覧から」に対応する項目は依存関係の確認 AUDIT13（Aud・プロセ・依存関）です。照合プロセ・依存関に関する監査プロセスの仕様は「Audit Processでプロセス一覧から Schedule」で、確認対象はプロセ・依存関・実行間です。比較監査プ・依存関でA:の変更前の確認 AGG02は「Aggregatorで監査タスクから」を述べるため、正答側の照合軸はAud・依存関・プロセです。運用依存関・AudでB:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸はプロセ・監査プ・依存関です。項目プロセ・依存関でC:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は実行間・監査プ・プロセです。用語プロセ・依存関という用語は「Audit Processでプロセス一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・プロセ・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 依存関係の確認 AUDIT13**

    - 検証目的: 監査プロセスのAudit Process Builderについて依存資源を点検し、AUDIT13のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT13のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT13 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT13の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT13 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT13の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Schedule が画面・出力に表示されること
    ② ステップ2 の Status が画面・出力に表示されること
    ③ ステップ3 の audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 保守後の確認 AUDIT20 {#c10-i0525}
*分類: 監査プロセス*  ・  難易度: 初級

保守後の確認では 監査プロセス の 作業一覧 を主操作として AUDIT20 を判定します。有効化された定義と版数への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT20 に残します。保守後の確認を補助する 報告上限 では max_audit_reporting を補助値として AUDIT20 へ保存します。主判定の保守後の確認では監査プロセスの 作業一覧 から Status を読み AUDIT20 へ残します。証跡照合の保守後の確認では監査プロセスの Status と max_audit_reporting を AUDIT20 に保存します。記録対応の保守後の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT20 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 保守後の確認 AUDIT20を同一分類のAggregator Guardium Aggregator 復旧後の確認と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は復旧確認で保持設定を証跡に残し・Aggregatorで保持設定から drop_ad_hoc_。
    - B. 構成を確認する際の意味は移行でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。
    - C. 構成を確認する際の意味は保守確認で作業一覧を証跡に残し・Audit Processで作業一覧から Status。 ✅
    - D. 構成を確認する際の意味は解析でロール割当を証跡に残し・Login Nameのロール割当と取得時刻を記録し。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能作業一・実行間でCの記述「Audit Processで作業一覧から Status」に対応する項目は保守後の確認 AUDIT20（Aud・作業一・保守確）です。照合作業一・保守確に関する監査プロセスの仕様は「Audit Processで作業一覧から Status を読み」で、確認対象は作業一・保守確・実行間です。比較監査プ・保守確でA:の復旧後の確認 AGG06は「Aggregatorで保持設定から」を述べるため、正答側の照合軸はAud・保守確・作業一です。運用保守確・AudでB:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は作業一・監査プ・保守確です。仕様作業一・保守確でD:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は保守確・実行間・作業一です。用語作業一・保守確という用語は「Audit Processで作業一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・作業一・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 保守後の確認 AUDIT20**

    - 検証目的: 監査プロセスのAudit Process Builderについて保守反映を検証し、AUDIT20のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT20と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT20の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT20 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT20の対応を確認します。有効化された定義と版数を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT20の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT20の対応を確認します。有効化された定義と版数を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT20のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT20 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT20の対応を確認します。有効化された定義と版数を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Status が画面・出力に表示されること
    ② ステップ2 の audit が画面・出力に表示されること
    ③ ステップ3 の Schedule が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 停止前の確認 AUDIT14 {#c10-i0526}
*分類: 監査プロセス*  ・  難易度: 初級

停止前の確認では 監査プロセス の 作業一覧 を主操作として AUDIT14 を判定します。処理中資源と未完了要求への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT14 に残します。停止前の確認を補助する 報告上限 では max_audit_reporting を補助値として AUDIT14 へ保存します。主判定の停止前の確認では監査プロセスの 作業一覧 から Status を読み AUDIT14 へ残します。証跡照合の停止前の確認では監査プロセスの Status と max_audit_reporting を AUDIT14 に保存します。記録対応の停止前の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT14 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 停止前の確認 AUDIT14の役割を調べています。監査プロセス Audit Process Builder 監査証跡の保存の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはAudit Processで報告上限から max_audit_reporting を読みである。報告上限からmax_audit_reときは実行間隔より短いFROM/Tを防ぐ。
    - B. 機能の説明としてはLogin Nameのロール割当と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。
    - C. 機能の説明としてはRoleのディレクトリー取込と取得時刻を記録し・GuardAPI実行権限不足を防ぐである。監査操作で記録欄を比較するときはGuardAPI実行権限不足を防ぐ。
    - D. 機能の説明としてはAudit Processで作業一覧から Status を読み・Status とである。作業一覧からStatusを読むときは実行間隔より短いFROM/Tを防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能作業一・実行間でDの記述「Audit Processで作業一覧から Status」に対応する項目は停止前の確認 AUDIT14（Aud・作業一・停止確）です。照合作業一・停止確に関する監査プロセスの仕様は「Audit Processで作業一覧から Status を読み」で、確認対象は作業一・停止確・実行間です。比較監査プ・停止確でA:の監査証跡の保存 AUDIT18は「Audit Processで報告上限から」を述べるため、正答側の照合軸はAud・停止確・作業一です。運用停止確・AudでB:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は作業一・監査プ・停止確です。項目作業一・停止確でC:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は実行間・監査プ・作業一です。用語作業一・停止確という用語は「Audit Processで作業一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・作業一・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 停止前の確認 AUDIT14**

    - 検証目的: 監査プロセスのAudit Process Builderについて安全な停止条件を確認し、AUDIT14のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT14の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT14 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT14の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT14のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT14 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Status が画面・出力に表示されること
    ② ステップ2 の audit が画面・出力に表示されること
    ③ ステップ3 の Schedule が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 再始動後の確認 AUDIT15 {#c10-i0527}
*分類: 監査プロセス*  ・  難易度: 初級

再始動後の確認では 監査プロセス の 報告上限 を主操作として AUDIT15 を判定します。再開点と未処理データへの注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT15 に残します。再始動後の確認を補助する プロセス一覧 では Schedule を補助値として AUDIT15 へ保存します。主判定の再始動後の確認では監査プロセスの 報告上限 から max_audit_reporting を読み AUDIT15 へ残します。証跡照合の再始動後の確認では監査プロセスの max_audit_reporting と Schedule を AUDIT15 に保存します。記録対応の再始動後の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT15 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 再始動後の確認 AUDIT15について構成や状態を確認します。Central Manager 中央管理サーバー 監査証跡の保存 CM18ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは監査証跡の保で監査証跡の保を確認することで監査証跡の保を確認し・managed unitからを防ぐ。
    - B. 対象資源に対する働きは照合操作で確認欄を採取することでロール割当を確認し・監査担当者の閲覧範囲不足を防ぐ。
    - C. 対象資源に対する働きは確認操作で状態欄を整理することで最終応答を確認し・最終応答停止の見落としを防ぐ。
    - D. 対象資源に対する働きは報告上限からmax_audit_repoことで報告上限を確認し・実行間隔より短いFROM/Tを防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能報告上・実行間でDの記述「Audit Processで報告上限から」に対応する項目は再始動後の確認 AUDIT15（Aud・報告上・再始動）です。照合報告上・再始動に関する監査プロセスの仕様は「Audit Processで報告上限から」で、確認対象は報告上・再始動・実行間です。比較監査プ・再始動でA:の監査証跡の保存 CM18は「Central ManagerでCentra」を述べるため、正答側の照合軸はAud・再始動・報告上です。運用再始動・AudでB:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は報告上・監査プ・再始動です。項目報告上・再始動でC:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は実行間・監査プ・報告上です。用語報告上・再始動という用語は「Audit Processで報告上限から」を指し、照合する値と誤認リスクの組合せは監査プ・報告上・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 再始動後の確認 AUDIT15**

    - 検証目的: 監査プロセスのAudit Process Builderについて再始動結果を検証し、AUDIT15のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT15の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT15のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT15 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT15の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT15 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の audit が画面・出力に表示されること
    ② ステップ2 の Schedule が画面・出力に表示されること
    ③ ステップ3 の Status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 変更前の確認 AUDIT02 {#c10-i0528}
*分類: 監査プロセス*  ・  難易度: 初級

変更前の確認では 監査プロセス の 作業一覧 を主操作として AUDIT02 を判定します。変更対象と非対象の境界への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT02 に残します。変更前の確認を補助する 報告上限 では max_audit_reporting を補助値として AUDIT02 へ保存します。主判定の変更前の確認では監査プロセスの 作業一覧 から Status を読み AUDIT02 へ残します。証跡照合の変更前の確認では監査プロセスの Status と max_audit_reporting を AUDIT02 に保存します。記録対応の変更前の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT02 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 変更前の確認 AUDIT02に関する障害切り分けの前提を確認しています。ポリシー・検査エンジン Inspection Engine 引継ぎ記録 IE09の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはInspectionを避けるため・エージェント変更からInspectionしてエージェントを照合する。
    - B. 機能の説明としては実行間隔より短いFROM/TO範を避けるため・作業一覧からStatusを読むして作業一覧を照合する。 ✅
    - C. 機能の説明としては監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するしてディレクトリを照合する。
    - D. 機能の説明としては最終応答停止の見落としを避けるため・確認操作で状態欄を整理するして承認クライアを照合する。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能作業一・実行間でBの記述「Audit Processで作業一覧から Status」に対応する項目は変更前の確認 AUDIT02（Aud・作業一・変更確）です。照合作業一・変更確に関する監査プロセスの仕様は「Audit Processで作業一覧から Status を読み」で、確認対象は作業一・変更確・実行間です。比較監査プ・変更確でA:の引継ぎ記録 IE09は「Inspection Engineでエージェ」を述べるため、正答側の照合軸はAud・変更確・作業一です。項目作業一・変更確でC:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は実行間・監査プ・作業一です。仕様作業一・変更確でD:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は変更確・実行間・作業一です。用語作業一・変更確という用語は「Audit Processで作業一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・作業一・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 変更前の確認 AUDIT02**

    - 検証目的: 監査プロセスのAudit Process Builderについて変更前の証跡を保存し、AUDIT02のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT02の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT02 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT02の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT02のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT02 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Status が画面・出力に表示されること
    ② ステップ2 の audit が画面・出力に表示されること
    ③ ステップ3 の Schedule が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 変更後の確認 AUDIT03 {#c10-i0529}
*分類: 監査プロセス*  ・  難易度: 初級

変更後の確認では 監査プロセス の 報告上限 を主操作として AUDIT03 を判定します。反映値と残存値への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT03 に残します。変更後の確認を補助する プロセス一覧 では Schedule を補助値として AUDIT03 へ保存します。主判定の変更後の確認では監査プロセスの 報告上限 から max_audit_reporting を読み AUDIT03 へ残します。証跡照合の変更後の確認では監査プロセスの max_audit_reporting と Schedule を AUDIT03 に保存します。記録対応の変更後の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT03 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 変更後の確認 AUDIT03の設定や表示を読む前に役割を確認します。Central Manager 中央管理サーバー 復旧後の確認 CM06ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは復旧確認で復旧後の確認を証跡に残し・Central ManagerでCentral。
    - B. 対象資源に対する働きは変更確認で報告上限を証跡に残し・Audit Processで報告上限から。 ✅
    - C. 対象資源に対する働きは保守でジョブキューを証跡に残し・照会文 Verbのジョブキューと取得時刻を記録し。
    - D. 対象資源に対する働きは抑止で承認クライアを証跡に残し・監視エージェントの承認クライアントと取得時刻を記録し。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能報告上・実行間でBの記述「Audit Processで報告上限から」に対応する項目は変更後の確認 AUDIT03（Aud・報告上・変更確）です。照合報告上・変更確に関する監査プロセスの仕様は「Audit Processで報告上限から」で、確認対象は報告上・変更確・実行間です。比較監査プ・変更確でA:の復旧後の確認 CM06は「Central ManagerでCentra」を述べるため、正答側の照合軸はAud・変更確・報告上です。項目報告上・変更確でC:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は実行間・監査プ・報告上です。仕様報告上・変更確でD:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は変更確・実行間・報告上です。用語報告上・変更確という用語は「Audit Processで報告上限から」を指し、照合する値と誤認リスクの組合せは監査プ・報告上・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 変更後の確認 AUDIT03**

    - 検証目的: 監査プロセスのAudit Process Builderについて変更結果を検証し、AUDIT03のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT03の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT03のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT03 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT03の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT03 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の audit が画面・出力に表示されること
    ② ステップ2 の Schedule が画面・出力に表示されること
    ③ ステップ3 の Status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 容量余力の確認 AUDIT16 {#c10-i0530}
*分類: 監査プロセス*  ・  難易度: 初級

容量余力の確認では 監査プロセス の プロセス一覧 を主操作として AUDIT16 を判定します。使用量と警告しきい値への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT16 に残します。容量余力の確認を補助する 作業一覧 では Status を補助値として AUDIT16 へ保存します。主判定の容量余力の確認では監査プロセスの プロセス一覧 から Schedule を読み AUDIT16 へ残します。証跡照合の容量余力の確認では監査プロセスの Schedule と Status を AUDIT16 に保存します。記録対応の容量余力の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT16 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 容量余力の確認 AUDIT16の技術的な意味を資料で確認するとき、Aggregator Guardium Aggregator 構成監査 AGG08との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は監査タスクからAdHocデータベースを読ことで監査タスクを確認し・集約遅延中の期間を監査完了とを防ぐ。
    - B. コマンドまたは機能の用途はプロセス一覧からScheduleを読むことでプロセス一覧を確認し・実行間隔より短いFROM/Tを防ぐ。 ✅
    - C. コマンドまたは機能の用途は記録操作で証跡欄を照合することで最終応答を確認し・未承認監視エージェント接続を防ぐ。
    - D. コマンドまたは機能の用途は監査操作で記録欄を比較することでユーザー有効を確認し・GuardAPI実行権限不足を防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能プロセ・実行間でBの記述「Audit Processでプロセス一覧から」に対応する項目は容量余力の確認 AUDIT16（Aud・プロセ・容量余）です。照合プロセ・容量余に関する監査プロセスの仕様は「Audit Processでプロセス一覧から Schedule」で、確認対象はプロセ・容量余・実行間です。比較監査プ・容量余でA:の構成監査 AGG08は「Aggregatorで監査タスクから」を述べるため、正答側の照合軸はAud・容量余・プロセです。項目プロセ・容量余でC:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は実行間・監査プ・プロセです。仕様プロセ・容量余でD:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は容量余・実行間・プロセです。用語プロセ・容量余という用語は「Audit Processでプロセス一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・プロセ・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 容量余力の確認 AUDIT16**

    - 検証目的: 監査プロセスのAudit Process Builderについて容量枯渇を予防し、AUDIT16のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT16と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT16のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT16 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT16の対応を確認します。使用量と警告しきい値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT16の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT16 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT16の対応を確認します。使用量と警告しきい値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT16の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT16の対応を確認します。使用量と警告しきい値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Schedule が画面・出力に表示されること
    ② ステップ2 の Status が画面・出力に表示されること
    ③ ステップ3 の audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 引継ぎ記録 AUDIT09 {#c10-i0531}
*分類: 監査プロセス*  ・  難易度: 初級

引継ぎ記録では 監査プロセス の 報告上限 を主操作として AUDIT09 を判定します。次担当者が追跡できる証跡への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT09 に残します。引継ぎ記録を補助する プロセス一覧 では Schedule を補助値として AUDIT09 へ保存します。主判定の引継ぎ記録では監査プロセスの 報告上限 から max_audit_reporting を読み AUDIT09 へ残します。証跡照合の引継ぎ記録では監査プロセスの max_audit_reporting と Schedule を AUDIT09 に保存します。記録対応の引継ぎ記録では監査プロセスの ScheduleとTask Status の証跡へ AUDIT09 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 引継ぎ記録 AUDIT09を保守記録に説明する必要があります。Central Manager 中央管理サーバー 復旧準備 CM05と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は報告上限からmax_audit_repoことで報告上限を確認し・実行間隔より短いFROM/Tを防ぐ。 ✅
    - B. 保守作業で参照する機能は復旧準備で復旧準備ではを確認することで復旧準備ではを確認し・managed unitからを防ぐ。
    - C. 保守作業で参照する機能は監査操作で記録欄を比較することで表示可能レポを確認し・GuardAPI実行権限不足を防ぐ。
    - D. 保守作業で参照する機能は調査操作で保守欄を引き継ぎすることで照会文動詞集を確認し・対象データソースの取り違えを防ぐ。監査レポート DB User Name 0284固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能報告上・実行間でAの記述「Audit Processで報告上限から」に対応する項目は引継ぎ記録 AUDIT09（Aud・報告上・監査プ）です。照合報告上・監査プに関する監査プロセスの仕様は「Audit Processで報告上限から」で、確認対象は報告上・監査プ・実行間です。運用監査プ・AudでB:の復旧準備 CM05は「Central Managerで復旧準備では」を述べるため、正答側の照合軸は報告上・監査プ・監査プです。項目報告上・監査プでC:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸は実行間・監査プ・報告上です。仕様報告上・監査プでD:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は監査プ・実行間・報告上です。用語報告上・監査プという用語は「Audit Processで報告上限から」を指し、照合する値と誤認リスクの組合せは監査プ・報告上・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 引継ぎ記録 AUDIT09**

    - 検証目的: 監査プロセスのAudit Process Builderについて再現可能な記録を作成し、AUDIT09のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT09の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT09のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT09 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT09の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT09 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の audit が画面・出力に表示されること
    ② ステップ2 の Schedule が画面・出力に表示されること
    ③ ステップ3 の Status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 復旧後の確認 AUDIT06 {#c10-i0532}
*分類: 監査プロセス*  ・  難易度: 初級

復旧後の確認では 監査プロセス の 報告上限 を主操作として AUDIT06 を判定します。再発していないことを示す値への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT06 に残します。復旧後の確認を補助する プロセス一覧 では Schedule を補助値として AUDIT06 へ保存します。主判定の復旧後の確認では監査プロセスの 報告上限 から max_audit_reporting を読み AUDIT06 へ残します。証跡照合の復旧後の確認では監査プロセスの max_audit_reporting と Schedule を AUDIT06 に保存します。記録対応の復旧後の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT06 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 復旧後の確認 AUDIT06の役割を調べています。Central Manager 中央管理サーバー 変更前の確認 CM02の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はmanaged unitからのデを避けるため・変更確認で変更前の確認を確認するして変更前の確認を照合する。
    - B. 表示や設定で扱う内容は照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するしてジョブキューを照合する。
    - C. 表示や設定で扱う内容は未承認監視エージェント接続を避けるため・記録操作で証跡欄を照合するして最終応答を照合する。S-TAP監視 S-TAP Host 0301固有の属性も確認対象に含める。
    - D. 表示や設定で扱う内容は実行間隔より短いFROM/TO範を避けるため・報告上限からmax_audit_repoして報告上限を照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能報告上・実行間でDの記述「Audit Processで報告上限から」に対応する項目は復旧後の確認 AUDIT06（Aud・報告上・復旧確）です。照合報告上・復旧確に関する監査プロセスの仕様は「Audit Processで報告上限から」で、確認対象は報告上・復旧確・実行間です。比較監査プ・復旧確でA:の変更前の確認 CM02は「Central Managerで変更前の確認」を述べるため、正答側の照合軸はAud・復旧確・報告上です。運用復旧確・AudでB:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は報告上・監査プ・復旧確です。項目報告上・復旧確でC:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は実行間・監査プ・報告上です。用語報告上・復旧確という用語は「Audit Processで報告上限から」を指し、照合する値と誤認リスクの組合せは監査プ・報告上・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 復旧後の確認 AUDIT06**

    - 検証目的: 監査プロセスのAudit Process Builderについて復旧後の安定性を確認し、AUDIT06のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT06の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT06のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT06 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT06の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT06 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の audit が画面・出力に表示されること
    ② ステップ2 の Schedule が画面・出力に表示されること
    ③ ステップ3 の Status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 復旧準備 AUDIT05 {#c10-i0533}
*分類: 監査プロセス*  ・  難易度: 初級

復旧準備では 監査プロセス の 作業一覧 を主操作として AUDIT05 を判定します。再開前に必要な整合性への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT05 に残します。復旧準備を補助する 報告上限 では max_audit_reporting を補助値として AUDIT05 へ保存します。主判定の復旧準備では監査プロセスの 作業一覧 から Status を読み AUDIT05 へ残します。証跡照合の復旧準備では監査プロセスの Status と max_audit_reporting を AUDIT05 に保存します。記録対応の復旧準備では監査プロセスの ScheduleとTask Status の証跡へ AUDIT05 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査プロセス Audit Process Builder 復旧準備 AUDIT05」を「データソース管理 Guardiumデータソース 変更前の確認 DSRC02」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は変更確認で参照箇所を証跡に残し・Guardiumで参照箇所から UsedBy を読み。
    - B. 運用時に利用する技術的役割は移行で最終応答を証跡に残し・監視エージェントの最終応答と取得時刻を記録し。
    - C. 運用時に利用する技術的役割は復旧準備で作業一覧を証跡に残し・Audit Processで作業一覧から Status。 ✅
    - D. 運用時に利用する技術的役割は抑止で暗号化表示を証跡に残し・監視エージェントの暗号化表示と取得時刻を記録し。S-TAP監視 S-TAP Version 0283固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能作業一・実行間でCの記述「Audit Processで作業一覧から Status」に対応する項目は復旧準備 AUDIT05（Aud・作業一・復旧準）です。照合作業一・復旧準に関する監査プロセスの仕様は「Audit Processで作業一覧から Status を読み」で、確認対象は作業一・復旧準・実行間です。比較監査プ・復旧準でA:の変更前の確認 DSRC02は「Guardiumで参照箇所から」を述べるため、正答側の照合軸はAud・復旧準・作業一です。運用復旧準・AudでB:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は作業一・監査プ・復旧準です。仕様作業一・復旧準でD:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は復旧準・実行間・作業一です。用語作業一・復旧準という用語は「Audit Processで作業一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・作業一・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 復旧準備 AUDIT05**

    - 検証目的: 監査プロセスのAudit Process Builderについて復旧条件を確認し、AUDIT05のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT05の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT05 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT05の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT05のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT05 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Status が画面・出力に表示されること
    ② ステップ2 の audit が画面・出力に表示されること
    ③ ステップ3 の Schedule が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 性能影響の確認 AUDIT11 {#c10-i0534}
*分類: 監査プロセス*  ・  難易度: 初級

性能影響の確認では 監査プロセス の 作業一覧 を主操作として AUDIT11 を判定します。処理時間と滞留箇所への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT11 に残します。性能影響の確認を補助する 報告上限 では max_audit_reporting を補助値として AUDIT11 へ保存します。主判定の性能影響の確認では監査プロセスの 作業一覧 から Status を読み AUDIT11 へ残します。証跡照合の性能影響の確認では監査プロセスの Status と max_audit_reporting を AUDIT11 に保存します。記録対応の性能影響の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT11 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 性能影響の確認 AUDIT11の設定や表示を読む前に役割を確認します。ポリシー・検査エンジン Inspection Engine 権限境界の確認 IE12ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはInspection Engineでエージェント変更から InspectionEngine を読みである。エージェント変更からInspectiときはInspectionを防ぐ。
    - B. 状態を読み取るための働きは監視エージェントのカーネル監視有無と取得時刻を記録し・未承認監視エージェント接続を防ぐである。記録操作で証跡欄を照合するときは未承認監視エージェント接続を防ぐ。
    - C. 状態を読み取るための働きはAudit Processで作業一覧から Status を読み・Status とである。作業一覧からStatusを読むときは実行間隔より短いFROM/Tを防ぐ。 ✅
    - D. 状態を読み取るための働きはデータベース User Nameの照会文動詞集計と取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能作業一・実行間でCの記述「Audit Processで作業一覧から Status」に対応する項目は性能影響の確認 AUDIT11（Aud・作業一・性能影）です。照合作業一・性能影に関する監査プロセスの仕様は「Audit Processで作業一覧から Status を読み」で、確認対象は作業一・性能影・実行間です。比較監査プ・性能影でA:の権限境界の確認 IE12は「Inspection Engineでエージェ」を述べるため、正答側の照合軸はAud・性能影・作業一です。運用性能影・AudでB:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は作業一・監査プ・性能影です。仕様作業一・性能影でD:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は性能影・実行間・作業一です。用語作業一・性能影という用語は「Audit Processで作業一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・作業一・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 性能影響の確認 AUDIT11**

    - 検証目的: 監査プロセスのAudit Process Builderについて負荷と待ちを確認し、AUDIT11のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT11の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT11 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT11の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT11のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT11 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Status が画面・出力に表示されること
    ② ステップ2 の audit が画面・出力に表示されること
    ③ ステップ3 の Schedule が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 構成監査 AUDIT08 {#c10-i0535}
*分類: 監査プロセス*  ・  難易度: 初級

構成監査では 監査プロセス の 作業一覧 を主操作として AUDIT08 を判定します。定義値と稼働値の一致への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT08 に残します。構成監査を補助する 報告上限 では max_audit_reporting を補助値として AUDIT08 へ保存します。主判定の構成監査では監査プロセスの 作業一覧 から Status を読み AUDIT08 へ残します。証跡照合の構成監査では監査プロセスの Status と max_audit_reporting を AUDIT08 に保存します。記録対応の構成監査では監査プロセスの ScheduleとTask Status の証跡へ AUDIT08 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 構成監査 AUDIT08の技術的な意味を資料で確認するとき、アプライアンス健全性 Appliance Monitoring 復旧準備 APP05との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はDB処理一覧からTURBINEを読むことでデータベースを確認し・ディスク逼迫中に検査データ流を防ぐ。
    - B. 構成を確認する際の意味は作業一覧からStatusを読むことで作業一覧を確認し・実行間隔より短いFROM/Tを防ぐ。 ✅
    - C. 構成を確認する際の意味は表示操作で対象欄を追跡することでユーザー活動を確認し・ジョブ失敗の見落としを防ぐ。
    - D. 構成を確認する際の意味は採取操作で照合欄を点検することでカーネル監視を確認し・カーネル監視導入状態の誤読を防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能作業一・実行間でBの記述「Audit Processで作業一覧から Status」に対応する項目は構成監査 AUDIT08（Aud・作業一・構成監）です。照合作業一・構成監に関する監査プロセスの仕様は「Audit Processで作業一覧から Status を読み」で、確認対象は作業一・構成監・実行間です。比較監査プ・構成監でA:の復旧準備 APP05は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸はAud・構成監・作業一です。項目作業一・構成監でC:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は実行間・監査プ・作業一です。仕様作業一・構成監でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は構成監・実行間・作業一です。用語作業一・構成監という用語は「Audit Processで作業一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・作業一・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 構成監査 AUDIT08**

    - 検証目的: 監査プロセスのAudit Process Builderについて構成差分を監査し、AUDIT08のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT08の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT08 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT08の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT08のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT08 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Status が画面・出力に表示されること
    ② ステップ2 の audit が画面・出力に表示されること
    ③ ステップ3 の Schedule が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 権限境界の確認 AUDIT12 {#c10-i0536}
*分類: 監査プロセス*  ・  難易度: 初級

権限境界の確認では 監査プロセス の 報告上限 を主操作として AUDIT12 を判定します。参照操作と変更操作の分離への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT12 に残します。権限境界の確認を補助する プロセス一覧 では Schedule を補助値として AUDIT12 へ保存します。主判定の権限境界の確認では監査プロセスの 報告上限 から max_audit_reporting を読み AUDIT12 へ残します。証跡照合の権限境界の確認では監査プロセスの max_audit_reporting と Schedule を AUDIT12 に保存します。記録対応の権限境界の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT12 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 権限境界の確認 AUDIT12を同一分類のデータソース管理 Guardiumデータソース 性能影響の確認 DSRC11と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は参照箇所からUsedByを読むことで参照箇所を確認し・廃止サーバーの参照を残して監を防ぐ。
    - B. 管理対象との関係を表す説明は点検操作で判定欄を記録することでジョブキューを確認し・照会文動詞集計の期間誤りを防ぐ。監査レポート SQL Verb 0086固有の属性も確認対象に含める。
    - C. 管理対象との関係を表す説明は報告上限からmax_audit_repoことで報告上限を確認し・実行間隔より短いFROM/Tを防ぐ。 ✅
    - D. 管理対象との関係を表す説明は主操作で出力欄を評価することで表示可能レポを確認し・過剰ロール付与を防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能報告上・実行間でCの記述「Audit Processで報告上限から」に対応する項目は権限境界の確認 AUDIT12（Aud・報告上・権限境）です。照合報告上・権限境に関する監査プロセスの仕様は「Audit Processで報告上限から」で、確認対象は報告上・権限境・実行間です。比較監査プ・権限境でA:の性能影響の確認 DSRC11は「Guardiumで参照箇所から」を述べるため、正答側の照合軸はAud・権限境・報告上です。運用権限境・AudでB:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は報告上・監査プ・権限境です。仕様報告上・権限境でD:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸は権限境・実行間・報告上です。用語報告上・権限境という用語は「Audit Processで報告上限から」を指し、照合する値と誤認リスクの組合せは監査プ・報告上・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 権限境界の確認 AUDIT12**

    - 検証目的: 監査プロセスのAudit Process Builderについて実行権限を点検し、AUDIT12のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT12の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT12のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT12 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT12の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT12 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の audit が画面・出力に表示されること
    ② ステップ2 の Schedule が画面・出力に表示されること
    ③ ステップ3 の Status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 異常終了後の確認 AUDIT19 {#c10-i0537}
*分類: 監査プロセス*  ・  難易度: 初級

異常終了後の確認では 監査プロセス の プロセス一覧 を主操作として AUDIT19 を判定します。未完了処理と再実行条件への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT19 に残します。異常終了後の確認を補助する 作業一覧 では Status を補助値として AUDIT19 へ保存します。主判定の異常終了後の確認では監査プロセスの プロセス一覧 から Schedule を読み AUDIT19 へ残します。証跡照合の異常終了後の確認では監査プロセスの Schedule と Status を AUDIT19 に保存します。記録対応の異常終了後の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT19 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 異常終了後の確認 AUDIT19の設定や表示を読む前に役割を確認します。アプライアンス健全性 Appliance Monitoring 変更後の確認ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はAppliance Monitoriでジョブキューから JobName を読み・JobName とである。ジョブキューからJobNameを読むときはディスク逼迫中に検査データ流を防ぐ。
    - B. 一次資料が示す主目的は照会文 Verbのジョブキューと取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。
    - C. 一次資料が示す主目的は監視エージェントのカーネル監視有無と取得時刻を記録し・ローカル通信制御監視の未確認を防ぐである。保守操作で監査欄を保存するときはローカル通信制御監視の未確認を防ぐ。S-TAP監視 Last Response 0292固有の属性も確認対象に含める。
    - D. 一次資料が示す主目的はAudit Processでプロセス一覧から Schedule を読み・Schedule と Statusである。プロセス一覧からScheduleを読ときは実行間隔より短いFROM/Tを防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能プロセ・実行間でDの記述「Audit Processでプロセス一覧から」に対応する項目は異常終了後の確認 AUDIT19（Aud・プロセ・異常終）です。照合プロセ・異常終に関する監査プロセスの仕様は「Audit Processでプロセス一覧から Schedule」で、確認対象はプロセ・異常終・実行間です。比較監査プ・異常終でA:の変更後の確認 APP03は「Appliance Monitoriでジョブ」を述べるため、正答側の照合軸はAud・異常終・プロセです。運用異常終・AudでB:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はプロセ・監査プ・異常終です。項目プロセ・異常終でC:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は実行間・監査プ・プロセです。用語プロセ・異常終という用語は「Audit Processでプロセス一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・プロセ・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 異常終了後の確認 AUDIT19**

    - 検証目的: 監査プロセスのAudit Process Builderについて異常終了の影響を限定し、AUDIT19のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT19と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT19のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT19 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT19の対応を確認します。未完了処理と再実行条件を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT19の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT19 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT19の対応を確認します。未完了処理と再実行条件を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT19の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT19の対応を確認します。未完了処理と再実行条件を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Schedule が画面・出力に表示されること
    ② ステップ2 の Status が画面・出力に表示されること
    ③ ステップ3 の audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 監査証跡の保存 AUDIT18 {#c10-i0538}
*分類: 監査プロセス*  ・  難易度: 初級

監査証跡の保存では 監査プロセス の 報告上限 を主操作として AUDIT18 を判定します。実行者と結果の対応への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT18 に残します。監査証跡の保存を補助する プロセス一覧 では Schedule を補助値として AUDIT18 へ保存します。主判定の監査証跡の保存では監査プロセスの 報告上限 から max_audit_reporting を読み AUDIT18 へ残します。証跡照合の監査証跡の保存では監査プロセスの max_audit_reporting と Schedule を AUDIT18 に保存します。記録対応の監査証跡の保存では監査プロセスの ScheduleとTask Status の証跡へ AUDIT18 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 監査証跡の保存 AUDIT18に関する障害切り分けの前提を確認しています。Central Manager 中央管理サーバー 異常終了後の確認 CM19の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は異常終了確認で確認では中央を確認することで確認では中央を確認し・managed unitからを防ぐ。
    - B. 表示や設定で扱う内容は報告上限からmax_audit_repoことで報告上限を確認し・実行間隔より短いFROM/Tを防ぐ。 ✅
    - C. 表示や設定で扱う内容は記録操作で証跡欄を照合することで最終応答を確認し・未承認監視エージェント接続を防ぐ。
    - D. 表示や設定で扱う内容は主操作で出力欄を評価することで表示可能レポを確認し・過剰ロール付与を防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能報告上・実行間でBの記述「Audit Processで報告上限から」に対応する項目は監査証跡の保存 AUDIT18（Aud・報告上・監査証）です。照合報告上・監査証に関する監査プロセスの仕様は「Audit Processで報告上限から」で、確認対象は報告上・監査証・実行間です。比較監査プ・監査証でA:の異常終了後の確認 CM19は「Central Managerで異常終了後の」を述べるため、正答側の照合軸はAud・監査証・報告上です。項目報告上・監査証でC:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は実行間・監査プ・報告上です。仕様報告上・監査証でD:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸は監査証・実行間・報告上です。用語報告上・監査証という用語は「Audit Processで報告上限から」を指し、照合する値と誤認リスクの組合せは監査プ・報告上・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 監査証跡の保存 AUDIT18**

    - 検証目的: 監査プロセスのAudit Process Builderについて監査可能な証跡を保存し、AUDIT18のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT18と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT18の報告上限を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> show max_audit_reporting
    → Enter を押す
    ```

    画面・出力:
    ```text
    max_audit_reporting = 500000 rows
    ```

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT18の対応を確認します。実行者と結果の対応を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT18のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT18 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT18の対応を確認します。実行者と結果の対応を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT18の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT18 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT18の対応を確認します。実行者と結果の対応を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の audit が画面・出力に表示されること
    ② ステップ2 の Schedule が画面・出力に表示されること
    ③ ステップ3 の Status が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


