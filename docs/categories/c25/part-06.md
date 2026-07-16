---
search:
  exclude: true
---

# PowerHA SystemMirror 7.2 — 詳細 (6/6)

[← PowerHA SystemMirror 7.2 の概要へ戻る](index.md)


## PowerHA SystemMirror 7.2 > 構成検証

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



### 資源依存関係 Resource Group Dependency 再始動後の確認 DEP15 {#c25-i0508}
*分類: 資源依存関係*  ・  難易度: 上級

再始動後の確認では 資源依存関係 の イベント順序 を主操作として DEP15 を判定します。再開点と未処理データへの注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP15 に残します。再始動後の確認を補助する 依存照会 では START_AFTER を補助値として DEP15 へ保存します。主判定の再始動後の確認では資源依存関係の イベント順序 から completed を読み DEP15 へ残します。証跡照合の再始動後の確認では資源依存関係の completed と START_AFTER を DEP15 に保存します。記録対応の再始動後の確認では資源依存関係の Parent RGとChild RG の証跡へ DEP15 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 再始動後の確認 DEP15を同一分類のGLVM地理的ミラー RPV Client 0024と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は依存順を無視して子資源を先にオンを避けるため・イベント順序からcompletedを読むしてイベント順序を照合する。 ✅
    - B. 管理対象との関係を表す説明はミラー再同期条件の誤読を避けるため・照合操作で確認欄を採取するして遠隔ボリューを照合する。GLVM地理的ミラー RPV Client 0024固有の属性も確認対象に含める。
    - C. 管理対象との関係を表す説明はノード間構成データODM差分の残を避けるため・確認操作で状態欄を整理するして検証報告ROを照合する。
    - D. 管理対象との関係を表す説明は永続アドレスとサービスアドレスのを避けるため・RG位置からオンライン表示を読むして資源グループを照合する。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能再始動・資源依・イベンでAの記述「資源グループでイベント順序から completed」に対応する項目は再始動後の確認 DEP15（資源グ・イベン・再始動）です。照合再始動・資源依・イベンに関する資源依存関係の仕様は「資源グループでイベント順序から completed を読み」で、確認対象はイベン・再始動・依存順です。運用再始動・資源グでB:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸はイベン・資源依・再始動です。項目再始動・資源依・イベンでC:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸は依存順・資源依・イベンです。仕様再始動・資源依・イベンでD:の構成監査 SVCIP08は「IP Service IPで資源グループ位置」を述べるため、正答側の照合軸は再始動・依存順・イベンです。用語再始動・資源依・イベンという用語は「資源グループでイベント順序から completed」を指し、照合する値と誤認リスクの組合せは資源依・イベン・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 再始動後の確認 DEP15**

    - 検証目的: 資源依存関係のResource Group Dependencyについて再始動結果を検証し、DEP15のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP15のイベント順序を表示します。
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

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP15の依存照会を表示します。
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

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP15のRG一覧を表示します。
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

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の completed が画面・出力に表示されること
    ② ステップ2 の NAME=app が画面・出力に表示されること
    ③ ステップ3 の database が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 変更前の確認 DEP02 {#c25-i0509}
*分類: 資源依存関係*  ・  難易度: 上級

変更前の確認では 資源依存関係 の RG一覧 を主操作として DEP02 を判定します。変更対象と非対象の境界への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP02 に残します。変更前の確認を補助する イベント順序 では completed を補助値として DEP02 へ保存します。主判定の変更前の確認では資源依存関係の RG一覧 から database_rg を読み DEP02 へ残します。証跡照合の変更前の確認では資源依存関係の database_rg と completed を DEP02 に保存します。記録対応の変更前の確認では資源依存関係の Parent RGとChild RG の証跡へ DEP02 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 変更前の確認 DEP02について構成や状態を確認します。GLVM地理的ミラー RPV Server 0081ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは地理的ミラーの項目のミラー更新状態と取得時刻を記録し・片側VGのvaryon誤操作を防ぐである。主操作で出力欄を評価するときは片側VGのvaryon誤操作を防ぐ。
    - B. 状態を読み取るための働きはイベント要約の失敗ラベルと取得時刻を記録し・自動戻し条件の誤読を防ぐである。調査操作で保守欄を引き継ぎするときは自動戻し条件の誤読を防ぐ。リソースグループ制御 Event Summary 0248固有の属性も確認対象に含める。
    - C. 状態を読み取るための働きは資源グループで資源グループRG一覧から database_rg を読み・database_rg とである。RG一覧からdatabase_rgをときは依存順を無視して子資源を先にを防ぐ。 ✅
    - D. 状態を読み取るための働きはPowerHA Node Stateでイベント確認から 終了状態 を読み・終了状態 と 実状態値 を照合する。イベント確認から終了状態を読むときは基本ソフト稼働とクラスタ稼働を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能変更確・資源依・資源グでCの記述「資源グループで資源グループRG一覧から」に対応する項目は変更前の確認 DEP02（資源グ・資源グ・変更確）です。照合変更確・資源依・資源グに関する資源依存関係の仕様は「資源グループで資源グループRG一覧から database_rg」で、確認対象は資源グ・変更確・依存順です。比較資源依・変更確でA:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は資源グ・変更確・資源グです。運用変更確・資源グでB:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は資源グ・資源依・変更確です。仕様変更確・資源依・資源グでD:の変更後の確認 NODE03は「PowerHA Node Stateでイベン」を述べるため、正答側の照合軸は変更確・依存順・資源グです。用語変更確・資源依・資源グという用語は「資源グループで資源グループRG一覧から」を指し、照合する値と誤認リスクの組合せは資源依・資源グ・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 変更前の確認 DEP02**

    - 検証目的: 資源依存関係のResource Group Dependencyについて変更前の証跡を保存し、DEP02のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP02のRG一覧を表示します。
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

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP02のイベント順序を表示します。
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

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP02の依存照会を表示します。
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

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の database が画面・出力に表示されること
    ② ステップ2 の completed が画面・出力に表示されること
    ③ ステップ3 の NAME=app が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 変更後の確認 DEP03 {#c25-i0510}
*分類: 資源依存関係*  ・  難易度: 上級

変更後の確認では 資源依存関係 の イベント順序 を主操作として DEP03 を判定します。反映値と残存値への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP03 に残します。変更後の確認を補助する 依存照会 では START_AFTER を補助値として DEP03 へ保存します。主判定の変更後の確認では資源依存関係の イベント順序 から completed を読み DEP03 へ残します。証跡照合の変更後の確認では資源依存関係の completed と START_AFTER を DEP03 に保存します。記録対応の変更後の確認では資源依存関係の Parent RGとChild RG の証跡へ DEP03 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 変更後の確認 DEP03の技術的な意味を資料で確認するとき、GLVM地理的ミラー RPV Client 0009との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は変更確認でイベント順序を証跡に残し・資源グループでイベント順序から completed を読み。 ✅
    - B. 管理対象との関係を表す説明は巡回で遠隔ボリューを証跡に残し・地理的ミラーの項目の遠隔ボリュームRPV通信ペアと取得時刻を。GLVM地理的ミラー RPV Client 0009固有の属性も確認対象に含める。
    - C. 管理対象との関係を表す説明は切替で検証報告ROを証跡に残し・clverify.logの検証報告ROHAレポートと取得時刻。
    - D. 管理対象との関係を表す説明は所有先確認で除外条件を証跡に残し・Cluster Manager の状態・クラスタ版数。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能変更確・資源依・イベンでAの記述「資源グループでイベント順序から completed」に対応する項目は変更後の確認 DEP03（資源グ・イベン・変更確）です。照合変更確・資源依・イベンに関する資源依存関係の仕様は「資源グループでイベント順序から completed を読み」で、確認対象はイベン・変更確・依存順です。運用変更確・資源グでB:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸はイベン・資源依・変更確です。項目変更確・資源依・イベンでC:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸は依存順・資源依・イベンです。仕様変更確・資源依・イベンでD:の所有先確認 除外条件は「Cluster Manager の状態」を述べるため、正答側の照合軸は変更確・依存順・イベンです。用語変更確・資源依・イベンという用語は「資源グループでイベント順序から completed」を指し、照合する値と誤認リスクの組合せは資源依・イベン・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 変更後の確認 DEP03**

    - 検証目的: 資源依存関係のResource Group Dependencyについて変更結果を検証し、DEP03のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP03のイベント順序を表示します。
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

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP03の依存照会を表示します。
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

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP03のRG一覧を表示します。
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

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の completed が画面・出力に表示されること
    ② ステップ2 の NAME=app が画面・出力に表示されること
    ③ ステップ3 の database が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 引継ぎ記録 DEP09 {#c25-i0511}
*分類: 資源依存関係*  ・  難易度: 上級

引継ぎ記録では 資源依存関係 の イベント順序 を主操作として DEP09 を判定します。次担当者が追跡できる証跡への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP09 に残します。引継ぎ記録を補助する 依存照会 では START_AFTER を補助値として DEP09 へ保存します。主判定の引継ぎ記録では資源依存関係の イベント順序 から completed を読み DEP09 へ残します。証跡照合の引継ぎ記録では資源依存関係の completed と START_AFTER を DEP09 に保存します。記録対応の引継ぎ記録では資源依存関係の Parent RGとChild RG の証跡へ DEP09 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 引継ぎ記録 DEP09の役割を調べています。GLVM地理的ミラー syslog entry 0012の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は資源依存関係でイベント順序を証跡に残し・資源グループでイベント順序から completed を読み。 ✅
    - B. 表示や設定で扱う内容は巡回でsyslogを証跡に残し・地理的ミラーの項目のsyslog記録と取得時刻を記録し。
    - C. 表示や設定で扱う内容は登録で移動履歴を証跡に残し・ノード一覧の移動履歴と取得時刻を記録し。
    - D. 表示や設定で扱う内容は同期確認で出力比較を証跡に残し・クラスタトポロジーとリソースの整合性を検査するコマンドを同期。clmgr verify cluster 同期確認 出力比較固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能資源依・資源依・イベンでAの記述「資源グループでイベント順序から completed」に対応する項目は引継ぎ記録 DEP09（資源グ・イベン・資源依）です。照合資源依・資源依・イベンに関する資源依存関係の仕様は「資源グループでイベント順序から completed を読み」で、確認対象はイベン・資源依・依存順です。運用資源依・資源グでB:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸はイベン・資源依・資源依です。項目資源依・資源依・イベンでC:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は依存順・資源依・イベンです。仕様資源依・資源依・イベンでD:の同期確認 出力比較は「クラスタトポロジーとリソースの整合性を検査す」を述べるため、正答側の照合軸は資源依・依存順・イベンです。用語資源依・資源依・イベンという用語は「資源グループでイベント順序から completed」を指し、照合する値と誤認リスクの組合せは資源依・イベン・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 引継ぎ記録 DEP09**

    - 検証目的: 資源依存関係のResource Group Dependencyについて再現可能な記録を作成し、DEP09のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP09のイベント順序を表示します。
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

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP09の依存照会を表示します。
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

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP09のRG一覧を表示します。
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

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の completed が画面・出力に表示されること
    ② ステップ2 の NAME=app が画面・出力に表示されること
    ③ ステップ3 の database が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 復旧後の確認 DEP06 {#c25-i0512}
*分類: 資源依存関係*  ・  難易度: 上級

復旧後の確認では 資源依存関係 の イベント順序 を主操作として DEP06 を判定します。再発していないことを示す値への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP06 に残します。復旧後の確認を補助する 依存照会 では START_AFTER を補助値として DEP06 へ保存します。主判定の復旧後の確認では資源依存関係の イベント順序 から completed を読み DEP06 へ残します。証跡照合の復旧後の確認では資源依存関係の completed と START_AFTER を DEP06 に保存します。記録対応の復旧後の確認では資源依存関係の Parent RGとChild RG の証跡へ DEP06 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 復旧後の確認 DEP06の設定や表示を読む前に役割を確認します。クラスタ構成検証 Cluster Topology 0088ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは保守操作で監査欄を保存することで構成データOを確認し・検証ログの採取漏れを防ぐ。
    - B. 対象資源に対する働きは監査操作で記録欄を比較することで遠隔ボリューを確認し・syslogとhacmp.oを防ぐ。GLVM地理的ミラー RPV Client 0219固有の属性も確認対象に含める。
    - C. 対象資源に対する働きはイベント順序からcompletedを読むことでイベント順序を確認し・依存順を無視して子資源を先にを防ぐ。 ✅
    - D. 対象資源に対する働きは同期処理で識別値を確認することで識別値を確認し・識別値の誤読を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能復旧確・資源依・イベンでCの記述「資源グループでイベント順序から completed」に対応する項目は復旧後の確認 DEP06（資源グ・イベン・復旧確）です。照合復旧確・資源依・イベンに関する資源依存関係の仕様は「資源グループでイベント順序から completed を読み」で、確認対象はイベン・復旧確・依存順です。比較資源依・復旧確でA:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は資源グ・復旧確・イベンです。運用復旧確・資源グでB:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸はイベン・資源依・復旧確です。仕様復旧確・資源依・イベンでD:の障害切り分け 識別値は「リソースグループの状態と所有ノードを表示する」を述べるため、正答側の照合軸は復旧確・依存順・イベンです。用語復旧確・資源依・イベンという用語は「資源グループでイベント順序から completed」を指し、照合する値と誤認リスクの組合せは資源依・イベン・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 復旧後の確認 DEP06**

    - 検証目的: 資源依存関係のResource Group Dependencyについて復旧後の安定性を確認し、DEP06のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP06のイベント順序を表示します。
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

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP06の依存照会を表示します。
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

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP06のRG一覧を表示します。
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

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の completed が画面・出力に表示されること
    ② ステップ2 の NAME=app が画面・出力に表示されること
    ③ ステップ3 の database が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 復旧準備 DEP05 {#c25-i0513}
*分類: 資源依存関係*  ・  難易度: 上級

復旧準備では 資源依存関係 の RG一覧 を主操作として DEP05 を判定します。再開前に必要な整合性への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP05 に残します。復旧準備を補助する イベント順序 では completed を補助値として DEP05 へ保存します。主判定の復旧準備では資源依存関係の RG一覧 から database_rg を読み DEP05 へ残します。証跡照合の復旧準備では資源依存関係の database_rg と completed を DEP05 に保存します。記録対応の復旧準備では資源依存関係の Parent RGとChild RG の証跡へ DEP05 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 復旧準備 DEP05に関する障害切り分けの前提を確認しています。リソースグループ制御 Event Summary 0083の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはイベント要約の失敗ラベルと取得時刻を記録し・獲得失敗ログの未採取を防ぐである。表示操作で対象欄を追跡するときは獲得失敗ログの未採取を防ぐ。
    - B. 機能の説明としてはクラスター資源のトポロジ要約と取得時刻を記録し・ノード間構成データODM差分の残存を防ぐである。確認操作で状態欄を整理するときはノード間構成データODM差分を防ぐ。クラスタ構成検証 Cluster Resources 0250固有の属性も確認対象に含める。
    - C. 機能の説明としては資源グループで資源グループRG一覧から database_rg を読み・database_rg とである。RG一覧からdatabase_rgをときは依存順を無視して子資源を先にを防ぐ。 ✅
    - D. 機能の説明としては地理的ミラーの項目のsyslog記録と取得時刻を記録し・片側VGのvaryon誤操作を防ぐである。主操作で出力欄を評価するときは片側VGのvaryon誤操作を防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能復旧準・資源依・資源グでCの記述「資源グループで資源グループRG一覧から」に対応する項目は復旧準備 DEP05（資源グ・資源グ・復旧準）です。照合復旧準・資源依・資源グに関する資源依存関係の仕様は「資源グループで資源グループRG一覧から database_rg」で、確認対象は資源グ・復旧準・依存順です。比較資源依・復旧準でA:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は資源グ・復旧準・資源グです。運用復旧準・資源グでB:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は資源グ・資源依・復旧準です。仕様復旧準・資源依・資源グでD:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は復旧準・依存順・資源グです。用語復旧準・資源依・資源グという用語は「資源グループで資源グループRG一覧から」を指し、照合する値と誤認リスクの組合せは資源依・資源グ・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 復旧準備 DEP05**

    - 検証目的: 資源依存関係のResource Group Dependencyについて復旧条件を確認し、DEP05のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP05のRG一覧を表示します。
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

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP05のイベント順序を表示します。
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

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP05の依存照会を表示します。
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

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の database が画面・出力に表示されること
    ② ステップ2 の completed が画面・出力に表示されること
    ③ ステップ3 の NAME=app が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 性能影響の確認 DEP11 {#c25-i0514}
*分類: 資源依存関係*  ・  難易度: 上級

性能影響の確認では 資源依存関係 の RG一覧 を主操作として DEP11 を判定します。処理時間と滞留箇所への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP11 に残します。性能影響の確認を補助する イベント順序 では completed を補助値として DEP11 へ保存します。主判定の性能影響の確認では資源依存関係の RG一覧 から database_rg を読み DEP11 へ残します。証跡照合の性能影響の確認では資源依存関係の database_rg と completed を DEP11 に保存します。記録対応の性能影響の確認では資源依存関係の Parent RGとChild RG の証跡へ DEP11 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 性能影響の確認 DEP11の技術的な意味を資料で確認するとき、GLVM地理的ミラー RPV Server 0006との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は地理的ミラーの項目のミラー更新状態と取得時刻を記録し・遠隔ボリュームRPV経路断の見落としを防ぐである。変更確認操作で採取欄を棚卸するときは遠隔ボリュームRPV経路断のを防ぐ。
    - B. 構成を確認する際の意味は地理的ミラーの項目のsyslog記録と取得時刻を記録し・遠隔ボリュームRPV経路断の見落としを防ぐである。変更確認操作で採取欄を棚卸するときは遠隔ボリュームRPV経路断のを防ぐ。
    - C. 構成を確認する際の意味はクラスタ構成と状態をスナップショットとして表示するコマンドをトポロジー確認する。トポロジー確で警告行を確認するときは警告行の誤読を防ぐ。cldump トポロジー確認 警告行固有の属性も確認対象に含める。
    - D. 構成を確認する際の意味は資源グループで資源グループRG一覧から database_rg を読み・database_rg とである。RG一覧からdatabase_rgをときは依存順を無視して子資源を先にを防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能性能影・資源依・資源グでDの記述「資源グループで資源グループRG一覧から」に対応する項目は性能影響の確認 DEP11（資源グ・資源グ・性能影）です。照合性能影・資源依・資源グに関する資源依存関係の仕様は「資源グループで資源グループRG一覧から database_rg」で、確認対象は資源グ・性能影・依存順です。比較資源依・性能影でA:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は資源グ・性能影・資源グです。運用性能影・資源グでB:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は資源グ・資源依・性能影です。項目性能影・資源依・資源グでC:のトポロジー確認 警告行は「クラスタ構成と状態をスナップショットとして表」を述べるため、正答側の照合軸は依存順・資源依・資源グです。用語性能影・資源依・資源グという用語は「資源グループで資源グループRG一覧から」を指し、照合する値と誤認リスクの組合せは資源依・資源グ・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 性能影響の確認 DEP11**

    - 検証目的: 資源依存関係のResource Group Dependencyについて負荷と待ちを確認し、DEP11のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP11のRG一覧を表示します。
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

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP11のイベント順序を表示します。
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

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP11の依存照会を表示します。
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

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の database が画面・出力に表示されること
    ② ステップ2 の completed が画面・出力に表示されること
    ③ ステップ3 の NAME=app が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 構成監査 DEP08 {#c25-i0515}
*分類: 資源依存関係*  ・  難易度: 上級

構成監査では 資源依存関係 の RG一覧 を主操作として DEP08 を判定します。定義値と稼働値の一致への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP08 に残します。構成監査を補助する イベント順序 では completed を補助値として DEP08 へ保存します。主判定の構成監査では資源依存関係の RG一覧 から database_rg を読み DEP08 へ残します。証跡照合の構成監査では資源依存関係の database_rg と completed を DEP08 に保存します。記録対応の構成監査では資源依存関係の Parent RGとChild RG の証跡へ DEP08 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 「資源依存関係 Resource Group Dependency 構成監査 DEP08」を「資源依存関係 Resource Group Dependency 再始動後の確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は依存順を無視して子資源を先にオンを避けるため・イベント順序からcompletedを読むしてイベント順序を照合する。
    - B. 運用時に利用する技術的役割は依存順を無視して子資源を先にオンを避けるため・RG一覧からdatabase_rgを読むして資源グループを照合する。 ✅
    - C. 運用時に利用する技術的役割は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして構成データOを照合する。
    - D. 運用時に利用する技術的役割は実行結果の誤読を避けるため・トポロジー確で実行結果を確認するして実行結果を照合する。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能構成監・資源依・資源グでBの記述「資源グループで資源グループRG一覧から」に対応する項目は構成監査 DEP08（資源グ・資源グ・構成監）です。照合構成監・資源依・資源グに関する資源依存関係の仕様は「資源グループで資源グループRG一覧から database_rg」で、確認対象は資源グ・構成監・依存順です。比較資源依・構成監でA:の再始動後の確認 DEP15は「資源グループでイベント順序から」を述べるため、正答側の照合軸は資源グ・構成監・資源グです。項目構成監・資源依・資源グでC:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は依存順・資源依・資源グです。仕様構成監・資源依・資源グでD:のトポロジー確認 実行結果は「クラスタトポロジー、ネットワーク」を述べるため、正答側の照合軸は構成監・依存順・資源グです。用語構成監・資源依・資源グという用語は「資源グループで資源グループRG一覧から」を指し、照合する値と誤認リスクの組合せは資源依・資源グ・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 構成監査 DEP08**

    - 検証目的: 資源依存関係のResource Group Dependencyについて構成差分を監査し、DEP08のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP08のRG一覧を表示します。
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

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP08のイベント順序を表示します。
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

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP08の依存照会を表示します。
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

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の database が画面・出力に表示されること
    ② ステップ2 の completed が画面・出力に表示されること
    ③ ステップ3 の NAME=app が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 権限境界の確認 DEP12 {#c25-i0516}
*分類: 資源依存関係*  ・  難易度: 上級

権限境界の確認では 資源依存関係 の イベント順序 を主操作として DEP12 を判定します。参照操作と変更操作の分離への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP12 に残します。権限境界の確認を補助する 依存照会 では START_AFTER を補助値として DEP12 へ保存します。主判定の権限境界の確認では資源依存関係の イベント順序 から completed を読み DEP12 へ残します。証跡照合の権限境界の確認では資源依存関係の completed と START_AFTER を DEP12 に保存します。記録対応の権限境界の確認では資源依存関係の Parent RGとChild RG の証跡へ DEP12 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 権限境界の確認 DEP12を保守記録に説明する必要があります。クラスタ構成検証 SMIT Command Status 0004と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は巡回で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。クラスタ構成検証 SMIT Command Status 0004固有の属性も確認対象に含める。
    - B. 保守作業で参照する機能は権限境界確認でイベント順序を証跡に残し・資源グループでイベント順序から completed を読み。 ✅
    - C. 保守作業で参照する機能は収集でミラー更新状を証跡に残し・地理的ミラーの項目のミラー更新状態と取得時刻を記録し。
    - D. 保守作業で参照する機能はログ採取でログ採取を証跡に残し・検証後に構成を同期し・クラスタスナップショットを作成する操作。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能権限境・資源依・イベンでBの記述「資源グループでイベント順序から completed」に対応する項目は権限境界の確認 DEP12（資源グ・イベン・権限境）です。照合権限境・資源依・イベンに関する資源依存関係の仕様は「資源グループでイベント順序から completed を読み」で、確認対象はイベン・権限境・依存順です。比較資源依・権限境でA:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸は資源グ・権限境・イベンです。項目権限境・資源依・イベンでC:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は依存順・資源依・イベンです。仕様権限境・資源依・イベンでD:の同期確認 ログ採取は「検証後に構成を同期し、クラスタスナップショッ」を述べるため、正答側の照合軸は権限境・依存順・イベンです。用語権限境・資源依・イベンという用語は「資源グループでイベント順序から completed」を指し、照合する値と誤認リスクの組合せは資源依・イベン・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 権限境界の確認 DEP12**

    - 検証目的: 資源依存関係のResource Group Dependencyについて実行権限を点検し、DEP12のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP12のイベント順序を表示します。
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

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP12の依存照会を表示します。
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

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP12のRG一覧を表示します。
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

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の completed が画面・出力に表示されること
    ② ステップ2 の NAME=app が画面・出力に表示されること
    ③ ステップ3 の database が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 通常状態の確認 DEP01 {#c25-i0517}
*分類: 資源依存関係*  ・  難易度: 上級

通常状態の確認では 資源依存関係 の 依存照会 を主操作として DEP01 を判定します。基準値と現在値の差への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP01 に残します。通常状態の確認を補助する RG一覧 では database_rg を補助値として DEP01 へ保存します。主判定の通常状態の確認では資源依存関係の 依存照会 から START_AFTER を読み DEP01 へ残します。証跡照合の通常状態の確認では資源依存関係の START_AFTER と database_rg を DEP01 に保存します。記録対応の通常状態の確認では資源依存関係の Parent RGとChild RG の証跡へ DEP01 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 通常状態の確認 DEP01の役割を調べています。資源依存関係 Resource Group Dependency 変更前の確認の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は変更確認で資源グループを証跡に残し・資源グループで資源グループRG一覧から。
    - B. 障害切り分けに用いる役割は保護で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。クラスタ構成検証 SMIT Command Status 0259固有の属性も確認対象に含める。
    - C. 障害切り分けに用いる役割は解除でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。
    - D. 障害切り分けに用いる役割は通常状態確認で依存照会を証跡に残し・資源グループで依存照会から START_AFTER を読み。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能通常状・資源依・依存照でDの記述「資源グループで依存照会から START_AFTER」に対応する項目は通常状態の確認 DEP01（資源グ・依存照・通常状）です。照合通常状・資源依・依存照に関する資源依存関係の仕様は「資源グループで依存照会から START_AFTER を読み」で、確認対象は依存照・通常状・依存順です。比較資源依・通常状でA:の変更前の確認 DEP02は「資源グループで資源グループRG一覧から」を述べるため、正答側の照合軸は資源グ・通常状・依存照です。運用通常状・資源グでB:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸は依存照・資源依・通常状です。項目通常状・資源依・依存照でC:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は依存順・資源依・依存照です。用語通常状・資源依・依存照という用語は「資源グループで依存照会から START_AFTER」を指し、照合する値と誤認リスクの組合せは資源依・依存照・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 通常状態の確認 DEP01**

    - 検証目的: 資源依存関係のResource Group Dependencyについて通常状態を確定し、DEP01のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP01の依存照会を表示します。
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

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP01のRG一覧を表示します。
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

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP01のイベント順序を表示します。
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

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の NAME=app が画面・出力に表示されること
    ② ステップ2 の database が画面・出力に表示されること
    ③ ステップ3 の completed が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 資源依存関係 Resource Group Dependency 障害切り分け DEP04 {#c25-i0518}
*分類: 資源依存関係*  ・  難易度: 上級

障害切り分けでは 資源依存関係 の 依存照会 を主操作として DEP04 を判定します。最初に失敗した処理への注意として「依存順を無視して子資源を先にオンライン化する危険があります」を DEP04 に残します。障害切り分けを補助する RG一覧 では database_rg を補助値として DEP04 へ保存します。主判定の障害切り分けでは資源依存関係の 依存照会 から START_AFTER を読み DEP04 へ残します。証跡照合の障害切り分けでは資源依存関係の START_AFTER と database_rg を DEP04 に保存します。記録対応の障害切り分けでは資源依存関係の Parent RGとChild RG の証跡へ DEP04 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 資源依存関係 Resource Group Dependency 障害切り分け DEP04を保守記録に説明する必要があります。資源依存関係 Resource Group Dependency 代替経路の確認と取り違えない説明はどれですか。

    - A. 仕様上の役割は依存照会からSTART_AFTERを読むことで依存照会を確認し・依存順を無視して子資源を先にを防ぐ。
    - B. 仕様上の役割は依存照会からSTART_AFTERを読むことで依存照会を確認し・依存順を無視して子資源を先にを防ぐ。 ✅
    - C. 仕様上の役割は照合操作で確認欄を採取することでsyslogを確認し・ミラー再同期条件の誤読を防ぐ。
    - D. 仕様上の役割は整合確認で一致条件を確認することで一致条件を確認し・一致条件の誤読を防ぐ。

    正解: **B** ／ 難易度: 上級

    **解説:** 機能資源依・資源依・依存照でBの記述「資源グループで依存照会から START_AFTER」に対応する項目は障害切り分け DEP04（資源グ・依存照・資源依）です。照合資源依・資源依・依存照に関する資源依存関係の仕様は「資源グループで依存照会から START_AFTER を読み」で、確認対象は依存照・資源依・依存順です。比較資源依・資源依でA:の代替経路の確認 DEP10は「資源グループで依存照会から」を述べるため、正答側の照合軸は資源グ・資源依・依存照です。項目資源依・資源依・依存照でC:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は依存順・資源依・依存照です。仕様資源依・資源依・依存照でD:の整合確認 一致条件は「リソースグループの状態と所有ノードを表示する」を述べるため、正答側の照合軸は資源依・依存順・依存照です。用語資源依・資源依・依存照という用語は「資源グループで依存照会から START_AFTER」を指し、照合する値と誤認リスクの組合せは資源依・依存照・依存順です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **資源依存関係 Resource Group Dependency 障害切り分け DEP04**

    - 検証目的: 資源依存関係のResource Group Dependencyについて障害範囲を限定し、DEP04のParent RGとChild RGを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象DEP04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclmgr query resource_group app_rgを指定し、DEP04の依存照会を表示します。
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

    画面・出力にあるNAME=appを読み、Parent RGとChild RGと対象DEP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へclRGinfo -vを指定し、DEP04のRG一覧を表示します。
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

    画面・出力にあるdatabaseを読み、Parent RGとChild RGと対象DEP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の資源依存関係を確認する入力画面です。COMMAND入力口へgrep -i "database_rg|app_rg" /var/hacmp/log/hacmp.outを指定し、DEP04のイベント順序を表示します。
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

    画面・出力にあるcompletedを読み、Parent RGとChild RGと対象DEP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の NAME=app が画面・出力に表示されること
    ② ステップ2 の database が画面・出力に表示されること
    ③ ステップ3 の completed が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278




## PowerHA SystemMirror 7.2 > 障害調査

### cldump 所有先確認 変更証跡 {#c25-i0519}
*分類: 障害調査*  ・  難易度: 中級

PowerHA SystemMirror 7.2 の 障害調査 で扱う「cldump 所有先確認 変更証跡」は、クラスタ構成と状態をスナップショットとして表示するコマンドを所有先確認の観点で確認する技術項目です。SubState 行とcldump 040を同じ記録で見比べることで、所有ノードの誤認を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** cldump 所有先確認 変更証跡を同一分類のトポロジー Cluster Topology 代替経路の確認 TOPO10と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は代替経路確認でクラスタ照会を証跡に残し・クラスタートポロジーでクラスタ照会から。
    - B. コマンドまたは機能の用途は監査でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。
    - C. コマンドまたは機能の用途は保護でVG varを証跡に残し・地理的ミラーの項目のVG vary状態と取得時刻を記録し。GLVM地理的ミラー Mirror Pool 0255固有の属性も確認対象に含める。
    - D. コマンドまたは機能の用途は変更証跡で変更証跡を証跡に残し・クラスタ構成と状態をスナップショットとして表示するコマンドを。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能変更証・所有先・変更証でDの記述「クラスタ構成と状態をスナップショットとして表示するコマン」に対応する項目は所有先確認 変更証跡（cld・変更証・変更証）です。照合変更証・所有先・変更証に関する障害調査の仕様は「クラスタ構成と状態をスナップショットとして表示するコマンドを所有先確」で、確認対象は変更証・変更証・変更証です。比較変更証・所有先・変更証・変更証でA:の代替経路の確認 TOPO10は「クラスタートポロジーでクラスタ照会から」を述べるため、正答側の照合軸はcld・変更証・変更証です。運用変更証・cldでB:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は変更証・所有先・変更証です。項目変更証・所有先・変更証でC:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は変更証・所有先・変更証です。用語変更証・所有先・変更証という用語は「クラスタ構成と状態をスナップショットとして表示するコ」を指し、照合する値と誤認リスクの組合せは所有先・変更証・変更証です。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **cldump 所有先確認 変更証跡**

    - 検証目的: 障害調査のcldump 所有先確認 変更証跡について、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、障害調査の対象へ進みます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clstat -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstat - Cluster Status Monitor
    Cluster: prodcluster040
    State: UP
    SubState: STABLE
    Resource Group: rg_app_040
    State: Online
    ```

    画面・出力には clstat が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。SubState 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> /usr/es/sbin/cluster/utilities/cldump
    → Enter を押す
    ```

    画面・出力:
    ```text
    Cluster prodcluster040
    Node clnode_1 State UP
    Network net_ether_01
    Resource Group rg_app_040 Online
    ```

    画面・出力には Cluster が含まれ、cldump 所有先確認 変更証跡の証跡を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の詳細確認画面です。表示名とメッセージ形式を照合し、所有ノードの誤認を切り分けます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr -a state query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    STATE="ONLINE"
    ```

    画面・出力には STATE= が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の clstat が画面・出力に表示されること
    ② ステップ2 の Cluster が画面・出力に表示されること
    ③ ステップ3 の STATE= が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting



### clmgr query cluster 所有先確認 製品レベル {#c25-i0520}
*分類: 障害調査*  ・  難易度: 中級

PowerHA SystemMirror 7.2 の 障害調査 で扱う「clmgr query cluster 所有先確認 製品レベル」は、クラスタ名、状態、バージョンなどのクラスタ属性を表示するコマンドを所有先確認の観点で確認する技術項目です。SubState 行とclstrmgrES 032を同じ記録で見比べることで、サービスIP定義の不一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** clmgr query cluster 所有先確認 製品レベルを同一分類のクラスタ起動・停止 Cluster Services Lifecycleと比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はCluster Servicesで状態確認から ST_STABLE を読み・ST_STABLE とである。状態確認からST_STABLEを読むときは管理設定と資源状態の混同を防ぐ。
    - B. 構成を確認する際の意味はクラスタ名・状態・バージョンなどのクラスタ属性を表示するコマンドを所有先確認する。所有先確認で製品レベルを確認するときは製品レベルの誤読を防ぐ。 ✅
    - C. 構成を確認する際の意味は獲得処理の獲得イベントと取得時刻を記録し・自動戻し条件の誤読を防ぐである。調査操作で保守欄を引き継ぎするときは自動戻し条件の誤読を防ぐ。
    - D. 構成を確認する際の意味はクラスター資源のトポロジ要約と取得時刻を記録し・検証ログの採取漏れを防ぐである。保守操作で監査欄を保存するときは検証ログの採取漏れを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能所有先・所有先・製品レでBの記述「クラスタ名、状態、バージョンなどのクラスタ属性を表示する」に対応する項目は所有先確認 製品レベル（clm・製品レ・所有先）です。照合所有先・所有先・製品レに関する障害調査の仕様は「クラスタ名、状態、バージョンなどのクラスタ属性を表示するコマンドを所」で、確認対象は製品レ・所有先・製品レです。比較所有先・所有先・製品レ・製品レでA:の性能影響の確認 START11は「Cluster Servicesで状態確認か」を述べるため、正答側の照合軸はclm・所有先・製品レです。項目所有先・所有先・製品レでC:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は製品レ・所有先・製品レです。仕様所有先・所有先・製品レでD:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は所有先・製品レ・製品レです。用語所有先・所有先・製品レという用語は「クラスタ名、状態、バージョンなどのクラスタ属性を表示」を指し、照合する値と誤認リスクの組合せは所有先・製品レ・製品レです。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **clmgr query cluster 所有先確認 製品レベル**

    - 検証目的: 障害調査のclmgr query cluster 所有先確認 製品レベルについて、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、障害調査の対象へ進みます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> cltopinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Cluster Name:    prodcluster032
    Heartbeat Type:  Unicast
    Repository Disk: hdisk2
    Resource Group rg_app_032
    Service IP Label clst_svcIP_032
    ```

    画面・出力には Cluster が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。SubState 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clRGinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Group Name     Group State                  Node
    rg_app_032     ONLINE                       clnode_1
                   OFFLINE                      clnode_2
    ```

    画面・出力には Group が含まれ、clmgr query cluster 所有先確認 製品レベルの証跡を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の詳細確認画面です。表示名とメッセージ形式を照合し、サービスIP定義の不一致を切り分けます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr query resource_group rg_app_032
    → Enter を押す
    ```

    画面・出力:
    ```text
    NAME="rg_app_032"
    STATE="ONLINE"
    PARTICIPATING_NODES="clnode_1 clnode_2"
    ```

    画面・出力には NAME= が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Cluster が画面・出力に表示されること
    ② ステップ2 の Group が画面・出力に表示されること
    ③ ステップ3 の NAME= が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting



### clmgr start cluster 整合確認 メッセージ行 {#c25-i0521}
*分類: 障害調査*  ・  難易度: 中級

PowerHA SystemMirror 7.2 の 障害調査 で扱う「clmgr start cluster 整合確認 メッセージ行」は、クラスタサービスを開始し、リソースグループをオンライン化する操作を整合確認の観点で確認する技術項目です。SubState 行とrg_app_024を同じ記録で見比べることで、クラスタ版数混在の誤認を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** clmgr start cluster 整合確認 メッセージ行を同一分類のノード状態 PowerHA Node State 復旧準備 NODE05と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はPowerHA Node Stateでサブシステム状態から クラスター管理プロセス を読みである。SRC状態からクラスター管理プロセスときは基本ソフト稼働とクラスタ稼働を防ぐ。
    - B. 管理対象との関係を表す説明はオンラインノードの資源グループRG現在位置と取得時刻を記録し・資源グループ位置の誤認を防ぐである。復旧操作で点検欄を確認するときは資源グループ位置の誤認を防ぐ。
    - C. 管理対象との関係を表す説明はシステム管理コマンドの検証進行率と取得時刻を記録し・検証ログの採取漏れを防ぐである。保守操作で監査欄を保存するときは検証ログの採取漏れを防ぐ。
    - D. 管理対象との関係を表す説明はクラスタサービスを開始し・リソースグループをオンライン化する操作を整合確認する。整合確認でメッセージ行を確認するときはメッセージ行の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能整合確・整合・メッセでDの記述「クラスタサービスを開始し、リソースグループをオンライン化」に対応する項目は整合確認 メッセージ行（clm・メッセ・整合確）です。照合整合確・整合・メッセに関する障害調査の仕様は「クラスタサービスを開始し、リソースグループをオンライン化する操作を整」で、確認対象はメッセ・整合確・メッセです。比較整合確・整合・メッセ・メッセでA:の復旧準備 NODE05は「PowerHA Node Stateでサブシ」を述べるため、正答側の照合軸はclm・整合確・メッセです。運用整合確・clmでB:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸はメッセ・整合・整合確です。項目整合確・整合・メッセでC:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はメッセ・整合・メッセです。用語整合確・整合・メッセという用語は「クラスタサービスを開始し、リソースグループをオンライ」を指し、照合する値と誤認リスクの組合せは整合・メッセ・メッセです。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **clmgr start cluster 整合確認 メッセージ行**

    - 検証目的: 障害調査のclmgr start cluster 整合確認 メッセージ行について、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、障害調査の対象へ進みます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr start cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Starting Cluster Services on node: clnode_1
    clnode_1: Exit status = 0
    The cluster is now online.
    ```

    画面・出力には Starting が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。SubState 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr sync cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verifying additional prerequisites for Dynamic Reconfiguration...
    Verification has completed normally.
    clsnapshot: Succeeded creating Cluster Snapshot: active.0
    ```

    画面・出力には Verifying が含まれ、clmgr start cluster 整合確認 メッセージ行の証跡を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の詳細確認画面です。表示名とメッセージ形式を照合し、クラスタ版数混在の誤認を切り分けます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> cat /usr/es/sbin/cluster/netmon.cf
    → Enter を押す
    ```

    画面・出力:
    ```text
    !REQD en0 192.168.100.1
    ```

    画面・出力には REQD が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Starting が画面・出力に表示されること
    ② ステップ2 の Verifying が画面・出力に表示されること
    ③ ステップ3 の REQD が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting



### cltopinfo 同期確認 共有定義 {#c25-i0522}
*分類: 障害調査*  ・  難易度: 上級

PowerHA SystemMirror 7.2 の 障害調査 で扱う「cltopinfo 同期確認 共有定義」は、クラスタトポロジー、ネットワーク、サービスIP、リソースグループを表示するコマンドを同期確認の観点で確認する技術項目です。SubState 行とclstrmgrES 056を同じ記録で見比べることで、同期前構成の採用を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** cltopinfo 同期確認 共有定義を同一分類のサービスIP Service IP Label ログとの照合 SVCIP07と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はIP資源照会からアドレスを読むことでサービスアドを確認し・永続アドレスとサービスアドレを防ぐ。
    - B. 構成を確認する際の意味は復旧操作で点検欄を確認することで資源グループを確認し・資源グループ位置の誤認を防ぐ。
    - C. 構成を確認する際の意味は同期確認で共有定義を確認することで共有定義を確認し・共有定義の誤読を防ぐ。 ✅
    - D. 構成を確認する際の意味は監査操作で記録欄を比較することで基本ソフトAを確認し・syslogとhacmp.oを防ぐ。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能同期確・同期・共有定でCの記述「クラスタトポロジー、ネットワーク、サービスIP」に対応する項目は同期確認 共有定義（clt・共有定・同期確）です。照合同期確・同期・共有定に関する障害調査の仕様は「クラスタトポロジー、ネットワーク、サービスIP」で、確認対象は共有定・同期確・共有定です。比較同期確・同期・共有定・共有定でA:のログとの照合 SVCIP07は「IP Service IPでサービスアドレス」を述べるため、正答側の照合軸はclt・同期確・共有定です。運用同期確・cltでB:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は共有定・同期・同期確です。仕様同期確・同期・共有定でD:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸は同期確・共有定・共有定です。用語同期確・同期・共有定という用語は「クラスタトポロジー、ネットワーク、サービスIP」を指し、照合する値と誤認リスクの組合せは同期・共有定・共有定です。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **cltopinfo 同期確認 共有定義**

    - 検証目的: 障害調査のcltopinfo 同期確認 共有定義について、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、障害調査の対象へ進みます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on the following:
            Cluster Topology
            Cluster Resources
    Completed 100 percent of the verification checks
    Verification exiting with error count: 0
    ```

    画面・出力には Verification が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。SubState 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    CLUSTER_NAME="prodcluster056"
    STATE="ONLINE"
    VERSION="7.2.2.1"
    ```

    画面・出力には CLUSTER が含まれ、cltopinfo 同期確認 共有定義の証跡を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の詳細確認画面です。表示名とメッセージ形式を照合し、同期前構成の採用を切り分けます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr -cv -a name,state,raw_state query node
    → Enter を押す
    ```

    画面・出力:
    ```text
    # NAME:STATE:RAW_STATE
    clnode_1:NORMAL:ST_STABLE
    clnode_2:NORMAL:ST_STABLE
    ```

    画面・出力には NAME が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Verification が画面・出力に表示されること
    ② ステップ2 の CLUSTER が画面・出力に表示されること
    ③ ステップ3 の NAME が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting



### cltopinfo 状態確認 対象ファイル {#c25-i0523}
*分類: 障害調査*  ・  難易度: 中級

PowerHA SystemMirror 7.2 の 障害調査 で扱う「cltopinfo 状態確認 対象ファイル」は、クラスタトポロジー、ネットワーク、サービスIP、リソースグループを表示するコマンドを状態確認の観点で確認する技術項目です。SubState 行とcldump 016を同じ記録で見比べることで、同期前構成の採用を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** cltopinfo 状態確認 対象ファイルを同一分類のサービスIP Service IP Label 変更後の確認 SVCIP03と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は変更確認でインターフェを証跡に残し・IP Service IPでインターフェースから。
    - B. コマンドまたは機能の用途は復旧で失敗ラベルを証跡に残し・イベント要約の失敗ラベルと取得時刻を記録し。
    - C. コマンドまたは機能の用途は保護で移動履歴を証跡に残し・ノード一覧の移動履歴と取得時刻を記録し。
    - D. コマンドまたは機能の用途は状態確認で対象ファイルを証跡に残し・クラスタトポロジー・ネットワーク・サービスIP。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能状態確・状態・対象フでDの記述「クラスタトポロジー、ネットワーク、サービスIP」に対応する項目は状態確認 対象ファイル（clt・対象フ・状態確）です。照合状態確・状態・対象フに関する障害調査の仕様は「クラスタトポロジー、ネットワーク、サービスIP」で、確認対象は対象フ・状態確・対象フです。比較状態確・状態・対象フ・対象フでA:の変更後の確認 SVCIP03は「IP Service IPでインターフェース」を述べるため、正答側の照合軸はclt・状態確・対象フです。運用状態確・cltでB:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は対象フ・状態・状態確です。項目状態確・状態・対象フでC:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は対象フ・状態・対象フです。用語状態確・状態・対象フという用語は「クラスタトポロジー、ネットワーク、サービスIP」を指し、照合する値と誤認リスクの組合せは状態・対象フ・対象フです。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **cltopinfo 状態確認 対象ファイル**

    - 検証目的: 障害調査のcltopinfo 状態確認 対象ファイルについて、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、障害調査の対象へ進みます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr verify cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on the following:
            Cluster Topology
            Cluster Resources
    Completed 100 percent of the verification checks
    Verification exiting with error count: 0
    ```

    画面・出力には Verification が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。SubState 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    CLUSTER_NAME="prodcluster016"
    STATE="ONLINE"
    VERSION="7.2.2.1"
    ```

    画面・出力には CLUSTER が含まれ、cltopinfo 状態確認 対象ファイルの証跡を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の詳細確認画面です。表示名とメッセージ形式を照合し、同期前構成の採用を切り分けます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr -cv -a name,state,raw_state query node
    → Enter を押す
    ```

    画面・出力:
    ```text
    # NAME:STATE:RAW_STATE
    clnode_1:NORMAL:ST_STABLE
    clnode_2:NORMAL:ST_STABLE
    ```

    画面・出力には NAME が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Verification が画面・出力に表示されること
    ② ステップ2 の CLUSTER が画面・出力に表示されること
    ③ ステップ3 の NAME が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting



### lssrc -ls clstrmgrES 版数確認 障害記録 {#c25-i0524}
*分類: 障害調査*  ・  難易度: 初級

PowerHA SystemMirror 7.2 の 障害調査 で扱う「lssrc -ls clstrmgrES 版数確認 障害記録」は、Cluster Manager の状態、クラスタ版数、ノード版数を表示するコマンドを版数確認の観点で確認する技術項目です。SubState 行とclstrmgrES 008を同じ記録で見比べることで、検証警告の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** lssrc -ls clstrmgrES 版数確認 障害記録を同一分類のclRGinfo トポロジー確認 冗長性確認と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は版数確認で障害記録を証跡に残し・Cluster Manager の状態・クラスタ版数。 ✅
    - B. 構成を確認する際の意味は冗長性確認で冗長性確認を証跡に残し・リソースグループの状態と所有ノードを表示するコマンドをトポロ。
    - C. 構成を確認する際の意味は棚卸で優先ノード一を証跡に残し・資源グループの優先ノード一覧と取得時刻を記録し。
    - D. 構成を確認する際の意味は確認で移動履歴を証跡に残し・ノード一覧の移動履歴と取得時刻を記録し。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能版数確・版数・障害記でAの記述「Cluster Manager の状態、クラスタ版数」に対応する項目は版数確認 障害記録（lss・障害記・版数確）です。照合版数確・版数・障害記に関する障害調査の仕様は「Cluster Manager の状態、クラスタ版数」で、確認対象は障害記・版数確・障害記です。運用版数確・lssでB:のトポロジー確認 冗長性確認は「リソースグループの状態と所有ノードを表示する」を述べるため、正答側の照合軸は障害記・版数・版数確です。項目版数確・版数・障害記でC:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は障害記・版数・障害記です。仕様版数確・版数・障害記でD:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は版数確・障害記・障害記です。用語版数確・版数・障害記という用語は「Cluster Manager の状態」を指し、照合する値と誤認リスクの組合せは版数・障害記・障害記です。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **lssrc -ls clstrmgrES 版数確認 障害記録**

    - 検証目的: 障害調査のlssrc -ls clstrmgrES 版数確認 障害記録について、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、障害調査の対象へ進みます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> lssrc -ls clstrmgrES
    → Enter を押す
    ```

    画面・出力:
    ```text
    Current state: ST_STABLE
    CLversion: 16
    local node vrmf is 7200
    cluster fix level is "0"
    ```

    画面・出力には Current が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。SubState 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> ps -ef | grep clstrmgrES
    → Enter を押す
    ```

    画面・出力:
    ```text
    root 18363 3346 3 11:02:05 - 10:20 /usr/es/sbin/cluster/clstrmgrES
    ```

    画面・出力には root が含まれ、lssrc -ls clstrmgrES 版数確認 障害記録の証跡を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の詳細確認画面です。表示名とメッセージ形式を照合し、検証警告の見落としを切り分けます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> lssrc -g cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subsystem         Group            PID          Status
    clstrmgrES        cluster          544802       active
    clcomdES          clcomdES         204920       active
    ```

    画面・出力には Subsystem が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Current が画面・出力に表示されること
    ② ステップ2 の root が画面・出力に表示されること
    ③ ステップ3 の Subsystem が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting



### lssrc -ls clstrmgrES 起動確認 時刻情報 {#c25-i0525}
*分類: 障害調査*  ・  難易度: 中級

PowerHA SystemMirror 7.2 の 障害調査 で扱う「lssrc -ls clstrmgrES 起動確認 時刻情報」は、Cluster Manager の状態、クラスタ版数、ノード版数を表示するコマンドを起動確認の観点で確認する技術項目です。SubState 行とrg_app_048を同じ記録で見比べることで、検証警告の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** lssrc -ls clstrmgrES 起動確認 時刻情報を同一分類の障害調査 hacmp.out Event Summary 引継ぎ記録 FAIL09と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はcluster historyだを避けるため・エラー記録からIDENTIFIERを読むしてエラー記録を照合する。
    - B. 管理対象との関係を表す説明は遠隔ボリュームRPV経路断の見落を避けるため・変更確認操作で採取欄を棚卸するして基本ソフトAを照合する。
    - C. 管理対象との関係を表す説明は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして資源グループを照合する。
    - D. 管理対象との関係を表す説明は時刻情報の誤読を避けるため・起動確認で時刻情報を確認するして時刻情報を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能起動確・起動・時刻情でDの記述「Cluster Manager の状態、クラスタ版数」に対応する項目は起動確認 時刻情報（lss・時刻情・起動確）です。照合起動確・起動・時刻情に関する障害調査の仕様は「Cluster Manager の状態、クラスタ版数」で、確認対象は時刻情・起動確・時刻情です。比較起動確・起動・時刻情・時刻情でA:の引継ぎ記録 FAIL09は「hacmp.out Eventでエラー記録か」を述べるため、正答側の照合軸はlss・起動確・時刻情です。運用起動確・lssでB:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸は時刻情・起動・起動確です。項目起動確・起動・時刻情でC:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は時刻情・起動・時刻情です。用語起動確・起動・時刻情という用語は「Cluster Manager の状態」を指し、照合する値と誤認リスクの組合せは起動・時刻情・時刻情です。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **lssrc -ls clstrmgrES 起動確認 時刻情報**

    - 検証目的: 障害調査のlssrc -ls clstrmgrES 起動確認 時刻情報について、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、障害調査の対象へ進みます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> lssrc -ls clstrmgrES
    → Enter を押す
    ```

    画面・出力:
    ```text
    Current state: ST_STABLE
    CLversion: 16
    local node vrmf is 7200
    cluster fix level is "0"
    ```

    画面・出力には Current が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。SubState 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> ps -ef | grep clstrmgrES
    → Enter を押す
    ```

    画面・出力:
    ```text
    root 18363 3346 3 11:02:05 - 10:20 /usr/es/sbin/cluster/clstrmgrES
    ```

    画面・出力には root が含まれ、lssrc -ls clstrmgrES 起動確認 時刻情報の証跡を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の詳細確認画面です。表示名とメッセージ形式を照合し、検証警告の見落としを切り分けます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> lssrc -g cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Subsystem         Group            PID          Status
    clstrmgrES        cluster          544802       active
    clcomdES          clcomdES         204920       active
    ```

    画面・出力には Subsystem が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Current が画面・出力に表示されること
    ② ステップ2 の root が画面・出力に表示されること
    ③ ステップ3 の Subsystem が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting



### 障害調査 hacmp.out Event Summary ログとの照合 FAIL07 {#c25-i0526}
*分類: 障害調査*  ・  難易度: 中級

ログとの照合では 障害調査 の 主要ログ を主操作として FAIL07 を判定します。時刻と対象識別子への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL07 に残します。ログとの照合を補助する マネージャーログ では clstrmgrES を補助値として FAIL07 へ保存します。主判定のログとの照合では障害調査の 主要ログ から ACQUISITION を読み FAIL07 へ残します。証跡照合のログとの照合では障害調査の ACQUISITION と clstrmgrES を FAIL07 に保存します。記録対応のログとの照合では障害調査の Event NameとExit Status の証跡へ FAIL07 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary ログとの照合 FAIL07の役割を調べています。clstat・SNMP clinfoES Status Path 通常状態の確認の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は主要ログからACQUISITIONを読むことで主要ログを確認し・cluster historを防ぐ。 ✅
    - B. 障害切り分けに用いる役割はclinfoES状態からclinfoESことでclinfoを確認し・SNMP情報の残留を実ノードを防ぐ。
    - C. 障害切り分けに用いる役割は点検操作で判定欄を記録することで獲得イベントを確認し・依存リソース順序の見落としを防ぐ。
    - D. 障害切り分けに用いる役割はサンプル採取でサンプル採取を確認することでサンプル採取を確認し・サンプル採取の誤読を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能主要ロ・cluでAの記述「hacmp.out Eventで主要ログから」に対応する項目はログとの照合 FAIL07（hac・主要ロ・ログと）です。照合主要ロ・ログとに関する障害調査の仕様は「hacmp.out Eventで主要ログから」で、確認対象は主要ロ・ログと・cluです。運用ログと・hacでB:の通常状態の確認 CLSTAT01は「clstatでclinfoES状態から」を述べるため、正答側の照合軸は主要ロ・障害調・ログとです。項目主要ロ・ログとでC:のAcquisitionは「Acquisitionの獲得イベントと取得時」を述べるため、正答側の照合軸はclu・障害調・主要ロです。仕様主要ロ・ログとでD:の状態確認 サンプル採取は「ノードの状態と raw_state」を述べるため、正答側の照合軸はログと・clu・主要ロです。用語主要ロ・ログとという用語は「hacmp.out Eventで主要ログから」を指し、照合する値と誤認リスクの組合せは障害調・主要ロ・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary ログとの照合 FAIL07**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて操作とログを対応し、FAIL07のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL07の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL07のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL07のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ACQUISITION が画面・出力に表示されること
    ② ステップ2 の clstrmgrES が画面・出力に表示されること
    ③ ステップ3 の IDENTIFIER が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 代替経路の確認 FAIL10 {#c25-i0527}
*分類: 障害調査*  ・  難易度: 中級

代替経路の確認では 障害調査 の 主要ログ を主操作として FAIL10 を判定します。主経路との役割差への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL10 に残します。代替経路の確認を補助する マネージャーログ では clstrmgrES を補助値として FAIL10 へ保存します。主判定の代替経路の確認では障害調査の 主要ログ から ACQUISITION を読み FAIL10 へ残します。証跡照合の代替経路の確認では障害調査の ACQUISITION と clstrmgrES を FAIL10 に保存します。記録対応の代替経路の確認では障害調査の Event NameとExit Status の証跡へ FAIL10 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 代替経路の確認 FAIL10を保守記録に説明する必要があります。clstat・SNMP clinfoES Status Path 依存関係の確認と取り違えない説明はどれですか。

    - A. 仕様上の役割はSNMP情報の残留を実ノード状態を避けるため・clinfoES状態からclinfoESしてclinfoを照合する。
    - B. 仕様上の役割は獲得失敗ログの未採取を避けるため・表示操作で対象欄を追跡するして獲得イベントを照合する。
    - C. 仕様上の役割はチューニングの誤読を避けるため・トポロジー確でチューニングを確認するしてチューニングを照合する。
    - D. 仕様上の役割はcluster historyだを避けるため・主要ログからACQUISITIONを読むして主要ログを照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能主要ロ・cluでDの記述「hacmp.out Eventで主要ログから」に対応する項目は代替経路の確認 FAIL10（hac・主要ロ・代替経）です。照合主要ロ・代替経に関する障害調査の仕様は「hacmp.out Eventで主要ログから」で、確認対象は主要ロ・代替経・cluです。比較障害調・代替経でA:の依存関係の確認 CLSTAT13は「clstatでclinfoES状態から」を述べるため、正答側の照合軸はhac・代替経・主要ロです。運用代替経・hacでB:のAcquisitionは「Acquisitionの獲得イベントと取得時」を述べるため、正答側の照合軸は主要ロ・障害調・代替経です。項目主要ロ・代替経でC:のトポロジー確認 チューニング値は「検証後に構成を同期し、クラスタスナップショッ」を述べるため、正答側の照合軸はclu・障害調・主要ロです。用語主要ロ・代替経という用語は「hacmp.out Eventで主要ログから」を指し、照合する値と誤認リスクの組合せは障害調・主要ロ・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 代替経路の確認 FAIL10**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて代替手段の成立を確認し、FAIL10のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL10の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL10のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL10のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ACQUISITION が画面・出力に表示されること
    ② ステップ2 の clstrmgrES が画面・出力に表示されること
    ③ ステップ3 の IDENTIFIER が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 依存関係の確認 FAIL13 {#c25-i0528}
*分類: 障害調査*  ・  難易度: 中級

依存関係の確認では 障害調査 の 主要ログ を主操作として FAIL13 を判定します。前提資源と後続処理の順序への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL13 に残します。依存関係の確認を補助する マネージャーログ では clstrmgrES を補助値として FAIL13 へ保存します。主判定の依存関係の確認では障害調査の 主要ログ から ACQUISITION を読み FAIL13 へ残します。証跡照合の依存関係の確認では障害調査の ACQUISITION と clstrmgrES を FAIL13 に保存します。記録対応の依存関係の確認では障害調査の Event NameとExit Status の証跡へ FAIL13 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 依存関係の確認 FAIL13を同一分類のクラスタ構成検証 Cluster Topology 0043と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は復旧でODM登録値を証跡に残し・Cluster TopologyのODM登録値と取得時刻を記。
    - B. コマンドまたは機能の用途は保守でRG現在位置を証跡に残し・Online NodeのRG現在位置と取得時刻を記録し。
    - C. コマンドまたは機能の用途は所有先確認で製品レベルを証跡に残し・クラスタ名・状態・バージョンなどのクラスタ属性を表示するコマ。
    - D. コマンドまたは機能の用途は依存関係確認で主要ログを証跡に残し・hacmp.out Eventで主要ログから。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能主要ロ・cluでDの記述「hacmp.out Eventで主要ログから」に対応する項目は依存関係の確認 FAIL13（hac・主要ロ・依存関）です。照合主要ロ・依存関に関する障害調査の仕様は「hacmp.out Eventで主要ログから」で、確認対象は主要ロ・依存関・cluです。比較障害調・依存関でA:のCluster Topologyは「Cluster TopologyのODM登録」を述べるため、正答側の照合軸はhac・依存関・主要ロです。運用依存関・hacでB:のOnline Nodeは「Online NodeのRG現在位置と取得時」を述べるため、正答側の照合軸は主要ロ・障害調・依存関です。項目主要ロ・依存関でC:の所有先確認 製品レベルは「クラスタ名、状態、バージョンなどのクラスタ属」を述べるため、正答側の照合軸はclu・障害調・主要ロです。用語主要ロ・依存関という用語は「hacmp.out Eventで主要ログから」を指し、照合する値と誤認リスクの組合せは障害調・主要ロ・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 依存関係の確認 FAIL13**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて依存資源を点検し、FAIL13のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL13の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL13のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL13のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ACQUISITION が画面・出力に表示されること
    ② ステップ2 の clstrmgrES が画面・出力に表示されること
    ③ ステップ3 の IDENTIFIER が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 停止前の確認 FAIL14 {#c25-i0529}
*分類: 障害調査*  ・  難易度: 中級

停止前の確認では 障害調査 の マネージャーログ を主操作として FAIL14 を判定します。処理中資源と未完了要求への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL14 に残します。停止前の確認を補助する エラー記録 では IDENTIFIER を補助値として FAIL14 へ保存します。主判定の停止前の確認では障害調査の マネージャーログ から clstrmgrES を読み FAIL14 へ残します。証跡照合の停止前の確認では障害調査の clstrmgrES と IDENTIFIER を FAIL14 に保存します。記録対応の停止前の確認では障害調査の Event NameとExit Status の証跡へ FAIL14 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 「障害調査 hacmp.out Event Summary 停止前の確認 FAIL14」を「clstat・SNMP clinfoES Status Path 代替経路の確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はclinfoES状態からclinfoESことでclinfoを確認し・SNMP情報の残留を実ノードを防ぐ。
    - B. 運用時に利用する技術的役割はマネージャーログからクラスター管理プロセことでマネージャーを確認し・cluster historを防ぐ。 ✅
    - C. 運用時に利用する技術的役割は表示操作で対象欄を追跡することで優先ノード一を確認し・獲得失敗ログの未採取を防ぐ。
    - D. 運用時に利用する技術的役割は冗長性確認で冗長性確認を確認することで冗長性確認を確認し・冗長性確認の誤読を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能マネー・cluでBの記述「hacmp.out Eventでマネージャーログから」に対応する項目は停止前の確認 FAIL14（hac・マネー・停止確）です。照合マネー・停止確に関する障害調査の仕様は「hacmp.out Eventでマネージャーログから」で、確認対象はマネー・停止確・cluです。比較障害調・停止確でA:の代替経路の確認 CLSTAT10は「clstatでclinfoES状態から」を述べるため、正答側の照合軸はhac・停止確・マネーです。項目マネー・停止確でC:のGroup Nameは「Resource Groupの優先ノード一覧」を述べるため、正答側の照合軸はclu・障害調・マネーです。仕様マネー・停止確でD:のトポロジー確認 冗長性確認は「リソースグループの状態と所有ノードを表示する」を述べるため、正答側の照合軸は停止確・clu・マネーです。用語マネー・停止確という用語は「hacmp.out Eventでマネージャーログから」を指し、照合する値と誤認リスクの組合せは障害調・マネー・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 停止前の確認 FAIL14**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて安全な停止条件を確認し、FAIL14のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL14のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL14のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL14の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の clstrmgrES が画面・出力に表示されること
    ② ステップ2 の IDENTIFIER が画面・出力に表示されること
    ③ ステップ3 の ACQUISITION が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 再始動後の確認 FAIL15 {#c25-i0530}
*分類: 障害調査*  ・  難易度: 中級

再始動後の確認では 障害調査 の エラー記録 を主操作として FAIL15 を判定します。再開点と未処理データへの注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL15 に残します。再始動後の確認を補助する 主要ログ では ACQUISITION を補助値として FAIL15 へ保存します。主判定の再始動後の確認では障害調査の エラー記録 から IDENTIFIER を読み FAIL15 へ残します。証跡照合の再始動後の確認では障害調査の IDENTIFIER と ACQUISITION を FAIL15 に保存します。記録対応の再始動後の確認では障害調査の Event NameとExit Status の証跡へ FAIL15 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 再始動後の確認 FAIL15の役割を調べています。clstat・SNMP clinfoES Status Path 引継ぎ記録の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はclstatでクラスタ表示を証跡に残し・clstatでクラスタ表示から Cluster を読み。
    - B. 表示や設定で扱う内容は登録で優先ノード一を証跡に残し・Resource Groupの優先ノード一覧と取得時刻を記録。
    - C. 表示や設定で扱う内容は再始動確認でエラー記録を証跡に残し・hacmp.out Eventでエラー記録から。 ✅
    - D. 表示や設定で扱う内容は解除でODM登録値を証跡に残し・Cluster TopologyのODM登録値と取得時刻を記。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能エラー・cluでCの記述「hacmp.out Eventでエラー記録から」に対応する項目は再始動後の確認 FAIL15（hac・エラー・再始動）です。照合エラー・再始動に関する障害調査の仕様は「hacmp.out Eventでエラー記録から」で、確認対象はエラー・再始動・cluです。比較障害調・再始動でA:の引継ぎ記録 CLSTAT09は「clstatでクラスタ表示から」を述べるため、正答側の照合軸はhac・再始動・エラーです。運用再始動・hacでB:のGroup Nameは「Resource Groupの優先ノード一覧」を述べるため、正答側の照合軸はエラー・障害調・再始動です。仕様エラー・再始動でD:のCluster Topologyは「Cluster TopologyのODM登録」を述べるため、正答側の照合軸は再始動・clu・エラーです。用語エラー・再始動という用語は「hacmp.out Eventでエラー記録から」を指し、照合する値と誤認リスクの組合せは障害調・エラー・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 再始動後の確認 FAIL15**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて再始動結果を検証し、FAIL15のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL15のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL15の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL15のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IDENTIFIER が画面・出力に表示されること
    ② ステップ2 の ACQUISITION が画面・出力に表示されること
    ③ ステップ3 の clstrmgrES が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 変更前の確認 FAIL02 {#c25-i0531}
*分類: 障害調査*  ・  難易度: 中級

変更前の確認では 障害調査 の マネージャーログ を主操作として FAIL02 を判定します。変更対象と非対象の境界への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL02 に残します。変更前の確認を補助する エラー記録 では IDENTIFIER を補助値として FAIL02 へ保存します。主判定の変更前の確認では障害調査の マネージャーログ から clstrmgrES を読み FAIL02 へ残します。証跡照合の変更前の確認では障害調査の clstrmgrES と IDENTIFIER を FAIL02 に保存します。記録対応の変更前の確認では障害調査の Event NameとExit Status の証跡へ FAIL02 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 変更前の確認 FAIL02を保守記録に説明する必要があります。資源依存関係 Resource Group Dependency 再始動後の確認と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は再始動確認でイベント順序を証跡に残し・Resource Groupでイベント順序から。
    - B. 運用時に利用する技術的役割は変更確認でマネージャーを証跡に残し・hacmp.out Eventでマネージャーログから。 ✅
    - C. 運用時に利用する技術的役割は切替でRG現在位置を証跡に残し・Online NodeのRG現在位置と取得時刻を記録し。リソースグループ制御 Online Node 0179固有の属性も確認対象に含める。
    - D. 運用時に利用する技術的役割は解除で検証進行率を証跡に残し・SMIT Commandの検証進行率と取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能マネー・cluでBの記述「hacmp.out Eventでマネージャーログから」に対応する項目は変更前の確認 FAIL02（hac・マネー・変更確）です。照合マネー・変更確に関する障害調査の仕様は「hacmp.out Eventでマネージャーログから」で、確認対象はマネー・変更確・cluです。比較障害調・変更確でA:の再始動後の確認 DEP15は「Resource Groupでイベント順序か」を述べるため、正答側の照合軸はhac・変更確・マネーです。項目マネー・変更確でC:のOnline Nodeは「Online NodeのRG現在位置と取得時」を述べるため、正答側の照合軸はclu・障害調・マネーです。仕様マネー・変更確でD:のCommand Statusは「SMIT Commandの検証進行率と取得時」を述べるため、正答側の照合軸は変更確・clu・マネーです。用語マネー・変更確という用語は「hacmp.out Eventでマネージャーログから」を指し、照合する値と誤認リスクの組合せは障害調・マネー・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 変更前の確認 FAIL02**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて変更前の証跡を保存し、FAIL02のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL02のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL02のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL02の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の clstrmgrES が画面・出力に表示されること
    ② ステップ2 の IDENTIFIER が画面・出力に表示されること
    ③ ステップ3 の ACQUISITION が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 変更後の確認 FAIL03 {#c25-i0532}
*分類: 障害調査*  ・  難易度: 中級

変更後の確認では 障害調査 の エラー記録 を主操作として FAIL03 を判定します。反映値と残存値への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL03 に残します。変更後の確認を補助する 主要ログ では ACQUISITION を補助値として FAIL03 へ保存します。主判定の変更後の確認では障害調査の エラー記録 から IDENTIFIER を読み FAIL03 へ残します。証跡照合の変更後の確認では障害調査の IDENTIFIER と ACQUISITION を FAIL03 に保存します。記録対応の変更後の確認では障害調査の Event NameとExit Status の証跡へ FAIL03 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 変更後の確認 FAIL03に関する障害切り分けの前提を確認しています。GLVM地理的ミラー VG STATE 0048の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はミラー再同期条件の誤読を避けるため・照合操作で確認欄を採取するしてAIXエラーを照合する。
    - B. 表示や設定で扱う内容はsyslogとhacmp.outを避けるため・監査操作で記録欄を比較するしてミラー更新状を照合する。
    - C. 表示や設定で扱う内容はcluster historyだを避けるため・エラー記録からIDENTIFIERを読むしてエラー記録を照合する。 ✅
    - D. 表示や設定で扱う内容は監査証跡の誤読を避けるため・監査証跡で監査証跡を確認するして監査証跡を照合する。clmgr sync cluster 状態確認 監査証跡固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能エラー・cluでCの記述「hacmp.out Eventでエラー記録から」に対応する項目は変更後の確認 FAIL03（hac・エラー・変更確）です。照合エラー・変更確に関する障害調査の仕様は「hacmp.out Eventでエラー記録から」で、確認対象はエラー・変更確・cluです。比較障害調・変更確でA:のVG STATEは「地理的ミラーの項目のAIXエラー識別子と取得」を述べるため、正答側の照合軸はhac・変更確・エラーです。運用変更確・hacでB:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸はエラー・障害調・変更確です。仕様エラー・変更確でD:の状態確認 監査証跡は「検証後に構成を同期し、クラスタスナップショッ」を述べるため、正答側の照合軸は変更確・clu・エラーです。用語エラー・変更確という用語は「hacmp.out Eventでエラー記録から」を指し、照合する値と誤認リスクの組合せは障害調・エラー・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 変更後の確認 FAIL03**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて変更結果を検証し、FAIL03のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL03のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL03の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL03のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IDENTIFIER が画面・出力に表示されること
    ② ステップ2 の ACQUISITION が画面・出力に表示されること
    ③ ステップ3 の clstrmgrES が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 引継ぎ記録 FAIL09 {#c25-i0533}
*分類: 障害調査*  ・  難易度: 中級

引継ぎ記録では 障害調査 の エラー記録 を主操作として FAIL09 を判定します。次担当者が追跡できる証跡への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL09 に残します。引継ぎ記録を補助する 主要ログ では ACQUISITION を補助値として FAIL09 へ保存します。主判定の引継ぎ記録では障害調査の エラー記録 から IDENTIFIER を読み FAIL09 へ残します。証跡照合の引継ぎ記録では障害調査の IDENTIFIER と ACQUISITION を FAIL09 に保存します。記録対応の引継ぎ記録では障害調査の Event NameとExit Status の証跡へ FAIL09 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 引継ぎ記録 FAIL09の技術的な意味を資料で確認するとき、clstat・SNMP clinfoES Status Path 引継ぎ記録との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はエラー記録からIDENTIFIERを読むことでエラー記録を確認し・cluster historを防ぐ。 ✅
    - B. 管理対象との関係を表す説明はクラスタ表示からClusterを読むことでクラスタ表示を確認し・SNMP情報の残留を実ノードを防ぐ。clstat・SNMP clinfoES Status Path固有の属性も確認対象に含める。
    - C. 管理対象との関係を表す説明は記録操作で証跡欄を照合することでROHAレポを確認し・未同期構成の見落としを防ぐ。
    - D. 管理対象との関係を表す説明はトポロジー確でページング状を確認することでページング状を確認し・ページング状の誤読を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能エラー・cluでAの記述「hacmp.out Eventでエラー記録から」に対応する項目は引継ぎ記録 FAIL09（hac・エラー・障害調）です。照合エラー・障害調に関する障害調査の仕様は「hacmp.out Eventでエラー記録から」で、確認対象はエラー・障害調・cluです。運用障害調・hacでB:の引継ぎ記録 CLSTAT09は「clstatでクラスタ表示から」を述べるため、正答側の照合軸はエラー・障害調・障害調です。項目エラー・障害調でC:のクラスタ構成検証 clverifは「clverify.logのROHAレポートと」を述べるため、正答側の照合軸はclu・障害調・エラーです。仕様エラー・障害調でD:のトポロジー確認 ページング状態は「Cluster Manager の状態」を述べるため、正答側の照合軸は障害調・clu・エラーです。用語エラー・障害調という用語は「hacmp.out Eventでエラー記録から」を指し、照合する値と誤認リスクの組合せは障害調・エラー・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 引継ぎ記録 FAIL09**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて再現可能な記録を作成し、FAIL09のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL09のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL09の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL09のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IDENTIFIER が画面・出力に表示されること
    ② ステップ2 の ACQUISITION が画面・出力に表示されること
    ③ ステップ3 の clstrmgrES が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 復旧後の確認 FAIL06 {#c25-i0534}
*分類: 障害調査*  ・  難易度: 中級

復旧後の確認では 障害調査 の エラー記録 を主操作として FAIL06 を判定します。再発していないことを示す値への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL06 に残します。復旧後の確認を補助する 主要ログ では ACQUISITION を補助値として FAIL06 へ保存します。主判定の復旧後の確認では障害調査の エラー記録 から IDENTIFIER を読み FAIL06 へ残します。証跡照合の復旧後の確認では障害調査の IDENTIFIER と ACQUISITION を FAIL06 に保存します。記録対応の復旧後の確認では障害調査の Event NameとExit Status の証跡へ FAIL06 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 「障害調査 hacmp.out Event Summary 復旧後の確認 FAIL06」を「clstat・SNMP clinfoES Status Path 通常状態の確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はエラー記録からIDENTIFIERを読むことでエラー記録を確認し・cluster historを防ぐ。 ✅
    - B. 保守作業で参照する機能はclinfoES状態からclinfoESことでclinfoを確認し・SNMP情報の残留を実ノードを防ぐ。
    - C. 保守作業で参照する機能は変更確認操作で採取欄を棚卸することでRPV通信ペを確認し・RPV経路断の見落としを防ぐ。
    - D. 保守作業で参照する機能は主操作で出力欄を評価することでVG varを確認し・片側VGのvaryon誤操作を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能エラー・cluでAの記述「hacmp.out Eventでエラー記録から」に対応する項目は復旧後の確認 FAIL06（hac・エラー・復旧確）です。照合エラー・復旧確に関する障害調査の仕様は「hacmp.out Eventでエラー記録から」で、確認対象はエラー・復旧確・cluです。運用復旧確・hacでB:の通常状態の確認 CLSTAT01は「clstatでclinfoES状態から」を述べるため、正答側の照合軸はエラー・障害調・復旧確です。項目エラー・復旧確でC:のRPV Clientは「地理的ミラーの項目のRPV通信ペアと取得時刻」を述べるため、正答側の照合軸はclu・障害調・エラーです。仕様エラー・復旧確でD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は復旧確・clu・エラーです。用語エラー・復旧確という用語は「hacmp.out Eventでエラー記録から」を指し、照合する値と誤認リスクの組合せは障害調・エラー・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 復旧後の確認 FAIL06**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて復旧後の安定性を確認し、FAIL06のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL06のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL06の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL06のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IDENTIFIER が画面・出力に表示されること
    ② ステップ2 の ACQUISITION が画面・出力に表示されること
    ③ ステップ3 の clstrmgrES が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 復旧準備 FAIL05 {#c25-i0535}
*分類: 障害調査*  ・  難易度: 中級

復旧準備では 障害調査 の マネージャーログ を主操作として FAIL05 を判定します。再開前に必要な整合性への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL05 に残します。復旧準備を補助する エラー記録 では IDENTIFIER を補助値として FAIL05 へ保存します。主判定の復旧準備では障害調査の マネージャーログ から clstrmgrES を読み FAIL05 へ残します。証跡照合の復旧準備では障害調査の clstrmgrES と IDENTIFIER を FAIL05 に保存します。記録対応の復旧準備では障害調査の Event NameとExit Status の証跡へ FAIL05 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 復旧準備 FAIL05を同一分類のクラスタ構成検証 SMIT Command Status 0049と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は復旧で検証進行率を証跡に残し・SMIT Commandの検証進行率と取得時刻を記録し。
    - B. 構成を確認する際の意味は復旧準備でマネージャーを証跡に残し・hacmp.out Eventでマネージャーログから。 ✅
    - C. 構成を確認する際の意味は切替でリソース要約を証跡に残し・Verificationのリソース要約と取得時刻を記録し。
    - D. 構成を確認する際の意味は計画でRPV通信ペを証跡に残し・地理的ミラーの項目のRPV通信ペアと取得時刻を記録し。GLVM地理的ミラー RPV Client 0339固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能マネー・cluでBの記述「hacmp.out Eventでマネージャーログから」に対応する項目は復旧準備 FAIL05（hac・マネー・復旧準）です。照合マネー・復旧準に関する障害調査の仕様は「hacmp.out Eventでマネージャーログから」で、確認対象はマネー・復旧準・cluです。比較障害調・復旧準でA:のCommand Statusは「SMIT Commandの検証進行率と取得時」を述べるため、正答側の照合軸はhac・復旧準・マネーです。項目マネー・復旧準でC:のVerificationは「Verificationのリソース要約と取得」を述べるため、正答側の照合軸はclu・障害調・マネーです。仕様マネー・復旧準でD:のRPV Clientは「地理的ミラーの項目のRPV通信ペアと取得時刻」を述べるため、正答側の照合軸は復旧準・clu・マネーです。用語マネー・復旧準という用語は「hacmp.out Eventでマネージャーログから」を指し、照合する値と誤認リスクの組合せは障害調・マネー・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 復旧準備 FAIL05**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて復旧条件を確認し、FAIL05のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL05のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL05のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL05の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の clstrmgrES が画面・出力に表示されること
    ② ステップ2 の IDENTIFIER が画面・出力に表示されること
    ③ ステップ3 の ACQUISITION が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 性能影響の確認 FAIL11 {#c25-i0536}
*分類: 障害調査*  ・  難易度: 中級

性能影響の確認では 障害調査 の マネージャーログ を主操作として FAIL11 を判定します。処理時間と滞留箇所への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL11 に残します。性能影響の確認を補助する エラー記録 では IDENTIFIER を補助値として FAIL11 へ保存します。主判定の性能影響の確認では障害調査の マネージャーログ から clstrmgrES を読み FAIL11 へ残します。証跡照合の性能影響の確認では障害調査の clstrmgrES と IDENTIFIER を FAIL11 に保存します。記録対応の性能影響の確認では障害調査の Event NameとExit Status の証跡へ FAIL11 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 性能影響の確認 FAIL11に関する障害切り分けの前提を確認しています。GLVM地理的ミラー syslog entry 0042の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては地理的ミラーの項目のsyslog記録と取得時刻を記録し・RPV経路断の見落としを防ぐである。変更確認操作で採取欄を棚卸するときはRPV経路断の見落としを防ぐ。
    - B. 機能の説明としてはhacmp.out Eventでマネージャーログから クラスター管理プロセス を読みである。マネージャーログからクラスター管理プときはcluster historを防ぐ。 ✅
    - C. 機能の説明としては地理的ミラーの項目のRPV通信ペアと取得時刻を記録し・syslogとhacmp.outの突合漏れを防ぐである。監査操作で記録欄を比較するときはsyslogとhacmp.oを防ぐ。
    - D. 機能の説明としてはクラスタサービスを開始し・リソースグループをオンライン化する操作を版数確認する。復旧手掛かりで復旧手掛かりを確認するときは復旧手掛かりの誤読を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能マネー・cluでBの記述「hacmp.out Eventでマネージャーログから」に対応する項目は性能影響の確認 FAIL11（hac・マネー・性能影）です。照合マネー・性能影に関する障害調査の仕様は「hacmp.out Eventでマネージャーログから」で、確認対象はマネー・性能影・cluです。比較障害調・性能影でA:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸はhac・性能影・マネーです。項目マネー・性能影でC:のRPV Clientは「地理的ミラーの項目のRPV通信ペアと取得時刻」を述べるため、正答側の照合軸はclu・障害調・マネーです。仕様マネー・性能影でD:の版数確認 復旧手掛かりは「クラスタサービスを開始し、リソースグループを」を述べるため、正答側の照合軸は性能影・clu・マネーです。用語マネー・性能影という用語は「hacmp.out Eventでマネージャーログから」を指し、照合する値と誤認リスクの組合せは障害調・マネー・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 性能影響の確認 FAIL11**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて負荷と待ちを確認し、FAIL11のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL11のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL11のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL11の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の clstrmgrES が画面・出力に表示されること
    ② ステップ2 の IDENTIFIER が画面・出力に表示されること
    ③ ステップ3 の ACQUISITION が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 構成監査 FAIL08 {#c25-i0537}
*分類: 障害調査*  ・  難易度: 中級

構成監査では 障害調査 の マネージャーログ を主操作として FAIL08 を判定します。定義値と稼働値の一致への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL08 に残します。構成監査を補助する エラー記録 では IDENTIFIER を補助値として FAIL08 へ保存します。主判定の構成監査では障害調査の マネージャーログ から clstrmgrES を読み FAIL08 へ残します。証跡照合の構成監査では障害調査の clstrmgrES と IDENTIFIER を FAIL08 に保存します。記録対応の構成監査では障害調査の Event NameとExit Status の証跡へ FAIL08 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 構成監査 FAIL08について構成や状態を確認します。clstat・SNMP clinfoES Status Path 代替経路の確認ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはclinfoES状態からclinfoESことでclinfoを確認し・SNMP情報の残留を実ノードを防ぐ。
    - B. 状態を読み取るための働きは採取操作で照合欄を点検することでトポロジ要約を確認し・警告と致命エラーの混同を防ぐ。
    - C. 状態を読み取るための働きは運用記録で運用記録を確認することで運用記録を確認し・運用記録の誤読を防ぐ。
    - D. 状態を読み取るための働きはマネージャーログからクラスター管理プロセことでマネージャーを確認し・cluster historを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能マネー・cluでDの記述「hacmp.out Eventでマネージャーログから」に対応する項目は構成監査 FAIL08（hac・マネー・構成監）です。照合マネー・構成監に関する障害調査の仕様は「hacmp.out Eventでマネージャーログから」で、確認対象はマネー・構成監・cluです。比較障害調・構成監でA:の代替経路の確認 CLSTAT10は「clstatでclinfoES状態から」を述べるため、正答側の照合軸はhac・構成監・マネーです。運用構成監・hacでB:のCluster Resourceは「Cluster Resourcesのトポロジ」を述べるため、正答側の照合軸はマネー・障害調・構成監です。項目マネー・構成監でC:の障害切り分け 運用記録は「ノードの状態と raw_state」を述べるため、正答側の照合軸はclu・障害調・マネーです。用語マネー・構成監という用語は「hacmp.out Eventでマネージャーログから」を指し、照合する値と誤認リスクの組合せは障害調・マネー・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 構成監査 FAIL08**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて構成差分を監査し、FAIL08のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL08のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL08のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL08の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の clstrmgrES が画面・出力に表示されること
    ② ステップ2 の IDENTIFIER が画面・出力に表示されること
    ③ ステップ3 の ACQUISITION が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 権限境界の確認 FAIL12 {#c25-i0538}
*分類: 障害調査*  ・  難易度: 中級

権限境界の確認では 障害調査 の エラー記録 を主操作として FAIL12 を判定します。参照操作と変更操作の分離への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL12 に残します。権限境界の確認を補助する 主要ログ では ACQUISITION を補助値として FAIL12 へ保存します。主判定の権限境界の確認では障害調査の エラー記録 から IDENTIFIER を読み FAIL12 へ残します。証跡照合の権限境界の確認では障害調査の IDENTIFIER と ACQUISITION を FAIL12 に保存します。記録対応の権限境界の確認では障害調査の Event NameとExit Status の証跡へ FAIL12 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 権限境界の確認 FAIL12の設定や表示を読む前に役割を確認します。資源依存関係 Resource Group Dependency 構成監査ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは依存順を無視して子資源を先にオンを避けるため・RG一覧からdatabase_rgを読むしてRG一覧を照合する。
    - B. 対象資源に対する働きは片側VGのvaryon誤操作を避けるため・主操作で出力欄を評価するしてVG varを照合する。
    - C. 対象資源に対する働きはcluster historyだを避けるため・エラー記録からIDENTIFIERを読むしてエラー記録を照合する。 ✅
    - D. 対象資源に対する働きは警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するしてトポロジ要約を照合する。クラスタ構成検証 Cluster Resources 0355固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能エラー・cluでCの記述「hacmp.out Eventでエラー記録から」に対応する項目は権限境界の確認 FAIL12（hac・エラー・権限境）です。照合エラー・権限境に関する障害調査の仕様は「hacmp.out Eventでエラー記録から」で、確認対象はエラー・権限境・cluです。比較障害調・権限境でA:の構成監査 DEP08は「Resource GroupでRG一覧から」を述べるため、正答側の照合軸はhac・権限境・エラーです。運用権限境・hacでB:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸はエラー・障害調・権限境です。仕様エラー・権限境でD:のCluster Resourceは「Cluster Resourcesのトポロジ」を述べるため、正答側の照合軸は権限境・clu・エラーです。用語エラー・権限境という用語は「hacmp.out Eventでエラー記録から」を指し、照合する値と誤認リスクの組合せは障害調・エラー・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 権限境界の確認 FAIL12**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて実行権限を点検し、FAIL12のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL12のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL12の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL12のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の IDENTIFIER が画面・出力に表示されること
    ② ステップ2 の ACQUISITION が画面・出力に表示されること
    ③ ステップ3 の clstrmgrES が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 通常状態の確認 FAIL01 {#c25-i0539}
*分類: 障害調査*  ・  難易度: 中級

通常状態の確認では 障害調査 の 主要ログ を主操作として FAIL01 を判定します。基準値と現在値の差への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL01 に残します。通常状態の確認を補助する マネージャーログ では clstrmgrES を補助値として FAIL01 へ保存します。主判定の通常状態の確認では障害調査の 主要ログ から ACQUISITION を読み FAIL01 へ残します。証跡照合の通常状態の確認では障害調査の ACQUISITION と clstrmgrES を FAIL01 に保存します。記録対応の通常状態の確認では障害調査の Event NameとExit Status の証跡へ FAIL01 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 通常状態の確認 FAIL01の技術的な意味を資料で確認するとき、clstat・SNMP clinfoES Status Path 代替経路の確認との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は代替経路確認でclinfoを証跡に残し・clstatでclinfoES状態から clinfoES。
    - B. コマンドまたは機能の用途は通常状態確認で主要ログを証跡に残し・hacmp.out Eventで主要ログから。 ✅
    - C. コマンドまたは機能の用途は収集でRPV通信ペを証跡に残し・地理的ミラーの項目のRPV通信ペアと取得時刻を記録し。
    - D. コマンドまたは機能の用途はサービスIPでパス状態を証跡に残し・クラスタトポロジー・ネットワーク・サービスIP。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能主要ロ・cluでBの記述「hacmp.out Eventで主要ログから」に対応する項目は通常状態の確認 FAIL01（hac・主要ロ・通常状）です。照合主要ロ・通常状に関する障害調査の仕様は「hacmp.out Eventで主要ログから」で、確認対象は主要ロ・通常状・cluです。比較障害調・通常状でA:の代替経路の確認 CLSTAT10は「clstatでclinfoES状態から」を述べるため、正答側の照合軸はhac・通常状・主要ロです。項目主要ロ・通常状でC:のRPV Clientは「地理的ミラーの項目のRPV通信ペアと取得時刻」を述べるため、正答側の照合軸はclu・障害調・主要ロです。仕様主要ロ・通常状でD:の障害切り分け パス状態は「クラスタトポロジー、ネットワーク」を述べるため、正答側の照合軸は通常状・clu・主要ロです。用語主要ロ・通常状という用語は「hacmp.out Eventで主要ログから」を指し、照合する値と誤認リスクの組合せは障害調・主要ロ・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 通常状態の確認 FAIL01**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて通常状態を確定し、FAIL01のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL01の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL01のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL01のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ACQUISITION が画面・出力に表示されること
    ② ステップ2 の clstrmgrES が画面・出力に表示されること
    ③ ステップ3 の IDENTIFIER が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 障害調査 hacmp.out Event Summary 障害切り分け FAIL04 {#c25-i0540}
*分類: 障害調査*  ・  難易度: 中級

障害切り分けでは 障害調査 の 主要ログ を主操作として FAIL04 を判定します。最初に失敗した処理への注意として「cluster historyだけを見て並列RG処理の詳細を失う危険があります」を FAIL04 に残します。障害切り分けを補助する マネージャーログ では clstrmgrES を補助値として FAIL04 へ保存します。主判定の障害切り分けでは障害調査の 主要ログ から ACQUISITION を読み FAIL04 へ残します。証跡照合の障害切り分けでは障害調査の ACQUISITION と clstrmgrES を FAIL04 に保存します。記録対応の障害切り分けでは障害調査の Event NameとExit Status の証跡へ FAIL04 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 障害調査 hacmp.out Event Summary 障害切り分け FAIL04の設定や表示を読む前に役割を確認します。障害調査 hacmp.out Event Summary 依存関係の確認ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は障害調査で主要ログを証跡に残し・hacmp.out Eventで主要ログから。 ✅
    - B. 一次資料が示す主目的は依存関係確認で主要ログを証跡に残し・hacmp.out Eventで主要ログから。
    - C. 一次資料が示す主目的は診断で検証進行率を証跡に残し・SMIT Commandの検証進行率と取得時刻を記録し。
    - D. 一次資料が示す主目的は確認範囲で確認範囲を証跡に残し・クラスタトポロジー・ネットワーク・サービスIP。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能主要ロ・cluでAの記述「hacmp.out Eventで主要ログから」に対応する項目は障害切り分け FAIL04（hac・主要ロ・障害調）です。照合主要ロ・障害調に関する障害調査の仕様は「hacmp.out Eventで主要ログから」で、確認対象は主要ロ・障害調・cluです。運用障害調・hacでB:の依存関係の確認 FAIL13は「hacmp.out Eventで主要ログから」を述べるため、正答側の照合軸は主要ロ・障害調・障害調です。項目主要ロ・障害調でC:のCommand Statusは「SMIT Commandの検証進行率と取得時」を述べるため、正答側の照合軸はclu・障害調・主要ロです。仕様主要ロ・障害調でD:の整合確認 確認範囲は「クラスタトポロジー、ネットワーク」を述べるため、正答側の照合軸は障害調・clu・主要ロです。用語主要ロ・障害調という用語は「hacmp.out Eventで主要ログから」を指し、照合する値と誤認リスクの組合せは障害調・主要ロ・cluです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **障害調査 hacmp.out Event Summary 障害切り分け FAIL04**

    - 検証目的: 障害調査のhacmp.out Event Summaryについて障害範囲を限定し、FAIL04のEvent NameとExit Statusを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象FAIL04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へgrep -i "rg_move|acquisition" /var/hacmp/log/hacmp.outを指定し、FAIL04の主要ログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> grep -i "rg_move|acquisition" /var/hacmp/log/hacmp.out
    → Enter を押す
    ```

    画面・出力:
    ```text
    EVENT rg_move app_rg FROM node1 TO node2 ACQUISITION SUCCESS
    ```

    画面・出力にあるACQUISITIONを読み、Event NameとExit Statusと対象FAIL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へtail -80 /var/hacmp/log/clstrmgr.debugを指定し、FAIL04のマネージャーログを表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> tail -80 /var/hacmp/log/clstrmgr.debug
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgrES app_rg state changed OFFLINE to ONLINE on node2
    ```

    画面・出力にあるclstrmgrESを読み、Event NameとExit Statusと対象FAIL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の障害調査を確認する入力画面です。COMMAND入力口へerrpt -aを指定し、FAIL04のエラー記録を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> errpt -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: HA_RESOURCE_MOVE
    IDENTIFIER: A6DF45AA
    Resource Group: app_rg
    Node: node2
    ```

    画面・出力にあるIDENTIFIERを読み、Event NameとExit Statusと対象FAIL04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の ACQUISITION が画面・出力に表示されること
    ② ステップ2 の clstrmgrES が画面・出力に表示されること
    ③ ステップ3 の IDENTIFIER が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


