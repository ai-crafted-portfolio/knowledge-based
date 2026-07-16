---
search:
  exclude: true
---

# IBM Spectrum Protect 8.1 — 詳細 (10/12)

[← IBM Spectrum Protect 8.1 の概要へ戻る](index.md)


## IBM Spectrum Protect 8.1 > ポリシー

### ポリシーと管理クラス Policy Domain 0350 {#c14-i0476}
*分類: ポリシー*  ・  難易度: 上級

紺K解除0351ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紺K解除0351です。紺K解除0351はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録紺K解除0351です。紺K解除0351では管理クラス詳細と取得時刻を採取票紺K解除0351へ残します。紺K解除0351ではDIRMC誤設定を避けるため補助資料も照合する判断紺K解除0351です。紺K解除0351の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録紺K解除0351です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0350の技術的な意味を資料で確認するとき、storage pool 状態確認 スケジュールとの境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は状態確認でスケジュールを確認することでスケジュールを確認し・スケジュールの誤読を防ぐ。
    - B. コマンドまたは機能の用途は点検操作で判定欄を記録することで管理クラス詳を確認し・ディレクトリー管理クラス指定を防ぐ。 ✅
    - C. コマンドまたは機能の用途は照合操作で確認欄を採取することで失敗理由を確認し・日次処理順序の誤読を防ぐ。クライアントスケジュール Start Time 0048固有の属性も確認対象に含める。
    - D. コマンドまたは機能の用途は照合操作で確認欄を採取することで開始時刻を確認し・日次処理順序の誤読を防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 解除対象PolicでBの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・解除・管理ク・ディレク）です。解除時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・解除・管理ク・ディレクです。stora・状態確認のA:は「バックアップやアーカイブのデータを格納するサーバー側領域」を述べ、対象は状態確認 スケジュール（stora・状態確・スケジ・スケジュ）です。復旧時のStartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・復旧・失敗理・日次処理）です。Actiを保守のD:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Actio・保守・開始時・日次処理）です。Poliを解除という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・解除・管理ク・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0350**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0350について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Domain と 管理クラス詳細
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Domain を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY POLICYSET
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0350A
    ```

    画面・出力には SP81DD0350A が表示され、ポリシーと管理クラス Policy Domain 0350 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Domain を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL05
    Retain Extra Versions 30
    確認コード SP81DD0350B
    ```

    画面・出力には SP81DD0350B が表示され、ポリシーと管理クラス Policy Domain 0350 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Domain を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR00
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0350C
    ```

    画面・出力には SP81DD0350C が表示され、ポリシーと管理クラス Policy Domain 0350 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0350A が画面・出力に表示されること
    ② ステップ2 の SP81DD0350B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0350C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0002 {#c14-i0477}
*分類: ポリシー*  ・  難易度: 初級

緑C巡回0003ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票緑C巡回0003です。緑C巡回0003はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録緑C巡回0003です。緑C巡回0003ではディレクトリ管理クラスと取得時刻を採取票緑C巡回0003へ残します。緑C巡回0003ではDIRMC誤設定を避けるため補助資料も照合する判断緑C巡回0003です。緑C巡回0003の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録緑C巡回0003です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0002を同一分類のクライアントスケジュール Start Time 0063と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - B. コマンドまたは機能の用途はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - C. コマンドまたは機能の用途はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - D. コマンドまたは機能の用途はManagement Classでログとの照合では管理クラスの 管理クラス照会からManagementClaである。

    正解: **B** ／ 難易度: 初級

    **解説:** 巡回対象PolicでBの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Policy・巡回・ディレク）です。ポリシに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPolic・巡回・ディレクです。Start・監査のA:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・監査・失敗理由）です。登録時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・登録・イベント）です。Manaをログとの照のD:は「Management Classでログとの照合では管理クラスの」を述べ、対象はログとの照合 MC07（Manage・ログと・ログとの）です。Poliを巡回という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Policy・巡回・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0002**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0002について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0002A
    ```

    画面・出力には SP81DD0002A が表示され、ポリシーと管理クラス Policy Set 0002 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL02
    Retain Extra Versions 30
    確認コード SP81DD0002B
    ```

    画面・出力には SP81DD0002B が表示され、ポリシーと管理クラス Policy Set 0002 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0002C
    ```

    画面・出力には SP81DD0002C が表示され、ポリシーと管理クラス Policy Set 0002 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0002A が画面・出力に表示されること
    ② ステップ2 の SP81DD0002B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0002C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0017 {#c14-i0478}
*分類: ポリシー*  ・  難易度: 初級

藤R巡回0018ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票藤R巡回0018です。藤R巡回0018はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録藤R巡回0018です。藤R巡回0018ではディレクトリ管理クラスと取得時刻を採取票藤R巡回0018へ残します。藤R巡回0018では管理クラス未割当を避けるため補助資料も照合する判断藤R巡回0018です。藤R巡回0018の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録藤R巡回0018です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0017の設定や表示を読む前に役割を確認します。クライアントスケジュール Schedule Name 0039ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - B. 一次資料が示す主目的はStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - C. 一次資料が示す主目的はBackup andで権限境界の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。
    - D. 一次資料が示す主目的はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 巡回対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Policy・巡回・ディレク）です。ポリシに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPolic・巡回・ディレクです。Sched・棚卸のA:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・棚卸・スケジュ）です。照合対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storag・照合・ストレー）です。権限境界時のBackuのC:は「Backup andで権限境界の確認ではコピーグループの」を述べ、対象は権限境界の確認 CG12（Backup・権限境・確認では）です。Poliを巡回という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Policy・巡回・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0017**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0017について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0017A
    ```

    画面・出力には SP81DD0017A が表示され、ポリシーと管理クラス Policy Set 0017 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL03
    Retain Extra Versions 30
    確認コード SP81DD0017B
    ```

    画面・出力には SP81DD0017B が表示され、ポリシーと管理クラス Policy Set 0017 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0017C
    ```

    画面・出力には SP81DD0017C が表示され、ポリシーと管理クラス Policy Set 0017 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0017A が画面・出力に表示されること
    ② ステップ2 の SP81DD0017B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0017C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0032 {#c14-i0479}
*分類: ポリシー*  ・  難易度: 中級

桃M棚卸0033ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票桃M棚卸0033です。桃M棚卸0033はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録桃M棚卸0033です。桃M棚卸0033ではディレクトリ管理クラスと取得時刻を採取票桃M棚卸0033へ残します。桃M棚卸0033では登録ドメインの取り違えを避けるため補助資料も照合する判断桃M棚卸0033です。桃M棚卸0033の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録桃M棚卸0033です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0032に関する障害切り分けの前提を確認しています。ポリシーと管理クラス Policy Domain 0095の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。
    - B. 障害切り分けに用いる役割はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。
    - C. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅
    - D. 障害切り分けに用いる役割はストレージプール内の空き領域を回収する処理を期限切れ確認する。reclamation 期限切れ確認 診断採取固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** 棚卸対象PolicでCの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Policy・棚卸・ディレク）です。棚卸時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPolic・棚卸・ディレクです。Polic・変更のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・変更・管理クラ）です。抑止対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・抑止・ノード登）です。reclを診断採取のD:は「ストレージプール内の空き領域を回収する処理を期限切れ確認する」を述べ、対象は期限切れ確認 診断採取（reclam・診断採・診断採取）です。Poliを棚卸という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Policy・棚卸・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0032**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0032について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0032A
    ```

    画面・出力には SP81DD0032A が表示され、ポリシーと管理クラス Policy Set 0032 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL04
    Retain Extra Versions 30
    確認コード SP81DD0032B
    ```

    画面・出力には SP81DD0032B が表示され、ポリシーと管理クラス Policy Set 0032 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0032C
    ```

    画面・出力には SP81DD0032C が表示され、ポリシーと管理クラス Policy Set 0032 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0032A が画面・出力に表示されること
    ② ステップ2 の SP81DD0032B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0032C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0047 {#c14-i0480}
*分類: ポリシー*  ・  難易度: 中級

茶H復旧0048ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票茶H復旧0048です。茶H復旧0048はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録茶H復旧0048です。茶H復旧0048ではディレクトリ管理クラスと取得時刻を採取票茶H復旧0048へ残します。茶H復旧0048ではコピーグループ未定義を避けるため補助資料も照合する判断茶H復旧0048です。茶H復旧0048の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録茶H復旧0048です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0047を保守記録に説明する必要があります。クライアントスケジュール Action 0096と取り違えない説明はどれですか。

    - A. 仕様上の役割はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - B. 仕様上の役割はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - C. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅
    - D. 仕様上の役割はClient Nodeで障害切り分けではノード管理の ノード照会からLastAccessを読み・ノードに使うである。

    正解: **C** ／ 難易度: 中級

    **解説:** 復旧対象PolicでCの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Policy・復旧・ディレク）です。復旧時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPolic・復旧・ディレクです。Actio・変更のA:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Action・変更・開始時刻）です。照合対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databa・照合・期限切れ）です。ClieをノードのD:は「Client Nodeで障害切り分けではノード管理の」を述べ、対象は障害切り分け NODE04（Client・ノード・障害切り）です。Poliを復旧という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Policy・復旧・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0047**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0047について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0047A
    ```

    画面・出力には SP81DD0047A が表示され、ポリシーと管理クラス Policy Set 0047 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL05
    Retain Extra Versions 30
    確認コード SP81DD0047B
    ```

    画面・出力には SP81DD0047B が表示され、ポリシーと管理クラス Policy Set 0047 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0047C
    ```

    画面・出力には SP81DD0047C が表示され、ポリシーと管理クラス Policy Set 0047 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0047A が画面・出力に表示されること
    ② ステップ2 の SP81DD0047B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0047C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0062 {#c14-i0481}
*分類: ポリシー*  ・  難易度: 中級

緑C監査0063ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票緑C監査0063です。緑C監査0063はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録緑C監査0063です。緑C監査0063ではディレクトリ管理クラスと取得時刻を採取票緑C監査0063へ残します。緑C監査0063ではDIRMC誤設定を避けるため補助資料も照合する判断緑C監査0063です。緑C監査0063の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録緑C監査0063です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0062の技術的な意味を資料で確認するとき、クライアントスケジュール Event Status 0087との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - B. コマンドまたは機能の用途はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。クライアントスケジュール Event Status 0087固有の属性も確認対象に含める。
    - C. コマンドまたは機能の用途はStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。
    - D. コマンドまたは機能の用途はManagement Classで通常状態の確認では管理クラスのである。

    正解: **A** ／ 難易度: 中級

    **解説:** 監査対象PolicでAの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Policy・監査・ディレク）です。監査時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPolic・監査・ディレクです。変更対象EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・変更・イベント）です。照合時のStartのC:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・照合・失敗理由）です。Manaを通常状態確のD:は「Management Classで通常状態の確認では管理クラスの」を述べ、対象は通常状態の確認 MC01（Manage・通常状・通常状態）です。Poliを監査という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Policy・監査・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0062**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0062について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0062A
    ```

    画面・出力には SP81DD0062A が表示され、ポリシーと管理クラス Policy Set 0062 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL06
    Retain Extra Versions 30
    確認コード SP81DD0062B
    ```

    画面・出力には SP81DD0062B が表示され、ポリシーと管理クラス Policy Set 0062 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0062C
    ```

    画面・出力には SP81DD0062C が表示され、ポリシーと管理クラス Policy Set 0062 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0062A が画面・出力に表示されること
    ② ステップ2 の SP81DD0062B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0062C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0077 {#c14-i0482}
*分類: ポリシー*  ・  難易度: 中級

藤R監査0078ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票藤R監査0078です。藤R監査0078はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録藤R監査0078です。藤R監査0078ではディレクトリ管理クラスと取得時刻を採取票藤R監査0078へ残します。藤R監査0078では管理クラス未割当を避けるため補助資料も照合する判断藤R監査0078です。藤R監査0078の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録藤R監査0078です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0077について構成や状態を確認します。サーバー日次運用 Server Name 0121ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - B. 一次資料が示す主目的はActionの開始時刻と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - C. 一次資料が示す主目的はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。 ✅
    - D. 一次資料が示す主目的はArchive Operationで停止前の確認ではアーカイブ運用のである。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査対象PolicでCの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Policy・監査・ディレク）です。監査時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPolic・監査・ディレクです。Serve・診断のA:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・診断・データベ）です。解除対象ActioのB:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Action・解除・開始時刻）です。Archを停止確認のD:は「Archive Operationで停止前の確認ではアーカイブ運用の」を述べ、対象は停止前の確認 ARC14（Archiv・停止確・停止前の）です。Poliを監査という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Policy・監査・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0077**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0077について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0077A
    ```

    画面・出力には SP81DD0077A が表示され、ポリシーと管理クラス Policy Set 0077 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL00
    Retain Extra Versions 30
    確認コード SP81DD0077B
    ```

    画面・出力には SP81DD0077B が表示され、ポリシーと管理クラス Policy Set 0077 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0077C
    ```

    画面・出力には SP81DD0077C が表示され、ポリシーと管理クラス Policy Set 0077 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0077A が画面・出力に表示されること
    ② ステップ2 の SP81DD0077B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0077C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0092 {#c14-i0483}
*分類: ポリシー*  ・  難易度: 中級

桃M変更0093ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票桃M変更0093です。桃M変更0093はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録桃M変更0093です。桃M変更0093ではディレクトリ管理クラスと取得時刻を採取票桃M変更0093へ残します。桃M変更0093では登録ドメインの取り違えを避けるため補助資料も照合する判断桃M変更0093です。桃M変更0093の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録桃M変更0093です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0092の役割を調べています。ポリシーと管理クラス Management Class 0119の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅
    - B. 障害切り分けに用いる役割はManagement Classのドメイン割当と取得時刻を記録し・コピーグループ未定義を防ぐである。
    - C. 障害切り分けに用いる役割はExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。サーバー日次運用 Expiration Status 0349固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割はIncremental Backupで再始動後の確認ではバックアップ運用のである。

    正解: **A** ／ 難易度: 中級

    **解説:** 変更対象PolicでAの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Policy・変更・ディレク）です。変更時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPolic・変更・ディレクです。移行対象ManagのB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manage・移行・ドメイン）です。解除時のExpirのC:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expira・解除・ノード登）です。Incrを再始動確認のD:は「Incremental Backupで再始動後の確認ではバックアップ」を述べ、対象は再始動後の確認 BKP15（Increm・再始動・再始動後）です。Poliを変更という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Policy・変更・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0092**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0092について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0092A
    ```

    画面・出力には SP81DD0092A が表示され、ポリシーと管理クラス Policy Set 0092 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL01
    Retain Extra Versions 30
    確認コード SP81DD0092B
    ```

    画面・出力には SP81DD0092B が表示され、ポリシーと管理クラス Policy Set 0092 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0092C
    ```

    画面・出力には SP81DD0092C が表示され、ポリシーと管理クラス Policy Set 0092 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0092A が画面・出力に表示されること
    ② ステップ2 の SP81DD0092B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0092C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0107 {#c14-i0484}
*分類: ポリシー*  ・  難易度: 上級

茶H移行0108ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票茶H移行0108です。茶H移行0108はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録茶H移行0108です。茶H移行0108ではディレクトリ管理クラスと取得時刻を採取票茶H移行0108へ残します。茶H移行0108ではコピーグループ未定義を避けるため補助資料も照合する判断茶H移行0108です。茶H移行0108の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録茶H移行0108です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシーと管理クラス Policy Set 0107」を「クライアントスケジュール Association 0120」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - B. 仕様上の役割はバックアップ版数と保存先を定めるコピー規則をノード割当確認する。
    - C. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅
    - D. 仕様上の役割はClient Nodeで引継ぎ記録ではノード管理の 関連付けからAssociatedNodeを読みである。

    正解: **C** ／ 難易度: 上級

    **解説:** 移行対象PolicでCの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Policy・移行・ディレク）です。移行時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPolic・移行・ディレクです。Assoc・診断のA:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・診断・関連ノー）です。ノード割対象backuのB:は「バックアップ版数と保存先を定めるコピー規則をノード割当確認する」を述べ、対象はノード割当確認 再同期判断（backup・ノード・再同期判）です。ClieをノードのD:は「Client Nodeで引継ぎ記録ではノード管理の」を述べ、対象は引継ぎ記録 NODE09（Client・ノード・引継ぎ記）です。Poliを移行という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Policy・移行・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0107**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0107について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0107A
    ```

    画面・出力には SP81DD0107A が表示され、ポリシーと管理クラス Policy Set 0107 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL02
    Retain Extra Versions 30
    確認コード SP81DD0107B
    ```

    画面・出力には SP81DD0107B が表示され、ポリシーと管理クラス Policy Set 0107 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0107C
    ```

    画面・出力には SP81DD0107C が表示され、ポリシーと管理クラス Policy Set 0107 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0107A が画面・出力に表示されること
    ② ステップ2 の SP81DD0107B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0107C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0122 {#c14-i0485}
*分類: ポリシー*  ・  難易度: 初級

緑C診断0123ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票緑C診断0123です。緑C診断0123はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録緑C診断0123です。緑C診断0123ではディレクトリ管理クラスと取得時刻を採取票緑C診断0123へ残します。緑C診断0123ではDIRMC誤設定を避けるため補助資料も照合する判断緑C診断0123です。緑C診断0123の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録緑C診断0123です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0122を同一分類のポリシーと管理クラス Management Class 0149と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。
    - B. コマンドまたは機能の用途はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - C. コマンドまたは機能の用途はIncremental Backupで変更前の確認ではバックアップ運用のである。
    - D. コマンドまたは機能の用途はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 診断対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・診断・ディレ・ディレク）です。診断時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・診断・ディレ・ディレクです。Manag・保守のA:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Manag・保守・ドメイ・管理クラ）です。解除対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・解除・ストレ・ノード状）です。変更確認時のIncreのC:は「Incremental Backupで変更前の確認ではバックアップ運」を述べ、対象は変更前の確認 BKP02（Incre・変更確・変更前・除外規則）です。Poliを診断という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・診断・ディレ・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0122**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0122について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0122A
    ```

    画面・出力には SP81DD0122A が表示され、ポリシーと管理クラス Policy Set 0122 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL02
    Retain Extra Versions 30
    確認コード SP81DD0122B
    ```

    画面・出力には SP81DD0122B が表示され、ポリシーと管理クラス Policy Set 0122 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0122C
    ```

    画面・出力には SP81DD0122C が表示され、ポリシーと管理クラス Policy Set 0122 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0122A が画面・出力に表示されること
    ② ステップ2 の SP81DD0122B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0122C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0137 {#c14-i0486}
*分類: ポリシー*  ・  難易度: 初級

藤R診断0138ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票藤R診断0138です。藤R診断0138はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録藤R診断0138です。藤R診断0138ではディレクトリ管理クラスと取得時刻を採取票藤R診断0138へ残します。藤R診断0138では管理クラス未割当を避けるため補助資料も照合する判断藤R診断0138です。藤R診断0138の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録藤R診断0138です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0137の設定や表示を読む前に役割を確認します。ポリシーと管理クラス DIRMC 0188ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はDIRMCのノード登録値と取得時刻を記録し・登録ドメインの取り違えを防ぐである。
    - B. 一次資料が示す主目的はクライアントに適用するバックアップとアーカイブの規則を束ねる単位である。
    - C. 一次資料が示す主目的はClient Restoreで代替経路の確認ではリストア確認の 候補照会からMgmtClassを読みである。
    - D. 一次資料が示す主目的はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 診断対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・診断・ディレ・管理クラ）です。診断時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・診断・ディレ・管理クラです。収集対象ノード登録のA:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・収集・ノード・登録ドメ）です。宛先照合対象policのB:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位」を述べ、対象は宛先照合 プロファイル（polic・宛先照・プロフ・プロファ）です。代替経路時のClienのC:は「Client Restoreで代替経路の確認ではリストア確認の」を述べ、対象は代替経路の確認 RST10（Clien・代替経・代替経・置換条件）です。Poliを診断という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・診断・ディレ・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0137**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0137について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0137A
    ```

    画面・出力には SP81DD0137A が表示され、ポリシーと管理クラス Policy Set 0137 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL03
    Retain Extra Versions 30
    確認コード SP81DD0137B
    ```

    画面・出力には SP81DD0137B が表示され、ポリシーと管理クラス Policy Set 0137 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0137C
    ```

    画面・出力には SP81DD0137C が表示され、ポリシーと管理クラス Policy Set 0137 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0137A が画面・出力に表示されること
    ② ステップ2 の SP81DD0137B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0137C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0152 {#c14-i0487}
*分類: ポリシー*  ・  難易度: 中級

桃M保守0153ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票桃M保守0153です。桃M保守0153はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録桃M保守0153です。桃M保守0153ではディレクトリ管理クラスと取得時刻を採取票桃M保守0153へ残します。桃M保守0153では登録ドメインの取り違えを避けるため補助資料も照合する判断桃M保守0153です。桃M保守0153の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録桃M保守0153です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0152に関する障害切り分けの前提を確認しています。サーバー日次運用 Storage Pool 0175の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - B. 障害切り分けに用いる役割はバックアップや管理コマンドを決めた時刻に実行する定義である。
    - C. 障害切り分けに用いる役割はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - D. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 保守対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・保守・ディレ・登録ドメ）です。保守時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・保守・ディレ・登録ドメです。Stora・切替のA:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・切替・ストレ・プール容）です。宛先照合対象schedのB:は「バックアップや管理コマンドを決めた時刻に実行する定義」を述べ、対象は宛先照合 ホスト検査（sched・宛先照・ホスト・ホスト検）です。巡回時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・巡回・期限切・プール容）です。Poliを保守という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・保守・ディレ・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0152**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0152について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0152A
    ```

    画面・出力には SP81DD0152A が表示され、ポリシーと管理クラス Policy Set 0152 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL04
    Retain Extra Versions 30
    確認コード SP81DD0152B
    ```

    画面・出力には SP81DD0152B が表示され、ポリシーと管理クラス Policy Set 0152 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0152C
    ```

    画面・出力には SP81DD0152C が表示され、ポリシーと管理クラス Policy Set 0152 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0152A が画面・出力に表示されること
    ② ステップ2 の SP81DD0152B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0152C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0167 {#c14-i0488}
*分類: ポリシー*  ・  難易度: 中級

茶H切替0168ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票茶H切替0168です。茶H切替0168はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録茶H切替0168です。茶H切替0168ではディレクトリ管理クラスと取得時刻を採取票茶H切替0168へ残します。茶H切替0168ではコピーグループ未定義を避けるため補助資料も照合する判断茶H切替0168です。茶H切替0168の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録茶H切替0168です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0167を保守記録に説明する必要があります。クライアントスケジュール Start Time 0243と取り違えない説明はどれですか。

    - A. 仕様上の役割はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - B. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅
    - C. 仕様上の役割はバックアップ版数と保存先を定めるコピー規則を容量監視として確認する。
    - D. 仕様上の役割はStorage Poolで引継ぎ記録では複製・保護の 検証からANR3730Iを読み・複製・保護に使うである。

    正解: **B** ／ 難易度: 中級

    **解説:** 切替対象PolicでBの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・切替・ディレ・コピーグ）です。切替時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・切替・ディレ・コピーグです。Start・保護のA:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・保護・失敗理・失敗イベ）です。コピーグ時のbackuのC:は「バックアップ版数と保存先を定めるコピー規則を容量監視として確認する」を述べ、対象は容量監視 復元前提（backu・コピー・復元前・復元前提）です。Storを複製・保護のD:は「Storage Poolで引継ぎ記録では複製・保護の」を述べ、対象は引継ぎ記録 REPL09（Stora・複製・引継ぎ・PROT）です。Poliを切替という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・切替・ディレ・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0167**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0167について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0167A
    ```

    画面・出力には SP81DD0167A が表示され、ポリシーと管理クラス Policy Set 0167 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL05
    Retain Extra Versions 30
    確認コード SP81DD0167B
    ```

    画面・出力には SP81DD0167B が表示され、ポリシーと管理クラス Policy Set 0167 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0167C
    ```

    画面・出力には SP81DD0167C が表示され、ポリシーと管理クラス Policy Set 0167 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0167A が画面・出力に表示されること
    ② ステップ2 の SP81DD0167B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0167C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0182 {#c14-i0489}
*分類: ポリシー*  ・  難易度: 中級

緑C収集0183ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票緑C収集0183です。緑C収集0183はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録緑C収集0183です。緑C収集0183ではディレクトリ管理クラスと取得時刻を採取票緑C収集0183へ残します。緑C収集0183ではDIRMC誤設定を避けるため補助資料も照合する判断緑C収集0183です。緑C収集0183の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録緑C収集0183です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0182の技術的な意味を資料で確認するとき、クライアントスケジュール Start Time 0243との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - B. コマンドまたは機能の用途はストレージプール内の空き領域を回収する処理である。
    - C. コマンドまたは機能の用途はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - D. コマンドまたは機能の用途はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 収集対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・収集・ディレ・ディレク）です。収集時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・収集・ディレ・ディレクです。Start・保護のA:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・保護・失敗理・失敗イベ）です。状態確認対象reclaのB:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は状態確認 承認待ち（recla・状態確・承認待・承認待ち）です。監査時のExpirのC:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・監査・ノード・ノード状）です。Poliを収集という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・収集・ディレ・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0182**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0182について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0182A
    ```

    画面・出力には SP81DD0182A が表示され、ポリシーと管理クラス Policy Set 0182 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL06
    Retain Extra Versions 30
    確認コード SP81DD0182B
    ```

    画面・出力には SP81DD0182B が表示され、ポリシーと管理クラス Policy Set 0182 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0182C
    ```

    画面・出力には SP81DD0182C が表示され、ポリシーと管理クラス Policy Set 0182 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0182A が画面・出力に表示されること
    ② ステップ2 の SP81DD0182B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0182C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0197 {#c14-i0490}
*分類: ポリシー*  ・  難易度: 中級

藤R収集0198ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票藤R収集0198です。藤R収集0198はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録藤R収集0198です。藤R収集0198ではディレクトリ管理クラスと取得時刻を採取票藤R収集0198へ残します。藤R収集0198では管理クラス未割当を避けるため補助資料も照合する判断藤R収集0198です。藤R収集0198の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録藤R収集0198です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0197について構成や状態を確認します。クライアントスケジュール Schedule Name 0219ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - B. 一次資料が示す主目的はBackup andで障害切り分けではコピーグループの コピーグループ照会からVersionsDataを読みである。
    - C. 一次資料が示す主目的はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - D. 一次資料が示す主目的はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 収集対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・収集・ディレ・管理クラ）です。収集時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・収集・ディレ・管理クラです。Sched・登録のA:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Sched・登録・スケジ・失敗イベ）です。コピーグ対象BackuのB:は「Backup andで障害切り分けではコピーグループの」を述べ、対象は障害切り分け CG04（Backu・コピー・コピー・バックア）です。棚卸時のDIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・棚卸・ノード・ディレク）です。Poliを収集という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・収集・ディレ・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0197**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0197について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0197A
    ```

    画面・出力には SP81DD0197A が表示され、ポリシーと管理クラス Policy Set 0197 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL00
    Retain Extra Versions 30
    確認コード SP81DD0197B
    ```

    画面・出力には SP81DD0197B が表示され、ポリシーと管理クラス Policy Set 0197 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0197C
    ```

    画面・出力には SP81DD0197C が表示され、ポリシーと管理クラス Policy Set 0197 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0197A が画面・出力に表示されること
    ② ステップ2 の SP81DD0197B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0197C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0212 {#c14-i0491}
*分類: ポリシー*  ・  難易度: 中級

桃M登録0213ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票桃M登録0213です。桃M登録0213はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録桃M登録0213です。桃M登録0213ではディレクトリ管理クラスと取得時刻を採取票桃M登録0213へ残します。桃M登録0213では登録ドメインの取り違えを避けるため補助資料も照合する判断桃M登録0213です。桃M登録0213の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録桃M登録0213です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0212の役割を調べています。サーバー日次運用 Storage Pool 0295の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - B. 障害切り分けに用いる役割はBackup andで変更前の確認ではコピーグループの アーカイブグループからRetainVersionを読である。
    - C. 障害切り分けに用いる役割はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - D. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 登録対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・登録・ディレ・登録ドメ）です。登録時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・登録・ディレ・登録ドメです。Stora・抑止のA:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・抑止・ストレ・プール容）です。変更確認対象BackuのB:は「Backup andで変更前の確認ではコピーグループの」を述べ、対象は変更前の確認 CG02（Backu・変更確・確認で・バックア）です。棚卸時のActioのC:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Actio・棚卸・開始時・日次処理）です。Poliを登録という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・登録・ディレ・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0212**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0212について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0212A
    ```

    画面・出力には SP81DD0212A が表示され、ポリシーと管理クラス Policy Set 0212 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL01
    Retain Extra Versions 30
    確認コード SP81DD0212B
    ```

    画面・出力には SP81DD0212B が表示され、ポリシーと管理クラス Policy Set 0212 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0212C
    ```

    画面・出力には SP81DD0212C が表示され、ポリシーと管理クラス Policy Set 0212 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0212A が画面・出力に表示されること
    ② ステップ2 の SP81DD0212B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0212C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0227 {#c14-i0492}
*分類: ポリシー*  ・  難易度: 上級

茶H確認0228ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票茶H確認0228です。茶H確認0228はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録茶H確認0228です。茶H確認0228ではディレクトリ管理クラスと取得時刻を採取票茶H確認0228へ残します。茶H確認0228ではコピーグループ未定義を避けるため補助資料も照合する判断茶H確認0228です。茶H確認0228の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録茶H確認0228です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシーと管理クラス Policy Set 0227」を「サーバー日次運用 Database Backup 0277」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅
    - B. 仕様上の役割はDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - C. 仕様上の役割はManagement Classで停止前の確認では管理クラスの クライアント詳細からDefaultManagである。
    - D. 仕様上の役割はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。

    正解: **A** ／ 難易度: 上級

    **解説:** 確認対象PolicでAの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・確認・ディレ・コピーグ）です。確認時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・確認・ディレ・コピーグです。照合対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・照合・期限切・期限切れ）です。停止確認時のManagのC:は「Management Classで停止前の確認では管理クラスの」を述べ、対象は停止前の確認 MC14（Manag・停止確・停止前・既定管理）です。ノード登録を棚卸のD:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・棚卸・ノード・ディレク）です。Poliを確認という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・確認・ディレ・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0227**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0227について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0227A
    ```

    画面・出力には SP81DD0227A が表示され、ポリシーと管理クラス Policy Set 0227 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL02
    Retain Extra Versions 30
    確認コード SP81DD0227B
    ```

    画面・出力には SP81DD0227B が表示され、ポリシーと管理クラス Policy Set 0227 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0227C
    ```

    画面・出力には SP81DD0227C が表示され、ポリシーと管理クラス Policy Set 0227 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0227A が画面・出力に表示されること
    ② ステップ2 の SP81DD0227B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0227C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0242 {#c14-i0493}
*分類: ポリシー*  ・  難易度: 初級

緑C保護0243ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票緑C保護0243です。緑C保護0243はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録緑C保護0243です。緑C保護0243ではディレクトリ管理クラスと取得時刻を採取票緑C保護0243へ残します。緑C保護0243ではDIRMC誤設定を避けるため補助資料も照合する判断緑C保護0243です。緑C保護0243の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録緑C保護0243です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0242を同一分類のサーバー日次運用 Storage Pool 0280と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - B. コマンドまたは機能の用途はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - C. コマンドまたは機能の用途はDirectory-containeで停止前の確認ではストレージプールのである。
    - D. コマンドまたは機能の用途はDIRMCのノード登録値と取得時刻を記録し・登録ドメインの取り違えを防ぐである。

    正解: **A** ／ 難易度: 初級

    **解説:** 保護対象PolicでAの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・保護・ディレ・ディレク）です。保護時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・保護・ディレ・ディレクです。抑止対象StoraのB:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・抑止・ストレ・ノード状）です。停止確認時のDirecのC:は「Directory-containeで停止前の確認ではストレージプー」を述べ、対象は停止前の確認 POOL14（Direc・停止確・停止前・容量使用）です。ノード登録を監査のD:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・監査・ノード・登録ドメ）です。Poliを保護という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・保護・ディレ・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0242**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0242について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0242A
    ```

    画面・出力には SP81DD0242A が表示され、ポリシーと管理クラス Policy Set 0242 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL02
    Retain Extra Versions 30
    確認コード SP81DD0242B
    ```

    画面・出力には SP81DD0242B が表示され、ポリシーと管理クラス Policy Set 0242 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0242C
    ```

    画面・出力には SP81DD0242C が表示され、ポリシーと管理クラス Policy Set 0242 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0242A が画面・出力に表示されること
    ② ステップ2 の SP81DD0242B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0242C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0257 {#c14-i0494}
*分類: ポリシー*  ・  難易度: 初級

藤R保護0258ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票藤R保護0258です。藤R保護0258はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録藤R保護0258です。藤R保護0258ではディレクトリ管理クラスと取得時刻を採取票藤R保護0258へ残します。藤R保護0258では管理クラス未割当を避けるため補助資料も照合する判断藤R保護0258です。藤R保護0258の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録藤R保護0258です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0257の設定や表示を読む前に役割を確認します。サーバー日次運用 Storage Pool 0280ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - B. 一次資料が示す主目的はManagement Classで停止前の確認では管理クラスの クライアント詳細からDefaultManagである。
    - C. 一次資料が示す主目的はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - D. 一次資料が示す主目的はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 保護対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・保護・ディレ・管理クラ）です。保護時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・保護・ディレ・管理クラです。Stora・抑止のA:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・抑止・ストレ・ノード状）です。停止確認対象ManagのB:は「Management Classで停止前の確認では管理クラスの」を述べ、対象は停止前の確認 MC14（Manag・停止確・停止前・既定管理）です。監査時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Assoc・監査・関連ノ・日次処理）です。Poliを保護という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・保護・ディレ・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0257**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0257について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0257A
    ```

    画面・出力には SP81DD0257A が表示され、ポリシーと管理クラス Policy Set 0257 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL03
    Retain Extra Versions 30
    確認コード SP81DD0257B
    ```

    画面・出力には SP81DD0257B が表示され、ポリシーと管理クラス Policy Set 0257 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0257C
    ```

    画面・出力には SP81DD0257C が表示され、ポリシーと管理クラス Policy Set 0257 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0257A が画面・出力に表示されること
    ② ステップ2 の SP81DD0257B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0257C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0272 {#c14-i0495}
*分類: ポリシー*  ・  難易度: 中級

桃M照合0273ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票桃M照合0273です。桃M照合0273はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録桃M照合0273です。桃M照合0273ではディレクトリ管理クラスと取得時刻を採取票桃M照合0273へ残します。桃M照合0273では登録ドメインの取り違えを避けるため補助資料も照合する判断桃M照合0273です。桃M照合0273の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録桃M照合0273です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0272に関する障害切り分けの前提を確認しています。クライアントスケジュール Action 0291の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は抑止で開始時刻を証跡に残し・Actionの開始時刻と取得時刻を記録し。クライアントスケジュール Action 0291固有の属性も確認対象に含める。
    - B. 障害切り分けに用いる役割は停止確認で停止前の確認を証跡に残し・Client Nodeで停止前の確認ではノード管理の。
    - C. 障害切り分けに用いる役割は照合でディレクトリを証跡に残し・Policy Setのディレクトリ管理クラスと取得時刻を記録。 ✅
    - D. 障害切り分けに用いる役割は移行でストレージプを証跡に残し・Storage Poolのストレージプール使用量と取得時刻を。

    正解: **C** ／ 難易度: 中級

    **解説:** 照合対象PolicでCの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・照合・ディレ・登録ドメ）です。照合時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・照合・ディレ・登録ドメです。Actio・抑止のA:は「Actionの開始時刻と取得時刻を記録し」を述べ、対象はクライアントスケジュール（Actio・抑止・開始時・失敗イベ）です。停止確認対象ClienのB:は「Client Nodeで停止前の確認ではノード管理の」を述べ、対象は停止前の確認 NODE14（Clien・停止確・停止前・長期未接）です。Storを移行のD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・移行・ストレ・プール容）です。Poliを照合という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・照合・ディレ・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0272**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0272について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0272A
    ```

    画面・出力には SP81DD0272A が表示され、ポリシーと管理クラス Policy Set 0272 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL04
    Retain Extra Versions 30
    確認コード SP81DD0272B
    ```

    画面・出力には SP81DD0272B が表示され、ポリシーと管理クラス Policy Set 0272 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0272C
    ```

    画面・出力には SP81DD0272C が表示され、ポリシーと管理クラス Policy Set 0272 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0272A が画面・出力に表示されること
    ② ステップ2 の SP81DD0272B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0272C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0287 {#c14-i0496}
*分類: ポリシー*  ・  難易度: 中級

茶H抑止0288ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票茶H抑止0288です。茶H抑止0288はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録茶H抑止0288です。茶H抑止0288ではディレクトリ管理クラスと取得時刻を採取票茶H抑止0288へ残します。茶H抑止0288ではコピーグループ未定義を避けるため補助資料も照合する判断茶H抑止0288です。茶H抑止0288の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録茶H抑止0288です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0287を保守記録に説明する必要があります。expiration 容量監視 詳細表示と取り違えない説明はどれですか。

    - A. 仕様上の役割はコピーグループ未定義を避けるため・表示操作で対象欄を追跡するしてディレクトリを照合する。 ✅
    - B. 仕様上の役割は詳細表示の誤読を避けるため・詳細表示で詳細表示を確認するして詳細表示を照合する。
    - C. 仕様上の役割は長期未接続ノードを正常な保護対象を避けるため・通常状態確認で通常状態の確を確認するして通常状態の確を照合する。
    - D. 仕様上の役割はノード状態の誤読を避けるため・保守操作で監査欄を保存するして期限切れ処理を照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 抑止対象PolicでAの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・抑止・ディレ・コピーグ）です。抑止時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・抑止・ディレ・コピーグです。詳細表示対象expirのB:は「保存期間を過ぎた版やアーカイブを期限切れにする処理を容量監視として確」を述べ、対象は容量監視 詳細表示（expir・詳細表・詳細表・詳細表示）です。通常状態時のClienのC:は「Client Nodeで通常状態の確認ではノード管理の」を述べ、対象は通常状態の確認 NODE01（Clien・通常状・通常状・長期未接）です。Dataを切替のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・切替・期限切・ノード状）です。Poliを抑止という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・抑止・ディレ・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0287**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0287について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0287A
    ```

    画面・出力には SP81DD0287A が表示され、ポリシーと管理クラス Policy Set 0287 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL05
    Retain Extra Versions 30
    確認コード SP81DD0287B
    ```

    画面・出力には SP81DD0287B が表示され、ポリシーと管理クラス Policy Set 0287 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0287C
    ```

    画面・出力には SP81DD0287C が表示され、ポリシーと管理クラス Policy Set 0287 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0287A が画面・出力に表示されること
    ② ステップ2 の SP81DD0287B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0287C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0302 {#c14-i0497}
*分類: ポリシー*  ・  難易度: 中級

緑C解析0303ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票緑C解析0303です。緑C解析0303はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録緑C解析0303です。緑C解析0303ではディレクトリ管理クラスと取得時刻を採取票緑C解析0303へ残します。緑C解析0303ではDIRMC誤設定を避けるため補助資料も照合する判断緑C解析0303です。緑C解析0303の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録緑C解析0303です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0302の技術的な意味を資料で確認するとき、サーバー日次運用 Node Name 0328との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は点検操作で判定欄を記録することでディレクトリを確認し・ディレクトリー管理クラス指定を防ぐ。 ✅
    - B. コマンドまたは機能の用途は保守操作で監査欄を保存することで運用状態を確認し・ノード状態の誤読を防ぐ。
    - C. コマンドまたは機能の用途は変更確認で変更後の確認を確認することで変更後の確認を確認し・置換条件や復元先を確認せず本を防ぐ。
    - D. コマンドまたは機能の用途は復旧操作で点検欄を確認することでノード登録値を確認し・管理クラス未割当を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 解析対象PolicでAの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・解析・ディレ・ディレク）です。解析時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・解析・ディレ・ディレクです。計画対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・計画・運用状・ノード状）です。変更確認時のClienのC:は「Client Restoreで変更後の確認ではリストア確認の」を述べ、対象は変更後の確認 RST03（Clien・変更確・変更後・置換条件）です。ディレクを移行のD:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（ディレクト・移行・ノード・管理クラ）です。Poliを解析という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・解析・ディレ・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0302**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0302について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0302A
    ```

    画面・出力には SP81DD0302A が表示され、ポリシーと管理クラス Policy Set 0302 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL06
    Retain Extra Versions 30
    確認コード SP81DD0302B
    ```

    画面・出力には SP81DD0302B が表示され、ポリシーと管理クラス Policy Set 0302 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0302C
    ```

    画面・出力には SP81DD0302C が表示され、ポリシーと管理クラス Policy Set 0302 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0302A が画面・出力に表示されること
    ② ステップ2 の SP81DD0302B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0302C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0317 {#c14-i0498}
*分類: ポリシー*  ・  難易度: 中級

藤R解析0318ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票藤R解析0318です。藤R解析0318はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録藤R解析0318です。藤R解析0318ではディレクトリ管理クラスと取得時刻を採取票藤R解析0318へ残します。藤R解析0318では管理クラス未割当を避けるため補助資料も照合する判断藤R解析0318です。藤R解析0318の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録藤R解析0318です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0317について構成や状態を確認します。expiration 期限切れ確認 入力欄ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は期限切れ確認で入力欄を証跡に残し・保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ。
    - B. 一次資料が示す主目的は再始動確認で確認ではアーを証跡に残し・Archive Operationで再始動後の確認ではアーカ。
    - C. 一次資料が示す主目的は収集でイベント結果を証跡に残し・Event Statusのイベント結果と取得時刻を記録し。
    - D. 一次資料が示す主目的は解析でディレクトリを証跡に残し・Policy Setのディレクトリ管理クラスと取得時刻を記録。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 解析対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・解析・ディレ・管理クラ）です。解析時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・解析・ディレ・管理クラです。expir・期限切れ確のA:は「保存期間を過ぎた版やアーカイブを期限切れにする処理を期限切れ確認する」を述べ、対象は期限切れ確認 入力欄（expir・期限切・入力欄・入力欄の）です。再始動確対象ArchiのB:は「Archive Operationで再始動後の確認ではアーカイブ運用」を述べ、対象は再始動後の確認 ARC15（Archi・再始動・確認で・バックア）です。収集時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・収集・イベン・日次処理）です。Poliを解析という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・解析・ディレ・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0317**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0317について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0317A
    ```

    画面・出力には SP81DD0317A が表示され、ポリシーと管理クラス Policy Set 0317 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL00
    Retain Extra Versions 30
    確認コード SP81DD0317B
    ```

    画面・出力には SP81DD0317B が表示され、ポリシーと管理クラス Policy Set 0317 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0317C
    ```

    画面・出力には SP81DD0317C が表示され、ポリシーと管理クラス Policy Set 0317 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0317A が画面・出力に表示されること
    ② ステップ2 の SP81DD0317B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0317C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0332 {#c14-i0499}
*分類: ポリシー*  ・  難易度: 中級

桃M計画0333ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票桃M計画0333です。桃M計画0333はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録桃M計画0333です。桃M計画0333ではディレクトリ管理クラスと取得時刻を採取票桃M計画0333へ残します。桃M計画0333では登録ドメインの取り違えを避けるため補助資料も照合する判断桃M計画0333です。桃M計画0333の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録桃M計画0333です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Set 0332の役割を調べています。schedule 容量監視 履歴行の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はバックアップや管理コマンドを決めた時刻に実行する定義を容量監視として確認する。ノードで履歴行を確認するときは履歴行の誤読を防ぐ。
    - B. 障害切り分けに用いる役割はArchive Operationで依存関係の確認ではアーカイブ運用のである。依存関係確認で確認ではアーを確認するときはバックアップデータをアーカイを防ぐ。アーカイブ運用 Archive Operation 依存関係の確認固有の属性も確認対象に含める。
    - C. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。表示操作で対象欄を追跡するときはコピーグループ未定義を防ぐ。
    - D. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは登録ドメインの取り違えを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 計画対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・計画・ディレ・登録ドメ）です。計画時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・計画・ディレ・登録ドメです。sched・ノードのA:は「バックアップや管理コマンドを決めた時刻に実行する定義を容量監視として」を述べ、対象は容量監視 履歴行（sched・ノード・履歴行・履歴行の）です。依存関係対象ArchiのB:は「Archive Operationで依存関係の確認ではアーカイブ運用」を述べ、対象は依存関係の確認 ARC13（Archi・依存関・確認で・バックア）です。保守時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・保守・管理ク・コピーグ）です。Poliを計画という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・計画・ディレ・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0332**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0332について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0332A
    ```

    画面・出力には SP81DD0332A が表示され、ポリシーと管理クラス Policy Set 0332 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL01
    Retain Extra Versions 30
    確認コード SP81DD0332B
    ```

    画面・出力には SP81DD0332B が表示され、ポリシーと管理クラス Policy Set 0332 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0332C
    ```

    画面・出力には SP81DD0332C が表示され、ポリシーと管理クラス Policy Set 0332 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0332A が画面・出力に表示されること
    ② ステップ2 の SP81DD0332B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0332C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Set 0347 {#c14-i0500}
*分類: ポリシー*  ・  難易度: 上級

茶H解除0348ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票茶H解除0348です。茶H解除0348はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録茶H解除0348です。茶H解除0348ではディレクトリ管理クラスと取得時刻を採取票茶H解除0348へ残します。茶H解除0348ではコピーグループ未定義を避けるため補助資料も照合する判断茶H解除0348です。茶H解除0348の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録茶H解除0348です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシーと管理クラス Policy Set 0347」を「backup copy group 状態確認 文字変換」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はバックアップ版数と保存先を定めるコピー規則である。状態確認で文字変換を確認するときは文字変換の誤読を防ぐ。
    - B. 仕様上の役割はSchedule Nameのスケジュール定義と取得時刻を記録し・関連付け漏れを防ぐである。主操作で出力欄を評価するときは関連付け漏れを防ぐ。
    - C. 仕様上の役割はExpiration Statusのノード登録と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。確認操作で状態欄を整理するときはデータベースバックアップ時刻を防ぐ。
    - D. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。表示操作で対象欄を追跡するときはコピーグループ未定義を防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 解除対象PolicでDの記述「Policy Setのディレクトリ管理クラスと取得時刻を記録し」に対応する項目はPolicy Set（Polic・解除・ディレ・コピーグ）です。解除時のPolicに関するポリシーの仕様は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」で、確認対象はPoli・解除・ディレ・コピーグです。backu・状態確認のA:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は状態確認 文字変換（backu・状態確・文字変・文字変換）です。巡回対象SchedのB:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Sched・巡回・スケジ・関連付け）です。登録時のExpirのC:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・登録・ノード・データベ）です。Poliを解除という用語は「Policy Setのディレクトリ管理クラスと取得時」を指し、Policy Set（Polic・解除・ディレ・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Set 0347**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Set 0347について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Policy Set と ディレクトリ管理クラス
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0347A
    ```

    画面・出力には SP81DD0347A が表示され、ポリシーと管理クラス Policy Set 0347 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmc QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Copy Group STANDARD
    Destination DIRPOOL02
    Retain Extra Versions 30
    確認コード SP81DD0347B
    ```

    画面・出力には SP81DD0347B が表示され、ポリシーと管理クラス Policy Set 0347 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Policy Set を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR02
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0347C
    ```

    画面・出力には SP81DD0347C が表示され、ポリシーと管理クラス Policy Set 0347 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0347A が画面・出力に表示されること
    ② ステップ2 の SP81DD0347B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0347C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en




## IBM Spectrum Protect 8.1 > ポリシードメイン

### backup copy group コマンド証跡 収集装置 {#c14-i0501}
*分類: ポリシードメイン*  ・  難易度: 上級

IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「backup copy group コマンド証跡 収集装置」は、バックアップ版数と保存先を定めるコピー規則をコマンド証跡の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR073Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** 「backup copy group コマンド証跡 収集装置」を「バックアップ運用 Incremental Backup 停止前の確認 BKP14」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はIncremental Backupで停止前の確認ではバックアップ運用のである。
    - B. 仕様上の役割はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - C. 仕様上の役割はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - D. 仕様上の役割はバックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** コマンでポリシードでDの記述「バックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認す」に対応する項目はコマンド証跡 収集装置（backup・ポリシー）です。コマン・収集装に関するポリシードメインの仕様は「バックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認す」で、確認対象はbackup・ポリシードです。Incre・停止確認のA:は「Incremental Backupで停止前の確認ではバックアップ運」を述べ、対象は停止前の確認 BKP14（Increme・停止確認）です。サーバで監査のB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・監査）です。解析時のServeのC:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・解析）です。backをポリシードという用語は「バックアップ版数と保存先を定めるコピー規則をコマンド」を指し、コマンド証跡 収集装置（backup・ポリシー）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **backup copy group コマンド証跡 収集装置**

    - 検証目的: ポリシードメインのbackup copy group コマンド証跡 収集装置について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
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
    Destination Pool POOL073
    ```

    画面・出力には ANR1550I が含まれ、backup copy group コマンド証跡 収集装置の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL073 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL073
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



### backup copy group ノード割当確認 再同期判断 {#c14-i0502}
*分類: ポリシードメイン*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「backup copy group ノード割当確認 再同期判断」は、バックアップ版数と保存先を定めるコピー規則をノード割当確認の観点で確認する技術項目です。QUERY STGPOOL の容量表示とANR033Iを同じ記録で見比べることで、ノード割当漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** 「backup copy group ノード割当確認 再同期判断」を「backup copy group 保存期間確認 ルール読替」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はバックアップ版数と保存先を定めるコピー規則である。
    - B. 保守作業で参照する機能はバックアップ版数と保存先を定めるコピー規則をノード割当確認する。 ✅
    - C. 保守作業で参照する機能はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。
    - D. 保守作業で参照する機能はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。

    正解: **B** ／ 難易度: 中級

    **解説:** ノード割当・backupでBの記述「バックアップ版数と保存先を定めるコピー規則をノード割当確認する」に対応する項目はノード割当確認 再同期判断（backup・ノード割）です。ノード・再同期に関するポリシードメインの仕様は「バックアップ版数と保存先を定めるコピー規則をノード割当確認する」で、確認対象はbackup・ノード割当です。保存期間確・backupのA:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は保存期間確認 ルール読替（backup・保存期間）です。巡回・PolicyのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・巡回）です。確認・NodeのD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・確認）です。「backup copy group」は「バックアップ版数と保存先を定めるコピー規則をノード割」を指す用語で、ノード割当確認 再同期判断（backup・ノード割）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **backup copy group ノード割当確認 再同期判断**

    - 検証目的: ポリシードメインのbackup copy group ノード割当確認 再同期判断について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
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
    Destination Pool POOL033
    ```

    画面・出力には ANR1550I が含まれ、backup copy group ノード割当確認 再同期判断の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、ノード割当漏れを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL033 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL033
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



### expiration 保存期間確認 同期範囲 {#c14-i0503}
*分類: ポリシードメイン*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「expiration 保存期間確認 同期範囲」は、保存期間を過ぎた版やアーカイブを期限切れにする処理を保存期間確認の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL017を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** 「expiration 保存期間確認 同期範囲」を「management class 状態確認 イベント識別」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はファイルのバックアップ先や保存期間を決めるポリシー要素である。
    - B. 運用時に利用する技術的役割は保存期間を過ぎた版やアーカイブを期限切れにする処理である。 ✅
    - C. 運用時に利用する技術的役割はDBで障害切り分けではサーバーの DB状態からLastDatabaseを読み・サーバーDBに使うである。
    - D. 運用時に利用する技術的役割はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。

    正解: **B** ／ 難易度: 中級

    **解説:** 保存期間確・expiratiでBの記述「保存期間を過ぎた版やアーカイブを期限切れにする処理である」に対応する項目は保存期間確認 同期範囲（expirat・保存期間）です。保存期・同期範に関するポリシードメインの仕様は「保存期間を過ぎた版やアーカイブを期限切れにする処理」で、確認対象はexpirat・保存期間確です。状態確認・managemeのA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素」を述べ、対象は状態確認 イベント識別（managem・状態確認）です。サーバーD・DBのC:は「DBで障害切り分けではサーバーの DB状態からLastDatabas」を述べ、対象は障害切り分け DBBK04（DB・サーバー）です。登録・EventのD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・登録）です。「expiration」は「保存期間を過ぎた版やアーカイブを期限切れにする処理」を指す用語で、保存期間確認 同期範囲（expirat・保存期間）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **expiration 保存期間確認 同期範囲**

    - 検証目的: ポリシードメインのexpiration 保存期間確認 同期範囲について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
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
    Destination Pool POOL017
    ```

    画面・出力には ANR1550I が含まれ、expiration 保存期間確認 同期範囲の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL017 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL017
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



### expiration 復元前確認 自動処理 {#c14-i0504}
*分類: ポリシードメイン*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「expiration 復元前確認 自動処理」は、保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認の観点で確認する技術項目です。VALIDATE POLICYSET の警告とPOOL057を同じ記録で見比べることで、存在しない storage poolを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** 「expiration 復元前確認 自動処理」を「backup copy group コマンド証跡 収集装置」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認する。 ✅
    - B. 保守作業で参照する機能はバックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認する。
    - C. 保守作業で参照する機能はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - D. 保守作業で参照する機能はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。

    正解: **A** ／ 難易度: 中級

    **解説:** 復元前で復元前確認でAの記述「保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認する」に対応する項目は復元前確認 自動処理（expirat・復元前確）です。復元前・自動処に関するポリシードメインの仕様は「保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認する」で、確認対象はexpirat・復元前確認です。コマンでポリシードのB:は「バックアップ版数と保存先を定めるコピー規則をコマンド証跡として確認す」を述べ、対象はコマンド証跡 収集装置（backup・ポリシー）です。復旧時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・復旧）です。Manaを保護のD:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・保護）です。expiを復元前確認という用語は「保存期間を過ぎた版やアーカイブを期限切れにする処理を」を指し、復元前確認 自動処理（expirat・復元前確）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **expiration 復元前確認 自動処理**

    - 検証目的: ポリシードメインのexpiration 復元前確認 自動処理について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
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
    Destination Pool POOL057
    ```

    画面・出力には ANR1550I が含まれ、expiration 復元前確認 自動処理の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、存在しない storage poolを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL057 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL057
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



### policy domain 期限切れ確認 容量表示 {#c14-i0505}
*分類: ポリシードメイン*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「policy domain 期限切れ確認 容量表示」は、クライアントに適用するバックアップとアーカイブの規則を束ねる単位を期限切れ確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE041を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** 「policy domain 期限切れ確認 容量表示」を「管理クラス Management Class 権限境界の確認 MC12」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はManagement Classで権限境界の確認では管理クラスの オプション確認からDIRMCを読みである。
    - B. 運用時に利用する技術的役割はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - C. 運用時に利用する技術的役割はクライアントに適用するバックアップとアーカイブの規則を束ねる単位を期限切れ確認する。 ✅
    - D. 運用時に利用する技術的役割はStorage Poolのストレージプール使用量と取得時刻を記録し・プール容量不足の見落としを防ぐである。

    正解: **C** ／ 難易度: 中級

    **解説:** 容量表示・policyでCの記述「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を期」に対応する項目は期限切れ確認 容量表示（policy・容量表示）です。期限切・容量に関するポリシードメインの仕様は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を期」で、確認対象はpolicy・容量表示です。権限境界確・ManagemeのA:は「Management Classで権限境界の確認では管理クラスの」を述べ、対象は権限境界の確認 MC12（Managem・権限境界）です。復旧・NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・復旧）です。確認・StorageのD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・確認）です。「policy domain」は「クライアントに適用するバックアップとアーカイブの規則」を指す用語で、期限切れ確認 容量表示（policy・容量表示）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **policy domain 期限切れ確認 容量表示**

    - 検証目的: ポリシードメインのpolicy domain 期限切れ確認 容量表示について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
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
    Destination Pool POOL041
    ```

    画面・出力には ANR1550I が含まれ、policy domain 期限切れ確認 容量表示の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL041 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL041
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



### policy domain 状態確認 開始時刻 {#c14-i0506}
*分類: ポリシードメイン*  ・  難易度: 初級

IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「policy domain 状態確認 開始時刻」は、クライアントに適用するバックアップとアーカイブの規則を束ねる単位を状態確認の観点で確認する技術項目です。QUERY DOMAIN の詳細表示とNODE001を同じ記録で見比べることで、保存期間の誤認を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** 「policy domain 状態確認 開始時刻」を「ポリシードメイン Policy Domain 性能影響の確認 DOM11」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はPolicy Domainで性能影響の確認ではポリシードメインのである。
    - B. 仕様上の役割はクライアントに適用するバックアップとアーカイブの規則を束ねる単位である。 ✅
    - C. 仕様上の役割はCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。
    - D. 仕様上の役割はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** 状態確認・policyでBの記述「クライアントに適用するバックアップとアーカイブの規則を束ねる単位であ」に対応する項目は状態確認 開始時刻（policy・状態確認）です。状態・開始時に関するポリシードメインの仕様は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位」で、確認対象はpolicy・状態確認です。性能影響確・PolicyのA:は「Policy Domainで性能影響の確認ではポリシードメインの」を述べ、対象は性能影響の確認 DOM11（Policy・性能影響）です。棚卸・CopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・棚卸）です。確認・NodeのD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・確認）です。「policy domain」は「クライアントに適用するバックアップとアーカイブの規則」を指す用語で、状態確認 開始時刻（policy・状態確認）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **policy domain 状態確認 開始時刻**

    - 検証目的: ポリシードメインのpolicy domain 状態確認 開始時刻について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
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
    Destination Pool POOL001
    ```

    画面・出力には ANR1550I が含まれ、policy domain 状態確認 開始時刻の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、保存期間の誤認を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL001 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL001
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



### schedule 期限切れ確認 ドメイン値 {#c14-i0507}
*分類: ポリシードメイン*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「schedule 期限切れ確認 ドメイン値」は、バックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 049を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** 「schedule 期限切れ確認 ドメイン値」を「コピーグループ Backup and Archive Copy Group」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はBackup andで変更後の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。
    - B. 仕様上の役割はExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - C. 仕様上の役割はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - D. 仕様上の役割はバックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 期限切れ確・scheduleでDの記述「バックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認す」に対応する項目は期限切れ確認 ドメイン値（schedul・期限切れ）です。期限切・ドメイに関するポリシードメインの仕様は「バックアップや管理コマンドを決めた時刻に実行する定義を期限切れ確認す」で、確認対象はschedul・期限切れ確です。変更確認・BackupのA:は「Backup andで変更後の確認ではコピーグループの」を述べ、対象は変更後の確認 CG03（Backup・変更確認）です。復旧・ExpiratiのB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・復旧）です。登録・ActionのC:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Action・登録）です。「schedule」は「バックアップや管理コマンドを決めた時刻に実行する定義」を指す用語で、期限切れ確認 ドメイン値（schedul・期限切れ）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **schedule 期限切れ確認 ドメイン値**

    - 検証目的: ポリシードメインのschedule 期限切れ確認 ドメイン値について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
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
    Destination Pool POOL049
    ```

    画面・出力には ANR1550I が含まれ、schedule 期限切れ確認 ドメイン値の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL049 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL049
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



### schedule 状態確認 復旧手掛かり {#c14-i0508}
*分類: ポリシードメイン*  ・  難易度: 初級

IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「schedule 状態確認 復旧手掛かり」は、バックアップや管理コマンドを決めた時刻に実行する定義を状態確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 009を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** 「schedule 状態確認 復旧手掛かり」を「node 宛先照合 データソース」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はサーバーへ登録されたクライアントを表す管理単位である。
    - B. 保守作業で参照する機能はバックアップや管理コマンドを決めた時刻に実行する定義である。 ✅
    - C. 保守作業で参照する機能はServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - D. 保守作業で参照する機能はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** 復旧手掛か・scheduleでBの記述「バックアップや管理コマンドを決めた時刻に実行する定義である」に対応する項目は状態確認 復旧手掛かり（schedul・復旧手掛）です。状態・復旧手に関するポリシードメインの仕様は「バックアップや管理コマンドを決めた時刻に実行する定義」で、確認対象はschedul・復旧手掛かです。宛先照合・nodeのA:は「サーバーへ登録されたクライアントを表す管理単位」を述べ、対象は宛先照合 データソース（node・宛先照合）です。監査・ServerのC:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・監査）です。保護・AssociatのD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・保護）です。「schedule」は「バックアップや管理コマンドを決めた時刻に実行する定義」を指す用語で、状態確認 復旧手掛かり（schedul・復旧手掛）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **schedule 状態確認 復旧手掛かり**

    - 検証目的: ポリシードメインのschedule 状態確認 復旧手掛かりについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
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
    Destination Pool POOL009
    ```

    画面・出力には ANR1550I が含まれ、schedule 状態確認 復旧手掛かりの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL009 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL009
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



### storage pool 宛先照合 キーマップ {#c14-i0509}
*分類: ポリシードメイン*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「storage pool 宛先照合 キーマップ」は、バックアップやアーカイブのデータを格納するサーバー側領域を宛先照合の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 025を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** 「storage pool 宛先照合 キーマップ」を「management class 復元前確認 期限切れ」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認する。
    - B. 仕様上の役割はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - C. 仕様上の役割はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - D. 仕様上の役割はバックアップやアーカイブのデータを格納するサーバー側領域である。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 宛先照合・storageでDの記述「バックアップやアーカイブのデータを格納するサーバー側領域である」に対応する項目は宛先照合 キーマップ（storage・宛先照合）です。宛先・キーマに関するポリシードメインの仕様は「バックアップやアーカイブのデータを格納するサーバー側領域」で、確認対象はstorage・宛先照合です。復元前確認・managemeのA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認す」を述べ、対象は復元前確認 期限切れ（managem・復元前確）です。監査・StartのB:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・監査）です。照合・ScheduleのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・照合）です。「storage pool」は「バックアップやアーカイブのデータを格納するサーバー側」を指す用語で、宛先照合 キーマップ（storage・宛先照合）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **storage pool 宛先照合 キーマップ**

    - 検証目的: ポリシードメインのstorage pool 宛先照合 キーマップについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
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
    Destination Pool POOL025
    ```

    画面・出力には ANR1550I が含まれ、storage pool 宛先照合 キーマップの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL025 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL025
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



### storage pool 容量監視 翻訳表 {#c14-i0510}
*分類: ポリシードメイン*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の ポリシードメイン で扱う「storage pool 容量監視 翻訳表」は、バックアップやアーカイブのデータを格納するサーバー側領域を容量監視の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 065を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** 「storage pool 容量監視 翻訳表」を「reclamation 期限切れ確認 診断採取」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はストレージプール内の空き領域を回収する処理を期限切れ確認する。
    - B. 運用時に利用する技術的役割はバックアップやアーカイブのデータを格納するサーバー側領域を容量監視として確認する。 ✅
    - C. 運用時に利用する技術的役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・登録ドメインの取り違えを防ぐである。
    - D. 運用時に利用する技術的役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・DIRMC誤設定を防ぐである。

    正解: **B** ／ 難易度: 中級

    **解説:** 容量監でポリシードでBの記述「バックアップやアーカイブのデータを格納するサーバー側領域を容量監視と」に対応する項目は容量監視 翻訳表（storage・ポリシー）です。容量監・翻訳表に関するポリシードメインの仕様は「バックアップやアーカイブのデータを格納するサーバー側領域を容量監視と」で、確認対象はstorage・ポリシードです。recla・診断採取のA:は「ストレージプール内の空き領域を回収する処理を期限切れ確認する」を述べ、対象は期限切れ確認 診断採取（reclama・診断採取）です。変更時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・変更）です。Poliを確認のD:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・確認）です。storをポリシードという用語は「バックアップやアーカイブのデータを格納するサーバー側」を指し、容量監視 翻訳表（storage・ポリシー）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **storage pool 容量監視 翻訳表**

    - 検証目的: ポリシードメインのstorage pool 容量監視 翻訳表について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
    - 前提条件: IBM Spectrum Protect 8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の入力画面です。COMMAND ===> または ?S に最初の確認操作を入れ、ポリシードメインの対象へ進みます。
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
    Destination Pool POOL065
    ```

    画面・出力には ANR1550I が含まれ、storage pool 容量監視 翻訳表の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL065 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL065
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



### ポリシードメイン Policy Domain ログとの照合 DOM07 {#c14-i0511}
*分類: ポリシードメイン*  ・  難易度: 初級

ログとの照合では ポリシードメイン の ドメイン照会 を主操作として DOM07 を判定します。時刻と対象識別子への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM07 に残します。ログとの照合を補助する ポリシーセット では PolicySet を補助値として DOM07 へ保存します。主判定のログとの照合ではポリシードメインの ドメイン照会 から PolicyDomain を読み DOM07 へ残します。証跡照合のログとの照合ではポリシードメインの PolicyDomain と PolicySet を DOM07 に保存します。記録対応のログとの照合ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM07 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain ログとの照合 DOM07の設定や表示を読む前に役割を確認します。アーカイブ運用 Archive Operation 構成監査 ARC08ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはArchive Operationで構成監査ではアーカイブ運用のである。アーカイブ運用 Archive Operation 構成監査 ARC08固有の属性も確認対象に含める。
    - B. 対象資源に対する働きはSchedule Nameのスケジュール定義と取得時刻を記録し・開始時刻誤設定を防ぐである。
    - C. 対象資源に対する働きはPolicy Domainでログとの照合ではポリシードメインの ドメイン照会からPolicyDomainを読である。 ✅
    - D. 対象資源に対する働きはDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** ポリシでログとの照でCの記述「Policy Domainでログとの照合ではポリシードメインの」に対応する項目はログとの照合 DOM07（Policy・ログとの）です。ポリシ・ログとに関するポリシードメインの仕様は「Policy Domainでログとの照合ではポリシードメインの」で、確認対象はPolicy・ログとの照です。Archi・構成監査のA:は「Archive Operationで構成監査ではアーカイブ運用の」を述べ、対象は構成監査 ARC08（Archive・構成監査）です。クライで移行のB:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・移行）です。Dataを抑止のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・抑止）です。Poliをログとの照という用語は「Policy Domainでログとの照合ではポリシー」を指し、ログとの照合 DOM07（Policy・ログとの）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain ログとの照合 DOM07**

    - 検証目的: ポリシードメインのPolicy Domainについて操作とログを対応し、DOM07のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM07 FORMAT=DETAILEDを指定し、DOM07のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM07 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM07
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM07 ACTIVEを指定し、DOM07のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM07 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM07 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE07 FORMAT=DETAILEDを指定し、DOM07のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE07 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE07 Policy Domain Name: DOM07 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Node が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 代替経路の確認 DOM10 {#c14-i0512}
*分類: ポリシードメイン*  ・  難易度: 初級

代替経路の確認では ポリシードメイン の ドメイン照会 を主操作として DOM10 を判定します。主経路との役割差への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM10 に残します。代替経路の確認を補助する ポリシーセット では PolicySet を補助値として DOM10 へ保存します。主判定の代替経路の確認ではポリシードメインの ドメイン照会 から PolicyDomain を読み DOM10 へ残します。証跡照合の代替経路の確認ではポリシードメインの PolicyDomain と PolicySet を DOM10 に保存します。記録対応の代替経路の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM10 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 代替経路の確認 DOM10の役割を調べています。ストレージプール Directory-container Storage Poolの説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はDirectory-containeで代替経路の確認ではストレージプールのである。
    - B. 表示や設定で扱う内容はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - C. 表示や設定で扱う内容はDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - D. 表示や設定で扱う内容はPolicy Domainで代替経路の確認ではポリシードメインのである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** ポリシで代替経路確でDの記述「Policy Domainで代替経路の確認ではポリシードメインのであ」に対応する項目は代替経路の確認 DOM10（Policy・代替経路）です。ポリシ・代替経に関するポリシードメインの仕様は「Policy Domainで代替経路の確認ではポリシードメインの」で、確認対象はPolicy・代替経路確です。Direc・代替経路確のA:は「Directory-containeで代替経路の確認ではストレージプ」を述べ、対象は代替経路の確認 POOL10（Directo・代替経路）です。サーバで移行のB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・移行）です。照合時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・照合）です。Poliを代替経路確という用語は「Policy Domainで代替経路の確認ではポリシ」を指し、代替経路の確認 DOM10（Policy・代替経路）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 代替経路の確認 DOM10**

    - 検証目的: ポリシードメインのPolicy Domainについて代替手段の成立を確認し、DOM10のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM10 FORMAT=DETAILEDを指定し、DOM10のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM10 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM10
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM10 ACTIVEを指定し、DOM10のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM10 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM10 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE10 FORMAT=DETAILEDを指定し、DOM10のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE10 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE10 Policy Domain Name: DOM10 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Node が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 依存関係の確認 DOM13 {#c14-i0513}
*分類: ポリシードメイン*  ・  難易度: 初級

依存関係の確認では ポリシードメイン の ドメイン照会 を主操作として DOM13 を判定します。前提資源と後続処理の順序への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM13 に残します。依存関係の確認を補助する ポリシーセット では PolicySet を補助値として DOM13 へ保存します。主判定の依存関係の確認ではポリシードメインの ドメイン照会 から PolicyDomain を読み DOM13 へ残します。証跡照合の依存関係の確認ではポリシードメインの PolicyDomain と PolicySet を DOM13 に保存します。記録対応の依存関係の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM13 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 依存関係の確認 DOM13を保守記録に説明する必要があります。管理クラス Management Class 性能影響の確認 MC11と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はManagement Classで性能影響の確認では管理クラスのである。
    - B. 保守作業で参照する機能はStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。
    - C. 保守作業で参照する機能はSchedule Nameのスケジュール定義と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - D. 保守作業で参照する機能はPolicy Domainで依存関係の確認ではポリシードメインのである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** ポリシで依存関係確でDの記述「Policy Domainで依存関係の確認ではポリシードメインのであ」に対応する項目は依存関係の確認 DOM13（Policy・依存関係）です。ポリシ・依存関に関するポリシードメインの仕様は「Policy Domainで依存関係の確認ではポリシードメインの」で、確認対象はPolicy・依存関係確です。Manag・性能影響確のA:は「Management Classで性能影響の確認では管理クラスの」を述べ、対象は性能影響の確認 MC11（Managem・性能影響）です。クライで保守のB:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・保守）です。計画時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・計画）です。Poliを依存関係確という用語は「Policy Domainで依存関係の確認ではポリシ」を指し、依存関係の確認 DOM13（Policy・依存関係）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 依存関係の確認 DOM13**

    - 検証目的: ポリシードメインのPolicy Domainについて依存資源を点検し、DOM13のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM13 FORMAT=DETAILEDを指定し、DOM13のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM13 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM13
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM13 ACTIVEを指定し、DOM13のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM13 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM13 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE13 FORMAT=DETAILEDを指定し、DOM13のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE13 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE13 Policy Domain Name: DOM13 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Node が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 停止前の確認 DOM14 {#c14-i0514}
*分類: ポリシードメイン*  ・  難易度: 初級

停止前の確認では ポリシードメイン の ポリシーセット を主操作として DOM14 を判定します。処理中資源と未完了要求への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM14 に残します。停止前の確認を補助する ノード所属 では NodeName を補助値として DOM14 へ保存します。主判定の停止前の確認ではポリシードメインの ポリシーセット から PolicySet を読み DOM14 へ残します。証跡照合の停止前の確認ではポリシードメインの PolicySet と NodeName を DOM14 に保存します。記録対応の停止前の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM14 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 停止前の確認 DOM14に関する障害切り分けの前提を確認しています。コピーグループ Backup and Archive Copy Groupの機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はBackup andで構成監査ではコピーグループの アーカイブグループからRetainVersionを読みである。
    - B. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。
    - C. 障害切り分けに用いる役割はPolicy Domainで停止前の確認ではポリシードメインの ポリシーセットからPolicySetを読みである。 ✅
    - D. 障害切り分けに用いる役割はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** ポリシで停止確認でCの記述「Policy Domainで停止前の確認ではポリシードメインの」に対応する項目は停止前の確認 DOM14（Policy・停止確認）です。ポリシ・停止前に関するポリシードメインの仕様は「Policy Domainで停止前の確認ではポリシードメインの」で、確認対象はPolicy・停止確認です。Backu・構成監査のA:は「Backup andで構成監査ではコピーグループの」を述べ、対象は構成監査 CG08（Backup・構成監査）です。ポリシで移行のB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・移行）です。Expiを解析のD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・解析）です。Poliを停止確認という用語は「Policy Domainで停止前の確認ではポリシー」を指し、停止前の確認 DOM14（Policy・停止確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 停止前の確認 DOM14**

    - 検証目的: ポリシードメインのPolicy Domainについて安全な停止条件を確認し、DOM14のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM14 ACTIVEを指定し、DOM14のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM14 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM14 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE14 FORMAT=DETAILEDを指定し、DOM14のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE14 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE14 Policy Domain Name: DOM14 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM14 FORMAT=DETAILEDを指定し、DOM14のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM14 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM14
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Node が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 再始動後の確認 DOM15 {#c14-i0515}
*分類: ポリシードメイン*  ・  難易度: 初級

再始動後の確認では ポリシードメイン の ノード所属 を主操作として DOM15 を判定します。再開点と未処理データへの注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM15 に残します。再始動後の確認を補助する ドメイン照会 では PolicyDomain を補助値として DOM15 へ保存します。主判定の再始動後の確認ではポリシードメインの ノード所属 から NodeName を読み DOM15 へ残します。証跡照合の再始動後の確認ではポリシードメインの NodeName と PolicyDomain を DOM15 に保存します。記録対応の再始動後の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM15 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 再始動後の確認 DOM15の設定や表示を読む前に役割を確認します。アーカイブ運用 Archive Operation 通常状態の確認 ARC01ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはArchive Operationで通常状態の確認ではアーカイブ運用のである。アーカイブ運用 Archive Operation 通常状態の確認固有の属性も確認対象に含める。
    - B. 状態を読み取るための働きはManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - C. 状態を読み取るための働きはSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - D. 状態を読み取るための働きはPolicy Domainで再始動後の確認ではポリシードメインの ノード所属からNodeNameを読みである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** ポリシで再始動確認でDの記述「Policy Domainで再始動後の確認ではポリシードメインの」に対応する項目は再始動後の確認 DOM15（Policy・再始動確）です。ポリシ・再始動に関するポリシードメインの仕様は「Policy Domainで再始動後の確認ではポリシードメインの」で、確認対象はPolicy・再始動確認です。Archi・通常状態確のA:は「Archive Operationで通常状態の確認ではアーカイブ運用」を述べ、対象は通常状態の確認 ARC01（Archive・通常状態）です。ポリシで監査のB:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・監査）です。照合時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・照合）です。Poliを再始動確認という用語は「Policy Domainで再始動後の確認ではポリシ」を指し、再始動後の確認 DOM15（Policy・再始動確）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 再始動後の確認 DOM15**

    - 検証目的: ポリシードメインのPolicy Domainについて再始動結果を検証し、DOM15のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE15 FORMAT=DETAILEDを指定し、DOM15のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE15 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE15 Policy Domain Name: DOM15 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM15 FORMAT=DETAILEDを指定し、DOM15のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM15 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM15
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM15 ACTIVEを指定し、DOM15のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM15 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM15 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Node が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 変更前の確認 DOM02 {#c14-i0516}
*分類: ポリシードメイン*  ・  難易度: 初級

変更前の確認では ポリシードメイン の ポリシーセット を主操作として DOM02 を判定します。変更対象と非対象の境界への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM02 に残します。変更前の確認を補助する ノード所属 では NodeName を補助値として DOM02 へ保存します。主判定の変更前の確認ではポリシードメインの ポリシーセット から PolicySet を読み DOM02 へ残します。証跡照合の変更前の確認ではポリシードメインの PolicySet と NodeName を DOM02 に保存します。記録対応の変更前の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM02 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 変更前の確認 DOM02の役割を調べています。ストレージプール Directory-container Storage Poolの説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はPolicy Domainで変更前の確認ではポリシードメインの ポリシーセットからPolicySetを読みである。 ✅
    - B. 障害切り分けに用いる役割はDirectory-containeで障害切り分けではストレージプールのである。
    - C. 障害切り分けに用いる役割はSchedule Nameのスケジュール定義と取得時刻を記録し・開始時刻誤設定を防ぐである。
    - D. 障害切り分けに用いる役割はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。サーバー日次運用 Node Name 0283固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 初級

    **解説:** ポリシで変更確認でAの記述「Policy Domainで変更前の確認ではポリシードメインの」に対応する項目は変更前の確認 DOM02（Policy・変更確認）です。ポリシ・変更前に関するポリシードメインの仕様は「Policy Domainで変更前の確認ではポリシードメインの」で、確認対象はPolicy・変更確認です。ストレでストレージのB:は「Directory-containeで障害切り分けではストレージプー」を述べ、対象は障害切り分け POOL04（Directo・ストレー）です。移行時のSchedのC:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedul・移行）です。Nodeを抑止のD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・抑止）です。Poliを変更確認という用語は「Policy Domainで変更前の確認ではポリシー」を指し、変更前の確認 DOM02（Policy・変更確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 変更前の確認 DOM02**

    - 検証目的: ポリシードメインのPolicy Domainについて変更前の証跡を保存し、DOM02のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM02 ACTIVEを指定し、DOM02のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM02 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM02 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE02 FORMAT=DETAILEDを指定し、DOM02のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE02 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE02 Policy Domain Name: DOM02 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM02 FORMAT=DETAILEDを指定し、DOM02のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM02 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM02
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Node が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 変更後の確認 DOM03 {#c14-i0517}
*分類: ポリシードメイン*  ・  難易度: 初級

変更後の確認では ポリシードメイン の ノード所属 を主操作として DOM03 を判定します。反映値と残存値への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM03 に残します。変更後の確認を補助する ドメイン照会 では PolicyDomain を補助値として DOM03 へ保存します。主判定の変更後の確認ではポリシードメインの ノード所属 から NodeName を読み DOM03 へ残します。証跡照合の変更後の確認ではポリシードメインの NodeName と PolicyDomain を DOM03 に保存します。記録対応の変更後の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM03 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 変更後の確認 DOM03について構成や状態を確認します。ポリシードメイン Policy Domain 再始動後の確認 DOM15ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはPolicy Domainで再始動後の確認ではポリシードメインの ノード所属からNodeNameを読みである。
    - B. 状態を読み取るための働きはServer NameのDBバックアップ履歴と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - C. 状態を読み取るための働きはManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。
    - D. 状態を読み取るための働きはPolicy Domainで変更後の確認ではポリシードメインの ノード所属からNodeNameを読みである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** ポリシで変更確認でDの記述「Policy Domainで変更後の確認ではポリシードメインの」に対応する項目は変更後の確認 DOM03（Policy・変更確認）です。ポリシ・変更後に関するポリシードメインの仕様は「Policy Domainで変更後の確認ではポリシードメインの」で、確認対象はPolicy・変更確認です。Polic・再始動確認のA:は「Policy Domainで再始動後の確認ではポリシードメインの」を述べ、対象は再始動後の確認 DOM15（Policy・再始動確）です。サーバで監査のB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・監査）です。照合時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・照合）です。Poliを変更確認という用語は「Policy Domainで変更後の確認ではポリシー」を指し、変更後の確認 DOM03（Policy・変更確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 変更後の確認 DOM03**

    - 検証目的: ポリシードメインのPolicy Domainについて変更結果を検証し、DOM03のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE03 FORMAT=DETAILEDを指定し、DOM03のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE03 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE03 Policy Domain Name: DOM03 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM03 FORMAT=DETAILEDを指定し、DOM03のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM03 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM03
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM03 ACTIVEを指定し、DOM03のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM03 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM03 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Node が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 引継ぎ記録 DOM09 {#c14-i0518}
*分類: ポリシードメイン*  ・  難易度: 初級

引継ぎ記録では ポリシードメイン の ノード所属 を主操作として DOM09 を判定します。次担当者が追跡できる証跡への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM09 に残します。引継ぎ記録を補助する ドメイン照会 では PolicyDomain を補助値として DOM09 へ保存します。主判定の引継ぎ記録ではポリシードメインの ノード所属 から NodeName を読み DOM09 へ残します。証跡照合の引継ぎ記録ではポリシードメインの NodeName と PolicyDomain を DOM09 に保存します。記録対応の引継ぎ記録ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM09 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシードメイン Policy Domain 引継ぎ記録 DOM09」を「ストレージプール Directory-container Storage Pool」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はDirectory-containeで構成監査ではストレージプールのである。
    - B. 運用時に利用する技術的役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。ポリシーと管理クラス Policy Set 0062固有の属性も確認対象に含める。
    - C. 運用時に利用する技術的役割はCopy Groupのコピーグループと取得時刻を記録し・管理クラス未割当を防ぐである。
    - D. 運用時に利用する技術的役割はPolicy Domainで引継ぎ記録ではポリシードメインの ノード所属からNodeNameを読みである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** ポリシでポリシードでDの記述「Policy Domainで引継ぎ記録ではポリシードメインの」に対応する項目は引継ぎ記録 DOM09（Policy・ポリシー）です。ポリシ・引継ぎに関するポリシードメインの仕様は「Policy Domainで引継ぎ記録ではポリシードメインの」で、確認対象はPolicy・ポリシードです。Direc・構成監査のA:は「Directory-containeで構成監査ではストレージプールの」を述べ、対象は構成監査 POOL08（Directo・構成監査）です。ポリシで監査のB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・監査）です。解除時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・解除）です。Poliをポリシードという用語は「Policy Domainで引継ぎ記録ではポリシード」を指し、引継ぎ記録 DOM09（Policy・ポリシー）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 引継ぎ記録 DOM09**

    - 検証目的: ポリシードメインのPolicy Domainについて再現可能な記録を作成し、DOM09のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE09 FORMAT=DETAILEDを指定し、DOM09のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE09 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE09 Policy Domain Name: DOM09 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM09 FORMAT=DETAILEDを指定し、DOM09のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM09 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM09
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM09 ACTIVEを指定し、DOM09のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM09 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM09 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Node が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 復旧後の確認 DOM06 {#c14-i0519}
*分類: ポリシードメイン*  ・  難易度: 初級

復旧後の確認では ポリシードメイン の ノード所属 を主操作として DOM06 を判定します。再発していないことを示す値への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM06 に残します。復旧後の確認を補助する ドメイン照会 では PolicyDomain を補助値として DOM06 へ保存します。主判定の復旧後の確認ではポリシードメインの ノード所属 から NodeName を読み DOM06 へ残します。証跡照合の復旧後の確認ではポリシードメインの NodeName と PolicyDomain を DOM06 に保存します。記録対応の復旧後の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM06 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 復旧後の確認 DOM06に関する障害切り分けの前提を確認しています。バックアップ運用 Incremental Backup 変更後の確認 BKP03の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはIncremental Backupで変更後の確認ではバックアップ運用のである。
    - B. 機能の説明としてはPolicy Domainで復旧後の確認ではポリシードメインの ノード所属からNodeNameを読みである。 ✅
    - C. 機能の説明としてはPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。ポリシーと管理クラス Policy Set 0122固有の属性も確認対象に含める。
    - D. 機能の説明としてはAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** ポリシで復旧確認でBの記述「Policy Domainで復旧後の確認ではポリシードメインの」に対応する項目は復旧後の確認 DOM06（Policy・復旧確認）です。ポリシ・復旧後に関するポリシードメインの仕様は「Policy Domainで復旧後の確認ではポリシードメインの」で、確認対象はPolicy・復旧確認です。Incre・変更確認のA:は「Incremental Backupで変更後の確認ではバックアップ運」を述べ、対象は変更後の確認 BKP03（Increme・変更確認）です。診断時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・診断）です。Assoを照合のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・照合）です。Poliを復旧確認という用語は「Policy Domainで復旧後の確認ではポリシー」を指し、復旧後の確認 DOM06（Policy・復旧確認）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 復旧後の確認 DOM06**

    - 検証目的: ポリシードメインのPolicy Domainについて復旧後の安定性を確認し、DOM06のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE06 FORMAT=DETAILEDを指定し、DOM06のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE06 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE06 Policy Domain Name: DOM06 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM06 FORMAT=DETAILEDを指定し、DOM06のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM06 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM06
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM06 ACTIVEを指定し、DOM06のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM06 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM06 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Node が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 復旧準備 DOM05 {#c14-i0520}
*分類: ポリシードメイン*  ・  難易度: 初級

復旧準備では ポリシードメイン の ポリシーセット を主操作として DOM05 を判定します。再開前に必要な整合性への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM05 に残します。復旧準備を補助する ノード所属 では NodeName を補助値として DOM05 へ保存します。主判定の復旧準備ではポリシードメインの ポリシーセット から PolicySet を読み DOM05 へ残します。証跡照合の復旧準備ではポリシードメインの PolicySet と NodeName を DOM05 に保存します。記録対応の復旧準備ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM05 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 復旧準備 DOM05を保守記録に説明する必要があります。管理クラス Management Class 性能影響の確認 MC11と取り違えない説明はどれですか。

    - A. 仕様上の役割はManagement Classで性能影響の確認では管理クラスのである。管理クラス Management Class 性能影響の確認 MC11固有の属性も確認対象に含める。
    - B. 仕様上の役割はPolicy Domainで復旧準備ではポリシードメインの ポリシーセットからPolicySetを読みである。 ✅
    - C. 仕様上の役割はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - D. 仕様上の役割はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** ポリシで復旧準備でBの記述「Policy Domainで復旧準備ではポリシードメインの」に対応する項目は復旧準備 DOM05（Policy・復旧準備）です。ポリシ・復旧準に関するポリシードメインの仕様は「Policy Domainで復旧準備ではポリシードメインの」で、確認対象はPolicy・復旧準備です。Manag・性能影響確のA:は「Management Classで性能影響の確認では管理クラスの」を述べ、対象は性能影響の確認 MC11（Managem・性能影響）です。監査時のManagのC:は「Management Classのドメイン割当と取得時刻を記録し」を述べ、対象はManagement Class（Managem・監査）です。Assoを照合のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・照合）です。Poliを復旧準備という用語は「Policy Domainで復旧準備ではポリシードメ」を指し、復旧準備 DOM05（Policy・復旧準備）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 復旧準備 DOM05**

    - 検証目的: ポリシードメインのPolicy Domainについて復旧条件を確認し、DOM05のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM05 ACTIVEを指定し、DOM05のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM05 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM05 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE05 FORMAT=DETAILEDを指定し、DOM05のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE05 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE05 Policy Domain Name: DOM05 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM05 FORMAT=DETAILEDを指定し、DOM05のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM05 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM05
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Node が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 性能影響の確認 DOM11 {#c14-i0521}
*分類: ポリシードメイン*  ・  難易度: 初級

性能影響の確認では ポリシードメイン の ポリシーセット を主操作として DOM11 を判定します。処理時間と滞留箇所への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM11 に残します。性能影響の確認を補助する ノード所属 では NodeName を補助値として DOM11 へ保存します。主判定の性能影響の確認ではポリシードメインの ポリシーセット から PolicySet を読み DOM11 へ残します。証跡照合の性能影響の確認ではポリシードメインの PolicySet と NodeName を DOM11 に保存します。記録対応の性能影響の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM11 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 性能影響の確認 DOM11について構成や状態を確認します。アーカイブ運用 Archive Operation ログとの照合 ARC07ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はArchive Operationでログとの照合ではアーカイブ運用のである。
    - B. 一次資料が示す主目的はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - C. 一次資料が示す主目的はPolicy Domainで性能影響の確認ではポリシードメインのである。 ✅
    - D. 一次資料が示す主目的はStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** ポリシで性能影響確でCの記述「Policy Domainで性能影響の確認ではポリシードメインのであ」に対応する項目は性能影響の確認 DOM11（Policy・性能影響）です。ポリシ・性能影に関するポリシードメインの仕様は「Policy Domainで性能影響の確認ではポリシードメインの」で、確認対象はPolicy・性能影響確です。Archi・ログとの照のA:は「Archive Operationでログとの照合ではアーカイブ運用の」を述べ、対象はログとの照合 ARC07（Archive・ログとの）です。サーバで診断のB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・診断）です。Starを抑止のD:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・抑止）です。Poliを性能影響確という用語は「Policy Domainで性能影響の確認ではポリシ」を指し、性能影響の確認 DOM11（Policy・性能影響）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 性能影響の確認 DOM11**

    - 検証目的: ポリシードメインのPolicy Domainについて負荷と待ちを確認し、DOM11のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM11 ACTIVEを指定し、DOM11のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM11 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM11 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE11 FORMAT=DETAILEDを指定し、DOM11のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE11 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE11 Policy Domain Name: DOM11 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM11 FORMAT=DETAILEDを指定し、DOM11のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM11 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM11
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Node が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 構成監査 DOM08 {#c14-i0522}
*分類: ポリシードメイン*  ・  難易度: 初級

構成監査では ポリシードメイン の ポリシーセット を主操作として DOM08 を判定します。定義値と稼働値の一致への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM08 に残します。構成監査を補助する ノード所属 では NodeName を補助値として DOM08 へ保存します。主判定の構成監査ではポリシードメインの ポリシーセット から PolicySet を読み DOM08 へ残します。証跡照合の構成監査ではポリシードメインの PolicySet と NodeName を DOM08 に保存します。記録対応の構成監査ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM08 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 構成監査 DOM08を同一分類の管理クラス Management Class 構成監査 MC08と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はPolicy Domainで構成監査ではポリシードメインの ポリシーセットからPolicySetを読みである。 ✅
    - B. コマンドまたは機能の用途はManagement Classで構成監査では管理クラスの クライアント詳細からDefaultManagemである。
    - C. コマンドまたは機能の用途はStorage Poolのストレージプール使用量と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - D. コマンドまたは機能の用途はAssociationの関連ノードと取得時刻を記録し・失敗イベントの見落としを防ぐである。

    正解: **A** ／ 難易度: 初級

    **解説:** ポリシで構成監査でAの記述「Policy Domainで構成監査ではポリシードメインの」に対応する項目は構成監査 DOM08（Policy・構成監査）です。ポリシ・構成監に関するポリシードメインの仕様は「Policy Domainで構成監査ではポリシードメインの」で、確認対象はPolicy・構成監査です。管理クで構成監査のB:は「Management Classで構成監査では管理クラスの」を述べ、対象は構成監査 MC08（Managem・構成監査）です。監査時のStoraのC:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・監査）です。Assoを解析のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・解析）です。Poliを構成監査という用語は「Policy Domainで構成監査ではポリシードメ」を指し、構成監査 DOM08（Policy・構成監査）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 構成監査 DOM08**

    - 検証目的: ポリシードメインのPolicy Domainについて構成差分を監査し、DOM08のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM08 ACTIVEを指定し、DOM08のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM08 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM08 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE08 FORMAT=DETAILEDを指定し、DOM08のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE08 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE08 Policy Domain Name: DOM08 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM08 FORMAT=DETAILEDを指定し、DOM08のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM08 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM08
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Node が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 権限境界の確認 DOM12 {#c14-i0523}
*分類: ポリシードメイン*  ・  難易度: 初級

権限境界の確認では ポリシードメイン の ノード所属 を主操作として DOM12 を判定します。参照操作と変更操作の分離への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM12 に残します。権限境界の確認を補助する ドメイン照会 では PolicyDomain を補助値として DOM12 へ保存します。主判定の権限境界の確認ではポリシードメインの ノード所属 から NodeName を読み DOM12 へ残します。証跡照合の権限境界の確認ではポリシードメインの NodeName と PolicyDomain を DOM12 に保存します。記録対応の権限境界の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM12 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 権限境界の確認 DOM12の技術的な意味を資料で確認するとき、コピーグループ Backup and Archive Copy Groupとの境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はBackup andで権限境界の確認ではコピーグループの 管理クラス対応からBackupCopyを読みである。
    - B. 構成を確認する際の意味はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - C. 構成を確認する際の意味はDatabase Backupの期限切れ処理と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - D. 構成を確認する際の意味はPolicy Domainで権限境界の確認ではポリシードメインの ノード所属からNodeNameを読みである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** ポリシで権限境界確でDの記述「Policy Domainで権限境界の確認ではポリシードメインの」に対応する項目は権限境界の確認 DOM12（Policy・権限境界）です。ポリシ・権限境に関するポリシードメインの仕様は「Policy Domainで権限境界の確認ではポリシードメインの」で、確認対象はPolicy・権限境界確です。Backu・権限境界確のA:は「Backup andで権限境界の確認ではコピーグループの」を述べ、対象は権限境界の確認 CG12（Backup・権限境界）です。サーバで診断のB:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expirat・診断）です。照合時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databas・照合）です。Poliを権限境界確という用語は「Policy Domainで権限境界の確認ではポリシ」を指し、権限境界の確認 DOM12（Policy・権限境界）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 権限境界の確認 DOM12**

    - 検証目的: ポリシードメインのPolicy Domainについて実行権限を点検し、DOM12のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE12 FORMAT=DETAILEDを指定し、DOM12のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE12 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE12 Policy Domain Name: DOM12 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM12 FORMAT=DETAILEDを指定し、DOM12のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM12 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM12
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM12 ACTIVEを指定し、DOM12のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM12 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM12 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Node が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Policy が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 通常状態の確認 DOM01 {#c14-i0524}
*分類: ポリシードメイン*  ・  難易度: 初級

通常状態の確認では ポリシードメイン の ドメイン照会 を主操作として DOM01 を判定します。基準値と現在値の差への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM01 に残します。通常状態の確認を補助する ポリシーセット では PolicySet を補助値として DOM01 へ保存します。主判定の通常状態の確認ではポリシードメインの ドメイン照会 から PolicyDomain を読み DOM01 へ残します。証跡照合の通常状態の確認ではポリシードメインの PolicyDomain と PolicySet を DOM01 に保存します。記録対応の通常状態の確認ではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM01 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシードメイン Policy Domain 通常状態の確認 DOM01」を「コピーグループ Backup and Archive Copy Group」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はBackup andで通常状態の確認ではコピーグループの コピーグループ照会からVersionsDataを読である。
    - B. 保守作業で参照する機能はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。
    - C. 保守作業で参照する機能はPolicy Domainで通常状態の確認ではポリシードメインのである。 ✅
    - D. 保守作業で参照する機能はStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** ポリシで通常状態確でCの記述「Policy Domainで通常状態の確認ではポリシードメインのであ」に対応する項目は通常状態の確認 DOM01（Policy・通常状態）です。ポリシ・通常状に関するポリシードメインの仕様は「Policy Domainで通常状態の確認ではポリシードメインの」で、確認対象はPolicy・通常状態確です。Backu・通常状態確のA:は「Backup andで通常状態の確認ではコピーグループの」を述べ、対象は通常状態の確認 CG01（Backup・通常状態）です。ポリシで復旧のB:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・復旧）です。Starを計画のD:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・計画）です。Poliを通常状態確という用語は「Policy Domainで通常状態の確認ではポリシ」を指し、通常状態の確認 DOM01（Policy・通常状態）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 通常状態の確認 DOM01**

    - 検証目的: ポリシードメインのPolicy Domainについて通常状態を確定し、DOM01のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM01 FORMAT=DETAILEDを指定し、DOM01のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM01 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM01
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM01 ACTIVEを指定し、DOM01のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM01 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM01 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE01 FORMAT=DETAILEDを指定し、DOM01のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE01 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE01 Policy Domain Name: DOM01 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Node が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシードメイン Policy Domain 障害切り分け DOM04 {#c14-i0525}
*分類: ポリシードメイン*  ・  難易度: 初級

障害切り分けでは ポリシードメイン の ドメイン照会 を主操作として DOM04 を判定します。最初に失敗した処理への注意として「ノードを別ドメインへ登録して保持条件を誤る危険があります」を DOM04 に残します。障害切り分けを補助する ポリシーセット では PolicySet を補助値として DOM04 へ保存します。主判定の障害切り分けではポリシードメインの ドメイン照会 から PolicyDomain を読み DOM04 へ残します。証跡照合の障害切り分けではポリシードメインの PolicyDomain と PolicySet を DOM04 に保存します。記録対応の障害切り分けではポリシードメインの Domain NameとActivated Policy Set の証跡へ DOM04 を結びます。

**出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシードメイン Policy Domain 障害切り分け DOM04の技術的な意味を資料で確認するとき、ストレージプール Directory-container Storage Poolとの境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はDirectory-containeで再始動後の確認ではストレージプールのである。
    - B. 管理対象との関係を表す説明はPolicy Domainで障害切り分けではポリシードメインの ドメイン照会からPolicyDomainを読である。 ✅
    - C. 管理対象との関係を表す説明はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。
    - D. 管理対象との関係を表す説明はStorage Poolのストレージプール使用量と取得時刻を記録し・期限切れ処理の未実行を防ぐである。サーバー日次運用 Storage Pool 0325固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 初級

    **解説:** ポリシでポリシードでBの記述「Policy Domainで障害切り分けではポリシードメインの」に対応する項目は障害切り分け DOM04（Policy・ポリシー）です。ポリシ・障害切に関するポリシードメインの仕様は「Policy Domainで障害切り分けではポリシードメインの」で、確認対象はPolicy・ポリシードです。Direc・再始動確認のA:は「Directory-containeで再始動後の確認ではストレージプ」を述べ、対象は再始動後の確認 POOL15（Directo・再始動確）です。診断時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・診断）です。Storを計画のD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Storage・計画）です。Poliをポリシードという用語は「Policy Domainで障害切り分けではポリシー」を指し、障害切り分け DOM04（Policy・ポリシー）に該当します。

    **出典:** SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシードメイン Policy Domain 障害切り分け DOM04**

    - 検証目的: ポリシードメインのPolicy Domainについて障害範囲を限定し、DOM04のDomain NameとActivated Policy Setを実出力で確認する。
    - 前提条件: IBM Spectrum Protect 8.1の参照権限を持ち、対象DOM04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: IBM Spectrum Protect 8.1の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY DOMAIN DOM04 FORMAT=DETAILEDを指定し、DOM04のドメイン照会を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY DOMAIN DOM04 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM04
    Activated Policy Set: ACTIVE
    Number of Nodes: 12
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY POLICYSET DOM04 ACTIVEを指定し、DOM04のポリシーセットを表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY POLICYSET DOM04 ACTIVE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain Name: DOM04 Policy Set Name: ACTIVE Default Mgmt Class: STANDARD
    ```

    画面・出力にあるPolicyを読み、Domain NameとActivated Policy Setと対象DOM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1のポリシードメインを確認する入力画面です。COMMAND入力口へQUERY NODE NODE04 FORMAT=DETAILEDを指定し、DOM04のノード所属を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY NODE NODE04 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Node Name: NODE04 Policy Domain Name: DOM04 Locked: No
    ```

    画面・出力にあるNodeを読み、Domain NameとActivated Policy Setと対象DOM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の Policy が画面・出力に表示されること
    ② ステップ2 の Policy が画面・出力に表示されること
    ③ ステップ3 の Node が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_admin_ref_aix_en / SP_EE_admin_ref_windows_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en




## IBM Spectrum Protect 8.1 > リストア確認

### activity log 宛先照合 キュー状態 {#c14-i0526}
*分類: リストア確認*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の リストア確認 で扱う「activity log 宛先照合 キュー状態」は、サーバー操作とメッセージを追跡するログを宛先照合の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 040を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** activity log 宛先照合 キュー状態を同一分類のmanagement class 復元前確認 期限切れと比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認する。
    - B. コマンドまたは機能の用途はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - C. コマンドまたは機能の用途はサーバー操作とメッセージを追跡するログである。 ✅
    - D. コマンドまたは機能の用途はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。

    正解: **C** ／ 難易度: 中級

    **解説:** 宛先照合・activityでCの記述「サーバー操作とメッセージを追跡するログである」に対応する項目は宛先照合 キュー状態（activit・宛先照合）です。宛先・キューに関するリストア確認の仕様は「サーバー操作とメッセージを追跡するログ」で、確認対象はactivit・宛先照合です。復元前確認・managemeのA:は「ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認す」を述べ、対象は復元前確認 期限切れ（managem・復元前確）です。変更・NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・変更）です。照合・AssociatのD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associa・照合）です。「activity log」は「サーバー操作とメッセージを追跡するログ」を指す用語で、宛先照合 キュー状態（activit・宛先照合）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **activity log 宛先照合 キュー状態**

    - 検証目的: リストア確認のactivity log 宛先照合 キュー状態について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
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
    Destination Pool POOL040
    ```

    画面・出力には ANR1550I が含まれ、activity log 宛先照合 キュー状態の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL040 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL040
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



### activity log 容量監視 アーカイブ {#c14-i0527}
*分類: リストア確認*  ・  難易度: 上級

IBM Spectrum Protect 8.1 の リストア確認 で扱う「activity log 容量監視 アーカイブ」は、サーバー操作とメッセージを追跡するログを容量監視の観点で確認する技術項目です。QUERY NODE の登録情報とACTIVE policyset 080を同じ記録で見比べることで、default management class の欠落を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** activity log 容量監視 アーカイブを同一分類の管理クラス Management Class 停止前の確認 MC14と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はManagement Classで停止前の確認では管理クラスの クライアント詳細からDefaultManagである。
    - B. 構成を確認する際の意味はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - C. 構成を確認する際の意味はサーバー操作とメッセージを追跡するログを容量監視として確認する。 ✅
    - D. 構成を確認する際の意味はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。

    正解: **C** ／ 難易度: 上級

    **解説:** 容量監でリストアでCの記述「サーバー操作とメッセージを追跡するログを容量監視として確認する」に対応する項目は容量監視 アーカイブ（activit・リストア）です。容量監・アーカに関するリストア確認の仕様は「サーバー操作とメッセージを追跡するログを容量監視として確認する」で、確認対象はactivit・リストアです。Manag・停止確認のA:は「Management Classで停止前の確認では管理クラスの」を述べ、対象は停止前の確認 MC14（Managem・停止確認）です。サーバで監査のB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・監査）です。Actiを解析のD:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Action・解析）です。actiをリストアという用語は「サーバー操作とメッセージを追跡するログを容量監視とし」を指し、容量監視 アーカイブ（activit・リストア）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **activity log 容量監視 アーカイブ**

    - 検証目的: リストア確認のactivity log 容量監視 アーカイブについて、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
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
    Destination Pool POOL080
    ```

    画面・出力には ANR1550I が含まれ、activity log 容量監視 アーカイブの証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、default management class の欠落を切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL080 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL080
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



### archive copy group 保存期間確認 証明書検査 {#c14-i0528}
*分類: リストア確認*  ・  難易度: 中級

IBM Spectrum Protect 8.1 の リストア確認 で扱う「archive copy group 保存期間確認 証明書検査」は、アーカイブコピーの保存期間と宛先を定めるコピー規則を保存期間確認の観点で確認する技術項目です。QUERY ACTLOG の ANR メッセージとSTANDARD domain 024を同じ記録で見比べることで、期限切れ処理の見落としを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。

**出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands

??? question "確認問題（1問）"
    **問題.** archive copy group 保存期間確認 証明書検査を同一分類のポリシードメイン Policy Domain 通常状態の確認 DOM01と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はPolicy Domainで通常状態の確認ではポリシードメインのである。
    - B. 管理対象との関係を表す説明はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - C. 管理対象との関係を表す説明はStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。
    - D. 管理対象との関係を表す説明はアーカイブコピーの保存期間と宛先を定めるコピー規則である。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 保存期間確・archiveでDの記述「アーカイブコピーの保存期間と宛先を定めるコピー規則である」に対応する項目は保存期間確認 証明書検査（archive・保存期間）です。保存期・証明書に関するリストア確認の仕様は「アーカイブコピーの保存期間と宛先を定めるコピー規則」で、確認対象はarchive・保存期間確です。通常状態確・PolicyのA:は「Policy Domainで通常状態の確認ではポリシードメインの」を述べ、対象は通常状態の確認 DOM01（Policy・通常状態）です。監査・EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・監査）です。照合・StartのC:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・照合）です。「archive copy group」は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を指す用語で、保存期間確認 証明書検査（archive・保存期間）に該当します。

    **出典:** SP_EE_admin_ref_linux_en / SP_BA_client_unix_linux_en / IBM Spectrum Protect 8.1 policy domain and storage pool commands


??? note "検証手順（1件）"
    **archive copy group 保存期間確認 証明書検査**

    - 検証目的: リストア確認のarchive copy group 保存期間確認 証明書検査について、IBM Spectrum Protect 8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。
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
    Destination Pool POOL024
    ```

    画面・出力には ANR1550I が含まれ、archive copy group 保存期間確認 証明書検査の証跡を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の詳細確認画面です。表示名とメッセージ形式を照合し、期限切れ処理の見落としを切り分けます。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面
    COMMAND ===> QUERY STGPOOL POOL024 FORMAT=DETAILED
    → Enter を押す
    ```

    画面・出力:
    ```text
    Storage Pool Name POOL024
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


