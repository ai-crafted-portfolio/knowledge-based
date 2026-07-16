---
search:
  exclude: true
---

# IBM Guardium Data Protection 12.x — 詳細 (5/6)

[← IBM Guardium Data Protection 12.x の概要へ戻る](index.md)


## IBM Guardium Data Protection 12.x > ポリシー・検査エンジン

### ポリシー・検査エンジン Inspection Engine ログとの照合 IE07 {#c10-i0361}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

ログとの照合では ポリシー・検査エンジン の 検査状態 を主操作として IE07 を判定します。時刻と対象識別子への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE07 に残します。ログとの照合を補助する ポリシー変更 では Policy を補助値として IE07 へ保存します。主判定のログとの照合ではポリシー・検査エンジンの 検査状態 から LastResponse を読み IE07 へ残します。証跡照合のログとの照合ではポリシー・検査エンジンの LastResponse と Policy を IE07 に保存します。記録対応のログとの照合ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE07 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine ログとの照合 IE07について構成や状態を確認します。監査レポート SQL Verb 0026ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するしてジョブキューを照合する。監査レポート SQL Verb 0026固有の属性も確認対象に含める。
    - B. 対象資源に対する働きは過剰ロール付与を避けるため・主操作で出力欄を評価するしてGuardAを照合する。
    - C. 対象資源に対する働きはInspectionを避けるため・検査状態からLastResponseを読して検査状態を照合する。 ✅
    - D. 対象資源に対する働きはディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてロール割当を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能検査状・InsでCの記述「Inspection Engineで検査状態から」に対応する項目はログとの照合 IE07（Ins・検査状・ログと）です。照合検査状・ログとに関するポリシー・検査エンジンの仕様は「Inspection Engineで検査状態から」で、確認対象は検査状・ログと・Insです。比較検査エ・ログとでA:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はIns・ログと・検査状です。運用ログと・InsでB:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は検査状・検査エ・ログとです。仕様検査状・ログとでD:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸はログと・Ins・検査状です。用語検査状・ログとという用語は「Inspection Engineで検査状態から」を指し、照合する値と誤認リスクの組合せは検査エ・検査状・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine ログとの照合 IE07**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて操作とログを対応し、IE07のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE07の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db07.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE07のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE07 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE07のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db07.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の S-TAP が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Host が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 世代整合の確認 IE17 {#c10-i0362}
*分類: ポリシー・検査エンジン*  ・  難易度: 上級

世代整合の確認では ポリシー・検査エンジン の ポリシー変更 を主操作として IE17 を判定します。定義と実行モジュールの版への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE17 に残します。世代整合の確認を補助する エージェント変更 では InspectionEngine を補助値として IE17 へ保存します。主判定の世代整合の確認ではポリシー・検査エンジンの ポリシー変更 から Policy を読み IE17 へ残します。証跡照合の世代整合の確認ではポリシー・検査エンジンの Policy と InspectionEngine を IE17 に保存します。記録対応の世代整合の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE17 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 世代整合の確認 IE17を保守記録に説明する必要があります。監査レポート DB User Name 0074と取り違えない説明はどれですか。

    - A. 仕様上の役割は照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するして照会文動詞集を照合する。
    - B. 仕様上の役割は対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてジョブキューを照合する。
    - C. 仕様上の役割はInspectionを避けるため・ポリシー変更からPolicyを読むしてポリシー変更を照合する。 ✅
    - D. 仕様上の役割は停止時刻の誤読を避けるため・証跡採取で停止時刻を確認するして停止時刻を照合する。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能ポリシ・InsでCの記述「Inspection Engineでポリシー変更から」に対応する項目は世代整合の確認 IE17（Ins・ポリシ・世代整）です。照合ポリシ・世代整に関するポリシー・検査エンジンの仕様は「Inspection Engineでポリシー変更から Policy」で、確認対象はポリシ・世代整・Insです。比較検査エ・世代整でA:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸はIns・世代整・ポリシです。運用世代整・InsでB:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はポリシ・検査エ・世代整です。仕様ポリシ・世代整でD:の証跡採取 停止時刻は「接続を許可された S-TAP」を述べるため、正答側の照合軸は世代整・Ins・ポリシです。用語ポリシ・世代整という用語は「Inspection Engineでポリシー変更から」を指し、照合する値と誤認リスクの組合せは検査エ・ポリシ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 世代整合の確認 IE17**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて世代差を検出し、IE17のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE17と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE17のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE17 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE17のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db17.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE17の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db17.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE17の対応を確認します。定義と実行モジュールの版を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Host が画面・出力に表示されること
    ③ ステップ3 の S-TAP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 代替経路の確認 IE10 {#c10-i0363}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

代替経路の確認では ポリシー・検査エンジン の 検査状態 を主操作として IE10 を判定します。主経路との役割差への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE10 に残します。代替経路の確認を補助する ポリシー変更 では Policy を補助値として IE10 へ保存します。主判定の代替経路の確認ではポリシー・検査エンジンの 検査状態 から LastResponse を読み IE10 へ残します。証跡照合の代替経路の確認ではポリシー・検査エンジンの LastResponse と Policy を IE10 に保存します。記録対応の代替経路の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE10 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 代替経路の確認 IE10に関する障害切り分けの前提を確認しています。S-TAP監視 S-TAP Version 0028の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はInspectionを避けるため・検査状態からLastResponseを読して検査状態を照合する。 ✅
    - B. 表示や設定で扱う内容はローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するして暗号化表示を照合する。S-TAP監視 S-TAP Version 0028固有の属性も確認対象に含める。
    - C. 表示や設定で扱う内容はディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてロール割当を照合する。
    - D. 表示や設定で扱う内容は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するしてユーザー活動を照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能検査状・InsでAの記述「Inspection Engineで検査状態から」に対応する項目は代替経路の確認 IE10（Ins・検査状・代替経）です。照合検査状・代替経に関するポリシー・検査エンジンの仕様は「Inspection Engineで検査状態から」で、確認対象は検査状・代替経・Insです。運用代替経・InsでB:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は検査状・検査エ・代替経です。項目検査状・代替経でC:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸はIns・検査エ・検査状です。仕様検査状・代替経でD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は代替経・Ins・検査状です。用語検査状・代替経という用語は「Inspection Engineで検査状態から」を指し、照合する値と誤認リスクの組合せは検査エ・検査状・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 代替経路の確認 IE10**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて代替手段の成立を確認し、IE10のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE10の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db10.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE10のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE10 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE10のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db10.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の S-TAP が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Host が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 依存関係の確認 IE13 {#c10-i0364}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

依存関係の確認では ポリシー・検査エンジン の 検査状態 を主操作として IE13 を判定します。前提資源と後続処理の順序への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE13 に残します。依存関係の確認を補助する ポリシー変更 では Policy を補助値として IE13 へ保存します。主判定の依存関係の確認ではポリシー・検査エンジンの 検査状態 から LastResponse を読み IE13 へ残します。証跡照合の依存関係の確認ではポリシー・検査エンジンの LastResponse と Policy を IE13 に保存します。記録対応の依存関係の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE13 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「ポリシー・検査エンジン Inspection Engine 依存関係の確認 IE13」を「アプライアンス健全性 Appliance Monitoring 変更前の確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はDB処理一覧からTURBINEを読むことでデータベースを確認し・ディスク逼迫中に検査データ流を防ぐ。
    - B. 保守作業で参照する機能は監査操作で記録欄を比較することでGuardAを確認し・GuardAPI実行権限不足を防ぐ。
    - C. 保守作業で参照する機能は検査状態からLastResponseを読ことで検査状態を確認し・Inspectionを防ぐ。 ✅
    - D. 保守作業で参照する機能はCentraで同期範囲を確認することで同期範囲を確認し・同期範囲の誤読を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能検査状・InsでCの記述「Inspection Engineで検査状態から」に対応する項目は依存関係の確認 IE13（Ins・検査状・依存関）です。照合検査状・依存関に関するポリシー・検査エンジンの仕様は「Inspection Engineで検査状態から」で、確認対象は検査状・依存関・Insです。比較検査エ・依存関でA:の変更前の確認 APP02は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸はIns・依存関・検査状です。運用依存関・InsでB:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は検査状・検査エ・依存関です。仕様検査状・依存関でD:の障害時切り分け 同期範囲は「処理ID、状態、開始終了時刻、Data」を述べるため、正答側の照合軸は依存関・Ins・検査状です。用語検査状・依存関という用語は「Inspection Engineで検査状態から」を指し、照合する値と誤認リスクの組合せは検査エ・検査状・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 依存関係の確認 IE13**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて依存資源を点検し、IE13のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE13の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db13.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE13のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE13 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE13のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db13.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の S-TAP が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Host が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 保守後の確認 IE20 {#c10-i0365}
*分類: ポリシー・検査エンジン*  ・  難易度: 上級

保守後の確認では ポリシー・検査エンジン の ポリシー変更 を主操作として IE20 を判定します。有効化された定義と版数への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE20 に残します。保守後の確認を補助する エージェント変更 では InspectionEngine を補助値として IE20 へ保存します。主判定の保守後の確認ではポリシー・検査エンジンの ポリシー変更 から Policy を読み IE20 へ残します。証跡照合の保守後の確認ではポリシー・検査エンジンの Policy と InspectionEngine を IE20 に保存します。記録対応の保守後の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE20 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 保守後の確認 IE20を同一分類のロールと権限 Application Access 0045と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は復旧でユーザー有効を証跡に残し・Application Accessのユーザー有効化と取得時。
    - B. コマンドまたは機能の用途は登録でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。
    - C. コマンドまたは機能の用途は保守確認でポリシー変更を証跡に残し・Inspection Engineでポリシー変更から。 ✅
    - D. コマンドまたは機能の用途は解除でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能ポリシ・InsでCの記述「Inspection Engineでポリシー変更から」に対応する項目は保守後の確認 IE20（Ins・ポリシ・保守確）です。照合ポリシ・保守確に関するポリシー・検査エンジンの仕様は「Inspection Engineでポリシー変更から Policy」で、確認対象はポリシ・保守確・Insです。比較検査エ・保守確でA:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はIns・保守確・ポリシです。運用保守確・InsでB:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸はポリシ・検査エ・保守確です。仕様ポリシ・保守確でD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は保守確・Ins・ポリシです。用語ポリシ・保守確という用語は「Inspection Engineでポリシー変更から」を指し、照合する値と誤認リスクの組合せは検査エ・ポリシ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 保守後の確認 IE20**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて保守反映を検証し、IE20のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE20と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE20のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE20 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE20の対応を確認します。有効化された定義と版数を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE20のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db20.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE20の対応を確認します。有効化された定義と版数を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE20の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db20.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE20の対応を確認します。有効化された定義と版数を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Host が画面・出力に表示されること
    ③ ステップ3 の S-TAP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 停止前の確認 IE14 {#c10-i0366}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

停止前の確認では ポリシー・検査エンジン の ポリシー変更 を主操作として IE14 を判定します。処理中資源と未完了要求への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE14 に残します。停止前の確認を補助する エージェント変更 では InspectionEngine を補助値として IE14 へ保存します。主判定の停止前の確認ではポリシー・検査エンジンの ポリシー変更 から Policy を読み IE14 へ残します。証跡照合の停止前の確認ではポリシー・検査エンジンの Policy と InspectionEngine を IE14 に保存します。記録対応の停止前の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE14 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 停止前の確認 IE14の役割を調べています。S-TAP監視 S-TAP Version 0028の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は保守操作で監査欄を保存することで暗号化表示を確認し・ローカル通信制御監視の未確認を防ぐ。
    - B. 障害切り分けに用いる役割は点検操作で判定欄を記録することでユーザー活動を確認し・照会文動詞集計の期間誤りを防ぐ。
    - C. 障害切り分けに用いる役割はポリシー変更からPolicyを読むことでポリシー変更を確認し・Inspectionを防ぐ。 ✅
    - D. 障害切り分けに用いる役割は調査操作で保守欄を引き継ぎすることでジョブキューを確認し・対象データソースの取り違えを防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ポリシ・InsでCの記述「Inspection Engineでポリシー変更から」に対応する項目は停止前の確認 IE14（Ins・ポリシ・停止確）です。照合ポリシ・停止確に関するポリシー・検査エンジンの仕様は「Inspection Engineでポリシー変更から Policy」で、確認対象はポリシ・停止確・Insです。比較検査エ・停止確でA:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はIns・停止確・ポリシです。運用停止確・InsでB:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸はポリシ・検査エ・停止確です。仕様ポリシ・停止確でD:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は停止確・Ins・ポリシです。用語ポリシ・停止確という用語は「Inspection Engineでポリシー変更から」を指し、照合する値と誤認リスクの組合せは検査エ・ポリシ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 停止前の確認 IE14**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて安全な停止条件を確認し、IE14のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE14のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE14 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE14のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db14.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE14の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db14.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Host が画面・出力に表示されること
    ③ ステップ3 の S-TAP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 再始動後の確認 IE15 {#c10-i0367}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

再始動後の確認では ポリシー・検査エンジン の エージェント変更 を主操作として IE15 を判定します。再開点と未処理データへの注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE15 に残します。再始動後の確認を補助する 検査状態 では LastResponse を補助値として IE15 へ保存します。主判定の再始動後の確認ではポリシー・検査エンジンの エージェント変更 から InspectionEngine を読み IE15 へ残します。証跡照合の再始動後の確認ではポリシー・検査エンジンの InspectionEngine と LastResponse を IE15 に保存します。記録対応の再始動後の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE15 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 再始動後の確認 IE15について構成や状態を確認します。S-TAP監視 DB Server Type 0040ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはエージェント変更からInspectionことでエージェントを確認し・Inspectionを防ぐ。 ✅
    - B. 状態を読み取るための働きは保守操作で監査欄を保存することで承認クライアを確認し・ローカル通信制御監視の未確認を防ぐ。
    - C. 状態を読み取るための働きは記録操作で証跡欄を照合することで暗号化表示を確認し・未承認監視エージェント接続を防ぐ。
    - D. 状態を読み取るための働きはプロセス一覧からScheduleを読むことでプロセス一覧を確認し・実行間隔より短いFROM/Tを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能エージ・InsでAの記述「Inspection Engineでエージェント変更から」に対応する項目は再始動後の確認 IE15（Ins・エージ・再始動）です。照合エージ・再始動に関するポリシー・検査エンジンの仕様は「Inspection Engineでエージェント変更から」で、確認対象はエージ・再始動・Insです。運用再始動・InsでB:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はエージ・検査エ・再始動です。項目エージ・再始動でC:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はIns・検査エ・エージです。仕様エージ・再始動でD:の障害切り分け AUDIT04は「Audit Processでプロセス一覧から」を述べるため、正答側の照合軸は再始動・Ins・エージです。用語エージ・再始動という用語は「Inspection Engineでエージェント変更」を指し、照合する値と誤認リスクの組合せは検査エ・エージ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 再始動後の確認 IE15**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて再始動結果を検証し、IE15のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE15のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db15.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE15の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db15.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE15のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE15 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Host が画面・出力に表示されること
    ② ステップ2 の S-TAP が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 変更前の確認 IE02 {#c10-i0368}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

変更前の確認では ポリシー・検査エンジン の ポリシー変更 を主操作として IE02 を判定します。変更対象と非対象の境界への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE02 に残します。変更前の確認を補助する エージェント変更 では InspectionEngine を補助値として IE02 へ保存します。主判定の変更前の確認ではポリシー・検査エンジンの ポリシー変更 から Policy を読み IE02 へ残します。証跡照合の変更前の確認ではポリシー・検査エンジンの Policy と InspectionEngine を IE02 に保存します。記録対応の変更前の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE02 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 変更前の確認 IE02に関する障害切り分けの前提を確認しています。ポリシー・検査エンジン Inspection Engine 障害切り分け IE04の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は変更確認でポリシー変更を証跡に残し・Inspection Engineでポリシー変更から。 ✅
    - B. 障害切り分けに用いる役割はポリシーで検査状態を証跡に残し・Inspection Engineで検査状態から。
    - C. 障害切り分けに用いる役割は保守でカーネル監視を証跡に残し・監視エージェントのカーネル監視有無と取得時刻を記録し。
    - D. 障害切り分けに用いる役割は監査プロセスでキーマップを証跡に残し・複数 collector の監査情報を集約しレポートへ渡す装。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ポリシ・InsでAの記述「Inspection Engineでポリシー変更から」に対応する項目は変更前の確認 IE02（Ins・ポリシ・変更確）です。照合ポリシ・変更確に関するポリシー・検査エンジンの仕様は「Inspection Engineでポリシー変更から Policy」で、確認対象はポリシ・変更確・Insです。運用変更確・InsでB:の障害切り分け IE04は「Inspection Engineで検査状態」を述べるため、正答側の照合軸はポリシ・検査エ・変更確です。項目ポリシ・変更確でC:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はIns・検査エ・ポリシです。仕様ポリシ・変更確でD:の対象絞り込み キーマップは「複数 collector の監査情報を集約し」を述べるため、正答側の照合軸は変更確・Ins・ポリシです。用語ポリシ・変更確という用語は「Inspection Engineでポリシー変更から」を指し、照合する値と誤認リスクの組合せは検査エ・ポリシ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 変更前の確認 IE02**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて変更前の証跡を保存し、IE02のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE02のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE02 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE02のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db02.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE02の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db02.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Host が画面・出力に表示されること
    ③ ステップ3 の S-TAP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 変更後の確認 IE03 {#c10-i0369}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

変更後の確認では ポリシー・検査エンジン の エージェント変更 を主操作として IE03 を判定します。反映値と残存値への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE03 に残します。変更後の確認を補助する 検査状態 では LastResponse を補助値として IE03 へ保存します。主判定の変更後の確認ではポリシー・検査エンジンの エージェント変更 から InspectionEngine を読み IE03 へ残します。証跡照合の変更後の確認ではポリシー・検査エンジンの InspectionEngine と LastResponse を IE03 に保存します。記録対応の変更後の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE03 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 変更後の確認 IE03の設定や表示を読む前に役割を確認します。S-TAP監視 KTAP Installed 0004ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは巡回で監視エージェを証跡に残し・監視エージェントの監視エージェント状態と取得時刻を記録し。
    - B. 状態を読み取るための働きは保守で照会文動詞集を証跡に残し・データベース User Nameの照会文動詞集計と取得時刻を。
    - C. 状態を読み取るための働きは変更確認でエージェントを証跡に残し・Inspection Engineでエージェント変更から。 ✅
    - D. 状態を読み取るための働きはCentraでノード割当を証跡に残し・処理ID・状態・開始終了時刻・Data Sources。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能エージ・InsでCの記述「Inspection Engineでエージェント変更から」に対応する項目は変更後の確認 IE03（Ins・エージ・変更確）です。照合エージ・変更確に関するポリシー・検査エンジンの仕様は「Inspection Engineでエージェント変更から」で、確認対象はエージ・変更確・Insです。比較検査エ・変更確でA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はIns・変更確・エージです。運用変更確・InsでB:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸はエージ・検査エ・変更確です。仕様エージ・変更確でD:の対象絞り込み ノード割当は「処理ID、状態、開始終了時刻、Data」を述べるため、正答側の照合軸は変更確・Ins・エージです。用語エージ・変更確という用語は「Inspection Engineでエージェント変更」を指し、照合する値と誤認リスクの組合せは検査エ・エージ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 変更後の確認 IE03**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて変更結果を検証し、IE03のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE03のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db03.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE03の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db03.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE03のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE03 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Host が画面・出力に表示されること
    ② ステップ2 の S-TAP が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 容量余力の確認 IE16 {#c10-i0370}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

容量余力の確認では ポリシー・検査エンジン の 検査状態 を主操作として IE16 を判定します。使用量と警告しきい値への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE16 に残します。容量余力の確認を補助する ポリシー変更 では Policy を補助値として IE16 へ保存します。主判定の容量余力の確認ではポリシー・検査エンジンの 検査状態 から LastResponse を読み IE16 へ残します。証跡照合の容量余力の確認ではポリシー・検査エンジンの LastResponse と Policy を IE16 に保存します。記録対応の容量余力の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE16 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 容量余力の確認 IE16の技術的な意味を資料で確認するとき、S-TAP監視 Last Response 0052との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は監視エージェントのカーネル監視有無と取得時刻を記録し・ローカル通信制御監視の未確認を防ぐである。保守操作で監査欄を保存するときはローカル通信制御監視の未確認を防ぐ。
    - B. 管理対象との関係を表す説明はInspection Engineで検査状態から LastResponse を読みである。検査状態からLastResponseときはInspectionを防ぐ。 ✅
    - C. 管理対象との関係を表す説明は照会文 Verbのジョブキューと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。
    - D. 管理対象との関係を表す説明はApplication Accessのユーザー有効化と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能検査状・InsでBの記述「Inspection Engineで検査状態から」に対応する項目は容量余力の確認 IE16（Ins・検査状・容量余）です。照合検査状・容量余に関するポリシー・検査エンジンの仕様は「Inspection Engineで検査状態から」で、確認対象は検査状・容量余・Insです。比較検査エ・容量余でA:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はIns・容量余・検査状です。項目検査状・容量余でC:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はIns・検査エ・検査状です。仕様検査状・容量余でD:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は容量余・Ins・検査状です。用語検査状・容量余という用語は「Inspection Engineで検査状態から」を指し、照合する値と誤認リスクの組合せは検査エ・検査状・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 容量余力の確認 IE16**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて容量枯渇を予防し、IE16のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE16と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE16の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db16.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE16の対応を確認します。使用量と警告しきい値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE16のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE16 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE16の対応を確認します。使用量と警告しきい値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE16のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db16.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE16の対応を確認します。使用量と警告しきい値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の S-TAP が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Host が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 引継ぎ記録 IE09 {#c10-i0371}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

引継ぎ記録では ポリシー・検査エンジン の エージェント変更 を主操作として IE09 を判定します。次担当者が追跡できる証跡への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE09 に残します。引継ぎ記録を補助する 検査状態 では LastResponse を補助値として IE09 へ保存します。主判定の引継ぎ記録ではポリシー・検査エンジンの エージェント変更 から InspectionEngine を読み IE09 へ残します。証跡照合の引継ぎ記録ではポリシー・検査エンジンの InspectionEngine と LastResponse を IE09 に保存します。記録対応の引継ぎ記録ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE09 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 引継ぎ記録 IE09を保守記録に説明する必要があります。ロールと権限 Application Access 0030と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は変更確認操作で採取欄を棚卸することでユーザー有効を確認し・ディレクトリー取込対象の誤りを防ぐ。
    - B. 運用時に利用する技術的役割は点検操作で判定欄を記録することでジョブキューを確認し・照会文動詞集計の期間誤りを防ぐ。
    - C. 運用時に利用する技術的役割は証跡採取で停止時刻を確認することで停止時刻を確認し・停止時刻の誤読を防ぐ。Approved TAP Clients 証跡採取 停止時刻固有の属性も確認対象に含める。
    - D. 運用時に利用する技術的役割はエージェント変更からInspectionことでエージェントを確認し・Inspectionを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能エージ・InsでDの記述「Inspection Engineでエージェント変更から」に対応する項目は引継ぎ記録 IE09（Ins・エージ・ポリシ）です。照合エージ・ポリシに関するポリシー・検査エンジンの仕様は「Inspection Engineでエージェント変更から」で、確認対象はエージ・ポリシ・Insです。比較検査エ・ポリシでA:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はIns・ポリシ・エージです。運用ポリシ・InsでB:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はエージ・検査エ・ポリシです。項目エージ・ポリシでC:の証跡採取 停止時刻は「接続を許可された S-TAP」を述べるため、正答側の照合軸はIns・検査エ・エージです。用語エージ・ポリシという用語は「Inspection Engineでエージェント変更」を指し、照合する値と誤認リスクの組合せは検査エ・エージ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 引継ぎ記録 IE09**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて再現可能な記録を作成し、IE09のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE09のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db09.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE09の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db09.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE09のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE09 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Host が画面・出力に表示されること
    ② ステップ2 の S-TAP が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 復旧後の確認 IE06 {#c10-i0372}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

復旧後の確認では ポリシー・検査エンジン の エージェント変更 を主操作として IE06 を判定します。再発していないことを示す値への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE06 に残します。復旧後の確認を補助する 検査状態 では LastResponse を補助値として IE06 へ保存します。主判定の復旧後の確認ではポリシー・検査エンジンの エージェント変更 から InspectionEngine を読み IE06 へ残します。証跡照合の復旧後の確認ではポリシー・検査エンジンの InspectionEngine と LastResponse を IE06 に保存します。記録対応の復旧後の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE06 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 復旧後の確認 IE06の役割を調べています。ロールと権限 Role 0036の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては監査担当者の閲覧範囲不足を避けるため・照合操作で確認欄を採取するしてディレクトリを照合する。ロールと権限 Role 0036固有の属性も確認対象に含める。
    - B. 機能の説明としては過剰ロール付与を避けるため・主操作で出力欄を評価するして表示可能レポを照合する。
    - C. 機能の説明としてはInspectionを避けるため・エージェント変更からInspectionしてエージェントを照合する。 ✅
    - D. 機能の説明としては適用位置の誤読を避けるため・状態確認で適用位置を確認するして適用位置を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能エージ・InsでCの記述「Inspection Engineでエージェント変更から」に対応する項目は復旧後の確認 IE06（Ins・エージ・復旧確）です。照合エージ・復旧確に関するポリシー・検査エンジンの仕様は「Inspection Engineでエージェント変更から」で、確認対象はエージ・復旧確・Insです。比較検査エ・復旧確でA:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸はIns・復旧確・エージです。運用復旧確・InsでB:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はエージ・検査エ・復旧確です。仕様エージ・復旧確でD:の状態確認 適用位置は「S-TAP や外部接続から監査データを受け取」を述べるため、正答側の照合軸は復旧確・Ins・エージです。用語エージ・復旧確という用語は「Inspection Engineでエージェント変更」を指し、照合する値と誤認リスクの組合せは検査エ・エージ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 復旧後の確認 IE06**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて復旧後の安定性を確認し、IE06のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE06のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db06.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE06の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db06.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE06のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE06 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Host が画面・出力に表示されること
    ② ステップ2 の S-TAP が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 復旧準備 IE05 {#c10-i0373}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

復旧準備では ポリシー・検査エンジン の ポリシー変更 を主操作として IE05 を判定します。再開前に必要な整合性への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE05 に残します。復旧準備を補助する エージェント変更 では InspectionEngine を補助値として IE05 へ保存します。主判定の復旧準備ではポリシー・検査エンジンの ポリシー変更 から Policy を読み IE05 へ残します。証跡照合の復旧準備ではポリシー・検査エンジンの Policy と InspectionEngine を IE05 に保存します。記録対応の復旧準備ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE05 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「ポリシー・検査エンジン Inspection Engine 復旧準備 IE05」を「S-TAP監視 S-TAP Version 0058」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は復旧準備でポリシー変更を証跡に残し・Inspection Engineでポリシー変更から。 ✅
    - B. 仕様上の役割は復旧で暗号化表示を証跡に残し・監視エージェントの暗号化表示と取得時刻を記録し。
    - C. 仕様上の役割は確認でカーネル監視を証跡に残し・監視エージェントのカーネル監視有無と取得時刻を記録し。
    - D. 仕様上の役割は計画でユーザー有効を証跡に残し・Application Accessのユーザー有効化と取得時。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ポリシ・InsでAの記述「Inspection Engineでポリシー変更から」に対応する項目は復旧準備 IE05（Ins・ポリシ・復旧準）です。照合ポリシ・復旧準に関するポリシー・検査エンジンの仕様は「Inspection Engineでポリシー変更から Policy」で、確認対象はポリシ・復旧準・Insです。運用復旧準・InsでB:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はポリシ・検査エ・復旧準です。項目ポリシ・復旧準でC:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はIns・検査エ・ポリシです。仕様ポリシ・復旧準でD:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は復旧準・Ins・ポリシです。用語ポリシ・復旧準という用語は「Inspection Engineでポリシー変更から」を指し、照合する値と誤認リスクの組合せは検査エ・ポリシ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 復旧準備 IE05**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて復旧条件を確認し、IE05のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE05のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE05 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE05のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db05.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE05の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db05.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Host が画面・出力に表示されること
    ③ ステップ3 の S-TAP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 性能影響の確認 IE11 {#c10-i0374}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

性能影響の確認では ポリシー・検査エンジン の ポリシー変更 を主操作として IE11 を判定します。処理時間と滞留箇所への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE11 に残します。性能影響の確認を補助する エージェント変更 では InspectionEngine を補助値として IE11 へ保存します。主判定の性能影響の確認ではポリシー・検査エンジンの ポリシー変更 から Policy を読み IE11 へ残します。証跡照合の性能影響の確認ではポリシー・検査エンジンの Policy と InspectionEngine を IE11 に保存します。記録対応の性能影響の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE11 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 性能影響の確認 IE11の設定や表示を読む前に役割を確認します。S-TAP監視 KTAP Installed 0064ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はInspectionを避けるため・ポリシー変更からPolicyを読むしてポリシー変更を照合する。 ✅
    - B. 一次資料が示す主目的はローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するして監視エージェを照合する。
    - C. 一次資料が示す主目的はローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するして承認クライアを照合する。S-TAP監視 DB Server Type 0220固有の属性も確認対象に含める。
    - D. 一次資料が示す主目的は復元前提の誤読を避けるため・承認履歴確認で復元前提を確認するして復元前提を照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ポリシ・InsでAの記述「Inspection Engineでポリシー変更から」に対応する項目は性能影響の確認 IE11（Ins・ポリシ・性能影）です。照合ポリシ・性能影に関するポリシー・検査エンジンの仕様は「Inspection Engineでポリシー変更から Policy」で、確認対象はポリシ・性能影・Insです。運用性能影・InsでB:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はポリシ・検査エ・性能影です。項目ポリシ・性能影でC:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はIns・検査エ・ポリシです。仕様ポリシ・性能影でD:の承認履歴確認 復元前提は「監視対象データベースやサービスを表す」を述べるため、正答側の照合軸は性能影・Ins・ポリシです。用語ポリシ・性能影という用語は「Inspection Engineでポリシー変更から」を指し、照合する値と誤認リスクの組合せは検査エ・ポリシ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 性能影響の確認 IE11**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて負荷と待ちを確認し、IE11のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE11のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE11 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE11のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db11.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE11の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db11.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Host が画面・出力に表示されること
    ③ ステップ3 の S-TAP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 構成監査 IE08 {#c10-i0375}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

構成監査では ポリシー・検査エンジン の ポリシー変更 を主操作として IE08 を判定します。定義値と稼働値の一致への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE08 に残します。構成監査を補助する エージェント変更 では InspectionEngine を補助値として IE08 へ保存します。主判定の構成監査ではポリシー・検査エンジンの ポリシー変更 から Policy を読み IE08 へ残します。証跡照合の構成監査ではポリシー・検査エンジンの Policy と InspectionEngine を IE08 に保存します。記録対応の構成監査ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE08 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 構成監査 IE08の技術的な意味を資料で確認するとき、監査レポート Server IP 0017との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は巡回でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。
    - B. コマンドまたは機能の用途は収集で最終応答を証跡に残し・監視エージェントの最終応答と取得時刻を記録し。
    - C. コマンドまたは機能の用途はデータソースでレビュー結果を証跡に残し・データベース通信を解析し監査レコードを作る処理を障害時切り分。
    - D. コマンドまたは機能の用途は構成監査でポリシー変更を証跡に残し・Inspection Engineでポリシー変更から。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ポリシ・InsでDの記述「Inspection Engineでポリシー変更から」に対応する項目は構成監査 IE08（Ins・ポリシ・構成監）です。照合ポリシ・構成監に関するポリシー・検査エンジンの仕様は「Inspection Engineでポリシー変更から Policy」で、確認対象はポリシ・構成監・Insです。比較検査エ・構成監でA:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸はIns・構成監・ポリシです。運用構成監・InsでB:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はポリシ・検査エ・構成監です。項目ポリシ・構成監でC:の障害時切り分け レビュー結果は「データベース通信を解析し監査レコードを作る処」を述べるため、正答側の照合軸はIns・検査エ・ポリシです。用語ポリシ・構成監という用語は「Inspection Engineでポリシー変更から」を指し、照合する値と誤認リスクの組合せは検査エ・ポリシ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 構成監査 IE08**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて構成差分を監査し、IE08のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE08のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE08 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE08のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db08.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE08の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db08.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Host が画面・出力に表示されること
    ③ ステップ3 の S-TAP が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 権限境界の確認 IE12 {#c10-i0376}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

権限境界の確認では ポリシー・検査エンジン の エージェント変更 を主操作として IE12 を判定します。参照操作と変更操作の分離への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE12 に残します。権限境界の確認を補助する 検査状態 では LastResponse を補助値として IE12 へ保存します。主判定の権限境界の確認ではポリシー・検査エンジンの エージェント変更 から InspectionEngine を読み IE12 へ残します。証跡照合の権限境界の確認ではポリシー・検査エンジンの InspectionEngine と LastResponse を IE12 に保存します。記録対応の権限境界の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE12 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 権限境界の確認 IE12を同一分類の監査レポート DB User Name 0014と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はデータベース User Nameの照会文動詞集計と取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。監査レポート DB User Name 0014固有の属性も確認対象に含める。
    - B. 構成を確認する際の意味はClient IPの監査タスクと取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。
    - C. 構成を確認する際の意味は監視エージェントの監視エージェント状態と取得時刻を記録し・最終応答停止の見落としを防ぐである。確認操作で状態欄を整理するときは最終応答停止の見落としを防ぐ。
    - D. 構成を確認する際の意味はInspection Engineでエージェント変更から InspectionEngine を読みである。エージェント変更からInspectiときはInspectionを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能エージ・InsでDの記述「Inspection Engineでエージェント変更から」に対応する項目は権限境界の確認 IE12（Ins・エージ・権限境）です。照合エージ・権限境に関するポリシー・検査エンジンの仕様は「Inspection Engineでエージェント変更から」で、確認対象はエージ・権限境・Insです。比較検査エ・権限境でA:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸はIns・権限境・エージです。運用権限境・InsでB:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸はエージ・検査エ・権限境です。項目エージ・権限境でC:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はIns・検査エ・エージです。用語エージ・権限境という用語は「Inspection Engineでエージェント変更」を指し、照合する値と誤認リスクの組合せは検査エ・エージ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 権限境界の確認 IE12**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて実行権限を点検し、IE12のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE12のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db12.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE12の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db12.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE12のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE12 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Host が画面・出力に表示されること
    ② ステップ2 の S-TAP が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 異常終了後の確認 IE19 {#c10-i0377}
*分類: ポリシー・検査エンジン*  ・  難易度: 上級

異常終了後の確認では ポリシー・検査エンジン の 検査状態 を主操作として IE19 を判定します。未完了処理と再実行条件への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE19 に残します。異常終了後の確認を補助する ポリシー変更 では Policy を補助値として IE19 へ保存します。主判定の異常終了後の確認ではポリシー・検査エンジンの 検査状態 から LastResponse を読み IE19 へ残します。証跡照合の異常終了後の確認ではポリシー・検査エンジンの LastResponse と Policy を IE19 に保存します。記録対応の異常終了後の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE19 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 異常終了後の確認 IE19の設定や表示を読む前に役割を確認します。アプライアンス健全性 Appliance Monitoring ログとの照合ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはInspection Engineで検査状態から LastResponse を読みである。検査状態からLastResponseときはInspectionを防ぐ。 ✅
    - B. 対象資源に対する働きはAppliance Monitoriで監視プロセスから Appliance を読み・Appliance とである。監視プロセスからApplianceをときはディスク逼迫中に検査データ流を防ぐ。
    - C. 対象資源に対する働きはデータベース User Nameの照会文動詞集計と取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。
    - D. 対象資源に対する働きは複数 collector の監査情報を集約しレポートへ渡す装置を証跡採取として確認する。証跡採取で取得間隔を確認するときは取得間隔の誤読を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能検査状・InsでAの記述「Inspection Engineで検査状態から」に対応する項目は異常終了後の確認 IE19（Ins・検査状・異常終）です。照合検査状・異常終に関するポリシー・検査エンジンの仕様は「Inspection Engineで検査状態から」で、確認対象は検査状・異常終・Insです。運用異常終・InsでB:のログとの照合 APP07は「Appliance Monitoriで監視プ」を述べるため、正答側の照合軸は検査状・検査エ・異常終です。項目検査状・異常終でC:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸はIns・検査エ・検査状です。仕様検査状・異常終でD:の証跡採取 取得間隔は「複数 collector の監査情報を集約し」を述べるため、正答側の照合軸は異常終・Ins・検査状です。用語検査状・異常終という用語は「Inspection Engineで検査状態から」を指し、照合する値と誤認リスクの組合せは検査エ・検査状・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 異常終了後の確認 IE19**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて異常終了の影響を限定し、IE19のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE19と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE19の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db19.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE19の対応を確認します。未完了処理と再実行条件を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE19のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE19 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE19の対応を確認します。未完了処理と再実行条件を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE19のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db19.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE19の対応を確認します。未完了処理と再実行条件を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の S-TAP が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Host が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 監査証跡の保存 IE18 {#c10-i0378}
*分類: ポリシー・検査エンジン*  ・  難易度: 上級

監査証跡の保存では ポリシー・検査エンジン の エージェント変更 を主操作として IE18 を判定します。実行者と結果の対応への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE18 に残します。監査証跡の保存を補助する 検査状態 では LastResponse を補助値として IE18 へ保存します。主判定の監査証跡の保存ではポリシー・検査エンジンの エージェント変更 から InspectionEngine を読み IE18 へ残します。証跡照合の監査証跡の保存ではポリシー・検査エンジンの InspectionEngine と LastResponse を IE18 に保存します。記録対応の監査証跡の保存ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE18 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 監査証跡の保存 IE18に関する障害切り分けの前提を確認しています。アプライアンス健全性 Appliance Monitoring ログとの照合の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはディスク逼迫中に検査データ流入をを避けるため・監視プロセスからApplianceを読むして監視プロセスを照合する。
    - B. 機能の説明としては最終応答停止の見落としを避けるため・確認操作で状態欄を整理するして最終応答を照合する。
    - C. 機能の説明としてはInspectionを避けるため・エージェント変更からInspectionしてエージェントを照合する。 ✅
    - D. 機能の説明としては取得間隔の誤読を避けるため・証跡採取で取得間隔を確認するして取得間隔を照合する。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能エージ・InsでCの記述「Inspection Engineでエージェント変更から」に対応する項目は監査証跡の保存 IE18（Ins・エージ・監査証）です。照合エージ・監査証に関するポリシー・検査エンジンの仕様は「Inspection Engineでエージェント変更から」で、確認対象はエージ・監査証・Insです。比較検査エ・監査証でA:のログとの照合 APP07は「Appliance Monitoriで監視プ」を述べるため、正答側の照合軸はIns・監査証・エージです。運用監査証・InsでB:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はエージ・検査エ・監査証です。仕様エージ・監査証でD:の証跡採取 取得間隔は「複数 collector の監査情報を集約し」を述べるため、正答側の照合軸は監査証・Ins・エージです。用語エージ・監査証という用語は「Inspection Engineでエージェント変更」を指し、照合する値と誤認リスクの組合せは検査エ・エージ・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 監査証跡の保存 IE18**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて監査可能な証跡を保存し、IE18のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE18と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE18のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db18.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE18の対応を確認します。実行者と結果の対応を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE18の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db18.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE18の対応を確認します。実行者と結果の対応を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE18のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE18 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE18の対応を確認します。実行者と結果の対応を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Host が画面・出力に表示されること
    ② ステップ2 の S-TAP が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 通常状態の確認 IE01 {#c10-i0379}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

通常状態の確認では ポリシー・検査エンジン の 検査状態 を主操作として IE01 を判定します。基準値と現在値の差への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE01 に残します。通常状態の確認を補助する ポリシー変更 では Policy を補助値として IE01 へ保存します。主判定の通常状態の確認ではポリシー・検査エンジンの 検査状態 から LastResponse を読み IE01 へ残します。証跡照合の通常状態の確認ではポリシー・検査エンジンの LastResponse と Policy を IE01 に保存します。記録対応の通常状態の確認ではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE01 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 通常状態の確認 IE01を保守記録に説明する必要があります。ポリシー・検査エンジン Inspection Engine 障害切り分け IE04と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はポリシーで検査状態を証跡に残し・Inspection Engineで検査状態から。
    - B. 保守作業で参照する機能は通常状態確認で検査状態を証跡に残し・Inspection Engineで検査状態から。 ✅
    - C. 保守作業で参照する機能は確認で表示可能レポを証跡に残し・Permissionの表示可能レポートと取得時刻を記録し。
    - D. 保守作業で参照する機能は計画で承認クライアを証跡に残し・監視エージェントの承認クライアントと取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能検査状・InsでBの記述「Inspection Engineで検査状態から」に対応する項目は通常状態の確認 IE01（Ins・検査状・通常状）です。照合検査状・通常状に関するポリシー・検査エンジンの仕様は「Inspection Engineで検査状態から」で、確認対象は検査状・通常状・Insです。比較検査エ・通常状でA:の障害切り分け IE04は「Inspection Engineで検査状態」を述べるため、正答側の照合軸はIns・通常状・検査状です。項目検査状・通常状でC:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はIns・検査エ・検査状です。仕様検査状・通常状でD:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は通常状・Ins・検査状です。用語検査状・通常状という用語は「Inspection Engineで検査状態から」を指し、照合する値と誤認リスクの組合せは検査エ・検査状・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 通常状態の確認 IE01**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて通常状態を確定し、IE01のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE01の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db01.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE01のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE01 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE01のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db01.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の S-TAP が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Host が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### ポリシー・検査エンジン Inspection Engine 障害切り分け IE04 {#c10-i0380}
*分類: ポリシー・検査エンジン*  ・  難易度: 中級

障害切り分けでは ポリシー・検査エンジン の 検査状態 を主操作として IE04 を判定します。最初に失敗した処理への注意として「Inspection Engine不一致をS-TAP停止だけと判断する危険があります」を IE04 に残します。障害切り分けを補助する ポリシー変更 では Policy を補助値として IE04 へ保存します。主判定の障害切り分けではポリシー・検査エンジンの 検査状態 から LastResponse を読み IE04 へ残します。証跡照合の障害切り分けではポリシー・検査エンジンの LastResponse と Policy を IE04 に保存します。記録対応の障害切り分けではポリシー・検査エンジンの DB TypeとLast Response の証跡へ IE04 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** ポリシー・検査エンジン Inspection Engine 障害切り分け IE04を同一分類のロールと権限 Application Access 0060と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はApplication Accessのユーザー有効化と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。
    - B. 管理対象との関係を表す説明は監視エージェントの暗号化表示と取得時刻を記録し・ローカル通信制御監視の未確認を防ぐである。保守操作で監査欄を保存するときはローカル通信制御監視の未確認を防ぐ。
    - C. 管理対象との関係を表す説明はInspection Engineで検査状態から LastResponse を読みである。検査状態からLastResponseときはInspectionを防ぐ。 ✅
    - D. 管理対象との関係を表す説明はLogin Nameのロール割当と取得時刻を記録し・ディレクトリー取込対象の誤りを防ぐである。変更確認操作で採取欄を棚卸するときはディレクトリー取込対象の誤りを防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能検査状・InsでCの記述「Inspection Engineで検査状態から」に対応する項目は障害切り分け IE04（Ins・検査状・ポリシ）です。照合検査状・ポリシに関するポリシー・検査エンジンの仕様は「Inspection Engineで検査状態から」で、確認対象は検査状・ポリシ・Insです。比較検査エ・ポリシでA:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はIns・ポリシ・検査状です。運用ポリシ・InsでB:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は検査状・検査エ・ポリシです。仕様検査状・ポリシでD:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸はポリシ・Ins・検査状です。用語検査状・ポリシという用語は「Inspection Engineで検査状態から」を指し、照合する値と誤認リスクの組合せは検査エ・検査状・Insです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **ポリシー・検査エンジン Inspection Engine 障害切り分け IE04**

    - 検証目的: ポリシー・検査エンジンのInspection Engineについて障害範囲を限定し、IE04のDB TypeとLast Responseを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象IE04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection engine statusを指定し、IE04の検査状態を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection engine status
    → Enter を押す
    ```

    画面・出力:
    ```text
    S-TAP Host | DB Type | DB Executable | Last Response | KTAP
    db04.example | Oracle | oracle | 2026-07-15 13:10 | Installed
    ```

    画面・出力にあるS-TAPを読み、DB TypeとLast Responseと対象IE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Policy Related Changesを指定し、IE04のポリシー変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Policy Related Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Date | User | Policy | Operation
    2026-07-15 13:12 | secadmin | IE04 | INSTALL
    ```

    画面・出力にあるPolicyを読み、DB TypeとLast Responseと対象IE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xのポリシー・検査エンジンを確認する入力画面です。COMMAND入力口へReports > Inspection Engines and S-TAP Changesを指定し、IE04のエージェント変更を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Reports > Inspection Engines and S-TAP Changes
    → Enter を押す
    ```

    画面・出力:
    ```text
    Host | Object | Change | Date
    db04.example | Inspection Engine | UPDATE | 2026-07-15 13:13
    ```

    画面・出力にあるHostを読み、DB TypeとLast Responseと対象IE04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の S-TAP が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Host が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring




## IBM Guardium Data Protection 12.x > レポート

### 監査レポート Audit Task Status 0008 {#c10-i0381}
*分類: レポート*  ・  難易度: 初級

黄I巡回0009ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黄I巡回0009です。黄I巡回0009は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録黄I巡回0009です。黄I巡回0009ではユーザー活動と取得時刻を採取票黄I巡回0009へ残します。黄I巡回0009では対象データソースの取り違えを避けるため補助資料も照合する判断黄I巡回0009です。黄I巡回0009の用語整理では監査レポートの対象値を実在出力で整理する記録黄I巡回0009です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0008を同一分類のS-TAP監視 KTAP Installed 0019と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は採取操作で照合欄を点検することで監視エージェを確認し・カーネル監視導入状態の誤読を防ぐ。
    - B. 構成を確認する際の意味は保守操作で監査欄を保存することで暗号化表示を確認し・ローカル通信制御監視の未確認を防ぐ。
    - C. 構成を確認する際の意味は調査操作で保守欄を引き継ぎすることでユーザー活動を確認し・対象データソースの取り違えを防ぐ。 ✅
    - D. 構成を確認する際の意味は変更確認で変更後の確認を確認することで変更後の確認を確認し・managed unitからを防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 巡回対象ユーザー活でCの記述「Audit Task Statusのユーザー活動と取得時刻を記録し」に対応する項目はTask Status（Audit・巡回・ユーザ・対象デー）です。巡回時のユーザー活に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はAudi・巡回・ユーザ・対象デーです。監視・巡回・監視エーのA:は「S-TAPのS-TAP状態と取得時刻を記録し」を述べ、対象はKTAP Installed（監視エージ・巡回・監視エ・カーネル）です。登録対象暗号化表示のB:は「S-TAPの暗号化表示と取得時刻を記録し」を述べ、対象はS-TAP Version（監視エージ・登録・暗号化・ローカル）です。変更後の確を変更確認のD:は「Central ManagerでCentral」を述べ、対象は変更後の確認 CM03（Centr・変更確・変更後・mana）です。ユーザー活を巡回という用語は「Audit Task Statusのユーザー活動と取」を指し、Task Status（Audit・巡回・ユーザ・対象デー）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0008**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0008について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.18
    Server IP 198.51.100.28
    Count 18
    確認コード GDP12DD0008A
    ```

    画面・出力には GDP12DD0008A が表示され、監査レポート Audit Task Status 0008 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0008
    Process Type Report
    Status completed
    確認コード GDP12DD0008B
    ```

    画面・出力には GDP12DD0008B が表示され、監査レポート Audit Task Status 0008 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0008C
    ```

    画面・出力には GDP12DD0008C が表示され、監査レポート Audit Task Status 0008 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0008A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0008B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0008C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0023 {#c10-i0382}
*分類: レポート*  ・  難易度: 中級

藍D棚卸0024ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藍D棚卸0024です。藍D棚卸0024は監査レポートの表示操作で監査レポートの対象欄を追跡する記録藍D棚卸0024です。藍D棚卸0024ではユーザー活動と取得時刻を採取票藍D棚卸0024へ残します。藍D棚卸0024ではジョブ失敗の見落としを避けるため補助資料も照合する判断藍D棚卸0024です。藍D棚卸0024の用語整理では監査レポートの対象値を実在出力で照合する記録藍D棚卸0024です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0023の設定や表示を読む前に役割を確認します。S-TAP監視 KTAP Installed 0034ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは棚卸で監視エージェを証跡に残し・S-TAPのS-TAP状態と取得時刻を記録し。
    - B. 状態を読み取るための働きは抑止で暗号化表示を証跡に残し・S-TAPの暗号化表示と取得時刻を記録し。
    - C. 状態を読み取るための働きは棚卸でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。 ✅
    - D. 状態を読み取るための働きは通常状態確認で確認では中央を証跡に残し・Central Managerで通常状態の確認では中央管理サ。

    正解: **C** ／ 難易度: 中級

    **解説:** 棚卸対象ユーザー活でCの記述「Audit Task Statusのユーザー活動と取得時刻を記録し」に対応する項目はTask Status（Audit・棚卸・ユーザ・ジョブ失）です。棚卸時のユーザー活に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はAudi・棚卸・ユーザ・ジョブ失です。監視・棚卸・監視エーのA:は「S-TAPのS-TAP状態と取得時刻を記録し」を述べ、対象はKTAP Installed（監視エージ・棚卸・監視エ・最終応答）です。抑止対象暗号化表示のB:は「S-TAPの暗号化表示と取得時刻を記録し」を述べ、対象はS-TAP Version（監視エージ・抑止・暗号化・カーネル）です。確認では中を通常状態確のD:は「Central Managerで通常状態の確認では中央管理サーバーの」を述べ、対象は通常状態の確認 CM01（Centr・通常状・確認で・mana）です。ユーザー活を棚卸という用語は「Audit Task Statusのユーザー活動と取」を指し、Task Status（Audit・棚卸・ユーザ・ジョブ失）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0023**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0023について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.33
    Server IP 198.51.100.43
    Count 33
    確認コード GDP12DD0023A
    ```

    画面・出力には GDP12DD0023A が表示され、監査レポート Audit Task Status 0023 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0023
    Process Type Report
    Status completed
    確認コード GDP12DD0023B
    ```

    画面・出力には GDP12DD0023B が表示され、監査レポート Audit Task Status 0023 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0023C
    ```

    画面・出力には GDP12DD0023C が表示され、監査レポート Audit Task Status 0023 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0023A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0023B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0023C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0038 {#c10-i0383}
*分類: レポート*  ・  難易度: 中級

黒S棚卸0039ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黒S棚卸0039です。黒S棚卸0039は監査レポートの点検操作で監査レポートの判定欄を記録する記録黒S棚卸0039です。黒S棚卸0039ではユーザー活動と取得時刻を採取票黒S棚卸0039へ残します。黒S棚卸0039ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断黒S棚卸0039です。黒S棚卸0039の用語整理では監査レポートの対象値を実在出力で保管する記録黒S棚卸0039です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0038に関する障害切り分けの前提を確認しています。監査レポート Client IP 0050の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては点検操作で判定欄を記録することで監査タスクを確認し・照会文動詞集計の期間誤りを防ぐ。
    - B. 機能の説明としては変更確認操作で採取欄を棚卸することで表示可能レポを確認し・ディレクトリー取込対象の誤りを防ぐ。
    - C. 機能の説明としては証跡採取で活動ログを確認することで活動ログを確認し・活動ログの誤読を防ぐ。
    - D. 機能の説明としては点検操作で判定欄を記録することでユーザー活動を確認し・照会文動詞集計の期間誤りを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 棚卸対象ユーザー活でDの記述「Audit Task Statusのユーザー活動と取得時刻を記録し」に対応する項目はTask Status（Audit・棚卸・ユーザ・照会文動）です。棚卸時のユーザー活に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はAudi・棚卸・ユーザ・照会文動です。Cl・復旧・監査タスのA:は「Client IPの監査タスクと取得時刻を記録し」を述べ、対象はClient IP（Clien・復旧・監査タ・照会文動）です。保護対象表示可能レのB:は「Permissionの表示可能レポートと取得時刻を記録し」を述べ、対象はロールと権限 Permission（Permi・保護・表示可・ディレク）です。証跡採取時の活動ログのC:は「管理対象システムの構成と配布を統制する管理点を証跡採取として確認する」を述べ、対象は証跡採取 活動ログ（Centr・証跡採・活動ロ・活動ログ）です。ユーザー活を棚卸という用語は「Audit Task Statusのユーザー活動と取」を指し、Task Status（Audit・棚卸・ユーザ・照会文動）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0038**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0038について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.48
    Server IP 198.51.100.58
    Count 48
    確認コード GDP12DD0038A
    ```

    画面・出力には GDP12DD0038A が表示され、監査レポート Audit Task Status 0038 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0038
    Process Type Report
    Status completed
    確認コード GDP12DD0038B
    ```

    画面・出力には GDP12DD0038B が表示され、監査レポート Audit Task Status 0038 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0038C
    ```

    画面・出力には GDP12DD0038C が表示され、監査レポート Audit Task Status 0038 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0038A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0038B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0038C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0053 {#c10-i0384}
*分類: レポート*  ・  難易度: 中級

灰N復旧0054ではIBM Guardium Data Protection 12.x の レポートを扱う採取票灰N復旧0054です。灰N復旧0054は監査レポートの復旧操作で監査レポートの点検欄を確認する記録灰N復旧0054です。灰N復旧0054ではユーザー活動と取得時刻を採取票灰N復旧0054へ残します。灰N復旧0054では監査タスク未レビューを避けるため補助資料も照合する判断灰N復旧0054です。灰N復旧0054の用語整理では監査レポートの対象値を実在出力で点検する記録灰N復旧0054です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0053を保守記録に説明する必要があります。S-TAP監視 KTAP Installed 0109と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は記録操作で証跡欄を照合することで監視エージェを確認し・未承認監視エージェント接続を防ぐ。
    - B. 運用時に利用する技術的役割は復旧操作で点検欄を確認することでユーザー活動を確認し・監査タスク未レビューを防ぐ。 ✅
    - C. 運用時に利用する技術的役割は変更確認操作で採取欄を棚卸することでロール割当を確認し・ディレクトリー取込対象の誤りを防ぐ。
    - D. 運用時に利用する技術的役割はCentraで引継ぎ記録を確認することで引継ぎ記録を確認し・managed unitからを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ユーザ・監査タでBの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・復旧）です。照合ユーザ・復旧に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・復旧・監査タです。比較監査レ・復旧でA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はAud・復旧・ユーザです。項目ユーザ・復旧でC:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は監査タ・監査レ・ユーザです。仕様ユーザ・復旧でD:の引継ぎ記録 CM09は「Central ManagerでCentra」を述べるため、正答側の照合軸は復旧・監査タ・ユーザです。用語ユーザ・復旧という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0053**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0053について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.63
    Server IP 198.51.100.73
    Count 63
    確認コード GDP12DD0053A
    ```

    画面・出力には GDP12DD0053A が表示され、監査レポート Audit Task Status 0053 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0053
    Process Type Report
    Status completed
    確認コード GDP12DD0053B
    ```

    画面・出力には GDP12DD0053B が表示され、監査レポート Audit Task Status 0053 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0053C
    ```

    画面・出力には GDP12DD0053C が表示され、監査レポート Audit Task Status 0053 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0053A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0053B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0053C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0068 {#c10-i0385}
*分類: レポート*  ・  難易度: 中級

黄I監査0069ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黄I監査0069です。黄I監査0069は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録黄I監査0069です。黄I監査0069ではユーザー活動と取得時刻を採取票黄I監査0069へ残します。黄I監査0069では対象データソースの取り違えを避けるため補助資料も照合する判断黄I監査0069です。黄I監査0069の用語整理では監査レポートの対象値を実在出力で整理する記録黄I監査0069です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0068の技術的な意味を資料で確認するとき、S-TAP監視 S-TAP Version 0118との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は最終応答停止の見落としを避けるため・確認操作で状態欄を整理するして暗号化表示を照合する。
    - B. 構成を確認する際の意味は最終応答停止の見落としを避けるため・確認操作で状態欄を整理するして監視エージェを照合する。
    - C. 構成を確認する際の意味は廃止サーバーの参照を残して監査対を避けるため・変更履歴からOperationを読むして変更履歴を照合する。
    - D. 構成を確認する際の意味は対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてユーザー活動を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ユーザ・対象デでDの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・監査）です。照合ユーザ・監査に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・監査・対象デです。比較監査レ・監査でA:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はAud・監査・ユーザです。運用監査・AudでB:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はユーザ・監査レ・監査です。項目ユーザ・監査でC:の権限境界の確認 DSRC12は「Guardiumで変更履歴から」を述べるため、正答側の照合軸は対象デ・監査レ・ユーザです。用語ユーザ・監査という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0068**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0068について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.78
    Server IP 198.51.100.28
    Count 78
    確認コード GDP12DD0068A
    ```

    画面・出力には GDP12DD0068A が表示され、監査レポート Audit Task Status 0068 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0068
    Process Type Report
    Status completed
    確認コード GDP12DD0068B
    ```

    画面・出力には GDP12DD0068B が表示され、監査レポート Audit Task Status 0068 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0068C
    ```

    画面・出力には GDP12DD0068C が表示され、監査レポート Audit Task Status 0068 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0068A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0068B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0068C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0083 {#c10-i0386}
*分類: レポート*  ・  難易度: 中級

藍D変更0084ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藍D変更0084です。藍D変更0084は監査レポートの表示操作で監査レポートの対象欄を追跡する記録藍D変更0084です。藍D変更0084ではユーザー活動と取得時刻を採取票藍D変更0084へ残します。藍D変更0084ではジョブ失敗の見落としを避けるため補助資料も照合する判断藍D変更0084です。藍D変更0084の用語整理では監査レポートの対象値を実在出力で照合する記録藍D変更0084です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0083について構成や状態を確認します。S-TAP監視 S-TAP Host 0121ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは表示操作で対象欄を追跡することでユーザー活動を確認し・ジョブ失敗の見落としを防ぐ。 ✅
    - B. 状態を読み取るための働きは記録操作で証跡欄を照合することで最終応答を確認し・未承認監視エージェント接続を防ぐ。
    - C. 状態を読み取るための働きは変更確認操作で採取欄を棚卸することでGuardAを確認し・ディレクトリー取込対象の誤りを防ぐ。
    - D. 状態を読み取るための働きは再始動確認で再始動後の確を確認することで再始動後の確を確認し・managed unitからを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ユーザ・ジョブでAの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・変更）です。照合ユーザ・変更に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・変更・ジョブです。運用変更・AudでB:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はユーザ・監査レ・変更です。項目ユーザ・変更でC:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸はジョブ・監査レ・ユーザです。仕様ユーザ・変更でD:の再始動後の確認 CM15は「Central ManagerでCentra」を述べるため、正答側の照合軸は変更・ジョブ・ユーザです。用語ユーザ・変更という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0083**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0083について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.13
    Server IP 198.51.100.43
    Count 93
    確認コード GDP12DD0083A
    ```

    画面・出力には GDP12DD0083A が表示され、監査レポート Audit Task Status 0083 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0083
    Process Type Report
    Status completed
    確認コード GDP12DD0083B
    ```

    画面・出力には GDP12DD0083B が表示され、監査レポート Audit Task Status 0083 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0083C
    ```

    画面・出力には GDP12DD0083C が表示され、監査レポート Audit Task Status 0083 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0083A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0083B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0083C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0098 {#c10-i0387}
*分類: レポート*  ・  難易度: 中級

黒S変更0099ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黒S変更0099です。黒S変更0099は監査レポートの点検操作で監査レポートの判定欄を記録する記録黒S変更0099です。黒S変更0099ではユーザー活動と取得時刻を採取票黒S変更0099へ残します。黒S変更0099ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断黒S変更0099です。黒S変更0099の用語整理では監査レポートの対象値を実在出力で保管する記録黒S変更0099です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0098の役割を調べています。ロールと権限 Permission 0168の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては切替で表示可能レポを証跡に残し・Permissionの表示可能レポートと取得時刻を記録し。ロールと権限 Permission 0168固有の属性も確認対象に含める。
    - B. 機能の説明としては抑止でジョブキューを証跡に残し・照会文 Verbのジョブキューと取得時刻を記録し。
    - C. 機能の説明としては変更でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。 ✅
    - D. 機能の説明としては代替経路確認で検査状態を証跡に残し・Inspection Engineで検査状態から。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ユーザ・照会文でCの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・変更）です。照合ユーザ・変更に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・変更・照会文です。比較監査レ・変更でA:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はAud・変更・ユーザです。運用変更・AudでB:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸はユーザ・監査レ・変更です。仕様ユーザ・変更でD:の代替経路の確認 IE10は「Inspection Engineで検査状態」を述べるため、正答側の照合軸は変更・照会文・ユーザです。用語ユーザ・変更という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0098**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0098について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.28
    Server IP 198.51.100.58
    Count 108
    確認コード GDP12DD0098A
    ```

    画面・出力には GDP12DD0098A が表示され、監査レポート Audit Task Status 0098 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0098
    Process Type Report
    Status completed
    確認コード GDP12DD0098B
    ```

    画面・出力には GDP12DD0098B が表示され、監査レポート Audit Task Status 0098 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0098C
    ```

    画面・出力には GDP12DD0098C が表示され、監査レポート Audit Task Status 0098 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0098A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0098B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0098C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0113 {#c10-i0388}
*分類: レポート*  ・  難易度: 上級

灰N移行0114ではIBM Guardium Data Protection 12.x の レポートを扱う採取票灰N移行0114です。灰N移行0114は監査レポートの復旧操作で監査レポートの点検欄を確認する記録灰N移行0114です。灰N移行0114ではユーザー活動と取得時刻を採取票灰N移行0114へ残します。灰N移行0114では監査タスク未レビューを避けるため補助資料も照合する判断灰N移行0114です。灰N移行0114の用語整理では監査レポートの対象値を実在出力で点検する記録灰N移行0114です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート Audit Task Status 0113」を「ロールと権限 Application Access 0165」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は過剰ロール付与を避けるため・主操作で出力欄を評価するしてユーザー有効を照合する。
    - B. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するしてユーザー活動を照合する。 ✅
    - C. 運用時に利用する技術的役割はローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するして暗号化表示を照合する。
    - D. 運用時に利用する技術的役割はInspectionを避けるため・ポリシー変更からPolicyを読むしてポリシー変更を照合する。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能ユーザ・監査タでBの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・移行）です。照合ユーザ・移行に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・移行・監査タです。比較監査レ・移行でA:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はAud・移行・ユーザです。項目ユーザ・移行でC:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は監査タ・監査レ・ユーザです。仕様ユーザ・移行でD:の復旧準備 IE05は「Inspection Engineでポリシー」を述べるため、正答側の照合軸は移行・監査タ・ユーザです。用語ユーザ・移行という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0113**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0113について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.43
    Server IP 198.51.100.73
    Count 123
    確認コード GDP12DD0113A
    ```

    画面・出力には GDP12DD0113A が表示され、監査レポート Audit Task Status 0113 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0113
    Process Type Report
    Status completed
    確認コード GDP12DD0113B
    ```

    画面・出力には GDP12DD0113B が表示され、監査レポート Audit Task Status 0113 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0113C
    ```

    画面・出力には GDP12DD0113C が表示され、監査レポート Audit Task Status 0113 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0113A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0113B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0113C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0128 {#c10-i0389}
*分類: レポート*  ・  難易度: 初級

黄I診断0129ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黄I診断0129です。黄I診断0129は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録黄I診断0129です。黄I診断0129ではユーザー活動と取得時刻を採取票黄I診断0129へ残します。黄I診断0129では対象データソースの取り違えを避けるため補助資料も照合する判断黄I診断0129です。黄I診断0129の用語整理では監査レポートの対象値を実在出力で整理する記録黄I診断0129です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0128を同一分類のS-TAP監視 DB Server Type 0175と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は診断でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。 ✅
    - B. 構成を確認する際の意味は切替で承認クライアを証跡に残し・監視エージェントの承認クライアントと取得時刻を記録し。
    - C. 構成を確認する際の意味は承認履歴確認で初期同期を証跡に残し・接続を許可された S-TAP と状態を確認する管理レポートを。
    - D. 構成を確認する際の意味は変更確認でジョブキューを証跡に残し・Appliance Monitoriでジョブキューから。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能ユーザ・対象デでAの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・診断）です。照合ユーザ・診断に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・診断・対象デです。運用診断・AudでB:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はユーザ・監査レ・診断です。項目ユーザ・診断でC:の承認履歴確認 初期同期は「接続を許可された S-TAP」を述べるため、正答側の照合軸は対象デ・監査レ・ユーザです。仕様ユーザ・診断でD:の変更後の確認 APP03は「Appliance Monitoriでジョブ」を述べるため、正答側の照合軸は診断・対象デ・ユーザです。用語ユーザ・診断という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0128**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0128について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.18
    Server IP 198.51.100.28
    Count 18
    確認コード GDP12DD0128A
    ```

    画面・出力には GDP12DD0128A が表示され、監査レポート Audit Task Status 0128 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0128
    Process Type Report
    Status completed
    確認コード GDP12DD0128B
    ```

    画面・出力には GDP12DD0128B が表示され、監査レポート Audit Task Status 0128 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0128C
    ```

    画面・出力には GDP12DD0128C が表示され、監査レポート Audit Task Status 0128 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0128A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0128B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0128C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0143 {#c10-i0390}
*分類: レポート*  ・  難易度: 中級

藍D保守0144ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藍D保守0144です。藍D保守0144は監査レポートの表示操作で監査レポートの対象欄を追跡する記録藍D保守0144です。藍D保守0144ではユーザー活動と取得時刻を採取票藍D保守0144へ残します。藍D保守0144ではジョブ失敗の見落としを避けるため補助資料も照合する判断藍D保守0144です。藍D保守0144の用語整理では監査レポートの対象値を実在出力で照合する記録藍D保守0144です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0143の設定や表示を読む前に役割を確認します。監査レポート DB User Name 0194ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは保守でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。 ✅
    - B. 状態を読み取るための働きは収集で照会文動詞集を証跡に残し・データベース User Nameの照会文動詞集計と取得時刻を。
    - C. 状態を読み取るための働きは復旧手掛かりで復旧手掛かりを証跡に残し・データベース通信を解析し監査レコードを作る処理を対象絞り込み。
    - D. 状態を読み取るための働きは復旧でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ユーザ・ジョブでAの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・保守）です。照合ユーザ・保守に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・保守・ジョブです。運用保守・AudでB:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸はユーザ・監査レ・保守です。項目ユーザ・保守でC:の対象絞り込み 復旧手掛かりは「データベース通信を解析し監査レコードを作る処」を述べるため、正答側の照合軸はジョブ・監査レ・ユーザです。仕様ユーザ・保守でD:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は保守・ジョブ・ユーザです。用語ユーザ・保守という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0143**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0143について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.33
    Server IP 198.51.100.43
    Count 33
    確認コード GDP12DD0143A
    ```

    画面・出力には GDP12DD0143A が表示され、監査レポート Audit Task Status 0143 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0143
    Process Type Report
    Status completed
    確認コード GDP12DD0143B
    ```

    画面・出力には GDP12DD0143B が表示され、監査レポート Audit Task Status 0143 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0143C
    ```

    画面・出力には GDP12DD0143C が表示され、監査レポート Audit Task Status 0143 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0143A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0143B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0143C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0158 {#c10-i0391}
*分類: レポート*  ・  難易度: 中級

黒S保守0159ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黒S保守0159です。黒S保守0159は監査レポートの点検操作で監査レポートの判定欄を記録する記録黒S保守0159です。黒S保守0159ではユーザー活動と取得時刻を採取票黒S保守0159へ残します。黒S保守0159ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断黒S保守0159です。黒S保守0159の用語整理では監査レポートの対象値を実在出力で保管する記録黒S保守0159です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0158に関する障害切り分けの前提を確認しています。ロールと権限 LDAP User 0252の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては照合操作で確認欄を採取することでGuardAを確認し・監査担当者の閲覧範囲不足を防ぐ。
    - B. 機能の説明としては点検操作で判定欄を記録することでユーザー活動を確認し・照会文動詞集計の期間誤りを防ぐ。 ✅
    - C. 機能の説明としては採取操作で照合欄を点検することで承認クライアを確認し・カーネル監視導入状態の誤読を防ぐ。
    - D. 機能の説明としては確認操作で状態欄を整理することで暗号化表示を確認し・最終応答停止の見落としを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ユーザ・照会文でBの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・保守）です。照合ユーザ・保守に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・保守・照会文です。比較監査レ・保守でA:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸はAud・保守・ユーザです。項目ユーザ・保守でC:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は照会文・監査レ・ユーザです。仕様ユーザ・保守でD:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は保守・照会文・ユーザです。用語ユーザ・保守という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0158**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0158について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.48
    Server IP 198.51.100.58
    Count 48
    確認コード GDP12DD0158A
    ```

    画面・出力には GDP12DD0158A が表示され、監査レポート Audit Task Status 0158 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0158
    Process Type Report
    Status completed
    確認コード GDP12DD0158B
    ```

    画面・出力には GDP12DD0158B が表示され、監査レポート Audit Task Status 0158 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0158C
    ```

    画面・出力には GDP12DD0158C が表示され、監査レポート Audit Task Status 0158 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0158A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0158B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0158C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0173 {#c10-i0392}
*分類: レポート*  ・  難易度: 中級

灰N切替0174ではIBM Guardium Data Protection 12.x の レポートを扱う採取票灰N切替0174です。灰N切替0174は監査レポートの復旧操作で監査レポートの点検欄を確認する記録灰N切替0174です。灰N切替0174ではユーザー活動と取得時刻を採取票灰N切替0174へ残します。灰N切替0174では監査タスク未レビューを避けるため補助資料も照合する判断灰N切替0174です。灰N切替0174の用語整理では監査レポートの対象値を実在出力で点検する記録灰N切替0174です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0173を保守記録に説明する必要があります。監査レポート Server IP 0242と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は点検操作で判定欄を記録することでデータソースを確認し・照会文動詞集計の期間誤りを防ぐ。
    - B. 運用時に利用する技術的役割は復旧操作で点検欄を確認することでユーザー活動を確認し・監査タスク未レビューを防ぐ。 ✅
    - C. 運用時に利用する技術的役割は状態確認で適用位置を確認することで適用位置を確認し・適用位置の誤読を防ぐ。
    - D. 運用時に利用する技術的役割は記録操作で証跡欄を照合することで暗号化表示を確認し・未承認監視エージェント接続を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ユーザ・監査タでBの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・切替）です。照合ユーザ・切替に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・切替・監査タです。比較監査レ・切替でA:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸はAud・切替・ユーザです。項目ユーザ・切替でC:の状態確認 適用位置は「S-TAP や外部接続から監査データを受け取」を述べるため、正答側の照合軸は監査タ・監査レ・ユーザです。仕様ユーザ・切替でD:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は切替・監査タ・ユーザです。用語ユーザ・切替という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0173**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0173について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.63
    Server IP 198.51.100.73
    Count 63
    確認コード GDP12DD0173A
    ```

    画面・出力には GDP12DD0173A が表示され、監査レポート Audit Task Status 0173 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0173
    Process Type Report
    Status completed
    確認コード GDP12DD0173B
    ```

    画面・出力には GDP12DD0173B が表示され、監査レポート Audit Task Status 0173 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0173C
    ```

    画面・出力には GDP12DD0173C が表示され、監査レポート Audit Task Status 0173 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0173A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0173B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0173C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0188 {#c10-i0393}
*分類: レポート*  ・  難易度: 中級

黄I収集0189ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黄I収集0189です。黄I収集0189は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録黄I収集0189です。黄I収集0189ではユーザー活動と取得時刻を採取票黄I収集0189へ残します。黄I収集0189では対象データソースの取り違えを避けるため補助資料も照合する判断黄I収集0189です。黄I収集0189の用語整理では監査レポートの対象値を実在出力で整理する記録黄I収集0189です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0188の技術的な意味を資料で確認するとき、監査レポート Server IP 0212との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はServer IPのデータソースと取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。
    - B. 構成を確認する際の意味はI/O 指標を収集するサポートCLIコマンドを証跡採取として確認する。差分確認で差分確認を確認するときは差分確認の誤読を防ぐ。
    - C. 構成を確認する際の意味はRoleのディレクトリー取込と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。ロールと権限 Role 0036固有の属性も確認対象に含める。
    - D. 構成を確認する際の意味はAudit Task Statusのユーザー活動と取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ユーザ・対象デでDの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・収集）です。照合ユーザ・収集に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・収集・対象デです。比較監査レ・収集でA:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸はAud・収集・ユーザです。運用収集・AudでB:の証跡採取 差分確認は「I/O 指標を収集するサポートCLIコマンド」を述べるため、正答側の照合軸はユーザ・監査レ・収集です。項目ユーザ・収集でC:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は対象デ・監査レ・ユーザです。用語ユーザ・収集という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0188**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0188について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.78
    Server IP 198.51.100.28
    Count 78
    確認コード GDP12DD0188A
    ```

    画面・出力には GDP12DD0188A が表示され、監査レポート Audit Task Status 0188 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0188
    Process Type Report
    Status completed
    確認コード GDP12DD0188B
    ```

    画面・出力には GDP12DD0188B が表示され、監査レポート Audit Task Status 0188 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0188C
    ```

    画面・出力には GDP12DD0188C が表示され、監査レポート Audit Task Status 0188 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0188A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0188B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0188C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0203 {#c10-i0394}
*分類: レポート*  ・  難易度: 中級

藍D登録0204ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藍D登録0204です。藍D登録0204は監査レポートの表示操作で監査レポートの対象欄を追跡する記録藍D登録0204です。藍D登録0204ではユーザー活動と取得時刻を採取票藍D登録0204へ残します。藍D登録0204ではジョブ失敗の見落としを避けるため補助資料も照合する判断藍D登録0204です。藍D登録0204の用語整理では監査レポートの対象値を実在出力で照合する記録藍D登録0204です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0203について構成や状態を確認します。監査レポート Server IP 0227ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは表示操作で対象欄を追跡することでデータソースを確認し・ジョブ失敗の見落としを防ぐ。
    - B. 状態を読み取るための働きは表示操作で対象欄を追跡することでユーザー活動を確認し・ジョブ失敗の見落としを防ぐ。 ✅
    - C. 状態を読み取るための働きはプロセス一覧からScheduleを読むことでプロセス一覧を確認し・実行間隔より短いFROM/Tを防ぐ。
    - D. 状態を読み取るための働きは復旧操作で点検欄を確認することでジョブキューを確認し・監査タスク未レビューを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ユーザ・ジョブでBの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・登録）です。照合ユーザ・登録に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・登録・ジョブです。比較監査レ・登録でA:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸はAud・登録・ユーザです。項目ユーザ・登録でC:の障害切り分け AUDIT04は「Audit Processでプロセス一覧から」を述べるため、正答側の照合軸はジョブ・監査レ・ユーザです。仕様ユーザ・登録でD:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は登録・ジョブ・ユーザです。用語ユーザ・登録という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0203**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0203について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.13
    Server IP 198.51.100.43
    Count 93
    確認コード GDP12DD0203A
    ```

    画面・出力には GDP12DD0203A が表示され、監査レポート Audit Task Status 0203 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0203
    Process Type Report
    Status completed
    確認コード GDP12DD0203B
    ```

    画面・出力には GDP12DD0203B が表示され、監査レポート Audit Task Status 0203 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0203C
    ```

    画面・出力には GDP12DD0203C が表示され、監査レポート Audit Task Status 0203 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0203A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0203B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0203C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0218 {#c10-i0395}
*分類: レポート*  ・  難易度: 中級

黒S登録0219ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黒S登録0219です。黒S登録0219は監査レポートの点検操作で監査レポートの判定欄を記録する記録黒S登録0219です。黒S登録0219ではユーザー活動と取得時刻を採取票黒S登録0219へ残します。黒S登録0219ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断黒S登録0219です。黒S登録0219の用語整理では監査レポートの対象値を実在出力で保管する記録黒S登録0219です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0218の役割を調べています。ロールと権限 Login Name 0309の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはLogin Nameのロール割当と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。
    - B. 機能の説明としてはAudit Task Statusのユーザー活動と取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。 ✅
    - C. 機能の説明としてはCentral Managerで保守後の確認では中央管理サーバーの 例外レポートから Exceptionである。保守確認で保守後の確認を確認するときはmanaged unitからを防ぐ。
    - D. 機能の説明としてはServer IPのデータソースと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ユーザ・照会文でBの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・登録）です。照合ユーザ・登録に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・登録・照会文です。比較監査レ・登録でA:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸はAud・登録・ユーザです。項目ユーザ・登録でC:の保守後の確認 CM20は「Central Managerで保守後の確認」を述べるため、正答側の照合軸は照会文・監査レ・ユーザです。仕様ユーザ・登録でD:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は登録・照会文・ユーザです。用語ユーザ・登録という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0218**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0218について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.28
    Server IP 198.51.100.58
    Count 108
    確認コード GDP12DD0218A
    ```

    画面・出力には GDP12DD0218A が表示され、監査レポート Audit Task Status 0218 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0218
    Process Type Report
    Status completed
    確認コード GDP12DD0218B
    ```

    画面・出力には GDP12DD0218B が表示され、監査レポート Audit Task Status 0218 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0218C
    ```

    画面・出力には GDP12DD0218C が表示され、監査レポート Audit Task Status 0218 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0218A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0218B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0218C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0233 {#c10-i0396}
*分類: レポート*  ・  難易度: 上級

灰N確認0234ではIBM Guardium Data Protection 12.x の レポートを扱う採取票灰N確認0234です。灰N確認0234は監査レポートの復旧操作で監査レポートの点検欄を確認する記録灰N確認0234です。灰N確認0234ではユーザー活動と取得時刻を採取票灰N確認0234へ残します。灰N確認0234では監査タスク未レビューを避けるため補助資料も照合する判断灰N確認0234です。灰N確認0234の用語整理では監査レポートの対象値を実在出力で点検する記録灰N確認0234です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート Audit Task Status 0233」を「S-TAP監視 DB Server Type 0295」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして承認クライアを照合する。
    - B. 運用時に利用する技術的役割はmanaged unitからのデを避けるため・通常状態確認で確認では中央を確認するして確認では中央を照合する。
    - C. 運用時に利用する技術的役割は対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてジョブキューを照合する。
    - D. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するしてユーザー活動を照合する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能ユーザ・監査タでDの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・確認）です。照合ユーザ・確認に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・確認・監査タです。比較監査レ・確認でA:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はAud・確認・ユーザです。運用確認・AudでB:の通常状態の確認 CM01は「Central Managerで通常状態の確」を述べるため、正答側の照合軸はユーザ・監査レ・確認です。項目ユーザ・確認でC:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は監査タ・監査レ・ユーザです。用語ユーザ・確認という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0233**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0233について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.43
    Server IP 198.51.100.73
    Count 123
    確認コード GDP12DD0233A
    ```

    画面・出力には GDP12DD0233A が表示され、監査レポート Audit Task Status 0233 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0233
    Process Type Report
    Status completed
    確認コード GDP12DD0233B
    ```

    画面・出力には GDP12DD0233B が表示され、監査レポート Audit Task Status 0233 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0233C
    ```

    画面・出力には GDP12DD0233C が表示され、監査レポート Audit Task Status 0233 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0233A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0233B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0233C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0248 {#c10-i0397}
*分類: レポート*  ・  難易度: 初級

黄I保護0249ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黄I保護0249です。黄I保護0249は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録黄I保護0249です。黄I保護0249ではユーザー活動と取得時刻を採取票黄I保護0249へ残します。黄I保護0249では対象データソースの取り違えを避けるため補助資料も照合する判断黄I保護0249です。黄I保護0249の用語整理では監査レポートの対象値を実在出力で整理する記録黄I保護0249です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0248を同一分類のS-TAP監視 DB Server Type 0310と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は確認操作で状態欄を整理することで承認クライアを確認し・最終応答停止の見落としを防ぐ。
    - B. 構成を確認する際の意味は作業一覧からStatusを読むことで作業一覧を確認し・実行間隔より短いFROM/Tを防ぐ。
    - C. 構成を確認する際の意味は調査操作で保守欄を引き継ぎすることでデータソースを確認し・対象データソースの取り違えを防ぐ。
    - D. 構成を確認する際の意味は調査操作で保守欄を引き継ぎすることでユーザー活動を確認し・対象データソースの取り違えを防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能ユーザ・対象デでDの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・保護）です。照合ユーザ・保護に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・保護・対象デです。比較監査レ・保護でA:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はAud・保護・ユーザです。運用保護・AudでB:の構成監査 AUDIT08は「Audit Processで作業一覧から」を述べるため、正答側の照合軸はユーザ・監査レ・保護です。項目ユーザ・保護でC:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は対象デ・監査レ・ユーザです。用語ユーザ・保護という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0248**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0248について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.18
    Server IP 198.51.100.28
    Count 18
    確認コード GDP12DD0248A
    ```

    画面・出力には GDP12DD0248A が表示され、監査レポート Audit Task Status 0248 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0248
    Process Type Report
    Status completed
    確認コード GDP12DD0248B
    ```

    画面・出力には GDP12DD0248B が表示され、監査レポート Audit Task Status 0248 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0248C
    ```

    画面・出力には GDP12DD0248C が表示され、監査レポート Audit Task Status 0248 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0248A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0248B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0248C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0263 {#c10-i0398}
*分類: レポート*  ・  難易度: 中級

藍D照合0264ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藍D照合0264です。藍D照合0264は監査レポートの表示操作で監査レポートの対象欄を追跡する記録藍D照合0264です。藍D照合0264ではユーザー活動と取得時刻を採取票藍D照合0264へ残します。藍D照合0264ではジョブ失敗の見落としを避けるため補助資料も照合する判断藍D照合0264です。藍D照合0264の用語整理では監査レポートの対象値を実在出力で照合する記録藍D照合0264です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0263の設定や表示を読む前に役割を確認します。S-TAP監視 S-TAP Version 0283ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして暗号化表示を照合する。
    - B. 状態を読み取るための働きはInspectionを避けるため・検査状態からLastResponseを読して検査状態を照合する。
    - C. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するしてユーザー活動を照合する。 ✅
    - D. 状態を読み取るための働きは過剰ロール付与を避けるため・主操作で出力欄を評価するして表示可能レポを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能ユーザ・ジョブでCの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・照合）です。照合ユーザ・照合に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・照合・ジョブです。比較監査レ・照合でA:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はAud・照合・ユーザです。運用照合・AudでB:の障害切り分け IE04は「Inspection Engineで検査状態」を述べるため、正答側の照合軸はユーザ・監査レ・照合です。仕様ユーザ・照合でD:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸は照合・ジョブ・ユーザです。用語ユーザ・照合という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0263**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0263について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.33
    Server IP 198.51.100.43
    Count 33
    確認コード GDP12DD0263A
    ```

    画面・出力には GDP12DD0263A が表示され、監査レポート Audit Task Status 0263 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0263
    Process Type Report
    Status completed
    確認コード GDP12DD0263B
    ```

    画面・出力には GDP12DD0263B が表示され、監査レポート Audit Task Status 0263 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0263C
    ```

    画面・出力には GDP12DD0263C が表示され、監査レポート Audit Task Status 0263 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0263A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0263B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0263C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0278 {#c10-i0399}
*分類: レポート*  ・  難易度: 中級

黒S照合0279ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黒S照合0279です。黒S照合0279は監査レポートの点検操作で監査レポートの判定欄を記録する記録黒S照合0279です。黒S照合0279ではユーザー活動と取得時刻を採取票黒S照合0279へ残します。黒S照合0279ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断黒S照合0279です。黒S照合0279の用語整理では監査レポートの対象値を実在出力で保管する記録黒S照合0279です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0278に関する障害切り分けの前提を確認しています。監査レポート Client IP 0350の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては解除で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。
    - B. 機能の説明としては性能影響確認で確認では中央を証跡に残し・Central Managerで性能影響の確認では中央管理サ。
    - C. 機能の説明としては診断でGuardAを証跡に残し・ディレクトリー UserのGuardAPI権限と取得時刻を記。
    - D. 機能の説明としては照合でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ユーザ・照会文でDの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・照合）です。照合ユーザ・照合に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・照合・照会文です。比較監査レ・照合でA:のClient IPは「Client IPの監査タスクと取得時刻を記」を述べるため、正答側の照合軸はAud・照合・ユーザです。運用照合・AudでB:の性能影響の確認 CM11は「Central Managerで性能影響の確」を述べるため、正答側の照合軸はユーザ・監査レ・照合です。項目ユーザ・照合でC:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は照会文・監査レ・ユーザです。用語ユーザ・照合という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0278**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0278について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.48
    Server IP 198.51.100.58
    Count 48
    確認コード GDP12DD0278A
    ```

    画面・出力には GDP12DD0278A が表示され、監査レポート Audit Task Status 0278 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0278
    Process Type Report
    Status completed
    確認コード GDP12DD0278B
    ```

    画面・出力には GDP12DD0278B が表示され、監査レポート Audit Task Status 0278 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0278C
    ```

    画面・出力には GDP12DD0278C が表示され、監査レポート Audit Task Status 0278 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0278A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0278B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0278C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0293 {#c10-i0400}
*分類: レポート*  ・  難易度: 中級

灰N抑止0294ではIBM Guardium Data Protection 12.x の レポートを扱う採取票灰N抑止0294です。灰N抑止0294は監査レポートの復旧操作で監査レポートの点検欄を確認する記録灰N抑止0294です。灰N抑止0294ではユーザー活動と取得時刻を採取票灰N抑止0294へ残します。灰N抑止0294では監査タスク未レビューを避けるため補助資料も照合する判断灰N抑止0294です。灰N抑止0294の用語整理では監査レポートの対象値を実在出力で点検する記録灰N抑止0294です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0293を保守記録に説明する必要があります。S-TAP監視 DB Server Type 0295と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するしてユーザー活動を照合する。 ✅
    - B. 運用時に利用する技術的役割はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして承認クライアを照合する。
    - C. 運用時に利用する技術的役割はInspectionを避けるため・エージェント変更からInspectionしてエージェントを照合する。
    - D. 運用時に利用する技術的役割はジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するしてジョブキューを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能ユーザ・監査タでAの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・抑止）です。照合ユーザ・抑止に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・抑止・監査タです。運用抑止・AudでB:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はユーザ・監査レ・抑止です。項目ユーザ・抑止でC:の引継ぎ記録 IE09は「Inspection Engineでエージェ」を述べるため、正答側の照合軸は監査タ・監査レ・ユーザです。仕様ユーザ・抑止でD:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は抑止・監査タ・ユーザです。用語ユーザ・抑止という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0293**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0293について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.63
    Server IP 198.51.100.73
    Count 63
    確認コード GDP12DD0293A
    ```

    画面・出力には GDP12DD0293A が表示され、監査レポート Audit Task Status 0293 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0293
    Process Type Report
    Status completed
    確認コード GDP12DD0293B
    ```

    画面・出力には GDP12DD0293B が表示され、監査レポート Audit Task Status 0293 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0293C
    ```

    画面・出力には GDP12DD0293C が表示され、監査レポート Audit Task Status 0293 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0293A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0293B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0293C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0308 {#c10-i0401}
*分類: レポート*  ・  難易度: 中級

黄I解析0309ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黄I解析0309です。黄I解析0309は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録黄I解析0309です。黄I解析0309ではユーザー活動と取得時刻を採取票黄I解析0309へ残します。黄I解析0309では対象データソースの取り違えを避けるため補助資料も照合する判断黄I解析0309です。黄I解析0309の用語整理では監査レポートの対象値を実在出力で整理する記録黄I解析0309です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0308の技術的な意味を資料で確認するとき、S-TAP監視 S-TAP Host 0346との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は確認操作で状態欄を整理することで最終応答を確認し・最終応答停止の見落としを防ぐ。
    - B. 構成を確認する際の意味はジョブキューからJobNameを読むことでジョブキューを確認し・ディスク逼迫中に検査データ流を防ぐ。
    - C. 構成を確認する際の意味は変更確認操作で採取欄を棚卸することで表示可能レポを確認し・ディレクトリー取込対象の誤りを防ぐ。
    - D. 構成を確認する際の意味は調査操作で保守欄を引き継ぎすることでユーザー活動を確認し・対象データソースの取り違えを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能ユーザ・対象デでDの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・解析）です。照合ユーザ・解析に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・解析・対象デです。比較監査レ・解析でA:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸はAud・解析・ユーザです。運用解析・AudでB:の再始動後の確認 APP15は「Appliance Monitoriでジョブ」を述べるため、正答側の照合軸はユーザ・監査レ・解析です。項目ユーザ・解析でC:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸は対象デ・監査レ・ユーザです。用語ユーザ・解析という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0308**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0308について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.78
    Server IP 198.51.100.28
    Count 78
    確認コード GDP12DD0308A
    ```

    画面・出力には GDP12DD0308A が表示され、監査レポート Audit Task Status 0308 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0308
    Process Type Report
    Status completed
    確認コード GDP12DD0308B
    ```

    画面・出力には GDP12DD0308B が表示され、監査レポート Audit Task Status 0308 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0308C
    ```

    画面・出力には GDP12DD0308C が表示され、監査レポート Audit Task Status 0308 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0308A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0308B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0308C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0323 {#c10-i0402}
*分類: レポート*  ・  難易度: 中級

藍D計画0324ではIBM Guardium Data Protection 12.x の レポートを扱う採取票藍D計画0324です。藍D計画0324は監査レポートの表示操作で監査レポートの対象欄を追跡する記録藍D計画0324です。藍D計画0324ではユーザー活動と取得時刻を採取票藍D計画0324へ残します。藍D計画0324ではジョブ失敗の見落としを避けるため補助資料も照合する判断藍D計画0324です。藍D計画0324の用語整理では監査レポートの対象値を実在出力で照合する記録藍D計画0324です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0323について構成や状態を確認します。S-TAP監視 KTAP Installed 0334ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは確認操作で状態欄を整理することで監視エージェを確認し・最終応答停止の見落としを防ぐ。
    - B. 状態を読み取るための働きは表示操作で対象欄を追跡することでユーザー活動を確認し・ジョブ失敗の見落としを防ぐ。 ✅
    - C. 状態を読み取るための働きは監視プロセスからApplianceを読むことで監視プロセスを確認し・ディスク逼迫中に検査データ流を防ぐ。
    - D. 状態を読み取るための働きは主操作で出力欄を評価することでGuardAを確認し・過剰ロール付与を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ユーザ・ジョブでBの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・計画）です。照合ユーザ・計画に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・計画・ジョブです。比較監査レ・計画でA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はAud・計画・ユーザです。項目ユーザ・計画でC:の障害切り分け APP04は「Appliance Monitoriで監視プ」を述べるため、正答側の照合軸はジョブ・監査レ・ユーザです。仕様ユーザ・計画でD:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は計画・ジョブ・ユーザです。用語ユーザ・計画という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0323**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0323について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.13
    Server IP 198.51.100.43
    Count 93
    確認コード GDP12DD0323A
    ```

    画面・出力には GDP12DD0323A が表示され、監査レポート Audit Task Status 0323 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0323
    Process Type Report
    Status completed
    確認コード GDP12DD0323B
    ```

    画面・出力には GDP12DD0323B が表示され、監査レポート Audit Task Status 0323 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0323C
    ```

    画面・出力には GDP12DD0323C が表示され、監査レポート Audit Task Status 0323 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0323A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0323B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0323C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0338 {#c10-i0403}
*分類: レポート*  ・  難易度: 中級

黒S計画0339ではIBM Guardium Data Protection 12.x の レポートを扱う採取票黒S計画0339です。黒S計画0339は監査レポートの点検操作で監査レポートの判定欄を記録する記録黒S計画0339です。黒S計画0339ではユーザー活動と取得時刻を採取票黒S計画0339へ残します。黒S計画0339ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断黒S計画0339です。黒S計画0339の用語整理では監査レポートの対象値を実在出力で保管する記録黒S計画0339です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Audit Task Status 0338の役割を調べています。監査プロセス Audit Process Builder 変更前の確認の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては変更確認で作業一覧を証跡に残し・Audit Processで作業一覧から Status。
    - B. 機能の説明としては計画でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。 ✅
    - C. 機能の説明としては棚卸でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。監査レポート Server IP 0032固有の属性も確認対象に含める。
    - D. 機能の説明としては切替でロール割当を証跡に残し・Login Nameのロール割当と取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能ユーザ・照会文でBの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・計画）です。照合ユーザ・計画に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・計画・照会文です。比較監査レ・計画でA:の変更前の確認 AUDIT02は「Audit Processで作業一覧から」を述べるため、正答側の照合軸はAud・計画・ユーザです。項目ユーザ・計画でC:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は照会文・監査レ・ユーザです。仕様ユーザ・計画でD:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は計画・照会文・ユーザです。用語ユーザ・計画という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0338**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0338について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.28
    Server IP 198.51.100.58
    Count 108
    確認コード GDP12DD0338A
    ```

    画面・出力には GDP12DD0338A が表示され、監査レポート Audit Task Status 0338 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0338
    Process Type Report
    Status completed
    確認コード GDP12DD0338B
    ```

    画面・出力には GDP12DD0338B が表示され、監査レポート Audit Task Status 0338 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0338C
    ```

    画面・出力には GDP12DD0338C が表示され、監査レポート Audit Task Status 0338 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0338A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0338B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0338C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Audit Task Status 0353 {#c10-i0404}
*分類: レポート*  ・  難易度: 上級

灰N解除0354ではIBM Guardium Data Protection 12.x の レポートを扱う採取票灰N解除0354です。灰N解除0354は監査レポートの復旧操作で監査レポートの点検欄を確認する記録灰N解除0354です。灰N解除0354ではユーザー活動と取得時刻を採取票灰N解除0354へ残します。灰N解除0354では監査タスク未レビューを避けるため補助資料も照合する判断灰N解除0354です。灰N解除0354の用語整理では監査レポートの対象値を実在出力で点検する記録灰N解除0354です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート Audit Task Status 0353」を「監査プロセス Audit Process Builder 復旧後の確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は報告上限からmax_audit_repoことで報告上限を確認し・実行間隔より短いFROM/Tを防ぐ。
    - B. 運用時に利用する技術的役割はジョブキューからJobNameを読むことでジョブキューを確認し・ディスク逼迫中に検査データ流を防ぐ。
    - C. 運用時に利用する技術的役割は復旧操作で点検欄を確認することでユーザー活動を確認し・監査タスク未レビューを防ぐ。 ✅
    - D. 運用時に利用する技術的役割は監査操作で記録欄を比較することでGuardAを確認し・GuardAPI実行権限不足を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能ユーザ・監査タでCの記述「Audit Task Statusのユーザー活動と取得時」に対応する項目はTask Status（Aud・ユーザ・解除）です。照合ユーザ・解除に関するレポートの仕様は「Audit Task Statusのユーザー活動と取得時刻を記録し」で、確認対象はユーザ・解除・監査タです。比較監査レ・解除でA:の復旧後の確認 AUDIT06は「Audit Processで報告上限から」を述べるため、正答側の照合軸はAud・解除・ユーザです。運用解除・AudでB:の監査証跡の保存 APP18は「Appliance Monitoriでジョブ」を述べるため、正答側の照合軸はユーザ・監査レ・解除です。仕様ユーザ・解除でD:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は解除・監査タ・ユーザです。用語ユーザ・解除という用語は「Audit Task Statusのユーザー活動と取」を指し、照合する値と誤認リスクの組合せは監査レ・ユーザ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Audit Task Status 0353**

    - 検証目的: 監査レポートの監査レポート Audit Task Status 0353について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Audit Task Status と ユーザー活動
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> Guardium Job Queue report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.43
    Server IP 198.51.100.73
    Count 123
    確認コード GDP12DD0353A
    ```

    画面・出力には GDP12DD0353A が表示され、監査レポート Audit Task Status 0353 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0353
    Process Type Report
    Status completed
    確認コード GDP12DD0353B
    ```

    画面・出力には GDP12DD0353B が表示され、監査レポート Audit Task Status 0353 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Audit Task Status を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0353C
    ```

    画面・出力には GDP12DD0353C が表示され、監査レポート Audit Task Status 0353 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0353A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0353B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0353C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0005 {#c10-i0405}
*分類: レポート*  ・  難易度: 初級

銀F巡回0006ではIBM Guardium Data Protection 12.x の レポートを扱う採取票銀F巡回0006です。銀F巡回0006は監査レポートの復旧操作で監査レポートの点検欄を確認する記録銀F巡回0006です。銀F巡回0006では監査タスクと取得時刻を採取票銀F巡回0006へ残します。銀F巡回0006では監査タスク未レビューを避けるため補助資料も照合する判断銀F巡回0006です。銀F巡回0006の用語整理では監査レポートの対象値を実在出力で点検する記録銀F巡回0006です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0005を保守記録に説明する必要があります。S-TAP監視 S-TAP Version 0058と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は最終応答停止の見落としを避けるため・確認操作で状態欄を整理するして暗号化表示を照合する。
    - B. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するしてジョブキューを照合する。
    - C. 運用時に利用する技術的役割は実行間隔より短いFROM/TO範を避けるため・世代整合確認で世代整合の確を確認するして世代整合の確を照合する。
    - D. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するして監査タスクを照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 巡回対象監査タスクでDの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Clien・巡回・監査タ・監査タス）です。巡回時の監査タスクに関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象はClie・巡回・監査タ・監査タスです。監視・復旧・暗号化表のA:は「S-TAPの暗号化表示と取得時刻を記録し」を述べ、対象はS-TAP Version（監視エージ・復旧・暗号化・最終応答）です。確認対象ジョブキュのB:は「SQL Verbのジョブキューと取得時刻を記録し」を述べ、対象はSQL Verb（照会文・確認・ジョブ・監査タス）です。世代整合時の世代整合ののC:は「Audit Processで世代整合の確認では監査プロセスの」を述べ、対象は世代整合の確認 AUDIT17（Audit・世代整・世代整・実行間隔）です。監査タスクを巡回という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、Client IP（Clien・巡回・監査タ・監査タス）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0005**

    - 検証目的: 監査レポートの監査レポート Client IP 0005について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.15
    Server IP 198.51.100.25
    Count 15
    確認コード GDP12DD0005A
    ```

    画面・出力には GDP12DD0005A が表示され、監査レポート Client IP 0005 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0005
    Process Type Report
    Status completed
    確認コード GDP12DD0005B
    ```

    画面・出力には GDP12DD0005B が表示され、監査レポート Client IP 0005 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0005C
    ```

    画面・出力には GDP12DD0005C が表示され、監査レポート Client IP 0005 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0005A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0005B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0005C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0020 {#c10-i0406}
*分類: レポート*  ・  難易度: 初級

蒼A棚卸0021ではIBM Guardium Data Protection 12.x の レポートを扱う採取票蒼A棚卸0021です。蒼A棚卸0021は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録蒼A棚卸0021です。蒼A棚卸0021では監査タスクと取得時刻を採取票蒼A棚卸0021へ残します。蒼A棚卸0021では対象データソースの取り違えを避けるため補助資料も照合する判断蒼A棚卸0021です。蒼A棚卸0021の用語整理では監査レポートの対象値を実在出力で整理する記録蒼A棚卸0021です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0020の技術的な意味を資料で確認するとき、監査レポート SQL Verb 0086との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は変更でジョブキューを証跡に残し・SQL Verbのジョブキューと取得時刻を記録し。
    - B. 構成を確認する際の意味は保護で表示可能レポを証跡に残し・Permissionの表示可能レポートと取得時刻を記録し。
    - C. 構成を確認する際の意味は依存関係確認で依存関係の確を証跡に残し・Audit Processで依存関係の確認では監査プロセスの。
    - D. 構成を確認する際の意味は棚卸で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 棚卸対象監査タスクでDの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Clien・棚卸・監査タ・対象デー）です。棚卸時の監査タスクに関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象はClie・棚卸・監査タ・対象デーです。照会・変更・ジョブキのA:は「SQL Verbのジョブキューと取得時刻を記録し」を述べ、対象はSQL Verb（照会文・変更・ジョブ・照会文動）です。保護対象表示可能レのB:は「Permissionの表示可能レポートと取得時刻を記録し」を述べ、対象はロールと権限 Permission（Permi・保護・表示可・ディレク）です。依存関係時の依存関係ののC:は「Audit Processで依存関係の確認では監査プロセスの」を述べ、対象は依存関係の確認 AUDIT13（Audit・依存関・依存関・実行間隔）です。監査タスクを棚卸という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、Client IP（Clien・棚卸・監査タ・対象デー）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0020**

    - 検証目的: 監査レポートの監査レポート Client IP 0020について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.30
    Server IP 198.51.100.40
    Count 30
    確認コード GDP12DD0020A
    ```

    画面・出力には GDP12DD0020A が表示され、監査レポート Client IP 0020 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0020
    Process Type Report
    Status completed
    確認コード GDP12DD0020B
    ```

    画面・出力には GDP12DD0020B が表示され、監査レポート Client IP 0020 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0020C
    ```

    画面・出力には GDP12DD0020C が表示され、監査レポート Client IP 0020 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0020A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0020B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0020C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0035 {#c10-i0407}
*分類: レポート*  ・  難易度: 中級

金P棚卸0036ではIBM Guardium Data Protection 12.x の レポートを扱う採取票金P棚卸0036です。金P棚卸0036は監査レポートの表示操作で監査レポートの対象欄を追跡する記録金P棚卸0036です。金P棚卸0036では監査タスクと取得時刻を採取票金P棚卸0036へ残します。金P棚卸0036ではジョブ失敗の見落としを避けるため補助資料も照合する判断金P棚卸0036です。金P棚卸0036の用語整理では監査レポートの対象値を実在出力で照合する記録金P棚卸0036です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0035について構成や状態を確認します。監査レポート SQL Verb 0071ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するしてジョブキューを照合する。
    - B. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するして監査タスクを照合する。 ✅
    - C. 状態を読み取るための働きはGuardAPI実行権限不足を避けるため・監査操作で記録欄を比較するしてユーザー有効を照合する。
    - D. 状態を読み取るための働きは実行間隔より短いFROM/TO範を避けるため・監査プロセスで引継ぎ記録でを確認するして引継ぎ記録でを照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 棚卸対象監査タスクでBの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Clien・棚卸・監査タ・ジョブ失）です。棚卸時の監査タスクに関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象はClie・棚卸・監査タ・ジョブ失です。照会・監査・ジョブキのA:は「SQL Verbのジョブキューと取得時刻を記録し」を述べ、対象はSQL Verb（照会文・監査・ジョブ・ジョブ失）です。保護時のユーザー有のC:は「Application Accessのユーザー有効化と取得時刻を記録」を述べ、対象はApplication Access（Appli・保護・ユーザ・Guar）です。引継ぎ記録を監査プロセのD:は「Audit Processで引継ぎ記録では監査プロセスの」を述べ、対象は引継ぎ記録 AUDIT09（Audit・監査プ・引継ぎ・実行間隔）です。監査タスクを棚卸という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、Client IP（Clien・棚卸・監査タ・ジョブ失）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0035**

    - 検証目的: 監査レポートの監査レポート Client IP 0035について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.45
    Server IP 198.51.100.55
    Count 45
    確認コード GDP12DD0035A
    ```

    画面・出力には GDP12DD0035A が表示され、監査レポート Client IP 0035 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0035
    Process Type Report
    Status completed
    確認コード GDP12DD0035B
    ```

    画面・出力には GDP12DD0035B が表示され、監査レポート Client IP 0035 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0035C
    ```

    画面・出力には GDP12DD0035C が表示され、監査レポート Client IP 0035 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0035A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0035B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0035C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0050 {#c10-i0408}
*分類: レポート*  ・  難易度: 中級

紺K復旧0051ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紺K復旧0051です。紺K復旧0051は監査レポートの点検操作で監査レポートの判定欄を記録する記録紺K復旧0051です。紺K復旧0051では監査タスクと取得時刻を採取票紺K復旧0051へ残します。紺K復旧0051ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紺K復旧0051です。紺K復旧0051の用語整理では監査レポートの対象値を実在出力で保管する記録紺K復旧0051です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0050の役割を調べています。ロールと権限 LDAP User 0102の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては変更確認操作で採取欄を棚卸することでGuardAを確認し・ディレクトリー取込対象の誤りを防ぐ。
    - B. 機能の説明としては監査操作で記録欄を比較することでディレクトリを確認し・GuardAPI実行権限不足を防ぐ。
    - C. 機能の説明としては依存関係確認で依存関係の確を確認することで依存関係の確を確認し・実行間隔より短いFROM/Tを防ぐ。
    - D. 機能の説明としては点検操作で判定欄を記録することで監査タスクを確認し・照会文動詞集計の期間誤りを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 復旧対象監査タスクでDの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Clien・復旧・監査タ・照会文動）です。復旧時の監査タスクに関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象はClie・復旧・監査タ・照会文動です。ディ・移行・GuarのA:は「LDAP UserのGuardAPI権限と取得時刻を記録し」を述べ、対象はLDAP User（ディレクト・移行・Gua・ディレク）です。確認対象ディレクトのB:は「RoleのLDAP取込と取得時刻を記録し」を述べ、対象はロールと権限 Role（Role・確認・ディレ・Guar）です。依存関係時の依存関係ののC:は「Audit Processで依存関係の確認では監査プロセスの」を述べ、対象は依存関係の確認 AUDIT13（Audit・依存関・依存関・実行間隔）です。監査タスクを復旧という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、Client IP（Clien・復旧・監査タ・照会文動）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0050**

    - 検証目的: 監査レポートの監査レポート Client IP 0050について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.60
    Server IP 198.51.100.70
    Count 60
    確認コード GDP12DD0050A
    ```

    画面・出力には GDP12DD0050A が表示され、監査レポート Client IP 0050 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0050
    Process Type Report
    Status completed
    確認コード GDP12DD0050B
    ```

    画面・出力には GDP12DD0050B が表示され、監査レポート Client IP 0050 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0050C
    ```

    画面・出力には GDP12DD0050C が表示され、監査レポート Client IP 0050 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0050A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0050B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0050C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0065 {#c10-i0409}
*分類: レポート*  ・  難易度: 中級

銀F監査0066ではIBM Guardium Data Protection 12.x の レポートを扱う採取票銀F監査0066です。銀F監査0066は監査レポートの復旧操作で監査レポートの点検欄を確認する記録銀F監査0066です。銀F監査0066では監査タスクと取得時刻を採取票銀F監査0066へ残します。銀F監査0066では監査タスク未レビューを避けるため補助資料も照合する判断銀F監査0066です。銀F監査0066の用語整理では監査レポートの対象値を実在出力で点検する記録銀F監査0066です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート Client IP 0065」を「ロールと権限 Role 0141」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は監査で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。 ✅
    - B. 運用時に利用する技術的役割は保守でディレクトリを証跡に残し・Roleのディレクトリー取込と取得時刻を記録し。
    - C. 運用時に利用する技術的役割は計画でユーザー有効を証跡に残し・Application Accessのユーザー有効化と取得時。
    - D. 運用時に利用する技術的役割は容量余力確認で集約エラーを証跡に残し・Aggregatorで集約エラーから。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能監査タ・監査タでAの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・監査）です。照合監査タ・監査に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・監査・監査タです。運用監査・CliでB:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は監査タ・監査レ・監査です。項目監査タ・監査でC:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は監査タ・監査レ・監査タです。仕様監査タ・監査でD:の容量余力の確認 AGG16は「Aggregatorで集約エラーから」を述べるため、正答側の照合軸は監査・監査タ・監査タです。用語監査タ・監査という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0065**

    - 検証目的: 監査レポートの監査レポート Client IP 0065について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.75
    Server IP 198.51.100.25
    Count 75
    確認コード GDP12DD0065A
    ```

    画面・出力には GDP12DD0065A が表示され、監査レポート Client IP 0065 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0065
    Process Type Report
    Status completed
    確認コード GDP12DD0065B
    ```

    画面・出力には GDP12DD0065B が表示され、監査レポート Client IP 0065 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0065C
    ```

    画面・出力には GDP12DD0065C が表示され、監査レポート Client IP 0065 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0065A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0065B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0065C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0080 {#c10-i0410}
*分類: レポート*  ・  難易度: 中級

蒼A変更0081ではIBM Guardium Data Protection 12.x の レポートを扱う採取票蒼A変更0081です。蒼A変更0081は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録蒼A変更0081です。蒼A変更0081では監査タスクと取得時刻を採取票蒼A変更0081へ残します。蒼A変更0081では対象データソースの取り違えを避けるため補助資料も照合する判断蒼A変更0081です。蒼A変更0081の用語整理では監査レポートの対象値を実在出力で整理する記録蒼A変更0081です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0080を同一分類のS-TAP監視 DB Server Type 0160と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は切替で承認クライアを証跡に残し・監視エージェントの承認クライアントと取得時刻を記録し。
    - B. 構成を確認する際の意味は抑止でロール割当を証跡に残し・Login Nameのロール割当と取得時刻を記録し。
    - C. 構成を確認する際の意味は監査証跡の保でエージェントを証跡に残し・Inspection Engineでエージェント変更から。
    - D. 構成を確認する際の意味は変更で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能監査タ・対象デでDの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・変更）です。照合監査タ・変更に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・変更・対象デです。比較監査レ・変更でA:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はCli・変更・監査タです。運用変更・CliでB:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は監査タ・監査レ・変更です。項目監査タ・変更でC:の監査証跡の保存 IE18は「Inspection Engineでエージェ」を述べるため、正答側の照合軸は対象デ・監査レ・監査タです。用語監査タ・変更という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0080**

    - 検証目的: 監査レポートの監査レポート Client IP 0080について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.10
    Server IP 198.51.100.40
    Count 90
    確認コード GDP12DD0080A
    ```

    画面・出力には GDP12DD0080A が表示され、監査レポート Client IP 0080 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0080
    Process Type Report
    Status completed
    確認コード GDP12DD0080B
    ```

    画面・出力には GDP12DD0080B が表示され、監査レポート Client IP 0080 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0080C
    ```

    画面・出力には GDP12DD0080C が表示され、監査レポート Client IP 0080 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0080A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0080B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0080C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0095 {#c10-i0411}
*分類: レポート*  ・  難易度: 中級

金P変更0096ではIBM Guardium Data Protection 12.x の レポートを扱う採取票金P変更0096です。金P変更0096は監査レポートの表示操作で監査レポートの対象欄を追跡する記録金P変更0096です。金P変更0096では監査タスクと取得時刻を採取票金P変更0096へ残します。金P変更0096ではジョブ失敗の見落としを避けるため補助資料も照合する判断金P変更0096です。金P変更0096の用語整理では監査レポートの対象値を実在出力で照合する記録金P変更0096です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0095の設定や表示を読む前に役割を確認します。ロールと権限 Application Access 0120ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはClient IPの監査タスクと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。 ✅
    - B. 状態を読み取るための働きはApplication Accessのユーザー有効化と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。
    - C. 状態を読み取るための働きは監査要件に沿ってレポート実行とレビューを束ねる処理である。状態確認で開始時刻を確認するときは開始時刻の誤読を防ぐ。
    - D. 状態を読み取るための働きはGuardiumで参照箇所から UsedBy を読み・UsedBy と Operation を照合する。参照箇所からUsedByを読むときは廃止サーバーの参照を残して監を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能監査タ・ジョブでAの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・変更）です。照合監査タ・変更に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・変更・ジョブです。運用変更・CliでB:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は監査タ・監査レ・変更です。項目監査タ・変更でC:の状態確認 開始時刻は「監査要件に沿ってレポート実行とレビューを束ね」を述べるため、正答側の照合軸はジョブ・監査レ・監査タです。仕様監査タ・変更でD:の保守後の確認 DSRC20は「Guardiumで参照箇所から」を述べるため、正答側の照合軸は変更・ジョブ・監査タです。用語監査タ・変更という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0095**

    - 検証目的: 監査レポートの監査レポート Client IP 0095について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.25
    Server IP 198.51.100.55
    Count 105
    確認コード GDP12DD0095A
    ```

    画面・出力には GDP12DD0095A が表示され、監査レポート Client IP 0095 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0095
    Process Type Report
    Status completed
    確認コード GDP12DD0095B
    ```

    画面・出力には GDP12DD0095B が表示され、監査レポート Client IP 0095 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0095C
    ```

    画面・出力には GDP12DD0095C が表示され、監査レポート Client IP 0095 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0095A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0095B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0095C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0110 {#c10-i0412}
*分類: レポート*  ・  難易度: 上級

紺K移行0111ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紺K移行0111です。紺K移行0111は監査レポートの点検操作で監査レポートの判定欄を記録する記録紺K移行0111です。紺K移行0111では監査タスクと取得時刻を採取票紺K移行0111へ残します。紺K移行0111ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紺K移行0111です。紺K移行0111の用語整理では監査レポートの対象値を実在出力で保管する記録紺K移行0111です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0110に関する障害切り分けの前提を確認しています。S-TAP監視 S-TAP Version 0133の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはClient IPの監査タスクと取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。 ✅
    - B. 機能の説明としては監視エージェントの暗号化表示と取得時刻を記録し・未承認監視エージェント接続を防ぐである。記録操作で証跡欄を照合するときは未承認監視エージェント接続を防ぐ。
    - C. 機能の説明としては監視エージェントの最終応答と取得時刻を記録し・カーネル監視導入状態の誤読を防ぐである。採取操作で照合欄を点検するときはカーネル監視導入状態の誤読を防ぐ。
    - D. 機能の説明としてはディレクトリー UserのGuardAPI権限と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能監査タ・照会文でAの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・移行）です。照合監査タ・移行に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・移行・照会文です。運用移行・CliでB:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は監査タ・監査レ・移行です。項目監査タ・移行でC:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は照会文・監査レ・監査タです。仕様監査タ・移行でD:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は移行・照会文・監査タです。用語監査タ・移行という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0110**

    - 検証目的: 監査レポートの監査レポート Client IP 0110について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.40
    Server IP 198.51.100.70
    Count 120
    確認コード GDP12DD0110A
    ```

    画面・出力には GDP12DD0110A が表示され、監査レポート Client IP 0110 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0110
    Process Type Report
    Status completed
    確認コード GDP12DD0110B
    ```

    画面・出力には GDP12DD0110B が表示され、監査レポート Client IP 0110 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0110C
    ```

    画面・出力には GDP12DD0110C が表示され、監査レポート Client IP 0110 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0110A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0110B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0110C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0125 {#c10-i0413}
*分類: レポート*  ・  難易度: 初級

銀F診断0126ではIBM Guardium Data Protection 12.x の レポートを扱う採取票銀F診断0126です。銀F診断0126は監査レポートの復旧操作で監査レポートの点検欄を確認する記録銀F診断0126です。銀F診断0126では監査タスクと取得時刻を採取票銀F診断0126へ残します。銀F診断0126では監査タスク未レビューを避けるため補助資料も照合する判断銀F診断0126です。銀F診断0126の用語整理では監査レポートの対象値を実在出力で点検する記録銀F診断0126です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0125を保守記録に説明する必要があります。監査レポート DB User Name 0164と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は切替で照会文動詞集を証跡に残し・データベース User Nameの照会文動詞集計と取得時刻を。
    - B. 運用時に利用する技術的役割は計画でGuardAを証跡に残し・ディレクトリー UserのGuardAPI権限と取得時刻を記。
    - C. 運用時に利用する技術的役割は診断で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。 ✅
    - D. 運用時に利用する技術的役割は依存関係確認で検査状態を証跡に残し・Inspection Engineで検査状態から。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能監査タ・監査タでCの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・診断）です。照合監査タ・診断に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・診断・監査タです。比較監査レ・診断でA:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸はCli・診断・監査タです。運用診断・CliでB:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は監査タ・監査レ・診断です。仕様監査タ・診断でD:の依存関係の確認 IE13は「Inspection Engineで検査状態」を述べるため、正答側の照合軸は診断・監査タ・監査タです。用語監査タ・診断という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0125**

    - 検証目的: 監査レポートの監査レポート Client IP 0125について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.15
    Server IP 198.51.100.25
    Count 15
    確認コード GDP12DD0125A
    ```

    画面・出力には GDP12DD0125A が表示され、監査レポート Client IP 0125 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0125
    Process Type Report
    Status completed
    確認コード GDP12DD0125B
    ```

    画面・出力には GDP12DD0125B が表示され、監査レポート Client IP 0125 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0125C
    ```

    画面・出力には GDP12DD0125C が表示され、監査レポート Client IP 0125 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0125A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0125B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0125C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0140 {#c10-i0414}
*分類: レポート*  ・  難易度: 初級

蒼A保守0141ではIBM Guardium Data Protection 12.x の レポートを扱う採取票蒼A保守0141です。蒼A保守0141は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録蒼A保守0141です。蒼A保守0141では監査タスクと取得時刻を採取票蒼A保守0141へ残します。蒼A保守0141では対象データソースの取り違えを避けるため補助資料も照合する判断蒼A保守0141です。蒼A保守0141の用語整理では監査レポートの対象値を実在出力で整理する記録蒼A保守0141です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0140の技術的な意味を資料で確認するとき、S-TAP監視 KTAP Installed 0214との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は監視エージェントの監視エージェント状態と取得時刻を記録し・最終応答停止の見落としを防ぐである。確認操作で状態欄を整理するときは最終応答停止の見落としを防ぐ。
    - B. 構成を確認する際の意味はClient IPの監査タスクと取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。 ✅
    - C. 構成を確認する際の意味は監査要件に沿ってレポート実行とレビューを束ねる処理である。状態確認で開始時刻を確認するときは開始時刻の誤読を防ぐ。
    - D. 構成を確認する際の意味はRoleのディレクトリー取込と取得時刻を記録し・過剰ロール付与を防ぐである。主操作で出力欄を評価するときは過剰ロール付与を防ぐ。ロールと権限 Role 0021固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能監査タ・対象デでBの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・保守）です。照合監査タ・保守に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・保守・対象デです。比較監査レ・保守でA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はCli・保守・監査タです。項目監査タ・保守でC:の状態確認 開始時刻は「監査要件に沿ってレポート実行とレビューを束ね」を述べるため、正答側の照合軸は対象デ・監査レ・監査タです。仕様監査タ・保守でD:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は保守・対象デ・監査タです。用語監査タ・保守という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0140**

    - 検証目的: 監査レポートの監査レポート Client IP 0140について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.30
    Server IP 198.51.100.40
    Count 30
    確認コード GDP12DD0140A
    ```

    画面・出力には GDP12DD0140A が表示され、監査レポート Client IP 0140 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0140
    Process Type Report
    Status completed
    確認コード GDP12DD0140B
    ```

    画面・出力には GDP12DD0140B が表示され、監査レポート Client IP 0140 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0140C
    ```

    画面・出力には GDP12DD0140C が表示され、監査レポート Client IP 0140 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0140A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0140B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0140C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0155 {#c10-i0415}
*分類: レポート*  ・  難易度: 中級

金P保守0156ではIBM Guardium Data Protection 12.x の レポートを扱う採取票金P保守0156です。金P保守0156は監査レポートの表示操作で監査レポートの対象欄を追跡する記録金P保守0156です。金P保守0156では監査タスクと取得時刻を採取票金P保守0156へ残します。金P保守0156ではジョブ失敗の見落としを避けるため補助資料も照合する判断金P保守0156です。金P保守0156の用語整理では監査レポートの対象値を実在出力で照合する記録金P保守0156です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0155について構成や状態を確認します。ロールと権限 Role 0216ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは表示操作で対象欄を追跡することで監査タスクを確認し・ジョブ失敗の見落としを防ぐ。 ✅
    - B. 状態を読み取るための働きは照合操作で確認欄を採取することでディレクトリを確認し・監査担当者の閲覧範囲不足を防ぐ。
    - C. 状態を読み取るための働きは証跡採取で自動処理を確認することで自動処理を確認し・自動処理の誤読を防ぐ。
    - D. 状態を読み取るための働きは確認操作で状態欄を整理することでカーネル監視を確認し・最終応答停止の見落としを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能監査タ・ジョブでAの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・保守）です。照合監査タ・保守に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・保守・ジョブです。運用保守・CliでB:のロールと権限 Roleは「Roleのディレクトリー取込と取得時刻を記録」を述べるため、正答側の照合軸は監査タ・監査レ・保守です。項目監査タ・保守でC:の証跡採取 自動処理は「処理ID、状態、開始終了時刻、Data」を述べるため、正答側の照合軸はジョブ・監査レ・監査タです。仕様監査タ・保守でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は保守・ジョブ・監査タです。用語監査タ・保守という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0155**

    - 検証目的: 監査レポートの監査レポート Client IP 0155について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.45
    Server IP 198.51.100.55
    Count 45
    確認コード GDP12DD0155A
    ```

    画面・出力には GDP12DD0155A が表示され、監査レポート Client IP 0155 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0155
    Process Type Report
    Status completed
    確認コード GDP12DD0155B
    ```

    画面・出力には GDP12DD0155B が表示され、監査レポート Client IP 0155 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0155C
    ```

    画面・出力には GDP12DD0155C が表示され、監査レポート Client IP 0155 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0155A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0155B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0155C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0170 {#c10-i0416}
*分類: レポート*  ・  難易度: 中級

紺K切替0171ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紺K切替0171です。紺K切替0171は監査レポートの点検操作で監査レポートの判定欄を記録する記録紺K切替0171です。紺K切替0171では監査タスクと取得時刻を採取票紺K切替0171へ残します。紺K切替0171ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紺K切替0171です。紺K切替0171の用語整理では監査レポートの対象値を実在出力で保管する記録紺K切替0171です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0170の役割を調べています。S-TAP監視 KTAP Installed 0259の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては採取操作で照合欄を点検することで監視エージェを確認し・カーネル監視導入状態の誤読を防ぐ。
    - B. 機能の説明としては証跡採取で承認履歴を確認することで承認履歴を確認し・承認履歴の誤読を防ぐ。
    - C. 機能の説明としては点検操作で判定欄を記録することで監査タスクを確認し・照会文動詞集計の期間誤りを防ぐ。 ✅
    - D. 機能の説明としては照合操作で確認欄を採取することでロール割当を確認し・監査担当者の閲覧範囲不足を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能監査タ・照会文でCの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・切替）です。照合監査タ・切替に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・切替・照会文です。比較監査レ・切替でA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はCli・切替・監査タです。運用切替・CliでB:の証跡採取 承認履歴は「監視対象データベースやサービスを表す」を述べるため、正答側の照合軸は監査タ・監査レ・切替です。仕様監査タ・切替でD:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は切替・照会文・監査タです。用語監査タ・切替という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0170**

    - 検証目的: 監査レポートの監査レポート Client IP 0170について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.60
    Server IP 198.51.100.70
    Count 60
    確認コード GDP12DD0170A
    ```

    画面・出力には GDP12DD0170A が表示され、監査レポート Client IP 0170 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0170
    Process Type Report
    Status completed
    確認コード GDP12DD0170B
    ```

    画面・出力には GDP12DD0170B が表示され、監査レポート Client IP 0170 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0170C
    ```

    画面・出力には GDP12DD0170C が表示され、監査レポート Client IP 0170 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0170A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0170B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0170C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0185 {#c10-i0417}
*分類: レポート*  ・  難易度: 中級

銀F収集0186ではIBM Guardium Data Protection 12.x の レポートを扱う採取票銀F収集0186です。銀F収集0186は監査レポートの復旧操作で監査レポートの点検欄を確認する記録銀F収集0186です。銀F収集0186では監査タスクと取得時刻を採取票銀F収集0186へ残します。銀F収集0186では監査タスク未レビューを避けるため補助資料も照合する判断銀F収集0186です。銀F収集0186の用語整理では監査レポートの対象値を実在出力で点検する記録銀F収集0186です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート Client IP 0185」を「監査レポート Audit Task Status 0218」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はClient IPの監査タスクと取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。 ✅
    - B. 運用時に利用する技術的役割はAudit Task Statusのユーザー活動と取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。
    - C. 運用時に利用する技術的役割は複数 collector の監査情報を集約しレポートへ渡す装置を証跡採取として確認する。証跡採取で取得間隔を確認するときは取得間隔の誤読を防ぐ。
    - D. 運用時に利用する技術的役割は監視エージェントのカーネル監視有無と取得時刻を記録し・最終応答停止の見落としを防ぐである。確認操作で状態欄を整理するときは最終応答停止の見落としを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能監査タ・監査タでAの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・収集）です。照合監査タ・収集に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・収集・監査タです。運用収集・CliでB:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は監査タ・監査レ・収集です。項目監査タ・収集でC:の証跡採取 取得間隔は「複数 collector の監査情報を集約し」を述べるため、正答側の照合軸は監査タ・監査レ・監査タです。仕様監査タ・収集でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は収集・監査タ・監査タです。用語監査タ・収集という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0185**

    - 検証目的: 監査レポートの監査レポート Client IP 0185について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.75
    Server IP 198.51.100.25
    Count 75
    確認コード GDP12DD0185A
    ```

    画面・出力には GDP12DD0185A が表示され、監査レポート Client IP 0185 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0185
    Process Type Report
    Status completed
    確認コード GDP12DD0185B
    ```

    画面・出力には GDP12DD0185B が表示され、監査レポート Client IP 0185 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0185C
    ```

    画面・出力には GDP12DD0185C が表示され、監査レポート Client IP 0185 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0185A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0185B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0185C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0200 {#c10-i0418}
*分類: レポート*  ・  難易度: 中級

蒼A登録0201ではIBM Guardium Data Protection 12.x の レポートを扱う採取票蒼A登録0201です。蒼A登録0201は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録蒼A登録0201です。蒼A登録0201では監査タスクと取得時刻を採取票蒼A登録0201へ残します。蒼A登録0201では対象データソースの取り違えを避けるため補助資料も照合する判断蒼A登録0201です。蒼A登録0201の用語整理では監査レポートの対象値を実在出力で整理する記録蒼A登録0201です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0200を同一分類のロールと権限 LDAP User 0297と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は過剰ロール付与を避けるため・主操作で出力欄を評価するしてGuardAを照合する。
    - B. 構成を確認する際の意味はプール宛先の誤読を避けるため・実行結果照合でプール宛先を確認するしてプール宛先を照合する。
    - C. 構成を確認する際の意味は対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするして監査タスクを照合する。 ✅
    - D. 構成を確認する際の意味は最終応答停止の見落としを避けるため・確認操作で状態欄を整理するしてカーネル監視を照合する。S-TAP監視 Last Response 0082固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能監査タ・対象デでCの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・登録）です。照合監査タ・登録に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・登録・対象デです。比較監査レ・登録でA:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸はCli・登録・監査タです。運用登録・CliでB:の実行結果照合 プール宛先は「I/O 指標を収集するサポートCLIコマンド」を述べるため、正答側の照合軸は監査タ・監査レ・登録です。仕様監査タ・登録でD:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸は登録・対象デ・監査タです。用語監査タ・登録という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0200**

    - 検証目的: 監査レポートの監査レポート Client IP 0200について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.10
    Server IP 198.51.100.40
    Count 90
    確認コード GDP12DD0200A
    ```

    画面・出力には GDP12DD0200A が表示され、監査レポート Client IP 0200 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0200
    Process Type Report
    Status completed
    確認コード GDP12DD0200B
    ```

    画面・出力には GDP12DD0200B が表示され、監査レポート Client IP 0200 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0200C
    ```

    画面・出力には GDP12DD0200C が表示され、監査レポート Client IP 0200 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0200A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0200B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0200C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0215 {#c10-i0419}
*分類: レポート*  ・  難易度: 中級

金P登録0216ではIBM Guardium Data Protection 12.x の レポートを扱う採取票金P登録0216です。金P登録0216は監査レポートの表示操作で監査レポートの対象欄を追跡する記録金P登録0216です。金P登録0216では監査タスクと取得時刻を採取票金P登録0216へ残します。金P登録0216ではジョブ失敗の見落としを避けるため補助資料も照合する判断金P登録0216です。金P登録0216の用語整理では監査レポートの対象値を実在出力で照合する記録金P登録0216です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0215の設定や表示を読む前に役割を確認します。ロールと権限 Permission 0258ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは変更確認操作で採取欄を棚卸することで表示可能レポを確認し・ディレクトリー取込対象の誤りを防ぐ。
    - B. 状態を読み取るための働きは表示操作で対象欄を追跡することで監査タスクを確認し・ジョブ失敗の見落としを防ぐ。 ✅
    - C. 状態を読み取るための働きは作業一覧からStatusを読むことで作業一覧を確認し・実行間隔より短いFROM/Tを防ぐ。
    - D. 状態を読み取るための働きは復旧操作で点検欄を確認することでユーザー活動を確認し・監査タスク未レビューを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能監査タ・ジョブでBの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・登録）です。照合監査タ・登録に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・登録・ジョブです。比較監査レ・登録でA:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はCli・登録・監査タです。項目監査タ・登録でC:の性能影響の確認 AUDIT11は「Audit Processで作業一覧から」を述べるため、正答側の照合軸はジョブ・監査レ・監査タです。仕様監査タ・登録でD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は登録・ジョブ・監査タです。用語監査タ・登録という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0215**

    - 検証目的: 監査レポートの監査レポート Client IP 0215について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.25
    Server IP 198.51.100.55
    Count 105
    確認コード GDP12DD0215A
    ```

    画面・出力には GDP12DD0215A が表示され、監査レポート Client IP 0215 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0215
    Process Type Report
    Status completed
    確認コード GDP12DD0215B
    ```

    画面・出力には GDP12DD0215B が表示され、監査レポート Client IP 0215 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0215C
    ```

    画面・出力には GDP12DD0215C が表示され、監査レポート Client IP 0215 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0215A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0215B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0215C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0230 {#c10-i0420}
*分類: レポート*  ・  難易度: 上級

紺K確認0231ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紺K確認0231です。紺K確認0231は監査レポートの点検操作で監査レポートの判定欄を記録する記録紺K確認0231です。紺K確認0231では監査タスクと取得時刻を採取票紺K確認0231へ残します。紺K確認0231ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紺K確認0231です。紺K確認0231の用語整理では監査レポートの対象値を実在出力で保管する記録紺K確認0231です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0230に関する障害切り分けの前提を確認しています。S-TAP監視 Last Response 0292の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはローカル通信制御監視の未確認を避けるため・保守操作で監査欄を保存するしてカーネル監視を照合する。
    - B. 機能の説明としては照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するして監査タスクを照合する。 ✅
    - C. 機能の説明としては集約遅延中の期間を監査完了としてを避けるため・集約エラーからAggregationを読して集約エラーを照合する。
    - D. 機能の説明としては照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するしてユーザー活動を照合する。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能監査タ・照会文でBの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・確認）です。照合監査タ・確認に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・確認・照会文です。比較監査レ・確認でA:のLast Responseは「監視エージェントのカーネル監視有無と取得時刻」を述べるため、正答側の照合軸はCli・確認・監査タです。項目監査タ・確認でC:の代替経路の確認 AGG10は「Aggregatorで集約エラーから」を述べるため、正答側の照合軸は照会文・監査レ・監査タです。仕様監査タ・確認でD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は確認・照会文・監査タです。用語監査タ・確認という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0230**

    - 検証目的: 監査レポートの監査レポート Client IP 0230について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.40
    Server IP 198.51.100.70
    Count 120
    確認コード GDP12DD0230A
    ```

    画面・出力には GDP12DD0230A が表示され、監査レポート Client IP 0230 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0230
    Process Type Report
    Status completed
    確認コード GDP12DD0230B
    ```

    画面・出力には GDP12DD0230B が表示され、監査レポート Client IP 0230 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0230C
    ```

    画面・出力には GDP12DD0230C が表示され、監査レポート Client IP 0230 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0230A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0230B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0230C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0245 {#c10-i0421}
*分類: レポート*  ・  難易度: 初級

銀F保護0246ではIBM Guardium Data Protection 12.x の レポートを扱う採取票銀F保護0246です。銀F保護0246は監査レポートの復旧操作で監査レポートの点検欄を確認する記録銀F保護0246です。銀F保護0246では監査タスクと取得時刻を採取票銀F保護0246へ残します。銀F保護0246では監査タスク未レビューを避けるため補助資料も照合する判断銀F保護0246です。銀F保護0246の用語整理では監査レポートの対象値を実在出力で点検する記録銀F保護0246です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0245を保守記録に説明する必要があります。S-TAP監視 KTAP Installed 0319と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして監視エージェを照合する。
    - B. 運用時に利用する技術的役割は実行間隔より短いFROM/TO範を避けるため・報告上限からmax_audit_repoして報告上限を照合する。
    - C. 運用時に利用する技術的役割は過剰ロール付与を避けるため・主操作で出力欄を評価するしてロール割当を照合する。
    - D. 運用時に利用する技術的役割は監査タスク未レビューを避けるため・復旧操作で点検欄を確認するして監査タスクを照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能監査タ・監査タでDの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・保護）です。照合監査タ・保護に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・保護・監査タです。比較監査レ・保護でA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はCli・保護・監査タです。運用保護・CliでB:の監査証跡の保存 AUDIT18は「Audit Processで報告上限から」を述べるため、正答側の照合軸は監査タ・監査レ・保護です。項目監査タ・保護でC:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸は監査タ・監査レ・監査タです。用語監査タ・保護という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0245**

    - 検証目的: 監査レポートの監査レポート Client IP 0245について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.15
    Server IP 198.51.100.25
    Count 15
    確認コード GDP12DD0245A
    ```

    画面・出力には GDP12DD0245A が表示され、監査レポート Client IP 0245 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0245
    Process Type Report
    Status completed
    確認コード GDP12DD0245B
    ```

    画面・出力には GDP12DD0245B が表示され、監査レポート Client IP 0245 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0245C
    ```

    画面・出力には GDP12DD0245C が表示され、監査レポート Client IP 0245 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0245A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0245B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0245C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0260 {#c10-i0422}
*分類: レポート*  ・  難易度: 初級

蒼A照合0261ではIBM Guardium Data Protection 12.x の レポートを扱う採取票蒼A照合0261です。蒼A照合0261は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録蒼A照合0261です。蒼A照合0261では監査タスクと取得時刻を採取票蒼A照合0261へ残します。蒼A照合0261では対象データソースの取り違えを避けるため補助資料も照合する判断蒼A照合0261です。蒼A照合0261の用語整理では監査レポートの対象値を実在出力で整理する記録蒼A照合0261です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0260の技術的な意味を資料で確認するとき、ロールと権限 Application Access 0345との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は調査操作で保守欄を引き継ぎすることで監査タスクを確認し・対象データソースの取り違えを防ぐ。 ✅
    - B. 構成を確認する際の意味は主操作で出力欄を評価することでユーザー有効を確認し・過剰ロール付与を防ぐ。
    - C. 構成を確認する際の意味は監視プロセスからApplianceを読むことで監視プロセスを確認し・ディスク逼迫中に検査データ流を防ぐ。
    - D. 構成を確認する際の意味は保守操作で監査欄を保存することで承認クライアを確認し・ローカル通信制御監視の未確認を防ぐ。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能監査タ・対象デでAの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・照合）です。照合監査タ・照合に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・照合・対象デです。運用照合・CliでB:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は監査タ・監査レ・照合です。項目監査タ・照合でC:のログとの照合 APP07は「Appliance Monitoriで監視プ」を述べるため、正答側の照合軸は対象デ・監査レ・監査タです。仕様監査タ・照合でD:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は照合・対象デ・監査タです。用語監査タ・照合という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0260**

    - 検証目的: 監査レポートの監査レポート Client IP 0260について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.30
    Server IP 198.51.100.40
    Count 30
    確認コード GDP12DD0260A
    ```

    画面・出力には GDP12DD0260A が表示され、監査レポート Client IP 0260 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0260
    Process Type Report
    Status completed
    確認コード GDP12DD0260B
    ```

    画面・出力には GDP12DD0260B が表示され、監査レポート Client IP 0260 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0260C
    ```

    画面・出力には GDP12DD0260C が表示され、監査レポート Client IP 0260 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0260A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0260B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0260C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0275 {#c10-i0423}
*分類: レポート*  ・  難易度: 中級

金P照合0276ではIBM Guardium Data Protection 12.x の レポートを扱う採取票金P照合0276です。金P照合0276は監査レポートの表示操作で監査レポートの対象欄を追跡する記録金P照合0276です。金P照合0276では監査タスクと取得時刻を採取票金P照合0276へ残します。金P照合0276ではジョブ失敗の見落としを避けるため補助資料も照合する判断金P照合0276です。金P照合0276の用語整理では監査レポートの対象値を実在出力で照合する記録金P照合0276です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0275について構成や状態を確認します。ロールと権限 LDAP User 0312ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはディレクトリー UserのGuardAPI権限と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。
    - B. 状態を読み取るための働きはClient IPの監査タスクと取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。 ✅
    - C. 状態を読み取るための働きはCentral Managerで依存関係の確認では中央管理サーバーの 管理単位状態からである。依存関係確認で確認では中央を確認するときはmanaged unitからを防ぐ。
    - D. 状態を読み取るための働きは監視エージェントの承認クライアントと取得時刻を記録し・ローカル通信制御監視の未確認を防ぐである。保守操作で監査欄を保存するときはローカル通信制御監視の未確認を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能監査タ・ジョブでBの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・照合）です。照合監査タ・照合に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・照合・ジョブです。比較監査レ・照合でA:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸はCli・照合・監査タです。項目監査タ・照合でC:の依存関係の確認 CM13は「Central Managerで依存関係の確」を述べるため、正答側の照合軸はジョブ・監査レ・監査タです。仕様監査タ・照合でD:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は照合・ジョブ・監査タです。用語監査タ・照合という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0275**

    - 検証目的: 監査レポートの監査レポート Client IP 0275について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.45
    Server IP 198.51.100.55
    Count 45
    確認コード GDP12DD0275A
    ```

    画面・出力には GDP12DD0275A が表示され、監査レポート Client IP 0275 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0275
    Process Type Report
    Status completed
    確認コード GDP12DD0275B
    ```

    画面・出力には GDP12DD0275B が表示され、監査レポート Client IP 0275 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0275C
    ```

    画面・出力には GDP12DD0275C が表示され、監査レポート Client IP 0275 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0275A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0275B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0275C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0290 {#c10-i0424}
*分類: レポート*  ・  難易度: 中級

紺K抑止0291ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紺K抑止0291です。紺K抑止0291は監査レポートの点検操作で監査レポートの判定欄を記録する記録紺K抑止0291です。紺K抑止0291では監査タスクと取得時刻を採取票紺K抑止0291へ残します。紺K抑止0291ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紺K抑止0291です。紺K抑止0291の用語整理では監査レポートの対象値を実在出力で保管する記録紺K抑止0291です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0290の役割を調べています。collector 証跡採取 証明書検査の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはS-TAP や外部接続から監査データを受け取る Guardium 装置を証跡採取として確認する。証跡採取で証明書検査を確認するときは証明書検査の誤読を防ぐ。
    - B. 機能の説明としてはCentral Managerで性能影響の確認では中央管理サーバーの 例外レポートから Exceptionである。性能影響確認で確認では中央を確認するときはmanaged unitからを防ぐ。
    - C. 機能の説明としては照会文 Verbのジョブキューと取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。
    - D. 機能の説明としてはClient IPの監査タスクと取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能監査タ・照会文でDの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・抑止）です。照合監査タ・抑止に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・抑止・照会文です。比較監査レ・抑止でA:の証跡採取 証明書検査は「S-TAP や外部接続から監査データを受け取」を述べるため、正答側の照合軸はCli・抑止・監査タです。運用抑止・CliでB:の性能影響の確認 CM11は「Central Managerで性能影響の確」を述べるため、正答側の照合軸は監査タ・監査レ・抑止です。項目監査タ・抑止でC:のSQL Verbは「照会文 Verbのジョブキューと取得時刻を記」を述べるため、正答側の照合軸は照会文・監査レ・監査タです。用語監査タ・抑止という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0290**

    - 検証目的: 監査レポートの監査レポート Client IP 0290について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.60
    Server IP 198.51.100.70
    Count 60
    確認コード GDP12DD0290A
    ```

    画面・出力には GDP12DD0290A が表示され、監査レポート Client IP 0290 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0290
    Process Type Report
    Status completed
    確認コード GDP12DD0290B
    ```

    画面・出力には GDP12DD0290B が表示され、監査レポート Client IP 0290 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0290C
    ```

    画面・出力には GDP12DD0290C が表示され、監査レポート Client IP 0290 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0290A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0290B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0290C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0305 {#c10-i0425}
*分類: レポート*  ・  難易度: 中級

銀F解析0306ではIBM Guardium Data Protection 12.x の レポートを扱う採取票銀F解析0306です。銀F解析0306は監査レポートの復旧操作で監査レポートの点検欄を確認する記録銀F解析0306です。銀F解析0306では監査タスクと取得時刻を採取票銀F解析0306へ残します。銀F解析0306では監査タスク未レビューを避けるため補助資料も照合する判断銀F解析0306です。銀F解析0306の用語整理では監査レポートの対象値を実在出力で点検する記録銀F解析0306です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート Client IP 0305」を「Central Manager 承認履歴確認 構成配布」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は承認履歴確認で構成配布を証跡に残し・管理対象システムの構成と配布を統制する管理点を承認履歴確認す。
    - B. 運用時に利用する技術的役割は世代整合確認でポリシー変更を証跡に残し・Inspection Engineでポリシー変更から。
    - C. 運用時に利用する技術的役割は解析で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。 ✅
    - D. 運用時に利用する技術的役割は保守でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能監査タ・監査タでCの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・解析）です。照合監査タ・解析に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・解析・監査タです。比較監査レ・解析でA:の承認履歴確認 構成配布は「管理対象システムの構成と配布を統制する管理点」を述べるため、正答側の照合軸はCli・解析・監査タです。運用解析・CliでB:の世代整合の確認 IE17は「Inspection Engineでポリシー」を述べるため、正答側の照合軸は監査タ・監査レ・解析です。仕様監査タ・解析でD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は解析・監査タ・監査タです。用語監査タ・解析という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0305**

    - 検証目的: 監査レポートの監査レポート Client IP 0305について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.75
    Server IP 198.51.100.25
    Count 75
    確認コード GDP12DD0305A
    ```

    画面・出力には GDP12DD0305A が表示され、監査レポート Client IP 0305 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0305
    Process Type Report
    Status completed
    確認コード GDP12DD0305B
    ```

    画面・出力には GDP12DD0305B が表示され、監査レポート Client IP 0305 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0305C
    ```

    画面・出力には GDP12DD0305C が表示され、監査レポート Client IP 0305 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0305A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0305B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0305C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0320 {#c10-i0426}
*分類: レポート*  ・  難易度: 中級

蒼A計画0321ではIBM Guardium Data Protection 12.x の レポートを扱う採取票蒼A計画0321です。蒼A計画0321は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録蒼A計画0321です。蒼A計画0321では監査タスクと取得時刻を採取票蒼A計画0321へ残します。蒼A計画0321では対象データソースの取り違えを避けるため補助資料も照合する判断蒼A計画0321です。蒼A計画0321の用語整理では監査レポートの対象値を実在出力で整理する記録蒼A計画0321です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0320を同一分類のcollector 承認履歴確認 伝搬経路と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は計画で監査タスクを証跡に残し・Client IPの監査タスクと取得時刻を記録し。 ✅
    - B. 構成を確認する際の意味は承認履歴確認で伝搬経路を証跡に残し・S-TAP や外部接続から監査データを受け取る。
    - C. 構成を確認する際の意味は復旧でデータソースを証跡に残し・Server IPのデータソースと取得時刻を記録し。
    - D. 構成を確認する際の意味は収集で表示可能レポを証跡に残し・Permissionの表示可能レポートと取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能監査タ・対象デでAの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・計画）です。照合監査タ・計画に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・計画・対象デです。運用計画・CliでB:の承認履歴確認 伝搬経路は「S-TAP や外部接続から監査データを受け取」を述べるため、正答側の照合軸は監査タ・監査レ・計画です。項目監査タ・計画でC:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸は対象デ・監査レ・監査タです。仕様監査タ・計画でD:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸は計画・対象デ・監査タです。用語監査タ・計画という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0320**

    - 検証目的: 監査レポートの監査レポート Client IP 0320について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.10
    Server IP 198.51.100.40
    Count 90
    確認コード GDP12DD0320A
    ```

    画面・出力には GDP12DD0320A が表示され、監査レポート Client IP 0320 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0320
    Process Type Report
    Status completed
    確認コード GDP12DD0320B
    ```

    画面・出力には GDP12DD0320B が表示され、監査レポート Client IP 0320 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0320C
    ```

    画面・出力には GDP12DD0320C が表示され、監査レポート Client IP 0320 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0320A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0320B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0320C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0335 {#c10-i0427}
*分類: レポート*  ・  難易度: 中級

金P計画0336ではIBM Guardium Data Protection 12.x の レポートを扱う採取票金P計画0336です。金P計画0336は監査レポートの表示操作で監査レポートの対象欄を追跡する記録金P計画0336です。金P計画0336では監査タスクと取得時刻を採取票金P計画0336へ残します。金P計画0336ではジョブ失敗の見落としを避けるため補助資料も照合する判断金P計画0336です。金P計画0336の用語整理では監査レポートの対象値を実在出力で照合する記録金P計画0336です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0335の設定や表示を読む前に役割を確認します。support gather_io_metrics 障害時切り分け 出力見出しではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは出力見出しの誤読を避けるため・レポートで出力見出しを確認するして出力見出しを照合する。
    - B. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するして監査タスクを照合する。 ✅
    - C. 状態を読み取るための働きは対象データソースの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてユーザー活動を照合する。
    - D. 状態を読み取るための働きはカーネル監視導入状態の誤読を避けるため・採取操作で照合欄を点検するして暗号化表示を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能監査タ・ジョブでBの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・計画）です。照合監査タ・計画に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・計画・ジョブです。比較監査レ・計画でA:の障害時切り分け 出力見出しは「I/O 指標を収集するサポートCLIコマンド」を述べるため、正答側の照合軸はCli・計画・監査タです。項目監査タ・計画でC:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸はジョブ・監査レ・監査タです。仕様監査タ・計画でD:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸は計画・ジョブ・監査タです。用語監査タ・計画という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0335**

    - 検証目的: 監査レポートの監査レポート Client IP 0335について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.25
    Server IP 198.51.100.55
    Count 105
    確認コード GDP12DD0335A
    ```

    画面・出力には GDP12DD0335A が表示され、監査レポート Client IP 0335 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0335
    Process Type Report
    Status completed
    確認コード GDP12DD0335B
    ```

    画面・出力には GDP12DD0335B が表示され、監査レポート Client IP 0335 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0335C
    ```

    画面・出力には GDP12DD0335C が表示され、監査レポート Client IP 0335 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0335A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0335B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0335C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート Client IP 0350 {#c10-i0428}
*分類: レポート*  ・  難易度: 上級

紺K解除0351ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紺K解除0351です。紺K解除0351は監査レポートの点検操作で監査レポートの判定欄を記録する記録紺K解除0351です。紺K解除0351では監査タスクと取得時刻を採取票紺K解除0351へ残します。紺K解除0351ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断紺K解除0351です。紺K解除0351の用語整理では監査レポートの対象値を実在出力で保管する記録紺K解除0351です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート Client IP 0350に関する障害切り分けの前提を確認しています。aggregator 状態確認 スケジュールの機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては状態確認でスケジュールを確認することでスケジュールを確認し・スケジュールの誤読を防ぐ。
    - B. 機能の説明としては点検操作で判定欄を記録することで監査タスクを確認し・照会文動詞集計の期間誤りを防ぐ。 ✅
    - C. 機能の説明としては採取操作で照合欄を点検することで最終応答を確認し・カーネル監視導入状態の誤読を防ぐ。
    - D. 機能の説明としては調査操作で保守欄を引き継ぎすることでユーザー活動を確認し・対象データソースの取り違えを防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能監査タ・照会文でBの記述「Client IPの監査タスクと取得時刻を記録し」に対応する項目はClient IP（Cli・監査タ・解除）です。照合監査タ・解除に関するレポートの仕様は「Client IPの監査タスクと取得時刻を記録し」で、確認対象は監査タ・解除・照会文です。比較監査レ・解除でA:の状態確認 スケジュールは「複数 collector の監査情報を集約し」を述べるため、正答側の照合軸はCli・解除・監査タです。項目監査タ・解除でC:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は照会文・監査レ・監査タです。仕様監査タ・解除でD:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は解除・照会文・監査タです。用語監査タ・解除という用語は「Client IPの監査タスクと取得時刻を記録し」を指し、照合する値と誤認リスクの組合せは監査レ・監査タ・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート Client IP 0350**

    - 検証目的: 監査レポートの監査レポート Client IP 0350について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Client IP と 監査タスク
    - セッション環境: 机上検証。IBM Guardium Data Protection 12.xのコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    SQL Verb SELECT
    Client IP 192.0.2.40
    Server IP 198.51.100.70
    Count 120
    確認コード GDP12DD0350A
    ```

    画面・出力には GDP12DD0350A が表示され、監査レポート Client IP 0350 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面またはコマンド環境
    COMMAND ===> SQL Verb report
    → Enter を押す
    ```

    画面・出力:
    ```text
    Guardium Job Queue
    Process Run ID GDP0350
    Process Type Report
    Status completed
    確認コード GDP12DD0350B
    ```

    画面・出力には GDP12DD0350B が表示され、監査レポート Client IP 0350 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの確認画面またはコマンド結果です。Client IP を読むため、監査レポート の対象値を表示します。
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
    確認コード GDP12DD0350C
    ```

    画面・出力には GDP12DD0350C が表示され、監査レポート Client IP 0350 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0350A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0350B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0350C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0014 {#c10-i0429}
*分類: レポート*  ・  難易度: 初級

翠O巡回0015ではIBM Guardium Data Protection 12.x の レポートを扱う採取票翠O巡回0015です。翠O巡回0015は監査レポートの点検操作で監査レポートの判定欄を記録する記録翠O巡回0015です。翠O巡回0015ではSQL動詞集計と取得時刻を採取票翠O巡回0015へ残します。翠O巡回0015ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断翠O巡回0015です。翠O巡回0015の用語整理では監査レポートの対象値を実在出力で保管する記録翠O巡回0015です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0014に関する障害切り分けの前提を確認しています。ロールと権限 Permission 0033の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては過剰ロール付与を避けるため・主操作で出力欄を評価するして表示可能レポを照合する。
    - B. 機能の説明としてはディレクトリー取込対象の誤りを避けるため・変更確認操作で採取欄を棚卸するしてGuardAを照合する。
    - C. 機能の説明としては履歴行の誤読を避けるため・状態確認で履歴行を確認するして履歴行を照合する。
    - D. 機能の説明としては照会文動詞集計の期間誤りを避けるため・点検操作で判定欄を記録するして照会文動詞集を照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 巡回対象照会文動詞でDの記述「DB User NameのSQL動詞集計と取得時刻を記録し」に対応する項目はUser Name（データベー・巡回・照会文・照会文動）です。巡回時の照会文動詞に関するレポートの仕様は「DB User NameのSQL動詞集計と取得時刻を記録し」で、確認対象はデータベ・巡回・照会文・照会文動です。Pe・棚卸・表示可能のA:は「Permissionの表示可能レポートと取得時刻を記録し」を述べ、対象はロールと権限 Permission（Permi・棚卸・表示可・過剰ロー）です。抑止対象GuardのB:は「LDAP UserのGuardAPI権限と取得時刻を記録し」を述べ、対象はLDAP User（ディレクト・抑止・Gua・ディレク）です。状態確認時の履歴行のC:は「データベース通信を解析し監査レコードを作る処理」を述べ、対象は状態確認 履歴行（inspe・状態確・履歴行・履歴行の）です。照会文動詞を巡回という用語は「DB User NameのSQL動詞集計と取得時刻を」を指し、User Name（データベー・巡回・照会文・照会文動）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0014**

    - 検証目的: 監査レポートの監査レポート DB User Name 0014について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0014A
    ```

    画面・出力には GDP12DD0014A が表示され、監査レポート DB User Name 0014 の入力欄確認を確認できます。

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
    Process Run ID GDP0014
    Process Type Report
    Status completed
    確認コード GDP12DD0014B
    ```

    画面・出力には GDP12DD0014B が表示され、監査レポート DB User Name 0014 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0014C
    ```

    画面・出力には GDP12DD0014C が表示され、監査レポート DB User Name 0014 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0014A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0014B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0014C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0029 {#c10-i0430}
*分類: レポート*  ・  難易度: 中級

朱J棚卸0030ではIBM Guardium Data Protection 12.x の レポートを扱う採取票朱J棚卸0030です。朱J棚卸0030は監査レポートの復旧操作で監査レポートの点検欄を確認する記録朱J棚卸0030です。朱J棚卸0030ではSQL動詞集計と取得時刻を採取票朱J棚卸0030へ残します。朱J棚卸0030では監査タスク未レビューを避けるため補助資料も照合する判断朱J棚卸0030です。朱J棚卸0030の用語整理では監査レポートの対象値を実在出力で点検する記録朱J棚卸0030です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0029を保守記録に説明する必要があります。S-TAP監視 S-TAP Host 0061と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は棚卸で照会文動詞集を証跡に残し・DB User NameのSQL動詞集計と取得時刻を記録し。 ✅
    - B. 運用時に利用する技術的役割は監査で最終応答を証跡に残し・S-TAPの最終応答と取得時刻を記録し。
    - C. 運用時に利用する技術的役割は登録でユーザー活動を証跡に残し・Audit Task Statusのユーザー活動と取得時刻を。
    - D. 運用時に利用する技術的役割は監査プロセスで障害切り分けを証跡に残し・Audit Processで障害切り分けでは監査プロセスの。

    正解: **A** ／ 難易度: 中級

    **解説:** 棚卸対象照会文動詞でAの記述「DB User NameのSQL動詞集計と取得時刻を記録し」に対応する項目はUser Name（データベー・棚卸・照会文・監査タス）です。棚卸時の照会文動詞に関するレポートの仕様は「DB User NameのSQL動詞集計と取得時刻を記録し」で、確認対象はデータベ・棚卸・照会文・監査タスです。監査対象最終応答のB:は「S-TAPの最終応答と取得時刻を記録し、未承認S-TAP接続を防ぐ」を述べ、対象はS-TAP Host（監視エージ・監査・最終応・未承認監）です。登録時のユーザー活のC:は「Audit Task Statusのユーザー活動と取得時刻を記録し」を述べ、対象はTask Status（Audit・登録・ユーザ・照会文動）です。障害切り分を監査プロセのD:は「Audit Processで障害切り分けでは監査プロセスの」を述べ、対象は障害切り分け AUDIT04（Audit・監査プ・障害切・実行間隔）です。照会文動詞を棚卸という用語は「DB User NameのSQL動詞集計と取得時刻を」を指し、User Name（データベー・棚卸・照会文・監査タス）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0029**

    - 検証目的: 監査レポートの監査レポート DB User Name 0029について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0029A
    ```

    画面・出力には GDP12DD0029A が表示され、監査レポート DB User Name 0029 の入力欄確認を確認できます。

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
    Process Run ID GDP0029
    Process Type Report
    Status completed
    確認コード GDP12DD0029B
    ```

    画面・出力には GDP12DD0029B が表示され、監査レポート DB User Name 0029 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0029C
    ```

    画面・出力には GDP12DD0029C が表示され、監査レポート DB User Name 0029 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0029A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0029B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0029C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0044 {#c10-i0431}
*分類: レポート*  ・  難易度: 中級

紅E復旧0045ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紅E復旧0045です。紅E復旧0045は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録紅E復旧0045です。紅E復旧0045ではSQL動詞集計と取得時刻を採取票紅E復旧0045へ残します。紅E復旧0045では対象データソースの取り違えを避けるため補助資料も照合する判断紅E復旧0045です。紅E復旧0045の用語整理では監査レポートの対象値を実在出力で整理する記録紅E復旧0045です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0044の技術的な意味を資料で確認するとき、ロールと権限 LDAP User 0057との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は復旧でGuardAを証跡に残し・LDAP UserのGuardAPI権限と取得時刻を記録し。
    - B. 構成を確認する際の意味は復旧で照会文動詞集を証跡に残し・DB User NameのSQL動詞集計と取得時刻を記録し。 ✅
    - C. 構成を確認する際の意味は抑止で暗号化表示を証跡に残し・S-TAPの暗号化表示と取得時刻を記録し。
    - D. 構成を確認する際の意味は監査プロセスで引継ぎ記録でを証跡に残し・Audit Processで引継ぎ記録では監査プロセスの。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧対象照会文動詞でBの記述「DB User NameのSQL動詞集計と取得時刻を記録し」に対応する項目はUser Name（データベー・復旧・照会文・対象デー）です。復旧時の照会文動詞に関するレポートの仕様は「DB User NameのSQL動詞集計と取得時刻を記録し」で、確認対象はデータベ・復旧・照会文・対象デーです。ディ・復旧・GuarのA:は「LDAP UserのGuardAPI権限と取得時刻を記録し」を述べ、対象はLDAP User（ディレクト・復旧・Gua・過剰ロー）です。抑止時の暗号化表示のC:は「S-TAPの暗号化表示と取得時刻を記録し」を述べ、対象はS-TAP Version（監視エージ・抑止・暗号化・カーネル）です。引継ぎ記録を監査プロセのD:は「Audit Processで引継ぎ記録では監査プロセスの」を述べ、対象は引継ぎ記録 AUDIT09（Audit・監査プ・引継ぎ・実行間隔）です。照会文動詞を復旧という用語は「DB User NameのSQL動詞集計と取得時刻を」を指し、User Name（データベー・復旧・照会文・対象デー）に該当します。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0044**

    - 検証目的: 監査レポートの監査レポート DB User Name 0044について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0044A
    ```

    画面・出力には GDP12DD0044A が表示され、監査レポート DB User Name 0044 の入力欄確認を確認できます。

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
    Process Run ID GDP0044
    Process Type Report
    Status completed
    確認コード GDP12DD0044B
    ```

    画面・出力には GDP12DD0044B が表示され、監査レポート DB User Name 0044 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0044C
    ```

    画面・出力には GDP12DD0044C が表示され、監査レポート DB User Name 0044 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0044A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0044B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0044C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0059 {#c10-i0432}
*分類: レポート*  ・  難易度: 中級

空T復旧0060ではIBM Guardium Data Protection 12.x の レポートを扱う採取票空T復旧0060です。空T復旧0060は監査レポートの表示操作で監査レポートの対象欄を追跡する記録空T復旧0060です。空T復旧0060ではSQL動詞集計と取得時刻を採取票空T復旧0060へ残します。空T復旧0060ではジョブ失敗の見落としを避けるため補助資料も照合する判断空T復旧0060です。空T復旧0060の用語整理では監査レポートの対象値を実在出力で照合する記録空T復旧0060です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0059について構成や状態を確認します。S-TAP監視 KTAP Installed 0094ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは最終応答停止の見落としを避けるため・確認操作で状態欄を整理するして監視エージェを照合する。
    - B. 状態を読み取るための働きはGuardAPI実行権限不足を避けるため・監査操作で記録欄を比較するしてGuardAを照合する。
    - C. 状態を読み取るための働きは高速伝搬の誤読を避けるため・承認履歴確認で高速伝搬を確認するして高速伝搬を照合する。
    - D. 状態を読み取るための働きはジョブ失敗の見落としを避けるため・表示操作で対象欄を追跡するして照会文動詞集を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能照会文・ジョブでDの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・復旧）です。照合照会文・復旧に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・復旧・ジョブです。比較監査レ・復旧でA:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸はデータ・復旧・照会文です。運用復旧・データでB:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は照会文・監査レ・復旧です。項目照会文・復旧でC:の承認履歴確認 高速伝搬は「監査結果のレビューと承認の履歴を承認履歴確認」を述べるため、正答側の照合軸はジョブ・監査レ・照会文です。用語照会文・復旧という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0059**

    - 検証目的: 監査レポートの監査レポート DB User Name 0059について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0059A
    ```

    画面・出力には GDP12DD0059A が表示され、監査レポート DB User Name 0059 の入力欄確認を確認できます。

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
    Process Run ID GDP0059
    Process Type Report
    Status completed
    確認コード GDP12DD0059B
    ```

    画面・出力には GDP12DD0059B が表示され、監査レポート DB User Name 0059 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0059C
    ```

    画面・出力には GDP12DD0059C が表示され、監査レポート DB User Name 0059 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0059A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0059B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0059C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0074 {#c10-i0433}
*分類: レポート*  ・  難易度: 中級

翠O監査0075ではIBM Guardium Data Protection 12.x の レポートを扱う採取票翠O監査0075です。翠O監査0075は監査レポートの点検操作で監査レポートの判定欄を記録する記録翠O監査0075です。翠O監査0075ではSQL動詞集計と取得時刻を採取票翠O監査0075へ残します。翠O監査0075ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断翠O監査0075です。翠O監査0075の用語整理では監査レポートの対象値を実在出力で保管する記録翠O監査0075です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0074の役割を調べています。S-TAP監視 DB Server Type 0130の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはデータベース User Nameの照会文動詞集計と取得時刻を記録し・照会文動詞集計の期間誤りを防ぐである。点検操作で判定欄を記録するときは照会文動詞集計の期間誤りを防ぐ。 ✅
    - B. 機能の説明としては監視エージェントの承認クライアントと取得時刻を記録し・最終応答停止の見落としを防ぐである。確認操作で状態欄を整理するときは最終応答停止の見落としを防ぐ。
    - C. 機能の説明としてはディレクトリー UserのGuardAPI権限と取得時刻を記録し・ディレクトリー取込対象の誤りを防ぐである。変更確認操作で採取欄を棚卸するときはディレクトリー取込対象の誤りを防ぐ。
    - D. 機能の説明としてはCentral Managerで通常状態の確認では中央管理サーバーの 管理単位状態からである。通常状態確認で確認では中央を確認するときはmanaged unitからを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能照会文・照会文でAの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・監査）です。照合照会文・監査に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・監査・照会文です。運用監査・データでB:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸は照会文・監査レ・監査です。項目照会文・監査でC:のLDAP Userは「ディレクトリー UserのGuardAPI権」を述べるため、正答側の照合軸は照会文・監査レ・照会文です。仕様照会文・監査でD:の通常状態の確認 CM01は「Central Managerで通常状態の確」を述べるため、正答側の照合軸は監査・照会文・照会文です。用語照会文・監査という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0074**

    - 検証目的: 監査レポートの監査レポート DB User Name 0074について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0074A
    ```

    画面・出力には GDP12DD0074A が表示され、監査レポート DB User Name 0074 の入力欄確認を確認できます。

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
    Process Run ID GDP0074
    Process Type Report
    Status completed
    確認コード GDP12DD0074B
    ```

    画面・出力には GDP12DD0074B が表示され、監査レポート DB User Name 0074 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0074C
    ```

    画面・出力には GDP12DD0074C が表示され、監査レポート DB User Name 0074 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0074A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0074B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0074C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0089 {#c10-i0434}
*分類: レポート*  ・  難易度: 中級

朱J変更0090ではIBM Guardium Data Protection 12.x の レポートを扱う採取票朱J変更0090です。朱J変更0090は監査レポートの復旧操作で監査レポートの点検欄を確認する記録朱J変更0090です。朱J変更0090ではSQL動詞集計と取得時刻を採取票朱J変更0090へ残します。朱J変更0090では監査タスク未レビューを避けるため補助資料も照合する判断朱J変更0090です。朱J変更0090の用語整理では監査レポートの対象値を実在出力で点検する記録朱J変更0090です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 「監査レポート DB User Name 0089」を「S-TAP監視 DB Server Type 0130」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は確認操作で状態欄を整理することで承認クライアを確認し・最終応答停止の見落としを防ぐ。
    - B. 運用時に利用する技術的役割は復旧操作で点検欄を確認することで照会文動詞集を確認し・監査タスク未レビューを防ぐ。 ✅
    - C. 運用時に利用する技術的役割は照合操作で確認欄を採取することでユーザー有効を確認し・監査担当者の閲覧範囲不足を防ぐ。
    - D. 運用時に利用する技術的役割はジョブキューからJobNameを読むことでジョブキューを確認し・ディスク逼迫中に検査データ流を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能照会文・監査タでBの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・変更）です。照合照会文・変更に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・変更・監査タです。比較監査レ・変更でA:のServer Typeは「監視エージェントの承認クライアントと取得時刻」を述べるため、正答側の照合軸はデータ・変更・照会文です。項目照会文・変更でC:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸は監査タ・監査レ・照会文です。仕様照会文・変更でD:の再始動後の確認 APP15は「Appliance Monitoriでジョブ」を述べるため、正答側の照合軸は変更・監査タ・照会文です。用語照会文・変更という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0089**

    - 検証目的: 監査レポートの監査レポート DB User Name 0089について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0089A
    ```

    画面・出力には GDP12DD0089A が表示され、監査レポート DB User Name 0089 の入力欄確認を確認できます。

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
    Process Run ID GDP0089
    Process Type Report
    Status completed
    確認コード GDP12DD0089B
    ```

    画面・出力には GDP12DD0089B が表示され、監査レポート DB User Name 0089 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0089C
    ```

    画面・出力には GDP12DD0089C が表示され、監査レポート DB User Name 0089 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0089A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0089B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0089C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0104 {#c10-i0435}
*分類: レポート*  ・  難易度: 上級

紅E移行0105ではIBM Guardium Data Protection 12.x の レポートを扱う採取票紅E移行0105です。紅E移行0105は監査レポートの調査操作で監査レポートの保守欄を引き継ぎする記録紅E移行0105です。紅E移行0105ではSQL動詞集計と取得時刻を採取票紅E移行0105へ残します。紅E移行0105では対象データソースの取り違えを避けるため補助資料も照合する判断紅E移行0105です。紅E移行0105の用語整理では監査レポートの対象値を実在出力で整理する記録紅E移行0105です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0104を同一分類のロールと権限 Login Name 0114と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はLogin Nameのロール割当と取得時刻を記録し・ディレクトリー取込対象の誤りを防ぐである。変更確認操作で採取欄を棚卸するときはディレクトリー取込対象の誤りを防ぐ。
    - B. 構成を確認する際の意味は処理ID・状態・開始終了時刻・Data Sources を示すジョブ一覧を障害時切り分けとして確認する。Centraで同期範囲を確認するときは同期範囲の誤読を防ぐ。Guardium Job Queue 障害時切り分け 同期範囲固有の属性も確認対象に含める。
    - C. 構成を確認する際の意味はデータベース User Nameの照会文動詞集計と取得時刻を記録し・対象データソースの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは対象データソースの取り違えを防ぐ。 ✅
    - D. 構成を確認する際の意味はCentral Managerで依存関係の確認では中央管理サーバーの 管理単位状態からである。依存関係確認で確認では中央を確認するときはmanaged unitからを防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能照会文・対象デでCの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・移行）です。照合照会文・移行に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・移行・対象デです。比較監査レ・移行でA:のLogin Nameは「Login Nameのロール割当と取得時刻を」を述べるため、正答側の照合軸はデータ・移行・照会文です。運用移行・データでB:の障害時切り分け 同期範囲は「処理ID、状態、開始終了時刻、Data」を述べるため、正答側の照合軸は照会文・監査レ・移行です。仕様照会文・移行でD:の依存関係の確認 CM13は「Central Managerで依存関係の確」を述べるため、正答側の照合軸は移行・対象デ・照会文です。用語照会文・移行という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・対象デです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0104**

    - 検証目的: 監査レポートの監査レポート DB User Name 0104について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0104A
    ```

    画面・出力には GDP12DD0104A が表示され、監査レポート DB User Name 0104 の入力欄確認を確認できます。

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
    Process Run ID GDP0104
    Process Type Report
    Status completed
    確認コード GDP12DD0104B
    ```

    画面・出力には GDP12DD0104B が表示され、監査レポート DB User Name 0104 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0104C
    ```

    画面・出力には GDP12DD0104C が表示され、監査レポート DB User Name 0104 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0104A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0104B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0104C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0119 {#c10-i0436}
*分類: レポート*  ・  難易度: 上級

空T移行0120ではIBM Guardium Data Protection 12.x の レポートを扱う採取票空T移行0120です。空T移行0120は監査レポートの表示操作で監査レポートの対象欄を追跡する記録空T移行0120です。空T移行0120ではSQL動詞集計と取得時刻を採取票空T移行0120へ残します。空T移行0120ではジョブ失敗の見落としを避けるため補助資料も照合する判断空T移行0120です。空T移行0120の用語整理では監査レポートの対象値を実在出力で照合する記録空T移行0120です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0119の設定や表示を読む前に役割を確認します。ロールと権限 Application Access 0180ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはApplication Accessのユーザー有効化と取得時刻を記録し・監査担当者の閲覧範囲不足を防ぐである。照合操作で確認欄を採取するときは監査担当者の閲覧範囲不足を防ぐ。
    - B. 状態を読み取るための働きは監視エージェントの最終応答と取得時刻を記録し・未承認監視エージェント接続を防ぐである。記録操作で証跡欄を照合するときは未承認監視エージェント接続を防ぐ。
    - C. 状態を読み取るための働きはデータベース User Nameの照会文動詞集計と取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。 ✅
    - D. 状態を読み取るための働きはAppliance Monitoriでデータベース処理一覧から TURBINE を読み・TURBINE とである。DB処理一覧からTURBINEを読むときはディスク逼迫中に検査データ流を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能照会文・ジョブでCの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・移行）です。照合照会文・移行に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・移行・ジョブです。比較監査レ・移行でA:のApplicationは「Application Accessのユーザ」を述べるため、正答側の照合軸はデータ・移行・照会文です。運用移行・データでB:のS-TAP Hostは「監視エージェントの最終応答と取得時刻を記録し」を述べるため、正答側の照合軸は照会文・監査レ・移行です。仕様照会文・移行でD:の停止前の確認 APP14は「Appliance Monitoriでデータ」を述べるため、正答側の照合軸は移行・ジョブ・照会文です。用語照会文・移行という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・ジョブです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0119**

    - 検証目的: 監査レポートの監査レポート DB User Name 0119について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0119A
    ```

    画面・出力には GDP12DD0119A が表示され、監査レポート DB User Name 0119 の入力欄確認を確認できます。

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
    Process Run ID GDP0119
    Process Type Report
    Status completed
    確認コード GDP12DD0119B
    ```

    画面・出力には GDP12DD0119B が表示され、監査レポート DB User Name 0119 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0119C
    ```

    画面・出力には GDP12DD0119C が表示され、監査レポート DB User Name 0119 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0119A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0119B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0119C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0134 {#c10-i0437}
*分類: レポート*  ・  難易度: 初級

翠O診断0135ではIBM Guardium Data Protection 12.x の レポートを扱う採取票翠O診断0135です。翠O診断0135は監査レポートの点検操作で監査レポートの判定欄を記録する記録翠O診断0135です。翠O診断0135ではSQL動詞集計と取得時刻を採取票翠O診断0135へ残します。翠O診断0135ではSQL動詞集計の期間誤りを避けるため補助資料も照合する判断翠O診断0135です。翠O診断0135の用語整理では監査レポートの対象値を実在出力で保管する記録翠O診断0135です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0134に関する障害切り分けの前提を確認しています。ロールと権限 Permission 0138の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては変更確認操作で採取欄を棚卸することで表示可能レポを確認し・ディレクトリー取込対象の誤りを防ぐ。
    - B. 機能の説明としては証跡採取で統計値を確認することで統計値を確認し・統計値の誤読を防ぐ。
    - C. 機能の説明としては表示操作で対象欄を追跡することでユーザー活動を確認し・ジョブ失敗の見落としを防ぐ。
    - D. 機能の説明としては点検操作で判定欄を記録することで照会文動詞集を確認し・照会文動詞集計の期間誤りを防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能照会文・照会文でDの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・診断）です。照合照会文・診断に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・診断・照会文です。比較監査レ・診断でA:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸はデータ・診断・照会文です。運用診断・データでB:の証跡採取 統計値は「監査結果のレビューと承認の履歴を証跡採取とし」を述べるため、正答側の照合軸は照会文・監査レ・診断です。項目照会文・診断でC:のTask Statusは「Audit Task Statusのユーザー」を述べるため、正答側の照合軸は照会文・監査レ・照会文です。用語照会文・診断という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・照会文です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0134**

    - 検証目的: 監査レポートの監査レポート DB User Name 0134について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0134A
    ```

    画面・出力には GDP12DD0134A が表示され、監査レポート DB User Name 0134 の入力欄確認を確認できます。

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
    Process Run ID GDP0134
    Process Type Report
    Status completed
    確認コード GDP12DD0134B
    ```

    画面・出力には GDP12DD0134B が表示され、監査レポート DB User Name 0134 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0134C
    ```

    画面・出力には GDP12DD0134C が表示され、監査レポート DB User Name 0134 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0134A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0134B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0134C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査レポート DB User Name 0149 {#c10-i0438}
*分類: レポート*  ・  難易度: 中級

朱J保守0150ではIBM Guardium Data Protection 12.x の レポートを扱う採取票朱J保守0150です。朱J保守0150は監査レポートの復旧操作で監査レポートの点検欄を確認する記録朱J保守0150です。朱J保守0150ではSQL動詞集計と取得時刻を採取票朱J保守0150へ残します。朱J保守0150では監査タスク未レビューを避けるため補助資料も照合する判断朱J保守0150です。朱J保守0150の用語整理では監査レポートの対象値を実在出力で点検する記録朱J保守0150です。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査レポート DB User Name 0149を保守記録に説明する必要があります。S-TAP監視 S-TAP Version 0223と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は監視エージェントの暗号化表示と取得時刻を記録し・カーネル監視導入状態の誤読を防ぐである。採取操作で照合欄を点検するときはカーネル監視導入状態の誤読を防ぐ。
    - B. 運用時に利用する技術的役割は管理対象システムの構成と配布を統制する管理点である。状態確認で更新配布を確認するときは更新配布の誤読を防ぐ。
    - C. 運用時に利用する技術的役割はデータベース User Nameの照会文動詞集計と取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。 ✅
    - D. 運用時に利用する技術的役割はPermissionの表示可能レポートと取得時刻を記録し・GuardAPI実行権限不足を防ぐである。監査操作で記録欄を比較するときはGuardAPI実行権限不足を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能照会文・監査タでCの記述「データベース User Nameの照会文動詞集計と取得時」に対応する項目はUser Name（データ・照会文・保守）です。照合照会文・保守に関するレポートの仕様は「データベース User Nameの照会文動詞集計と取得時刻を記録し」で、確認対象は照会文・保守・監査タです。比較監査レ・保守でA:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はデータ・保守・照会文です。運用保守・データでB:の状態確認 更新配布は「管理対象システムの構成と配布を統制する管理点」を述べるため、正答側の照合軸は照会文・監査レ・保守です。仕様照会文・保守でD:のロールと権限 Permissioは「Permissionの表示可能レポートと取得」を述べるため、正答側の照合軸は保守・監査タ・照会文です。用語照会文・保守という用語は「データベース User Nameの照会文動詞集計と取」を指し、照合する値と誤認リスクの組合せは監査レ・照会文・監査タです。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査レポート DB User Name 0149**

    - 検証目的: 監査レポートの監査レポート DB User Name 0149について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード GDP12DD0149A
    ```

    画面・出力には GDP12DD0149A が表示され、監査レポート DB User Name 0149 の入力欄確認を確認できます。

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
    Process Run ID GDP0149
    Process Type Report
    Status completed
    確認コード GDP12DD0149B
    ```

    画面・出力には GDP12DD0149B が表示され、監査レポート DB User Name 0149 の証跡表示確認を確認できます。

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
    確認コード GDP12DD0149C
    ```

    画面・出力には GDP12DD0149C が表示され、監査レポート DB User Name 0149 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の GDP12DD0149A が画面・出力に表示されること
    ② ステップ2 の GDP12DD0149B が画面・出力に表示されること
    ③ ステップ3 の GDP12DD0149C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



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


