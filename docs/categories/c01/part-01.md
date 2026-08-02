# AIX 7.3 — 詳細 (1/6)

[← AIX 7.3 の概要へ戻る](index.md)


## JFS2


<section class="kb-item" id="c01-i0001"><h3>chfs バックアウト確認 mountguard 0101</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第百一観点 JFS2 で chfs は バックアウト確認 を点検します（運用第百一）（第百一観点）。第百一観点 確認時には mountguard と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第百一）（第百一観点）。第百一観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第百一観点）。第百一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0101へ書きます（第百一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chfs バックアウト確認 mountguard 0101を保守記録に説明する必要があります。refresh -s syslogd 監査記録 IDENTIFIER 0102と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はSRCとログでrefresh -s syslogdを用い・IDENTIFIERである。</li><li>B. 仕様上の役割は性能管理でvmstat 2 2を用い・avm とsvmon全体表示を確認する。</li><li>C. 仕様上の役割はJFS2でchfsを用い・mountguard とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 仕様上の役割はSRCとログでtail -f /tmp/myfileを用い・Status とSRCサブシステム表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「JFS2でchfsを用い、mountguard とマウントオプションを確認する」に対応する項目はバックアウト確認 mountguar（バッ・chfs）です。バックに関するJFS2の仕様は「JFS2でchfsを用い、mountguard」で、確認対象はch・バックです。監査・refrのA:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は監査記録 IDENTIFIER（監査・refr）です。変更前・vmstのB:は「性能管理でvmstat 2 2を用い、avm」を述べ、対象は変更前確認 avm（変更・vmst）です。属性・tailのD:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は属性確認 Status（属性・tail）です。「chfs」は「JFS2でchfsを用い、mountguard」を指し、バックアウト確認 mountguarではch・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chfs バックアウト確認 mountguard 0101</strong></p><p>検証目的: JFS2のchfs バックアウト確認 mountguard 0101について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2バックアウト確認101-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chfs
→ Enter を押す
［画面・出力］
/data/aixdd0101:
        dev             = /dev/fslv101
        vfs             = jfs2
        log             = INLINE
確認コード AIX0101A
画面・出力には AIX0101A が表示され、chfs バックアウト確認 mountguard 0101 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv101       16.00      9.42   42%     128     1% /data/aixdd0101
確認コード AIX0101B
画面・出力には AIX0101B が表示され、chfs バックアウト確認 mountguard 0101 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0101      --         /data/aixdd0101          jfs2  33554432 rw,log=INLINE
確認コード AIX0101C
画面・出力には AIX0101C が表示され、chfs バックアウト確認 mountguard 0101 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0101A が画面・出力に表示されること
② ステップ2 の AIX0101B が画面・出力に表示されること
③ ステップ3 の AIX0101C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0002"><h3>chfs バックアウト確認 ファイルシステム使用率 0577</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第五百七十七観点 JFS2 で chfs は バックアウト確認 を点検します（運用第五百七十七）（第五百七十七観点）。第五百七十七観点 確認時には ファイルシステム使用率 と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第五百七十七）（第五百七十七観点）。第五百七十七観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第五百七十七観点）。第五百七十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0577へ書きます（第五百七十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「chfs バックアウト確認 ファイルシステム使用率 0577」を「refresh -s syslogd 監査記録 syslog.conf 0578」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はSRCとログでrefresh -s syslogdを用い・syslog.confである。</li><li>B. 保守作業で参照する機能は論理ボリュームの属性と割り当て情報を表示するコマンドである。</li><li>C. 保守作業で参照する機能はネットワークでchdev -l en0 -aを用い・EtherChannel とアダプター一覧を確認する。</li><li>D. 保守作業で参照する機能はJFS2でchfsを用い・ファイルシステム使用率 とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でchfsを用い、ファイルシステム使用率 とマウントオプションを確認する」に対応する項目はバックアウト確認 ファイルシステム使（バッ・chfs）です。バック・ファイに関するJFS2の仕様は「JFS2でchfsを用い、ファイルシステム使用率」で、確認対象はch・バックです。監査・refrのA:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は監査記録 syslog.conf（監査・refr）です。変更前・lslvのB:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は変更前確認 運用記録（変更・lslv）です。容量・chdeのC:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は容量確認 EtherChannel（容量・chde）です。「chfs」は「JFS2でchfsを用い、ファイルシステム使用率」を指し、バックアウト確認 ファイルシステム使ではch・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chfs バックアウト確認 ファイルシステム使用率 0577</strong></p><p>検証目的: JFS2のchfs バックアウト確認 ファイルシステム使用率 0577について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2バックアウト確認097-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chfs
→ Enter を押す
［画面・出力］
/data/aixdd0577:
        dev             = /dev/fslv97
        vfs             = jfs2
        log             = INLINE
確認コード AIX0577A
画面・出力には AIX0577A が表示され、chfs バックアウト確認 ファイルシステム使用率 0577 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv97       16.00      9.42   42%     128     1% /data/aixdd0577
確認コード AIX0577B
画面・出力には AIX0577B が表示され、chfs バックアウト確認 ファイルシステム使用率 0577 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0577      --         /data/aixdd0577          jfs2  33554432 rw,log=INLINE
確認コード AIX0577C
画面・出力には AIX0577C が表示され、chfs バックアウト確認 ファイルシステム使用率 0577 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0577A が画面・出力に表示されること
② ステップ2 の AIX0577B が画面・出力に表示されること
③ ステップ3 の AIX0577C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0003"><h3>chfs 性能確認 isnapshot 0735</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第七百三十五観点 JFS2 で chfs は 性能確認 を点検します（運用第七百三十五）（第七百三十五観点）。第七百三十五観点 確認時には isnapshot と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第七百三十五）（第七百三十五観点）。第七百三十五観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第七百三十五観点）。第七百三十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0735へ書きます（第七百三十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chfs 性能確認 isnapshot 0735の設定や表示を読む前に役割を確認します。refresh -s syslogd 起動確認 Status 0736ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはSRCとログでrefresh -s syslogdを用い・Status とsyslog設定変換を確認する。</li><li>B. 状態を読み取るための働きはデバイス管理でchdev -l hdisk0を用い・attribute と診断対象表示を確認する。</li><li>C. 状態を読み取るための働きはネットワークでifconfig en0を用い・Media Speed Running と経路表を確認する。</li><li>D. 状態を読み取るための働きはJFS2でchfsを用い・isnapshot と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「JFS2でchfsを用い、isnapshot と内部スナップショットを確認する」に対応する項目は性能確認 isnapshot（性能・chfs）です。性能に関するJFS2の仕様は「JFS2でchfsを用い、isnapshot」で、確認対象はch・性能です。起動・refrのA:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は起動確認 Status（起動・refr）です。変更前・chdeのB:は「デバイス管理でchdev -l hdisk0を用い」を述べ、対象は変更前確認 attribute（変更・chde）です。属性・ifcoのC:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（属性・ifco）です。「chfs」は「JFS2でchfsを用い、isnapshot」を指し、性能確認 isnapshotではch・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chfs 性能確認 isnapshot 0735</strong></p><p>検証目的: JFS2のchfs 性能確認 isnapshot 0735について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2性能確認015-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chfs
→ Enter を押す
［画面・出力］
/data/aixdd0735:
        dev             = /dev/fslv15
        vfs             = jfs2
        log             = INLINE
確認コード AIX0735A
画面・出力には AIX0735A が表示され、chfs 性能確認 isnapshot 0735 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv15       16.00      9.42   42%     128     1% /data/aixdd0735
確認コード AIX0735B
画面・出力には AIX0735B が表示され、chfs 性能確認 isnapshot 0735 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0735      --         /data/aixdd0735          jfs2  33554432 rw,log=INLINE
確認コード AIX0735C
画面・出力には AIX0735C が表示され、chfs 性能確認 isnapshot 0735 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0735A が画面・出力に表示されること
② ステップ2 の AIX0735B が画面・出力に表示されること
③ ステップ3 の AIX0735C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0004"><h3>chfs 性能確認 log=INLINE 0259</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第二百五十九観点 JFS2 で chfs は 性能確認 を点検します（運用第二百五十九）（第二百五十九観点）。第二百五十九観点 確認時には log=INLINE と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第二百五十九）（第二百五十九観点）。第二百五十九観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第二百五十九観点）。第二百五十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0259へ書きます（第二百五十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chfs 性能確認 log=INLINE 0259について構成や状態を確認します。refresh -s syslogd 起動確認 Subsystem 0260ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはJFS2でchfsを用い・log=INLINE と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 対象資源に対する働きはSRCとログでrefresh -s syslogdを用い・Subsystemである。</li><li>C. 対象資源に対する働きは性能管理でvmo -aを用い・Entitled Capacity とAME統計を確認する。</li><li>D. 対象資源に対する働きはボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「JFS2でchfsを用い、log=INLINE と内部スナップショットを確認する」に対応する項目は性能確認 log=INLINE（性能・chfs）です。性能に関するJFS2の仕様は「JFS2でchfsを用い、log=INLINE」で、確認対象はch・性能です。起動・refrのB:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は起動確認 Subsystem（起動・refr）です。バック・vmoのC:は「性能管理でvmo -aを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（バッ・vmo）です。状態・製品・lsvgのD:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は状態判定 製品レベル（状態・lsvg）です。「chfs」は「JFS2でchfsを用い、log=INLINE」を指し、性能確認 log=INLINEではch・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chfs 性能確認 log=INLINE 0259</strong></p><p>検証目的: JFS2のchfs 性能確認 log=INLINE 0259について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2性能確認019-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chfs
→ Enter を押す
［画面・出力］
/data/aixdd0259:
        dev             = /dev/fslv19
        vfs             = jfs2
        log             = INLINE
確認コード AIX0259A
画面・出力には AIX0259A が表示され、chfs 性能確認 log=INLINE 0259 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv19       16.00      9.42   42%     128     1% /data/aixdd0259
確認コード AIX0259B
画面・出力には AIX0259B が表示され、chfs 性能確認 log=INLINE 0259 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0259      --         /data/aixdd0259          jfs2  33554432 rw,log=INLINE
確認コード AIX0259C
画面・出力には AIX0259C が表示され、chfs 性能確認 log=INLINE 0259 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0259A が画面・出力に表示されること
② ステップ2 の AIX0259B が画面・出力に表示されること
③ ステップ3 の AIX0259C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0005"><h3>chfs 構成照合 isnapshot 0418</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第四百十八観点 JFS2 で chfs は 構成照合 を点検します（運用第四百十八）（第四百十八観点）。第四百十八観点 確認時には isnapshot と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第四百十八）（第四百十八観点）。第四百十八観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第四百十八観点）。第四百十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0418へ書きます（第四百十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chfs 構成照合 isnapshot 0418の役割を調べています。refresh -s syslogd 変更前確認 IDENTIFIER 0419の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はSRCとログでrefresh -s syslogdを用い・IDENTIFIER とエラーログ一覧を確認する。</li><li>B. 表示や設定で扱う内容は性能管理でvmstat 2 2を用い・Entitled Capacity とtopasディスク表示を確認する。</li><li>C. 表示や設定で扱う内容はJFS2でchfsを用い・isnapshot とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はネットワークでifconfig en0を用い・MTU とEthernet統計を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でchfsを用い、isnapshot とファイルシステム属性を確認する」に対応する項目は構成照合 isnapshot（構成・chfs）です。構成に関するJFS2の仕様は「JFS2でchfsを用い、isnapshot」で、確認対象はch・構成です。変更前・refrのA:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は変更前確認 IDENTIFIER（変更・refr）です。起動・vmstのB:は「性能管理でvmstat 2 2を用い、Entitled」を述べ、対象はEntitled Capacity（起動・vmst）です。変更後・ifcoのD:は「ネットワークでifconfig en0を用い、MTU」を述べ、対象は変更後確認 MTU（変更・ifco）です。「chfs」は「JFS2でchfsを用い、isnapshot」を指し、構成照合 isnapshotではch・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chfs 構成照合 isnapshot 0418</strong></p><p>検証目的: JFS2のchfs 構成照合 isnapshot 0418について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2構成照合058-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chfs
→ Enter を押す
［画面・出力］
/data/aixdd0418:
        dev             = /dev/fslv58
        vfs             = jfs2
        log             = INLINE
確認コード AIX0418A
画面・出力には AIX0418A が表示され、chfs 構成照合 isnapshot 0418 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv58       16.00      9.42   42%     128     1% /data/aixdd0418
確認コード AIX0418B
画面・出力には AIX0418B が表示され、chfs 構成照合 isnapshot 0418 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0418      --         /data/aixdd0418          jfs2  33554432 rw,log=INLINE
確認コード AIX0418C
画面・出力には AIX0418C が表示され、chfs 構成照合 isnapshot 0418 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0418A が画面・出力に表示されること
② ステップ2 の AIX0418B が画面・出力に表示されること
③ ステップ3 の AIX0418C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0006"><h3>chfs 構成照合 isnapshot 0478</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第四百七十八観点 JFS2 で chfs は 構成照合 を点検します（運用第四百七十八）（第四百七十八観点）。第四百七十八観点 確認時には isnapshot と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第四百七十八）（第四百七十八観点）。第四百七十八観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第四百七十八観点）。第四百七十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0478へ書きます（第四百七十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chfs 構成照合 isnapshot 0478に関する障害切り分けの前提を確認しています。refresh -s syslogd 変更前確認 IDENTIFIER 0479の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はSRCとログでrefresh -s syslogdを用い・IDENTIFIER とエラーログ一覧を確認する。</li><li>B. 表示や設定で扱う内容はJFS2でchfsを用い・isnapshot とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容は性能管理でvmstat 2 2を用い・pi とtopasディスク表示を確認する。</li><li>D. 表示や設定で扱う内容はネットワークでchdev -l en0 -aを用い・Destination とEthernet統計を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「JFS2でchfsを用い、isnapshot とファイルシステム属性を確認する」に対応する項目は構成照合 isnapshot（構成・chfs）です。構成に関するJFS2の仕様は「JFS2でchfsを用い、isnapshot」で、確認対象はch・構成です。変更前・refrのA:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は変更前確認 IDENTIFIER（変更・refr）です。起動・vmstのC:は「性能管理でvmstat 2 2を用い、pi」を述べ、対象は起動確認 pi（起動・vmst）です。障害切・chdeのD:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は障害切り分け Destination（障害・chde）です。「chfs」は「JFS2でchfsを用い、isnapshot」を指し、構成照合 isnapshotではch・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chfs 構成照合 isnapshot 0478</strong></p><p>検証目的: JFS2のchfs 構成照合 isnapshot 0478について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2構成照合118-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chfs
→ Enter を押す
［画面・出力］
/data/aixdd0478:
        dev             = /dev/fslv118
        vfs             = jfs2
        log             = INLINE
確認コード AIX0478A
画面・出力には AIX0478A が表示され、chfs 構成照合 isnapshot 0478 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv118       16.00      9.42   42%     128     1% /data/aixdd0478
確認コード AIX0478B
画面・出力には AIX0478B が表示され、chfs 構成照合 isnapshot 0478 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0478      --         /data/aixdd0478          jfs2  33554432 rw,log=INLINE
確認コード AIX0478C
画面・出力には AIX0478C が表示され、chfs 構成照合 isnapshot 0478 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0478A が画面・出力に表示されること
② ステップ2 の AIX0478B が画面・出力に表示されること
③ ステップ3 の AIX0478C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0007"><h3>chfs 運用引継ぎ ファイルシステム使用率 0388</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第三百八十八観点 JFS2 で chfs は 運用引継ぎ を点検します（運用第三百八十八）（第三百八十八観点）。第三百八十八観点 確認時には ファイルシステム使用率 と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第三百八十八）（第三百八十八観点）。第三百八十八観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第三百八十八観点）。第三百八十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0388へ書きます（第三百八十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chfs 運用引継ぎ ファイルシステム使用率 0388の技術的な意味を資料で確認するとき、refresh -s syslogd 容量確認 Subsystem 0389との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はSRCとログでrefresh -s syslogdを用い・Subsystemである。</li><li>B. 管理対象との関係を表す説明は性能管理でvmo -aを用い・fre とvmstat表示を確認する。</li><li>C. 管理対象との関係を表す説明はネットワークでifconfig en0を用い・EtherChannel とMTU属性を確認する。</li><li>D. 管理対象との関係を表す説明はJFS2でchfsを用い・ファイルシステム使用率 とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でchfsを用い、ファイルシステム使用率 とログデバイス設定を確認する」に対応する項目は運用引継ぎ ファイルシステム使用率（運用・chfs）です。運用引・ファイに関するJFS2の仕様は「JFS2でchfsを用い、ファイルシステム使用率」で、確認対象はch・運用引です。容量・refrのA:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は容量確認 Subsystem（容量・refr）です。変更後・vmoのB:は「性能管理でvmo -aを用い、fre とvmstat表示を確認する」を述べ、対象は変更後確認 fre（変更・vmo）です。性能・ifcoのC:は「ネットワークでifconfig en0を用い」を述べ、対象は性能確認 EtherChannel（性能・ifco）です。「chfs」は「JFS2でchfsを用い、ファイルシステム使用率」を指し、運用引継ぎ ファイルシステム使用率ではch・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chfs 運用引継ぎ ファイルシステム使用率 0388</strong></p><p>検証目的: JFS2のchfs 運用引継ぎ ファイルシステム使用率 0388について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2運用引継ぎ028-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chfs
→ Enter を押す
［画面・出力］
/data/aixdd0388:
        dev             = /dev/fslv28
        vfs             = jfs2
        log             = INLINE
確認コード AIX0388A
画面・出力には AIX0388A が表示され、chfs 運用引継ぎ ファイルシステム使用率 0388 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv28       16.00      9.42   42%     128     1% /data/aixdd0388
確認コード AIX0388B
画面・出力には AIX0388B が表示され、chfs 運用引継ぎ ファイルシステム使用率 0388 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0388      --         /data/aixdd0388          jfs2  33554432 rw,log=INLINE
確認コード AIX0388C
画面・出力には AIX0388C が表示され、chfs 運用引継ぎ ファイルシステム使用率 0388 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0388A が画面・出力に表示されること
② ステップ2 の AIX0388B が画面・出力に表示されること
③ ステップ3 の AIX0388C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0008"><h3>chfs 運用引継ぎ ファイルシステム使用率 0448</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第四百四十八観点 JFS2 で chfs は 運用引継ぎ を点検します（運用第四百四十八）（第四百四十八観点）。第四百四十八観点 確認時には ファイルシステム使用率 と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第四百四十八）（第四百四十八観点）。第四百四十八観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第四百四十八観点）。第四百四十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0448へ書きます（第四百四十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chfs 運用引継ぎ ファイルシステム使用率 0448を同一分類のrefresh -s syslogd 容量確認 Subsystem 0449と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はJFS2でchfsを用い・ファイルシステム使用率 とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はSRCとログでrefresh -s syslogdを用い・Subsystemである。</li><li>C. 管理対象との関係を表す説明は性能管理でvmstat 2 2を用い・dxm とvmstat表示を確認する。</li><li>D. 管理対象との関係を表す説明はネットワークでchdev -l en0 -aを用い・Link Status とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「JFS2でchfsを用い、ファイルシステム使用率 とログデバイス設定を確認する」に対応する項目は運用引継ぎ ファイルシステム使用率（運用・chfs）です。運用引・ファイに関するJFS2の仕様は「JFS2でchfsを用い、ファイルシステム使用率」で、確認対象はch・運用引です。容量・refrのB:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は容量確認 Subsystem（容量・refr）です。障害切・vmstのC:は「性能管理でvmstat 2 2を用い、dxm」を述べ、対象は障害切り分け dxm（障害・vmst）です。起動・chdeのD:は「ネットワークでchdev -l en0 -aを用い、Link」を述べ、対象はLink Status（起動・chde）です。「chfs」は「JFS2でchfsを用い、ファイルシステム使用率」を指し、運用引継ぎ ファイルシステム使用率ではch・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chfs 運用引継ぎ ファイルシステム使用率 0448</strong></p><p>検証目的: JFS2のchfs 運用引継ぎ ファイルシステム使用率 0448について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2運用引継ぎ088-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chfs
→ Enter を押す
［画面・出力］
/data/aixdd0448:
        dev             = /dev/fslv88
        vfs             = jfs2
        log             = INLINE
確認コード AIX0448A
画面・出力には AIX0448A が表示され、chfs 運用引継ぎ ファイルシステム使用率 0448 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv88       16.00      9.42   42%     128     1% /data/aixdd0448
確認コード AIX0448B
画面・出力には AIX0448B が表示され、chfs 運用引継ぎ ファイルシステム使用率 0448 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0448      --         /data/aixdd0448          jfs2  33554432 rw,log=INLINE
確認コード AIX0448C
画面・出力には AIX0448C が表示され、chfs 運用引継ぎ ファイルシステム使用率 0448 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0448A が画面・出力に表示されること
② ステップ2 の AIX0448B が画面・出力に表示されること
③ ステップ3 の AIX0448C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0009"><h3>crfs 変更前確認 isnapshot 0169</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第百六十九観点 JFS2 で crfs は 変更前確認 を点検します（運用第百六十九）（第百六十九観点）。第百六十九観点 確認時には isnapshot と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第百六十九）（第百六十九観点）。第百六十九観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第百六十九観点）。第百六十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0169へ書きます（第百六十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「crfs 変更前確認 isnapshot 0169」を「startsrc -s syslogd 変更後確認 Status 0170」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はSRCとログでstartsrc -s syslogdを用い・Status とSRCサブシステム表示を確認する。</li><li>B. 保守作業で参照する機能は性能管理でlparstat -iを用い・PhysB とsvmon全体表示を確認する。</li><li>C. 保守作業で参照する機能はSRCとログでstartsrc -s inetd -aを用い・PID とSRCサブシステム表示を確認する。</li><li>D. 保守作業で参照する機能はJFS2でcrfsを用い・isnapshot とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でcrfsを用い、isnapshot とマウントオプションを確認する」に対応する項目は変更前確認 isnapshot（変更・crfs）です。変更前に関するJFS2の仕様は「JFS2でcrfsを用い、isnapshot」で、確認対象はcr・変更前です。変更後・starのA:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は変更後確認 Status（変更・star）です。起動・lparのB:は「性能管理でlparstat -iを用い、PhysB」を述べ、対象は起動確認 PhysB（起動・lpar）です。容量・starのC:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は容量確認 PID（容量・star）です。「crfs」は「JFS2でcrfsを用い、isnapshot」を指し、変更前確認 isnapshotではcr・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 変更前確認 isnapshot 0169</strong></p><p>検証目的: JFS2のcrfs 変更前確認 isnapshot 0169について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更前確認049-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0169:
        dev             = /dev/fslv49
        vfs             = jfs2
        log             = INLINE
確認コード AIX0169A
画面・出力には AIX0169A が表示され、crfs 変更前確認 isnapshot 0169 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv49       16.00      9.42   42%     128     1% /data/aixdd0169
確認コード AIX0169B
画面・出力には AIX0169B が表示され、crfs 変更前確認 isnapshot 0169 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0169      --         /data/aixdd0169          jfs2  33554432 rw,log=INLINE
確認コード AIX0169C
画面・出力には AIX0169C が表示され、crfs 変更前確認 isnapshot 0169 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0169A が画面・出力に表示されること
② ステップ2 の AIX0169B が画面・出力に表示されること
③ ステップ3 の AIX0169C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0010"><h3>crfs 変更前確認 isnapshot 0229</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第二百二十九観点 JFS2 で crfs は 変更前確認 を点検します（運用第二百二十九）（第二百二十九観点）。第二百二十九観点 確認時には isnapshot と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第二百二十九）（第二百二十九観点）。第二百二十九観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第二百二十九観点）。第二百二十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0229へ書きます（第二百二十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> crfs 変更前確認 isnapshot 0229を保守記録に説明する必要があります。startsrc -s syslogd 変更後確認 Status 0230と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はSRCとログでstartsrc -s syslogdを用い・Status とSRCサブシステム表示を確認する。</li><li>B. 保守作業で参照する機能は性能管理でvmo -aを用い・pi とsvmon全体表示を確認する。</li><li>C. 保守作業で参照する機能はJFS2でcrfsを用い・isnapshot とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「JFS2でcrfsを用い、isnapshot とマウントオプションを確認する」に対応する項目は変更前確認 isnapshot（変更・crfs）です。変更前に関するJFS2の仕様は「JFS2でcrfsを用い、isnapshot」で、確認対象はcr・変更前です。変更後・starのA:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は変更後確認 Status（変更・star）です。属性・vmoのB:は「性能管理でvmo -aを用い、pi とsvmon全体表示を確認する」を述べ、対象は属性確認 pi（属性・vmo）です。詳細・詳細・lsvgのD:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は詳細確認 詳細表示（詳細・lsvg）です。「crfs」は「JFS2でcrfsを用い、isnapshot」を指し、変更前確認 isnapshotではcr・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 変更前確認 isnapshot 0229</strong></p><p>検証目的: JFS2のcrfs 変更前確認 isnapshot 0229について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更前確認109-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0229:
        dev             = /dev/fslv109
        vfs             = jfs2
        log             = INLINE
確認コード AIX0229A
画面・出力には AIX0229A が表示され、crfs 変更前確認 isnapshot 0229 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv109       16.00      9.42   42%     128     1% /data/aixdd0229
確認コード AIX0229B
画面・出力には AIX0229B が表示され、crfs 変更前確認 isnapshot 0229 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0229      --         /data/aixdd0229          jfs2  33554432 rw,log=INLINE
確認コード AIX0229C
画面・出力には AIX0229C が表示され、crfs 変更前確認 isnapshot 0229 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0229A が画面・出力に表示されること
② ステップ2 の AIX0229B が画面・出力に表示されること
③ ステップ3 の AIX0229C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0011"><h3>crfs 変更前確認 lff 0645</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第六百四十五観点 JFS2 で crfs は 変更前確認 を点検します（運用第六百四十五）（第六百四十五観点）。第六百四十五観点 確認時には lff と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第六百四十五）（第六百四十五観点）。第六百四十五観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第六百四十五観点）。第六百四十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0645へ書きます（第六百四十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> crfs 変更前確認 lff 0645を保守記録に説明する必要があります。startsrc -s syslogd 変更後確認 TIMESTAMP 0646と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はSRCとログでstartsrc -s syslogdを用い・TIMESTAMPである。</li><li>B. 運用時に利用する技術的役割はJFS2でcrfsを用い・lff とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はデバイス管理でlsattr -El hdisk0を用い・path status とODM属性を確認する。</li><li>D. 運用時に利用する技術的役割はネットワークでlsdev -Cc adapterを用い・Destination とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でcrfsを用い、lff とマウントオプションを確認する」に対応する項目は変更前確認 lff（変更・crfs）です。変更前に関するJFS2の仕様は「JFS2でcrfsを用い、lff とマウントオプションを確認する」で、確認対象はcr・変更前です。変更後・starのA:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は変更後確認 TIMESTAMP（変更・star）です。運用引・lsatのC:は「デバイス管理でlsattr -El hdisk0を用い、path」を述べ、対象はpath status（運用・lsat）です。障害切・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は障害切り分け Destination（障害・lsde）です。「crfs」は「JFS2でcrfsを用い、lff とマウントオプションを確認する」を指し、変更前確認 lffではcr・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 変更前確認 lff 0645</strong></p><p>検証目的: JFS2のcrfs 変更前確認 lff 0645について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更前確認045-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0645:
        dev             = /dev/fslv45
        vfs             = jfs2
        log             = INLINE
確認コード AIX0645A
画面・出力には AIX0645A が表示され、crfs 変更前確認 lff 0645 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv45       16.00      9.42   42%     128     1% /data/aixdd0645
確認コード AIX0645B
画面・出力には AIX0645B が表示され、crfs 変更前確認 lff 0645 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0645      --         /data/aixdd0645          jfs2  33554432 rw,log=INLINE
確認コード AIX0645C
画面・出力には AIX0645C が表示され、crfs 変更前確認 lff 0645 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0645A が画面・出力に表示されること
② ステップ2 の AIX0645B が画面・出力に表示されること
③ ステップ3 の AIX0645C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0012"><h3>crfs 変更前確認 lff 0705</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第七百五観点 JFS2 で crfs は 変更前確認 を点検します（運用第七百五）（第七百五観点）。第七百五観点 確認時には lff と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第七百五）（第七百五観点）。第七百五観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第七百五観点）。第七百五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0705へ書きます（第七百五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「crfs 変更前確認 lff 0705」を「startsrc -s syslogd 変更後確認 TIMESTAMP 0706」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はSRCとログでstartsrc -s syslogdを用い・TIMESTAMPである。</li><li>B. 運用時に利用する技術的役割はJFS2でcrfsを用い・lff とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はデバイス管理でlsattr -El hdisk0を用い・path status とODM属性を確認する。</li><li>D. 運用時に利用する技術的役割はネットワークでifconfig en0を用い・Gateway とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「JFS2でcrfsを用い、lff とマウントオプションを確認する」に対応する項目は変更前確認 lff（変更・crfs）です。変更前に関するJFS2の仕様は「JFS2でcrfsを用い、lff とマウントオプションを確認する」で、確認対象はcr・変更前です。変更後・starのA:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は変更後確認 TIMESTAMP（変更・star）です。運用引・lsatのC:は「デバイス管理でlsattr -El hdisk0を用い、path」を述べ、対象はpath status（運用・lsat）です。バック・ifcoのD:は「ネットワークでifconfig en0を用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・ifco）です。「crfs」は「JFS2でcrfsを用い、lff とマウントオプションを確認する」を指し、変更前確認 lffではcr・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 変更前確認 lff 0705</strong></p><p>検証目的: JFS2のcrfs 変更前確認 lff 0705について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更前確認105-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0705:
        dev             = /dev/fslv105
        vfs             = jfs2
        log             = INLINE
確認コード AIX0705A
画面・出力には AIX0705A が表示され、crfs 変更前確認 lff 0705 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv105       16.00      9.42   42%     128     1% /data/aixdd0705
確認コード AIX0705B
画面・出力には AIX0705B が表示され、crfs 変更前確認 lff 0705 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0705      --         /data/aixdd0705          jfs2  33554432 rw,log=INLINE
確認コード AIX0705C
画面・出力には AIX0705C が表示され、crfs 変更前確認 lff 0705 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0705A が画面・出力に表示されること
② ステップ2 の AIX0705B が画面・出力に表示されること
③ ステップ3 の AIX0705C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0013"><h3>crfs 容量確認 agblksize 0675</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第六百七十五観点 JFS2 で crfs は 容量確認 を点検します（運用第六百七十五）（第六百七十五観点）。第六百七十五観点 確認時には agblksize と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第六百七十五）（第六百七十五観点）。第六百七十五観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第六百七十五観点）。第六百七十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0675へ書きます（第六百七十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> crfs 容量確認 agblksize 0675について構成や状態を確認します。startsrc -s syslogd 性能確認 PID 0676ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはJFS2でcrfsを用い・agblksize と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 状態を読み取るための働きはSRCとログでstartsrc -s syslogdを用い・PID とsyslog設定変換を確認する。</li><li>C. 状態を読み取るための働きはデバイス管理でlsattr -El hdisk0を用い・location code と診断対象表示を確認する。</li><li>D. 状態を読み取るための働きはネットワークでifconfig en0を用い・Media Speed Running と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「JFS2でcrfsを用い、agblksize と内部スナップショットを確認する」に対応する項目は容量確認 agblksize（容量・crfs）です。容量に関するJFS2の仕様は「JFS2でcrfsを用い、agblksize」で、確認対象はcr・容量です。性能・starのB:は「SRCとログでstartsrc -s syslogdを用い、PID」を述べ、対象は性能確認 PID（性能・star）です。構成・lsatのC:は「デバイス管理でlsattr -El hdisk0を用い」を述べ、対象はlocation code（構成・lsat）です。属性・ifcoのD:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（属性・ifco）です。「crfs」は「JFS2でcrfsを用い、agblksize」を指し、容量確認 agblksizeではcr・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 容量確認 agblksize 0675</strong></p><p>検証目的: JFS2のcrfs 容量確認 agblksize 0675について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2容量確認075-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0675:
        dev             = /dev/fslv75
        vfs             = jfs2
        log             = INLINE
確認コード AIX0675A
画面・出力には AIX0675A が表示され、crfs 容量確認 agblksize 0675 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv75       16.00      9.42   42%     128     1% /data/aixdd0675
確認コード AIX0675B
画面・出力には AIX0675B が表示され、crfs 容量確認 agblksize 0675 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0675      --         /data/aixdd0675          jfs2  33554432 rw,log=INLINE
確認コード AIX0675C
画面・出力には AIX0675C が表示され、crfs 容量確認 agblksize 0675 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0675A が画面・出力に表示されること
② ステップ2 の AIX0675B が画面・出力に表示されること
③ ステップ3 の AIX0675C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0014"><h3>crfs 容量確認 ファイルシステム使用率 0199</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第百九十九観点 JFS2 で crfs は 容量確認 を点検します（運用第百九十九）（第百九十九観点）。第百九十九観点 確認時には ファイルシステム使用率 と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第百九十九）（第百九十九観点）。第百九十九観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第百九十九観点）。第百九十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0199へ書きます（第百九十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> crfs 容量確認 ファイルシステム使用率 0199の設定や表示を読む前に役割を確認します。startsrc -s syslogd 性能確認 syslog.conf 0200ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはSRCとログでstartsrc -s syslogdを用い・syslog.confである。</li><li>B. 対象資源に対する働きは性能管理でvmo -aを用い・dxm とAME統計を確認する。</li><li>C. 対象資源に対する働きはJFS2でcrfsを用い・ファイルシステム使用率 と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはSRCとログでstartsrc -s inetd -aを用い・TIMESTAMPである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でcrfsを用い、ファイルシステム使用率 と内部スナップショットを確認する」に対応する項目は容量確認 ファイルシステム使用率（容量・crfs）です。容量・ファイに関するJFS2の仕様は「JFS2でcrfsを用い、ファイルシステム使用率」で、確認対象はcr・容量・ファです。性能・starのA:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は性能確認 syslog.conf（性能・star）です。バック・vmoのB:は「性能管理でvmo -aを用い、dxm とAME統計を確認する」を述べ、対象はバックアウト確認 dxm（バッ・vmo）です。変更前・starのD:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は変更前確認 TIMESTAMP（変更・star）です。「crfs」は「JFS2でcrfsを用い、ファイルシステム使用率」を指し、容量確認 ファイルシステム使用率ではcr・容量・ファに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 容量確認 ファイルシステム使用率 0199</strong></p><p>検証目的: JFS2のcrfs 容量確認 ファイルシステム使用率 0199について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2容量確認079-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0199:
        dev             = /dev/fslv79
        vfs             = jfs2
        log             = INLINE
確認コード AIX0199A
画面・出力には AIX0199A が表示され、crfs 容量確認 ファイルシステム使用率 0199 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv79       16.00      9.42   42%     128     1% /data/aixdd0199
確認コード AIX0199B
画面・出力には AIX0199B が表示され、crfs 容量確認 ファイルシステム使用率 0199 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0199      --         /data/aixdd0199          jfs2  33554432 rw,log=INLINE
確認コード AIX0199C
画面・出力には AIX0199C が表示され、crfs 容量確認 ファイルシステム使用率 0199 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0199A が画面・出力に表示されること
② ステップ2 の AIX0199B が画面・出力に表示されること
③ ステップ3 の AIX0199C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0015"><h3>crfs 起動確認 agblksize 0486</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第四百八十六観点 JFS2 で crfs は 起動確認 を点検します（運用第四百八十六）（第四百八十六観点）。第四百八十六観点 確認時には agblksize と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第四百八十六）（第四百八十六観点）。第四百八十六観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第四百八十六観点）。第四百八十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0486へ書きます（第四百八十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> crfs 起動確認 agblksize 0486に関する障害切り分けの前提を確認しています。startsrc -s syslogd 属性確認 Status 0487の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはSRCとログでstartsrc -s syslogdを用い・Status とエラーログ一覧を確認する。</li><li>B. 機能の説明としてはJFS2でcrfsを用い・agblksize とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としては性能管理でlparstat -iを用い・Busy% とtopasディスク表示を確認する。</li><li>D. 機能の説明としてはネットワークでlsdev -Cc adapterを用い・Media Speed Runningである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「JFS2でcrfsを用い、agblksize とファイルシステム属性を確認する」に対応する項目は起動確認 agblksize（起動・crfs）です。起動に関するJFS2の仕様は「JFS2でcrfsを用い、agblksize」で、確認対象はcr・起動です。属性・starのA:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は属性確認 Status（属性・star）です。監査・lparのC:は「性能管理でlparstat -iを用い、Busy%」を述べ、対象は監査記録 Busy%（監査・lpar）です。状態・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い、Media」を述べ、対象はSpeed Running（状態・lsde）です。「crfs」は「JFS2でcrfsを用い、agblksize」を指し、起動確認 agblksizeではcr・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 起動確認 agblksize 0486</strong></p><p>検証目的: JFS2のcrfs 起動確認 agblksize 0486について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2起動確認006-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0486:
        dev             = /dev/fslv06
        vfs             = jfs2
        log             = INLINE
確認コード AIX0486A
画面・出力には AIX0486A が表示され、crfs 起動確認 agblksize 0486 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv06       16.00      9.42   42%     128     1% /data/aixdd0486
確認コード AIX0486B
画面・出力には AIX0486B が表示され、crfs 起動確認 agblksize 0486 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0486      --         /data/aixdd0486          jfs2  33554432 rw,log=INLINE
確認コード AIX0486C
画面・出力には AIX0486C が表示され、crfs 起動確認 agblksize 0486 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0486A が画面・出力に表示されること
② ステップ2 の AIX0486B が画面・出力に表示されること
③ ステップ3 の AIX0486C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0016"><h3>crfs 起動確認 agblksize 0546</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第五百四十六観点 JFS2 で crfs は 起動確認 を点検します（運用第五百四十六）（第五百四十六観点）。第五百四十六観点 確認時には agblksize と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第五百四十六）（第五百四十六観点）。第五百四十六観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第五百四十六観点）。第五百四十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0546へ書きます（第五百四十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> crfs 起動確認 agblksize 0546の役割を調べています。startsrc -s syslogd 属性確認 Status 0547の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはJFS2でcrfsを用い・agblksize とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 機能の説明としてはSRCとログでstartsrc -s syslogdを用い・Status とエラーログ一覧を確認する。</li><li>C. 機能の説明としてはボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>D. 機能の説明としてはネットワークでlsdev -Cc adapterを用い・Media Speed Runningである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「JFS2でcrfsを用い、agblksize とファイルシステム属性を確認する」に対応する項目は起動確認 agblksize（起動・crfs）です。起動に関するJFS2の仕様は「JFS2でcrfsを用い、agblksize」で、確認対象はcr・起動です。属性・starのB:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は属性確認 Status（属性・star）です。障害切・lsvgのC:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は障害切り分け 設定値（障害・lsvg）です。状態・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い、Media」を述べ、対象はSpeed Running（状態・lsde）です。「crfs」は「JFS2でcrfsを用い、agblksize」を指し、起動確認 agblksizeではcr・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 起動確認 agblksize 0546</strong></p><p>検証目的: JFS2のcrfs 起動確認 agblksize 0546について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2起動確認066-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0546:
        dev             = /dev/fslv66
        vfs             = jfs2
        log             = INLINE
確認コード AIX0546A
画面・出力には AIX0546A が表示され、crfs 起動確認 agblksize 0546 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv66       16.00      9.42   42%     128     1% /data/aixdd0546
確認コード AIX0546B
画面・出力には AIX0546B が表示され、crfs 起動確認 agblksize 0546 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0546      --         /data/aixdd0546          jfs2  33554432 rw,log=INLINE
確認コード AIX0546C
画面・出力には AIX0546C が表示され、crfs 起動確認 agblksize 0546 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0546A が画面・出力に表示されること
② ステップ2 の AIX0546B が画面・出力に表示されること
③ ステップ3 の AIX0546C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0017"><h3>crfs 起動確認 ファイルシステム使用率 0010</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第十観点 JFS2 で crfs は 起動確認 を点検します（運用第十）（第十観点）。第十観点 確認時には ファイルシステム使用率 と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第十）（第十観点）。第十観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第十観点）。第十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0010へ書きます（第十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> crfs 起動確認 ファイルシステム使用率 0010の役割を調べています。startsrc -s syslogd 属性確認 Subsystem 0011の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はSRCとログでstartsrc -s syslogdを用い・Subsystem とエラーログ一覧を確認する。</li><li>B. 表示や設定で扱う内容は性能管理でlparstat -iを用い・PhysB とtopasディスク表示を確認する。</li><li>C. 表示や設定で扱う内容はJFS2でcrfsを用い・ファイルシステム使用率 とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はSRCとログでstartsrc -s inetd -aを用い・syslog.confである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「JFS2でcrfsを用い、ファイルシステム使用率 とファイルシステム属性を確認する」に対応する項目は起動確認 ファイルシステム使用率（起動・crfs）です。JFS2の仕様は「JFS2でcrfsを用い、ファイルシステム使用率」で、確認対象はcr・起動・ファです。属性・starのA:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は属性確認 Subsystem（属性・star）です。監査・lparのB:は「性能管理でlparstat -iを用い、PhysB」を述べ、対象は監査記録 PhysB（監査・lpar）です。障害切・starのD:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け syslog.conf（障害・star）です。「crfs」は「JFS2でcrfsを用い、ファイルシステム使用率」を指し、起動確認 ファイルシステム使用率ではcr・起動・ファに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 起動確認 ファイルシステム使用率 0010</strong></p><p>検証目的: JFS2のcrfs 起動確認 ファイルシステム使用率 0010について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2起動確認010-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0010:
        dev             = /dev/fslv10
        vfs             = jfs2
        log             = INLINE
確認コード AIX0010A
画面・出力には AIX0010A が表示され、crfs 起動確認 ファイルシステム使用率 0010 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv10       16.00      9.42   42%     128     1% /data/aixdd0010
確認コード AIX0010B
画面・出力には AIX0010B が表示され、crfs 起動確認 ファイルシステム使用率 0010 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0010      --         /data/aixdd0010          jfs2  33554432 rw,log=INLINE
確認コード AIX0010C
画面・出力には AIX0010C が表示され、crfs 起動確認 ファイルシステム使用率 0010 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0010A が画面・出力に表示されること
② ステップ2 の AIX0010B が画面・出力に表示されること
③ ステップ3 の AIX0010C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0018"><h3>crfs 起動確認 ファイルシステム使用率 0070</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第七十観点 JFS2 で crfs は 起動確認 を点検します（運用第七十）（第七十観点）。第七十観点 確認時には ファイルシステム使用率 と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第七十）（第七十観点）。第七十観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第七十観点）。第七十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0070へ書きます（第七十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> crfs 起動確認 ファイルシステム使用率 0070に関する障害切り分けの前提を確認しています。startsrc -s syslogd 属性確認 Subsystem 0071の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はSRCとログでstartsrc -s syslogdを用い・Subsystem とエラーログ一覧を確認する。</li><li>B. 表示や設定で扱う内容は性能管理でvmo -aを用い・pi とtopasディスク表示を確認する。</li><li>C. 表示や設定で扱う内容はJFS2でcrfsを用い・ファイルシステム使用率 とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容はSRCとログでstartsrc -s inetd -aを用い・syslog.confである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でcrfsを用い、ファイルシステム使用率 とファイルシステム属性を確認する」に対応する項目は起動確認 ファイルシステム使用率（起動・crfs）です。JFS2の仕様は「JFS2でcrfsを用い、ファイルシステム使用率」で、確認対象はcr・起動・ファです。属性・starのA:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は属性確認 Subsystem（属性・star）です。運用引・vmoのB:は「性能管理でvmo -aを用い、pi とtopasディスク表示を確認す」を述べ、対象は運用引継ぎ pi（運用・vmo）です。障害切・starのD:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け syslog.conf（障害・star）です。「crfs」は「JFS2でcrfsを用い、ファイルシステム使用率」を指し、起動確認 ファイルシステム使用率ではcr・起動・ファに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 起動確認 ファイルシステム使用率 0070</strong></p><p>検証目的: JFS2のcrfs 起動確認 ファイルシステム使用率 0070について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2起動確認070-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0070:
        dev             = /dev/fslv70
        vfs             = jfs2
        log             = INLINE
確認コード AIX0070A
画面・出力には AIX0070A が表示され、crfs 起動確認 ファイルシステム使用率 0070 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv70       16.00      9.42   42%     128     1% /data/aixdd0070
確認コード AIX0070B
画面・出力には AIX0070B が表示され、crfs 起動確認 ファイルシステム使用率 0070 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0070      --         /data/aixdd0070          jfs2  33554432 rw,log=INLINE
確認コード AIX0070C
画面・出力には AIX0070C が表示され、crfs 起動確認 ファイルシステム使用率 0070 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0070A が画面・出力に表示されること
② ステップ2 の AIX0070B が画面・出力に表示されること
③ ステップ3 の AIX0070C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0019"><h3>crfs 障害切り分け isnapshot 0040</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第四十観点 JFS2 で crfs は 障害切り分け を点検します（運用第四十）（第四十観点）。第四十観点 確認時には isnapshot と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第四十）（第四十観点）。第四十観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第四十観点）。第四十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0040へ書きます（第四十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> crfs 障害切り分け isnapshot 0040を同一分類のstartsrc -s syslogd バックアウト確認 IDENTIFIERと比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はSRCとログでstartsrc -s syslogdを用い・IDENTIFIERである。</li><li>B. 管理対象との関係を表す説明は性能管理でlparstat -iを用い・csz とvmstat表示を確認する。</li><li>C. 管理対象との関係を表す説明はSRCとログでstartsrc -s inetd -aを用い・Statusである。</li><li>D. 管理対象との関係を表す説明はJFS2でcrfsを用い・isnapshot とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でcrfsを用い、isnapshot とログデバイス設定を確認する」に対応する項目は障害切り分け isnapshot（障害・crfs）です。JFS2の仕様は「JFS2でcrfsを用い、isnapshot」で、確認対象はcr・障害切です。バック・starのA:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象はバックアウト確認 IDENTIFIE（バッ・star）です。状態・lparのB:は「性能管理でlparstat -iを用い、csz」を述べ、対象は状態確認 csz（状態・lpar）です。起動・starのC:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は起動確認 Status（起動・star）です。「crfs」は「JFS2でcrfsを用い、isnapshot」を指し、障害切り分け isnapshotではcr・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 障害切り分け isnapshot 0040</strong></p><p>検証目的: JFS2のcrfs 障害切り分け isnapshot 0040について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2障害切り分け040-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0040:
        dev             = /dev/fslv40
        vfs             = jfs2
        log             = INLINE
確認コード AIX0040A
画面・出力には AIX0040A が表示され、crfs 障害切り分け isnapshot 0040 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv40       16.00      9.42   42%     128     1% /data/aixdd0040
確認コード AIX0040B
画面・出力には AIX0040B が表示され、crfs 障害切り分け isnapshot 0040 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0040      --         /data/aixdd0040          jfs2  33554432 rw,log=INLINE
確認コード AIX0040C
画面・出力には AIX0040C が表示され、crfs 障害切り分け isnapshot 0040 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0040A が画面・出力に表示されること
② ステップ2 の AIX0040B が画面・出力に表示されること
③ ステップ3 の AIX0040C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0020"><h3>crfs 障害切り分け lff 0516</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第五百十六観点 JFS2 で crfs は 障害切り分け を点検します（運用第五百十六）（第五百十六観点）。第五百十六観点 確認時には lff と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第五百十六）（第五百十六観点）。第五百十六観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第五百十六観点）。第五百十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0516へ書きます（第五百十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> crfs 障害切り分け lff 0516の技術的な意味を資料で確認するとき、startsrc -s syslogd バックアウト確認 syslog.confとの境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はSRCとログでstartsrc -s syslogdを用い・syslog.confである。</li><li>B. 構成を確認する際の意味は性能管理でlparstat -iを用い・po とvmstat表示を確認する。</li><li>C. 構成を確認する際の意味はネットワークでlsdev -Cc adapterを用い・Gateway とMTU属性を確認する。</li><li>D. 構成を確認する際の意味はJFS2でcrfsを用い・lff とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でcrfsを用い、lff とログデバイス設定を確認する」に対応する項目は障害切り分け lff（障害・crfs）です。障害切に関するJFS2の仕様は「JFS2でcrfsを用い、lff とログデバイス設定を確認する」で、確認対象はcr・障害切です。バック・starのA:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象はバックアウト確認 syslog.co（バッ・star）です。状態・lparのB:は「性能管理でlparstat -iを用い、po」を述べ、対象は状態確認 po（状態・lpar）です。監査・lsdeのC:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は監査記録 Gateway（監査・lsde）です。「crfs」は「JFS2でcrfsを用い、lff とログデバイス設定を確認する」を指し、障害切り分け lffではcr・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>crfs 障害切り分け lff 0516</strong></p><p>検証目的: JFS2のcrfs 障害切り分け lff 0516について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2障害切り分け036-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; crfs
→ Enter を押す
［画面・出力］
/data/aixdd0516:
        dev             = /dev/fslv36
        vfs             = jfs2
        log             = INLINE
確認コード AIX0516A
画面・出力には AIX0516A が表示され、crfs 障害切り分け lff 0516 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv36       16.00      9.42   42%     128     1% /data/aixdd0516
確認コード AIX0516B
画面・出力には AIX0516B が表示され、crfs 障害切り分け lff 0516 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0516      --         /data/aixdd0516          jfs2  33554432 rw,log=INLINE
確認コード AIX0516C
画面・出力には AIX0516C が表示され、crfs 障害切り分け lff 0516 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0516A が画面・出力に表示されること
② ステップ2 の AIX0516B が画面・出力に表示されること
③ ステップ3 の AIX0516C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0021"><h3>defragfs バックアウト確認 lff 0267</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第二百六十七観点 JFS2 で defragfs は バックアウト確認 を点検します（運用第二百六十七）（第二百六十七観点）。第二百六十七観点 確認時には lff と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第二百六十七）（第二百六十七観点）。第二百六十七観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第二百六十七観点）。第二百六十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0267へ書きます（第二百六十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> defragfs バックアウト確認 lff 0267について構成や状態を確認します。lssrc -s syslogd 監査記録 TIMESTAMP 0268ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはSRCとログでlssrc -s syslogdを用い・TIMESTAMP とsyslog設定変換を確認する。</li><li>B. 状態を読み取るための働きは性能管理でfilemonを用い・po とAME統計を確認する。</li><li>C. 状態を読み取るための働きはLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>D. 状態を読み取るための働きはJFS2でdefragfsを用い・lff と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でdefragfsを用い、lff と内部スナップショットを確認する」に対応する項目はバックアウト確認 lff（バッ・defr）です。バックに関するJFS2の仕様は「JFS2でdefragfsを用い、lff」で、確認対象はde・バックです。監査・lssrのA:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は監査記録 TIMESTAMP（監査・lssr）です。構成・fileのB:は「性能管理でfilemonを用い、po とAME統計を確認する」を述べ、対象は構成照合 po（構成・file）です。状態・変更・lparのC:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は状態判定 変更証跡（状態・lpar）です。「defragfs」は「JFS2でdefragfsを用い、lff」を指し、バックアウト確認 lffではde・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>defragfs バックアウト確認 lff 0267</strong></p><p>検証目的: JFS2のdefragfs バックアウト確認 lff 0267について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2バックアウト確認027-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; defragfs
→ Enter を押す
［画面・出力］
/data/aixdd0267:
        dev             = /dev/fslv27
        vfs             = jfs2
        log             = INLINE
確認コード AIX0267A
画面・出力には AIX0267A が表示され、defragfs バックアウト確認 lff 0267 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv27       16.00      9.42   42%     128     1% /data/aixdd0267
確認コード AIX0267B
画面・出力には AIX0267B が表示され、defragfs バックアウト確認 lff 0267 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0267      --         /data/aixdd0267          jfs2  33554432 rw,log=INLINE
確認コード AIX0267C
画面・出力には AIX0267C が表示され、defragfs バックアウト確認 lff 0267 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0267A が画面・出力に表示されること
② ステップ2 の AIX0267B が画面・出力に表示されること
③ ステップ3 の AIX0267C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0022"><h3>defragfs バックアウト確認 lff 0327</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第三百二十七観点 JFS2 で defragfs は バックアウト確認 を点検します（運用第三百二十七）（第三百二十七観点）。第三百二十七観点 確認時には lff と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第三百二十七）（第三百二十七観点）。第三百二十七観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第三百二十七観点）。第三百二十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0327へ書きます（第三百二十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> defragfs バックアウト確認 lff 0327の設定や表示を読む前に役割を確認します。lssrc -s syslogd 監査記録 TIMESTAMP 0328ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはSRCとログでlssrc -s syslogdを用い・TIMESTAMP とsyslog設定変換を確認する。</li><li>B. 状態を読み取るための働きはJFS2でdefragfsを用い・lff と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きは性能管理でlparstat -iを用い・PhysB とAME統計を確認する。</li><li>D. 状態を読み取るための働きはネットワークでlsdev -Cc adapterを用い・Gateway と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でdefragfsを用い、lff と内部スナップショットを確認する」に対応する項目はバックアウト確認 lff（バッ・defr）です。バックに関するJFS2の仕様は「JFS2でdefragfsを用い、lff」で、確認対象はde・バックです。監査・lssrのA:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は監査記録 TIMESTAMP（監査・lssr）です。変更前・lparのC:は「性能管理でlparstat -iを用い、PhysB」を述べ、対象は変更前確認 PhysB（変更・lpar）です。容量・lsdeのD:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は容量確認 Gateway（容量・lsde）です。「defragfs」は「JFS2でdefragfsを用い、lff」を指し、バックアウト確認 lffではde・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>defragfs バックアウト確認 lff 0327</strong></p><p>検証目的: JFS2のdefragfs バックアウト確認 lff 0327について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2バックアウト確認087-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; defragfs
→ Enter を押す
［画面・出力］
/data/aixdd0327:
        dev             = /dev/fslv87
        vfs             = jfs2
        log             = INLINE
確認コード AIX0327A
画面・出力には AIX0327A が表示され、defragfs バックアウト確認 lff 0327 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv87       16.00      9.42   42%     128     1% /data/aixdd0327
確認コード AIX0327B
画面・出力には AIX0327B が表示され、defragfs バックアウト確認 lff 0327 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0327      --         /data/aixdd0327          jfs2  33554432 rw,log=INLINE
確認コード AIX0327C
画面・出力には AIX0327C が表示され、defragfs バックアウト確認 lff 0327 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0327A が画面・出力に表示されること
② ステップ2 の AIX0327B が画面・出力に表示されること
③ ステップ3 の AIX0327C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0023"><h3>defragfs バックアウト確認 log=INLINE 0743</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第七百四十三観点 JFS2 で defragfs は バックアウト確認 を点検します（運用第七百四十三）（第七百四十三観点）。第七百四十三観点 確認時には log=INLINE と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第七百四十三）（第七百四十三観点）。第七百四十三観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第七百四十三観点）。第七百四十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0743へ書きます（第七百四十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> defragfs バックアウト確認 log=INLINE 0743の設定や表示を読む前に役割を確認します。lssrc -s syslogd 監査記録 Subsystem 0744ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はSRCとログでlssrc -s syslogdを用い・Subsystem とsyslog設定変換を確認する。</li><li>B. 一次資料が示す主目的はデバイス管理でlsdev -Cc diskを用い・Available と診断対象表示を確認する。</li><li>C. 一次資料が示す主目的はJFS2でdefragfsを用い・log=INLINE と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はネットワークでcfgmgrを用い・EtherChannel と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でdefragfsを用い、log=INLINE」に対応する項目はバックアウト確認 log=INLIN（バッ・defr）です。バックに関するJFS2の仕様は「JFS2でdefragfsを用い、log=INLINE」で、確認対象はde・バックです。監査・lssrのA:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は監査記録 Subsystem（監査・lssr）です。起動・lsdeのB:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 Available（起動・lsde）です。運用引・cfgmのD:は「ネットワークでcfgmgrを用い、EtherChannel」を述べ、対象は運用引継ぎ EtherChannel（運用・cfgm）です。「defragfs」は「JFS2でdefragfsを用い、log=INLINE」を指し、バックアウト確認 log=INLINではde・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>defragfs バックアウト確認 log=INLINE 0743</strong></p><p>検証目的: JFS2のdefragfs バックアウト確認 log=INLINE 0743について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2バックアウト確認023-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; defragfs
→ Enter を押す
［画面・出力］
/data/aixdd0743:
        dev             = /dev/fslv23
        vfs             = jfs2
        log             = INLINE
確認コード AIX0743A
画面・出力には AIX0743A が表示され、defragfs バックアウト確認 log=INLINE 0743 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv23       16.00      9.42   42%     128     1% /data/aixdd0743
確認コード AIX0743B
画面・出力には AIX0743B が表示され、defragfs バックアウト確認 log=INLINE 0743 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0743      --         /data/aixdd0743          jfs2  33554432 rw,log=INLINE
確認コード AIX0743C
画面・出力には AIX0743C が表示され、defragfs バックアウト確認 log=INLINE 0743 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0743A が画面・出力に表示されること
② ステップ2 の AIX0743B が画面・出力に表示されること
③ ステップ3 の AIX0743C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0024"><h3>defragfs バックアウト確認 log=INLINE 0803</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第八百三観点 JFS2 で defragfs は バックアウト確認 を点検します（運用第八百三）（第八百三観点）。第八百三観点 確認時には log=INLINE と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第八百三）（第八百三観点）。第八百三観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第八百三観点）。第八百三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0803へ書きます（第八百三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> defragfs バックアウト確認 log=INLINE 0803について構成や状態を確認します。vmstat 復旧前確認 出力見出しではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はJFS2でdefragfsを用い・log=INLINE と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 一次資料が示す主目的はCPU・メモリー・ページング・AME 統計を表示する性能コマンドである。</li><li>C. 一次資料が示す主目的はデバイス管理でlsdev -Cc diskを用い・Available と診断対象表示を確認する。</li><li>D. 一次資料が示す主目的はSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> バック・defrでAの記述「JFS2でdefragfsを用い、log=INLINE」に対応する項目はバックアウト確認 log=INLIN（バッ・defr）です。バックに関するJFS2の仕様は「JFS2でdefragfsを用い、log=INLINE」で、確認対象はde・バックです。復旧前・vmstのB:は「CPU、メモリー、ページング、AME 統計を表示する性能コマンド」を述べ、対象は復旧前確認 出力見出し（復旧・vmst）です。起動・lsdeのC:は「デバイス管理でlsdev -Cc diskを用い」を述べ、対象は起動確認 Available（起動・lsde）です。構成・tailのD:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は構成照合 IDENTIFIER（構成・tail）です。「defragfs」は「JFS2でdefragfsを用い、log=INLINE」を指し、バックアウト確認 log=INLINではde・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>defragfs バックアウト確認 log=INLINE 0803</strong></p><p>検証目的: JFS2のdefragfs バックアウト確認 log=INLINE 0803について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2バックアウト確認083-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; defragfs
→ Enter を押す
［画面・出力］
/data/aixdd0803:
        dev             = /dev/fslv83
        vfs             = jfs2
        log             = INLINE
確認コード AIX0803A
画面・出力には AIX0803A が表示され、defragfs バックアウト確認 log=INLINE 0803 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv83       16.00      9.42   42%     128     1% /data/aixdd0803
確認コード AIX0803B
画面・出力には AIX0803B が表示され、defragfs バックアウト確認 log=INLINE 0803 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0803      --         /data/aixdd0803          jfs2  33554432 rw,log=INLINE
確認コード AIX0803C
画面・出力には AIX0803C が表示され、defragfs バックアウト確認 log=INLINE 0803 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0803A が画面・出力に表示されること
② ステップ2 の AIX0803B が画面・出力に表示されること
③ ステップ3 の AIX0803C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0025"><h3>defragfs 変更後確認 mountguard 0456</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第四百五十六観点 JFS2 で defragfs は 変更後確認 を点検します（運用第四百五十六）（第四百五十六観点）。第四百五十六観点 確認時には mountguard と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第四百五十六）（第四百五十六観点）。第四百五十六観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第四百五十六観点）。第四百五十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0456へ書きます（第四百五十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> defragfs 変更後確認 mountguard 0456を同一分類のlssrc -s syslogd 障害切り分け TIMESTAMP 0457と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はSRCとログでlssrc -s syslogdを用い・TIMESTAMP とinetdデバッグ出力を確認する。</li><li>B. 構成を確認する際の意味は性能管理でlparstat -iを用い・avm とvmstat表示を確認する。</li><li>C. 構成を確認する際の意味はネットワークでlsdev -Cc adapterを用い・Gateway とMTU属性を確認する。</li><li>D. 構成を確認する際の意味はJFS2でdefragfsを用い・mountguard とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でdefragfsを用い、mountguard とログデバイス設定を確認する」に対応する項目は変更後確認 mountguard（変更・defr）です。変更後に関するJFS2の仕様は「JFS2でdefragfsを用い、mountguard」で、確認対象はde・変更後です。障害切・lssrのA:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は障害切り分け TIMESTAMP（障害・lssr）です。状態・lparのB:は「性能管理でlparstat -iを用い、avm」を述べ、対象は状態確認 avm（状態・lpar）です。監査・lsdeのC:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は監査記録 Gateway（監査・lsde）です。「defragfs」は「JFS2でdefragfsを用い、mountguard」を指し、変更後確認 mountguardではde・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>defragfs 変更後確認 mountguard 0456</strong></p><p>検証目的: JFS2のdefragfs 変更後確認 mountguard 0456について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更後確認096-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; defragfs
→ Enter を押す
［画面・出力］
/data/aixdd0456:
        dev             = /dev/fslv96
        vfs             = jfs2
        log             = INLINE
確認コード AIX0456A
画面・出力には AIX0456A が表示され、defragfs 変更後確認 mountguard 0456 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv96       16.00      9.42   42%     128     1% /data/aixdd0456
確認コード AIX0456B
画面・出力には AIX0456B が表示され、defragfs 変更後確認 mountguard 0456 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0456      --         /data/aixdd0456          jfs2  33554432 rw,log=INLINE
確認コード AIX0456C
画面・出力には AIX0456C が表示され、defragfs 変更後確認 mountguard 0456 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0456A が画面・出力に表示されること
② ステップ2 の AIX0456B が画面・出力に表示されること
③ ステップ3 の AIX0456C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0026"><h3>defragfs 属性確認 agblksize 0297</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第二百九十七観点 JFS2 で defragfs は 属性確認 を点検します（運用第二百九十七）（第二百九十七観点）。第二百九十七観点 確認時には agblksize と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第二百九十七）（第二百九十七観点）。第二百九十七観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第二百九十七観点）。第二百九十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0297へ書きます（第二百九十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「defragfs 属性確認 agblksize 0297」を「lssrc -s syslogd 状態確認 PID 0298」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はJFS2でdefragfsを用い・agblksize とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はSRCとログでlssrc -s syslogdを用い・PID とSRCサブシステム表示を確認する。</li><li>C. 運用時に利用する技術的役割は性能管理でlparstat -iを用い・fre とsvmon全体表示を確認する。</li><li>D. 運用時に利用する技術的役割はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「JFS2でdefragfsを用い、agblksize とマウントオプションを確認する」に対応する項目は属性確認 agblksize（属性・defr）です。属性に関するJFS2の仕様は「JFS2でdefragfsを用い、agblksize」で、確認対象はde・属性です。状態・lssrのB:は「SRCとログでlssrc -s syslogdを用い、PID」を述べ、対象は状態確認 PID（状態・lssr）です。容量・lparのC:は「性能管理でlparstat -iを用い、fre」を述べ、対象は容量確認 fre（容量・lpar）です。属性・受信・lparのD:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は属性照合 受信先（属性・lpar）です。「defragfs」は「JFS2でdefragfsを用い、agblksize」を指し、属性確認 agblksizeではde・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>defragfs 属性確認 agblksize 0297</strong></p><p>検証目的: JFS2のdefragfs 属性確認 agblksize 0297について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2属性確認057-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; defragfs
→ Enter を押す
［画面・出力］
/data/aixdd0297:
        dev             = /dev/fslv57
        vfs             = jfs2
        log             = INLINE
確認コード AIX0297A
画面・出力には AIX0297A が表示され、defragfs 属性確認 agblksize 0297 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv57       16.00      9.42   42%     128     1% /data/aixdd0297
確認コード AIX0297B
画面・出力には AIX0297B が表示され、defragfs 属性確認 agblksize 0297 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0297      --         /data/aixdd0297          jfs2  33554432 rw,log=INLINE
確認コード AIX0297C
画面・出力には AIX0297C が表示され、defragfs 属性確認 agblksize 0297 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0297A が画面・出力に表示されること
② ステップ2 の AIX0297B が画面・出力に表示されること
③ ステップ3 の AIX0297C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0027"><h3>defragfs 属性確認 mountguard 0773</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第七百七十三観点 JFS2 で defragfs は 属性確認 を点検します（運用第七百七十三）（第七百七十三観点）。第七百七十三観点 確認時には mountguard と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第七百七十三）（第七百七十三観点）。第七百七十三観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第七百七十三観点）。第七百七十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0773へ書きます（第七百七十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> defragfs 属性確認 mountguard 0773を保守記録に説明する必要があります。lslv 構成照合 STALE PARTITIONS 0787と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はJFS2でdefragfsを用い・mountguard とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割はLVMでlslvを用い・STALE PARTITIONS とボリュームグループ属性を確認する。</li><li>C. 仕様上の役割はLVMでchvgを用い・STALE PARTITIONS と物理ボリューム一覧を確認する。</li><li>D. 仕様上の役割はデバイス管理でodmget CuDvを用い・attribute と構成マネージャー結果を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 属性・defrでAの記述「JFS2でdefragfsを用い、mountguard」に対応する項目は属性確認 mountguard（属性・defr）です。属性に関するJFS2の仕様は「JFS2でdefragfsを用い、mountguard」で、確認対象はde・属性です。構成・lslvのB:は「LVMでlslvを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（構成・lslv）です。運用引・chvgのC:は「LVMでchvgを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（運用・chvg）です。状態・odmgのD:は「デバイス管理でodmget CuDvを用い、attribute」を述べ、対象は状態確認 attribute（状態・odmg）です。「defragfs」は「JFS2でdefragfsを用い、mountguard」を指し、属性確認 mountguardではde・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>defragfs 属性確認 mountguard 0773</strong></p><p>検証目的: JFS2のdefragfs 属性確認 mountguard 0773について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2属性確認053-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; defragfs
→ Enter を押す
［画面・出力］
/data/aixdd0773:
        dev             = /dev/fslv53
        vfs             = jfs2
        log             = INLINE
確認コード AIX0773A
画面・出力には AIX0773A が表示され、defragfs 属性確認 mountguard 0773 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv53       16.00      9.42   42%     128     1% /data/aixdd0773
確認コード AIX0773B
画面・出力には AIX0773B が表示され、defragfs 属性確認 mountguard 0773 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0773      --         /data/aixdd0773          jfs2  33554432 rw,log=INLINE
確認コード AIX0773C
画面・出力には AIX0773C が表示され、defragfs 属性確認 mountguard 0773 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0773A が画面・出力に表示されること
② ステップ2 の AIX0773B が画面・出力に表示されること
③ ステップ3 の AIX0773C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0028"><h3>defragfs 運用引継ぎ lff 0138</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第百三十八観点 JFS2 で defragfs は 運用引継ぎ を点検します（運用第百三十八）（第百三十八観点）。第百三十八観点 確認時には lff と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第百三十八）（第百三十八観点）。第百三十八観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第百三十八観点）。第百三十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0138へ書きます（第百三十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> defragfs 運用引継ぎ lff 0138の役割を調べています。lssrc -s syslogd 容量確認 syslog.conf 0139の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはJFS2でdefragfsを用い・lff とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 機能の説明としてはSRCとログでlssrc -s syslogdを用い・syslog.conf とエラーログ一覧を確認する。</li><li>C. 機能の説明としては性能管理でfilemonを用い・avm とtopasディスク表示を確認する。</li><li>D. 機能の説明としてはSRCとログでerrclearを用い・TIMESTAMP とエラーログ一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「JFS2でdefragfsを用い、lff とファイルシステム属性を確認する」に対応する項目は運用引継ぎ lff（運用・defr）です。運用引に関するJFS2の仕様は「JFS2でdefragfsを用い、lff」で、確認対象はde・運用引です。容量・lssrのB:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は容量確認 syslog.conf（容量・lssr）です。変更後・fileのC:は「性能管理でfilemonを用い、avm とtopasディスク表示を確」を述べ、対象は変更後確認 avm（変更・file）です。構成・errcのD:は「SRCとログでerrclearを用い、TIMESTAMP」を述べ、対象は構成照合 TIMESTAMP（構成・errc）です。「defragfs」は「JFS2でdefragfsを用い、lff」を指し、運用引継ぎ lffではde・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>defragfs 運用引継ぎ lff 0138</strong></p><p>検証目的: JFS2のdefragfs 運用引継ぎ lff 0138について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2運用引継ぎ018-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; defragfs
→ Enter を押す
［画面・出力］
/data/aixdd0138:
        dev             = /dev/fslv18
        vfs             = jfs2
        log             = INLINE
確認コード AIX0138A
画面・出力には AIX0138A が表示され、defragfs 運用引継ぎ lff 0138 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv18       16.00      9.42   42%     128     1% /data/aixdd0138
確認コード AIX0138B
画面・出力には AIX0138B が表示され、defragfs 運用引継ぎ lff 0138 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0138      --         /data/aixdd0138          jfs2  33554432 rw,log=INLINE
確認コード AIX0138C
画面・出力には AIX0138C が表示され、defragfs 運用引継ぎ lff 0138 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0138A が画面・出力に表示されること
② ステップ2 の AIX0138B が画面・出力に表示されること
③ ステップ3 の AIX0138C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0029"><h3>defragfs 運用引継ぎ log=INLINE 0614</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第六百十四観点 JFS2 で defragfs は 運用引継ぎ を点検します（運用第六百十四）（第六百十四観点）。第六百十四観点 確認時には log=INLINE と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第六百十四）（第六百十四観点）。第六百十四観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第六百十四観点）。第六百十四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0614へ書きます（第六百十四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> defragfs 運用引継ぎ log=INLINE 0614に関する障害切り分けの前提を確認しています。lssrc -s syslogd 容量確認 PID 0615の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はJFS2でdefragfsを用い・log=INLINE とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 障害切り分けに用いる役割はSRCとログでlssrc -s syslogdを用い・PID とエラーログ一覧を確認する。</li><li>C. 障害切り分けに用いる役割はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>D. 障害切り分けに用いる役割はネットワークでcfgmgrを用い・Link Status とEthernet統計を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「JFS2でdefragfsを用い、log=INLINE」に対応する項目は運用引継ぎ log=INLINE（運用・defr）です。運用引に関するJFS2の仕様は「JFS2でdefragfsを用い、log=INLINE」で、確認対象はde・運用引です。容量・lssrのB:は「SRCとログでlssrc -s syslogdを用い、PID」を述べ、対象は容量確認 PID（容量・lssr）です。変更前・lparのC:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は変更前確認 キュー状態（変更・lpar）です。性能・cfgmのD:は「ネットワークでcfgmgrを用い、Link Status」を述べ、対象はLink Status（性能・cfgm）です。「defragfs」は「JFS2でdefragfsを用い、log=INLINE」を指し、運用引継ぎ log=INLINEではde・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>defragfs 運用引継ぎ log=INLINE 0614</strong></p><p>検証目的: JFS2のdefragfs 運用引継ぎ log=INLINE 0614について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2運用引継ぎ014-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; defragfs
→ Enter を押す
［画面・出力］
/data/aixdd0614:
        dev             = /dev/fslv14
        vfs             = jfs2
        log             = INLINE
確認コード AIX0614A
画面・出力には AIX0614A が表示され、defragfs 運用引継ぎ log=INLINE 0614 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv14       16.00      9.42   42%     128     1% /data/aixdd0614
確認コード AIX0614B
画面・出力には AIX0614B が表示され、defragfs 運用引継ぎ log=INLINE 0614 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0614      --         /data/aixdd0614          jfs2  33554432 rw,log=INLINE
確認コード AIX0614C
画面・出力には AIX0614C が表示され、defragfs 運用引継ぎ log=INLINE 0614 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0614A が画面・出力に表示されること
② ステップ2 の AIX0614B が画面・出力に表示されること
③ ステップ3 の AIX0614C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0030"><h3>df -g バックアウト確認 mountguard 0184</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第百八十四観点 JFS2 で df -g は バックアウト確認 を点検します（運用第百八十四）（第百八十四観点）。第百八十四観点 確認時には mountguard と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第百八十四）（第百八十四観点）。第百八十四観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第百八十四観点）。第百八十四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0184へ書きます（第百八十四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> df -g バックアウト確認 mountguard 0184を同一分類のerrpt -a 監査記録 TIMESTAMP 0185と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はSRCとログでerrpt -aを用い・TIMESTAMP とinetdデバッグ出力を確認する。</li><li>B. 管理対象との関係を表す説明は性能管理でtopas -Dを用い・Busy% とvmstat表示を確認する。</li><li>C. 管理対象との関係を表す説明はJFS2でdf -gを用い・mountguard とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はSRCとログでsyslog_ssw -cを用い・IDENTIFIER とinetdデバッグ出力を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でdf -gを用い、mountguard とログデバイス設定を確認する」に対応する項目はバックアウト確認 mountguar（バッ・df）です。バックに関するJFS2の仕様は「JFS2でdf -gを用い、mountguard」で、確認対象はdf・バックです。監査・errpのA:は「SRCとログでerrpt -aを用い、TIMESTAMP」を述べ、対象は監査記録 TIMESTAMP（監査・errp）です。変更前・topaのB:は「性能管理でtopas -Dを用い、Busy%」を述べ、対象は変更前確認 Busy%（変更・topa）です。属性・syslのD:は「SRCとログでsyslog_ssw -cを用い」を述べ、対象は属性確認 IDENTIFIER（属性・sysl）です。「df -g」は「JFS2でdf -gを用い、mountguard」を指し、バックアウト確認 mountguarではdf・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>df -g バックアウト確認 mountguard 0184</strong></p><p>検証目的: JFS2のdf -g バックアウト確認 mountguard 0184について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2バックアウト確認064-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g
→ Enter を押す
［画面・出力］
/data/aixdd0184:
        dev             = /dev/fslv64
        vfs             = jfs2
        log             = INLINE
確認コード AIX0184A
画面・出力には AIX0184A が表示され、df -g バックアウト確認 mountguard 0184 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv64       16.00      9.42   42%     128     1% /data/aixdd0184
確認コード AIX0184B
画面・出力には AIX0184B が表示され、df -g バックアウト確認 mountguard 0184 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0184      --         /data/aixdd0184          jfs2  33554432 rw,log=INLINE
確認コード AIX0184C
画面・出力には AIX0184C が表示され、df -g バックアウト確認 mountguard 0184 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0184A が画面・出力に表示されること
② ステップ2 の AIX0184B が画面・出力に表示されること
③ ステップ3 の AIX0184C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0031"><h3>df -g バックアウト確認 ファイルシステム使用率 0660</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第六百六十観点 JFS2 で df -g は バックアウト確認 を点検します（運用第六百六十）（第六百六十観点）。第六百六十観点 確認時には ファイルシステム使用率 と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第六百六十）（第六百六十観点）。第六百六十観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第六百六十観点）。第六百六十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0660へ書きます（第六百六十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> df -g バックアウト確認 ファイルシステム使用率 0660の技術的な意味を資料で確認するとき、errpt -a 監査記録 Subsystem 0661との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はSRCとログでerrpt -aを用い・Subsystem とinetdデバッグ出力を確認する。</li><li>B. 構成を確認する際の意味はJFS2でdf -gを用い・ファイルシステム使用率 とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はデバイス管理でdiag -d ent0を用い・microcode level とデバイス一覧を確認する。</li><li>D. 構成を確認する際の意味はネットワークでnetstat -vを用い・EtherChannel とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でdf -gを用い、ファイルシステム使用率 とログデバイス設定を確認する」に対応する項目はバックアウト確認 ファイルシステム使（バッ・df）です。バック・ファイに関するJFS2の仕様は「JFS2でdf -gを用い、ファイルシステム使用率」で、確認対象はdf・バックです。監査・errpのA:は「SRCとログでerrpt -aを用い、Subsystem」を述べ、対象は監査記録 Subsystem（監査・errp）です。起動・diagのC:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（起動・diag）です。運用引・netsのD:は「ネットワークでnetstat -vを用い、EtherChannel」を述べ、対象は運用引継ぎ EtherChannel（運用・nets）です。「df -g」は「JFS2でdf -gを用い、ファイルシステム使用率」を指し、バックアウト確認 ファイルシステム使ではdf・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>df -g バックアウト確認 ファイルシステム使用率 0660</strong></p><p>検証目的: JFS2のdf -g バックアウト確認 ファイルシステム使用率 0660について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2バックアウト確認060-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g
→ Enter を押す
［画面・出力］
/data/aixdd0660:
        dev             = /dev/fslv60
        vfs             = jfs2
        log             = INLINE
確認コード AIX0660A
画面・出力には AIX0660A が表示され、df -g バックアウト確認 ファイルシステム使用率 0660 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv60       16.00      9.42   42%     128     1% /data/aixdd0660
確認コード AIX0660B
画面・出力には AIX0660B が表示され、df -g バックアウト確認 ファイルシステム使用率 0660 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0660      --         /data/aixdd0660          jfs2  33554432 rw,log=INLINE
確認コード AIX0660C
画面・出力には AIX0660C が表示され、df -g バックアウト確認 ファイルシステム使用率 0660 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0660A が画面・出力に表示されること
② ステップ2 の AIX0660B が画面・出力に表示されること
③ ステップ3 の AIX0660C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0032"><h3>df -g バックアウト確認 ファイルシステム使用率 0720</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第七百二十観点 JFS2 で df -g は バックアウト確認 を点検します（運用第七百二十）（第七百二十観点）。第七百二十観点 確認時には ファイルシステム使用率 と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第七百二十）（第七百二十観点）。第七百二十観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第七百二十観点）。第七百二十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0720へ書きます（第七百二十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> df -g バックアウト確認 ファイルシステム使用率 0720を同一分類のerrclear 運用引継ぎ PID 0721と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はJFS2でdf -gを用い・ファイルシステム使用率 とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はSRCとログでerrclearを用い・PID とinetdデバッグ出力を確認する。</li><li>C. 構成を確認する際の意味はデバイス管理でdiag -d ent0を用い・microcode level とデバイス一覧を確認する。</li><li>D. 構成を確認する際の意味はネットワークでsmitty etherchannelを用い・Link Status とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「JFS2でdf -gを用い、ファイルシステム使用率 とログデバイス設定を確認する」に対応する項目はバックアウト確認 ファイルシステム使（バッ・df）です。バック・ファイに関するJFS2の仕様は「JFS2でdf -gを用い、ファイルシステム使用率」で、確認対象はdf・バックです。運用引・errcのB:は「SRCとログでerrclearを用い、PID」を述べ、対象は運用引継ぎ PID（運用・errc）です。起動・diagのC:は「デバイス管理でdiag -d ent0を用い、microcode」を述べ、対象はmicrocode level（起動・diag）です。容量・smitのD:は「ネットワークでsmitty etherchannelを用い」を述べ、対象はLink Status（容量・smit）です。「df -g」は「JFS2でdf -gを用い、ファイルシステム使用率」を指し、バックアウト確認 ファイルシステム使ではdf・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>df -g バックアウト確認 ファイルシステム使用率 0720</strong></p><p>検証目的: JFS2のdf -g バックアウト確認 ファイルシステム使用率 0720について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2バックアウト確認120-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g
→ Enter を押す
［画面・出力］
/data/aixdd0720:
        dev             = /dev/fslv120
        vfs             = jfs2
        log             = INLINE
確認コード AIX0720A
画面・出力には AIX0720A が表示され、df -g バックアウト確認 ファイルシステム使用率 0720 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv120       16.00      9.42   42%     128     1% /data/aixdd0720
確認コード AIX0720B
画面・出力には AIX0720B が表示され、df -g バックアウト確認 ファイルシステム使用率 0720 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0720      --         /data/aixdd0720          jfs2  33554432 rw,log=INLINE
確認コード AIX0720C
画面・出力には AIX0720C が表示され、df -g バックアウト確認 ファイルシステム使用率 0720 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0720A が画面・出力に表示されること
② ステップ2 の AIX0720B が画面・出力に表示されること
③ ステップ3 の AIX0720C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0033"><h3>df -g 属性確認 isnapshot 0690</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第六百九十観点 JFS2 で df -g は 属性確認 を点検します（運用第六百九十）（第六百九十観点）。第六百九十観点 確認時には isnapshot と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第六百九十）（第六百九十観点）。第六百九十観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第六百九十観点）。第六百九十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0690へ書きます（第六百九十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> df -g 属性確認 isnapshot 0690の役割を調べています。errpt -a 状態確認 IDENTIFIER 0691の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはSRCとログでerrpt -aを用い・IDENTIFIER とエラーログ一覧を確認する。</li><li>B. 機能の説明としてはデバイス管理でdiag -d ent0を用い・attribute と構成マネージャー結果を確認する。</li><li>C. 機能の説明としてはJFS2でdf -gを用い・isnapshot とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはネットワークでsmitty etherchannelを用い・Destinationである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でdf -gを用い、isnapshot とファイルシステム属性を確認する」に対応する項目は属性確認 isnapshot（属性・df）です。属性に関するJFS2の仕様は「JFS2でdf -gを用い、isnapshot」で、確認対象はdf・属性です。状態・errpのA:は「SRCとログでerrpt -aを用い、IDENTIFIER」を述べ、対象は状態確認 IDENTIFIER（状態・errp）です。障害切・diagのB:は「デバイス管理でdiag -d ent0を用い、attribute」を述べ、対象は障害切り分け attribute（障害・diag）です。変更前・smitのD:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は変更前確認 Destination（変更・smit）です。「df -g」は「JFS2でdf -gを用い、isnapshot」を指し、属性確認 isnapshotではdf・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>df -g 属性確認 isnapshot 0690</strong></p><p>検証目的: JFS2のdf -g 属性確認 isnapshot 0690について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2属性確認090-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g
→ Enter を押す
［画面・出力］
/data/aixdd0690:
        dev             = /dev/fslv90
        vfs             = jfs2
        log             = INLINE
確認コード AIX0690A
画面・出力には AIX0690A が表示され、df -g 属性確認 isnapshot 0690 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv90       16.00      9.42   42%     128     1% /data/aixdd0690
確認コード AIX0690B
画面・出力には AIX0690B が表示され、df -g 属性確認 isnapshot 0690 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0690      --         /data/aixdd0690          jfs2  33554432 rw,log=INLINE
確認コード AIX0690C
画面・出力には AIX0690C が表示され、df -g 属性確認 isnapshot 0690 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0690A が画面・出力に表示されること
② ステップ2 の AIX0690B が画面・出力に表示されること
③ ステップ3 の AIX0690C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0034"><h3>df -g 属性確認 log=INLINE 0214</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第二百十四観点 JFS2 で df -g は 属性確認 を点検します（運用第二百十四）（第二百十四観点）。第二百十四観点 確認時には log=INLINE と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第二百十四）（第二百十四観点）。第二百十四観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第二百十四観点）。第二百十四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0214へ書きます（第二百十四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> df -g 属性確認 log=INLINE 0214に関する障害切り分けの前提を確認しています。errpt -a 状態確認 PID 0215の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はSRCとログでerrpt -aを用い・PID とエラーログ一覧を確認する。</li><li>B. 表示や設定で扱う内容は性能管理でtopas -Dを用い・po とtopasディスク表示を確認する。</li><li>C. 表示や設定で扱う内容はSRCとログでsyslog_ssw -cを用い・Subsystem とエラーログ一覧を確認する。</li><li>D. 表示や設定で扱う内容はJFS2でdf -gを用い・log=INLINE とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でdf -gを用い、log=INLINE とファイルシステム属性を確認する」に対応する項目は属性確認 log=INLINE（属性・df）です。属性に関するJFS2の仕様は「JFS2でdf -gを用い、log=INLINE」で、確認対象はdf・属性です。状態・errpのA:は「SRCとログでerrpt -aを用い、PID」を述べ、対象は状態確認 PID（状態・errp）です。容量・topaのB:は「性能管理でtopas -Dを用い、po とtopasディスク表示を確」を述べ、対象は容量確認 po（容量・topa）です。バック・syslのC:は「SRCとログでsyslog_ssw -cを用い、Subsystem」を述べ、対象はバックアウト確認 Subsystem（バッ・sysl）です。「df -g」は「JFS2でdf -gを用い、log=INLINE」を指し、属性確認 log=INLINEではdf・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>df -g 属性確認 log=INLINE 0214</strong></p><p>検証目的: JFS2のdf -g 属性確認 log=INLINE 0214について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2属性確認094-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g
→ Enter を押す
［画面・出力］
/data/aixdd0214:
        dev             = /dev/fslv94
        vfs             = jfs2
        log             = INLINE
確認コード AIX0214A
画面・出力には AIX0214A が表示され、df -g 属性確認 log=INLINE 0214 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv94       16.00      9.42   42%     128     1% /data/aixdd0214
確認コード AIX0214B
画面・出力には AIX0214B が表示され、df -g 属性確認 log=INLINE 0214 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0214      --         /data/aixdd0214          jfs2  33554432 rw,log=INLINE
確認コード AIX0214C
画面・出力には AIX0214C が表示され、df -g 属性確認 log=INLINE 0214 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0214A が画面・出力に表示されること
② ステップ2 の AIX0214B が画面・出力に表示されること
③ ステップ3 の AIX0214C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0035"><h3>df -g 構成照合 agblksize 0025</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第二十五観点 JFS2 で df -g は 構成照合 を点検します（運用第二十五）（第二十五観点）。第二十五観点 確認時には agblksize と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第二十五）（第二十五観点）。第二十五観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第二十五観点）。第二十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0025へ書きます（第二十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「df -g 構成照合 agblksize 0025」を「errpt -a 変更前確認 PID 0026」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はSRCとログでerrpt -aを用い・PID とSRCサブシステム表示を確認する。</li><li>B. 保守作業で参照する機能は性能管理でiostat -Dl 2 2を用い・Busy% とsvmon全体表示を確認する。</li><li>C. 保守作業で参照する機能はSRCとログでsyslog_ssw -cを用い・Subsystem とSRCサブシステム表示を確認する。</li><li>D. 保守作業で参照する機能はJFS2でdf -gを用い・agblksize とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でdf -gを用い、agblksize とマウントオプションを確認する」に対応する項目は構成照合 agblksize（構成・df）です。JFS2の仕様は「JFS2でdf -gを用い、agblksize」で、確認対象はdf・構成です。変更前・errpのA:は「SRCとログでerrpt -aを用い、PID」を述べ、対象は変更前確認 PID（変更・errp）です。性能・iostのB:は「性能管理でiostat -Dl 2 2を用い、Busy%」を述べ、対象は性能確認 Busy%（性能・iost）です。運用引・syslのC:は「SRCとログでsyslog_ssw -cを用い、Subsystem」を述べ、対象は運用引継ぎ Subsystem（運用・sysl）です。「df -g」は「JFS2でdf -gを用い、agblksize」を指し、構成照合 agblksizeではdf・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>df -g 構成照合 agblksize 0025</strong></p><p>検証目的: JFS2のdf -g 構成照合 agblksize 0025について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2構成照合025-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g
→ Enter を押す
［画面・出力］
/data/aixdd0025:
        dev             = /dev/fslv25
        vfs             = jfs2
        log             = INLINE
確認コード AIX0025A
画面・出力には AIX0025A が表示され、df -g 構成照合 agblksize 0025 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv25       16.00      9.42   42%     128     1% /data/aixdd0025
確認コード AIX0025B
画面・出力には AIX0025B が表示され、df -g 構成照合 agblksize 0025 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0025      --         /data/aixdd0025          jfs2  33554432 rw,log=INLINE
確認コード AIX0025C
画面・出力には AIX0025C が表示され、df -g 構成照合 agblksize 0025 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0025A が画面・出力に表示されること
② ステップ2 の AIX0025B が画面・出力に表示されること
③ ステップ3 の AIX0025C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0036"><h3>df -g 構成照合 mountguard 0501</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第五百一観点 JFS2 で df -g は 構成照合 を点検します（運用第五百一）（第五百一観点）。第五百一観点 確認時には mountguard と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第五百一）（第五百一観点）。第五百一観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第五百一観点）。第五百一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0501へ書きます（第五百一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> df -g 構成照合 mountguard 0501を保守記録に説明する必要があります。errpt -a 変更前確認 IDENTIFIER 0502と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はSRCとログでerrpt -aを用い・IDENTIFIER とSRCサブシステム表示を確認する。</li><li>B. 運用時に利用する技術的役割は性能管理でiostat -Dl 2 2を用い・dxm とsvmon全体表示を確認する。</li><li>C. 運用時に利用する技術的役割はJFS2でdf -gを用い・mountguard とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はネットワークでnetstat -vを用い・MTU とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「JFS2でdf -gを用い、mountguard とマウントオプションを確認する」に対応する項目は構成照合 mountguard（構成・df）です。構成に関するJFS2の仕様は「JFS2でdf -gを用い、mountguard」で、確認対象はdf・構成です。変更前・errpのA:は「SRCとログでerrpt -aを用い、IDENTIFIER」を述べ、対象は変更前確認 IDENTIFIER（変更・errp）です。性能・iostのB:は「性能管理でiostat -Dl 2 2を用い、dxm」を述べ、対象は性能確認 dxm（性能・iost）です。変更後・netsのD:は「ネットワークでnetstat -vを用い、MTU」を述べ、対象は変更後確認 MTU（変更・nets）です。「df -g」は「JFS2でdf -gを用い、mountguard」を指し、構成照合 mountguardではdf・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>df -g 構成照合 mountguard 0501</strong></p><p>検証目的: JFS2のdf -g 構成照合 mountguard 0501について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2構成照合021-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g
→ Enter を押す
［画面・出力］
/data/aixdd0501:
        dev             = /dev/fslv21
        vfs             = jfs2
        log             = INLINE
確認コード AIX0501A
画面・出力には AIX0501A が表示され、df -g 構成照合 mountguard 0501 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv21       16.00      9.42   42%     128     1% /data/aixdd0501
確認コード AIX0501B
画面・出力には AIX0501B が表示され、df -g 構成照合 mountguard 0501 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0501      --         /data/aixdd0501          jfs2  33554432 rw,log=INLINE
確認コード AIX0501C
画面・出力には AIX0501C が表示され、df -g 構成照合 mountguard 0501 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0501A が画面・出力に表示されること
② ステップ2 の AIX0501B が画面・出力に表示されること
③ ステップ3 の AIX0501C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0037"><h3>df -g 運用引継ぎ lff 0055</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第五十五観点 JFS2 で df -g は 運用引継ぎ を点検します（運用第五十五）（第五十五観点）。第五十五観点 確認時には lff と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第五十五）（第五十五観点）。第五十五観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第五十五観点）。第五十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0055へ書きます（第五十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> df -g 運用引継ぎ lff 0055の設定や表示を読む前に役割を確認します。errpt -a 容量確認 TIMESTAMP 0056ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはSRCとログでerrpt -aを用い・TIMESTAMP とsyslog設定変換を確認する。</li><li>B. 対象資源に対する働きはJFS2でdf -gを用い・lff と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きは性能管理でtopas -Dを用い・csz とAME統計を確認する。</li><li>D. 対象資源に対する働きはSRCとログでsyslog_ssw -cを用い・IDENTIFIER とsyslog設定変換を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でdf -gを用い、lff と内部スナップショットを確認する」に対応する項目は運用引継ぎ lff（運用・df）です。JFS2の仕様は「JFS2でdf -gを用い、lff と内部スナップショットを確認する」で、確認対象はdf・運用引です。容量・errpのA:は「SRCとログでerrpt -aを用い、TIMESTAMP」を述べ、対象は容量確認 TIMESTAMP（容量・errp）です。障害切・topaのC:は「性能管理でtopas -Dを用い、csz とAME統計を確認する」を述べ、対象は障害切り分け csz（障害・topa）です。構成・syslのD:は「SRCとログでsyslog_ssw -cを用い」を述べ、対象は構成照合 IDENTIFIER（構成・sysl）です。「df -g」は「JFS2でdf -gを用い、lff と内部スナップショットを確認する」を指し、運用引継ぎ lffではdf・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>df -g 運用引継ぎ lff 0055</strong></p><p>検証目的: JFS2のdf -g 運用引継ぎ lff 0055について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2運用引継ぎ055-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g
→ Enter を押す
［画面・出力］
/data/aixdd0055:
        dev             = /dev/fslv55
        vfs             = jfs2
        log             = INLINE
確認コード AIX0055A
画面・出力には AIX0055A が表示され、df -g 運用引継ぎ lff 0055 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv55       16.00      9.42   42%     128     1% /data/aixdd0055
確認コード AIX0055B
画面・出力には AIX0055B が表示され、df -g 運用引継ぎ lff 0055 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0055      --         /data/aixdd0055          jfs2  33554432 rw,log=INLINE
確認コード AIX0055C
画面・出力には AIX0055C が表示され、df -g 運用引継ぎ lff 0055 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0055A が画面・出力に表示されること
② ステップ2 の AIX0055B が画面・出力に表示されること
③ ステップ3 の AIX0055C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0038"><h3>df -g 運用引継ぎ log=INLINE 0531</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第五百三十一観点 JFS2 で df -g は 運用引継ぎ を点検します（運用第五百三十一）（第五百三十一観点）。第五百三十一観点 確認時には log=INLINE と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第五百三十一）（第五百三十一観点）。第五百三十一観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第五百三十一観点）。第五百三十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0531へ書きます（第五百三十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> df -g 運用引継ぎ log=INLINE 0531について構成や状態を確認します。errpt -a 容量確認 Subsystem 0532ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはJFS2でdf -gを用い・log=INLINE と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 状態を読み取るための働きはSRCとログでerrpt -aを用い・Subsystem とsyslog設定変換を確認する。</li><li>C. 状態を読み取るための働きは性能管理でiostat -Dl 2 2を用い・pi とAME統計を確認する。</li><li>D. 状態を読み取るための働きはネットワークでnetstat -vを用い・EtherChannel と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「JFS2でdf -gを用い、log=INLINE と内部スナップショットを確認する」に対応する項目は運用引継ぎ log=INLINE（運用・df）です。運用引に関するJFS2の仕様は「JFS2でdf -gを用い、log=INLINE」で、確認対象はdf・運用引です。容量・errpのB:は「SRCとログでerrpt -aを用い、Subsystem」を述べ、対象は容量確認 Subsystem（容量・errp）です。変更後・iostのC:は「性能管理でiostat -Dl 2 2を用い、pi」を述べ、対象は変更後確認 pi（変更・iost）です。性能・netsのD:は「ネットワークでnetstat -vを用い、EtherChannel」を述べ、対象は性能確認 EtherChannel（性能・nets）です。「df -g」は「JFS2でdf -gを用い、log=INLINE」を指し、運用引継ぎ log=INLINEではdf・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>df -g 運用引継ぎ log=INLINE 0531</strong></p><p>検証目的: JFS2のdf -g 運用引継ぎ log=INLINE 0531について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2運用引継ぎ051-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g
→ Enter を押す
［画面・出力］
/data/aixdd0531:
        dev             = /dev/fslv51
        vfs             = jfs2
        log             = INLINE
確認コード AIX0531A
画面・出力には AIX0531A が表示され、df -g 運用引継ぎ log=INLINE 0531 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv51       16.00      9.42   42%     128     1% /data/aixdd0531
確認コード AIX0531B
画面・出力には AIX0531B が表示され、df -g 運用引継ぎ log=INLINE 0531 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0531      --         /data/aixdd0531          jfs2  33554432 rw,log=INLINE
確認コード AIX0531C
画面・出力には AIX0531C が表示され、df -g 運用引継ぎ log=INLINE 0531 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0531A が画面・出力に表示されること
② ステップ2 の AIX0531B が画面・出力に表示されること
③ ステップ3 の AIX0531C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0039"><h3>fsck 変更前確認 isnapshot 0252</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第二百五十二観点 JFS2 で fsck は 変更前確認 を点検します（運用第二百五十二）（第二百五十二観点）。第二百五十二観点 確認時には isnapshot と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第二百五十二）（第二百五十二観点）。第二百五十二観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第二百五十二観点）。第二百五十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0252へ書きます（第二百五十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> fsck 変更前確認 isnapshot 0252の技術的な意味を資料で確認するとき、errpt 変更後確認 IDENTIFIER 0253との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はSRCとログでerrptを用い・IDENTIFIER とinetdデバッグ出力を確認する。</li><li>B. 構成を確認する際の意味は性能管理でsvmon -Gを用い・csz とvmstat表示を確認する。</li><li>C. 構成を確認する際の意味はJFS2でfsckを用い・isnapshot とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「JFS2でfsckを用い、isnapshot とログデバイス設定を確認する」に対応する項目は変更前確認 isnapshot（変更・fsck）です。変更前に関するJFS2の仕様は「JFS2でfsckを用い、isnapshot」で、確認対象はfs・変更前です。変更後・errpのA:は「SRCとログでerrptを用い、IDENTIFIER」を述べ、対象は変更後確認 IDENTIFIER（変更・errp）です。起動・svmoのB:は「性能管理でsvmon -Gを用い、csz」を述べ、対象は起動確認 csz（起動・svmo）です。状態・表形・errpのD:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は状態判定 表形式（状態・errp）です。「fsck」は「JFS2でfsckを用い、isnapshot」を指し、変更前確認 isnapshotではfs・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fsck 変更前確認 isnapshot 0252</strong></p><p>検証目的: JFS2のfsck 変更前確認 isnapshot 0252について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更前確認012-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; fsck
→ Enter を押す
［画面・出力］
/data/aixdd0252:
        dev             = /dev/fslv12
        vfs             = jfs2
        log             = INLINE
確認コード AIX0252A
画面・出力には AIX0252A が表示され、fsck 変更前確認 isnapshot 0252 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv12       16.00      9.42   42%     128     1% /data/aixdd0252
確認コード AIX0252B
画面・出力には AIX0252B が表示され、fsck 変更前確認 isnapshot 0252 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0252      --         /data/aixdd0252          jfs2  33554432 rw,log=INLINE
確認コード AIX0252C
画面・出力には AIX0252C が表示され、fsck 変更前確認 isnapshot 0252 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0252A が画面・出力に表示されること
② ステップ2 の AIX0252B が画面・出力に表示されること
③ ステップ3 の AIX0252C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0040"><h3>fsck 変更前確認 isnapshot 0312</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第三百十二観点 JFS2 で fsck は 変更前確認 を点検します（運用第三百十二）（第三百十二観点）。第三百十二観点 確認時には isnapshot と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第三百十二）（第三百十二観点）。第三百十二観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第三百十二観点）。第三百十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0312へ書きます（第三百十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> fsck 変更前確認 isnapshot 0312を同一分類のerrpt 変更後確認 IDENTIFIER 0313と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はSRCとログでerrptを用い・IDENTIFIER とinetdデバッグ出力を確認する。</li><li>B. 構成を確認する際の意味は性能管理でiostat -Dl 2 2を用い・Entitled Capacityである。</li><li>C. 構成を確認する際の意味はJFS2でfsckを用い・isnapshot とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はネットワークでnetstat -vを用い・Destination とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でfsckを用い、isnapshot とログデバイス設定を確認する」に対応する項目は変更前確認 isnapshot（変更・fsck）です。変更前に関するJFS2の仕様は「JFS2でfsckを用い、isnapshot」で、確認対象はfs・変更前です。変更後・errpのA:は「SRCとログでerrptを用い、IDENTIFIER」を述べ、対象は変更後確認 IDENTIFIER（変更・errp）です。属性・iostのB:は「性能管理でiostat -Dl 2 2を用い、Entitled」を述べ、対象はEntitled Capacity（属性・iost）です。バック・netsのD:は「ネットワークでnetstat -vを用い、Destination」を述べ、対象はバックアウト確認 Destinati（バッ・nets）です。「fsck」は「JFS2でfsckを用い、isnapshot」を指し、変更前確認 isnapshotではfs・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fsck 変更前確認 isnapshot 0312</strong></p><p>検証目的: JFS2のfsck 変更前確認 isnapshot 0312について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更前確認072-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; fsck
→ Enter を押す
［画面・出力］
/data/aixdd0312:
        dev             = /dev/fslv72
        vfs             = jfs2
        log             = INLINE
確認コード AIX0312A
画面・出力には AIX0312A が表示され、fsck 変更前確認 isnapshot 0312 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv72       16.00      9.42   42%     128     1% /data/aixdd0312
確認コード AIX0312B
画面・出力には AIX0312B が表示され、fsck 変更前確認 isnapshot 0312 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0312      --         /data/aixdd0312          jfs2  33554432 rw,log=INLINE
確認コード AIX0312C
画面・出力には AIX0312C が表示され、fsck 変更前確認 isnapshot 0312 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0312A が画面・出力に表示されること
② ステップ2 の AIX0312B が画面・出力に表示されること
③ ステップ3 の AIX0312C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0041"><h3>fsck 変更前確認 lff 0728</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第七百二十八観点 JFS2 で fsck は 変更前確認 を点検します（運用第七百二十八）（第七百二十八観点）。第七百二十八観点 確認時には lff と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第七百二十八）（第七百二十八観点）。第七百二十八観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第七百二十八観点）。第七百二十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0728へ書きます（第七百二十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> fsck 変更前確認 lff 0728を同一分類のerrpt 変更後確認 syslog.conf 0729と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はSRCとログでerrptを用い・syslog.conf とinetdデバッグ出力を確認する。</li><li>B. コマンドまたは機能の用途はデバイス管理でodmget CuDvを用い・PVID とデバイス一覧を確認する。</li><li>C. コマンドまたは機能の用途はJFS2でfsckを用い・lff とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はネットワークでnetstat -rnを用い・Gateway とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「JFS2でfsckを用い、lff とログデバイス設定を確認する」に対応する項目は変更前確認 lff（変更・fsck）です。変更前に関するJFS2の仕様は「JFS2でfsckを用い、lff とログデバイス設定を確認する」で、確認対象はfs・変更前です。変更後・errpのA:は「SRCとログでerrptを用い、syslog.conf」を述べ、対象は変更後確認 syslog.conf（変更・errp）です。監査・odmgのB:は「デバイス管理でodmget CuDvを用い、PVID」を述べ、対象は監査記録 PVID（監査・odmg）です。障害切・netsのD:は「ネットワークでnetstat -rnを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・nets）です。「fsck」は「JFS2でfsckを用い、lff とログデバイス設定を確認する」を指し、変更前確認 lffではfs・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fsck 変更前確認 lff 0728</strong></p><p>検証目的: JFS2のfsck 変更前確認 lff 0728について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更前確認008-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; fsck
→ Enter を押す
［画面・出力］
/data/aixdd0728:
        dev             = /dev/fslv08
        vfs             = jfs2
        log             = INLINE
確認コード AIX0728A
画面・出力には AIX0728A が表示され、fsck 変更前確認 lff 0728 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv08       16.00      9.42   42%     128     1% /data/aixdd0728
確認コード AIX0728B
画面・出力には AIX0728B が表示され、fsck 変更前確認 lff 0728 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0728      --         /data/aixdd0728          jfs2  33554432 rw,log=INLINE
確認コード AIX0728C
画面・出力には AIX0728C が表示され、fsck 変更前確認 lff 0728 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0728A が画面・出力に表示されること
② ステップ2 の AIX0728B が画面・出力に表示されること
③ ステップ3 の AIX0728C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0042"><h3>fsck 変更前確認 lff 0788</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第七百八十八観点 JFS2 で fsck は 変更前確認 を点検します（運用第七百八十八）（第七百八十八観点）。第七百八十八観点 確認時には lff と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第七百八十八）（第七百八十八観点）。第七百八十八観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第七百八十八観点）。第七百八十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0788へ書きます（第七百八十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> fsck 変更前確認 lff 0788の技術的な意味を資料で確認するとき、lscfg 状態判定 除外条件との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途は構成済みデバイスと VPD を表示するコマンドである。</li><li>B. コマンドまたは機能の用途はJFS2でlsfs -qを用い・agblksize と内部スナップショットを確認する。</li><li>C. コマンドまたは機能の用途はJFS2でfsckを用い・lff とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途は導入と起動でbosboot -a -dを用い・altinst_rootvg とfileset一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更前・fsckでCの記述「JFS2でfsckを用い、lff とログデバイス設定を確認する」に対応する項目は変更前確認 lff（変更・fsck）です。変更前に関するJFS2の仕様は「JFS2でfsckを用い、lff とログデバイス設定を確認する」で、確認対象はfs・変更前です。状態・除外・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は状態判定 除外条件（状態・lscf）です。状態・lsfsのB:は「JFS2でlsfs -qを用い、agblksize」を述べ、対象は状態確認 agblksize（状態・lsfs）です。変更後・bosbのD:は「導入と起動でbosboot -a -dを用い」を述べ、対象は変更後確認 altinst_root（変更・bosb）です。「fsck」は「JFS2でfsckを用い、lff とログデバイス設定を確認する」を指し、変更前確認 lffではfs・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fsck 変更前確認 lff 0788</strong></p><p>検証目的: JFS2のfsck 変更前確認 lff 0788について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更前確認068-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; fsck
→ Enter を押す
［画面・出力］
/data/aixdd0788:
        dev             = /dev/fslv68
        vfs             = jfs2
        log             = INLINE
確認コード AIX0788A
画面・出力には AIX0788A が表示され、fsck 変更前確認 lff 0788 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv68       16.00      9.42   42%     128     1% /data/aixdd0788
確認コード AIX0788B
画面・出力には AIX0788B が表示され、fsck 変更前確認 lff 0788 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0788      --         /data/aixdd0788          jfs2  33554432 rw,log=INLINE
確認コード AIX0788C
画面・出力には AIX0788C が表示され、fsck 変更前確認 lff 0788 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0788A が画面・出力に表示されること
② ステップ2 の AIX0788B が画面・出力に表示されること
③ ステップ3 の AIX0788C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0043"><h3>fsck 容量確認 agblksize 0758</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第七百五十八観点 JFS2 で fsck は 容量確認 を点検します（運用第七百五十八）（第七百五十八観点）。第七百五十八観点 確認時には agblksize と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第七百五十八）（第七百五十八観点）。第七百五十八観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第七百五十八観点）。第七百五十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0758へ書きます（第七百五十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> fsck 容量確認 agblksize 0758に関する障害切り分けの前提を確認しています。errpt 性能確認 Status 0759の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はSRCとログでerrptを用い・Status とエラーログ一覧を確認する。</li><li>B. 障害切り分けに用いる役割はデバイス管理でlscfg -vl ent0を用い・location codeである。</li><li>C. 障害切り分けに用いる役割はJFS2でfsckを用い・agblksize とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割はネットワークでnetstat -rnを用い・Media Speed Runningである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でfsckを用い、agblksize とファイルシステム属性を確認する」に対応する項目は容量確認 agblksize（容量・fsck）です。容量に関するJFS2の仕様は「JFS2でfsckを用い、agblksize」で、確認対象はfs・容量です。性能・errpのA:は「SRCとログでerrptを用い、Status」を述べ、対象は性能確認 Status（性能・errp）です。構成・lscfのB:は「デバイス管理でlscfg -vl ent0を用い、location」を述べ、対象はlocation code（構成・lscf）です。起動・netsのD:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（起動・nets）です。「fsck」は「JFS2でfsckを用い、agblksize」を指し、容量確認 agblksizeではfs・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fsck 容量確認 agblksize 0758</strong></p><p>検証目的: JFS2のfsck 容量確認 agblksize 0758について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2容量確認038-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; fsck
→ Enter を押す
［画面・出力］
/data/aixdd0758:
        dev             = /dev/fslv38
        vfs             = jfs2
        log             = INLINE
確認コード AIX0758A
画面・出力には AIX0758A が表示され、fsck 容量確認 agblksize 0758 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv38       16.00      9.42   42%     128     1% /data/aixdd0758
確認コード AIX0758B
画面・出力には AIX0758B が表示され、fsck 容量確認 agblksize 0758 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0758      --         /data/aixdd0758          jfs2  33554432 rw,log=INLINE
確認コード AIX0758C
画面・出力には AIX0758C が表示され、fsck 容量確認 agblksize 0758 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0758A が画面・出力に表示されること
② ステップ2 の AIX0758B が画面・出力に表示されること
③ ステップ3 の AIX0758C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0044"><h3>fsck 容量確認 agblksize 0818</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第八百十八観点 JFS2 で fsck は 容量確認 を点検します（運用第八百十八）（第八百十八観点）。第八百十八観点 確認時には agblksize と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第八百十八）（第八百十八観点）。第八百十八観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第八百十八観点）。第八百十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0818へ書きます（第八百十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> fsck 容量確認 agblksize 0818の役割を調べています。errpt 変更前確認 再読込の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>B. 障害切り分けに用いる役割は導入と起動でemgr -lを用い・altinst_rootvg とfileset一覧を確認する。</li><li>C. 障害切り分けに用いる役割はJFS2でfsckを用い・agblksize とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割はセキュリティでlsattr -E -l sys0 -aを用い・roles とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 容量・fsckでCの記述「JFS2でfsckを用い、agblksize」に対応する項目は容量確認 agblksize（容量・fsck）です。容量に関するJFS2の仕様は「JFS2でfsckを用い、agblksize」で、確認対象はfs・容量です。変更前・errpのA:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は変更前確認 再読込（変更・errp）です。バック・emgrのB:は「導入と起動でemgr -lを用い、altinst_rootvg」を述べ、対象はバックアウト確認 altinst_r（バッ・emgr）です。状態・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 roles（状態・lsat）です。「fsck」は「JFS2でfsckを用い、agblksize」を指し、容量確認 agblksizeではfs・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fsck 容量確認 agblksize 0818</strong></p><p>検証目的: JFS2のfsck 容量確認 agblksize 0818について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2容量確認098-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; fsck
→ Enter を押す
［画面・出力］
/data/aixdd0818:
        dev             = /dev/fslv98
        vfs             = jfs2
        log             = INLINE
確認コード AIX0818A
画面・出力には AIX0818A が表示され、fsck 容量確認 agblksize 0818 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv98       16.00      9.42   42%     128     1% /data/aixdd0818
確認コード AIX0818B
画面・出力には AIX0818B が表示され、fsck 容量確認 agblksize 0818 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0818      --         /data/aixdd0818          jfs2  33554432 rw,log=INLINE
確認コード AIX0818C
画面・出力には AIX0818C が表示され、fsck 容量確認 agblksize 0818 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0818A が画面・出力に表示されること
② ステップ2 の AIX0818B が画面・出力に表示されること
③ ステップ3 の AIX0818C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0045"><h3>fsck 容量確認 ファイルシステム使用率 0282</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第二百八十二観点 JFS2 で fsck は 容量確認 を点検します（運用第二百八十二）（第二百八十二観点）。第二百八十二観点 確認時には ファイルシステム使用率 と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第二百八十二）（第二百八十二観点）。第二百八十二観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第二百八十二観点）。第二百八十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0282へ書きます（第二百八十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> fsck 容量確認 ファイルシステム使用率 0282の役割を調べています。errpt 性能確認 Subsystem 0283の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはSRCとログでerrptを用い・Subsystem とエラーログ一覧を確認する。errpt 性能確認 Subsystem 0283固有の属性も確認対象に含める。</li><li>B. 機能の説明としては性能管理でsvmon -Gを用い・fre とtopasディスク表示を確認する。</li><li>C. 機能の説明としてはJFS2でfsckを用い・ファイルシステム使用率 とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としてはAIX エラーログから要約または詳細レポートを生成するコマンドである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でfsckを用い、ファイルシステム使用率 とファイルシステム属性を確認する」に対応する項目は容量確認 ファイルシステム使用率（容量・fsck）です。容量・ファイに関するJFS2の仕様は「JFS2でfsckを用い、ファイルシステム使用率」で、確認対象はfs・容量・ファです。性能・errpのA:は「SRCとログでerrptを用い、Subsystem」を述べ、対象は性能確認 Subsystem（性能・errp）です。障害切・svmoのB:は「性能管理でsvmon -Gを用い、fre」を述べ、対象は障害切り分け fre（障害・svmo）です。属性・ログ・errpのD:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は属性照合 ログ採取（属性・errp）です。「fsck」は「JFS2でfsckを用い、ファイルシステム使用率」を指し、容量確認 ファイルシステム使用率ではfs・容量・ファに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fsck 容量確認 ファイルシステム使用率 0282</strong></p><p>検証目的: JFS2のfsck 容量確認 ファイルシステム使用率 0282について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2容量確認042-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; fsck
→ Enter を押す
［画面・出力］
/data/aixdd0282:
        dev             = /dev/fslv42
        vfs             = jfs2
        log             = INLINE
確認コード AIX0282A
画面・出力には AIX0282A が表示され、fsck 容量確認 ファイルシステム使用率 0282 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv42       16.00      9.42   42%     128     1% /data/aixdd0282
確認コード AIX0282B
画面・出力には AIX0282B が表示され、fsck 容量確認 ファイルシステム使用率 0282 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0282      --         /data/aixdd0282          jfs2  33554432 rw,log=INLINE
確認コード AIX0282C
画面・出力には AIX0282C が表示され、fsck 容量確認 ファイルシステム使用率 0282 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0282A が画面・出力に表示されること
② ステップ2 の AIX0282B が画面・出力に表示されること
③ ステップ3 の AIX0282C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0046"><h3>fsck 容量確認 ファイルシステム使用率 0342</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第三百四十二観点 JFS2 で fsck は 容量確認 を点検します（運用第三百四十二）（第三百四十二観点）。第三百四十二観点 確認時には ファイルシステム使用率 と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第三百四十二）（第三百四十二観点）。第三百四十二観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第三百四十二観点）。第三百四十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0342へ書きます（第三百四十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> fsck 容量確認 ファイルシステム使用率 0342に関する障害切り分けの前提を確認しています。errpt 性能確認 Subsystem 0343の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはJFS2でfsckを用い・ファイルシステム使用率 とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 機能の説明としてはSRCとログでerrptを用い・Subsystem とエラーログ一覧を確認する。</li><li>C. 機能の説明としては性能管理でiostat -Dl 2 2を用い・dxm とtopasディスク表示を確認する。</li><li>D. 機能の説明としてはネットワークでnetstat -vを用い・Link Status とEthernet統計を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「JFS2でfsckを用い、ファイルシステム使用率 とファイルシステム属性を確認する」に対応する項目は容量確認 ファイルシステム使用率（容量・fsck）です。容量・ファイに関するJFS2の仕様は「JFS2でfsckを用い、ファイルシステム使用率」で、確認対象はfs・容量・ファです。性能・errpのB:は「SRCとログでerrptを用い、Subsystem」を述べ、対象は性能確認 Subsystem（性能・errp）です。バック・iostのC:は「性能管理でiostat -Dl 2 2を用い、dxm」を述べ、対象はバックアウト確認 dxm（バッ・iost）です。属性・netsのD:は「ネットワークでnetstat -vを用い、Link Status」を述べ、対象はLink Status（属性・nets）です。「fsck」は「JFS2でfsckを用い、ファイルシステム使用率」を指し、容量確認 ファイルシステム使用率ではfs・容量・ファに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fsck 容量確認 ファイルシステム使用率 0342</strong></p><p>検証目的: JFS2のfsck 容量確認 ファイルシステム使用率 0342について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2容量確認102-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; fsck
→ Enter を押す
［画面・出力］
/data/aixdd0342:
        dev             = /dev/fslv102
        vfs             = jfs2
        log             = INLINE
確認コード AIX0342A
画面・出力には AIX0342A が表示され、fsck 容量確認 ファイルシステム使用率 0342 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv102       16.00      9.42   42%     128     1% /data/aixdd0342
確認コード AIX0342B
画面・出力には AIX0342B が表示され、fsck 容量確認 ファイルシステム使用率 0342 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0342      --         /data/aixdd0342          jfs2  33554432 rw,log=INLINE
確認コード AIX0342C
画面・出力には AIX0342C が表示され、fsck 容量確認 ファイルシステム使用率 0342 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0342A が画面・出力に表示されること
② ステップ2 の AIX0342B が画面・出力に表示されること
③ ステップ3 の AIX0342C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0047"><h3>fsck 状態確認 isnapshot 0441</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第四百四十一観点 JFS2 で fsck は 状態確認 を点検します（運用第四百四十一）（第四百四十一観点）。第四百四十一観点 確認時には isnapshot と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第四百四十一）（第四百四十一観点）。第四百四十一観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第四百四十一観点）。第四百四十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0441へ書きます（第四百四十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「fsck 状態確認 isnapshot 0441」を「errpt 構成照合 Status 0442」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はSRCとログでerrptを用い・Status とSRCサブシステム表示を確認する。</li><li>B. 運用時に利用する技術的役割はJFS2でfsckを用い・isnapshot とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割は性能管理でiostat -Dl 2 2を用い・pi とsvmon全体表示を確認する。</li><li>D. 運用時に利用する技術的役割はネットワークでnetstat -vを用い・MTU とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でfsckを用い、isnapshot とマウントオプションを確認する」に対応する項目は状態確認 isnapshot（状態・fsck）です。状態に関するJFS2の仕様は「JFS2でfsckを用い、isnapshot」で、確認対象はfs・状態です。構成・errpのA:は「SRCとログでerrptを用い、Status」を述べ、対象は構成照合 Status（構成・errp）です。性能・iostのC:は「性能管理でiostat -Dl 2 2を用い、pi」を述べ、対象は性能確認 pi（性能・iost）です。変更後・netsのD:は「ネットワークでnetstat -vを用い、MTU」を述べ、対象は変更後確認 MTU（変更・nets）です。「fsck」は「JFS2でfsckを用い、isnapshot」を指し、状態確認 isnapshotではfs・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fsck 状態確認 isnapshot 0441</strong></p><p>検証目的: JFS2のfsck 状態確認 isnapshot 0441について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2状態確認081-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; fsck
→ Enter を押す
［画面・出力］
/data/aixdd0441:
        dev             = /dev/fslv81
        vfs             = jfs2
        log             = INLINE
確認コード AIX0441A
画面・出力には AIX0441A が表示され、fsck 状態確認 isnapshot 0441 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv81       16.00      9.42   42%     128     1% /data/aixdd0441
確認コード AIX0441B
画面・出力には AIX0441B が表示され、fsck 状態確認 isnapshot 0441 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0441      --         /data/aixdd0441          jfs2  33554432 rw,log=INLINE
確認コード AIX0441C
画面・出力には AIX0441C が表示され、fsck 状態確認 isnapshot 0441 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0441A が画面・出力に表示されること
② ステップ2 の AIX0441B が画面・出力に表示されること
③ ステップ3 の AIX0441C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0048"><h3>fsck 監査記録 ファイルシステム使用率 0471</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第四百七十一観点 JFS2 で fsck は 監査記録 を点検します（運用第四百七十一）（第四百七十一観点）。第四百七十一観点 確認時には ファイルシステム使用率 と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第四百七十一）（第四百七十一観点）。第四百七十一観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第四百七十一観点）。第四百七十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0471へ書きます（第四百七十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> fsck 監査記録 ファイルシステム使用率 0471の設定や表示を読む前に役割を確認します。errpt 運用引継ぎ syslog.conf 0472ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはSRCとログでerrptを用い・syslog.conf とsyslog設定変換を確認する。</li><li>B. 状態を読み取るための働きは性能管理でiostat -Dl 2 2を用い・Entitled Capacity とAME統計を確認する。</li><li>C. 状態を読み取るための働きはネットワークでnetstat -vを用い・EtherChannel と経路表を確認する。</li><li>D. 状態を読み取るための働きはJFS2でfsckを用い・ファイルシステム使用率 と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「JFS2でfsckを用い、ファイルシステム使用率 と内部スナップショットを確認する」に対応する項目は監査記録 ファイルシステム使用率（監査・fsck）です。監査・ファイに関するJFS2の仕様は「JFS2でfsckを用い、ファイルシステム使用率」で、確認対象はfs・監査・ファです。運用引・errpのA:は「SRCとログでerrptを用い、syslog.conf」を述べ、対象は運用引継ぎ syslog.conf（運用・errp）です。変更後・iostのB:は「性能管理でiostat -Dl 2 2を用い、Entitled」を述べ、対象はEntitled Capacity（変更・iost）です。性能・netsのC:は「ネットワークでnetstat -vを用い、EtherChannel」を述べ、対象は性能確認 EtherChannel（性能・nets）です。「fsck」は「JFS2でfsckを用い、ファイルシステム使用率」を指し、監査記録 ファイルシステム使用率ではfs・監査・ファに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fsck 監査記録 ファイルシステム使用率 0471</strong></p><p>検証目的: JFS2のfsck 監査記録 ファイルシステム使用率 0471について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2監査記録111-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; fsck
→ Enter を押す
［画面・出力］
/data/aixdd0471:
        dev             = /dev/fslv111
        vfs             = jfs2
        log             = INLINE
確認コード AIX0471A
画面・出力には AIX0471A が表示され、fsck 監査記録 ファイルシステム使用率 0471 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv111       16.00      9.42   42%     128     1% /data/aixdd0471
確認コード AIX0471B
画面・出力には AIX0471B が表示され、fsck 監査記録 ファイルシステム使用率 0471 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0471      --         /data/aixdd0471          jfs2  33554432 rw,log=INLINE
確認コード AIX0471C
画面・出力には AIX0471C が表示され、fsck 監査記録 ファイルシステム使用率 0471 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0471A が画面・出力に表示されること
② ステップ2 の AIX0471B が画面・出力に表示されること
③ ステップ3 の AIX0471C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0049"><h3>fsck 障害切り分け mountguard 0123</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第百二十三観点 JFS2 で fsck は 障害切り分け を点検します（運用第百二十三）（第百二十三観点）。第百二十三観点 確認時には mountguard と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第百二十三）（第百二十三観点）。第百二十三観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第百二十三観点）。第百二十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0123へ書きます（第百二十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> fsck 障害切り分け mountguard 0123について構成や状態を確認します。errpt バックアウト確認 IDENTIFIER 0124ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはSRCとログでerrptを用い・IDENTIFIER とsyslog設定変換を確認する。</li><li>B. 状態を読み取るための働きはJFS2でfsckを用い・mountguard と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きは性能管理でsvmon -Gを用い・pi とAME統計を確認する。</li><li>D. 状態を読み取るための働きはSRCとログでrefresh -s syslogdを用い・Status とsyslog設定変換を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「JFS2でfsckを用い、mountguard と内部スナップショットを確認する」に対応する項目は障害切り分け mountguard（障害・fsck）です。障害切に関するJFS2の仕様は「JFS2でfsckを用い、mountguard」で、確認対象はfs・障害切です。バック・errpのA:は「SRCとログでerrptを用い、IDENTIFIER」を述べ、対象はバックアウト確認 IDENTIFIE（バッ・errp）です。状態・svmoのC:は「性能管理でsvmon -Gを用い、pi とAME統計を確認する」を述べ、対象は状態確認 pi（状態・svmo）です。起動・refrのD:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は起動確認 Status（起動・refr）です。「fsck」は「JFS2でfsckを用い、mountguard」を指し、障害切り分け mountguardではfs・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>fsck 障害切り分け mountguard 0123</strong></p><p>検証目的: JFS2のfsck 障害切り分け mountguard 0123について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2障害切り分け003-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; fsck
→ Enter を押す
［画面・出力］
/data/aixdd0123:
        dev             = /dev/fslv03
        vfs             = jfs2
        log             = INLINE
確認コード AIX0123A
画面・出力には AIX0123A が表示され、fsck 障害切り分け mountguard 0123 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv03       16.00      9.42   42%     128     1% /data/aixdd0123
確認コード AIX0123B
画面・出力には AIX0123B が表示され、fsck 障害切り分け mountguard 0123 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0123      --         /data/aixdd0123          jfs2  33554432 rw,log=INLINE
確認コード AIX0123C
画面・出力には AIX0123C が表示され、fsck 障害切り分け mountguard 0123 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0123A が画面・出力に表示されること
② ステップ2 の AIX0123B が画面・出力に表示されること
③ ステップ3 の AIX0123C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0050"><h3>logform 変更前確認 mountguard 0395</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第三百九十五観点 JFS2 で logform は 変更前確認 を点検します（運用第三百九十五）（第三百九十五観点）。第三百九十五観点 確認時には mountguard と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第三百九十五）（第三百九十五観点）。第三百九十五観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第三百九十五観点）。第三百九十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0395へ書きます（第三百九十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> logform 変更前確認 mountguard 0395について構成や状態を確認します。tail -f /tmp/myfile 変更後確認 IDENTIFIER 0396ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。</li><li>B. 一次資料が示す主目的は性能管理でnmonを用い・dxm とAME統計を確認する。</li><li>C. 一次資料が示す主目的はJFS2でlogformを用い・mountguard と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はネットワークでroute -n getを用い・MTU と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でlogformを用い、mountguard」に対応する項目は変更前確認 mountguard（変更・logf）です。変更前に関するJFS2の仕様は「JFS2でlogformを用い、mountguard」で、確認対象はlo・変更前です。変更後・tailのA:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は変更後確認 IDENTIFIER（変更・tail）です。起動・nmonのB:は「性能管理でnmonを用い、dxm とAME統計を確認する」を述べ、対象は起動確認 dxm（起動・nmon）です。障害切・routのD:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は障害切り分け MTU（障害・rout）です。「logform」は「JFS2でlogformを用い、mountguard」を指し、変更前確認 mountguardではlo・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>logform 変更前確認 mountguard 0395</strong></p><p>検証目的: JFS2のlogform 変更前確認 mountguard 0395について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更前確認035-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; logform
→ Enter を押す
［画面・出力］
/data/aixdd0395:
        dev             = /dev/fslv35
        vfs             = jfs2
        log             = INLINE
確認コード AIX0395A
画面・出力には AIX0395A が表示され、logform 変更前確認 mountguard 0395 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv35       16.00      9.42   42%     128     1% /data/aixdd0395
確認コード AIX0395B
画面・出力には AIX0395B が表示され、logform 変更前確認 mountguard 0395 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0395      --         /data/aixdd0395          jfs2  33554432 rw,log=INLINE
確認コード AIX0395C
画面・出力には AIX0395C が表示され、logform 変更前確認 mountguard 0395 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0395A が画面・出力に表示されること
② ステップ2 の AIX0395B が画面・出力に表示されること
③ ステップ3 の AIX0395C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0051"><h3>logform 容量確認 log=INLINE 0365</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第三百六十五観点 JFS2 で logform は 容量確認 を点検します（運用第三百六十五）（第三百六十五観点）。第三百六十五観点 確認時には log=INLINE と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第三百六十五）（第三百六十五観点）。第三百六十五観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第三百六十五観点）。第三百六十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0365へ書きます（第三百六十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> logform 容量確認 log=INLINE 0365を保守記録に説明する必要があります。tail -f /tmp/myfile 性能確認 Subsystem 0366と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はSRCとログでtail -f /tmp/myfileを用い・Subsystemである。</li><li>B. 仕様上の役割は性能管理でnmonを用い・Entitled Capacity とsvmon全体表示を確認する。</li><li>C. 仕様上の役割はJFS2でlogformを用い・log=INLINE とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 仕様上の役割はネットワークでroute -n getを用い・EtherChannel とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「JFS2でlogformを用い、log=INLINE とマウントオプションを確認する」に対応する項目は容量確認 log=INLINE（容量・logf）です。容量に関するJFS2の仕様は「JFS2でlogformを用い、log=INLINE」で、確認対象はlo・容量です。性能・tailのA:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は性能確認 Subsystem（性能・tail）です。障害切・nmonのB:は「性能管理でnmonを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（障害・nmon）です。起動・routのD:は「ネットワークでroute -n getを用い」を述べ、対象は起動確認 EtherChannel（起動・rout）です。「logform」は「JFS2でlogformを用い、log=INLINE」を指し、容量確認 log=INLINEではlo・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>logform 容量確認 log=INLINE 0365</strong></p><p>検証目的: JFS2のlogform 容量確認 log=INLINE 0365について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2容量確認005-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; logform
→ Enter を押す
［画面・出力］
/data/aixdd0365:
        dev             = /dev/fslv05
        vfs             = jfs2
        log             = INLINE
確認コード AIX0365A
画面・出力には AIX0365A が表示され、logform 容量確認 log=INLINE 0365 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv05       16.00      9.42   42%     128     1% /data/aixdd0365
確認コード AIX0365B
画面・出力には AIX0365B が表示され、logform 容量確認 log=INLINE 0365 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0365      --         /data/aixdd0365          jfs2  33554432 rw,log=INLINE
確認コード AIX0365C
画面・出力には AIX0365C が表示され、logform 容量確認 log=INLINE 0365 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0365A が画面・出力に表示されること
② ステップ2 の AIX0365B が画面・出力に表示されること
③ ステップ3 の AIX0365C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0052"><h3>logform 状態確認 isnapshot 0524</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第五百二十四観点 JFS2 で logform は 状態確認 を点検します（運用第五百二十四）（第五百二十四観点）。第五百二十四観点 確認時には isnapshot と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第五百二十四）（第五百二十四観点）。第五百二十四観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第五百二十四観点）。第五百二十四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0524へ書きます（第五百二十四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> logform 状態確認 isnapshot 0524の技術的な意味を資料で確認するとき、tail -f /tmp/myfile 構成照合 IDENTIFIER 0525との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。</li><li>B. コマンドまたは機能の用途は性能管理でnmonを用い・PhysB とvmstat表示を確認する。</li><li>C. コマンドまたは機能の用途はJFS2でlogformを用い・isnapshot とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はネットワークでroute -n getを用い・MTU とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でlogformを用い、isnapshot とログデバイス設定を確認する」に対応する項目は状態確認 isnapshot（状態・logf）です。状態に関するJFS2の仕様は「JFS2でlogformを用い、isnapshot」で、確認対象はlo・状態です。構成・tailのA:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は構成照合 IDENTIFIER（構成・tail）です。容量・nmonのB:は「性能管理でnmonを用い、PhysB とvmstat表示を確認する」を述べ、対象は容量確認 PhysB（容量・nmon）です。変更前・routのD:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は変更前確認 MTU（変更・rout）です。「logform」は「JFS2でlogformを用い、isnapshot」を指し、状態確認 isnapshotではlo・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>logform 状態確認 isnapshot 0524</strong></p><p>検証目的: JFS2のlogform 状態確認 isnapshot 0524について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2状態確認044-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; logform
→ Enter を押す
［画面・出力］
/data/aixdd0524:
        dev             = /dev/fslv44
        vfs             = jfs2
        log             = INLINE
確認コード AIX0524A
画面・出力には AIX0524A が表示され、logform 状態確認 isnapshot 0524 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv44       16.00      9.42   42%     128     1% /data/aixdd0524
確認コード AIX0524B
画面・出力には AIX0524B が表示され、logform 状態確認 isnapshot 0524 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0524      --         /data/aixdd0524          jfs2  33554432 rw,log=INLINE
確認コード AIX0524C
画面・出力には AIX0524C が表示され、logform 状態確認 isnapshot 0524 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0524A が画面・出力に表示されること
② ステップ2 の AIX0524B が画面・出力に表示されること
③ ステップ3 の AIX0524C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0053"><h3>logform 状態確認 isnapshot 0584</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第五百八十四観点 JFS2 で logform は 状態確認 を点検します（運用第五百八十四）（第五百八十四観点）。第五百八十四観点 確認時には isnapshot と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第五百八十四）（第五百八十四観点）。第五百八十四観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第五百八十四観点）。第五百八十四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0584へ書きます（第五百八十四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> logform 状態確認 isnapshot 0584を同一分類のtail -f /tmp/myfile 構成照合 IDENTIFIER 0585と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。</li><li>B. コマンドまたは機能の用途はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>C. コマンドまたは機能の用途はJFS2でlogformを用い・isnapshot とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はネットワークでcfgmgrを用い・Destination とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「JFS2でlogformを用い、isnapshot とログデバイス設定を確認する」に対応する項目は状態確認 isnapshot（状態・logf）です。状態に関するJFS2の仕様は「JFS2でlogformを用い、isnapshot」で、確認対象はlo・状態です。構成・tailのA:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は構成照合 IDENTIFIER（構成・tail）です。性能・警告・lparのB:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は性能確認 警告行（性能・lpar）です。変更後・cfgmのD:は「ネットワークでcfgmgrを用い、Destination」を述べ、対象は変更後確認 Destination（変更・cfgm）です。「logform」は「JFS2でlogformを用い、isnapshot」を指し、状態確認 isnapshotではlo・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>logform 状態確認 isnapshot 0584</strong></p><p>検証目的: JFS2のlogform 状態確認 isnapshot 0584について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2状態確認104-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; logform
→ Enter を押す
［画面・出力］
/data/aixdd0584:
        dev             = /dev/fslv104
        vfs             = jfs2
        log             = INLINE
確認コード AIX0584A
画面・出力には AIX0584A が表示され、logform 状態確認 isnapshot 0584 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv104       16.00      9.42   42%     128     1% /data/aixdd0584
確認コード AIX0584B
画面・出力には AIX0584B が表示され、logform 状態確認 isnapshot 0584 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0584      --         /data/aixdd0584          jfs2  33554432 rw,log=INLINE
確認コード AIX0584C
画面・出力には AIX0584C が表示され、logform 状態確認 isnapshot 0584 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0584A が画面・出力に表示されること
② ステップ2 の AIX0584B が画面・出力に表示されること
③ ステップ3 の AIX0584C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0054"><h3>logform 状態確認 log=INLINE 0048</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第四十八観点 JFS2 で logform は 状態確認 を点検します（運用第四十八）（第四十八観点）。第四十八観点 確認時には log=INLINE と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第四十八）（第四十八観点）。第四十八観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第四十八観点）。第四十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0048へ書きます（第四十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> logform 状態確認 log=INLINE 0048を同一分類のtail -f /tmp/myfile 構成照合 PID 0049と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はJFS2でlogformを用い・log=INLINE とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はSRCとログでtail -f /tmp/myfileを用い・PID とinetdデバッグ出力を確認する。</li><li>C. 構成を確認する際の意味は性能管理でnmonを用い・Entitled Capacity とvmstat表示を確認する。</li><li>D. 構成を確認する際の意味はSRCとログでerrpt -aを用い・Subsystem とinetdデバッグ出力を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「JFS2でlogformを用い、log=INLINE とログデバイス設定を確認する」に対応する項目は状態確認 log=INLINE（状態・logf）です。JFS2の仕様は「JFS2でlogformを用い、log=INLINE」で、確認対象はlo・状態です。構成・tailのB:は「SRCとログでtail -f /tmp/myfileを用い、PID」を述べ、対象は構成照合 PID（構成・tail）です。容量・nmonのC:は「性能管理でnmonを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（容量・nmon）です。監査・errpのD:は「SRCとログでerrpt -aを用い、Subsystem」を述べ、対象は監査記録 Subsystem（監査・errp）です。「logform」は「JFS2でlogformを用い、log=INLINE」を指し、状態確認 log=INLINEではlo・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>logform 状態確認 log=INLINE 0048</strong></p><p>検証目的: JFS2のlogform 状態確認 log=INLINE 0048について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2状態確認048-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; logform
→ Enter を押す
［画面・出力］
/data/aixdd0048:
        dev             = /dev/fslv48
        vfs             = jfs2
        log             = INLINE
確認コード AIX0048A
画面・出力には AIX0048A が表示され、logform 状態確認 log=INLINE 0048 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv48       16.00      9.42   42%     128     1% /data/aixdd0048
確認コード AIX0048B
画面・出力には AIX0048B が表示され、logform 状態確認 log=INLINE 0048 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0048      --         /data/aixdd0048          jfs2  33554432 rw,log=INLINE
確認コード AIX0048C
画面・出力には AIX0048C が表示され、logform 状態確認 log=INLINE 0048 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0048A が画面・出力に表示されること
② ステップ2 の AIX0048B が画面・出力に表示されること
③ ステップ3 の AIX0048C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0055"><h3>logform 状態確認 log=INLINE 0108</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第百八観点 JFS2 で logform は 状態確認 を点検します（運用第百八）（第百八観点）。第百八観点 確認時には log=INLINE と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第百八）（第百八観点）。第百八観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第百八観点）。第百八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0108へ書きます（第百八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> logform 状態確認 log=INLINE 0108の技術的な意味を資料で確認するとき、tail -f /tmp/myfile 構成照合 PID 0109との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はSRCとログでtail -f /tmp/myfileを用い・PID とinetdデバッグ出力を確認する。</li><li>B. 構成を確認する際の意味は性能管理でfilemonを用い・po とvmstat表示を確認する。</li><li>C. 構成を確認する際の意味はJFS2でlogformを用い・log=INLINE とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はSRCとログでerrclearを用い・PID とinetdデバッグ出力を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「JFS2でlogformを用い、log=INLINE とログデバイス設定を確認する」に対応する項目は状態確認 log=INLINE（状態・logf）です。状態に関するJFS2の仕様は「JFS2でlogformを用い、log=INLINE」で、確認対象はlo・状態です。構成・tailのA:は「SRCとログでtail -f /tmp/myfileを用い、PID」を述べ、対象は構成照合 PID（構成・tail）です。性能・fileのB:は「性能管理でfilemonを用い、po とvmstat表示を確認する」を述べ、対象は性能確認 po（性能・file）です。運用引・errcのD:は「SRCとログでerrclearを用い、PID」を述べ、対象は運用引継ぎ PID（運用・errc）です。「logform」は「JFS2でlogformを用い、log=INLINE」を指し、状態確認 log=INLINEではlo・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>logform 状態確認 log=INLINE 0108</strong></p><p>検証目的: JFS2のlogform 状態確認 log=INLINE 0108について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2状態確認108-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; logform
→ Enter を押す
［画面・出力］
/data/aixdd0108:
        dev             = /dev/fslv108
        vfs             = jfs2
        log             = INLINE
確認コード AIX0108A
画面・出力には AIX0108A が表示され、logform 状態確認 log=INLINE 0108 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv108       16.00      9.42   42%     128     1% /data/aixdd0108
確認コード AIX0108B
画面・出力には AIX0108B が表示され、logform 状態確認 log=INLINE 0108 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0108      --         /data/aixdd0108          jfs2  33554432 rw,log=INLINE
確認コード AIX0108C
画面・出力には AIX0108C が表示され、logform 状態確認 log=INLINE 0108 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0108A が画面・出力に表示されること
② ステップ2 の AIX0108B が画面・出力に表示されること
③ ステップ3 の AIX0108C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0056"><h3>logform 監査記録 mountguard 0078</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第七十八観点 JFS2 で logform は 監査記録 を点検します（運用第七十八）（第七十八観点）。第七十八観点 確認時には mountguard と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第七十八）（第七十八観点）。第七十八観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第七十八観点）。第七十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0078へ書きます（第七十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> logform 監査記録 mountguard 0078に関する障害切り分けの前提を確認しています。tail -f /tmp/myfile 運用引継ぎ TIMESTAMP 0079の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはSRCとログでtail -f /tmp/myfileを用い・TIMESTAMP とエラーログ一覧を確認する。</li><li>B. 機能の説明としてはJFS2でlogformを用い・mountguard とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 機能の説明としては性能管理でfilemonを用い・Busy% とtopasディスク表示を確認する。</li><li>D. 機能の説明としてはSRCとログでerrpt -aを用い・IDENTIFIER とエラーログ一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でlogformを用い、mountguard」に対応する項目は監査記録 mountguard（監査・logf）です。監査に関するJFS2の仕様は「JFS2でlogformを用い、mountguard」で、確認対象はlo・監査です。運用引・tailのA:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は運用引継ぎ TIMESTAMP（運用・tail）です。変更後・fileのC:は「性能管理でfilemonを用い、Busy%」を述べ、対象は変更後確認 Busy%（変更・file）です。状態・errpのD:は「SRCとログでerrpt -aを用い、IDENTIFIER」を述べ、対象は状態確認 IDENTIFIER（状態・errp）です。「logform」は「JFS2でlogformを用い、mountguard」を指し、監査記録 mountguardではlo・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>logform 監査記録 mountguard 0078</strong></p><p>検証目的: JFS2のlogform 監査記録 mountguard 0078について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2監査記録078-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; logform
→ Enter を押す
［画面・出力］
/data/aixdd0078:
        dev             = /dev/fslv78
        vfs             = jfs2
        log             = INLINE
確認コード AIX0078A
画面・出力には AIX0078A が表示され、logform 監査記録 mountguard 0078 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv78       16.00      9.42   42%     128     1% /data/aixdd0078
確認コード AIX0078B
画面・出力には AIX0078B が表示され、logform 監査記録 mountguard 0078 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0078      --         /data/aixdd0078          jfs2  33554432 rw,log=INLINE
確認コード AIX0078C
画面・出力には AIX0078C が表示され、logform 監査記録 mountguard 0078 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0078A が画面・出力に表示されること
② ステップ2 の AIX0078B が画面・出力に表示されること
③ ステップ3 の AIX0078C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0057"><h3>logform 監査記録 ファイルシステム使用率 0554</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第五百五十四観点 JFS2 で logform は 監査記録 を点検します（運用第五百五十四）（第五百五十四観点）。第五百五十四観点 確認時には ファイルシステム使用率 と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第五百五十四）（第五百五十四観点）。第五百五十四観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第五百五十四観点）。第五百五十四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0554へ書きます（第五百五十四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> logform 監査記録 ファイルシステム使用率 0554の役割を調べています。tail -f /tmp/myfile 運用引継ぎ Subsystem 0555の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はJFS2でlogformを用い・ファイルシステム使用率 とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 障害切り分けに用いる役割はSRCとログでtail -f /tmp/myfileを用い・Subsystem とエラーログ一覧を確認する。</li><li>C. 障害切り分けに用いる役割はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li><li>D. 障害切り分けに用いる役割はネットワークでcfgmgrを用い・Link Status とEthernet統計を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「JFS2でlogformを用い、ファイルシステム使用率」に対応する項目は監査記録 ファイルシステム使用率（監査・logf）です。監査・ファイに関するJFS2の仕様は「JFS2でlogformを用い、ファイルシステム使用率」で、確認対象はlo・監査・ファです。運用引・tailのB:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は運用引継ぎ Subsystem（運用・tail）です。障害切・lparのC:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は障害切り分け 受信先（障害・lpar）です。性能・cfgmのD:は「ネットワークでcfgmgrを用い、Link Status」を述べ、対象はLink Status（性能・cfgm）です。「logform」は「JFS2でlogformを用い、ファイルシステム使用率」を指し、監査記録 ファイルシステム使用率ではlo・監査・ファに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>logform 監査記録 ファイルシステム使用率 0554</strong></p><p>検証目的: JFS2のlogform 監査記録 ファイルシステム使用率 0554について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2監査記録074-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; logform
→ Enter を押す
［画面・出力］
/data/aixdd0554:
        dev             = /dev/fslv74
        vfs             = jfs2
        log             = INLINE
確認コード AIX0554A
画面・出力には AIX0554A が表示され、logform 監査記録 ファイルシステム使用率 0554 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv74       16.00      9.42   42%     128     1% /data/aixdd0554
確認コード AIX0554B
画面・出力には AIX0554B が表示され、logform 監査記録 ファイルシステム使用率 0554 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0554      --         /data/aixdd0554          jfs2  33554432 rw,log=INLINE
確認コード AIX0554C
画面・出力には AIX0554C が表示され、logform 監査記録 ファイルシステム使用率 0554 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0554A が画面・出力に表示されること
② ステップ2 の AIX0554B が画面・出力に表示されること
③ ステップ3 の AIX0554C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0058"><h3>logform 起動確認 isnapshot 0713</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第七百十三観点 JFS2 で logform は 起動確認 を点検します（運用第七百十三）（第七百十三観点）。第七百十三観点 確認時には isnapshot と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第七百十三）（第七百十三観点）。第七百十三観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第七百十三観点）。第七百十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0713へ書きます（第七百十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「logform 起動確認 isnapshot 0713」を「tail -f /tmp/myfile 属性確認 Status 0714」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はSRCとログでtail -f /tmp/myfileを用い・Status とSRCサブシステム表示を確認する。</li><li>B. 仕様上の役割はデバイス管理でlsmpio -l hdisk0を用い・attribute とODM属性を確認する。</li><li>C. 仕様上の役割はネットワークでcfgmgrを用い・MTU とアダプター一覧を確認する。</li><li>D. 仕様上の役割はJFS2でlogformを用い・isnapshot とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「JFS2でlogformを用い、isnapshot とマウントオプションを確認する」に対応する項目は起動確認 isnapshot（起動・logf）です。起動に関するJFS2の仕様は「JFS2でlogformを用い、isnapshot」で、確認対象はlo・起動です。属性・tailのA:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は属性確認 Status（属性・tail）です。変更後・lsmpのB:は「デバイス管理でlsmpio -l hdisk0を用い」を述べ、対象は変更後確認 attribute（変更・lsmp）です。構成・cfgmのC:は「ネットワークでcfgmgrを用い、MTU とアダプター一覧を確認する」を述べ、対象は構成照合 MTU（構成・cfgm）です。「logform」は「JFS2でlogformを用い、isnapshot」を指し、起動確認 isnapshotではlo・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>logform 起動確認 isnapshot 0713</strong></p><p>検証目的: JFS2のlogform 起動確認 isnapshot 0713について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2起動確認113-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; logform
→ Enter を押す
［画面・出力］
/data/aixdd0713:
        dev             = /dev/fslv113
        vfs             = jfs2
        log             = INLINE
確認コード AIX0713A
画面・出力には AIX0713A が表示され、logform 起動確認 isnapshot 0713 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv113       16.00      9.42   42%     128     1% /data/aixdd0713
確認コード AIX0713B
画面・出力には AIX0713B が表示され、logform 起動確認 isnapshot 0713 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0713      --         /data/aixdd0713          jfs2  33554432 rw,log=INLINE
確認コード AIX0713C
画面・出力には AIX0713C が表示され、logform 起動確認 isnapshot 0713 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0713A が画面・出力に表示されること
② ステップ2 の AIX0713B が画面・出力に表示されること
③ ステップ3 の AIX0713C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0059"><h3>logform 起動確認 log=INLINE 0237</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第二百三十七観点 JFS2 で logform は 起動確認 を点検します（運用第二百三十七）（第二百三十七観点）。第二百三十七観点 確認時には log=INLINE と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第二百三十七）（第二百三十七観点）。第二百三十七観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第二百三十七観点）。第二百三十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0237へ書きます（第二百三十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> logform 起動確認 log=INLINE 0237を保守記録に説明する必要があります。tail -f /tmp/myfile 属性確認 Subsystem 0238と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はSRCとログでtail -f /tmp/myfileを用い・Subsystemである。</li><li>B. 運用時に利用する技術的役割はJFS2でlogformを用い・log=INLINE とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割は性能管理でfilemonを用い・Busy% とsvmon全体表示を確認する。</li><li>D. 運用時に利用する技術的役割はLPAR の CPU 使用率・物理CPU消費・AME 関連値を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「JFS2でlogformを用い、log=INLINE とマウントオプションを確認する」に対応する項目は起動確認 log=INLINE（起動・logf）です。起動に関するJFS2の仕様は「JFS2でlogformを用い、log=INLINE」で、確認対象はlo・起動です。属性・tailのA:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は属性確認 Subsystem（属性・tail）です。運用引・fileのC:は「性能管理でfilemonを用い、Busy%」を述べ、対象は運用引継ぎ Busy%（運用・file）です。詳細・保存・lparのD:は「LPAR の CPU 使用率、物理CPU消費、AME」を述べ、対象は詳細確認 保存場所（詳細・lpar）です。「logform」は「JFS2でlogformを用い、log=INLINE」を指し、起動確認 log=INLINEではlo・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>logform 起動確認 log=INLINE 0237</strong></p><p>検証目的: JFS2のlogform 起動確認 log=INLINE 0237について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2起動確認117-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; logform
→ Enter を押す
［画面・出力］
/data/aixdd0237:
        dev             = /dev/fslv117
        vfs             = jfs2
        log             = INLINE
確認コード AIX0237A
画面・出力には AIX0237A が表示され、logform 起動確認 log=INLINE 0237 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv117       16.00      9.42   42%     128     1% /data/aixdd0237
確認コード AIX0237B
画面・出力には AIX0237B が表示され、logform 起動確認 log=INLINE 0237 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0237      --         /data/aixdd0237          jfs2  33554432 rw,log=INLINE
確認コード AIX0237C
画面・出力には AIX0237C が表示され、logform 起動確認 log=INLINE 0237 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0237A が画面・出力に表示されること
② ステップ2 の AIX0237B が画面・出力に表示されること
③ ステップ3 の AIX0237C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0060"><h3>lsfs -q 変更前確認 agblksize 0002</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第二観点 JFS2 で lsfs -q は 変更前確認 を点検します（運用第二）（第二観点）。第二観点 確認時には agblksize と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第二）（第二観点）。第二観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第二観点）。第二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0002へ書きます（第二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsfs -q 変更前確認 agblksize 0002の役割を調べています。syslog_ssw -c 変更後確認 Status 0003の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はSRCとログでsyslog_ssw -cを用い・Status とエラーログ一覧を確認する。</li><li>B. 障害切り分けに用いる役割はJFS2でlsfs -qを用い・agblksize とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割は性能管理でvmstat 2 2を用い・po とtopasディスク表示を確認する。</li><li>D. 障害切り分けに用いる役割はSRCとログでlssrc -s syslogdを用い・PID とエラーログ一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「JFS2でlsfs -qを用い、agblksize とファイルシステム属性を確認する」に対応する項目は変更前確認 agblksize（変更・lsfs）です。JFS2の仕様は「JFS2でlsfs -qを用い、agblksize」で、確認対象はls・変更前です。変更後・syslのA:は「SRCとログでsyslog_ssw -cを用い、Status」を述べ、対象は変更後確認 Status（変更・sysl）です。起動・vmstのC:は「性能管理でvmstat 2 2を用い、po」を述べ、対象は起動確認 po（起動・vmst）です。容量・lssrのD:は「SRCとログでlssrc -s syslogdを用い、PID」を述べ、対象は容量確認 PID（容量・lssr）です。「lsfs -q」は「JFS2でlsfs -qを用い、agblksize」を指し、変更前確認 agblksizeではls・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsfs -q 変更前確認 agblksize 0002</strong></p><p>検証目的: JFS2のlsfs -q 変更前確認 agblksize 0002について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更前確認002-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q
→ Enter を押す
［画面・出力］
/data/aixdd0002:
        dev             = /dev/fslv02
        vfs             = jfs2
        log             = INLINE
確認コード AIX0002A
画面・出力には AIX0002A が表示され、lsfs -q 変更前確認 agblksize 0002 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv02       16.00      9.42   42%     128     1% /data/aixdd0002
確認コード AIX0002B
画面・出力には AIX0002B が表示され、lsfs -q 変更前確認 agblksize 0002 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0002      --         /data/aixdd0002          jfs2  33554432 rw,log=INLINE
確認コード AIX0002C
画面・出力には AIX0002C が表示され、lsfs -q 変更前確認 agblksize 0002 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0002A が画面・出力に表示されること
② ステップ2 の AIX0002B が画面・出力に表示されること
③ ステップ3 の AIX0002C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0061"><h3>lsfs -q 状態確認 agblksize 0131</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第百三十一観点 JFS2 で lsfs -q は 状態確認 を点検します（運用第百三十一）（第百三十一観点）。第百三十一観点 確認時には agblksize と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第百三十一）（第百三十一観点）。第百三十一観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第百三十一観点）。第百三十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0131へ書きます（第百三十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsfs -q 状態確認 agblksize 0131について構成や状態を確認します。syslog_ssw -c 構成照合 PID 0132ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はSRCとログでsyslog_ssw -cを用い・PID とsyslog設定変換を確認する。</li><li>B. 一次資料が示す主目的は性能管理でvmstat 2 2を用い・Busy% とAME統計を確認する。</li><li>C. 一次資料が示す主目的はSRCとログでlssrc -s syslogdを用い・Subsystem とsyslog設定変換を確認する。</li><li>D. 一次資料が示す主目的はJFS2でlsfs -qを用い・agblksize と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「JFS2でlsfs -qを用い、agblksize と内部スナップショットを確認する」に対応する項目は状態確認 agblksize（状態・lsfs）です。状態に関するJFS2の仕様は「JFS2でlsfs -qを用い、agblksize」で、確認対象はls・状態です。構成・syslのA:は「SRCとログでsyslog_ssw -cを用い、PID」を述べ、対象は構成照合 PID（構成・sysl）です。容量・vmstのB:は「性能管理でvmstat 2 2を用い、Busy%」を述べ、対象は容量確認 Busy%（容量・vmst）です。監査・lssrのC:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は監査記録 Subsystem（監査・lssr）です。「lsfs -q」は「JFS2でlsfs -qを用い、agblksize」を指し、状態確認 agblksizeではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsfs -q 状態確認 agblksize 0131</strong></p><p>検証目的: JFS2のlsfs -q 状態確認 agblksize 0131について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2状態確認011-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q
→ Enter を押す
［画面・出力］
/data/aixdd0131:
        dev             = /dev/fslv11
        vfs             = jfs2
        log             = INLINE
確認コード AIX0131A
画面・出力には AIX0131A が表示され、lsfs -q 状態確認 agblksize 0131 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv11       16.00      9.42   42%     128     1% /data/aixdd0131
確認コード AIX0131B
画面・出力には AIX0131B が表示され、lsfs -q 状態確認 agblksize 0131 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0131      --         /data/aixdd0131          jfs2  33554432 rw,log=INLINE
確認コード AIX0131C
画面・出力には AIX0131C が表示され、lsfs -q 状態確認 agblksize 0131 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0131A が画面・出力に表示されること
② ステップ2 の AIX0131B が画面・出力に表示されること
③ ステップ3 の AIX0131C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0062"><h3>lsfs -q 状態確認 agblksize 0191</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第百九十一観点 JFS2 で lsfs -q は 状態確認 を点検します（運用第百九十一）（第百九十一観点）。第百九十一観点 確認時には agblksize と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第百九十一）（第百九十一観点）。第百九十一観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第百九十一観点）。第百九十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0191へ書きます（第百九十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsfs -q 状態確認 agblksize 0191の設定や表示を読む前に役割を確認します。syslog_ssw -c 構成照合 PID 0192ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はSRCとログでsyslog_ssw -cを用い・PID とsyslog設定変換を確認する。</li><li>B. 一次資料が示す主目的は性能管理でvmstat -c 2 1を用い・fre とAME統計を確認する。</li><li>C. 一次資料が示す主目的はJFS2でlsfs -qを用い・agblksize と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はSRCとログでlssrc -s syslogdを用い・Subsystem とsyslog設定変換を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でlsfs -qを用い、agblksize と内部スナップショットを確認する」に対応する項目は状態確認 agblksize（状態・lsfs）です。状態に関するJFS2の仕様は「JFS2でlsfs -qを用い、agblksize」で、確認対象はls・状態です。構成・syslのA:は「SRCとログでsyslog_ssw -cを用い、PID」を述べ、対象は構成照合 PID（構成・sysl）です。性能・vmstのB:は「性能管理でvmstat -c 2 1を用い、fre」を述べ、対象は性能確認 fre（性能・vmst）です。監査・lssrのD:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は監査記録 Subsystem（監査・lssr）です。「lsfs -q」は「JFS2でlsfs -qを用い、agblksize」を指し、状態確認 agblksizeではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsfs -q 状態確認 agblksize 0191</strong></p><p>検証目的: JFS2のlsfs -q 状態確認 agblksize 0191について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2状態確認071-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q
→ Enter を押す
［画面・出力］
/data/aixdd0191:
        dev             = /dev/fslv71
        vfs             = jfs2
        log             = INLINE
確認コード AIX0191A
画面・出力には AIX0191A が表示され、lsfs -q 状態確認 agblksize 0191 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv71       16.00      9.42   42%     128     1% /data/aixdd0191
確認コード AIX0191B
画面・出力には AIX0191B が表示され、lsfs -q 状態確認 agblksize 0191 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0191      --         /data/aixdd0191          jfs2  33554432 rw,log=INLINE
確認コード AIX0191C
画面・出力には AIX0191C が表示され、lsfs -q 状態確認 agblksize 0191 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0191A が画面・出力に表示されること
② ステップ2 の AIX0191B が画面・出力に表示されること
③ ステップ3 の AIX0191C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0063"><h3>lsfs -q 状態確認 mountguard 0607</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第六百七観点 JFS2 で lsfs -q は 状態確認 を点検します（運用第六百七）（第六百七観点）。第六百七観点 確認時には mountguard と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第六百七）（第六百七観点）。第六百七観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第六百七観点）。第六百七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0607へ書きます（第六百七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsfs -q 状態確認 mountguard 0607の設定や表示を読む前に役割を確認します。syslog_ssw -c 構成照合 IDENTIFIER 0608ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはSRCとログでsyslog_ssw -cを用い・IDENTIFIER とsyslog設定変換を確認する。</li><li>B. 対象資源に対する働きはJFS2でlsfs -qを用い・mountguard と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きは論理ボリュームの属性と割り当て情報を表示するコマンドである。</li><li>D. 対象資源に対する働きはネットワークでchdev -l en0 -aを用い・MTU と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「JFS2でlsfs -qを用い、mountguard」に対応する項目は状態確認 mountguard（状態・lsfs）です。状態に関するJFS2の仕様は「JFS2でlsfs -qを用い、mountguard」で、確認対象はls・状態です。構成・syslのA:は「SRCとログでsyslog_ssw -cを用い」を述べ、対象は構成照合 IDENTIFIER（構成・sysl）です。復旧前・lslvのC:は「論理ボリュームの属性と割り当て情報を表示するコマンド」を述べ、対象は復旧前確認 サンプル採取（復旧・lslv）です。変更前・chdeのD:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は変更前確認 MTU（変更・chde）です。「lsfs -q」は「JFS2でlsfs -qを用い、mountguard」を指し、状態確認 mountguardではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsfs -q 状態確認 mountguard 0607</strong></p><p>検証目的: JFS2のlsfs -q 状態確認 mountguard 0607について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2状態確認007-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q
→ Enter を押す
［画面・出力］
/data/aixdd0607:
        dev             = /dev/fslv07
        vfs             = jfs2
        log             = INLINE
確認コード AIX0607A
画面・出力には AIX0607A が表示され、lsfs -q 状態確認 mountguard 0607 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv07       16.00      9.42   42%     128     1% /data/aixdd0607
確認コード AIX0607B
画面・出力には AIX0607B が表示され、lsfs -q 状態確認 mountguard 0607 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0607      --         /data/aixdd0607          jfs2  33554432 rw,log=INLINE
確認コード AIX0607C
画面・出力には AIX0607C が表示され、lsfs -q 状態確認 mountguard 0607 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0607A が画面・出力に表示されること
② ステップ2 の AIX0607B が画面・出力に表示されること
③ ステップ3 の AIX0607C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0064"><h3>lsfs -q 状態確認 mountguard 0667</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第六百六十七観点 JFS2 で lsfs -q は 状態確認 を点検します（運用第六百六十七）（第六百六十七観点）。第六百六十七観点 確認時には mountguard と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第六百六十七）（第六百六十七観点）。第六百六十七観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第六百六十七観点）。第六百六十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0667へ書きます（第六百六十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsfs -q 状態確認 mountguard 0667について構成や状態を確認します。syslog_ssw -c 構成照合 IDENTIFIER 0668ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはSRCとログでsyslog_ssw -cを用い・IDENTIFIER とsyslog設定変換を確認する。</li><li>B. 対象資源に対する働きはデバイス管理でcfgmgrを用い・PVID と診断対象表示を確認する。</li><li>C. 対象資源に対する働きはJFS2でlsfs -qを用い・mountguard と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きはネットワークでchdev -l en0 -aを用い・MTU と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でlsfs -qを用い、mountguard」に対応する項目は状態確認 mountguard（状態・lsfs）です。状態に関するJFS2の仕様は「JFS2でlsfs -qを用い、mountguard」で、確認対象はls・状態です。構成・syslのA:は「SRCとログでsyslog_ssw -cを用い」を述べ、対象は構成照合 IDENTIFIER（構成・sysl）です。バック・cfgmのB:は「デバイス管理でcfgmgrを用い、PVID と診断対象表示を確認する」を述べ、対象はバックアウト確認 PVID（バッ・cfgm）です。変更前・chdeのD:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は変更前確認 MTU（変更・chde）です。「lsfs -q」は「JFS2でlsfs -qを用い、mountguard」を指し、状態確認 mountguardではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsfs -q 状態確認 mountguard 0667</strong></p><p>検証目的: JFS2のlsfs -q 状態確認 mountguard 0667について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2状態確認067-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q
→ Enter を押す
［画面・出力］
/data/aixdd0667:
        dev             = /dev/fslv67
        vfs             = jfs2
        log             = INLINE
確認コード AIX0667A
画面・出力には AIX0667A が表示され、lsfs -q 状態確認 mountguard 0667 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv67       16.00      9.42   42%     128     1% /data/aixdd0667
確認コード AIX0667B
画面・出力には AIX0667B が表示され、lsfs -q 状態確認 mountguard 0667 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0667      --         /data/aixdd0667          jfs2  33554432 rw,log=INLINE
確認コード AIX0667C
画面・出力には AIX0667C が表示され、lsfs -q 状態確認 mountguard 0667 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0667A が画面・出力に表示されること
② ステップ2 の AIX0667B が画面・出力に表示されること
③ ステップ3 の AIX0667C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0065"><h3>lsfs -q 監査記録 lff 0161</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第百六十一観点 JFS2 で lsfs -q は 監査記録 を点検します（運用第百六十一）（第百六十一観点）。第百六十一観点 確認時には lff と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第百六十一）（第百六十一観点）。第百六十一観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第百六十一観点）。第百六十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0161へ書きます（第百六十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lsfs -q 監査記録 lff 0161」を「syslog_ssw -c 運用引継ぎ TIMESTAMP 0162」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はSRCとログでsyslog_ssw -cを用い・TIMESTAMP とSRCサブシステム表示を確認する。</li><li>B. 仕様上の役割はJFS2でlsfs -qを用い・lff とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割は性能管理でvmstat 2 2を用い・po とsvmon全体表示を確認する。</li><li>D. 仕様上の役割はSRCとログでlssrc -s syslogdを用い・IDENTIFIERである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でlsfs -qを用い、lff とマウントオプションを確認する」に対応する項目は監査記録 lff（監査・lsfs）です。監査に関するJFS2の仕様は「JFS2でlsfs -qを用い、lff とマウントオプションを確認す」で、確認対象はls・監査です。運用引・syslのA:は「SRCとログでsyslog_ssw -cを用い、TIMESTAMP」を述べ、対象は運用引継ぎ TIMESTAMP（運用・sysl）です。変更前・vmstのC:は「性能管理でvmstat 2 2を用い、po」を述べ、対象は変更前確認 po（変更・vmst）です。状態・lssrのD:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は状態確認 IDENTIFIER（状態・lssr）です。「lsfs -q」は「JFS2でlsfs -qを用い、lff とマウントオプションを確認す」を指し、監査記録 lffではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsfs -q 監査記録 lff 0161</strong></p><p>検証目的: JFS2のlsfs -q 監査記録 lff 0161について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2監査記録041-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q
→ Enter を押す
［画面・出力］
/data/aixdd0161:
        dev             = /dev/fslv41
        vfs             = jfs2
        log             = INLINE
確認コード AIX0161A
画面・出力には AIX0161A が表示され、lsfs -q 監査記録 lff 0161 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv41       16.00      9.42   42%     128     1% /data/aixdd0161
確認コード AIX0161B
画面・出力には AIX0161B が表示され、lsfs -q 監査記録 lff 0161 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0161      --         /data/aixdd0161          jfs2  33554432 rw,log=INLINE
確認コード AIX0161C
画面・出力には AIX0161C が表示され、lsfs -q 監査記録 lff 0161 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0161A が画面・出力に表示されること
② ステップ2 の AIX0161B が画面・出力に表示されること
③ ステップ3 の AIX0161C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0066"><h3>lsfs -q 監査記録 log=INLINE 0637</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第六百三十七観点 JFS2 で lsfs -q は 監査記録 を点検します（運用第六百三十七）（第六百三十七観点）。第六百三十七観点 確認時には log=INLINE と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第六百三十七）（第六百三十七観点）。第六百三十七観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第六百三十七観点）。第六百三十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0637へ書きます（第六百三十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsfs -q 監査記録 log=INLINE 0637を保守記録に説明する必要があります。syslog_ssw -c 運用引継ぎ Subsystem 0638と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はSRCとログでsyslog_ssw -cを用い・Subsystem とSRCサブシステム表示を確認する。</li><li>B. 保守作業で参照する機能はJFS2でlsfs -qを用い・log=INLINE とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はデバイス管理でcfgmgrを用い・Available とODM属性を確認する。</li><li>D. 保守作業で参照する機能はネットワークでchdev -l en0 -aを用い・EtherChannel とアダプター一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でlsfs -qを用い、log=INLINE とマウントオプションを確認する」に対応する項目は監査記録 log=INLINE（監査・lsfs）です。監査に関するJFS2の仕様は「JFS2でlsfs -qを用い、log=INLINE」で、確認対象はls・監査です。運用引・syslのA:は「SRCとログでsyslog_ssw -cを用い、Subsystem」を述べ、対象は運用引継ぎ Subsystem（運用・sysl）です。属性・cfgmのC:は「デバイス管理でcfgmgrを用い、Available」を述べ、対象は属性確認 Available（属性・cfgm）です。容量・chdeのD:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は容量確認 EtherChannel（容量・chde）です。「lsfs -q」は「JFS2でlsfs -qを用い、log=INLINE」を指し、監査記録 log=INLINEではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsfs -q 監査記録 log=INLINE 0637</strong></p><p>検証目的: JFS2のlsfs -q 監査記録 log=INLINE 0637について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2監査記録037-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q
→ Enter を押す
［画面・出力］
/data/aixdd0637:
        dev             = /dev/fslv37
        vfs             = jfs2
        log             = INLINE
確認コード AIX0637A
画面・出力には AIX0637A が表示され、lsfs -q 監査記録 log=INLINE 0637 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv37       16.00      9.42   42%     128     1% /data/aixdd0637
確認コード AIX0637B
画面・出力には AIX0637B が表示され、lsfs -q 監査記録 log=INLINE 0637 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0637      --         /data/aixdd0637          jfs2  33554432 rw,log=INLINE
確認コード AIX0637C
画面・出力には AIX0637C が表示され、lsfs -q 監査記録 log=INLINE 0637 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0637A が画面・出力に表示されること
② ステップ2 の AIX0637B が画面・出力に表示されること
③ ステップ3 の AIX0637C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0067"><h3>lsfs -q 起動確認 isnapshot 0796</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第七百九十六観点 JFS2 で lsfs -q は 起動確認 を点検します（運用第七百九十六）（第七百九十六観点）。第七百九十六観点 確認時には isnapshot と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第七百九十六）（第七百九十六観点）。第七百九十六観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第七百九十六観点）。第七百九十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0796へ書きます（第七百九十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsfs -q 起動確認 isnapshot 0796の技術的な意味を資料で確認するとき、lssecattr -c 障害切り分け enhanced_RBAC 0838との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はJFS2でlsfs -qを用い・isnapshot とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はセキュリティでlssecattr -cを用い・enhanced_RBAC とRBAC属性を確認する。</li><li>C. 管理対象との関係を表す説明は導入と起動でbootlist -m normalを用い・EFIX LABEL と代替ディスク状態を確認する。</li><li>D. 管理対象との関係を表す説明はネットワークでroute -n getを用い・Media Speed Runningである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 起動・lsfsでAの記述「JFS2でlsfs -qを用い、isnapshot」に対応する項目は起動確認 isnapshot（起動・lsfs）です。起動に関するJFS2の仕様は「JFS2でlsfs -qを用い、isnapshot」で、確認対象はls・起動です。障害切・lsseのB:は「セキュリティでlssecattr -cを用い」を述べ、対象は障害切り分け enhanced_RB（障害・lsse）です。変更前・bootのC:は「導入と起動でbootlist -m normalを用い、EFIX」を述べ、対象はEFIX LABEL（変更・boot）です。起動・routのD:は「ネットワークでroute -n getを用い、Media」を述べ、対象はSpeed Running（起動・rout）です。「lsfs -q」は「JFS2でlsfs -qを用い、isnapshot」を指し、起動確認 isnapshotではls・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsfs -q 起動確認 isnapshot 0796</strong></p><p>検証目的: JFS2のlsfs -q 起動確認 isnapshot 0796について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2起動確認076-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q
→ Enter を押す
［画面・出力］
/data/aixdd0796:
        dev             = /dev/fslv76
        vfs             = jfs2
        log             = INLINE
確認コード AIX0796A
画面・出力には AIX0796A が表示され、lsfs -q 起動確認 isnapshot 0796 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv76       16.00      9.42   42%     128     1% /data/aixdd0796
確認コード AIX0796B
画面・出力には AIX0796B が表示され、lsfs -q 起動確認 isnapshot 0796 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0796      --         /data/aixdd0796          jfs2  33554432 rw,log=INLINE
確認コード AIX0796C
画面・出力には AIX0796C が表示され、lsfs -q 起動確認 isnapshot 0796 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0796A が画面・出力に表示されること
② ステップ2 の AIX0796B が画面・出力に表示されること
③ ステップ3 の AIX0796C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0068"><h3>lsfs -q 起動確認 log=INLINE 0320</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第三百二十観点 JFS2 で lsfs -q は 起動確認 を点検します（運用第三百二十）（第三百二十観点）。第三百二十観点 確認時には log=INLINE と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第三百二十）（第三百二十観点）。第三百二十観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第三百二十観点）。第三百二十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0320へ書きます（第三百二十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsfs -q 起動確認 log=INLINE 0320を同一分類のsyslog_ssw -c 属性確認 PID 0321と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はSRCとログでsyslog_ssw -cを用い・PID とinetdデバッグ出力を確認する。</li><li>B. コマンドまたは機能の用途は性能管理でvmstat -c 2 1を用い・po とvmstat表示を確認する。</li><li>C. コマンドまたは機能の用途はJFS2でlsfs -qを用い・log=INLINE とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はネットワークでentstat -d ent0を用い・Media Speed Runningである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でlsfs -qを用い、log=INLINE とログデバイス設定を確認する」に対応する項目は起動確認 log=INLINE（起動・lsfs）です。起動に関するJFS2の仕様は「JFS2でlsfs -qを用い、log=INLINE」で、確認対象はls・起動です。属性・syslのA:は「SRCとログでsyslog_ssw -cを用い、PID」を述べ、対象は属性確認 PID（属性・sysl）です。運用引・vmstのB:は「性能管理でvmstat -c 2 1を用い、po」を述べ、対象は運用引継ぎ po（運用・vmst）です。構成・entsのD:は「ネットワークでentstat -d ent0を用い、Media」を述べ、対象はSpeed Running（構成・ents）です。「lsfs -q」は「JFS2でlsfs -qを用い、log=INLINE」を指し、起動確認 log=INLINEではls・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsfs -q 起動確認 log=INLINE 0320</strong></p><p>検証目的: JFS2のlsfs -q 起動確認 log=INLINE 0320について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2起動確認080-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q
→ Enter を押す
［画面・出力］
/data/aixdd0320:
        dev             = /dev/fslv80
        vfs             = jfs2
        log             = INLINE
確認コード AIX0320A
画面・出力には AIX0320A が表示され、lsfs -q 起動確認 log=INLINE 0320 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv80       16.00      9.42   42%     128     1% /data/aixdd0320
確認コード AIX0320B
画面・出力には AIX0320B が表示され、lsfs -q 起動確認 log=INLINE 0320 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0320      --         /data/aixdd0320          jfs2  33554432 rw,log=INLINE
確認コード AIX0320C
画面・出力には AIX0320C が表示され、lsfs -q 起動確認 log=INLINE 0320 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0320A が画面・出力に表示されること
② ステップ2 の AIX0320B が画面・出力に表示されること
③ ステップ3 の AIX0320C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0069"><h3>lsfs -q 障害切り分け mountguard 0350</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第三百五十観点 JFS2 で lsfs -q は 障害切り分け を点検します（運用第三百五十）（第三百五十観点）。第三百五十観点 確認時には mountguard と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第三百五十）（第三百五十観点）。第三百五十観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第三百五十観点）。第三百五十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0350へ書きます（第三百五十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsfs -q 障害切り分け mountguard 0350に関する障害切り分けの前提を確認しています。syslog_ssw -c バックアウト確認 TIMESTAMP 0351の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はSRCとログでsyslog_ssw -cを用い・TIMESTAMP とエラーログ一覧を確認する。</li><li>B. 障害切り分けに用いる役割はJFS2でlsfs -qを用い・mountguard とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割は性能管理でvmstat -c 2 1を用い・avm とtopasディスク表示を確認する。</li><li>D. 障害切り分けに用いる役割はネットワークでentstat -d ent0を用い・Gateway とEthernet統計を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「JFS2でlsfs -qを用い、mountguard」に対応する項目は障害切り分け mountguard（障害・lsfs）です。障害切に関するJFS2の仕様は「JFS2でlsfs -qを用い、mountguard」で、確認対象はls・障害切です。バック・syslのA:は「SRCとログでsyslog_ssw -cを用い、TIMESTAMP」を述べ、対象はバックアウト確認 TIMESTAMP（バッ・sysl）です。構成・vmstのC:は「性能管理でvmstat -c 2 1を用い、avm」を述べ、対象は構成照合 avm（構成・vmst）です。運用引・entsのD:は「ネットワークでentstat -d ent0を用い、Gateway」を述べ、対象は運用引継ぎ Gateway（運用・ents）です。「lsfs -q」は「JFS2でlsfs -qを用い、mountguard」を指し、障害切り分け mountguardではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsfs -q 障害切り分け mountguard 0350</strong></p><p>検証目的: JFS2のlsfs -q 障害切り分け mountguard 0350について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2障害切り分け110-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q
→ Enter を押す
［画面・出力］
/data/aixdd0350:
        dev             = /dev/fslv110
        vfs             = jfs2
        log             = INLINE
確認コード AIX0350A
画面・出力には AIX0350A が表示され、lsfs -q 障害切り分け mountguard 0350 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv110       16.00      9.42   42%     128     1% /data/aixdd0350
確認コード AIX0350B
画面・出力には AIX0350B が表示され、lsfs -q 障害切り分け mountguard 0350 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0350      --         /data/aixdd0350          jfs2  33554432 rw,log=INLINE
確認コード AIX0350C
画面・出力には AIX0350C が表示され、lsfs -q 障害切り分け mountguard 0350 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0350A が画面・出力に表示されること
② ステップ2 の AIX0350B が画面・出力に表示されること
③ ステップ3 の AIX0350C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0070"><h3>lsfs -q 障害切り分け ファイルシステム使用率 0826</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第八百二十六観点 JFS2 で lsfs -q は 障害切り分け を点検します（運用第八百二十六）（第八百二十六観点）。第八百二十六観点 確認時には ファイルシステム使用率 と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第八百二十六）（第八百二十六観点）。第八百二十六観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第八百二十六観点）。第八百二十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0826へ書きます（第八百二十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsfs -q 障害切り分け ファイルシステム使用率 0826の役割を調べています。lscfg 復旧前確認 障害記録の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はJFS2でlsfs -qを用い・ファイルシステム使用率 とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容は構成済みデバイスと VPD を表示するコマンドである。</li><li>C. 表示や設定で扱う内容はSRCとログでerrclearを用い・syslog.conf とinetdデバッグ出力を確認する。</li><li>D. 表示や設定で扱う内容はSRCとログでtail -f /tmp/myfileを用い・IDENTIFIERである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 障害切・lsfsでAの記述「JFS2でlsfs -qを用い、ファイルシステム使用率」に対応する項目は障害切り分け ファイルシステム使用率（障害・lsfs）です。障害切・ファイに関するJFS2の仕様は「JFS2でlsfs -qを用い、ファイルシステム使用率」で、確認対象はls・障害切です。復旧前・lscfのB:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は復旧前確認 障害記録（復旧・lscf）です。運用引・errcのC:は「SRCとログでerrclearを用い、syslog.conf」を述べ、対象は運用引継ぎ syslog.conf（運用・errc）です。構成・tailのD:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は構成照合 IDENTIFIER（構成・tail）です。「lsfs -q」は「JFS2でlsfs -qを用い、ファイルシステム使用率」を指し、障害切り分け ファイルシステム使用率ではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsfs -q 障害切り分け ファイルシステム使用率 0826</strong></p><p>検証目的: JFS2のlsfs -q 障害切り分け ファイルシステム使用率 0826について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2障害切り分け106-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q
→ Enter を押す
［画面・出力］
/data/aixdd0826:
        dev             = /dev/fslv106
        vfs             = jfs2
        log             = INLINE
確認コード AIX0826A
画面・出力には AIX0826A が表示され、lsfs -q 障害切り分け ファイルシステム使用率 0826 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv106       16.00      9.42   42%     128     1% /data/aixdd0826
確認コード AIX0826B
画面・出力には AIX0826B が表示され、lsfs -q 障害切り分け ファイルシステム使用率 0826 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0826      --         /data/aixdd0826          jfs2  33554432 rw,log=INLINE
確認コード AIX0826C
画面・出力には AIX0826C が表示され、lsfs -q 障害切り分け ファイルシステム使用率 0826 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0826A が画面・出力に表示されること
② ステップ2 の AIX0826B が画面・出力に表示されること
③ ステップ3 の AIX0826C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0071"><h3>mount -o remount バックアウト確認 lff 0410</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第四百十観点 JFS2 で mount -o remount は バックアウト確認 を点検します（運用第四百十）（第四百十観点）。第四百十観点 確認時には lff と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第四百十）（第四百十観点）。第四百十観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第四百十観点）。第四百十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0410へ書きます（第四百十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mount -o remount バックアウト確認 lff 0410の役割を調べています。syslog_ssw -r 監査記録 syslog.conf 0411の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はSRCとログでsyslog_ssw -rを用い・syslog.conf とエラーログ一覧を確認する。</li><li>B. 障害切り分けに用いる役割は性能管理でvmstat -c 2 1を用い・po とtopasディスク表示を確認する。</li><li>C. 障害切り分けに用いる役割はネットワークでentstat -d ent0を用い・Gateway とEthernet統計を確認する。</li><li>D. 障害切り分けに用いる役割はJFS2でmount -o remountを用い・lff とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でmount -o remountを用い、lff」に対応する項目はバックアウト確認 lff（バッ・moun）です。バックに関するJFS2の仕様は「JFS2でmount -o remountを用い、lff」で、確認対象はmo・バックです。監査・syslのA:は「SRCとログでsyslog_ssw -rを用い」を述べ、対象は監査記録 syslog.conf（監査・sysl）です。構成・vmstのB:は「性能管理でvmstat -c 2 1を用い、po」を述べ、対象は構成照合 po（構成・vmst）です。運用引・entsのC:は「ネットワークでentstat -d ent0を用い、Gateway」を述べ、対象は運用引継ぎ Gateway（運用・ents）です。「mount -o remount」は「JFS2でmount -o remountを用い、lff」を指し、バックアウト確認 lffではmo・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mount -o remount バックアウト確認 lff 0410</strong></p><p>検証目的: JFS2のmount -o remount バックアウト確認 lff 0410について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2バックアウト確認050-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount -o remount
→ Enter を押す
［画面・出力］
/data/aixdd0410:
        dev             = /dev/fslv50
        vfs             = jfs2
        log             = INLINE
確認コード AIX0410A
画面・出力には AIX0410A が表示され、mount -o remount バックアウト確認 lff 0410 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv50       16.00      9.42   42%     128     1% /data/aixdd0410
確認コード AIX0410B
画面・出力には AIX0410B が表示され、mount -o remount バックアウト確認 lff 0410 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0410      --         /data/aixdd0410          jfs2  33554432 rw,log=INLINE
確認コード AIX0410C
画面・出力には AIX0410C が表示され、mount -o remount バックアウト確認 lff 0410 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0410A が画面・出力に表示されること
② ステップ2 の AIX0410B が画面・出力に表示されること
③ ステップ3 の AIX0410C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0072"><h3>mount -o remount 変更後確認 isnapshot 0063</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第六十三観点 JFS2 で mount -o remount は 変更後確認 を点検します（運用第六十三）（第六十三観点）。第六十三観点 確認時には isnapshot と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第六十三）（第六十三観点）。第六十三観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第六十三観点）。第六十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0063へ書きます（第六十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mount -o remount 変更後確認 isnapshot 0063の設定や表示を読む前に役割を確認します。syslog_ssw -r 障害切り分け Status 0064ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはSRCとログでsyslog_ssw -rを用い・Status とsyslog設定変換を確認する。syslog_ssw -r 障害切り分け Status 0064固有の属性も確認対象に含める。</li><li>B. 状態を読み取るための働きは性能管理でsvmon -Gを用い・Entitled Capacity とAME統計を確認する。</li><li>C. 状態を読み取るための働きはJFS2でmount -o remountを用い・isnapshot と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 状態を読み取るための働きはSRCとログでstartsrc -s syslogdを用い・PID とsyslog設定変換を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でmount -o remountを用い、isnapshot」に対応する項目は変更後確認 isnapshot（変更・moun）です。JFS2の仕様は「JFS2でmount -o remountを用い、isnapshot」で、確認対象はmo・変更後です。障害切・syslのA:は「SRCとログでsyslog_ssw -rを用い、Status」を述べ、対象は障害切り分け Status（障害・sysl）です。状態・svmoのB:は「性能管理でsvmon -Gを用い、Entitled」を述べ、対象はEntitled Capacity（状態・svmo）です。性能・starのD:は「SRCとログでstartsrc -s syslogdを用い、PID」を述べ、対象は性能確認 PID（性能・star）です。「mount -o remount」は「JFS2でmount -o remountを用い」を指し、変更後確認 isnapshotではmo・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mount -o remount 変更後確認 isnapshot 0063</strong></p><p>検証目的: JFS2のmount -o remount 変更後確認 isnapshot 0063について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更後確認063-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount -o remount
→ Enter を押す
［画面・出力］
/data/aixdd0063:
        dev             = /dev/fslv63
        vfs             = jfs2
        log             = INLINE
確認コード AIX0063A
画面・出力には AIX0063A が表示され、mount -o remount 変更後確認 isnapshot 0063 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv63       16.00      9.42   42%     128     1% /data/aixdd0063
確認コード AIX0063B
画面・出力には AIX0063B が表示され、mount -o remount 変更後確認 isnapshot 0063 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0063      --         /data/aixdd0063          jfs2  33554432 rw,log=INLINE
確認コード AIX0063C
画面・出力には AIX0063C が表示され、mount -o remount 変更後確認 isnapshot 0063 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0063A が画面・出力に表示されること
② ステップ2 の AIX0063B が画面・出力に表示されること
③ ステップ3 の AIX0063C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0073"><h3>mount -o remount 変更後確認 lff 0539</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第五百三十九観点 JFS2 で mount -o remount は 変更後確認 を点検します（運用第五百三十九）（第五百三十九観点）。第五百三十九観点 確認時には lff と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第五百三十九）（第五百三十九観点）。第五百三十九観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第五百三十九観点）。第五百三十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0539へ書きます（第五百三十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mount -o remount 変更後確認 lff 0539について構成や状態を確認します。syslog_ssw -r 障害切り分け TIMESTAMP 0540ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はSRCとログでsyslog_ssw -rを用い・TIMESTAMP とsyslog設定変換を確認する。</li><li>B. 一次資料が示す主目的はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>C. 一次資料が示す主目的はJFS2でmount -o remountを用い・lff と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 一次資料が示す主目的はネットワークでentstat -d ent0を用い・Destination と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でmount -o remountを用い、lff」に対応する項目は変更後確認 lff（変更・moun）です。変更後に関するJFS2の仕様は「JFS2でmount -o remountを用い、lff」で、確認対象はmo・変更後です。障害切・syslのA:は「SRCとログでsyslog_ssw -rを用い、TIMESTAMP」を述べ、対象は障害切り分け TIMESTAMP（障害・sysl）です。障害切・errpのB:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は障害切り分け ログ採取（障害・errp）です。バック・entsのD:は「ネットワークでentstat -d ent0を用い」を述べ、対象はバックアウト確認 Destinati（バッ・ents）です。「mount -o remount」は「JFS2でmount -o remountを用い、lff」を指し、変更後確認 lffではmo・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mount -o remount 変更後確認 lff 0539</strong></p><p>検証目的: JFS2のmount -o remount 変更後確認 lff 0539について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更後確認059-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount -o remount
→ Enter を押す
［画面・出力］
/data/aixdd0539:
        dev             = /dev/fslv59
        vfs             = jfs2
        log             = INLINE
確認コード AIX0539A
画面・出力には AIX0539A が表示され、mount -o remount 変更後確認 lff 0539 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv59       16.00      9.42   42%     128     1% /data/aixdd0539
確認コード AIX0539B
画面・出力には AIX0539B が表示され、mount -o remount 変更後確認 lff 0539 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0539      --         /data/aixdd0539          jfs2  33554432 rw,log=INLINE
確認コード AIX0539C
画面・出力には AIX0539C が表示され、mount -o remount 変更後確認 lff 0539 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0539A が画面・出力に表示されること
② ステップ2 の AIX0539B が画面・出力に表示されること
③ ステップ3 の AIX0539C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0074"><h3>mount -o remount 変更後確認 lff 0599</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第五百九十九観点 JFS2 で mount -o remount は 変更後確認 を点検します（運用第五百九十九）（第五百九十九観点）。第五百九十九観点 確認時には lff と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第五百九十九）（第五百九十九観点）。第五百九十九観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第五百九十九観点）。第五百九十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0599へ書きます（第五百九十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mount -o remount 変更後確認 lff 0599の設定や表示を読む前に役割を確認します。syslog_ssw -r 障害切り分け TIMESTAMP 0600ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はSRCとログでsyslog_ssw -rを用い・TIMESTAMP とsyslog設定変換を確認する。</li><li>B. 一次資料が示す主目的はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>C. 一次資料が示す主目的はネットワークでnetstat -rnを用い・Gateway と経路表を確認する。</li><li>D. 一次資料が示す主目的はJFS2でmount -o remountを用い・lff と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「JFS2でmount -o remountを用い、lff」に対応する項目は変更後確認 lff（変更・moun）です。変更後に関するJFS2の仕様は「JFS2でmount -o remountを用い、lff」で、確認対象はmo・変更後です。障害切・syslのA:は「SRCとログでsyslog_ssw -rを用い、TIMESTAMP」を述べ、対象は障害切り分け TIMESTAMP（障害・sysl）です。変更前・errpのB:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は変更前確認 再読込（変更・errp）です。監査・netsのC:は「ネットワークでnetstat -rnを用い、Gateway」を述べ、対象は監査記録 Gateway（監査・nets）です。「mount -o remount」は「JFS2でmount -o remountを用い、lff」を指し、変更後確認 lffではmo・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mount -o remount 変更後確認 lff 0599</strong></p><p>検証目的: JFS2のmount -o remount 変更後確認 lff 0599について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更後確認119-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount -o remount
→ Enter を押す
［画面・出力］
/data/aixdd0599:
        dev             = /dev/fslv119
        vfs             = jfs2
        log             = INLINE
確認コード AIX0599A
画面・出力には AIX0599A が表示され、mount -o remount 変更後確認 lff 0599 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv119       16.00      9.42   42%     128     1% /data/aixdd0599
確認コード AIX0599B
画面・出力には AIX0599B が表示され、mount -o remount 変更後確認 lff 0599 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0599      --         /data/aixdd0599          jfs2  33554432 rw,log=INLINE
確認コード AIX0599C
画面・出力には AIX0599C が表示され、mount -o remount 変更後確認 lff 0599 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0599A が画面・出力に表示されること
② ステップ2 の AIX0599B が画面・出力に表示されること
③ ステップ3 の AIX0599C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0075"><h3>mount -o remount 属性確認 agblksize 0380</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第三百八十観点 JFS2 で mount -o remount は 属性確認 を点検します（運用第三百八十）（第三百八十観点）。第三百八十観点 確認時には agblksize と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第三百八十）（第三百八十観点）。第三百八十観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第三百八十観点）。第三百八十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0380へ書きます（第三百八十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mount -o remount 属性確認 agblksize 0380の技術的な意味を資料で確認するとき、syslog_ssw -r 状態確認 Status 0381との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はSRCとログでsyslog_ssw -rを用い・Status とinetdデバッグ出力を確認する。</li><li>B. コマンドまたは機能の用途は性能管理でvmstat -c 2 1を用い・Busy% とvmstat表示を確認する。</li><li>C. コマンドまたは機能の用途はJFS2でmount -o remountを用い・agblksize とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途はネットワークでentstat -d ent0を用い・Media Speed Runningである。entstat -d ent0 構成照合 Media Speed固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「JFS2でmount -o remountを用い、agblksize」に対応する項目は属性確認 agblksize（属性・moun）です。属性に関するJFS2の仕様は「JFS2でmount -o remountを用い」で、確認対象はmo・属性です。状態・syslのA:は「SRCとログでsyslog_ssw -rを用い、Status」を述べ、対象は状態確認 Status（状態・sysl）です。運用引・vmstのB:は「性能管理でvmstat -c 2 1を用い、Busy%」を述べ、対象は運用引継ぎ Busy%（運用・vmst）です。構成・entsのD:は「ネットワークでentstat -d ent0を用い、Media」を述べ、対象はSpeed Running（構成・ents）です。「mount -o remount」は「JFS2でmount -o remountを用い」を指し、属性確認 agblksizeではmo・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mount -o remount 属性確認 agblksize 0380</strong></p><p>検証目的: JFS2のmount -o remount 属性確認 agblksize 0380について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2属性確認020-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount -o remount
→ Enter を押す
［画面・出力］
/data/aixdd0380:
        dev             = /dev/fslv20
        vfs             = jfs2
        log             = INLINE
確認コード AIX0380A
画面・出力には AIX0380A が表示され、mount -o remount 属性確認 agblksize 0380 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv20       16.00      9.42   42%     128     1% /data/aixdd0380
確認コード AIX0380B
画面・出力には AIX0380B が表示され、mount -o remount 属性確認 agblksize 0380 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0380      --         /data/aixdd0380          jfs2  33554432 rw,log=INLINE
確認コード AIX0380C
画面・出力には AIX0380C が表示され、mount -o remount 属性確認 agblksize 0380 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0380A が画面・出力に表示されること
② ステップ2 の AIX0380B が画面・出力に表示されること
③ ステップ3 の AIX0380C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0076"><h3>mount -o remount 性能確認 agblksize 0509</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第五百九観点 JFS2 で mount -o remount は 性能確認 を点検します（運用第五百九）（第五百九観点）。第五百九観点 確認時には agblksize と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第五百九）（第五百九観点）。第五百九観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第五百九観点）。第五百九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0509へ書きます（第五百九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mount -o remount 性能確認 agblksize 0509を保守記録に説明する必要があります。syslog_ssw -r 起動確認 PID 0510と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はSRCとログでsyslog_ssw -rを用い・PID とSRCサブシステム表示を確認する。</li><li>B. 仕様上の役割は性能管理でvmstat -c 2 1を用い・avm とsvmon全体表示を確認する。</li><li>C. 仕様上の役割はネットワークでentstat -d ent0を用い・Link Status とアダプター一覧を確認する。</li><li>D. 仕様上の役割はJFS2でmount -o remountを用い・agblksize とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でmount -o remountを用い、agblksize」に対応する項目は性能確認 agblksize（性能・moun）です。性能に関するJFS2の仕様は「JFS2でmount -o remountを用い」で、確認対象はmo・性能です。起動・syslのA:は「SRCとログでsyslog_ssw -rを用い、PID」を述べ、対象は起動確認 PID（起動・sysl）です。バック・vmstのB:は「性能管理でvmstat -c 2 1を用い、avm」を述べ、対象はバックアウト確認 avm（バッ・vmst）です。属性・entsのC:は「ネットワークでentstat -d ent0を用い、Link」を述べ、対象はLink Status（属性・ents）です。「mount -o remount」は「JFS2でmount -o remountを用い」を指し、性能確認 agblksizeではmo・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mount -o remount 性能確認 agblksize 0509</strong></p><p>検証目的: JFS2のmount -o remount 性能確認 agblksize 0509について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2性能確認029-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount -o remount
→ Enter を押す
［画面・出力］
/data/aixdd0509:
        dev             = /dev/fslv29
        vfs             = jfs2
        log             = INLINE
確認コード AIX0509A
画面・出力には AIX0509A が表示され、mount -o remount 性能確認 agblksize 0509 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv29       16.00      9.42   42%     128     1% /data/aixdd0509
確認コード AIX0509B
画面・出力には AIX0509B が表示され、mount -o remount 性能確認 agblksize 0509 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0509      --         /data/aixdd0509          jfs2  33554432 rw,log=INLINE
確認コード AIX0509C
画面・出力には AIX0509C が表示され、mount -o remount 性能確認 agblksize 0509 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0509A が画面・出力に表示されること
② ステップ2 の AIX0509B が画面・出力に表示されること
③ ステップ3 の AIX0509C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0077"><h3>mount -o remount 性能確認 agblksize 0569</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第五百六十九観点 JFS2 で mount -o remount は 性能確認 を点検します（運用第五百六十九）（第五百六十九観点）。第五百六十九観点 確認時には agblksize と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第五百六十九）（第五百六十九観点）。第五百六十九観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第五百六十九観点）。第五百六十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0569へ書きます（第五百六十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「mount -o remount 性能確認 agblksize 0569」を「syslog_ssw -r 起動確認 PID 0570」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はSRCとログでsyslog_ssw -rを用い・PID とSRCサブシステム表示を確認する。</li><li>B. 仕様上の役割はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>C. 仕様上の役割はネットワークでnetstat -rnを用い・Media Speed Runningである。netstat -rn 状態確認 Media Speed固有の属性も確認対象に含める。</li><li>D. 仕様上の役割はJFS2でmount -o remountを用い・agblksize とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でmount -o remountを用い、agblksize」に対応する項目は性能確認 agblksize（性能・moun）です。性能に関するJFS2の仕様は「JFS2でmount -o remountを用い」で、確認対象はmo・性能です。起動・syslのA:は「SRCとログでsyslog_ssw -rを用い、PID」を述べ、対象は起動確認 PID（起動・sysl）です。性能・チュ・errpのB:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は性能確認 チューニング値（性能・errp）です。状態・netsのC:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（状態・nets）です。「mount -o remount」は「JFS2でmount -o remountを用い」を指し、性能確認 agblksizeではmo・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mount -o remount 性能確認 agblksize 0569</strong></p><p>検証目的: JFS2のmount -o remount 性能確認 agblksize 0569について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2性能確認089-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount -o remount
→ Enter を押す
［画面・出力］
/data/aixdd0569:
        dev             = /dev/fslv89
        vfs             = jfs2
        log             = INLINE
確認コード AIX0569A
画面・出力には AIX0569A が表示され、mount -o remount 性能確認 agblksize 0569 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv89       16.00      9.42   42%     128     1% /data/aixdd0569
確認コード AIX0569B
画面・出力には AIX0569B が表示され、mount -o remount 性能確認 agblksize 0569 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0569      --         /data/aixdd0569          jfs2  33554432 rw,log=INLINE
確認コード AIX0569C
画面・出力には AIX0569C が表示され、mount -o remount 性能確認 agblksize 0569 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0569A が画面・出力に表示されること
② ステップ2 の AIX0569B が画面・出力に表示されること
③ ステップ3 の AIX0569C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0078"><h3>mount -o remount 性能確認 ファイルシステム使用率 0033</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第三十三観点 JFS2 で mount -o remount は 性能確認 を点検します（運用第三十三）（第三十三観点）。第三十三観点 確認時には ファイルシステム使用率 と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第三十三）（第三十三観点）。第三十三観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第三十三観点）。第三十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0033へ書きます（第三十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「mount -o remount 性能確認 ファイルシステム使用率 0033」を「syslog_ssw -r 起動確認 syslog.conf 0034」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はSRCとログでsyslog_ssw -rを用い・syslog.conf とSRCサブシステム表示を確認する。</li><li>B. 運用時に利用する技術的役割は性能管理でvmstat -c 2 1を用い・fre とsvmon全体表示を確認する。</li><li>C. 運用時に利用する技術的役割はJFS2でmount -o remountを用い・ファイルシステム使用率 とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はSRCとログでstartsrc -s syslogdを用い・TIMESTAMPである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でmount -o remountを用い、ファイルシステム使用率」に対応する項目は性能確認 ファイルシステム使用率（性能・moun）です。JFS2の仕様は「JFS2でmount -o remountを用い」で、確認対象はmo・性能・ファです。起動・syslのA:は「SRCとログでsyslog_ssw -rを用い」を述べ、対象は起動確認 syslog.conf（起動・sysl）です。バック・vmstのB:は「性能管理でvmstat -c 2 1を用い、fre」を述べ、対象はバックアウト確認 fre（バッ・vmst）です。変更後・starのD:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は変更後確認 TIMESTAMP（変更・star）です。「mount -o remount」は「JFS2でmount -o remountを用い」を指し、性能確認 ファイルシステム使用率ではmo・性能・ファに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mount -o remount 性能確認 ファイルシステム使用率 0033</strong></p><p>検証目的: JFS2のmount -o remount 性能確認 ファイルシステム使用率 0033について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2性能確認033-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount -o remount
→ Enter を押す
［画面・出力］
/data/aixdd0033:
        dev             = /dev/fslv33
        vfs             = jfs2
        log             = INLINE
確認コード AIX0033A
画面・出力には AIX0033A が表示され、mount -o remount 性能確認 ファイルシステム使用率 0033 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv33       16.00      9.42   42%     128     1% /data/aixdd0033
確認コード AIX0033B
画面・出力には AIX0033B が表示され、mount -o remount 性能確認 ファイルシステム使用率 0033 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0033      --         /data/aixdd0033          jfs2  33554432 rw,log=INLINE
確認コード AIX0033C
画面・出力には AIX0033C が表示され、mount -o remount 性能確認 ファイルシステム使用率 0033 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0033A が画面・出力に表示されること
② ステップ2 の AIX0033B が画面・出力に表示されること
③ ステップ3 の AIX0033C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0079"><h3>mount -o remount 性能確認 ファイルシステム使用率 0093</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第九十三観点 JFS2 で mount -o remount は 性能確認 を点検します（運用第九十三）（第九十三観点）。第九十三観点 確認時には ファイルシステム使用率 と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第九十三）（第九十三観点）。第九十三観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第九十三観点）。第九十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0093へ書きます（第九十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> mount -o remount 性能確認 ファイルシステム使用率 0093を保守記録に説明する必要があります。syslog_ssw -r 起動確認 syslog.conf 0094と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はJFS2でmount -o remountを用い・ファイルシステム使用率 とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はSRCとログでsyslog_ssw -rを用い・syslog.conf とSRCサブシステム表示を確認する。</li><li>C. 運用時に利用する技術的役割は性能管理でsvmon -Gを用い・dxm とsvmon全体表示を確認する。</li><li>D. 運用時に利用する技術的役割はSRCとログでstartsrc -s syslogdを用い・TIMESTAMPである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「JFS2でmount -o remountを用い、ファイルシステム使用率」に対応する項目は性能確認 ファイルシステム使用率（性能・moun）です。性能・ファイに関するJFS2の仕様は「JFS2でmount -o remountを用い」で、確認対象はmo・性能・ファです。起動・syslのB:は「SRCとログでsyslog_ssw -rを用い」を述べ、対象は起動確認 syslog.conf（起動・sysl）です。監査・svmoのC:は「性能管理でsvmon -Gを用い、dxm」を述べ、対象は監査記録 dxm（監査・svmo）です。変更後・starのD:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は変更後確認 TIMESTAMP（変更・star）です。「mount -o remount」は「JFS2でmount -o remountを用い」を指し、性能確認 ファイルシステム使用率ではmo・性能・ファに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>mount -o remount 性能確認 ファイルシステム使用率 0093</strong></p><p>検証目的: JFS2のmount -o remount 性能確認 ファイルシステム使用率 0093について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2性能確認093-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount -o remount
→ Enter を押す
［画面・出力］
/data/aixdd0093:
        dev             = /dev/fslv93
        vfs             = jfs2
        log             = INLINE
確認コード AIX0093A
画面・出力には AIX0093A が表示され、mount -o remount 性能確認 ファイルシステム使用率 0093 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv93       16.00      9.42   42%     128     1% /data/aixdd0093
確認コード AIX0093B
画面・出力には AIX0093B が表示され、mount -o remount 性能確認 ファイルシステム使用率 0093 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0093      --         /data/aixdd0093          jfs2  33554432 rw,log=INLINE
確認コード AIX0093C
画面・出力には AIX0093C が表示され、mount -o remount 性能確認 ファイルシステム使用率 0093 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0093A が画面・出力に表示されること
② ステップ2 の AIX0093B が画面・出力に表示されること
③ ステップ3 の AIX0093C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0080"><h3>snap 容量確認 lff 0116</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第百十六観点 JFS2 で snap は 容量確認 を点検します（運用第百十六）（第百十六観点）。第百十六観点 確認時には lff と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第百十六）（第百十六観点）。第百十六観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第百十六観点）。第百十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0116へ書きます（第百十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> snap 容量確認 lff 0116の技術的な意味を資料で確認するとき、errclear 性能確認 syslog.conf 0117との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はSRCとログでerrclearを用い・syslog.conf とinetdデバッグ出力を確認する。</li><li>B. コマンドまたは機能の用途は性能管理でtopas -Cを用い・PhysB とvmstat表示を確認する。</li><li>C. コマンドまたは機能の用途はSRCとログでerrptを用い・syslog.conf とinetdデバッグ出力を確認する。</li><li>D. コマンドまたは機能の用途はJFS2でsnapを用い・lff とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「JFS2でsnapを用い、lff とログデバイス設定を確認する」に対応する項目は容量確認 lff（容量・snap）です。容量に関するJFS2の仕様は「JFS2でsnapを用い、lff とログデバイス設定を確認する」で、確認対象はsn・容量です。性能・errcのA:は「SRCとログでerrclearを用い、syslog.conf」を述べ、対象は性能確認 syslog.conf（性能・errc）です。バック・topaのB:は「性能管理でtopas -Cを用い、PhysB」を述べ、対象はバックアウト確認 PhysB（バッ・topa）です。変更後・errpのC:は「SRCとログでerrptを用い、syslog.conf」を述べ、対象は変更後確認 syslog.conf（変更・errp）です。「snap」は「JFS2でsnapを用い、lff とログデバイス設定を確認する」を指し、容量確認 lffではsn・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>snap 容量確認 lff 0116</strong></p><p>検証目的: JFS2のsnap 容量確認 lff 0116について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2容量確認116-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; snap
→ Enter を押す
［画面・出力］
/data/aixdd0116:
        dev             = /dev/fslv116
        vfs             = jfs2
        log             = INLINE
確認コード AIX0116A
画面・出力には AIX0116A が表示され、snap 容量確認 lff 0116 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv116       16.00      9.42   42%     128     1% /data/aixdd0116
確認コード AIX0116B
画面・出力には AIX0116B が表示され、snap 容量確認 lff 0116 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0116      --         /data/aixdd0116          jfs2  33554432 rw,log=INLINE
確認コード AIX0116C
画面・出力には AIX0116C が表示され、snap 容量確認 lff 0116 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0116A が画面・出力に表示されること
② ステップ2 の AIX0116B が画面・出力に表示されること
③ ステップ3 の AIX0116C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0081"><h3>snap 容量確認 log=INLINE 0592</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第五百九十二観点 JFS2 で snap は 容量確認 を点検します（運用第五百九十二）（第五百九十二観点）。第五百九十二観点 確認時には log=INLINE と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第五百九十二）（第五百九十二観点）。第五百九十二観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第五百九十二観点）。第五百九十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0592へ書きます（第五百九十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> snap 容量確認 log=INLINE 0592を同一分類のerrclear 性能確認 PID 0593と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はSRCとログでerrclearを用い・PID とinetdデバッグ出力を確認する。</li><li>B. 管理対象との関係を表す説明はJFS2でsnapを用い・log=INLINE とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明は構成済みデバイスと VPD を表示するコマンドである。</li><li>D. 管理対象との関係を表す説明はネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「JFS2でsnapを用い、log=INLINE とログデバイス設定を確認する」に対応する項目は容量確認 log=INLINE（容量・snap）です。容量に関するJFS2の仕様は「JFS2でsnapを用い、log=INLINE」で、確認対象はsn・容量です。性能・errcのA:は「SRCとログでerrclearを用い、PID」を述べ、対象は性能確認 PID（性能・errc）です。変更前・lscfのC:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は変更前確認 障害記録（変更・lscf）です。属性・noのD:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（属性・no）です。「snap」は「JFS2でsnapを用い、log=INLINE」を指し、容量確認 log=INLINEではsn・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>snap 容量確認 log=INLINE 0592</strong></p><p>検証目的: JFS2のsnap 容量確認 log=INLINE 0592について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2容量確認112-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; snap
→ Enter を押す
［画面・出力］
/data/aixdd0592:
        dev             = /dev/fslv112
        vfs             = jfs2
        log             = INLINE
確認コード AIX0592A
画面・出力には AIX0592A が表示され、snap 容量確認 log=INLINE 0592 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv112       16.00      9.42   42%     128     1% /data/aixdd0592
確認コード AIX0592B
画面・出力には AIX0592B が表示され、snap 容量確認 log=INLINE 0592 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。log=INLINE を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0592      --         /data/aixdd0592          jfs2  33554432 rw,log=INLINE
確認コード AIX0592C
画面・出力には AIX0592C が表示され、snap 容量確認 log=INLINE 0592 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0592A が画面・出力に表示されること
② ステップ2 の AIX0592B が画面・出力に表示されること
③ ステップ3 の AIX0592C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0082"><h3>snap 状態確認 agblksize 0274</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第二百七十四観点 JFS2 で snap は 状態確認 を点検します（運用第二百七十四）（第二百七十四観点）。第二百七十四観点 確認時には agblksize と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第二百七十四）（第二百七十四観点）。第二百七十四観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第二百七十四観点）。第二百七十四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0274へ書きます（第二百七十四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> snap 状態確認 agblksize 0274の役割を調べています。errclear 構成照合 Status 0275の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はSRCとログでerrclearを用い・Status とエラーログ一覧を確認する。</li><li>B. 表示や設定で扱う内容はJFS2でsnapを用い・agblksize とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容は性能管理でtopas -Dを用い・Busy% とtopasディスク表示を確認する。</li><li>D. 表示や設定で扱う内容はデバイス属性を変更する管理コマンドである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でsnapを用い、agblksize とファイルシステム属性を確認する」に対応する項目は状態確認 agblksize（状態・snap）です。状態に関するJFS2の仕様は「JFS2でsnapを用い、agblksize」で、確認対象はsn・状態です。構成・errcのA:は「SRCとログでerrclearを用い、Status」を述べ、対象は構成照合 Status（構成・errc）です。容量・topaのC:は「性能管理でtopas -Dを用い、Busy%」を述べ、対象は容量確認 Busy%（容量・topa）です。状態・対象・chdeのD:は「デバイス属性を変更する管理コマンド」を述べ、対象は状態判定 対象ノード（状態・chde）です。「snap」は「JFS2でsnapを用い、agblksize」を指し、状態確認 agblksizeではsn・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>snap 状態確認 agblksize 0274</strong></p><p>検証目的: JFS2のsnap 状態確認 agblksize 0274について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2状態確認034-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; snap
→ Enter を押す
［画面・出力］
/data/aixdd0274:
        dev             = /dev/fslv34
        vfs             = jfs2
        log             = INLINE
確認コード AIX0274A
画面・出力には AIX0274A が表示され、snap 状態確認 agblksize 0274 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv34       16.00      9.42   42%     128     1% /data/aixdd0274
確認コード AIX0274B
画面・出力には AIX0274B が表示され、snap 状態確認 agblksize 0274 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0274      --         /data/aixdd0274          jfs2  33554432 rw,log=INLINE
確認コード AIX0274C
画面・出力には AIX0274C が表示され、snap 状態確認 agblksize 0274 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0274A が画面・出力に表示されること
② ステップ2 の AIX0274B が画面・出力に表示されること
③ ステップ3 の AIX0274C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0083"><h3>snap 状態確認 mountguard 0750</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第七百五十観点 JFS2 で snap は 状態確認 を点検します（運用第七百五十）（第七百五十観点）。第七百五十観点 確認時には mountguard と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第七百五十）（第七百五十観点）。第七百五十観点 lsfs -q /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第七百五十観点）。第七百五十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0750へ書きます（第七百五十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> snap 状態確認 mountguard 0750に関する障害切り分けの前提を確認しています。errclear 構成照合 TIMESTAMP 0751の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはJFS2でsnapを用い・mountguard とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 機能の説明としてはSRCとログでerrclearを用い・TIMESTAMP とエラーログ一覧を確認する。</li><li>C. 機能の説明としてはセキュリティでlsuserを用い・user attributes とユーザー属性を確認する。</li><li>D. 機能の説明としてはネットワークでsmitty etherchannelを用い・Destinationである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「JFS2でsnapを用い、mountguard とファイルシステム属性を確認する」に対応する項目は状態確認 mountguard（状態・snap）です。状態に関するJFS2の仕様は「JFS2でsnapを用い、mountguard」で、確認対象はsn・状態です。構成・errcのB:は「SRCとログでerrclearを用い、TIMESTAMP」を述べ、対象は構成照合 TIMESTAMP（構成・errc）です。バック・lsusのC:は「セキュリティでlsuserを用い、user attributes」を述べ、対象はuser attributes（バッ・lsus）です。変更前・smitのD:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は変更前確認 Destination（変更・smit）です。「snap」は「JFS2でsnapを用い、mountguard」を指し、状態確認 mountguardではsn・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>snap 状態確認 mountguard 0750</strong></p><p>検証目的: JFS2のsnap 状態確認 mountguard 0750について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2状態確認030-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; snap
→ Enter を押す
［画面・出力］
/data/aixdd0750:
        dev             = /dev/fslv30
        vfs             = jfs2
        log             = INLINE
確認コード AIX0750A
画面・出力には AIX0750A が表示され、snap 状態確認 mountguard 0750 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv30       16.00      9.42   42%     128     1% /data/aixdd0750
確認コード AIX0750B
画面・出力には AIX0750B が表示され、snap 状態確認 mountguard 0750 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。mountguard を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0750      --         /data/aixdd0750          jfs2  33554432 rw,log=INLINE
確認コード AIX0750C
画面・出力には AIX0750C が表示され、snap 状態確認 mountguard 0750 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0750A が画面・出力に表示されること
② ステップ2 の AIX0750B が画面・出力に表示されること
③ ステップ3 の AIX0750C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0084"><h3>snap 監査記録 lff 0244</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第二百四十四観点 JFS2 で snap は 監査記録 を点検します（運用第二百四十四）（第二百四十四観点）。第二百四十四観点 確認時には lff と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第二百四十四）（第二百四十四観点）。第二百四十四観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第二百四十四観点）。第二百四十四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0244へ書きます（第二百四十四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> snap 監査記録 lff 0244の技術的な意味を資料で確認するとき、errclear 運用引継ぎ syslog.conf 0245との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はSRCとログでerrclearを用い・syslog.conf とinetdデバッグ出力を確認する。</li><li>B. 管理対象との関係を表す説明は性能管理でtopas -Dを用い・avm とvmstat表示を確認する。</li><li>C. 管理対象との関係を表す説明はデバイス属性を変更する管理コマンドである。</li><li>D. 管理対象との関係を表す説明はJFS2でsnapを用い・lff とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「JFS2でsnapを用い、lff とログデバイス設定を確認する」に対応する項目は監査記録 lff（監査・snap）です。監査に関するJFS2の仕様は「JFS2でsnapを用い、lff とログデバイス設定を確認する」で、確認対象はsn・監査です。運用引・errcのA:は「SRCとログでerrclearを用い、syslog.conf」を述べ、対象は運用引継ぎ syslog.conf（運用・errc）です。変更前・topaのB:は「性能管理でtopas -Dを用い、avm」を述べ、対象は変更前確認 avm（変更・topa）です。詳細・一致・chdeのC:は「デバイス属性を変更する管理コマンド」を述べ、対象は詳細確認 一致条件（詳細・chde）です。「snap」は「JFS2でsnapを用い、lff とログデバイス設定を確認する」を指し、監査記録 lffではsn・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>snap 監査記録 lff 0244</strong></p><p>検証目的: JFS2のsnap 監査記録 lff 0244について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2監査記録004-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; snap
→ Enter を押す
［画面・出力］
/data/aixdd0244:
        dev             = /dev/fslv04
        vfs             = jfs2
        log             = INLINE
確認コード AIX0244A
画面・出力には AIX0244A が表示され、snap 監査記録 lff 0244 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv04       16.00      9.42   42%     128     1% /data/aixdd0244
確認コード AIX0244B
画面・出力には AIX0244B が表示され、snap 監査記録 lff 0244 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0244      --         /data/aixdd0244          jfs2  33554432 rw,log=INLINE
確認コード AIX0244C
画面・出力には AIX0244C が表示され、snap 監査記録 lff 0244 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0244A が画面・出力に表示されること
② ステップ2 の AIX0244B が画面・出力に表示されること
③ ステップ3 の AIX0244C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0085"><h3>snap 起動確認 agblksize 0403</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第四百三観点 JFS2 で snap は 起動確認 を点検します（運用第四百三）（第四百三観点）。第四百三観点 確認時には agblksize と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第四百三）（第四百三観点）。第四百三観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第四百三観点）。第四百三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0403へ書きます（第四百三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> snap 起動確認 agblksize 0403について構成や状態を確認します。errclear 属性確認 PID 0404ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはSRCとログでerrclearを用い・PID とsyslog設定変換を確認する。</li><li>B. 対象資源に対する働きは性能管理でtopas -Dを用い・avm とAME統計を確認する。</li><li>C. 対象資源に対する働きはネットワークでsmitty etherchannelを用い・Link Status と経路表を確認する。</li><li>D. 対象資源に対する働きはJFS2でsnapを用い・agblksize と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でsnapを用い、agblksize と内部スナップショットを確認する」に対応する項目は起動確認 agblksize（起動・snap）です。起動に関するJFS2の仕様は「JFS2でsnapを用い、agblksize」で、確認対象はsn・起動です。属性・errcのA:は「SRCとログでerrclearを用い、PID」を述べ、対象は属性確認 PID（属性・errc）です。監査・topaのB:は「性能管理でtopas -Dを用い、avm とAME統計を確認する」を述べ、対象は監査記録 avm（監査・topa）です。状態・smitのC:は「ネットワークでsmitty etherchannelを用い」を述べ、対象はLink Status（状態・smit）です。「snap」は「JFS2でsnapを用い、agblksize」を指し、起動確認 agblksizeではsn・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>snap 起動確認 agblksize 0403</strong></p><p>検証目的: JFS2のsnap 起動確認 agblksize 0403について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2起動確認043-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; snap
→ Enter を押す
［画面・出力］
/data/aixdd0403:
        dev             = /dev/fslv43
        vfs             = jfs2
        log             = INLINE
確認コード AIX0403A
画面・出力には AIX0403A が表示され、snap 起動確認 agblksize 0403 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv43       16.00      9.42   42%     128     1% /data/aixdd0403
確認コード AIX0403B
画面・出力には AIX0403B が表示され、snap 起動確認 agblksize 0403 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0403      --         /data/aixdd0403          jfs2  33554432 rw,log=INLINE
確認コード AIX0403C
画面・出力には AIX0403C が表示され、snap 起動確認 agblksize 0403 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0403A が画面・出力に表示されること
② ステップ2 の AIX0403B が画面・出力に表示されること
③ ステップ3 の AIX0403C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0086"><h3>snap 起動確認 agblksize 0463</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 上級</p><p>第四百六十三観点 JFS2 で snap は 起動確認 を点検します（運用第四百六十三）（第四百六十三観点）。第四百六十三観点 確認時には agblksize と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第四百六十三）（第四百六十三観点）。第四百六十三観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第四百六十三観点）。第四百六十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0463へ書きます（第四百六十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> snap 起動確認 agblksize 0463の設定や表示を読む前に役割を確認します。errclear 属性確認 PID 0464ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはSRCとログでerrclearを用い・PID とsyslog設定変換を確認する。</li><li>B. 対象資源に対する働きは性能管理でtopas -Cを用い・csz とAME統計を確認する。</li><li>C. 対象資源に対する働きはネットワークでno -aを用い・Media Speed Running と経路表を確認する。</li><li>D. 対象資源に対する働きはJFS2でsnapを用い・agblksize と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「JFS2でsnapを用い、agblksize と内部スナップショットを確認する」に対応する項目は起動確認 agblksize（起動・snap）です。起動に関するJFS2の仕様は「JFS2でsnapを用い、agblksize」で、確認対象はsn・起動です。属性・errcのA:は「SRCとログでerrclearを用い、PID」を述べ、対象は属性確認 PID（属性・errc）です。運用引・topaのB:は「性能管理でtopas -Cを用い、csz とAME統計を確認する」を述べ、対象は運用引継ぎ csz（運用・topa）です。構成・noのC:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（構成・no）です。「snap」は「JFS2でsnapを用い、agblksize」を指し、起動確認 agblksizeではsn・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>snap 起動確認 agblksize 0463</strong></p><p>検証目的: JFS2のsnap 起動確認 agblksize 0463について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2起動確認103-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; snap
→ Enter を押す
［画面・出力］
/data/aixdd0463:
        dev             = /dev/fslv103
        vfs             = jfs2
        log             = INLINE
確認コード AIX0463A
画面・出力には AIX0463A が表示され、snap 起動確認 agblksize 0463 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv103       16.00      9.42   42%     128     1% /data/aixdd0463
確認コード AIX0463B
画面・出力には AIX0463B が表示され、snap 起動確認 agblksize 0463 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0463      --         /data/aixdd0463          jfs2  33554432 rw,log=INLINE
確認コード AIX0463C
画面・出力には AIX0463C が表示され、snap 起動確認 agblksize 0463 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0463A が画面・出力に表示されること
② ステップ2 の AIX0463B が画面・出力に表示されること
③ ステップ3 の AIX0463C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0087"><h3>snap 障害切り分け lff 0373</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第三百七十三観点 JFS2 で snap は 障害切り分け を点検します（運用第三百七十三）（第三百七十三観点）。第三百七十三観点 確認時には lff と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第三百七十三）（第三百七十三観点）。第三百七十三観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第三百七十三観点）。第三百七十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0373へ書きます（第三百七十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> snap 障害切り分け lff 0373を保守記録に説明する必要があります。errclear バックアウト確認 TIMESTAMP 0374と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はJFS2でsnapを用い・lff とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 保守作業で参照する機能はSRCとログでerrclearを用い・TIMESTAMP とSRCサブシステム表示を確認する。</li><li>C. 保守作業で参照する機能は性能管理でtopas -Dを用い・po とsvmon全体表示を確認する。</li><li>D. 保守作業で参照する機能はネットワークでsmitty etherchannelを用い・Destinationである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Aの記述「JFS2でsnapを用い、lff とマウントオプションを確認する」に対応する項目は障害切り分け lff（障害・snap）です。障害切に関するJFS2の仕様は「JFS2でsnapを用い、lff とマウントオプションを確認する」で、確認対象はsn・障害切です。バック・errcのB:は「SRCとログでerrclearを用い、TIMESTAMP」を述べ、対象はバックアウト確認 TIMESTAMP（バッ・errc）です。状態・topaのC:は「性能管理でtopas -Dを用い、po とsvmon全体表示を確認す」を述べ、対象は状態確認 po（状態・topa）です。監査・smitのD:は「ネットワークでsmitty etherchannelを用い」を述べ、対象は監査記録 Destination（監査・smit）です。「snap」は「JFS2でsnapを用い、lff とマウントオプションを確認する」を指し、障害切り分け lffではsn・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>snap 障害切り分け lff 0373</strong></p><p>検証目的: JFS2のsnap 障害切り分け lff 0373について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2障害切り分け013-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; snap
→ Enter を押す
［画面・出力］
/data/aixdd0373:
        dev             = /dev/fslv13
        vfs             = jfs2
        log             = INLINE
確認コード AIX0373A
画面・出力には AIX0373A が表示され、snap 障害切り分け lff 0373 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv13       16.00      9.42   42%     128     1% /data/aixdd0373
確認コード AIX0373B
画面・出力には AIX0373B が表示され、snap 障害切り分け lff 0373 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0373      --         /data/aixdd0373          jfs2  33554432 rw,log=INLINE
確認コード AIX0373C
画面・出力には AIX0373C が表示され、snap 障害切り分け lff 0373 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0373A が画面・出力に表示されること
② ステップ2 の AIX0373B が画面・出力に表示されること
③ ステップ3 の AIX0373C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0088"><h3>snap 障害切り分け lff 0433</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第四百三十三観点 JFS2 で snap は 障害切り分け を点検します（運用第四百三十三）（第四百三十三観点）。第四百三十三観点 確認時には lff と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第四百三十三）（第四百三十三観点）。第四百三十三観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第四百三十三観点）。第四百三十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0433へ書きます（第四百三十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「snap 障害切り分け lff 0433」を「errclear バックアウト確認 TIMESTAMP 0434」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はSRCとログでerrclearを用い・TIMESTAMP とSRCサブシステム表示を確認する。</li><li>B. 保守作業で参照する機能は性能管理でtopas -Cを用い・PhysB とsvmon全体表示を確認する。</li><li>C. 保守作業で参照する機能はネットワークでno -aを用い・Gateway とアダプター一覧を確認する。</li><li>D. 保守作業で参照する機能はJFS2でsnapを用い・lff とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「JFS2でsnapを用い、lff とマウントオプションを確認する」に対応する項目は障害切り分け lff（障害・snap）です。障害切に関するJFS2の仕様は「JFS2でsnapを用い、lff とマウントオプションを確認する」で、確認対象はsn・障害切です。バック・errcのA:は「SRCとログでerrclearを用い、TIMESTAMP」を述べ、対象はバックアウト確認 TIMESTAMP（バッ・errc）です。構成・topaのB:は「性能管理でtopas -Cを用い、PhysB」を述べ、対象は構成照合 PhysB（構成・topa）です。運用引・noのC:は「ネットワークでno -aを用い、Gateway」を述べ、対象は運用引継ぎ Gateway（運用・no）です。「snap」は「JFS2でsnapを用い、lff とマウントオプションを確認する」を指し、障害切り分け lffではsn・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>snap 障害切り分け lff 0433</strong></p><p>検証目的: JFS2のsnap 障害切り分け lff 0433について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2障害切り分け073-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; snap
→ Enter を押す
［画面・出力］
/data/aixdd0433:
        dev             = /dev/fslv73
        vfs             = jfs2
        log             = INLINE
確認コード AIX0433A
画面・出力には AIX0433A が表示され、snap 障害切り分け lff 0433 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv73       16.00      9.42   42%     128     1% /data/aixdd0433
確認コード AIX0433B
画面・出力には AIX0433B が表示され、snap 障害切り分け lff 0433 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0433      --         /data/aixdd0433          jfs2  33554432 rw,log=INLINE
確認コード AIX0433C
画面・出力には AIX0433C が表示され、snap 障害切り分け lff 0433 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0433A が画面・出力に表示されること
② ステップ2 の AIX0433B が画面・出力に表示されること
③ ステップ3 の AIX0433C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0089"><h3>splitcopy 変更後確認 isnapshot 0146</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第百四十六観点 JFS2 で splitcopy は 変更後確認 を点検します（運用第百四十六）（第百四十六観点）。第百四十六観点 確認時には isnapshot と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第百四十六）（第百四十六観点）。第百四十六観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第百四十六観点）。第百四十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0146へ書きます（第百四十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> splitcopy 変更後確認 isnapshot 0146の役割を調べています。startsrc -s inetd -a &quot;-d&quot; 障害切り分けの説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はSRCとログでstartsrc -s inetd -aを用い・IDENTIFIERである。</li><li>B. 障害切り分けに用いる役割は性能管理でtopas -Cを用い・csz とtopasディスク表示を確認する。</li><li>C. 障害切り分けに用いる役割はJFS2でsplitcopyを用い・isnapshot とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割はSRCとログでerrptを用い・Status とエラーログ一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「JFS2でsplitcopyを用い、isnapshot」に対応する項目は変更後確認 isnapshot（変更・spli）です。変更後に関するJFS2の仕様は「JFS2でsplitcopyを用い、isnapshot」で、確認対象はsp・変更後です。障害切・starのA:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け IDENTIFIER（障害・star）です。属性・topaのB:は「性能管理でtopas -Cを用い、csz」を述べ、対象は属性確認 csz（属性・topa）です。性能・errpのD:は「SRCとログでerrptを用い、Status」を述べ、対象は性能確認 Status（性能・errp）です。「splitcopy」は「JFS2でsplitcopyを用い、isnapshot」を指し、変更後確認 isnapshotではsp・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>splitcopy 変更後確認 isnapshot 0146</strong></p><p>検証目的: JFS2のsplitcopy 変更後確認 isnapshot 0146について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更後確認026-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; splitcopy
→ Enter を押す
［画面・出力］
/data/aixdd0146:
        dev             = /dev/fslv26
        vfs             = jfs2
        log             = INLINE
確認コード AIX0146A
画面・出力には AIX0146A が表示され、splitcopy 変更後確認 isnapshot 0146 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv26       16.00      9.42   42%     128     1% /data/aixdd0146
確認コード AIX0146B
画面・出力には AIX0146B が表示され、splitcopy 変更後確認 isnapshot 0146 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0146      --         /data/aixdd0146          jfs2  33554432 rw,log=INLINE
確認コード AIX0146C
画面・出力には AIX0146C が表示され、splitcopy 変更後確認 isnapshot 0146 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0146A が画面・出力に表示されること
② ステップ2 の AIX0146B が画面・出力に表示されること
③ ステップ3 の AIX0146C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0090"><h3>splitcopy 変更後確認 isnapshot 0206</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第二百六観点 JFS2 で splitcopy は 変更後確認 を点検します（運用第二百六）（第二百六観点）。第二百六観点 確認時には isnapshot と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第二百六）（第二百六観点）。第二百六観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第二百六観点）。第二百六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0206へ書きます（第二百六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> splitcopy 変更後確認 isnapshot 0206に関する障害切り分けの前提を確認しています。startsrc -s inetd -a &quot;-d&quot; 障害切り分けの機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はSRCとログでstartsrc -s inetd -aを用い・IDENTIFIERである。</li><li>B. 障害切り分けに用いる役割はJFS2でsplitcopyを用い・isnapshot とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割は性能管理でnmonを用い・Entitled Capacity とtopasディスク表示を確認する。</li><li>D. 障害切り分けに用いる役割はSRCとログでerrptを用い・Status とエラーログ一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でsplitcopyを用い、isnapshot」に対応する項目は変更後確認 isnapshot（変更・spli）です。変更後に関するJFS2の仕様は「JFS2でsplitcopyを用い、isnapshot」で、確認対象はsp・変更後です。障害切・starのA:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け IDENTIFIER（障害・star）です。状態・nmonのC:は「性能管理でnmonを用い、Entitled Capacity」を述べ、対象はEntitled Capacity（状態・nmon）です。性能・errpのD:は「SRCとログでerrptを用い、Status」を述べ、対象は性能確認 Status（性能・errp）です。「splitcopy」は「JFS2でsplitcopyを用い、isnapshot」を指し、変更後確認 isnapshotではsp・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>splitcopy 変更後確認 isnapshot 0206</strong></p><p>検証目的: JFS2のsplitcopy 変更後確認 isnapshot 0206について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更後確認086-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; splitcopy
→ Enter を押す
［画面・出力］
/data/aixdd0206:
        dev             = /dev/fslv86
        vfs             = jfs2
        log             = INLINE
確認コード AIX0206A
画面・出力には AIX0206A が表示され、splitcopy 変更後確認 isnapshot 0206 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv86       16.00      9.42   42%     128     1% /data/aixdd0206
確認コード AIX0206B
画面・出力には AIX0206B が表示され、splitcopy 変更後確認 isnapshot 0206 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0206      --         /data/aixdd0206          jfs2  33554432 rw,log=INLINE
確認コード AIX0206C
画面・出力には AIX0206C が表示され、splitcopy 変更後確認 isnapshot 0206 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0206A が画面・出力に表示されること
② ステップ2 の AIX0206B が画面・出力に表示されること
③ ステップ3 の AIX0206C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0091"><h3>splitcopy 変更後確認 lff 0622</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 初級</p><p>第六百二十二観点 JFS2 で splitcopy は 変更後確認 を点検します（運用第六百二十二）（第六百二十二観点）。第六百二十二観点 確認時には lff と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第六百二十二）（第六百二十二観点）。第六百二十二観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第六百二十二観点）。第六百二十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0622へ書きます（第六百二十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> splitcopy 変更後確認 lff 0622に関する障害切り分けの前提を確認しています。startsrc -s inetd -a &quot;-d&quot; 障害切り分けの機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はSRCとログでstartsrc -s inetd -aを用い・syslog.confである。</li><li>B. 表示や設定で扱う内容はデバイス管理でbootinfo -B hdisk0を用い・path statusである。</li><li>C. 表示や設定で扱う内容はネットワークでno -aを用い・Gateway とEthernet統計を確認する。</li><li>D. 表示や設定で扱う内容はJFS2でsplitcopyを用い・lff とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「JFS2でsplitcopyを用い、lff とファイルシステム属性を確認する」に対応する項目は変更後確認 lff（変更・spli）です。変更後に関するJFS2の仕様は「JFS2でsplitcopyを用い、lff」で、確認対象はsp・変更後です。障害切・starのA:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け syslog.conf（障害・star）です。容量・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い、path」を述べ、対象はpath status（容量・boot）です。バック・noのC:は「ネットワークでno -aを用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・no）です。「splitcopy」は「JFS2でsplitcopyを用い、lff」を指し、変更後確認 lffではsp・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>splitcopy 変更後確認 lff 0622</strong></p><p>検証目的: JFS2のsplitcopy 変更後確認 lff 0622について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更後確認022-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; splitcopy
→ Enter を押す
［画面・出力］
/data/aixdd0622:
        dev             = /dev/fslv22
        vfs             = jfs2
        log             = INLINE
確認コード AIX0622A
画面・出力には AIX0622A が表示され、splitcopy 変更後確認 lff 0622 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv22       16.00      9.42   42%     128     1% /data/aixdd0622
確認コード AIX0622B
画面・出力には AIX0622B が表示され、splitcopy 変更後確認 lff 0622 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0622      --         /data/aixdd0622          jfs2  33554432 rw,log=INLINE
確認コード AIX0622C
画面・出力には AIX0622C が表示され、splitcopy 変更後確認 lff 0622 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0622A が画面・出力に表示されること
② ステップ2 の AIX0622B が画面・出力に表示されること
③ ステップ3 の AIX0622C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0092"><h3>splitcopy 変更後確認 lff 0682</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第六百八十二観点 JFS2 で splitcopy は 変更後確認 を点検します（運用第六百八十二）（第六百八十二観点）。第六百八十二観点 確認時には lff と ファイルシステム属性 の対応を同じ資料上で追えることを前提にします（資料第六百八十二）（第六百八十二観点）。第六百八十二観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、lff属性の不可逆変更 を避ける判断根拠を説明可能にします（第六百八十二観点）。第六百八十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0682へ書きます（第六百八十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> splitcopy 変更後確認 lff 0682の役割を調べています。startsrc -s inetd -a &quot;-d&quot; 障害切り分けの説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はSRCとログでstartsrc -s inetd -aを用い・syslog.confである。</li><li>B. 表示や設定で扱う内容はJFS2でsplitcopyを用い・lff とファイルシステム属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 表示や設定で扱う内容はセキュリティでpwdck -n ALLを用い・user attributes とユーザー属性を確認する。</li><li>D. 表示や設定で扱う内容はネットワークでroute -n getを用い・EtherChannel とEthernet統計を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でsplitcopyを用い、lff とファイルシステム属性を確認する」に対応する項目は変更後確認 lff（変更・spli）です。変更後に関するJFS2の仕様は「JFS2でsplitcopyを用い、lff」で、確認対象はsp・変更後です。障害切・starのA:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は障害切り分け syslog.conf（障害・star）です。容量・pwdcのC:は「セキュリティでpwdck -n ALLを用い、user」を述べ、対象はuser attributes（容量・pwdc）です。監査・routのD:は「ネットワークでroute -n getを用い」を述べ、対象は監査記録 EtherChannel（監査・rout）です。「splitcopy」は「JFS2でsplitcopyを用い、lff」を指し、変更後確認 lffではsp・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>splitcopy 変更後確認 lff 0682</strong></p><p>検証目的: JFS2のsplitcopy 変更後確認 lff 0682について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2変更後確認082-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; splitcopy
→ Enter を押す
［画面・出力］
/data/aixdd0682:
        dev             = /dev/fslv82
        vfs             = jfs2
        log             = INLINE
確認コード AIX0682A
画面・出力には AIX0682A が表示され、splitcopy 変更後確認 lff 0682 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv82       16.00      9.42   42%     128     1% /data/aixdd0682
確認コード AIX0682B
画面・出力には AIX0682B が表示され、splitcopy 変更後確認 lff 0682 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0682      --         /data/aixdd0682          jfs2  33554432 rw,log=INLINE
確認コード AIX0682C
画面・出力には AIX0682C が表示され、splitcopy 変更後確認 lff 0682 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0682A が画面・出力に表示されること
② ステップ2 の AIX0682B が画面・出力に表示されること
③ ステップ3 の AIX0682C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0093"><h3>splitcopy 性能確認 agblksize 0652</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第六百五十二観点 JFS2 で splitcopy は 性能確認 を点検します（運用第六百五十二）（第六百五十二観点）。第六百五十二観点 確認時には agblksize と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第六百五十二）（第六百五十二観点）。第六百五十二観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第六百五十二観点）。第六百五十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0652へ書きます（第六百五十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> splitcopy 性能確認 agblksize 0652の技術的な意味を資料で確認するとき、startsrc -s inetd -a &quot;-d&quot; 起動確認 Status 0653との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はSRCとログでstartsrc -s inetd -aを用い・Statusである。</li><li>B. 管理対象との関係を表す説明はJFS2でsplitcopyを用い・agblksize とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はデバイス管理でbootinfo -B hdisk0を用い・location codeである。</li><li>D. 管理対象との関係を表す説明はネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でsplitcopyを用い、agblksize とログデバイス設定を確認する」に対応する項目は性能確認 agblksize（性能・spli）です。性能に関するJFS2の仕様は「JFS2でsplitcopyを用い、agblksize」で、確認対象はsp・性能です。起動・starのA:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は起動確認 Status（起動・star）です。変更前・bootのC:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象はlocation code（変更・boot）です。属性・noのD:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（属性・no）です。「splitcopy」は「JFS2でsplitcopyを用い、agblksize」を指し、性能確認 agblksizeではsp・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>splitcopy 性能確認 agblksize 0652</strong></p><p>検証目的: JFS2のsplitcopy 性能確認 agblksize 0652について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2性能確認052-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; splitcopy
→ Enter を押す
［画面・出力］
/data/aixdd0652:
        dev             = /dev/fslv52
        vfs             = jfs2
        log             = INLINE
確認コード AIX0652A
画面・出力には AIX0652A が表示され、splitcopy 性能確認 agblksize 0652 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv52       16.00      9.42   42%     128     1% /data/aixdd0652
確認コード AIX0652B
画面・出力には AIX0652B が表示され、splitcopy 性能確認 agblksize 0652 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0652      --         /data/aixdd0652          jfs2  33554432 rw,log=INLINE
確認コード AIX0652C
画面・出力には AIX0652C が表示され、splitcopy 性能確認 agblksize 0652 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0652A が画面・出力に表示されること
② ステップ2 の AIX0652B が画面・出力に表示されること
③ ステップ3 の AIX0652C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0094"><h3>splitcopy 性能確認 ファイルシステム使用率 0176</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第百七十六観点 JFS2 で splitcopy は 性能確認 を点検します（運用第百七十六）（第百七十六観点）。第百七十六観点 確認時には ファイルシステム使用率 と ログデバイス設定 の対応を同じ資料上で追えることを前提にします（資料第百七十六）（第百七十六観点）。第百七十六観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、INLINEログとOUTLINEログの混同 を避ける判断根拠を説明可能にします（第百七十六観点）。第百七十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0176へ書きます（第百七十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> splitcopy 性能確認 ファイルシステム使用率 0176を同一分類のstartsrc -s inetd -a &quot;-d&quot; 起動確認 Subsystemと比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はJFS2でsplitcopyを用い・ファイルシステム使用率 とログデバイス設定を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はSRCとログでstartsrc -s inetd -aを用い・Subsystemである。</li><li>C. コマンドまたは機能の用途は性能管理でnmonを用い・pi とvmstat表示を確認する。</li><li>D. コマンドまたは機能の用途はSRCとログでerrptを用い・syslog.conf とinetdデバッグ出力を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「JFS2でsplitcopyを用い、ファイルシステム使用率」に対応する項目は性能確認 ファイルシステム使用率（性能・spli）です。性能・ファイに関するJFS2の仕様は「JFS2でsplitcopyを用い、ファイルシステム使用率」で、確認対象はsp・性能・ファです。起動・starのB:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は起動確認 Subsystem（起動・star）です。監査・nmonのC:は「性能管理でnmonを用い、pi とvmstat表示を確認する」を述べ、対象は監査記録 pi（監査・nmon）です。変更後・errpのD:は「SRCとログでerrptを用い、syslog.conf」を述べ、対象は変更後確認 syslog.conf（変更・errp）です。「splitcopy」は「JFS2でsplitcopyを用い、ファイルシステム使用率」を指し、性能確認 ファイルシステム使用率ではsp・性能・ファに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>splitcopy 性能確認 ファイルシステム使用率 0176</strong></p><p>検証目的: JFS2のsplitcopy 性能確認 ファイルシステム使用率 0176について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2性能確認056-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; splitcopy
→ Enter を押す
［画面・出力］
/data/aixdd0176:
        dev             = /dev/fslv56
        vfs             = jfs2
        log             = INLINE
確認コード AIX0176A
画面・出力には AIX0176A が表示され、splitcopy 性能確認 ファイルシステム使用率 0176 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv56       16.00      9.42   42%     128     1% /data/aixdd0176
確認コード AIX0176B
画面・出力には AIX0176B が表示され、splitcopy 性能確認 ファイルシステム使用率 0176 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0176      --         /data/aixdd0176          jfs2  33554432 rw,log=INLINE
確認コード AIX0176C
画面・出力には AIX0176C が表示され、splitcopy 性能確認 ファイルシステム使用率 0176 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0176A が画面・出力に表示されること
② ステップ2 の AIX0176B が画面・出力に表示されること
③ ステップ3 の AIX0176C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0095"><h3>splitcopy 構成照合 isnapshot 0335</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第三百三十五観点 JFS2 で splitcopy は 構成照合 を点検します（運用第三百三十五）（第三百三十五観点）。第三百三十五観点 確認時には isnapshot と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第三百三十五）（第三百三十五観点）。第三百三十五観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第三百三十五観点）。第三百三十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0335へ書きます（第三百三十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> splitcopy 構成照合 isnapshot 0335の設定や表示を読む前に役割を確認します。startsrc -s inetd -a &quot;-d&quot; 変更前確認 Statusではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はSRCとログでstartsrc -s inetd -aを用い・Status とsyslog設定変換を確認する。</li><li>B. 一次資料が示す主目的はJFS2でsplitcopyを用い・isnapshot と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 一次資料が示す主目的は性能管理でnmonを用い・pi とAME統計を確認する。</li><li>D. 一次資料が示す主目的はネットワークでroute -n getを用い・MTU と経路表を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「JFS2でsplitcopyを用い、isnapshot」に対応する項目は構成照合 isnapshot（構成・spli）です。構成に関するJFS2の仕様は「JFS2でsplitcopyを用い、isnapshot」で、確認対象はsp・構成です。変更前・starのA:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は変更前確認 Status（変更・star）です。起動・nmonのC:は「性能管理でnmonを用い、pi とAME統計を確認する」を述べ、対象は起動確認 pi（起動・nmon）です。障害切・routのD:は「ネットワークでroute -n getを用い、MTU」を述べ、対象は障害切り分け MTU（障害・rout）です。「splitcopy」は「JFS2でsplitcopyを用い、isnapshot」を指し、構成照合 isnapshotではsp・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>splitcopy 構成照合 isnapshot 0335</strong></p><p>検証目的: JFS2のsplitcopy 構成照合 isnapshot 0335について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2構成照合095-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; splitcopy
→ Enter を押す
［画面・出力］
/data/aixdd0335:
        dev             = /dev/fslv95
        vfs             = jfs2
        log             = INLINE
確認コード AIX0335A
画面・出力には AIX0335A が表示され、splitcopy 構成照合 isnapshot 0335 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv95       16.00      9.42   42%     128     1% /data/aixdd0335
確認コード AIX0335B
画面・出力には AIX0335B が表示され、splitcopy 構成照合 isnapshot 0335 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。isnapshot を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0335      --         /data/aixdd0335          jfs2  33554432 rw,log=INLINE
確認コード AIX0335C
画面・出力には AIX0335C が表示され、splitcopy 構成照合 isnapshot 0335 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0335A が画面・出力に表示されること
② ステップ2 の AIX0335B が画面・出力に表示されること
③ ステップ3 の AIX0335C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0096"><h3>splitcopy 構成照合 lff 0811</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第八百十一観点 JFS2 で splitcopy は 構成照合 を点検します（運用第八百十一）（第八百十一観点）。第八百十一観点 確認時には lff と 内部スナップショット の対応を同じ資料上で追えることを前提にします（資料第八百十一）（第八百十一観点）。第八百十一観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、mountguard解除の誤用 を避ける判断根拠を説明可能にします（第八百十一観点）。第八百十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0811へ書きます（第八百十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> splitcopy 構成照合 lff 0811について構成や状態を確認します。errpt 性能確認 Status 0819ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはSRCとログでerrptを用い・Status とエラーログ一覧を確認する。</li><li>B. 対象資源に対する働きは導入と起動でbosboot -a -dを用い・fileset level と代替ディスク状態を確認する。</li><li>C. 対象資源に対する働きはJFS2でsplitcopyを用い・lff と内部スナップショットを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きは性能管理でtopas -Dを用い・Busy% とtopasディスク表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構成・spliでCの記述「JFS2でsplitcopyを用い、lff」に対応する項目は構成照合 lff（構成・spli）です。構成に関するJFS2の仕様は「JFS2でsplitcopyを用い、lff」で、確認対象はsp・構成です。性能・errpのA:は「SRCとログでerrptを用い、Status」を述べ、対象は性能確認 Status（性能・errp）です。構成・bosbのB:は「導入と起動でbosboot -a -dを用い、fileset」を述べ、対象はfileset level（構成・bosb）です。容量・topaのD:は「性能管理でtopas -Dを用い、Busy%」を述べ、対象は容量確認 Busy%（容量・topa）です。「splitcopy」は「JFS2でsplitcopyを用い、lff」を指し、構成照合 lffではsp・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>splitcopy 構成照合 lff 0811</strong></p><p>検証目的: JFS2のsplitcopy 構成照合 lff 0811について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2構成照合091-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; splitcopy
→ Enter を押す
［画面・出力］
/data/aixdd0811:
        dev             = /dev/fslv91
        vfs             = jfs2
        log             = INLINE
確認コード AIX0811A
画面・出力には AIX0811A が表示され、splitcopy 構成照合 lff 0811 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv91       16.00      9.42   42%     128     1% /data/aixdd0811
確認コード AIX0811B
画面・出力には AIX0811B が表示され、splitcopy 構成照合 lff 0811 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。lff を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0811      --         /data/aixdd0811          jfs2  33554432 rw,log=INLINE
確認コード AIX0811C
画面・出力には AIX0811C が表示され、splitcopy 構成照合 lff 0811 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0811A が画面・出力に表示されること
② ステップ2 の AIX0811B が画面・出力に表示されること
③ ステップ3 の AIX0811C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0097"><h3>splitcopy 運用引継ぎ agblksize 0781</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第七百八十一観点 JFS2 で splitcopy は 運用引継ぎ を点検します（運用第七百八十一）（第七百八十一観点）。第七百八十一観点 確認時には agblksize と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第七百八十一）（第七百八十一観点）。第七百八十一観点 df -g /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第七百八十一観点）。第七百八十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0781へ書きます（第七百八十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> splitcopy 運用引継ぎ agblksize 0781を保守記録に説明する必要があります。errpt 性能確認 チューニング値と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はAIX エラーログから要約または詳細レポートを生成するコマンドである。</li><li>B. 保守作業で参照する機能はネットワークでlsdev -Cc adapterを用い・Media Speed Runningである。</li><li>C. 保守作業で参照する機能はJFS2でsplitcopyを用い・agblksize とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はセキュリティでpwdck -n ALLを用い・authorizations とユーザー属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 運用引・spliでCの記述「JFS2でsplitcopyを用い、agblksize」に対応する項目は運用引継ぎ agblksize（運用・spli）です。運用引に関するJFS2の仕様は「JFS2でsplitcopyを用い、agblksize」で、確認対象はsp・運用引です。性能・チュ・errpのA:は「AIX エラーログから要約または詳細レポートを生成するコマンド」を述べ、対象は性能確認 チューニング値（性能・errp）です。状態・lsdeのB:は「ネットワークでlsdev -Cc adapterを用い、Media」を述べ、対象はSpeed Running（状態・lsde）です。容量・pwdcのD:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は容量確認 authorization（容量・pwdc）です。「splitcopy」は「JFS2でsplitcopyを用い、agblksize」を指し、運用引継ぎ agblksizeではsp・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>splitcopy 運用引継ぎ agblksize 0781</strong></p><p>検証目的: JFS2のsplitcopy 運用引継ぎ agblksize 0781について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2運用引継ぎ061-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; splitcopy
→ Enter を押す
［画面・出力］
/data/aixdd0781:
        dev             = /dev/fslv61
        vfs             = jfs2
        log             = INLINE
確認コード AIX0781A
画面・出力には AIX0781A が表示され、splitcopy 運用引継ぎ agblksize 0781 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; mount | grep /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv61       16.00      9.42   42%     128     1% /data/aixdd0781
確認コード AIX0781B
画面・出力には AIX0781B が表示され、splitcopy 運用引継ぎ agblksize 0781 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。agblksize を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0781      --         /data/aixdd0781          jfs2  33554432 rw,log=INLINE
確認コード AIX0781C
画面・出力には AIX0781C が表示され、splitcopy 運用引継ぎ agblksize 0781 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0781A が画面・出力に表示されること
② ステップ2 の AIX0781B が画面・出力に表示されること
③ ステップ3 の AIX0781C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0098"><h3>splitcopy 運用引継ぎ ファイルシステム使用率 0305</h3><p class="kb-meta">分類: JFS2 ・ 難易度: 中級</p><p>第三百五観点 JFS2 で splitcopy は 運用引継ぎ を点検します（運用第三百五）（第三百五観点）。第三百五観点 確認時には ファイルシステム使用率 と マウントオプション の対応を同じ資料上で追えることを前提にします（資料第三百五）（第三百五観点）。第三百五観点 mount | grep /data/app の出力と取得時刻を同じ確認票に置き、内部スナップショット削除条件の見落とし を避ける判断根拠を説明可能にします（第三百五観点）。第三百五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0305へ書きます（第三百五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「splitcopy 運用引継ぎ ファイルシステム使用率 0305」を「startsrc -s inetd -a &quot;-d&quot; 容量確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はJFS2でsplitcopyを用い・ファイルシステム使用率 とマウントオプションを確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割はSRCとログでstartsrc -s inetd -aを用い・syslog.confである。</li><li>C. 仕様上の役割は性能管理でnmonを用い・dxm とsvmon全体表示を確認する。</li><li>D. 仕様上の役割は構成済みデバイスと VPD を表示するコマンドである。lscfg 障害切り分け ページング状態固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「JFS2でsplitcopyを用い、ファイルシステム使用率」に対応する項目は運用引継ぎ ファイルシステム使用率（運用・spli）です。運用引・ファイに関するJFS2の仕様は「JFS2でsplitcopyを用い、ファイルシステム使用率」で、確認対象はsp・運用引です。容量・starのB:は「SRCとログでstartsrc -s inetd -aを用い」を述べ、対象は容量確認 syslog.conf（容量・star）です。障害切・nmonのC:は「性能管理でnmonを用い、dxm とsvmon全体表示を確認する」を述べ、対象は障害切り分け dxm（障害・nmon）です。障害切・lscfのD:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は障害切り分け ページング状態（障害・lscf）です。「splitcopy」は「JFS2でsplitcopyを用い、ファイルシステム使用率」を指し、運用引継ぎ ファイルシステム使用率ではsp・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>splitcopy 運用引継ぎ ファイルシステム使用率 0305</strong></p><p>検証目的: JFS2のsplitcopy 運用引継ぎ ファイルシステム使用率 0305について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=JFS2運用引継ぎ065-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; splitcopy
→ Enter を押す
［画面・出力］
/data/aixdd0305:
        dev             = /dev/fslv65
        vfs             = jfs2
        log             = INLINE
確認コード AIX0305A
画面・出力には AIX0305A が表示され、splitcopy 運用引継ぎ ファイルシステム使用率 0305 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsfs -q /data/app
→ Enter を押す
［画面・出力］
Filesystem    GB blocks      Free %Used    Iused %Iused Mounted on
/dev/fslv65       16.00      9.42   42%     128     1% /data/aixdd0305
確認コード AIX0305B
画面・出力には AIX0305B が表示され、splitcopy 運用引継ぎ ファイルシステム使用率 0305 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。ファイルシステム使用率 を読むため、JFS2 の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; df -g /data/app
→ Enter を押す
［画面・出力］
Name            Nodename   Mount Pt               VFS   Size    Options
aixdd0305      --         /data/aixdd0305          jfs2  33554432 rw,log=INLINE
確認コード AIX0305C
画面・出力には AIX0305C が表示され、splitcopy 運用引継ぎ ファイルシステム使用率 0305 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0305A が画面・出力に表示されること
② ステップ2 の AIX0305B が画面・出力に表示されること
③ ステップ3 の AIX0305C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


## LVM


<section class="kb-item" id="c01-i0099"><h3>chdev 性能確認 識別値</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第九十九観点 LVM で chdev は 性能確認 を点検します（運用第九十九）（第九十九観点）。第九十九観点 確認時には 識別値 と PVID 欄 の対応を同じ資料上で追えることを前提にします（資料第九十九）（第九十九観点）。第九十九観点 chdev の出力と取得時刻を同じ確認票に置き、停止中の論理ボリューム見落とし を避ける判断根拠を説明可能にします（第九十九観点）。第九十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0099へ書きます（第九十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「chdev 性能確認 識別値」を「lscfg 変更前確認 障害記録」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能は構成済みデバイスと VPD を表示するコマンドである。</li><li>B. 保守作業で参照する機能はSRCとログでerrptを用い・Subsystem とエラーログ一覧を確認する。</li><li>C. 保守作業で参照する機能はデバイス管理でodmget CuDvを用い・microcode level とデバイス一覧を確認する。</li><li>D. 保守作業で参照する機能はデバイス属性を変更する管理コマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「デバイス属性を変更する管理コマンドである」に対応する項目は性能確認 識別値（性能・chde）です。LVMの仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・性能・識別です。変更前・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は変更前確認 障害記録（変更・lscf）です。性能・errpのB:は「SRCとログでerrptを用い、Subsystem」を述べ、対象は性能確認 Subsystem（性能・errp）です。監査・odmgのC:は「デバイス管理でodmget CuDvを用い、microcode」を述べ、対象はmicrocode level（監査・odmg）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、性能確認 識別値ではch・性能・識別に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev 性能確認 識別値</strong></p><p>検証目的: LVMのchdev 性能確認 識別値について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、LVMの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。PVID 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsps -a
→ Enter を押す
［画面・出力］
Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
画面・出力には Page が含まれ、chdev 性能確認 識別値の証跡を確認できます。
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


<section class="kb-item" id="c01-i0100"><h3>chdev 詳細確認 一致条件</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第百観点 LVM で chdev は 詳細確認 を点検します（運用第百）（第百観点）。第百観点 確認時には 一致条件 と PVID 欄 の対応を同じ資料上で追えることを前提にします（資料第百）（第百観点）。第百観点 chdev の出力と取得時刻を同じ確認票に置き、停止中の論理ボリューム見落とし を避ける判断根拠を説明可能にします（第百観点）。第百観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0100へ書きます（第百観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「chdev 詳細確認 一致条件」を「lscfg 状態判定 除外条件」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割は構成済みデバイスと VPD を表示するコマンドである。</li><li>B. 運用時に利用する技術的役割はLVMでchlvを用い・STALE PARTITIONS とボリュームグループ属性を確認する。</li><li>C. 運用時に利用する技術的役割はデバイス属性を変更する管理コマンドである。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割は性能管理でtopas -Dを用い・avm とvmstat表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「デバイス属性を変更する管理コマンドである」に対応する項目は詳細確認 一致条件（詳細・chde）です。LVMの仕様は「デバイス属性を変更する管理コマンド」で、確認対象はch・詳細・一致です。状態・除外・lscfのA:は「構成済みデバイスと VPD を表示するコマンド」を述べ、対象は状態判定 除外条件（状態・lscf）です。バック・chlvのB:は「LVMでchlvを用い、STALE PARTITIONS」を述べ、対象はSTALE PARTITIONS（バッ・chlv）です。変更前・topaのD:は「性能管理でtopas -Dを用い、avm」を述べ、対象は変更前確認 avm（変更・topa）です。「chdev」は「デバイス属性を変更する管理コマンド」を指し、詳細確認 一致条件ではch・詳細・一致に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chdev 詳細確認 一致条件</strong></p><p>検証目的: LVMのchdev 詳細確認 一致条件について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、LVMの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。PVID 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsps -a
→ Enter を押す
［画面・出力］
Page Space      Physical Volume   Volume Group    Size   %Used Active Auto Type
hd6             hdisk0            rootvg          1024MB 1     yes    yes  lv
画面・出力には Page が含まれ、chdev 詳細確認 一致条件の証跡を確認できます。
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


<section class="kb-item" id="c01-i0101"><h3>chlv バックアウト確認 STALE PARTITIONS 0243</h3><p class="kb-meta">分類: LVM ・ 難易度: 初級</p><p>第二百四十三観点 LVM で chlv は バックアウト確認 を点検します（運用第二百四十三）（第二百四十三観点）。第二百四十三観点 確認時には STALE PARTITIONS と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第二百四十三）（第二百四十三観点）。第二百四十三観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第二百四十三観点）。第二百四十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0243へ書きます（第二百四十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chlv バックアウト確認 STALE PARTITIONS 0243について構成や状態を確認します。snap 監査記録 lff 0244ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはJFS2でsnapを用い・lff とログデバイス設定を確認する。</li><li>B. 状態を読み取るための働きはLVMでchlvを用い・STALE PARTITIONS とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはネットワークでentstat -d ent0を用い・Destination とMTU属性を確認する。</li><li>D. 状態を読み取るための働きはデバイスや sys0 などの属性値を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「LVMでchlvを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（バッ・chlv）です。バックに関するLVMの仕様は「LVMでchlvを用い、STALE PARTITIONS」で、確認対象はch・バックです。監査・snapのA:は「JFS2でsnapを用い、lff とログデバイス設定を確認する」を述べ、対象は監査記録 lff（監査・snap）です。構成・entsのC:は「ネットワークでentstat -d ent0を用い」を述べ、対象は構成照合 Destination（構成・ents）です。一覧・対象・lsatのD:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は一覧確認 対象ファイル（一覧・lsat）です。「chlv」は「LVMでchlvを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではch・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chlv バックアウト確認 STALE PARTITIONS 0243</strong></p><p>検証目的: LVMのchlv バックアウト確認 STALE PARTITIONS 0243について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVMバックアウト確認003-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chlv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40243        rootvg          active
hdisk1          00f6a1b2c3d50243        datavg          active
確認コード AIX0243A
画面・出力には AIX0243A が表示され、chlv バックアウト確認 STALE PARTITIONS 0243 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1003
確認コード AIX0243B
画面・出力には AIX0243B が表示され、chlv バックアウト確認 STALE PARTITIONS 0243 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0243C
画面・出力には AIX0243C が表示され、chlv バックアウト確認 STALE PARTITIONS 0243 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0243A が画面・出力に表示されること
② ステップ2 の AIX0243B が画面・出力に表示されること
③ ステップ3 の AIX0243C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0102"><h3>chlv 変更後確認 PP SIZE 0372</h3><p class="kb-meta">分類: LVM ・ 難易度: 初級</p><p>第三百七十二観点 LVM で chlv は 変更後確認 を点検します（運用第三百七十二）（第三百七十二観点）。第三百七十二観点 確認時には PP SIZE と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第三百七十二）（第三百七十二観点）。第三百七十二観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第三百七十二観点）。第三百七十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0372へ書きます（第三百七十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chlv 変更後確認 PP SIZE 0372の技術的な意味を資料で確認するとき、snap 障害切り分け lff 0373との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はJFS2でsnapを用い・lff とマウントオプションを確認する。</li><li>B. 構成を確認する際の意味はネットワークでentstat -d ent0を用い・MTU とアダプター一覧を確認する。</li><li>C. 構成を確認する際の意味は導入と起動でalt_disk_mksysbを用い・bootlist と起動デバイス設定を確認する。</li><li>D. 構成を確認する際の意味はLVMでchlvを用い・PP SIZE と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認する」に対応する項目はPP SIZE（変更・chlv）です。変更後に関するLVMの仕様は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」で、確認対象はch・変更後です。障害切・snapのA:は「JFS2でsnapを用い、lff とマウントオプションを確認する」を述べ、対象は障害切り分け lff（障害・snap）です。属性・entsのB:は「ネットワークでentstat -d ent0を用い、MTU」を述べ、対象は属性確認 MTU（属性・ents）です。バック・alt_のC:は「導入と起動でalt_disk_mksysbを用い、bootlist」を述べ、対象はバックアウト確認 bootlist（バッ・alt_）です。「chlv」は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」を指し、PP SIZEではch・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chlv 変更後確認 PP SIZE 0372</strong></p><p>検証目的: LVMのchlv 変更後確認 PP SIZE 0372について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM変更後確認012-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chlv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40372        rootvg          active
hdisk1          00f6a1b2c3d50372        datavg          active
確認コード AIX0372A
画面・出力には AIX0372A が表示され、chlv 変更後確認 PP SIZE 0372 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1012
確認コード AIX0372B
画面・出力には AIX0372B が表示され、chlv 変更後確認 PP SIZE 0372 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0372C
画面・出力には AIX0372C が表示され、chlv 変更後確認 PP SIZE 0372 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0372A が画面・出力に表示されること
② ステップ2 の AIX0372B が画面・出力に表示されること
③ ステップ3 の AIX0372C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0103"><h3>chlv 変更後確認 PP SIZE 0432</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第四百三十二観点 LVM で chlv は 変更後確認 を点検します（運用第四百三十二）（第四百三十二観点）。第四百三十二観点 確認時には PP SIZE と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第四百三十二）（第四百三十二観点）。第四百三十二観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第四百三十二観点）。第四百三十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0432へ書きます（第四百三十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chlv 変更後確認 PP SIZE 0432を同一分類のsnap 障害切り分け lff 0433と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はLVMでchlvを用い・PP SIZE と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はJFS2でsnapを用い・lff とマウントオプションを確認する。</li><li>C. 構成を確認する際の意味はネットワークでnetstat -rnを用い・Destination とアダプター一覧を確認する。</li><li>D. 構成を確認する際の意味は導入と起動でmksysbを用い・altinst_rootvg と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認する」に対応する項目はPP SIZE（変更・chlv）です。変更後に関するLVMの仕様は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」で、確認対象はch・変更後です。障害切・snapのB:は「JFS2でsnapを用い、lff とマウントオプションを確認する」を述べ、対象は障害切り分け lff（障害・snap）です。状態・netsのC:は「ネットワークでnetstat -rnを用い、Destination」を述べ、対象は状態確認 Destination（状態・nets）です。監査・mksyのD:は「導入と起動でmksysbを用い、altinst_rootvg」を述べ、対象は監査記録 altinst_rootv（監査・mksy）です。「chlv」は「LVMでchlvを用い、PP SIZE と論理ボリューム配置を確認す」を指し、PP SIZEではch・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chlv 変更後確認 PP SIZE 0432</strong></p><p>検証目的: LVMのchlv 変更後確認 PP SIZE 0432について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM変更後確認072-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chlv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40432        rootvg          active
hdisk1          00f6a1b2c3d50432        datavg          active
確認コード AIX0432A
画面・出力には AIX0432A が表示され、chlv 変更後確認 PP SIZE 0432 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1072
確認コード AIX0432B
画面・出力には AIX0432B が表示され、chlv 変更後確認 PP SIZE 0432 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0432C
画面・出力には AIX0432C が表示され、chlv 変更後確認 PP SIZE 0432 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0432A が画面・出力に表示されること
② ステップ2 の AIX0432B が画面・出力に表示されること
③ ステップ3 の AIX0432C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0104"><h3>chlv 属性確認 PP SIZE 0749</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第七百四十九観点 LVM で chlv は 属性確認 を点検します（運用第七百四十九）（第七百四十九観点）。第七百四十九観点 確認時には PP SIZE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第七百四十九）（第七百四十九観点）。第七百四十九観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第七百四十九観点）。第七百四十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0749へ書きます（第七百四十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chlv 属性確認 PP SIZE 0749を保守記録に説明する必要があります。snap 状態確認 mountguard 0750と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はJFS2でsnapを用い・mountguard とファイルシステム属性を確認する。</li><li>B. 仕様上の役割は性能管理でnmonを用い・Busy% とsvmon全体表示を確認する。</li><li>C. 仕様上の役割はLVMでchlvを用い・PP SIZE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 仕様上の役割はSRCとログでerrptを用い・Status とSRCサブシステム表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」に対応する項目はPP SIZE（属性・chlv）です。属性に関するLVMの仕様は「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」で、確認対象はch・属性です。状態・snapのA:は「JFS2でsnapを用い、mountguard」を述べ、対象は状態確認 mountguard（状態・snap）です。障害切・nmonのB:は「性能管理でnmonを用い、Busy% とsvmon全体表示を確認する」を述べ、対象は障害切り分け Busy%（障害・nmon）です。構成・errpのD:は「SRCとログでerrptを用い、Status」を述べ、対象は構成照合 Status（構成・errp）です。「chlv」は「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」を指し、PP SIZEではch・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chlv 属性確認 PP SIZE 0749</strong></p><p>検証目的: LVMのchlv 属性確認 PP SIZE 0749について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM属性確認029-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chlv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40749        rootvg          active
hdisk1          00f6a1b2c3d50749        datavg          active
確認コード AIX0749A
画面・出力には AIX0749A が表示され、chlv 属性確認 PP SIZE 0749 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1029
確認コード AIX0749B
画面・出力には AIX0749B が表示され、chlv 属性確認 PP SIZE 0749 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0749C
画面・出力には AIX0749C が表示され、chlv 属性確認 PP SIZE 0749 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0749A が画面・出力に表示されること
② ステップ2 の AIX0749B が画面・出力に表示されること
③ ステップ3 の AIX0749C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0105"><h3>chlv 属性確認 VG STATE 0273</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第二百七十三観点 LVM で chlv は 属性確認 を点検します（運用第二百七十三）（第二百七十三観点）。第二百七十三観点 確認時には VG STATE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第二百七十三）（第二百七十三観点）。第二百七十三観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第二百七十三観点）。第二百七十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0273へ書きます（第二百七十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「chlv 属性確認 VG STATE 0273」を「snap 状態確認 agblksize 0274」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はJFS2でsnapを用い・agblksize とファイルシステム属性を確認する。</li><li>B. 運用時に利用する技術的役割はネットワークでentstat -d ent0を用い・Link Status とEthernet統計を確認する。</li><li>C. 運用時に利用する技術的役割はLVMでchlvを用い・VG STATE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はデバイスや sys0 などの属性値を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「LVMでchlvを用い、VG STATE とミラーコピー状態を確認する」に対応する項目はVG STATE（属性・chlv）です。属性に関するLVMの仕様は「LVMでchlvを用い、VG STATE」で、確認対象はch・属性です。状態・snapのA:は「JFS2でsnapを用い、agblksize」を述べ、対象は状態確認 agblksize（状態・snap）です。運用引・entsのB:は「ネットワークでentstat -d ent0を用い、Link」を述べ、対象はLink Status（運用・ents）です。詳細・確認・lsatのD:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は詳細確認 確認範囲（詳細・lsat）です。「chlv」は「LVMでchlvを用い、VG STATE」を指し、VG STATEではch・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chlv 属性確認 VG STATE 0273</strong></p><p>検証目的: LVMのchlv 属性確認 VG STATE 0273について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM属性確認033-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chlv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40273        rootvg          active
hdisk1          00f6a1b2c3d50273        datavg          active
確認コード AIX0273A
画面・出力には AIX0273A が表示され、chlv 属性確認 VG STATE 0273 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1033
確認コード AIX0273B
画面・出力には AIX0273B が表示され、chlv 属性確認 VG STATE 0273 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0273C
画面・出力には AIX0273C が表示され、chlv 属性確認 VG STATE 0273 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0273A が画面・出力に表示されること
② ステップ2 の AIX0273B が画面・出力に表示されること
③ ステップ3 の AIX0273C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0106"><h3>chlv 性能確認 PVID 0402</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第四百二観点 LVM で chlv は 性能確認 を点検します（運用第四百二）（第四百二観点）。第四百二観点 確認時には PVID と 物理ボリューム一覧 の対応を同じ資料上で追えることを前提にします（資料第四百二）（第四百二観点）。第四百二観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、stale区画の見落とし を避ける判断根拠を説明可能にします（第四百二観点）。第四百二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0402へ書きます（第四百二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chlv 性能確認 PVID 0402の役割を調べています。snap 起動確認 agblksize 0403の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはJFS2でsnapを用い・agblksize と内部スナップショットを確認する。</li><li>B. 機能の説明としてはネットワークでentstat -d ent0を用い・EtherChannel と経路表を確認する。</li><li>C. 機能の説明としてはLVMでchlvを用い・PVID と物理ボリューム一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としては導入と起動でalt_disk_mksysbを用い・Technology Levelである。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」に対応する項目は性能確認 PVID（性能・chlv）です。性能に関するLVMの仕様は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」で、確認対象はch・性能です。起動・snapのA:は「JFS2でsnapを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・snap）です。バック・entsのB:は「ネットワークでentstat -d ent0を用い」を述べ、対象はバックアウト確認 EtherChan（バッ・ents）です。属性・alt_のD:は「導入と起動でalt_disk_mksysbを用い」を述べ、対象はTechnology Level（属性・alt_）です。「chlv」は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」を指し、性能確認 PVIDではch・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chlv 性能確認 PVID 0402</strong></p><p>検証目的: LVMのchlv 性能確認 PVID 0402について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM性能確認042-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chlv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40402        rootvg          active
hdisk1          00f6a1b2c3d50402        datavg          active
確認コード AIX0402A
画面・出力には AIX0402A が表示され、chlv 性能確認 PVID 0402 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1042
確認コード AIX0402B
画面・出力には AIX0402B が表示され、chlv 性能確認 PVID 0402 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0402C
画面・出力には AIX0402C が表示され、chlv 性能確認 PVID 0402 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0402A が画面・出力に表示されること
② ステップ2 の AIX0402B が画面・出力に表示されること
③ ステップ3 の AIX0402C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0107"><h3>chlv 性能確認 PVID 0462</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第四百六十二観点 LVM で chlv は 性能確認 を点検します（運用第四百六十二）（第四百六十二観点）。第四百六十二観点 確認時には PVID と 物理ボリューム一覧 の対応を同じ資料上で追えることを前提にします（資料第四百六十二）（第四百六十二観点）。第四百六十二観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、stale区画の見落とし を避ける判断根拠を説明可能にします（第四百六十二観点）。第四百六十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0462へ書きます（第四百六十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chlv 性能確認 PVID 0462に関する障害切り分けの前提を確認しています。snap 起動確認 agblksize 0463の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはLVMでchlvを用い・PVID と物理ボリューム一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 機能の説明としてはJFS2でsnapを用い・agblksize と内部スナップショットを確認する。</li><li>C. 機能の説明としてはネットワークでnetstat -rnを用い・Link Status と経路表を確認する。</li><li>D. 機能の説明としては導入と起動でmksysbを用い・fileset level とfileset一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」に対応する項目は性能確認 PVID（性能・chlv）です。性能に関するLVMの仕様は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」で、確認対象はch・性能です。起動・snapのB:は「JFS2でsnapを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・snap）です。監査・netsのC:は「ネットワークでnetstat -rnを用い、Link Status」を述べ、対象はLink Status（監査・nets）です。状態・mksyのD:は「導入と起動でmksysbを用い、fileset level」を述べ、対象はfileset level（状態・mksy）です。「chlv」は「LVMでchlvを用い、PVID と物理ボリューム一覧を確認する」を指し、性能確認 PVIDではch・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chlv 性能確認 PVID 0462</strong></p><p>検証目的: LVMのchlv 性能確認 PVID 0462について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM性能確認102-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chlv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40462        rootvg          active
hdisk1          00f6a1b2c3d50462        datavg          active
確認コード AIX0462A
画面・出力には AIX0462A が表示され、chlv 性能確認 PVID 0462 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1102
確認コード AIX0462B
画面・出力には AIX0462B が表示され、chlv 性能確認 PVID 0462 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0462C
画面・出力には AIX0462C が表示され、chlv 性能確認 PVID 0462 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0462A が画面・出力に表示されること
② ステップ2 の AIX0462B が画面・出力に表示されること
③ ステップ3 の AIX0462C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0108"><h3>chlv 構成照合 PP SIZE 0561</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第五百六十一観点 LVM で chlv は 構成照合 を点検します（運用第五百六十一）（第五百六十一観点）。第五百六十一観点 確認時には PP SIZE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第五百六十一）（第五百六十一観点）。第五百六十一観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第五百六十一観点）。第五百六十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0561へ書きます（第五百六十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「chlv 構成照合 PP SIZE 0561」を「errpt -a 変更前確認 IDENTIFIER 0562」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はSRCとログでerrpt -aを用い・IDENTIFIER とSRCサブシステム表示を確認する。</li><li>B. 運用時に利用する技術的役割はデバイス属性を変更する管理コマンドである。</li><li>C. 運用時に利用する技術的役割は導入と起動でmksysbを用い・bootlist とOSレベル表示を確認する。</li><li>D. 運用時に利用する技術的役割はLVMでchlvを用い・PP SIZE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」に対応する項目はPP SIZE（構成・chlv）です。構成に関するLVMの仕様は「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」で、確認対象はch・構成です。変更前・errpのA:は「SRCとログでerrpt -aを用い、IDENTIFIER」を述べ、対象は変更前確認 IDENTIFIER（変更・errp）です。障害切・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は障害切り分け ボリューム状態（障害・chde）です。障害切・mksyのC:は「導入と起動でmksysbを用い、bootlist」を述べ、対象は障害切り分け bootlist（障害・mksy）です。「chlv」は「LVMでchlvを用い、PP SIZE とミラーコピー状態を確認する」を指し、PP SIZEではch・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chlv 構成照合 PP SIZE 0561</strong></p><p>検証目的: LVMのchlv 構成照合 PP SIZE 0561について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM構成照合081-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chlv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40561        rootvg          active
hdisk1          00f6a1b2c3d50561        datavg          active
確認コード AIX0561A
画面・出力には AIX0561A が表示され、chlv 構成照合 PP SIZE 0561 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1081
確認コード AIX0561B
画面・出力には AIX0561B が表示され、chlv 構成照合 PP SIZE 0561 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0561C
画面・出力には AIX0561C が表示され、chlv 構成照合 PP SIZE 0561 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0561A が画面・出力に表示されること
② ステップ2 の AIX0561B が画面・出力に表示されること
③ ステップ3 の AIX0561C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0109"><h3>chlv 構成照合 VG STATE 0085</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第八十五観点 LVM で chlv は 構成照合 を点検します（運用第八十五）（第八十五観点）。第八十五観点 確認時には VG STATE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第八十五）（第八十五観点）。第八十五観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第八十五観点）。第八十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0085へ書きます（第八十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chlv 構成照合 VG STATE 0085を保守記録に説明する必要があります。errpt -a 変更前確認 PID 0086と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はSRCとログでerrpt -aを用い・PID とSRCサブシステム表示を確認する。</li><li>B. 保守作業で参照する機能はネットワークでnetstat -rnを用い・Media Speed Runningである。</li><li>C. 保守作業で参照する機能はLVMでchlvを用い・VG STATE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能はSRCとログでsyslog_ssw -cを用い・Subsystem とSRCサブシステム表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「LVMでchlvを用い、VG STATE とミラーコピー状態を確認する」に対応する項目はVG STATE（構成・chlv）です。構成に関するLVMの仕様は「LVMでchlvを用い、VG STATE」で、確認対象はch・構成です。変更前・errpのA:は「SRCとログでerrpt -aを用い、PID」を述べ、対象は変更前確認 PID（変更・errp）です。起動・netsのB:は「ネットワークでnetstat -rnを用い、Media Speed」を述べ、対象はSpeed Running（起動・nets）です。運用引・syslのD:は「SRCとログでsyslog_ssw -cを用い、Subsystem」を述べ、対象は運用引継ぎ Subsystem（運用・sysl）です。「chlv」は「LVMでchlvを用い、VG STATE」を指し、VG STATEではch・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chlv 構成照合 VG STATE 0085</strong></p><p>検証目的: LVMのchlv 構成照合 VG STATE 0085について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM構成照合085-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chlv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40085        rootvg          active
hdisk1          00f6a1b2c3d50085        datavg          active
確認コード AIX0085A
画面・出力には AIX0085A が表示され、chlv 構成照合 VG STATE 0085 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1085
確認コード AIX0085B
画面・出力には AIX0085B が表示され、chlv 構成照合 VG STATE 0085 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0085C
画面・出力には AIX0085C が表示され、chlv 構成照合 VG STATE 0085 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0085A が画面・出力に表示されること
② ステップ2 の AIX0085B が画面・出力に表示されること
③ ステップ3 の AIX0085C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0110"><h3>chlv 運用引継ぎ PVID 0591</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第五百九十一観点 LVM で chlv は 運用引継ぎ を点検します（運用第五百九十一）（第五百九十一観点）。第五百九十一観点 確認時には PVID と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第五百九十一）（第五百九十一観点）。第五百九十一観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第五百九十一観点）。第五百九十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0591へ書きます（第五百九十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chlv 運用引継ぎ PVID 0591の設定や表示を読む前に役割を確認します。snap 容量確認 log=INLINE 0592ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはJFS2でsnapを用い・log=INLINE とログデバイス設定を確認する。</li><li>B. 状態を読み取るための働きはデバイス属性を変更する管理コマンドである。</li><li>C. 状態を読み取るための働きはLVMでchlvを用い・PVID とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 状態を読み取るための働きは導入と起動でmksysbを用い・Technology Level と代替ディスク状態を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「LVMでchlvを用い、PVID とボリュームグループ属性を確認する」に対応する項目は運用引継ぎ PVID（運用・chlv）です。運用引に関するLVMの仕様は「LVMでchlvを用い、PVID とボリュームグループ属性を確認する」で、確認対象はch・運用引です。容量・snapのA:は「JFS2でsnapを用い、log=INLINE」を述べ、対象は容量確認 log=INLINE（容量・snap）です。性能・識別・chdeのB:は「デバイス属性を変更する管理コマンド」を述べ、対象は性能確認 識別値（性能・chde）です。起動・mksyのD:は「導入と起動でmksysbを用い、Technology Level」を述べ、対象はTechnology Level（起動・mksy）です。「chlv」は「LVMでchlvを用い、PVID とボリュームグループ属性を確認する」を指し、運用引継ぎ PVIDではch・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chlv 運用引継ぎ PVID 0591</strong></p><p>検証目的: LVMのchlv 運用引継ぎ PVID 0591について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM運用引継ぎ111-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chlv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40591        rootvg          active
hdisk1          00f6a1b2c3d50591        datavg          active
確認コード AIX0591A
画面・出力には AIX0591A が表示され、chlv 運用引継ぎ PVID 0591 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1111
確認コード AIX0591B
画面・出力には AIX0591B が表示され、chlv 運用引継ぎ PVID 0591 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0591C
画面・出力には AIX0591C が表示され、chlv 運用引継ぎ PVID 0591 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0591A が画面・出力に表示されること
② ステップ2 の AIX0591B が画面・出力に表示されること
③ ステップ3 の AIX0591C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0111"><h3>chlv 運用引継ぎ STALE PARTITIONS 0115</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第百十五観点 LVM で chlv は 運用引継ぎ を点検します（運用第百十五）（第百十五観点）。第百十五観点 確認時には STALE PARTITIONS と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第百十五）（第百十五観点）。第百十五観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第百十五観点）。第百十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0115へ書きます（第百十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chlv 運用引継ぎ STALE PARTITIONS 0115について構成や状態を確認します。snap 容量確認 lff 0116ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはJFS2でsnapを用い・lff とログデバイス設定を確認する。snap 容量確認 lff 0116固有の属性も確認対象に含める。</li><li>B. 対象資源に対する働きはLVMでchlvを用い・STALE PARTITIONS とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 対象資源に対する働きはネットワークでnetstat -rnを用い・Gateway とMTU属性を確認する。</li><li>D. 対象資源に対する働きはJFS2でfsckを用い・lff とログデバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「LVMでchlvを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（運用・chlv）です。運用引に関するLVMの仕様は「LVMでchlvを用い、STALE PARTITIONS」で、確認対象はch・運用引です。容量・snapのA:は「JFS2でsnapを用い、lff とログデバイス設定を確認する」を述べ、対象は容量確認 lff（容量・snap）です。障害切・netsのC:は「ネットワークでnetstat -rnを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・nets）です。変更前・fsckのD:は「JFS2でfsckを用い、lff とログデバイス設定を確認する」を述べ、対象は変更前確認 lff（変更・fsck）です。「chlv」は「LVMでchlvを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではch・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chlv 運用引継ぎ STALE PARTITIONS 0115</strong></p><p>検証目的: LVMのchlv 運用引継ぎ STALE PARTITIONS 0115について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM運用引継ぎ115-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chlv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40115        rootvg          active
hdisk1          00f6a1b2c3d50115        datavg          active
確認コード AIX0115A
画面・出力には AIX0115A が表示され、chlv 運用引継ぎ STALE PARTITIONS 0115 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1115
確認コード AIX0115B
画面・出力には AIX0115B が表示され、chlv 運用引継ぎ STALE PARTITIONS 0115 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0115C
画面・出力には AIX0115C が表示され、chlv 運用引継ぎ STALE PARTITIONS 0115 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0115A が画面・出力に表示されること
② ステップ2 の AIX0115B が画面・出力に表示されること
③ ステップ3 の AIX0115C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0112"><h3>chvg 変更後確認 LV STATE 0039</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第三十九観点 LVM で chvg は 変更後確認 を点検します（運用第三十九）（第三十九観点）。第三十九観点 確認時には LV STATE と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第三十九）（第三十九観点）。第三十九観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第三十九観点）。第三十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0039へ書きます（第三十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chvg 変更後確認 LV STATE 0039の設定や表示を読む前に役割を確認します。crfs 障害切り分け isnapshot 0040ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはJFS2でcrfsを用い・isnapshot とログデバイス設定を確認する。</li><li>B. 状態を読み取るための働きはネットワークでno -aを用い・Media Speed Running とMTU属性を確認する。</li><li>C. 状態を読み取るための働きはJFS2でsplitcopyを用い・agblksize とログデバイス設定を確認する。</li><li>D. 状態を読み取るための働きはLVMでchvgを用い・LV STATE とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「LVMでchvgを用い、LV STATE とボリュームグループ属性を確認する」に対応する項目はLV STATE（変更・chvg）です。LVMの仕様は「LVMでchvgを用い、LV STATE とボリュームグループ属性を確認」で、確認対象はch・変更後です。障害切・crfsのA:は「JFS2でcrfsを用い、isnapshot」を述べ、対象は障害切り分け isnapshot（障害・crfs）です。属性・noのB:は「ネットワークでno -aを用い、Media Speed」を述べ、対象はSpeed Running（属性・no）です。性能・spliのC:は「JFS2でsplitcopyを用い、agblksize」を述べ、対象は性能確認 agblksize（性能・spli）です。「chvg」は「LVMでchvgを用い、LV STATE」を指し、LV STATEではch・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 変更後確認 LV STATE 0039</strong></p><p>検証目的: LVMのchvg 変更後確認 LV STATE 0039について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM変更後確認039-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40039        rootvg          active
hdisk1          00f6a1b2c3d50039        datavg          active
確認コード AIX0039A
画面・出力には AIX0039A が表示され、chvg 変更後確認 LV STATE 0039 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1039
確認コード AIX0039B
画面・出力には AIX0039B が表示され、chvg 変更後確認 LV STATE 0039 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0039C
画面・出力には AIX0039C が表示され、chvg 変更後確認 LV STATE 0039 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0039A が画面・出力に表示されること
② ステップ2 の AIX0039B が画面・出力に表示されること
③ ステップ3 の AIX0039C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0113"><h3>chvg 変更後確認 STALE PARTITIONS 0515</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第五百十五観点 LVM で chvg は 変更後確認 を点検します（運用第五百十五）（第五百十五観点）。第五百十五観点 確認時には STALE PARTITIONS と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第五百十五）（第五百十五観点）。第五百十五観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第五百十五観点）。第五百十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0515へ書きます（第五百十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chvg 変更後確認 STALE PARTITIONS 0515について構成や状態を確認します。crfs 障害切り分け lff 0516ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はJFS2でcrfsを用い・lff とログデバイス設定を確認する。</li><li>B. 一次資料が示す主目的はLVMでchvgを用い・STALE PARTITIONS とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 一次資料が示す主目的はネットワークでno -aを用い・Destination とMTU属性を確認する。</li><li>D. 一次資料が示す主目的は導入と起動でnimadmを用い・bootlist と代替ディスク状態を確認する。nimadm バックアウト確認 bootlist 0208固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LVMでchvgを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（変更・chvg）です。変更後に関するLVMの仕様は「LVMでchvgを用い、STALE PARTITIONS」で、確認対象はch・変更後です。障害切・crfsのA:は「JFS2でcrfsを用い、lff とログデバイス設定を確認する」を述べ、対象は障害切り分け lff（障害・crfs）です。属性・noのC:は「ネットワークでno -aを用い、Destination」を述べ、対象は属性確認 Destination（属性・no）です。バック・nimaのD:は「導入と起動でnimadmを用い、bootlist」を述べ、対象はバックアウト確認 bootlist（バッ・nima）です。「chvg」は「LVMでchvgを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではch・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 変更後確認 STALE PARTITIONS 0515</strong></p><p>検証目的: LVMのchvg 変更後確認 STALE PARTITIONS 0515について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM変更後確認035-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40515        rootvg          active
hdisk1          00f6a1b2c3d50515        datavg          active
確認コード AIX0515A
画面・出力には AIX0515A が表示され、chvg 変更後確認 STALE PARTITIONS 0515 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1035
確認コード AIX0515B
画面・出力には AIX0515B が表示され、chvg 変更後確認 STALE PARTITIONS 0515 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0515C
画面・出力には AIX0515C が表示され、chvg 変更後確認 STALE PARTITIONS 0515 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0515A が画面・出力に表示されること
② ステップ2 の AIX0515B が画面・出力に表示されること
③ ステップ3 の AIX0515C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0114"><h3>chvg 属性確認 PP SIZE 0833</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第八百三十三観点 LVM で chvg は 属性確認 を点検します（運用第八百三十三）（第八百三十三観点）。第八百三十三観点 確認時には PP SIZE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第八百三十三）（第八百三十三観点）。第八百三十三観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第八百三十三観点）。第八百三十三観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0833へ書きます（第八百三十三観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「chvg 属性確認 PP SIZE 0833」を「lsvg 詳細確認 詳細表示」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>B. 仕様上の役割は導入と起動でinstallp -Cを用い・bootlist とfileset一覧を確認する。</li><li>C. 仕様上の役割はLVMでchvgを用い・PP SIZE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 仕様上の役割は性能管理でvmo -aを用い・pi とsvmon全体表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 属性・chvgでCの記述「LVMでchvgを用い、PP SIZE とミラーコピー状態を確認する」に対応する項目はPP SIZE（属性・chvg）です。属性に関するLVMの仕様は「LVMでchvgを用い、PP SIZE とミラーコピー状態を確認する」で、確認対象はch・属性です。詳細・詳細・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は詳細確認 詳細表示（詳細・lsvg）です。障害切・instのB:は「導入と起動でinstallp -Cを用い、bootlist」を述べ、対象は障害切り分け bootlist（障害・inst）です。属性・vmoのD:は「性能管理でvmo -aを用い、pi とsvmon全体表示を確認する」を述べ、対象は属性確認 pi（属性・vmo）です。「chvg」は「LVMでchvgを用い、PP SIZE とミラーコピー状態を確認する」を指し、PP SIZEではch・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 属性確認 PP SIZE 0833</strong></p><p>検証目的: LVMのchvg 属性確認 PP SIZE 0833について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM属性確認113-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40833        rootvg          active
hdisk1          00f6a1b2c3d50833        datavg          active
確認コード AIX0833A
画面・出力には AIX0833A が表示され、chvg 属性確認 PP SIZE 0833 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1113
確認コード AIX0833B
画面・出力には AIX0833B が表示され、chvg 属性確認 PP SIZE 0833 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0833C
画面・出力には AIX0833C が表示され、chvg 属性確認 PP SIZE 0833 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0833A が画面・出力に表示されること
② ステップ2 の AIX0833B が画面・出力に表示されること
③ ステップ3 の AIX0833C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0115"><h3>chvg 属性確認 VG STATE 0357</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第三百五十七観点 LVM で chvg は 属性確認 を点検します（運用第三百五十七）（第三百五十七観点）。第三百五十七観点 確認時には VG STATE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第三百五十七）（第三百五十七観点）。第三百五十七観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第三百五十七観点）。第三百五十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0357へ書きます（第三百五十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chvg 属性確認 VG STATE 0357を保守記録に説明する必要があります。lssrc -s syslogd 状態確認 PID 0358と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はSRCとログでlssrc -s syslogdを用い・PID とSRCサブシステム表示を確認する。</li><li>B. 運用時に利用する技術的役割はネットワークでroute -n getを用い・Media Speed Runningである。</li><li>C. 運用時に利用する技術的役割は導入と起動でoslevel -sを用い・fileset level とOSレベル表示を確認する。</li><li>D. 運用時に利用する技術的役割はLVMでchvgを用い・VG STATE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「LVMでchvgを用い、VG STATE とミラーコピー状態を確認する」に対応する項目はVG STATE（属性・chvg）です。属性に関するLVMの仕様は「LVMでchvgを用い、VG STATE」で、確認対象はch・属性です。状態・lssrのA:は「SRCとログでlssrc -s syslogdを用い、PID」を述べ、対象は状態確認 PID（状態・lssr）です。容量・routのB:は「ネットワークでroute -n getを用い、Media」を述べ、対象はSpeed Running（容量・rout）です。変更前・osleのC:は「導入と起動でoslevel -sを用い、fileset level」を述べ、対象はfileset level（変更・osle）です。「chvg」は「LVMでchvgを用い、VG STATE」を指し、VG STATEではch・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 属性確認 VG STATE 0357</strong></p><p>検証目的: LVMのchvg 属性確認 VG STATE 0357について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM属性確認117-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40357        rootvg          active
hdisk1          00f6a1b2c3d50357        datavg          active
確認コード AIX0357A
画面・出力には AIX0357A が表示され、chvg 属性確認 VG STATE 0357 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1117
確認コード AIX0357B
画面・出力には AIX0357B が表示され、chvg 属性確認 VG STATE 0357 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0357C
画面・出力には AIX0357C が表示され、chvg 属性確認 VG STATE 0357 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0357A が画面・出力に表示されること
② ステップ2 の AIX0357B が画面・出力に表示されること
③ ステップ3 の AIX0357C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0116"><h3>chvg 性能確認 MIRROR WRITE CONSISTENCY 0009</h3><p class="kb-meta">分類: LVM ・ 難易度: 初級</p><p>第九観点 LVM で chvg は 性能確認 を点検します（運用第九）（第九観点）。第九観点 確認時には MIRROR WRITE CONSISTENCY と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第九）（第九観点）。第九観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第九観点）。第九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0009へ書きます（第九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「chvg 性能確認 MIRROR WRITE CONSISTENCY 0009」を「crfs 起動確認 ファイルシステム使用率 0010」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はJFS2でcrfsを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li><li>B. 運用時に利用する技術的役割はLVMでchvgを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はネットワークでno -aを用い・Gateway とEthernet統計を確認する。no -a バックアウト確認 Gateway 0315固有の属性も確認対象に含める。</li><li>D. 運用時に利用する技術的役割はJFS2でsplitcopyを用い・lff とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「LVMでchvgを用い、MIRROR WRITE CONSISTENCY」に対応する項目はWRITE CONSISTENCY（性能・chvg）です。LVMの仕様は「LVMでchvgを用い、MIRROR WRITE」で、確認対象はch・性能です。起動・ファ・crfsのA:は「JFS2でcrfsを用い、ファイルシステム使用率」を述べ、対象は起動確認 ファイルシステム使用率（起動・crfs）です。バック・noのC:は「ネットワークでno -aを用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・no）です。変更後・spliのD:は「JFS2でsplitcopyを用い、lff」を述べ、対象は変更後確認 lff（変更・spli）です。「chvg」は「LVMでchvgを用い、MIRROR WRITE」を指し、WRITE CONSISTENCYではch・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 性能確認 MIRROR WRITE CONSISTENCY 0009</strong></p><p>検証目的: LVMのchvg 性能確認 MIRROR WRITE CONSISTENCY 0009について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM性能確認009-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40009        rootvg          active
hdisk1          00f6a1b2c3d50009        datavg          active
確認コード AIX0009A
画面・出力には AIX0009A が表示され、chvg 性能確認 MIRROR WRITE CONSISTENCY 0009 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1009
確認コード AIX0009B
画面・出力には AIX0009B が表示され、chvg 性能確認 MIRROR WRITE CONSISTENCY 0009 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0009C
画面・出力には AIX0009C が表示され、chvg 性能確認 MIRROR WRITE CONSISTENCY 0009 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0009A が画面・出力に表示されること
② ステップ2 の AIX0009B が画面・出力に表示されること
③ ステップ3 の AIX0009C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0117"><h3>chvg 性能確認 MIRROR WRITE CONSISTENCY 0069</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第六十九観点 LVM で chvg は 性能確認 を点検します（運用第六十九）（第六十九観点）。第六十九観点 確認時には MIRROR WRITE CONSISTENCY と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第六十九）（第六十九観点）。第六十九観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第六十九観点）。第六十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0069へ書きます（第六十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chvg 性能確認 MIRROR WRITE CONSISTENCY 0069を保守記録に説明する必要があります。crfs 起動確認 ファイルシステム使用率 0070と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はJFS2でcrfsを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li><li>B. 運用時に利用する技術的役割はネットワークでroute -n getを用い・EtherChannel とEthernet統計を確認する。</li><li>C. 運用時に利用する技術的役割はLVMでchvgを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 運用時に利用する技術的役割はJFS2でsplitcopyを用い・lff とファイルシステム属性を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「LVMでchvgを用い、MIRROR WRITE CONSISTENCY」に対応する項目はWRITE CONSISTENCY（性能・chvg）です。LVMの仕様は「LVMでchvgを用い、MIRROR WRITE」で、確認対象はch・性能です。起動・ファ・crfsのA:は「JFS2でcrfsを用い、ファイルシステム使用率」を述べ、対象は起動確認 ファイルシステム使用率（起動・crfs）です。監査・routのB:は「ネットワークでroute -n getを用い」を述べ、対象は監査記録 EtherChannel（監査・rout）です。変更後・spliのD:は「JFS2でsplitcopyを用い、lff」を述べ、対象は変更後確認 lff（変更・spli）です。「chvg」は「LVMでchvgを用い、MIRROR WRITE」を指し、WRITE CONSISTENCYではch・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 性能確認 MIRROR WRITE CONSISTENCY 0069</strong></p><p>検証目的: LVMのchvg 性能確認 MIRROR WRITE CONSISTENCY 0069について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM性能確認069-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40069        rootvg          active
hdisk1          00f6a1b2c3d50069        datavg          active
確認コード AIX0069A
画面・出力には AIX0069A が表示され、chvg 性能確認 MIRROR WRITE CONSISTENCY 0069 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1069
確認コード AIX0069B
画面・出力には AIX0069B が表示され、chvg 性能確認 MIRROR WRITE CONSISTENCY 0069 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0069C
画面・出力には AIX0069C が表示され、chvg 性能確認 MIRROR WRITE CONSISTENCY 0069 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0069A が画面・出力に表示されること
② ステップ2 の AIX0069B が画面・出力に表示されること
③ ステップ3 の AIX0069C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0118"><h3>chvg 性能確認 VG STATE 0485</h3><p class="kb-meta">分類: LVM ・ 難易度: 初級</p><p>第四百八十五観点 LVM で chvg は 性能確認 を点検します（運用第四百八十五）（第四百八十五観点）。第四百八十五観点 確認時には VG STATE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第四百八十五）（第四百八十五観点）。第四百八十五観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第四百八十五観点）。第四百八十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0485へ書きます（第四百八十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chvg 性能確認 VG STATE 0485を保守記録に説明する必要があります。crfs 起動確認 agblksize 0486と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はJFS2でcrfsを用い・agblksize とファイルシステム属性を確認する。</li><li>B. 仕様上の役割はLVMでchvgを用い・VG STATE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割はネットワークでno -aを用い・Link Status とEthernet統計を確認する。</li><li>D. 仕様上の役割は導入と起動でnimadmを用い・Technology Level とOSレベル表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Bの記述「LVMでchvgを用い、VG STATE とミラーコピー状態を確認する」に対応する項目はVG STATE（性能・chvg）です。性能に関するLVMの仕様は「LVMでchvgを用い、VG STATE」で、確認対象はch・性能です。起動・crfsのA:は「JFS2でcrfsを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・crfs）です。バック・noのC:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（バッ・no）です。属性・nimaのD:は「導入と起動でnimadmを用い、Technology Level」を述べ、対象はTechnology Level（属性・nima）です。「chvg」は「LVMでchvgを用い、VG STATE」を指し、VG STATEではch・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 性能確認 VG STATE 0485</strong></p><p>検証目的: LVMのchvg 性能確認 VG STATE 0485について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM性能確認005-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40485        rootvg          active
hdisk1          00f6a1b2c3d50485        datavg          active
確認コード AIX0485A
画面・出力には AIX0485A が表示され、chvg 性能確認 VG STATE 0485 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1005
確認コード AIX0485B
画面・出力には AIX0485B が表示され、chvg 性能確認 VG STATE 0485 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0485C
画面・出力には AIX0485C が表示され、chvg 性能確認 VG STATE 0485 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0485A が画面・出力に表示されること
② ステップ2 の AIX0485B が画面・出力に表示されること
③ ステップ3 の AIX0485C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0119"><h3>chvg 性能確認 VG STATE 0545</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第五百四十五観点 LVM で chvg は 性能確認 を点検します（運用第五百四十五）（第五百四十五観点）。第五百四十五観点 確認時には VG STATE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第五百四十五）（第五百四十五観点）。第五百四十五観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第五百四十五観点）。第五百四十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0545へ書きます（第五百四十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「chvg 性能確認 VG STATE 0545」を「crfs 起動確認 agblksize 0546」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はJFS2でcrfsを用い・agblksize とファイルシステム属性を確認する。</li><li>B. 仕様上の役割は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。</li><li>C. 仕様上の役割はSRCとログでtail -f /tmp/myfileを用い・Subsystemである。</li><li>D. 仕様上の役割はLVMでchvgを用い・VG STATE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「LVMでchvgを用い、VG STATE とミラーコピー状態を確認する」に対応する項目はVG STATE（性能・chvg）です。性能に関するLVMの仕様は「LVMでchvgを用い、VG STATE」で、確認対象はch・性能です。起動・crfsのA:は「JFS2でcrfsを用い、agblksize」を述べ、対象は起動確認 agblksize（起動・crfs）です。属性・照合・lspvのB:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は属性照合 照合単位（属性・lspv）です。属性・tailのC:は「SRCとログでtail -f /tmp/myfileを用い」を述べ、対象は属性確認 Subsystem（属性・tail）です。「chvg」は「LVMでchvgを用い、VG STATE」を指し、VG STATEではch・性能に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 性能確認 VG STATE 0545</strong></p><p>検証目的: LVMのchvg 性能確認 VG STATE 0545について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM性能確認065-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40545        rootvg          active
hdisk1          00f6a1b2c3d50545        datavg          active
確認コード AIX0545A
画面・出力には AIX0545A が表示され、chvg 性能確認 VG STATE 0545 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1065
確認コード AIX0545B
画面・出力には AIX0545B が表示され、chvg 性能確認 VG STATE 0545 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0545C
画面・出力には AIX0545C が表示され、chvg 性能確認 VG STATE 0545 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0545A が画面・出力に表示されること
② ステップ2 の AIX0545B が画面・出力に表示されること
③ ステップ3 の AIX0545C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0120"><h3>chvg 構成照合 PP SIZE 0644</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第六百四十四観点 LVM で chvg は 構成照合 を点検します（運用第六百四十四）（第六百四十四観点）。第六百四十四観点 確認時には PP SIZE と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第六百四十四）（第六百四十四観点）。第六百四十四観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第六百四十四観点）。第六百四十四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0644へ書きます（第六百四十四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chvg 構成照合 PP SIZE 0644の技術的な意味を資料で確認するとき、crfs 変更前確認 lff 0645との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はJFS2でcrfsを用い・lff とマウントオプションを確認する。</li><li>B. コマンドまたは機能の用途はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。</li><li>C. コマンドまたは機能の用途はLVMでchvgを用い・PP SIZE と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途は導入と起動でnimadmを用い・bootlist と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「LVMでchvgを用い、PP SIZE と論理ボリューム配置を確認する」に対応する項目はPP SIZE（構成・chvg）です。構成に関するLVMの仕様は「LVMでchvgを用い、PP SIZE と論理ボリューム配置を確認す」で、確認対象はch・構成です。変更前・crfsのA:は「JFS2でcrfsを用い、lff とマウントオプションを確認する」を述べ、対象は変更前確認 lff（変更・crfs）です。監査・lsatのB:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsat）です。変更後・nimaのD:は「導入と起動でnimadmを用い、bootlist」を述べ、対象は変更後確認 bootlist（変更・nima）です。「chvg」は「LVMでchvgを用い、PP SIZE と論理ボリューム配置を確認す」を指し、PP SIZEではch・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 構成照合 PP SIZE 0644</strong></p><p>検証目的: LVMのchvg 構成照合 PP SIZE 0644について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM構成照合044-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40644        rootvg          active
hdisk1          00f6a1b2c3d50644        datavg          active
確認コード AIX0644A
画面・出力には AIX0644A が表示され、chvg 構成照合 PP SIZE 0644 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1044
確認コード AIX0644B
画面・出力には AIX0644B が表示され、chvg 構成照合 PP SIZE 0644 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0644C
画面・出力には AIX0644C が表示され、chvg 構成照合 PP SIZE 0644 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0644A が画面・出力に表示されること
② ステップ2 の AIX0644B が画面・出力に表示されること
③ ステップ3 の AIX0644C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0121"><h3>chvg 構成照合 PP SIZE 0704</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第七百四観点 LVM で chvg は 構成照合 を点検します（運用第七百四）（第七百四観点）。第七百四観点 確認時には PP SIZE と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第七百四）（第七百四観点）。第七百四観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第七百四観点）。第七百四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0704へ書きます（第七百四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chvg 構成照合 PP SIZE 0704を同一分類のcrfs 変更前確認 lff 0705と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はJFS2でcrfsを用い・lff とマウントオプションを確認する。</li><li>B. コマンドまたは機能の用途はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。</li><li>C. コマンドまたは機能の用途はLVMでchvgを用い・PP SIZE と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. コマンドまたは機能の用途は導入と起動でoslevel -sを用い・altinst_rootvg と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「LVMでchvgを用い、PP SIZE と論理ボリューム配置を確認する」に対応する項目はPP SIZE（構成・chvg）です。構成に関するLVMの仕様は「LVMでchvgを用い、PP SIZE と論理ボリューム配置を確認す」で、確認対象はch・構成です。変更前・crfsのA:は「JFS2でcrfsを用い、lff とマウントオプションを確認する」を述べ、対象は変更前確認 lff（変更・crfs）です。監査・lsatのB:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 enhanced_RBAC（監査・lsat）です。障害切・osleのD:は「導入と起動でoslevel -sを用い、altinst_rootvg」を述べ、対象は障害切り分け altinst_roo（障害・osle）です。「chvg」は「LVMでchvgを用い、PP SIZE と論理ボリューム配置を確認す」を指し、PP SIZEではch・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 構成照合 PP SIZE 0704</strong></p><p>検証目的: LVMのchvg 構成照合 PP SIZE 0704について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM構成照合104-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40704        rootvg          active
hdisk1          00f6a1b2c3d50704        datavg          active
確認コード AIX0704A
画面・出力には AIX0704A が表示され、chvg 構成照合 PP SIZE 0704 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1104
確認コード AIX0704B
画面・出力には AIX0704B が表示され、chvg 構成照合 PP SIZE 0704 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0704C
画面・出力には AIX0704C が表示され、chvg 構成照合 PP SIZE 0704 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0704A が画面・出力に表示されること
② ステップ2 の AIX0704B が画面・出力に表示されること
③ ステップ3 の AIX0704C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0122"><h3>chvg 構成照合 VG STATE 0168</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第百六十八観点 LVM で chvg は 構成照合 を点検します（運用第百六十八）（第百六十八観点）。第百六十八観点 確認時には VG STATE と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第百六十八）（第百六十八観点）。第百六十八観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第百六十八観点）。第百六十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0168へ書きます（第百六十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chvg 構成照合 VG STATE 0168を同一分類のcrfs 変更前確認 isnapshot 0169と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はJFS2でcrfsを用い・isnapshot とマウントオプションを確認する。</li><li>B. 構成を確認する際の意味はネットワークでno -aを用い・Link Status とアダプター一覧を確認する。</li><li>C. 構成を確認する際の意味はLVMでchvgを用い・VG STATE と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味はJFS2でsplitcopyを用い・agblksize とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「LVMでchvgを用い、VG STATE と論理ボリューム配置を確認する」に対応する項目はVG STATE（構成・chvg）です。構成に関するLVMの仕様は「LVMでchvgを用い、VG STATE」で、確認対象はch・構成です。変更前・crfsのA:は「JFS2でcrfsを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・crfs）です。性能・noのB:は「ネットワークでno -aを用い、Link Status」を述べ、対象はLink Status（性能・no）です。運用引・spliのD:は「JFS2でsplitcopyを用い、agblksize」を述べ、対象は運用引継ぎ agblksize（運用・spli）です。「chvg」は「LVMでchvgを用い、VG STATE」を指し、VG STATEではch・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 構成照合 VG STATE 0168</strong></p><p>検証目的: LVMのchvg 構成照合 VG STATE 0168について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM構成照合048-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40168        rootvg          active
hdisk1          00f6a1b2c3d50168        datavg          active
確認コード AIX0168A
画面・出力には AIX0168A が表示され、chvg 構成照合 VG STATE 0168 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1048
確認コード AIX0168B
画面・出力には AIX0168B が表示され、chvg 構成照合 VG STATE 0168 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0168C
画面・出力には AIX0168C が表示され、chvg 構成照合 VG STATE 0168 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0168A が画面・出力に表示されること
② ステップ2 の AIX0168B が画面・出力に表示されること
③ ステップ3 の AIX0168C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0123"><h3>chvg 構成照合 VG STATE 0228</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第二百二十八観点 LVM で chvg は 構成照合 を点検します（運用第二百二十八）（第二百二十八観点）。第二百二十八観点 確認時には VG STATE と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第二百二十八）（第二百二十八観点）。第二百二十八観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第二百二十八観点）。第二百二十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0228へ書きます（第二百二十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chvg 構成照合 VG STATE 0228の技術的な意味を資料で確認するとき、crfs 変更前確認 isnapshot 0229との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はJFS2でcrfsを用い・isnapshot とマウントオプションを確認する。</li><li>B. 構成を確認する際の意味はLVMでchvgを用い・VG STATE と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 構成を確認する際の意味はネットワークでroute -n getを用い・Media Speed Runningである。</li><li>D. 構成を確認する際の意味は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「LVMでchvgを用い、VG STATE と論理ボリューム配置を確認する」に対応する項目はVG STATE（構成・chvg）です。構成に関するLVMの仕様は「LVMでchvgを用い、VG STATE」で、確認対象はch・構成です。変更前・crfsのA:は「JFS2でcrfsを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・crfs）です。起動・routのC:は「ネットワークでroute -n getを用い、Media」を述べ、対象はSpeed Running（起動・rout）です。一覧・状態・lspvのD:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は一覧確認 状態確認（一覧・lspv）です。「chvg」は「LVMでchvgを用い、VG STATE」を指し、VG STATEではch・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 構成照合 VG STATE 0228</strong></p><p>検証目的: LVMのchvg 構成照合 VG STATE 0228について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM構成照合108-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40228        rootvg          active
hdisk1          00f6a1b2c3d50228        datavg          active
確認コード AIX0228A
画面・出力には AIX0228A が表示され、chvg 構成照合 VG STATE 0228 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1108
確認コード AIX0228B
画面・出力には AIX0228B が表示され、chvg 構成照合 VG STATE 0228 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0228C
画面・出力には AIX0228C が表示され、chvg 構成照合 VG STATE 0228 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0228A が画面・出力に表示されること
② ステップ2 の AIX0228B が画面・出力に表示されること
③ ステップ3 の AIX0228C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0124"><h3>chvg 運用引継ぎ PVID 0674</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第六百七十四観点 LVM で chvg は 運用引継ぎ を点検します（運用第六百七十四）（第六百七十四観点）。第六百七十四観点 確認時には PVID と 物理ボリューム一覧 の対応を同じ資料上で追えることを前提にします（資料第六百七十四）（第六百七十四観点）。第六百七十四観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、stale区画の見落とし を避ける判断根拠を説明可能にします（第六百七十四観点）。第六百七十四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0674へ書きます（第六百七十四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chvg 運用引継ぎ PVID 0674の役割を調べています。crfs 容量確認 agblksize 0675の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はJFS2でcrfsを用い・agblksize と内部スナップショットを確認する。</li><li>B. 障害切り分けに用いる役割はLVMでchvgを用い・PVID と物理ボリューム一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 障害切り分けに用いる役割はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。</li><li>D. 障害切り分けに用いる役割は導入と起動でoslevel -sを用い・fileset level とfileset一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LVMでchvgを用い、PVID と物理ボリューム一覧を確認する」に対応する項目は運用引継ぎ PVID（運用・chvg）です。運用引に関するLVMの仕様は「LVMでchvgを用い、PVID と物理ボリューム一覧を確認する」で、確認対象はch・運用引です。容量・crfsのA:は「JFS2でcrfsを用い、agblksize」を述べ、対象は容量確認 agblksize（容量・crfs）です。状態・lsatのC:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsat）です。起動・osleのD:は「導入と起動でoslevel -sを用い、fileset level」を述べ、対象はfileset level（起動・osle）です。「chvg」は「LVMでchvgを用い、PVID と物理ボリューム一覧を確認する」を指し、運用引継ぎ PVIDではch・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 運用引継ぎ PVID 0674</strong></p><p>検証目的: LVMのchvg 運用引継ぎ PVID 0674について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM運用引継ぎ074-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40674        rootvg          active
hdisk1          00f6a1b2c3d50674        datavg          active
確認コード AIX0674A
画面・出力には AIX0674A が表示され、chvg 運用引継ぎ PVID 0674 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1074
確認コード AIX0674B
画面・出力には AIX0674B が表示され、chvg 運用引継ぎ PVID 0674 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0674C
画面・出力には AIX0674C が表示され、chvg 運用引継ぎ PVID 0674 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0674A が画面・出力に表示されること
② ステップ2 の AIX0674B が画面・出力に表示されること
③ ステップ3 の AIX0674C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0125"><h3>chvg 運用引継ぎ STALE PARTITIONS 0198</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第百九十八観点 LVM で chvg は 運用引継ぎ を点検します（運用第百九十八）（第百九十八観点）。第百九十八観点 確認時には STALE PARTITIONS と 物理ボリューム一覧 の対応を同じ資料上で追えることを前提にします（資料第百九十八）（第百九十八観点）。第百九十八観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、stale区画の見落とし を避ける判断根拠を説明可能にします（第百九十八観点）。第百九十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0198へ書きます（第百九十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> chvg 運用引継ぎ STALE PARTITIONS 0198に関する障害切り分けの前提を確認しています。crfs 容量確認 ファイルシステム使用率 0199の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはJFS2でcrfsを用い・ファイルシステム使用率 と内部スナップショットを確認する。crfs 容量確認 ファイルシステム使用率 0199固有の属性も確認対象に含める。</li><li>B. 機能の説明としてはネットワークでroute -n getを用い・Gateway と経路表を確認する。</li><li>C. 機能の説明としてはJFS2でsplitcopyを用い・lff と内部スナップショットを確認する。</li><li>D. 機能の説明としてはLVMでchvgを用い・STALE PARTITIONS と物理ボリューム一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「LVMでchvgを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（運用・chvg）です。運用引に関するLVMの仕様は「LVMでchvgを用い、STALE PARTITIONS」で、確認対象はch・運用引です。容量・ファ・crfsのA:は「JFS2でcrfsを用い、ファイルシステム使用率」を述べ、対象は容量確認 ファイルシステム使用率（容量・crfs）です。障害切・routのB:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・rout）です。構成・spliのC:は「JFS2でsplitcopyを用い、lff」を述べ、対象は構成照合 lff（構成・spli）です。「chvg」は「LVMでchvgを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではch・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>chvg 運用引継ぎ STALE PARTITIONS 0198</strong></p><p>検証目的: LVMのchvg 運用引継ぎ STALE PARTITIONS 0198について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM運用引継ぎ078-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; chvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40198        rootvg          active
hdisk1          00f6a1b2c3d50198        datavg          active
確認コード AIX0198A
画面・出力には AIX0198A が表示され、chvg 運用引継ぎ STALE PARTITIONS 0198 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1078
確認コード AIX0198B
画面・出力には AIX0198B が表示され、chvg 運用引継ぎ STALE PARTITIONS 0198 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0198C
画面・出力には AIX0198C が表示され、chvg 運用引継ぎ STALE PARTITIONS 0198 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0198A が画面・出力に表示されること
② ステップ2 の AIX0198B が画面・出力に表示されること
③ ステップ3 の AIX0198C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0126"><h3>errpt 変更前確認 再読込</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第百二十六観点 LVM で errpt は 変更前確認 を点検します（運用第百二十六）（第百二十六観点）。第百二十六観点 確認時には 再読込 と PVID 欄 の対応を同じ資料上で追えることを前提にします（資料第百二十六）（第百二十六観点）。第百二十六観点 errpt の出力と取得時刻を同じ確認票に置き、ボリュームグループの取り違え を避ける判断根拠を説明可能にします（第百二十六観点）。第百二十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0126へ書きます（第百二十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「errpt 変更前確認 再読込」を「lsattr 復旧前確認 対象ファイル」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はAIX エラーログから要約または詳細レポートを生成するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はデバイスや sys0 などの属性値を表示するコマンドである。</li><li>C. 運用時に利用する技術的役割は導入と起動でemgr -lを用い・altinst_rootvg とfileset一覧を確認する。</li><li>D. 運用時に利用する技術的役割はLVMでlsvg -lを用い・PP SIZE と物理ボリューム一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は変更前確認 再読込（変更・errp）です。LVMの仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・変更前です。復旧前・lsatのB:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は復旧前確認 対象ファイル（復旧・lsat）です。バック・emgrのC:は「導入と起動でemgr -lを用い、altinst_rootvg」を述べ、対象はバックアウト確認 altinst_r（バッ・emgr）です。変更前・lsvgのD:は「LVMでlsvg -lを用い、PP SIZE」を述べ、対象はPP SIZE（変更・lsvg）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、変更前確認 再読込ではer・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>errpt 変更前確認 再読込</strong></p><p>検証目的: LVMのerrpt 変更前確認 再読込について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、LVMの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。PVID 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lparstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
%user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
画面・出力には System が含まれ、errpt 変更前確認 再読込の証跡を確認できます。
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


<section class="kb-item" id="c01-i0127"><h3>errpt 状態判定 表形式</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第百二十七観点 LVM で errpt 状態判定 表形式 は 確認 を点検します（運用第百二十七）（第百二十七観点）。第百二十七観点 確認時には PVID 欄 と PVID 欄 の対応を同じ資料上で追えることを前提にします（資料第百二十七）（第百二十七観点）。第百二十七観点 errpt 状態判定 表形式 の出力と取得時刻を同じ確認票に置き、ボリュームグループの取り違え を避ける判断根拠を説明可能にします（第百二十七観点）。第百二十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0127へ書きます（第百二十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「errpt 状態判定 表形式」を「lsattr 属性照合 ディスク状態」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はデバイスや sys0 などの属性値を表示するコマンドである。</li><li>B. 仕様上の役割はAIX エラーログから要約または詳細レポートを生成するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 仕様上の役割はLVMでlslvを用い・LV STATE とボリュームグループ属性を確認する。</li><li>D. 仕様上の役割は性能管理でsvmon -Gを用い・csz とvmstat表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「AIX エラーログから要約または詳細レポートを生成するコマンドである」に対応する項目は状態判定 表形式（状態・errp）です。LVMの仕様は「AIX エラーログから要約または詳細レポートを生成するコマンド」で、確認対象はer・状態・表形です。属性・ディ・lsatのA:は「デバイスや sys0 などの属性値を表示するコマンド」を述べ、対象は属性照合 ディスク状態（属性・lsat）です。構成・lslvのC:は「LVMでlslvを用い、LV STATE」を述べ、対象はLV STATE（構成・lslv）です。起動・svmoのD:は「性能管理でsvmon -Gを用い、csz」を述べ、対象は起動確認 csz（起動・svmo）です。「errpt」は「AIX エラーログから要約または詳細レポートを生成するコマンド」を指し、状態判定 表形式ではer・状態・表形に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>errpt 状態判定 表形式</strong></p><p>検証目的: LVMのerrpt 状態判定 表形式について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、LVMの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。PVID 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lparstat -c 2 1
→ Enter を押す
［画面・出力］
System configuration: type=Shared mode=Uncapped mmode=Ded-E smt=On
%user %sys %wait %idle physc %entc lbusy app vcsw phint %xcpu dxm
画面・出力には System が含まれ、errpt 状態判定 表形式の証跡を確認できます。
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


<section class="kb-item" id="c01-i0128"><h3>lslv バックアウト確認 STALE PARTITIONS 0470</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第四百七十観点 LVM で lslv は バックアウト確認 を点検します（運用第四百七十）（第四百七十観点）。第四百七十観点 確認時には STALE PARTITIONS と 物理ボリューム一覧 の対応を同じ資料上で追えることを前提にします（資料第四百七十）（第四百七十観点）。第四百七十観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、stale区画の見落とし を避ける判断根拠を説明可能にします（第四百七十観点）。第四百七十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0470へ書きます（第四百七十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv バックアウト確認 STALE PARTITIONS 0470に関する障害切り分けの前提を確認しています。fsck 監査記録 ファイルシステム使用率 0471の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はJFS2でfsckを用い・ファイルシステム使用率 と内部スナップショットを確認する。</li><li>B. 障害切り分けに用いる役割はネットワークでchdev -l en0 -aを用い・Gateway と経路表を確認する。</li><li>C. 障害切り分けに用いる役割は導入と起動でalt_disk_copyを用い・mksysb image とfileset一覧を確認する。</li><li>D. 障害切り分けに用いる役割はLVMでlslvを用い・STALE PARTITIONS と物理ボリューム一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Dの記述「LVMでlslvを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（バッ・lslv）です。バックに関するLVMの仕様は「LVMでlslvを用い、STALE PARTITIONS」で、確認対象はls・バックです。監査・ファ・fsckのA:は「JFS2でfsckを用い、ファイルシステム使用率」を述べ、対象は監査記録 ファイルシステム使用率（監査・fsck）です。変更前・chdeのB:は「ネットワークでchdev -l en0 -aを用い、Gateway」を述べ、対象は変更前確認 Gateway（変更・chde）です。容量・alt_のC:は「導入と起動でalt_disk_copyを用い、mksysb」を述べ、対象はmksysb image（容量・alt_）です。「lslv」は「LVMでlslvを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではls・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv バックアウト確認 STALE PARTITIONS 0470</strong></p><p>検証目的: LVMのlslv バックアウト確認 STALE PARTITIONS 0470について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVMバックアウト確認110-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40470        rootvg          active
hdisk1          00f6a1b2c3d50470        datavg          active
確認コード AIX0470A
画面・出力には AIX0470A が表示され、lslv バックアウト確認 STALE PARTITIONS 0470 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1110
確認コード AIX0470B
画面・出力には AIX0470B が表示され、lslv バックアウト確認 STALE PARTITIONS 0470 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0470C
画面・出力には AIX0470C が表示され、lslv バックアウト確認 STALE PARTITIONS 0470 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0470A が画面・出力に表示されること
② ステップ2 の AIX0470B が画面・出力に表示されること
③ ステップ3 の AIX0470C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0129"><h3>lslv 変更後確認 LV STATE 0122</h3><p class="kb-meta">分類: LVM ・ 難易度: 初級</p><p>第百二十二観点 LVM で lslv は 変更後確認 を点検します（運用第百二十二）（第百二十二観点）。第百二十二観点 確認時には LV STATE と 物理ボリューム一覧 の対応を同じ資料上で追えることを前提にします（資料第百二十二）（第百二十二観点）。第百二十二観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、stale区画の見落とし を避ける判断根拠を説明可能にします（第百二十二観点）。第百二十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0122へ書きます（第百二十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 変更後確認 LV STATE 0122の役割を調べています。fsck 障害切り分け mountguard 0123の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はJFS2でfsckを用い・mountguard と内部スナップショットを確認する。</li><li>B. 障害切り分けに用いる役割はネットワークでifconfig en0を用い・Media Speed Running と経路表を確認する。</li><li>C. 障害切り分けに用いる役割はJFS2でchfsを用い・isnapshot と内部スナップショットを確認する。</li><li>D. 障害切り分けに用いる役割はLVMでlslvを用い・LV STATE と物理ボリューム一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「LVMでlslvを用い、LV STATE と物理ボリューム一覧を確認する」に対応する項目はLV STATE（変更・lslv）です。変更後に関するLVMの仕様は「LVMでlslvを用い、LV STATE」で、確認対象はls・変更後です。障害切・fsckのA:は「JFS2でfsckを用い、mountguard」を述べ、対象は障害切り分け mountguard（障害・fsck）です。属性・ifcoのB:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（属性・ifco）です。性能・chfsのC:は「JFS2でchfsを用い、isnapshot」を述べ、対象は性能確認 isnapshot（性能・chfs）です。「lslv」は「LVMでlslvを用い、LV STATE」を指し、LV STATEではls・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 変更後確認 LV STATE 0122</strong></p><p>検証目的: LVMのlslv 変更後確認 LV STATE 0122について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM変更後確認002-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40122        rootvg          active
hdisk1          00f6a1b2c3d50122        datavg          active
確認コード AIX0122A
画面・出力には AIX0122A が表示され、lslv 変更後確認 LV STATE 0122 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1002
確認コード AIX0122B
画面・出力には AIX0122B が表示され、lslv 変更後確認 LV STATE 0122 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0122C
画面・出力には AIX0122C が表示され、lslv 変更後確認 LV STATE 0122 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0122A が画面・出力に表示されること
② ステップ2 の AIX0122B が画面・出力に表示されること
③ ステップ3 の AIX0122C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0130"><h3>lslv 属性照合 エラー詳細</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第百三十観点 LVM で lslv 属性照合 エラー詳細 は 確認 を点検します（運用第百三十）（第百三十観点）。第百三十観点 確認時には PVID 欄 と PVID 欄 の対応を同じ資料上で追えることを前提にします（資料第百三十）（第百三十観点）。第百三十観点 lslv 属性照合 エラー詳細 の出力と取得時刻を同じ確認票に置き、ページング使用率の見落とし を避ける判断根拠を説明可能にします（第百三十観点）。第百三十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0130へ書きます（第百三十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lslv 属性照合 エラー詳細」を「lsps 障害切り分け ファイルセット」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>B. 保守作業で参照する機能は論理ボリュームの属性と割り当て情報を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はJFS2でchfsを用い・log=INLINE と内部スナップショットを確認する。</li><li>D. 保守作業で参照する機能はセキュリティでlsattr -E -l sys0 -aを用い・roles とRBAC属性を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は属性照合 エラー詳細（属性・lslv）です。LVMの仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・属性・エラです。障害切・lspsのA:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は障害切り分け ファイルセット（障害・lsps）です。性能・chfsのC:は「JFS2でchfsを用い、log=INLINE」を述べ、対象は性能確認 log=INLINE（性能・chfs）です。監査・lsatのD:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は監査記録 roles（監査・lsat）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、属性照合 エラー詳細ではls・属性・エラに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 属性照合 エラー詳細</strong></p><p>検証目的: LVMのlslv 属性照合 エラー詳細について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、LVMの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。PVID 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt -a -N hdisk1
→ Enter を押す
［画面・出力］
LABEL: DISK_ERR4
RESOURCE NAME: hdisk1
Description
DISK OPERATION ERROR
画面・出力には LABEL が含まれ、lslv 属性照合 エラー詳細の証跡を確認できます。
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


<section class="kb-item" id="c01-i0131"><h3>lslv 属性確認 VG STATE 0440</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第四百四十観点 LVM で lslv は 属性確認 を点検します（運用第四百四十）（第四百四十観点）。第四百四十観点 確認時には VG STATE と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第四百四十）（第四百四十観点）。第四百四十観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第四百四十観点）。第四百四十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0440へ書きます（第四百四十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 属性確認 VG STATE 0440を同一分類のfsck 状態確認 isnapshot 0441と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はJFS2でfsckを用い・isnapshot とマウントオプションを確認する。</li><li>B. コマンドまたは機能の用途はLVMでlslvを用い・VG STATE と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. コマンドまたは機能の用途はネットワークでchdev -l en0 -aを用い・Media Speed Runningである。</li><li>D. コマンドまたは機能の用途は導入と起動でalt_disk_copyを用い・EFIX LABEL と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LVMでlslvを用い、VG STATE と論理ボリューム配置を確認する」に対応する項目はVG STATE（属性・lslv）です。属性に関するLVMの仕様は「LVMでlslvを用い、VG STATE」で、確認対象はls・属性です。状態・fsckのA:は「JFS2でfsckを用い、isnapshot」を述べ、対象は状態確認 isnapshot（状態・fsck）です。容量・chdeのC:は「ネットワークでchdev -l en0 -aを用い、Media」を述べ、対象はSpeed Running（容量・chde）です。変更前・alt_のD:は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（変更・alt_）です。「lslv」は「LVMでlslvを用い、VG STATE」を指し、VG STATEではls・属性に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 属性確認 VG STATE 0440</strong></p><p>検証目的: LVMのlslv 属性確認 VG STATE 0440について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM属性確認080-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40440        rootvg          active
hdisk1          00f6a1b2c3d50440        datavg          active
確認コード AIX0440A
画面・出力には AIX0440A が表示され、lslv 属性確認 VG STATE 0440 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1080
確認コード AIX0440B
画面・出力には AIX0440B が表示され、lslv 属性確認 VG STATE 0440 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0440C
画面・出力には AIX0440C が表示され、lslv 属性確認 VG STATE 0440 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0440A が画面・出力に表示されること
② ステップ2 の AIX0440B が画面・出力に表示されること
③ ステップ3 の AIX0440C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0132"><h3>lslv 復旧前確認 サンプル採取</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第百三十二観点 LVM で lslv 復旧前確認 サンプル採取 は 確認 を点検します（運用第百三十二）（第百三十二観点）。第百三十二観点 確認時には PVID 欄 と PVID 欄 の対応を同じ資料上で追えることを前提にします（資料第百三十二）（第百三十二観点）。第百三十二観点 lslv 復旧前確認 サンプル採取 の出力と取得時刻を同じ確認票に置き、ページング使用率の見落とし を避ける判断根拠を説明可能にします（第百三十二観点）。第百三十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0132へ書きます（第百三十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lslv 復旧前確認 サンプル採取」を「lsps 一覧確認 メッセージ行」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割は論理ボリュームの属性と割り当て情報を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>C. 仕様上の役割は導入と起動でlslpp -Lを用い・EFIX LABEL とfileset一覧を確認する。</li><li>D. 仕様上の役割はLVMでlsvgを用い・LV STATE と物理ボリューム一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「論理ボリュームの属性と割り当て情報を表示するコマンドである」に対応する項目は復旧前確認 サンプル採取（復旧・lslv）です。LVMの仕様は「論理ボリュームの属性と割り当て情報を表示するコマンド」で、確認対象はls・復旧前です。一覧・メッ・lspsのB:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は一覧確認 メッセージ行（一覧・lsps）です。構成・lslpのC:は「導入と起動でlslpp -Lを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（構成・lslp）です。属性・lsvgのD:は「LVMでlsvgを用い、LV STATE」を述べ、対象はLV STATE（属性・lsvg）です。「lslv」は「論理ボリュームの属性と割り当て情報を表示するコマンド」を指し、復旧前確認 サンプル採取ではls・復旧前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 復旧前確認 サンプル採取</strong></p><p>検証目的: LVMのlslv 復旧前確認 サンプル採取について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、LVMの対象へ進みます。
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
現在の画面はAIX 7.3の確認画面です。PVID 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; errpt -a -N hdisk1
→ Enter を押す
［画面・出力］
LABEL: DISK_ERR4
RESOURCE NAME: hdisk1
Description
DISK OPERATION ERROR
画面・出力には LABEL が含まれ、lslv 復旧前確認 サンプル採取の証跡を確認できます。
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


<section class="kb-item" id="c01-i0133"><h3>lslv 構成照合 LV STATE 0251</h3><p class="kb-meta">分類: LVM ・ 難易度: 初級</p><p>第二百五十一観点 LVM で lslv は 構成照合 を点検します（運用第二百五十一）（第二百五十一観点）。第二百五十一観点 確認時には LV STATE と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第二百五十一）（第二百五十一観点）。第二百五十一観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第二百五十一観点）。第二百五十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0251へ書きます（第二百五十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 構成照合 LV STATE 0251について構成や状態を確認します。fsck 変更前確認 isnapshot 0252ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はJFS2でfsckを用い・isnapshot とログデバイス設定を確認する。</li><li>B. 一次資料が示す主目的はネットワークでifconfig en0を用い・Media Speed Running とMTU属性を確認する。</li><li>C. 一次資料が示す主目的はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>D. 一次資料が示す主目的はLVMでlslvを用い・LV STATE とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「LVMでlslvを用い、LV STATE とボリュームグループ属性を確認する」に対応する項目はLV STATE（構成・lslv）です。構成に関するLVMの仕様は「LVMでlslvを用い、LV STATE」で、確認対象はls・構成です。変更前・fsckのA:は「JFS2でfsckを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・fsck）です。性能・ifcoのB:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（性能・ifco）です。詳細・メッ・lspsのC:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は詳細確認 メッセージ行（詳細・lsps）です。「lslv」は「LVMでlslvを用い、LV STATE」を指し、LV STATEではls・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 構成照合 LV STATE 0251</strong></p><p>検証目的: LVMのlslv 構成照合 LV STATE 0251について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM構成照合011-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40251        rootvg          active
hdisk1          00f6a1b2c3d50251        datavg          active
確認コード AIX0251A
画面・出力には AIX0251A が表示され、lslv 構成照合 LV STATE 0251 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1011
確認コード AIX0251B
画面・出力には AIX0251B が表示され、lslv 構成照合 LV STATE 0251 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0251C
画面・出力には AIX0251C が表示され、lslv 構成照合 LV STATE 0251 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0251A が画面・出力に表示されること
② ステップ2 の AIX0251B が画面・出力に表示されること
③ ステップ3 の AIX0251C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0134"><h3>lslv 構成照合 LV STATE 0311</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第三百十一観点 LVM で lslv は 構成照合 を点検します（運用第三百十一）（第三百十一観点）。第三百十一観点 確認時には LV STATE と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第三百十一）（第三百十一観点）。第三百十一観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第三百十一観点）。第三百十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0311へ書きます（第三百十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 構成照合 LV STATE 0311の設定や表示を読む前に役割を確認します。fsck 変更前確認 isnapshot 0312ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 一次資料が示す主目的はJFS2でfsckを用い・isnapshot とログデバイス設定を確認する。</li><li>B. 一次資料が示す主目的はネットワークでchdev -l en0 -aを用い・MTU とMTU属性を確認する。</li><li>C. 一次資料が示す主目的は導入と起動でalt_disk_copyを用い・EFIX LABEL と代替ディスク状態を確認する。</li><li>D. 一次資料が示す主目的はLVMでlslvを用い・LV STATE とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「LVMでlslvを用い、LV STATE とボリュームグループ属性を確認する」に対応する項目はLV STATE（構成・lslv）です。構成に関するLVMの仕様は「LVMでlslvを用い、LV STATE」で、確認対象はls・構成です。変更前・fsckのA:は「JFS2でfsckを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・fsck）です。起動・chdeのB:は「ネットワークでchdev -l en0 -aを用い、MTU」を述べ、対象は起動確認 MTU（起動・chde）です。障害切・alt_のC:は「導入と起動でalt_disk_copyを用い、EFIX LABEL」を述べ、対象はEFIX LABEL（障害・alt_）です。「lslv」は「LVMでlslvを用い、LV STATE」を指し、LV STATEではls・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 構成照合 LV STATE 0311</strong></p><p>検証目的: LVMのlslv 構成照合 LV STATE 0311について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM構成照合071-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40311        rootvg          active
hdisk1          00f6a1b2c3d50311        datavg          active
確認コード AIX0311A
画面・出力には AIX0311A が表示され、lslv 構成照合 LV STATE 0311 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1071
確認コード AIX0311B
画面・出力には AIX0311B が表示され、lslv 構成照合 LV STATE 0311 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0311C
画面・出力には AIX0311C が表示され、lslv 構成照合 LV STATE 0311 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0311A が画面・出力に表示されること
② ステップ2 の AIX0311B が画面・出力に表示されること
③ ステップ3 の AIX0311C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0135"><h3>lslv 構成照合 STALE PARTITIONS 0727</h3><p class="kb-meta">分類: LVM ・ 難易度: 初級</p><p>第七百二十七観点 LVM で lslv は 構成照合 を点検します（運用第七百二十七）（第七百二十七観点）。第七百二十七観点 確認時には STALE PARTITIONS と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第七百二十七）（第七百二十七観点）。第七百二十七観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第七百二十七観点）。第七百二十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0727へ書きます（第七百二十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 構成照合 STALE PARTITIONS 0727の設定や表示を読む前に役割を確認します。fsck 変更前確認 lff 0728ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはJFS2でfsckを用い・lff とログデバイス設定を確認する。</li><li>B. 対象資源に対する働きはセキュリティでrbacqry -u user1 -Tを用い・roles と監査設定を確認する。</li><li>C. 対象資源に対する働きはLVMでlslvを用い・STALE PARTITIONS とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きは導入と起動でemgr -lを用い・bootlist と代替ディスク状態を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「LVMでlslvを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（構成・lslv）です。構成に関するLVMの仕様は「LVMでlslvを用い、STALE PARTITIONS」で、確認対象はls・構成です。変更前・fsckのA:は「JFS2でfsckを用い、lff とログデバイス設定を確認する」を述べ、対象は変更前確認 lff（変更・fsck）です。バック・rbacのB:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象はバックアウト確認 roles（バッ・rbac）です。変更後・emgrのD:は「導入と起動でemgr -lを用い、bootlist」を述べ、対象は変更後確認 bootlist（変更・emgr）です。「lslv」は「LVMでlslvを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではls・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 構成照合 STALE PARTITIONS 0727</strong></p><p>検証目的: LVMのlslv 構成照合 STALE PARTITIONS 0727について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM構成照合007-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40727        rootvg          active
hdisk1          00f6a1b2c3d50727        datavg          active
確認コード AIX0727A
画面・出力には AIX0727A が表示され、lslv 構成照合 STALE PARTITIONS 0727 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1007
確認コード AIX0727B
画面・出力には AIX0727B が表示され、lslv 構成照合 STALE PARTITIONS 0727 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0727C
画面・出力には AIX0727C が表示され、lslv 構成照合 STALE PARTITIONS 0727 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0727A が画面・出力に表示されること
② ステップ2 の AIX0727B が画面・出力に表示されること
③ ステップ3 の AIX0727C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0136"><h3>lslv 構成照合 STALE PARTITIONS 0787</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第七百八十七観点 LVM で lslv は 構成照合 を点検します（運用第七百八十七）（第七百八十七観点）。第七百八十七観点 確認時には STALE PARTITIONS と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第七百八十七）（第七百八十七観点）。第七百八十七観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第七百八十七観点）。第七百八十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0787へ書きます（第七百八十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 構成照合 STALE PARTITIONS 0787について構成や状態を確認します。chdev 詳細確認 一致条件ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはデバイス属性を変更する管理コマンドである。</li><li>B. 対象資源に対する働きはJFS2でfsckを用い・isnapshot とログデバイス設定を確認する。</li><li>C. 対象資源に対する働きはLVMでlslvを用い・STALE PARTITIONS とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きは導入と起動でoslevel -sを用い・Technology Level と代替ディスク状態を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構成・lslvでCの記述「LVMでlslvを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（構成・lslv）です。構成に関するLVMの仕様は「LVMでlslvを用い、STALE PARTITIONS」で、確認対象はls・構成です。詳細・一致・chdeのA:は「デバイス属性を変更する管理コマンド」を述べ、対象は詳細確認 一致条件（詳細・chde）です。変更前・fsckのB:は「JFS2でfsckを用い、isnapshot」を述べ、対象は変更前確認 isnapshot（変更・fsck）です。容量・osleのD:は「導入と起動でoslevel -sを用い、Technology」を述べ、対象はTechnology Level（容量・osle）です。「lslv」は「LVMでlslvを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではls・構成に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 構成照合 STALE PARTITIONS 0787</strong></p><p>検証目的: LVMのlslv 構成照合 STALE PARTITIONS 0787について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM構成照合067-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40787        rootvg          active
hdisk1          00f6a1b2c3d50787        datavg          active
確認コード AIX0787A
画面・出力には AIX0787A が表示され、lslv 構成照合 STALE PARTITIONS 0787 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1067
確認コード AIX0787B
画面・出力には AIX0787B が表示され、lslv 構成照合 STALE PARTITIONS 0787 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0787C
画面・出力には AIX0787C が表示され、lslv 構成照合 STALE PARTITIONS 0787 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0787A が画面・出力に表示されること
② ステップ2 の AIX0787B が画面・出力に表示されること
③ ステップ3 の AIX0787C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0137"><h3>lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0281</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第二百八十一観点 LVM で lslv は 運用引継ぎ を点検します（運用第二百八十一）（第二百八十一観点）。第二百八十一観点 確認時には MIRROR WRITE CONSISTENCY と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第二百八十一）（第二百八十一観点）。第二百八十一観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第二百八十一観点）。第二百八十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0281へ書きます（第二百八十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0281」を「fsck 容量確認 ファイルシステム使用率 0282」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はJFS2でfsckを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li><li>B. 仕様上の役割はネットワークでifconfig en0を用い・Gateway とEthernet統計を確認する。ifconfig en0 変更後確認 Gateway 0587固有の属性も確認対象に含める。</li><li>C. 仕様上の役割はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>D. 仕様上の役割はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「LVMでlslvを用い、MIRROR WRITE CONSISTENCY」に対応する項目はWRITE CONSISTENCY（運用・lslv）です。運用引に関するLVMの仕様は「LVMでlslvを用い、MIRROR WRITE」で、確認対象はls・運用引です。容量・ファ・fsckのA:は「JFS2でfsckを用い、ファイルシステム使用率」を述べ、対象は容量確認 ファイルシステム使用率（容量・fsck）です。変更後・ifcoのB:は「ネットワークでifconfig en0を用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・ifco）です。状態・属性・lspsのC:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は状態判定 属性確認（状態・lsps）です。「lslv」は「LVMでlslvを用い、MIRROR WRITE」を指し、WRITE CONSISTENCYではls・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0281</strong></p><p>検証目的: LVMのlslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0281について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM運用引継ぎ041-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40281        rootvg          active
hdisk1          00f6a1b2c3d50281        datavg          active
確認コード AIX0281A
画面・出力には AIX0281A が表示され、lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0281 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1041
確認コード AIX0281B
画面・出力には AIX0281B が表示され、lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0281 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0281C
画面・出力には AIX0281C が表示され、lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0281 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0281A が画面・出力に表示されること
② ステップ2 の AIX0281B が画面・出力に表示されること
③ ステップ3 の AIX0281C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0138"><h3>lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0341</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第三百四十一観点 LVM で lslv は 運用引継ぎ を点検します（運用第三百四十一）（第三百四十一観点）。第三百四十一観点 確認時には MIRROR WRITE CONSISTENCY と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第三百四十一）（第三百四十一観点）。第三百四十一観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第三百四十一観点）。第三百四十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0341へ書きます（第三百四十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0341を保守記録に説明する必要があります。fsck 容量確認 ファイルシステム使用率 0342と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はJFS2でfsckを用い・ファイルシステム使用率 とファイルシステム属性を確認する。</li><li>B. 仕様上の役割はネットワークでchdev -l en0 -aを用い・EtherChannelである。</li><li>C. 仕様上の役割はLVMでlslvを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 仕様上の役割はSRCとログでsyslog_ssw -rを用い・syslog.conf とSRCサブシステム表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「LVMでlslvを用い、MIRROR WRITE CONSISTENCY」に対応する項目はWRITE CONSISTENCY（運用・lslv）です。運用引に関するLVMの仕様は「LVMでlslvを用い、MIRROR WRITE」で、確認対象はls・運用引です。容量・ファ・fsckのA:は「JFS2でfsckを用い、ファイルシステム使用率」を述べ、対象は容量確認 ファイルシステム使用率（容量・fsck）です。障害切・chdeのB:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は障害切り分け EtherChanne（障害・chde）です。起動・syslのD:は「SRCとログでsyslog_ssw -rを用い」を述べ、対象は起動確認 syslog.conf（起動・sysl）です。「lslv」は「LVMでlslvを用い、MIRROR WRITE」を指し、WRITE CONSISTENCYではls・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0341</strong></p><p>検証目的: LVMのlslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0341について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM運用引継ぎ101-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40341        rootvg          active
hdisk1          00f6a1b2c3d50341        datavg          active
確認コード AIX0341A
画面・出力には AIX0341A が表示され、lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0341 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1101
確認コード AIX0341B
画面・出力には AIX0341B が表示され、lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0341 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0341C
画面・出力には AIX0341C が表示され、lslv 運用引継ぎ MIRROR WRITE CONSISTENCY 0341 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0341A が画面・出力に表示されること
② ステップ2 の AIX0341B が画面・出力に表示されること
③ ステップ3 の AIX0341C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0139"><h3>lslv 運用引継ぎ VG STATE 0757</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第七百五十七観点 LVM で lslv は 運用引継ぎ を点検します（運用第七百五十七）（第七百五十七観点）。第七百五十七観点 確認時には VG STATE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第七百五十七）（第七百五十七観点）。第七百五十七観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第七百五十七観点）。第七百五十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0757へ書きます（第七百五十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lslv 運用引継ぎ VG STATE 0757を保守記録に説明する必要があります。fsck 容量確認 agblksize 0758と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はJFS2でfsckを用い・agblksize とファイルシステム属性を確認する。</li><li>B. 保守作業で参照する機能はLVMでlslvを用い・VG STATE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はセキュリティでlssecattr -cを用い・audit class とロール一覧を確認する。</li><li>D. 保守作業で参照する機能は導入と起動でemgr -lを用い・Technology Level とOSレベル表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LVMでlslvを用い、VG STATE とミラーコピー状態を確認する」に対応する項目はVG STATE（運用・lslv）です。運用引に関するLVMの仕様は「LVMでlslvを用い、VG STATE」で、確認対象はls・運用引です。容量・fsckのA:は「JFS2でfsckを用い、agblksize」を述べ、対象は容量確認 agblksize（容量・fsck）です。状態・lsseのC:は「セキュリティでlssecattr -cを用い、audit」を述べ、対象はaudit class（状態・lsse）です。性能・emgrのD:は「導入と起動でemgr -lを用い、Technology Level」を述べ、対象はTechnology Level（性能・emgr）です。「lslv」は「LVMでlslvを用い、VG STATE」を指し、VG STATEではls・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 運用引継ぎ VG STATE 0757</strong></p><p>検証目的: LVMのlslv 運用引継ぎ VG STATE 0757について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM運用引継ぎ037-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40757        rootvg          active
hdisk1          00f6a1b2c3d50757        datavg          active
確認コード AIX0757A
画面・出力には AIX0757A が表示され、lslv 運用引継ぎ VG STATE 0757 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1037
確認コード AIX0757B
画面・出力には AIX0757B が表示され、lslv 運用引継ぎ VG STATE 0757 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0757C
画面・出力には AIX0757C が表示され、lslv 運用引継ぎ VG STATE 0757 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0757A が画面・出力に表示されること
② ステップ2 の AIX0757B が画面・出力に表示されること
③ ステップ3 の AIX0757C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0140"><h3>lslv 運用引継ぎ VG STATE 0817</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第八百十七観点 LVM で lslv は 運用引継ぎ を点検します（運用第八百十七）（第八百十七観点）。第八百十七観点 確認時には VG STATE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第八百十七）（第八百十七観点）。第八百十七観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第八百十七観点）。第八百十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0817へ書きます（第八百十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lslv 運用引継ぎ VG STATE 0817」を「lsps 属性照合 属性確認」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>B. 保守作業で参照する機能はネットワークでchdev -l en0 -aを用い・EtherChannel とアダプター一覧を確認する。</li><li>C. 保守作業で参照する機能はLVMでlslvを用い・VG STATE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 保守作業で参照する機能は性能管理でlparstat -iを用い・fre とsvmon全体表示を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 運用引・lslvでCの記述「LVMでlslvを用い、VG STATE」に対応する項目はVG STATE（運用・lslv）です。運用引に関するLVMの仕様は「LVMでlslvを用い、VG STATE」で、確認対象はls・運用引です。属性・属性・lspsのA:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は属性照合 属性確認（属性・lsps）です。容量・chdeのB:は「ネットワークでchdev -l en0 -aを用い」を述べ、対象は容量確認 EtherChannel（容量・chde）です。容量・lparのD:は「性能管理でlparstat -iを用い、fre」を述べ、対象は容量確認 fre（容量・lpar）です。「lslv」は「LVMでlslvを用い、VG STATE」を指し、VG STATEではls・運用引に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lslv 運用引継ぎ VG STATE 0817</strong></p><p>検証目的: LVMのlslv 運用引継ぎ VG STATE 0817について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM運用引継ぎ097-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lslv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40817        rootvg          active
hdisk1          00f6a1b2c3d50817        datavg          active
確認コード AIX0817A
画面・出力には AIX0817A が表示され、lslv 運用引継ぎ VG STATE 0817 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1097
確認コード AIX0817B
画面・出力には AIX0817B が表示され、lslv 運用引継ぎ VG STATE 0817 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0817C
画面・出力には AIX0817C が表示され、lslv 運用引継ぎ VG STATE 0817 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0817A が画面・出力に表示されること
② ステップ2 の AIX0817B が画面・出力に表示されること
③ ステップ3 の AIX0817C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0141"><h3>lspv 一覧確認 状態確認</h3><p class="kb-meta">分類: LVM ・ 難易度: 初級</p><p>第百四十一観点 LVM で lspv は 一覧確認 を点検します（運用第百四十一）（第百四十一観点）。第百四十一観点 確認時には 状態確認 と PVID 欄 の対応を同じ資料上で追えることを前提にします（資料第百四十一）（第百四十一観点）。第百四十一観点 lspv の出力と取得時刻を同じ確認票に置き、PVID の誤読 を避ける判断根拠を説明可能にします（第百四十一観点）。第百四十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0141へ書きます（第百四十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lspv 一覧確認 状態確認」を「lsvg 詳細確認 詳細表示」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>B. 仕様上の役割はデバイス管理でbootinfo -B hdisk0を用い・location code とODM属性を確認する。</li><li>C. 仕様上の役割はネットワークでroute -n getを用い・Media Speed Runningである。</li><li>D. 仕様上の役割は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Dの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は一覧確認 状態確認（一覧・lspv）です。LVMの仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・一覧・状態です。詳細・詳細・lsvgのA:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は詳細確認 詳細表示（詳細・lsvg）です。状態・bootのB:は「デバイス管理でbootinfo -B hdisk0を用い」を述べ、対象はlocation code（状態・boot）です。起動・routのC:は「ネットワークでroute -n getを用い、Media」を述べ、対象はSpeed Running（起動・rout）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、一覧確認 状態確認ではls・一覧・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 一覧確認 状態確認</strong></p><p>検証目的: LVMのlspv 一覧確認 状態確認について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、LVMの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d4e01        rootvg          active
hdisk1          00f6a1b2c3d5e01        datavg          active
画面・出力には hdisk0 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。PVID 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1092
画面・出力には VOLUME が含まれ、lspv 一覧確認 状態確認の証跡を確認できます。
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


<section class="kb-item" id="c01-i0142"><h3>lspv 容量確認 MIRROR WRITE CONSISTENCY 0258</h3><p class="kb-meta">分類: LVM ・ 難易度: 初級</p><p>第二百五十八観点 LVM で lspv は 容量確認 を点検します（運用第二百五十八）（第二百五十八観点）。第二百五十八観点 確認時には MIRROR WRITE CONSISTENCY と 物理ボリューム一覧 の対応を同じ資料上で追えることを前提にします（資料第二百五十八）（第二百五十八観点）。第二百五十八観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、stale区画の見落とし を避ける判断根拠を説明可能にします（第二百五十八観点）。第二百五十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0258へ書きます（第二百五十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lspv 容量確認 MIRROR WRITE CONSISTENCY 0258の役割を調べています。chfs 性能確認 log=INLINE 0259の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 機能の説明としてはJFS2でchfsを用い・log=INLINE と内部スナップショットを確認する。</li><li>B. 機能の説明としてはネットワークでroute -n getを用い・Gateway と経路表を確認する。</li><li>C. 機能の説明としてはLVMでlspvを用い・MIRROR WRITE CONSISTENCY と物理ボリューム一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 機能の説明としては物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。lspv 詳細確認 装置一覧固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「LVMでlspvを用い、MIRROR WRITE CONSISTENCY」に対応する項目はWRITE CONSISTENCY（容量・lspv）です。容量に関するLVMの仕様は「LVMでlspvを用い、MIRROR WRITE」で、確認対象はls・容量です。性能・chfsのA:は「JFS2でchfsを用い、log=INLINE」を述べ、対象は性能確認 log=INLINE（性能・chfs）です。障害切・routのB:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は障害切り分け Gateway（障害・rout）です。詳細・装置・lspvのD:は「物理ボリュームの PVID、所属ボリュームグループ」を述べ、対象は詳細確認 装置一覧（詳細・lspv）です。「lspv」は「LVMでlspvを用い、MIRROR WRITE」を指し、WRITE CONSISTENCYではls・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 容量確認 MIRROR WRITE CONSISTENCY 0258</strong></p><p>検証目的: LVMのlspv 容量確認 MIRROR WRITE CONSISTENCY 0258について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM容量確認018-03</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40258        rootvg          active
hdisk1          00f6a1b2c3d50258        datavg          active
確認コード AIX0258A
画面・出力には AIX0258A が表示され、lspv 容量確認 MIRROR WRITE CONSISTENCY 0258 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1018
確認コード AIX0258B
画面・出力には AIX0258B が表示され、lspv 容量確認 MIRROR WRITE CONSISTENCY 0258 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0258C
画面・出力には AIX0258C が表示され、lspv 容量確認 MIRROR WRITE CONSISTENCY 0258 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0258A が画面・出力に表示されること
② ステップ2 の AIX0258B が画面・出力に表示されること
③ ステップ3 の AIX0258C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0143"><h3>lspv 容量確認 VG STATE 0734</h3><p class="kb-meta">分類: LVM ・ 難易度: 初級</p><p>第七百三十四観点 LVM で lspv は 容量確認 を点検します（運用第七百三十四）（第七百三十四観点）。第七百三十四観点 確認時には VG STATE と 物理ボリューム一覧 の対応を同じ資料上で追えることを前提にします（資料第七百三十四）（第七百三十四観点）。第七百三十四観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、stale区画の見落とし を避ける判断根拠を説明可能にします（第七百三十四観点）。第七百三十四観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0734へ書きます（第七百三十四観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lspv 容量確認 VG STATE 0734に関する障害切り分けの前提を確認しています。chfs 性能確認 isnapshot 0735の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はJFS2でchfsを用い・isnapshot と内部スナップショットを確認する。</li><li>B. 障害切り分けに用いる役割はセキュリティでlsattr -E -l sys0 -aを用い・enhanced_RBACである。</li><li>C. 障害切り分けに用いる役割はLVMでlspvを用い・VG STATE と物理ボリューム一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 障害切り分けに用いる役割は導入と起動でoslevel -sを用い・fileset level とfileset一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「LVMでlspvを用い、VG STATE と物理ボリューム一覧を確認する」に対応する項目はVG STATE（容量・lspv）です。容量に関するLVMの仕様は「LVMでlspvを用い、VG STATE」で、確認対象はls・容量です。性能・chfsのA:は「JFS2でchfsを用い、isnapshot」を述べ、対象は性能確認 isnapshot（性能・chfs）です。状態・lsatのB:は「セキュリティでlsattr -E -l sys0 -aを用い」を述べ、対象は状態確認 enhanced_RBAC（状態・lsat）です。起動・osleのD:は「導入と起動でoslevel -sを用い、fileset level」を述べ、対象はfileset level（起動・osle）です。「lspv」は「LVMでlspvを用い、VG STATE」を指し、VG STATEではls・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 容量確認 VG STATE 0734</strong></p><p>検証目的: LVMのlspv 容量確認 VG STATE 0734について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM容量確認014-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40734        rootvg          active
hdisk1          00f6a1b2c3d50734        datavg          active
確認コード AIX0734A
画面・出力には AIX0734A が表示され、lspv 容量確認 VG STATE 0734 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1014
確認コード AIX0734B
画面・出力には AIX0734B が表示され、lspv 容量確認 VG STATE 0734 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0734C
画面・出力には AIX0734C が表示され、lspv 容量確認 VG STATE 0734 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0734A が画面・出力に表示されること
② ステップ2 の AIX0734B が画面・出力に表示されること
③ ステップ3 の AIX0734C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0144"><h3>lspv 状態確認 LV STATE 0417</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第四百十七観点 LVM で lspv は 状態確認 を点検します（運用第四百十七）（第四百十七観点）。第四百十七観点 確認時には LV STATE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第四百十七）（第四百十七観点）。第四百十七観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第四百十七観点）。第四百十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0417へ書きます（第四百十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lspv 状態確認 LV STATE 0417」を「chfs 構成照合 isnapshot 0418」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はJFS2でchfsを用い・isnapshot とファイルシステム属性を確認する。</li><li>B. 運用時に利用する技術的役割はLVMでlspvを用い・LV STATE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はネットワークでcfgmgrを用い・MTU とEthernet統計を確認する。</li><li>D. 運用時に利用する技術的役割は導入と起動でoslevel -sを用い・fileset level とOSレベル表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LVMでlspvを用い、LV STATE とミラーコピー状態を確認する」に対応する項目はLV STATE（状態・lspv）です。状態に関するLVMの仕様は「LVMでlspvを用い、LV STATE」で、確認対象はls・状態です。構成・chfsのA:は「JFS2でchfsを用い、isnapshot」を述べ、対象は構成照合 isnapshot（構成・chfs）です。性能・cfgmのC:は「ネットワークでcfgmgrを用い、MTU」を述べ、対象は性能確認 MTU（性能・cfgm）です。変更前・osleのD:は「導入と起動でoslevel -sを用い、fileset level」を述べ、対象はfileset level（変更・osle）です。「lspv」は「LVMでlspvを用い、LV STATE」を指し、LV STATEではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 状態確認 LV STATE 0417</strong></p><p>検証目的: LVMのlspv 状態確認 LV STATE 0417について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM状態確認057-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40417        rootvg          active
hdisk1          00f6a1b2c3d50417        datavg          active
確認コード AIX0417A
画面・出力には AIX0417A が表示され、lspv 状態確認 LV STATE 0417 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1057
確認コード AIX0417B
画面・出力には AIX0417B が表示され、lspv 状態確認 LV STATE 0417 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0417C
画面・出力には AIX0417C が表示され、lspv 状態確認 LV STATE 0417 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0417A が画面・出力に表示されること
② ステップ2 の AIX0417B が画面・出力に表示されること
③ ステップ3 の AIX0417C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0145"><h3>lspv 状態確認 LV STATE 0477</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第四百七十七観点 LVM で lspv は 状態確認 を点検します（運用第四百七十七）（第四百七十七観点）。第四百七十七観点 確認時には LV STATE と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第四百七十七）（第四百七十七観点）。第四百七十七観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第四百七十七観点）。第四百七十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0477へ書きます（第四百七十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lspv 状態確認 LV STATE 0477を保守記録に説明する必要があります。chfs 構成照合 isnapshot 0478と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はJFS2でchfsを用い・isnapshot とファイルシステム属性を確認する。</li><li>B. 運用時に利用する技術的役割はLVMでlspvを用い・LV STATE とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 運用時に利用する技術的役割はネットワークでcfgmgrを用い・MTU とEthernet統計を確認する。</li><li>D. 運用時に利用する技術的役割はSRCとログでstartsrc -s syslogdを用い・Status とSRCサブシステム表示を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Bの記述「LVMでlspvを用い、LV STATE とミラーコピー状態を確認する」に対応する項目はLV STATE（状態・lspv）です。状態に関するLVMの仕様は「LVMでlspvを用い、LV STATE」で、確認対象はls・状態です。構成・chfsのA:は「JFS2でchfsを用い、isnapshot」を述べ、対象は構成照合 isnapshot（構成・chfs）です。性能・cfgmのC:は「ネットワークでcfgmgrを用い、MTU」を述べ、対象は性能確認 MTU（性能・cfgm）です。変更後・starのD:は「SRCとログでstartsrc -s syslogdを用い」を述べ、対象は変更後確認 Status（変更・star）です。「lspv」は「LVMでlspvを用い、LV STATE」を指し、LV STATEではls・状態に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 状態確認 LV STATE 0477</strong></p><p>検証目的: LVMのlspv 状態確認 LV STATE 0477について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM状態確認117-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40477        rootvg          active
hdisk1          00f6a1b2c3d50477        datavg          active
確認コード AIX0477A
画面・出力には AIX0477A が表示され、lspv 状態確認 LV STATE 0477 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1117
確認コード AIX0477B
画面・出力には AIX0477B が表示され、lspv 状態確認 LV STATE 0477 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0477C
画面・出力には AIX0477C が表示され、lspv 状態確認 LV STATE 0477 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0477A が画面・出力に表示されること
② ステップ2 の AIX0477B が画面・出力に表示されること
③ ステップ3 の AIX0477C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0146"><h3>lspv 監査記録 MIRROR WRITE CONSISTENCY 0387</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第三百八十七観点 LVM で lspv は 監査記録 を点検します（運用第三百八十七）（第三百八十七観点）。第三百八十七観点 確認時には MIRROR WRITE CONSISTENCY と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第三百八十七）（第三百八十七観点）。第三百八十七観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第三百八十七観点）。第三百八十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0387へ書きます（第三百八十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lspv 監査記録 MIRROR WRITE CONSISTENCY 0387について構成や状態を確認します。chfs 運用引継ぎ ファイルシステム使用率 0388ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはJFS2でchfsを用い・ファイルシステム使用率 とログデバイス設定を確認する。chfs 運用引継ぎ ファイルシステム使用率 0388固有の属性も確認対象に含める。</li><li>B. 状態を読み取るための働きはLVMでlspvを用い・MIRROR WRITE CONSISTENCY とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはネットワークでroute -n getを用い・Gateway とMTU属性を確認する。</li><li>D. 状態を読み取るための働きは導入と起動でoslevel -sを用い・altinst_rootvg と代替ディスク状態を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LVMでlspvを用い、MIRROR WRITE CONSISTENCY」に対応する項目はWRITE CONSISTENCY（監査・lspv）です。監査に関するLVMの仕様は「LVMでlspvを用い、MIRROR WRITE」で、確認対象はls・監査です。運用引・chfsのA:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象は運用引継ぎ ファイルシステム使用率（運用・chfs）です。変更前・routのC:は「ネットワークでroute -n getを用い、Gateway」を述べ、対象は変更前確認 Gateway（変更・rout）です。容量・osleのD:は「導入と起動でoslevel -sを用い、altinst_rootvg」を述べ、対象は容量確認 altinst_rootv（容量・osle）です。「lspv」は「LVMでlspvを用い、MIRROR WRITE」を指し、WRITE CONSISTENCYではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 監査記録 MIRROR WRITE CONSISTENCY 0387</strong></p><p>検証目的: LVMのlspv 監査記録 MIRROR WRITE CONSISTENCY 0387について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM監査記録027-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40387        rootvg          active
hdisk1          00f6a1b2c3d50387        datavg          active
確認コード AIX0387A
画面・出力には AIX0387A が表示され、lspv 監査記録 MIRROR WRITE CONSISTENCY 0387 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1027
確認コード AIX0387B
画面・出力には AIX0387B が表示され、lspv 監査記録 MIRROR WRITE CONSISTENCY 0387 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0387C
画面・出力には AIX0387C が表示され、lspv 監査記録 MIRROR WRITE CONSISTENCY 0387 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0387A が画面・出力に表示されること
② ステップ2 の AIX0387B が画面・出力に表示されること
③ ステップ3 の AIX0387C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0147"><h3>lspv 監査記録 MIRROR WRITE CONSISTENCY 0447</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第四百四十七観点 LVM で lspv は 監査記録 を点検します（運用第四百四十七）（第四百四十七観点）。第四百四十七観点 確認時には MIRROR WRITE CONSISTENCY と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第四百四十七）（第四百四十七観点）。第四百四十七観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第四百四十七観点）。第四百四十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0447へ書きます（第四百四十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lspv 監査記録 MIRROR WRITE CONSISTENCY 0447の設定や表示を読む前に役割を確認します。chfs 運用引継ぎ ファイルシステム使用率 0448ではなく対象を説明しているものはどれですか。</p><ul class="kb-choices"><li>A. 状態を読み取るための働きはJFS2でchfsを用い・ファイルシステム使用率 とログデバイス設定を確認する。</li><li>B. 状態を読み取るための働きはLVMでlspvを用い・MIRROR WRITE CONSISTENCY とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 状態を読み取るための働きはネットワークでcfgmgrを用い・EtherChannel とMTU属性を確認する。</li><li>D. 状態を読み取るための働きは導入と起動でlslpp -Lを用い・mksysb image と代替ディスク状態を確認する。lslpp -L 性能確認 mksysb image 0140固有の属性も確認対象に含める。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LVMでlspvを用い、MIRROR WRITE CONSISTENCY」に対応する項目はWRITE CONSISTENCY（監査・lspv）です。監査に関するLVMの仕様は「LVMでlspvを用い、MIRROR WRITE」で、確認対象はls・監査です。運用引・chfsのA:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象は運用引継ぎ ファイルシステム使用率（運用・chfs）です。変更後・cfgmのC:は「ネットワークでcfgmgrを用い、EtherChannel」を述べ、対象は変更後確認 EtherChannel（変更・cfgm）です。性能・lslpのD:は「導入と起動でlslpp -Lを用い、mksysb image」を述べ、対象はmksysb image（性能・lslp）です。「lspv」は「LVMでlspvを用い、MIRROR WRITE」を指し、WRITE CONSISTENCYではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 監査記録 MIRROR WRITE CONSISTENCY 0447</strong></p><p>検証目的: LVMのlspv 監査記録 MIRROR WRITE CONSISTENCY 0447について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM監査記録087-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40447        rootvg          active
hdisk1          00f6a1b2c3d50447        datavg          active
確認コード AIX0447A
画面・出力には AIX0447A が表示され、lspv 監査記録 MIRROR WRITE CONSISTENCY 0447 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1087
確認コード AIX0447B
画面・出力には AIX0447B が表示され、lspv 監査記録 MIRROR WRITE CONSISTENCY 0447 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0447C
画面・出力には AIX0447C が表示され、lspv 監査記録 MIRROR WRITE CONSISTENCY 0447 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0447A が画面・出力に表示されること
② ステップ2 の AIX0447B が画面・出力に表示されること
③ ステップ3 の AIX0447C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0148"><h3>lspv 障害切り分け LV STATE 0100</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第百観点 LVM で lspv は 障害切り分け を点検します（運用第百）（第百観点）。第百観点 確認時には LV STATE と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第百）（第百観点）。第百観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第百観点）。第百観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0100へ書きます（第百観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lspv 障害切り分け LV STATE 0100の技術的な意味を資料で確認するとき、chfs バックアウト確認 mountguard 0101との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はJFS2でchfsを用い・mountguard とマウントオプションを確認する。</li><li>B. 管理対象との関係を表す説明はネットワークでcfgmgrを用い・MTU とアダプター一覧を確認する。</li><li>C. 管理対象との関係を表す説明はLVMでlspvを用い・LV STATE と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 管理対象との関係を表す説明はJFS2でlogformを用い・isnapshot とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Cの記述「LVMでlspvを用い、LV STATE と論理ボリューム配置を確認する」に対応する項目はLV STATE（障害・lspv）です。障害切に関するLVMの仕様は「LVMでlspvを用い、LV STATE」で、確認対象はls・障害切です。バック・chfsのA:は「JFS2でchfsを用い、mountguard」を述べ、対象はバックアウト確認 mountguar（バッ・chfs）です。構成・cfgmのB:は「ネットワークでcfgmgrを用い、MTU とアダプター一覧を確認する」を述べ、対象は構成照合 MTU（構成・cfgm）です。起動・logfのD:は「JFS2でlogformを用い、isnapshot」を述べ、対象は起動確認 isnapshot（起動・logf）です。「lspv」は「LVMでlspvを用い、LV STATE」を指し、LV STATEではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 障害切り分け LV STATE 0100</strong></p><p>検証目的: LVMのlspv 障害切り分け LV STATE 0100について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM障害切り分け100-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40100        rootvg          active
hdisk1          00f6a1b2c3d50100        datavg          active
確認コード AIX0100A
画面・出力には AIX0100A が表示され、lspv 障害切り分け LV STATE 0100 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1100
確認コード AIX0100B
画面・出力には AIX0100B が表示され、lspv 障害切り分け LV STATE 0100 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。LV STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0100C
画面・出力には AIX0100C が表示され、lspv 障害切り分け LV STATE 0100 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0100A が画面・出力に表示されること
② ステップ2 の AIX0100B が画面・出力に表示されること
③ ステップ3 の AIX0100C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0149"><h3>lspv 障害切り分け STALE PARTITIONS 0576</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第五百七十六観点 LVM で lspv は 障害切り分け を点検します（運用第五百七十六）（第五百七十六観点）。第五百七十六観点 確認時には STALE PARTITIONS と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第五百七十六）（第五百七十六観点）。第五百七十六観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第五百七十六観点）。第五百七十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0576へ書きます（第五百七十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lspv 障害切り分け STALE PARTITIONS 0576を同一分類のchfs バックアウト確認 ファイルシステム使用率 0577と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はJFS2でchfsを用い・ファイルシステム使用率 とマウントオプションを確認する。</li><li>B. 構成を確認する際の意味はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>C. 構成を確認する際の意味はLVMでlspvを用い・STALE PARTITIONS と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 構成を確認する際の意味は導入と起動でlslpp -Lを用い・mksysb image と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「LVMでlspvを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（障害・lspv）です。障害切に関するLVMの仕様は「LVMでlspvを用い、STALE PARTITIONS」で、確認対象はls・障害切です。バック・chfsのA:は「JFS2でchfsを用い、ファイルシステム使用率」を述べ、対象はバックアウト確認 ファイルシステム使（バッ・chfs）です。性能・資料・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は性能確認 資料見出し（性能・lsvg）です。運用引・lslpのD:は「導入と起動でlslpp -Lを用い、mksysb image」を述べ、対象はmksysb image（運用・lslp）です。「lspv」は「LVMでlspvを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 障害切り分け STALE PARTITIONS 0576</strong></p><p>検証目的: LVMのlspv 障害切り分け STALE PARTITIONS 0576について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM障害切り分け096-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40576        rootvg          active
hdisk1          00f6a1b2c3d50576        datavg          active
確認コード AIX0576A
画面・出力には AIX0576A が表示され、lspv 障害切り分け STALE PARTITIONS 0576 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1096
確認コード AIX0576B
画面・出力には AIX0576B が表示され、lspv 障害切り分け STALE PARTITIONS 0576 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0576C
画面・出力には AIX0576C が表示され、lspv 障害切り分け STALE PARTITIONS 0576 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0576A が画面・出力に表示されること
② ステップ2 の AIX0576B が画面・出力に表示されること
③ ステップ3 の AIX0576C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0150"><h3>lspv 障害切り分け 出力比較</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第百五十観点 LVM で lspv は 障害切り分け を点検します（運用第百五十）（第百五十観点）。第百五十観点 確認時には 出力比較 と PVID 欄 の対応を同じ資料上で追えることを前提にします（資料第百五十）（第百五十観点）。第百五十観点 lspv の出力と取得時刻を同じ確認票に置き、PVID の誤読 を避ける判断根拠を説明可能にします（第百五十観点）。第百五十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0150へ書きます（第百五十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lspv 障害切り分け 出力比較」を「lsvg 性能確認 資料見出し」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割は物理ボリュームの PVID・所属ボリュームグループ・状態を表示するコマンドである。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はボリュームグループの構成・状態・論理ボリューム一覧を表示するコマンドである。</li><li>C. 運用時に利用する技術的役割はJFS2でdefragfsを用い・lff と内部スナップショットを確認する。</li><li>D. 運用時に利用する技術的役割はセキュリティでpwdck -n ALLを用い・authorizations とRBAC属性を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「物理ボリュームの PVID、所属ボリュームグループ、状態を表示するコマンドである」に対応する項目は障害切り分け 出力比較（障害・lspv）です。LVMの仕様は「物理ボリュームの PVID、所属ボリュームグループ」で、確認対象はls・障害切です。性能・資料・lsvgのB:は「ボリュームグループの構成、状態、論理ボリューム一覧を表示するコマンド」を述べ、対象は性能確認 資料見出し（性能・lsvg）です。バック・defrのC:は「JFS2でdefragfsを用い、lff」を述べ、対象はバックアウト確認 lff（バッ・defr）です。変更前・pwdcのD:は「セキュリティでpwdck -n ALLを用い」を述べ、対象は変更前確認 authorizatio（変更・pwdc）です。「lspv」は「物理ボリュームの PVID、所属ボリュームグループ」を指し、障害切り分け 出力比較ではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_devicemanagement_en / AIX73_performance_en / AIX73_osmanagement_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lspv 障害切り分け 出力比較</strong></p><p>検証目的: LVMのlspv 障害切り分け 出力比較について、AIX 7.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: AIX 7.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、LVMの対象へ進みます。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lspv
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d4e41        rootvg          active
hdisk1          00f6a1b2c3d5e41        datavg          active
画面・出力には hdisk0 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3の確認画面です。PVID 欄を読むため、対象名を含む操作を入力します。
［操作（入力）］
AIX 7.3 操作画面
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1092
画面・出力には VOLUME が含まれ、lspv 障害切り分け 出力比較の証跡を確認できます。
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


<section class="kb-item" id="c01-i0151"><h3>lsvg -l 変更前確認 PP SIZE 0538</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第五百三十八観点 LVM で lsvg -l は 変更前確認 を点検します（運用第五百三十八）（第五百三十八観点）。第五百三十八観点 確認時には PP SIZE と 物理ボリューム一覧 の対応を同じ資料上で追えることを前提にします（資料第五百三十八）（第五百三十八観点）。第五百三十八観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、stale区画の見落とし を避ける判断根拠を説明可能にします（第五百三十八観点）。第五百三十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0538へ書きます（第五百三十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg -l 変更前確認 PP SIZE 0538の役割を調べています。mount -o remount 変更後確認 lff 0539の説明を混ぜずに採るべき記述はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はJFS2でmount -o remountを用い・lff と内部スナップショットを確認する。</li><li>B. 表示や設定で扱う内容はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>C. 表示や設定で扱う内容はLVMでlsvg -lを用い・PP SIZE と物理ボリューム一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 表示や設定で扱う内容は導入と起動でinstallp -Cを用い・bootlist とfileset一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Cの記述「LVMでlsvg -lを用い、PP SIZE と物理ボリューム一覧を確認する」に対応する項目はPP SIZE（変更・lsvg）です。変更前に関するLVMの仕様は「LVMでlsvg -lを用い、PP SIZE」で、確認対象はls・変更前です。変更後・mounのA:は「JFS2でmount -o remountを用い、lff」を述べ、対象は変更後確認 lff（変更・moun）です。属性・属性・lspsのB:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は属性照合 属性確認（属性・lsps）です。障害切・instのD:は「導入と起動でinstallp -Cを用い、bootlist」を述べ、対象は障害切り分け bootlist（障害・inst）です。「lsvg -l」は「LVMでlsvg -lを用い、PP SIZE」を指し、PP SIZEではls・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg -l 変更前確認 PP SIZE 0538</strong></p><p>検証目的: LVMのlsvg -l 変更前確認 PP SIZE 0538について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM変更前確認058-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40538        rootvg          active
hdisk1          00f6a1b2c3d50538        datavg          active
確認コード AIX0538A
画面・出力には AIX0538A が表示され、lsvg -l 変更前確認 PP SIZE 0538 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1058
確認コード AIX0538B
画面・出力には AIX0538B が表示され、lsvg -l 変更前確認 PP SIZE 0538 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0538C
画面・出力には AIX0538C が表示され、lsvg -l 変更前確認 PP SIZE 0538 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0538A が画面・出力に表示されること
② ステップ2 の AIX0538B が画面・出力に表示されること
③ ステップ3 の AIX0538C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0152"><h3>lsvg -l 変更前確認 PP SIZE 0598</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第五百九十八観点 LVM で lsvg -l は 変更前確認 を点検します（運用第五百九十八）（第五百九十八観点）。第五百九十八観点 確認時には PP SIZE と 物理ボリューム一覧 の対応を同じ資料上で追えることを前提にします（資料第五百九十八）（第五百九十八観点）。第五百九十八観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、stale区画の見落とし を避ける判断根拠を説明可能にします（第五百九十八観点）。第五百九十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0598へ書きます（第五百九十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg -l 変更前確認 PP SIZE 0598に関する障害切り分けの前提を確認しています。mount -o remount 変更後確認 lff 0599の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 表示や設定で扱う内容はLVMでlsvg -lを用い・PP SIZE と物理ボリューム一覧を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 表示や設定で扱う内容はJFS2でmount -o remountを用い・lff と内部スナップショットを確認する。</li><li>C. 表示や設定で扱う内容はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>D. 表示や設定で扱う内容は導入と起動でemgr -lを用い・altinst_rootvg とfileset一覧を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「LVMでlsvg -lを用い、PP SIZE と物理ボリューム一覧を確認する」に対応する項目はPP SIZE（変更・lsvg）です。変更前に関するLVMの仕様は「LVMでlsvg -lを用い、PP SIZE」で、確認対象はls・変更前です。変更後・mounのB:は「JFS2でmount -o remountを用い、lff」を述べ、対象は変更後確認 lff（変更・moun）です。性能・停止・lspsのC:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は性能確認 停止確認（性能・lsps）です。バック・emgrのD:は「導入と起動でemgr -lを用い、altinst_rootvg」を述べ、対象はバックアウト確認 altinst_r（バッ・emgr）です。「lsvg -l」は「LVMでlsvg -lを用い、PP SIZE」を指し、PP SIZEではls・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg -l 変更前確認 PP SIZE 0598</strong></p><p>検証目的: LVMのlsvg -l 変更前確認 PP SIZE 0598について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM変更前確認118-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40598        rootvg          active
hdisk1          00f6a1b2c3d50598        datavg          active
確認コード AIX0598A
画面・出力には AIX0598A が表示され、lsvg -l 変更前確認 PP SIZE 0598 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1118
確認コード AIX0598B
画面・出力には AIX0598B が表示され、lsvg -l 変更前確認 PP SIZE 0598 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0598C
画面・出力には AIX0598C が表示され、lsvg -l 変更前確認 PP SIZE 0598 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0598A が画面・出力に表示されること
② ステップ2 の AIX0598B が画面・出力に表示されること
③ ステップ3 の AIX0598C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0153"><h3>lsvg -l 変更前確認 VG STATE 0062</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第六十二観点 LVM で lsvg -l は 変更前確認 を点検します（運用第六十二）（第六十二観点）。第六十二観点 確認時には VG STATE と 物理ボリューム一覧 の対応を同じ資料上で追えることを前提にします（資料第六十二）（第六十二観点）。第六十二観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、stale区画の見落とし を避ける判断根拠を説明可能にします（第六十二観点）。第六十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0062へ書きます（第六十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg -l 変更前確認 VG STATE 0062に関する障害切り分けの前提を確認しています。mount -o remount 変更後確認 isnapshot 0063の機能を混同しない選択肢はどれですか。</p><ul class="kb-choices"><li>A. 障害切り分けに用いる役割はJFS2でmount -o remountを用い・isnapshot と内部スナップショットを確認する。</li><li>B. 障害切り分けに用いる役割はネットワークでifconfig en0を用い・Media Speed Running と経路表を確認する。</li><li>C. 障害切り分けに用いる役割はJFS2でcrfsを用い・agblksize と内部スナップショットを確認する。</li><li>D. 障害切り分けに用いる役割はLVMでlsvg -lを用い・VG STATE と物理ボリューム一覧を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「LVMでlsvg -lを用い、VG STATE と物理ボリューム一覧を確認する」に対応する項目はVG STATE（変更・lsvg）です。LVMの仕様は「LVMでlsvg -lを用い、VG STATE」で、確認対象はls・変更前です。変更後・mounのA:は「JFS2でmount -o remountを用い」を述べ、対象は変更後確認 isnapshot（変更・moun）です。属性・ifcoのB:は「ネットワークでifconfig en0を用い、Media」を述べ、対象はSpeed Running（属性・ifco）です。容量・crfsのC:は「JFS2でcrfsを用い、agblksize」を述べ、対象は容量確認 agblksize（容量・crfs）です。「lsvg -l」は「LVMでlsvg -lを用い、VG STATE」を指し、VG STATEではls・変更前に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg -l 変更前確認 VG STATE 0062</strong></p><p>検証目的: LVMのlsvg -l 変更前確認 VG STATE 0062について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM変更前確認062-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40062        rootvg          active
hdisk1          00f6a1b2c3d50062        datavg          active
確認コード AIX0062A
画面・出力には AIX0062A が表示され、lsvg -l 変更前確認 VG STATE 0062 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1062
確認コード AIX0062B
画面・出力には AIX0062B が表示され、lsvg -l 変更前確認 VG STATE 0062 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0062C
画面・出力には AIX0062C が表示され、lsvg -l 変更前確認 VG STATE 0062 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0062A が画面・出力に表示されること
② ステップ2 の AIX0062B が画面・出力に表示されること
③ ステップ3 の AIX0062C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0154"><h3>lsvg -l 容量確認 PVID 0508</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第五百八観点 LVM で lsvg -l は 容量確認 を点検します（運用第五百八）（第五百八観点）。第五百八観点 確認時には PVID と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第五百八）（第五百八観点）。第五百八観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第五百八観点）。第五百八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0508へ書きます（第五百八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg -l 容量確認 PVID 0508の技術的な意味を資料で確認するとき、mount -o remount 性能確認 agblksize 0509との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はJFS2でmount -o remountを用い・agblksize とマウントオプションを確認する。</li><li>B. 管理対象との関係を表す説明はLVMでlsvg -lを用い・PVID と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はネットワークでlsdev -Cc adapterを用い・EtherChannel とアダプター一覧を確認する。</li><li>D. 管理対象との関係を表す説明は導入と起動でinstallp -Cを用い・Technology Level と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LVMでlsvg -lを用い、PVID と論理ボリューム配置を確認する」に対応する項目は容量確認 PVID（容量・lsvg）です。容量に関するLVMの仕様は「LVMでlsvg -lを用い、PVID と論理ボリューム配置を確認す」で、確認対象はls・容量です。性能・mounのA:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 agblksize（性能・moun）です。障害切・lsdeのC:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は障害切り分け EtherChanne（障害・lsde）です。起動・instのD:は「導入と起動でinstallp -Cを用い、Technology」を述べ、対象はTechnology Level（起動・inst）です。「lsvg -l」は「LVMでlsvg -lを用い、PVID と論理ボリューム配置を確認す」を指し、容量確認 PVIDではls・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg -l 容量確認 PVID 0508</strong></p><p>検証目的: LVMのlsvg -l 容量確認 PVID 0508について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM容量確認028-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40508        rootvg          active
hdisk1          00f6a1b2c3d50508        datavg          active
確認コード AIX0508A
画面・出力には AIX0508A が表示され、lsvg -l 容量確認 PVID 0508 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1028
確認コード AIX0508B
画面・出力には AIX0508B が表示され、lsvg -l 容量確認 PVID 0508 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0508C
画面・出力には AIX0508C が表示され、lsvg -l 容量確認 PVID 0508 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0508A が画面・出力に表示されること
② ステップ2 の AIX0508B が画面・出力に表示されること
③ ステップ3 の AIX0508C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0155"><h3>lsvg -l 容量確認 PVID 0568</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第五百六十八観点 LVM で lsvg -l は 容量確認 を点検します（運用第五百六十八）（第五百六十八観点）。第五百六十八観点 確認時には PVID と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第五百六十八）（第五百六十八観点）。第五百六十八観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第五百六十八観点）。第五百六十八観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0568へ書きます（第五百六十八観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg -l 容量確認 PVID 0568を同一分類のmount -o remount 性能確認 agblksize 0569と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はLVMでlsvg -lを用い・PVID と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 管理対象との関係を表す説明はJFS2でmount -o remountを用い・agblksize とマウントオプションを確認する。</li><li>C. 管理対象との関係を表す説明はページングスペースの名前・サイズ・使用率・活動状態を表示するコマンドである。</li><li>D. 管理対象との関係を表す説明は導入と起動でemgr -lを用い・fileset level と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「LVMでlsvg -lを用い、PVID と論理ボリューム配置を確認する」に対応する項目は容量確認 PVID（容量・lsvg）です。容量に関するLVMの仕様は「LVMでlsvg -lを用い、PVID と論理ボリューム配置を確認す」で、確認対象はls・容量です。性能・mounのB:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 agblksize（性能・moun）です。障害切・lspsのC:は「ページングスペースの名前、サイズ、使用率、活動状態を表示するコマンド」を述べ、対象は障害切り分け ファイルセット（障害・lsps）です。属性・emgrのD:は「導入と起動でemgr -lを用い、fileset level」を述べ、対象はfileset level（属性・emgr）です。「lsvg -l」は「LVMでlsvg -lを用い、PVID と論理ボリューム配置を確認す」を指し、容量確認 PVIDではls・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg -l 容量確認 PVID 0568</strong></p><p>検証目的: LVMのlsvg -l 容量確認 PVID 0568について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM容量確認088-05</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40568        rootvg          active
hdisk1          00f6a1b2c3d50568        datavg          active
確認コード AIX0568A
画面・出力には AIX0568A が表示され、lsvg -l 容量確認 PVID 0568 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1088
確認コード AIX0568B
画面・出力には AIX0568B が表示され、lsvg -l 容量確認 PVID 0568 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0568C
画面・出力には AIX0568C が表示され、lsvg -l 容量確認 PVID 0568 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0568A が画面・出力に表示されること
② ステップ2 の AIX0568B が画面・出力に表示されること
③ ステップ3 の AIX0568C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0156"><h3>lsvg -l 容量確認 STALE PARTITIONS 0032</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第三十二観点 LVM で lsvg -l は 容量確認 を点検します（運用第三十二）（第三十二観点）。第三十二観点 確認時には STALE PARTITIONS と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第三十二）（第三十二観点）。第三十二観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第三十二観点）。第三十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0032へ書きます（第三十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg -l 容量確認 STALE PARTITIONS 0032を同一分類のmount -o remount 性能確認 ファイルシステム使用率 0033と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はJFS2でmount -o remountを用い・ファイルシステム使用率 とマウントオプションを確認する。</li><li>B. コマンドまたは機能の用途はLVMでlsvg -lを用い・STALE PARTITIONS と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. コマンドまたは機能の用途はネットワークでlsdev -Cc adapterを用い・Destination とアダプター一覧を確認する。</li><li>D. コマンドまたは機能の用途はJFS2でcrfsを用い・lff とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LVMでlsvg -lを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（容量・lsvg）です。LVMの仕様は「LVMでlsvg -lを用い、STALE PARTITIONS」で、確認対象はls・容量です。性能・ファ・mounのA:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 ファイルシステム使用率（性能・moun）です。障害切・lsdeのC:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は障害切り分け Destination（障害・lsde）です。変更前・crfsのD:は「JFS2でcrfsを用い、lff とマウントオプションを確認する」を述べ、対象は変更前確認 lff（変更・crfs）です。「lsvg -l」は「LVMでlsvg -lを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではls・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg -l 容量確認 STALE PARTITIONS 0032</strong></p><p>検証目的: LVMのlsvg -l 容量確認 STALE PARTITIONS 0032について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM容量確認032-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40032        rootvg          active
hdisk1          00f6a1b2c3d50032        datavg          active
確認コード AIX0032A
画面・出力には AIX0032A が表示され、lsvg -l 容量確認 STALE PARTITIONS 0032 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1032
確認コード AIX0032B
画面・出力には AIX0032B が表示され、lsvg -l 容量確認 STALE PARTITIONS 0032 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0032C
画面・出力には AIX0032C が表示され、lsvg -l 容量確認 STALE PARTITIONS 0032 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0032A が画面・出力に表示されること
② ステップ2 の AIX0032B が画面・出力に表示されること
③ ステップ3 の AIX0032C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0157"><h3>lsvg -l 容量確認 STALE PARTITIONS 0092</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第九十二観点 LVM で lsvg -l は 容量確認 を点検します（運用第九十二）（第九十二観点）。第九十二観点 確認時には STALE PARTITIONS と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第九十二）（第九十二観点）。第九十二観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第九十二観点）。第九十二観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0092へ書きます（第九十二観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg -l 容量確認 STALE PARTITIONS 0092の技術的な意味を資料で確認するとき、mount -o remount 性能確認 ファイルシステム使用率 0093との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. コマンドまたは機能の用途はLVMでlsvg -lを用い・STALE PARTITIONS と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. コマンドまたは機能の用途はJFS2でmount -o remountを用い・ファイルシステム使用率 とマウントオプションを確認する。</li><li>C. コマンドまたは機能の用途はネットワークでifconfig en0を用い・Gateway とアダプター一覧を確認する。</li><li>D. コマンドまたは機能の用途はJFS2でcrfsを用い・lff とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「LVMでlsvg -lを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（容量・lsvg）です。容量に関するLVMの仕様は「LVMでlsvg -lを用い、STALE PARTITIONS」で、確認対象はls・容量です。性能・ファ・mounのB:は「JFS2でmount -o remountを用い」を述べ、対象は性能確認 ファイルシステム使用率（性能・moun）です。バック・ifcoのC:は「ネットワークでifconfig en0を用い、Gateway」を述べ、対象はバックアウト確認 Gateway（バッ・ifco）です。変更前・crfsのD:は「JFS2でcrfsを用い、lff とマウントオプションを確認する」を述べ、対象は変更前確認 lff（変更・crfs）です。「lsvg -l」は「LVMでlsvg -lを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではls・容量に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg -l 容量確認 STALE PARTITIONS 0092</strong></p><p>検証目的: LVMのlsvg -l 容量確認 STALE PARTITIONS 0092について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM容量確認092-01</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40092        rootvg          active
hdisk1          00f6a1b2c3d50092        datavg          active
確認コード AIX0092A
画面・出力には AIX0092A が表示され、lsvg -l 容量確認 STALE PARTITIONS 0092 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1092
確認コード AIX0092B
画面・出力には AIX0092B が表示され、lsvg -l 容量確認 STALE PARTITIONS 0092 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0092C
画面・出力には AIX0092C が表示され、lsvg -l 容量確認 STALE PARTITIONS 0092 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0092A が画面・出力に表示されること
② ステップ2 の AIX0092B が画面・出力に表示されること
③ ステップ3 の AIX0092C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0158"><h3>lsvg -l 監査記録 PVID 0697</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第六百九十七観点 LVM で lsvg -l は 監査記録 を点検します（運用第六百九十七）（第六百九十七観点）。第六百九十七観点 確認時には PVID と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第六百九十七）（第六百九十七観点）。第六百九十七観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第六百九十七観点）。第六百九十七観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0697へ書きます（第六百九十七観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lsvg -l 監査記録 PVID 0697」を「syslog_ssw -c 運用引継ぎ Subsystem 0698」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はSRCとログでsyslog_ssw -cを用い・Subsystem とSRCサブシステム表示を確認する。</li><li>B. 保守作業で参照する機能はセキュリティでrbacqry -u user1 -Tを用い・roles とロール一覧を確認する。</li><li>C. 保守作業で参照する機能は導入と起動でemgr -lを用い・Technology Level とOSレベル表示を確認する。</li><li>D. 保守作業で参照する機能はLVMでlsvg -lを用い・PVID とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Dの記述「LVMでlsvg -lを用い、PVID とミラーコピー状態を確認する」に対応する項目は監査記録 PVID（監査・lsvg）です。監査に関するLVMの仕様は「LVMでlsvg -lを用い、PVID とミラーコピー状態を確認する」で、確認対象はls・監査です。運用引・syslのA:は「SRCとログでsyslog_ssw -cを用い、Subsystem」を述べ、対象は運用引継ぎ Subsystem（運用・sysl）です。属性・rbacのB:は「セキュリティでrbacqry -u user1 -Tを用い」を述べ、対象は属性確認 roles（属性・rbac）です。性能・emgrのC:は「導入と起動でemgr -lを用い、Technology Level」を述べ、対象はTechnology Level（性能・emgr）です。「lsvg -l」は「LVMでlsvg -lを用い、PVID とミラーコピー状態を確認する」を指し、監査記録 PVIDではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg -l 監査記録 PVID 0697</strong></p><p>検証目的: LVMのlsvg -l 監査記録 PVID 0697について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM監査記録097-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40697        rootvg          active
hdisk1          00f6a1b2c3d50697        datavg          active
確認コード AIX0697A
画面・出力には AIX0697A が表示され、lsvg -l 監査記録 PVID 0697 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1097
確認コード AIX0697B
画面・出力には AIX0697B が表示され、lsvg -l 監査記録 PVID 0697 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PVID を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0697C
画面・出力には AIX0697C が表示され、lsvg -l 監査記録 PVID 0697 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0697A が画面・出力に表示されること
② ステップ2 の AIX0697B が画面・出力に表示されること
③ ステップ3 の AIX0697C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0159"><h3>lsvg -l 監査記録 STALE PARTITIONS 0221</h3><p class="kb-meta">分類: LVM ・ 難易度: 上級</p><p>第二百二十一観点 LVM で lsvg -l は 監査記録 を点検します（運用第二百二十一）（第二百二十一観点）。第二百二十一観点 確認時には STALE PARTITIONS と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第二百二十一）（第二百二十一観点）。第二百二十一観点 lsvg -l rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第二百二十一観点）。第二百二十一観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0221へ書きます（第二百二十一観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg -l 監査記録 STALE PARTITIONS 0221を保守記録に説明する必要があります。syslog_ssw -c 運用引継ぎ TIMESTAMP 0222と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 仕様上の役割はLVMでlsvg -lを用い・STALE PARTITIONS とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 仕様上の役割はSRCとログでsyslog_ssw -cを用い・TIMESTAMP とSRCサブシステム表示を確認する。</li><li>C. 仕様上の役割はネットワークでifconfig en0を用い・Gateway とEthernet統計を確認する。</li><li>D. 仕様上の役割はSRCとログでlssrc -s syslogdを用い・IDENTIFIERである。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> Aの記述「LVMでlsvg -lを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（監査・lsvg）です。監査に関するLVMの仕様は「LVMでlsvg -lを用い、STALE PARTITIONS」で、確認対象はls・監査です。運用引・syslのB:は「SRCとログでsyslog_ssw -cを用い、TIMESTAMP」を述べ、対象は運用引継ぎ TIMESTAMP（運用・sysl）です。変更後・ifcoのC:は「ネットワークでifconfig en0を用い、Gateway」を述べ、対象は変更後確認 Gateway（変更・ifco）です。状態・lssrのD:は「SRCとログでlssrc -s syslogdを用い」を述べ、対象は状態確認 IDENTIFIER（状態・lssr）です。「lsvg -l」は「LVMでlsvg -lを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではls・監査に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg -l 監査記録 STALE PARTITIONS 0221</strong></p><p>検証目的: LVMのlsvg -l 監査記録 STALE PARTITIONS 0221について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM監査記録101-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40221        rootvg          active
hdisk1          00f6a1b2c3d50221        datavg          active
確認コード AIX0221A
画面・出力には AIX0221A が表示され、lsvg -l 監査記録 STALE PARTITIONS 0221 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1101
確認コード AIX0221B
画面・出力には AIX0221B が表示され、lsvg -l 監査記録 STALE PARTITIONS 0221 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0221C
画面・出力には AIX0221C が表示され、lsvg -l 監査記録 STALE PARTITIONS 0221 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0221A が画面・出力に表示されること
② ステップ2 の AIX0221B が画面・出力に表示されること
③ ステップ3 の AIX0221C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0160"><h3>lsvg -l 起動確認 VG STATE 0379</h3><p class="kb-meta">分類: LVM ・ 難易度: 初級</p><p>第三百七十九観点 LVM で lsvg -l は 起動確認 を点検します（運用第三百七十九）（第三百七十九観点）。第三百七十九観点 確認時には VG STATE と ボリュームグループ属性 の対応を同じ資料上で追えることを前提にします（資料第三百七十九）（第三百七十九観点）。第三百七十九観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、boot論理ボリュームの連続配置確認漏れ を避ける判断根拠を説明可能にします（第三百七十九観点）。第三百七十九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0379へ書きます（第三百七十九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg -l 起動確認 VG STATE 0379について構成や状態を確認します。mount -o remount 属性確認 agblksize 0380ではなく対象機能を表す記述はどれですか。</p><ul class="kb-choices"><li>A. 対象資源に対する働きはJFS2でmount -o remountを用い・agblksize とログデバイス設定を確認する。</li><li>B. 対象資源に対する働きはネットワークでlsdev -Cc adapterを用い・Link Status とMTU属性を確認する。</li><li>C. 対象資源に対する働きはLVMでlsvg -lを用い・VG STATE とボリュームグループ属性を確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 対象資源に対する働きは導入と起動でinstallp -Cを用い・Technology Level と代替ディスク状態を確認する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> Cの記述「LVMでlsvg -lを用い、VG STATE とボリュームグループ属性を確認する」に対応する項目はVG STATE（起動・lsvg）です。起動に関するLVMの仕様は「LVMでlsvg -lを用い、VG STATE」で、確認対象はls・起動です。属性・mounのA:は「JFS2でmount -o remountを用い」を述べ、対象は属性確認 agblksize（属性・moun）です。監査・lsdeのB:は「ネットワークでlsdev -Cc adapterを用い、Link」を述べ、対象はLink Status（監査・lsde）です。状態・instのD:は「導入と起動でinstallp -Cを用い、Technology」を述べ、対象はTechnology Level（状態・inst）です。「lsvg -l」は「LVMでlsvg -lを用い、VG STATE」を指し、VG STATEではls・起動に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg -l 起動確認 VG STATE 0379</strong></p><p>検証目的: LVMのlsvg -l 起動確認 VG STATE 0379について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM起動確認019-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40379        rootvg          active
hdisk1          00f6a1b2c3d50379        datavg          active
確認コード AIX0379A
画面・出力には AIX0379A が表示され、lsvg -l 起動確認 VG STATE 0379 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1019
確認コード AIX0379B
画面・出力には AIX0379B が表示され、lsvg -l 起動確認 VG STATE 0379 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。VG STATE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0379C
画面・出力には AIX0379C が表示され、lsvg -l 起動確認 VG STATE 0379 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0379A が画面・出力に表示されること
② ステップ2 の AIX0379B が画面・出力に表示されること
③ ステップ3 の AIX0379C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0161"><h3>lsvg -l 障害切り分け STALE PARTITIONS 0409</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第四百九観点 LVM で lsvg -l は 障害切り分け を点検します（運用第四百九）（第四百九観点）。第四百九観点 確認時には STALE PARTITIONS と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第四百九）（第四百九観点）。第四百九観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第四百九観点）。第四百九観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0409へ書きます（第四百九観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 「lsvg -l 障害切り分け STALE PARTITIONS 0409」を「mount -o remount バックアウト確認 lff 0410」と区別して説明するとき、一次資料と整合する組合せはどれですか。</p><ul class="kb-choices"><li>A. 保守作業で参照する機能はJFS2でmount -o remountを用い・lff とファイルシステム属性を確認する。</li><li>B. 保守作業で参照する機能はLVMでlsvg -lを用い・STALE PARTITIONS とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 保守作業で参照する機能はネットワークでlsdev -Cc adapterを用い・Destinationである。lsdev -Cc adapter 状態確認 Destination固有の属性も確認対象に含める。</li><li>D. 保守作業で参照する機能はSRCとログでrefresh -s syslogdを用い・IDENTIFIERである。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LVMでlsvg -lを用い、STALE PARTITIONS」に対応する項目はSTALE PARTITIONS（障害・lsvg）です。障害切に関するLVMの仕様は「LVMでlsvg -lを用い、STALE PARTITIONS」で、確認対象はls・障害切です。バック・mounのA:は「JFS2でmount -o remountを用い、lff」を述べ、対象はバックアウト確認 lff（バッ・moun）です。状態・lsdeのC:は「ネットワークでlsdev -Cc adapterを用い」を述べ、対象は状態確認 Destination（状態・lsde）です。監査・refrのD:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は監査記録 IDENTIFIER（監査・refr）です。「lsvg -l」は「LVMでlsvg -lを用い、STALE PARTITIONS」を指し、STALE PARTITIONSではls・障害切に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg -l 障害切り分け STALE PARTITIONS 0409</strong></p><p>検証目的: LVMのlsvg -l 障害切り分け STALE PARTITIONS 0409について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM障害切り分け049-04</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40409        rootvg          active
hdisk1          00f6a1b2c3d50409        datavg          active
確認コード AIX0409A
画面・出力には AIX0409A が表示され、lsvg -l 障害切り分け STALE PARTITIONS 0409 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1049
確認コード AIX0409B
画面・出力には AIX0409B が表示され、lsvg -l 障害切り分け STALE PARTITIONS 0409 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。STALE PARTITIONS を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0409C
画面・出力には AIX0409C が表示され、lsvg -l 障害切り分け STALE PARTITIONS 0409 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0409A が画面・出力に表示されること
② ステップ2 の AIX0409B が画面・出力に表示されること
③ ステップ3 の AIX0409C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0162"><h3>lsvg バックアウト確認 MIRROR WRITE CONSISTENCY 0636</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第六百三十六観点 LVM で lsvg は バックアウト確認 を点検します（運用第六百三十六）（第六百三十六観点）。第六百三十六観点 確認時には MIRROR WRITE CONSISTENCY と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第六百三十六）（第六百三十六観点）。第六百三十六観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第六百三十六観点）。第六百三十六観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0636へ書きます（第六百三十六観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg バックアウト確認 MIRROR WRITE CONSISTENCY 0636の技術的な意味を資料で確認するとき、lsfs -q 監査記録 log=INLINE 0637との境界を正しく示す記述はどれですか。</p><ul class="kb-choices"><li>A. 構成を確認する際の意味はLVMでlsvgを用い・MIRROR WRITE CONSISTENCY と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 構成を確認する際の意味はJFS2でlsfs -qを用い・log=INLINE とマウントオプションを確認する。</li><li>C. 構成を確認する際の意味はセキュリティでrolelist -u user1を用い・authorizationsである。rolelist -u user1 起動確認固有の属性も確認対象に含める。</li><li>D. 構成を確認する際の意味は導入と起動でlslpp -Lを用い・mksysb image と起動デバイス設定を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「LVMでlsvgを用い、MIRROR WRITE CONSISTENCY」に対応する項目はWRITE CONSISTENCY（バッ・lsvg）です。バックに関するLVMの仕様は「LVMでlsvgを用い、MIRROR WRITE」で、確認対象はls・バックです。監査・lsfsのB:は「JFS2でlsfs -qを用い、log=INLINE」を述べ、対象は監査記録 log=INLINE（監査・lsfs）です。起動・roleのC:は「セキュリティでrolelist -u user1を用い」を述べ、対象は起動確認 authorization（起動・role）です。運用引・lslpのD:は「導入と起動でlslpp -Lを用い、mksysb image」を述べ、対象はmksysb image（運用・lslp）です。「lsvg」は「LVMでlsvgを用い、MIRROR WRITE」を指し、WRITE CONSISTENCYではls・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg バックアウト確認 MIRROR WRITE CONSISTENCY 0636</strong></p><p>検証目的: LVMのlsvg バックアウト確認 MIRROR WRITE CONSISTENCY 0636について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVMバックアウト確認036-06</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40636        rootvg          active
hdisk1          00f6a1b2c3d50636        datavg          active
確認コード AIX0636A
画面・出力には AIX0636A が表示され、lsvg バックアウト確認 MIRROR WRITE CONSISTENCY 0636 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1036
確認コード AIX0636B
画面・出力には AIX0636B が表示され、lsvg バックアウト確認 MIRROR WRITE CONSISTENCY 0636 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0636C
画面・出力には AIX0636C が表示され、lsvg バックアウト確認 MIRROR WRITE CONSISTENCY 0636 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0636A が画面・出力に表示されること
② ステップ2 の AIX0636B が画面・出力に表示されること
③ ステップ3 の AIX0636C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0163"><h3>lsvg バックアウト確認 PP SIZE 0160</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第百六十観点 LVM で lsvg は バックアウト確認 を点検します（運用第百六十）（第百六十観点）。第百六十観点 確認時には PP SIZE と 論理ボリューム配置 の対応を同じ資料上で追えることを前提にします（資料第百六十）（第百六十観点）。第百六十観点 lsvg rootvg の出力と取得時刻を同じ確認票に置き、PVIDの取り違え を避ける判断根拠を説明可能にします（第百六十観点）。第百六十観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0160へ書きます（第百六十観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg バックアウト確認 PP SIZE 0160を同一分類のlsfs -q 監査記録 lff 0161と比較します。対象固有の機能として妥当な記述はどれですか。</p><ul class="kb-choices"><li>A. 管理対象との関係を表す説明はJFS2でlsfs -qを用い・lff とマウントオプションを確認する。</li><li>B. 管理対象との関係を表す説明はLVMでlsvgを用い・PP SIZE と論理ボリューム配置を確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. 管理対象との関係を表す説明はネットワークでcfgmgrを用い・MTU とアダプター一覧を確認する。</li><li>D. 管理対象との関係を表す説明はJFS2でdefragfsを用い・mountguard とマウントオプションを確認する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Bの記述「LVMでlsvgを用い、PP SIZE と論理ボリューム配置を確認する」に対応する項目はPP SIZE（バッ・lsvg）です。バックに関するLVMの仕様は「LVMでlsvgを用い、PP SIZE と論理ボリューム配置を確認す」で、確認対象はls・バックです。監査・lsfsのA:は「JFS2でlsfs -qを用い、lff とマウントオプションを確認す」を述べ、対象は監査記録 lff（監査・lsfs）です。構成・cfgmのC:は「ネットワークでcfgmgrを用い、MTU とアダプター一覧を確認する」を述べ、対象は構成照合 MTU（構成・cfgm）です。属性・defrのD:は「JFS2でdefragfsを用い、mountguard」を述べ、対象は属性確認 mountguard（属性・defr）です。「lsvg」は「LVMでlsvgを用い、PP SIZE と論理ボリューム配置を確認す」を指し、PP SIZEではls・バックに対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg バックアウト確認 PP SIZE 0160</strong></p><p>検証目的: LVMのlsvg バックアウト確認 PP SIZE 0160について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVMバックアウト確認040-02</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40160        rootvg          active
hdisk1          00f6a1b2c3d50160        datavg          active
確認コード AIX0160A
画面・出力には AIX0160A が表示され、lsvg バックアウト確認 PP SIZE 0160 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1040
確認コード AIX0160B
画面・出力には AIX0160B が表示され、lsvg バックアウト確認 PP SIZE 0160 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。PP SIZE を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; bootinfo -B hdisk1
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0160C
画面・出力には AIX0160C が表示され、lsvg バックアウト確認 PP SIZE 0160 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0160A が画面・出力に表示されること
② ステップ2 の AIX0160B が画面・出力に表示されること
③ ステップ3 の AIX0160C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>


<section class="kb-item" id="c01-i0164"><h3>lsvg 変更後確認 MIRROR WRITE CONSISTENCY 0765</h3><p class="kb-meta">分類: LVM ・ 難易度: 中級</p><p>第七百六十五観点 LVM で lsvg は 変更後確認 を点検します（運用第七百六十五）（第七百六十五観点）。第七百六十五観点 確認時には MIRROR WRITE CONSISTENCY と ミラーコピー状態 の対応を同じ資料上で追えることを前提にします（資料第七百六十五）（第七百六十五観点）。第七百六十五観点 bootinfo -B hdisk1 の出力と取得時刻を同じ確認票に置き、VGDA拡張後の写像再採取漏れ を避ける判断根拠を説明可能にします（第七百六十五観点）。第七百六十五観点 記録では対象名、出力見出し、確認値、関連コマンドを AIX記録0765へ書きます（第七百六十五観点）。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> lsvg 変更後確認 MIRROR WRITE CONSISTENCY 0765を保守記録に説明する必要があります。refresh -s syslogd 障害切り分け syslog.conf 0766と取り違えない説明はどれですか。</p><ul class="kb-choices"><li>A. 運用時に利用する技術的役割はLVMでlsvgを用い・MIRROR WRITE CONSISTENCY とミラーコピー状態を確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. 運用時に利用する技術的役割はSRCとログでrefresh -s syslogdを用い・syslog.confである。</li><li>C. 運用時に利用する技術的役割はセキュリティでrolelist -u user1を用い・roles とロール一覧を確認する。rolelist -u user1 容量確認 roles 0151固有の属性も確認対象に含める。</li><li>D. 運用時に利用する技術的役割は導入と起動でlslpp -Lを用い・altinst_rootvg とOSレベル表示を確認する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> Aの記述「LVMでlsvgを用い、MIRROR WRITE CONSISTENCY」に対応する項目はWRITE CONSISTENCY（変更・lsvg）です。変更後に関するLVMの仕様は「LVMでlsvgを用い、MIRROR WRITE」で、確認対象はls・変更後です。障害切・refrのB:は「SRCとログでrefresh -s syslogdを用い」を述べ、対象は障害切り分け syslog.conf（障害・refr）です。容量・roleのC:は「セキュリティでrolelist -u user1を用い、roles」を述べ、対象は容量確認 roles（容量・role）です。バック・lslpのD:は「導入と起動でlslpp -Lを用い、altinst_rootvg」を述べ、対象はバックアウト確認 altinst_r（バッ・lslp）です。「lsvg」は「LVMでlsvgを用い、MIRROR WRITE」を指し、WRITE CONSISTENCYではls・変更後に対応します。</p><p class="kb-src"><strong>出典:</strong> AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>lsvg 変更後確認 MIRROR WRITE CONSISTENCY 0765</strong></p><p>検証目的: LVMのlsvg 変更後確認 MIRROR WRITE CONSISTENCY 0765について、AIX 7.3資料で確認できる実在コマンドと出力形式を机上で照合する。</p><p>前提条件: 対象環境のAIX 7.3資料を確認済み。対象=LVM変更後確認045-07</p><p>セッション環境: 机上検証。AIXコマンド、構成ファイル、表見出し、エラーログ形式を資料に合わせて使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg
→ Enter を押す
［画面・出力］
hdisk0          00f6a1b2c3d40765        rootvg          active
hdisk1          00f6a1b2c3d50765        datavg          active
確認コード AIX0765A
画面・出力には AIX0765A が表示され、lsvg 変更後確認 MIRROR WRITE CONSISTENCY 0765 の入力欄確認を確認できます。
――――
■ ステップ 2
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg rootvg
→ Enter を押す
［画面・出力］
VOLUME GROUP: rootvg
VG STATE: active
PP SIZE: 128 megabyte(s)
TOTAL PPs: 1045
確認コード AIX0765B
画面・出力には AIX0765B が表示され、lsvg 変更後確認 MIRROR WRITE CONSISTENCY 0765 の証跡表示確認を確認できます。
――――
■ ステップ 3
現在の画面はAIX 7.3のシェルまたはSMIT相当の確認画面です。MIRROR WRITE CONSISTENCY を読むため、LVM の対象値を表示します。
［操作（入力）］
AIX 7.3 シェル
COMMAND ===&gt; lsvg -l rootvg
→ Enter を押す
［画面・出力］
LV NAME             TYPE       LPs   PPs   LV STATE      MOUNT POINT
hd4                 jfs2       1     1     open/syncd    /
hd2                 jfs2       48    48    open/syncd    /usr
確認コード AIX0765C
画面・出力には AIX0765C が表示され、lsvg 変更後確認 MIRROR WRITE CONSISTENCY 0765 の判定材料確認を確認できます。
――――</pre><p>合格条件: ① ステップ1 の AIX0765A が画面・出力に表示されること
② ステップ2 の AIX0765B が画面・出力に表示されること
③ ステップ3 の AIX0765C が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: AIX73_commands1_en / AIX73_commands2_en / AIX73_commands3_en / AIX73_devicemanagement_en / AIX73_network_en / AIX73_performance_en / AIX73_osmanagement_en / AIX73_security_en / AIX73_install_en</p></div></details></section>
