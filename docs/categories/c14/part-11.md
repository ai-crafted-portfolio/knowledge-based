---
search:
  exclude: true
---

# IBM Spectrum Protect 8.1 — 詳細 (11/12)

[← IBM Spectrum Protect 8.1 の概要へ戻る](index.md)


## IBM Spectrum Protect 8.1 > リストア確認

### archive copy group 復元前確認 送信操作 {#c14-i0529}
*分類: リストア確認*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の リストア確認 で扱う「archive copy group 復元前確認 送信操作」は、アーカイブコピーの保存期間と宛先を定めるコピー規則を復元前確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 064を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** archive copy group 復元前確認 送信操作を同一分類のbackup copy group コマンド証跡 収集装置と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はアーカイブコピーの保存期間と宛先を定めるコピー規則を復元前確認する。 ✅
    - B. コマンドまたは機能の用途はバックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認する。
    - C. コマンドまたは機能の用途はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - D. コマンドまたは機能の用途はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。

    正解: **A** ／ 難易度: 中級

    **解説:** 復元前で復元前確認でAの記述「アーカイブコピーの保存期間と宛先を定めるコピー規則を復元前確認する」に対応する項目は復元前確認 送信操作（archive・復元前確）です。復元前・送信操に関するリストア確認の仕様は「アーカイブコピーの保存期間と宛先を定めるコピー規則を復元前確認する」で、確認対象はarchive・復元前確認です。コマンでポリシードのB:は「バックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認す」を述べ、対象はコマンド証跡 収集装置（backup・ポリシー）です。変更時のActioのC:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Action・変更）です。Scheを照合のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・照合）です。archを復元前確認という用語は「アーカイブコピーの保存期間と宛先を定めるコピー規則を」を指し、復元前確認 送信操作（archive・復元前確）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **archive copy group 復元前確認 送信操作**

    - 検証目的: リストア確認のarchive copy group 復元前確認 送信操作について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY ACTLOG の ANR メッセージを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL064
    ```

    画面・出力には ANR1550I が含まれ、archive copy group 復元前確認 送信操作の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL064 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL064
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### management class 宛先照合 初期同期 {#c14-i0530}
*分類: リストア確認*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の リストア確認 で扱う「management class 宛先照合 初期同期」は、ファイルのバックアップ先や保存期間を決めるポリシー要素を宛先照合の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL032を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** management class 宛先照合 初期同期を同一分類のコピーグループ Backup and Archive Copy Groupと比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はBackup andで変更前の確認ではコピーグループの アーカイブグループからRetainVersionを読である。
    - B. 構成を確認する際の意味はファイルのバックアップ先や保存期間を決めるポリシー要素である。 ✅
    - C. 構成を確認する際の意味はDBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULLを読み・再始動確認に使うである。
    - D. 構成を確認する際の意味はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。

    正解: **B** ／ 難易度: 中級

    **解説:** 宛先照合・managemeでBの記述「ファイルのバックアップ先や保存期間を決めるポリシー要素である」に対応する項目は宛先照合 初期同期（managem・宛先照合）です。宛先・初期同に関するリストア確認の仕様は「ファイルのバックアップ先や保存期間を決めるポリシー要素」で、確認対象はmanagem・宛先照合です。変更確認・BackupのA:は「Backup andで変更前の確認ではコピーグループの」を述べ、対象は変更前の確認 CG02（Backup・変更確認）です。再始動確認・DBのC:は「DBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULL」を述べ、対象は再始動後の確認 DBBK15（DB・再始動確）です。照合・DIRMCのD:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・照合）です。「management class」は「ファイルのバックアップ先や保存期間を決めるポリシー要」を指す用語で、宛先照合 初期同期（managem・宛先照合）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **management class 宛先照合 初期同期**

    - 検証目的: リストア確認のmanagement class 宛先照合 初期同期について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。VALIDATE POLICYSET の警告を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL032
    ```

    画面・出力には ANR1550I が含まれ、management class 宛先照合 初期同期の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL032 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL032
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### management class 容量監視 分散定義 {#c14-i0531}
*分類: リストア確認*  ・  難易度: 上級

