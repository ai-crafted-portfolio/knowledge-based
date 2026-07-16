---
search:
  exclude: true
---

# PowerHA SystemMirror 7.2 — 詳細 (5/6)

[← PowerHA SystemMirror 7.2 の概要へ戻る](index.md)


## PowerHA SystemMirror 7.2 > 同期処理

### 同期処理 Cluster Synchronization 構成監査 SYNC08 {#c25-i0380}
*分類: 同期処理*  ・  難易度: 中級

構成監査では 同期処理 の 同期実行 を主操作として SYNC08 を判定します。定義値と稼働値の一致への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC08 に残します。構成監査を補助する 再確認 では false を補助値として SYNC08 へ保存します。主判定の構成監査では同期処理の 同期実行 から clsnapshot を読み SYNC08 へ残します。証跡照合の構成監査では同期処理の clsnapshot と false を SYNC08 に保存します。記録対応の構成監査では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC08 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 構成監査 SYNC08の技術的な意味を資料で確認するとき、clstat・SNMP clinfoES Status Path 復旧準備との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はSNMP情報の残留を実ノード状態を避けるため・SMUX接続からESTABLISHEDをしてSMUX接続を照合する。
    - B. 構成を確認する際の意味は獲得失敗ログの未採取を避けるため・表示操作で対象欄を追跡するして優先ノード一を照合する。
    - C. 構成を確認する際の意味はノード間ODM差分の残存を避けるため・確認操作で状態欄を整理するしてODM登録値を照合する。
    - D. 構成を確認する際の意味は同期元を誤ると古い定義を全ノードを避けるため・同期実行からclsnapshotを読むして同期実行を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能同期実・同期元でDの記述「Cluster Synchronizで同期実行から」に対応する項目は構成監査 SYNC08（Clu・同期実・構成監）です。照合同期実・構成監に関する同期処理の仕様は「Cluster Synchronizで同期実行から」で、確認対象は同期実・構成監・同期元です。比較同期処・構成監でA:の復旧準備 CLSTAT05は「clstatでSMUX接続から」を述べるため、正答側の照合軸はClu・構成監・同期実です。運用構成監・CluでB:のGroup Nameは「Resource Groupの優先ノード一覧」を述べるため、正答側の照合軸は同期実・同期処・構成監です。項目同期実・構成監でC:のCluster Topologyは「Cluster TopologyのODM登録」を述べるため、正答側の照合軸は同期元・同期処・同期実です。用語同期実・構成監という用語は「Cluster Synchronizで同期実行から」を指し、照合する値と誤認リスクの組合せは同期処・同期実・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 構成監査 SYNC08**

    - 検証目的: 同期処理のCluster Synchronizationについて構成差分を監査し、SYNC08のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC08と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC08の同期実行を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr sync cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Committing any changes, as required, to all available nodes...
    Verification has completed normally.
    clsnapshot: Succeeded creating Cluster Snapshot: clver_pass_snapshot.
    ```

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC08の再確認を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr -a UNSYNCED_CHANGES query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    UNSYNCED_CHANGES="false"
    ```

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC08の未同期確認を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr -a UNSYNCED_CHANGES query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    UNSYNCED_CHANGES="true"
    ```

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の clsnapshot が画面・出力に表示されること
    ② ステップ2 の false が画面・出力に表示されること
    ③ ステップ3 の UNSYNCED が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 権限境界の確認 SYNC12 {#c25-i0381}
*分類: 同期処理*  ・  難易度: 中級

権限境界の確認では 同期処理 の 再確認 を主操作として SYNC12 を判定します。参照操作と変更操作の分離への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC12 に残します。権限境界の確認を補助する 未同期確認 では UNSYNCED_CHANGES を補助値として SYNC12 へ保存します。主判定の権限境界の確認では同期処理の 再確認 から false を読み SYNC12 へ残します。証跡照合の権限境界の確認では同期処理の false と UNSYNCED_CHANGES を SYNC12 に保存します。記録対応の権限境界の確認では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC12 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 権限境界の確認 SYNC12を同一分類のGLVM地理的ミラー RPV Server 0036と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はミラー再同期条件の誤読を避けるため・照合操作で確認欄を採取するしてミラー更新状を照合する。GLVM地理的ミラー RPV Server 0036固有の属性も確認対象に含める。
    - B. 管理対象との関係を表す説明は同期元を誤ると古い定義を全ノードを避けるため・再確認からfalseを読むして再確認を照合する。 ✅
    - C. 管理対象との関係を表す説明は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして失敗ラベルを照合する。
    - D. 管理対象との関係を表す説明は変更証跡の誤読を避けるため・変更証跡で変更証跡を確認するして変更証跡を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能再確認・同期元でBの記述「Cluster Synchronizで再確認から」に対応する項目は権限境界の確認 SYNC12（Clu・再確認・権限境）です。照合再確認・権限境に関する同期処理の仕様は「Cluster Synchronizで再確認から false」で、確認対象は再確認・権限境・同期元です。比較同期処・権限境でA:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸はClu・権限境・再確認です。項目再確認・権限境でC:のEvent Summaryは「Event Summaryの失敗ラベルと取得」を述べるため、正答側の照合軸は同期元・同期処・再確認です。仕様再確認・権限境でD:の所有先確認 変更証跡は「クラスタ構成と状態をスナップショットとして表」を述べるため、正答側の照合軸は権限境・同期元・再確認です。用語再確認・権限境という用語は「Cluster Synchronizで再確認から」を指し、照合する値と誤認リスクの組合せは同期処・再確認・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 権限境界の確認 SYNC12**

    - 検証目的: 同期処理のCluster Synchronizationについて実行権限を点検し、SYNC12のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC12と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC12の再確認を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr -a UNSYNCED_CHANGES query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    UNSYNCED_CHANGES="false"
    ```

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC12の未同期確認を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr -a UNSYNCED_CHANGES query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    UNSYNCED_CHANGES="true"
    ```

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC12の同期実行を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr sync cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Committing any changes, as required, to all available nodes...
    Verification has completed normally.
    clsnapshot: Succeeded creating Cluster Snapshot: clver_pass_snapshot.
    ```

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC12の対応を確認します。参照操作と変更操作の分離を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の false が画面・出力に表示されること
    ② ステップ2 の UNSYNCED が画面・出力に表示されること
    ③ ステップ3 の clsnapshot が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 通常状態の確認 SYNC01 {#c25-i0382}
*分類: 同期処理*  ・  難易度: 中級

通常状態の確認では 同期処理 の 未同期確認 を主操作として SYNC01 を判定します。基準値と現在値の差への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC01 に残します。通常状態の確認を補助する 同期実行 では clsnapshot を補助値として SYNC01 へ保存します。主判定の通常状態の確認では同期処理の 未同期確認 から UNSYNCED_CHANGES を読み SYNC01 へ残します。証跡照合の通常状態の確認では同期処理の UNSYNCED_CHANGES と clsnapshot を SYNC01 に保存します。記録対応の通常状態の確認では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC01 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 通常状態の確認 SYNC01を保守記録に説明する必要があります。clstat・SNMP clinfoES Status Path 停止前の確認と取り違えない説明はどれですか。

    - A. 仕様上の役割は停止確認でSMUX接続を証跡に残し・clstatでSMUX接続から ESTABLISHED。
    - B. 仕様上の役割は収集でリソース要約を証跡に残し・Verificationのリソース要約と取得時刻を記録し。
    - C. 仕様上の役割は通常状態確認で未同期確認を証跡に残し・Cluster Synchronizで未同期確認から。 ✅
    - D. 仕様上の役割は計画で優先ノード一を証跡に残し・Resource Groupの優先ノード一覧と取得時刻を記録。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能未同期・同期元でCの記述「Cluster Synchronizで未同期確認から」に対応する項目は通常状態の確認 SYNC01（Clu・未同期・通常状）です。照合未同期・通常状に関する同期処理の仕様は「Cluster Synchronizで未同期確認から」で、確認対象は未同期・通常状・同期元です。比較同期処・通常状でA:の停止前の確認 CLSTAT14は「clstatでSMUX接続から」を述べるため、正答側の照合軸はClu・通常状・未同期です。運用通常状・CluでB:のVerificationは「Verificationのリソース要約と取得」を述べるため、正答側の照合軸は未同期・同期処・通常状です。仕様未同期・通常状でD:のGroup Nameは「Resource Groupの優先ノード一覧」を述べるため、正答側の照合軸は通常状・同期元・未同期です。用語未同期・通常状という用語は「Cluster Synchronizで未同期確認から」を指し、照合する値と誤認リスクの組合せは同期処・未同期・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 通常状態の確認 SYNC01**

    - 検証目的: 同期処理のCluster Synchronizationについて通常状態を確定し、SYNC01のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC01と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC01の未同期確認を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr -a UNSYNCED_CHANGES query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    UNSYNCED_CHANGES="true"
    ```

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC01の同期実行を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr sync cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Committing any changes, as required, to all available nodes...
    Verification has completed normally.
    clsnapshot: Succeeded creating Cluster Snapshot: clver_pass_snapshot.
    ```

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC01の再確認を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr -a UNSYNCED_CHANGES query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    UNSYNCED_CHANGES="false"
    ```

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の UNSYNCED が画面・出力に表示されること
    ② ステップ2 の clsnapshot が画面・出力に表示されること
    ③ ステップ3 の false が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 障害切り分け SYNC04 {#c25-i0383}
*分類: 同期処理*  ・  難易度: 中級

障害切り分けでは 同期処理 の 未同期確認 を主操作として SYNC04 を判定します。最初に失敗した処理への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC04 に残します。障害切り分けを補助する 同期実行 では clsnapshot を補助値として SYNC04 へ保存します。主判定の障害切り分けでは同期処理の 未同期確認 から UNSYNCED_CHANGES を読み SYNC04 へ残します。証跡照合の障害切り分けでは同期処理の UNSYNCED_CHANGES と clsnapshot を SYNC04 に保存します。記録対応の障害切り分けでは同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC04 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 障害切り分け SYNC04を同一分類のGLVM地理的ミラー RPV Server 0021と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は地理的ミラーの項目のミラー更新状態と取得時刻を記録し・片側VGのvaryon誤操作を防ぐである。主操作で出力欄を評価するときは片側VGのvaryon誤操作を防ぐ。
    - B. コマンドまたは機能の用途は地理的ミラーの項目のAIXエラー識別子と取得時刻を記録し・片側VGのvaryon誤操作を防ぐである。主操作で出力欄を評価するときは片側VGのvaryon誤操作を防ぐ。GLVM地理的ミラー VG STATE 0153固有の属性も確認対象に含める。
    - C. コマンドまたは機能の用途はCluster Synchronizで未同期確認から UNSYNCED_CHANGES を読みである。未同期確認からUNSYNCED_CHときは同期元を誤ると古い定義を全ノを防ぐ。 ✅
    - D. コマンドまたは機能の用途はクラスタサービスを開始し・リソースグループをオンライン化する操作を同期確認する。同期確認でファイルセッを確認するときはファイルセッの誤読を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能未同期・同期元でCの記述「Cluster Synchronizで未同期確認から」に対応する項目は障害切り分け SYNC04（Clu・未同期・同期処）です。照合未同期・同期処に関する同期処理の仕様は「Cluster Synchronizで未同期確認から」で、確認対象は未同期・同期処・同期元です。比較同期処・同期処でA:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸はClu・同期処・未同期です。運用同期処・CluでB:のVG STATEは「地理的ミラーの項目のAIXエラー識別子と取得」を述べるため、正答側の照合軸は未同期・同期処・同期処です。仕様未同期・同期処でD:の同期確認 ファイルセットは「クラスタサービスを開始し、リソースグループを」を述べるため、正答側の照合軸は同期処・同期元・未同期です。用語未同期・同期処という用語は「Cluster Synchronizで未同期確認から」を指し、照合する値と誤認リスクの組合せは同期処・未同期・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 障害切り分け SYNC04**

    - 検証目的: 同期処理のCluster Synchronizationについて障害範囲を限定し、SYNC04のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC04と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC04の未同期確認を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr -a UNSYNCED_CHANGES query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    UNSYNCED_CHANGES="true"
    ```

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC04の同期実行を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr sync cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    Committing any changes, as required, to all available nodes...
    Verification has completed normally.
    clsnapshot: Succeeded creating Cluster Snapshot: clver_pass_snapshot.
    ```

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC04の再確認を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr -a UNSYNCED_CHANGES query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    UNSYNCED_CHANGES="false"
    ```

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の UNSYNCED が画面・出力に表示されること
    ② ステップ2 の clsnapshot が画面・出力に表示されること
    ③ ステップ3 の false が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278




## PowerHA SystemMirror 7.2 > 構成検証

### クラスタ構成検証 Cluster Resources 0010 {#c25-i0384}
*分類: 構成検証*  ・  難易度: 初級

紺K巡回0011ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紺K巡回0011です。紺K巡回0011はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紺K巡回0011です。紺K巡回0011ではトポロジ要約と取得時刻を採取票紺K巡回0011へ残します。紺K巡回0011ではノード間ODM差分の残存を避けるため補助資料も照合する判断紺K巡回0011です。紺K巡回0011の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紺K巡回0011です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0010の役割を調べています。リソースグループ制御 Online Node 0059の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は復旧で資源グループを証跡に残し・オンラインノードの資源グループRG現在位置と取得時刻を記録し。
    - B. 障害切り分けに用いる役割は登録で失敗ラベルを証跡に残し・イベント要約の失敗ラベルと取得時刻を記録し。
    - C. 障害切り分けに用いる役割は変更証跡で変更証跡を証跡に残し・クラスタ構成と状態をスナップショットとして表示するコマンドを。
    - D. 障害切り分けに用いる役割は巡回でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能巡回・クラス・トポロでDの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・巡回）です。照合巡回・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・巡回・ノードです。比較クラス・巡回でA:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸はクラス・巡回・トポロです。運用巡回・クラスでB:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸はトポロ・クラス・巡回です。項目巡回・クラス・トポロでC:の所有先確認 変更証跡は「クラスタ構成と状態をスナップショットとして表」を述べるため、正答側の照合軸はノード・クラス・トポロです。用語巡回・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0010**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0010について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0010A
    ```

    画面・出力には PHA72DD0010A が表示され、クラスタ構成検証 Cluster Resources 0010 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0010
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0010B
    ```

    画面・出力には PHA72DD0010B が表示され、クラスタ構成検証 Cluster Resources 0010 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0010
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0010C
    ```

    画面・出力には PHA72DD0010C が表示され、クラスタ構成検証 Cluster Resources 0010 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0010A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0010B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0010C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0025 {#c25-i0385}
*分類: 構成検証*  ・  難易度: 中級

銀F棚卸0026ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票銀F棚卸0026です。銀F棚卸0026はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録銀F棚卸0026です。銀F棚卸0026ではトポロジ要約と取得時刻を採取票銀F棚卸0026へ残します。銀F棚卸0026では未同期構成の見落としを避けるため補助資料も照合する判断銀F棚卸0026です。銀F棚卸0026の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録銀F棚卸0026です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 Cluster Resources 0025」を「リソースグループ制御 Online Node 0104」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして資源グループを照合する。
    - B. 仕様上の役割は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するしてリソース要約を照合する。
    - C. 仕様上の役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するしてトポロジ要約を照合する。 ✅
    - D. 仕様上の役割は基本ソフト稼働とクラスタ稼働の混を避けるため・ノード一覧から実状態値を読むしてノード一覧を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能棚卸・クラス・トポロでCの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・棚卸）です。照合棚卸・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・棚卸・未同期です。比較クラス・棚卸でA:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸はクラス・棚卸・トポロです。運用棚卸・クラスでB:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸はトポロ・クラス・棚卸です。仕様棚卸・クラス・トポロでD:のログとの照合 NODE07は「PowerHA Node Stateでノード」を述べるため、正答側の照合軸は棚卸・未同期・トポロです。用語棚卸・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0025**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0025について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0025A
    ```

    画面・出力には PHA72DD0025A が表示され、クラスタ構成検証 Cluster Resources 0025 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0025
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0025B
    ```

    画面・出力には PHA72DD0025B が表示され、クラスタ構成検証 Cluster Resources 0025 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0025
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0025C
    ```

    画面・出力には PHA72DD0025C が表示され、クラスタ構成検証 Cluster Resources 0025 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0025A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0025B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0025C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0040 {#c25-i0386}
*分類: 構成検証*  ・  難易度: 中級

蒼A復旧0041ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票蒼A復旧0041です。蒼A復旧0041はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録蒼A復旧0041です。蒼A復旧0041ではトポロジ要約と取得時刻を採取票蒼A復旧0041へ残します。蒼A復旧0041では検証ログの採取漏れを避けるため補助資料も照合する判断蒼A復旧0041です。蒼A復旧0041の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録蒼A復旧0041です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0040を同一分類のGLVM地理的ミラー syslog entry 0042と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は復旧でsyslogを証跡に残し・地理的ミラーの項目のsyslog記録と取得時刻を記録し。
    - B. コマンドまたは機能の用途は保護で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。
    - C. コマンドまたは機能の用途は復旧でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。 ✅
    - D. コマンドまたは機能の用途は退避確認で退避確認を証跡に残し・Cluster Manager の状態・クラスタ版数。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能復旧・クラス・トポロでCの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・復旧）です。照合復旧・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・復旧・検証ロです。比較クラス・復旧でA:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸はクラス・復旧・トポロです。運用復旧・クラスでB:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸はトポロ・クラス・復旧です。仕様復旧・クラス・トポロでD:の障害切り分け 退避確認は「Cluster Manager の状態」を述べるため、正答側の照合軸は復旧・検証ロ・トポロです。用語復旧・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0040**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0040について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0040A
    ```

    画面・出力には PHA72DD0040A が表示され、クラスタ構成検証 Cluster Resources 0040 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0040
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0040B
    ```

    画面・出力には PHA72DD0040B が表示され、クラスタ構成検証 Cluster Resources 0040 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0040
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0040C
    ```

    画面・出力には PHA72DD0040C が表示され、クラスタ構成検証 Cluster Resources 0040 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0040A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0040B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0040C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0055 {#c25-i0387}
*分類: 構成検証*  ・  難易度: 中級

金P復旧0056ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票金P復旧0056です。金P復旧0056はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録金P復旧0056です。金P復旧0056ではトポロジ要約と取得時刻を採取票金P復旧0056へ残します。金P復旧0056では警告と致命エラーの混同を避けるため補助資料も照合する判断金P復旧0056です。金P復旧0056の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録金P復旧0056です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0055の設定や表示を読む前に役割を確認します。クラスタ構成検証 clverify.log 0142ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するしてトポロジ要約を照合する。 ✅
    - B. 一次資料が示す主目的はノード間構成データODM差分の残を避けるため・確認操作で状態欄を整理するして検証報告ROを照合する。
    - C. 一次資料が示す主目的は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして失敗ラベルを照合する。
    - D. 一次資料が示す主目的は永続アドレスとサービスアドレスのを避けるため・IP資源照会からアドレスを読むしてサービスアドを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能復旧・クラス・トポロでAの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・復旧）です。照合復旧・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・復旧・警告とです。運用復旧・クラスでB:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸はトポロ・クラス・復旧です。項目復旧・クラス・トポロでC:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は警告と・クラス・トポロです。仕様復旧・クラス・トポロでD:の障害切り分け SVCIP04は「IP Service IPでサービスアドレス」を述べるため、正答側の照合軸は復旧・警告と・トポロです。用語復旧・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0055**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0055について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0055A
    ```

    画面・出力には PHA72DD0055A が表示され、クラスタ構成検証 Cluster Resources 0055 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0055
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0055B
    ```

    画面・出力には PHA72DD0055B が表示され、クラスタ構成検証 Cluster Resources 0055 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0055
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0055C
    ```

    画面・出力には PHA72DD0055C が表示され、クラスタ構成検証 Cluster Resources 0055 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0055A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0055B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0055C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0070 {#c25-i0388}
*分類: 構成検証*  ・  難易度: 中級

紺K監査0071ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紺K監査0071です。紺K監査0071はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紺K監査0071です。紺K監査0071ではトポロジ要約と取得時刻を採取票紺K監査0071へ残します。紺K監査0071ではノード間ODM差分の残存を避けるため補助資料も照合する判断紺K監査0071です。紺K監査0071の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紺K監査0071です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0070に関する障害切り分けの前提を確認しています。リソースグループ制御 Node List 0092の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は確認操作で状態欄を整理することでトポロジ要約を確認し・ノード間構成データODM差分を防ぐ。 ✅
    - B. 障害切り分けに用いる役割は調査操作で保守欄を引き継ぎすることで移動履歴を確認し・自動戻し条件の誤読を防ぐ。
    - C. 障害切り分けに用いる役割は復旧操作で点検欄を確認することで獲得イベントを確認し・資源グループ位置の誤認を防ぐ。リソースグループ制御 Acquisition Failure 0281固有の属性も確認対象に含める。
    - D. 障害切り分けに用いる役割は開始から終了状態を読むことで開始を確認し・管理設定と資源状態の混同を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能監査・クラス・トポロでAの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・監査）です。照合監査・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・監査・ノードです。運用監査・クラスでB:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸はトポロ・クラス・監査です。項目監査・クラス・トポロでC:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸はノード・クラス・トポロです。仕様監査・クラス・トポロでD:の依存関係の確認 START13は「Cluster Servicesで開始から」を述べるため、正答側の照合軸は監査・ノード・トポロです。用語監査・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0070**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0070について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0070A
    ```

    画面・出力には PHA72DD0070A が表示され、クラスタ構成検証 Cluster Resources 0070 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0070
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0070B
    ```

    画面・出力には PHA72DD0070B が表示され、クラスタ構成検証 Cluster Resources 0070 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0070
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0070C
    ```

    画面・出力には PHA72DD0070C が表示され、クラスタ構成検証 Cluster Resources 0070 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0070A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0070B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0070C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0085 {#c25-i0389}
*分類: 構成検証*  ・  難易度: 中級

銀F変更0086ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票銀F変更0086です。銀F変更0086はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録銀F変更0086です。銀F変更0086ではトポロジ要約と取得時刻を採取票銀F変更0086へ残します。銀F変更0086では未同期構成の見落としを避けるため補助資料も照合する判断銀F変更0086です。銀F変更0086の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録銀F変更0086です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0085を保守記録に説明する必要があります。クラスタ構成検証 clverify.log 0112と取り違えない説明はどれですか。

    - A. 仕様上の役割は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するして検証報告ROを照合する。
    - B. 仕様上の役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして検証進行率を照合する。
    - C. 仕様上の役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するしてトポロジ要約を照合する。 ✅
    - D. 仕様上の役割は監視通信SNMP情報の残留を実ノを避けるため・clinfoES状態からclinfoESしてclinfoを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能変更・クラス・トポロでCの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・変更）です。照合変更・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・変更・未同期です。比較クラス・変更でA:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸はクラス・変更・トポロです。運用変更・クラスでB:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はトポロ・クラス・変更です。仕様変更・クラス・トポロでD:の代替経路の確認 CLSTAT10は「clstatでclinfoES状態から」を述べるため、正答側の照合軸は変更・未同期・トポロです。用語変更・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0085**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0085について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0085A
    ```

    画面・出力には PHA72DD0085A が表示され、クラスタ構成検証 Cluster Resources 0085 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0085
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0085B
    ```

    画面・出力には PHA72DD0085B が表示され、クラスタ構成検証 Cluster Resources 0085 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0085
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0085C
    ```

    画面・出力には PHA72DD0085C が表示され、クラスタ構成検証 Cluster Resources 0085 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0085A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0085B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0085C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0100 {#c25-i0390}
*分類: 構成検証*  ・  難易度: 上級

蒼A移行0101ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票蒼A移行0101です。蒼A移行0101はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録蒼A移行0101です。蒼A移行0101ではトポロジ要約と取得時刻を採取票蒼A移行0101へ残します。蒼A移行0101では検証ログの採取漏れを避けるため補助資料も照合する判断蒼A移行0101です。蒼A移行0101の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録蒼A移行0101です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0100の技術的な意味を資料で確認するとき、クラスタ構成検証 Verification Progress 0181との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は移行でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。 ✅
    - B. コマンドまたは機能の用途は収集でリソース要約を証跡に残し・構成検証のリソース要約と取得時刻を記録し。
    - C. コマンドまたは機能の用途は構成照合で構成照合を証跡に残し・ノードの状態と raw_state を確認するコマンドを所有。
    - D. コマンドまたは機能の用途は巡回でVG varを証跡に残し・地理的ミラーの項目のVG vary状態と取得時刻を記録し。

    正解: **A** ／ 難易度: 上級

    **解説:** 機能移行・クラス・トポロでAの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・移行）です。照合移行・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・移行・検証ロです。運用移行・クラスでB:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸はトポロ・クラス・移行です。項目移行・クラス・トポロでC:の所有先確認 構成照合は「ノードの状態と raw_state」を述べるため、正答側の照合軸は検証ロ・クラス・トポロです。仕様移行・クラス・トポロでD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は移行・検証ロ・トポロです。用語移行・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0100**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0100について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0100A
    ```

    画面・出力には PHA72DD0100A が表示され、クラスタ構成検証 Cluster Resources 0100 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0100
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0100B
    ```

    画面・出力には PHA72DD0100B が表示され、クラスタ構成検証 Cluster Resources 0100 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0100
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0100C
    ```

    画面・出力には PHA72DD0100C が表示され、クラスタ構成検証 Cluster Resources 0100 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0100A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0100B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0100C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0115 {#c25-i0391}
*分類: 構成検証*  ・  難易度: 上級

金P移行0116ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票金P移行0116です。金P移行0116はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録金P移行0116です。金P移行0116ではトポロジ要約と取得時刻を採取票金P移行0116へ残します。金P移行0116では警告と致命エラーの混同を避けるため補助資料も照合する判断金P移行0116です。金P移行0116の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録金P移行0116です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0115について構成や状態を確認します。リソースグループ制御 Acquisition Failure 0146ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は保守で獲得イベントを証跡に残し・獲得処理の獲得イベントと取得時刻を記録し。
    - B. 一次資料が示す主目的は計画で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。
    - C. 一次資料が示す主目的は停止確認でマネージャーを証跡に残し・hacmp.out Eventでマネージャーログから。
    - D. 一次資料が示す主目的は移行でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能移行・クラス・トポロでDの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・移行）です。照合移行・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・移行・警告とです。比較クラス・移行でA:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸はクラス・移行・トポロです。運用移行・クラスでB:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はトポロ・クラス・移行です。項目移行・クラス・トポロでC:の停止前の確認 FAIL14は「hacmp.out Eventでマネージャー」を述べるため、正答側の照合軸は警告と・クラス・トポロです。用語移行・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0115**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0115について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0115A
    ```

    画面・出力には PHA72DD0115A が表示され、クラスタ構成検証 Cluster Resources 0115 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0115
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0115B
    ```

    画面・出力には PHA72DD0115B が表示され、クラスタ構成検証 Cluster Resources 0115 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0115
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0115C
    ```

    画面・出力には PHA72DD0115C が表示され、クラスタ構成検証 Cluster Resources 0115 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0115A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0115B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0115C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0130 {#c25-i0392}
*分類: 構成検証*  ・  難易度: 初級

紺K診断0131ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紺K診断0131です。紺K診断0131はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紺K診断0131です。紺K診断0131ではトポロジ要約と取得時刻を採取票紺K診断0131へ残します。紺K診断0131ではノード間ODM差分の残存を避けるため補助資料も照合する判断紺K診断0131です。紺K診断0131の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紺K診断0131です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0130の役割を調べています。リソースグループ制御 Event Summary 0158の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は点検操作で判定欄を記録することで失敗ラベルを確認し・依存リソース順序の見落としを防ぐ。
    - B. 障害切り分けに用いる役割は起動確認でディスク状態を確認することでディスク状態を確認し・ディスク状態の誤読を防ぐ。cltopinfo 起動確認 ディスク状態固有の属性も確認対象に含める。
    - C. 障害切り分けに用いる役割は確認操作で状態欄を整理することでトポロジ要約を確認し・ノード間構成データODM差分を防ぐ。 ✅
    - D. 障害切り分けに用いる役割は採取操作で照合欄を点検することで構成データOを確認し・警告と致命エラーの混同を防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能診断・クラス・トポロでCの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・診断）です。照合診断・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・診断・ノードです。比較クラス・診断でA:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸はクラス・診断・トポロです。運用診断・クラスでB:の起動確認 ディスク状態は「クラスタトポロジー、ネットワーク」を述べるため、正答側の照合軸はトポロ・クラス・診断です。仕様診断・クラス・トポロでD:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は診断・ノード・トポロです。用語診断・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0130**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0130について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0130A
    ```

    画面・出力には PHA72DD0130A が表示され、クラスタ構成検証 Cluster Resources 0130 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0130
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0130B
    ```

    画面・出力には PHA72DD0130B が表示され、クラスタ構成検証 Cluster Resources 0130 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0130
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0130C
    ```

    画面・出力には PHA72DD0130C が表示され、クラスタ構成検証 Cluster Resources 0130 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0130A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0130B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0130C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0145 {#c25-i0393}
*分類: 構成検証*  ・  難易度: 中級

銀F保守0146ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票銀F保守0146です。銀F保守0146はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録銀F保守0146です。銀F保守0146ではトポロジ要約と取得時刻を採取票銀F保守0146へ残します。銀F保守0146では未同期構成の見落としを避けるため補助資料も照合する判断銀F保守0146です。銀F保守0146の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録銀F保守0146です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 Cluster Resources 0145」を「GLVM地理的ミラー syslog entry 0192」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は照合操作で確認欄を採取することでsyslogを確認し・ミラー再同期条件の誤読を防ぐ。
    - B. 仕様上の役割は記録操作で証跡欄を照合することでトポロジ要約を確認し・未同期構成の見落としを防ぐ。 ✅
    - C. 仕様上の役割は再投入確認で再投入確認を確認することで再投入確認を確認し・再投入確認の誤読を防ぐ。
    - D. 仕様上の役割はclinfoES状態からclinfoESことでclinfoを確認し・監視通信SNMP情報の残留をを防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能保守・クラス・トポロでBの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・保守）です。照合保守・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・保守・未同期です。比較保守・クラス・トポロ・未同期でA:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸はクラス・保守・トポロです。項目保守・クラス・トポロでC:の版数確認 再投入確認は「クラスタ、ノード、インターフェース」を述べるため、正答側の照合軸は未同期・クラス・トポロです。仕様保守・クラス・トポロでD:の障害切り分け CLSTAT04は「clstatでclinfoES状態から」を述べるため、正答側の照合軸は保守・未同期・トポロです。用語保守・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0145**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0145について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0145A
    ```

    画面・出力には PHA72DD0145A が表示され、クラスタ構成検証 Cluster Resources 0145 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0145
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0145B
    ```

    画面・出力には PHA72DD0145B が表示され、クラスタ構成検証 Cluster Resources 0145 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0145
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0145C
    ```

    画面・出力には PHA72DD0145C が表示され、クラスタ構成検証 Cluster Resources 0145 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0145A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0145B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0145C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0160 {#c25-i0394}
*分類: 構成検証*  ・  難易度: 中級

蒼A切替0161ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票蒼A切替0161です。蒼A切替0161はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録蒼A切替0161です。蒼A切替0161ではトポロジ要約と取得時刻を採取票蒼A切替0161へ残します。蒼A切替0161では検証ログの採取漏れを避けるため補助資料も照合する判断蒼A切替0161です。蒼A切替0161の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録蒼A切替0161です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0160を同一分類のGLVM地理的ミラー RPV Server 0231と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は地理的ミラーの項目のミラー更新状態と取得時刻を記録し・syslogとhacmp.outの突合漏れを防ぐである。監査操作で記録欄を比較するときはsyslogとhacmp.oを防ぐ。
    - B. コマンドまたは機能の用途はクラスタートポロジーの構成データODM登録値と取得時刻を記録し・警告と致命エラーの混同を防ぐである。採取操作で照合欄を点検するときは警告と致命エラーの混同を防ぐ。
    - C. コマンドまたは機能の用途は資源グループで依存照会から START_AFTER を読み・START_AFTER とである。依存照会からSTART_AFTERをときは依存順を無視して子資源を先にを防ぐ。
    - D. コマンドまたは機能の用途はクラスター資源のトポロジ要約と取得時刻を記録し・検証ログの採取漏れを防ぐである。保守操作で監査欄を保存するときは検証ログの採取漏れを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能切替・クラス・トポロでDの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・切替）です。照合切替・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・切替・検証ロです。比較切替・クラス・トポロ・検証ロでA:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸はクラス・切替・トポロです。運用切替・クラスでB:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸はトポロ・クラス・切替です。項目切替・クラス・トポロでC:の通常状態の確認 DEP01は「資源グループで依存照会から」を述べるため、正答側の照合軸は検証ロ・クラス・トポロです。用語切替・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0160**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0160について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0160A
    ```

    画面・出力には PHA72DD0160A が表示され、クラスタ構成検証 Cluster Resources 0160 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0160
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0160B
    ```

    画面・出力には PHA72DD0160B が表示され、クラスタ構成検証 Cluster Resources 0160 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0160
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0160C
    ```

    画面・出力には PHA72DD0160C が表示され、クラスタ構成検証 Cluster Resources 0160 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0160A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0160B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0160C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0175 {#c25-i0395}
*分類: 構成検証*  ・  難易度: 中級

金P切替0176ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票金P切替0176です。金P切替0176はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録金P切替0176です。金P切替0176ではトポロジ要約と取得時刻を採取票金P切替0176へ残します。金P切替0176では警告と致命エラーの混同を避けるため補助資料も照合する判断金P切替0176です。金P切替0176の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録金P切替0176です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0175の設定や表示を読む前に役割を確認します。リソースグループ制御 Acquisition Failure 0221ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は復旧操作で点検欄を確認することで獲得イベントを確認し・資源グループ位置の誤認を防ぐ。
    - B. 一次資料が示す主目的は整合確認で整合確認を確認することで整合確認を確認し・整合確認の誤読を防ぐ。
    - C. 一次資料が示す主目的は復旧操作で点検欄を確認することで失敗ラベルを確認し・資源グループ位置の誤認を防ぐ。
    - D. 一次資料が示す主目的は採取操作で照合欄を点検することでトポロジ要約を確認し・警告と致命エラーの混同を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能切替・クラス・トポロでDの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・切替）です。照合切替・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・切替・警告とです。比較切替・クラス・トポロ・警告とでA:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸はクラス・切替・トポロです。運用切替・クラスでB:の状態確認 整合確認は「クラスタ構成と状態をスナップショットとして表」を述べるため、正答側の照合軸はトポロ・クラス・切替です。項目切替・クラス・トポロでC:のEvent Summaryは「イベント要約の失敗ラベルと取得時刻を記録し」を述べるため、正答側の照合軸は警告と・クラス・トポロです。用語切替・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0175**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0175について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0175A
    ```

    画面・出力には PHA72DD0175A が表示され、クラスタ構成検証 Cluster Resources 0175 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0175
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0175B
    ```

    画面・出力には PHA72DD0175B が表示され、クラスタ構成検証 Cluster Resources 0175 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0175
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0175C
    ```

    画面・出力には PHA72DD0175C が表示され、クラスタ構成検証 Cluster Resources 0175 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0175A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0175B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0175C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0190 {#c25-i0396}
*分類: 構成検証*  ・  難易度: 中級

紺K収集0191ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紺K収集0191です。紺K収集0191はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紺K収集0191です。紺K収集0191ではトポロジ要約と取得時刻を採取票紺K収集0191へ残します。紺K収集0191ではノード間ODM差分の残存を避けるため補助資料も照合する判断紺K収集0191です。紺K収集0191の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紺K収集0191です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0190に関する障害切り分けの前提を確認しています。リソースグループ制御 Resource Group Name 0245の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は復旧操作で点検欄を確認することで優先ノード一を確認し・資源グループ位置の誤認を防ぐ。
    - B. 障害切り分けに用いる役割は同期確認でファイルセッを確認することでファイルセッを確認し・ファイルセッの誤読を防ぐ。clmgr start cluster 同期確認 ファイルセット固有の属性も確認対象に含める。
    - C. 障害切り分けに用いる役割は採取操作で照合欄を点検することで検証進行率を確認し・警告と致命エラーの混同を防ぐ。
    - D. 障害切り分けに用いる役割は確認操作で状態欄を整理することでトポロジ要約を確認し・ノード間構成データODM差分を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能収集・クラス・トポロでDの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・収集）です。照合収集・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・収集・ノードです。比較収集・クラス・トポロ・ノードでA:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸はクラス・収集・トポロです。運用収集・クラスでB:の同期確認 ファイルセットは「クラスタサービスを開始し、リソースグループを」を述べるため、正答側の照合軸はトポロ・クラス・収集です。項目収集・クラス・トポロでC:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はノード・クラス・トポロです。用語収集・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0190**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0190について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0190A
    ```

    画面・出力には PHA72DD0190A が表示され、クラスタ構成検証 Cluster Resources 0190 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0190
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0190B
    ```

    画面・出力には PHA72DD0190B が表示され、クラスタ構成検証 Cluster Resources 0190 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0190
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0190C
    ```

    画面・出力には PHA72DD0190C が表示され、クラスタ構成検証 Cluster Resources 0190 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0190A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0190B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0190C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0205 {#c25-i0397}
*分類: 構成検証*  ・  難易度: 中級

銀F登録0206ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票銀F登録0206です。銀F登録0206はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録銀F登録0206です。銀F登録0206ではトポロジ要約と取得時刻を採取票銀F登録0206へ残します。銀F登録0206では未同期構成の見落としを避けるため補助資料も照合する判断銀F登録0206です。銀F登録0206の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録銀F登録0206です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0205を保守記録に説明する必要があります。GLVM地理的ミラー VG STATE 0213と取り違えない説明はどれですか。

    - A. 仕様上の役割は登録で基本ソフトAを証跡に残し・地理的ミラーの項目の基本ソフトAIXエラー識別子と取得時刻を。
    - B. 仕様上の役割は所有先確認で依存関係を証跡に残し・クラスタサービスを開始し・リソースグループをオンライン化する。
    - C. 仕様上の役割は診断でリソース要約を証跡に残し・構成検証のリソース要約と取得時刻を記録し。
    - D. 仕様上の役割は登録でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能登録・クラス・トポロでDの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・登録）です。照合登録・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・登録・未同期です。比較登録・クラス・トポロ・未同期でA:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸はクラス・登録・トポロです。運用登録・クラスでB:の所有先確認 依存関係は「クラスタサービスを開始し、リソースグループを」を述べるため、正答側の照合軸はトポロ・クラス・登録です。項目登録・クラス・トポロでC:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸は未同期・クラス・トポロです。用語登録・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0205**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0205について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0205A
    ```

    画面・出力には PHA72DD0205A が表示され、クラスタ構成検証 Cluster Resources 0205 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0205
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0205B
    ```

    画面・出力には PHA72DD0205B が表示され、クラスタ構成検証 Cluster Resources 0205 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0205
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0205C
    ```

    画面・出力には PHA72DD0205C が表示され、クラスタ構成検証 Cluster Resources 0205 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0205A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0205B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0205C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0220 {#c25-i0398}
*分類: 構成検証*  ・  難易度: 上級

蒼A確認0221ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票蒼A確認0221です。蒼A確認0221はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録蒼A確認0221です。蒼A確認0221ではトポロジ要約と取得時刻を採取票蒼A確認0221へ残します。蒼A確認0221では検証ログの採取漏れを避けるため補助資料も照合する判断蒼A確認0221です。蒼A確認0221の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録蒼A確認0221です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0220の技術的な意味を資料で確認するとき、リソースグループ制御 Resource Group Name 0275との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は獲得失敗ログの未採取を避けるため・表示操作で対象欄を追跡するして優先ノード一を照合する。
    - B. コマンドまたは機能の用途は基本ソフト稼働とクラスタ稼働の混を避けるため・ノード一覧から実状態値を読むしてノード一覧を照合する。
    - C. コマンドまたは機能の用途はsyslogとhacmp.outを避けるため・監査操作で記録欄を比較するしてミラー更新状を照合する。
    - D. コマンドまたは機能の用途は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するしてトポロジ要約を照合する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能確認・クラス・トポロでDの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・確認）です。照合確認・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・確認・検証ロです。比較確認・クラス・トポロ・検証ロでA:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸はクラス・確認・トポロです。運用確認・クラスでB:の通常状態の確認 NODE01は「PowerHA Node Stateでノード」を述べるため、正答側の照合軸はトポロ・クラス・確認です。項目確認・クラス・トポロでC:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は検証ロ・クラス・トポロです。用語確認・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0220**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0220について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0220A
    ```

    画面・出力には PHA72DD0220A が表示され、クラスタ構成検証 Cluster Resources 0220 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0220
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0220B
    ```

    画面・出力には PHA72DD0220B が表示され、クラスタ構成検証 Cluster Resources 0220 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0220
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0220C
    ```

    画面・出力には PHA72DD0220C が表示され、クラスタ構成検証 Cluster Resources 0220 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0220A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0220B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0220C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0235 {#c25-i0399}
*分類: 構成検証*  ・  難易度: 上級

金P確認0236ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票金P確認0236です。金P確認0236はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録金P確認0236です。金P確認0236ではトポロジ要約と取得時刻を採取票金P確認0236へ残します。金P確認0236では警告と致命エラーの混同を避けるため補助資料も照合する判断金P確認0236です。金P確認0236の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録金P確認0236です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0235について構成や状態を確認します。クラスタ構成検証 SMIT Command Status 0274ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は照合で検証進行率を証跡に残し・システム管理コマンドの検証進行率と取得時刻を記録し。
    - B. 一次資料が示す主目的は復旧確認で資源グループを証跡に残し・Cluster Servicesで資源グループRG確認から。
    - C. 一次資料が示す主目的は確認でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。 ✅
    - D. 一次資料が示す主目的は監査でVG varを証跡に残し・地理的ミラーの項目のVG vary状態と取得時刻を記録し。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能確認・クラス・トポロでCの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・確認）です。照合確認・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・確認・警告とです。比較確認・クラス・トポロ・警告とでA:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はクラス・確認・トポロです。運用確認・クラスでB:の復旧後の確認 START06は「Cluster Servicesで資源グルー」を述べるため、正答側の照合軸はトポロ・クラス・確認です。仕様確認・クラス・トポロでD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は確認・警告と・トポロです。用語確認・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0235**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0235について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0235A
    ```

    画面・出力には PHA72DD0235A が表示され、クラスタ構成検証 Cluster Resources 0235 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0235
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0235B
    ```

    画面・出力には PHA72DD0235B が表示され、クラスタ構成検証 Cluster Resources 0235 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0235
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0235C
    ```

    画面・出力には PHA72DD0235C が表示され、クラスタ構成検証 Cluster Resources 0235 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0235A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0235B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0235C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0250 {#c25-i0400}
*分類: 構成検証*  ・  難易度: 初級

紺K保護0251ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紺K保護0251です。紺K保護0251はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紺K保護0251です。紺K保護0251ではトポロジ要約と取得時刻を採取票紺K保護0251へ残します。紺K保護0251ではノード間ODM差分の残存を避けるため補助資料も照合する判断紺K保護0251です。紺K保護0251の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紺K保護0251です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0250の役割を調べています。クラスタ構成検証 SMIT Command Status 0334の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は確認操作で状態欄を整理することでトポロジ要約を確認し・ノード間構成データODM差分を防ぐ。 ✅
    - B. 障害切り分けに用いる役割は確認操作で状態欄を整理することで検証進行率を確認し・ノード間構成データODM差分を防ぐ。
    - C. 障害切り分けに用いる役割は未同期確認からUNSYNCED_CHANことで未同期確認を確認し・同期元を誤ると古い定義を全ノを防ぐ。
    - D. 障害切り分けに用いる役割は照合操作で確認欄を採取することで基本ソフトAを確認し・ミラー再同期条件の誤読を防ぐ。

    正解: **A** ／ 難易度: 初級

    **解説:** 機能保護・クラス・トポロでAの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・保護）です。照合保護・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・保護・ノードです。運用保護・クラスでB:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はトポロ・クラス・保護です。項目保護・クラス・トポロでC:の障害切り分け SYNC04は「Cluster Synchronizで未同期」を述べるため、正答側の照合軸はノード・クラス・トポロです。仕様保護・クラス・トポロでD:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸は保護・ノード・トポロです。用語保護・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0250**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0250について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 30 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0250A
    ```

    画面・出力には PHA72DD0250A が表示され、クラスタ構成検証 Cluster Resources 0250 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0250
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0250B
    ```

    画面・出力には PHA72DD0250B が表示され、クラスタ構成検証 Cluster Resources 0250 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0250
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0250C
    ```

    画面・出力には PHA72DD0250C が表示され、クラスタ構成検証 Cluster Resources 0250 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0250A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0250B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0250C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0265 {#c25-i0401}
*分類: 構成検証*  ・  難易度: 中級

銀F照合0266ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票銀F照合0266です。銀F照合0266はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録銀F照合0266です。銀F照合0266ではトポロジ要約と取得時刻を採取票銀F照合0266へ残します。銀F照合0266では未同期構成の見落としを避けるため補助資料も照合する判断銀F照合0266です。銀F照合0266の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録銀F照合0266です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** 「クラスタ構成検証 Cluster Resources 0265」を「GLVM地理的ミラー syslog entry 0312」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するしてトポロジ要約を照合する。 ✅
    - B. 仕様上の役割はミラー再同期条件の誤読を避けるため・照合操作で確認欄を採取するしてsyslogを照合する。
    - C. 仕様上の役割は管理設定と資源状態の混同を避けるため・開始から終了状態を読むして開始を照合する。
    - D. 仕様上の役割は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして資源グループを照合する。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能照合・クラス・トポロでAの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・照合）です。照合照合・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・照合・未同期です。運用照合・クラスでB:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸はトポロ・クラス・照合です。項目照合・クラス・トポロでC:の代替経路の確認 START10は「Cluster Servicesで開始から」を述べるため、正答側の照合軸は未同期・クラス・トポロです。仕様照合・クラス・トポロでD:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は照合・未同期・トポロです。用語照合・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0265**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0265について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 20 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0265A
    ```

    画面・出力には PHA72DD0265A が表示され、クラスタ構成検証 Cluster Resources 0265 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0265
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0265B
    ```

    画面・出力には PHA72DD0265B が表示され、クラスタ構成検証 Cluster Resources 0265 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0265
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0265C
    ```

    画面・出力には PHA72DD0265C が表示され、クラスタ構成検証 Cluster Resources 0265 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0265A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0265B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0265C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0280 {#c25-i0402}
*分類: 構成検証*  ・  難易度: 中級

蒼A抑止0281ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票蒼A抑止0281です。蒼A抑止0281はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録蒼A抑止0281です。蒼A抑止0281ではトポロジ要約と取得時刻を採取票蒼A抑止0281へ残します。蒼A抑止0281では検証ログの採取漏れを避けるため補助資料も照合する判断蒼A抑止0281です。蒼A抑止0281の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録蒼A抑止0281です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0280を同一分類のGLVM地理的ミラー RPV Client 0354と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は遠隔ボリュームRPV経路断の見落を避けるため・変更確認操作で採取欄を棚卸するして遠隔ボリューを照合する。
    - B. コマンドまたは機能の用途はcluster historyだを避けるため・エラー記録からIDENTIFIERを読むしてエラー記録を照合する。
    - C. コマンドまたは機能の用途は獲得失敗ログの未採取を避けるため・表示操作で対象欄を追跡するして獲得イベントを照合する。
    - D. コマンドまたは機能の用途は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するしてトポロジ要約を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能抑止・クラス・トポロでDの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・抑止）です。照合抑止・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・抑止・検証ロです。比較抑止・クラス・トポロ・検証ロでA:のRPV Clientは「地理的ミラーの項目の遠隔ボリュームRPV通信」を述べるため、正答側の照合軸はクラス・抑止・トポロです。運用抑止・クラスでB:の変更後の確認 FAIL03は「hacmp.out Eventでエラー記録か」を述べるため、正答側の照合軸はトポロ・クラス・抑止です。項目抑止・クラス・トポロでC:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は検証ロ・クラス・トポロです。用語抑止・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0280**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0280について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 10 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0280A
    ```

    画面・出力には PHA72DD0280A が表示され、クラスタ構成検証 Cluster Resources 0280 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0280
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0280B
    ```

    画面・出力には PHA72DD0280B が表示され、クラスタ構成検証 Cluster Resources 0280 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0280
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0280C
    ```

    画面・出力には PHA72DD0280C が表示され、クラスタ構成検証 Cluster Resources 0280 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0280A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0280B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0280C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0295 {#c25-i0403}
*分類: 構成検証*  ・  難易度: 中級

金P抑止0296ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票金P抑止0296です。金P抑止0296はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録金P抑止0296です。金P抑止0296ではトポロジ要約と取得時刻を採取票金P抑止0296へ残します。金P抑止0296では警告と致命エラーの混同を避けるため補助資料も照合する判断金P抑止0296です。金P抑止0296の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録金P抑止0296です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0295の設定や表示を読む前に役割を確認します。クラスタ構成検証 SMIT Command Status 0304ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は保守操作で監査欄を保存することで検証進行率を確認し・検証ログの採取漏れを防ぐ。
    - B. 一次資料が示す主目的は調査操作で保守欄を引き継ぎすることで優先ノード一を確認し・自動戻し条件の誤読を防ぐ。
    - C. 一次資料が示す主目的は採取操作で照合欄を点検することで検証報告ROを確認し・警告と致命エラーの混同を防ぐ。
    - D. 一次資料が示す主目的は採取操作で照合欄を点検することでトポロジ要約を確認し・警告と致命エラーの混同を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能抑止・クラス・トポロでDの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・抑止）です。照合抑止・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・抑止・警告とです。比較抑止・クラス・トポロ・警告とでA:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はクラス・抑止・トポロです。運用抑止・クラスでB:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸はトポロ・クラス・抑止です。項目抑止・クラス・トポロでC:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸は警告と・クラス・トポロです。用語抑止・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0295**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0295について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 80 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0295A
    ```

    画面・出力には PHA72DD0295A が表示され、クラスタ構成検証 Cluster Resources 0295 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0295
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0295B
    ```

    画面・出力には PHA72DD0295B が表示され、クラスタ構成検証 Cluster Resources 0295 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0295
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0295C
    ```

    画面・出力には PHA72DD0295C が表示され、クラスタ構成検証 Cluster Resources 0295 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0295A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0295B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0295C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0310 {#c25-i0404}
*分類: 構成検証*  ・  難易度: 中級

紺K解析0311ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票紺K解析0311です。紺K解析0311はクラスタ構成検証の確認操作でクラスタ構成検証の状態欄を整理する記録紺K解析0311です。紺K解析0311ではトポロジ要約と取得時刻を採取票紺K解析0311へ残します。紺K解析0311ではノード間ODM差分の残存を避けるため補助資料も照合する判断紺K解析0311です。紺K解析0311の用語整理ではクラスタ構成検証の対象値を実在出力で読み分けする記録紺K解析0311です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0310に関する障害切り分けの前提を確認しています。cltopinfo 整合確認 確認範囲の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は確認範囲で確認範囲を証跡に残し・クラスタトポロジー・ネットワーク・サービスIP。
    - B. 障害切り分けに用いる役割は解析でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。 ✅
    - C. 障害切り分けに用いる役割は巡回で移動履歴を証跡に残し・ノード一覧の移動履歴と取得時刻を記録し。
    - D. 障害切り分けに用いる役割は収集でミラー更新状を証跡に残し・地理的ミラーの項目のミラー更新状態と取得時刻を記録し。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能解析・クラス・トポロでBの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・解析）です。照合解析・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・解析・ノードです。比較解析・クラス・トポロ・ノードでA:の整合確認 確認範囲は「クラスタトポロジー、ネットワーク」を述べるため、正答側の照合軸はクラス・解析・トポロです。項目解析・クラス・トポロでC:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸はノード・クラス・トポロです。仕様解析・クラス・トポロでD:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は解析・ノード・トポロです。用語解析・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・ノードです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0310**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0310について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 70 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0310A
    ```

    画面・出力には PHA72DD0310A が表示され、クラスタ構成検証 Cluster Resources 0310 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0310
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0310B
    ```

    画面・出力には PHA72DD0310B が表示され、クラスタ構成検証 Cluster Resources 0310 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0310
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0310C
    ```

    画面・出力には PHA72DD0310C が表示され、クラスタ構成検証 Cluster Resources 0310 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0310A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0310B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0310C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0325 {#c25-i0405}
*分類: 構成検証*  ・  難易度: 中級

銀F計画0326ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票銀F計画0326です。銀F計画0326はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録銀F計画0326です。銀F計画0326ではトポロジ要約と取得時刻を採取票銀F計画0326へ残します。銀F計画0326では未同期構成の見落としを避けるため補助資料も照合する判断銀F計画0326です。銀F計画0326の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録銀F計画0326です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0325を保守記録に説明する必要があります。リソースグループ制御 Acquisition Failure 0341と取り違えない説明はどれですか。

    - A. 仕様上の役割は復旧操作で点検欄を確認することで獲得イベントを確認し・資源グループ位置の誤認を防ぐ。
    - B. 仕様上の役割はエラー記録からIDENTIFIERを読むことでエラー記録を確認し・cluster historを防ぐ。
    - C. 仕様上の役割は記録操作で証跡欄を照合することでトポロジ要約を確認し・未同期構成の見落としを防ぐ。 ✅
    - D. 仕様上の役割は確認操作で状態欄を整理することで検証進行率を確認し・ノード間構成データODM差分を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能計画・クラス・トポロでCの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・計画）です。照合計画・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・計画・未同期です。比較計画・クラス・トポロ・未同期でA:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸はクラス・計画・トポロです。運用計画・クラスでB:の再始動後の確認 FAIL15は「hacmp.out Eventでエラー記録か」を述べるため、正答側の照合軸はトポロ・クラス・計画です。仕様計画・クラス・トポロでD:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸は計画・未同期・トポロです。用語計画・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0325**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0325について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 60 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0325A
    ```

    画面・出力には PHA72DD0325A が表示され、クラスタ構成検証 Cluster Resources 0325 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0325
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0325B
    ```

    画面・出力には PHA72DD0325B が表示され、クラスタ構成検証 Cluster Resources 0325 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0325
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0325C
    ```

    画面・出力には PHA72DD0325C が表示され、クラスタ構成検証 Cluster Resources 0325 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0325A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0325B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0325C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0340 {#c25-i0406}
*分類: 構成検証*  ・  難易度: 上級

蒼A解除0341ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票蒼A解除0341です。蒼A解除0341はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録蒼A解除0341です。蒼A解除0341ではトポロジ要約と取得時刻を採取票蒼A解除0341へ残します。蒼A解除0341では検証ログの採取漏れを避けるため補助資料も照合する判断蒼A解除0341です。蒼A解除0341の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録蒼A解除0341です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0340の技術的な意味を資料で確認するとき、cltopinfo 状態確認 対象ファイルとの境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は状態確認で対象ファイルを確認することで対象ファイルを確認し・対象ファイルの誤読を防ぐ。
    - B. コマンドまたは機能の用途はRG一覧からdatabase_rgを読むことで資源グループを確認し・依存順を無視して子資源を先にを防ぐ。
    - C. コマンドまたは機能の用途は調査操作で保守欄を引き継ぎすることで移動履歴を確認し・自動戻し条件の誤読を防ぐ。
    - D. コマンドまたは機能の用途は保守操作で監査欄を保存することでトポロジ要約を確認し・検証ログの採取漏れを防ぐ。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能解除・クラス・トポロでDの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・解除）です。照合解除・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・解除・検証ロです。比較解除・クラス・トポロ・検証ロでA:の状態確認 対象ファイルは「クラスタトポロジー、ネットワーク」を述べるため、正答側の照合軸はクラス・解除・トポロです。運用解除・クラスでB:の変更前の確認 DEP02は「資源グループで資源グループRG一覧から」を述べるため、正答側の照合軸はトポロ・クラス・解除です。項目解除・クラス・トポロでC:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は検証ロ・クラス・トポロです。用語解除・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0340**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0340について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 50 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0340A
    ```

    画面・出力には PHA72DD0340A が表示され、クラスタ構成検証 Cluster Resources 0340 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0340
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0340B
    ```

    画面・出力には PHA72DD0340B が表示され、クラスタ構成検証 Cluster Resources 0340 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0340
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0340C
    ```

    画面・出力には PHA72DD0340C が表示され、クラスタ構成検証 Cluster Resources 0340 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0340A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0340B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0340C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Resources 0355 {#c25-i0407}
*分類: 構成検証*  ・  難易度: 上級

金P解除0356ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票金P解除0356です。金P解除0356はクラスタ構成検証の採取操作でクラスタ構成検証の照合欄を点検する記録金P解除0356です。金P解除0356ではトポロジ要約と取得時刻を採取票金P解除0356へ残します。金P解除0356では警告と致命エラーの混同を避けるため補助資料も照合する判断金P解除0356です。金P解除0356の用語整理ではクラスタ構成検証の対象値を実在出力で評価する記録金P解除0356です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Resources 0355について構成や状態を確認します。トポロジー Cluster Topology 変更前の確認 TOPO02ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は変更確認でネットワークを証跡に残し・クラスタートポロジーでネットワーク照会から。
    - B. 一次資料が示す主目的は復旧で獲得イベントを証跡に残し・獲得処理の獲得イベントと取得時刻を記録し。
    - C. 一次資料が示す主目的は登録で優先ノード一を証跡に残し・資源グループの優先ノード一覧と取得時刻を記録し。
    - D. 一次資料が示す主目的は解除でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 機能解除・クラス・トポロでDの記述「クラスター資源のトポロジ要約と取得時刻を記録し」に対応する項目はCluster Resources（クラス・トポロ・解除）です。照合解除・クラス・トポロに関する構成検証の仕様は「クラスター資源のトポロジ要約と取得時刻を記録し」で、確認対象はトポロ・解除・警告とです。比較解除・クラス・トポロ・警告とでA:の変更前の確認 TOPO02は「クラスタートポロジーでネットワーク照会から」を述べるため、正答側の照合軸はクラス・解除・トポロです。運用解除・クラスでB:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸はトポロ・クラス・解除です。項目解除・クラス・トポロでC:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は警告と・クラス・トポロです。用語解除・クラス・トポロという用語は「クラスター資源のトポロジ要約と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはクラス・トポロ・警告とです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Resources 0355**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Resources 0355について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Cluster Resources と トポロジ要約
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr view report roha
    → Enter を押す
    ```

    画面・出力:
    ```text
    Verification to be performed on cluster topology and cluster resources
    Completed 40 percent of the verification checks
    Node nodeA data collection completed
    確認コード PHA72DD0355A
    ```

    画面・出力には PHA72DD0355A が表示され、クラスタ構成検証 Cluster Resources 0355 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> grep -i warning /var/hacmp/log/clverify.log
    → Enter を押す
    ```

    画面・出力:
    ```text
    clverify.log entry PHA0355
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0355B
    ```

    画面・出力には PHA72DD0355B が表示され、クラスタ構成検証 Cluster Resources 0355 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Cluster Resources を読むため、クラスタ構成検証 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clverify -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ROHA report PHA0355
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0355C
    ```

    画面・出力には PHA72DD0355C が表示され、クラスタ構成検証 Cluster Resources 0355 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0355A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0355B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0355C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0013 {#c25-i0408}
*分類: 構成検証*  ・  難易度: 初級

灰N巡回0014ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票灰N巡回0014です。灰N巡回0014はクラスタ構成検証の記録操作でクラスタ構成検証の証跡欄を照合する記録灰N巡回0014です。灰N巡回0014ではODM登録値と取得時刻を採取票灰N巡回0014へ残します。灰N巡回0014では未同期構成の見落としを避けるため補助資料も照合する判断灰N巡回0014です。灰N巡回0014の用語整理ではクラスタ構成検証の対象値を実在出力で比較する記録灰N巡回0014です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0013を保守記録に説明する必要があります。クラスタ構成検証 Cluster Resources 0055と取り違えない説明はどれですか。

    - A. 仕様上の役割は復旧でトポロジ要約を証跡に残し・クラスター資源のトポロジ要約と取得時刻を記録し。クラスタ構成検証 Cluster Resources 0055固有の属性も確認対象に含める。
    - B. 仕様上の役割は照合でsyslogを証跡に残し・地理的ミラーの項目のsyslog記録と取得時刻を記録し。
    - C. 仕様上の役割は代替経路確認でクラスタ照会を証跡に残し・クラスタートポロジーでクラスタ照会から。
    - D. 仕様上の役割は巡回で構成データOを証跡に残し・クラスタートポロジーの構成データODM登録値と取得時刻を記録。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** 機能巡回・クラス・構成デでDの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・巡回）です。照合巡回・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・巡回・未同期です。比較クラス・巡回でA:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸はクラス・巡回・構成デです。運用巡回・クラスでB:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は構成デ・クラス・巡回です。項目巡回・クラス・構成デでC:の代替経路の確認 TOPO10は「クラスタートポロジーでクラスタ照会から」を述べるため、正答側の照合軸は未同期・クラス・構成デです。用語巡回・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・未同期です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0013**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0013について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード PHA72DD0013A
    ```

    画面・出力には PHA72DD0013A が表示され、クラスタ構成検証 Cluster Topology 0013 の入力欄確認を確認できます。

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
    clverify.log entry PHA0013
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0013B
    ```

    画面・出力には PHA72DD0013B が表示され、クラスタ構成検証 Cluster Topology 0013 の証跡表示確認を確認できます。

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
    ROHA report PHA0013
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0013C
    ```

    画面・出力には PHA72DD0013C が表示され、クラスタ構成検証 Cluster Topology 0013 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0013A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0013B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0013C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### クラスタ構成検証 Cluster Topology 0028 {#c25-i0409}
*分類: 構成検証*  ・  難易度: 中級

黄I棚卸0029ではPowerHA SystemMirror 7.2 の 構成検証を扱う採取票黄I棚卸0029です。黄I棚卸0029はクラスタ構成検証の保守操作でクラスタ構成検証の監査欄を保存する記録黄I棚卸0029です。黄I棚卸0029ではODM登録値と取得時刻を採取票黄I棚卸0029へ残します。黄I棚卸0029では検証ログの採取漏れを避けるため補助資料も照合する判断黄I棚卸0029です。黄I棚卸0029の用語整理ではクラスタ構成検証の対象値を実在出力で区別する記録黄I棚卸0029です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** クラスタ構成検証 Cluster Topology 0028の技術的な意味を資料で確認するとき、リソースグループ制御 Node List 0077との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は保守操作で監査欄を保存することで構成データOを確認し・検証ログの採取漏れを防ぐ。 ✅
    - B. コマンドまたは機能の用途は復旧操作で点検欄を確認することで移動履歴を確認し・資源グループ位置の誤認を防ぐ。
    - C. コマンドまたは機能の用途は保守操作で監査欄を保存することで検証進行率を確認し・検証ログの採取漏れを防ぐ。
    - D. コマンドまたは機能の用途はノード一覧から実状態値を読むことでノード一覧を確認し・基本ソフト稼働とクラスタ稼働を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能棚卸・クラス・構成デでAの記述「クラスタートポロジーの構成データODM登録値と取得時刻を」に対応する項目はCluster Topology（クラス・構成デ・棚卸）です。照合棚卸・クラス・構成デに関する構成検証の仕様は「クラスタートポロジーの構成データODM登録値と取得時刻を記録し」で、確認対象は構成デ・棚卸・検証ロです。運用棚卸・クラスでB:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は構成デ・クラス・棚卸です。項目棚卸・クラス・構成デでC:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸は検証ロ・クラス・構成デです。仕様棚卸・クラス・構成デでD:の代替経路の確認 NODE10は「PowerHA Node Stateでノード」を述べるため、正答側の照合軸は棚卸・検証ロ・構成デです。用語棚卸・クラス・構成デという用語は「クラスタートポロジーの構成データODM登録値と取得時」を指し、照合する値と誤認リスクの組合せはクラス・構成デ・検証ロです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **クラスタ構成検証 Cluster Topology 0028**

    - 検証目的: クラスタ構成検証のクラスタ構成検証 Cluster Topology 0028について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
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
    確認コード PHA72DD0028A
    ```

    画面・出力には PHA72DD0028A が表示され、クラスタ構成検証 Cluster Topology 0028 の入力欄確認を確認できます。

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
    clverify.log entry PHA0028
    Warning group network labels reviewed
    Cluster resources synchronized after review
    確認コード PHA72DD0028B
    ```

    画面・出力には PHA72DD0028B が表示され、クラスタ構成検証 Cluster Topology 0028 の証跡表示確認を確認できます。

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
    ROHA report PHA0028
    Dynamic resource operation recorded
    clmgr verify cluster completed with review notes
    確認コード PHA72DD0028C
    ```

    画面・出力には PHA72DD0028C が表示され、クラスタ構成検証 Cluster Topology 0028 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0028A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0028B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0028C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



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


