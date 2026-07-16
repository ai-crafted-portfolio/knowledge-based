---
search:
  exclude: true
---

# IBM Guardium Data Protection 12.x — 詳細 (7/12)

[← IBM Guardium Data Protection 12.x の概要へ戻る](index.md)


## IBM Guardium Data Protection 12.x > アクセス管理

### ロールと権限 Role 0126 {#c10-i0295}
*分類: アクセス管理*  ・  難易度: 初級

紫G診断0127ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票紫G診断0127です。紫G診断0127はロール権限管理の変更確認操作でロール権限管理の採取欄を棚卸する記録紫G診断0127です。紫G診断0127ではLDAP取込と取得時刻を採取票紫G診断0127へ残します。紫G診断0127ではLDAP取込対象の誤りを避けるため補助資料も照合する判断紫G診断0127です。紫G診断0127の用語整理ではロール権限管理の対象値を実在出力で説明する記録紫G診断0127です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0126に関する障害切り分けの前提を確認しています。S-TAP監視 DB Server Type 0220の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は確認で承認クライアを証跡に残し・監視エージェントの承認クライアントと取得時刻を記録し。
    - B. 表示や設定で扱う内容は計画でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。
    - C. 表示や設定で扱う内容は診断でディレクトリを証跡に残し・Roleのディレクトリー取込と取得時刻を記録し。 ✅
    - D. 表示や設定で扱う内容は停止確認で監査タスクを証跡に残し・Aggregatorで監査タスクから。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能ディレ・ディレでCの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・診断）です。照合ディレ・診断に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・診断・ディレです。比較ロール・診断でA:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はRol・診断・ディレです。運用診断・RolでB:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸はディレ・ロール・診断です。仕様ディレ・診断でD:の停止前の確認 AGG14は「Aggregatorで監査タスクから」を述べるため、正答側の照合軸は診断・ディレ・ディレです。用語ディレ・診断という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・ディレです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0126**

    - 検証目的: ロールと権限のロールと権限 Role 0126について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor006
    Role auditor
    Account enabled yes
    確認コード GDP12DD0126A
    ```

    画面・出力には GDP12DD0126A が表示され、ロールと権限 Role 0126 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0126B
    ```

    画面・出力には GDP12DD0126B が表示され、ロールと権限 Role 0126 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 11
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0126C
    ```

    画面・出力には GDP12DD0126C が表示され、ロールと権限 Role 0126 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0126A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0126B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0126C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0141 {#c10-i0296}
*分類: アクセス管理*  ・  難易度: 初級

橙B保守0142ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票橙B保守0142です。橙B保守0142はロール権限管理の主操作でロール権限管理の出力欄を評価する記録橙B保守0142です。橙B保守0142ではLDAP取込と取得時刻を採取票橙B保守0142へ残します。橙B保守0142では過剰ロール付与を避けるため補助資料も照合する判断橙B保守0142です。橙B保守0142の用語整理ではロール権限管理の対象値を実在出力で追跡する記録橙B保守0142です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0141を保守記録に説明する必要があります。ロールと権限 Login Name 0219と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はLogin Nameのロール割当と取得時刻を記録し・GuardAPI実行権限不足を防ぐである。監査操作で記録欄を比較するときはGuardAPI実行権限不足を防ぐ。
    - B. 保守作業で参照する機能はRoleのディレクトリー取込と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。 ✅
    - C. 保守作業で参照する機能は接続を許可された S-TAP と状態を確認する管理レポートを障害時切り分けとして確認する。レポートで転送条件を確認するときは転送条件の誤読を防ぐ。
    - D. 保守作業で参照する機能は監視エージェントのカーネル監視有無と取得時刻を記録し・カーネル監視導入状態の誤読を防ぐである。採取操作で照合欄を点検するときはカーネル監視導入状態の誤読を防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能ディレ・過剰ロでBの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・保守）です。照合ディレ・保守に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し、過剰ロール付与を防ぐ」で、確認対象はディレ・保守・過剰ロです。比較ロール・保守でA:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸はRol・保守・ディレです。項目ディレ・保守でC:の障害時切り分け 転送条件は「接続を許可された S-TAP」を述べるため、正答側の照合軸は過剰ロ・ロール・ディレです。仕様ディレ・保守でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は保守・過剰ロ・ディレです。用語ディレ・保守という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・過剰ロです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0141**

    - 検証目的: ロールと権限のロールと権限 Role 0141について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor021
    Role auditor
    Account enabled yes
    確認コード GDP12DD0141A
    ```

    画面・出力には GDP12DD0141A が表示され、ロールと権限 Role 0141 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0141B
    ```

    画面・出力には GDP12DD0141B が表示され、ロールと権限 Role 0141 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 6
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0141C
    ```

    画面・出力には GDP12DD0141C が表示され、ロールと権限 Role 0141 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0141A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0141B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0141C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0156 {#c10-i0297}
*分類: アクセス管理*  ・  難易度: 中級

青Q保守0157ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票青Q保守0157です。青Q保守0157はロール権限管理の照合操作でロール権限管理の確認欄を採取する記録青Q保守0157です。青Q保守0157ではLDAP取込と取得時刻を採取票青Q保守0157へ残します。青Q保守0157では監査担当者の閲覧範囲不足を避けるため補助資料も照合する判断青Q保守0157です。青Q保守0157の用語整理ではロール権限管理の対象値を実在出力で記録する記録青Q保守0157です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0156の技術的な意味を資料で確認するとき、S-TAP監視 KTAP Installed 0199との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は監視エージェントの監視エージェント状態と取得時刻を記録し・カーネル監視導入状態の誤読を防ぐである。採取操作で照合欄を点検するときはカーネル監視導入状態の誤読を防ぐ。
    - B. 管理対象との関係を表す説明はRoleのディレクトリー取込と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。 ✅
    - C. 管理対象との関係を表す説明はディレクトリー UserのGuardAPI権限と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。
    - D. 管理対象との関係を表す説明はデータベース User Nameの照会文動詞集計と取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ディレ・監査担でBの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・保守）です。照合ディレ・保守に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・保守・監査担です。比較ロール・保守でA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はRol・保守・ディレです。項目ディレ・保守でC:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は監査担・ロール・ディレです。仕様ディレ・保守でD:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は保守・監査担・ディレです。用語ディレ・保守という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・監査担です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0156**

    - 検証目的: ロールと権限のロールと権限 Role 0156について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor036
    Role auditor
    Account enabled yes
    確認コード GDP12DD0156A
    ```

    画面・出力には GDP12DD0156A が表示され、ロールと権限 Role 0156 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0156B
    ```

    画面・出力には GDP12DD0156B が表示され、ロールと権限 Role 0156 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 21
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0156C
    ```

    画面・出力には GDP12DD0156C が表示され、ロールと権限 Role 0156 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0156A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0156B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0156C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0171 {#c10-i0298}
*分類: アクセス管理*  ・  難易度: 中級

白L切替0172ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票白L切替0172です。白L切替0172はロール権限管理の監査操作でロール権限管理の記録欄を比較する記録白L切替0172です。白L切替0172ではLDAP取込と取得時刻を採取票白L切替0172へ残します。白L切替0172ではGuardAPI実行権限不足を避けるため補助資料も照合する判断白L切替0172です。白L切替0172の用語整理ではロール権限管理の対象値を実在出力で確認する記録白L切替0172です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0171について構成や状態を確認します。S-TAP監視 KTAP Installed 0229ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは記録操作で証跡欄を照合することで監視エージェを確認し・未承認監視エージェント接続を防ぐ。
    - B. 対象資源に対する働きはプロセス一覧からScheduleを読むことでプロセス一覧を確認し・実行間隔より短いFROM/Tを防ぐ。
    - C. 対象資源に対する働きは監査操作で記録欄を比較することでディレクトリを確認し・GuardAPI実行権限不足を防ぐ。 ✅
    - D. 対象資源に対する働きは復旧操作で点検欄を確認することで照会文動詞集を確認し・監査タスク未レビューを防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ディレ・GuaでCの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・切替）です。照合ディレ・切替に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・切替・Guaです。比較ロール・切替でA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はRol・切替・ディレです。運用切替・RolでB:の代替経路の確認 AUDIT10は「Audit Processでプロセス一覧から」を述べるため、正答側の照合軸はディレ・ロール・切替です。仕様ディレ・切替でD:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は切替・Gua・ディレです。用語ディレ・切替という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・Guaです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0171**

    - 検証目的: ロールと権限のロールと権限 Role 0171について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor051
    Role auditor
    Account enabled yes
    確認コード GDP12DD0171A
    ```

    画面・出力には GDP12DD0171A が表示され、ロールと権限 Role 0171 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0171B
    ```

    画面・出力には GDP12DD0171B が表示され、ロールと権限 Role 0171 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 16
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0171C
    ```

    画面・出力には GDP12DD0171C が表示され、ロールと権限 Role 0171 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0171A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0171B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0171C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0186 {#c10-i0299}
*分類: アクセス管理*  ・  難易度: 中級

紫G収集0187ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票紫G収集0187です。紫G収集0187はロール権限管理の変更確認操作でロール権限管理の採取欄を棚卸する記録紫G収集0187です。紫G収集0187ではLDAP取込と取得時刻を採取票紫G収集0187へ残します。紫G収集0187ではLDAP取込対象の誤りを避けるため補助資料も照合する判断紫G収集0187です。紫G収集0187の用語整理ではロール権限管理の対象値を実在出力で説明する記録紫G収集0187です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0186の役割を調べています。監査レポート Client IP 0275の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は照合で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。
    - B. 表示や設定で扱う内容は証跡採取で重大度を証跡に残し・監査要件に沿ってレポート実行とレビューを束ねる処理を証跡採取。
    - C. 表示や設定で扱う内容は収集でディレクトリを証跡に残し・Roleのディレクトリー取込と取得時刻を記録し。 ✅
    - D. 表示や設定で扱う内容は復旧で承認クライアを証跡に残し・監視エージェントの承認クライアントと取得時刻を記録し。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ディレ・ディレでCの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・収集）です。照合ディレ・収集に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・収集・ディレです。比較ロール・収集でA:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸はRol・収集・ディレです。運用収集・RolでB:の証跡採取 重大度は「監査要件に沿ってレポート実行とレビューを束ね」を述べるため、正答側の照合軸はディレ・ロール・収集です。仕様ディレ・収集でD:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は収集・ディレ・ディレです。用語ディレ・収集という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・ディレです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0186**

    - 検証目的: ロールと権限のロールと権限 Role 0186について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor066
    Role auditor
    Account enabled yes
    確認コード GDP12DD0186A
    ```

    画面・出力には GDP12DD0186A が表示され、ロールと権限 Role 0186 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0186B
    ```

    画面・出力には GDP12DD0186B が表示され、ロールと権限 Role 0186 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 11
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0186C
    ```

    画面・出力には GDP12DD0186C が表示され、ロールと権限 Role 0186 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0186A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0186B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0186C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0201 {#c10-i0300}
*分類: アクセス管理*  ・  難易度: 中級

橙B登録0202ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票橙B登録0202です。橙B登録0202はロール権限管理の主操作でロール権限管理の出力欄を評価する記録橙B登録0202です。橙B登録0202ではLDAP取込と取得時刻を採取票橙B登録0202へ残します。橙B登録0202では過剰ロール付与を避けるため補助資料も照合する判断橙B登録0202です。橙B登録0202の用語整理ではロール権限管理の対象値を実在出力で追跡する記録橙B登録0202です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「ロールと権限 Role 0201」を「ロールと権限 Application Access 0285」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は抑止でユーザー有効を証跡に残し・Application Accessのユーザー有効化と取得時。
    - B. 保守作業で参照する機能は登録でディレクトリを証跡に残し・Roleのディレクトリー取込と取得時刻を記録し。 ✅
    - C. 保守作業で参照する機能は再始動確認で再始動後の確を証跡に残し・Central ManagerでCentral。
    - D. 保守作業で参照する機能は変更でロール割当を証跡に残し・Login Nameのロール割当と取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ディレ・過剰ロでBの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・登録）です。照合ディレ・登録に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し、過剰ロール付与を防ぐ」で、確認対象はディレ・登録・過剰ロです。比較ロール・登録でA:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はRol・登録・ディレです。項目ディレ・登録でC:の再始動後の確認 CM15は「Central ManagerでCentra」を述べるため、正答側の照合軸は過剰ロ・ロール・ディレです。仕様ディレ・登録でD:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は登録・過剰ロ・ディレです。用語ディレ・登録という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・過剰ロです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0201**

    - 検証目的: ロールと権限のロールと権限 Role 0201について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor081
    Role auditor
    Account enabled yes
    確認コード GDP12DD0201A
    ```

    画面・出力には GDP12DD0201A が表示され、ロールと権限 Role 0201 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0201B
    ```

    画面・出力には GDP12DD0201B が表示され、ロールと権限 Role 0201 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 6
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0201C
    ```

    画面・出力には GDP12DD0201C が表示され、ロールと権限 Role 0201 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0201A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0201B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0201C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0216 {#c10-i0301}
*分類: アクセス管理*  ・  難易度: 中級

青Q登録0217ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票青Q登録0217です。青Q登録0217はロール権限管理の照合操作でロール権限管理の確認欄を採取する記録青Q登録0217です。青Q登録0217ではLDAP取込と取得時刻を採取票青Q登録0217へ残します。青Q登録0217では監査担当者の閲覧範囲不足を避けるため補助資料も照合する判断青Q登録0217です。青Q登録0217の用語整理ではロール権限管理の対象値を実在出力で記録する記録青Q登録0217です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0216を同一分類の監査レポート Client IP 0260と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はClient IPの監査タスクと取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。
    - B. 管理対象との関係を表す説明はS-TAP や外部接続から監査データを受け取る Guardium 装置を障害時切り分けとして確認する。S-TAPで回収対象を確認するときは回収対象の誤読を防ぐ。
    - C. 管理対象との関係を表す説明はディレクトリー UserのGuardAPI権限と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。
    - D. 管理対象との関係を表す説明はRoleのディレクトリー取込と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ディレ・監査担でDの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・登録）です。照合ディレ・登録に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・登録・監査担です。比較ロール・登録でA:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸はRol・登録・ディレです。運用登録・RolでB:の障害時切り分け 回収対象は「S-TAP や外部接続から監査データを受け取」を述べるため、正答側の照合軸はディレ・ロール・登録です。項目ディレ・登録でC:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は監査担・ロール・ディレです。用語ディレ・登録という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・監査担です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0216**

    - 検証目的: ロールと権限のロールと権限 Role 0216について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor096
    Role auditor
    Account enabled yes
    確認コード GDP12DD0216A
    ```

    画面・出力には GDP12DD0216A が表示され、ロールと権限 Role 0216 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0216B
    ```

    画面・出力には GDP12DD0216B が表示され、ロールと権限 Role 0216 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 21
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0216C
    ```

    画面・出力には GDP12DD0216C が表示され、ロールと権限 Role 0216 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0216A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0216B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0216C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0231 {#c10-i0302}
*分類: アクセス管理*  ・  難易度: 上級

白L確認0232ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票白L確認0232です。白L確認0232はロール権限管理の監査操作でロール権限管理の記録欄を比較する記録白L確認0232です。白L確認0232ではLDAP取込と取得時刻を採取票白L確認0232へ残します。白L確認0232ではGuardAPI実行権限不足を避けるため補助資料も照合する判断白L確認0232です。白L確認0232の用語整理ではロール権限管理の対象値を実在出力で確認する記録白L確認0232です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0231の設定や表示を読む前に役割を確認します。ロールと権限 Login Name 0309ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは主操作で出力欄を評価することでロール割当を確認し・過剰ロール付与を防ぐ。
    - B. 対象資源に対する働きはポリシー変更からPolicyを読むことでポリシー変更を確認し・Inspectionを防ぐ。
    - C. 対象資源に対する働きは監査操作で記録欄を比較することでディレクトリを確認し・GuardAPI実行権限不足を防ぐ。 ✅
    - D. 対象資源に対する働きは調査操作で保守欄を引き継ぎすることでユーザー活動を確認し・対象データソースの取り違えを防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能ディレ・GuaでCの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・確認）です。照合ディレ・確認に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・確認・Guaです。比較ロール・確認でA:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸はRol・確認・ディレです。運用確認・RolでB:の変更前の確認 IE02は「Inspection Engineでポリシー」を述べるため、正答側の照合軸はディレ・ロール・確認です。仕様ディレ・確認でD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は確認・Gua・ディレです。用語ディレ・確認という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・Guaです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0231**

    - 検証目的: ロールと権限のロールと権限 Role 0231について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor111
    Role auditor
    Account enabled yes
    確認コード GDP12DD0231A
    ```

    画面・出力には GDP12DD0231A が表示され、ロールと権限 Role 0231 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0231B
    ```

    画面・出力には GDP12DD0231B が表示され、ロールと権限 Role 0231 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 16
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0231C
    ```

    画面・出力には GDP12DD0231C が表示され、ロールと権限 Role 0231 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0231A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0231B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0231C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0246 {#c10-i0303}
*分類: アクセス管理*  ・  難易度: 初級

紫G保護0247ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票紫G保護0247です。紫G保護0247はロール権限管理の変更確認操作でロール権限管理の採取欄を棚卸する記録紫G保護0247です。紫G保護0247ではLDAP取込と取得時刻を採取票紫G保護0247へ残します。紫G保護0247ではLDAP取込対象の誤りを避けるため補助資料も照合する判断紫G保護0247です。紫G保護0247の用語整理ではロール権限管理の対象値を実在出力で説明する記録紫G保護0247です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0246に関する障害切り分けの前提を確認しています。S-TAP監視 DB Server Type 0340の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は保守操作で監査欄を保存することで承認クライアを確認し・ローカル通信制御監視の未確認を防ぐ。
    - B. 表示や設定で扱う内容はDB処理一覧からTURBINEを読むことでデータベースを確認し・ディスク逼迫中に検査データ流を防ぐ。
    - C. 表示や設定で扱う内容は変更確認操作で採取欄を棚卸することでディレクトリを確認し・ディレクトリー取込対象の誤りを防ぐ。 ✅
    - D. 表示や設定で扱う内容は復旧操作で点検欄を確認することでデータソースを確認し・監査タスク未レビューを防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能ディレ・ディレでCの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・保護）です。照合ディレ・保護に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・保護・ディレです。比較ロール・保護でA:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はRol・保護・ディレです。運用保護・RolでB:の変更前の確認 APP02は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸はディレ・ロール・保護です。仕様ディレ・保護でD:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は保護・ディレ・ディレです。用語ディレ・保護という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・ディレです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0246**

    - 検証目的: ロールと権限のロールと権限 Role 0246について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor006
    Role auditor
    Account enabled yes
    確認コード GDP12DD0246A
    ```

    画面・出力には GDP12DD0246A が表示され、ロールと権限 Role 0246 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0246B
    ```

    画面・出力には GDP12DD0246B が表示され、ロールと権限 Role 0246 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 11
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0246C
    ```

    画面・出力には GDP12DD0246C が表示され、ロールと権限 Role 0246 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0246A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0246B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0246C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0261 {#c10-i0304}
*分類: アクセス管理*  ・  難易度: 初級

橙B照合0262ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票橙B照合0262です。橙B照合0262はロール権限管理の主操作でロール権限管理の出力欄を評価する記録橙B照合0262です。橙B照合0262ではLDAP取込と取得時刻を採取票橙B照合0262へ残します。橙B照合0262では過剰ロール付与を避けるため補助資料も照合する判断橙B照合0262です。橙B照合0262の用語整理ではロール権限管理の対象値を実在出力で追跡する記録橙B照合0262です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0261を保守記録に説明する必要があります。ロールと権限 LDAP User 0267と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はディレクトリー UserのGuardAPI権限と取得時刻を記録し・GuardAPI実行権限不足を防ぐである。監査操作で記録欄を比較するときはGuardAPI実行権限不足を防ぐ。
    - B. 保守作業で参照する機能はInspection Engineで検査状態から LastResponse を読みである。検査状態からLastResponseときはInspectionを防ぐ。
    - C. 保守作業で参照する機能はLogin Nameのロール割当と取得時刻を記録し・GuardAPI実行権限不足を防ぐである。監査操作で記録欄を比較するときはGuardAPI実行権限不足を防ぐ。
    - D. 保守作業で参照する機能はRoleのディレクトリー取込と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能ディレ・過剰ロでDの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・照合）です。照合ディレ・照合に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し、過剰ロール付与を防ぐ」で、確認対象はディレ・照合・過剰ロです。比較ロール・照合でA:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸はRol・照合・ディレです。運用照合・RolでB:の代替経路の確認 IE10は「Inspection Engineで検査状態」を述べるため、正答側の照合軸はディレ・ロール・照合です。項目ディレ・照合でC:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は過剰ロ・ロール・ディレです。用語ディレ・照合という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・過剰ロです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0261**

    - 検証目的: ロールと権限のロールと権限 Role 0261について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor021
    Role auditor
    Account enabled yes
    確認コード GDP12DD0261A
    ```

    画面・出力には GDP12DD0261A が表示され、ロールと権限 Role 0261 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0261B
    ```

    画面・出力には GDP12DD0261B が表示され、ロールと権限 Role 0261 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 6
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0261C
    ```

    画面・出力には GDP12DD0261C が表示され、ロールと権限 Role 0261 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0261A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0261B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0261C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0276 {#c10-i0305}
*分類: アクセス管理*  ・  難易度: 中級

青Q照合0277ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票青Q照合0277です。青Q照合0277はロール権限管理の照合操作でロール権限管理の確認欄を採取する記録青Q照合0277です。青Q照合0277ではLDAP取込と取得時刻を採取票青Q照合0277へ残します。青Q照合0277では監査担当者の閲覧範囲不足を避けるため補助資料も照合する判断青Q照合0277です。青Q照合0277の用語整理ではロール権限管理の対象値を実在出力で記録する記録青Q照合0277です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0276の技術的な意味を資料で確認するとき、ロールと権限 LDAP User 0327との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は計画でGuardAを証跡に残し・ディレクトリー UserのGuardAPI権限と取得時刻を記。
    - B. 管理対象との関係を表す説明は照合でディレクトリを証跡に残し・Roleのディレクトリー取込と取得時刻を記録し。 ✅
    - C. 管理対象との関係を表す説明は容量余力確認で監視プロセスを証跡に残し・Appliance Monitoriで監視プロセスから。
    - D. 管理対象との関係を表す説明は切替で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ディレ・監査担でBの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・照合）です。照合ディレ・照合に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・照合・監査担です。比較ロール・照合でA:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸はRol・照合・ディレです。項目ディレ・照合でC:の容量余力の確認 APP16は「Appliance Monitoriで監視プ」を述べるため、正答側の照合軸は監査担・ロール・ディレです。仕様ディレ・照合でD:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸は照合・監査担・ディレです。用語ディレ・照合という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・監査担です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0276**

    - 検証目的: ロールと権限のロールと権限 Role 0276について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor036
    Role auditor
    Account enabled yes
    確認コード GDP12DD0276A
    ```

    画面・出力には GDP12DD0276A が表示され、ロールと権限 Role 0276 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0276B
    ```

    画面・出力には GDP12DD0276B が表示され、ロールと権限 Role 0276 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 21
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0276C
    ```

    画面・出力には GDP12DD0276C が表示され、ロールと権限 Role 0276 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0276A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0276B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0276C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0291 {#c10-i0306}
*分類: アクセス管理*  ・  難易度: 中級

白L抑止0292ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票白L抑止0292です。白L抑止0292はロール権限管理の監査操作でロール権限管理の記録欄を比較する記録白L抑止0292です。白L抑止0292ではLDAP取込と取得時刻を採取票白L抑止0292へ残します。白L抑止0292ではGuardAPI実行権限不足を避けるため補助資料も照合する判断白L抑止0292です。白L抑止0292の用語整理ではロール権限管理の対象値を実在出力で確認する記録白L抑止0292です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0291について構成や状態を確認します。S-TAP監視 Last Response 0337ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは未承認監視エージェント接続を避けるため・記録操作で証跡欄を照合するしてカーネル監視を照合する。
    - B. 対象資源に対する働きはInspectionを避けるため・エージェント変更からInspectionしてエージェントを照合する。
    - C. 対象資源に対する働きは未承認監視エージェント接続を避けるため・記録操作で証跡欄を照合するして最終応答を照合する。
    - D. 対象資源に対する働きはGuardAPI実行権限不足を避けるため・監査操作で記録欄を比較するしてディレクトリを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ディレ・GuaでDの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・抑止）です。照合ディレ・抑止に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・抑止・Guaです。比較ロール・抑止でA:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はRol・抑止・ディレです。運用抑止・RolでB:の監査証跡の保存 IE18は「Inspection Engineでエージェ」を述べるため、正答側の照合軸はディレ・ロール・抑止です。項目ディレ・抑止でC:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はGua・ロール・ディレです。用語ディレ・抑止という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・Guaです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0291**

    - 検証目的: ロールと権限のロールと権限 Role 0291について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor051
    Role auditor
    Account enabled yes
    確認コード GDP12DD0291A
    ```

    画面・出力には GDP12DD0291A が表示され、ロールと権限 Role 0291 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0291B
    ```

    画面・出力には GDP12DD0291B が表示され、ロールと権限 Role 0291 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 16
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0291C
    ```

    画面・出力には GDP12DD0291C が表示され、ロールと権限 Role 0291 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0291A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0291B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0291C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0306 {#c10-i0307}
*分類: アクセス管理*  ・  難易度: 中級

紫G解析0307ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票紫G解析0307です。紫G解析0307はロール権限管理の変更確認操作でロール権限管理の採取欄を棚卸する記録紫G解析0307です。紫G解析0307ではLDAP取込と取得時刻を採取票紫G解析0307へ残します。紫G解析0307ではLDAP取込対象の誤りを避けるため補助資料も照合する判断紫G解析0307です。紫G解析0307の用語整理ではロール権限管理の対象値を実在出力で説明する記録紫G解析0307です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0306の役割を調べています。audit process 実行結果照合 遅延表示の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は遅延表示の誤読を避けるため・遅延表示で遅延表示を確認するして遅延表示を照合する。
    - B. 表示や設定で扱う内容はディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてディレクトリを照合する。 ✅
    - C. 表示や設定で扱う内容はディスク逼迫中に検査データ流入をを避けるため・監視プロセスからApplianceを読むして監視プロセスを照合する。
    - D. 表示や設定で扱う内容はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するしてカーネル監視を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ディレ・ディレでBの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・解析）です。照合ディレ・解析に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・解析・ディレです。比較ロール・解析でA:の実行結果照合 遅延表示は「監査要件に沿ってレポート実行とレビューを束ね」を述べるため、正答側の照合軸はRol・解析・ディレです。項目ディレ・解析でC:の依存関係の確認 APP13は「Appliance Monitoriで監視プ」を述べるため、正答側の照合軸はディレ・ロール・ディレです。仕様ディレ・解析でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は解析・ディレ・ディレです。用語ディレ・解析という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・ディレです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0306**

    - 検証目的: ロールと権限のロールと権限 Role 0306について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor066
    Role auditor
    Account enabled yes
    確認コード GDP12DD0306A
    ```

    画面・出力には GDP12DD0306A が表示され、ロールと権限 Role 0306 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0306B
    ```

    画面・出力には GDP12DD0306B が表示され、ロールと権限 Role 0306 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 11
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0306C
    ```

    画面・出力には GDP12DD0306C が表示され、ロールと権限 Role 0306 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0306A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0306B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0306C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0321 {#c10-i0308}
*分類: アクセス管理*  ・  難易度: 中級

橙B計画0322ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票橙B計画0322です。橙B計画0322はロール権限管理の主操作でロール権限管理の出力欄を評価する記録橙B計画0322です。橙B計画0322ではLDAP取込と取得時刻を採取票橙B計画0322へ残します。橙B計画0322では過剰ロール付与を避けるため補助資料も照合する判断橙B計画0322です。橙B計画0322の用語整理ではロール権限管理の対象値を実在出力で追跡する記録橙B計画0322です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「ロールと権限 Role 0321」を「support gather_io_metrics 証跡採取 差分確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は差分確認の誤読を避けるため・差分確認で差分確認を確認するして差分確認を照合する。
    - B. 保守作業で参照する機能はInspectionを避けるため・ポリシー変更からPolicyを読むしてポリシー変更を照合する。
    - C. 保守作業で参照する機能は過剰ロール付与を避けるため・主操作で出力欄を評価するしてディレクトリを照合する。 ✅
    - D. 保守作業で参照する機能は対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするして照会文動詞集を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ディレ・過剰ロでCの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・計画）です。照合ディレ・計画に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し、過剰ロール付与を防ぐ」で、確認対象はディレ・計画・過剰ロです。比較ロール・計画でA:の証跡採取 差分確認は「I/O 指標を収集するサポートCLIコマンド」を述べるため、正答側の照合軸はRol・計画・ディレです。運用計画・RolでB:の停止前の確認 IE14は「Inspection Engineでポリシー」を述べるため、正答側の照合軸はディレ・ロール・計画です。仕様ディレ・計画でD:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は計画・過剰ロ・ディレです。用語ディレ・計画という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・過剰ロです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0321**

    - 検証目的: ロールと権限のロールと権限 Role 0321について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor081
    Role auditor
    Account enabled yes
    確認コード GDP12DD0321A
    ```

    画面・出力には GDP12DD0321A が表示され、ロールと権限 Role 0321 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0321B
    ```

    画面・出力には GDP12DD0321B が表示され、ロールと権限 Role 0321 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 6
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0321C
    ```

    画面・出力には GDP12DD0321C が表示され、ロールと権限 Role 0321 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0321A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0321B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0321C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0336 {#c10-i0309}
*分類: アクセス管理*  ・  難易度: 中級

青Q計画0337ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票青Q計画0337です。青Q計画0337はロール権限管理の照合操作でロール権限管理の確認欄を採取する記録青Q計画0337です。青Q計画0337ではLDAP取込と取得時刻を採取票青Q計画0337へ残します。青Q計画0337では監査担当者の閲覧範囲不足を避けるため補助資料も照合する判断青Q計画0337です。青Q計画0337の用語整理ではロール権限管理の対象値を実在出力で記録する記録青Q計画0337です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0336を同一分類のinspection engine 状態確認 履歴行と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は履歴行の誤読を避けるため・状態確認で履歴行を確認するして履歴行を照合する。
    - B. 管理対象との関係を表す説明はディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するして表示可能レポを照合する。
    - C. 管理対象との関係を表す説明は対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてユーザー活動を照合する。
    - D. 管理対象との関係を表す説明は監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するしてディレクトリを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ディレ・監査担でDの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・計画）です。照合ディレ・計画に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・計画・監査担です。比較ロール・計画でA:の状態確認 履歴行は「データベース通信を解析し監査レコードを作る処」を述べるため、正答側の照合軸はRol・計画・ディレです。運用計画・RolでB:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はディレ・ロール・計画です。項目ディレ・計画でC:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は監査担・ロール・ディレです。用語ディレ・計画という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・監査担です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0336**

    - 検証目的: ロールと権限のロールと権限 Role 0336について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor096
    Role auditor
    Account enabled yes
    確認コード GDP12DD0336A
    ```

    画面・出力には GDP12DD0336A が表示され、ロールと権限 Role 0336 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0336B
    ```

    画面・出力には GDP12DD0336B が表示され、ロールと権限 Role 0336 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 21
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0336C
    ```

    画面・出力には GDP12DD0336C が表示され、ロールと権限 Role 0336 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0336A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0336B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0336C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ロールと権限 Role 0351 {#c10-i0310}
*分類: アクセス管理*  ・  難易度: 上級

白L解除0352ではIBM Guardium Data Protection 12.x の アクセス管理を扱う採取票白L解除0352です。白L解除0352はロール権限管理の監査操作でロール権限管理の記録欄を比較する記録白L解除0352です。白L解除0352ではLDAP取込と取得時刻を採取票白L解除0352へ残します。白L解除0352ではGuardAPI実行権限不足を避けるため補助資料も照合する判断白L解除0352です。白L解除0352の用語整理ではロール権限管理の対象値を実在出力で確認する記録白L解除0352です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ロールと権限 Role 0351の設定や表示を読む前に役割を確認します。aggregator 障害時切り分け 接続認証ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはGuardAPI実行権限不足を避けるため・監査操作で記録欄を比較するしてディレクトリを照合する。 ✅
    - B. 対象資源に対する働きは接続認証の誤読を避けるため・監査プロセスで接続認証を確認するして接続認証を照合する。
    - C. 対象資源に対する働きはディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するして表示可能レポを照合する。
    - D. 対象資源に対する働きはディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてGuardAを照合する。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能ディレ・GuaでAの記述「Roleのディレクトリー取込と取得時刻を記録し」に対応する項目はロールと権限 Role（Rol・ディレ・解除）です。照合ディレ・解除に関するアクセス管理の仕様は「Roleのディレクトリー取込と取得時刻を記録し」で、確認対象はディレ・解除・Guaです。運用解除・RolでB:の障害時切り分け 接続認証は「複数 collector の監査情報を集約し」を述べるため、正答側の照合軸はディレ・ロール・解除です。項目ディレ・解除でC:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はGua・ロール・ディレです。仕様ディレ・解除でD:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は解除・Gua・ディレです。用語ディレ・解除という用語は「Roleのディレクトリー取込と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはロール・ディレ・Guaです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ロールと権限 Role 0351**

    - 検証目的: ロールと権限のロールと権限 Role 0351について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Role と LDAP取込
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    User Browser
    Login Name auditor111
    Role auditor
    Account enabled yes
    確認コード GDP12DD0351A
    ```

    画面・出力には GDP12DD0351A が表示され、ロールと権限 Role 0351 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> User Browser
    → Enter を押す
    ```

    画面・出力:
    ```text
    Role Permission Review
    Application Access Reports
    CLI role no
    Access Manager role yes
    確認コード GDP12DD0351B
    ```

    画面・出力には GDP12DD0351B が表示され、ロールと権限 Role 0351 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Role を読むため、ロールと権限 の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Role permission review
    → Enter を押す
    ```

    画面・出力:
    ```text
    LDAP import operation
    Imported user count 16
    Group mapping reviewed
    GuardAPI entitlement checked
    確認コード GDP12DD0351C
    ```

    画面・出力には GDP12DD0351C が表示され、ロールと権限 Role 0351 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0351A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0351B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0351C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring




## IBM Guardium Data Protection 12.x > アプライアンス健全性

### アプライアンス健全性 Appliance Monitoring ログとの照合 APP07 {#c10-i0311}
*分類: アプライアンス健全性*  ・  難易度: 上級

ログとの照合では アプライアンス健全性 の 監視プロセス を主操作として APP07 を判定します。時刻と対象識別子への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP07 に残します。ログとの照合を補助する DB処理一覧 では TURBINE を補助値として APP07 へ保存します。主判定のログとの照合ではアプライアンス健全性の 監視プロセス から Appliance を読み APP07 へ残します。証跡照合のログとの照合ではアプライアンス健全性の Appliance と TURBINE を APP07 に保存します。記録対応のログとの照合ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP07 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring ログとの照合 APP07の設定や表示を読む前に役割を確認します。S-TAP監視 KTAP Installed 0019ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは監視エージェントの監視エージェント状態と取得時刻を記録し・カーネル監視導入状態の誤読を防ぐである。採取操作で照合欄を点検するときはカーネル監視導入状態の誤読を防ぐ。S-TAP監視 KTAP Installed 0019固有の属性も確認対象に含める。
    - B. 状態を読み取るための働きは照会文 Verbのジョブキューと取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。
    - C. 状態を読み取るための働きは監視エージェントのカーネル監視有無と取得時刻を記録し・ローカル通信制御監視の未確認を防ぐである。保守操作で監査欄を保存するときはローカル通信制御監視の未確認を防ぐ。
    - D. 状態を読み取るための働きはAppliance Monitoriで監視プロセスから Appliance を読み・Appliance とである。監視プロセスからApplianceをときはディスク逼迫中に検査データ流を防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能監視プ・ディスでDの記述「Appliance Monitoriで監視プロセスから」に対応する項目はログとの照合 APP07（App・監視プ・ログと）です。照合監視プ・ログとに関するアプライアンス健全性の仕様は「Appliance Monitoriで監視プロセスから」で、確認対象は監視プ・ログと・ディスです。比較アプラ・ログとでA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はApp・ログと・監視プです。運用ログと・AppでB:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は監視プ・アプラ・ログとです。項目監視プ・ログとでC:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はディス・アプラ・監視プです。用語監視プ・ログとという用語は「Appliance Monitoriで監視プロセスか」を指し、照合する値と誤認リスクの組合せはアプラ・監視プ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring ログとの照合 APP07**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて操作とログを対応し、APP07のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP07の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP07のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP07のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP07 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Appliance が画面・出力に表示されること
    ② ステップ2 の TURBINE が画面・出力に表示されること
    ③ ステップ3 の Name が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 世代整合の確認 APP17 {#c10-i0312}
*分類: アプライアンス健全性*  ・  難易度: 上級

世代整合の確認では アプライアンス健全性 の DB処理一覧 を主操作として APP17 を判定します。定義と実行モジュールの版への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP17 に残します。世代整合の確認を補助する ジョブキュー では JobName を補助値として APP17 へ保存します。主判定の世代整合の確認ではアプライアンス健全性の DB処理一覧 から TURBINE を読み APP17 へ残します。証跡照合の世代整合の確認ではアプライアンス健全性の TURBINE と JobName を APP17 に保存します。記録対応の世代整合の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP17 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「アプライアンス健全性 Appliance Monitoring 世代整合の確認 APP17」を「監査レポート SQL Verb 0011」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するしてジョブキューを照合する。
    - B. 保守作業で参照する機能はディスク逼迫中に検査データ流入をを避けるため・DB処理一覧からTURBINEを読むしてデータベースを照合する。 ✅
    - C. 保守作業で参照する機能は過剰ロール付与を避けるため・主操作で出力欄を評価するして表示可能レポを照合する。
    - D. 保守作業で参照する機能は実行間隔より短いFROM/TO範を避けるため・プロセス一覧からScheduleを読むしてプロセス一覧を照合する。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能データ・ディスでBの記述「Appliance Monitoriでデータベース処理一」に対応する項目は世代整合の確認 APP17（App・データ・世代整）です。照合データ・世代整に関するアプライアンス健全性の仕様は「Appliance Monitoriでデータベース処理一覧から」で、確認対象はデータ・世代整・ディスです。比較アプラ・世代整でA:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はApp・世代整・データです。項目データ・世代整でC:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はディス・アプラ・データです。仕様データ・世代整でD:の代替経路の確認 AUDIT10は「Audit Processでプロセス一覧から」を述べるため、正答側の照合軸は世代整・ディス・データです。用語データ・世代整という用語は「Appliance Monitoriでデータベース処」を指し、照合する値と誤認リスクの組合せはアプラ・データ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 世代整合の確認 APP17**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて世代差を検出し、APP17のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP17と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP17のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP17のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP17 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP17の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の TURBINE が画面・出力に表示されること
    ② ステップ2 の Name が画面・出力に表示されること
    ③ ステップ3 の Appliance が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 代替経路の確認 APP10 {#c10-i0313}
*分類: アプライアンス健全性*  ・  難易度: 上級

代替経路の確認では アプライアンス健全性 の 監視プロセス を主操作として APP10 を判定します。主経路との役割差への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP10 に残します。代替経路の確認を補助する DB処理一覧 では TURBINE を補助値として APP10 へ保存します。主判定の代替経路の確認ではアプライアンス健全性の 監視プロセス から Appliance を読み APP10 へ残します。証跡照合の代替経路の確認ではアプライアンス健全性の Appliance と TURBINE を APP10 に保存します。記録対応の代替経路の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP10 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 代替経路の確認 APP10の役割を調べています。監査レポート Server IP 0017の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはディスク逼迫中に検査データ流入をを避けるため・監視プロセスからApplianceを読むして監視プロセスを照合する。 ✅
    - B. 機能の説明としては監査タスク未レビューを避けるため・復旧操作で点検欄を確認するしてデータソースを照合する。
    - C. 機能の説明としては最終応答停止の見落としを避けるため・確認操作で状態欄を整理するして監視エージェを照合する。S-TAP監視 KTAP Installed 0214固有の属性も確認対象に含める。
    - D. 機能の説明としては活動ログの誤読を避けるため・証跡採取で活動ログを確認するして活動ログを照合する。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能監視プ・ディスでAの記述「Appliance Monitoriで監視プロセスから」に対応する項目は代替経路の確認 APP10（App・監視プ・代替経）です。照合監視プ・代替経に関するアプライアンス健全性の仕様は「Appliance Monitoriで監視プロセスから」で、確認対象は監視プ・代替経・ディスです。運用代替経・AppでB:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は監視プ・アプラ・代替経です。項目監視プ・代替経でC:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はディス・アプラ・監視プです。仕様監視プ・代替経でD:の証跡採取 活動ログは「管理対象システムの構成と配布を統制する管理点」を述べるため、正答側の照合軸は代替経・ディス・監視プです。用語監視プ・代替経という用語は「Appliance Monitoriで監視プロセスか」を指し、照合する値と誤認リスクの組合せはアプラ・監視プ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 代替経路の確認 APP10**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて代替手段の成立を確認し、APP10のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP10の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP10のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP10のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP10 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Appliance が画面・出力に表示されること
    ② ステップ2 の TURBINE が画面・出力に表示されること
    ③ ステップ3 の Name が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 依存関係の確認 APP13 {#c10-i0314}
*分類: アプライアンス健全性*  ・  難易度: 上級

依存関係の確認では アプライアンス健全性 の 監視プロセス を主操作として APP13 を判定します。前提資源と後続処理の順序への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP13 に残します。依存関係の確認を補助する DB処理一覧 では TURBINE を補助値として APP13 へ保存します。主判定の依存関係の確認ではアプライアンス健全性の 監視プロセス から Appliance を読み APP13 へ残します。証跡照合の依存関係の確認ではアプライアンス健全性の Appliance と TURBINE を APP13 に保存します。記録対応の依存関係の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP13 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 依存関係の確認 APP13を保守記録に説明する必要があります。S-TAP監視 S-TAP Host 0076と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するして最終応答を照合する。S-TAP監視 S-TAP Host 0076固有の属性も確認対象に含める。
    - B. 運用時に利用する技術的役割はディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてGuardAを照合する。
    - C. 運用時に利用する技術的役割は一覧画面の誤読を避けるため・レポートで一覧画面を確認するして一覧画面を照合する。
    - D. 運用時に利用する技術的役割はディスク逼迫中に検査データ流入をを避けるため・監視プロセスからApplianceを読むして監視プロセスを照合する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能監視プ・ディスでDの記述「Appliance Monitoriで監視プロセスから」に対応する項目は依存関係の確認 APP13（App・監視プ・依存関）です。照合監視プ・依存関に関するアプライアンス健全性の仕様は「Appliance Monitoriで監視プロセスから」で、確認対象は監視プ・依存関・ディスです。比較アプラ・依存関でA:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はApp・依存関・監視プです。運用依存関・AppでB:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は監視プ・アプラ・依存関です。項目監視プ・依存関でC:の対象絞り込み 一覧画面は「I/O 指標を収集するサポートCLIコマンド」を述べるため、正答側の照合軸はディス・アプラ・監視プです。用語監視プ・依存関という用語は「Appliance Monitoriで監視プロセスか」を指し、照合する値と誤認リスクの組合せはアプラ・監視プ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 依存関係の確認 APP13**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて依存資源を点検し、APP13のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP13の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP13のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP13のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP13 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Appliance が画面・出力に表示されること
    ② ステップ2 の TURBINE が画面・出力に表示されること
    ③ ステップ3 の Name が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 保守後の確認 APP20 {#c10-i0315}
*分類: アプライアンス健全性*  ・  難易度: 上級

保守後の確認では アプライアンス健全性 の DB処理一覧 を主操作として APP20 を判定します。有効化された定義と版数への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP20 に残します。保守後の確認を補助する ジョブキュー では JobName を補助値として APP20 へ保存します。主判定の保守後の確認ではアプライアンス健全性の DB処理一覧 から TURBINE を読み APP20 へ残します。証跡照合の保守後の確認ではアプライアンス健全性の TURBINE と JobName を APP20 に保存します。記録対応の保守後の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP20 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 保守後の確認 APP20の技術的な意味を資料で確認するとき、監査レポート Server IP 0092との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はAppliance Monitoriでデータベース処理一覧から TURBINE を読み・TURBINE とである。DB処理一覧からTURBINEを読むときはディスク逼迫中に検査データ流を防ぐ。 ✅
    - B. 管理対象との関係を表す説明はServer IPのデータソースと取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。
    - C. 管理対象との関係を表す説明はRoleのディレクトリー取込と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。ロールと権限 Role 0201固有の属性も確認対象に含める。
    - D. 管理対象との関係を表す説明は監視対象データベースやサービスを表す Guardium の登録単位を承認履歴確認する。承認履歴確認で復元前提を確認するときは復元前提の誤読を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能データ・ディスでAの記述「Appliance Monitoriでデータベース処理一」に対応する項目は保守後の確認 APP20（App・データ・保守確）です。照合データ・保守確に関するアプライアンス健全性の仕様は「Appliance Monitoriでデータベース処理一覧から」で、確認対象はデータ・保守確・ディスです。運用保守確・AppでB:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸はデータ・アプラ・保守確です。項目データ・保守確でC:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸はディス・アプラ・データです。仕様データ・保守確でD:の承認履歴確認 復元前提は「監視対象データベースやサービスを表す」を述べるため、正答側の照合軸は保守確・ディス・データです。用語データ・保守確という用語は「Appliance Monitoriでデータベース処」を指し、照合する値と誤認リスクの組合せはアプラ・データ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 保守後の確認 APP20**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて保守反映を検証し、APP20のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP20と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP20のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP20の対応を確認します。有効化された定義と版数を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP20のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP20 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP20の対応を確認します。有効化された定義と版数を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP20の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP20の対応を確認します。有効化された定義と版数を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の TURBINE が画面・出力に表示されること
    ② ステップ2 の Name が画面・出力に表示されること
    ③ ステップ3 の Appliance が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 停止前の確認 APP14 {#c10-i0316}
*分類: アプライアンス健全性*  ・  難易度: 上級

停止前の確認では アプライアンス健全性 の DB処理一覧 を主操作として APP14 を判定します。処理中資源と未完了要求への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP14 に残します。停止前の確認を補助する ジョブキュー では JobName を補助値として APP14 へ保存します。主判定の停止前の確認ではアプライアンス健全性の DB処理一覧 から TURBINE を読み APP14 へ残します。証跡照合の停止前の確認ではアプライアンス健全性の TURBINE と JobName を APP14 に保存します。記録対応の停止前の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP14 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 停止前の確認 APP14に関する障害切り分けの前提を確認しています。監査レポート SQL Verb 0086の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は変更でジョブキューを証跡に残し・照会文 Verbのジョブキューと取得時刻を記録し。監査レポート SQL Verb 0086固有の属性も確認対象に含める。
    - B. 表示や設定で扱う内容は停止確認でデータベースを証跡に残し・Appliance Monitoriでデータベース処理一覧か。 ✅
    - C. 表示や設定で扱う内容は切替で暗号化表示を証跡に残し・監視エージェントの暗号化表示と取得時刻を記録し。
    - D. 表示や設定で扱う内容は証跡採取で取得間隔を証跡に残し・複数 collector の監査情報を集約しレポートへ渡す装。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能データ・ディスでBの記述「Appliance Monitoriでデータベース処理一」に対応する項目は停止前の確認 APP14（App・データ・停止確）です。照合データ・停止確に関するアプライアンス健全性の仕様は「Appliance Monitoriでデータベース処理一覧から」で、確認対象はデータ・停止確・ディスです。比較アプラ・停止確でA:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はApp・停止確・データです。項目データ・停止確でC:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はディス・アプラ・データです。仕様データ・停止確でD:の証跡採取 取得間隔は「複数 collector の監査情報を集約し」を述べるため、正答側の照合軸は停止確・ディス・データです。用語データ・停止確という用語は「Appliance Monitoriでデータベース処」を指し、照合する値と誤認リスクの組合せはアプラ・データ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 停止前の確認 APP14**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて安全な停止条件を確認し、APP14のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP14のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP14のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP14 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP14の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の TURBINE が画面・出力に表示されること
    ② ステップ2 の Name が画面・出力に表示されること
    ③ ステップ3 の Appliance が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 再始動後の確認 APP15 {#c10-i0317}
*分類: アプライアンス健全性*  ・  難易度: 上級

再始動後の確認では アプライアンス健全性 の ジョブキュー を主操作として APP15 を判定します。再開点と未処理データへの注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP15 に残します。再始動後の確認を補助する 監視プロセス では Appliance を補助値として APP15 へ保存します。主判定の再始動後の確認ではアプライアンス健全性の ジョブキュー から JobName を読み APP15 へ残します。証跡照合の再始動後の確認ではアプライアンス健全性の JobName と Appliance を APP15 に保存します。記録対応の再始動後の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP15 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 再始動後の確認 APP15の設定や表示を読む前に役割を確認します。S-TAP監視 S-TAP Version 0058ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は最終応答停止の見落としを避けるため・確認操作で状態欄を整理するして暗号化表示を照合する。
    - B. 一次資料が示す主目的はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして監視エージェを照合する。
    - C. 一次資料が示す主目的は保存場所の誤読を避けるため・実行結果照合で保存場所を確認するして保存場所を照合する。Central Manager 実行結果照合 保存場所固有の属性も確認対象に含める。
    - D. 一次資料が示す主目的はディスク逼迫中に検査データ流入をを避けるため・ジョブキューからJobNameを読むしてジョブキューを照合する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能ジョブ・ディスでDの記述「Appliance Monitoriでジョブキューから」に対応する項目は再始動後の確認 APP15（App・ジョブ・再始動）です。照合ジョブ・再始動に関するアプライアンス健全性の仕様は「Appliance Monitoriでジョブキューから」で、確認対象はジョブ・再始動・ディスです。比較アプラ・再始動でA:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はApp・再始動・ジョブです。運用再始動・AppでB:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はジョブ・アプラ・再始動です。項目ジョブ・再始動でC:の実行結果照合 保存場所は「管理対象システムの構成と配布を統制する管理点」を述べるため、正答側の照合軸はディス・アプラ・ジョブです。用語ジョブ・再始動という用語は「Appliance Monitoriでジョブキューか」を指し、照合する値と誤認リスクの組合せはアプラ・ジョブ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 再始動後の確認 APP15**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて再始動結果を検証し、APP15のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP15のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP15 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP15の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP15のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Name が画面・出力に表示されること
    ② ステップ2 の Appliance が画面・出力に表示されること
    ③ ステップ3 の TURBINE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 変更前の確認 APP02 {#c10-i0318}
*分類: アプライアンス健全性*  ・  難易度: 上級

変更前の確認では アプライアンス健全性 の DB処理一覧 を主操作として APP02 を判定します。変更対象と非対象の境界への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP02 に残します。変更前の確認を補助する ジョブキュー では JobName を補助値として APP02 へ保存します。主判定の変更前の確認ではアプライアンス健全性の DB処理一覧 から TURBINE を読み APP02 へ残します。証跡照合の変更前の確認ではアプライアンス健全性の TURBINE と JobName を APP02 に保存します。記録対応の変更前の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP02 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 変更前の確認 APP02の役割を調べています。アプライアンス健全性 Appliance Monitoring 再始動後の確認の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はジョブキューからJobNameを読むことでジョブキューを確認し・ディスク逼迫中に検査データ流を防ぐ。
    - B. 表示や設定で扱う内容は保守操作で監査欄を保存することでカーネル監視を確認し・ローカル通信制御監視の未確認を防ぐ。
    - C. 表示や設定で扱う内容はDB処理一覧からTURBINEを読むことでデータベースを確認し・ディスク逼迫中に検査データ流を防ぐ。 ✅
    - D. 表示や設定で扱う内容はプロセス一覧からScheduleを読むことでプロセス一覧を確認し・実行間隔より短いFROM/Tを防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能データ・ディスでCの記述「Appliance Monitoriでデータベース処理一」に対応する項目は変更前の確認 APP02（App・データ・変更確）です。照合データ・変更確に関するアプライアンス健全性の仕様は「Appliance Monitoriでデータベース処理一覧から」で、確認対象はデータ・変更確・ディスです。比較アプラ・変更確でA:の再始動後の確認 APP15は「Appliance Monitoriでジョブ」を述べるため、正答側の照合軸はApp・変更確・データです。運用変更確・AppでB:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はデータ・アプラ・変更確です。仕様データ・変更確でD:の障害切り分け AUDIT04は「Audit Processでプロセス一覧から」を述べるため、正答側の照合軸は変更確・ディス・データです。用語データ・変更確という用語は「Appliance Monitoriでデータベース処」を指し、照合する値と誤認リスクの組合せはアプラ・データ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 変更前の確認 APP02**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて変更前の証跡を保存し、APP02のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP02のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP02のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP02 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP02の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の TURBINE が画面・出力に表示されること
    ② ステップ2 の Name が画面・出力に表示されること
    ③ ステップ3 の Appliance が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 変更後の確認 APP03 {#c10-i0319}
*分類: アプライアンス健全性*  ・  難易度: 上級

変更後の確認では アプライアンス健全性 の ジョブキュー を主操作として APP03 を判定します。反映値と残存値への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP03 に残します。変更後の確認を補助する 監視プロセス では Appliance を補助値として APP03 へ保存します。主判定の変更後の確認ではアプライアンス健全性の ジョブキュー から JobName を読み APP03 へ残します。証跡照合の変更後の確認ではアプライアンス健全性の JobName と Appliance を APP03 に保存します。記録対応の変更後の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP03 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 変更後の確認 APP03について構成や状態を確認します。アプライアンス健全性 Appliance Monitoring 代替経路の確認ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は変更確認でジョブキューを証跡に残し・Appliance Monitoriでジョブキューから。 ✅
    - B. 一次資料が示す主目的は代替経路確認で監視プロセスを証跡に残し・Appliance Monitoriで監視プロセスから。
    - C. 一次資料が示す主目的は登録でGuardAを証跡に残し・ディレクトリー UserのGuardAPI権限と取得時刻を記。
    - D. 一次資料が示す主目的は再始動確認で報告上限を証跡に残し・Audit Processで報告上限から。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能ジョブ・ディスでAの記述「Appliance Monitoriでジョブキューから」に対応する項目は変更後の確認 APP03（App・ジョブ・変更確）です。照合ジョブ・変更確に関するアプライアンス健全性の仕様は「Appliance Monitoriでジョブキューから」で、確認対象はジョブ・変更確・ディスです。運用変更確・AppでB:の代替経路の確認 APP10は「Appliance Monitoriで監視プ」を述べるため、正答側の照合軸はジョブ・アプラ・変更確です。項目ジョブ・変更確でC:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸はディス・アプラ・ジョブです。仕様ジョブ・変更確でD:の再始動後の確認 AUDIT15は「Audit Processで報告上限から」を述べるため、正答側の照合軸は変更確・ディス・ジョブです。用語ジョブ・変更確という用語は「Appliance Monitoriでジョブキューか」を指し、照合する値と誤認リスクの組合せはアプラ・ジョブ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 変更後の確認 APP03**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて変更結果を検証し、APP03のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP03のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP03 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP03の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP03のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Name が画面・出力に表示されること
    ② ステップ2 の Appliance が画面・出力に表示されること
    ③ ステップ3 の TURBINE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 容量余力の確認 APP16 {#c10-i0320}
*分類: アプライアンス健全性*  ・  難易度: 上級

容量余力の確認では アプライアンス健全性 の 監視プロセス を主操作として APP16 を判定します。使用量と警告しきい値への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP16 に残します。容量余力の確認を補助する DB処理一覧 では TURBINE を補助値として APP16 へ保存します。主判定の容量余力の確認ではアプライアンス健全性の 監視プロセス から Appliance を読み APP16 へ残します。証跡照合の容量余力の確認ではアプライアンス健全性の Appliance と TURBINE を APP16 に保存します。記録対応の容量余力の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP16 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 容量余力の確認 APP16を同一分類の監査レポート DB User Name 0074と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は点検操作で判定欄を記録することで照会文動詞集を確認し・照会文動詞集計の期間誤りを防ぐ。
    - B. 構成を確認する際の意味は保守操作で監査欄を保存することで暗号化表示を確認し・ローカル通信制御監視の未確認を防ぐ。
    - C. 構成を確認する際の意味は監視プロセスからApplianceを読むことで監視プロセスを確認し・ディスク逼迫中に検査データ流を防ぐ。 ✅
    - D. 構成を確認する際の意味はレポートでイベント識別を確認することでイベント識別を確認し・イベント識別の誤読を防ぐ。Approved TAP Clients 対象絞り込み イベント識別固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能監視プ・ディスでCの記述「Appliance Monitoriで監視プロセスから」に対応する項目は容量余力の確認 APP16（App・監視プ・容量余）です。照合監視プ・容量余に関するアプライアンス健全性の仕様は「Appliance Monitoriで監視プロセスから」で、確認対象は監視プ・容量余・ディスです。比較アプラ・容量余でA:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸はApp・容量余・監視プです。運用容量余・AppでB:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は監視プ・アプラ・容量余です。仕様監視プ・容量余でD:の対象絞り込み イベント識別は「接続を許可された S-TAP」を述べるため、正答側の照合軸は容量余・ディス・監視プです。用語監視プ・容量余という用語は「Appliance Monitoriで監視プロセスか」を指し、照合する値と誤認リスクの組合せはアプラ・監視プ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 容量余力の確認 APP16**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて容量枯渇を予防し、APP16のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP16と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP16の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP16の対応を確認します。使用量と警告しきい値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP16のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP16の対応を確認します。使用量と警告しきい値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP16のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP16 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP16の対応を確認します。使用量と警告しきい値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Appliance が画面・出力に表示されること
    ② ステップ2 の TURBINE が画面・出力に表示されること
    ③ ステップ3 の Name が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 引継ぎ記録 APP09 {#c10-i0321}
*分類: アプライアンス健全性*  ・  難易度: 上級

引継ぎ記録では アプライアンス健全性 の ジョブキュー を主操作として APP09 を判定します。次担当者が追跡できる証跡への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP09 に残します。引継ぎ記録を補助する 監視プロセス では Appliance を補助値として APP09 へ保存します。主判定の引継ぎ記録ではアプライアンス健全性の ジョブキュー から JobName を読み APP09 へ残します。証跡照合の引継ぎ記録ではアプライアンス健全性の JobName と Appliance を APP09 に保存します。記録対応の引継ぎ記録ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP09 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「アプライアンス健全性 Appliance Monitoring 引継ぎ記録 APP09」を「アプライアンス健全性 Appliance Monitoring 停止前の確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は停止確認でデータベースを証跡に残し・Appliance Monitoriでデータベース処理一覧か。
    - B. 仕様上の役割は照合で承認クライアを証跡に残し・監視エージェントの承認クライアントと取得時刻を記録し。
    - C. 仕様上の役割はアプライアンでジョブキューを証跡に残し・Appliance Monitoriでジョブキューから。 ✅
    - D. 仕様上の役割は承認履歴確認で初期同期を証跡に残し・接続を許可された S-TAP と状態を確認する管理レポートを。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能ジョブ・ディスでCの記述「Appliance Monitoriでジョブキューから」に対応する項目は引継ぎ記録 APP09（App・ジョブ・アプラ）です。照合ジョブ・アプラに関するアプライアンス健全性の仕様は「Appliance Monitoriでジョブキューから」で、確認対象はジョブ・アプラ・ディスです。比較アプラ・アプラでA:の停止前の確認 APP14は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸はApp・アプラ・ジョブです。運用アプラ・AppでB:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はジョブ・アプラ・アプラです。仕様ジョブ・アプラでD:の承認履歴確認 初期同期は「接続を許可された S-TAP」を述べるため、正答側の照合軸はアプラ・ディス・ジョブです。用語ジョブ・アプラという用語は「Appliance Monitoriでジョブキューか」を指し、照合する値と誤認リスクの組合せはアプラ・ジョブ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 引継ぎ記録 APP09**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて再現可能な記録を作成し、APP09のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP09のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP09 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP09の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP09のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Name が画面・出力に表示されること
    ② ステップ2 の Appliance が画面・出力に表示されること
    ③ ステップ3 の TURBINE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 復旧後の確認 APP06 {#c10-i0322}
*分類: アプライアンス健全性*  ・  難易度: 上級

復旧後の確認では アプライアンス健全性 の ジョブキュー を主操作として APP06 を判定します。再発していないことを示す値への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP06 に残します。復旧後の確認を補助する 監視プロセス では Appliance を補助値として APP06 へ保存します。主判定の復旧後の確認ではアプライアンス健全性の ジョブキュー から JobName を読み APP06 へ残します。証跡照合の復旧後の確認ではアプライアンス健全性の JobName と Appliance を APP06 に保存します。記録対応の復旧後の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP06 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 復旧後の確認 APP06に関する障害切り分けの前提を確認しています。ロールと権限 Permission 0063の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はGuardAPI実行権限不足を避けるため・監査操作で記録欄を比較するして表示可能レポを照合する。
    - B. 障害切り分けに用いる役割はディスク逼迫中に検査データ流入をを避けるため・ジョブキューからJobNameを読むしてジョブキューを照合する。 ✅
    - C. 障害切り分けに用いる役割はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして承認クライアを照合する。
    - D. 障害切り分けに用いる役割は実行間隔より短いFROM/TO範を避けるため・作業一覧からStatusを読むして作業一覧を照合する。監査プロセス Audit Process Builder 変更前の確認固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能ジョブ・ディスでBの記述「Appliance Monitoriでジョブキューから」に対応する項目は復旧後の確認 APP06（App・ジョブ・復旧確）です。照合ジョブ・復旧確に関するアプライアンス健全性の仕様は「Appliance Monitoriでジョブキューから」で、確認対象はジョブ・復旧確・ディスです。比較アプラ・復旧確でA:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はApp・復旧確・ジョブです。項目ジョブ・復旧確でC:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はディス・アプラ・ジョブです。仕様ジョブ・復旧確でD:の変更前の確認 AUDIT02は「Audit Processで作業一覧から」を述べるため、正答側の照合軸は復旧確・ディス・ジョブです。用語ジョブ・復旧確という用語は「Appliance Monitoriでジョブキューか」を指し、照合する値と誤認リスクの組合せはアプラ・ジョブ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 復旧後の確認 APP06**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて復旧後の安定性を確認し、APP06のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP06のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP06 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP06の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP06のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Name が画面・出力に表示されること
    ② ステップ2 の Appliance が画面・出力に表示されること
    ③ ステップ3 の TURBINE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 復旧準備 APP05 {#c10-i0323}
*分類: アプライアンス健全性*  ・  難易度: 上級

復旧準備では アプライアンス健全性 の DB処理一覧 を主操作として APP05 を判定します。再開前に必要な整合性への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP05 に残します。復旧準備を補助する ジョブキュー では JobName を補助値として APP05 へ保存します。主判定の復旧準備ではアプライアンス健全性の DB処理一覧 から TURBINE を読み APP05 へ残します。証跡照合の復旧準備ではアプライアンス健全性の TURBINE と JobName を APP05 に保存します。記録対応の復旧準備ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP05 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 復旧準備 APP05を保守記録に説明する必要があります。ロールと権限 Role 0081と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は主操作で出力欄を評価することでディレクトリを確認し・過剰ロール付与を防ぐ。
    - B. 保守作業で参照する機能は採取操作で照合欄を点検することで承認クライアを確認し・カーネル監視導入状態の誤読を防ぐ。S-TAP監視 DB Server Type 0235固有の属性も確認対象に含める。
    - C. 保守作業で参照する機能はDB処理一覧からTURBINEを読むことでデータベースを確認し・ディスク逼迫中に検査データ流を防ぐ。 ✅
    - D. 保守作業で参照する機能は復旧操作で点検欄を確認することでユーザー活動を確認し・監査タスク未レビューを防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能データ・ディスでCの記述「Appliance Monitoriでデータベース処理一」に対応する項目は復旧準備 APP05（App・データ・復旧準）です。照合データ・復旧準に関するアプライアンス健全性の仕様は「Appliance Monitoriでデータベース処理一覧から」で、確認対象はデータ・復旧準・ディスです。比較アプラ・復旧準でA:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸はApp・復旧準・データです。運用復旧準・AppでB:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はデータ・アプラ・復旧準です。仕様データ・復旧準でD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は復旧準・ディス・データです。用語データ・復旧準という用語は「Appliance Monitoriでデータベース処」を指し、照合する値と誤認リスクの組合せはアプラ・データ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 復旧準備 APP05**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて復旧条件を確認し、APP05のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP05のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP05のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP05 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP05の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の TURBINE が画面・出力に表示されること
    ② ステップ2 の Name が画面・出力に表示されること
    ③ ステップ3 の Appliance が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 性能影響の確認 APP11 {#c10-i0324}
*分類: アプライアンス健全性*  ・  難易度: 上級

性能影響の確認では アプライアンス健全性 の DB処理一覧 を主操作として APP11 を判定します。処理時間と滞留箇所への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP11 に残します。性能影響の確認を補助する ジョブキュー では JobName を補助値として APP11 へ保存します。主判定の性能影響の確認ではアプライアンス健全性の DB処理一覧 から TURBINE を読み APP11 へ残します。証跡照合の性能影響の確認ではアプライアンス健全性の TURBINE と JobName を APP11 に保存します。記録対応の性能影響の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP11 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 性能影響の確認 APP11について構成や状態を確認します。S-TAP監視 DB Server Type 0025ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは棚卸で承認クライアを証跡に残し・監視エージェントの承認クライアントと取得時刻を記録し。
    - B. 対象資源に対する働きは照合でロール割当を証跡に残し・Login Nameのロール割当と取得時刻を記録し。
    - C. 対象資源に対する働きは性能影響確認で作業一覧を証跡に残し・Audit Processで作業一覧から Status。監査プロセス Audit Process Builder固有の属性も確認対象に含める。
    - D. 対象資源に対する働きは性能影響確認でデータベースを証跡に残し・Appliance Monitoriでデータベース処理一覧か。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能データ・ディスでDの記述「Appliance Monitoriでデータベース処理一」に対応する項目は性能影響の確認 APP11（App・データ・性能影）です。照合データ・性能影に関するアプライアンス健全性の仕様は「Appliance Monitoriでデータベース処理一覧から」で、確認対象はデータ・性能影・ディスです。比較アプラ・性能影でA:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はApp・性能影・データです。運用性能影・AppでB:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸はデータ・アプラ・性能影です。項目データ・性能影でC:の性能影響の確認 AUDIT11は「Audit Processで作業一覧から」を述べるため、正答側の照合軸はディス・アプラ・データです。用語データ・性能影という用語は「Appliance Monitoriでデータベース処」を指し、照合する値と誤認リスクの組合せはアプラ・データ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 性能影響の確認 APP11**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて負荷と待ちを確認し、APP11のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP11のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP11のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP11 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP11の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の TURBINE が画面・出力に表示されること
    ② ステップ2 の Name が画面・出力に表示されること
    ③ ステップ3 の Appliance が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 構成監査 APP08 {#c10-i0325}
*分類: アプライアンス健全性*  ・  難易度: 上級

構成監査では アプライアンス健全性 の DB処理一覧 を主操作として APP08 を判定します。定義値と稼働値の一致への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP08 に残します。構成監査を補助する ジョブキュー では JobName を補助値として APP08 へ保存します。主判定の構成監査ではアプライアンス健全性の DB処理一覧 から TURBINE を読み APP08 へ残します。証跡照合の構成監査ではアプライアンス健全性の TURBINE と JobName を APP08 に保存します。記録対応の構成監査ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP08 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 構成監査 APP08を同一分類の監査レポート Client IP 0005と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するして監査タスクを照合する。
    - B. 管理対象との関係を表す説明はディスク逼迫中に検査データ流入をを避けるため・DB処理一覧からTURBINEを読むしてデータベースを照合する。 ✅
    - C. 管理対象との関係を表す説明はディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてユーザー有効を照合する。
    - D. 管理対象との関係を表す説明は宛先定義の誤読を避けるため・状態確認で宛先定義を確認するして宛先定義を照合する。Approved TAP Clients 状態確認 宛先定義固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能データ・ディスでBの記述「Appliance Monitoriでデータベース処理一」に対応する項目は構成監査 APP08（App・データ・構成監）です。照合データ・構成監に関するアプライアンス健全性の仕様は「Appliance Monitoriでデータベース処理一覧から」で、確認対象はデータ・構成監・ディスです。比較アプラ・構成監でA:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸はApp・構成監・データです。項目データ・構成監でC:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はディス・アプラ・データです。仕様データ・構成監でD:の状態確認 宛先定義は「接続を許可された S-TAP」を述べるため、正答側の照合軸は構成監・ディス・データです。用語データ・構成監という用語は「Appliance Monitoriでデータベース処」を指し、照合する値と誤認リスクの組合せはアプラ・データ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 構成監査 APP08**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて構成差分を監査し、APP08のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP08のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP08のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP08 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP08の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の TURBINE が画面・出力に表示されること
    ② ステップ2 の Name が画面・出力に表示されること
    ③ ステップ3 の Appliance が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 権限境界の確認 APP12 {#c10-i0326}
*分類: アプライアンス健全性*  ・  難易度: 上級

権限境界の確認では アプライアンス健全性 の ジョブキュー を主操作として APP12 を判定します。参照操作と変更操作の分離への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP12 に残します。権限境界の確認を補助する 監視プロセス では Appliance を補助値として APP12 へ保存します。主判定の権限境界の確認ではアプライアンス健全性の ジョブキュー から JobName を読み APP12 へ残します。証跡照合の権限境界の確認ではアプライアンス健全性の JobName と Appliance を APP12 に保存します。記録対応の権限境界の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP12 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 権限境界の確認 APP12の技術的な意味を資料で確認するとき、ロールと権限 LDAP User 0042との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はジョブキューからJobNameを読むことでジョブキューを確認し・ディスク逼迫中に検査データ流を防ぐ。 ✅
    - B. コマンドまたは機能の用途は変更確認操作で採取欄を棚卸することでGuardAを確認し・ディレクトリー取込対象の誤りを防ぐ。ロールと権限 LDAP User 0042固有の属性も確認対象に含める。
    - C. コマンドまたは機能の用途は主操作で出力欄を評価することでユーザー有効を確認し・過剰ロール付与を防ぐ。
    - D. コマンドまたは機能の用途はS-TAPで回収対象を確認することで回収対象を確認し・回収対象の誤読を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能ジョブ・ディスでAの記述「Appliance Monitoriでジョブキューから」に対応する項目は権限境界の確認 APP12（App・ジョブ・権限境）です。照合ジョブ・権限境に関するアプライアンス健全性の仕様は「Appliance Monitoriでジョブキューから」で、確認対象はジョブ・権限境・ディスです。運用権限境・AppでB:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸はジョブ・アプラ・権限境です。項目ジョブ・権限境でC:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はディス・アプラ・ジョブです。仕様ジョブ・権限境でD:の障害時切り分け 回収対象は「S-TAP や外部接続から監査データを受け取」を述べるため、正答側の照合軸は権限境・ディス・ジョブです。用語ジョブ・権限境という用語は「Appliance Monitoriでジョブキューか」を指し、照合する値と誤認リスクの組合せはアプラ・ジョブ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 権限境界の確認 APP12**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて実行権限を点検し、APP12のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP12のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP12 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP12の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP12のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Name が画面・出力に表示されること
    ② ステップ2 の Appliance が画面・出力に表示されること
    ③ ステップ3 の TURBINE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 異常終了後の確認 APP19 {#c10-i0327}
*分類: アプライアンス健全性*  ・  難易度: 上級

異常終了後の確認では アプライアンス健全性 の 監視プロセス を主操作として APP19 を判定します。未完了処理と再実行条件への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP19 に残します。異常終了後の確認を補助する DB処理一覧 では TURBINE を補助値として APP19 へ保存します。主判定の異常終了後の確認ではアプライアンス健全性の 監視プロセス から Appliance を読み APP19 へ残します。証跡照合の異常終了後の確認ではアプライアンス健全性の Appliance と TURBINE を APP19 に保存します。記録対応の異常終了後の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP19 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 異常終了後の確認 APP19について構成や状態を確認します。監査レポート DB User Name 0029ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは監視プロセスからApplianceを読むことで監視プロセスを確認し・ディスク逼迫中に検査データ流を防ぐ。 ✅
    - B. 状態を読み取るための働きは復旧操作で点検欄を確認することで照会文動詞集を確認し・監査タスク未レビューを防ぐ。
    - C. 状態を読み取るための働きは監査操作で記録欄を比較することでユーザー有効を確認し・GuardAPI実行権限不足を防ぐ。ロールと権限 Application Access 0255固有の属性も確認対象に含める。
    - D. 状態を読み取るための働きは状態確認で開始時刻を確認することで開始時刻を確認し・開始時刻の誤読を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能監視プ・ディスでAの記述「Appliance Monitoriで監視プロセスから」に対応する項目は異常終了後の確認 APP19（App・監視プ・異常終）です。照合監視プ・異常終に関するアプライアンス健全性の仕様は「Appliance Monitoriで監視プロセスから」で、確認対象は監視プ・異常終・ディスです。運用異常終・AppでB:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は監視プ・アプラ・異常終です。項目監視プ・異常終でC:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はディス・アプラ・監視プです。仕様監視プ・異常終でD:の状態確認 開始時刻は「監査要件に沿ってレポート実行とレビューを束ね」を述べるため、正答側の照合軸は異常終・ディス・監視プです。用語監視プ・異常終という用語は「Appliance Monitoriで監視プロセスか」を指し、照合する値と誤認リスクの組合せはアプラ・監視プ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 異常終了後の確認 APP19**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて異常終了の影響を限定し、APP19のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP19と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP19の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP19の対応を確認します。未完了処理と再実行条件を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP19のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP19の対応を確認します。未完了処理と再実行条件を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP19のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP19 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP19の対応を確認します。未完了処理と再実行条件を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Appliance が画面・出力に表示されること
    ② ステップ2 の TURBINE が画面・出力に表示されること
    ③ ステップ3 の Name が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 監査証跡の保存 APP18 {#c10-i0328}
*分類: アプライアンス健全性*  ・  難易度: 上級

監査証跡の保存では アプライアンス健全性 の ジョブキュー を主操作として APP18 を判定します。実行者と結果の対応への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP18 に残します。監査証跡の保存を補助する 監視プロセス では Appliance を補助値として APP18 へ保存します。主判定の監査証跡の保存ではアプライアンス健全性の ジョブキュー から JobName を読み APP18 へ残します。証跡照合の監査証跡の保存ではアプライアンス健全性の JobName と Appliance を APP18 に保存します。記録対応の監査証跡の保存ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP18 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 監査証跡の保存 APP18の役割を調べています。ロールと権限 Application Access 0015の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はGuardAPI実行権限不足を避けるため・監査操作で記録欄を比較するしてユーザー有効を照合する。
    - B. 障害切り分けに用いる役割は未承認監視エージェント接続を避けるため・記録操作で証跡欄を照合するして暗号化表示を照合する。S-TAP監視 S-TAP Version 0193固有の属性も確認対象に含める。
    - C. 障害切り分けに用いる役割はディスク逼迫中に検査データ流入をを避けるため・ジョブキューからJobNameを読むしてジョブキューを照合する。 ✅
    - D. 障害切り分けに用いる役割はキュー状態の誤読を避けるため・状態確認でキュー状態を確認するしてキュー状態を照合する。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能ジョブ・ディスでCの記述「Appliance Monitoriでジョブキューから」に対応する項目は監査証跡の保存 APP18（App・ジョブ・監査証）です。照合ジョブ・監査証に関するアプライアンス健全性の仕様は「Appliance Monitoriでジョブキューから」で、確認対象はジョブ・監査証・ディスです。比較アプラ・監査証でA:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はApp・監査証・ジョブです。運用監査証・AppでB:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はジョブ・アプラ・監査証です。仕様ジョブ・監査証でD:の状態確認 キュー状態は「監査結果のレビューと承認の履歴」を述べるため、正答側の照合軸は監査証・ディス・ジョブです。用語ジョブ・監査証という用語は「Appliance Monitoriでジョブキューか」を指し、照合する値と誤認リスクの組合せはアプラ・ジョブ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 監査証跡の保存 APP18**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて監査可能な証跡を保存し、APP18のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP18と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP18のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP18 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP18の対応を確認します。実行者と結果の対応を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP18の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP18の対応を確認します。実行者と結果の対応を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP18のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP18の対応を確認します。実行者と結果の対応を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Name が画面・出力に表示されること
    ② ステップ2 の Appliance が画面・出力に表示されること
    ③ ステップ3 の TURBINE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 通常状態の確認 APP01 {#c10-i0329}
*分類: アプライアンス健全性*  ・  難易度: 上級

通常状態の確認では アプライアンス健全性 の 監視プロセス を主操作として APP01 を判定します。基準値と現在値の差への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP01 に残します。通常状態の確認を補助する DB処理一覧 では TURBINE を補助値として APP01 へ保存します。主判定の通常状態の確認ではアプライアンス健全性の 監視プロセス から Appliance を読み APP01 へ残します。証跡照合の通常状態の確認ではアプライアンス健全性の Appliance と TURBINE を APP01 に保存します。記録対応の通常状態の確認ではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP01 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「アプライアンス健全性 Appliance Monitoring 通常状態の確認 APP01」を「S-TAP監視 DB Server Type 0010」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は監視エージェントの承認クライアントと取得時刻を記録し・最終応答停止の見落としを防ぐである。確認操作で状態欄を整理するときは最終応答停止の見落としを防ぐ。S-TAP監視 DB Server Type 0010固有の属性も確認対象に含める。
    - B. 運用時に利用する技術的役割は照会文 Verbのジョブキューと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。
    - C. 運用時に利用する技術的役割は管理対象システムの構成と配布を統制する管理点を承認履歴確認する。承認履歴確認で構成配布を確認するときは構成配布の誤読を防ぐ。
    - D. 運用時に利用する技術的役割はAppliance Monitoriで監視プロセスから Appliance を読み・Appliance とである。監視プロセスからApplianceをときはディスク逼迫中に検査データ流を防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能監視プ・ディスでDの記述「Appliance Monitoriで監視プロセスから」に対応する項目は通常状態の確認 APP01（App・監視プ・通常状）です。照合監視プ・通常状に関するアプライアンス健全性の仕様は「Appliance Monitoriで監視プロセスから」で、確認対象は監視プ・通常状・ディスです。比較アプラ・通常状でA:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はApp・通常状・監視プです。運用通常状・AppでB:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は監視プ・アプラ・通常状です。項目監視プ・通常状でC:の承認履歴確認 構成配布は「管理対象システムの構成と配布を統制する管理点」を述べるため、正答側の照合軸はディス・アプラ・監視プです。用語監視プ・通常状という用語は「Appliance Monitoriで監視プロセスか」を指し、照合する値と誤認リスクの組合せはアプラ・監視プ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 通常状態の確認 APP01**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて通常状態を確定し、APP01のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP01の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP01のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP01のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP01 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Appliance が画面・出力に表示されること
    ② ステップ2 の TURBINE が画面・出力に表示されること
    ③ ステップ3 の Name が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### アプライアンス健全性 Appliance Monitoring 障害切り分け APP04 {#c10-i0330}
*分類: アプライアンス健全性*  ・  難易度: 上級

障害切り分けでは アプライアンス健全性 の 監視プロセス を主操作として APP04 を判定します。最初に失敗した処理への注意として「ディスク逼迫中に検査データ流入を放置して監査DBを停止させる危険があります」を APP04 に残します。障害切り分けを補助する DB処理一覧 では TURBINE を補助値として APP04 へ保存します。主判定の障害切り分けではアプライアンス健全性の 監視プロセス から Appliance を読み APP04 へ残します。証跡照合の障害切り分けではアプライアンス健全性の Appliance と TURBINE を APP04 に保存します。記録対応の障害切り分けではアプライアンス健全性の Process CountとDisk Usage の証跡へ APP04 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** アプライアンス健全性 Appliance Monitoring 障害切り分け APP04の技術的な意味を資料で確認するとき、S-TAP監視 KTAP Installed 0004との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は保守操作で監査欄を保存することで監視エージェを確認し・ローカル通信制御監視の未確認を防ぐ。
    - B. 構成を確認する際の意味は点検操作で判定欄を記録することで監査タスクを確認し・照会文動詞集計の期間誤りを防ぐ。
    - C. 構成を確認する際の意味は報告上限からmax_audit_repoことで報告上限を確認し・実行間隔より短いFROM/Tを防ぐ。監査プロセス Audit Process Builder固有の属性も確認対象に含める。
    - D. 構成を確認する際の意味は監視プロセスからApplianceを読むことで監視プロセスを確認し・ディスク逼迫中に検査データ流を防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能監視プ・ディスでDの記述「Appliance Monitoriで監視プロセスから」に対応する項目は障害切り分け APP04（App・監視プ・アプラ）です。照合監視プ・アプラに関するアプライアンス健全性の仕様は「Appliance Monitoriで監視プロセスから」で、確認対象は監視プ・アプラ・ディスです。比較アプラ・アプラでA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はApp・アプラ・監視プです。運用アプラ・AppでB:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸は監視プ・アプラ・アプラです。項目監視プ・アプラでC:の監査証跡の保存 AUDIT18は「Audit Processで報告上限から」を述べるため、正答側の照合軸はディス・アプラ・監視プです。用語監視プ・アプラという用語は「Appliance Monitoriで監視プロセスか」を指し、照合する値と誤認リスクの組合せはアプラ・監視プ・ディスです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **アプライアンス健全性 Appliance Monitoring 障害切り分け APP04**

    - 検証目的: アプライアンス健全性のAppliance Monitoringについて障害範囲を限定し、APP04のProcess CountとDisk Usageを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象APP04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へComply > Audit Process Builder > Appliance Monitoringを指定し、APP04の監視プロセスを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process Builder > Appliance Monitoring
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process | Status | Reports
    Appliance Monitoring | Active | 12
    ```

    画面・出力にあるApplianceを読み、Process CountとDisk Usageと対象APP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へsupport show db-processlist runningを指定し、APP04のDB処理一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> support show db-processlist running
    → Enter を押す
    ```

    画面・出力:
    ```text
    Id | User | Host | db | Command | Time | State | Info
    141791 | guardium | localhost | TURBINE | Query | 0 | init | show processlist
    ```

    画面・出力にあるTURBINEを読み、Process CountとDisk Usageと対象APP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのアプライアンス健全性を確認する入力画面です。COMMAND入力口へReports > Guardium Job Queueを指定し、APP04のジョブキューを表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Guardium Job Queue
    → Enter を押す
    ```

    画面・出力:
    ```text
    Job Name | Type | Start Time | Status
    APP04 | Audit Process | 2026-07-15 13:15 | Completed
    ```

    画面・出力にあるNameを読み、Process CountとDisk Usageと対象APP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Appliance が画面・出力に表示されること
    ② ステップ2 の TURBINE が画面・出力に表示されること
    ③ ステップ3 の Name が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring




## IBM Guardium Data Protection 12.x > データソース管理

### Guardium Job Queue 承認履歴確認 入力欄 {#c10-i0331}
*分類: データソース管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の データソース管理 で扱う「Guardium Job Queue 承認履歴確認 入力欄」は、処理ID、状態、開始終了時刻、Data Sources を示すジョブ一覧を承認履歴確認の観点で確認する技術項目です。Guardium Job QueueとCOL027を同じ記録で見比べることで、監査タスク未完了を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** Guardium Job Queue 承認履歴確認 入力欄について構成や状態を確認します。Central Manager 中央管理サーバー 依存関係の確認 CM13ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは処理ID・状態・開始終了時刻・Data Sources を示すジョブ一覧を承認履歴確認する。承認履歴確認で入力欄を確認するときは入力欄の誤読を防ぐ。 ✅
    - B. 対象資源に対する働きはCentral Managerで依存関係の確認では中央管理サーバーの 管理単位状態からである。依存関係確認で確認では中央を確認するときはmanaged unitからを防ぐ。
    - C. 対象資源に対する働きはRoleのディレクトリー取込と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。
    - D. 対象資源に対する働きはディレクトリー UserのGuardAPI権限と取得時刻を記録し・ディレクトリー取込対象の誤りを防ぐである。変更確認操作で採取欄を棚卸するときはディレクトリー取込対象の誤りを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能入力欄・入力欄でAの記述「処理ID、状態、開始終了時刻、Data Sources」に対応する項目は承認履歴確認 入力欄（Gua・入力欄・承認履）です。照合入力欄・承認履に関するデータソース管理の仕様は「処理ID、状態、開始終了時刻、Data Sources」で、確認対象は入力欄・承認履・入力欄です。運用承認履・GuaでB:の依存関係の確認 CM13は「Central Managerで依存関係の確」を述べるため、正答側の照合軸は入力欄・承認履・承認履です。項目入力欄・承認履でC:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は入力欄・承認履・入力欄です。仕様入力欄・承認履でD:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は承認履・入力欄・入力欄です。用語入力欄・承認履という用語は「処理ID、状態、開始終了時刻、Data」を指し、照合する値と誤認リスクの組合せは承認履・入力欄・入力欄です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **Guardium Job Queue 承認履歴確認 入力欄**

    - 検証目的: データソース管理のGuardium Job Queue 承認履歴確認 入力欄について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、データソース管理の対象へ進みます。
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
    I/O metrics collection request accepted for appliance COL027.
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
    STAP027     Approved    COL027
    ```

    画面・出力には Approved が含まれ、Guardium Job Queue 承認履歴確認 入力欄の証跡を確認できます。

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
    AP027            Completed   DSRC027
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### Guardium Job Queue 証跡採取 自動処理 {#c10-i0332}
*分類: データソース管理*  ・  難易度: 上級

IBM Guardium Data Protection 12.x の データソース管理 で扱う「Guardium Job Queue 証跡採取 自動処理」は、処理ID、状態、開始終了時刻、Data Sources を示すジョブ一覧を証跡採取の観点で確認する技術項目です。Guardium Job QueueとCOL057を同じ記録で見比べることで、監査タスク未完了を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** 「Guardium Job Queue 証跡採取 自動処理」を「Central Manager 中央管理サーバー 権限境界の確認 CM12」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は証跡採取で自動処理を確認することで自動処理を確認し・自動処理の誤読を防ぐ。 ✅
    - B. 保守作業で参照する機能は権限境界確認で権限境界の確を確認することで権限境界の確を確認し・managed unitからを防ぐ。
    - C. 保守作業で参照する機能は記録操作で証跡欄を照合することで暗号化表示を確認し・未承認監視エージェント接続を防ぐ。
    - D. 保守作業で参照する機能は照合操作で確認欄を採取することでユーザー有効を確認し・監査担当者の閲覧範囲不足を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能自動処・自動処でAの記述「処理ID、状態、開始終了時刻、Data Sources」に対応する項目は証跡採取 自動処理（Gua・自動処・証跡採）です。照合自動処・証跡採に関するデータソース管理の仕様は「処理ID、状態、開始終了時刻、Data Sources」で、確認対象は自動処・証跡採・自動処です。運用証跡採・GuaでB:の権限境界の確認 CM12は「Central ManagerでCentra」を述べるため、正答側の照合軸は自動処・証跡・証跡採です。項目自動処・証跡採でC:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は自動処・証跡・自動処です。仕様自動処・証跡採でD:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は証跡採・自動処・自動処です。用語自動処・証跡採という用語は「処理ID、状態、開始終了時刻、Data」を指し、照合する値と誤認リスクの組合せは証跡・自動処・自動処です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **Guardium Job Queue 証跡採取 自動処理**

    - 検証目的: データソース管理のGuardium Job Queue 証跡採取 自動処理について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、データソース管理の対象へ進みます。
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
    I/O metrics collection request accepted for appliance COL057.
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
    STAP057     Approved    COL057
    ```

    画面・出力には Approved が含まれ、Guardium Job Queue 証跡採取 自動処理の証跡を確認できます。

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
    AP057            Completed   DSRC057
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### aggregator 実行結果照合 接続状態 {#c10-i0333}
*分類: データソース管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の データソース管理 で扱う「aggregator 実行結果照合 接続状態」は、複数 collector の監査情報を集約しレポートへ渡す装置を実行結果照合の観点で確認する技術項目です。support gather_io_metrics 出力とSTAP015を同じ記録で見比べることで、S-TAP 未承認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** aggregator 実行結果照合 接続状態の設定や表示を読む前に役割を確認します。データソース管理 Guardiumデータソース 容量余力の確認 DSRC16ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは接続状態の誤読を避けるため・実行結果照合で接続状態を確認するして接続状態を照合する。 ✅
    - B. 対象資源に対する働きは廃止サーバーの参照を残して監査対を避けるため・データソース一覧からServiceNamしてデータソースを照合する。
    - C. 対象資源に対する働きは監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するしてディレクトリを照合する。
    - D. 対象資源に対する働きはカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして監視エージェを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能接続状・接続状でAの記述「複数 collector の監査情報を集約しレポートへ渡」に対応する項目は実行結果照合 接続状態（agg・接続状・実行結）です。照合接続状・実行結に関するデータソース管理の仕様は「複数 collector の監査情報を集約しレポートへ渡す装置を実行」で、確認対象は接続状・実行結・接続状です。運用実行結・aggでB:の容量余力の確認 DSRC16は「Guardiumでデータソース一覧から」を述べるため、正答側の照合軸は接続状・実行結・実行結です。項目接続状・実行結でC:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は接続状・実行結・接続状です。仕様接続状・実行結でD:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸は実行結・接続状・接続状です。用語接続状・実行結という用語は「複数 collector の監査情報を集約しレポート」を指し、照合する値と誤認リスクの組合せは実行結・接続状・接続状です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **aggregator 実行結果照合 接続状態**

    - 検証目的: データソース管理のaggregator 実行結果照合 接続状態について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、データソース管理の対象へ進みます。
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
    I/O metrics collection request accepted for appliance COL015.
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
    STAP015     Approved    COL015
    ```

    画面・出力には Approved が含まれ、aggregator 実行結果照合 接続状態の証跡を確認できます。

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
    AP015            Completed   DSRC015
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### aggregator 状態確認 スケジュール {#c10-i0334}
*分類: データソース管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の データソース管理 で扱う「aggregator 状態確認 スケジュール」は、複数 collector の監査情報を集約しレポートへ渡す装置を状態確認の観点で確認する技術項目です。support gather_io_metrics 出力とSTAP045を同じ記録で見比べることで、S-TAP 未承認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** aggregator 状態確認 スケジュールを保守記録に説明する必要があります。監査プロセス Audit Process Builder 容量余力の確認と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は容量余力確認でプロセス一覧を証跡に残し・Audit Processでプロセス一覧から。
    - B. 保守作業で参照する機能は監査で最終応答を証跡に残し・監視エージェントの最終応答と取得時刻を記録し。S-TAP監視 S-TAP Host 0061固有の属性も確認対象に含める。
    - C. 保守作業で参照する機能は状態確認でスケジュールを証跡に残し・複数 collector の監査情報を集約しレポートへ渡す装。 ✅
    - D. 保守作業で参照する機能は確認でユーザー有効を証跡に残し・Application Accessのユーザー有効化と取得時。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能スケジ・スケジでCの記述「複数 collector の監査情報を集約しレポートへ渡」に対応する項目は状態確認 スケジュール（agg・スケジ・状態確）です。照合スケジ・状態確に関するデータソース管理の仕様は「複数 collector の監査情報を集約しレポートへ渡す装置」で、確認対象はスケジ・状態確・スケジです。比較状態・状態確でA:の容量余力の確認 AUDIT16は「Audit Processでプロセス一覧から」を述べるため、正答側の照合軸はagg・状態確・スケジです。運用状態確・aggでB:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はスケジ・状態・状態確です。仕様スケジ・状態確でD:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は状態確・スケジ・スケジです。用語スケジ・状態確という用語は「複数 collector の監査情報を集約しレポート」を指し、照合する値と誤認リスクの組合せは状態・スケジ・スケジです。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **aggregator 状態確認 スケジュール**

    - 検証目的: データソース管理のaggregator 状態確認 スケジュールについて、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、データソース管理の対象へ進みます。
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
    I/O metrics collection request accepted for appliance COL045.
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
    STAP045     Approved    COL045
    ```

    画面・出力には Approved が含まれ、aggregator 状態確認 スケジュールの証跡を確認できます。

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
    AP045            Completed   DSRC045
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### audit process 承認履歴確認 保護設定 {#c10-i0335}
*分類: データソース管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の データソース管理 で扱う「audit process 承認履歴確認 保護設定」は、監査要件に沿ってレポート実行とレビューを束ねる処理を承認履歴確認の観点で確認する技術項目です。Approved TAP Clients レポートとDSRC021を同じ記録で見比べることで、collector と aggregator の時刻差を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** audit process 承認履歴確認 保護設定を保守記録に説明する必要があります。監査プロセス Audit Process Builder 変更後の確認と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はAudit Processで報告上限から max_audit_reporting を読みである。報告上限からmax_audit_reときは実行間隔より短いFROM/Tを防ぐ。
    - B. 保守作業で参照する機能は照会文 Verbのジョブキューと取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。
    - C. 保守作業で参照する機能はServer IPのデータソースと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。
    - D. 保守作業で参照する機能は監査要件に沿ってレポート実行とレビューを束ねる処理を承認履歴確認する。保護設定で保護設定を確認するときは保護設定の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能保護設・保護設でDの記述「監査要件に沿ってレポート実行とレビューを束ねる処理を承認」に対応する項目は承認履歴確認 保護設定（aud・保護設・保護設）です。照合保護設・保護設に関するデータソース管理の仕様は「監査要件に沿ってレポート実行とレビューを束ねる処理を承認履歴確認する」で、確認対象は保護設・保護設・保護設です。比較承認履・保護設でA:の変更後の確認 AUDIT03は「Audit Processで報告上限から」を述べるため、正答側の照合軸はaud・保護設・保護設です。運用保護設・audでB:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は保護設・承認履・保護設です。項目保護設・保護設でC:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は保護設・承認履・保護設です。用語保護設・保護設という用語は「監査要件に沿ってレポート実行とレビューを束ねる処理を」を指し、照合する値と誤認リスクの組合せは承認履・保護設・保護設です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **audit process 承認履歴確認 保護設定**

    - 検証目的: データソース管理のaudit process 承認履歴確認 保護設定について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、データソース管理の対象へ進みます。
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
    I/O metrics collection request accepted for appliance COL021.
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
    STAP021     Approved    COL021
    ```

    画面・出力には Approved が含まれ、audit process 承認履歴確認 保護設定の証跡を確認できます。

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
    AP021            Completed   DSRC021
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### audit process 証跡採取 重大度 {#c10-i0336}
*分類: データソース管理*  ・  難易度: 上級

IBM Guardium Data Protection 12.x の データソース管理 で扱う「audit process 証跡採取 重大度」は、監査要件に沿ってレポート実行とレビューを束ねる処理を証跡採取の観点で確認する技術項目です。Approved TAP Clients レポートとDSRC051を同じ記録で見比べることで、collector と aggregator の時刻差を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** audit process 証跡採取 重大度について構成や状態を確認します。データソース管理 Guardiumデータソース 監査証跡の保存 DSRC18ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはGuardiumで変更履歴から Operation を読み・Operation と ServiceNameである。変更履歴からOperationを読むときは廃止サーバーの参照を残して監を防ぐ。
    - B. 対象資源に対する働きはPermissionの表示可能レポートと取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。
    - C. 対象資源に対する働きは監査要件に沿ってレポート実行とレビューを束ねる処理を証跡採取として確認する。証跡採取で重大度を確認するときは重大度の誤読を防ぐ。 ✅
    - D. 対象資源に対する働きは監視エージェントのカーネル監視有無と取得時刻を記録し・ローカル通信制御監視の未確認を防ぐである。保守操作で監査欄を保存するときはローカル通信制御監視の未確認を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能重大度・重大度でCの記述「監査要件に沿ってレポート実行とレビューを束ねる処理を証跡」に対応する項目は証跡採取 重大度（aud・重大度・証跡採）です。照合重大度・証跡採に関するデータソース管理の仕様は「監査要件に沿ってレポート実行とレビューを束ねる処理を証跡採取として確」で、確認対象は重大度・証跡採・重大度です。比較証跡・証跡採でA:の監査証跡の保存 DSRC18は「Guardiumで変更履歴から」を述べるため、正答側の照合軸はaud・証跡採・重大度です。運用証跡採・audでB:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸は重大度・証跡・証跡採です。仕様重大度・証跡採でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は証跡採・重大度・重大度です。用語重大度・証跡採という用語は「監査要件に沿ってレポート実行とレビューを束ねる処理を」を指し、照合する値と誤認リスクの組合せは証跡・重大度・重大度です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **audit process 証跡採取 重大度**

    - 検証目的: データソース管理のaudit process 証跡採取 重大度について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、データソース管理の対象へ進みます。
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
    I/O metrics collection request accepted for appliance COL051.
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
    STAP051     Approved    COL051
    ```

    画面・出力には Approved が含まれ、audit process 証跡採取 重大度の証跡を確認できます。

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
    AP051            Completed   DSRC051
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### datasource 対象絞り込み 接続先 {#c10-i0337}
*分類: データソース管理*  ・  難易度: 初級

IBM Guardium Data Protection 12.x の データソース管理 で扱う「datasource 対象絞り込み 接続先」は、監視対象データベースやサービスを表す Guardium の登録単位を対象絞り込みの観点で確認する技術項目です。audit process logとRUN003を同じ記録で見比べることで、データソース指定漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** datasource 対象絞り込み 接続先について構成や状態を確認します。Guardium Job Queue 対象絞り込み ノード割当ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは処理ID・状態・開始終了時刻・Data Sources を示すジョブ一覧を対象絞り込みとして確認する。Centraでノード割当を確認するときはノード割当の誤読を防ぐ。
    - B. 対象資源に対する働きは監視対象データベースやサービスを表す Guardium の登録単位を対象絞り込みとして確認する。データソースで接続先を確認するときは接続先の誤読を防ぐ。 ✅
    - C. 対象資源に対する働きはApplication Accessのユーザー有効化と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。
    - D. 対象資源に対する働きは照会文 Verbのジョブキューと取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能接続先・接続先でBの記述「監視対象データベースやサービスを表す Guardium」に対応する項目は対象絞り込み 接続先（dat・接続先・データ）です。照合接続先・データに関するデータソース管理の仕様は「監視対象データベースやサービスを表す Guardium」で、確認対象は接続先・データ・接続先です。比較対象絞・データでA:の対象絞り込み ノード割当は「処理ID、状態、開始終了時刻、Data」を述べるため、正答側の照合軸はdat・データ・接続先です。項目接続先・データでC:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は接続先・対象絞・接続先です。仕様接続先・データでD:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はデータ・接続先・接続先です。用語接続先・データという用語は「監視対象データベースやサービスを表す」を指し、照合する値と誤認リスクの組合せは対象絞・接続先・接続先です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **datasource 対象絞り込み 接続先**

    - 検証目的: データソース管理のdatasource 対象絞り込み 接続先について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、データソース管理の対象へ進みます。
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
    I/O metrics collection request accepted for appliance COL003.
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
    STAP003     Approved    COL003
    ```

    画面・出力には Approved が含まれ、datasource 対象絞り込み 接続先の証跡を確認できます。

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
    AP003            Completed   DSRC003
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### datasource 障害時切り分け 再同期判断 {#c10-i0338}
*分類: データソース管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の データソース管理 で扱う「datasource 障害時切り分け 再同期判断」は、監視対象データベースやサービスを表す Guardium の登録単位を障害時切り分けの観点で確認する技術項目です。audit process logとRUN033を同じ記録で見比べることで、データソース指定漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** 「datasource 障害時切り分け 再同期判断」を「Central Manager 中央管理サーバー 変更前の確認 CM02」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はデータソースで再同期判断を証跡に残し・監視対象データベースやサービスを表す Guardium。 ✅
    - B. 保守作業で参照する機能は変更確認で変更前の確認を証跡に残し・Central Managerで変更前の確認では中央管理サー。
    - C. 保守作業で参照する機能は移行でジョブキューを証跡に残し・照会文 Verbのジョブキューと取得時刻を記録し。
    - D. 保守作業で参照する機能は登録で表示可能レポを証跡に残し・Permissionの表示可能レポートと取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能再同期・再同期でAの記述「監視対象データベースやサービスを表す Guardium」に対応する項目は障害時切り分け 再同期判断（dat・再同期・データ）です。照合再同期・データに関するデータソース管理の仕様は「監視対象データベースやサービスを表す Guardium」で、確認対象は再同期・データ・再同期です。運用データ・datでB:の変更前の確認 CM02は「Central Managerで変更前の確認」を述べるため、正答側の照合軸は再同期・障害時・データです。項目再同期・データでC:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は再同期・障害時・再同期です。仕様再同期・データでD:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はデータ・再同期・再同期です。用語再同期・データという用語は「監視対象データベースやサービスを表す」を指し、照合する値と誤認リスクの組合せは障害時・再同期・再同期です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **datasource 障害時切り分け 再同期判断**

    - 検証目的: データソース管理のdatasource 障害時切り分け 再同期判断について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、データソース管理の対象へ進みます。
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
    I/O metrics collection request accepted for appliance COL033.
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
    STAP033     Approved    COL033
    ```

    画面・出力には Approved が含まれ、datasource 障害時切り分け 再同期判断の証跡を確認できます。

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
    AP033            Completed   DSRC033
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### inspection engine 対象絞り込み 復旧手掛かり {#c10-i0339}
*分類: データソース管理*  ・  難易度: 初級

IBM Guardium Data Protection 12.x の データソース管理 で扱う「inspection engine 対象絞り込み 復旧手掛かり」は、データベース通信を解析し監査レコードを作る処理を対象絞り込みの観点で確認する技術項目です。Data Sources 欄とAP009を同じ記録で見比べることで、サインオフ不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** 「inspection engine 対象絞り込み 復旧手掛かり」を「collector 承認履歴確認 伝搬経路」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は復旧手掛かりの誤読を避けるため・復旧手掛かりで復旧手掛かりを確認するして復旧手掛かりを照合する。 ✅
    - B. 保守作業で参照する機能は伝搬経路の誤読を避けるため・承認履歴確認で伝搬経路を確認するして伝搬経路を照合する。collector 承認履歴確認 伝搬経路固有の属性も確認対象に含める。
    - C. 保守作業で参照する機能はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして承認クライアを照合する。
    - D. 保守作業で参照する機能は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するしてジョブキューを照合する。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能復旧手・復旧手でAの記述「データベース通信を解析し監査レコードを作る処理を対象絞り」に対応する項目は対象絞り込み 復旧手掛かり（ins・復旧手・復旧手）です。照合復旧手・復旧手に関するデータソース管理の仕様は「データベース通信を解析し監査レコードを作る処理を対象絞り込みとして確」で、確認対象は復旧手・復旧手・復旧手です。運用復旧手・insでB:の承認履歴確認 伝搬経路は「S-TAP や外部接続から監査データを受け取」を述べるため、正答側の照合軸は復旧手・対象絞・復旧手です。項目復旧手・復旧手でC:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は復旧手・対象絞・復旧手です。仕様復旧手・復旧手でD:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は復旧手・復旧手・復旧手です。用語復旧手・復旧手という用語は「データベース通信を解析し監査レコードを作る処理を対象」を指し、照合する値と誤認リスクの組合せは対象絞・復旧手・復旧手です。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **inspection engine 対象絞り込み 復旧手掛かり**

    - 検証目的: データソース管理のinspection engine 対象絞り込み 復旧手掛かりについて、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、データソース管理の対象へ進みます。
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
    I/O metrics collection request accepted for appliance COL009.
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
    STAP009     Approved    COL009
    ```

    画面・出力には Approved が含まれ、inspection engine 対象絞り込み 復旧手掛かりの証跡を確認できます。

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
    AP009            Completed   DSRC009
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### inspection engine 障害時切り分け レビュー結果 {#c10-i0340}
*分類: データソース管理*  ・  難易度: 中級

IBM Guardium Data Protection 12.x の データソース管理 で扱う「inspection engine 障害時切り分け レビュー結果」は、データベース通信を解析し監査レコードを作る処理を障害時切り分けの観点で確認する技術項目です。Data Sources 欄とAP039を同じ記録で見比べることで、サインオフ不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide

??? question "確認問題（1問）"
    **問題.** inspection engine 障害時切り分け レビュー結果の設定や表示を読む前に役割を確認します。監査プロセス Audit Process Builder 再始動後の確認ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはAudit Processで報告上限から max_audit_reporting を読みである。報告上限からmax_audit_reときは実行間隔より短いFROM/Tを防ぐ。
    - B. 対象資源に対する働きはデータベース通信を解析し監査レコードを作る処理を障害時切り分けとして確認する。データソースでレビュー結果を確認するときはレビュー結果の誤読を防ぐ。 ✅
    - C. 対象資源に対する働きはApplication Accessのユーザー有効化と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。
    - D. 対象資源に対する働きはAudit Task Statusのユーザー活動と取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能レビュ・レビュでBの記述「データベース通信を解析し監査レコードを作る処理を障害時切」に対応する項目は障害時切り分け レビュー結果（ins・レビュ・データ）です。照合レビュ・データに関するデータソース管理の仕様は「データベース通信を解析し監査レコードを作る処理を障害時切り分けとして」で、確認対象はレビュ・データ・レビュです。比較障害時・データでA:の再始動後の確認 AUDIT15は「Audit Processで報告上限から」を述べるため、正答側の照合軸はins・データ・レビュです。項目レビュ・データでC:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はレビュ・障害時・レビュです。仕様レビュ・データでD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸はデータ・レビュ・レビュです。用語レビュ・データという用語は「データベース通信を解析し監査レコードを作る処理を障害」を指し、照合する値と誤認リスクの組合せは障害時・レビュ・レビュです。

    **出典:** IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide


??? note "検証手順（1件）"
    **inspection engine 障害時切り分け レビュー結果**

    - 検証目的: データソース管理のinspection engine 障害時切り分け レビュー結果について、IBM Guardium Data Protection 12.xの資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Guardium Data Protection 12.xの資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、データソース管理の対象へ進みます。
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
    I/O metrics collection request accepted for appliance COL039.
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
    STAP039     Approved    COL039
    ```

    画面・出力には Approved が含まれ、inspection engine 障害時切り分け レビュー結果の証跡を確認できます。

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
    AP039            Completed   DSRC039
    ```

    画面・出力には Audit が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Guardium が画面・出力に表示されること
    ② ステップ2 の Approved が画面・出力に表示されること
    ③ ステップ3 の Audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: IBM_Guardium_Data_Protection_12x_CLI_Commands / Predefined admin reports / Audit processes / S-TAP User's Guide



### データソース管理 Guardiumデータソース ログとの照合 DSRC07 {#c10-i0341}
*分類: データソース管理*  ・  難易度: 中級

ログとの照合では データソース管理 の データソース一覧 を主操作として DSRC07 を判定します。時刻と対象識別子への注意として「廃止サーバーの参照を残して監査対象を誤る危険があります」を DSRC07 に残します。ログとの照合を補助する 参照箇所 では UsedBy を補助値として DSRC07 へ保存します。主判定のログとの照合ではデータソース管理・データソースの データソース一覧 から ServiceName を読み DSRC07 へ残します。証跡照合のログとの照合ではデータソース管理・データソースの ServiceName と UsedBy を DSRC07 に保存します。記録対応のログとの照合ではデータソース管理・データソースの HostとService Name の証跡へ DSRC07 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** データソース管理 Guardiumデータソース ログとの照合 DSRC07の設定や表示を読む前に役割を確認します。Aggregator Guardium Aggregator 停止前の確認ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはデータソース一覧からServiceNamことでデータソースを確認し・廃止サーバーの参照を残して監を防ぐ。 ✅
    - B. 対象資源に対する働きは監査タスクからAdHocデータベースを読ことで監査タスクを確認し・集約遅延中の期間を監査完了とを防ぐ。
    - C. 対象資源に対する働きは表示操作で対象欄を追跡することで照会文動詞集を確認し・ジョブ失敗の見落としを防ぐ。
    - D. 対象資源に対する働きは表示操作で対象欄を追跡することで監査タスクを確認し・ジョブ失敗の見落としを防ぐ。監査レポート Client IP 0335固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能データ・廃止サでAの記述「Guardiumでデータソース一覧から」に対応する項目はログとの照合 DSRC07（Gua・データ・ログと）です。照合データ・ログとに関するデータソース管理の仕様は「Guardiumでデータソース一覧から ServiceName」で、確認対象はデータ・ログと・廃止サです。運用ログと・GuaでB:の停止前の確認 AGG14は「Aggregatorで監査タスクから」を述べるため、正答側の照合軸はデータ・データ・ログとです。項目データ・ログとでC:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は廃止サ・データ・データです。仕様データ・ログとでD:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸はログと・廃止サ・データです。用語データ・ログとという用語は「Guardiumでデータソース一覧から」を指し、照合する値と誤認リスクの組合せはデータ・データ・廃止サです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **データソース管理 Guardiumデータソース ログとの照合 DSRC07**

    - 検証目的: データソース管理のGuardiumデータソースについて操作とログを対応し、DSRC07のHostとService Nameを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象DSRC07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのデータソース管理を確認する入力画面です。COMMAND入力口へSetup > Tools and Views > Definitions > Datasource Definitionsを指定し、DSRC07のデータソース一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Setup > Tools and Views > Definitions > Datasource Definitions
    → Enter を押す
    ```

    画面・出力:
    ```text
    Data Source Name | Host | Port | Service Name
    DSRC07 | db07.example | 1521 | ORCL
    ```

    画面・出力にあるDataを読み、HostとService Nameと対象DSRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのデータソース管理を確認する入力画面です。COMMAND入力口へReports > Host references reportを指定し、DSRC07の参照箇所を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Host references report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Used By | Object Name
    db07.example | Audit Process | DSRC07
    db07.example | Assessment | VA07
    ```

    画面・出力にあるHostを読み、HostとService Nameと対象DSRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのデータソース管理を確認する入力画面です。COMMAND入力口へReports > Data Source Changesを指定し、DSRC07の変更履歴を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Data Source Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Operation | Data Source
    2026-07-15 13:00 | admin | UPDATE | DSRC07
    ```

    画面・出力にあるOperationを読み、HostとService Nameと対象DSRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Data が画面・出力に表示されること
    ② ステップ2 の Host が画面・出力に表示されること
    ③ ステップ3 の Operation が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### データソース管理 Guardiumデータソース 世代整合の確認 DSRC17 {#c10-i0342}
*分類: データソース管理*  ・  難易度: 中級

世代整合の確認では データソース管理 の 参照箇所 を主操作として DSRC17 を判定します。定義と実行モジュールの版への注意として「廃止サーバーの参照を残して監査対象を誤る危険があります」を DSRC17 に残します。世代整合の確認を補助する 変更履歴 では Operation を補助値として DSRC17 へ保存します。主判定の世代整合の確認ではデータソース管理・データソースの 参照箇所 から UsedBy を読み DSRC17 へ残します。証跡照合の世代整合の確認ではデータソース管理・データソースの UsedBy と Operation を DSRC17 に保存します。記録対応の世代整合の確認ではデータソース管理・データソースの HostとService Name の証跡へ DSRC17 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「データソース管理 Guardiumデータソース 世代整合の確認 DSRC17」を「Central Manager 中央管理サーバー 引継ぎ記録 CM09」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はCentral ManagerでCentral Managerの役割と出力を確認する。Centraで引継ぎ記録を確認するときはmanaged unitからを防ぐ。
    - B. 仕様上の役割はGuardiumで参照箇所から UsedBy を読み・UsedBy と Operation を照合する。参照箇所からUsedByを読むときは廃止サーバーの参照を残して監を防ぐ。 ✅
    - C. 仕様上の役割はServer IPのデータソースと取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。監査レポート Server IP 0122固有の属性も確認対象に含める。
    - D. 仕様上の役割は接続を許可された S-TAP と状態を確認する管理レポートである。状態確認で宛先定義を確認するときは宛先定義の誤読を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能参照箇・廃止サでBの記述「Guardiumで参照箇所から UsedBy を読み」に対応する項目は世代整合の確認 DSRC17（Gua・参照箇・世代整）です。照合参照箇・世代整に関するデータソース管理の仕様は「Guardiumで参照箇所から UsedBy を読み、UsedBy」で、確認対象は参照箇・世代整・廃止サです。比較データ・世代整でA:の引継ぎ記録 CM09は「Central ManagerでCentra」を述べるため、正答側の照合軸はGua・世代整・参照箇です。項目参照箇・世代整でC:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は廃止サ・データ・参照箇です。仕様参照箇・世代整でD:の状態確認 宛先定義は「接続を許可された S-TAP」を述べるため、正答側の照合軸は世代整・廃止サ・参照箇です。用語参照箇・世代整という用語は「Guardiumで参照箇所から UsedBy」を指し、照合する値と誤認リスクの組合せはデータ・参照箇・廃止サです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **データソース管理 Guardiumデータソース 世代整合の確認 DSRC17**

    - 検証目的: データソース管理のGuardiumデータソースについて世代差を検出し、DSRC17のHostとService Nameを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象DSRC17と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのデータソース管理を確認する入力画面です。COMMAND入力口へReports > Host references reportを指定し、DSRC17の参照箇所を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Host references report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Used By | Object Name
    db17.example | Audit Process | DSRC17
    db17.example | Assessment | VA17
    ```

    画面・出力にあるHostを読み、HostとService Nameと対象DSRC17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのデータソース管理を確認する入力画面です。COMMAND入力口へReports > Data Source Changesを指定し、DSRC17の変更履歴を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Data Source Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Operation | Data Source
    2026-07-15 13:00 | admin | UPDATE | DSRC17
    ```

    画面・出力にあるOperationを読み、HostとService Nameと対象DSRC17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのデータソース管理を確認する入力画面です。COMMAND入力口へSetup > Tools and Views > Definitions > Datasource Definitionsを指定し、DSRC17のデータソース一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Setup > Tools and Views > Definitions > Datasource Definitions
    → Enter を押す
    ```

    画面・出力:
    ```text
    Data Source Name | Host | Port | Service Name
    DSRC17 | db17.example | 1521 | ORCL
    ```

    画面・出力にあるDataを読み、HostとService Nameと対象DSRC17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Host が画面・出力に表示されること
    ② ステップ2 の Operation が画面・出力に表示されること
    ③ ステップ3 の Data が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