IBM Spectrum Protect 8.1 の リストア確認 で扱う「management class 容量監視 分散定義」は、ファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL072を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** management class 容量監視 分散定義を同一分類のコピーグループ Backup and Archive Copy Groupと比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はBackup andで復旧準備ではコピーグループの アーカイブグループからRetainVersionを読みである。
    - B. 管理対象との関係を表す説明はStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - C. 管理対象との関係を表す説明はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - D. 管理対象との関係を表す説明はファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視として確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 容量監でリストアでDの記述「ファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視とし」に対応する項目は容量監視 分散定義（managem・リストア）です。容量監・分散定に関するリストア確認の仕様は「ファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視とし」で、確認対象はmanagem・リストアです。Backu・復旧準備のA:は「Backup andで復旧準備ではコピーグループの」を述べ、対象は復旧準備 CG05（Backup・復旧準備）です。サーバで変更のB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・変更）です。解析時のExpirのC:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・解析）です。manaをリストアという用語は「ファイルのバックアップ先や保存期間を決めるポリシー要」を指し、容量監視 分散定義（managem・リストア）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **management class 容量監視 分散定義**

    - 検証目的: リストア確認のmanagement class 容量監視 分散定義について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。VALIDATE POLICYSET の警告を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL072
    ```

    画面・出力には ANR1550I が含まれ、management class 容量監視 分散定義の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL072 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL072
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### node 期限切れ確認 更新配布 {#c14-i0532}
*分類: リストア確認*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の リストア確認 で扱う「node 期限切れ確認 更新配布」は、サーバーへ登録されたクライアントを表す管理単位を期限切れ確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE056を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** node 期限切れ確認 更新配布を同一分類のポリシードメイン Policy Domain 復旧後の確認 DOM06と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はPolicy Domainで復旧後の確認ではポリシードメインの ノード所属からNodeNameを読みである。
    - B. 構成を確認する際の意味はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。
    - C. 構成を確認する際の意味はサーバーへ登録されたクライアントを表す管理単位を期限切れ確認する。 ✅
    - D. 構成を確認する際の意味はSchedule Nameのスケジュール定義と取得時刻を記録し・日次処理順序の誤読を防ぐである。

    正解: **C** ／ 難易度: 中級

    **解説:** 期限切で期限切れ確でCの記述「サーバーへ登録されたクライアントを表す管理単位を期限切れ確認する」に対応する項目は期限切れ確認 更新配布（node・期限切れ）です。期限切・更新配に関するリストア確認の仕様は「サーバーへ登録されたクライアントを表す管理単位を期限切れ確認する」で、確認対象はnode・期限切れ確です。Polic・復旧確認のA:は「Policy Domainで復旧後の確認ではポリシードメインの」を述べ、対象は復旧後の確認 DOM06（Policy・復旧確認）です。ポリシで移行のB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・移行）です。Scheを照合のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・照合）です。nodeを期限切れ確という用語は「サーバーへ登録されたクライアントを表す管理単位を期限」を指し、期限切れ確認 更新配布（node・期限切れ）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **node 期限切れ確認 更新配布**

    - 検証目的: リストア確認のnode 期限切れ確認 更新配布について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY DOMAIN の詳細表示を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL056
    ```

    画面・出力には ANR1550I が含まれ、node 期限切れ確認 更新配布の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL056 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL056
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### node 状態確認 構成配布 {#c14-i0533}
*分類: リストア確認*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の リストア確認 で扱う「node 状態確認 構成配布」は、サーバーへ登録されたクライアントを表す管理単位を状態確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE016を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** node 状態確認 構成配布を同一分類のreclamation 状態確認 承認待ちと比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はサーバーへ登録されたクライアントを表す管理単位である。 ✅
    - B. コマンドまたは機能の用途はストレージプール内の空き領域を回収する処理である。
    - C. コマンドまたは機能の用途はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - D. コマンドまたは機能の用途はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。

    正解: **A** ／ 難易度: 中級

    **解説:** 状態確認・nodeでAの記述「サーバーへ登録されたクライアントを表す管理単位である」に対応する項目は状態確認 構成配布（node・状態確認）です。状態・構成配に関するリストア確認の仕様は「サーバーへ登録されたクライアントを表す管理単位」で、確認対象はnode・状態確認です。状態確認・reclamatのB:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は状態確認 承認待ち（reclama・状態確認）です。巡回・StartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・巡回）です。保護・ServerのD:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・保護）です。「node」は「サーバーへ登録されたクライアントを表す管理単位」を指す用語で、状態確認 構成配布（node・状態確認）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **node 状態確認 構成配布**

    - 検証目的: リストア確認のnode 状態確認 構成配布について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY DOMAIN の詳細表示を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL016
    ```

    画面・出力には ANR1550I が含まれ、node 状態確認 構成配布の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL016 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL016
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### reclamation コマンド証跡 差分確認 {#c14-i0534}
*分類: リストア確認*  ・  難易度: 初級

IBM Spectrum Protect 8.1 の リストア確認 で扱う「reclamation コマンド証跡 差分確認」は、ストレージプール内の空き領域を回収する処理をコマンド証跡の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR008Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** reclamation コマンド証跡 差分確認を同一分類のmanagement class ノード割当確認 オンライン表示と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はファイルのバックアップ先や保存期間を決めるポリシー要素をノード割当確認する。
    - B. 構成を確認する際の意味はストレージプール内の空き領域を回収する処理をコマンド証跡として確認する。 ✅
    - C. 構成を確認する際の意味はSchedule Nameのスケジュール定義と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - D. 構成を確認する際の意味はStart Timeの失敗理由と取得時刻を記録し・開始時刻誤設定を防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** 差分確認・reclamatでBの記述「ストレージプール内の空き領域を回収する処理をコマンド証跡として確認す」に対応する項目はコマンド証跡 差分確認（reclama・差分確認）です。コマン・差分に関するリストア確認の仕様は「ストレージプール内の空き領域を回収する処理をコマンド証跡として確認す」で、確認対象はreclama・差分確認です。オンライン・managemeのA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素をノード割当確」を述べ、対象はノード割当確認 オンライン表示（managem・オンライ）です。棚卸・ScheduleのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・棚卸）です。保護・StartのD:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・保護）です。「reclamation」は「ストレージプール内の空き領域を回収する処理をコマンド」を指す用語で、コマンド証跡 差分確認（reclama・差分確認）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **reclamation コマンド証跡 差分確認**

    - 検証目的: リストア確認のreclamation コマンド証跡 差分確認について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY STGPOOL の容量表示を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL008
    ```

    画面・出力には ANR1550I が含まれ、reclamation コマンド証跡 差分確認の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL008 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL008
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### reclamation ノード割当確認 プール宛先 {#c14-i0535}
*分類: リストア確認*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の リストア確認 で扱う「reclamation ノード割当確認 プール宛先」は、ストレージプール内の空き領域を回収する処理をノード割当確認の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR048Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** reclamation ノード割当確認 プール宛先を同一分類の管理クラス Management Class 権限境界の確認 MC12と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はManagement Classで権限境界の確認では管理クラスの オプション確認からDIRMCを読みである。
    - B. 管理対象との関係を表す説明はストレージプール内の空き領域を回収する処理をノード割当確認する。 ✅
    - C. 管理対象との関係を表す説明はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - D. 管理対象との関係を表す説明はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。

    正解: **B** ／ 難易度: 中級

    **解説:** ノード割当・reclamatでBの記述「ストレージプール内の空き領域を回収する処理をノード割当確認する」に対応する項目はノード割当確認 プール宛先（reclama・ノード割）です。ノード・プールに関するリストア確認の仕様は「ストレージプール内の空き領域を回収する処理をノード割当確認する」で、確認対象はreclama・ノード割当です。権限境界確・ManagemeのA:は「Management Classで権限境界の確認では管理クラスの」を述べ、対象は権限境界の確認 MC12（Managem・権限境界）です。復旧・DatabaseのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・復旧）です。保護・ExpiratiのD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・保護）です。「reclamation」は「ストレージプール内の空き領域を回収する処理をノード割」を指す用語で、ノード割当確認 プール宛先（reclama・ノード割）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **reclamation ノード割当確認 プール宛先**

    - 検証目的: リストア確認のreclamation ノード割当確認 プール宛先について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、リストア確認の対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY STGPOOL の容量表示を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL048
    ```

    画面・出力には ANR1550I が含まれ、reclamation ノード割当確認 プール宛先の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL048 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL048
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### リストア確認 Client Restore ログとの照合 RST07 {#c14-i0536}
*分類: リストア確認*  ・  難易度: 中級

ログとの照合では リストア確認 の 候補照会 を主操作として RST07 を判定します。時刻と対象識別子への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST07 に残します。ログとの照合を補助する 別名復元 では restored を補助値として RST07 へ保存します。主判定のログとの照合ではリストア確認の 候補照会 から MgmtClass を読み RST07 へ残します。証跡照合のログとの照合ではリストア確認の MgmtClass と restored を RST07 に保存します。記録対応のログとの照合ではリストア確認の Restore CountとFailed Count の証跡へ RST07 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore ログとの照合 RST07を同一分類のリストア確認 Client Restore 引継ぎ記録 RST09と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はClient Restoreで引継ぎ記録ではリストア確認の 活動ログからRestoreを読みである。
    - B. 管理対象との関係を表す説明はClient Restoreでログとの照合ではリストア確認の 候補照会からMgmtClassを読みである。 ✅
    - C. 管理対象との関係を表す説明はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。
    - D. 管理対象との関係を表す説明はファイルのバックアップ先や保存期間を決めるポリシー要素をノード割当確認する。management class ノード割当確認 オンライン表示固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 中級

    **解説:** ログとの対象ClienでBの記述「Client Restoreでログとの照合ではリストア確認の」に対応する項目はログとの照合 RST07（Client・ログとの）です。リスト・ログとに関するリストア確認の仕様は「Client Restoreでログとの照合ではリストア確認の」で、確認対象はClient・ログとの照です。Clien・リストア確のA:は「Client Restoreで引継ぎ記録ではリストア確認の」を述べ、対象は引継ぎ記録 RST09（Client・リストア）です。保護時のActioのC:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Action・保護）です。manaをオンラインのD:は「ファイルのバックアップ先や保存期間を決めるポリシー要素をノード割当確」を述べ、対象はノード割当確認 オンライン表示（managem・オンライ）です。Clieをログとの照という用語は「Client Restoreでログとの照合ではリスト」を指し、ログとの照合 RST07（Client・ログとの）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore ログとの照合 RST07**

    - 検証目的: リストア確認のClient Restoreについて操作とログを対応し、RST07のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST07の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST07の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST07の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE07 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の MgmtClass が画面・出力に表示されること
    ② ステップ2 の restored が画面・出力に表示されること
    ③ ステップ3 の Restore が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 代替経路の確認 RST10 {#c14-i0537}
*分類: リストア確認*  ・  難易度: 中級

代替経路の確認では リストア確認 の 候補照会 を主操作として RST10 を判定します。主経路との役割差への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST10 に残します。代替経路の確認を補助する 別名復元 では restored を補助値として RST10 へ保存します。主判定の代替経路の確認ではリストア確認の 候補照会 から MgmtClass を読み RST10 へ残します。証跡照合の代替経路の確認ではリストア確認の MgmtClass と restored を RST10 に保存します。記録対応の代替経路の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST10 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 代替経路の確認 RST10について構成や状態を確認します。サーバーDB・DR Server Database Backup 性能影響の確認ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはDBで性能影響の確認ではサーバーの DBバックアップからANR4550Iを読み・性能影響確認に使うである。
    - B. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。サーバー日次運用 Expiration Status 0244固有の属性も確認対象に含める。
    - C. 対象資源に対する働きはClient Restoreで代替経路の確認ではリストア確認の 候補照会からMgmtClassを読みである。 ✅
    - D. 対象資源に対する働きはストレージプール内の空き領域を回収する処理をノード割当確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** 代替経路対象ClienでCの記述「Client Restoreで代替経路の確認ではリストア確認の」に対応する項目は代替経路の確認 RST10（Client・代替経路）です。リスト・代替経に関するリストア確認の仕様は「Client Restoreで代替経路の確認ではリストア確認の」で、確認対象はClient・代替経路確です。性能影響対象性能影響ののA:は「DBで性能影響の確認ではサーバーの DBバックアップからANR455」を述べ、対象は性能影響の確認 DBBK11（DB・性能影響）です。保護対象ExpirのB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・保護）です。reclをノード割当のD:は「ストレージプール内の空き領域を回収する処理をノード割当確認する」を述べ、対象はノード割当確認 プール宛先（reclama・ノード割）です。Clieを代替経路確という用語は「Client Restoreで代替経路の確認ではリス」を指し、代替経路の確認 RST10（Client・代替経路）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 代替経路の確認 RST10**

    - 検証目的: リストア確認のClient Restoreについて代替手段の成立を確認し、RST10のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST10の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST10の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST10の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE10 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の MgmtClass が画面・出力に表示されること
    ② ステップ2 の restored が画面・出力に表示されること
    ③ ステップ3 の Restore が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 依存関係の確認 RST13 {#c14-i0538}
*分類: リストア確認*  ・  難易度: 中級

依存関係の確認では リストア確認 の 候補照会 を主操作として RST13 を判定します。前提資源と後続処理の順序への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST13 に残します。依存関係の確認を補助する 別名復元 では restored を補助値として RST13 へ保存します。主判定の依存関係の確認ではリストア確認の 候補照会 から MgmtClass を読み RST13 へ残します。証跡照合の依存関係の確認ではリストア確認の MgmtClass と restored を RST13 に保存します。記録対応の依存関係の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST13 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 依存関係の確認 RST13に関する障害切り分けの前提を確認しています。サーバーDB・DR Server Database Backup 再始動後の確認の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はClient Restoreで依存関係の確認ではリストア確認の 候補照会からMgmtClassを読みである。 ✅
    - B. 表示や設定で扱う内容はDBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULLを読み・再始動確認に使うである。
    - C. 表示や設定で扱う内容はSchedule Nameのスケジュール定義と取得時刻を記録し・日次処理順序の誤読を防ぐである。クライアントスケジュール Schedule Name 0204固有の属性も確認対象に含める。
    - D. 表示や設定で扱う内容はバックアップ版数と保存先を定めるコピー規則である。

    正解: **A** ／ 難易度: 中級

    **解説:** 依存関係対象ClienでAの記述「Client Restoreで依存関係の確認ではリストア確認の」に対応する項目は依存関係の確認 RST13（Client・依存関係）です。リスト・依存関に関するリストア確認の仕様は「Client Restoreで依存関係の確認ではリストア確認の」で、確認対象はClient・依存関係確です。再始動確対象DBのB:は「DBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULL」を述べ、対象は再始動後の確認 DBBK15（DB・再始動確）です。登録時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・登録）です。backを保存期間確のD:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は保存期間確認 ルール読替（backup・保存期間）です。Clieを依存関係確という用語は「Client Restoreで依存関係の確認ではリス」を指し、依存関係の確認 RST13（Client・依存関係）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 依存関係の確認 RST13**

    - 検証目的: リストア確認のClient Restoreについて依存資源を点検し、RST13のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST13の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST13の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST13の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE13 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の MgmtClass が画面・出力に表示されること
    ② ステップ2 の restored が画面・出力に表示されること
    ③ ステップ3 の Restore が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 停止前の確認 RST14 {#c14-i0539}
*分類: リストア確認*  ・  難易度: 中級

停止前の確認では リストア確認 の 別名復元 を主操作として RST14 を判定します。処理中資源と未完了要求への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST14 に残します。停止前の確認を補助する 活動ログ では Restore を補助値として RST14 へ保存します。主判定の停止前の確認ではリストア確認の 別名復元 から restored を読み RST14 へ残します。証跡照合の停止前の確認ではリストア確認の restored と Restore を RST14 に保存します。記録対応の停止前の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST14 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 停止前の確認 RST14の設定や表示を読む前に役割を確認します。サーバーDB・DR Server Database Backup 停止前の確認ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はDBで停止前の確認ではサーバーの DBバックアップからANR4550Iを読み・停止確認に使うである。
    - B. 一次資料が示す主目的はCopy Groupのコピーグループと取得時刻を記録し・コピーグループ未定義を防ぐである。
    - C. 一次資料が示す主目的はClient Restoreで停止前の確認ではリストア確認の 別名復元からrestoredを読みである。 ✅
    - D. 一次資料が示す主目的はPolicy Domainで停止前の確認ではポリシードメインの ポリシーセットからPolicySetを読みである。

    正解: **C** ／ 難易度: 中級

    **解説:** 停止確認対象ClienでCの記述「Client Restoreで停止前の確認ではリストア確認の」に対応する項目は停止前の確認 RST14（Client・停止確認）です。リスト・停止前に関するリストア確認の仕様は「Client Restoreで停止前の確認ではリストア確認の」で、確認対象はClient・停止確認です。停止確認対象停止前の確のA:は「DBで停止前の確認ではサーバーの DBバックアップからANR4550」を述べ、対象は停止前の確認 DBBK14（DB・停止確認）です。収集対象CopyのB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・収集）です。Poliを停止確認のD:は「Policy Domainで停止前の確認ではポリシードメインの」を述べ、対象は停止前の確認 DOM14（Policy・停止確認）です。Clieを停止確認という用語は「Client Restoreで停止前の確認ではリスト」を指し、停止前の確認 RST14（Client・停止確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 停止前の確認 RST14**

    - 検証目的: リストア確認のClient Restoreについて安全な停止条件を確認し、RST14のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST14の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST14の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE14 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST14の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の restored が画面・出力に表示されること
    ② ステップ2 の Restore が画面・出力に表示されること
    ③ ステップ3 の MgmtClass が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 再始動後の確認 RST15 {#c14-i0540}
*分類: リストア確認*  ・  難易度: 中級

再始動後の確認では リストア確認 の 活動ログ を主操作として RST15 を判定します。再開点と未処理データへの注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST15 に残します。再始動後の確認を補助する 候補照会 では MgmtClass を補助値として RST15 へ保存します。主判定の再始動後の確認ではリストア確認の 活動ログ から Restore を読み RST15 へ残します。証跡照合の再始動後の確認ではリストア確認の Restore と MgmtClass を RST15 に保存します。記録対応の再始動後の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST15 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 再始動後の確認 RST15を同一分類のサーバーDB・DR Server Database Backup 停止前の確認と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はDBで停止前の確認ではサーバーの DBバックアップからANR4550Iを読み・停止確認に使うである。
    - B. 構成を確認する際の意味はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。サーバー日次運用 Database Backup 0247固有の属性も確認対象に含める。
    - C. 構成を確認する際の意味はバックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認する。
    - D. 構成を確認する際の意味はClient Restoreで再始動後の確認ではリストア確認の 活動ログからRestoreを読みである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 再始動確対象ClienでDの記述「Client Restoreで再始動後の確認ではリストア確認の」に対応する項目は再始動後の確認 RST15（Client・再始動確）です。リスト・再始動に関するリストア確認の仕様は「Client Restoreで再始動後の確認ではリストア確認の」で、確認対象はClient・再始動確認です。停止確認対象停止前の確のA:は「DBで停止前の確認ではサーバーの DBバックアップからANR4550」を述べ、対象は停止前の確認 DBBK14（DB・停止確認）です。保護対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・保護）です。期限切れ時のschedのC:は「バックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認す」を述べ、対象は期限切れ確認 ドメイン値（schedul・期限切れ）です。Clieを再始動確認という用語は「Client Restoreで再始動後の確認ではリス」を指し、再始動後の確認 RST15（Client・再始動確）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 再始動後の確認 RST15**

    - 検証目的: リストア確認のClient Restoreについて再始動結果を検証し、RST15のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST15の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE15 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST15の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST15の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Restore が画面・出力に表示されること
    ② ステップ2 の MgmtClass が画面・出力に表示されること
    ③ ステップ3 の restored が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 変更前の確認 RST02 {#c14-i0541}
*分類: リストア確認*  ・  難易度: 中級

変更前の確認では リストア確認 の 別名復元 を主操作として RST02 を判定します。変更対象と非対象の境界への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST02 に残します。変更前の確認を補助する 活動ログ では Restore を補助値として RST02 へ保存します。主判定の変更前の確認ではリストア確認の 別名復元 から restored を読み RST02 へ残します。証跡照合の変更前の確認ではリストア確認の restored と Restore を RST02 に保存します。記録対応の変更前の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST02 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 変更前の確認 RST02について構成や状態を確認します。サーバー日次運用 Server Name 0031ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はClient Restoreで変更前の確認ではリストア確認の 別名復元からrestoredを読みである。 ✅
    - B. 一次資料が示す主目的はServer NameのDBバックアップ履歴と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - C. 一次資料が示す主目的はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。クライアントスケジュール Start Time 0243固有の属性も確認対象に含める。
    - D. 一次資料が示す主目的はバックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** 変更確認対象ClienでAの記述「Client Restoreで変更前の確認ではリストア確認の」に対応する項目は変更前の確認 RST02（Client・変更確認）です。リスト・変更前に関するリストア確認の仕様は「Client Restoreで変更前の確認ではリストア確認の」で、確認対象はClient・変更確認です。棚卸対象ServeのB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・棚卸）です。保護時のStartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・保護）です。backをポリシードのD:は「バックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認す」を述べ、対象はコマンド証跡 収集装置（backup・ポリシー）です。Clieを変更確認という用語は「Client Restoreで変更前の確認ではリスト」を指し、変更前の確認 RST02（Client・変更確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 変更前の確認 RST02**

    - 検証目的: リストア確認のClient Restoreについて変更前の証跡を保存し、RST02のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST02の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST02の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE02 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST02の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の restored が画面・出力に表示されること
    ② ステップ2 の Restore が画面・出力に表示されること
    ③ ステップ3 の MgmtClass が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 変更後の確認 RST03 {#c14-i0542}
*分類: リストア確認*  ・  難易度: 中級

変更後の確認では リストア確認 の 活動ログ を主操作として RST03 を判定します。反映値と残存値への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST03 に残します。変更後の確認を補助する 候補照会 では MgmtClass を補助値として RST03 へ保存します。主判定の変更後の確認ではリストア確認の 活動ログ から Restore を読み RST03 へ残します。証跡照合の変更後の確認ではリストア確認の Restore と MgmtClass を RST03 に保存します。記録対応の変更後の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST03 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 変更後の確認 RST03の技術的な意味を資料で確認するとき、クライアントスケジュール Event Status 0027との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - B. 構成を確認する際の意味はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - C. 構成を確認する際の意味はバックアップや管理コマンドを決めた時刻に実行する定義をコマンド証跡として確認する。
    - D. 構成を確認する際の意味はClient Restoreで変更後の確認ではリストア確認の 活動ログからRestoreを読みである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更確認対象ClienでDの記述「Client Restoreで変更後の確認ではリストア確認の」に対応する項目は変更後の確認 RST03（Client・変更確認）です。リスト・変更後に関するリストア確認の仕様は「Client Restoreで変更後の確認ではリストア確認の」で、確認対象はClient・変更確認です。Event・棚卸のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・棚卸）です。登録対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・登録）です。コピーグ時のschedのC:は「バックアップや管理コマンドを決めた時刻に実行する定義をコマンド証跡と」を述べ、対象はコマンド証跡 詳細タブ（schedul・コピーグ）です。Clieを変更確認という用語は「Client Restoreで変更後の確認ではリスト」を指し、変更後の確認 RST03（Client・変更確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 変更後の確認 RST03**

    - 検証目的: リストア確認のClient Restoreについて変更結果を検証し、RST03のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST03の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE03 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST03の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST03の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Restore が画面・出力に表示されること
    ② ステップ2 の MgmtClass が画面・出力に表示されること
    ③ ステップ3 の restored が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 引継ぎ記録 RST09 {#c14-i0543}
*分類: リストア確認*  ・  難易度: 中級

引継ぎ記録では リストア確認 の 活動ログ を主操作として RST09 を判定します。次担当者が追跡できる証跡への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST09 に残します。引継ぎ記録を補助する 候補照会 では MgmtClass を補助値として RST09 へ保存します。主判定の引継ぎ記録ではリストア確認の 活動ログ から Restore を読み RST09 へ残します。証跡照合の引継ぎ記録ではリストア確認の Restore と MgmtClass を RST09 に保存します。記録対応の引継ぎ記録ではリストア確認の Restore CountとFailed Count の証跡へ RST09 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 引継ぎ記録 RST09の役割を調べています。サーバー日次運用 Database Backup 0007の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - B. 機能の説明としてはDIRMCのノード登録値と取得時刻を記録し・登録ドメインの取り違えを防ぐである。
    - C. 機能の説明としてはアーカイブコピーの保存期間と宛先を定めるコピー規則を容量監視として確認する。
    - D. 機能の説明としてはClient Restoreで引継ぎ記録ではリストア確認の 活動ログからRestoreを読みである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** リストア対象ClienでDの記述「Client Restoreで引継ぎ記録ではリストア確認の」に対応する項目は引継ぎ記録 RST09（Client・リストア）です。リスト・引継ぎに関するリストア確認の仕様は「Client Restoreで引継ぎ記録ではリストア確認の」で、確認対象はClient・リストア確です。Datab・巡回のA:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・巡回）です。収集対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・収集）です。バックア時のarchiのC:は「アーカイブコピーの保存期間と宛先を定めるコピー規則を容量監視として確」を述べ、対象は容量監視 実行結果（archive・バックア）です。Clieをリストア確という用語は「Client Restoreで引継ぎ記録ではリストア」を指し、引継ぎ記録 RST09（Client・リストア）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 引継ぎ記録 RST09**

    - 検証目的: リストア確認のClient Restoreについて再現可能な記録を作成し、RST09のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST09の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE09 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST09の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST09の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Restore が画面・出力に表示されること
    ② ステップ2 の MgmtClass が画面・出力に表示されること
    ③ ステップ3 の restored が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 復旧後の確認 RST06 {#c14-i0544}
*分類: リストア確認*  ・  難易度: 中級

復旧後の確認では リストア確認 の 活動ログ を主操作として RST06 を判定します。再発していないことを示す値への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST06 に残します。復旧後の確認を補助する 候補照会 では MgmtClass を補助値として RST06 へ保存します。主判定の復旧後の確認ではリストア確認の 活動ログ から Restore を読み RST06 へ残します。証跡照合の復旧後の確認ではリストア確認の Restore と MgmtClass を RST06 に保存します。記録対応の復旧後の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST06 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 復旧後の確認 RST06の設定や表示を読む前に役割を確認します。サーバー日次運用 Expiration Status 0034ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - B. 状態を読み取るための働きはNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - C. 状態を読み取るための働きはClient Restoreで復旧後の確認ではリストア確認の 活動ログからRestoreを読みである。 ✅
    - D. 状態を読み取るための働きはストレージプール内の空き領域を回収する処理である。

    正解: **C** ／ 難易度: 中級

    **解説:** 復旧確認対象ClienでCの記述「Client Restoreで復旧後の確認ではリストア確認の」に対応する項目は復旧後の確認 RST06（Client・復旧確認）です。リスト・復旧後に関するリストア確認の仕様は「Client Restoreで復旧後の確認ではリストア確認の」で、確認対象はClient・復旧確認です。Expir・棚卸のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・棚卸）です。保護対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・保護）です。reclを宛先照合のD:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は宛先照合 集約結果（reclama・宛先照合）です。Clieを復旧確認という用語は「Client Restoreで復旧後の確認ではリスト」を指し、復旧後の確認 RST06（Client・復旧確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 復旧後の確認 RST06**

    - 検証目的: リストア確認のClient Restoreについて復旧後の安定性を確認し、RST06のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST06の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE06 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST06の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST06の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Restore が画面・出力に表示されること
    ② ステップ2 の MgmtClass が画面・出力に表示されること
    ③ ステップ3 の restored が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 復旧準備 RST05 {#c14-i0545}
*分類: リストア確認*  ・  難易度: 中級

復旧準備では リストア確認 の 別名復元 を主操作として RST05 を判定します。再開前に必要な整合性への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST05 に残します。復旧準備を補助する 活動ログ では Restore を補助値として RST05 へ保存します。主判定の復旧準備ではリストア確認の 別名復元 から restored を読み RST05 へ残します。証跡照合の復旧準備ではリストア確認の restored と Restore を RST05 に保存します。記録対応の復旧準備ではリストア確認の Restore CountとFailed Count の証跡へ RST05 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 復旧準備 RST05に関する障害切り分けの前提を確認しています。サーバー日次運用 Node Name 0013の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - B. 障害切り分けに用いる役割はClient Restoreで復旧準備ではリストア確認の 別名復元からrestoredを読み・復旧準備に使うである。 ✅
    - C. 障害切り分けに用いる役割はStorage Poolのストレージプール使用量と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。サーバー日次運用 Storage Pool 0250固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割はアーカイブコピーの保存期間と宛先を定めるコピー規則である。

    正解: **B** ／ 難易度: 中級

    **解説:** 復旧準備対象ClienでBの記述「Client Restoreで復旧準備ではリストア確認の」に対応する項目は復旧準備 RST05（Client・復旧準備）です。リスト・復旧準に関するリストア確認の仕様は「Client Restoreで復旧準備ではリストア確認の」で、確認対象はClient・復旧準備です。Node・巡回のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・巡回）です。保護時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・保護）です。archを保存期間確のD:は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を述べ、対象は保存期間確認 証明書検査（archive・保存期間）です。Clieを復旧準備という用語は「Client Restoreで復旧準備ではリストア確」を指し、復旧準備 RST05（Client・復旧準備）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 復旧準備 RST05**

    - 検証目的: リストア確認のClient Restoreについて復旧条件を確認し、RST05のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST05の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST05の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE05 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST05の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の restored が画面・出力に表示されること
    ② ステップ2 の Restore が画面・出力に表示されること
    ③ ステップ3 の MgmtClass が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 性能影響の確認 RST11 {#c14-i0546}
*分類: リストア確認*  ・  難易度: 中級

性能影響の確認では リストア確認 の 別名復元 を主操作として RST11 を判定します。処理時間と滞留箇所への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST11 に残します。性能影響の確認を補助する 活動ログ では Restore を補助値として RST11 へ保存します。主判定の性能影響の確認ではリストア確認の 別名復元 から restored を読み RST11 へ残します。証跡照合の性能影響の確認ではリストア確認の restored と Restore を RST11 に保存します。記録対応の性能影響の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST11 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 性能影響の確認 RST11の技術的な意味を資料で確認するとき、サーバー日次運用 Node Name 0058との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。サーバー日次運用 Node Name 0058固有の属性も確認対象に含める。
    - B. コマンドまたは機能の用途はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。
    - C. コマンドまたは機能の用途はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - D. コマンドまたは機能の用途はClient Restoreで性能影響の確認ではリストア確認の 別名復元からrestoredを読みである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 性能影響対象ClienでDの記述「Client Restoreで性能影響の確認ではリストア確認の」に対応する項目は性能影響の確認 RST11（Client・性能影響）です。リスト・性能影に関するリストア確認の仕様は「Client Restoreで性能影響の確認ではリストア確認の」で、確認対象はClient・性能影響確です。Node・復旧のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・復旧）です。切替対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・切替）です。承認時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・承認）です。Clieを性能影響確という用語は「Client Restoreで性能影響の確認ではリス」を指し、性能影響の確認 RST11（Client・性能影響）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 性能影響の確認 RST11**

    - 検証目的: リストア確認のClient Restoreについて負荷と待ちを確認し、RST11のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST11の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST11の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE11 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST11の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の restored が画面・出力に表示されること
    ② ステップ2 の Restore が画面・出力に表示されること
    ③ ステップ3 の MgmtClass が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 構成監査 RST08 {#c14-i0547}
*分類: リストア確認*  ・  難易度: 中級

構成監査では リストア確認 の 別名復元 を主操作として RST08 を判定します。定義値と稼働値の一致への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST08 に残します。構成監査を補助する 活動ログ では Restore を補助値として RST08 へ保存します。主判定の構成監査ではリストア確認の 別名復元 から restored を読み RST08 へ残します。証跡照合の構成監査ではリストア確認の restored と Restore を RST08 に保存します。記録対応の構成監査ではリストア確認の Restore CountとFailed Count の証跡へ RST08 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「リストア確認 Client Restore 構成監査 RST08」を「サーバー日次運用 Node Name 0058」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はClient Restoreで構成監査ではリストア確認の 別名復元からrestoredを読み・構成監査に使うである。 ✅
    - B. 仕様上の役割はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - C. 仕様上の役割はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - D. 仕様上の役割はバックアップやアーカイブのデータを格納するサーバー側領域である。storage pool 保存期間確認 検査エンジン固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 中級

    **解説:** 構成監査対象ClienでAの記述「Client Restoreで構成監査ではリストア確認の」に対応する項目は構成監査 RST08（Client・構成監査）です。リスト・構成監に関するリストア確認の仕様は「Client Restoreで構成監査ではリストア確認の」で、確認対象はClient・構成監査です。復旧対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・復旧）です。収集時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・収集）です。storを保存期間確のD:は「バックアップやアーカイブのデータを格納するサーバー側領域」を述べ、対象は保存期間確認 検査エンジン（storage・保存期間）です。Clieを構成監査という用語は「Client Restoreで構成監査ではリストア確」を指し、構成監査 RST08（Client・構成監査）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 構成監査 RST08**

    - 検証目的: リストア確認のClient Restoreについて構成差分を監査し、RST08のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST08の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST08の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE08 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST08の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の restored が画面・出力に表示されること
    ② ステップ2 の Restore が画面・出力に表示されること
    ③ ステップ3 の MgmtClass が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 権限境界の確認 RST12 {#c14-i0548}
*分類: リストア確認*  ・  難易度: 中級

権限境界の確認では リストア確認 の 活動ログ を主操作として RST12 を判定します。参照操作と変更操作の分離への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST12 に残します。権限境界の確認を補助する 候補照会 では MgmtClass を補助値として RST12 へ保存します。主判定の権限境界の確認ではリストア確認の 活動ログ から Restore を読み RST12 へ残します。証跡照合の権限境界の確認ではリストア確認の Restore と MgmtClass を RST12 に保存します。記録対応の権限境界の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST12 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 権限境界の確認 RST12を保守記録に説明する必要があります。複製・保護 Storage Pool Protection and Nodeと取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はClient Restoreで権限境界の確認ではリストア確認の 活動ログからRestoreを読みである。 ✅
    - B. 運用時に利用する技術的役割はStorage Poolで変更後の確認では複製・保護の 検証からANR3730Iを読み・変更確認に使うである。
    - C. 運用時に利用する技術的役割はServer NameのDBバックアップ履歴と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - D. 運用時に利用する技術的役割はPolicy Domainで復旧後の確認ではポリシードメインの ノード所属からNodeNameを読みである。

    正解: **A** ／ 難易度: 中級

    **解説:** 権限境界対象ClienでAの記述「Client Restoreで権限境界の確認ではリストア確認の」に対応する項目は権限境界の確認 RST12（Client・権限境界）です。リスト・権限境に関するリストア確認の仕様は「Client Restoreで権限境界の確認ではリストア確認の」で、確認対象はClient・権限境界確です。変更確認対象StoraのB:は「Storage Poolで変更後の確認では複製・保護の」を述べ、対象は変更後の確認 REPL03（Storage・変更確認）です。確認時のServeのC:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・確認）です。Poliを復旧確認のD:は「Policy Domainで復旧後の確認ではポリシードメインの」を述べ、対象は復旧後の確認 DOM06（Policy・復旧確認）です。Clieを権限境界確という用語は「Client Restoreで権限境界の確認ではリス」を指し、権限境界の確認 RST12（Client・権限境界）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 権限境界の確認 RST12**

    - 検証目的: リストア確認のClient Restoreについて実行権限を点検し、RST12のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST12の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE12 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST12の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST12の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Restore が画面・出力に表示されること
    ② ステップ2 の MgmtClass が画面・出力に表示されること
    ③ ステップ3 の restored が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 通常状態の確認 RST01 {#c14-i0549}
*分類: リストア確認*  ・  難易度: 中級

通常状態の確認では リストア確認 の 候補照会 を主操作として RST01 を判定します。基準値と現在値の差への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST01 に残します。通常状態の確認を補助する 別名復元 では restored を補助値として RST01 へ保存します。主判定の通常状態の確認ではリストア確認の 候補照会 から MgmtClass を読み RST01 へ残します。証跡照合の通常状態の確認ではリストア確認の MgmtClass と restored を RST01 に保存します。記録対応の通常状態の確認ではリストア確認の Restore CountとFailed Count の証跡へ RST01 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 通常状態の確認 RST01の役割を調べています。サーバーDB・DR Server Database Backup 代替経路の確認の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はClient Restoreで通常状態の確認ではリストア確認の 候補照会からMgmtClassを読みである。 ✅
    - B. 表示や設定で扱う内容はDBで代替経路の確認ではサーバーの DB状態からLastDatabaseを読み・代替経路確認に使うである。サーバーDB・DR Server Database Backup固有の属性も確認対象に含める。
    - C. 表示や設定で扱う内容はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - D. 表示や設定で扱う内容はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。

    正解: **A** ／ 難易度: 中級

    **解説:** 通常状態対象ClienでAの記述「Client Restoreで通常状態の確認ではリストア確認の」に対応する項目は通常状態の確認 RST01（Client・通常状態）です。リスト・通常状に関するリストア確認の仕様は「Client Restoreで通常状態の確認ではリストア確認の」で、確認対象はClient・通常状態確です。代替経路対象DBのB:は「DBで代替経路の確認ではサーバーの DB状態からLastDataba」を述べ、対象は代替経路の確認 DBBK10（DB・代替経路）です。切替時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・切替）です。ノード登録を解除のD:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・解除）です。Clieを通常状態確という用語は「Client Restoreで通常状態の確認ではリス」を指し、通常状態の確認 RST01（Client・通常状態）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 通常状態の確認 RST01**

    - 検証目的: リストア確認のClient Restoreについて通常状態を確定し、RST01のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST01の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST01の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST01の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE01 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の MgmtClass が画面・出力に表示されること
    ② ステップ2 の restored が画面・出力に表示されること
    ③ ステップ3 の Restore が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### リストア確認 Client Restore 障害切り分け RST04 {#c14-i0550}
*分類: リストア確認*  ・  難易度: 中級

障害切り分けでは リストア確認 の 候補照会 を主操作として RST04 を判定します。最初に失敗した処理への注意として「置換条件や復元先を確認せず本番ファイルを上書きする危険があります」を RST04 に残します。障害切り分けを補助する 別名復元 では restored を補助値として RST04 へ保存します。主判定の障害切り分けではリストア確認の 候補照会 から MgmtClass を読み RST04 へ残します。証跡照合の障害切り分けではリストア確認の MgmtClass と restored を RST04 に保存します。記録対応の障害切り分けではリストア確認の Restore CountとFailed Count の証跡へ RST04 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** リストア確認 Client Restore 障害切り分け RST04を保守記録に説明する必要があります。サーバーDB・DR Server Database Backup 代替経路の確認と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はDBで代替経路の確認ではサーバーの DB状態からLastDatabaseを読み・代替経路確認に使うである。
    - B. 保守作業で参照する機能はClient Restoreで障害切り分けではリストア確認の 候補照会からMgmtClassを読みである。 ✅
    - C. 保守作業で参照する機能はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。
    - D. 保守作業で参照する機能はアーカイブコピーの保存期間と宛先を定めるコピー規則である。

    正解: **B** ／ 難易度: 中級

    **解説:** リストア対象ClienでBの記述「Client Restoreで障害切り分けではリストア確認の」に対応する項目は障害切り分け RST04（Client・リストア）です。リスト・障害切に関するリストア確認の仕様は「Client Restoreで障害切り分けではリストア確認の」で、確認対象はClient・リストア確です。代替経路対象代替経路ののA:は「DBで代替経路の確認ではサーバーの DB状態からLastDataba」を述べ、対象は代替経路の確認 DBBK10（DB・代替経路）です。確認時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・確認）です。archを宛先照合のD:は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を述べ、対象は宛先照合 伝搬経路（archive・宛先照合）です。Clieをリストア確という用語は「Client Restoreで障害切り分けではリスト」を指し、障害切り分け RST04（Client・リストア）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **リストア確認 Client Restore 障害切り分け RST04**

    - 検証目的: リストア確認のClient Restoreについて障害範囲を限定し、RST04のRestore CountとFailed Countを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象RST04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc query backup /app/report.dat -inactiveを指定し、RST04の候補照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query backup /app/report.dat -inactive
    → Enter を押す
    ```

    画面・出力:
    ```text
    Size Backup Date MgmtClass A/I File -- 1048576 07/15/2026 STANDARD A /app/report.dat
    ```

    画面・出力にあるMgmtClassを読み、Restore CountとFailed Countと対象RST04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へdsmc restore /app/report.dat /restore/report.datを指定し、RST04の別名復元を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc restore /app/report.dat /restore/report.dat
    → Enter を押す
    ```

    画面・出力:
    ```text
    Restoring /app/report.dat to /restore/report.dat
    Total number of objects restored: 1
    Total number of objects failed: 0
    ```

    画面・出力にあるrestoredを読み、Restore CountとFailed Countと対象RST04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のリストア確認を確認する入力画面です。COMMAND入力口へQUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAYを指定し、RST04の活動ログを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY ACTLOG SEARCH=RESTORE BEGINDATE=TODAY
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator issued command QUERY RESTORE. Restore session NODE04 completed.
    ```

    画面・出力にあるRestoreを読み、Restore CountとFailed Countと対象RST04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の MgmtClass が画面・出力に表示されること
    ② ステップ2 の restored が画面・出力に表示されること
    ③ ステップ3 の Restore が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en




