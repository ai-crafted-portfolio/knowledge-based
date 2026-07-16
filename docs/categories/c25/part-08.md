---
search:
  exclude: true
---

# PowerHA SystemMirror 7.2 — 詳細 (8/11)

[← PowerHA SystemMirror 7.2 の概要へ戻る](index.md)


## PowerHA SystemMirror 7.2 > リソースグループ

### リソースグループ制御 Resource Group Name 0335 {#c25-i0360}
*分類: リソースグループ*  ・  難易度: 中級

金P計画0336ではPowerHA SystemMirror 7.2 の リソースグループを扱う採取票金P計画0336です。金P計画0336はリソースグループ制御の表示操作でリソースグループ制御の対象欄を追跡する記録金P計画0336です。金P計画0336では優先ノード一覧と取得時刻を採取票金P計画0336へ残します。金P計画0336では獲得失敗ログの未採取を避けるため補助資料も照合する判断金P計画0336です。金P計画0336の用語整理ではリソースグループ制御の対象値を実在出力で照合する記録金P計画0336です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** リソースグループ制御 Resource Group Name 0335の設定や表示を読む前に役割を確認します。クラスタ構成検証 SMIT Command Status 0349ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして検証進行率を照合する。
    - B. 状態を読み取るための働きは遠隔ボリュームRPV経路断の見落を避けるため・変更確認操作で採取欄を棚卸するしてミラー更新状を照合する。
    - C. 状態を読み取るための働きは獲得失敗ログの未採取を避けるため・表示操作で対象欄を追跡するして優先ノード一を照合する。 ✅
    - D. 状態を読み取るための働きは未同期構成の見落としを避けるため・記録操作で証跡欄を照合するして検証報告ROを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能計画・リソー・優先ノでCの記述「資源グループの優先ノード一覧と取得時刻を記録し」に対応する項目はGroup Name（資源グ・優先ノ・計画）です。照合計画・リソー・優先ノに関するリソースグループの仕様は「資源グループの優先ノード一覧と取得時刻を記録し」で、確認対象は優先ノ・計画・獲得失です。比較計画・リソー・優先ノ・獲得失でA:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸は資源グ・計画・優先ノです。運用計画・資源グでB:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は優先ノ・リソー・計画です。仕様計画・リソー・優先ノでD:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸は計画・獲得失・優先ノです。用語計画・リソー・優先ノという用語は「資源グループの優先ノード一覧と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはリソー・優先ノ・獲得失です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **リソースグループ制御 Resource Group Name 0335**

    - 検証目的: リソースグループ制御のリソースグループ制御 Resource Group Name 0335について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Resource Group Name と 優先ノード一覧
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Resource Group Name を読むため、リソースグループ制御 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr query resource_group
    → Enter を押す
    ```

    画面・出力:
    ```text
    Resource Group rg_app_95
    Node List nodeA nodeB
    Online Node nodeA
    確認コード PHA72DD0335A
    ```

    画面・出力には PHA72DD0335A が表示され、リソースグループ制御 Resource Group Name 0335 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Resource Group Name を読むため、リソースグループ制御 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clRGinfo -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    hacmp.out PHA0335
    Resource group acquisition completed
    Application controller start method recorded
    確認コード PHA72DD0335B
    ```

    画面・出力には PHA72DD0335B が表示され、リソースグループ制御 Resource Group Name 0335 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Resource Group Name を読むため、リソースグループ制御 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr query resource_group
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgr.debug PHA0335
    Event resource group move processed
    Fallback policy evaluated
    確認コード PHA72DD0335C
    ```

    画面・出力には PHA72DD0335C が表示され、リソースグループ制御 Resource Group Name 0335 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0335A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0335B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0335C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434



### リソースグループ制御 Resource Group Name 0350 {#c25-i0361}
*分類: リソースグループ*  ・  難易度: 上級

紺K解除0351ではPowerHA SystemMirror 7.2 の リソースグループを扱う採取票紺K解除0351です。紺K解除0351はリソースグループ制御の点検操作でリソースグループ制御の判定欄を記録する記録紺K解除0351です。紺K解除0351では優先ノード一覧と取得時刻を採取票紺K解除0351へ残します。紺K解除0351では依存リソース順序の見落としを避けるため補助資料も照合する判断紺K解除0351です。紺K解除0351の用語整理ではリソースグループ制御の対象値を実在出力で保管する記録紺K解除0351です。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434

??? question "確認問題（1問）"
    **問題.** リソースグループ制御 Resource Group Name 0350に関する障害切り分けの前提を確認しています。ノード状態 PowerHA Node State 障害切り分け NODE04の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはノード状態でノード一覧を証跡に残し・PowerHA Node Stateでノード一覧から。
    - B. 機能の説明としては資源依存関係でイベント順序を証跡に残し・資源グループでイベント順序から completed を読み。
    - C. 機能の説明としては解除で優先ノード一を証跡に残し・資源グループの優先ノード一覧と取得時刻を記録し。 ✅
    - D. 機能の説明としては確認でsyslogを証跡に残し・地理的ミラーの項目のsyslog記録と取得時刻を記録し。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能解除・リソー・優先ノでCの記述「資源グループの優先ノード一覧と取得時刻を記録し」に対応する項目はGroup Name（資源グ・優先ノ・解除）です。照合解除・リソー・優先ノに関するリソースグループの仕様は「資源グループの優先ノード一覧と取得時刻を記録し」で、確認対象は優先ノ・解除・依存リです。比較解除・リソー・優先ノ・依存リでA:の障害切り分け NODE04は「PowerHA Node Stateでノード」を述べるため、正答側の照合軸は資源グ・解除・優先ノです。運用解除・資源グでB:の引継ぎ記録 DEP09は「資源グループでイベント順序から」を述べるため、正答側の照合軸は優先ノ・リソー・解除です。仕様解除・リソー・優先ノでD:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は解除・依存リ・優先ノです。用語解除・リソー・優先ノという用語は「資源グループの優先ノード一覧と取得時刻を記録し」を指し、照合する値と誤認リスクの組合せはリソー・優先ノ・依存リです。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434


??? note "検証手順（1件）"
    **リソースグループ制御 Resource Group Name 0350**

    - 検証目的: リソースグループ制御のリソースグループ制御 Resource Group Name 0350について、登録資料で確認できる実在コマンドまたは実在レポート形式を机上で照合する。
    - 前提条件: 対象資料を確認済み。対象=Resource Group Name と 優先ノード一覧
    - セッション環境: 机上検証。PowerHA SystemMirror 7.2のコマンド、管理画面、レポート、ログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Resource Group Name を読むため、リソースグループ制御 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr query resource_group
    → Enter を押す
    ```

    画面・出力:
    ```text
    Resource Group rg_app_110
    Node List nodeA nodeB
    Online Node nodeA
    確認コード PHA72DD0350A
    ```

    画面・出力には PHA72DD0350A が表示され、リソースグループ制御 Resource Group Name 0350 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Resource Group Name を読むため、リソースグループ制御 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clRGinfo -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    hacmp.out PHA0350
    Resource group acquisition completed
    Application controller start method recorded
    確認コード PHA72DD0350B
    ```

    画面・出力には PHA72DD0350B が表示され、リソースグループ制御 Resource Group Name 0350 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の確認画面またはコマンド結果です。Resource Group Name を読むため、リソースグループ制御 の対象値を表示します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面またはコマンド環境
    COMMAND ===> clmgr query resource_group
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstrmgr.debug PHA0350
    Event resource group move processed
    Fallback policy evaluated
    確認コード PHA72DD0350C
    ```

    画面・出力には PHA72DD0350C が表示され、リソースグループ制御 Resource Group Name 0350 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の PHA72DD0350A が画面・出力に表示されること
    ② ステップ2 の PHA72DD0350B が画面・出力に表示されること
    ③ ステップ3 の PHA72DD0350C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / EN_PowerHA72_GLVM_EE / RB_PowerHA723_Updates_SG248434




