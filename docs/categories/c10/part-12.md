---
search:
  exclude: true
---

# IBM Guardium Data Protection 12.x — 詳細 (12/12)

[← IBM Guardium Data Protection 12.x の概要へ戻る](index.md)


## IBM Guardium Data Protection 12.x > 監査プロセス

### 監査プロセス Audit Process Builder 通常状態の確認 AUDIT01 {#c10-i0539}
*分類: 監査プロセス*  ・  難易度: 初級

通常状態の確認では 監査プロセス の プロセス一覧 を主操作として AUDIT01 を判定します。基準値と現在値の差への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT01 に残します。通常状態の確認を補助する 作業一覧 では Status を補助値として AUDIT01 へ保存します。主判定の通常状態の確認では監査プロセスの プロセス一覧 から Schedule を読み AUDIT01 へ残します。証跡照合の通常状態の確認では監査プロセスの Schedule と Status を AUDIT01 に保存します。記録対応の通常状態の確認では監査プロセスの ScheduleとTask Status の証跡へ AUDIT01 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 通常状態の確認 AUDIT01を保守記録に説明する必要があります。監査プロセス Audit Process Builder 停止前の確認と取り違えない説明はどれですか。

    - A. 仕様上の役割はAudit Processで作業一覧から Status を読み・Status とである。作業一覧からStatusを読むときは実行間隔より短いFROM/Tを防ぐ。
    - B. 仕様上の役割は監視エージェントの暗号化表示と取得時刻を記録し・ローカル通信制御監視の未確認を防ぐである。保守操作で監査欄を保存するときはローカル通信制御監視の未確認を防ぐ。
    - C. 仕様上の役割はAudit Processでプロセス一覧から Schedule を読み・Schedule と Statusである。プロセス一覧からScheduleを読ときは実行間隔より短いFROM/Tを防ぐ。 ✅
    - D. 仕様上の役割はデータベース User Nameの照会文動詞集計と取得時刻を記録し・ジョブ失敗の見落としを防ぐである。表示操作で対象欄を追跡するときはジョブ失敗の見落としを防ぐ。監査レポート DB User Name 0299固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能プロセ・実行間でCの記述「Audit Processでプロセス一覧から」に対応する項目は通常状態の確認 AUDIT01（Aud・プロセ・通常状）です。照合プロセ・通常状に関する監査プロセスの仕様は「Audit Processでプロセス一覧から Schedule」で、確認対象はプロセ・通常状・実行間です。比較監査プ・通常状でA:の停止前の確認 AUDIT14は「Audit Processで作業一覧から」を述べるため、正答側の照合軸はAud・通常状・プロセです。運用通常状・AudでB:のS-TAP Versionは「監視エージェントの暗号化表示と取得時刻を記録」を述べるため、正答側の照合軸はプロセ・監査プ・通常状です。仕様プロセ・通常状でD:のUser Nameは「データベース User Nameの照会文動詞」を述べるため、正答側の照合軸は通常状・実行間・プロセです。用語プロセ・通常状という用語は「Audit Processでプロセス一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・プロセ・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 通常状態の確認 AUDIT01**

    - 検証目的: 監査プロセスのAudit Process Builderについて通常状態を確定し、AUDIT01のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT01のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT01 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT01の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT01 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT01の報告上限を表示します。
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

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Schedule が画面・出力に表示されること
    ② ステップ2 の Status が画面・出力に表示されること
    ③ ステップ3 の audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring



### 監査プロセス Audit Process Builder 障害切り分け AUDIT04 {#c10-i0540}
*分類: 監査プロセス*  ・  難易度: 初級

障害切り分けでは 監査プロセス の プロセス一覧 を主操作として AUDIT04 を判定します。最初に失敗した処理への注意として「実行間隔より短いFROM/TO範囲で監査日を欠落させる危険があります」を AUDIT04 に残します。障害切り分けを補助する 作業一覧 では Status を補助値として AUDIT04 へ保存します。主判定の障害切り分けでは監査プロセスの プロセス一覧 から Schedule を読み AUDIT04 へ残します。証跡照合の障害切り分けでは監査プロセスの Schedule と Status を AUDIT04 に保存します。記録対応の障害切り分けでは監査プロセスの ScheduleとTask Status の証跡へ AUDIT04 を結びます。