## IBM Spectrum Protect 8.1 > 管理クラス

### activity log 保存期間確認 監査証跡 {#c14-i0551}
*分類: 管理クラス*  ・  難易度: 初級

IBM Spectrum Protect 8.1 の 管理クラス で扱う「activity log 保存期間確認 監査証跡」は、サーバー操作とメッセージを追跡するログを保存期間確認の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 010を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** activity log 保存期間確認 監査証跡の役割を調べています。activity log 容量監視 アーカイブの説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はサーバー操作とメッセージを追跡するログを容量監視として確認する。
    - B. 障害切り分けに用いる役割はサーバー操作とメッセージを追跡するログである。 ✅
    - C. 障害切り分けに用いる役割はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。
    - D. 障害切り分けに用いる役割はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** 監査証跡・activityでBの記述「サーバー操作とメッセージを追跡するログである」に対応する項目は保存期間確認 監査証跡（activit・監査証跡）です。保存期・監査証に関する管理クラスの仕様は「サーバー操作とメッセージを追跡するログ」で、確認対象はactivit・監査証跡です。リストア・activityのA:は「サーバー操作とメッセージを追跡するログを容量監視として確認する」を述べ、対象は容量監視 アーカイブ（activit・リストア）です。棚卸・ManagemeのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・棚卸）です。切替・NodeのD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・切替）です。「activity log」は「サーバー操作とメッセージを追跡するログ」を指す用語で、保存期間確認 監査証跡（activit・監査証跡）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **activity log 保存期間確認 監査証跡**

    - 検証目的: 管理クラスのactivity log 保存期間確認 監査証跡について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY NODE の登録情報を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL010
    ```

    画面・出力には ANR1550I が含まれ、activity log 保存期間確認 監査証跡の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL010 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL010
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### activity log 復元前確認 管理クラス {#c14-i0552}
*分類: 管理クラス*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の 管理クラス で扱う「activity log 復元前確認 管理クラス」は、サーバー操作とメッセージを追跡するログを復元前確認の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 050を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** activity log 復元前確認 管理クラスの役割を調べています。policy domain 復元前確認 統合管理の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはサーバー操作とメッセージを追跡するログを復元前確認する。 ✅
    - B. 機能の説明としてはクライアントに適用するバックアップとアーカイブの規則を束ねる単位を復元前確認する。
    - C. 機能の説明としてはEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - D. 機能の説明としてはExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。

    正解: **A** ／ 難易度: 中級

    **解説:** 復元前確認・activityでAの記述「サーバー操作とメッセージを追跡するログを復元前確認する」に対応する項目は復元前確認 管理クラス（activit・復元前確）です。復元前・管理クに関する管理クラスの仕様は「サーバー操作とメッセージを追跡するログを復元前確認する」で、確認対象はactivit・復元前確認です。復元前確認・policyのB:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を復」を述べ、対象は復元前確認 統合管理（policy・復元前確）です。変更・EventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・変更）です。保護・ExpiratiのD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・保護）です。「activity log」は「サーバー操作とメッセージを追跡するログを復元前確認す」を指す用語で、復元前確認 管理クラス（activit・復元前確）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **activity log 復元前確認 管理クラス**

    - 検証目的: 管理クラスのactivity log 復元前確認 管理クラスについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY NODE の登録情報を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL050
    ```

    画面・出力には ANR1550I が含まれ、activity log 復元前確認 管理クラスの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL050 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL050
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### archive copy group 期限切れ確認 適用位置 {#c14-i0553}
*分類: 管理クラス*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の 管理クラス で扱う「archive copy group 期限切れ確認 適用位置」は、アーカイブコピーの保存期間と宛先を定めるコピー規則を期限切れ確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 034を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** archive copy group 期限切れ確認 適用位置の役割を調べています。archive copy group 宛先照合 伝搬経路の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はアーカイブコピーの保存期間と宛先を定めるコピー規則である。
    - B. 障害切り分けに用いる役割はSchedule Nameのスケジュール定義と取得時刻を記録し・開始時刻誤設定を防ぐである。
    - C. 障害切り分けに用いる役割はEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。
    - D. 障害切り分けに用いる役割はアーカイブコピーの保存期間と宛先を定めるコピー規則を期限切れ確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 期限切れ確・archiveでDの記述「アーカイブコピーの保存期間と宛先を定めるコピー規則を期限切れ確認する」に対応する項目は期限切れ確認 適用位置（archive・期限切れ）です。期限切・適用位に関する管理クラスの仕様は「アーカイブコピーの保存期間と宛先を定めるコピー規則を期限切れ確認する」で、確認対象はarchive・期限切れ確です。宛先照合・archiveのA:は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を述べ、対象は宛先照合 伝搬経路（archive・宛先照合）です。復旧・ScheduleのB:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・復旧）です。確認・EventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・確認）です。「archive copy group」は「アーカイブコピーの保存期間と宛先を定めるコピー規則を」を指す用語で、期限切れ確認 適用位置（archive・期限切れ）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **archive copy group 期限切れ確認 適用位置**

    - 検証目的: 管理クラスのarchive copy group 期限切れ確認 適用位置について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY ACTLOG の ANR メッセージを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL034
    ```

    画面・出力には ANR1550I が含まれ、archive copy group 期限切れ確認 適用位置の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL034 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL034
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### archive copy group 状態確認 集約装置 {#c14-i0554}
*分類: 管理クラス*  ・  難易度: 上級

IBM Spectrum Protect 8.1 の 管理クラス で扱う「archive copy group 状態確認 集約装置」は、アーカイブコピーの保存期間と宛先を定めるコピー規則を状態確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 074を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** archive copy group 状態確認 集約装置の役割を調べています。ポリシードメイン Policy Domain 引継ぎ記録 DOM09の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはPolicy Domainで引継ぎ記録ではポリシードメインの ノード所属からNodeNameを読みである。
    - B. 機能の説明としてはExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - C. 機能の説明としてはDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - D. 機能の説明としてはアーカイブコピーの保存期間と宛先を定めるコピー規則である。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 状態で状態確認でDの記述「アーカイブコピーの保存期間と宛先を定めるコピー規則である」に対応する項目は状態確認 集約装置（archive・状態確認）です。状態・集約装に関する管理クラスの仕様は「アーカイブコピーの保存期間と宛先を定めるコピー規則」で、確認対象はarchive・状態確認です。Polic・ポリシードのA:は「Policy Domainで引継ぎ記録ではポリシードメインの」を述べ、対象は引継ぎ記録 DOM09（Policy・ポリシー）です。サーバで復旧のB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・復旧）です。照合時のDIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・照合）です。archを状態確認という用語は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を指し、状態確認 集約装置（archive・状態確認）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **archive copy group 状態確認 集約装置**

    - 検証目的: 管理クラスのarchive copy group 状態確認 集約装置について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY ACTLOG の ANR メッセージを読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL074
    ```

    画面・出力には ANR1550I が含まれ、archive copy group 状態確認 集約装置の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL074 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL074
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### management class 保存期間確認 停止時刻 {#c14-i0555}
*分類: 管理クラス*  ・  難易度: 初級