## PowerHA SystemMirror 7.2 > 同期処理

### clRGinfo 所有先確認 対象ノード {#c25-i0362}
*分類: 同期処理*  ・  難易度: 中級

PowerHA SystemMirror 7.2 の 同期処理 で扱う「clRGinfo 所有先確認 対象ノード」は、リソースグループの状態と所有ノードを表示するコマンドを所有先確認の観点で確認する技術項目です。CLversion 行とclnode_3を同じ記録で見比べることで、サービスIP定義の不一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** clRGinfo 所有先確認 対象ノードの設定や表示を読む前に役割を確認します。ノード状態 PowerHA Node State 変更前の確認 NODE02ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはリソースグループの状態と所有ノードを表示するコマンドを所有先確認する。所有先確認で対象ノードを確認するときは対象ノードの誤読を防ぐ。 ✅
    - B. 状態を読み取るための働きはPowerHA Node Stateでサブシステム状態から クラスター管理プロセス を読みである。SRC状態からクラスター管理プロセスときは基本ソフト稼働とクラスタ稼働を防ぐ。
    - C. 状態を読み取るための働きはノード一覧の移動履歴と取得時刻を記録し・獲得失敗ログの未採取を防ぐである。表示操作で対象欄を追跡するときは獲得失敗ログの未採取を防ぐ。
    - D. 状態を読み取るための働きは資源グループの優先ノード一覧と取得時刻を記録し・獲得失敗ログの未採取を防ぐである。表示操作で対象欄を追跡するときは獲得失敗ログの未採取を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能所有先・所有先・対象ノでAの記述「リソースグループの状態と所有ノードを表示するコマンドを所」に対応する項目は所有先確認 対象ノード（clR・対象ノ・所有先）です。照合所有先・所有先・対象ノに関する同期処理の仕様は「リソースグループの状態と所有ノードを表示するコマンドを所有先確認する」で、確認対象は対象ノ・所有先・対象ノです。運用所有先・clRでB:の変更前の確認 NODE02は「PowerHA Node Stateでサブシ」を述べるため、正答側の照合軸は対象ノ・所有先・所有先です。項目所有先・所有先・対象ノでC:のNode Listは「ノード一覧の移動履歴と取得時刻を記録し」を述べるため、正答側の照合軸は対象ノ・所有先・対象ノです。仕様所有先・所有先・対象ノでD:のGroup Nameは「資源グループの優先ノード一覧と取得時刻を記録」を述べるため、正答側の照合軸は所有先・対象ノ・対象ノです。用語所有先・所有先・対象ノという用語は「リソースグループの状態と所有ノードを表示するコマンド」を指し、照合する値と誤認リスクの組合せは所有先・対象ノ・対象ノです。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **clRGinfo 所有先確認 対象ノード**

    - 検証目的: 同期処理のclRGinfo 所有先確認 対象ノードについて、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、同期処理の対象へ進みます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> cltopinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Cluster Name:    prodcluster047
    Heartbeat Type:  Unicast
    Repository Disk: hdisk2
    Resource Group rg_app_047
    Service IP Label clst_svcIP_047
    ```

    画面・出力には Cluster が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。CLversion 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clRGinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Group Name     Group State                  Node
    rg_app_047     ONLINE                       clnode_1
                   OFFLINE                      clnode_2
    ```

    画面・出力には Group が含まれ、clRGinfo 所有先確認 対象ノードの証跡を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の詳細確認画面です。表示名とメッセージ形式を照合し、サービスIP定義の不一致を切り分けます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr query resource_group rg_app_047
    → Enter を押す
    ```

    画面・出力:
    ```text
    NAME="rg_app_047"
    STATE="ONLINE"
    PARTICIPATING_NODES="clnode_1 clnode_2"
    ```

    画面・出力には NAME= が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Cluster が画面・出力に表示されること
    ② ステップ2 の Group が画面・出力に表示されること
    ③ ステップ3 の NAME= が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting



### clRGinfo 障害切り分け 識別値 {#c25-i0363}
*分類: 同期処理*  ・  難易度: 初級

PowerHA SystemMirror 7.2 の 同期処理 で扱う「clRGinfo 障害切り分け 識別値」は、リソースグループの状態と所有ノードを表示するコマンドを障害切り分けの観点で確認する技術項目です。CLversion 行とclst_svcIP_007を同じ記録で見比べることで、サービスIP定義の不一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** clRGinfo 障害切り分け 識別値の設定や表示を読む前に役割を確認します。clmgr verify cluster 同期確認 出力比較ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はクラスタトポロジーとリソースの整合性を検査するコマンドを同期確認する。同期確認で出力比較を確認するときは出力比較の誤読を防ぐ。
    - B. 一次資料が示す主目的はクラスタートポロジーの構成データODM登録値と取得時刻を記録し・未同期構成の見落としを防ぐである。記録操作で証跡欄を照合するときは未同期構成の見落としを防ぐ。
    - C. 一次資料が示す主目的はリソースグループの状態と所有ノードを表示するコマンドである。同期処理で識別値を確認するときは識別値の誤読を防ぐ。 ✅
    - D. 一次資料が示す主目的は構成検証のリソース要約と取得時刻を記録し・警告と致命エラーの混同を防ぐである。採取操作で照合欄を点検するときは警告と致命エラーの混同を防ぐ。

    正解: **C** ／ 難易度: 初級

    **解説:** 機能同期処・障害切・識別値でCの記述「リソースグループの状態と所有ノードを表示するコマンドであ」に対応する項目は障害切り分け 識別値（clR・識別値・同期処）です。照合同期処・障害切・識別値に関する同期処理の仕様は「リソースグループの状態と所有ノードを表示するコマンド」で、確認対象は識別値・同期処・識別値です。比較同期処・障害切・識別値・識別値でA:の同期確認 出力比較は「クラスタトポロジーとリソースの整合性を検査す」を述べるため、正答側の照合軸はclR・同期処・識別値です。運用同期処・clRでB:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は識別値・障害切・同期処です。仕様同期処・障害切・識別値でD:のVerificationは「構成検証のリソース要約と取得時刻を記録し」を述べるため、正答側の照合軸は同期処・識別値・識別値です。用語同期処・障害切・識別値という用語は「リソースグループの状態と所有ノードを表示するコマンド」を指し、照合する値と誤認リスクの組合せは障害切・識別値・識別値です。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **clRGinfo 障害切り分け 識別値**

    - 検証目的: 同期処理のclRGinfo 障害切り分け 識別値について、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、同期処理の対象へ進みます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> cltopinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Cluster Name:    prodcluster007
    Heartbeat Type:  Unicast
    Repository Disk: hdisk2
    Resource Group rg_app_007
    Service IP Label clst_svcIP_007
    ```

    画面・出力には Cluster が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。CLversion 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clRGinfo
    → Enter を押す
    ```

    画面・出力:
    ```text
    Group Name     Group State                  Node
    rg_app_007     ONLINE                       clnode_1
                   OFFLINE                      clnode_2
    ```

    画面・出力には Group が含まれ、clRGinfo 障害切り分け 識別値の証跡を確認できます。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の詳細確認画面です。表示名とメッセージ形式を照合し、サービスIP定義の不一致を切り分けます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr query resource_group rg_app_007
    → Enter を押す
    ```

    画面・出力:
    ```text
    NAME="rg_app_007"
    STATE="ONLINE"
    PARTICIPATING_NODES="clnode_1 clnode_2"
    ```

    画面・出力には NAME= が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の Cluster が画面・出力に表示されること
    ② ステップ2 の Group が画面・出力に表示されること
    ③ ステップ3 の NAME= が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting



### clmgr query node 状態確認 サンプル採取 {#c25-i0364}
*分類: 同期処理*  ・  難易度: 中級