**出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring

??? question "確認問題（1問）"
    **問題.** 監査プロセス Audit Process Builder 障害切り分け AUDIT04を同一分類のデータソース管理 Guardiumデータソース 異常終了後の確認 DSRC19と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はGuardiumでデータソース一覧から ServiceName を読み・ServiceName とである。データソース一覧からServiceNときは廃止サーバーの参照を残して監を防ぐ。
    - B. コマンドまたは機能の用途はServer IPのデータソースと取得時刻を記録し・監査タスク未レビューを防ぐである。復旧操作で点検欄を確認するときは監査タスク未レビューを防ぐ。
    - C. コマンドまたは機能の用途はAudit Processでプロセス一覧から Schedule を読み・Schedule と Statusである。プロセス一覧からScheduleを読ときは実行間隔より短いFROM/Tを防ぐ。 ✅
    - D. コマンドまたは機能の用途は監視エージェントの監視エージェント状態と取得時刻を記録し・カーネル監視導入状態の誤読を防ぐである。採取操作で照合欄を点検するときはカーネル監視導入状態の誤読を防ぐ。S-TAP監視 KTAP Installed 0319固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能プロセ・実行間でCの記述「Audit Processでプロセス一覧から」に対応する項目は障害切り分け AUDIT04（Aud・プロセ・監査プ）です。照合プロセ・監査プに関する監査プロセスの仕様は「Audit Processでプロセス一覧から Schedule」で、確認対象はプロセ・監査プ・実行間です。比較監査プ・監査プでA:の異常終了後の確認 DSRC19は「Guardiumでデータソース一覧から」を述べるため、正答側の照合軸はAud・監査プ・プロセです。運用監査プ・AudでB:のServer IPは「Server IPのデータソースと取得時刻を」を述べるため、正答側の照合軸はプロセ・監査プ・監査プです。仕様プロセ・監査プでD:のKTAP Installedは「監視エージェントの監視エージェント状態と取得」を述べるため、正答側の照合軸は監査プ・実行間・プロセです。用語プロセ・監査プという用語は「Audit Processでプロセス一覧から」を指し、照合する値と誤認リスクの組合せは監査プ・プロセ・実行間です。

    **出典:** Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


??? note "検証手順（1件）"
    **監査プロセス Audit Process Builder 障害切り分け AUDIT04**

    - 検証目的: 監査プロセスのAudit Process Builderについて障害範囲を限定し、AUDIT04のScheduleとTask Statusを実出力で確認する。
    - 前提条件: IBM Guardium Data Protection 12.xの参照権限を持ち、対象AUDIT04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Guardium Data Protection 12.xの運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Tools and Views > Audit Process Builderを指定し、AUDIT04のプロセス一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Tools and Views > Audit Process Builder
    → Enter を押す
    ```

    画面・出力:
    ```text
    Audit Process Name | Status | Schedule | Owner
    AUDIT04 | Active | Weekly | auditadmin
    ```

    画面・出力にあるScheduleを読み、ScheduleとTask Statusと対象AUDIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へComply > Audit Process To-Do Listを指定し、AUDIT04の作業一覧を表示します。
    操作（入力）:
    ```text
    IBM Guardium Data Protection 12.x 操作画面
    COMMAND ===> Comply > Audit Process To-Do List
    → Enter を押す
    ```

    画面・出力:
    ```text
    Process | Task | Due Date | Status
    AUDIT04 | Review Failed Logins | 2026-07-16 | Open
    ```

    画面・出力にあるStatusを読み、ScheduleとTask Statusと対象AUDIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Guardium Data Protection 12.xの監査プロセスを確認する入力画面です。COMMAND入力口へshow max_audit_reportingを指定し、AUDIT04の報告上限を表示します。
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

    画面・出力にあるauditを読み、ScheduleとTask Statusと対象AUDIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Schedule が画面・出力に表示されること
    ② ステップ2 の Status が画面・出力に表示されること
    ③ ステップ3 の audit が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: Guardium_Data_Protection_12_Predefined_reports / Guardium_Data_Protection_12_CLI_commands / Guardium_Data_Protection_12_Access_management / Guardium_Data_Protection_12_Compliance_monitoring