IBM Spectrum Protect 8.1 の 管理クラス で扱う「management class 保存期間確認 停止時刻」は、ファイルのバックアップ先や保存期間を決めるポリシー要素を保存期間確認の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL002を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** management class 保存期間確認 停止時刻の役割を調べています。expiration 期限切れ確認 入力欄の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはファイルのバックアップ先や保存期間を決めるポリシー要素である。 ✅
    - B. 機能の説明としては保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認する。
    - C. 機能の説明としてはStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - D. 機能の説明としてはDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。

    正解: **A** ／ 難易度: 初級

    **解説:** 保存期間確・managemeでAの記述「ファイルのバックアップ先や保存期間を決めるポリシー要素である」に対応する項目は保存期間確認 停止時刻（managem・保存期間）です。保存期・停止時に関する管理クラスの仕様は「ファイルのバックアップ先や保存期間を決めるポリシー要素」で、確認対象はmanagem・保存期間確です。期限切れ確・expiratiのB:は「保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認する」を述べ、対象は期限切れ確認 入力欄（expirat・期限切れ）です。復旧・StartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・復旧）です。登録・DatabaseのD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・登録）です。「management class」は「ファイルのバックアップ先や保存期間を決めるポリシー要」を指す用語で、保存期間確認 停止時刻（managem・保存期間）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **management class 保存期間確認 停止時刻**

    - 検証目的: 管理クラスのmanagement class 保存期間確認 停止時刻について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。VALIDATE POLICYSET の警告を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL002
    ```

    画面・出力には ANR1550I が含まれ、management class 保存期間確認 停止時刻の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL002 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL002
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### management class 復元前確認 期限切れ {#c14-i0556}
*分類: 管理クラス*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の 管理クラス で扱う「management class 復元前確認 期限切れ」は、ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL042を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** management class 復元前確認 期限切れの役割を調べています。policy domain コマンド証跡 重大度の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はクライアントに適用するバックアップとアーカイブの規則を束ねる単位をコマンド証跡として確認する。
    - B. 表示や設定で扱う内容はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。
    - C. 表示や設定で扱う内容はファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認する。 ✅
    - D. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。

    正解: **C** ／ 難易度: 中級

    **解説:** 復元前確認・managemeでCの記述「ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認す」に対応する項目は復元前確認 期限切れ（managem・復元前確）です。復元前・期限切に関する管理クラスの仕様は「ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認す」で、確認対象はmanagem・復元前確認です。コピーグル・policyのA:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をコ」を述べ、対象はコマンド証跡 重大度（policy・コピーグ）です。変更・ActionのB:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・変更）です。照合・DatabaseのD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・照合）です。「management class」は「ファイルのバックアップ先や保存期間を決めるポリシー要」を指す用語で、復元前確認 期限切れ（managem・復元前確）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **management class 復元前確認 期限切れ**

    - 検証目的: 管理クラスのmanagement class 復元前確認 期限切れについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。VALIDATE POLICYSET の警告を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL042
    ```

    画面・出力には ANR1550I が含まれ、management class 復元前確認 期限切れの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL042 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL042
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### node コマンド証跡 マクロ実行 {#c14-i0557}
*分類: 管理クラス*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の 管理クラス で扱う「node コマンド証跡 マクロ実行」は、サーバーへ登録されたクライアントを表す管理単位をコマンド証跡の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE066を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** node コマンド証跡 マクロ実行の役割を調べています。管理クラス Management Class 権限境界の確認 MC12の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はサーバーへ登録されたクライアントを表す管理単位をコマンド証跡として確認する。 ✅
    - B. 表示や設定で扱う内容はManagement Classで権限境界の確認では管理クラスの オプション確認からDIRMCを読みである。
    - C. 表示や設定で扱う内容はAssociationの関連ノードと取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - D. 表示や設定で扱う内容はServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。

    正解: **A** ／ 難易度: 中級

    **解説:** コマンで管理クラスでAの記述「サーバーへ登録されたクライアントを表す管理単位をコマンド証跡として確」に対応する項目はコマンド証跡 マクロ実行（node・管理クラ）です。コマン・マクロに関する管理クラスの仕様は「サーバーへ登録されたクライアントを表す管理単位をコマンド証跡として確」で、確認対象はnode・管理クラスです。管理クで権限境界確のB:は「Management Classで権限境界の確認では管理クラスの」を述べ、対象は権限境界の確認 MC12（Managem・権限境界）です。監査時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・監査）です。Servを保護のD:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・保護）です。nodeを管理クラスという用語は「サーバーへ登録されたクライアントを表す管理単位をコマ」を指し、コマンド証跡 マクロ実行（node・管理クラ）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **node コマンド証跡 マクロ実行**

    - 検証目的: 管理クラスのnode コマンド証跡 マクロ実行について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY DOMAIN の詳細表示を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL066
    ```

    画面・出力には ANR1550I が含まれ、node コマンド証跡 マクロ実行の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL066 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL066
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### node ノード割当確認 保存場所 {#c14-i0558}
*分類: 管理クラス*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の 管理クラス で扱う「node ノード割当確認 保存場所」は、サーバーへ登録されたクライアントを表す管理単位をノード割当確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE026を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** node ノード割当確認 保存場所の役割を調べています。コピーグループ Backup and Archive Copy Groupの説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはサーバーへ登録されたクライアントを表す管理単位をノード割当確認する。 ✅
    - B. 機能の説明としてはBackup andで構成監査ではコピーグループの アーカイブグループからRetainVersionを読みである。
    - C. 機能の説明としてはAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。
    - D. 機能の説明としてはServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。

    正解: **A** ／ 難易度: 中級

    **解説:** ノード割当・nodeでAの記述「サーバーへ登録されたクライアントを表す管理単位をノード割当確認する」に対応する項目はノード割当確認 保存場所（node・ノード割）です。ノード・保存場に関する管理クラスの仕様は「サーバーへ登録されたクライアントを表す管理単位をノード割当確認する」で、確認対象はnode・ノード割当です。構成監査・BackupのB:は「Backup andで構成監査ではコピーグループの」を述べ、対象は構成監査 CG08（Backup・構成監査）です。棚卸・AssociatのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・棚卸）です。収集・ServerのD:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・収集）です。「node」は「サーバーへ登録されたクライアントを表す管理単位をノー」を指す用語で、ノード割当確認 保存場所（node・ノード割）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **node ノード割当確認 保存場所**

    - 検証目的: 管理クラスのnode ノード割当確認 保存場所について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY DOMAIN の詳細表示を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL026
    ```

    画面・出力には ANR1550I が含まれ、node ノード割当確認 保存場所の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL026 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL026
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### reclamation 宛先照合 集約結果 {#c14-i0559}
*分類: 管理クラス*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の 管理クラス で扱う「reclamation 宛先照合 集約結果」は、ストレージプール内の空き領域を回収する処理を宛先照合の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR018Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** reclamation 宛先照合 集約結果の役割を調べています。ポリシードメイン Policy Domain 代替経路の確認 DOM10の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はストレージプール内の空き領域を回収する処理である。 ✅
    - B. 表示や設定で扱う内容はPolicy Domainで代替経路の確認ではポリシードメインのである。
    - C. 表示や設定で扱う内容はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。
    - D. 表示や設定で扱う内容はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。

    正解: **A** ／ 難易度: 中級

    **解説:** 宛先照合・reclamatでAの記述「ストレージプール内の空き領域を回収する処理である」に対応する項目は宛先照合 集約結果（reclama・宛先照合）です。宛先・集約結に関する管理クラスの仕様は「ストレージプール内の空き領域を回収する処理」で、確認対象はreclama・宛先照合です。代替経路確・PolicyのB:は「Policy Domainで代替経路の確認ではポリシードメインの」を述べ、対象は代替経路の確認 DOM10（Policy・代替経路）です。棚卸・ActionのC:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・棚卸）です。照合・PolicyのD:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・照合）です。「reclamation」は「ストレージプール内の空き領域を回収する処理」を指す用語で、宛先照合 集約結果（reclama・宛先照合）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **reclamation 宛先照合 集約結果**

    - 検証目的: 管理クラスのreclamation 宛先照合 集約結果について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY STGPOOL の容量表示を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL018
    ```

    画面・出力には ANR1550I が含まれ、reclamation 宛先照合 集約結果の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL018 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL018
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### reclamation 容量監視 一覧画面 {#c14-i0560}
*分類: 管理クラス*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の 管理クラス で扱う「reclamation 容量監視 一覧画面」は、ストレージプール内の空き領域を回収する処理を容量監視の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR058Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** reclamation 容量監視 一覧画面の役割を調べています。reclamation 保存期間確認 画面タグの説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はストレージプール内の空き領域を回収する処理である。
    - B. 障害切り分けに用いる役割はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - C. 障害切り分けに用いる役割はCopy Groupのコピーグループと取得時刻を記録し・登録ドメインの取り違えを防ぐである。
    - D. 障害切り分けに用いる役割はストレージプール内の空き領域を回収する処理を容量監視として確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 容量監で管理クラスでDの記述「ストレージプール内の空き領域を回収する処理を容量監視として確認する」に対応する項目は容量監視 一覧画面（reclama・管理クラ）です。容量監・一覧画に関する管理クラスの仕様は「ストレージプール内の空き領域を回収する処理を容量監視として確認する」で、確認対象はreclama・管理クラスです。recla・保存期間確のA:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は保存期間確認 画面タグ（reclama・保存期間）です。クライで変更のB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・変更）です。確認時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・確認）です。reclを管理クラスという用語は「ストレージプール内の空き領域を回収する処理を容量監視」を指し、容量監視 一覧画面（reclama・管理クラ）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **reclamation 容量監視 一覧画面**

    - 検証目的: 管理クラスのreclamation 容量監視 一覧画面について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、管理クラスの対象へ進みます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR2017I Administrator ADMIN issued command QUERY DOMAIN STANDARD FORMAT=DETAILED
    Policy Domain Name STANDARD
    Backup Retention 30
    Archive Retention 365
    ```

    画面・出力には ANR2017I が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面です。QUERY STGPOOL の容量表示を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE POLICYSET STANDARD ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR1550I Policy set ACTIVE in policy domain STANDARD validated.
    Management Class STANDARD
    Destination Pool POOL058
    ```

    画面・出力には ANR1550I が含まれ、reclamation 容量監視 一覧画面の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL058 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL058
    Device Class DISK
    Estimated Capacity 100 G
    Pct Util 42.0
    ```

    画面・出力には Storage が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ANR2017I が画面・出力に表示されること
    ② ステップ2 の ANR1550I が画面・出力に表示されること
    ③ ステップ3 の Storage が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands



