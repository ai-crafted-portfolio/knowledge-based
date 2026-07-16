---
search:
  exclude: true
---

# AIX 7.3 — 詳細 (3/6)

[← AIX 7.3 の概要へ戻る](index.md)


## SRCとログ


<section class="kb-item" id="c01-i0326"><h3>tail -f /tmp/myfile 構成照合 IDENTIFIER 0525</h3><p class="kb-meta">分類: SRCとログ ・ 難易度: 中級</p><p>深雪照合ではAIX 7.3のSRCとログで tail -f /tmp/myfile を確認します。深雪照合のSRCとログでは IDENTIFIER とinetdデバッグ出力を判定票へ残します。深雪照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。深雪照合の注意点として errpt識別子の取り違え を避けるため lssrc -s syslogd も併記します。システムリソースコントローラーの作業票として、深雪照合を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> tail -f /tmp/myfile 構成照合 IDENTIFIER 0525を保守記録に説明する必要があります。oslevel -s 変更前確認 bootlist 0526と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割は導入と起動でoslevel -sを用い・bootlist とOSレベル表示を確認する。</li><li>C. 運用時に利用する技術的役割はセキュリティでlsuserを用い・roles とロール一覧を確認する。</li><li>D. 運用時に利用する技術的役割は性能管理でvmo -aを用い・pi とvmstat表示を確認する。vmo -a 変更後確認 pi 0218固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「SRCとログでtail -f /tmp/myfileを用い」に対応する項目は構成照合 IDENTIFIER（構成・tail）です。構成に関するSRCとログの仕様は「SRCとログでtail -f /tmp/myfileを用い」で、確認対象はta・構成です。変更前・osleのB:は「導入と起動でoslevel -sを用い、bootlist」を述べ、対象は変更前確認 bootlist（変更・osle）です。性能・lsusのC:は「セキュリティでlsuserを用い、roles とロール一覧を確認する」を述べ、対象は性能確認 roles（性能・lsus）です。変更後・vmoのD:は「性能管理でvmo -aを用い、pi とvmstat表示を確認する」を述べ、対象は変更後確認 pi（変更・vmo）です。「tail -f /tmp/myfile」は「SRCとログでtail -f /tmp/myfileを用い」を指し、構成照合 IDENTIFIERではta・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>tail -f /tmp/myfile 構成照合 IDENTIFIER 0525</strong></p><p>検証目的: SRCとログのtail -f /tmp/myfile 構成照合 IDENTIFIER 0525について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=SRCとログ構成照合045-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。IDENTIFIER を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; tail -f /tmp/myfile
→ Enter を押す
［画面・出力］
Subsystem         Group            PID          Status
 syslogd          ras              2145         active
確認コード AIX0525A
画面・出力には AIX0525A が表示され、tail -f /tmp/myfile 構成照合 IDENTIFIER 0525 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。IDENTIFIER を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; errpt | head
→ Enter を押す
［画面・出力］
IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  DESCRIPTION
A6DF45AA   0715082626 P S SYSLOGD        SOFTWARE PROGRAM ERROR
確認コード AIX0525B
画面・出力には AIX0525B が表示され、tail -f /tmp/myfile 構成照合 IDENTIFIER 0525 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。IDENTIFIER を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; refresh -s syslogd
→ Enter を押す
［画面・出力］
syslog_ssw: default logging application set to syslogd
0513-095 The request for subsystem refresh was completed successfully.
確認コード AIX0525C
画面・出力には AIX0525C が表示され、tail -f /tmp/myfile 構成照合 IDENTIFIER 0525 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0525A が画面・出力に表示されること
② ステップ2 の AIX0525B が画面・出力に表示されること
③ ステップ3 の AIX0525C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0327"><h3>tail -f /tmp/myfile 構成照合 IDENTIFIER 0585</h3><p class="kb-meta">分類: SRCとログ ・ 難易度: 上級</p><p>花冷点検ではAIX 7.3のSRCとログで tail -f /tmp/myfile を確認します。花冷点検のSRCとログでは IDENTIFIER とinetdデバッグ出力を判定票へ残します。花冷点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。花冷点検の注意点として errpt識別子の取り違え を避けるため lssrc -s syslogd も併記します。システムリソースコントローラーの作業票として、花冷点検を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「tail -f /tmp/myfile 構成照合 IDENTIFIER 0585」を「oslevel -s 変更前確認 bootlist 0586」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割は導入と起動でoslevel -sを用い・bootlist とOSレベル表示を確認する。oslevel -s 変更前確認 bootlist 0586固有の属性も確認対象に含める。</li><li>B. 運用時に利用する技術的役割はSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。</li><li>D. 運用時に利用する技術的役割は性能管理でvmstat 2 2を用い・Busy% とvmstat表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「SRCとログでtail -f /tmp/myfileを用い」に対応する項目は構成照合 IDENTIFIER（構成・tail）です。構成に関するSRCとログの仕様は「SRCとログでtail -f /tmp/myfileを用い」で、確認対象はta・構成です。変更前・osleのA:は「導入と起動でoslevel -sを用い、bootlist」を述べ、対象は変更前確認 bootlist（変更・osle）です。復旧前・lspvのC:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は復旧前確認 状態確認（復旧・lspv）です。障害切・vmstのD:は「性能管理でvmstat 2 2を用い、Busy%」を述べ、対象は障害切り分け Busy%（障害・vmst）です。「tail -f /tmp/myfile」は「SRCとログでtail -f /tmp/myfileを用い」を指し、構成照合 IDENTIFIERではta・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>tail -f /tmp/myfile 構成照合 IDENTIFIER 0585</strong></p><p>検証目的: SRCとログのtail -f /tmp/myfile 構成照合 IDENTIFIER 0585について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=SRCとログ構成照合105-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。IDENTIFIER を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; tail -f /tmp/myfile
→ Enter を押す
［画面・出力］
Subsystem         Group            PID          Status
 syslogd          ras              2205         active
確認コード AIX0585A
画面・出力には AIX0585A が表示され、tail -f /tmp/myfile 構成照合 IDENTIFIER 0585 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。IDENTIFIER を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; errpt | head
→ Enter を押す
［画面・出力］
IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  DESCRIPTION
A6DF45AA   0715082626 P S SYSLOGD        SOFTWARE PROGRAM ERROR
確認コード AIX0585B
画面・出力には AIX0585B が表示され、tail -f /tmp/myfile 構成照合 IDENTIFIER 0585 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。IDENTIFIER を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; refresh -s syslogd
→ Enter を押す
［画面・出力］
syslog_ssw: default logging application set to syslogd
0513-095 The request for subsystem refresh was completed successfully.
確認コード AIX0585C
画面・出力には AIX0585C が表示され、tail -f /tmp/myfile 構成照合 IDENTIFIER 0585 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0585A が画面・出力に表示されること
② ステップ2 の AIX0585B が画面・出力に表示されること
③ ステップ3 の AIX0585C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0328"><h3>tail -f /tmp/myfile 構成照合 PID 0049</h3><p class="kb-meta">分類: SRCとログ ・ 難易度: 中級</p><p>銀砂照合ではAIX 7.3のSRCとログで tail -f /tmp/myfile を確認します。銀砂照合のSRCとログでは PID とinetdデバッグ出力を採取票へ記録します。銀砂照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。銀砂照合の注意点として errpt識別子の取り違え を避けるため errpt | head も併記します。システムリソースコントローラーの作業票として、銀砂照合を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「tail -f /tmp/myfile 構成照合 PID 0049」を「oslevel -s 変更前確認 fileset level 0050」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は導入と起動でoslevel -sを用い・fileset level とOSレベル表示を確認する。</li><li>B. 保守作業で参照する機能はセキュリティでlsuserを用い・enhanced_RBAC とロール一覧を確認する。</li><li>C. 保守作業で参照する機能は導入と起動でbosboot -a -dを用い・Technology Level とOSレベル表示を確認する。</li><li>D. 保守作業で参照する機能はSRCとログでtail -f /tmp/myfileを用い・PID とinetdデバッグ出力を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「SRCとログでtail -f /tmp/myfileを用い、PID」に対応する項目は構成照合 PID（構成・tail）です。SRCとログの仕様は「SRCとログでtail -f /tmp/myfileを用い、PID」で、確認対象はta・構成です。変更前・osleのA:は「導入と起動でoslevel -sを用い、fileset level」を述べ、対象はfileset level（変更・osle）です。性能・lsusのB:は「セキュリティでlsuserを用い、enhanced_RBAC」を述べ、対象は性能確認 enhanced_RBAC（性能・lsus）です。運用引・bosbのC:は「導入と起動でbosboot -a -dを用い、Technology」を述べ、対象はTechnology Level（運用・bosb）です。「tail -f /tmp/myfile」は「SRCとログでtail -f /tmp/myfileを用い、PID」を指し、構成照合 PIDではta・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>tail -f /tmp/myfile 構成照合 PID 0049</strong></p><p>検証目的: SRCとログのtail -f /tmp/myfile 構成照合 PID 0049について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=SRCとログ構成照合049-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PID を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; tail -f /tmp/myfile
→ Enter を押す
［画面・出力］
Subsystem         Group            PID          Status
 syslogd          ras              2149         active
確認コード AIX0049A
画面・出力には AIX0049A が表示され、tail -f /tmp/myfile 構成照合 PID 0049 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PID を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; refresh -s syslogd
→ Enter を押す
［画面・出力］
IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  DESCRIPTION
A6DF45AA   0715082626 P S SYSLOGD        SOFTWARE PROGRAM ERROR
確認コード AIX0049B
画面・出力には AIX0049B が表示され、tail -f /tmp/myfile 構成照合 PID 0049 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PID を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssrc -s syslogd
→ Enter を押す
［画面・出力］
syslog_ssw: default logging application set to syslogd
0513-095 The request for subsystem refresh was completed successfully.
確認コード AIX0049C
画面・出力には AIX0049C が表示され、tail -f /tmp/myfile 構成照合 PID 0049 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0049A が画面・出力に表示されること
② ステップ2 の AIX0049B が画面・出力に表示されること
③ ステップ3 の AIX0049C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0329"><h3>tail -f /tmp/myfile 構成照合 PID 0109</h3><p class="kb-meta">分類: SRCとログ ・ 難易度: 上級</p><p>梅雨晴点検ではAIX 7.3のSRCとログで tail -f /tmp/myfile を確認します。梅雨晴点検のSRCとログでは PID とinetdデバッグ出力を採取票へ記録します。梅雨晴点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。梅雨晴点検の注意点として errpt識別子の取り違え を避けるため errpt | head も併記します。システムリソースコントローラーの作業票として、梅雨晴点検を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> tail -f /tmp/myfile 構成照合 PID 0109を保守記録に説明する必要があります。oslevel -s 変更前確認 fileset level 0110と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は導入と起動でoslevel -sを用い・fileset level とOSレベル表示を確認する。</li><li>B. 保守作業で参照する機能はセキュリティでpwdck -n ALLを用い・authorizations とロール一覧を確認する。pwdck -n ALL 起動確認 authorizations固有の属性も確認対象に含める。</li><li>C. 保守作業で参照する機能はSRCとログでtail -f /tmp/myfileを用い・PID とinetdデバッグ出力を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能は導入と起動でbootlist -m normalを用い・fileset levelである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「SRCとログでtail -f /tmp/myfileを用い、PID」に対応する項目は構成照合 PID（構成・tail）です。構成に関するSRCとログの仕様は「SRCとログでtail -f /tmp/myfileを用い、PID」で、確認対象はta・構成です。変更前・osleのA:は「導入と起動でoslevel -sを用い、fileset level」を述べ、対象はfileset level（変更・osle）です。起動・pwdcのB:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は起動確認 authorization（起動・pwdc）です。容量・bootのD:は「導入と起動でbootlist -m normalを用い」を述べ、対象はfileset level（容量・boot）です。「tail -f /tmp/myfile」は「SRCとログでtail -f /tmp/myfileを用い、PID」を指し、構成照合 PIDではta・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>tail -f /tmp/myfile 構成照合 PID 0109</strong></p><p>検証目的: SRCとログのtail -f /tmp/myfile 構成照合 PID 0109について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=SRCとログ構成照合109-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PID を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; tail -f /tmp/myfile
→ Enter を押す
［画面・出力］
Subsystem         Group            PID          Status
 syslogd          ras              2209         active
確認コード AIX0109A
画面・出力には AIX0109A が表示され、tail -f /tmp/myfile 構成照合 PID 0109 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PID を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; refresh -s syslogd
→ Enter を押す
［画面・出力］
IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  DESCRIPTION
A6DF45AA   0715082626 P S SYSLOGD        SOFTWARE PROGRAM ERROR
確認コード AIX0109B
画面・出力には AIX0109B が表示され、tail -f /tmp/myfile 構成照合 PID 0109 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PID を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssrc -s syslogd
→ Enter を押す
［画面・出力］
syslog_ssw: default logging application set to syslogd
0513-095 The request for subsystem refresh was completed successfully.
確認コード AIX0109C
画面・出力には AIX0109C が表示され、tail -f /tmp/myfile 構成照合 PID 0109 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0109A が画面・出力に表示されること
② ステップ2 の AIX0109B が画面・出力に表示されること
③ ステップ3 の AIX0109C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0330"><h3>tail -f /tmp/myfile 運用引継ぎ Subsystem 0555</h3><p class="kb-meta">分類: SRCとログ ・ 難易度: 中級</p><p>青磁照合ではAIX 7.3のSRCとログで tail -f /tmp/myfile を確認します。青磁照合のSRCとログでは Subsystem とエラーログ一覧を作業票へ保管します。青磁照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。青磁照合の注意点として inetdデバッグ停止忘れ を避けるため lssrc -s syslogd も併記します。システムリソースコントローラーの作業票として、青磁照合を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> tail -f /tmp/myfile 運用引継ぎ Subsystem 0555について構成や状態を確認します。oslevel -s 容量確認 Technology Level 0556ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きは導入と起動でoslevel -sを用い・Technology Level と代替ディスク状態を確認する。</li><li>B. 状態を読み取るための働きは物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。lspv 変更前確認 保持設定固有の属性も確認対象に含める。</li><li>C. 状態を読み取るための働きはSRCとログでtail -f /tmp/myfileを用い・Subsystem とエラーログ一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 状態を読み取るための働きは性能管理でvmstat 2 2を用い・avm とtopasディスク表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「SRCとログでtail -f /tmp/myfileを用い、Subsystem」に対応する項目は運用引継ぎ Subsystem（運用・tail）です。運用引に関するSRCとログの仕様は「SRCとログでtail -f /tmp/myfileを用い」で、確認対象はta・運用引です。容量・osleのA:は「導入と起動でoslevel -sを用い、Technology」を述べ、対象はTechnology Level（容量・osle）です。変更前・lspvのB:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は変更前確認 保持設定（変更・lspv）です。起動・vmstのD:は「性能管理でvmstat 2 2を用い、avm」を述べ、対象は起動確認 avm（起動・vmst）です。「tail -f /tmp/myfile」は「SRCとログでtail -f /tmp/myfileを用い」を指し、運用引継ぎ Subsystemではta・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>tail -f /tmp/myfile 運用引継ぎ Subsystem 0555</strong></p><p>検証目的: SRCとログのtail -f /tmp/myfile 運用引継ぎ Subsystem 0555について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=SRCとログ運用引継ぎ075-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Subsystem を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; tail -f /tmp/myfile
→ Enter を押す
［画面・出力］
Subsystem         Group            PID          Status
 syslogd          ras              2175         active
確認コード AIX0555A
画面・出力には AIX0555A が表示され、tail -f /tmp/myfile 運用引継ぎ Subsystem 0555 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Subsystem を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; errpt | head
→ Enter を押す
［画面・出力］
IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  DESCRIPTION
A6DF45AA   0715082626 P S SYSLOGD        SOFTWARE PROGRAM ERROR
確認コード AIX0555B
画面・出力には AIX0555B が表示され、tail -f /tmp/myfile 運用引継ぎ Subsystem 0555 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Subsystem を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; refresh -s syslogd
→ Enter を押す
［画面・出力］
syslog_ssw: default logging application set to syslogd
0513-095 The request for subsystem refresh was completed successfully.
確認コード AIX0555C
画面・出力には AIX0555C が表示され、tail -f /tmp/myfile 運用引継ぎ Subsystem 0555 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0555A が画面・出力に表示されること
② ステップ2 の AIX0555B が画面・出力に表示されること
③ ステップ3 の AIX0555C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0331"><h3>tail -f /tmp/myfile 運用引継ぎ TIMESTAMP 0079</h3><p class="kb-meta">分類: SRCとログ ・ 難易度: 中級</p><p>秋桜照合ではAIX 7.3のSRCとログで tail -f /tmp/myfile を確認します。秋桜照合のSRCとログでは TIMESTAMP とエラーログ一覧を点検票へ整理します。秋桜照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。秋桜照合の注意点として inetdデバッグ停止忘れ を避けるため errpt | head も併記します。システムリソースコントローラーの作業票として、秋桜照合を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> tail -f /tmp/myfile 運用引継ぎ TIMESTAMP 0079の設定や表示を読む前に役割を確認します。oslevel -s 容量確認 altinst_rootvg 0080ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きは導入と起動でoslevel -sを用い・altinst_rootvg と代替ディスク状態を確認する。</li><li>B. 対象資源に対する働きはセキュリティでpwdck -n ALLを用い・authorizations と監査設定を確認する。</li><li>C. 対象資源に対する働きはSRCとログでtail -f /tmp/myfileを用い・TIMESTAMP とエラーログ一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きは導入と起動でbosboot -a -dを用い・bootlist と代替ディスク状態を確認する。bosboot -a -d 構成照合 bootlist 0692固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「SRCとログでtail -f /tmp/myfileを用い、TIMESTAMP」に対応する項目は運用引継ぎ TIMESTAMP（運用・tail）です。運用引に関するSRCとログの仕様は「SRCとログでtail -f /tmp/myfileを用い」で、確認対象はta・運用引です。容量・osleのA:は「導入と起動でoslevel -sを用い、altinst_rootvg」を述べ、対象は容量確認 altinst_rootv（容量・osle）です。障害切・pwdcのB:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は障害切り分け authorizati（障害・pwdc）です。構成・bosbのD:は「導入と起動でbosboot -a -dを用い、bootlist」を述べ、対象は構成照合 bootlist（構成・bosb）です。「tail -f /tmp/myfile」は「SRCとログでtail -f /tmp/myfileを用い」を指し、運用引継ぎ TIMESTAMPではta・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>tail -f /tmp/myfile 運用引継ぎ TIMESTAMP 0079</strong></p><p>検証目的: SRCとログのtail -f /tmp/myfile 運用引継ぎ TIMESTAMP 0079について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=SRCとログ運用引継ぎ079-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。TIMESTAMP を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; tail -f /tmp/myfile
→ Enter を押す
［画面・出力］
Subsystem         Group            PID          Status
 syslogd          ras              2179         active
確認コード AIX0079A
画面・出力には AIX0079A が表示され、tail -f /tmp/myfile 運用引継ぎ TIMESTAMP 0079 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。TIMESTAMP を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; refresh -s syslogd
→ Enter を押す
［画面・出力］
IDENTIFIER TIMESTAMP  T C RESOURCE_NAME  DESCRIPTION
A6DF45AA   0715082626 P S SYSLOGD        SOFTWARE PROGRAM ERROR
確認コード AIX0079B
画面・出力には AIX0079B が表示され、tail -f /tmp/myfile 運用引継ぎ TIMESTAMP 0079 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。TIMESTAMP を読むため、SRCとログ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssrc -s syslogd
→ Enter を押す
［画面・出力］
syslog_ssw: default logging application set to syslogd
0513-095 The request for subsystem refresh was completed successfully.
確認コード AIX0079C
画面・出力には AIX0079C が表示され、tail -f /tmp/myfile 運用引継ぎ TIMESTAMP 0079 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0079A が画面・出力に表示されること
② ステップ2 の AIX0079B が画面・出力に表示されること
③ ステップ3 の AIX0079C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


## エラーログ


<section class="kb-item" id="c01-i0332"><h3>chdev 属性照合 ボリューム状態</h3><p class="kb-meta">分類: エラーログ ・ 難易度: 上級</p><p>AIX 7.3 の エラーログ で扱う「chdev 属性照合 ボリューム状態」は、デバイス属性を変更する管理コマンドを属性照合の観点で確認する技術項目です。ERROR_IDENTIFIER 行とsysplanar0 077を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chdev 属性照合 ボリューム状態を保守記録に説明する必要があります。lscfg 障害切り分け ページング状態と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はデバイス属性を変更する管理コマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割は構成済みデバイスと VPD を表示するコマンドである。</li><li>C. 運用時に利用する技術的役割はデバイス管理でlscfg -vl ent0を用い・path status とODM属性を確認する。</li><li>D. 運用時に利用する技術的役割はネットワークでnetstat -vを用い・Gateway とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「デバイス属性を変更する管理コマンドである」に対応する項目は属性照合 ボリューム状態（属性・chde）です。エラーログの仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・属性・ボリです。障害切・lscfのB:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は障害切り分け ページング状態（障害・lscf）です。バック・lscfのC:は「デバイス管理でlscfg -vl ent0を用い、path」を述べ、対象はpath status（バッ・lscf）です。変更後・netsのD:は「ネットワークでnetstat -vを用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・nets）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、属性照合 ボリューム状態ではch・属性・ボリに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev 属性照合 ボリューム状態</strong></p><p>検証目的: エラーログのchdev 属性照合 ボリューム状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エラーログの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。ERROR_IDENTIFIER 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsps -a
→ Enter を押す
［画面・出力］
Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
画面・出力には Page が含まれ、chdev 属性照合 ボリューム状態の証跡を確認できます。
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


<section class="kb-item" id="c01-i0333"><h3>chdev 復旧前確認 仮想化表示</h3><p class="kb-meta">分類: エラーログ ・ 難易度: 中級</p><p>AIX 7.3 の エラーログ で扱う「chdev 復旧前確認 仮想化表示」は、デバイス属性を変更する管理コマンドを復旧前確認の観点で確認する技術項目です。ERROR_IDENTIFIER 行とsysplanar0 037を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chdev 復旧前確認 仮想化表示を保守記録に説明する必要があります。lscfg 一覧確認 LPAR表示と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割は構成済みデバイスと VPD を表示するコマンドである。</li><li>B. 仕様上の役割はデバイス属性を変更する管理コマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割は性能管理でtopas -Cを用い・Entitled Capacity とsvmon全体表示を確認する。</li><li>D. 仕様上の役割はSRCとログでsyslog_ssw -rを用い・PID とSRCサブシステム表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「デバイス属性を変更する管理コマンドである」に対応する項目は復旧前確認 仮想化表示（復旧・chde）です。エラーログの仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・復旧前です。一覧・表示・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は一覧確認 LPAR表示（一覧・lscf）です。構成・topaのC:は「性能管理でtopas -Cを用い、Entitled」を述べ、対象はEntitled Capacity（構成・topa）です。起動・syslのD:は「SRCとログでsyslog_ssw -rを用い、PID」を述べ、対象は起動確認 PID（起動・sysl）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、復旧前確認 仮想化表示ではch・復旧前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev 復旧前確認 仮想化表示</strong></p><p>検証目的: エラーログのchdev 復旧前確認 仮想化表示について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エラーログの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。ERROR_IDENTIFIER 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsps -a
→ Enter を押す
［画面・出力］
Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
画面・出力には Page が含まれ、chdev 復旧前確認 仮想化表示の証跡を確認できます。
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


<section class="kb-item" id="c01-i0334"><h3>errpt 一覧確認 監査証跡</h3><p class="kb-meta">分類: エラーログ ・ 難易度: 中級</p><p>AIX 7.3 の エラーログ で扱う「errpt 一覧確認 監査証跡」は、AIX エラーログから要約または詳細レポートを生成するコマンドを一覧確認の観点で確認する技術項目です。ERROR_IDENTIFIER 行とsysplanar0 045を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> errpt 一覧確認 監査証跡を保守記録に説明する必要があります。lsattr 詳細確認 確認範囲と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はデバイスや sys0 などの属性値を表示するコマンドである。</li><li>B. 保守作業で参照する機能はAIX エラーログから要約または詳細レポートを生成するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能は性能管理でiostat -Dl 2 2を用い・po とsvmon全体表示を確認する。</li><li>D. 保守作業で参照する機能はSRCとログでrefresh -s syslogdを用い・syslog.confである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は一覧確認 監査証跡（一覧・errp）です。エラーログの仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・一覧・監査です。詳細・確認・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は詳細確認 確認範囲（詳細・lsat）です。性能・iostのC:は「性能管理でiostat -Dl 2 2を用い、po」を述べ、対象は性能確認 po（性能・iost）です。監査・refrのD:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は監査記録 syslog.conf（監査・refr）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、一覧確認 監査証跡ではer・一覧・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>errpt 一覧確認 監査証跡</strong></p><p>検証目的: エラーログのerrpt 一覧確認 監査証跡について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エラーログの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。ERROR_IDENTIFIER 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lparstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
%user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
画面・出力には System が含まれ、errpt 一覧確認 監査証跡の証跡を確認できます。
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


<section class="kb-item" id="c01-i0335"><h3>errpt 障害切り分け ログ採取</h3><p class="kb-meta">分類: エラーログ ・ 難易度: 初級</p><p>AIX 7.3 の エラーログ で扱う「errpt 障害切り分け ログ採取」は、AIX エラーログから要約または詳細レポートを生成するコマンドを障害切り分けの観点で確認する技術項目です。ERROR_IDENTIFIER 行とsysplanar0 005を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> errpt 障害切り分け ログ採取を保守記録に説明する必要があります。lsattr 性能確認 実行結果と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はデバイスや sys0 などの属性値を表示するコマンドである。</li><li>B. 運用時に利用する技術的役割は導入と起動でinstallp -Cを用い・bootlist とfileset一覧を確認する。</li><li>C. 運用時に利用する技術的役割はAIX エラーログから要約または詳細レポートを生成するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はLVMでlsvg -lを用い・PP SIZE と物理ボリューム一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は障害切り分け ログ採取（障害・errp）です。エラーログの仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・障害切です。性能・実行・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は性能確認 実行結果（性能・lsat）です。障害切・instのB:は「導入と起動でinstallp -Cを用い、bootlist」を述べ、対象は障害切り分け bootlist（障害・inst）です。変更前・lsvgのD:は「LVMでlsvg -lを用い、PP SIZE」を述べ、対象はPP SIZE（変更・lsvg）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、障害切り分け ログ採取ではer・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>errpt 障害切り分け ログ採取</strong></p><p>検証目的: エラーログのerrpt 障害切り分け ログ採取について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エラーログの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。ERROR_IDENTIFIER 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lparstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
%user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
画面・出力には System が含まれ、errpt 障害切り分け ログ採取の証跡を確認できます。
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


<section class="kb-item" id="c01-i0336"><h3>lslv 性能確認 起動確認</h3><p class="kb-meta">分類: エラーログ ・ 難易度: 初級</p><p>AIX 7.3 の エラーログ で扱う「lslv 性能確認 起動確認」は、論理ボリュームの属性と割り当て情報を表示するコマンドを性能確認の観点で確認する技術項目です。ERROR_IDENTIFIER 行とsysplanar0 013を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 性能確認 起動確認を保守記録に説明する必要があります。lsps 変更前確認 停止確認と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割は論理ボリュームの属性と割り当て情報を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>C. 仕様上の役割はネットワークでlsdev -Cc adapterを用い・Media Speed Runningである。</li><li>D. 仕様上の役割はJFS2でcrfsを用い・agblksize とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は性能確認 起動確認（性能・lslv）です。エラーログの仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・性能・起動です。変更前・lspsのB:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は変更前確認 停止確認（変更・lsps）です。状態・lsdeのC:は「ネットワークでlsdev -Cc adapterを用い、Media」を述べ、対象はSpeed Running（状態・lsde）です。起動・crfsのD:は「JFS2でcrfsを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・crfs）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、性能確認 起動確認ではls・性能・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 性能確認 起動確認</strong></p><p>検証目的: エラーログのlslv 性能確認 起動確認について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エラーログの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。ERROR_IDENTIFIER 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt -a -N hdisk1
→ Enter を押す
［画面・出力］
LABEL: DISK_ERR4
RESOURCE NAME: hdisk1
Description
DISK OPERATION ERROR
画面・出力には LABEL が含まれ、lslv 性能確認 起動確認の証跡を確認できます。
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


<section class="kb-item" id="c01-i0337"><h3>lslv 詳細確認 構成照合</h3><p class="kb-meta">分類: エラーログ ・ 難易度: 中級</p><p>AIX 7.3 の エラーログ で扱う「lslv 詳細確認 構成照合」は、論理ボリュームの属性と割り当て情報を表示するコマンドを詳細確認の観点で確認する技術項目です。ERROR_IDENTIFIER 行とsysplanar0 053を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 詳細確認 構成照合を保守記録に説明する必要があります。lsps 状態判定 属性確認と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>B. 運用時に利用する技術的役割は論理ボリュームの属性と割り当て情報を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はセキュリティでlsroleを用い・roles とロール一覧を確認する。</li><li>D. 運用時に利用する技術的役割は導入と起動でoslevel -sを用い・bootlist とOSレベル表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は詳細確認 構成照合（詳細・lslv）です。エラーログの仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・詳細・構成です。状態・属性・lspsのA:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は状態判定 属性確認（状態・lsps）です。バック・lsroのC:は「セキュリティでlsroleを用い、roles とロール一覧を確認する」を述べ、対象はバックアウト確認 roles（バッ・lsro）です。変更前・osleのD:は「導入と起動でoslevel -sを用い、bootlist」を述べ、対象は変更前確認 bootlist（変更・osle）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、詳細確認 構成照合ではls・詳細・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 詳細確認 構成照合</strong></p><p>検証目的: エラーログのlslv 詳細確認 構成照合について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エラーログの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。ERROR_IDENTIFIER 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt -a -N hdisk1
→ Enter を押す
［画面・出力］
LABEL: DISK_ERR4
RESOURCE NAME: hdisk1
Description
DISK OPERATION ERROR
画面・出力には LABEL が含まれ、lslv 詳細確認 構成照合の証跡を確認できます。
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


<section class="kb-item" id="c01-i0338"><h3>lspv 変更前確認 保持設定</h3><p class="kb-meta">分類: エラーログ ・ 難易度: 中級</p><p>AIX 7.3 の エラーログ で扱う「lspv 変更前確認 保持設定」は、物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドを変更前確認の観点で確認する技術項目です。ERROR_IDENTIFIER 行とsysplanar0 021を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lspv 変更前確認 保持設定を保守記録に説明する必要があります。lsvg 復旧前確認 再開位置と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>C. 保守作業で参照する機能はネットワークでcfgmgrを用い・Link Status とEthernet統計を確認する。</li><li>D. 保守作業で参照する機能はJFS2でlogformを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は変更前確認 保持設定（変更・lspv）です。エラーログの仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・変更前です。復旧前・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は復旧前確認 再開位置（復旧・lsvg）です。性能・cfgmのC:は「ネットワークでcfgmgrを用い、Link Status」を述べ、対象はLink Status（性能・cfgm）です。監査・ファ・logfのD:は「JFS2でlogformを用い、ファイルシステム使用率」を述べ、対象は監査記録 ファイルシステム使用率（監査・logf）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、変更前確認 保持設定ではls・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 変更前確認 保持設定</strong></p><p>検証目的: エラーログのlspv 変更前確認 保持設定について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エラーログの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d4e21        rootvg          active
hdisk1          00f6a1b2c3d5e21        datavg          active
画面・出力には hdisk0 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。ERROR_IDENTIFIER 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1092
画面・出力には VOLUME が含まれ、lspv 変更前確認 保持設定の証跡を確認できます。
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


<section class="kb-item" id="c01-i0339"><h3>lspv 状態判定 照合単位</h3><p class="kb-meta">分類: エラーログ ・ 難易度: 中級</p><p>AIX 7.3 の エラーログ で扱う「lspv 状態判定 照合単位」は、物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドを状態判定の観点で確認する技術項目です。ERROR_IDENTIFIER 行とsysplanar0 061を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lspv 状態判定 照合単位を保守記録に説明する必要があります。lsvg 属性照合 設定値と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>B. 仕様上の役割はセキュリティでusrck -n ALLを用い・authorizations とロール一覧を確認する。</li><li>C. 仕様上の役割は導入と起動でbootlist -m normalを用い・fileset levelである。</li><li>D. 仕様上の役割は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は状態判定 照合単位（状態・lspv）です。エラーログの仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・状態・照合です。属性・設定・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は属性照合 設定値（属性・lsvg）です。構成・usrcのB:は「セキュリティでusrck -n ALLを用い」を述べ、対象は構成照合 authorization（構成・usrc）です。起動・bootのC:は「導入と起動でbootlist -m normalを用い」を述べ、対象はfileset level（起動・boot）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、状態判定 照合単位ではls・状態・照合に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 状態判定 照合単位</strong></p><p>検証目的: エラーログのlspv 状態判定 照合単位について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エラーログの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d4e61        rootvg          active
hdisk1          00f6a1b2c3d5e61        datavg          active
画面・出力には hdisk0 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。ERROR_IDENTIFIER 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1092
画面・出力には VOLUME が含まれ、lspv 状態判定 照合単位の証跡を確認できます。
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


<section class="kb-item" id="c01-i0340"><h3>vmstat 変更前確認 性能値</h3><p class="kb-meta">分類: エラーログ ・ 難易度: 中級</p><p>AIX 7.3 の エラーログ で扱う「vmstat 変更前確認 性能値」は、CPU、メモリー、ページング、AME 統計を表示する性能コマンドを変更前確認の観点で確認する技術項目です。ERROR_IDENTIFIER 行とsysplanar0 029を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> vmstat 変更前確認 性能値を保守記録に説明する必要があります。lparstat 復旧前確認 キュー状態と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>B. 運用時に利用する技術的役割はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はネットワークでno -aを用い・Gateway とEthernet統計を確認する。</li><li>D. 運用時に利用する技術的役割はSRCとログでerrpt -aを用い・IDENTIFIER とSRCサブシステム表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「CPU、メモリー、ページング、AME 統計を表示する性能コマンドである」に対応する項目は変更前確認 性能値（変更・vmst）です。エラーログの仕様は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」で、確認対象はvm・変更前です。復旧前・lparのA:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は復旧前確認 キュー状態（復旧・lpar）です。バック・noのC:は「ネットワークでno -aを用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・no）です。変更前・errpのD:は「SRCとログでerrpt -aを用い、IDENTIFIER」を述べ、対象は変更前確認 IDENTIFIER（変更・errp）です。「vmstat」は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を指し、変更前確認 性能値ではvm・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>vmstat 変更前確認 性能値</strong></p><p>検証目的: エラーログのvmstat 変更前確認 性能値について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エラーログの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsattr -E -l sys0 -a iostat
→ Enter を押す
［画面・出力］
iostat true Continuously maintain disk I/O history True
画面・出力には iostat が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。ERROR_IDENTIFIER 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; chdev -l sys0 -a iostat=true
→ Enter を押す
［画面・出力］
sys0 changed
画面・出力には sys0 が含まれ、vmstat 変更前確認 性能値の証跡を確認できます。
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


<section class="kb-item" id="c01-i0341"><h3>vmstat 状態判定 イベント転送</h3><p class="kb-meta">分類: エラーログ ・ 難易度: 上級</p><p>AIX 7.3 の エラーログ で扱う「vmstat 状態判定 イベント転送」は、CPU、メモリー、ページング、AME 統計を表示する性能コマンドを状態判定の観点で確認する技術項目です。ERROR_IDENTIFIER 行とsysplanar0 069を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> vmstat 状態判定 イベント転送を保守記録に説明する必要があります。lparstat 属性照合 受信先と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>C. 保守作業で参照する機能はデバイス管理でrmdev -Rl ent1を用い・Available とODM属性を確認する。</li><li>D. 保守作業で参照する機能はネットワークでno -aを用い・Link Status とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「CPU、メモリー、ページング、AME 統計を表示する性能コマンドである」に対応する項目は状態判定 イベント転送（状態・vmst）です。エラーログの仕様は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」で、確認対象はvm・状態・イベです。属性・受信・lparのB:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は属性照合 受信先（属性・lpar）です。性能・rmdeのC:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は性能確認 Available（性能・rmde）です。運用引・noのD:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（運用・no）です。「vmstat」は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を指し、状態判定 イベント転送ではvm・状態・イベに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>vmstat 状態判定 イベント転送</strong></p><p>検証目的: エラーログのvmstat 状態判定 イベント転送について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エラーログの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsattr -E -l sys0 -a iostat
→ Enter を押す
［画面・出力］
iostat true Continuously maintain disk I/O history True
画面・出力には iostat が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。ERROR_IDENTIFIER 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; chdev -l sys0 -a iostat=true
→ Enter を押す
［画面・出力］
sys0 changed
画面・出力には sys0 が含まれ、vmstat 状態判定 イベント転送の証跡を確認できます。
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


## システム属性


<section class="kb-item" id="c01-i0342"><h3>lparstat 変更前確認 キュー状態</h3><p class="kb-meta">分類: システム属性 ・ 難易度: 上級</p><p>AIX 7.3 の システム属性 で扱う「lparstat 変更前確認 キュー状態」は、LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドを変更前確認の観点で確認する技術項目です。AME 欄とhdisk8を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lparstat 変更前確認 キュー状態を同一分類のlsvg 構成照合 VG STATE 0001と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はLVMでlsvgを用い・VG STATE とミラーコピー状態を確認する。</li><li>B. 構成を確認する際の意味はSRCとログでstartsrc -s inetd -aを用い・syslog.confである。</li><li>C. 構成を確認する際の意味はLVMでvaryonvgを用い・PVID とミラーコピー状態を確認する。</li><li>D. 構成を確認する際の意味はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドである」に対応する項目は変更前確認 キュー状態（変更・lpar）です。システム属性の仕様は「LPAR の CPU 使用率、物理CPU消費、AME」で、確認対象はlp・変更前です。構成・lsvgのA:は「LVMでlsvgを用い、VG STATE」を述べ、対象はVG STATE（構成・lsvg）です。容量・starのB:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は容量確認 syslog.conf（容量・star）です。監査・varyのC:は「LVMでvaryonvgを用い、PVID」を述べ、対象は監査記録 PVID（監査・vary）です。「lparstat」は「LPAR の CPU 使用率、物理CPU消費、AME」を指し、変更前確認 キュー状態ではlp・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lparstat 変更前確認 キュー状態</strong></p><p>検証目的: システム属性のlparstat 変更前確認 キュー状態について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、システム属性の対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。AME 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lparstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
%user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
画面・出力には System が含まれ、lparstat 変更前確認 キュー状態の証跡を確認できます。
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


<section class="kb-item" id="c01-i0343"><h3>lparstat 状態判定 変更証跡</h3><p class="kb-meta">分類: システム属性 ・ 難易度: 中級</p><p>AIX 7.3 の システム属性 で扱う「lparstat 状態判定 変更証跡」は、LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドを状態判定の観点で確認する技術項目です。AME 欄とhdisk8を同じ記録で見比べることで、ボリュームグループの取り違えを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lparstat 状態判定 変更証跡を同一分類のlspv 障害切り分け 出力比較と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。</li><li>B. コマンドまたは機能の用途はLVMでvaryonvgを用い・PP SIZE と物理ボリューム一覧を確認する。varyonvg 障害切り分け PP SIZE 0266固有の属性も確認対象に含める。</li><li>C. コマンドまたは機能の用途はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途は性能管理でfilemonを用い・po とAME統計を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「LPAR の CPU 使用率、物理CPU消費、AME 関連値を表示するコマンドである」に対応する項目は状態判定 変更証跡（状態・lpar）です。システム属性の仕様は「LPAR の CPU 使用率、物理CPU消費、AME」で、確認対象はlp・状態・変更です。障害切・lspvのA:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は障害切り分け 出力比較（障害・lspv）です。障害切・varyのB:は「LVMでvaryonvgを用い、PP SIZE」を述べ、対象はPP SIZE（障害・vary）です。構成・fileのD:は「性能管理でfilemonを用い、po とAME統計を確認する」を述べ、対象は構成照合 po（構成・file）です。「lparstat」は「LPAR の CPU 使用率、物理CPU消費、AME」を指し、状態判定 変更証跡ではlp・状態・変更に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lparstat 状態判定 変更証跡</strong></p><p>検証目的: システム属性のlparstat 状態判定 変更証跡について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、システム属性の対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。AME 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lparstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
%user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
画面・出力には System が含まれ、lparstat 状態判定 変更証跡の証跡を確認できます。
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


<section class="kb-item" id="c01-i0344"><h3>lsattr 一覧確認 対象ファイル</h3><p class="kb-meta">分類: システム属性 ・ 難易度: 中級</p><p>AIX 7.3 の システム属性 で扱う「lsattr 一覧確認 対象ファイル」は、デバイスや sys0 などの属性値を表示するコマンドを一覧確認の観点で確認する技術項目です。AME 欄とhdisk8を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr 一覧確認 対象ファイルを同一分類のchdev 詳細確認 一致条件と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はデバイスや sys0 などの属性値を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はデバイス属性を変更する管理コマンドである。</li><li>C. コマンドまたは機能の用途はデバイス管理でodmget CuDvを用い・PVID とデバイス一覧を確認する。</li><li>D. コマンドまたは機能の用途はネットワークでentstat -d ent0を用い・Destination とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「デバイスや sys0 などの属性値を表示するコマンドである」に対応する項目は一覧確認 対象ファイル（一覧・lsat）です。システム属性の仕様は「デバイスや sys0 などの属性値を表示するコマンド」で、確認対象はls・一覧・対象です。詳細・一致・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は詳細確認 一致条件（詳細・chde）です。障害切・odmgのC:は「デバイス管理でodmget CuDvを用い、PVID」を述べ、対象は障害切り分け PVID（障害・odmg）です。構成・entsのD:は「ネットワークでentstat -d ent0を用い」を述べ、対象は構成照合 Destination（構成・ents）です。「lsattr」は「デバイスや sys0 などの属性値を表示するコマンド」を指し、一覧確認 対象ファイルではls・一覧・対象に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr 一覧確認 対象ファイル</strong></p><p>検証目的: システム属性のlsattr 一覧確認 対象ファイルについて、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、システム属性の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d4e16        rootvg          active
hdisk1          00f6a1b2c3d5e16        datavg          active
画面・出力には hdisk0 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。AME 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1092
画面・出力には VOLUME が含まれ、lsattr 一覧確認 対象ファイルの証跡を確認できます。
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


<section class="kb-item" id="c01-i0345"><h3>lsattr 障害切り分け 実行結果</h3><p class="kb-meta">分類: システム属性 ・ 難易度: 中級</p><p>AIX 7.3 の システム属性 で扱う「lsattr 障害切り分け 実行結果」は、デバイスや sys0 などの属性値を表示するコマンドを障害切り分けの観点で確認する技術項目です。AME 欄とhdisk8を同じ記録で見比べることで、PVID の誤読を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr 障害切り分け 実行結果を同一分類のchdev 性能確認 識別値と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はデバイス属性を変更する管理コマンドである。</li><li>B. 構成を確認する際の意味はデバイスや sys0 などの属性値を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はJFS2でfsckを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li><li>D. 構成を確認する際の意味はセキュリティでrbacqry -u user1 -Tを用い・user attributesである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「デバイスや sys0 などの属性値を表示するコマンドである」に対応する項目は障害切り分け 実行結果（障害・lsat）です。システム属性の仕様は「デバイスや sys0 などの属性値を表示するコマンド」で、確認対象はls・障害切です。性能・識別・chdeのA:は「デバイス属性を変更する管理コマンド」を述べ、対象は性能確認 識別値（性能・chde）です。容量・ファ・fsckのC:は「JFS2でfsckを用い、ファイルシステム使用率」を述べ、対象は容量確認 ファイルシステム使用率（容量・fsck）です。バック・rbacのD:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はuser attributes（バッ・rbac）です。「lsattr」は「デバイスや sys0 などの属性値を表示するコマンド」を指し、障害切り分け 実行結果ではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr 障害切り分け 実行結果</strong></p><p>検証目的: システム属性のlsattr 障害切り分け 実行結果について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、システム属性の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d4e56        rootvg          active
hdisk1          00f6a1b2c3d5e56        datavg          active
画面・出力には hdisk0 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。AME 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1092
画面・出力には VOLUME が含まれ、lsattr 障害切り分け 実行結果の証跡を確認できます。
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


<section class="kb-item" id="c01-i0346"><h3>lscfg 属性照合 時刻情報</h3><p class="kb-meta">分類: システム属性 ・ 難易度: 中級</p><p>AIX 7.3 の システム属性 で扱う「lscfg 属性照合 時刻情報」は、構成済みデバイスと VPD を表示するコマンドを属性照合の観点で確認する技術項目です。AME 欄とhdisk8を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lscfg 属性照合 時刻情報を同一分類のvmstat 障害切り分け 統計値と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>B. 管理対象との関係を表す説明はJFS2でsnapを用い・agblksize とファイルシステム属性を確認する。</li><li>C. 管理対象との関係を表す説明はセキュリティでsetsecattrを用い・enhanced_RBAC と監査設定を確認する。</li><li>D. 管理対象との関係を表す説明は構成済みデバイスと VPD を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「構成済みデバイスと VPD を表示するコマンドである」に対応する項目は属性照合 時刻情報（属性・lscf）です。システム属性の仕様は「構成済みデバイスと VPD を表示するコマンド」で、確認対象はls・属性・時刻です。障害切・vmstのA:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は障害切り分け 統計値（障害・vmst）です。状態・snapのB:は「JFS2でsnapを用い、agblksize」を述べ、対象は状態確認 agblksize（状態・snap）です。性能・setsのC:は「セキュリティでsetsecattrを用い」を述べ、対象は性能確認 enhanced_RBAC（性能・sets）です。「lscfg」は「構成済みデバイスと VPD を表示するコマンド」を指し、属性照合 時刻情報ではls・属性・時刻に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lscfg 属性照合 時刻情報</strong></p><p>検証目的: システム属性のlscfg 属性照合 時刻情報について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、システム属性の対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。AME 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt -a -N hdisk1
→ Enter を押す
［画面・出力］
LABEL: DISK_ERR4
RESOURCE NAME: hdisk1
Description
DISK OPERATION ERROR
画面・出力には LABEL が含まれ、lscfg 属性照合 時刻情報の証跡を確認できます。
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


<section class="kb-item" id="c01-i0347"><h3>lscfg 復旧前確認 障害記録</h3><p class="kb-meta">分類: システム属性 ・ 難易度: 初級</p><p>AIX 7.3 の システム属性 で扱う「lscfg 復旧前確認 障害記録」は、構成済みデバイスと VPD を表示するコマンドを復旧前確認の観点で確認する技術項目です。AME 欄とhdisk8を同じ記録で見比べることで、ページング使用率の見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lscfg 復旧前確認 障害記録を同一分類のvmstat 一覧確認 出力見出しと比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は構成済みデバイスと VPD を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>C. 構成を確認する際の意味はセキュリティでsetsecattrを用い・audit class とRBAC属性を確認する。</li><li>D. 構成を確認する際の意味は導入と起動でalt_disk_mksysbを用い・mksysb image と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「構成済みデバイスと VPD を表示するコマンドである」に対応する項目は復旧前確認 障害記録（復旧・lscf）です。システム属性の仕様は「構成済みデバイスと VPD を表示するコマンド」で、確認対象はls・復旧前です。一覧・出力・vmstのB:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は一覧確認 出力見出し（一覧・vmst）です。運用引・setsのC:は「セキュリティでsetsecattrを用い、audit class」を述べ、対象はaudit class（運用・sets）です。バック・alt_のD:は「導入と起動でalt_disk_mksysbを用い、mksysb」を述べ、対象はmksysb image（バッ・alt_）です。「lscfg」は「構成済みデバイスと VPD を表示するコマンド」を指し、復旧前確認 障害記録ではls・復旧前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lscfg 復旧前確認 障害記録</strong></p><p>検証目的: システム属性のlscfg 復旧前確認 障害記録について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、システム属性の対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。AME 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt -a -N hdisk1
→ Enter を押す
［画面・出力］
LABEL: DISK_ERR4
RESOURCE NAME: hdisk1
Description
DISK OPERATION ERROR
画面・出力には LABEL が含まれ、lscfg 復旧前確認 障害記録の証跡を確認できます。
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


<section class="kb-item" id="c01-i0348"><h3>lsps 性能確認 停止確認</h3><p class="kb-meta">分類: システム属性 ・ 難易度: 中級</p><p>AIX 7.3 の システム属性 で扱う「lsps 性能確認 停止確認」は、ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドを性能確認の観点で確認する技術項目です。AME 欄とhdisk8を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsps 性能確認 停止確認を同一分類のerrpt 変更前確認 再読込と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>B. コマンドまたは機能の用途はSRCとログでrefresh -s syslogdを用い・IDENTIFIERである。</li><li>C. コマンドまたは機能の用途はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はデバイス管理でlsattr -El hdisk0を用い・PVID と診断対象表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドである」に対応する項目は性能確認 停止確認（性能・lsps）です。システム属性の仕様は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」で、確認対象はls・性能・停止です。変更前・errpのA:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は変更前確認 再読込（変更・errp）です。障害切・refrのB:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は障害切り分け IDENTIFIER（障害・refr）です。構成・lsatのD:は「デバイス管理でlsattr -El hdisk0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lsat）です。「lsps」は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を指し、性能確認 停止確認ではls・性能・停止に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsps 性能確認 停止確認</strong></p><p>検証目的: システム属性のlsps 性能確認 停止確認について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、システム属性の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsattr -E -l sys0 -a iostat
→ Enter を押す
［画面・出力］
iostat true Continuously maintain disk I/O history True
画面・出力には iostat が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。AME 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; chdev -l sys0 -a iostat=true
→ Enter を押す
［画面・出力］
sys0 changed
画面・出力には sys0 が含まれ、lsps 性能確認 停止確認の証跡を確認できます。
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


<section class="kb-item" id="c01-i0349"><h3>lsps 詳細確認 メッセージ行</h3><p class="kb-meta">分類: システム属性 ・ 難易度: 中級</p><p>AIX 7.3 の システム属性 で扱う「lsps 詳細確認 メッセージ行」は、ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドを詳細確認の観点で確認する技術項目です。AME 欄とhdisk8を同じ記録で見比べることで、資源名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsps 詳細確認 メッセージ行を同一分類のerrpt 状態判定 表形式と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>B. 管理対象との関係を表す説明はデバイス管理でchdev -l hdisk0を用い・location code とデバイス一覧を確認する。</li><li>C. 管理対象との関係を表す説明はネットワークでifconfig en0を用い・Media Speed Running とMTU属性を確認する。</li><li>D. 管理対象との関係を表す説明はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンドである」に対応する項目は詳細確認 メッセージ行（詳細・lsps）です。システム属性の仕様は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」で、確認対象はls・詳細・メッです。状態・表形・errpのA:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は状態判定 表形式（状態・errp）です。状態・chdeのB:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象はlocation code（状態・chde）です。性能・ifcoのC:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（性能・ifco）です。「lsps」は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を指し、詳細確認 メッセージ行ではls・詳細・メッに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsps 詳細確認 メッセージ行</strong></p><p>検証目的: システム属性のlsps 詳細確認 メッセージ行について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、システム属性の対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsattr -E -l sys0 -a iostat
→ Enter を押す
［画面・出力］
iostat true Continuously maintain disk I/O history True
画面・出力には iostat が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。AME 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; chdev -l sys0 -a iostat=true
→ Enter を押す
［画面・出力］
sys0 changed
画面・出力には sys0 が含まれ、lsps 詳細確認 メッセージ行の証跡を確認できます。
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


<section class="kb-item" id="c01-i0350"><h3>lsvg 変更前確認 再開位置</h3><p class="kb-meta">分類: システム属性 ・ 難易度: 上級</p><p>AIX 7.3 の システム属性 で扱う「lsvg 変更前確認 再開位置」は、ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドを変更前確認の観点で確認する技術項目です。AME 欄とhdisk8を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg 変更前確認 再開位置を同一分類のlslv 復旧前確認 サンプル採取と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明は論理ボリュームの属性と割り当て情報を表示するコマンドである。</li><li>B. 管理対象との関係を表す説明はSRCとログでlssrc -s syslogdを用い・PID とSRCサブシステム表示を確認する。</li><li>C. 管理対象との関係を表す説明はデバイス管理でlsdev -Cc diskを用い・attribute と診断対象表示を確認する。</li><li>D. 管理対象との関係を表す説明はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドである」に対応する項目は変更前確認 再開位置（変更・lsvg）です。システム属性の仕様は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」で、確認対象はls・変更前です。復旧前・lslvのA:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は復旧前確認 サンプル採取（復旧・lslv）です。状態・lssrのB:は「SRCとログでlssrc -s syslogdを用い、PID」を述べ、対象は状態確認 PID（状態・lssr）です。起動・lsdeのC:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 attribute（起動・lsde）です。「lsvg」は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を指し、変更前確認 再開位置ではls・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg 変更前確認 再開位置</strong></p><p>検証目的: システム属性のlsvg 変更前確認 再開位置について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、システム属性の対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。AME 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsps -a
→ Enter を押す
［画面・出力］
Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
画面・出力には Page が含まれ、lsvg 変更前確認 再開位置の証跡を確認できます。
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


<section class="kb-item" id="c01-i0351"><h3>lsvg 状態判定 製品レベル</h3><p class="kb-meta">分類: システム属性 ・ 難易度: 中級</p><p>AIX 7.3 の システム属性 で扱う「lsvg 状態判定 製品レベル」は、ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドを状態判定の観点で確認する技術項目です。AME 欄とhdisk8を同じ記録で見比べることで、停止中の論理ボリューム見落としを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg 状態判定 製品レベルを同一分類のlslv 属性照合 エラー詳細と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味は論理ボリュームの属性と割り当て情報を表示するコマンドである。</li><li>B. 構成を確認する際の意味はLVMでlspvを用い・MIRROR WRITE CONSISTENCY と物理ボリューム一覧を確認する。</li><li>C. 構成を確認する際の意味はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味は性能管理でvmo -aを用い・Entitled Capacity とAME統計を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンドである」に対応する項目は状態判定 製品レベル（状態・lsvg）です。システム属性の仕様は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」で、確認対象はls・状態・製品です。属性・エラ・lslvのA:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は属性照合 エラー詳細（属性・lslv）です。容量・lspvのB:は「LVMでlspvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（容量・lspv）です。バック・vmoのD:は「性能管理でvmo -aを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（バッ・vmo）です。「lsvg」は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を指し、状態判定 製品レベルではls・状態・製品に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg 状態判定 製品レベル</strong></p><p>検証目的: システム属性のlsvg 状態判定 製品レベルについて、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、システム属性の対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。AME 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsps -a
→ Enter を押す
［画面・出力］
Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
画面・出力には Page が含まれ、lsvg 状態判定 製品レベルの証跡を確認できます。
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


## セキュリティ


<section class="kb-item" id="c01-i0352"><h3>chuser 変更前確認 authorizations 0740</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>薄明監査ではAIX 7.3のセキュリティで chuser を確認します。薄明監査のセキュリティでは authorizations とユーザー属性を引継ぎ票へ保管します。薄明監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。薄明監査の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、薄明監査を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chuser 変更前確認 authorizations 0740の技術的な意味を資料で確認するとき、rmdev -Rl ent1 変更後確認 microcode level 0741との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はデバイス管理でrmdev -Rl ent1を用い・microcode level と診断対象表示を確認する。</li><li>B. コマンドまたは機能の用途はネットワークでno -aを用い・Gateway とアダプター一覧を確認する。</li><li>C. コマンドまたは機能の用途はセキュリティでchuserを用い・authorizations とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はJFS2でsnapを用い・lff とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「セキュリティでchuserを用い、authorizations」に対応する項目は変更前確認 authorizatio（変更・chus）です。変更前に関するセキュリティの仕様は「セキュリティでchuserを用い、authorizations」で、確認対象はch・変更前です。変更後・rmdeのA:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象はmicrocode level（変更・rmde）です。運用引・noのB:は「ネットワークでno -aを用い、Gateway」を述べ、対象は運用引継ぎ Gateway（運用・no）です。障害切・snapのD:は「JFS2でsnapを用い、lff とマウントオプションを確認する」を述べ、対象は障害切り分け lff（障害・snap）です。「chuser」は「セキュリティでchuserを用い、authorizations」を指し、変更前確認 authorizatioではch・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chuser 変更前確認 authorizations 0740</strong></p><p>検証目的: セキュリティのchuser 変更前確認 authorizations 0740について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更前確認020-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0740A
画面・出力には AIX0740A が表示され、chuser 変更前確認 authorizations 0740 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0740B
画面・出力には AIX0740B が表示され、chuser 変更前確認 authorizations 0740 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0740C
画面・出力には AIX0740C が表示され、chuser 変更前確認 authorizations 0740 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0740A が画面・出力に表示されること
② ステップ2 の AIX0740B が画面・出力に表示されること
③ ステップ3 の AIX0740C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0353"><h3>chuser 変更前確認 authorizations 0800</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>青葉変更ではAIX 7.3のセキュリティで chuser を確認します。青葉変更のセキュリティでは authorizations とユーザー属性を引継ぎ票へ保管します。青葉変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。青葉変更の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、青葉変更を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chuser 変更前確認 authorizations 0800を同一分類のno -a 属性確認 Destination 0821と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はネットワークでno -aを用い・Destination とMTU属性を確認する。</li><li>B. コマンドまたは機能の用途はネットワークでnetstat -rnを用い・Media Speed Runningである。</li><li>C. コマンドまたは機能の用途はセキュリティでpwdck -n ALLを用い・authorizations とRBAC属性を確認する。</li><li>D. コマンドまたは機能の用途はセキュリティでchuserを用い・authorizations とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更前・chusでDの記述「セキュリティでchuserを用い、authorizations」に対応する項目は変更前確認 authorizatio（変更・chus）です。変更前に関するセキュリティの仕様は「セキュリティでchuserを用い、authorizations」で、確認対象はch・変更前です。属性・noのA:は「ネットワークでno -aを用い、Destination」を述べ、対象は属性確認 Destination（属性・no）です。状態・netsのB:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（状態・nets）です。変更前・pwdcのC:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は変更前確認 authorizatio（変更・pwdc）です。「chuser」は「セキュリティでchuserを用い、authorizations」を指し、変更前確認 authorizatioではch・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chuser 変更前確認 authorizations 0800</strong></p><p>検証目的: セキュリティのchuser 変更前確認 authorizations 0800について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更前確認080-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0800A
画面・出力には AIX0800A が表示され、chuser 変更前確認 authorizations 0800 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0800B
画面・出力には AIX0800B が表示され、chuser 変更前確認 authorizations 0800 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0800C
画面・出力には AIX0800C が表示され、chuser 変更前確認 authorizations 0800 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0800A が画面・出力に表示されること
② ステップ2 の AIX0800B が画面・出力に表示されること
③ ステップ3 の AIX0800C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0354"><h3>chuser 変更前確認 user attributes 0264</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>霜月監査ではAIX 7.3のセキュリティで chuser を確認します。霜月監査のセキュリティでは user attributes とユーザー属性を同じ証跡に残します。霜月監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。霜月監査の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、霜月監査を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chuser 変更前確認 user attributes 0264を同一分類のrmdev -Rl ent1 変更後確認 PVID 0265と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はセキュリティでchuserを用い・user attributes とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はデバイス管理でrmdev -Rl ent1を用い・PVID と診断対象表示を確認する。</li><li>C. 構成を確認する際の意味はSRCとログでsyslog_ssw -rを用い・PID とSRCサブシステム表示を確認する。</li><li>D. 構成を確認する際の意味はデバイス属性を変更する管理コマンドである。chdev 復旧前確認 仮想化表示固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでchuserを用い、user attributes」に対応する項目はuser attributes（変更・chus）です。変更前に関するセキュリティの仕様は「セキュリティでchuserを用い、user attributes」で、確認対象はch・変更前です。変更後・rmdeのB:は「デバイス管理でrmdev -Rl ent1を用い、PVID」を述べ、対象は変更後確認 PVID（変更・rmde）です。起動・syslのC:は「SRCとログでsyslog_ssw -rを用い、PID」を述べ、対象は起動確認 PID（起動・sysl）です。復旧前・chdeのD:は「デバイス属性を変更する管理コマンド」を述べ、対象は復旧前確認 仮想化表示（復旧・chde）です。「chuser」は「セキュリティでchuserを用い、user attributes」を指し、user attributesではch・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chuser 変更前確認 user attributes 0264</strong></p><p>検証目的: セキュリティのchuser 変更前確認 user attributes 0264について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更前確認024-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0264A
画面・出力には AIX0264A が表示され、chuser 変更前確認 user attributes 0264 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0264B
画面・出力には AIX0264B が表示され、chuser 変更前確認 user attributes 0264 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0264C
画面・出力には AIX0264C が表示され、chuser 変更前確認 user attributes 0264 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0264A が画面・出力に表示されること
② ステップ2 の AIX0264B が画面・出力に表示されること
③ ステップ3 の AIX0264C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0355"><h3>chuser 変更前確認 user attributes 0324</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>若草変更ではAIX 7.3のセキュリティで chuser を確認します。若草変更のセキュリティでは user attributes とユーザー属性を同じ証跡に残します。若草変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若草変更の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、若草変更を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chuser 変更前確認 user attributes 0324の技術的な意味を資料で確認するとき、rmdev -Rl ent1 変更後確認 PVID 0325との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はデバイス管理でrmdev -Rl ent1を用い・PVID と診断対象表示を確認する。rmdev -Rl ent1 変更後確認 PVID 0325固有の属性も確認対象に含める。</li><li>B. 構成を確認する際の意味はセキュリティでchuserを用い・user attributes とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はSRCとログでerrptを用い・Status とSRCサブシステム表示を確認する。</li><li>D. 構成を確認する際の意味はLVMでmigratepvを用い・PP SIZE とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでchuserを用い、user attributes」に対応する項目はuser attributes（変更・chus）です。変更前に関するセキュリティの仕様は「セキュリティでchuserを用い、user attributes」で、確認対象はch・変更前です。変更後・rmdeのA:は「デバイス管理でrmdev -Rl ent1を用い、PVID」を述べ、対象は変更後確認 PVID（変更・rmde）です。属性・errpのC:は「SRCとログでerrptを用い、Status」を述べ、対象は属性確認 Status（属性・errp）です。バック・migrのD:は「LVMでmigratepvを用い、PP SIZE」を述べ、対象はPP SIZE（バッ・migr）です。「chuser」は「セキュリティでchuserを用い、user attributes」を指し、user attributesではch・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chuser 変更前確認 user attributes 0324</strong></p><p>検証目的: セキュリティのchuser 変更前確認 user attributes 0324について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更前確認084-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0324A
画面・出力には AIX0324A が表示され、chuser 変更前確認 user attributes 0324 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0324B
画面・出力には AIX0324B が表示され、chuser 変更前確認 user attributes 0324 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0324C
画面・出力には AIX0324C が表示され、chuser 変更前確認 user attributes 0324 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0324A が画面・出力に表示されること
② ステップ2 の AIX0324B が画面・出力に表示されること
③ ステップ3 の AIX0324C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0356"><h3>chuser 容量確認 authorizations 0770</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>桜雲復旧ではAIX 7.3のセキュリティで chuser を確認します。桜雲復旧のセキュリティでは authorizations とRBAC属性を確認票へ整理します。桜雲復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。桜雲復旧の注意点として 監査データ未取得でのroleqry実行 を避けるため lsuser user1 も併記します。権限管理の作業票として、桜雲復旧を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chuser 容量確認 authorizations 0770の役割を調べています。rmdev -Rl ent1 性能確認 attribute 0771の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はデバイス管理でrmdev -Rl ent1を用い・attribute とODM属性を確認する。</li><li>B. 障害切り分けに用いる役割はネットワークでno -aを用い・Media Speed Running と経路表を確認する。</li><li>C. 障害切り分けに用いる役割はセキュリティでchuserを用い・authorizations とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割はJFS2でsnapを用い・agblksize と内部スナップショットを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでchuserを用い、authorizations」に対応する項目は容量確認 authorization（容量・chus）です。容量に関するセキュリティの仕様は「セキュリティでchuserを用い、authorizations」で、確認対象はch・容量です。性能・rmdeのA:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は性能確認 attribute（性能・rmde）です。構成・noのB:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（構成・no）です。起動・snapのD:は「JFS2でsnapを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・snap）です。「chuser」は「セキュリティでchuserを用い、authorizations」を指し、容量確認 authorizationではch・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chuser 容量確認 authorizations 0770</strong></p><p>検証目的: セキュリティのchuser 容量確認 authorizations 0770について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ容量確認050-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0770A
画面・出力には AIX0770A が表示され、chuser 容量確認 authorizations 0770 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0770B
画面・出力には AIX0770B が表示され、chuser 容量確認 authorizations 0770 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0770C
画面・出力には AIX0770C が表示され、chuser 容量確認 authorizations 0770 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0770A が画面・出力に表示されること
② ステップ2 の AIX0770B が画面・出力に表示されること
③ ステップ3 の AIX0770C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0357"><h3>chuser 容量確認 user attributes 0294</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>星霜復旧ではAIX 7.3のセキュリティで chuser を確認します。星霜復旧のセキュリティでは user attributes とRBAC属性を変更票へ記録します。星霜復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。星霜復旧の注意点として 監査データ未取得でのroleqry実行 を避けるため lsrole ALL も併記します。権限管理の作業票として、星霜復旧を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chuser 容量確認 user attributes 0294に関する障害切り分けの前提を確認しています。rmdev -Rl ent1 性能確認 Available 0295の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはデバイス管理でrmdev -Rl ent1を用い・Available とODM属性を確認する。</li><li>B. 機能の説明としてはSRCとログでsyslog_ssw -rを用い・TIMESTAMP とsyslog設定変換を確認する。</li><li>C. 機能の説明としてはセキュリティでchuserを用い・user attributes とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはデバイス属性を変更する管理コマンドである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでchuserを用い、user attributes」に対応する項目はuser attributes（容量・chus）です。容量に関するセキュリティの仕様は「セキュリティでchuserを用い、user attributes」で、確認対象はch・容量です。性能・rmdeのA:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は性能確認 Available（性能・rmde）です。障害切・syslのB:は「SRCとログでsyslog_ssw -rを用い、TIMESTAMP」を述べ、対象は障害切り分け TIMESTAMP（障害・sysl）です。一覧・一致・chdeのD:は「デバイス属性を変更する管理コマンド」を述べ、対象は一覧確認 一致条件（一覧・chde）です。「chuser」は「セキュリティでchuserを用い、user attributes」を指し、user attributesではch・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chuser 容量確認 user attributes 0294</strong></p><p>検証目的: セキュリティのchuser 容量確認 user attributes 0294について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ容量確認054-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0294A
画面・出力には AIX0294A が表示され、chuser 容量確認 user attributes 0294 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0294B
画面・出力には AIX0294B が表示され、chuser 容量確認 user attributes 0294 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0294C
画面・出力には AIX0294C が表示され、chuser 容量確認 user attributes 0294 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0294A が画面・出力に表示されること
② ステップ2 の AIX0294B が画面・出力に表示されること
③ ステップ3 の AIX0294C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0358"><h3>chuser 状態確認 enhanced_RBAC 0453</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>月影整理ではAIX 7.3のセキュリティで chuser を確認します。月影整理のセキュリティでは enhanced_RBAC と監査設定を判定票へ残します。月影整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。月影整理の注意点として ロール割当と権限文字列の不一致 を避けるため lsrole ALL も併記します。権限管理の作業票として、月影整理を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chuser 状態確認 enhanced_RBAC 0453を保守記録に説明する必要があります。rmdev -Rl ent1 構成照合 attribute 0454と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はセキュリティでchuserを用い・enhanced_RBAC と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はデバイス管理でrmdev -Rl ent1を用い・attribute とデバイス一覧を確認する。</li><li>C. 運用時に利用する技術的役割はSRCとログでerrptを用い・Status とエラーログ一覧を確認する。</li><li>D. 運用時に利用する技術的役割はJFS2でsplitcopyを用い・isnapshot とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでchuserを用い、enhanced_RBAC と監査設定を確認する」に対応する項目は状態確認 enhanced_RBAC（状態・chus）です。状態に関するセキュリティの仕様は「セキュリティでchuserを用い、enhanced_RBAC」で、確認対象はch・状態です。構成・rmdeのB:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は構成照合 attribute（構成・rmde）です。性能・errpのC:は「SRCとログでerrptを用い、Status」を述べ、対象は性能確認 Status（性能・errp）です。変更後・spliのD:は「JFS2でsplitcopyを用い、isnapshot」を述べ、対象は変更後確認 isnapshot（変更・spli）です。「chuser」は「セキュリティでchuserを用い、enhanced_RBAC」を指し、状態確認 enhanced_RBACではch・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chuser 状態確認 enhanced_RBAC 0453</strong></p><p>検証目的: セキュリティのchuser 状態確認 enhanced_RBAC 0453について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ状態確認093-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0453A
画面・出力には AIX0453A が表示され、chuser 状態確認 enhanced_RBAC 0453 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0453B
画面・出力には AIX0453B が表示され、chuser 状態確認 enhanced_RBAC 0453 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0453C
画面・出力には AIX0453C が表示され、chuser 状態確認 enhanced_RBAC 0453 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0453A が画面・出力に表示されること
② ステップ2 の AIX0453B が画面・出力に表示されること
③ ステップ3 の AIX0453C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0359"><h3>chuser 監査記録 enhanced_RBAC 0423</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>新緑評価ではAIX 7.3のセキュリティで chuser を確認します。新緑評価のセキュリティでは enhanced_RBAC とロール一覧を作業票へ保管します。新緑評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。新緑評価の注意点として ユーザー属性変更の根拠不足 を避けるため lsrole ALL も併記します。権限管理の作業票として、新緑評価を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chuser 監査記録 enhanced_RBAC 0423の設定や表示を読む前に役割を確認します。rmdev -Rl ent1 運用引継ぎ microcode level 0424ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはセキュリティでchuserを用い・enhanced_RBAC とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 状態を読み取るための働きはデバイス管理でrmdev -Rl ent1を用い・microcode levelである。</li><li>C. 状態を読み取るための働きはSRCとログでerrptを用い・syslog.conf とinetdデバッグ出力を確認する。</li><li>D. 状態を読み取るための働きはJFS2でsnapを用い・lff とログデバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでchuserを用い、enhanced_RBAC とロール一覧を確認する」に対応する項目は監査記録 enhanced_RBAC（監査・chus）です。監査に関するセキュリティの仕様は「セキュリティでchuserを用い、enhanced_RBAC」で、確認対象はch・監査です。運用引・rmdeのB:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象はmicrocode level（運用・rmde）です。変更後・errpのC:は「SRCとログでerrptを用い、syslog.conf」を述べ、対象は変更後確認 syslog.conf（変更・errp）です。容量・snapのD:は「JFS2でsnapを用い、lff とログデバイス設定を確認する」を述べ、対象は容量確認 lff（容量・snap）です。「chuser」は「セキュリティでchuserを用い、enhanced_RBAC」を指し、監査記録 enhanced_RBACではch・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chuser 監査記録 enhanced_RBAC 0423</strong></p><p>検証目的: セキュリティのchuser 監査記録 enhanced_RBAC 0423について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ監査記録063-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0423A
画面・出力には AIX0423A が表示され、chuser 監査記録 enhanced_RBAC 0423 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0423B
画面・出力には AIX0423B が表示され、chuser 監査記録 enhanced_RBAC 0423 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0423C
画面・出力には AIX0423C が表示され、chuser 監査記録 enhanced_RBAC 0423 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0423A が画面・出力に表示されること
② ステップ2 の AIX0423B が画面・出力に表示されること
③ ステップ3 の AIX0423C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0360"><h3>lsattr -E -l sys0 -a enhanced_RBAC 容量確認 roles 0377</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>初霜記録ではAIX 7.3のセキュリティで lsattr -E -l sys0 -a enhanced_RBAC を確認します。初霜記録のセキュリティでは roles と監査設定を復旧票へ残します。初霜記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。初霜記録の注意点として ロール割当と権限文字列の不一致 を避けるため lsuser user1 も併記します。権限管理の作業票として、初霜記録を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lsattr -E -l sys0 -a enhanced_RBAC 容量確認 roles 0377」を「lsattr -El hdisk0 性能確認 Available 0378」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はデバイス管理でlsattr -El hdisk0を用い・Available とデバイス一覧を確認する。</li><li>B. 仕様上の役割はセキュリティでlsattr -E -l sys0 -aを用い・roles と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割はSRCとログでstartsrc -s inetd -aを用い・syslog.confである。</li><li>D. 仕様上の役割はJFS2でcrfsを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「セキュリティでlsattr -E -l sys0 -aを用い、roles」に対応する項目は容量確認 roles（容量・lsat）です。容量に関するセキュリティの仕様は「セキュリティでlsattr -E -l sys0 -aを用い」で、確認対象はls・容量です。性能・lsatのA:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は性能確認 Available（性能・lsat）です。障害切・starのC:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け syslog.conf（障害・star）です。起動・ファ・crfsのD:は「JFS2でcrfsを用い、ファイルシステム使用率」を述べ、対象は起動確認 ファイルシステム使用率（起動・crfs）です。「lsattr -E -l sys0 -a」は「セキュリティでlsattr -E -l sys0 -aを用い」を指し、容量確認 rolesではls・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr -E -l sys0 -a enhanced_RBAC 容量確認 roles 0377</strong></p><p>検証目的: セキュリティのlsattr -E -l sys0 -a enhanced_RBAC 容量確認 roles 0377について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ容量確認017-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -E -l sys0 -a enhanced_RBAC
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0377A
画面・出力には AIX0377A が表示され、lsattr -E -l sys0 -a enhanced_RBAC 容量確認 roles 0377 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0377B
画面・出力には AIX0377B が表示され、lsattr -E -l sys0 -a enhanced_RBAC 容量確認 roles 0377 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0377C
画面・出力には AIX0377C が表示され、lsattr -E -l sys0 -a enhanced_RBAC 容量確認 roles 0377 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0377A が画面・出力に表示されること
② ステップ2 の AIX0377B が画面・出力に表示されること
③ ステップ3 の AIX0377C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0361"><h3>lsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0060</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>薄明照合ではAIX 7.3のセキュリティで lsattr -E -l sys0 -a enhanced_RBAC を確認します。薄明照合のセキュリティでは enhanced_RBAC とユーザー属性を同じ証跡に残します。薄明照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。薄明照合の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、薄明照合を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr -E -l sys0 -a enhanced_RBAC 状態確認の技術的な意味を資料で確認するとき、lsattr -El hdisk0 構成照合 location code 0061との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はデバイス管理でlsattr -El hdisk0を用い・location code と診断対象表示を確認する。</li><li>B. 構成を確認する際の意味はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はSRCとログでtail -f /tmp/myfileを用い・Subsystemである。</li><li>D. 構成を確認する際の意味はデバイス管理でbootinfo -B hdisk0を用い・Available と診断対象表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでlsattr -E -l sys0 -aを用い」に対応する項目は状態確認 enhanced_RBAC（状態・lsat）です。セキュリティの仕様は「セキュリティでlsattr -E -l sys0 -aを用い」で、確認対象はls・状態です。構成・lsatのA:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象はlocation code（構成・lsat）です。性能・tailのC:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は性能確認 Subsystem（性能・tail）です。監査・bootのD:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は監査記録 Available（監査・boot）です。「lsattr -E -l sys0 -a」は「セキュリティでlsattr -E -l sys0 -aを用い」を指し、状態確認 enhanced_RBACではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0060</strong></p><p>検証目的: セキュリティのlsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0060について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ状態確認060-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -E -l sys0 -a enhanced_RBAC
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0060A
画面・出力には AIX0060A が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0060 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0060B
画面・出力には AIX0060B が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0060 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0060C
画面・出力には AIX0060C が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0060 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0060A が画面・出力に表示されること
② ステップ2 の AIX0060B が画面・出力に表示されること
③ ステップ3 の AIX0060C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0362"><h3>lsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0120</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>青葉採取ではAIX 7.3のセキュリティで lsattr -E -l sys0 -a enhanced_RBAC を確認します。青葉採取のセキュリティでは enhanced_RBAC とユーザー属性を同じ証跡に残します。青葉採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。青葉採取の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、青葉採取を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr -E -l sys0 -a enhanced_RBAC 状態確認を同一分類のchdev -l hdisk0 変更前確認 attribute 0121と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はデバイス管理でchdev -l hdisk0を用い・attribute と診断対象表示を確認する。</li><li>B. 構成を確認する際の意味はSRCとログでtail -f /tmp/myfileを用い・Subsystemである。</li><li>C. 構成を確認する際の意味はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はデバイス管理でlsmpio -l hdisk0を用い・location code と診断対象表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「セキュリティでlsattr -E -l sys0 -aを用い」に対応する項目は状態確認 enhanced_RBAC（状態・lsat）です。状態に関するセキュリティの仕様は「セキュリティでlsattr -E -l sys0 -aを用い」で、確認対象はls・状態です。変更前・chdeのA:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象は変更前確認 attribute（変更・chde）です。性能・tailのB:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は性能確認 Subsystem（性能・tail）です。運用引・lsmpのD:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はlocation code（運用・lsmp）です。「lsattr -E -l sys0 -a」は「セキュリティでlsattr -E -l sys0 -aを用い」を指し、状態確認 enhanced_RBACではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0120</strong></p><p>検証目的: セキュリティのlsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0120について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ状態確認120-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -E -l sys0 -a enhanced_RBAC
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0120A
画面・出力には AIX0120A が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0120 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0120B
画面・出力には AIX0120B が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0120 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0120C
画面・出力には AIX0120C が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 enhanced_RBAC 0120 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0120A が画面・出力に表示されること
② ステップ2 の AIX0120B が画面・出力に表示されること
③ ステップ3 の AIX0120C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0363"><h3>lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0536</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>若竹照合ではAIX 7.3のセキュリティで lsattr -E -l sys0 -a enhanced_RBAC を確認します。若竹照合のセキュリティでは roles とユーザー属性を引継ぎ票へ保管します。若竹照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若竹照合の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、若竹照合を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0536を同一分類のlsattr -El hdisk0 構成照合 PVID 0537と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はデバイス管理でlsattr -El hdisk0を用い・PVID と診断対象表示を確認する。lsattr -El hdisk0 構成照合 PVID 0537固有の属性も確認対象に含める。</li><li>B. コマンドまたは機能の用途はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>C. コマンドまたは機能の用途はJFS2でcrfsを用い・isnapshot とマウントオプションを確認する。</li><li>D. コマンドまたは機能の用途はセキュリティでlsattr -E -l sys0 -aを用い・roles とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでlsattr -E -l sys0 -aを用い、roles」に対応する項目は状態確認 roles（状態・lsat）です。状態に関するセキュリティの仕様は「セキュリティでlsattr -E -l sys0 -aを用い」で、確認対象はls・状態です。構成・lsatのA:は「デバイス管理でlsattr -El hdisk0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lsat）です。詳細・詳細・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は詳細確認 詳細表示（詳細・lsvg）です。変更前・crfsのC:は「JFS2でcrfsを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・crfs）です。「lsattr -E -l sys0 -a」は「セキュリティでlsattr -E -l sys0 -aを用い」を指し、状態確認 rolesではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0536</strong></p><p>検証目的: セキュリティのlsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0536について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ状態確認056-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -E -l sys0 -a enhanced_RBAC
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0536A
画面・出力には AIX0536A が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0536 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0536B
画面・出力には AIX0536B が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0536 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0536C
画面・出力には AIX0536C が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0536 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0536A が画面・出力に表示されること
② ステップ2 の AIX0536B が画面・出力に表示されること
③ ステップ3 の AIX0536C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0364"><h3>lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0596</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>若潮点検ではAIX 7.3のセキュリティで lsattr -E -l sys0 -a enhanced_RBAC を確認します。若潮点検のセキュリティでは roles とユーザー属性を引継ぎ票へ保管します。若潮点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若潮点検の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、若潮点検を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0596の技術的な意味を資料で確認するとき、lsattr -El hdisk0 構成照合 PVID 0597との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はデバイス管理でlsattr -El hdisk0を用い・PVID と診断対象表示を確認する。</li><li>B. コマンドまたは機能の用途はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>C. コマンドまたは機能の用途はLVMでlsvgを用い・PP SIZE とミラーコピー状態を確認する。lsvg 変更後確認 PP SIZE 0289固有の属性も確認対象に含める。</li><li>D. コマンドまたは機能の用途はセキュリティでlsattr -E -l sys0 -aを用い・roles とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「セキュリティでlsattr -E -l sys0 -aを用い、roles」に対応する項目は状態確認 roles（状態・lsat）です。状態に関するセキュリティの仕様は「セキュリティでlsattr -E -l sys0 -aを用い」で、確認対象はls・状態です。構成・lsatのA:は「デバイス管理でlsattr -El hdisk0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lsat）です。属性・設定・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は属性照合 設定値（属性・lsvg）です。変更後・lsvgのC:は「LVMでlsvgを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（変更・lsvg）です。「lsattr -E -l sys0 -a」は「セキュリティでlsattr -E -l sys0 -aを用い」を指し、状態確認 rolesではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0596</strong></p><p>検証目的: セキュリティのlsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0596について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ状態確認116-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -E -l sys0 -a enhanced_RBAC
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0596A
画面・出力には AIX0596A が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0596 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0596B
画面・出力には AIX0596B が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0596 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0596C
画面・出力には AIX0596C が表示され、lsattr -E -l sys0 -a enhanced_RBAC 状態確認 roles 0596 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0596A が画面・出力に表示されること
② ステップ2 の AIX0596B が画面・出力に表示されること
③ ステップ3 の AIX0596C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0365"><h3>lsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0030</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>早苗確認ではAIX 7.3のセキュリティで lsattr -E -l sys0 -a enhanced_RBAC を確認します。早苗確認のセキュリティでは enhanced_RBAC とRBAC属性を変更票へ記録します。早苗確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。早苗確認の注意点として 監査データ未取得でのroleqry実行 を避けるため lsrole ALL も併記します。権限管理の作業票として、早苗確認を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr -E -l sys0 -a enhanced_RBAC 監査記録に関する障害切り分けの前提を確認しています。lsattr -El hdisk0 運用引継ぎ path status 0031の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはデバイス管理でlsattr -El hdisk0を用い・path status とODM属性を確認する。</li><li>B. 機能の説明としてはSRCとログでstartsrc -s inetd -aを用い・Status とsyslog設定変換を確認する。</li><li>C. 機能の説明としてはセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはデバイス管理でbootinfo -B hdisk0を用い・PVID とODM属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでlsattr -E -l sys0 -aを用い」に対応する項目は監査記録 enhanced_RBAC（監査・lsat）です。セキュリティの仕様は「セキュリティでlsattr -E -l sys0 -aを用い」で、確認対象はls・監査です。運用引・lsatのA:は「デバイス管理でlsattr -El hdisk0を用い、path」を述べ、対象はpath status（運用・lsat）です。変更前・starのB:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は変更前確認 Status（変更・star）です。状態・bootのD:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・boot）です。「lsattr -E -l sys0 -a」は「セキュリティでlsattr -E -l sys0 -aを用い」を指し、監査記録 enhanced_RBACではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0030</strong></p><p>検証目的: セキュリティのlsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0030について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ監査記録030-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -E -l sys0 -a enhanced_RBAC
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0030A
画面・出力には AIX0030A が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0030 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0030B
画面・出力には AIX0030B が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0030 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0030C
画面・出力には AIX0030C が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0030 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0030A が画面・出力に表示されること
② ステップ2 の AIX0030B が画面・出力に表示されること
③ ステップ3 の AIX0030C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0366"><h3>lsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0090</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>桜雲点検ではAIX 7.3のセキュリティで lsattr -E -l sys0 -a enhanced_RBAC を確認します。桜雲点検のセキュリティでは enhanced_RBAC とRBAC属性を変更票へ記録します。桜雲点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。桜雲点検の注意点として 監査データ未取得でのroleqry実行 を避けるため lsrole ALL も併記します。権限管理の作業票として、桜雲点検を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr -E -l sys0 -a enhanced_RBAC 監査記録の役割を調べています。lsattr -El hdisk0 運用引継ぎ path status 0091の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはデバイス管理でlsattr -El hdisk0を用い・path status とODM属性を確認する。</li><li>B. 機能の説明としてはセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としてはSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。</li><li>D. 機能の説明としてはデバイス管理でbootinfo -B hdisk0を用い・PVID とODM属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでlsattr -E -l sys0 -aを用い」に対応する項目は監査記録 enhanced_RBAC（監査・lsat）です。監査に関するセキュリティの仕様は「セキュリティでlsattr -E -l sys0 -aを用い」で、確認対象はls・監査です。運用引・lsatのA:は「デバイス管理でlsattr -El hdisk0を用い、path」を述べ、対象はpath status（運用・lsat）です。変更後・tailのC:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は変更後確認 IDENTIFIER（変更・tail）です。状態・bootのD:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・boot）です。「lsattr -E -l sys0 -a」は「セキュリティでlsattr -E -l sys0 -aを用い」を指し、監査記録 enhanced_RBACではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0090</strong></p><p>検証目的: セキュリティのlsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0090について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ監査記録090-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -E -l sys0 -a enhanced_RBAC
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0090A
画面・出力には AIX0090A が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0090 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0090B
画面・出力には AIX0090B が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0090 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0090C
画面・出力には AIX0090C が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 enhanced_RBAC 0090 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0090A が画面・出力に表示されること
② ステップ2 の AIX0090B が画面・出力に表示されること
③ ステップ3 の AIX0090C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0367"><h3>lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0506</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>陽炎確認ではAIX 7.3のセキュリティで lsattr -E -l sys0 -a enhanced_RBAC を確認します。陽炎確認のセキュリティでは roles とRBAC属性を確認票へ整理します。陽炎確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。陽炎確認の注意点として 監査データ未取得でのroleqry実行 を避けるため lsuser user1 も併記します。権限管理の作業票として、陽炎確認を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0506の役割を調べています。lsattr -El hdisk0 運用引継ぎ Available 0507の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はデバイス管理でlsattr -El hdisk0を用い・Available とODM属性を確認する。</li><li>B. 障害切り分けに用いる役割はSRCとログでstartsrc -s inetd -aを用い・TIMESTAMPである。</li><li>C. 障害切り分けに用いる役割はセキュリティでlsattr -E -l sys0 -aを用い・roles とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割はJFS2でcrfsを用い・ファイルシステム使用率 と内部スナップショットを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでlsattr -E -l sys0 -aを用い、roles」に対応する項目は監査記録 roles（監査・lsat）です。監査に関するセキュリティの仕様は「セキュリティでlsattr -E -l sys0 -aを用い」で、確認対象はls・監査です。運用引・lsatのA:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は運用引継ぎ Available（運用・lsat）です。変更前・starのB:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は変更前確認 TIMESTAMP（変更・star）です。容量・ファ・crfsのD:は「JFS2でcrfsを用い、ファイルシステム使用率」を述べ、対象は容量確認 ファイルシステム使用率（容量・crfs）です。「lsattr -E -l sys0 -a」は「セキュリティでlsattr -E -l sys0 -aを用い」を指し、監査記録 rolesではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0506</strong></p><p>検証目的: セキュリティのlsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0506について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ監査記録026-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -E -l sys0 -a enhanced_RBAC
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0506A
画面・出力には AIX0506A が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0506 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0506B
画面・出力には AIX0506B が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0506 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0506C
画面・出力には AIX0506C が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0506 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0506A が画面・出力に表示されること
② ステップ2 の AIX0506B が画面・出力に表示されること
③ ステップ3 の AIX0506C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0368"><h3>lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0566</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>朝凪点検ではAIX 7.3のセキュリティで lsattr -E -l sys0 -a enhanced_RBAC を確認します。朝凪点検のセキュリティでは roles とRBAC属性を確認票へ整理します。朝凪点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。朝凪点検の注意点として 監査データ未取得でのroleqry実行 を避けるため lsuser user1 も併記します。権限管理の作業票として、朝凪点検を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0566に関する障害切り分けの前提を確認しています。lsattr -El hdisk0 運用引継ぎ Available 0567の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はデバイス管理でlsattr -El hdisk0を用い・Available とODM属性を確認する。</li><li>B. 障害切り分けに用いる役割はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>C. 障害切り分けに用いる役割はセキュリティでlsattr -E -l sys0 -aを用い・roles とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割はJFS2でchfsを用い・log=INLINE と内部スナップショットを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでlsattr -E -l sys0 -aを用い、roles」に対応する項目は監査記録 roles（監査・lsat）です。監査に関するセキュリティの仕様は「セキュリティでlsattr -E -l sys0 -aを用い」で、確認対象はls・監査です。運用引・lsatのA:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は運用引継ぎ Available（運用・lsat）です。状態・製品・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は状態判定 製品レベル（状態・lsvg）です。性能・chfsのD:は「JFS2でchfsを用い、log=INLINE」を述べ、対象は性能確認 log=INLINE（性能・chfs）です。「lsattr -E -l sys0 -a」は「セキュリティでlsattr -E -l sys0 -aを用い」を指し、監査記録 rolesではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0566</strong></p><p>検証目的: セキュリティのlsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0566について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ監査記録086-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -E -l sys0 -a enhanced_RBAC
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0566A
画面・出力には AIX0566A が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0566 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0566B
画面・出力には AIX0566B が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0566 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0566C
画面・出力には AIX0566C が表示され、lsattr -E -l sys0 -a enhanced_RBAC 監査記録 roles 0566 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0566A が画面・出力に表示されること
② ステップ2 の AIX0566B が画面・出力に表示されること
③ ステップ3 の AIX0566C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0369"><h3>lsattr -E -l sys0 -a enhanced_RBAC 障害切り分け audit class 0695</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>岩清水保守ではAIX 7.3のセキュリティで lsattr -E -l sys0 -a enhanced_RBAC を確認します。岩清水保守のセキュリティでは audit class とロール一覧を照合票へ整理します。岩清水保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。岩清水保守の注意点として ユーザー属性変更の根拠不足 を避けるため lsuser user1 も併記します。権限管理の作業票として、岩清水保守を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr -E -l sys0 -a enhanced_RBAC 障害切り分け auditの設定や表示を読む前に役割を確認します。lsattr -El hdisk0 バックアウト確認 microcodeではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はデバイス管理でlsattr -El hdisk0を用い・microcode levelである。lsattr -El hdisk0 バックアウト確認固有の属性も確認対象に含める。</li><li>B. 一次資料が示す主目的はネットワークでifconfig en0を用い・EtherChannel とMTU属性を確認する。</li><li>C. 一次資料が示す主目的はセキュリティでlsattr -E -l sys0 -aを用い・audit class とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はJFS2でchfsを用い・ファイルシステム使用率 とログデバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでlsattr -E -l sys0 -aを用い、audit」に対応する項目はaudit class（障害・lsat）です。障害切に関するセキュリティの仕様は「セキュリティでlsattr -E -l sys0 -aを用い」で、確認対象はls・障害切です。バック・lsatのA:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象はmicrocode level（バッ・lsat）です。性能・ifcoのB:は「ネットワークでifconfig en0を用い」を述べ、対象は性能確認 EtherChannel（性能・ifco）です。運用引・chfsのD:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象は運用引継ぎ ファイルシステム使用率（運用・chfs）です。「lsattr -E -l sys0 -a」は「セキュリティでlsattr -E -l sys0 -aを用い」を指し、audit classではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr -E -l sys0 -a enhanced_RBAC 障害切り分け audit class 0695</strong></p><p>検証目的: セキュリティのlsattr -E -l sys0 -a enhanced_RBAC 障害切り分け audit class 0695について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ障害切り分け095-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -E -l sys0 -a enhanced_RBAC
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0695A
画面・出力には AIX0695A が表示され、lsattr -E -l sys0 -a enhanced_RBAC 障害切り分け audit class 0695 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0695B
画面・出力には AIX0695B が表示され、lsattr -E -l sys0 -a enhanced_RBAC 障害切り分け audit class 0695 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0695C
画面・出力には AIX0695C が表示され、lsattr -E -l sys0 -a enhanced_RBAC 障害切り分け audit class 0695 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0695A が画面・出力に表示されること
② ステップ2 の AIX0695B が画面・出力に表示されること
③ ステップ3 の AIX0695C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0370"><h3>lsattr -E -l sys0 -a enhanced_RBAC 障害切り分け authorizations 0219</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>山吹保守ではAIX 7.3のセキュリティで lsattr -E -l sys0 -a enhanced_RBAC を確認します。山吹保守のセキュリティでは authorizations とロール一覧を作業票へ保管します。山吹保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。山吹保守の注意点として ユーザー属性変更の根拠不足 を避けるため lsrole ALL も併記します。権限管理の作業票として、山吹保守を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsattr -E -l sys0 -a enhanced_RBAC 障害切り分けについて構成や状態を確認します。lsattr -El hdisk0 バックアウト確認 PVID 0220ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはデバイス管理でlsattr -El hdisk0を用い・PVID と構成マネージャー結果を確認する。</li><li>B. 状態を読み取るための働きはセキュリティでlsattr -E -l sys0 -aを用い・authorizationsである。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。</li><li>D. 状態を読み取るための働きはデバイス管理でbootinfo -B hdisk0を用い・attributeである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでlsattr -E -l sys0 -aを用い」に対応する項目は障害切り分け authorizati（障害・lsat）です。障害切に関するセキュリティの仕様は「セキュリティでlsattr -E -l sys0 -aを用い」で、確認対象はls・障害切です。バック・lsatのA:は「デバイス管理でlsattr -El hdisk0を用い、PVID」を述べ、対象はバックアウト確認 PVID（バッ・lsat）です。構成・tailのC:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は構成照合 IDENTIFIER（構成・tail）です。起動・bootのD:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は起動確認 attribute（起動・boot）です。「lsattr -E -l sys0 -a」は「セキュリティでlsattr -E -l sys0 -aを用い」を指し、障害切り分け authorizatiではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsattr -E -l sys0 -a enhanced_RBAC 障害切り分け authorizations 0219</strong></p><p>検証目的: セキュリティのlsattr -E -l sys0 -a enhanced_RBAC 障害切り分け authorizations 0219について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ障害切り分け099-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -E -l sys0 -a enhanced_RBAC
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0219A
画面・出力には AIX0219A が表示され、lsattr -E -l sys0 -a enhanced_RBAC 障害切り分け authorizations 0219 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0219B
画面・出力には AIX0219B が表示され、lsattr -E -l sys0 -a enhanced_RBAC 障害切り分け authorizations 0219 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0219C
画面・出力には AIX0219C が表示され、lsattr -E -l sys0 -a enhanced_RBAC 障害切り分け authorizations 0219 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0219A が画面・出力に表示されること
② ステップ2 の AIX0219B が画面・出力に表示されること
③ ステップ3 の AIX0219C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0371"><h3>lsrole バックアウト確認 roles 0279</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>秋桜監査ではAIX 7.3のセキュリティで lsrole を確認します。秋桜監査のセキュリティでは roles とロール一覧を作業票へ保管します。秋桜監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。秋桜監査の注意点として ユーザー属性変更の根拠不足 を避けるため lsrole ALL も併記します。権限管理の作業票として、秋桜監査を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsrole バックアウト確認 roles 0279の設定や表示を読む前に役割を確認します。chdev -l hdisk0 監査記録 path status 0280ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはセキュリティでlsroleを用い・roles とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 状態を読み取るための働きはデバイス管理でchdev -l hdisk0を用い・path status と構成マネージャー結果を確認する。</li><li>C. 状態を読み取るための働きはSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。</li><li>D. 状態を読み取るための働きはボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでlsroleを用い、roles とロール一覧を確認する」に対応する項目はバックアウト確認 roles（バッ・lsro）です。バックに関するセキュリティの仕様は「セキュリティでlsroleを用い、roles とロール一覧を確認する」で、確認対象はls・バックです。監査・chdeのB:は「デバイス管理でchdev -l hdisk0を用い、path」を述べ、対象はpath status（監査・chde）です。構成・tailのC:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は構成照合 IDENTIFIER（構成・tail）です。一覧・詳細・lsvgのD:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は一覧確認 詳細表示（一覧・lsvg）です。「lsrole」は「セキュリティでlsroleを用い、roles とロール一覧を確認する」を指し、バックアウト確認 rolesではls・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsrole バックアウト確認 roles 0279</strong></p><p>検証目的: セキュリティのlsrole バックアウト確認 roles 0279について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティバックアウト確認039-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0279A
画面・出力には AIX0279A が表示され、lsrole バックアウト確認 roles 0279 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0279B
画面・出力には AIX0279B が表示され、lsrole バックアウト確認 roles 0279 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0279C
画面・出力には AIX0279C が表示され、lsrole バックアウト確認 roles 0279 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0279A が画面・出力に表示されること
② ステップ2 の AIX0279B が画面・出力に表示されること
③ ステップ3 の AIX0279C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0372"><h3>lsrole バックアウト確認 user attributes 0755</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>青磁監査ではAIX 7.3のセキュリティで lsrole を確認します。青磁監査のセキュリティでは user attributes とロール一覧を照合票へ整理します。青磁監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。青磁監査の注意点として ユーザー属性変更の根拠不足 を避けるため lsuser user1 も併記します。権限管理の作業票として、青磁監査を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsrole バックアウト確認 user attributes 0755について構成や状態を確認します。chdev -l hdisk0 監査記録 Available 0756ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はデバイス管理でchdev -l hdisk0を用い・Available と構成マネージャー結果を確認する。</li><li>B. 一次資料が示す主目的はセキュリティでlsroleを用い・user attributes とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 一次資料が示す主目的はネットワークでchdev -l en0 -aを用い・Link Status とMTU属性を確認する。</li><li>D. 一次資料が示す主目的はJFS2でchfsを用い・ファイルシステム使用率 とログデバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでlsroleを用い、user attributes」に対応する項目はuser attributes（バッ・lsro）です。バックに関するセキュリティの仕様は「セキュリティでlsroleを用い、user attributes」で、確認対象はls・バックです。監査・chdeのA:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象は監査記録 Available（監査・chde）です。起動・chdeのC:は「ネットワークでchdev -l en0 -aを用い、Link」を述べ、対象はLink Status（起動・chde）です。運用引・chfsのD:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象は運用引継ぎ ファイルシステム使用率（運用・chfs）です。「lsrole」は「セキュリティでlsroleを用い、user attributes」を指し、user attributesではls・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsrole バックアウト確認 user attributes 0755</strong></p><p>検証目的: セキュリティのlsrole バックアウト確認 user attributes 0755について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティバックアウト確認035-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0755A
画面・出力には AIX0755A が表示され、lsrole バックアウト確認 user attributes 0755 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0755B
画面・出力には AIX0755B が表示され、lsrole バックアウト確認 user attributes 0755 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0755C
画面・出力には AIX0755C が表示され、lsrole バックアウト確認 user attributes 0755 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0755A が画面・出力に表示されること
② ステップ2 の AIX0755B が画面・出力に表示されること
③ ステップ3 の AIX0755C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0373"><h3>lsrole 変更後確認 roles 0408</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>翠風評価ではAIX 7.3のセキュリティで lsrole を確認します。翠風評価のセキュリティでは roles とユーザー属性を同じ証跡に残します。翠風評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。翠風評価の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、翠風評価を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsrole 変更後確認 roles 0408を同一分類のlsvg -l 障害切り分け STALE PARTITIONS 0409と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はLVMでlsvg -lを用い・STALE PARTITIONS とミラーコピー状態を確認する。</li><li>B. 構成を確認する際の意味はセキュリティでlsroleを用い・roles とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はSRCとログでtail -f /tmp/myfileを用い・Status とSRCサブシステム表示を確認する。</li><li>D. 構成を確認する際の意味はJFS2でchfsを用い・mountguard とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでlsroleを用い、roles とユーザー属性を確認する」に対応する項目は変更後確認 roles（変更・lsro）です。変更後に関するセキュリティの仕様は「セキュリティでlsroleを用い、roles」で、確認対象はls・変更後です。障害切・lsvgのA:は「LVMでlsvg -lを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（障害・lsvg）です。属性・tailのC:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は属性確認 Status（属性・tail）です。バック・chfsのD:は「JFS2でchfsを用い、mountguard」を述べ、対象はバックアウト確認 mountguar（バッ・chfs）です。「lsrole」は「セキュリティでlsroleを用い、roles」を指し、変更後確認 rolesではls・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsrole 変更後確認 roles 0408</strong></p><p>検証目的: セキュリティのlsrole 変更後確認 roles 0408について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更後確認048-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0408A
画面・出力には AIX0408A が表示され、lsrole 変更後確認 roles 0408 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0408B
画面・出力には AIX0408B が表示され、lsrole 変更後確認 roles 0408 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0408C
画面・出力には AIX0408C が表示され、lsrole 変更後確認 roles 0408 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0408A が画面・出力に表示されること
② ステップ2 の AIX0408B が画面・出力に表示されること
③ ステップ3 の AIX0408C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0374"><h3>lsrole 変更後確認 roles 0468</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>雪解整理ではAIX 7.3のセキュリティで lsrole を確認します。雪解整理のセキュリティでは roles とユーザー属性を同じ証跡に残します。雪解整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。雪解整理の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、雪解整理を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsrole 変更後確認 roles 0468の技術的な意味を資料で確認するとき、chdev -l hdisk0 障害切り分け path status 0469との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はデバイス管理でchdev -l hdisk0を用い・path status と診断対象表示を確認する。</li><li>B. 構成を確認する際の意味はSRCとログでlssrc -s syslogdを用い・IDENTIFIERである。</li><li>C. 構成を確認する際の意味はJFS2でlsfs -qを用い・lff とマウントオプションを確認する。</li><li>D. 構成を確認する際の意味はセキュリティでlsroleを用い・roles とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「セキュリティでlsroleを用い、roles とユーザー属性を確認する」に対応する項目は変更後確認 roles（変更・lsro）です。変更後に関するセキュリティの仕様は「セキュリティでlsroleを用い、roles」で、確認対象はls・変更後です。障害切・chdeのA:は「デバイス管理でchdev -l hdisk0を用い、path」を述べ、対象はpath status（障害・chde）です。状態・lssrのB:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は状態確認 IDENTIFIER（状態・lssr）です。監査・lsfsのC:は「JFS2でlsfs -qを用い、lff とマウントオプションを確認す」を述べ、対象は監査記録 lff（監査・lsfs）です。「lsrole」は「セキュリティでlsroleを用い、roles」を指し、変更後確認 rolesではls・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsrole 変更後確認 roles 0468</strong></p><p>検証目的: セキュリティのlsrole 変更後確認 roles 0468について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更後確認108-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0468A
画面・出力には AIX0468A が表示され、lsrole 変更後確認 roles 0468 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0468B
画面・出力には AIX0468B が表示され、lsrole 変更後確認 roles 0468 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0468C
画面・出力には AIX0468C が表示され、lsrole 変更後確認 roles 0468 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0468A が画面・出力に表示されること
② ステップ2 の AIX0468B が画面・出力に表示されること
③ ステップ3 の AIX0468C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0375"><h3>lsrole 属性確認 roles 0249</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>銀砂監査ではAIX 7.3のセキュリティで lsrole を確認します。銀砂監査のセキュリティでは roles と監査設定を判定票へ残します。銀砂監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。銀砂監査の注意点として ロール割当と権限文字列の不一致 を避けるため lsrole ALL も併記します。権限管理の作業票として、銀砂監査を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lsrole 属性確認 roles 0249」を「chdev -l hdisk0 状態確認 location code 0250」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はデバイス管理でchdev -l hdisk0を用い・location code とデバイス一覧を確認する。</li><li>B. 運用時に利用する技術的役割はSRCとログでtail -f /tmp/myfileを用い・Subsystem とエラーログ一覧を確認する。</li><li>C. 運用時に利用する技術的役割はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>D. 運用時に利用する技術的役割はセキュリティでlsroleを用い・roles と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「セキュリティでlsroleを用い、roles と監査設定を確認する」に対応する項目は属性確認 roles（属性・lsro）です。属性に関するセキュリティの仕様は「セキュリティでlsroleを用い、roles と監査設定を確認する」で、確認対象はls・属性です。状態・chdeのA:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象はlocation code（状態・chde）です。運用引・tailのB:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は運用引継ぎ Subsystem（運用・tail）です。復旧前・lsvgのC:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は復旧前確認 再開位置（復旧・lsvg）です。「lsrole」は「セキュリティでlsroleを用い、roles と監査設定を確認する」を指し、属性確認 rolesではls・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsrole 属性確認 roles 0249</strong></p><p>検証目的: セキュリティのlsrole 属性確認 roles 0249について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認009-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0249A
画面・出力には AIX0249A が表示され、lsrole 属性確認 roles 0249 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0249B
画面・出力には AIX0249B が表示され、lsrole 属性確認 roles 0249 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0249C
画面・出力には AIX0249C が表示され、lsrole 属性確認 roles 0249 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0249A が画面・出力に表示されること
② ステップ2 の AIX0249B が画面・出力に表示されること
③ ステップ3 の AIX0249C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0376"><h3>lsrole 属性確認 roles 0309</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>梅雨晴復旧ではAIX 7.3のセキュリティで lsrole を確認します。梅雨晴復旧のセキュリティでは roles と監査設定を判定票へ残します。梅雨晴復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。梅雨晴復旧の注意点として ロール割当と権限文字列の不一致 を避けるため lsrole ALL も併記します。権限管理の作業票として、梅雨晴復旧を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsrole 属性確認 roles 0309を保守記録に説明する必要があります。chdev -l hdisk0 状態確認 location code 0310と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はデバイス管理でchdev -l hdisk0を用い・location code とデバイス一覧を確認する。</li><li>B. 運用時に利用する技術的役割はセキュリティでlsroleを用い・roles と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はSRCとログでlssrc -s syslogdを用い・PID とエラーログ一覧を確認する。</li><li>D. 運用時に利用する技術的役割はJFS2でlsfs -qを用い・agblksize とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでlsroleを用い、roles と監査設定を確認する」に対応する項目は属性確認 roles（属性・lsro）です。属性に関するセキュリティの仕様は「セキュリティでlsroleを用い、roles と監査設定を確認する」で、確認対象はls・属性です。状態・chdeのA:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象はlocation code（状態・chde）です。容量・lssrのC:は「SRCとログでlssrc -s syslogdを用い、PID」を述べ、対象は容量確認 PID（容量・lssr）です。変更前・lsfsのD:は「JFS2でlsfs -qを用い、agblksize」を述べ、対象は変更前確認 agblksize（変更・lsfs）です。「lsrole」は「セキュリティでlsroleを用い、roles と監査設定を確認する」を指し、属性確認 rolesではls・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsrole 属性確認 roles 0309</strong></p><p>検証目的: セキュリティのlsrole 属性確認 roles 0309について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認069-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0309A
画面・出力には AIX0309A が表示され、lsrole 属性確認 roles 0309 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0309B
画面・出力には AIX0309B が表示され、lsrole 属性確認 roles 0309 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0309C
画面・出力には AIX0309C が表示され、lsrole 属性確認 roles 0309 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0309A が画面・出力に表示されること
② ステップ2 の AIX0309B が画面・出力に表示されること
③ ステップ3 の AIX0309C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0377"><h3>lsrole 属性確認 user attributes 0725</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>深雪監査ではAIX 7.3のセキュリティで lsrole を確認します。深雪監査のセキュリティでは user attributes と監査設定を復旧票へ残します。深雪監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。深雪監査の注意点として ロール割当と権限文字列の不一致 を避けるため lsuser user1 も併記します。権限管理の作業票として、深雪監査を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsrole 属性確認 user attributes 0725を保守記録に説明する必要があります。chdev -l hdisk0 状態確認 PVID 0726と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はデバイス管理でchdev -l hdisk0を用い・PVID とデバイス一覧を確認する。</li><li>B. 仕様上の役割はネットワークでifconfig en0を用い・MTU とEthernet統計を確認する。</li><li>C. 仕様上の役割はJFS2でchfsを用い・isnapshot とファイルシステム属性を確認する。</li><li>D. 仕様上の役割はセキュリティでlsroleを用い・user attributes と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「セキュリティでlsroleを用い、user attributes」に対応する項目はuser attributes（属性・lsro）です。属性に関するセキュリティの仕様は「セキュリティでlsroleを用い、user attributes」で、確認対象はls・属性です。状態・chdeのA:は「デバイス管理でchdev -l hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・chde）です。変更後・ifcoのB:は「ネットワークでifconfig en0を用い、MTU」を述べ、対象は変更後確認 MTU（変更・ifco）です。構成・chfsのC:は「JFS2でchfsを用い、isnapshot」を述べ、対象は構成照合 isnapshot（構成・chfs）です。「lsrole」は「セキュリティでlsroleを用い、user attributes」を指し、user attributesではls・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsrole 属性確認 user attributes 0725</strong></p><p>検証目的: セキュリティのlsrole 属性確認 user attributes 0725について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認005-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0725A
画面・出力には AIX0725A が表示され、lsrole 属性確認 user attributes 0725 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0725B
画面・出力には AIX0725B が表示され、lsrole 属性確認 user attributes 0725 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0725C
画面・出力には AIX0725C が表示され、lsrole 属性確認 user attributes 0725 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0725A が画面・出力に表示されること
② ステップ2 の AIX0725B が画面・出力に表示されること
③ ステップ3 の AIX0725C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0378"><h3>lsrole 属性確認 user attributes 0785</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>花冷復旧ではAIX 7.3のセキュリティで lsrole を確認します。花冷復旧のセキュリティでは user attributes と監査設定を復旧票へ残します。花冷復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。花冷復旧の注意点として ロール割当と権限文字列の不一致 を避けるため lsuser user1 も併記します。権限管理の作業票として、花冷復旧を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lsrole 属性確認 user attributes 0785」を「chdev 復旧前確認 仮想化表示」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はセキュリティでlsroleを用い・user attributes と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割はデバイス属性を変更する管理コマンドである。</li><li>C. 仕様上の役割はネットワークでroute -n getを用い・EtherChannel とEthernet統計を確認する。</li><li>D. 仕様上の役割はJFS2でdf -gを用い・log=INLINE と内部スナップショットを確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 属性・lsroでAの記述「セキュリティでlsroleを用い、user attributes」に対応する項目はuser attributes（属性・lsro）です。属性に関するセキュリティの仕様は「セキュリティでlsroleを用い、user attributes」で、確認対象はls・属性です。復旧前・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は復旧前確認 仮想化表示（復旧・chde）です。容量・routのC:は「ネットワークでroute -n getを用い」を述べ、対象は容量確認 EtherChannel（容量・rout）です。運用引・dfのD:は「JFS2でdf -gを用い、log=INLINE」を述べ、対象は運用引継ぎ log=INLINE（運用・df）です。「lsrole」は「セキュリティでlsroleを用い、user attributes」を指し、user attributesではls・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsrole 属性確認 user attributes 0785</strong></p><p>検証目的: セキュリティのlsrole 属性確認 user attributes 0785について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認065-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0785A
画面・出力には AIX0785A が表示され、lsrole 属性確認 user attributes 0785 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0785B
画面・出力には AIX0785B が表示され、lsrole 属性確認 user attributes 0785 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0785C
画面・出力には AIX0785C が表示され、lsrole 属性確認 user attributes 0785 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0785A が画面・出力に表示されること
② ステップ2 の AIX0785B が画面・出力に表示されること
③ ステップ3 の AIX0785C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0379"><h3>lsrole 性能確認 roles 0438</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>春霞評価ではAIX 7.3のセキュリティで lsrole を確認します。春霞評価のセキュリティでは roles とRBAC属性を変更票へ記録します。春霞評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。春霞評価の注意点として 監査データ未取得でのroleqry実行 を避けるため lsrole ALL も併記します。権限管理の作業票として、春霞評価を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsrole 性能確認 roles 0438に関する障害切り分けの前提を確認しています。chdev -l hdisk0 起動確認 location code 0439の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはデバイス管理でchdev -l hdisk0を用い・location code とODM属性を確認する。</li><li>B. 機能の説明としてはSRCとログでlssrc -s syslogdを用い・Subsystem とsyslog設定変換を確認する。</li><li>C. 機能の説明としてはJFS2でlsfs -qを用い・agblksize と内部スナップショットを確認する。</li><li>D. 機能の説明としてはセキュリティでlsroleを用い・roles とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでlsroleを用い、roles とRBAC属性を確認する」に対応する項目は性能確認 roles（性能・lsro）です。性能に関するセキュリティの仕様は「セキュリティでlsroleを用い、roles」で、確認対象はls・性能です。起動・chdeのA:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象はlocation code（起動・chde）です。監査・lssrのB:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は監査記録 Subsystem（監査・lssr）です。状態・lsfsのC:は「JFS2でlsfs -qを用い、agblksize」を述べ、対象は状態確認 agblksize（状態・lsfs）です。「lsrole」は「セキュリティでlsroleを用い、roles」を指し、性能確認 rolesではls・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsrole 性能確認 roles 0438</strong></p><p>検証目的: セキュリティのlsrole 性能確認 roles 0438について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ性能確認078-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0438A
画面・出力には AIX0438A が表示され、lsrole 性能確認 roles 0438 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0438B
画面・出力には AIX0438B が表示され、lsrole 性能確認 roles 0438 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0438C
画面・出力には AIX0438C が表示され、lsrole 性能確認 roles 0438 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0438A が画面・出力に表示されること
② ステップ2 の AIX0438B が画面・出力に表示されること
③ ステップ3 の AIX0438C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0380"><h3>lssecattr -c 状態確認 audit class 0143</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>新緑採取ではAIX 7.3のセキュリティで lssecattr -c を確認します。新緑採取のセキュリティでは audit class とロール一覧を照合票へ整理します。新緑採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。新緑採取の注意点として ユーザー属性変更の根拠不足 を避けるため lsuser user1 も併記します。権限管理の作業票として、新緑採取を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lssecattr -c 状態確認 audit class 0143の設定や表示を読む前に役割を確認します。lscfg -vl ent0 構成照合 location code 0144ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はデバイス管理でlscfg -vl ent0を用い・location codeである。</li><li>B. 一次資料が示す主目的はSRCとログでrefresh -s syslogdを用い・Subsystemである。</li><li>C. 一次資料が示す主目的はセキュリティでlssecattr -cを用い・audit class とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はデバイス管理でchdev -l hdisk0を用い・Available と構成マネージャー結果を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでlssecattr -cを用い、audit class」に対応する項目はaudit class（状態・lsse）です。状態に関するセキュリティの仕様は「セキュリティでlssecattr -cを用い、audit」で、確認対象はls・状態です。構成・lscfのA:は「デバイス管理でlscfg -vl ent0を用い、location」を述べ、対象はlocation code（構成・lscf）です。容量・refrのB:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は容量確認 Subsystem（容量・refr）です。監査・chdeのD:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象は監査記録 Available（監査・chde）です。「lssecattr -c」は「セキュリティでlssecattr -cを用い、audit」を指し、audit classではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lssecattr -c 状態確認 audit class 0143</strong></p><p>検証目的: セキュリティのlssecattr -c 状態確認 audit class 0143について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ状態確認023-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssecattr -c
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0143A
画面・出力には AIX0143A が表示され、lssecattr -c 状態確認 audit class 0143 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0143B
画面・出力には AIX0143B が表示され、lssecattr -c 状態確認 audit class 0143 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0143C
画面・出力には AIX0143C が表示され、lssecattr -c 状態確認 audit class 0143 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0143A が画面・出力に表示されること
② ステップ2 の AIX0143B が画面・出力に表示されること
③ ステップ3 の AIX0143C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0381"><h3>lssecattr -c 状態確認 enhanced_RBAC 0619</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>山吹採取ではAIX 7.3のセキュリティで lssecattr -c を確認します。山吹採取のセキュリティでは enhanced_RBAC とロール一覧を点検票へ整理します。山吹採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。山吹採取の注意点として ユーザー属性変更の根拠不足 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、山吹採取を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lssecattr -c 状態確認 enhanced_RBAC 0619について構成や状態を確認します。lscfg -vl ent0 構成照合 PVID 0620ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはセキュリティでlssecattr -cを用い・enhanced_RBAC とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはデバイス管理でlscfg -vl ent0を用い・PVID と構成マネージャー結果を確認する。</li><li>C. 対象資源に対する働きはネットワークでnetstat -vを用い・Destination とMTU属性を確認する。</li><li>D. 対象資源に対する働きはJFS2でfsckを用い・isnapshot とログデバイス設定を確認する。fsck 変更前確認 isnapshot 0312固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「セキュリティでlssecattr -cを用い、enhanced_RBAC」に対応する項目は状態確認 enhanced_RBAC（状態・lsse）です。状態に関するセキュリティの仕様は「セキュリティでlssecattr -cを用い」で、確認対象はls・状態です。構成・lscfのB:は「デバイス管理でlscfg -vl ent0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lscf）です。バック・netsのC:は「ネットワークでnetstat -vを用い、Destination」を述べ、対象はバックアウト確認 Destinati（バッ・nets）です。変更前・fsckのD:は「JFS2でfsckを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・fsck）です。「lssecattr -c」は「セキュリティでlssecattr -cを用い」を指し、状態確認 enhanced_RBACではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lssecattr -c 状態確認 enhanced_RBAC 0619</strong></p><p>検証目的: セキュリティのlssecattr -c 状態確認 enhanced_RBAC 0619について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ状態確認019-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssecattr -c
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0619A
画面・出力には AIX0619A が表示され、lssecattr -c 状態確認 enhanced_RBAC 0619 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0619B
画面・出力には AIX0619B が表示され、lssecattr -c 状態確認 enhanced_RBAC 0619 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0619C
画面・出力には AIX0619C が表示され、lssecattr -c 状態確認 enhanced_RBAC 0619 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0619A が画面・出力に表示されること
② ステップ2 の AIX0619B が画面・出力に表示されること
③ ステップ3 の AIX0619C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0382"><h3>lssecattr -c 監査記録 audit class 0173</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>月影判定ではAIX 7.3のセキュリティで lssecattr -c を確認します。月影判定のセキュリティでは audit class と監査設定を復旧票へ残します。月影判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。月影判定の注意点として ロール割当と権限文字列の不一致 を避けるため lsuser user1 も併記します。権限管理の作業票として、月影判定を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lssecattr -c 監査記録 audit class 0173を保守記録に説明する必要があります。lscfg -vl ent0 運用引継ぎ path status 0174と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はデバイス管理でlscfg -vl ent0を用い・path status とデバイス一覧を確認する。</li><li>B. 仕様上の役割はSRCとログでrefresh -s syslogdを用い・IDENTIFIER とエラーログ一覧を確認する。</li><li>C. 仕様上の役割はデバイス管理でchdev -l hdisk0を用い・PVID とデバイス一覧を確認する。</li><li>D. 仕様上の役割はセキュリティでlssecattr -cを用い・audit class と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでlssecattr -cを用い、audit class」に対応する項目はaudit class（監査・lsse）です。監査に関するセキュリティの仕様は「セキュリティでlssecattr -cを用い、audit」で、確認対象はls・監査です。運用引・lscfのA:は「デバイス管理でlscfg -vl ent0を用い、path」を述べ、対象はpath status（運用・lscf）です。変更前・refrのB:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は変更前確認 IDENTIFIER（変更・refr）です。状態・chdeのC:は「デバイス管理でchdev -l hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・chde）です。「lssecattr -c」は「セキュリティでlssecattr -cを用い、audit」を指し、audit classではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lssecattr -c 監査記録 audit class 0173</strong></p><p>検証目的: セキュリティのlssecattr -c 監査記録 audit class 0173について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ監査記録053-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssecattr -c
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0173A
画面・出力には AIX0173A が表示され、lssecattr -c 監査記録 audit class 0173 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0173B
画面・出力には AIX0173B が表示され、lssecattr -c 監査記録 audit class 0173 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0173C
画面・出力には AIX0173C が表示され、lssecattr -c 監査記録 audit class 0173 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0173A が画面・出力に表示されること
② ステップ2 の AIX0173B が画面・出力に表示されること
③ ステップ3 の AIX0173C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0383"><h3>lssecattr -c 監査記録 enhanced_RBAC 0649</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>銀砂判定ではAIX 7.3のセキュリティで lssecattr -c を確認します。銀砂判定のセキュリティでは enhanced_RBAC と監査設定を採取票へ記録します。銀砂判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。銀砂判定の注意点として ロール割当と権限文字列の不一致 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、銀砂判定を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lssecattr -c 監査記録 enhanced_RBAC 0649」を「lscfg -vl ent0 運用引継ぎ Available 0650」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はセキュリティでlssecattr -cを用い・enhanced_RBAC と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はデバイス管理でlscfg -vl ent0を用い・Available とデバイス一覧を確認する。</li><li>C. 保守作業で参照する機能はネットワークでnetstat -vを用い・Link Status とEthernet統計を確認する。</li><li>D. 保守作業で参照する機能はJFS2でfsckを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでlssecattr -cを用い、enhanced_RBAC」に対応する項目は監査記録 enhanced_RBAC（監査・lsse）です。監査に関するセキュリティの仕様は「セキュリティでlssecattr -cを用い」で、確認対象はls・監査です。運用引・lscfのB:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象は運用引継ぎ Available（運用・lscf）です。属性・netsのC:は「ネットワークでnetstat -vを用い、Link Status」を述べ、対象はLink Status（属性・nets）です。容量・ファ・fsckのD:は「JFS2でfsckを用い、ファイルシステム使用率」を述べ、対象は容量確認 ファイルシステム使用率（容量・fsck）です。「lssecattr -c」は「セキュリティでlssecattr -cを用い」を指し、監査記録 enhanced_RBACではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lssecattr -c 監査記録 enhanced_RBAC 0649</strong></p><p>検証目的: セキュリティのlssecattr -c 監査記録 enhanced_RBAC 0649について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ監査記録049-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssecattr -c
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0649A
画面・出力には AIX0649A が表示され、lssecattr -c 監査記録 enhanced_RBAC 0649 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0649B
画面・出力には AIX0649B が表示され、lssecattr -c 監査記録 enhanced_RBAC 0649 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0649C
画面・出力には AIX0649C が表示され、lssecattr -c 監査記録 enhanced_RBAC 0649 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0649A が画面・出力に表示されること
② ステップ2 の AIX0649B が画面・出力に表示されること
③ ステップ3 の AIX0649C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0384"><h3>lssecattr -c 起動確認 audit class 0272</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>夕映監査ではAIX 7.3のセキュリティで lssecattr -c を確認します。夕映監査のセキュリティでは audit class とユーザー属性を引継ぎ票へ保管します。夕映監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。夕映監査の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、夕映監査を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lssecattr -c 起動確認 audit class 0272を同一分類のchlv 属性確認 VG STATE 0273と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はLVMでchlvを用い・VG STATE とミラーコピー状態を確認する。chlv 属性確認 VG STATE 0273固有の属性も確認対象に含める。</li><li>B. コマンドまたは機能の用途はSRCとログでrefresh -s syslogdを用い・syslog.confである。</li><li>C. コマンドまたは機能の用途はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>D. コマンドまたは機能の用途はセキュリティでlssecattr -cを用い・audit class とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでlssecattr -cを用い、audit class」に対応する項目はaudit class（起動・lsse）です。起動に関するセキュリティの仕様は「セキュリティでlssecattr -cを用い、audit」で、確認対象はls・起動です。属性・chlvのA:は「LVMでchlvを用い、VG STATE」を述べ、対象はVG STATE（属性・chlv）です。監査・refrのB:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は監査記録 syslog.conf（監査・refr）です。一覧・監査・errpのC:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は一覧確認 監査証跡（一覧・errp）です。「lssecattr -c」は「セキュリティでlssecattr -cを用い、audit」を指し、audit classではls・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lssecattr -c 起動確認 audit class 0272</strong></p><p>検証目的: セキュリティのlssecattr -c 起動確認 audit class 0272について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ起動確認032-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssecattr -c
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0272A
画面・出力には AIX0272A が表示され、lssecattr -c 起動確認 audit class 0272 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0272B
画面・出力には AIX0272B が表示され、lssecattr -c 起動確認 audit class 0272 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0272C
画面・出力には AIX0272C が表示され、lssecattr -c 起動確認 audit class 0272 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0272A が画面・出力に表示されること
② ステップ2 の AIX0272B が画面・出力に表示されること
③ ステップ3 の AIX0272C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0385"><h3>lssecattr -c 起動確認 audit class 0332</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>水音変更ではAIX 7.3のセキュリティで lssecattr -c を確認します。水音変更のセキュリティでは audit class とユーザー属性を引継ぎ票へ保管します。水音変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。水音変更の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、水音変更を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lssecattr -c 起動確認 audit class 0332の技術的な意味を資料で確認するとき、lscfg -vl ent0 属性確認 location code 0333との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はセキュリティでlssecattr -cを用い・audit class とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はデバイス管理でlscfg -vl ent0を用い・location code と診断対象表示を確認する。</li><li>C. コマンドまたは機能の用途はSRCとログでsyslog_ssw -cを用い・Subsystem とSRCサブシステム表示を確認する。</li><li>D. コマンドまたは機能の用途はJFS2でdf -gを用い・agblksize とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでlssecattr -cを用い、audit class」に対応する項目はaudit class（起動・lsse）です。起動に関するセキュリティの仕様は「セキュリティでlssecattr -cを用い、audit」で、確認対象はls・起動です。属性・lscfのB:は「デバイス管理でlscfg -vl ent0を用い、location」を述べ、対象はlocation code（属性・lscf）です。運用引・syslのC:は「SRCとログでsyslog_ssw -cを用い、Subsystem」を述べ、対象は運用引継ぎ Subsystem（運用・sysl）です。構成・dfのD:は「JFS2でdf -gを用い、agblksize」を述べ、対象は構成照合 agblksize（構成・df）です。「lssecattr -c」は「セキュリティでlssecattr -cを用い、audit」を指し、audit classではls・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lssecattr -c 起動確認 audit class 0332</strong></p><p>検証目的: セキュリティのlssecattr -c 起動確認 audit class 0332について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ起動確認092-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssecattr -c
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0332A
画面・出力には AIX0332A が表示され、lssecattr -c 起動確認 audit class 0332 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0332B
画面・出力には AIX0332B が表示され、lssecattr -c 起動確認 audit class 0332 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0332C
画面・出力には AIX0332C が表示され、lssecattr -c 起動確認 audit class 0332 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0332A が画面・出力に表示されること
② ステップ2 の AIX0332B が画面・出力に表示されること
③ ステップ3 の AIX0332C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0386"><h3>lssecattr -c 起動確認 enhanced_RBAC 0748</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>雪解監査ではAIX 7.3のセキュリティで lssecattr -c を確認します。雪解監査のセキュリティでは enhanced_RBAC とユーザー属性を監査票へ転記します。雪解監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。雪解監査の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、雪解監査を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lssecattr -c 起動確認 enhanced_RBAC 0748の技術的な意味を資料で確認するとき、chlv 属性確認 PP SIZE 0749との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はセキュリティでlssecattr -cを用い・enhanced_RBAC とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はLVMでchlvを用い・PP SIZE とミラーコピー状態を確認する。chlv 属性確認 PP SIZE 0749固有の属性も確認対象に含める。</li><li>C. 管理対象との関係を表す説明はネットワークでnetstat -vを用い・MTU とアダプター一覧を確認する。</li><li>D. 管理対象との関係を表す説明はJFS2でfsckを用い・isnapshot とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでlssecattr -cを用い、enhanced_RBAC」に対応する項目は起動確認 enhanced_RBAC（起動・lsse）です。起動に関するセキュリティの仕様は「セキュリティでlssecattr -cを用い」で、確認対象はls・起動です。属性・chlvのB:は「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（属性・chlv）です。変更後・netsのC:は「ネットワークでnetstat -vを用い、MTU」を述べ、対象は変更後確認 MTU（変更・nets）です。状態・fsckのD:は「JFS2でfsckを用い、isnapshot」を述べ、対象は状態確認 isnapshot（状態・fsck）です。「lssecattr -c」は「セキュリティでlssecattr -cを用い」を指し、起動確認 enhanced_RBACではls・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lssecattr -c 起動確認 enhanced_RBAC 0748</strong></p><p>検証目的: セキュリティのlssecattr -c 起動確認 enhanced_RBAC 0748について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ起動確認028-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssecattr -c
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0748A
画面・出力には AIX0748A が表示され、lssecattr -c 起動確認 enhanced_RBAC 0748 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0748B
画面・出力には AIX0748B が表示され、lssecattr -c 起動確認 enhanced_RBAC 0748 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0748C
画面・出力には AIX0748C が表示され、lssecattr -c 起動確認 enhanced_RBAC 0748 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0748A が画面・出力に表示されること
② ステップ2 の AIX0748B が画面・出力に表示されること
③ ステップ3 の AIX0748C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0387"><h3>lssecattr -c 起動確認 enhanced_RBAC 0808</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>翠風変更ではAIX 7.3のセキュリティで lssecattr -c を確認します。翠風変更のセキュリティでは enhanced_RBAC とユーザー属性を監査票へ転記します。翠風変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。翠風変更の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、翠風変更を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lssecattr -c 起動確認 enhanced_RBAC 0808を同一分類のlparstat 障害切り分け 受信先と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>B. 管理対象との関係を表す説明はネットワークでlsdev -Cc adapterを用い・Gateway とMTU属性を確認する。</li><li>C. 管理対象との関係を表す説明はセキュリティでpwdck -n ALLを用い・authorizations とRBAC属性を確認する。</li><li>D. 管理対象との関係を表す説明はセキュリティでlssecattr -cを用い・enhanced_RBAC とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 起動・lsseでDの記述「セキュリティでlssecattr -cを用い」に対応する項目は起動確認 enhanced_RBAC（起動・lsse）です。起動に関するセキュリティの仕様は「セキュリティでlssecattr -cを用い」で、確認対象はls・起動です。障害切・lparのA:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は障害切り分け 受信先（障害・lpar）です。監査・lsdeのB:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は監査記録 Gateway（監査・lsde）です。変更前・pwdcのC:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は変更前確認 authorizatio（変更・pwdc）です。「lssecattr -c」は「セキュリティでlssecattr -cを用い」を指し、起動確認 enhanced_RBACではls・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lssecattr -c 起動確認 enhanced_RBAC 0808</strong></p><p>検証目的: セキュリティのlssecattr -c 起動確認 enhanced_RBAC 0808について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ起動確認088-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssecattr -c
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0808A
画面・出力には AIX0808A が表示され、lssecattr -c 起動確認 enhanced_RBAC 0808 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0808B
画面・出力には AIX0808B が表示され、lssecattr -c 起動確認 enhanced_RBAC 0808 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0808C
画面・出力には AIX0808C が表示され、lssecattr -c 起動確認 enhanced_RBAC 0808 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0808A が画面・出力に表示されること
② ステップ2 の AIX0808B が画面・出力に表示されること
③ ステップ3 の AIX0808C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0388"><h3>lssecattr -c 障害切り分け audit class 0302</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>紅葉復旧ではAIX 7.3のセキュリティで lssecattr -c を確認します。紅葉復旧のセキュリティでは audit class とRBAC属性を確認票へ整理します。紅葉復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。紅葉復旧の注意点として 監査データ未取得でのroleqry実行 を避けるため lsuser user1 も併記します。権限管理の作業票として、紅葉復旧を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lssecattr -c 障害切り分け audit class 0302に関する障害切り分けの前提を確認しています。lscfg -vl ent0 バックアウト確認 path status 0303の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はデバイス管理でlscfg -vl ent0を用い・path status とODM属性を確認する。</li><li>B. 障害切り分けに用いる役割はSRCとログでsyslog_ssw -cを用い・IDENTIFIER とsyslog設定変換を確認する。</li><li>C. 障害切り分けに用いる役割はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>D. 障害切り分けに用いる役割はセキュリティでlssecattr -cを用い・audit class とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでlssecattr -cを用い、audit class」に対応する項目はaudit class（障害・lsse）です。障害切に関するセキュリティの仕様は「セキュリティでlssecattr -cを用い、audit」で、確認対象はls・障害切です。バック・lscfのA:は「デバイス管理でlscfg -vl ent0を用い、path」を述べ、対象はpath status（バッ・lscf）です。構成・syslのB:は「SRCとログでsyslog_ssw -cを用い」を述べ、対象は構成照合 IDENTIFIER（構成・sysl）です。詳細・表形・errpのC:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は詳細確認 表形式（詳細・errp）です。「lssecattr -c」は「セキュリティでlssecattr -cを用い、audit」を指し、audit classではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lssecattr -c 障害切り分け audit class 0302</strong></p><p>検証目的: セキュリティのlssecattr -c 障害切り分け audit class 0302について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ障害切り分け062-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssecattr -c
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0302A
画面・出力には AIX0302A が表示され、lssecattr -c 障害切り分け audit class 0302 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0302B
画面・出力には AIX0302B が表示され、lssecattr -c 障害切り分け audit class 0302 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0302C
画面・出力には AIX0302C が表示され、lssecattr -c 障害切り分け audit class 0302 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0302A が画面・出力に表示されること
② ステップ2 の AIX0302B が画面・出力に表示されること
③ ステップ3 の AIX0302C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0389"><h3>lssecattr -c 障害切り分け enhanced_RBAC 0778</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>潮騒復旧ではAIX 7.3のセキュリティで lssecattr -c を確認します。潮騒復旧のセキュリティでは enhanced_RBAC とRBAC属性を保守票へ記録します。潮騒復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。潮騒復旧の注意点として 監査データ未取得でのroleqry実行 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、潮騒復旧を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lssecattr -c 障害切り分け enhanced_RBAC 0778の役割を調べています。no -a バックアウト確認 Link Status 0791の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はネットワークでno -aを用い・Link Status とEthernet統計を確認する。</li><li>B. 表示や設定で扱う内容はセキュリティでlssecattr -cを用い・enhanced_RBAC とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はネットワークでroute -n getを用い・MTU とMTU属性を確認する。</li><li>D. 表示や設定で扱う内容はデバイス管理でlsattr -El hdisk0を用い・Available とODM属性を確認する。lsattr -El hdisk0 運用引継ぎ Available固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 障害切・lsseでBの記述「セキュリティでlssecattr -cを用い」に対応する項目は障害切り分け enhanced_RB（障害・lsse）です。障害切に関するセキュリティの仕様は「セキュリティでlssecattr -cを用い」で、確認対象はls・障害切です。バック・noのA:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（バッ・no）です。変更前・routのC:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は変更前確認 MTU（変更・rout）です。運用引・lsatのD:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象は運用引継ぎ Available（運用・lsat）です。「lssecattr -c」は「セキュリティでlssecattr -cを用い」を指し、障害切り分け enhanced_RBではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lssecattr -c 障害切り分け enhanced_RBAC 0778</strong></p><p>検証目的: セキュリティのlssecattr -c 障害切り分け enhanced_RBAC 0778について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ障害切り分け058-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssecattr -c
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0778A
画面・出力には AIX0778A が表示され、lssecattr -c 障害切り分け enhanced_RBAC 0778 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0778B
画面・出力には AIX0778B が表示され、lssecattr -c 障害切り分け enhanced_RBAC 0778 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0778C
画面・出力には AIX0778C が表示され、lssecattr -c 障害切り分け enhanced_RBAC 0778 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0778A が画面・出力に表示されること
② ステップ2 の AIX0778B が画面・出力に表示されること
③ ステップ3 の AIX0778C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0390"><h3>lssecattr -c 障害切り分け enhanced_RBAC 0838</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>春霞変更ではAIX 7.3のセキュリティで lssecattr -c を確認します。春霞変更のセキュリティでは enhanced_RBAC とRBAC属性を保守票へ記録します。春霞変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。春霞変更の注意点として 監査データ未取得でのroleqry実行 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、春霞変更を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lssecattr -c 障害切り分け enhanced_RBAC 0838に関する障害切り分けの前提を確認しています。lsvg 詳細確認 詳細表示の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>B. 表示や設定で扱う内容はネットワークでchdev -l en0 -aを用い・MTU と経路表を確認する。chdev -l en0 -a mtu=1500 変更前確認 MTU固有の属性も確認対象に含める。</li><li>C. 表示や設定で扱う内容はネットワークでnetstat -vを用い・Gateway とアダプター一覧を確認する。</li><li>D. 表示や設定で扱う内容はセキュリティでlssecattr -cを用い・enhanced_RBAC とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 障害切・lsseでDの記述「セキュリティでlssecattr -cを用い」に対応する項目は障害切り分け enhanced_RB（障害・lsse）です。障害切に関するセキュリティの仕様は「セキュリティでlssecattr -cを用い」で、確認対象はls・障害切です。詳細・詳細・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は詳細確認 詳細表示（詳細・lsvg）です。変更前・chdeのB:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は変更前確認 MTU（変更・chde）です。変更後・netsのC:は「ネットワークでnetstat -vを用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・nets）です。「lssecattr -c」は「セキュリティでlssecattr -cを用い」を指し、障害切り分け enhanced_RBではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lssecattr -c 障害切り分け enhanced_RBAC 0838</strong></p><p>検証目的: セキュリティのlssecattr -c 障害切り分け enhanced_RBAC 0838について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ障害切り分け118-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lssecattr -c
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0838A
画面・出力には AIX0838A が表示され、lssecattr -c 障害切り分け enhanced_RBAC 0838 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0838B
画面・出力には AIX0838B が表示され、lssecattr -c 障害切り分け enhanced_RBAC 0838 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0838C
画面・出力には AIX0838C が表示され、lssecattr -c 障害切り分け enhanced_RBAC 0838 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0838A が画面・出力に表示されること
② ステップ2 の AIX0838B が画面・出力に表示されること
③ ステップ3 の AIX0838C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0391"><h3>lsuser バックアウト確認 authorizations 0612</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>水音採取ではAIX 7.3のセキュリティで lsuser を確認します。水音採取のセキュリティでは authorizations とユーザー属性を同じ証跡に残します。水音採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。水音採取の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、水音採取を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser バックアウト確認 authorizations 0612の技術的な意味を資料で確認するとき、varyonvg 監査記録 PVID 0613との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はLVMでvaryonvgを用い・PVID とミラーコピー状態を確認する。</li><li>B. 構成を確認する際の意味は構成済みデバイスと VPD を表示するコマンドである。</li><li>C. 構成を確認する際の意味はJFS2でsplitcopyを用い・ファイルシステム使用率 とマウントオプションを確認する。</li><li>D. 構成を確認する際の意味はセキュリティでlsuserを用い・authorizations とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「セキュリティでlsuserを用い、authorizations」に対応する項目はバックアウト確認 authoriza（バッ・lsus）です。バックに関するセキュリティの仕様は「セキュリティでlsuserを用い、authorizations」で、確認対象はls・バックです。監査・varyのA:は「LVMでvaryonvgを用い、PVID」を述べ、対象は監査記録 PVID（監査・vary）です。障害切・lscfのB:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は障害切り分け ページング状態（障害・lscf）です。運用引・spliのC:は「JFS2でsplitcopyを用い、ファイルシステム使用率」を述べ、対象は運用引継ぎ ファイルシステム使用率（運用・spli）です。「lsuser」は「セキュリティでlsuserを用い、authorizations」を指し、バックアウト確認 authorizaではls・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser バックアウト確認 authorizations 0612</strong></p><p>検証目的: セキュリティのlsuser バックアウト確認 authorizations 0612について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティバックアウト確認012-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0612A
画面・出力には AIX0612A が表示され、lsuser バックアウト確認 authorizations 0612 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0612B
画面・出力には AIX0612B が表示され、lsuser バックアウト確認 authorizations 0612 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0612C
画面・出力には AIX0612C が表示され、lsuser バックアウト確認 authorizations 0612 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0612A が画面・出力に表示されること
② ステップ2 の AIX0612B が画面・出力に表示されること
③ ステップ3 の AIX0612C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0392"><h3>lsuser バックアウト確認 authorizations 0672</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>夕映判定ではAIX 7.3のセキュリティで lsuser を確認します。夕映判定のセキュリティでは authorizations とユーザー属性を同じ証跡に残します。夕映判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。夕映判定の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、夕映判定を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser バックアウト確認 authorizations 0672を同一分類のbootinfo -B hdisk0 監査記録 Available 0673と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はデバイス管理でbootinfo -B hdisk0を用い・Available と診断対象表示を確認する。</li><li>B. 構成を確認する際の意味はネットワークでroute -n getを用い・EtherChannel とアダプター一覧を確認する。</li><li>C. 構成を確認する際の意味はセキュリティでlsuserを用い・authorizations とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はJFS2でlogformを用い・log=INLINE とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでlsuserを用い、authorizations」に対応する項目はバックアウト確認 authoriza（バッ・lsus）です。バックに関するセキュリティの仕様は「セキュリティでlsuserを用い、authorizations」で、確認対象はls・バックです。監査・bootのA:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は監査記録 Available（監査・boot）です。起動・routのB:は「ネットワークでroute -n getを用い」を述べ、対象は起動確認 EtherChannel（起動・rout）です。容量・logfのD:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は容量確認 log=INLINE（容量・logf）です。「lsuser」は「セキュリティでlsuserを用い、authorizations」を指し、バックアウト確認 authorizaではls・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser バックアウト確認 authorizations 0672</strong></p><p>検証目的: セキュリティのlsuser バックアウト確認 authorizations 0672について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティバックアウト確認072-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0672A
画面・出力には AIX0672A が表示され、lsuser バックアウト確認 authorizations 0672 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0672B
画面・出力には AIX0672B が表示され、lsuser バックアウト確認 authorizations 0672 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0672C
画面・出力には AIX0672C が表示され、lsuser バックアウト確認 authorizations 0672 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0672A が画面・出力に表示されること
② ステップ2 の AIX0672B が画面・出力に表示されること
③ ステップ3 の AIX0672C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0393"><h3>lsuser バックアウト確認 user attributes 0136</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>若竹採取ではAIX 7.3のセキュリティで lsuser を確認します。若竹採取のセキュリティでは user attributes とユーザー属性を監査票へ転記します。若竹採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若竹採取の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、若竹採取を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser バックアウト確認 user attributes 0136を同一分類のvaryonvg 監査記録 STALE PARTITIONS 0137と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はLVMでvaryonvgを用い・STALE PARTITIONS とミラーコピー状態を確認する。</li><li>B. 管理対象との関係を表す説明はSRCとログでerrptを用い・Status とSRCサブシステム表示を確認する。</li><li>C. 管理対象との関係を表す説明はセキュリティでlsuserを用い・user attributes とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はLVMでchlvを用い・PP SIZE とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「セキュリティでlsuserを用い、user attributes」に対応する項目はuser attributes（バッ・lsus）です。バックに関するセキュリティの仕様は「セキュリティでlsuserを用い、user attributes」で、確認対象はls・バックです。監査・varyのA:は「LVMでvaryonvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（監査・vary）です。構成・errpのB:は「SRCとログでerrptを用い、Status」を述べ、対象は構成照合 Status（構成・errp）です。属性・chlvのD:は「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」を述べ、対象はPP SIZE（属性・chlv）です。「lsuser」は「セキュリティでlsuserを用い、user attributes」を指し、user attributesではls・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser バックアウト確認 user attributes 0136</strong></p><p>検証目的: セキュリティのlsuser バックアウト確認 user attributes 0136について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティバックアウト確認016-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0136A
画面・出力には AIX0136A が表示され、lsuser バックアウト確認 user attributes 0136 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0136B
画面・出力には AIX0136B が表示され、lsuser バックアウト確認 user attributes 0136 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0136C
画面・出力には AIX0136C が表示され、lsuser バックアウト確認 user attributes 0136 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0136A が画面・出力に表示されること
② ステップ2 の AIX0136B が画面・出力に表示されること
③ ステップ3 の AIX0136C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0394"><h3>lsuser バックアウト確認 user attributes 0196</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>若潮判定ではAIX 7.3のセキュリティで lsuser を確認します。若潮判定のセキュリティでは user attributes とユーザー属性を監査票へ転記します。若潮判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若潮判定の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、若潮判定を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser バックアウト確認 user attributes 0196の技術的な意味を資料で確認するとき、bootinfo -B hdisk0 監査記録 path status 0197との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はデバイス管理でbootinfo -B hdisk0を用い・path status と診断対象表示を確認する。</li><li>B. 管理対象との関係を表す説明はSRCとログでerrpt -aを用い・IDENTIFIER とSRCサブシステム表示を確認する。</li><li>C. 管理対象との関係を表す説明はデバイス管理でlscfg -vl ent0を用い・PVID と診断対象表示を確認する。</li><li>D. 管理対象との関係を表す説明はセキュリティでlsuserを用い・user attributes とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでlsuserを用い、user attributes」に対応する項目はuser attributes（バッ・lsus）です。バックに関するセキュリティの仕様は「セキュリティでlsuserを用い、user attributes」で、確認対象はls・バックです。監査・bootのA:は「デバイス管理でbootinfo -B hdisk0を用い、path」を述べ、対象はpath status（監査・boot）です。変更前・errpのB:は「SRCとログでerrpt -aを用い、IDENTIFIER」を述べ、対象は変更前確認 IDENTIFIER（変更・errp）です。属性・lscfのC:は「デバイス管理でlscfg -vl ent0を用い、PVID」を述べ、対象は属性確認 PVID（属性・lscf）です。「lsuser」は「セキュリティでlsuserを用い、user attributes」を指し、user attributesではls・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser バックアウト確認 user attributes 0196</strong></p><p>検証目的: セキュリティのlsuser バックアウト確認 user attributes 0196について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティバックアウト確認076-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0196A
画面・出力には AIX0196A が表示され、lsuser バックアウト確認 user attributes 0196 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0196B
画面・出力には AIX0196B が表示され、lsuser バックアウト確認 user attributes 0196 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0196C
画面・出力には AIX0196C が表示され、lsuser バックアウト確認 user attributes 0196 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0196A が画面・出力に表示されること
② ステップ2 の AIX0196B が画面・出力に表示されること
③ ステップ3 の AIX0196C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0395"><h3>lsuser 属性確認 authorizations 0642</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>春分判定ではAIX 7.3のセキュリティで lsuser を確認します。春分判定のセキュリティでは authorizations とRBAC属性を変更票へ記録します。春分判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。春分判定の注意点として 監査データ未取得でのroleqry実行 を避けるため lsrole ALL も併記します。権限管理の作業票として、春分判定を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser 属性確認 authorizations 0642の役割を調べています。bootinfo -B hdisk0 状態確認 PVID 0643の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはデバイス管理でbootinfo -B hdisk0を用い・PVID とODM属性を確認する。</li><li>B. 機能の説明としてはネットワークでroute -n getを用い・MTU と経路表を確認する。</li><li>C. 機能の説明としてはセキュリティでlsuserを用い・authorizations とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはJFS2でsplitcopyを用い・isnapshot と内部スナップショットを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでlsuserを用い、authorizations」に対応する項目は属性確認 authorization（属性・lsus）です。属性に関するセキュリティの仕様は「セキュリティでlsuserを用い、authorizations」で、確認対象はls・属性です。状態・bootのA:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・boot）です。障害切・routのB:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は障害切り分け MTU（障害・rout）です。構成・spliのD:は「JFS2でsplitcopyを用い、isnapshot」を述べ、対象は構成照合 isnapshot（構成・spli）です。「lsuser」は「セキュリティでlsuserを用い、authorizations」を指し、属性確認 authorizationではls・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser 属性確認 authorizations 0642</strong></p><p>検証目的: セキュリティのlsuser 属性確認 authorizations 0642について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認042-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0642A
画面・出力には AIX0642A が表示され、lsuser 属性確認 authorizations 0642 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0642B
画面・出力には AIX0642B が表示され、lsuser 属性確認 authorizations 0642 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0642C
画面・出力には AIX0642C が表示され、lsuser 属性確認 authorizations 0642 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0642A が画面・出力に表示されること
② ステップ2 の AIX0642B が画面・出力に表示されること
③ ステップ3 の AIX0642C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0396"><h3>lsuser 属性確認 authorizations 0702</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>紅葉保守ではAIX 7.3のセキュリティで lsuser を確認します。紅葉保守のセキュリティでは authorizations とRBAC属性を変更票へ記録します。紅葉保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。紅葉保守の注意点として 監査データ未取得でのroleqry実行 を避けるため lsrole ALL も併記します。権限管理の作業票として、紅葉保守を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser 属性確認 authorizations 0702に関する障害切り分けの前提を確認しています。bootinfo -B hdisk0 状態確認 PVID 0703の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはデバイス管理でbootinfo -B hdisk0を用い・PVID とODM属性を確認する。</li><li>B. 機能の説明としてはネットワークでroute -n getを用い・MTU と経路表を確認する。</li><li>C. 機能の説明としてはセキュリティでlsuserを用い・authorizations とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはJFS2でlogformを用い・mountguard と内部スナップショットを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「セキュリティでlsuserを用い、authorizations」に対応する項目は属性確認 authorization（属性・lsus）です。属性に関するセキュリティの仕様は「セキュリティでlsuserを用い、authorizations」で、確認対象はls・属性です。状態・bootのA:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・boot）です。障害切・routのB:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は障害切り分け MTU（障害・rout）です。変更前・logfのD:は「JFS2でlogformを用い、mountguard」を述べ、対象は変更前確認 mountguard（変更・logf）です。「lsuser」は「セキュリティでlsuserを用い、authorizations」を指し、属性確認 authorizationではls・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser 属性確認 authorizations 0702</strong></p><p>検証目的: セキュリティのlsuser 属性確認 authorizations 0702について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認102-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0702A
画面・出力には AIX0702A が表示され、lsuser 属性確認 authorizations 0702 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0702B
画面・出力には AIX0702B が表示され、lsuser 属性確認 authorizations 0702 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0702C
画面・出力には AIX0702C が表示され、lsuser 属性確認 authorizations 0702 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0702A が画面・出力に表示されること
② ステップ2 の AIX0702B が画面・出力に表示されること
③ ステップ3 の AIX0702C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0397"><h3>lsuser 属性確認 user attributes 0166</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>朝凪判定ではAIX 7.3のセキュリティで lsuser を確認します。朝凪判定のセキュリティでは user attributes とRBAC属性を保守票へ記録します。朝凪判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。朝凪判定の注意点として 監査データ未取得でのroleqry実行 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、朝凪判定を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser 属性確認 user attributes 0166に関する障害切り分けの前提を確認しています。bootinfo -B hdisk0 状態確認 location code 0167の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はデバイス管理でbootinfo -B hdisk0を用い・location code とODM属性を確認する。</li><li>B. 表示や設定で扱う内容はセキュリティでlsuserを用い・user attributes とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はSRCとログでerrptを用い・syslog.conf とsyslog設定変換を確認する。</li><li>D. 表示や設定で扱う内容はデバイス管理でlscfg -vl ent0を用い・Available とODM属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでlsuserを用い、user attributes」に対応する項目はuser attributes（属性・lsus）です。属性に関するセキュリティの仕様は「セキュリティでlsuserを用い、user attributes」で、確認対象はls・属性です。状態・bootのA:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象はlocation code（状態・boot）です。運用引・errpのC:は「SRCとログでerrptを用い、syslog.conf」を述べ、対象は運用引継ぎ syslog.conf（運用・errp）です。バック・lscfのD:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象はバックアウト確認 Available（バッ・lscf）です。「lsuser」は「セキュリティでlsuserを用い、user attributes」を指し、user attributesではls・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser 属性確認 user attributes 0166</strong></p><p>検証目的: セキュリティのlsuser 属性確認 user attributes 0166について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認046-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0166A
画面・出力には AIX0166A が表示され、lsuser 属性確認 user attributes 0166 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0166B
画面・出力には AIX0166B が表示され、lsuser 属性確認 user attributes 0166 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0166C
画面・出力には AIX0166C が表示され、lsuser 属性確認 user attributes 0166 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0166A が画面・出力に表示されること
② ステップ2 の AIX0166B が画面・出力に表示されること
③ ステップ3 の AIX0166C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0398"><h3>lsuser 属性確認 user attributes 0226</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>陽炎保守ではAIX 7.3のセキュリティで lsuser を確認します。陽炎保守のセキュリティでは user attributes とRBAC属性を保守票へ記録します。陽炎保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。陽炎保守の注意点として 監査データ未取得でのroleqry実行 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、陽炎保守を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser 属性確認 user attributes 0226の役割を調べています。bootinfo -B hdisk0 状態確認 location code 0227の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はデバイス管理でbootinfo -B hdisk0を用い・location code とODM属性を確認する。</li><li>B. 表示や設定で扱う内容はSRCとログでerrpt -aを用い・Subsystem とsyslog設定変換を確認する。</li><li>C. 表示や設定で扱う内容はセキュリティでlsuserを用い・user attributes とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はデバイス管理でlscfg -vl ent0を用い・Available とODM属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「セキュリティでlsuserを用い、user attributes」に対応する項目はuser attributes（属性・lsus）です。属性に関するセキュリティの仕様は「セキュリティでlsuserを用い、user attributes」で、確認対象はls・属性です。状態・bootのA:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象はlocation code（状態・boot）です。容量・errpのB:は「SRCとログでerrpt -aを用い、Subsystem」を述べ、対象は容量確認 Subsystem（容量・errp）です。バック・lscfのD:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象はバックアウト確認 Available（バッ・lscf）です。「lsuser」は「セキュリティでlsuserを用い、user attributes」を指し、user attributesではls・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser 属性確認 user attributes 0226</strong></p><p>検証目的: セキュリティのlsuser 属性確認 user attributes 0226について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認106-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0226A
画面・出力には AIX0226A が表示され、lsuser 属性確認 user attributes 0226 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0226B
画面・出力には AIX0226B が表示され、lsuser 属性確認 user attributes 0226 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0226C
画面・出力には AIX0226C が表示され、lsuser 属性確認 user attributes 0226 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0226A が画面・出力に表示されること
② ステップ2 の AIX0226B が画面・出力に表示されること
③ ステップ3 の AIX0226C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0399"><h3>lsuser 性能確認 enhanced_RBAC 0355</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>青磁変更ではAIX 7.3のセキュリティで lsuser を確認します。青磁変更のセキュリティでは enhanced_RBAC とロール一覧を点検票へ整理します。青磁変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。青磁変更の注意点として ユーザー属性変更の根拠不足 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、青磁変更を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser 性能確認 enhanced_RBAC 0355について構成や状態を確認します。bootinfo -B hdisk0 起動確認 Available 0356ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはデバイス管理でbootinfo -B hdisk0を用い・Availableである。</li><li>B. 対象資源に対する働きはセキュリティでlsuserを用い・enhanced_RBAC とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはSRCとログでerrpt -aを用い・Subsystem とinetdデバッグ出力を確認する。</li><li>D. 対象資源に対する働きはJFS2でlogformを用い・log=INLINE とログデバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「セキュリティでlsuserを用い、enhanced_RBAC とロール一覧を確認する」に対応する項目は性能確認 enhanced_RBAC（性能・lsus）です。性能に関するセキュリティの仕様は「セキュリティでlsuserを用い、enhanced_RBAC」で、確認対象はls・性能です。起動・bootのA:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は起動確認 Available（起動・boot）です。監査・errpのC:は「SRCとログでerrpt -aを用い、Subsystem」を述べ、対象は監査記録 Subsystem（監査・errp）です。状態・logfのD:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は状態確認 log=INLINE（状態・logf）です。「lsuser」は「セキュリティでlsuserを用い、enhanced_RBAC」を指し、性能確認 enhanced_RBACではls・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser 性能確認 enhanced_RBAC 0355</strong></p><p>検証目的: セキュリティのlsuser 性能確認 enhanced_RBAC 0355について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ性能確認115-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0355A
画面・出力には AIX0355A が表示され、lsuser 性能確認 enhanced_RBAC 0355 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0355B
画面・出力には AIX0355B が表示され、lsuser 性能確認 enhanced_RBAC 0355 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0355C
画面・出力には AIX0355C が表示され、lsuser 性能確認 enhanced_RBAC 0355 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0355A が画面・出力に表示されること
② ステップ2 の AIX0355B が画面・出力に表示されること
③ ステップ3 の AIX0355C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0400"><h3>lsuser 性能確認 roles 0831</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>遠雷変更ではAIX 7.3のセキュリティで lsuser を確認します。遠雷変更のセキュリティでは roles とロール一覧を作業票へ保管します。遠雷変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。遠雷変更の注意点として ユーザー属性変更の根拠不足 を避けるため lsrole ALL も併記します。権限管理の作業票として、遠雷変更を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser 性能確認 roles 0831の設定や表示を読む前に役割を確認します。vmstat 復旧前確認 出力見出しではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはセキュリティでlsuserを用い・roles とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 状態を読み取るための働きはCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>C. 状態を読み取るための働きはSRCとログでtail -f /tmp/myfileを用い・Subsystemである。</li><li>D. 状態を読み取るための働きは性能管理でfilemonを用い・po とAME統計を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 性能・lsusでAの記述「セキュリティでlsuserを用い、roles とロール一覧を確認する」に対応する項目は性能確認 roles（性能・lsus）です。性能に関するセキュリティの仕様は「セキュリティでlsuserを用い、roles とロール一覧を確認する」で、確認対象はls・性能です。復旧前・vmstのB:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は復旧前確認 出力見出し（復旧・vmst）です。属性・tailのC:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は属性確認 Subsystem（属性・tail）です。構成・fileのD:は「性能管理でfilemonを用い、po とAME統計を確認する」を述べ、対象は構成照合 po（構成・file）です。「lsuser」は「セキュリティでlsuserを用い、roles とロール一覧を確認する」を指し、性能確認 rolesではls・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser 性能確認 roles 0831</strong></p><p>検証目的: セキュリティのlsuser 性能確認 roles 0831について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ性能確認111-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0831A
画面・出力には AIX0831A が表示され、lsuser 性能確認 roles 0831 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0831B
画面・出力には AIX0831B が表示され、lsuser 性能確認 roles 0831 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0831C
画面・出力には AIX0831C が表示され、lsuser 性能確認 roles 0831 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0831A が画面・出力に表示されること
② ステップ2 の AIX0831B が画面・出力に表示されること
③ ステップ3 の AIX0831C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0401"><h3>lsuser 構成照合 authorizations 0513</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>朝霧確認ではAIX 7.3のセキュリティで lsuser を確認します。朝霧確認のセキュリティでは authorizations と監査設定を判定票へ残します。朝霧確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。朝霧確認の注意点として ロール割当と権限文字列の不一致 を避けるため lsrole ALL も併記します。権限管理の作業票として、朝霧確認を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lsuser 構成照合 authorizations 0513」を「bootinfo -B hdisk0 変更前確認 PVID 0514」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はセキュリティでlsuserを用い・authorizations と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はデバイス管理でbootinfo -B hdisk0を用い・PVID とデバイス一覧を確認する。</li><li>C. 運用時に利用する技術的役割はSRCとログでerrptを用い・Status とエラーログ一覧を確認する。</li><li>D. 運用時に利用する技術的役割はJFS2でsplitcopyを用い・isnapshot とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでlsuserを用い、authorizations と監査設定を確認する」に対応する項目は構成照合 authorization（構成・lsus）です。構成に関するセキュリティの仕様は「セキュリティでlsuserを用い、authorizations」で、確認対象はls・構成です。変更前・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を述べ、対象は変更前確認 PVID（変更・boot）です。性能・errpのC:は「SRCとログでerrptを用い、Status」を述べ、対象は性能確認 Status（性能・errp）です。変更後・spliのD:は「JFS2でsplitcopyを用い、isnapshot」を述べ、対象は変更後確認 isnapshot（変更・spli）です。「lsuser」は「セキュリティでlsuserを用い、authorizations」を指し、構成照合 authorizationではls・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser 構成照合 authorizations 0513</strong></p><p>検証目的: セキュリティのlsuser 構成照合 authorizations 0513について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ構成照合033-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0513A
画面・出力には AIX0513A が表示され、lsuser 構成照合 authorizations 0513 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0513B
画面・出力には AIX0513B が表示され、lsuser 構成照合 authorizations 0513 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0513C
画面・出力には AIX0513C が表示され、lsuser 構成照合 authorizations 0513 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0513A が画面・出力に表示されること
② ステップ2 の AIX0513B が画面・出力に表示されること
③ ステップ3 の AIX0513C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0402"><h3>lsuser 構成照合 user attributes 0037</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>冬晴確認ではAIX 7.3のセキュリティで lsuser を確認します。冬晴確認のセキュリティでは user attributes と監査設定を採取票へ記録します。冬晴確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。冬晴確認の注意点として ロール割当と権限文字列の不一致 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、冬晴確認を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser 構成照合 user attributes 0037を保守記録に説明する必要があります。bootinfo -B hdisk0 変更前確認 location codeと取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はセキュリティでlsuserを用い・user attributes と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はデバイス管理でbootinfo -B hdisk0を用い・location codeである。</li><li>C. 保守作業で参照する機能はSRCとログでerrptを用い・Subsystem とエラーログ一覧を確認する。</li><li>D. 保守作業で参照する機能はデバイス管理でlscfg -vl ent0を用い・Available とデバイス一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでlsuserを用い、user attributes」に対応する項目はuser attributes（構成・lsus）です。セキュリティの仕様は「セキュリティでlsuserを用い、user attributes」で、確認対象はls・構成です。変更前・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象はlocation code（変更・boot）です。性能・errpのC:は「SRCとログでerrptを用い、Subsystem」を述べ、対象は性能確認 Subsystem（性能・errp）です。運用引・lscfのD:は「デバイス管理でlscfg -vl ent0を用い」を述べ、対象は運用引継ぎ Available（運用・lscf）です。「lsuser」は「セキュリティでlsuserを用い、user attributes」を指し、user attributesではls・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser 構成照合 user attributes 0037</strong></p><p>検証目的: セキュリティのlsuser 構成照合 user attributes 0037について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ構成照合037-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0037A
画面・出力には AIX0037A が表示され、lsuser 構成照合 user attributes 0037 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0037B
画面・出力には AIX0037B が表示され、lsuser 構成照合 user attributes 0037 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0037C
画面・出力には AIX0037C が表示され、lsuser 構成照合 user attributes 0037 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0037A が画面・出力に表示されること
② ステップ2 の AIX0037B が画面・出力に表示されること
③ ステップ3 の AIX0037C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0403"><h3>lsuser 運用引継ぎ authorizations 0483</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>秋声確認ではAIX 7.3のセキュリティで lsuser を確認します。秋声確認のセキュリティでは authorizations とロール一覧を作業票へ保管します。秋声確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。秋声確認の注意点として ユーザー属性変更の根拠不足 を避けるため lsrole ALL も併記します。権限管理の作業票として、秋声確認を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser 運用引継ぎ authorizations 0483について構成や状態を確認します。bootinfo -B hdisk0 容量確認 Available 0484ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはデバイス管理でbootinfo -B hdisk0を用い・Availableである。</li><li>B. 状態を読み取るための働きはSRCとログでerrptを用い・syslog.conf とinetdデバッグ出力を確認する。</li><li>C. 状態を読み取るための働きはJFS2でsplitcopyを用い・ファイルシステム使用率 とログデバイス設定を確認する。</li><li>D. 状態を読み取るための働きはセキュリティでlsuserを用い・authorizations とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「セキュリティでlsuserを用い、authorizations」に対応する項目は運用引継ぎ authorizatio（運用・lsus）です。運用引に関するセキュリティの仕様は「セキュリティでlsuserを用い、authorizations」で、確認対象はls・運用引です。容量・bootのA:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象は容量確認 Available（容量・boot）です。変更後・errpのB:は「SRCとログでerrptを用い、syslog.conf」を述べ、対象は変更後確認 syslog.conf（変更・errp）です。性能・ファ・spliのC:は「JFS2でsplitcopyを用い、ファイルシステム使用率」を述べ、対象は性能確認 ファイルシステム使用率（性能・spli）です。「lsuser」は「セキュリティでlsuserを用い、authorizations」を指し、運用引継ぎ authorizatioではls・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser 運用引継ぎ authorizations 0483</strong></p><p>検証目的: セキュリティのlsuser 運用引継ぎ authorizations 0483について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ運用引継ぎ003-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0483A
画面・出力には AIX0483A が表示され、lsuser 運用引継ぎ authorizations 0483 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0483B
画面・出力には AIX0483B が表示され、lsuser 運用引継ぎ authorizations 0483 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0483C
画面・出力には AIX0483C が表示され、lsuser 運用引継ぎ authorizations 0483 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0483A が画面・出力に表示されること
② ステップ2 の AIX0483B が画面・出力に表示されること
③ ステップ3 の AIX0483C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0404"><h3>lsuser 運用引継ぎ user attributes 0007</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>夕凪確認ではAIX 7.3のセキュリティで lsuser を確認します。夕凪確認のセキュリティでは user attributes とロール一覧を点検票へ整理します。夕凪確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。夕凪確認の注意点として ユーザー属性変更の根拠不足 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、夕凪確認を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsuser 運用引継ぎ user attributes 0007の設定や表示を読む前に役割を確認します。bootinfo -B hdisk0 容量確認 path status 0008ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはデバイス管理でbootinfo -B hdisk0を用い・path statusである。</li><li>B. 対象資源に対する働きはSRCとログでerrptを用い・IDENTIFIER とinetdデバッグ出力を確認する。</li><li>C. 対象資源に対する働きはデバイス管理でlscfg -vl ent0を用い・PVID と構成マネージャー結果を確認する。</li><li>D. 対象資源に対する働きはセキュリティでlsuserを用い・user attributes とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「セキュリティでlsuserを用い、user attributes」に対応する項目はuser attributes（運用・lsus）です。セキュリティの仕様は「セキュリティでlsuserを用い、user attributes」で、確認対象はls・運用引です。容量・bootのA:は「デバイス管理でbootinfo -B hdisk0を用い、path」を述べ、対象はpath status（容量・boot）です。変更後・errpのB:は「SRCとログでerrptを用い、IDENTIFIER」を述べ、対象は変更後確認 IDENTIFIER（変更・errp）です。構成・lscfのC:は「デバイス管理でlscfg -vl ent0を用い、PVID」を述べ、対象は構成照合 PVID（構成・lscf）です。「lsuser」は「セキュリティでlsuserを用い、user attributes」を指し、user attributesではls・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsuser 運用引継ぎ user attributes 0007</strong></p><p>検証目的: セキュリティのlsuser 運用引継ぎ user attributes 0007について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ運用引継ぎ007-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0007A
画面・出力には AIX0007A が表示され、lsuser 運用引継ぎ user attributes 0007 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0007B
画面・出力には AIX0007B が表示され、lsuser 運用引継ぎ user attributes 0007 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0007C
画面・出力には AIX0007C が表示され、lsuser 運用引継ぎ user attributes 0007 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0007A が画面・出力に表示されること
② ステップ2 の AIX0007B が画面・出力に表示されること
③ ステップ3 の AIX0007C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0405"><h3>pwdck -n ALL 変更前確認 authorizations 0574</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>星霜点検ではAIX 7.3のセキュリティで pwdck -n ALL を確認します。星霜点検のセキュリティでは authorizations とRBAC属性を保守票へ記録します。星霜点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。星霜点検の注意点として 監査データ未取得でのroleqry実行 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、星霜点検を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> pwdck -n ALL 変更前確認 authorizations 0574に関する障害切り分けの前提を確認しています。lsmpio -l hdisk0 変更後確認 path status 0575の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はデバイス管理でlsmpio -l hdisk0を用い・path status とODM属性を確認する。</li><li>B. 表示や設定で扱う内容はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>C. 表示や設定で扱う内容はJFS2でdefragfsを用い・lff と内部スナップショットを確認する。</li><li>D. 表示や設定で扱う内容はセキュリティでpwdck -n ALLを用い・authorizations とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでpwdck -n ALLを用い、authorizations」に対応する項目は変更前確認 authorizatio（変更・pwdc）です。変更前に関するセキュリティの仕様は「セキュリティでpwdck -n ALLを用い」で、確認対象はpw・変更前です。変更後・lsmpのA:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（変更・lsmp）です。状態・変更・lparのB:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は状態判定 変更証跡（状態・lpar）です。バック・defrのC:は「JFS2でdefragfsを用い、lff」を述べ、対象はバックアウト確認 lff（バッ・defr）です。「pwdck -n ALL」は「セキュリティでpwdck -n ALLを用い」を指し、変更前確認 authorizatioではpw・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>pwdck -n ALL 変更前確認 authorizations 0574</strong></p><p>検証目的: セキュリティのpwdck -n ALL 変更前確認 authorizations 0574について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更前確認094-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; pwdck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0574A
画面・出力には AIX0574A が表示され、pwdck -n ALL 変更前確認 authorizations 0574 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0574B
画面・出力には AIX0574B が表示され、pwdck -n ALL 変更前確認 authorizations 0574 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0574C
画面・出力には AIX0574C が表示され、pwdck -n ALL 変更前確認 authorizations 0574 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0574A が画面・出力に表示されること
② ステップ2 の AIX0574B が画面・出力に表示されること
③ ステップ3 の AIX0574C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0406"><h3>pwdck -n ALL 変更前確認 user attributes 0098</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>潮騒点検ではAIX 7.3のセキュリティで pwdck -n ALL を確認します。潮騒点検のセキュリティでは user attributes とRBAC属性を確認票へ整理します。潮騒点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。潮騒点検の注意点として 監査データ未取得でのroleqry実行 を避けるため lsuser user1 も併記します。権限管理の作業票として、潮騒点検を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> pwdck -n ALL 変更前確認 user attributes 0098の役割を調べています。lsmpio -l hdisk0 変更後確認 attribute 0099の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はデバイス管理でlsmpio -l hdisk0を用い・attribute とODM属性を確認する。</li><li>B. 障害切り分けに用いる役割はセキュリティでpwdck -n ALLを用い・user attributes とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割はSRCとログでerrclearを用い・PID とsyslog設定変換を確認する。errclear 属性確認 PID 0404固有の属性も確認対象に含める。</li><li>D. 障害切り分けに用いる役割はデバイス管理でdiag -d ent0を用い・location code とODM属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでpwdck -n ALLを用い、user attributes」に対応する項目はuser attributes（変更・pwdc）です。変更前に関するセキュリティの仕様は「セキュリティでpwdck -n ALLを用い、user」で、確認対象はpw・変更前です。変更後・lsmpのA:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象は変更後確認 attribute（変更・lsmp）です。属性・errcのC:は「SRCとログでerrclearを用い、PID」を述べ、対象は属性確認 PID（属性・errc）です。容量・diagのD:は「デバイス管理でdiag -d ent0を用い、location」を述べ、対象はlocation code（容量・diag）です。「pwdck -n ALL」は「セキュリティでpwdck -n ALLを用い、user」を指し、user attributesではpw・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>pwdck -n ALL 変更前確認 user attributes 0098</strong></p><p>検証目的: セキュリティのpwdck -n ALL 変更前確認 user attributes 0098について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更前確認098-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; pwdck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0098A
画面・出力には AIX0098A が表示され、pwdck -n ALL 変更前確認 user attributes 0098 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0098B
画面・出力には AIX0098B が表示され、pwdck -n ALL 変更前確認 user attributes 0098 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0098C
画面・出力には AIX0098C が表示され、pwdck -n ALL 変更前確認 user attributes 0098 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0098A が画面・出力に表示されること
② ステップ2 の AIX0098B が画面・出力に表示されること
③ ステップ3 の AIX0098C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0407"><h3>pwdck -n ALL 容量確認 authorizations 0544</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>霜月照合ではAIX 7.3のセキュリティで pwdck -n ALL を確認します。霜月照合のセキュリティでは authorizations とユーザー属性を監査票へ転記します。霜月照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。霜月照合の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、霜月照合を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> pwdck -n ALL 容量確認 authorizations 0544を同一分類のchvg 性能確認 VG STATE 0545と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はセキュリティでpwdck -n ALLを用い・authorizations とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はLVMでchvgを用い・VG STATE とミラーコピー状態を確認する。</li><li>C. 管理対象との関係を表す説明はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>D. 管理対象との関係を表す説明はJFS2でlogformを用い・log=INLINE とマウントオプションを確認する。logform 起動確認 log=INLINE 0237固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでpwdck -n ALLを用い、authorizations」に対応する項目は容量確認 authorization（容量・pwdc）です。容量に関するセキュリティの仕様は「セキュリティでpwdck -n ALLを用い」で、確認対象はpw・容量です。性能・chvgのB:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（性能・chvg）です。詳細・保存・lparのC:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は詳細確認 保存場所（詳細・lpar）です。起動・logfのD:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は起動確認 log=INLINE（起動・logf）です。「pwdck -n ALL」は「セキュリティでpwdck -n ALLを用い」を指し、容量確認 authorizationではpw・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>pwdck -n ALL 容量確認 authorizations 0544</strong></p><p>検証目的: セキュリティのpwdck -n ALL 容量確認 authorizations 0544について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ容量確認064-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; pwdck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0544A
画面・出力には AIX0544A が表示され、pwdck -n ALL 容量確認 authorizations 0544 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0544B
画面・出力には AIX0544B が表示され、pwdck -n ALL 容量確認 authorizations 0544 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0544C
画面・出力には AIX0544C が表示され、pwdck -n ALL 容量確認 authorizations 0544 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0544A が画面・出力に表示されること
② ステップ2 の AIX0544B が画面・出力に表示されること
③ ステップ3 の AIX0544C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0408"><h3>pwdck -n ALL 容量確認 user attributes 0068</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>雪解照合ではAIX 7.3のセキュリティで pwdck -n ALL を確認します。雪解照合のセキュリティでは user attributes とユーザー属性を引継ぎ票へ保管します。雪解照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。雪解照合の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、雪解照合を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> pwdck -n ALL 容量確認 user attributes 0068の技術的な意味を資料で確認するとき、chvg 性能確認 MIRROR WRITE CONSISTENCY 0069との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はセキュリティでpwdck -n ALLを用い・user attributes とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はLVMでchvgを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。</li><li>C. コマンドまたは機能の用途はSRCとログでerrclearを用い・TIMESTAMP とSRCサブシステム表示を確認する。errclear バックアウト確認 TIMESTAMP 0374固有の属性も確認対象に含める。</li><li>D. コマンドまたは機能の用途はLVMでmirrorvgを用い・STALE PARTITIONS とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでpwdck -n ALLを用い、user attributes」に対応する項目はuser attributes（容量・pwdc）です。セキュリティの仕様は「セキュリティでpwdck -n ALLを用い、user」で、確認対象はpw・容量です。性能・chvgのB:は「LVMでchvgを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（性能・chvg）です。バック・errcのC:は「SRCとログでerrclearを用い、TIMESTAMP」を述べ、対象はバックアウト確認 TIMESTAMP（バッ・errc）です。変更前・mirrのD:は「LVMでmirrorvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（変更・mirr）です。「pwdck -n ALL」は「セキュリティでpwdck -n ALLを用い、user」を指し、user attributesではpw・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>pwdck -n ALL 容量確認 user attributes 0068</strong></p><p>検証目的: セキュリティのpwdck -n ALL 容量確認 user attributes 0068について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ容量確認068-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; pwdck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0068A
画面・出力には AIX0068A が表示され、pwdck -n ALL 容量確認 user attributes 0068 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0068B
画面・出力には AIX0068B が表示され、pwdck -n ALL 容量確認 user attributes 0068 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0068C
画面・出力には AIX0068C が表示され、pwdck -n ALL 容量確認 user attributes 0068 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0068A が画面・出力に表示されること
② ステップ2 の AIX0068B が画面・出力に表示されること
③ ステップ3 の AIX0068C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0409"><h3>pwdck -n ALL 監査記録 enhanced_RBAC 0256</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>若竹監査ではAIX 7.3のセキュリティで pwdck -n ALL を確認します。若竹監査のセキュリティでは enhanced_RBAC とユーザー属性を監査票へ転記します。若竹監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若竹監査の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、若竹監査を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> pwdck -n ALL 監査記録 enhanced_RBAC 0256を同一分類のlsmpio -l hdisk0 運用引継ぎ microcode levelと比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はデバイス管理でlsmpio -l hdisk0を用い・microcode levelである。lsmpio -l hdisk0 運用引継ぎ microcode固有の属性も確認対象に含める。</li><li>B. 管理対象との関係を表す説明はセキュリティでpwdck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はSRCとログでerrpt -aを用い・IDENTIFIER とSRCサブシステム表示を確認する。</li><li>D. 管理対象との関係を表す説明はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「セキュリティでpwdck -n ALLを用い、enhanced_RBAC」に対応する項目は監査記録 enhanced_RBAC（監査・pwdc）です。監査に関するセキュリティの仕様は「セキュリティでpwdck -n ALLを用い」で、確認対象はpw・監査です。運用引・lsmpのA:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はmicrocode level（運用・lsmp）です。変更前・errpのC:は「SRCとログでerrpt -aを用い、IDENTIFIER」を述べ、対象は変更前確認 IDENTIFIER（変更・errp）です。変更前・vmstのD:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は変更前確認 性能値（変更・vmst）です。「pwdck -n ALL」は「セキュリティでpwdck -n ALLを用い」を指し、監査記録 enhanced_RBACではpw・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>pwdck -n ALL 監査記録 enhanced_RBAC 0256</strong></p><p>検証目的: セキュリティのpwdck -n ALL 監査記録 enhanced_RBAC 0256について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ監査記録016-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; pwdck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0256A
画面・出力には AIX0256A が表示され、pwdck -n ALL 監査記録 enhanced_RBAC 0256 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0256B
画面・出力には AIX0256B が表示され、pwdck -n ALL 監査記録 enhanced_RBAC 0256 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0256C
画面・出力には AIX0256C が表示され、pwdck -n ALL 監査記録 enhanced_RBAC 0256 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0256A が画面・出力に表示されること
② ステップ2 の AIX0256B が画面・出力に表示されること
③ ステップ3 の AIX0256C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0410"><h3>pwdck -n ALL 監査記録 roles 0732</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>水音監査ではAIX 7.3のセキュリティで pwdck -n ALL を確認します。水音監査のセキュリティでは roles とユーザー属性を同じ証跡に残します。水音監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。水音監査の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、水音監査を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> pwdck -n ALL 監査記録 roles 0732の技術的な意味を資料で確認するとき、lsmpio -l hdisk0 運用引継ぎ location code 0733との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はデバイス管理でlsmpio -l hdisk0を用い・location code と診断対象表示を確認する。</li><li>B. 構成を確認する際の意味は導入と起動でbootlist -m normalを用い・mksysb image とOSレベル表示を確認する。</li><li>C. 構成を確認する際の意味はセキュリティでpwdck -n ALLを用い・roles とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はLVMでvaryonvgを用い・PVID とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「セキュリティでpwdck -n ALLを用い、roles とユーザー属性を確認する」に対応する項目は監査記録 roles（監査・pwdc）です。監査に関するセキュリティの仕様は「セキュリティでpwdck -n ALLを用い、roles」で、確認対象はpw・監査です。運用引・lsmpのA:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はlocation code（運用・lsmp）です。起動・bootのB:は「導入と起動でbootlist -m normalを用い」を述べ、対象はmksysb image（起動・boot）です。容量・varyのD:は「LVMでvaryonvgを用い、PVID」を述べ、対象は容量確認 PVID（容量・vary）です。「pwdck -n ALL」は「セキュリティでpwdck -n ALLを用い、roles」を指し、監査記録 rolesではpw・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>pwdck -n ALL 監査記録 roles 0732</strong></p><p>検証目的: セキュリティのpwdck -n ALL 監査記録 roles 0732について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ監査記録012-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; pwdck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0732A
画面・出力には AIX0732A が表示され、pwdck -n ALL 監査記録 roles 0732 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0732B
画面・出力には AIX0732B が表示され、pwdck -n ALL 監査記録 roles 0732 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0732C
画面・出力には AIX0732C が表示され、pwdck -n ALL 監査記録 roles 0732 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0732A が画面・出力に表示されること
② ステップ2 の AIX0732B が画面・出力に表示されること
③ ステップ3 の AIX0732C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0411"><h3>pwdck -n ALL 起動確認 authorizations 0415</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>岩清水評価ではAIX 7.3のセキュリティで pwdck -n ALL を確認します。岩清水評価のセキュリティでは authorizations とロール一覧を点検票へ整理します。岩清水評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。岩清水評価の注意点として ユーザー属性変更の根拠不足 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、岩清水評価を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> pwdck -n ALL 起動確認 authorizations 0415の設定や表示を読む前に役割を確認します。lsmpio -l hdisk0 属性確認 location code 0416ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはデバイス管理でlsmpio -l hdisk0を用い・location codeである。</li><li>B. 対象資源に対する働きはSRCとログでerrclearを用い・PID とinetdデバッグ出力を確認する。</li><li>C. 対象資源に対する働きはセキュリティでpwdck -n ALLを用い・authorizations とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはJFS2でlogformを用い・log=INLINE とログデバイス設定を確認する。logform 状態確認 log=INLINE 0108固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでpwdck -n ALLを用い、authorizations」に対応する項目は起動確認 authorization（起動・pwdc）です。起動に関するセキュリティの仕様は「セキュリティでpwdck -n ALLを用い」で、確認対象はpw・起動です。属性・lsmpのA:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象はlocation code（属性・lsmp）です。運用引・errcのB:は「SRCとログでerrclearを用い、PID」を述べ、対象は運用引継ぎ PID（運用・errc）です。状態・logfのD:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は状態確認 log=INLINE（状態・logf）です。「pwdck -n ALL」は「セキュリティでpwdck -n ALLを用い」を指し、起動確認 authorizationではpw・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>pwdck -n ALL 起動確認 authorizations 0415</strong></p><p>検証目的: セキュリティのpwdck -n ALL 起動確認 authorizations 0415について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ起動確認055-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; pwdck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0415A
画面・出力には AIX0415A が表示され、pwdck -n ALL 起動確認 authorizations 0415 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0415B
画面・出力には AIX0415B が表示され、pwdck -n ALL 起動確認 authorizations 0415 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0415C
画面・出力には AIX0415C が表示され、pwdck -n ALL 起動確認 authorizations 0415 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0415A が画面・出力に表示されること
② ステップ2 の AIX0415B が画面・出力に表示されること
③ ステップ3 の AIX0415C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0412"><h3>pwdck -n ALL 障害切り分け authorizations 0385</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>花冷記録ではAIX 7.3のセキュリティで pwdck -n ALL を確認します。花冷記録のセキュリティでは authorizations と監査設定を採取票へ記録します。花冷記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。花冷記録の注意点として ロール割当と権限文字列の不一致 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、花冷記録を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「pwdck -n ALL 障害切り分け authorizations 0385」を「lsmpio -l hdisk0 バックアウト確認 path status 0386」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はデバイス管理でlsmpio -l hdisk0を用い・path status とデバイス一覧を確認する。</li><li>B. 保守作業で参照する機能はSRCとログでerrpt -aを用い・IDENTIFIER とエラーログ一覧を確認する。</li><li>C. 保守作業で参照する機能はJFS2でlogformを用い・mountguard とファイルシステム属性を確認する。</li><li>D. 保守作業で参照する機能はセキュリティでpwdck -n ALLを用い・authorizations と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでpwdck -n ALLを用い、authorizations」に対応する項目は障害切り分け authorizati（障害・pwdc）です。障害切に関するセキュリティの仕様は「セキュリティでpwdck -n ALLを用い」で、確認対象はpw・障害切です。バック・lsmpのA:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（バッ・lsmp）です。状態・errpのB:は「SRCとログでerrpt -aを用い、IDENTIFIER」を述べ、対象は状態確認 IDENTIFIER（状態・errp）です。監査・logfのC:は「JFS2でlogformを用い、mountguard」を述べ、対象は監査記録 mountguard（監査・logf）です。「pwdck -n ALL」は「セキュリティでpwdck -n ALLを用い」を指し、障害切り分け authorizatiではpw・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>pwdck -n ALL 障害切り分け authorizations 0385</strong></p><p>検証目的: セキュリティのpwdck -n ALL 障害切り分け authorizations 0385について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ障害切り分け025-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; pwdck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0385A
画面・出力には AIX0385A が表示され、pwdck -n ALL 障害切り分け authorizations 0385 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0385B
画面・出力には AIX0385B が表示され、pwdck -n ALL 障害切り分け authorizations 0385 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0385C
画面・出力には AIX0385C が表示され、pwdck -n ALL 障害切り分け authorizations 0385 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0385A が画面・出力に表示されること
② ステップ2 の AIX0385B が画面・出力に表示されること
③ ステップ3 の AIX0385C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0413"><h3>pwdck -n ALL 障害切り分け authorizations 0445</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>深雪整理ではAIX 7.3のセキュリティで pwdck -n ALL を確認します。深雪整理のセキュリティでは authorizations と監査設定を採取票へ記録します。深雪整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。深雪整理の注意点として ロール割当と権限文字列の不一致 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、深雪整理を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> pwdck -n ALL 障害切り分け authorizations 0445を保守記録に説明する必要があります。lsmpio -l hdisk0 バックアウト確認 path status 0446と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はセキュリティでpwdck -n ALLを用い・authorizations と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はデバイス管理でlsmpio -l hdisk0を用い・path status とデバイス一覧を確認する。</li><li>C. 保守作業で参照する機能はSRCとログでerrclearを用い・TIMESTAMP とエラーログ一覧を確認する。</li><li>D. 保守作業で参照する機能はJFS2でdefragfsを用い・lff とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでpwdck -n ALLを用い、authorizations」に対応する項目は障害切り分け authorizati（障害・pwdc）です。障害切に関するセキュリティの仕様は「セキュリティでpwdck -n ALLを用い」で、確認対象はpw・障害切です。バック・lsmpのB:は「デバイス管理でlsmpio -l hdisk0を用い、path」を述べ、対象はpath status（バッ・lsmp）です。構成・errcのC:は「SRCとログでerrclearを用い、TIMESTAMP」を述べ、対象は構成照合 TIMESTAMP（構成・errc）です。運用引・defrのD:は「JFS2でdefragfsを用い、lff」を述べ、対象は運用引継ぎ lff（運用・defr）です。「pwdck -n ALL」は「セキュリティでpwdck -n ALLを用い」を指し、障害切り分け authorizatiではpw・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>pwdck -n ALL 障害切り分け authorizations 0445</strong></p><p>検証目的: セキュリティのpwdck -n ALL 障害切り分け authorizations 0445について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ障害切り分け085-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; pwdck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0445A
画面・出力には AIX0445A が表示され、pwdck -n ALL 障害切り分け authorizations 0445 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0445B
画面・出力には AIX0445B が表示され、pwdck -n ALL 障害切り分け authorizations 0445 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0445C
画面・出力には AIX0445C が表示され、pwdck -n ALL 障害切り分け authorizations 0445 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0445A が画面・出力に表示されること
② ステップ2 の AIX0445B が画面・出力に表示されること
③ ステップ3 の AIX0445C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0414"><h3>rbacqry -u user1 -T バックアウト確認 roles 0113</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>朝霧点検ではAIX 7.3のセキュリティで rbacqry -u user1 -T を確認します。朝霧点検のセキュリティでは roles と監査設定を復旧票へ残します。朝霧点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。朝霧点検の注意点として ロール割当と権限文字列の不一致 を避けるため lsuser user1 も併記します。権限管理の作業票として、朝霧点検を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「rbacqry -u user1 -T バックアウト確認 roles 0113」を「odmget CuDv 監査記録 PVID 0114」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はデバイス管理でodmget CuDvを用い・PVID とデバイス一覧を確認する。</li><li>B. 仕様上の役割はSRCとログでrefresh -s syslogdを用い・IDENTIFIER とエラーログ一覧を確認する。</li><li>C. 仕様上の役割はデバイス管理でchdev -l hdisk0を用い・PVID とデバイス一覧を確認する。</li><li>D. 仕様上の役割はセキュリティでrbacqry -u user1 -Tを用い・roles と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「セキュリティでrbacqry -u user1 -Tを用い、roles」に対応する項目はバックアウト確認 roles（バッ・rbac）です。バックに関するセキュリティの仕様は「セキュリティでrbacqry -u user1 -Tを用い」で、確認対象はrb・バックです。監査・odmgのA:は「デバイス管理でodmget CuDvを用い、PVID」を述べ、対象は監査記録 PVID（監査・odmg）です。変更前・refrのB:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は変更前確認 IDENTIFIER（変更・refr）です。状態・chdeのC:は「デバイス管理でchdev -l hdisk0を用い、PVID」を述べ、対象は状態確認 PVID（状態・chde）です。「rbacqry -u user1 -T」は「セキュリティでrbacqry -u user1 -Tを用い」を指し、バックアウト確認 rolesではrb・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rbacqry -u user1 -T バックアウト確認 roles 0113</strong></p><p>検証目的: セキュリティのrbacqry -u user1 -T バックアウト確認 roles 0113について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティバックアウト確認113-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rbacqry -u user1 -T
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0113A
画面・出力には AIX0113A が表示され、rbacqry -u user1 -T バックアウト確認 roles 0113 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0113B
画面・出力には AIX0113B が表示され、rbacqry -u user1 -T バックアウト確認 roles 0113 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0113C
画面・出力には AIX0113C が表示され、rbacqry -u user1 -T バックアウト確認 roles 0113 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0113A が画面・出力に表示されること
② ステップ2 の AIX0113B が画面・出力に表示されること
③ ステップ3 の AIX0113C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0415"><h3>rbacqry -u user1 -T バックアウト確認 user attributes 0589</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>梅雨晴点検ではAIX 7.3のセキュリティで rbacqry -u user1 -T を確認します。梅雨晴点検のセキュリティでは user attributes と監査設定を採取票へ記録します。梅雨晴点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。梅雨晴点検の注意点として ロール割当と権限文字列の不一致 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、梅雨晴点検を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rbacqry -u user1 -T バックアウト確認 user attributes 0589を保守記録に説明する必要があります。odmget CuDv 監査記録 microcode level 0590と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はデバイス管理でodmget CuDvを用い・microcode level とデバイス一覧を確認する。</li><li>B. 保守作業で参照する機能はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>C. 保守作業で参照する機能はセキュリティでrbacqry -u user1 -Tを用い・user attributesである。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はJFS2でfsckを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「セキュリティでrbacqry -u user1 -Tを用い、user」に対応する項目はuser attributes（バッ・rbac）です。バックに関するセキュリティの仕様は「セキュリティでrbacqry -u user1 -Tを用い」で、確認対象はrb・バックです。監査・odmgのA:は「デバイス管理でodmget CuDvを用い、microcode」を述べ、対象はmicrocode level（監査・odmg）です。属性・ログ・errpのB:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は属性照合 ログ採取（属性・errp）です。容量・ファ・fsckのD:は「JFS2でfsckを用い、ファイルシステム使用率」を述べ、対象は容量確認 ファイルシステム使用率（容量・fsck）です。「rbacqry -u user1 -T」は「セキュリティでrbacqry -u user1 -Tを用い」を指し、user attributesではrb・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rbacqry -u user1 -T バックアウト確認 user attributes 0589</strong></p><p>検証目的: セキュリティのrbacqry -u user1 -T バックアウト確認 user attributes 0589について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティバックアウト確認109-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rbacqry -u user1 -T
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0589A
画面・出力には AIX0589A が表示され、rbacqry -u user1 -T バックアウト確認 user attributes 0589 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0589B
画面・出力には AIX0589B が表示され、rbacqry -u user1 -T バックアウト確認 user attributes 0589 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0589C
画面・出力には AIX0589C が表示され、rbacqry -u user1 -T バックアウト確認 user attributes 0589 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0589A が画面・出力に表示されること
② ステップ2 の AIX0589B が画面・出力に表示されること
③ ステップ3 の AIX0589C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0416"><h3>rbacqry -u user1 -T 変更後確認 audit class 0241</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>白露監査ではAIX 7.3のセキュリティで rbacqry -u user1 -T を確認します。白露監査のセキュリティでは audit class と監査設定を採取票へ記録します。白露監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。白露監査の注意点として ロール割当と権限文字列の不一致 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、白露監査を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「rbacqry -u user1 -T 変更後確認 audit class 0241」を「odmget CuDv 障害切り分け PVID 0242」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はデバイス管理でodmget CuDvを用い・PVID とデバイス一覧を確認する。</li><li>B. 保守作業で参照する機能はセキュリティでrbacqry -u user1 -Tを用い・audit class と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はSRCとログでstartsrc -s syslogdを用い・Status とエラーログ一覧を確認する。startsrc -s syslogd 属性確認 Status 0547固有の属性も確認対象に含める。</li><li>D. 保守作業で参照する機能はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「セキュリティでrbacqry -u user1 -Tを用い、audit class」に対応する項目はaudit class（変更・rbac）です。変更後に関するセキュリティの仕様は「セキュリティでrbacqry -u user1 -Tを用い」で、確認対象はrb・変更後です。障害切・odmgのA:は「デバイス管理でodmget CuDvを用い、PVID」を述べ、対象は障害切り分け PVID（障害・odmg）です。属性・starのC:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は属性確認 Status（属性・star）です。変更前・lspsのD:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は変更前確認 停止確認（変更・lsps）です。「rbacqry -u user1 -T」は「セキュリティでrbacqry -u user1 -Tを用い」を指し、audit classではrb・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rbacqry -u user1 -T 変更後確認 audit class 0241</strong></p><p>検証目的: セキュリティのrbacqry -u user1 -T 変更後確認 audit class 0241について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更後確認001-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rbacqry -u user1 -T
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0241A
画面・出力には AIX0241A が表示され、rbacqry -u user1 -T 変更後確認 audit class 0241 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0241B
画面・出力には AIX0241B が表示され、rbacqry -u user1 -T 変更後確認 audit class 0241 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0241C
画面・出力には AIX0241C が表示され、rbacqry -u user1 -T 変更後確認 audit class 0241 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0241A が画面・出力に表示されること
② ステップ2 の AIX0241B が画面・出力に表示されること
③ ステップ3 の AIX0241C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0417"><h3>rbacqry -u user1 -T 属性確認 roles 0083</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>秋声点検ではAIX 7.3のセキュリティで rbacqry -u user1 -T を確認します。秋声点検のセキュリティでは roles とロール一覧を照合票へ整理します。秋声点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。秋声点検の注意点として ユーザー属性変更の根拠不足 を避けるため lsuser user1 も併記します。権限管理の作業票として、秋声点検を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rbacqry -u user1 -T 属性確認 roles 0083について構成や状態を確認します。odmget CuDv 状態確認 Available 0084ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はデバイス管理でodmget CuDvを用い・Available と構成マネージャー結果を確認する。</li><li>B. 一次資料が示す主目的はSRCとログでrefresh -s syslogdを用い・Subsystemである。</li><li>C. 一次資料が示す主目的はデバイス管理でlsattr -El hdisk0を用い・microcode levelである。</li><li>D. 一次資料が示す主目的はセキュリティでrbacqry -u user1 -Tを用い・roles とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでrbacqry -u user1 -Tを用い、roles」に対応する項目は属性確認 roles（属性・rbac）です。属性に関するセキュリティの仕様は「セキュリティでrbacqry -u user1 -Tを用い」で、確認対象はrb・属性です。状態・odmgのA:は「デバイス管理でodmget CuDvを用い、Available」を述べ、対象は状態確認 Available（状態・odmg）です。容量・refrのB:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は容量確認 Subsystem（容量・refr）です。バック・lsatのC:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象はmicrocode level（バッ・lsat）です。「rbacqry -u user1 -T」は「セキュリティでrbacqry -u user1 -Tを用い」を指し、属性確認 rolesではrb・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rbacqry -u user1 -T 属性確認 roles 0083</strong></p><p>検証目的: セキュリティのrbacqry -u user1 -T 属性確認 roles 0083について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認083-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rbacqry -u user1 -T
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0083A
画面・出力には AIX0083A が表示され、rbacqry -u user1 -T 属性確認 roles 0083 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0083B
画面・出力には AIX0083B が表示され、rbacqry -u user1 -T 属性確認 roles 0083 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0083C
画面・出力には AIX0083C が表示され、rbacqry -u user1 -T 属性確認 roles 0083 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0083A が画面・出力に表示されること
② ステップ2 の AIX0083B が画面・出力に表示されること
③ ステップ3 の AIX0083C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0418"><h3>rbacqry -u user1 -T 属性確認 user attributes 0559</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>秋桜照合ではAIX 7.3のセキュリティで rbacqry -u user1 -T を確認します。秋桜照合のセキュリティでは user attributes とロール一覧を点検票へ整理します。秋桜照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。秋桜照合の注意点として ユーザー属性変更の根拠不足 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、秋桜照合を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rbacqry -u user1 -T 属性確認 user attributes 0559の設定や表示を読む前に役割を確認します。odmget CuDv 状態確認 attribute 0560ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはデバイス管理でodmget CuDvを用い・attribute と構成マネージャー結果を確認する。</li><li>B. 対象資源に対する働きはセキュリティでrbacqry -u user1 -Tを用い・user attributesである。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>D. 対象資源に対する働きはJFS2でfsckを用い・isnapshot とログデバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでrbacqry -u user1 -Tを用い、user」に対応する項目はuser attributes（属性・rbac）です。属性に関するセキュリティの仕様は「セキュリティでrbacqry -u user1 -Tを用い」で、確認対象はrb・属性です。状態・odmgのA:は「デバイス管理でodmget CuDvを用い、attribute」を述べ、対象は状態確認 attribute（状態・odmg）です。状態・表形・errpのC:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は状態判定 表形式（状態・errp）です。変更前・fsckのD:は「JFS2でfsckを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・fsck）です。「rbacqry -u user1 -T」は「セキュリティでrbacqry -u user1 -Tを用い」を指し、user attributesではrb・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rbacqry -u user1 -T 属性確認 user attributes 0559</strong></p><p>検証目的: セキュリティのrbacqry -u user1 -T 属性確認 user attributes 0559について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認079-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rbacqry -u user1 -T
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0559A
画面・出力には AIX0559A が表示され、rbacqry -u user1 -T 属性確認 user attributes 0559 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0559B
画面・出力には AIX0559B が表示され、rbacqry -u user1 -T 属性確認 user attributes 0559 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0559C
画面・出力には AIX0559C が表示され、rbacqry -u user1 -T 属性確認 user attributes 0559 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0559A が画面・出力に表示されること
② ステップ2 の AIX0559B が画面・出力に表示されること
③ ステップ3 の AIX0559C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0419"><h3>rbacqry -u user1 -T 構成照合 audit class 0370</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>桜雲記録ではAIX 7.3のセキュリティで rbacqry -u user1 -T を確認します。桜雲記録のセキュリティでは audit class とRBAC属性を保守票へ記録します。桜雲記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。桜雲記録の注意点として 監査データ未取得でのroleqry実行 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、桜雲記録を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rbacqry -u user1 -T 構成照合 audit class 0370の役割を調べています。odmget CuDv 変更前確認 PVID 0371の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はセキュリティでrbacqry -u user1 -Tを用い・audit class とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はデバイス管理でodmget CuDvを用い・PVID とODM属性を確認する。</li><li>C. 表示や設定で扱う内容はSRCとログでstartsrc -s syslogdを用い・PID とsyslog設定変換を確認する。startsrc -s syslogd 性能確認 PID 0676固有の属性も確認対象に含める。</li><li>D. 表示や設定で扱う内容はJFS2でmount -o remountを用い・isnapshot と内部スナップショットを確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「セキュリティでrbacqry -u user1 -Tを用い、audit class」に対応する項目はaudit class（構成・rbac）です。構成に関するセキュリティの仕様は「セキュリティでrbacqry -u user1 -Tを用い」で、確認対象はrb・構成です。変更前・odmgのB:は「デバイス管理でodmget CuDvを用い、PVID」を述べ、対象は変更前確認 PVID（変更・odmg）です。性能・starのC:は「SRCとログでstartsrc -s syslogdを用い、PID」を述べ、対象は性能確認 PID（性能・star）です。変更後・mounのD:は「JFS2でmount -o remountを用い」を述べ、対象は変更後確認 isnapshot（変更・moun）です。「rbacqry -u user1 -T」は「セキュリティでrbacqry -u user1 -Tを用い」を指し、audit classではrb・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rbacqry -u user1 -T 構成照合 audit class 0370</strong></p><p>検証目的: セキュリティのrbacqry -u user1 -T 構成照合 audit class 0370について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ構成照合010-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rbacqry -u user1 -T
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0370A
画面・出力には AIX0370A が表示され、rbacqry -u user1 -T 構成照合 audit class 0370 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0370B
画面・出力には AIX0370B が表示され、rbacqry -u user1 -T 構成照合 audit class 0370 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0370C
画面・出力には AIX0370C が表示され、rbacqry -u user1 -T 構成照合 audit class 0370 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0370A が画面・出力に表示されること
② ステップ2 の AIX0370B が画面・出力に表示されること
③ ステップ3 の AIX0370C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0420"><h3>rbacqry -u user1 -T 構成照合 audit class 0430</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>早苗評価ではAIX 7.3のセキュリティで rbacqry -u user1 -T を確認します。早苗評価のセキュリティでは audit class とRBAC属性を保守票へ記録します。早苗評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。早苗評価の注意点として 監査データ未取得でのroleqry実行 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、早苗評価を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rbacqry -u user1 -T 構成照合 audit class 0430に関する障害切り分けの前提を確認しています。odmget CuDv 変更前確認 PVID 0431の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はセキュリティでrbacqry -u user1 -Tを用い・audit class とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はデバイス管理でodmget CuDvを用い・PVID とODM属性を確認する。</li><li>C. 表示や設定で扱う内容はSRCとログでrefresh -s syslogdを用い・Status とsyslog設定変換を確認する。refresh -s syslogd 起動確認 Status 0736固有の属性も確認対象に含める。</li><li>D. 表示や設定で扱う内容はJFS2でfsckを用い・mountguard と内部スナップショットを確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでrbacqry -u user1 -Tを用い、audit class」に対応する項目はaudit class（構成・rbac）です。構成に関するセキュリティの仕様は「セキュリティでrbacqry -u user1 -Tを用い」で、確認対象はrb・構成です。変更前・odmgのB:は「デバイス管理でodmget CuDvを用い、PVID」を述べ、対象は変更前確認 PVID（変更・odmg）です。起動・refrのC:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は起動確認 Status（起動・refr）です。障害切・fsckのD:は「JFS2でfsckを用い、mountguard」を述べ、対象は障害切り分け mountguard（障害・fsck）です。「rbacqry -u user1 -T」は「セキュリティでrbacqry -u user1 -Tを用い」を指し、audit classではrb・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rbacqry -u user1 -T 構成照合 audit class 0430</strong></p><p>検証目的: セキュリティのrbacqry -u user1 -T 構成照合 audit class 0430について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ構成照合070-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rbacqry -u user1 -T
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0430A
画面・出力には AIX0430A が表示され、rbacqry -u user1 -T 構成照合 audit class 0430 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0430B
画面・出力には AIX0430B が表示され、rbacqry -u user1 -T 構成照合 audit class 0430 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0430C
画面・出力には AIX0430C が表示され、rbacqry -u user1 -T 構成照合 audit class 0430 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0430A が画面・出力に表示されること
② ステップ2 の AIX0430B が画面・出力に表示されること
③ ステップ3 の AIX0430C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0421"><h3>rbacqry -u user1 -T 運用引継ぎ audit class 0400</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>青葉評価ではAIX 7.3のセキュリティで rbacqry -u user1 -T を確認します。青葉評価のセキュリティでは audit class とユーザー属性を監査票へ転記します。青葉評価は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。青葉評価の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、青葉評価を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rbacqry -u user1 -T 運用引継ぎ audit class 0400を同一分類のodmget CuDv 容量確認 Available 0401と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はセキュリティでrbacqry -u user1 -Tを用い・audit class とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はデバイス管理でodmget CuDvを用い・Available と診断対象表示を確認する。</li><li>C. 管理対象との関係を表す説明はSRCとログでstartsrc -s syslogdを用い・TIMESTAMPである。startsrc -s syslogd 変更後確認 TIMESTAMP固有の属性も確認対象に含める。</li><li>D. 管理対象との関係を表す説明はJFS2でmount -o remountを用い・ファイルシステム使用率 とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでrbacqry -u user1 -Tを用い、audit class」に対応する項目はaudit class（運用・rbac）です。運用引に関するセキュリティの仕様は「セキュリティでrbacqry -u user1 -Tを用い」で、確認対象はrb・運用引です。容量・odmgのB:は「デバイス管理でodmget CuDvを用い、Available」を述べ、対象は容量確認 Available（容量・odmg）です。変更後・starのC:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は変更後確認 TIMESTAMP（変更・star）です。性能・ファ・mounのD:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 ファイルシステム使用率（性能・moun）です。「rbacqry -u user1 -T」は「セキュリティでrbacqry -u user1 -Tを用い」を指し、audit classではrb・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rbacqry -u user1 -T 運用引継ぎ audit class 0400</strong></p><p>検証目的: セキュリティのrbacqry -u user1 -T 運用引継ぎ audit class 0400について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ運用引継ぎ040-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rbacqry -u user1 -T
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0400A
画面・出力には AIX0400A が表示され、rbacqry -u user1 -T 運用引継ぎ audit class 0400 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0400B
画面・出力には AIX0400B が表示され、rbacqry -u user1 -T 運用引継ぎ audit class 0400 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0400C
画面・出力には AIX0400C が表示され、rbacqry -u user1 -T 運用引継ぎ audit class 0400 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0400A が画面・出力に表示されること
② ステップ2 の AIX0400B が画面・出力に表示されること
③ ステップ3 の AIX0400C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0422"><h3>rbacqry -u user1 -T 運用引継ぎ audit class 0460</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>薄明整理ではAIX 7.3のセキュリティで rbacqry -u user1 -T を確認します。薄明整理のセキュリティでは audit class とユーザー属性を監査票へ転記します。薄明整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。薄明整理の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、薄明整理を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rbacqry -u user1 -T 運用引継ぎ audit class 0460の技術的な意味を資料で確認するとき、odmget CuDv 容量確認 Available 0461との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はセキュリティでrbacqry -u user1 -Tを用い・audit class とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はデバイス管理でodmget CuDvを用い・Available と診断対象表示を確認する。</li><li>C. 管理対象との関係を表す説明はSRCとログでrefresh -s syslogdを用い・syslog.confである。</li><li>D. 管理対象との関係を表す説明はLVMでmklvを用い・PVID とミラーコピー状態を確認する。mklv 起動確認 PVID 0153固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「セキュリティでrbacqry -u user1 -Tを用い、audit class」に対応する項目はaudit class（運用・rbac）です。運用引に関するセキュリティの仕様は「セキュリティでrbacqry -u user1 -Tを用い」で、確認対象はrb・運用引です。容量・odmgのB:は「デバイス管理でodmget CuDvを用い、Available」を述べ、対象は容量確認 Available（容量・odmg）です。障害切・refrのC:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は障害切り分け syslog.conf（障害・refr）です。起動・mklvのD:は「LVMでmklvを用い、PVID とミラーコピー状態を確認する」を述べ、対象は起動確認 PVID（起動・mklv）です。「rbacqry -u user1 -T」は「セキュリティでrbacqry -u user1 -Tを用い」を指し、audit classではrb・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rbacqry -u user1 -T 運用引継ぎ audit class 0460</strong></p><p>検証目的: セキュリティのrbacqry -u user1 -T 運用引継ぎ audit class 0460について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ運用引継ぎ100-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rbacqry -u user1 -T
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0460A
画面・出力には AIX0460A が表示され、rbacqry -u user1 -T 運用引継ぎ audit class 0460 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0460B
画面・出力には AIX0460B が表示され、rbacqry -u user1 -T 運用引継ぎ audit class 0460 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0460C
画面・出力には AIX0460C が表示され、rbacqry -u user1 -T 運用引継ぎ audit class 0460 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0460A が画面・出力に表示されること
② ステップ2 の AIX0460B が画面・出力に表示されること
③ ステップ3 の AIX0460C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0423"><h3>rolelist -u user1 変更前確認 roles 0181</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>群青判定ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。群青判定のセキュリティでは roles と監査設定を採取票へ記録します。群青判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。群青判定の注意点として ロール割当と権限文字列の不一致 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、群青判定を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 変更前確認 roles 0181を保守記録に説明する必要があります。cfgmgr 変更後確認 attribute 0182と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はデバイス管理でcfgmgrを用い・attribute とデバイス一覧を確認する。</li><li>B. 保守作業で参照する機能はSRCとログでstartsrc -s syslogdを用い・Status とエラーログ一覧を確認する。</li><li>C. 保守作業で参照する機能はセキュリティでrolelist -u user1を用い・roles と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はデバイス管理でlsdev -Cc diskを用い・location code とデバイス一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでrolelist -u user1を用い、roles」に対応する項目は変更前確認 roles（変更・role）です。変更前に関するセキュリティの仕様は「セキュリティでrolelist -u user1を用い、roles」で、確認対象はro・変更前です。変更後・cfgmのA:は「デバイス管理でcfgmgrを用い、attribute」を述べ、対象は変更後確認 attribute（変更・cfgm）です。属性・starのB:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は属性確認 Status（属性・star）です。容量・lsdeのD:は「デバイス管理でlsdev -Cc diskを用い、location」を述べ、対象はlocation code（容量・lsde）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い、roles」を指し、変更前確認 rolesではro・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 変更前確認 roles 0181</strong></p><p>検証目的: セキュリティのrolelist -u user1 変更前確認 roles 0181について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更前確認061-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0181A
画面・出力には AIX0181A が表示され、rolelist -u user1 変更前確認 roles 0181 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0181B
画面・出力には AIX0181B が表示され、rolelist -u user1 変更前確認 roles 0181 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0181C
画面・出力には AIX0181C が表示され、rolelist -u user1 変更前確認 roles 0181 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0181A が画面・出力に表示されること
② ステップ2 の AIX0181B が画面・出力に表示されること
③ ステップ3 の AIX0181C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0424"><h3>rolelist -u user1 変更前確認 user attributes 0657</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>初霜判定ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。初霜判定のセキュリティでは user attributes と監査設定を判定票へ残します。初霜判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。初霜判定の注意点として ロール割当と権限文字列の不一致 を避けるため lsrole ALL も併記します。権限管理の作業票として、初霜判定を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「rolelist -u user1 変更前確認 user attributes 0657」を「cfgmgr 変更後確認 path status 0658」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はデバイス管理でcfgmgrを用い・path status とデバイス一覧を確認する。</li><li>B. 運用時に利用する技術的役割はネットワークでentstat -d ent0を用い・Gateway とEthernet統計を確認する。</li><li>C. 運用時に利用する技術的役割はセキュリティでrolelist -u user1を用い・user attributes と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はJFS2でlsfs -qを用い・mountguard とファイルシステム属性を確認する。lsfs -q 障害切り分け mountguard 0350固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでrolelist -u user1を用い、user」に対応する項目はuser attributes（変更・role）です。変更前に関するセキュリティの仕様は「セキュリティでrolelist -u user1を用い、user」で、確認対象はro・変更前です。変更後・cfgmのA:は「デバイス管理でcfgmgrを用い、path status」を述べ、対象はpath status（変更・cfgm）です。運用引・entsのB:は「ネットワークでentstat -d ent0を用い、Gateway」を述べ、対象は運用引継ぎ Gateway（運用・ents）です。障害切・lsfsのD:は「JFS2でlsfs -qを用い、mountguard」を述べ、対象は障害切り分け mountguard（障害・lsfs）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い、user」を指し、user attributesではro・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 変更前確認 user attributes 0657</strong></p><p>検証目的: セキュリティのrolelist -u user1 変更前確認 user attributes 0657について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更前確認057-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0657A
画面・出力には AIX0657A が表示され、rolelist -u user1 変更前確認 user attributes 0657 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0657B
画面・出力には AIX0657B が表示され、rolelist -u user1 変更前確認 user attributes 0657 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0657C
画面・出力には AIX0657C が表示され、rolelist -u user1 変更前確認 user attributes 0657 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0657A が画面・出力に表示されること
② ステップ2 の AIX0657B が画面・出力に表示されること
③ ステップ3 の AIX0657C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0425"><h3>rolelist -u user1 変更前確認 user attributes 0717</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>冬晴保守ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。冬晴保守のセキュリティでは user attributes と監査設定を判定票へ残します。冬晴保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。冬晴保守の注意点として ロール割当と権限文字列の不一致 を避けるため lsrole ALL も併記します。権限管理の作業票として、冬晴保守を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 変更前確認 user attributes 0717を保守記録に説明する必要があります。cfgmgr 変更後確認 path status 0718と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はセキュリティでrolelist -u user1を用い・user attributes と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はデバイス管理でcfgmgrを用い・path status とデバイス一覧を確認する。cfgmgr 変更後確認 path status 0718固有の属性も確認対象に含める。</li><li>C. 運用時に利用する技術的役割はネットワークでentstat -d ent0を用い・Gateway とEthernet統計を確認する。</li><li>D. 運用時に利用する技術的役割はJFS2でmount -o remountを用い・lff とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「セキュリティでrolelist -u user1を用い、user」に対応する項目はuser attributes（変更・role）です。変更前に関するセキュリティの仕様は「セキュリティでrolelist -u user1を用い、user」で、確認対象はro・変更前です。変更後・cfgmのB:は「デバイス管理でcfgmgrを用い、path status」を述べ、対象はpath status（変更・cfgm）です。運用引・entsのC:は「ネットワークでentstat -d ent0を用い、Gateway」を述べ、対象は運用引継ぎ Gateway（運用・ents）です。バック・mounのD:は「JFS2でmount -o remountを用い、lff」を述べ、対象はバックアウト確認 lff（バッ・moun）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い、user」を指し、user attributesではro・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 変更前確認 user attributes 0717</strong></p><p>検証目的: セキュリティのrolelist -u user1 変更前確認 user attributes 0717について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更前確認117-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0717A
画面・出力には AIX0717A が表示され、rolelist -u user1 変更前確認 user attributes 0717 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0717B
画面・出力には AIX0717B が表示され、rolelist -u user1 変更前確認 user attributes 0717 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0717C
画面・出力には AIX0717C が表示され、rolelist -u user1 変更前確認 user attributes 0717 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0717A が画面・出力に表示されること
② ステップ2 の AIX0717B が画面・出力に表示されること
③ ステップ3 の AIX0717C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0426"><h3>rolelist -u user1 容量確認 roles 0151</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>遠雷採取ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。遠雷採取のセキュリティでは roles とロール一覧を点検票へ整理します。遠雷採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。遠雷採取の注意点として ユーザー属性変更の根拠不足 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、遠雷採取を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 容量確認 roles 0151の設定や表示を読む前に役割を確認します。cfgmgr 性能確認 microcode level 0152ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはデバイス管理でcfgmgrを用い・microcode level と構成マネージャー結果を確認する。</li><li>B. 対象資源に対する働きはセキュリティでrolelist -u user1を用い・roles とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはSRCとログでlssrc -s syslogdを用い・TIMESTAMP とinetdデバッグ出力を確認する。</li><li>D. 対象資源に対する働きはデバイス管理でlsdev -Cc diskを用い・path status と構成マネージャー結果を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでrolelist -u user1を用い、roles」に対応する項目は容量確認 roles（容量・role）です。容量に関するセキュリティの仕様は「セキュリティでrolelist -u user1を用い、roles」で、確認対象はro・容量です。性能・cfgmのA:は「デバイス管理でcfgmgrを用い、microcode level」を述べ、対象はmicrocode level（性能・cfgm）です。障害切・lssrのC:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は障害切り分け TIMESTAMP（障害・lssr）です。変更前・lsdeのD:は「デバイス管理でlsdev -Cc diskを用い、path」を述べ、対象はpath status（変更・lsde）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い、roles」を指し、容量確認 rolesではro・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 容量確認 roles 0151</strong></p><p>検証目的: セキュリティのrolelist -u user1 容量確認 roles 0151について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ容量確認031-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0151A
画面・出力には AIX0151A が表示され、rolelist -u user1 容量確認 roles 0151 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0151B
画面・出力には AIX0151B が表示され、rolelist -u user1 容量確認 roles 0151 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0151C
画面・出力には AIX0151C が表示され、rolelist -u user1 容量確認 roles 0151 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0151A が画面・出力に表示されること
② ステップ2 の AIX0151B が画面・出力に表示されること
③ ステップ3 の AIX0151C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0427"><h3>rolelist -u user1 容量確認 roles 0211</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>松風保守ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。松風保守のセキュリティでは roles とロール一覧を点検票へ整理します。松風保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。松風保守の注意点として ユーザー属性変更の根拠不足 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、松風保守を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 容量確認 roles 0211について構成や状態を確認します。cfgmgr 性能確認 microcode level 0212ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはセキュリティでrolelist -u user1を用い・roles とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはデバイス管理でcfgmgrを用い・microcode level と構成マネージャー結果を確認する。</li><li>C. 対象資源に対する働きはSRCとログでstartsrc -s syslogdを用い・syslog.confである。</li><li>D. 対象資源に対する働きはデバイス管理でlsdev -Cc diskを用い・path status と構成マネージャー結果を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでrolelist -u user1を用い、roles」に対応する項目は容量確認 roles（容量・role）です。容量に関するセキュリティの仕様は「セキュリティでrolelist -u user1を用い、roles」で、確認対象はro・容量です。性能・cfgmのB:は「デバイス管理でcfgmgrを用い、microcode level」を述べ、対象はmicrocode level（性能・cfgm）です。バック・starのC:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象はバックアウト確認 syslog.co（バッ・star）です。変更前・lsdeのD:は「デバイス管理でlsdev -Cc diskを用い、path」を述べ、対象はpath status（変更・lsde）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い、roles」を指し、容量確認 rolesではro・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 容量確認 roles 0211</strong></p><p>検証目的: セキュリティのrolelist -u user1 容量確認 roles 0211について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ容量確認091-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0211A
画面・出力には AIX0211A が表示され、rolelist -u user1 容量確認 roles 0211 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0211B
画面・出力には AIX0211B が表示され、rolelist -u user1 容量確認 roles 0211 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0211C
画面・出力には AIX0211C が表示され、rolelist -u user1 容量確認 roles 0211 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0211A が画面・出力に表示されること
② ステップ2 の AIX0211B が画面・出力に表示されること
③ ステップ3 の AIX0211C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0428"><h3>rolelist -u user1 容量確認 user attributes 0627</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>風花採取ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。風花採取のセキュリティでは user attributes とロール一覧を作業票へ保管します。風花採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。風花採取の注意点として ユーザー属性変更の根拠不足 を避けるため lsrole ALL も併記します。権限管理の作業票として、風花採取を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 容量確認 user attributes 0627について構成や状態を確認します。cfgmgr 性能確認 location code 0628ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはデバイス管理でcfgmgrを用い・location code と構成マネージャー結果を確認する。</li><li>B. 状態を読み取るための働きはセキュリティでrolelist -u user1を用い・user attributesである。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはネットワークでentstat -d ent0を用い・Media Speed Runningである。</li><li>D. 状態を読み取るための働きはJFS2でlsfs -qを用い・log=INLINE とログデバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでrolelist -u user1を用い、user」に対応する項目はuser attributes（容量・role）です。容量に関するセキュリティの仕様は「セキュリティでrolelist -u user1を用い、user」で、確認対象はro・容量です。性能・cfgmのA:は「デバイス管理でcfgmgrを用い、location code」を述べ、対象はlocation code（性能・cfgm）です。構成・entsのC:は「ネットワークでentstat -d ent0を用い、Media」を述べ、対象はSpeed Running（構成・ents）です。起動・lsfsのD:は「JFS2でlsfs -qを用い、log=INLINE」を述べ、対象は起動確認 log=INLINE（起動・lsfs）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い、user」を指し、user attributesではro・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 容量確認 user attributes 0627</strong></p><p>検証目的: セキュリティのrolelist -u user1 容量確認 user attributes 0627について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ容量確認027-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0627A
画面・出力には AIX0627A が表示され、rolelist -u user1 容量確認 user attributes 0627 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0627B
画面・出力には AIX0627B が表示され、rolelist -u user1 容量確認 user attributes 0627 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0627C
画面・出力には AIX0627C が表示され、rolelist -u user1 容量確認 user attributes 0627 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0627A が画面・出力に表示されること
② ステップ2 の AIX0627B が画面・出力に表示されること
③ ステップ3 の AIX0627C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0429"><h3>rolelist -u user1 容量確認 user attributes 0687</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>夕凪保守ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。夕凪保守のセキュリティでは user attributes とロール一覧を作業票へ保管します。夕凪保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。夕凪保守の注意点として ユーザー属性変更の根拠不足 を避けるため lsrole ALL も併記します。権限管理の作業票として、夕凪保守を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 容量確認 user attributes 0687の設定や表示を読む前に役割を確認します。cfgmgr 性能確認 location code 0688ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはデバイス管理でcfgmgrを用い・location code と構成マネージャー結果を確認する。</li><li>B. 状態を読み取るための働きはネットワークでentstat -d ent0を用い・Media Speed Runningである。</li><li>C. 状態を読み取るための働きはセキュリティでrolelist -u user1を用い・user attributesである。 <span class="kb-ok">✅ 正解</span></li><li>D. 状態を読み取るための働きはJFS2でmount -o remountを用い・agblksize とログデバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでrolelist -u user1を用い、user」に対応する項目はuser attributes（容量・role）です。容量に関するセキュリティの仕様は「セキュリティでrolelist -u user1を用い、user」で、確認対象はro・容量です。性能・cfgmのA:は「デバイス管理でcfgmgrを用い、location code」を述べ、対象はlocation code（性能・cfgm）です。構成・entsのB:は「ネットワークでentstat -d ent0を用い、Media」を述べ、対象はSpeed Running（構成・ents）です。属性・mounのD:は「JFS2でmount -o remountを用い」を述べ、対象は属性確認 agblksize（属性・moun）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い、user」を指し、user attributesではro・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 容量確認 user attributes 0687</strong></p><p>検証目的: セキュリティのrolelist -u user1 容量確認 user attributes 0687について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ容量確認087-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0687A
画面・出力には AIX0687A が表示され、rolelist -u user1 容量確認 user attributes 0687 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0687B
画面・出力には AIX0687B が表示され、rolelist -u user1 容量確認 user attributes 0687 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0687C
画面・出力には AIX0687C が表示され、rolelist -u user1 容量確認 user attributes 0687 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0687A が画面・出力に表示されること
② ステップ2 の AIX0687B が画面・出力に表示されること
③ ステップ3 の AIX0687C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0430"><h3>rolelist -u user1 監査記録 roles 0340</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>薄明変更ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。薄明変更のセキュリティでは roles とユーザー属性を監査票へ転記します。薄明変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。薄明変更の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、薄明変更を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 監査記録 roles 0340の技術的な意味を資料で確認するとき、lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0341との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。</li><li>B. 管理対象との関係を表す説明はSRCとログでstartsrc -s syslogdを用い・TIMESTAMPである。</li><li>C. 管理対象との関係を表す説明はセキュリティでrolelist -u user1を用い・roles とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はJFS2でmount -o remountを用い・ファイルシステム使用率 とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「セキュリティでrolelist -u user1を用い、roles」に対応する項目は監査記録 roles（監査・role）です。監査に関するセキュリティの仕様は「セキュリティでrolelist -u user1を用い、roles」で、確認対象はro・監査です。運用引・lslvのA:は「LVMでlslvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（運用・lslv）です。変更後・starのB:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は変更後確認 TIMESTAMP（変更・star）です。性能・ファ・mounのD:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 ファイルシステム使用率（性能・moun）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い、roles」を指し、監査記録 rolesではro・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 監査記録 roles 0340</strong></p><p>検証目的: セキュリティのrolelist -u user1 監査記録 roles 0340について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ監査記録100-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0340A
画面・出力には AIX0340A が表示され、rolelist -u user1 監査記録 roles 0340 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0340B
画面・出力には AIX0340B が表示され、rolelist -u user1 監査記録 roles 0340 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0340C
画面・出力には AIX0340C が表示され、rolelist -u user1 監査記録 roles 0340 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0340A が画面・出力に表示されること
② ステップ2 の AIX0340B が画面・出力に表示されること
③ ステップ3 の AIX0340C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0431"><h3>rolelist -u user1 監査記録 user attributes 0816</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>若竹変更ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。若竹変更のセキュリティでは user attributes とユーザー属性を同じ証跡に残します。若竹変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若竹変更の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、若竹変更を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 監査記録 user attributes 0816を同一分類のlspv 状態判定 照合単位と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はセキュリティでrolelist -u user1を用い・user attributesである。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。</li><li>C. 構成を確認する際の意味はセキュリティでchuserを用い・user attributes とRBAC属性を確認する。</li><li>D. 構成を確認する際の意味はLVMでchvgを用い・VG STATE とミラーコピー状態を確認する。chvg 性能確認 VG STATE 0545固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査・roleでAの記述「セキュリティでrolelist -u user1を用い、user」に対応する項目はuser attributes（監査・role）です。監査に関するセキュリティの仕様は「セキュリティでrolelist -u user1を用い、user」で、確認対象はro・監査です。状態・照合・lspvのB:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は状態判定 照合単位（状態・lspv）です。容量・chusのC:は「セキュリティでchuserを用い、user attributes」を述べ、対象はuser attributes（容量・chus）です。性能・chvgのD:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（性能・chvg）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い、user」を指し、user attributesではro・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 監査記録 user attributes 0816</strong></p><p>検証目的: セキュリティのrolelist -u user1 監査記録 user attributes 0816について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ監査記録096-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0816A
画面・出力には AIX0816A が表示され、rolelist -u user1 監査記録 user attributes 0816 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0816B
画面・出力には AIX0816B が表示され、rolelist -u user1 監査記録 user attributes 0816 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0816C
画面・出力には AIX0816C が表示され、rolelist -u user1 監査記録 user attributes 0816 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0816A が画面・出力に表示されること
② ステップ2 の AIX0816B が画面・出力に表示されること
③ ステップ3 の AIX0816C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0432"><h3>rolelist -u user1 起動確認 audit class 0498</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>潮騒確認ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。潮騒確認のセキュリティでは audit class とRBAC属性を変更票へ記録します。潮騒確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。潮騒確認の注意点として 監査データ未取得でのroleqry実行 を避けるため lsrole ALL も併記します。権限管理の作業票として、潮騒確認を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 起動確認 audit class 0498の役割を調べています。cfgmgr 属性確認 attribute 0499の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはデバイス管理でcfgmgrを用い・attribute とODM属性を確認する。</li><li>B. 機能の説明としてはセキュリティでrolelist -u user1を用い・audit class とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としてはSRCとログでlssrc -s syslogdを用い・Subsystem とsyslog設定変換を確認する。</li><li>D. 機能の説明としてはJFS2でlsfs -qを用い・agblksize と内部スナップショットを確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「セキュリティでrolelist -u user1を用い、audit class」に対応する項目はaudit class（起動・role）です。起動に関するセキュリティの仕様は「セキュリティでrolelist -u user1を用い、audit」で、確認対象はro・起動です。属性・cfgmのA:は「デバイス管理でcfgmgrを用い、attribute」を述べ、対象は属性確認 attribute（属性・cfgm）です。監査・lssrのC:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は監査記録 Subsystem（監査・lssr）です。状態・lsfsのD:は「JFS2でlsfs -qを用い、agblksize」を述べ、対象は状態確認 agblksize（状態・lsfs）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い、audit」を指し、audit classではro・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 起動確認 audit class 0498</strong></p><p>検証目的: セキュリティのrolelist -u user1 起動確認 audit class 0498について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ起動確認018-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0498A
画面・出力には AIX0498A が表示され、rolelist -u user1 起動確認 audit class 0498 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0498B
画面・出力には AIX0498B が表示され、rolelist -u user1 起動確認 audit class 0498 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0498C
画面・出力には AIX0498C が表示され、rolelist -u user1 起動確認 audit class 0498 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0498A が画面・出力に表示されること
② ステップ2 の AIX0498B が画面・出力に表示されること
③ ステップ3 の AIX0498C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0433"><h3>rolelist -u user1 起動確認 authorizations 0022</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>紅葉確認ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。紅葉確認のセキュリティでは authorizations とRBAC属性を保守票へ記録します。紅葉確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。紅葉確認の注意点として 監査データ未取得でのroleqry実行 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、紅葉確認を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 起動確認 authorizations 0022に関する障害切り分けの前提を確認しています。cfgmgr 属性確認 Available 0023の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はデバイス管理でcfgmgrを用い・Available とODM属性を確認する。</li><li>B. 表示や設定で扱う内容はSRCとログでlssrc -s syslogdを用い・TIMESTAMP とsyslog設定変換を確認する。</li><li>C. 表示や設定で扱う内容はセキュリティでrolelist -u user1を用い・authorizationsである。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はデバイス管理でlsdev -Cc diskを用い・microcode level とODM属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「セキュリティでrolelist -u user1を用い」に対応する項目は起動確認 authorization（起動・role）です。セキュリティの仕様は「セキュリティでrolelist -u user1を用い」で、確認対象はro・起動です。属性・cfgmのA:は「デバイス管理でcfgmgrを用い、Available」を述べ、対象は属性確認 Available（属性・cfgm）です。監査・lssrのB:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は監査記録 TIMESTAMP（監査・lssr）です。障害切・lsdeのD:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象はmicrocode level（障害・lsde）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い」を指し、起動確認 authorizationではro・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 起動確認 authorizations 0022</strong></p><p>検証目的: セキュリティのrolelist -u user1 起動確認 authorizations 0022について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ起動確認022-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0022A
画面・出力には AIX0022A が表示され、rolelist -u user1 起動確認 authorizations 0022 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0022B
画面・出力には AIX0022B が表示され、rolelist -u user1 起動確認 authorizations 0022 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0022C
画面・出力には AIX0022C が表示され、rolelist -u user1 起動確認 authorizations 0022 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0022A が画面・出力に表示されること
② ステップ2 の AIX0022B が画面・出力に表示されること
③ ステップ3 の AIX0022C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0434"><h3>rolelist -u user1 障害切り分け audit class 0528</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>翠風照合ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。翠風照合のセキュリティでは audit class とユーザー属性を同じ証跡に残します。翠風照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。翠風照合の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、翠風照合を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 障害切り分け audit class 0528を同一分類のcfgmgr バックアウト確認 microcode level 0529と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はデバイス管理でcfgmgrを用い・microcode level と診断対象表示を確認する。</li><li>B. 構成を確認する際の意味はSRCとログでlssrc -s syslogdを用い・IDENTIFIERである。</li><li>C. 構成を確認する際の意味はLVMでlsvg -lを用い・STALE PARTITIONS とミラーコピー状態を確認する。lsvg -l 監査記録 STALE PARTITIONS 0221固有の属性も確認対象に含める。</li><li>D. 構成を確認する際の意味はセキュリティでrolelist -u user1を用い・audit class とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでrolelist -u user1を用い、audit class」に対応する項目はaudit class（障害・role）です。障害切に関するセキュリティの仕様は「セキュリティでrolelist -u user1を用い、audit」で、確認対象はro・障害切です。バック・cfgmのA:は「デバイス管理でcfgmgrを用い、microcode level」を述べ、対象はmicrocode level（バッ・cfgm）です。状態・lssrのB:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は状態確認 IDENTIFIER（状態・lssr）です。監査・lsvgのC:は「LVMでlsvg -lを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（監査・lsvg）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い、audit」を指し、audit classではro・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 障害切り分け audit class 0528</strong></p><p>検証目的: セキュリティのrolelist -u user1 障害切り分け audit class 0528について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ障害切り分け048-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0528A
画面・出力には AIX0528A が表示され、rolelist -u user1 障害切り分け audit class 0528 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0528B
画面・出力には AIX0528B が表示され、rolelist -u user1 障害切り分け audit class 0528 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0528C
画面・出力には AIX0528C が表示され、rolelist -u user1 障害切り分け audit class 0528 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0528A が画面・出力に表示されること
② ステップ2 の AIX0528B が画面・出力に表示されること
③ ステップ3 の AIX0528C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0435"><h3>rolelist -u user1 障害切り分け authorizations 0052</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>水音照合ではAIX 7.3のセキュリティで rolelist -u user1 を確認します。水音照合のセキュリティでは authorizations とユーザー属性を監査票へ転記します。水音照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。水音照合の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、水音照合を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> rolelist -u user1 障害切り分け authorizations 0052の技術的な意味を資料で確認するとき、cfgmgr バックアウト確認 PVID 0053との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はセキュリティでrolelist -u user1を用い・authorizationsである。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はデバイス管理でcfgmgrを用い・PVID と診断対象表示を確認する。</li><li>C. 管理対象との関係を表す説明はSRCとログでlssrc -s syslogdを用い・PID とSRCサブシステム表示を確認する。</li><li>D. 管理対象との関係を表す説明はデバイス管理でlsdev -Cc diskを用い・attribute と診断対象表示を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでrolelist -u user1を用い」に対応する項目は障害切り分け authorizati（障害・role）です。セキュリティの仕様は「セキュリティでrolelist -u user1を用い」で、確認対象はro・障害切です。バック・cfgmのB:は「デバイス管理でcfgmgrを用い、PVID と診断対象表示を確認する」を述べ、対象はバックアウト確認 PVID（バッ・cfgm）です。状態・lssrのC:は「SRCとログでlssrc -s syslogdを用い、PID」を述べ、対象は状態確認 PID（状態・lssr）です。起動・lsdeのD:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 attribute（起動・lsde）です。「rolelist -u user1」は「セキュリティでrolelist -u user1を用い」を指し、障害切り分け authorizatiではro・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>rolelist -u user1 障害切り分け authorizations 0052</strong></p><p>検証目的: セキュリティのrolelist -u user1 障害切り分け authorizations 0052について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ障害切り分け052-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0052A
画面・出力には AIX0052A が表示され、rolelist -u user1 障害切り分け authorizations 0052 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0052B
画面・出力には AIX0052B が表示され、rolelist -u user1 障害切り分け authorizations 0052 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0052C
画面・出力には AIX0052C が表示され、rolelist -u user1 障害切り分け authorizations 0052 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0052A が画面・出力に表示されること
② ステップ2 の AIX0052B が画面・出力に表示されること
③ ステップ3 の AIX0052C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0436"><h3>setsecattr バックアウト確認 user attributes 0362</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>春分記録ではAIX 7.3のセキュリティで setsecattr を確認します。春分記録のセキュリティでは user attributes とRBAC属性を確認票へ整理します。春分記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。春分記録の注意点として 監査データ未取得でのroleqry実行 を避けるため lsuser user1 も併記します。権限管理の作業票として、春分記録を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr バックアウト確認 user attributes 0362の役割を調べています。diag -d ent0 監査記録 microcode level 0363の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はデバイス管理でdiag -d ent0を用い・microcode level とODM属性を確認する。</li><li>B. 障害切り分けに用いる役割はセキュリティでsetsecattrを用い・user attributes とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割はSRCとログでsyslog_ssw -cを用い・IDENTIFIER とsyslog設定変換を確認する。</li><li>D. 障害切り分けに用いる役割はJFS2でdf -gを用い・lff と内部スナップショットを確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「セキュリティでsetsecattrを用い、user attributes」に対応する項目はuser attributes（バッ・sets）です。バックに関するセキュリティの仕様は「セキュリティでsetsecattrを用い、user」で、確認対象はse・バックです。監査・diagのA:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（監査・diag）です。構成・syslのC:は「SRCとログでsyslog_ssw -cを用い」を述べ、対象は構成照合 IDENTIFIER（構成・sysl）です。運用引・dfのD:は「JFS2でdf -gを用い、lff と内部スナップショットを確認する」を述べ、対象は運用引継ぎ lff（運用・df）です。「setsecattr」は「セキュリティでsetsecattrを用い、user」を指し、user attributesではse・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr バックアウト確認 user attributes 0362</strong></p><p>検証目的: セキュリティのsetsecattr バックアウト確認 user attributes 0362について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティバックアウト確認002-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0362A
画面・出力には AIX0362A が表示され、setsecattr バックアウト確認 user attributes 0362 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0362B
画面・出力には AIX0362B が表示され、setsecattr バックアウト確認 user attributes 0362 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0362C
画面・出力には AIX0362C が表示され、setsecattr バックアウト確認 user attributes 0362 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0362A が画面・出力に表示されること
② ステップ2 の AIX0362B が画面・出力に表示されること
③ ステップ3 の AIX0362C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0437"><h3>setsecattr 変更後確認 audit class 0015</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>岩清水確認ではAIX 7.3のセキュリティで setsecattr を確認します。岩清水確認のセキュリティでは audit class とロール一覧を作業票へ保管します。岩清水確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。岩清水確認の注意点として ユーザー属性変更の根拠不足 を避けるため lsrole ALL も併記します。権限管理の作業票として、岩清水確認を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr 変更後確認 audit class 0015の設定や表示を読む前に役割を確認します。diag -d ent0 障害切り分け attribute 0016ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはセキュリティでsetsecattrを用い・audit class とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 状態を読み取るための働きはデバイス管理でdiag -d ent0を用い・attribute と構成マネージャー結果を確認する。</li><li>C. 状態を読み取るための働きはSRCとログでsyslog_ssw -cを用い・PID とinetdデバッグ出力を確認する。</li><li>D. 状態を読み取るための働きはデバイス管理でcfgmgrを用い・location code と構成マネージャー結果を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「セキュリティでsetsecattrを用い、audit class」に対応する項目はaudit class（変更・sets）です。セキュリティの仕様は「セキュリティでsetsecattrを用い、audit class」で、確認対象はse・変更後です。障害切・diagのB:は「デバイス管理でdiag -d ent0を用い、attribute」を述べ、対象は障害切り分け attribute（障害・diag）です。属性・syslのC:は「SRCとログでsyslog_ssw -cを用い、PID」を述べ、対象は属性確認 PID（属性・sysl）です。性能・cfgmのD:は「デバイス管理でcfgmgrを用い、location code」を述べ、対象はlocation code（性能・cfgm）です。「setsecattr」は「セキュリティでsetsecattrを用い、audit class」を指し、audit classではse・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 変更後確認 audit class 0015</strong></p><p>検証目的: セキュリティのsetsecattr 変更後確認 audit class 0015について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更後確認015-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0015A
画面・出力には AIX0015A が表示され、setsecattr 変更後確認 audit class 0015 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0015B
画面・出力には AIX0015B が表示され、setsecattr 変更後確認 audit class 0015 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0015C
画面・出力には AIX0015C が表示され、setsecattr 変更後確認 audit class 0015 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0015A が画面・出力に表示されること
② ステップ2 の AIX0015B が画面・出力に表示されること
③ ステップ3 の AIX0015C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0438"><h3>setsecattr 変更後確認 audit class 0075</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>青磁照合ではAIX 7.3のセキュリティで setsecattr を確認します。青磁照合のセキュリティでは audit class とロール一覧を作業票へ保管します。青磁照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる材料にします。青磁照合の注意点として ユーザー属性変更の根拠不足 を避けるため lsrole ALL も併記します。権限管理の作業票として、青磁照合を照合結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr 変更後確認 audit class 0075について構成や状態を確認します。diag -d ent0 障害切り分け attribute 0076ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはデバイス管理でdiag -d ent0を用い・attribute と構成マネージャー結果を確認する。</li><li>B. 状態を読み取るための働きはセキュリティでsetsecattrを用い・audit class とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはSRCとログでsyslog_ssw -rを用い・Status とinetdデバッグ出力を確認する。</li><li>D. 状態を読み取るための働きはデバイス管理でcfgmgrを用い・location code と構成マネージャー結果を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでsetsecattrを用い、audit class」に対応する項目はaudit class（変更・sets）です。変更後に関するセキュリティの仕様は「セキュリティでsetsecattrを用い、audit class」で、確認対象はse・変更後です。障害切・diagのA:は「デバイス管理でdiag -d ent0を用い、attribute」を述べ、対象は障害切り分け attribute（障害・diag）です。状態・syslのC:は「SRCとログでsyslog_ssw -rを用い、Status」を述べ、対象は状態確認 Status（状態・sysl）です。性能・cfgmのD:は「デバイス管理でcfgmgrを用い、location code」を述べ、対象はlocation code（性能・cfgm）です。「setsecattr」は「セキュリティでsetsecattrを用い、audit class」を指し、audit classではse・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 変更後確認 audit class 0075</strong></p><p>検証目的: セキュリティのsetsecattr 変更後確認 audit class 0075について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更後確認075-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0075A
画面・出力には AIX0075A が表示され、setsecattr 変更後確認 audit class 0075 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0075B
画面・出力には AIX0075B が表示され、setsecattr 変更後確認 audit class 0075 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0075C
画面・出力には AIX0075C が表示され、setsecattr 変更後確認 audit class 0075 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0075A が画面・出力に表示されること
② ステップ2 の AIX0075B が画面・出力に表示されること
③ ステップ3 の AIX0075C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0439"><h3>setsecattr 変更後確認 enhanced_RBAC 0491</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>松風確認ではAIX 7.3のセキュリティで setsecattr を確認します。松風確認のセキュリティでは enhanced_RBAC とロール一覧を照合票へ整理します。松風確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。松風確認の注意点として ユーザー属性変更の根拠不足 を避けるため lsuser user1 も併記します。権限管理の作業票として、松風確認を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr 変更後確認 enhanced_RBAC 0491について構成や状態を確認します。diag -d ent0 障害切り分け path status 0492ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はデバイス管理でdiag -d ent0を用い・path status と構成マネージャー結果を確認する。</li><li>B. 一次資料が示す主目的はSRCとログでsyslog_ssw -cを用い・IDENTIFIER とinetdデバッグ出力を確認する。</li><li>C. 一次資料が示す主目的はセキュリティでsetsecattrを用い・enhanced_RBAC とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はJFS2でdf -gを用い・mountguard とログデバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「セキュリティでsetsecattrを用い、enhanced_RBAC」に対応する項目は変更後確認 enhanced_RBA（変更・sets）です。変更後に関するセキュリティの仕様は「セキュリティでsetsecattrを用い」で、確認対象はse・変更後です。障害切・diagのA:は「デバイス管理でdiag -d ent0を用い、path」を述べ、対象はpath status（障害・diag）です。属性・syslのB:は「SRCとログでsyslog_ssw -cを用い」を述べ、対象は属性確認 IDENTIFIER（属性・sysl）です。バック・dfのD:は「JFS2でdf -gを用い、mountguard」を述べ、対象はバックアウト確認 mountguar（バッ・df）です。「setsecattr」は「セキュリティでsetsecattrを用い」を指し、変更後確認 enhanced_RBAではse・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 変更後確認 enhanced_RBAC 0491</strong></p><p>検証目的: セキュリティのsetsecattr 変更後確認 enhanced_RBAC 0491について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更後確認011-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0491A
画面・出力には AIX0491A が表示され、setsecattr 変更後確認 enhanced_RBAC 0491 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0491B
画面・出力には AIX0491B が表示され、setsecattr 変更後確認 enhanced_RBAC 0491 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0491C
画面・出力には AIX0491C が表示され、setsecattr 変更後確認 enhanced_RBAC 0491 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0491A が画面・出力に表示されること
② ステップ2 の AIX0491B が画面・出力に表示されること
③ ステップ3 の AIX0491C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0440"><h3>setsecattr 変更後確認 enhanced_RBAC 0551</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>遠雷照合ではAIX 7.3のセキュリティで setsecattr を確認します。遠雷照合のセキュリティでは enhanced_RBAC とロール一覧を照合票へ整理します。遠雷照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。遠雷照合の注意点として ユーザー属性変更の根拠不足 を避けるため lsuser user1 も併記します。権限管理の作業票として、遠雷照合を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr 変更後確認 enhanced_RBAC 0551の設定や表示を読む前に役割を確認します。diag -d ent0 障害切り分け path status 0552ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はデバイス管理でdiag -d ent0を用い・path status と構成マネージャー結果を確認する。</li><li>B. 一次資料が示す主目的はデバイス属性を変更する管理コマンドである。</li><li>C. 一次資料が示す主目的はJFS2でsnapを用い・lff とログデバイス設定を確認する。</li><li>D. 一次資料が示す主目的はセキュリティでsetsecattrを用い・enhanced_RBAC とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでsetsecattrを用い、enhanced_RBAC」に対応する項目は変更後確認 enhanced_RBA（変更・sets）です。変更後に関するセキュリティの仕様は「セキュリティでsetsecattrを用い」で、確認対象はse・変更後です。障害切・diagのA:は「デバイス管理でdiag -d ent0を用い、path」を述べ、対象はpath status（障害・diag）です。詳細・一致・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は詳細確認 一致条件（詳細・chde）です。監査・snapのC:は「JFS2でsnapを用い、lff とログデバイス設定を確認する」を述べ、対象は監査記録 lff（監査・snap）です。「setsecattr」は「セキュリティでsetsecattrを用い」を指し、変更後確認 enhanced_RBAではse・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 変更後確認 enhanced_RBAC 0551</strong></p><p>検証目的: セキュリティのsetsecattr 変更後確認 enhanced_RBAC 0551について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更後確認071-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0551A
画面・出力には AIX0551A が表示され、setsecattr 変更後確認 enhanced_RBAC 0551 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0551B
画面・出力には AIX0551B が表示され、setsecattr 変更後確認 enhanced_RBAC 0551 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0551C
画面・出力には AIX0551C が表示され、setsecattr 変更後確認 enhanced_RBAC 0551 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0551A が画面・出力に表示されること
② ステップ2 の AIX0551B が画面・出力に表示されること
③ ステップ3 の AIX0551C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0441"><h3>setsecattr 属性確認 user attributes 0392</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>夕映記録ではAIX 7.3のセキュリティで setsecattr を確認します。夕映記録のセキュリティでは user attributes とユーザー属性を引継ぎ票へ保管します。夕映記録は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。夕映記録の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、夕映記録を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr 属性確認 user attributes 0392を同一分類のdiag -d ent0 状態確認 attribute 0393と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はデバイス管理でdiag -d ent0を用い・attribute と診断対象表示を確認する。</li><li>B. コマンドまたは機能の用途はSRCとログでsyslog_ssw -cを用い・Subsystem とSRCサブシステム表示を確認する。</li><li>C. コマンドまたは機能の用途はLVMでchlvを用い・VG STATE とミラーコピー状態を確認する。</li><li>D. コマンドまたは機能の用途はセキュリティでsetsecattrを用い・user attributes とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでsetsecattrを用い、user attributes」に対応する項目はuser attributes（属性・sets）です。属性に関するセキュリティの仕様は「セキュリティでsetsecattrを用い、user」で、確認対象はse・属性です。状態・diagのA:は「デバイス管理でdiag -d ent0を用い、attribute」を述べ、対象は状態確認 attribute（状態・diag）です。運用引・syslのB:は「SRCとログでsyslog_ssw -cを用い、Subsystem」を述べ、対象は運用引継ぎ Subsystem（運用・sysl）です。構成・chlvのC:は「LVMでchlvを用い、VG STATE」を述べ、対象はVG STATE（構成・chlv）です。「setsecattr」は「セキュリティでsetsecattrを用い、user」を指し、user attributesではse・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 属性確認 user attributes 0392</strong></p><p>検証目的: セキュリティのsetsecattr 属性確認 user attributes 0392について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認032-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0392A
画面・出力には AIX0392A が表示され、setsecattr 属性確認 user attributes 0392 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0392B
画面・出力には AIX0392B が表示され、setsecattr 属性確認 user attributes 0392 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。user attributes を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0392C
画面・出力には AIX0392C が表示され、setsecattr 属性確認 user attributes 0392 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0392A が画面・出力に表示されること
② ステップ2 の AIX0392B が画面・出力に表示されること
③ ステップ3 の AIX0392C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0442"><h3>setsecattr 性能確認 audit class 0045</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>深雪照合ではAIX 7.3のセキュリティで setsecattr を確認します。深雪照合のセキュリティでは audit class と監査設定を判定票へ残します。深雪照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。深雪照合の注意点として ロール割当と権限文字列の不一致 を避けるため lsrole ALL も併記します。権限管理の作業票として、深雪照合を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr 性能確認 audit class 0045を保守記録に説明する必要があります。diag -d ent0 起動確認 microcode level 0046と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はデバイス管理でdiag -d ent0を用い・microcode level とデバイス一覧を確認する。</li><li>B. 運用時に利用する技術的役割はSRCとログでsyslog_ssw -cを用い・TIMESTAMP とエラーログ一覧を確認する。</li><li>C. 運用時に利用する技術的役割はセキュリティでsetsecattrを用い・audit class と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はデバイス管理でcfgmgrを用い・path status とデバイス一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでsetsecattrを用い、audit class」に対応する項目はaudit class（性能・sets）です。セキュリティの仕様は「セキュリティでsetsecattrを用い、audit class」で、確認対象はse・性能です。起動・diagのA:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（起動・diag）です。バック・syslのB:は「SRCとログでsyslog_ssw -cを用い、TIMESTAMP」を述べ、対象はバックアウト確認 TIMESTAMP（バッ・sysl）です。変更後・cfgmのD:は「デバイス管理でcfgmgrを用い、path status」を述べ、対象はpath status（変更・cfgm）です。「setsecattr」は「セキュリティでsetsecattrを用い、audit class」を指し、audit classではse・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 性能確認 audit class 0045</strong></p><p>検証目的: セキュリティのsetsecattr 性能確認 audit class 0045について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ性能確認045-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0045A
画面・出力には AIX0045A が表示され、setsecattr 性能確認 audit class 0045 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0045B
画面・出力には AIX0045B が表示され、setsecattr 性能確認 audit class 0045 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0045C
画面・出力には AIX0045C が表示され、setsecattr 性能確認 audit class 0045 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0045A が画面・出力に表示されること
② ステップ2 の AIX0045B が画面・出力に表示されること
③ ステップ3 の AIX0045C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0443"><h3>setsecattr 性能確認 audit class 0105</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>花冷点検ではAIX 7.3のセキュリティで setsecattr を確認します。花冷点検のセキュリティでは audit class と監査設定を判定票へ残します。花冷点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる判定結果にします。花冷点検の注意点として ロール割当と権限文字列の不一致 を避けるため lsrole ALL も併記します。権限管理の作業票として、花冷点検を引継ぎ材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「setsecattr 性能確認 audit class 0105」を「diag -d ent0 起動確認 microcode level 0106」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はデバイス管理でdiag -d ent0を用い・microcode level とデバイス一覧を確認する。</li><li>B. 運用時に利用する技術的役割はセキュリティでsetsecattrを用い・audit class と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はSRCとログでsyslog_ssw -rを用い・syslog.conf とエラーログ一覧を確認する。</li><li>D. 運用時に利用する技術的役割はデバイス管理でcfgmgrを用い・path status とデバイス一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「セキュリティでsetsecattrを用い、audit class」に対応する項目はaudit class（性能・sets）です。性能に関するセキュリティの仕様は「セキュリティでsetsecattrを用い、audit class」で、確認対象はse・性能です。起動・diagのA:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（起動・diag）です。監査・syslのC:は「SRCとログでsyslog_ssw -rを用い」を述べ、対象は監査記録 syslog.conf（監査・sysl）です。変更後・cfgmのD:は「デバイス管理でcfgmgrを用い、path status」を述べ、対象はpath status（変更・cfgm）です。「setsecattr」は「セキュリティでsetsecattrを用い、audit class」を指し、audit classではse・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 性能確認 audit class 0105</strong></p><p>検証目的: セキュリティのsetsecattr 性能確認 audit class 0105について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ性能確認105-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0105A
画面・出力には AIX0105A が表示され、setsecattr 性能確認 audit class 0105 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0105B
画面・出力には AIX0105B が表示され、setsecattr 性能確認 audit class 0105 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0105C
画面・出力には AIX0105C が表示され、setsecattr 性能確認 audit class 0105 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0105A が画面・出力に表示されること
② ステップ2 の AIX0105B が画面・出力に表示されること
③ ステップ3 の AIX0105C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0444"><h3>setsecattr 性能確認 enhanced_RBAC 0521</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>白露照合ではAIX 7.3のセキュリティで setsecattr を確認します。白露照合のセキュリティでは enhanced_RBAC と監査設定を復旧票へ残します。白露照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。白露照合の注意点として ロール割当と権限文字列の不一致 を避けるため lsuser user1 も併記します。権限管理の作業票として、白露照合を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「setsecattr 性能確認 enhanced_RBAC 0521」を「diag -d ent0 起動確認 location code 0522」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はデバイス管理でdiag -d ent0を用い・location code とデバイス一覧を確認する。</li><li>B. 仕様上の役割はSRCとログでsyslog_ssw -cを用い・Subsystem とエラーログ一覧を確認する。</li><li>C. 仕様上の役割はJFS2でdf -gを用い・log=INLINE とファイルシステム属性を確認する。</li><li>D. 仕様上の役割はセキュリティでsetsecattrを用い・enhanced_RBAC と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでsetsecattrを用い、enhanced_RBAC」に対応する項目は性能確認 enhanced_RBAC（性能・sets）です。性能に関するセキュリティの仕様は「セキュリティでsetsecattrを用い」で、確認対象はse・性能です。起動・diagのA:は「デバイス管理でdiag -d ent0を用い、location」を述べ、対象はlocation code（起動・diag）です。バック・syslのB:は「SRCとログでsyslog_ssw -cを用い、Subsystem」を述べ、対象はバックアウト確認 Subsystem（バッ・sysl）です。属性・dfのC:は「JFS2でdf -gを用い、log=INLINE」を述べ、対象は属性確認 log=INLINE（属性・df）です。「setsecattr」は「セキュリティでsetsecattrを用い」を指し、性能確認 enhanced_RBACではse・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 性能確認 enhanced_RBAC 0521</strong></p><p>検証目的: セキュリティのsetsecattr 性能確認 enhanced_RBAC 0521について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ性能確認041-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0521A
画面・出力には AIX0521A が表示され、setsecattr 性能確認 enhanced_RBAC 0521 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0521B
画面・出力には AIX0521B が表示され、setsecattr 性能確認 enhanced_RBAC 0521 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0521C
画面・出力には AIX0521C が表示され、setsecattr 性能確認 enhanced_RBAC 0521 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0521A が画面・出力に表示されること
② ステップ2 の AIX0521B が画面・出力に表示されること
③ ステップ3 の AIX0521C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0445"><h3>setsecattr 性能確認 enhanced_RBAC 0581</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>群青点検ではAIX 7.3のセキュリティで setsecattr を確認します。群青点検のセキュリティでは enhanced_RBAC と監査設定を復旧票へ残します。群青点検は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。群青点検の注意点として ロール割当と権限文字列の不一致 を避けるため lsuser user1 も併記します。権限管理の作業票として、群青点検を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr 性能確認 enhanced_RBAC 0581を保守記録に説明する必要があります。diag -d ent0 起動確認 location code 0582と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はデバイス管理でdiag -d ent0を用い・location code とデバイス一覧を確認する。</li><li>B. 仕様上の役割はデバイス属性を変更する管理コマンドである。</li><li>C. 仕様上の役割はJFS2でsnapを用い・agblksize とファイルシステム属性を確認する。</li><li>D. 仕様上の役割はセキュリティでsetsecattrを用い・enhanced_RBAC と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「セキュリティでsetsecattrを用い、enhanced_RBAC」に対応する項目は性能確認 enhanced_RBAC（性能・sets）です。性能に関するセキュリティの仕様は「セキュリティでsetsecattrを用い」で、確認対象はse・性能です。起動・diagのA:は「デバイス管理でdiag -d ent0を用い、location」を述べ、対象はlocation code（起動・diag）です。状態・対象・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は状態判定 対象ノード（状態・chde）です。状態・snapのC:は「JFS2でsnapを用い、agblksize」を述べ、対象は状態確認 agblksize（状態・snap）です。「setsecattr」は「セキュリティでsetsecattrを用い」を指し、性能確認 enhanced_RBACではse・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 性能確認 enhanced_RBAC 0581</strong></p><p>検証目的: セキュリティのsetsecattr 性能確認 enhanced_RBAC 0581について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ性能確認101-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0581A
画面・出力には AIX0581A が表示され、setsecattr 性能確認 enhanced_RBAC 0581 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0581B
画面・出力には AIX0581B が表示され、setsecattr 性能確認 enhanced_RBAC 0581 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0581C
画面・出力には AIX0581C が表示され、setsecattr 性能確認 enhanced_RBAC 0581 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0581A が画面・出力に表示されること
② ステップ2 の AIX0581B が画面・出力に表示されること
③ ステップ3 の AIX0581C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0446"><h3>setsecattr 構成照合 audit class 0204</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>若草保守ではAIX 7.3のセキュリティで setsecattr を確認します。若草保守のセキュリティでは audit class とユーザー属性を同じ証跡に残します。若草保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若草保守の注意点として RBACモード誤認 を避けるため lsrole ALL も併記します。権限管理の作業票として、若草保守を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr 構成照合 audit class 0204の技術的な意味を資料で確認するとき、mirrorvg 変更前確認 LV STATE 0205との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はLVMでmirrorvgを用い・LV STATE とミラーコピー状態を確認する。</li><li>B. 構成を確認する際の意味はSRCとログでsyslog_ssw -rを用い・PID とSRCサブシステム表示を確認する。</li><li>C. 構成を確認する際の意味はLVMでlslvを用い・VG STATE とミラーコピー状態を確認する。</li><li>D. 構成を確認する際の意味はセキュリティでsetsecattrを用い・audit class とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでsetsecattrを用い、audit class」に対応する項目はaudit class（構成・sets）です。構成に関するセキュリティの仕様は「セキュリティでsetsecattrを用い、audit class」で、確認対象はse・構成です。変更前・mirrのA:は「LVMでmirrorvgを用い、LV STATE」を述べ、対象はLV STATE（変更・mirr）です。起動・syslのB:は「SRCとログでsyslog_ssw -rを用い、PID」を述べ、対象は起動確認 PID（起動・sysl）です。運用引・lslvのC:は「LVMでlslvを用い、VG STATE」を述べ、対象はVG STATE（運用・lslv）です。「setsecattr」は「セキュリティでsetsecattrを用い、audit class」を指し、audit classではse・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 構成照合 audit class 0204</strong></p><p>検証目的: セキュリティのsetsecattr 構成照合 audit class 0204について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ構成照合084-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0204A
画面・出力には AIX0204A が表示され、setsecattr 構成照合 audit class 0204 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0204B
画面・出力には AIX0204B が表示され、setsecattr 構成照合 audit class 0204 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0204C
画面・出力には AIX0204C が表示され、setsecattr 構成照合 audit class 0204 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0204A が画面・出力に表示されること
② ステップ2 の AIX0204B が画面・出力に表示されること
③ ステップ3 の AIX0204C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0447"><h3>setsecattr 構成照合 enhanced_RBAC 0680</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>青葉保守ではAIX 7.3のセキュリティで setsecattr を確認します。青葉保守のセキュリティでは enhanced_RBAC とユーザー属性を引継ぎ票へ保管します。青葉保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。青葉保守の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、青葉保守を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr 構成照合 enhanced_RBAC 0680を同一分類のmirrorvg 変更前確認 STALE PARTITIONS 0681と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はLVMでmirrorvgを用い・STALE PARTITIONS とミラーコピー状態を確認する。</li><li>B. コマンドまたは機能の用途はネットワークでsmitty etherchannelを用い・Destinationである。</li><li>C. コマンドまたは機能の用途はセキュリティでsetsecattrを用い・enhanced_RBAC とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はJFS2でsnapを用い・lff とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでsetsecattrを用い、enhanced_RBAC」に対応する項目は構成照合 enhanced_RBAC（構成・sets）です。構成に関するセキュリティの仕様は「セキュリティでsetsecattrを用い」で、確認対象はse・構成です。変更前・mirrのA:は「LVMでmirrorvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（変更・mirr）です。監査・smitのB:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は監査記録 Destination（監査・smit）です。障害切・snapのD:は「JFS2でsnapを用い、lff とマウントオプションを確認する」を述べ、対象は障害切り分け lff（障害・snap）です。「setsecattr」は「セキュリティでsetsecattrを用い」を指し、構成照合 enhanced_RBACではse・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 構成照合 enhanced_RBAC 0680</strong></p><p>検証目的: セキュリティのsetsecattr 構成照合 enhanced_RBAC 0680について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ構成照合080-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0680A
画面・出力には AIX0680A が表示され、setsecattr 構成照合 enhanced_RBAC 0680 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0680B
画面・出力には AIX0680B が表示され、setsecattr 構成照合 enhanced_RBAC 0680 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0680C
画面・出力には AIX0680C が表示され、setsecattr 構成照合 enhanced_RBAC 0680 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0680A が画面・出力に表示されること
② ステップ2 の AIX0680B が画面・出力に表示されること
③ ステップ3 の AIX0680C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0448"><h3>setsecattr 運用引継ぎ audit class 0234</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>銀嶺保守ではAIX 7.3のセキュリティで setsecattr を確認します。銀嶺保守のセキュリティでは audit class とRBAC属性を変更票へ記録します。銀嶺保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。銀嶺保守の注意点として 監査データ未取得でのroleqry実行 を避けるため lsrole ALL も併記します。権限管理の作業票として、銀嶺保守を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr 運用引継ぎ audit class 0234の役割を調べています。diag -d ent0 容量確認 microcode level 0235の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはデバイス管理でdiag -d ent0を用い・microcode level とODM属性を確認する。</li><li>B. 機能の説明としてはSRCとログでsyslog_ssw -rを用い・TIMESTAMP とsyslog設定変換を確認する。</li><li>C. 機能の説明としてはセキュリティでsetsecattrを用い・audit class とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはデバイス属性を変更する管理コマンドである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「セキュリティでsetsecattrを用い、audit class」に対応する項目はaudit class（運用・sets）です。運用引に関するセキュリティの仕様は「セキュリティでsetsecattrを用い、audit class」で、確認対象はse・運用引です。容量・diagのA:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（容量・diag）です。障害切・syslのB:は「SRCとログでsyslog_ssw -rを用い、TIMESTAMP」を述べ、対象は障害切り分け TIMESTAMP（障害・sysl）です。変更前・chdeのD:は「デバイス属性を変更する管理コマンド」を述べ、対象は変更前確認 識別値（変更・chde）です。「setsecattr」は「セキュリティでsetsecattrを用い、audit class」を指し、audit classではse・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 運用引継ぎ audit class 0234</strong></p><p>検証目的: セキュリティのsetsecattr 運用引継ぎ audit class 0234について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ運用引継ぎ114-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0234A
画面・出力には AIX0234A が表示され、setsecattr 運用引継ぎ audit class 0234 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0234B
画面・出力には AIX0234B が表示され、setsecattr 運用引継ぎ audit class 0234 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0234C
画面・出力には AIX0234C が表示され、setsecattr 運用引継ぎ audit class 0234 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0234A が画面・出力に表示されること
② ステップ2 の AIX0234B が画面・出力に表示されること
③ ステップ3 の AIX0234C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0449"><h3>setsecattr 運用引継ぎ enhanced_RBAC 0710</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>早苗保守ではAIX 7.3のセキュリティで setsecattr を確認します。早苗保守のセキュリティでは enhanced_RBAC とRBAC属性を確認票へ整理します。早苗保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。早苗保守の注意点として 監査データ未取得でのroleqry実行 を避けるため lsuser user1 も併記します。権限管理の作業票として、早苗保守を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> setsecattr 運用引継ぎ enhanced_RBAC 0710に関する障害切り分けの前提を確認しています。diag -d ent0 容量確認 location code 0711の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はデバイス管理でdiag -d ent0を用い・location code とODM属性を確認する。</li><li>B. 障害切り分けに用いる役割はネットワークでsmitty etherchannelを用い・Link Status と経路表を確認する。</li><li>C. 障害切り分けに用いる役割はJFS2でsnapを用い・agblksize と内部スナップショットを確認する。</li><li>D. 障害切り分けに用いる役割はセキュリティでsetsecattrを用い・enhanced_RBAC とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「セキュリティでsetsecattrを用い、enhanced_RBAC」に対応する項目は運用引継ぎ enhanced_RBA（運用・sets）です。運用引に関するセキュリティの仕様は「セキュリティでsetsecattrを用い」で、確認対象はse・運用引です。容量・diagのA:は「デバイス管理でdiag -d ent0を用い、location」を述べ、対象はlocation code（容量・diag）です。状態・smitのB:は「ネットワークでsmitty etherchannelを用い」を述べ、対象はLink Status（状態・smit）です。起動・snapのC:は「JFS2でsnapを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・snap）です。「setsecattr」は「セキュリティでsetsecattrを用い」を指し、運用引継ぎ enhanced_RBAではse・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>setsecattr 運用引継ぎ enhanced_RBAC 0710</strong></p><p>検証目的: セキュリティのsetsecattr 運用引継ぎ enhanced_RBAC 0710について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ運用引継ぎ110-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; setsecattr
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0710A
画面・出力には AIX0710A が表示され、setsecattr 運用引継ぎ enhanced_RBAC 0710 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0710B
画面・出力には AIX0710B が表示され、setsecattr 運用引継ぎ enhanced_RBAC 0710 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0710C
画面・出力には AIX0710C が表示され、setsecattr 運用引継ぎ enhanced_RBAC 0710 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0710A が画面・出力に表示されること
② ステップ2 の AIX0710B が画面・出力に表示されること
③ ステップ3 の AIX0710C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0450"><h3>usrck -n ALL 変更後確認 enhanced_RBAC 0158</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>春霞採取ではAIX 7.3のセキュリティで usrck -n ALL を確認します。春霞採取のセキュリティでは enhanced_RBAC とRBAC属性を確認票へ整理します。春霞採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。春霞採取の注意点として 監査データ未取得でのroleqry実行 を避けるため lsuser user1 も併記します。権限管理の作業票として、春霞採取を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 変更後確認 enhanced_RBAC 0158に関する障害切り分けの前提を確認しています。lsdev -Cc disk 障害切り分け PVID 0159の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はセキュリティでusrck -n ALLを用い・enhanced_RBAC とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 障害切り分けに用いる役割はデバイス管理でlsdev -Cc diskを用い・PVID とODM属性を確認する。</li><li>C. 障害切り分けに用いる役割はSRCとログでerrclearを用い・PID とsyslog設定変換を確認する。errclear 属性確認 PID 0464固有の属性も確認対象に含める。</li><li>D. 障害切り分けに用いる役割はデバイス管理でrmdev -Rl ent1を用い・attribute とODM属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでusrck -n ALLを用い、enhanced_RBAC」に対応する項目は変更後確認 enhanced_RBA（変更・usrc）です。変更後に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い」で、確認対象はus・変更後です。障害切・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い、PVID」を述べ、対象は障害切り分け PVID（障害・lsde）です。属性・errcのC:は「SRCとログでerrclearを用い、PID」を述べ、対象は属性確認 PID（属性・errc）です。性能・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象は性能確認 attribute（性能・rmde）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い」を指し、変更後確認 enhanced_RBAではus・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 変更後確認 enhanced_RBAC 0158</strong></p><p>検証目的: セキュリティのusrck -n ALL 変更後確認 enhanced_RBAC 0158について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更後確認038-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0158A
画面・出力には AIX0158A が表示され、usrck -n ALL 変更後確認 enhanced_RBAC 0158 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0158B
画面・出力には AIX0158B が表示され、usrck -n ALL 変更後確認 enhanced_RBAC 0158 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0158C
画面・出力には AIX0158C が表示され、usrck -n ALL 変更後確認 enhanced_RBAC 0158 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0158A が画面・出力に表示されること
② ステップ2 の AIX0158B が画面・出力に表示されること
③ ステップ3 の AIX0158C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0451"><h3>usrck -n ALL 変更後確認 roles 0634</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>銀嶺採取ではAIX 7.3のセキュリティで usrck -n ALL を確認します。銀嶺採取のセキュリティでは roles とRBAC属性を保守票へ記録します。銀嶺採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。銀嶺採取の注意点として 監査データ未取得でのroleqry実行 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、銀嶺採取を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 変更後確認 roles 0634の役割を調べています。lsdev -Cc disk 障害切り分け microcode level 0635の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はデバイス管理でlsdev -Cc diskを用い・microcode level とODM属性を確認する。</li><li>B. 表示や設定で扱う内容はネットワークでlsdev -Cc adapterを用い・Gateway と経路表を確認する。</li><li>C. 表示や設定で扱う内容はセキュリティでusrck -n ALLを用い・roles とRBAC属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はJFS2でdefragfsを用い・lff と内部スナップショットを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでusrck -n ALLを用い、roles とRBAC属性を確認する」に対応する項目は変更後確認 roles（変更・usrc）です。変更後に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い、roles」で、確認対象はus・変更後です。障害切・lsdeのA:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象はmicrocode level（障害・lsde）です。容量・lsdeのB:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は容量確認 Gateway（容量・lsde）です。バック・defrのD:は「JFS2でdefragfsを用い、lff」を述べ、対象はバックアウト確認 lff（バッ・defr）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い、roles」を指し、変更後確認 rolesではus・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 変更後確認 roles 0634</strong></p><p>検証目的: セキュリティのusrck -n ALL 変更後確認 roles 0634について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ変更後確認034-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0634A
画面・出力には AIX0634A が表示され、usrck -n ALL 変更後確認 roles 0634 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0634B
画面・出力には AIX0634B が表示され、usrck -n ALL 変更後確認 roles 0634 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0634C
画面・出力には AIX0634C が表示され、usrck -n ALL 変更後確認 roles 0634 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0634A が画面・出力に表示されること
② ステップ2 の AIX0634B が画面・出力に表示されること
③ ステップ3 の AIX0634C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0452"><h3>usrck -n ALL 属性確認 authorizations 0476</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>若潮整理ではAIX 7.3のセキュリティで usrck -n ALL を確認します。若潮整理のセキュリティでは authorizations とユーザー属性を引継ぎ票へ保管します。若潮整理は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若潮整理の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、若潮整理を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 属性確認 authorizations 0476の技術的な意味を資料で確認するとき、lspv 状態確認 LV STATE 0477との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はセキュリティでusrck -n ALLを用い・authorizations とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はLVMでlspvを用い・LV STATE とミラーコピー状態を確認する。</li><li>C. コマンドまたは機能の用途はSRCとログでstartsrc -s inetd -aを用い・PID とSRCサブシステム表示を確認する。</li><li>D. コマンドまたは機能の用途はJFS2でcrfsを用い・isnapshot とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「セキュリティでusrck -n ALLを用い、authorizations」に対応する項目は属性確認 authorization（属性・usrc）です。属性に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い」で、確認対象はus・属性です。状態・lspvのB:は「LVMでlspvを用い、LV STATE」を述べ、対象はLV STATE（状態・lspv）です。容量・starのC:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は容量確認 PID（容量・star）です。変更前・crfsのD:は「JFS2でcrfsを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・crfs）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い」を指し、属性確認 authorizationではus・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 属性確認 authorizations 0476</strong></p><p>検証目的: セキュリティのusrck -n ALL 属性確認 authorizations 0476について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ属性確認116-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0476A
画面・出力には AIX0476A が表示され、usrck -n ALL 属性確認 authorizations 0476 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0476B
画面・出力には AIX0476B が表示され、usrck -n ALL 属性確認 authorizations 0476 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0476C
画面・出力には AIX0476C が表示され、usrck -n ALL 属性確認 authorizations 0476 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0476A が画面・出力に表示されること
② ステップ2 の AIX0476B が画面・出力に表示されること
③ ステップ3 の AIX0476C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0453"><h3>usrck -n ALL 性能確認 enhanced_RBAC 0128</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>翠風採取ではAIX 7.3のセキュリティで usrck -n ALL を確認します。翠風採取のセキュリティでは enhanced_RBAC とユーザー属性を引継ぎ票へ保管します。翠風採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。翠風採取の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、翠風採取を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 性能確認 enhanced_RBAC 0128を同一分類のlsdev -Cc disk 起動確認 Available 0129と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はデバイス管理でlsdev -Cc diskを用い・Available と診断対象表示を確認する。</li><li>B. コマンドまたは機能の用途はセキュリティでusrck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. コマンドまたは機能の用途はSRCとログでerrclearを用い・TIMESTAMP とSRCサブシステム表示を確認する。</li><li>D. コマンドまたは機能の用途はデバイス管理でrmdev -Rl ent1を用い・microcode level と診断対象表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「セキュリティでusrck -n ALLを用い、enhanced_RBAC」に対応する項目は性能確認 enhanced_RBAC（性能・usrc）です。性能に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い」で、確認対象はus・性能です。起動・lsdeのA:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 Available（起動・lsde）です。バック・errcのC:は「SRCとログでerrclearを用い、TIMESTAMP」を述べ、対象はバックアウト確認 TIMESTAMP（バッ・errc）です。変更後・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象はmicrocode level（変更・rmde）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い」を指し、性能確認 enhanced_RBACではus・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 性能確認 enhanced_RBAC 0128</strong></p><p>検証目的: セキュリティのusrck -n ALL 性能確認 enhanced_RBAC 0128について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ性能確認008-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0128A
画面・出力には AIX0128A が表示され、usrck -n ALL 性能確認 enhanced_RBAC 0128 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0128B
画面・出力には AIX0128B が表示され、usrck -n ALL 性能確認 enhanced_RBAC 0128 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0128C
画面・出力には AIX0128C が表示され、usrck -n ALL 性能確認 enhanced_RBAC 0128 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0128A が画面・出力に表示されること
② ステップ2 の AIX0128B が画面・出力に表示されること
③ ステップ3 の AIX0128C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0454"><h3>usrck -n ALL 性能確認 enhanced_RBAC 0188</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>雪解判定ではAIX 7.3のセキュリティで usrck -n ALL を確認します。雪解判定のセキュリティでは enhanced_RBAC とユーザー属性を引継ぎ票へ保管します。雪解判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。雪解判定の注意点として RBACモード誤認 を避けるため lsuser user1 も併記します。権限管理の作業票として、雪解判定を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 性能確認 enhanced_RBAC 0188の技術的な意味を資料で確認するとき、lsdev -Cc disk 起動確認 Available 0189との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はデバイス管理でlsdev -Cc diskを用い・Available と診断対象表示を確認する。</li><li>B. コマンドまたは機能の用途はセキュリティでusrck -n ALLを用い・enhanced_RBAC とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. コマンドまたは機能の用途はSRCとログでstartsrc -s inetd -aを用い・syslog.confである。</li><li>D. コマンドまたは機能の用途はデバイス管理でrmdev -Rl ent1を用い・microcode level と診断対象表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「セキュリティでusrck -n ALLを用い、enhanced_RBAC」に対応する項目は性能確認 enhanced_RBAC（性能・usrc）です。性能に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い」で、確認対象はus・性能です。起動・lsdeのA:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 Available（起動・lsde）です。監査・starのC:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は監査記録 syslog.conf（監査・star）です。変更後・rmdeのD:は「デバイス管理でrmdev -Rl ent1を用い」を述べ、対象はmicrocode level（変更・rmde）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い」を指し、性能確認 enhanced_RBACではus・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 性能確認 enhanced_RBAC 0188</strong></p><p>検証目的: セキュリティのusrck -n ALL 性能確認 enhanced_RBAC 0188について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ性能確認068-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0188A
画面・出力には AIX0188A が表示され、usrck -n ALL 性能確認 enhanced_RBAC 0188 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0188B
画面・出力には AIX0188B が表示され、usrck -n ALL 性能確認 enhanced_RBAC 0188 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。enhanced_RBAC を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0188C
画面・出力には AIX0188C が表示され、usrck -n ALL 性能確認 enhanced_RBAC 0188 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0188A が画面・出力に表示されること
② ステップ2 の AIX0188B が画面・出力に表示されること
③ ステップ3 の AIX0188C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0455"><h3>usrck -n ALL 性能確認 roles 0604</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 初級</p><p>若草採取ではAIX 7.3のセキュリティで usrck -n ALL を確認します。若草採取のセキュリティでは roles とユーザー属性を監査票へ転記します。若草採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若草採取の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、若草採取を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 性能確認 roles 0604の技術的な意味を資料で確認するとき、lsdev -Cc disk 起動確認 attribute 0605との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はセキュリティでusrck -n ALLを用い・roles とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はデバイス管理でlsdev -Cc diskを用い・attribute と診断対象表示を確認する。</li><li>C. 管理対象との関係を表す説明はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>D. 管理対象との関係を表す説明はJFS2でdefragfsを用い・agblksize とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「セキュリティでusrck -n ALLを用い、roles とユーザー属性を確認する」に対応する項目は性能確認 roles（性能・usrc）です。性能に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い、roles」で、確認対象はus・性能です。起動・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 attribute（起動・lsde）です。属性・受信・lparのC:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は属性照合 受信先（属性・lpar）です。属性・defrのD:は「JFS2でdefragfsを用い、agblksize」を述べ、対象は属性確認 agblksize（属性・defr）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い、roles」を指し、性能確認 rolesではus・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 性能確認 roles 0604</strong></p><p>検証目的: セキュリティのusrck -n ALL 性能確認 roles 0604について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ性能確認004-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0604A
画面・出力には AIX0604A が表示され、usrck -n ALL 性能確認 roles 0604 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0604B
画面・出力には AIX0604B が表示され、usrck -n ALL 性能確認 roles 0604 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0604C
画面・出力には AIX0604C が表示され、usrck -n ALL 性能確認 roles 0604 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0604A が画面・出力に表示されること
② ステップ2 の AIX0604B が画面・出力に表示されること
③ ステップ3 の AIX0604C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0456"><h3>usrck -n ALL 性能確認 roles 0664</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>霜月判定ではAIX 7.3のセキュリティで usrck -n ALL を確認します。霜月判定のセキュリティでは roles とユーザー属性を監査票へ転記します。霜月判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。霜月判定の注意点として RBACモード誤認 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、霜月判定を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 性能確認 roles 0664を同一分類のlsdev -Cc disk 起動確認 attribute 0665と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はデバイス管理でlsdev -Cc diskを用い・attribute と診断対象表示を確認する。</li><li>B. 管理対象との関係を表す説明は導入と起動でoslevel -sを用い・fileset level とOSレベル表示を確認する。</li><li>C. 管理対象との関係を表す説明はセキュリティでusrck -n ALLを用い・roles とユーザー属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はLVMでchvgを用い・VG STATE とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「セキュリティでusrck -n ALLを用い、roles とユーザー属性を確認する」に対応する項目は性能確認 roles（性能・usrc）です。性能に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い、roles」で、確認対象はus・性能です。起動・lsdeのA:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 attribute（起動・lsde）です。変更前・osleのB:は「導入と起動でoslevel -sを用い、fileset level」を述べ、対象はfileset level（変更・osle）です。属性・chvgのD:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（属性・chvg）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い、roles」を指し、性能確認 rolesではus・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 性能確認 roles 0664</strong></p><p>検証目的: セキュリティのusrck -n ALL 性能確認 roles 0664について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ性能確認064-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0664A
画面・出力には AIX0664A が表示され、usrck -n ALL 性能確認 roles 0664 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0664B
画面・出力には AIX0664B が表示され、usrck -n ALL 性能確認 roles 0664 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。roles を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0664C
画面・出力には AIX0664C が表示され、usrck -n ALL 性能確認 roles 0664 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0664A が画面・出力に表示されること
② ステップ2 の AIX0664B が画面・出力に表示されること
③ ステップ3 の AIX0664C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0457"><h3>usrck -n ALL 構成照合 audit class 0763</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>秋声復旧ではAIX 7.3のセキュリティで usrck -n ALL を確認します。秋声復旧のセキュリティでは audit class とロール一覧を点検票へ整理します。秋声復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。秋声復旧の注意点として ユーザー属性変更の根拠不足 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、秋声復旧を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 構成照合 audit class 0763について構成や状態を確認します。lsdev -Cc disk 変更前確認 path status 0764ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはデバイス管理でlsdev -Cc diskを用い・path status と構成マネージャー結果を確認する。</li><li>B. 対象資源に対する働きはネットワークでlsdev -Cc adapterを用い・Gateway とMTU属性を確認する。</li><li>C. 対象資源に対する働きはJFS2でdefragfsを用い・mountguard とログデバイス設定を確認する。</li><li>D. 対象資源に対する働きはセキュリティでusrck -n ALLを用い・audit class とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「セキュリティでusrck -n ALLを用い、audit class」に対応する項目はaudit class（構成・usrc）です。構成に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い、audit」で、確認対象はus・構成です。変更前・lsdeのA:は「デバイス管理でlsdev -Cc diskを用い、path」を述べ、対象はpath status（変更・lsde）です。監査・lsdeのB:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は監査記録 Gateway（監査・lsde）です。変更後・defrのC:は「JFS2でdefragfsを用い、mountguard」を述べ、対象は変更後確認 mountguard（変更・defr）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い、audit」を指し、audit classではus・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 構成照合 audit class 0763</strong></p><p>検証目的: セキュリティのusrck -n ALL 構成照合 audit class 0763について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ構成照合043-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0763A
画面・出力には AIX0763A が表示され、usrck -n ALL 構成照合 audit class 0763 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0763B
画面・出力には AIX0763B が表示され、usrck -n ALL 構成照合 audit class 0763 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0763C
画面・出力には AIX0763C が表示され、usrck -n ALL 構成照合 audit class 0763 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0763A が画面・出力に表示されること
② ステップ2 の AIX0763B が画面・出力に表示されること
③ ステップ3 の AIX0763C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0458"><h3>usrck -n ALL 構成照合 audit class 0823</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>新緑変更ではAIX 7.3のセキュリティで usrck -n ALL を確認します。新緑変更のセキュリティでは audit class とロール一覧を点検票へ整理します。新緑変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。新緑変更の注意点として ユーザー属性変更の根拠不足 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、新緑変更を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 構成照合 audit class 0823の設定や表示を読む前に役割を確認します。lparstat 詳細確認 保存場所ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。lparstat 詳細確認 保存場所固有の属性も確認対象に含める。</li><li>B. 対象資源に対する働きは性能管理でiostat -Dl 2 2を用い・po とsvmon全体表示を確認する。</li><li>C. 対象資源に対する働きはLVMでmigratepvを用い・LV STATE とボリュームグループ属性を確認する。</li><li>D. 対象資源に対する働きはセキュリティでusrck -n ALLを用い・audit class とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構成・usrcでDの記述「セキュリティでusrck -n ALLを用い、audit」に対応する項目はaudit class（構成・usrc）です。構成に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い、audit」で、確認対象はus・構成です。詳細・保存・lparのA:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は詳細確認 保存場所（詳細・lpar）です。性能・iostのB:は「性能管理でiostat -Dl 2 2を用い、po」を述べ、対象は性能確認 po（性能・iost）です。属性・migrのC:は「LVMでmigratepvを用い、LV STATE」を述べ、対象はLV STATE（属性・migr）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い、audit」を指し、audit classではus・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 構成照合 audit class 0823</strong></p><p>検証目的: セキュリティのusrck -n ALL 構成照合 audit class 0823について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ構成照合103-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0823A
画面・出力には AIX0823A が表示され、usrck -n ALL 構成照合 audit class 0823 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0823B
画面・出力には AIX0823B が表示され、usrck -n ALL 構成照合 audit class 0823 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0823C
画面・出力には AIX0823C が表示され、usrck -n ALL 構成照合 audit class 0823 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0823A が画面・出力に表示されること
② ステップ2 の AIX0823B が画面・出力に表示されること
③ ステップ3 の AIX0823C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0459"><h3>usrck -n ALL 構成照合 authorizations 0287</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>夕凪復旧ではAIX 7.3のセキュリティで usrck -n ALL を確認します。夕凪復旧のセキュリティでは authorizations とロール一覧を照合票へ整理します。夕凪復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。夕凪復旧の注意点として ユーザー属性変更の根拠不足 を避けるため lsuser user1 も併記します。権限管理の作業票として、夕凪復旧を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 構成照合 authorizations 0287の設定や表示を読む前に役割を確認します。lsdev -Cc disk 変更前確認 attribute 0288ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はセキュリティでusrck -n ALLを用い・authorizations とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的はデバイス管理でlsdev -Cc diskを用い・attribute と構成マネージャー結果を確認する。</li><li>C. 一次資料が示す主目的はSRCとログでerrclearを用い・PID とinetdデバッグ出力を確認する。</li><li>D. 一次資料が示す主目的はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでusrck -n ALLを用い、authorizations」に対応する項目は構成照合 authorization（構成・usrc）です。構成に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い」で、確認対象はus・構成です。変更前・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は変更前確認 attribute（変更・lsde）です。性能・errcのC:は「SRCとログでerrclearを用い、PID」を述べ、対象は性能確認 PID（性能・errc）です。一覧・保存・lparのD:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は一覧確認 保存場所（一覧・lpar）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い」を指し、構成照合 authorizationではus・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 構成照合 authorizations 0287</strong></p><p>検証目的: セキュリティのusrck -n ALL 構成照合 authorizations 0287について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ構成照合047-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0287A
画面・出力には AIX0287A が表示され、usrck -n ALL 構成照合 authorizations 0287 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0287B
画面・出力には AIX0287B が表示され、usrck -n ALL 構成照合 authorizations 0287 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0287C
画面・出力には AIX0287C が表示され、usrck -n ALL 構成照合 authorizations 0287 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0287A が画面・出力に表示されること
② ステップ2 の AIX0287B が画面・出力に表示されること
③ ステップ3 の AIX0287C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0460"><h3>usrck -n ALL 構成照合 authorizations 0347</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 上級</p><p>風花変更ではAIX 7.3のセキュリティで usrck -n ALL を確認します。風花変更のセキュリティでは authorizations とロール一覧を照合票へ整理します。風花変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。風花変更の注意点として ユーザー属性変更の根拠不足 を避けるため lsuser user1 も併記します。権限管理の作業票として、風花変更を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 構成照合 authorizations 0347について構成や状態を確認します。lsdev -Cc disk 変更前確認 attribute 0348ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はデバイス管理でlsdev -Cc diskを用い・attribute と構成マネージャー結果を確認する。</li><li>B. 一次資料が示す主目的はSRCとログでstartsrc -s inetd -aを用い・Statusである。</li><li>C. 一次資料が示す主目的はセキュリティでusrck -n ALLを用い・authorizations とロール一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はJFS2でcrfsを用い・isnapshot とログデバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「セキュリティでusrck -n ALLを用い、authorizations」に対応する項目は構成照合 authorization（構成・usrc）です。構成に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い」で、確認対象はus・構成です。変更前・lsdeのA:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は変更前確認 attribute（変更・lsde）です。起動・starのB:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は起動確認 Status（起動・star）です。障害切・crfsのD:は「JFS2でcrfsを用い、isnapshot」を述べ、対象は障害切り分け isnapshot（障害・crfs）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い」を指し、構成照合 authorizationではus・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 構成照合 authorizations 0347</strong></p><p>検証目的: セキュリティのusrck -n ALL 構成照合 authorizations 0347について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ構成照合107-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0347A
画面・出力には AIX0347A が表示され、usrck -n ALL 構成照合 authorizations 0347 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0347B
画面・出力には AIX0347B が表示され、usrck -n ALL 構成照合 authorizations 0347 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0347C
画面・出力には AIX0347C が表示され、usrck -n ALL 構成照合 authorizations 0347 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0347A が画面・出力に表示されること
② ステップ2 の AIX0347B が画面・出力に表示されること
③ ステップ3 の AIX0347C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0461"><h3>usrck -n ALL 運用引継ぎ audit class 0793</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>朝霧復旧ではAIX 7.3のセキュリティで usrck -n ALL を確認します。朝霧復旧のセキュリティでは audit class と監査設定を採取票へ記録します。朝霧復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。朝霧復旧の注意点として ロール割当と権限文字列の不一致 を避けるため rolelist -u user1 も併記します。権限管理の作業票として、朝霧復旧を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「usrck -n ALL 運用引継ぎ audit class 0793」を「chdev 変更前確認 識別値」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はデバイス属性を変更する管理コマンドである。</li><li>B. 保守作業で参照する機能はLVMでmklvを用い・PP SIZE とボリュームグループ属性を確認する。</li><li>C. 保守作業で参照する機能はJFS2でchfsを用い・ファイルシステム使用率 とマウントオプションを確認する。chfs バックアウト確認 ファイルシステム使用率 0577固有の属性も確認対象に含める。</li><li>D. 保守作業で参照する機能はセキュリティでusrck -n ALLを用い・audit class と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 運用引・usrcでDの記述「セキュリティでusrck -n ALLを用い、audit」に対応する項目はaudit class（運用・usrc）です。運用引に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い、audit」で、確認対象はus・運用引です。変更前・chdeのA:は「デバイス属性を変更する管理コマンド」を述べ、対象は変更前確認 識別値（変更・chde）です。障害切・mklvのB:は「LVMでmklvを用い、PP SIZE とボリュームグループ属性を確」を述べ、対象はPP SIZE（障害・mklv）です。バック・chfsのC:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象はバックアウト確認 ファイルシステム使（バッ・chfs）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い、audit」を指し、audit classではus・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 運用引継ぎ audit class 0793</strong></p><p>検証目的: セキュリティのusrck -n ALL 運用引継ぎ audit class 0793について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ運用引継ぎ073-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0793A
画面・出力には AIX0793A が表示され、usrck -n ALL 運用引継ぎ audit class 0793 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsuser user1
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0793B
画面・出力には AIX0793B が表示され、usrck -n ALL 運用引継ぎ audit class 0793 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。audit class を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0793C
画面・出力には AIX0793C が表示され、usrck -n ALL 運用引継ぎ audit class 0793 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0793A が画面・出力に表示されること
② ステップ2 の AIX0793B が画面・出力に表示されること
③ ステップ3 の AIX0793C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0462"><h3>usrck -n ALL 運用引継ぎ authorizations 0317</h3><p class="kb-meta">分類: セキュリティ ・ 難易度: 中級</p><p>冬晴復旧ではAIX 7.3のセキュリティで usrck -n ALL を確認します。冬晴復旧のセキュリティでは authorizations と監査設定を復旧票へ残します。冬晴復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。冬晴復旧の注意点として ロール割当と権限文字列の不一致 を避けるため lsuser user1 も併記します。権限管理の作業票として、冬晴復旧を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> usrck -n ALL 運用引継ぎ authorizations 0317を保守記録に説明する必要があります。lsdev -Cc disk 容量確認 microcode level 0318と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はセキュリティでusrck -n ALLを用い・authorizations と監査設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割はデバイス管理でlsdev -Cc diskを用い・microcode level とデバイス一覧を確認する。</li><li>C. 仕様上の役割はSRCとログでstartsrc -s inetd -aを用い・syslog.confである。</li><li>D. 仕様上の役割はJFS2でcrfsを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「セキュリティでusrck -n ALLを用い、authorizations」に対応する項目は運用引継ぎ authorizatio（運用・usrc）です。運用引に関するセキュリティの仕様は「セキュリティでusrck -n ALLを用い」で、確認対象はus・運用引です。容量・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象はmicrocode level（容量・lsde）です。障害切・starのC:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け syslog.conf（障害・star）です。起動・ファ・crfsのD:は「JFS2でcrfsを用い、ファイルシステム使用率」を述べ、対象は起動確認 ファイルシステム使用率（起動・crfs）です。「usrck -n ALL」は「セキュリティでusrck -n ALLを用い」を指し、運用引継ぎ authorizatioではus・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>usrck -n ALL 運用引継ぎ authorizations 0317</strong></p><p>検証目的: セキュリティのusrck -n ALL 運用引継ぎ authorizations 0317について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=セキュリティ運用引継ぎ077-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; usrck -n ALL
→ Enter を押す
［画面・出力］
attribute     value      description
 enhanced_RBAC true       Enhanced RBAC mode
確認コード AIX0317A
画面・出力には AIX0317A が表示され、usrck -n ALL 運用引継ぎ authorizations 0317 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsrole ALL
→ Enter を押す
［画面・出力］
rolelist output for user1
SysInfo          System Information Retrieval
UserAdmin        User Administration
確認コード AIX0317B
画面・出力には AIX0317B が表示され、usrck -n ALL 運用引継ぎ authorizations 0317 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。authorizations を読むため、セキュリティ の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; rolelist -u user1
→ Enter を押す
［画面・出力］
authorizations=aix.security.user,aix.security.role
roles=UserAdmin,SysInfo
確認コード AIX0317C
画面・出力には AIX0317C が表示され、usrck -n ALL 運用引継ぎ authorizations 0317 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0317A が画面・出力に表示されること
② ステップ2 の AIX0317B が画面・出力に表示されること
③ ステップ3 の AIX0317C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


## デバイス管理


<section class="kb-item" id="c01-i0463"><h3>bootinfo -B hdisk0 変更前確認 PVID 0514</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>銀嶺確認ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。銀嶺確認のデバイス管理では PVID とデバイス一覧を保守票へ記録します。銀嶺確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。銀嶺確認の注意点として 構成再検出前の判断 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、銀嶺確認を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootinfo -B hdisk0 変更前確認 PVID 0514の役割を調べています。chvg 変更後確認 STALE PARTITIONS 0515の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はデバイス管理でbootinfo -B hdisk0を用い・PVID とデバイス一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はLVMでchvgを用い・STALE PARTITIONS とボリュームグループ属性を確認する。chvg 変更後確認 STALE PARTITIONS 0515固有の属性も確認対象に含める。</li><li>C. 表示や設定で扱う内容は導入と起動でmksysbを用い・EFIX LABEL と代替ディスク状態を確認する。</li><li>D. 表示や設定で扱う内容はSRCとログでstartsrc -s inetd -aを用い・IDENTIFIERである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「デバイス管理でbootinfo -B hdisk0を用い、PVID」に対応する項目は変更前確認 PVID（変更・boot）です。変更前に関するデバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い、PVID」で、確認対象はbo・変更前です。変更後・chvgのB:は「LVMでchvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（変更・chvg）です。起動・mksyのC:は「導入と起動でmksysbを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（起動・mksy）です。障害切・starのD:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け IDENTIFIER（障害・star）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を指し、変更前確認 PVIDではbo・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 変更前確認 PVID 0514</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 変更前確認 PVID 0514について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理変更前確認034-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0514A
画面・出力には AIX0514A が表示され、bootinfo -B hdisk0 変更前確認 PVID 0514 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0514B
画面・出力には AIX0514B が表示され、bootinfo -B hdisk0 変更前確認 PVID 0514 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0514C
画面・出力には AIX0514C が表示され、bootinfo -B hdisk0 変更前確認 PVID 0514 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0514A が画面・出力に表示されること
② ステップ2 の AIX0514B が画面・出力に表示されること
③ ステップ3 の AIX0514C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0464"><h3>bootinfo -B hdisk0 変更前確認 location code 0038</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>春霞確認ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。春霞確認のデバイス管理では location code とデバイス一覧を確認票へ整理します。春霞確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。春霞確認の注意点として 構成再検出前の判断 を避けるため lscfg -vl ent0 も併記します。デバイス構成管理の作業票として、春霞確認を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootinfo -B hdisk0 変更前確認 location code 0038に関する障害切り分けの前提を確認しています。chvg 変更後確認 LV STATE 0039の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はLVMでchvgを用い・LV STATE とボリュームグループ属性を確認する。</li><li>B. 障害切り分けに用いる役割はデバイス管理でbootinfo -B hdisk0を用い・location codeである。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割は導入と起動でmksysbを用い・Technology Level と代替ディスク状態を確認する。</li><li>D. 障害切り分けに用いる役割はLVMでmirrorvgを用い・VG STATE とボリュームグループ属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「デバイス管理でbootinfo -B hdisk0を用い、location」に対応する項目はlocation code（変更・boot）です。デバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い」で、確認対象はbo・変更前です。変更後・chvgのA:は「LVMでchvgを用い、LV STATE」を述べ、対象はLV STATE（変更・chvg）です。起動・mksyのC:は「導入と起動でmksysbを用い、Technology Level」を述べ、対象はTechnology Level（起動・mksy）です。容量・mirrのD:は「LVMでmirrorvgを用い、VG STATE」を述べ、対象はVG STATE（容量・mirr）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い」を指し、location codeではbo・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 変更前確認 location code 0038</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 変更前確認 location code 0038について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理変更前確認038-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0038A
画面・出力には AIX0038A が表示され、bootinfo -B hdisk0 変更前確認 location code 0038 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0038B
画面・出力には AIX0038B が表示され、bootinfo -B hdisk0 変更前確認 location code 0038 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0038C
画面・出力には AIX0038C が表示され、bootinfo -B hdisk0 変更前確認 location code 0038 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0038A が画面・出力に表示されること
② ステップ2 の AIX0038B が画面・出力に表示されること
③ ステップ3 の AIX0038C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0465"><h3>bootinfo -B hdisk0 容量確認 Available 0484</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 初級</p><p>若草確認ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。若草確認のデバイス管理では Available と構成マネージャー結果を監査票へ転記します。若草確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。若草確認の注意点として DefinedとAvailableの混同 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、若草確認を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootinfo -B hdisk0 容量確認 Available 0484の技術的な意味を資料で確認するとき、chvg 性能確認 VG STATE 0485との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はデバイス管理でbootinfo -B hdisk0を用い・Availableである。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はLVMでchvgを用い・VG STATE とミラーコピー状態を確認する。</li><li>C. 管理対象との関係を表す説明は導入と起動でmksysbを用い・mksysb image とOSレベル表示を確認する。</li><li>D. 管理対象との関係を表す説明はSRCとログでstartsrc -s inetd -aを用い・Subsystemである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「デバイス管理でbootinfo -B hdisk0を用い、Availableである」に対応する項目は容量確認 Available（容量・boot）です。容量に関するデバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い」で、確認対象はbo・容量です。性能・chvgのB:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（性能・chvg）です。障害切・mksyのC:は「導入と起動でmksysbを用い、mksysb image」を述べ、対象はmksysb image（障害・mksy）です。起動・starのD:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は起動確認 Subsystem（起動・star）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い」を指し、容量確認 Availableではbo・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 容量確認 Available 0484</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 容量確認 Available 0484について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理容量確認004-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0484A
画面・出力には AIX0484A が表示され、bootinfo -B hdisk0 容量確認 Available 0484 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0484B
画面・出力には AIX0484B が表示され、bootinfo -B hdisk0 容量確認 Available 0484 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0484C
画面・出力には AIX0484C が表示され、bootinfo -B hdisk0 容量確認 Available 0484 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0484A が画面・出力に表示されること
② ステップ2 の AIX0484B が画面・出力に表示されること
③ ステップ3 の AIX0484C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0466"><h3>bootinfo -B hdisk0 容量確認 path status 0008</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 初級</p><p>翠風確認ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。翠風確認のデバイス管理では path status と構成マネージャー結果を引継ぎ票へ保管します。翠風確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。翠風確認の注意点として DefinedとAvailableの混同 を避けるため lscfg -vl ent0 も併記します。デバイス構成管理の作業票として、翠風確認を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootinfo -B hdisk0 容量確認 path status 0008を同一分類のchvg 性能確認 MIRROR WRITE CONSISTENCY 0009と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はLVMでchvgを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。</li><li>B. コマンドまたは機能の用途はデバイス管理でbootinfo -B hdisk0を用い・path statusである。 <span class="kb-ok">✅ 正解</span></li><li>C. コマンドまたは機能の用途は導入と起動でmksysbを用い・bootlist とOSレベル表示を確認する。</li><li>D. コマンドまたは機能の用途はLVMでmirrorvgを用い・STALE PARTITIONS とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「デバイス管理でbootinfo -B hdisk0を用い、path」に対応する項目はpath status（容量・boot）です。デバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い、path」で、確認対象はbo・容量です。性能・chvgのA:は「LVMでchvgを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（性能・chvg）です。障害切・mksyのC:は「導入と起動でmksysbを用い、bootlist」を述べ、対象は障害切り分け bootlist（障害・mksy）です。変更前・mirrのD:は「LVMでmirrorvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（変更・mirr）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い、path」を指し、path statusではbo・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 容量確認 path status 0008</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 容量確認 path status 0008について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理容量確認008-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0008A
画面・出力には AIX0008A が表示され、bootinfo -B hdisk0 容量確認 path status 0008 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0008B
画面・出力には AIX0008B が表示され、bootinfo -B hdisk0 容量確認 path status 0008 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0008C
画面・出力には AIX0008C が表示され、bootinfo -B hdisk0 容量確認 path status 0008 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0008A が画面・出力に表示されること
② ステップ2 の AIX0008B が画面・出力に表示されること
③ ステップ3 の AIX0008C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0467"><h3>bootinfo -B hdisk0 状態確認 PVID 0643</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>秋声判定ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。秋声判定のデバイス管理では PVID とODM属性を点検票へ整理します。秋声判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。秋声判定の注意点として パス状態と物理障害の混同 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、秋声判定を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootinfo -B hdisk0 状態確認 PVID 0643について構成や状態を確認します。chvg 構成照合 PP SIZE 0644ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはLVMでchvgを用い・PP SIZE と論理ボリューム配置を確認する。</li><li>B. 対象資源に対する働きは性能管理でvmo -aを用い・Busy% とAME統計を確認する。</li><li>C. 対象資源に対する働きはSRCとログでstartsrc -s inetd -aを用い・Status とsyslog設定変換を確認する。</li><li>D. 対象資源に対する働きはデバイス管理でbootinfo -B hdisk0を用い・PVID とODM属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「デバイス管理でbootinfo -B hdisk0を用い、PVID」に対応する項目は状態確認 PVID（状態・boot）です。状態に関するデバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い、PVID」で、確認対象はbo・状態です。構成・chvgのA:は「LVMでchvgを用い、PP SIZE と論理ボリューム配置を確認す」を述べ、対象はPP SIZE（構成・chvg）です。バック・vmoのB:は「性能管理でvmo -aを用い、Busy% とAME統計を確認する」を述べ、対象はバックアウト確認 Busy%（バッ・vmo）です。変更前・starのC:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は変更前確認 Status（変更・star）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を指し、状態確認 PVIDではbo・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 状態確認 PVID 0643</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 状態確認 PVID 0643について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理状態確認043-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0643A
画面・出力には AIX0643A が表示され、bootinfo -B hdisk0 状態確認 PVID 0643 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0643B
画面・出力には AIX0643B が表示され、bootinfo -B hdisk0 状態確認 PVID 0643 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0643C
画面・出力には AIX0643C が表示され、bootinfo -B hdisk0 状態確認 PVID 0643 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0643A が画面・出力に表示されること
② ステップ2 の AIX0643B が画面・出力に表示されること
③ ステップ3 の AIX0643C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0468"><h3>bootinfo -B hdisk0 状態確認 PVID 0703</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 上級</p><p>新緑保守ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。新緑保守のデバイス管理では PVID とODM属性を点検票へ整理します。新緑保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。新緑保守の注意点として パス状態と物理障害の混同 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、新緑保守を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootinfo -B hdisk0 状態確認 PVID 0703の設定や表示を読む前に役割を確認します。chvg 構成照合 PP SIZE 0704ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはLVMでchvgを用い・PP SIZE と論理ボリューム配置を確認する。chvg 構成照合 PP SIZE 0704固有の属性も確認対象に含める。</li><li>B. 対象資源に対する働きは性能管理でvmo -aを用い・avm とAME統計を確認する。</li><li>C. 対象資源に対する働きはデバイス管理でbootinfo -B hdisk0を用い・PVID とODM属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「デバイス管理でbootinfo -B hdisk0を用い、PVID」に対応する項目は状態確認 PVID（状態・boot）です。状態に関するデバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い、PVID」で、確認対象はbo・状態です。構成・chvgのA:は「LVMでchvgを用い、PP SIZE と論理ボリューム配置を確認す」を述べ、対象はPP SIZE（構成・chvg）です。バック・vmoのB:は「性能管理でvmo -aを用い、avm とAME統計を確認する」を述べ、対象はバックアウト確認 avm（バッ・vmo）です。変更後・tailのD:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は変更後確認 IDENTIFIER（変更・tail）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い、PVID」を指し、状態確認 PVIDではbo・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 状態確認 PVID 0703</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 状態確認 PVID 0703について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理状態確認103-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0703A
画面・出力には AIX0703A が表示され、bootinfo -B hdisk0 状態確認 PVID 0703 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0703B
画面・出力には AIX0703B が表示され、bootinfo -B hdisk0 状態確認 PVID 0703 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0703C
画面・出力には AIX0703C が表示され、bootinfo -B hdisk0 状態確認 PVID 0703 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0703A が画面・出力に表示されること
② ステップ2 の AIX0703B が画面・出力に表示されること
③ ステップ3 の AIX0703C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0469"><h3>bootinfo -B hdisk0 状態確認 location code 0167</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>夕凪判定ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。夕凪判定のデバイス管理では location code とODM属性を照合票へ整理します。夕凪判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。夕凪判定の注意点として パス状態と物理障害の混同 を避けるため lscfg -vl ent0 も併記します。デバイス構成管理の作業票として、夕凪判定を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootinfo -B hdisk0 状態確認 location code 0167の設定や表示を読む前に役割を確認します。chvg 構成照合 VG STATE 0168ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はデバイス管理でbootinfo -B hdisk0を用い・location code とODM属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的はLVMでchvgを用い・VG STATE と論理ボリューム配置を確認する。chvg 構成照合 VG STATE 0168固有の属性も確認対象に含める。</li><li>C. 一次資料が示す主目的は導入と起動でmksysbを用い・Technology Level と起動デバイス設定を確認する。</li><li>D. 一次資料が示す主目的はLVMでmirrorvgを用い・PVID と論理ボリューム配置を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「デバイス管理でbootinfo -B hdisk0を用い、location」に対応する項目はlocation code（状態・boot）です。状態に関するデバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い」で、確認対象はbo・状態です。構成・chvgのB:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（構成・chvg）です。容量・mksyのC:は「導入と起動でmksysbを用い、Technology Level」を述べ、対象はTechnology Level（容量・mksy）です。監査・mirrのD:は「LVMでmirrorvgを用い、PVID」を述べ、対象は監査記録 PVID（監査・mirr）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い」を指し、location codeではbo・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 状態確認 location code 0167</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 状態確認 location code 0167について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理状態確認047-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0167A
画面・出力には AIX0167A が表示され、bootinfo -B hdisk0 状態確認 location code 0167 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0167B
画面・出力には AIX0167B が表示され、bootinfo -B hdisk0 状態確認 location code 0167 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0167C
画面・出力には AIX0167C が表示され、bootinfo -B hdisk0 状態確認 location code 0167 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0167A が画面・出力に表示されること
② ステップ2 の AIX0167B が画面・出力に表示されること
③ ステップ3 の AIX0167C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0470"><h3>bootinfo -B hdisk0 状態確認 location code 0227</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 上級</p><p>風花保守ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。風花保守のデバイス管理では location code とODM属性を照合票へ整理します。風花保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。風花保守の注意点として パス状態と物理障害の混同 を避けるため lscfg -vl ent0 も併記します。デバイス構成管理の作業票として、風花保守を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootinfo -B hdisk0 状態確認 location code 0227について構成や状態を確認します。chvg 構成照合 VG STATE 0228ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はLVMでchvgを用い・VG STATE と論理ボリューム配置を確認する。</li><li>B. 一次資料が示す主目的はデバイス管理でbootinfo -B hdisk0を用い・location code とODM属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 一次資料が示す主目的は導入と起動でbosboot -a -dを用い・fileset level と起動デバイス設定を確認する。bosboot -a -d 性能確認 fileset level固有の属性も確認対象に含める。</li><li>D. 一次資料が示す主目的はLVMでmirrorvgを用い・PVID と論理ボリューム配置を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「デバイス管理でbootinfo -B hdisk0を用い、location」に対応する項目はlocation code（状態・boot）です。状態に関するデバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い」で、確認対象はbo・状態です。構成・chvgのA:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（構成・chvg）です。性能・bosbのC:は「導入と起動でbosboot -a -dを用い、fileset」を述べ、対象はfileset level（性能・bosb）です。監査・mirrのD:は「LVMでmirrorvgを用い、PVID」を述べ、対象は監査記録 PVID（監査・mirr）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い」を指し、location codeではbo・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 状態確認 location code 0227</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 状態確認 location code 0227について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理状態確認107-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0227A
画面・出力には AIX0227A が表示され、bootinfo -B hdisk0 状態確認 location code 0227 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0227B
画面・出力には AIX0227B が表示され、bootinfo -B hdisk0 状態確認 location code 0227 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0227C
画面・出力には AIX0227C が表示され、bootinfo -B hdisk0 状態確認 location code 0227 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0227A が画面・出力に表示されること
② ステップ2 の AIX0227B が画面・出力に表示されること
③ ステップ3 の AIX0227C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0471"><h3>bootinfo -B hdisk0 監査記録 Available 0673</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>朝霧判定ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。朝霧判定のデバイス管理では Available と診断対象表示を採取票へ記録します。朝霧判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。朝霧判定の注意点として ODM属性の更新反映漏れ を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、朝霧判定を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「bootinfo -B hdisk0 監査記録 Available 0673」を「chvg 運用引継ぎ PVID 0674」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はLVMでchvgを用い・PVID と物理ボリューム一覧を確認する。chvg 運用引継ぎ PVID 0674固有の属性も確認対象に含める。</li><li>B. 保守作業で参照する機能は性能管理でvmo -aを用い・po とsvmon全体表示を確認する。</li><li>C. 保守作業で参照する機能はデバイス管理でbootinfo -B hdisk0を用い・Available と診断対象表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はSRCとログでtail -f /tmp/myfileを用い・Subsystemである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「デバイス管理でbootinfo -B hdisk0を用い、Available」に対応する項目は監査記録 Available（監査・boot）です。監査に関するデバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い」で、確認対象はbo・監査です。運用引・chvgのA:は「LVMでchvgを用い、PVID と物理ボリューム一覧を確認する」を述べ、対象は運用引継ぎ PVID（運用・chvg）です。属性・vmoのB:は「性能管理でvmo -aを用い、po とsvmon全体表示を確認する」を述べ、対象は属性確認 po（属性・vmo）です。性能・tailのD:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は性能確認 Subsystem（性能・tail）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い」を指し、監査記録 Availableではbo・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 監査記録 Available 0673</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 監査記録 Available 0673について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理監査記録073-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0673A
画面・出力には AIX0673A が表示され、bootinfo -B hdisk0 監査記録 Available 0673 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0673B
画面・出力には AIX0673B が表示され、bootinfo -B hdisk0 監査記録 Available 0673 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0673C
画面・出力には AIX0673C が表示され、bootinfo -B hdisk0 監査記録 Available 0673 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0673A が画面・出力に表示されること
② ステップ2 の AIX0673B が画面・出力に表示されること
③ ステップ3 の AIX0673C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0472"><h3>bootinfo -B hdisk0 監査記録 path status 0197</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>冬晴判定ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。冬晴判定のデバイス管理では path status と診断対象表示を復旧票へ残します。冬晴判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。冬晴判定の注意点として ODM属性の更新反映漏れ を避けるため lscfg -vl ent0 も併記します。デバイス構成管理の作業票として、冬晴判定を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootinfo -B hdisk0 監査記録 path status 0197を保守記録に説明する必要があります。chvg 運用引継ぎ STALE PARTITIONS 0198と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はLVMでchvgを用い・STALE PARTITIONS と物理ボリューム一覧を確認する。chvg 運用引継ぎ STALE PARTITIONS 0198固有の属性も確認対象に含める。</li><li>B. 仕様上の役割はデバイス管理でbootinfo -B hdisk0を用い・path status と診断対象表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割は導入と起動でbosboot -a -dを用い・altinst_rootvg とfileset一覧を確認する。</li><li>D. 仕様上の役割はLVMでmirrorvgを用い・PP SIZE と物理ボリューム一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「デバイス管理でbootinfo -B hdisk0を用い、path status」に対応する項目はpath status（監査・boot）です。監査に関するデバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い、path」で、確認対象はbo・監査です。運用引・chvgのA:は「LVMでchvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（運用・chvg）です。変更後・bosbのC:は「導入と起動でbosboot -a -dを用い」を述べ、対象は変更後確認 altinst_root（変更・bosb）です。状態・mirrのD:は「LVMでmirrorvgを用い、PP SIZE」を述べ、対象はPP SIZE（状態・mirr）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い、path」を指し、path statusではbo・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 監査記録 path status 0197</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 監査記録 path status 0197について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理監査記録077-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0197A
画面・出力には AIX0197A が表示され、bootinfo -B hdisk0 監査記録 path status 0197 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0197B
画面・出力には AIX0197B が表示され、bootinfo -B hdisk0 監査記録 path status 0197 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0197C
画面・出力には AIX0197C が表示され、bootinfo -B hdisk0 監査記録 path status 0197 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0197A が画面・出力に表示されること
② ステップ2 の AIX0197B が画面・出力に表示されること
③ ステップ3 の AIX0197C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0473"><h3>bootinfo -B hdisk0 起動確認 Available 0356</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 上級</p><p>若潮変更ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。若潮変更のデバイス管理では Available と構成マネージャー結果を引継ぎ票へ保管します。若潮変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。若潮変更の注意点として DefinedとAvailableの混同 を避けるため lscfg -vl ent0 も併記します。デバイス構成管理の作業票として、若潮変更を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootinfo -B hdisk0 起動確認 Available 0356の技術的な意味を資料で確認するとき、chvg 属性確認 VG STATE 0357との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はLVMでchvgを用い・VG STATE とミラーコピー状態を確認する。</li><li>B. コマンドまたは機能の用途は導入と起動でbosboot -a -dを用い・Technology Level とOSレベル表示を確認する。</li><li>C. コマンドまたは機能の用途はSRCとログでtail -f /tmp/myfileを用い・PID とinetdデバッグ出力を確認する。</li><li>D. コマンドまたは機能の用途はデバイス管理でbootinfo -B hdisk0を用い・Availableである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「デバイス管理でbootinfo -B hdisk0を用い、Availableである」に対応する項目は起動確認 Available（起動・boot）です。起動に関するデバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い」で、確認対象はbo・起動です。属性・chvgのA:は「LVMでchvgを用い、VG STATE」を述べ、対象はVG STATE（属性・chvg）です。運用引・bosbのB:は「導入と起動でbosboot -a -dを用い、Technology」を述べ、対象はTechnology Level（運用・bosb）です。構成・tailのC:は「SRCとログでtail -f /tmp/myfileを用い、PID」を述べ、対象は構成照合 PID（構成・tail）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い」を指し、起動確認 Availableではbo・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 起動確認 Available 0356</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 起動確認 Available 0356について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理起動確認116-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0356A
画面・出力には AIX0356A が表示され、bootinfo -B hdisk0 起動確認 Available 0356 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0356B
画面・出力には AIX0356B が表示され、bootinfo -B hdisk0 起動確認 Available 0356 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0356C
画面・出力には AIX0356C が表示され、bootinfo -B hdisk0 起動確認 Available 0356 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0356A が画面・出力に表示されること
② ステップ2 の AIX0356B が画面・出力に表示されること
③ ステップ3 の AIX0356C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0474"><h3>bootinfo -B hdisk0 起動確認 attribute 0832</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 上級</p><p>夕映変更ではAIX 7.3のデバイス管理で bootinfo -B hdisk0 を確認します。夕映変更のデバイス管理では attribute と構成マネージャー結果を監査票へ転記します。夕映変更は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。夕映変更の注意点として DefinedとAvailableの混同 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、夕映変更を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> bootinfo -B hdisk0 起動確認 attribute 0832を同一分類のlsfs -q 変更前確認 agblksize 0002と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はJFS2でlsfs -qを用い・agblksize とファイルシステム属性を確認する。</li><li>B. 管理対象との関係を表す説明はデバイス管理でbootinfo -B hdisk0を用い・attributeである。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はJFS2でlogformを用い・log=INLINE とマウントオプションを確認する。</li><li>D. 管理対象との関係を表す説明はセキュリティでusrck -n ALLを用い・roles とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 起動・bootでBの記述「デバイス管理でbootinfo -B hdisk0を用い」に対応する項目は起動確認 attribute（起動・boot）です。起動に関するデバイス管理の仕様は「デバイス管理でbootinfo -B hdisk0を用い」で、確認対象はbo・起動です。変更前・lsfsのA:は「JFS2でlsfs -qを用い、agblksize」を述べ、対象は変更前確認 agblksize（変更・lsfs）です。起動・logfのC:は「JFS2でlogformを用い、log=INLINE」を述べ、対象は起動確認 log=INLINE（起動・logf）です。性能・usrcのD:は「セキュリティでusrck -n ALLを用い、roles」を述べ、対象は性能確認 roles（性能・usrc）です。「bootinfo -B hdisk0」は「デバイス管理でbootinfo -B hdisk0を用い」を指し、起動確認 attributeではbo・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>bootinfo -B hdisk0 起動確認 attribute 0832</strong></p><p>検証目的: デバイス管理のbootinfo -B hdisk0 起動確認 attribute 0832について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理起動確認112-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0832A
画面・出力には AIX0832A が表示され、bootinfo -B hdisk0 起動確認 attribute 0832 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0832B
画面・出力には AIX0832B が表示され、bootinfo -B hdisk0 起動確認 attribute 0832 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0832C
画面・出力には AIX0832C が表示され、bootinfo -B hdisk0 起動確認 attribute 0832 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0832A が画面・出力に表示されること
② ステップ2 の AIX0832B が画面・出力に表示されること
③ ステップ3 の AIX0832C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0475"><h3>cfgmgr バックアウト確認 PVID 0053</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>月影照合ではAIX 7.3のデバイス管理で cfgmgr を確認します。月影照合のデバイス管理では PVID と診断対象表示を復旧票へ残します。月影照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる欄にします。月影照合の注意点として ODM属性の更新反映漏れ を避けるため lscfg -vl ent0 も併記します。デバイス構成管理の作業票として、月影照合を判定結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> cfgmgr バックアウト確認 PVID 0053を保守記録に説明する必要があります。mklv 監査記録 PP SIZE 0054と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はLVMでmklvを用い・PP SIZE と物理ボリューム一覧を確認する。</li><li>B. 仕様上の役割は導入と起動でlslpp -Lを用い・EFIX LABEL とfileset一覧を確認する。</li><li>C. 仕様上の役割はデバイス管理でcfgmgrを用い・PVID と診断対象表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 仕様上の役割はLVMでlsvgを用い・LV STATE と物理ボリューム一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「デバイス管理でcfgmgrを用い、PVID と診断対象表示を確認する」に対応する項目はバックアウト確認 PVID（バッ・cfgm）です。デバイス管理の仕様は「デバイス管理でcfgmgrを用い、PVID と診断対象表示を確認する」で、確認対象はcf・バックです。監査・mklvのA:は「LVMでmklvを用い、PP SIZE と物理ボリューム一覧を確認す」を述べ、対象はPP SIZE（監査・mklv）です。構成・lslpのB:は「導入と起動でlslpp -Lを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（構成・lslp）です。属性・lsvgのD:は「LVMでlsvgを用い、LV STATE」を述べ、対象はLV STATE（属性・lsvg）です。「cfgmgr」は「デバイス管理でcfgmgrを用い、PVID と診断対象表示を確認する」を指し、バックアウト確認 PVIDではcf・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cfgmgr バックアウト確認 PVID 0053</strong></p><p>検証目的: デバイス管理のcfgmgr バックアウト確認 PVID 0053について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理バックアウト確認053-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; cfgmgr
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0053A
画面・出力には AIX0053A が表示され、cfgmgr バックアウト確認 PVID 0053 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0053B
画面・出力には AIX0053B が表示され、cfgmgr バックアウト確認 PVID 0053 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0053C
画面・出力には AIX0053C が表示され、cfgmgr バックアウト確認 PVID 0053 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0053A が画面・出力に表示されること
② ステップ2 の AIX0053B が画面・出力に表示されること
③ ステップ3 の AIX0053C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0476"><h3>cfgmgr バックアウト確認 microcode level 0529</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>銀砂照合ではAIX 7.3のデバイス管理で cfgmgr を確認します。銀砂照合のデバイス管理では microcode level と診断対象表示を採取票へ記録します。銀砂照合は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。銀砂照合の注意点として ODM属性の更新反映漏れ を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、銀砂照合を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「cfgmgr バックアウト確認 microcode level 0529」を「mklv 監査記録 MIRROR WRITE CONSISTENCY 0530」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はLVMでmklvを用い・MIRROR WRITE CONSISTENCY と物理ボリューム一覧を確認する。</li><li>B. 保守作業で参照する機能は導入と起動でlslpp -Lを用い・altinst_rootvg とfileset一覧を確認する。</li><li>C. 保守作業で参照する機能はデバイス管理でcfgmgrを用い・microcode level と診断対象表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はSRCとログでsyslog_ssw -cを用い・TIMESTAMP とSRCサブシステム表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「デバイス管理でcfgmgrを用い、microcode level」に対応する項目はmicrocode level（バッ・cfgm）です。バックに関するデバイス管理の仕様は「デバイス管理でcfgmgrを用い、microcode level」で、確認対象はcf・バックです。監査・mklvのA:は「LVMでmklvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（監査・mklv）です。構成・lslpのB:は「導入と起動でlslpp -Lを用い、altinst_rootvg」を述べ、対象は構成照合 altinst_rootv（構成・lslp）です。運用引・syslのD:は「SRCとログでsyslog_ssw -cを用い、TIMESTAMP」を述べ、対象は運用引継ぎ TIMESTAMP（運用・sysl）です。「cfgmgr」は「デバイス管理でcfgmgrを用い、microcode level」を指し、microcode levelではcf・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cfgmgr バックアウト確認 microcode level 0529</strong></p><p>検証目的: デバイス管理のcfgmgr バックアウト確認 microcode level 0529について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理バックアウト確認049-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。microcode level を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; cfgmgr
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0529A
画面・出力には AIX0529A が表示され、cfgmgr バックアウト確認 microcode level 0529 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。microcode level を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0529B
画面・出力には AIX0529B が表示され、cfgmgr バックアウト確認 microcode level 0529 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。microcode level を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0529C
画面・出力には AIX0529C が表示され、cfgmgr バックアウト確認 microcode level 0529 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0529A が画面・出力に表示されること
② ステップ2 の AIX0529B が画面・出力に表示されること
③ ステップ3 の AIX0529C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0477"><h3>cfgmgr 変更後確認 attribute 0182</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>紅葉判定ではAIX 7.3のデバイス管理で cfgmgr を確認します。紅葉判定のデバイス管理では attribute とデバイス一覧を確認票へ整理します。紅葉判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる根拠にします。紅葉判定の注意点として 構成再検出前の判断 を避けるため lscfg -vl ent0 も併記します。デバイス構成管理の作業票として、紅葉判定を点検結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> cfgmgr 変更後確認 attribute 0182に関する障害切り分けの前提を確認しています。mklv 障害切り分け PP SIZE 0183の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はデバイス管理でcfgmgrを用い・attribute とデバイス一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 障害切り分けに用いる役割はLVMでmklvを用い・PP SIZE とボリュームグループ属性を確認する。</li><li>C. 障害切り分けに用いる役割は導入と起動でinstallp -Cを用い・EFIX LABEL と代替ディスク状態を確認する。</li><li>D. 障害切り分けに用いる役割はLVMでlsvgを用い・LV STATE とボリュームグループ属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「デバイス管理でcfgmgrを用い、attribute とデバイス一覧を確認する」に対応する項目は変更後確認 attribute（変更・cfgm）です。変更後に関するデバイス管理の仕様は「デバイス管理でcfgmgrを用い、attribute」で、確認対象はcf・変更後です。障害切・mklvのB:は「LVMでmklvを用い、PP SIZE とボリュームグループ属性を確」を述べ、対象はPP SIZE（障害・mklv）です。状態・instのC:は「導入と起動でinstallp -Cを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（状態・inst）です。性能・lsvgのD:は「LVMでlsvgを用い、LV STATE」を述べ、対象はLV STATE（性能・lsvg）です。「cfgmgr」は「デバイス管理でcfgmgrを用い、attribute」を指し、変更後確認 attributeではcf・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cfgmgr 変更後確認 attribute 0182</strong></p><p>検証目的: デバイス管理のcfgmgr 変更後確認 attribute 0182について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理変更後確認062-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; cfgmgr
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0182A
画面・出力には AIX0182A が表示され、cfgmgr 変更後確認 attribute 0182 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0182B
画面・出力には AIX0182B が表示され、cfgmgr 変更後確認 attribute 0182 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0182C
画面・出力には AIX0182C が表示され、cfgmgr 変更後確認 attribute 0182 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0182A が画面・出力に表示されること
② ステップ2 の AIX0182B が画面・出力に表示されること
③ ステップ3 の AIX0182C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0478"><h3>cfgmgr 変更後確認 path status 0658</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>潮騒判定ではAIX 7.3のデバイス管理で cfgmgr を確認します。潮騒判定のデバイス管理では path status とデバイス一覧を保守票へ記録します。潮騒判定は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。潮騒判定の注意点として 構成再検出前の判断 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、潮騒判定を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> cfgmgr 変更後確認 path status 0658の役割を調べています。mklv 障害切り分け MIRROR WRITE CONSISTENCY 0659の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はデバイス管理でcfgmgrを用い・path status とデバイス一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はLVMでmklvを用い・MIRROR WRITE CONSISTENCY とボリュームグループ属性を確認する。</li><li>C. 表示や設定で扱う内容は性能管理でtopas -Dを用い・csz とtopasディスク表示を確認する。</li><li>D. 表示や設定で扱う内容はSRCとログでsyslog_ssw -cを用い・TIMESTAMP とエラーログ一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「デバイス管理でcfgmgrを用い、path status とデバイス一覧を確認する」に対応する項目はpath status（変更・cfgm）です。変更後に関するデバイス管理の仕様は「デバイス管理でcfgmgrを用い、path status」で、確認対象はcf・変更後です。障害切・mklvのB:は「LVMでmklvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（障害・mklv）です。容量・topaのC:は「性能管理でtopas -Dを用い、csz」を述べ、対象は容量確認 csz（容量・topa）です。バック・syslのD:は「SRCとログでsyslog_ssw -cを用い、TIMESTAMP」を述べ、対象はバックアウト確認 TIMESTAMP（バッ・sysl）です。「cfgmgr」は「デバイス管理でcfgmgrを用い、path status」を指し、path statusではcf・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cfgmgr 変更後確認 path status 0658</strong></p><p>検証目的: デバイス管理のcfgmgr 変更後確認 path status 0658について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理変更後確認058-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; cfgmgr
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0658A
画面・出力には AIX0658A が表示され、cfgmgr 変更後確認 path status 0658 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0658B
画面・出力には AIX0658B が表示され、cfgmgr 変更後確認 path status 0658 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0658C
画面・出力には AIX0658C が表示され、cfgmgr 変更後確認 path status 0658 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0658A が画面・出力に表示されること
② ステップ2 の AIX0658B が画面・出力に表示されること
③ ステップ3 の AIX0658C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0479"><h3>cfgmgr 変更後確認 path status 0718</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 上級</p><p>春霞保守ではAIX 7.3のデバイス管理で cfgmgr を確認します。春霞保守のデバイス管理では path status とデバイス一覧を保守票へ記録します。春霞保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。春霞保守の注意点として 構成再検出前の判断 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、春霞保守を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> cfgmgr 変更後確認 path status 0718に関する障害切り分けの前提を確認しています。mklv 障害切り分け MIRROR WRITE CONSISTENCY 0719の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はLVMでmklvを用い・MIRROR WRITE CONSISTENCY とボリュームグループ属性を確認する。</li><li>B. 表示や設定で扱う内容は性能管理でtopas -Dを用い・PhysB とtopasディスク表示を確認する。</li><li>C. 表示や設定で扱う内容はデバイス管理でcfgmgrを用い・path status とデバイス一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はSRCとログでsyslog_ssw -rを用い・syslog.conf とエラーログ一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「デバイス管理でcfgmgrを用い、path status とデバイス一覧を確認する」に対応する項目はpath status（変更・cfgm）です。変更後に関するデバイス管理の仕様は「デバイス管理でcfgmgrを用い、path status」で、確認対象はcf・変更後です。障害切・mklvのA:は「LVMでmklvを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（障害・mklv）です。容量・topaのB:は「性能管理でtopas -Dを用い、PhysB」を述べ、対象は容量確認 PhysB（容量・topa）です。監査・syslのD:は「SRCとログでsyslog_ssw -rを用い」を述べ、対象は監査記録 syslog.conf（監査・sysl）です。「cfgmgr」は「デバイス管理でcfgmgrを用い、path status」を指し、path statusではcf・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cfgmgr 変更後確認 path status 0718</strong></p><p>検証目的: デバイス管理のcfgmgr 変更後確認 path status 0718について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理変更後確認118-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; cfgmgr
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0718A
画面・出力には AIX0718A が表示され、cfgmgr 変更後確認 path status 0718 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0718B
画面・出力には AIX0718B が表示され、cfgmgr 変更後確認 path status 0718 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。path status を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0718C
画面・出力には AIX0718C が表示され、cfgmgr 変更後確認 path status 0718 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0718A が画面・出力に表示されること
② ステップ2 の AIX0718B が画面・出力に表示されること
③ ステップ3 の AIX0718C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0480"><h3>cfgmgr 属性確認 Available 0023</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>新緑確認ではAIX 7.3のデバイス管理で cfgmgr を確認します。新緑確認のデバイス管理では Available とODM属性を照合票へ整理します。新緑確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる控えにします。新緑確認の注意点として パス状態と物理障害の混同 を避けるため lscfg -vl ent0 も併記します。デバイス構成管理の作業票として、新緑確認を復旧材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> cfgmgr 属性確認 Available 0023の設定や表示を読む前に役割を確認します。mklv 状態確認 PVID 0024ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はLVMでmklvを用い・PVID と論理ボリューム配置を確認する。</li><li>B. 一次資料が示す主目的は導入と起動でlslpp -Lを用い・mksysb image と起動デバイス設定を確認する。</li><li>C. 一次資料が示す主目的はデバイス管理でcfgmgrを用い・Available とODM属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はLVMでlsvgを用い・MIRROR WRITE CONSISTENCY と論理ボリューム配置を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「デバイス管理でcfgmgrを用い、Available とODM属性を確認する」に対応する項目は属性確認 Available（属性・cfgm）です。デバイス管理の仕様は「デバイス管理でcfgmgrを用い、Available」で、確認対象はcf・属性です。状態・mklvのA:は「LVMでmklvを用い、PVID と論理ボリューム配置を確認する」を述べ、対象は状態確認 PVID（状態・mklv）です。運用引・lslpのB:は「導入と起動でlslpp -Lを用い、mksysb image」を述べ、対象はmksysb image（運用・lslp）です。バック・lsvgのD:は「LVMでlsvgを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（バッ・lsvg）です。「cfgmgr」は「デバイス管理でcfgmgrを用い、Available」を指し、属性確認 Availableではcf・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cfgmgr 属性確認 Available 0023</strong></p><p>検証目的: デバイス管理のcfgmgr 属性確認 Available 0023について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理属性確認023-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; cfgmgr
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0023A
画面・出力には AIX0023A が表示され、cfgmgr 属性確認 Available 0023 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0023B
画面・出力には AIX0023B が表示され、cfgmgr 属性確認 Available 0023 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0023C
画面・出力には AIX0023C が表示され、cfgmgr 属性確認 Available 0023 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0023A が画面・出力に表示されること
② ステップ2 の AIX0023B が画面・出力に表示されること
③ ステップ3 の AIX0023C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0481"><h3>cfgmgr 属性確認 attribute 0499</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 初級</p><p>山吹確認ではAIX 7.3のデバイス管理で cfgmgr を確認します。山吹確認のデバイス管理では attribute とODM属性を点検票へ整理します。山吹確認は対象名と取得時刻を残し、出力見出しを資料名へ戻せる履歴にします。山吹確認の注意点として パス状態と物理障害の混同 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、山吹確認を調査記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> cfgmgr 属性確認 attribute 0499について構成や状態を確認します。mklv 状態確認 LV STATE 0500ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはLVMでmklvを用い・LV STATE と論理ボリューム配置を確認する。</li><li>B. 対象資源に対する働きは導入と起動でlslpp -Lを用い・fileset level と起動デバイス設定を確認する。</li><li>C. 対象資源に対する働きはデバイス管理でcfgmgrを用い・attribute とODM属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはSRCとログでsyslog_ssw -cを用い・PID とsyslog設定変換を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「デバイス管理でcfgmgrを用い、attribute とODM属性を確認する」に対応する項目は属性確認 attribute（属性・cfgm）です。属性に関するデバイス管理の仕様は「デバイス管理でcfgmgrを用い、attribute」で、確認対象はcf・属性です。状態・mklvのA:は「LVMでmklvを用い、LV STATE」を述べ、対象はLV STATE（状態・mklv）です。運用引・lslpのB:は「導入と起動でlslpp -Lを用い、fileset level」を述べ、対象はfileset level（運用・lslp）です。構成・syslのD:は「SRCとログでsyslog_ssw -cを用い、PID」を述べ、対象は構成照合 PID（構成・sysl）です。「cfgmgr」は「デバイス管理でcfgmgrを用い、attribute」を指し、属性確認 attributeではcf・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cfgmgr 属性確認 attribute 0499</strong></p><p>検証目的: デバイス管理のcfgmgr 属性確認 attribute 0499について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理属性確認019-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; cfgmgr
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0499A
画面・出力には AIX0499A が表示され、cfgmgr 属性確認 attribute 0499 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0499B
画面・出力には AIX0499B が表示され、cfgmgr 属性確認 attribute 0499 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0499C
画面・出力には AIX0499C が表示され、cfgmgr 属性確認 attribute 0499 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0499A が画面・出力に表示されること
② ステップ2 の AIX0499B が画面・出力に表示されること
③ ステップ3 の AIX0499C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0482"><h3>cfgmgr 性能確認 location code 0628</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>雪解採取ではAIX 7.3のデバイス管理で cfgmgr を確認します。雪解採取のデバイス管理では location code と構成マネージャー結果を監査票へ転記します。雪解採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。雪解採取の注意点として DefinedとAvailableの混同 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、雪解採取を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> cfgmgr 性能確認 location code 0628の技術的な意味を資料で確認するとき、mklv 起動確認 LV STATE 0629との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はLVMでmklvを用い・LV STATE とミラーコピー状態を確認する。</li><li>B. 管理対象との関係を表す説明は性能管理でtopas -Dを用い・PhysB とvmstat表示を確認する。</li><li>C. 管理対象との関係を表す説明はSRCとログでsyslog_ssw -cを用い・PID とinetdデバッグ出力を確認する。syslog_ssw -c 属性確認 PID 0321固有の属性も確認対象に含める。</li><li>D. 管理対象との関係を表す説明はデバイス管理でcfgmgrを用い・location code と構成マネージャー結果を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「デバイス管理でcfgmgrを用い、location code」に対応する項目はlocation code（性能・cfgm）です。性能に関するデバイス管理の仕様は「デバイス管理でcfgmgrを用い、location code」で、確認対象はcf・性能です。起動・mklvのA:は「LVMでmklvを用い、LV STATE」を述べ、対象はLV STATE（起動・mklv）です。変更前・topaのB:は「性能管理でtopas -Dを用い、PhysB」を述べ、対象は変更前確認 PhysB（変更・topa）です。属性・syslのC:は「SRCとログでsyslog_ssw -cを用い、PID」を述べ、対象は属性確認 PID（属性・sysl）です。「cfgmgr」は「デバイス管理でcfgmgrを用い、location code」を指し、location codeではcf・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cfgmgr 性能確認 location code 0628</strong></p><p>検証目的: デバイス管理のcfgmgr 性能確認 location code 0628について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理性能確認028-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; cfgmgr
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0628A
画面・出力には AIX0628A が表示され、cfgmgr 性能確認 location code 0628 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0628B
画面・出力には AIX0628B が表示され、cfgmgr 性能確認 location code 0628 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0628C
画面・出力には AIX0628C が表示され、cfgmgr 性能確認 location code 0628 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0628A が画面・出力に表示されること
② ステップ2 の AIX0628B が画面・出力に表示されること
③ ステップ3 の AIX0628C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0483"><h3>cfgmgr 性能確認 location code 0688</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>翠風保守ではAIX 7.3のデバイス管理で cfgmgr を確認します。翠風保守のデバイス管理では location code と構成マネージャー結果を監査票へ転記します。翠風保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる項目にします。翠風保守の注意点として DefinedとAvailableの混同 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、翠風保守を採取結果にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> cfgmgr 性能確認 location code 0688を同一分類のmklv 起動確認 LV STATE 0689と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はLVMでmklvを用い・LV STATE とミラーコピー状態を確認する。</li><li>B. 管理対象との関係を表す説明は性能管理でtopas -Dを用い・fre とvmstat表示を確認する。</li><li>C. 管理対象との関係を表す説明はデバイス管理でcfgmgrを用い・location code と構成マネージャー結果を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はSRCとログでsyslog_ssw -rを用い・Status とinetdデバッグ出力を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「デバイス管理でcfgmgrを用い、location code」に対応する項目はlocation code（性能・cfgm）です。性能に関するデバイス管理の仕様は「デバイス管理でcfgmgrを用い、location code」で、確認対象はcf・性能です。起動・mklvのA:は「LVMでmklvを用い、LV STATE」を述べ、対象はLV STATE（起動・mklv）です。変更前・topaのB:は「性能管理でtopas -Dを用い、fre」を述べ、対象は変更前確認 fre（変更・topa）です。状態・syslのD:は「SRCとログでsyslog_ssw -rを用い、Status」を述べ、対象は状態確認 Status（状態・sysl）です。「cfgmgr」は「デバイス管理でcfgmgrを用い、location code」を指し、location codeではcf・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cfgmgr 性能確認 location code 0688</strong></p><p>検証目的: デバイス管理のcfgmgr 性能確認 location code 0688について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理性能確認088-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; cfgmgr
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0688A
画面・出力には AIX0688A が表示され、cfgmgr 性能確認 location code 0688 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0688B
画面・出力には AIX0688B が表示され、cfgmgr 性能確認 location code 0688 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0688C
画面・出力には AIX0688C が表示され、cfgmgr 性能確認 location code 0688 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0688A が画面・出力に表示されること
② ステップ2 の AIX0688B が画面・出力に表示されること
③ ステップ3 の AIX0688C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0484"><h3>cfgmgr 性能確認 microcode level 0152</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>夕映採取ではAIX 7.3のデバイス管理で cfgmgr を確認します。夕映採取のデバイス管理では microcode level と構成マネージャー結果を引継ぎ票へ保管します。夕映採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。夕映採取の注意点として DefinedとAvailableの混同 を避けるため lscfg -vl ent0 も併記します。デバイス構成管理の作業票として、夕映採取を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> cfgmgr 性能確認 microcode level 0152を同一分類のmklv 起動確認 PVID 0153と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はLVMでmklvを用い・PVID とミラーコピー状態を確認する。</li><li>B. コマンドまたは機能の用途はデバイス管理でcfgmgrを用い・microcode level と構成マネージャー結果を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. コマンドまたは機能の用途は導入と起動でlslpp -Lを用い・altinst_rootvg とOSレベル表示を確認する。</li><li>D. コマンドまたは機能の用途はLVMでlsvgを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「デバイス管理でcfgmgrを用い、microcode level」に対応する項目はmicrocode level（性能・cfgm）です。性能に関するデバイス管理の仕様は「デバイス管理でcfgmgrを用い、microcode level」で、確認対象はcf・性能です。起動・mklvのA:は「LVMでmklvを用い、PVID とミラーコピー状態を確認する」を述べ、対象は起動確認 PVID（起動・mklv）です。バック・lslpのC:は「導入と起動でlslpp -Lを用い、altinst_rootvg」を述べ、対象はバックアウト確認 altinst_r（バッ・lslp）です。変更後・lsvgのD:は「LVMでlsvgを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（変更・lsvg）です。「cfgmgr」は「デバイス管理でcfgmgrを用い、microcode level」を指し、microcode levelではcf・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cfgmgr 性能確認 microcode level 0152</strong></p><p>検証目的: デバイス管理のcfgmgr 性能確認 microcode level 0152について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理性能確認032-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。microcode level を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; cfgmgr
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0152A
画面・出力には AIX0152A が表示され、cfgmgr 性能確認 microcode level 0152 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。microcode level を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0152B
画面・出力には AIX0152B が表示され、cfgmgr 性能確認 microcode level 0152 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。microcode level を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0152C
画面・出力には AIX0152C が表示され、cfgmgr 性能確認 microcode level 0152 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0152A が画面・出力に表示されること
② ステップ2 の AIX0152B が画面・出力に表示されること
③ ステップ3 の AIX0152C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0485"><h3>cfgmgr 性能確認 microcode level 0212</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>水音保守ではAIX 7.3のデバイス管理で cfgmgr を確認します。水音保守のデバイス管理では microcode level と構成マネージャー結果を引継ぎ票へ保管します。水音保守は対象名と取得時刻を残し、出力見出しを資料名へ戻せる確認結果にします。水音保守の注意点として DefinedとAvailableの混同 を避けるため lscfg -vl ent0 も併記します。デバイス構成管理の作業票として、水音保守を再確認材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> cfgmgr 性能確認 microcode level 0212の技術的な意味を資料で確認するとき、mklv 起動確認 PVID 0213との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はデバイス管理でcfgmgrを用い・microcode level と構成マネージャー結果を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はLVMでmklvを用い・PVID とミラーコピー状態を確認する。</li><li>C. コマンドまたは機能の用途は導入と起動でinstallp -Cを用い・mksysb image とOSレベル表示を確認する。</li><li>D. コマンドまたは機能の用途はLVMでlsvgを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「デバイス管理でcfgmgrを用い、microcode level」に対応する項目はmicrocode level（性能・cfgm）です。性能に関するデバイス管理の仕様は「デバイス管理でcfgmgrを用い、microcode level」で、確認対象はcf・性能です。起動・mklvのB:は「LVMでmklvを用い、PVID とミラーコピー状態を確認する」を述べ、対象は起動確認 PVID（起動・mklv）です。監査・instのC:は「導入と起動でinstallp -Cを用い、mksysb image」を述べ、対象はmksysb image（監査・inst）です。変更後・lsvgのD:は「LVMでlsvgを用い、MIRROR WRITE」を述べ、対象はWRITE CONSISTENCY（変更・lsvg）です。「cfgmgr」は「デバイス管理でcfgmgrを用い、microcode level」を指し、microcode levelではcf・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>cfgmgr 性能確認 microcode level 0212</strong></p><p>検証目的: デバイス管理のcfgmgr 性能確認 microcode level 0212について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理性能確認092-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。microcode level を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; cfgmgr
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0212A
画面・出力には AIX0212A が表示され、cfgmgr 性能確認 microcode level 0212 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。microcode level を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0212B
画面・出力には AIX0212B が表示され、cfgmgr 性能確認 microcode level 0212 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。microcode level を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0212C
画面・出力には AIX0212C が表示され、cfgmgr 性能確認 microcode level 0212 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0212A が画面・出力に表示されること
② ステップ2 の AIX0212B が画面・出力に表示されること
③ ステップ3 の AIX0212C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0486"><h3>chdev -l hdisk0 変更前確認 attribute 0121</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 初級</p><p>白露採取ではAIX 7.3のデバイス管理で chdev -l hdisk0 を確認します。白露採取のデバイス管理では attribute と診断対象表示を採取票へ記録します。白露採取は対象名と取得時刻を残し、出力見出しを資料名へ戻せる票にします。白露採取の注意点として ODM属性の更新反映漏れ を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、白露採取を保守判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「chdev -l hdisk0 変更前確認 attribute 0121」を「lslv 変更後確認 LV STATE 0122」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はLVMでlslvを用い・LV STATE と物理ボリューム一覧を確認する。</li><li>B. 保守作業で参照する機能はデバイス管理でchdev -l hdisk0を用い・attribute と診断対象表示を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能は導入と起動でoslevel -sを用い・fileset level とfileset一覧を確認する。</li><li>D. 保守作業で参照する機能はLVMでlspvを用い・VG STATE と物理ボリューム一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「デバイス管理でchdev -l hdisk0を用い、attribute」に対応する項目は変更前確認 attribute（変更・chde）です。変更前に関するデバイス管理の仕様は「デバイス管理でchdev -l hdisk0を用い」で、確認対象はch・変更前です。変更後・lslvのA:は「LVMでlslvを用い、LV STATE」を述べ、対象はLV STATE（変更・lslv）です。起動・osleのC:は「導入と起動でoslevel -sを用い、fileset level」を述べ、対象はfileset level（起動・osle）です。容量・lspvのD:は「LVMでlspvを用い、VG STATE」を述べ、対象はVG STATE（容量・lspv）です。「chdev -l hdisk0」は「デバイス管理でchdev -l hdisk0を用い」を指し、変更前確認 attributeではch・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev -l hdisk0 変更前確認 attribute 0121</strong></p><p>検証目的: デバイス管理のchdev -l hdisk0 変更前確認 attribute 0121について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理変更前確認001-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chdev -l hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0121A
画面・出力には AIX0121A が表示され、chdev -l hdisk0 変更前確認 attribute 0121 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0121B
画面・出力には AIX0121B が表示され、chdev -l hdisk0 変更前確認 attribute 0121 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。attribute を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0121C
画面・出力には AIX0121C が表示され、chdev -l hdisk0 変更前確認 attribute 0121 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0121A が画面・出力に表示されること
② ステップ2 の AIX0121B が画面・出力に表示されること
③ ステップ3 の AIX0121C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0487"><h3>chdev -l hdisk0 状態確認 PVID 0726</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 初級</p><p>朝凪監査ではAIX 7.3のデバイス管理で chdev -l hdisk0 を確認します。朝凪監査のデバイス管理では PVID とデバイス一覧を変更票へ記録します。朝凪監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。朝凪監査の注意点として 構成再検出前の判断 を避けるため lsdev -Cc disk も併記します。デバイス構成管理の作業票として、朝凪監査を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chdev -l hdisk0 状態確認 PVID 0726に関する障害切り分けの前提を確認しています。lslv 構成照合 STALE PARTITIONS 0727の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはLVMでlslvを用い・STALE PARTITIONS とボリュームグループ属性を確認する。</li><li>B. 機能の説明としてはデバイス管理でchdev -l hdisk0を用い・PVID とデバイス一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としては性能管理でsvmon -Gを用い・pi とtopasディスク表示を確認する。</li><li>D. 機能の説明としてはSRCとログでrefresh -s syslogdを用い・IDENTIFIER とエラーログ一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「デバイス管理でchdev -l hdisk0を用い、PVID」に対応する項目は状態確認 PVID（状態・chde）です。状態に関するデバイス管理の仕様は「デバイス管理でchdev -l hdisk0を用い、PVID」で、確認対象はch・状態です。構成・lslvのA:は「LVMでlslvを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（構成・lslv）です。障害切・svmoのC:は「性能管理でsvmon -Gを用い、pi とtopasディスク表示を確」を述べ、対象は障害切り分け pi（障害・svmo）です。変更前・refrのD:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は変更前確認 IDENTIFIER（変更・refr）です。「chdev -l hdisk0」は「デバイス管理でchdev -l hdisk0を用い、PVID」を指し、状態確認 PVIDではch・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev -l hdisk0 状態確認 PVID 0726</strong></p><p>検証目的: デバイス管理のchdev -l hdisk0 状態確認 PVID 0726について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理状態確認006-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chdev -l hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0726A
画面・出力には AIX0726A が表示され、chdev -l hdisk0 状態確認 PVID 0726 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0726B
画面・出力には AIX0726B が表示され、chdev -l hdisk0 状態確認 PVID 0726 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0726C
画面・出力には AIX0726C が表示され、chdev -l hdisk0 状態確認 PVID 0726 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0726A が画面・出力に表示されること
② ステップ2 の AIX0726B が画面・出力に表示されること
③ ステップ3 の AIX0726C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0488"><h3>chdev -l hdisk0 状態確認 PVID 0786</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>陽炎復旧ではAIX 7.3のデバイス管理で chdev -l hdisk0 を確認します。陽炎復旧のデバイス管理では PVID とデバイス一覧を変更票へ記録します。陽炎復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる台帳にします。陽炎復旧の注意点として 構成再検出前の判断 を避けるため lsdev -Cc disk も併記します。デバイス構成管理の作業票として、陽炎復旧を運用記録にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chdev -l hdisk0 状態確認 PVID 0786の役割を調べています。nmon 容量確認 PhysB 0830の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としては性能管理でnmonを用い・PhysB とvmstat表示を確認する。</li><li>B. 機能の説明としてはJFS2でsnapを用い・lff とログデバイス設定を確認する。</li><li>C. 機能の説明としては導入と起動でoslevel -sを用い・Technology Level と代替ディスク状態を確認する。</li><li>D. 機能の説明としてはデバイス管理でchdev -l hdisk0を用い・PVID とデバイス一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 状態・chdeでDの記述「デバイス管理でchdev -l hdisk0を用い、PVID」に対応する項目は状態確認 PVID（状態・chde）です。状態に関するデバイス管理の仕様は「デバイス管理でchdev -l hdisk0を用い、PVID」で、確認対象はch・状態です。容量・nmonのA:は「性能管理でnmonを用い、PhysB とvmstat表示を確認する」を述べ、対象は容量確認 PhysB（容量・nmon）です。監査・snapのB:は「JFS2でsnapを用い、lff とログデバイス設定を確認する」を述べ、対象は監査記録 lff（監査・snap）です。容量・osleのC:は「導入と起動でoslevel -sを用い、Technology」を述べ、対象はTechnology Level（容量・osle）です。「chdev -l hdisk0」は「デバイス管理でchdev -l hdisk0を用い、PVID」を指し、状態確認 PVIDではch・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev -l hdisk0 状態確認 PVID 0786</strong></p><p>検証目的: デバイス管理のchdev -l hdisk0 状態確認 PVID 0786について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理状態確認066-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chdev -l hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0786A
画面・出力には AIX0786A が表示され、chdev -l hdisk0 状態確認 PVID 0786 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0786B
画面・出力には AIX0786B が表示され、chdev -l hdisk0 状態確認 PVID 0786 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0786C
画面・出力には AIX0786C が表示され、chdev -l hdisk0 状態確認 PVID 0786 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0786A が画面・出力に表示されること
② ステップ2 の AIX0786B が画面・出力に表示されること
③ ステップ3 の AIX0786C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0489"><h3>chdev -l hdisk0 状態確認 location code 0250</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 初級</p><p>桜雲監査ではAIX 7.3のデバイス管理で chdev -l hdisk0 を確認します。桜雲監査のデバイス管理では location code とデバイス一覧を保守票へ記録します。桜雲監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。桜雲監査の注意点として 構成再検出前の判断 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、桜雲監査を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chdev -l hdisk0 状態確認 location code 0250の役割を調べています。lslv 構成照合 LV STATE 0251の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はLVMでlslvを用い・LV STATE とボリュームグループ属性を確認する。lslv 構成照合 LV STATE 0251固有の属性も確認対象に含める。</li><li>B. 表示や設定で扱う内容は導入と起動でoslevel -sを用い・Technology Level と代替ディスク状態を確認する。</li><li>C. 表示や設定で扱う内容はデバイス管理でchdev -l hdisk0を用い・location code とデバイス一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容は論理ボリュームの属性と割り当て情報を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「デバイス管理でchdev -l hdisk0を用い、location code」に対応する項目はlocation code（状態・chde）です。状態に関するデバイス管理の仕様は「デバイス管理でchdev -l hdisk0を用い」で、確認対象はch・状態です。構成・lslvのA:は「LVMでlslvを用い、LV STATE」を述べ、対象はLV STATE（構成・lslv）です。容量・osleのB:は「導入と起動でoslevel -sを用い、Technology」を述べ、対象はTechnology Level（容量・osle）です。一覧・サン・lslvのD:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は一覧確認 サンプル採取（一覧・lslv）です。「chdev -l hdisk0」は「デバイス管理でchdev -l hdisk0を用い」を指し、location codeではch・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev -l hdisk0 状態確認 location code 0250</strong></p><p>検証目的: デバイス管理のchdev -l hdisk0 状態確認 location code 0250について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理状態確認010-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chdev -l hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0250A
画面・出力には AIX0250A が表示され、chdev -l hdisk0 状態確認 location code 0250 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0250B
画面・出力には AIX0250B が表示され、chdev -l hdisk0 状態確認 location code 0250 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0250C
画面・出力には AIX0250C が表示され、chdev -l hdisk0 状態確認 location code 0250 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0250A が画面・出力に表示されること
② ステップ2 の AIX0250B が画面・出力に表示されること
③ ステップ3 の AIX0250C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0490"><h3>chdev -l hdisk0 状態確認 location code 0310</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>早苗復旧ではAIX 7.3のデバイス管理で chdev -l hdisk0 を確認します。早苗復旧のデバイス管理では location code とデバイス一覧を保守票へ記録します。早苗復旧は対象名と取得時刻を残し、出力見出しを資料名へ戻せる記録にします。早苗復旧の注意点として 構成再検出前の判断 を避けるため lsattr -El hdisk0 も併記します。デバイス構成管理の作業票として、早苗復旧を監査材料にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chdev -l hdisk0 状態確認 location code 0310に関する障害切り分けの前提を確認しています。lslv 構成照合 LV STATE 0311の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はLVMでlslvを用い・LV STATE とボリュームグループ属性を確認する。</li><li>B. 表示や設定で扱う内容は導入と起動でlslpp -Lを用い・fileset level と代替ディスク状態を確認する。</li><li>C. 表示や設定で扱う内容はSRCとログでsyslog_ssw -cを用い・Status とエラーログ一覧を確認する。syslog_ssw -c 変更後確認 Status 0003固有の属性も確認対象に含める。</li><li>D. 表示や設定で扱う内容はデバイス管理でchdev -l hdisk0を用い・location code とデバイス一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「デバイス管理でchdev -l hdisk0を用い、location code」に対応する項目はlocation code（状態・chde）です。状態に関するデバイス管理の仕様は「デバイス管理でchdev -l hdisk0を用い」で、確認対象はch・状態です。構成・lslvのA:は「LVMでlslvを用い、LV STATE」を述べ、対象はLV STATE（構成・lslv）です。性能・lslpのB:は「導入と起動でlslpp -Lを用い、fileset level」を述べ、対象はfileset level（性能・lslp）です。変更後・syslのC:は「SRCとログでsyslog_ssw -cを用い、Status」を述べ、対象は変更後確認 Status（変更・sysl）です。「chdev -l hdisk0」は「デバイス管理でchdev -l hdisk0を用い」を指し、location codeではch・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev -l hdisk0 状態確認 location code 0310</strong></p><p>検証目的: デバイス管理のchdev -l hdisk0 状態確認 location code 0310について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理状態確認070-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chdev -l hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0310A
画面・出力には AIX0310A が表示され、chdev -l hdisk0 状態確認 location code 0310 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0310B
画面・出力には AIX0310B が表示され、chdev -l hdisk0 状態確認 location code 0310 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。location code を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsdev -Cc disk
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0310C
画面・出力には AIX0310C が表示され、chdev -l hdisk0 状態確認 location code 0310 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0310A が画面・出力に表示されること
② ステップ2 の AIX0310B が画面・出力に表示されること
③ ステップ3 の AIX0310C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0491"><h3>chdev -l hdisk0 監査記録 Available 0756</h3><p class="kb-meta">分類: デバイス管理 ・ 難易度: 中級</p><p>若潮監査ではAIX 7.3のデバイス管理で chdev -l hdisk0 を確認します。若潮監査のデバイス管理では Available と構成マネージャー結果を同じ証跡に残します。若潮監査は対象名と取得時刻を残し、出力見出しを資料名へ戻せる証跡にします。若潮監査の注意点として DefinedとAvailableの混同 を避けるため lsdev -Cc disk も併記します。デバイス構成管理の作業票として、若潮監査を変更判断にします。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chdev -l hdisk0 監査記録 Available 0756の技術的な意味を資料で確認するとき、lslv 運用引継ぎ VG STATE 0757との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はデバイス管理でchdev -l hdisk0を用い・Available と構成マネージャー結果を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はLVMでlslvを用い・VG STATE とミラーコピー状態を確認する。lslv 運用引継ぎ VG STATE 0757固有の属性も確認対象に含める。</li><li>C. 構成を確認する際の意味は性能管理でiostat -Dl 2 2を用い・avm とvmstat表示を確認する。</li><li>D. 構成を確認する際の意味はSRCとログでrefresh -s syslogdを用い・Subsystemである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「デバイス管理でchdev -l hdisk0を用い、Available」に対応する項目は監査記録 Available（監査・chde）です。監査に関するデバイス管理の仕様は「デバイス管理でchdev -l hdisk0を用い」で、確認対象はch・監査です。運用引・lslvのB:は「LVMでlslvを用い、VG STATE」を述べ、対象はVG STATE（運用・lslv）です。属性・iostのC:は「性能管理でiostat -Dl 2 2を用い、avm」を述べ、対象は属性確認 avm（属性・iost）です。容量・refrのD:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は容量確認 Subsystem（容量・refr）です。「chdev -l hdisk0」は「デバイス管理でchdev -l hdisk0を用い」を指し、監査記録 Availableではch・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev -l hdisk0 監査記録 Available 0756</strong></p><p>検証目的: デバイス管理のchdev -l hdisk0 監査記録 Available 0756について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=デバイス管理監査記録036-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chdev -l hdisk0
→ Enter を押す
［画面・出力］
hdisk0 Available 00-00-00 SAS Disk Drive
hdisk1 Available 00-00-01 SAS Disk Drive
確認コード AIX0756A
画面・出力には AIX0756A が表示され、chdev -l hdisk0 監査記録 Available 0756 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsattr -El hdisk0
→ Enter を押す
［画面・出力］
attribute    value      description
queue_depth  32         Queue DEPTH
reserve_policy no_reserve Reserve Policy
確認コード AIX0756B
画面・出力には AIX0756B が表示され、chdev -l hdisk0 監査記録 Available 0756 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。Available を読むため、デバイス管理 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lscfg -vl ent0
→ Enter を押す
［画面・出力］
DEVICE            LOCATION          DESCRIPTION
ent0              U78D4.001.WZS0000-P1-C2-T1 PCIe3 10GbE Adapter
確認コード AIX0756C
画面・出力には AIX0756C が表示され、chdev -l hdisk0 監査記録 Available 0756 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0756A が画面・出力に表示されること
② ステップ2 の AIX0756B が画面・出力に表示されること
③ ステップ3 の AIX0756C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>
