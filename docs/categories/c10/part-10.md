---
search:
  exclude: true
---

# IBM Guardium Data Protection 12.x — 詳細 (10/12)

[← IBM Guardium Data Protection 12.x の概要へ戻る](index.md)


## IBM Guardium Data Protection 12.x > レポート

### 監査レポート DB User Name 0164 {#c10-i0439}
*分類: レポート*  ・  難易度: 中級

紅E切替0165ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紅E切替0165です。紅E切替0165は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録紅E切替0165です。紅E切替0165ではSQL動詞集計と取得時刻を採取票紅E切替0165へ残します。紅E切替0165では対象データソースの取り違えを避けるため補助資料も照合する判断紅E切替0165です。紅E切替0165の用語整理では監査レポートの対象値を実在出力で整理する記録紅E切替0165です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0164の技術的な意味を資料で確認するとき、ロールと権限 Role 0201との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は切替で照会文動詞集を証跡に残し・データベース User Nameの照会文動詞集計と取得時刻を。 ✅
    - B. 構成を確認する際の意味は登録でディレクトリを証跡に残し・Roleのディレクトリー取込と取得時刻を記録し。
    - C. 構成を確認する際の意味は状態確認でキュー状態を証跡に残し・監査結果のレビューと承認の履歴。sign-off trail 状態確認 キュー状態固有の属性も確認対象に含める。
    - D. 構成を確認する際の意味は巡回で最終応答を証跡に残し・監視エージェントの最終応答と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能照会文・対象デでAの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・切替）です。照合照会文・切替に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・切替・対象デです。運用切替・データでB:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は照会文・監査レ・切替です。項目照会文・切替でC:の状態確認 キュー状態は「監査結果のレビューと承認の履歴」を述べるため、正答側の照合軸は対象デ・監査レ・照会文です。仕様照会文・切替でD:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は切替・対象デ・照会文です。用語照会文・切替という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0164**

    - 検証目的: 監査レポートの監査レポート DB User Name 0164について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.54
    Server IP 198.51.100.64
    Count 54
    確認コード GDP12DD0164A
    ```

    画面・出力には GDP12DD0164A が表示され、監査レポート DB User Name 0164 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0164
    Process Type Report
    Status completed
    確認コード GDP12DD0164B
    ```

    画面・出力には GDP12DD0164B が表示され、監査レポート DB User Name 0164 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0164C
    ```

    画面・出力には GDP12DD0164C が表示され、監査レポート DB User Name 0164 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0164A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0164B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0164C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0179 {#c10-i0440}
*分類: レポート*  ・  難易度: 中級

空T切替0180ではIBM Guardium Data Protection 12.x の レポートを扱う採取票空T切替0180です。空T切替0180は監査レポートの表示操作で監査レポートの対象欄を追跡する記録空T切替0180です。空T切替0180ではSQL動詞集計と取得時刻を採取票空T切替0180へ残します。空T切替0180ではジョブ失敗の見落としを避けるため補助資料も照合する判断空T切替0180です。空T切替0180の用語整理では監査レポートの対象値を実在出力で照合する記録空T切替0180です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0179について構成や状態を確認します。S-TAP監視 S-TAP Host 0211ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは監視エージェントの最終応答と取得時刻を記録し・カーネル監視導入状態の誤読を防ぐである。採取操作で照合欄を点検するときはカーネル監視導入状態の誤読を防ぐ。
    - B. 状態を読み取るための働きはAudit Processでプロセス一覧から Schedule を読み・Schedule と Statusである。プロセス一覧からScheduleを読ときは実行間隔より短いFROM/Tを防ぐ。
    - C. 状態を読み取るための働きはLogin Nameのロール割当と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。
    - D. 状態を読み取るための働きはデータベース User Nameの照会文動詞集計と取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能照会文・ジョブでDの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・切替）です。照合照会文・切替に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・切替・ジョブです。比較監査レ・切替でA:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はデータ・切替・照会文です。運用切替・データでB:の容量余力の確認 AUDIT16は「Audit Processでプロセス一覧から」を述べるため、正答側の照合軸は照会文・監査レ・切替です。項目照会文・切替でC:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸はジョブ・監査レ・照会文です。用語照会文・切替という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0179**

    - 検証目的: 監査レポートの監査レポート DB User Name 0179について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.69
    Server IP 198.51.100.79
    Count 69
    確認コード GDP12DD0179A
    ```

    画面・出力には GDP12DD0179A が表示され、監査レポート DB User Name 0179 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0179
    Process Type Report
    Status completed
    確認コード GDP12DD0179B
    ```

    画面・出力には GDP12DD0179B が表示され、監査レポート DB User Name 0179 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0179C
    ```

    画面・出力には GDP12DD0179C が表示され、監査レポート DB User Name 0179 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0179A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0179B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0179C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0194 {#c10-i0441}
*分類: レポート*  ・  難易度: 中級

翠O収集0195ではIBM Guardium Data Protection 12.x の レポートを扱う採取票翠O収集0195です。翠O収集0195は監査レポートの点検操作で監査レポートの判定欄を記録する記録翠O収集0195です。翠O収集0195ではSQL動詞集計と取得時刻を採取票翠O収集0195へ残します。翠O収集0195ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断翠O収集0195です。翠O収集0195の用語整理では監査レポートの対象値を実在出力で保管する記録翠O収集0195です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0194の役割を調べています。ロールと権限 Role 0246の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては点検操作で判定欄を記録することで照会文動詞集を確認し・照会文動詞集計の期間誤りを防ぐ。 ✅
    - B. 機能の説明としては変更確認操作で採取欄を棚卸することでディレクトリを確認し・ディレクトリー取込対象の誤りを防ぐ。
    - C. 機能の説明としては承認履歴確認で初期同期を確認することで初期同期を確認し・初期同期の誤読を防ぐ。
    - D. 機能の説明としては採取操作で照合欄を点検することで暗号化表示を確認し・カーネル監視導入状態の誤読を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能照会文・照会文でAの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・収集）です。照合照会文・収集に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・収集・照会文です。運用収集・データでB:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は照会文・監査レ・収集です。項目照会文・収集でC:の承認履歴確認 初期同期は「接続を許可された S-TAP」を述べるため、正答側の照合軸は照会文・監査レ・照会文です。仕様照会文・収集でD:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は収集・照会文・照会文です。用語照会文・収集という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0194**

    - 検証目的: 監査レポートの監査レポート DB User Name 0194について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.84
    Server IP 198.51.100.34
    Count 84
    確認コード GDP12DD0194A
    ```

    画面・出力には GDP12DD0194A が表示され、監査レポート DB User Name 0194 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0194
    Process Type Report
    Status completed
    確認コード GDP12DD0194B
    ```

    画面・出力には GDP12DD0194B が表示され、監査レポート DB User Name 0194 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0194C
    ```

    画面・出力には GDP12DD0194C が表示され、監査レポート DB User Name 0194 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0194A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0194B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0194C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0209 {#c10-i0442}
*分類: レポート*  ・  難易度: 中級

朱J登録0210ではIBM Guardium Data Protection 12.x の レポートを扱う採取票朱J登録0210です。朱J登録0210は監査レポートの復旧操作で監査レポートの点検欄を確認する記録朱J登録0210です。朱J登録0210ではSQL動詞集計と取得時刻を採取票朱J登録0210へ残します。朱J登録0210では監査タスク未レビューを避けるため補助資料も照合する判断朱J登録0210です。朱J登録0210の用語整理では監査レポートの対象値を実在出力で点検する記録朱J登録0210です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート DB User Name 0209」を「S-TAP監視 DB Server Type 0295」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして承認クライアを照合する。
    - B. 運用時に利用する技術的役割はルール読替の誤読を避けるため・実行結果照合でルール読替を確認するしてルール読替を照合する。
    - C. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するして照会文動詞集を照合する。 ✅
    - D. 運用時に利用する技術的役割はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして最終応答を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能照会文・監査タでCの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・登録）です。照合照会文・登録に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・登録・監査タです。比較監査レ・登録でA:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はデータ・登録・照会文です。運用登録・データでB:の実行結果照合 ルール読替は「監視対象データベースやサービスを表す」を述べるため、正答側の照合軸は照会文・監査レ・登録です。仕様照会文・登録でD:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は登録・監査タ・照会文です。用語照会文・登録という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0209**

    - 検証目的: 監査レポートの監査レポート DB User Name 0209について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.19
    Server IP 198.51.100.49
    Count 99
    確認コード GDP12DD0209A
    ```

    画面・出力には GDP12DD0209A が表示され、監査レポート DB User Name 0209 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0209
    Process Type Report
    Status completed
    確認コード GDP12DD0209B
    ```

    画面・出力には GDP12DD0209B が表示され、監査レポート DB User Name 0209 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0209C
    ```

    画面・出力には GDP12DD0209C が表示され、監査レポート DB User Name 0209 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0209A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0209B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0209C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0224 {#c10-i0443}
*分類: レポート*  ・  難易度: 上級

紅E確認0225ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紅E確認0225です。紅E確認0225は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録紅E確認0225です。紅E確認0225ではSQL動詞集計と取得時刻を採取票紅E確認0225へ残します。紅E確認0225では対象データソースの取り違えを避けるため補助資料も照合する判断紅E確認0225です。紅E確認0225の用語整理では監査レポートの対象値を実在出力で整理する記録紅E確認0225です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0224を同一分類の監査レポート Audit Task Status 0233と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は復旧操作で点検欄を確認することでユーザー活動を確認し・監査タスク未レビューを防ぐ。
    - B. 構成を確認する際の意味は状態確認でスケジュールを確認することでスケジュールを確認し・スケジュールの誤読を防ぐ。
    - C. 構成を確認する際の意味は調査操作で保守欄を引き継ぎすることで照会文動詞集を確認し・対象データソースの取り違えを防ぐ。 ✅
    - D. 構成を確認する際の意味は保守操作で監査欄を保存することでカーネル監視を確認し・ローカル通信制御監視の未確認を防ぐ。S-TAP監視 Last Response 0052固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能照会文・対象デでCの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・確認）です。照合照会文・確認に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・確認・対象デです。比較監査レ・確認でA:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸はデータ・確認・照会文です。運用確認・データでB:の状態確認 スケジュールは「複数 collector の監査情報を集約し」を述べるため、正答側の照合軸は照会文・監査レ・確認です。仕様照会文・確認でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は確認・対象デ・照会文です。用語照会文・確認という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0224**

    - 検証目的: 監査レポートの監査レポート DB User Name 0224について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.34
    Server IP 198.51.100.64
    Count 114
    確認コード GDP12DD0224A
    ```

    画面・出力には GDP12DD0224A が表示され、監査レポート DB User Name 0224 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0224
    Process Type Report
    Status completed
    確認コード GDP12DD0224B
    ```

    画面・出力には GDP12DD0224B が表示され、監査レポート DB User Name 0224 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0224C
    ```

    画面・出力には GDP12DD0224C が表示され、監査レポート DB User Name 0224 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0224A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0224B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0224C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0239 {#c10-i0444}
*分類: レポート*  ・  難易度: 上級

空T確認0240ではIBM Guardium Data Protection 12.x の レポートを扱う採取票空T確認0240です。空T確認0240は監査レポートの表示操作で監査レポートの対象欄を追跡する記録空T確認0240です。空T確認0240ではSQL動詞集計と取得時刻を採取票空T確認0240へ残します。空T確認0240ではジョブ失敗の見落としを避けるため補助資料も照合する判断空T確認0240です。空T確認0240の用語整理では監査レポートの対象値を実在出力で照合する記録空T確認0240です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0239の設定や表示を読む前に役割を確認します。ロールと権限 Application Access 0300ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは照合操作で確認欄を採取することでユーザー有効を確認し・監査担当者の閲覧範囲不足を防ぐ。
    - B. 状態を読み取るための働きは作業一覧からStatusを読むことで作業一覧を確認し・実行間隔より短いFROM/Tを防ぐ。
    - C. 状態を読み取るための働きは表示操作で対象欄を追跡することで照会文動詞集を確認し・ジョブ失敗の見落としを防ぐ。 ✅
    - D. 状態を読み取るための働きは表示操作で対象欄を追跡することでユーザー活動を確認し・ジョブ失敗の見落としを防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能照会文・ジョブでCの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・確認）です。照合照会文・確認に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・確認・ジョブです。比較監査レ・確認でA:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はデータ・確認・照会文です。運用確認・データでB:の保守後の確認 AUDIT20は「Audit Processで作業一覧から」を述べるため、正答側の照合軸は照会文・監査レ・確認です。仕様照会文・確認でD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は確認・ジョブ・照会文です。用語照会文・確認という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0239**

    - 検証目的: 監査レポートの監査レポート DB User Name 0239について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.49
    Server IP 198.51.100.79
    Count 129
    確認コード GDP12DD0239A
    ```

    画面・出力には GDP12DD0239A が表示され、監査レポート DB User Name 0239 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0239
    Process Type Report
    Status completed
    確認コード GDP12DD0239B
    ```

    画面・出力には GDP12DD0239B が表示され、監査レポート DB User Name 0239 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0239C
    ```

    画面・出力には GDP12DD0239C が表示され、監査レポート DB User Name 0239 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0239A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0239B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0239C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0254 {#c10-i0445}
*分類: レポート*  ・  難易度: 初級

翠O保護0255ではIBM Guardium Data Protection 12.x の レポートを扱う採取票翠O保護0255です。翠O保護0255は監査レポートの点検操作で監査レポートの判定欄を記録する記録翠O保護0255です。翠O保護0255ではSQL動詞集計と取得時刻を採取票翠O保護0255へ残します。翠O保護0255ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断翠O保護0255です。翠O保護0255の用語整理では監査レポートの対象値を実在出力で保管する記録翠O保護0255です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0254に関する障害切り分けの前提を確認しています。S-TAP監視 Last Response 0292の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するして照会文動詞集を照合する。 ✅
    - B. 機能の説明としてはローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するしてカーネル監視を照合する。
    - C. 機能の説明としては廃止サーバーの参照を残して監査対を避けるため・参照箇所からUsedByを読むして参照箇所を照合する。
    - D. 機能の説明としては照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するしてデータソースを照合する。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能照会文・照会文でAの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・保護）です。照合照会文・保護に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・保護・照会文です。運用保護・データでB:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は照会文・監査レ・保護です。項目照会文・保護でC:の停止前の確認 DSRC14は「Guardiumで参照箇所から」を述べるため、正答側の照合軸は照会文・監査レ・照会文です。仕様照会文・保護でD:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は保護・照会文・照会文です。用語照会文・保護という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0254**

    - 検証目的: 監査レポートの監査レポート DB User Name 0254について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.24
    Server IP 198.51.100.34
    Count 24
    確認コード GDP12DD0254A
    ```

    画面・出力には GDP12DD0254A が表示され、監査レポート DB User Name 0254 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0254
    Process Type Report
    Status completed
    確認コード GDP12DD0254B
    ```

    画面・出力には GDP12DD0254B が表示され、監査レポート DB User Name 0254 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0254C
    ```

    画面・出力には GDP12DD0254C が表示され、監査レポート DB User Name 0254 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0254A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0254B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0254C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0269 {#c10-i0446}
*分類: レポート*  ・  難易度: 中級

朱J照合0270ではIBM Guardium Data Protection 12.x の レポートを扱う採取票朱J照合0270です。朱J照合0270は監査レポートの復旧操作で監査レポートの点検欄を確認する記録朱J照合0270です。朱J照合0270ではSQL動詞集計と取得時刻を採取票朱J照合0270へ残します。朱J照合0270では監査タスク未レビューを避けるため補助資料も照合する判断朱J照合0270です。朱J照合0270の用語整理では監査レポートの対象値を実在出力で点検する記録朱J照合0270です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0269を保守記録に説明する必要があります。ロールと権限 Permission 0288と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するして表示可能レポを照合する。
    - B. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するして照会文動詞集を照合する。 ✅
    - C. 運用時に利用する技術的役割はディスク逼迫中に検査データ流入をを避けるため・監視プロセスからApplianceを読むして監視プロセスを照合する。
    - D. 運用時に利用する技術的役割は未承認監視エージェント接続を避けるため・記録操作で証跡欄を照合するして暗号化表示を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能照会文・監査タでBの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・照合）です。照合照会文・照合に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・照合・監査タです。比較監査レ・照合でA:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はデータ・照合・照会文です。項目照会文・照合でC:の通常状態の確認 APP01は「Appliance Monitoriで監視プ」を述べるため、正答側の照合軸は監査タ・監査レ・照会文です。仕様照会文・照合でD:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は照合・監査タ・照会文です。用語照会文・照合という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0269**

    - 検証目的: 監査レポートの監査レポート DB User Name 0269について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.39
    Server IP 198.51.100.49
    Count 39
    確認コード GDP12DD0269A
    ```

    画面・出力には GDP12DD0269A が表示され、監査レポート DB User Name 0269 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0269
    Process Type Report
    Status completed
    確認コード GDP12DD0269B
    ```

    画面・出力には GDP12DD0269B が表示され、監査レポート DB User Name 0269 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0269C
    ```

    画面・出力には GDP12DD0269C が表示され、監査レポート DB User Name 0269 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0269A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0269B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0269C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0284 {#c10-i0447}
*分類: レポート*  ・  難易度: 中級

紅E抑止0285ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紅E抑止0285です。紅E抑止0285は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録紅E抑止0285です。紅E抑止0285ではSQL動詞集計と取得時刻を採取票紅E抑止0285へ残します。紅E抑止0285では対象データソースの取り違えを避けるため補助資料も照合する判断紅E抑止0285です。紅E抑止0285の用語整理では監査レポートの対象値を実在出力で整理する記録紅E抑止0285です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0284の技術的な意味を資料で確認するとき、S-TAP監視 S-TAP Host 0286との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は監視エージェントの最終応答と取得時刻を記録し・最終応答停止の見落としを防ぐである。確認操作で状態欄を整理するときは最終応答停止の見落としを防ぐ。
    - B. 構成を確認する際の意味はAppliance Monitoriでデータベース処理一覧から TURBINE を読み・TURBINE とである。DB処理一覧からTURBINEを読むときはディスク逼迫中に検査データ流を防ぐ。
    - C. 構成を確認する際の意味はApplication Accessのユーザー有効化と取得時刻を記録し・GuardAPI実行権限不足を防ぐである。監査操作で記録欄を比較するときはGuardAPI実行権限不足を防ぐ。
    - D. 構成を確認する際の意味はデータベース User Nameの照会文動詞集計と取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能照会文・対象デでDの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・抑止）です。照合照会文・抑止に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・抑止・対象デです。比較監査レ・抑止でA:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はデータ・抑止・照会文です。運用抑止・データでB:の変更前の確認 APP02は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸は照会文・監査レ・抑止です。項目照会文・抑止でC:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は対象デ・監査レ・照会文です。用語照会文・抑止という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0284**

    - 検証目的: 監査レポートの監査レポート DB User Name 0284について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.54
    Server IP 198.51.100.64
    Count 54
    確認コード GDP12DD0284A
    ```

    画面・出力には GDP12DD0284A が表示され、監査レポート DB User Name 0284 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0284
    Process Type Report
    Status completed
    確認コード GDP12DD0284B
    ```

    画面・出力には GDP12DD0284B が表示され、監査レポート DB User Name 0284 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0284C
    ```

    画面・出力には GDP12DD0284C が表示され、監査レポート DB User Name 0284 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0284A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0284B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0284C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0299 {#c10-i0448}
*分類: レポート*  ・  難易度: 中級

空T抑止0300ではIBM Guardium Data Protection 12.x の レポートを扱う採取票空T抑止0300です。空T抑止0300は監査レポートの表示操作で監査レポートの対象欄を追跡する記録空T抑止0300です。空T抑止0300ではSQL動詞集計と取得時刻を採取票空T抑止0300へ残します。空T抑止0300ではジョブ失敗の見落としを避けるため補助資料も照合する判断空T抑止0300です。空T抑止0300の用語整理では監査レポートの対象値を実在出力で照合する記録空T抑止0300です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0299について構成や状態を確認します。監査レポート Client IP 0320ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするして監査タスクを照合する。
    - B. 状態を読み取るための働きはディスク逼迫中に検査データ流入をを避けるため・DB処理一覧からTURBINEを読むしてデータベースを照合する。
    - C. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するして照会文動詞集を照合する。 ✅
    - D. 状態を読み取るための働きは監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するしてロール割当を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能照会文・ジョブでCの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・抑止）です。照合照会文・抑止に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・抑止・ジョブです。比較監査レ・抑止でA:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸はデータ・抑止・照会文です。運用抑止・データでB:の復旧準備 APP05は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸は照会文・監査レ・抑止です。仕様照会文・抑止でD:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は抑止・ジョブ・照会文です。用語照会文・抑止という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0299**

    - 検証目的: 監査レポートの監査レポート DB User Name 0299について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.69
    Server IP 198.51.100.79
    Count 69
    確認コード GDP12DD0299A
    ```

    画面・出力には GDP12DD0299A が表示され、監査レポート DB User Name 0299 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0299
    Process Type Report
    Status completed
    確認コード GDP12DD0299B
    ```

    画面・出力には GDP12DD0299B が表示され、監査レポート DB User Name 0299 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0299C
    ```

    画面・出力には GDP12DD0299C が表示され、監査レポート DB User Name 0299 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0299A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0299B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0299C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0314 {#c10-i0449}
*分類: レポート*  ・  難易度: 中級

翠O解析0315ではIBM Guardium Data Protection 12.x の レポートを扱う採取票翠O解析0315です。翠O解析0315は監査レポートの点検操作で監査レポートの判定欄を記録する記録翠O解析0315です。翠O解析0315ではSQL動詞集計と取得時刻を採取票翠O解析0315へ残します。翠O解析0315ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断翠O解析0315です。翠O解析0315の用語整理では監査レポートの対象値を実在出力で保管する記録翠O解析0315です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0314の役割を調べています。Approved TAP Clients 証跡採取 停止時刻の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては停止時刻の誤読を避けるため・証跡採取で停止時刻を確認するして停止時刻を照合する。
    - B. 機能の説明としてはディスク逼迫中に検査データ流入をを避けるため・DB処理一覧からTURBINEを読むしてデータベースを照合する。
    - C. 機能の説明としては照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するして照会文動詞集を照合する。 ✅
    - D. 機能の説明としては監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するしてユーザー有効を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能照会文・照会文でCの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・解析）です。照合照会文・解析に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・解析・照会文です。比較監査レ・解析でA:の証跡採取 停止時刻は「接続を許可された S-TAP」を述べるため、正答側の照合軸はデータ・解析・照会文です。運用解析・データでB:の性能影響の確認 APP11は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸は照会文・監査レ・解析です。仕様照会文・解析でD:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は解析・照会文・照会文です。用語照会文・解析という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0314**

    - 検証目的: 監査レポートの監査レポート DB User Name 0314について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.84
    Server IP 198.51.100.34
    Count 84
    確認コード GDP12DD0314A
    ```

    画面・出力には GDP12DD0314A が表示され、監査レポート DB User Name 0314 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0314
    Process Type Report
    Status completed
    確認コード GDP12DD0314B
    ```

    画面・出力には GDP12DD0314B が表示され、監査レポート DB User Name 0314 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0314C
    ```

    画面・出力には GDP12DD0314C が表示され、監査レポート DB User Name 0314 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0314A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0314B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0314C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0329 {#c10-i0450}
*分類: レポート*  ・  難易度: 中級

朱J計画0330ではIBM Guardium Data Protection 12.x の レポートを扱う採取票朱J計画0330です。朱J計画0330は監査レポートの復旧操作で監査レポートの点検欄を確認する記録朱J計画0330です。朱J計画0330ではSQL動詞集計と取得時刻を採取票朱J計画0330へ残します。朱J計画0330では監査タスク未レビューを避けるため補助資料も照合する判断朱J計画0330です。朱J計画0330の用語整理では監査レポートの対象値を実在出力で点検する記録朱J計画0330です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート DB User Name 0329」を「audit process 証跡採取 重大度」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は証跡採取で重大度を証跡に残し・監査要件に沿ってレポート実行とレビューを束ねる処理を証跡採取。
    - B. 運用時に利用する技術的役割は巡回で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。
    - C. 運用時に利用する技術的役割は切替でユーザー有効を証跡に残し・Application Accessのユーザー有効化と取得時。
    - D. 運用時に利用する技術的役割は計画で照会文動詞集を証跡に残し・データベース User Nameの照会文動詞集計と取得時刻を。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能照会文・監査タでDの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・計画）です。照合照会文・計画に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・計画・監査タです。比較監査レ・計画でA:の証跡採取 重大度は「監査要件に沿ってレポート実行とレビューを束ね」を述べるため、正答側の照合軸はデータ・計画・照会文です。運用計画・データでB:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸は照会文・監査レ・計画です。項目照会文・計画でC:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は監査タ・監査レ・照会文です。用語照会文・計画という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0329**

    - 検証目的: 監査レポートの監査レポート DB User Name 0329について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.19
    Server IP 198.51.100.49
    Count 99
    確認コード GDP12DD0329A
    ```

    画面・出力には GDP12DD0329A が表示され、監査レポート DB User Name 0329 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0329
    Process Type Report
    Status completed
    確認コード GDP12DD0329B
    ```

    画面・出力には GDP12DD0329B が表示され、監査レポート DB User Name 0329 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0329C
    ```

    画面・出力には GDP12DD0329C が表示され、監査レポート DB User Name 0329 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0329A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0329B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0329C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0344 {#c10-i0451}
*分類: レポート*  ・  難易度: 上級

紅E解除0345ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紅E解除0345です。紅E解除0345は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録紅E解除0345です。紅E解除0345ではSQL動詞集計と取得時刻を採取票紅E解除0345へ残します。紅E解除0345では対象データソースの取り違えを避けるため補助資料も照合する判断紅E解除0345です。紅E解除0345の用語整理では監査レポートの対象値を実在出力で整理する記録紅E解除0345です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0344を同一分類のaggregator 対象絞り込み キーマップと比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はキーマップの誤読を避けるため・監査プロセスでキーマップを確認するしてキーマップを照合する。
    - B. 構成を確認する際の意味は対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするして照会文動詞集を照合する。 ✅
    - C. 構成を確認する際の意味は監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するしてGuardAを照合する。
    - D. 構成を確認する際の意味はディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてディレクトリを照合する。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能照会文・対象デでBの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・解除）です。照合照会文・解除に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・解除・対象デです。比較監査レ・解除でA:の対象絞り込み キーマップは「複数 collector の監査情報を集約し」を述べるため、正答側の照合軸はデータ・解除・照会文です。項目照会文・解除でC:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は対象デ・監査レ・照会文です。仕様照会文・解除でD:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は解除・対象デ・照会文です。用語照会文・解除という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0344**

    - 検証目的: 監査レポートの監査レポート DB User Name 0344について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.34
    Server IP 198.51.100.64
    Count 114
    確認コード GDP12DD0344A
    ```

    画面・出力には GDP12DD0344A が表示され、監査レポート DB User Name 0344 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0344
    Process Type Report
    Status completed
    確認コード GDP12DD0344B
    ```

    画面・出力には GDP12DD0344B が表示され、監査レポート DB User Name 0344 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0344C
    ```

    画面・出力には GDP12DD0344C が表示され、監査レポート DB User Name 0344 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0344A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0344B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0344C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0359 {#c10-i0452}
*分類: レポート*  ・  難易度: 上級

空T解除0360ではIBM Guardium Data Protection 12.x の レポートを扱う採取票空T解除0360です。空T解除0360は監査レポートの表示操作で監査レポートの対象欄を追跡する記録空T解除0360です。空T解除0360ではSQL動詞集計と取得時刻を採取票空T解除0360へ残します。空T解除0360ではジョブ失敗の見落としを避けるため補助資料も照合する判断空T解除0360です。空T解除0360の用語整理では監査レポートの対象値を実在出力で照合する記録空T解除0360です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0359の設定や表示を読む前に役割を確認します。collector 実行結果照合 対象表ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは対象表の誤読を避けるため・実行結果照合で対象表を確認するして対象表を照合する。
    - B. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するして監査タスクを照合する。
    - C. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するして照会文動詞集を照合する。 ✅
    - D. 状態を読み取るための働きは照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するしてジョブキューを照合する。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能照会文・ジョブでCの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・解除）です。照合照会文・解除に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・解除・ジョブです。比較監査レ・解除でA:の実行結果照合 対象表は「S-TAP や外部接続から監査データを受け取」を述べるため、正答側の照合軸はデータ・解除・照会文です。運用解除・データでB:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸は照会文・監査レ・解除です。仕様照会文・解除でD:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は解除・ジョブ・照会文です。用語照会文・解除という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0359**

    - 検証目的: 監査レポートの監査レポート DB User Name 0359について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DB User Name と SQL動詞集計
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Assessment Datasources report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.49
    Server IP 198.51.100.79
    Count 129
    確認コード GDP12DD0359A
    ```

    画面・出力には GDP12DD0359A が表示され、監査レポート DB User Name 0359 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0359
    Process Type Report
    Status completed
    確認コード GDP12DD0359B
    ```

    画面・出力には GDP12DD0359B が表示され、監査レポート DB User Name 0359 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。DB User Name を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0359C
    ```

    画面・出力には GDP12DD0359C が表示され、監査レポート DB User Name 0359 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0359A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0359B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0359C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0011 {#c10-i0453}
*分類: レポート*  ・  難易度: 初級

白L巡回0012ではIBM Guardium Data Protection 12.x の レポートを扱う採取票白L巡回0012です。白L巡回0012は監査レポートの表示操作で監査レポートの対象欄を追跡する記録白L巡回0012です。白L巡回0012ではジョブキューと取得時刻を採取票白L巡回0012へ残します。白L巡回0012ではジョブ失敗の見落としを避けるため補助資料も照合する判断白L巡回0012です。白L巡回0012の用語整理では監査レポートの対象値を実在出力で照合する記録白L巡回0012です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0011について構成や状態を確認します。ロールと権限 Application Access 0060ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはApplication Accessのユーザー有効化と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。
    - B. 状態を読み取るための働きはLDAP UserのGuardAPI権限と取得時刻を記録し・LDAP取込対象の誤りを防ぐである。変更確認操作で採取欄を棚卸するときはディレクトリー取込対象の誤りを防ぐ。
    - C. 状態を読み取るための働きはSQL Verbのジョブキューと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。 ✅
    - D. 状態を読み取るための働きはAudit Processで代替経路の確認では監査プロセスの プロセス一覧からScheduleを読みである。代替経路確認で代替経路の確を確認するときは実行間隔より短いFROM/Tを防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 巡回対象ジョブキュでCの記述「SQL Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・巡回・ジョブ・ジョブ失）です。巡回時のジョブキュに関するレポートの仕様は「SQL Verbのジョブキューと取得時刻を記録し」で、確認対象は照会文・巡回・ジョブ・ジョブ失です。Ap・監査・ユーザーのA:は「Application Accessのユーザー有効化と取得時刻を記録」を述べ、対象はApplication Access（Appli・監査・ユーザ・監査担当）です。抑止対象GuardのB:は「LDAP UserのGuardAPI権限と取得時刻を記録し」を述べ、対象はLDAP User（ディレクト・抑止・Gua・ディレク）です。代替経路のを代替経路確のD:は「Audit Processで代替経路の確認では監査プロセスの」を述べ、対象は代替経路の確認 AUDIT10（Audit・代替経・代替経・実行間隔）です。ジョブキュを巡回という用語は「SQL Verbのジョブキューと取得時刻を記録し」を指し、SQL Verb（照会文・巡回・ジョブ・ジョブ失）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0011**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0011について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.21
    Server IP 198.51.100.31
    Count 21
    確認コード GDP12DD0011A
    ```

    画面・出力には GDP12DD0011A が表示され、監査レポート SQL Verb 0011 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0011
    Process Type Report
    Status completed
    確認コード GDP12DD0011B
    ```

    画面・出力には GDP12DD0011B が表示され、監査レポート SQL Verb 0011 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0011C
    ```

    画面・出力には GDP12DD0011C が表示され、監査レポート SQL Verb 0011 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0011A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0011B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0011C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0026 {#c10-i0454}
*分類: レポート*  ・  難易度: 中級

紫G棚卸0027ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紫G棚卸0027です。紫G棚卸0027は監査レポートの点検操作で監査レポートの判定欄を記録する記録紫G棚卸0027です。紫G棚卸0027ではジョブキューと取得時刻を採取票紫G棚卸0027へ残します。紫G棚卸0027ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紫G棚卸0027です。紫G棚卸0027の用語整理では監査レポートの対象値を実在出力で保管する記録紫G棚卸0027です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0026の役割を調べています。ロールと権限 LDAP User 0117の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するしてジョブキューを照合する。 ✅
    - B. 機能の説明としては過剰ロール付与を避けるため・主操作で出力欄を評価するしてGuardAを照合する。
    - C. 機能の説明としてはディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてユーザー有効を照合する。
    - D. 機能の説明としては廃止サーバーの参照を残して監査対を避けるため・復旧確認で変更履歴を確認するして変更履歴を照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 棚卸対象ジョブキュでAの記述「SQL Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・棚卸・ジョブ・照会文動）です。棚卸時のジョブキュに関するレポートの仕様は「SQL Verbのジョブキューと取得時刻を記録し」で、確認対象は照会文・棚卸・ジョブ・照会文動です。移行対象GuardのB:は「LDAP UserのGuardAPI権限と取得時刻を記録し」を述べ、対象はLDAP User（ディレクト・移行・Gua・過剰ロー）です。登録時のユーザー有のC:は「Application Accessのユーザー有効化と取得時刻を記録」を述べ、対象はApplication Access（Appli・登録・ユーザ・ディレク）です。変更履歴を復旧確認のD:は「Guardiumで復旧後の確認ではデータソース管理・データソースの」を述べ、対象は復旧後の確認 DSRC06（Guard・復旧確・変更履・廃止サー）です。ジョブキュを棚卸という用語は「SQL Verbのジョブキューと取得時刻を記録し」を指し、SQL Verb（照会文・棚卸・ジョブ・照会文動）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0026**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0026について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.36
    Server IP 198.51.100.46
    Count 36
    確認コード GDP12DD0026A
    ```

    画面・出力には GDP12DD0026A が表示され、監査レポート SQL Verb 0026 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0026
    Process Type Report
    Status completed
    確認コード GDP12DD0026B
    ```

    画面・出力には GDP12DD0026B が表示され、監査レポート SQL Verb 0026 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0026C
    ```

    画面・出力には GDP12DD0026C が表示され、監査レポート SQL Verb 0026 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0026A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0026B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0026C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0041 {#c10-i0455}
*分類: レポート*  ・  難易度: 中級

橙B復旧0042ではIBM Guardium Data Protection 12.x の レポートを扱う採取票橙B復旧0042です。橙B復旧0042は監査レポートの復旧操作で監査レポートの点検欄を確認する記録橙B復旧0042です。橙B復旧0042ではジョブキューと取得時刻を採取票橙B復旧0042へ残します。橙B復旧0042では監査タスク未レビューを避けるため補助資料も照合する判断橙B復旧0042です。橙B復旧0042の用語整理では監査レポートの対象値を実在出力で点検する記録橙B復旧0042です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート SQL Verb 0041」を「ロールと権限 Login Name 0084」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は照合操作で確認欄を採取することでロール割当を確認し・監査担当者の閲覧範囲不足を防ぐ。
    - B. 運用時に利用する技術的役割は確認操作で状態欄を整理することで承認クライアを確認し・最終応答停止の見落としを防ぐ。
    - C. 運用時に利用する技術的役割はデータソースで変更履歴を確認することで変更履歴を確認し・廃止サーバーの参照を残して監を防ぐ。
    - D. 運用時に利用する技術的役割は復旧操作で点検欄を確認することでジョブキューを確認し・監査タスク未レビューを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 復旧対象ジョブキュでDの記述「SQL Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・復旧・ジョブ・監査タス）です。復旧時のジョブキュに関するレポートの仕様は「SQL Verbのジョブキューと取得時刻を記録し」で、確認対象は照会文・復旧・ジョブ・監査タスです。Lo・変更・ロール割のA:は「Login Nameのロール割当と取得時刻を記録し」を述べ、対象はLogin Name（Login・変更・ロール・監査担当）です。保護対象承認クライのB:は「S-TAPの承認クライアントと取得時刻を記録し」を述べ、対象はServer Type（監視エージ・保護・承認ク・最終応答）です。データソ時の変更履歴のC:は「Guardiumで引継ぎ記録ではデータソース管理・データソースの」を述べ、対象は引継ぎ記録 DSRC09（Guard・データ・変更履・廃止サー）です。ジョブキュを復旧という用語は「SQL Verbのジョブキューと取得時刻を記録し」を指し、SQL Verb（照会文・復旧・ジョブ・監査タス）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0041**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0041について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.51
    Server IP 198.51.100.61
    Count 51
    確認コード GDP12DD0041A
    ```

    画面・出力には GDP12DD0041A が表示され、監査レポート SQL Verb 0041 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0041
    Process Type Report
    Status completed
    確認コード GDP12DD0041B
    ```

    画面・出力には GDP12DD0041B が表示され、監査レポート SQL Verb 0041 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0041C
    ```

    画面・出力には GDP12DD0041C が表示され、監査レポート SQL Verb 0041 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0041A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0041B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0041C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0056 {#c10-i0456}
*分類: レポート*  ・  難易度: 中級

青Q復旧0057ではIBM Guardium Data Protection 12.x の レポートを扱う採取票青Q復旧0057です。青Q復旧0057は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録青Q復旧0057です。青Q復旧0057ではジョブキューと取得時刻を採取票青Q復旧0057へ残します。青Q復旧0057では対象データソースの取り違えを避けるため補助資料も照合する判断青Q復旧0057です。青Q復旧0057の用語整理では監査レポートの対象値を実在出力で整理する記録青Q復旧0057です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0056を同一分類のS-TAP監視 S-TAP Version 0133と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は監視エージェントの暗号化表示と取得時刻を記録し・未承認監視エージェント接続を防ぐである。記録操作で証跡欄を照合するときは未承認監視エージェント接続を防ぐ。
    - B. 構成を確認する際の意味は監視エージェントの最終応答と取得時刻を記録し・未承認監視エージェント接続を防ぐである。記録操作で証跡欄を照合するときは未承認監視エージェント接続を防ぐ。
    - C. 構成を確認する際の意味はAudit Processで報告上限から max_audit_reporting を読みである。報告上限からmax_audit_reときは実行間隔より短いFROM/Tを防ぐ。
    - D. 構成を確認する際の意味は照会文 Verbのジョブキューと取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ジョブ・対象デでDの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・復旧）です。照合ジョブ・復旧に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・復旧・対象デです。比較監査レ・復旧でA:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は照会文・復旧・ジョブです。運用復旧・照会文でB:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はジョブ・監査レ・復旧です。項目ジョブ・復旧でC:の復旧後の確認 AUDIT06は「Audit Processで報告上限から」を述べるため、正答側の照合軸は対象デ・監査レ・ジョブです。用語ジョブ・復旧という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0056**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0056について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.66
    Server IP 198.51.100.76
    Count 66
    確認コード GDP12DD0056A
    ```

    画面・出力には GDP12DD0056A が表示され、監査レポート SQL Verb 0056 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0056
    Process Type Report
    Status completed
    確認コード GDP12DD0056B
    ```

    画面・出力には GDP12DD0056B が表示され、監査レポート SQL Verb 0056 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0056C
    ```

    画面・出力には GDP12DD0056C が表示され、監査レポート SQL Verb 0056 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0056A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0056B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0056C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0071 {#c10-i0457}
*分類: レポート*  ・  難易度: 中級

白L監査0072ではIBM Guardium Data Protection 12.x の レポートを扱う採取票白L監査0072です。白L監査0072は監査レポートの表示操作で監査レポートの対象欄を追跡する記録白L監査0072です。白L監査0072ではジョブキューと取得時刻を採取票白L監査0072へ残します。白L監査0072ではジョブ失敗の見落としを避けるため補助資料も照合する判断白L監査0072です。白L監査0072の用語整理では監査レポートの対象値を実在出力で照合する記録白L監査0072です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0071の設定や表示を読む前に役割を確認します。ロールと権限 Role 0156ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するしてディレクトリを照合する。
    - B. 状態を読み取るための働きはディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてユーザー有効を照合する。
    - C. 状態を読み取るための働きはInspectionを避けるため・検査状態からLastResponseを読して検査状態を照合する。
    - D. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するしてジョブキューを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ジョブ・ジョブでDの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・監査）です。照合ジョブ・監査に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・監査・ジョブです。比較監査レ・監査でA:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は照会文・監査・ジョブです。運用監査・照会文でB:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はジョブ・監査レ・監査です。項目ジョブ・監査でC:の異常終了後の確認 IE19は「Inspection Engineで検査状態」を述べるため、正答側の照合軸はジョブ・監査レ・ジョブです。用語ジョブ・監査という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0071**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0071について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.81
    Server IP 198.51.100.31
    Count 81
    確認コード GDP12DD0071A
    ```

    画面・出力には GDP12DD0071A が表示され、監査レポート SQL Verb 0071 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0071
    Process Type Report
    Status completed
    確認コード GDP12DD0071B
    ```

    画面・出力には GDP12DD0071B が表示され、監査レポート SQL Verb 0071 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0071C
    ```

    画面・出力には GDP12DD0071C が表示され、監査レポート SQL Verb 0071 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0071A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0071B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0071C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0086 {#c10-i0458}
*分類: レポート*  ・  難易度: 中級

紫G変更0087ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紫G変更0087です。紫G変更0087は監査レポートの点検操作で監査レポートの判定欄を記録する記録紫G変更0087です。紫G変更0087ではジョブキューと取得時刻を採取票紫G変更0087へ残します。紫G変更0087ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紫G変更0087です。紫G変更0087の用語整理では監査レポートの対象値を実在出力で保管する記録紫G変更0087です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0086に関する障害切り分けの前提を確認しています。S-TAP監視 S-TAP Version 0103の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては監視エージェントの暗号化表示と取得時刻を記録し・カーネル監視導入状態の誤読を防ぐである。採取操作で照合欄を点検するときはカーネル監視導入状態の誤読を防ぐ。
    - B. 機能の説明としては監視エージェントのカーネル監視有無と取得時刻を記録し・ローカル通信制御監視の未確認を防ぐである。保守操作で監査欄を保存するときはローカル通信制御監視の未確認を防ぐ。
    - C. 機能の説明としては照会文 Verbのジョブキューと取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。 ✅
    - D. 機能の説明としてはInspection Engineでエージェント変更から InspectionEngine を読みである。エージェント変更からInspectiときはInspectionを防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ジョブ・照会文でCの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・変更）です。照合ジョブ・変更に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・変更・照会文です。比較監査レ・変更でA:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は照会文・変更・ジョブです。運用変更・照会文でB:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はジョブ・監査レ・変更です。仕様ジョブ・変更でD:の権限境界の確認 IE12は「Inspection Engineでエージェ」を述べるため、正答側の照合軸は変更・照会文・ジョブです。用語ジョブ・変更という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0086**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0086について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.16
    Server IP 198.51.100.46
    Count 96
    確認コード GDP12DD0086A
    ```

    画面・出力には GDP12DD0086A が表示され、監査レポート SQL Verb 0086 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0086
    Process Type Report
    Status completed
    確認コード GDP12DD0086B
    ```

    画面・出力には GDP12DD0086B が表示され、監査レポート SQL Verb 0086 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0086C
    ```

    画面・出力には GDP12DD0086C が表示され、監査レポート SQL Verb 0086 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0086A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0086B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0086C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0101 {#c10-i0459}
*分類: レポート*  ・  難易度: 上級

橙B移行0102ではIBM Guardium Data Protection 12.x の レポートを扱う採取票橙B移行0102です。橙B移行0102は監査レポートの復旧操作で監査レポートの点検欄を確認する記録橙B移行0102です。橙B移行0102ではジョブキューと取得時刻を採取票橙B移行0102へ残します。橙B移行0102では監査タスク未レビューを避けるため補助資料も照合する判断橙B移行0102です。橙B移行0102の用語整理では監査レポートの対象値を実在出力で点検する記録橙B移行0102です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0101を保守記録に説明する必要があります。ロールと権限 Login Name 0174と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてロール割当を照合する。
    - B. 運用時に利用する技術的役割は照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するしてデータソースを照合する。
    - C. 運用時に利用する技術的役割はmanaged unitからのデを避けるため・Centraで引継ぎ記録を確認するして引継ぎ記録を照合する。
    - D. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するしてジョブキューを照合する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能ジョブ・監査タでDの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・移行）です。照合ジョブ・移行に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・移行・監査タです。比較監査レ・移行でA:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は照会文・移行・ジョブです。運用移行・照会文でB:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸はジョブ・監査レ・移行です。項目ジョブ・移行でC:の引継ぎ記録 CM09は「Central ManagerでCentra」を述べるため、正答側の照合軸は監査タ・監査レ・ジョブです。用語ジョブ・移行という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0101**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0101について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.31
    Server IP 198.51.100.61
    Count 111
    確認コード GDP12DD0101A
    ```

    画面・出力には GDP12DD0101A が表示され、監査レポート SQL Verb 0101 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0101
    Process Type Report
    Status completed
    確認コード GDP12DD0101B
    ```

    画面・出力には GDP12DD0101B が表示され、監査レポート SQL Verb 0101 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0101C
    ```

    画面・出力には GDP12DD0101C が表示され、監査レポート SQL Verb 0101 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0101A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0101B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0101C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0116 {#c10-i0460}
*分類: レポート*  ・  難易度: 上級

青Q移行0117ではIBM Guardium Data Protection 12.x の レポートを扱う採取票青Q移行0117です。青Q移行0117は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録青Q移行0117です。青Q移行0117ではジョブキューと取得時刻を採取票青Q移行0117へ残します。青Q移行0117では対象データソースの取り違えを避けるため補助資料も照合する判断青Q移行0117です。青Q移行0117の用語整理では監査レポートの対象値を実在出力で整理する記録青Q移行0117です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0116の技術的な意味を資料で確認するとき、S-TAP監視 KTAP Installed 0184との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は監視エージェントの監視エージェント状態と取得時刻を記録し・ローカル通信制御監視の未確認を防ぐである。保守操作で監査欄を保存するときはローカル通信制御監視の未確認を防ぐ。
    - B. 構成を確認する際の意味は照会文 Verbのジョブキューと取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。 ✅
    - C. 構成を確認する際の意味はClient IPの監査タスクと取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。
    - D. 構成を確認する際の意味はInspection Engineで検査状態から LastResponse を読みである。検査状態からLastResponseときはInspectionを防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能ジョブ・対象デでBの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・移行）です。照合ジョブ・移行に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・移行・対象デです。比較監査レ・移行でA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸は照会文・移行・ジョブです。項目ジョブ・移行でC:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸は対象デ・監査レ・ジョブです。仕様ジョブ・移行でD:の異常終了後の確認 IE19は「Inspection Engineで検査状態」を述べるため、正答側の照合軸は移行・対象デ・ジョブです。用語ジョブ・移行という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0116**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0116について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.46
    Server IP 198.51.100.76
    Count 126
    確認コード GDP12DD0116A
    ```

    画面・出力には GDP12DD0116A が表示され、監査レポート SQL Verb 0116 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0116
    Process Type Report
    Status completed
    確認コード GDP12DD0116B
    ```

    画面・出力には GDP12DD0116B が表示され、監査レポート SQL Verb 0116 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0116C
    ```

    画面・出力には GDP12DD0116C が表示され、監査レポート SQL Verb 0116 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0116A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0116B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0116C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0131 {#c10-i0461}
*分類: レポート*  ・  難易度: 初級

白L診断0132ではIBM Guardium Data Protection 12.x の レポートを扱う採取票白L診断0132です。白L診断0132は監査レポートの表示操作で監査レポートの対象欄を追跡する記録白L診断0132です。白L診断0132ではジョブキューと取得時刻を採取票白L診断0132へ残します。白L診断0132ではジョブ失敗の見落としを避けるため補助資料も照合する判断白L診断0132です。白L診断0132の用語整理では監査レポートの対象値を実在出力で照合する記録白L診断0132です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0131について構成や状態を確認します。S-TAP監視 KTAP Installed 0154ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは監視エージェントの監視エージェント状態と取得時刻を記録し・最終応答停止の見落としを防ぐである。確認操作で状態欄を整理するときは最終応答停止の見落としを防ぐ。
    - B. 状態を読み取るための働きは接続を許可された S-TAP と状態を確認する管理レポートを承認履歴確認する。承認履歴確認で初期同期を確認するときは初期同期の誤読を防ぐ。
    - C. 状態を読み取るための働きは照会文 Verbのジョブキューと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。 ✅
    - D. 状態を読み取るための働きはAppliance Monitoriでデータベース処理一覧から TURBINE を読み・TURBINE とである。DB処理一覧からTURBINEを読むときはディスク逼迫中に検査データ流を防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能ジョブ・ジョブでCの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・診断）です。照合ジョブ・診断に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・診断・ジョブです。比較監査レ・診断でA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸は照会文・診断・ジョブです。運用診断・照会文でB:の承認履歴確認 初期同期は「接続を許可された S-TAP」を述べるため、正答側の照合軸はジョブ・監査レ・診断です。仕様ジョブ・診断でD:の保守後の確認 APP20は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸は診断・ジョブ・ジョブです。用語ジョブ・診断という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0131**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0131について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.21
    Server IP 198.51.100.31
    Count 21
    確認コード GDP12DD0131A
    ```

    画面・出力には GDP12DD0131A が表示され、監査レポート SQL Verb 0131 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0131
    Process Type Report
    Status completed
    確認コード GDP12DD0131B
    ```

    画面・出力には GDP12DD0131B が表示され、監査レポート SQL Verb 0131 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0131C
    ```

    画面・出力には GDP12DD0131C が表示され、監査レポート SQL Verb 0131 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0131A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0131B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0131C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0146 {#c10-i0462}
*分類: レポート*  ・  難易度: 中級

紫G保守0147ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紫G保守0147です。紫G保守0147は監査レポートの点検操作で監査レポートの判定欄を記録する記録紫G保守0147です。紫G保守0147ではジョブキューと取得時刻を採取票紫G保守0147へ残します。紫G保守0147ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紫G保守0147です。紫G保守0147の用語整理では監査レポートの対象値を実在出力で保管する記録紫G保守0147です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0146の役割を調べています。ロールと権限 LDAP User 0222の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては変更確認操作で採取欄を棚卸することでGuardAを確認し・ディレクトリー取込対象の誤りを防ぐ。
    - B. 機能の説明としては遅延表示で遅延表示を確認することで遅延表示を確認し・遅延表示の誤読を防ぐ。
    - C. 機能の説明としては監視プロセスからApplianceを読むことで監視プロセスを確認し・ディスク逼迫中に検査データ流を防ぐ。
    - D. 機能の説明としては点検操作で判定欄を記録することでジョブキューを確認し・照会文動詞集計の期間誤りを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ジョブ・照会文でDの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・保守）です。照合ジョブ・保守に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・保守・照会文です。比較監査レ・保守でA:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は照会文・保守・ジョブです。運用保守・照会文でB:の実行結果照合 遅延表示は「監査要件に沿ってレポート実行とレビューを束ね」を述べるため、正答側の照合軸はジョブ・監査レ・保守です。項目ジョブ・保守でC:のログとの照合 APP07は「Appliance Monitoriで監視プ」を述べるため、正答側の照合軸は照会文・監査レ・ジョブです。用語ジョブ・保守という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0146**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0146について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.36
    Server IP 198.51.100.46
    Count 36
    確認コード GDP12DD0146A
    ```

    画面・出力には GDP12DD0146A が表示され、監査レポート SQL Verb 0146 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0146
    Process Type Report
    Status completed
    確認コード GDP12DD0146B
    ```

    画面・出力には GDP12DD0146B が表示され、監査レポート SQL Verb 0146 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0146C
    ```

    画面・出力には GDP12DD0146C が表示され、監査レポート SQL Verb 0146 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0146A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0146B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0146C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0161 {#c10-i0463}
*分類: レポート*  ・  難易度: 中級

橙B切替0162ではIBM Guardium Data Protection 12.x の レポートを扱う採取票橙B切替0162です。橙B切替0162は監査レポートの復旧操作で監査レポートの点検欄を確認する記録橙B切替0162です。橙B切替0162ではジョブキューと取得時刻を採取票橙B切替0162へ残します。橙B切替0162では監査タスク未レビューを避けるため補助資料も照合する判断橙B切替0162です。橙B切替0162の用語整理では監査レポートの対象値を実在出力で点検する記録橙B切替0162です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート SQL Verb 0161」を「S-TAP監視 S-TAP Host 0166」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は復旧操作で点検欄を確認することでジョブキューを確認し・監査タスク未レビューを防ぐ。 ✅
    - B. 運用時に利用する技術的役割は確認操作で状態欄を整理することで最終応答を確認し・最終応答停止の見落としを防ぐ。
    - C. 運用時に利用する技術的役割は遅延表示で遅延表示を確認することで遅延表示を確認し・遅延表示の誤読を防ぐ。
    - D. 運用時に利用する技術的役割は保守操作で監査欄を保存することでカーネル監視を確認し・ローカル通信制御監視の未確認を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ジョブ・監査タでAの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・切替）です。照合ジョブ・切替に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・切替・監査タです。運用切替・照会文でB:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はジョブ・監査レ・切替です。項目ジョブ・切替でC:の実行結果照合 遅延表示は「監査要件に沿ってレポート実行とレビューを束ね」を述べるため、正答側の照合軸は監査タ・監査レ・ジョブです。仕様ジョブ・切替でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は切替・監査タ・ジョブです。用語ジョブ・切替という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0161**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0161について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.51
    Server IP 198.51.100.61
    Count 51
    確認コード GDP12DD0161A
    ```

    画面・出力には GDP12DD0161A が表示され、監査レポート SQL Verb 0161 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0161
    Process Type Report
    Status completed
    確認コード GDP12DD0161B
    ```

    画面・出力には GDP12DD0161B が表示され、監査レポート SQL Verb 0161 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0161C
    ```

    画面・出力には GDP12DD0161C が表示され、監査レポート SQL Verb 0161 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0161A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0161B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0161C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0176 {#c10-i0464}
*分類: レポート*  ・  難易度: 中級

青Q切替0177ではIBM Guardium Data Protection 12.x の レポートを扱う採取票青Q切替0177です。青Q切替0177は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録青Q切替0177です。青Q切替0177ではジョブキューと取得時刻を採取票青Q切替0177へ残します。青Q切替0177では対象データソースの取り違えを避けるため補助資料も照合する判断青Q切替0177です。青Q切替0177の用語整理では監査レポートの対象値を実在出力で整理する記録青Q切替0177です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0176を同一分類の監査レポート DB User Name 0209と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は登録で照会文動詞集を証跡に残し・データベース User Nameの照会文動詞集計と取得時刻を。
    - B. 構成を確認する際の意味はAggregで応答行を証跡に残し・管理対象システムの構成と配布を統制する管理点を障害時切り分け。
    - C. 構成を確認する際の意味は監査でカーネル監視を証跡に残し・監視エージェントのカーネル監視有無と取得時刻を記録し。
    - D. 構成を確認する際の意味は切替でジョブキューを証跡に残し・照会文 Verbのジョブキューと取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ジョブ・対象デでDの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・切替）です。照合ジョブ・切替に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・切替・対象デです。比較監査レ・切替でA:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は照会文・切替・ジョブです。運用切替・照会文でB:の障害時切り分け 応答行は「管理対象システムの構成と配布を統制する管理点」を述べるため、正答側の照合軸はジョブ・監査レ・切替です。項目ジョブ・切替でC:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は対象デ・監査レ・ジョブです。用語ジョブ・切替という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0176**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0176について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.66
    Server IP 198.51.100.76
    Count 66
    確認コード GDP12DD0176A
    ```

    画面・出力には GDP12DD0176A が表示され、監査レポート SQL Verb 0176 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0176
    Process Type Report
    Status completed
    確認コード GDP12DD0176B
    ```

    画面・出力には GDP12DD0176B が表示され、監査レポート SQL Verb 0176 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0176C
    ```

    画面・出力には GDP12DD0176C が表示され、監査レポート SQL Verb 0176 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0176A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0176B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0176C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0191 {#c10-i0465}
*分類: レポート*  ・  難易度: 中級

白L収集0192ではIBM Guardium Data Protection 12.x の レポートを扱う採取票白L収集0192です。白L収集0192は監査レポートの表示操作で監査レポートの対象欄を追跡する記録白L収集0192です。白L収集0192ではジョブキューと取得時刻を採取票白L収集0192へ残します。白L収集0192ではジョブ失敗の見落としを避けるため補助資料も照合する判断白L収集0192です。白L収集0192の用語整理では監査レポートの対象値を実在出力で照合する記録白L収集0192です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0191の設定や表示を読む前に役割を確認します。S-TAP監視 S-TAP Host 0226ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは表示操作で対象欄を追跡することでジョブキューを確認し・ジョブ失敗の見落としを防ぐ。 ✅
    - B. 状態を読み取るための働きは確認操作で状態欄を整理することで最終応答を確認し・最終応答停止の見落としを防ぐ。
    - C. 状態を読み取るための働きはレポートでイベント識別を確認することでイベント識別を確認し・イベント識別の誤読を防ぐ。
    - D. 状態を読み取るための働きは記録操作で証跡欄を照合することでカーネル監視を確認し・未承認監視エージェント接続を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ジョブ・ジョブでAの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・収集）です。照合ジョブ・収集に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・収集・ジョブです。運用収集・照会文でB:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はジョブ・監査レ・収集です。項目ジョブ・収集でC:の対象絞り込み イベント識別は「接続を許可された S-TAP」を述べるため、正答側の照合軸はジョブ・監査レ・ジョブです。仕様ジョブ・収集でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は収集・ジョブ・ジョブです。用語ジョブ・収集という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0191**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0191について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.81
    Server IP 198.51.100.31
    Count 81
    確認コード GDP12DD0191A
    ```

    画面・出力には GDP12DD0191A が表示され、監査レポート SQL Verb 0191 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0191
    Process Type Report
    Status completed
    確認コード GDP12DD0191B
    ```

    画面・出力には GDP12DD0191B が表示され、監査レポート SQL Verb 0191 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0191C
    ```

    画面・出力には GDP12DD0191C が表示され、監査レポート SQL Verb 0191 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0191A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0191B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0191C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0206 {#c10-i0466}
*分類: レポート*  ・  難易度: 中級

紫G登録0207ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紫G登録0207です。紫G登録0207は監査レポートの点検操作で監査レポートの判定欄を記録する記録紫G登録0207です。紫G登録0207ではジョブキューと取得時刻を採取票紫G登録0207へ残します。紫G登録0207ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紫G登録0207です。紫G登録0207の用語整理では監査レポートの対象値を実在出力で保管する記録紫G登録0207です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0206に関する障害切り分けの前提を確認しています。監査レポート Audit Task Status 0278の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するしてジョブキューを照合する。 ✅
    - B. 機能の説明としては照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するしてユーザー活動を照合する。
    - C. 機能の説明としては廃止サーバーの参照を残して監査対を避けるため・データソース一覧からServiceNamしてデータソースを照合する。
    - D. 機能の説明としては未承認監視エージェント接続を避けるため・記録操作で証跡欄を照合するして承認クライアを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ジョブ・照会文でAの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・登録）です。照合ジョブ・登録に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・登録・照会文です。運用登録・照会文でB:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸はジョブ・監査レ・登録です。項目ジョブ・登録でC:の障害切り分け DSRC04は「Guardiumでデータソース一覧から」を述べるため、正答側の照合軸は照会文・監査レ・ジョブです。仕様ジョブ・登録でD:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は登録・照会文・ジョブです。用語ジョブ・登録という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0206**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0206について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.16
    Server IP 198.51.100.46
    Count 96
    確認コード GDP12DD0206A
    ```

    画面・出力には GDP12DD0206A が表示され、監査レポート SQL Verb 0206 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0206
    Process Type Report
    Status completed
    確認コード GDP12DD0206B
    ```

    画面・出力には GDP12DD0206B が表示され、監査レポート SQL Verb 0206 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0206C
    ```

    画面・出力には GDP12DD0206C が表示され、監査レポート SQL Verb 0206 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0206A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0206B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0206C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0221 {#c10-i0467}
*分類: レポート*  ・  難易度: 上級

橙B確認0222ではIBM Guardium Data Protection 12.x の レポートを扱う採取票橙B確認0222です。橙B確認0222は監査レポートの復旧操作で監査レポートの点検欄を確認する記録橙B確認0222です。橙B確認0222ではジョブキューと取得時刻を採取票橙B確認0222へ残します。橙B確認0222では監査タスク未レビューを避けるため補助資料も照合する判断橙B確認0222です。橙B確認0222の用語整理では監査レポートの対象値を実在出力で点検する記録橙B確認0222です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0221を保守記録に説明する必要があります。監査レポート Server IP 0317と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は復旧操作で点検欄を確認することでデータソースを確認し・監査タスク未レビューを防ぐ。
    - B. 運用時に利用する技術的役割は報告上限からmax_audit_repoことで報告上限を確認し・実行間隔より短いFROM/Tを防ぐ。
    - C. 運用時に利用する技術的役割は復旧操作で点検欄を確認することでジョブキューを確認し・監査タスク未レビューを防ぐ。 ✅
    - D. 運用時に利用する技術的役割は変更確認操作で採取欄を棚卸することでロール割当を確認し・ディレクトリー取込対象の誤りを防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能ジョブ・監査タでCの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・確認）です。照合ジョブ・確認に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・確認・監査タです。比較監査レ・確認でA:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は照会文・確認・ジョブです。運用確認・照会文でB:の復旧後の確認 AUDIT06は「Audit Processで報告上限から」を述べるため、正答側の照合軸はジョブ・監査レ・確認です。仕様ジョブ・確認でD:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は確認・監査タ・ジョブです。用語ジョブ・確認という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0221**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0221について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.31
    Server IP 198.51.100.61
    Count 111
    確認コード GDP12DD0221A
    ```

    画面・出力には GDP12DD0221A が表示され、監査レポート SQL Verb 0221 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0221
    Process Type Report
    Status completed
    確認コード GDP12DD0221B
    ```

    画面・出力には GDP12DD0221B が表示され、監査レポート SQL Verb 0221 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0221C
    ```

    画面・出力には GDP12DD0221C が表示され、監査レポート SQL Verb 0221 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0221A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0221B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0221C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0236 {#c10-i0468}
*分類: レポート*  ・  難易度: 上級

青Q確認0237ではIBM Guardium Data Protection 12.x の レポートを扱う採取票青Q確認0237です。青Q確認0237は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録青Q確認0237です。青Q確認0237ではジョブキューと取得時刻を採取票青Q確認0237へ残します。青Q確認0237では対象データソースの取り違えを避けるため補助資料も照合する判断青Q確認0237です。青Q確認0237の用語整理では監査レポートの対象値を実在出力で整理する記録青Q確認0237です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0236の技術的な意味を資料で確認するとき、S-TAP監視 S-TAP Host 0316との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するして最終応答を照合する。
    - B. 構成を確認する際の意味は実行間隔より短いFROM/TO範を避けるため・報告上限からmax_audit_repoして報告上限を照合する。
    - C. 構成を確認する際の意味はジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するして照会文動詞集を照合する。
    - D. 構成を確認する際の意味は対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてジョブキューを照合する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能ジョブ・対象デでDの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・確認）です。照合ジョブ・確認に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・確認・対象デです。比較監査レ・確認でA:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は照会文・確認・ジョブです。運用確認・照会文でB:の監査証跡の保存 AUDIT18は「Audit Processで報告上限から」を述べるため、正答側の照合軸はジョブ・監査レ・確認です。項目ジョブ・確認でC:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は対象デ・監査レ・ジョブです。用語ジョブ・確認という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0236**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0236について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.46
    Server IP 198.51.100.76
    Count 126
    確認コード GDP12DD0236A
    ```

    画面・出力には GDP12DD0236A が表示され、監査レポート SQL Verb 0236 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0236
    Process Type Report
    Status completed
    確認コード GDP12DD0236B
    ```

    画面・出力には GDP12DD0236B が表示され、監査レポート SQL Verb 0236 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0236C
    ```

    画面・出力には GDP12DD0236C が表示され、監査レポート SQL Verb 0236 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0236A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0236B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0236C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0251 {#c10-i0469}
*分類: レポート*  ・  難易度: 初級

白L保護0252ではIBM Guardium Data Protection 12.x の レポートを扱う採取票白L保護0252です。白L保護0252は監査レポートの表示操作で監査レポートの対象欄を追跡する記録白L保護0252です。白L保護0252ではジョブキューと取得時刻を採取票白L保護0252へ残します。白L保護0252ではジョブ失敗の見落としを避けるため補助資料も照合する判断白L保護0252です。白L保護0252の用語整理では監査レポートの対象値を実在出力で照合する記録白L保護0252です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0251について構成や状態を確認します。S-TAP監視 S-TAP Version 0298ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは抑止で暗号化表示を証跡に残し・監視エージェントの暗号化表示と取得時刻を記録し。
    - B. 状態を読み取るための働きは保護でジョブキューを証跡に残し・照会文 Verbのジョブキューと取得時刻を記録し。 ✅
    - C. 状態を読み取るための働きは代替経路確認で検査状態を証跡に残し・Inspection Engineで検査状態から。
    - D. 状態を読み取るための働きは診断で最終応答を証跡に残し・監視エージェントの最終応答と取得時刻を記録し。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能ジョブ・ジョブでBの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・保護）です。照合ジョブ・保護に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・保護・ジョブです。比較監査レ・保護でA:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は照会文・保護・ジョブです。項目ジョブ・保護でC:の代替経路の確認 IE10は「Inspection Engineで検査状態」を述べるため、正答側の照合軸はジョブ・監査レ・ジョブです。仕様ジョブ・保護でD:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は保護・ジョブ・ジョブです。用語ジョブ・保護という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0251**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0251について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.21
    Server IP 198.51.100.31
    Count 21
    確認コード GDP12DD0251A
    ```

    画面・出力には GDP12DD0251A が表示され、監査レポート SQL Verb 0251 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0251
    Process Type Report
    Status completed
    確認コード GDP12DD0251B
    ```

    画面・出力には GDP12DD0251B が表示され、監査レポート SQL Verb 0251 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0251C
    ```

    画面・出力には GDP12DD0251C が表示され、監査レポート SQL Verb 0251 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0251A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0251B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0251C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0266 {#c10-i0470}
*分類: レポート*  ・  難易度: 中級

紫G照合0267ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紫G照合0267です。紫G照合0267は監査レポートの点検操作で監査レポートの判定欄を記録する記録紫G照合0267です。紫G照合0267ではジョブキューと取得時刻を採取票紫G照合0267へ残します。紫G照合0267ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紫G照合0267です。紫G照合0267の用語整理では監査レポートの対象値を実在出力で保管する記録紫G照合0267です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0266の役割を調べています。ロールと権限 LDAP User 0357の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては主操作で出力欄を評価することでGuardAを確認し・過剰ロール付与を防ぐ。
    - B. 機能の説明としては点検操作で判定欄を記録することでジョブキューを確認し・照会文動詞集計の期間誤りを防ぐ。 ✅
    - C. 機能の説明としては参照箇所からUsedByを読むことで参照箇所を確認し・廃止サーバーの参照を残して監を防ぐ。
    - D. 機能の説明としては記録操作で証跡欄を照合することで最終応答を確認し・未承認監視エージェント接続を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ジョブ・照会文でBの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・照合）です。照合ジョブ・照合に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・照合・照会文です。比較監査レ・照合でA:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は照会文・照合・ジョブです。項目ジョブ・照合でC:の性能影響の確認 DSRC11は「Guardiumで参照箇所から」を述べるため、正答側の照合軸は照会文・監査レ・ジョブです。仕様ジョブ・照合でD:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は照合・照会文・ジョブです。用語ジョブ・照合という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0266**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0266について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.36
    Server IP 198.51.100.46
    Count 36
    確認コード GDP12DD0266A
    ```

    画面・出力には GDP12DD0266A が表示され、監査レポート SQL Verb 0266 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0266
    Process Type Report
    Status completed
    確認コード GDP12DD0266B
    ```

    画面・出力には GDP12DD0266B が表示され、監査レポート SQL Verb 0266 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0266C
    ```

    画面・出力には GDP12DD0266C が表示され、監査レポート SQL Verb 0266 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0266A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0266B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0266C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0281 {#c10-i0471}
*分類: レポート*  ・  難易度: 中級

橙B抑止0282ではIBM Guardium Data Protection 12.x の レポートを扱う採取票橙B抑止0282です。橙B抑止0282は監査レポートの復旧操作で監査レポートの点検欄を確認する記録橙B抑止0282です。橙B抑止0282ではジョブキューと取得時刻を採取票橙B抑止0282へ残します。橙B抑止0282では監査タスク未レビューを避けるため補助資料も照合する判断橙B抑止0282です。橙B抑止0282の用語整理では監査レポートの対象値を実在出力で点検する記録橙B抑止0282です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート SQL Verb 0281」を「ロールと権限 Role 0291」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は監査操作で記録欄を比較することでディレクトリを確認し・GuardAPI実行権限不足を防ぐ。
    - B. 運用時に利用する技術的役割はDB処理一覧からTURBINEを読むことでデータベースを確認し・ディスク逼迫中に検査データ流を防ぐ。
    - C. 運用時に利用する技術的役割は復旧操作で点検欄を確認することでジョブキューを確認し・監査タスク未レビューを防ぐ。 ✅
    - D. 運用時に利用する技術的役割は採取操作で照合欄を点検することで最終応答を確認し・カーネル監視導入状態の誤読を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ジョブ・監査タでCの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・抑止）です。照合ジョブ・抑止に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・抑止・監査タです。比較監査レ・抑止でA:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は照会文・抑止・ジョブです。運用抑止・照会文でB:の変更前の確認 APP02は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸はジョブ・監査レ・抑止です。仕様ジョブ・抑止でD:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は抑止・監査タ・ジョブです。用語ジョブ・抑止という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0281**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0281について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.51
    Server IP 198.51.100.61
    Count 51
    確認コード GDP12DD0281A
    ```

    画面・出力には GDP12DD0281A が表示され、監査レポート SQL Verb 0281 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0281
    Process Type Report
    Status completed
    確認コード GDP12DD0281B
    ```

    画面・出力には GDP12DD0281B が表示され、監査レポート SQL Verb 0281 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0281C
    ```

    画面・出力には GDP12DD0281C が表示され、監査レポート SQL Verb 0281 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0281A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0281B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0281C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0296 {#c10-i0472}
*分類: レポート*  ・  難易度: 中級

青Q抑止0297ではIBM Guardium Data Protection 12.x の レポートを扱う採取票青Q抑止0297です。青Q抑止0297は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録青Q抑止0297です。青Q抑止0297ではジョブキューと取得時刻を採取票青Q抑止0297へ残します。青Q抑止0297では対象データソースの取り違えを避けるため補助資料も照合する判断青Q抑止0297です。青Q抑止0297の用語整理では監査レポートの対象値を実在出力で整理する記録青Q抑止0297です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0296を同一分類のS-TAP監視 S-TAP Version 0298と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は抑止でジョブキューを証跡に残し・照会文 Verbのジョブキューと取得時刻を記録し。 ✅
    - B. 構成を確認する際の意味は抑止で暗号化表示を証跡に残し・監視エージェントの暗号化表示と取得時刻を記録し。
    - C. 構成を確認する際の意味は棚卸でカーネル監視を証跡に残し・監視エージェントのカーネル監視有無と取得時刻を記録し。
    - D. 構成を確認する際の意味は診断でロール割当を証跡に残し・Login Nameのロール割当と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ジョブ・対象デでAの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・抑止）です。照合ジョブ・抑止に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・抑止・対象デです。運用抑止・照会文でB:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はジョブ・監査レ・抑止です。項目ジョブ・抑止でC:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は対象デ・監査レ・ジョブです。仕様ジョブ・抑止でD:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は抑止・対象デ・ジョブです。用語ジョブ・抑止という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0296**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0296について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.66
    Server IP 198.51.100.76
    Count 66
    確認コード GDP12DD0296A
    ```

    画面・出力には GDP12DD0296A が表示され、監査レポート SQL Verb 0296 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0296
    Process Type Report
    Status completed
    確認コード GDP12DD0296B
    ```

    画面・出力には GDP12DD0296B が表示され、監査レポート SQL Verb 0296 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0296C
    ```

    画面・出力には GDP12DD0296C が表示され、監査レポート SQL Verb 0296 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0296A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0296B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0296C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0311 {#c10-i0473}
*分類: レポート*  ・  難易度: 中級

白L解析0312ではIBM Guardium Data Protection 12.x の レポートを扱う採取票白L解析0312です。白L解析0312は監査レポートの表示操作で監査レポートの対象欄を追跡する記録白L解析0312です。白L解析0312ではジョブキューと取得時刻を採取票白L解析0312へ残します。白L解析0312ではジョブ失敗の見落としを避けるため補助資料も照合する判断白L解析0312です。白L解析0312の用語整理では監査レポートの対象値を実在出力で照合する記録白L解析0312です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0311の設定や表示を読む前に役割を確認します。監査レポート Server IP 0347ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するしてジョブキューを照合する。 ✅
    - B. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するしてデータソースを照合する。
    - C. 状態を読み取るための働きはInspectionを避けるため・ポリシー変更からPolicyを読むしてポリシー変更を照合する。
    - D. 状態を読み取るための働きはGuardAPI実行権限不足を避けるため・監査操作で記録欄を比較するしてロール割当を照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ジョブ・ジョブでAの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・解析）です。照合ジョブ・解析に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・解析・ジョブです。運用解析・照会文でB:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸はジョブ・監査レ・解析です。項目ジョブ・解析でC:の性能影響の確認 IE11は「Inspection Engineでポリシー」を述べるため、正答側の照合軸はジョブ・監査レ・ジョブです。仕様ジョブ・解析でD:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は解析・ジョブ・ジョブです。用語ジョブ・解析という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0311**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0311について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.81
    Server IP 198.51.100.31
    Count 81
    確認コード GDP12DD0311A
    ```

    画面・出力には GDP12DD0311A が表示され、監査レポート SQL Verb 0311 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0311
    Process Type Report
    Status completed
    確認コード GDP12DD0311B
    ```

    画面・出力には GDP12DD0311B が表示され、監査レポート SQL Verb 0311 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0311C
    ```

    画面・出力には GDP12DD0311C が表示され、監査レポート SQL Verb 0311 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0311A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0311B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0311C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0326 {#c10-i0474}
*分類: レポート*  ・  難易度: 中級

紫G計画0327ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紫G計画0327です。紫G計画0327は監査レポートの点検操作で監査レポートの判定欄を記録する記録紫G計画0327です。紫G計画0327ではジョブキューと取得時刻を採取票紫G計画0327へ残します。紫G計画0327ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紫G計画0327です。紫G計画0327の用語整理では監査レポートの対象値を実在出力で保管する記録紫G計画0327です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0326に関する障害切り分けの前提を確認しています。監査レポート Audit Task Status 0338の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはAudit Task Statusのユーザー活動と取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。
    - B. 機能の説明としては照会文 Verbのジョブキューと取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。 ✅
    - C. 機能の説明としてはInspection Engineでエージェント変更から InspectionEngine を読みである。エージェント変更からInspectiときはInspectionを防ぐ。
    - D. 機能の説明としては監視エージェントの監視エージェント状態と取得時刻を記録し・未承認監視エージェント接続を防ぐである。記録操作で証跡欄を照合するときは未承認監視エージェント接続を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ジョブ・照会文でBの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・計画）です。照合ジョブ・計画に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・計画・照会文です。比較監査レ・計画でA:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は照会文・計画・ジョブです。項目ジョブ・計画でC:の引継ぎ記録 IE09は「Inspection Engineでエージェ」を述べるため、正答側の照合軸は照会文・監査レ・ジョブです。仕様ジョブ・計画でD:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸は計画・照会文・ジョブです。用語ジョブ・計画という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0326**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0326について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.16
    Server IP 198.51.100.46
    Count 96
    確認コード GDP12DD0326A
    ```

    画面・出力には GDP12DD0326A が表示され、監査レポート SQL Verb 0326 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0326
    Process Type Report
    Status completed
    確認コード GDP12DD0326B
    ```

    画面・出力には GDP12DD0326B が表示され、監査レポート SQL Verb 0326 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0326C
    ```

    画面・出力には GDP12DD0326C が表示され、監査レポート SQL Verb 0326 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0326A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0326B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0326C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0341 {#c10-i0475}
*分類: レポート*  ・  難易度: 上級

橙B解除0342ではIBM Guardium Data Protection 12.x の レポートを扱う採取票橙B解除0342です。橙B解除0342は監査レポートの復旧操作で監査レポートの点検欄を確認する記録橙B解除0342です。橙B解除0342ではジョブキューと取得時刻を採取票橙B解除0342へ残します。橙B解除0342では監査タスク未レビューを避けるため補助資料も照合する判断橙B解除0342です。橙B解除0342の用語整理では監査レポートの対象値を実在出力で点検する記録橙B解除0342です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0341を保守記録に説明する必要があります。audit process 状態確認 開始時刻と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は監査要件に沿ってレポート実行とレビューを束ねる処理である。状態確認で開始時刻を確認するときは開始時刻の誤読を防ぐ。
    - B. 運用時に利用する技術的役割はClient IPの監査タスクと取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。
    - C. 運用時に利用する技術的役割は照会文 Verbのジョブキューと取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。 ✅
    - D. 運用時に利用する技術的役割は監視エージェントの監視エージェント状態と取得時刻を記録し・ローカル通信制御監視の未確認を防ぐである。保守操作で監査欄を保存するときはローカル通信制御監視の未確認を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能ジョブ・監査タでCの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・解除）です。照合ジョブ・解除に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・解除・監査タです。比較監査レ・解除でA:の状態確認 開始時刻は「監査要件に沿ってレポート実行とレビューを束ね」を述べるため、正答側の照合軸は照会文・解除・ジョブです。運用解除・照会文でB:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸はジョブ・監査レ・解除です。仕様ジョブ・解除でD:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸は解除・監査タ・ジョブです。用語ジョブ・解除という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0341**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0341について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.31
    Server IP 198.51.100.61
    Count 111
    確認コード GDP12DD0341A
    ```

    画面・出力には GDP12DD0341A が表示され、監査レポート SQL Verb 0341 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0341
    Process Type Report
    Status completed
    確認コード GDP12DD0341B
    ```

    画面・出力には GDP12DD0341B が表示され、監査レポート SQL Verb 0341 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0341C
    ```

    画面・出力には GDP12DD0341C が表示され、監査レポート SQL Verb 0341 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0341A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0341B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0341C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート SQL Verb 0356 {#c10-i0476}
*分類: レポート*  ・  難易度: 上級

青Q解除0357ではIBM Guardium Data Protection 12.x の レポートを扱う採取票青Q解除0357です。青Q解除0357は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録青Q解除0357です。青Q解除0357ではジョブキューと取得時刻を採取票青Q解除0357へ残します。青Q解除0357では対象データソースの取り違えを避けるため補助資料も照合する判断青Q解除0357です。青Q解除0357の用語整理では監査レポートの対象値を実在出力で整理する記録青Q解除0357です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート SQL Verb 0356の技術的な意味を資料で確認するとき、監査プロセス Audit Process Builder 容量余力の確認との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は実行間隔より短いFROM/TO範を避けるため・プロセス一覧からScheduleを読むしてプロセス一覧を照合する。
    - B. 構成を確認する際の意味はローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するして最終応答を照合する。
    - C. 構成を確認する際の意味はジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するしてユーザー活動を照合する。
    - D. 構成を確認する際の意味は対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてジョブキューを照合する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能ジョブ・対象デでDの記述「照会文 Verbのジョブキューと取得時刻を記録し」に対応する項目はSQL Verb（照会文・ジョブ・解除）です。照合ジョブ・解除に関するレポートの仕様は「照会文 Verbのジョブキューと取得時刻を記録し」で、確認対象はジョブ・解除・対象デです。比較監査レ・解除でA:の容量余力の確認 AUDIT16は「Audit Processでプロセス一覧から」を述べるため、正答側の照合軸は照会文・解除・ジョブです。運用解除・照会文でB:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はジョブ・監査レ・解除です。項目ジョブ・解除でC:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は対象デ・監査レ・ジョブです。用語ジョブ・解除という用語は「照会文 Verbのジョブキューと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・ジョブ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート SQL Verb 0356**

    - 検証目的: 監査レポートの監査レポート SQL Verb 0356について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SQL Verb と ジョブキュー
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.46
    Server IP 198.51.100.76
    Count 126
    確認コード GDP12DD0356A
    ```

    画面・出力には GDP12DD0356A が表示され、監査レポート SQL Verb 0356 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0356
    Process Type Report
    Status completed
    確認コード GDP12DD0356B
    ```

    画面・出力には GDP12DD0356B が表示され、監査レポート SQL Verb 0356 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。SQL Verb を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0356C
    ```

    画面・出力には GDP12DD0356C が表示され、監査レポート SQL Verb 0356 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0356A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0356B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0356C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0002 {#c10-i0477}
*分類: レポート*  ・  難易度: 初級

緑C巡回0003ではIBM Guardium Data Protection 12.x の レポートを扱う採取票緑C巡回0003です。緑C巡回0003は監査レポートの点検操作で監査レポートの判定欄を記録する記録緑C巡回0003です。緑C巡回0003ではデータソースと取得時刻を採取票緑C巡回0003へ残します。緑C巡回0003ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断緑C巡回0003です。緑C巡回0003の用語整理では監査レポートの対象値を実在出力で保管する記録緑C巡回0003です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0002の役割を調べています。ロールと権限 Login Name 0039の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはLogin Nameのロール割当と取得時刻を記録し・GuardAPI実行権限不足を防ぐである。監査操作で記録欄を比較するときはGuardAPI実行権限不足を防ぐ。
    - B. 機能の説明としてはS-TAPのS-TAP状態と取得時刻を記録し・KTAP導入状態の誤読を防ぐである。採取操作で照合欄を点検するときはカーネル監視導入状態の誤読を防ぐ。
    - C. 機能の説明としてはServer IPのデータソースと取得時刻を記録し・SQL動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。 ✅
    - D. 機能の説明としては監査要件に沿ってレポート実行とレビューを束ねる処理を承認履歴確認する。保護設定で保護設定を確認するときは保護設定の誤読を防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 巡回対象データソーでCの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Serve・巡回・データ・照会文動）です。巡回時のデータソーに関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はServ・巡回・データ・照会文動です。Lo・棚卸・ロール割のA:は「Login Nameのロール割当と取得時刻を記録し」を述べ、対象はLogin Name（Login・棚卸・ロール・Guar）です。収集対象監視エージのB:は「S-TAPのS-TAP状態と取得時刻を記録し」を述べ、対象はKTAP Installed（監視エージ・収集・監視エ・カーネル）です。保護設定を保護設定のD:は「監査要件に沿ってレポート実行とレビューを束ねる処理を承認履歴確認する」を述べ、対象は承認履歴確認 保護設定（audit・保護設・保護設・保護設定）です。データソーを巡回という用語は「Server IPのデータソースと取得時刻を記録し」を指し、Server IP（Serve・巡回・データ・照会文動）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0002**

    - 検証目的: 監査レポートの監査レポート Server IP 0002について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0002A
    ```

    画面・出力には GDP12DD0002A が表示され、監査レポート Server IP 0002 の入力欄確認を確認できます。

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
    Process Run ID GDP0002
    Process Type Report
    Status completed
    確認コード GDP12DD0002B
    ```

    画面・出力には GDP12DD0002B が表示され、監査レポート Server IP 0002 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0002C
    ```

    画面・出力には GDP12DD0002C が表示され、監査レポート Server IP 0002 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0002A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0002B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0002C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0017 {#c10-i0478}
*分類: レポート*  ・  難易度: 初級

藤R巡回0018ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藤R巡回0018です。藤R巡回0018は監査レポートの復旧操作で監査レポートの点検欄を確認する記録藤R巡回0018です。藤R巡回0018ではデータソースと取得時刻を採取票藤R巡回0018へ残します。藤R巡回0018では監査タスク未レビューを避けるため補助資料も照合する判断藤R巡回0018です。藤R巡回0018の用語整理では監査レポートの対象値を実在出力で点検する記録藤R巡回0018です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート Server IP 0017」を「監査レポート Audit Task Status 0098」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はAudit Task Statusのユーザー活動と取得時刻を記録し・SQL動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。
    - B. 運用時に利用する技術的役割はServer IPのデータソースと取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。 ✅
    - C. 運用時に利用する技術的役割はRoleのLDAP取込と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。
    - D. 運用時に利用する技術的役割はCentral ManagerでCentral Managerの役割と出力を確認する。Centraで引継ぎ記録を確認するときはmanaged unitからを防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 巡回対象データソーでBの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Serve・巡回・データ・監査タス）です。巡回時のデータソーに関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はServ・巡回・データ・監査タスです。Au・変更・ユーザーのA:は「Audit Task Statusのユーザー活動と取得時刻を記録し」を述べ、対象はTask Status（Audit・変更・ユーザ・照会文動）です。照合時のディレクトのC:は「RoleのLDAP取込と取得時刻を記録し、過剰ロール付与を防ぐ」を述べ、対象はロールと権限 Role（Role・照合・ディレ・過剰ロー）です。引継ぎ記録をCentrのD:は「Central ManagerでCentral」を述べ、対象は引継ぎ記録 CM09（Centr・Cen・引継ぎ・mana）です。データソーを巡回という用語は「Server IPのデータソースと取得時刻を記録し」を指し、Server IP（Serve・巡回・データ・監査タス）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0017**

    - 検証目的: 監査レポートの監査レポート Server IP 0017について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0017A
    ```

    画面・出力には GDP12DD0017A が表示され、監査レポート Server IP 0017 の入力欄確認を確認できます。

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
    Process Run ID GDP0017
    Process Type Report
    Status completed
    確認コード GDP12DD0017B
    ```

    画面・出力には GDP12DD0017B が表示され、監査レポート Server IP 0017 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0017C
    ```

    画面・出力には GDP12DD0017C が表示され、監査レポート Server IP 0017 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0017A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0017B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0017C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0032 {#c10-i0479}
*分類: レポート*  ・  難易度: 中級

桃M棚卸0033ではIBM Guardium Data Protection 12.x の レポートを扱う採取票桃M棚卸0033です。桃M棚卸0033は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録桃M棚卸0033です。桃M棚卸0033ではデータソースと取得時刻を採取票桃M棚卸0033へ残します。桃M棚卸0033では対象データソースの取り違えを避けるため補助資料も照合する判断桃M棚卸0033です。桃M棚卸0033の用語整理では監査レポートの対象値を実在出力で整理する記録桃M棚卸0033です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0032を同一分類のS-TAP監視 S-TAP Version 0088と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するして暗号化表示を照合する。
    - B. 構成を確認する際の意味は対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてデータソースを照合する。 ✅
    - C. 構成を確認する際の意味は監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するしてディレクトリを照合する。
    - D. 構成を確認する際の意味はmanaged unitからのデを避けるため・世代整合確認で確認では中央を確認するして確認では中央を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 棚卸対象データソーでBの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Serve・棚卸・データ・対象デー）です。棚卸時のデータソーに関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はServ・棚卸・データ・対象デーです。監視・変更・暗号化表のA:は「S-TAPの暗号化表示と取得時刻を記録し」を述べ、対象はS-TAP Version（監視エージ・変更・暗号化・ローカル）です。照合時のディレクトのC:は「RoleのLDAP取込と取得時刻を記録し」を述べ、対象はロールと権限 Role（Role・照合・ディレ・監査担当）です。確認では中を世代整合確のD:は「Central Managerで世代整合の確認では中央管理サーバーの」を述べ、対象は世代整合の確認 CM17（Centr・世代整・確認で・mana）です。データソーを棚卸という用語は「Server IPのデータソースと取得時刻を記録し」を指し、Server IP（Serve・棚卸・データ・対象デー）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0032**

    - 検証目的: 監査レポートの監査レポート Server IP 0032について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0032A
    ```

    画面・出力には GDP12DD0032A が表示され、監査レポート Server IP 0032 の入力欄確認を確認できます。

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
    Process Run ID GDP0032
    Process Type Report
    Status completed
    確認コード GDP12DD0032B
    ```

    画面・出力には GDP12DD0032B が表示され、監査レポート Server IP 0032 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0032C
    ```

    画面・出力には GDP12DD0032C が表示され、監査レポート Server IP 0032 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0032A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0032B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0032C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0047 {#c10-i0480}
*分類: レポート*  ・  難易度: 中級

茶H復旧0048ではIBM Guardium Data Protection 12.x の レポートを扱う採取票茶H復旧0048です。茶H復旧0048は監査レポートの表示操作で監査レポートの対象欄を追跡する記録茶H復旧0048です。茶H復旧0048ではデータソースと取得時刻を採取票茶H復旧0048へ残します。茶H復旧0048ではジョブ失敗の見落としを避けるため補助資料も照合する判断茶H復旧0048です。茶H復旧0048の用語整理では監査レポートの対象値を実在出力で照合する記録茶H復旧0048です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0047の設定や表示を読む前に役割を確認します。ロールと権限 Permission 0063ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは表示操作で対象欄を追跡することでデータソースを確認し・ジョブ失敗の見落としを防ぐ。 ✅
    - B. 状態を読み取るための働きは監査操作で記録欄を比較することで表示可能レポを確認し・GuardAPI実行権限不足を防ぐ。
    - C. 状態を読み取るための働きは監査操作で記録欄を比較することでGuardAを確認し・GuardAPI実行権限不足を防ぐ。
    - D. 状態を読み取るための働きは構成監査で構成監査ではを確認することで構成監査ではを確認し・集約遅延中の期間を監査完了とを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 復旧対象データソーでAの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Serve・復旧・データ・ジョブ失）です。復旧時のデータソーに関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はServ・復旧・データ・ジョブ失です。監査対象表示可能レのB:は「Permissionの表示可能レポートと取得時刻を記録し」を述べ、対象はロールと権限 Permission（Permi・監査・表示可・Guar）です。照合時のGuardのC:は「LDAP UserのGuardAPI権限と取得時刻を記録し」を述べ、対象はLDAP User（ディレクト・照合・Gua・Guar）です。構成監査でを構成監査のD:は「Aggregatorで構成監査では監査データ集約管理の」を述べ、対象は構成監査 AGG08（Aggre・構成監・構成監・集約遅延）です。データソーを復旧という用語は「Server IPのデータソースと取得時刻を記録し」を指し、Server IP（Serve・復旧・データ・ジョブ失）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0047**

    - 検証目的: 監査レポートの監査レポート Server IP 0047について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0047A
    ```

    画面・出力には GDP12DD0047A が表示され、監査レポート Server IP 0047 の入力欄確認を確認できます。

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
    Process Run ID GDP0047
    Process Type Report
    Status completed
    確認コード GDP12DD0047B
    ```

    画面・出力には GDP12DD0047B が表示され、監査レポート Server IP 0047 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0047C
    ```

    画面・出力には GDP12DD0047C が表示され、監査レポート Server IP 0047 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0047A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0047B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0047C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0062 {#c10-i0481}
*分類: レポート*  ・  難易度: 中級

緑C監査0063ではIBM Guardium Data Protection 12.x の レポートを扱う採取票緑C監査0063です。緑C監査0063は監査レポートの点検操作で監査レポートの判定欄を記録する記録緑C監査0063です。緑C監査0063ではデータソースと取得時刻を採取票緑C監査0063へ残します。緑C監査0063ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断緑C監査0063です。緑C監査0063の用語整理では監査レポートの対象値を実在出力で保管する記録緑C監査0063です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0062に関する障害切り分けの前提を確認しています。ロールと権限 Permission 0078の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはPermissionの表示可能レポートと取得時刻を記録し・ディレクトリー取込対象の誤りを防ぐである。変更確認操作で採取欄を棚卸するときはディレクトリー取込対象の誤りを防ぐ。
    - B. 機能の説明としてはClient IPの監査タスクと取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。
    - C. 機能の説明としてはInspection Engineでポリシー変更から Policy を読み・Policy とである。ポリシー変更からPolicyを読むときはInspectionを防ぐ。
    - D. 機能の説明としてはServer IPのデータソースと取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能データ・照会文でDの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・監査）です。照合データ・監査に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・監査・照会文です。比較監査レ・監査でA:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はSer・監査・データです。運用監査・SerでB:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸はデータ・監査レ・監査です。項目データ・監査でC:の世代整合の確認 IE17は「Inspection Engineでポリシー」を述べるため、正答側の照合軸は照会文・監査レ・データです。用語データ・監査という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0062**

    - 検証目的: 監査レポートの監査レポート Server IP 0062について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0062A
    ```

    画面・出力には GDP12DD0062A が表示され、監査レポート Server IP 0062 の入力欄確認を確認できます。

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
    Process Run ID GDP0062
    Process Type Report
    Status completed
    確認コード GDP12DD0062B
    ```

    画面・出力には GDP12DD0062B が表示され、監査レポート Server IP 0062 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0062C
    ```

    画面・出力には GDP12DD0062C が表示され、監査レポート Server IP 0062 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0062A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0062B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0062C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0077 {#c10-i0482}
*分類: レポート*  ・  難易度: 中級

藤R監査0078ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藤R監査0078です。藤R監査0078は監査レポートの復旧操作で監査レポートの点検欄を確認する記録藤R監査0078です。藤R監査0078ではデータソースと取得時刻を採取票藤R監査0078へ残します。藤R監査0078では監査タスク未レビューを避けるため補助資料も照合する判断藤R監査0078です。藤R監査0078の用語整理では監査レポートの対象値を実在出力で点検する記録藤R監査0078です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0077を保守記録に説明する必要があります。S-TAP監視 S-TAP Version 0118と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は移行で暗号化表示を証跡に残し・監視エージェントの暗号化表示と取得時刻を記録し。
    - B. 運用時に利用する技術的役割は監査でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。 ✅
    - C. 運用時に利用する技術的役割は抑止で承認クライアを証跡に残し・監視エージェントの承認クライアントと取得時刻を記録し。
    - D. 運用時に利用する技術的役割は権限境界確認で変更履歴を証跡に残し・Guardiumで変更履歴から Operation を読み。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能データ・監査タでBの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・監査）です。照合データ・監査に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・監査・監査タです。比較監査レ・監査でA:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はSer・監査・データです。項目データ・監査でC:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は監査タ・監査レ・データです。仕様データ・監査でD:の権限境界の確認 DSRC12は「Guardiumで変更履歴から」を述べるため、正答側の照合軸は監査・監査タ・データです。用語データ・監査という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0077**

    - 検証目的: 監査レポートの監査レポート Server IP 0077について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0077A
    ```

    画面・出力には GDP12DD0077A が表示され、監査レポート Server IP 0077 の入力欄確認を確認できます。

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
    Process Run ID GDP0077
    Process Type Report
    Status completed
    確認コード GDP12DD0077B
    ```

    画面・出力には GDP12DD0077B が表示され、監査レポート Server IP 0077 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0077C
    ```

    画面・出力には GDP12DD0077C が表示され、監査レポート Server IP 0077 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0077A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0077B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0077C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0092 {#c10-i0483}
*分類: レポート*  ・  難易度: 中級

桃M変更0093ではIBM Guardium Data Protection 12.x の レポートを扱う採取票桃M変更0093です。桃M変更0093は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録桃M変更0093です。桃M変更0093ではデータソースと取得時刻を採取票桃M変更0093へ残します。桃M変更0093では対象データソースの取り違えを避けるため補助資料も照合する判断桃M変更0093です。桃M変更0093の用語整理では監査レポートの対象値を実在出力で整理する記録桃M変更0093です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0092の技術的な意味を資料で確認するとき、S-TAP監視 Last Response 0172との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は監視エージェントのカーネル監視有無と取得時刻を記録し・ローカル通信制御監視の未確認を防ぐである。保守操作で監査欄を保存するときはローカル通信制御監視の未確認を防ぐ。
    - B. 構成を確認する際の意味はデータベース User Nameの照会文動詞集計と取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。
    - C. 構成を確認する際の意味はAppliance Monitoriでジョブキューから JobName を読み・JobName とである。ジョブキューからJobNameを読むときはディスク逼迫中に検査データ流を防ぐ。
    - D. 構成を確認する際の意味はServer IPのデータソースと取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能データ・対象デでDの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・変更）です。照合データ・変更に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・変更・対象デです。比較監査レ・変更でA:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はSer・変更・データです。運用変更・SerでB:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸はデータ・監査レ・変更です。項目データ・変更でC:の再始動後の確認 APP15は「Appliance Monitoriでジョブ」を述べるため、正答側の照合軸は対象デ・監査レ・データです。用語データ・変更という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0092**

    - 検証目的: 監査レポートの監査レポート Server IP 0092について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0092A
    ```

    画面・出力には GDP12DD0092A が表示され、監査レポート Server IP 0092 の入力欄確認を確認できます。

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
    Process Run ID GDP0092
    Process Type Report
    Status completed
    確認コード GDP12DD0092B
    ```

    画面・出力には GDP12DD0092B が表示され、監査レポート Server IP 0092 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0092C
    ```

    画面・出力には GDP12DD0092C が表示され、監査レポート Server IP 0092 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0092A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0092B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0092C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0107 {#c10-i0484}
*分類: レポート*  ・  難易度: 上級

茶H移行0108ではIBM Guardium Data Protection 12.x の レポートを扱う採取票茶H移行0108です。茶H移行0108は監査レポートの表示操作で監査レポートの対象欄を追跡する記録茶H移行0108です。茶H移行0108ではデータソースと取得時刻を採取票茶H移行0108へ残します。茶H移行0108ではジョブ失敗の見落としを避けるため補助資料も照合する判断茶H移行0108です。茶H移行0108の用語整理では監査レポートの対象値を実在出力で照合する記録茶H移行0108です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0107について構成や状態を確認します。ロールと権限 Login Name 0114ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはLogin Nameのロール割当と取得時刻を記録し・ディレクトリー取込対象の誤りを防ぐである。変更確認操作で採取欄を棚卸するときはディレクトリー取込対象の誤りを防ぐ。
    - B. 状態を読み取るための働きはServer IPのデータソースと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。 ✅
    - C. 状態を読み取るための働きはAudit Task Statusのユーザー活動と取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。
    - D. 状態を読み取るための働きはCentral Managerで性能影響の確認では中央管理サーバーの 例外レポートから Exceptionである。性能影響確認で確認では中央を確認するときはmanaged unitからを防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能データ・ジョブでBの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・移行）です。照合データ・移行に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・移行・ジョブです。比較監査レ・移行でA:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸はSer・移行・データです。項目データ・移行でC:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸はジョブ・監査レ・データです。仕様データ・移行でD:の性能影響の確認 CM11は「Central Managerで性能影響の確」を述べるため、正答側の照合軸は移行・ジョブ・データです。用語データ・移行という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0107**

    - 検証目的: 監査レポートの監査レポート Server IP 0107について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0107A
    ```

    画面・出力には GDP12DD0107A が表示され、監査レポート Server IP 0107 の入力欄確認を確認できます。

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
    Process Run ID GDP0107
    Process Type Report
    Status completed
    確認コード GDP12DD0107B
    ```

    画面・出力には GDP12DD0107B が表示され、監査レポート Server IP 0107 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0107C
    ```

    画面・出力には GDP12DD0107C が表示され、監査レポート Server IP 0107 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0107A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0107B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0107C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0122 {#c10-i0485}
*分類: レポート*  ・  難易度: 初級

緑C診断0123ではIBM Guardium Data Protection 12.x の レポートを扱う採取票緑C診断0123です。緑C診断0123は監査レポートの点検操作で監査レポートの判定欄を記録する記録緑C診断0123です。緑C診断0123ではデータソースと取得時刻を採取票緑C診断0123へ残します。緑C診断0123ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断緑C診断0123です。緑C診断0123の用語整理では監査レポートの対象値を実在出力で保管する記録緑C診断0123です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0122の役割を調べています。S-TAP監視 Last Response 0202の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては登録でカーネル監視を証跡に残し・監視エージェントのカーネル監視有無と取得時刻を記録し。
    - B. 機能の説明としてはレポートで出力見出しを証跡に残し・I/O 指標を収集するサポートCLIコマンドを障害時切り分け。
    - C. 機能の説明としては診断でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。 ✅
    - D. 機能の説明としては巡回で最終応答を証跡に残し・監視エージェントの最終応答と取得時刻を記録し。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能データ・照会文でCの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・診断）です。照合データ・診断に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・診断・照会文です。比較監査レ・診断でA:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はSer・診断・データです。運用診断・SerでB:の障害時切り分け 出力見出しは「I/O 指標を収集するサポートCLIコマンド」を述べるため、正答側の照合軸はデータ・監査レ・診断です。仕様データ・診断でD:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は診断・照会文・データです。用語データ・診断という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0122**

    - 検証目的: 監査レポートの監査レポート Server IP 0122について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0122A
    ```

    画面・出力には GDP12DD0122A が表示され、監査レポート Server IP 0122 の入力欄確認を確認できます。

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
    Process Run ID GDP0122
    Process Type Report
    Status completed
    確認コード GDP12DD0122B
    ```

    画面・出力には GDP12DD0122B が表示され、監査レポート Server IP 0122 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0122C
    ```

    画面・出力には GDP12DD0122C が表示され、監査レポート Server IP 0122 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0122A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0122B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0122C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0137 {#c10-i0486}
*分類: レポート*  ・  難易度: 初級

藤R診断0138ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藤R診断0138です。藤R診断0138は監査レポートの復旧操作で監査レポートの点検欄を確認する記録藤R診断0138です。藤R診断0138ではデータソースと取得時刻を採取票藤R診断0138へ残します。藤R診断0138では監査タスク未レビューを避けるため補助資料も照合する判断藤R診断0138です。藤R診断0138の用語整理では監査レポートの対象値を実在出力で点検する記録藤R診断0138です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート Server IP 0137」を「S-TAP監視 Last Response 0187」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するしてデータソースを照合する。 ✅
    - B. 運用時に利用する技術的役割はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するしてカーネル監視を照合する。
    - C. 運用時に利用する技術的役割はドメイン値の誤読を避けるため・承認履歴確認でドメイン値を確認するしてドメイン値を照合する。
    - D. 運用時に利用する技術的役割はディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてユーザー有効を照合する。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能データ・監査タでAの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・診断）です。照合データ・診断に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・診断・監査タです。運用診断・SerでB:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はデータ・監査レ・診断です。項目データ・診断でC:の承認履歴確認 ドメイン値は「データベース通信を解析し監査レコードを作る処」を述べるため、正答側の照合軸は監査タ・監査レ・データです。仕様データ・診断でD:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は診断・監査タ・データです。用語データ・診断という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0137**

    - 検証目的: 監査レポートの監査レポート Server IP 0137について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0137A
    ```

    画面・出力には GDP12DD0137A が表示され、監査レポート Server IP 0137 の入力欄確認を確認できます。

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
    Process Run ID GDP0137
    Process Type Report
    Status completed
    確認コード GDP12DD0137B
    ```

    画面・出力には GDP12DD0137B が表示され、監査レポート Server IP 0137 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0137C
    ```

    画面・出力には GDP12DD0137C が表示され、監査レポート Server IP 0137 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0137A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0137B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0137C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0152 {#c10-i0487}
*分類: レポート*  ・  難易度: 中級

桃M保守0153ではIBM Guardium Data Protection 12.x の レポートを扱う採取票桃M保守0153です。桃M保守0153は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録桃M保守0153です。桃M保守0153ではデータソースと取得時刻を採取票桃M保守0153へ残します。桃M保守0153では対象データソースの取り違えを避けるため補助資料も照合する判断桃M保守0153です。桃M保守0153の用語整理では監査レポートの対象値を実在出力で整理する記録桃M保守0153です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0152を同一分類のS-TAP監視 DB Server Type 0190と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は確認操作で状態欄を整理することで承認クライアを確認し・最終応答停止の見落としを防ぐ。
    - B. 構成を確認する際の意味は承認履歴確認で復元前提を確認することで復元前提を確認し・復元前提の誤読を防ぐ。datasource 承認履歴確認 復元前提固有の属性も確認対象に含める。
    - C. 構成を確認する際の意味は調査操作で保守欄を引き継ぎすることでデータソースを確認し・対象データソースの取り違えを防ぐ。 ✅
    - D. 構成を確認する際の意味は保守操作で監査欄を保存することで暗号化表示を確認し・ローカル通信制御監視の未確認を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能データ・対象デでCの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・保守）です。照合データ・保守に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・保守・対象デです。比較監査レ・保守でA:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はSer・保守・データです。運用保守・SerでB:の承認履歴確認 復元前提は「監視対象データベースやサービスを表す」を述べるため、正答側の照合軸はデータ・監査レ・保守です。仕様データ・保守でD:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は保守・対象デ・データです。用語データ・保守という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0152**

    - 検証目的: 監査レポートの監査レポート Server IP 0152について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0152A
    ```

    画面・出力には GDP12DD0152A が表示され、監査レポート Server IP 0152 の入力欄確認を確認できます。

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
    Process Run ID GDP0152
    Process Type Report
    Status completed
    確認コード GDP12DD0152B
    ```

    画面・出力には GDP12DD0152B が表示され、監査レポート Server IP 0152 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0152C
    ```

    画面・出力には GDP12DD0152C が表示され、監査レポート Server IP 0152 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0152A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0152B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0152C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Server IP 0167 {#c10-i0488}
*分類: レポート*  ・  難易度: 中級

茶H切替0168ではIBM Guardium Data Protection 12.x の レポートを扱う採取票茶H切替0168です。茶H切替0168は監査レポートの表示操作で監査レポートの対象欄を追跡する記録茶H切替0168です。茶H切替0168ではデータソースと取得時刻を採取票茶H切替0168へ残します。茶H切替0168ではジョブ失敗の見落としを避けるため補助資料も照合する判断茶H切替0168です。茶H切替0168の用語整理では監査レポートの対象値を実在出力で照合する記録茶H切替0168です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Server IP 0167の設定や表示を読む前に役割を確認します。S-TAP監視 Last Response 0262ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するしてデータソースを照合する。 ✅
    - B. 状態を読み取るための働きは最終応答停止の見落としを避けるため・確認操作で状態欄を整理するしてカーネル監視を照合する。
    - C. 状態を読み取るための働きは実行間隔より短いFROM/TO範を避けるため・報告上限からmax_audit_repoして報告上限を照合する。
    - D. 状態を読み取るための働きはディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてGuardAを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能データ・ジョブでAの記述「Server IPのデータソースと取得時刻を記録し」に対応する項目はServer IP（Ser・データ・切替）です。照合データ・切替に関するレポートの仕様は「Server IPのデータソースと取得時刻を記録し」で、確認対象はデータ・切替・ジョブです。運用切替・SerでB:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はデータ・監査レ・切替です。項目データ・切替でC:の引継ぎ記録 AUDIT09は「Audit Processで報告上限から」を述べるため、正答側の照合軸はジョブ・監査レ・データです。仕様データ・切替でD:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は切替・ジョブ・データです。用語データ・切替という用語は「Server IPのデータソースと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・データ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Server IP 0167**

    - 検証目的: 監査レポートの監査レポート Server IP 0167について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0167A
    ```

    画面・出力には GDP12DD0167A が表示され、監査レポート Server IP 0167 の入力欄確認を確認できます。

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
    Process Run ID GDP0167
    Process Type Report
    Status completed
    確認コード GDP12DD0167B
    ```

    画面・出力には GDP12DD0167B が表示され、監査レポート Server IP 0167 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0167C
    ```

    画面・出力には GDP12DD0167C が表示され、監査レポート Server IP 0167 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0167A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0167B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0167C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