PowerHA SystemMirror 7.2 の 同期処理 で扱う「clmgr query node 状態確認 サンプル採取」は、ノードの状態と raw_state を確認するコマンドを状態確認の観点で確認する技術項目です。CLversion 行とclnode_3を同じ記録で見比べることで、検証警告の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** clmgr query node 状態確認 サンプル採取の設定や表示を読む前に役割を確認します。clmgr verify cluster 整合確認 装置一覧ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは整合確認で装置一覧を証跡に残し・クラスタトポロジーとリソースの整合性を検査するコマンドを整合。
    - B. 状態を読み取るための働きは監査で資源グループを証跡に残し・オンラインノードの資源グループRG現在位置と取得時刻を記録し。リソースグループ制御 Online Node 0074固有の属性も確認対象に含める。
    - C. 状態を読み取るための働きはサンプル採取でサンプル採取を証跡に残し・ノードの状態と raw_state を確認するコマンド。 ✅
    - D. 状態を読み取るための働きは登録でVG varを証跡に残し・地理的ミラーの項目のVG vary状態と取得時刻を記録し。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能サンプ・状態・サンプでCの記述「ノードの状態と raw_state」に対応する項目は状態確認 サンプル採取（clm・サンプ・サンプ）です。照合サンプ・状態・サンプに関する同期処理の仕様は「ノードの状態と raw_state を確認するコマンド」で、確認対象はサンプ・サンプ・サンプです。比較サンプ・状態・サンプ・サンプでA:の整合確認 装置一覧は「クラスタトポロジーとリソースの整合性を検査す」を述べるため、正答側の照合軸はclm・サンプ・サンプです。運用サンプ・clmでB:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸はサンプ・状態・サンプです。仕様サンプ・状態・サンプでD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸はサンプ・サンプ・サンプです。用語サンプ・状態・サンプという用語は「ノードの状態と raw_state」を指し、照合する値と誤認リスクの組合せは状態・サンプ・サンプです。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **clmgr query node 状態確認 サンプル採取**

    - 検証目的: 同期処理のclmgr query node 状態確認 サンプル採取について、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、同期処理の対象へ進みます。
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
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。CLversion 行を読むため、対象名を含む操作を入力します。
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

    画面・出力には root が含まれ、clmgr query node 状態確認 サンプル採取の証跡を確認できます。

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



### clmgr sync cluster 版数確認 再読込 {#c25-i0365}
*分類: 同期処理*  ・  難易度: 中級

PowerHA SystemMirror 7.2 の 同期処理 で扱う「clmgr sync cluster 版数確認 再読込」は、検証後に構成を同期し、クラスタスナップショットを作成する操作を版数確認の観点で確認する技術項目です。CLversion 行とcltopinfo 015を同じ記録で見比べることで、所有ノードの誤認を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** clmgr sync cluster 版数確認 再読込の設定や表示を読む前に役割を確認します。ノード状態 PowerHA Node State 再始動後の確認 NODE15ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはイベント確認から終了状態を読むことでイベント確認を確認し・基本ソフト稼働とクラスタ稼働を防ぐ。
    - B. 対象資源に対する働きは照合操作で確認欄を採取することで基本ソフトAを確認し・ミラー再同期条件の誤読を防ぐ。
    - C. 対象資源に対する働きは版数確認で再読込を確認することで再読込を確認し・再読込の誤読を防ぐ。 ✅
    - D. 対象資源に対する働きは確認操作で状態欄を整理することで構成データOを確認し・ノード間構成データODM差分を防ぐ。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能版数確・版数・再読込でCの記述「検証後に構成を同期し、クラスタスナップショットを作成する」に対応する項目は版数確認 再読込（clm・再読込・版数確）です。照合版数確・版数・再読込に関する同期処理の仕様は「検証後に構成を同期し、クラスタスナップショットを作成する操作を版数確」で、確認対象は再読込・版数確・再読込です。比較版数確・版数・再読込・再読込でA:の再始動後の確認 NODE15は「PowerHA Node Stateでイベン」を述べるため、正答側の照合軸はclm・版数確・再読込です。運用版数確・clmでB:のVG STATEは「地理的ミラーの項目の基本ソフトAIXエラー識」を述べるため、正答側の照合軸は再読込・版数・版数確です。仕様版数確・版数・再読込でD:のCluster Topologyは「クラスタートポロジーの構成データODM登録値」を述べるため、正答側の照合軸は版数確・再読込・再読込です。用語版数確・版数・再読込という用語は「検証後に構成を同期し、クラスタスナップショットを作成」を指し、照合する値と誤認リスクの組合せは版数・再読込・再読込です。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **clmgr sync cluster 版数確認 再読込**

    - 検証目的: 同期処理のclmgr sync cluster 版数確認 再読込について、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、同期処理の対象へ進みます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clstat -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstat - Cluster Status Monitor
    Cluster: prodcluster015
    State: UP
    SubState: STABLE
    Resource Group: rg_app_015
    State: Online
    ```

    画面・出力には clstat が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。CLversion 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> /usr/es/sbin/cluster/utilities/cldump
    → Enter を押す
    ```

    画面・出力:
    ```text
    Cluster prodcluster015
    Node clnode_1 State UP
    Network net_ether_01
    Resource Group rg_app_015 Online
    ```

    画面・出力には Cluster が含まれ、clmgr sync cluster 版数確認 再読込の証跡を確認できます。

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



### clmgr sync cluster 起動確認 経路確認 {#c25-i0366}
*分類: 同期処理*  ・  難易度: 上級

PowerHA SystemMirror 7.2 の 同期処理 で扱う「clmgr sync cluster 起動確認 経路確認」は、検証後に構成を同期し、クラスタスナップショットを作成する操作を起動確認の観点で確認する技術項目です。CLversion 行とclst_svcIP_055を同じ記録で見比べることで、所有ノードの誤認を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** clmgr sync cluster 起動確認 経路確認の設定や表示を読む前に役割を確認します。ノード状態 PowerHA Node State 代替経路の確認 NODE10ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は基本ソフト稼働とクラスタ稼働の混を避けるため・ノード一覧から実状態値を読むしてノード一覧を照合する。
    - B. 一次資料が示す主目的は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして資源グループを照合する。
    - C. 一次資料が示す主目的は経路確認の誤読を避けるため・経路確認で経路確認を確認するして経路確認を照合する。 ✅
    - D. 一次資料が示す主目的は遠隔ボリュームRPV経路断の見落を避けるため・変更確認操作で採取欄を棚卸するしてVG varを照合する。

    正解: **C** ／ 難易度: 上級

    **解説:** 機能経路確・起動・経路確でCの記述「検証後に構成を同期し、クラスタスナップショットを作成する」に対応する項目は起動確認 経路確認（clm・経路確・経路確）です。照合経路確・起動・経路確に関する同期処理の仕様は「検証後に構成を同期し、クラスタスナップショットを作成する操作を起動確」で、確認対象は経路確・経路確・経路確です。比較経路確・起動・経路確・経路確でA:の代替経路の確認 NODE10は「PowerHA Node Stateでノード」を述べるため、正答側の照合軸はclm・経路確・経路確です。運用経路確・clmでB:のOnline Nodeは「オンラインノードの資源グループRG現在位置と」を述べるため、正答側の照合軸は経路確・起動・経路確です。仕様経路確・起動・経路確でD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は経路確・経路確・経路確です。用語経路確・起動・経路確という用語は「検証後に構成を同期し、クラスタスナップショットを作成」を指し、照合する値と誤認リスクの組合せは起動・経路確・経路確です。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **clmgr sync cluster 起動確認 経路確認**

    - 検証目的: 同期処理のclmgr sync cluster 起動確認 経路確認について、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、同期処理の対象へ進みます。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clstat -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    clstat - Cluster Status Monitor
    Cluster: prodcluster055
    State: UP
    SubState: STABLE
    Resource Group: rg_app_055
    State: Online
    ```

    画面・出力には clstat が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。CLversion 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> /usr/es/sbin/cluster/utilities/cldump
    → Enter を押す
    ```

    画面・出力:
    ```text
    Cluster prodcluster055
    Node clnode_1 State UP
    Network net_ether_01
    Resource Group rg_app_055 Online
    ```

    画面・出力には Cluster が含まれ、clmgr sync cluster 起動確認 経路確認の証跡を確認できます。

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