### 管理クラス Management Class ログとの照合 MC07 {#c14-i0561}
*分類: 管理クラス*  ・  難易度: 初級

ログとの照合では 管理クラス の 管理クラス照会 を主操作として MC07 を判定します。時刻と対象識別子への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC07 に残します。ログとの照合を補助する クライアント詳細 では DefaultManagement を補助値として MC07 へ保存します。主判定のログとの照合では管理クラスの 管理クラス照会 から ManagementClass を読み MC07 へ残します。証跡照合のログとの照合では管理クラスの ManagementClass と DefaultManagement を MC07 に保存します。記録対応のログとの照合では管理クラスの Management ClassとDefault の証跡へ MC07 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class ログとの照合 MC07に関する障害切り分けの前提を確認しています。ノード管理 Client Node 代替経路の確認 NODE10の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はClient Nodeで代替経路の確認ではノード管理の ノード照会からLastAccessを読みである。ノード管理 Client Node 代替経路の確認 NODE10固有の属性も確認対象に含める。
    - B. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - C. 表示や設定で扱う内容はManagement Classでログとの照合では管理クラスの 管理クラス照会からManagementClaである。 ✅
    - D. 表示や設定で扱う内容はDIRMCのノード登録値と取得時刻を記録し・コピーグループ未定義を防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** 管理クでログとの照でCの記述「Management Classでログとの照合では管理クラスの」に対応する項目はログとの照合 MC07（Managem・ログとの）です。管理ク・ログとに関する管理クラスの仕様は「Management Classでログとの照合では管理クラスの」で、確認対象はManagem・ログとの照です。Clien・代替経路確のA:は「Client Nodeで代替経路の確認ではノード管理の」を述べ、対象は代替経路の確認 NODE10（Client・代替経路）です。サーバで保守のB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・保守）です。計画でDIRMCのD:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・計画）です。Manaをログとの照という用語は「Management Classでログとの照合では管」を指し、ログとの照合 MC07（Managem・ログとの）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class ログとの照合 MC07**

    - 検証目的: 管理クラスのManagement Classについて操作とログを対応し、MC07のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC07 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC07の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC07 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC07
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC07のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC07 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC07のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Domain が画面・出力に表示されること
    ③ ステップ3 の DIRMC が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 代替経路の確認 MC10 {#c14-i0562}
*分類: 管理クラス*  ・  難易度: 初級

代替経路の確認では 管理クラス の 管理クラス照会 を主操作として MC10 を判定します。主経路との役割差への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC10 に残します。代替経路の確認を補助する クライアント詳細 では DefaultManagement を補助値として MC10 へ保存します。主判定の代替経路の確認では管理クラスの 管理クラス照会 から ManagementClass を読み MC10 へ残します。証跡照合の代替経路の確認では管理クラスの ManagementClass と DefaultManagement を MC10 に保存します。記録対応の代替経路の確認では管理クラスの Management ClassとDefault の証跡へ MC10 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「管理クラス Management Class 代替経路の確認 MC10」を「ノード管理 Client Node 権限境界の確認 NODE12」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はClient Nodeで権限境界の確認ではノード管理の 関連付けからAssociatedNodeを読みである。
    - B. 保守作業で参照する機能はManagement Classで代替経路の確認では管理クラスのである。 ✅
    - C. 保守作業で参照する機能はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。
    - D. 保守作業で参照する機能はDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** 管理クで代替経路確でBの記述「Management Classで代替経路の確認では管理クラスのであ」に対応する項目は代替経路の確認 MC10（Managem・代替経路）です。管理ク・代替経に関する管理クラスの仕様は「Management Classで代替経路の確認では管理クラスの」で、確認対象はManagem・代替経路確です。Clien・権限境界確のA:は「Client Nodeで権限境界の確認ではノード管理の」を述べ、対象は権限境界の確認 NODE12（Client・権限境界）です。移行時のDIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・移行）です。Dataを照合のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・照合）です。Manaを代替経路確という用語は「Management Classで代替経路の確認では」を指し、代替経路の確認 MC10（Managem・代替経路）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 代替経路の確認 MC10**

    - 検証目的: 管理クラスのManagement Classについて代替手段の成立を確認し、MC10のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC10 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC10の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC10 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC10
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC10のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC10 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC10のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Domain が画面・出力に表示されること
    ③ ステップ3 の DIRMC が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 依存関係の確認 MC13 {#c14-i0563}
*分類: 管理クラス*  ・  難易度: 初級

依存関係の確認では 管理クラス の 管理クラス照会 を主操作として MC13 を判定します。前提資源と後続処理の順序への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC13 に残します。依存関係の確認を補助する クライアント詳細 では DefaultManagement を補助値として MC13 へ保存します。主判定の依存関係の確認では管理クラスの 管理クラス照会 から ManagementClass を読み MC13 へ残します。証跡照合の依存関係の確認では管理クラスの ManagementClass と DefaultManagement を MC13 に保存します。記録対応の依存関係の確認では管理クラスの Management ClassとDefault の証跡へ MC13 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 依存関係の確認 MC13の技術的な意味を資料で確認するとき、アーカイブ運用 Archive Operation 障害切り分け ARC04との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はArchive Operationで障害切り分けではアーカイブ運用のである。
    - B. 管理対象との関係を表す説明はManagement Classで依存関係の確認では管理クラスのである。 ✅
    - C. 管理対象との関係を表す説明はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - D. 管理対象との関係を表す説明はAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** 管理クで依存関係確でBの記述「Management Classで依存関係の確認では管理クラスのであ」に対応する項目は依存関係の確認 MC13（Managem・依存関係）です。管理ク・依存関に関する管理クラスの仕様は「Management Classで依存関係の確認では管理クラスの」で、確認対象はManagem・依存関係確です。Archi・アーカイブのA:は「Archive Operationで障害切り分けではアーカイブ運用の」を述べ、対象は障害切り分け ARC04（Archive・アーカイ）です。診断時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・診断）です。Assoを抑止のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・抑止）です。Manaを依存関係確という用語は「Management Classで依存関係の確認では」を指し、依存関係の確認 MC13（Managem・依存関係）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 依存関係の確認 MC13**

    - 検証目的: 管理クラスのManagement Classについて依存資源を点検し、MC13のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC13 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC13の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC13 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC13
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC13のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC13 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC13のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Domain が画面・出力に表示されること
    ③ ステップ3 の DIRMC が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 停止前の確認 MC14 {#c14-i0564}
*分類: 管理クラス*  ・  難易度: 初級

停止前の確認では 管理クラス の クライアント詳細 を主操作として MC14 を判定します。処理中資源と未完了要求への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC14 に残します。停止前の確認を補助する オプション確認 では DIRMC を補助値として MC14 へ保存します。主判定の停止前の確認では管理クラスの クライアント詳細 から DefaultManagement を読み MC14 へ残します。証跡照合の停止前の確認では管理クラスの DefaultManagement と DIRMC を MC14 に保存します。記録対応の停止前の確認では管理クラスの Management ClassとDefault の証跡へ MC14 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 停止前の確認 MC14を保守記録に説明する必要があります。ノード管理 Client Node 性能影響の確認 NODE11と取り違えない説明はどれですか。

    - A. 仕様上の役割はClient Nodeで性能影響の確認ではノード管理の 占有量照会からLogicalFilesを読みである。
    - B. 仕様上の役割はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。
    - C. 仕様上の役割はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。サーバー日次運用 Node Name 0328固有の属性も確認対象に含める。
    - D. 仕様上の役割はManagement Classで停止前の確認では管理クラスの クライアント詳細からDefaultManagである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 管理クで停止確認でDの記述「Management Classで停止前の確認では管理クラスの」に対応する項目は停止前の確認 MC14（Managem・停止確認）です。管理ク・停止前に関する管理クラスの仕様は「Management Classで停止前の確認では管理クラスの」で、確認対象はManagem・停止確認です。Clien・性能影響確のA:は「Client Nodeで性能影響の確認ではノード管理の」を述べ、対象は性能影響の確認 NODE11（Client・性能影響）です。クライで保守のB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・保守）です。計画時のNodeのC:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・計画）です。Manaを停止確認という用語は「Management Classで停止前の確認では管」を指し、停止前の確認 MC14（Managem・停止確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 停止前の確認 MC14**

    - 検証目的: 管理クラスのManagement Classについて安全な停止条件を確認し、MC14のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC14のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC14 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC14のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC14 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC14の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC14 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC14
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Domain が画面・出力に表示されること
    ② ステップ2 の DIRMC が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 再始動後の確認 MC15 {#c14-i0565}
*分類: 管理クラス*  ・  難易度: 初級

再始動後の確認では 管理クラス の オプション確認 を主操作として MC15 を判定します。再開点と未処理データへの注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC15 に残します。再始動後の確認を補助する 管理クラス照会 では ManagementClass を補助値として MC15 へ保存します。主判定の再始動後の確認では管理クラスの オプション確認 から DIRMC を読み MC15 へ残します。証跡照合の再始動後の確認では管理クラスの DIRMC と ManagementClass を MC15 に保存します。記録対応の再始動後の確認では管理クラスの Management ClassとDefault の証跡へ MC15 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 再始動後の確認 MC15に関する障害切り分けの前提を確認しています。複製・保護 Storage Pool Protection and Nodeの機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはStorage Poolで変更後の確認では複製・保護の 検証からANR3730Iを読み・変更確認に使うである。
    - B. 機能の説明としてはActionの開始時刻と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - C. 機能の説明としてはManagement Classで再始動後の確認では管理クラスの オプション確認からDIRMCを読みである。 ✅
    - D. 機能の説明としてはDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** 管理クで再始動確認でCの記述「Management Classで再始動後の確認では管理クラスの」に対応する項目は再始動後の確認 MC15（Managem・再始動確）です。管理ク・再始動に関する管理クラスの仕様は「Management Classで再始動後の確認では管理クラスの」で、確認対象はManagem・再始動確認です。Stora・変更確認のA:は「Storage Poolで変更後の確認では複製・保護の」を述べ、対象は変更後の確認 REPL03（Storage・変更確認）です。クライで移行のB:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Action・移行）です。Dataを計画のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・計画）です。Manaを再始動確認という用語は「Management Classで再始動後の確認では」を指し、再始動後の確認 MC15（Managem・再始動確）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 再始動後の確認 MC15**

    - 検証目的: 管理クラスのManagement Classについて再始動結果を検証し、MC15のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC15のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC15 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC15の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC15 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC15
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC15のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC15 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DIRMC が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Domain が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 変更前の確認 MC02 {#c14-i0566}
*分類: 管理クラス*  ・  難易度: 初級

変更前の確認では 管理クラス の クライアント詳細 を主操作として MC02 を判定します。変更対象と非対象の境界への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC02 に残します。変更前の確認を補助する オプション確認 では DIRMC を補助値として MC02 へ保存します。主判定の変更前の確認では管理クラスの クライアント詳細 から DefaultManagement を読み MC02 へ残します。証跡照合の変更前の確認では管理クラスの DefaultManagement と DIRMC を MC02 に保存します。記録対応の変更前の確認では管理クラスの Management ClassとDefault の証跡へ MC02 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「管理クラス Management Class 変更前の確認 MC02」を「ノード管理 Client Node 通常状態の確認 NODE01」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はClient Nodeで通常状態の確認ではノード管理の ノード照会からLastAccessを読みである。ノード管理 Client Node 通常状態の確認 NODE01固有の属性も確認対象に含める。
    - B. 仕様上の役割はCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。
    - C. 仕様上の役割はManagement Classで変更前の確認では管理クラスの クライアント詳細からDefaultManagである。 ✅
    - D. 仕様上の役割はActionの開始時刻と取得時刻を記録し・失敗イベントの見落としを防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** 管理クで変更確認でCの記述「Management Classで変更前の確認では管理クラスの」に対応する項目は変更前の確認 MC02（Managem・変更確認）です。管理ク・変更前に関する管理クラスの仕様は「Management Classで変更前の確認では管理クラスの」で、確認対象はManagem・変更確認です。Clien・通常状態確のA:は「Client Nodeで通常状態の確認ではノード管理の」を述べ、対象は通常状態の確認 NODE01（Client・通常状態）です。ポリシで保守のB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・保守）です。Actiを解除のD:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Action・解除）です。Manaを変更確認という用語は「Management Classで変更前の確認では管」を指し、変更前の確認 MC02（Managem・変更確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 変更前の確認 MC02**

    - 検証目的: 管理クラスのManagement Classについて変更前の証跡を保存し、MC02のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC02のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC02 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC02のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC02 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC02の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC02 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC02
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Domain が画面・出力に表示されること
    ② ステップ2 の DIRMC が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 変更後の確認 MC03 {#c14-i0567}
*分類: 管理クラス*  ・  難易度: 初級

変更後の確認では 管理クラス の オプション確認 を主操作として MC03 を判定します。反映値と残存値への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC03 に残します。変更後の確認を補助する 管理クラス照会 では ManagementClass を補助値として MC03 へ保存します。主判定の変更後の確認では管理クラスの オプション確認 から DIRMC を読み MC03 へ残します。証跡照合の変更後の確認では管理クラスの DIRMC と ManagementClass を MC03 に保存します。記録対応の変更後の確認では管理クラスの Management ClassとDefault の証跡へ MC03 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 変更後の確認 MC03の役割を調べています。ノード管理 Client Node 変更後の確認 NODE03の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはClient Nodeで変更後の確認ではノード管理の 関連付けからAssociatedNodeを読みである。
    - B. 機能の説明としてはStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - C. 機能の説明としてはManagement Classで変更後の確認では管理クラスの オプション確認からDIRMCを読みである。 ✅
    - D. 機能の説明としてはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** 管理クで変更確認でCの記述「Management Classで変更後の確認では管理クラスの」に対応する項目は変更後の確認 MC03（Managem・変更確認）です。管理ク・変更後に関する管理クラスの仕様は「Management Classで変更後の確認では管理クラスの」で、確認対象はManagem・変更確認です。Clien・変更確認のA:は「Client Nodeで変更後の確認ではノード管理の」を述べ、対象は変更後の確認 NODE03（Client・変更確認）です。サーバで変更のB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・変更）です。Poliを抑止のD:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・抑止）です。Manaを変更確認という用語は「Management Classで変更後の確認では管」を指し、変更後の確認 MC03（Managem・変更確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 変更後の確認 MC03**

    - 検証目的: 管理クラスのManagement Classについて変更結果を検証し、MC03のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC03のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC03 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC03の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC03 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC03
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC03のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC03 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DIRMC が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Domain が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 引継ぎ記録 MC09 {#c14-i0568}
*分類: 管理クラス*  ・  難易度: 初級

引継ぎ記録では 管理クラス の オプション確認 を主操作として MC09 を判定します。次担当者が追跡できる証跡への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC09 に残します。引継ぎ記録を補助する 管理クラス照会 では ManagementClass を補助値として MC09 へ保存します。主判定の引継ぎ記録では管理クラスの オプション確認 から DIRMC を読み MC09 へ残します。証跡照合の引継ぎ記録では管理クラスの DIRMC と ManagementClass を MC09 に保存します。記録対応の引継ぎ記録では管理クラスの Management ClassとDefault の証跡へ MC09 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 引継ぎ記録 MC09を同一分類のリストア確認 Client Restore 性能影響の確認 RST11と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はClient Restoreで性能影響の確認ではリストア確認の 別名復元からrestoredを読みである。
    - B. 構成を確認する際の意味はCopy Groupのコピーグループと取得時刻を記録し・登録ドメインの取り違えを防ぐである。
    - C. 構成を確認する際の意味はManagement Classで引継ぎ記録では管理クラスの オプション確認からDIRMCを読みである。 ✅
    - D. 構成を確認する際の意味はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** 管理クで管理クラスでCの記述「Management Classで引継ぎ記録では管理クラスの」に対応する項目は引継ぎ記録 MC09（Managem・管理クラ）です。管理ク・引継ぎに関する管理クラスの仕様は「Management Classで引継ぎ記録では管理クラスの」で、確認対象はManagem・管理クラスです。Clien・性能影響確のA:は「Client Restoreで性能影響の確認ではリストア確認の」を述べ、対象は性能影響の確認 RST11（Client・性能影響）です。ポリシで移行のB:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・移行）です。Evenを計画のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・計画）です。Manaを管理クラスという用語は「Management Classで引継ぎ記録では管理」を指し、引継ぎ記録 MC09（Managem・管理クラ）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 引継ぎ記録 MC09**

    - 検証目的: 管理クラスのManagement Classについて再現可能な記録を作成し、MC09のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC09のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC09 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC09の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC09 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC09
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC09のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC09 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DIRMC が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Domain が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 復旧後の確認 MC06 {#c14-i0569}
*分類: 管理クラス*  ・  難易度: 初級

復旧後の確認では 管理クラス の オプション確認 を主操作として MC06 を判定します。再発していないことを示す値への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC06 に残します。復旧後の確認を補助する 管理クラス照会 では ManagementClass を補助値として MC06 へ保存します。主判定の復旧後の確認では管理クラスの オプション確認 から DIRMC を読み MC06 へ残します。証跡照合の復旧後の確認では管理クラスの DIRMC と ManagementClass を MC06 に保存します。記録対応の復旧後の確認では管理クラスの Management ClassとDefault の証跡へ MC06 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 復旧後の確認 MC06を保守記録に説明する必要があります。管理クラス Management Class 停止前の確認 MC14と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はManagement Classで停止前の確認では管理クラスの クライアント詳細からDefaultManagである。
    - B. 運用時に利用する技術的役割はManagement Classで復旧後の確認では管理クラスの オプション確認からDIRMCを読みである。 ✅
    - C. 運用時に利用する技術的役割はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - D. 運用時に利用する技術的役割はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** 管理クで復旧確認でBの記述「Management Classで復旧後の確認では管理クラスの」に対応する項目は復旧後の確認 MC06（Managem・復旧確認）です。管理ク・復旧後に関する管理クラスの仕様は「Management Classで復旧後の確認では管理クラスの」で、確認対象はManagem・復旧確認です。Manag・停止確認のA:は「Management Classで停止前の確認では管理クラスの」を述べ、対象は停止前の確認 MC14（Managem・停止確認）です。移行時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・移行）です。Actiを計画のD:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・計画）です。Manaを復旧確認という用語は「Management Classで復旧後の確認では管」を指し、復旧後の確認 MC06（Managem・復旧確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 復旧後の確認 MC06**

    - 検証目的: 管理クラスのManagement Classについて復旧後の安定性を確認し、MC06のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC06のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC06 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC06の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC06 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC06
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC06のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC06 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DIRMC が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Domain が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 復旧準備 MC05 {#c14-i0570}
*分類: 管理クラス*  ・  難易度: 初級

復旧準備では 管理クラス の クライアント詳細 を主操作として MC05 を判定します。再開前に必要な整合性への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC05 に残します。復旧準備を補助する オプション確認 では DIRMC を補助値として MC05 へ保存します。主判定の復旧準備では管理クラスの クライアント詳細 から DefaultManagement を読み MC05 へ残します。証跡照合の復旧準備では管理クラスの DefaultManagement と DIRMC を MC05 に保存します。記録対応の復旧準備では管理クラスの Management ClassとDefault の証跡へ MC05 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 復旧準備 MC05の技術的な意味を資料で確認するとき、ノード管理 Client Node 障害切り分け NODE04との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はClient Nodeで障害切り分けではノード管理の ノード照会からLastAccessを読み・ノードに使うである。
    - B. コマンドまたは機能の用途はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。
    - C. コマンドまたは機能の用途はNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - D. コマンドまたは機能の用途はManagement Classで復旧準備では管理クラスの クライアント詳細からDefaultManagemである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 管理クで復旧準備でDの記述「Management Classで復旧準備では管理クラスの」に対応する項目は復旧準備 MC05（Managem・復旧準備）です。管理ク・復旧準に関する管理クラスの仕様は「Management Classで復旧準備では管理クラスの」で、確認対象はManagem・復旧準備です。Clien・ノードのA:は「Client Nodeで障害切り分けではノード管理の」を述べ、対象は障害切り分け NODE04（Client・ノード）です。ポリシで変更のB:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・変更）です。解析時のNodeのC:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・解析）です。Manaを復旧準備という用語は「Management Classで復旧準備では管理ク」を指し、復旧準備 MC05（Managem・復旧準備）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 復旧準備 MC05**

    - 検証目的: 管理クラスのManagement Classについて復旧条件を確認し、MC05のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC05のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC05 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC05のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC05 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC05の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC05 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC05
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Domain が画面・出力に表示されること
    ② ステップ2 の DIRMC が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 性能影響の確認 MC11 {#c14-i0571}
*分類: 管理クラス*  ・  難易度: 初級

性能影響の確認では 管理クラス の クライアント詳細 を主操作として MC11 を判定します。処理時間と滞留箇所への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC11 に残します。性能影響の確認を補助する オプション確認 では DIRMC を補助値として MC11 へ保存します。主判定の性能影響の確認では管理クラスの クライアント詳細 から DefaultManagement を読み MC11 へ残します。証跡照合の性能影響の確認では管理クラスの DefaultManagement と DIRMC を MC11 に保存します。記録対応の性能影響の確認では管理クラスの Management ClassとDefault の証跡へ MC11 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 性能影響の確認 MC11の役割を調べています。ノード管理 Client Node 性能影響の確認 NODE11の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はClient Nodeで性能影響の確認ではノード管理の 占有量照会からLogicalFilesを読みである。
    - B. 障害切り分けに用いる役割はActionの開始時刻と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - C. 障害切り分けに用いる役割はCopy Groupのコピーグループと取得時刻を記録し・コピーグループ未定義を防ぐである。
    - D. 障害切り分けに用いる役割はManagement Classで性能影響の確認では管理クラスのである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 管理クで性能影響確でDの記述「Management Classで性能影響の確認では管理クラスのであ」に対応する項目は性能影響の確認 MC11（Managem・性能影響）です。管理ク・性能影に関する管理クラスの仕様は「Management Classで性能影響の確認では管理クラスの」で、確認対象はManagem・性能影響確です。Clien・性能影響確のA:は「Client Nodeで性能影響の確認ではノード管理の」を述べ、対象は性能影響の確認 NODE11（Client・性能影響）です。クライで移行のB:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Action・移行）です。解析時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・解析）です。Manaを性能影響確という用語は「Management Classで性能影響の確認では」を指し、性能影響の確認 MC11（Managem・性能影響）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 性能影響の確認 MC11**

    - 検証目的: 管理クラスのManagement Classについて負荷と待ちを確認し、MC11のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC11のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC11 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC11のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC11 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC11の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC11 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC11
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Domain が画面・出力に表示されること
    ② ステップ2 の DIRMC が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 構成監査 MC08 {#c14-i0572}
*分類: 管理クラス*  ・  難易度: 初級

構成監査では 管理クラス の クライアント詳細 を主操作として MC08 を判定します。定義値と稼働値の一致への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC08 に残します。構成監査を補助する オプション確認 では DIRMC を補助値として MC08 へ保存します。主判定の構成監査では管理クラスの クライアント詳細 から DefaultManagement を読み MC08 へ残します。証跡照合の構成監査では管理クラスの DefaultManagement と DIRMC を MC08 に保存します。記録対応の構成監査では管理クラスの Management ClassとDefault の証跡へ MC08 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 構成監査 MC08の設定や表示を読む前に役割を確認します。コピーグループ Backup and Archive Copy Groupではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はBackup andで代替経路の確認ではコピーグループの コピーグループ照会からVersionsDataを読である。
    - B. 一次資料が示す主目的はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - C. 一次資料が示す主目的はManagement Classで構成監査では管理クラスの クライアント詳細からDefaultManagemである。 ✅
    - D. 一次資料が示す主目的はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** 管理クで構成監査でCの記述「Management Classで構成監査では管理クラスの」に対応する項目は構成監査 MC08（Managem・構成監査）です。管理ク・構成監に関する管理クラスの仕様は「Management Classで構成監査では管理クラスの」で、確認対象はManagem・構成監査です。Backu・代替経路確のA:は「Backup andで代替経路の確認ではコピーグループの」を述べ、対象は代替経路の確認 CG10（Backup・代替経路）です。ポリシで診断のB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・診断）です。Scheを照合のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・照合）です。Manaを構成監査という用語は「Management Classで構成監査では管理ク」を指し、構成監査 MC08（Managem・構成監査）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 構成監査 MC08**

    - 検証目的: 管理クラスのManagement Classについて構成差分を監査し、MC08のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC08のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC08 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC08のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC08 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC08の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC08 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC08
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Domain が画面・出力に表示されること
    ② ステップ2 の DIRMC が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 権限境界の確認 MC12 {#c14-i0573}
*分類: 管理クラス*  ・  難易度: 初級

権限境界の確認では 管理クラス の オプション確認 を主操作として MC12 を判定します。参照操作と変更操作の分離への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC12 に残します。権限境界の確認を補助する 管理クラス照会 では ManagementClass を補助値として MC12 へ保存します。主判定の権限境界の確認では管理クラスの オプション確認 から DIRMC を読み MC12 へ残します。証跡照合の権限境界の確認では管理クラスの DIRMC と ManagementClass を MC12 に保存します。記録対応の権限境界の確認では管理クラスの Management ClassとDefault の証跡へ MC12 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 権限境界の確認 MC12について構成や状態を確認します。管理クラス Management Class 依存関係の確認 MC13ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはManagement Classで依存関係の確認では管理クラスのである。
    - B. 状態を読み取るための働きはManagement Classで権限境界の確認では管理クラスの オプション確認からDIRMCを読みである。 ✅
    - C. 状態を読み取るための働きはStorage Poolのストレージプール使用量と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - D. 状態を読み取るための働きはEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** 管理クで権限境界確でBの記述「Management Classで権限境界の確認では管理クラスの」に対応する項目は権限境界の確認 MC12（Managem・権限境界）です。管理ク・権限境に関する管理クラスの仕様は「Management Classで権限境界の確認では管理クラスの」で、確認対象はManagem・権限境界確です。Manag・依存関係確のA:は「Management Classで依存関係の確認では管理クラスの」を述べ、対象は依存関係の確認 MC13（Managem・依存関係）です。診断時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・診断）です。Evenを抑止のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・抑止）です。Manaを権限境界確という用語は「Management Classで権限境界の確認では」を指し、権限境界の確認 MC12（Managem・権限境界）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 権限境界の確認 MC12**

    - 検証目的: 管理クラスのManagement Classについて実行権限を点検し、MC12のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC12のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC12 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC12の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC12 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC12
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC12のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC12 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の DIRMC が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Domain が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 通常状態の確認 MC01 {#c14-i0574}
*分類: 管理クラス*  ・  難易度: 初級

通常状態の確認では 管理クラス の 管理クラス照会 を主操作として MC01 を判定します。基準値と現在値の差への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC01 に残します。通常状態の確認を補助する クライアント詳細 では DefaultManagement を補助値として MC01 へ保存します。主判定の通常状態の確認では管理クラスの 管理クラス照会 から ManagementClass を読み MC01 へ残します。証跡照合の通常状態の確認では管理クラスの ManagementClass と DefaultManagement を MC01 に保存します。記録対応の通常状態の確認では管理クラスの Management ClassとDefault の証跡へ MC01 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 通常状態の確認 MC01を同一分類のバックアップ運用 Incremental Backup ログとの照合 BKP07と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はIncremental Backupでログとの照合ではバックアップ運用の 増分実行からobjectsを読みである。
    - B. 管理対象との関係を表す説明はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。
    - C. 管理対象との関係を表す説明はManagement Classで通常状態の確認では管理クラスのである。 ✅
    - D. 管理対象との関係を表す説明はSchedule Nameのスケジュール定義と取得時刻を記録し・開始時刻誤設定を防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** 管理クで通常状態確でCの記述「Management Classで通常状態の確認では管理クラスのであ」に対応する項目は通常状態の確認 MC01（Managem・通常状態）です。管理ク・通常状に関する管理クラスの仕様は「Management Classで通常状態の確認では管理クラスの」で、確認対象はManagem・通常状態確です。Incre・ログとの照のA:は「Incremental Backupでログとの照合ではバックアップ運」を述べ、対象はログとの照合 BKP07（Increme・ログとの）です。クライで保守のB:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・保守）です。Scheを解除のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・解除）です。Manaを通常状態確という用語は「Management Classで通常状態の確認では」を指し、通常状態の確認 MC01（Managem・通常状態）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 通常状態の確認 MC01**

    - 検証目的: 管理クラスのManagement Classについて通常状態を確定し、MC01のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC01 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC01の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC01 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC01
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC01のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC01 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC01のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Domain が画面・出力に表示されること
    ③ ステップ3 の DIRMC が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 管理クラス Management Class 障害切り分け MC04 {#c14-i0575}
*分類: 管理クラス*  ・  難易度: 初級

障害切り分けでは 管理クラス の 管理クラス照会 を主操作として MC04 を判定します。最初に失敗した処理への注意として「既定管理クラスとinclude-exclude指定を混同する危険があります」を MC04 に残します。障害切り分けを補助する クライアント詳細 では DefaultManagement を補助値として MC04 へ保存します。主判定の障害切り分けでは管理クラスの 管理クラス照会 から ManagementClass を読み MC04 へ残します。証跡照合の障害切り分けでは管理クラスの ManagementClass と DefaultManagement を MC04 に保存します。記録対応の障害切り分けでは管理クラスの Management ClassとDefault の証跡へ MC04 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 管理クラス Management Class 障害切り分け MC04について構成や状態を確認します。コピーグループ Backup and Archive Copy Groupではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはBackup andで復旧後の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。コピーグループ Backup and Archive Copy固有の属性も確認対象に含める。
    - B. 対象資源に対する働きはManagement Classで障害切り分けでは管理クラスの 管理クラス照会からManagementClaである。 ✅
    - C. 対象資源に対する働きはStart Timeの失敗理由と取得時刻を記録し・開始時刻誤設定を防ぐである。
    - D. 対象資源に対する働きはExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** 管理クで管理クラスでBの記述「Management Classで障害切り分けでは管理クラスの」に対応する項目は障害切り分け MC04（Managem・管理クラ）です。管理ク・障害切に関する管理クラスの仕様は「Management Classで障害切り分けでは管理クラスの」で、確認対象はManagem・管理クラスです。Backu・復旧確認のA:は「Backup andで復旧後の確認ではコピーグループの」を述べ、対象は復旧後の確認 CG06（Backup・復旧確認）です。監査時のStartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・監査）です。Expiを計画のD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・計画）です。Manaを管理クラスという用語は「Management Classで障害切り分けでは管」を指し、障害切り分け MC04（Managem・管理クラ）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **管理クラス Management Class 障害切り分け MC04**

    - 検証目的: 管理クラスのManagement Classについて障害範囲を限定し、MC04のManagement ClassとDefaultを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象MC04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へQUERY MGMTCLASS MC04 ACTIVE STANDARD FORMAT=DETAILEDを指定し、MC04の管理クラス照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY MGMTCLASS MC04 ACTIVE STANDARD FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: MC04
    Policy Set Name: ACTIVE
    Management Class Name: STANDARD
    Default Management Class: Yes
    ```

    画面・出力にあるPolicyを読み、Management ClassとDefaultと対象MC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query mgmtclass -detailを指定し、MC04のクライアント詳細を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query mgmtclass -detail
    → Enter を押す
    ```

    画面・出力:
    ```text
    Domain Name: MC04 Active Policy Set: ACTIVE Default Management Class: STANDARD
    ```

    画面・出力にあるDomainを読み、Management ClassとDefaultと対象MC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の管理クラスを確認する入力画面です。COMMAND入力口へdsmc query optionを指定し、MC04のオプション確認を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> dsmc query option
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC STANDARD MC ARCHIVE KEEP30 INCLUDE /app/... STANDARD
    ```

    画面・出力にあるDIRMCを読み、Management ClassとDefaultと対象MC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Domain が画面・出力に表示されること
    ③ ステップ3 の DIRMC が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en




## IBM Spectrum Protect 8.1 > 複製・保護

### 複製・保護 Storage Pool Protection and Node Replication ログとの照合 REPL07 {#c14-i0576}
*分類: 複製・保護*  ・  難易度: 上級

ログとの照合では 複製・保護 の プール保護 を主操作として REPL07 を判定します。時刻と対象識別子への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL07 に残します。ログとの照合を補助する 複製状態 では TargetServer を補助値として REPL07 へ保存します。主判定のログとの照合では複製・保護の プール保護 から ANR0984I を読み REPL07 へ残します。証跡照合のログとの照合では複製・保護の ANR0984I と TargetServer を REPL07 に保存します。記録対応のログとの照合では複製・保護の Replication StatusとTarget Server の証跡へ REPL07 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationの設定や表示を読む前に役割を確認します。ポリシーと管理クラス Policy Domain 0005ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。
    - B. 対象資源に対する働きはStorage Poolでログとの照合では複製・保護の プール保護からANR0984Iを読みである。 ✅
    - C. 対象資源に対する働きはActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - D. 対象資源に対する働きはクライアントに適用するバックアップとアーカイブの規則を束ねる単位をノード割当確認する。policy domain ノード割当確認 保持期間固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 上級

    **解説:** ログとの対象StoraでBの記述「Storage Poolでログとの照合では複製・保護の」に対応する項目はログとの照合 REPL07（Storag・ログと・ログとの）です。保護・ログとに関する複製・保護の仕様は「Storage Poolでログとの照合では複製・保護の」で、確認対象はStora・ログと・ログとのです。Polic・巡回のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・巡回・管理クラ）です。登録時のActioのC:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Action・登録・開始時刻）です。poliをノード割当のD:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をノ」を述べ、対象はノード割当確認 保持期間（policy・ノード・保持期間）です。Storをログとの照という用語は「Storage Poolでログとの照合では複製」を指し、ログとの照合 REPL07（Storag・ログと・ログとの）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication ログとの照合 REPL07**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて操作とログを対応し、REPL07のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL07を指定し、REPL07のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL07
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 07 for PROTECT STORAGE POOL started. ANR0985I Process 07 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE07を指定し、REPL07の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE07
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE07 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE07を指定し、REPL07の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE07
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE07 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ANR0984I が画面・出力に表示されること
    ② ステップ2 の Node が画面・出力に表示されること
    ③ ステップ3 の ANR3730I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 代替経路の確認 REPL10 {#c14-i0577}
*分類: 複製・保護*  ・  難易度: 上級

代替経路の確認では 複製・保護 の プール保護 を主操作として REPL10 を判定します。主経路との役割差への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL10 に残します。代替経路の確認を補助する 複製状態 では TargetServer を補助値として REPL10 へ保存します。主判定の代替経路の確認では複製・保護の プール保護 から ANR0984I を読み REPL10 へ残します。証跡照合の代替経路の確認では複製・保護の ANR0984I と TargetServer を REPL10 に保存します。記録対応の代替経路の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL10 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationの役割を調べています。クライアントスケジュール Action 0006の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。
    - B. 表示や設定で扱う内容はStorage Poolで代替経路の確認では複製・保護の プール保護からANR0984Iを読みである。 ✅
    - C. 表示や設定で扱う内容はSchedule Nameのスケジュール定義と取得時刻を記録し・関連付け漏れを防ぐである。
    - D. 表示や設定で扱う内容はストレージプール内の空き領域を回収する処理を容量監視として確認する。reclamation 容量監視 一覧画面固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 上級

    **解説:** 代替経路対象StoraでBの記述「Storage Poolで代替経路の確認では複製・保護の」に対応する項目は代替経路の確認 REPL10（Storag・代替経・代替経路）です。保護・代替経に関する複製・保護の仕様は「Storage Poolで代替経路の確認では複製・保護の」で、確認対象はStora・代替経・代替経路です。Actio・巡回のA:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Action・巡回・開始時刻）です。保護時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・保護・スケジュ）です。reclを管理クラスのD:は「ストレージプール内の空き領域を回収する処理を容量監視として確認する」を述べ、対象は容量監視 一覧画面（reclam・管理ク・一覧画面）です。Storを代替経路確という用語は「Storage Poolで代替経路の確認では複製」を指し、代替経路の確認 REPL10（Storag・代替経・代替経路）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 代替経路の確認 REPL10**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて代替手段の成立を確認し、REPL10のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL10を指定し、REPL10のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL10
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 10 for PROTECT STORAGE POOL started. ANR0985I Process 10 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE10を指定し、REPL10の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE10
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE10 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE10を指定し、REPL10の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE10
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE10 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ANR0984I が画面・出力に表示されること
    ② ステップ2 の Node が画面・出力に表示されること
    ③ ステップ3 の ANR3730I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 依存関係の確認 REPL13 {#c14-i0578}
*分類: 複製・保護*  ・  難易度: 上級

依存関係の確認では 複製・保護 の プール保護 を主操作として REPL13 を判定します。前提資源と後続処理の順序への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL13 に残します。依存関係の確認を補助する 複製状態 では TargetServer を補助値として REPL13 へ保存します。主判定の依存関係の確認では複製・保護の プール保護 から ANR0984I を読み REPL13 へ残します。証跡照合の依存関係の確認では複製・保護の ANR0984I と TargetServer を REPL13 に保存します。記録対応の依存関係の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL13 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationを保守記録に説明する必要があります。サーバー日次運用 Server Name 0001と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はStorage Poolで依存関係の確認では複製・保護の プール保護からANR0984Iを読みである。 ✅
    - B. 保守作業で参照する機能はServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - C. 保守作業で参照する機能はStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。サーバー日次運用 Storage Pool 0265固有の属性も確認対象に含める。
    - D. 保守作業で参照する機能はサーバーへ登録されたクライアントを表す管理単位をコマンド証跡として確認する。

    正解: **A** ／ 難易度: 上級

    **解説:** 依存関係対象StoraでAの記述「Storage Poolで依存関係の確認では複製・保護の」に対応する項目は依存関係の確認 REPL13（Storag・依存関・依存関係）です。保護・依存関に関する複製・保護の仕様は「Storage Poolで依存関係の確認では複製・保護の」で、確認対象はStora・依存関・依存関係です。巡回対象ServeのB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・巡回・DBバッ）です。照合時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storag・照合・ストレー）です。nodeを管理クラスのD:は「サーバーへ登録されたクライアントを表す管理単位をコマンド証跡として確」を述べ、対象はコマンド証跡 マクロ実行（node・管理ク・マクロ実）です。Storを依存関係確という用語は「Storage Poolで依存関係の確認では複製」を指し、依存関係の確認 REPL13（Storag・依存関・依存関係）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 依存関係の確認 REPL13**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて依存資源を点検し、REPL13のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL13を指定し、REPL13のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL13
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 13 for PROTECT STORAGE POOL started. ANR0985I Process 13 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE13を指定し、REPL13の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE13
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE13 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE13を指定し、REPL13の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE13
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE13 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ANR0984I が画面・出力に表示されること
    ② ステップ2 の Node が画面・出力に表示されること
    ③ ステップ3 の ANR3730I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### 複製・保護 Storage Pool Protection and Node Replication 停止前の確認 REPL14 {#c14-i0579}
*分類: 複製・保護*  ・  難易度: 上級

停止前の確認では 複製・保護 の 複製状態 を主操作として REPL14 を判定します。処理中資源と未完了要求への注意として「PROTECT STGPOOLとREPLICATE NODEを同時実行して競合させる危険があります」を REPL14 に残します。停止前の確認を補助する 検証 では ANR3730I を補助値として REPL14 へ保存します。主判定の停止前の確認では複製・保護の 複製状態 から TargetServer を読み REPL14 へ残します。証跡照合の停止前の確認では複製・保護の TargetServer と ANR3730I を REPL14 に保存します。記録対応の停止前の確認では複製・保護の Replication StatusとTarget Server の証跡へ REPL14 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 複製・保護 Storage Pool Protection and Node Replicationに関する障害切り分けの前提を確認しています。ポリシーと管理クラス Policy Domain 0020の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。
    - B. 障害切り分けに用いる役割はDIRMCのノード登録値と取得時刻を記録し・コピーグループ未定義を防ぐである。
    - C. 障害切り分けに用いる役割はバックアップ版数と保存先を定めるコピー規則をノード割当確認する。backup copy group ノード割当確認 再同期判断固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割はStorage Poolで停止前の確認では複製・保護の 複製状態からTargetServerを読みである。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 停止確認対象StoraでDの記述「Storage Poolで停止前の確認では複製・保護の」に対応する項目は停止前の確認 REPL14（Storag・停止確・停止前の）です。保護・停止前に関する複製・保護の仕様は「Storage Poolで停止前の確認では複製・保護の」で、確認対象はStora・停止確・停止前のです。Polic・棚卸のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・棚卸・管理クラ）です。照合対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・照合・ノード登）です。ノード割時のbackuのC:は「バックアップ版数と保存先を定めるコピー規則をノード割当確認する」を述べ、対象はノード割当確認 再同期判断（backup・ノード・再同期判）です。Storを停止確認という用語は「Storage Poolで停止前の確認では複製」を指し、停止前の確認 REPL14（Storag・停止確・停止前の）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **複製・保護 Storage Pool Protection and Node Replication 停止前の確認 REPL14**

    - 検証目的: 複製・保護のStorage Pool Protection and Node Replicationについて安全な停止条件を確認し、REPL14のReplication StatusとTarget Serverを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象REPL14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へQUERY REPLICATION NODE14を指定し、REPL14の複製状態を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY REPLICATION NODE14
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE14 Target Server: DR1 Status: Complete Files Replicated: 1240
    ```

    画面・出力にあるNodeを読み、Replication StatusとTarget Serverと対象REPL14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へVALIDATE REPLICATION NODE14を指定し、REPL14の検証を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> VALIDATE REPLICATION NODE14
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR3730I Replication validation for node NODE14 completed. Differences: 0
    ```

    画面・出力にあるANR3730Iを読み、Replication StatusとTarget Serverと対象REPL14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の複製・保護を確認する入力画面です。COMMAND入力口へPROTECT STGPOOL REPL14を指定し、REPL14のプール保護を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> PROTECT STGPOOL REPL14
    → Enter を押す
    ```

    画面・出力:
    ```text
    ANR0984I Process 14 for PROTECT STORAGE POOL started. ANR0985I Process 14 completed with completion state SUCCESS.
    ```

    画面・出力にあるANR0984Iを読み、Replication StatusとTarget Serverと対象REPL14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Node が画面・出力に表示されること
    ② ステップ2 の ANR3730I が画面・出力に表示されること
    ③ ステップ3 の ANR0984I が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


