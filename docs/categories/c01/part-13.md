---
search:
  exclude: true
---

# AIX 7.3 — 詳細 (13/18)

[← AIX 7.3 の概要へ戻る](index.md)


## AIX 7.3 > ネットワーク

### netstat -v バックアウト確認 Destination 0005 {#c01-i0636}
*分類: ネットワーク*  ・  難易度: 初級

深雪確認ではAIX 7.3のネットワークで netstat -v を確認します。深雪確認のネットワークでは Destination とMTU属性を復旧票へ残します。深雪確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。深雪確認の注意点として EtherChannel構成対象の誤選択 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、深雪確認を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v バックアウト確認 Destination 0005を保守記録に説明する必要があります。nmon 監査記録 po 0006と取り違えない説明はどれですか。

    - A. 仕様上の役割は性能管理でnmonを用い・po とvmstat表示を確認する。nmon 監査記録 po 0006固有の属性も確認対象に含める。
    - B. 仕様上の役割はネットワークでnetstat -vを用い・Destination とMTU属性を確認する。 ✅
    - C. 仕様上の役割はLVMでlslvを用い・LV STATE とボリュームグループ属性を確認する。
    - D. 仕様上の役割は性能管理でiostat -Dl 2 2を用い・Entitled Capacityである。

    正解: **B** ／ 難易度: 初級

    **解説:** Bの記述「ネットワークでnetstat -vを用い、Destination」に対応する項目はバックアウト確認 Destinati（バッ・nets）です。ネットワークの仕様は「ネットワークでnetstat -vを用い、Destination」で、確認対象はne・バックです。監査・nmonのA:は「性能管理でnmonを用い、po とvmstat表示を確認する」を述べ、対象は監査記録 po（監査・nmon）です。構成・lslvのC:は「LVMでlslvを用い、LV STATE」を述べ、対象はLV STATE（構成・lslv）です。属性・iostのD:は「性能管理でiostat -Dl 2 2を用い、Entitled」を述べ、対象はEntitled Capacity（属性・iost）です。「netstat -v」は「ネットワークでnetstat -vを用い、Destination」を指し、バックアウト確認 Destinatiではne・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v バックアウト確認 Destination 0005**

    - 検証目的: ネットワークのnetstat -v バックアウト確認 Destination 0005について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワークバックアウト確認005-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0005A
    ```

    画面・出力には AIX0005A が表示され、netstat -v バックアウト確認 Destination 0005 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0005B
    ```

    画面・出力には AIX0005B が表示され、netstat -v バックアウト確認 Destination 0005 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0005C
    ```

    画面・出力には AIX0005C が表示され、netstat -v バックアウト確認 Destination 0005 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0005A が画面・出力に表示されること
    ② ステップ2 の AIX0005B が画面・出力に表示されること
    ③ ステップ3 の AIX0005C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v バックアウト確認 EtherChannel 0481 {#c01-i0637}
*分類: ネットワーク*  ・  難易度: 初級

白露確認ではAIX 7.3のネットワークで netstat -v を確認します。白露確認のネットワークでは EtherChannel とMTU属性を採取票へ記録します。白露確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。白露確認の注意点として EtherChannel構成対象の誤選択 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、白露確認を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「netstat -v バックアウト確認 EtherChannel 0481」を「nmon 監査記録 pi 0482」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能はネットワークでnetstat -vを用い・EtherChannel とMTU属性を確認する。 ✅
    - B. 保守作業で参照する機能は性能管理でnmonを用い・pi とvmstat表示を確認する。
    - C. 保守作業で参照する機能はLVMでlslvを用い・STALE PARTITIONS とボリュームグループ属性を確認する。
    - D. 保守作業で参照する機能はデバイス管理でlscfg -vl ent0を用い・path status とデバイス一覧を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「ネットワークでnetstat -vを用い、EtherChannel」に対応する項目はバックアウト確認 EtherChan（バッ・nets）です。バックに関するネットワークの仕様は「ネットワークでnetstat -vを用い、EtherChannel」で、確認対象はne・バックです。監査・nmonのB:は「性能管理でnmonを用い、pi とvmstat表示を確認する」を述べ、対象は監査記録 pi（監査・nmon）です。構成・lslvのC:は「LVMでlslvを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（構成・lslv）です。運用引・lscfのD:は「デバイス管理でlscfg -vl ent0を用い、path」を述べ、対象はpath status（運用・lscf）です。「netstat -v」は「ネットワークでnetstat -vを用い、EtherChannel」を指し、バックアウト確認 EtherChanではne・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v バックアウト確認 EtherChannel 0481**

    - 検証目的: ネットワークのnetstat -v バックアウト確認 EtherChannel 0481について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワークバックアウト確認001-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0481A
    ```

    画面・出力には AIX0481A が表示され、netstat -v バックアウト確認 EtherChannel 0481 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0481B
    ```

    画面・出力には AIX0481B が表示され、netstat -v バックアウト確認 EtherChannel 0481 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0481C
    ```

    画面・出力には AIX0481C が表示され、netstat -v バックアウト確認 EtherChannel 0481 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0481A が画面・出力に表示されること
    ② ステップ2 の AIX0481B が画面・出力に表示されること
    ③ ステップ3 の AIX0481C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 変更後確認 Gateway 0610 {#c01-i0638}
*分類: ネットワーク*  ・  難易度: 初級

桜雲採取ではAIX 7.3のネットワークで netstat -v を確認します。桜雲採取のネットワークでは Gateway とアダプター一覧を保守票へ記録します。桜雲採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。桜雲採取の注意点として jumbo frame前提の不一致 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、桜雲採取を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 変更後確認 Gateway 0610の役割を調べています。nmon 障害切り分け dxm 0611の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容はネットワークでnetstat -vを用い・Gateway とアダプター一覧を確認する。 ✅
    - B. 表示や設定で扱う内容は性能管理でnmonを用い・dxm とsvmon全体表示を確認する。
    - C. 表示や設定で扱う内容はデバイスや sys0 などの属性値を表示するコマンドである。
    - D. 表示や設定で扱う内容はデバイス管理でlscfg -vl ent0を用い・path status とODM属性を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「ネットワークでnetstat -vを用い、Gateway とアダプター一覧を確認する」に対応する項目は変更後確認 Gateway（変更・nets）です。変更後に関するネットワークの仕様は「ネットワークでnetstat -vを用い、Gateway」で、確認対象はne・変更後です。障害切・nmonのB:は「性能管理でnmonを用い、dxm とsvmon全体表示を確認する」を述べ、対象は障害切り分け dxm（障害・nmon）です。状態・ディ・lsatのC:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は状態判定 ディスク状態（状態・lsat）です。バック・lscfのD:は「デバイス管理でlscfg -vl ent0を用い、path」を述べ、対象はpath status（バッ・lscf）です。「netstat -v」は「ネットワークでnetstat -vを用い、Gateway」を指し、変更後確認 Gatewayではne・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 変更後確認 Gateway 0610**

    - 検証目的: ネットワークのnetstat -v 変更後確認 Gateway 0610について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更後確認010-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0610A
    ```

    画面・出力には AIX0610A が表示され、netstat -v 変更後確認 Gateway 0610 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0610B
    ```

    画面・出力には AIX0610B が表示され、netstat -v 変更後確認 Gateway 0610 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0610C
    ```

    画面・出力には AIX0610C が表示され、netstat -v 変更後確認 Gateway 0610 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0610A が画面・出力に表示されること
    ② ステップ2 の AIX0610B が画面・出力に表示されること
    ③ ステップ3 の AIX0610C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 変更後確認 Gateway 0670 {#c01-i0639}
*分類: ネットワーク*  ・  難易度: 中級

早苗判定ではAIX 7.3のネットワークで netstat -v を確認します。早苗判定のネットワークでは Gateway とアダプター一覧を保守票へ記録します。早苗判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。早苗判定の注意点として jumbo frame前提の不一致 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、早苗判定を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 変更後確認 Gateway 0670に関する障害切り分けの前提を確認しています。nmon 障害切り分け Entitled Capacity 0671の機能を混同しない選択肢はどれですか。

    - A. 表示や設定で扱う内容は性能管理でnmonを用い・Entitled Capacity とsvmon全体表示を確認する。
    - B. 表示や設定で扱う内容はSRCとログでerrpt -aを用い・TIMESTAMP とsyslog設定変換を確認する。
    - C. 表示や設定で扱う内容はデバイス管理でdiag -d ent0を用い・microcode level とODM属性を確認する。
    - D. 表示や設定で扱う内容はネットワークでnetstat -vを用い・Gateway とアダプター一覧を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでnetstat -vを用い、Gateway とアダプター一覧を確認する」に対応する項目は変更後確認 Gateway（変更・nets）です。変更後に関するネットワークの仕様は「ネットワークでnetstat -vを用い、Gateway」で、確認対象はne・変更後です。障害切・nmonのA:は「性能管理でnmonを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（障害・nmon）です。容量・errpのB:は「SRCとログでerrpt -aを用い、TIMESTAMP」を述べ、対象は容量確認 TIMESTAMP（容量・errp）です。監査・diagのC:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（監査・diag）です。「netstat -v」は「ネットワークでnetstat -vを用い、Gateway」を指し、変更後確認 Gatewayではne・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 変更後確認 Gateway 0670**

    - 検証目的: ネットワークのnetstat -v 変更後確認 Gateway 0670について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更後確認070-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0670A
    ```

    画面・出力には AIX0670A が表示され、netstat -v 変更後確認 Gateway 0670 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0670B
    ```

    画面・出力には AIX0670B が表示され、netstat -v 変更後確認 Gateway 0670 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0670C
    ```

    画面・出力には AIX0670C が表示され、netstat -v 変更後確認 Gateway 0670 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0670A が画面・出力に表示されること
    ② ステップ2 の AIX0670B が画面・出力に表示されること
    ③ ステップ3 の AIX0670C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 変更後確認 MTU 0134 {#c01-i0640}
*分類: ネットワーク*  ・  難易度: 初級

星霜採取ではAIX 7.3のネットワークで netstat -v を確認します。星霜採取のネットワークでは MTU とアダプター一覧を確認票へ整理します。星霜採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。星霜採取の注意点として jumbo frame前提の不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、星霜採取を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 変更後確認 MTU 0134に関する障害切り分けの前提を確認しています。nmon 障害切り分け Busy% 0135の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は性能管理でnmonを用い・Busy% とsvmon全体表示を確認する。
    - B. 障害切り分けに用いる役割はLVMでlslvを用い・VG STATE と論理ボリューム配置を確認する。
    - C. 障害切り分けに用いる役割はネットワークでnetstat -vを用い・MTU とアダプター一覧を確認する。 ✅
    - D. 障害切り分けに用いる役割は性能管理でiostat -Dl 2 2を用い・pi とsvmon全体表示を確認する。

    正解: **C** ／ 難易度: 初級

    **解説:** Cの記述「ネットワークでnetstat -vを用い、MTU とアダプター一覧を確認する」に対応する項目は変更後確認 MTU（変更・nets）です。変更後に関するネットワークの仕様は「ネットワークでnetstat -vを用い、MTU」で、確認対象はne・変更後です。障害切・nmonのA:は「性能管理でnmonを用い、Busy% とsvmon全体表示を確認する」を述べ、対象は障害切り分け Busy%（障害・nmon）です。属性・lslvのB:は「LVMでlslvを用い、VG STATE」を述べ、対象はVG STATE（属性・lslv）です。性能・iostのD:は「性能管理でiostat -Dl 2 2を用い、pi」を述べ、対象は性能確認 pi（性能・iost）です。「netstat -v」は「ネットワークでnetstat -vを用い、MTU」を指し、変更後確認 MTUではne・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 変更後確認 MTU 0134**

    - 検証目的: ネットワークのnetstat -v 変更後確認 MTU 0134について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更後確認014-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0134A
    ```

    画面・出力には AIX0134A が表示され、netstat -v 変更後確認 MTU 0134 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0134B
    ```

    画面・出力には AIX0134B が表示され、netstat -v 変更後確認 MTU 0134 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0134C
    ```

    画面・出力には AIX0134C が表示され、netstat -v 変更後確認 MTU 0134 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0134A が画面・出力に表示されること
    ② ステップ2 の AIX0134B が画面・出力に表示されること
    ③ ステップ3 の AIX0134C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 変更後確認 MTU 0194 {#c01-i0641}
*分類: ネットワーク*  ・  難易度: 中級

銀嶺判定ではAIX 7.3のネットワークで netstat -v を確認します。銀嶺判定のネットワークでは MTU とアダプター一覧を確認票へ整理します。銀嶺判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。銀嶺判定の注意点として jumbo frame前提の不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、銀嶺判定を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 変更後確認 MTU 0194の役割を調べています。nmon 障害切り分け avm 0195の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は性能管理でnmonを用い・avm とsvmon全体表示を確認する。
    - B. 障害切り分けに用いる役割はネットワークでnetstat -vを用い・MTU とアダプター一覧を確認する。 ✅
    - C. 障害切り分けに用いる役割はLVMでmklvを用い・LV STATE と論理ボリューム配置を確認する。
    - D. 障害切り分けに用いる役割は性能管理でiostat -Dl 2 2を用い・dxm とsvmon全体表示を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「ネットワークでnetstat -vを用い、MTU とアダプター一覧を確認する」に対応する項目は変更後確認 MTU（変更・nets）です。変更後に関するネットワークの仕様は「ネットワークでnetstat -vを用い、MTU」で、確認対象はne・変更後です。障害切・nmonのA:は「性能管理でnmonを用い、avm とsvmon全体表示を確認する」を述べ、対象は障害切り分け avm（障害・nmon）です。状態・mklvのC:は「LVMでmklvを用い、LV STATE」を述べ、対象はLV STATE（状態・mklv）です。性能・iostのD:は「性能管理でiostat -Dl 2 2を用い、dxm」を述べ、対象は性能確認 dxm（性能・iost）です。「netstat -v」は「ネットワークでnetstat -vを用い、MTU」を指し、変更後確認 MTUではne・変更後に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 変更後確認 MTU 0194**

    - 検証目的: ネットワークのnetstat -v 変更後確認 MTU 0194について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更後確認074-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0194A
    ```

    画面・出力には AIX0194A が表示され、netstat -v 変更後確認 MTU 0194 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0194B
    ```

    画面・出力には AIX0194B が表示され、netstat -v 変更後確認 MTU 0194 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0194C
    ```

    画面・出力には AIX0194C が表示され、netstat -v 変更後確認 MTU 0194 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0194A が画面・出力に表示されること
    ② ステップ2 の AIX0194B が画面・出力に表示されること
    ③ ステップ3 の AIX0194C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 属性確認 Link Status 0035 {#c01-i0642}
*分類: ネットワーク*  ・  難易度: 中級

青磁確認ではAIX 7.3のネットワークで netstat -v を確認します。青磁確認のネットワークでは Link Status とEthernet統計を照合票へ整理します。青磁確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。青磁確認の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、青磁確認を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 属性確認 Link Status 0035について構成や状態を確認します。nmon 状態確認 avm 0036ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的は性能管理でnmonを用い・avm とtopasディスク表示を確認する。
    - B. 一次資料が示す主目的はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。
    - C. 一次資料が示す主目的は性能管理でiostat -Dl 2 2を用い・dxm とtopasディスク表示を確認する。
    - D. 一次資料が示す主目的はネットワークでnetstat -vを用い・Link Status とEthernet統計を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでnetstat -vを用い、Link Status」に対応する項目はLink Status（属性・nets）です。ネットワークの仕様は「ネットワークでnetstat -vを用い、Link Status」で、確認対象はne・属性です。状態・nmonのA:は「性能管理でnmonを用い、avm とtopasディスク表示を確認する」を述べ、対象は状態確認 avm（状態・nmon）です。運用引・lslvのB:は「LVMでlslvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・lslv）です。バック・iostのC:は「性能管理でiostat -Dl 2 2を用い、dxm」を述べ、対象はバックアウト確認 dxm（バッ・iost）です。「netstat -v」は「ネットワークでnetstat -vを用い、Link Status」を指し、Link Statusではne・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 属性確認 Link Status 0035**

    - 検証目的: ネットワークのnetstat -v 属性確認 Link Status 0035について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク属性確認035-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0035A
    ```

    画面・出力には AIX0035A が表示され、netstat -v 属性確認 Link Status 0035 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0035B
    ```

    画面・出力には AIX0035B が表示され、netstat -v 属性確認 Link Status 0035 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0035C
    ```

    画面・出力には AIX0035C が表示され、netstat -v 属性確認 Link Status 0035 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0035A が画面・出力に表示されること
    ② ステップ2 の AIX0035B が画面・出力に表示されること
    ③ ステップ3 の AIX0035C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 属性確認 MTU 0511 {#c01-i0643}
*分類: ネットワーク*  ・  難易度: 中級

遠雷確認ではAIX 7.3のネットワークで netstat -v を確認します。遠雷確認のネットワークでは MTU とEthernet統計を点検票へ整理します。遠雷確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。遠雷確認の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、遠雷確認を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 属性確認 MTU 0511の設定や表示を読む前に役割を確認します。nmon 状態確認 Entitled Capacity 0512ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きはネットワークでnetstat -vを用い・MTU とEthernet統計を確認する。 ✅
    - B. 対象資源に対する働きは性能管理でnmonを用い・Entitled Capacity とtopasディスク表示を確認する。
    - C. 対象資源に対する働きはLVMでlslvを用い・VG STATE とミラーコピー状態を確認する。
    - D. 対象資源に対する働きはセキュリティでsetsecattrを用い・audit class とユーザー属性を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「ネットワークでnetstat -vを用い、MTU とEthernet統計を確認する」に対応する項目は属性確認 MTU（属性・nets）です。属性に関するネットワークの仕様は「ネットワークでnetstat -vを用い、MTU」で、確認対象はne・属性です。状態・nmonのB:は「性能管理でnmonを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（状態・nmon）です。運用引・lslvのC:は「LVMでlslvを用い、VG STATE」を述べ、対象はVG STATE（運用・lslv）です。構成・setsのD:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（構成・sets）です。「netstat -v」は「ネットワークでnetstat -vを用い、MTU」を指し、属性確認 MTUではne・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 属性確認 MTU 0511**

    - 検証目的: ネットワークのnetstat -v 属性確認 MTU 0511について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク属性確認031-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0511A
    ```

    画面・出力には AIX0511A が表示され、netstat -v 属性確認 MTU 0511 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0511B
    ```

    画面・出力には AIX0511B が表示され、netstat -v 属性確認 MTU 0511 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0511C
    ```

    画面・出力には AIX0511C が表示され、netstat -v 属性確認 MTU 0511 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0511A が画面・出力に表示されること
    ② ステップ2 の AIX0511B が画面・出力に表示されること
    ③ ステップ3 の AIX0511C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 性能確認 EtherChannel 0164 {#c01-i0644}
*分類: ネットワーク*  ・  難易度: 中級

若草判定ではAIX 7.3のネットワークで netstat -v を確認します。若草判定のネットワークでは EtherChannel と経路表を引継ぎ票へ保管します。若草判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若草判定の注意点として MTU不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、若草判定を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 性能確認 EtherChannel 0164の技術的な意味を資料で確認するとき、nmon 起動確認 po 0165との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は性能管理でnmonを用い・po とAME統計を確認する。
    - B. コマンドまたは機能の用途はLVMでlslvを用い・STALE PARTITIONS と物理ボリューム一覧を確認する。
    - C. コマンドまたは機能の用途は性能管理でiostat -Dl 2 2を用い・Entitled Capacity とAME統計を確認する。
    - D. コマンドまたは機能の用途はネットワークでnetstat -vを用い・EtherChannel と経路表を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでnetstat -vを用い、EtherChannel」に対応する項目は性能確認 EtherChannel（性能・nets）です。性能に関するネットワークの仕様は「ネットワークでnetstat -vを用い、EtherChannel」で、確認対象はne・性能です。起動・nmonのA:は「性能管理でnmonを用い、po とAME統計を確認する」を述べ、対象は起動確認 po（起動・nmon）です。バック・lslvのB:は「LVMでlslvを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（バッ・lslv）です。変更後・iostのC:は「性能管理でiostat -Dl 2 2を用い、Entitled」を述べ、対象はEntitled Capacity（変更・iost）です。「netstat -v」は「ネットワークでnetstat -vを用い、EtherChannel」を指し、性能確認 EtherChannelではne・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 性能確認 EtherChannel 0164**

    - 検証目的: ネットワークのnetstat -v 性能確認 EtherChannel 0164について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク性能確認044-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0164A
    ```

    画面・出力には AIX0164A が表示され、netstat -v 性能確認 EtherChannel 0164 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0164B
    ```

    画面・出力には AIX0164B が表示され、netstat -v 性能確認 EtherChannel 0164 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0164C
    ```

    画面・出力には AIX0164C が表示され、netstat -v 性能確認 EtherChannel 0164 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0164A が画面・出力に表示されること
    ② ステップ2 の AIX0164B が画面・出力に表示されること
    ③ ステップ3 の AIX0164C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 性能確認 EtherChannel 0224 {#c01-i0645}
*分類: ネットワーク*  ・  難易度: 上級

霜月保守ではAIX 7.3のネットワークで netstat -v を確認します。霜月保守のネットワークでは EtherChannel と経路表を引継ぎ票へ保管します。霜月保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。霜月保守の注意点として MTU不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、霜月保守を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 性能確認 EtherChannel 0224を同一分類のnmon 起動確認 Busy% 0225と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途はネットワークでnetstat -vを用い・EtherChannel と経路表を確認する。 ✅
    - B. コマンドまたは機能の用途は性能管理でnmonを用い・Busy% とAME統計を確認する。
    - C. コマンドまたは機能の用途はLVMでmklvを用い・MIRROR WRITE CONSISTENCY と物理ボリューム一覧を確認する。
    - D. コマンドまたは機能の用途は性能管理でiostat -Dl 2 2を用い・pi とAME統計を確認する。

    正解: **A** ／ 難易度: 上級

    **解説:** Aの記述「ネットワークでnetstat -vを用い、EtherChannel」に対応する項目は性能確認 EtherChannel（性能・nets）です。性能に関するネットワークの仕様は「ネットワークでnetstat -vを用い、EtherChannel」で、確認対象はne・性能です。起動・nmonのB:は「性能管理でnmonを用い、Busy% とAME統計を確認する」を述べ、対象は起動確認 Busy%（起動・nmon）です。監査・mklvのC:は「LVMでmklvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（監査・mklv）です。変更後・iostのD:は「性能管理でiostat -Dl 2 2を用い、pi」を述べ、対象は変更後確認 pi（変更・iost）です。「netstat -v」は「ネットワークでnetstat -vを用い、EtherChannel」を指し、性能確認 EtherChannelではne・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 性能確認 EtherChannel 0224**

    - 検証目的: ネットワークのnetstat -v 性能確認 EtherChannel 0224について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク性能確認104-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0224A
    ```

    画面・出力には AIX0224A が表示され、netstat -v 性能確認 EtherChannel 0224 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0224B
    ```

    画面・出力には AIX0224B が表示され、netstat -v 性能確認 EtherChannel 0224 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0224C
    ```

    画面・出力には AIX0224C が表示され、netstat -v 性能確認 EtherChannel 0224 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0224A が画面・出力に表示されること
    ② ステップ2 の AIX0224B が画面・出力に表示されること
    ③ ステップ3 の AIX0224C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 性能確認 Media Speed Running 0640 {#c01-i0646}
*分類: ネットワーク*  ・  難易度: 中級

青葉判定ではAIX 7.3のネットワークで netstat -v を確認します。青葉判定のネットワークでは Media Speed Running と経路表を監査票へ転記します。青葉判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。青葉判定の注意点として MTU不一致 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、青葉判定を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 性能確認 Media Speed Running 0640を同一分類のnmon 起動確認 pi 0641と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明は性能管理でnmonを用い・pi とAME統計を確認する。
    - B. 管理対象との関係を表す説明はSRCとログでerrpt -aを用い・PID とSRCサブシステム表示を確認する。
    - C. 管理対象との関係を表す説明はネットワークでnetstat -vを用い・Media Speed Running と経路表を確認する。 ✅
    - D. 管理対象との関係を表す説明はデバイス管理でlscfg -vl ent0を用い・location code と診断対象表示を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「ネットワークでnetstat -vを用い、Media Speed Running」に対応する項目はSpeed Running（性能・nets）です。性能に関するネットワークの仕様は「ネットワークでnetstat -vを用い、Media Speed」で、確認対象はne・性能です。起動・nmonのA:は「性能管理でnmonを用い、pi とAME統計を確認する」を述べ、対象は起動確認 pi（起動・nmon）です。変更前・errpのB:は「SRCとログでerrpt -aを用い、PID」を述べ、対象は変更前確認 PID（変更・errp）です。属性・lscfのD:は「デバイス管理でlscfg -vl ent0を用い、location」を述べ、対象はlocation code（属性・lscf）です。「netstat -v」は「ネットワークでnetstat -vを用い、Media Speed」を指し、Speed Runningではne・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 性能確認 Media Speed Running 0640**

    - 検証目的: ネットワークのnetstat -v 性能確認 Media Speed Running 0640について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク性能確認040-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0640A
    ```

    画面・出力には AIX0640A が表示され、netstat -v 性能確認 Media Speed Running 0640 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0640B
    ```

    画面・出力には AIX0640B が表示され、netstat -v 性能確認 Media Speed Running 0640 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0640C
    ```

    画面・出力には AIX0640C が表示され、netstat -v 性能確認 Media Speed Running 0640 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0640A が画面・出力に表示されること
    ② ステップ2 の AIX0640B が画面・出力に表示されること
    ③ ステップ3 の AIX0640C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 性能確認 Media Speed Running 0700 {#c01-i0647}
*分類: ネットワーク*  ・  難易度: 上級

薄明保守ではAIX 7.3のネットワークで netstat -v を確認します。薄明保守のネットワークでは Media Speed Running と経路表を監査票へ転記します。薄明保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。薄明保守の注意点として MTU不一致 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、薄明保守を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 性能確認 Media Speed Running 0700の技術的な意味を資料で確認するとき、nmon 起動確認 dxm 0701との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は性能管理でnmonを用い・dxm とAME統計を確認する。nmon 起動確認 dxm 0701固有の属性も確認対象に含める。
    - B. 管理対象との関係を表す説明はネットワークでnetstat -vを用い・Media Speed Running と経路表を確認する。 ✅
    - C. 管理対象との関係を表す説明はSRCとログでerrpt -aを用い・PID とSRCサブシステム表示を確認する。
    - D. 管理対象との関係を表す説明はデバイス管理でdiag -d ent0を用い・attribute と診断対象表示を確認する。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「ネットワークでnetstat -vを用い、Media Speed Running」に対応する項目はSpeed Running（性能・nets）です。性能に関するネットワークの仕様は「ネットワークでnetstat -vを用い、Media Speed」で、確認対象はne・性能です。起動・nmonのA:は「性能管理でnmonを用い、dxm とAME統計を確認する」を述べ、対象は起動確認 dxm（起動・nmon）です。変更前・errpのC:は「SRCとログでerrpt -aを用い、PID」を述べ、対象は変更前確認 PID（変更・errp）です。状態・diagのD:は「デバイス管理でdiag -d ent0を用い、attribute」を述べ、対象は状態確認 attribute（状態・diag）です。「netstat -v」は「ネットワークでnetstat -vを用い、Media Speed」を指し、Speed Runningではne・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 性能確認 Media Speed Running 0700**

    - 検証目的: ネットワークのnetstat -v 性能確認 Media Speed Running 0700について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク性能確認100-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0700A
    ```

    画面・出力には AIX0700A が表示され、netstat -v 性能確認 Media Speed Running 0700 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0700B
    ```

    画面・出力には AIX0700B が表示され、netstat -v 性能確認 Media Speed Running 0700 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0700C
    ```

    画面・出力には AIX0700C が表示され、netstat -v 性能確認 Media Speed Running 0700 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0700A が画面・出力に表示されること
    ② ステップ2 の AIX0700B が画面・出力に表示されること
    ③ ステップ3 の AIX0700C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 構成照合 Gateway 0799 {#c01-i0648}
*分類: ネットワーク*  ・  難易度: 中級

秋桜復旧ではAIX 7.3のネットワークで netstat -v を確認します。秋桜復旧のネットワークでは Gateway とEthernet統計を点検票へ整理します。秋桜復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。秋桜復旧の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、秋桜復旧を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 構成照合 Gateway 0799の設定や表示を読む前に役割を確認します。lslv 詳細確認 構成照合ではなく対象を説明しているものはどれですか。

    - A. 対象資源に対する働きは論理ボリュームの属性と割り当て情報を表示するコマンドである。
    - B. 対象資源に対する働きはネットワークでnetstat -vを用い・Gateway とEthernet統計を確認する。 ✅
    - C. 対象資源に対する働きはデバイス管理でlsdev -Cc diskを用い・Available と診断対象表示を確認する。
    - D. 対象資源に対する働きはセキュリティでsetsecattrを用い・enhanced_RBAC と監査設定を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** 構成・netsでBの記述「ネットワークでnetstat -vを用い、Gateway」に対応する項目は構成照合 Gateway（構成・nets）です。構成に関するネットワークの仕様は「ネットワークでnetstat -vを用い、Gateway」で、確認対象はne・構成です。詳細・構成・lslvのA:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は詳細確認 構成照合（詳細・lslv）です。起動・lsdeのC:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 Available（起動・lsde）です。性能・setsのD:は「セキュリティでsetsecattrを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・sets）です。「netstat -v」は「ネットワークでnetstat -vを用い、Gateway」を指し、構成照合 Gatewayではne・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 構成照合 Gateway 0799**

    - 検証目的: ネットワークのnetstat -v 構成照合 Gateway 0799について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク構成照合079-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0799A
    ```

    画面・出力には AIX0799A が表示され、netstat -v 構成照合 Gateway 0799 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0799B
    ```

    画面・出力には AIX0799B が表示され、netstat -v 構成照合 Gateway 0799 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0799C
    ```

    画面・出力には AIX0799C が表示され、netstat -v 構成照合 Gateway 0799 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0799A が画面・出力に表示されること
    ② ステップ2 の AIX0799B が画面・出力に表示されること
    ③ ステップ3 の AIX0799C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 構成照合 MTU 0323 {#c01-i0649}
*分類: ネットワーク*  ・  難易度: 中級

秋声変更ではAIX 7.3のネットワークで netstat -v を確認します。秋声変更のネットワークでは MTU とEthernet統計を照合票へ整理します。秋声変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。秋声変更の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、秋声変更を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 構成照合 MTU 0323について構成や状態を確認します。chuser 変更前確認 user attributes 0324ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はセキュリティでchuserを用い・user attributes とユーザー属性を確認する。
    - B. 一次資料が示す主目的はLVMでmklvを用い・LV STATE とミラーコピー状態を確認する。
    - C. 一次資料が示す主目的はデバイス管理でdiag -d ent0を用い・attribute と構成マネージャー結果を確認する。
    - D. 一次資料が示す主目的はネットワークでnetstat -vを用い・MTU とEthernet統計を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでnetstat -vを用い、MTU とEthernet統計を確認する」に対応する項目は構成照合 MTU（構成・nets）です。構成に関するネットワークの仕様は「ネットワークでnetstat -vを用い、MTU」で、確認対象はne・構成です。変更前・chusのA:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（変更・chus）です。起動・mklvのB:は「LVMでmklvを用い、LV STATE」を述べ、対象はLV STATE（起動・mklv）です。障害切・diagのC:は「デバイス管理でdiag -d ent0を用い、attribute」を述べ、対象は障害切り分け attribute（障害・diag）です。「netstat -v」は「ネットワークでnetstat -vを用い、MTU」を指し、構成照合 MTUではne・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 構成照合 MTU 0323**

    - 検証目的: ネットワークのnetstat -v 構成照合 MTU 0323について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク構成照合083-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0323A
    ```

    画面・出力には AIX0323A が表示され、netstat -v 構成照合 MTU 0323 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0323B
    ```

    画面・出力には AIX0323B が表示され、netstat -v 構成照合 MTU 0323 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0323C
    ```

    画面・出力には AIX0323C が表示され、netstat -v 構成照合 MTU 0323 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0323A が画面・出力に表示されること
    ② ステップ2 の AIX0323B が画面・出力に表示されること
    ③ ステップ3 の AIX0323C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 運用引継ぎ EtherChannel 0353 {#c01-i0650}
*分類: ネットワーク*  ・  難易度: 上級

朝霧変更ではAIX 7.3のネットワークで netstat -v を確認します。朝霧変更のネットワークでは EtherChannel とMTU属性を復旧票へ残します。朝霧変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。朝霧変更の注意点として EtherChannel構成対象の誤選択 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、朝霧変更を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「netstat -v 運用引継ぎ EtherChannel 0353」を「nmon 容量確認 Entitled Capacity 0354」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はネットワークでnetstat -vを用い・EtherChannel とMTU属性を確認する。 ✅
    - B. 仕様上の役割は性能管理でnmonを用い・Entitled Capacity とvmstat表示を確認する。
    - C. 仕様上の役割はLVMでmklvを用い・MIRROR WRITE CONSISTENCY とボリュームグループ属性を確認する。
    - D. 仕様上の役割はデバイス管理でdiag -d ent0を用い・microcode level とデバイス一覧を確認する。

    正解: **A** ／ 難易度: 上級

    **解説:** Aの記述「ネットワークでnetstat -vを用い、EtherChannel」に対応する項目は運用引継ぎ EtherChannel（運用・nets）です。運用引に関するネットワークの仕様は「ネットワークでnetstat -vを用い、EtherChannel」で、確認対象はne・運用引です。容量・nmonのB:は「性能管理でnmonを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（容量・nmon）です。障害切・mklvのC:は「LVMでmklvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（障害・mklv）です。起動・diagのD:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（起動・diag）です。「netstat -v」は「ネットワークでnetstat -vを用い、EtherChannel」を指し、運用引継ぎ EtherChannelではne・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 運用引継ぎ EtherChannel 0353**

    - 検証目的: ネットワークのnetstat -v 運用引継ぎ EtherChannel 0353について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク運用引継ぎ113-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0353A
    ```

    画面・出力には AIX0353A が表示され、netstat -v 運用引継ぎ EtherChannel 0353 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0353B
    ```

    画面・出力には AIX0353B が表示され、netstat -v 運用引継ぎ EtherChannel 0353 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0353C
    ```

    画面・出力には AIX0353C が表示され、netstat -v 運用引継ぎ EtherChannel 0353 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0353A が画面・出力に表示されること
    ② ステップ2 の AIX0353B が画面・出力に表示されること
    ③ ステップ3 の AIX0353C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### netstat -v 運用引継ぎ Media Speed Running 0829 {#c01-i0651}
*分類: ネットワーク*  ・  難易度: 上級

梅雨晴変更ではAIX 7.3のネットワークで netstat -v を確認します。梅雨晴変更のネットワークでは Media Speed Running とMTU属性を採取票へ記録します。梅雨晴変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。梅雨晴変更の注意点として EtherChannel構成対象の誤選択 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、梅雨晴変更を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** netstat -v 運用引継ぎ Media Speed Running 0829を保守記録に説明する必要があります。chdev 障害切り分け ボリューム状態と取り違えない説明はどれですか。

    - A. 保守作業で参照する機能はデバイス属性を変更する管理コマンドである。chdev 障害切り分け ボリューム状態固有の属性も確認対象に含める。
    - B. 保守作業で参照する機能はデバイス管理でlscfg -vl ent0を用い・path status とODM属性を確認する。
    - C. 保守作業で参照する機能はSRCとログでsyslog_ssw -cを用い・IDENTIFIER とsyslog設定変換を確認する。
    - D. 保守作業で参照する機能はネットワークでnetstat -vを用い・Media Speed Running とMTU属性を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 運用引・netsでDの記述「ネットワークでnetstat -vを用い、Media Speed」に対応する項目はSpeed Running（運用・nets）です。運用引に関するネットワークの仕様は「ネットワークでnetstat -vを用い、Media Speed」で、確認対象はne・運用引です。障害切・chdeのA:は「デバイス属性を変更する管理コマンド」を述べ、対象は障害切り分け ボリューム状態（障害・chde）です。バック・lscfのB:は「デバイス管理でlscfg -vl ent0を用い、path」を述べ、対象はpath status（バッ・lscf）です。構成・syslのC:は「SRCとログでsyslog_ssw -cを用い」を述べ、対象は構成照合 IDENTIFIER（構成・sysl）です。「netstat -v」は「ネットワークでnetstat -vを用い、Media Speed」を指し、Speed Runningではne・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **netstat -v 運用引継ぎ Media Speed Running 0829**

    - 検証目的: ネットワークのnetstat -v 運用引継ぎ Media Speed Running 0829について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク運用引継ぎ109-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -v
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0829A
    ```

    画面・出力には AIX0829A が表示され、netstat -v 運用引継ぎ Media Speed Running 0829 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0829B
    ```

    画面・出力には AIX0829B が表示され、netstat -v 運用引継ぎ Media Speed Running 0829 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0829C
    ```

    画面・出力には AIX0829C が表示され、netstat -v 運用引継ぎ Media Speed Running 0829 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0829A が画面・出力に表示されること
    ② ステップ2 の AIX0829B が画面・出力に表示されること
    ③ ステップ3 の AIX0829C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a バックアウト確認 Gateway 0255 {#c01-i0652}
*分類: ネットワーク*  ・  難易度: 初級

岩清水監査ではAIX 7.3のネットワークで no -a を確認します。岩清水監査のネットワークでは Gateway とEthernet統計を作業票へ保管します。岩清水監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。岩清水監査の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、岩清水監査を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** no -a バックアウト確認 Gateway 0255の設定や表示を読む前に役割を確認します。pwdck -n ALL 監査記録 enhanced_RBAC 0256ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはセキュリティでpwdck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。
    - B. 状態を読み取るための働きはLVMでchlvを用い・PP SIZE とミラーコピー状態を確認する。
    - C. 状態を読み取るための働きは構成済みデバイスと VPD を表示するコマンドである。
    - D. 状態を読み取るための働きはネットワークでno -aを用い・Gateway とEthernet統計を確認する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「ネットワークでno -aを用い、Gateway とEthernet統計を確認する」に対応する項目はバックアウト確認 Gateway（バッ・no）です。バックに関するネットワークの仕様は「ネットワークでno -aを用い、Gateway」で、確認対象はno・バックです。監査・pwdcのA:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・pwdc）です。構成・chlvのB:は「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（構成・chlv）です。性能・ペー・lscfのC:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は性能確認 ページング状態（性能・lscf）です。「no -a」は「ネットワークでno -aを用い、Gateway」を指し、バックアウト確認 Gatewayではno・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a バックアウト確認 Gateway 0255**

    - 検証目的: ネットワークのno -a バックアウト確認 Gateway 0255について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワークバックアウト確認015-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0255A
    ```

    画面・出力には AIX0255A が表示され、no -a バックアウト確認 Gateway 0255 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0255B
    ```

    画面・出力には AIX0255B が表示され、no -a バックアウト確認 Gateway 0255 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0255C
    ```

    画面・出力には AIX0255C が表示され、no -a バックアウト確認 Gateway 0255 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0255A が画面・出力に表示されること
    ② ステップ2 の AIX0255B が画面・出力に表示されること
    ③ ステップ3 の AIX0255C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a バックアウト確認 Gateway 0315 {#c01-i0653}
*分類: ネットワーク*  ・  難易度: 中級

青磁復旧ではAIX 7.3のネットワークで no -a を確認します。青磁復旧のネットワークでは Gateway とEthernet統計を作業票へ保管します。青磁復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。青磁復旧の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、青磁復旧を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** no -a バックアウト確認 Gateway 0315について構成や状態を確認します。lparstat -i 監査記録 PhysB 0316ではなく対象機能を表す記述はどれですか。

    - A. 状態を読み取るための働きは性能管理でlparstat -iを用い・PhysB とtopasディスク表示を確認する。
    - B. 状態を読み取るための働きはLVMでmirrorvgを用い・STALE PARTITIONS とミラーコピー状態を確認する。
    - C. 状態を読み取るための働きはデバイス管理でbootinfo -B hdisk0を用い・path statusである。
    - D. 状態を読み取るための働きはネットワークでno -aを用い・Gateway とEthernet統計を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでno -aを用い、Gateway とEthernet統計を確認する」に対応する項目はバックアウト確認 Gateway（バッ・no）です。バックに関するネットワークの仕様は「ネットワークでno -aを用い、Gateway」で、確認対象はno・バックです。監査・lparのA:は「性能管理でlparstat -iを用い、PhysB」を述べ、対象は監査記録 PhysB（監査・lpar）です。変更前・mirrのB:は「LVMでmirrorvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（変更・mirr）です。容量・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い、path」を述べ、対象はpath status（容量・boot）です。「no -a」は「ネットワークでno -aを用い、Gateway」を指し、バックアウト確認 Gatewayではno・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a バックアウト確認 Gateway 0315**

    - 検証目的: ネットワークのno -a バックアウト確認 Gateway 0315について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワークバックアウト確認075-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0315A
    ```

    画面・出力には AIX0315A が表示され、no -a バックアウト確認 Gateway 0315 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0315B
    ```

    画面・出力には AIX0315B が表示され、no -a バックアウト確認 Gateway 0315 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0315C
    ```

    画面・出力には AIX0315C が表示され、no -a バックアウト確認 Gateway 0315 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0315A が画面・出力に表示されること
    ② ステップ2 の AIX0315B が画面・出力に表示されること
    ③ ステップ3 の AIX0315C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a バックアウト確認 Link Status 0731 {#c01-i0654}
*分類: ネットワーク*  ・  難易度: 初級

松風監査ではAIX 7.3のネットワークで no -a を確認します。松風監査のネットワークでは Link Status とEthernet統計を照合票へ整理します。松風監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。松風監査の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、松風監査を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** no -a バックアウト確認 Link Status 0731について構成や状態を確認します。pwdck -n ALL 監査記録 roles 0732ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はネットワークでno -aを用い・Link Status とEthernet統計を確認する。 ✅
    - B. 一次資料が示す主目的はセキュリティでpwdck -n ALLを用い・roles とユーザー属性を確認する。
    - C. 一次資料が示す主目的はSRCとログでerrclearを用い・syslog.conf とinetdデバッグ出力を確認する。
    - D. 一次資料が示す主目的はデバイス管理でrmdev -Rl ent1を用い・microcode levelである。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「ネットワークでno -aを用い、Link Status」に対応する項目はLink Status（バッ・no）です。バックに関するネットワークの仕様は「ネットワークでno -aを用い、Link Status」で、確認対象はno・バックです。監査・pwdcのB:は「セキュリティでpwdck -n ALLを用い、roles」を述べ、対象は監査記録 roles（監査・pwdc）です。性能・errcのC:は「SRCとログでerrclearを用い、syslog.conf」を述べ、対象は性能確認 syslog.conf（性能・errc）です。運用引・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象はmicrocode level（運用・rmde）です。「no -a」は「ネットワークでno -aを用い、Link Status」を指し、Link Statusではno・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a バックアウト確認 Link Status 0731**

    - 検証目的: ネットワークのno -a バックアウト確認 Link Status 0731について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワークバックアウト確認011-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0731A
    ```

    画面・出力には AIX0731A が表示され、no -a バックアウト確認 Link Status 0731 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0731B
    ```

    画面・出力には AIX0731B が表示され、no -a バックアウト確認 Link Status 0731 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0731C
    ```

    画面・出力には AIX0731C が表示され、no -a バックアウト確認 Link Status 0731 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0731A が画面・出力に表示されること
    ② ステップ2 の AIX0731B が画面・出力に表示されること
    ③ ステップ3 の AIX0731C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a バックアウト確認 Link Status 0791 {#c01-i0655}
*分類: ネットワーク*  ・  難易度: 中級

遠雷復旧ではAIX 7.3のネットワークで no -a を確認します。遠雷復旧のネットワークでは Link Status とEthernet統計を照合票へ整理します。遠雷復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。遠雷復旧の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、遠雷復旧を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** no -a バックアウト確認 Link Status 0791の設定や表示を読む前に役割を確認します。lsattr 性能確認 実行結果ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はデバイスや sys0 などの属性値を表示するコマンドである。
    - B. 一次資料が示す主目的はセキュリティでrolelist -u user1を用い・roles と監査設定を確認する。
    - C. 一次資料が示す主目的はLVMでlspvを用い・STALE PARTITIONS と論理ボリューム配置を確認する。
    - D. 一次資料が示す主目的はネットワークでno -aを用い・Link Status とEthernet統計を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** バック・noでDの記述「ネットワークでno -aを用い、Link Status」に対応する項目はLink Status（バッ・no）です。バックに関するネットワークの仕様は「ネットワークでno -aを用い、Link Status」で、確認対象はno・バックです。性能・実行・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は性能確認 実行結果（性能・lsat）です。変更前・roleのB:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は変更前確認 roles（変更・role）です。障害切・lspvのC:は「LVMでlspvを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（障害・lspv）です。「no -a」は「ネットワークでno -aを用い、Link Status」を指し、Link Statusではno・バックに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a バックアウト確認 Link Status 0791**

    - 検証目的: ネットワークのno -a バックアウト確認 Link Status 0791について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワークバックアウト確認071-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0791A
    ```

    画面・出力には AIX0791A が表示され、no -a バックアウト確認 Link Status 0791 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0791B
    ```

    画面・出力には AIX0791B が表示され、no -a バックアウト確認 Link Status 0791 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0791C
    ```

    画面・出力には AIX0791C が表示され、no -a バックアウト確認 Link Status 0791 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0791A が画面・出力に表示されること
    ② ステップ2 の AIX0791B が画面・出力に表示されること
    ③ ステップ3 の AIX0791C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a 属性確認 Destination 0761 {#c01-i0656}
*分類: ネットワーク*  ・  難易度: 中級

白露復旧ではAIX 7.3のネットワークで no -a を確認します。白露復旧のネットワークでは Destination とMTU属性を復旧票へ残します。白露復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。白露復旧の注意点として EtherChannel構成対象の誤選択 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、白露復旧を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「no -a 属性確認 Destination 0761」を「lparstat -i 状態確認 avm 0762」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 仕様上の役割はネットワークでno -aを用い・Destination とMTU属性を確認する。 ✅
    - B. 仕様上の役割は性能管理でlparstat -iを用い・avm とvmstat表示を確認する。
    - C. 仕様上の役割はSRCとログでstartsrc -s inetd -aを用い・IDENTIFIERである。
    - D. 仕様上の役割はデバイス管理でrmdev -Rl ent1を用い・attribute とデバイス一覧を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「ネットワークでno -aを用い、Destination とMTU属性を確認する」に対応する項目は属性確認 Destination（属性・no）です。属性に関するネットワークの仕様は「ネットワークでno -aを用い、Destination」で、確認対象はno・属性です。状態・lparのB:は「性能管理でlparstat -iを用い、avm」を述べ、対象は状態確認 avm（状態・lpar）です。障害切・starのC:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け IDENTIFIER（障害・star）です。構成・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は構成照合 attribute（構成・rmde）です。「no -a」は「ネットワークでno -aを用い、Destination」を指し、属性確認 Destinationではno・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a 属性確認 Destination 0761**

    - 検証目的: ネットワークのno -a 属性確認 Destination 0761について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク属性確認041-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0761A
    ```

    画面・出力には AIX0761A が表示され、no -a 属性確認 Destination 0761 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0761B
    ```

    画面・出力には AIX0761B が表示され、no -a 属性確認 Destination 0761 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0761C
    ```

    画面・出力には AIX0761C が表示され、no -a 属性確認 Destination 0761 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0761A が画面・出力に表示されること
    ② ステップ2 の AIX0761B が画面・出力に表示されること
    ③ ステップ3 の AIX0761C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a 属性確認 Destination 0821 {#c01-i0657}
*分類: ネットワーク*  ・  難易度: 上級

群青変更ではAIX 7.3のネットワークで no -a を確認します。群青変更のネットワークでは Destination とMTU属性を復旧票へ残します。群青変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。群青変更の注意点として EtherChannel構成対象の誤選択 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、群青変更を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** no -a 属性確認 Destination 0821を保守記録に説明する必要があります。bootinfo -B hdisk0 起動確認 attribute 0832と取り違えない説明はどれですか。

    - A. 仕様上の役割はデバイス管理でbootinfo -B hdisk0を用い・attributeである。
    - B. 仕様上の役割はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。
    - C. 仕様上の役割はセキュリティでrbacqry -u user1 -Tを用い・user attributesである。
    - D. 仕様上の役割はネットワークでno -aを用い・Destination とMTU属性を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** 属性・noでDの記述「ネットワークでno -aを用い、Destination」に対応する項目は属性確認 Destination（属性・no）です。属性に関するネットワークの仕様は「ネットワークでno -aを用い、Destination」で、確認対象はno・属性です。起動・bootのA:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は起動確認 attribute（起動・boot）です。運用引・lslvのB:は「LVMでlslvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・lslv）です。属性・rbacのC:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はuser attributes（属性・rbac）です。「no -a」は「ネットワークでno -aを用い、Destination」を指し、属性確認 Destinationではno・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a 属性確認 Destination 0821**

    - 検証目的: ネットワークのno -a 属性確認 Destination 0821について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク属性確認101-07
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0821A
    ```

    画面・出力には AIX0821A が表示され、no -a 属性確認 Destination 0821 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0821B
    ```

    画面・出力には AIX0821B が表示され、no -a 属性確認 Destination 0821 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0821C
    ```

    画面・出力には AIX0821C が表示され、no -a 属性確認 Destination 0821 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0821A が画面・出力に表示されること
    ② ステップ2 の AIX0821B が画面・出力に表示されること
    ③ ステップ3 の AIX0821C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a 属性確認 Media Speed Running 0285 {#c01-i0658}
*分類: ネットワーク*  ・  難易度: 中級

深雪復旧ではAIX 7.3のネットワークで no -a を確認します。深雪復旧のネットワークでは Media Speed Running とMTU属性を判定票へ残します。深雪復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。深雪復旧の注意点として EtherChannel構成対象の誤選択 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、深雪復旧を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** no -a 属性確認 Media Speed Running 0285を保守記録に説明する必要があります。lparstat -i 状態確認 fre 0286と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は性能管理でlparstat -iを用い・fre とvmstat表示を確認する。lparstat -i 状態確認 fre 0286固有の属性も確認対象に含める。
    - B. 運用時に利用する技術的役割はLVMでchlvを用い・PVID とボリュームグループ属性を確認する。
    - C. 運用時に利用する技術的役割は構成済みデバイスと VPD を表示するコマンドである。
    - D. 運用時に利用する技術的役割はネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでno -aを用い、Media Speed Running」に対応する項目はSpeed Running（属性・no）です。属性に関するネットワークの仕様は「ネットワークでno -aを用い、Media Speed」で、確認対象はno・属性です。状態・lparのA:は「性能管理でlparstat -iを用い、fre」を述べ、対象は状態確認 fre（状態・lpar）です。運用引・chlvのB:は「LVMでchlvを用い、PVID とボリュームグループ属性を確認する」を述べ、対象は運用引継ぎ PVID（運用・chlv）です。変更前・lscfのC:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は変更前確認 障害記録（変更・lscf）です。「no -a」は「ネットワークでno -aを用い、Media Speed」を指し、Speed Runningではno・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a 属性確認 Media Speed Running 0285**

    - 検証目的: ネットワークのno -a 属性確認 Media Speed Running 0285について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク属性確認045-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0285A
    ```

    画面・出力には AIX0285A が表示され、no -a 属性確認 Media Speed Running 0285 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0285B
    ```

    画面・出力には AIX0285B が表示され、no -a 属性確認 Media Speed Running 0285 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0285C
    ```

    画面・出力には AIX0285C が表示され、no -a 属性確認 Media Speed Running 0285 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0285A が画面・出力に表示されること
    ② ステップ2 の AIX0285B が画面・出力に表示されること
    ③ ステップ3 の AIX0285C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a 属性確認 Media Speed Running 0345 {#c01-i0659}
*分類: ネットワーク*  ・  難易度: 上級

花冷変更ではAIX 7.3のネットワークで no -a を確認します。花冷変更のネットワークでは Media Speed Running とMTU属性を判定票へ残します。花冷変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。花冷変更の注意点として EtherChannel構成対象の誤選択 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、花冷変更を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「no -a 属性確認 Media Speed Running 0345」を「lparstat -i 状態確認 csz 0346」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 運用時に利用する技術的役割は性能管理でlparstat -iを用い・csz とvmstat表示を確認する。
    - B. 運用時に利用する技術的役割はLVMでmirrorvgを用い・VG STATE とボリュームグループ属性を確認する。mirrorvg 容量確認 VG STATE 0651固有の属性も確認対象に含める。
    - C. 運用時に利用する技術的役割はデバイス管理でbootinfo -B hdisk0を用い・location codeである。
    - D. 運用時に利用する技術的役割はネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。 ✅

    正解: **D** ／ 難易度: 上級

    **解説:** Dの記述「ネットワークでno -aを用い、Media Speed Running」に対応する項目はSpeed Running（属性・no）です。属性に関するネットワークの仕様は「ネットワークでno -aを用い、Media Speed」で、確認対象はno・属性です。状態・lparのA:は「性能管理でlparstat -iを用い、csz」を述べ、対象は状態確認 csz（状態・lpar）です。容量・mirrのB:は「LVMでmirrorvgを用い、VG STATE」を述べ、対象はVG STATE（容量・mirr）です。変更前・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象はlocation code（変更・boot）です。「no -a」は「ネットワークでno -aを用い、Media Speed」を指し、Speed Runningではno・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a 属性確認 Media Speed Running 0345**

    - 検証目的: ネットワークのno -a 属性確認 Media Speed Running 0345について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク属性確認105-03
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0345A
    ```

    画面・出力には AIX0345A が表示され、no -a 属性確認 Media Speed Running 0345 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0345B
    ```

    画面・出力には AIX0345B が表示され、no -a 属性確認 Media Speed Running 0345 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0345C
    ```

    画面・出力には AIX0345C が表示され、no -a 属性確認 Media Speed Running 0345 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0345A が画面・出力に表示されること
    ② ステップ2 の AIX0345B が画面・出力に表示されること
    ③ ステップ3 の AIX0345C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a 性能確認 Link Status 0474 {#c01-i0660}
*分類: ネットワーク*  ・  難易度: 上級

銀嶺整理ではAIX 7.3のネットワークで no -a を確認します。銀嶺整理のネットワークでは Link Status とアダプター一覧を変更票へ記録します。銀嶺整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。銀嶺整理の注意点として jumbo frame前提の不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、銀嶺整理を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** no -a 性能確認 Link Status 0474の役割を調べています。lparstat -i 起動確認 PhysB 0475の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては性能管理でlparstat -iを用い・PhysB とsvmon全体表示を確認する。
    - B. 機能の説明としてはLVMでmirrorvgを用い・PVID と論理ボリューム配置を確認する。
    - C. 機能の説明としてはネットワークでno -aを用い・Link Status とアダプター一覧を確認する。 ✅
    - D. 機能の説明としてはデバイス管理でbootinfo -B hdisk0を用い・location code とODM属性を確認する。

    正解: **C** ／ 難易度: 上級

    **解説:** Cの記述「ネットワークでno -aを用い、Link Status とアダプター一覧を確認する」に対応する項目はLink Status（性能・no）です。性能に関するネットワークの仕様は「ネットワークでno -aを用い、Link Status」で、確認対象はno・性能です。起動・lparのA:は「性能管理でlparstat -iを用い、PhysB」を述べ、対象は起動確認 PhysB（起動・lpar）です。監査・mirrのB:は「LVMでmirrorvgを用い、PVID」を述べ、対象は監査記録 PVID（監査・mirr）です。状態・bootのD:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象はlocation code（状態・boot）です。「no -a」は「ネットワークでno -aを用い、Link Status」を指し、Link Statusではno・性能に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a 性能確認 Link Status 0474**

    - 検証目的: ネットワークのno -a 性能確認 Link Status 0474について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク性能確認114-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0474A
    ```

    画面・出力には AIX0474A が表示され、no -a 性能確認 Link Status 0474 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0474B
    ```

    画面・出力には AIX0474B が表示され、no -a 性能確認 Link Status 0474 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0474C
    ```

    画面・出力には AIX0474C が表示され、no -a 性能確認 Link Status 0474 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0474A が画面・出力に表示されること
    ② ステップ2 の AIX0474B が画面・出力に表示されること
    ③ ステップ3 の AIX0474C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a 構成照合 Destination 0632 {#c01-i0661}
*分類: ネットワーク*  ・  難易度: 中級

夕映採取ではAIX 7.3のネットワークで no -a を確認します。夕映採取のネットワークでは Destination と経路表を引継ぎ票へ保管します。夕映採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。夕映採取の注意点として MTU不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、夕映採取を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** no -a 構成照合 Destination 0632を同一分類のlparstat -i 変更前確認 PhysB 0633と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. コマンドまたは機能の用途は性能管理でlparstat -iを用い・PhysB とAME統計を確認する。
    - B. コマンドまたは機能の用途はSRCとログでstartsrc -s inetd -aを用い・IDENTIFIERである。
    - C. コマンドまたは機能の用途はネットワークでno -aを用い・Destination と経路表を確認する。 ✅
    - D. コマンドまたは機能の用途はデバイス管理でrmdev -Rl ent1を用い・PVID と診断対象表示を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「ネットワークでno -aを用い、Destination と経路表を確認する」に対応する項目は構成照合 Destination（構成・no）です。構成に関するネットワークの仕様は「ネットワークでno -aを用い、Destination」で、確認対象はno・構成です。変更前・lparのA:は「性能管理でlparstat -iを用い、PhysB」を述べ、対象は変更前確認 PhysB（変更・lpar）です。監査・starのB:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は監査記録 IDENTIFIER（監査・star）です。変更後・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い、PVID」を述べ、対象は変更後確認 PVID（変更・rmde）です。「no -a」は「ネットワークでno -aを用い、Destination」を指し、構成照合 Destinationではno・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a 構成照合 Destination 0632**

    - 検証目的: ネットワークのno -a 構成照合 Destination 0632について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク構成照合032-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0632A
    ```

    画面・出力には AIX0632A が表示され、no -a 構成照合 Destination 0632 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0632B
    ```

    画面・出力には AIX0632B が表示され、no -a 構成照合 Destination 0632 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0632C
    ```

    画面・出力には AIX0632C が表示され、no -a 構成照合 Destination 0632 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0632A が画面・出力に表示されること
    ② ステップ2 の AIX0632B が画面・出力に表示されること
    ③ ステップ3 の AIX0632C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a 構成照合 Media Speed Running 0156 {#c01-i0662}
*分類: ネットワーク*  ・  難易度: 中級

若潮採取ではAIX 7.3のネットワークで no -a を確認します。若潮採取のネットワークでは Media Speed Running と経路表を同じ証跡に残します。若潮採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若潮採取の注意点として MTU不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、若潮採取を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** no -a 構成照合 Media Speed Running 0156の技術的な意味を資料で確認するとき、lparstat -i 変更前確認 Entitled Capacity 0157との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は性能管理でlparstat -iを用い・Entitled Capacity とAME統計を確認する。
    - B. 構成を確認する際の意味はLVMでchlvを用い・PVID と物理ボリューム一覧を確認する。
    - C. 構成を確認する際の意味はネットワークでno -aを用い・Media Speed Running と経路表を確認する。 ✅
    - D. 構成を確認する際の意味は性能管理でtopas -Cを用い・csz とAME統計を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「ネットワークでno -aを用い、Media Speed Running」に対応する項目はSpeed Running（構成・no）です。構成に関するネットワークの仕様は「ネットワークでno -aを用い、Media Speed」で、確認対象はno・構成です。変更前・lparのA:は「性能管理でlparstat -iを用い、Entitled」を述べ、対象はEntitled Capacity（変更・lpar）です。性能・chlvのB:は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は性能確認 PVID（性能・chlv）です。運用引・topaのD:は「性能管理でtopas -Cを用い、csz とAME統計を確認する」を述べ、対象は運用引継ぎ csz（運用・topa）です。「no -a」は「ネットワークでno -aを用い、Media Speed」を指し、Speed Runningではno・構成に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a 構成照合 Media Speed Running 0156**

    - 検証目的: ネットワークのno -a 構成照合 Media Speed Running 0156について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク構成照合036-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0156A
    ```

    画面・出力には AIX0156A が表示され、no -a 構成照合 Media Speed Running 0156 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0156B
    ```

    画面・出力には AIX0156B が表示され、no -a 構成照合 Media Speed Running 0156 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0156C
    ```

    画面・出力には AIX0156C が表示され、no -a 構成照合 Media Speed Running 0156 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0156A が画面・出力に表示されること
    ② ステップ2 の AIX0156B が画面・出力に表示されること
    ③ ステップ3 の AIX0156C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a 運用引継ぎ Gateway 0126 {#c01-i0663}
*分類: ネットワーク*  ・  難易度: 初級

朝凪採取ではAIX 7.3のネットワークで no -a を確認します。朝凪採取のネットワークでは Gateway とアダプター一覧を変更票へ記録します。朝凪採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。朝凪採取の注意点として jumbo frame前提の不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、朝凪採取を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** no -a 運用引継ぎ Gateway 0126に関する障害切り分けの前提を確認しています。lparstat -i 容量確認 pi 0127の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としてはネットワークでno -aを用い・Gateway とアダプター一覧を確認する。 ✅
    - B. 機能の説明としては性能管理でlparstat -iを用い・pi とsvmon全体表示を確認する。
    - C. 機能の説明としてはLVMでchlvを用い・PP SIZE と論理ボリューム配置を確認する。
    - D. 機能の説明としては性能管理でtopas -Cを用い・PhysB とsvmon全体表示を確認する。

    正解: **A** ／ 難易度: 初級

    **解説:** Aの記述「ネットワークでno -aを用い、Gateway とアダプター一覧を確認する」に対応する項目は運用引継ぎ Gateway（運用・no）です。運用引に関するネットワークの仕様は「ネットワークでno -aを用い、Gateway」で、確認対象はno・運用引です。容量・lparのB:は「性能管理でlparstat -iを用い、pi」を述べ、対象は容量確認 pi（容量・lpar）です。変更後・chlvのC:は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」を述べ、対象はPP SIZE（変更・chlv）です。構成・topaのD:は「性能管理でtopas -Cを用い、PhysB」を述べ、対象は構成照合 PhysB（構成・topa）です。「no -a」は「ネットワークでno -aを用い、Gateway」を指し、運用引継ぎ Gatewayではno・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a 運用引継ぎ Gateway 0126**

    - 検証目的: ネットワークのno -a 運用引継ぎ Gateway 0126について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク運用引継ぎ006-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0126A
    ```

    画面・出力には AIX0126A が表示され、no -a 運用引継ぎ Gateway 0126 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0126B
    ```

    画面・出力には AIX0126B が表示され、no -a 運用引継ぎ Gateway 0126 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0126C
    ```

    画面・出力には AIX0126C が表示され、no -a 運用引継ぎ Gateway 0126 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0126A が画面・出力に表示されること
    ② ステップ2 の AIX0126B が画面・出力に表示されること
    ③ ステップ3 の AIX0126C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### no -a 運用引継ぎ Link Status 0602 {#c01-i0664}
*分類: ネットワーク*  ・  難易度: 初級

春分採取ではAIX 7.3のネットワークで no -a を確認します。春分採取のネットワークでは Link Status とアダプター一覧を確認票へ整理します。春分採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。春分採取の注意点として jumbo frame前提の不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、春分採取を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** no -a 運用引継ぎ Link Status 0602の役割を調べています。lparstat -i 容量確認 fre 0603の説明を混ぜずに採るべき記述はどれですか。

    - A. 障害切り分けに用いる役割は性能管理でlparstat -iを用い・fre とsvmon全体表示を確認する。
    - B. 障害切り分けに用いる役割はネットワークでno -aを用い・Link Status とアダプター一覧を確認する。 ✅
    - C. 障害切り分けに用いる役割は構成済みデバイスと VPD を表示するコマンドである。
    - D. 障害切り分けに用いる役割はデバイス管理でrmdev -Rl ent1を用い・Available とODM属性を確認する。

    正解: **B** ／ 難易度: 初級

    **解説:** Bの記述「ネットワークでno -aを用い、Link Status とアダプター一覧を確認する」に対応する項目はLink Status（運用・no）です。運用引に関するネットワークの仕様は「ネットワークでno -aを用い、Link Status」で、確認対象はno・運用引です。容量・lparのA:は「性能管理でlparstat -iを用い、fre」を述べ、対象は容量確認 fre（容量・lpar）です。詳細・除外・lscfのC:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は詳細確認 除外条件（詳細・lscf）です。性能・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は性能確認 Available（性能・rmde）です。「no -a」は「ネットワークでno -aを用い、Link Status」を指し、Link Statusではno・運用引に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **no -a 運用引継ぎ Link Status 0602**

    - 検証目的: ネットワークのno -a 運用引継ぎ Link Status 0602について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク運用引継ぎ002-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> no -a
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0602A
    ```

    画面・出力には AIX0602A が表示され、no -a 運用引継ぎ Link Status 0602 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0602B
    ```

    画面・出力には AIX0602B が表示され、no -a 運用引継ぎ Link Status 0602 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0602C
    ```

    画面・出力には AIX0602C が表示され、no -a 運用引継ぎ Link Status 0602 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0602A が画面・出力に表示されること
    ② ステップ2 の AIX0602B が画面・出力に表示されること
    ③ ステップ3 の AIX0602C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### route -n get 変更前確認 Gateway 0693 {#c01-i0665}
*分類: ネットワーク*  ・  難易度: 中級

月影保守ではAIX 7.3のネットワークで route -n get を確認します。月影保守のネットワークでは Gateway とMTU属性を判定票へ残します。月影保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。月影保守の注意点として EtherChannel構成対象の誤選択 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、月影保守を引継ぎ材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** route -n get 変更前確認 Gateway 0693を保守記録に説明する必要があります。vmo -a 変更後確認 fre 0694と取り違えない説明はどれですか。

    - A. 運用時に利用する技術的役割は性能管理でvmo -aを用い・fre とvmstat表示を確認する。
    - B. 運用時に利用する技術的役割はSRCとログでtail -f /tmp/myfileを用い・TIMESTAMP とエラーログ一覧を確認する。
    - C. 運用時に利用する技術的役割はネットワークでroute -n getを用い・Gateway とMTU属性を確認する。 ✅
    - D. 運用時に利用する技術的役割はデバイス管理でlsmpio -l hdisk0を用い・path status とデバイス一覧を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「ネットワークでroute -n getを用い、Gateway とMTU属性を確認する」に対応する項目は変更前確認 Gateway（変更・rout）です。変更前に関するネットワークの仕様は「ネットワークでroute -n getを用い、Gateway」で、確認対象はro・変更前です。変更後・vmoのA:は「性能管理でvmo -aを用い、fre とvmstat表示を確認する」を述べ、対象は変更後確認 fre（変更・vmo）です。運用引・tailのB:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は運用引継ぎ TIMESTAMP（運用・tail）です。バック・lsmpのD:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（バッ・lsmp）です。「route -n get」は「ネットワークでroute -n getを用い、Gateway」を指し、変更前確認 Gatewayではro・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **route -n get 変更前確認 Gateway 0693**

    - 検証目的: ネットワークのroute -n get 変更前確認 Gateway 0693について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更前確認093-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> route -n get
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0693A
    ```

    画面・出力には AIX0693A が表示され、route -n get 変更前確認 Gateway 0693 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0693B
    ```

    画面・出力には AIX0693B が表示され、route -n get 変更前確認 Gateway 0693 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0693C
    ```

    画面・出力には AIX0693C が表示され、route -n get 変更前確認 Gateway 0693 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0693A が画面・出力に表示されること
    ② ステップ2 の AIX0693B が画面・出力に表示されること
    ③ ステップ3 の AIX0693C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### route -n get 変更前確認 MTU 0217 {#c01-i0666}
*分類: ネットワーク*  ・  難易度: 中級

初霜保守ではAIX 7.3のネットワークで route -n get を確認します。初霜保守のネットワークでは MTU とMTU属性を採取票へ記録します。初霜保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。初霜保守の注意点として EtherChannel構成対象の誤選択 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、初霜保守を保守判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** 「route -n get 変更前確認 MTU 0217」を「vmo -a 変更後確認 pi 0218」と区別して説明するとき、一次資料と整合する組合せはどれですか。

    - A. 保守作業で参照する機能は性能管理でvmo -aを用い・pi とvmstat表示を確認する。
    - B. 保守作業で参照する機能はLVMでmigratepvを用い・LV STATE とボリュームグループ属性を確認する。
    - C. 保守作業で参照する機能は性能管理でnmonを用い・PhysB とvmstat表示を確認する。
    - D. 保守作業で参照する機能はネットワークでroute -n getを用い・MTU とMTU属性を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでroute -n getを用い、MTU とMTU属性を確認する」に対応する項目は変更前確認 MTU（変更・rout）です。変更前に関するネットワークの仕様は「ネットワークでroute -n getを用い、MTU」で、確認対象はro・変更前です。変更後・vmoのA:は「性能管理でvmo -aを用い、pi とvmstat表示を確認する」を述べ、対象は変更後確認 pi（変更・vmo）です。属性・migrのB:は「LVMでmigratepvを用い、LV STATE」を述べ、対象はLV STATE（属性・migr）です。容量・nmonのC:は「性能管理でnmonを用い、PhysB とvmstat表示を確認する」を述べ、対象は容量確認 PhysB（容量・nmon）です。「route -n get」は「ネットワークでroute -n getを用い、MTU」を指し、変更前確認 MTUではro・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **route -n get 変更前確認 MTU 0217**

    - 検証目的: ネットワークのroute -n get 変更前確認 MTU 0217について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更前確認097-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> route -n get
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0217A
    ```

    画面・出力には AIX0217A が表示され、route -n get 変更前確認 MTU 0217 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0217B
    ```

    画面・出力には AIX0217B が表示され、route -n get 変更前確認 MTU 0217 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0217C
    ```

    画面・出力には AIX0217C が表示され、route -n get 変更前確認 MTU 0217 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0217A が画面・出力に表示されること
    ② ステップ2 の AIX0217B が画面・出力に表示されること
    ③ ステップ3 の AIX0217C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### route -n get 容量確認 EtherChannel 0187 {#c01-i0667}
*分類: ネットワーク*  ・  難易度: 中級

風花判定ではAIX 7.3のネットワークで route -n get を確認します。風花判定のネットワークでは EtherChannel とEthernet統計を点検票へ整理します。風花判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。風花判定の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、風花判定を調査記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** route -n get 容量確認 EtherChannel 0187について構成や状態を確認します。usrck -n ALL 性能確認 enhanced_RBAC 0188ではなく対象機能を表す記述はどれですか。

    - A. 対象資源に対する働きはセキュリティでusrck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。
    - B. 対象資源に対する働きはLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。
    - C. 対象資源に対する働きはセキュリティでchuserを用い・authorizations とユーザー属性を確認する。chuser 変更前確認 authorizations 0800固有の属性も確認対象に含める。
    - D. 対象資源に対する働きはネットワークでroute -n getを用い・EtherChannel とEthernet統計を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでroute -n getを用い、EtherChannel」に対応する項目は容量確認 EtherChannel（容量・rout）です。容量に関するネットワークの仕様は「ネットワークでroute -n getを用い」で、確認対象はro・容量です。性能・usrcのA:は「セキュリティでusrck -n ALLを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・usrc）です。バック・migrのB:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（バッ・migr）です。変更前・chusのC:は「セキュリティでchuserを用い、authorizations」を述べ、対象は変更前確認 authorizatio（変更・chus）です。「route -n get」は「ネットワークでroute -n getを用い」を指し、容量確認 EtherChannelではro・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **route -n get 容量確認 EtherChannel 0187**

    - 検証目的: ネットワークのroute -n get 容量確認 EtherChannel 0187について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク容量確認067-02
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> route -n get
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0187A
    ```

    画面・出力には AIX0187A が表示され、route -n get 容量確認 EtherChannel 0187 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0187B
    ```

    画面・出力には AIX0187B が表示され、route -n get 容量確認 EtherChannel 0187 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0187C
    ```

    画面・出力には AIX0187C が表示され、route -n get 容量確認 EtherChannel 0187 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0187A が画面・出力に表示されること
    ② ステップ2 の AIX0187B が画面・出力に表示されること
    ③ ステップ3 の AIX0187C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### route -n get 容量確認 Media Speed Running 0663 {#c01-i0668}
*分類: ネットワーク*  ・  難易度: 中級

新緑判定ではAIX 7.3のネットワークで route -n get を確認します。新緑判定のネットワークでは Media Speed Running とEthernet統計を作業票へ保管します。新緑判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。新緑判定の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、新緑判定を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** route -n get 容量確認 Media Speed Running 0663の設定や表示を読む前に役割を確認します。usrck -n ALL 性能確認 roles 0664ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きはネットワークでroute -n getを用い・Media Speed Runningである。 ✅
    - B. 状態を読み取るための働きはセキュリティでusrck -n ALLを用い・roles とユーザー属性を確認する。
    - C. 状態を読み取るための働きはSRCとログでtail -f /tmp/myfileを用い・PID とinetdデバッグ出力を確認する。
    - D. 状態を読み取るための働きはデバイス管理でbootinfo -B hdisk0を用い・Availableである。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「ネットワークでroute -n getを用い、Media Speed」に対応する項目はSpeed Running（容量・rout）です。容量に関するネットワークの仕様は「ネットワークでroute -n getを用い、Media」で、確認対象はro・容量です。性能・usrcのB:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は性能確認 roles（性能・usrc）です。構成・tailのC:は「SRCとログでtail -f /tmp/myfileを用い、PID」を述べ、対象は構成照合 PID（構成・tail）です。起動・bootのD:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は起動確認 Available（起動・boot）です。「route -n get」は「ネットワークでroute -n getを用い、Media」を指し、Speed Runningではro・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **route -n get 容量確認 Media Speed Running 0663**

    - 検証目的: ネットワークのroute -n get 容量確認 Media Speed Running 0663について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク容量確認063-06
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> route -n get
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0663A
    ```

    画面・出力には AIX0663A が表示され、route -n get 容量確認 Media Speed Running 0663 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0663B
    ```

    画面・出力には AIX0663B が表示され、route -n get 容量確認 Media Speed Running 0663 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0663C
    ```

    画面・出力には AIX0663C が表示され、route -n get 容量確認 Media Speed Running 0663 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0663A が画面・出力に表示されること
    ② ステップ2 の AIX0663B が画面・出力に表示されること
    ③ ステップ3 の AIX0663C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### route -n get 監査記録 EtherChannel 0375 {#c01-i0669}
*分類: ネットワーク*  ・  難易度: 初級

岩清水記録ではAIX 7.3のネットワークで route -n get を確認します。岩清水記録のネットワークでは EtherChannel とEthernet統計を作業票へ保管します。岩清水記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。岩清水記録の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、岩清水記録を照合結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** route -n get 監査記録 EtherChannel 0375の設定や表示を読む前に役割を確認します。vmo -a 運用引継ぎ pi 0376ではなく対象を説明しているものはどれですか。

    - A. 状態を読み取るための働きは性能管理でvmo -aを用い・pi とtopasディスク表示を確認する。
    - B. 状態を読み取るための働きはLVMでmirrorvgを用い・STALE PARTITIONS とミラーコピー状態を確認する。
    - C. 状態を読み取るための働きはセキュリティでpwdck -n ALLを用い・user attributes とユーザー属性を確認する。pwdck -n ALL 容量確認 user attributes固有の属性も確認対象に含める。
    - D. 状態を読み取るための働きはネットワークでroute -n getを用い・EtherChannel とEthernet統計を確認する。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「ネットワークでroute -n getを用い、EtherChannel」に対応する項目は監査記録 EtherChannel（監査・rout）です。監査に関するネットワークの仕様は「ネットワークでroute -n getを用い」で、確認対象はro・監査です。運用引・vmoのA:は「性能管理でvmo -aを用い、pi とtopasディスク表示を確認す」を述べ、対象は運用引継ぎ pi（運用・vmo）です。変更前・mirrのB:は「LVMでmirrorvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（変更・mirr）です。容量・pwdcのC:は「セキュリティでpwdck -n ALLを用い、user」を述べ、対象はuser attributes（容量・pwdc）です。「route -n get」は「ネットワークでroute -n getを用い」を指し、監査記録 EtherChannelではro・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **route -n get 監査記録 EtherChannel 0375**

    - 検証目的: ネットワークのroute -n get 監査記録 EtherChannel 0375について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク監査記録015-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> route -n get
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0375A
    ```

    画面・出力には AIX0375A が表示され、route -n get 監査記録 EtherChannel 0375 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0375B
    ```

    画面・出力には AIX0375B が表示され、route -n get 監査記録 EtherChannel 0375 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0375C
    ```

    画面・出力には AIX0375C が表示され、route -n get 監査記録 EtherChannel 0375 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0375A が画面・出力に表示されること
    ② ステップ2 の AIX0375B が画面・出力に表示されること
    ③ ステップ3 の AIX0375C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### route -n get 起動確認 EtherChannel 0058 {#c01-i0670}
*分類: ネットワーク*  ・  難易度: 中級

潮騒照合ではAIX 7.3のネットワークで route -n get を確認します。潮騒照合のネットワークでは EtherChannel とアダプター一覧を保守票へ記録します。潮騒照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。潮騒照合の注意点として jumbo frame前提の不一致 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、潮騒照合を監査材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** route -n get 起動確認 EtherChannel 0058の役割を調べています。vmo -a 属性確認 po 0059の説明を混ぜずに採るべき記述はどれですか。

    - A. 表示や設定で扱う内容は性能管理でvmo -aを用い・po とsvmon全体表示を確認する。vmo -a 属性確認 po 0059固有の属性も確認対象に含める。
    - B. 表示や設定で扱う内容はネットワークでroute -n getを用い・EtherChannel とアダプター一覧を確認する。 ✅
    - C. 表示や設定で扱う内容はLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。
    - D. 表示や設定で扱う内容は性能管理でnmonを用い・Entitled Capacity とsvmon全体表示を確認する。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「ネットワークでroute -n getを用い、EtherChannel」に対応する項目は起動確認 EtherChannel（起動・rout）です。ネットワークの仕様は「ネットワークでroute -n getを用い、EtherChannel」で、確認対象はro・起動です。属性・vmoのA:は「性能管理でvmo -aを用い、po とsvmon全体表示を確認する」を述べ、対象は属性確認 po（属性・vmo）です。運用引・migrのC:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・migr）です。障害切・nmonのD:は「性能管理でnmonを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（障害・nmon）です。「route -n get」は「ネットワークでroute -n getを用い」を指し、起動確認 EtherChannelではro・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **route -n get 起動確認 EtherChannel 0058**

    - 検証目的: ネットワークのroute -n get 起動確認 EtherChannel 0058について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク起動確認058-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> route -n get
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0058A
    ```

    画面・出力には AIX0058A が表示され、route -n get 起動確認 EtherChannel 0058 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0058B
    ```

    画面・出力には AIX0058B が表示され、route -n get 起動確認 EtherChannel 0058 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0058C
    ```

    画面・出力には AIX0058C が表示され、route -n get 起動確認 EtherChannel 0058 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0058A が画面・出力に表示されること
    ② ステップ2 の AIX0058B が画面・出力に表示されること
    ③ ステップ3 の AIX0058C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### route -n get 起動確認 Media Speed Running 0534 {#c01-i0671}
*分類: ネットワーク*  ・  難易度: 中級

星霜照合ではAIX 7.3のネットワークで route -n get を確認します。星霜照合のネットワークでは Media Speed Running とアダプター一覧を変更票へ記録します。星霜照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。星霜照合の注意点として jumbo frame前提の不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、星霜照合を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** route -n get 起動確認 Media Speed Running 0534に関する障害切り分けの前提を確認しています。vmo -a 属性確認 pi 0535の機能を混同しない選択肢はどれですか。

    - A. 機能の説明としては性能管理でvmo -aを用い・pi とsvmon全体表示を確認する。
    - B. 機能の説明としてはLVMでmirrorvgを用い・PVID と論理ボリューム配置を確認する。
    - C. 機能の説明としてはデバイス管理でbootinfo -B hdisk0を用い・location code とODM属性を確認する。
    - D. 機能の説明としてはネットワークでroute -n getを用い・Media Speed Runningである。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでroute -n getを用い、Media Speed」に対応する項目はSpeed Running（起動・rout）です。起動に関するネットワークの仕様は「ネットワークでroute -n getを用い、Media」で、確認対象はro・起動です。属性・vmoのA:は「性能管理でvmo -aを用い、pi とsvmon全体表示を確認する」を述べ、対象は属性確認 pi（属性・vmo）です。監査・mirrのB:は「LVMでmirrorvgを用い、PVID」を述べ、対象は監査記録 PVID（監査・mirr）です。状態・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象はlocation code（状態・boot）です。「route -n get」は「ネットワークでroute -n getを用い、Media」を指し、Speed Runningではro・起動に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **route -n get 起動確認 Media Speed Running 0534**

    - 検証目的: ネットワークのroute -n get 起動確認 Media Speed Running 0534について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク起動確認054-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> route -n get
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0534A
    ```

    画面・出力には AIX0534A が表示され、route -n get 起動確認 Media Speed Running 0534 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0534B
    ```

    画面・出力には AIX0534B が表示され、route -n get 起動確認 Media Speed Running 0534 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0534C
    ```

    画面・出力には AIX0534C が表示され、route -n get 起動確認 Media Speed Running 0534 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0534A が画面・出力に表示されること
    ② ステップ2 の AIX0534B が画面・出力に表示されること
    ③ ステップ3 の AIX0534C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### route -n get 障害切り分け Gateway 0504 {#c01-i0672}
*分類: ネットワーク*  ・  難易度: 中級

霜月確認ではAIX 7.3のネットワークで route -n get を確認します。霜月確認のネットワークでは Gateway と経路表を同じ証跡に残します。霜月確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。霜月確認の注意点として MTU不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、霜月確認を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** route -n get 障害切り分け Gateway 0504を同一分類のvmo -a バックアウト確認 dxm 0505と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は性能管理でvmo -aを用い・dxm とAME統計を確認する。
    - B. 構成を確認する際の意味はLVMでmirrorvgを用い・PP SIZE と物理ボリューム一覧を確認する。
    - C. 構成を確認する際の意味はデバイス管理でbootinfo -B hdisk0を用い・path status と診断対象表示を確認する。
    - D. 構成を確認する際の意味はネットワークでroute -n getを用い・Gateway と経路表を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでroute -n getを用い、Gateway と経路表を確認する」に対応する項目は障害切り分け Gateway（障害・rout）です。障害切に関するネットワークの仕様は「ネットワークでroute -n getを用い、Gateway」で、確認対象はro・障害切です。バック・vmoのA:は「性能管理でvmo -aを用い、dxm とAME統計を確認する」を述べ、対象はバックアウト確認 dxm（バッ・vmo）です。状態・mirrのB:は「LVMでmirrorvgを用い、PP SIZE」を述べ、対象はPP SIZE（状態・mirr）です。監査・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い、path」を述べ、対象はpath status（監査・boot）です。「route -n get」は「ネットワークでroute -n getを用い、Gateway」を指し、障害切り分け Gatewayではro・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **route -n get 障害切り分け Gateway 0504**

    - 検証目的: ネットワークのroute -n get 障害切り分け Gateway 0504について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク障害切り分け024-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> route -n get
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0504A
    ```

    画面・出力には AIX0504A が表示され、route -n get 障害切り分け Gateway 0504 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0504B
    ```

    画面・出力には AIX0504B が表示され、route -n get 障害切り分け Gateway 0504 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0504C
    ```

    画面・出力には AIX0504C が表示され、route -n get 障害切り分け Gateway 0504 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0504A が画面・出力に表示されること
    ② ステップ2 の AIX0504B が画面・出力に表示されること
    ③ ステップ3 の AIX0504C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### route -n get 障害切り分け Gateway 0564 {#c01-i0673}
*分類: ネットワーク*  ・  難易度: 中級

若草点検ではAIX 7.3のネットワークで route -n get を確認します。若草点検のネットワークでは Gateway と経路表を同じ証跡に残します。若草点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若草点検の注意点として MTU不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、若草点検を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** route -n get 障害切り分け Gateway 0564の技術的な意味を資料で確認するとき、vmo -a バックアウト確認 Entitled Capacity 0565との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は性能管理でvmo -aを用い・Entitled Capacity とAME統計を確認する。
    - B. 構成を確認する際の意味はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。
    - C. 構成を確認する際の意味はデバイス管理でlsmpio -l hdisk0を用い・microcode levelである。
    - D. 構成を確認する際の意味はネットワークでroute -n getを用い・Gateway と経路表を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでroute -n getを用い、Gateway と経路表を確認する」に対応する項目は障害切り分け Gateway（障害・rout）です。障害切に関するネットワークの仕様は「ネットワークでroute -n getを用い、Gateway」で、確認対象はro・障害切です。バック・vmoのA:は「性能管理でvmo -aを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（バッ・vmo）です。復旧前・lparのB:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は復旧前確認 キュー状態（復旧・lpar）です。運用引・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はmicrocode level（運用・lsmp）です。「route -n get」は「ネットワークでroute -n getを用い、Gateway」を指し、障害切り分け Gatewayではro・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **route -n get 障害切り分け Gateway 0564**

    - 検証目的: ネットワークのroute -n get 障害切り分け Gateway 0564について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク障害切り分け084-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> route -n get
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0564A
    ```

    画面・出力には AIX0564A が表示され、route -n get 障害切り分け Gateway 0564 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0564B
    ```

    画面・出力には AIX0564B が表示され、route -n get 障害切り分け Gateway 0564 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0564C
    ```

    画面・出力には AIX0564C が表示され、route -n get 障害切り分け Gateway 0564 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0564A が画面・出力に表示されること
    ② ステップ2 の AIX0564B が画面・出力に表示されること
    ③ ステップ3 の AIX0564C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### route -n get 障害切り分け MTU 0028 {#c01-i0674}
*分類: ネットワーク*  ・  難易度: 中級

雪解確認ではAIX 7.3のネットワークで route -n get を確認します。雪解確認のネットワークでは MTU と経路表を監査票へ転記します。雪解確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。雪解確認の注意点として MTU不一致 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、雪解確認を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** route -n get 障害切り分け MTU 0028の技術的な意味を資料で確認するとき、vmo -a バックアウト確認 Busy% 0029との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はネットワークでroute -n getを用い・MTU と経路表を確認する。 ✅
    - B. 管理対象との関係を表す説明は性能管理でvmo -aを用い・Busy% とAME統計を確認する。
    - C. 管理対象との関係を表す説明はLVMでmirrorvgを用い・VG STATE と物理ボリューム一覧を確認する。
    - D. 管理対象との関係を表す説明は性能管理でnmonを用い・pi とAME統計を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「ネットワークでroute -n getを用い、MTU と経路表を確認する」に対応する項目は障害切り分け MTU（障害・rout）です。ネットワークの仕様は「ネットワークでroute -n getを用い、MTU と経路表を確認する」で、確認対象はro・障害切です。バック・vmoのB:は「性能管理でvmo -aを用い、Busy% とAME統計を確認する」を述べ、対象はバックアウト確認 Busy%（バッ・vmo）です。状態・mirrのC:は「LVMでmirrorvgを用い、VG STATE」を述べ、対象はVG STATE（状態・mirr）です。起動・nmonのD:は「性能管理でnmonを用い、pi とAME統計を確認する」を述べ、対象は起動確認 pi（起動・nmon）です。「route -n get」は「ネットワークでroute -n getを用い、MTU」を指し、障害切り分け MTUではro・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **route -n get 障害切り分け MTU 0028**

    - 検証目的: ネットワークのroute -n get 障害切り分け MTU 0028について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク障害切り分け028-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> route -n get
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0028A
    ```

    画面・出力には AIX0028A が表示され、route -n get 障害切り分け MTU 0028 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0028B
    ```

    画面・出力には AIX0028B が表示され、route -n get 障害切り分け MTU 0028 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0028C
    ```

    画面・出力には AIX0028C が表示され、route -n get 障害切り分け MTU 0028 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0028A が画面・出力に表示されること
    ② ステップ2 の AIX0028B が画面・出力に表示されること
    ③ ステップ3 の AIX0028C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### route -n get 障害切り分け MTU 0088 {#c01-i0675}
*分類: ネットワーク*  ・  難易度: 中級

翠風点検ではAIX 7.3のネットワークで route -n get を確認します。翠風点検のネットワークでは MTU と経路表を監査票へ転記します。翠風点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。翠風点検の注意点として MTU不一致 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、翠風点検を採取結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** route -n get 障害切り分け MTU 0088を同一分類のvmo -a バックアウト確認 avm 0089と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 管理対象との関係を表す説明はネットワークでroute -n getを用い・MTU と経路表を確認する。 ✅
    - B. 管理対象との関係を表す説明は性能管理でvmo -aを用い・avm とAME統計を確認する。
    - C. 管理対象との関係を表す説明はLVMでmigratepvを用い・LV STATE と物理ボリューム一覧を確認する。
    - D. 管理対象との関係を表す説明は性能管理でnmonを用い・dxm とAME統計を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「ネットワークでroute -n getを用い、MTU と経路表を確認する」に対応する項目は障害切り分け MTU（障害・rout）です。障害切に関するネットワークの仕様は「ネットワークでroute -n getを用い、MTU」で、確認対象はro・障害切です。バック・vmoのB:は「性能管理でvmo -aを用い、avm とAME統計を確認する」を述べ、対象はバックアウト確認 avm（バッ・vmo）です。構成・migrのC:は「LVMでmigratepvを用い、LV STATE」を述べ、対象はLV STATE（構成・migr）です。起動・nmonのD:は「性能管理でnmonを用い、dxm とAME統計を確認する」を述べ、対象は起動確認 dxm（起動・nmon）です。「route -n get」は「ネットワークでroute -n getを用い、MTU」を指し、障害切り分け MTUではro・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **route -n get 障害切り分け MTU 0088**

    - 検証目的: ネットワークのroute -n get 障害切り分け MTU 0088について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク障害切り分け088-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> route -n get
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0088A
    ```

    画面・出力には AIX0088A が表示され、route -n get 障害切り分け MTU 0088 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0088B
    ```

    画面・出力には AIX0088B が表示され、route -n get 障害切り分け MTU 0088 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0088C
    ```

    画面・出力には AIX0088C が表示され、route -n get 障害切り分け MTU 0088 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0088A が画面・出力に表示されること
    ② ステップ2 の AIX0088B が画面・出力に表示されること
    ③ ステップ3 の AIX0088C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### smitty etherchannel 変更前確認 Destination 0383 {#c01-i0676}
*分類: ネットワーク*  ・  難易度: 中級

新緑記録ではAIX 7.3のネットワークで smitty etherchannel を確認します。新緑記録のネットワークでは Destination とEthernet統計を照合票へ整理します。新緑記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。新緑記録の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、新緑記録を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** smitty etherchannel 変更前確認 Destination 0383の設定や表示を読む前に役割を確認します。filemon 変更後確認 Busy% 0384ではなく対象を説明しているものはどれですか。

    - A. 一次資料が示す主目的はネットワークでsmitty etherchannelを用い・Destinationである。 ✅
    - B. 一次資料が示す主目的は性能管理でfilemonを用い・Busy% とtopasディスク表示を確認する。
    - C. 一次資料が示す主目的はLVMでmklvを用い・LV STATE とミラーコピー状態を確認する。
    - D. 一次資料が示す主目的はデバイス管理でdiag -d ent0を用い・attribute と構成マネージャー結果を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「ネットワークでsmitty etherchannelを用い」に対応する項目は変更前確認 Destination（変更・smit）です。変更前に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・変更前です。変更後・fileのB:は「性能管理でfilemonを用い、Busy%」を述べ、対象は変更後確認 Busy%（変更・file）です。起動・mklvのC:は「LVMでmklvを用い、LV STATE」を述べ、対象はLV STATE（起動・mklv）です。障害切・diagのD:は「デバイス管理でdiag -d ent0を用い、attribute」を述べ、対象は障害切り分け attribute（障害・diag）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、変更前確認 Destinationではsm・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **smitty etherchannel 変更前確認 Destination 0383**

    - 検証目的: ネットワークのsmitty etherchannel 変更前確認 Destination 0383について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更前確認023-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> smitty etherchannel
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0383A
    ```

    画面・出力には AIX0383A が表示され、smitty etherchannel 変更前確認 Destination 0383 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0383B
    ```

    画面・出力には AIX0383B が表示され、smitty etherchannel 変更前確認 Destination 0383 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0383C
    ```

    画面・出力には AIX0383C が表示され、smitty etherchannel 変更前確認 Destination 0383 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0383A が画面・出力に表示されること
    ② ステップ2 の AIX0383B が画面・出力に表示されること
    ③ ステップ3 の AIX0383C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### smitty etherchannel 変更前確認 Destination 0443 {#c01-i0677}
*分類: ネットワーク*  ・  難易度: 中級

秋声整理ではAIX 7.3のネットワークで smitty etherchannel を確認します。秋声整理のネットワークでは Destination とEthernet統計を照合票へ整理します。秋声整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。秋声整理の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、秋声整理を復旧材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** smitty etherchannel 変更前確認 Destination 0443について構成や状態を確認します。filemon 変更後確認 avm 0444ではなく対象機能を表す記述はどれですか。

    - A. 一次資料が示す主目的はネットワークでsmitty etherchannelを用い・Destinationである。 ✅
    - B. 一次資料が示す主目的は性能管理でfilemonを用い・avm とtopasディスク表示を確認する。
    - C. 一次資料が示す主目的はLVMでchlvを用い・PP SIZE とミラーコピー状態を確認する。
    - D. 一次資料が示す主目的はセキュリティでlsuserを用い・user attributes とユーザー属性を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「ネットワークでsmitty etherchannelを用い」に対応する項目は変更前確認 Destination（変更・smit）です。変更前に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・変更前です。変更後・fileのB:は「性能管理でfilemonを用い、avm とtopasディスク表示を確」を述べ、対象は変更後確認 avm（変更・file）です。属性・chlvのC:は「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（属性・chlv）です。バック・lsusのD:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（バッ・lsus）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、変更前確認 Destinationではsm・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **smitty etherchannel 変更前確認 Destination 0443**

    - 検証目的: ネットワークのsmitty etherchannel 変更前確認 Destination 0443について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更前確認083-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> smitty etherchannel
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0443A
    ```

    画面・出力には AIX0443A が表示され、smitty etherchannel 変更前確認 Destination 0443 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0443B
    ```

    画面・出力には AIX0443B が表示され、smitty etherchannel 変更前確認 Destination 0443 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0443C
    ```

    画面・出力には AIX0443C が表示され、smitty etherchannel 変更前確認 Destination 0443 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0443A が画面・出力に表示されること
    ② ステップ2 の AIX0443B が画面・出力に表示されること
    ③ ステップ3 の AIX0443C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### smitty etherchannel 容量確認 Link Status 0413 {#c01-i0678}
*分類: ネットワーク*  ・  難易度: 中級

月影評価ではAIX 7.3のネットワークで smitty etherchannel を確認します。月影評価のネットワークでは Link Status とMTU属性を復旧票へ残します。月影評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。月影評価の注意点として EtherChannel構成対象の誤選択 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、月影評価を判定結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** smitty etherchannel 容量確認 Link Status 0413を保守記録に説明する必要があります。filemon 性能確認 po 0414と取り違えない説明はどれですか。

    - A. 仕様上の役割は性能管理でfilemonを用い・po とvmstat表示を確認する。
    - B. 仕様上の役割はLVMでmklvを用い・MIRROR WRITE CONSISTENCY とボリュームグループ属性を確認する。
    - C. 仕様上の役割はデバイス管理でdiag -d ent0を用い・microcode level とデバイス一覧を確認する。
    - D. 仕様上の役割はネットワークでsmitty etherchannelを用い・Link Status とMTU属性を確認する。 ✅

    正解: **D** ／ 難易度: 中級

    **解説:** Dの記述「ネットワークでsmitty etherchannelを用い、Link Status」に対応する項目はLink Status（容量・smit）です。容量に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・容量です。性能・fileのA:は「性能管理でfilemonを用い、po とvmstat表示を確認する」を述べ、対象は性能確認 po（性能・file）です。障害切・mklvのB:は「LVMでmklvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（障害・mklv）です。起動・diagのC:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（起動・diag）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、Link Statusではsm・容量に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **smitty etherchannel 容量確認 Link Status 0413**

    - 検証目的: ネットワークのsmitty etherchannel 容量確認 Link Status 0413について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク容量確認053-04
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> smitty etherchannel
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0413A
    ```

    画面・出力には AIX0413A が表示され、smitty etherchannel 容量確認 Link Status 0413 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0413B
    ```

    画面・出力には AIX0413B が表示され、smitty etherchannel 容量確認 Link Status 0413 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0413C
    ```

    画面・出力には AIX0413C が表示され、smitty etherchannel 容量確認 Link Status 0413 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0413A が画面・出力に表示されること
    ② ステップ2 の AIX0413B が画面・出力に表示されること
    ③ ステップ3 の AIX0413C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### smitty etherchannel 状態確認 Link Status 0096 {#c01-i0679}
*分類: ネットワーク*  ・  難易度: 中級

若竹点検ではAIX 7.3のネットワークで smitty etherchannel を確認します。若竹点検のネットワークでは Link Status と経路表を同じ証跡に残します。若竹点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若竹点検の注意点として MTU不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、若竹点検を変更判断にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** smitty etherchannel 状態確認 Link Status 0096を同一分類のfilemon 構成照合 csz 0097と比較します。対象固有の機能として妥当な記述はどれですか。

    - A. 構成を確認する際の意味は性能管理でfilemonを用い・csz とAME統計を確認する。
    - B. 構成を確認する際の意味はLVMでchlvを用い・PVID と物理ボリューム一覧を確認する。chlv 性能確認 PVID 0402固有の属性も確認対象に含める。
    - C. 構成を確認する際の意味はネットワークでsmitty etherchannelを用い・Link Status と経路表を確認する。 ✅
    - D. 構成を確認する際の意味は性能管理でtopas -Dを用い・avm とAME統計を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「ネットワークでsmitty etherchannelを用い、Link Status」に対応する項目はLink Status（状態・smit）です。状態に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・状態です。構成・fileのA:は「性能管理でfilemonを用い、csz とAME統計を確認する」を述べ、対象は構成照合 csz（構成・file）です。性能・chlvのB:は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は性能確認 PVID（性能・chlv）です。監査・topaのD:は「性能管理でtopas -Dを用い、avm とAME統計を確認する」を述べ、対象は監査記録 avm（監査・topa）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、Link Statusではsm・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **smitty etherchannel 状態確認 Link Status 0096**

    - 検証目的: ネットワークのsmitty etherchannel 状態確認 Link Status 0096について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク状態確認096-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> smitty etherchannel
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0096A
    ```

    画面・出力には AIX0096A が表示され、smitty etherchannel 状態確認 Link Status 0096 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0096B
    ```

    画面・出力には AIX0096B が表示され、smitty etherchannel 状態確認 Link Status 0096 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0096C
    ```

    画面・出力には AIX0096C が表示され、smitty etherchannel 状態確認 Link Status 0096 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0096A が画面・出力に表示されること
    ② ステップ2 の AIX0096B が画面・出力に表示されること
    ③ ステップ3 の AIX0096C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### smitty etherchannel 状態確認 MTU 0572 {#c01-i0680}
*分類: ネットワーク*  ・  難易度: 中級

水音点検ではAIX 7.3のネットワークで smitty etherchannel を確認します。水音点検のネットワークでは MTU と経路表を引継ぎ票へ保管します。水音点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。水音点検の注意点として MTU不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、水音点検を再確認材料にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** smitty etherchannel 状態確認 MTU 0572の技術的な意味を資料で確認するとき、filemon 構成照合 po 0573との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は性能管理でfilemonを用い・po とAME統計を確認する。
    - B. コマンドまたは機能の用途は構成済みデバイスと VPD を表示するコマンドである。
    - C. コマンドまたは機能の用途はネットワークでsmitty etherchannelを用い・MTU と経路表を確認する。 ✅
    - D. コマンドまたは機能の用途はデバイス管理でrmdev -Rl ent1を用い・PVID と診断対象表示を確認する。rmdev -Rl ent1 変更後確認 PVID 0265固有の属性も確認対象に含める。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「ネットワークでsmitty etherchannelを用い、MTU」に対応する項目は状態確認 MTU（状態・smit）です。状態に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い、MTU」で、確認対象はsm・状態です。構成・fileのA:は「性能管理でfilemonを用い、po とAME統計を確認する」を述べ、対象は構成照合 po（構成・file）です。一覧・表示・lscfのB:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は一覧確認 LPAR表示（一覧・lscf）です。変更後・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い、PVID」を述べ、対象は変更後確認 PVID（変更・rmde）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い、MTU」を指し、状態確認 MTUではsm・状態に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **smitty etherchannel 状態確認 MTU 0572**

    - 検証目的: ネットワークのsmitty etherchannel 状態確認 MTU 0572について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク状態確認092-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> smitty etherchannel
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0572A
    ```

    画面・出力には AIX0572A が表示され、smitty etherchannel 状態確認 MTU 0572 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0572B
    ```

    画面・出力には AIX0572B が表示され、smitty etherchannel 状態確認 MTU 0572 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0572C
    ```

    画面・出力には AIX0572C が表示され、smitty etherchannel 状態確認 MTU 0572 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0572A が画面・出力に表示されること
    ② ステップ2 の AIX0572B が画面・出力に表示されること
    ③ ステップ3 の AIX0572C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### smitty etherchannel 監査記録 Destination 0066 {#c01-i0681}
*分類: ネットワーク*  ・  難易度: 中級

陽炎照合ではAIX 7.3のネットワークで smitty etherchannel を確認します。陽炎照合のネットワークでは Destination とアダプター一覧を変更票へ記録します。陽炎照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。陽炎照合の注意点として jumbo frame前提の不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、陽炎照合を運用記録にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** smitty etherchannel 監査記録 Destination 0066の役割を調べています。filemon 運用引継ぎ PhysB 0067の説明を混ぜずに採るべき記述はどれですか。

    - A. 機能の説明としては性能管理でfilemonを用い・PhysB とsvmon全体表示を確認する。
    - B. 機能の説明としてはネットワークでsmitty etherchannelを用い・Destinationである。 ✅
    - C. 機能の説明としてはLVMでchlvを用い・PP SIZE と論理ボリューム配置を確認する。
    - D. 機能の説明としては性能管理でtopas -Dを用い・po とsvmon全体表示を確認する。topas -D 状態確認 po 0679固有の属性も確認対象に含める。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「ネットワークでsmitty etherchannelを用い」に対応する項目は監査記録 Destination（監査・smit）です。ネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・監査です。運用引・fileのA:は「性能管理でfilemonを用い、PhysB」を述べ、対象は運用引継ぎ PhysB（運用・file）です。変更後・chlvのC:は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」を述べ、対象はPP SIZE（変更・chlv）です。状態・topaのD:は「性能管理でtopas -Dを用い、po とsvmon全体表示を確認す」を述べ、対象は状態確認 po（状態・topa）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、監査記録 Destinationではsm・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **smitty etherchannel 監査記録 Destination 0066**

    - 検証目的: ネットワークのsmitty etherchannel 監査記録 Destination 0066について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク監査記録066-01
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> smitty etherchannel
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0066A
    ```

    画面・出力には AIX0066A が表示され、smitty etherchannel 監査記録 Destination 0066 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0066B
    ```

    画面・出力には AIX0066B が表示され、smitty etherchannel 監査記録 Destination 0066 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> ifconfig en0
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0066C
    ```

    画面・出力には AIX0066C が表示され、smitty etherchannel 監査記録 Destination 0066 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0066A が画面・出力に表示されること
    ② ステップ2 の AIX0066B が画面・出力に表示されること
    ③ ステップ3 の AIX0066C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en



### smitty etherchannel 監査記録 EtherChannel 0542 {#c01-i0682}
*分類: ネットワーク*  ・  難易度: 中級

紅葉照合ではAIX 7.3のネットワークで smitty etherchannel を確認します。紅葉照合のネットワークでは EtherChannel とアダプター一覧を確認票へ整理します。紅葉照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。紅葉照合の注意点として jumbo frame前提の不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、紅葉照合を点検結果にします。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en

??? question "確認問題（1問）"
    **問題.** smitty etherchannel 監査記録 EtherChannel 0542に関する障害切り分けの前提を確認しています。filemon 運用引継ぎ Busy% 0543の機能を混同しない選択肢はどれですか。

    - A. 障害切り分けに用いる役割は性能管理でfilemonを用い・Busy% とsvmon全体表示を確認する。
    - B. 障害切り分けに用いる役割は構成済みデバイスと VPD を表示するコマンドである。
    - C. 障害切り分けに用いる役割はネットワークでsmitty etherchannelを用い・EtherChannelである。 ✅
    - D. 障害切り分けに用いる役割はデバイス管理でdiag -d ent0を用い・microcode level とODM属性を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「ネットワークでsmitty etherchannelを用い」に対応する項目は監査記録 EtherChannel（監査・smit）です。監査に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・監査です。運用引・fileのA:は「性能管理でfilemonを用い、Busy%」を述べ、対象は運用引継ぎ Busy%（運用・file）です。復旧前・lscfのB:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は復旧前確認 障害記録（復旧・lscf）です。容量・diagのD:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（容量・diag）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、監査記録 EtherChannelではsm・監査に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en


??? note "検証手順（1件）"
    **smitty etherchannel 監査記録 EtherChannel 0542**

    - 検証目的: ネットワークのsmitty etherchannel 監査記録 EtherChannel 0542について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。
    - 前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク監査記録062-05
    - セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。

    **ステップ 1**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> smitty etherchannel
    → Enter を押す
    ```

    画面・出力:
    ```text
    ent0 Available 00-00 PCIe3 10GbE SR Adapter
    en0  Available 00-00 Standard Ethernet Network Interface
    確認コード AIX0542A
    ```

    画面・出力には AIX0542A が表示され、smitty etherchannel 監査記録 EtherChannel 0542 の入力欄確認を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> entstat -d ent0
    → Enter を押す
    ```

    画面・出力:
    ```text
    10/100/1000 Base-TX Adapter Specific Statistics:
    Link Status: Up
    Media Speed Running: 1000 Mbps Full Duplex
    確認コード AIX0542B
    ```

    画面・出力には AIX0542B が表示され、smitty etherchannel 監査記録 EtherChannel 0542 の証跡表示確認を確認できます。

    **ステップ 3**
    現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
    操作（入力）:
    ```text
    AIX 7.3 シェル
    COMMAND ===> netstat -rn
    → Enter を押す
    ```

    画面・出力:
    ```text
    Routing tables
    Destination        Gateway           Flags   Refs     Use  If
    default            192.0.2.1         UG        4      241  en0
    確認コード AIX0542C
    ```

    画面・出力には AIX0542C が表示され、smitty etherchannel 監査記録 EtherChannel 0542 の判定材料確認を確認できます。

    - 合格条件: ① ステップ1 の AIX0542A が画面・出力に表示されること
    ② ステップ2 の AIX0542B が画面・出力に表示されること
    ③ ステップ3 の AIX0542C が画面・出力に表示されること
    - 検証状態: 机上
    - 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en




## AIX 7.3 > ページング

### lparstat 一覧確認 保存場所 {#c01-i0683}
*分類: ページング*  ・  難易度: 中級

AIX 7.3 の ページング で扱う「lparstat 一覧確認 保存場所」は、LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドを一覧確認の観点で確認する技術項目です。Paging Space 表とsys0 060を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lparstat 一覧確認 保存場所の技術的な意味を資料で確認するとき、lspv 状態判定 照合単位との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。lspv 状態判定 照合単位固有の属性も確認対象に含める。
    - B. 管理対象との関係を表す説明は性能管理でlparstat -iを用い・fre とvmstat表示を確認する。
    - C. 管理対象との関係を表す説明はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。 ✅
    - D. 管理対象との関係を表す説明はSRCとログでerrclearを用い・PID とinetdデバッグ出力を確認する。

    正解: **C** ／ 難易度: 中級

    **解説:** Cの記述「LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドである」に対応する項目は一覧確認 保存場所（一覧・lpar）です。ページングの仕様は「LPAR の CPU 使用率、物理CPU消費、AME」で、確認対象はlp・一覧・保存です。状態・照合・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は状態判定 照合単位（状態・lspv）です。状態・lparのB:は「性能管理でlparstat -iを用い、fre」を述べ、対象は状態確認 fre（状態・lpar）です。性能・errcのD:は「SRCとログでerrclearを用い、PID」を述べ、対象は性能確認 PID（性能・errc）です。「lparstat」は「LPAR の CPU 使用率、物理CPU消費、AME」を指し、一覧確認 保存場所ではlp・一覧・保存に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lparstat 一覧確認 保存場所**

    - 検証目的: ページングのlparstat 一覧確認 保存場所について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、ページングの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
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

    画面・出力には System が含まれ、lparstat 一覧確認 保存場所の証跡を確認できます。

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



### lparstat 障害切り分け 受信先 {#c01-i0684}
*分類: ページング*  ・  難易度: 中級

AIX 7.3 の ページング で扱う「lparstat 障害切り分け 受信先」は、LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドを障害切り分けの観点で確認する技術項目です。Paging Space 表とsys0 020を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lparstat 障害切り分け 受信先の技術的な意味を資料で確認するとき、lspv 変更前確認 保持設定との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。
    - B. 構成を確認する際の意味はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。 ✅
    - C. 構成を確認する際の意味は導入と起動でbootlist -m normalを用い・mksysb image とOSレベル表示を確認する。
    - D. 構成を確認する際の意味はLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。

    正解: **B** ／ 難易度: 中級

    **解説:** Bの記述「LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドである」に対応する項目は障害切り分け 受信先（障害・lpar）です。ページングの仕様は「LPAR の CPU 使用率、物理CPU消費、AME」で、確認対象はlp・障害切です。変更前・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は変更前確認 保持設定（変更・lspv）です。容量・bootのC:は「導入と起動でbootlist -m normalを用い」を述べ、対象はmksysb image（容量・boot）です。バック・migrのD:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（バッ・migr）です。「lparstat」は「LPAR の CPU 使用率、物理CPU消費、AME」を指し、障害切り分け 受信先ではlp・障害切に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lparstat 障害切り分け 受信先**

    - 検証目的: ページングのlparstat 障害切り分け 受信先について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、ページングの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
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

    画面・出力には System が含まれ、lparstat 障害切り分け 受信先の証跡を確認できます。

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



### lsattr 変更前確認 パス状態 {#c01-i0685}
*分類: ページング*  ・  難易度: 中級

AIX 7.3 の ページング で扱う「lsattr 変更前確認 パス状態」は、デバイスや sys0 などの属性値を表示するコマンドを変更前確認の観点で確認する技術項目です。Paging Space 表とsys0 036を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsattr 変更前確認 パス状態の技術的な意味を資料で確認するとき、chdev 復旧前確認 仮想化表示との境界を正しく示す記述はどれですか。

    - A. 管理対象との関係を表す説明はデバイスや sys0 などの属性値を表示するコマンドである。 ✅
    - B. 管理対象との関係を表す説明はデバイス属性を変更する管理コマンドである。
    - C. 管理対象との関係を表す説明はネットワークでnetstat -rnを用い・Media Speed Runningである。
    - D. 管理対象との関係を表す説明はJFS2でmount -o remountを用い・agblksize とマウントオプションを確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「デバイスや sys0 などの属性値を表示するコマンドである」に対応する項目は変更前確認 パス状態（変更・lsat）です。ページングの仕様は「デバイスや sys0 などの属性値を表示するコマンド」で、確認対象はls・変更前です。復旧前・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は復旧前確認 仮想化表示（復旧・chde）です。状態・netsのC:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（状態・nets）です。性能・mounのD:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 agblksize（性能・moun）です。「lsattr」は「デバイスや sys0 などの属性値を表示するコマンド」を指し、変更前確認 パス状態ではls・変更前に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsattr 変更前確認 パス状態**

    - 検証目的: ページングのlsattr 変更前確認 パス状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、ページングの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lspv
    → Enter を押す
    ```

    画面・出力:
    ```text
    hdisk0          00f6a1b2c3d4e36        rootvg          active
    hdisk1          00f6a1b2c3d5e36        datavg          active
    ```

    画面・出力には hdisk0 が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
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

    画面・出力には VOLUME が含まれ、lsattr 変更前確認 パス状態の証跡を確認できます。

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



### lsattr 状態判定 ディスク状態 {#c01-i0686}
*分類: ページング*  ・  難易度: 上級

AIX 7.3 の ページング で扱う「lsattr 状態判定 ディスク状態」は、デバイスや sys0 などの属性値を表示するコマンドを状態判定の観点で確認する技術項目です。Paging Space 表とsys0 076を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsattr 状態判定 ディスク状態の技術的な意味を資料で確認するとき、chdev 属性照合 ボリューム状態との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はデバイスや sys0 などの属性値を表示するコマンドである。 ✅
    - B. コマンドまたは機能の用途はデバイス属性を変更する管理コマンドである。
    - C. コマンドまたは機能の用途はセキュリティでlssecattr -cを用い・audit class とRBAC属性を確認する。
    - D. コマンドまたは機能の用途は導入と起動でalt_disk_copyを用い・altinst_rootvg と起動デバイス設定を確認する。

    正解: **A** ／ 難易度: 上級

    **解説:** Aの記述「デバイスや sys0 などの属性値を表示するコマンドである」に対応する項目は状態判定 ディスク状態（状態・lsat）です。ページングの仕様は「デバイスや sys0 などの属性値を表示するコマンド」で、確認対象はls・状態・ディです。属性・ボリ・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は属性照合 ボリューム状態（属性・chde）です。障害切・lsseのC:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（障害・lsse）です。変更前・alt_のD:は「導入と起動でalt_disk_copyを用い」を述べ、対象は変更前確認 altinst_root（変更・alt_）です。「lsattr」は「デバイスや sys0 などの属性値を表示するコマンド」を指し、状態判定 ディスク状態ではls・状態・ディに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsattr 状態判定 ディスク状態**

    - 検証目的: ページングのlsattr 状態判定 ディスク状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、ページングの対象へ進みます。
    操作（入力）:
    ```text
    AIX 7.3 操作画面
    COMMAND ===> lspv
    → Enter を押す
    ```

    画面・出力:
    ```text
    hdisk0          00f6a1b2c3d4e76        rootvg          active
    hdisk1          00f6a1b2c3d5e76        datavg          active
    ```

    画面・出力には hdisk0 が表示され、最初の到達点を確認できます。

    **ステップ 2**
    現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
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

    画面・出力には VOLUME が含まれ、lsattr 状態判定 ディスク状態の証跡を確認できます。

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



### lscfg 性能確認 ページング状態 {#c01-i0687}
*分類: ページング*  ・  難易度: 中級

AIX 7.3 の ページング で扱う「lscfg 性能確認 ページング状態」は、構成済みデバイスと VPD を表示するコマンドを性能確認の観点で確認する技術項目です。Paging Space 表とsys0 028を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lscfg 性能確認 ページング状態の技術的な意味を資料で確認するとき、vmstat 変更前確認 性能値との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途は構成済みデバイスと VPD を表示するコマンドである。 ✅
    - B. コマンドまたは機能の用途はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。
    - C. コマンドまたは機能の用途は導入と起動でmksysbを用い・bootlist とOSレベル表示を確認する。
    - D. コマンドまたは機能の用途はLVMでchlvを用い・PP SIZE とミラーコピー状態を確認する。

    正解: **A** ／ 難易度: 中級

    **解説:** Aの記述「構成済みデバイスと VPD を表示するコマンドである」に対応する項目は性能確認 ページング状態（性能・lscf）です。ページングの仕様は「構成済みデバイスと VPD を表示するコマンド」で、確認対象はls・性能・ペーです。変更前・vmstのB:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は変更前確認 性能値（変更・vmst）です。障害切・mksyのC:は「導入と起動でmksysbを用い、bootlist」を述べ、対象は障害切り分け bootlist（障害・mksy）です。構成・chlvのD:は「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（構成・chlv）です。「lscfg」は「構成済みデバイスと VPD を表示するコマンド」を指し、性能確認 ページング状態ではls・性能・ペーに対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lscfg 性能確認 ページング状態**

    - 検証目的: ページングのlscfg 性能確認 ページング状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、ページングの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
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

    画面・出力には LABEL が含まれ、lscfg 性能確認 ページング状態の証跡を確認できます。

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



### lscfg 詳細確認 除外条件 {#c01-i0688}
*分類: ページング*  ・  難易度: 上級

AIX 7.3 の ページング で扱う「lscfg 詳細確認 除外条件」は、構成済みデバイスと VPD を表示するコマンドを詳細確認の観点で確認する技術項目です。Paging Space 表とsys0 068を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lscfg 詳細確認 除外条件の技術的な意味を資料で確認するとき、vmstat 状態判定 イベント転送との境界を正しく示す記述はどれですか。

    - A. 構成を確認する際の意味はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。
    - B. 構成を確認する際の意味は構成済みデバイスと VPD を表示するコマンドである。 ✅
    - C. 構成を確認する際の意味はセキュリティでchuserを用い・user attributes とRBAC属性を確認する。
    - D. 構成を確認する際の意味は導入と起動でmksysbを用い・Technology Level と起動デバイス設定を確認する。

    正解: **B** ／ 難易度: 上級

    **解説:** Bの記述「構成済みデバイスと VPD を表示するコマンドである」に対応する項目は詳細確認 除外条件（詳細・lscf）です。ページングの仕様は「構成済みデバイスと VPD を表示するコマンド」で、確認対象はls・詳細・除外です。状態・イベ・vmstのA:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は状態判定 イベント転送（状態・vmst）です。容量・chusのC:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（容量・chus）です。監査・mksyのD:は「導入と起動でmksysbを用い、Technology Level」を述べ、対象はTechnology Level（監査・mksy）です。「lscfg」は「構成済みデバイスと VPD を表示するコマンド」を指し、詳細確認 除外条件ではls・詳細・除外に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lscfg 詳細確認 除外条件**

    - 検証目的: ページングのlscfg 詳細確認 除外条件について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、ページングの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
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

    画面・出力には LABEL が含まれ、lscfg 詳細確認 除外条件の証跡を確認できます。

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



### lsps 属性照合 属性確認 {#c01-i0689}
*分類: ページング*  ・  難易度: 初級

AIX 7.3 の ページング で扱う「lsps 属性照合 属性確認」は、ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドを属性照合の観点で確認する技術項目です。Paging Space 表とsys0 004を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。

**出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en

??? question "確認問題（1問）"
    **問題.** lsps 属性照合 属性確認の技術的な意味を資料で確認するとき、errpt 障害切り分け ログ採取との境界を正しく示す記述はどれですか。

    - A. コマンドまたは機能の用途はAIX エラーログから要約または詳細レポートを生成するコマンドである。
    - B. コマンドまたは機能の用途はSRCとログでstartsrc -s syslogdを用い・Status とSRCサブシステム表示を確認する。
    - C. コマンドまたは機能の用途はデバイス管理でlsattr -El hdisk0を用い・PVID と診断対象表示を確認する。
    - D. コマンドまたは機能の用途はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。 ✅

    正解: **D** ／ 難易度: 初級

    **解説:** Dの記述「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドである」に対応する項目は属性照合 属性確認（属性・lsps）です。ページングの仕様は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」で、確認対象はls・属性・属性です。障害切・errpのA:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は障害切り分け ログ採取（障害・errp）です。変更後・starのB:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は変更後確認 Status（変更・star）です。構成・lsatのC:は「デバイス管理でlsattr -El hdisk0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lsat）です。「lsps」は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を指し、属性照合 属性確認ではls・属性・属性に対応します。

    **出典:** AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en


??? note "検証手順（1件）"
    **lsps 属性照合 属性確認**

    - 検証目的: ページングのlsps 属性照合 属性確認について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。
    - 前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。
    - セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。

    **ステップ 1**
    現在の画面はAIX 7.3の入力画面です。COMMAND ===> に最初の確認操作を入れ、ページングの対象へ進みます。
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
    現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
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

    画面・出力には sys0 が含まれ、lsps 属性照合 属性確認の証跡を確認できます。

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


