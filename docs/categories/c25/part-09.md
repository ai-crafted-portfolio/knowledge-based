---
search:
  exclude: true
---

# PowerHA SystemMirror 7.2 — 詳細 (9/11)

[← PowerHA SystemMirror 7.2 の概要へ戻る](index.md)


## PowerHA SystemMirror 7.2 > 構成検証

### クラスタ構成検証 Cluster Topology 0043 {#c25-i0410}
*分類: 構成検証*  ・  難易度: 中級

藍D復旧0044ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藍D復旧0044です。藍D復旧0044はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録藍D復旧0044です。藍D復旧0044ではODM登録値と取得時刻を採取票藍D復旧0044へ残します。藍D復旧0044では警告と致命エラーの混同を避けるため補助資料も照合する判断藍D復旧0044です。藍D復旧0044の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録藍D復旧0044です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0043について構成や状態を確認します。リソースグループ制御 Resource Group Name 0095ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は変更で優先ノード一を証跡に残し・資源グループの優先ノード一覧と取得時刻を記録し。
    - B. 一次資料が示す主目的は確認で基本ソフトAを証跡に残し・地理的ミラーの項目の基本ソフトAIXエラー識別子と取得時刻を。
    - C. 一次資料が示す主目的はサービスIPでインターフェを証跡に残し・IP Service IPでインターフェースから。
    - D. 一次資料が示す主目的は復旧で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能復旧・クラス・構成デでDの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・復旧）です。照合復旧・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・復旧・警告とです。比較クラス・復旧でA:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸はクラス・復旧・構成デです。運用復旧・クラスでB:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸は構成デ・クラス・復旧です。項目復旧・クラス・構成デでC:の引継ぎ記録 SVCIP09は「IP Service IPでインターフェース」を述べるため、正答側の照合軸は警告と・クラス・構成デです。用語復旧・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0043**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0043について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0043A
    ```

    画面・出力には PHA72DD0043A が表示され、クラスタ構成検証 Cluster Topology 0043 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0043
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0043B
    ```

    画面・出力には PHA72DD0043B が表示され、クラスタ構成検証 Cluster Topology 0043 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0043
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0043C
    ```

    画面・出力には PHA72DD0043C が表示され、クラスタ構成検証 Cluster Topology 0043 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0043A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0043B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0043C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0058 {#c25-i0411}
*分類: 構成検証*  ・  難易度: 中級

黒S復旧0059ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黒S復旧0059です。黒S復旧0059はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録黒S復旧0059です。黒S復旧0059ではODM登録値と取得時刻を採取票黒S復旧0059へ残します。黒S復旧0059ではノード間ODM差分の残存を避けるため補助資料も照合する判断黒S復旧0059です。黒S復旧0059の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録黒S復旧0059です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0058の役割を調べています。リソースグループ制御 Event Summary 0083の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は復旧で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。 ✅
    - B. 障害切り分けに用いる役割は変更で失敗ラベルを証跡に残し・イベント要約の失敗ラベルと取得時刻を記録し。
    - C. 障害切り分けに用いる役割は計画で獲得イベントを証跡に残し・獲得処理の獲得イベントと取得時刻を記録し。リソースグループ制御 Acquisition Failure 0326固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割は通常状態確認で主要ログを証跡に残し・hacmp.out Eventで主要ログから。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能復旧・クラス・構成デでAの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・復旧）です。照合復旧・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・復旧・ノードです。運用復旧・クラスでB:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は構成デ・クラス・復旧です。項目復旧・クラス・構成デでC:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸はノード・クラス・構成デです。仕様復旧・クラス・構成デでD:の通常状態の確認 FAIL01は「hacmp.out Eventで主要ログから」を述べるため、正答側の照合軸は復旧・ノード・構成デです。用語復旧・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0058**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0058について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0058A
    ```

    画面・出力には PHA72DD0058A が表示され、クラスタ構成検証 Cluster Topology 0058 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0058
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0058B
    ```

    画面・出力には PHA72DD0058B が表示され、クラスタ構成検証 Cluster Topology 0058 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0058
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0058C
    ```

    画面・出力には PHA72DD0058C が表示され、クラスタ構成検証 Cluster Topology 0058 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0058A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0058B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0058C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0073 {#c25-i0412}
*分類: 構成検証*  ・  難易度: 中級

灰N監査0074ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票灰N監査0074です。灰N監査0074はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録灰N監査0074です。灰N監査0074ではODM登録値と取得時刻を採取票灰N監査0074へ残します。灰N監査0074では未同期構成の見落としを避けるため補助資料も照合する判断灰N監査0074です。灰N監査0074の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録灰N監査0074です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 Cluster Topology 0073」を「クラスタ構成検証 SMIT Command Status 0139」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は診断で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。クラスタ構成検証 SMIT Command Status 0139固有の属性も確認対象に含める。
    - B. 仕様上の役割は監査で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。 ✅
    - C. 仕様上の役割は解除でsyslogを証跡に残し・地理的ミラーの項目のsyslog記録と取得時刻を記録し。
    - D. 仕様上の役割は停止確認で状態確認を証跡に残し・Cluster Servicesで状態確認から。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能監査・クラス・構成デでBの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・監査）です。照合監査・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・監査・未同期です。比較クラス・監査でA:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はクラス・監査・構成デです。項目監査・クラス・構成デでC:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は未同期・クラス・構成デです。仕様監査・クラス・構成デでD:の停止前の確認 START14は「Cluster Servicesで状態確認か」を述べるため、正答側の照合軸は監査・未同期・構成デです。用語監査・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0073**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0073について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0073A
    ```

    画面・出力には PHA72DD0073A が表示され、クラスタ構成検証 Cluster Topology 0073 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0073
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0073B
    ```

    画面・出力には PHA72DD0073B が表示され、クラスタ構成検証 Cluster Topology 0073 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0073
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0073C
    ```

    画面・出力には PHA72DD0073C が表示され、クラスタ構成検証 Cluster Topology 0073 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0073A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0073B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0073C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0088 {#c25-i0413}
*分類: 構成検証*  ・  難易度: 中級

黄I変更0089ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黄I変更0089です。黄I変更0089はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録黄I変更0089です。黄I変更0089ではODM登録値と取得時刻を採取票黄I変更0089へ残します。黄I変更0089では検証ログの採取漏れを避けるため補助資料も照合する判断黄I変更0089です。黄I変更0089の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録黄I変更0089です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0088を同一分類のクラスタ構成検証 SMIT Command Status 0139と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するして検証進行率を照合する。
    - B. コマンドまたは機能の用途はsyslogとhacmp.outを避けるため・監査操作で記録欄を比較するしてミラー更新状を照合する。
    - C. コマンドまたは機能の用途はsyslogとhacmp.outを避けるため・監査操作で記録欄を比較するして基本ソフトAを照合する。
    - D. コマンドまたは機能の用途は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして構成データOを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能変更・クラス・構成デでDの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・変更）です。照合変更・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・変更・検証ロです。比較クラス・変更でA:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はクラス・変更・構成デです。運用変更・クラスでB:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は構成デ・クラス・変更です。項目変更・クラス・構成デでC:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸は検証ロ・クラス・構成デです。用語変更・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0088**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0088について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0088A
    ```

    画面・出力には PHA72DD0088A が表示され、クラスタ構成検証 Cluster Topology 0088 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0088
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0088B
    ```

    画面・出力には PHA72DD0088B が表示され、クラスタ構成検証 Cluster Topology 0088 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0088
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0088C
    ```

    画面・出力には PHA72DD0088C が表示され、クラスタ構成検証 Cluster Topology 0088 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0088A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0088B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0088C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0103 {#c25-i0414}
*分類: 構成検証*  ・  難易度: 上級

藍D移行0104ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藍D移行0104です。藍D移行0104はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録藍D移行0104です。藍D移行0104ではODM登録値と取得時刻を採取票藍D移行0104へ残します。藍D移行0104では警告と致命エラーの混同を避けるため補助資料も照合する判断藍D移行0104です。藍D移行0104の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録藍D移行0104です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0103の設定や表示を読む前に役割を確認します。クラスタ構成検証 Verification Progress 0106ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は確認操作で状態欄を整理することでリソース要約を確認し・ノード間構成データODM差分を防ぐ。
    - B. 一次資料が示す主目的は採取操作で照合欄を点検することで構成データOを確認し・警告と致命エラーの混同を防ぐ。 ✅
    - C. 一次資料が示す主目的は監査操作で記録欄を比較することでsyslogを確認し・syslogとhacmp.oを防ぐ。
    - D. 一次資料が示す主目的はRG確認からapp_rgを読むことで資源グループを確認し・管理設定と資源状態の混同を防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能移行・クラス・構成デでBの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・移行）です。照合移行・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・移行・警告とです。比較クラス・移行でA:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸はクラス・移行・構成デです。項目移行・クラス・構成デでC:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は警告と・クラス・構成デです。仕様移行・クラス・構成デでD:の変更後の確認 START03は「Cluster Servicesで資源グルー」を述べるため、正答側の照合軸は移行・警告と・構成デです。用語移行・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0103**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0103について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0103A
    ```

    画面・出力には PHA72DD0103A が表示され、クラスタ構成検証 Cluster Topology 0103 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0103
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0103B
    ```

    画面・出力には PHA72DD0103B が表示され、クラスタ構成検証 Cluster Topology 0103 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0103
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0103C
    ```

    画面・出力には PHA72DD0103C が表示され、クラスタ構成検証 Cluster Topology 0103 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0103A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0103B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0103C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0118 {#c25-i0415}
*分類: 構成検証*  ・  難易度: 上級

黒S移行0119ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黒S移行0119です。黒S移行0119はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録黒S移行0119です。黒S移行0119ではODM登録値と取得時刻を採取票黒S移行0119へ残します。黒S移行0119ではノード間ODM差分の残存を避けるため補助資料も照合する判断黒S移行0119です。黒S移行0119の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録黒S移行0119です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0118に関する障害切り分けの前提を確認しています。クラスタ構成検証 Cluster Resources 0160の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は保守操作で監査欄を保存することでトポロジ要約を確認し・検証ログの採取漏れを防ぐ。クラスタ構成検証 Cluster Resources 0160固有の属性も確認対象に含める。
    - B. 障害切り分けに用いる役割は確認操作で状態欄を整理することで構成データOを確認し・ノード間構成データODM差分を防ぐ。 ✅
    - C. 障害切り分けに用いる役割は調査操作で保守欄を引き継ぎすることで失敗ラベルを確認し・自動戻し条件の誤読を防ぐ。
    - D. 障害切り分けに用いる役割は復旧操作で点検欄を確認することで移動履歴を確認し・資源グループ位置の誤認を防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能移行・クラス・構成デでBの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・移行）です。照合移行・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・移行・ノードです。比較クラス・移行でA:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸はクラス・移行・構成デです。項目移行・クラス・構成デでC:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸はノード・クラス・構成デです。仕様移行・クラス・構成デでD:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は移行・ノード・構成デです。用語移行・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0118**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0118について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0118A
    ```

    画面・出力には PHA72DD0118A が表示され、クラスタ構成検証 Cluster Topology 0118 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0118
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0118B
    ```

    画面・出力には PHA72DD0118B が表示され、クラスタ構成検証 Cluster Topology 0118 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0118
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0118C
    ```

    画面・出力には PHA72DD0118C が表示され、クラスタ構成検証 Cluster Topology 0118 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0118A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0118B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0118C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0133 {#c25-i0416}
*分類: 構成検証*  ・  難易度: 初級

灰N診断0134ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票灰N診断0134です。灰N診断0134はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録灰N診断0134です。灰N診断0134ではODM登録値と取得時刻を採取票灰N診断0134へ残します。灰N診断0134では未同期構成の見落としを避けるため補助資料も照合する判断灰N診断0134です。灰N診断0134の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録灰N診断0134です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0133を保守記録に説明する必要があります。クラスタ構成検証 SMIT Command Status 0169と取り違えない説明はどれですか。

    - A. 仕様上の役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして検証進行率を照合する。
    - B. 仕様上の役割は片側VGのvaryon誤操作を避けるため・主操作で出力欄を評価するしてsyslogを照合する。
    - C. 仕様上の役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして構成データOを照合する。 ✅
    - D. 仕様上の役割は監視通信SNMP情報の残留を実ノを避けるため・clinfoES状態からclinfoESしてclinfoを照合する。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能診断・クラス・構成デでCの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・診断）です。照合診断・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・診断・未同期です。比較診断・クラス・構成デ・未同期でA:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はクラス・診断・構成デです。運用診断・クラスでB:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は構成デ・クラス・診断です。仕様診断・クラス・構成デでD:のログとの照合 CLSTAT07は「clstatでclinfoES状態から」を述べるため、正答側の照合軸は診断・未同期・構成デです。用語診断・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0133**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0133について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0133A
    ```

    画面・出力には PHA72DD0133A が表示され、クラスタ構成検証 Cluster Topology 0133 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0133
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0133B
    ```

    画面・出力には PHA72DD0133B が表示され、クラスタ構成検証 Cluster Topology 0133 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0133
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0133C
    ```

    画面・出力には PHA72DD0133C が表示され、クラスタ構成検証 Cluster Topology 0133 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0133A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0133B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0133C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0148 {#c25-i0417}
*分類: 構成検証*  ・  難易度: 中級

黄I保守0149ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黄I保守0149です。黄I保守0149はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録黄I保守0149です。黄I保守0149ではODM登録値と取得時刻を採取票黄I保守0149へ残します。黄I保守0149では検証ログの採取漏れを避けるため補助資料も照合する判断黄I保守0149です。黄I保守0149の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録黄I保守0149です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0148の技術的な意味を資料で確認するとき、リソースグループ制御 Node List 0212との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして構成データOを照合する。 ✅
    - B. コマンドまたは機能の用途は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして移動履歴を照合する。
    - C. コマンドまたは機能の用途は整合確認の誤読を避けるため・整合確認で整合確認を確認するして整合確認を照合する。
    - D. コマンドまたは機能の用途はcluster historyだを避けるため・エラー記録からIDENTIFIERを読むしてエラー記録を照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能保守・クラス・構成デでAの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・保守）です。照合保守・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・保守・検証ロです。運用保守・クラスでB:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は構成デ・クラス・保守です。項目保守・クラス・構成デでC:の状態確認 整合確認は「クラスタ構成と状態をスナップショットとして表」を述べるため、正答側の照合軸は検証ロ・クラス・構成デです。仕様保守・クラス・構成デでD:の再始動後の確認 FAIL15は「hacmp.out Eventでエラー記録か」を述べるため、正答側の照合軸は保守・検証ロ・構成デです。用語保守・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0148**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0148について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0148A
    ```

    画面・出力には PHA72DD0148A が表示され、クラスタ構成検証 Cluster Topology 0148 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0148
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0148B
    ```

    画面・出力には PHA72DD0148B が表示され、クラスタ構成検証 Cluster Topology 0148 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0148
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0148C
    ```

    画面・出力には PHA72DD0148C が表示され、クラスタ構成検証 Cluster Topology 0148 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0148A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0148B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0148C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0163 {#c25-i0418}
*分類: 構成検証*  ・  難易度: 中級

藍D切替0164ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藍D切替0164です。藍D切替0164はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録藍D切替0164です。藍D切替0164ではODM登録値と取得時刻を採取票藍D切替0164へ残します。藍D切替0164では警告と致命エラーの混同を避けるため補助資料も照合する判断藍D切替0164です。藍D切替0164の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録藍D切替0164です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0163について構成や状態を確認します。GLVM地理的ミラー VG STATE 0213ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は片側VGのvaryon誤操作を避けるため・主操作で出力欄を評価するして基本ソフトAを照合する。
    - B. 一次資料が示す主目的は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして検証進行率を照合する。
    - C. 一次資料が示す主目的は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして失敗ラベルを照合する。
    - D. 一次資料が示す主目的は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するして構成データOを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能切替・クラス・構成デでDの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・切替）です。照合切替・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・切替・警告とです。比較切替・クラス・構成デ・警告とでA:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸はクラス・切替・構成デです。運用切替・クラスでB:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸は構成デ・クラス・切替です。項目切替・クラス・構成デでC:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は警告と・クラス・構成デです。用語切替・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0163**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0163について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0163A
    ```

    画面・出力には PHA72DD0163A が表示され、クラスタ構成検証 Cluster Topology 0163 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0163
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0163B
    ```

    画面・出力には PHA72DD0163B が表示され、クラスタ構成検証 Cluster Topology 0163 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0163
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0163C
    ```

    画面・出力には PHA72DD0163C が表示され、クラスタ構成検証 Cluster Topology 0163 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0163A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0163B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0163C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0178 {#c25-i0419}
*分類: 構成検証*  ・  難易度: 中級

黒S切替0179ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黒S切替0179です。黒S切替0179はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録黒S切替0179です。黒S切替0179ではODM登録値と取得時刻を採取票黒S切替0179へ残します。黒S切替0179ではノード間ODM差分の残存を避けるため補助資料も照合する判断黒S切替0179です。黒S切替0179の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録黒S切替0179です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0178の役割を調べています。GLVM地理的ミラー syslog entry 0267の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はクラスタートポロジーの構成データODM登録値と取得時刻を記録し・ノード間構成データODM差分の残存を防ぐである。確認操作で状態欄を整理するときはノード間構成データODM差分を防ぐ。 ✅
    - B. 障害切り分けに用いる役割は地理的ミラーの項目のsyslog記録と取得時刻を記録し・syslogとhacmp.outの突合漏れを防ぐである。監査操作で記録欄を比較するときはsyslogとhacmp.oを防ぐ。GLVM地理的ミラー syslog entry 0267固有の属性も確認対象に含める。
    - C. 障害切り分けに用いる役割はクラスタサービスを開始し・リソースグループをオンライン化する操作を起動確認する。属性確認で属性確認を確認するときは属性確認の誤読を防ぐ。
    - D. 障害切り分けに用いる役割は地理的ミラーの項目のVG vary状態と取得時刻を記録し・ミラー再同期条件の誤読を防ぐである。照合操作で確認欄を採取するときはミラー再同期条件の誤読を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能切替・クラス・構成デでAの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・切替）です。照合切替・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・切替・ノードです。運用切替・クラスでB:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は構成デ・クラス・切替です。項目切替・クラス・構成デでC:の起動確認 属性確認は「クラスタサービスを開始し、リソースグループを」を述べるため、正答側の照合軸はノード・クラス・構成デです。仕様切替・クラス・構成デでD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は切替・ノード・構成デです。用語切替・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0178**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0178について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0178A
    ```

    画面・出力には PHA72DD0178A が表示され、クラスタ構成検証 Cluster Topology 0178 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0178
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0178B
    ```

    画面・出力には PHA72DD0178B が表示され、クラスタ構成検証 Cluster Topology 0178 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0178
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0178C
    ```

    画面・出力には PHA72DD0178C が表示され、クラスタ構成検証 Cluster Topology 0178 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0178A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0178B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0178C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0193 {#c25-i0420}
*分類: 構成検証*  ・  難易度: 中級

灰N収集0194ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票灰N収集0194です。灰N収集0194はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録灰N収集0194です。灰N収集0194ではODM登録値と取得時刻を採取票灰N収集0194へ残します。灰N収集0194では未同期構成の見落としを避けるため補助資料も照合する判断灰N収集0194です。灰N収集0194の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録灰N収集0194です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 Cluster Topology 0193」を「リソースグループ制御 Event Summary 0248」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は保護で失敗ラベルを証跡に残し・イベント要約の失敗ラベルと取得時刻を記録し。
    - B. 仕様上の役割はトポロジー確で警告行を証跡に残し・クラスタ構成と状態をスナップショットとして表示するコマンドを。
    - C. 仕様上の役割は収集で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。 ✅
    - D. 仕様上の役割は棚卸で優先ノード一を証跡に残し・資源グループの優先ノード一覧と取得時刻を記録し。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能収集・クラス・構成デでCの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・収集）です。照合収集・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・収集・未同期です。比較収集・クラス・構成デ・未同期でA:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸はクラス・収集・構成デです。運用収集・クラスでB:のトポロジー確認 警告行は「クラスタ構成と状態をスナップショットとして表」を述べるため、正答側の照合軸は構成デ・クラス・収集です。仕様収集・クラス・構成デでD:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は収集・未同期・構成デです。用語収集・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0193**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0193について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0193A
    ```

    画面・出力には PHA72DD0193A が表示され、クラスタ構成検証 Cluster Topology 0193 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0193
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0193B
    ```

    画面・出力には PHA72DD0193B が表示され、クラスタ構成検証 Cluster Topology 0193 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0193
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0193C
    ```

    画面・出力には PHA72DD0193C が表示され、クラスタ構成検証 Cluster Topology 0193 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0193A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0193B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0193C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0208 {#c25-i0421}
*分類: 構成検証*  ・  難易度: 中級

黄I登録0209ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黄I登録0209です。黄I登録0209はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録黄I登録0209です。黄I登録0209ではODM登録値と取得時刻を採取票黄I登録0209へ残します。黄I登録0209では検証ログの採取漏れを避けるため補助資料も照合する判断黄I登録0209です。黄I登録0209の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録黄I登録0209です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0208を同一分類のGLVM地理的ミラー RPV Client 0294と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は地理的ミラーの項目の遠隔ボリュームRPV通信ペアと取得時刻を記録しである。変更確認操作で採取欄を棚卸するときは遠隔ボリュームRPV経路断のを防ぐ。
    - B. コマンドまたは機能の用途は検証後に構成を同期し・クラスタスナップショットを作成する操作をトポロジー確認する。トポロジー確でチューニングを確認するときはチューニングの誤読を防ぐ。
    - C. コマンドまたは機能の用途はクラスタートポロジーの構成データODM登録値と取得時刻を記録し・検証ログの採取漏れを防ぐである。保守操作で監査欄を保存するときは検証ログの採取漏れを防ぐ。 ✅
    - D. コマンドまたは機能の用途は獲得処理の獲得イベントと取得時刻を記録し・資源グループ位置の誤認を防ぐである。復旧操作で点検欄を確認するときは資源グループ位置の誤認を防ぐ。リソースグループ制御 Acquisition Failure 0041固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能登録・クラス・構成デでCの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・登録）です。照合登録・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・登録・検証ロです。比較登録・クラス・構成デ・検証ロでA:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸はクラス・登録・構成デです。運用登録・クラスでB:のトポロジー確認 チューニング値は「検証後に構成を同期し、クラスタスナップショッ」を述べるため、正答側の照合軸は構成デ・クラス・登録です。仕様登録・クラス・構成デでD:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は登録・検証ロ・構成デです。用語登録・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0208**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0208について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0208A
    ```

    画面・出力には PHA72DD0208A が表示され、クラスタ構成検証 Cluster Topology 0208 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0208
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0208B
    ```

    画面・出力には PHA72DD0208B が表示され、クラスタ構成検証 Cluster Topology 0208 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0208
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0208C
    ```

    画面・出力には PHA72DD0208C が表示され、クラスタ構成検証 Cluster Topology 0208 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0208A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0208B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0208C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0223 {#c25-i0422}
*分類: 構成検証*  ・  難易度: 上級

藍D確認0224ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藍D確認0224です。藍D確認0224はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録藍D確認0224です。藍D確認0224ではODM登録値と取得時刻を採取票藍D確認0224へ残します。藍D確認0224では警告と致命エラーの混同を避けるため補助資料も照合する判断藍D確認0224です。藍D確認0224の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録藍D確認0224です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0223の設定や表示を読む前に役割を確認します。リソースグループ制御 Online Node 0239ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は採取操作で照合欄を点検することで構成データOを確認し・警告と致命エラーの混同を防ぐ。 ✅
    - B. 一次資料が示す主目的は表示操作で対象欄を追跡することで資源グループを確認し・獲得失敗ログの未採取を防ぐ。
    - C. 一次資料が示す主目的は開始から終了状態を読むことで開始を確認し・管理設定と資源状態の混同を防ぐ。
    - D. 一次資料が示す主目的は照合操作で確認欄を採取することで遠隔ボリューを確認し・ミラー再同期条件の誤読を防ぐ。GLVM地理的ミラー RPV Client 0084固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能確認・クラス・構成デでAの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・確認）です。照合確認・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・確認・警告とです。運用確認・クラスでB:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は構成デ・クラス・確認です。項目確認・クラス・構成デでC:の通常状態の確認 START01は「Cluster Servicesで開始から」を述べるため、正答側の照合軸は警告と・クラス・構成デです。仕様確認・クラス・構成デでD:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸は確認・警告と・構成デです。用語確認・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0223**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0223について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0223A
    ```

    画面・出力には PHA72DD0223A が表示され、クラスタ構成検証 Cluster Topology 0223 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0223
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0223B
    ```

    画面・出力には PHA72DD0223B が表示され、クラスタ構成検証 Cluster Topology 0223 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0223
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0223C
    ```

    画面・出力には PHA72DD0223C が表示され、クラスタ構成検証 Cluster Topology 0223 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0223A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0223B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0223C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0238 {#c25-i0423}
*分類: 構成検証*  ・  難易度: 上級

黒S確認0239ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黒S確認0239です。黒S確認0239はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録黒S確認0239です。黒S確認0239ではODM登録値と取得時刻を採取票黒S確認0239へ残します。黒S確認0239ではノード間ODM差分の残存を避けるため補助資料も照合する判断黒S確認0239です。黒S確認0239の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録黒S確認0239です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0238に関する障害切り分けの前提を確認しています。リソースグループ制御 Node List 0242の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はノード間構成データODM差分の残を避けるため・確認操作で状態欄を整理するして構成データOを照合する。 ✅
    - B. 障害切り分けに用いる役割は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして移動履歴を照合する。リソースグループ制御 Node List 0242固有の属性も確認対象に含める。
    - C. 障害切り分けに用いる役割は片系定義を全体正本とする誤認を避けるため・検証からVerificationを読むして検証を照合する。
    - D. 障害切り分けに用いる役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するしてトポロジ要約を照合する。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能確認・クラス・構成デでAの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・確認）です。照合確認・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・確認・ノードです。運用確認・クラスでB:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は構成デ・クラス・確認です。項目確認・クラス・構成デでC:の復旧後の確認 TOPO06は「クラスタートポロジーで検証から」を述べるため、正答側の照合軸はノード・クラス・構成デです。仕様確認・クラス・構成デでD:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は確認・ノード・構成デです。用語確認・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0238**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0238について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0238A
    ```

    画面・出力には PHA72DD0238A が表示され、クラスタ構成検証 Cluster Topology 0238 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0238
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0238B
    ```

    画面・出力には PHA72DD0238B が表示され、クラスタ構成検証 Cluster Topology 0238 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0238
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0238C
    ```

    画面・出力には PHA72DD0238C が表示され、クラスタ構成検証 Cluster Topology 0238 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0238A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0238B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0238C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0253 {#c25-i0424}
*分類: 構成検証*  ・  難易度: 初級

灰N保護0254ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票灰N保護0254です。灰N保護0254はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録灰N保護0254です。灰N保護0254ではODM登録値と取得時刻を採取票灰N保護0254へ残します。灰N保護0254では未同期構成の見落としを避けるため補助資料も照合する判断灰N保護0254です。灰N保護0254の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録灰N保護0254です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0253を保守記録に説明する必要があります。GLVM地理的ミラー VG STATE 0273と取り違えない説明はどれですか。

    - A. 仕様上の役割は主操作で出力欄を評価することで基本ソフトAを確認し・片側VGのvaryon誤操作を防ぐ。
    - B. 仕様上の役割は記録操作で証跡欄を照合することで構成データOを確認し・未同期構成の見落としを防ぐ。 ✅
    - C. 仕様上の役割はRG確認からapp_rgを読むことで資源グループを確認し・管理設定と資源状態の混同を防ぐ。
    - D. 仕様上の役割は確認操作で状態欄を整理することでリソース要約を確認し・ノード間構成データODM差分を防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能保護・クラス・構成デでBの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・保護）です。照合保護・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・保護・未同期です。比較保護・クラス・構成デ・未同期でA:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸はクラス・保護・構成デです。項目保護・クラス・構成デでC:の変更後の確認 START03は「Cluster Servicesで資源グルー」を述べるため、正答側の照合軸は未同期・クラス・構成デです。仕様保護・クラス・構成デでD:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸は保護・未同期・構成デです。用語保護・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0253**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0253について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0253A
    ```

    画面・出力には PHA72DD0253A が表示され、クラスタ構成検証 Cluster Topology 0253 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0253
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0253B
    ```

    画面・出力には PHA72DD0253B が表示され、クラスタ構成検証 Cluster Topology 0253 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0253
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0253C
    ```

    画面・出力には PHA72DD0253C が表示され、クラスタ構成検証 Cluster Topology 0253 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0253A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0253B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0253C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0268 {#c25-i0425}
*分類: 構成検証*  ・  難易度: 中級

黄I照合0269ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黄I照合0269です。黄I照合0269はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録黄I照合0269です。黄I照合0269ではODM登録値と取得時刻を採取票黄I照合0269へ残します。黄I照合0269では検証ログの採取漏れを避けるため補助資料も照合する判断黄I照合0269です。黄I照合0269の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録黄I照合0269です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0268の技術的な意味を資料で確認するとき、リソースグループ制御 Online Node 0314との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は解析で資源グループを証跡に残し・オンラインノードの資源グループRG現在位置と取得時刻を記録し。
    - B. コマンドまたは機能の用途は停止確認で同期実行を証跡に残し・Cluster Synchronizで同期実行から。
    - C. コマンドまたは機能の用途は照合で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。 ✅
    - D. コマンドまたは機能の用途は移行でsyslogを証跡に残し・地理的ミラーの項目のsyslog記録と取得時刻を記録し。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能照合・クラス・構成デでCの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・照合）です。照合照合・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・照合・検証ロです。比較照合・クラス・構成デ・検証ロでA:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸はクラス・照合・構成デです。運用照合・クラスでB:の停止前の確認 SYNC14は「Cluster Synchronizで同期実」を述べるため、正答側の照合軸は構成デ・クラス・照合です。仕様照合・クラス・構成デでD:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は照合・検証ロ・構成デです。用語照合・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0268**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0268について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0268A
    ```

    画面・出力には PHA72DD0268A が表示され、クラスタ構成検証 Cluster Topology 0268 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0268
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0268B
    ```

    画面・出力には PHA72DD0268B が表示され、クラスタ構成検証 Cluster Topology 0268 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0268
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0268C
    ```

    画面・出力には PHA72DD0268C が表示され、クラスタ構成検証 Cluster Topology 0268 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0268A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0268B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0268C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0283 {#c25-i0426}
*分類: 構成検証*  ・  難易度: 中級

藍D抑止0284ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藍D抑止0284です。藍D抑止0284はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録藍D抑止0284です。藍D抑止0284ではODM登録値と取得時刻を採取票藍D抑止0284へ残します。藍D抑止0284では警告と致命エラーの混同を避けるため補助資料も照合する判断藍D抑止0284です。藍D抑止0284の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録藍D抑止0284です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0283について構成や状態を確認します。クラスタ構成検証 clverify.log 0292ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして検証報告ROを照合する。
    - B. 一次資料が示す主目的は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するして構成データOを照合する。 ✅
    - C. 一次資料が示す主目的は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして資源グループを照合する。
    - D. 一次資料が示す主目的はsyslogとhacmp.outを避けるため・監査操作で記録欄を比較するして基本ソフトAを照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能抑止・クラス・構成デでBの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・抑止）です。照合抑止・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・抑止・警告とです。比較抑止・クラス・構成デ・警告とでA:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸はクラス・抑止・構成デです。項目抑止・クラス・構成デでC:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は警告と・クラス・構成デです。仕様抑止・クラス・構成デでD:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸は抑止・警告と・構成デです。用語抑止・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0283**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0283について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0283A
    ```

    画面・出力には PHA72DD0283A が表示され、クラスタ構成検証 Cluster Topology 0283 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0283
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0283B
    ```

    画面・出力には PHA72DD0283B が表示され、クラスタ構成検証 Cluster Topology 0283 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0283
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0283C
    ```

    画面・出力には PHA72DD0283C が表示され、クラスタ構成検証 Cluster Topology 0283 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0283A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0283B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0283C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0298 {#c25-i0427}
*分類: 構成検証*  ・  難易度: 中級

黒S抑止0299ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黒S抑止0299です。黒S抑止0299はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録黒S抑止0299です。黒S抑止0299ではODM登録値と取得時刻を採取票黒S抑止0299へ残します。黒S抑止0299ではノード間ODM差分の残存を避けるため補助資料も照合する判断黒S抑止0299です。黒S抑止0299の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録黒S抑止0299です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0298の役割を調べています。lssrc -ls clstrmgrES トポロジー確認 ページング状態の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はトポロジー確でページング状を証跡に残し・Cluster Manager の状態・クラスタ版数。
    - B. 障害切り分けに用いる役割は抑止で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。 ✅
    - C. 障害切り分けに用いる役割は復旧確認でエラー記録を証跡に残し・hacmp.out Eventでエラー記録から。
    - D. 障害切り分けに用いる役割は保守で優先ノード一を証跡に残し・資源グループの優先ノード一覧と取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能抑止・クラス・構成デでBの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・抑止）です。照合抑止・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・抑止・ノードです。比較抑止・クラス・構成デ・ノードでA:のトポロジー確認 ページング状態は「Cluster Manager の状態」を述べるため、正答側の照合軸はクラス・抑止・構成デです。項目抑止・クラス・構成デでC:の復旧後の確認 FAIL06は「hacmp.out Eventでエラー記録か」を述べるため、正答側の照合軸はノード・クラス・構成デです。仕様抑止・クラス・構成デでD:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は抑止・ノード・構成デです。用語抑止・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0298**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0298について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0298A
    ```

    画面・出力には PHA72DD0298A が表示され、クラスタ構成検証 Cluster Topology 0298 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0298
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0298B
    ```

    画面・出力には PHA72DD0298B が表示され、クラスタ構成検証 Cluster Topology 0298 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0298
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0298C
    ```

    画面・出力には PHA72DD0298C が表示され、クラスタ構成検証 Cluster Topology 0298 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0298A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0298B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0298C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0313 {#c25-i0428}
*分類: 構成検証*  ・  難易度: 中級

灰N解析0314ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票灰N解析0314です。灰N解析0314はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録灰N解析0314です。灰N解析0314ではODM登録値と取得時刻を採取票灰N解析0314へ残します。灰N解析0314では未同期構成の見落としを避けるため補助資料も照合する判断灰N解析0314です。灰N解析0314の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録灰N解析0314です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 Cluster Topology 0313」を「clstat -o 状態確認 出力見出し」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は状態確認で出力見出しを証跡に残し・クラスタ・ノード・インターフェース・リソースグループの状態を。
    - B. 仕様上の役割は復旧で獲得イベントを証跡に残し・獲得処理の獲得イベントと取得時刻を記録し。
    - C. 仕様上の役割は解析で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。 ✅
    - D. 仕様上の役割は切替でsyslogを証跡に残し・地理的ミラーの項目のsyslog記録と取得時刻を記録し。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能解析・クラス・構成デでCの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・解析）です。照合解析・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・解析・未同期です。比較解析・クラス・構成デ・未同期でA:の状態確認 出力見出しは「クラスタ、ノード、インターフェース」を述べるため、正答側の照合軸はクラス・解析・構成デです。運用解析・クラスでB:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は構成デ・クラス・解析です。仕様解析・クラス・構成デでD:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は解析・未同期・構成デです。用語解析・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0313**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0313について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0313A
    ```

    画面・出力には PHA72DD0313A が表示され、クラスタ構成検証 Cluster Topology 0313 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0313
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0313B
    ```

    画面・出力には PHA72DD0313B が表示され、クラスタ構成検証 Cluster Topology 0313 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0313
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0313C
    ```

    画面・出力には PHA72DD0313C が表示され、クラスタ構成検証 Cluster Topology 0313 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0313A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0313B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0313C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0328 {#c25-i0429}
*分類: 構成検証*  ・  難易度: 中級

黄I計画0329ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黄I計画0329です。黄I計画0329はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録黄I計画0329です。黄I計画0329ではODM登録値と取得時刻を採取票黄I計画0329へ残します。黄I計画0329では検証ログの採取漏れを避けるため補助資料も照合する判断黄I計画0329です。黄I計画0329の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録黄I計画0329です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0328を同一分類のGLVM地理的ミラー RPV Client 0354と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は計画で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。 ✅
    - B. コマンドまたは機能の用途は解除で遠隔ボリューを証跡に残し・地理的ミラーの項目の遠隔ボリュームRPV通信ペアと取得時刻を。GLVM地理的ミラー RPV Client 0354固有の属性も確認対象に含める。
    - C. コマンドまたは機能の用途は復旧で獲得イベントを証跡に残し・獲得処理の獲得イベントと取得時刻を記録し。
    - D. コマンドまたは機能の用途は切替でミラー更新状を証跡に残し・地理的ミラーの項目のミラー更新状態と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能計画・クラス・構成デでAの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・計画）です。照合計画・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・計画・検証ロです。運用計画・クラスでB:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸は構成デ・クラス・計画です。項目計画・クラス・構成デでC:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は検証ロ・クラス・構成デです。仕様計画・クラス・構成デでD:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は計画・検証ロ・構成デです。用語計画・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0328**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0328について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0328A
    ```

    画面・出力には PHA72DD0328A が表示され、クラスタ構成検証 Cluster Topology 0328 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0328
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0328B
    ```

    画面・出力には PHA72DD0328B が表示され、クラスタ構成検証 Cluster Topology 0328 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0328
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0328C
    ```

    画面・出力には PHA72DD0328C が表示され、クラスタ構成検証 Cluster Topology 0328 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0328A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0328B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0328C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0343 {#c25-i0430}
*分類: 構成検証*  ・  難易度: 上級

藍D解除0344ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票藍D解除0344です。藍D解除0344はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録藍D解除0344です。藍D解除0344ではODM登録値と取得時刻を採取票藍D解除0344へ残します。藍D解除0344では警告と致命エラーの混同を避けるため補助資料も照合する判断藍D解除0344です。藍D解除0344の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録藍D解除0344です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0343の設定や表示を読む前に役割を確認します。clmgr sync cluster 起動確認 経路確認ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は経路確認の誤読を避けるため・経路確認で経路確認を確認するして経路確認を照合する。
    - B. 一次資料が示す主目的は依存順を無視して子資源を先にオンを避けるため・イベント順序からcompletedを読むしてイベント順序を照合する。
    - C. 一次資料が示す主目的は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するして構成データOを照合する。 ✅
    - D. 一次資料が示す主目的は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして資源グループを照合する。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能解除・クラス・構成デでCの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・解除）です。照合解除・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・解除・警告とです。比較解除・クラス・構成デ・警告とでA:の起動確認 経路確認は「検証後に構成を同期し、クラスタスナップショッ」を述べるため、正答側の照合軸はクラス・解除・構成デです。運用解除・クラスでB:の変更後の確認 DEP03は「資源グループでイベント順序から」を述べるため、正答側の照合軸は構成デ・クラス・解除です。仕様解除・クラス・構成デでD:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は解除・警告と・構成デです。用語解除・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0343**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0343について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0343A
    ```

    画面・出力には PHA72DD0343A が表示され、クラスタ構成検証 Cluster Topology 0343 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0343
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0343B
    ```

    画面・出力には PHA72DD0343B が表示され、クラスタ構成検証 Cluster Topology 0343 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0343
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0343C
    ```

    画面・出力には PHA72DD0343C が表示され、クラスタ構成検証 Cluster Topology 0343 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0343A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0343B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0343C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0358 {#c25-i0431}
*分類: 構成検証*  ・  難易度: 上級

黒S解除0359ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黒S解除0359です。黒S解除0359はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録黒S解除0359です。黒S解除0359ではODM登録値と取得時刻を採取票黒S解除0359へ残します。黒S解除0359ではノード間ODM差分の残存を避けるため補助資料も照合する判断黒S解除0359です。黒S解除0359の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録黒S解除0359です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0358に関する障害切り分けの前提を確認しています。clmgr query node 起動確認 エラー詳細の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はノードの状態と raw_state を確認するコマンドを起動確認する。起動確認でエラー詳細を確認するときはエラー詳細の誤読を防ぐ。
    - B. 障害切り分けに用いる役割はクラスタートポロジーの構成データODM登録値と取得時刻を記録し・ノード間構成データODM差分の残存を防ぐである。確認操作で状態欄を整理するときはノード間構成データODM差分を防ぐ。 ✅
    - C. 障害切り分けに用いる役割はclverify.logの検証報告ROHAレポートと取得時刻を記録し・警告と致命エラーの混同を防ぐである。採取操作で照合欄を点検するときは警告と致命エラーの混同を防ぐ。
    - D. 障害切り分けに用いる役割は地理的ミラーの項目のミラー更新状態と取得時刻を記録し・ミラー再同期条件の誤読を防ぐである。照合操作で確認欄を採取するときはミラー再同期条件の誤読を防ぐ。GLVM地理的ミラー RPV Server 0216固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能解除・クラス・構成デでBの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・解除）です。照合解除・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・解除・ノードです。比較解除・クラス・構成デ・ノードでA:の起動確認 エラー詳細は「ノードの状態と raw_state」を述べるため、正答側の照合軸はクラス・解除・構成デです。項目解除・クラス・構成デでC:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸はノード・クラス・構成デです。仕様解除・クラス・構成デでD:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は解除・ノード・構成デです。用語解除・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0358**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0358について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Topology と ODM登録値
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clodmget HACMPdynresop
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0358A
    ```

    画面・出力には PHA72DD0358A が表示され、クラスタ構成検証 Cluster Topology 0358 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0358
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0358B
    ```

    画面・出力には PHA72DD0358B が表示され、クラスタ構成検証 Cluster Topology 0358 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Topology を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0358
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0358C
    ```

    画面・出力には PHA72DD0358C が表示され、クラスタ構成検証 Cluster Topology 0358 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0358A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0358B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0358C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0004 {#c25-i0432}
*分類: 構成検証*  ・  難易度: 初級

紅E巡回0005ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紅E巡回0005です。紅E巡回0005はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録紅E巡回0005です。紅E巡回0005では検証進行率と取得時刻を採取票紅E巡回0005へ残します。紅E巡回0005では検証ログの採取漏れを避けるため補助資料も照合する判断紅E巡回0005です。紅E巡回0005の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録紅E巡回0005です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0004の技術的な意味を資料で確認するとき、GLVM地理的ミラー RPV Server 0081との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は主操作で出力欄を評価することでミラー更新状を確認し・片側VGのvaryon誤操作を防ぐ。
    - B. コマンドまたは機能の用途は点検操作で判定欄を記録することで資源グループを確認し・依存リソース順序の見落としを防ぐ。
    - C. コマンドまたは機能の用途は保守操作で監査欄を保存することで検証進行率を確認し・検証ログの採取漏れを防ぐ。 ✅
    - D. コマンドまたは機能の用途はノード一覧から実状態値を読むことでノード一覧を確認し・基本ソフト稼働とクラスタ稼働を防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能巡回・クラス・検証進でCの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・巡回）です。照合巡回・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・巡回・検証ロです。比較クラス・巡回でA:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸はシステ・巡回・検証進です。運用巡回・システでB:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は検証進・クラス・巡回です。仕様巡回・クラス・検証進でD:の障害切り分け NODE04は「PowerHA Node Stateでノード」を述べるため、正答側の照合軸は巡回・検証ロ・検証進です。用語巡回・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0004**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0004について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0004A
    ```

    画面・出力には PHA72DD0004A が表示され、クラスタ構成検証 SMIT Command Status 0004 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0004
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0004B
    ```

    画面・出力には PHA72DD0004B が表示され、クラスタ構成検証 SMIT Command Status 0004 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0004
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0004C
    ```

    画面・出力には PHA72DD0004C が表示され、クラスタ構成検証 SMIT Command Status 0004 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0004A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0004B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0004C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0019 {#c25-i0433}
*分類: 構成検証*  ・  難易度: 初級

空T巡回0020ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票空T巡回0020です。空T巡回0020はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録空T巡回0020です。空T巡回0020では検証進行率と取得時刻を採取票空T巡回0020へ残します。空T巡回0020では警告と致命エラーの混同を避けるため補助資料も照合する判断空T巡回0020です。空T巡回0020の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録空T巡回0020です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0019について構成や状態を確認します。GLVM地理的ミラー VG STATE 0078ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は地理的ミラーの項目の基本ソフトAIXエラー識別子と取得時刻を記録しである。変更確認操作で採取欄を棚卸するときは遠隔ボリュームRPV経路断のを防ぐ。
    - B. 一次資料が示す主目的はオンラインノードの資源グループRG現在位置と取得時刻を記録し・資源グループ位置の誤認を防ぐである。復旧操作で点検欄を確認するときは資源グループ位置の誤認を防ぐ。
    - C. 一次資料が示す主目的はクラスタトポロジー・ネットワーク・サービスIP・リソースグループを表示するコマンドを整合確認する。確認範囲で確認範囲を確認するときは確認範囲の誤読を防ぐ。
    - D. 一次資料が示す主目的はシステム管理コマンドの検証進行率と取得時刻を記録し・警告と致命エラーの混同を防ぐである。採取操作で照合欄を点検するときは警告と致命エラーの混同を防ぐ。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能巡回・クラス・検証進でDの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・巡回）です。照合巡回・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・巡回・警告とです。比較クラス・巡回でA:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸はシステ・巡回・検証進です。運用巡回・システでB:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は検証進・クラス・巡回です。項目巡回・クラス・検証進でC:の整合確認 確認範囲は「クラスタトポロジー、ネットワーク」を述べるため、正答側の照合軸は警告と・クラス・検証進です。用語巡回・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0019**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0019について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0019A
    ```

    画面・出力には PHA72DD0019A が表示され、クラスタ構成検証 SMIT Command Status 0019 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0019
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0019B
    ```

    画面・出力には PHA72DD0019B が表示され、クラスタ構成検証 SMIT Command Status 0019 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0019
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0019C
    ```

    画面・出力には PHA72DD0019C が表示され、クラスタ構成検証 SMIT Command Status 0019 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0019A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0019B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0019C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0034 {#c25-i0434}
*分類: 構成検証*  ・  難易度: 中級

翠O棚卸0035ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票翠O棚卸0035です。翠O棚卸0035はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録翠O棚卸0035です。翠O棚卸0035では検証進行率と取得時刻を採取票翠O棚卸0035へ残します。翠O棚卸0035ではノード間ODM差分の残存を避けるため補助資料も照合する判断翠O棚卸0035です。翠O棚卸0035の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録翠O棚卸0035です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0034の役割を調べています。リソースグループ制御 Node List 0107の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は表示操作で対象欄を追跡することで移動履歴を確認し・獲得失敗ログの未採取を防ぐ。
    - B. 障害切り分けに用いる役割は確認操作で状態欄を整理することで検証進行率を確認し・ノード間構成データODM差分を防ぐ。 ✅
    - C. 障害切り分けに用いる役割は点検操作で判定欄を記録することで失敗ラベルを確認し・依存リソース順序の見落としを防ぐ。リソースグループ制御 Event Summary 0218固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割は開始から終了状態を読むことで開始を確認し・管理設定と資源状態の混同を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能棚卸・クラス・検証進でBの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・棚卸）です。照合棚卸・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・棚卸・ノードです。比較クラス・棚卸でA:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸はシステ・棚卸・検証進です。項目棚卸・クラス・検証進でC:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸はノード・クラス・検証進です。仕様棚卸・クラス・検証進でD:の依存関係の確認 START13は「Cluster Servicesで開始から」を述べるため、正答側の照合軸は棚卸・ノード・検証進です。用語棚卸・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0034**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0034について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0034A
    ```

    画面・出力には PHA72DD0034A が表示され、クラスタ構成検証 SMIT Command Status 0034 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0034
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0034B
    ```

    画面・出力には PHA72DD0034B が表示され、クラスタ構成検証 SMIT Command Status 0034 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0034
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0034C
    ```

    画面・出力には PHA72DD0034C が表示され、クラスタ構成検証 SMIT Command Status 0034 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0034A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0034B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0034C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0049 {#c25-i0435}
*分類: 構成検証*  ・  難易度: 中級

朱J復旧0050ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票朱J復旧0050です。朱J復旧0050はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録朱J復旧0050です。朱J復旧0050では検証進行率と取得時刻を採取票朱J復旧0050へ残します。朱J復旧0050では未同期構成の見落としを避けるため補助資料も照合する判断朱J復旧0050です。朱J復旧0050の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録朱J復旧0050です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 SMIT Command Status 0049」を「リソースグループ制御 Event Summary 0053」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は復旧で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。 ✅
    - B. 仕様上の役割は復旧で失敗ラベルを証跡に残し・イベント要約の失敗ラベルと取得時刻を記録し。
    - C. 仕様上の役割は抑止で獲得イベントを証跡に残し・獲得処理の獲得イベントと取得時刻を記録し。
    - D. 仕様上の役割は所有先確認で依存関係を証跡に残し・クラスタサービスを開始し・リソースグループをオンライン化する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能復旧・クラス・検証進でAの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・復旧）です。照合復旧・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・復旧・未同期です。運用復旧・システでB:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は検証進・クラス・復旧です。項目復旧・クラス・検証進でC:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は未同期・クラス・検証進です。仕様復旧・クラス・検証進でD:の所有先確認 依存関係は「クラスタサービスを開始し、リソースグループを」を述べるため、正答側の照合軸は復旧・未同期・検証進です。用語復旧・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0049**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0049について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0049A
    ```

    画面・出力には PHA72DD0049A が表示され、クラスタ構成検証 SMIT Command Status 0049 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0049
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0049B
    ```

    画面・出力には PHA72DD0049B が表示され、クラスタ構成検証 SMIT Command Status 0049 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0049
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0049C
    ```

    画面・出力には PHA72DD0049C が表示され、クラスタ構成検証 SMIT Command Status 0049 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0049A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0049B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0049C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0064 {#c25-i0436}
*分類: 構成検証*  ・  難易度: 中級

紅E監査0065ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紅E監査0065です。紅E監査0065はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録紅E監査0065です。紅E監査0065では検証進行率と取得時刻を採取票紅E監査0065へ残します。紅E監査0065では検証ログの採取漏れを避けるため補助資料も照合する判断紅E監査0065です。紅E監査0065の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録紅E監査0065です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0064を同一分類のクラスタ構成検証 Cluster Topology 0103と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するして構成データOを照合する。
    - B. コマンドまたは機能の用途は遠隔ボリュームRPV経路断の見落を避けるため・変更確認操作で採取欄を棚卸するして遠隔ボリューを照合する。
    - C. コマンドまたは機能の用途は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして検証進行率を照合する。 ✅
    - D. コマンドまたは機能の用途は基本ソフト稼働とクラスタ稼働の混を避けるため・ノード一覧から実状態値を読むしてノード一覧を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能監査・クラス・検証進でCの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・監査）です。照合監査・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・監査・検証ロです。比較クラス・監査でA:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸はシステ・監査・検証進です。運用監査・システでB:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸は検証進・クラス・監査です。仕様監査・クラス・検証進でD:の障害切り分け NODE04は「PowerHA Node Stateでノード」を述べるため、正答側の照合軸は監査・検証ロ・検証進です。用語監査・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0064**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0064について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0064A
    ```

    画面・出力には PHA72DD0064A が表示され、クラスタ構成検証 SMIT Command Status 0064 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0064
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0064B
    ```

    画面・出力には PHA72DD0064B が表示され、クラスタ構成検証 SMIT Command Status 0064 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0064
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0064C
    ```

    画面・出力には PHA72DD0064C が表示され、クラスタ構成検証 SMIT Command Status 0064 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0064A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0064B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0064C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0079 {#c25-i0437}
*分類: 構成検証*  ・  難易度: 中級

空T監査0080ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票空T監査0080です。空T監査0080はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録空T監査0080です。空T監査0080では検証進行率と取得時刻を採取票空T監査0080へ残します。空T監査0080では警告と致命エラーの混同を避けるため補助資料も照合する判断空T監査0080です。空T監査0080の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録空T監査0080です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0079の設定や表示を読む前に役割を確認します。リソースグループ制御 Event Summary 0128ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして失敗ラベルを照合する。
    - B. 一次資料が示す主目的は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして優先ノード一を照合する。
    - C. 一次資料が示す主目的は片系定義を全体正本とする誤認を避けるため・検証からVerificationを読むして検証を照合する。
    - D. 一次資料が示す主目的は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するして検証進行率を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能監査・クラス・検証進でDの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・監査）です。照合監査・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・監査・警告とです。比較クラス・監査でA:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸はシステ・監査・検証進です。運用監査・システでB:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は検証進・クラス・監査です。項目監査・クラス・検証進でC:の復旧後の確認 TOPO06は「クラスタートポロジーで検証から」を述べるため、正答側の照合軸は警告と・クラス・検証進です。用語監査・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0079**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0079について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0079A
    ```

    画面・出力には PHA72DD0079A が表示され、クラスタ構成検証 SMIT Command Status 0079 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0079
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0079B
    ```

    画面・出力には PHA72DD0079B が表示され、クラスタ構成検証 SMIT Command Status 0079 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0079
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0079C
    ```

    画面・出力には PHA72DD0079C が表示され、クラスタ構成検証 SMIT Command Status 0079 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0079A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0079B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0079C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0094 {#c25-i0438}
*分類: 構成検証*  ・  難易度: 中級

翠O変更0095ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票翠O変更0095です。翠O変更0095はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録翠O変更0095です。翠O変更0095では検証進行率と取得時刻を採取票翠O変更0095へ残します。翠O変更0095ではノード間ODM差分の残存を避けるため補助資料も照合する判断翠O変更0095です。翠O変更0095の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録翠O変更0095です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0094に関する障害切り分けの前提を確認しています。GLVM地理的ミラー Mirror Pool 0120の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は変更で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。 ✅
    - B. 障害切り分けに用いる役割は診断でVG varを証跡に残し・地理的ミラーの項目のVG vary状態と取得時刻を記録し。
    - C. 障害切り分けに用いる役割は解析で移動履歴を証跡に残し・ノード一覧の移動履歴と取得時刻を記録し。
    - D. 障害切り分けに用いる役割は変更確認でエラー記録を証跡に残し・hacmp.out Eventでエラー記録から。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能変更・クラス・検証進でAの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・変更）です。照合変更・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・変更・ノードです。運用変更・システでB:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は検証進・クラス・変更です。項目変更・クラス・検証進でC:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸はノード・クラス・検証進です。仕様変更・クラス・検証進でD:の変更後の確認 FAIL03は「hacmp.out Eventでエラー記録か」を述べるため、正答側の照合軸は変更・ノード・検証進です。用語変更・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0094**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0094について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0094A
    ```

    画面・出力には PHA72DD0094A が表示され、クラスタ構成検証 SMIT Command Status 0094 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0094
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0094B
    ```

    画面・出力には PHA72DD0094B が表示され、クラスタ構成検証 SMIT Command Status 0094 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0094
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0094C
    ```

    画面・出力には PHA72DD0094C が表示され、クラスタ構成検証 SMIT Command Status 0094 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0094A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0094B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0094C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0109 {#c25-i0439}
*分類: 構成検証*  ・  難易度: 上級

朱J移行0110ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票朱J移行0110です。朱J移行0110はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録朱J移行0110です。朱J移行0110では検証進行率と取得時刻を採取票朱J移行0110へ残します。朱J移行0110では未同期構成の見落としを避けるため補助資料も照合する判断朱J移行0110です。朱J移行0110の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録朱J移行0110です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0109を保守記録に説明する必要があります。GLVM地理的ミラー RPV Server 0156と取り違えない説明はどれですか。

    - A. 仕様上の役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして検証進行率を照合する。 ✅
    - B. 仕様上の役割はミラー再同期条件の誤読を避けるため・照合操作で確認欄を採取するしてミラー更新状を照合する。
    - C. 仕様上の役割は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するしてリソース要約を照合する。
    - D. 仕様上の役割は依存順を無視して子資源を先にオンを避けるため・イベント順序からcompletedを読むしてイベント順序を照合する。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能移行・クラス・検証進でAの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・移行）です。照合移行・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・移行・未同期です。運用移行・システでB:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は検証進・クラス・移行です。項目移行・クラス・検証進でC:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸は未同期・クラス・検証進です。仕様移行・クラス・検証進でD:の変更後の確認 DEP03は「資源グループでイベント順序から」を述べるため、正答側の照合軸は移行・未同期・検証進です。用語移行・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0109**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0109について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0109A
    ```

    画面・出力には PHA72DD0109A が表示され、クラスタ構成検証 SMIT Command Status 0109 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0109
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0109B
    ```

    画面・出力には PHA72DD0109B が表示され、クラスタ構成検証 SMIT Command Status 0109 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0109
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0109C
    ```

    画面・出力には PHA72DD0109C が表示され、クラスタ構成検証 SMIT Command Status 0109 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0109A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0109B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0109C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0124 {#c25-i0440}
*分類: 構成検証*  ・  難易度: 初級

紅E診断0125ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紅E診断0125です。紅E診断0125はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録紅E診断0125です。紅E診断0125では検証進行率と取得時刻を採取票紅E診断0125へ残します。紅E診断0125では検証ログの採取漏れを避けるため補助資料も照合する判断紅E診断0125です。紅E診断0125の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録紅E診断0125です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0124の技術的な意味を資料で確認するとき、GLVM地理的ミラー syslog entry 0162との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は保守操作で監査欄を保存することで検証進行率を確認し・検証ログの採取漏れを防ぐ。 ✅
    - B. コマンドまたは機能の用途は変更確認操作で採取欄を棚卸することでsyslogを確認し・遠隔ボリュームRPV経路断のを防ぐ。
    - C. コマンドまたは機能の用途は表示操作で対象欄を追跡することで失敗ラベルを確認し・獲得失敗ログの未採取を防ぐ。
    - D. コマンドまたは機能の用途はマネージャーログからクラスター管理プロセことでマネージャーを確認し・cluster historを防ぐ。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能診断・クラス・検証進でAの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・診断）です。照合診断・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・診断・検証ロです。運用診断・システでB:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は検証進・クラス・診断です。項目診断・クラス・検証進でC:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は検証ロ・クラス・検証進です。仕様診断・クラス・検証進でD:の性能影響の確認 FAIL11は「hacmp.out Eventでマネージャー」を述べるため、正答側の照合軸は診断・検証ロ・検証進です。用語診断・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0124**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0124について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0124A
    ```

    画面・出力には PHA72DD0124A が表示され、クラスタ構成検証 SMIT Command Status 0124 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0124
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0124B
    ```

    画面・出力には PHA72DD0124B が表示され、クラスタ構成検証 SMIT Command Status 0124 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0124
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0124C
    ```

    画面・出力には PHA72DD0124C が表示され、クラスタ構成検証 SMIT Command Status 0124 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0124A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0124B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0124C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0139 {#c25-i0441}
*分類: 構成検証*  ・  難易度: 初級

空T診断0140ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票空T診断0140です。空T診断0140はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録空T診断0140です。空T診断0140では検証進行率と取得時刻を採取票空T診断0140へ残します。空T診断0140では警告と致命エラーの混同を避けるため補助資料も照合する判断空T診断0140です。空T診断0140の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録空T診断0140です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0139について構成や状態を確認します。GLVM地理的ミラー RPV Server 0141ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は保守でミラー更新状を証跡に残し・地理的ミラーの項目のミラー更新状態と取得時刻を記録し。
    - B. 一次資料が示す主目的は診断で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。 ✅
    - C. 一次資料が示す主目的はログ採取でログ採取を証跡に残し・検証後に構成を同期し・クラスタスナップショットを作成する操作。
    - D. 一次資料が示す主目的は棚卸でリソース要約を証跡に残し・構成検証のリソース要約と取得時刻を記録し。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能診断・クラス・検証進でBの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・診断）です。照合診断・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・診断・警告とです。比較診断・クラス・検証進・警告とでA:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸はシステ・診断・検証進です。項目診断・クラス・検証進でC:の同期確認 ログ採取は「検証後に構成を同期し、クラスタスナップショッ」を述べるため、正答側の照合軸は警告と・クラス・検証進です。仕様診断・クラス・検証進でD:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸は診断・警告と・検証進です。用語診断・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0139**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0139について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0139A
    ```

    画面・出力には PHA72DD0139A が表示され、クラスタ構成検証 SMIT Command Status 0139 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0139
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0139B
    ```

    画面・出力には PHA72DD0139B が表示され、クラスタ構成検証 SMIT Command Status 0139 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0139
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0139C
    ```

    画面・出力には PHA72DD0139C が表示され、クラスタ構成検証 SMIT Command Status 0139 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0139A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0139B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0139C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0154 {#c25-i0442}
*分類: 構成検証*  ・  難易度: 中級

翠O保守0155ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票翠O保守0155です。翠O保守0155はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録翠O保守0155です。翠O保守0155では検証進行率と取得時刻を採取票翠O保守0155へ残します。翠O保守0155ではノード間ODM差分の残存を避けるため補助資料も照合する判断翠O保守0155です。翠O保守0155の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録翠O保守0155です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0154の役割を調べています。クラスタ構成検証 Verification Progress 0226の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は確認操作で状態欄を整理することでリソース要約を確認し・ノード間構成データODM差分を防ぐ。
    - B. 障害切り分けに用いる役割は同期確認で受信先を確認することで受信先を確認し・受信先の誤読を防ぐ。
    - C. 障害切り分けに用いる役割は確認操作で状態欄を整理することで検証進行率を確認し・ノード間構成データODM差分を防ぐ。 ✅
    - D. 障害切り分けに用いる役割は採取操作で照合欄を点検することで検証報告ROを確認し・警告と致命エラーの混同を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能保守・クラス・検証進でCの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・保守）です。照合保守・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・保守・ノードです。比較保守・クラス・検証進・ノードでA:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸はシステ・保守・検証進です。運用保守・システでB:の同期確認 受信先は「クラスタ構成と状態をスナップショットとして表」を述べるため、正答側の照合軸は検証進・クラス・保守です。仕様保守・クラス・検証進でD:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸は保守・ノード・検証進です。用語保守・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0154**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0154について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0154A
    ```

    画面・出力には PHA72DD0154A が表示され、クラスタ構成検証 SMIT Command Status 0154 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0154
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0154B
    ```

    画面・出力には PHA72DD0154B が表示され、クラスタ構成検証 SMIT Command Status 0154 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0154
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0154C
    ```

    画面・出力には PHA72DD0154C が表示され、クラスタ構成検証 SMIT Command Status 0154 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0154A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0154B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0154C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0169 {#c25-i0443}
*分類: 構成検証*  ・  難易度: 中級

朱J切替0170ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票朱J切替0170です。朱J切替0170はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録朱J切替0170です。朱J切替0170では検証進行率と取得時刻を採取票朱J切替0170へ残します。朱J切替0170では未同期構成の見落としを避けるため補助資料も照合する判断朱J切替0170です。朱J切替0170の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録朱J切替0170です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 SMIT Command Status 0169」を「GLVM地理的ミラー RPV Server 0231」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は地理的ミラーの項目のミラー更新状態と取得時刻を記録し・syslogとhacmp.outの突合漏れを防ぐである。監査操作で記録欄を比較するときはsyslogとhacmp.oを防ぐ。
    - B. 仕様上の役割はリソースグループの状態と所有ノードを表示するコマンドである。同期処理で識別値を確認するときは識別値の誤読を防ぐ。
    - C. 仕様上の役割は地理的ミラーの項目のsyslog記録と取得時刻を記録し・ミラー再同期条件の誤読を防ぐである。照合操作で確認欄を採取するときはミラー再同期条件の誤読を防ぐ。
    - D. 仕様上の役割はシステム管理コマンドの検証進行率と取得時刻を記録し・未同期構成の見落としを防ぐである。記録操作で証跡欄を照合するときは未同期構成の見落としを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能切替・クラス・検証進でDの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・切替）です。照合切替・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・切替・未同期です。比較切替・クラス・検証進・未同期でA:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸はシステ・切替・検証進です。運用切替・システでB:の障害切り分け 識別値は「リソースグループの状態と所有ノードを表示する」を述べるため、正答側の照合軸は検証進・クラス・切替です。項目切替・クラス・検証進でC:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は未同期・クラス・検証進です。用語切替・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0169**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0169について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0169A
    ```

    画面・出力には PHA72DD0169A が表示され、クラスタ構成検証 SMIT Command Status 0169 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0169
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0169B
    ```

    画面・出力には PHA72DD0169B が表示され、クラスタ構成検証 SMIT Command Status 0169 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0169
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0169C
    ```

    画面・出力には PHA72DD0169C が表示され、クラスタ構成検証 SMIT Command Status 0169 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0169A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0169B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0169C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0184 {#c25-i0444}
*分類: 構成検証*  ・  難易度: 中級

紅E収集0185ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紅E収集0185です。紅E収集0185はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録紅E収集0185です。紅E収集0185では検証進行率と取得時刻を採取票紅E収集0185へ残します。紅E収集0185では検証ログの採取漏れを避けるため補助資料も照合する判断紅E収集0185です。紅E収集0185の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録紅E収集0185です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0184を同一分類のリソースグループ制御 Acquisition Failure 0206と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして検証進行率を照合する。 ✅
    - B. コマンドまたは機能の用途は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして獲得イベントを照合する。
    - C. コマンドまたは機能の用途は基本ソフト稼働とクラスタ稼働の混を避けるため・ノード一覧から実状態値を読むしてノード一覧を照合する。
    - D. コマンドまたは機能の用途はsyslogとhacmp.outを避けるため・監査操作で記録欄を比較するしてVG varを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能収集・クラス・検証進でAの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・収集）です。照合収集・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・収集・検証ロです。運用収集・システでB:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は検証進・クラス・収集です。項目収集・クラス・検証進でC:の依存関係の確認 NODE13は「PowerHA Node Stateでノード」を述べるため、正答側の照合軸は検証ロ・クラス・検証進です。仕様収集・クラス・検証進でD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は収集・検証ロ・検証進です。用語収集・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0184**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0184について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0184A
    ```

    画面・出力には PHA72DD0184A が表示され、クラスタ構成検証 SMIT Command Status 0184 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0184
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0184B
    ```

    画面・出力には PHA72DD0184B が表示され、クラスタ構成検証 SMIT Command Status 0184 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0184
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0184C
    ```

    画面・出力には PHA72DD0184C が表示され、クラスタ構成検証 SMIT Command Status 0184 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0184A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0184B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0184C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0199 {#c25-i0445}
*分類: 構成検証*  ・  難易度: 中級

空T収集0200ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票空T収集0200です。空T収集0200はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録空T収集0200です。空T収集0200では検証進行率と取得時刻を採取票空T収集0200へ残します。空T収集0200では警告と致命エラーの混同を避けるため補助資料も照合する判断空T収集0200です。空T収集0200の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録空T収集0200です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0199の設定や表示を読む前に役割を確認します。リソースグループ制御 Online Node 0284ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するして検証進行率を照合する。 ✅
    - B. 一次資料が示す主目的は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして資源グループを照合する。
    - C. 一次資料が示す主目的は資料見出しの誤読を避けるため・トポロジー確で資料見出しを確認するして資料見出しを照合する。
    - D. 一次資料が示す主目的は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして検証報告ROを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能収集・クラス・検証進でAの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・収集）です。照合収集・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・収集・警告とです。運用収集・システでB:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は検証進・クラス・収集です。項目収集・クラス・検証進でC:のトポロジー確認 資料見出しは「クラスタ名、状態、バージョンなどのクラスタ属」を述べるため、正答側の照合軸は警告と・クラス・検証進です。仕様収集・クラス・検証進でD:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸は収集・警告と・検証進です。用語収集・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0199**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0199について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0199A
    ```

    画面・出力には PHA72DD0199A が表示され、クラスタ構成検証 SMIT Command Status 0199 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0199
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0199B
    ```

    画面・出力には PHA72DD0199B が表示され、クラスタ構成検証 SMIT Command Status 0199 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0199
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0199C
    ```

    画面・出力には PHA72DD0199C が表示され、クラスタ構成検証 SMIT Command Status 0199 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0199A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0199B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0199C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0214 {#c25-i0446}
*分類: 構成検証*  ・  難易度: 中級

翠O登録0215ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票翠O登録0215です。翠O登録0215はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録翠O登録0215です。翠O登録0215では検証進行率と取得時刻を採取票翠O登録0215へ残します。翠O登録0215ではノード間ODM差分の残存を避けるため補助資料も照合する判断翠O登録0215です。翠O登録0215の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録翠O登録0215です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0214に関する障害切り分けの前提を確認しています。GLVM地理的ミラー RPV Client 0234の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は地理的ミラーの項目の遠隔ボリュームRPV通信ペアと取得時刻を記録しである。変更確認操作で採取欄を棚卸するときは遠隔ボリュームRPV経路断のを防ぐ。
    - B. 障害切り分けに用いる役割はシステム管理コマンドの検証進行率と取得時刻を記録し・ノード間構成データODM差分の残存を防ぐである。確認操作で状態欄を整理するときはノード間構成データODM差分を防ぐ。 ✅
    - C. 障害切り分けに用いる役割はCluster Servicesで資源グループRG確認から app_rg を読み・app_rg とである。RG確認からapp_rgを読むときは管理設定と資源状態の混同を防ぐ。
    - D. 障害切り分けに用いる役割は地理的ミラーの項目のVG vary状態と取得時刻を記録し・syslogとhacmp.outの突合漏れを防ぐである。監査操作で記録欄を比較するときはsyslogとhacmp.oを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能登録・クラス・検証進でBの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・登録）です。照合登録・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・登録・ノードです。比較登録・クラス・検証進・ノードでA:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸はシステ・登録・検証進です。項目登録・クラス・検証進でC:の変更後の確認 START03は「Cluster Servicesで資源グルー」を述べるため、正答側の照合軸はノード・クラス・検証進です。仕様登録・クラス・検証進でD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は登録・ノード・検証進です。用語登録・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0214**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0214について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0214A
    ```

    画面・出力には PHA72DD0214A が表示され、クラスタ構成検証 SMIT Command Status 0214 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0214
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0214B
    ```

    画面・出力には PHA72DD0214B が表示され、クラスタ構成検証 SMIT Command Status 0214 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0214
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0214C
    ```

    画面・出力には PHA72DD0214C が表示され、クラスタ構成検証 SMIT Command Status 0214 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0214A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0214B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0214C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0229 {#c25-i0447}
*分類: 構成検証*  ・  難易度: 上級

朱J確認0230ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票朱J確認0230です。朱J確認0230はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録朱J確認0230です。朱J確認0230では検証進行率と取得時刻を採取票朱J確認0230へ残します。朱J確認0230では未同期構成の見落としを避けるため補助資料も照合する判断朱J確認0230です。朱J確認0230の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録朱J確認0230です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0229を保守記録に説明する必要があります。クラスタ構成検証 Verification Progress 0301と取り違えない説明はどれですか。

    - A. 仕様上の役割は記録操作で証跡欄を照合することでリソース要約を確認し・未同期構成の見落としを防ぐ。
    - B. 仕様上の役割は記録操作で証跡欄を照合することで検証進行率を確認し・未同期構成の見落としを防ぐ。 ✅
    - C. 仕様上の役割は状態確認からST_STABLEを読むことで状態確認を確認し・管理設定と資源状態の混同を防ぐ。
    - D. 仕様上の役割は変更確認操作で採取欄を棚卸することでVG varを確認し・遠隔ボリュームRPV経路断のを防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能確認・クラス・検証進でBの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・確認）です。照合確認・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・確認・未同期です。比較確認・クラス・検証進・未同期でA:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸はシステ・確認・検証進です。項目確認・クラス・検証進でC:の変更前の確認 START02は「Cluster Servicesで状態確認か」を述べるため、正答側の照合軸は未同期・クラス・検証進です。仕様確認・クラス・検証進でD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は確認・未同期・検証進です。用語確認・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0229**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0229について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0229A
    ```

    画面・出力には PHA72DD0229A が表示され、クラスタ構成検証 SMIT Command Status 0229 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0229
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0229B
    ```

    画面・出力には PHA72DD0229B が表示され、クラスタ構成検証 SMIT Command Status 0229 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0229
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0229C
    ```

    画面・出力には PHA72DD0229C が表示され、クラスタ構成検証 SMIT Command Status 0229 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0229A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0229B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0229C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0244 {#c25-i0448}
*分類: 構成検証*  ・  難易度: 初級

紅E保護0245ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紅E保護0245です。紅E保護0245はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録紅E保護0245です。紅E保護0245では検証進行率と取得時刻を採取票紅E保護0245へ残します。紅E保護0245では検証ログの採取漏れを避けるため補助資料も照合する判断紅E保護0245です。紅E保護0245の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録紅E保護0245です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0244の技術的な意味を資料で確認するとき、GLVM地理的ミラー RPV Client 0294との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は遠隔ボリュームRPV経路断の見落を避けるため・変更確認操作で採取欄を棚卸するして遠隔ボリューを照合する。
    - B. コマンドまたは機能の用途は基本ソフト稼働とクラスタ稼働の混を避けるため・イベント確認から終了状態を読むしてイベント確認を照合する。
    - C. コマンドまたは機能の用途は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するして構成データOを照合する。
    - D. コマンドまたは機能の用途は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして検証進行率を照合する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能保護・クラス・検証進でDの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・保護）です。照合保護・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・保護・検証ロです。比較保護・クラス・検証進・検証ロでA:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸はシステ・保護・検証進です。運用保護・システでB:の復旧後の確認 NODE06は「PowerHA Node Stateでイベン」を述べるため、正答側の照合軸は検証進・クラス・保護です。項目保護・クラス・検証進でC:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は検証ロ・クラス・検証進です。用語保護・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0244**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0244について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0244A
    ```

    画面・出力には PHA72DD0244A が表示され、クラスタ構成検証 SMIT Command Status 0244 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0244
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0244B
    ```

    画面・出力には PHA72DD0244B が表示され、クラスタ構成検証 SMIT Command Status 0244 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0244
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0244C
    ```

    画面・出力には PHA72DD0244C が表示され、クラスタ構成検証 SMIT Command Status 0244 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0244A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0244B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0244C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0259 {#c25-i0449}
*分類: 構成検証*  ・  難易度: 初級

空T保護0260ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票空T保護0260です。空T保護0260はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録空T保護0260です。空T保護0260では検証進行率と取得時刻を採取票空T保護0260へ残します。空T保護0260では警告と致命エラーの混同を避けるため補助資料も照合する判断空T保護0260です。空T保護0260の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録空T保護0260です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0259について構成や状態を確認します。クラスタ構成検証 Cluster Resources 0265ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は記録操作で証跡欄を照合することでトポロジ要約を確認し・未同期構成の見落としを防ぐ。
    - B. 一次資料が示す主目的はRG確認からapp_rgを読むことで資源グループを確認し・管理設定と資源状態の混同を防ぐ。
    - C. 一次資料が示す主目的は採取操作で照合欄を点検することで検証進行率を確認し・警告と致命エラーの混同を防ぐ。 ✅
    - D. 一次資料が示す主目的は調査操作で保守欄を引き継ぎすることで獲得イベントを確認し・自動戻し条件の誤読を防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能保護・クラス・検証進でCの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・保護）です。照合保護・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・保護・警告とです。比較保護・クラス・検証進・警告とでA:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸はシステ・保護・検証進です。運用保護・システでB:の再始動後の確認 START15は「Cluster Servicesで資源グルー」を述べるため、正答側の照合軸は検証進・クラス・保護です。仕様保護・クラス・検証進でD:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は保護・警告と・検証進です。用語保護・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0259**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0259について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0259A
    ```

    画面・出力には PHA72DD0259A が表示され、クラスタ構成検証 SMIT Command Status 0259 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0259
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0259B
    ```

    画面・出力には PHA72DD0259B が表示され、クラスタ構成検証 SMIT Command Status 0259 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0259
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0259C
    ```

    画面・出力には PHA72DD0259C が表示され、クラスタ構成検証 SMIT Command Status 0259 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0259A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0259B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0259C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0274 {#c25-i0450}
*分類: 構成検証*  ・  難易度: 中級

翠O照合0275ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票翠O照合0275です。翠O照合0275はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録翠O照合0275です。翠O照合0275では検証進行率と取得時刻を採取票翠O照合0275へ残します。翠O照合0275ではノード間ODM差分の残存を避けるため補助資料も照合する判断翠O照合0275です。翠O照合0275の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録翠O照合0275です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0274の役割を調べています。リソースグループ制御 Acquisition Failure 0326の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はノード間構成データODM差分の残を避けるため・確認操作で状態欄を整理するして検証進行率を照合する。 ✅
    - B. 障害切り分けに用いる役割は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして獲得イベントを照合する。
    - C. 障害切り分けに用いる役割は同期元を誤ると古い定義を全ノードを避けるため・未同期確認からUNSYNCED_CHANして未同期確認を照合する。
    - D. 障害切り分けに用いる役割は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして失敗ラベルを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能照合・クラス・検証進でAの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・照合）です。照合照合・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・照合・ノードです。運用照合・システでB:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は検証進・クラス・照合です。項目照合・クラス・検証進でC:の障害切り分け SYNC04は「Cluster Synchronizで未同期」を述べるため、正答側の照合軸はノード・クラス・検証進です。仕様照合・クラス・検証進でD:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は照合・ノード・検証進です。用語照合・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0274**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0274について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0274A
    ```

    画面・出力には PHA72DD0274A が表示され、クラスタ構成検証 SMIT Command Status 0274 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0274
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0274B
    ```

    画面・出力には PHA72DD0274B が表示され、クラスタ構成検証 SMIT Command Status 0274 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0274
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0274C
    ```

    画面・出力には PHA72DD0274C が表示され、クラスタ構成検証 SMIT Command Status 0274 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0274A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0274B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0274C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0289 {#c25-i0451}
*分類: 構成検証*  ・  難易度: 中級

朱J抑止0290ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票朱J抑止0290です。朱J抑止0290はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録朱J抑止0290です。朱J抑止0290では検証進行率と取得時刻を採取票朱J抑止0290へ残します。朱J抑止0290では未同期構成の見落としを避けるため補助資料も照合する判断朱J抑止0290です。朱J抑止0290の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録朱J抑止0290です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 SMIT Command Status 0289」を「リソースグループ制御 Resource Group Name 0305」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は解析で優先ノード一を証跡に残し・資源グループの優先ノード一覧と取得時刻を記録し。
    - B. 仕様上の役割は構成監査でマネージャーを証跡に残し・hacmp.out Eventでマネージャーログから。
    - C. 仕様上の役割は移行で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。
    - D. 仕様上の役割は抑止で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能抑止・クラス・検証進でDの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・抑止）です。照合抑止・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・抑止・未同期です。比較抑止・クラス・検証進・未同期でA:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸はシステ・抑止・検証進です。運用抑止・システでB:の構成監査 FAIL08は「hacmp.out Eventでマネージャー」を述べるため、正答側の照合軸は検証進・クラス・抑止です。項目抑止・クラス・検証進でC:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は未同期・クラス・検証進です。用語抑止・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0289**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0289について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0289A
    ```

    画面・出力には PHA72DD0289A が表示され、クラスタ構成検証 SMIT Command Status 0289 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0289
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0289B
    ```

    画面・出力には PHA72DD0289B が表示され、クラスタ構成検証 SMIT Command Status 0289 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0289
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0289C
    ```

    画面・出力には PHA72DD0289C が表示され、クラスタ構成検証 SMIT Command Status 0289 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0289A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0289B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0289C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0304 {#c25-i0452}
*分類: 構成検証*  ・  難易度: 中級

紅E解析0305ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紅E解析0305です。紅E解析0305はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録紅E解析0305です。紅E解析0305では検証進行率と取得時刻を採取票紅E解析0305へ残します。紅E解析0305では検証ログの採取漏れを避けるため補助資料も照合する判断紅E解析0305です。紅E解析0305の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録紅E解析0305です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0304を同一分類のclRGinfo 障害切り分け 識別値と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はシステム管理コマンドの検証進行率と取得時刻を記録し・検証ログの採取漏れを防ぐである。保守操作で監査欄を保存するときは検証ログの採取漏れを防ぐ。 ✅
    - B. コマンドまたは機能の用途はリソースグループの状態と所有ノードを表示するコマンドである。同期処理で識別値を確認するときは識別値の誤読を防ぐ。
    - C. コマンドまたは機能の用途はhacmp.out Eventで主要ログから ACQUISITION を読み・ACQUISITION とである。主要ログからACQUISITIONをときはcluster historを防ぐ。
    - D. コマンドまたは機能の用途はクラスター資源のトポロジ要約と取得時刻を記録し・未同期構成の見落としを防ぐである。記録操作で証跡欄を照合するときは未同期構成の見落としを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能解析・クラス・検証進でAの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・解析）です。照合解析・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・解析・検証ロです。運用解析・システでB:の障害切り分け 識別値は「リソースグループの状態と所有ノードを表示する」を述べるため、正答側の照合軸は検証進・クラス・解析です。項目解析・クラス・検証進でC:の障害切り分け FAIL04は「hacmp.out Eventで主要ログから」を述べるため、正答側の照合軸は検証ロ・クラス・検証進です。仕様解析・クラス・検証進でD:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は解析・検証ロ・検証進です。用語解析・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0304**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0304について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0304A
    ```

    画面・出力には PHA72DD0304A が表示され、クラスタ構成検証 SMIT Command Status 0304 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0304
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0304B
    ```

    画面・出力には PHA72DD0304B が表示され、クラスタ構成検証 SMIT Command Status 0304 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0304
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0304C
    ```

    画面・出力には PHA72DD0304C が表示され、クラスタ構成検証 SMIT Command Status 0304 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0304A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0304B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0304C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0319 {#c25-i0453}
*分類: 構成検証*  ・  難易度: 中級

空T解析0320ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票空T解析0320です。空T解析0320はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録空T解析0320です。空T解析0320では検証進行率と取得時刻を採取票空T解析0320へ残します。空T解析0320では警告と致命エラーの混同を避けるため補助資料も照合する判断空T解析0320です。空T解析0320の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録空T解析0320です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0319の設定や表示を読む前に役割を確認します。cldump トポロジー確認 警告行ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はシステム管理コマンドの検証進行率と取得時刻を記録し・警告と致命エラーの混同を防ぐである。採取操作で照合欄を点検するときは警告と致命エラーの混同を防ぐ。 ✅
    - B. 一次資料が示す主目的はクラスタ構成と状態をスナップショットとして表示するコマンドをトポロジー確認する。トポロジー確で警告行を確認するときは警告行の誤読を防ぐ。
    - C. 一次資料が示す主目的は資源グループで資源グループRG一覧から database_rg を読み・database_rg とである。RG一覧からdatabase_rgをときは依存順を無視して子資源を先にを防ぐ。
    - D. 一次資料が示す主目的は地理的ミラーの項目のVG vary状態と取得時刻を記録し・syslogとhacmp.outの突合漏れを防ぐである。監査操作で記録欄を比較するときはsyslogとhacmp.oを防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能解析・クラス・検証進でAの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・解析）です。照合解析・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・解析・警告とです。運用解析・システでB:のトポロジー確認 警告行は「クラスタ構成と状態をスナップショットとして表」を述べるため、正答側の照合軸は検証進・クラス・解析です。項目解析・クラス・検証進でC:の変更前の確認 DEP02は「資源グループで資源グループRG一覧から」を述べるため、正答側の照合軸は警告と・クラス・検証進です。仕様解析・クラス・検証進でD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は解析・警告と・検証進です。用語解析・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0319**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0319について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0319A
    ```

    画面・出力には PHA72DD0319A が表示され、クラスタ構成検証 SMIT Command Status 0319 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0319
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0319B
    ```

    画面・出力には PHA72DD0319B が表示され、クラスタ構成検証 SMIT Command Status 0319 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0319
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0319C
    ```

    画面・出力には PHA72DD0319C が表示され、クラスタ構成検証 SMIT Command Status 0319 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0319A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0319B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0319C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0334 {#c25-i0454}
*分類: 構成検証*  ・  難易度: 中級

翠O計画0335ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票翠O計画0335です。翠O計画0335はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録翠O計画0335です。翠O計画0335では検証進行率と取得時刻を採取票翠O計画0335へ残します。翠O計画0335ではノード間ODM差分の残存を避けるため補助資料も照合する判断翠O計画0335です。翠O計画0335の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録翠O計画0335です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0334に関する障害切り分けの前提を確認しています。clstat -o 版数確認 再投入確認の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は再投入確認の誤読を避けるため・再投入確認で再投入確認を確認するして再投入確認を照合する。clstat -o 版数確認 再投入確認固有の属性も確認対象に含める。
    - B. 障害切り分けに用いる役割は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして優先ノード一を照合する。
    - C. 障害切り分けに用いる役割はノード間構成データODM差分の残を避けるため・確認操作で状態欄を整理するして検証進行率を照合する。 ✅
    - D. 障害切り分けに用いる役割は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するして検証報告ROを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能計画・クラス・検証進でCの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・計画）です。照合計画・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・計画・ノードです。比較計画・クラス・検証進・ノードでA:の版数確認 再投入確認は「クラスタ、ノード、インターフェース」を述べるため、正答側の照合軸はシステ・計画・検証進です。運用計画・システでB:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は検証進・クラス・計画です。仕様計画・クラス・検証進でD:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸は計画・ノード・検証進です。用語計画・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0334**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0334について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0334A
    ```

    画面・出力には PHA72DD0334A が表示され、クラスタ構成検証 SMIT Command Status 0334 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0334
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0334B
    ```

    画面・出力には PHA72DD0334B が表示され、クラスタ構成検証 SMIT Command Status 0334 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0334
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0334C
    ```

    画面・出力には PHA72DD0334C が表示され、クラスタ構成検証 SMIT Command Status 0334 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0334A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0334B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0334C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 SMIT Command Status 0349 {#c25-i0455}
*分類: 構成検証*  ・  難易度: 上級

朱J解除0350ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票朱J解除0350です。朱J解除0350はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録朱J解除0350です。朱J解除0350では検証進行率と取得時刻を採取票朱J解除0350へ残します。朱J解除0350では未同期構成の見落としを避けるため補助資料も照合する判断朱J解除0350です。朱J解除0350の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録朱J解除0350です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 SMIT Command Status 0349を保守記録に説明する必要があります。clstat -o 同期確認 統計値と取り違えない説明はどれですか。

    - A. 仕様上の役割は同期確認で統計値を証跡に残し・クラスタ・ノード・インターフェース・リソースグループの状態を。
    - B. 仕様上の役割は解除で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。 ✅
    - C. 仕様上の役割は変更で遠隔ボリューを証跡に残し・地理的ミラーの項目の遠隔ボリュームRPV通信ペアと取得時刻を。
    - D. 仕様上の役割は保護でVG varを証跡に残し・地理的ミラーの項目のVG vary状態と取得時刻を記録し。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能解除・クラス・検証進でBの記述「システム管理コマンドの検証進行率と取得時刻を記録し」に対応する項目はCommand Status（システ・検証進・解除）です。照合解除・クラス・検証進に関する構成検証の仕様は「システム管理コマンドの検証進行率と取得時刻を記録し」で、確認対象は検証進・解除・未同期です。比較解除・クラス・検証進・未同期でA:の同期確認 統計値は「クラスタ、ノード、インターフェース」を述べるため、正答側の照合軸はシステ・解除・検証進です。項目解除・クラス・検証進でC:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸は未同期・クラス・検証進です。仕様解除・クラス・検証進でD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は解除・未同期・検証進です。用語解除・クラス・検証進という用語は「システム管理コマンドの検証進行率と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・検証進・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 SMIT Command Status 0349**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 SMIT Command Status 0349について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=SMIT Command Status と 検証進行率
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> smit sysmirror
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0349A
    ```

    画面・出力には PHA72DD0349A が表示され、クラスタ構成検証 SMIT Command Status 0349 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0349
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0349B
    ```

    画面・出力には PHA72DD0349B が表示され、クラスタ構成検証 SMIT Command Status 0349 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。SMIT Command Status を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0349
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0349C
    ```

    画面・出力には PHA72DD0349C が表示され、クラスタ構成検証 SMIT Command Status 0349 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0349A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0349B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0349C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0001 {#c25-i0456}
*分類: 構成検証*  ・  難易度: 初級

橙B巡回0002ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票橙B巡回0002です。橙B巡回0002はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録橙B巡回0002です。橙B巡回0002ではリソース要約と取得時刻を採取票橙B巡回0002へ残します。橙B巡回0002では未同期構成の見落としを避けるため補助資料も照合する判断橙B巡回0002です。橙B巡回0002の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録橙B巡回0002です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 Verification Progress 0001」を「リソースグループ制御 Node List 0077」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はノード一覧の移動履歴と取得時刻を記録し・資源グループ位置の誤認を防ぐである。復旧操作で点検欄を確認するときは資源グループ位置の誤認を防ぐ。
    - B. 仕様上の役割は構成検証のリソース要約と取得時刻を記録し・未同期構成の見落としを防ぐである。記録操作で証跡欄を照合するときは未同期構成の見落としを防ぐ。 ✅
    - C. 仕様上の役割はシステム管理コマンドの検証進行率と取得時刻を記録し・警告と致命エラーの混同を防ぐである。採取操作で照合欄を点検するときは警告と致命エラーの混同を防ぐ。
    - D. 仕様上の役割はクラスタ・ノード・インターフェース・リソースグループの状態を表示する監視コマンドを版数確認する。再投入確認で再投入確認を確認するときは再投入確認の誤読を防ぐ。

    正解: **B** ／ 難易度: 初級

    **解説:** 機能巡回・クラス・リソーでBの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・巡回）です。照合巡回・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、未同期構成の見落としを防ぐ」で、確認対象はリソー・巡回・未同期です。比較クラス・巡回でA:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は構成検・巡回・リソーです。項目巡回・クラス・リソーでC:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸は未同期・クラス・リソーです。仕様巡回・クラス・リソーでD:の版数確認 再投入確認は「クラスタ、ノード、インターフェース」を述べるため、正答側の照合軸は巡回・未同期・リソーです。用語巡回・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0001**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0001について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード PHA72DD0001A
    ```

    画面・出力には PHA72DD0001A が表示され、クラスタ構成検証 Verification Progress 0001 の入力欄確認を確認できます。

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
    clverify.log entry PHA0001
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0001B
    ```

    画面・出力には PHA72DD0001B が表示され、クラスタ構成検証 Verification Progress 0001 の証跡表示確認を確認できます。

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
    ROHA report PHA0001
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0001C
    ```

    画面・出力には PHA72DD0001C が表示され、クラスタ構成検証 Verification Progress 0001 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0001A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0001B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0001C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0016 {#c25-i0457}
*分類: 構成検証*  ・  難易度: 初級

青Q巡回0017ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票青Q巡回0017です。青Q巡回0017はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録青Q巡回0017です。青Q巡回0017ではリソース要約と取得時刻を採取票青Q巡回0017へ残します。青Q巡回0017では検証ログの採取漏れを避けるため補助資料も照合する判断青Q巡回0017です。青Q巡回0017の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録青Q巡回0017です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0016を同一分類のクラスタ構成検証 Cluster Resources 0055と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は復旧でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。
    - B. コマンドまたは機能の用途は照合で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。
    - C. コマンドまたは機能の用途は巡回でリソース要約を証跡に残し・構成検証のリソース要約と取得時刻を記録し。 ✅
    - D. コマンドまたは機能の用途は復旧確認でイベント確認を証跡に残し・PowerHA Node Stateでイベント確認から。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能巡回・クラス・リソーでCの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・巡回）です。照合巡回・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し、検証ログの採取漏れを防ぐ」で、確認対象はリソー・巡回・検証ロです。比較クラス・巡回でA:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は構成検・巡回・リソーです。運用巡回・構成検でB:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はリソー・クラス・巡回です。仕様巡回・クラス・リソーでD:の復旧後の確認 NODE06は「PowerHA Node Stateでイベン」を述べるため、正答側の照合軸は巡回・検証ロ・リソーです。用語巡回・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0016**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0016について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード PHA72DD0016A
    ```

    画面・出力には PHA72DD0016A が表示され、クラスタ構成検証 Verification Progress 0016 の入力欄確認を確認できます。

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
    clverify.log entry PHA0016
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0016B
    ```

    画面・出力には PHA72DD0016B が表示され、クラスタ構成検証 Verification Progress 0016 の証跡表示確認を確認できます。

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
    ROHA report PHA0016
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0016C
    ```

    画面・出力には PHA72DD0016C が表示され、クラスタ構成検証 Verification Progress 0016 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0016A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0016B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0016C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Verification Progress 0031 {#c25-i0458}
*分類: 構成検証*  ・  難易度: 中級

白L棚卸0032ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票白L棚卸0032です。白L棚卸0032はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録白L棚卸0032です。白L棚卸0032ではリソース要約と取得時刻を採取票白L棚卸0032へ残します。白L棚卸0032では警告と致命エラーの混同を避けるため補助資料も照合する判断白L棚卸0032です。白L棚卸0032の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録白L棚卸0032です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Verification Progress 0031の設定や表示を読む前に役割を確認します。リソースグループ制御 Resource Group Name 0065ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は監査で優先ノード一を証跡に残し・資源グループの優先ノード一覧と取得時刻を記録し。
    - B. 一次資料が示す主目的は棚卸でリソース要約を証跡に残し・構成検証のリソース要約と取得時刻を記録し。 ✅
    - C. 一次資料が示す主目的は解析でVG varを証跡に残し・地理的ミラーの項目のVG vary状態と取得時刻を記録し。
    - D. 一次資料が示す主目的は構成監査で状態確認を証跡に残し・Cluster Servicesで状態確認から。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能棚卸・クラス・リソーでBの記述「構成検証のリソース要約と取得時刻を記録し」に対応する項目はVerification（構成検・リソー・棚卸）です。照合棚卸・クラス・リソーに関する構成検証の仕様は「構成検証のリソース要約と取得時刻を記録し」で、確認対象はリソー・棚卸・警告とです。比較クラス・棚卸でA:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は構成検・棚卸・リソーです。項目棚卸・クラス・リソーでC:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は警告と・クラス・リソーです。仕様棚卸・クラス・リソーでD:の構成監査 START08は「Cluster Servicesで状態確認か」を述べるため、正答側の照合軸は棚卸・警告と・リソーです。用語棚卸・クラス・リソーという用語は「構成検証のリソース要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・リソー・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Verification Progress 0031**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Verification Progress 0031について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード PHA72DD0031A
    ```

    画面・出力には PHA72DD0031A が表示され、クラスタ構成検証 Verification Progress 0031 の入力欄確認を確認できます。

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
    clverify.log entry PHA0031
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0031B
    ```

    画面・出力には PHA72DD0031B が表示され、クラスタ構成検証 Verification Progress 0031 の証跡表示確認を確認できます。

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
    ROHA report PHA0031
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0031C
    ```

    画面・出力には PHA72DD0031C が表示され、クラスタ構成検証 Verification Progress 0031 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0031A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0031B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0031C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


