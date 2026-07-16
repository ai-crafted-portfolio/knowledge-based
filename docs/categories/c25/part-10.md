---
search:
  exclude: true
---

# PowerHA SystemMirror 7.2 — 詳細 (10/11)

[← PowerHA SystemMirror 7.2 の概要へ戻る](index.md)


## PowerHA SystemMirror 7.2 > 構成検証

### クラスタ構成検証 Verification Progress 0046 {#c25-i0459}
*分類: 構成検証*  ・  難易度: 中級

紫G復旧0047ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紫G復旧0047です。紫G復旧0047はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紫G復旧0047です。紫G復旧0047ではリソース要約と取得時刻を採取票紫G復旧0047へ残します。紫G復旧0047ではノード間ODM差分の残存を避けるため補助資料も照合する判断紫G復旧0047です。紫G復旧0047の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紫G復旧0047です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0046に関する障害切り分けの前提を確認しています。GLVM地理的ミラー VG STATE 0123の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は診断で基本ソフトAを証跡に残し・地理的ミラーの項目の基本ソフトAIXエラー識別子と取得時刻を。
    - B. 障害切り分けに用いる役割は復旧でリソース要約を証跡に残し・構成検証のリソース要約と取得時刻を記録し。 ✅
    - C. 障害切り分けに用いる役割は照合で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。
    - D. 障害切り分けに用いる役割は依存関係確認でクラスタ照会を証跡に残し・クラスタートポロジーでクラスタ照会から。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能復旧・クラス・リソーでBの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・復旧）です。照合復旧・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・復旧・ノードです。比較クラス・復旧でA:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸は構成検・復旧・リソーです。項目復旧・クラス・リソーでC:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はノード・クラス・リソーです。仕様復旧・クラス・リソーでD:の依存関係の確認 TOPO13は「クラスタートポロジーでクラスタ照会から」を述べるため、正答側の照合軸は復旧・ノード・リソーです。用語復旧・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0046**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0046について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0046A
    ```

    画面・出力には PHA72DD0046A が表示され、クラスタ構成検証 Verification Progress 0046 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0046
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0046B
    ```

    画面・出力には PHA72DD0046B が表示され、クラスタ構成検証 Verification Progress 0046 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0046
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0046C
    ```

    画面・出力には PHA72DD0046C が表示され、クラスタ構成検証 Verification Progress 0046 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0046A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0046B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0046C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0061 {#c25-i0460}
*分類: 構成検証*  ・  難易度: 中級

橙B監査0062ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票橙B監査0062です。橙B監査0062はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録橙B監査0062です。橙B監査0062ではリソース要約と取得時刻を採取票橙B監査0062へ残します。橙B監査0062では未同期構成の見落としを避けるため補助資料も照合する判断橙B監査0062です。橙B監査0062の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録橙B監査0062です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0061を保守記録に説明する必要があります。リソースグループ制御 Resource Group Name 0125と取り違えない説明はどれですか。

    - A. 仕様上の役割は復旧操作で点検欄を確認することで優先ノード一を確認し・資源グループ位置の誤認を防ぐ。
    - B. 仕様上の役割は点検操作で判定欄を記録することで移動履歴を確認し・依存リソース順序の見落としを防ぐ。
    - C. 仕様上の役割はSRC状態からクラスター管理プロセスを読ことでサブシステムを確認し・基本ソフト稼働とクラスタ稼働を防ぐ。
    - D. 仕様上の役割は記録操作で証跡欄を照合することでリソース要約を確認し・未同期構成の見落としを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能監査・クラス・リソーでDの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・監査）です。照合監査・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、未同期構成の見落としを防ぐ」で、確認対象はリソー・監査・未同期です。比較クラス・監査でA:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は構成検・監査・リソーです。運用監査・構成検でB:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸はリソー・クラス・監査です。項目監査・クラス・リソーでC:の性能影響の確認 NODE11は「PowerHA Node Stateでサブシ」を述べるため、正答側の照合軸は未同期・クラス・リソーです。用語監査・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0061**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0061について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0061A
    ```

    画面・出力には PHA72DD0061A が表示され、クラスタ構成検証 Verification Progress 0061 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0061
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0061B
    ```

    画面・出力には PHA72DD0061B が表示され、クラスタ構成検証 Verification Progress 0061 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0061
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0061C
    ```

    画面・出力には PHA72DD0061C が表示され、クラスタ構成検証 Verification Progress 0061 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0061A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0061B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0061C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0076 {#c25-i0461}
*分類: 構成検証*  ・  難易度: 中級

青Q監査0077ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票青Q監査0077です。青Q監査0077はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録青Q監査0077です。青Q監査0077ではリソース要約と取得時刻を採取票青Q監査0077へ残します。青Q監査0077では検証ログの採取漏れを避けるため補助資料も照合する判断青Q監査0077です。青Q監査0077の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録青Q監査0077です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0076の技術的な意味を資料で確認するとき、GLVM地理的ミラー RPV Client 0084との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は監査でリソース要約を証跡に残し・構成検証のリソース要約と取得時刻を記録し。 ✅
    - B. コマンドまたは機能の用途は変更で遠隔ボリューを証跡に残し・地理的ミラーの項目の遠隔ボリュームRPV通信ペアと取得時刻を。
    - C. コマンドまたは機能の用途は解析で基本ソフトAを証跡に残し・地理的ミラーの項目の基本ソフトAIXエラー識別子と取得時刻を。
    - D. コマンドまたは機能の用途は停止確認でマネージャーを証跡に残し・hacmp.out Eventでマネージャーログから。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能監査・クラス・リソーでAの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・監査）です。照合監査・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、検証ログの採取漏れを防ぐ」で、確認対象はリソー・監査・検証ロです。運用監査・構成検でB:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸はリソー・クラス・監査です。項目監査・クラス・リソーでC:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸は検証ロ・クラス・リソーです。仕様監査・クラス・リソーでD:の停止前の確認 FAIL14は「hacmp.out Eventでマネージャー」を述べるため、正答側の照合軸は監査・検証ロ・リソーです。用語監査・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0076**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0076について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0076A
    ```

    画面・出力には PHA72DD0076A が表示され、クラスタ構成検証 Verification Progress 0076 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0076
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0076B
    ```

    画面・出力には PHA72DD0076B が表示され、クラスタ構成検証 Verification Progress 0076 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0076
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0076C
    ```

    画面・出力には PHA72DD0076C が表示され、クラスタ構成検証 Verification Progress 0076 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0076A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0076B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0076C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0091 {#c25-i0462}
*分類: 構成検証*  ・  難易度: 中級

白L変更0092ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票白L変更0092です。白L変更0092はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録白L変更0092です。白L変更0092ではリソース要約と取得時刻を採取票白L変更0092へ残します。白L変更0092では警告と致命エラーの混同を避けるため補助資料も照合する判断白L変更0092です。白L変更0092の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録白L変更0092です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0091について構成や状態を確認します。GLVM地理的ミラー RPV Server 0111ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は地理的ミラーの項目のミラー更新状態と取得時刻を記録し・syslogとhacmp.outの突合漏れを防ぐである。監査操作で記録欄を比較するときはsyslogとhacmp.oを防ぐ。
    - B. 一次資料が示す主目的は構成検証のリソース要約と取得時刻を記録し・警告と致命エラーの混同を防ぐである。採取操作で照合欄を点検するときは警告と致命エラーの混同を防ぐ。 ✅
    - C. 一次資料が示す主目的は獲得処理の獲得イベントと取得時刻を記録し・獲得失敗ログの未採取を防ぐである。表示操作で対象欄を追跡するときは獲得失敗ログの未採取を防ぐ。
    - D. 一次資料が示す主目的はCluster Servicesで資源グループRG確認から app_rg を読み・app_rg とである。RG確認からapp_rgを読むときは管理設定と資源状態の混同を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能変更・クラス・リソーでBの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・変更）です。照合変更・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・変更・警告とです。比較クラス・変更でA:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は構成検・変更・リソーです。項目変更・クラス・リソーでC:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は警告と・クラス・リソーです。仕様変更・クラス・リソーでD:の再始動後の確認 START15は「Cluster Servicesで資源グルー」を述べるため、正答側の照合軸は変更・警告と・リソーです。用語変更・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0091**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0091について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0091A
    ```

    画面・出力には PHA72DD0091A が表示され、クラスタ構成検証 Verification Progress 0091 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0091
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0091B
    ```

    画面・出力には PHA72DD0091B が表示され、クラスタ構成検証 Verification Progress 0091 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0091
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0091C
    ```

    画面・出力には PHA72DD0091C が表示され、クラスタ構成検証 Verification Progress 0091 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0091A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0091B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0091C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0106 {#c25-i0463}
*分類: 構成検証*  ・  難易度: 上級

紫G移行0107ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紫G移行0107です。紫G移行0107はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紫G移行0107です。紫G移行0107ではリソース要約と取得時刻を採取票紫G移行0107へ残します。紫G移行0107ではノード間ODM差分の残存を避けるため補助資料も照合する判断紫G移行0107です。紫G移行0107の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紫G移行0107です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0106の役割を調べています。リソースグループ制御 Node List 0152の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はノード一覧の移動履歴と取得時刻を記録し・自動戻し条件の誤読を防ぐである。調査操作で保守欄を引き継ぎするときは自動戻し条件の誤読を防ぐ。
    - B. 障害切り分けに用いる役割はイベント要約の失敗ラベルと取得時刻を記録し・獲得失敗ログの未採取を防ぐである。表示操作で対象欄を追跡するときは獲得失敗ログの未採取を防ぐ。リソースグループ制御 Event Summary 0323固有の属性も確認対象に含める。
    - C. 障害切り分けに用いる役割は構成検証のリソース要約と取得時刻を記録し・ノード間構成データODM差分の残存を防ぐである。確認操作で状態欄を整理するときはノード間構成データODM差分を防ぐ。 ✅
    - D. 障害切り分けに用いる役割は資源グループの優先ノード一覧と取得時刻を記録し・自動戻し条件の誤読を防ぐである。調査操作で保守欄を引き継ぎするときは自動戻し条件の誤読を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能移行・クラス・リソーでCの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・移行）です。照合移行・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・移行・ノードです。比較クラス・移行でA:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は構成検・移行・リソーです。運用移行・構成検でB:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸はリソー・クラス・移行です。仕様移行・クラス・リソーでD:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は移行・ノード・リソーです。用語移行・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0106**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0106について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0106A
    ```

    画面・出力には PHA72DD0106A が表示され、クラスタ構成検証 Verification Progress 0106 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0106
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0106B
    ```

    画面・出力には PHA72DD0106B が表示され、クラスタ構成検証 Verification Progress 0106 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0106
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0106C
    ```

    画面・出力には PHA72DD0106C が表示され、クラスタ構成検証 Verification Progress 0106 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0106A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0106B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0106C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0121 {#c25-i0464}
*分類: 構成検証*  ・  難易度: 初級

橙B診断0122ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票橙B診断0122です。橙B診断0122はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録橙B診断0122です。橙B診断0122ではリソース要約と取得時刻を採取票橙B診断0122へ残します。橙B診断0122では未同期構成の見落としを避けるため補助資料も照合する判断橙B診断0122です。橙B診断0122の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録橙B診断0122です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 Verification Progress 0121」を「GLVM地理的ミラー RPV Server 0126」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は変更確認操作で採取欄を棚卸することでミラー更新状を確認し・遠隔ボリュームRPV経路断のを防ぐ。
    - B. 仕様上の役割は保守操作で監査欄を保存することで検証報告ROを確認し・検証ログの採取漏れを防ぐ。
    - C. 仕様上の役割は記録操作で証跡欄を照合することでリソース要約を確認し・未同期構成の見落としを防ぐ。 ✅
    - D. 仕様上の役割は表示操作で対象欄を追跡することで獲得イベントを確認し・獲得失敗ログの未採取を防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能診断・クラス・リソーでCの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・診断）です。照合診断・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、未同期構成の見落としを防ぐ」で、確認対象はリソー・診断・未同期です。比較クラス・診断でA:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は構成検・診断・リソーです。運用診断・構成検でB:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸はリソー・クラス・診断です。仕様診断・クラス・リソーでD:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は診断・未同期・リソーです。用語診断・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0121**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0121について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0121A
    ```

    画面・出力には PHA72DD0121A が表示され、クラスタ構成検証 Verification Progress 0121 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0121
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0121B
    ```

    画面・出力には PHA72DD0121B が表示され、クラスタ構成検証 Verification Progress 0121 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0121
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0121C
    ```

    画面・出力には PHA72DD0121C が表示され、クラスタ構成検証 Verification Progress 0121 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0121A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0121B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0121C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0136 {#c25-i0465}
*分類: 構成検証*  ・  難易度: 初級

青Q診断0137ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票青Q診断0137です。青Q診断0137はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録青Q診断0137です。青Q診断0137ではリソース要約と取得時刻を採取票青Q診断0137へ残します。青Q診断0137では検証ログの採取漏れを避けるため補助資料も照合する判断青Q診断0137です。青Q診断0137の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録青Q診断0137です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0136を同一分類のクラスタ構成検証 SMIT Command Status 0199と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は採取操作で照合欄を点検することで検証進行率を確認し・警告と致命エラーの混同を防ぐ。
    - B. コマンドまたは機能の用途は変更確認操作で採取欄を棚卸することでsyslogを確認し・遠隔ボリュームRPV経路断のを防ぐ。
    - C. コマンドまたは機能の用途は保守操作で監査欄を保存することで検証報告ROを確認し・検証ログの採取漏れを防ぐ。
    - D. コマンドまたは機能の用途は保守操作で監査欄を保存することでリソース要約を確認し・検証ログの採取漏れを防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能診断・クラス・リソーでDの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・診断）です。照合診断・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、検証ログの採取漏れを防ぐ」で、確認対象はリソー・診断・検証ロです。比較診断・クラス・リソー・検証ロでA:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸は構成検・診断・リソーです。運用診断・構成検でB:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸はリソー・クラス・診断です。項目診断・クラス・リソーでC:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸は検証ロ・クラス・リソーです。用語診断・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0136**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0136について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0136A
    ```

    画面・出力には PHA72DD0136A が表示され、クラスタ構成検証 Verification Progress 0136 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0136
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0136B
    ```

    画面・出力には PHA72DD0136B が表示され、クラスタ構成検証 Verification Progress 0136 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0136
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0136C
    ```

    画面・出力には PHA72DD0136C が表示され、クラスタ構成検証 Verification Progress 0136 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0136A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0136B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0136C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0151 {#c25-i0466}
*分類: 構成検証*  ・  難易度: 中級

白L保守0152ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票白L保守0152です。白L保守0152はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録白L保守0152です。白L保守0152ではリソース要約と取得時刻を採取票白L保守0152へ残します。白L保守0152では警告と致命エラーの混同を避けるため補助資料も照合する判断白L保守0152です。白L保守0152の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録白L保守0152です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0151の設定や表示を読む前に役割を確認します。GLVM地理的ミラー syslog entry 0177ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は片側VGのvaryon誤操作を避けるため・主操作で出力欄を評価するしてsyslogを照合する。
    - B. 一次資料が示す主目的は監査証跡の誤読を避けるため・監査証跡で監査証跡を確認するして監査証跡を照合する。
    - C. 一次資料が示す主目的は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するしてリソース要約を照合する。 ✅
    - D. 一次資料が示す主目的は資源グループ位置の誤認を避けるため・復旧操作で点検欄を確認するして失敗ラベルを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能保守・クラス・リソーでCの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・保守）です。照合保守・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・保守・警告とです。比較保守・クラス・リソー・警告とでA:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は構成検・保守・リソーです。運用保守・構成検でB:の状態確認 監査証跡は「検証後に構成を同期し、クラスタスナップショッ」を述べるため、正答側の照合軸はリソー・クラス・保守です。仕様保守・クラス・リソーでD:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は保守・警告と・リソーです。用語保守・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0151**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0151について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0151A
    ```

    画面・出力には PHA72DD0151A が表示され、クラスタ構成検証 Verification Progress 0151 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0151
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0151B
    ```

    画面・出力には PHA72DD0151B が表示され、クラスタ構成検証 Verification Progress 0151 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0151
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0151C
    ```

    画面・出力には PHA72DD0151C が表示され、クラスタ構成検証 Verification Progress 0151 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0151A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0151B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0151C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0166 {#c25-i0467}
*分類: 構成検証*  ・  難易度: 中級

紫G切替0167ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紫G切替0167です。紫G切替0167はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紫G切替0167です。紫G切替0167ではリソース要約と取得時刻を採取票紫G切替0167へ残します。紫G切替0167ではノード間ODM差分の残存を避けるため補助資料も照合する判断紫G切替0167です。紫G切替0167の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紫G切替0167です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0166に関する障害切り分けの前提を確認しています。GLVM地理的ミラー VG STATE 0198の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は変更確認操作で採取欄を棚卸することで基本ソフトAを確認し・遠隔ボリュームRPV経路断のを防ぐ。
    - B. 障害切り分けに用いる役割は確認操作で状態欄を整理することでリソース要約を確認し・ノード間構成データODM差分を防ぐ。 ✅
    - C. 障害切り分けに用いる役割は起動確認で時刻情報を確認することで時刻情報を確認し・時刻情報の誤読を防ぐ。
    - D. 障害切り分けに用いる役割は点検操作で判定欄を記録することで移動履歴を確認し・依存リソース順序の見落としを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能切替・クラス・リソーでBの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・切替）です。照合切替・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・切替・ノードです。比較切替・クラス・リソー・ノードでA:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸は構成検・切替・リソーです。項目切替・クラス・リソーでC:の起動確認 時刻情報は「Cluster Manager の状態」を述べるため、正答側の照合軸はノード・クラス・リソーです。仕様切替・クラス・リソーでD:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は切替・ノード・リソーです。用語切替・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0166**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0166について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0166A
    ```

    画面・出力には PHA72DD0166A が表示され、クラスタ構成検証 Verification Progress 0166 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0166
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0166B
    ```

    画面・出力には PHA72DD0166B が表示され、クラスタ構成検証 Verification Progress 0166 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0166
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0166C
    ```

    画面・出力には PHA72DD0166C が表示され、クラスタ構成検証 Verification Progress 0166 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0166A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0166B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0166C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0181 {#c25-i0468}
*分類: 構成検証*  ・  難易度: 中級

橙B収集0182ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票橙B収集0182です。橙B収集0182はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録橙B収集0182です。橙B収集0182ではリソース要約と取得時刻を採取票橙B収集0182へ残します。橙B収集0182では未同期構成の見落としを避けるため補助資料も照合する判断橙B収集0182です。橙B収集0182の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録橙B収集0182です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0181を保守記録に説明する必要があります。クラスタ構成検証 Cluster Topology 0223と取り違えない説明はどれですか。

    - A. 仕様上の役割は採取操作で照合欄を点検することで構成データOを確認し・警告と致命エラーの混同を防ぐ。
    - B. 仕様上の役割は記録操作で証跡欄を照合することでリソース要約を確認し・未同期構成の見落としを防ぐ。 ✅
    - C. 仕様上の役割は所有先確認で依存関係を確認することで依存関係を確認し・依存関係の誤読を防ぐ。
    - D. 仕様上の役割は採取操作で照合欄を点検することでトポロジ要約を確認し・警告と致命エラーの混同を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能収集・クラス・リソーでBの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・収集）です。照合収集・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、未同期構成の見落としを防ぐ」で、確認対象はリソー・収集・未同期です。比較収集・クラス・リソー・未同期でA:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は構成検・収集・リソーです。項目収集・クラス・リソーでC:の所有先確認 依存関係は「クラスタサービスを開始し、リソースグループを」を述べるため、正答側の照合軸は未同期・クラス・リソーです。仕様収集・クラス・リソーでD:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は収集・未同期・リソーです。用語収集・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0181**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0181について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0181A
    ```

    画面・出力には PHA72DD0181A が表示され、クラスタ構成検証 Verification Progress 0181 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0181
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0181B
    ```

    画面・出力には PHA72DD0181B が表示され、クラスタ構成検証 Verification Progress 0181 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0181
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0181C
    ```

    画面・出力には PHA72DD0181C が表示され、クラスタ構成検証 Verification Progress 0181 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0181A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0181B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0181C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0196 {#c25-i0469}
*分類: 構成検証*  ・  難易度: 中級

青Q収集0197ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票青Q収集0197です。青Q収集0197はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録青Q収集0197です。青Q収集0197ではリソース要約と取得時刻を採取票青Q収集0197へ残します。青Q収集0197では検証ログの採取漏れを避けるため補助資料も照合する判断青Q収集0197です。青Q収集0197の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録青Q収集0197です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0196の技術的な意味を資料で確認するとき、GLVM地理的ミラー Mirror Pool 0255との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はsyslogとhacmp.outを避けるため・監査操作で記録欄を比較するしてVG varを照合する。
    - B. コマンドまたは機能の用途は管理設定と資源状態の混同を避けるため・状態確認からST_STABLEを読むして状態確認を照合する。
    - C. コマンドまたは機能の用途は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして移動履歴を照合する。
    - D. コマンドまたは機能の用途は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するしてリソース要約を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能収集・クラス・リソーでDの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・収集）です。照合収集・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、検証ログの採取漏れを防ぐ」で、確認対象はリソー・収集・検証ロです。比較収集・クラス・リソー・検証ロでA:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は構成検・収集・リソーです。運用収集・構成検でB:の変更前の確認 START02は「Cluster Servicesで状態確認か」を述べるため、正答側の照合軸はリソー・クラス・収集です。項目収集・クラス・リソーでC:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は検証ロ・クラス・リソーです。用語収集・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0196**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0196について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0196A
    ```

    画面・出力には PHA72DD0196A が表示され、クラスタ構成検証 Verification Progress 0196 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0196
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0196B
    ```

    画面・出力には PHA72DD0196B が表示され、クラスタ構成検証 Verification Progress 0196 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0196
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0196C
    ```

    画面・出力には PHA72DD0196C が表示され、クラスタ構成検証 Verification Progress 0196 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0196A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0196B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0196C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0211 {#c25-i0470}
*分類: 構成検証*  ・  難易度: 中級

白L登録0212ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票白L登録0212です。白L登録0212はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録白L登録0212です。白L登録0212ではリソース要約と取得時刻を採取票白L登録0212へ残します。白L登録0212では警告と致命エラーの混同を避けるため補助資料も照合する判断白L登録0212です。白L登録0212の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録白L登録0212です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0211について構成や状態を確認します。クラスタ構成検証 clverify.log 0277ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は記録操作で証跡欄を照合することで検証報告ROを確認し・未同期構成の見落としを防ぐ。
    - B. 一次資料が示す主目的は採取操作で照合欄を点検することでリソース要約を確認し・警告と致命エラーの混同を防ぐ。 ✅
    - C. 一次資料が示す主目的はインターフェースから192.0.2.50ことでインターフェを確認し・永続アドレスとサービスアドレを防ぐ。
    - D. 一次資料が示す主目的は復旧操作で点検欄を確認することで獲得イベントを確認し・資源グループ位置の誤認を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能登録・クラス・リソーでBの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・登録）です。照合登録・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・登録・警告とです。比較登録・クラス・リソー・警告とでA:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸は構成検・登録・リソーです。項目登録・クラス・リソーでC:の変更後の確認 SVCIP03は「IP Service IPでインターフェース」を述べるため、正答側の照合軸は警告と・クラス・リソーです。仕様登録・クラス・リソーでD:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は登録・警告と・リソーです。用語登録・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0211**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0211について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0211A
    ```

    画面・出力には PHA72DD0211A が表示され、クラスタ構成検証 Verification Progress 0211 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0211
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0211B
    ```

    画面・出力には PHA72DD0211B が表示され、クラスタ構成検証 Verification Progress 0211 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0211
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0211C
    ```

    画面・出力には PHA72DD0211C が表示され、クラスタ構成検証 Verification Progress 0211 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0211A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0211B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0211C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0226 {#c25-i0471}
*分類: 構成検証*  ・  難易度: 上級

紫G確認0227ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紫G確認0227です。紫G確認0227はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紫G確認0227です。紫G確認0227ではリソース要約と取得時刻を採取票紫G確認0227へ残します。紫G確認0227ではノード間ODM差分の残存を避けるため補助資料も照合する判断紫G確認0227です。紫G確認0227の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紫G確認0227です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0226の役割を調べています。リソースグループ制御 Node List 0272の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして移動履歴を照合する。
    - B. 障害切り分けに用いる役割はcluster historyだを避けるため・主要ログからACQUISITIONを読むして主要ログを照合する。
    - C. 障害切り分けに用いる役割はsyslogとhacmp.outを避けるため・監査操作で記録欄を比較するして基本ソフトAを照合する。
    - D. 障害切り分けに用いる役割はノード間構成データODM差分の残を避けるため・確認操作で状態欄を整理するしてリソース要約を照合する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能確認・クラス・リソーでDの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・確認）です。照合確認・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・確認・ノードです。比較確認・クラス・リソー・ノードでA:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は構成検・確認・リソーです。運用確認・構成検でB:のログとの照合 FAIL07は「hacmp.out Eventで主要ログから」を述べるため、正答側の照合軸はリソー・クラス・確認です。項目確認・クラス・リソーでC:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸はノード・クラス・リソーです。用語確認・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0226**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0226について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0226A
    ```

    画面・出力には PHA72DD0226A が表示され、クラスタ構成検証 Verification Progress 0226 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0226
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0226B
    ```

    画面・出力には PHA72DD0226B が表示され、クラスタ構成検証 Verification Progress 0226 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0226
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0226C
    ```

    画面・出力には PHA72DD0226C が表示され、クラスタ構成検証 Verification Progress 0226 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0226A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0226B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0226C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0241 {#c25-i0472}
*分類: 構成検証*  ・  難易度: 初級

橙B保護0242ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票橙B保護0242です。橙B保護0242はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録橙B保護0242です。橙B保護0242ではリソース要約と取得時刻を採取票橙B保護0242へ残します。橙B保護0242では未同期構成の見落としを避けるため補助資料も照合する判断橙B保護0242です。橙B保護0242の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録橙B保護0242です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 Verification Progress 0241」を「リソースグループ制御 Node List 0272」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はノード一覧の移動履歴と取得時刻を記録し・自動戻し条件の誤読を防ぐである。調査操作で保守欄を引き継ぎするときは自動戻し条件の誤読を防ぐ。
    - B. 仕様上の役割は構成検証のリソース要約と取得時刻を記録し・未同期構成の見落としを防ぐである。記録操作で証跡欄を照合するときは未同期構成の見落としを防ぐ。 ✅
    - C. 仕様上の役割はPowerHA Node Stateでイベント確認から 終了状態 を読み・終了状態 と 実状態値 を照合する。イベント確認から終了状態を読むときは基本ソフト稼働とクラスタ稼働を防ぐ。
    - D. 仕様上の役割は地理的ミラーの項目のsyslog記録と取得時刻を記録し・遠隔ボリュームRPV経路断の見落としを防ぐである。変更確認操作で採取欄を棚卸するときは遠隔ボリュームRPV経路断のを防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能保護・クラス・リソーでBの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・保護）です。照合保護・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、未同期構成の見落としを防ぐ」で、確認対象はリソー・保護・未同期です。比較保護・クラス・リソー・未同期でA:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は構成検・保護・リソーです。項目保護・クラス・リソーでC:の権限境界の確認 NODE12は「PowerHA Node Stateでイベン」を述べるため、正答側の照合軸は未同期・クラス・リソーです。仕様保護・クラス・リソーでD:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は保護・未同期・リソーです。用語保護・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0241**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0241について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0241A
    ```

    画面・出力には PHA72DD0241A が表示され、クラスタ構成検証 Verification Progress 0241 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0241
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0241B
    ```

    画面・出力には PHA72DD0241B が表示され、クラスタ構成検証 Verification Progress 0241 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0241
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0241C
    ```

    画面・出力には PHA72DD0241C が表示され、クラスタ構成検証 Verification Progress 0241 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0241A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0241B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0241C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0256 {#c25-i0473}
*分類: 構成検証*  ・  難易度: 初級

青Q保護0257ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票青Q保護0257です。青Q保護0257はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録青Q保護0257です。青Q保護0257ではリソース要約と取得時刻を採取票青Q保護0257へ残します。青Q保護0257では検証ログの採取漏れを避けるため補助資料も照合する判断青Q保護0257です。青Q保護0257の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録青Q保護0257です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0256を同一分類のGLVM地理的ミラー RPV Client 0309と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は主操作で出力欄を評価することで遠隔ボリューを確認し・片側VGのvaryon誤操作を防ぐ。
    - B. コマンドまたは機能の用途は保守操作で監査欄を保存することでリソース要約を確認し・検証ログの採取漏れを防ぐ。 ✅
    - C. コマンドまたは機能の用途は検証からVerificationを読むことで検証を確認し・片系定義を全体正本とする誤認を防ぐ。
    - D. コマンドまたは機能の用途は監査操作で記録欄を比較することでミラー更新状を確認し・syslogとhacmp.oを防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能保護・クラス・リソーでBの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・保護）です。照合保護・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、検証ログの採取漏れを防ぐ」で、確認対象はリソー・保護・検証ロです。比較保護・クラス・リソー・検証ロでA:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸は構成検・保護・リソーです。項目保護・クラス・リソーでC:の変更後の確認 TOPO03は「クラスタートポロジーで検証から」を述べるため、正答側の照合軸は検証ロ・クラス・リソーです。仕様保護・クラス・リソーでD:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は保護・検証ロ・リソーです。用語保護・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0256**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0256について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0256A
    ```

    画面・出力には PHA72DD0256A が表示され、クラスタ構成検証 Verification Progress 0256 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0256
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0256B
    ```

    画面・出力には PHA72DD0256B が表示され、クラスタ構成検証 Verification Progress 0256 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0256
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0256C
    ```

    画面・出力には PHA72DD0256C が表示され、クラスタ構成検証 Verification Progress 0256 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0256A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0256B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0256C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0271 {#c25-i0474}
*分類: 構成検証*  ・  難易度: 中級

白L照合0272ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票白L照合0272です。白L照合0272はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録白L照合0272です。白L照合0272ではリソース要約と取得時刻を採取票白L照合0272へ残します。白L照合0272では警告と致命エラーの混同を避けるため補助資料も照合する判断白L照合0272です。白L照合0272の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録白L照合0272です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0271の設定や表示を読む前に役割を確認します。クラスタ構成検証 Cluster Topology 0328ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして構成データOを照合する。
    - B. 一次資料が示す主目的はcluster historyだを避けるため・エラー記録からIDENTIFIERを読むしてエラー記録を照合する。
    - C. 一次資料が示す主目的はsyslogとhacmp.outを避けるため・監査操作で記録欄を比較するして基本ソフトAを照合する。
    - D. 一次資料が示す主目的は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するしてリソース要約を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能照合・クラス・リソーでDの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・照合）です。照合照合・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・照合・警告とです。比較照合・クラス・リソー・警告とでA:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は構成検・照合・リソーです。運用照合・構成検でB:の変更後の確認 FAIL03は「hacmp.out Eventでエラー記録か」を述べるため、正答側の照合軸はリソー・クラス・照合です。項目照合・クラス・リソーでC:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸は警告と・クラス・リソーです。用語照合・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0271**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0271について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0271A
    ```

    画面・出力には PHA72DD0271A が表示され、クラスタ構成検証 Verification Progress 0271 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0271
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0271B
    ```

    画面・出力には PHA72DD0271B が表示され、クラスタ構成検証 Verification Progress 0271 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0271
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0271C
    ```

    画面・出力には PHA72DD0271C が表示され、クラスタ構成検証 Verification Progress 0271 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0271A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0271B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0271C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0286 {#c25-i0475}
*分類: 構成検証*  ・  難易度: 中級

紫G抑止0287ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紫G抑止0287です。紫G抑止0287はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紫G抑止0287です。紫G抑止0287ではリソース要約と取得時刻を採取票紫G抑止0287へ残します。紫G抑止0287ではノード間ODM差分の残存を避けるため補助資料も照合する判断紫G抑止0287です。紫G抑止0287の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紫G抑止0287です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0286に関する障害切り分けの前提を確認しています。リソースグループ制御 Online Node 0359の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は解除で資源グループを証跡に残し・オンラインノードの資源グループRG現在位置と取得時刻を記録し。
    - B. 障害切り分けに用いる役割は抑止でリソース要約を証跡に残し・構成検証のリソース要約と取得時刻を記録し。 ✅
    - C. 障害切り分けに用いる役割は停止確認で同期実行を証跡に残し・Cluster Synchronizで同期実行から。
    - D. 障害切り分けに用いる役割は切替で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能抑止・クラス・リソーでBの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・抑止）です。照合抑止・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・抑止・ノードです。比較抑止・クラス・リソー・ノードでA:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は構成検・抑止・リソーです。項目抑止・クラス・リソーでC:の停止前の確認 SYNC14は「Cluster Synchronizで同期実」を述べるため、正答側の照合軸はノード・クラス・リソーです。仕様抑止・クラス・リソーでD:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は抑止・ノード・リソーです。用語抑止・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0286**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0286について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0286A
    ```

    画面・出力には PHA72DD0286A が表示され、クラスタ構成検証 Verification Progress 0286 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0286
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0286B
    ```

    画面・出力には PHA72DD0286B が表示され、クラスタ構成検証 Verification Progress 0286 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0286
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0286C
    ```

    画面・出力には PHA72DD0286C が表示され、クラスタ構成検証 Verification Progress 0286 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0286A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0286B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0286C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0301 {#c25-i0476}
*分類: 構成検証*  ・  難易度: 中級

橙B解析0302ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票橙B解析0302です。橙B解析0302はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録橙B解析0302です。橙B解析0302ではリソース要約と取得時刻を採取票橙B解析0302へ残します。橙B解析0302では未同期構成の見落としを避けるため補助資料も照合する判断橙B解析0302です。橙B解析0302の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録橙B解析0302です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0301を保守記録に説明する必要があります。GLVM地理的ミラー RPV Client 0354と取り違えない説明はどれですか。

    - A. 仕様上の役割は地理的ミラーの項目の遠隔ボリュームRPV通信ペアと取得時刻を記録しである。変更確認操作で採取欄を棚卸するときは遠隔ボリュームRPV経路断のを防ぐ。
    - B. 仕様上の役割はCluster Synchronizで同期実行から clsnapshot を読み・clsnapshot とである。同期実行からclsnapshotを読ときは同期元を誤ると古い定義を全ノを防ぐ。
    - C. 仕様上の役割は地理的ミラーの項目のミラー更新状態と取得時刻を記録し・ミラー再同期条件の誤読を防ぐである。照合操作で確認欄を採取するときはミラー再同期条件の誤読を防ぐ。
    - D. 仕様上の役割は構成検証のリソース要約と取得時刻を記録し・未同期構成の見落としを防ぐである。記録操作で証跡欄を照合するときは未同期構成の見落としを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能解析・クラス・リソーでDの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・解析）です。照合解析・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、未同期構成の見落としを防ぐ」で、確認対象はリソー・解析・未同期です。比較解析・クラス・リソー・未同期でA:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸は構成検・解析・リソーです。運用解析・構成検でB:の構成監査 SYNC08は「Cluster Synchronizで同期実」を述べるため、正答側の照合軸はリソー・クラス・解析です。項目解析・クラス・リソーでC:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は未同期・クラス・リソーです。用語解析・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0301**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0301について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0301A
    ```

    画面・出力には PHA72DD0301A が表示され、クラスタ構成検証 Verification Progress 0301 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0301
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0301B
    ```

    画面・出力には PHA72DD0301B が表示され、クラスタ構成検証 Verification Progress 0301 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0301
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0301C
    ```

    画面・出力には PHA72DD0301C が表示され、クラスタ構成検証 Verification Progress 0301 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0301A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0301B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0301C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0316 {#c25-i0477}
*分類: 構成検証*  ・  難易度: 中級

青Q解析0317ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票青Q解析0317です。青Q解析0317はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録青Q解析0317です。青Q解析0317ではリソース要約と取得時刻を採取票青Q解析0317へ残します。青Q解析0317では検証ログの採取漏れを避けるため補助資料も照合する判断青Q解析0317です。青Q解析0317の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録青Q解析0317です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0316の技術的な意味を資料で確認するとき、clmgr query cluster 版数確認 再開位置との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は版数確認で再開位置を確認することで再開位置を確認し・再開位置の誤読を防ぐ。
    - B. コマンドまたは機能の用途は変更確認操作で採取欄を棚卸することでミラー更新状を確認し・遠隔ボリュームRPV経路断のを防ぐ。
    - C. コマンドまたは機能の用途は点検操作で判定欄を記録することで失敗ラベルを確認し・依存リソース順序の見落としを防ぐ。
    - D. コマンドまたは機能の用途は保守操作で監査欄を保存することでリソース要約を確認し・検証ログの採取漏れを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能解析・クラス・リソーでDの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・解析）です。照合解析・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、検証ログの採取漏れを防ぐ」で、確認対象はリソー・解析・検証ロです。比較解析・クラス・リソー・検証ロでA:の版数確認 再開位置は「クラスタ名、状態、バージョンなどのクラスタ属」を述べるため、正答側の照合軸は構成検・解析・リソーです。運用解析・構成検でB:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸はリソー・クラス・解析です。項目解析・クラス・リソーでC:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は検証ロ・クラス・リソーです。用語解析・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0316**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0316について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0316A
    ```

    画面・出力には PHA72DD0316A が表示され、クラスタ構成検証 Verification Progress 0316 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0316
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0316B
    ```

    画面・出力には PHA72DD0316B が表示され、クラスタ構成検証 Verification Progress 0316 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0316
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0316C
    ```

    画面・出力には PHA72DD0316C が表示され、クラスタ構成検証 Verification Progress 0316 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0316A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0316B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0316C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0331 {#c25-i0478}
*分類: 構成検証*  ・  難易度: 中級

白L計画0332ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票白L計画0332です。白L計画0332はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録白L計画0332です。白L計画0332ではリソース要約と取得時刻を採取票白L計画0332へ残します。白L計画0332では警告と致命エラーの混同を避けるため補助資料も照合する判断白L計画0332です。白L計画0332の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録白L計画0332です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0331について構成や状態を確認します。clmgr sync cluster 版数確認 再読込ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は版数確認で再読込を確認することで再読込を確認し・再読込の誤読を防ぐ。
    - B. 一次資料が示す主目的は変更確認操作で採取欄を棚卸することでミラー更新状を確認し・遠隔ボリュームRPV経路断のを防ぐ。
    - C. 一次資料が示す主目的は採取操作で照合欄を点検することでリソース要約を確認し・警告と致命エラーの混同を防ぐ。 ✅
    - D. 一次資料が示す主目的は表示操作で対象欄を追跡することで資源グループを確認し・獲得失敗ログの未採取を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能計画・クラス・リソーでCの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・計画）です。照合計画・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・計画・警告とです。比較計画・クラス・リソー・警告とでA:の版数確認 再読込は「検証後に構成を同期し、クラスタスナップショッ」を述べるため、正答側の照合軸は構成検・計画・リソーです。運用計画・構成検でB:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸はリソー・クラス・計画です。仕様計画・クラス・リソーでD:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は計画・警告と・リソーです。用語計画・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0331**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0331について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0331A
    ```

    画面・出力には PHA72DD0331A が表示され、クラスタ構成検証 Verification Progress 0331 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0331
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0331B
    ```

    画面・出力には PHA72DD0331B が表示され、クラスタ構成検証 Verification Progress 0331 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0331
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0331C
    ```

    画面・出力には PHA72DD0331C が表示され、クラスタ構成検証 Verification Progress 0331 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0331A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0331B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0331C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0346 {#c25-i0479}
*分類: 構成検証*  ・  難易度: 上級

紫G解除0347ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紫G解除0347です。紫G解除0347はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紫G解除0347です。紫G解除0347ではリソース要約と取得時刻を採取票紫G解除0347へ残します。紫G解除0347ではノード間ODM差分の残存を避けるため補助資料も照合する判断紫G解除0347です。紫G解除0347の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紫G解除0347です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0346の役割を調べています。clmgr sync cluster 同期確認 ログ採取の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は構成検証のリソース要約と取得時刻を記録し・ノード間構成データODM差分の残存を防ぐである。確認操作で状態欄を整理するときはノード間構成データODM差分を防ぐ。 ✅
    - B. 障害切り分けに用いる役割は検証後に構成を同期し・クラスタスナップショットを作成する操作を同期確認する。ログ採取でログ採取を確認するときはログ採取の誤読を防ぐ。
    - C. 障害切り分けに用いる役割は資源グループで依存照会から START_AFTER を読み・START_AFTER とである。依存照会からSTART_AFTERをときは依存順を無視して子資源を先にを防ぐ。
    - D. 障害切り分けに用いる役割は資源グループの優先ノード一覧と取得時刻を記録し・自動戻し条件の誤読を防ぐである。調査操作で保守欄を引き継ぎするときは自動戻し条件の誤読を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能解除・クラス・リソーでAの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・解除）です。照合解除・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・解除・ノードです。運用解除・構成検でB:の同期確認 ログ採取は「検証後に構成を同期し、クラスタスナップショッ」を述べるため、正答側の照合軸はリソー・クラス・解除です。項目解除・クラス・リソーでC:の通常状態の確認 DEP01は「資源グループで依存照会から」を述べるため、正答側の照合軸はノード・クラス・リソーです。仕様解除・クラス・リソーでD:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は解除・ノード・リソーです。用語解除・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0346**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0346について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Verification Progress と リソース要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0346A
    ```

    画面・出力には PHA72DD0346A が表示され、クラスタ構成検証 Verification Progress 0346 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0346
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0346B
    ```

    画面・出力には PHA72DD0346B が表示され、クラスタ構成検証 Verification Progress 0346 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Verification Progress を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0346
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0346C
    ```

    画面・出力には PHA72DD0346C が表示され、クラスタ構成検証 Verification Progress 0346 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0346A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0346B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0346C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0007 {#c25-i0480}
*分類: 構成検証*  ・  難易度: 初級

茶H巡回0008ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票茶H巡回0008です。茶H巡回0008はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録茶H巡回0008です。茶H巡回0008ではROHAレポートと取得時刻を採取票茶H巡回0008へ残します。茶H巡回0008では警告と致命エラーの混同を避けるため補助資料も照合する判断茶H巡回0008です。茶H巡回0008の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録茶H巡回0008です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0007の設定や表示を読む前に役割を確認します。クラスタ構成検証 SMIT Command Status 0034ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はノード間構成データODM差分の残を避けるため・確認操作で状態欄を整理するして検証進行率を照合する。
    - B. 一次資料が示す主目的は片側VGのvaryon誤操作を避けるため・主操作で出力欄を評価するして遠隔ボリューを照合する。
    - C. 一次資料が示す主目的は永続アドレスとサービスアドレスのを避けるため・RG位置からオンライン表示を読むして資源グループを照合する。
    - D. 一次資料が示す主目的は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するして検証報告ROを照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能巡回・クラス・検証報でDの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・巡回）です。照合巡回・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・巡回・警告とです。比較クラス・巡回でA:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はclv・巡回・検証報です。運用巡回・clvでB:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸は検証報・クラス・巡回です。項目巡回・クラス・検証報でC:の停止前の確認 SVCIP14は「IP Service IPで資源グループ位置」を述べるため、正答側の照合軸は警告と・クラス・検証報です。用語巡回・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0007**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0007について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0007A
    ```

    画面・出力には PHA72DD0007A が表示され、クラスタ構成検証 clverify.log 0007 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0007
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0007B
    ```

    画面・出力には PHA72DD0007B が表示され、クラスタ構成検証 clverify.log 0007 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0007
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0007C
    ```

    画面・出力には PHA72DD0007C が表示され、クラスタ構成検証 clverify.log 0007 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0007A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0007B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0007C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0022 {#c25-i0481}
*分類: 構成検証*  ・  難易度: 初級

緑C棚卸0023ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票緑C棚卸0023です。緑C棚卸0023はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録緑C棚卸0023です。緑C棚卸0023ではROHAレポートと取得時刻を採取票緑C棚卸0023へ残します。緑C棚卸0023ではノード間ODM差分の残存を避けるため補助資料も照合する判断緑C棚卸0023です。緑C棚卸0023の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録緑C棚卸0023です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0022に関する障害切り分けの前提を確認しています。リソースグループ制御 Online Node 0119の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は獲得失敗ログの未採取を避けるため・表示操作で対象欄を追跡するして資源グループを照合する。
    - B. 障害切り分けに用いる役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして検証進行率を照合する。
    - C. 障害切り分けに用いる役割はノード間構成データODM差分の残を避けるため・確認操作で状態欄を整理するして検証報告ROを照合する。 ✅
    - D. 障害切り分けに用いる役割は復旧手掛かりの誤読を避けるため・復旧手掛かりで復旧手掛かりを確認するして復旧手掛かりを照合する。clmgr start cluster 版数確認 復旧手掛かり固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能棚卸・クラス・検証報でCの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・棚卸）です。照合棚卸・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・棚卸・ノードです。比較クラス・棚卸でA:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸はclv・棚卸・検証報です。運用棚卸・clvでB:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸は検証報・クラス・棚卸です。仕様棚卸・クラス・検証報でD:の版数確認 復旧手掛かりは「クラスタサービスを開始し、リソースグループを」を述べるため、正答側の照合軸は棚卸・ノード・検証報です。用語棚卸・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0022**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0022について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0022A
    ```

    画面・出力には PHA72DD0022A が表示され、クラスタ構成検証 clverify.log 0022 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0022
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0022B
    ```

    画面・出力には PHA72DD0022B が表示され、クラスタ構成検証 clverify.log 0022 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0022
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0022C
    ```

    画面・出力には PHA72DD0022C が表示され、クラスタ構成検証 clverify.log 0022 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0022A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0022B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0022C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0037 {#c25-i0482}
*分類: 構成検証*  ・  難易度: 中級

藤R棚卸0038ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藤R棚卸0038です。藤R棚卸0038はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録藤R棚卸0038です。藤R棚卸0038ではROHAレポートと取得時刻を採取票藤R棚卸0038へ残します。藤R棚卸0038では未同期構成の見落としを避けるため補助資料も照合する判断藤R棚卸0038です。藤R棚卸0038の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録藤R棚卸0038です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0037を保守記録に説明する必要があります。クラスタ構成検証 Cluster Topology 0088と取り違えない説明はどれですか。

    - A. 仕様上の役割は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして構成データOを照合する。
    - B. 仕様上の役割は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして獲得イベントを照合する。
    - C. 仕様上の役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして検証報告ROを照合する。 ✅
    - D. 仕様上の役割は永続アドレスとサービスアドレスのを避けるため・インターフェースから192.0.2.50してインターフェを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能棚卸・クラス・検証報でCの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・棚卸）です。照合棚卸・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・棚卸・未同期です。比較クラス・棚卸でA:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸はclv・棚卸・検証報です。運用棚卸・clvでB:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は検証報・クラス・棚卸です。仕様棚卸・クラス・検証報でD:の権限境界の確認 SVCIP12は「IP Service IPでインターフェース」を述べるため、正答側の照合軸は棚卸・未同期・検証報です。用語棚卸・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0037**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0037について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0037A
    ```

    画面・出力には PHA72DD0037A が表示され、クラスタ構成検証 clverify.log 0037 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0037
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0037B
    ```

    画面・出力には PHA72DD0037B が表示され、クラスタ構成検証 clverify.log 0037 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0037
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0037C
    ```

    画面・出力には PHA72DD0037C が表示され、クラスタ構成検証 clverify.log 0037 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0037A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0037B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0037C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0052 {#c25-i0483}
*分類: 構成検証*  ・  難易度: 中級

桃M復旧0053ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票桃M復旧0053です。桃M復旧0053はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録桃M復旧0053です。桃M復旧0053ではROHAレポートと取得時刻を採取票桃M復旧0053へ残します。桃M復旧0053では検証ログの採取漏れを避けるため補助資料も照合する判断桃M復旧0053です。桃M復旧0053の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録桃M復旧0053です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0052の技術的な意味を資料で確認するとき、リソースグループ制御 Event Summary 0083との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は獲得失敗ログの未採取を避けるため・表示操作で対象欄を追跡するして失敗ラベルを照合する。
    - B. コマンドまたは機能の用途はノード間構成データODM差分の残を避けるため・確認操作で状態欄を整理するしてリソース要約を照合する。
    - C. コマンドまたは機能の用途は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして検証報告ROを照合する。 ✅
    - D. コマンドまたは機能の用途は管理設定と資源状態の混同を避けるため・RG確認からapp_rgを読むして資源グループを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能復旧・クラス・検証報でCの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・復旧）です。照合復旧・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・復旧・検証ロです。比較クラス・復旧でA:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸はclv・復旧・検証報です。運用復旧・clvでB:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸は検証報・クラス・復旧です。仕様復旧・クラス・検証報でD:の再始動後の確認 START15は「Cluster Servicesで資源グルー」を述べるため、正答側の照合軸は復旧・検証ロ・検証報です。用語復旧・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0052**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0052について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0052A
    ```

    画面・出力には PHA72DD0052A が表示され、クラスタ構成検証 clverify.log 0052 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0052
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0052B
    ```

    画面・出力には PHA72DD0052B が表示され、クラスタ構成検証 clverify.log 0052 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0052
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0052C
    ```

    画面・出力には PHA72DD0052C が表示され、クラスタ構成検証 clverify.log 0052 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0052A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0052B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0052C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0067 {#c25-i0484}
*分類: 構成検証*  ・  難易度: 中級

茶H監査0068ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票茶H監査0068です。茶H監査0068はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録茶H監査0068です。茶H監査0068ではROHAレポートと取得時刻を採取票茶H監査0068へ残します。茶H監査0068では警告と致命エラーの混同を避けるため補助資料も照合する判断茶H監査0068です。茶H監査0068の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録茶H監査0068です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0067について構成や状態を確認します。クラスタ構成検証 Cluster Resources 0115ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は採取操作で照合欄を点検することで検証報告ROを確認し・警告と致命エラーの混同を防ぐ。 ✅
    - B. 一次資料が示す主目的は採取操作で照合欄を点検することでトポロジ要約を確認し・警告と致命エラーの混同を防ぐ。
    - C. 一次資料が示す主目的は表示操作で対象欄を追跡することで獲得イベントを確認し・獲得失敗ログの未採取を防ぐ。
    - D. 一次資料が示す主目的はclinfoES状態からclinfoESことでclinfoを確認し・監視通信SNMP情報の残留をを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能監査・クラス・検証報でAの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・監査）です。照合監査・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・監査・警告とです。運用監査・clvでB:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は検証報・クラス・監査です。項目監査・クラス・検証報でC:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は警告と・クラス・検証報です。仕様監査・クラス・検証報でD:の依存関係の確認 CLSTAT13は「clstatでclinfoES状態から」を述べるため、正答側の照合軸は監査・警告と・検証報です。用語監査・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0067**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0067について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0067A
    ```

    画面・出力には PHA72DD0067A が表示され、クラスタ構成検証 clverify.log 0067 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0067
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0067B
    ```

    画面・出力には PHA72DD0067B が表示され、クラスタ構成検証 clverify.log 0067 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0067
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0067C
    ```

    画面・出力には PHA72DD0067C が表示され、クラスタ構成検証 clverify.log 0067 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0067A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0067B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0067C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0082 {#c25-i0485}
*分類: 構成検証*  ・  難易度: 中級

緑C変更0083ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票緑C変更0083です。緑C変更0083はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録緑C変更0083です。緑C変更0083ではROHAレポートと取得時刻を採取票緑C変更0083へ残します。緑C変更0083ではノード間ODM差分の残存を避けるため補助資料も照合する判断緑C変更0083です。緑C変更0083の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録緑C変更0083です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0082の役割を調べています。リソースグループ制御 Event Summary 0158の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は変更で検証報告ROを証跡に残し・clverify.logの検証報告ROHAレポートと取得時刻。 ✅
    - B. 障害切り分けに用いる役割は保守で失敗ラベルを証跡に残し・イベント要約の失敗ラベルと取得時刻を記録し。
    - C. 障害切り分けに用いる役割は計画でミラー更新状を証跡に残し・地理的ミラーの項目のミラー更新状態と取得時刻を記録し。
    - D. 障害切り分けに用いる役割は通常状態確認で依存照会を証跡に残し・資源グループで依存照会から START_AFTER を読み。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能変更・クラス・検証報でAの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・変更）です。照合変更・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・変更・ノードです。運用変更・clvでB:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は検証報・クラス・変更です。項目変更・クラス・検証報でC:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸はノード・クラス・検証報です。仕様変更・クラス・検証報でD:の通常状態の確認 DEP01は「資源グループで依存照会から」を述べるため、正答側の照合軸は変更・ノード・検証報です。用語変更・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0082**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0082について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0082A
    ```

    画面・出力には PHA72DD0082A が表示され、クラスタ構成検証 clverify.log 0082 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0082
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0082B
    ```

    画面・出力には PHA72DD0082B が表示され、クラスタ構成検証 clverify.log 0082 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0082
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0082C
    ```

    画面・出力には PHA72DD0082C が表示され、クラスタ構成検証 clverify.log 0082 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0082A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0082B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0082C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0097 {#c25-i0486}
*分類: 構成検証*  ・  難易度: 中級

藤R変更0098ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藤R変更0098です。藤R変更0098はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録藤R変更0098です。藤R変更0098ではROHAレポートと取得時刻を採取票藤R変更0098へ残します。藤R変更0098では未同期構成の見落としを避けるため補助資料も照合する判断藤R変更0098です。藤R変更0098の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録藤R変更0098です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 clverify.log 0097」を「GLVM地理的ミラー syslog entry 0147」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はsyslogとhacmp.outを避けるため・監査操作で記録欄を比較するしてsyslogを照合する。
    - B. 仕様上の役割は獲得失敗ログの未採取を避けるため・表示操作で対象欄を追跡するして優先ノード一を照合する。
    - C. 仕様上の役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして検証報告ROを照合する。 ✅
    - D. 仕様上の役割は依存順を無視して子資源を先にオンを避けるため・イベント順序からcompletedを読むしてイベント順序を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能変更・クラス・検証報でCの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・変更）です。照合変更・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・変更・未同期です。比較クラス・変更でA:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸はclv・変更・検証報です。運用変更・clvでB:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は検証報・クラス・変更です。仕様変更・クラス・検証報でD:の復旧後の確認 DEP06は「資源グループでイベント順序から」を述べるため、正答側の照合軸は変更・未同期・検証報です。用語変更・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0097**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0097について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0097A
    ```

    画面・出力には PHA72DD0097A が表示され、クラスタ構成検証 clverify.log 0097 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0097
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0097B
    ```

    画面・出力には PHA72DD0097B が表示され、クラスタ構成検証 clverify.log 0097 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0097
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0097C
    ```

    画面・出力には PHA72DD0097C が表示され、クラスタ構成検証 clverify.log 0097 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0097A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0097B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0097C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0112 {#c25-i0487}
*分類: 構成検証*  ・  難易度: 上級

桃M移行0113ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票桃M移行0113です。桃M移行0113はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録桃M移行0113です。桃M移行0113ではROHAレポートと取得時刻を採取票桃M移行0113へ残します。桃M移行0113では検証ログの採取漏れを避けるため補助資料も照合する判断桃M移行0113です。桃M移行0113の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録桃M移行0113です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0112を同一分類のクラスタ構成検証 Verification Progress 0196と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は収集でリソース要約を証跡に残し・構成検証のリソース要約と取得時刻を記録し。
    - B. コマンドまたは機能の用途は移行で検証報告ROを証跡に残し・clverify.logの検証報告ROHAレポートと取得時刻。 ✅
    - C. コマンドまたは機能の用途は抑止で失敗ラベルを証跡に残し・イベント要約の失敗ラベルと取得時刻を記録し。
    - D. コマンドまたは機能の用途は通常状態確認でclinfoを証跡に残し・clstatでclinfoES状態から clinfoES。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能移行・クラス・検証報でBの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・移行）です。照合移行・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・移行・検証ロです。比較クラス・移行でA:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸はclv・移行・検証報です。項目移行・クラス・検証報でC:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は検証ロ・クラス・検証報です。仕様移行・クラス・検証報でD:の通常状態の確認 CLSTAT01は「clstatでclinfoES状態から」を述べるため、正答側の照合軸は移行・検証ロ・検証報です。用語移行・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0112**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0112について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0112A
    ```

    画面・出力には PHA72DD0112A が表示され、クラスタ構成検証 clverify.log 0112 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0112
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0112B
    ```

    画面・出力には PHA72DD0112B が表示され、クラスタ構成検証 clverify.log 0112 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0112
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0112C
    ```

    画面・出力には PHA72DD0112C が表示され、クラスタ構成検証 clverify.log 0112 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0112A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0112B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0112C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0127 {#c25-i0488}
*分類: 構成検証*  ・  難易度: 初級

茶H診断0128ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票茶H診断0128です。茶H診断0128はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録茶H診断0128です。茶H診断0128ではROHAレポートと取得時刻を採取票茶H診断0128へ残します。茶H診断0128では警告と致命エラーの混同を避けるため補助資料も照合する判断茶H診断0128です。茶H診断0128の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録茶H診断0128です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0127の設定や表示を読む前に役割を確認します。クラスタ構成検証 Cluster Resources 0160ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は保守操作で監査欄を保存することでトポロジ要約を確認し・検証ログの採取漏れを防ぐ。
    - B. 一次資料が示す主目的は保守操作で監査欄を保存することで構成データOを確認し・検証ログの採取漏れを防ぐ。
    - C. 一次資料が示す主目的はclinfoES状態からclinfoESことでclinfoを確認し・監視通信SNMP情報の残留をを防ぐ。
    - D. 一次資料が示す主目的は採取操作で照合欄を点検することで検証報告ROを確認し・警告と致命エラーの混同を防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能診断・クラス・検証報でDの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・診断）です。照合診断・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・診断・警告とです。比較クラス・診断でA:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸はclv・診断・検証報です。運用診断・clvでB:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は検証報・クラス・診断です。項目診断・クラス・検証報でC:のログとの照合 CLSTAT07は「clstatでclinfoES状態から」を述べるため、正答側の照合軸は警告と・クラス・検証報です。用語診断・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0127**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0127について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0127A
    ```

    画面・出力には PHA72DD0127A が表示され、クラスタ構成検証 clverify.log 0127 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0127
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0127B
    ```

    画面・出力には PHA72DD0127B が表示され、クラスタ構成検証 clverify.log 0127 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0127
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0127C
    ```

    画面・出力には PHA72DD0127C が表示され、クラスタ構成検証 clverify.log 0127 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0127A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0127B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0127C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0142 {#c25-i0489}
*分類: 構成検証*  ・  難易度: 初級

緑C保守0143ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票緑C保守0143です。緑C保守0143はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録緑C保守0143です。緑C保守0143ではROHAレポートと取得時刻を採取票緑C保守0143へ残します。緑C保守0143ではノード間ODM差分の残存を避けるため補助資料も照合する判断緑C保守0143です。緑C保守0143の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録緑C保守0143です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0142に関する障害切り分けの前提を確認しています。GLVM地理的ミラー syslog entry 0207の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は保守で検証報告ROを証跡に残し・clverify.logの検証報告ROHAレポートと取得時刻。 ✅
    - B. 障害切り分けに用いる役割は登録でsyslogを証跡に残し・地理的ミラーの項目のsyslog記録と取得時刻を記録し。
    - C. 障害切り分けに用いる役割は解除でVG varを証跡に残し・地理的ミラーの項目のVG vary状態と取得時刻を記録し。
    - D. 障害切り分けに用いる役割はログとの照合で依存照会を証跡に残し・資源グループで依存照会から START_AFTER を読み。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能保守・クラス・検証報でAの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・保守）です。照合保守・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・保守・ノードです。運用保守・clvでB:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は検証報・クラス・保守です。項目保守・クラス・検証報でC:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸はノード・クラス・検証報です。仕様保守・クラス・検証報でD:のログとの照合 DEP07は「資源グループで依存照会から」を述べるため、正答側の照合軸は保守・ノード・検証報です。用語保守・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0142**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0142について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0142A
    ```

    画面・出力には PHA72DD0142A が表示され、クラスタ構成検証 clverify.log 0142 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0142
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0142B
    ```

    画面・出力には PHA72DD0142B が表示され、クラスタ構成検証 clverify.log 0142 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0142
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0142C
    ```

    画面・出力には PHA72DD0142C が表示され、クラスタ構成検証 clverify.log 0142 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0142A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0142B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0142C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0157 {#c25-i0490}
*分類: 構成検証*  ・  難易度: 中級

藤R保守0158ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藤R保守0158です。藤R保守0158はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録藤R保守0158です。藤R保守0158ではROHAレポートと取得時刻を採取票藤R保守0158へ残します。藤R保守0158では未同期構成の見落としを避けるため補助資料も照合する判断藤R保守0158です。藤R保守0158の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録藤R保守0158です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0157を保守記録に説明する必要があります。リソースグループ制御 Acquisition Failure 0221と取り違えない説明はどれですか。

    - A. 仕様上の役割は獲得処理の獲得イベントと取得時刻を記録し・資源グループ位置の誤認を防ぐである。復旧操作で点検欄を確認するときは資源グループ位置の誤認を防ぐ。
    - B. 仕様上の役割はクラスタ構成と状態をスナップショットとして表示するコマンドである。整合確認で整合確認を確認するときは整合確認の誤読を防ぐ。cldump 状態確認 整合確認固有の属性も確認対象に含める。
    - C. 仕様上の役割はclverify.logの検証報告ROHAレポートと取得時刻を記録し・未同期構成の見落としを防ぐである。記録操作で証跡欄を照合するときは未同期構成の見落としを防ぐ。 ✅
    - D. 仕様上の役割は地理的ミラーの項目のVG vary状態と取得時刻を記録し・ミラー再同期条件の誤読を防ぐである。照合操作で確認欄を採取するときはミラー再同期条件の誤読を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能保守・クラス・検証報でCの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・保守）です。照合保守・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・保守・未同期です。比較保守・クラス・検証報・未同期でA:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸はclv・保守・検証報です。運用保守・clvでB:の状態確認 整合確認は「クラスタ構成と状態をスナップショットとして表」を述べるため、正答側の照合軸は検証報・クラス・保守です。仕様保守・クラス・検証報でD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は保守・未同期・検証報です。用語保守・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0157**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0157について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0157A
    ```

    画面・出力には PHA72DD0157A が表示され、クラスタ構成検証 clverify.log 0157 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0157
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0157B
    ```

    画面・出力には PHA72DD0157B が表示され、クラスタ構成検証 clverify.log 0157 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0157
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0157C
    ```

    画面・出力には PHA72DD0157C が表示され、クラスタ構成検証 clverify.log 0157 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0157A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0157B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0157C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0172 {#c25-i0491}
*分類: 構成検証*  ・  難易度: 中級

桃M切替0173ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票桃M切替0173です。桃M切替0173はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録桃M切替0173です。桃M切替0173ではROHAレポートと取得時刻を採取票桃M切替0173へ残します。桃M切替0173では検証ログの採取漏れを避けるため補助資料も照合する判断桃M切替0173です。桃M切替0173の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録桃M切替0173です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0172の技術的な意味を資料で確認するとき、GLVM地理的ミラー VG STATE 0228との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は照合操作で確認欄を採取することで基本ソフトAを確認し・ミラー再同期条件の誤読を防ぐ。
    - B. コマンドまたは機能の用途は整合確認で整合確認を確認することで整合確認を確認し・整合確認の誤読を防ぐ。
    - C. コマンドまたは機能の用途は表示操作で対象欄を追跡することで獲得イベントを確認し・獲得失敗ログの未採取を防ぐ。
    - D. コマンドまたは機能の用途は保守操作で監査欄を保存することで検証報告ROを確認し・検証ログの採取漏れを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能切替・クラス・検証報でDの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・切替）です。照合切替・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・切替・検証ロです。比較切替・クラス・検証報・検証ロでA:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸はclv・切替・検証報です。運用切替・clvでB:の状態確認 整合確認は「クラスタ構成と状態をスナップショットとして表」を述べるため、正答側の照合軸は検証報・クラス・切替です。項目切替・クラス・検証報でC:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は検証ロ・クラス・検証報です。用語切替・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0172**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0172について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0172A
    ```

    画面・出力には PHA72DD0172A が表示され、クラスタ構成検証 clverify.log 0172 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0172
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0172B
    ```

    画面・出力には PHA72DD0172B が表示され、クラスタ構成検証 clverify.log 0172 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0172
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0172C
    ```

    画面・出力には PHA72DD0172C が表示され、クラスタ構成検証 clverify.log 0172 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0172A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0172B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0172C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0187 {#c25-i0492}
*分類: 構成検証*  ・  難易度: 中級

茶H収集0188ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票茶H収集0188です。茶H収集0188はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録茶H収集0188です。茶H収集0188ではROHAレポートと取得時刻を採取票茶H収集0188へ残します。茶H収集0188では警告と致命エラーの混同を避けるため補助資料も照合する判断茶H収集0188です。茶H収集0188の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録茶H収集0188です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0187について構成や状態を確認します。リソースグループ制御 Node List 0242ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は点検操作で判定欄を記録することで移動履歴を確認し・依存リソース順序の見落としを防ぐ。
    - B. 一次資料が示す主目的はIP資源照会からアドレスを読むことでサービスアドを確認し・永続アドレスとサービスアドレを防ぐ。
    - C. 一次資料が示す主目的は点検操作で判定欄を記録することで資源グループを確認し・依存リソース順序の見落としを防ぐ。
    - D. 一次資料が示す主目的は採取操作で照合欄を点検することで検証報告ROを確認し・警告と致命エラーの混同を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能収集・クラス・検証報でDの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・収集）です。照合収集・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・収集・警告とです。比較収集・クラス・検証報・警告とでA:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸はclv・収集・検証報です。運用収集・clvでB:のログとの照合 SVCIP07は「IP Service IPでサービスアドレス」を述べるため、正答側の照合軸は検証報・クラス・収集です。項目収集・クラス・検証報でC:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は警告と・クラス・検証報です。用語収集・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0187**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0187について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0187A
    ```

    画面・出力には PHA72DD0187A が表示され、クラスタ構成検証 clverify.log 0187 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0187
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0187B
    ```

    画面・出力には PHA72DD0187B が表示され、クラスタ構成検証 clverify.log 0187 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0187
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0187C
    ```

    画面・出力には PHA72DD0187C が表示され、クラスタ構成検証 clverify.log 0187 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0187A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0187B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0187C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0202 {#c25-i0493}
*分類: 構成検証*  ・  難易度: 中級

緑C登録0203ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票緑C登録0203です。緑C登録0203はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録緑C登録0203です。緑C登録0203ではROHAレポートと取得時刻を採取票緑C登録0203へ残します。緑C登録0203ではノード間ODM差分の残存を避けるため補助資料も照合する判断緑C登録0203です。緑C登録0203の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録緑C登録0203です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0202の役割を調べています。リソースグループ制御 Online Node 0224の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は調査操作で保守欄を引き継ぎすることで資源グループを確認し・自動戻し条件の誤読を防ぐ。
    - B. 障害切り分けに用いる役割は整合確認で起動順序を確認することで起動順序を確認し・起動順序の誤読を防ぐ。
    - C. 障害切り分けに用いる役割は点検操作で判定欄を記録することで失敗ラベルを確認し・依存リソース順序の見落としを防ぐ。リソースグループ制御 Event Summary 0038固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割は確認操作で状態欄を整理することで検証報告ROを確認し・ノード間構成データODM差分を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能登録・クラス・検証報でDの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・登録）です。照合登録・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・登録・ノードです。比較登録・クラス・検証報・ノードでA:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸はclv・登録・検証報です。運用登録・clvでB:の整合確認 起動順序は「ノードの状態と raw_state」を述べるため、正答側の照合軸は検証報・クラス・登録です。項目登録・クラス・検証報でC:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸はノード・クラス・検証報です。用語登録・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0202**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0202について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0202A
    ```

    画面・出力には PHA72DD0202A が表示され、クラスタ構成検証 clverify.log 0202 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0202
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0202B
    ```

    画面・出力には PHA72DD0202B が表示され、クラスタ構成検証 clverify.log 0202 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0202
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0202C
    ```

    画面・出力には PHA72DD0202C が表示され、クラスタ構成検証 clverify.log 0202 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0202A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0202B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0202C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0217 {#c25-i0494}
*分類: 構成検証*  ・  難易度: 中級

藤R登録0218ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藤R登録0218です。藤R登録0218はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録藤R登録0218です。藤R登録0218ではROHAレポートと取得時刻を採取票藤R登録0218へ残します。藤R登録0218では未同期構成の見落としを避けるため補助資料も照合する判断藤R登録0218です。藤R登録0218の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録藤R登録0218です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 clverify.log 0217」を「リソースグループ制御 Resource Group Name 0260」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして優先ノード一を照合する。
    - B. 仕様上の役割は片系定義を全体正本とする誤認を避けるため・ネットワーク照会からnet_ether_してネットワークを照合する。
    - C. 仕様上の役割はミラー再同期条件の誤読を避けるため・照合操作で確認欄を採取するしてミラー更新状を照合する。
    - D. 仕様上の役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして検証報告ROを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能登録・クラス・検証報でDの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・登録）です。照合登録・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・登録・未同期です。比較登録・クラス・検証報・未同期でA:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸はclv・登録・検証報です。運用登録・clvでB:の性能影響の確認 TOPO11は「クラスタートポロジーでネットワーク照会から」を述べるため、正答側の照合軸は検証報・クラス・登録です。項目登録・クラス・検証報でC:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は未同期・クラス・検証報です。用語登録・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0217**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0217について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0217A
    ```

    画面・出力には PHA72DD0217A が表示され、クラスタ構成検証 clverify.log 0217 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0217
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0217B
    ```

    画面・出力には PHA72DD0217B が表示され、クラスタ構成検証 clverify.log 0217 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0217
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0217C
    ```

    画面・出力には PHA72DD0217C が表示され、クラスタ構成検証 clverify.log 0217 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0217A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0217B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0217C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0232 {#c25-i0495}
*分類: 構成検証*  ・  難易度: 上級

桃M確認0233ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票桃M確認0233です。桃M確認0233はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録桃M確認0233です。桃M確認0233ではROHAレポートと取得時刻を採取票桃M確認0233へ残します。桃M確認0233では検証ログの採取漏れを避けるため補助資料も照合する判断桃M確認0233です。桃M確認0233の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録桃M確認0233です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0232を同一分類のリソースグループ制御 Resource Group Name 0305と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は資源グループの優先ノード一覧と取得時刻を記録し・資源グループ位置の誤認を防ぐである。復旧操作で点検欄を確認するときは資源グループ位置の誤認を防ぐ。リソースグループ制御 Resource Group Name 0305固有の属性も確認対象に含める。
    - B. コマンドまたは機能の用途はノードの状態と raw_state を確認するコマンドを整合確認する。整合確認で起動順序を確認するときは起動順序の誤読を防ぐ。
    - C. コマンドまたは機能の用途はclverify.logの検証報告ROHAレポートと取得時刻を記録し・検証ログの採取漏れを防ぐである。保守操作で監査欄を保存するときは検証ログの採取漏れを防ぐ。 ✅
    - D. コマンドまたは機能の用途はイベント要約の失敗ラベルと取得時刻を記録し・獲得失敗ログの未採取を防ぐである。表示操作で対象欄を追跡するときは獲得失敗ログの未採取を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能確認・クラス・検証報でCの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・確認）です。照合確認・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・確認・検証ロです。比較確認・クラス・検証報・検証ロでA:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸はclv・確認・検証報です。運用確認・clvでB:の整合確認 起動順序は「ノードの状態と raw_state」を述べるため、正答側の照合軸は検証報・クラス・確認です。仕様確認・クラス・検証報でD:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は確認・検証ロ・検証報です。用語確認・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0232**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0232について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0232A
    ```

    画面・出力には PHA72DD0232A が表示され、クラスタ構成検証 clverify.log 0232 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0232
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0232B
    ```

    画面・出力には PHA72DD0232B が表示され、クラスタ構成検証 clverify.log 0232 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0232
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0232C
    ```

    画面・出力には PHA72DD0232C が表示され、クラスタ構成検証 clverify.log 0232 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0232A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0232B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0232C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0247 {#c25-i0496}
*分類: 構成検証*  ・  難易度: 初級

茶H保護0248ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票茶H保護0248です。茶H保護0248はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録茶H保護0248です。茶H保護0248ではROHAレポートと取得時刻を採取票茶H保護0248へ残します。茶H保護0248では警告と致命エラーの混同を避けるため補助資料も照合する判断茶H保護0248です。茶H保護0248の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録茶H保護0248です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0247の設定や表示を読む前に役割を確認します。GLVM地理的ミラー Mirror Pool 0300ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は地理的ミラーの項目のVG vary状態と取得時刻を記録し・ミラー再同期条件の誤読を防ぐである。照合操作で確認欄を採取するときはミラー再同期条件の誤読を防ぐ。
    - B. 一次資料が示す主目的はclverify.logの検証報告ROHAレポートと取得時刻を記録し・警告と致命エラーの混同を防ぐである。採取操作で照合欄を点検するときは警告と致命エラーの混同を防ぐ。 ✅
    - C. 一次資料が示す主目的はPowerHA Node Stateでノード一覧から 実状態値 を読み・実状態値 とである。ノード一覧から実状態値を読むときは基本ソフト稼働とクラスタ稼働を防ぐ。ノード状態 PowerHA Node State 依存関係の確認固有の属性も確認対象に含める。
    - D. 一次資料が示す主目的は構成検証のリソース要約と取得時刻を記録し・ノード間構成データODM差分の残存を防ぐである。確認操作で状態欄を整理するときはノード間構成データODM差分を防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能保護・クラス・検証報でBの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・保護）です。照合保護・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・保護・警告とです。比較保護・クラス・検証報・警告とでA:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸はclv・保護・検証報です。項目保護・クラス・検証報でC:の依存関係の確認 NODE13は「PowerHA Node Stateでノード」を述べるため、正答側の照合軸は警告と・クラス・検証報です。仕様保護・クラス・検証報でD:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸は保護・警告と・検証報です。用語保護・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0247**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0247について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0247A
    ```

    画面・出力には PHA72DD0247A が表示され、クラスタ構成検証 clverify.log 0247 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0247
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0247B
    ```

    画面・出力には PHA72DD0247B が表示され、クラスタ構成検証 clverify.log 0247 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0247
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0247C
    ```

    画面・出力には PHA72DD0247C が表示され、クラスタ構成検証 clverify.log 0247 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0247A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0247B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0247C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0262 {#c25-i0497}
*分類: 構成検証*  ・  難易度: 初級

緑C照合0263ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票緑C照合0263です。緑C照合0263はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録緑C照合0263です。緑C照合0263ではROHAレポートと取得時刻を採取票緑C照合0263へ残します。緑C照合0263ではノード間ODM差分の残存を避けるため補助資料も照合する判断緑C照合0263です。緑C照合0263の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録緑C照合0263です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0262に関する障害切り分けの前提を確認しています。クラスタ構成検証 Verification Progress 0316の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はノード間構成データODM差分の残を避けるため・確認操作で状態欄を整理するして検証報告ROを照合する。 ✅
    - B. 障害切り分けに用いる役割は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するしてリソース要約を照合する。
    - C. 障害切り分けに用いる役割は監視通信SNMP情報の残留を実ノを避けるため・クラスタ表示からClusterを読むしてクラスタ表示を照合する。
    - D. 障害切り分けに用いる役割はsyslogとhacmp.outを避けるため・監査操作で記録欄を比較するして遠隔ボリューを照合する。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能照合・クラス・検証報でAの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・照合）です。照合照合・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・照合・ノードです。運用照合・clvでB:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸は検証報・クラス・照合です。項目照合・クラス・検証報でC:の引継ぎ記録 CLSTAT09は「clstatでクラスタ表示から」を述べるため、正答側の照合軸はノード・クラス・検証報です。仕様照合・クラス・検証報でD:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸は照合・ノード・検証報です。用語照合・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0262**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0262について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0262A
    ```

    画面・出力には PHA72DD0262A が表示され、クラスタ構成検証 clverify.log 0262 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0262
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0262B
    ```

    画面・出力には PHA72DD0262B が表示され、クラスタ構成検証 clverify.log 0262 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0262
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0262C
    ```

    画面・出力には PHA72DD0262C が表示され、クラスタ構成検証 clverify.log 0262 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0262A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0262B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0262C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0277 {#c25-i0498}
*分類: 構成検証*  ・  難易度: 中級

藤R照合0278ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藤R照合0278です。藤R照合0278はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録藤R照合0278です。藤R照合0278ではROHAレポートと取得時刻を採取票藤R照合0278へ残します。藤R照合0278では未同期構成の見落としを避けるため補助資料も照合する判断藤R照合0278です。藤R照合0278の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録藤R照合0278です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0277を保守記録に説明する必要があります。リソースグループ制御 Acquisition Failure 0356と取り違えない説明はどれですか。

    - A. 仕様上の役割は解除で獲得イベントを証跡に残し・獲得処理の獲得イベントと取得時刻を記録し。
    - B. 仕様上の役割は再始動確認でエラー記録を証跡に残し・hacmp.out Eventでエラー記録から。
    - C. 仕様上の役割は診断でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。クラスタ構成検証 Cluster Resources 0130固有の属性も確認対象に含める。
    - D. 仕様上の役割は照合で検証報告ROを証跡に残し・clverify.logの検証報告ROHAレポートと取得時刻。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能照合・クラス・検証報でDの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・照合）です。照合照合・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・照合・未同期です。比較照合・クラス・検証報・未同期でA:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸はclv・照合・検証報です。運用照合・clvでB:の再始動後の確認 FAIL15は「hacmp.out Eventでエラー記録か」を述べるため、正答側の照合軸は検証報・クラス・照合です。項目照合・クラス・検証報でC:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は未同期・クラス・検証報です。用語照合・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0277**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0277について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0277A
    ```

    画面・出力には PHA72DD0277A が表示され、クラスタ構成検証 clverify.log 0277 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0277
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0277B
    ```

    画面・出力には PHA72DD0277B が表示され、クラスタ構成検証 clverify.log 0277 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0277
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0277C
    ```

    画面・出力には PHA72DD0277C が表示され、クラスタ構成検証 clverify.log 0277 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0277A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0277B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0277C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0292 {#c25-i0499}
*分類: 構成検証*  ・  難易度: 中級

桃M抑止0293ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票桃M抑止0293です。桃M抑止0293はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録桃M抑止0293です。桃M抑止0293ではROHAレポートと取得時刻を採取票桃M抑止0293へ残します。桃M抑止0293では検証ログの採取漏れを避けるため補助資料も照合する判断桃M抑止0293です。桃M抑止0293の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録桃M抑止0293です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0292の技術的な意味を資料で確認するとき、GLVM地理的ミラー VG STATE 0348との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は解除で基本ソフトAを証跡に残し・地理的ミラーの項目の基本ソフトAIXエラー識別子と取得時刻を。
    - B. コマンドまたは機能の用途は再始動確認で再確認を証跡に残し・Cluster Synchronizで再確認から。
    - C. コマンドまたは機能の用途は収集で失敗ラベルを証跡に残し・イベント要約の失敗ラベルと取得時刻を記録し。
    - D. コマンドまたは機能の用途は抑止で検証報告ROを証跡に残し・clverify.logの検証報告ROHAレポートと取得時刻。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能抑止・クラス・検証報でDの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・抑止）です。照合抑止・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・抑止・検証ロです。比較抑止・クラス・検証報・検証ロでA:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸はclv・抑止・検証報です。運用抑止・clvでB:の再始動後の確認 SYNC15は「Cluster Synchronizで再確認」を述べるため、正答側の照合軸は検証報・クラス・抑止です。項目抑止・クラス・検証報でC:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は検証ロ・クラス・検証報です。用語抑止・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0292**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0292について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0292A
    ```

    画面・出力には PHA72DD0292A が表示され、クラスタ構成検証 clverify.log 0292 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0292
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0292B
    ```

    画面・出力には PHA72DD0292B が表示され、クラスタ構成検証 clverify.log 0292 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0292
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0292C
    ```

    画面・出力には PHA72DD0292C が表示され、クラスタ構成検証 clverify.log 0292 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0292A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0292B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0292C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0307 {#c25-i0500}
*分類: 構成検証*  ・  難易度: 中級

茶H解析0308ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票茶H解析0308です。茶H解析0308はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録茶H解析0308です。茶H解析0308ではROHAレポートと取得時刻を採取票茶H解析0308へ残します。茶H解析0308では警告と致命エラーの混同を避けるため補助資料も照合する判断茶H解析0308です。茶H解析0308の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録茶H解析0308です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0307について構成や状態を確認します。cltopinfo トポロジー確認 実行結果ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はトポロジー確で実行結果を証跡に残し・クラスタトポロジー・ネットワーク・サービスIP。cltopinfo トポロジー確認 実行結果固有の属性も確認対象に含める。
    - B. 一次資料が示す主目的は解析で検証報告ROを証跡に残し・clverify.logの検証報告ROHAレポートと取得時刻。 ✅
    - C. 一次資料が示す主目的は棚卸で失敗ラベルを証跡に残し・イベント要約の失敗ラベルと取得時刻を記録し。
    - D. 一次資料が示す主目的は収集でVG varを証跡に残し・地理的ミラーの項目のVG vary状態と取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能解析・クラス・検証報でBの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・解析）です。照合解析・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・解析・警告とです。比較解析・クラス・検証報・警告とでA:のトポロジー確認 実行結果は「クラスタトポロジー、ネットワーク」を述べるため、正答側の照合軸はclv・解析・検証報です。項目解析・クラス・検証報でC:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は警告と・クラス・検証報です。仕様解析・クラス・検証報でD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は解析・警告と・検証報です。用語解析・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0307**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0307について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0307A
    ```

    画面・出力には PHA72DD0307A が表示され、クラスタ構成検証 clverify.log 0307 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0307
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0307B
    ```

    画面・出力には PHA72DD0307B が表示され、クラスタ構成検証 clverify.log 0307 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0307
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0307C
    ```

    画面・出力には PHA72DD0307C が表示され、クラスタ構成検証 clverify.log 0307 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0307A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0307B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0307C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0322 {#c25-i0501}
*分類: 構成検証*  ・  難易度: 中級

緑C計画0323ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票緑C計画0323です。緑C計画0323はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録緑C計画0323です。緑C計画0323ではROHAレポートと取得時刻を採取票緑C計画0323へ残します。緑C計画0323ではノード間ODM差分の残存を避けるため補助資料も照合する判断緑C計画0323です。緑C計画0323の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録緑C計画0323です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0322の役割を調べています。クラスタ構成検証 Cluster Topology 0328の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして構成データOを照合する。
    - B. 障害切り分けに用いる役割はノード間構成データODM差分の残を避けるため・確認操作で状態欄を整理するして検証報告ROを照合する。 ✅
    - C. 障害切り分けに用いる役割は監視通信SNMP情報の残留を実ノを避けるため・クラスタ表示からClusterを読むしてクラスタ表示を照合する。
    - D. 障害切り分けに用いる役割は獲得失敗ログの未採取を避けるため・表示操作で対象欄を追跡するして失敗ラベルを照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能計画・クラス・検証報でBの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・計画）です。照合計画・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・計画・ノードです。比較計画・クラス・検証報・ノードでA:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸はclv・計画・検証報です。項目計画・クラス・検証報でC:の引継ぎ記録 CLSTAT09は「clstatでクラスタ表示から」を述べるため、正答側の照合軸はノード・クラス・検証報です。仕様計画・クラス・検証報でD:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は計画・ノード・検証報です。用語計画・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0322**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0322について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0322A
    ```

    画面・出力には PHA72DD0322A が表示され、クラスタ構成検証 clverify.log 0322 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0322
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0322B
    ```

    画面・出力には PHA72DD0322B が表示され、クラスタ構成検証 clverify.log 0322 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0322
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0322C
    ```

    画面・出力には PHA72DD0322C が表示され、クラスタ構成検証 clverify.log 0322 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0322A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0322B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0322C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0337 {#c25-i0502}
*分類: 構成検証*  ・  難易度: 中級

藤R計画0338ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藤R計画0338です。藤R計画0338はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録藤R計画0338です。藤R計画0338ではROHAレポートと取得時刻を採取票藤R計画0338へ残します。藤R計画0338では未同期構成の見落としを避けるため補助資料も照合する判断藤R計画0338です。藤R計画0338の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録藤R計画0338です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 clverify.log 0337」を「cltopinfo 障害切り分け パス状態」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はclverify.logの検証報告ROHAレポートと取得時刻を記録し・未同期構成の見落としを防ぐである。記録操作で証跡欄を照合するときは未同期構成の見落としを防ぐ。 ✅
    - B. 仕様上の役割はクラスタトポロジー・ネットワーク・サービスIP・リソースグループを表示するコマンドである。サービスIPでパス状態を確認するときはパス状態の誤読を防ぐ。
    - C. 仕様上の役割は獲得処理の獲得イベントと取得時刻を記録し・依存リソース順序の見落としを防ぐである。点検操作で判定欄を記録するときは依存リソース順序の見落としを防ぐ。
    - D. 仕様上の役割は地理的ミラーの項目のミラー更新状態と取得時刻を記録し・syslogとhacmp.outの突合漏れを防ぐである。監査操作で記録欄を比較するときはsyslogとhacmp.oを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能計画・クラス・検証報でAの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・計画）です。照合計画・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・計画・未同期です。運用計画・clvでB:の障害切り分け パス状態は「クラスタトポロジー、ネットワーク」を述べるため、正答側の照合軸は検証報・クラス・計画です。項目計画・クラス・検証報でC:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は未同期・クラス・検証報です。仕様計画・クラス・検証報でD:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は計画・未同期・検証報です。用語計画・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0337**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0337について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0337A
    ```

    画面・出力には PHA72DD0337A が表示され、クラスタ構成検証 clverify.log 0337 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0337
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0337B
    ```

    画面・出力には PHA72DD0337B が表示され、クラスタ構成検証 clverify.log 0337 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0337
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0337C
    ```

    画面・出力には PHA72DD0337C が表示され、クラスタ構成検証 clverify.log 0337 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0337A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0337B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0337C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 clverify.log 0352 {#c25-i0503}
*分類: 構成検証*  ・  難易度: 上級

桃M解除0353ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票桃M解除0353です。桃M解除0353はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録桃M解除0353です。桃M解除0353ではROHAレポートと取得時刻を採取票桃M解除0353へ残します。桃M解除0353では検証ログの採取漏れを避けるため補助資料も照合する判断桃M解除0353です。桃M解除0353の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録桃M解除0353です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 clverify.log 0352を同一分類のclmgr query cluster 整合確認 詳細表示と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はclverify.logの検証報告ROHAレポートと取得時刻を記録し・検証ログの採取漏れを防ぐである。保守操作で監査欄を保存するときは検証ログの採取漏れを防ぐ。 ✅
    - B. コマンドまたは機能の用途はクラスタ名・状態・バージョンなどのクラスタ属性を表示するコマンドを整合確認する。詳細表示で詳細表示を確認するときは詳細表示の誤読を防ぐ。
    - C. コマンドまたは機能の用途はシステム管理コマンドの検証進行率と取得時刻を記録し・検証ログの採取漏れを防ぐである。保守操作で監査欄を保存するときは検証ログの採取漏れを防ぐ。クラスタ構成検証 SMIT Command Status 0004固有の属性も確認対象に含める。
    - D. コマンドまたは機能の用途は資源グループの優先ノード一覧と取得時刻を記録し・資源グループ位置の誤認を防ぐである。復旧操作で点検欄を確認するときは資源グループ位置の誤認を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能解除・クラス・検証報でAの記述「clverify.logの検証報告ROHAレポートと取得」に対応する項目はクラスタ構成検証 clverify.（clv・検証報・解除）です。照合解除・クラス・検証報に関する構成検証の仕様は「clverify.logの検証報告ROHAレポートと取得時刻を記録し」で、確認対象は検証報・解除・検証ロです。運用解除・clvでB:の整合確認 詳細表示は「クラスタ名、状態、バージョンなどのクラスタ属」を述べるため、正答側の照合軸は検証報・クラス・解除です。項目解除・クラス・検証報でC:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸は検証ロ・クラス・検証報です。仕様解除・クラス・検証報でD:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は解除・検証ロ・検証報です。用語解除・クラス・検証報という用語は「clverify.logの検証報告ROHAレポートと」を指し、照合する値と誤認リスクの組合せはクラス・検証報・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 clverify.log 0352**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 clverify.log 0352について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=clverify.log と ROHAレポート
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0352A
    ```

    画面・出力には PHA72DD0352A が表示され、クラスタ構成検証 clverify.log 0352 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0352
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0352B
    ```

    画面・出力には PHA72DD0352B が表示され、クラスタ構成検証 clverify.log 0352 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。clverify.log を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0352
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0352C
    ```

    画面・出力には PHA72DD0352C が表示され、クラスタ構成検証 clverify.log 0352 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0352A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0352B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0352C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434




## PowerHA SystemMirror 7.2 > 資源依存関係

### 資源依存関係 Resource Group Dependency ログとの照合 DEP07 {#c25-i0504}
*分類: 資源依存関係*  ・  難易度: 上級

ログとの照合では 資源依存関係 の 依存照会 を主操作として DEP07 を判定します。時刻と対象識別子への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP07 に残します。ログとの照合を補助する RG一覧 では database_rg を補助値として DEP07 へ保存します。主判定のログとの照合では資源依存関係の 依存照会 から START_AFTER を読み DEP07 へ残します。証跡照合のログとの照合では資源依存関係の START_AFTER と database_rg を DEP07 に保存します。記録対応のログとの照合では資源依存関係の Parent RGとChild RG の証跡へ DEP07 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency ログとの照合 DEP07を同一分類のクラスタ構成検証 Cluster Topology 0088と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は保守操作で監査欄を保存することで構成データOを確認し・検証ログの採取漏れを防ぐ。クラスタ構成検証 Cluster Topology 0088固有の属性も確認対象に含める。
    - B. コマンドまたは機能の用途は保守操作で監査欄を保存することでリソース要約を確認し・検証ログの採取漏れを防ぐ。
    - C. コマンドまたは機能の用途は依存照会からSTART_AFTERを読むことで依存照会を確認し・依存順を無視して子資源を先にを防ぐ。 ✅
    - D. コマンドまたは機能の用途はサンプル採取でサンプル採取を確認することでサンプル採取を確認し・サンプル採取の誤読を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能ログと・資源依・依存照でCの記述「資源グループで依存照会から START_AFTER」に対応する項目はログとの照合 DEP07（資源グ・依存照・ログと）です。照合ログと・資源依・依存照に関する資源依存関係の仕様は「資源グループで依存照会から START_AFTER を読み」で、確認対象は依存照・ログと・依存順です。比較資源依・ログとでA:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は資源グ・ログと・依存照です。運用ログと・資源グでB:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸は依存照・資源依・ログとです。仕様ログと・資源依・依存照でD:の状態確認 サンプル採取は「ノードの状態と raw_state」を述べるため、正答側の照合軸はログと・依存順・依存照です。用語ログと・資源依・依存照という用語は「資源グループで依存照会から START_AFTER」を指し、照合する値と誤認リスクの組合せは資源依・依存照・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency ログとの照合 DEP07**

    - 検証目的: 資源依存関係のResource Group Dependencyについて操作とログを対応し、DEP07のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP07の依存照会を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr query resource_group app_rg
    → Enter を押す
    ```

    画面・出力:
    ```text
    NAME=app_rg
    PARENT=database_rg
    START_AFTER=network_rg
    ONLINE_NODE=node1
    ```

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP07のRG一覧を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clRGinfo -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    database_rg ONLINE node1
    network_rg ONLINE node1
    app_rg ONLINE node1
    ```

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP07のイベント順序を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "database_rg|app_rg" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    database_rg acquire completed Exit status = 0
    app_rg acquire started after database_rg
    app_rg acquire completed Exit status = 0
    ```

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の NAME=app が画面・出力に表示されること
    ② ステップ2 の database が画面・出力に表示されること
    ③ ステップ3 の completed が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 代替経路の確認 DEP10 {#c25-i0505}
*分類: 資源依存関係*  ・  難易度: 上級

代替経路の確認では 資源依存関係 の 依存照会 を主操作として DEP10 を判定します。主経路との役割差への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP10 に残します。代替経路の確認を補助する RG一覧 では database_rg を補助値として DEP10 へ保存します。主判定の代替経路の確認では資源依存関係の 依存照会 から START_AFTER を読み DEP10 へ残します。証跡照合の代替経路の確認では資源依存関係の START_AFTER と database_rg を DEP10 に保存します。記録対応の代替経路の確認では資源依存関係の Parent RGとChild RG の証跡へ DEP10 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 代替経路の確認 DEP10について構成や状態を確認します。リソースグループ制御 Event Summary 0083ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は資源グループで依存照会から START_AFTER を読み・START_AFTER とである。依存照会からSTART_AFTERをときは依存順を無視して子資源を先にを防ぐ。 ✅
    - B. 一次資料が示す主目的はイベント要約の失敗ラベルと取得時刻を記録し・獲得失敗ログの未採取を防ぐである。表示操作で対象欄を追跡するときは獲得失敗ログの未採取を防ぐ。リソースグループ制御 Event Summary 0083固有の属性も確認対象に含める。
    - C. 一次資料が示す主目的はclverify.logの検証報告ROHAレポートと取得時刻を記録しである。確認操作で状態欄を整理するときはノード間構成データODM差分を防ぐ。
    - D. 一次資料が示す主目的はクラスタ・ノード・インターフェース・リソースグループの状態を表示する監視コマンドを起動確認する。起動確認でイベント転送を確認するときはイベント転送の誤読を防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能代替経・資源依・依存照でAの記述「資源グループで依存照会から START_AFTER」に対応する項目は代替経路の確認 DEP10（資源グ・依存照・代替経）です。照合代替経・資源依・依存照に関する資源依存関係の仕様は「資源グループで依存照会から START_AFTER を読み」で、確認対象は依存照・代替経・依存順です。運用代替経・資源グでB:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は依存照・資源依・代替経です。項目代替経・資源依・依存照でC:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸は依存順・資源依・依存照です。仕様代替経・資源依・依存照でD:の起動確認 イベント転送は「クラスタ、ノード、インターフェース」を述べるため、正答側の照合軸は代替経・依存順・依存照です。用語代替経・資源依・依存照という用語は「資源グループで依存照会から START_AFTER」を指し、照合する値と誤認リスクの組合せは資源依・依存照・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 代替経路の確認 DEP10**

    - 検証目的: 資源依存関係のResource Group Dependencyについて代替手段の成立を確認し、DEP10のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP10の依存照会を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr query resource_group app_rg
    → Enter を押す
    ```

    画面・出力:
    ```text
    NAME=app_rg
    PARENT=database_rg
    START_AFTER=network_rg
    ONLINE_NODE=node1
    ```

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP10のRG一覧を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clRGinfo -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    database_rg ONLINE node1
    network_rg ONLINE node1
    app_rg ONLINE node1
    ```

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP10のイベント順序を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "database_rg|app_rg" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    database_rg acquire completed Exit status = 0
    app_rg acquire started after database_rg
    app_rg acquire completed Exit status = 0
    ```

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の NAME=app が画面・出力に表示されること
    ② ステップ2 の database が画面・出力に表示されること
    ③ ステップ3 の completed が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 依存関係の確認 DEP13 {#c25-i0506}
*分類: 資源依存関係*  ・  難易度: 上級

依存関係の確認では 資源依存関係 の 依存照会 を主操作として DEP13 を判定します。前提資源と後続処理の順序への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP13 に残します。依存関係の確認を補助する RG一覧 では database_rg を補助値として DEP13 へ保存します。主判定の依存関係の確認では資源依存関係の 依存照会 から START_AFTER を読み DEP13 へ残します。証跡照合の依存関係の確認では資源依存関係の START_AFTER と database_rg を DEP13 に保存します。記録対応の依存関係の確認では資源依存関係の Parent RGとChild RG の証跡へ DEP13 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 依存関係の確認 DEP13に関する障害切り分けの前提を確認しています。リソースグループ制御 Resource Group Name 0020の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして優先ノード一を照合する。
    - B. 障害切り分けに用いる役割は依存順を無視して子資源を先にオンを避けるため・依存照会からSTART_AFTERを読むして依存照会を照合する。 ✅
    - C. 障害切り分けに用いる役割は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして検証進行率を照合する。クラスタ構成検証 SMIT Command Status 0184固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割は照合単位の誤読を避けるため・照合単位で照合単位を確認するして照合単位を照合する。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能依存関・資源依・依存照でBの記述「資源グループで依存照会から START_AFTER」に対応する項目は依存関係の確認 DEP13（資源グ・依存照・依存関）です。照合依存関・資源依・依存照に関する資源依存関係の仕様は「資源グループで依存照会から START_AFTER を読み」で、確認対象は依存照・依存関・依存順です。比較資源依・依存関でA:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は資源グ・依存関・依存照です。項目依存関・資源依・依存照でC:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸は依存順・資源依・依存照です。仕様依存関・資源依・依存照でD:の起動確認 照合単位は「クラスタトポロジーとリソースの整合性を検査す」を述べるため、正答側の照合軸は依存関・依存順・依存照です。用語依存関・資源依・依存照という用語は「資源グループで依存照会から START_AFTER」を指し、照合する値と誤認リスクの組合せは資源依・依存照・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 依存関係の確認 DEP13**

    - 検証目的: 資源依存関係のResource Group Dependencyについて依存資源を点検し、DEP13のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP13の依存照会を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr query resource_group app_rg
    → Enter を押す
    ```

    画面・出力:
    ```text
    NAME=app_rg
    PARENT=database_rg
    START_AFTER=network_rg
    ONLINE_NODE=node1
    ```

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP13のRG一覧を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clRGinfo -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    database_rg ONLINE node1
    network_rg ONLINE node1
    app_rg ONLINE node1
    ```

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP13のイベント順序を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "database_rg|app_rg" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    database_rg acquire completed Exit status = 0
    app_rg acquire started after database_rg
    app_rg acquire completed Exit status = 0
    ```

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の NAME=app が画面・出力に表示されること
    ② ステップ2 の database が画面・出力に表示されること
    ③ ステップ3 の completed が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 停止前の確認 DEP14 {#c25-i0507}
*分類: 資源依存関係*  ・  難易度: 上級

停止前の確認では 資源依存関係 の RG一覧 を主操作として DEP14 を判定します。処理中資源と未完了要求への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP14 に残します。停止前の確認を補助する イベント順序 では completed を補助値として DEP14 へ保存します。主判定の停止前の確認では資源依存関係の RG一覧 から database_rg を読み DEP14 へ残します。証跡照合の停止前の確認では資源依存関係の database_rg と completed を DEP14 に保存します。記録対応の停止前の確認では資源依存関係の Parent RGとChild RG の証跡へ DEP14 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 停止前の確認 DEP14の設定や表示を読む前に役割を確認します。リソースグループ制御 Event Summary 0068ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは資源グループで資源グループRG一覧から database_rg を読み・database_rg とである。RG一覧からdatabase_rgをときは依存順を無視して子資源を先にを防ぐ。 ✅
    - B. 状態を読み取るための働きはイベント要約の失敗ラベルと取得時刻を記録し・自動戻し条件の誤読を防ぐである。調査操作で保守欄を引き継ぎするときは自動戻し条件の誤読を防ぐ。リソースグループ制御 Event Summary 0068固有の属性も確認対象に含める。
    - C. 状態を読み取るための働きはクラスター資源のトポロジ要約と取得時刻を記録し・ノード間構成データODM差分の残存を防ぐである。確認操作で状態欄を整理するときはノード間構成データODM差分を防ぐ。
    - D. 状態を読み取るための働きはIP Service IPで資源グループ位置から オンライン表示 を読み・オンライン表示 とである。RG位置からオンライン表示を読むときは永続アドレスとサービスアドレを防ぐ。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能停止確・資源依・資源グでAの記述「資源グループで資源グループRG一覧から」に対応する項目は停止前の確認 DEP14（資源グ・資源グ・停止確）です。照合停止確・資源依・資源グに関する資源依存関係の仕様は「資源グループで資源グループRG一覧から database_rg」で、確認対象は資源グ・停止確・依存順です。運用停止確・資源グでB:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は資源グ・資源依・停止確です。項目停止確・資源依・資源グでC:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は依存順・資源依・資源グです。仕様停止確・資源依・資源グでD:の停止前の確認 SVCIP14は「IP Service IPで資源グループ位置」を述べるため、正答側の照合軸は停止確・依存順・資源グです。用語停止確・資源依・資源グという用語は「資源グループで資源グループRG一覧から」を指し、照合する値と誤認リスクの組合せは資源依・資源グ・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 停止前の確認 DEP14**

    - 検証目的: 資源依存関係のResource Group Dependencyについて安全な停止条件を確認し、DEP14のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP14のRG一覧を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clRGinfo -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    database_rg ONLINE node1
    network_rg ONLINE node1
    app_rg ONLINE node1
    ```

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP14のイベント順序を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "database_rg|app_rg" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    database_rg acquire completed Exit status = 0
    app_rg acquire started after database_rg
    app_rg acquire completed Exit status = 0
    ```

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP14の依存照会を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr query resource_group app_rg
    → Enter を押す
    ```

    画面・出力:
    ```text
    NAME=app_rg
    PARENT=database_rg
    START_AFTER=network_rg
    ONLINE_NODE=node1
    ```

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の database が画面・出力に表示されること
    ② ステップ2 の completed が画面・出力に表示されること
    ③ ステップ3 の NAME=app が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


