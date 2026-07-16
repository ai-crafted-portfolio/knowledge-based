---
search:
  exclude: true
---

# AIX 7.3 — 詳細 (9/10)

[← AIX 7.3 の概要へ戻る](index.md)


## AIX 7.3 > 導入と起動

### oslevel -s 変更前確認 fileset level 0110 {#c01-i0786}
*分類: 導入と起動*  ・  難易度: 上級

早苗点検ではAIX 7.3の導入と起動で oslevel -s を確認します。早苗点検の導入と起動では fileset level とOSレベル表示を確認票へ整理します。早苗点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。早苗点検の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、早苗点検を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 変更前確認 fileset level 0110に関する障害切り分けの前提を確認しています。ifconfig en0 変更後確認 MTU 0111の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はネットワークでifconfig en0を用い・MTU とEthernet統計を確認する。
    - B. 障害切り分けに用いる役割は導入と起動でoslevel -sを用い・fileset level とOSレベル表示を確認する。 ✅
    - C. 障害切り分けに用いる役割はデバイス管理でlsmpio -l hdisk0を用い・location codeである。
    - D. 障害切り分けに用いる役割はネットワークでcfgmgrを用い・MTU とEthernet統計を確認する。cfgmgr 性能確認 MTU 0723固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「導入と起動でoslevel -sを用い、fileset level」に対応する項目はfileset level（変更・osle）です。変更前に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、fileset level」で、確認対象はos・変更前です。変更後・ifcoのA:は「ネットワークでifconfig en0を用い、MTU」を述べ、対象は変更後確認 MTU（変更・ifco）です。属性・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はlocation code（属性・lsmp）です。性能・cfgmのD:は「ネットワークでcfgmgrを用い、MTU」を述べ、対象は性能確認 MTU（性能・cfgm）です。「oslevel -s」は「導入と起動でoslevel -sを用い、fileset level」を指し、fileset levelではos・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 変更前確認 fileset level 0110**

    - 検証目的: 導入と起動のoslevel -s 変更前確認 fileset level 0110について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認110-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0110A
    ```

    画面・出力には AIX0110A が表示され、oslevel -s 変更前確認 fileset level 0110 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0110B
    ```

    画面・出力には AIX0110B が表示され、oslevel -s 変更前確認 fileset level 0110 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0110C
    ```

    画面・出力には AIX0110C が表示され、oslevel -s 変更前確認 fileset level 0110 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0110A が画面・出力に表示されること
    ② ステップ2 の AIX0110B が画面・出力に表示されること
    ③ ステップ3 の AIX0110C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 容量確認 Technology Level 0556 {#c01-i0787}
*分類: 導入と起動*  ・  難易度: 中級

若潮照合ではAIX 7.3の導入と起動で oslevel -s を確認します。若潮照合の導入と起動では Technology Level と代替ディスク状態を監査票へ転記します。若潮照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若潮照合の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、若潮照合を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 容量確認 Technology Level 0556の技術的な意味を資料で確認するとき、ifconfig en0 性能確認 Media Speed Running 0557との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はネットワークでifconfig en0を用い・Media Speed Running とMTU属性を確認する。
    - B. 管理対象との関係を表す説明はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。
    - C. 管理対象との関係を表す説明は導入と起動でoslevel -sを用い・Technology Level と代替ディスク状態を確認する。 ✅
    - D. 管理対象との関係を表す説明はセキュリティでlsroleを用い・roles と監査設定を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でoslevel -sを用い、Technology Level」に対応する項目はTechnology Level（容量・osle）です。容量に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、Technology」で、確認対象はos・容量です。性能・ifcoのA:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（性能・ifco）です。復旧前・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は復旧前確認 再開位置（復旧・lsvg）です。属性・lsroのD:は「セキュリティでlsroleを用い、roles と監査設定を確認する」を述べ、対象は属性確認 roles（属性・lsro）です。「oslevel -s」は「導入と起動でoslevel -sを用い、Technology」を指し、Technology Levelではos・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 容量確認 Technology Level 0556**

    - 検証目的: 導入と起動のoslevel -s 容量確認 Technology Level 0556について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認076-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0556A
    ```

    画面・出力には AIX0556A が表示され、oslevel -s 容量確認 Technology Level 0556 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0556B
    ```

    画面・出力には AIX0556B が表示され、oslevel -s 容量確認 Technology Level 0556 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0556C
    ```

    画面・出力には AIX0556C が表示され、oslevel -s 容量確認 Technology Level 0556 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0556A が画面・出力に表示されること
    ② ステップ2 の AIX0556B が画面・出力に表示されること
    ③ ステップ3 の AIX0556C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 容量確認 altinst_rootvg 0080 {#c01-i0788}
*分類: 導入と起動*  ・  難易度: 中級

青葉点検ではAIX 7.3の導入と起動で oslevel -s を確認します。青葉点検の導入と起動では altinst_rootvg と代替ディスク状態を引継ぎ票へ保管します。青葉点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。青葉点検の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、青葉点検を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 容量確認 altinst_rootvg 0080を同一分類のifconfig en0 性能確認 EtherChannel 0081と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はネットワークでifconfig en0を用い・EtherChannel とMTU属性を確認する。
    - B. コマンドまたは機能の用途はデバイス管理でlsmpio -l hdisk0を用い・path status とデバイス一覧を確認する。
    - C. コマンドまたは機能の用途はネットワークでroute -n getを用い・Gateway とMTU属性を確認する。
    - D. コマンドまたは機能の用途は導入と起動でoslevel -sを用い・altinst_rootvg と代替ディスク状態を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「導入と起動でoslevel -sを用い、altinst_rootvg」に対応する項目は容量確認 altinst_rootv（容量・osle）です。容量に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、altinst_rootvg」で、確認対象はos・容量です。性能・ifcoのA:は「ネットワークでifconfig en0を用い」を述べ、対象は性能確認 EtherChannel（性能・ifco）です。バック・lsmpのB:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（バッ・lsmp）です。変更前・routのC:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は変更前確認 Gateway（変更・rout）です。「oslevel -s」は「導入と起動でoslevel -sを用い、altinst_rootvg」を指し、容量確認 altinst_rootvではos・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 容量確認 altinst_rootvg 0080**

    - 検証目的: 導入と起動のoslevel -s 容量確認 altinst_rootvg 0080について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認080-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0080A
    ```

    画面・出力には AIX0080A が表示され、oslevel -s 容量確認 altinst_rootvg 0080 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0080B
    ```

    画面・出力には AIX0080B が表示され、oslevel -s 容量確認 altinst_rootvg 0080 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lslpp -L bos.rte
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0080C
    ```

    画面・出力には AIX0080C が表示され、oslevel -s 容量確認 altinst_rootvg 0080 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0080A が画面・出力に表示されること
    ② ステップ2 の AIX0080B が画面・出力に表示されること
    ③ ステップ3 の AIX0080C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 起動確認 fileset level 0367 {#c01-i0789}
*分類: 導入と起動*  ・  難易度: 初級

夕凪記録ではAIX 7.3の導入と起動で oslevel -s を確認します。夕凪記録の導入と起動では fileset level とfileset一覧を点検票へ整理します。夕凪記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。夕凪記録の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、夕凪記録を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 起動確認 fileset level 0367の設定や表示を読む前に役割を確認します。ifconfig en0 属性確認 Media Speed Running 0368ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはネットワークでifconfig en0を用い・Media Speed Running と経路表を確認する。
    - B. 対象資源に対する働きはデバイス管理でbootinfo -B hdisk0を用い・Available と診断対象表示を確認する。
    - C. 対象資源に対する働きは導入と起動でoslevel -sを用い・fileset level とfileset一覧を確認する。 ✅
    - D. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「導入と起動でoslevel -sを用い、fileset level」に対応する項目はfileset level（起動・osle）です。起動に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、fileset level」で、確認対象はos・起動です。属性・ifcoのA:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（属性・ifco）です。監査・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は監査記録 Available（監査・boot）です。状態・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsat）です。「oslevel -s」は「導入と起動でoslevel -sを用い、fileset level」を指し、fileset levelではos・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 起動確認 fileset level 0367**

    - 検証目的: 導入と起動のoslevel -s 起動確認 fileset level 0367について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認007-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0367A
    ```

    画面・出力には AIX0367A が表示され、oslevel -s 起動確認 fileset level 0367 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0367B
    ```

    画面・出力には AIX0367B が表示され、oslevel -s 起動確認 fileset level 0367 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0367C
    ```

    画面・出力には AIX0367C が表示され、oslevel -s 起動確認 fileset level 0367 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0367A が画面・出力に表示されること
    ② ステップ2 の AIX0367B が画面・出力に表示されること
    ③ ステップ3 の AIX0367C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 起動確認 fileset level 0427 {#c01-i0790}
*分類: 導入と起動*  ・  難易度: 中級

風花評価ではAIX 7.3の導入と起動で oslevel -s を確認します。風花評価の導入と起動では fileset level とfileset一覧を点検票へ整理します。風花評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。風花評価の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、風花評価を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 起動確認 fileset level 0427について構成や状態を確認します。ifconfig en0 属性確認 Media Speed Running 0428ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはネットワークでifconfig en0を用い・Media Speed Running と経路表を確認する。
    - B. 対象資源に対する働きは導入と起動でoslevel -sを用い・fileset level とfileset一覧を確認する。 ✅
    - C. 対象資源に対する働きはデバイス管理でlsmpio -l hdisk0を用い・location code と診断対象表示を確認する。
    - D. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「導入と起動でoslevel -sを用い、fileset level」に対応する項目はfileset level（起動・osle）です。起動に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、fileset level」で、確認対象はos・起動です。属性・ifcoのA:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（属性・ifco）です。運用引・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はlocation code（運用・lsmp）です。状態・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsat）です。「oslevel -s」は「導入と起動でoslevel -sを用い、fileset level」を指し、fileset levelではos・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 起動確認 fileset level 0427**

    - 検証目的: 導入と起動のoslevel -s 起動確認 fileset level 0427について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認067-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0427A
    ```

    画面・出力には AIX0427A が表示され、oslevel -s 起動確認 fileset level 0427 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0427B
    ```

    画面・出力には AIX0427B が表示され、oslevel -s 起動確認 fileset level 0427 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0427C
    ```

    画面・出力には AIX0427C が表示され、oslevel -s 起動確認 fileset level 0427 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0427A が画面・出力に表示されること
    ② ステップ2 の AIX0427B が画面・出力に表示されること
    ③ ステップ3 の AIX0427C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### oslevel -s 障害切り分け altinst_rootvg 0397 {#c01-i0791}
*分類: 導入と起動*  ・  難易度: 中級

冬晴記録ではAIX 7.3の導入と起動で oslevel -s を確認します。冬晴記録の導入と起動では altinst_rootvg と起動デバイス設定を採取票へ記録します。冬晴記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。冬晴記録の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、冬晴記録を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** oslevel -s 障害切り分け altinst_rootvg 0397を保守記録に説明する必要があります。ifconfig en0 バックアウト確認 Gateway 0398と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はネットワークでifconfig en0を用い・Gateway とアダプター一覧を確認する。ifconfig en0 バックアウト確認 Gateway 0398固有の属性も確認対象に含める。
    - B. 保守作業で参照する機能はデバイス管理でbootinfo -B hdisk0を用い・PVID とODM属性を確認する。
    - C. 保守作業で参照する機能は導入と起動でoslevel -sを用い・altinst_rootvg と起動デバイス設定を確認する。 ✅
    - D. 保守作業で参照する機能はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「導入と起動でoslevel -sを用い、altinst_rootvg」に対応する項目は障害切り分け altinst_roo（障害・osle）です。障害切に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、altinst_rootvg」で、確認対象はos・障害切です。バック・ifcoのA:は「ネットワークでifconfig en0を用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・ifco）です。状態・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・boot）です。監査・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsat）です。「oslevel -s」は「導入と起動でoslevel -sを用い、altinst_rootvg」を指し、障害切り分け altinst_rooではos・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **oslevel -s 障害切り分け altinst_rootvg 0397**

    - 検証目的: 導入と起動のoslevel -s 障害切り分け altinst_rootvg 0397について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け037-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    7300-02-01-2346
    確認コード AIX0397A
    ```

    画面・出力には AIX0397A が表示され、oslevel -s 障害切り分け altinst_rootvg 0397 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> bootlist -m normal -o
    → Enter を押す
    ```

    画面・出力:
    ```text
    Fileset                      Level  State  Description
    bos.rte                   7.3.2.1    C     Base Operating System Runtime
    確認コード AIX0397B
    ```

    画面・出力には AIX0397B が表示され、oslevel -s 障害切り分け altinst_rootvg 0397 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> oslevel -s
    → Enter を押す
    ```

    画面・出力:
    ```text
    Boot device list
    hdisk0 blv=hd5 pathid=0
    hdisk1 blv=hd5 pathid=1
    確認コード AIX0397C
    ```

    画面・出力には AIX0397C が表示され、oslevel -s 障害切り分け altinst_rootvg 0397 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0397A が画面・出力に表示されること
    ② ステップ2 の AIX0397B が画面・出力に表示されること
    ③ ステップ3 の AIX0397C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en




## AIX 7.3 > 性能監視

### chdev 変更前確認 識別値 {#c01-i0792}
*分類: 性能監視*  ・  難易度: 初級

AIX 7.3 の 性能監視 で扱う「chdev 変更前確認 識別値」は、デバイス属性を変更する管理コマンドを変更前確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-007を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** chdev 変更前確認 識別値の設定や表示を読む前に役割を確認します。lscfg 復旧前確認 障害記録ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は構成済みデバイスと VPD を表示するコマンドである。
    - B. 一次資料が示す主目的は性能管理でtopas -Dを用い・fre とAME統計を確認する。
    - C. 一次資料が示す主目的はSRCとログでsyslog_ssw -rを用い・TIMESTAMP とsyslog設定変換を確認する。
    - D. 一次資料が示す主目的はデバイス属性を変更する管理コマンドである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「デバイス属性を変更する管理コマンドである」に対応する項目は変更前確認 識別値（変更・chde）です。性能監視の仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・変更前です。復旧前・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は復旧前確認 障害記録（復旧・lscf）です。監査・topaのB:は「性能管理でtopas -Dを用い、fre とAME統計を確認する」を述べ、対象は監査記録 fre（監査・topa）です。障害切・syslのC:は「SRCとログでsyslog_ssw -rを用い、TIMESTAMP」を述べ、対象は障害切り分け TIMESTAMP（障害・sysl）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、変更前確認 識別値ではch・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **chdev 変更前確認 識別値**

    - 検証目的: 性能監視のchdev 変更前確認 識別値について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lslv hd4
    → Enter を押す
    ```

    画面・出力:
    ```text
    LOGICAL VOLUME: hd4
    VOLUME GROUP: rootvg
    LV STATE: opened/syncd
    TYPE: jfs2
    ```

    画面・出力には LOGICAL が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsps -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
    hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
    ```

    画面・出力には Page が含まれ、chdev 変更前確認 識別値の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、停止中の論理ボリューム見落としを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> smit lsps
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMIT fast path: lsps
    Command to run: lsps -a
    Paging space list displayed
    ```

    画面・出力には SMIT が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の LOGICAL が画面・出力に表示されること
    ② ステップ2 の Page が画面・出力に表示されること
    ③ ステップ3 の SMIT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### chdev 状態判定 対象ノード {#c01-i0793}
*分類: 性能監視*  ・  難易度: 中級

AIX 7.3 の 性能監視 で扱う「chdev 状態判定 対象ノード」は、デバイス属性を変更する管理コマンドを状態判定の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-047を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** chdev 状態判定 対象ノードの設定や表示を読む前に役割を確認します。lscfg 属性照合 時刻情報ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはデバイス属性を変更する管理コマンドである。 ✅
    - B. 状態を読み取るための働きは構成済みデバイスと VPD を表示するコマンドである。
    - C. 状態を読み取るための働きはLVMでchlvを用い・VG STATE とミラーコピー状態を確認する。
    - D. 状態を読み取るための働きは性能管理でtopas -Dを用い・Busy% とtopasディスク表示を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「デバイス属性を変更する管理コマンドである」に対応する項目は状態判定 対象ノード（状態・chde）です。性能監視の仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・状態・対象です。属性・時刻・lscfのB:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は属性照合 時刻情報（属性・lscf）です。属性・chlvのC:は「LVMでchlvを用い、VG STATE」を述べ、対象はVG STATE（属性・chlv）です。容量・topaのD:は「性能管理でtopas -Dを用い、Busy%」を述べ、対象は容量確認 Busy%（容量・topa）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、状態判定 対象ノードではch・状態・対象に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **chdev 状態判定 対象ノード**

    - 検証目的: 性能監視のchdev 状態判定 対象ノードについて、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lslv hd4
    → Enter を押す
    ```

    画面・出力:
    ```text
    LOGICAL VOLUME: hd4
    VOLUME GROUP: rootvg
    LV STATE: opened/syncd
    TYPE: jfs2
    ```

    画面・出力には LOGICAL が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsps -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
    hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
    ```

    画面・出力には Page が含まれ、chdev 状態判定 対象ノードの証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、停止中の論理ボリューム見落としを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> smit lsps
    → Enter を押す
    ```

    画面・出力:
    ```text
    SMIT fast path: lsps
    Command to run: lsps -a
    Paging space list displayed
    ```

    画面・出力には SMIT が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の LOGICAL が画面・出力に表示されること
    ② ステップ2 の Page が画面・出力に表示されること
    ③ ステップ3 の SMIT が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### errpt 属性照合 ログ採取 {#c01-i0794}
*分類: 性能監視*  ・  難易度: 中級

AIX 7.3 の 性能監視 で扱う「errpt 属性照合 ログ採取」は、AIX エラーログから要約または詳細レポートを生成するコマンドを属性照合の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-055を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** errpt 属性照合 ログ採取の設定や表示を読む前に役割を確認します。lsattr 障害切り分け 実行結果ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はデバイスや sys0 などの属性値を表示するコマンドである。
    - B. 一次資料が示す主目的はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。
    - C. 一次資料が示す主目的は性能管理でsvmon -Gを用い・fre とtopasディスク表示を確認する。
    - D. 一次資料が示す主目的はAIX エラーログから要約または詳細レポートを生成するコマンドである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は属性照合 ログ採取（属性・errp）です。性能監視の仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・属性・ログです。障害切・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は障害切り分け 実行結果（障害・lsat）です。運用引・lslvのB:は「LVMでlslvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・lslv）です。障害切・svmoのC:は「性能管理でsvmon -Gを用い、fre」を述べ、対象は障害切り分け fre（障害・svmo）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、属性照合 ログ採取ではer・属性・ログに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **errpt 属性照合 ログ採取**

    - 検証目的: 性能監視のerrpt 属性照合 ログ採取について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    System configuration: lcpu=2 mem=1024MB tmem=512MB ent=0.40 mmode=dedicated-E
     r b avm fre csz cfr dxm ci co pi po in sy cs
    ```

    画面・出力には System が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lparstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
    %user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
    ```

    画面・出力には System が含まれ、errpt 属性照合 ログ採取の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ボリュームグループの取り違えを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> topas
    → Enter を押す
    ```

    画面・出力:
    ```text
    Topas Monitor for host: aixhost
    CPU User% Kern% Wait% Idle%
    AME TMEM,MB 512 CMEM,MB 114 EF[T/A] 2.0/1.5
    ```

    画面・出力には Topas が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の System が画面・出力に表示されること
    ② ステップ2 の System が画面・出力に表示されること
    ③ ステップ3 の Topas が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### errpt 復旧前確認 再読込 {#c01-i0795}
*分類: 性能監視*  ・  難易度: 初級

AIX 7.3 の 性能監視 で扱う「errpt 復旧前確認 再読込」は、AIX エラーログから要約または詳細レポートを生成するコマンドを復旧前確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-015を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** errpt 復旧前確認 再読込の設定や表示を読む前に役割を確認します。lsattr 一覧確認 対象ファイルではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはデバイスや sys0 などの属性値を表示するコマンドである。
    - B. 対象資源に対する働きはセキュリティでrbacqry -u user1 -Tを用い・audit class と監査設定を確認する。
    - C. 対象資源に対する働きは導入と起動でinstallp -Cを用い・EFIX LABEL と代替ディスク状態を確認する。
    - D. 対象資源に対する働きはAIX エラーログから要約または詳細レポートを生成するコマンドである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は復旧前確認 再読込（復旧・errp）です。性能監視の仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・復旧前です。一覧・対象・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は一覧確認 対象ファイル（一覧・lsat）です。変更後・rbacのB:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（変更・rbac）です。状態・instのC:は「導入と起動でinstallp -Cを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（状態・inst）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、復旧前確認 再読込ではer・復旧前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **errpt 復旧前確認 再読込**

    - 検証目的: 性能監視のerrpt 復旧前確認 再読込について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    System configuration: lcpu=2 mem=1024MB tmem=512MB ent=0.40 mmode=dedicated-E
     r b avm fre csz cfr dxm ci co pi po in sy cs
    ```

    画面・出力には System が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lparstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
    %user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
    ```

    画面・出力には System が含まれ、errpt 復旧前確認 再読込の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ボリュームグループの取り違えを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> topas
    → Enter を押す
    ```

    画面・出力:
    ```text
    Topas Monitor for host: aixhost
    CPU User% Kern% Wait% Idle%
    AME TMEM,MB 512 CMEM,MB 114 EF[T/A] 2.0/1.5
    ```

    画面・出力には Topas が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の System が画面・出力に表示されること
    ② ステップ2 の System が画面・出力に表示されること
    ③ ステップ3 の Topas が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### lslv 一覧確認 サンプル採取 {#c01-i0796}
*分類: 性能監視*  ・  難易度: 中級

AIX 7.3 の 性能監視 で扱う「lslv 一覧確認 サンプル採取」は、論理ボリュームの属性と割り当て情報を表示するコマンドを一覧確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-023を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lslv 一覧確認 サンプル採取の設定や表示を読む前に役割を確認します。lsps 詳細確認 メッセージ行ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。
    - B. 状態を読み取るための働きは論理ボリュームの属性と割り当て情報を表示するコマンドである。 ✅
    - C. 状態を読み取るための働きはセキュリティでlsroleを用い・roles と監査設定を確認する。
    - D. 状態を読み取るための働きは導入と起動でoslevel -sを用い・Technology Level と代替ディスク状態を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は一覧確認 サンプル採取（一覧・lslv）です。性能監視の仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・一覧・サンです。詳細・メッ・lspsのA:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は詳細確認 メッセージ行（詳細・lsps）です。属性・lsroのC:は「セキュリティでlsroleを用い、roles と監査設定を確認する」を述べ、対象は属性確認 roles（属性・lsro）です。容量・osleのD:は「導入と起動でoslevel -sを用い、Technology」を述べ、対象はTechnology Level（容量・osle）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、一覧確認 サンプル採取ではls・一覧・サンに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lslv 一覧確認 サンプル採取**

    - 検証目的: 性能監視のlslv 一覧確認 サンプル採取について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> errpt
    → Enter を押す
    ```

    画面・出力:
    ```text
    ERROR_IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  ERROR_DESCRIPTION
    0E017ED1         0405131090 P H mem2           Memory failure
    ```

    画面・出力には ERROR が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> errpt -a -N hdisk1
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: DISK_ERR4
    RESOURCE NAME: hdisk1
    Description
    DISK OPERATION ERROR
    ```

    画面・出力には LABEL が含まれ、lslv 一覧確認 サンプル採取の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ページング使用率の見落としを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> /usr/lib/errdemon -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    /var/adm/ras/errlog
    ```

    画面・出力には errlog が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ERROR が画面・出力に表示されること
    ② ステップ2 の LABEL が画面・出力に表示されること
    ③ ステップ3 の errlog が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### lslv 障害切り分け 起動確認 {#c01-i0797}
*分類: 性能監視*  ・  難易度: 中級

AIX 7.3 の 性能監視 で扱う「lslv 障害切り分け 起動確認」は、論理ボリュームの属性と割り当て情報を表示するコマンドを障害切り分けの観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-063を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lslv 障害切り分け 起動確認の設定や表示を読む前に役割を確認します。lsps 性能確認 停止確認ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。
    - B. 対象資源に対する働きはLVMでlsvgを用い・PP SIZE とミラーコピー状態を確認する。
    - C. 対象資源に対する働きは論理ボリュームの属性と割り当て情報を表示するコマンドである。 ✅
    - D. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・roles とユーザー属性を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は障害切り分け 起動確認（障害・lslv）です。性能監視の仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・障害切です。性能・停止・lspsのA:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は性能確認 停止確認（性能・lsps）です。変更後・lsvgのB:は「LVMでlsvgを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（変更・lsvg）です。状態・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 roles（状態・lsat）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、障害切り分け 起動確認ではls・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lslv 障害切り分け 起動確認**

    - 検証目的: 性能監視のlslv 障害切り分け 起動確認について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> errpt
    → Enter を押す
    ```

    画面・出力:
    ```text
    ERROR_IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  ERROR_DESCRIPTION
    0E017ED1         0405131090 P H mem2           Memory failure
    ```

    画面・出力には ERROR が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> errpt -a -N hdisk1
    → Enter を押す
    ```

    画面・出力:
    ```text
    LABEL: DISK_ERR4
    RESOURCE NAME: hdisk1
    Description
    DISK OPERATION ERROR
    ```

    画面・出力には LABEL が含まれ、lslv 障害切り分け 起動確認の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ページング使用率の見落としを切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> /usr/lib/errdemon -l
    → Enter を押す
    ```

    画面・出力:
    ```text
    /var/adm/ras/errlog
    ```

    画面・出力には errlog が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の ERROR が画面・出力に表示されること
    ② ステップ2 の LABEL が画面・出力に表示されること
    ③ ステップ3 の errlog が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### lspv 性能確認 保持設定 {#c01-i0798}
*分類: 性能監視*  ・  難易度: 上級

AIX 7.3 の 性能監視 で扱う「lspv 性能確認 保持設定」は、物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドを性能確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-071を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lspv 性能確認 保持設定の設定や表示を読む前に役割を確認します。lsvg 変更前確認 再開位置ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。
    - B. 状態を読み取るための働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 ✅
    - C. 状態を読み取るための働きはJFS2でdefragfsを用い・agblksize とマウントオプションを確認する。
    - D. 状態を読み取るための働きはセキュリティでusrck -n ALLを用い・roles とユーザー属性を確認する。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は性能確認 保持設定（性能・lspv）です。性能監視の仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・性能・保持です。変更前・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は変更前確認 再開位置（変更・lsvg）です。属性・defrのC:は「JFS2でdefragfsを用い、agblksize」を述べ、対象は属性確認 agblksize（属性・defr）です。性能・usrcのD:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は性能確認 roles（性能・usrc）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、性能確認 保持設定ではls・性能・保持に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lspv 性能確認 保持設定**

    - 検証目的: 性能監視のlspv 性能確認 保持設定について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lspv
    → Enter を押す
    ```

    画面・出力:
    ```text
    hdisk0          00f6a1b2c3d4e71        rootvg          active
    hdisk1          00f6a1b2c3d5e71        datavg          active
    ```

    画面・出力には hdisk0 が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsvg rootvg
    → Enter を押す
    ```

    画面・出力:
    ```text
    VOLUME GROUP: rootvg
    VG STATE: active
    PP SIZE: 128 megabyte(s)
    TOTAL PPs: 1092
    ```

    画面・出力には VOLUME が含まれ、lspv 性能確認 保持設定の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、PVID の誤読を切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsvg -l rootvg
    → Enter を押す
    ```

    画面・出力:
    ```text
    LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
    hd4                 jfs2       1     1     open/syncd    /
    ```

    画面・出力には NAME が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の hdisk0 が画面・出力に表示されること
    ② ステップ2 の VOLUME が画面・出力に表示されること
    ③ ステップ3 の NAME が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### lspv 詳細確認 装置一覧 {#c01-i0799}
*分類: 性能監視*  ・  難易度: 中級

AIX 7.3 の 性能監視 で扱う「lspv 詳細確認 装置一覧」は、物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドを詳細確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-031を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lspv 詳細確認 装置一覧の設定や表示を読む前に役割を確認します。lsvg 状態判定 製品レベルではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。
    - B. 一次資料が示す主目的は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 ✅
    - C. 一次資料が示す主目的はデバイス管理でlsmpio -l hdisk0を用い・microcode levelである。
    - D. 一次資料が示す主目的はネットワークでroute -n getを用い・Gateway と経路表を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は詳細確認 装置一覧（詳細・lspv）です。性能監視の仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・詳細・装置です。状態・製品・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は状態判定 製品レベル（状態・lsvg）です。運用引・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はmicrocode level（運用・lsmp）です。障害切・routのD:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・rout）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、詳細確認 装置一覧ではls・詳細・装置に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lspv 詳細確認 装置一覧**

    - 検証目的: 性能監視のlspv 詳細確認 装置一覧について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lspv
    → Enter を押す
    ```

    画面・出力:
    ```text
    hdisk0          00f6a1b2c3d4e31        rootvg          active
    hdisk1          00f6a1b2c3d5e31        datavg          active
    ```

    画面・出力には hdisk0 が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsvg rootvg
    → Enter を押す
    ```

    画面・出力:
    ```text
    VOLUME GROUP: rootvg
    VG STATE: active
    PP SIZE: 128 megabyte(s)
    TOTAL PPs: 1092
    ```

    画面・出力には VOLUME が含まれ、lspv 詳細確認 装置一覧の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、PVID の誤読を切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsvg -l rootvg
    → Enter を押す
    ```

    画面・出力:
    ```text
    LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
    hd4                 jfs2       1     1     open/syncd    /
    ```

    画面・出力には NAME が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の hdisk0 が画面・出力に表示されること
    ② ステップ2 の VOLUME が画面・出力に表示されること
    ③ ステップ3 の NAME が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### vmstat 性能確認 性能値 {#c01-i0800}
*分類: 性能監視*  ・  難易度: 上級

AIX 7.3 の 性能監視 で扱う「vmstat 性能確認 性能値」は、CPU、メモリー、ページング、AME 統計を表示する性能コマンドを性能確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-079を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** vmstat 性能確認 性能値の設定や表示を読む前に役割を確認します。lparstat 変更前確認 キュー状態ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。
    - B. 一次資料が示す主目的はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。 ✅
    - C. 一次資料が示す主目的はJFS2でsplitcopyを用い・ファイルシステム使用率 とマウントオプションを確認する。
    - D. 一次資料が示す主目的はセキュリティでlsuserを用い・authorizations とユーザー属性を確認する。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「CPU、メモリー、ページング、AME 統計を表示する性能コマンドである」に対応する項目は性能確認 性能値（性能・vmst）です。性能監視の仕様は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」で、確認対象はvm・性能・性能です。変更前・lparのA:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は変更前確認 キュー状態（変更・lpar）です。運用引・spliのC:は「JFS2でsplitcopyを用い、ファイルシステム使用率」を述べ、対象は運用引継ぎ ファイルシステム使用率（運用・spli）です。バック・lsusのD:は「セキュリティでlsuserを用い、authorizations」を述べ、対象はバックアウト確認 authoriza（バッ・lsus）です。「vmstat」は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を指し、性能確認 性能値ではvm・性能・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **vmstat 性能確認 性能値**

    - 検証目的: 性能監視のvmstat 性能確認 性能値について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsattr -E -l sys0 -a iostat
    → Enter を押す
    ```

    画面・出力:
    ```text
    iostat true Continuously maintain disk I/O history True
    ```

    画面・出力には iostat が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> chdev -l sys0 -a iostat=true
    → Enter を押す
    ```

    画面・出力:
    ```text
    sys0 changed
    ```

    画面・出力には sys0 が含まれ、vmstat 性能確認 性能値の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、資源名の誤指定を切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lscfg -l sysplanar0
    → Enter を押す
    ```

    画面・出力:
    ```text
    DEVICE          LOCATION     DESCRIPTION
    sysplanar0      00-00        CPU Planar
    ```

    画面・出力には DEVICE が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の iostat が画面・出力に表示されること
    ② ステップ2 の sys0 が画面・出力に表示されること
    ③ ステップ3 の DEVICE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en



### vmstat 詳細確認 サービス状態 {#c01-i0801}
*分類: 性能監視*  ・  難易度: 中級

AIX 7.3 の 性能監視 で扱う「vmstat 詳細確認 サービス状態」は、CPU、メモリー、ページング、AME 統計を表示する性能コマンドを詳細確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-039を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** vmstat 詳細確認 サービス状態の設定や表示を読む前に役割を確認します。lparstat 状態判定 変更証跡ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。
    - B. 対象資源に対する働きはデバイス管理でrmdev -Rl ent1を用い・PVID と診断対象表示を確認する。
    - C. 対象資源に対する働きはCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。 ✅
    - D. 対象資源に対する働きはネットワークでsmitty etherchannelを用い・MTU と経路表を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「CPU、メモリー、ページング、AME 統計を表示する性能コマンドである」に対応する項目は詳細確認 サービス状態（詳細・vmst）です。性能監視の仕様は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」で、確認対象はvm・詳細・サーです。状態・変更・lparのA:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は状態判定 変更証跡（状態・lpar）です。変更後・rmdeのB:は「デバイス管理でrmdev -Rl ent1を用い、PVID」を述べ、対象は変更後確認 PVID（変更・rmde）です。状態・smitのD:は「ネットワークでsmitty etherchannelを用い、MTU」を述べ、対象は状態確認 MTU（状態・smit）です。「vmstat」は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を指し、詳細確認 サービス状態ではvm・詳細・サーに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **vmstat 詳細確認 サービス状態**

    - 検証目的: 性能監視のvmstat 詳細確認 サービス状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、性能監視の対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lsattr -E -l sys0 -a iostat
    → Enter を押す
    ```

    画面・出力:
    ```text
    iostat true Continuously maintain disk I/O history True
    ```

    画面・出力には iostat が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> chdev -l sys0 -a iostat=true
    → Enter を押す
    ```

    画面・出力:
    ```text
    sys0 changed
    ```

    画面・出力には sys0 が含まれ、vmstat 詳細確認 サービス状態の証跡を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、資源名の誤指定を切り分けます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lscfg -l sysplanar0
    → Enter を押す
    ```

    画面・出力:
    ```text
    DEVICE          LOCATION     DESCRIPTION
    sysplanar0      00-00        CPU Planar
    ```

    画面・出力には DEVICE が現れ、判定材料を記録できます。

    - 合格条件: ① ステップ1 の iostat が画面・出力に表示されること
    ② ステップ2 の sys0 が画面・出力に表示されること
    ③ ステップ3 の DEVICE が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en




## AIX 7.3 > 性能管理

### filemon 変更後確認 Busy% 0384 {#c01-i0802}
*分類: 性能管理*  ・  難易度: 中級

霜月記録ではAIX 7.3の性能管理で filemon を確認します。霜月記録の性能管理では Busy% とtopasディスク表示を同じ証跡に残します。霜月記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。霜月記録の注意点として 初回サンプルだけの誤判定 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、霜月記録を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** filemon 変更後確認 Busy% 0384を同一分類のpwdck -n ALL 障害切り分け authorizations 0385と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味はセキュリティでpwdck -n ALLを用い・authorizations と監査設定を確認する。
    - B. 構成を確認する際の意味はJFS2でdf -gを用い・isnapshot とファイルシステム属性を確認する。
    - C. 構成を確認する際の意味は性能管理でfilemonを用い・Busy% とtopasディスク表示を確認する。 ✅
    - D. 構成を確認する際の意味はLVMでmigratepvを用い・PP SIZE とミラーコピー状態を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でfilemonを用い、Busy% とtopasディスク表示を確認する」に対応する項目は変更後確認 Busy%（変更・file）です。変更後に関する性能管理の仕様は「性能管理でfilemonを用い、Busy%」で、確認対象はfi・変更後です。障害切・pwdcのA:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は障害切り分け authorizati（障害・pwdc）です。属性・dfのB:は「JFS2でdf -gを用い、isnapshot」を述べ、対象は属性確認 isnapshot（属性・df）です。バック・migrのD:は「LVMでmigratepvを用い、PP SIZE」を述べ、対象はPP SIZE（バッ・migr）です。「filemon」は「性能管理でfilemonを用い、Busy%」を指し、変更後確認 Busy%ではfi・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **filemon 変更後確認 Busy% 0384**

    - 検証目的: 性能管理のfilemon 変更後確認 Busy% 0384について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認024-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> filemon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0384A
    ```

    画面・出力には AIX0384A が表示され、filemon 変更後確認 Busy% 0384 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0384B
    ```

    画面・出力には AIX0384B が表示され、filemon 変更後確認 Busy% 0384 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0384C
    ```

    画面・出力には AIX0384C が表示され、filemon 変更後確認 Busy% 0384 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0384A が画面・出力に表示されること
    ② ステップ2 の AIX0384B が画面・出力に表示されること
    ③ ステップ3 の AIX0384C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### filemon 変更後確認 avm 0444 {#c01-i0803}
*分類: 性能管理*  ・  難易度: 中級

若草整理ではAIX 7.3の性能管理で filemon を確認します。若草整理の性能管理では avm とtopasディスク表示を同じ証跡に残します。若草整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若草整理の注意点として 初回サンプルだけの誤判定 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、若草整理を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** filemon 変更後確認 avm 0444の技術的な意味を資料で確認するとき、pwdck -n ALL 障害切り分け authorizations 0445との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はセキュリティでpwdck -n ALLを用い・authorizations と監査設定を確認する。
    - B. 構成を確認する際の意味はJFS2でsnapを用い・mountguard とファイルシステム属性を確認する。
    - C. 構成を確認する際の意味は性能管理でfilemonを用い・avm とtopasディスク表示を確認する。 ✅
    - D. 構成を確認する際の意味はLVMでvaryonvgを用い・STALE PARTITIONS とミラーコピー状態を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でfilemonを用い、avm とtopasディスク表示を確認する」に対応する項目は変更後確認 avm（変更・file）です。変更後に関する性能管理の仕様は「性能管理でfilemonを用い、avm とtopasディスク表示を確」で、確認対象はfi・変更後です。障害切・pwdcのA:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は障害切り分け authorizati（障害・pwdc）です。状態・snapのB:は「JFS2でsnapを用い、mountguard」を述べ、対象は状態確認 mountguard（状態・snap）です。監査・varyのD:は「LVMでvaryonvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（監査・vary）です。「filemon」は「性能管理でfilemonを用い、avm とtopasディスク表示を確」を指し、変更後確認 avmではfi・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **filemon 変更後確認 avm 0444**

    - 検証目的: 性能管理のfilemon 変更後確認 avm 0444について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認084-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> filemon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0444A
    ```

    画面・出力には AIX0444A が表示され、filemon 変更後確認 avm 0444 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0444B
    ```

    画面・出力には AIX0444B が表示され、filemon 変更後確認 avm 0444 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0444C
    ```

    画面・出力には AIX0444C が表示され、filemon 変更後確認 avm 0444 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0444A が画面・出力に表示されること
    ② ステップ2 の AIX0444B が画面・出力に表示されること
    ③ ステップ3 の AIX0444C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### filemon 性能確認 po 0414 {#c01-i0804}
*分類: 性能管理*  ・  難易度: 中級

星霜評価ではAIX 7.3の性能管理で filemon を確認します。星霜評価の性能管理では po とvmstat表示を変更票へ記録します。星霜評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。星霜評価の注意点として ディスクBusyと待ち時間の混同 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、星霜評価を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** filemon 性能確認 po 0414に関する障害切り分けの前提を確認しています。pwdck -n ALL 起動確認 authorizations 0415の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはセキュリティでpwdck -n ALLを用い・authorizations とロール一覧を確認する。
    - B. 機能の説明としては性能管理でfilemonを用い・po とvmstat表示を確認する。 ✅
    - C. 機能の説明としてはJFS2でdf -gを用い・ファイルシステム使用率 とログデバイス設定を確認する。
    - D. 機能の説明としてはLVMでmigratepvを用い・PVID とボリュームグループ属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でfilemonを用い、po とvmstat表示を確認する」に対応する項目は性能確認 po（性能・file）です。性能に関する性能管理の仕様は「性能管理でfilemonを用い、po とvmstat表示を確認する」で、確認対象はfi・性能です。起動・pwdcのA:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は起動確認 authorization（起動・pwdc）です。バック・dfのC:は「JFS2でdf -gを用い、ファイルシステム使用率」を述べ、対象はバックアウト確認 ファイルシステム使（バッ・df）です。属性・migrのD:は「LVMでmigratepvを用い、PVID」を述べ、対象は属性確認 PVID（属性・migr）です。「filemon」は「性能管理でfilemonを用い、po とvmstat表示を確認する」を指し、性能確認 poではfi・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **filemon 性能確認 po 0414**

    - 検証目的: 性能管理のfilemon 性能確認 po 0414について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認054-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> filemon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0414A
    ```

    画面・出力には AIX0414A が表示され、filemon 性能確認 po 0414 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0414B
    ```

    画面・出力には AIX0414B が表示され、filemon 性能確認 po 0414 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0414C
    ```

    画面・出力には AIX0414C が表示され、filemon 性能確認 po 0414 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0414A が画面・出力に表示されること
    ② ステップ2 の AIX0414B が画面・出力に表示されること
    ③ ステップ3 の AIX0414C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### filemon 構成照合 csz 0097 {#c01-i0805}
*分類: 性能管理*  ・  難易度: 中級

初霜点検ではAIX 7.3の性能管理で filemon を確認します。初霜点検の性能管理では csz とAME統計を採取票へ記録します。初霜点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。初霜点検の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、初霜点検を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「filemon 構成照合 csz 0097」を「pwdck -n ALL 変更前確認 user attributes 0098」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はセキュリティでpwdck -n ALLを用い・user attributes とRBAC属性を確認する。
    - B. 保守作業で参照する機能は性能管理でfilemonを用い・csz とAME統計を確認する。 ✅
    - C. 保守作業で参照する機能はJFS2でsnapを用い・agblksize と内部スナップショットを確認する。
    - D. 保守作業で参照する機能はセキュリティでsetsecattrを用い・enhanced_RBAC とRBAC属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でfilemonを用い、csz とAME統計を確認する」に対応する項目は構成照合 csz（構成・file）です。構成に関する性能管理の仕様は「性能管理でfilemonを用い、csz とAME統計を確認する」で、確認対象はfi・構成です。変更前・pwdcのA:は「セキュリティでpwdck -n ALLを用い、user」を述べ、対象はuser attributes（変更・pwdc）です。起動・snapのC:は「JFS2でsnapを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・snap）です。運用引・setsのD:は「セキュリティでsetsecattrを用い」を述べ、対象は運用引継ぎ enhanced_RBA（運用・sets）です。「filemon」は「性能管理でfilemonを用い、csz とAME統計を確認する」を指し、構成照合 cszではfi・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **filemon 構成照合 csz 0097**

    - 検証目的: 性能管理のfilemon 構成照合 csz 0097について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合097-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> filemon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0097A
    ```

    画面・出力には AIX0097A が表示され、filemon 構成照合 csz 0097 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0097B
    ```

    画面・出力には AIX0097B が表示され、filemon 構成照合 csz 0097 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0097C
    ```

    画面・出力には AIX0097C が表示され、filemon 構成照合 csz 0097 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0097A が画面・出力に表示されること
    ② ステップ2 の AIX0097B が画面・出力に表示されること
    ③ ステップ3 の AIX0097C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### filemon 構成照合 po 0573 {#c01-i0806}
*分類: 性能管理*  ・  難易度: 中級

月影点検ではAIX 7.3の性能管理で filemon を確認します。月影点検の性能管理では po とAME統計を判定票へ残します。月影点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。月影点検の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、月影点検を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** filemon 構成照合 po 0573を保守記録に説明する必要があります。pwdck -n ALL 変更前確認 authorizations 0574と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はセキュリティでpwdck -n ALLを用い・authorizations とRBAC属性を確認する。
    - B. 運用時に利用する技術的役割はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。
    - C. 運用時に利用する技術的役割は性能管理でfilemonを用い・po とAME統計を確認する。 ✅
    - D. 運用時に利用する技術的役割はLVMでvaryonvgを用い・PP SIZE と物理ボリューム一覧を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でfilemonを用い、po とAME統計を確認する」に対応する項目は構成照合 po（構成・file）です。構成に関する性能管理の仕様は「性能管理でfilemonを用い、po とAME統計を確認する」で、確認対象はfi・構成です。変更前・pwdcのA:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は変更前確認 authorizatio（変更・pwdc）です。詳細・サー・vmstのB:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は詳細確認 サービス状態（詳細・vmst）です。障害切・varyのD:は「LVMでvaryonvgを用い、PP SIZE」を述べ、対象はPP SIZE（障害・vary）です。「filemon」は「性能管理でfilemonを用い、po とAME統計を確認する」を指し、構成照合 poではfi・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **filemon 構成照合 po 0573**

    - 検証目的: 性能管理のfilemon 構成照合 po 0573について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合093-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> filemon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0573A
    ```

    画面・出力には AIX0573A が表示され、filemon 構成照合 po 0573 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0573B
    ```

    画面・出力には AIX0573B が表示され、filemon 構成照合 po 0573 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0573C
    ```

    画面・出力には AIX0573C が表示され、filemon 構成照合 po 0573 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0573A が画面・出力に表示されること
    ② ステップ2 の AIX0573B が画面・出力に表示されること
    ③ ステップ3 の AIX0573C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### filemon 運用引継ぎ Busy% 0543 {#c01-i0807}
*分類: 性能管理*  ・  難易度: 中級

新緑照合ではAIX 7.3の性能管理で filemon を確認します。新緑照合の性能管理では Busy% とsvmon全体表示を作業票へ保管します。新緑照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。新緑照合の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、新緑照合を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** filemon 運用引継ぎ Busy% 0543の設定や表示を読む前に役割を確認します。pwdck -n ALL 容量確認 authorizations 0544ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは性能管理でfilemonを用い・Busy% とsvmon全体表示を確認する。 ✅
    - B. 状態を読み取るための働きはセキュリティでpwdck -n ALLを用い・authorizations とユーザー属性を確認する。
    - C. 状態を読み取るための働きはCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。
    - D. 状態を読み取るための働きはLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でfilemonを用い、Busy% とsvmon全体表示を確認する」に対応する項目は運用引継ぎ Busy%（運用・file）です。運用引に関する性能管理の仕様は「性能管理でfilemonを用い、Busy%」で、確認対象はfi・運用引です。容量・pwdcのB:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は容量確認 authorization（容量・pwdc）です。一覧・出力・vmstのC:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は一覧確認 出力見出し（一覧・vmst）です。性能・migrのD:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（性能・migr）です。「filemon」は「性能管理でfilemonを用い、Busy%」を指し、運用引継ぎ Busy%ではfi・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **filemon 運用引継ぎ Busy% 0543**

    - 検証目的: 性能管理のfilemon 運用引継ぎ Busy% 0543について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ063-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> filemon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0543A
    ```

    画面・出力には AIX0543A が表示され、filemon 運用引継ぎ Busy% 0543 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0543B
    ```

    画面・出力には AIX0543B が表示され、filemon 運用引継ぎ Busy% 0543 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0543C
    ```

    画面・出力には AIX0543C が表示され、filemon 運用引継ぎ Busy% 0543 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0543A が画面・出力に表示されること
    ② ステップ2 の AIX0543B が画面・出力に表示されること
    ③ ステップ3 の AIX0543C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### filemon 運用引継ぎ PhysB 0067 {#c01-i0808}
*分類: 性能管理*  ・  難易度: 中級

風花照合ではAIX 7.3の性能管理で filemon を確認します。風花照合の性能管理では PhysB とsvmon全体表示を点検票へ整理します。風花照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。風花照合の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、風花照合を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** filemon 運用引継ぎ PhysB 0067について構成や状態を確認します。pwdck -n ALL 容量確認 user attributes 0068ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはセキュリティでpwdck -n ALLを用い・user attributes とユーザー属性を確認する。
    - B. 対象資源に対する働きはJFS2でsnapを用い・lff とマウントオプションを確認する。
    - C. 対象資源に対する働きはセキュリティでsetsecattrを用い・enhanced_RBAC とユーザー属性を確認する。
    - D. 対象資源に対する働きは性能管理でfilemonを用い・PhysB とsvmon全体表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でfilemonを用い、PhysB とsvmon全体表示を確認する」に対応する項目は運用引継ぎ PhysB（運用・file）です。性能管理の仕様は「性能管理でfilemonを用い、PhysB」で、確認対象はfi・運用引です。容量・pwdcのA:は「セキュリティでpwdck -n ALLを用い、user」を述べ、対象はuser attributes（容量・pwdc）です。障害切・snapのB:は「JFS2でsnapを用い、lff とマウントオプションを確認する」を述べ、対象は障害切り分け lff（障害・snap）です。構成・setsのC:は「セキュリティでsetsecattrを用い」を述べ、対象は構成照合 enhanced_RBAC（構成・sets）です。「filemon」は「性能管理でfilemonを用い、PhysB」を指し、運用引継ぎ PhysBではfi・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **filemon 運用引継ぎ PhysB 0067**

    - 検証目的: 性能管理のfilemon 運用引継ぎ PhysB 0067について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ067-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> filemon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0067A
    ```

    画面・出力には AIX0067A が表示され、filemon 運用引継ぎ PhysB 0067 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0067B
    ```

    画面・出力には AIX0067B が表示され、filemon 運用引継ぎ PhysB 0067 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0067C
    ```

    画面・出力には AIX0067C が表示され、filemon 運用引継ぎ PhysB 0067 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0067A が画面・出力に表示されること
    ② ステップ2 の AIX0067B が画面・出力に表示されること
    ③ ステップ3 の AIX0067C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### iostat -Dl 2 2 バックアウト確認 Busy% 0172 {#c01-i0809}
*分類: 性能管理*  ・  難易度: 中級

水音判定ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。水音判定の性能管理では Busy% とtopasディスク表示を監査票へ転記します。水音判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。水音判定の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、水音判定を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** iostat -Dl 2 2 バックアウト確認 Busy% 0172の技術的な意味を資料で確認するとき、lssecattr -c 監査記録 audit class 0173との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はセキュリティでlssecattr -cを用い・audit class と監査設定を確認する。
    - B. 管理対象との関係を表す説明は性能管理でiostat -Dl 2 2を用い・Busy% とtopasディスク表示を確認する。 ✅
    - C. 管理対象との関係を表す説明はJFS2でchfsを用い・isnapshot とファイルシステム属性を確認する。
    - D. 管理対象との関係を表す説明はセキュリティでlsroleを用い・user attributes と監査設定を確認する。lsrole 属性確認 user attributes 0785固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でiostat -Dl 2 2を用い、Busy%」に対応する項目はバックアウト確認 Busy%（バッ・iost）です。バックに関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、Busy%」で、確認対象はio・バックです。監査・lsseのA:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（監査・lsse）です。構成・chfsのC:は「JFS2でchfsを用い、isnapshot」を述べ、対象は構成照合 isnapshot（構成・chfs）です。属性・lsroのD:は「セキュリティでlsroleを用い、user attributes」を述べ、対象はuser attributes（属性・lsro）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、Busy%」を指し、バックアウト確認 Busy%ではio・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **iostat -Dl 2 2 バックアウト確認 Busy% 0172**

    - 検証目的: 性能管理のiostat -Dl 2 2 バックアウト確認 Busy% 0172について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認052-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> iostat -Dl 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0172A
    ```

    画面・出力には AIX0172A が表示され、iostat -Dl 2 2 バックアウト確認 Busy% 0172 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0172B
    ```

    画面・出力には AIX0172B が表示され、iostat -Dl 2 2 バックアウト確認 Busy% 0172 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0172C
    ```

    画面・出力には AIX0172C が表示され、iostat -Dl 2 2 バックアウト確認 Busy% 0172 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0172A が画面・出力に表示されること
    ② ステップ2 の AIX0172B が画面・出力に表示されること
    ③ ステップ3 の AIX0172C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### iostat -Dl 2 2 バックアウト確認 dxm 0648 {#c01-i0810}
*分類: 性能管理*  ・  難易度: 中級

翠風判定ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。翠風判定の性能管理では dxm とtopasディスク表示を同じ証跡に残します。翠風判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。翠風判定の注意点として 初回サンプルだけの誤判定 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、翠風判定を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** iostat -Dl 2 2 バックアウト確認 dxm 0648を同一分類のlssecattr -c 監査記録 enhanced_RBAC 0649と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は性能管理でiostat -Dl 2 2を用い・dxm とtopasディスク表示を確認する。 ✅
    - B. 構成を確認する際の意味はセキュリティでlssecattr -cを用い・enhanced_RBAC と監査設定を確認する。
    - C. 構成を確認する際の意味はSRCとログでsyslog_ssw -rを用い・syslog.conf とSRCサブシステム表示を確認する。
    - D. 構成を確認する際の意味はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でiostat -Dl 2 2を用い、dxm」に対応する項目はバックアウト確認 dxm（バッ・iost）です。バックに関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、dxm」で、確認対象はio・バックです。監査・lsseのB:は「セキュリティでlssecattr -cを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsse）です。起動・syslのC:は「SRCとログでsyslog_ssw -rを用い」を述べ、対象は起動確認 syslog.conf（起動・sysl）です。運用引・lslvのD:は「LVMでlslvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・lslv）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、dxm」を指し、バックアウト確認 dxmではio・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **iostat -Dl 2 2 バックアウト確認 dxm 0648**

    - 検証目的: 性能管理のiostat -Dl 2 2 バックアウト確認 dxm 0648について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認048-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> iostat -Dl 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0648A
    ```

    画面・出力には AIX0648A が表示され、iostat -Dl 2 2 バックアウト確認 dxm 0648 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0648B
    ```

    画面・出力には AIX0648B が表示され、iostat -Dl 2 2 バックアウト確認 dxm 0648 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0648C
    ```

    画面・出力には AIX0648C が表示され、iostat -Dl 2 2 バックアウト確認 dxm 0648 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0648A が画面・出力に表示されること
    ② ステップ2 の AIX0648B が画面・出力に表示されること
    ③ ステップ3 の AIX0648C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### iostat -Dl 2 2 変更後確認 Entitled Capacity 0777 {#c01-i0811}
*分類: 性能管理*  ・  難易度: 中級

初霜復旧ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。初霜復旧の性能管理では Entitled Capacity とAME統計を判定票へ残します。初霜復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。初霜復旧の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、初霜復旧を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「iostat -Dl 2 2 変更後確認 Entitled Capacity 0777」を「chdev 障害切り分け ボリューム状態」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はデバイス属性を変更する管理コマンドである。chdev 障害切り分け ボリューム状態固有の属性も確認対象に含める。
    - B. 運用時に利用する技術的役割は性能管理でnmonを用い・Busy% とAME統計を確認する。
    - C. 運用時に利用する技術的役割は性能管理でiostat -Dl 2 2を用い・Entitled Capacity とAME統計を確認する。 ✅
    - D. 運用時に利用する技術的役割はネットワークでsmitty etherchannelを用い・EtherChannelである。

    正解: **C** ／ 難易度: 中級

    **解説:** 変更後・iostでCの記述「性能管理でiostat -Dl 2 2を用い、Entitled」に対応する項目はEntitled Capacity（変更・iost）です。変更後に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、Entitled」で、確認対象はio・変更後です。障害切・chdeのA:は「デバイス属性を変更する管理コマンド」を述べ、対象は障害切り分け ボリューム状態（障害・chde）です。起動・nmonのB:は「性能管理でnmonを用い、Busy% とAME統計を確認する」を述べ、対象は起動確認 Busy%（起動・nmon）です。監査・smitのD:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は監査記録 EtherChannel（監査・smit）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、Entitled」を指し、Entitled Capacityではio・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **iostat -Dl 2 2 変更後確認 Entitled Capacity 0777**

    - 検証目的: 性能管理のiostat -Dl 2 2 変更後確認 Entitled Capacity 0777について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認057-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> iostat -Dl 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0777A
    ```

    画面・出力には AIX0777A が表示され、iostat -Dl 2 2 変更後確認 Entitled Capacity 0777 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0777B
    ```

    画面・出力には AIX0777B が表示され、iostat -Dl 2 2 変更後確認 Entitled Capacity 0777 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0777C
    ```

    画面・出力には AIX0777C が表示され、iostat -Dl 2 2 変更後確認 Entitled Capacity 0777 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0777A が画面・出力に表示されること
    ② ステップ2 の AIX0777B が画面・出力に表示されること
    ③ ステップ3 の AIX0777C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### iostat -Dl 2 2 変更後確認 avm 0301 {#c01-i0812}
*分類: 性能管理*  ・  難易度: 中級

群青復旧ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。群青復旧の性能管理では avm とAME統計を採取票へ記録します。群青復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。群青復旧の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、群青復旧を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** iostat -Dl 2 2 変更後確認 avm 0301を保守記録に説明する必要があります。lssecattr -c 障害切り分け audit class 0302と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能は性能管理でiostat -Dl 2 2を用い・avm とAME統計を確認する。 ✅
    - B. 保守作業で参照する機能はセキュリティでlssecattr -cを用い・audit class とRBAC属性を確認する。
    - C. 保守作業で参照する機能はJFS2でlsfs -qを用い・mountguard と内部スナップショットを確認する。
    - D. 保守作業で参照する機能はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でiostat -Dl 2 2を用い、avm とAME統計を確認する」に対応する項目は変更後確認 avm（変更・iost）です。変更後に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、avm」で、確認対象はio・変更後です。障害切・lsseのB:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（障害・lsse）です。状態・lsfsのC:は「JFS2でlsfs -qを用い、mountguard」を述べ、対象は状態確認 mountguard（状態・lsfs）です。一覧・メッ・lspsのD:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は一覧確認 メッセージ行（一覧・lsps）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、avm」を指し、変更後確認 avmではio・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **iostat -Dl 2 2 変更後確認 avm 0301**

    - 検証目的: 性能管理のiostat -Dl 2 2 変更後確認 avm 0301について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認061-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> iostat -Dl 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0301A
    ```

    画面・出力には AIX0301A が表示され、iostat -Dl 2 2 変更後確認 avm 0301 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0301B
    ```

    画面・出力には AIX0301B が表示され、iostat -Dl 2 2 変更後確認 avm 0301 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0301C
    ```

    画面・出力には AIX0301C が表示され、iostat -Dl 2 2 変更後確認 avm 0301 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0301A が画面・出力に表示されること
    ② ステップ2 の AIX0301B が画面・出力に表示されること
    ③ ステップ3 の AIX0301C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### iostat -Dl 2 2 変更後確認 pi 0837 {#c01-i0813}
*分類: 性能管理*  ・  難易度: 上級

冬晴変更ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。冬晴変更の性能管理では pi とAME統計を判定票へ残します。冬晴変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。冬晴変更の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、冬晴変更を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** iostat -Dl 2 2 変更後確認 pi 0837を保守記録に説明する必要があります。lscfg 状態判定 除外条件と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は構成済みデバイスと VPD を表示するコマンドである。
    - B. 運用時に利用する技術的役割はセキュリティでsetsecattrを用い・audit class とRBAC属性を確認する。
    - C. 運用時に利用する技術的役割はセキュリティでlsattr -E -l sys0 -aを用い・roles とRBAC属性を確認する。
    - D. 運用時に利用する技術的役割は性能管理でiostat -Dl 2 2を用い・pi とAME統計を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 変更後・iostでDの記述「性能管理でiostat -Dl 2 2を用い、pi」に対応する項目は変更後確認 pi（変更・iost）です。変更後に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、pi」で、確認対象はio・変更後です。状態・除外・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は状態判定 除外条件（状態・lscf）です。運用引・setsのB:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（運用・sets）です。監査・lsatのC:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 roles（監査・lsat）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、pi」を指し、変更後確認 piではio・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **iostat -Dl 2 2 変更後確認 pi 0837**

    - 検証目的: 性能管理のiostat -Dl 2 2 変更後確認 pi 0837について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認117-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> iostat -Dl 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0837A
    ```

    画面・出力には AIX0837A が表示され、iostat -Dl 2 2 変更後確認 pi 0837 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0837B
    ```

    画面・出力には AIX0837B が表示され、iostat -Dl 2 2 変更後確認 pi 0837 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0837C
    ```

    画面・出力には AIX0837C が表示され、iostat -Dl 2 2 変更後確認 pi 0837 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0837A が画面・出力に表示されること
    ② ステップ2 の AIX0837B が画面・出力に表示されること
    ③ ステップ3 の AIX0837C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### iostat -Dl 2 2 属性確認 Entitled Capacity 0618 {#c01-i0814}
*分類: 性能管理*  ・  難易度: 初級

潮騒採取ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。潮騒採取の性能管理では Entitled Capacity とvmstat表示を変更票へ記録します。潮騒採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。潮騒採取の注意点として ディスクBusyと待ち時間の混同 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、潮騒採取を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** iostat -Dl 2 2 属性確認 Entitled Capacity 0618の役割を調べています。lssecattr -c 状態確認 enhanced_RBAC 0619の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはセキュリティでlssecattr -cを用い・enhanced_RBAC とロール一覧を確認する。
    - B. 機能の説明としては導入と起動でalt_disk_copyを用い・EFIX LABEL と代替ディスク状態を確認する。
    - C. 機能の説明としては性能管理でiostat -Dl 2 2を用い・Entitled Capacityである。 ✅
    - D. 機能の説明としてはLVMでlslvを用い・LV STATE とボリュームグループ属性を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「性能管理でiostat -Dl 2 2を用い、Entitled」に対応する項目はEntitled Capacity（属性・iost）です。属性に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、Entitled」で、確認対象はio・属性です。状態・lsseのA:は「セキュリティでlssecattr -cを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsse）です。障害切・alt_のB:は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（障害・alt_）です。構成・lslvのD:は「LVMでlslvを用い、LV STATE」を述べ、対象はLV STATE（構成・lslv）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、Entitled」を指し、Entitled Capacityではio・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **iostat -Dl 2 2 属性確認 Entitled Capacity 0618**

    - 検証目的: 性能管理のiostat -Dl 2 2 属性確認 Entitled Capacity 0618について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理属性確認018-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> iostat -Dl 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0618A
    ```

    画面・出力には AIX0618A が表示され、iostat -Dl 2 2 属性確認 Entitled Capacity 0618 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0618B
    ```

    画面・出力には AIX0618B が表示され、iostat -Dl 2 2 属性確認 Entitled Capacity 0618 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0618C
    ```

    画面・出力には AIX0618C が表示され、iostat -Dl 2 2 属性確認 Entitled Capacity 0618 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0618A が画面・出力に表示されること
    ② ステップ2 の AIX0618B が画面・出力に表示されること
    ③ ステップ3 の AIX0618C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### iostat -Dl 2 2 属性確認 avm 0142 {#c01-i0815}
*分類: 性能管理*  ・  難易度: 初級

紅葉採取ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。紅葉採取の性能管理では avm とvmstat表示を保守票へ記録します。紅葉採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。紅葉採取の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、紅葉採取を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** iostat -Dl 2 2 属性確認 avm 0142に関する障害切り分けの前提を確認しています。lssecattr -c 状態確認 audit class 0143の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はセキュリティでlssecattr -cを用い・audit class とロール一覧を確認する。
    - B. 表示や設定で扱う内容はJFS2でchfsを用い・ファイルシステム使用率 とログデバイス設定を確認する。
    - C. 表示や設定で扱う内容はセキュリティでlsroleを用い・user attributes とロール一覧を確認する。
    - D. 表示や設定で扱う内容は性能管理でiostat -Dl 2 2を用い・avm とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「性能管理でiostat -Dl 2 2を用い、avm とvmstat表示を確認する」に対応する項目は属性確認 avm（属性・iost）です。属性に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、avm」で、確認対象はio・属性です。状態・lsseのA:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（状態・lsse）です。運用引・chfsのB:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象は運用引継ぎ ファイルシステム使用率（運用・chfs）です。バック・lsroのC:は「セキュリティでlsroleを用い、user attributes」を述べ、対象はuser attributes（バッ・lsro）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、avm」を指し、属性確認 avmではio・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **iostat -Dl 2 2 属性確認 avm 0142**

    - 検証目的: 性能管理のiostat -Dl 2 2 属性確認 avm 0142について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理属性確認022-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> iostat -Dl 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0142A
    ```

    画面・出力には AIX0142A が表示され、iostat -Dl 2 2 属性確認 avm 0142 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0142B
    ```

    画面・出力には AIX0142B が表示され、iostat -Dl 2 2 属性確認 avm 0142 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0142C
    ```

    画面・出力には AIX0142C が表示され、iostat -Dl 2 2 属性確認 avm 0142 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0142A が画面・出力に表示されること
    ② ステップ2 の AIX0142B が画面・出力に表示されること
    ③ ステップ3 の AIX0142C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### iostat -Dl 2 2 性能確認 Busy% 0331 {#c01-i0816}
*分類: 性能管理*  ・  難易度: 中級

松風変更ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。松風変更の性能管理では Busy% とsvmon全体表示を点検票へ整理します。松風変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。松風変更の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、松風変更を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** iostat -Dl 2 2 性能確認 Busy% 0331について構成や状態を確認します。lssecattr -c 起動確認 audit class 0332ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは性能管理でiostat -Dl 2 2を用い・Busy% とsvmon全体表示を確認する。 ✅
    - B. 対象資源に対する働きはセキュリティでlssecattr -cを用い・audit class とユーザー属性を確認する。
    - C. 対象資源に対する働きはJFS2でlsfs -qを用い・log=INLINE とマウントオプションを確認する。
    - D. 対象資源に対する働きはLVMでmklvを用い・PVID と論理ボリューム配置を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でiostat -Dl 2 2を用い、Busy%」に対応する項目は性能確認 Busy%（性能・iost）です。性能に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、Busy%」で、確認対象はio・性能です。起動・lsseのB:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（起動・lsse）です。監査・lsfsのC:は「JFS2でlsfs -qを用い、log=INLINE」を述べ、対象は監査記録 log=INLINE（監査・lsfs）です。状態・mklvのD:は「LVMでmklvを用い、PVID と論理ボリューム配置を確認する」を述べ、対象は状態確認 PVID（状態・mklv）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、Busy%」を指し、性能確認 Busy%ではio・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **iostat -Dl 2 2 性能確認 Busy% 0331**

    - 検証目的: 性能管理のiostat -Dl 2 2 性能確認 Busy% 0331について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認091-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> iostat -Dl 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0331A
    ```

    画面・出力には AIX0331A が表示され、iostat -Dl 2 2 性能確認 Busy% 0331 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0331B
    ```

    画面・出力には AIX0331B が表示され、iostat -Dl 2 2 性能確認 Busy% 0331 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0331C
    ```

    画面・出力には AIX0331C が表示され、iostat -Dl 2 2 性能確認 Busy% 0331 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0331A が画面・出力に表示されること
    ② ステップ2 の AIX0331B が画面・出力に表示されること
    ③ ステップ3 の AIX0331C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### iostat -Dl 2 2 性能確認 dxm 0807 {#c01-i0817}
*分類: 性能管理*  ・  難易度: 中級

夕凪変更ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。夕凪変更の性能管理では dxm とsvmon全体表示を作業票へ保管します。夕凪変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。夕凪変更の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、夕凪変更を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** iostat -Dl 2 2 性能確認 dxm 0807の設定や表示を読む前に役割を確認します。lspv 状態判定 照合単位ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - B. 状態を読み取るための働きはJFS2でdf -gを用い・log=INLINE とファイルシステム属性を確認する。
    - C. 状態を読み取るための働きは性能管理でiostat -Dl 2 2を用い・dxm とsvmon全体表示を確認する。 ✅
    - D. 状態を読み取るための働きはLVMでmigratepvを用い・LV STATE とボリュームグループ属性を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** 性能・iostでCの記述「性能管理でiostat -Dl 2 2を用い、dxm」に対応する項目は性能確認 dxm（性能・iost）です。性能に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、dxm」で、確認対象はio・性能です。状態・照合・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は状態判定 照合単位（状態・lspv）です。属性・dfのB:は「JFS2でdf -gを用い、log=INLINE」を述べ、対象は属性確認 log=INLINE（属性・df）です。属性・migrのD:は「LVMでmigratepvを用い、LV STATE」を述べ、対象はLV STATE（属性・migr）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、dxm」を指し、性能確認 dxmではio・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **iostat -Dl 2 2 性能確認 dxm 0807**

    - 検証目的: 性能管理のiostat -Dl 2 2 性能確認 dxm 0807について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認087-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> iostat -Dl 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0807A
    ```

    画面・出力には AIX0807A が表示され、iostat -Dl 2 2 性能確認 dxm 0807 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0807B
    ```

    画面・出力には AIX0807B が表示され、iostat -Dl 2 2 性能確認 dxm 0807 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0807C
    ```

    画面・出力には AIX0807C が表示され、iostat -Dl 2 2 性能確認 dxm 0807 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0807A が画面・出力に表示されること
    ② ステップ2 の AIX0807B が画面・出力に表示されること
    ③ ステップ3 の AIX0807C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### iostat -Dl 2 2 性能確認 pi 0747 {#c01-i0818}
*分類: 性能管理*  ・  難易度: 中級

風花監査ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。風花監査の性能管理では pi とsvmon全体表示を作業票へ保管します。風花監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。風花監査の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、風花監査を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** iostat -Dl 2 2 性能確認 pi 0747について構成や状態を確認します。lssecattr -c 起動確認 enhanced_RBAC 0748ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはセキュリティでlssecattr -cを用い・enhanced_RBAC とユーザー属性を確認する。
    - B. 状態を読み取るための働きは性能管理でiostat -Dl 2 2を用い・pi とsvmon全体表示を確認する。 ✅
    - C. 状態を読み取るための働きは導入と起動でalt_disk_copyを用い・EFIX LABEL と起動デバイス設定を確認する。
    - D. 状態を読み取るための働きはLVMでlslvを用い・VG STATE と論理ボリューム配置を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でiostat -Dl 2 2を用い、pi とsvmon全体表示を確認する」に対応する項目は性能確認 pi（性能・iost）です。性能に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、pi」で、確認対象はio・性能です。起動・lsseのA:は「セキュリティでlssecattr -cを用い」を述べ、対象は起動確認 enhanced_RBAC（起動・lsse）です。変更前・alt_のC:は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（変更・alt_）です。属性・lslvのD:は「LVMでlslvを用い、VG STATE」を述べ、対象はVG STATE（属性・lslv）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、pi」を指し、性能確認 piではio・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **iostat -Dl 2 2 性能確認 pi 0747**

    - 検証目的: 性能管理のiostat -Dl 2 2 性能確認 pi 0747について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認027-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> iostat -Dl 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0747A
    ```

    画面・出力には AIX0747A が表示され、iostat -Dl 2 2 性能確認 pi 0747 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0747B
    ```

    画面・出力には AIX0747B が表示され、iostat -Dl 2 2 性能確認 pi 0747 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0747C
    ```

    画面・出力には AIX0747C が表示され、iostat -Dl 2 2 性能確認 pi 0747 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0747A が画面・出力に表示されること
    ② ステップ2 の AIX0747B が画面・出力に表示されること
    ③ ステップ3 の AIX0747C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### iostat -Dl 2 2 性能確認 po 0271 {#c01-i0819}
*分類: 性能管理*  ・  難易度: 中級

遠雷監査ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。遠雷監査の性能管理では po とsvmon全体表示を点検票へ整理します。遠雷監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。遠雷監査の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、遠雷監査を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** iostat -Dl 2 2 性能確認 po 0271の設定や表示を読む前に役割を確認します。lssecattr -c 起動確認 audit class 0272ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはセキュリティでlssecattr -cを用い・audit class とユーザー属性を確認する。
    - B. 対象資源に対する働きは性能管理でiostat -Dl 2 2を用い・po とsvmon全体表示を確認する。 ✅
    - C. 対象資源に対する働きはJFS2でchfsを用い・ファイルシステム使用率 とマウントオプションを確認する。
    - D. 対象資源に対する働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でiostat -Dl 2 2を用い、po とsvmon全体表示を確認する」に対応する項目は性能確認 po（性能・iost）です。性能に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、po」で、確認対象はio・性能です。起動・lsseのA:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（起動・lsse）です。バック・chfsのC:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象はバックアウト確認 ファイルシステム使（バッ・chfs）です。復旧前・lspsのD:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は復旧前確認 復旧手掛かり（復旧・lsps）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、po」を指し、性能確認 poではio・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **iostat -Dl 2 2 性能確認 po 0271**

    - 検証目的: 性能管理のiostat -Dl 2 2 性能確認 po 0271について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認031-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> iostat -Dl 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0271A
    ```

    画面・出力には AIX0271A が表示され、iostat -Dl 2 2 性能確認 po 0271 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0271B
    ```

    画面・出力には AIX0271B が表示され、iostat -Dl 2 2 性能確認 po 0271 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0271C
    ```

    画面・出力には AIX0271C が表示され、iostat -Dl 2 2 性能確認 po 0271 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0271A が画面・出力に表示されること
    ② ステップ2 の AIX0271B が画面・出力に表示されること
    ③ ステップ3 の AIX0271C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lparstat -i 変更前確認 Entitled Capacity 0157 {#c01-i0820}
*分類: 性能管理*  ・  難易度: 中級

冬晴採取ではAIX 7.3の性能管理で lparstat -i を確認します。冬晴採取の性能管理では Entitled Capacity とAME統計を採取票へ記録します。冬晴採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。冬晴採取の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、冬晴採取を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lparstat -i 変更前確認 Entitled Capacity 0157を保守記録に説明する必要があります。usrck -n ALL 変更後確認 enhanced_RBAC 0158と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はセキュリティでusrck -n ALLを用い・enhanced_RBAC とRBAC属性を確認する。
    - B. 保守作業で参照する機能はJFS2でsnapを用い・agblksize と内部スナップショットを確認する。
    - C. 保守作業で参照する機能はセキュリティでchuserを用い・authorizations とRBAC属性を確認する。
    - D. 保守作業で参照する機能は性能管理でlparstat -iを用い・Entitled Capacity とAME統計を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でlparstat -iを用い、Entitled Capacity」に対応する項目はEntitled Capacity（変更・lpar）です。変更前に関する性能管理の仕様は「性能管理でlparstat -iを用い、Entitled」で、確認対象はlp・変更前です。変更後・usrcのA:は「セキュリティでusrck -n ALLを用い」を述べ、対象は変更後確認 enhanced_RBA（変更・usrc）です。起動・snapのB:は「JFS2でsnapを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・snap）です。容量・chusのC:は「セキュリティでchuserを用い、authorizations」を述べ、対象は容量確認 authorization（容量・chus）です。「lparstat -i」は「性能管理でlparstat -iを用い、Entitled」を指し、Entitled Capacityではlp・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lparstat -i 変更前確認 Entitled Capacity 0157**

    - 検証目的: 性能管理のlparstat -i 変更前確認 Entitled Capacity 0157について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認037-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lparstat -i
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0157A
    ```

    画面・出力には AIX0157A が表示され、lparstat -i 変更前確認 Entitled Capacity 0157 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0157B
    ```

    画面・出力には AIX0157B が表示され、lparstat -i 変更前確認 Entitled Capacity 0157 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0157C
    ```

    画面・出力には AIX0157C が表示され、lparstat -i 変更前確認 Entitled Capacity 0157 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0157A が画面・出力に表示されること
    ② ステップ2 の AIX0157B が画面・出力に表示されること
    ③ ステップ3 の AIX0157C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lparstat -i 変更前確認 PhysB 0633 {#c01-i0821}
*分類: 性能管理*  ・  難易度: 中級

朝霧採取ではAIX 7.3の性能管理で lparstat -i を確認します。朝霧採取の性能管理では PhysB とAME統計を判定票へ残します。朝霧採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。朝霧採取の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、朝霧採取を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「lparstat -i 変更前確認 PhysB 0633」を「usrck -n ALL 変更後確認 roles 0634」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は性能管理でlparstat -iを用い・PhysB とAME統計を確認する。 ✅
    - B. 運用時に利用する技術的役割はセキュリティでusrck -n ALLを用い・roles とRBAC属性を確認する。
    - C. 運用時に利用する技術的役割は導入と起動でnimadmを用い・altinst_rootvg とfileset一覧を確認する。
    - D. 運用時に利用する技術的役割はLVMでvaryonvgを用い・PP SIZE と物理ボリューム一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でlparstat -iを用い、PhysB とAME統計を確認する」に対応する項目は変更前確認 PhysB（変更・lpar）です。変更前に関する性能管理の仕様は「性能管理でlparstat -iを用い、PhysB」で、確認対象はlp・変更前です。変更後・usrcのB:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は変更後確認 roles（変更・usrc）です。運用引・nimaのC:は「導入と起動でnimadmを用い、altinst_rootvg」を述べ、対象は運用引継ぎ altinst_root（運用・nima）です。障害切・varyのD:は「LVMでvaryonvgを用い、PP SIZE」を述べ、対象はPP SIZE（障害・vary）です。「lparstat -i」は「性能管理でlparstat -iを用い、PhysB」を指し、変更前確認 PhysBではlp・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lparstat -i 変更前確認 PhysB 0633**

    - 検証目的: 性能管理のlparstat -i 変更前確認 PhysB 0633について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認033-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lparstat -i
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0633A
    ```

    画面・出力には AIX0633A が表示され、lparstat -i 変更前確認 PhysB 0633 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0633B
    ```

    画面・出力には AIX0633B が表示され、lparstat -i 変更前確認 PhysB 0633 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0633C
    ```

    画面・出力には AIX0633C が表示され、lparstat -i 変更前確認 PhysB 0633 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0633A が画面・出力に表示されること
    ② ステップ2 の AIX0633B が画面・出力に表示されること
    ③ ステップ3 の AIX0633C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lparstat -i 容量確認 fre 0603 {#c01-i0822}
*分類: 性能管理*  ・  難易度: 初級

秋声採取ではAIX 7.3の性能管理で lparstat -i を確認します。秋声採取の性能管理では fre とsvmon全体表示を作業票へ保管します。秋声採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。秋声採取の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、秋声採取を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lparstat -i 容量確認 fre 0603について構成や状態を確認します。usrck -n ALL 性能確認 roles 0604ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはセキュリティでusrck -n ALLを用い・roles とユーザー属性を確認する。
    - B. 状態を読み取るための働きは性能管理でlparstat -iを用い・fre とsvmon全体表示を確認する。 ✅
    - C. 状態を読み取るための働きはCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。
    - D. 状態を読み取るための働きはLVMでvaryonvgを用い・PVID と論理ボリューム配置を確認する。

    正解: **B** ／ 難易度: 初級

    **解説:** Bの記述「性能管理でlparstat -iを用い、fre とsvmon全体表示を確認する」に対応する項目は容量確認 fre（容量・lpar）です。容量に関する性能管理の仕様は「性能管理でlparstat -iを用い、fre」で、確認対象はlp・容量です。性能・usrcのA:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は性能確認 roles（性能・usrc）です。状態・イベ・vmstのC:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は状態判定 イベント転送（状態・vmst）です。起動・varyのD:は「LVMでvaryonvgを用い、PVID」を述べ、対象は起動確認 PVID（起動・vary）です。「lparstat -i」は「性能管理でlparstat -iを用い、fre」を指し、容量確認 freではlp・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lparstat -i 容量確認 fre 0603**

    - 検証目的: 性能管理のlparstat -i 容量確認 fre 0603について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認003-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lparstat -i
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0603A
    ```

    画面・出力には AIX0603A が表示され、lparstat -i 容量確認 fre 0603 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0603B
    ```

    画面・出力には AIX0603B が表示され、lparstat -i 容量確認 fre 0603 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0603C
    ```

    画面・出力には AIX0603C が表示され、lparstat -i 容量確認 fre 0603 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0603A が画面・出力に表示されること
    ② ステップ2 の AIX0603B が画面・出力に表示されること
    ③ ステップ3 の AIX0603C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lparstat -i 容量確認 pi 0127 {#c01-i0823}
*分類: 性能管理*  ・  難易度: 初級

夕凪採取ではAIX 7.3の性能管理で lparstat -i を確認します。夕凪採取の性能管理では pi とsvmon全体表示を点検票へ整理します。夕凪採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。夕凪採取の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、夕凪採取を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lparstat -i 容量確認 pi 0127の設定や表示を読む前に役割を確認します。usrck -n ALL 性能確認 enhanced_RBAC 0128ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはセキュリティでusrck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。
    - B. 対象資源に対する働きはJFS2でsnapを用い・lff とマウントオプションを確認する。
    - C. 対象資源に対する働きは性能管理でlparstat -iを用い・pi とsvmon全体表示を確認する。 ✅
    - D. 対象資源に対する働きはセキュリティでchuserを用い・authorizations とユーザー属性を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「性能管理でlparstat -iを用い、pi とsvmon全体表示を確認する」に対応する項目は容量確認 pi（容量・lpar）です。容量に関する性能管理の仕様は「性能管理でlparstat -iを用い、pi」で、確認対象はlp・容量です。性能・usrcのA:は「セキュリティでusrck -n ALLを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・usrc）です。障害切・snapのB:は「JFS2でsnapを用い、lff とマウントオプションを確認する」を述べ、対象は障害切り分け lff（障害・snap）です。変更前・chusのD:は「セキュリティでchuserを用い、authorizations」を述べ、対象は変更前確認 authorizatio（変更・chus）です。「lparstat -i」は「性能管理でlparstat -iを用い、pi」を指し、容量確認 piではlp・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lparstat -i 容量確認 pi 0127**

    - 検証目的: 性能管理のlparstat -i 容量確認 pi 0127について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認007-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lparstat -i
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0127A
    ```

    画面・出力には AIX0127A が表示され、lparstat -i 容量確認 pi 0127 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0127B
    ```

    画面・出力には AIX0127B が表示され、lparstat -i 容量確認 pi 0127 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0127C
    ```

    画面・出力には AIX0127C が表示され、lparstat -i 容量確認 pi 0127 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0127A が画面・出力に表示されること
    ② ステップ2 の AIX0127B が画面・出力に表示されること
    ③ ステップ3 の AIX0127C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lparstat -i 状態確認 avm 0762 {#c01-i0824}
*分類: 性能管理*  ・  難易度: 中級

春分復旧ではAIX 7.3の性能管理で lparstat -i を確認します。春分復旧の性能管理では avm とvmstat表示を変更票へ記録します。春分復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。春分復旧の注意点として ディスクBusyと待ち時間の混同 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、春分復旧を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lparstat -i 状態確認 avm 0762の役割を調べています。usrck -n ALL 構成照合 audit class 0763の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては性能管理でlparstat -iを用い・avm とvmstat表示を確認する。 ✅
    - B. 機能の説明としてはセキュリティでusrck -n ALLを用い・audit class とロール一覧を確認する。
    - C. 機能の説明としては導入と起動でnimadmを用い・bootlist と代替ディスク状態を確認する。
    - D. 機能の説明としてはLVMでvaryonvgを用い・PP SIZE とボリュームグループ属性を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でlparstat -iを用い、avm とvmstat表示を確認する」に対応する項目は状態確認 avm（状態・lpar）です。状態に関する性能管理の仕様は「性能管理でlparstat -iを用い、avm」で、確認対象はlp・状態です。構成・usrcのB:は「セキュリティでusrck -n ALLを用い、audit」を述べ、対象はaudit class（構成・usrc）です。バック・nimaのC:は「導入と起動でnimadmを用い、bootlist」を述べ、対象はバックアウト確認 bootlist（バッ・nima）です。変更前・varyのD:は「LVMでvaryonvgを用い、PP SIZE」を述べ、対象はPP SIZE（変更・vary）です。「lparstat -i」は「性能管理でlparstat -iを用い、avm」を指し、状態確認 avmではlp・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lparstat -i 状態確認 avm 0762**

    - 検証目的: 性能管理のlparstat -i 状態確認 avm 0762について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認042-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lparstat -i
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0762A
    ```

    画面・出力には AIX0762A が表示され、lparstat -i 状態確認 avm 0762 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0762B
    ```

    画面・出力には AIX0762B が表示され、lparstat -i 状態確認 avm 0762 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0762C
    ```

    画面・出力には AIX0762C が表示され、lparstat -i 状態確認 avm 0762 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0762A が画面・出力に表示されること
    ② ステップ2 の AIX0762B が画面・出力に表示されること
    ③ ステップ3 の AIX0762C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lparstat -i 状態確認 csz 0346 {#c01-i0825}
*分類: 性能管理*  ・  難易度: 上級

陽炎変更ではAIX 7.3の性能管理で lparstat -i を確認します。陽炎変更の性能管理では csz とvmstat表示を保守票へ記録します。陽炎変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。陽炎変更の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、陽炎変更を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lparstat -i 状態確認 csz 0346の役割を調べています。usrck -n ALL 構成照合 authorizations 0347の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は性能管理でlparstat -iを用い・csz とvmstat表示を確認する。 ✅
    - B. 表示や設定で扱う内容はセキュリティでusrck -n ALLを用い・authorizations とロール一覧を確認する。
    - C. 表示や設定で扱う内容はJFS2でsplitcopyを用い・agblksize とログデバイス設定を確認する。
    - D. 表示や設定で扱う内容はLVMでchvgを用い・LV STATE とボリュームグループ属性を確認する。

    正解: **A** ／ 難易度: 上級

    **解説:** Aの記述「性能管理でlparstat -iを用い、csz とvmstat表示を確認する」に対応する項目は状態確認 csz（状態・lpar）です。状態に関する性能管理の仕様は「性能管理でlparstat -iを用い、csz」で、確認対象はlp・状態です。構成・usrcのB:は「セキュリティでusrck -n ALLを用い」を述べ、対象は構成照合 authorization（構成・usrc）です。性能・spliのC:は「JFS2でsplitcopyを用い、agblksize」を述べ、対象は性能確認 agblksize（性能・spli）です。変更後・chvgのD:は「LVMでchvgを用い、LV STATE」を述べ、対象はLV STATE（変更・chvg）です。「lparstat -i」は「性能管理でlparstat -iを用い、csz」を指し、状態確認 cszではlp・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lparstat -i 状態確認 csz 0346**

    - 検証目的: 性能管理のlparstat -i 状態確認 csz 0346について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認106-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lparstat -i
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0346A
    ```

    画面・出力には AIX0346A が表示され、lparstat -i 状態確認 csz 0346 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0346B
    ```

    画面・出力には AIX0346B が表示され、lparstat -i 状態確認 csz 0346 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0346C
    ```

    画面・出力には AIX0346C が表示され、lparstat -i 状態確認 csz 0346 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0346A が画面・出力に表示されること
    ② ステップ2 の AIX0346B が画面・出力に表示されること
    ③ ステップ3 の AIX0346C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lparstat -i 状態確認 fre 0286 {#c01-i0826}
*分類: 性能管理*  ・  難易度: 中級

朝凪復旧ではAIX 7.3の性能管理で lparstat -i を確認します。朝凪復旧の性能管理では fre とvmstat表示を保守票へ記録します。朝凪復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。朝凪復旧の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、朝凪復旧を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lparstat -i 状態確認 fre 0286に関する障害切り分けの前提を確認しています。usrck -n ALL 構成照合 authorizations 0287の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は性能管理でlparstat -iを用い・fre とvmstat表示を確認する。 ✅
    - B. 表示や設定で扱う内容はセキュリティでusrck -n ALLを用い・authorizations とロール一覧を確認する。
    - C. 表示や設定で扱う内容はJFS2でsnapを用い・log=INLINE とログデバイス設定を確認する。
    - D. 表示や設定で扱う内容はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でlparstat -iを用い、fre とvmstat表示を確認する」に対応する項目は状態確認 fre（状態・lpar）です。状態に関する性能管理の仕様は「性能管理でlparstat -iを用い、fre」で、確認対象はlp・状態です。構成・usrcのB:は「セキュリティでusrck -n ALLを用い」を述べ、対象は構成照合 authorization（構成・usrc）です。容量・snapのC:は「JFS2でsnapを用い、log=INLINE」を述べ、対象は容量確認 log=INLINE（容量・snap）です。復旧前・vmstのD:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は復旧前確認 出力見出し（復旧・vmst）です。「lparstat -i」は「性能管理でlparstat -iを用い、fre」を指し、状態確認 freではlp・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lparstat -i 状態確認 fre 0286**

    - 検証目的: 性能管理のlparstat -i 状態確認 fre 0286について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認046-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lparstat -i
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0286A
    ```

    画面・出力には AIX0286A が表示され、lparstat -i 状態確認 fre 0286 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0286B
    ```

    画面・出力には AIX0286B が表示され、lparstat -i 状態確認 fre 0286 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0286C
    ```

    画面・出力には AIX0286C が表示され、lparstat -i 状態確認 fre 0286 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0286A が画面・出力に表示されること
    ② ステップ2 の AIX0286B が画面・出力に表示されること
    ③ ステップ3 の AIX0286C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lparstat -i 状態確認 po 0822 {#c01-i0827}
*分類: 性能管理*  ・  難易度: 上級

紅葉変更ではAIX 7.3の性能管理で lparstat -i を確認します。紅葉変更の性能管理では po とvmstat表示を変更票へ記録します。紅葉変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。紅葉変更の注意点として ディスクBusyと待ち時間の混同 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、紅葉変更を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lparstat -i 状態確認 po 0822に関する障害切り分けの前提を確認しています。lsvg 詳細確認 詳細表示の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては性能管理でlparstat -iを用い・po とvmstat表示を確認する。 ✅
    - B. 機能の説明としてはボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。
    - C. 機能の説明としては性能管理でtopas -Dを用い・fre とAME統計を確認する。
    - D. 機能の説明としてはセキュリティでsetsecattrを用い・enhanced_RBAC と監査設定を確認する。

    正解: **A** ／ 難易度: 上級

    **解説:** 状態・lparでAの記述「性能管理でlparstat -iを用い、po」に対応する項目は状態確認 po（状態・lpar）です。状態に関する性能管理の仕様は「性能管理でlparstat -iを用い、po」で、確認対象はlp・状態です。詳細・詳細・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は詳細確認 詳細表示（詳細・lsvg）です。監査・topaのC:は「性能管理でtopas -Dを用い、fre とAME統計を確認する」を述べ、対象は監査記録 fre（監査・topa）です。性能・setsのD:は「セキュリティでsetsecattrを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・sets）です。「lparstat -i」は「性能管理でlparstat -iを用い、po」を指し、状態確認 poではlp・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lparstat -i 状態確認 po 0822**

    - 検証目的: 性能管理のlparstat -i 状態確認 po 0822について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認102-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lparstat -i
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0822A
    ```

    画面・出力には AIX0822A が表示され、lparstat -i 状態確認 po 0822 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0822B
    ```

    画面・出力には AIX0822B が表示され、lparstat -i 状態確認 po 0822 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0822C
    ```

    画面・出力には AIX0822C が表示され、lparstat -i 状態確認 po 0822 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0822A が画面・出力に表示されること
    ② ステップ2 の AIX0822B が画面・出力に表示されること
    ③ ステップ3 の AIX0822C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lparstat -i 監査記録 Busy% 0792 {#c01-i0828}
*分類: 性能管理*  ・  難易度: 中級

夕映復旧ではAIX 7.3の性能管理で lparstat -i を確認します。夕映復旧の性能管理では Busy% とtopasディスク表示を同じ証跡に残します。夕映復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。夕映復旧の注意点として 初回サンプルだけの誤判定 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、夕映復旧を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lparstat -i 監査記録 Busy% 0792を同一分類のlsvg 詳細確認 詳細表示と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は性能管理でlparstat -iを用い・Busy% とtopasディスク表示を確認する。 ✅
    - B. 構成を確認する際の意味はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。
    - C. 構成を確認する際の意味はLVMでlsvg -lを用い・STALE PARTITIONS とミラーコピー状態を確認する。
    - D. 構成を確認する際の意味は導入と起動でoslevel -sを用い・bootlist とOSレベル表示を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** 監査・lparでAの記述「性能管理でlparstat -iを用い、Busy%」に対応する項目は監査記録 Busy%（監査・lpar）です。監査に関する性能管理の仕様は「性能管理でlparstat -iを用い、Busy%」で、確認対象はlp・監査です。詳細・詳細・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は詳細確認 詳細表示（詳細・lsvg）です。監査・lsvgのC:は「LVMでlsvg -lを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（監査・lsvg）です。変更前・osleのD:は「導入と起動でoslevel -sを用い、bootlist」を述べ、対象は変更前確認 bootlist（変更・osle）です。「lparstat -i」は「性能管理でlparstat -iを用い、Busy%」を指し、監査記録 Busy%ではlp・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lparstat -i 監査記録 Busy% 0792**

    - 検証目的: 性能管理のlparstat -i 監査記録 Busy% 0792について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理監査記録072-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lparstat -i
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0792A
    ```

    画面・出力には AIX0792A が表示され、lparstat -i 監査記録 Busy% 0792 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0792B
    ```

    画面・出力には AIX0792B が表示され、lparstat -i 監査記録 Busy% 0792 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0792C
    ```

    画面・出力には AIX0792C が表示され、lparstat -i 監査記録 Busy% 0792 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0792A が画面・出力に表示されること
    ② ステップ2 の AIX0792B が画面・出力に表示されること
    ③ ステップ3 の AIX0792C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lparstat -i 監査記録 PhysB 0316 {#c01-i0829}
*分類: 性能管理*  ・  難易度: 中級

若潮復旧ではAIX 7.3の性能管理で lparstat -i を確認します。若潮復旧の性能管理では PhysB とtopasディスク表示を監査票へ転記します。若潮復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若潮復旧の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、若潮復旧を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lparstat -i 監査記録 PhysB 0316の技術的な意味を資料で確認するとき、usrck -n ALL 運用引継ぎ authorizations 0317との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はセキュリティでusrck -n ALLを用い・authorizations と監査設定を確認する。
    - B. 管理対象との関係を表す説明はJFS2でsplitcopyを用い・lff とファイルシステム属性を確認する。
    - C. 管理対象との関係を表す説明は性能管理でlparstat -iを用い・PhysB とtopasディスク表示を確認する。 ✅
    - D. 管理対象との関係を表す説明はLVMでchvgを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でlparstat -iを用い、PhysB」に対応する項目は監査記録 PhysB（監査・lpar）です。監査に関する性能管理の仕様は「性能管理でlparstat -iを用い、PhysB」で、確認対象はlp・監査です。運用引・usrcのA:は「セキュリティでusrck -n ALLを用い」を述べ、対象は運用引継ぎ authorizatio（運用・usrc）です。変更後・spliのB:は「JFS2でsplitcopyを用い、lff」を述べ、対象は変更後確認 lff（変更・spli）です。性能・chvgのD:は「LVMでchvgを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（性能・chvg）です。「lparstat -i」は「性能管理でlparstat -iを用い、PhysB」を指し、監査記録 PhysBではlp・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lparstat -i 監査記録 PhysB 0316**

    - 検証目的: 性能管理のlparstat -i 監査記録 PhysB 0316について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理監査記録076-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lparstat -i
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0316A
    ```

    画面・出力には AIX0316A が表示され、lparstat -i 監査記録 PhysB 0316 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0316B
    ```

    画面・出力には AIX0316B が表示され、lparstat -i 監査記録 PhysB 0316 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0316C
    ```

    画面・出力には AIX0316C が表示され、lparstat -i 監査記録 PhysB 0316 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0316A が画面・出力に表示されること
    ② ステップ2 の AIX0316B が画面・出力に表示されること
    ③ ステップ3 の AIX0316C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### lparstat -i 起動確認 PhysB 0475 {#c01-i0830}
*分類: 性能管理*  ・  難易度: 上級

青磁整理ではAIX 7.3の性能管理で lparstat -i を確認します。青磁整理の性能管理では PhysB とsvmon全体表示を点検票へ整理します。青磁整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。青磁整理の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、青磁整理を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** lparstat -i 起動確認 PhysB 0475について構成や状態を確認します。usrck -n ALL 属性確認 authorizations 0476ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはセキュリティでusrck -n ALLを用い・authorizations とユーザー属性を確認する。
    - B. 対象資源に対する働きはJFS2でsplitcopyを用い・agblksize とマウントオプションを確認する。
    - C. 対象資源に対する働きは性能管理でlparstat -iを用い・PhysB とsvmon全体表示を確認する。 ✅
    - D. 対象資源に対する働きはLVMでchvgを用い・VG STATE と論理ボリューム配置を確認する。

    正解: **C** ／ 難易度: 上級

    **解説:** Cの記述「性能管理でlparstat -iを用い、PhysB とsvmon全体表示を確認する」に対応する項目は起動確認 PhysB（起動・lpar）です。起動に関する性能管理の仕様は「性能管理でlparstat -iを用い、PhysB」で、確認対象はlp・起動です。属性・usrcのA:は「セキュリティでusrck -n ALLを用い」を述べ、対象は属性確認 authorization（属性・usrc）です。運用引・spliのB:は「JFS2でsplitcopyを用い、agblksize」を述べ、対象は運用引継ぎ agblksize（運用・spli）です。構成・chvgのD:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（構成・chvg）です。「lparstat -i」は「性能管理でlparstat -iを用い、PhysB」を指し、起動確認 PhysBではlp・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **lparstat -i 起動確認 PhysB 0475**

    - 検証目的: 性能管理のlparstat -i 起動確認 PhysB 0475について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理起動確認115-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> lparstat -i
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0475A
    ```

    画面・出力には AIX0475A が表示され、lparstat -i 起動確認 PhysB 0475 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0475B
    ```

    画面・出力には AIX0475B が表示され、lparstat -i 起動確認 PhysB 0475 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0475C
    ```

    画面・出力には AIX0475C が表示され、lparstat -i 起動確認 PhysB 0475 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0475A が画面・出力に表示されること
    ② ステップ2 の AIX0475B が画面・出力に表示されること
    ③ ステップ3 の AIX0475C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 容量確認 Entitled Capacity 0354 {#c01-i0831}
*分類: 性能管理*  ・  難易度: 上級

銀嶺変更ではAIX 7.3の性能管理で nmon を確認します。銀嶺変更の性能管理では Entitled Capacity とvmstat表示を変更票へ記録します。銀嶺変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。銀嶺変更の注意点として ディスクBusyと待ち時間の混同 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、銀嶺変更を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 容量確認 Entitled Capacity 0354の役割を調べています。lsuser 性能確認 enhanced_RBAC 0355の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としてはセキュリティでlsuserを用い・enhanced_RBAC とロール一覧を確認する。
    - B. 機能の説明としてはJFS2でdf -gを用い・ファイルシステム使用率 とログデバイス設定を確認する。
    - C. 機能の説明としてはLVMでmigratepvを用い・PVID とボリュームグループ属性を確認する。migratepv 属性確認 PVID 0047固有の属性も確認対象に含める。
    - D. 機能の説明としては性能管理でnmonを用い・Entitled Capacity とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「性能管理でnmonを用い、Entitled Capacity」に対応する項目はEntitled Capacity（容量・nmon）です。容量に関する性能管理の仕様は「性能管理でnmonを用い、Entitled Capacity」で、確認対象はnm・容量です。性能・lsusのA:は「セキュリティでlsuserを用い、enhanced_RBAC」を述べ、対象は性能確認 enhanced_RBAC（性能・lsus）です。バック・dfのB:は「JFS2でdf -gを用い、ファイルシステム使用率」を述べ、対象はバックアウト確認 ファイルシステム使（バッ・df）です。属性・migrのC:は「LVMでmigratepvを用い、PVID」を述べ、対象は属性確認 PVID（属性・migr）です。「nmon」は「性能管理でnmonを用い、Entitled Capacity」を指し、Entitled Capacityではnm・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 容量確認 Entitled Capacity 0354**

    - 検証目的: 性能管理のnmon 容量確認 Entitled Capacity 0354について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認114-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0354A
    ```

    画面・出力には AIX0354A が表示され、nmon 容量確認 Entitled Capacity 0354 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0354B
    ```

    画面・出力には AIX0354B が表示され、nmon 容量確認 Entitled Capacity 0354 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0354C
    ```

    画面・出力には AIX0354C が表示され、nmon 容量確認 Entitled Capacity 0354 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0354A が画面・出力に表示されること
    ② ステップ2 の AIX0354B が画面・出力に表示されること
    ③ ステップ3 の AIX0354C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 容量確認 PhysB 0830 {#c01-i0832}
*分類: 性能管理*  ・  難易度: 上級

早苗変更ではAIX 7.3の性能管理で nmon を確認します。早苗変更の性能管理では PhysB とvmstat表示を確認票へ整理します。早苗変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。早苗変更の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、早苗変更を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 容量確認 PhysB 0830に関する障害切り分けの前提を確認しています。lscfg 障害切り分け ページング状態の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は構成済みデバイスと VPD を表示するコマンドである。
    - B. 障害切り分けに用いる役割はデバイス管理でdiag -d ent0を用い・microcode level とODM属性を確認する。
    - C. 障害切り分けに用いる役割はネットワークでroute -n getを用い・Gateway と経路表を確認する。
    - D. 障害切り分けに用いる役割は性能管理でnmonを用い・PhysB とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 容量・nmonでDの記述「性能管理でnmonを用い、PhysB とvmstat表示を確認する」に対応する項目は容量確認 PhysB（容量・nmon）です。容量に関する性能管理の仕様は「性能管理でnmonを用い、PhysB とvmstat表示を確認する」で、確認対象はnm・容量です。障害切・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は障害切り分け ページング状態（障害・lscf）です。容量・diagのB:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（容量・diag）です。障害切・routのC:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・rout）です。「nmon」は「性能管理でnmonを用い、PhysB とvmstat表示を確認する」を指し、容量確認 PhysBではnm・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 容量確認 PhysB 0830**

    - 検証目的: 性能管理のnmon 容量確認 PhysB 0830について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認110-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0830A
    ```

    画面・出力には AIX0830A が表示され、nmon 容量確認 PhysB 0830 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0830B
    ```

    画面・出力には AIX0830B が表示され、nmon 容量確認 PhysB 0830 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0830C
    ```

    画面・出力には AIX0830C が表示され、nmon 容量確認 PhysB 0830 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0830A が画面・出力に表示されること
    ② ステップ2 の AIX0830B が画面・出力に表示されること
    ③ ステップ3 の AIX0830C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 状態確認 Entitled Capacity 0512 {#c01-i0833}
*分類: 性能管理*  ・  難易度: 中級

夕映確認ではAIX 7.3の性能管理で nmon を確認します。夕映確認の性能管理では Entitled Capacity とtopasディスク表示を引継ぎ票へ保管します。夕映確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。夕映確認の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、夕映確認を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 状態確認 Entitled Capacity 0512を同一分類のlsuser 構成照合 authorizations 0513と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は性能管理でnmonを用い・Entitled Capacity とtopasディスク表示を確認する。 ✅
    - B. コマンドまたは機能の用途はセキュリティでlsuserを用い・authorizations と監査設定を確認する。
    - C. コマンドまたは機能の用途はJFS2でfsckを用い・agblksize とファイルシステム属性を確認する。
    - D. コマンドまたは機能の用途はLVMでmirrorvgを用い・LV STATE とミラーコピー状態を確認する。mirrorvg 変更前確認 LV STATE 0205固有の属性も確認対象に含める。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でnmonを用い、Entitled Capacity」に対応する項目はEntitled Capacity（状態・nmon）です。状態に関する性能管理の仕様は「性能管理でnmonを用い、Entitled Capacity」で、確認対象はnm・状態です。構成・lsusのB:は「セキュリティでlsuserを用い、authorizations」を述べ、対象は構成照合 authorization（構成・lsus）です。容量・fsckのC:は「JFS2でfsckを用い、agblksize」を述べ、対象は容量確認 agblksize（容量・fsck）です。変更前・mirrのD:は「LVMでmirrorvgを用い、LV STATE」を述べ、対象はLV STATE（変更・mirr）です。「nmon」は「性能管理でnmonを用い、Entitled Capacity」を指し、Entitled Capacityではnm・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 状態確認 Entitled Capacity 0512**

    - 検証目的: 性能管理のnmon 状態確認 Entitled Capacity 0512について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認032-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0512A
    ```

    画面・出力には AIX0512A が表示され、nmon 状態確認 Entitled Capacity 0512 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0512B
    ```

    画面・出力には AIX0512B が表示され、nmon 状態確認 Entitled Capacity 0512 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0512C
    ```

    画面・出力には AIX0512C が表示され、nmon 状態確認 Entitled Capacity 0512 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0512A が画面・出力に表示されること
    ② ステップ2 の AIX0512B が画面・出力に表示されること
    ③ ステップ3 の AIX0512C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 状態確認 avm 0036 {#c01-i0834}
*分類: 性能管理*  ・  難易度: 中級

若潮確認ではAIX 7.3の性能管理で nmon を確認します。若潮確認の性能管理では avm とtopasディスク表示を同じ証跡に残します。若潮確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若潮確認の注意点として 初回サンプルだけの誤判定 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、若潮確認を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 状態確認 avm 0036の技術的な意味を資料で確認するとき、lsuser 構成照合 user attributes 0037との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はセキュリティでlsuserを用い・user attributes と監査設定を確認する。
    - B. 構成を確認する際の意味はJFS2でfsckを用い・ファイルシステム使用率 とファイルシステム属性を確認する。
    - C. 構成を確認する際の意味は性能管理でnmonを用い・avm とtopasディスク表示を確認する。 ✅
    - D. 構成を確認する際の意味はセキュリティでlssecattr -cを用い・enhanced_RBAC と監査設定を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でnmonを用い、avm とtopasディスク表示を確認する」に対応する項目は状態確認 avm（状態・nmon）です。性能管理の仕様は「性能管理でnmonを用い、avm とtopasディスク表示を確認する」で、確認対象はnm・状態です。構成・lsusのA:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（構成・lsus）です。容量・ファ・fsckのB:は「JFS2でfsckを用い、ファイルシステム使用率」を述べ、対象は容量確認 ファイルシステム使用率（容量・fsck）です。監査・lsseのD:は「セキュリティでlssecattr -cを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsse）です。「nmon」は「性能管理でnmonを用い、avm とtopasディスク表示を確認する」を指し、状態確認 avmではnm・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 状態確認 avm 0036**

    - 検証目的: 性能管理のnmon 状態確認 avm 0036について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認036-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0036A
    ```

    画面・出力には AIX0036A が表示され、nmon 状態確認 avm 0036 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0036B
    ```

    画面・出力には AIX0036B が表示され、nmon 状態確認 avm 0036 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0036C
    ```

    画面・出力には AIX0036C が表示され、nmon 状態確認 avm 0036 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0036A が画面・出力に表示されること
    ② ステップ2 の AIX0036B が画面・出力に表示されること
    ③ ステップ3 の AIX0036C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 監査記録 pi 0482 {#c01-i0835}
*分類: 性能管理*  ・  難易度: 初級

春分確認ではAIX 7.3の性能管理で nmon を確認します。春分確認の性能管理では pi とvmstat表示を確認票へ整理します。春分確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。春分確認の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、春分確認を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 監査記録 pi 0482の役割を調べています。lsuser 運用引継ぎ authorizations 0483の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はセキュリティでlsuserを用い・authorizations とロール一覧を確認する。
    - B. 障害切り分けに用いる役割はJFS2でfsckを用い・lff とログデバイス設定を確認する。
    - C. 障害切り分けに用いる役割は性能管理でnmonを用い・pi とvmstat表示を確認する。 ✅
    - D. 障害切り分けに用いる役割はLVMでmirrorvgを用い・MIRROR WRITE CONSISTENCYである。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「性能管理でnmonを用い、pi とvmstat表示を確認する」に対応する項目は監査記録 pi（監査・nmon）です。監査に関する性能管理の仕様は「性能管理でnmonを用い、pi とvmstat表示を確認する」で、確認対象はnm・監査です。運用引・lsusのA:は「セキュリティでlsuserを用い、authorizations」を述べ、対象は運用引継ぎ authorizatio（運用・lsus）です。変更前・fsckのB:は「JFS2でfsckを用い、lff とログデバイス設定を確認する」を述べ、対象は変更前確認 lff（変更・fsck）です。容量・mirrのD:は「LVMでmirrorvgを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（容量・mirr）です。「nmon」は「性能管理でnmonを用い、pi とvmstat表示を確認する」を指し、監査記録 piではnm・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 監査記録 pi 0482**

    - 検証目的: 性能管理のnmon 監査記録 pi 0482について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理監査記録002-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0482A
    ```

    画面・出力には AIX0482A が表示され、nmon 監査記録 pi 0482 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0482B
    ```

    画面・出力には AIX0482B が表示され、nmon 監査記録 pi 0482 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0482C
    ```

    画面・出力には AIX0482C が表示され、nmon 監査記録 pi 0482 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0482A が画面・出力に表示されること
    ② ステップ2 の AIX0482B が画面・出力に表示されること
    ③ ステップ3 の AIX0482C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 監査記録 po 0006 {#c01-i0836}
*分類: 性能管理*  ・  難易度: 初級

朝凪確認ではAIX 7.3の性能管理で nmon を確認します。朝凪確認の性能管理では po とvmstat表示を変更票へ記録します。朝凪確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。朝凪確認の注意点として ディスクBusyと待ち時間の混同 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、朝凪確認を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 監査記録 po 0006に関する障害切り分けの前提を確認しています。lsuser 運用引継ぎ user attributes 0007の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはセキュリティでlsuserを用い・user attributes とロール一覧を確認する。
    - B. 機能の説明としてはJFS2でfsckを用い・isnapshot とログデバイス設定を確認する。
    - C. 機能の説明としてはセキュリティでlssecattr -cを用い・enhanced_RBAC とロール一覧を確認する。
    - D. 機能の説明としては性能管理でnmonを用い・po とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「性能管理でnmonを用い、po とvmstat表示を確認する」に対応する項目は監査記録 po（監査・nmon）です。性能管理の仕様は「性能管理でnmonを用い、po とvmstat表示を確認する」で、確認対象はnm・監査です。運用引・lsusのA:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（運用・lsus）です。変更前・fsckのB:は「JFS2でfsckを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・fsck）です。状態・lsseのC:は「セキュリティでlssecattr -cを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsse）です。「nmon」は「性能管理でnmonを用い、po とvmstat表示を確認する」を指し、監査記録 poではnm・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 監査記録 po 0006**

    - 検証目的: 性能管理のnmon 監査記録 po 0006について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理監査記録006-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0006A
    ```

    画面・出力には AIX0006A が表示され、nmon 監査記録 po 0006 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0006B
    ```

    画面・出力には AIX0006B が表示され、nmon 監査記録 po 0006 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0006C
    ```

    画面・出力には AIX0006C が表示され、nmon 監査記録 po 0006 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0006A が画面・出力に表示されること
    ② ステップ2 の AIX0006B が画面・出力に表示されること
    ③ ステップ3 の AIX0006C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 起動確認 Busy% 0225 {#c01-i0837}
*分類: 性能管理*  ・  難易度: 上級

花冷保守ではAIX 7.3の性能管理で nmon を確認します。花冷保守の性能管理では Busy% とAME統計を判定票へ残します。花冷保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。花冷保守の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、花冷保守を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「nmon 起動確認 Busy% 0225」を「lsuser 属性確認 user attributes 0226」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割はセキュリティでlsuserを用い・user attributes とRBAC属性を確認する。
    - B. 運用時に利用する技術的役割はJFS2でdf -gを用い・log=INLINE と内部スナップショットを確認する。
    - C. 運用時に利用する技術的役割はセキュリティでlssecattr -cを用い・enhanced_RBAC とRBAC属性を確認する。
    - D. 運用時に利用する技術的役割は性能管理でnmonを用い・Busy% とAME統計を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「性能管理でnmonを用い、Busy% とAME統計を確認する」に対応する項目は起動確認 Busy%（起動・nmon）です。起動に関する性能管理の仕様は「性能管理でnmonを用い、Busy% とAME統計を確認する」で、確認対象はnm・起動です。属性・lsusのA:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（属性・lsus）です。運用引・dfのB:は「JFS2でdf -gを用い、log=INLINE」を述べ、対象は運用引継ぎ log=INLINE（運用・df）です。障害切・lsseのC:は「セキュリティでlssecattr -cを用い」を述べ、対象は障害切り分け enhanced_RB（障害・lsse）です。「nmon」は「性能管理でnmonを用い、Busy% とAME統計を確認する」を指し、起動確認 Busy%ではnm・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 起動確認 Busy% 0225**

    - 検証目的: 性能管理のnmon 起動確認 Busy% 0225について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理起動確認105-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0225A
    ```

    画面・出力には AIX0225A が表示され、nmon 起動確認 Busy% 0225 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0225B
    ```

    画面・出力には AIX0225B が表示され、nmon 起動確認 Busy% 0225 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0225C
    ```

    画面・出力には AIX0225C が表示され、nmon 起動確認 Busy% 0225 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0225A が画面・出力に表示されること
    ② ステップ2 の AIX0225B が画面・出力に表示されること
    ③ ステップ3 の AIX0225C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 起動確認 dxm 0701 {#c01-i0838}
*分類: 性能管理*  ・  難易度: 上級

群青保守ではAIX 7.3の性能管理で nmon を確認します。群青保守の性能管理では dxm とAME統計を復旧票へ残します。群青保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。群青保守の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、群青保守を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 起動確認 dxm 0701を保守記録に説明する必要があります。lsuser 属性確認 authorizations 0702と取り違えない説明はどれですか。

    - A. 仕様上の役割はセキュリティでlsuserを用い・authorizations とRBAC属性を確認する。
    - B. 仕様上の役割は導入と起動でbosboot -a -dを用い・EFIX LABEL とfileset一覧を確認する。
    - C. 仕様上の役割は性能管理でnmonを用い・dxm とAME統計を確認する。 ✅
    - D. 仕様上の役割はLVMでmigratepvを用い・LV STATE と物理ボリューム一覧を確認する。

    正解: **C** ／ 難易度: 上級

    **解説:** Cの記述「性能管理でnmonを用い、dxm とAME統計を確認する」に対応する項目は起動確認 dxm（起動・nmon）です。起動に関する性能管理の仕様は「性能管理でnmonを用い、dxm とAME統計を確認する」で、確認対象はnm・起動です。属性・lsusのA:は「セキュリティでlsuserを用い、authorizations」を述べ、対象は属性確認 authorization（属性・lsus）です。変更後・bosbのB:は「導入と起動でbosboot -a -dを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（変更・bosb）です。構成・migrのD:は「LVMでmigratepvを用い、LV STATE」を述べ、対象はLV STATE（構成・migr）です。「nmon」は「性能管理でnmonを用い、dxm とAME統計を確認する」を指し、起動確認 dxmではnm・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 起動確認 dxm 0701**

    - 検証目的: 性能管理のnmon 起動確認 dxm 0701について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理起動確認101-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0701A
    ```

    画面・出力には AIX0701A が表示され、nmon 起動確認 dxm 0701 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0701B
    ```

    画面・出力には AIX0701B が表示され、nmon 起動確認 dxm 0701 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0701C
    ```

    画面・出力には AIX0701C が表示され、nmon 起動確認 dxm 0701 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0701A が画面・出力に表示されること
    ② ステップ2 の AIX0701B が画面・出力に表示されること
    ③ ステップ3 の AIX0701C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 起動確認 pi 0641 {#c01-i0839}
*分類: 性能管理*  ・  難易度: 中級

白露判定ではAIX 7.3の性能管理で nmon を確認します。白露判定の性能管理では pi とAME統計を復旧票へ残します。白露判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。白露判定の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、白露判定を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「nmon 起動確認 pi 0641」を「lsuser 属性確認 authorizations 0642」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割は性能管理でnmonを用い・pi とAME統計を確認する。 ✅
    - B. 仕様上の役割はセキュリティでlsuserを用い・authorizations とRBAC属性を確認する。
    - C. 仕様上の役割は導入と起動でbosboot -a -dを用い・EFIX LABEL とfileset一覧を確認する。
    - D. 仕様上の役割はLVMでmirrorvgを用い・VG STATE と物理ボリューム一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でnmonを用い、pi とAME統計を確認する」に対応する項目は起動確認 pi（起動・nmon）です。起動に関する性能管理の仕様は「性能管理でnmonを用い、pi とAME統計を確認する」で、確認対象はnm・起動です。属性・lsusのB:は「セキュリティでlsuserを用い、authorizations」を述べ、対象は属性確認 authorization（属性・lsus）です。変更後・bosbのC:は「導入と起動でbosboot -a -dを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（変更・bosb）です。状態・mirrのD:は「LVMでmirrorvgを用い、VG STATE」を述べ、対象はVG STATE（状態・mirr）です。「nmon」は「性能管理でnmonを用い、pi とAME統計を確認する」を指し、起動確認 piではnm・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 起動確認 pi 0641**

    - 検証目的: 性能管理のnmon 起動確認 pi 0641について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理起動確認041-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0641A
    ```

    画面・出力には AIX0641A が表示され、nmon 起動確認 pi 0641 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0641B
    ```

    画面・出力には AIX0641B が表示され、nmon 起動確認 pi 0641 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0641C
    ```

    画面・出力には AIX0641C が表示され、nmon 起動確認 pi 0641 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0641A が画面・出力に表示されること
    ② ステップ2 の AIX0641B が画面・出力に表示されること
    ③ ステップ3 の AIX0641C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 起動確認 po 0165 {#c01-i0840}
*分類: 性能管理*  ・  難易度: 中級

深雪判定ではAIX 7.3の性能管理で nmon を確認します。深雪判定の性能管理では po とAME統計を判定票へ残します。深雪判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。深雪判定の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、深雪判定を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 起動確認 po 0165を保守記録に説明する必要があります。lsuser 属性確認 user attributes 0166と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はセキュリティでlsuserを用い・user attributes とRBAC属性を確認する。
    - B. 運用時に利用する技術的役割は性能管理でnmonを用い・po とAME統計を確認する。 ✅
    - C. 運用時に利用する技術的役割はJFS2でfsckを用い・ファイルシステム使用率 と内部スナップショットを確認する。
    - D. 運用時に利用する技術的役割はセキュリティでlssecattr -cを用い・enhanced_RBAC とRBAC属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でnmonを用い、po とAME統計を確認する」に対応する項目は起動確認 po（起動・nmon）です。起動に関する性能管理の仕様は「性能管理でnmonを用い、po とAME統計を確認する」で、確認対象はnm・起動です。属性・lsusのA:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（属性・lsus）です。監査・ファ・fsckのC:は「JFS2でfsckを用い、ファイルシステム使用率」を述べ、対象は監査記録 ファイルシステム使用率（監査・fsck）です。障害切・lsseのD:は「セキュリティでlssecattr -cを用い」を述べ、対象は障害切り分け enhanced_RB（障害・lsse）です。「nmon」は「性能管理でnmonを用い、po とAME統計を確認する」を指し、起動確認 poではnm・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 起動確認 po 0165**

    - 検証目的: 性能管理のnmon 起動確認 po 0165について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理起動確認045-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0165A
    ```

    画面・出力には AIX0165A が表示され、nmon 起動確認 po 0165 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0165B
    ```

    画面・出力には AIX0165B が表示され、nmon 起動確認 po 0165 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0165C
    ```

    画面・出力には AIX0165C が表示され、nmon 起動確認 po 0165 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0165A が画面・出力に表示されること
    ② ステップ2 の AIX0165B が画面・出力に表示されること
    ③ ステップ3 の AIX0165C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 障害切り分け Busy% 0135 {#c01-i0841}
*分類: 性能管理*  ・  難易度: 初級

岩清水採取ではAIX 7.3の性能管理で nmon を確認します。岩清水採取の性能管理では Busy% とsvmon全体表示を作業票へ保管します。岩清水採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。岩清水採取の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、岩清水採取を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 障害切り分け Busy% 0135の設定や表示を読む前に役割を確認します。lsuser バックアウト確認 user attributes 0136ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは性能管理でnmonを用い・Busy% とsvmon全体表示を確認する。 ✅
    - B. 状態を読み取るための働きはセキュリティでlsuserを用い・user attributes とユーザー属性を確認する。
    - C. 状態を読み取るための働きはJFS2でfsckを用い・isnapshot とマウントオプションを確認する。
    - D. 状態を読み取るための働きはセキュリティでlssecattr -cを用い・enhanced_RBAC とユーザー属性を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でnmonを用い、Busy% とsvmon全体表示を確認する」に対応する項目は障害切り分け Busy%（障害・nmon）です。障害切に関する性能管理の仕様は「性能管理でnmonを用い、Busy% とsvmon全体表示を確認する」で、確認対象はnm・障害切です。バック・lsusのB:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（バッ・lsus）です。状態・fsckのC:は「JFS2でfsckを用い、isnapshot」を述べ、対象は状態確認 isnapshot（状態・fsck）です。起動・lsseのD:は「セキュリティでlssecattr -cを用い」を述べ、対象は起動確認 enhanced_RBAC（起動・lsse）です。「nmon」は「性能管理でnmonを用い、Busy% とsvmon全体表示を確認する」を指し、障害切り分け Busy%ではnm・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 障害切り分け Busy% 0135**

    - 検証目的: 性能管理のnmon 障害切り分け Busy% 0135について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理障害切り分け015-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0135A
    ```

    画面・出力には AIX0135A が表示され、nmon 障害切り分け Busy% 0135 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0135B
    ```

    画面・出力には AIX0135B が表示され、nmon 障害切り分け Busy% 0135 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0135C
    ```

    画面・出力には AIX0135C が表示され、nmon 障害切り分け Busy% 0135 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0135A が画面・出力に表示されること
    ② ステップ2 の AIX0135B が画面・出力に表示されること
    ③ ステップ3 の AIX0135C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 障害切り分け Entitled Capacity 0671 {#c01-i0842}
*分類: 性能管理*  ・  難易度: 中級

遠雷判定ではAIX 7.3の性能管理で nmon を確認します。遠雷判定の性能管理では Entitled Capacity とsvmon全体表示を照合票へ整理します。遠雷判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。遠雷判定の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、遠雷判定を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 障害切り分け Entitled Capacity 0671の設定や表示を読む前に役割を確認します。lsuser バックアウト確認 authorizations 0672ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はセキュリティでlsuserを用い・authorizations とユーザー属性を確認する。
    - B. 一次資料が示す主目的は性能管理でnmonを用い・Entitled Capacity とsvmon全体表示を確認する。 ✅
    - C. 一次資料が示す主目的は導入と起動でbosboot -a -dを用い・mksysb image と起動デバイス設定を確認する。
    - D. 一次資料が示す主目的はLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でnmonを用い、Entitled Capacity」に対応する項目はEntitled Capacity（障害・nmon）です。障害切に関する性能管理の仕様は「性能管理でnmonを用い、Entitled Capacity」で、確認対象はnm・障害切です。バック・lsusのA:は「セキュリティでlsuserを用い、authorizations」を述べ、対象はバックアウト確認 authoriza（バッ・lsus）です。性能・bosbのC:は「導入と起動でbosboot -a -dを用い、mksysb」を述べ、対象はmksysb image（性能・bosb）です。運用引・migrのD:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・migr）です。「nmon」は「性能管理でnmonを用い、Entitled Capacity」を指し、Entitled Capacityではnm・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 障害切り分け Entitled Capacity 0671**

    - 検証目的: 性能管理のnmon 障害切り分け Entitled Capacity 0671について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理障害切り分け071-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0671A
    ```

    画面・出力には AIX0671A が表示され、nmon 障害切り分け Entitled Capacity 0671 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0671B
    ```

    画面・出力には AIX0671B が表示され、nmon 障害切り分け Entitled Capacity 0671 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0671C
    ```

    画面・出力には AIX0671C が表示され、nmon 障害切り分け Entitled Capacity 0671 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0671A が画面・出力に表示されること
    ② ステップ2 の AIX0671B が画面・出力に表示されること
    ③ ステップ3 の AIX0671C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 障害切り分け avm 0195 {#c01-i0843}
*分類: 性能管理*  ・  難易度: 中級

青磁判定ではAIX 7.3の性能管理で nmon を確認します。青磁判定の性能管理では avm とsvmon全体表示を作業票へ保管します。青磁判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。青磁判定の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、青磁判定を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 障害切り分け avm 0195について構成や状態を確認します。lsuser バックアウト確認 user attributes 0196ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはセキュリティでlsuserを用い・user attributes とユーザー属性を確認する。
    - B. 状態を読み取るための働きは性能管理でnmonを用い・avm とsvmon全体表示を確認する。 ✅
    - C. 状態を読み取るための働きはJFS2でdf -gを用い・mountguard とマウントオプションを確認する。
    - D. 状態を読み取るための働きはセキュリティでlssecattr -cを用い・enhanced_RBAC とユーザー属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でnmonを用い、avm とsvmon全体表示を確認する」に対応する項目は障害切り分け avm（障害・nmon）です。障害切に関する性能管理の仕様は「性能管理でnmonを用い、avm とsvmon全体表示を確認する」で、確認対象はnm・障害切です。バック・lsusのA:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（バッ・lsus）です。構成・dfのC:は「JFS2でdf -gを用い、mountguard」を述べ、対象は構成照合 mountguard（構成・df）です。起動・lsseのD:は「セキュリティでlssecattr -cを用い」を述べ、対象は起動確認 enhanced_RBAC（起動・lsse）です。「nmon」は「性能管理でnmonを用い、avm とsvmon全体表示を確認する」を指し、障害切り分け avmではnm・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 障害切り分け avm 0195**

    - 検証目的: 性能管理のnmon 障害切り分け avm 0195について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理障害切り分け075-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0195A
    ```

    画面・出力には AIX0195A が表示され、nmon 障害切り分け avm 0195 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0195B
    ```

    画面・出力には AIX0195B が表示され、nmon 障害切り分け avm 0195 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0195C
    ```

    画面・出力には AIX0195C が表示され、nmon 障害切り分け avm 0195 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0195A が画面・出力に表示されること
    ② ステップ2 の AIX0195B が画面・出力に表示されること
    ③ ステップ3 の AIX0195C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### nmon 障害切り分け dxm 0611 {#c01-i0844}
*分類: 性能管理*  ・  難易度: 初級

松風採取ではAIX 7.3の性能管理で nmon を確認します。松風採取の性能管理では dxm とsvmon全体表示を照合票へ整理します。松風採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。松風採取の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、松風採取を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** nmon 障害切り分け dxm 0611について構成や状態を確認します。lsuser バックアウト確認 authorizations 0612ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はセキュリティでlsuserを用い・authorizations とユーザー属性を確認する。
    - B. 一次資料が示す主目的はデバイス属性を変更する管理コマンドである。
    - C. 一次資料が示す主目的はLVMでmirrorvgを用い・STALE PARTITIONS と論理ボリューム配置を確認する。
    - D. 一次資料が示す主目的は性能管理でnmonを用い・dxm とsvmon全体表示を確認する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「性能管理でnmonを用い、dxm とsvmon全体表示を確認する」に対応する項目は障害切り分け dxm（障害・nmon）です。障害切に関する性能管理の仕様は「性能管理でnmonを用い、dxm とsvmon全体表示を確認する」で、確認対象はnm・障害切です。バック・lsusのA:は「セキュリティでlsuserを用い、authorizations」を述べ、対象はバックアウト確認 authoriza（バッ・lsus）です。属性・ボリ・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は属性照合 ボリューム状態（属性・chde）です。監査・mirrのC:は「LVMでmirrorvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（監査・mirr）です。「nmon」は「性能管理でnmonを用い、dxm とsvmon全体表示を確認する」を指し、障害切り分け dxmではnm・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **nmon 障害切り分け dxm 0611**

    - 検証目的: 性能管理のnmon 障害切り分け dxm 0611について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理障害切り分け011-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> nmon
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0611A
    ```

    画面・出力には AIX0611A が表示され、nmon 障害切り分け dxm 0611 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0611B
    ```

    画面・出力には AIX0611B が表示され、nmon 障害切り分け dxm 0611 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0611C
    ```

    画面・出力には AIX0611C が表示され、nmon 障害切り分け dxm 0611 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0611A が画面・出力に表示されること
    ② ステップ2 の AIX0611B が画面・出力に表示されること
    ③ ステップ3 の AIX0611C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### svmon -G 状態確認 Entitled Capacity 0369 {#c01-i0845}
*分類: 性能管理*  ・  難易度: 初級

銀砂記録ではAIX 7.3の性能管理で svmon -G を確認します。銀砂記録の性能管理では Entitled Capacity とAME統計を判定票へ残します。銀砂記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。銀砂記録の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、銀砂記録を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「svmon -G 状態確認 Entitled Capacity 0369」を「rbacqry -u user1 -T 構成照合 audit class 0370」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は性能管理でsvmon -Gを用い・Entitled Capacity とAME統計を確認する。 ✅
    - B. 運用時に利用する技術的役割はセキュリティでrbacqry -u user1 -Tを用い・audit class とRBAC属性を確認する。
    - C. 運用時に利用する技術的役割はJFS2でcrfsを用い・agblksize と内部スナップショットを確認する。
    - D. 運用時に利用する技術的役割はLVMでlsvg -lを用い・VG STATE と物理ボリューム一覧を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でsvmon -Gを用い、Entitled Capacity」に対応する項目はEntitled Capacity（状態・svmo）です。状態に関する性能管理の仕様は「性能管理でsvmon -Gを用い、Entitled」で、確認対象はsv・状態です。構成・rbacのB:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（構成・rbac）です。容量・crfsのC:は「JFS2でcrfsを用い、agblksize」を述べ、対象は容量確認 agblksize（容量・crfs）です。変更前・lsvgのD:は「LVMでlsvg -lを用い、VG STATE」を述べ、対象はVG STATE（変更・lsvg）です。「svmon -G」は「性能管理でsvmon -Gを用い、Entitled」を指し、Entitled Capacityではsv・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **svmon -G 状態確認 Entitled Capacity 0369**

    - 検証目的: 性能管理のsvmon -G 状態確認 Entitled Capacity 0369について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認009-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0369A
    ```

    画面・出力には AIX0369A が表示され、svmon -G 状態確認 Entitled Capacity 0369 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0369B
    ```

    画面・出力には AIX0369B が表示され、svmon -G 状態確認 Entitled Capacity 0369 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0369C
    ```

    画面・出力には AIX0369C が表示され、svmon -G 状態確認 Entitled Capacity 0369 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0369A が画面・出力に表示されること
    ② ステップ2 の AIX0369B が画面・出力に表示されること
    ③ ステップ3 の AIX0369C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### svmon -G 状態確認 pi 0429 {#c01-i0846}
*分類: 性能管理*  ・  難易度: 中級

梅雨晴評価ではAIX 7.3の性能管理で svmon -G を確認します。梅雨晴評価の性能管理では pi とAME統計を判定票へ残します。梅雨晴評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。梅雨晴評価の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、梅雨晴評価を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** svmon -G 状態確認 pi 0429を保守記録に説明する必要があります。rbacqry -u user1 -T 構成照合 audit class 0430と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割はセキュリティでrbacqry -u user1 -Tを用い・audit class とRBAC属性を確認する。
    - B. 運用時に利用する技術的役割は性能管理でsvmon -Gを用い・pi とAME統計を確認する。 ✅
    - C. 運用時に利用する技術的役割はJFS2でchfsを用い・isnapshot と内部スナップショットを確認する。
    - D. 運用時に利用する技術的役割はLVMでlslvを用い・LV STATE と物理ボリューム一覧を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でsvmon -Gを用い、pi とAME統計を確認する」に対応する項目は状態確認 pi（状態・svmo）です。状態に関する性能管理の仕様は「性能管理でsvmon -Gを用い、pi とAME統計を確認する」で、確認対象はsv・状態です。構成・rbacのA:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（構成・rbac）です。性能・chfsのC:は「JFS2でchfsを用い、isnapshot」を述べ、対象は性能確認 isnapshot（性能・chfs）です。変更後・lslvのD:は「LVMでlslvを用い、LV STATE」を述べ、対象はLV STATE（変更・lslv）です。「svmon -G」は「性能管理でsvmon -Gを用い、pi とAME統計を確認する」を指し、状態確認 piではsv・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **svmon -G 状態確認 pi 0429**

    - 検証目的: 性能管理のsvmon -G 状態確認 pi 0429について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認069-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0429A
    ```

    画面・出力には AIX0429A が表示され、svmon -G 状態確認 pi 0429 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0429B
    ```

    画面・出力には AIX0429B が表示され、svmon -G 状態確認 pi 0429 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0429C
    ```

    画面・出力には AIX0429C が表示され、svmon -G 状態確認 pi 0429 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0429A が画面・出力に表示されること
    ② ステップ2 の AIX0429B が画面・出力に表示されること
    ③ ステップ3 の AIX0429C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### svmon -G 監査記録 dxm 0399 {#c01-i0847}
*分類: 性能管理*  ・  難易度: 中級

秋桜記録ではAIX 7.3の性能管理で svmon -G を確認します。秋桜記録の性能管理では dxm とsvmon全体表示を作業票へ保管します。秋桜記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。秋桜記録の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、秋桜記録を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** svmon -G 監査記録 dxm 0399の設定や表示を読む前に役割を確認します。rbacqry -u user1 -T 運用引継ぎ audit class 0400ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは性能管理でsvmon -Gを用い・dxm とsvmon全体表示を確認する。 ✅
    - B. 状態を読み取るための働きはセキュリティでrbacqry -u user1 -Tを用い・audit class とユーザー属性を確認する。
    - C. 状態を読み取るための働きはJFS2でcrfsを用い・lff とマウントオプションを確認する。
    - D. 状態を読み取るための働きはLVMでlsvg -lを用い・STALE PARTITIONS と論理ボリューム配置を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でsvmon -Gを用い、dxm とsvmon全体表示を確認する」に対応する項目は監査記録 dxm（監査・svmo）です。監査に関する性能管理の仕様は「性能管理でsvmon -Gを用い、dxm」で、確認対象はsv・監査です。運用引・rbacのB:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（運用・rbac）です。変更前・crfsのC:は「JFS2でcrfsを用い、lff とマウントオプションを確認する」を述べ、対象は変更前確認 lff（変更・crfs）です。容量・lsvgのD:は「LVMでlsvg -lを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（容量・lsvg）です。「svmon -G」は「性能管理でsvmon -Gを用い、dxm」を指し、監査記録 dxmではsv・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **svmon -G 監査記録 dxm 0399**

    - 検証目的: 性能管理のsvmon -G 監査記録 dxm 0399について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理監査記録039-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0399A
    ```

    画面・出力には AIX0399A が表示され、svmon -G 監査記録 dxm 0399 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0399B
    ```

    画面・出力には AIX0399B が表示され、svmon -G 監査記録 dxm 0399 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0399C
    ```

    画面・出力には AIX0399C が表示され、svmon -G 監査記録 dxm 0399 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0399A が画面・出力に表示されること
    ② ステップ2 の AIX0399B が画面・出力に表示されること
    ③ ステップ3 の AIX0399C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### svmon -G 起動確認 csz 0558 {#c01-i0848}
*分類: 性能管理*  ・  難易度: 中級

春霞照合ではAIX 7.3の性能管理で svmon -G を確認します。春霞照合の性能管理では csz とvmstat表示を変更票へ記録します。春霞照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。春霞照合の注意点として ディスクBusyと待ち時間の混同 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、春霞照合を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** svmon -G 起動確認 csz 0558に関する障害切り分けの前提を確認しています。rbacqry -u user1 -T 属性確認 user attributesの機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはセキュリティでrbacqry -u user1 -Tを用い・user attributesである。
    - B. 機能の説明としては性能管理でsvmon -Gを用い・csz とvmstat表示を確認する。 ✅
    - C. 機能の説明としてはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。
    - D. 機能の説明としてはLVMでlslvを用い・LV STATE とボリュームグループ属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でsvmon -Gを用い、csz とvmstat表示を確認する」に対応する項目は起動確認 csz（起動・svmo）です。起動に関する性能管理の仕様は「性能管理でsvmon -Gを用い、csz」で、確認対象はsv・起動です。属性・rbacのA:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はuser attributes（属性・rbac）です。詳細・メッ・lspsのC:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は詳細確認 メッセージ行（詳細・lsps）です。構成・lslvのD:は「LVMでlslvを用い、LV STATE」を述べ、対象はLV STATE（構成・lslv）です。「svmon -G」は「性能管理でsvmon -Gを用い、csz」を指し、起動確認 cszではsv・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **svmon -G 起動確認 csz 0558**

    - 検証目的: 性能管理のsvmon -G 起動確認 csz 0558について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理起動確認078-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0558A
    ```

    画面・出力には AIX0558A が表示され、svmon -G 起動確認 csz 0558 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0558B
    ```

    画面・出力には AIX0558B が表示され、svmon -G 起動確認 csz 0558 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0558C
    ```

    画面・出力には AIX0558C が表示され、svmon -G 起動確認 csz 0558 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0558A が画面・出力に表示されること
    ② ステップ2 の AIX0558B が画面・出力に表示されること
    ③ ステップ3 の AIX0558C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### svmon -G 起動確認 dxm 0082 {#c01-i0849}
*分類: 性能管理*  ・  難易度: 中級

春分点検ではAIX 7.3の性能管理で svmon -G を確認します。春分点検の性能管理では dxm とvmstat表示を保守票へ記録します。春分点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。春分点検の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、春分点検を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** svmon -G 起動確認 dxm 0082の役割を調べています。rbacqry -u user1 -T 属性確認 roles 0083の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は性能管理でsvmon -Gを用い・dxm とvmstat表示を確認する。 ✅
    - B. 表示や設定で扱う内容はセキュリティでrbacqry -u user1 -Tを用い・roles とロール一覧を確認する。
    - C. 表示や設定で扱う内容はJFS2でchfsを用い・ファイルシステム使用率 とログデバイス設定を確認する。
    - D. 表示や設定で扱う内容はセキュリティでlsattr -E -l sys0 -aを用い・audit class とロール一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でsvmon -Gを用い、dxm とvmstat表示を確認する」に対応する項目は起動確認 dxm（起動・svmo）です。起動に関する性能管理の仕様は「性能管理でsvmon -Gを用い、dxm」で、確認対象はsv・起動です。属性・rbacのB:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象は属性確認 roles（属性・rbac）です。運用引・chfsのC:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象は運用引継ぎ ファイルシステム使用率（運用・chfs）です。障害切・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象はaudit class（障害・lsat）です。「svmon -G」は「性能管理でsvmon -Gを用い、dxm」を指し、起動確認 dxmではsv・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **svmon -G 起動確認 dxm 0082**

    - 検証目的: 性能管理のsvmon -G 起動確認 dxm 0082について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理起動確認082-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0082A
    ```

    画面・出力には AIX0082A が表示され、svmon -G 起動確認 dxm 0082 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0082B
    ```

    画面・出力には AIX0082B が表示され、svmon -G 起動確認 dxm 0082 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0082C
    ```

    画面・出力には AIX0082C が表示され、svmon -G 起動確認 dxm 0082 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0082A が画面・出力に表示されること
    ② ステップ2 の AIX0082B が画面・出力に表示されること
    ③ ステップ3 の AIX0082C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### svmon -G 障害切り分け fre 0588 {#c01-i0850}
*分類: 性能管理*  ・  難易度: 上級

雪解点検ではAIX 7.3の性能管理で svmon -G を確認します。雪解点検の性能管理では fre とtopasディスク表示を同じ証跡に残します。雪解点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。雪解点検の注意点として 初回サンプルだけの誤判定 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、雪解点検を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** svmon -G 障害切り分け fre 0588の技術的な意味を資料で確認するとき、rbacqry -u user1 -T バックアウト確認 userとの境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はセキュリティでrbacqry -u user1 -Tを用い・user attributesである。
    - B. 構成を確認する際の意味はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。
    - C. 構成を確認する際の意味は性能管理でsvmon -Gを用い・fre とtopasディスク表示を確認する。 ✅
    - D. 構成を確認する際の意味はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。

    正解: **C** ／ 難易度: 上級

    **解説:** Cの記述「性能管理でsvmon -Gを用い、fre とtopasディスク表示を確認する」に対応する項目は障害切り分け fre（障害・svmo）です。障害切に関する性能管理の仕様は「性能管理でsvmon -Gを用い、fre」で、確認対象はsv・障害切です。バック・rbacのA:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はuser attributes（バッ・rbac）です。状態・属性・lspsのB:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は状態判定 属性確認（状態・lsps）です。運用引・lslvのD:は「LVMでlslvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・lslv）です。「svmon -G」は「性能管理でsvmon -Gを用い、fre」を指し、障害切り分け freではsv・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **svmon -G 障害切り分け fre 0588**

    - 検証目的: 性能管理のsvmon -G 障害切り分け fre 0588について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理障害切り分け108-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0588A
    ```

    画面・出力には AIX0588A が表示され、svmon -G 障害切り分け fre 0588 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0588B
    ```

    画面・出力には AIX0588B が表示され、svmon -G 障害切り分け fre 0588 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0588C
    ```

    画面・出力には AIX0588C が表示され、svmon -G 障害切り分け fre 0588 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0588A が画面・出力に表示されること
    ② ステップ2 の AIX0588B が画面・出力に表示されること
    ③ ステップ3 の AIX0588C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### svmon -G 障害切り分け pi 0112 {#c01-i0851}
*分類: 性能管理*  ・  難易度: 上級

夕映点検ではAIX 7.3の性能管理で svmon -G を確認します。夕映点検の性能管理では pi とtopasディスク表示を監査票へ転記します。夕映点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。夕映点検の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、夕映点検を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** svmon -G 障害切り分け pi 0112を同一分類のrbacqry -u user1 -T バックアウト確認 roles 0113と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はセキュリティでrbacqry -u user1 -Tを用い・roles と監査設定を確認する。
    - B. 管理対象との関係を表す説明はJFS2でchfsを用い・isnapshot とファイルシステム属性を確認する。
    - C. 管理対象との関係を表す説明はセキュリティでlsroleを用い・user attributes と監査設定を確認する。
    - D. 管理対象との関係を表す説明は性能管理でsvmon -Gを用い・pi とtopasディスク表示を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「性能管理でsvmon -Gを用い、pi とtopasディスク表示を確認する」に対応する項目は障害切り分け pi（障害・svmo）です。障害切に関する性能管理の仕様は「性能管理でsvmon -Gを用い、pi とtopasディスク表示を確」で、確認対象はsv・障害切です。バック・rbacのA:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はバックアウト確認 roles（バッ・rbac）です。構成・chfsのB:は「JFS2でchfsを用い、isnapshot」を述べ、対象は構成照合 isnapshot（構成・chfs）です。属性・lsroのC:は「セキュリティでlsroleを用い、user attributes」を述べ、対象はuser attributes（属性・lsro）です。「svmon -G」は「性能管理でsvmon -Gを用い、pi とtopasディスク表示を確」を指し、障害切り分け piではsv・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **svmon -G 障害切り分け pi 0112**

    - 検証目的: 性能管理のsvmon -G 障害切り分け pi 0112について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理障害切り分け112-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0112A
    ```

    画面・出力には AIX0112A が表示され、svmon -G 障害切り分け pi 0112 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0112B
    ```

    画面・出力には AIX0112B が表示され、svmon -G 障害切り分け pi 0112 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0112C
    ```

    画面・出力には AIX0112C が表示され、svmon -G 障害切り分け pi 0112 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0112A が画面・出力に表示されること
    ② ステップ2 の AIX0112B が画面・出力に表示されること
    ③ ステップ3 の AIX0112C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -C バックアウト確認 PhysB 0422 {#c01-i0852}
*分類: 性能管理*  ・  難易度: 中級

紅葉評価ではAIX 7.3の性能管理で topas -C を確認します。紅葉評価の性能管理では PhysB とvmstat表示を確認票へ整理します。紅葉評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。紅葉評価の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、紅葉評価を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -C バックアウト確認 PhysB 0422に関する障害切り分けの前提を確認しています。chuser 監査記録 enhanced_RBAC 0423の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割はセキュリティでchuserを用い・enhanced_RBAC とロール一覧を確認する。
    - B. 障害切り分けに用いる役割はJFS2でfsckを用い・lff とログデバイス設定を確認する。
    - C. 障害切り分けに用いる役割はLVMでchlvを用い・STALE PARTITIONS とボリュームグループ属性を確認する。
    - D. 障害切り分けに用いる役割は性能管理でtopas -Cを用い・PhysB とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でtopas -Cを用い、PhysB とvmstat表示を確認する」に対応する項目はバックアウト確認 PhysB（バッ・topa）です。バックに関する性能管理の仕様は「性能管理でtopas -Cを用い、PhysB」で、確認対象はto・バックです。監査・chusのA:は「セキュリティでchuserを用い、enhanced_RBAC」を述べ、対象は監査記録 enhanced_RBAC（監査・chus）です。変更前・fsckのB:は「JFS2でfsckを用い、lff とログデバイス設定を確認する」を述べ、対象は変更前確認 lff（変更・fsck）です。運用引・chlvのC:は「LVMでchlvを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（運用・chlv）です。「topas -C」は「性能管理でtopas -Cを用い、PhysB」を指し、バックアウト確認 PhysBではto・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -C バックアウト確認 PhysB 0422**

    - 検証目的: 性能管理のtopas -C バックアウト確認 PhysB 0422について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認062-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0422A
    ```

    画面・出力には AIX0422A が表示され、topas -C バックアウト確認 PhysB 0422 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0422B
    ```

    画面・出力には AIX0422B が表示され、topas -C バックアウト確認 PhysB 0422 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0422C
    ```

    画面・出力には AIX0422C が表示され、topas -C バックアウト確認 PhysB 0422 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0422A が画面・出力に表示されること
    ② ステップ2 の AIX0422B が画面・出力に表示されること
    ③ ステップ3 の AIX0422C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -C 属性確認 csz 0452 {#c01-i0853}
*分類: 性能管理*  ・  難易度: 中級

水音整理ではAIX 7.3の性能管理で topas -C を確認します。水音整理の性能管理では csz とtopasディスク表示を引継ぎ票へ保管します。水音整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。水音整理の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、水音整理を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -C 属性確認 csz 0452の技術的な意味を資料で確認するとき、chuser 状態確認 enhanced_RBAC 0453との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はセキュリティでchuserを用い・enhanced_RBAC と監査設定を確認する。
    - B. コマンドまたは機能の用途はJFS2でfsckを用い・agblksize とファイルシステム属性を確認する。
    - C. コマンドまたは機能の用途は性能管理でtopas -Cを用い・csz とtopasディスク表示を確認する。 ✅
    - D. コマンドまたは機能の用途はLVMでmirrorvgを用い・LV STATE とミラーコピー状態を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でtopas -Cを用い、csz とtopasディスク表示を確認する」に対応する項目は属性確認 csz（属性・topa）です。属性に関する性能管理の仕様は「性能管理でtopas -Cを用い、csz」で、確認対象はto・属性です。状態・chusのA:は「セキュリティでchuserを用い、enhanced_RBAC」を述べ、対象は状態確認 enhanced_RBAC（状態・chus）です。容量・fsckのB:は「JFS2でfsckを用い、agblksize」を述べ、対象は容量確認 agblksize（容量・fsck）です。変更前・mirrのD:は「LVMでmirrorvgを用い、LV STATE」を述べ、対象はLV STATE（変更・mirr）です。「topas -C」は「性能管理でtopas -Cを用い、csz」を指し、属性確認 cszではto・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -C 属性確認 csz 0452**

    - 検証目的: 性能管理のtopas -C 属性確認 csz 0452について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理属性確認092-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0452A
    ```

    画面・出力には AIX0452A が表示され、topas -C 属性確認 csz 0452 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0452B
    ```

    画面・出力には AIX0452B が表示され、topas -C 属性確認 csz 0452 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0452C
    ```

    画面・出力には AIX0452C が表示され、topas -C 属性確認 csz 0452 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0452A が画面・出力に表示されること
    ② ステップ2 の AIX0452B が画面・出力に表示されること
    ③ ステップ3 の AIX0452C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -C 構成照合 Entitled Capacity 0263 {#c01-i0854}
*分類: 性能管理*  ・  難易度: 中級

新緑監査ではAIX 7.3の性能管理で topas -C を確認します。新緑監査の性能管理では Entitled Capacity とsvmon全体表示を照合票へ整理します。新緑監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。新緑監査の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、新緑監査を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -C 構成照合 Entitled Capacity 0263の設定や表示を読む前に役割を確認します。chuser 変更前確認 user attributes 0264ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は性能管理でtopas -Cを用い・Entitled Capacity とsvmon全体表示を確認する。 ✅
    - B. 一次資料が示す主目的はセキュリティでchuserを用い・user attributes とユーザー属性を確認する。
    - C. 一次資料が示す主目的はJFS2でmount -o remountを用い・agblksize とマウントオプションを確認する。mount -o remount 性能確認 agblksize 0569固有の属性も確認対象に含める。
    - D. 一次資料が示す主目的はデバイスや sys0 などの属性値を表示するコマンドである。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Cを用い、Entitled Capacity」に対応する項目はEntitled Capacity（構成・topa）です。構成に関する性能管理の仕様は「性能管理でtopas -Cを用い、Entitled」で、確認対象はto・構成です。変更前・chusのB:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（変更・chus）です。性能・mounのC:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 agblksize（性能・moun）です。変更前・lsatのD:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は変更前確認 パス状態（変更・lsat）です。「topas -C」は「性能管理でtopas -Cを用い、Entitled」を指し、Entitled Capacityではto・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -C 構成照合 Entitled Capacity 0263**

    - 検証目的: 性能管理のtopas -C 構成照合 Entitled Capacity 0263について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合023-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0263A
    ```

    画面・出力には AIX0263A が表示され、topas -C 構成照合 Entitled Capacity 0263 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0263B
    ```

    画面・出力には AIX0263B が表示され、topas -C 構成照合 Entitled Capacity 0263 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0263C
    ```

    画面・出力には AIX0263C が表示され、topas -C 構成照合 Entitled Capacity 0263 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0263A が画面・出力に表示されること
    ② ステップ2 の AIX0263B が画面・出力に表示されること
    ③ ステップ3 の AIX0263C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -C 構成照合 PhysB 0739 {#c01-i0855}
*分類: 性能管理*  ・  難易度: 初級

山吹監査ではAIX 7.3の性能管理で topas -C を確認します。山吹監査の性能管理では PhysB とsvmon全体表示を点検票へ整理します。山吹監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。山吹監査の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、山吹監査を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -C 構成照合 PhysB 0739について構成や状態を確認します。chuser 変更前確認 authorizations 0740ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きは性能管理でtopas -Cを用い・PhysB とsvmon全体表示を確認する。 ✅
    - B. 対象資源に対する働きはセキュリティでchuserを用い・authorizations とユーザー属性を確認する。
    - C. 対象資源に対する働きは導入と起動でmksysbを用い・altinst_rootvg と起動デバイス設定を確認する。
    - D. 対象資源に対する働きはLVMでchlvを用い・PP SIZE と論理ボリューム配置を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でtopas -Cを用い、PhysB とsvmon全体表示を確認する」に対応する項目は構成照合 PhysB（構成・topa）です。構成に関する性能管理の仕様は「性能管理でtopas -Cを用い、PhysB」で、確認対象はto・構成です。変更前・chusのB:は「セキュリティでchuserを用い、authorizations」を述べ、対象は変更前確認 authorizatio（変更・chus）です。監査・mksyのC:は「導入と起動でmksysbを用い、altinst_rootvg」を述べ、対象は監査記録 altinst_rootv（監査・mksy）です。変更後・chlvのD:は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」を述べ、対象はPP SIZE（変更・chlv）です。「topas -C」は「性能管理でtopas -Cを用い、PhysB」を指し、構成照合 PhysBではto・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -C 構成照合 PhysB 0739**

    - 検証目的: 性能管理のtopas -C 構成照合 PhysB 0739について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合019-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0739A
    ```

    画面・出力には AIX0739A が表示され、topas -C 構成照合 PhysB 0739 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0739B
    ```

    画面・出力には AIX0739B が表示され、topas -C 構成照合 PhysB 0739 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0739C
    ```

    画面・出力には AIX0739C が表示され、topas -C 構成照合 PhysB 0739 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0739A が画面・出力に表示されること
    ② ステップ2 の AIX0739B が画面・出力に表示されること
    ③ ステップ3 の AIX0739C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -C 運用引継ぎ csz 0769 {#c01-i0856}
*分類: 性能管理*  ・  難易度: 中級

銀砂復旧ではAIX 7.3の性能管理で topas -C を確認します。銀砂復旧の性能管理では csz とAME統計を採取票へ記録します。銀砂復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。銀砂復旧の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、銀砂復旧を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「topas -C 運用引継ぎ csz 0769」を「chuser 容量確認 authorizations 0770」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は性能管理でtopas -Cを用い・csz とAME統計を確認する。 ✅
    - B. 保守作業で参照する機能はセキュリティでchuserを用い・authorizations とRBAC属性を確認する。
    - C. 保守作業で参照する機能は導入と起動でmksysbを用い・fileset level とfileset一覧を確認する。
    - D. 保守作業で参照する機能はLVMでchlvを用い・PVID と物理ボリューム一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Cを用い、csz とAME統計を確認する」に対応する項目は運用引継ぎ csz（運用・topa）です。運用引に関する性能管理の仕様は「性能管理でtopas -Cを用い、csz とAME統計を確認する」で、確認対象はto・運用引です。容量・chusのB:は「セキュリティでchuserを用い、authorizations」を述べ、対象は容量確認 authorization（容量・chus）です。状態・mksyのC:は「導入と起動でmksysbを用い、fileset level」を述べ、対象はfileset level（状態・mksy）です。性能・chlvのD:は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は性能確認 PVID（性能・chlv）です。「topas -C」は「性能管理でtopas -Cを用い、csz とAME統計を確認する」を指し、運用引継ぎ cszではto・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -C 運用引継ぎ csz 0769**

    - 検証目的: 性能管理のtopas -C 運用引継ぎ csz 0769について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ049-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0769A
    ```

    画面・出力には AIX0769A が表示され、topas -C 運用引継ぎ csz 0769 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0769B
    ```

    画面・出力には AIX0769B が表示され、topas -C 運用引継ぎ csz 0769 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0769C
    ```

    画面・出力には AIX0769C が表示され、topas -C 運用引継ぎ csz 0769 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0769A が画面・出力に表示されること
    ② ステップ2 の AIX0769B が画面・出力に表示されること
    ③ ステップ3 の AIX0769C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -C 運用引継ぎ dxm 0293 {#c01-i0857}
*分類: 性能管理*  ・  難易度: 中級

月影復旧ではAIX 7.3の性能管理で topas -C を確認します。月影復旧の性能管理では dxm とAME統計を復旧票へ残します。月影復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。月影復旧の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、月影復旧を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -C 運用引継ぎ dxm 0293を保守記録に説明する必要があります。chuser 容量確認 user attributes 0294と取り違えない説明はどれですか。

    - A. 仕様上の役割はセキュリティでchuserを用い・user attributes とRBAC属性を確認する。
    - B. 仕様上の役割はJFS2でmount -o remountを用い・lff と内部スナップショットを確認する。
    - C. 仕様上の役割はデバイスや sys0 などの属性値を表示するコマンドである。
    - D. 仕様上の役割は性能管理でtopas -Cを用い・dxm とAME統計を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でtopas -Cを用い、dxm とAME統計を確認する」に対応する項目は運用引継ぎ dxm（運用・topa）です。運用引に関する性能管理の仕様は「性能管理でtopas -Cを用い、dxm とAME統計を確認する」で、確認対象はto・運用引です。容量・chusのA:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（容量・chus）です。変更後・mounのB:は「JFS2でmount -o remountを用い、lff」を述べ、対象は変更後確認 lff（変更・moun）です。復旧前・lsatのC:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は復旧前確認 対象ファイル（復旧・lsat）です。「topas -C」は「性能管理でtopas -Cを用い、dxm とAME統計を確認する」を指し、運用引継ぎ dxmではto・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -C 運用引継ぎ dxm 0293**

    - 検証目的: 性能管理のtopas -C 運用引継ぎ dxm 0293について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ053-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -C
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0293A
    ```

    画面・出力には AIX0293A が表示され、topas -C 運用引継ぎ dxm 0293 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0293B
    ```

    画面・出力には AIX0293B が表示され、topas -C 運用引継ぎ dxm 0293 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0293C
    ```

    画面・出力には AIX0293C が表示され、topas -C 運用引継ぎ dxm 0293 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0293A が画面・出力に表示されること
    ② ステップ2 の AIX0293B が画面・出力に表示されること
    ③ ステップ3 の AIX0293C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 変更前確認 Busy% 0490 {#c01-i0858}
*分類: 性能管理*  ・  難易度: 初級

桜雲確認ではAIX 7.3の性能管理で topas -D を確認します。桜雲確認の性能管理では Busy% とvmstat表示を保守票へ記録します。桜雲確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。桜雲確認の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、桜雲確認を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 変更前確認 Busy% 0490の役割を調べています。setsecattr 変更後確認 enhanced_RBAC 0491の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は性能管理でtopas -Dを用い・Busy% とvmstat表示を確認する。 ✅
    - B. 表示や設定で扱う内容はセキュリティでsetsecattrを用い・enhanced_RBAC とロール一覧を確認する。
    - C. 表示や設定で扱う内容はJFS2でlsfs -qを用い・isnapshot とログデバイス設定を確認する。
    - D. 表示や設定で扱う内容はLVMでmklvを用い・PP SIZE とボリュームグループ属性を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でtopas -Dを用い、Busy% とvmstat表示を確認する」に対応する項目は変更前確認 Busy%（変更・topa）です。変更前に関する性能管理の仕様は「性能管理でtopas -Dを用い、Busy%」で、確認対象はto・変更前です。変更後・setsのB:は「セキュリティでsetsecattrを用い」を述べ、対象は変更後確認 enhanced_RBA（変更・sets）です。起動・lsfsのC:は「JFS2でlsfs -qを用い、isnapshot」を述べ、対象は起動確認 isnapshot（起動・lsfs）です。障害切・mklvのD:は「LVMでmklvを用い、PP SIZE とボリュームグループ属性を確」を述べ、対象はPP SIZE（障害・mklv）です。「topas -D」は「性能管理でtopas -Dを用い、Busy%」を指し、変更前確認 Busy%ではto・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 変更前確認 Busy% 0490**

    - 検証目的: 性能管理のtopas -D 変更前確認 Busy% 0490について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認010-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0490A
    ```

    画面・出力には AIX0490A が表示され、topas -D 変更前確認 Busy% 0490 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0490B
    ```

    画面・出力には AIX0490B が表示され、topas -D 変更前確認 Busy% 0490 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0490C
    ```

    画面・出力には AIX0490C が表示され、topas -D 変更前確認 Busy% 0490 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0490A が画面・出力に表示されること
    ② ステップ2 の AIX0490B が画面・出力に表示されること
    ③ ステップ3 の AIX0490C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 変更前確認 PhysB 0014 {#c01-i0859}
*分類: 性能管理*  ・  難易度: 初級

星霜確認ではAIX 7.3の性能管理で topas -D を確認します。星霜確認の性能管理では PhysB とvmstat表示を確認票へ整理します。星霜確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。星霜確認の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、星霜確認を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 変更前確認 PhysB 0014に関する障害切り分けの前提を確認しています。setsecattr 変更後確認 audit class 0015の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は性能管理でtopas -Dを用い・PhysB とvmstat表示を確認する。 ✅
    - B. 障害切り分けに用いる役割はセキュリティでsetsecattrを用い・audit class とロール一覧を確認する。
    - C. 障害切り分けに用いる役割はJFS2でlsfs -qを用い・log=INLINE とログデバイス設定を確認する。
    - D. 障害切り分けに用いる役割はセキュリティでrolelist -u user1を用い・user attributesである。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でtopas -Dを用い、PhysB とvmstat表示を確認する」に対応する項目は変更前確認 PhysB（変更・topa）です。性能管理の仕様は「性能管理でtopas -Dを用い、PhysB」で、確認対象はto・変更前です。変更後・setsのB:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（変更・sets）です。起動・lsfsのC:は「JFS2でlsfs -qを用い、log=INLINE」を述べ、対象は起動確認 log=INLINE（起動・lsfs）です。容量・roleのD:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（容量・role）です。「topas -D」は「性能管理でtopas -Dを用い、PhysB」を指し、変更前確認 PhysBではto・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 変更前確認 PhysB 0014**

    - 検証目的: 性能管理のtopas -D 変更前確認 PhysB 0014について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認014-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0014A
    ```

    画面・出力には AIX0014A が表示され、topas -D 変更前確認 PhysB 0014 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0014B
    ```

    画面・出力には AIX0014B が表示され、topas -D 変更前確認 PhysB 0014 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0014C
    ```

    画面・出力には AIX0014C が表示され、topas -D 変更前確認 PhysB 0014 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0014A が画面・出力に表示されること
    ② ステップ2 の AIX0014B が画面・出力に表示されること
    ③ ステップ3 の AIX0014C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 変更前確認 avm 0550 {#c01-i0860}
*分類: 性能管理*  ・  難易度: 中級

早苗照合ではAIX 7.3の性能管理で topas -D を確認します。早苗照合の性能管理では avm とvmstat表示を保守票へ記録します。早苗照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。早苗照合の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、早苗照合を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 変更前確認 avm 0550に関する障害切り分けの前提を確認しています。setsecattr 変更後確認 enhanced_RBAC 0551の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はセキュリティでsetsecattrを用い・enhanced_RBAC とロール一覧を確認する。
    - B. 表示や設定で扱う内容はデバイスや sys0 などの属性値を表示するコマンドである。
    - C. 表示や設定で扱う内容はLVMでchlvを用い・STALE PARTITIONS とボリュームグループ属性を確認する。
    - D. 表示や設定で扱う内容は性能管理でtopas -Dを用い・avm とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でtopas -Dを用い、avm とvmstat表示を確認する」に対応する項目は変更前確認 avm（変更・topa）です。変更前に関する性能管理の仕様は「性能管理でtopas -Dを用い、avm」で、確認対象はto・変更前です。変更後・setsのA:は「セキュリティでsetsecattrを用い」を述べ、対象は変更後確認 enhanced_RBA（変更・sets）です。一覧・対象・lsatのB:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は一覧確認 対象ファイル（一覧・lsat）です。バック・chlvのC:は「LVMでchlvを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（バッ・chlv）です。「topas -D」は「性能管理でtopas -Dを用い、avm」を指し、変更前確認 avmではto・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 変更前確認 avm 0550**

    - 検証目的: 性能管理のtopas -D 変更前確認 avm 0550について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認070-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0550A
    ```

    画面・出力には AIX0550A が表示され、topas -D 変更前確認 avm 0550 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0550B
    ```

    画面・出力には AIX0550B が表示され、topas -D 変更前確認 avm 0550 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0550C
    ```

    画面・出力には AIX0550C が表示され、topas -D 変更前確認 avm 0550 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0550A が画面・出力に表示されること
    ② ステップ2 の AIX0550B が画面・出力に表示されること
    ③ ステップ3 の AIX0550C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 変更前確認 fre 0074 {#c01-i0861}
*分類: 性能管理*  ・  難易度: 中級

銀嶺照合ではAIX 7.3の性能管理で topas -D を確認します。銀嶺照合の性能管理では fre とvmstat表示を確認票へ整理します。銀嶺照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。銀嶺照合の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、銀嶺照合を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 変更前確認 fre 0074の役割を調べています。setsecattr 変更後確認 audit class 0075の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はセキュリティでsetsecattrを用い・audit class とロール一覧を確認する。
    - B. 障害切り分けに用いる役割はJFS2でmount -o remountを用い・agblksize とログデバイス設定を確認する。
    - C. 障害切り分けに用いる役割はセキュリティでrolelist -u user1を用い・user attributesである。
    - D. 障害切り分けに用いる役割は性能管理でtopas -Dを用い・fre とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でtopas -Dを用い、fre とvmstat表示を確認する」に対応する項目は変更前確認 fre（変更・topa）です。変更前に関する性能管理の仕様は「性能管理でtopas -Dを用い、fre」で、確認対象はto・変更前です。変更後・setsのA:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（変更・sets）です。属性・mounのB:は「JFS2でmount -o remountを用い」を述べ、対象は属性確認 agblksize（属性・moun）です。容量・roleのC:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（容量・role）です。「topas -D」は「性能管理でtopas -Dを用い、fre」を指し、変更前確認 freではto・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 変更前確認 fre 0074**

    - 検証目的: 性能管理のtopas -D 変更前確認 fre 0074について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認074-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0074A
    ```

    画面・出力には AIX0074A が表示され、topas -D 変更前確認 fre 0074 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0074B
    ```

    画面・出力には AIX0074B が表示され、topas -D 変更前確認 fre 0074 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0074C
    ```

    画面・出力には AIX0074C が表示され、topas -D 変更前確認 fre 0074 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0074A が画面・出力に表示されること
    ② ステップ2 の AIX0074B が画面・出力に表示されること
    ③ ステップ3 の AIX0074C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 容量確認 Busy% 0580 {#c01-i0862}
*分類: 性能管理*  ・  難易度: 上級

薄明点検ではAIX 7.3の性能管理で topas -D を確認します。薄明点検の性能管理では Busy% とtopasディスク表示を監査票へ転記します。薄明点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。薄明点検の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、薄明点検を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 容量確認 Busy% 0580の技術的な意味を資料で確認するとき、setsecattr 性能確認 enhanced_RBAC 0581との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はセキュリティでsetsecattrを用い・enhanced_RBAC と監査設定を確認する。
    - B. 管理対象との関係を表す説明はデバイスや sys0 などの属性値を表示するコマンドである。
    - C. 管理対象との関係を表す説明はLVMでchlvを用い・VG STATE とミラーコピー状態を確認する。
    - D. 管理対象との関係を表す説明は性能管理でtopas -Dを用い・Busy% とtopasディスク表示を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「性能管理でtopas -Dを用い、Busy% とtopasディスク表示を確認する」に対応する項目は容量確認 Busy%（容量・topa）です。容量に関する性能管理の仕様は「性能管理でtopas -Dを用い、Busy%」で、確認対象はto・容量です。性能・setsのA:は「セキュリティでsetsecattrを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・sets）です。詳細・確認・lsatのB:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は詳細確認 確認範囲（詳細・lsat）です。属性・chlvのC:は「LVMでchlvを用い、VG STATE」を述べ、対象はVG STATE（属性・chlv）です。「topas -D」は「性能管理でtopas -Dを用い、Busy%」を指し、容量確認 Busy%ではto・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 容量確認 Busy% 0580**

    - 検証目的: 性能管理のtopas -D 容量確認 Busy% 0580について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認100-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0580A
    ```

    画面・出力には AIX0580A が表示され、topas -D 容量確認 Busy% 0580 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0580B
    ```

    画面・出力には AIX0580B が表示され、topas -D 容量確認 Busy% 0580 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0580C
    ```

    画面・出力には AIX0580C が表示され、topas -D 容量確認 Busy% 0580 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0580A が画面・出力に表示されること
    ② ステップ2 の AIX0580B が画面・出力に表示されること
    ③ ステップ3 の AIX0580C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 容量確認 PhysB 0104 {#c01-i0863}
*分類: 性能管理*  ・  難易度: 上級

霜月点検ではAIX 7.3の性能管理で topas -D を確認します。霜月点検の性能管理では PhysB とtopasディスク表示を引継ぎ票へ保管します。霜月点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。霜月点検の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、霜月点検を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 容量確認 PhysB 0104を同一分類のsetsecattr 性能確認 audit class 0105と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はセキュリティでsetsecattrを用い・audit class と監査設定を確認する。
    - B. コマンドまたは機能の用途はJFS2でmount -o remountを用い・lff とファイルシステム属性を確認する。
    - C. コマンドまたは機能の用途はセキュリティでrolelist -u user1を用い・user attributes と監査設定を確認する。
    - D. コマンドまたは機能の用途は性能管理でtopas -Dを用い・PhysB とtopasディスク表示を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「性能管理でtopas -Dを用い、PhysB とtopasディスク表示を確認する」に対応する項目は容量確認 PhysB（容量・topa）です。容量に関する性能管理の仕様は「性能管理でtopas -Dを用い、PhysB」で、確認対象はto・容量です。性能・setsのA:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（性能・sets）です。バック・mounのB:は「JFS2でmount -o remountを用い、lff」を述べ、対象はバックアウト確認 lff（バッ・moun）です。変更前・roleのC:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（変更・role）です。「topas -D」は「性能管理でtopas -Dを用い、PhysB」を指し、容量確認 PhysBではto・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 容量確認 PhysB 0104**

    - 検証目的: 性能管理のtopas -D 容量確認 PhysB 0104について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認104-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0104A
    ```

    画面・出力には AIX0104A が表示され、topas -D 容量確認 PhysB 0104 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0104B
    ```

    画面・出力には AIX0104B が表示され、topas -D 容量確認 PhysB 0104 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0104C
    ```

    画面・出力には AIX0104C が表示され、topas -D 容量確認 PhysB 0104 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0104A が画面・出力に表示されること
    ② ステップ2 の AIX0104B が画面・出力に表示されること
    ③ ステップ3 の AIX0104C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 容量確認 csz 0044 {#c01-i0864}
*分類: 性能管理*  ・  難易度: 中級

若草照合ではAIX 7.3の性能管理で topas -D を確認します。若草照合の性能管理では csz とtopasディスク表示を引継ぎ票へ保管します。若草照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若草照合の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、若草照合を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 容量確認 csz 0044の技術的な意味を資料で確認するとき、setsecattr 性能確認 audit class 0045との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は性能管理でtopas -Dを用い・csz とtopasディスク表示を確認する。 ✅
    - B. コマンドまたは機能の用途はセキュリティでsetsecattrを用い・audit class と監査設定を確認する。
    - C. コマンドまたは機能の用途はJFS2でlsfs -qを用い・mountguard とファイルシステム属性を確認する。
    - D. コマンドまたは機能の用途はセキュリティでrolelist -u user1を用い・user attributes と監査設定を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Dを用い、csz とtopasディスク表示を確認する」に対応する項目は容量確認 csz（容量・topa）です。性能管理の仕様は「性能管理でtopas -Dを用い、csz とtopasディスク表示を確認」で、確認対象はto・容量です。性能・setsのB:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（性能・sets）です。障害切・lsfsのC:は「JFS2でlsfs -qを用い、mountguard」を述べ、対象は障害切り分け mountguard（障害・lsfs）です。変更前・roleのD:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（変更・role）です。「topas -D」は「性能管理でtopas -Dを用い、csz」を指し、容量確認 cszではto・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 容量確認 csz 0044**

    - 検証目的: 性能管理のtopas -D 容量確認 csz 0044について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認044-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0044A
    ```

    画面・出力には AIX0044A が表示され、topas -D 容量確認 csz 0044 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0044B
    ```

    画面・出力には AIX0044B が表示され、topas -D 容量確認 csz 0044 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0044C
    ```

    画面・出力には AIX0044C が表示され、topas -D 容量確認 csz 0044 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0044A が画面・出力に表示されること
    ② ステップ2 の AIX0044B が画面・出力に表示されること
    ③ ステップ3 の AIX0044C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 容量確認 po 0520 {#c01-i0865}
*分類: 性能管理*  ・  難易度: 中級

青葉照合ではAIX 7.3の性能管理で topas -D を確認します。青葉照合の性能管理では po とtopasディスク表示を監査票へ転記します。青葉照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。青葉照合の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、青葉照合を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 容量確認 po 0520を同一分類のsetsecattr 性能確認 enhanced_RBAC 0521と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は性能管理でtopas -Dを用い・po とtopasディスク表示を確認する。 ✅
    - B. 管理対象との関係を表す説明はセキュリティでsetsecattrを用い・enhanced_RBAC と監査設定を確認する。
    - C. 管理対象との関係を表す説明はJFS2でlsfs -qを用い・ファイルシステム使用率 とファイルシステム属性を確認する。
    - D. 管理対象との関係を表す説明はLVMでmklvを用い・PVID とミラーコピー状態を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Dを用い、po とtopasディスク表示を確認する」に対応する項目は容量確認 po（容量・topa）です。容量に関する性能管理の仕様は「性能管理でtopas -Dを用い、po とtopasディスク表示を確」で、確認対象はto・容量です。性能・setsのB:は「セキュリティでsetsecattrを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・sets）です。障害切・lsfsのC:は「JFS2でlsfs -qを用い、ファイルシステム使用率」を述べ、対象は障害切り分け ファイルシステム使用率（障害・lsfs）です。起動・mklvのD:は「LVMでmklvを用い、PVID とミラーコピー状態を確認する」を述べ、対象は起動確認 PVID（起動・mklv）です。「topas -D」は「性能管理でtopas -Dを用い、po とtopasディスク表示を確」を指し、容量確認 poではto・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 容量確認 po 0520**

    - 検証目的: 性能管理のtopas -D 容量確認 po 0520について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認040-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0520A
    ```

    画面・出力には AIX0520A が表示され、topas -D 容量確認 po 0520 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0520B
    ```

    画面・出力には AIX0520B が表示され、topas -D 容量確認 po 0520 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0520C
    ```

    画面・出力には AIX0520C が表示され、topas -D 容量確認 po 0520 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0520A が画面・出力に表示されること
    ② ステップ2 の AIX0520B が画面・出力に表示されること
    ③ ステップ3 の AIX0520C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 状態確認 csz 0203 {#c01-i0866}
*分類: 性能管理*  ・  難易度: 中級

秋声保守ではAIX 7.3の性能管理で topas -D を確認します。秋声保守の性能管理では csz とsvmon全体表示を照合票へ整理します。秋声保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。秋声保守の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、秋声保守を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 状態確認 csz 0203について構成や状態を確認します。setsecattr 構成照合 audit class 0204ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は性能管理でtopas -Dを用い・csz とsvmon全体表示を確認する。 ✅
    - B. 一次資料が示す主目的はセキュリティでsetsecattrを用い・audit class とユーザー属性を確認する。
    - C. 一次資料が示す主目的はJFS2でmount -o remountを用い・agblksize とマウントオプションを確認する。
    - D. 一次資料が示す主目的はセキュリティでrolelist -u user1を用い・user attributesである。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Dを用い、csz とsvmon全体表示を確認する」に対応する項目は状態確認 csz（状態・topa）です。状態に関する性能管理の仕様は「性能管理でtopas -Dを用い、csz」で、確認対象はto・状態です。構成・setsのB:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（構成・sets）です。性能・mounのC:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 agblksize（性能・moun）です。監査・roleのD:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（監査・role）です。「topas -D」は「性能管理でtopas -Dを用い、csz」を指し、状態確認 cszではto・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 状態確認 csz 0203**

    - 検証目的: 性能管理のtopas -D 状態確認 csz 0203について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認083-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0203A
    ```

    画面・出力には AIX0203A が表示され、topas -D 状態確認 csz 0203 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0203B
    ```

    画面・出力には AIX0203B が表示され、topas -D 状態確認 csz 0203 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0203C
    ```

    画面・出力には AIX0203C が表示され、topas -D 状態確認 csz 0203 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0203A が画面・出力に表示されること
    ② ステップ2 の AIX0203B が画面・出力に表示されること
    ③ ステップ3 の AIX0203C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 状態確認 po 0679 {#c01-i0867}
*分類: 性能管理*  ・  難易度: 中級

秋桜判定ではAIX 7.3の性能管理で topas -D を確認します。秋桜判定の性能管理では po とsvmon全体表示を点検票へ整理します。秋桜判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。秋桜判定の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、秋桜判定を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 状態確認 po 0679の設定や表示を読む前に役割を確認します。setsecattr 構成照合 enhanced_RBAC 0680ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは性能管理でtopas -Dを用い・po とsvmon全体表示を確認する。 ✅
    - B. 対象資源に対する働きはセキュリティでsetsecattrを用い・enhanced_RBAC とユーザー属性を確認する。
    - C. 対象資源に対する働きは導入と起動でalt_disk_mksysbを用い・bootlist と起動デバイス設定を確認する。
    - D. 対象資源に対する働きはLVMでchlvを用い・PP SIZE と論理ボリューム配置を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でtopas -Dを用い、po とsvmon全体表示を確認する」に対応する項目は状態確認 po（状態・topa）です。状態に関する性能管理の仕様は「性能管理でtopas -Dを用い、po とsvmon全体表示を確認す」で、確認対象はto・状態です。構成・setsのB:は「セキュリティでsetsecattrを用い」を述べ、対象は構成照合 enhanced_RBAC（構成・sets）です。バック・alt_のC:は「導入と起動でalt_disk_mksysbを用い、bootlist」を述べ、対象はバックアウト確認 bootlist（バッ・alt_）です。変更後・chlvのD:は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」を述べ、対象はPP SIZE（変更・chlv）です。「topas -D」は「性能管理でtopas -Dを用い、po とsvmon全体表示を確認す」を指し、状態確認 poではto・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 状態確認 po 0679**

    - 検証目的: 性能管理のtopas -D 状態確認 po 0679について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理状態確認079-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0679A
    ```

    画面・出力には AIX0679A が表示され、topas -D 状態確認 po 0679 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0679B
    ```

    画面・出力には AIX0679B が表示され、topas -D 状態確認 po 0679 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0679C
    ```

    画面・出力には AIX0679C が表示され、topas -D 状態確認 po 0679 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0679A が画面・出力に表示されること
    ② ステップ2 の AIX0679B が画面・出力に表示されること
    ③ ステップ3 の AIX0679C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 監査記録 avm 0709 {#c01-i0868}
*分類: 性能管理*  ・  難易度: 上級

梅雨晴保守ではAIX 7.3の性能管理で topas -D を確認します。梅雨晴保守の性能管理では avm とAME統計を採取票へ記録します。梅雨晴保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。梅雨晴保守の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、梅雨晴保守を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** topas -D 監査記録 avm 0709を保守記録に説明する必要があります。setsecattr 運用引継ぎ enhanced_RBAC 0710と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はセキュリティでsetsecattrを用い・enhanced_RBAC とRBAC属性を確認する。
    - B. 保守作業で参照する機能は導入と起動でalt_disk_mksysbを用い・Technology Levelである。
    - C. 保守作業で参照する機能はLVMでchlvを用い・PVID と物理ボリューム一覧を確認する。
    - D. 保守作業で参照する機能は性能管理でtopas -Dを用い・avm とAME統計を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「性能管理でtopas -Dを用い、avm とAME統計を確認する」に対応する項目は監査記録 avm（監査・topa）です。監査に関する性能管理の仕様は「性能管理でtopas -Dを用い、avm とAME統計を確認する」で、確認対象はto・監査です。運用引・setsのA:は「セキュリティでsetsecattrを用い」を述べ、対象は運用引継ぎ enhanced_RBA（運用・sets）です。属性・alt_のB:は「導入と起動でalt_disk_mksysbを用い」を述べ、対象はTechnology Level（属性・alt_）です。性能・chlvのC:は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は性能確認 PVID（性能・chlv）です。「topas -D」は「性能管理でtopas -Dを用い、avm とAME統計を確認する」を指し、監査記録 avmではto・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 監査記録 avm 0709**

    - 検証目的: 性能管理のtopas -D 監査記録 avm 0709について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理監査記録109-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0709A
    ```

    画面・出力には AIX0709A が表示され、topas -D 監査記録 avm 0709 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0709B
    ```

    画面・出力には AIX0709B が表示され、topas -D 監査記録 avm 0709 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0709C
    ```

    画面・出力には AIX0709C が表示され、topas -D 監査記録 avm 0709 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0709A が画面・出力に表示されること
    ② ステップ2 の AIX0709B が画面・出力に表示されること
    ③ ステップ3 の AIX0709C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 監査記録 fre 0233 {#c01-i0869}
*分類: 性能管理*  ・  難易度: 上級

朝霧保守ではAIX 7.3の性能管理で topas -D を確認します。朝霧保守の性能管理では fre とAME統計を復旧票へ残します。朝霧保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。朝霧保守の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、朝霧保守を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「topas -D 監査記録 fre 0233」を「setsecattr 運用引継ぎ audit class 0234」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はセキュリティでsetsecattrを用い・audit class とRBAC属性を確認する。
    - B. 仕様上の役割は性能管理でtopas -Dを用い・fre とAME統計を確認する。 ✅
    - C. 仕様上の役割はJFS2でmount -o remountを用い・lff と内部スナップショットを確認する。
    - D. 仕様上の役割はデバイスや sys0 などの属性値を表示するコマンドである。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「性能管理でtopas -Dを用い、fre とAME統計を確認する」に対応する項目は監査記録 fre（監査・topa）です。監査に関する性能管理の仕様は「性能管理でtopas -Dを用い、fre とAME統計を確認する」で、確認対象はto・監査です。運用引・setsのA:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（運用・sets）です。変更後・mounのC:は「JFS2でmount -o remountを用い、lff」を述べ、対象は変更後確認 lff（変更・moun）です。性能・実行・lsatのD:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は性能確認 実行結果（性能・lsat）です。「topas -D」は「性能管理でtopas -Dを用い、fre とAME統計を確認する」を指し、監査記録 freではto・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 監査記録 fre 0233**

    - 検証目的: 性能管理のtopas -D 監査記録 fre 0233について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理監査記録113-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0233A
    ```

    画面・出力には AIX0233A が表示され、topas -D 監査記録 fre 0233 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0233B
    ```

    画面・出力には AIX0233B が表示され、topas -D 監査記録 fre 0233 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0233C
    ```

    画面・出力には AIX0233C が表示され、topas -D 監査記録 fre 0233 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0233A が画面・出力に表示されること
    ② ステップ2 の AIX0233B が画面・出力に表示されること
    ③ ステップ3 の AIX0233C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### topas -D 障害切り分け csz 0361 {#c01-i0870}
*分類: 性能管理*  ・  難易度: 初級

白露記録ではAIX 7.3の性能管理で topas -D を確認します。白露記録の性能管理では csz とAME統計を採取票へ記録します。白露記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。白露記録の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、白露記録を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「topas -D 障害切り分け csz 0361」を「setsecattr バックアウト確認 user attributes 0362」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は性能管理でtopas -Dを用い・csz とAME統計を確認する。 ✅
    - B. 保守作業で参照する機能はセキュリティでsetsecattrを用い・user attributes とRBAC属性を確認する。
    - C. 保守作業で参照する機能はJFS2でlsfs -qを用い・mountguard と内部スナップショットを確認する。
    - D. 保守作業で参照する機能はLVMでmklvを用い・PP SIZE と物理ボリューム一覧を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でtopas -Dを用い、csz とAME統計を確認する」に対応する項目は障害切り分け csz（障害・topa）です。障害切に関する性能管理の仕様は「性能管理でtopas -Dを用い、csz とAME統計を確認する」で、確認対象はto・障害切です。バック・setsのB:は「セキュリティでsetsecattrを用い、user」を述べ、対象はuser attributes（バッ・sets）です。状態・lsfsのC:は「JFS2でlsfs -qを用い、mountguard」を述べ、対象は状態確認 mountguard（状態・lsfs）です。監査・mklvのD:は「LVMでmklvを用い、PP SIZE と物理ボリューム一覧を確認す」を述べ、対象はPP SIZE（監査・mklv）です。「topas -D」は「性能管理でtopas -Dを用い、csz とAME統計を確認する」を指し、障害切り分け cszではto・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **topas -D 障害切り分け csz 0361**

    - 検証目的: 性能管理のtopas -D 障害切り分け csz 0361について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理障害切り分け001-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0361A
    ```

    画面・出力には AIX0361A が表示され、topas -D 障害切り分け csz 0361 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0361B
    ```

    画面・出力には AIX0361B が表示され、topas -D 障害切り分け csz 0361 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0361C
    ```

    画面・出力には AIX0361C が表示され、topas -D 障害切り分け csz 0361 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0361A が画面・出力に表示されること
    ② ステップ2 の AIX0361B が画面・出力に表示されること
    ③ ステップ3 の AIX0361C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a バックアウト確認 Busy% 0029 {#c01-i0871}
*分類: 性能管理*  ・  難易度: 中級

梅雨晴確認ではAIX 7.3の性能管理で vmo -a を確認します。梅雨晴確認の性能管理では Busy% とAME統計を復旧票へ残します。梅雨晴確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。梅雨晴確認の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、梅雨晴確認を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a バックアウト確認 Busy% 0029を保守記録に説明する必要があります。lsattr -E -l sys0 -a enhanced_RBAC 監査記録と取り違えない説明はどれですか。

    - A. 仕様上の役割はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。
    - B. 仕様上の役割はJFS2でsplitcopyを用い・isnapshot と内部スナップショットを確認する。
    - C. 仕様上の役割はセキュリティでlsuserを用い・authorizations とRBAC属性を確認する。
    - D. 仕様上の役割は性能管理でvmo -aを用い・Busy% とAME統計を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でvmo -aを用い、Busy% とAME統計を確認する」に対応する項目はバックアウト確認 Busy%（バッ・vmo）です。性能管理の仕様は「性能管理でvmo -aを用い、Busy% とAME統計を確認する」で、確認対象はvm・バックです。監査・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsat）です。構成・spliのB:は「JFS2でsplitcopyを用い、isnapshot」を述べ、対象は構成照合 isnapshot（構成・spli）です。属性・lsusのC:は「セキュリティでlsuserを用い、authorizations」を述べ、対象は属性確認 authorization（属性・lsus）です。「vmo -a」は「性能管理でvmo -aを用い、Busy% とAME統計を確認する」を指し、バックアウト確認 Busy%ではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a バックアウト確認 Busy% 0029**

    - 検証目的: 性能管理のvmo -a バックアウト確認 Busy% 0029について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認029-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0029A
    ```

    画面・出力には AIX0029A が表示され、vmo -a バックアウト確認 Busy% 0029 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0029B
    ```

    画面・出力には AIX0029B が表示され、vmo -a バックアウト確認 Busy% 0029 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0029C
    ```

    画面・出力には AIX0029C が表示され、vmo -a バックアウト確認 Busy% 0029 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0029A が画面・出力に表示されること
    ② ステップ2 の AIX0029B が画面・出力に表示されること
    ③ ステップ3 の AIX0029C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a バックアウト確認 Entitled Capacity 0565 {#c01-i0872}
*分類: 性能管理*  ・  難易度: 中級

深雪点検ではAIX 7.3の性能管理で vmo -a を確認します。深雪点検の性能管理では Entitled Capacity とAME統計を採取票へ記録します。深雪点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。深雪点検の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、深雪点検を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a バックアウト確認 Entitled Capacity 0565を保守記録に説明する必要があります。lsattr -E -l sys0 -a enhanced_RBAC 監査記録と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はセキュリティでlsattr -E -l sys0 -aを用い・roles とRBAC属性を確認する。
    - B. 保守作業で参照する機能は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - C. 保守作業で参照する機能は性能管理でvmo -aを用い・Entitled Capacity とAME統計を確認する。 ✅
    - D. 保守作業で参照する機能はLVMでlspvを用い・MIRROR WRITE CONSISTENCY と物理ボリューム一覧を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でvmo -aを用い、Entitled Capacity」に対応する項目はEntitled Capacity（バッ・vmo）です。バックに関する性能管理の仕様は「性能管理でvmo -aを用い、Entitled Capacity」で、確認対象はvm・バックです。監査・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 roles（監査・lsat）です。詳細・装置・lspvのB:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は詳細確認 装置一覧（詳細・lspv）です。容量・lspvのD:は「LVMでlspvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（容量・lspv）です。「vmo -a」は「性能管理でvmo -aを用い、Entitled Capacity」を指し、Entitled Capacityではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a バックアウト確認 Entitled Capacity 0565**

    - 検証目的: 性能管理のvmo -a バックアウト確認 Entitled Capacity 0565について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認085-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0565A
    ```

    画面・出力には AIX0565A が表示され、vmo -a バックアウト確認 Entitled Capacity 0565 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0565B
    ```

    画面・出力には AIX0565B が表示され、vmo -a バックアウト確認 Entitled Capacity 0565 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0565C
    ```

    画面・出力には AIX0565C が表示され、vmo -a バックアウト確認 Entitled Capacity 0565 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0565A が画面・出力に表示されること
    ② ステップ2 の AIX0565B が画面・出力に表示されること
    ③ ステップ3 の AIX0565C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a バックアウト確認 avm 0089 {#c01-i0873}
*分類: 性能管理*  ・  難易度: 中級

銀砂点検ではAIX 7.3の性能管理で vmo -a を確認します。銀砂点検の性能管理では avm とAME統計を復旧票へ残します。銀砂点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。銀砂点検の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、銀砂点検を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「vmo -a バックアウト確認 avm 0089」を「lsattr -E -l sys0 -a enhanced_RBAC 監査記録」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。
    - B. 仕様上の役割はJFS2でlogformを用い・mountguard と内部スナップショットを確認する。
    - C. 仕様上の役割は性能管理でvmo -aを用い・avm とAME統計を確認する。 ✅
    - D. 仕様上の役割はセキュリティでlsuserを用い・authorizations とRBAC属性を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でvmo -aを用い、avm とAME統計を確認する」に対応する項目はバックアウト確認 avm（バッ・vmo）です。バックに関する性能管理の仕様は「性能管理でvmo -aを用い、avm とAME統計を確認する」で、確認対象はvm・バックです。監査・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsat）です。変更前・logfのB:は「JFS2でlogformを用い、mountguard」を述べ、対象は変更前確認 mountguard（変更・logf）です。属性・lsusのD:は「セキュリティでlsuserを用い、authorizations」を述べ、対象は属性確認 authorization（属性・lsus）です。「vmo -a」は「性能管理でvmo -aを用い、avm とAME統計を確認する」を指し、バックアウト確認 avmではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a バックアウト確認 avm 0089**

    - 検証目的: 性能管理のvmo -a バックアウト確認 avm 0089について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認089-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0089A
    ```

    画面・出力には AIX0089A が表示され、vmo -a バックアウト確認 avm 0089 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0089B
    ```

    画面・出力には AIX0089B が表示され、vmo -a バックアウト確認 avm 0089 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0089C
    ```

    画面・出力には AIX0089C が表示され、vmo -a バックアウト確認 avm 0089 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0089A が画面・出力に表示されること
    ② ステップ2 の AIX0089B が画面・出力に表示されること
    ③ ステップ3 の AIX0089C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a バックアウト確認 dxm 0505 {#c01-i0874}
*分類: 性能管理*  ・  難易度: 中級

花冷確認ではAIX 7.3の性能管理で vmo -a を確認します。花冷確認の性能管理では dxm とAME統計を採取票へ記録します。花冷確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。花冷確認の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、花冷確認を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「vmo -a バックアウト確認 dxm 0505」を「lsattr -E -l sys0 -a enhanced_RBAC 監査記録」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はセキュリティでlsattr -E -l sys0 -aを用い・roles とRBAC属性を確認する。
    - B. 保守作業で参照する機能はJFS2でsplitcopyを用い・lff と内部スナップショットを確認する。
    - C. 保守作業で参照する機能は性能管理でvmo -aを用い・dxm とAME統計を確認する。 ✅
    - D. 保守作業で参照する機能はLVMでchvgを用い・STALE PARTITIONS と物理ボリューム一覧を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でvmo -aを用い、dxm とAME統計を確認する」に対応する項目はバックアウト確認 dxm（バッ・vmo）です。バックに関する性能管理の仕様は「性能管理でvmo -aを用い、dxm とAME統計を確認する」で、確認対象はvm・バックです。監査・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 roles（監査・lsat）です。構成・spliのB:は「JFS2でsplitcopyを用い、lff」を述べ、対象は構成照合 lff（構成・spli）です。運用引・chvgのD:は「LVMでchvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（運用・chvg）です。「vmo -a」は「性能管理でvmo -aを用い、dxm とAME統計を確認する」を指し、バックアウト確認 dxmではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a バックアウト確認 dxm 0505**

    - 検証目的: 性能管理のvmo -a バックアウト確認 dxm 0505について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認025-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0505A
    ```

    画面・出力には AIX0505A が表示され、vmo -a バックアウト確認 dxm 0505 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0505B
    ```

    画面・出力には AIX0505B が表示され、vmo -a バックアウト確認 dxm 0505 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0505C
    ```

    画面・出力には AIX0505C が表示され、vmo -a バックアウト確認 dxm 0505 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0505A が画面・出力に表示されること
    ② ステップ2 の AIX0505B が画面・出力に表示されること
    ③ ステップ3 の AIX0505C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a 変更後確認 fre 0694 {#c01-i0875}
*分類: 性能管理*  ・  難易度: 中級

星霜保守ではAIX 7.3の性能管理で vmo -a を確認します。星霜保守の性能管理では fre とvmstat表示を保守票へ記録します。星霜保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。星霜保守の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、星霜保守を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a 変更後確認 fre 0694に関する障害切り分けの前提を確認しています。lsattr -E -l sys0 -a enhanced_RBAC 障害切り分けの機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容はセキュリティでlsattr -E -l sys0 -aを用い・audit class とロール一覧を確認する。
    - B. 表示や設定で扱う内容は導入と起動でoslevel -sを用い・altinst_rootvg と代替ディスク状態を確認する。
    - C. 表示や設定で扱う内容はLVMでlspvを用い・MIRROR WRITE CONSISTENCY とボリュームグループ属性を確認する。
    - D. 表示や設定で扱う内容は性能管理でvmo -aを用い・fre とvmstat表示を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「性能管理でvmo -aを用い、fre とvmstat表示を確認する」に対応する項目は変更後確認 fre（変更・vmo）です。変更後に関する性能管理の仕様は「性能管理でvmo -aを用い、fre とvmstat表示を確認する」で、確認対象はvm・変更後です。障害切・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象はaudit class（障害・lsat）です。容量・osleのB:は「導入と起動でoslevel -sを用い、altinst_rootvg」を述べ、対象は容量確認 altinst_rootv（容量・osle）です。監査・lspvのC:は「LVMでlspvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（監査・lspv）です。「vmo -a」は「性能管理でvmo -aを用い、fre とvmstat表示を確認する」を指し、変更後確認 freではvm・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a 変更後確認 fre 0694**

    - 検証目的: 性能管理のvmo -a 変更後確認 fre 0694について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認094-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0694A
    ```

    画面・出力には AIX0694A が表示され、vmo -a 変更後確認 fre 0694 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0694B
    ```

    画面・出力には AIX0694B が表示され、vmo -a 変更後確認 fre 0694 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0694C
    ```

    画面・出力には AIX0694C が表示され、vmo -a 変更後確認 fre 0694 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0694A が画面・出力に表示されること
    ② ステップ2 の AIX0694B が画面・出力に表示されること
    ③ ステップ3 の AIX0694C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a 変更後確認 pi 0218 {#c01-i0876}
*分類: 性能管理*  ・  難易度: 中級

潮騒保守ではAIX 7.3の性能管理で vmo -a を確認します。潮騒保守の性能管理では pi とvmstat表示を確認票へ整理します。潮騒保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。潮騒保守の注意点として ディスクBusyと待ち時間の混同 を避けるため topas -D も併記します。性能監視の作業票として、潮騒保守を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a 変更後確認 pi 0218の役割を調べています。lsattr -E -l sys0 -a enhanced_RBAC 障害切り分けの説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割はセキュリティでlsattr -E -l sys0 -aを用い・authorizationsである。
    - B. 障害切り分けに用いる役割は性能管理でvmo -aを用い・pi とvmstat表示を確認する。 ✅
    - C. 障害切り分けに用いる役割はJFS2でlogformを用い・isnapshot とログデバイス設定を確認する。
    - D. 障害切り分けに用いる役割はセキュリティでlsuserを用い・roles とロール一覧を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でvmo -aを用い、pi とvmstat表示を確認する」に対応する項目は変更後確認 pi（変更・vmo）です。変更後に関する性能管理の仕様は「性能管理でvmo -aを用い、pi とvmstat表示を確認する」で、確認対象はvm・変更後です。障害切・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は障害切り分け authorizati（障害・lsat）です。状態・logfのC:は「JFS2でlogformを用い、isnapshot」を述べ、対象は状態確認 isnapshot（状態・logf）です。性能・lsusのD:は「セキュリティでlsuserを用い、roles とロール一覧を確認する」を述べ、対象は性能確認 roles（性能・lsus）です。「vmo -a」は「性能管理でvmo -aを用い、pi とvmstat表示を確認する」を指し、変更後確認 piではvm・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a 変更後確認 pi 0218**

    - 検証目的: 性能管理のvmo -a 変更後確認 pi 0218について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認098-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0218A
    ```

    画面・出力には AIX0218A が表示され、vmo -a 変更後確認 pi 0218 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0218B
    ```

    画面・出力には AIX0218B が表示され、vmo -a 変更後確認 pi 0218 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0218C
    ```

    画面・出力には AIX0218C が表示され、vmo -a 変更後確認 pi 0218 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0218A が画面・出力に表示されること
    ② ステップ2 の AIX0218B が画面・出力に表示されること
    ③ ステップ3 の AIX0218C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a 属性確認 pi 0535 {#c01-i0877}
*分類: 性能管理*  ・  難易度: 中級

岩清水照合ではAIX 7.3の性能管理で vmo -a を確認します。岩清水照合の性能管理では pi とsvmon全体表示を点検票へ整理します。岩清水照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。岩清水照合の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、岩清水照合を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a 属性確認 pi 0535の設定や表示を読む前に役割を確認します。lsattr -E -l sys0 -a enhanced_RBAC 状態確認ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・roles とユーザー属性を確認する。
    - B. 対象資源に対する働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - C. 対象資源に対する働きは性能管理でvmo -aを用い・pi とsvmon全体表示を確認する。 ✅
    - D. 対象資源に対する働きはLVMでchvgを用い・VG STATE と論理ボリューム配置を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「性能管理でvmo -aを用い、pi とsvmon全体表示を確認する」に対応する項目は属性確認 pi（属性・vmo）です。属性に関する性能管理の仕様は「性能管理でvmo -aを用い、pi とsvmon全体表示を確認する」で、確認対象はvm・属性です。状態・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 roles（状態・lsat）です。一覧・状態・lspvのB:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は一覧確認 状態確認（一覧・lspv）です。構成・chvgのD:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（構成・chvg）です。「vmo -a」は「性能管理でvmo -aを用い、pi とsvmon全体表示を確認する」を指し、属性確認 piではvm・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a 属性確認 pi 0535**

    - 検証目的: 性能管理のvmo -a 属性確認 pi 0535について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理属性確認055-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0535A
    ```

    画面・出力には AIX0535A が表示され、vmo -a 属性確認 pi 0535 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0535B
    ```

    画面・出力には AIX0535B が表示され、vmo -a 属性確認 pi 0535 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0535C
    ```

    画面・出力には AIX0535C が表示され、vmo -a 属性確認 pi 0535 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0535A が画面・出力に表示されること
    ② ステップ2 の AIX0535B が画面・出力に表示されること
    ③ ステップ3 の AIX0535C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a 属性確認 po 0059 {#c01-i0878}
*分類: 性能管理*  ・  難易度: 中級

山吹照合ではAIX 7.3の性能管理で vmo -a を確認します。山吹照合の性能管理では po とsvmon全体表示を照合票へ整理します。山吹照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。山吹照合の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、山吹照合を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a 属性確認 po 0059について構成や状態を確認します。lsattr -E -l sys0 -a enhanced_RBAC 状態確認ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。
    - B. 一次資料が示す主目的は性能管理でvmo -aを用い・po とsvmon全体表示を確認する。 ✅
    - C. 一次資料が示す主目的はJFS2でlogformを用い・log=INLINE とマウントオプションを確認する。
    - D. 一次資料が示す主目的はセキュリティでlsuserを用い・authorizations とユーザー属性を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でvmo -aを用い、po とsvmon全体表示を確認する」に対応する項目は属性確認 po（属性・vmo）です。性能管理の仕様は「性能管理でvmo -aを用い、po とsvmon全体表示を確認する」で、確認対象はvm・属性です。状態・lsatのA:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsat）です。容量・logfのC:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は容量確認 log=INLINE（容量・logf）です。バック・lsusのD:は「セキュリティでlsuserを用い、authorizations」を述べ、対象はバックアウト確認 authoriza（バッ・lsus）です。「vmo -a」は「性能管理でvmo -aを用い、po とsvmon全体表示を確認する」を指し、属性確認 poではvm・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a 属性確認 po 0059**

    - 検証目的: 性能管理のvmo -a 属性確認 po 0059について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理属性確認059-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0059A
    ```

    画面・出力には AIX0059A が表示され、vmo -a 属性確認 po 0059 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0059B
    ```

    画面・出力には AIX0059B が表示され、vmo -a 属性確認 po 0059 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0059C
    ```

    画面・出力には AIX0059C が表示され、vmo -a 属性確認 po 0059 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0059A が画面・出力に表示されること
    ② ステップ2 の AIX0059B が画面・出力に表示されること
    ③ ステップ3 の AIX0059C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmo -a 運用引継ぎ pi 0376 {#c01-i0879}
*分類: 性能管理*  ・  難易度: 初級

若竹記録ではAIX 7.3の性能管理で vmo -a を確認します。若竹記録の性能管理では pi とtopasディスク表示を監査票へ転記します。若竹記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若竹記録の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、若竹記録を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmo -a 運用引継ぎ pi 0376を同一分類のlsattr -E -l sys0 -a enhanced_RBAC 容量確認と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は性能管理でvmo -aを用い・pi とtopasディスク表示を確認する。 ✅
    - B. 管理対象との関係を表す説明はセキュリティでlsattr -E -l sys0 -aを用い・roles と監査設定を確認する。
    - C. 管理対象との関係を表す説明はJFS2でsplitcopyを用い・lff とファイルシステム属性を確認する。
    - D. 管理対象との関係を表す説明はLVMでchvgを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でvmo -aを用い、pi とtopasディスク表示を確認する」に対応する項目は運用引継ぎ pi（運用・vmo）です。運用引に関する性能管理の仕様は「性能管理でvmo -aを用い、pi とtopasディスク表示を確認す」で、確認対象はvm・運用引です。容量・lsatのB:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は容量確認 roles（容量・lsat）です。変更後・spliのC:は「JFS2でsplitcopyを用い、lff」を述べ、対象は変更後確認 lff（変更・spli）です。性能・chvgのD:は「LVMでchvgを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（性能・chvg）です。「vmo -a」は「性能管理でvmo -aを用い、pi とtopasディスク表示を確認す」を指し、運用引継ぎ piではvm・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmo -a 運用引継ぎ pi 0376**

    - 検証目的: 性能管理のvmo -a 運用引継ぎ pi 0376について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ016-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmo -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0376A
    ```

    画面・出力には AIX0376A が表示され、vmo -a 運用引継ぎ pi 0376 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0376B
    ```

    画面・出力には AIX0376B が表示され、vmo -a 運用引継ぎ pi 0376 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0376C
    ```

    画面・出力には AIX0376C が表示され、vmo -a 運用引継ぎ pi 0376 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0376A が画面・出力に表示されること
    ② ステップ2 の AIX0376B が画面・出力に表示されること
    ③ ステップ3 の AIX0376C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 バックアウト確認 avm 0815 {#c01-i0880}
*分類: 性能管理*  ・  難易度: 中級

岩清水変更ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。岩清水変更の性能管理では avm とsvmon全体表示を照合票へ整理します。岩清水変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。岩清水変更の注意点として 区画CPU権利値の見落とし を避けるため topas -D も併記します。性能監視の作業票として、岩清水変更を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 バックアウト確認 avm 0815の設定や表示を読む前に役割を確認します。lspv 障害切り分け 出力比較ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - B. 一次資料が示す主目的は性能管理でvmstat -c 2 1を用い・avm とsvmon全体表示を確認する。 ✅
    - C. 一次資料が示す主目的はセキュリティでlsroleを用い・roles とロール一覧を確認する。
    - D. 一次資料が示す主目的はデバイス管理でcfgmgrを用い・microcode level と診断対象表示を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** バック・vmstでBの記述「性能管理でvmstat -c 2 1を用い、avm」に対応する項目はバックアウト確認 avm（バッ・vmst）です。バックに関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、avm」で、確認対象はvm・バックです。障害切・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は障害切り分け 出力比較（障害・lspv）です。バック・lsroのC:は「セキュリティでlsroleを用い、roles とロール一覧を確認する」を述べ、対象はバックアウト確認 roles（バッ・lsro）です。バック・cfgmのD:は「デバイス管理でcfgmgrを用い、microcode level」を述べ、対象はmicrocode level（バッ・cfgm）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、avm」を指し、バックアウト確認 avmではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 バックアウト確認 avm 0815**

    - 検証目的: 性能管理のvmstat -c 2 1 バックアウト確認 avm 0815について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認095-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0815A
    ```

    画面・出力には AIX0815A が表示され、vmstat -c 2 1 バックアウト確認 avm 0815 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0815B
    ```

    画面・出力には AIX0815B が表示され、vmstat -c 2 1 バックアウト確認 avm 0815 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0815C
    ```

    画面・出力には AIX0815C が表示され、vmstat -c 2 1 バックアウト確認 avm 0815 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0815A が画面・出力に表示されること
    ② ステップ2 の AIX0815B が画面・出力に表示されること
    ③ ステップ3 の AIX0815C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 バックアウト確認 fre 0339 {#c01-i0881}
*分類: 性能管理*  ・  難易度: 中級

山吹変更ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。山吹変更の性能管理では fre とsvmon全体表示を作業票へ保管します。山吹変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。山吹変更の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、山吹変更を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 バックアウト確認 fre 0339について構成や状態を確認します。rolelist -u user1 監査記録 roles 0340ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きはセキュリティでrolelist -u user1を用い・roles とユーザー属性を確認する。
    - B. 状態を読み取るための働きは性能管理でvmstat -c 2 1を用い・fre とsvmon全体表示を確認する。 ✅
    - C. 状態を読み取るための働きはJFS2でcrfsを用い・lff とマウントオプションを確認する。
    - D. 状態を読み取るための働きはLVMでlsvg -lを用い・STALE PARTITIONS と論理ボリューム配置を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「性能管理でvmstat -c 2 1を用い、fre とsvmon全体表示を確認する」に対応する項目はバックアウト確認 fre（バッ・vmst）です。バックに関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、fre」で、確認対象はvm・バックです。監査・roleのA:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は監査記録 roles（監査・role）です。変更前・crfsのC:は「JFS2でcrfsを用い、lff とマウントオプションを確認する」を述べ、対象は変更前確認 lff（変更・crfs）です。容量・lsvgのD:は「LVMでlsvg -lを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（容量・lsvg）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、fre」を指し、バックアウト確認 freではvm・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 バックアウト確認 fre 0339**

    - 検証目的: 性能管理のvmstat -c 2 1 バックアウト確認 fre 0339について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認099-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0339A
    ```

    画面・出力には AIX0339A が表示され、vmstat -c 2 1 バックアウト確認 fre 0339 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0339B
    ```

    画面・出力には AIX0339B が表示され、vmstat -c 2 1 バックアウト確認 fre 0339 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0339C
    ```

    画面・出力には AIX0339C が表示され、vmstat -c 2 1 バックアウト確認 fre 0339 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0339A が画面・出力に表示されること
    ② ステップ2 の AIX0339B が画面・出力に表示されること
    ③ ステップ3 の AIX0339C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 性能確認 fre 0497 {#c01-i0882}
*分類: 性能管理*  ・  難易度: 初級

初霜確認ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。初霜確認の性能管理では fre とAME統計を復旧票へ残します。初霜確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。初霜確認の注意点として 圧縮メモリー統計の読み落とし を避けるため topas -D も併記します。性能監視の作業票として、初霜確認を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「vmstat -c 2 1 性能確認 fre 0497」を「rolelist -u user1 起動確認 audit class 0498」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はセキュリティでrolelist -u user1を用い・audit class とRBAC属性を確認する。
    - B. 仕様上の役割はJFS2でdefragfsを用い・log=INLINE と内部スナップショットを確認する。
    - C. 仕様上の役割は性能管理でvmstat -c 2 1を用い・fre とAME統計を確認する。 ✅
    - D. 仕様上の役割はLVMでlsvgを用い・PVID と物理ボリューム一覧を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「性能管理でvmstat -c 2 1を用い、fre とAME統計を確認する」に対応する項目は性能確認 fre（性能・vmst）です。性能に関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、fre」で、確認対象はvm・性能です。起動・roleのA:は「セキュリティでrolelist -u user1を用い、audit」を述べ、対象はaudit class（起動・role）です。バック・defrのB:は「JFS2でdefragfsを用い、log=INLINE」を述べ、対象はバックアウト確認 log=INLIN（バッ・defr）です。属性・lsvgのD:は「LVMでlsvgを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は属性確認 PVID（属性・lsvg）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、fre」を指し、性能確認 freではvm・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 性能確認 fre 0497**

    - 検証目的: 性能管理のvmstat -c 2 1 性能確認 fre 0497について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認017-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0497A
    ```

    画面・出力には AIX0497A が表示され、vmstat -c 2 1 性能確認 fre 0497 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0497B
    ```

    画面・出力には AIX0497B が表示され、vmstat -c 2 1 性能確認 fre 0497 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0497C
    ```

    画面・出力には AIX0497C が表示され、vmstat -c 2 1 性能確認 fre 0497 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0497A が画面・出力に表示されること
    ② ステップ2 の AIX0497B が画面・出力に表示されること
    ③ ステップ3 の AIX0497C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 性能確認 pi 0021 {#c01-i0883}
*分類: 性能管理*  ・  難易度: 初級

群青確認ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。群青確認の性能管理では pi とAME統計を判定票へ残します。群青確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。群青確認の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、群青確認を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 性能確認 pi 0021を保守記録に説明する必要があります。rolelist -u user1 起動確認 authorizations 0022と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は性能管理でvmstat -c 2 1を用い・pi とAME統計を確認する。 ✅
    - B. 運用時に利用する技術的役割はセキュリティでrolelist -u user1を用い・authorizationsである。
    - C. 運用時に利用する技術的役割はJFS2でdefragfsを用い・lff と内部スナップショットを確認する。
    - D. 運用時に利用する技術的役割はセキュリティでusrck -n ALLを用い・roles とRBAC属性を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「性能管理でvmstat -c 2 1を用い、pi とAME統計を確認する」に対応する項目は性能確認 pi（性能・vmst）です。性能管理の仕様は「性能管理でvmstat -c 2 1を用い、pi とAME統計を確認する」で、確認対象はvm・性能です。起動・roleのB:は「セキュリティでrolelist -u user1を用い」を述べ、対象は起動確認 authorization（起動・role）です。バック・defrのC:は「JFS2でdefragfsを用い、lff」を述べ、対象はバックアウト確認 lff（バッ・defr）です。変更後・usrcのD:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は変更後確認 roles（変更・usrc）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、pi」を指し、性能確認 piではvm・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 性能確認 pi 0021**

    - 検証目的: 性能管理のvmstat -c 2 1 性能確認 pi 0021について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認021-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0021A
    ```

    画面・出力には AIX0021A が表示され、vmstat -c 2 1 性能確認 pi 0021 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0021B
    ```

    画面・出力には AIX0021B が表示され、vmstat -c 2 1 性能確認 pi 0021 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> topas -D
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0021C
    ```

    画面・出力には AIX0021C が表示され、vmstat -c 2 1 性能確認 pi 0021 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0021A が画面・出力に表示されること
    ② ステップ2 の AIX0021B が画面・出力に表示されること
    ③ ステップ3 の AIX0021C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### vmstat -c 2 1 構成照合 avm 0656 {#c01-i0884}
*分類: 性能管理*  ・  難易度: 中級

若竹判定ではAIX 7.3の性能管理で vmstat -c 2 1 を確認します。若竹判定の性能管理では avm とtopasディスク表示を引継ぎ票へ保管します。若竹判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若竹判定の注意点として 初回サンプルだけの誤判定 を避けるため topas -D も併記します。性能監視の作業票として、若竹判定を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** vmstat -c 2 1 構成照合 avm 0656を同一分類のrolelist -u user1 変更前確認 user attributesと比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は性能管理でvmstat -c 2 1を用い・avm とtopasディスク表示を確認する。 ✅
    - B. コマンドまたは機能の用途はセキュリティでrolelist -u user1を用い・user attributes と監査設定を確認する。
    - C. コマンドまたは機能の用途は導入と起動でinstallp -Cを用い・bootlist とOSレベル表示を確認する。
    - D. コマンドまたは機能の用途はLVMでlsvgを用い・PP SIZE とミラーコピー状態を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「性能管理でvmstat -c 2 1を用い、avm」に対応する項目は構成照合 avm（構成・vmst）です。構成に関する性能管理の仕様は「性能管理でvmstat -c 2 1を用い、avm」で、確認対象はvm・構成です。変更前・roleのB:は「セキュリティでrolelist -u user1を用い、user」を述べ、対象はuser attributes（変更・role）です。監査・instのC:は「導入と起動でinstallp -Cを用い、bootlist」を述べ、対象は監査記録 bootlist（監査・inst）です。変更後・lsvgのD:は「LVMでlsvgを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（変更・lsvg）です。「vmstat -c 2 1」は「性能管理でvmstat -c 2 1を用い、avm」を指し、構成照合 avmではvm・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **vmstat -c 2 1 構成照合 avm 0656**

    - 検証目的: 性能管理のvmstat -c 2 1 構成照合 avm 0656について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合056-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat -c 2 1
    → Enter を押す
    ```

    画面・出力:
    ```text
    kthr     memory             page              faults        cpu
     r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
     1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
    確認コード AIX0656A
    ```

    画面・出力には AIX0656A が表示され、vmstat -c 2 1 構成照合 avm 0656 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> vmstat 2 2
    → Enter を押す
    ```

    画面・出力:
    ```text
    size      inuse       free        pin    virtual
    memory      1048576     417374     631202      66533     151468
    pg space     262144      31993
    確認コード AIX0656B
    ```

    画面・出力には AIX0656B が表示され、vmstat -c 2 1 構成照合 avm 0656 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> svmon -G
    → Enter を押す
    ```

    画面・出力:
    ```text
    Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
    hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
    確認コード AIX0656C
    ```

    画面・出力には AIX0656C が表示され、vmstat -c 2 1 構成照合 avm 0656 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0656A が画面・出力に表示されること
    ② ステップ2 の AIX0656B が画面・出力に表示されること
    ③ ステップ3 の AIX0656C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


