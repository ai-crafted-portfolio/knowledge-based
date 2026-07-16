---
search:
  exclude: true
---

# IBM Spectrum Protect 8.1 — 詳細 (9/12)

[← IBM Spectrum Protect 8.1 の概要へ戻る](index.md)


## IBM Spectrum Protect 8.1 > ポリシー

### ポリシーと管理クラス DIRMC 0278 {#c14-i0423}
*分類: ポリシー*  ・  難易度: 中級

黒S照合0279ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票黒S照合0279です。黒S照合0279はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録黒S照合0279です。黒S照合0279ではノード登録値と取得時刻を採取票黒S照合0279へ残します。黒S照合0279ではDIRMC誤設定を避けるため補助資料も照合する判断黒S照合0279です。黒S照合0279の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録黒S照合0279です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス DIRMC 0278の技術的な意味を資料で確認するとき、サーバー日次運用 Expiration Status 0289との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は抑止でノード登録を証跡に残し・Expiration Statusのノード登録と取得時刻を記。
    - B. コマンドまたは機能の用途は照合でノード登録値を証跡に残し・DIRMCのノード登録値と取得時刻を記録し。 ✅
    - C. コマンドまたは機能の用途は停止確認で停止前の確認を証跡に残し・Incremental Backupで停止前の確認ではバック。
    - D. コマンドまたは機能の用途は診断で関連ノードを証跡に残し・Associationの関連ノードと取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 照合対象ディレクトでBの記述「DIRMCのノード登録値と取得時刻を記録し」に対応する項目はポリシーと管理クラス DIRMC（ディレクト・照合・ノード・ディレク）です。照合時のディレクトに関するポリシーの仕様は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」で、確認対象はディレク・照合・ノード・ディレクです。Expir・抑止のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・抑止・ノード・期限切れ）です。停止確認時のIncreのC:は「Incremental Backupで停止前の確認ではバックアップ運」を述べ、対象は停止前の確認 BKP14（Incre・停止確・停止前・除外規則）です。Assoを診断のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Assoc・診断・関連ノ・日次処理）です。ディレクを照合という用語は「DIRMCのノード登録値と取得時刻を記録し」を指し、ポリシーと管理クラス DIRMC（ディレクト・照合・ノード・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス DIRMC 0278**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス DIRMC 0278について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DIRMC と ノード登録値
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0278A
    ```

    画面・出力には SP81DD0278A が表示され、ポリシーと管理クラス DIRMC 0278 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0278B
    ```

    画面・出力には SP81DD0278B が表示され、ポリシーと管理クラス DIRMC 0278 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR03
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0278C
    ```

    画面・出力には SP81DD0278C が表示され、ポリシーと管理クラス DIRMC 0278 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0278A が画面・出力に表示されること
    ② ステップ2 の SP81DD0278B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0278C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス DIRMC 0293 {#c14-i0424}
*分類: ポリシー*  ・  難易度: 中級

灰N抑止0294ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票灰N抑止0294です。灰N抑止0294はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録灰N抑止0294です。灰N抑止0294ではノード登録値と取得時刻を採取票灰N抑止0294へ残します。灰N抑止0294では管理クラス未割当を避けるため補助資料も照合する判断灰N抑止0294です。灰N抑止0294の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録灰N抑止0294です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス DIRMC 0293について構成や状態を確認します。クライアントスケジュール Schedule Name 0354ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は抑止でノード登録値を証跡に残し・DIRMCのノード登録値と取得時刻を記録し。 ✅
    - B. 一次資料が示す主目的は解除でスケジュールを証跡に残し・Schedule Nameのスケジュール定義と取得時刻を記録。
    - C. 一次資料が示す主目的は停止確認で停止前の確認を証跡に残し・Storage Poolで停止前の確認では複製・保護の。
    - D. 一次資料が示す主目的は収集でイベント結果を証跡に残し・Event Statusのイベント結果と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 抑止対象ディレクトでAの記述「DIRMCのノード登録値と取得時刻を記録し」に対応する項目はポリシーと管理クラス DIRMC（ディレクト・抑止・ノード・管理クラ）です。抑止時のディレクトに関するポリシーの仕様は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」で、確認対象はディレク・抑止・ノード・管理クラです。解除対象SchedのB:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Sched・解除・スケジ・開始時刻）です。停止確認時のStoraのC:は「Storage Poolで停止前の確認では複製・保護の」を述べ、対象は停止前の確認 REPL14（Stora・停止確・停止前・PROT）です。Evenを収集のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・収集・イベン・日次処理）です。ディレクを抑止という用語は「DIRMCのノード登録値と取得時刻を記録し」を指し、ポリシーと管理クラス DIRMC（ディレクト・抑止・ノード・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス DIRMC 0293**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス DIRMC 0293について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DIRMC と ノード登録値
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0293A
    ```

    画面・出力には SP81DD0293A が表示され、ポリシーと管理クラス DIRMC 0293 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0293B
    ```

    画面・出力には SP81DD0293B が表示され、ポリシーと管理クラス DIRMC 0293 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR03
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0293C
    ```

    画面・出力には SP81DD0293C が表示され、ポリシーと管理クラス DIRMC 0293 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0293A が画面・出力に表示されること
    ② ステップ2 の SP81DD0293B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0293C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス DIRMC 0308 {#c14-i0425}
*分類: ポリシー*  ・  難易度: 中級

黄I解析0309ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票黄I解析0309です。黄I解析0309はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録黄I解析0309です。黄I解析0309ではノード登録値と取得時刻を採取票黄I解析0309へ残します。黄I解析0309では登録ドメインの取り違えを避けるため補助資料も照合する判断黄I解析0309です。黄I解析0309の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録黄I解析0309です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス DIRMC 0308の役割を調べています。サーバー日次運用 Storage Pool 0310の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はデータベースバックアップ時刻の記を避けるため・確認操作で状態欄を整理するしてストレージプを照合する。
    - B. 障害切り分けに用いる役割は登録ドメインの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてノード登録値を照合する。 ✅
    - C. 障害切り分けに用いる役割はPROTECT STGPOOLとを避けるため・性能影響確認で性能影響の確を確認するして性能影響の確を照合する。
    - D. 障害切り分けに用いる役割は日次処理順序の誤読を避けるため・照合操作で確認欄を採取するして開始時刻を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 解析対象ディレクトでBの記述「DIRMCのノード登録値と取得時刻を記録し」に対応する項目はポリシーと管理クラス DIRMC（ディレクト・解析・ノード・登録ドメ）です。解析時のディレクトに関するポリシーの仕様は「DIRMCのノード登録値と取得時刻を記録し」で、確認対象はディレク・解析・ノード・登録ドメです。Stora・解析のA:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・解析・ストレ・データベ）です。性能影響時のStoraのC:は「Storage Poolで性能影響の確認では複製・保護の」を述べ、対象は性能影響の確認 REPL11（Stora・性能影・性能影・PROT）です。Actiを保守のD:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Actio・保守・開始時・日次処理）です。ディレクを解析という用語は「DIRMCのノード登録値と取得時刻を記録し」を指し、ポリシーと管理クラス DIRMC（ディレクト・解析・ノード・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス DIRMC 0308**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス DIRMC 0308について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DIRMC と ノード登録値
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0308A
    ```

    画面・出力には SP81DD0308A が表示され、ポリシーと管理クラス DIRMC 0308 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0308B
    ```

    画面・出力には SP81DD0308B が表示され、ポリシーと管理クラス DIRMC 0308 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR03
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0308C
    ```

    画面・出力には SP81DD0308C が表示され、ポリシーと管理クラス DIRMC 0308 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0308A が画面・出力に表示されること
    ② ステップ2 の SP81DD0308B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0308C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス DIRMC 0323 {#c14-i0426}
*分類: ポリシー*  ・  難易度: 中級

藍D計画0324ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票藍D計画0324です。藍D計画0324はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録藍D計画0324です。藍D計画0324ではノード登録値と取得時刻を採取票藍D計画0324へ残します。藍D計画0324ではコピーグループ未定義を避けるため補助資料も照合する判断藍D計画0324です。藍D計画0324の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録藍D計画0324です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシーと管理クラス DIRMC 0323」を「node 状態確認 構成配布」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は状態確認で構成配布を証跡に残し・サーバーへ登録されたクライアントを表す管理単位。
    - B. 仕様上の役割は変更確認で変更前の確認を証跡に残し・Client Restoreで変更前の確認ではリストア確認の。
    - C. 仕様上の役割は診断でコピーグルーを証跡に残し・Copy Groupのコピーグループと取得時刻を記録し。
    - D. 仕様上の役割は計画でノード登録値を証跡に残し・DIRMCのノード登録値と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 計画対象ディレクトでDの記述「DIRMCのノード登録値と取得時刻を記録し」に対応する項目はポリシーと管理クラス DIRMC（ディレクト・計画・ノード・コピーグ）です。計画時のディレクトに関するポリシーの仕様は「DIRMCのノード登録値と取得時刻を記録し」で、確認対象はディレク・計画・ノード・コピーグです。node・状態確認のA:は「サーバーへ登録されたクライアントを表す管理単位」を述べ、対象は状態確認 構成配布（node・状態確・構成配・構成配布）です。変更確認対象ClienのB:は「Client Restoreで変更前の確認ではリストア確認の」を述べ、対象は変更前の確認 RST02（Clien・変更確・変更前・置換条件）です。診断時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・診断・コピー・コピーグ）です。ディレクを計画という用語は「DIRMCのノード登録値と取得時刻を記録し」を指し、ポリシーと管理クラス DIRMC（ディレクト・計画・ノード・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス DIRMC 0323**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス DIRMC 0323について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DIRMC と ノード登録値
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0323A
    ```

    画面・出力には SP81DD0323A が表示され、ポリシーと管理クラス DIRMC 0323 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0323B
    ```

    画面・出力には SP81DD0323B が表示され、ポリシーと管理クラス DIRMC 0323 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR03
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0323C
    ```

    画面・出力には SP81DD0323C が表示され、ポリシーと管理クラス DIRMC 0323 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0323A が画面・出力に表示されること
    ② ステップ2 の SP81DD0323B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0323C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス DIRMC 0338 {#c14-i0427}
*分類: ポリシー*  ・  難易度: 中級

黒S計画0339ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票黒S計画0339です。黒S計画0339はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録黒S計画0339です。黒S計画0339ではノード登録値と取得時刻を採取票黒S計画0339へ残します。黒S計画0339ではDIRMC誤設定を避けるため補助資料も照合する判断黒S計画0339です。黒S計画0339の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録黒S計画0339です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス DIRMC 0338を同一分類のarchive copy group 状態確認 集約装置と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は集約装置の誤読を避けるため・状態確認で集約装置を確認するして集約装置を照合する。
    - B. コマンドまたは機能の用途はディレクトリー管理クラス指定誤設を避けるため・点検操作で判定欄を記録するしてノード登録値を照合する。 ✅
    - C. コマンドまたは機能の用途は登録ドメインの取り違えを避けるため・調査操作で保守欄を引き継ぎするしてディレクトリを照合する。ポリシーと管理クラス Policy Set 0032固有の属性も確認対象に含める。
    - D. コマンドまたは機能の用途は期限切れ処理の未実行を避けるため・記録操作で証跡欄を照合するしてストレージプを照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 計画対象ディレクトでBの記述「DIRMCのノード登録値と取得時刻を記録し」に対応する項目はポリシーと管理クラス DIRMC（ディレクト・計画・ノード・ディレク）です。計画時のディレクトに関するポリシーの仕様は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」で、確認対象はディレク・計画・ノード・ディレクです。archi・状態確認のA:は「アーカイブコピーの保存期間と宛先を定めるコピー規則」を述べ、対象は状態確認 集約装置（archi・状態確・集約装・集約装置）です。棚卸時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Polic・棚卸・ディレ・登録ドメ）です。Storを保守のD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・保守・ストレ・期限切れ）です。ディレクを計画という用語は「DIRMCのノード登録値と取得時刻を記録し」を指し、ポリシーと管理クラス DIRMC（ディレクト・計画・ノード・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス DIRMC 0338**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス DIRMC 0338について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DIRMC と ノード登録値
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0338A
    ```

    画面・出力には SP81DD0338A が表示され、ポリシーと管理クラス DIRMC 0338 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0338B
    ```

    画面・出力には SP81DD0338B が表示され、ポリシーと管理クラス DIRMC 0338 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR03
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0338C
    ```

    画面・出力には SP81DD0338C が表示され、ポリシーと管理クラス DIRMC 0338 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0338A が画面・出力に表示されること
    ② ステップ2 の SP81DD0338B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0338C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス DIRMC 0353 {#c14-i0428}
*分類: ポリシー*  ・  難易度: 上級

灰N解除0354ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票灰N解除0354です。灰N解除0354はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録灰N解除0354です。灰N解除0354ではノード登録値と取得時刻を採取票灰N解除0354へ残します。灰N解除0354では管理クラス未割当を避けるため補助資料も照合する判断灰N解除0354です。灰N解除0354の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録灰N解除0354です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス DIRMC 0353の設定や表示を読む前に役割を確認します。activity log コマンド証跡 統計値ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はサーバー操作とメッセージを追跡するログをコマンド証跡として確認する。バックアップで統計値を確認するときは統計値の誤読を防ぐ。
    - B. 一次資料が示す主目的はDBで引継ぎ記録ではサーバーの 履歴照会からBACKUPFULLを読み・サーバーDBに使うである。サーバーDBで引継ぎ記録でを確認するときはデータベースバックアップ媒体を防ぐ。
    - C. 一次資料が示す主目的はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。復旧操作で点検欄を確認するときは管理クラス未割当を防ぐ。 ✅
    - D. 一次資料が示す主目的はServer NameのDBバックアップ履歴と取得時刻を記録し・プール容量不足の見落としを防ぐである。採取操作で照合欄を点検するときはプール容量不足の見落としを防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 解除対象ディレクトでCの記述「DIRMCのノード登録値と取得時刻を記録し」に対応する項目はポリシーと管理クラス DIRMC（ディレクト・解除・ノード・管理クラ）です。解除時のディレクトに関するポリシーの仕様は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」で、確認対象はディレク・解除・ノード・管理クラです。activ・バックアッのA:は「サーバー操作とメッセージを追跡するログをコマンド証跡として確認する」を述べ、対象はコマンド証跡 統計値（activ・バック・統計値・統計値の）です。サーバー対象データベーのB:は「DBで引継ぎ記録ではサーバーの 履歴照会からBACKUPFULLを読」を述べ、対象は引継ぎ記録 DBBK09（データベー・サーバ・引継ぎ・データベ）です。Servを登録のD:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Serve・登録・データ・プール容）です。ディレクを解除という用語は「DIRMCのノード登録値と取得時刻を記録し」を指し、ポリシーと管理クラス DIRMC（ディレクト・解除・ノード・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス DIRMC 0353**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス DIRMC 0353について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=DIRMC と ノード登録値
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> QUERY MGMTCLASS -DETAIL
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0353A
    ```

    画面・出力には SP81DD0353A が表示され、ポリシーと管理クラス DIRMC 0353 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0353B
    ```

    画面・出力には SP81DD0353B が表示され、ポリシーと管理クラス DIRMC 0353 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。DIRMC を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR03
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0353C
    ```

    画面・出力には SP81DD0353C が表示され、ポリシーと管理クラス DIRMC 0353 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0353A が画面・出力に表示されること
    ② ステップ2 の SP81DD0353B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0353C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0014 {#c14-i0429}
*分類: ポリシー*  ・  難易度: 初級

翠O巡回0015ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票翠O巡回0015です。翠O巡回0015はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録翠O巡回0015です。翠O巡回0015ではドメイン割当と取得時刻を採取票翠O巡回0015へ残します。翠O巡回0015ではDIRMC誤設定を避けるため補助資料も照合する判断翠O巡回0015です。翠O巡回0015の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録翠O巡回0015です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0014の技術的な意味を資料で確認するとき、サーバー日次運用 Database Backup 0082との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - B. コマンドまたは機能の用途はSchedule Nameのスケジュール定義と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - C. コマンドまたは機能の用途はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - D. コマンドまたは機能の用途はサーバーへ登録されたクライアントを表す管理単位である。

    正解: **C** ／ 難易度: 初級

    **解説:** 巡回対象ManagでCの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manage・巡回・ドメイン）です。ポリシに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はManag・巡回・ドメインです。Datab・変更のA:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databa・変更・期限切れ）です。照合対象SchedのB:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Schedu・照合・スケジュ）です。nodeを宛先照合のD:は「サーバーへ登録されたクライアントを表す管理単位」を述べ、対象は宛先照合 データソース（node・宛先照・データソ）です。Manaを巡回という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manage・巡回・ドメイン）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0014**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0014について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0014A
    ```

    画面・出力には SP81DD0014A が表示され、ポリシーと管理クラス Management Class 0014 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0014B
    ```

    画面・出力には SP81DD0014B が表示され、ポリシーと管理クラス Management Class 0014 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0014C
    ```

    画面・出力には SP81DD0014C が表示され、ポリシーと管理クラス Management Class 0014 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0014A が画面・出力に表示されること
    ② ステップ2 の SP81DD0014B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0014C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0029 {#c14-i0430}
*分類: ポリシー*  ・  難易度: 中級

朱J棚卸0030ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票朱J棚卸0030です。朱J棚卸0030はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録朱J棚卸0030です。朱J棚卸0030ではドメイン割当と取得時刻を採取票朱J棚卸0030へ残します。朱J棚卸0030では管理クラス未割当を避けるため補助資料も照合する判断朱J棚卸0030です。朱J棚卸0030の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録朱J棚卸0030です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0029について構成や状態を確認します。サーバー日次運用 Node Name 0118ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はNode Nameの運用状態と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - B. 一次資料が示す主目的はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。 ✅
    - C. 一次資料が示す主目的はDIRMCのノード登録値と取得時刻を記録し・コピーグループ未定義を防ぐである。
    - D. 一次資料が示す主目的はPolicy Domainで再始動後の確認ではポリシードメインの ノード所属からNodeNameを読みである。

    正解: **B** ／ 難易度: 中級

    **解説:** 棚卸対象ManagでBの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manage・棚卸・ドメイン）です。棚卸時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はManag・棚卸・ドメインです。Node・移行のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・移行・運用状態）です。照合時のDIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・照合・ノード登）です。Poliを再始動確認のD:は「Policy Domainで再始動後の確認ではポリシードメインの」を述べ、対象は再始動後の確認 DOM15（Policy・再始動・再始動後）です。Manaを棚卸という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manage・棚卸・ドメイン）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0029**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0029について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0029A
    ```

    画面・出力には SP81DD0029A が表示され、ポリシーと管理クラス Management Class 0029 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0029B
    ```

    画面・出力には SP81DD0029B が表示され、ポリシーと管理クラス Management Class 0029 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0029C
    ```

    画面・出力には SP81DD0029C が表示され、ポリシーと管理クラス Management Class 0029 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0029A が画面・出力に表示されること
    ② ステップ2 の SP81DD0029B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0029C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0044 {#c14-i0431}
*分類: ポリシー*  ・  難易度: 中級

紅E復旧0045ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紅E復旧0045です。紅E復旧0045はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録紅E復旧0045です。紅E復旧0045ではドメイン割当と取得時刻を採取票紅E復旧0045へ残します。紅E復旧0045では登録ドメインの取り違えを避けるため補助資料も照合する判断紅E復旧0045です。紅E復旧0045の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録紅E復旧0045です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0044の役割を調べています。クライアントスケジュール Association 0105の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。クライアントスケジュール Association 0105固有の属性も確認対象に含める。
    - B. 障害切り分けに用いる役割はDIRMCのノード登録値と取得時刻を記録し・コピーグループ未定義を防ぐである。
    - C. 障害切り分けに用いる役割はサーバー操作とメッセージを追跡するログを容量監視として確認する。
    - D. 障害切り分けに用いる役割はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 復旧対象ManagでDの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manage・復旧・ドメイン）です。復旧時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はManag・復旧・ドメインです。Assoc・移行のA:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Associ・移行・関連ノー）です。照合対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・照合・ノード登）です。リストア時のactivのC:は「サーバー操作とメッセージを追跡するログを容量監視として確認する」を述べ、対象は容量監視 アーカイブ（activi・リスト・アーカイ）です。Manaを復旧という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manage・復旧・ドメイン）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0044**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0044について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0044A
    ```

    画面・出力には SP81DD0044A が表示され、ポリシーと管理クラス Management Class 0044 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0044B
    ```

    画面・出力には SP81DD0044B が表示され、ポリシーと管理クラス Management Class 0044 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0044C
    ```

    画面・出力には SP81DD0044C が表示され、ポリシーと管理クラス Management Class 0044 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0044A が画面・出力に表示されること
    ② ステップ2 の SP81DD0044B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0044C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0059 {#c14-i0432}
*分類: ポリシー*  ・  難易度: 中級

空T復旧0060ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票空T復旧0060です。空T復旧0060はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録空T復旧0060です。空T復旧0060ではドメイン割当と取得時刻を採取票空T復旧0060へ残します。空T復旧0060ではコピーグループ未定義を避けるため補助資料も照合する判断空T復旧0060です。空T復旧0060の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録空T復旧0060です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシーと管理クラス Management Class 0059」を「クライアントスケジュール Start Time 0063」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はStart Timeの失敗理由と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - B. 仕様上の役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - C. 仕様上の役割はManagement Classで障害切り分けでは管理クラスの 管理クラス照会からManagementClaである。
    - D. 仕様上の役割はManagement Classのドメイン割当と取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 復旧対象ManagでDの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manage・復旧・ドメイン）です。復旧時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はManag・復旧・ドメインです。Start・監査のA:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・監査・失敗理由）です。解除対象PolicのB:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・解除・管理クラ）です。管理クラ時のManagのC:は「Management Classで障害切り分けでは管理クラスの」を述べ、対象は障害切り分け MC04（Manage・管理ク・障害切り）です。Manaを復旧という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manage・復旧・ドメイン）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0059**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0059について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0059A
    ```

    画面・出力には SP81DD0059A が表示され、ポリシーと管理クラス Management Class 0059 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0059B
    ```

    画面・出力には SP81DD0059B が表示され、ポリシーと管理クラス Management Class 0059 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0059C
    ```

    画面・出力には SP81DD0059C が表示され、ポリシーと管理クラス Management Class 0059 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0059A が画面・出力に表示されること
    ② ステップ2 の SP81DD0059B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0059C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0074 {#c14-i0433}
*分類: ポリシー*  ・  難易度: 中級

翠O監査0075ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票翠O監査0075です。翠O監査0075はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録翠O監査0075です。翠O監査0075ではドメイン割当と取得時刻を採取票翠O監査0075へ残します。翠O監査0075ではDIRMC誤設定を避けるため補助資料も照合する判断翠O監査0075です。翠O監査0075の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録翠O監査0075です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0074を同一分類のポリシーと管理クラス Policy Domain 0125と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。
    - B. コマンドまたは機能の用途はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - C. コマンドまたは機能の用途はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - D. コマンドまたは機能の用途はClient Nodeで依存関係の確認ではノード管理の ノード照会からLastAccessを読みである。

    正解: **C** ／ 難易度: 中級

    **解説:** 監査対象ManagでCの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manage・監査・ドメイン）です。監査時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はManag・監査・ドメインです。Polic・診断のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Policy・診断・管理クラ）です。解除対象NodeのB:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・解除・運用状態）です。Clieを依存関係確のD:は「Client Nodeで依存関係の確認ではノード管理の」を述べ、対象は依存関係の確認 NODE13（Client・依存関・依存関係）です。Manaを監査という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manage・監査・ドメイン）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0074**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0074について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0074A
    ```

    画面・出力には SP81DD0074A が表示され、ポリシーと管理クラス Management Class 0074 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0074B
    ```

    画面・出力には SP81DD0074B が表示され、ポリシーと管理クラス Management Class 0074 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0074C
    ```

    画面・出力には SP81DD0074C が表示され、ポリシーと管理クラス Management Class 0074 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0074A が画面・出力に表示されること
    ② ステップ2 の SP81DD0074B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0074C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0089 {#c14-i0434}
*分類: ポリシー*  ・  難易度: 中級

朱J変更0090ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票朱J変更0090です。朱J変更0090はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録朱J変更0090です。朱J変更0090ではドメイン割当と取得時刻を採取票朱J変更0090へ残します。朱J変更0090では管理クラス未割当を避けるため補助資料も照合する判断朱J変更0090です。朱J変更0090の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録朱J変更0090です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0089の設定や表示を読む前に役割を確認します。クライアントスケジュール Event Status 0117ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。 ✅
    - B. 一次資料が示す主目的はEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。クライアントスケジュール Event Status 0117固有の属性も確認対象に含める。
    - C. 一次資料が示す主目的はファイルのバックアップ先や保存期間を決めるポリシー要素を期限切れ確認する。
    - D. 一次資料が示す主目的はIncremental Backupで代替経路の確認ではバックアップ運用のである。

    正解: **A** ／ 難易度: 中級

    **解説:** 変更対象ManagでAの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manage・変更・ドメイン）です。変更時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はManag・変更・ドメインです。移行対象EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・移行・イベント）です。期限切れ時のmanagのC:は「ファイルのバックアップ先や保存期間を決めるポリシー要素を期限切れ確認」を述べ、対象は期限切れ確認 宛先定義（manage・期限切・宛先定義）です。Incrを代替経路確のD:は「Incremental Backupで代替経路の確認ではバックアップ」を述べ、対象は代替経路の確認 BKP10（Increm・代替経・代替経路）です。Manaを変更という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manage・変更・ドメイン）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0089**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0089について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0089A
    ```

    画面・出力には SP81DD0089A が表示され、ポリシーと管理クラス Management Class 0089 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0089B
    ```

    画面・出力には SP81DD0089B が表示され、ポリシーと管理クラス Management Class 0089 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0089C
    ```

    画面・出力には SP81DD0089C が表示され、ポリシーと管理クラス Management Class 0089 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0089A が画面・出力に表示されること
    ② ステップ2 の SP81DD0089B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0089C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0104 {#c14-i0435}
*分類: ポリシー*  ・  難易度: 上級

紅E移行0105ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紅E移行0105です。紅E移行0105はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録紅E移行0105です。紅E移行0105ではドメイン割当と取得時刻を採取票紅E移行0105へ残します。紅E移行0105では登録ドメインの取り違えを避けるため補助資料も照合する判断紅E移行0105です。紅E移行0105の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録紅E移行0105です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0104に関する障害切り分けの前提を確認しています。ポリシーと管理クラス Copy Group 0146の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。
    - B. 障害切り分けに用いる役割はストレージプール内の空き領域を回収する処理である。
    - C. 障害切り分けに用いる役割はArchive Operationで権限境界の確認ではアーカイブ運用のである。アーカイブ運用 Archive Operation 権限境界の確認固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 移行対象ManagでDの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manage・移行・ドメイン）です。移行時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はManag・移行・ドメインです。Copy・保守のA:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・保守・コピーグ）です。宛先照合対象reclaのB:は「ストレージプール内の空き領域を回収する処理」を述べ、対象は宛先照合 集約結果（reclam・宛先照・集約結果）です。権限境界時のArchiのC:は「Archive Operationで権限境界の確認ではアーカイブ運用」を述べ、対象は権限境界の確認 ARC12（Archiv・権限境・確認では）です。Manaを移行という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manage・移行・ドメイン）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0104**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0104について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0104A
    ```

    画面・出力には SP81DD0104A が表示され、ポリシーと管理クラス Management Class 0104 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0104B
    ```

    画面・出力には SP81DD0104B が表示され、ポリシーと管理クラス Management Class 0104 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0104C
    ```

    画面・出力には SP81DD0104C が表示され、ポリシーと管理クラス Management Class 0104 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0104A が画面・出力に表示されること
    ② ステップ2 の SP81DD0104B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0104C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0119 {#c14-i0436}
*分類: ポリシー*  ・  難易度: 上級

空T移行0120ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票空T移行0120です。空T移行0120はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録空T移行0120です。空T移行0120ではドメイン割当と取得時刻を採取票空T移行0120へ残します。空T移行0120ではコピーグループ未定義を避けるため補助資料も照合する判断空T移行0120です。空T移行0120の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録空T移行0120です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0119を保守記録に説明する必要があります。ポリシーと管理クラス Policy Set 0197と取り違えない説明はどれですか。

    - A. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・管理クラス未割当を防ぐである。
    - B. 仕様上の役割はManagement Classのドメイン割当と取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅
    - C. 仕様上の役割はファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認する。
    - D. 仕様上の役割はIncremental Backupで障害切り分けではバックアップ運用の 増分実行からobjectsを読みである。

    正解: **B** ／ 難易度: 上級

    **解説:** 移行対象ManagでBの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manage・移行・ドメイン）です。移行時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はManag・移行・ドメインです。Polic・収集のA:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・収集・ディレク）です。復元前確時のmanagのC:は「ファイルのバックアップ先や保存期間を決めるポリシー要素を復元前確認す」を述べ、対象は復元前確認 期限切れ（manage・復元前・期限切れ）です。IncrをバックアッのD:は「Incremental Backupで障害切り分けではバックアップ運」を述べ、対象は障害切り分け BKP04（Increm・バック・障害切り）です。Manaを移行という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manage・移行・ドメイン）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0119**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0119について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0119A
    ```

    画面・出力には SP81DD0119A が表示され、ポリシーと管理クラス Management Class 0119 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0119B
    ```

    画面・出力には SP81DD0119B が表示され、ポリシーと管理クラス Management Class 0119 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0119C
    ```

    画面・出力には SP81DD0119C が表示され、ポリシーと管理クラス Management Class 0119 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0119A が画面・出力に表示されること
    ② ステップ2 の SP81DD0119B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0119C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0134 {#c14-i0437}
*分類: ポリシー*  ・  難易度: 初級

翠O診断0135ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票翠O診断0135です。翠O診断0135はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録翠O診断0135です。翠O診断0135ではドメイン割当と取得時刻を採取票翠O診断0135へ残します。翠O診断0135ではDIRMC誤設定を避けるため補助資料も照合する判断翠O診断0135です。翠O診断0135の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録翠O診断0135です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0134の技術的な意味を資料で確認するとき、ポリシーと管理クラス DIRMC 0158との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - B. コマンドまたは機能の用途はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - C. コマンドまたは機能の用途はサーバーへ登録されたクライアントを表す管理単位を復元前確認する。
    - D. コマンドまたは機能の用途はStorage Poolでログとの照合では複製・保護の プール保護からANR0984Iを読みである。

    正解: **A** ／ 難易度: 初級

    **解説:** 診断対象ManagでAの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・診断・ドメイ・ディレク）です。診断時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・診断・ドメイ・ディレクです。保守対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・保守・ノード・ディレク）です。復元前確時のnodeのC:は「サーバーへ登録されたクライアントを表す管理単位を復元前確認する」を述べ、対象は復元前確認 応答行（node・復元前・応答行・応答行の）です。Storをログとの照のD:は「Storage Poolでログとの照合では複製・保護の」を述べ、対象はログとの照合 REPL07（Stora・ログと・ログと・PROT）です。Manaを診断という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・診断・ドメイ・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0134**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0134について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0134A
    ```

    画面・出力には SP81DD0134A が表示され、ポリシーと管理クラス Management Class 0134 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0134B
    ```

    画面・出力には SP81DD0134B が表示され、ポリシーと管理クラス Management Class 0134 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0134C
    ```

    画面・出力には SP81DD0134C が表示され、ポリシーと管理クラス Management Class 0134 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0134A が画面・出力に表示されること
    ② ステップ2 の SP81DD0134B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0134C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0149 {#c14-i0438}
*分類: ポリシー*  ・  難易度: 中級

朱J保守0150ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票朱J保守0150です。朱J保守0150はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録朱J保守0150です。朱J保守0150ではドメイン割当と取得時刻を採取票朱J保守0150へ残します。朱J保守0150では管理クラス未割当を避けるため補助資料も照合する判断朱J保守0150です。朱J保守0150の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録朱J保守0150です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0149について構成や状態を確認します。ポリシーと管理クラス Policy Domain 0245ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。
    - B. 一次資料が示す主目的はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。 ✅
    - C. 一次資料が示す主目的はサーバーへ登録されたクライアントを表す管理単位を復元前確認する。node 復元前確認 応答行固有の属性も確認対象に含める。
    - D. 一次資料が示す主目的はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。

    正解: **B** ／ 難易度: 中級

    **解説:** 保守対象ManagでBの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・保守・ドメイ・管理クラ）です。保守時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・保守・ドメイ・管理クラです。Polic・保護のA:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・保護・管理ク・管理クラ）です。復元前確時のnodeのC:は「サーバーへ登録されたクライアントを表す管理単位を復元前確認する」を述べ、対象は復元前確認 応答行（node・復元前・応答行・応答行の）です。Poliを巡回のD:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Polic・巡回・ディレ・ディレク）です。Manaを保守という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・保守・ドメイ・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0149**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0149について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0149A
    ```

    画面・出力には SP81DD0149A が表示され、ポリシーと管理クラス Management Class 0149 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0149B
    ```

    画面・出力には SP81DD0149B が表示され、ポリシーと管理クラス Management Class 0149 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0149C
    ```

    画面・出力には SP81DD0149C が表示され、ポリシーと管理クラス Management Class 0149 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0149A が画面・出力に表示されること
    ② ステップ2 の SP81DD0149B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0149C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0164 {#c14-i0439}
*分類: ポリシー*  ・  難易度: 中級

紅E切替0165ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紅E切替0165です。紅E切替0165はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録紅E切替0165です。紅E切替0165ではドメイン割当と取得時刻を採取票紅E切替0165へ残します。紅E切替0165では登録ドメインの取り違えを避けるため補助資料も照合する判断紅E切替0165です。紅E切替0165の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録紅E切替0165です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0164の役割を調べています。ポリシーと管理クラス Copy Group 0236の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はCopy Groupのコピーグループと取得時刻を記録し・登録ドメインの取り違えを防ぐである。
    - B. 障害切り分けに用いる役割はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅
    - C. 障害切り分けに用いる役割はクライアントに適用するバックアップとアーカイブの規則を束ねる単位をノード割当確認する。policy domain ノード割当確認 保持期間固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割はStart Timeの失敗理由と取得時刻を記録し・開始時刻誤設定を防ぐである。

    正解: **B** ／ 難易度: 中級

    **解説:** 切替対象ManagでBの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・切替・ドメイ・登録ドメ）です。切替時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・切替・ドメイ・登録ドメです。Copy・確認のA:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・確認・コピー・登録ドメ）です。ノード割時のpolicのC:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をノ」を述べ、対象はノード割当確認 保持期間（polic・ノード・保持期・保持期間）です。Starを巡回のD:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・巡回・失敗理・開始時刻）です。Manaを切替という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・切替・ドメイ・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0164**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0164について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0164A
    ```

    画面・出力には SP81DD0164A が表示され、ポリシーと管理クラス Management Class 0164 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0164B
    ```

    画面・出力には SP81DD0164B が表示され、ポリシーと管理クラス Management Class 0164 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0164C
    ```

    画面・出力には SP81DD0164C が表示され、ポリシーと管理クラス Management Class 0164 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0164A が画面・出力に表示されること
    ② ステップ2 の SP81DD0164B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0164C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0179 {#c14-i0440}
*分類: ポリシー*  ・  難易度: 中級

空T切替0180ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票空T切替0180です。空T切替0180はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録空T切替0180です。空T切替0180ではドメイン割当と取得時刻を採取票空T切替0180へ残します。空T切替0180ではコピーグループ未定義を避けるため補助資料も照合する判断空T切替0180です。空T切替0180の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録空T切替0180です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシーと管理クラス Management Class 0179」を「サーバー日次運用 Expiration Status 0259」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はExpiration Statusのノード登録と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - B. 仕様上の役割はファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視として確認する。
    - C. 仕様上の役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。
    - D. 仕様上の役割はManagement Classのドメイン割当と取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 切替対象ManagでDの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・切替・ドメイ・コピーグ）です。切替時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・切替・ドメイ・コピーグです。Expir・保護のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・保護・ノード・プール容）です。リストア対象managのB:は「ファイルのバックアップ先や保存期間を決めるポリシー要素を容量監視とし」を述べ、対象は容量監視 分散定義（manag・リスト・分散定・分散定義）です。監査時のPolicのC:は「Policy Domainの管理クラス詳細と取得時刻を記録し」を述べ、対象はPolicy Domain（Polic・監査・管理ク・管理クラ）です。Manaを切替という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・切替・ドメイ・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0179**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0179について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0179A
    ```

    画面・出力には SP81DD0179A が表示され、ポリシーと管理クラス Management Class 0179 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0179B
    ```

    画面・出力には SP81DD0179B が表示され、ポリシーと管理クラス Management Class 0179 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0179C
    ```

    画面・出力には SP81DD0179C が表示され、ポリシーと管理クラス Management Class 0179 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0179A が画面・出力に表示されること
    ② ステップ2 の SP81DD0179B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0179C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0194 {#c14-i0441}
*分類: ポリシー*  ・  難易度: 中級

翠O収集0195ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票翠O収集0195です。翠O収集0195はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録翠O収集0195です。翠O収集0195ではドメイン割当と取得時刻を採取票翠O収集0195へ残します。翠O収集0195ではDIRMC誤設定を避けるため補助資料も照合する判断翠O収集0195です。翠O収集0195の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録翠O収集0195です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0194を同一分類のポリシーと管理クラス DIRMC 0233と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - B. コマンドまたは機能の用途はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。
    - C. コマンドまたは機能の用途はバックアップ版数と保存先を定めるコピー規則をノード割当確認する。
    - D. コマンドまたは機能の用途はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。

    正解: **A** ／ 難易度: 中級

    **解説:** 収集対象ManagでAの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・収集・ドメイ・ディレク）です。収集時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・収集・ドメイ・ディレクです。確認対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・確認・ノード・管理クラ）です。ノード割時のbackuのC:は「バックアップ版数と保存先を定めるコピー規則をノード割当確認する」を述べ、対象はノード割当確認 再同期判断（backu・ノード・再同期・再同期判）です。Dataを監査のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・監査・期限切・プール容）です。Manaを収集という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・収集・ドメイ・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0194**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0194について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0194A
    ```

    画面・出力には SP81DD0194A が表示され、ポリシーと管理クラス Management Class 0194 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0194B
    ```

    画面・出力には SP81DD0194B が表示され、ポリシーと管理クラス Management Class 0194 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0194C
    ```

    画面・出力には SP81DD0194C が表示され、ポリシーと管理クラス Management Class 0194 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0194A が画面・出力に表示されること
    ② ステップ2 の SP81DD0194B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0194C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0209 {#c14-i0442}
*分類: ポリシー*  ・  難易度: 中級

朱J登録0210ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票朱J登録0210です。朱J登録0210はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録朱J登録0210です。朱J登録0210ではドメイン割当と取得時刻を採取票朱J登録0210へ残します。朱J登録0210では管理クラス未割当を避けるため補助資料も照合する判断朱J登録0210です。朱J登録0210の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録朱J登録0210です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0209の設定や表示を読む前に役割を確認します。クライアントスケジュール Start Time 0228ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - B. 一次資料が示す主目的はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。 ✅
    - C. 一次資料が示す主目的はBackup andで性能影響の確認ではコピーグループの アーカイブグループからRetainVersionをである。
    - D. 一次資料が示す主目的はAssociationの関連ノードと取得時刻を記録し・開始時刻誤設定を防ぐである。

    正解: **B** ／ 難易度: 中級

    **解説:** 登録対象ManagでBの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・登録・ドメイ・管理クラ）です。登録時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・登録・ドメイ・管理クラです。Start・確認のA:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・確認・失敗理・日次処理）です。性能影響時のBackuのC:は「Backup andで性能影響の確認ではコピーグループの」を述べ、対象は性能影響の確認 CG11（Backu・性能影・確認で・バックア）です。Assoを棚卸のD:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Assoc・棚卸・関連ノ・開始時刻）です。Manaを登録という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・登録・ドメイ・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0209**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0209について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0209A
    ```

    画面・出力には SP81DD0209A が表示され、ポリシーと管理クラス Management Class 0209 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0209B
    ```

    画面・出力には SP81DD0209B が表示され、ポリシーと管理クラス Management Class 0209 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0209C
    ```

    画面・出力には SP81DD0209C が表示され、ポリシーと管理クラス Management Class 0209 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0209A が画面・出力に表示されること
    ② ステップ2 の SP81DD0209B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0209C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0224 {#c14-i0443}
*分類: ポリシー*  ・  難易度: 上級

紅E確認0225ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紅E確認0225です。紅E確認0225はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録紅E確認0225です。紅E確認0225ではドメイン割当と取得時刻を採取票紅E確認0225へ残します。紅E確認0225では登録ドメインの取り違えを避けるため補助資料も照合する判断紅E確認0225です。紅E確認0225の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録紅E確認0225です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0224に関する障害切り分けの前提を確認しています。ポリシーと管理クラス DIRMC 0293の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅
    - B. 障害切り分けに用いる役割はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。
    - C. 障害切り分けに用いる役割はPolicy Domainで復旧準備ではポリシードメインの ポリシーセットからPolicySetを読みである。
    - D. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。

    正解: **A** ／ 難易度: 上級

    **解説:** 確認対象ManagでAの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・確認・ドメイ・登録ドメ）です。確認時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・確認・ドメイ・登録ドメです。抑止対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・抑止・ノード・管理クラ）です。復旧準備時のPolicのC:は「Policy Domainで復旧準備ではポリシードメインの」を述べ、対象は復旧準備 DOM05（Polic・復旧準・復旧準・ノードを）です。Poliを復旧のD:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Polic・復旧・ディレ・コピーグ）です。Manaを確認という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・確認・ドメイ・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0224**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0224について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0224A
    ```

    画面・出力には SP81DD0224A が表示され、ポリシーと管理クラス Management Class 0224 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0224B
    ```

    画面・出力には SP81DD0224B が表示され、ポリシーと管理クラス Management Class 0224 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0224C
    ```

    画面・出力には SP81DD0224C が表示され、ポリシーと管理クラス Management Class 0224 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0224A が画面・出力に表示されること
    ② ステップ2 の SP81DD0224B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0224C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0239 {#c14-i0444}
*分類: ポリシー*  ・  難易度: 上級

空T確認0240ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票空T確認0240です。空T確認0240はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録空T確認0240です。空T確認0240ではドメイン割当と取得時刻を採取票空T確認0240へ残します。空T確認0240ではコピーグループ未定義を避けるため補助資料も照合する判断空T確認0240です。空T確認0240の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録空T確認0240です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0239を保守記録に説明する必要があります。ポリシーと管理クラス Policy Set 0242と取り違えない説明はどれですか。

    - A. 仕様上の役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。ポリシーと管理クラス Policy Set 0242固有の属性も確認対象に含める。
    - B. 仕様上の役割はManagement Classのドメイン割当と取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅
    - C. 仕様上の役割はManagement Classで通常状態の確認では管理クラスのである。
    - D. 仕様上の役割はStart Timeの失敗理由と取得時刻を記録し・関連付け漏れを防ぐである。

    正解: **B** ／ 難易度: 上級

    **解説:** 確認対象ManagでBの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・確認・ドメイ・コピーグ）です。確認時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・確認・ドメイ・コピーグです。Polic・保護のA:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Polic・保護・ディレ・ディレク）です。通常状態時のManagのC:は「Management Classで通常状態の確認では管理クラスの」を述べ、対象は通常状態の確認 MC01（Manag・通常状・通常状・既定管理）です。Starを変更のD:は「Start Timeの失敗理由と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はStart Time（Start・変更・失敗理・関連付け）です。Manaを確認という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・確認・ドメイ・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0239**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0239について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0239A
    ```

    画面・出力には SP81DD0239A が表示され、ポリシーと管理クラス Management Class 0239 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0239B
    ```

    画面・出力には SP81DD0239B が表示され、ポリシーと管理クラス Management Class 0239 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0239C
    ```

    画面・出力には SP81DD0239C が表示され、ポリシーと管理クラス Management Class 0239 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0239A が画面・出力に表示されること
    ② ステップ2 の SP81DD0239B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0239C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0254 {#c14-i0445}
*分類: ポリシー*  ・  難易度: 初級

翠O保護0255ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票翠O保護0255です。翠O保護0255はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録翠O保護0255です。翠O保護0255ではドメイン割当と取得時刻を採取票翠O保護0255へ残します。翠O保護0255ではDIRMC誤設定を避けるため補助資料も照合する判断翠O保護0255です。翠O保護0255の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録翠O保護0255です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0254の技術的な意味を資料で確認するとき、クライアントスケジュール Action 0336との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はActionの開始時刻と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - B. コマンドまたは機能の用途はArchive Operationで依存関係の確認ではアーカイブ運用のである。
    - C. コマンドまたは機能の用途はManagement Classのドメイン割当と取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - D. コマンドまたは機能の用途はStorage Poolのストレージプール使用量と取得時刻を記録し・ノード状態の誤読を防ぐである。

    正解: **C** ／ 難易度: 初級

    **解説:** 保護対象ManagでCの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・保護・ドメイ・ディレク）です。保護時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・保護・ドメイ・ディレクです。Actio・計画のA:は「Actionの開始時刻と取得時刻を記録し、日次処理順序の誤読を防ぐ」を述べ、対象はクライアントスケジュール（Actio・計画・開始時・日次処理）です。依存関係対象ArchiのB:は「Archive Operationで依存関係の確認ではアーカイブ運用」を述べ、対象は依存関係の確認 ARC13（Archi・依存関・確認で・バックア）です。Storを移行のD:は「Storage Poolのストレージプール使用量と取得時刻を記録し」を述べ、対象はStorage Pool（Stora・移行・ストレ・ノード状）です。Manaを保護という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・保護・ドメイ・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0254**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0254について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0254A
    ```

    画面・出力には SP81DD0254A が表示され、ポリシーと管理クラス Management Class 0254 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0254B
    ```

    画面・出力には SP81DD0254B が表示され、ポリシーと管理クラス Management Class 0254 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0254C
    ```

    画面・出力には SP81DD0254C が表示され、ポリシーと管理クラス Management Class 0254 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0254A が画面・出力に表示されること
    ② ステップ2 の SP81DD0254B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0254C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0269 {#c14-i0446}
*分類: ポリシー*  ・  難易度: 中級

朱J照合0270ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票朱J照合0270です。朱J照合0270はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録朱J照合0270です。朱J照合0270ではドメイン割当と取得時刻を採取票朱J照合0270へ残します。朱J照合0270では管理クラス未割当を避けるため補助資料も照合する判断朱J照合0270です。朱J照合0270の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録朱J照合0270です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0269について構成や状態を確認します。クライアントスケジュール Association 0360ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はAssociationの関連ノードと取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - B. 一次資料が示す主目的はClient Nodeで構成監査ではノード管理の 占有量照会からLogicalFilesを読みである。
    - C. 一次資料が示す主目的はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。 ✅
    - D. 一次資料が示す主目的はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。

    正解: **C** ／ 難易度: 中級

    **解説:** 照合対象ManagでCの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・照合・ドメイ・管理クラ）です。照合時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・照合・ドメイ・管理クラです。Assoc・承認のA:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Assoc・承認・関連ノ・日次処理）です。構成監査対象ClienのB:は「Client Nodeで構成監査ではノード管理の」を述べ、対象は構成監査 NODE08（Clien・構成監・構成監・長期未接）です。Nodeを切替のD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・切替・運用状・プール容）です。Manaを照合という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・照合・ドメイ・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0269**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0269について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0269A
    ```

    画面・出力には SP81DD0269A が表示され、ポリシーと管理クラス Management Class 0269 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0269B
    ```

    画面・出力には SP81DD0269B が表示され、ポリシーと管理クラス Management Class 0269 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0269C
    ```

    画面・出力には SP81DD0269C が表示され、ポリシーと管理クラス Management Class 0269 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0269A が画面・出力に表示されること
    ② ステップ2 の SP81DD0269B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0269C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0284 {#c14-i0447}
*分類: ポリシー*  ・  難易度: 中級

紅E抑止0285ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紅E抑止0285です。紅E抑止0285はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録紅E抑止0285です。紅E抑止0285ではドメイン割当と取得時刻を採取票紅E抑止0285へ残します。紅E抑止0285では登録ドメインの取り違えを避けるため補助資料も照合する判断紅E抑止0285です。紅E抑止0285の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録紅E抑止0285です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0284の役割を調べています。ポリシーと管理クラス DIRMC 0338の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は調査操作で保守欄を引き継ぎすることでドメイン割当を確認し・登録ドメインの取り違えを防ぐ。 ✅
    - B. 障害切り分けに用いる役割は点検操作で判定欄を記録することでノード登録値を確認し・ディレクトリー管理クラス指定を防ぐ。
    - C. 障害切り分けに用いる役割は復旧確認で復旧後の確認を確認することで復旧後の確認を確認し・バックアップデータをアーカイを防ぐ。
    - D. 障害切り分けに用いる役割は監査操作で記録欄を比較することでイベント結果を確認し・失敗イベントの見落としを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 抑止対象ManagでAの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・抑止・ドメイ・登録ドメ）です。抑止時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・抑止・ドメイ・登録ドメです。計画対象ディレクトのB:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（ディレクト・計画・ノード・ディレク）です。復旧確認時のArchiのC:は「Archive Operationで復旧後の確認ではアーカイブ運用の」を述べ、対象は復旧後の確認 ARC06（Archi・復旧確・復旧後・バックア）です。Evenを変更のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・変更・イベン・失敗イベ）です。Manaを抑止という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・抑止・ドメイ・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0284**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0284について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0284A
    ```

    画面・出力には SP81DD0284A が表示され、ポリシーと管理クラス Management Class 0284 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0284B
    ```

    画面・出力には SP81DD0284B が表示され、ポリシーと管理クラス Management Class 0284 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0284C
    ```

    画面・出力には SP81DD0284C が表示され、ポリシーと管理クラス Management Class 0284 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0284A が画面・出力に表示されること
    ② ステップ2 の SP81DD0284B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0284C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0299 {#c14-i0448}
*分類: ポリシー*  ・  難易度: 中級

空T抑止0300ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票空T抑止0300です。空T抑止0300はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録空T抑止0300です。空T抑止0300ではドメイン割当と取得時刻を採取票空T抑止0300へ残します。空T抑止0300ではコピーグループ未定義を避けるため補助資料も照合する判断空T抑止0300です。空T抑止0300の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録空T抑止0300です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシーと管理クラス Management Class 0299」を「policy domain 保存期間確認 遅延表示」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は遅延表示で遅延表示を証跡に残し・クライアントに適用するバックアップとアーカイブの規則を束ねる。
    - B. 仕様上の役割は抑止でドメイン割当を証跡に残し・Management Classのドメイン割当と取得時刻を記。 ✅
    - C. 仕様上の役割は復旧準備で復旧準備ではを証跡に残し・Archive Operationで復旧準備ではアーカイブ運。
    - D. 仕様上の役割は保守で期限切れ処理を証跡に残し・Database Backupの期限切れ処理と取得時刻を記録。

    正解: **B** ／ 難易度: 中級

    **解説:** 抑止対象ManagでBの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・抑止・ドメイ・コピーグ）です。抑止時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・抑止・ドメイ・コピーグです。polic・遅延表示のA:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位」を述べ、対象は保存期間確認 遅延表示（polic・遅延表・遅延表・遅延表示）です。復旧準備時のArchiのC:は「Archive Operationで復旧準備ではアーカイブ運用の」を述べ、対象は復旧準備 ARC05（Archi・復旧準・復旧準・バックア）です。Dataを保守のD:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・保守・期限切・データベ）です。Manaを抑止という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・抑止・ドメイ・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0299**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0299について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0299A
    ```

    画面・出力には SP81DD0299A が表示され、ポリシーと管理クラス Management Class 0299 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0299B
    ```

    画面・出力には SP81DD0299B が表示され、ポリシーと管理クラス Management Class 0299 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0299C
    ```

    画面・出力には SP81DD0299C が表示され、ポリシーと管理クラス Management Class 0299 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0299A が画面・出力に表示されること
    ② ステップ2 の SP81DD0299B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0299C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0314 {#c14-i0449}
*分類: ポリシー*  ・  難易度: 中級

翠O解析0315ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票翠O解析0315です。翠O解析0315はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録翠O解析0315です。翠O解析0315ではドメイン割当と取得時刻を採取票翠O解析0315へ残します。翠O解析0315ではDIRMC誤設定を避けるため補助資料も照合する判断翠O解析0315です。翠O解析0315の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録翠O解析0315です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0314を同一分類のポリシーと管理クラス DIRMC 0323と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はディレクトリー管理クラス指定誤設を避けるため・点検操作で判定欄を記録するしてドメイン割当を照合する。 ✅
    - B. コマンドまたは機能の用途はコピーグループ未定義を避けるため・表示操作で対象欄を追跡するしてノード登録値を照合する。
    - C. コマンドまたは機能の用途は除外規則や失敗ファイルを見ず完了を避けるため・バックアップで障害切り分けを確認するして障害切り分けを照合する。
    - D. コマンドまたは機能の用途は関連付け漏れを避けるため・主操作で出力欄を評価するして開始時刻を照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 解析対象ManagでAの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・解析・ドメイ・ディレク）です。解析時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・解析・ドメイ・ディレクです。計画対象ディレクトのB:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（ディレクト・計画・ノード・コピーグ）です。バックア時のIncreのC:は「Incremental Backupで障害切り分けではバックアップ運」を述べ、対象は障害切り分け BKP04（Incre・バック・障害切・除外規則）です。Actiを登録のD:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Actio・登録・開始時・関連付け）です。Manaを解析という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・解析・ドメイ・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0314**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0314について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0314A
    ```

    画面・出力には SP81DD0314A が表示され、ポリシーと管理クラス Management Class 0314 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0314B
    ```

    画面・出力には SP81DD0314B が表示され、ポリシーと管理クラス Management Class 0314 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0314C
    ```

    画面・出力には SP81DD0314C が表示され、ポリシーと管理クラス Management Class 0314 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0314A が画面・出力に表示されること
    ② ステップ2 の SP81DD0314B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0314C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0329 {#c14-i0450}
*分類: ポリシー*  ・  難易度: 中級

朱J計画0330ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票朱J計画0330です。朱J計画0330はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録朱J計画0330です。朱J計画0330ではドメイン割当と取得時刻を採取票朱J計画0330へ残します。朱J計画0330では管理クラス未割当を避けるため補助資料も照合する判断朱J計画0330です。朱J計画0330の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録朱J計画0330です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0329の設定や表示を読む前に役割を確認します。expiration 復元前確認 自動処理ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認する。復元前確認で自動処理を確認するときは自動処理の誤読を防ぐ。
    - B. 一次資料が示す主目的はManagement Classのドメイン割当と取得時刻を記録し・管理クラス未割当を防ぐである。復旧操作で点検欄を確認するときは管理クラス未割当を防ぐ。 ✅
    - C. 一次資料が示す主目的はStart Timeの失敗理由と取得時刻を記録し・開始時刻誤設定を防ぐである。変更確認操作で採取欄を棚卸するときは開始時刻誤設定を防ぐ。
    - D. 一次資料が示す主目的はNode Nameの運用状態と取得時刻を記録し・プール容量不足の見落としを防ぐである。採取操作で照合欄を点検するときはプール容量不足の見落としを防ぐ。サーバー日次運用 Node Name 0163固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 中級

    **解説:** 計画対象ManagでBの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・計画・ドメイ・管理クラ）です。計画時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・計画・ドメイ・管理クラです。expir・復元前確認のA:は「保存期間を過ぎた版やアーカイブを期限切れにする処理を復元前確認する」を述べ、対象は復元前確認 自動処理（expir・復元前・自動処・自動処理）です。巡回時のStartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・巡回・失敗理・開始時刻）です。Nodeを切替のD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・切替・運用状・プール容）です。Manaを計画という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・計画・ドメイ・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0329**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0329について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC08
    確認コード SP81DD0329A
    ```

    画面・出力には SP81DD0329A が表示され、ポリシーと管理クラス Management Class 0329 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0329B
    ```

    画面・出力には SP81DD0329B が表示され、ポリシーと管理クラス Management Class 0329 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0329C
    ```

    画面・出力には SP81DD0329C が表示され、ポリシーと管理クラス Management Class 0329 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0329A が画面・出力に表示されること
    ② ステップ2 の SP81DD0329B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0329C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0344 {#c14-i0451}
*分類: ポリシー*  ・  難易度: 上級

紅E解除0345ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紅E解除0345です。紅E解除0345はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録紅E解除0345です。紅E解除0345ではドメイン割当と取得時刻を採取票紅E解除0345へ残します。紅E解除0345では登録ドメインの取り違えを避けるため補助資料も照合する判断紅E解除0345です。紅E解除0345の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録紅E解除0345です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0344に関する障害切り分けの前提を確認しています。policy domain ノード割当確認 保持期間の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はクライアントに適用するバックアップとアーカイブの規則を束ねる単位をノード割当確認する。ノード割当確で保持期間を確認するときは保持期間の誤読を防ぐ。
    - B. 障害切り分けに用いる役割はDBで代替経路の確認ではサーバーの DB状態からLastDatabaseを読み・代替経路確認に使うである。代替経路確認で代替経路の確を確認するときはデータベースバックアップ媒体を防ぐ。
    - C. 障害切り分けに用いる役割はStart Timeの失敗理由と取得時刻を記録し・日次処理順序の誤読を防ぐである。照合操作で確認欄を採取するときは日次処理順序の誤読を防ぐ。
    - D. 障害切り分けに用いる役割はManagement Classのドメイン割当と取得時刻を記録し・登録ドメインの取り違えを防ぐである。調査操作で保守欄を引き継ぎするときは登録ドメインの取り違えを防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 解除対象ManagでDの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・解除・ドメイ・登録ドメ）です。解除時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・解除・ドメイ・登録ドメです。polic・ノード割当のA:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をノ」を述べ、対象はノード割当確認 保持期間（polic・ノード・保持期・保持期間）です。代替経路対象データベーのB:は「DBで代替経路の確認ではサーバーの DB状態からLastDataba」を述べ、対象は代替経路の確認 DBBK10（データベー・代替経・代替経・データベ）です。切替時のStartのC:は「Start Timeの失敗理由と取得時刻を記録し」を述べ、対象はStart Time（Start・切替・失敗理・日次処理）です。Manaを解除という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・解除・ドメイ・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0344**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0344について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC05
    確認コード SP81DD0344A
    ```

    画面・出力には SP81DD0344A が表示され、ポリシーと管理クラス Management Class 0344 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0344B
    ```

    画面・出力には SP81DD0344B が表示され、ポリシーと管理クラス Management Class 0344 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0344C
    ```

    画面・出力には SP81DD0344C が表示され、ポリシーと管理クラス Management Class 0344 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0344A が画面・出力に表示されること
    ② ステップ2 の SP81DD0344B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0344C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Management Class 0359 {#c14-i0452}
*分類: ポリシー*  ・  難易度: 上級

空T解除0360ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票空T解除0360です。空T解除0360はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録空T解除0360です。空T解除0360ではドメイン割当と取得時刻を採取票空T解除0360へ残します。空T解除0360ではコピーグループ未定義を避けるため補助資料も照合する判断空T解除0360です。空T解除0360の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録空T解除0360です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Management Class 0359を保守記録に説明する必要があります。backup copy group 状態確認 文字変換と取り違えない説明はどれですか。

    - A. 仕様上の役割は状態確認で文字変換を確認することで文字変換を確認し・文字変換の誤読を防ぐ。
    - B. 仕様上の役割は表示操作で対象欄を追跡することでドメイン割当を確認し・コピーグループ未定義を防ぐ。 ✅
    - C. 仕様上の役割は表示操作で対象欄を追跡することでコピーグルーを確認し・コピーグループ未定義を防ぐ。ポリシーと管理クラス Copy Group 0011固有の属性も確認対象に含める。
    - D. 仕様上の役割は変更確認操作で採取欄を棚卸することでイベント結果を確認し・開始時刻誤設定を防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 解除対象ManagでBの記述「Management Classのドメイン割当と取得時刻を記録し」に対応する項目はManagement Class（Manag・解除・ドメイ・コピーグ）です。解除時のManagに関するポリシーの仕様は「Management Classのドメイン割当と取得時刻を記録し」で、確認対象はMana・解除・ドメイ・コピーグです。backu・状態確認のA:は「バックアップ版数と保存先を定めるコピー規則」を述べ、対象は状態確認 文字変換（backu・状態確・文字変・文字変換）です。巡回時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・巡回・コピー・コピーグ）です。Evenを確認のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・確認・イベン・開始時刻）です。Manaを解除という用語は「Management Classのドメイン割当と取得」を指し、Management Class（Manag・解除・ドメイ・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Management Class 0359**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Management Class 0359について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Management Class と ドメイン割当
    - セッション環境: 机上検証。IBM Spectrum Protect 8.1のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> REGISTER NODE
    → Enter を押す
    ```

    画面・出力:
    ```text
    Policy Domain STANDARD
    Policy Set ACTIVE
    Management Class MC02
    確認コード SP81DD0359A
    ```

    画面・出力には SP81DD0359A が表示され、ポリシーと管理クラス Management Class 0359 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
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
    確認コード SP81DD0359B
    ```

    画面・出力には SP81DD0359B が表示され、ポリシーと管理クラス Management Class 0359 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はIBM Spectrum Protect 8.1の確認画面またはコマンド結果です。Management Class を読むため、ポリシーと管理クラス の対象値を表示します。
    操作（入力）:
    ```text
    IBM Spectrum Protect 8.1 操作画面またはコマンド環境
    COMMAND ===> dsmadmc QUERY DOMAIN
    → Enter を押す
    ```

    画面・出力:
    ```text
    DIRMC MC_DIR04
    Include Exclude rule reviewed
    Client option file checked
    確認コード SP81DD0359C
    ```

    画面・出力には SP81DD0359C が表示され、ポリシーと管理クラス Management Class 0359 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0359A が画面・出力に表示されること
    ② ステップ2 の SP81DD0359B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0359C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0005 {#c14-i0453}
*分類: ポリシー*  ・  難易度: 初級

銀F巡回0006ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票銀F巡回0006です。銀F巡回0006はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録銀F巡回0006です。銀F巡回0006では管理クラス詳細と取得時刻を採取票銀F巡回0006へ残します。銀F巡回0006では管理クラス未割当を避けるため補助資料も照合する判断銀F巡回0006です。銀F巡回0006の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録銀F巡回0006です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0005について構成や状態を確認します。クライアントスケジュール Action 0021ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。 ✅
    - B. 一次資料が示す主目的はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。
    - C. 一次資料が示す主目的はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - D. 一次資料が示す主目的はサーバーへ登録されたクライアントを表す管理単位である。

    正解: **A** ／ 難易度: 初級

    **解説:** 巡回対象PolicでAの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Policy・巡回・管理クラ）です。ポリシに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPolic・巡回・管理クラです。棚卸対象ActioのB:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Action・棚卸・開始時刻）です。登録時のEventのC:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・登録・イベント）です。nodeを保存期間確のD:は「サーバーへ登録されたクライアントを表す管理単位」を述べ、対象は保存期間確認 活動ログ（node・保存期・活動ログ）です。Poliを巡回という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Policy・巡回・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0005**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0005について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC05
    確認コード SP81DD0005A
    ```

    画面・出力には SP81DD0005A が表示され、ポリシーと管理クラス Policy Domain 0005 の入力欄確認を確認できます。

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
    確認コード SP81DD0005B
    ```

    画面・出力には SP81DD0005B が表示され、ポリシーと管理クラス Policy Domain 0005 の証跡表示確認を確認できます。

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
    確認コード SP81DD0005C
    ```

    画面・出力には SP81DD0005C が表示され、ポリシーと管理クラス Policy Domain 0005 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0005A が画面・出力に表示されること
    ② ステップ2 の SP81DD0005B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0005C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0020 {#c14-i0454}
*分類: ポリシー*  ・  難易度: 初級

蒼A棚卸0021ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票蒼A棚卸0021です。蒼A棚卸0021はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録蒼A棚卸0021です。蒼A棚卸0021では管理クラス詳細と取得時刻を採取票蒼A棚卸0021へ残します。蒼A棚卸0021では登録ドメインの取り違えを避けるため補助資料も照合する判断蒼A棚卸0021です。蒼A棚卸0021の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録蒼A棚卸0021です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0020の役割を調べています。ポリシーと管理クラス Policy Set 0062の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・DIRMC誤設定を防ぐである。
    - B. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅
    - C. 障害切り分けに用いる役割はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。ポリシーと管理クラス DIRMC 0218固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割はサーバーへ登録されたクライアントを表す管理単位である。

    正解: **B** ／ 難易度: 初級

    **解説:** 棚卸対象PolicでBの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Policy・棚卸・管理クラ）です。ポリシに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPolic・棚卸・管理クラです。Polic・監査のA:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・監査・ディレク）です。登録時のDIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・登録・ノード登）です。nodeを宛先照合のD:は「サーバーへ登録されたクライアントを表す管理単位」を述べ、対象は宛先照合 データソース（node・宛先照・データソ）です。Poliを棚卸という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Policy・棚卸・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0020**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0020について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード SP81DD0020A
    ```

    画面・出力には SP81DD0020A が表示され、ポリシーと管理クラス Policy Domain 0020 の入力欄確認を確認できます。

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
    Destination DIRPOOL06
    Retain Extra Versions 30
    確認コード SP81DD0020B
    ```

    画面・出力には SP81DD0020B が表示され、ポリシーと管理クラス Policy Domain 0020 の証跡表示確認を確認できます。

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
    確認コード SP81DD0020C
    ```

    画面・出力には SP81DD0020C が表示され、ポリシーと管理クラス Policy Domain 0020 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0020A が画面・出力に表示されること
    ② ステップ2 の SP81DD0020B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0020C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0035 {#c14-i0455}
*分類: ポリシー*  ・  難易度: 中級

金P棚卸0036ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票金P棚卸0036です。金P棚卸0036はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録金P棚卸0036です。金P棚卸0036では管理クラス詳細と取得時刻を採取票金P棚卸0036へ残します。金P棚卸0036ではコピーグループ未定義を避けるため補助資料も照合する判断金P棚卸0036です。金P棚卸0036の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録金P棚卸0036です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシーと管理クラス Policy Domain 0035」を「サーバー日次運用 Database Backup 0067」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅
    - B. 仕様上の役割はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - C. 仕様上の役割はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。
    - D. 仕様上の役割はClient Nodeで依存関係の確認ではノード管理の ノード照会からLastAccessを読みである。

    正解: **A** ／ 難易度: 中級

    **解説:** 棚卸対象PolicでAの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Policy・棚卸・管理クラ）です。棚卸時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPolic・棚卸・管理クラです。監査対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databa・監査・期限切れ）です。確認時のDIRMCのC:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・確認・ノード登）です。Clieを依存関係確のD:は「Client Nodeで依存関係の確認ではノード管理の」を述べ、対象は依存関係の確認 NODE13（Client・依存関・依存関係）です。Poliを棚卸という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Policy・棚卸・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0035**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0035について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC08
    確認コード SP81DD0035A
    ```

    画面・出力には SP81DD0035A が表示され、ポリシーと管理クラス Policy Domain 0035 の入力欄確認を確認できます。

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
    Destination DIRPOOL00
    Retain Extra Versions 30
    確認コード SP81DD0035B
    ```

    画面・出力には SP81DD0035B が表示され、ポリシーと管理クラス Policy Domain 0035 の証跡表示確認を確認できます。

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
    確認コード SP81DD0035C
    ```

    画面・出力には SP81DD0035C が表示され、ポリシーと管理クラス Policy Domain 0035 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0035A が画面・出力に表示されること
    ② ステップ2 の SP81DD0035B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0035C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0050 {#c14-i0456}
*分類: ポリシー*  ・  難易度: 中級

紺K復旧0051ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紺K復旧0051です。紺K復旧0051はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録紺K復旧0051です。紺K復旧0051では管理クラス詳細と取得時刻を採取票紺K復旧0051へ残します。紺K復旧0051ではDIRMC誤設定を避けるため補助資料も照合する判断紺K復旧0051です。紺K復旧0051の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録紺K復旧0051です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0050を同一分類のクライアントスケジュール Event Status 0117と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はPolicy Domainの管理クラス詳細と取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - B. コマンドまたは機能の用途はEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。
    - C. コマンドまたは機能の用途はDatabase Backupの期限切れ処理と取得時刻を記録し・プール容量不足の見落としを防ぐである。
    - D. コマンドまたは機能の用途はBackup andで復旧準備ではコピーグループの アーカイブグループからRetainVersionを読みである。

    正解: **A** ／ 難易度: 中級

    **解説:** 復旧対象PolicでAの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Policy・復旧・管理クラ）です。復旧時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPolic・復旧・管理クラです。移行対象EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・移行・イベント）です。保護時のDatabのC:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Databa・保護・期限切れ）です。Backを復旧準備のD:は「Backup andで復旧準備ではコピーグループの」を述べ、対象は復旧準備 CG05（Backup・復旧準・復旧準備）です。Poliを復旧という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Policy・復旧・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0050**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0050について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC05
    確認コード SP81DD0050A
    ```

    画面・出力には SP81DD0050A が表示され、ポリシーと管理クラス Policy Domain 0050 の入力欄確認を確認できます。

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
    Destination DIRPOOL01
    Retain Extra Versions 30
    確認コード SP81DD0050B
    ```

    画面・出力には SP81DD0050B が表示され、ポリシーと管理クラス Policy Domain 0050 の証跡表示確認を確認できます。

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
    確認コード SP81DD0050C
    ```

    画面・出力には SP81DD0050C が表示され、ポリシーと管理クラス Policy Domain 0050 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0050A が画面・出力に表示されること
    ② ステップ2 の SP81DD0050B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0050C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0065 {#c14-i0457}
*分類: ポリシー*  ・  難易度: 中級

銀F監査0066ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票銀F監査0066です。銀F監査0066はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録銀F監査0066です。銀F監査0066では管理クラス詳細と取得時刻を採取票銀F監査0066へ残します。銀F監査0066では管理クラス未割当を避けるため補助資料も照合する判断銀F監査0066です。銀F監査0066の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録銀F監査0066です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0065の設定や表示を読む前に役割を確認します。サーバー日次運用 Server Name 0076ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。 ✅
    - B. 一次資料が示す主目的はServer NameのDBバックアップ履歴と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - C. 一次資料が示す主目的はPolicy Setのディレクトリ管理クラスと取得時刻を記録し・コピーグループ未定義を防ぐである。
    - D. 一次資料が示す主目的はArchive Operationで構成監査ではアーカイブ運用のである。

    正解: **A** ／ 難易度: 中級

    **解説:** 監査対象PolicでAの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Policy・監査・管理クラ）です。監査時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPolic・監査・管理クラです。監査対象ServeのB:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Server・監査・データベ）です。抑止時のPolicのC:は「Policy Setのディレクトリ管理クラスと取得時刻を記録し」を述べ、対象はPolicy Set（Policy・抑止・ディレク）です。Archを構成監査のD:は「Archive Operationで構成監査ではアーカイブ運用の」を述べ、対象は構成監査 ARC08（Archiv・構成監・構成監査）です。Poliを監査という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Policy・監査・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0065**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0065について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード SP81DD0065A
    ```

    画面・出力には SP81DD0065A が表示され、ポリシーと管理クラス Policy Domain 0065 の入力欄確認を確認できます。

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
    Destination DIRPOOL02
    Retain Extra Versions 30
    確認コード SP81DD0065B
    ```

    画面・出力には SP81DD0065B が表示され、ポリシーと管理クラス Policy Domain 0065 の証跡表示確認を確認できます。

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
    確認コード SP81DD0065C
    ```

    画面・出力には SP81DD0065C が表示され、ポリシーと管理クラス Policy Domain 0065 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0065A が画面・出力に表示されること
    ② ステップ2 の SP81DD0065B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0065C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0080 {#c14-i0458}
*分類: ポリシー*  ・  難易度: 中級

蒼A変更0081ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票蒼A変更0081です。蒼A変更0081はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録蒼A変更0081です。蒼A変更0081では管理クラス詳細と取得時刻を採取票蒼A変更0081へ残します。蒼A変更0081では登録ドメインの取り違えを避けるため補助資料も照合する判断蒼A変更0081です。蒼A変更0081の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録蒼A変更0081です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0080に関する障害切り分けの前提を確認しています。ポリシーと管理クラス DIRMC 0098の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - B. 障害切り分けに用いる役割はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。
    - C. 障害切り分けに用いる役割はStorage Poolで引継ぎ記録では複製・保護の 検証からANR3730Iを読み・複製・保護に使うである。
    - D. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 変更対象PolicでDの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Policy・変更・管理クラ）です。変更時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPolic・変更・管理クラです。変更対象ノード登録のA:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・変更・ノード登）です。計画対象EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・計画・イベント）です。複製時のStoraのC:は「Storage Poolで引継ぎ記録では複製・保護の」を述べ、対象は引継ぎ記録 REPL09（Storag・複製・引継ぎ記）です。Poliを変更という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Policy・変更・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0080**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0080について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC08
    確認コード SP81DD0080A
    ```

    画面・出力には SP81DD0080A が表示され、ポリシーと管理クラス Policy Domain 0080 の入力欄確認を確認できます。

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
    Destination DIRPOOL03
    Retain Extra Versions 30
    確認コード SP81DD0080B
    ```

    画面・出力には SP81DD0080B が表示され、ポリシーと管理クラス Policy Domain 0080 の証跡表示確認を確認できます。

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
    確認コード SP81DD0080C
    ```

    画面・出力には SP81DD0080C が表示され、ポリシーと管理クラス Policy Domain 0080 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0080A が画面・出力に表示されること
    ② ステップ2 の SP81DD0080B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0080C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0095 {#c14-i0459}
*分類: ポリシー*  ・  難易度: 中級

金P変更0096ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票金P変更0096です。金P変更0096はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録金P変更0096です。金P変更0096では管理クラス詳細と取得時刻を採取票金P変更0096へ残します。金P変更0096ではコピーグループ未定義を避けるため補助資料も照合する判断金P変更0096です。金P変更0096の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録金P変更0096です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0095を保守記録に説明する必要があります。クライアントスケジュール Event Status 0147と取り違えない説明はどれですか。

    - A. 仕様上の役割はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。クライアントスケジュール Event Status 0147固有の属性も確認対象に含める。
    - B. 仕様上の役割はクライアントに適用するバックアップとアーカイブの規則を束ねる単位をノード割当確認する。
    - C. 仕様上の役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅
    - D. 仕様上の役割はArchive Operationで変更後の確認ではアーカイブ運用のである。

    正解: **C** ／ 難易度: 中級

    **解説:** 変更対象PolicでCの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Policy・変更・管理クラ）です。変更時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPolic・変更・管理クラです。Event・保守のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・保守・イベント）です。ノード割対象policのB:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をノ」を述べ、対象はノード割当確認 保持期間（policy・ノード・保持期間）です。Archを変更確認のD:は「Archive Operationで変更後の確認ではアーカイブ運用の」を述べ、対象は変更後の確認 ARC03（Archiv・変更確・変更後の）です。Poliを変更という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Policy・変更・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0095**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0095について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC05
    確認コード SP81DD0095A
    ```

    画面・出力には SP81DD0095A が表示され、ポリシーと管理クラス Policy Domain 0095 の入力欄確認を確認できます。

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
    Destination DIRPOOL04
    Retain Extra Versions 30
    確認コード SP81DD0095B
    ```

    画面・出力には SP81DD0095B が表示され、ポリシーと管理クラス Policy Domain 0095 の証跡表示確認を確認できます。

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
    確認コード SP81DD0095C
    ```

    画面・出力には SP81DD0095C が表示され、ポリシーと管理クラス Policy Domain 0095 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0095A が画面・出力に表示されること
    ② ステップ2 の SP81DD0095B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0095C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0110 {#c14-i0460}
*分類: ポリシー*  ・  難易度: 上級

紺K移行0111ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紺K移行0111です。紺K移行0111はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録紺K移行0111です。紺K移行0111では管理クラス詳細と取得時刻を採取票紺K移行0111へ残します。紺K移行0111ではDIRMC誤設定を避けるため補助資料も照合する判断紺K移行0111です。紺K移行0111の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録紺K移行0111です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0110の技術的な意味を資料で確認するとき、ポリシーと管理クラス DIRMC 0158との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はDIRMCのノード登録値と取得時刻を記録し・DIRMC誤設定を防ぐである。
    - B. コマンドまたは機能の用途はPolicy Domainの管理クラス詳細と取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - C. コマンドまたは機能の用途はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。
    - D. コマンドまたは機能の用途はDBで停止前の確認ではサーバーの DBバックアップからANR4550Iを読み・停止確認に使うである。

    正解: **B** ／ 難易度: 上級

    **解説:** 移行対象PolicでBの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Policy・移行・管理クラ）です。移行時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPolic・移行・管理クラです。保守対象ノード登録のA:は「DIRMCのノード登録値と取得時刻を記録し、DIRMC誤設定を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・保守・ノード登）です。解析時のActioのC:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Action・解析・開始時刻）です。停止前の確を停止確認のD:は「DBで停止前の確認ではサーバーの DBバックアップからANR4550」を述べ、対象は停止前の確認 DBBK14（DB・停止確・停止前の）です。Poliを移行という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Policy・移行・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0110**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0110について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード SP81DD0110A
    ```

    画面・出力には SP81DD0110A が表示され、ポリシーと管理クラス Policy Domain 0110 の入力欄確認を確認できます。

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
    確認コード SP81DD0110B
    ```

    画面・出力には SP81DD0110B が表示され、ポリシーと管理クラス Policy Domain 0110 の証跡表示確認を確認できます。

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
    確認コード SP81DD0110C
    ```

    画面・出力には SP81DD0110C が表示され、ポリシーと管理クラス Policy Domain 0110 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0110A が画面・出力に表示されること
    ② ステップ2 の SP81DD0110B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0110C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0125 {#c14-i0461}
*分類: ポリシー*  ・  難易度: 初級

銀F診断0126ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票銀F診断0126です。銀F診断0126はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録銀F診断0126です。銀F診断0126では管理クラス詳細と取得時刻を採取票銀F診断0126へ残します。銀F診断0126では管理クラス未割当を避けるため補助資料も照合する判断銀F診断0126です。銀F診断0126の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録銀F診断0126です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0125について構成や状態を確認します。クライアントスケジュール Event Status 0192ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。 ✅
    - B. 一次資料が示す主目的はEvent Statusのイベント結果と取得時刻を記録し・日次処理順序の誤読を防ぐである。
    - C. 一次資料が示す主目的はクライアントに適用するバックアップとアーカイブの規則を束ねる単位をコマンド証跡として確認する。
    - D. 一次資料が示す主目的はClient Restoreで引継ぎ記録ではリストア確認の 活動ログからRestoreを読みである。

    正解: **A** ／ 難易度: 初級

    **解説:** 診断対象PolicでAの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・診断・管理ク・管理クラ）です。診断時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・診断・管理ク・管理クラです。収集対象EventのB:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・収集・イベン・日次処理）です。コピーグ時のpolicのC:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位をコ」を述べ、対象はコマンド証跡 重大度（polic・コピー・重大度・重大度の）です。Clieをリストア確のD:は「Client Restoreで引継ぎ記録ではリストア確認の」を述べ、対象は引継ぎ記録 RST09（Clien・リスト・引継ぎ・置換条件）です。Poliを診断という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・診断・管理ク・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0125**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0125について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC05
    確認コード SP81DD0125A
    ```

    画面・出力には SP81DD0125A が表示され、ポリシーと管理クラス Policy Domain 0125 の入力欄確認を確認できます。

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
    確認コード SP81DD0125B
    ```

    画面・出力には SP81DD0125B が表示され、ポリシーと管理クラス Policy Domain 0125 の証跡表示確認を確認できます。

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
    確認コード SP81DD0125C
    ```

    画面・出力には SP81DD0125C が表示され、ポリシーと管理クラス Policy Domain 0125 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0125A が画面・出力に表示されること
    ② ステップ2 の SP81DD0125B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0125C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0140 {#c14-i0462}
*分類: ポリシー*  ・  難易度: 初級

蒼A保守0141ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票蒼A保守0141です。蒼A保守0141はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録蒼A保守0141です。蒼A保守0141では管理クラス詳細と取得時刻を採取票蒼A保守0141へ残します。蒼A保守0141では登録ドメインの取り違えを避けるため補助資料も照合する判断蒼A保守0141です。蒼A保守0141の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録蒼A保守0141です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0140の役割を調べています。サーバー日次運用 Database Backup 0202の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はDatabase Backupの期限切れ処理と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。
    - B. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅
    - C. 障害切り分けに用いる役割はAssociationの関連ノードと取得時刻を記録し・関連付け漏れを防ぐである。
    - D. 障害切り分けに用いる役割はSchedule Nameのスケジュール定義と取得時刻を記録し・失敗イベントの見落としを防ぐである。

    正解: **B** ／ 難易度: 初級

    **解説:** 保守対象PolicでBの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・保守・管理ク・登録ドメ）です。保守時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・保守・管理ク・登録ドメです。Datab・登録のA:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・登録・期限切・データベ）です。解除時のAssocのC:は「Associationの関連ノードと取得時刻を記録し」を述べ、対象はクライアントスケジュール（Assoc・解除・関連ノ・関連付け）です。Scheを棚卸のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Sched・棚卸・スケジ・失敗イベ）です。Poliを保守という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・保守・管理ク・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0140**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0140について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード SP81DD0140A
    ```

    画面・出力には SP81DD0140A が表示され、ポリシーと管理クラス Policy Domain 0140 の入力欄確認を確認できます。

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
    Destination DIRPOOL06
    Retain Extra Versions 30
    確認コード SP81DD0140B
    ```

    画面・出力には SP81DD0140B が表示され、ポリシーと管理クラス Policy Domain 0140 の証跡表示確認を確認できます。

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
    確認コード SP81DD0140C
    ```

    画面・出力には SP81DD0140C が表示され、ポリシーと管理クラス Policy Domain 0140 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0140A が画面・出力に表示されること
    ② ステップ2 の SP81DD0140B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0140C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0155 {#c14-i0463}
*分類: ポリシー*  ・  難易度: 中級

金P保守0156ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票金P保守0156です。金P保守0156はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録金P保守0156です。金P保守0156では管理クラス詳細と取得時刻を採取票金P保守0156へ残します。金P保守0156ではコピーグループ未定義を避けるため補助資料も照合する判断金P保守0156です。金P保守0156の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録金P保守0156です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシーと管理クラス Policy Domain 0155」を「ポリシーと管理クラス DIRMC 0173」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。
    - B. 仕様上の役割は保存期間を過ぎた版やアーカイブを期限切れにする処理をノード割当確認する。expiration ノード割当確認 管理レポート固有の属性も確認対象に含める。
    - C. 仕様上の役割はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。
    - D. 仕様上の役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 保守対象PolicでDの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・保守・管理ク・コピーグ）です。保守時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・保守・管理ク・コピーグです。切替対象ノード登録のA:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・切替・ノード・管理クラ）です。ノード割対象expirのB:は「保存期間を過ぎた版やアーカイブを期限切れにする処理をノード割当確認す」を述べ、対象はノード割当確認 管理レポート（expir・ノード・管理レ・管理レポ）です。巡回時のActioのC:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Actio・巡回・開始時・開始時刻）です。Poliを保守という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・保守・管理ク・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0155**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0155について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC08
    確認コード SP81DD0155A
    ```

    画面・出力には SP81DD0155A が表示され、ポリシーと管理クラス Policy Domain 0155 の入力欄確認を確認できます。

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
    Destination DIRPOOL00
    Retain Extra Versions 30
    確認コード SP81DD0155B
    ```

    画面・出力には SP81DD0155B が表示され、ポリシーと管理クラス Policy Domain 0155 の証跡表示確認を確認できます。

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
    確認コード SP81DD0155C
    ```

    画面・出力には SP81DD0155C が表示され、ポリシーと管理クラス Policy Domain 0155 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0155A が画面・出力に表示されること
    ② ステップ2 の SP81DD0155B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0155C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0170 {#c14-i0464}
*分類: ポリシー*  ・  難易度: 中級

紺K切替0171ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紺K切替0171です。紺K切替0171はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録紺K切替0171です。紺K切替0171では管理クラス詳細と取得時刻を採取票紺K切替0171へ残します。紺K切替0171ではDIRMC誤設定を避けるため補助資料も照合する判断紺K切替0171です。紺K切替0171の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録紺K切替0171です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0170を同一分類のクライアントスケジュール Event Status 0237と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はEvent Statusのイベント結果と取得時刻を記録し・関連付け漏れを防ぐである。
    - B. コマンドまたは機能の用途はクライアントに適用するバックアップとアーカイブの規則を束ねる単位を復元前確認する。
    - C. コマンドまたは機能の用途はPolicy Domainの管理クラス詳細と取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - D. コマンドまたは機能の用途はServer NameのDBバックアップ履歴と取得時刻を記録し・DBバックアップ時刻の記録漏れを防ぐである。

    正解: **C** ／ 難易度: 中級

    **解説:** 切替対象PolicでCの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・切替・管理ク・ディレク）です。切替時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・切替・管理ク・ディレクです。Event・確認のA:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・確認・イベン・関連付け）です。復元前確対象policのB:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位を復」を述べ、対象は復元前確認 統合管理（polic・復元前・統合管・統合管理）です。Servを復旧のD:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Serve・復旧・データ・データベ）です。Poliを切替という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・切替・管理ク・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0170**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0170について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC05
    確認コード SP81DD0170A
    ```

    画面・出力には SP81DD0170A が表示され、ポリシーと管理クラス Policy Domain 0170 の入力欄確認を確認できます。

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
    Destination DIRPOOL01
    Retain Extra Versions 30
    確認コード SP81DD0170B
    ```

    画面・出力には SP81DD0170B が表示され、ポリシーと管理クラス Policy Domain 0170 の証跡表示確認を確認できます。

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
    確認コード SP81DD0170C
    ```

    画面・出力には SP81DD0170C が表示され、ポリシーと管理クラス Policy Domain 0170 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0170A が画面・出力に表示されること
    ② ステップ2 の SP81DD0170B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0170C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0185 {#c14-i0465}
*分類: ポリシー*  ・  難易度: 中級

銀F収集0186ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票銀F収集0186です。銀F収集0186はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録銀F収集0186です。銀F収集0186では管理クラス詳細と取得時刻を採取票銀F収集0186へ残します。銀F収集0186では管理クラス未割当を避けるため補助資料も照合する判断銀F収集0186です。銀F収集0186の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録銀F収集0186です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0185の設定や表示を読む前に役割を確認します。サーバー日次運用 Node Name 0253ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はNode Nameの運用状態と取得時刻を記録し・期限切れ処理の未実行を防ぐである。
    - B. 一次資料が示す主目的はバックアップや管理コマンドを決めた時刻に実行する定義を復元前確認する。
    - C. 一次資料が示す主目的はDBで依存関係の確認ではサーバーの DB状態からLastDatabaseを読み・依存関係確認に使うである。
    - D. 一次資料が示す主目的はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 収集対象PolicでDの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・収集・管理ク・管理クラ）です。収集時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・収集・管理ク・管理クラです。Node・保護のA:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・保護・運用状・期限切れ）です。復元前確対象schedのB:は「バックアップや管理コマンドを決めた時刻に実行する定義を復元前確認する」を述べ、対象は復元前確認 時刻合わせ（sched・復元前・時刻合・時刻合わ）です。依存関係時のDBのC:は「DBで依存関係の確認ではサーバーの DB状態からLastDataba」を述べ、対象は依存関係の確認 DBBK13（DB・依存関・依存関・データベ）です。Poliを収集という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・収集・管理ク・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0185**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0185について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード SP81DD0185A
    ```

    画面・出力には SP81DD0185A が表示され、ポリシーと管理クラス Policy Domain 0185 の入力欄確認を確認できます。

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
    Destination DIRPOOL02
    Retain Extra Versions 30
    確認コード SP81DD0185B
    ```

    画面・出力には SP81DD0185B が表示され、ポリシーと管理クラス Policy Domain 0185 の証跡表示確認を確認できます。

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
    確認コード SP81DD0185C
    ```

    画面・出力には SP81DD0185C が表示され、ポリシーと管理クラス Policy Domain 0185 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0185A が画面・出力に表示されること
    ② ステップ2 の SP81DD0185B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0185C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0200 {#c14-i0466}
*分類: ポリシー*  ・  難易度: 中級

蒼A登録0201ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票蒼A登録0201です。蒼A登録0201はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録蒼A登録0201です。蒼A登録0201では管理クラス詳細と取得時刻を採取票蒼A登録0201へ残します。蒼A登録0201では登録ドメインの取り違えを避けるため補助資料も照合する判断蒼A登録0201です。蒼A登録0201の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録蒼A登録0201です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0200に関する障害切り分けの前提を確認しています。ポリシーと管理クラス DIRMC 0233の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅
    - B. 障害切り分けに用いる役割はDIRMCのノード登録値と取得時刻を記録し・管理クラス未割当を防ぐである。
    - C. 障害切り分けに用いる役割はManagement Classで通常状態の確認では管理クラスのである。
    - D. 障害切り分けに用いる役割はExpiration Statusのノード登録と取得時刻を記録し・期限切れ処理の未実行を防ぐである。

    正解: **A** ／ 難易度: 中級

    **解説:** 登録対象PolicでAの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・登録・管理ク・登録ドメ）です。登録時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・登録・管理ク・登録ドメです。確認対象DIRMCのB:は「DIRMCのノード登録値と取得時刻を記録し、管理クラス未割当を防ぐ」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・確認・ノード・管理クラ）です。通常状態時のManagのC:は「Management Classで通常状態の確認では管理クラスの」を述べ、対象は通常状態の確認 MC01（Manag・通常状・通常状・既定管理）です。Expiを復旧のD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・復旧・ノード・期限切れ）です。Poliを登録という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・登録・管理ク・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0200**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0200について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC08
    確認コード SP81DD0200A
    ```

    画面・出力には SP81DD0200A が表示され、ポリシーと管理クラス Policy Domain 0200 の入力欄確認を確認できます。

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
    Destination DIRPOOL03
    Retain Extra Versions 30
    確認コード SP81DD0200B
    ```

    画面・出力には SP81DD0200B が表示され、ポリシーと管理クラス Policy Domain 0200 の証跡表示確認を確認できます。

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
    確認コード SP81DD0200C
    ```

    画面・出力には SP81DD0200C が表示され、ポリシーと管理クラス Policy Domain 0200 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0200A が画面・出力に表示されること
    ② ステップ2 の SP81DD0200B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0200C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0215 {#c14-i0467}
*分類: ポリシー*  ・  難易度: 中級

金P登録0216ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票金P登録0216です。金P登録0216はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録金P登録0216です。金P登録0216では管理クラス詳細と取得時刻を採取票金P登録0216へ残します。金P登録0216ではコピーグループ未定義を避けるため補助資料も照合する判断金P登録0216です。金P登録0216の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録金P登録0216です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0215を保守記録に説明する必要があります。サーバー日次運用 Database Backup 0292と取り違えない説明はどれですか。

    - A. 仕様上の役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・コピーグループ未定義を防ぐである。 ✅
    - B. 仕様上の役割はDatabase Backupの期限切れ処理と取得時刻を記録し・ノード状態の誤読を防ぐである。サーバー日次運用 Database Backup 0292固有の属性も確認対象に含める。
    - C. 仕様上の役割はDirectory-containeで依存関係の確認ではストレージプールのである。
    - D. 仕様上の役割はEvent Statusのイベント結果と取得時刻を記録し・失敗イベントの見落としを防ぐである。

    正解: **A** ／ 難易度: 中級

    **解説:** 登録対象PolicでAの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・登録・管理ク・コピーグ）です。登録時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・登録・管理ク・コピーグです。抑止対象DatabのB:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・抑止・期限切・ノード状）です。依存関係時のDirecのC:は「Directory-containeで依存関係の確認ではストレージプ」を述べ、対象は依存関係の確認 POOL13（Direc・依存関・依存関・容量使用）です。Evenを棚卸のD:は「Event Statusのイベント結果と取得時刻を記録し」を述べ、対象はEvent Status（Event・棚卸・イベン・失敗イベ）です。Poliを登録という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・登録・管理ク・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0215**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0215について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC05
    確認コード SP81DD0215A
    ```

    画面・出力には SP81DD0215A が表示され、ポリシーと管理クラス Policy Domain 0215 の入力欄確認を確認できます。

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
    Destination DIRPOOL04
    Retain Extra Versions 30
    確認コード SP81DD0215B
    ```

    画面・出力には SP81DD0215B が表示され、ポリシーと管理クラス Policy Domain 0215 の証跡表示確認を確認できます。

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
    確認コード SP81DD0215C
    ```

    画面・出力には SP81DD0215C が表示され、ポリシーと管理クラス Policy Domain 0215 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0215A が画面・出力に表示されること
    ② ステップ2 の SP81DD0215B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0215C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0230 {#c14-i0468}
*分類: ポリシー*  ・  難易度: 上級

紺K確認0231ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紺K確認0231です。紺K確認0231はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録紺K確認0231です。紺K確認0231では管理クラス詳細と取得時刻を採取票紺K確認0231へ残します。紺K確認0231ではDIRMC誤設定を避けるため補助資料も照合する判断紺K確認0231です。紺K確認0231の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録紺K確認0231です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0230の技術的な意味を資料で確認するとき、クライアントスケジュール Action 0306との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はPolicy Domainの管理クラス詳細と取得時刻を記録し・DIRMC誤設定を防ぐである。 ✅
    - B. コマンドまたは機能の用途はActionの開始時刻と取得時刻を記録し・開始時刻誤設定を防ぐである。
    - C. コマンドまたは機能の用途はPolicy Domainで復旧後の確認ではポリシードメインの ノード所属からNodeNameを読みである。
    - D. コマンドまたは機能の用途はNode Nameの運用状態と取得時刻を記録し・ノード状態の誤読を防ぐである。

    正解: **A** ／ 難易度: 上級

    **解説:** 確認対象PolicでAの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・確認・管理ク・ディレク）です。確認時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・確認・管理ク・ディレクです。解析対象ActioのB:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Actio・解析・開始時・開始時刻）です。復旧確認時のPolicのC:は「Policy Domainで復旧後の確認ではポリシードメインの」を述べ、対象は復旧後の確認 DOM06（Polic・復旧確・復旧後・ノードを）です。Nodeを変更のD:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・変更・運用状・ノード状）です。Poliを確認という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・確認・管理ク・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0230**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0230について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード SP81DD0230A
    ```

    画面・出力には SP81DD0230A が表示され、ポリシーと管理クラス Policy Domain 0230 の入力欄確認を確認できます。

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
    確認コード SP81DD0230B
    ```

    画面・出力には SP81DD0230B が表示され、ポリシーと管理クラス Policy Domain 0230 の証跡表示確認を確認できます。

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
    確認コード SP81DD0230C
    ```

    画面・出力には SP81DD0230C が表示され、ポリシーと管理クラス Policy Domain 0230 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0230A が画面・出力に表示されること
    ② ステップ2 の SP81DD0230B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0230C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0245 {#c14-i0469}
*分類: ポリシー*  ・  難易度: 初級

銀F保護0246ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票銀F保護0246です。銀F保護0246はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録銀F保護0246です。銀F保護0246では管理クラス詳細と取得時刻を採取票銀F保護0246へ残します。銀F保護0246では管理クラス未割当を避けるため補助資料も照合する判断銀F保護0246です。銀F保護0246の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録銀F保護0246です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0245について構成や状態を確認します。サーバー日次運用 Expiration Status 0304ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はExpiration Statusのノード登録と取得時刻を記録し・ノード状態の誤読を防ぐである。
    - B. 一次資料が示す主目的はClient Nodeで再始動後の確認ではノード管理の 関連付けからAssociatedNodeを読みである。
    - C. 一次資料が示す主目的はActionの開始時刻と取得時刻を記録し・関連付け漏れを防ぐである。
    - D. 一次資料が示す主目的はPolicy Domainの管理クラス詳細と取得時刻を記録し・管理クラス未割当を防ぐである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 保護対象PolicでDの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・保護・管理ク・管理クラ）です。保護時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・保護・管理ク・管理クラです。Expir・解析のA:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・解析・ノード・ノード状）です。再始動確対象ClienのB:は「Client Nodeで再始動後の確認ではノード管理の」を述べ、対象は再始動後の確認 NODE15（Clien・再始動・再始動・長期未接）です。保守時のActioのC:は「Actionの開始時刻と取得時刻を記録し、関連付け漏れを防ぐ」を述べ、対象はクライアントスケジュール（Actio・保守・開始時・関連付け）です。Poliを保護という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・保護・管理ク・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0245**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0245について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC05
    確認コード SP81DD0245A
    ```

    画面・出力には SP81DD0245A が表示され、ポリシーと管理クラス Policy Domain 0245 の入力欄確認を確認できます。

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
    確認コード SP81DD0245B
    ```

    画面・出力には SP81DD0245B が表示され、ポリシーと管理クラス Policy Domain 0245 の証跡表示確認を確認できます。

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
    確認コード SP81DD0245C
    ```

    画面・出力には SP81DD0245C が表示され、ポリシーと管理クラス Policy Domain 0245 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0245A が画面・出力に表示されること
    ② ステップ2 の SP81DD0245B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0245C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0260 {#c14-i0470}
*分類: ポリシー*  ・  難易度: 初級

蒼A照合0261ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票蒼A照合0261です。蒼A照合0261はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録蒼A照合0261です。蒼A照合0261では管理クラス詳細と取得時刻を採取票蒼A照合0261へ残します。蒼A照合0261では登録ドメインの取り違えを避けるため補助資料も照合する判断蒼A照合0261です。蒼A照合0261の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録蒼A照合0261です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0260の役割を調べています。ポリシーと管理クラス DIRMC 0308の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はDIRMCのノード登録値と取得時刻を記録し・登録ドメインの取り違えを防ぐである。ポリシーと管理クラス DIRMC 0308固有の属性も確認対象に含める。
    - B. 障害切り分けに用いる役割はManagement Classで依存関係の確認では管理クラスのである。
    - C. 障害切り分けに用いる役割はCopy Groupのコピーグループと取得時刻を記録し・DIRMC誤設定を防ぐである。
    - D. 障害切り分けに用いる役割はPolicy Domainの管理クラス詳細と取得時刻を記録し・登録ドメインの取り違えを防ぐである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 照合対象PolicでDの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・照合・管理ク・登録ドメ）です。照合時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・照合・管理ク・登録ドメです。解析対象ノード登録のA:は「DIRMCのノード登録値と取得時刻を記録し」を述べ、対象はポリシーと管理クラス DIRMC（DIRMC・解析・ノード・登録ドメ）です。依存関係対象ManagのB:は「Management Classで依存関係の確認では管理クラスの」を述べ、対象は依存関係の確認 MC13（Manag・依存関・依存関・既定管理）です。変更時のCopyのC:は「Copy Groupのコピーグループと取得時刻を記録し」を述べ、対象はCopy Group（Copy・変更・コピー・ディレク）です。Poliを照合という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・照合・管理ク・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0260**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0260について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード SP81DD0260A
    ```

    画面・出力には SP81DD0260A が表示され、ポリシーと管理クラス Policy Domain 0260 の入力欄確認を確認できます。

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
    Destination DIRPOOL06
    Retain Extra Versions 30
    確認コード SP81DD0260B
    ```

    画面・出力には SP81DD0260B が表示され、ポリシーと管理クラス Policy Domain 0260 の証跡表示確認を確認できます。

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
    確認コード SP81DD0260C
    ```

    画面・出力には SP81DD0260C が表示され、ポリシーと管理クラス Policy Domain 0260 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0260A が画面・出力に表示されること
    ② ステップ2 の SP81DD0260B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0260C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0275 {#c14-i0471}
*分類: ポリシー*  ・  難易度: 中級

金P照合0276ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票金P照合0276です。金P照合0276はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録金P照合0276です。金P照合0276では管理クラス詳細と取得時刻を採取票金P照合0276へ残します。金P照合0276ではコピーグループ未定義を避けるため補助資料も照合する判断金P照合0276です。金P照合0276の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録金P照合0276です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** 「ポリシーと管理クラス Policy Domain 0275」を「クライアントスケジュール Schedule Name 0324」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は照合で管理クラス詳を証跡に残し・Policy Domainの管理クラス詳細と取得時刻を記録し。 ✅
    - B. 仕様上の役割は計画でスケジュールを証跡に残し・Schedule Nameのスケジュール定義と取得時刻を記録。
    - C. 仕様上の役割はログとの照合で照合ではコピを証跡に残し・Backup andでログとの照合ではコピーグループの。
    - D. 仕様上の役割は保守でノード登録を証跡に残し・Expiration Statusのノード登録と取得時刻を記。

    正解: **A** ／ 難易度: 中級

    **解説:** 照合対象PolicでAの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・照合・管理ク・コピーグ）です。照合時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・照合・管理ク・コピーグです。計画対象SchedのB:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Sched・計画・スケジ・日次処理）です。ログとの時のBackuのC:は「Backup andでログとの照合ではコピーグループの」を述べ、対象はログとの照合 CG07（Backu・ログと・照合で・バックア）です。Expiを保守のD:は「Expiration Statusのノード登録と取得時刻を記録し」を述べ、対象はExpiration Status（Expir・保守・ノード・データベ）です。Poliを照合という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・照合・管理ク・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0275**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0275について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC08
    確認コード SP81DD0275A
    ```

    画面・出力には SP81DD0275A が表示され、ポリシーと管理クラス Policy Domain 0275 の入力欄確認を確認できます。

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
    Destination DIRPOOL00
    Retain Extra Versions 30
    確認コード SP81DD0275B
    ```

    画面・出力には SP81DD0275B が表示され、ポリシーと管理クラス Policy Domain 0275 の証跡表示確認を確認できます。

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
    確認コード SP81DD0275C
    ```

    画面・出力には SP81DD0275C が表示され、ポリシーと管理クラス Policy Domain 0275 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0275A が画面・出力に表示されること
    ② ステップ2 の SP81DD0275B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0275C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0290 {#c14-i0472}
*分類: ポリシー*  ・  難易度: 中級

紺K抑止0291ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票紺K抑止0291です。紺K抑止0291はポリシー管理クラスの点検操作でポリシー管理クラスの判定欄を記録する記録紺K抑止0291です。紺K抑止0291では管理クラス詳細と取得時刻を採取票紺K抑止0291へ残します。紺K抑止0291ではDIRMC誤設定を避けるため補助資料も照合する判断紺K抑止0291です。紺K抑止0291の用語整理ではポリシー管理クラスの対象値を実在出力で保管する記録紺K抑止0291です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0290を同一分類のサーバー日次運用 Database Backup 0352と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は解除で期限切れ処理を証跡に残し・Database Backupの期限切れ処理と取得時刻を記録。
    - B. コマンドまたは機能の用途は再始動確認で再始動後の確を証跡に残し・Client Nodeで再始動後の確認ではノード管理の。
    - C. コマンドまたは機能の用途は保守で運用状態を証跡に残し・Node Nameの運用状態と取得時刻を記録し。
    - D. コマンドまたは機能の用途は抑止で管理クラス詳を証跡に残し・Policy Domainの管理クラス詳細と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 抑止対象PolicでDの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・抑止・管理ク・ディレク）です。抑止時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・抑止・管理ク・ディレクです。Datab・解除のA:は「Database Backupの期限切れ処理と取得時刻を記録し」を述べ、対象はDatabase Backup（Datab・解除・期限切・ノード状）です。再始動確対象ClienのB:は「Client Nodeで再始動後の確認ではノード管理の」を述べ、対象は再始動後の確認 NODE15（Clien・再始動・再始動・長期未接）です。保守時のNodeのC:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・保守・運用状・ノード状）です。Poliを抑止という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・抑止・管理ク・ディレク）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0290**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0290について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC05
    確認コード SP81DD0290A
    ```

    画面・出力には SP81DD0290A が表示され、ポリシーと管理クラス Policy Domain 0290 の入力欄確認を確認できます。

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
    Destination DIRPOOL01
    Retain Extra Versions 30
    確認コード SP81DD0290B
    ```

    画面・出力には SP81DD0290B が表示され、ポリシーと管理クラス Policy Domain 0290 の証跡表示確認を確認できます。

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
    確認コード SP81DD0290C
    ```

    画面・出力には SP81DD0290C が表示され、ポリシーと管理クラス Policy Domain 0290 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0290A が画面・出力に表示されること
    ② ステップ2 の SP81DD0290B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0290C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0305 {#c14-i0473}
*分類: ポリシー*  ・  難易度: 中級

銀F解析0306ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票銀F解析0306です。銀F解析0306はポリシー管理クラスの復旧操作でポリシー管理クラスの点検欄を確認する記録銀F解析0306です。銀F解析0306では管理クラス詳細と取得時刻を採取票銀F解析0306へ残します。銀F解析0306では管理クラス未割当を避けるため補助資料も照合する判断銀F解析0306です。銀F解析0306の用語整理ではポリシー管理クラスの対象値を実在出力で点検する記録銀F解析0306です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0305の設定や表示を読む前に役割を確認します。サーバー日次運用 Server Name 0331ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はプール容量不足の見落としを避けるため・採取操作で照合欄を点検するしてデータベースを照合する。
    - B. 一次資料が示す主目的は管理クラス未割当を避けるため・復旧操作で点検欄を確認するして管理クラス詳を照合する。 ✅
    - C. 一次資料が示す主目的はPROTECT STGPOOLとを避けるため・権限境界確認で権限境界の確を確認するして権限境界の確を照合する。
    - D. 一次資料が示す主目的は開始時刻誤設定を避けるため・変更確認操作で採取欄を棚卸するして開始時刻を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 解析対象PolicでBの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・解析・管理ク・管理クラ）です。解析時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・解析・管理ク・管理クラです。Serve・計画のA:は「Server NameのDBバックアップ履歴と取得時刻を記録し」を述べ、対象はServer Name（Serve・計画・データ・プール容）です。権限境界時のStoraのC:は「Storage Poolで権限境界の確認では複製・保護の」を述べ、対象は権限境界の確認 REPL12（Stora・権限境・権限境・PROT）です。Actiを収集のD:は「Actionの開始時刻と取得時刻を記録し、開始時刻誤設定を防ぐ」を述べ、対象はクライアントスケジュール（Actio・収集・開始時・開始時刻）です。Poliを解析という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・解析・管理ク・管理クラ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0305**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0305について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード SP81DD0305A
    ```

    画面・出力には SP81DD0305A が表示され、ポリシーと管理クラス Policy Domain 0305 の入力欄確認を確認できます。

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
    Destination DIRPOOL02
    Retain Extra Versions 30
    確認コード SP81DD0305B
    ```

    画面・出力には SP81DD0305B が表示され、ポリシーと管理クラス Policy Domain 0305 の証跡表示確認を確認できます。

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
    確認コード SP81DD0305C
    ```

    画面・出力には SP81DD0305C が表示され、ポリシーと管理クラス Policy Domain 0305 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0305A が画面・出力に表示されること
    ② ステップ2 の SP81DD0305B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0305C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0320 {#c14-i0474}
*分類: ポリシー*  ・  難易度: 中級

蒼A計画0321ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票蒼A計画0321です。蒼A計画0321はポリシー管理クラスの調査操作でポリシー管理クラスの保守欄を引き継ぎする記録蒼A計画0321です。蒼A計画0321では管理クラス詳細と取得時刻を採取票蒼A計画0321へ残します。蒼A計画0321では登録ドメインの取り違えを避けるため補助資料も照合する判断蒼A計画0321です。蒼A計画0321の用語整理ではポリシー管理クラスの対象値を実在出力で整理する記録蒼A計画0321です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0320に関する障害切り分けの前提を確認しています。schedule 状態確認 復旧手掛かりの機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は復旧手掛かりで復旧手掛かりを証跡に残し・バックアップや管理コマンドを決めた時刻に実行する定義。
    - B. 障害切り分けに用いる役割は変更確認で変更前の確認を証跡に残し・Client Restoreで変更前の確認ではリストア確認の。
    - C. 障害切り分けに用いる役割は登録で運用状態を証跡に残し・Node Nameの運用状態と取得時刻を記録し。
    - D. 障害切り分けに用いる役割は計画で管理クラス詳を証跡に残し・Policy Domainの管理クラス詳細と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 計画対象PolicでDの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・計画・管理ク・登録ドメ）です。計画時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・計画・管理ク・登録ドメです。sched・復旧手掛かのA:は「バックアップや管理コマンドを決めた時刻に実行する定義」を述べ、対象は状態確認 復旧手掛かり（sched・復旧手・復旧手・復旧手掛）です。変更確認対象ClienのB:は「Client Restoreで変更前の確認ではリストア確認の」を述べ、対象は変更前の確認 RST02（Clien・変更確・変更前・置換条件）です。登録時のNodeのC:は「Node Nameの運用状態と取得時刻を記録し」を述べ、対象はNode Name（Node・登録・運用状・ノード状）です。Poliを計画という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・計画・管理ク・登録ドメ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0320**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0320について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC08
    確認コード SP81DD0320A
    ```

    画面・出力には SP81DD0320A が表示され、ポリシーと管理クラス Policy Domain 0320 の入力欄確認を確認できます。

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
    Destination DIRPOOL03
    Retain Extra Versions 30
    確認コード SP81DD0320B
    ```

    画面・出力には SP81DD0320B が表示され、ポリシーと管理クラス Policy Domain 0320 の証跡表示確認を確認できます。

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
    確認コード SP81DD0320C
    ```

    画面・出力には SP81DD0320C が表示され、ポリシーと管理クラス Policy Domain 0320 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0320A が画面・出力に表示されること
    ② ステップ2 の SP81DD0320B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0320C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en



### ポリシーと管理クラス Policy Domain 0335 {#c14-i0475}
*分類: ポリシー*  ・  難易度: 中級

金P計画0336ではIBM Spectrum Protect 8.1 の ポリシーを扱う採取票金P計画0336です。金P計画0336はポリシー管理クラスの表示操作でポリシー管理クラスの対象欄を追跡する記録金P計画0336です。金P計画0336では管理クラス詳細と取得時刻を採取票金P計画0336へ残します。金P計画0336ではコピーグループ未定義を避けるため補助資料も照合する判断金P計画0336です。金P計画0336の用語整理ではポリシー管理クラスの対象値を実在出力で照合する記録金P計画0336です。

**出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en

??? question "確認問題（1問）"
    **問題.** ポリシーと管理クラス Policy Domain 0335を保守記録に説明する必要があります。policy domain 保存期間確認 遅延表示と取り違えない説明はどれですか。

    - A. 仕様上の役割は表示操作で対象欄を追跡することで管理クラス詳を確認し・コピーグループ未定義を防ぐ。 ✅
    - B. 仕様上の役割は遅延表示で遅延表示を確認することで遅延表示を確認し・遅延表示の誤読を防ぐ。
    - C. 仕様上の役割は再始動確認で再始動後の確を確認することで再始動後の確を確認し・データベースバックアップ媒体を防ぐ。
    - D. 仕様上の役割は照合操作で確認欄を採取することでスケジュールを確認し・日次処理順序の誤読を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 計画対象PolicでAの記述「Policy Domainの管理クラス詳細と取得時刻を記録し」に対応する項目はPolicy Domain（Polic・計画・管理ク・コピーグ）です。計画時のPolicに関するポリシーの仕様は「Policy Domainの管理クラス詳細と取得時刻を記録し」で、確認対象はPoli・計画・管理ク・コピーグです。遅延表示対象policのB:は「クライアントに適用するバックアップとアーカイブの規則を束ねる単位」を述べ、対象は保存期間確認 遅延表示（polic・遅延表・遅延表・遅延表示）です。再始動確時のデータベーのC:は「DBで再始動後の確認ではサーバーの 履歴照会からBACKUPFULL」を述べ、対象は再始動後の確認 DBBK15（データベー・再始動・再始動・データベ）です。Scheを登録のD:は「Schedule Nameのスケジュール定義と取得時刻を記録し」を述べ、対象はSchedule Name（Sched・登録・スケジ・日次処理）です。Poliを計画という用語は「Policy Domainの管理クラス詳細と取得時刻」を指し、Policy Domain（Polic・計画・管理ク・コピーグ）に該当します。

    **出典:** SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


??? note "検証手順（1件）"
    **ポリシーと管理クラス Policy Domain 0335**

    - 検証目的: ポリシーと管理クラスのポリシーと管理クラス Policy Domain 0335について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    Management Class MC05
    確認コード SP81DD0335A
    ```

    画面・出力には SP81DD0335A が表示され、ポリシーと管理クラス Policy Domain 0335 の入力欄確認を確認できます。

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
    Destination DIRPOOL04
    Retain Extra Versions 30
    確認コード SP81DD0335B
    ```

    画面・出力には SP81DD0335B が表示され、ポリシーと管理クラス Policy Domain 0335 の証跡表示確認を確認できます。

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
    確認コード SP81DD0335C
    ```

    画面・出力には SP81DD0335C が表示され、ポリシーと管理クラス Policy Domain 0335 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の SP81DD0335A が画面・出力に表示されること
    ② ステップ2 の SP81DD0335B が画面・出力に表示されること
    ③ ステップ3 の SP81DD0335C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: SP_EE_install_aix_en / SP_api_guide_en / SP_BA_client_windows_en / SP_BA_client_msgs_en / SP_server_admin_center_en


