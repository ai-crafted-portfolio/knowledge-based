---
search:
  exclude: true
---

# AIX 7.3 — 詳細 (5/6)

[← AIX 7.3 の概要へ戻る](index.md)


## ネットワーク


<section class="kb-item" id="c01-i0655"><h3>no -a バックアウト確認 Link Status 0791</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>遠雷復旧ではAIX 7.3のネットワークで no -a を確認します。遠雷復旧のネットワークでは Link Status とEthernet統計を照合票へ整理します。遠雷復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。遠雷復旧の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、遠雷復旧を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> no -a バックアウト確認 Link Status 0791の設定や表示を読む前に役割を確認します。lsattr 性能確認 実行結果ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はデバイスや sys0 などの属性値を表示するコマンドである。</li><li>B. 一次資料が示す主目的はセキュリティでrolelist -u user1を用い・roles と監査設定を確認する。</li><li>C. 一次資料が示す主目的はLVMでlspvを用い・STALE PARTITIONS と論理ボリューム配置を確認する。</li><li>D. 一次資料が示す主目的はネットワークでno -aを用い・Link Status とEthernet統計を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> バック・noでDの記述「ネットワークでno -aを用い、Link Status」に対応する項目はLink Status（バッ・no）です。バックに関するネットワークの仕様は「ネットワークでno -aを用い、Link Status」で、確認対象はno・バックです。性能・実行・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は性能確認 実行結果（性能・lsat）です。変更前・roleのB:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は変更前確認 roles（変更・role）です。障害切・lspvのC:は「LVMでlspvを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（障害・lspv）です。「no -a」は「ネットワークでno -aを用い、Link Status」を指し、Link Statusではno・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>no -a バックアウト確認 Link Status 0791</strong></p><p>検証目的: ネットワークのno -a バックアウト確認 Link Status 0791について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワークバックアウト確認071-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; no -a
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0791A
画面・出力には AIX0791A が表示され、no -a バックアウト確認 Link Status 0791 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0791B
画面・出力には AIX0791B が表示され、no -a バックアウト確認 Link Status 0791 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0791C
画面・出力には AIX0791C が表示され、no -a バックアウト確認 Link Status 0791 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0791A が画面・出力に表示されること
② ステップ2 の AIX0791B が画面・出力に表示されること
③ ステップ3 の AIX0791C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0656"><h3>no -a 属性確認 Destination 0761</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>白露復旧ではAIX 7.3のネットワークで no -a を確認します。白露復旧のネットワークでは Destination とMTU属性を復旧票へ残します。白露復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。白露復旧の注意点として EtherChannel構成対象の誤選択 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、白露復旧を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「no -a 属性確認 Destination 0761」を「lparstat -i 状態確認 avm 0762」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はネットワークでno -aを用い・Destination とMTU属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割は性能管理でlparstat -iを用い・avm とvmstat表示を確認する。</li><li>C. 仕様上の役割はSRCとログでstartsrc -s inetd -aを用い・IDENTIFIERである。</li><li>D. 仕様上の役割はデバイス管理でrmdev -Rl ent1を用い・attribute とデバイス一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「ネットワークでno -aを用い、Destination とMTU属性を確認する」に対応する項目は属性確認 Destination（属性・no）です。属性に関するネットワークの仕様は「ネットワークでno -aを用い、Destination」で、確認対象はno・属性です。状態・lparのB:は「性能管理でlparstat -iを用い、avm」を述べ、対象は状態確認 avm（状態・lpar）です。障害切・starのC:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け IDENTIFIER（障害・star）です。構成・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は構成照合 attribute（構成・rmde）です。「no -a」は「ネットワークでno -aを用い、Destination」を指し、属性確認 Destinationではno・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>no -a 属性確認 Destination 0761</strong></p><p>検証目的: ネットワークのno -a 属性確認 Destination 0761について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク属性確認041-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; no -a
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0761A
画面・出力には AIX0761A が表示され、no -a 属性確認 Destination 0761 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0761B
画面・出力には AIX0761B が表示され、no -a 属性確認 Destination 0761 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0761C
画面・出力には AIX0761C が表示され、no -a 属性確認 Destination 0761 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0761A が画面・出力に表示されること
② ステップ2 の AIX0761B が画面・出力に表示されること
③ ステップ3 の AIX0761C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0657"><h3>no -a 属性確認 Destination 0821</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 上級</p><p>群青変更ではAIX 7.3のネットワークで no -a を確認します。群青変更のネットワークでは Destination とMTU属性を復旧票へ残します。群青変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。群青変更の注意点として EtherChannel構成対象の誤選択 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、群青変更を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> no -a 属性確認 Destination 0821を保守記録に説明する必要があります。bootinfo -B hdisk0 起動確認 attribute 0832と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はデバイス管理でbootinfo -B hdisk0を用い・attributeである。</li><li>B. 仕様上の役割はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。</li><li>C. 仕様上の役割はセキュリティでrbacqry -u user1 -Tを用い・user attributesである。</li><li>D. 仕様上の役割はネットワークでno -aを用い・Destination とMTU属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 属性・noでDの記述「ネットワークでno -aを用い、Destination」に対応する項目は属性確認 Destination（属性・no）です。属性に関するネットワークの仕様は「ネットワークでno -aを用い、Destination」で、確認対象はno・属性です。起動・bootのA:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は起動確認 attribute（起動・boot）です。運用引・lslvのB:は「LVMでlslvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・lslv）です。属性・rbacのC:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はuser attributes（属性・rbac）です。「no -a」は「ネットワークでno -aを用い、Destination」を指し、属性確認 Destinationではno・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>no -a 属性確認 Destination 0821</strong></p><p>検証目的: ネットワークのno -a 属性確認 Destination 0821について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク属性確認101-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; no -a
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0821A
画面・出力には AIX0821A が表示され、no -a 属性確認 Destination 0821 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0821B
画面・出力には AIX0821B が表示され、no -a 属性確認 Destination 0821 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0821C
画面・出力には AIX0821C が表示され、no -a 属性確認 Destination 0821 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0821A が画面・出力に表示されること
② ステップ2 の AIX0821B が画面・出力に表示されること
③ ステップ3 の AIX0821C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0658"><h3>no -a 属性確認 Media Speed Running 0285</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>深雪復旧ではAIX 7.3のネットワークで no -a を確認します。深雪復旧のネットワークでは Media Speed Running とMTU属性を判定票へ残します。深雪復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。深雪復旧の注意点として EtherChannel構成対象の誤選択 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、深雪復旧を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> no -a 属性確認 Media Speed Running 0285を保守記録に説明する必要があります。lparstat -i 状態確認 fre 0286と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割は性能管理でlparstat -iを用い・fre とvmstat表示を確認する。lparstat -i 状態確認 fre 0286固有の属性も確認対象に含める。</li><li>B. 運用時に利用する技術的役割はLVMでchlvを用い・PVID とボリュームグループ属性を確認する。</li><li>C. 運用時に利用する技術的役割は構成済みデバイスと VPD を表示するコマンドである。</li><li>D. 運用時に利用する技術的役割はネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「ネットワークでno -aを用い、Media Speed Running」に対応する項目はSpeed Running（属性・no）です。属性に関するネットワークの仕様は「ネットワークでno -aを用い、Media Speed」で、確認対象はno・属性です。状態・lparのA:は「性能管理でlparstat -iを用い、fre」を述べ、対象は状態確認 fre（状態・lpar）です。運用引・chlvのB:は「LVMでchlvを用い、PVID とボリュームグループ属性を確認する」を述べ、対象は運用引継ぎ PVID（運用・chlv）です。変更前・lscfのC:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は変更前確認 障害記録（変更・lscf）です。「no -a」は「ネットワークでno -aを用い、Media Speed」を指し、Speed Runningではno・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>no -a 属性確認 Media Speed Running 0285</strong></p><p>検証目的: ネットワークのno -a 属性確認 Media Speed Running 0285について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク属性確認045-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; no -a
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0285A
画面・出力には AIX0285A が表示され、no -a 属性確認 Media Speed Running 0285 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0285B
画面・出力には AIX0285B が表示され、no -a 属性確認 Media Speed Running 0285 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0285C
画面・出力には AIX0285C が表示され、no -a 属性確認 Media Speed Running 0285 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0285A が画面・出力に表示されること
② ステップ2 の AIX0285B が画面・出力に表示されること
③ ステップ3 の AIX0285C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0659"><h3>no -a 属性確認 Media Speed Running 0345</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 上級</p><p>花冷変更ではAIX 7.3のネットワークで no -a を確認します。花冷変更のネットワークでは Media Speed Running とMTU属性を判定票へ残します。花冷変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。花冷変更の注意点として EtherChannel構成対象の誤選択 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、花冷変更を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「no -a 属性確認 Media Speed Running 0345」を「lparstat -i 状態確認 csz 0346」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割は性能管理でlparstat -iを用い・csz とvmstat表示を確認する。</li><li>B. 運用時に利用する技術的役割はLVMでmirrorvgを用い・VG STATE とボリュームグループ属性を確認する。mirrorvg 容量確認 VG STATE 0651固有の属性も確認対象に含める。</li><li>C. 運用時に利用する技術的役割はデバイス管理でbootinfo -B hdisk0を用い・location codeである。</li><li>D. 運用時に利用する技術的役割はネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「ネットワークでno -aを用い、Media Speed Running」に対応する項目はSpeed Running（属性・no）です。属性に関するネットワークの仕様は「ネットワークでno -aを用い、Media Speed」で、確認対象はno・属性です。状態・lparのA:は「性能管理でlparstat -iを用い、csz」を述べ、対象は状態確認 csz（状態・lpar）です。容量・mirrのB:は「LVMでmirrorvgを用い、VG STATE」を述べ、対象はVG STATE（容量・mirr）です。変更前・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象はlocation code（変更・boot）です。「no -a」は「ネットワークでno -aを用い、Media Speed」を指し、Speed Runningではno・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>no -a 属性確認 Media Speed Running 0345</strong></p><p>検証目的: ネットワークのno -a 属性確認 Media Speed Running 0345について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク属性確認105-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; no -a
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0345A
画面・出力には AIX0345A が表示され、no -a 属性確認 Media Speed Running 0345 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0345B
画面・出力には AIX0345B が表示され、no -a 属性確認 Media Speed Running 0345 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0345C
画面・出力には AIX0345C が表示され、no -a 属性確認 Media Speed Running 0345 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0345A が画面・出力に表示されること
② ステップ2 の AIX0345B が画面・出力に表示されること
③ ステップ3 の AIX0345C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0660"><h3>no -a 性能確認 Link Status 0474</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 上級</p><p>銀嶺整理ではAIX 7.3のネットワークで no -a を確認します。銀嶺整理のネットワークでは Link Status とアダプター一覧を変更票へ記録します。銀嶺整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。銀嶺整理の注意点として jumbo frame前提の不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、銀嶺整理を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> no -a 性能確認 Link Status 0474の役割を調べています。lparstat -i 起動確認 PhysB 0475の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としては性能管理でlparstat -iを用い・PhysB とsvmon全体表示を確認する。</li><li>B. 機能の説明としてはLVMでmirrorvgを用い・PVID と論理ボリューム配置を確認する。</li><li>C. 機能の説明としてはネットワークでno -aを用い・Link Status とアダプター一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはデバイス管理でbootinfo -B hdisk0を用い・location code とODM属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「ネットワークでno -aを用い、Link Status とアダプター一覧を確認する」に対応する項目はLink Status（性能・no）です。性能に関するネットワークの仕様は「ネットワークでno -aを用い、Link Status」で、確認対象はno・性能です。起動・lparのA:は「性能管理でlparstat -iを用い、PhysB」を述べ、対象は起動確認 PhysB（起動・lpar）です。監査・mirrのB:は「LVMでmirrorvgを用い、PVID」を述べ、対象は監査記録 PVID（監査・mirr）です。状態・bootのD:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象はlocation code（状態・boot）です。「no -a」は「ネットワークでno -aを用い、Link Status」を指し、Link Statusではno・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>no -a 性能確認 Link Status 0474</strong></p><p>検証目的: ネットワークのno -a 性能確認 Link Status 0474について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク性能確認114-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; no -a
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0474A
画面・出力には AIX0474A が表示され、no -a 性能確認 Link Status 0474 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0474B
画面・出力には AIX0474B が表示され、no -a 性能確認 Link Status 0474 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0474C
画面・出力には AIX0474C が表示され、no -a 性能確認 Link Status 0474 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0474A が画面・出力に表示されること
② ステップ2 の AIX0474B が画面・出力に表示されること
③ ステップ3 の AIX0474C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0661"><h3>no -a 構成照合 Destination 0632</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>夕映採取ではAIX 7.3のネットワークで no -a を確認します。夕映採取のネットワークでは Destination と経路表を引継ぎ票へ保管します。夕映採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。夕映採取の注意点として MTU不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、夕映採取を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> no -a 構成照合 Destination 0632を同一分類のlparstat -i 変更前確認 PhysB 0633と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途は性能管理でlparstat -iを用い・PhysB とAME統計を確認する。</li><li>B. コマンドまたは機能の用途はSRCとログでstartsrc -s inetd -aを用い・IDENTIFIERである。</li><li>C. コマンドまたは機能の用途はネットワークでno -aを用い・Destination と経路表を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はデバイス管理でrmdev -Rl ent1を用い・PVID と診断対象表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「ネットワークでno -aを用い、Destination と経路表を確認する」に対応する項目は構成照合 Destination（構成・no）です。構成に関するネットワークの仕様は「ネットワークでno -aを用い、Destination」で、確認対象はno・構成です。変更前・lparのA:は「性能管理でlparstat -iを用い、PhysB」を述べ、対象は変更前確認 PhysB（変更・lpar）です。監査・starのB:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は監査記録 IDENTIFIER（監査・star）です。変更後・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い、PVID」を述べ、対象は変更後確認 PVID（変更・rmde）です。「no -a」は「ネットワークでno -aを用い、Destination」を指し、構成照合 Destinationではno・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>no -a 構成照合 Destination 0632</strong></p><p>検証目的: ネットワークのno -a 構成照合 Destination 0632について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク構成照合032-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; no -a
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0632A
画面・出力には AIX0632A が表示され、no -a 構成照合 Destination 0632 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0632B
画面・出力には AIX0632B が表示され、no -a 構成照合 Destination 0632 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0632C
画面・出力には AIX0632C が表示され、no -a 構成照合 Destination 0632 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0632A が画面・出力に表示されること
② ステップ2 の AIX0632B が画面・出力に表示されること
③ ステップ3 の AIX0632C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0662"><h3>no -a 構成照合 Media Speed Running 0156</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>若潮採取ではAIX 7.3のネットワークで no -a を確認します。若潮採取のネットワークでは Media Speed Running と経路表を同じ証跡に残します。若潮採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若潮採取の注意点として MTU不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、若潮採取を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> no -a 構成照合 Media Speed Running 0156の技術的な意味を資料で確認するとき、lparstat -i 変更前確認 Entitled Capacity 0157との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は性能管理でlparstat -iを用い・Entitled Capacity とAME統計を確認する。</li><li>B. 構成を確認する際の意味はLVMでchlvを用い・PVID と物理ボリューム一覧を確認する。</li><li>C. 構成を確認する際の意味はネットワークでno -aを用い・Media Speed Running と経路表を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味は性能管理でtopas -Cを用い・csz とAME統計を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「ネットワークでno -aを用い、Media Speed Running」に対応する項目はSpeed Running（構成・no）です。構成に関するネットワークの仕様は「ネットワークでno -aを用い、Media Speed」で、確認対象はno・構成です。変更前・lparのA:は「性能管理でlparstat -iを用い、Entitled」を述べ、対象はEntitled Capacity（変更・lpar）です。性能・chlvのB:は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は性能確認 PVID（性能・chlv）です。運用引・topaのD:は「性能管理でtopas -Cを用い、csz とAME統計を確認する」を述べ、対象は運用引継ぎ csz（運用・topa）です。「no -a」は「ネットワークでno -aを用い、Media Speed」を指し、Speed Runningではno・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>no -a 構成照合 Media Speed Running 0156</strong></p><p>検証目的: ネットワークのno -a 構成照合 Media Speed Running 0156について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク構成照合036-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; no -a
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0156A
画面・出力には AIX0156A が表示され、no -a 構成照合 Media Speed Running 0156 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0156B
画面・出力には AIX0156B が表示され、no -a 構成照合 Media Speed Running 0156 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0156C
画面・出力には AIX0156C が表示され、no -a 構成照合 Media Speed Running 0156 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0156A が画面・出力に表示されること
② ステップ2 の AIX0156B が画面・出力に表示されること
③ ステップ3 の AIX0156C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0663"><h3>no -a 運用引継ぎ Gateway 0126</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 初級</p><p>朝凪採取ではAIX 7.3のネットワークで no -a を確認します。朝凪採取のネットワークでは Gateway とアダプター一覧を変更票へ記録します。朝凪採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。朝凪採取の注意点として jumbo frame前提の不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、朝凪採取を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> no -a 運用引継ぎ Gateway 0126に関する障害切り分けの前提を確認しています。lparstat -i 容量確認 pi 0127の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはネットワークでno -aを用い・Gateway とアダプター一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 機能の説明としては性能管理でlparstat -iを用い・pi とsvmon全体表示を確認する。</li><li>C. 機能の説明としてはLVMでchlvを用い・PP SIZE と論理ボリューム配置を確認する。</li><li>D. 機能の説明としては性能管理でtopas -Cを用い・PhysB とsvmon全体表示を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「ネットワークでno -aを用い、Gateway とアダプター一覧を確認する」に対応する項目は運用引継ぎ Gateway（運用・no）です。運用引に関するネットワークの仕様は「ネットワークでno -aを用い、Gateway」で、確認対象はno・運用引です。容量・lparのB:は「性能管理でlparstat -iを用い、pi」を述べ、対象は容量確認 pi（容量・lpar）です。変更後・chlvのC:は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」を述べ、対象はPP SIZE（変更・chlv）です。構成・topaのD:は「性能管理でtopas -Cを用い、PhysB」を述べ、対象は構成照合 PhysB（構成・topa）です。「no -a」は「ネットワークでno -aを用い、Gateway」を指し、運用引継ぎ Gatewayではno・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>no -a 運用引継ぎ Gateway 0126</strong></p><p>検証目的: ネットワークのno -a 運用引継ぎ Gateway 0126について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク運用引継ぎ006-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; no -a
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0126A
画面・出力には AIX0126A が表示され、no -a 運用引継ぎ Gateway 0126 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0126B
画面・出力には AIX0126B が表示され、no -a 運用引継ぎ Gateway 0126 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0126C
画面・出力には AIX0126C が表示され、no -a 運用引継ぎ Gateway 0126 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0126A が画面・出力に表示されること
② ステップ2 の AIX0126B が画面・出力に表示されること
③ ステップ3 の AIX0126C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0664"><h3>no -a 運用引継ぎ Link Status 0602</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 初級</p><p>春分採取ではAIX 7.3のネットワークで no -a を確認します。春分採取のネットワークでは Link Status とアダプター一覧を確認票へ整理します。春分採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。春分採取の注意点として jumbo frame前提の不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、春分採取を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> no -a 運用引継ぎ Link Status 0602の役割を調べています。lparstat -i 容量確認 fre 0603の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割は性能管理でlparstat -iを用い・fre とsvmon全体表示を確認する。</li><li>B. 障害切り分けに用いる役割はネットワークでno -aを用い・Link Status とアダプター一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割は構成済みデバイスと VPD を表示するコマンドである。</li><li>D. 障害切り分けに用いる役割はデバイス管理でrmdev -Rl ent1を用い・Available とODM属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「ネットワークでno -aを用い、Link Status とアダプター一覧を確認する」に対応する項目はLink Status（運用・no）です。運用引に関するネットワークの仕様は「ネットワークでno -aを用い、Link Status」で、確認対象はno・運用引です。容量・lparのA:は「性能管理でlparstat -iを用い、fre」を述べ、対象は容量確認 fre（容量・lpar）です。詳細・除外・lscfのC:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は詳細確認 除外条件（詳細・lscf）です。性能・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は性能確認 Available（性能・rmde）です。「no -a」は「ネットワークでno -aを用い、Link Status」を指し、Link Statusではno・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>no -a 運用引継ぎ Link Status 0602</strong></p><p>検証目的: ネットワークのno -a 運用引継ぎ Link Status 0602について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク運用引継ぎ002-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; no -a
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0602A
画面・出力には AIX0602A が表示され、no -a 運用引継ぎ Link Status 0602 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0602B
画面・出力には AIX0602B が表示され、no -a 運用引継ぎ Link Status 0602 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0602C
画面・出力には AIX0602C が表示され、no -a 運用引継ぎ Link Status 0602 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0602A が画面・出力に表示されること
② ステップ2 の AIX0602B が画面・出力に表示されること
③ ステップ3 の AIX0602C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0665"><h3>route -n get 変更前確認 Gateway 0693</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>月影保守ではAIX 7.3のネットワークで route -n get を確認します。月影保守のネットワークでは Gateway とMTU属性を判定票へ残します。月影保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。月影保守の注意点として EtherChannel構成対象の誤選択 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、月影保守を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> route -n get 変更前確認 Gateway 0693を保守記録に説明する必要があります。vmo -a 変更後確認 fre 0694と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割は性能管理でvmo -aを用い・fre とvmstat表示を確認する。</li><li>B. 運用時に利用する技術的役割はSRCとログでtail -f /tmp/myfileを用い・TIMESTAMP とエラーログ一覧を確認する。</li><li>C. 運用時に利用する技術的役割はネットワークでroute -n getを用い・Gateway とMTU属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はデバイス管理でlsmpio -l hdisk0を用い・path status とデバイス一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「ネットワークでroute -n getを用い、Gateway とMTU属性を確認する」に対応する項目は変更前確認 Gateway（変更・rout）です。変更前に関するネットワークの仕様は「ネットワークでroute -n getを用い、Gateway」で、確認対象はro・変更前です。変更後・vmoのA:は「性能管理でvmo -aを用い、fre とvmstat表示を確認する」を述べ、対象は変更後確認 fre（変更・vmo）です。運用引・tailのB:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は運用引継ぎ TIMESTAMP（運用・tail）です。バック・lsmpのD:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（バッ・lsmp）です。「route -n get」は「ネットワークでroute -n getを用い、Gateway」を指し、変更前確認 Gatewayではro・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>route -n get 変更前確認 Gateway 0693</strong></p><p>検証目的: ネットワークのroute -n get 変更前確認 Gateway 0693について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更前確認093-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; route -n get
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0693A
画面・出力には AIX0693A が表示され、route -n get 変更前確認 Gateway 0693 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0693B
画面・出力には AIX0693B が表示され、route -n get 変更前確認 Gateway 0693 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0693C
画面・出力には AIX0693C が表示され、route -n get 変更前確認 Gateway 0693 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0693A が画面・出力に表示されること
② ステップ2 の AIX0693B が画面・出力に表示されること
③ ステップ3 の AIX0693C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0666"><h3>route -n get 変更前確認 MTU 0217</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>初霜保守ではAIX 7.3のネットワークで route -n get を確認します。初霜保守のネットワークでは MTU とMTU属性を採取票へ記録します。初霜保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。初霜保守の注意点として EtherChannel構成対象の誤選択 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、初霜保守を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「route -n get 変更前確認 MTU 0217」を「vmo -a 変更後確認 pi 0218」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は性能管理でvmo -aを用い・pi とvmstat表示を確認する。</li><li>B. 保守作業で参照する機能はLVMでmigratepvを用い・LV STATE とボリュームグループ属性を確認する。</li><li>C. 保守作業で参照する機能は性能管理でnmonを用い・PhysB とvmstat表示を確認する。</li><li>D. 保守作業で参照する機能はネットワークでroute -n getを用い・MTU とMTU属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「ネットワークでroute -n getを用い、MTU とMTU属性を確認する」に対応する項目は変更前確認 MTU（変更・rout）です。変更前に関するネットワークの仕様は「ネットワークでroute -n getを用い、MTU」で、確認対象はro・変更前です。変更後・vmoのA:は「性能管理でvmo -aを用い、pi とvmstat表示を確認する」を述べ、対象は変更後確認 pi（変更・vmo）です。属性・migrのB:は「LVMでmigratepvを用い、LV STATE」を述べ、対象はLV STATE（属性・migr）です。容量・nmonのC:は「性能管理でnmonを用い、PhysB とvmstat表示を確認する」を述べ、対象は容量確認 PhysB（容量・nmon）です。「route -n get」は「ネットワークでroute -n getを用い、MTU」を指し、変更前確認 MTUではro・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>route -n get 変更前確認 MTU 0217</strong></p><p>検証目的: ネットワークのroute -n get 変更前確認 MTU 0217について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更前確認097-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; route -n get
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0217A
画面・出力には AIX0217A が表示され、route -n get 変更前確認 MTU 0217 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0217B
画面・出力には AIX0217B が表示され、route -n get 変更前確認 MTU 0217 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0217C
画面・出力には AIX0217C が表示され、route -n get 変更前確認 MTU 0217 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0217A が画面・出力に表示されること
② ステップ2 の AIX0217B が画面・出力に表示されること
③ ステップ3 の AIX0217C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0667"><h3>route -n get 容量確認 EtherChannel 0187</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>風花判定ではAIX 7.3のネットワークで route -n get を確認します。風花判定のネットワークでは EtherChannel とEthernet統計を点検票へ整理します。風花判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。風花判定の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、風花判定を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> route -n get 容量確認 EtherChannel 0187について構成や状態を確認します。usrck -n ALL 性能確認 enhanced_RBAC 0188ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはセキュリティでusrck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。</li><li>B. 対象資源に対する働きはLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。</li><li>C. 対象資源に対する働きはセキュリティでchuserを用い・authorizations とユーザー属性を確認する。chuser 変更前確認 authorizations 0800固有の属性も確認対象に含める。</li><li>D. 対象資源に対する働きはネットワークでroute -n getを用い・EtherChannel とEthernet統計を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「ネットワークでroute -n getを用い、EtherChannel」に対応する項目は容量確認 EtherChannel（容量・rout）です。容量に関するネットワークの仕様は「ネットワークでroute -n getを用い」で、確認対象はro・容量です。性能・usrcのA:は「セキュリティでusrck -n ALLを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・usrc）です。バック・migrのB:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（バッ・migr）です。変更前・chusのC:は「セキュリティでchuserを用い、authorizations」を述べ、対象は変更前確認 authorizatio（変更・chus）です。「route -n get」は「ネットワークでroute -n getを用い」を指し、容量確認 EtherChannelではro・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>route -n get 容量確認 EtherChannel 0187</strong></p><p>検証目的: ネットワークのroute -n get 容量確認 EtherChannel 0187について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク容量確認067-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; route -n get
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0187A
画面・出力には AIX0187A が表示され、route -n get 容量確認 EtherChannel 0187 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0187B
画面・出力には AIX0187B が表示され、route -n get 容量確認 EtherChannel 0187 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0187C
画面・出力には AIX0187C が表示され、route -n get 容量確認 EtherChannel 0187 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0187A が画面・出力に表示されること
② ステップ2 の AIX0187B が画面・出力に表示されること
③ ステップ3 の AIX0187C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0668"><h3>route -n get 容量確認 Media Speed Running 0663</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>新緑判定ではAIX 7.3のネットワークで route -n get を確認します。新緑判定のネットワークでは Media Speed Running とEthernet統計を作業票へ保管します。新緑判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。新緑判定の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、新緑判定を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> route -n get 容量確認 Media Speed Running 0663の設定や表示を読む前に役割を確認します。usrck -n ALL 性能確認 roles 0664ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはネットワークでroute -n getを用い・Media Speed Runningである。 <span class="kb-ok">✅ 正解</span></li><li>B. 状態を読み取るための働きはセキュリティでusrck -n ALLを用い・roles とユーザー属性を確認する。</li><li>C. 状態を読み取るための働きはSRCとログでtail -f /tmp/myfileを用い・PID とinetdデバッグ出力を確認する。</li><li>D. 状態を読み取るための働きはデバイス管理でbootinfo -B hdisk0を用い・Availableである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「ネットワークでroute -n getを用い、Media Speed」に対応する項目はSpeed Running（容量・rout）です。容量に関するネットワークの仕様は「ネットワークでroute -n getを用い、Media」で、確認対象はro・容量です。性能・usrcのB:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は性能確認 roles（性能・usrc）です。構成・tailのC:は「SRCとログでtail -f /tmp/myfileを用い、PID」を述べ、対象は構成照合 PID（構成・tail）です。起動・bootのD:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は起動確認 Available（起動・boot）です。「route -n get」は「ネットワークでroute -n getを用い、Media」を指し、Speed Runningではro・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>route -n get 容量確認 Media Speed Running 0663</strong></p><p>検証目的: ネットワークのroute -n get 容量確認 Media Speed Running 0663について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク容量確認063-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; route -n get
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0663A
画面・出力には AIX0663A が表示され、route -n get 容量確認 Media Speed Running 0663 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0663B
画面・出力には AIX0663B が表示され、route -n get 容量確認 Media Speed Running 0663 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0663C
画面・出力には AIX0663C が表示され、route -n get 容量確認 Media Speed Running 0663 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0663A が画面・出力に表示されること
② ステップ2 の AIX0663B が画面・出力に表示されること
③ ステップ3 の AIX0663C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0669"><h3>route -n get 監査記録 EtherChannel 0375</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 初級</p><p>岩清水記録ではAIX 7.3のネットワークで route -n get を確認します。岩清水記録のネットワークでは EtherChannel とEthernet統計を作業票へ保管します。岩清水記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。岩清水記録の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、岩清水記録を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> route -n get 監査記録 EtherChannel 0375の設定や表示を読む前に役割を確認します。vmo -a 運用引継ぎ pi 0376ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きは性能管理でvmo -aを用い・pi とtopasディスク表示を確認する。</li><li>B. 状態を読み取るための働きはLVMでmirrorvgを用い・STALE PARTITIONS とミラーコピー状態を確認する。</li><li>C. 状態を読み取るための働きはセキュリティでpwdck -n ALLを用い・user attributes とユーザー属性を確認する。pwdck -n ALL 容量確認 user attributes固有の属性も確認対象に含める。</li><li>D. 状態を読み取るための働きはネットワークでroute -n getを用い・EtherChannel とEthernet統計を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「ネットワークでroute -n getを用い、EtherChannel」に対応する項目は監査記録 EtherChannel（監査・rout）です。監査に関するネットワークの仕様は「ネットワークでroute -n getを用い」で、確認対象はro・監査です。運用引・vmoのA:は「性能管理でvmo -aを用い、pi とtopasディスク表示を確認す」を述べ、対象は運用引継ぎ pi（運用・vmo）です。変更前・mirrのB:は「LVMでmirrorvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（変更・mirr）です。容量・pwdcのC:は「セキュリティでpwdck -n ALLを用い、user」を述べ、対象はuser attributes（容量・pwdc）です。「route -n get」は「ネットワークでroute -n getを用い」を指し、監査記録 EtherChannelではro・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>route -n get 監査記録 EtherChannel 0375</strong></p><p>検証目的: ネットワークのroute -n get 監査記録 EtherChannel 0375について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク監査記録015-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; route -n get
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0375A
画面・出力には AIX0375A が表示され、route -n get 監査記録 EtherChannel 0375 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0375B
画面・出力には AIX0375B が表示され、route -n get 監査記録 EtherChannel 0375 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0375C
画面・出力には AIX0375C が表示され、route -n get 監査記録 EtherChannel 0375 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0375A が画面・出力に表示されること
② ステップ2 の AIX0375B が画面・出力に表示されること
③ ステップ3 の AIX0375C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0670"><h3>route -n get 起動確認 EtherChannel 0058</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>潮騒照合ではAIX 7.3のネットワークで route -n get を確認します。潮騒照合のネットワークでは EtherChannel とアダプター一覧を保守票へ記録します。潮騒照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。潮騒照合の注意点として jumbo frame前提の不一致 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、潮騒照合を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> route -n get 起動確認 EtherChannel 0058の役割を調べています。vmo -a 属性確認 po 0059の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容は性能管理でvmo -aを用い・po とsvmon全体表示を確認する。vmo -a 属性確認 po 0059固有の属性も確認対象に含める。</li><li>B. 表示や設定で扱う内容はネットワークでroute -n getを用い・EtherChannel とアダプター一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。</li><li>D. 表示や設定で扱う内容は性能管理でnmonを用い・Entitled Capacity とsvmon全体表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「ネットワークでroute -n getを用い、EtherChannel」に対応する項目は起動確認 EtherChannel（起動・rout）です。ネットワークの仕様は「ネットワークでroute -n getを用い、EtherChannel」で、確認対象はro・起動です。属性・vmoのA:は「性能管理でvmo -aを用い、po とsvmon全体表示を確認する」を述べ、対象は属性確認 po（属性・vmo）です。運用引・migrのC:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・migr）です。障害切・nmonのD:は「性能管理でnmonを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（障害・nmon）です。「route -n get」は「ネットワークでroute -n getを用い」を指し、起動確認 EtherChannelではro・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>route -n get 起動確認 EtherChannel 0058</strong></p><p>検証目的: ネットワークのroute -n get 起動確認 EtherChannel 0058について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク起動確認058-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; route -n get
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0058A
画面・出力には AIX0058A が表示され、route -n get 起動確認 EtherChannel 0058 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0058B
画面・出力には AIX0058B が表示され、route -n get 起動確認 EtherChannel 0058 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0058C
画面・出力には AIX0058C が表示され、route -n get 起動確認 EtherChannel 0058 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0058A が画面・出力に表示されること
② ステップ2 の AIX0058B が画面・出力に表示されること
③ ステップ3 の AIX0058C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0671"><h3>route -n get 起動確認 Media Speed Running 0534</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>星霜照合ではAIX 7.3のネットワークで route -n get を確認します。星霜照合のネットワークでは Media Speed Running とアダプター一覧を変更票へ記録します。星霜照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。星霜照合の注意点として jumbo frame前提の不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、星霜照合を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> route -n get 起動確認 Media Speed Running 0534に関する障害切り分けの前提を確認しています。vmo -a 属性確認 pi 0535の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としては性能管理でvmo -aを用い・pi とsvmon全体表示を確認する。</li><li>B. 機能の説明としてはLVMでmirrorvgを用い・PVID と論理ボリューム配置を確認する。</li><li>C. 機能の説明としてはデバイス管理でbootinfo -B hdisk0を用い・location code とODM属性を確認する。</li><li>D. 機能の説明としてはネットワークでroute -n getを用い・Media Speed Runningである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「ネットワークでroute -n getを用い、Media Speed」に対応する項目はSpeed Running（起動・rout）です。起動に関するネットワークの仕様は「ネットワークでroute -n getを用い、Media」で、確認対象はro・起動です。属性・vmoのA:は「性能管理でvmo -aを用い、pi とsvmon全体表示を確認する」を述べ、対象は属性確認 pi（属性・vmo）です。監査・mirrのB:は「LVMでmirrorvgを用い、PVID」を述べ、対象は監査記録 PVID（監査・mirr）です。状態・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象はlocation code（状態・boot）です。「route -n get」は「ネットワークでroute -n getを用い、Media」を指し、Speed Runningではro・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>route -n get 起動確認 Media Speed Running 0534</strong></p><p>検証目的: ネットワークのroute -n get 起動確認 Media Speed Running 0534について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク起動確認054-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; route -n get
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0534A
画面・出力には AIX0534A が表示され、route -n get 起動確認 Media Speed Running 0534 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0534B
画面・出力には AIX0534B が表示され、route -n get 起動確認 Media Speed Running 0534 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Media Speed Running を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0534C
画面・出力には AIX0534C が表示され、route -n get 起動確認 Media Speed Running 0534 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0534A が画面・出力に表示されること
② ステップ2 の AIX0534B が画面・出力に表示されること
③ ステップ3 の AIX0534C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0672"><h3>route -n get 障害切り分け Gateway 0504</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>霜月確認ではAIX 7.3のネットワークで route -n get を確認します。霜月確認のネットワークでは Gateway と経路表を同じ証跡に残します。霜月確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。霜月確認の注意点として MTU不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、霜月確認を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> route -n get 障害切り分け Gateway 0504を同一分類のvmo -a バックアウト確認 dxm 0505と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は性能管理でvmo -aを用い・dxm とAME統計を確認する。</li><li>B. 構成を確認する際の意味はLVMでmirrorvgを用い・PP SIZE と物理ボリューム一覧を確認する。</li><li>C. 構成を確認する際の意味はデバイス管理でbootinfo -B hdisk0を用い・path status と診断対象表示を確認する。</li><li>D. 構成を確認する際の意味はネットワークでroute -n getを用い・Gateway と経路表を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「ネットワークでroute -n getを用い、Gateway と経路表を確認する」に対応する項目は障害切り分け Gateway（障害・rout）です。障害切に関するネットワークの仕様は「ネットワークでroute -n getを用い、Gateway」で、確認対象はro・障害切です。バック・vmoのA:は「性能管理でvmo -aを用い、dxm とAME統計を確認する」を述べ、対象はバックアウト確認 dxm（バッ・vmo）です。状態・mirrのB:は「LVMでmirrorvgを用い、PP SIZE」を述べ、対象はPP SIZE（状態・mirr）です。監査・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い、path」を述べ、対象はpath status（監査・boot）です。「route -n get」は「ネットワークでroute -n getを用い、Gateway」を指し、障害切り分け Gatewayではro・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>route -n get 障害切り分け Gateway 0504</strong></p><p>検証目的: ネットワークのroute -n get 障害切り分け Gateway 0504について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク障害切り分け024-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; route -n get
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0504A
画面・出力には AIX0504A が表示され、route -n get 障害切り分け Gateway 0504 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0504B
画面・出力には AIX0504B が表示され、route -n get 障害切り分け Gateway 0504 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0504C
画面・出力には AIX0504C が表示され、route -n get 障害切り分け Gateway 0504 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0504A が画面・出力に表示されること
② ステップ2 の AIX0504B が画面・出力に表示されること
③ ステップ3 の AIX0504C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0673"><h3>route -n get 障害切り分け Gateway 0564</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>若草点検ではAIX 7.3のネットワークで route -n get を確認します。若草点検のネットワークでは Gateway と経路表を同じ証跡に残します。若草点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若草点検の注意点として MTU不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、若草点検を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> route -n get 障害切り分け Gateway 0564の技術的な意味を資料で確認するとき、vmo -a バックアウト確認 Entitled Capacity 0565との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は性能管理でvmo -aを用い・Entitled Capacity とAME統計を確認する。</li><li>B. 構成を確認する際の意味はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>C. 構成を確認する際の意味はデバイス管理でlsmpio -l hdisk0を用い・microcode levelである。</li><li>D. 構成を確認する際の意味はネットワークでroute -n getを用い・Gateway と経路表を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「ネットワークでroute -n getを用い、Gateway と経路表を確認する」に対応する項目は障害切り分け Gateway（障害・rout）です。障害切に関するネットワークの仕様は「ネットワークでroute -n getを用い、Gateway」で、確認対象はro・障害切です。バック・vmoのA:は「性能管理でvmo -aを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（バッ・vmo）です。復旧前・lparのB:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は復旧前確認 キュー状態（復旧・lpar）です。運用引・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はmicrocode level（運用・lsmp）です。「route -n get」は「ネットワークでroute -n getを用い、Gateway」を指し、障害切り分け Gatewayではro・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>route -n get 障害切り分け Gateway 0564</strong></p><p>検証目的: ネットワークのroute -n get 障害切り分け Gateway 0564について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク障害切り分け084-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; route -n get
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0564A
画面・出力には AIX0564A が表示され、route -n get 障害切り分け Gateway 0564 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0564B
画面・出力には AIX0564B が表示され、route -n get 障害切り分け Gateway 0564 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Gateway を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0564C
画面・出力には AIX0564C が表示され、route -n get 障害切り分け Gateway 0564 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0564A が画面・出力に表示されること
② ステップ2 の AIX0564B が画面・出力に表示されること
③ ステップ3 の AIX0564C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0674"><h3>route -n get 障害切り分け MTU 0028</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>雪解確認ではAIX 7.3のネットワークで route -n get を確認します。雪解確認のネットワークでは MTU と経路表を監査票へ転記します。雪解確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。雪解確認の注意点として MTU不一致 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、雪解確認を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> route -n get 障害切り分け MTU 0028の技術的な意味を資料で確認するとき、vmo -a バックアウト確認 Busy% 0029との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はネットワークでroute -n getを用い・MTU と経路表を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明は性能管理でvmo -aを用い・Busy% とAME統計を確認する。</li><li>C. 管理対象との関係を表す説明はLVMでmirrorvgを用い・VG STATE と物理ボリューム一覧を確認する。</li><li>D. 管理対象との関係を表す説明は性能管理でnmonを用い・pi とAME統計を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「ネットワークでroute -n getを用い、MTU と経路表を確認する」に対応する項目は障害切り分け MTU（障害・rout）です。ネットワークの仕様は「ネットワークでroute -n getを用い、MTU と経路表を確認する」で、確認対象はro・障害切です。バック・vmoのB:は「性能管理でvmo -aを用い、Busy% とAME統計を確認する」を述べ、対象はバックアウト確認 Busy%（バッ・vmo）です。状態・mirrのC:は「LVMでmirrorvgを用い、VG STATE」を述べ、対象はVG STATE（状態・mirr）です。起動・nmonのD:は「性能管理でnmonを用い、pi とAME統計を確認する」を述べ、対象は起動確認 pi（起動・nmon）です。「route -n get」は「ネットワークでroute -n getを用い、MTU」を指し、障害切り分け MTUではro・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>route -n get 障害切り分け MTU 0028</strong></p><p>検証目的: ネットワークのroute -n get 障害切り分け MTU 0028について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク障害切り分け028-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; route -n get
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0028A
画面・出力には AIX0028A が表示され、route -n get 障害切り分け MTU 0028 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0028B
画面・出力には AIX0028B が表示され、route -n get 障害切り分け MTU 0028 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0028C
画面・出力には AIX0028C が表示され、route -n get 障害切り分け MTU 0028 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0028A が画面・出力に表示されること
② ステップ2 の AIX0028B が画面・出力に表示されること
③ ステップ3 の AIX0028C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0675"><h3>route -n get 障害切り分け MTU 0088</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>翠風点検ではAIX 7.3のネットワークで route -n get を確認します。翠風点検のネットワークでは MTU と経路表を監査票へ転記します。翠風点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。翠風点検の注意点として MTU不一致 を避けるため netstat -rn も併記します。ネットワーク構成管理の作業票として、翠風点検を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> route -n get 障害切り分け MTU 0088を同一分類のvmo -a バックアウト確認 avm 0089と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はネットワークでroute -n getを用い・MTU と経路表を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明は性能管理でvmo -aを用い・avm とAME統計を確認する。</li><li>C. 管理対象との関係を表す説明はLVMでmigratepvを用い・LV STATE と物理ボリューム一覧を確認する。</li><li>D. 管理対象との関係を表す説明は性能管理でnmonを用い・dxm とAME統計を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「ネットワークでroute -n getを用い、MTU と経路表を確認する」に対応する項目は障害切り分け MTU（障害・rout）です。障害切に関するネットワークの仕様は「ネットワークでroute -n getを用い、MTU」で、確認対象はro・障害切です。バック・vmoのB:は「性能管理でvmo -aを用い、avm とAME統計を確認する」を述べ、対象はバックアウト確認 avm（バッ・vmo）です。構成・migrのC:は「LVMでmigratepvを用い、LV STATE」を述べ、対象はLV STATE（構成・migr）です。起動・nmonのD:は「性能管理でnmonを用い、dxm とAME統計を確認する」を述べ、対象は起動確認 dxm（起動・nmon）です。「route -n get」は「ネットワークでroute -n getを用い、MTU」を指し、障害切り分け MTUではro・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>route -n get 障害切り分け MTU 0088</strong></p><p>検証目的: ネットワークのroute -n get 障害切り分け MTU 0088について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク障害切り分け088-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; route -n get
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0088A
画面・出力には AIX0088A が表示され、route -n get 障害切り分け MTU 0088 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0088B
画面・出力には AIX0088B が表示され、route -n get 障害切り分け MTU 0088 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0088C
画面・出力には AIX0088C が表示され、route -n get 障害切り分け MTU 0088 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0088A が画面・出力に表示されること
② ステップ2 の AIX0088B が画面・出力に表示されること
③ ステップ3 の AIX0088C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0676"><h3>smitty etherchannel 変更前確認 Destination 0383</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>新緑記録ではAIX 7.3のネットワークで smitty etherchannel を確認します。新緑記録のネットワークでは Destination とEthernet統計を照合票へ整理します。新緑記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。新緑記録の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、新緑記録を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> smitty etherchannel 変更前確認 Destination 0383の設定や表示を読む前に役割を確認します。filemon 変更後確認 Busy% 0384ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はネットワークでsmitty etherchannelを用い・Destinationである。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的は性能管理でfilemonを用い・Busy% とtopasディスク表示を確認する。</li><li>C. 一次資料が示す主目的はLVMでmklvを用い・LV STATE とミラーコピー状態を確認する。</li><li>D. 一次資料が示す主目的はデバイス管理でdiag -d ent0を用い・attribute と構成マネージャー結果を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「ネットワークでsmitty etherchannelを用い」に対応する項目は変更前確認 Destination（変更・smit）です。変更前に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・変更前です。変更後・fileのB:は「性能管理でfilemonを用い、Busy%」を述べ、対象は変更後確認 Busy%（変更・file）です。起動・mklvのC:は「LVMでmklvを用い、LV STATE」を述べ、対象はLV STATE（起動・mklv）です。障害切・diagのD:は「デバイス管理でdiag -d ent0を用い、attribute」を述べ、対象は障害切り分け attribute（障害・diag）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、変更前確認 Destinationではsm・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>smitty etherchannel 変更前確認 Destination 0383</strong></p><p>検証目的: ネットワークのsmitty etherchannel 変更前確認 Destination 0383について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更前確認023-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; smitty etherchannel
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0383A
画面・出力には AIX0383A が表示され、smitty etherchannel 変更前確認 Destination 0383 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0383B
画面・出力には AIX0383B が表示され、smitty etherchannel 変更前確認 Destination 0383 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0383C
画面・出力には AIX0383C が表示され、smitty etherchannel 変更前確認 Destination 0383 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0383A が画面・出力に表示されること
② ステップ2 の AIX0383B が画面・出力に表示されること
③ ステップ3 の AIX0383C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0677"><h3>smitty etherchannel 変更前確認 Destination 0443</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>秋声整理ではAIX 7.3のネットワークで smitty etherchannel を確認します。秋声整理のネットワークでは Destination とEthernet統計を照合票へ整理します。秋声整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。秋声整理の注意点として 仮想Ethernetバックアップ確認漏れ を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、秋声整理を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> smitty etherchannel 変更前確認 Destination 0443について構成や状態を確認します。filemon 変更後確認 avm 0444ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はネットワークでsmitty etherchannelを用い・Destinationである。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的は性能管理でfilemonを用い・avm とtopasディスク表示を確認する。</li><li>C. 一次資料が示す主目的はLVMでchlvを用い・PP SIZE とミラーコピー状態を確認する。</li><li>D. 一次資料が示す主目的はセキュリティでlsuserを用い・user attributes とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「ネットワークでsmitty etherchannelを用い」に対応する項目は変更前確認 Destination（変更・smit）です。変更前に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・変更前です。変更後・fileのB:は「性能管理でfilemonを用い、avm とtopasディスク表示を確」を述べ、対象は変更後確認 avm（変更・file）です。属性・chlvのC:は「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（属性・chlv）です。バック・lsusのD:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（バッ・lsus）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、変更前確認 Destinationではsm・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>smitty etherchannel 変更前確認 Destination 0443</strong></p><p>検証目的: ネットワークのsmitty etherchannel 変更前確認 Destination 0443について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク変更前確認083-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; smitty etherchannel
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0443A
画面・出力には AIX0443A が表示され、smitty etherchannel 変更前確認 Destination 0443 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0443B
画面・出力には AIX0443B が表示され、smitty etherchannel 変更前確認 Destination 0443 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0443C
画面・出力には AIX0443C が表示され、smitty etherchannel 変更前確認 Destination 0443 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0443A が画面・出力に表示されること
② ステップ2 の AIX0443B が画面・出力に表示されること
③ ステップ3 の AIX0443C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0678"><h3>smitty etherchannel 容量確認 Link Status 0413</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>月影評価ではAIX 7.3のネットワークで smitty etherchannel を確認します。月影評価のネットワークでは Link Status とMTU属性を復旧票へ残します。月影評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。月影評価の注意点として EtherChannel構成対象の誤選択 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、月影評価を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> smitty etherchannel 容量確認 Link Status 0413を保守記録に説明する必要があります。filemon 性能確認 po 0414と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割は性能管理でfilemonを用い・po とvmstat表示を確認する。</li><li>B. 仕様上の役割はLVMでmklvを用い・MIRROR WRITE CONSISTENCY とボリュームグループ属性を確認する。</li><li>C. 仕様上の役割はデバイス管理でdiag -d ent0を用い・microcode level とデバイス一覧を確認する。</li><li>D. 仕様上の役割はネットワークでsmitty etherchannelを用い・Link Status とMTU属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「ネットワークでsmitty etherchannelを用い、Link Status」に対応する項目はLink Status（容量・smit）です。容量に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・容量です。性能・fileのA:は「性能管理でfilemonを用い、po とvmstat表示を確認する」を述べ、対象は性能確認 po（性能・file）です。障害切・mklvのB:は「LVMでmklvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（障害・mklv）です。起動・diagのC:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（起動・diag）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、Link Statusではsm・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>smitty etherchannel 容量確認 Link Status 0413</strong></p><p>検証目的: ネットワークのsmitty etherchannel 容量確認 Link Status 0413について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク容量確認053-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; smitty etherchannel
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0413A
画面・出力には AIX0413A が表示され、smitty etherchannel 容量確認 Link Status 0413 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0413B
画面・出力には AIX0413B が表示され、smitty etherchannel 容量確認 Link Status 0413 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0413C
画面・出力には AIX0413C が表示され、smitty etherchannel 容量確認 Link Status 0413 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0413A が画面・出力に表示されること
② ステップ2 の AIX0413B が画面・出力に表示されること
③ ステップ3 の AIX0413C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0679"><h3>smitty etherchannel 状態確認 Link Status 0096</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>若竹点検ではAIX 7.3のネットワークで smitty etherchannel を確認します。若竹点検のネットワークでは Link Status と経路表を同じ証跡に残します。若竹点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若竹点検の注意点として MTU不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、若竹点検を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> smitty etherchannel 状態確認 Link Status 0096を同一分類のfilemon 構成照合 csz 0097と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は性能管理でfilemonを用い・csz とAME統計を確認する。</li><li>B. 構成を確認する際の意味はLVMでchlvを用い・PVID と物理ボリューム一覧を確認する。chlv 性能確認 PVID 0402固有の属性も確認対象に含める。</li><li>C. 構成を確認する際の意味はネットワークでsmitty etherchannelを用い・Link Status と経路表を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味は性能管理でtopas -Dを用い・avm とAME統計を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「ネットワークでsmitty etherchannelを用い、Link Status」に対応する項目はLink Status（状態・smit）です。状態に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・状態です。構成・fileのA:は「性能管理でfilemonを用い、csz とAME統計を確認する」を述べ、対象は構成照合 csz（構成・file）です。性能・chlvのB:は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は性能確認 PVID（性能・chlv）です。監査・topaのD:は「性能管理でtopas -Dを用い、avm とAME統計を確認する」を述べ、対象は監査記録 avm（監査・topa）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、Link Statusではsm・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>smitty etherchannel 状態確認 Link Status 0096</strong></p><p>検証目的: ネットワークのsmitty etherchannel 状態確認 Link Status 0096について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク状態確認096-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; smitty etherchannel
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0096A
画面・出力には AIX0096A が表示され、smitty etherchannel 状態確認 Link Status 0096 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0096B
画面・出力には AIX0096B が表示され、smitty etherchannel 状態確認 Link Status 0096 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Link Status を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0096C
画面・出力には AIX0096C が表示され、smitty etherchannel 状態確認 Link Status 0096 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0096A が画面・出力に表示されること
② ステップ2 の AIX0096B が画面・出力に表示されること
③ ステップ3 の AIX0096C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0680"><h3>smitty etherchannel 状態確認 MTU 0572</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>水音点検ではAIX 7.3のネットワークで smitty etherchannel を確認します。水音点検のネットワークでは MTU と経路表を引継ぎ票へ保管します。水音点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。水音点検の注意点として MTU不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、水音点検を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> smitty etherchannel 状態確認 MTU 0572の技術的な意味を資料で確認するとき、filemon 構成照合 po 0573との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途は性能管理でfilemonを用い・po とAME統計を確認する。</li><li>B. コマンドまたは機能の用途は構成済みデバイスと VPD を表示するコマンドである。</li><li>C. コマンドまたは機能の用途はネットワークでsmitty etherchannelを用い・MTU と経路表を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はデバイス管理でrmdev -Rl ent1を用い・PVID と診断対象表示を確認する。rmdev -Rl ent1 変更後確認 PVID 0265固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「ネットワークでsmitty etherchannelを用い、MTU」に対応する項目は状態確認 MTU（状態・smit）です。状態に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い、MTU」で、確認対象はsm・状態です。構成・fileのA:は「性能管理でfilemonを用い、po とAME統計を確認する」を述べ、対象は構成照合 po（構成・file）です。一覧・表示・lscfのB:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は一覧確認 LPAR表示（一覧・lscf）です。変更後・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い、PVID」を述べ、対象は変更後確認 PVID（変更・rmde）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い、MTU」を指し、状態確認 MTUではsm・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>smitty etherchannel 状態確認 MTU 0572</strong></p><p>検証目的: ネットワークのsmitty etherchannel 状態確認 MTU 0572について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク状態確認092-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; smitty etherchannel
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0572A
画面・出力には AIX0572A が表示され、smitty etherchannel 状態確認 MTU 0572 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0572B
画面・出力には AIX0572B が表示され、smitty etherchannel 状態確認 MTU 0572 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MTU を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0572C
画面・出力には AIX0572C が表示され、smitty etherchannel 状態確認 MTU 0572 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0572A が画面・出力に表示されること
② ステップ2 の AIX0572B が画面・出力に表示されること
③ ステップ3 の AIX0572C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0681"><h3>smitty etherchannel 監査記録 Destination 0066</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>陽炎照合ではAIX 7.3のネットワークで smitty etherchannel を確認します。陽炎照合のネットワークでは Destination とアダプター一覧を変更票へ記録します。陽炎照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。陽炎照合の注意点として jumbo frame前提の不一致 を避けるため entstat -d ent0 も併記します。ネットワーク構成管理の作業票として、陽炎照合を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> smitty etherchannel 監査記録 Destination 0066の役割を調べています。filemon 運用引継ぎ PhysB 0067の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としては性能管理でfilemonを用い・PhysB とsvmon全体表示を確認する。</li><li>B. 機能の説明としてはネットワークでsmitty etherchannelを用い・Destinationである。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としてはLVMでchlvを用い・PP SIZE と論理ボリューム配置を確認する。</li><li>D. 機能の説明としては性能管理でtopas -Dを用い・po とsvmon全体表示を確認する。topas -D 状態確認 po 0679固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「ネットワークでsmitty etherchannelを用い」に対応する項目は監査記録 Destination（監査・smit）です。ネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・監査です。運用引・fileのA:は「性能管理でfilemonを用い、PhysB」を述べ、対象は運用引継ぎ PhysB（運用・file）です。変更後・chlvのC:は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」を述べ、対象はPP SIZE（変更・chlv）です。状態・topaのD:は「性能管理でtopas -Dを用い、po とsvmon全体表示を確認す」を述べ、対象は状態確認 po（状態・topa）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、監査記録 Destinationではsm・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>smitty etherchannel 監査記録 Destination 0066</strong></p><p>検証目的: ネットワークのsmitty etherchannel 監査記録 Destination 0066について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク監査記録066-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; smitty etherchannel
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0066A
画面・出力には AIX0066A が表示され、smitty etherchannel 監査記録 Destination 0066 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0066B
画面・出力には AIX0066B が表示され、smitty etherchannel 監査記録 Destination 0066 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Destination を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; ifconfig en0
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0066C
画面・出力には AIX0066C が表示され、smitty etherchannel 監査記録 Destination 0066 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0066A が画面・出力に表示されること
② ステップ2 の AIX0066B が画面・出力に表示されること
③ ステップ3 の AIX0066C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0682"><h3>smitty etherchannel 監査記録 EtherChannel 0542</h3><p class="kb-meta">分類: ネットワーク ・ 難易度: 中級</p><p>紅葉照合ではAIX 7.3のネットワークで smitty etherchannel を確認します。紅葉照合のネットワークでは EtherChannel とアダプター一覧を確認票へ整理します。紅葉照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。紅葉照合の注意点として jumbo frame前提の不一致 を避けるため ifconfig en0 も併記します。ネットワーク構成管理の作業票として、紅葉照合を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> smitty etherchannel 監査記録 EtherChannel 0542に関する障害切り分けの前提を確認しています。filemon 運用引継ぎ Busy% 0543の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割は性能管理でfilemonを用い・Busy% とsvmon全体表示を確認する。</li><li>B. 障害切り分けに用いる役割は構成済みデバイスと VPD を表示するコマンドである。</li><li>C. 障害切り分けに用いる役割はネットワークでsmitty etherchannelを用い・EtherChannelである。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割はデバイス管理でdiag -d ent0を用い・microcode level とODM属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「ネットワークでsmitty etherchannelを用い」に対応する項目は監査記録 EtherChannel（監査・smit）です。監査に関するネットワークの仕様は「ネットワークでsmitty etherchannelを用い」で、確認対象はsm・監査です。運用引・fileのA:は「性能管理でfilemonを用い、Busy%」を述べ、対象は運用引継ぎ Busy%（運用・file）です。復旧前・lscfのB:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は復旧前確認 障害記録（復旧・lscf）です。容量・diagのD:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（容量・diag）です。「smitty etherchannel」は「ネットワークでsmitty etherchannelを用い」を指し、監査記録 EtherChannelではsm・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>smitty etherchannel 監査記録 EtherChannel 0542</strong></p><p>検証目的: ネットワークのsmitty etherchannel 監査記録 EtherChannel 0542について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=ネットワーク監査記録062-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; smitty etherchannel
→ Enter を押す
［画面・出力］
ent0 Available 00-00 PCIe3 10GbE SR Adapter
en0  Available 00-00 Standard Ethernet Network Interface
確認コード AIX0542A
画面・出力には AIX0542A が表示され、smitty etherchannel 監査記録 EtherChannel 0542 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; entstat -d ent0
→ Enter を押す
［画面・出力］
10/100/1000 Base-TX Adapter Specific Statistics:
Link Status: Up
Media Speed Running: 1000 Mbps Full Duplex
確認コード AIX0542B
画面・出力には AIX0542B が表示され、smitty etherchannel 監査記録 EtherChannel 0542 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EtherChannel を読むため、ネットワーク の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; netstat -rn
→ Enter を押す
［画面・出力］
Routing tables
Destination        Gateway           Flags   Refs     Use  If
default            192.0.2.1         UG        4      241  en0
確認コード AIX0542C
画面・出力には AIX0542C が表示され、smitty etherchannel 監査記録 EtherChannel 0542 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0542A が画面・出力に表示されること
② ステップ2 の AIX0542B が画面・出力に表示されること
③ ステップ3 の AIX0542C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


## ページング


<section class="kb-item" id="c01-i0683"><h3>lparstat 一覧確認 保存場所</h3><p class="kb-meta">分類: ページング ・ 難易度: 中級</p><p>AIX 7.3 の ページング で扱う「lparstat 一覧確認 保存場所」は、LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドを一覧確認の観点で確認する技術項目です。Paging Space 表とsys0 060を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lparstat 一覧確認 保存場所の技術的な意味を資料で確認するとき、lspv 状態判定 照合単位との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。lspv 状態判定 照合単位固有の属性も確認対象に含める。</li><li>B. 管理対象との関係を表す説明は性能管理でlparstat -iを用い・fre とvmstat表示を確認する。</li><li>C. 管理対象との関係を表す説明はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はSRCとログでerrclearを用い・PID とinetdデバッグ出力を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドである」に対応する項目は一覧確認 保存場所（一覧・lpar）です。ページングの仕様は「LPAR の CPU 使用率、物理CPU消費、AME」で、確認対象はlp・一覧・保存です。状態・照合・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は状態判定 照合単位（状態・lspv）です。状態・lparのB:は「性能管理でlparstat -iを用い、fre」を述べ、対象は状態確認 fre（状態・lpar）です。性能・errcのD:は「SRCとログでerrclearを用い、PID」を述べ、対象は性能確認 PID（性能・errc）です。「lparstat」は「LPAR の CPU 使用率、物理CPU消費、AME」を指し、一覧確認 保存場所ではlp・一覧・保存に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lparstat 一覧確認 保存場所</strong></p><p>検証目的: ページングのlparstat 一覧確認 保存場所について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ページングの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; vmstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: lcpu=2 mem=1024MB tmem=512MB ent=0.40 mmode=dedicated-E
 r b avm fre csz cfr dxm ci co pi po in sy cs
画面・出力には System が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lparstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
%user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
画面・出力には System が含まれ、lparstat 一覧確認 保存場所の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ボリュームグループの取り違えを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; topas
→ Enter を押す
［画面・出力］
Topas Monitor for host: aixhost
CPU User% Kern% Wait% Idle%
AME TMEM,MB 512 CMEM,MB 114 EF[T/A] 2.0/1.5
画面・出力には Topas が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の System が画面・出力に表示されること
② ステップ2 の System が画面・出力に表示されること
③ ステップ3 の Topas が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0684"><h3>lparstat 障害切り分け 受信先</h3><p class="kb-meta">分類: ページング ・ 難易度: 中級</p><p>AIX 7.3 の ページング で扱う「lparstat 障害切り分け 受信先」は、LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドを障害切り分けの観点で確認する技術項目です。Paging Space 表とsys0 020を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lparstat 障害切り分け 受信先の技術的な意味を資料で確認するとき、lspv 変更前確認 保持設定との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。</li><li>B. 構成を確認する際の意味はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味は導入と起動でbootlist -m normalを用い・mksysb image とOSレベル表示を確認する。</li><li>D. 構成を確認する際の意味はLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドである」に対応する項目は障害切り分け 受信先（障害・lpar）です。ページングの仕様は「LPAR の CPU 使用率、物理CPU消費、AME」で、確認対象はlp・障害切です。変更前・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は変更前確認 保持設定（変更・lspv）です。容量・bootのC:は「導入と起動でbootlist -m normalを用い」を述べ、対象はmksysb image（容量・boot）です。バック・migrのD:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（バッ・migr）です。「lparstat」は「LPAR の CPU 使用率、物理CPU消費、AME」を指し、障害切り分け 受信先ではlp・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lparstat 障害切り分け 受信先</strong></p><p>検証目的: ページングのlparstat 障害切り分け 受信先について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ページングの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; vmstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: lcpu=2 mem=1024MB tmem=512MB ent=0.40 mmode=dedicated-E
 r b avm fre csz cfr dxm ci co pi po in sy cs
画面・出力には System が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lparstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
%user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
画面・出力には System が含まれ、lparstat 障害切り分け 受信先の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ボリュームグループの取り違えを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; topas
→ Enter を押す
［画面・出力］
Topas Monitor for host: aixhost
CPU User% Kern% Wait% Idle%
AME TMEM,MB 512 CMEM,MB 114 EF[T/A] 2.0/1.5
画面・出力には Topas が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の System が画面・出力に表示されること
② ステップ2 の System が画面・出力に表示されること
③ ステップ3 の Topas が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0685"><h3>lsattr 変更前確認 パス状態</h3><p class="kb-meta">分類: ページング ・ 難易度: 中級</p><p>AIX 7.3 の ページング で扱う「lsattr 変更前確認 パス状態」は、デバイスや sys0 などの属性値を表示するコマンドを変更前確認の観点で確認する技術項目です。Paging Space 表とsys0 036を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr 変更前確認 パス状態の技術的な意味を資料で確認するとき、chdev 復旧前確認 仮想化表示との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はデバイスや sys0 などの属性値を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はデバイス属性を変更する管理コマンドである。</li><li>C. 管理対象との関係を表す説明はネットワークでnetstat -rnを用い・Media Speed Runningである。</li><li>D. 管理対象との関係を表す説明はJFS2でmount -o remountを用い・agblksize とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「デバイスや sys0 などの属性値を表示するコマンドである」に対応する項目は変更前確認 パス状態（変更・lsat）です。ページングの仕様は「デバイスや sys0 などの属性値を表示するコマンド」で、確認対象はls・変更前です。復旧前・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は復旧前確認 仮想化表示（復旧・chde）です。状態・netsのC:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（状態・nets）です。性能・mounのD:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 agblksize（性能・moun）です。「lsattr」は「デバイスや sys0 などの属性値を表示するコマンド」を指し、変更前確認 パス状態ではls・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr 変更前確認 パス状態</strong></p><p>検証目的: ページングのlsattr 変更前確認 パス状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ページングの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d4e36        rootvg          active
hdisk1          00f6a1b2c3d5e36        datavg          active
画面・出力には hdisk0 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1092
画面・出力には VOLUME が含まれ、lsattr 変更前確認 パス状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、PVID の誤読を切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
画面・出力には NAME が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の hdisk0 が画面・出力に表示されること
② ステップ2 の VOLUME が画面・出力に表示されること
③ ステップ3 の NAME が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0686"><h3>lsattr 状態判定 ディスク状態</h3><p class="kb-meta">分類: ページング ・ 難易度: 上級</p><p>AIX 7.3 の ページング で扱う「lsattr 状態判定 ディスク状態」は、デバイスや sys0 などの属性値を表示するコマンドを状態判定の観点で確認する技術項目です。Paging Space 表とsys0 076を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr 状態判定 ディスク状態の技術的な意味を資料で確認するとき、chdev 属性照合 ボリューム状態との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はデバイスや sys0 などの属性値を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はデバイス属性を変更する管理コマンドである。</li><li>C. コマンドまたは機能の用途はセキュリティでlssecattr -cを用い・audit class とRBAC属性を確認する。</li><li>D. コマンドまたは機能の用途は導入と起動でalt_disk_copyを用い・altinst_rootvg と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「デバイスや sys0 などの属性値を表示するコマンドである」に対応する項目は状態判定 ディスク状態（状態・lsat）です。ページングの仕様は「デバイスや sys0 などの属性値を表示するコマンド」で、確認対象はls・状態・ディです。属性・ボリ・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は属性照合 ボリューム状態（属性・chde）です。障害切・lsseのC:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（障害・lsse）です。変更前・alt_のD:は「導入と起動でalt_disk_copyを用い」を述べ、対象は変更前確認 altinst_root（変更・alt_）です。「lsattr」は「デバイスや sys0 などの属性値を表示するコマンド」を指し、状態判定 ディスク状態ではls・状態・ディに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr 状態判定 ディスク状態</strong></p><p>検証目的: ページングのlsattr 状態判定 ディスク状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ページングの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d4e76        rootvg          active
hdisk1          00f6a1b2c3d5e76        datavg          active
画面・出力には hdisk0 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1092
画面・出力には VOLUME が含まれ、lsattr 状態判定 ディスク状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、PVID の誤読を切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
画面・出力には NAME が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の hdisk0 が画面・出力に表示されること
② ステップ2 の VOLUME が画面・出力に表示されること
③ ステップ3 の NAME が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0687"><h3>lscfg 性能確認 ページング状態</h3><p class="kb-meta">分類: ページング ・ 難易度: 中級</p><p>AIX 7.3 の ページング で扱う「lscfg 性能確認 ページング状態」は、構成済みデバイスと VPD を表示するコマンドを性能確認の観点で確認する技術項目です。Paging Space 表とsys0 028を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lscfg 性能確認 ページング状態の技術的な意味を資料で確認するとき、vmstat 変更前確認 性能値との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途は構成済みデバイスと VPD を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>C. コマンドまたは機能の用途は導入と起動でmksysbを用い・bootlist とOSレベル表示を確認する。</li><li>D. コマンドまたは機能の用途はLVMでchlvを用い・PP SIZE とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「構成済みデバイスと VPD を表示するコマンドである」に対応する項目は性能確認 ページング状態（性能・lscf）です。ページングの仕様は「構成済みデバイスと VPD を表示するコマンド」で、確認対象はls・性能・ペーです。変更前・vmstのB:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は変更前確認 性能値（変更・vmst）です。障害切・mksyのC:は「導入と起動でmksysbを用い、bootlist」を述べ、対象は障害切り分け bootlist（障害・mksy）です。構成・chlvのD:は「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（構成・chlv）です。「lscfg」は「構成済みデバイスと VPD を表示するコマンド」を指し、性能確認 ページング状態ではls・性能・ペーに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lscfg 性能確認 ページング状態</strong></p><p>検証目的: ページングのlscfg 性能確認 ページング状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ページングの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt
→ Enter を押す
［画面・出力］
ERROR_IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  ERROR_DESCRIPTION
0E017ED1         0405131090 P H mem2           Memory failure
画面・出力には ERROR が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt -a -N hdisk1
→ Enter を押す
［画面・出力］
LABEL: DISK_ERR4
RESOURCE NAME: hdisk1
Description
DISK OPERATION ERROR
画面・出力には LABEL が含まれ、lscfg 性能確認 ページング状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ページング使用率の見落としを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; /usr/lib/errdemon -l
→ Enter を押す
［画面・出力］
/var/adm/ras/errlog
画面・出力には errlog が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ERROR が画面・出力に表示されること
② ステップ2 の LABEL が画面・出力に表示されること
③ ステップ3 の errlog が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0688"><h3>lscfg 詳細確認 除外条件</h3><p class="kb-meta">分類: ページング ・ 難易度: 上級</p><p>AIX 7.3 の ページング で扱う「lscfg 詳細確認 除外条件」は、構成済みデバイスと VPD を表示するコマンドを詳細確認の観点で確認する技術項目です。Paging Space 表とsys0 068を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lscfg 詳細確認 除外条件の技術的な意味を資料で確認するとき、vmstat 状態判定 イベント転送との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>B. 構成を確認する際の意味は構成済みデバイスと VPD を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はセキュリティでchuserを用い・user attributes とRBAC属性を確認する。</li><li>D. 構成を確認する際の意味は導入と起動でmksysbを用い・Technology Level と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「構成済みデバイスと VPD を表示するコマンドである」に対応する項目は詳細確認 除外条件（詳細・lscf）です。ページングの仕様は「構成済みデバイスと VPD を表示するコマンド」で、確認対象はls・詳細・除外です。状態・イベ・vmstのA:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は状態判定 イベント転送（状態・vmst）です。容量・chusのC:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（容量・chus）です。監査・mksyのD:は「導入と起動でmksysbを用い、Technology Level」を述べ、対象はTechnology Level（監査・mksy）です。「lscfg」は「構成済みデバイスと VPD を表示するコマンド」を指し、詳細確認 除外条件ではls・詳細・除外に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lscfg 詳細確認 除外条件</strong></p><p>検証目的: ページングのlscfg 詳細確認 除外条件について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ページングの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt
→ Enter を押す
［画面・出力］
ERROR_IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  ERROR_DESCRIPTION
0E017ED1         0405131090 P H mem2           Memory failure
画面・出力には ERROR が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt -a -N hdisk1
→ Enter を押す
［画面・出力］
LABEL: DISK_ERR4
RESOURCE NAME: hdisk1
Description
DISK OPERATION ERROR
画面・出力には LABEL が含まれ、lscfg 詳細確認 除外条件の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ページング使用率の見落としを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; /usr/lib/errdemon -l
→ Enter を押す
［画面・出力］
/var/adm/ras/errlog
画面・出力には errlog が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ERROR が画面・出力に表示されること
② ステップ2 の LABEL が画面・出力に表示されること
③ ステップ3 の errlog が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0689"><h3>lsps 属性照合 属性確認</h3><p class="kb-meta">分類: ページング ・ 難易度: 初級</p><p>AIX 7.3 の ページング で扱う「lsps 属性照合 属性確認」は、ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドを属性照合の観点で確認する技術項目です。Paging Space 表とsys0 004を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsps 属性照合 属性確認の技術的な意味を資料で確認するとき、errpt 障害切り分け ログ採取との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>B. コマンドまたは機能の用途はSRCとログでstartsrc -s syslogdを用い・Status とSRCサブシステム表示を確認する。</li><li>C. コマンドまたは機能の用途はデバイス管理でlsattr -El hdisk0を用い・PVID と診断対象表示を確認する。</li><li>D. コマンドまたは機能の用途はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドである」に対応する項目は属性照合 属性確認（属性・lsps）です。ページングの仕様は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」で、確認対象はls・属性・属性です。障害切・errpのA:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は障害切り分け ログ採取（障害・errp）です。変更後・starのB:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は変更後確認 Status（変更・star）です。構成・lsatのC:は「デバイス管理でlsattr -El hdisk0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lsat）です。「lsps」は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を指し、属性照合 属性確認ではls・属性・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsps 属性照合 属性確認</strong></p><p>検証目的: ページングのlsps 属性照合 属性確認について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ページングの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsattr -E -l sys0 -a iostat
→ Enter を押す
［画面・出力］
iostat true Continuously maintain disk I/O history True
画面・出力には iostat が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; chdev -l sys0 -a iostat=true
→ Enter を押す
［画面・出力］
sys0 changed
画面・出力には sys0 が含まれ、lsps 属性照合 属性確認の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、資源名の誤指定を切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lscfg -l sysplanar0
→ Enter を押す
［画面・出力］
DEVICE          LOCATION     DESCRIPTION
sysplanar0      00-00        CPU Planar
画面・出力には DEVICE が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の iostat が画面・出力に表示されること
② ステップ2 の sys0 が画面・出力に表示されること
③ ステップ3 の DEVICE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0690"><h3>lsps 復旧前確認 復旧手掛かり</h3><p class="kb-meta">分類: ページング ・ 難易度: 中級</p><p>AIX 7.3 の ページング で扱う「lsps 復旧前確認 復旧手掛かり」は、ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドを復旧前確認の観点で確認する技術項目です。Paging Space 表とsys0 044を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsps 復旧前確認 復旧手掛かりの技術的な意味を資料で確認するとき、errpt 一覧確認 監査証跡との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>B. 構成を確認する際の意味はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はネットワークでchdev -l en0 -aを用い・EtherChannel とアダプター一覧を確認する。</li><li>D. 構成を確認する際の意味はJFS2でchfsを用い・ファイルシステム使用率 とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドである」に対応する項目は復旧前確認 復旧手掛かり（復旧・lsps）です。ページングの仕様は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」で、確認対象はls・復旧前です。一覧・監査・errpのA:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は一覧確認 監査証跡（一覧・errp）です。容量・chdeのC:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は容量確認 EtherChannel（容量・chde）です。バック・chfsのD:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象はバックアウト確認 ファイルシステム使（バッ・chfs）です。「lsps」は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を指し、復旧前確認 復旧手掛かりではls・復旧前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsps 復旧前確認 復旧手掛かり</strong></p><p>検証目的: ページングのlsps 復旧前確認 復旧手掛かりについて、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ページングの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsattr -E -l sys0 -a iostat
→ Enter を押す
［画面・出力］
iostat true Continuously maintain disk I/O history True
画面・出力には iostat が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; chdev -l sys0 -a iostat=true
→ Enter を押す
［画面・出力］
sys0 changed
画面・出力には sys0 が含まれ、lsps 復旧前確認 復旧手掛かりの証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、資源名の誤指定を切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lscfg -l sysplanar0
→ Enter を押す
［画面・出力］
DEVICE          LOCATION     DESCRIPTION
sysplanar0      00-00        CPU Planar
画面・出力には DEVICE が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の iostat が画面・出力に表示されること
② ステップ2 の sys0 が画面・出力に表示されること
③ ステップ3 の DEVICE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0691"><h3>lsvg 一覧確認 詳細表示</h3><p class="kb-meta">分類: ページング ・ 難易度: 中級</p><p>AIX 7.3 の ページング で扱う「lsvg 一覧確認 詳細表示」は、ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドを一覧確認の観点で確認する技術項目です。Paging Space 表とsys0 052を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg 一覧確認 詳細表示の技術的な意味を資料で確認するとき、lslv 詳細確認 構成照合との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途は論理ボリュームの属性と割り当て情報を表示するコマンドである。</li><li>B. コマンドまたは機能の用途は性能管理でvmstat 2 2を用い・Busy% とvmstat表示を確認する。</li><li>C. コマンドまたは機能の用途はSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。</li><li>D. コマンドまたは機能の用途はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドである」に対応する項目は一覧確認 詳細表示（一覧・lsvg）です。ページングの仕様は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」で、確認対象はls・一覧・詳細です。詳細・構成・lslvのA:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は詳細確認 構成照合（詳細・lslv）です。障害切・vmstのB:は「性能管理でvmstat 2 2を用い、Busy%」を述べ、対象は障害切り分け Busy%（障害・vmst）です。構成・tailのC:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は構成照合 IDENTIFIER（構成・tail）です。「lsvg」は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を指し、一覧確認 詳細表示ではls・一覧・詳細に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg 一覧確認 詳細表示</strong></p><p>検証目的: ページングのlsvg 一覧確認 詳細表示について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ページングの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lslv hd4
→ Enter を押す
［画面・出力］
LOGICAL VOLUME: hd4
VOLUME GROUP: rootvg
LV STATE: opened/syncd
TYPE: jfs2
画面・出力には LOGICAL が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsps -a
→ Enter を押す
［画面・出力］
Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
画面・出力には Page が含まれ、lsvg 一覧確認 詳細表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、停止中の論理ボリューム見落としを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; smit lsps
→ Enter を押す
［画面・出力］
SMIT fast path: lsps
Command to run: lsps -a
Paging space list displayed
画面・出力には SMIT が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の LOGICAL が画面・出力に表示されること
② ステップ2 の Page が画面・出力に表示されること
③ ステップ3 の SMIT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0692"><h3>lsvg 障害切り分け 設定値</h3><p class="kb-meta">分類: ページング ・ 難易度: 初級</p><p>AIX 7.3 の ページング で扱う「lsvg 障害切り分け 設定値」は、ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドを障害切り分けの観点で確認する技術項目です。Paging Space 表とsys0 012を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg 障害切り分け 設定値の技術的な意味を資料で確認するとき、lslv 性能確認 起動確認との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明は論理ボリュームの属性と割り当て情報を表示するコマンドである。</li><li>B. 管理対象との関係を表す説明はSRCとログでtail -f /tmp/myfileを用い・Subsystemである。</li><li>C. 管理対象との関係を表す説明はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はLVMでchvgを用い・VG STATE とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドである」に対応する項目は障害切り分け 設定値（障害・lsvg）です。ページングの仕様は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」で、確認対象はls・障害切です。性能・起動・lslvのA:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は性能確認 起動確認（性能・lslv）です。属性・tailのB:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は属性確認 Subsystem（属性・tail）です。性能・chvgのD:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（性能・chvg）です。「lsvg」は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を指し、障害切り分け 設定値ではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg 障害切り分け 設定値</strong></p><p>検証目的: ページングのlsvg 障害切り分け 設定値について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ページングの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lslv hd4
→ Enter を押す
［画面・出力］
LOGICAL VOLUME: hd4
VOLUME GROUP: rootvg
LV STATE: opened/syncd
TYPE: jfs2
画面・出力には LOGICAL が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。Paging Space 表を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsps -a
→ Enter を押す
［画面・出力］
Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
画面・出力には Page が含まれ、lsvg 障害切り分け 設定値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、停止中の論理ボリューム見落としを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; smit lsps
→ Enter を押す
［画面・出力］
SMIT fast path: lsps
Command to run: lsps -a
Paging space list displayed
画面・出力には SMIT が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の LOGICAL が画面・出力に表示されること
② ステップ2 の Page が画面・出力に表示されること
③ ステップ3 の SMIT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


## 導入と起動


<section class="kb-item" id="c01-i0693"><h3>alt_disk_copy 変更前確認 EFIX LABEL 0133</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>月影採取ではAIX 7.3の導入と起動で alt_disk_copy を確認します。月影採取の導入と起動では EFIX LABEL と起動デバイス設定を採取票へ記録します。月影採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。月影採取の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、月影採取を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_copy 変更前確認 EFIX LABEL 0133を保守記録に説明する必要があります。netstat -v 変更後確認 MTU 0134と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はネットワークでnetstat -vを用い・MTU とアダプター一覧を確認する。</li><li>B. 保守作業で参照する機能はデバイス管理でchdev -l hdisk0を用い・location code とODM属性を確認する。</li><li>C. 保守作業で参照する機能は導入と起動でalt_disk_copyを用い・EFIX LABEL と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はネットワークでchdev -l en0 -aを用い・Media Speed Runningである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「導入と起動でalt_disk_copyを用い、EFIX LABEL」に対応する項目はEFIX LABEL（変更・alt_）です。変更前に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、EFIX LABEL」で、確認対象はal・変更前です。変更後・netsのA:は「ネットワークでnetstat -vを用い、MTU」を述べ、対象は変更後確認 MTU（変更・nets）です。起動・chdeのB:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象はlocation code（起動・chde）です。容量・chdeのD:は「ネットワークでchdev -l en0 -aを用い、Media」を述べ、対象はSpeed Running（容量・chde）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を指し、EFIX LABELではal・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 変更前確認 EFIX LABEL 0133</strong></p><p>検証目的: 導入と起動のalt_disk_copy 変更前確認 EFIX LABEL 0133について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認013-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0133A
画面・出力には AIX0133A が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0133 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0133B
画面・出力には AIX0133B が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0133 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0133C
画面・出力には AIX0133C が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0133 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0133A が画面・出力に表示されること
② ステップ2 の AIX0133B が画面・出力に表示されること
③ ステップ3 の AIX0133C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0694"><h3>alt_disk_copy 変更前確認 EFIX LABEL 0193</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>朝霧判定ではAIX 7.3の導入と起動で alt_disk_copy を確認します。朝霧判定の導入と起動では EFIX LABEL と起動デバイス設定を採取票へ記録します。朝霧判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。朝霧判定の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、朝霧判定を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「alt_disk_copy 変更前確認 EFIX LABEL 0193」を「netstat -v 変更後確認 MTU 0194」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は導入と起動でalt_disk_copyを用い・EFIX LABEL と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はネットワークでnetstat -vを用い・MTU とアダプター一覧を確認する。</li><li>C. 保守作業で参照する機能はデバイス管理でcfgmgrを用い・attribute とODM属性を確認する。</li><li>D. 保守作業で参照する機能はネットワークでchdev -l en0 -aを用い・Media Speed Runningである。chdev -l en0 -a mtu=1500 容量確認 Media固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でalt_disk_copyを用い、EFIX LABEL」に対応する項目はEFIX LABEL（変更・alt_）です。変更前に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、EFIX LABEL」で、確認対象はal・変更前です。変更後・netsのB:は「ネットワークでnetstat -vを用い、MTU」を述べ、対象は変更後確認 MTU（変更・nets）です。属性・cfgmのC:は「デバイス管理でcfgmgrを用い、attribute」を述べ、対象は属性確認 attribute（属性・cfgm）です。容量・chdeのD:は「ネットワークでchdev -l en0 -aを用い、Media」を述べ、対象はSpeed Running（容量・chde）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を指し、EFIX LABELではal・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 変更前確認 EFIX LABEL 0193</strong></p><p>検証目的: 導入と起動のalt_disk_copy 変更前確認 EFIX LABEL 0193について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認073-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0193A
画面・出力には AIX0193A が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0193 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0193B
画面・出力には AIX0193B が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0193 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0193C
画面・出力には AIX0193C が表示され、alt_disk_copy 変更前確認 EFIX LABEL 0193 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0193A が画面・出力に表示されること
② ステップ2 の AIX0193B が画面・出力に表示されること
③ ステップ3 の AIX0193C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0695"><h3>alt_disk_copy 変更前確認 altinst_rootvg 0609</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>銀砂採取ではAIX 7.3の導入と起動で alt_disk_copy を確認します。銀砂採取の導入と起動では altinst_rootvg と起動デバイス設定を判定票へ残します。銀砂採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。銀砂採取の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、銀砂採取を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「alt_disk_copy 変更前確認 altinst_rootvg 0609」を「netstat -v 変更後確認 Gateway 0610」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はネットワークでnetstat -vを用い・Gateway とアダプター一覧を確認する。netstat -v 変更後確認 Gateway 0610固有の属性も確認対象に含める。</li><li>B. 運用時に利用する技術的役割はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>C. 運用時に利用する技術的役割は導入と起動でalt_disk_copyを用い・altinst_rootvg と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はセキュリティでlssecattr -cを用い・audit class とRBAC属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「導入と起動でalt_disk_copyを用い、altinst_rootvg」に対応する項目は変更前確認 altinst_root（変更・alt_）です。変更前に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い」で、確認対象はal・変更前です。変更後・netsのA:は「ネットワークでnetstat -vを用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・nets）です。詳細・表形・errpのB:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は詳細確認 表形式（詳細・errp）です。障害切・lsseのD:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（障害・lsse）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い」を指し、変更前確認 altinst_rootではal・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 変更前確認 altinst_rootvg 0609</strong></p><p>検証目的: 導入と起動のalt_disk_copy 変更前確認 altinst_rootvg 0609について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認009-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0609A
画面・出力には AIX0609A が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0609 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0609B
画面・出力には AIX0609B が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0609 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0609C
画面・出力には AIX0609C が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0609 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0609A が画面・出力に表示されること
② ステップ2 の AIX0609B が画面・出力に表示されること
③ ステップ3 の AIX0609C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0696"><h3>alt_disk_copy 変更前確認 altinst_rootvg 0669</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>梅雨晴判定ではAIX 7.3の導入と起動で alt_disk_copy を確認します。梅雨晴判定の導入と起動では altinst_rootvg と起動デバイス設定を判定票へ残します。梅雨晴判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。梅雨晴判定の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、梅雨晴判定を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_copy 変更前確認 altinst_rootvg 0669を保守記録に説明する必要があります。netstat -v 変更後確認 Gateway 0670と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割は導入と起動でalt_disk_copyを用い・altinst_rootvg と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はネットワークでnetstat -vを用い・Gateway とアダプター一覧を確認する。netstat -v 変更後確認 Gateway 0670固有の属性も確認対象に含める。</li><li>C. 運用時に利用する技術的役割はJFS2でdf -gを用い・lff と内部スナップショットを確認する。</li><li>D. 運用時に利用する技術的役割はセキュリティでsetsecattrを用い・user attributes とRBAC属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でalt_disk_copyを用い、altinst_rootvg」に対応する項目は変更前確認 altinst_root（変更・alt_）です。変更前に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い」で、確認対象はal・変更前です。変更後・netsのB:は「ネットワークでnetstat -vを用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・nets）です。運用引・dfのC:は「JFS2でdf -gを用い、lff と内部スナップショットを確認する」を述べ、対象は運用引継ぎ lff（運用・df）です。バック・setsのD:は「セキュリティでsetsecattrを用い、user」を述べ、対象はuser attributes（バッ・sets）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い」を指し、変更前確認 altinst_rootではal・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 変更前確認 altinst_rootvg 0669</strong></p><p>検証目的: 導入と起動のalt_disk_copy 変更前確認 altinst_rootvg 0669について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認069-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0669A
画面・出力には AIX0669A が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0669 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0669B
画面・出力には AIX0669B が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0669 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0669C
画面・出力には AIX0669C が表示され、alt_disk_copy 変更前確認 altinst_rootvg 0669 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0669A が画面・出力に表示されること
② ステップ2 の AIX0669B が画面・出力に表示されること
③ ステップ3 の AIX0669C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0697"><h3>alt_disk_copy 容量確認 fileset level 0639</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>秋桜採取ではAIX 7.3の導入と起動で alt_disk_copy を確認します。秋桜採取の導入と起動では fileset level とfileset一覧を作業票へ保管します。秋桜採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。秋桜採取の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、秋桜採取を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_copy 容量確認 fileset level 0639の設定や表示を読む前に役割を確認します。netstat -v 性能確認 Media Speed Running 0640ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはネットワークでnetstat -vを用い・Media Speed Running と経路表を確認する。netstat -v 性能確認 Media Speed Running固有の属性も確認対象に含める。</li><li>B. 状態を読み取るための働きはJFS2でdf -gを用い・agblksize とマウントオプションを確認する。</li><li>C. 状態を読み取るための働きは導入と起動でalt_disk_copyを用い・fileset level とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 状態を読み取るための働きはセキュリティでlssecattr -cを用い・audit class とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でalt_disk_copyを用い、fileset level」に対応する項目はfileset level（容量・alt_）です。容量に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、fileset」で、確認対象はal・容量です。性能・netsのA:は「ネットワークでnetstat -vを用い、Media Speed」を述べ、対象はSpeed Running（性能・nets）です。構成・dfのB:は「JFS2でdf -gを用い、agblksize」を述べ、対象は構成照合 agblksize（構成・df）です。起動・lsseのD:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（起動・lsse）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、fileset」を指し、fileset levelではal・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 容量確認 fileset level 0639</strong></p><p>検証目的: 導入と起動のalt_disk_copy 容量確認 fileset level 0639について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認039-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0639A
画面・出力には AIX0639A が表示され、alt_disk_copy 容量確認 fileset level 0639 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0639B
画面・出力には AIX0639B が表示され、alt_disk_copy 容量確認 fileset level 0639 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0639C
画面・出力には AIX0639C が表示され、alt_disk_copy 容量確認 fileset level 0639 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0639A が画面・出力に表示されること
② ステップ2 の AIX0639B が画面・出力に表示されること
③ ステップ3 の AIX0639C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0698"><h3>alt_disk_copy 容量確認 fileset level 0699</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>山吹保守ではAIX 7.3の導入と起動で alt_disk_copy を確認します。山吹保守の導入と起動では fileset level とfileset一覧を作業票へ保管します。山吹保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。山吹保守の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、山吹保守を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_copy 容量確認 fileset level 0699について構成や状態を確認します。netstat -v 性能確認 Media Speed Running 0700ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはネットワークでnetstat -vを用い・Media Speed Running と経路表を確認する。netstat -v 性能確認 Media Speed Running固有の属性も確認対象に含める。</li><li>B. 状態を読み取るための働きはLVMでchlvを用い・VG STATE とミラーコピー状態を確認する。</li><li>C. 状態を読み取るための働きはセキュリティでsetsecattrを用い・user attributes とユーザー属性を確認する。</li><li>D. 状態を読み取るための働きは導入と起動でalt_disk_copyを用い・fileset level とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でalt_disk_copyを用い、fileset level」に対応する項目はfileset level（容量・alt_）です。容量に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、fileset」で、確認対象はal・容量です。性能・netsのA:は「ネットワークでnetstat -vを用い、Media Speed」を述べ、対象はSpeed Running（性能・nets）です。構成・chlvのB:は「LVMでchlvを用い、VG STATE」を述べ、対象はVG STATE（構成・chlv）です。属性・setsのC:は「セキュリティでsetsecattrを用い、user」を述べ、対象はuser attributes（属性・sets）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、fileset」を指し、fileset levelではal・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 容量確認 fileset level 0699</strong></p><p>検証目的: 導入と起動のalt_disk_copy 容量確認 fileset level 0699について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認099-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0699A
画面・出力には AIX0699A が表示され、alt_disk_copy 容量確認 fileset level 0699 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0699B
画面・出力には AIX0699B が表示され、alt_disk_copy 容量確認 fileset level 0699 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0699C
画面・出力には AIX0699C が表示され、alt_disk_copy 容量確認 fileset level 0699 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0699A が画面・出力に表示されること
② ステップ2 の AIX0699B が画面・出力に表示されること
③ ステップ3 の AIX0699C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0699"><h3>alt_disk_copy 容量確認 mksysb image 0163</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>秋声判定ではAIX 7.3の導入と起動で alt_disk_copy を確認します。秋声判定の導入と起動では mksysb image とfileset一覧を点検票へ整理します。秋声判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。秋声判定の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、秋声判定を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_copy 容量確認 mksysb image 0163について構成や状態を確認します。netstat -v 性能確認 EtherChannel 0164ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きは導入と起動でalt_disk_copyを用い・mksysb image とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはネットワークでnetstat -vを用い・EtherChannel と経路表を確認する。</li><li>C. 対象資源に対する働きはデバイス管理でchdev -l hdisk0を用い・path status と診断対象表示を確認する。chdev -l hdisk0 障害切り分け path status固有の属性も確認対象に含める。</li><li>D. 対象資源に対する働きはネットワークでchdev -l en0 -aを用い・Gateway と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でalt_disk_copyを用い、mksysb image」に対応する項目はmksysb image（容量・alt_）です。容量に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、mksysb」で、確認対象はal・容量です。性能・netsのB:は「ネットワークでnetstat -vを用い、EtherChannel」を述べ、対象は性能確認 EtherChannel（性能・nets）です。障害切・chdeのC:は「デバイス管理でchdev -l hdisk0を用い、path」を述べ、対象はpath status（障害・chde）です。変更前・chdeのD:は「ネットワークでchdev -l en0 -aを用い、Gateway」を述べ、対象は変更前確認 Gateway（変更・chde）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、mksysb」を指し、mksysb imageではal・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 容量確認 mksysb image 0163</strong></p><p>検証目的: 導入と起動のalt_disk_copy 容量確認 mksysb image 0163について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認043-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0163A
画面・出力には AIX0163A が表示され、alt_disk_copy 容量確認 mksysb image 0163 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0163B
画面・出力には AIX0163B が表示され、alt_disk_copy 容量確認 mksysb image 0163 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0163C
画面・出力には AIX0163C が表示され、alt_disk_copy 容量確認 mksysb image 0163 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0163A が画面・出力に表示されること
② ステップ2 の AIX0163B が画面・出力に表示されること
③ ステップ3 の AIX0163C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0700"><h3>alt_disk_copy 容量確認 mksysb image 0223</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>新緑保守ではAIX 7.3の導入と起動で alt_disk_copy を確認します。新緑保守の導入と起動では mksysb image とfileset一覧を点検票へ整理します。新緑保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。新緑保守の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、新緑保守を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_copy 容量確認 mksysb image 0223の設定や表示を読む前に役割を確認します。netstat -v 性能確認 EtherChannel 0224ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きは導入と起動でalt_disk_copyを用い・mksysb image とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはネットワークでnetstat -vを用い・EtherChannel と経路表を確認する。</li><li>C. 対象資源に対する働きはデバイス管理でcfgmgrを用い・microcode level と診断対象表示を確認する。</li><li>D. 対象資源に対する働きはネットワークでchdev -l en0 -aを用い・Gateway と経路表を確認する。chdev -l en0 -a mtu=1500 変更前確認固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「導入と起動でalt_disk_copyを用い、mksysb image」に対応する項目はmksysb image（容量・alt_）です。容量に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、mksysb」で、確認対象はal・容量です。性能・netsのB:は「ネットワークでnetstat -vを用い、EtherChannel」を述べ、対象は性能確認 EtherChannel（性能・nets）です。バック・cfgmのC:は「デバイス管理でcfgmgrを用い、microcode level」を述べ、対象はmicrocode level（バッ・cfgm）です。変更前・chdeのD:は「ネットワークでchdev -l en0 -aを用い、Gateway」を述べ、対象は変更前確認 Gateway（変更・chde）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、mksysb」を指し、mksysb imageではal・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 容量確認 mksysb image 0223</strong></p><p>検証目的: 導入と起動のalt_disk_copy 容量確認 mksysb image 0223について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認103-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0223A
画面・出力には AIX0223A が表示され、alt_disk_copy 容量確認 mksysb image 0223 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0223B
画面・出力には AIX0223B が表示され、alt_disk_copy 容量確認 mksysb image 0223 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0223C
画面・出力には AIX0223C が表示され、alt_disk_copy 容量確認 mksysb image 0223 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0223A が画面・出力に表示されること
② ステップ2 の AIX0223B が画面・出力に表示されること
③ ステップ3 の AIX0223C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0701"><h3>alt_disk_copy 状態確認 bootlist 0798</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>春霞復旧ではAIX 7.3の導入と起動で alt_disk_copy を確認します。春霞復旧の導入と起動では bootlist とOSレベル表示を変更票へ記録します。春霞復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。春霞復旧の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、春霞復旧を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_copy 状態確認 bootlist 0798に関する障害切り分けの前提を確認しています。lslv 変更前確認 運用記録の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としては導入と起動でalt_disk_copyを用い・bootlist とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 機能の説明としては論理ボリュームの属性と割り当て情報を表示するコマンドである。</li><li>C. 機能の説明としてはセキュリティでlsuserを用い・user attributes とユーザー属性を確認する。</li><li>D. 機能の説明としては導入と起動でbosboot -a -dを用い・altinst_rootvg とfileset一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 状態・alt_でAの記述「導入と起動でalt_disk_copyを用い、bootlist」に対応する項目は状態確認 bootlist（状態・alt_）です。状態に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、bootlist」で、確認対象はal・状態です。変更前・lslvのB:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は変更前確認 運用記録（変更・lslv）です。バック・lsusのC:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（バッ・lsus）です。変更後・bosbのD:は「導入と起動でbosboot -a -dを用い」を述べ、対象は変更後確認 altinst_root（変更・bosb）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、bootlist」を指し、状態確認 bootlistではal・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 状態確認 bootlist 0798</strong></p><p>検証目的: 導入と起動のalt_disk_copy 状態確認 bootlist 0798について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認078-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0798A
画面・出力には AIX0798A が表示され、alt_disk_copy 状態確認 bootlist 0798 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0798B
画面・出力には AIX0798B が表示され、alt_disk_copy 状態確認 bootlist 0798 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0798C
画面・出力には AIX0798C が表示され、alt_disk_copy 状態確認 bootlist 0798 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0798A が画面・出力に表示されること
② ステップ2 の AIX0798B が画面・出力に表示されること
③ ステップ3 の AIX0798C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0702"><h3>alt_disk_copy 状態確認 fileset level 0322</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>春分変更ではAIX 7.3の導入と起動で alt_disk_copy を確認します。春分変更の導入と起動では fileset level とOSレベル表示を保守票へ記録します。春分変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。春分変更の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、春分変更を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_copy 状態確認 fileset level 0322の役割を調べています。netstat -v 構成照合 MTU 0323の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はネットワークでnetstat -vを用い・MTU とEthernet統計を確認する。</li><li>B. 表示や設定で扱う内容はデバイス管理でcfgmgrを用い・location code と構成マネージャー結果を確認する。</li><li>C. 表示や設定で扱う内容は導入と起動でalt_disk_copyを用い・fileset level とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はセキュリティでsetsecattrを用い・audit class とロール一覧を確認する。setsecattr 変更後確認 audit class 0015固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でalt_disk_copyを用い、fileset level」に対応する項目はfileset level（状態・alt_）です。状態に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、fileset」で、確認対象はal・状態です。構成・netsのA:は「ネットワークでnetstat -vを用い、MTU」を述べ、対象は構成照合 MTU（構成・nets）です。性能・cfgmのB:は「デバイス管理でcfgmgrを用い、location code」を述べ、対象はlocation code（性能・cfgm）です。変更後・setsのD:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（変更・sets）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、fileset」を指し、fileset levelではal・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 状態確認 fileset level 0322</strong></p><p>検証目的: 導入と起動のalt_disk_copy 状態確認 fileset level 0322について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認082-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0322A
画面・出力には AIX0322A が表示され、alt_disk_copy 状態確認 fileset level 0322 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0322B
画面・出力には AIX0322B が表示され、alt_disk_copy 状態確認 fileset level 0322 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0322C
画面・出力には AIX0322C が表示され、alt_disk_copy 状態確認 fileset level 0322 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0322A が画面・出力に表示されること
② ステップ2 の AIX0322B が画面・出力に表示されること
③ ステップ3 の AIX0322C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0703"><h3>alt_disk_copy 監査記録 Technology Level 0828</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>雪解変更ではAIX 7.3の導入と起動で alt_disk_copy を確認します。雪解変更の導入と起動では Technology Level と代替ディスク状態を同じ証跡に残します。雪解変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。雪解変更の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、雪解変更を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_copy 監査記録 Technology Level 0828の技術的な意味を資料で確認するとき、alt_disk_copy 障害切り分け EFIX LABEL 0004との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は導入と起動でalt_disk_copyを用い・EFIX LABEL と代替ディスク状態を確認する。</li><li>B. 構成を確認する際の意味はセキュリティでpwdck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。pwdck -n ALL 監査記録 enhanced_RBAC 0256固有の属性も確認対象に含める。</li><li>C. 構成を確認する際の意味はSRCとログでsyslog_ssw -rを用い・TIMESTAMP とsyslog設定変換を確認する。</li><li>D. 構成を確認する際の意味は導入と起動でalt_disk_copyを用い・Technology Level と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査・alt_でDの記述「導入と起動でalt_disk_copyを用い、Technology」に対応する項目はTechnology Level（監査・alt_）です。監査に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い、Technology」で、確認対象はal・監査です。障害切・alt_のA:は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（障害・alt_）です。監査・pwdcのB:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・pwdc）です。障害切・syslのC:は「SRCとログでsyslog_ssw -rを用い、TIMESTAMP」を述べ、対象は障害切り分け TIMESTAMP（障害・sysl）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、Technology」を指し、Technology Levelではal・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 監査記録 Technology Level 0828</strong></p><p>検証目的: 導入と起動のalt_disk_copy 監査記録 Technology Level 0828について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録108-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0828A
画面・出力には AIX0828A が表示され、alt_disk_copy 監査記録 Technology Level 0828 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0828B
画面・出力には AIX0828B が表示され、alt_disk_copy 監査記録 Technology Level 0828 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0828C
画面・出力には AIX0828C が表示され、alt_disk_copy 監査記録 Technology Level 0828 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0828A が画面・出力に表示されること
② ステップ2 の AIX0828B が画面・出力に表示されること
③ ステップ3 の AIX0828C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0704"><h3>alt_disk_copy 監査記録 altinst_rootvg 0352</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>夕映変更ではAIX 7.3の導入と起動で alt_disk_copy を確認します。夕映変更の導入と起動では altinst_rootvg と代替ディスク状態を監査票へ転記します。夕映変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。夕映変更の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、夕映変更を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_copy 監査記録 altinst_rootvg 0352を同一分類のnetstat -v 運用引継ぎ EtherChannel 0353と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はネットワークでnetstat -vを用い・EtherChannel とMTU属性を確認する。</li><li>B. 管理対象との関係を表す説明は導入と起動でalt_disk_copyを用い・altinst_rootvg と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はデバイス管理でcfgmgrを用い・path status とデバイス一覧を確認する。cfgmgr 変更後確認 path status 0658固有の属性も確認対象に含める。</li><li>D. 管理対象との関係を表す説明はセキュリティでsetsecattrを用い・audit class と監査設定を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「導入と起動でalt_disk_copyを用い、altinst_rootvg」に対応する項目は監査記録 altinst_rootv（監査・alt_）です。監査に関する導入と起動の仕様は「導入と起動でalt_disk_copyを用い」で、確認対象はal・監査です。運用引・netsのA:は「ネットワークでnetstat -vを用い、EtherChannel」を述べ、対象は運用引継ぎ EtherChannel（運用・nets）です。変更後・cfgmのC:は「デバイス管理でcfgmgrを用い、path status」を述べ、対象はpath status（変更・cfgm）です。性能・setsのD:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（性能・sets）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い」を指し、監査記録 altinst_rootvではal・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 監査記録 altinst_rootvg 0352</strong></p><p>検証目的: 導入と起動のalt_disk_copy 監査記録 altinst_rootvg 0352について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録112-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0352A
画面・出力には AIX0352A が表示され、alt_disk_copy 監査記録 altinst_rootvg 0352 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0352B
画面・出力には AIX0352B が表示され、alt_disk_copy 監査記録 altinst_rootvg 0352 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0352C
画面・出力には AIX0352C が表示され、alt_disk_copy 監査記録 altinst_rootvg 0352 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0352A が画面・出力に表示されること
② ステップ2 の AIX0352B が画面・出力に表示されること
③ ステップ3 の AIX0352C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0705"><h3>alt_disk_copy 障害切り分け EFIX LABEL 0004</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>若草確認ではAIX 7.3の導入と起動で alt_disk_copy を確認します。若草確認の導入と起動では EFIX LABEL と代替ディスク状態を監査票へ転記します。若草確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若草確認の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、若草確認を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_copy 障害切り分け EFIX LABEL 0004の技術的な意味を資料で確認するとき、netstat -v バックアウト確認 Destination 0005との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はネットワークでnetstat -vを用い・Destination とMTU属性を確認する。</li><li>B. 管理対象との関係を表す説明はデバイス管理でchdev -l hdisk0を用い・location code とデバイス一覧を確認する。</li><li>C. 管理対象との関係を表す説明は導入と起動でalt_disk_copyを用い・EFIX LABEL と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はネットワークでchdev -l en0 -aを用い・MTU とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「導入と起動でalt_disk_copyを用い、EFIX LABEL」に対応する項目はEFIX LABEL（障害・alt_）です。導入と起動の仕様は「導入と起動でalt_disk_copyを用い、EFIX LABEL」で、確認対象はal・障害切です。バック・netsのA:は「ネットワークでnetstat -vを用い、Destination」を述べ、対象はバックアウト確認 Destinati（バッ・nets）です。状態・chdeのB:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象はlocation code（状態・chde）です。起動・chdeのD:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は起動確認 MTU（起動・chde）です。「alt_disk_copy」は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を指し、EFIX LABELではal・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_copy 障害切り分け EFIX LABEL 0004</strong></p><p>検証目的: 導入と起動のalt_disk_copy 障害切り分け EFIX LABEL 0004について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け004-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_copy
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0004A
画面・出力には AIX0004A が表示され、alt_disk_copy 障害切り分け EFIX LABEL 0004 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0004B
画面・出力には AIX0004B が表示され、alt_disk_copy 障害切り分け EFIX LABEL 0004 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0004C
画面・出力には AIX0004C が表示され、alt_disk_copy 障害切り分け EFIX LABEL 0004 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0004A が画面・出力に表示されること
② ステップ2 の AIX0004B が画面・出力に表示されること
③ ステップ3 の AIX0004C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0706"><h3>alt_disk_mksysb バックアウト確認 bootlist 0065</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>花冷照合ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。花冷照合の導入と起動では bootlist と起動デバイス設定を復旧票へ残します。花冷照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。花冷照合の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、花冷照合を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「alt_disk_mksysb バックアウト確認 bootlist 0065」を「smitty etherchannel 監査記録 Destination 0066」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はネットワークでsmitty etherchannelを用い・Destinationである。</li><li>B. 仕様上の役割は導入と起動でalt_disk_mksysbを用い・bootlist と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割はデバイス管理でodmget CuDvを用い・PVID とODM属性を確認する。odmget CuDv 変更前確認 PVID 0371固有の属性も確認対象に含める。</li><li>D. 仕様上の役割はネットワークでentstat -d ent0を用い・MTU とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でalt_disk_mksysbを用い、bootlist」に対応する項目はバックアウト確認 bootlist（バッ・alt_）です。導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い、bootlist」で、確認対象はal・バックです。監査・smitのA:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は監査記録 Destination（監査・smit）です。変更前・odmgのC:は「デバイス管理でodmget CuDvを用い、PVID」を述べ、対象は変更前確認 PVID（変更・odmg）です。属性・entsのD:は「ネットワークでentstat -d ent0を用い、MTU」を述べ、対象は属性確認 MTU（属性・ents）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い、bootlist」を指し、バックアウト確認 bootlistではal・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_mksysb バックアウト確認 bootlist 0065</strong></p><p>検証目的: 導入と起動のalt_disk_mksysb バックアウト確認 bootlist 0065について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認065-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0065A
画面・出力には AIX0065A が表示され、alt_disk_mksysb バックアウト確認 bootlist 0065 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0065B
画面・出力には AIX0065B が表示され、alt_disk_mksysb バックアウト確認 bootlist 0065 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0065C
画面・出力には AIX0065C が表示され、alt_disk_mksysb バックアウト確認 bootlist 0065 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0065A が画面・出力に表示されること
② ステップ2 の AIX0065B が画面・出力に表示されること
③ ステップ3 の AIX0065C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0707"><h3>alt_disk_mksysb バックアウト確認 mksysb image 0541</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>群青照合ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。群青照合の導入と起動では mksysb image と起動デバイス設定を採取票へ記録します。群青照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。群青照合の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、群青照合を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_mksysb バックアウト確認 mksysb image 0541を保守記録に説明する必要があります。smitty etherchannel 監査記録 EtherChannel 0542と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はネットワークでsmitty etherchannelを用い・EtherChannelである。</li><li>B. 保守作業で参照する機能は導入と起動でalt_disk_mksysbを用い・mksysb image と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はデバイス属性を変更する管理コマンドである。</li><li>D. 保守作業で参照する機能はセキュリティでsetsecattrを用い・audit class とRBAC属性を確認する。setsecattr 運用引継ぎ audit class 0234固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でalt_disk_mksysbを用い、mksysb image」に対応する項目はmksysb image（バッ・alt_）です。バックに関する導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い、mksysb」で、確認対象はal・バックです。監査・smitのA:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は監査記録 EtherChannel（監査・smit）です。変更前・chdeのC:は「デバイス属性を変更する管理コマンド」を述べ、対象は変更前確認 識別値（変更・chde）です。運用引・setsのD:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（運用・sets）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い、mksysb」を指し、mksysb imageではal・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_mksysb バックアウト確認 mksysb image 0541</strong></p><p>検証目的: 導入と起動のalt_disk_mksysb バックアウト確認 mksysb image 0541について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認061-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0541A
画面・出力には AIX0541A が表示され、alt_disk_mksysb バックアウト確認 mksysb image 0541 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0541B
画面・出力には AIX0541B が表示され、alt_disk_mksysb バックアウト確認 mksysb image 0541 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0541C
画面・出力には AIX0541C が表示され、alt_disk_mksysb バックアウト確認 mksysb image 0541 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0541A が画面・出力に表示されること
② ステップ2 の AIX0541B が画面・出力に表示されること
③ ステップ3 の AIX0541C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0708"><h3>alt_disk_mksysb 属性確認 EFIX LABEL 0571</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>松風点検ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。松風点検の導入と起動では EFIX LABEL とfileset一覧を点検票へ整理します。松風点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。松風点検の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、松風点検を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_mksysb 属性確認 EFIX LABEL 0571について構成や状態を確認します。smitty etherchannel 状態確認 MTU 0572ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはネットワークでsmitty etherchannelを用い・MTU と経路表を確認する。</li><li>B. 対象資源に対する働きは導入と起動でalt_disk_mksysbを用い・EFIX LABEL とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはデバイス属性を変更する管理コマンドである。</li><li>D. 対象資源に対する働きはセキュリティでchuserを用い・user attributes とユーザー属性を確認する。chuser 変更前確認 user attributes 0264固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でalt_disk_mksysbを用い、EFIX LABEL」に対応する項目はEFIX LABEL（属性・alt_）です。属性に関する導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い、EFIX」で、確認対象はal・属性です。状態・smitのA:は「ネットワークでsmitty etherchannelを用い、MTU」を述べ、対象は状態確認 MTU（状態・smit）です。復旧前・chdeのC:は「デバイス属性を変更する管理コマンド」を述べ、対象は復旧前確認 仮想化表示（復旧・chde）です。変更前・chusのD:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（変更・chus）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い、EFIX」を指し、EFIX LABELではal・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_mksysb 属性確認 EFIX LABEL 0571</strong></p><p>検証目的: 導入と起動のalt_disk_mksysb 属性確認 EFIX LABEL 0571について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認091-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0571A
画面・出力には AIX0571A が表示され、alt_disk_mksysb 属性確認 EFIX LABEL 0571 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0571B
画面・出力には AIX0571B が表示され、alt_disk_mksysb 属性確認 EFIX LABEL 0571 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0571C
画面・出力には AIX0571C が表示され、alt_disk_mksysb 属性確認 EFIX LABEL 0571 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0571A が画面・出力に表示されること
② ステップ2 の AIX0571B が画面・出力に表示されること
③ ステップ3 の AIX0571C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0709"><h3>alt_disk_mksysb 属性確認 Technology Level 0095</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>岩清水点検ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。岩清水点検の導入と起動では Technology Level とfileset一覧を照合票へ整理します。岩清水点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。岩清水点検の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、岩清水点検を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_mksysb 属性確認 Technology Level 0095の設定や表示を読む前に役割を確認します。smitty etherchannel 状態確認 Link Status 0096ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はネットワークでsmitty etherchannelを用い・Link Status と経路表を確認する。</li><li>B. 一次資料が示す主目的はデバイス管理でodmget CuDvを用い・Available と診断対象表示を確認する。</li><li>C. 一次資料が示す主目的はネットワークでentstat -d ent0を用い・EtherChannel と経路表を確認する。</li><li>D. 一次資料が示す主目的は導入と起動でalt_disk_mksysbを用い・Technology Levelである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でalt_disk_mksysbを用い、Technology」に対応する項目はTechnology Level（属性・alt_）です。属性に関する導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い」で、確認対象はal・属性です。状態・smitのA:は「ネットワークでsmitty etherchannelを用い」を述べ、対象はLink Status（状態・smit）です。容量・odmgのB:は「デバイス管理でodmget CuDvを用い、Available」を述べ、対象は容量確認 Available（容量・odmg）です。バック・entsのC:は「ネットワークでentstat -d ent0を用い」を述べ、対象はバックアウト確認 EtherChan（バッ・ents）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い」を指し、Technology Levelではal・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_mksysb 属性確認 Technology Level 0095</strong></p><p>検証目的: 導入と起動のalt_disk_mksysb 属性確認 Technology Level 0095について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認095-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0095A
画面・出力には AIX0095A が表示され、alt_disk_mksysb 属性確認 Technology Level 0095 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0095B
画面・出力には AIX0095B が表示され、alt_disk_mksysb 属性確認 Technology Level 0095 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0095C
画面・出力には AIX0095C が表示され、alt_disk_mksysb 属性確認 Technology Level 0095 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0095A が画面・出力に表示されること
② ステップ2 の AIX0095B が画面・出力に表示されること
③ ステップ3 の AIX0095C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0710"><h3>alt_disk_mksysb 構成照合 EFIX LABEL 0382</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>紅葉記録ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。紅葉記録の導入と起動では EFIX LABEL とOSレベル表示を保守票へ記録します。紅葉記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。紅葉記録の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、紅葉記録を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_mksysb 構成照合 EFIX LABEL 0382に関する障害切り分けの前提を確認しています。smitty etherchannel 変更前確認 Destination 0383の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はネットワークでsmitty etherchannelを用い・Destinationである。smitty etherchannel 変更前確認固有の属性も確認対象に含める。</li><li>B. 表示や設定で扱う内容は導入と起動でalt_disk_mksysbを用い・EFIX LABEL とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はデバイス管理でcfgmgrを用い・location code と構成マネージャー結果を確認する。</li><li>D. 表示や設定で扱う内容はセキュリティでsetsecattrを用い・audit class とロール一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「導入と起動でalt_disk_mksysbを用い、EFIX LABEL」に対応する項目はEFIX LABEL（構成・alt_）です。構成に関する導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い、EFIX」で、確認対象はal・構成です。変更前・smitのA:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は変更前確認 Destination（変更・smit）です。性能・cfgmのC:は「デバイス管理でcfgmgrを用い、location code」を述べ、対象はlocation code（性能・cfgm）です。変更後・setsのD:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（変更・sets）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い、EFIX」を指し、EFIX LABELではal・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_mksysb 構成照合 EFIX LABEL 0382</strong></p><p>検証目的: 導入と起動のalt_disk_mksysb 構成照合 EFIX LABEL 0382について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合022-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0382A
画面・出力には AIX0382A が表示され、alt_disk_mksysb 構成照合 EFIX LABEL 0382 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0382B
画面・出力には AIX0382B が表示され、alt_disk_mksysb 構成照合 EFIX LABEL 0382 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0382C
画面・出力には AIX0382C が表示され、alt_disk_mksysb 構成照合 EFIX LABEL 0382 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0382A が画面・出力に表示されること
② ステップ2 の AIX0382B が画面・出力に表示されること
③ ステップ3 の AIX0382C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0711"><h3>alt_disk_mksysb 運用引継ぎ mksysb image 0412</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>水音評価ではAIX 7.3の導入と起動で alt_disk_mksysb を確認します。水音評価の導入と起動では mksysb image と代替ディスク状態を監査票へ転記します。水音評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。水音評価の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、水音評価を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> alt_disk_mksysb 運用引継ぎ mksysb image 0412の技術的な意味を資料で確認するとき、smitty etherchannel 容量確認 Link Status 0413との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はネットワークでsmitty etherchannelを用い・Link Status とMTU属性を確認する。</li><li>B. 管理対象との関係を表す説明はデバイス管理でcfgmgrを用い・path status とデバイス一覧を確認する。</li><li>C. 管理対象との関係を表す説明はセキュリティでsetsecattrを用い・audit class と監査設定を確認する。</li><li>D. 管理対象との関係を表す説明は導入と起動でalt_disk_mksysbを用い・mksysb image と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でalt_disk_mksysbを用い、mksysb image」に対応する項目はmksysb image（運用・alt_）です。運用引に関する導入と起動の仕様は「導入と起動でalt_disk_mksysbを用い、mksysb」で、確認対象はal・運用引です。容量・smitのA:は「ネットワークでsmitty etherchannelを用い」を述べ、対象はLink Status（容量・smit）です。変更後・cfgmのB:は「デバイス管理でcfgmgrを用い、path status」を述べ、対象はpath status（変更・cfgm）です。性能・setsのC:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（性能・sets）です。「alt_disk_mksysb」は「導入と起動でalt_disk_mksysbを用い、mksysb」を指し、mksysb imageではal・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alt_disk_mksysb 運用引継ぎ mksysb image 0412</strong></p><p>検証目的: 導入と起動のalt_disk_mksysb 運用引継ぎ mksysb image 0412について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ052-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; alt_disk_mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0412A
画面・出力には AIX0412A が表示され、alt_disk_mksysb 運用引継ぎ mksysb image 0412 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0412B
画面・出力には AIX0412B が表示され、alt_disk_mksysb 運用引継ぎ mksysb image 0412 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0412C
画面・出力には AIX0412C が表示され、alt_disk_mksysb 運用引継ぎ mksysb image 0412 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0412A が画面・出力に表示されること
② ステップ2 の AIX0412B が画面・出力に表示されること
③ ステップ3 の AIX0412C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0712"><h3>bootlist -m normal 変更前確認 EFIX LABEL 0276</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>若潮監査ではAIX 7.3の導入と起動で bootlist -m normal を確認します。若潮監査の導入と起動では EFIX LABEL と代替ディスク状態を同じ証跡に残します。若潮監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若潮監査の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、若潮監査を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootlist -m normal 変更前確認 EFIX LABEL 0276の技術的な意味を資料で確認するとき、cfgmgr 変更後確認 Destination 0277との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はネットワークでcfgmgrを用い・Destination とMTU属性を確認する。cfgmgr 変更後確認 Destination 0277固有の属性も確認対象に含める。</li><li>B. 構成を確認する際の意味はデバイス管理でdiag -d ent0を用い・location code とデバイス一覧を確認する。</li><li>C. 構成を確認する際の意味はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>D. 構成を確認する際の意味は導入と起動でbootlist -m normalを用い・EFIX LABEL と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でbootlist -m normalを用い、EFIX LABEL」に対応する項目はEFIX LABEL（変更・boot）です。変更前に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い、EFIX」で、確認対象はbo・変更前です。変更後・cfgmのA:は「ネットワークでcfgmgrを用い、Destination」を述べ、対象は変更後確認 Destination（変更・cfgm）です。起動・diagのB:は「デバイス管理でdiag -d ent0を用い、location」を述べ、対象はlocation code（起動・diag）です。障害切・vmstのC:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は障害切り分け 統計値（障害・vmst）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い、EFIX」を指し、EFIX LABELではbo・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootlist -m normal 変更前確認 EFIX LABEL 0276</strong></p><p>検証目的: 導入と起動のbootlist -m normal 変更前確認 EFIX LABEL 0276について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認036-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0276A
画面・出力には AIX0276A が表示され、bootlist -m normal 変更前確認 EFIX LABEL 0276 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0276B
画面・出力には AIX0276B が表示され、bootlist -m normal 変更前確認 EFIX LABEL 0276 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0276C
画面・出力には AIX0276C が表示され、bootlist -m normal 変更前確認 EFIX LABEL 0276 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0276A が画面・出力に表示されること
② ステップ2 の AIX0276B が画面・出力に表示されること
③ ステップ3 の AIX0276C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0713"><h3>bootlist -m normal 変更前確認 altinst_rootvg 0752</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>夕映監査ではAIX 7.3の導入と起動で bootlist -m normal を確認します。夕映監査の導入と起動では altinst_rootvg と代替ディスク状態を引継ぎ票へ保管します。夕映監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。夕映監査の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、夕映監査を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootlist -m normal 変更前確認 altinst_rootvg 0752を同一分類のcfgmgr 変更後確認 EtherChannel 0753と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途は導入と起動でbootlist -m normalを用い・altinst_rootvgである。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はネットワークでcfgmgrを用い・EtherChannel とMTU属性を確認する。</li><li>C. コマンドまたは機能の用途はJFS2でdefragfsを用い・lff とファイルシステム属性を確認する。</li><li>D. コマンドまたは機能の用途はセキュリティでpwdck -n ALLを用い・authorizations と監査設定を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でbootlist -m normalを用い」に対応する項目は変更前確認 altinst_root（変更・boot）です。変更前に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・変更前です。変更後・cfgmのB:は「ネットワークでcfgmgrを用い、EtherChannel」を述べ、対象は変更後確認 EtherChannel（変更・cfgm）です。運用引・defrのC:は「JFS2でdefragfsを用い、lff」を述べ、対象は運用引継ぎ lff（運用・defr）です。障害切・pwdcのD:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は障害切り分け authorizati（障害・pwdc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、変更前確認 altinst_rootではbo・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootlist -m normal 変更前確認 altinst_rootvg 0752</strong></p><p>検証目的: 導入と起動のbootlist -m normal 変更前確認 altinst_rootvg 0752について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認032-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0752A
画面・出力には AIX0752A が表示され、bootlist -m normal 変更前確認 altinst_rootvg 0752 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0752B
画面・出力には AIX0752B が表示され、bootlist -m normal 変更前確認 altinst_rootvg 0752 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0752C
画面・出力には AIX0752C が表示され、bootlist -m normal 変更前確認 altinst_rootvg 0752 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0752A が画面・出力に表示されること
② ステップ2 の AIX0752B が画面・出力に表示されること
③ ステップ3 の AIX0752C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0714"><h3>bootlist -m normal 容量確認 fileset level 0722</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>春分監査ではAIX 7.3の導入と起動で bootlist -m normal を確認します。春分監査の導入と起動では fileset level とOSレベル表示を確認票へ整理します。春分監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。春分監査の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、春分監査を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootlist -m normal 容量確認 fileset level 0722の役割を調べています。cfgmgr 性能確認 MTU 0723の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はネットワークでcfgmgrを用い・MTU とEthernet統計を確認する。</li><li>B. 障害切り分けに用いる役割は導入と起動でbootlist -m normalを用い・fileset levelである。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割はJFS2でlogformを用い・log=INLINE とログデバイス設定を確認する。</li><li>D. 障害切り分けに用いる役割はセキュリティでpwdck -n ALLを用い・authorizations とロール一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「導入と起動でbootlist -m normalを用い、fileset」に対応する項目はfileset level（容量・boot）です。容量に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・容量です。性能・cfgmのA:は「ネットワークでcfgmgrを用い、MTU」を述べ、対象は性能確認 MTU（性能・cfgm）です。状態・logfのC:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は状態確認 log=INLINE（状態・logf）です。起動・pwdcのD:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は起動確認 authorization（起動・pwdc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、fileset levelではbo・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootlist -m normal 容量確認 fileset level 0722</strong></p><p>検証目的: 導入と起動のbootlist -m normal 容量確認 fileset level 0722について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認002-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0722A
画面・出力には AIX0722A が表示され、bootlist -m normal 容量確認 fileset level 0722 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0722B
画面・出力には AIX0722B が表示され、bootlist -m normal 容量確認 fileset level 0722 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0722C
画面・出力には AIX0722C が表示され、bootlist -m normal 容量確認 fileset level 0722 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0722A が画面・出力に表示されること
② ステップ2 の AIX0722B が画面・出力に表示されること
③ ステップ3 の AIX0722C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0715"><h3>bootlist -m normal 容量確認 mksysb image 0246</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>朝凪監査ではAIX 7.3の導入と起動で bootlist -m normal を確認します。朝凪監査の導入と起動では mksysb image とOSレベル表示を変更票へ記録します。朝凪監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。朝凪監査の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、朝凪監査を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootlist -m normal 容量確認 mksysb image 0246に関する障害切り分けの前提を確認しています。cfgmgr 性能確認 Link Status 0247の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはネットワークでcfgmgrを用い・Link Status とEthernet統計を確認する。cfgmgr 性能確認 Link Status 0247固有の属性も確認対象に含める。</li><li>B. 機能の説明としてはデバイス管理でdiag -d ent0を用い・path status と構成マネージャー結果を確認する。</li><li>C. 機能の説明としてはCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>D. 機能の説明としては導入と起動でbootlist -m normalを用い・mksysb image とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「導入と起動でbootlist -m normalを用い、mksysb image」に対応する項目はmksysb image（容量・boot）です。容量に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・容量です。性能・cfgmのA:は「ネットワークでcfgmgrを用い、Link Status」を述べ、対象はLink Status（性能・cfgm）です。障害切・diagのB:は「デバイス管理でdiag -d ent0を用い、path」を述べ、対象はpath status（障害・diag）です。属性・イベ・vmstのC:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は属性照合 イベント転送（属性・vmst）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、mksysb imageではbo・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootlist -m normal 容量確認 mksysb image 0246</strong></p><p>検証目的: 導入と起動のbootlist -m normal 容量確認 mksysb image 0246について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認006-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0246A
画面・出力には AIX0246A が表示され、bootlist -m normal 容量確認 mksysb image 0246 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0246B
画面・出力には AIX0246B が表示され、bootlist -m normal 容量確認 mksysb image 0246 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0246C
画面・出力には AIX0246C が表示され、bootlist -m normal 容量確認 mksysb image 0246 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0246A が画面・出力に表示されること
② ステップ2 の AIX0246B が画面・出力に表示されること
③ ステップ3 の AIX0246C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0716"><h3>bootlist -m normal 状態確認 EFIX LABEL 0405</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>深雪評価ではAIX 7.3の導入と起動で bootlist -m normal を確認します。深雪評価の導入と起動では EFIX LABEL と起動デバイス設定を判定票へ残します。深雪評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。深雪評価の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、深雪評価を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootlist -m normal 状態確認 EFIX LABEL 0405を保守記録に説明する必要があります。cfgmgr 構成照合 MTU 0406と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はネットワークでcfgmgrを用い・MTU とアダプター一覧を確認する。cfgmgr 構成照合 MTU 0406固有の属性も確認対象に含める。</li><li>B. 運用時に利用する技術的役割はデバイス管理でdiag -d ent0を用い・location code とODM属性を確認する。</li><li>C. 運用時に利用する技術的役割は導入と起動でbootlist -m normalを用い・EFIX LABEL と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はセキュリティでpwdck -n ALLを用い・user attributes とRBAC属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でbootlist -m normalを用い、EFIX LABEL」に対応する項目はEFIX LABEL（状態・boot）です。状態に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い、EFIX」で、確認対象はbo・状態です。構成・cfgmのA:は「ネットワークでcfgmgrを用い、MTU とアダプター一覧を確認する」を述べ、対象は構成照合 MTU（構成・cfgm）です。容量・diagのB:は「デバイス管理でdiag -d ent0を用い、location」を述べ、対象はlocation code（容量・diag）です。変更前・pwdcのD:は「セキュリティでpwdck -n ALLを用い、user」を述べ、対象はuser attributes（変更・pwdc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い、EFIX」を指し、EFIX LABELではbo・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootlist -m normal 状態確認 EFIX LABEL 0405</strong></p><p>検証目的: 導入と起動のbootlist -m normal 状態確認 EFIX LABEL 0405について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認045-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0405A
画面・出力には AIX0405A が表示され、bootlist -m normal 状態確認 EFIX LABEL 0405 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0405B
画面・出力には AIX0405B が表示され、bootlist -m normal 状態確認 EFIX LABEL 0405 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0405C
画面・出力には AIX0405C が表示され、bootlist -m normal 状態確認 EFIX LABEL 0405 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0405A が画面・出力に表示されること
② ステップ2 の AIX0405B が画面・出力に表示されること
③ ステップ3 の AIX0405C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0717"><h3>bootlist -m normal 状態確認 EFIX LABEL 0465</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>花冷整理ではAIX 7.3の導入と起動で bootlist -m normal を確認します。花冷整理の導入と起動では EFIX LABEL と起動デバイス設定を判定票へ残します。花冷整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。花冷整理の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、花冷整理を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「bootlist -m normal 状態確認 EFIX LABEL 0465」を「cfgmgr 構成照合 MTU 0466」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はネットワークでcfgmgrを用い・MTU とアダプター一覧を確認する。</li><li>B. 運用時に利用する技術的役割はデバイス管理でrmdev -Rl ent1を用い・attribute とODM属性を確認する。rmdev -Rl ent1 性能確認 attribute 0771固有の属性も確認対象に含める。</li><li>C. 運用時に利用する技術的役割は導入と起動でbootlist -m normalを用い・EFIX LABEL と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はセキュリティでusrck -n ALLを用い・enhanced_RBAC とRBAC属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「導入と起動でbootlist -m normalを用い、EFIX LABEL」に対応する項目はEFIX LABEL（状態・boot）です。状態に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い、EFIX」で、確認対象はbo・状態です。構成・cfgmのA:は「ネットワークでcfgmgrを用い、MTU とアダプター一覧を確認する」を述べ、対象は構成照合 MTU（構成・cfgm）です。性能・rmdeのB:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は性能確認 attribute（性能・rmde）です。変更後・usrcのD:は「セキュリティでusrck -n ALLを用い」を述べ、対象は変更後確認 enhanced_RBA（変更・usrc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い、EFIX」を指し、EFIX LABELではbo・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootlist -m normal 状態確認 EFIX LABEL 0465</strong></p><p>検証目的: 導入と起動のbootlist -m normal 状態確認 EFIX LABEL 0465について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認105-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0465A
画面・出力には AIX0465A が表示され、bootlist -m normal 状態確認 EFIX LABEL 0465 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0465B
画面・出力には AIX0465B が表示され、bootlist -m normal 状態確認 EFIX LABEL 0465 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0465C
画面・出力には AIX0465C が表示され、bootlist -m normal 状態確認 EFIX LABEL 0465 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0465A が画面・出力に表示されること
② ステップ2 の AIX0465B が画面・出力に表示されること
③ ステップ3 の AIX0465C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0718"><h3>bootlist -m normal 監査記録 mksysb image 0435</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>青磁評価ではAIX 7.3の導入と起動で bootlist -m normal を確認します。青磁評価の導入と起動では mksysb image とfileset一覧を作業票へ保管します。青磁評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。青磁評価の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、青磁評価を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootlist -m normal 監査記録 mksysb image 0435について構成や状態を確認します。cfgmgr 運用引継ぎ EtherChannel 0436ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはネットワークでcfgmgrを用い・EtherChannel と経路表を確認する。</li><li>B. 状態を読み取るための働きはデバイス管理でrmdev -Rl ent1を用い・microcode level と診断対象表示を確認する。</li><li>C. 状態を読み取るための働きはセキュリティでusrck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。</li><li>D. 状態を読み取るための働きは導入と起動でbootlist -m normalを用い・mksysb imageである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でbootlist -m normalを用い、mksysb」に対応する項目はmksysb image（監査・boot）です。監査に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・監査です。運用引・cfgmのA:は「ネットワークでcfgmgrを用い、EtherChannel」を述べ、対象は運用引継ぎ EtherChannel（運用・cfgm）です。変更後・rmdeのB:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象はmicrocode level（変更・rmde）です。性能・usrcのC:は「セキュリティでusrck -n ALLを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・usrc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、mksysb imageではbo・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootlist -m normal 監査記録 mksysb image 0435</strong></p><p>検証目的: 導入と起動のbootlist -m normal 監査記録 mksysb image 0435について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録075-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0435A
画面・出力には AIX0435A が表示され、bootlist -m normal 監査記録 mksysb image 0435 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0435B
画面・出力には AIX0435B が表示され、bootlist -m normal 監査記録 mksysb image 0435 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0435C
画面・出力には AIX0435C が表示され、bootlist -m normal 監査記録 mksysb image 0435 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0435A が画面・出力に表示されること
② ステップ2 の AIX0435B が画面・出力に表示されること
③ ステップ3 の AIX0435C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0719"><h3>bootlist -m normal 起動確認 fileset level 0594</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>銀嶺点検ではAIX 7.3の導入と起動で bootlist -m normal を確認します。銀嶺点検の導入と起動では fileset level とOSレベル表示を変更票へ記録します。銀嶺点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。銀嶺点検の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、銀嶺点検を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootlist -m normal 起動確認 fileset level 0594の役割を調べています。cfgmgr 属性確認 MTU 0595の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはネットワークでcfgmgrを用い・MTU とEthernet統計を確認する。</li><li>B. 機能の説明としては導入と起動でbootlist -m normalを用い・fileset levelである。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としてはLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>D. 機能の説明としてはセキュリティでusrck -n ALLを用い・authorizations とロール一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「導入と起動でbootlist -m normalを用い、fileset」に対応する項目はfileset level（起動・boot）です。起動に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・起動です。属性・cfgmのA:は「ネットワークでcfgmgrを用い、MTU」を述べ、対象は属性確認 MTU（属性・cfgm）です。一覧・保存・lparのC:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は一覧確認 保存場所（一覧・lpar）です。構成・usrcのD:は「セキュリティでusrck -n ALLを用い」を述べ、対象は構成照合 authorization（構成・usrc）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、fileset levelではbo・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootlist -m normal 起動確認 fileset level 0594</strong></p><p>検証目的: 導入と起動のbootlist -m normal 起動確認 fileset level 0594について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認114-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0594A
画面・出力には AIX0594A が表示され、bootlist -m normal 起動確認 fileset level 0594 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0594B
画面・出力には AIX0594B が表示され、bootlist -m normal 起動確認 fileset level 0594 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0594C
画面・出力には AIX0594C が表示され、bootlist -m normal 起動確認 fileset level 0594 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0594A が画面・出力に表示されること
② ステップ2 の AIX0594B が画面・出力に表示されること
③ ステップ3 の AIX0594C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0720"><h3>bootlist -m normal 起動確認 mksysb image 0118</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>春霞点検ではAIX 7.3の導入と起動で bootlist -m normal を確認します。春霞点検の導入と起動では mksysb image とOSレベル表示を保守票へ記録します。春霞点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。春霞点検の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、春霞点検を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootlist -m normal 起動確認 mksysb image 0118に関する障害切り分けの前提を確認しています。cfgmgr 属性確認 Link Status 0119の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はネットワークでcfgmgrを用い・Link Status とEthernet統計を確認する。</li><li>B. 表示や設定で扱う内容は導入と起動でbootlist -m normalを用い・mksysb image とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はデバイス管理でrmdev -Rl ent1を用い・microcode levelである。rmdev -Rl ent1 運用引継ぎ microcode固有の属性も確認対象に含める。</li><li>D. 表示や設定で扱う内容はネットワークでno -aを用い・Link Status とEthernet統計を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「導入と起動でbootlist -m normalを用い、mksysb image」に対応する項目はmksysb image（起動・boot）です。起動に関する導入と起動の仕様は「導入と起動でbootlist -m normalを用い」で、確認対象はbo・起動です。属性・cfgmのA:は「ネットワークでcfgmgrを用い、Link Status」を述べ、対象はLink Status（属性・cfgm）です。運用引・rmdeのC:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象はmicrocode level（運用・rmde）です。バック・noのD:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（バッ・no）です。「bootlist -m normal」は「導入と起動でbootlist -m normalを用い」を指し、mksysb imageではbo・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootlist -m normal 起動確認 mksysb image 0118</strong></p><p>検証目的: 導入と起動のbootlist -m normal 起動確認 mksysb image 0118について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認118-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0118A
画面・出力には AIX0118A が表示され、bootlist -m normal 起動確認 mksysb image 0118 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0118B
画面・出力には AIX0118B が表示され、bootlist -m normal 起動確認 mksysb image 0118 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0118C
画面・出力には AIX0118C が表示され、bootlist -m normal 起動確認 mksysb image 0118 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0118A が画面・出力に表示されること
② ステップ2 の AIX0118B が画面・出力に表示されること
③ ステップ3 の AIX0118C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0721"><h3>bosboot -a -d 変更後確認 EFIX LABEL 0027</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>風花確認ではAIX 7.3の導入と起動で bosboot -a -d を確認します。風花確認の導入と起動では EFIX LABEL とfileset一覧を作業票へ保管します。風花確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。風花確認の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、風花確認を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bosboot -a -d 変更後確認 EFIX LABEL 0027について構成や状態を確認します。route -n get 障害切り分け MTU 0028ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはネットワークでroute -n getを用い・MTU と経路表を確認する。</li><li>B. 状態を読み取るための働きは導入と起動でbosboot -a -dを用い・EFIX LABEL とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはデバイス管理でlscfg -vl ent0を用い・location code と診断対象表示を確認する。</li><li>D. 状態を読み取るための働きはネットワークでnetstat -vを用い・Media Speed Running と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でbosboot -a -dを用い、EFIX LABEL」に対応する項目はEFIX LABEL（変更・bosb）です。導入と起動の仕様は「導入と起動でbosboot -a -dを用い、EFIX LABEL」で、確認対象はbo・変更後です。障害切・routのA:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は障害切り分け MTU（障害・rout）です。属性・lscfのC:は「デバイス管理でlscfg -vl ent0を用い、location」を述べ、対象はlocation code（属性・lscf）です。性能・netsのD:は「ネットワークでnetstat -vを用い、Media Speed」を述べ、対象はSpeed Running（性能・nets）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、EFIX LABEL」を指し、EFIX LABELではbo・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bosboot -a -d 変更後確認 EFIX LABEL 0027</strong></p><p>検証目的: 導入と起動のbosboot -a -d 変更後確認 EFIX LABEL 0027について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認027-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bosboot -a -d
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0027A
画面・出力には AIX0027A が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0027 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0027B
画面・出力には AIX0027B が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0027 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0027C
画面・出力には AIX0027C が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0027 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0027A が画面・出力に表示されること
② ステップ2 の AIX0027B が画面・出力に表示されること
③ ステップ3 の AIX0027C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0722"><h3>bosboot -a -d 変更後確認 EFIX LABEL 0087</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>夕凪点検ではAIX 7.3の導入と起動で bosboot -a -d を確認します。夕凪点検の導入と起動では EFIX LABEL とfileset一覧を作業票へ保管します。夕凪点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。夕凪点検の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、夕凪点検を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bosboot -a -d 変更後確認 EFIX LABEL 0087の設定や表示を読む前に役割を確認します。route -n get 障害切り分け MTU 0088ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはネットワークでroute -n getを用い・MTU と経路表を確認する。</li><li>B. 状態を読み取るための働きは導入と起動でbosboot -a -dを用い・EFIX LABEL とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはデバイス管理でdiag -d ent0を用い・attribute と診断対象表示を確認する。</li><li>D. 状態を読み取るための働きはネットワークでnetstat -vを用い・Media Speed Running と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でbosboot -a -dを用い、EFIX LABEL」に対応する項目はEFIX LABEL（変更・bosb）です。変更後に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い、EFIX LABEL」で、確認対象はbo・変更後です。障害切・routのA:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は障害切り分け MTU（障害・rout）です。状態・diagのC:は「デバイス管理でdiag -d ent0を用い、attribute」を述べ、対象は状態確認 attribute（状態・diag）です。性能・netsのD:は「ネットワークでnetstat -vを用い、Media Speed」を述べ、対象はSpeed Running（性能・nets）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、EFIX LABEL」を指し、EFIX LABELではbo・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bosboot -a -d 変更後確認 EFIX LABEL 0087</strong></p><p>検証目的: 導入と起動のbosboot -a -d 変更後確認 EFIX LABEL 0087について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認087-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bosboot -a -d
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0087A
画面・出力には AIX0087A が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0087 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0087B
画面・出力には AIX0087B が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0087 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0087C
画面・出力には AIX0087C が表示され、bosboot -a -d 変更後確認 EFIX LABEL 0087 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0087A が画面・出力に表示されること
② ステップ2 の AIX0087B が画面・出力に表示されること
③ ステップ3 の AIX0087C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0723"><h3>bosboot -a -d 変更後確認 altinst_rootvg 0503</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>新緑確認ではAIX 7.3の導入と起動で bosboot -a -d を確認します。新緑確認の導入と起動では altinst_rootvg とfileset一覧を照合票へ整理します。新緑確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。新緑確認の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、新緑確認を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bosboot -a -d 変更後確認 altinst_rootvg 0503の設定や表示を読む前に役割を確認します。route -n get 障害切り分け Gateway 0504ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的は導入と起動でbosboot -a -dを用い・altinst_rootvg とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的はネットワークでroute -n getを用い・Gateway と経路表を確認する。</li><li>C. 一次資料が示す主目的はデバイス管理でlscfg -vl ent0を用い・PVID と診断対象表示を確認する。lscfg -vl ent0 属性確認 PVID 0809固有の属性も確認対象に含める。</li><li>D. 一次資料が示す主目的はセキュリティでlsuserを用い・user attributes とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でbosboot -a -dを用い、altinst_rootvg」に対応する項目は変更後確認 altinst_root（変更・bosb）です。変更後に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い」で、確認対象はbo・変更後です。障害切・routのB:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・rout）です。属性・lscfのC:は「デバイス管理でlscfg -vl ent0を用い、PVID」を述べ、対象は属性確認 PVID（属性・lscf）です。バック・lsusのD:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（バッ・lsus）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い」を指し、変更後確認 altinst_rootではbo・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bosboot -a -d 変更後確認 altinst_rootvg 0503</strong></p><p>検証目的: 導入と起動のbosboot -a -d 変更後確認 altinst_rootvg 0503について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認023-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bosboot -a -d
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0503A
画面・出力には AIX0503A が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0503 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0503B
画面・出力には AIX0503B が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0503 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0503C
画面・出力には AIX0503C が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0503 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0503A が画面・出力に表示されること
② ステップ2 の AIX0503B が画面・出力に表示されること
③ ステップ3 の AIX0503C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0724"><h3>bosboot -a -d 変更後確認 altinst_rootvg 0563</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>秋声点検ではAIX 7.3の導入と起動で bosboot -a -d を確認します。秋声点検の導入と起動では altinst_rootvg とfileset一覧を照合票へ整理します。秋声点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。秋声点検の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、秋声点検を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bosboot -a -d 変更後確認 altinst_rootvg 0563について構成や状態を確認します。route -n get 障害切り分け Gateway 0564ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はネットワークでroute -n getを用い・Gateway と経路表を確認する。route -n get 障害切り分け Gateway 0564固有の属性も確認対象に含める。</li><li>B. 一次資料が示す主目的はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>C. 一次資料が示す主目的はセキュリティでpwdck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。</li><li>D. 一次資料が示す主目的は導入と起動でbosboot -a -dを用い・altinst_rootvg とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でbosboot -a -dを用い、altinst_rootvg」に対応する項目は変更後確認 altinst_root（変更・bosb）です。変更後に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い」で、確認対象はbo・変更後です。障害切・routのA:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・rout）です。変更前・vmstのB:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は変更前確認 性能値（変更・vmst）です。監査・pwdcのC:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・pwdc）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い」を指し、変更後確認 altinst_rootではbo・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bosboot -a -d 変更後確認 altinst_rootvg 0563</strong></p><p>検証目的: 導入と起動のbosboot -a -d 変更後確認 altinst_rootvg 0563について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認083-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bosboot -a -d
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0563A
画面・出力には AIX0563A が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0563 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0563B
画面・出力には AIX0563B が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0563 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0563C
画面・出力には AIX0563C が表示され、bosboot -a -d 変更後確認 altinst_rootvg 0563 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0563A が画面・出力に表示されること
② ステップ2 の AIX0563B が画面・出力に表示されること
③ ステップ3 の AIX0563C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0725"><h3>bosboot -a -d 性能確認 fileset level 0533</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>月影照合ではAIX 7.3の導入と起動で bosboot -a -d を確認します。月影照合の導入と起動では fileset level と起動デバイス設定を復旧票へ残します。月影照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。月影照合の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、月影照合を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bosboot -a -d 性能確認 fileset level 0533を保守記録に説明する必要があります。route -n get 起動確認 Media Speed Running 0534と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割は導入と起動でbosboot -a -dを用い・fileset level と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割はネットワークでroute -n getを用い・Media Speed Runningである。</li><li>C. 仕様上の役割はデバイス管理でlscfg -vl ent0を用い・Available とODM属性を確認する。lscfg -vl ent0 バックアウト確認 Available固有の属性も確認対象に含める。</li><li>D. 仕様上の役割はセキュリティでlsuserを用い・user attributes とRBAC属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でbosboot -a -dを用い、fileset level」に対応する項目はfileset level（性能・bosb）です。性能に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い、fileset」で、確認対象はbo・性能です。起動・routのB:は「ネットワークでroute -n getを用い、Media」を述べ、対象はSpeed Running（起動・rout）です。バック・lscfのC:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象はバックアウト確認 Available（バッ・lscf）です。属性・lsusのD:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（属性・lsus）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、fileset」を指し、fileset levelではbo・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bosboot -a -d 性能確認 fileset level 0533</strong></p><p>検証目的: 導入と起動のbosboot -a -d 性能確認 fileset level 0533について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認053-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bosboot -a -d
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0533A
画面・出力には AIX0533A が表示され、bosboot -a -d 性能確認 fileset level 0533 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0533B
画面・出力には AIX0533B が表示され、bosboot -a -d 性能確認 fileset level 0533 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0533C
画面・出力には AIX0533C が表示され、bosboot -a -d 性能確認 fileset level 0533 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0533A が画面・出力に表示されること
② ステップ2 の AIX0533B が画面・出力に表示されること
③ ステップ3 の AIX0533C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0726"><h3>bosboot -a -d 性能確認 mksysb image 0057</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>初霜照合ではAIX 7.3の導入と起動で bosboot -a -d を確認します。初霜照合の導入と起動では mksysb image と起動デバイス設定を判定票へ残します。初霜照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。初霜照合の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、初霜照合を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「bosboot -a -d 性能確認 mksysb image 0057」を「route -n get 起動確認 EtherChannel 0058」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割は導入と起動でbosboot -a -dを用い・mksysb image と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はネットワークでroute -n getを用い・EtherChannel とアダプター一覧を確認する。</li><li>C. 運用時に利用する技術的役割はデバイス管理でdiag -d ent0を用い・microcode level とODM属性を確認する。diag -d ent0 監査記録 microcode level固有の属性も確認対象に含める。</li><li>D. 運用時に利用する技術的役割はネットワークでnetstat -vを用い・Gateway とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でbosboot -a -dを用い、mksysb image」に対応する項目はmksysb image（性能・bosb）です。導入と起動の仕様は「導入と起動でbosboot -a -dを用い、mksysb image」で、確認対象はbo・性能です。起動・routのB:は「ネットワークでroute -n getを用い」を述べ、対象は起動確認 EtherChannel（起動・rout）です。監査・diagのC:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（監査・diag）です。変更後・netsのD:は「ネットワークでnetstat -vを用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・nets）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、mksysb」を指し、mksysb imageではbo・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bosboot -a -d 性能確認 mksysb image 0057</strong></p><p>検証目的: 導入と起動のbosboot -a -d 性能確認 mksysb image 0057について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認057-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bosboot -a -d
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0057A
画面・出力には AIX0057A が表示され、bosboot -a -d 性能確認 mksysb image 0057 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0057B
画面・出力には AIX0057B が表示され、bosboot -a -d 性能確認 mksysb image 0057 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0057C
画面・出力には AIX0057C が表示され、bosboot -a -d 性能確認 mksysb image 0057 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0057A が画面・出力に表示されること
② ステップ2 の AIX0057B が画面・出力に表示されること
③ ステップ3 の AIX0057C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0727"><h3>bosboot -a -d 構成照合 bootlist 0692</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>水音保守ではAIX 7.3の導入と起動で bosboot -a -d を確認します。水音保守の導入と起動では bootlist と代替ディスク状態を引継ぎ票へ保管します。水音保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。水音保守の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、水音保守を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bosboot -a -d 構成照合 bootlist 0692の技術的な意味を資料で確認するとき、route -n get 変更前確認 Gateway 0693との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はネットワークでroute -n getを用い・Gateway とMTU属性を確認する。</li><li>B. コマンドまたは機能の用途はJFS2でlogformを用い・mountguard とファイルシステム属性を確認する。</li><li>C. コマンドまたは機能の用途は導入と起動でbosboot -a -dを用い・bootlist と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はセキュリティでpwdck -n ALLを用い・authorizations と監査設定を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でbosboot -a -dを用い、bootlist」に対応する項目は構成照合 bootlist（構成・bosb）です。構成に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い、bootlist」で、確認対象はbo・構成です。変更前・routのA:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は変更前確認 Gateway（変更・rout）です。監査・logfのB:は「JFS2でlogformを用い、mountguard」を述べ、対象は監査記録 mountguard（監査・logf）です。障害切・pwdcのD:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は障害切り分け authorizati（障害・pwdc）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、bootlist」を指し、構成照合 bootlistではbo・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bosboot -a -d 構成照合 bootlist 0692</strong></p><p>検証目的: 導入と起動のbosboot -a -d 構成照合 bootlist 0692について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合092-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bosboot -a -d
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0692A
画面・出力には AIX0692A が表示され、bosboot -a -d 構成照合 bootlist 0692 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0692B
画面・出力には AIX0692B が表示され、bosboot -a -d 構成照合 bootlist 0692 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0692C
画面・出力には AIX0692C が表示され、bosboot -a -d 構成照合 bootlist 0692 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0692A が画面・出力に表示されること
② ステップ2 の AIX0692B が画面・出力に表示されること
③ ステップ3 の AIX0692C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0728"><h3>bosboot -a -d 構成照合 fileset level 0216</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>若竹保守ではAIX 7.3の導入と起動で bosboot -a -d を確認します。若竹保守の導入と起動では fileset level と代替ディスク状態を同じ証跡に残します。若竹保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若竹保守の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、若竹保守を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bosboot -a -d 構成照合 fileset level 0216を同一分類のroute -n get 変更前確認 MTU 0217と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は導入と起動でbosboot -a -dを用い・fileset level と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はネットワークでroute -n getを用い・MTU とMTU属性を確認する。</li><li>C. 構成を確認する際の意味はデバイス管理でdiag -d ent0を用い・location code とデバイス一覧を確認する。</li><li>D. 構成を確認する際の意味はネットワークでnetstat -vを用い・Media Speed Running とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でbosboot -a -dを用い、fileset level」に対応する項目はfileset level（構成・bosb）です。構成に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い、fileset」で、確認対象はbo・構成です。変更前・routのB:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は変更前確認 MTU（変更・rout）です。起動・diagのC:は「デバイス管理でdiag -d ent0を用い、location」を述べ、対象はlocation code（起動・diag）です。運用引・netsのD:は「ネットワークでnetstat -vを用い、Media Speed」を述べ、対象はSpeed Running（運用・nets）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、fileset」を指し、fileset levelではbo・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bosboot -a -d 構成照合 fileset level 0216</strong></p><p>検証目的: 導入と起動のbosboot -a -d 構成照合 fileset level 0216について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合096-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bosboot -a -d
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0216A
画面・出力には AIX0216A が表示され、bosboot -a -d 構成照合 fileset level 0216 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0216B
画面・出力には AIX0216B が表示され、bosboot -a -d 構成照合 fileset level 0216 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0216C
画面・出力には AIX0216C が表示され、bosboot -a -d 構成照合 fileset level 0216 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0216A が画面・出力に表示されること
② ステップ2 の AIX0216B が画面・出力に表示されること
③ ステップ3 の AIX0216C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0729"><h3>bosboot -a -d 運用引継ぎ Technology Level 0662</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>紅葉判定ではAIX 7.3の導入と起動で bosboot -a -d を確認します。紅葉判定の導入と起動では Technology Level とOSレベル表示を確認票へ整理します。紅葉判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。紅葉判定の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、紅葉判定を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bosboot -a -d 運用引継ぎ Technology Level 0662に関する障害切り分けの前提を確認しています。route -n get 容量確認 Media Speed Running 0663の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はネットワークでroute -n getを用い・Media Speed Runningである。route -n get 容量確認 Media Speed固有の属性も確認対象に含める。</li><li>B. 障害切り分けに用いる役割はJFS2でlogformを用い・log=INLINE とログデバイス設定を確認する。</li><li>C. 障害切り分けに用いる役割は導入と起動でbosboot -a -dを用い・Technology Level とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割はセキュリティでlsuserを用い・enhanced_RBAC とロール一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でbosboot -a -dを用い、Technology Level」に対応する項目はTechnology Level（運用・bosb）です。運用引に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い、Technology」で、確認対象はbo・運用引です。容量・routのA:は「ネットワークでroute -n getを用い、Media」を述べ、対象はSpeed Running（容量・rout）です。状態・logfのB:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は状態確認 log=INLINE（状態・logf）です。性能・lsusのD:は「セキュリティでlsuserを用い、enhanced_RBAC」を述べ、対象は性能確認 enhanced_RBAC（性能・lsus）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い、Technology」を指し、Technology Levelではbo・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bosboot -a -d 運用引継ぎ Technology Level 0662</strong></p><p>検証目的: 導入と起動のbosboot -a -d 運用引継ぎ Technology Level 0662について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ062-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bosboot -a -d
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0662A
画面・出力には AIX0662A が表示され、bosboot -a -d 運用引継ぎ Technology Level 0662 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0662B
画面・出力には AIX0662B が表示され、bosboot -a -d 運用引継ぎ Technology Level 0662 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0662C
画面・出力には AIX0662C が表示され、bosboot -a -d 運用引継ぎ Technology Level 0662 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0662A が画面・出力に表示されること
② ステップ2 の AIX0662B が画面・出力に表示されること
③ ステップ3 の AIX0662C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0730"><h3>bosboot -a -d 運用引継ぎ altinst_rootvg 0186</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>陽炎判定ではAIX 7.3の導入と起動で bosboot -a -d を確認します。陽炎判定の導入と起動では altinst_rootvg とOSレベル表示を変更票へ記録します。陽炎判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。陽炎判定の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、陽炎判定を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bosboot -a -d 運用引継ぎ altinst_rootvg 0186の役割を調べています。route -n get 容量確認 EtherChannel 0187の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としては導入と起動でbosboot -a -dを用い・altinst_rootvg とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 機能の説明としてはネットワークでroute -n getを用い・EtherChannel とEthernet統計を確認する。</li><li>C. 機能の説明としてはデバイス管理でdiag -d ent0を用い・path status と構成マネージャー結果を確認する。</li><li>D. 機能の説明としてはネットワークでnetstat -vを用い・Gateway とEthernet統計を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でbosboot -a -dを用い、altinst_rootvg」に対応する項目は運用引継ぎ altinst_root（運用・bosb）です。運用引に関する導入と起動の仕様は「導入と起動でbosboot -a -dを用い」で、確認対象はbo・運用引です。容量・routのB:は「ネットワークでroute -n getを用い」を述べ、対象は容量確認 EtherChannel（容量・rout）です。障害切・diagのC:は「デバイス管理でdiag -d ent0を用い、path」を述べ、対象はpath status（障害・diag）です。構成・netsのD:は「ネットワークでnetstat -vを用い、Gateway」を述べ、対象は構成照合 Gateway（構成・nets）です。「bosboot -a -d」は「導入と起動でbosboot -a -dを用い」を指し、運用引継ぎ altinst_rootではbo・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bosboot -a -d 運用引継ぎ altinst_rootvg 0186</strong></p><p>検証目的: 導入と起動のbosboot -a -d 運用引継ぎ altinst_rootvg 0186について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ066-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bosboot -a -d
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0186A
画面・出力には AIX0186A が表示され、bosboot -a -d 運用引継ぎ altinst_rootvg 0186 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0186B
画面・出力には AIX0186B が表示され、bosboot -a -d 運用引継ぎ altinst_rootvg 0186 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0186C
画面・出力には AIX0186C が表示され、bosboot -a -d 運用引継ぎ altinst_rootvg 0186 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0186A が画面・出力に表示されること
② ステップ2 の AIX0186B が画面・出力に表示されること
③ ステップ3 の AIX0186C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0731"><h3>emgr -l バックアウト確認 Technology Level 0767</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>夕凪復旧ではAIX 7.3の導入と起動で emgr -l を確認します。夕凪復旧の導入と起動では Technology Level とfileset一覧を照合票へ整理します。夕凪復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。夕凪復旧の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、夕凪復旧を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> emgr -l バックアウト確認 Technology Level 0767の設定や表示を読む前に役割を確認します。netstat -rn 監査記録 Link Status 0768ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はネットワークでnetstat -rnを用い・Link Status と経路表を確認する。</li><li>B. 一次資料が示す主目的はLVMでmklvを用い・PVID とミラーコピー状態を確認する。</li><li>C. 一次資料が示す主目的はセキュリティでrbacqry -u user1 -Tを用い・audit class とユーザー属性を確認する。</li><li>D. 一次資料が示す主目的は導入と起動でemgr -lを用い・Technology Level とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でemgr -lを用い、Technology Level」に対応する項目はTechnology Level（バッ・emgr）です。バックに関する導入と起動の仕様は「導入と起動でemgr -lを用い、Technology Level」で、確認対象はem・バックです。監査・netsのA:は「ネットワークでnetstat -rnを用い、Link Status」を述べ、対象はLink Status（監査・nets）です。起動・mklvのB:は「LVMでmklvを用い、PVID とミラーコピー状態を確認する」を述べ、対象は起動確認 PVID（起動・mklv）です。運用引・rbacのC:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（運用・rbac）です。「emgr -l」は「導入と起動でemgr -lを用い、Technology Level」を指し、Technology Levelではem・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>emgr -l バックアウト確認 Technology Level 0767</strong></p><p>検証目的: 導入と起動のemgr -l バックアウト確認 Technology Level 0767について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認047-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; emgr -l
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0767A
画面・出力には AIX0767A が表示され、emgr -l バックアウト確認 Technology Level 0767 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0767B
画面・出力には AIX0767B が表示され、emgr -l バックアウト確認 Technology Level 0767 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0767C
画面・出力には AIX0767C が表示され、emgr -l バックアウト確認 Technology Level 0767 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0767A が画面・出力に表示されること
② ステップ2 の AIX0767B が画面・出力に表示されること
③ ステップ3 の AIX0767C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0732"><h3>emgr -l バックアウト確認 altinst_rootvg 0291</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>松風復旧ではAIX 7.3の導入と起動で emgr -l を確認します。松風復旧の導入と起動では altinst_rootvg とfileset一覧を作業票へ保管します。松風復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。松風復旧の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、松風復旧を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> emgr -l バックアウト確認 altinst_rootvg 0291について構成や状態を確認します。netstat -rn 監査記録 Gateway 0292ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはネットワークでnetstat -rnを用い・Gateway と経路表を確認する。</li><li>B. 状態を読み取るための働きはデバイス管理でlsattr -El hdisk0を用い・PVID と診断対象表示を確認する。lsattr -El hdisk0 構成照合 PVID 0597固有の属性も確認対象に含める。</li><li>C. 状態を読み取るための働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>D. 状態を読み取るための働きは導入と起動でemgr -lを用い・altinst_rootvg とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でemgr -lを用い、altinst_rootvg」に対応する項目はバックアウト確認 altinst_r（バッ・emgr）です。バックに関する導入と起動の仕様は「導入と起動でemgr -lを用い、altinst_rootvg」で、確認対象はem・バックです。監査・netsのA:は「ネットワークでnetstat -rnを用い、Gateway」を述べ、対象は監査記録 Gateway（監査・nets）です。構成・lsatのB:は「デバイス管理でlsattr -El hdisk0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lsat）です。性能・停止・lspsのC:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は性能確認 停止確認（性能・lsps）です。「emgr -l」は「導入と起動でemgr -lを用い、altinst_rootvg」を指し、バックアウト確認 altinst_rではem・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>emgr -l バックアウト確認 altinst_rootvg 0291</strong></p><p>検証目的: 導入と起動のemgr -l バックアウト確認 altinst_rootvg 0291について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認051-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; emgr -l
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0291A
画面・出力には AIX0291A が表示され、emgr -l バックアウト確認 altinst_rootvg 0291 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0291B
画面・出力には AIX0291B が表示され、emgr -l バックアウト確認 altinst_rootvg 0291 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0291C
画面・出力には AIX0291C が表示され、emgr -l バックアウト確認 altinst_rootvg 0291 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0291A が画面・出力に表示されること
② ステップ2 の AIX0291B が画面・出力に表示されること
③ ステップ3 の AIX0291C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0733"><h3>emgr -l 変更後確認 bootlist 0420</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>薄明評価ではAIX 7.3の導入と起動で emgr -l を確認します。薄明評価の導入と起動では bootlist と代替ディスク状態を同じ証跡に残します。薄明評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。薄明評価の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、薄明評価を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> emgr -l 変更後確認 bootlist 0420の技術的な意味を資料で確認するとき、netstat -rn 障害切り分け Gateway 0421との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は導入と起動でemgr -lを用い・bootlist と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はネットワークでnetstat -rnを用い・Gateway とMTU属性を確認する。</li><li>C. 構成を確認する際の意味はデバイス管理でchdev -l hdisk0を用い・PVID とデバイス一覧を確認する。</li><li>D. 構成を確認する際の意味はセキュリティでrbacqry -u user1 -Tを用い・roles と監査設定を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でemgr -lを用い、bootlist と代替ディスク状態を確認する」に対応する項目は変更後確認 bootlist（変更・emgr）です。変更後に関する導入と起動の仕様は「導入と起動でemgr -lを用い、bootlist」で、確認対象はem・変更後です。障害切・netsのB:は「ネットワークでnetstat -rnを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・nets）です。状態・chdeのC:は「デバイス管理でchdev -l hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・chde）です。バック・rbacのD:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はバックアウト確認 roles（バッ・rbac）です。「emgr -l」は「導入と起動でemgr -lを用い、bootlist」を指し、変更後確認 bootlistではem・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>emgr -l 変更後確認 bootlist 0420</strong></p><p>検証目的: 導入と起動のemgr -l 変更後確認 bootlist 0420について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認060-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; emgr -l
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0420A
画面・出力には AIX0420A が表示され、emgr -l 変更後確認 bootlist 0420 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0420B
画面・出力には AIX0420B が表示され、emgr -l 変更後確認 bootlist 0420 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0420C
画面・出力には AIX0420C が表示され、emgr -l 変更後確認 bootlist 0420 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0420A が画面・出力に表示されること
② ステップ2 の AIX0420B が画面・出力に表示されること
③ ステップ3 の AIX0420C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0734"><h3>emgr -l 変更後確認 bootlist 0480</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>青葉確認ではAIX 7.3の導入と起動で emgr -l を確認します。青葉確認の導入と起動では bootlist と代替ディスク状態を同じ証跡に残します。青葉確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。青葉確認の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、青葉確認を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> emgr -l 変更後確認 bootlist 0480を同一分類のnetstat -v バックアウト確認 EtherChannel 0481と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は導入と起動でemgr -lを用い・bootlist と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はネットワークでnetstat -vを用い・EtherChannel とMTU属性を確認する。</li><li>C. 構成を確認する際の意味はデバイス管理でchdev -l hdisk0を用い・PVID とデバイス一覧を確認する。</li><li>D. 構成を確認する際の意味はセキュリティでlssecattr -cを用い・audit class と監査設定を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「導入と起動でemgr -lを用い、bootlist と代替ディスク状態を確認する」に対応する項目は変更後確認 bootlist（変更・emgr）です。変更後に関する導入と起動の仕様は「導入と起動でemgr -lを用い、bootlist」で、確認対象はem・変更後です。バック・netsのB:は「ネットワークでnetstat -vを用い、EtherChannel」を述べ、対象はバックアウト確認 EtherChan（バッ・nets）です。状態・chdeのC:は「デバイス管理でchdev -l hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・chde）です。監査・lsseのD:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（監査・lsse）です。「emgr -l」は「導入と起動でemgr -lを用い、bootlist」を指し、変更後確認 bootlistではem・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>emgr -l 変更後確認 bootlist 0480</strong></p><p>検証目的: 導入と起動のemgr -l 変更後確認 bootlist 0480について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認120-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; emgr -l
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0480A
画面・出力には AIX0480A が表示され、emgr -l 変更後確認 bootlist 0480 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0480B
画面・出力には AIX0480B が表示され、emgr -l 変更後確認 bootlist 0480 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0480C
画面・出力には AIX0480C が表示され、emgr -l 変更後確認 bootlist 0480 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0480A が画面・出力に表示されること
② ステップ2 の AIX0480B が画面・出力に表示されること
③ ステップ3 の AIX0480C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0735"><h3>emgr -l 属性確認 bootlist 0737</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>初霜監査ではAIX 7.3の導入と起動で emgr -l を確認します。初霜監査の導入と起動では bootlist と起動デバイス設定を復旧票へ残します。初霜監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。初霜監査の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、初霜監査を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「emgr -l 属性確認 bootlist 0737」を「netstat -rn 状態確認 Destination 0738」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はネットワークでnetstat -rnを用い・Destination とアダプター一覧を確認する。</li><li>B. 仕様上の役割はJFS2でfsckを用い・mountguard と内部スナップショットを確認する。</li><li>C. 仕様上の役割はセキュリティでrbacqry -u user1 -Tを用い・audit class とRBAC属性を確認する。</li><li>D. 仕様上の役割は導入と起動でemgr -lを用い・bootlist と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「導入と起動でemgr -lを用い、bootlist と起動デバイス設定を確認する」に対応する項目は属性確認 bootlist（属性・emgr）です。属性に関する導入と起動の仕様は「導入と起動でemgr -lを用い、bootlist」で、確認対象はem・属性です。状態・netsのA:は「ネットワークでnetstat -rnを用い、Destination」を述べ、対象は状態確認 Destination（状態・nets）です。障害切・fsckのB:は「JFS2でfsckを用い、mountguard」を述べ、対象は障害切り分け mountguard（障害・fsck）です。構成・rbacのC:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（構成・rbac）です。「emgr -l」は「導入と起動でemgr -lを用い、bootlist」を指し、属性確認 bootlistではem・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>emgr -l 属性確認 bootlist 0737</strong></p><p>検証目的: 導入と起動のemgr -l 属性確認 bootlist 0737について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認017-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; emgr -l
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0737A
画面・出力には AIX0737A が表示され、emgr -l 属性確認 bootlist 0737 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0737B
画面・出力には AIX0737B が表示され、emgr -l 属性確認 bootlist 0737 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0737C
画面・出力には AIX0737C が表示され、emgr -l 属性確認 bootlist 0737 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0737A が画面・出力に表示されること
② ステップ2 の AIX0737B が画面・出力に表示されること
③ ステップ3 の AIX0737C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0736"><h3>emgr -l 属性確認 fileset level 0261</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>群青監査ではAIX 7.3の導入と起動で emgr -l を確認します。群青監査の導入と起動では fileset level と起動デバイス設定を判定票へ残します。群青監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。群青監査の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、群青監査を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> emgr -l 属性確認 fileset level 0261を保守記録に説明する必要があります。netstat -rn 状態確認 Media Speed Running 0262と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はネットワークでnetstat -rnを用い・Media Speed Runningである。</li><li>B. 運用時に利用する技術的役割は導入と起動でemgr -lを用い・fileset level と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はデバイス管理でlsattr -El hdisk0を用い・Available とODM属性を確認する。</li><li>D. 運用時に利用する技術的役割はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「導入と起動でemgr -lを用い、fileset level」に対応する項目はfileset level（属性・emgr）です。属性に関する導入と起動の仕様は「導入と起動でemgr -lを用い、fileset level」で、確認対象はem・属性です。状態・netsのA:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（状態・nets）です。運用引・lsatのC:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は運用引継ぎ Available（運用・lsat）です。障害切・lspsのD:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は障害切り分け ファイルセット（障害・lsps）です。「emgr -l」は「導入と起動でemgr -lを用い、fileset level」を指し、fileset levelではem・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>emgr -l 属性確認 fileset level 0261</strong></p><p>検証目的: 導入と起動のemgr -l 属性確認 fileset level 0261について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認021-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; emgr -l
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0261A
画面・出力には AIX0261A が表示され、emgr -l 属性確認 fileset level 0261 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0261B
画面・出力には AIX0261B が表示され、emgr -l 属性確認 fileset level 0261 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0261C
画面・出力には AIX0261C が表示され、emgr -l 属性確認 fileset level 0261 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0261A が画面・出力に表示されること
② ステップ2 の AIX0261B が画面・出力に表示されること
③ ステップ3 の AIX0261C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0737"><h3>emgr -l 性能確認 Technology Level 0390</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>早苗記録ではAIX 7.3の導入と起動で emgr -l を確認します。早苗記録の導入と起動では Technology Level とOSレベル表示を変更票へ記録します。早苗記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。早苗記録の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、早苗記録を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> emgr -l 性能確認 Technology Level 0390に関する障害切り分けの前提を確認しています。netstat -rn 起動確認 Media Speed Running 0391の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはネットワークでnetstat -rnを用い・Media Speed Runningである。</li><li>B. 機能の説明としてはデバイス管理でlsattr -El hdisk0を用い・microcode levelである。</li><li>C. 機能の説明としてはセキュリティでrbacqry -u user1 -Tを用い・roles とロール一覧を確認する。</li><li>D. 機能の説明としては導入と起動でemgr -lを用い・Technology Level とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でemgr -lを用い、Technology Level」に対応する項目はTechnology Level（性能・emgr）です。性能に関する導入と起動の仕様は「導入と起動でemgr -lを用い、Technology Level」で、確認対象はem・性能です。起動・netsのA:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（起動・nets）です。バック・lsatのB:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象はmicrocode level（バッ・lsat）です。属性・rbacのC:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象は属性確認 roles（属性・rbac）です。「emgr -l」は「導入と起動でemgr -lを用い、Technology Level」を指し、Technology Levelではem・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>emgr -l 性能確認 Technology Level 0390</strong></p><p>検証目的: 導入と起動のemgr -l 性能確認 Technology Level 0390について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認030-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; emgr -l
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0390A
画面・出力には AIX0390A が表示され、emgr -l 性能確認 Technology Level 0390 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0390B
画面・出力には AIX0390B が表示され、emgr -l 性能確認 Technology Level 0390 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0390C
画面・出力には AIX0390C が表示され、emgr -l 性能確認 Technology Level 0390 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0390A が画面・出力に表示されること
② ステップ2 の AIX0390B が画面・出力に表示されること
③ ステップ3 の AIX0390C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0738"><h3>emgr -l 性能確認 Technology Level 0450</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>桜雲整理ではAIX 7.3の導入と起動で emgr -l を確認します。桜雲整理の導入と起動では Technology Level とOSレベル表示を変更票へ記録します。桜雲整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。桜雲整理の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、桜雲整理を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> emgr -l 性能確認 Technology Level 0450の役割を調べています。netstat -rn 起動確認 Media Speed Running 0451の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはネットワークでnetstat -rnを用い・Media Speed Runningである。</li><li>B. 機能の説明としては導入と起動でemgr -lを用い・Technology Level とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としてはデバイス管理でchdev -l hdisk0を用い・Available と構成マネージャー結果を確認する。</li><li>D. 機能の説明としてはセキュリティでlssecattr -cを用い・audit class とロール一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でemgr -lを用い、Technology Level」に対応する項目はTechnology Level（性能・emgr）です。性能に関する導入と起動の仕様は「導入と起動でemgr -lを用い、Technology Level」で、確認対象はem・性能です。起動・netsのA:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（起動・nets）です。監査・chdeのC:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象は監査記録 Available（監査・chde）です。状態・lsseのD:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（状態・lsse）です。「emgr -l」は「導入と起動でemgr -lを用い、Technology Level」を指し、Technology Levelではem・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>emgr -l 性能確認 Technology Level 0450</strong></p><p>検証目的: 導入と起動のemgr -l 性能確認 Technology Level 0450について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認090-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; emgr -l
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0450A
画面・出力には AIX0450A が表示され、emgr -l 性能確認 Technology Level 0450 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0450B
画面・出力には AIX0450B が表示され、emgr -l 性能確認 Technology Level 0450 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0450C
画面・出力には AIX0450C が表示され、emgr -l 性能確認 Technology Level 0450 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0450A が画面・出力に表示されること
② ステップ2 の AIX0450B が画面・出力に表示されること
③ ステップ3 の AIX0450C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0739"><h3>installp -C 状態確認 EFIX LABEL 0488</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>翠風確認ではAIX 7.3の導入と起動で installp -C を確認します。翠風確認の導入と起動では EFIX LABEL と代替ディスク状態を引継ぎ票へ保管します。翠風確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。翠風確認の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、翠風確認を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> installp -C 状態確認 EFIX LABEL 0488を同一分類のentstat -d ent0 構成照合 Destination 0489と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はネットワークでentstat -d ent0を用い・Destination とMTU属性を確認する。</li><li>B. コマンドまたは機能の用途はデバイス管理でlsdev -Cc diskを用い・location code とデバイス一覧を確認する。</li><li>C. コマンドまたは機能の用途はセキュリティでrolelist -u user1を用い・roles と監査設定を確認する。</li><li>D. コマンドまたは機能の用途は導入と起動でinstallp -Cを用い・EFIX LABEL と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「導入と起動でinstallp -Cを用い、EFIX LABEL」に対応する項目はEFIX LABEL（状態・inst）です。状態に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、EFIX LABEL」で、確認対象はin・状態です。構成・entsのA:は「ネットワークでentstat -d ent0を用い」を述べ、対象は構成照合 Destination（構成・ents）です。容量・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い、location」を述べ、対象はlocation code（容量・lsde）です。変更前・roleのC:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は変更前確認 roles（変更・role）です。「installp -C」は「導入と起動でinstallp -Cを用い、EFIX LABEL」を指し、EFIX LABELではin・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>installp -C 状態確認 EFIX LABEL 0488</strong></p><p>検証目的: 導入と起動のinstallp -C 状態確認 EFIX LABEL 0488について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認008-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; installp -C
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0488A
画面・出力には AIX0488A が表示され、installp -C 状態確認 EFIX LABEL 0488 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0488B
画面・出力には AIX0488B が表示され、installp -C 状態確認 EFIX LABEL 0488 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0488C
画面・出力には AIX0488C が表示され、installp -C 状態確認 EFIX LABEL 0488 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0488A が画面・出力に表示されること
② ステップ2 の AIX0488B が画面・出力に表示されること
③ ステップ3 の AIX0488C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0740"><h3>installp -C 状態確認 EFIX LABEL 0548</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>雪解照合ではAIX 7.3の導入と起動で installp -C を確認します。雪解照合の導入と起動では EFIX LABEL と代替ディスク状態を引継ぎ票へ保管します。雪解照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。雪解照合の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、雪解照合を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> installp -C 状態確認 EFIX LABEL 0548の技術的な意味を資料で確認するとき、entstat -d ent0 構成照合 Destination 0549との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はネットワークでentstat -d ent0を用い・Destination とMTU属性を確認する。</li><li>B. コマンドまたは機能の用途はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>C. コマンドまたは機能の用途は導入と起動でinstallp -Cを用い・EFIX LABEL と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はセキュリティでrbacqry -u user1 -Tを用い・audit class と監査設定を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でinstallp -Cを用い、EFIX LABEL」に対応する項目はEFIX LABEL（状態・inst）です。状態に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、EFIX LABEL」で、確認対象はin・状態です。構成・entsのA:は「ネットワークでentstat -d ent0を用い」を述べ、対象は構成照合 Destination（構成・ents）です。変更前・lspsのB:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は変更前確認 停止確認（変更・lsps）です。変更後・rbacのD:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（変更・rbac）です。「installp -C」は「導入と起動でinstallp -Cを用い、EFIX LABEL」を指し、EFIX LABELではin・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>installp -C 状態確認 EFIX LABEL 0548</strong></p><p>検証目的: 導入と起動のinstallp -C 状態確認 EFIX LABEL 0548について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認068-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; installp -C
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0548A
画面・出力には AIX0548A が表示され、installp -C 状態確認 EFIX LABEL 0548 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0548B
画面・出力には AIX0548B が表示され、installp -C 状態確認 EFIX LABEL 0548 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0548C
画面・出力には AIX0548C が表示され、installp -C 状態確認 EFIX LABEL 0548 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0548A が画面・出力に表示されること
② ステップ2 の AIX0548B が画面・出力に表示されること
③ ステップ3 の AIX0548C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0741"><h3>installp -C 状態確認 Technology Level 0012</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>水音確認ではAIX 7.3の導入と起動で installp -C を確認します。水音確認の導入と起動では Technology Level と代替ディスク状態を同じ証跡に残します。水音確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。水音確認の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、水音確認を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> installp -C 状態確認 Technology Level 0012の技術的な意味を資料で確認するとき、entstat -d ent0 構成照合 Media Speed Runningとの境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は導入と起動でinstallp -Cを用い・Technology Level と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はネットワークでentstat -d ent0を用い・Media Speed Runningである。</li><li>C. 構成を確認する際の意味はデバイス管理でlsdev -Cc diskを用い・microcode level とデバイス一覧を確認する。</li><li>D. 構成を確認する際の意味はネットワークでlsdev -Cc adapterを用い・Link Status とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「導入と起動でinstallp -Cを用い、Technology Level」に対応する項目はTechnology Level（状態・inst）です。導入と起動の仕様は「導入と起動でinstallp -Cを用い、Technology」で、確認対象はin・状態です。構成・entsのB:は「ネットワークでentstat -d ent0を用い、Media」を述べ、対象はSpeed Running（構成・ents）です。容量・lsdeのC:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象はmicrocode level（容量・lsde）です。監査・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い、Link」を述べ、対象はLink Status（監査・lsde）です。「installp -C」は「導入と起動でinstallp -Cを用い、Technology」を指し、Technology Levelではin・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>installp -C 状態確認 Technology Level 0012</strong></p><p>検証目的: 導入と起動のinstallp -C 状態確認 Technology Level 0012について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認012-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; installp -C
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0012A
画面・出力には AIX0012A が表示され、installp -C 状態確認 Technology Level 0012 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0012B
画面・出力には AIX0012B が表示され、installp -C 状態確認 Technology Level 0012 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0012C
画面・出力には AIX0012C が表示され、installp -C 状態確認 Technology Level 0012 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0012A が画面・出力に表示されること
② ステップ2 の AIX0012B が画面・出力に表示されること
③ ステップ3 の AIX0012C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0742"><h3>installp -C 状態確認 Technology Level 0072</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>夕映照合ではAIX 7.3の導入と起動で installp -C を確認します。夕映照合の導入と起動では Technology Level と代替ディスク状態を同じ証跡に残します。夕映照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。夕映照合の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、夕映照合を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> installp -C 状態確認 Technology Level 0072を同一分類のentstat -d ent0 構成照合 Media Speed Runningと比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はネットワークでentstat -d ent0を用い・Media Speed Runningである。</li><li>B. 構成を確認する際の意味は導入と起動でinstallp -Cを用い・Technology Level と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はデバイス管理でlsattr -El hdisk0を用い・Available とデバイス一覧を確認する。</li><li>D. 構成を確認する際の意味はネットワークでlsdev -Cc adapterを用い・Link Status とMTU属性を確認する。lsdev -Cc adapter 監査記録 Link Status固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でinstallp -Cを用い、Technology Level」に対応する項目はTechnology Level（状態・inst）です。状態に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、Technology」で、確認対象はin・状態です。構成・entsのA:は「ネットワークでentstat -d ent0を用い、Media」を述べ、対象はSpeed Running（構成・ents）です。性能・lsatのC:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は性能確認 Available（性能・lsat）です。監査・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い、Link」を述べ、対象はLink Status（監査・lsde）です。「installp -C」は「導入と起動でinstallp -Cを用い、Technology」を指し、Technology Levelではin・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>installp -C 状態確認 Technology Level 0072</strong></p><p>検証目的: 導入と起動のinstallp -C 状態確認 Technology Level 0072について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認072-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; installp -C
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0072A
画面・出力には AIX0072A が表示され、installp -C 状態確認 Technology Level 0072 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0072B
画面・出力には AIX0072B が表示され、installp -C 状態確認 Technology Level 0072 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0072C
画面・出力には AIX0072C が表示され、installp -C 状態確認 Technology Level 0072 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0072A が画面・出力に表示されること
② ステップ2 の AIX0072B が画面・出力に表示されること
③ ステップ3 の AIX0072C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0743"><h3>installp -C 監査記録 bootlist 0042</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>春分照合ではAIX 7.3の導入と起動で installp -C を確認します。春分照合の導入と起動では bootlist とOSレベル表示を変更票へ記録します。春分照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。春分照合の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、春分照合を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> installp -C 監査記録 bootlist 0042の役割を調べています。entstat -d ent0 運用引継ぎ Gateway 0043の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはネットワークでentstat -d ent0を用い・Gateway とEthernet統計を確認する。</li><li>B. 機能の説明としては導入と起動でinstallp -Cを用い・bootlist とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としてはデバイス管理でlsdev -Cc diskを用い・attribute と構成マネージャー結果を確認する。</li><li>D. 機能の説明としてはネットワークでlsdev -Cc adapterを用い・Destinationである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でinstallp -Cを用い、bootlist」に対応する項目は監査記録 bootlist（監査・inst）です。導入と起動の仕様は「導入と起動でinstallp -Cを用い、bootlist」で、確認対象はin・監査です。運用引・entsのA:は「ネットワークでentstat -d ent0を用い、Gateway」を述べ、対象は運用引継ぎ Gateway（運用・ents）です。変更前・lsdeのC:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は変更前確認 attribute（変更・lsde）です。状態・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は状態確認 Destination（状態・lsde）です。「installp -C」は「導入と起動でinstallp -Cを用い、bootlist」を指し、監査記録 bootlistではin・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>installp -C 監査記録 bootlist 0042</strong></p><p>検証目的: 導入と起動のinstallp -C 監査記録 bootlist 0042について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録042-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; installp -C
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0042A
画面・出力には AIX0042A が表示され、installp -C 監査記録 bootlist 0042 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0042B
画面・出力には AIX0042B が表示され、installp -C 監査記録 bootlist 0042 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0042C
画面・出力には AIX0042C が表示され、installp -C 監査記録 bootlist 0042 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0042A が画面・出力に表示されること
② ステップ2 の AIX0042B が画面・出力に表示されること
③ ステップ3 の AIX0042C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0744"><h3>installp -C 監査記録 mksysb image 0518</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>春霞確認ではAIX 7.3の導入と起動で installp -C を確認します。春霞確認の導入と起動では mksysb image とOSレベル表示を確認票へ整理します。春霞確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。春霞確認の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、春霞確認を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> installp -C 監査記録 mksysb image 0518に関する障害切り分けの前提を確認しています。entstat -d ent0 運用引継ぎ Link Status 0519の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はネットワークでentstat -d ent0を用い・Link Status とEthernet統計を確認する。</li><li>B. 障害切り分けに用いる役割はデバイス管理でlsdev -Cc diskを用い・path status と構成マネージャー結果を確認する。</li><li>C. 障害切り分けに用いる役割は導入と起動でinstallp -Cを用い・mksysb image とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割はセキュリティでrolelist -u user1を用い・roles とロール一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でinstallp -Cを用い、mksysb image」に対応する項目はmksysb image（監査・inst）です。監査に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、mksysb image」で、確認対象はin・監査です。運用引・entsのA:は「ネットワークでentstat -d ent0を用い、Link」を述べ、対象はLink Status（運用・ents）です。変更前・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い、path」を述べ、対象はpath status（変更・lsde）です。容量・roleのD:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は容量確認 roles（容量・role）です。「installp -C」は「導入と起動でinstallp -Cを用い、mksysb image」を指し、mksysb imageではin・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>installp -C 監査記録 mksysb image 0518</strong></p><p>検証目的: 導入と起動のinstallp -C 監査記録 mksysb image 0518について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録038-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; installp -C
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0518A
画面・出力には AIX0518A が表示され、installp -C 監査記録 mksysb image 0518 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0518B
画面・出力には AIX0518B が表示され、installp -C 監査記録 mksysb image 0518 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0518C
画面・出力には AIX0518C が表示され、installp -C 監査記録 mksysb image 0518 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0518A が画面・出力に表示されること
② ステップ2 の AIX0518B が画面・出力に表示されること
③ ステップ3 の AIX0518C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0745"><h3>installp -C 起動確認 EFIX LABEL 0677</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>冬晴判定ではAIX 7.3の導入と起動で installp -C を確認します。冬晴判定の導入と起動では EFIX LABEL と起動デバイス設定を復旧票へ残します。冬晴判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。冬晴判定の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、冬晴判定を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> installp -C 起動確認 EFIX LABEL 0677を保守記録に説明する必要があります。entstat -d ent0 属性確認 MTU 0678と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はネットワークでentstat -d ent0を用い・MTU とアダプター一覧を確認する。</li><li>B. 仕様上の役割は導入と起動でinstallp -Cを用い・EFIX LABEL と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割はJFS2でmount -o remountを用い・isnapshot と内部スナップショットを確認する。</li><li>D. 仕様上の役割はセキュリティでrbacqry -u user1 -Tを用い・audit class とRBAC属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でinstallp -Cを用い、EFIX LABEL」に対応する項目はEFIX LABEL（起動・inst）です。起動に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、EFIX LABEL」で、確認対象はin・起動です。属性・entsのA:は「ネットワークでentstat -d ent0を用い、MTU」を述べ、対象は属性確認 MTU（属性・ents）です。変更後・mounのC:は「JFS2でmount -o remountを用い」を述べ、対象は変更後確認 isnapshot（変更・moun）です。構成・rbacのD:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（構成・rbac）です。「installp -C」は「導入と起動でinstallp -Cを用い、EFIX LABEL」を指し、EFIX LABELではin・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>installp -C 起動確認 EFIX LABEL 0677</strong></p><p>検証目的: 導入と起動のinstallp -C 起動確認 EFIX LABEL 0677について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認077-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; installp -C
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0677A
画面・出力には AIX0677A が表示され、installp -C 起動確認 EFIX LABEL 0677 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0677B
画面・出力には AIX0677B が表示され、installp -C 起動確認 EFIX LABEL 0677 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0677C
画面・出力には AIX0677C が表示され、installp -C 起動確認 EFIX LABEL 0677 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0677A が画面・出力に表示されること
② ステップ2 の AIX0677B が画面・出力に表示されること
③ ステップ3 の AIX0677C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0746"><h3>installp -C 起動確認 Technology Level 0201</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>白露保守ではAIX 7.3の導入と起動で installp -C を確認します。白露保守の導入と起動では Technology Level と起動デバイス設定を判定票へ残します。白露保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。白露保守の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、白露保守を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「installp -C 起動確認 Technology Level 0201」を「entstat -d ent0 属性確認 Link Status 0202」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はネットワークでentstat -d ent0を用い・Link Status とアダプター一覧を確認する。</li><li>B. 運用時に利用する技術的役割はデバイス管理でlsattr -El hdisk0を用い・Available とODM属性を確認する。</li><li>C. 運用時に利用する技術的役割は導入と起動でinstallp -Cを用い・Technology Level と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はネットワークでlsdev -Cc adapterを用い・EtherChannel とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でinstallp -Cを用い、Technology Level」に対応する項目はTechnology Level（起動・inst）です。起動に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、Technology」で、確認対象はin・起動です。属性・entsのA:は「ネットワークでentstat -d ent0を用い、Link」を述べ、対象はLink Status（属性・ents）です。運用引・lsatのB:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は運用引継ぎ Available（運用・lsat）です。障害切・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は障害切り分け EtherChanne（障害・lsde）です。「installp -C」は「導入と起動でinstallp -Cを用い、Technology」を指し、Technology Levelではin・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>installp -C 起動確認 Technology Level 0201</strong></p><p>検証目的: 導入と起動のinstallp -C 起動確認 Technology Level 0201について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認081-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; installp -C
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0201A
画面・出力には AIX0201A が表示され、installp -C 起動確認 Technology Level 0201 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0201B
画面・出力には AIX0201B が表示され、installp -C 起動確認 Technology Level 0201 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0201C
画面・出力には AIX0201C が表示され、installp -C 起動確認 Technology Level 0201 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0201A が画面・出力に表示されること
② ステップ2 の AIX0201B が画面・出力に表示されること
③ ステップ3 の AIX0201C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0747"><h3>installp -C 障害切り分け bootlist 0231</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>遠雷保守ではAIX 7.3の導入と起動で installp -C を確認します。遠雷保守の導入と起動では bootlist とfileset一覧を作業票へ保管します。遠雷保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。遠雷保守の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、遠雷保守を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> installp -C 障害切り分け bootlist 0231の設定や表示を読む前に役割を確認します。entstat -d ent0 バックアウト確認 Destination 0232ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはネットワークでentstat -d ent0を用い・Destination と経路表を確認する。</li><li>B. 状態を読み取るための働きはデバイス管理でlsattr -El hdisk0を用い・PVID と診断対象表示を確認する。</li><li>C. 状態を読み取るための働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>D. 状態を読み取るための働きは導入と起動でinstallp -Cを用い・bootlist とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「導入と起動でinstallp -Cを用い、bootlist」に対応する項目は障害切り分け bootlist（障害・inst）です。障害切に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、bootlist」で、確認対象はin・障害切です。バック・entsのA:は「ネットワークでentstat -d ent0を用い」を述べ、対象はバックアウト確認 Destinati（バッ・ents）です。構成・lsatのB:は「デバイス管理でlsattr -El hdisk0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lsat）です。属性・属性・lspsのC:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は属性照合 属性確認（属性・lsps）です。「installp -C」は「導入と起動でinstallp -Cを用い、bootlist」を指し、障害切り分け bootlistではin・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>installp -C 障害切り分け bootlist 0231</strong></p><p>検証目的: 導入と起動のinstallp -C 障害切り分け bootlist 0231について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け111-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; installp -C
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0231A
画面・出力には AIX0231A が表示され、installp -C 障害切り分け bootlist 0231 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0231B
画面・出力には AIX0231B が表示され、installp -C 障害切り分け bootlist 0231 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0231C
画面・出力には AIX0231C が表示され、installp -C 障害切り分け bootlist 0231 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0231A が画面・出力に表示されること
② ステップ2 の AIX0231B が画面・出力に表示されること
③ ステップ3 の AIX0231C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0748"><h3>installp -C 障害切り分け mksysb image 0707</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>風花保守ではAIX 7.3の導入と起動で installp -C を確認します。風花保守の導入と起動では mksysb image とfileset一覧を照合票へ整理します。風花保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。風花保守の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、風花保守を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> installp -C 障害切り分け mksysb image 0707について構成や状態を確認します。entstat -d ent0 バックアウト確認 EtherChannel 0708ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はネットワークでentstat -d ent0を用い・EtherChannel と経路表を確認する。</li><li>B. 一次資料が示す主目的はJFS2でmount -o remountを用い・ファイルシステム使用率 とマウントオプションを確認する。</li><li>C. 一次資料が示す主目的は導入と起動でinstallp -Cを用い・mksysb image とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はセキュリティでrbacqry -u user1 -Tを用い・audit class とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「導入と起動でinstallp -Cを用い、mksysb image」に対応する項目はmksysb image（障害・inst）です。障害切に関する導入と起動の仕様は「導入と起動でinstallp -Cを用い、mksysb image」で、確認対象はin・障害切です。バック・entsのA:は「ネットワークでentstat -d ent0を用い」を述べ、対象はバックアウト確認 EtherChan（バッ・ents）です。性能・ファ・mounのB:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 ファイルシステム使用率（性能・moun）です。運用引・rbacのD:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（運用・rbac）です。「installp -C」は「導入と起動でinstallp -Cを用い、mksysb image」を指し、mksysb imageではin・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>installp -C 障害切り分け mksysb image 0707</strong></p><p>検証目的: 導入と起動のinstallp -C 障害切り分け mksysb image 0707について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け107-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; installp -C
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0707A
画面・出力には AIX0707A が表示され、installp -C 障害切り分け mksysb image 0707 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0707B
画面・出力には AIX0707B が表示され、installp -C 障害切り分け mksysb image 0707 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0707C
画面・出力には AIX0707C が表示され、installp -C 障害切り分け mksysb image 0707 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0707A が画面・出力に表示されること
② ステップ2 の AIX0707B が画面・出力に表示されること
③ ステップ3 の AIX0707C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0749"><h3>lslpp -L バックアウト確認 altinst_rootvg 0458</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>潮騒整理ではAIX 7.3の導入と起動で lslpp -L を確認します。潮騒整理の導入と起動では altinst_rootvg とOSレベル表示を確認票へ整理します。潮騒整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。潮騒整理の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、潮騒整理を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslpp -L バックアウト確認 altinst_rootvg 0458の役割を調べています。chdev -l en0 -a mtu=1500 監査記録の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はネットワークでchdev -l en0 -aを用い・EtherChannelである。</li><li>B. 障害切り分けに用いる役割はデバイス管理でlsdev -Cc diskを用い・path status と構成マネージャー結果を確認する。</li><li>C. 障害切り分けに用いる役割はセキュリティでrolelist -u user1を用い・roles とロール一覧を確認する。</li><li>D. 障害切り分けに用いる役割は導入と起動でlslpp -Lを用い・altinst_rootvg とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でlslpp -Lを用い、altinst_rootvg」に対応する項目はバックアウト確認 altinst_r（バッ・lslp）です。バックに関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、altinst_rootvg」で、確認対象はls・バックです。監査・chdeのA:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は監査記録 EtherChannel（監査・chde）です。変更前・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い、path」を述べ、対象はpath status（変更・lsde）です。容量・roleのC:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は容量確認 roles（容量・role）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、altinst_rootvg」を指し、バックアウト確認 altinst_rではls・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslpp -L バックアウト確認 altinst_rootvg 0458</strong></p><p>検証目的: 導入と起動のlslpp -L バックアウト確認 altinst_rootvg 0458について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認098-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0458A
画面・出力には AIX0458A が表示され、lslpp -L バックアウト確認 altinst_rootvg 0458 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0458B
画面・出力には AIX0458B が表示され、lslpp -L バックアウト確認 altinst_rootvg 0458 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0458C
画面・出力には AIX0458C が表示され、lslpp -L バックアウト確認 altinst_rootvg 0458 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0458A が画面・出力に表示されること
② ステップ2 の AIX0458B が画面・出力に表示されること
③ ステップ3 の AIX0458C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0750"><h3>lslpp -L 性能確認 fileset level 0616</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>若竹採取ではAIX 7.3の導入と起動で lslpp -L を確認します。若竹採取の導入と起動では fileset level と代替ディスク状態を監査票へ転記します。若竹採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若竹採取の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、若竹採取を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslpp -L 性能確認 fileset level 0616を同一分類のchdev -l en0 -a mtu=1500 起動確認 MTU 0617と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はネットワークでchdev -l en0 -aを用い・MTU とMTU属性を確認する。</li><li>B. 管理対象との関係を表す説明はJFS2でlsfs -qを用い・agblksize とファイルシステム属性を確認する。lsfs -q 変更前確認 agblksize 0002固有の属性も確認対象に含める。</li><li>C. 管理対象との関係を表す説明は導入と起動でlslpp -Lを用い・fileset level と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はセキュリティでlsroleを用い・roles と監査設定を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「導入と起動でlslpp -Lを用い、fileset level」に対応する項目はfileset level（性能・lslp）です。性能に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、fileset level」で、確認対象はls・性能です。起動・chdeのA:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は起動確認 MTU（起動・chde）です。変更前・lsfsのB:は「JFS2でlsfs -qを用い、agblksize」を述べ、対象は変更前確認 agblksize（変更・lsfs）です。属性・lsroのD:は「セキュリティでlsroleを用い、roles と監査設定を確認する」を述べ、対象は属性確認 roles（属性・lsro）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、fileset level」を指し、fileset levelではls・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslpp -L 性能確認 fileset level 0616</strong></p><p>検証目的: 導入と起動のlslpp -L 性能確認 fileset level 0616について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認016-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0616A
画面・出力には AIX0616A が表示され、lslpp -L 性能確認 fileset level 0616 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0616B
画面・出力には AIX0616B が表示され、lslpp -L 性能確認 fileset level 0616 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0616C
画面・出力には AIX0616C が表示され、lslpp -L 性能確認 fileset level 0616 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0616A が画面・出力に表示されること
② ステップ2 の AIX0616B が画面・出力に表示されること
③ ステップ3 の AIX0616C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0751"><h3>lslpp -L 性能確認 mksysb image 0140</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>薄明採取ではAIX 7.3の導入と起動で lslpp -L を確認します。薄明採取の導入と起動では mksysb image と代替ディスク状態を引継ぎ票へ保管します。薄明採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。薄明採取の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、薄明採取を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslpp -L 性能確認 mksysb image 0140の技術的な意味を資料で確認するとき、chdev -l en0 -a mtu=1500 起動確認 Link Statusとの境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はネットワークでchdev -l en0 -aを用い・Link Status とMTU属性を確認する。</li><li>B. コマンドまたは機能の用途はデバイス管理でlsmpio -l hdisk0を用い・path status とデバイス一覧を確認する。</li><li>C. コマンドまたは機能の用途は導入と起動でlslpp -Lを用い・mksysb image と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はネットワークでcfgmgrを用い・EtherChannel とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「導入と起動でlslpp -Lを用い、mksysb image」に対応する項目はmksysb image（性能・lslp）です。性能に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、mksysb image」で、確認対象はls・性能です。起動・chdeのA:は「ネットワークでchdev -l en0 -aを用い、Link」を述べ、対象はLink Status（起動・chde）です。バック・lsmpのB:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（バッ・lsmp）です。変更後・cfgmのD:は「ネットワークでcfgmgrを用い、EtherChannel」を述べ、対象は変更後確認 EtherChannel（変更・cfgm）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、mksysb image」を指し、mksysb imageではls・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslpp -L 性能確認 mksysb image 0140</strong></p><p>検証目的: 導入と起動のlslpp -L 性能確認 mksysb image 0140について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動性能確認020-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0140A
画面・出力には AIX0140A が表示され、lslpp -L 性能確認 mksysb image 0140 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0140B
画面・出力には AIX0140B が表示され、lslpp -L 性能確認 mksysb image 0140 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0140C
画面・出力には AIX0140C が表示され、lslpp -L 性能確認 mksysb image 0140 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0140A が画面・出力に表示されること
② ステップ2 の AIX0140B が画面・出力に表示されること
③ ステップ3 の AIX0140C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0752"><h3>lslpp -L 構成照合 EFIX LABEL 0299</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>山吹復旧ではAIX 7.3の導入と起動で lslpp -L を確認します。山吹復旧の導入と起動では EFIX LABEL とfileset一覧を照合票へ整理します。山吹復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。山吹復旧の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、山吹復旧を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslpp -L 構成照合 EFIX LABEL 0299について構成や状態を確認します。chdev -l en0 -a mtu=1500 変更前確認 MTU 0300ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はネットワークでchdev -l en0 -aを用い・MTU と経路表を確認する。</li><li>B. 一次資料が示す主目的はデバイス管理でlsdev -Cc diskを用い・attribute と診断対象表示を確認する。</li><li>C. 一次資料が示す主目的は導入と起動でlslpp -Lを用い・EFIX LABEL とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でlslpp -Lを用い、EFIX LABEL」に対応する項目はEFIX LABEL（構成・lslp）です。構成に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、EFIX LABEL」で、確認対象はls・構成です。変更前・chdeのA:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は変更前確認 MTU（変更・chde）です。起動・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 attribute（起動・lsde）です。変更前・lsvgのD:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は変更前確認 再開位置（変更・lsvg）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、EFIX LABEL」を指し、EFIX LABELではls・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslpp -L 構成照合 EFIX LABEL 0299</strong></p><p>検証目的: 導入と起動のlslpp -L 構成照合 EFIX LABEL 0299について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合059-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0299A
画面・出力には AIX0299A が表示され、lslpp -L 構成照合 EFIX LABEL 0299 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0299B
画面・出力には AIX0299B が表示され、lslpp -L 構成照合 EFIX LABEL 0299 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0299C
画面・出力には AIX0299C が表示され、lslpp -L 構成照合 EFIX LABEL 0299 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0299A が画面・出力に表示されること
② ステップ2 の AIX0299B が画面・出力に表示されること
③ ステップ3 の AIX0299C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0753"><h3>lslpp -L 構成照合 EFIX LABEL 0359</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>秋桜変更ではAIX 7.3の導入と起動で lslpp -L を確認します。秋桜変更の導入と起動では EFIX LABEL とfileset一覧を照合票へ整理します。秋桜変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。秋桜変更の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、秋桜変更を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslpp -L 構成照合 EFIX LABEL 0359の設定や表示を読む前に役割を確認します。chdev -l en0 -a mtu=1500 変更前確認 MTU 0360ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的は導入と起動でlslpp -Lを用い・EFIX LABEL とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的はネットワークでchdev -l en0 -aを用い・MTU と経路表を確認する。</li><li>C. 一次資料が示す主目的はデバイス管理でlsdev -Cc diskを用い・attribute と診断対象表示を確認する。</li><li>D. 一次資料が示す主目的はセキュリティでrolelist -u user1を用い・authorizationsである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「導入と起動でlslpp -Lを用い、EFIX LABEL」に対応する項目はEFIX LABEL（構成・lslp）です。構成に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、EFIX LABEL」で、確認対象はls・構成です。変更前・chdeのB:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は変更前確認 MTU（変更・chde）です。起動・lsdeのC:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 attribute（起動・lsde）です。障害切・roleのD:は「セキュリティでrolelist -u user1を用い」を述べ、対象は障害切り分け authorizati（障害・role）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、EFIX LABEL」を指し、EFIX LABELではls・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslpp -L 構成照合 EFIX LABEL 0359</strong></p><p>検証目的: 導入と起動のlslpp -L 構成照合 EFIX LABEL 0359について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合119-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0359A
画面・出力には AIX0359A が表示され、lslpp -L 構成照合 EFIX LABEL 0359 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0359B
画面・出力には AIX0359B が表示され、lslpp -L 構成照合 EFIX LABEL 0359 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0359C
画面・出力には AIX0359C が表示され、lslpp -L 構成照合 EFIX LABEL 0359 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0359A が画面・出力に表示されること
② ステップ2 の AIX0359B が画面・出力に表示されること
③ ステップ3 の AIX0359C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0754"><h3>lslpp -L 構成照合 altinst_rootvg 0775</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>岩清水復旧ではAIX 7.3の導入と起動で lslpp -L を確認します。岩清水復旧の導入と起動では altinst_rootvg とfileset一覧を点検票へ整理します。岩清水復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。岩清水復旧の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、岩清水復旧を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslpp -L 構成照合 altinst_rootvg 0775の設定や表示を読む前に役割を確認します。mksysb 起動確認 EFIX LABEL 0820ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きは導入と起動でmksysbを用い・EFIX LABEL と代替ディスク状態を確認する。</li><li>B. 対象資源に対する働きはSRCとログでstartsrc -s inetd -aを用い・IDENTIFIERである。startsrc -s inetd -a &quot;-d&quot; 障害切り分け固有の属性も確認対象に含める。</li><li>C. 対象資源に対する働きは導入と起動でlslpp -Lを用い・altinst_rootvg とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはデバイス管理でodmget CuDvを用い・attribute と構成マネージャー結果を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構成・lslpでCの記述「導入と起動でlslpp -Lを用い、altinst_rootvg」に対応する項目は構成照合 altinst_rootv（構成・lslp）です。構成に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、altinst_rootvg」で、確認対象はls・構成です。起動・mksyのA:は「導入と起動でmksysbを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（起動・mksy）です。障害切・starのB:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け IDENTIFIER（障害・star）です。状態・odmgのD:は「デバイス管理でodmget CuDvを用い、attribute」を述べ、対象は状態確認 attribute（状態・odmg）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、altinst_rootvg」を指し、構成照合 altinst_rootvではls・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslpp -L 構成照合 altinst_rootvg 0775</strong></p><p>検証目的: 導入と起動のlslpp -L 構成照合 altinst_rootvg 0775について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合055-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0775A
画面・出力には AIX0775A が表示され、lslpp -L 構成照合 altinst_rootvg 0775 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0775B
画面・出力には AIX0775B が表示され、lslpp -L 構成照合 altinst_rootvg 0775 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0775C
画面・出力には AIX0775C が表示され、lslpp -L 構成照合 altinst_rootvg 0775 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0775A が画面・出力に表示されること
② ステップ2 の AIX0775B が画面・出力に表示されること
③ ステップ3 の AIX0775C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0755"><h3>lslpp -L 構成照合 altinst_rootvg 0835</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>青磁変更ではAIX 7.3の導入と起動で lslpp -L を確認します。青磁変更の導入と起動では altinst_rootvg とfileset一覧を点検票へ整理します。青磁変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。青磁変更の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、青磁変更を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslpp -L 構成照合 altinst_rootvg 0835について構成や状態を確認します。lspv 性能確認 保持設定ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。</li><li>B. 対象資源に対する働きは導入と起動でalt_disk_copyを用い・mksysb image とfileset一覧を確認する。</li><li>C. 対象資源に対する働きはセキュリティでsetsecattrを用い・enhanced_RBAC と監査設定を確認する。</li><li>D. 対象資源に対する働きは導入と起動でlslpp -Lを用い・altinst_rootvg とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構成・lslpでDの記述「導入と起動でlslpp -Lを用い、altinst_rootvg」に対応する項目は構成照合 altinst_rootv（構成・lslp）です。構成に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、altinst_rootvg」で、確認対象はls・構成です。性能・保持・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は性能確認 保持設定（性能・lspv）です。容量・alt_のB:は「導入と起動でalt_disk_copyを用い、mksysb」を述べ、対象はmksysb image（容量・alt_）です。性能・setsのC:は「セキュリティでsetsecattrを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・sets）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、altinst_rootvg」を指し、構成照合 altinst_rootvではls・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslpp -L 構成照合 altinst_rootvg 0835</strong></p><p>検証目的: 導入と起動のlslpp -L 構成照合 altinst_rootvg 0835について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動構成照合115-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0835A
画面・出力には AIX0835A が表示され、lslpp -L 構成照合 altinst_rootvg 0835 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0835B
画面・出力には AIX0835B が表示され、lslpp -L 構成照合 altinst_rootvg 0835 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0835C
画面・出力には AIX0835C が表示され、lslpp -L 構成照合 altinst_rootvg 0835 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0835A が画面・出力に表示されること
② ステップ2 の AIX0835B が画面・出力に表示されること
③ ステップ3 の AIX0835C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0756"><h3>lslpp -L 運用引継ぎ fileset level 0745</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>花冷監査ではAIX 7.3の導入と起動で lslpp -L を確認します。花冷監査の導入と起動では fileset level と起動デバイス設定を採取票へ記録します。花冷監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。花冷監査の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、花冷監査を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lslpp -L 運用引継ぎ fileset level 0745」を「chdev -l en0 -a mtu=1500 容量確認 Media Speed」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はネットワークでchdev -l en0 -aを用い・Media Speed Runningである。</li><li>B. 保守作業で参照する機能は導入と起動でlslpp -Lを用い・fileset level と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はJFS2でlsfs -qを用い・agblksize と内部スナップショットを確認する。</li><li>D. 保守作業で参照する機能はセキュリティでlsroleを用い・roles とRBAC属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でlslpp -Lを用い、fileset level」に対応する項目はfileset level（運用・lslp）です。運用引に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、fileset level」で、確認対象はls・運用引です。容量・chdeのA:は「ネットワークでchdev -l en0 -aを用い、Media」を述べ、対象はSpeed Running（容量・chde）です。状態・lsfsのC:は「JFS2でlsfs -qを用い、agblksize」を述べ、対象は状態確認 agblksize（状態・lsfs）です。性能・lsroのD:は「セキュリティでlsroleを用い、roles」を述べ、対象は性能確認 roles（性能・lsro）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、fileset level」を指し、fileset levelではls・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslpp -L 運用引継ぎ fileset level 0745</strong></p><p>検証目的: 導入と起動のlslpp -L 運用引継ぎ fileset level 0745について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ025-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0745A
画面・出力には AIX0745A が表示され、lslpp -L 運用引継ぎ fileset level 0745 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0745B
画面・出力には AIX0745B が表示され、lslpp -L 運用引継ぎ fileset level 0745 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0745C
画面・出力には AIX0745C が表示され、lslpp -L 運用引継ぎ fileset level 0745 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0745A が画面・出力に表示されること
② ステップ2 の AIX0745B が画面・出力に表示されること
③ ステップ3 の AIX0745C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0757"><h3>lslpp -L 運用引継ぎ fileset level 0805</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>深雪変更ではAIX 7.3の導入と起動で lslpp -L を確認します。深雪変更の導入と起動では fileset level と起動デバイス設定を採取票へ記録します。深雪変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。深雪変更の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、深雪変更を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslpp -L 運用引継ぎ fileset level 0805を保守記録に説明する必要があります。lsattr 詳細確認 確認範囲と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は導入と起動でlslpp -Lを用い・fileset level と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はデバイスや sys0 などの属性値を表示するコマンドである。</li><li>C. 保守作業で参照する機能はLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。</li><li>D. 保守作業で参照する機能は導入と起動でbosboot -a -dを用い・fileset level と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 運用引・lslpでAの記述「導入と起動でlslpp -Lを用い、fileset level」に対応する項目はfileset level（運用・lslp）です。運用引に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、fileset level」で、確認対象はls・運用引です。詳細・確認・lsatのB:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は詳細確認 確認範囲（詳細・lsat）です。性能・migrのC:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（性能・migr）です。性能・bosbのD:は「導入と起動でbosboot -a -dを用い、fileset」を述べ、対象はfileset level（性能・bosb）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、fileset level」を指し、fileset levelではls・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslpp -L 運用引継ぎ fileset level 0805</strong></p><p>検証目的: 導入と起動のlslpp -L 運用引継ぎ fileset level 0805について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ085-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0805A
画面・出力には AIX0805A が表示され、lslpp -L 運用引継ぎ fileset level 0805 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0805B
画面・出力には AIX0805B が表示され、lslpp -L 運用引継ぎ fileset level 0805 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0805C
画面・出力には AIX0805C が表示され、lslpp -L 運用引継ぎ fileset level 0805 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0805A が画面・出力に表示されること
② ステップ2 の AIX0805B が画面・出力に表示されること
③ ステップ3 の AIX0805C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0758"><h3>lslpp -L 運用引継ぎ mksysb image 0269</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>梅雨晴監査ではAIX 7.3の導入と起動で lslpp -L を確認します。梅雨晴監査の導入と起動では mksysb image と起動デバイス設定を復旧票へ残します。梅雨晴監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。梅雨晴監査の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、梅雨晴監査を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslpp -L 運用引継ぎ mksysb image 0269を保守記録に説明する必要があります。chdev -l en0 -a mtu=1500 容量確認と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はネットワークでchdev -l en0 -aを用い・EtherChannel とアダプター一覧を確認する。</li><li>B. 仕様上の役割は導入と起動でlslpp -Lを用い・mksysb image と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割はデバイス管理でlsmpio -l hdisk0を用い・path status とODM属性を確認する。</li><li>D. 仕様上の役割はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でlslpp -Lを用い、mksysb image」に対応する項目はmksysb image（運用・lslp）です。運用引に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、mksysb image」で、確認対象はls・運用引です。容量・chdeのA:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は容量確認 EtherChannel（容量・chde）です。変更後・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（変更・lsmp）です。性能・資料・lsvgのD:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は性能確認 資料見出し（性能・lsvg）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、mksysb image」を指し、mksysb imageではls・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslpp -L 運用引継ぎ mksysb image 0269</strong></p><p>検証目的: 導入と起動のlslpp -L 運用引継ぎ mksysb image 0269について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ029-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0269A
画面・出力には AIX0269A が表示され、lslpp -L 運用引継ぎ mksysb image 0269 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0269B
画面・出力には AIX0269B が表示され、lslpp -L 運用引継ぎ mksysb image 0269 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0269C
画面・出力には AIX0269C が表示され、lslpp -L 運用引継ぎ mksysb image 0269 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0269A が画面・出力に表示されること
② ステップ2 の AIX0269B が画面・出力に表示されること
③ ステップ3 の AIX0269C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0759"><h3>lslpp -L 運用引継ぎ mksysb image 0329</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>銀砂変更ではAIX 7.3の導入と起動で lslpp -L を確認します。銀砂変更の導入と起動では mksysb image と起動デバイス設定を復旧票へ残します。銀砂変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。銀砂変更の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、銀砂変更を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lslpp -L 運用引継ぎ mksysb image 0329」を「chdev -l en0 -a mtu=1500 容量確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はネットワークでchdev -l en0 -aを用い・EtherChannel とアダプター一覧を確認する。</li><li>B. 仕様上の役割は導入と起動でlslpp -Lを用い・mksysb image と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割はデバイス管理でlsdev -Cc diskを用い・microcode level とODM属性を確認する。</li><li>D. 仕様上の役割はセキュリティでrolelist -u user1を用い・authorizationsである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でlslpp -Lを用い、mksysb image」に対応する項目はmksysb image（運用・lslp）です。運用引に関する導入と起動の仕様は「導入と起動でlslpp -Lを用い、mksysb image」で、確認対象はls・運用引です。容量・chdeのA:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は容量確認 EtherChannel（容量・chde）です。障害切・lsdeのC:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象はmicrocode level（障害・lsde）です。起動・roleのD:は「セキュリティでrolelist -u user1を用い」を述べ、対象は起動確認 authorization（起動・role）です。「lslpp -L」は「導入と起動でlslpp -Lを用い、mksysb image」を指し、mksysb imageではls・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslpp -L 運用引継ぎ mksysb image 0329</strong></p><p>検証目的: 導入と起動のlslpp -L 運用引継ぎ mksysb image 0329について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ089-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0329A
画面・出力には AIX0329A が表示され、lslpp -L 運用引継ぎ mksysb image 0329 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0329B
画面・出力には AIX0329B が表示され、lslpp -L 運用引継ぎ mksysb image 0329 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0329C
画面・出力には AIX0329C が表示され、lslpp -L 運用引継ぎ mksysb image 0329 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0329A が画面・出力に表示されること
② ステップ2 の AIX0329B が画面・出力に表示されること
③ ステップ3 の AIX0329C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0760"><h3>mksysb 容量確認 Technology Level 0473</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>朝霧整理ではAIX 7.3の導入と起動で mksysb を確認します。朝霧整理の導入と起動では Technology Level と起動デバイス設定を復旧票へ残します。朝霧整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。朝霧整理の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、朝霧整理を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「mksysb 容量確認 Technology Level 0473」を「no -a 性能確認 Link Status 0474」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はネットワークでno -aを用い・Link Status とアダプター一覧を確認する。</li><li>B. 仕様上の役割はデバイス管理でlscfg -vl ent0を用い・Available とODM属性を確認する。</li><li>C. 仕様上の役割はセキュリティでlsuserを用い・user attributes とRBAC属性を確認する。lsuser 属性確認 user attributes 0166固有の属性も確認対象に含める。</li><li>D. 仕様上の役割は導入と起動でmksysbを用い・Technology Level と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「導入と起動でmksysbを用い、Technology Level」に対応する項目はTechnology Level（容量・mksy）です。容量に関する導入と起動の仕様は「導入と起動でmksysbを用い、Technology Level」で、確認対象はmk・容量です。性能・noのA:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（性能・no）です。バック・lscfのB:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象はバックアウト確認 Available（バッ・lscf）です。属性・lsusのC:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（属性・lsus）です。「mksysb」は「導入と起動でmksysbを用い、Technology Level」を指し、Technology Levelではmk・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 容量確認 Technology Level 0473</strong></p><p>検証目的: 導入と起動のmksysb 容量確認 Technology Level 0473について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認113-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0473A
画面・出力には AIX0473A が表示され、mksysb 容量確認 Technology Level 0473 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0473B
画面・出力には AIX0473B が表示され、mksysb 容量確認 Technology Level 0473 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0473C
画面・出力には AIX0473C が表示され、mksysb 容量確認 Technology Level 0473 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0473A が画面・出力に表示されること
② ステップ2 の AIX0473B が画面・出力に表示されること
③ ステップ3 の AIX0473C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0761"><h3>mksysb 状態確認 bootlist 0631</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>遠雷採取ではAIX 7.3の導入と起動で mksysb を確認します。遠雷採取の導入と起動では bootlist とfileset一覧を点検票へ整理します。遠雷採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。遠雷採取の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、遠雷採取を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mksysb 状態確認 bootlist 0631の設定や表示を読む前に役割を確認します。no -a 構成照合 Destination 0632ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはネットワークでno -aを用い・Destination と経路表を確認する。</li><li>B. 対象資源に対する働きはLVMでmigratepvを用い・PP SIZE とミラーコピー状態を確認する。</li><li>C. 対象資源に対する働きは導入と起動でmksysbを用い・bootlist とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはセキュリティでchuserを用い・user attributes とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でmksysbを用い、bootlist とfileset一覧を確認する」に対応する項目は状態確認 bootlist（状態・mksy）です。状態に関する導入と起動の仕様は「導入と起動でmksysbを用い、bootlist」で、確認対象はmk・状態です。構成・noのA:は「ネットワークでno -aを用い、Destination」を述べ、対象は構成照合 Destination（構成・no）です。バック・migrのB:は「LVMでmigratepvを用い、PP SIZE」を述べ、対象はPP SIZE（バッ・migr）です。変更前・chusのD:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（変更・chus）です。「mksysb」は「導入と起動でmksysbを用い、bootlist」を指し、状態確認 bootlistではmk・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 状態確認 bootlist 0631</strong></p><p>検証目的: 導入と起動のmksysb 状態確認 bootlist 0631について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認031-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0631A
画面・出力には AIX0631A が表示され、mksysb 状態確認 bootlist 0631 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0631B
画面・出力には AIX0631B が表示され、mksysb 状態確認 bootlist 0631 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0631C
画面・出力には AIX0631C が表示され、mksysb 状態確認 bootlist 0631 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0631A が画面・出力に表示されること
② ステップ2 の AIX0631B が画面・出力に表示されること
③ ステップ3 の AIX0631C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0762"><h3>mksysb 状態確認 fileset level 0155</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>青磁採取ではAIX 7.3の導入と起動で mksysb を確認します。青磁採取の導入と起動では fileset level とfileset一覧を照合票へ整理します。青磁採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。青磁採取の注意点として bosboot失敗後の再起動 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、青磁採取を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mksysb 状態確認 fileset level 0155について構成や状態を確認します。no -a 構成照合 Media Speed Running 0156ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はネットワークでno -aを用い・Media Speed Running と経路表を確認する。</li><li>B. 一次資料が示す主目的はデバイス管理でodmget CuDvを用い・Available と診断対象表示を確認する。</li><li>C. 一次資料が示す主目的は導入と起動でmksysbを用い・fileset level とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はネットワークでnetstat -rnを用い・Link Status と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でmksysbを用い、fileset level」に対応する項目はfileset level（状態・mksy）です。状態に関する導入と起動の仕様は「導入と起動でmksysbを用い、fileset level」で、確認対象はmk・状態です。構成・noのA:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（構成・no）です。容量・odmgのB:は「デバイス管理でodmget CuDvを用い、Available」を述べ、対象は容量確認 Available（容量・odmg）です。監査・netsのD:は「ネットワークでnetstat -rnを用い、Link Status」を述べ、対象はLink Status（監査・nets）です。「mksysb」は「導入と起動でmksysbを用い、fileset level」を指し、fileset levelではmk・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 状態確認 fileset level 0155</strong></p><p>検証目的: 導入と起動のmksysb 状態確認 fileset level 0155について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動状態確認035-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0155A
画面・出力には AIX0155A が表示され、mksysb 状態確認 fileset level 0155 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0155B
画面・出力には AIX0155B が表示され、mksysb 状態確認 fileset level 0155 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0155C
画面・出力には AIX0155C が表示され、mksysb 状態確認 fileset level 0155 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0155A が画面・出力に表示されること
② ステップ2 の AIX0155B が画面・出力に表示されること
③ ステップ3 の AIX0155C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0763"><h3>mksysb 監査記録 Technology Level 0601</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>白露採取ではAIX 7.3の導入と起動で mksysb を確認します。白露採取の導入と起動では Technology Level と起動デバイス設定を採取票へ記録します。白露採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。白露採取の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、白露採取を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「mksysb 監査記録 Technology Level 0601」を「no -a 運用引継ぎ Link Status 0602」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は導入と起動でmksysbを用い・Technology Level と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はネットワークでno -aを用い・Link Status とアダプター一覧を確認する。</li><li>C. 保守作業で参照する機能はデバイス属性を変更する管理コマンドである。</li><li>D. 保守作業で参照する機能はセキュリティでchuserを用い・user attributes とRBAC属性を確認する。chuser 容量確認 user attributes 0294固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「導入と起動でmksysbを用い、Technology Level」に対応する項目はTechnology Level（監査・mksy）です。監査に関する導入と起動の仕様は「導入と起動でmksysbを用い、Technology Level」で、確認対象はmk・監査です。運用引・noのB:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（運用・no）です。一覧・一致・chdeのC:は「デバイス属性を変更する管理コマンド」を述べ、対象は一覧確認 一致条件（一覧・chde）です。容量・chusのD:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（容量・chus）です。「mksysb」は「導入と起動でmksysbを用い、Technology Level」を指し、Technology Levelではmk・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 監査記録 Technology Level 0601</strong></p><p>検証目的: 導入と起動のmksysb 監査記録 Technology Level 0601について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録001-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0601A
画面・出力には AIX0601A が表示され、mksysb 監査記録 Technology Level 0601 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0601B
画面・出力には AIX0601B が表示され、mksysb 監査記録 Technology Level 0601 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0601C
画面・出力には AIX0601C が表示され、mksysb 監査記録 Technology Level 0601 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0601A が画面・出力に表示されること
② ステップ2 の AIX0601B が画面・出力に表示されること
③ ステップ3 の AIX0601C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0764"><h3>mksysb 監査記録 altinst_rootvg 0125</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>深雪採取ではAIX 7.3の導入と起動で mksysb を確認します。深雪採取の導入と起動では altinst_rootvg と起動デバイス設定を復旧票へ残します。深雪採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。深雪採取の注意点として altinst_rootvgの誤varyon を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、深雪採取を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mksysb 監査記録 altinst_rootvg 0125を保守記録に説明する必要があります。no -a 運用引継ぎ Gateway 0126と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はネットワークでno -aを用い・Gateway とアダプター一覧を確認する。</li><li>B. 仕様上の役割は導入と起動でmksysbを用い・altinst_rootvg と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割はデバイス管理でodmget CuDvを用い・PVID とODM属性を確認する。</li><li>D. 仕様上の役割はネットワークでnetstat -rnを用い・Destination とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「導入と起動でmksysbを用い、altinst_rootvg」に対応する項目は監査記録 altinst_rootv（監査・mksy）です。監査に関する導入と起動の仕様は「導入と起動でmksysbを用い、altinst_rootvg」で、確認対象はmk・監査です。運用引・noのA:は「ネットワークでno -aを用い、Gateway」を述べ、対象は運用引継ぎ Gateway（運用・no）です。変更前・odmgのC:は「デバイス管理でodmget CuDvを用い、PVID」を述べ、対象は変更前確認 PVID（変更・odmg）です。状態・netsのD:は「ネットワークでnetstat -rnを用い、Destination」を述べ、対象は状態確認 Destination（状態・nets）です。「mksysb」は「導入と起動でmksysbを用い、altinst_rootvg」を指し、監査記録 altinst_rootvではmk・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 監査記録 altinst_rootvg 0125</strong></p><p>検証目的: 導入と起動のmksysb 監査記録 altinst_rootvg 0125について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動監査記録005-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0125A
画面・出力には AIX0125A が表示され、mksysb 監査記録 altinst_rootvg 0125 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0125B
画面・出力には AIX0125B が表示され、mksysb 監査記録 altinst_rootvg 0125 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0125C
画面・出力には AIX0125C が表示され、mksysb 監査記録 altinst_rootvg 0125 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0125A が画面・出力に表示されること
② ステップ2 の AIX0125B が画面・出力に表示されること
③ ステップ3 の AIX0125C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0765"><h3>mksysb 起動確認 EFIX LABEL 0760</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>青葉復旧ではAIX 7.3の導入と起動で mksysb を確認します。青葉復旧の導入と起動では EFIX LABEL と代替ディスク状態を監査票へ転記します。青葉復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。青葉復旧の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、青葉復旧を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mksysb 起動確認 EFIX LABEL 0760を同一分類のno -a 属性確認 Destination 0761と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はネットワークでno -aを用い・Destination とMTU属性を確認する。</li><li>B. 管理対象との関係を表す説明はJFS2でsplitcopyを用い・isnapshot とファイルシステム属性を確認する。</li><li>C. 管理対象との関係を表す説明はセキュリティでchuserを用い・enhanced_RBAC と監査設定を確認する。</li><li>D. 管理対象との関係を表す説明は導入と起動でmksysbを用い・EFIX LABEL と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でmksysbを用い、EFIX LABEL と代替ディスク状態を確認する」に対応する項目はEFIX LABEL（起動・mksy）です。起動に関する導入と起動の仕様は「導入と起動でmksysbを用い、EFIX LABEL」で、確認対象はmk・起動です。属性・noのA:は「ネットワークでno -aを用い、Destination」を述べ、対象は属性確認 Destination（属性・no）です。変更後・spliのB:は「JFS2でsplitcopyを用い、isnapshot」を述べ、対象は変更後確認 isnapshot（変更・spli）です。状態・chusのC:は「セキュリティでchuserを用い、enhanced_RBAC」を述べ、対象は状態確認 enhanced_RBAC（状態・chus）です。「mksysb」は「導入と起動でmksysbを用い、EFIX LABEL」を指し、EFIX LABELではmk・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 起動確認 EFIX LABEL 0760</strong></p><p>検証目的: 導入と起動のmksysb 起動確認 EFIX LABEL 0760について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認040-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0760A
画面・出力には AIX0760A が表示され、mksysb 起動確認 EFIX LABEL 0760 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0760B
画面・出力には AIX0760B が表示され、mksysb 起動確認 EFIX LABEL 0760 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0760C
画面・出力には AIX0760C が表示され、mksysb 起動確認 EFIX LABEL 0760 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0760A が画面・出力に表示されること
② ステップ2 の AIX0760B が画面・出力に表示されること
③ ステップ3 の AIX0760C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0766"><h3>mksysb 起動確認 EFIX LABEL 0820</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>薄明変更ではAIX 7.3の導入と起動で mksysb を確認します。薄明変更の導入と起動では EFIX LABEL と代替ディスク状態を監査票へ転記します。薄明変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。薄明変更の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、薄明変更を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mksysb 起動確認 EFIX LABEL 0820の技術的な意味を資料で確認するとき、errpt 属性照合 ログ採取との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明は導入と起動でmksysbを用い・EFIX LABEL と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>C. 管理対象との関係を表す説明は導入と起動でinstallp -Cを用い・bootlist とfileset一覧を確認する。</li><li>D. 管理対象との関係を表す説明はデバイス管理でlsdev -Cc diskを用い・attribute と診断対象表示を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 起動・mksyでAの記述「導入と起動でmksysbを用い、EFIX LABEL」に対応する項目はEFIX LABEL（起動・mksy）です。起動に関する導入と起動の仕様は「導入と起動でmksysbを用い、EFIX LABEL」で、確認対象はmk・起動です。属性・ログ・errpのB:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は属性照合 ログ採取（属性・errp）です。障害切・instのC:は「導入と起動でinstallp -Cを用い、bootlist」を述べ、対象は障害切り分け bootlist（障害・inst）です。起動・lsdeのD:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 attribute（起動・lsde）です。「mksysb」は「導入と起動でmksysbを用い、EFIX LABEL」を指し、EFIX LABELではmk・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 起動確認 EFIX LABEL 0820</strong></p><p>検証目的: 導入と起動のmksysb 起動確認 EFIX LABEL 0820について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認100-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0820A
画面・出力には AIX0820A が表示され、mksysb 起動確認 EFIX LABEL 0820 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0820B
画面・出力には AIX0820B が表示され、mksysb 起動確認 EFIX LABEL 0820 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0820C
画面・出力には AIX0820C が表示され、mksysb 起動確認 EFIX LABEL 0820 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0820A が画面・出力に表示されること
② ステップ2 の AIX0820B が画面・出力に表示されること
③ ステップ3 の AIX0820C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0767"><h3>mksysb 起動確認 Technology Level 0284</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>若草復旧ではAIX 7.3の導入と起動で mksysb を確認します。若草復旧の導入と起動では Technology Level と代替ディスク状態を引継ぎ票へ保管します。若草復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若草復旧の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、若草復旧を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mksysb 起動確認 Technology Level 0284の技術的な意味を資料で確認するとき、no -a 属性確認 Media Speed Running 0285との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。</li><li>B. コマンドまたは機能の用途はデバイス管理でodmget CuDvを用い・microcode level とデバイス一覧を確認する。</li><li>C. コマンドまたは機能の用途は導入と起動でmksysbを用い・Technology Level と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はデバイス属性を変更する管理コマンドである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でmksysbを用い、Technology Level」に対応する項目はTechnology Level（起動・mksy）です。起動に関する導入と起動の仕様は「導入と起動でmksysbを用い、Technology Level」で、確認対象はmk・起動です。属性・noのA:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（属性・no）です。監査・odmgのB:は「デバイス管理でodmget CuDvを用い、microcode」を述べ、対象はmicrocode level（監査・odmg）です。性能・識別・chdeのD:は「デバイス属性を変更する管理コマンド」を述べ、対象は性能確認 識別値（性能・chde）です。「mksysb」は「導入と起動でmksysbを用い、Technology Level」を指し、Technology Levelではmk・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 起動確認 Technology Level 0284</strong></p><p>検証目的: 導入と起動のmksysb 起動確認 Technology Level 0284について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認044-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0284A
画面・出力には AIX0284A が表示され、mksysb 起動確認 Technology Level 0284 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0284B
画面・出力には AIX0284B が表示され、mksysb 起動確認 Technology Level 0284 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0284C
画面・出力には AIX0284C が表示され、mksysb 起動確認 Technology Level 0284 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0284A が画面・出力に表示されること
② ステップ2 の AIX0284B が画面・出力に表示されること
③ ステップ3 の AIX0284C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0768"><h3>mksysb 起動確認 Technology Level 0344</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>霜月変更ではAIX 7.3の導入と起動で mksysb を確認します。霜月変更の導入と起動では Technology Level と代替ディスク状態を引継ぎ票へ保管します。霜月変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。霜月変更の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、霜月変更を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mksysb 起動確認 Technology Level 0344を同一分類のno -a 属性確認 Media Speed Running 0345と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。</li><li>B. コマンドまたは機能の用途はデバイス管理でlscfg -vl ent0を用い・Available とデバイス一覧を確認する。</li><li>C. コマンドまたは機能の用途はセキュリティでlsuserを用い・user attributes と監査設定を確認する。</li><li>D. コマンドまたは機能の用途は導入と起動でmksysbを用い・Technology Level と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「導入と起動でmksysbを用い、Technology Level」に対応する項目はTechnology Level（起動・mksy）です。起動に関する導入と起動の仕様は「導入と起動でmksysbを用い、Technology Level」で、確認対象はmk・起動です。属性・noのA:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（属性・no）です。運用引・lscfのB:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象は運用引継ぎ Available（運用・lscf）です。構成・lsusのC:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（構成・lsus）です。「mksysb」は「導入と起動でmksysbを用い、Technology Level」を指し、Technology Levelではmk・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 起動確認 Technology Level 0344</strong></p><p>検証目的: 導入と起動のmksysb 起動確認 Technology Level 0344について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認104-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0344A
画面・出力には AIX0344A が表示され、mksysb 起動確認 Technology Level 0344 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0344B
画面・出力には AIX0344B が表示され、mksysb 起動確認 Technology Level 0344 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0344C
画面・出力には AIX0344C が表示され、mksysb 起動確認 Technology Level 0344 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0344A が画面・出力に表示されること
② ステップ2 の AIX0344B が画面・出力に表示されること
③ ステップ3 の AIX0344C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0769"><h3>mksysb 障害切り分け bootlist 0254</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>星霜監査ではAIX 7.3の導入と起動で mksysb を確認します。星霜監査の導入と起動では bootlist とOSレベル表示を確認票へ整理します。星霜監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。星霜監査の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、星霜監査を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mksysb 障害切り分け bootlist 0254に関する障害切り分けの前提を確認しています。no -a バックアウト確認 Gateway 0255の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割は導入と起動でmksysbを用い・bootlist とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 障害切り分けに用いる役割はネットワークでno -aを用い・Gateway とEthernet統計を確認する。</li><li>C. 障害切り分けに用いる役割はデバイス管理でodmget CuDvを用い・attribute と構成マネージャー結果を確認する。</li><li>D. 障害切り分けに用いる役割はデバイス属性を変更する管理コマンドである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「導入と起動でmksysbを用い、bootlist とOSレベル表示を確認する」に対応する項目は障害切り分け bootlist（障害・mksy）です。障害切に関する導入と起動の仕様は「導入と起動でmksysbを用い、bootlist」で、確認対象はmk・障害切です。バック・noのB:は「ネットワークでno -aを用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・no）です。状態・odmgのC:は「デバイス管理でodmget CuDvを用い、attribute」を述べ、対象は状態確認 attribute（状態・odmg）です。障害切・chdeのD:は「デバイス属性を変更する管理コマンド」を述べ、対象は障害切り分け ボリューム状態（障害・chde）です。「mksysb」は「導入と起動でmksysbを用い、bootlist」を指し、障害切り分け bootlistではmk・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 障害切り分け bootlist 0254</strong></p><p>検証目的: 導入と起動のmksysb 障害切り分け bootlist 0254について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け014-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0254A
画面・出力には AIX0254A が表示され、mksysb 障害切り分け bootlist 0254 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0254B
画面・出力には AIX0254B が表示され、mksysb 障害切り分け bootlist 0254 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0254C
画面・出力には AIX0254C が表示され、mksysb 障害切り分け bootlist 0254 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0254A が画面・出力に表示されること
② ステップ2 の AIX0254B が画面・出力に表示されること
③ ステップ3 の AIX0254C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0770"><h3>mksysb 障害切り分け bootlist 0314</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>銀嶺復旧ではAIX 7.3の導入と起動で mksysb を確認します。銀嶺復旧の導入と起動では bootlist とOSレベル表示を確認票へ整理します。銀嶺復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。銀嶺復旧の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、銀嶺復旧を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mksysb 障害切り分け bootlist 0314の役割を調べています。no -a バックアウト確認 Gateway 0315の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割は導入と起動でmksysbを用い・bootlist とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 障害切り分けに用いる役割はネットワークでno -aを用い・Gateway とEthernet統計を確認する。</li><li>C. 障害切り分けに用いる役割はデバイス管理でlscfg -vl ent0を用い・PVID と構成マネージャー結果を確認する。</li><li>D. 障害切り分けに用いる役割はセキュリティでlsuserを用い・user attributes とロール一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でmksysbを用い、bootlist とOSレベル表示を確認する」に対応する項目は障害切り分け bootlist（障害・mksy）です。障害切に関する導入と起動の仕様は「導入と起動でmksysbを用い、bootlist」で、確認対象はmk・障害切です。バック・noのB:は「ネットワークでno -aを用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・no）です。構成・lscfのC:は「デバイス管理でlscfg -vl ent0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lscf）です。運用引・lsusのD:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（運用・lsus）です。「mksysb」は「導入と起動でmksysbを用い、bootlist」を指し、障害切り分け bootlistではmk・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 障害切り分け bootlist 0314</strong></p><p>検証目的: 導入と起動のmksysb 障害切り分け bootlist 0314について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け074-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0314A
画面・出力には AIX0314A が表示され、mksysb 障害切り分け bootlist 0314 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0314B
画面・出力には AIX0314B が表示され、mksysb 障害切り分け bootlist 0314 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0314C
画面・出力には AIX0314C が表示され、mksysb 障害切り分け bootlist 0314 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0314A が画面・出力に表示されること
② ステップ2 の AIX0314B が画面・出力に表示されること
③ ステップ3 の AIX0314C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0771"><h3>mksysb 障害切り分け mksysb image 0730</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>桜雲監査ではAIX 7.3の導入と起動で mksysb を確認します。桜雲監査の導入と起動では mksysb image とOSレベル表示を保守票へ記録します。桜雲監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。桜雲監査の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、桜雲監査を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mksysb 障害切り分け mksysb image 0730の役割を調べています。no -a バックアウト確認 Link Status 0731の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はネットワークでno -aを用い・Link Status とEthernet統計を確認する。</li><li>B. 表示や設定で扱う内容は導入と起動でmksysbを用い・mksysb image とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はJFS2でsnapを用い・lff とログデバイス設定を確認する。</li><li>D. 表示や設定で扱う内容はセキュリティでchuserを用い・enhanced_RBAC とロール一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「導入と起動でmksysbを用い、mksysb image とOSレベル表示を確認する」に対応する項目はmksysb image（障害・mksy）です。障害切に関する導入と起動の仕様は「導入と起動でmksysbを用い、mksysb image」で、確認対象はmk・障害切です。バック・noのA:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（バッ・no）です。容量・snapのC:は「JFS2でsnapを用い、lff とログデバイス設定を確認する」を述べ、対象は容量確認 lff（容量・snap）です。監査・chusのD:は「セキュリティでchuserを用い、enhanced_RBAC」を述べ、対象は監査記録 enhanced_RBAC（監査・chus）です。「mksysb」は「導入と起動でmksysbを用い、mksysb image」を指し、mksysb imageではmk・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 障害切り分け mksysb image 0730</strong></p><p>検証目的: 導入と起動のmksysb 障害切り分け mksysb image 0730について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け010-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0730A
画面・出力には AIX0730A が表示され、mksysb 障害切り分け mksysb image 0730 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0730B
画面・出力には AIX0730B が表示され、mksysb 障害切り分け mksysb image 0730 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0730C
画面・出力には AIX0730C が表示され、mksysb 障害切り分け mksysb image 0730 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0730A が画面・出力に表示されること
② ステップ2 の AIX0730B が画面・出力に表示されること
③ ステップ3 の AIX0730C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0772"><h3>mksysb 障害切り分け mksysb image 0790</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>早苗復旧ではAIX 7.3の導入と起動で mksysb を確認します。早苗復旧の導入と起動では mksysb image とOSレベル表示を保守票へ記録します。早苗復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。早苗復旧の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、早苗復旧を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mksysb 障害切り分け mksysb image 0790に関する障害切り分けの前提を確認しています。defragfs バックアウト確認 log=INLINE 0803の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容は導入と起動でmksysbを用い・mksysb image とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はJFS2でdefragfsを用い・log=INLINE と内部スナップショットを確認する。</li><li>C. 表示や設定で扱う内容は導入と起動でnimadmを用い・bootlist と代替ディスク状態を確認する。</li><li>D. 表示や設定で扱う内容はデバイス管理でlsattr -El hdisk0を用い・Available とODM属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 障害切・mksyでAの記述「導入と起動でmksysbを用い、mksysb image」に対応する項目はmksysb image（障害・mksy）です。障害切に関する導入と起動の仕様は「導入と起動でmksysbを用い、mksysb image」で、確認対象はmk・障害切です。バック・defrのB:は「JFS2でdefragfsを用い、log=INLINE」を述べ、対象はバックアウト確認 log=INLIN（バッ・defr）です。バック・nimaのC:は「導入と起動でnimadmを用い、bootlist」を述べ、対象はバックアウト確認 bootlist（バッ・nima）です。運用引・lsatのD:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は運用引継ぎ Available（運用・lsat）です。「mksysb」は「導入と起動でmksysbを用い、mksysb image」を指し、mksysb imageではmk・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mksysb 障害切り分け mksysb image 0790</strong></p><p>検証目的: 導入と起動のmksysb 障害切り分け mksysb image 0790について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け070-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mksysb
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0790A
画面・出力には AIX0790A が表示され、mksysb 障害切り分け mksysb image 0790 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0790B
画面・出力には AIX0790B が表示され、mksysb 障害切り分け mksysb image 0790 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0790C
画面・出力には AIX0790C が表示され、mksysb 障害切り分け mksysb image 0790 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0790A が画面・出力に表示されること
② ステップ2 の AIX0790B が画面・出力に表示されること
③ ステップ3 の AIX0790C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0773"><h3>nimadm バックアウト確認 bootlist 0148</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>雪解採取ではAIX 7.3の導入と起動で nimadm を確認します。雪解採取の導入と起動では bootlist と代替ディスク状態を監査票へ転記します。雪解採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。雪解採取の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、雪解採取を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> nimadm バックアウト確認 bootlist 0148の技術的な意味を資料で確認するとき、lsdev -Cc adapter 監査記録 Gateway 0149との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明は導入と起動でnimadmを用い・bootlist と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はネットワークでlsdev -Cc adapterを用い・Gateway とMTU属性を確認する。</li><li>C. 管理対象との関係を表す説明はデバイス管理でrmdev -Rl ent1を用い・attribute とデバイス一覧を確認する。</li><li>D. 管理対象との関係を表す説明はネットワークでno -aを用い・Destination とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でnimadmを用い、bootlist と代替ディスク状態を確認する」に対応する項目はバックアウト確認 bootlist（バッ・nima）です。バックに関する導入と起動の仕様は「導入と起動でnimadmを用い、bootlist」で、確認対象はni・バックです。監査・lsdeのB:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は監査記録 Gateway（監査・lsde）です。構成・rmdeのC:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は構成照合 attribute（構成・rmde）です。属性・noのD:は「ネットワークでno -aを用い、Destination」を述べ、対象は属性確認 Destination（属性・no）です。「nimadm」は「導入と起動でnimadmを用い、bootlist」を指し、バックアウト確認 bootlistではni・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>nimadm バックアウト確認 bootlist 0148</strong></p><p>検証目的: 導入と起動のnimadm バックアウト確認 bootlist 0148について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認028-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; nimadm
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0148A
画面・出力には AIX0148A が表示され、nimadm バックアウト確認 bootlist 0148 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0148B
画面・出力には AIX0148B が表示され、nimadm バックアウト確認 bootlist 0148 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0148C
画面・出力には AIX0148C が表示され、nimadm バックアウト確認 bootlist 0148 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0148A が画面・出力に表示されること
② ステップ2 の AIX0148B が画面・出力に表示されること
③ ステップ3 の AIX0148C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0774"><h3>nimadm バックアウト確認 bootlist 0208</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>翠風保守ではAIX 7.3の導入と起動で nimadm を確認します。翠風保守の導入と起動では bootlist と代替ディスク状態を監査票へ転記します。翠風保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。翠風保守の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、翠風保守を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> nimadm バックアウト確認 bootlist 0208を同一分類のlsdev -Cc adapter 監査記録 Gateway 0209と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はネットワークでlsdev -Cc adapterを用い・Gateway とMTU属性を確認する。</li><li>B. 管理対象との関係を表す説明はデバイス管理でbootinfo -B hdisk0を用い・PVID とデバイス一覧を確認する。</li><li>C. 管理対象との関係を表す説明は導入と起動でnimadmを用い・bootlist と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はネットワークでno -aを用い・Destination とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でnimadmを用い、bootlist と代替ディスク状態を確認する」に対応する項目はバックアウト確認 bootlist（バッ・nima）です。バックに関する導入と起動の仕様は「導入と起動でnimadmを用い、bootlist」で、確認対象はni・バックです。監査・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は監査記録 Gateway（監査・lsde）です。変更前・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は変更前確認 PVID（変更・boot）です。属性・noのD:は「ネットワークでno -aを用い、Destination」を述べ、対象は属性確認 Destination（属性・no）です。「nimadm」は「導入と起動でnimadmを用い、bootlist」を指し、バックアウト確認 bootlistではni・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>nimadm バックアウト確認 bootlist 0208</strong></p><p>検証目的: 導入と起動のnimadm バックアウト確認 bootlist 0208について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認088-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; nimadm
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0208A
画面・出力には AIX0208A が表示され、nimadm バックアウト確認 bootlist 0208 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0208B
画面・出力には AIX0208B が表示され、nimadm バックアウト確認 bootlist 0208 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0208C
画面・出力には AIX0208C が表示され、nimadm バックアウト確認 bootlist 0208 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0208A が画面・出力に表示されること
② ステップ2 の AIX0208B が画面・出力に表示されること
③ ステップ3 の AIX0208C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0775"><h3>nimadm バックアウト確認 mksysb image 0624</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>霜月採取ではAIX 7.3の導入と起動で nimadm を確認します。霜月採取の導入と起動では mksysb image と代替ディスク状態を同じ証跡に残します。霜月採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。霜月採取の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、霜月採取を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> nimadm バックアウト確認 mksysb image 0624を同一分類のlsdev -Cc adapter 監査記録 Link Status 0625と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はネットワークでlsdev -Cc adapterを用い・Link Status とMTU属性を確認する。</li><li>B. 構成を確認する際の意味はJFS2でcrfsを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li><li>C. 構成を確認する際の意味はセキュリティでusrck -n ALLを用い・authorizations と監査設定を確認する。</li><li>D. 構成を確認する際の意味は導入と起動でnimadmを用い・mksysb image と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でnimadmを用い、mksysb image」に対応する項目はmksysb image（バッ・nima）です。バックに関する導入と起動の仕様は「導入と起動でnimadmを用い、mksysb image」で、確認対象はni・バックです。監査・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い、Link」を述べ、対象はLink Status（監査・lsde）です。起動・ファ・crfsのB:は「JFS2でcrfsを用い、ファイルシステム使用率」を述べ、対象は起動確認 ファイルシステム使用率（起動・crfs）です。運用引・usrcのC:は「セキュリティでusrck -n ALLを用い」を述べ、対象は運用引継ぎ authorizatio（運用・usrc）です。「nimadm」は「導入と起動でnimadmを用い、mksysb image」を指し、mksysb imageではni・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>nimadm バックアウト確認 mksysb image 0624</strong></p><p>検証目的: 導入と起動のnimadm バックアウト確認 mksysb image 0624について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認024-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; nimadm
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0624A
画面・出力には AIX0624A が表示され、nimadm バックアウト確認 mksysb image 0624 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0624B
画面・出力には AIX0624B が表示され、nimadm バックアウト確認 mksysb image 0624 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0624C
画面・出力には AIX0624C が表示され、nimadm バックアウト確認 mksysb image 0624 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0624A が画面・出力に表示されること
② ステップ2 の AIX0624B が画面・出力に表示されること
③ ステップ3 の AIX0624C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0776"><h3>nimadm バックアウト確認 mksysb image 0684</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>若草保守ではAIX 7.3の導入と起動で nimadm を確認します。若草保守の導入と起動では mksysb image と代替ディスク状態を同じ証跡に残します。若草保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若草保守の注意点として bootlist再設定漏れ を避けるため oslevel -s も併記します。導入保守の作業票として、若草保守を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> nimadm バックアウト確認 mksysb image 0684の技術的な意味を資料で確認するとき、lsdev -Cc adapter 監査記録 Link Status 0685との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はネットワークでlsdev -Cc adapterを用い・Link Status とMTU属性を確認する。</li><li>B. 構成を確認する際の意味はJFS2でcrfsを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li><li>C. 構成を確認する際の意味はセキュリティでlsattr -E -l sys0 -aを用い・roles と監査設定を確認する。</li><li>D. 構成を確認する際の意味は導入と起動でnimadmを用い・mksysb image と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でnimadmを用い、mksysb image」に対応する項目はmksysb image（バッ・nima）です。バックに関する導入と起動の仕様は「導入と起動でnimadmを用い、mksysb image」で、確認対象はni・バックです。監査・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い、Link」を述べ、対象はLink Status（監査・lsde）です。起動・ファ・crfsのB:は「JFS2でcrfsを用い、ファイルシステム使用率」を述べ、対象は起動確認 ファイルシステム使用率（起動・crfs）です。容量・lsatのC:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は容量確認 roles（容量・lsat）です。「nimadm」は「導入と起動でnimadmを用い、mksysb image」を指し、mksysb imageではni・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>nimadm バックアウト確認 mksysb image 0684</strong></p><p>検証目的: 導入と起動のnimadm バックアウト確認 mksysb image 0684について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動バックアウト確認084-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; nimadm
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0684A
画面・出力には AIX0684A が表示され、nimadm バックアウト確認 mksysb image 0684 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0684B
画面・出力には AIX0684B が表示され、nimadm バックアウト確認 mksysb image 0684 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0684C
画面・出力には AIX0684C が表示され、nimadm バックアウト確認 mksysb image 0684 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0684A が画面・出力に表示されること
② ステップ2 の AIX0684B が画面・出力に表示されること
③ ステップ3 の AIX0684C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0777"><h3>nimadm 変更後確認 bootlist 0337</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>初霜変更ではAIX 7.3の導入と起動で nimadm を確認します。初霜変更の導入と起動では bootlist と起動デバイス設定を採取票へ記録します。初霜変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。初霜変更の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、初霜変更を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「nimadm 変更後確認 bootlist 0337」を「lsdev -Cc adapter 障害切り分け Destination 0338」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はネットワークでlsdev -Cc adapterを用い・Destination とアダプター一覧を確認する。</li><li>B. 保守作業で参照する機能は導入と起動でnimadmを用い・bootlist と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はデバイス管理でbootinfo -B hdisk0を用い・PVID とODM属性を確認する。</li><li>D. 保守作業で参照する機能はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でnimadmを用い、bootlist と起動デバイス設定を確認する」に対応する項目は変更後確認 bootlist（変更・nima）です。変更後に関する導入と起動の仕様は「導入と起動でnimadmを用い、bootlist」で、確認対象はni・変更後です。障害切・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は障害切り分け Destination（障害・lsde）です。状態・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・boot）です。監査・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsat）です。「nimadm」は「導入と起動でnimadmを用い、bootlist」を指し、変更後確認 bootlistではni・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>nimadm 変更後確認 bootlist 0337</strong></p><p>検証目的: 導入と起動のnimadm 変更後確認 bootlist 0337について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認097-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; nimadm
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0337A
画面・出力には AIX0337A が表示され、nimadm 変更後確認 bootlist 0337 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0337B
画面・出力には AIX0337B が表示され、nimadm 変更後確認 bootlist 0337 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0337C
画面・出力には AIX0337C が表示され、nimadm 変更後確認 bootlist 0337 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0337A が画面・出力に表示されること
② ステップ2 の AIX0337B が画面・出力に表示されること
③ ステップ3 の AIX0337C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0778"><h3>nimadm 変更後確認 mksysb image 0813</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>月影変更ではAIX 7.3の導入と起動で nimadm を確認します。月影変更の導入と起動では mksysb image と起動デバイス設定を判定票へ残します。月影変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。月影変更の注意点として altinst_rootvgの誤varyon を避けるため oslevel -s も併記します。導入保守の作業票として、月影変更を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> nimadm 変更後確認 mksysb image 0813を保守記録に説明する必要があります。lscfg -vl ent0 バックアウト確認 Available 0839と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割は導入と起動でnimadmを用い・mksysb image と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はデバイス管理でlscfg -vl ent0を用い・Available とODM属性を確認する。</li><li>C. 運用時に利用する技術的役割はネットワークでlsdev -Cc adapterを用い・Gateway とMTU属性を確認する。</li><li>D. 運用時に利用する技術的役割はSRCとログでstartsrc -s syslogdを用い・Status とエラーログ一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更後・nimaでAの記述「導入と起動でnimadmを用い、mksysb image」に対応する項目はmksysb image（変更・nima）です。変更後に関する導入と起動の仕様は「導入と起動でnimadmを用い、mksysb image」で、確認対象はni・変更後です。バック・lscfのB:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象はバックアウト確認 Available（バッ・lscf）です。監査・lsdeのC:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は監査記録 Gateway（監査・lsde）です。属性・starのD:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は属性確認 Status（属性・star）です。「nimadm」は「導入と起動でnimadmを用い、mksysb image」を指し、mksysb imageではni・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>nimadm 変更後確認 mksysb image 0813</strong></p><p>検証目的: 導入と起動のnimadm 変更後確認 mksysb image 0813について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更後確認093-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; nimadm
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0813A
画面・出力には AIX0813A が表示され、nimadm 変更後確認 mksysb image 0813 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0813B
画面・出力には AIX0813B が表示され、nimadm 変更後確認 mksysb image 0813 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mksysb image を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0813C
画面・出力には AIX0813C が表示され、nimadm 変更後確認 mksysb image 0813 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0813A が画面・出力に表示されること
② ステップ2 の AIX0813B が画面・出力に表示されること
③ ステップ3 の AIX0813C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0779"><h3>nimadm 属性確認 EFIX LABEL 0654</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>星霜判定ではAIX 7.3の導入と起動で nimadm を確認します。星霜判定の導入と起動では EFIX LABEL とOSレベル表示を変更票へ記録します。星霜判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。星霜判定の注意点として mksysbレベル不一致 を避けるため oslevel -s も併記します。導入保守の作業票として、星霜判定を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> nimadm 属性確認 EFIX LABEL 0654に関する障害切り分けの前提を確認しています。lsdev -Cc adapter 状態確認 Destination 0655の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはネットワークでlsdev -Cc adapterを用い・Destinationである。</li><li>B. 機能の説明としてはJFS2でcrfsを用い・isnapshot とログデバイス設定を確認する。</li><li>C. 機能の説明としてはセキュリティでusrck -n ALLを用い・authorizations とロール一覧を確認する。</li><li>D. 機能の説明としては導入と起動でnimadmを用い・EFIX LABEL とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でnimadmを用い、EFIX LABEL とOSレベル表示を確認する」に対応する項目はEFIX LABEL（属性・nima）です。属性に関する導入と起動の仕様は「導入と起動でnimadmを用い、EFIX LABEL」で、確認対象はni・属性です。状態・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は状態確認 Destination（状態・lsde）です。障害切・crfsのB:は「JFS2でcrfsを用い、isnapshot」を述べ、対象は障害切り分け isnapshot（障害・crfs）です。構成・usrcのC:は「セキュリティでusrck -n ALLを用い」を述べ、対象は構成照合 authorization（構成・usrc）です。「nimadm」は「導入と起動でnimadmを用い、EFIX LABEL」を指し、EFIX LABELではni・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>nimadm 属性確認 EFIX LABEL 0654</strong></p><p>検証目的: 導入と起動のnimadm 属性確認 EFIX LABEL 0654について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認054-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; nimadm
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0654A
画面・出力には AIX0654A が表示され、nimadm 属性確認 EFIX LABEL 0654 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0654B
画面・出力には AIX0654B が表示され、nimadm 属性確認 EFIX LABEL 0654 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。EFIX LABEL を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0654C
画面・出力には AIX0654C が表示され、nimadm 属性確認 EFIX LABEL 0654 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0654A が画面・出力に表示されること
② ステップ2 の AIX0654B が画面・出力に表示されること
③ ステップ3 の AIX0654C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0780"><h3>nimadm 属性確認 Technology Level 0178</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>潮騒判定ではAIX 7.3の導入と起動で nimadm を確認します。潮騒判定の導入と起動では Technology Level とOSレベル表示を保守票へ記録します。潮騒判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。潮騒判定の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、潮騒判定を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> nimadm 属性確認 Technology Level 0178の役割を調べています。lsdev -Cc adapter 状態確認 Media Speedの説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容は導入と起動でnimadmを用い・Technology Level とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はネットワークでlsdev -Cc adapterを用い・Media Speed Runningである。</li><li>C. 表示や設定で扱う内容はデバイス管理でbootinfo -B hdisk0を用い・Availableである。</li><li>D. 表示や設定で扱う内容はネットワークでno -aを用い・Link Status とEthernet統計を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でnimadmを用い、Technology Level」に対応する項目はTechnology Level（属性・nima）です。属性に関する導入と起動の仕様は「導入と起動でnimadmを用い、Technology Level」で、確認対象はni・属性です。状態・lsdeのB:は「ネットワークでlsdev -Cc adapterを用い、Media」を述べ、対象はSpeed Running（状態・lsde）です。容量・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は容量確認 Available（容量・boot）です。バック・noのD:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（バッ・no）です。「nimadm」は「導入と起動でnimadmを用い、Technology Level」を指し、Technology Levelではni・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>nimadm 属性確認 Technology Level 0178</strong></p><p>検証目的: 導入と起動のnimadm 属性確認 Technology Level 0178について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動属性確認058-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; nimadm
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0178A
画面・出力には AIX0178A が表示され、nimadm 属性確認 Technology Level 0178 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0178B
画面・出力には AIX0178B が表示され、nimadm 属性確認 Technology Level 0178 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0178C
画面・出力には AIX0178C が表示され、nimadm 属性確認 Technology Level 0178 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0178A が画面・出力に表示されること
② ステップ2 の AIX0178B が画面・出力に表示されること
③ ステップ3 の AIX0178C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0781"><h3>nimadm 運用引継ぎ Technology Level 0495</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>岩清水確認ではAIX 7.3の導入と起動で nimadm を確認します。岩清水確認の導入と起動では Technology Level とfileset一覧を作業票へ保管します。岩清水確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。岩清水確認の注意点として bosboot失敗後の再起動 を避けるため oslevel -s も併記します。導入保守の作業票として、岩清水確認を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> nimadm 運用引継ぎ Technology Level 0495の設定や表示を読む前に役割を確認します。lsdev -Cc adapter 容量確認 Link Status 0496ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはネットワークでlsdev -Cc adapterを用い・Link Status と経路表を確認する。</li><li>B. 状態を読み取るための働きは導入と起動でnimadmを用い・Technology Level とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはデバイス管理でrmdev -Rl ent1を用い・microcode level と診断対象表示を確認する。</li><li>D. 状態を読み取るための働きはセキュリティでusrck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「導入と起動でnimadmを用い、Technology Level」に対応する項目はTechnology Level（運用・nima）です。運用引に関する導入と起動の仕様は「導入と起動でnimadmを用い、Technology Level」で、確認対象はni・運用引です。容量・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い、Link」を述べ、対象はLink Status（容量・lsde）です。変更後・rmdeのC:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象はmicrocode level（変更・rmde）です。性能・usrcのD:は「セキュリティでusrck -n ALLを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・usrc）です。「nimadm」は「導入と起動でnimadmを用い、Technology Level」を指し、Technology Levelではni・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>nimadm 運用引継ぎ Technology Level 0495</strong></p><p>検証目的: 導入と起動のnimadm 運用引継ぎ Technology Level 0495について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ015-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; nimadm
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0495A
画面・出力には AIX0495A が表示され、nimadm 運用引継ぎ Technology Level 0495 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0495B
画面・出力には AIX0495B が表示され、nimadm 運用引継ぎ Technology Level 0495 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0495C
画面・出力には AIX0495C が表示され、nimadm 運用引継ぎ Technology Level 0495 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0495A が画面・出力に表示されること
② ステップ2 の AIX0495B が画面・出力に表示されること
③ ステップ3 の AIX0495C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0782"><h3>nimadm 運用引継ぎ altinst_rootvg 0019</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>山吹確認ではAIX 7.3の導入と起動で nimadm を確認します。山吹確認の導入と起動では altinst_rootvg とfileset一覧を点検票へ整理します。山吹確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。山吹確認の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、山吹確認を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> nimadm 運用引継ぎ altinst_rootvg 0019について構成や状態を確認します。lsdev -Cc adapter 容量確認 Gateway 0020ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはネットワークでlsdev -Cc adapterを用い・Gateway と経路表を確認する。lsdev -Cc adapter 容量確認 Gateway 0020固有の属性も確認対象に含める。</li><li>B. 対象資源に対する働きはデバイス管理でrmdev -Rl ent1を用い・PVID と診断対象表示を確認する。</li><li>C. 対象資源に対する働きはネットワークでno -aを用い・Destination と経路表を確認する。</li><li>D. 対象資源に対する働きは導入と起動でnimadmを用い・altinst_rootvg とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「導入と起動でnimadmを用い、altinst_rootvg」に対応する項目は運用引継ぎ altinst_root（運用・nima）です。導入と起動の仕様は「導入と起動でnimadmを用い、altinst_rootvg」で、確認対象はni・運用引です。容量・lsdeのA:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は容量確認 Gateway（容量・lsde）です。変更後・rmdeのB:は「デバイス管理でrmdev -Rl ent1を用い、PVID」を述べ、対象は変更後確認 PVID（変更・rmde）です。構成・noのC:は「ネットワークでno -aを用い、Destination」を述べ、対象は構成照合 Destination（構成・no）です。「nimadm」は「導入と起動でnimadmを用い、altinst_rootvg」を指し、運用引継ぎ altinst_rootではni・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>nimadm 運用引継ぎ altinst_rootvg 0019</strong></p><p>検証目的: 導入と起動のnimadm 運用引継ぎ altinst_rootvg 0019について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動運用引継ぎ019-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; nimadm
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0019A
画面・出力には AIX0019A が表示され、nimadm 運用引継ぎ altinst_rootvg 0019 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0019B
画面・出力には AIX0019B が表示され、nimadm 運用引継ぎ altinst_rootvg 0019 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0019C
画面・出力には AIX0019C が表示され、nimadm 運用引継ぎ altinst_rootvg 0019 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0019A が画面・出力に表示されること
② ステップ2 の AIX0019B が画面・出力に表示されること
③ ステップ3 の AIX0019C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0783"><h3>oslevel -s 変更前確認 bootlist 0526</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>朝凪照合ではAIX 7.3の導入と起動で oslevel -s を確認します。朝凪照合の導入と起動では bootlist とOSレベル表示を保守票へ記録します。朝凪照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。朝凪照合の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、朝凪照合を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> oslevel -s 変更前確認 bootlist 0526に関する障害切り分けの前提を確認しています。ifconfig en0 変更後確認 Gateway 0527の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容は導入と起動でoslevel -sを用い・bootlist とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はネットワークでifconfig en0を用い・Gateway とEthernet統計を確認する。</li><li>C. 表示や設定で扱う内容はデバイス管理でbootinfo -B hdisk0を用い・attributeである。</li><li>D. 表示や設定で扱う内容はセキュリティでlsattr -E -l sys0 -aを用い・authorizationsである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でoslevel -sを用い、bootlist とOSレベル表示を確認する」に対応する項目は変更前確認 bootlist（変更・osle）です。変更前に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、bootlist」で、確認対象はos・変更前です。変更後・ifcoのB:は「ネットワークでifconfig en0を用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・ifco）です。起動・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は起動確認 attribute（起動・boot）です。障害切・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は障害切り分け authorizati（障害・lsat）です。「oslevel -s」は「導入と起動でoslevel -sを用い、bootlist」を指し、変更前確認 bootlistではos・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>oslevel -s 変更前確認 bootlist 0526</strong></p><p>検証目的: 導入と起動のoslevel -s 変更前確認 bootlist 0526について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認046-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0526A
画面・出力には AIX0526A が表示され、oslevel -s 変更前確認 bootlist 0526 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0526B
画面・出力には AIX0526B が表示され、oslevel -s 変更前確認 bootlist 0526 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0526C
画面・出力には AIX0526C が表示され、oslevel -s 変更前確認 bootlist 0526 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0526A が画面・出力に表示されること
② ステップ2 の AIX0526B が画面・出力に表示されること
③ ステップ3 の AIX0526C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0784"><h3>oslevel -s 変更前確認 bootlist 0586</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>陽炎点検ではAIX 7.3の導入と起動で oslevel -s を確認します。陽炎点検の導入と起動では bootlist とOSレベル表示を保守票へ記録します。陽炎点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。陽炎点検の注意点として mksysbレベル不一致 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、陽炎点検を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> oslevel -s 変更前確認 bootlist 0586の役割を調べています。ifconfig en0 変更後確認 Gateway 0587の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はネットワークでifconfig en0を用い・Gateway とEthernet統計を確認する。</li><li>B. 表示や設定で扱う内容はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>C. 表示や設定で扱う内容はセキュリティでlsroleを用い・roles とロール一覧を確認する。</li><li>D. 表示や設定で扱う内容は導入と起動でoslevel -sを用い・bootlist とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「導入と起動でoslevel -sを用い、bootlist とOSレベル表示を確認する」に対応する項目は変更前確認 bootlist（変更・osle）です。変更前に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、bootlist」で、確認対象はos・変更前です。変更後・ifcoのA:は「ネットワークでifconfig en0を用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・ifco）です。一覧・詳細・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は一覧確認 詳細表示（一覧・lsvg）です。バック・lsroのC:は「セキュリティでlsroleを用い、roles とロール一覧を確認する」を述べ、対象はバックアウト確認 roles（バッ・lsro）です。「oslevel -s」は「導入と起動でoslevel -sを用い、bootlist」を指し、変更前確認 bootlistではos・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>oslevel -s 変更前確認 bootlist 0586</strong></p><p>検証目的: 導入と起動のoslevel -s 変更前確認 bootlist 0586について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認106-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0586A
画面・出力には AIX0586A が表示され、oslevel -s 変更前確認 bootlist 0586 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0586B
画面・出力には AIX0586B が表示され、oslevel -s 変更前確認 bootlist 0586 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。bootlist を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0586C
画面・出力には AIX0586C が表示され、oslevel -s 変更前確認 bootlist 0586 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0586A が画面・出力に表示されること
② ステップ2 の AIX0586B が画面・出力に表示されること
③ ステップ3 の AIX0586C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0785"><h3>oslevel -s 変更前確認 fileset level 0050</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>桜雲照合ではAIX 7.3の導入と起動で oslevel -s を確認します。桜雲照合の導入と起動では fileset level とOSレベル表示を確認票へ整理します。桜雲照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。桜雲照合の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、桜雲照合を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> oslevel -s 変更前確認 fileset level 0050の役割を調べています。ifconfig en0 変更後確認 MTU 0051の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割は導入と起動でoslevel -sを用い・fileset level とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 障害切り分けに用いる役割はネットワークでifconfig en0を用い・MTU とEthernet統計を確認する。</li><li>C. 障害切り分けに用いる役割はデバイス管理でbootinfo -B hdisk0を用い・Availableである。bootinfo -B hdisk0 起動確認 Available固有の属性も確認対象に含める。</li><li>D. 障害切り分けに用いる役割はネットワークでroute -n getを用い・Media Speed Runningである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「導入と起動でoslevel -sを用い、fileset level」に対応する項目はfileset level（変更・osle）です。導入と起動の仕様は「導入と起動でoslevel -sを用い、fileset level」で、確認対象はos・変更前です。変更後・ifcoのB:は「ネットワークでifconfig en0を用い、MTU」を述べ、対象は変更後確認 MTU（変更・ifco）です。起動・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は起動確認 Available（起動・boot）です。容量・routのD:は「ネットワークでroute -n getを用い、Media」を述べ、対象はSpeed Running（容量・rout）です。「oslevel -s」は「導入と起動でoslevel -sを用い、fileset level」を指し、fileset levelではos・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>oslevel -s 変更前確認 fileset level 0050</strong></p><p>検証目的: 導入と起動のoslevel -s 変更前確認 fileset level 0050について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認050-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0050A
画面・出力には AIX0050A が表示され、oslevel -s 変更前確認 fileset level 0050 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0050B
画面・出力には AIX0050B が表示され、oslevel -s 変更前確認 fileset level 0050 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0050C
画面・出力には AIX0050C が表示され、oslevel -s 変更前確認 fileset level 0050 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0050A が画面・出力に表示されること
② ステップ2 の AIX0050B が画面・出力に表示されること
③ ステップ3 の AIX0050C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0786"><h3>oslevel -s 変更前確認 fileset level 0110</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 上級</p><p>早苗点検ではAIX 7.3の導入と起動で oslevel -s を確認します。早苗点検の導入と起動では fileset level とOSレベル表示を確認票へ整理します。早苗点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。早苗点検の注意点として mksysbレベル不一致 を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、早苗点検を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> oslevel -s 変更前確認 fileset level 0110に関する障害切り分けの前提を確認しています。ifconfig en0 変更後確認 MTU 0111の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はネットワークでifconfig en0を用い・MTU とEthernet統計を確認する。</li><li>B. 障害切り分けに用いる役割は導入と起動でoslevel -sを用い・fileset level とOSレベル表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割はデバイス管理でlsmpio -l hdisk0を用い・location codeである。</li><li>D. 障害切り分けに用いる役割はネットワークでcfgmgrを用い・MTU とEthernet統計を確認する。cfgmgr 性能確認 MTU 0723固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「導入と起動でoslevel -sを用い、fileset level」に対応する項目はfileset level（変更・osle）です。変更前に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、fileset level」で、確認対象はos・変更前です。変更後・ifcoのA:は「ネットワークでifconfig en0を用い、MTU」を述べ、対象は変更後確認 MTU（変更・ifco）です。属性・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はlocation code（属性・lsmp）です。性能・cfgmのD:は「ネットワークでcfgmgrを用い、MTU」を述べ、対象は性能確認 MTU（性能・cfgm）です。「oslevel -s」は「導入と起動でoslevel -sを用い、fileset level」を指し、fileset levelではos・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>oslevel -s 変更前確認 fileset level 0110</strong></p><p>検証目的: 導入と起動のoslevel -s 変更前確認 fileset level 0110について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動変更前確認110-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0110A
画面・出力には AIX0110A が表示され、oslevel -s 変更前確認 fileset level 0110 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0110B
画面・出力には AIX0110B が表示され、oslevel -s 変更前確認 fileset level 0110 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0110C
画面・出力には AIX0110C が表示され、oslevel -s 変更前確認 fileset level 0110 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0110A が画面・出力に表示されること
② ステップ2 の AIX0110B が画面・出力に表示されること
③ ステップ3 の AIX0110C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0787"><h3>oslevel -s 容量確認 Technology Level 0556</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>若潮照合ではAIX 7.3の導入と起動で oslevel -s を確認します。若潮照合の導入と起動では Technology Level と代替ディスク状態を監査票へ転記します。若潮照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若潮照合の注意点として bootlist再設定漏れ を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、若潮照合を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> oslevel -s 容量確認 Technology Level 0556の技術的な意味を資料で確認するとき、ifconfig en0 性能確認 Media Speed Running 0557との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はネットワークでifconfig en0を用い・Media Speed Running とMTU属性を確認する。</li><li>B. 管理対象との関係を表す説明はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>C. 管理対象との関係を表す説明は導入と起動でoslevel -sを用い・Technology Level と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はセキュリティでlsroleを用い・roles と監査設定を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でoslevel -sを用い、Technology Level」に対応する項目はTechnology Level（容量・osle）です。容量に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、Technology」で、確認対象はos・容量です。性能・ifcoのA:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（性能・ifco）です。復旧前・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は復旧前確認 再開位置（復旧・lsvg）です。属性・lsroのD:は「セキュリティでlsroleを用い、roles と監査設定を確認する」を述べ、対象は属性確認 roles（属性・lsro）です。「oslevel -s」は「導入と起動でoslevel -sを用い、Technology」を指し、Technology Levelではos・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>oslevel -s 容量確認 Technology Level 0556</strong></p><p>検証目的: 導入と起動のoslevel -s 容量確認 Technology Level 0556について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認076-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0556A
画面・出力には AIX0556A が表示され、oslevel -s 容量確認 Technology Level 0556 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0556B
画面・出力には AIX0556B が表示され、oslevel -s 容量確認 Technology Level 0556 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Technology Level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0556C
画面・出力には AIX0556C が表示され、oslevel -s 容量確認 Technology Level 0556 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0556A が画面・出力に表示されること
② ステップ2 の AIX0556B が画面・出力に表示されること
③ ステップ3 の AIX0556C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0788"><h3>oslevel -s 容量確認 altinst_rootvg 0080</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>青葉点検ではAIX 7.3の導入と起動で oslevel -s を確認します。青葉点検の導入と起動では altinst_rootvg と代替ディスク状態を引継ぎ票へ保管します。青葉点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。青葉点検の注意点として bootlist再設定漏れ を避けるため bootlist -m normal -o も併記します。導入保守の作業票として、青葉点検を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> oslevel -s 容量確認 altinst_rootvg 0080を同一分類のifconfig en0 性能確認 EtherChannel 0081と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はネットワークでifconfig en0を用い・EtherChannel とMTU属性を確認する。</li><li>B. コマンドまたは機能の用途はデバイス管理でlsmpio -l hdisk0を用い・path status とデバイス一覧を確認する。</li><li>C. コマンドまたは機能の用途はネットワークでroute -n getを用い・Gateway とMTU属性を確認する。</li><li>D. コマンドまたは機能の用途は導入と起動でoslevel -sを用い・altinst_rootvg と代替ディスク状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「導入と起動でoslevel -sを用い、altinst_rootvg」に対応する項目は容量確認 altinst_rootv（容量・osle）です。容量に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、altinst_rootvg」で、確認対象はos・容量です。性能・ifcoのA:は「ネットワークでifconfig en0を用い」を述べ、対象は性能確認 EtherChannel（性能・ifco）です。バック・lsmpのB:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（バッ・lsmp）です。変更前・routのC:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は変更前確認 Gateway（変更・rout）です。「oslevel -s」は「導入と起動でoslevel -sを用い、altinst_rootvg」を指し、容量確認 altinst_rootvではos・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>oslevel -s 容量確認 altinst_rootvg 0080</strong></p><p>検証目的: 導入と起動のoslevel -s 容量確認 altinst_rootvg 0080について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動容量確認080-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0080A
画面・出力には AIX0080A が表示され、oslevel -s 容量確認 altinst_rootvg 0080 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0080B
画面・出力には AIX0080B が表示され、oslevel -s 容量確認 altinst_rootvg 0080 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslpp -L bos.rte
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0080C
画面・出力には AIX0080C が表示され、oslevel -s 容量確認 altinst_rootvg 0080 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0080A が画面・出力に表示されること
② ステップ2 の AIX0080B が画面・出力に表示されること
③ ステップ3 の AIX0080C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0789"><h3>oslevel -s 起動確認 fileset level 0367</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 初級</p><p>夕凪記録ではAIX 7.3の導入と起動で oslevel -s を確認します。夕凪記録の導入と起動では fileset level とfileset一覧を点検票へ整理します。夕凪記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。夕凪記録の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、夕凪記録を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> oslevel -s 起動確認 fileset level 0367の設定や表示を読む前に役割を確認します。ifconfig en0 属性確認 Media Speed Running 0368ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはネットワークでifconfig en0を用い・Media Speed Running と経路表を確認する。</li><li>B. 対象資源に対する働きはデバイス管理でbootinfo -B hdisk0を用い・Available と診断対象表示を確認する。</li><li>C. 対象資源に対する働きは導入と起動でoslevel -sを用い・fileset level とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「導入と起動でoslevel -sを用い、fileset level」に対応する項目はfileset level（起動・osle）です。起動に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、fileset level」で、確認対象はos・起動です。属性・ifcoのA:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（属性・ifco）です。監査・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は監査記録 Available（監査・boot）です。状態・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsat）です。「oslevel -s」は「導入と起動でoslevel -sを用い、fileset level」を指し、fileset levelではos・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>oslevel -s 起動確認 fileset level 0367</strong></p><p>検証目的: 導入と起動のoslevel -s 起動確認 fileset level 0367について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認007-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0367A
画面・出力には AIX0367A が表示され、oslevel -s 起動確認 fileset level 0367 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0367B
画面・出力には AIX0367B が表示され、oslevel -s 起動確認 fileset level 0367 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0367C
画面・出力には AIX0367C が表示され、oslevel -s 起動確認 fileset level 0367 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0367A が画面・出力に表示されること
② ステップ2 の AIX0367B が画面・出力に表示されること
③ ステップ3 の AIX0367C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0790"><h3>oslevel -s 起動確認 fileset level 0427</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>風花評価ではAIX 7.3の導入と起動で oslevel -s を確認します。風花評価の導入と起動では fileset level とfileset一覧を点検票へ整理します。風花評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。風花評価の注意点として bosboot失敗後の再起動 を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、風花評価を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> oslevel -s 起動確認 fileset level 0427について構成や状態を確認します。ifconfig en0 属性確認 Media Speed Running 0428ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはネットワークでifconfig en0を用い・Media Speed Running と経路表を確認する。</li><li>B. 対象資源に対する働きは導入と起動でoslevel -sを用い・fileset level とfileset一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはデバイス管理でlsmpio -l hdisk0を用い・location code と診断対象表示を確認する。</li><li>D. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「導入と起動でoslevel -sを用い、fileset level」に対応する項目はfileset level（起動・osle）です。起動に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、fileset level」で、確認対象はos・起動です。属性・ifcoのA:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（属性・ifco）です。運用引・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はlocation code（運用・lsmp）です。状態・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsat）です。「oslevel -s」は「導入と起動でoslevel -sを用い、fileset level」を指し、fileset levelではos・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>oslevel -s 起動確認 fileset level 0427</strong></p><p>検証目的: 導入と起動のoslevel -s 起動確認 fileset level 0427について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動起動確認067-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0427A
画面・出力には AIX0427A が表示され、oslevel -s 起動確認 fileset level 0427 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0427B
画面・出力には AIX0427B が表示され、oslevel -s 起動確認 fileset level 0427 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fileset level を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0427C
画面・出力には AIX0427C が表示され、oslevel -s 起動確認 fileset level 0427 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0427A が画面・出力に表示されること
② ステップ2 の AIX0427B が画面・出力に表示されること
③ ステップ3 の AIX0427C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0791"><h3>oslevel -s 障害切り分け altinst_rootvg 0397</h3><p class="kb-meta">分類: 導入と起動 ・ 難易度: 中級</p><p>冬晴記録ではAIX 7.3の導入と起動で oslevel -s を確認します。冬晴記録の導入と起動では altinst_rootvg と起動デバイス設定を採取票へ記録します。冬晴記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。冬晴記録の注意点として altinst_rootvgの誤varyon を避けるため lslpp -L bos.rte も併記します。導入保守の作業票として、冬晴記録を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> oslevel -s 障害切り分け altinst_rootvg 0397を保守記録に説明する必要があります。ifconfig en0 バックアウト確認 Gateway 0398と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はネットワークでifconfig en0を用い・Gateway とアダプター一覧を確認する。ifconfig en0 バックアウト確認 Gateway 0398固有の属性も確認対象に含める。</li><li>B. 保守作業で参照する機能はデバイス管理でbootinfo -B hdisk0を用い・PVID とODM属性を確認する。</li><li>C. 保守作業で参照する機能は導入と起動でoslevel -sを用い・altinst_rootvg と起動デバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「導入と起動でoslevel -sを用い、altinst_rootvg」に対応する項目は障害切り分け altinst_roo（障害・osle）です。障害切に関する導入と起動の仕様は「導入と起動でoslevel -sを用い、altinst_rootvg」で、確認対象はos・障害切です。バック・ifcoのA:は「ネットワークでifconfig en0を用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・ifco）です。状態・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・boot）です。監査・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsat）です。「oslevel -s」は「導入と起動でoslevel -sを用い、altinst_rootvg」を指し、障害切り分け altinst_rooではos・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>oslevel -s 障害切り分け altinst_rootvg 0397</strong></p><p>検証目的: 導入と起動のoslevel -s 障害切り分け altinst_rootvg 0397について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=導入と起動障害切り分け037-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
7300-02-01-2346
確認コード AIX0397A
画面・出力には AIX0397A が表示され、oslevel -s 障害切り分け altinst_rootvg 0397 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootlist -m normal -o
→ Enter を押す
［画面・出力］
Fileset                      Level  State  Description
bos.rte                   7.3.2.1    C     Base Operating System Runtime
確認コード AIX0397B
画面・出力には AIX0397B が表示され、oslevel -s 障害切り分け altinst_rootvg 0397 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。altinst_rootvg を読むため、導入と起動 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; oslevel -s
→ Enter を押す
［画面・出力］
Boot device list
hdisk0 blv=hd5 pathid=0
hdisk1 blv=hd5 pathid=1
確認コード AIX0397C
画面・出力には AIX0397C が表示され、oslevel -s 障害切り分け altinst_rootvg 0397 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0397A が画面・出力に表示されること
② ステップ2 の AIX0397B が画面・出力に表示されること
③ ステップ3 の AIX0397C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


## 性能監視


<section class="kb-item" id="c01-i0792"><h3>chdev 変更前確認 識別値</h3><p class="kb-meta">分類: 性能監視 ・ 難易度: 初級</p><p>AIX 7.3 の 性能監視 で扱う「chdev 変更前確認 識別値」は、デバイス属性を変更する管理コマンドを変更前確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-007を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chdev 変更前確認 識別値の設定や表示を読む前に役割を確認します。lscfg 復旧前確認 障害記録ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的は構成済みデバイスと VPD を表示するコマンドである。</li><li>B. 一次資料が示す主目的は性能管理でtopas -Dを用い・fre とAME統計を確認する。</li><li>C. 一次資料が示す主目的はSRCとログでsyslog_ssw -rを用い・TIMESTAMP とsyslog設定変換を確認する。</li><li>D. 一次資料が示す主目的はデバイス属性を変更する管理コマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「デバイス属性を変更する管理コマンドである」に対応する項目は変更前確認 識別値（変更・chde）です。性能監視の仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・変更前です。復旧前・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は復旧前確認 障害記録（復旧・lscf）です。監査・topaのB:は「性能管理でtopas -Dを用い、fre とAME統計を確認する」を述べ、対象は監査記録 fre（監査・topa）です。障害切・syslのC:は「SRCとログでsyslog_ssw -rを用い、TIMESTAMP」を述べ、対象は障害切り分け TIMESTAMP（障害・sysl）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、変更前確認 識別値ではch・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev 変更前確認 識別値</strong></p><p>検証目的: 性能監視のchdev 変更前確認 識別値について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、性能監視の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lslv hd4
→ Enter を押す
［画面・出力］
LOGICAL VOLUME: hd4
VOLUME GROUP: rootvg
LV STATE: opened/syncd
TYPE: jfs2
画面・出力には LOGICAL が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsps -a
→ Enter を押す
［画面・出力］
Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
画面・出力には Page が含まれ、chdev 変更前確認 識別値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、停止中の論理ボリューム見落としを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; smit lsps
→ Enter を押す
［画面・出力］
SMIT fast path: lsps
Command to run: lsps -a
Paging space list displayed
画面・出力には SMIT が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の LOGICAL が画面・出力に表示されること
② ステップ2 の Page が画面・出力に表示されること
③ ステップ3 の SMIT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0793"><h3>chdev 状態判定 対象ノード</h3><p class="kb-meta">分類: 性能監視 ・ 難易度: 中級</p><p>AIX 7.3 の 性能監視 で扱う「chdev 状態判定 対象ノード」は、デバイス属性を変更する管理コマンドを状態判定の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-047を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chdev 状態判定 対象ノードの設定や表示を読む前に役割を確認します。lscfg 属性照合 時刻情報ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはデバイス属性を変更する管理コマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. 状態を読み取るための働きは構成済みデバイスと VPD を表示するコマンドである。</li><li>C. 状態を読み取るための働きはLVMでchlvを用い・VG STATE とミラーコピー状態を確認する。</li><li>D. 状態を読み取るための働きは性能管理でtopas -Dを用い・Busy% とtopasディスク表示を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「デバイス属性を変更する管理コマンドである」に対応する項目は状態判定 対象ノード（状態・chde）です。性能監視の仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・状態・対象です。属性・時刻・lscfのB:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は属性照合 時刻情報（属性・lscf）です。属性・chlvのC:は「LVMでchlvを用い、VG STATE」を述べ、対象はVG STATE（属性・chlv）です。容量・topaのD:は「性能管理でtopas -Dを用い、Busy%」を述べ、対象は容量確認 Busy%（容量・topa）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、状態判定 対象ノードではch・状態・対象に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev 状態判定 対象ノード</strong></p><p>検証目的: 性能監視のchdev 状態判定 対象ノードについて、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、性能監視の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lslv hd4
→ Enter を押す
［画面・出力］
LOGICAL VOLUME: hd4
VOLUME GROUP: rootvg
LV STATE: opened/syncd
TYPE: jfs2
画面・出力には LOGICAL が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsps -a
→ Enter を押す
［画面・出力］
Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
画面・出力には Page が含まれ、chdev 状態判定 対象ノードの証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、停止中の論理ボリューム見落としを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; smit lsps
→ Enter を押す
［画面・出力］
SMIT fast path: lsps
Command to run: lsps -a
Paging space list displayed
画面・出力には SMIT が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の LOGICAL が画面・出力に表示されること
② ステップ2 の Page が画面・出力に表示されること
③ ステップ3 の SMIT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0794"><h3>errpt 属性照合 ログ採取</h3><p class="kb-meta">分類: 性能監視 ・ 難易度: 中級</p><p>AIX 7.3 の 性能監視 で扱う「errpt 属性照合 ログ採取」は、AIX エラーログから要約または詳細レポートを生成するコマンドを属性照合の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-055を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> errpt 属性照合 ログ採取の設定や表示を読む前に役割を確認します。lsattr 障害切り分け 実行結果ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はデバイスや sys0 などの属性値を表示するコマンドである。</li><li>B. 一次資料が示す主目的はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。</li><li>C. 一次資料が示す主目的は性能管理でsvmon -Gを用い・fre とtopasディスク表示を確認する。</li><li>D. 一次資料が示す主目的はAIX エラーログから要約または詳細レポートを生成するコマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は属性照合 ログ採取（属性・errp）です。性能監視の仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・属性・ログです。障害切・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は障害切り分け 実行結果（障害・lsat）です。運用引・lslvのB:は「LVMでlslvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・lslv）です。障害切・svmoのC:は「性能管理でsvmon -Gを用い、fre」を述べ、対象は障害切り分け fre（障害・svmo）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、属性照合 ログ採取ではer・属性・ログに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>errpt 属性照合 ログ採取</strong></p><p>検証目的: 性能監視のerrpt 属性照合 ログ採取について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、性能監視の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; vmstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: lcpu=2 mem=1024MB tmem=512MB ent=0.40 mmode=dedicated-E
 r b avm fre csz cfr dxm ci co pi po in sy cs
画面・出力には System が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lparstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
%user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
画面・出力には System が含まれ、errpt 属性照合 ログ採取の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ボリュームグループの取り違えを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; topas
→ Enter を押す
［画面・出力］
Topas Monitor for host: aixhost
CPU User% Kern% Wait% Idle%
AME TMEM,MB 512 CMEM,MB 114 EF[T/A] 2.0/1.5
画面・出力には Topas が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の System が画面・出力に表示されること
② ステップ2 の System が画面・出力に表示されること
③ ステップ3 の Topas が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0795"><h3>errpt 復旧前確認 再読込</h3><p class="kb-meta">分類: 性能監視 ・ 難易度: 初級</p><p>AIX 7.3 の 性能監視 で扱う「errpt 復旧前確認 再読込」は、AIX エラーログから要約または詳細レポートを生成するコマンドを復旧前確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-015を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> errpt 復旧前確認 再読込の設定や表示を読む前に役割を確認します。lsattr 一覧確認 対象ファイルではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはデバイスや sys0 などの属性値を表示するコマンドである。</li><li>B. 対象資源に対する働きはセキュリティでrbacqry -u user1 -Tを用い・audit class と監査設定を確認する。</li><li>C. 対象資源に対する働きは導入と起動でinstallp -Cを用い・EFIX LABEL と代替ディスク状態を確認する。</li><li>D. 対象資源に対する働きはAIX エラーログから要約または詳細レポートを生成するコマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は復旧前確認 再読込（復旧・errp）です。性能監視の仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・復旧前です。一覧・対象・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は一覧確認 対象ファイル（一覧・lsat）です。変更後・rbacのB:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はaudit class（変更・rbac）です。状態・instのC:は「導入と起動でinstallp -Cを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（状態・inst）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、復旧前確認 再読込ではer・復旧前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>errpt 復旧前確認 再読込</strong></p><p>検証目的: 性能監視のerrpt 復旧前確認 再読込について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、性能監視の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; vmstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: lcpu=2 mem=1024MB tmem=512MB ent=0.40 mmode=dedicated-E
 r b avm fre csz cfr dxm ci co pi po in sy cs
画面・出力には System が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lparstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
%user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
画面・出力には System が含まれ、errpt 復旧前確認 再読込の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ボリュームグループの取り違えを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; topas
→ Enter を押す
［画面・出力］
Topas Monitor for host: aixhost
CPU User% Kern% Wait% Idle%
AME TMEM,MB 512 CMEM,MB 114 EF[T/A] 2.0/1.5
画面・出力には Topas が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の System が画面・出力に表示されること
② ステップ2 の System が画面・出力に表示されること
③ ステップ3 の Topas が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0796"><h3>lslv 一覧確認 サンプル採取</h3><p class="kb-meta">分類: 性能監視 ・ 難易度: 中級</p><p>AIX 7.3 の 性能監視 で扱う「lslv 一覧確認 サンプル採取」は、論理ボリュームの属性と割り当て情報を表示するコマンドを一覧確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-023を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 一覧確認 サンプル採取の設定や表示を読む前に役割を確認します。lsps 詳細確認 メッセージ行ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>B. 状態を読み取るための働きは論理ボリュームの属性と割り当て情報を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはセキュリティでlsroleを用い・roles と監査設定を確認する。</li><li>D. 状態を読み取るための働きは導入と起動でoslevel -sを用い・Technology Level と代替ディスク状態を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は一覧確認 サンプル採取（一覧・lslv）です。性能監視の仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・一覧・サンです。詳細・メッ・lspsのA:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は詳細確認 メッセージ行（詳細・lsps）です。属性・lsroのC:は「セキュリティでlsroleを用い、roles と監査設定を確認する」を述べ、対象は属性確認 roles（属性・lsro）です。容量・osleのD:は「導入と起動でoslevel -sを用い、Technology」を述べ、対象はTechnology Level（容量・osle）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、一覧確認 サンプル採取ではls・一覧・サンに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 一覧確認 サンプル採取</strong></p><p>検証目的: 性能監視のlslv 一覧確認 サンプル採取について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、性能監視の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt
→ Enter を押す
［画面・出力］
ERROR_IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  ERROR_DESCRIPTION
0E017ED1         0405131090 P H mem2           Memory failure
画面・出力には ERROR が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt -a -N hdisk1
→ Enter を押す
［画面・出力］
LABEL: DISK_ERR4
RESOURCE NAME: hdisk1
Description
DISK OPERATION ERROR
画面・出力には LABEL が含まれ、lslv 一覧確認 サンプル採取の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ページング使用率の見落としを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; /usr/lib/errdemon -l
→ Enter を押す
［画面・出力］
/var/adm/ras/errlog
画面・出力には errlog が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ERROR が画面・出力に表示されること
② ステップ2 の LABEL が画面・出力に表示されること
③ ステップ3 の errlog が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0797"><h3>lslv 障害切り分け 起動確認</h3><p class="kb-meta">分類: 性能監視 ・ 難易度: 中級</p><p>AIX 7.3 の 性能監視 で扱う「lslv 障害切り分け 起動確認」は、論理ボリュームの属性と割り当て情報を表示するコマンドを障害切り分けの観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-063を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 障害切り分け 起動確認の設定や表示を読む前に役割を確認します。lsps 性能確認 停止確認ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>B. 対象資源に対する働きはLVMでlsvgを用い・PP SIZE とミラーコピー状態を確認する。</li><li>C. 対象資源に対する働きは論理ボリュームの属性と割り当て情報を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはセキュリティでlsattr -E -l sys0 -aを用い・roles とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は障害切り分け 起動確認（障害・lslv）です。性能監視の仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・障害切です。性能・停止・lspsのA:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は性能確認 停止確認（性能・lsps）です。変更後・lsvgのB:は「LVMでlsvgを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（変更・lsvg）です。状態・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 roles（状態・lsat）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、障害切り分け 起動確認ではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 障害切り分け 起動確認</strong></p><p>検証目的: 性能監視のlslv 障害切り分け 起動確認について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、性能監視の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt
→ Enter を押す
［画面・出力］
ERROR_IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  ERROR_DESCRIPTION
0E017ED1         0405131090 P H mem2           Memory failure
画面・出力には ERROR が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt -a -N hdisk1
→ Enter を押す
［画面・出力］
LABEL: DISK_ERR4
RESOURCE NAME: hdisk1
Description
DISK OPERATION ERROR
画面・出力には LABEL が含まれ、lslv 障害切り分け 起動確認の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、ページング使用率の見落としを切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; /usr/lib/errdemon -l
→ Enter を押す
［画面・出力］
/var/adm/ras/errlog
画面・出力には errlog が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の ERROR が画面・出力に表示されること
② ステップ2 の LABEL が画面・出力に表示されること
③ ステップ3 の errlog が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0798"><h3>lspv 性能確認 保持設定</h3><p class="kb-meta">分類: 性能監視 ・ 難易度: 上級</p><p>AIX 7.3 の 性能監視 で扱う「lspv 性能確認 保持設定」は、物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドを性能確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-071を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lspv 性能確認 保持設定の設定や表示を読む前に役割を確認します。lsvg 変更前確認 再開位置ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>B. 状態を読み取るための働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはJFS2でdefragfsを用い・agblksize とマウントオプションを確認する。</li><li>D. 状態を読み取るための働きはセキュリティでusrck -n ALLを用い・roles とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は性能確認 保持設定（性能・lspv）です。性能監視の仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・性能・保持です。変更前・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は変更前確認 再開位置（変更・lsvg）です。属性・defrのC:は「JFS2でdefragfsを用い、agblksize」を述べ、対象は属性確認 agblksize（属性・defr）です。性能・usrcのD:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は性能確認 roles（性能・usrc）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、性能確認 保持設定ではls・性能・保持に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 性能確認 保持設定</strong></p><p>検証目的: 性能監視のlspv 性能確認 保持設定について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、性能監視の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d4e71        rootvg          active
hdisk1          00f6a1b2c3d5e71        datavg          active
画面・出力には hdisk0 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1092
画面・出力には VOLUME が含まれ、lspv 性能確認 保持設定の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、PVID の誤読を切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
画面・出力には NAME が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の hdisk0 が画面・出力に表示されること
② ステップ2 の VOLUME が画面・出力に表示されること
③ ステップ3 の NAME が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0799"><h3>lspv 詳細確認 装置一覧</h3><p class="kb-meta">分類: 性能監視 ・ 難易度: 中級</p><p>AIX 7.3 の 性能監視 で扱う「lspv 詳細確認 装置一覧」は、物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドを詳細確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-031を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lspv 詳細確認 装置一覧の設定や表示を読む前に役割を確認します。lsvg 状態判定 製品レベルではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>B. 一次資料が示す主目的は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 一次資料が示す主目的はデバイス管理でlsmpio -l hdisk0を用い・microcode levelである。</li><li>D. 一次資料が示す主目的はネットワークでroute -n getを用い・Gateway と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は詳細確認 装置一覧（詳細・lspv）です。性能監視の仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・詳細・装置です。状態・製品・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は状態判定 製品レベル（状態・lsvg）です。運用引・lsmpのC:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はmicrocode level（運用・lsmp）です。障害切・routのD:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・rout）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、詳細確認 装置一覧ではls・詳細・装置に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 詳細確認 装置一覧</strong></p><p>検証目的: 性能監視のlspv 詳細確認 装置一覧について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、性能監視の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d4e31        rootvg          active
hdisk1          00f6a1b2c3d5e31        datavg          active
画面・出力には hdisk0 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1092
画面・出力には VOLUME が含まれ、lspv 詳細確認 装置一覧の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、PVID の誤読を切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
画面・出力には NAME が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の hdisk0 が画面・出力に表示されること
② ステップ2 の VOLUME が画面・出力に表示されること
③ ステップ3 の NAME が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0800"><h3>vmstat 性能確認 性能値</h3><p class="kb-meta">分類: 性能監視 ・ 難易度: 上級</p><p>AIX 7.3 の 性能監視 で扱う「vmstat 性能確認 性能値」は、CPU、メモリー、ページング、AME 統計を表示する性能コマンドを性能確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-079を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> vmstat 性能確認 性能値の設定や表示を読む前に役割を確認します。lparstat 変更前確認 キュー状態ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>B. 一次資料が示す主目的はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 一次資料が示す主目的はJFS2でsplitcopyを用い・ファイルシステム使用率 とマウントオプションを確認する。</li><li>D. 一次資料が示す主目的はセキュリティでlsuserを用い・authorizations とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「CPU、メモリー、ページング、AME 統計を表示する性能コマンドである」に対応する項目は性能確認 性能値（性能・vmst）です。性能監視の仕様は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」で、確認対象はvm・性能・性能です。変更前・lparのA:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は変更前確認 キュー状態（変更・lpar）です。運用引・spliのC:は「JFS2でsplitcopyを用い、ファイルシステム使用率」を述べ、対象は運用引継ぎ ファイルシステム使用率（運用・spli）です。バック・lsusのD:は「セキュリティでlsuserを用い、authorizations」を述べ、対象はバックアウト確認 authoriza（バッ・lsus）です。「vmstat」は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を指し、性能確認 性能値ではvm・性能・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>vmstat 性能確認 性能値</strong></p><p>検証目的: 性能監視のvmstat 性能確認 性能値について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、性能監視の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsattr -E -l sys0 -a iostat
→ Enter を押す
［画面・出力］
iostat true Continuously maintain disk I/O history True
画面・出力には iostat が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; chdev -l sys0 -a iostat=true
→ Enter を押す
［画面・出力］
sys0 changed
画面・出力には sys0 が含まれ、vmstat 性能確認 性能値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、資源名の誤指定を切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lscfg -l sysplanar0
→ Enter を押す
［画面・出力］
DEVICE          LOCATION     DESCRIPTION
sysplanar0      00-00        CPU Planar
画面・出力には DEVICE が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の iostat が画面・出力に表示されること
② ステップ2 の sys0 が画面・出力に表示されること
③ ステップ3 の DEVICE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


<section class="kb-item" id="c01-i0801"><h3>vmstat 詳細確認 サービス状態</h3><p class="kb-meta">分類: 性能監視 ・ 難易度: 中級</p><p>AIX 7.3 の 性能監視 で扱う「vmstat 詳細確認 サービス状態」は、CPU、メモリー、ページング、AME 統計を表示する性能コマンドを詳細確認の観点で確認する技術項目です。DEVICE LOCATION 行とrootvg-039を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> vmstat 詳細確認 サービス状態の設定や表示を読む前に役割を確認します。lparstat 状態判定 変更証跡ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>B. 対象資源に対する働きはデバイス管理でrmdev -Rl ent1を用い・PVID と診断対象表示を確認する。</li><li>C. 対象資源に対する働きはCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはネットワークでsmitty etherchannelを用い・MTU と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「CPU、メモリー、ページング、AME 統計を表示する性能コマンドである」に対応する項目は詳細確認 サービス状態（詳細・vmst）です。性能監視の仕様は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」で、確認対象はvm・詳細・サーです。状態・変更・lparのA:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は状態判定 変更証跡（状態・lpar）です。変更後・rmdeのB:は「デバイス管理でrmdev -Rl ent1を用い、PVID」を述べ、対象は変更後確認 PVID（変更・rmde）です。状態・smitのD:は「ネットワークでsmitty etherchannelを用い、MTU」を述べ、対象は状態確認 MTU（状態・smit）です。「vmstat」は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を指し、詳細確認 サービス状態ではvm・詳細・サーに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>vmstat 詳細確認 サービス状態</strong></p><p>検証目的: 性能監視のvmstat 詳細確認 サービス状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、性能監視の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsattr -E -l sys0 -a iostat
→ Enter を押す
［画面・出力］
iostat true Continuously maintain disk I/O history True
画面・出力には iostat が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。DEVICE LOCATION 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; chdev -l sys0 -a iostat=true
→ Enter を押す
［画面・出力］
sys0 changed
画面・出力には sys0 が含まれ、vmstat 詳細確認 サービス状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3の詳細確認画面です。表示名とメッセージ形式を照合し、資源名の誤指定を切り分けます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lscfg -l sysplanar0
→ Enter を押す
［画面・出力］
DEVICE          LOCATION     DESCRIPTION
sysplanar0      00-00        CPU Planar
画面・出力には DEVICE が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の iostat が画面・出力に表示されること
② ステップ2 の sys0 が画面・出力に表示されること
③ ステップ3 の DEVICE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details></section>


## 性能管理


<section class="kb-item" id="c01-i0802"><h3>filemon 変更後確認 Busy% 0384</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>霜月記録ではAIX 7.3の性能管理で filemon を確認します。霜月記録の性能管理では Busy% とtopasディスク表示を同じ証跡に残します。霜月記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。霜月記録の注意点として 初回サンプルだけの誤判定 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、霜月記録を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> filemon 変更後確認 Busy% 0384を同一分類のpwdck -n ALL 障害切り分け authorizations 0385と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はセキュリティでpwdck -n ALLを用い・authorizations と監査設定を確認する。</li><li>B. 構成を確認する際の意味はJFS2でdf -gを用い・isnapshot とファイルシステム属性を確認する。</li><li>C. 構成を確認する際の意味は性能管理でfilemonを用い・Busy% とtopasディスク表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はLVMでmigratepvを用い・PP SIZE とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「性能管理でfilemonを用い、Busy% とtopasディスク表示を確認する」に対応する項目は変更後確認 Busy%（変更・file）です。変更後に関する性能管理の仕様は「性能管理でfilemonを用い、Busy%」で、確認対象はfi・変更後です。障害切・pwdcのA:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は障害切り分け authorizati（障害・pwdc）です。属性・dfのB:は「JFS2でdf -gを用い、isnapshot」を述べ、対象は属性確認 isnapshot（属性・df）です。バック・migrのD:は「LVMでmigratepvを用い、PP SIZE」を述べ、対象はPP SIZE（バッ・migr）です。「filemon」は「性能管理でfilemonを用い、Busy%」を指し、変更後確認 Busy%ではfi・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>filemon 変更後確認 Busy% 0384</strong></p><p>検証目的: 性能管理のfilemon 変更後確認 Busy% 0384について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認024-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; filemon
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0384A
画面・出力には AIX0384A が表示され、filemon 変更後確認 Busy% 0384 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0384B
画面・出力には AIX0384B が表示され、filemon 変更後確認 Busy% 0384 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0384C
画面・出力には AIX0384C が表示され、filemon 変更後確認 Busy% 0384 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0384A が画面・出力に表示されること
② ステップ2 の AIX0384B が画面・出力に表示されること
③ ステップ3 の AIX0384C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0803"><h3>filemon 変更後確認 avm 0444</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>若草整理ではAIX 7.3の性能管理で filemon を確認します。若草整理の性能管理では avm とtopasディスク表示を同じ証跡に残します。若草整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若草整理の注意点として 初回サンプルだけの誤判定 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、若草整理を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> filemon 変更後確認 avm 0444の技術的な意味を資料で確認するとき、pwdck -n ALL 障害切り分け authorizations 0445との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はセキュリティでpwdck -n ALLを用い・authorizations と監査設定を確認する。</li><li>B. 構成を確認する際の意味はJFS2でsnapを用い・mountguard とファイルシステム属性を確認する。</li><li>C. 構成を確認する際の意味は性能管理でfilemonを用い・avm とtopasディスク表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はLVMでvaryonvgを用い・STALE PARTITIONS とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「性能管理でfilemonを用い、avm とtopasディスク表示を確認する」に対応する項目は変更後確認 avm（変更・file）です。変更後に関する性能管理の仕様は「性能管理でfilemonを用い、avm とtopasディスク表示を確」で、確認対象はfi・変更後です。障害切・pwdcのA:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は障害切り分け authorizati（障害・pwdc）です。状態・snapのB:は「JFS2でsnapを用い、mountguard」を述べ、対象は状態確認 mountguard（状態・snap）です。監査・varyのD:は「LVMでvaryonvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（監査・vary）です。「filemon」は「性能管理でfilemonを用い、avm とtopasディスク表示を確」を指し、変更後確認 avmではfi・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>filemon 変更後確認 avm 0444</strong></p><p>検証目的: 性能管理のfilemon 変更後確認 avm 0444について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認084-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; filemon
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0444A
画面・出力には AIX0444A が表示され、filemon 変更後確認 avm 0444 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0444B
画面・出力には AIX0444B が表示され、filemon 変更後確認 avm 0444 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0444C
画面・出力には AIX0444C が表示され、filemon 変更後確認 avm 0444 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0444A が画面・出力に表示されること
② ステップ2 の AIX0444B が画面・出力に表示されること
③ ステップ3 の AIX0444C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0804"><h3>filemon 性能確認 po 0414</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>星霜評価ではAIX 7.3の性能管理で filemon を確認します。星霜評価の性能管理では po とvmstat表示を変更票へ記録します。星霜評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。星霜評価の注意点として ディスクBusyと待ち時間の混同 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、星霜評価を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> filemon 性能確認 po 0414に関する障害切り分けの前提を確認しています。pwdck -n ALL 起動確認 authorizations 0415の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはセキュリティでpwdck -n ALLを用い・authorizations とロール一覧を確認する。</li><li>B. 機能の説明としては性能管理でfilemonを用い・po とvmstat表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としてはJFS2でdf -gを用い・ファイルシステム使用率 とログデバイス設定を確認する。</li><li>D. 機能の説明としてはLVMでmigratepvを用い・PVID とボリュームグループ属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「性能管理でfilemonを用い、po とvmstat表示を確認する」に対応する項目は性能確認 po（性能・file）です。性能に関する性能管理の仕様は「性能管理でfilemonを用い、po とvmstat表示を確認する」で、確認対象はfi・性能です。起動・pwdcのA:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は起動確認 authorization（起動・pwdc）です。バック・dfのC:は「JFS2でdf -gを用い、ファイルシステム使用率」を述べ、対象はバックアウト確認 ファイルシステム使（バッ・df）です。属性・migrのD:は「LVMでmigratepvを用い、PVID」を述べ、対象は属性確認 PVID（属性・migr）です。「filemon」は「性能管理でfilemonを用い、po とvmstat表示を確認する」を指し、性能確認 poではfi・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>filemon 性能確認 po 0414</strong></p><p>検証目的: 性能管理のfilemon 性能確認 po 0414について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認054-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; filemon
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0414A
画面・出力には AIX0414A が表示され、filemon 性能確認 po 0414 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0414B
画面・出力には AIX0414B が表示され、filemon 性能確認 po 0414 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0414C
画面・出力には AIX0414C が表示され、filemon 性能確認 po 0414 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0414A が画面・出力に表示されること
② ステップ2 の AIX0414B が画面・出力に表示されること
③ ステップ3 の AIX0414C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0805"><h3>filemon 構成照合 csz 0097</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>初霜点検ではAIX 7.3の性能管理で filemon を確認します。初霜点検の性能管理では csz とAME統計を採取票へ記録します。初霜点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。初霜点検の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、初霜点検を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「filemon 構成照合 csz 0097」を「pwdck -n ALL 変更前確認 user attributes 0098」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はセキュリティでpwdck -n ALLを用い・user attributes とRBAC属性を確認する。</li><li>B. 保守作業で参照する機能は性能管理でfilemonを用い・csz とAME統計を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はJFS2でsnapを用い・agblksize と内部スナップショットを確認する。</li><li>D. 保守作業で参照する機能はセキュリティでsetsecattrを用い・enhanced_RBAC とRBAC属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「性能管理でfilemonを用い、csz とAME統計を確認する」に対応する項目は構成照合 csz（構成・file）です。構成に関する性能管理の仕様は「性能管理でfilemonを用い、csz とAME統計を確認する」で、確認対象はfi・構成です。変更前・pwdcのA:は「セキュリティでpwdck -n ALLを用い、user」を述べ、対象はuser attributes（変更・pwdc）です。起動・snapのC:は「JFS2でsnapを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・snap）です。運用引・setsのD:は「セキュリティでsetsecattrを用い」を述べ、対象は運用引継ぎ enhanced_RBA（運用・sets）です。「filemon」は「性能管理でfilemonを用い、csz とAME統計を確認する」を指し、構成照合 cszではfi・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>filemon 構成照合 csz 0097</strong></p><p>検証目的: 性能管理のfilemon 構成照合 csz 0097について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合097-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; filemon
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0097A
画面・出力には AIX0097A が表示され、filemon 構成照合 csz 0097 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0097B
画面・出力には AIX0097B が表示され、filemon 構成照合 csz 0097 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。csz を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; vmstat 2 2
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0097C
画面・出力には AIX0097C が表示され、filemon 構成照合 csz 0097 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0097A が画面・出力に表示されること
② ステップ2 の AIX0097B が画面・出力に表示されること
③ ステップ3 の AIX0097C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0806"><h3>filemon 構成照合 po 0573</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>月影点検ではAIX 7.3の性能管理で filemon を確認します。月影点検の性能管理では po とAME統計を判定票へ残します。月影点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。月影点検の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、月影点検を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> filemon 構成照合 po 0573を保守記録に説明する必要があります。pwdck -n ALL 変更前確認 authorizations 0574と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はセキュリティでpwdck -n ALLを用い・authorizations とRBAC属性を確認する。</li><li>B. 運用時に利用する技術的役割はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>C. 運用時に利用する技術的役割は性能管理でfilemonを用い・po とAME統計を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はLVMでvaryonvgを用い・PP SIZE と物理ボリューム一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「性能管理でfilemonを用い、po とAME統計を確認する」に対応する項目は構成照合 po（構成・file）です。構成に関する性能管理の仕様は「性能管理でfilemonを用い、po とAME統計を確認する」で、確認対象はfi・構成です。変更前・pwdcのA:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は変更前確認 authorizatio（変更・pwdc）です。詳細・サー・vmstのB:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は詳細確認 サービス状態（詳細・vmst）です。障害切・varyのD:は「LVMでvaryonvgを用い、PP SIZE」を述べ、対象はPP SIZE（障害・vary）です。「filemon」は「性能管理でfilemonを用い、po とAME統計を確認する」を指し、構成照合 poではfi・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>filemon 構成照合 po 0573</strong></p><p>検証目的: 性能管理のfilemon 構成照合 po 0573について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理構成照合093-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; filemon
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0573A
画面・出力には AIX0573A が表示され、filemon 構成照合 po 0573 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0573B
画面・出力には AIX0573B が表示され、filemon 構成照合 po 0573 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0573C
画面・出力には AIX0573C が表示され、filemon 構成照合 po 0573 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0573A が画面・出力に表示されること
② ステップ2 の AIX0573B が画面・出力に表示されること
③ ステップ3 の AIX0573C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0807"><h3>filemon 運用引継ぎ Busy% 0543</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>新緑照合ではAIX 7.3の性能管理で filemon を確認します。新緑照合の性能管理では Busy% とsvmon全体表示を作業票へ保管します。新緑照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。新緑照合の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、新緑照合を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> filemon 運用引継ぎ Busy% 0543の設定や表示を読む前に役割を確認します。pwdck -n ALL 容量確認 authorizations 0544ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きは性能管理でfilemonを用い・Busy% とsvmon全体表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 状態を読み取るための働きはセキュリティでpwdck -n ALLを用い・authorizations とユーザー属性を確認する。</li><li>C. 状態を読み取るための働きはCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>D. 状態を読み取るための働きはLVMでmigratepvを用い・MIRROR WRITE CONSISTENCYである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「性能管理でfilemonを用い、Busy% とsvmon全体表示を確認する」に対応する項目は運用引継ぎ Busy%（運用・file）です。運用引に関する性能管理の仕様は「性能管理でfilemonを用い、Busy%」で、確認対象はfi・運用引です。容量・pwdcのB:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は容量確認 authorization（容量・pwdc）です。一覧・出力・vmstのC:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は一覧確認 出力見出し（一覧・vmst）です。性能・migrのD:は「LVMでmigratepvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（性能・migr）です。「filemon」は「性能管理でfilemonを用い、Busy%」を指し、運用引継ぎ Busy%ではfi・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>filemon 運用引継ぎ Busy% 0543</strong></p><p>検証目的: 性能管理のfilemon 運用引継ぎ Busy% 0543について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ063-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; filemon
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0543A
画面・出力には AIX0543A が表示され、filemon 運用引継ぎ Busy% 0543 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0543B
画面・出力には AIX0543B が表示され、filemon 運用引継ぎ Busy% 0543 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0543C
画面・出力には AIX0543C が表示され、filemon 運用引継ぎ Busy% 0543 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0543A が画面・出力に表示されること
② ステップ2 の AIX0543B が画面・出力に表示されること
③ ステップ3 の AIX0543C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0808"><h3>filemon 運用引継ぎ PhysB 0067</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>風花照合ではAIX 7.3の性能管理で filemon を確認します。風花照合の性能管理では PhysB とsvmon全体表示を点検票へ整理します。風花照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。風花照合の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、風花照合を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> filemon 運用引継ぎ PhysB 0067について構成や状態を確認します。pwdck -n ALL 容量確認 user attributes 0068ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはセキュリティでpwdck -n ALLを用い・user attributes とユーザー属性を確認する。</li><li>B. 対象資源に対する働きはJFS2でsnapを用い・lff とマウントオプションを確認する。</li><li>C. 対象資源に対する働きはセキュリティでsetsecattrを用い・enhanced_RBAC とユーザー属性を確認する。</li><li>D. 対象資源に対する働きは性能管理でfilemonを用い・PhysB とsvmon全体表示を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「性能管理でfilemonを用い、PhysB とsvmon全体表示を確認する」に対応する項目は運用引継ぎ PhysB（運用・file）です。性能管理の仕様は「性能管理でfilemonを用い、PhysB」で、確認対象はfi・運用引です。容量・pwdcのA:は「セキュリティでpwdck -n ALLを用い、user」を述べ、対象はuser attributes（容量・pwdc）です。障害切・snapのB:は「JFS2でsnapを用い、lff とマウントオプションを確認する」を述べ、対象は障害切り分け lff（障害・snap）です。構成・setsのC:は「セキュリティでsetsecattrを用い」を述べ、対象は構成照合 enhanced_RBAC（構成・sets）です。「filemon」は「性能管理でfilemonを用い、PhysB」を指し、運用引継ぎ PhysBではfi・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>filemon 運用引継ぎ PhysB 0067</strong></p><p>検証目的: 性能管理のfilemon 運用引継ぎ PhysB 0067について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理運用引継ぎ067-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; filemon
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0067A
画面・出力には AIX0067A が表示され、filemon 運用引継ぎ PhysB 0067 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0067B
画面・出力には AIX0067B が表示され、filemon 運用引継ぎ PhysB 0067 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; vmstat 2 2
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0067C
画面・出力には AIX0067C が表示され、filemon 運用引継ぎ PhysB 0067 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0067A が画面・出力に表示されること
② ステップ2 の AIX0067B が画面・出力に表示されること
③ ステップ3 の AIX0067C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0809"><h3>iostat -Dl 2 2 バックアウト確認 Busy% 0172</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>水音判定ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。水音判定の性能管理では Busy% とtopasディスク表示を監査票へ転記します。水音判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。水音判定の注意点として 初回サンプルだけの誤判定 を避けるため svmon -G も併記します。性能監視の作業票として、水音判定を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> iostat -Dl 2 2 バックアウト確認 Busy% 0172の技術的な意味を資料で確認するとき、lssecattr -c 監査記録 audit class 0173との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はセキュリティでlssecattr -cを用い・audit class と監査設定を確認する。</li><li>B. 管理対象との関係を表す説明は性能管理でiostat -Dl 2 2を用い・Busy% とtopasディスク表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はJFS2でchfsを用い・isnapshot とファイルシステム属性を確認する。</li><li>D. 管理対象との関係を表す説明はセキュリティでlsroleを用い・user attributes と監査設定を確認する。lsrole 属性確認 user attributes 0785固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「性能管理でiostat -Dl 2 2を用い、Busy%」に対応する項目はバックアウト確認 Busy%（バッ・iost）です。バックに関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、Busy%」で、確認対象はio・バックです。監査・lsseのA:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（監査・lsse）です。構成・chfsのC:は「JFS2でchfsを用い、isnapshot」を述べ、対象は構成照合 isnapshot（構成・chfs）です。属性・lsroのD:は「セキュリティでlsroleを用い、user attributes」を述べ、対象はuser attributes（属性・lsro）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、Busy%」を指し、バックアウト確認 Busy%ではio・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>iostat -Dl 2 2 バックアウト確認 Busy% 0172</strong></p><p>検証目的: 性能管理のiostat -Dl 2 2 バックアウト確認 Busy% 0172について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認052-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; iostat -Dl 2 2
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0172A
画面・出力には AIX0172A が表示され、iostat -Dl 2 2 バックアウト確認 Busy% 0172 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0172B
画面・出力には AIX0172B が表示され、iostat -Dl 2 2 バックアウト確認 Busy% 0172 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; vmstat 2 2
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0172C
画面・出力には AIX0172C が表示され、iostat -Dl 2 2 バックアウト確認 Busy% 0172 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0172A が画面・出力に表示されること
② ステップ2 の AIX0172B が画面・出力に表示されること
③ ステップ3 の AIX0172C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0810"><h3>iostat -Dl 2 2 バックアウト確認 dxm 0648</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>翠風判定ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。翠風判定の性能管理では dxm とtopasディスク表示を同じ証跡に残します。翠風判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。翠風判定の注意点として 初回サンプルだけの誤判定 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、翠風判定を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> iostat -Dl 2 2 バックアウト確認 dxm 0648を同一分類のlssecattr -c 監査記録 enhanced_RBAC 0649と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は性能管理でiostat -Dl 2 2を用い・dxm とtopasディスク表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はセキュリティでlssecattr -cを用い・enhanced_RBAC と監査設定を確認する。</li><li>C. 構成を確認する際の意味はSRCとログでsyslog_ssw -rを用い・syslog.conf とSRCサブシステム表示を確認する。</li><li>D. 構成を確認する際の意味はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「性能管理でiostat -Dl 2 2を用い、dxm」に対応する項目はバックアウト確認 dxm（バッ・iost）です。バックに関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、dxm」で、確認対象はio・バックです。監査・lsseのB:は「セキュリティでlssecattr -cを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsse）です。起動・syslのC:は「SRCとログでsyslog_ssw -rを用い」を述べ、対象は起動確認 syslog.conf（起動・sysl）です。運用引・lslvのD:は「LVMでlslvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・lslv）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、dxm」を指し、バックアウト確認 dxmではio・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>iostat -Dl 2 2 バックアウト確認 dxm 0648</strong></p><p>検証目的: 性能管理のiostat -Dl 2 2 バックアウト確認 dxm 0648について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理バックアウト確認048-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; iostat -Dl 2 2
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0648A
画面・出力には AIX0648A が表示され、iostat -Dl 2 2 バックアウト確認 dxm 0648 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0648B
画面・出力には AIX0648B が表示され、iostat -Dl 2 2 バックアウト確認 dxm 0648 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0648C
画面・出力には AIX0648C が表示され、iostat -Dl 2 2 バックアウト確認 dxm 0648 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0648A が画面・出力に表示されること
② ステップ2 の AIX0648B が画面・出力に表示されること
③ ステップ3 の AIX0648C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0811"><h3>iostat -Dl 2 2 変更後確認 Entitled Capacity 0777</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>初霜復旧ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。初霜復旧の性能管理では Entitled Capacity とAME統計を判定票へ残します。初霜復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。初霜復旧の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、初霜復旧を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「iostat -Dl 2 2 変更後確認 Entitled Capacity 0777」を「chdev 障害切り分け ボリューム状態」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はデバイス属性を変更する管理コマンドである。chdev 障害切り分け ボリューム状態固有の属性も確認対象に含める。</li><li>B. 運用時に利用する技術的役割は性能管理でnmonを用い・Busy% とAME統計を確認する。</li><li>C. 運用時に利用する技術的役割は性能管理でiostat -Dl 2 2を用い・Entitled Capacity とAME統計を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はネットワークでsmitty etherchannelを用い・EtherChannelである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更後・iostでCの記述「性能管理でiostat -Dl 2 2を用い、Entitled」に対応する項目はEntitled Capacity（変更・iost）です。変更後に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、Entitled」で、確認対象はio・変更後です。障害切・chdeのA:は「デバイス属性を変更する管理コマンド」を述べ、対象は障害切り分け ボリューム状態（障害・chde）です。起動・nmonのB:は「性能管理でnmonを用い、Busy% とAME統計を確認する」を述べ、対象は起動確認 Busy%（起動・nmon）です。監査・smitのD:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は監査記録 EtherChannel（監査・smit）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、Entitled」を指し、Entitled Capacityではio・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>iostat -Dl 2 2 変更後確認 Entitled Capacity 0777</strong></p><p>検証目的: 性能管理のiostat -Dl 2 2 変更後確認 Entitled Capacity 0777について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認057-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; iostat -Dl 2 2
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0777A
画面・出力には AIX0777A が表示され、iostat -Dl 2 2 変更後確認 Entitled Capacity 0777 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0777B
画面・出力には AIX0777B が表示され、iostat -Dl 2 2 変更後確認 Entitled Capacity 0777 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0777C
画面・出力には AIX0777C が表示され、iostat -Dl 2 2 変更後確認 Entitled Capacity 0777 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0777A が画面・出力に表示されること
② ステップ2 の AIX0777B が画面・出力に表示されること
③ ステップ3 の AIX0777C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0812"><h3>iostat -Dl 2 2 変更後確認 avm 0301</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>群青復旧ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。群青復旧の性能管理では avm とAME統計を採取票へ記録します。群青復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。群青復旧の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、群青復旧を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> iostat -Dl 2 2 変更後確認 avm 0301を保守記録に説明する必要があります。lssecattr -c 障害切り分け audit class 0302と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は性能管理でiostat -Dl 2 2を用い・avm とAME統計を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はセキュリティでlssecattr -cを用い・audit class とRBAC属性を確認する。</li><li>C. 保守作業で参照する機能はJFS2でlsfs -qを用い・mountguard と内部スナップショットを確認する。</li><li>D. 保守作業で参照する機能はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「性能管理でiostat -Dl 2 2を用い、avm とAME統計を確認する」に対応する項目は変更後確認 avm（変更・iost）です。変更後に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、avm」で、確認対象はio・変更後です。障害切・lsseのB:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（障害・lsse）です。状態・lsfsのC:は「JFS2でlsfs -qを用い、mountguard」を述べ、対象は状態確認 mountguard（状態・lsfs）です。一覧・メッ・lspsのD:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は一覧確認 メッセージ行（一覧・lsps）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、avm」を指し、変更後確認 avmではio・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>iostat -Dl 2 2 変更後確認 avm 0301</strong></p><p>検証目的: 性能管理のiostat -Dl 2 2 変更後確認 avm 0301について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認061-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; iostat -Dl 2 2
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0301A
画面・出力には AIX0301A が表示され、iostat -Dl 2 2 変更後確認 avm 0301 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0301B
画面・出力には AIX0301B が表示され、iostat -Dl 2 2 変更後確認 avm 0301 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; vmstat 2 2
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0301C
画面・出力には AIX0301C が表示され、iostat -Dl 2 2 変更後確認 avm 0301 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0301A が画面・出力に表示されること
② ステップ2 の AIX0301B が画面・出力に表示されること
③ ステップ3 の AIX0301C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0813"><h3>iostat -Dl 2 2 変更後確認 pi 0837</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 上級</p><p>冬晴変更ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。冬晴変更の性能管理では pi とAME統計を判定票へ残します。冬晴変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。冬晴変更の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、冬晴変更を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> iostat -Dl 2 2 変更後確認 pi 0837を保守記録に説明する必要があります。lscfg 状態判定 除外条件と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割は構成済みデバイスと VPD を表示するコマンドである。</li><li>B. 運用時に利用する技術的役割はセキュリティでsetsecattrを用い・audit class とRBAC属性を確認する。</li><li>C. 運用時に利用する技術的役割はセキュリティでlsattr -E -l sys0 -aを用い・roles とRBAC属性を確認する。</li><li>D. 運用時に利用する技術的役割は性能管理でiostat -Dl 2 2を用い・pi とAME統計を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更後・iostでDの記述「性能管理でiostat -Dl 2 2を用い、pi」に対応する項目は変更後確認 pi（変更・iost）です。変更後に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、pi」で、確認対象はio・変更後です。状態・除外・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は状態判定 除外条件（状態・lscf）です。運用引・setsのB:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（運用・sets）です。監査・lsatのC:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 roles（監査・lsat）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、pi」を指し、変更後確認 piではio・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>iostat -Dl 2 2 変更後確認 pi 0837</strong></p><p>検証目的: 性能管理のiostat -Dl 2 2 変更後確認 pi 0837について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更後確認117-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; iostat -Dl 2 2
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0837A
画面・出力には AIX0837A が表示され、iostat -Dl 2 2 変更後確認 pi 0837 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0837B
画面・出力には AIX0837B が表示され、iostat -Dl 2 2 変更後確認 pi 0837 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0837C
画面・出力には AIX0837C が表示され、iostat -Dl 2 2 変更後確認 pi 0837 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0837A が画面・出力に表示されること
② ステップ2 の AIX0837B が画面・出力に表示されること
③ ステップ3 の AIX0837C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0814"><h3>iostat -Dl 2 2 属性確認 Entitled Capacity 0618</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 初級</p><p>潮騒採取ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。潮騒採取の性能管理では Entitled Capacity とvmstat表示を変更票へ記録します。潮騒採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。潮騒採取の注意点として ディスクBusyと待ち時間の混同 を避けるため vmstat 2 2 も併記します。性能監視の作業票として、潮騒採取を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> iostat -Dl 2 2 属性確認 Entitled Capacity 0618の役割を調べています。lssecattr -c 状態確認 enhanced_RBAC 0619の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはセキュリティでlssecattr -cを用い・enhanced_RBAC とロール一覧を確認する。</li><li>B. 機能の説明としては導入と起動でalt_disk_copyを用い・EFIX LABEL と代替ディスク状態を確認する。</li><li>C. 機能の説明としては性能管理でiostat -Dl 2 2を用い・Entitled Capacityである。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはLVMでlslvを用い・LV STATE とボリュームグループ属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「性能管理でiostat -Dl 2 2を用い、Entitled」に対応する項目はEntitled Capacity（属性・iost）です。属性に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、Entitled」で、確認対象はio・属性です。状態・lsseのA:は「セキュリティでlssecattr -cを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsse）です。障害切・alt_のB:は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（障害・alt_）です。構成・lslvのD:は「LVMでlslvを用い、LV STATE」を述べ、対象はLV STATE（構成・lslv）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、Entitled」を指し、Entitled Capacityではio・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>iostat -Dl 2 2 属性確認 Entitled Capacity 0618</strong></p><p>検証目的: 性能管理のiostat -Dl 2 2 属性確認 Entitled Capacity 0618について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理属性確認018-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; iostat -Dl 2 2
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0618A
画面・出力には AIX0618A が表示され、iostat -Dl 2 2 属性確認 Entitled Capacity 0618 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0618B
画面・出力には AIX0618B が表示され、iostat -Dl 2 2 属性確認 Entitled Capacity 0618 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0618C
画面・出力には AIX0618C が表示され、iostat -Dl 2 2 属性確認 Entitled Capacity 0618 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0618A が画面・出力に表示されること
② ステップ2 の AIX0618B が画面・出力に表示されること
③ ステップ3 の AIX0618C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0815"><h3>iostat -Dl 2 2 属性確認 avm 0142</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 初級</p><p>紅葉採取ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。紅葉採取の性能管理では avm とvmstat表示を保守票へ記録します。紅葉採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。紅葉採取の注意点として ディスクBusyと待ち時間の混同 を避けるため svmon -G も併記します。性能監視の作業票として、紅葉採取を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> iostat -Dl 2 2 属性確認 avm 0142に関する障害切り分けの前提を確認しています。lssecattr -c 状態確認 audit class 0143の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はセキュリティでlssecattr -cを用い・audit class とロール一覧を確認する。</li><li>B. 表示や設定で扱う内容はJFS2でchfsを用い・ファイルシステム使用率 とログデバイス設定を確認する。</li><li>C. 表示や設定で扱う内容はセキュリティでlsroleを用い・user attributes とロール一覧を確認する。</li><li>D. 表示や設定で扱う内容は性能管理でiostat -Dl 2 2を用い・avm とvmstat表示を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「性能管理でiostat -Dl 2 2を用い、avm とvmstat表示を確認する」に対応する項目は属性確認 avm（属性・iost）です。属性に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、avm」で、確認対象はio・属性です。状態・lsseのA:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（状態・lsse）です。運用引・chfsのB:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象は運用引継ぎ ファイルシステム使用率（運用・chfs）です。バック・lsroのC:は「セキュリティでlsroleを用い、user attributes」を述べ、対象はuser attributes（バッ・lsro）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、avm」を指し、属性確認 avmではio・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>iostat -Dl 2 2 属性確認 avm 0142</strong></p><p>検証目的: 性能管理のiostat -Dl 2 2 属性確認 avm 0142について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理属性確認022-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; iostat -Dl 2 2
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0142A
画面・出力には AIX0142A が表示され、iostat -Dl 2 2 属性確認 avm 0142 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0142B
画面・出力には AIX0142B が表示され、iostat -Dl 2 2 属性確認 avm 0142 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。avm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; vmstat 2 2
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0142C
画面・出力には AIX0142C が表示され、iostat -Dl 2 2 属性確認 avm 0142 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0142A が画面・出力に表示されること
② ステップ2 の AIX0142B が画面・出力に表示されること
③ ステップ3 の AIX0142C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0816"><h3>iostat -Dl 2 2 性能確認 Busy% 0331</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>松風変更ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。松風変更の性能管理では Busy% とsvmon全体表示を点検票へ整理します。松風変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。松風変更の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、松風変更を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> iostat -Dl 2 2 性能確認 Busy% 0331について構成や状態を確認します。lssecattr -c 起動確認 audit class 0332ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きは性能管理でiostat -Dl 2 2を用い・Busy% とsvmon全体表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはセキュリティでlssecattr -cを用い・audit class とユーザー属性を確認する。</li><li>C. 対象資源に対する働きはJFS2でlsfs -qを用い・log=INLINE とマウントオプションを確認する。</li><li>D. 対象資源に対する働きはLVMでmklvを用い・PVID と論理ボリューム配置を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「性能管理でiostat -Dl 2 2を用い、Busy%」に対応する項目は性能確認 Busy%（性能・iost）です。性能に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、Busy%」で、確認対象はio・性能です。起動・lsseのB:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（起動・lsse）です。監査・lsfsのC:は「JFS2でlsfs -qを用い、log=INLINE」を述べ、対象は監査記録 log=INLINE（監査・lsfs）です。状態・mklvのD:は「LVMでmklvを用い、PVID と論理ボリューム配置を確認する」を述べ、対象は状態確認 PVID（状態・mklv）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、Busy%」を指し、性能確認 Busy%ではio・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>iostat -Dl 2 2 性能確認 Busy% 0331</strong></p><p>検証目的: 性能管理のiostat -Dl 2 2 性能確認 Busy% 0331について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認091-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; iostat -Dl 2 2
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0331A
画面・出力には AIX0331A が表示され、iostat -Dl 2 2 性能確認 Busy% 0331 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0331B
画面・出力には AIX0331B が表示され、iostat -Dl 2 2 性能確認 Busy% 0331 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Busy% を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; vmstat 2 2
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0331C
画面・出力には AIX0331C が表示され、iostat -Dl 2 2 性能確認 Busy% 0331 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0331A が画面・出力に表示されること
② ステップ2 の AIX0331B が画面・出力に表示されること
③ ステップ3 の AIX0331C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0817"><h3>iostat -Dl 2 2 性能確認 dxm 0807</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>夕凪変更ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。夕凪変更の性能管理では dxm とsvmon全体表示を作業票へ保管します。夕凪変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。夕凪変更の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、夕凪変更を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> iostat -Dl 2 2 性能確認 dxm 0807の設定や表示を読む前に役割を確認します。lspv 状態判定 照合単位ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。</li><li>B. 状態を読み取るための働きはJFS2でdf -gを用い・log=INLINE とファイルシステム属性を確認する。</li><li>C. 状態を読み取るための働きは性能管理でiostat -Dl 2 2を用い・dxm とsvmon全体表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 状態を読み取るための働きはLVMでmigratepvを用い・LV STATE とボリュームグループ属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 性能・iostでCの記述「性能管理でiostat -Dl 2 2を用い、dxm」に対応する項目は性能確認 dxm（性能・iost）です。性能に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、dxm」で、確認対象はio・性能です。状態・照合・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は状態判定 照合単位（状態・lspv）です。属性・dfのB:は「JFS2でdf -gを用い、log=INLINE」を述べ、対象は属性確認 log=INLINE（属性・df）です。属性・migrのD:は「LVMでmigratepvを用い、LV STATE」を述べ、対象はLV STATE（属性・migr）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、dxm」を指し、性能確認 dxmではio・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>iostat -Dl 2 2 性能確認 dxm 0807</strong></p><p>検証目的: 性能管理のiostat -Dl 2 2 性能確認 dxm 0807について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認087-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; iostat -Dl 2 2
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0807A
画面・出力には AIX0807A が表示され、iostat -Dl 2 2 性能確認 dxm 0807 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0807B
画面・出力には AIX0807B が表示され、iostat -Dl 2 2 性能確認 dxm 0807 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。dxm を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0807C
画面・出力には AIX0807C が表示され、iostat -Dl 2 2 性能確認 dxm 0807 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0807A が画面・出力に表示されること
② ステップ2 の AIX0807B が画面・出力に表示されること
③ ステップ3 の AIX0807C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0818"><h3>iostat -Dl 2 2 性能確認 pi 0747</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>風花監査ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。風花監査の性能管理では pi とsvmon全体表示を作業票へ保管します。風花監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。風花監査の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、風花監査を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> iostat -Dl 2 2 性能確認 pi 0747について構成や状態を確認します。lssecattr -c 起動確認 enhanced_RBAC 0748ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはセキュリティでlssecattr -cを用い・enhanced_RBAC とユーザー属性を確認する。</li><li>B. 状態を読み取るための働きは性能管理でiostat -Dl 2 2を用い・pi とsvmon全体表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きは導入と起動でalt_disk_copyを用い・EFIX LABEL と起動デバイス設定を確認する。</li><li>D. 状態を読み取るための働きはLVMでlslvを用い・VG STATE と論理ボリューム配置を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「性能管理でiostat -Dl 2 2を用い、pi とsvmon全体表示を確認する」に対応する項目は性能確認 pi（性能・iost）です。性能に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、pi」で、確認対象はio・性能です。起動・lsseのA:は「セキュリティでlssecattr -cを用い」を述べ、対象は起動確認 enhanced_RBAC（起動・lsse）です。変更前・alt_のC:は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（変更・alt_）です。属性・lslvのD:は「LVMでlslvを用い、VG STATE」を述べ、対象はVG STATE（属性・lslv）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、pi」を指し、性能確認 piではio・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>iostat -Dl 2 2 性能確認 pi 0747</strong></p><p>検証目的: 性能管理のiostat -Dl 2 2 性能確認 pi 0747について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認027-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; iostat -Dl 2 2
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0747A
画面・出力には AIX0747A が表示され、iostat -Dl 2 2 性能確認 pi 0747 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0747B
画面・出力には AIX0747B が表示され、iostat -Dl 2 2 性能確認 pi 0747 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。pi を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0747C
画面・出力には AIX0747C が表示され、iostat -Dl 2 2 性能確認 pi 0747 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0747A が画面・出力に表示されること
② ステップ2 の AIX0747B が画面・出力に表示されること
③ ステップ3 の AIX0747C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0819"><h3>iostat -Dl 2 2 性能確認 po 0271</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>遠雷監査ではAIX 7.3の性能管理で iostat -Dl 2 2 を確認します。遠雷監査の性能管理では po とsvmon全体表示を点検票へ整理します。遠雷監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。遠雷監査の注意点として 区画CPU権利値の見落とし を避けるため svmon -G も併記します。性能監視の作業票として、遠雷監査を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> iostat -Dl 2 2 性能確認 po 0271の設定や表示を読む前に役割を確認します。lssecattr -c 起動確認 audit class 0272ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはセキュリティでlssecattr -cを用い・audit class とユーザー属性を確認する。</li><li>B. 対象資源に対する働きは性能管理でiostat -Dl 2 2を用い・po とsvmon全体表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはJFS2でchfsを用い・ファイルシステム使用率 とマウントオプションを確認する。</li><li>D. 対象資源に対する働きはページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「性能管理でiostat -Dl 2 2を用い、po とsvmon全体表示を確認する」に対応する項目は性能確認 po（性能・iost）です。性能に関する性能管理の仕様は「性能管理でiostat -Dl 2 2を用い、po」で、確認対象はio・性能です。起動・lsseのA:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（起動・lsse）です。バック・chfsのC:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象はバックアウト確認 ファイルシステム使（バッ・chfs）です。復旧前・lspsのD:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は復旧前確認 復旧手掛かり（復旧・lsps）です。「iostat -Dl 2 2」は「性能管理でiostat -Dl 2 2を用い、po」を指し、性能確認 poではio・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>iostat -Dl 2 2 性能確認 po 0271</strong></p><p>検証目的: 性能管理のiostat -Dl 2 2 性能確認 po 0271について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理性能確認031-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; iostat -Dl 2 2
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0271A
画面・出力には AIX0271A が表示され、iostat -Dl 2 2 性能確認 po 0271 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0271B
画面・出力には AIX0271B が表示され、iostat -Dl 2 2 性能確認 po 0271 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。po を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; vmstat 2 2
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0271C
画面・出力には AIX0271C が表示され、iostat -Dl 2 2 性能確認 po 0271 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0271A が画面・出力に表示されること
② ステップ2 の AIX0271B が画面・出力に表示されること
③ ステップ3 の AIX0271C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0820"><h3>lparstat -i 変更前確認 Entitled Capacity 0157</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>冬晴採取ではAIX 7.3の性能管理で lparstat -i を確認します。冬晴採取の性能管理では Entitled Capacity とAME統計を採取票へ記録します。冬晴採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。冬晴採取の注意点として 圧縮メモリー統計の読み落とし を避けるため svmon -G も併記します。性能監視の作業票として、冬晴採取を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lparstat -i 変更前確認 Entitled Capacity 0157を保守記録に説明する必要があります。usrck -n ALL 変更後確認 enhanced_RBAC 0158と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はセキュリティでusrck -n ALLを用い・enhanced_RBAC とRBAC属性を確認する。</li><li>B. 保守作業で参照する機能はJFS2でsnapを用い・agblksize と内部スナップショットを確認する。</li><li>C. 保守作業で参照する機能はセキュリティでchuserを用い・authorizations とRBAC属性を確認する。</li><li>D. 保守作業で参照する機能は性能管理でlparstat -iを用い・Entitled Capacity とAME統計を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「性能管理でlparstat -iを用い、Entitled Capacity」に対応する項目はEntitled Capacity（変更・lpar）です。変更前に関する性能管理の仕様は「性能管理でlparstat -iを用い、Entitled」で、確認対象はlp・変更前です。変更後・usrcのA:は「セキュリティでusrck -n ALLを用い」を述べ、対象は変更後確認 enhanced_RBA（変更・usrc）です。起動・snapのB:は「JFS2でsnapを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・snap）です。容量・chusのC:は「セキュリティでchuserを用い、authorizations」を述べ、対象は容量確認 authorization（容量・chus）です。「lparstat -i」は「性能管理でlparstat -iを用い、Entitled」を指し、Entitled Capacityではlp・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lparstat -i 変更前確認 Entitled Capacity 0157</strong></p><p>検証目的: 性能管理のlparstat -i 変更前確認 Entitled Capacity 0157について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認037-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lparstat -i
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0157A
画面・出力には AIX0157A が表示され、lparstat -i 変更前確認 Entitled Capacity 0157 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0157B
画面・出力には AIX0157B が表示され、lparstat -i 変更前確認 Entitled Capacity 0157 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Entitled Capacity を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; vmstat 2 2
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0157C
画面・出力には AIX0157C が表示され、lparstat -i 変更前確認 Entitled Capacity 0157 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0157A が画面・出力に表示されること
② ステップ2 の AIX0157B が画面・出力に表示されること
③ ステップ3 の AIX0157C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0821"><h3>lparstat -i 変更前確認 PhysB 0633</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 中級</p><p>朝霧採取ではAIX 7.3の性能管理で lparstat -i を確認します。朝霧採取の性能管理では PhysB とAME統計を判定票へ残します。朝霧採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。朝霧採取の注意点として 圧縮メモリー統計の読み落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、朝霧採取を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lparstat -i 変更前確認 PhysB 0633」を「usrck -n ALL 変更後確認 roles 0634」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割は性能管理でlparstat -iを用い・PhysB とAME統計を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はセキュリティでusrck -n ALLを用い・roles とRBAC属性を確認する。</li><li>C. 運用時に利用する技術的役割は導入と起動でnimadmを用い・altinst_rootvg とfileset一覧を確認する。</li><li>D. 運用時に利用する技術的役割はLVMでvaryonvgを用い・PP SIZE と物理ボリューム一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「性能管理でlparstat -iを用い、PhysB とAME統計を確認する」に対応する項目は変更前確認 PhysB（変更・lpar）です。変更前に関する性能管理の仕様は「性能管理でlparstat -iを用い、PhysB」で、確認対象はlp・変更前です。変更後・usrcのB:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は変更後確認 roles（変更・usrc）です。運用引・nimaのC:は「導入と起動でnimadmを用い、altinst_rootvg」を述べ、対象は運用引継ぎ altinst_root（運用・nima）です。障害切・varyのD:は「LVMでvaryonvgを用い、PP SIZE」を述べ、対象はPP SIZE（障害・vary）です。「lparstat -i」は「性能管理でlparstat -iを用い、PhysB」を指し、変更前確認 PhysBではlp・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lparstat -i 変更前確認 PhysB 0633</strong></p><p>検証目的: 性能管理のlparstat -i 変更前確認 PhysB 0633について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理変更前確認033-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lparstat -i
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0633A
画面・出力には AIX0633A が表示され、lparstat -i 変更前確認 PhysB 0633 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0633B
画面・出力には AIX0633B が表示され、lparstat -i 変更前確認 PhysB 0633 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PhysB を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0633C
画面・出力には AIX0633C が表示され、lparstat -i 変更前確認 PhysB 0633 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0633A が画面・出力に表示されること
② ステップ2 の AIX0633B が画面・出力に表示されること
③ ステップ3 の AIX0633C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0822"><h3>lparstat -i 容量確認 fre 0603</h3><p class="kb-meta">分類: 性能管理 ・ 難易度: 初級</p><p>秋声採取ではAIX 7.3の性能管理で lparstat -i を確認します。秋声採取の性能管理では fre とsvmon全体表示を作業票へ保管します。秋声採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。秋声採取の注意点として 区画CPU権利値の見落とし を避けるため vmstat 2 2 も併記します。性能監視の作業票として、秋声採取を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lparstat -i 容量確認 fre 0603について構成や状態を確認します。usrck -n ALL 性能確認 roles 0604ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはセキュリティでusrck -n ALLを用い・roles とユーザー属性を確認する。</li><li>B. 状態を読み取るための働きは性能管理でlparstat -iを用い・fre とsvmon全体表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>D. 状態を読み取るための働きはLVMでvaryonvgを用い・PVID と論理ボリューム配置を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「性能管理でlparstat -iを用い、fre とsvmon全体表示を確認する」に対応する項目は容量確認 fre（容量・lpar）です。容量に関する性能管理の仕様は「性能管理でlparstat -iを用い、fre」で、確認対象はlp・容量です。性能・usrcのA:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は性能確認 roles（性能・usrc）です。状態・イベ・vmstのC:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は状態判定 イベント転送（状態・vmst）です。起動・varyのD:は「LVMでvaryonvgを用い、PVID」を述べ、対象は起動確認 PVID（起動・vary）です。「lparstat -i」は「性能管理でlparstat -iを用い、fre」を指し、容量確認 freではlp・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lparstat -i 容量確認 fre 0603</strong></p><p>検証目的: 性能管理のlparstat -i 容量確認 fre 0603について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=性能管理容量確認003-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lparstat -i
→ Enter を押す
［画面・出力］
kthr     memory             page              faults        cpu
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
 1  0 205031 631304 0   0   0   0    0   0 1331 2202 528  2  3 95  0
確認コード AIX0603A
画面・出力には AIX0603A が表示され、lparstat -i 容量確認 fre 0603 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; svmon -G
→ Enter を押す
［画面・出力］
size      inuse       free        pin    virtual
memory      1048576     417374     631202      66533     151468
pg space     262144      31993
確認コード AIX0603B
画面・出力には AIX0603B が表示され、lparstat -i 容量確認 fre 0603 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。fre を読むため、性能管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; topas -D
→ Enter を押す
［画面・出力］
Disk     Busy%  KBPS     TPS   KB-R   ART   MRT   KB-W   AWT
hdisk0     3.0  56.0     3.5   0.0   0.0   5.4   56.0   5.8
確認コード AIX0603C
画面・出力には AIX0603C が表示され、lparstat -i 容量確認 fre 0603 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0603A が画面・出力に表示されること
② ステップ2 の AIX0603B が画面・出力に表示されること
③ ステップ3 の AIX0603C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>