### clmgr verify cluster 整合確認 装置一覧 {#c25-i0367}
*分類: 同期処理*  ・  難易度: 中級

PowerHA SystemMirror 7.2 の 同期処理 で扱う「clmgr verify cluster 整合確認 装置一覧」は、クラスタトポロジーとリソースの整合性を検査するコマンドを整合確認の観点で確認する技術項目です。CLversion 行とclst_svcIP_031を同じ記録で見比べることで、同期前構成の採用を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** clmgr verify cluster 整合確認 装置一覧の設定や表示を読む前に役割を確認します。clmgr start cluster 所有先確認 依存関係ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は依存関係の誤読を避けるため・所有先確認で依存関係を確認するして依存関係を照合する。
    - B. 一次資料が示す主目的は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するしてトポロジ要約を照合する。
    - C. 一次資料が示す主目的は装置一覧の誤読を避けるため・整合確認で装置一覧を確認するして装置一覧を照合する。 ✅
    - D. 一次資料が示す主目的は依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして獲得イベントを照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能整合確・整合・装置一でCの記述「クラスタトポロジーとリソースの整合性を検査するコマンドを」に対応する項目は整合確認 装置一覧（clm・装置一・整合確）です。照合整合確・整合・装置一に関する同期処理の仕様は「クラスタトポロジーとリソースの整合性を検査するコマンドを整合確認する」で、確認対象は装置一・整合確・装置一です。比較整合確・整合・装置一・装置一でA:の所有先確認 依存関係は「クラスタサービスを開始し、リソースグループを」を述べるため、正答側の照合軸はclm・整合確・装置一です。運用整合確・clmでB:のCluster Resourceは「クラスター資源のトポロジ要約と取得時刻を記録」を述べるため、正答側の照合軸は装置一・整合・整合確です。仕様整合確・整合・装置一でD:のAcquisitionは「獲得処理の獲得イベントと取得時刻を記録し」を述べるため、正答側の照合軸は整合確・装置一・装置一です。用語整合確・整合・装置一という用語は「クラスタトポロジーとリソースの整合性を検査するコマン」を指し、照合する値と誤認リスクの組合せは整合・装置一・装置一です。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **clmgr verify cluster 整合確認 装置一覧**

    - 検証目的: 同期処理のclmgr verify cluster 整合確認 装置一覧について、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、同期処理の対象へ進みます。
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
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。CLversion 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    PowerHA SystemMirror 7.2 操作画面
    COMMAND ===> clmgr query cluster
    → Enter を押す
    ```

    画面・出力:
    ```text
    CLUSTER_NAME="prodcluster031"
    STATE="ONLINE"
    VERSION="7.2.2.1"
    ```

    画面・出力には CLUSTER が含まれ、clmgr verify cluster 整合確認 装置一覧の証跡を確認できます。

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



### clstat -o 整合確認 サービス状態 {#c25-i0368}
*分類: 同期処理*  ・  難易度: 中級

PowerHA SystemMirror 7.2 の 同期処理 で扱う「clstat -o 整合確認 サービス状態」は、クラスタ、ノード、インターフェース、リソースグループの状態を表示する監視コマンドを整合確認の観点で確認する技術項目です。CLversion 行とcltopinfo 039を同じ記録で見比べることで、クラスタ版数混在の誤認を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting

??? question "確認問題（1問）"
    **問題.** clstat -o 整合確認 サービス状態の設定や表示を読む前に役割を確認します。トポロジー Cluster Topology 復旧後の確認 TOPO06ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはクラスタートポロジーで検証から Verification を読み・Verification とである。検証からVerificationを読ときは片系定義を全体正本とする誤認を防ぐ。
    - B. 対象資源に対する働きはclverify.logの検証報告ROHAレポートと取得時刻を記録し・検証ログの採取漏れを防ぐである。保守操作で監査欄を保存するときは検証ログの採取漏れを防ぐ。
    - C. 対象資源に対する働きはシステム管理コマンドの検証進行率と取得時刻を記録し・検証ログの採取漏れを防ぐである。保守操作で監査欄を保存するときは検証ログの採取漏れを防ぐ。
    - D. 対象資源に対する働きはクラスタ・ノード・インターフェース・リソースグループの状態を表示する監視コマンドを整合確認する。整合確認でサービス状態を確認するときはサービス状態の誤読を防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能整合確・整合・サービでDの記述「クラスタ、ノード、インターフェース」に対応する項目は整合確認 サービス状態（cls・サービ・整合確）です。照合整合確・整合・サービに関する同期処理の仕様は「クラスタ、ノード、インターフェース、リソースグループの状態を表示する」で、確認対象はサービ・整合確・サービです。比較整合確・整合・サービ・サービでA:の復旧後の確認 TOPO06は「クラスタートポロジーで検証から」を述べるため、正答側の照合軸はcls・整合確・サービです。運用整合確・clsでB:のクラスタ構成検証 clverifは「clverify.logの検証報告ROHAレ」を述べるため、正答側の照合軸はサービ・整合・整合確です。項目整合確・整合・サービでC:のCommand Statusは「システム管理コマンドの検証進行率と取得時刻を」を述べるため、正答側の照合軸はサービ・整合・サービです。用語整合確・整合・サービという用語は「クラスタ、ノード、インターフェース」を指し、照合する値と誤認リスクの組合せは整合・サービ・サービです。

    **出典:** RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278 / EN_PowerHA72_Administering / EN_PowerHA72_Commands / EN_PowerHA72_Troubleshooting


??? note "検証手順（1件）"
    **clstat -o 整合確認 サービス状態**

    - 検証目的: 同期処理のclstat -o 整合確認 サービス状態について、PowerHA SystemMirror 7.2の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: PowerHA SystemMirror 7.2の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の入力画面です。COMMAND ===> に最初の確認操作を入れ、同期処理の対象へ進みます。
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
    現在の画面はPowerHA SystemMirror 7.2の確認画面です。CLversion 行を読むため、対象名を含む操作を入力します。
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

    画面・出力には Verifying が含まれ、clstat -o 整合確認 サービス状態の証跡を確認できます。

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



### 同期処理 Cluster Synchronization ログとの照合 SYNC07 {#c25-i0369}
*分類: 同期処理*  ・  難易度: 中級

ログとの照合では 同期処理 の 未同期確認 を主操作として SYNC07 を判定します。時刻と対象識別子への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC07 に残します。ログとの照合を補助する 同期実行 では clsnapshot を補助値として SYNC07 へ保存します。主判定のログとの照合では同期処理の 未同期確認 から UNSYNCED_CHANGES を読み SYNC07 へ残します。証跡照合のログとの照合では同期処理の UNSYNCED_CHANGES と clsnapshot を SYNC07 に保存します。記録対応のログとの照合では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC07 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization ログとの照合 SYNC07について構成や状態を確認します。クラスタ構成検証 SMIT Command Status 0019ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は巡回で検証進行率を証跡に残し・SMIT Commandの検証進行率と取得時刻を記録し。
    - B. 一次資料が示す主目的は切替で移動履歴を証跡に残し・Node Listの移動履歴と取得時刻を記録し。
    - C. 一次資料が示す主目的は整合確認でサービス状態を証跡に残し・クラスタ・ノード・インターフェース・リソースグループの状態を。
    - D. 一次資料が示す主目的はログとの照合で未同期確認を証跡に残し・Cluster Synchronizで未同期確認から。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能未同期・同期元でDの記述「Cluster Synchronizで未同期確認から」に対応する項目はログとの照合 SYNC07（Clu・未同期・ログと）です。照合未同期・ログとに関する同期処理の仕様は「Cluster Synchronizで未同期確認から」で、確認対象は未同期・ログと・同期元です。比較同期処・ログとでA:のCommand Statusは「SMIT Commandの検証進行率と取得時」を述べるため、正答側の照合軸はClu・ログと・未同期です。運用ログと・CluでB:のNode Listは「Node Listの移動履歴と取得時刻を記録」を述べるため、正答側の照合軸は未同期・同期処・ログとです。項目未同期・ログとでC:の整合確認 サービス状態は「クラスタ、ノード、インターフェース」を述べるため、正答側の照合軸は同期元・同期処・未同期です。用語未同期・ログとという用語は「Cluster Synchronizで未同期確認から」を指し、照合する値と誤認リスクの組合せは同期処・未同期・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization ログとの照合 SYNC07**

    - 検証目的: 同期処理のCluster Synchronizationについて操作とログを対応し、SYNC07のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC07と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC07の未同期確認を表示します。
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

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC07の同期実行を表示します。
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

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC07の再確認を表示します。
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

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の UNSYNCED が画面・出力に表示されること
    ② ステップ2 の clsnapshot が画面・出力に表示されること
    ③ ステップ3 の false が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 代替経路の確認 SYNC10 {#c25-i0370}
*分類: 同期処理*  ・  難易度: 中級

代替経路の確認では 同期処理 の 未同期確認 を主操作として SYNC10 を判定します。主経路との役割差への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC10 に残します。代替経路の確認を補助する 同期実行 では clsnapshot を補助値として SYNC10 へ保存します。主判定の代替経路の確認では同期処理の 未同期確認 から UNSYNCED_CHANGES を読み SYNC10 へ残します。証跡照合の代替経路の確認では同期処理の UNSYNCED_CHANGES と clsnapshot を SYNC10 に保存します。記録対応の代替経路の確認では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC10 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 代替経路の確認 SYNC10に関する障害切り分けの前提を確認しています。障害調査 hacmp.out Event Summary 復旧準備 FAIL05の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はcluster historyだを避けるため・マネージャーログからクラスター管理プロセしてマネージャーを照合する。
    - B. 障害切り分けに用いる役割は自動戻し条件の誤読を避けるため・調査操作で保守欄を引き継ぎするして移動履歴を照合する。
    - C. 障害切り分けに用いる役割は未同期構成の見落としを避けるため・記録操作で証跡欄を照合するしてODM登録値を照合する。
    - D. 障害切り分けに用いる役割は同期元を誤ると古い定義を全ノードを避けるため・未同期確認からUNSYNCED_CHANして未同期確認を照合する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能未同期・同期元でDの記述「Cluster Synchronizで未同期確認から」に対応する項目は代替経路の確認 SYNC10（Clu・未同期・代替経）です。照合未同期・代替経に関する同期処理の仕様は「Cluster Synchronizで未同期確認から」で、確認対象は未同期・代替経・同期元です。比較同期処・代替経でA:の復旧準備 FAIL05は「hacmp.out Eventでマネージャー」を述べるため、正答側の照合軸はClu・代替経・未同期です。運用代替経・CluでB:のNode Listは「Node Listの移動履歴と取得時刻を記録」を述べるため、正答側の照合軸は未同期・同期処・代替経です。項目未同期・代替経でC:のCluster Topologyは「Cluster TopologyのODM登録」を述べるため、正答側の照合軸は同期元・同期処・未同期です。用語未同期・代替経という用語は「Cluster Synchronizで未同期確認から」を指し、照合する値と誤認リスクの組合せは同期処・未同期・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 代替経路の確認 SYNC10**

    - 検証目的: 同期処理のCluster Synchronizationについて代替手段の成立を確認し、SYNC10のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC10と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC10の未同期確認を表示します。
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

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC10の同期実行を表示します。
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

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC10の再確認を表示します。
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

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の UNSYNCED が画面・出力に表示されること
    ② ステップ2 の clsnapshot が画面・出力に表示されること
    ③ ステップ3 の false が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 依存関係の確認 SYNC13 {#c25-i0371}
*分類: 同期処理*  ・  難易度: 中級

依存関係の確認では 同期処理 の 未同期確認 を主操作として SYNC13 を判定します。前提資源と後続処理の順序への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC13 に残します。依存関係の確認を補助する 同期実行 では clsnapshot を補助値として SYNC13 へ保存します。主判定の依存関係の確認では同期処理の 未同期確認 から UNSYNCED_CHANGES を読み SYNC13 へ残します。証跡照合の依存関係の確認では同期処理の UNSYNCED_CHANGES と clsnapshot を SYNC13 に保存します。記録対応の依存関係の確認では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC13 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 「同期処理 Cluster Synchronization 依存関係の確認 SYNC13」を「GLVM地理的ミラー RPV Client 0009」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は主操作で出力欄を評価することでRPV通信ペを確認し・片側VGのvaryon誤操作を防ぐ。GLVM地理的ミラー RPV Client 0009固有の属性も確認対象に含める。
    - B. 仕様上の役割は未同期確認からUNSYNCED_CHANことで未同期確認を確認し・同期元を誤ると古い定義を全ノを防ぐ。 ✅
    - C. 仕様上の役割は点検操作で判定欄を記録することで失敗ラベルを確認し・依存リソース順序の見落としを防ぐ。
    - D. 仕様上の役割は停止確認で停止確認を確認することで停止確認を確認し・停止確認の誤読を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能未同期・同期元でBの記述「Cluster Synchronizで未同期確認から」に対応する項目は依存関係の確認 SYNC13（Clu・未同期・依存関）です。照合未同期・依存関に関する同期処理の仕様は「Cluster Synchronizで未同期確認から」で、確認対象は未同期・依存関・同期元です。比較同期処・依存関でA:のRPV Clientは「地理的ミラーの項目のRPV通信ペアと取得時刻」を述べるため、正答側の照合軸はClu・依存関・未同期です。項目未同期・依存関でC:のEvent Summaryは「Event Summaryの失敗ラベルと取得」を述べるため、正答側の照合軸は同期元・同期処・未同期です。仕様未同期・依存関でD:の障害切り分け 停止確認は「クラスタサービスを開始し、リソースグループを」を述べるため、正答側の照合軸は依存関・同期元・未同期です。用語未同期・依存関という用語は「Cluster Synchronizで未同期確認から」を指し、照合する値と誤認リスクの組合せは同期処・未同期・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 依存関係の確認 SYNC13**

    - 検証目的: 同期処理のCluster Synchronizationについて依存資源を点検し、SYNC13のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC13と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC13の未同期確認を表示します。
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

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC13の同期実行を表示します。
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

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC13の再確認を表示します。
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

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC13の対応を確認します。前提資源と後続処理の順序を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の UNSYNCED が画面・出力に表示されること
    ② ステップ2 の clsnapshot が画面・出力に表示されること
    ③ ステップ3 の false が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 停止前の確認 SYNC14 {#c25-i0372}
*分類: 同期処理*  ・  難易度: 中級

停止前の確認では 同期処理 の 同期実行 を主操作として SYNC14 を判定します。処理中資源と未完了要求への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC14 に残します。停止前の確認を補助する 再確認 では false を補助値として SYNC14 へ保存します。主判定の停止前の確認では同期処理の 同期実行 から clsnapshot を読み SYNC14 へ残します。証跡照合の停止前の確認では同期処理の clsnapshot と false を SYNC14 に保存します。記録対応の停止前の確認では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC14 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 停止前の確認 SYNC14の役割を調べています。障害調査 hacmp.out Event Summary 構成監査 FAIL08の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはhacmp.out Eventでマネージャーログから クラスター管理プロセス を読みである。マネージャーログからクラスター管理プときはcluster historを防ぐ。
    - B. 機能の説明としてはCluster Synchronizで同期実行から clsnapshot を読み・clsnapshot とである。同期実行からclsnapshotを読ときは同期元を誤ると古い定義を全ノを防ぐ。 ✅
    - C. 機能の説明としてはOnline NodeのRG現在位置と取得時刻を記録し・自動戻し条件の誤読を防ぐである。調査操作で保守欄を引き継ぎするときは自動戻し条件の誤読を防ぐ。リソースグループ制御 Online Node 0164固有の属性も確認対象に含める。
    - D. 機能の説明としては地理的ミラーの項目のVG vary状態と取得時刻を記録し・ミラー再同期条件の誤読を防ぐである。照合操作で確認欄を採取するときはミラー再同期条件の誤読を防ぐ。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能同期実・同期元でBの記述「Cluster Synchronizで同期実行から」に対応する項目は停止前の確認 SYNC14（Clu・同期実・停止確）です。照合同期実・停止確に関する同期処理の仕様は「Cluster Synchronizで同期実行から」で、確認対象は同期実・停止確・同期元です。比較同期処・停止確でA:の構成監査 FAIL08は「hacmp.out Eventでマネージャー」を述べるため、正答側の照合軸はClu・停止確・同期実です。項目同期実・停止確でC:のOnline Nodeは「Online NodeのRG現在位置と取得時」を述べるため、正答側の照合軸は同期元・同期処・同期実です。仕様同期実・停止確でD:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は停止確・同期元・同期実です。用語同期実・停止確という用語は「Cluster Synchronizで同期実行から」を指し、照合する値と誤認リスクの組合せは同期処・同期実・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 停止前の確認 SYNC14**

    - 検証目的: 同期処理のCluster Synchronizationについて安全な停止条件を確認し、SYNC14のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC14と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC14の同期実行を表示します。
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

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC14の再確認を表示します。
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

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC14の未同期確認を表示します。
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

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC14の対応を確認します。処理中資源と未完了要求を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の clsnapshot が画面・出力に表示されること
    ② ステップ2 の false が画面・出力に表示されること
    ③ ステップ3 の UNSYNCED が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 再始動後の確認 SYNC15 {#c25-i0373}
*分類: 同期処理*  ・  難易度: 中級

再始動後の確認では 同期処理 の 再確認 を主操作として SYNC15 を判定します。再開点と未処理データへの注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC15 に残します。再始動後の確認を補助する 未同期確認 では UNSYNCED_CHANGES を補助値として SYNC15 へ保存します。主判定の再始動後の確認では同期処理の 再確認 から false を読み SYNC15 へ残します。証跡照合の再始動後の確認では同期処理の false と UNSYNCED_CHANGES を SYNC15 に保存します。記録対応の再始動後の確認では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC15 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 再始動後の確認 SYNC15について構成や状態を確認します。リソースグループ制御 Acquisition Failure 0026ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは再確認からfalseを読むことで再確認を確認し・同期元を誤ると古い定義を全ノを防ぐ。 ✅
    - B. 対象資源に対する働きは点検操作で判定欄を記録することで獲得イベントを確認し・依存リソース順序の見落としを防ぐ。
    - C. 対象資源に対する働きは主操作で出力欄を評価することでVG varを確認し・片側VGのvaryon誤操作を防ぐ。
    - D. 対象資源に対する働きは停止確認で停止確認を確認することで停止確認を確認し・停止確認の誤読を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能再確認・同期元でAの記述「Cluster Synchronizで再確認から」に対応する項目は再始動後の確認 SYNC15（Clu・再確認・再始動）です。照合再確認・再始動に関する同期処理の仕様は「Cluster Synchronizで再確認から false」で、確認対象は再確認・再始動・同期元です。運用再始動・CluでB:のAcquisitionは「Acquisitionの獲得イベントと取得時」を述べるため、正答側の照合軸は再確認・同期処・再始動です。項目再確認・再始動でC:のMirror Poolは「地理的ミラーの項目のVG vary状態と取得」を述べるため、正答側の照合軸は同期元・同期処・再確認です。仕様再確認・再始動でD:の障害切り分け 停止確認は「クラスタサービスを開始し、リソースグループを」を述べるため、正答側の照合軸は再始動・同期元・再確認です。用語再確認・再始動という用語は「Cluster Synchronizで再確認から」を指し、照合する値と誤認リスクの組合せは同期処・再確認・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 再始動後の確認 SYNC15**

    - 検証目的: 同期処理のCluster Synchronizationについて再始動結果を検証し、SYNC15のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC15と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC15の再確認を表示します。
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

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC15の未同期確認を表示します。
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

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC15の同期実行を表示します。
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

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC15の対応を確認します。再開点と未処理データを説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の false が画面・出力に表示されること
    ② ステップ2 の UNSYNCED が画面・出力に表示されること
    ③ ステップ3 の clsnapshot が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 変更前の確認 SYNC02 {#c25-i0374}
*分類: 同期処理*  ・  難易度: 中級

変更前の確認では 同期処理 の 同期実行 を主操作として SYNC02 を判定します。変更対象と非対象の境界への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC02 に残します。変更前の確認を補助する 再確認 では false を補助値として SYNC02 へ保存します。主判定の変更前の確認では同期処理の 同期実行 から clsnapshot を読み SYNC02 へ残します。証跡照合の変更前の確認では同期処理の clsnapshot と false を SYNC02 に保存します。記録対応の変更前の確認では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC02 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 変更前の確認 SYNC02に関する障害切り分けの前提を確認しています。clstat・SNMP clinfoES Status Path 権限境界の確認の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはclstatでクラスタ表示から Cluster を読み・Cluster と clinfoES を照合する。クラスタ表示からClusterを読むときはSNMP情報の残留を実ノードを防ぐ。clstat・SNMP clinfoES Status Path固有の属性も確認対象に含める。
    - B. 機能の説明としては地理的ミラーの項目のAIXエラー識別子と取得時刻を記録し・syslogとhacmp.outの突合漏れを防ぐである。監査操作で記録欄を比較するときはsyslogとhacmp.oを防ぐ。
    - C. 機能の説明としてはノードの状態と raw_state を確認するコマンドを起動確認する。起動確認でエラー詳細を確認するときはエラー詳細の誤読を防ぐ。
    - D. 機能の説明としてはCluster Synchronizで同期実行から clsnapshot を読み・clsnapshot とである。同期実行からclsnapshotを読ときは同期元を誤ると古い定義を全ノを防ぐ。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** 機能同期実・同期元でDの記述「Cluster Synchronizで同期実行から」に対応する項目は変更前の確認 SYNC02（Clu・同期実・変更確）です。照合同期実・変更確に関する同期処理の仕様は「Cluster Synchronizで同期実行から」で、確認対象は同期実・変更確・同期元です。比較同期処・変更確でA:の権限境界の確認 CLSTAT12は「clstatでクラスタ表示から」を述べるため、正答側の照合軸はClu・変更確・同期実です。運用変更確・CluでB:のVG STATEは「地理的ミラーの項目のAIXエラー識別子と取得」を述べるため、正答側の照合軸は同期実・同期処・変更確です。項目同期実・変更確でC:の起動確認 エラー詳細は「ノードの状態と raw_state」を述べるため、正答側の照合軸は同期元・同期処・同期実です。用語同期実・変更確という用語は「Cluster Synchronizで同期実行から」を指し、照合する値と誤認リスクの組合せは同期処・同期実・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 変更前の確認 SYNC02**

    - 検証目的: 同期処理のCluster Synchronizationについて変更前の証跡を保存し、SYNC02のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC02と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC02の同期実行を表示します。
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

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC02の再確認を表示します。
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

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC02の未同期確認を表示します。
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

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の clsnapshot が画面・出力に表示されること
    ② ステップ2 の false が画面・出力に表示されること
    ③ ステップ3 の UNSYNCED が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 変更後の確認 SYNC03 {#c25-i0375}
*分類: 同期処理*  ・  難易度: 中級

変更後の確認では 同期処理 の 再確認 を主操作として SYNC03 を判定します。反映値と残存値への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC03 に残します。変更後の確認を補助する 未同期確認 では UNSYNCED_CHANGES を補助値として SYNC03 へ保存します。主判定の変更後の確認では同期処理の 再確認 から false を読み SYNC03 へ残します。証跡照合の変更後の確認では同期処理の false と UNSYNCED_CHANGES を SYNC03 に保存します。記録対応の変更後の確認では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC03 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 変更後の確認 SYNC03の設定や表示を読む前に役割を確認します。障害調査 hacmp.out Event Summary 引継ぎ記録 FAIL09ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはCluster Synchronizで再確認から false を読み・false とである。再確認からfalseを読むときは同期元を誤ると古い定義を全ノを防ぐ。 ✅
    - B. 対象資源に対する働きはhacmp.out Eventでエラー記録から IDENTIFIER を読み・IDENTIFIER とである。エラー記録からIDENTIFIERをときはcluster historを防ぐ。
    - C. 対象資源に対する働きは地理的ミラーの項目のRPV通信ペアと取得時刻を記録し・片側VGのvaryon誤操作を防ぐである。主操作で出力欄を評価するときは片側VGのvaryon誤操作を防ぐ。
    - D. 対象資源に対する働きはCluster TopologyのODM登録値と取得時刻を記録し・ノード間ODM差分の残存を防ぐである。確認操作で状態欄を整理するときはノード間ODM差分の残存を防ぐ。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能再確認・同期元でAの記述「Cluster Synchronizで再確認から」に対応する項目は変更後の確認 SYNC03（Clu・再確認・変更確）です。照合再確認・変更確に関する同期処理の仕様は「Cluster Synchronizで再確認から false」で、確認対象は再確認・変更確・同期元です。運用変更確・CluでB:の引継ぎ記録 FAIL09は「hacmp.out Eventでエラー記録か」を述べるため、正答側の照合軸は再確認・同期処・変更確です。項目再確認・変更確でC:のRPV Clientは「地理的ミラーの項目のRPV通信ペアと取得時刻」を述べるため、正答側の照合軸は同期元・同期処・再確認です。仕様再確認・変更確でD:のCluster Topologyは「Cluster TopologyのODM登録」を述べるため、正答側の照合軸は変更確・同期元・再確認です。用語再確認・変更確という用語は「Cluster Synchronizで再確認から」を指し、照合する値と誤認リスクの組合せは同期処・再確認・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 変更後の確認 SYNC03**

    - 検証目的: 同期処理のCluster Synchronizationについて変更結果を検証し、SYNC03のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC03と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC03の再確認を表示します。
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

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC03の未同期確認を表示します。
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

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC03の同期実行を表示します。
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

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の false が画面・出力に表示されること
    ② ステップ2 の UNSYNCED が画面・出力に表示されること
    ③ ステップ3 の clsnapshot が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 引継ぎ記録 SYNC09 {#c25-i0376}
*分類: 同期処理*  ・  難易度: 中級

引継ぎ記録では 同期処理 の 再確認 を主操作として SYNC09 を判定します。次担当者が追跡できる証跡への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC09 に残します。引継ぎ記録を補助する 未同期確認 では UNSYNCED_CHANGES を補助値として SYNC09 へ保存します。主判定の引継ぎ記録では同期処理の 再確認 から false を読み SYNC09 へ残します。証跡照合の引継ぎ記録では同期処理の false と UNSYNCED_CHANGES を SYNC09 に保存します。記録対応の引継ぎ記録では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC09 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 引継ぎ記録 SYNC09を保守記録に説明する必要があります。クラスタ構成検証 Cluster Topology 0043と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は警告と致命エラーの混同を避けるため・採取操作で照合欄を点検するしてODM登録値を照合する。クラスタ構成検証 Cluster Topology 0043固有の属性も確認対象に含める。
    - B. 保守作業で参照する機能は同期元を誤ると古い定義を全ノードを避けるため・再確認からfalseを読むして再確認を照合する。 ✅
    - C. 保守作業で参照する機能は片側VGのvaryon誤操作を避けるため・主操作で出力欄を評価するしてRPV通信ペを照合する。
    - D. 保守作業で参照する機能は表形式の誤読を避けるため・所有先確認で表形式を確認するして表形式を照合する。

    正解: **B** ／ 難易度: 中級

    **解説:** 機能再確認・同期元でBの記述「Cluster Synchronizで再確認から」に対応する項目は引継ぎ記録 SYNC09（Clu・再確認・同期処）です。照合再確認・同期処に関する同期処理の仕様は「Cluster Synchronizで再確認から false」で、確認対象は再確認・同期処・同期元です。比較同期処・同期処でA:のCluster Topologyは「Cluster TopologyのODM登録」を述べるため、正答側の照合軸はClu・同期処・再確認です。項目再確認・同期処でC:のRPV Clientは「地理的ミラーの項目のRPV通信ペアと取得時刻」を述べるため、正答側の照合軸は同期元・同期処・再確認です。仕様再確認・同期処でD:の所有先確認 表形式は「検証後に構成を同期し、クラスタスナップショッ」を述べるため、正答側の照合軸は同期処・同期元・再確認です。用語再確認・同期処という用語は「Cluster Synchronizで再確認から」を指し、照合する値と誤認リスクの組合せは同期処・再確認・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 引継ぎ記録 SYNC09**

    - 検証目的: 同期処理のCluster Synchronizationについて再現可能な記録を作成し、SYNC09のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC09と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC09の再確認を表示します。
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

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC09の未同期確認を表示します。
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

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC09の同期実行を表示します。
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

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の false が画面・出力に表示されること
    ② ステップ2 の UNSYNCED が画面・出力に表示されること
    ③ ステップ3 の clsnapshot が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 復旧後の確認 SYNC06 {#c25-i0377}
*分類: 同期処理*  ・  難易度: 中級

復旧後の確認では 同期処理 の 再確認 を主操作として SYNC06 を判定します。再発していないことを示す値への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC06 に残します。復旧後の確認を補助する 未同期確認 では UNSYNCED_CHANGES を補助値として SYNC06 へ保存します。主判定の復旧後の確認では同期処理の 再確認 から false を読み SYNC06 へ残します。証跡照合の復旧後の確認では同期処理の false と UNSYNCED_CHANGES を SYNC06 に保存します。記録対応の復旧後の確認では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC06 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 復旧後の確認 SYNC06の役割を調べています。障害調査 hacmp.out Event Summary 停止前の確認 FAIL14の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はcluster historyだを避けるため・マネージャーログからクラスター管理プロセしてマネージャーを照合する。
    - B. 表示や設定で扱う内容は片側VGのvaryon誤操作を避けるため・主操作で出力欄を評価するしてミラー更新状を照合する。
    - C. 表示や設定で扱う内容は同期元を誤ると古い定義を全ノードを避けるため・再確認からfalseを読むして再確認を照合する。 ✅
    - D. 表示や設定で扱う内容は検証ログの採取漏れを避けるため・保守操作で監査欄を保存するしてトポロジ要約を照合する。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能再確認・同期元でCの記述「Cluster Synchronizで再確認から」に対応する項目は復旧後の確認 SYNC06（Clu・再確認・復旧確）です。照合再確認・復旧確に関する同期処理の仕様は「Cluster Synchronizで再確認から false」で、確認対象は再確認・復旧確・同期元です。比較同期処・復旧確でA:の停止前の確認 FAIL14は「hacmp.out Eventでマネージャー」を述べるため、正答側の照合軸はClu・復旧確・再確認です。運用復旧確・CluでB:のRPV Serverは「地理的ミラーの項目のミラー更新状態と取得時刻」を述べるため、正答側の照合軸は再確認・同期処・復旧確です。仕様再確認・復旧確でD:のCluster Resourceは「Cluster Resourcesのトポロジ」を述べるため、正答側の照合軸は復旧確・同期元・再確認です。用語再確認・復旧確という用語は「Cluster Synchronizで再確認から」を指し、照合する値と誤認リスクの組合せは同期処・再確認・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 復旧後の確認 SYNC06**

    - 検証目的: 同期処理のCluster Synchronizationについて復旧後の安定性を確認し、SYNC06のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC06と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC06の再確認を表示します。
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

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC06の未同期確認を表示します。
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

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC06の同期実行を表示します。
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

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の false が画面・出力に表示されること
    ② ステップ2 の UNSYNCED が画面・出力に表示されること
    ③ ステップ3 の clsnapshot が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 復旧準備 SYNC05 {#c25-i0378}
*分類: 同期処理*  ・  難易度: 中級

復旧準備では 同期処理 の 同期実行 を主操作として SYNC05 を判定します。再開前に必要な整合性への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC05 に残します。復旧準備を補助する 再確認 では false を補助値として SYNC05 へ保存します。主判定の復旧準備では同期処理の 同期実行 から clsnapshot を読み SYNC05 へ残します。証跡照合の復旧準備では同期処理の clsnapshot と false を SYNC05 に保存します。記録対応の復旧準備では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC05 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 「同期処理 Cluster Synchronization 復旧準備 SYNC05」を「clstat・SNMP clinfoES Status Path 構成監査」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は復旧準備で同期実行を証跡に残し・Cluster Synchronizで同期実行から。 ✅
    - B. 運用時に利用する技術的役割は構成監査でSMUX接続を証跡に残し・clstatでSMUX接続から ESTABLISHED。
    - C. 運用時に利用する技術的役割は登録で優先ノード一を証跡に残し・Resource Groupの優先ノード一覧と取得時刻を記録。
    - D. 運用時に利用する技術的役割は解析でsyslogを証跡に残し・地理的ミラーの項目のsyslog記録と取得時刻を記録し。

    正解: **A** ／ 難易度: 中級

    **解説:** 機能同期実・同期元でAの記述「Cluster Synchronizで同期実行から」に対応する項目は復旧準備 SYNC05（Clu・同期実・復旧準）です。照合同期実・復旧準に関する同期処理の仕様は「Cluster Synchronizで同期実行から」で、確認対象は同期実・復旧準・同期元です。運用復旧準・CluでB:の構成監査 CLSTAT08は「clstatでSMUX接続から」を述べるため、正答側の照合軸は同期実・同期処・復旧準です。項目同期実・復旧準でC:のGroup Nameは「Resource Groupの優先ノード一覧」を述べるため、正答側の照合軸は同期元・同期処・同期実です。仕様同期実・復旧準でD:のsyslog entryは「地理的ミラーの項目のsyslog記録と取得時」を述べるため、正答側の照合軸は復旧準・同期元・同期実です。用語同期実・復旧準という用語は「Cluster Synchronizで同期実行から」を指し、照合する値と誤認リスクの組合せは同期処・同期実・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 復旧準備 SYNC05**

    - 検証目的: 同期処理のCluster Synchronizationについて復旧条件を確認し、SYNC05のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC05と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC05の同期実行を表示します。
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

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC05の再確認を表示します。
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

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC05の未同期確認を表示します。
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

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の clsnapshot が画面・出力に表示されること
    ② ステップ2 の false が画面・出力に表示されること
    ③ ステップ3 の UNSYNCED が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



### 同期処理 Cluster Synchronization 性能影響の確認 SYNC11 {#c25-i0379}
*分類: 同期処理*  ・  難易度: 中級

性能影響の確認では 同期処理 の 同期実行 を主操作として SYNC11 を判定します。処理時間と滞留箇所への注意として「同期元を誤ると古い定義を全ノードへ配布する危険があります」を SYNC11 に残します。性能影響の確認を補助する 再確認 では false を補助値として SYNC11 へ保存します。主判定の性能影響の確認では同期処理の 同期実行 から clsnapshot を読み SYNC11 へ残します。証跡照合の性能影響の確認では同期処理の clsnapshot と false を SYNC11 に保存します。記録対応の性能影響の確認では同期処理の UNSYNCED_CHANGESとVerification の証跡へ SYNC11 を結びます。

**出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278

??? question "確認問題（1問）"
    **問題.** 同期処理 Cluster Synchronization 性能影響の確認 SYNC11の設定や表示を読む前に役割を確認します。リソースグループ制御 Acquisition Failure 0026ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは依存リソース順序の見落としを避けるため・点検操作で判定欄を記録するして獲得イベントを照合する。
    - B. 状態を読み取るための働きは獲得失敗ログの未採取を避けるため・表示操作で対象欄を追跡するして失敗ラベルを照合する。
    - C. 状態を読み取るための働きは同期元を誤ると古い定義を全ノードを避けるため・同期実行からclsnapshotを読むして同期実行を照合する。 ✅
    - D. 状態を読み取るための働きは識別値の誤読を避けるため・同期処理で識別値を確認するして識別値を照合する。clRGinfo 障害切り分け 識別値固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** 機能同期実・同期元でCの記述「Cluster Synchronizで同期実行から」に対応する項目は性能影響の確認 SYNC11（Clu・同期実・性能影）です。照合同期実・性能影に関する同期処理の仕様は「Cluster Synchronizで同期実行から」で、確認対象は同期実・性能影・同期元です。比較同期処・性能影でA:のAcquisitionは「Acquisitionの獲得イベントと取得時」を述べるため、正答側の照合軸はClu・性能影・同期実です。運用性能影・CluでB:のEvent Summaryは「Event Summaryの失敗ラベルと取得」を述べるため、正答側の照合軸は同期実・同期処・性能影です。仕様同期実・性能影でD:の障害切り分け 識別値は「リソースグループの状態と所有ノードを表示する」を述べるため、正答側の照合軸は性能影・同期元・同期実です。用語同期実・性能影という用語は「Cluster Synchronizで同期実行から」を指し、照合する値と誤認リスクの組合せは同期処・同期実・同期元です。

    **出典:** EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278


??? note "検証手順（1件）"
    **同期処理 Cluster Synchronization 性能影響の確認 SYNC11**

    - 検証目的: 同期処理のCluster Synchronizationについて負荷と待ちを確認し、SYNC11のUNSYNCED_CHANGESとVerificationを実出力で確認する。
    - 前提条件: PowerHA SystemMirror 7.2の参照権限を持ち、対象SYNC11と実行時刻を記録できること。変更操作は実施せず机上で確認する。
    - セッション環境: PowerHA SystemMirror 7.2の運用画面またはコマンド入力画面

    **ステップ 1**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr sync clusterを指定し、SYNC11の同期実行を表示します。
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

    画面・出力にあるclsnapshotを読み、UNSYNCED_CHANGESとVerificationと対象SYNC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 2**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC11の再確認を表示します。
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

    画面・出力にあるfalseを読み、UNSYNCED_CHANGESとVerificationと対象SYNC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    **ステップ 3**
    現在の画面はPowerHA SystemMirror 7.2の同期処理を確認する入力画面です。COMMAND入力口へclmgr -a UNSYNCED_CHANGES query clusterを指定し、SYNC11の未同期確認を表示します。
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

    画面・出力にあるUNSYNCEDを読み、UNSYNCED_CHANGESとVerificationと対象SYNC11の対応を確認します。処理時間と滞留箇所を説明できるよう時刻も残します。

    - 合格条件: ① ステップ1 の clsnapshot が画面・出力に表示されること
    ② ステップ2 の false が画面・出力に表示されること
    ③ ステップ3 の UNSYNCED が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: EN_PowerHA72_Administering / EN_PowerHA72_Concepts / EN_PowerHA72_Troubleshooting / RB_PowerHA72_Cookbook_SG247739 / RB_PowerHA72_Updates_SG248278



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


