---
search:
  exclude: true
---

# z/OS System Programming — 詳細 (2/2)

[← z/OS System Programming の概要へ戻る](index.md)


## SMFダンプ


<section class="kb-item" id="c38-i0151"><h3>IEFU83出口 優先順位確認 運用確認039</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>第三十九観点 SMFダンプ の運用では IEFU83出口 を表示、定義、証跡で確認します（第三十九観点）。第三十九観点 役割は SMFレコード書き込み時などに記録内容を選別または補足する出口という範囲です（第三十九観点）。第三十九観点 D PROG,APF のCSV450I表示 の値を SYS1.PARMLIB(SMFSP) と合わせ、SMF記録欠落の早期検出を記録します（第三十九観点）。第三十九観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録039に残します（第三十九観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IEFU83出口 優先順位確認 運用確認039</strong></p><p>検証目的: IEFU83出口 の 優先順位確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / WLM dispatch</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IEFU83出口 の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.05.15 ACTIVE JOBS DISPLAY 638
JOBNAME  ASID  STATUS
WLM      000A  ACTIVE
JES2     0012  ACTIVE
画面・出力には IEE114I が含まれる。IEE114I を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IEFU83出口 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D WLM,SYSTEMS
→ Enter を押す
［画面・出力］
IWM026I 12.06.15 WLM DISPLAY 648
SYSTEM   MODE     POLICY
SC65     GOAL     POLSP15
画面・出力には GOAL が含まれる。GOAL を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IEFU83出口 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
SDSF DA panel
COMMAND ===&gt; DA
→ Enter を押す
［画面・出力］
SDSF DA DISPLAY
JOBNAME  ASID  CPU%  DP
BATCH15 0015  02.1  245
画面・出力には JOBNAME が含まれる。JOBNAME を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE114I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: GOAL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: JOBNAME が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0152"><h3>SMFダンプ IFASMFDPダンプ ログとの照合 DUMP07</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>ログとの照合では SMFダンプ の 入力確認 を主操作として DUMP07 を判定します。時刻と対象識別子への注意として「抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します」を DUMP07 に残します。ログとの照合を補助する ダンプ実行 では IFASMFDP を補助値として DUMP07 へ保存します。主判定のログとの照合ではダンプ・入力期間と戻りコードの 入力確認 から ORGANIZATION を読み DUMP07 へ残します。証跡照合のログとの照合ではダンプ・入力期間と戻りコードの ORGANIZATION と IFASMFDP を DUMP07 に保存します。記録対応のログとの照合ではダンプ・入力期間と戻りコードの 入力期間と戻りコード の証跡へ DUMP07 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で SMFダンプ の 入力確認 と ダンプ実行 を使い 操作とログを対応 します。IFASMFDPダンプ はMANデータセットまたはログストリームから指定レコードを抽出し、監査または分析用データセットへコピーするユーティリティです。抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します。ORGANIZATION を読み対象 DUMP07 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. ORGANIZATIONを含む入力確認の応答行を保存する。その応答を得るためBROWSE SYS1.MAN07を使用する。対象DUMP07の入力期間と戻りコードとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. BROWSE SYS1.MAN07が応答を返した時点で正常とする。応答中のORGANIZATIONの値は記録しない。RECFM=VBSをORGANIZATIONと同じ判定値とみなし対象DUMP07の主証跡にする。</li><li>C. BROWSE SYS1.MAN07のコマンド文字列だけを記録する。ORGANIZATIONを含む応答行は保存しない。</li><li>D. IFASMFDPダンプの停止または再定義を実施する。その後にBROWSE SYS1.MAN07でORGANIZATIONを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: Aは入力確認で ORGANIZATION を読み入力期間と戻りコードの主値として操作とログを対応しDUMP07に残します。
機能の仕組み: ログとの照合ではダンプ実行を補助操作としIFASMFDPダンプの時刻と対象識別子をIFASMFDPと対象DUMP07で照合します。
各候補の評価: 入力確認とダンプ実行の役割を分けるとA: ORGANIZATIONの実値を対象別に残す点で主証跡になります、B: 応答の有無だけでは入力期間と戻りコードを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけでは入力期間と戻りコードを証明できない点で入力期間と戻りコードを確認できません、D: 変更前の入力期間と戻りコードを失う点でダンプ実行の範囲を越えます。結論としてログとの照合のダンプ・入力期間と戻りコードで判定する対象は DUMP07 です。
用語の定義: ログとの照合で使う IFASMFDPダンプ はSMFダンプで入力期間と戻りコードを扱う機能を表し入力期間と戻りコードを判定する際にDUMP07へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFダンプ IFASMFDPダンプ ログとの照合 DUMP07</strong></p><p>検証目的: SMFダンプのIFASMFDPダンプについて操作とログを対応し、DUMP07の入力期間と戻りコードを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象DUMP07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へBROWSE SYS1.MAN07を指定し、DUMP07の入力確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; BROWSE SYS1.MAN07
→ Enter を押す
［画面・出力］
DATA SET NAME SYS1.MAN07 ORGANIZATION PS RECORD FORMAT VBS
画面・出力にあるORGANIZATIONを読み、入力期間と戻りコードと対象DUMP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へSUBMIT SYS1.SAMPLIB(IFASMFDP)を指定し、DUMP07のダンプ実行を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SUBMIT SYS1.SAMPLIB(IFASMFDP)
→ Enter を押す
［画面・出力］
IFASMFDP SMF DATA SET DUMP PROGRAM
RECORDS READ 00001234
RECORDS WRITTEN 00000456
RETURN CODE 0000
画面・出力にあるIFASMFDPを読み、入力期間と戻りコードと対象DUMP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へLISTDS SYS1.SMF.DUMP07を指定し、DUMP07の出力属性を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; LISTDS SYS1.SMF.DUMP07
→ Enter を押す
［画面・出力］
SYS1.SMF.DUMP07 RECFM=VBS LRECL=32760 BLKSIZE=0
画面・出力にあるRECFM=VBSを読み、入力期間と戻りコードと対象DUMP07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ORGANIZATION が画面・出力に表示されること
② ステップ2 の IFASMFDP が画面・出力に表示されること
③ ステップ3 の RECFM=VBS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0153"><h3>SMFダンプ IFASMFDPダンプ 代替経路の確認 DUMP10</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>代替経路の確認では SMFダンプ の 入力確認 を主操作として DUMP10 を判定します。主経路との役割差への注意として「抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します」を DUMP10 に残します。代替経路の確認を補助する ダンプ実行 では IFASMFDP を補助値として DUMP10 へ保存します。主判定の代替経路の確認ではダンプ・入力期間と戻りコードの 入力確認 から ORGANIZATION を読み DUMP10 へ残します。証跡照合の代替経路の確認ではダンプ・入力期間と戻りコードの ORGANIZATION と IFASMFDP を DUMP10 に保存します。記録対応の代替経路の確認ではダンプ・入力期間と戻りコードの 入力期間と戻りコード の証跡へ DUMP10 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で SMFダンプ の 入力確認 と ダンプ実行 を照合し 主経路との役割差 を確かめます。IFASMFDPダンプ はMANデータセットまたはログストリームから指定レコードを抽出し、監査または分析用データセットへコピーするユーティリティです。抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します。ORGANIZATION を読む前に対象 DUMP10 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. BROWSE SYS1.MAN10のコマンド文字列だけを記録する。ORGANIZATIONを含む応答行は保存しない。</li><li>B. IFASMFDPダンプの停止または再定義を実施する。その後にBROWSE SYS1.MAN10でORGANIZATIONを採取する。</li><li>C. APF管理のDSNAMEとVOLSERを確認する。その値をSMFダンプのDUMP10にも適用する。</li><li>D. BROWSE SYS1.MAN10とSUBMIT SYS1.SAMPLIB(IFASMFDP)の対象名をそろえる。前者のORGANIZATIONを入力期間と戻りコードの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: Dは入力確認で ORGANIZATION を読み入力期間と戻りコードの主値として代替手段の成立を確認しDUMP10に残します。
運用上の背景: 代替経路の確認ではダンプ実行を補助操作としIFASMFDPダンプの主経路との役割差をIFASMFDPと対象DUMP10で照合します。
候補別の検討: 入力確認とダンプ実行の役割を分けるとA: 入力記録だけでは入力期間と戻りコードを証明できない点で一次資料と一致しません、B: 変更前の入力期間と戻りコードを失う点で入力期間と戻りコードを確認できません、C: APF管理の値ではORGANIZATIONを確認できない点でダンプ実行の範囲を越えます、D: 同じ対象名のORGANIZATIONを採用する点で現在値を示します。結論として代替経路の確認のダンプ・入力期間と戻りコードで判定する対象は DUMP10 です。
重要用語の定義: 代替経路の確認で使う IFASMFDPダンプ はSMFダンプで入力期間と戻りコードを扱う機能を表し入力期間と戻りコードを判定する際にDUMP10へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFダンプ IFASMFDPダンプ 代替経路の確認 DUMP10</strong></p><p>検証目的: SMFダンプのIFASMFDPダンプについて代替手段の成立を確認し、DUMP10の入力期間と戻りコードを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象DUMP10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へBROWSE SYS1.MAN10を指定し、DUMP10の入力確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; BROWSE SYS1.MAN10
→ Enter を押す
［画面・出力］
DATA SET NAME SYS1.MAN10 ORGANIZATION PS RECORD FORMAT VBS
画面・出力にあるORGANIZATIONを読み、入力期間と戻りコードと対象DUMP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へSUBMIT SYS1.SAMPLIB(IFASMFDP)を指定し、DUMP10のダンプ実行を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SUBMIT SYS1.SAMPLIB(IFASMFDP)
→ Enter を押す
［画面・出力］
IFASMFDP SMF DATA SET DUMP PROGRAM
RECORDS READ 00001234
RECORDS WRITTEN 00000456
RETURN CODE 0000
画面・出力にあるIFASMFDPを読み、入力期間と戻りコードと対象DUMP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へLISTDS SYS1.SMF.DUMP10を指定し、DUMP10の出力属性を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; LISTDS SYS1.SMF.DUMP10
→ Enter を押す
［画面・出力］
SYS1.SMF.DUMP10 RECFM=VBS LRECL=32760 BLKSIZE=0
画面・出力にあるRECFM=VBSを読み、入力期間と戻りコードと対象DUMP10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ORGANIZATION が画面・出力に表示されること
② ステップ2 の IFASMFDP が画面・出力に表示されること
③ ステップ3 の RECFM=VBS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0154"><h3>SMFダンプ IFASMFDPダンプ 変更前の確認 DUMP02</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>変更前の確認では SMFダンプ の ダンプ実行 を主操作として DUMP02 を判定します。変更対象と非対象の境界への注意として「抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します」を DUMP02 に残します。変更前の確認を補助する 出力属性 では RECFM=VBS を補助値として DUMP02 へ保存します。主判定の変更前の確認ではダンプ・入力期間と戻りコードの ダンプ実行 から IFASMFDP を読み DUMP02 へ残します。証跡照合の変更前の確認ではダンプ・入力期間と戻りコードの IFASMFDP と RECFM=VBS を DUMP02 に保存します。記録対応の変更前の確認ではダンプ・入力期間と戻りコードの 入力期間と戻りコード の証跡へ DUMP02 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で SMFダンプ の ダンプ実行 と 出力属性 を実施し IFASMFDPダンプ の役割を確認します。抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します。対象 DUMP02 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. SUBMIT SYS1.SAMPLIB(IFASMFDP)を対象名なしで実行する。一覧の先頭行をDUMP02の結果として記録する。</li><li>B. 前回保存したSUBMIT SYS1.SAMPLIB(IFASMFDP)の結果を使う。今回のLISTDS SYS1.SMF.DUMP02の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのDUMP02の出力を再利用する。今回のSUBMIT SYS1.SAMPLIB(IFASMFDP)とLISTDS SYS1.SMF.DUMP02は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象DUMP02についてSUBMIT SYS1.SAMPLIB(IFASMFDP)の応答からIFASMFDPを確認する。LISTDS SYS1.SMF.DUMP02は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Dはダンプ実行で IFASMFDP を読み入力期間と戻りコードの主値として変更前の証跡を保存しDUMP02に残します。
動作の背景: 変更前の確認では出力属性を補助操作としIFASMFDPダンプの変更対象と非対象の境界をRECFM=VBSと対象DUMP02で照合します。
各選択肢の検討: ダンプ実行と出力属性の役割を分けるとA: 先頭行はDUMP02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でダンプ実行を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でSMFダンプに使いません、D: IFASMFDPと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のダンプ・入力期間と戻りコードで判定する対象は DUMP02 です。
初出用語の定義: 変更前の確認で使う IFASMFDPダンプ はSMFダンプで入力期間と戻りコードを扱う機能を表し入力期間と戻りコードを判定する際にDUMP02へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFダンプ IFASMFDPダンプ 変更前の確認 DUMP02</strong></p><p>検証目的: SMFダンプのIFASMFDPダンプについて変更前の証跡を保存し、DUMP02の入力期間と戻りコードを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象DUMP02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へSUBMIT SYS1.SAMPLIB(IFASMFDP)を指定し、DUMP02のダンプ実行を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SUBMIT SYS1.SAMPLIB(IFASMFDP)
→ Enter を押す
［画面・出力］
IFASMFDP SMF DATA SET DUMP PROGRAM
RECORDS READ 00001234
RECORDS WRITTEN 00000456
RETURN CODE 0000
画面・出力にあるIFASMFDPを読み、入力期間と戻りコードと対象DUMP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へLISTDS SYS1.SMF.DUMP02を指定し、DUMP02の出力属性を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; LISTDS SYS1.SMF.DUMP02
→ Enter を押す
［画面・出力］
SYS1.SMF.DUMP02 RECFM=VBS LRECL=32760 BLKSIZE=0
画面・出力にあるRECFM=VBSを読み、入力期間と戻りコードと対象DUMP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へBROWSE SYS1.MAN02を指定し、DUMP02の入力確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; BROWSE SYS1.MAN02
→ Enter を押す
［画面・出力］
DATA SET NAME SYS1.MAN02 ORGANIZATION PS RECORD FORMAT VBS
画面・出力にあるORGANIZATIONを読み、入力期間と戻りコードと対象DUMP02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IFASMFDP が画面・出力に表示されること
② ステップ2 の RECFM=VBS が画面・出力に表示されること
③ ステップ3 の ORGANIZATION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0155"><h3>SMFダンプ IFASMFDPダンプ 変更後の確認 DUMP03</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>変更後の確認では SMFダンプ の 出力属性 を主操作として DUMP03 を判定します。反映値と残存値への注意として「抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します」を DUMP03 に残します。変更後の確認を補助する 入力確認 では ORGANIZATION を補助値として DUMP03 へ保存します。主判定の変更後の確認ではダンプ・入力期間と戻りコードの 出力属性 から RECFM=VBS を読み DUMP03 へ残します。証跡照合の変更後の確認ではダンプ・入力期間と戻りコードの RECFM=VBS と ORGANIZATION を DUMP03 に保存します。記録対応の変更後の確認ではダンプ・入力期間と戻りコードの 入力期間と戻りコード の証跡へ DUMP03 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で SMFダンプ の 出力属性 と 入力確認 を用い 変更結果を検証 します。IFASMFDPダンプ はMANデータセットまたはログストリームから指定レコードを抽出し、監査または分析用データセットへコピーするユーティリティです。抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します。RECFM=VBS で対象 DUMP03 の 入力期間と戻りコード を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. BROWSE SYS1.MAN03で周辺状態を押さえる。その後にLISTDS SYS1.SMF.DUMP03でRECFM=VBSを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. IFASMFDPダンプの停止または再定義を実施する。その後にLISTDS SYS1.SMF.DUMP03でRECFM=VBSを採取する。</li><li>C. SAF連携のSAF RCとRACF RCを確認する。その値をSMFダンプのDUMP03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。IFASMFDPダンプの反映値と残存値は確認済みとして扱う。さらにSUBMIT SYS1.SAMPLIB(IFASMFDP)のIFASMFDPをRECFM=VBSと同種の値として併記する。</li><li>D. BROWSE SYS1.MAN03が成功したためLISTDS SYS1.SMF.DUMP03のRECFM=VBSも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: Aは出力属性で RECFM=VBS を読み入力期間と戻りコードの主値として変更結果を検証しDUMP03に残します。
内部の仕組み: 変更後の確認では入力確認を補助操作としIFASMFDPダンプの反映値と残存値をORGANIZATIONと対象DUMP03で照合します。
誤答を含む比較: 出力属性と入力確認の役割を分けるとA: 周辺状態の後にRECFM=VBSを確認する点でDUMP03を判定できます、B: 変更前の入力期間と戻りコードを失う点で入力確認の範囲を越えます、C: SAF連携の値ではRECFM=VBSを確認できないうえに追加前提も不正な点でDUMP03の値を示しません、D: 補助操作の成功ではRECFM=VBSを確定できない点で変更後の確認に合いません。結論として変更後の確認のダンプ・入力期間と戻りコードで判定する対象は DUMP03 です。
用語定義: 変更後の確認で使う IFASMFDPダンプ はSMFダンプで入力期間と戻りコードを扱う機能を表し入力期間と戻りコードを判定する際にDUMP03へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFダンプ IFASMFDPダンプ 変更後の確認 DUMP03</strong></p><p>検証目的: SMFダンプのIFASMFDPダンプについて変更結果を検証し、DUMP03の入力期間と戻りコードを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象DUMP03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へLISTDS SYS1.SMF.DUMP03を指定し、DUMP03の出力属性を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; LISTDS SYS1.SMF.DUMP03
→ Enter を押す
［画面・出力］
SYS1.SMF.DUMP03 RECFM=VBS LRECL=32760 BLKSIZE=0
画面・出力にあるRECFM=VBSを読み、入力期間と戻りコードと対象DUMP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へBROWSE SYS1.MAN03を指定し、DUMP03の入力確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; BROWSE SYS1.MAN03
→ Enter を押す
［画面・出力］
DATA SET NAME SYS1.MAN03 ORGANIZATION PS RECORD FORMAT VBS
画面・出力にあるORGANIZATIONを読み、入力期間と戻りコードと対象DUMP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へSUBMIT SYS1.SAMPLIB(IFASMFDP)を指定し、DUMP03のダンプ実行を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SUBMIT SYS1.SAMPLIB(IFASMFDP)
→ Enter を押す
［画面・出力］
IFASMFDP SMF DATA SET DUMP PROGRAM
RECORDS READ 00001234
RECORDS WRITTEN 00000456
RETURN CODE 0000
画面・出力にあるIFASMFDPを読み、入力期間と戻りコードと対象DUMP03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の RECFM=VBS が画面・出力に表示されること
② ステップ2 の ORGANIZATION が画面・出力に表示されること
③ ステップ3 の IFASMFDP が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0156"><h3>SMFダンプ IFASMFDPダンプ 引継ぎ記録 DUMP09</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>引継ぎ記録では SMFダンプ の 出力属性 を主操作として DUMP09 を判定します。次担当者が追跡できる証跡への注意として「抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します」を DUMP09 に残します。引継ぎ記録を補助する 入力確認 では ORGANIZATION を補助値として DUMP09 へ保存します。主判定の引継ぎ記録ではダンプ・入力期間と戻りコードの 出力属性 から RECFM=VBS を読み DUMP09 へ残します。証跡照合の引継ぎ記録ではダンプ・入力期間と戻りコードの RECFM=VBS と ORGANIZATION を DUMP09 に保存します。記録対応の引継ぎ記録ではダンプ・入力期間と戻りコードの 入力期間と戻りコード の証跡へ DUMP09 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で SMFダンプ の 出力属性 と 入力確認 を用い 再現可能な記録を作成 します。IFASMFDPダンプ はMANデータセットまたはログストリームから指定レコードを抽出し、監査または分析用データセットへコピーするユーティリティです。抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します。RECFM=VBS で対象 DUMP09 の 入力期間と戻りコード を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. BROWSE SYS1.MAN09が成功したためLISTDS SYS1.SMF.DUMP09のRECFM=VBSも正常だと推定する。主出力は保存しない。</li><li>B. LISTDS SYS1.SMF.DUMP09を対象名なしで実行する。一覧の先頭行をDUMP09の結果として記録する。</li><li>C. 対象名DUMP09を指定してLISTDS SYS1.SMF.DUMP09を実行する。応答中のRECFM=VBSと時刻を保存する。BROWSE SYS1.MAN09で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したLISTDS SYS1.SMF.DUMP09の結果を使う。今回のBROWSE SYS1.MAN09の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: Cは出力属性で RECFM=VBS を読み入力期間と戻りコードの主値として再現可能な記録を作成しDUMP09に残します。
製品内の仕組み: 引継ぎ記録では入力確認を補助操作としIFASMFDPダンプの次担当者が追跡できる証跡をORGANIZATIONと対象DUMP09で照合します。
選択肢別の説明: 出力属性と入力確認の役割を分けるとA: 補助操作の成功ではRECFM=VBSを確定できない点でDUMP09の値を示しません、B: 先頭行はDUMP09と確定できない点で引継ぎ記録に合いません、C: RECFM=VBSと時刻を保存する点で出力属性に合います、D: 採取時刻が異なる点でSMFダンプに使いません。結論として引継ぎ記録のダンプ・入力期間と戻りコードで判定する対象は DUMP09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う IFASMFDPダンプ はSMFダンプで入力期間と戻りコードを扱う機能を表し入力期間と戻りコードを判定する際にDUMP09へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFダンプ IFASMFDPダンプ 引継ぎ記録 DUMP09</strong></p><p>検証目的: SMFダンプのIFASMFDPダンプについて再現可能な記録を作成し、DUMP09の入力期間と戻りコードを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象DUMP09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へLISTDS SYS1.SMF.DUMP09を指定し、DUMP09の出力属性を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; LISTDS SYS1.SMF.DUMP09
→ Enter を押す
［画面・出力］
SYS1.SMF.DUMP09 RECFM=VBS LRECL=32760 BLKSIZE=0
画面・出力にあるRECFM=VBSを読み、入力期間と戻りコードと対象DUMP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へBROWSE SYS1.MAN09を指定し、DUMP09の入力確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; BROWSE SYS1.MAN09
→ Enter を押す
［画面・出力］
DATA SET NAME SYS1.MAN09 ORGANIZATION PS RECORD FORMAT VBS
画面・出力にあるORGANIZATIONを読み、入力期間と戻りコードと対象DUMP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へSUBMIT SYS1.SAMPLIB(IFASMFDP)を指定し、DUMP09のダンプ実行を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SUBMIT SYS1.SAMPLIB(IFASMFDP)
→ Enter を押す
［画面・出力］
IFASMFDP SMF DATA SET DUMP PROGRAM
RECORDS READ 00001234
RECORDS WRITTEN 00000456
RETURN CODE 0000
画面・出力にあるIFASMFDPを読み、入力期間と戻りコードと対象DUMP09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の RECFM=VBS が画面・出力に表示されること
② ステップ2 の ORGANIZATION が画面・出力に表示されること
③ ステップ3 の IFASMFDP が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0157"><h3>SMFダンプ IFASMFDPダンプ 復旧後の確認 DUMP06</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>復旧後の確認では SMFダンプ の 出力属性 を主操作として DUMP06 を判定します。再発していないことを示す値への注意として「抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します」を DUMP06 に残します。復旧後の確認を補助する 入力確認 では ORGANIZATION を補助値として DUMP06 へ保存します。主判定の復旧後の確認ではダンプ・入力期間と戻りコードの 出力属性 から RECFM=VBS を読み DUMP06 へ残します。証跡照合の復旧後の確認ではダンプ・入力期間と戻りコードの RECFM=VBS と ORGANIZATION を DUMP06 に保存します。記録対応の復旧後の確認ではダンプ・入力期間と戻りコードの 入力期間と戻りコード の証跡へ DUMP06 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で SMFダンプ の 出力属性 と 入力確認 の役割を分け 再発していないことを示す値 を調べます。IFASMFDPダンプ はMANデータセットまたはログストリームから指定レコードを抽出し、監査または分析用データセットへコピーするユーティリティです。抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します。対象 DUMP06 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. Cross MemoryのHOME ASIDとSECONDARY ASIDを確認する。その値をSMFダンプのDUMP06にも適用する。</li><li>B. BROWSE SYS1.MAN06が成功したためLISTDS SYS1.SMF.DUMP06のRECFM=VBSも正常だと推定する。主出力は保存しない。別資源で得た状態を対象DUMP06へ引き継げるものとする。IFASMFDPダンプの再発していないことを示す値は確認済みとして扱う。さらにSUBMIT SYS1.SAMPLIB(IFASMFDP)のIFASMFDPをRECFM=VBSと同種の値として併記する。</li><li>C. LISTDS SYS1.SMF.DUMP06を対象名なしで実行する。一覧の先頭行をDUMP06の結果として記録する。</li><li>D. LISTDS SYS1.SMF.DUMP06でRECFM=VBSを取得してからSUBMIT SYS1.SAMPLIB(IFASMFDP)でIFASMFDPを照合する。DUMP06の入力期間と戻りコードを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Dは出力属性で RECFM=VBS を読み入力期間と戻りコードの主値として復旧後の安定性を確認しDUMP06に残します。
構成上の背景: 復旧後の確認では入力確認を補助操作としIFASMFDPダンプの再発していないことを示す値をORGANIZATIONと対象DUMP06で照合します。
候補ごとの理由: 出力属性と入力確認の役割を分けるとA: Cross Memoryの値ではRECFM=VBSを確認できない点で入力確認の範囲を越えます、B: 補助操作の成功ではRECFM=VBSを確定できないうえに追加前提も不正な点でDUMP06の値を示しません、C: 先頭行はDUMP06と確定できない点で復旧後の確認に合いません、D: RECFM=VBSとIFASMFDPを順に照合する点で出力属性に合います。結論として復旧後の確認のダンプ・入力期間と戻りコードで判定する対象は DUMP06 です。
初出用語: 復旧後の確認で使う IFASMFDPダンプ はSMFダンプで入力期間と戻りコードを扱う機能を表し入力期間と戻りコードを判定する際にDUMP06へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFダンプ IFASMFDPダンプ 復旧後の確認 DUMP06</strong></p><p>検証目的: SMFダンプのIFASMFDPダンプについて復旧後の安定性を確認し、DUMP06の入力期間と戻りコードを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象DUMP06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へLISTDS SYS1.SMF.DUMP06を指定し、DUMP06の出力属性を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; LISTDS SYS1.SMF.DUMP06
→ Enter を押す
［画面・出力］
SYS1.SMF.DUMP06 RECFM=VBS LRECL=32760 BLKSIZE=0
画面・出力にあるRECFM=VBSを読み、入力期間と戻りコードと対象DUMP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へBROWSE SYS1.MAN06を指定し、DUMP06の入力確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; BROWSE SYS1.MAN06
→ Enter を押す
［画面・出力］
DATA SET NAME SYS1.MAN06 ORGANIZATION PS RECORD FORMAT VBS
画面・出力にあるORGANIZATIONを読み、入力期間と戻りコードと対象DUMP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へSUBMIT SYS1.SAMPLIB(IFASMFDP)を指定し、DUMP06のダンプ実行を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SUBMIT SYS1.SAMPLIB(IFASMFDP)
→ Enter を押す
［画面・出力］
IFASMFDP SMF DATA SET DUMP PROGRAM
RECORDS READ 00001234
RECORDS WRITTEN 00000456
RETURN CODE 0000
画面・出力にあるIFASMFDPを読み、入力期間と戻りコードと対象DUMP06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の RECFM=VBS が画面・出力に表示されること
② ステップ2 の ORGANIZATION が画面・出力に表示されること
③ ステップ3 の IFASMFDP が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0158"><h3>SMFダンプ IFASMFDPダンプ 復旧準備 DUMP05</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>復旧準備では SMFダンプ の ダンプ実行 を主操作として DUMP05 を判定します。再開前に必要な整合性への注意として「抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します」を DUMP05 に残します。復旧準備を補助する 出力属性 では RECFM=VBS を補助値として DUMP05 へ保存します。主判定の復旧準備ではダンプ・入力期間と戻りコードの ダンプ実行 から IFASMFDP を読み DUMP05 へ残します。証跡照合の復旧準備ではダンプ・入力期間と戻りコードの IFASMFDP と RECFM=VBS を DUMP05 に保存します。記録対応の復旧準備ではダンプ・入力期間と戻りコードの 入力期間と戻りコード の証跡へ DUMP05 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で SMFダンプ の ダンプ実行 と 出力属性 を組み合わせる際は IFASMFDPダンプ がMANデータセットまたはログストリームから指定レコードを抽出し、監査または分析用データセットへコピーするユーティリティという仕組みを前提にします。抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します。IFASMFDP と 入力期間と戻りコード を対象 DUMP05 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 前回保存したSUBMIT SYS1.SAMPLIB(IFASMFDP)の結果を使う。今回のLISTDS SYS1.SMF.DUMP05の結果と同一時点の証跡として比較する。</li><li>B. 保存済みのDUMP05の出力を再利用する。今回のSUBMIT SYS1.SAMPLIB(IFASMFDP)とLISTDS SYS1.SMF.DUMP05は実行済みとして扱う。</li><li>C. 変更を加えずSUBMIT SYS1.SAMPLIB(IFASMFDP)を実行する。IFASMFDPを保存する。差分はLISTDS SYS1.SMF.DUMP05の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. LISTDS SYS1.SMF.DUMP05のRECFM=VBSを入力期間と戻りコードの主判定に採用する。SUBMIT SYS1.SAMPLIB(IFASMFDP)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Cはダンプ実行で IFASMFDP を読み入力期間と戻りコードの主値として復旧条件を確認しDUMP05に残します。
処理の仕組み: 復旧準備では出力属性を補助操作としIFASMFDPダンプの再開前に必要な整合性をRECFM=VBSと対象DUMP05で照合します。
選択結果の内訳: ダンプ実行と出力属性の役割を分けるとA: 採取時刻が異なる点でダンプ実行を代替しません、B: 過去出力では今回の復旧準備を示せない点でSMFダンプに使いません、C: 変更前のIFASMFDPを保存する点で正答です、D: RECFM=VBSはIFASMFDPを代替しないうえに追加前提も不正な点でDUMP05を採用できません。結論として復旧準備のダンプ・入力期間と戻りコードで判定する対象は DUMP05 です。
用語の説明: 復旧準備で使う IFASMFDPダンプ はSMFダンプで入力期間と戻りコードを扱う機能を表し入力期間と戻りコードを判定する際にDUMP05へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFダンプ IFASMFDPダンプ 復旧準備 DUMP05</strong></p><p>検証目的: SMFダンプのIFASMFDPダンプについて復旧条件を確認し、DUMP05の入力期間と戻りコードを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象DUMP05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へSUBMIT SYS1.SAMPLIB(IFASMFDP)を指定し、DUMP05のダンプ実行を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SUBMIT SYS1.SAMPLIB(IFASMFDP)
→ Enter を押す
［画面・出力］
IFASMFDP SMF DATA SET DUMP PROGRAM
RECORDS READ 00001234
RECORDS WRITTEN 00000456
RETURN CODE 0000
画面・出力にあるIFASMFDPを読み、入力期間と戻りコードと対象DUMP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へLISTDS SYS1.SMF.DUMP05を指定し、DUMP05の出力属性を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; LISTDS SYS1.SMF.DUMP05
→ Enter を押す
［画面・出力］
SYS1.SMF.DUMP05 RECFM=VBS LRECL=32760 BLKSIZE=0
画面・出力にあるRECFM=VBSを読み、入力期間と戻りコードと対象DUMP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へBROWSE SYS1.MAN05を指定し、DUMP05の入力確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; BROWSE SYS1.MAN05
→ Enter を押す
［画面・出力］
DATA SET NAME SYS1.MAN05 ORGANIZATION PS RECORD FORMAT VBS
画面・出力にあるORGANIZATIONを読み、入力期間と戻りコードと対象DUMP05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IFASMFDP が画面・出力に表示されること
② ステップ2 の RECFM=VBS が画面・出力に表示されること
③ ステップ3 の ORGANIZATION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0159"><h3>SMFダンプ IFASMFDPダンプ 構成監査 DUMP08</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>構成監査では SMFダンプ の ダンプ実行 を主操作として DUMP08 を判定します。定義値と稼働値の一致への注意として「抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します」を DUMP08 に残します。構成監査を補助する 出力属性 では RECFM=VBS を補助値として DUMP08 へ保存します。主判定の構成監査ではダンプ・入力期間と戻りコードの ダンプ実行 から IFASMFDP を読み DUMP08 へ残します。証跡照合の構成監査ではダンプ・入力期間と戻りコードの IFASMFDP と RECFM=VBS を DUMP08 に保存します。記録対応の構成監査ではダンプ・入力期間と戻りコードの 入力期間と戻りコード の証跡へ DUMP08 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で SMFダンプ の ダンプ実行 と 出力属性 を実施し IFASMFDPダンプ の役割を確認します。抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します。対象 DUMP08 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのDUMP08の出力を再利用する。今回のSUBMIT SYS1.SAMPLIB(IFASMFDP)とLISTDS SYS1.SMF.DUMP08は実行済みとして扱う。</li><li>B. LISTDS SYS1.SMF.DUMP08の結果だけでは確定しない。SUBMIT SYS1.SAMPLIB(IFASMFDP)のIFASMFDPを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTDS SYS1.SMF.DUMP08のRECFM=VBSを入力期間と戻りコードの主判定に採用する。SUBMIT SYS1.SAMPLIB(IFASMFDP)の応答は採取対象から外す。</li><li>D. BROWSE SYS1.MAN08のORGANIZATIONをIFASMFDPと同義の成功表示として扱う。SUBMIT SYS1.SAMPLIB(IFASMFDP)は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Bはダンプ実行で IFASMFDP を読み入力期間と戻りコードの主値として構成差分を監査しDUMP08に残します。
実行時の背景: 構成監査では出力属性を補助操作としIFASMFDPダンプの定義値と稼働値の一致をRECFM=VBSと対象DUMP08で照合します。
四つの候補の理由: ダンプ実行と出力属性の役割を分けるとA: 過去出力では今回の構成監査を示せない点でSMFダンプに使いません、B: IFASMFDPを主証跡として区別する点で正答です、C: RECFM=VBSはIFASMFDPを代替しない点でDUMP08を採用できません、D: ORGANIZATIONとIFASMFDPは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のダンプ・入力期間と戻りコードで判定する対象は DUMP08 です。
初出語定義: 構成監査で使う IFASMFDPダンプ はSMFダンプで入力期間と戻りコードを扱う機能を表し入力期間と戻りコードを判定する際にDUMP08へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFダンプ IFASMFDPダンプ 構成監査 DUMP08</strong></p><p>検証目的: SMFダンプのIFASMFDPダンプについて構成差分を監査し、DUMP08の入力期間と戻りコードを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象DUMP08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へSUBMIT SYS1.SAMPLIB(IFASMFDP)を指定し、DUMP08のダンプ実行を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SUBMIT SYS1.SAMPLIB(IFASMFDP)
→ Enter を押す
［画面・出力］
IFASMFDP SMF DATA SET DUMP PROGRAM
RECORDS READ 00001234
RECORDS WRITTEN 00000456
RETURN CODE 0000
画面・出力にあるIFASMFDPを読み、入力期間と戻りコードと対象DUMP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へLISTDS SYS1.SMF.DUMP08を指定し、DUMP08の出力属性を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; LISTDS SYS1.SMF.DUMP08
→ Enter を押す
［画面・出力］
SYS1.SMF.DUMP08 RECFM=VBS LRECL=32760 BLKSIZE=0
画面・出力にあるRECFM=VBSを読み、入力期間と戻りコードと対象DUMP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へBROWSE SYS1.MAN08を指定し、DUMP08の入力確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; BROWSE SYS1.MAN08
→ Enter を押す
［画面・出力］
DATA SET NAME SYS1.MAN08 ORGANIZATION PS RECORD FORMAT VBS
画面・出力にあるORGANIZATIONを読み、入力期間と戻りコードと対象DUMP08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IFASMFDP が画面・出力に表示されること
② ステップ2 の RECFM=VBS が画面・出力に表示されること
③ ステップ3 の ORGANIZATION が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0160"><h3>SMFダンプ IFASMFDPダンプ 通常状態の確認 DUMP01</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>通常状態の確認では SMFダンプ の 入力確認 を主操作として DUMP01 を判定します。基準値と現在値の差への注意として「抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します」を DUMP01 に残します。通常状態の確認を補助する ダンプ実行 では IFASMFDP を補助値として DUMP01 へ保存します。主判定の通常状態の確認ではダンプ・入力期間と戻りコードの 入力確認 から ORGANIZATION を読み DUMP01 へ残します。証跡照合の通常状態の確認ではダンプ・入力期間と戻りコードの ORGANIZATION と IFASMFDP を DUMP01 に保存します。記録対応の通常状態の確認ではダンプ・入力期間と戻りコードの 入力期間と戻りコード の証跡へ DUMP01 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で SMFダンプ の 入力確認 と ダンプ実行 を使い 通常状態を確定 します。IFASMFDPダンプ はMANデータセットまたはログストリームから指定レコードを抽出し、監査または分析用データセットへコピーするユーティリティです。抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します。ORGANIZATION を読み対象 DUMP01 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. SUBMIT SYS1.SAMPLIB(IFASMFDP)のIFASMFDPを入力期間と戻りコードの主判定に採用する。BROWSE SYS1.MAN01の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. LISTDS SYS1.SMF.DUMP01のRECFM=VBSをORGANIZATIONと同義の成功表示として扱う。BROWSE SYS1.MAN01は実行しない。</li><li>C. BROWSE SYS1.MAN01を先に実行する。対象DUMP01のORGANIZATIONを入力期間と戻りコードとして記録する。続いてSUBMIT SYS1.SAMPLIB(IFASMFDP)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. BROWSE SYS1.MAN01が応答を返した時点で正常とする。応答中のORGANIZATIONの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Cは入力確認で ORGANIZATION を読み入力期間と戻りコードの主値として通常状態を確定しDUMP01に残します。
背景・仕組み: 通常状態の確認ではダンプ実行を補助操作としIFASMFDPダンプの基準値と現在値の差をIFASMFDPと対象DUMP01で照合します。
選択肢の理由: 入力確認とダンプ実行の役割を分けるとA: IFASMFDPはORGANIZATIONを代替しないうえに追加前提も不正な点でIFASMFDPダンプに使えません、B: RECFM=VBSとORGANIZATIONは確認項目が異なる点でDUMP01を採用できません、C: ORGANIZATIONを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけでは入力期間と戻りコードを判定できない点で一次資料と一致しません。結論として通常状態の確認のダンプ・入力期間と戻りコードで判定する対象は DUMP01 です。
用語の初出定義: 通常状態の確認で使う IFASMFDPダンプ はSMFダンプで入力期間と戻りコードを扱う機能を表し入力期間と戻りコードを判定する際にDUMP01へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFダンプ IFASMFDPダンプ 通常状態の確認 DUMP01</strong></p><p>検証目的: SMFダンプのIFASMFDPダンプについて通常状態を確定し、DUMP01の入力期間と戻りコードを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象DUMP01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へBROWSE SYS1.MAN01を指定し、DUMP01の入力確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; BROWSE SYS1.MAN01
→ Enter を押す
［画面・出力］
DATA SET NAME SYS1.MAN01 ORGANIZATION PS RECORD FORMAT VBS
画面・出力にあるORGANIZATIONを読み、入力期間と戻りコードと対象DUMP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へSUBMIT SYS1.SAMPLIB(IFASMFDP)を指定し、DUMP01のダンプ実行を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SUBMIT SYS1.SAMPLIB(IFASMFDP)
→ Enter を押す
［画面・出力］
IFASMFDP SMF DATA SET DUMP PROGRAM
RECORDS READ 00001234
RECORDS WRITTEN 00000456
RETURN CODE 0000
画面・出力にあるIFASMFDPを読み、入力期間と戻りコードと対象DUMP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へLISTDS SYS1.SMF.DUMP01を指定し、DUMP01の出力属性を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; LISTDS SYS1.SMF.DUMP01
→ Enter を押す
［画面・出力］
SYS1.SMF.DUMP01 RECFM=VBS LRECL=32760 BLKSIZE=0
画面・出力にあるRECFM=VBSを読み、入力期間と戻りコードと対象DUMP01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ORGANIZATION が画面・出力に表示されること
② ステップ2 の IFASMFDP が画面・出力に表示されること
③ ステップ3 の RECFM=VBS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0161"><h3>SMFダンプ IFASMFDPダンプ 障害切り分け DUMP04</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>障害切り分けでは SMFダンプ の 入力確認 を主操作として DUMP04 を判定します。最初に失敗した処理への注意として「抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します」を DUMP04 に残します。障害切り分けを補助する ダンプ実行 では IFASMFDP を補助値として DUMP04 へ保存します。主判定の障害切り分けではダンプ・入力期間と戻りコードの 入力確認 から ORGANIZATION を読み DUMP04 へ残します。証跡照合の障害切り分けではダンプ・入力期間と戻りコードの ORGANIZATION と IFASMFDP を DUMP04 に保存します。記録対応の障害切り分けではダンプ・入力期間と戻りコードの 入力期間と戻りコード の証跡へ DUMP04 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで SMFダンプ の 入力確認 と ダンプ実行 を照合し 最初に失敗した処理 を確かめます。IFASMFDPダンプ はMANデータセットまたはログストリームから指定レコードを抽出し、監査または分析用データセットへコピーするユーティリティです。抽出条件や時刻範囲を誤ると必要なSMFレコードが欠落します。ORGANIZATION を読む前に対象 DUMP04 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. LISTDS SYS1.SMF.DUMP04のRECFM=VBSをORGANIZATIONと同義の成功表示として扱う。BROWSE SYS1.MAN04は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. BROWSE SYS1.MAN04の出力でDUMP04とORGANIZATIONが同じ応答にあることを確認する。入力期間と戻りコードをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. BROWSE SYS1.MAN04が応答を返した時点で正常とする。応答中のORGANIZATIONの値は記録しない。</li><li>D. BROWSE SYS1.MAN04のコマンド文字列だけを記録する。ORGANIZATIONを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Bは入力確認で ORGANIZATION を読み入力期間と戻りコードの主値として障害範囲を限定しDUMP04に残します。
技術的背景: 障害切り分けではダンプ実行を補助操作としIFASMFDPダンプの最初に失敗した処理をIFASMFDPと対象DUMP04で照合します。
四択の評価: 入力確認とダンプ実行の役割を分けるとA: RECFM=VBSとORGANIZATIONは確認項目が異なるうえに追加前提も不正な点でDUMP04を採用できません、B: DUMP04とORGANIZATIONを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけでは入力期間と戻りコードを判定できない点で一次資料と一致しません、D: 入力記録だけでは入力期間と戻りコードを証明できない点で入力期間と戻りコードを確認できません。結論として障害切り分けのダンプ・入力期間と戻りコードで判定する対象は DUMP04 です。
初出語の意味: 障害切り分けで使う IFASMFDPダンプ はSMFダンプで入力期間と戻りコードを扱う機能を表し入力期間と戻りコードを判定する際にDUMP04へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFダンプ IFASMFDPダンプ 障害切り分け DUMP04</strong></p><p>検証目的: SMFダンプのIFASMFDPダンプについて障害範囲を限定し、DUMP04の入力期間と戻りコードを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象DUMP04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へBROWSE SYS1.MAN04を指定し、DUMP04の入力確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; BROWSE SYS1.MAN04
→ Enter を押す
［画面・出力］
DATA SET NAME SYS1.MAN04 ORGANIZATION PS RECORD FORMAT VBS
画面・出力にあるORGANIZATIONを読み、入力期間と戻りコードと対象DUMP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へSUBMIT SYS1.SAMPLIB(IFASMFDP)を指定し、DUMP04のダンプ実行を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SUBMIT SYS1.SAMPLIB(IFASMFDP)
→ Enter を押す
［画面・出力］
IFASMFDP SMF DATA SET DUMP PROGRAM
RECORDS READ 00001234
RECORDS WRITTEN 00000456
RETURN CODE 0000
画面・出力にあるIFASMFDPを読み、入力期間と戻りコードと対象DUMP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMFダンプを確認する入力画面です。COMMAND入力口へLISTDS SYS1.SMF.DUMP04を指定し、DUMP04の出力属性を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; LISTDS SYS1.SMF.DUMP04
→ Enter を押す
［画面・出力］
SYS1.SMF.DUMP04 RECFM=VBS LRECL=32760 BLKSIZE=0
画面・出力にあるRECFM=VBSを読み、入力期間と戻りコードと対象DUMP04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ORGANIZATION が画面・出力に表示されること
② ステップ2 の IFASMFDP が画面・出力に表示されること
③ ステップ3 の RECFM=VBS が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0162"><h3>WTORマクロ 権限確認 運用確認022</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>第二十二観点 WTORマクロ は z/OS System Programming の SMFダンプ で扱う管理項目です（第二十二観点）。第二十二観点 オペレーター応答を必要とするメッセージを発行し、返信番号で応答を受けという説明を操作結果と照合します（第二十二観点）。第二十二観点 SYS1.SVCLIB、DISPLAY GRS のISG343I表示、定義メンバーを照合し、割り込み経路の説明性確保を確認します（第二十二観点）。第二十二観点 証跡には資料IDと確認値を併記し、zOSSP記録022として保存します（第二十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第二十二証跡です。WTORマクロ に関する設定変更を扱います。確認観点は WTORマクロ、権限確認、運用確認 です。割り込み経路の説明性確保のために、DISPLAY GRS のISG343I表示 を使った運用記録として最も適切な扱いはどれか。</p><ul class="kb-choices"><li>A. DISPLAY GRS のISG343I表示 と SYS1.SVCLIB を同一票へ記録し、WTORマクロ を zOSSP正022で確定する。 <span class="kb-ok">✅ 正解</span></li><li>B. WTOメッセージ の一般メモを採り、SYS1.SVCLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記022として調査範囲を狭める。</li><li>C. WTORマクロ の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延022として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在022として残す。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第二十二観点 正答根拠: Aは DISPLAY GRS のISG343I表示 と SYS1.SVCLIB を結び付けるため、対象システムの取り違えを防げます（第二十二観点）。第二十二観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第二十二観点）。第二十二観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第二十二観点）。第二十二観点 用語説明: WTOは通知メッセージです（第二十二観点）。第二十二観点 WTORは応答を求めるメッセージです（第二十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTORマクロ 権限確認 運用確認022</strong></p><p>検証目的: WTORマクロ の 権限確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: IPCS / dump analysis</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により WTORマクロ の値を確認し、対象の現在値を固定する。
［操作（入力）］
IPCS option 6
COMMAND ===&gt; VERBX LOGDATA
→ Enter を押す
［画面・出力］
LOGDATA VERBEXIT PROCESSING
LOGREC BUFFER RECORDS LOCATED
EREP DETAIL EDIT REPORT FOLLOWS
画面・出力には LOGDATA が含まれる。LOGDATA を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により WTORマクロ の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.30.22 TRACE DISPLAY 191
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON MT=(ON,024K)
画面・出力には IEE843I が含まれる。IEE843I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により WTORマクロ の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
IPCS command line
COMMAND ===&gt; STATUS CPU
→ Enter を押す
［画面・出力］
IPCS STATUS CPU
PSW=070C1000 81234567  ASID=0010
CURRENT TCB ADDRESS SYS1.SVCLIB
画面・出力には ASID=0010 が含まれる。ASID=0010 を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LOGDATA が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE843I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ASID=0010 が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0163"><h3>WTOマクロ 権限確認 運用確認072</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 中級</p><p>第七十二観点 z/OS System Programming の SMFダンプ では WTOマクロ を障害調査で照合します（第七十二観点）。第七十二観点 資料上は プログラムからオペレーターとハードコピー・ログへメッセージを送るマクとして扱います（第七十二観点）。第七十二観点 ASID=0010 を起点に表示値を戻し、割り込み経路の説明性確保を点検します（第七十二観点）。第七十二観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録072へ書きます（第七十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第七十二証跡です。WTOマクロ に関する設定変更を扱います。確認観点は WTOマクロ、権限確認、運用確認 です。割り込み経路の説明性確保を満たす記録方法として、表示値と定義を結ぶものはどれか。</p><ul class="kb-choices"><li>A. LOGREC診断 の一般メモを採り、ASID=0010、メッセージID、時刻の対応を記録外に置き、zOSSP誤記072として調査範囲を狭める。</li><li>B. WTOマクロ の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延072として扱う。</li><li>C. DISPLAY GRS のISG343I表示 と ASID=0010 を同一票へ記録し、WTOマクロ を zOSSP正072で確定する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在072として残す。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第七十二観点 照合結果: Cは ASID=0010 をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第七十二観点）。第七十二観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第七十二観点）。第七十二観点 誤答確認: Aは ASID=0010 未追跡、Bはコマンド確認不足、Dは別システム混同が理由です（第七十二観点）。第七十二観点 初出定義: PSWは実行状態を示す語です（第七十二観点）。第七十二観点 SVCは監視プログラム呼出しです（第七十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOマクロ 権限確認 運用確認072</strong></p><p>検証目的: WTOマクロ の 権限確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: ISPF / SAF review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により WTOマクロ の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(IEASYS24)
→ Enter を押す
［画面・出力］
IEASYS24
PROG=SP
SMF=SP
GRSRNL=SP
LNKAUTH=LNKLST
画面・出力には LNKAUTH が含まれる。LNKAUTH を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により WTOマクロ の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX CSV
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
CSV450I PROG,APF DISPLAY
画面・出力には CSV410I が含まれる。CSV410I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により WTOマクロ の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX IEE
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE536I が含まれる。IEE536I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LNKAUTH が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE536I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0164"><h3>システムキー 優先順位確認 運用確認089</h3><p class="kb-meta">分類: SMFダンプ ・ 難易度: 上級</p><p>第八十九観点 SMFダンプ で システムキー は 優先順位確認 の対象です（第八十九観点）。第八十九観点 確認時には キー0から7の保護キーで実行され、保護されたデータへ到達できる権限という性質を前提にします（第八十九観点）。第八十九観点 D PROG,APF のCSV450I表示 と DUMPIN を同じ証跡に置き、SMF記録欠落の早期検出を管理します（第八十九観点）。第八十九観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録089から再現します（第八十九観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システムキー 優先順位確認 運用確認089</strong></p><p>検証目的: システムキー の 優先順位確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SDSF LOG</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により システムキー の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 05.18.17 PROG,APF DISPLAY 908
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   2  MPRES1 SYS1.SVCLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により システムキー の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SETPROG APF,ADD,DSNAME=MYPROG.LOADLIB,VOLUME=MPRES3
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
画面・出力には CSV410I が含まれる。CSV410I を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により システムキー の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF,ENTRY=(1-5)
→ Enter を押す
［画面・出力］
CSV450I 05.26.17 PROG,APF DISPLAY 958
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   5  MPRES1 ISF.SISFLPA
画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


## SMF記録


<section class="kb-item" id="c38-i0165"><h3>D PROG,APF 出口確認 運用確認055</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>第五十五観点 SMF記録 の運用では D PROG,APF を表示、定義、証跡で確認します（第五十五観点）。第五十五観点 役割は APF許可ライブラリーのエントリー番号、ボリューム、データセット名をという範囲です（第五十五観点）。第五十五観点 IFASMFDPジョブログのSYSPRINT の値を WTOR reply 005 と合わせ、アドレス空間分離の確認を記録します（第五十五観点）。第五十五観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録055に残します（第五十五観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第五十五証跡です。IFASMFDPジョブログのSYSPRINT を採取した後の扱いを選びます。確認観点は D PROG、出口確認、運用確認 です。WTOR reply 005 を根拠として残す時、対象の取り違えを抑える対応はどれか。</p><ul class="kb-choices"><li>A. PROGxx運用 の一般メモを採り、WTOR reply 005、メッセージID、時刻の対応を記録外に置き、zOSSP誤記055として調査範囲を狭める。</li><li>B. D PROG,APF の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延055として扱う。</li><li>C. IFASMFDPジョブログのSYSPRINT と WTOR reply 005 を同一票へ記録し、D PROG を zOSSP正055で確定する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在055として残す。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第五十五観点 採用理由: Cは D PROG の状態を表示値と定義の両方から確認するため、記録として妥当です（第五十五観点）。第五十五観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第五十五観点）。第五十五観点 誤答整理: Aは一般メモ偏重、Bはジョブログ除外、Dは再現性不足が理由です（第五十五観点）。第五十五観点 用語確認: APFは許可ライブラリーの管理機能です（第五十五観点）。第五十五観点 PROGxxは動的なプログラム管理指定です（第五十五観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PROG,APF 出口確認 運用確認055</strong></p><p>検証目的: D PROG,APF の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / WLM dispatch</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により D PROG,APF の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.05.07 ACTIVE JOBS DISPLAY 654
JOBNAME  ASID  STATUS
WLM      000A  ACTIVE
JES2     0012  ACTIVE
画面・出力には IEE114I が含まれる。IEE114I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により D PROG,APF の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D WLM,SYSTEMS
→ Enter を押す
［画面・出力］
IWM026I 12.06.07 WLM DISPLAY 664
SYSTEM   MODE     POLICY
SC65     GOAL     POLSP07
画面・出力には GOAL が含まれる。GOAL を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により D PROG,APF の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
SDSF DA panel
COMMAND ===&gt; DA
→ Enter を押す
［画面・出力］
SDSF DA DISPLAY
JOBNAME  ASID  CPU%  DP
BATCH07 0007  02.1  245
画面・出力には JOBNAME が含まれる。JOBNAME を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE114I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: GOAL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: JOBNAME が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0166"><h3>ISGDGRSRES出口 定義照合 運用確認071</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>第七十一観点 SMF記録 の運用では ISGDGRSRES出口 を表示、定義、証跡で確認します（第七十一観点）。第七十一観点 役割は DISPLAY GRS出力へアプリケーション固有の資源説明を補うインという範囲です（第七十一観点）。第七十一観点 SET PROG=xx後のIEE252I表示 の値を TRACE DISPLAY と合わせ、資源競合時の保有者確認を記録します（第七十一観点）。第七十一観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録071に残します（第七十一観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ISGDGRSRES出口 定義照合 運用確認071</strong></p><p>検証目的: ISGDGRSRES出口 の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / WLM dispatch</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により ISGDGRSRES出口 の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.05.23 ACTIVE JOBS DISPLAY 670
JOBNAME  ASID  STATUS
WLM      000A  ACTIVE
JES2     0012  ACTIVE
画面・出力には IEE114I が含まれる。IEE114I を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により ISGDGRSRES出口 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D WLM,SYSTEMS
→ Enter を押す
［画面・出力］
IWM026I 12.06.23 WLM DISPLAY 680
SYSTEM   MODE     POLICY
SC65     GOAL     POLSP23
画面・出力には GOAL が含まれる。GOAL を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により ISGDGRSRES出口 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
SDSF DA panel
COMMAND ===&gt; DA
→ Enter を押す
［画面・出力］
SDSF DA DISPLAY
JOBNAME  ASID  CPU%  DP
BATCH23 0023  02.1  245
画面・出力には JOBNAME が含まれる。JOBNAME を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE114I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: GOAL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: JOBNAME が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0167"><h3>LPA探索順序 出口確認 運用確認005</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 初級</p><p>第五観点 SMF記録 で LPA探索順序 は 出口確認 の対象です（第五観点）。第五観点 確認時には 動的LPA、FLPA、MLPA、PLPAの順に共通ストレージ上のモジという性質を前提にします（第五観点）。第五観点 IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を同じ証跡に置き、アドレス空間分離の確認を管理します（第五観点）。第五観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録005から再現します（第五観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LPA探索順序 出口確認 運用確認005</strong></p><p>検証目的: LPA探索順序 の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / operations</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により LPA探索順序 の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY R,ALL
→ Enter を押す
［画面・出力］
IEE112I 11.15.05 DISPLAY R 704
REPLY ID   MESSAGE TEXT
005        IEA793A SPECIFY DUMP OPTION FOR QNAME=SYSDSN
画面・出力には IEE112I が含まれる。IEE112I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により LPA探索順序 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D C
→ Enter を押す
［画面・出力］
IEE889I 15.33.05 CONSOLE DISPLAY 494
MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
画面・出力には IEE889I が含まれる。IEE889I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により LPA探索順序 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; R 005,INFO
→ Enter を押す
［画面・出力］
IEE600I REPLY TO 005 IS;INFO
IEA631I OPERATOR OPER05 NOW ACTIVE, SYSTEM=SC65
画面・出力には IEE600I が含まれる。IEE600I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0168"><h3>SAF呼出し ストレージ確認 運用確認088</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 上級</p><p>第八十八観点 z/OS System Programming の SMF記録 では SAF呼出し を障害調査で照合します（第八十八観点）。第八十八観点 資料上は セキュリティサービス要求を外部セキュリティ管理製品へ中継するシステムとして扱います（第八十八観点）。第八十八観点 SMF.LOGSTREAM.SP を起点に表示値を戻し、parmlib反映範囲の追跡を点検します（第八十八観点）。第八十八観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録088へ書きます（第八十八観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第八十八証跡です。SAF呼出し の記録を監査用に整えます。確認観点は SAF呼出し、ストレージ確認、運用確認 です。parmlib反映範囲の追跡のために、parmlibメンバーの該当ステートメント を使った運用記録として最も適切な扱いはどれか。</p><ul class="kb-choices"><li>A. アドレス空間 の一般メモを採り、SMF.LOGSTREAM.SP、メッセージID、時刻の対応を記録外に置き、zOSSP誤記088として調査範囲を狭める。</li><li>B. SAF呼出し の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延088として扱う。</li><li>C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在088として残す。</li><li>D. parmlibメンバーの該当ステートメント と SMF.LOGSTREAM.SP を同一票へ記録し、SAF呼出し を zOSSP正088で確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 第八十八観点 照合結果: Dは SMF.LOGSTREAM.SP をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第八十八観点）。第八十八観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第八十八観点）。第八十八観点 誤答確認: Aは SMF.LOGSTREAM.SP 未追跡、Bはコマンド確認不足、Cは別システム混同が理由です（第八十八観点）。第八十八観点 用語説明: WTOは通知メッセージです（第八十八観点）。第八十八観点 WTORは応答を求めるメッセージです（第八十八観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SAF呼出し ストレージ確認 運用確認088</strong></p><p>検証目的: SAF呼出し の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: ISPF / SAF review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SAF呼出し の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(IEASYS16)
→ Enter を押す
［画面・出力］
IEASYS16
PROG=SP
SMF=SP
GRSRNL=SP
LNKAUTH=LNKLST
画面・出力には LNKAUTH が含まれる。LNKAUTH を読み取り、parmlib反映範囲の追跡のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SAF呼出し の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX CSV
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
CSV450I PROG,APF DISPLAY
画面・出力には CSV410I が含まれる。CSV410I を読み取り、parmlib反映範囲の追跡のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SAF呼出し の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX IEE
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE536I が含まれる。IEE536I を読み取り、parmlib反映範囲の追跡のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LNKAUTH が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE536I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0169"><h3>SMF記録 SMF稼働状態 ログとの照合 SMF07</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>ログとの照合では SMF記録 の SMF表示 を主操作として SMF07 を判定します。時刻と対象識別子への注意として「記録停止やデータセット切替待ちを見落とすと監査期間が欠けます」を SMF07 に残します。ログとの照合を補助する データセット表示 では IEE975I を補助値として SMF07 へ保存します。主判定のログとの照合では記録・稼働状態の SMF表示 から IEE974I を読み SMF07 へ残します。証跡照合のログとの照合では記録・稼働状態の IEE974I と IEE975I を SMF07 に保存します。記録対応のログとの照合では記録・稼働状態の ACTIVE DATASETとRECORDING の証跡へ SMF07 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で SMF記録 の SMF表示 と データセット表示 を用い 操作とログを対応 します。SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能です。記録停止やデータセット切替待ちを見落とすと監査期間が欠けます。IEE974I で対象 SMF07 の ACTIVE DATASETとRECORDING を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. D SMFが応答を返した時点で正常とする。応答中のIEE974Iの値は記録しない。SMFPRMをIEE974Iと同じ判定値とみなし対象SMF07の主証跡にする。SMF稼働状態の時刻と対象識別子は確認済みとして扱う。さらにD PARMLIB(SMFPRM07)のSMFPRMをIEE974Iと同種の値として併記する。</li><li>B. D SMFのコマンド文字列だけを記録する。IEE974Iを含む応答行は保存しない。</li><li>C. IEE974Iを含むSMF表示の応答行を保存する。その応答を得るためD SMFを使用する。対象SMF07のACTIVE DATASETとRECORDINGとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. SMF稼働状態の停止または再定義を実施する。その後にD SMFでIEE974Iを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: CはSMF表示で IEE974I を読みACTIVE DATASETとRECORDINGの主値として操作とログを対応しSMF07に残します。
機能の仕組み: ログとの照合ではデータセット表示を補助操作としSMF稼働状態の時刻と対象識別子をIEE975Iと対象SMF07で照合します。
各候補の評価: SMF表示とデータセット表示の役割を分けるとA: 応答の有無だけではACTIVE DATASETとRECORDINGを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではACTIVE DATASETとRECORDINGを証明できない点で一次資料と一致しません、C: IEE974Iの実値を対象別に残す点でSMF07を判定できます、D: 変更前のACTIVE DATASETとRECORDINGを失う点でデータセット表示の範囲を越えます。結論としてログとの照合の記録・稼働状態で判定する対象は SMF07 です。
用語の定義: ログとの照合で使う SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能を表しACTIVE DATASETとRECORDINGを判定する際にSMF07へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF記録 SMF稼働状態 ログとの照合 SMF07</strong></p><p>検証目的: SMF記録のSMF稼働状態について操作とログを対応し、SMF07のACTIVE DATASETとRECORDINGを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SMF07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMFを指定し、SMF07のSMF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF
→ Enter を押す
［画面・出力］
IEE974I 12.15.30 SMF DATA
STATUS ACTIVE
DATA SET NAME SYS1.MAN1 RECORDING
画面・出力にあるIEE974Iを読み、ACTIVE DATASETとRECORDINGと対象SMF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMF,Sを指定し、SMF07のデータセット表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF,S
→ Enter を押す
［画面・出力］
IEE975I SMF DATA SET STATUS SYS1.MAN1 ACTIVE SYS1.MAN2 ALTERNATE
画面・出力にあるIEE975Iを読み、ACTIVE DATASETとRECORDINGと対象SMF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD PARMLIB(SMFPRM07)を指定し、SMF07のparmlib確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PARMLIB(SMFPRM07)
→ Enter を押す
［画面・出力］
IEE252I MEMBER SMFPRM07 FOUND IN SYS1.PARMLIB
画面・出力にあるSMFPRMを読み、ACTIVE DATASETとRECORDINGと対象SMF07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE974I が画面・出力に表示されること
② ステップ2 の IEE975I が画面・出力に表示されること
③ ステップ3 の SMFPRM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0170"><h3>SMF記録 SMF稼働状態 代替経路の確認 SMF10</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>代替経路の確認では SMF記録 の SMF表示 を主操作として SMF10 を判定します。主経路との役割差への注意として「記録停止やデータセット切替待ちを見落とすと監査期間が欠けます」を SMF10 に残します。代替経路の確認を補助する データセット表示 では IEE975I を補助値として SMF10 へ保存します。主判定の代替経路の確認では記録・稼働状態の SMF表示 から IEE974I を読み SMF10 へ残します。証跡照合の代替経路の確認では記録・稼働状態の IEE974I と IEE975I を SMF10 に保存します。記録対応の代替経路の確認では記録・稼働状態の ACTIVE DATASETとRECORDING の証跡へ SMF10 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で SMF記録 の SMF表示 と データセット表示 の役割を分け 主経路との役割差 を調べます。SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能です。記録停止やデータセット切替待ちを見落とすと監査期間が欠けます。対象 SMF10 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. D SMFのコマンド文字列だけを記録する。IEE974Iを含む応答行は保存しない。</li><li>B. D SMFとD SMF,Sの対象名をそろえる。前者のIEE974IをACTIVE DATASETとRECORDINGの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. SMF稼働状態の停止または再定義を実施する。その後にD SMFでIEE974Iを採取する。</li><li>D. SVC処理のSVC番号とROUTINEを確認する。その値をSMF記録のSMF10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: BはSMF表示で IEE974I を読みACTIVE DATASETとRECORDINGの主値として代替手段の成立を確認しSMF10に残します。
運用上の背景: 代替経路の確認ではデータセット表示を補助操作としSMF稼働状態の主経路との役割差をIEE975Iと対象SMF10で照合します。
候補別の検討: SMF表示とデータセット表示の役割を分けるとA: 入力記録だけではACTIVE DATASETとRECORDINGを証明できない点で一次資料と一致しません、B: 同じ対象名のIEE974Iを採用する点でSMF10を判定できます、C: 変更前のACTIVE DATASETとRECORDINGを失う点でデータセット表示の範囲を越えます、D: SVC処理の値ではIEE974Iを確認できない点でSMF10の値を示しません。結論として代替経路の確認の記録・稼働状態で判定する対象は SMF10 です。
重要用語の定義: 代替経路の確認で使う SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能を表しACTIVE DATASETとRECORDINGを判定する際にSMF10へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF記録 SMF稼働状態 代替経路の確認 SMF10</strong></p><p>検証目的: SMF記録のSMF稼働状態について代替手段の成立を確認し、SMF10のACTIVE DATASETとRECORDINGを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SMF10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMFを指定し、SMF10のSMF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF
→ Enter を押す
［画面・出力］
IEE974I 12.15.30 SMF DATA
STATUS ACTIVE
DATA SET NAME SYS1.MAN1 RECORDING
画面・出力にあるIEE974Iを読み、ACTIVE DATASETとRECORDINGと対象SMF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMF,Sを指定し、SMF10のデータセット表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF,S
→ Enter を押す
［画面・出力］
IEE975I SMF DATA SET STATUS SYS1.MAN1 ACTIVE SYS1.MAN2 ALTERNATE
画面・出力にあるIEE975Iを読み、ACTIVE DATASETとRECORDINGと対象SMF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD PARMLIB(SMFPRM10)を指定し、SMF10のparmlib確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PARMLIB(SMFPRM10)
→ Enter を押す
［画面・出力］
IEE252I MEMBER SMFPRM10 FOUND IN SYS1.PARMLIB
画面・出力にあるSMFPRMを読み、ACTIVE DATASETとRECORDINGと対象SMF10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE974I が画面・出力に表示されること
② ステップ2 の IEE975I が画面・出力に表示されること
③ ステップ3 の SMFPRM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0171"><h3>SMF記録 SMF稼働状態 変更前の確認 SMF02</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>変更前の確認では SMF記録 の データセット表示 を主操作として SMF02 を判定します。変更対象と非対象の境界への注意として「記録停止やデータセット切替待ちを見落とすと監査期間が欠けます」を SMF02 に残します。変更前の確認を補助する parmlib確認 では SMFPRM を補助値として SMF02 へ保存します。主判定の変更前の確認では記録・稼働状態の データセット表示 から IEE975I を読み SMF02 へ残します。証跡照合の変更前の確認では記録・稼働状態の IEE975I と SMFPRM を SMF02 に保存します。記録対応の変更前の確認では記録・稼働状態の ACTIVE DATASETとRECORDING の証跡へ SMF02 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で SMF記録 の データセット表示 と parmlib確認 を照合し 変更対象と非対象の境界 を確かめます。SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能です。記録停止やデータセット切替待ちを見落とすと監査期間が欠けます。IEE975I を読む前に対象 SMF02 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. D SMF,Sを対象名なしで実行する。一覧の先頭行をSMF02の結果として記録する。</li><li>B. 対象SMF02についてD SMF,Sの応答からIEE975Iを確認する。D PARMLIB(SMFPRM02)は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存したD SMF,Sの結果を使う。今回のD PARMLIB(SMFPRM02)の結果と同一時点の証跡として比較する。</li><li>D. 保存済みのSMF02の出力を再利用する。今回のD SMF,SとD PARMLIB(SMFPRM02)は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Bはデータセット表示で IEE975I を読みACTIVE DATASETとRECORDINGの主値として変更前の証跡を保存しSMF02に残します。
動作の背景: 変更前の確認ではparmlib確認を補助操作としSMF稼働状態の変更対象と非対象の境界をSMFPRMと対象SMF02で照合します。
各選択肢の検討: データセット表示とparmlib確認の役割を分けるとA: 先頭行はSMF02と確定できない点で変更前の確認に合いません、B: IEE975Iと補助証跡の時刻を合わせる点でデータセット表示に合います、C: 採取時刻が異なる点でSMF記録に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でSMF稼働状態に使えません。結論として変更前の確認の記録・稼働状態で判定する対象は SMF02 です。
初出用語の定義: 変更前の確認で使う SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能を表しACTIVE DATASETとRECORDINGを判定する際にSMF02へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF記録 SMF稼働状態 変更前の確認 SMF02</strong></p><p>検証目的: SMF記録のSMF稼働状態について変更前の証跡を保存し、SMF02のACTIVE DATASETとRECORDINGを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SMF02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMF,Sを指定し、SMF02のデータセット表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF,S
→ Enter を押す
［画面・出力］
IEE975I SMF DATA SET STATUS SYS1.MAN1 ACTIVE SYS1.MAN2 ALTERNATE
画面・出力にあるIEE975Iを読み、ACTIVE DATASETとRECORDINGと対象SMF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD PARMLIB(SMFPRM02)を指定し、SMF02のparmlib確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PARMLIB(SMFPRM02)
→ Enter を押す
［画面・出力］
IEE252I MEMBER SMFPRM02 FOUND IN SYS1.PARMLIB
画面・出力にあるSMFPRMを読み、ACTIVE DATASETとRECORDINGと対象SMF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMFを指定し、SMF02のSMF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF
→ Enter を押す
［画面・出力］
IEE974I 12.15.30 SMF DATA
STATUS ACTIVE
DATA SET NAME SYS1.MAN1 RECORDING
画面・出力にあるIEE974Iを読み、ACTIVE DATASETとRECORDINGと対象SMF02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE975I が画面・出力に表示されること
② ステップ2 の SMFPRM が画面・出力に表示されること
③ ステップ3 の IEE974I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0172"><h3>SMF記録 SMF稼働状態 変更後の確認 SMF03</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>変更後の確認では SMF記録 の parmlib確認 を主操作として SMF03 を判定します。反映値と残存値への注意として「記録停止やデータセット切替待ちを見落とすと監査期間が欠けます」を SMF03 に残します。変更後の確認を補助する SMF表示 では IEE974I を補助値として SMF03 へ保存します。主判定の変更後の確認では記録・稼働状態の parmlib確認 から SMFPRM を読み SMF03 へ残します。証跡照合の変更後の確認では記録・稼働状態の SMFPRM と IEE974I を SMF03 に保存します。記録対応の変更後の確認では記録・稼働状態の ACTIVE DATASETとRECORDING の証跡へ SMF03 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で SMF記録 の parmlib確認 と SMF表示 を組み合わせる際は SMF稼働状態 がシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能という仕組みを前提にします。記録停止やデータセット切替待ちを見落とすと監査期間が欠けます。SMFPRM と ACTIVE DATASETとRECORDING を対象 SMF03 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. SMF稼働状態の停止または再定義を実施する。その後にD PARMLIB(SMFPRM03)でSMFPRMを採取する。</li><li>B. LNKLST管理のSET名とDATASET順序を確認する。その値をSMF記録のSMF03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>C. D SMFで周辺状態を押さえる。その後にD PARMLIB(SMFPRM03)でSMFPRMを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. D SMFが成功したためD PARMLIB(SMFPRM03)のSMFPRMも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: Cはparmlib確認で SMFPRM を読みACTIVE DATASETとRECORDINGの主値として変更結果を検証しSMF03に残します。
内部の仕組み: 変更後の確認ではSMF表示を補助操作としSMF稼働状態の反映値と残存値をIEE974Iと対象SMF03で照合します。
誤答を含む比較: parmlib確認とSMF表示の役割を分けるとA: 変更前のACTIVE DATASETとRECORDINGを失う点でACTIVE DATASETとRECORDINGを確認できません、B: LNKLST管理の値ではSMFPRMを確認できないうえに追加前提も不正な点でSMF表示の範囲を越えます、C: 周辺状態の後にSMFPRMを確認する点で現在値を示します、D: 補助操作の成功ではSMFPRMを確定できない点で変更後の確認に合いません。結論として変更後の確認の記録・稼働状態で判定する対象は SMF03 です。
用語定義: 変更後の確認で使う SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能を表しACTIVE DATASETとRECORDINGを判定する際にSMF03へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF記録 SMF稼働状態 変更後の確認 SMF03</strong></p><p>検証目的: SMF記録のSMF稼働状態について変更結果を検証し、SMF03のACTIVE DATASETとRECORDINGを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SMF03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD PARMLIB(SMFPRM03)を指定し、SMF03のparmlib確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PARMLIB(SMFPRM03)
→ Enter を押す
［画面・出力］
IEE252I MEMBER SMFPRM03 FOUND IN SYS1.PARMLIB
画面・出力にあるSMFPRMを読み、ACTIVE DATASETとRECORDINGと対象SMF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMFを指定し、SMF03のSMF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF
→ Enter を押す
［画面・出力］
IEE974I 12.15.30 SMF DATA
STATUS ACTIVE
DATA SET NAME SYS1.MAN1 RECORDING
画面・出力にあるIEE974Iを読み、ACTIVE DATASETとRECORDINGと対象SMF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMF,Sを指定し、SMF03のデータセット表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF,S
→ Enter を押す
［画面・出力］
IEE975I SMF DATA SET STATUS SYS1.MAN1 ACTIVE SYS1.MAN2 ALTERNATE
画面・出力にあるIEE975Iを読み、ACTIVE DATASETとRECORDINGと対象SMF03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SMFPRM が画面・出力に表示されること
② ステップ2 の IEE974I が画面・出力に表示されること
③ ステップ3 の IEE975I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0173"><h3>SMF記録 SMF稼働状態 引継ぎ記録 SMF09</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>引継ぎ記録では SMF記録 の parmlib確認 を主操作として SMF09 を判定します。次担当者が追跡できる証跡への注意として「記録停止やデータセット切替待ちを見落とすと監査期間が欠けます」を SMF09 に残します。引継ぎ記録を補助する SMF表示 では IEE974I を補助値として SMF09 へ保存します。主判定の引継ぎ記録では記録・稼働状態の parmlib確認 から SMFPRM を読み SMF09 へ残します。証跡照合の引継ぎ記録では記録・稼働状態の SMFPRM と IEE974I を SMF09 に保存します。記録対応の引継ぎ記録では記録・稼働状態の ACTIVE DATASETとRECORDING の証跡へ SMF09 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で SMF記録 の parmlib確認 と SMF表示 を組み合わせる際は SMF稼働状態 がシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能という仕組みを前提にします。記録停止やデータセット切替待ちを見落とすと監査期間が欠けます。SMFPRM と ACTIVE DATASETとRECORDING を対象 SMF09 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 対象名SMF09を指定してD PARMLIB(SMFPRM09)を実行する。応答中のSMFPRMと時刻を保存する。D SMFで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. D SMFが成功したためD PARMLIB(SMFPRM09)のSMFPRMも正常だと推定する。主出力は保存しない。</li><li>C. D PARMLIB(SMFPRM09)を対象名なしで実行する。一覧の先頭行をSMF09の結果として記録する。</li><li>D. 前回保存したD PARMLIB(SMFPRM09)の結果を使う。今回のD SMFの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: Aはparmlib確認で SMFPRM を読みACTIVE DATASETとRECORDINGの主値として再現可能な記録を作成しSMF09に残します。
製品内の仕組み: 引継ぎ記録ではSMF表示を補助操作としSMF稼働状態の次担当者が追跡できる証跡をIEE974Iと対象SMF09で照合します。
選択肢別の説明: parmlib確認とSMF表示の役割を分けるとA: SMFPRMと時刻を保存する点で現在値を示します、B: 補助操作の成功ではSMFPRMを確定できない点で引継ぎ記録に合いません、C: 先頭行はSMF09と確定できない点でparmlib確認を代替しません、D: 採取時刻が異なる点でSMF記録に使いません。結論として引継ぎ記録の記録・稼働状態で判定する対象は SMF09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能を表しACTIVE DATASETとRECORDINGを判定する際にSMF09へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF記録 SMF稼働状態 引継ぎ記録 SMF09</strong></p><p>検証目的: SMF記録のSMF稼働状態について再現可能な記録を作成し、SMF09のACTIVE DATASETとRECORDINGを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SMF09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD PARMLIB(SMFPRM09)を指定し、SMF09のparmlib確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PARMLIB(SMFPRM09)
→ Enter を押す
［画面・出力］
IEE252I MEMBER SMFPRM09 FOUND IN SYS1.PARMLIB
画面・出力にあるSMFPRMを読み、ACTIVE DATASETとRECORDINGと対象SMF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMFを指定し、SMF09のSMF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF
→ Enter を押す
［画面・出力］
IEE974I 12.15.30 SMF DATA
STATUS ACTIVE
DATA SET NAME SYS1.MAN1 RECORDING
画面・出力にあるIEE974Iを読み、ACTIVE DATASETとRECORDINGと対象SMF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMF,Sを指定し、SMF09のデータセット表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF,S
→ Enter を押す
［画面・出力］
IEE975I SMF DATA SET STATUS SYS1.MAN1 ACTIVE SYS1.MAN2 ALTERNATE
画面・出力にあるIEE975Iを読み、ACTIVE DATASETとRECORDINGと対象SMF09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SMFPRM が画面・出力に表示されること
② ステップ2 の IEE974I が画面・出力に表示されること
③ ステップ3 の IEE975I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0174"><h3>SMF記録 SMF稼働状態 復旧後の確認 SMF06</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>復旧後の確認では SMF記録 の parmlib確認 を主操作として SMF06 を判定します。再発していないことを示す値への注意として「記録停止やデータセット切替待ちを見落とすと監査期間が欠けます」を SMF06 に残します。復旧後の確認を補助する SMF表示 では IEE974I を補助値として SMF06 へ保存します。主判定の復旧後の確認では記録・稼働状態の parmlib確認 から SMFPRM を読み SMF06 へ残します。証跡照合の復旧後の確認では記録・稼働状態の SMFPRM と IEE974I を SMF06 に保存します。記録対応の復旧後の確認では記録・稼働状態の ACTIVE DATASETとRECORDING の証跡へ SMF06 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で SMF記録 の parmlib確認 と SMF表示 を実施し SMF稼働状態 の役割を確認します。記録停止やデータセット切替待ちを見落とすと監査期間が欠けます。対象 SMF06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. GRS資源直列化のSYSTEMとMODEを確認する。その値をSMF記録のSMF06にも適用する。</li><li>B. D PARMLIB(SMFPRM06)でSMFPRMを取得してからD SMF,SでIEE975Iを照合する。SMF06のACTIVE DATASETとRECORDINGを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D SMFが成功したためD PARMLIB(SMFPRM06)のSMFPRMも正常だと推定する。主出力は保存しない。別資源で得た状態を対象SMF06へ引き継げるものとする。SMF稼働状態の再発していないことを示す値は確認済みとして扱う。さらにD SMF,SのIEE975IをSMFPRMと同種の値として併記する。</li><li>D. D PARMLIB(SMFPRM06)を対象名なしで実行する。一覧の先頭行をSMF06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Bはparmlib確認で SMFPRM を読みACTIVE DATASETとRECORDINGの主値として復旧後の安定性を確認しSMF06に残します。
構成上の背景: 復旧後の確認ではSMF表示を補助操作としSMF稼働状態の再発していないことを示す値をIEE974Iと対象SMF06で照合します。
候補ごとの理由: parmlib確認とSMF表示の役割を分けるとA: GRS資源直列化の値ではSMFPRMを確認できない点でSMF表示の範囲を越えます、B: SMFPRMとIEE975Iを順に照合する点で現在値を示します、C: 補助操作の成功ではSMFPRMを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はSMF06と確定できない点でparmlib確認を代替しません。結論として復旧後の確認の記録・稼働状態で判定する対象は SMF06 です。
初出用語: 復旧後の確認で使う SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能を表しACTIVE DATASETとRECORDINGを判定する際にSMF06へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF記録 SMF稼働状態 復旧後の確認 SMF06</strong></p><p>検証目的: SMF記録のSMF稼働状態について復旧後の安定性を確認し、SMF06のACTIVE DATASETとRECORDINGを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SMF06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD PARMLIB(SMFPRM06)を指定し、SMF06のparmlib確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PARMLIB(SMFPRM06)
→ Enter を押す
［画面・出力］
IEE252I MEMBER SMFPRM06 FOUND IN SYS1.PARMLIB
画面・出力にあるSMFPRMを読み、ACTIVE DATASETとRECORDINGと対象SMF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMFを指定し、SMF06のSMF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF
→ Enter を押す
［画面・出力］
IEE974I 12.15.30 SMF DATA
STATUS ACTIVE
DATA SET NAME SYS1.MAN1 RECORDING
画面・出力にあるIEE974Iを読み、ACTIVE DATASETとRECORDINGと対象SMF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMF,Sを指定し、SMF06のデータセット表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF,S
→ Enter を押す
［画面・出力］
IEE975I SMF DATA SET STATUS SYS1.MAN1 ACTIVE SYS1.MAN2 ALTERNATE
画面・出力にあるIEE975Iを読み、ACTIVE DATASETとRECORDINGと対象SMF06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SMFPRM が画面・出力に表示されること
② ステップ2 の IEE974I が画面・出力に表示されること
③ ステップ3 の IEE975I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0175"><h3>SMF記録 SMF稼働状態 復旧準備 SMF05</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>復旧準備では SMF記録 の データセット表示 を主操作として SMF05 を判定します。再開前に必要な整合性への注意として「記録停止やデータセット切替待ちを見落とすと監査期間が欠けます」を SMF05 に残します。復旧準備を補助する parmlib確認 では SMFPRM を補助値として SMF05 へ保存します。主判定の復旧準備では記録・稼働状態の データセット表示 から IEE975I を読み SMF05 へ残します。証跡照合の復旧準備では記録・稼働状態の IEE975I と SMFPRM を SMF05 に保存します。記録対応の復旧準備では記録・稼働状態の ACTIVE DATASETとRECORDING の証跡へ SMF05 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で SMF記録 の データセット表示 と parmlib確認 を使い 復旧条件を確認 します。SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能です。記録停止やデータセット切替待ちを見落とすと監査期間が欠けます。IEE975I を読み対象 SMF05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずD SMF,Sを実行する。IEE975Iを保存する。差分はD PARMLIB(SMFPRM05)の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したD SMF,Sの結果を使う。今回のD PARMLIB(SMFPRM05)の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのSMF05の出力を再利用する。今回のD SMF,SとD PARMLIB(SMFPRM05)は実行済みとして扱う。</li><li>D. D PARMLIB(SMFPRM05)のSMFPRMをACTIVE DATASETとRECORDINGの主判定に採用する。D SMF,Sの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Aはデータセット表示で IEE975I を読みACTIVE DATASETとRECORDINGの主値として復旧条件を確認しSMF05に残します。
処理の仕組み: 復旧準備ではparmlib確認を補助操作としSMF稼働状態の再開前に必要な整合性をSMFPRMと対象SMF05で照合します。
選択結果の内訳: データセット表示とparmlib確認の役割を分けるとA: 変更前のIEE975Iを保存する点でデータセット表示に合います、B: 採取時刻が異なる点でSMF記録に使いません、C: 過去出力では今回の復旧準備を示せない点でSMF稼働状態に使えません、D: SMFPRMはIEE975Iを代替しないうえに追加前提も不正な点でSMF05を採用できません。結論として復旧準備の記録・稼働状態で判定する対象は SMF05 です。
用語の説明: 復旧準備で使う SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能を表しACTIVE DATASETとRECORDINGを判定する際にSMF05へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF記録 SMF稼働状態 復旧準備 SMF05</strong></p><p>検証目的: SMF記録のSMF稼働状態について復旧条件を確認し、SMF05のACTIVE DATASETとRECORDINGを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SMF05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMF,Sを指定し、SMF05のデータセット表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF,S
→ Enter を押す
［画面・出力］
IEE975I SMF DATA SET STATUS SYS1.MAN1 ACTIVE SYS1.MAN2 ALTERNATE
画面・出力にあるIEE975Iを読み、ACTIVE DATASETとRECORDINGと対象SMF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD PARMLIB(SMFPRM05)を指定し、SMF05のparmlib確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PARMLIB(SMFPRM05)
→ Enter を押す
［画面・出力］
IEE252I MEMBER SMFPRM05 FOUND IN SYS1.PARMLIB
画面・出力にあるSMFPRMを読み、ACTIVE DATASETとRECORDINGと対象SMF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMFを指定し、SMF05のSMF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF
→ Enter を押す
［画面・出力］
IEE974I 12.15.30 SMF DATA
STATUS ACTIVE
DATA SET NAME SYS1.MAN1 RECORDING
画面・出力にあるIEE974Iを読み、ACTIVE DATASETとRECORDINGと対象SMF05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE975I が画面・出力に表示されること
② ステップ2 の SMFPRM が画面・出力に表示されること
③ ステップ3 の IEE974I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0176"><h3>SMF記録 SMF稼働状態 構成監査 SMF08</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>構成監査では SMF記録 の データセット表示 を主操作として SMF08 を判定します。定義値と稼働値の一致への注意として「記録停止やデータセット切替待ちを見落とすと監査期間が欠けます」を SMF08 に残します。構成監査を補助する parmlib確認 では SMFPRM を補助値として SMF08 へ保存します。主判定の構成監査では記録・稼働状態の データセット表示 から IEE975I を読み SMF08 へ残します。証跡照合の構成監査では記録・稼働状態の IEE975I と SMFPRM を SMF08 に保存します。記録対応の構成監査では記録・稼働状態の ACTIVE DATASETとRECORDING の証跡へ SMF08 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で SMF記録 の データセット表示 と parmlib確認 を照合し 定義値と稼働値の一致 を確かめます。SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能です。記録停止やデータセット切替待ちを見落とすと監査期間が欠けます。IEE975I を読む前に対象 SMF08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのSMF08の出力を再利用する。今回のD SMF,SとD PARMLIB(SMFPRM08)は実行済みとして扱う。</li><li>B. D PARMLIB(SMFPRM08)のSMFPRMをACTIVE DATASETとRECORDINGの主判定に採用する。D SMF,Sの応答は採取対象から外す。</li><li>C. D SMFのIEE974IをIEE975Iと同義の成功表示として扱う。D SMF,Sは実行しない。</li><li>D. D PARMLIB(SMFPRM08)の結果だけでは確定しない。D SMF,SのIEE975Iを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Dはデータセット表示で IEE975I を読みACTIVE DATASETとRECORDINGの主値として構成差分を監査しSMF08に残します。
実行時の背景: 構成監査ではparmlib確認を補助操作としSMF稼働状態の定義値と稼働値の一致をSMFPRMと対象SMF08で照合します。
四つの候補の理由: データセット表示とparmlib確認の役割を分けるとA: 過去出力では今回の構成監査を示せない点でSMF記録に使いません、B: SMFPRMはIEE975Iを代替しない点でSMF稼働状態に使えません、C: IEE974IとIEE975Iは確認項目が異なる点でSMF08を採用できません、D: IEE975Iを主証跡として区別する点で主証跡になります。結論として構成監査の記録・稼働状態で判定する対象は SMF08 です。
初出語定義: 構成監査で使う SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能を表しACTIVE DATASETとRECORDINGを判定する際にSMF08へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF記録 SMF稼働状態 構成監査 SMF08</strong></p><p>検証目的: SMF記録のSMF稼働状態について構成差分を監査し、SMF08のACTIVE DATASETとRECORDINGを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SMF08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMF,Sを指定し、SMF08のデータセット表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF,S
→ Enter を押す
［画面・出力］
IEE975I SMF DATA SET STATUS SYS1.MAN1 ACTIVE SYS1.MAN2 ALTERNATE
画面・出力にあるIEE975Iを読み、ACTIVE DATASETとRECORDINGと対象SMF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD PARMLIB(SMFPRM08)を指定し、SMF08のparmlib確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PARMLIB(SMFPRM08)
→ Enter を押す
［画面・出力］
IEE252I MEMBER SMFPRM08 FOUND IN SYS1.PARMLIB
画面・出力にあるSMFPRMを読み、ACTIVE DATASETとRECORDINGと対象SMF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMFを指定し、SMF08のSMF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF
→ Enter を押す
［画面・出力］
IEE974I 12.15.30 SMF DATA
STATUS ACTIVE
DATA SET NAME SYS1.MAN1 RECORDING
画面・出力にあるIEE974Iを読み、ACTIVE DATASETとRECORDINGと対象SMF08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE975I が画面・出力に表示されること
② ステップ2 の SMFPRM が画面・出力に表示されること
③ ステップ3 の IEE974I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0177"><h3>SMF記録 SMF稼働状態 通常状態の確認 SMF01</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>通常状態の確認では SMF記録 の SMF表示 を主操作として SMF01 を判定します。基準値と現在値の差への注意として「記録停止やデータセット切替待ちを見落とすと監査期間が欠けます」を SMF01 に残します。通常状態の確認を補助する データセット表示 では IEE975I を補助値として SMF01 へ保存します。主判定の通常状態の確認では記録・稼働状態の SMF表示 から IEE974I を読み SMF01 へ残します。証跡照合の通常状態の確認では記録・稼働状態の IEE974I と IEE975I を SMF01 に保存します。記録対応の通常状態の確認では記録・稼働状態の ACTIVE DATASETとRECORDING の証跡へ SMF01 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で SMF記録 の SMF表示 と データセット表示 を用い 通常状態を確定 します。SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能です。記録停止やデータセット切替待ちを見落とすと監査期間が欠けます。IEE974I で対象 SMF01 の ACTIVE DATASETとRECORDING を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. D SMFを先に実行する。対象SMF01のIEE974IをACTIVE DATASETとRECORDINGとして記録する。続いてD SMF,Sで同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. D SMF,SのIEE975IをACTIVE DATASETとRECORDINGの主判定に採用する。D SMFの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. D PARMLIB(SMFPRM01)のSMFPRMをIEE974Iと同義の成功表示として扱う。D SMFは実行しない。</li><li>D. D SMFが応答を返した時点で正常とする。応答中のIEE974Iの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: AはSMF表示で IEE974I を読みACTIVE DATASETとRECORDINGの主値として通常状態を確定しSMF01に残します。
背景・仕組み: 通常状態の確認ではデータセット表示を補助操作としSMF稼働状態の基準値と現在値の差をIEE975Iと対象SMF01で照合します。
選択肢の理由: SMF表示とデータセット表示の役割を分けるとA: IEE974Iを主値として補助結果と照合する点で正答です、B: IEE975IはIEE974Iを代替しないうえに追加前提も不正な点でSMF01を採用できません、C: SMFPRMとIEE974Iは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではACTIVE DATASETとRECORDINGを判定できない点で一次資料と一致しません。結論として通常状態の確認の記録・稼働状態で判定する対象は SMF01 です。
用語の初出定義: 通常状態の確認で使う SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能を表しACTIVE DATASETとRECORDINGを判定する際にSMF01へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF記録 SMF稼働状態 通常状態の確認 SMF01</strong></p><p>検証目的: SMF記録のSMF稼働状態について通常状態を確定し、SMF01のACTIVE DATASETとRECORDINGを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SMF01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMFを指定し、SMF01のSMF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF
→ Enter を押す
［画面・出力］
IEE974I 12.15.30 SMF DATA
STATUS ACTIVE
DATA SET NAME SYS1.MAN1 RECORDING
画面・出力にあるIEE974Iを読み、ACTIVE DATASETとRECORDINGと対象SMF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMF,Sを指定し、SMF01のデータセット表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF,S
→ Enter を押す
［画面・出力］
IEE975I SMF DATA SET STATUS SYS1.MAN1 ACTIVE SYS1.MAN2 ALTERNATE
画面・出力にあるIEE975Iを読み、ACTIVE DATASETとRECORDINGと対象SMF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD PARMLIB(SMFPRM01)を指定し、SMF01のparmlib確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PARMLIB(SMFPRM01)
→ Enter を押す
［画面・出力］
IEE252I MEMBER SMFPRM01 FOUND IN SYS1.PARMLIB
画面・出力にあるSMFPRMを読み、ACTIVE DATASETとRECORDINGと対象SMF01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE974I が画面・出力に表示されること
② ステップ2 の IEE975I が画面・出力に表示されること
③ ステップ3 の SMFPRM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0178"><h3>SMF記録 SMF稼働状態 障害切り分け SMF04</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>障害切り分けでは SMF記録 の SMF表示 を主操作として SMF04 を判定します。最初に失敗した処理への注意として「記録停止やデータセット切替待ちを見落とすと監査期間が欠けます」を SMF04 に残します。障害切り分けを補助する データセット表示 では IEE975I を補助値として SMF04 へ保存します。主判定の障害切り分けでは記録・稼働状態の SMF表示 から IEE974I を読み SMF04 へ残します。証跡照合の障害切り分けでは記録・稼働状態の IEE974I と IEE975I を SMF04 に保存します。記録対応の障害切り分けでは記録・稼働状態の ACTIVE DATASETとRECORDING の証跡へ SMF04 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで SMF記録 の SMF表示 と データセット表示 の役割を分け 最初に失敗した処理 を調べます。SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能です。記録停止やデータセット切替待ちを見落とすと監査期間が欠けます。対象 SMF04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. D PARMLIB(SMFPRM04)のSMFPRMをIEE974Iと同義の成功表示として扱う。D SMFは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. D SMFが応答を返した時点で正常とする。応答中のIEE974Iの値は記録しない。</li><li>C. D SMFのコマンド文字列だけを記録する。IEE974Iを含む応答行は保存しない。</li><li>D. D SMFの出力でSMF04とIEE974Iが同じ応答にあることを確認する。ACTIVE DATASETとRECORDINGをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: DはSMF表示で IEE974I を読みACTIVE DATASETとRECORDINGの主値として障害範囲を限定しSMF04に残します。
技術的背景: 障害切り分けではデータセット表示を補助操作としSMF稼働状態の最初に失敗した処理をIEE975Iと対象SMF04で照合します。
四択の評価: SMF表示とデータセット表示の役割を分けるとA: SMFPRMとIEE974Iは確認項目が異なるうえに追加前提も不正な点でSMF04を採用できません、B: 応答の有無だけではACTIVE DATASETとRECORDINGを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではACTIVE DATASETとRECORDINGを証明できない点で一次資料と一致しません、D: SMF04とIEE974Iを同じ応答で結ぶ点でSMF04を判定できます。結論として障害切り分けの記録・稼働状態で判定する対象は SMF04 です。
初出語の意味: 障害切り分けで使う SMF稼働状態 はシステムと製品の活動記録をレコードタイプ別に収集し、ログストリームまたはデータセットへ書き出す機能を表しACTIVE DATASETとRECORDINGを判定する際にSMF04へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF記録 SMF稼働状態 障害切り分け SMF04</strong></p><p>検証目的: SMF記録のSMF稼働状態について障害範囲を限定し、SMF04のACTIVE DATASETとRECORDINGを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SMF04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMFを指定し、SMF04のSMF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF
→ Enter を押す
［画面・出力］
IEE974I 12.15.30 SMF DATA
STATUS ACTIVE
DATA SET NAME SYS1.MAN1 RECORDING
画面・出力にあるIEE974Iを読み、ACTIVE DATASETとRECORDINGと対象SMF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD SMF,Sを指定し、SMF04のデータセット表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SMF,S
→ Enter を押す
［画面・出力］
IEE975I SMF DATA SET STATUS SYS1.MAN1 ACTIVE SYS1.MAN2 ALTERNATE
画面・出力にあるIEE975Iを読み、ACTIVE DATASETとRECORDINGと対象SMF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSMF記録を確認する入力画面です。COMMAND入力口へD PARMLIB(SMFPRM04)を指定し、SMF04のparmlib確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PARMLIB(SMFPRM04)
→ Enter を押す
［画面・出力］
IEE252I MEMBER SMFPRM04 FOUND IN SYS1.PARMLIB
画面・出力にあるSMFPRMを読み、ACTIVE DATASETとRECORDINGと対象SMF04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE974I が画面・出力に表示されること
② ステップ2 の IEE975I が画面・出力に表示されること
③ ステップ3 の SMFPRM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0179"><h3>WTOマクロ 定義照合 運用確認021</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>第二十一観点 SMF記録 で WTOマクロ は 定義照合 の対象です（第二十一観点）。第二十一観点 確認時には プログラムからオペレーターとハードコピー・ログへメッセージを送るマクという性質を前提にします（第二十一観点）。第二十一観点 SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同じ証跡に置き、資源競合時の保有者確認を管理します（第二十一観点）。第二十一観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録021から再現します（第二十一観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第二十一証跡です。SMF記録 の運用で WTOマクロ を点検します。確認観点は WTOマクロ、定義照合、運用確認 です。SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を合わせて読む時の採用方針として正しいものはどれか。</p><ul class="kb-choices"><li>A. ENQ資源管理 の一般メモを採り、SYS1.LINKLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記021として調査範囲を狭める。</li><li>B. SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同一票へ記録し、WTOマクロ を zOSSP正021で確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. WTOマクロ の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延021として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在021として残す。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第二十一観点 正解確認: Bは WTOマクロ と SYS1.LINKLIB を同じ証跡で扱うため、後続の照合に使えます（第二十一観点）。第二十一観点 実行背景: SVC、TCB、SRB、PSWは割り込みとディスパッチの説明に使います（第二十一観点）。第二十一観点 誤答比較: Aは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第二十一観点）。第二十一観点 用語整理: SMFはシステム測定記録です（第二十一観点）。第二十一観点 IFASMFDPはSMFデータ退避に使います（第二十一観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOマクロ 定義照合 運用確認021</strong></p><p>検証目的: WTOマクロ の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / operations</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により WTOマクロ の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY R,ALL
→ Enter を押す
［画面・出力］
IEE112I 11.15.21 DISPLAY R 720
REPLY ID   MESSAGE TEXT
005        IEA793A SPECIFY DUMP OPTION FOR SYS1.LINKLIB
画面・出力には IEE112I が含まれる。IEE112I を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により WTOマクロ の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D C
→ Enter を押す
［画面・出力］
IEE889I 15.33.21 CONSOLE DISPLAY 510
MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
画面・出力には IEE889I が含まれる。IEE889I を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により WTOマクロ の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; R 005,INFO
→ Enter を押す
［画面・出力］
IEE600I REPLY TO 005 IS;INFO
IEA631I OPERATOR OPER21 NOW ACTIVE, SYSTEM=SC65
画面・出力には IEE600I が含まれる。IEE600I を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0180"><h3>システムキー ストレージ確認 運用確認038</h3><p class="kb-meta">分類: SMF記録 ・ 難易度: 中級</p><p>第三十八観点 システムキー は z/OS System Programming の SMF記録 で扱う管理項目です（第三十八観点）。第三十八観点 キー0から7の保護キーで実行され、保護されたデータへ到達できる権限という説明を操作結果と照合します（第三十八観点）。第三十八観点 SYS1.PARMLIB(PROGSP)、parmlibメンバーの該当ステートメント、定義メンバーを照合し、parmlib反映範囲の追跡を確認します（第三十八観点）。第三十八観点 証跡には資料IDと確認値を併記し、zOSSP記録038として保存します（第三十八観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第三十八証跡です。システムキー の記録を監査用に整えます。確認観点は システムキー、ストレージ確認、運用確認 です。メッセージID、定義メンバー、表示出力を同じ確認票に置く対応として適切なものはどれか。</p><ul class="kb-choices"><li>A. SMF記録 の一般メモを採り、SYS1.PARMLIB(PROGSP)、メッセージID、時刻の対応を記録外に置き、zOSSP誤記038として調査範囲を狭める。</li><li>B. システムキー の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延038として扱う。</li><li>C. parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を同一票へ記録し、システムキー を zOSSP正038で確定する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在038として残す。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第三十八観点 正答根拠: Cは parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を結び付けるため、対象システムの取り違えを防げます（第三十八観点）。第三十八観点 操作背景: WTOとWTORはオペレーター通知と応答をコンソールログへ残します（第三十八観点）。第三十八観点 誤答点検: Aはシステム名欠落、Bは定義未確認、Dは時刻差の欠落が理由です（第三十八観点）。第三十八観点 用語補足: ENQは資源を直列化します（第三十八観点）。第三十八観点 DEQは取得した資源を解放します（第三十八観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システムキー ストレージ確認 運用確認038</strong></p><p>検証目的: システムキー の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: IPCS / dump analysis</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により システムキー の値を確認し、対象の現在値を固定する。
［操作（入力）］
IPCS option 6
COMMAND ===&gt; VERBX LOGDATA
→ Enter を押す
［画面・出力］
LOGDATA VERBEXIT PROCESSING
LOGREC BUFFER RECORDS LOCATED
EREP DETAIL EDIT REPORT FOLLOWS
画面・出力には LOGDATA が含まれる。LOGDATA を読み取り、parmlib反映範囲の追跡のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により システムキー の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.30.14 TRACE DISPLAY 207
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON MT=(ON,024K)
画面・出力には IEE843I が含まれる。IEE843I を読み取り、parmlib反映範囲の追跡のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により システムキー の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
IPCS command line
COMMAND ===&gt; STATUS CPU
→ Enter を押す
［画面・出力］
IPCS STATUS CPU
PSW=070C1000 81234567  ASID=0010
CURRENT TCB ADDRESS SYS1.PARMLIB(PROGSP)
画面・出力には ASID=0010 が含まれる。ASID=0010 を読み取り、parmlib反映範囲の追跡のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LOGDATA が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE843I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ASID=0010 が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


## SVC処理


<section class="kb-item" id="c38-i0181"><h3>D TRACE 表示確認 運用確認043</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>第四十三観点 SVC処理 の運用では D TRACE を表示、定義、証跡で確認します（第四十三観点）。第四十三観点 役割は システムまたはコンポーネントのトレース状態を表示する診断コマンドという範囲です（第四十三観点）。第四十三観点 DISPLAY R,ALL の未応答要求表示 の値を MYPROG.LOADLIB と合わせ、共通ストレージ変更の記録を記録します（第四十三観点）。第四十三観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録043に残します（第四十三観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第四十三証跡です。zOSSP記録043として MYPROG.LOADLIB の証跡を残します。確認観点は D TRACE、表示確認、運用確認 です。MYPROG.LOADLIB を根拠として残す時、対象の取り違えを抑える対応はどれか。</p><ul class="kb-choices"><li>A. WTOR応答管理 の一般メモを採り、MYPROG.LOADLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記043として調査範囲を狭める。</li><li>B. D TRACE の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延043として扱う。</li><li>C. DISPLAY R,ALL の未応答要求表示 と MYPROG.LOADLIB を同一票へ記録し、D TRACE を zOSSP正043で確定する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在043として残す。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第四十三観点 採用理由: Cは D TRACE の状態を表示値と定義の両方から確認するため、記録として妥当です（第四十三観点）。第四十三観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第四十三観点）。第四十三観点 誤答整理: Aは一般メモ偏重、Bはジョブログ除外、Dは再現性不足が理由です（第四十三観点）。第四十三観点 用語確認: APFは許可ライブラリーの管理機能です（第四十三観点）。第四十三観点 PROGxxは動的なプログラム管理指定です（第四十三観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D TRACE 表示確認 運用確認043</strong></p><p>検証目的: D TRACE の 表示確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / GRS</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により D TRACE の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS
→ Enter を押す
［画面・出力］
ISG343I 10.27.19 GRS STATUS 862
SYSTEM    STATE               SYSTEM    STATE
SC65      CONNECTED           SC63      CONNECTED
GRS STAR MODE INFORMATION
画面・出力には ISG343I が含まれる。ISG343I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により D TRACE の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS,RNL=INCL
→ Enter を押す
［画面・出力］
ISG343I 10.28.19 GRS STATUS 872
RNL=INCL
QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により D TRACE の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D XCF,STR,STRNAME=ISGLOCK
→ Enter を押す
［画面・出力］
IXC360I 10.29.19 DISPLAY XCF 882
STRUCTURE NAME: ISGLOCK
STATUS: ALLOCATED IN CFRM POLICY
画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0182"><h3>IEFU29出口 状態確認 運用確認010</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 初級</p><p>第十観点 IEFU29出口 は z/OS System Programming の SVC処理 で扱う管理項目です（第十観点）。第十観点 SMF記録データセットが満杯になった時にダンプ処理へつなぐ出口という説明を操作結果と照合します（第十観点）。第十観点 SYSPRINT、SETPROG APF後のCSV410I表示、定義メンバーを照合し、診断ログの再現性確保を確認します（第十観点）。第十観点 証跡には資料IDと確認値を併記し、zOSSP記録010として保存します（第十観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IEFU29出口 状態確認 運用確認010</strong></p><p>検証目的: IEFU29出口 の 状態確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / parmlib review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IEFU29出口 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(PROGSP)
→ Enter を押す
［画面・出力］
APF FORMAT(DYNAMIC)
APF ADD DSNAME(MYPROG.LOADLIB) VOLUME(MPRES3)
LPA ADD MODNAME(MOD10) DSNAME(SYS1.LPALIB)
画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IEFU29出口 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SET PROG=SP
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE252I が含まれる。IEE252I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IEFU29出口 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 06.10.10 PROG,APF DISPLAY 809
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
  12  MPRES3 MYPROG.LOADLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0183"><h3>SVC処理 SVCテーブル ログとの照合 SVC07</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>ログとの照合では SVC処理 の SVC表示 を主操作として SVC07 を判定します。時刻と対象識別子への注意として「誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります」を SVC07 に残します。ログとの照合を補助する モジュール所在 では CSV411I を補助値として SVC07 へ保存します。主判定のログとの照合では処理・テーブルの SVC表示 から ROUTINE を読み SVC07 へ残します。証跡照合のログとの照合では処理・テーブルの ROUTINE と CSV411I を SVC07 に保存します。記録対応のログとの照合では処理・テーブルの SVC番号とROUTINE の証跡へ SVC07 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で SVC処理 の SVC表示 と モジュール所在 を用い 操作とログを対応 します。SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みです。誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります。ROUTINE で対象 SVC07 の SVC番号とROUTINE を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. D PROG,SVCが応答を返した時点で正常とする。応答中のROUTINEの値は記録しない。CSV450IをROUTINEと同じ判定値とみなし対象SVC07の主証跡にする。</li><li>B. D PROG,SVCのコマンド文字列だけを記録する。ROUTINEを含む応答行は保存しない。</li><li>C. ROUTINEを含むSVC表示の応答行を保存する。その応答を得るためD PROG,SVCを使用する。対象SVC07のSVC番号とROUTINEとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. SVCテーブルの停止または再定義を実施する。その後にD PROG,SVCでROUTINEを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: CはSVC表示で ROUTINE を読みSVC番号とROUTINEの主値として操作とログを対応しSVC07に残します。
機能の仕組み: ログとの照合ではモジュール所在を補助操作としSVCテーブルの時刻と対象識別子をCSV411Iと対象SVC07で照合します。
各候補の評価: SVC表示とモジュール所在の役割を分けるとA: 応答の有無だけではSVC番号とROUTINEを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではSVC番号とROUTINEを証明できない点で一次資料と一致しません、C: ROUTINEの実値を対象別に残す点でSVC07を判定できます、D: 変更前のSVC番号とROUTINEを失う点でモジュール所在の範囲を越えます。結論としてログとの照合の処理・テーブルで判定する対象は SVC07 です。
用語の定義: ログとの照合で使う SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みを表しSVC番号とROUTINEを判定する際にSVC07へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC処理 SVCテーブル ログとの照合 SVC07</strong></p><p>検証目的: SVC処理のSVCテーブルについて操作とログを対応し、SVC07のSVC番号とROUTINEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SVC07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,SVCを指定し、SVC07のSVC表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,SVC
→ Enter を押す
［画面・出力］
CSV420I SVC TABLE ENTRY SVC=07 ROUTINE=IGC0007 TYPE=3 STATUS ACTIVE
画面・出力にあるROUTINEを読み、SVC番号とROUTINEと対象SVC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=IGC0007を指定し、SVC07のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=IGC0007
→ Enter を押す
［画面・出力］
CSV411I MODULE IGC0007 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、SVC番号とROUTINEと対象SVC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,APF,DSNAME=SYS1.LINKLIBを指定し、SVC07のAPF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,APF,DSNAME=SYS1.LINKLIB
→ Enter を押す
［画面・出力］
CSV450I APF DISPLAY FOR SYS1.LINKLIB VOLUME SMS STATUS AUTHORIZED
画面・出力にあるCSV450Iを読み、SVC番号とROUTINEと対象SVC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ROUTINE が画面・出力に表示されること
② ステップ2 の CSV411I が画面・出力に表示されること
③ ステップ3 の CSV450I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0184"><h3>SVC処理 SVCテーブル 代替経路の確認 SVC10</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>代替経路の確認では SVC処理 の SVC表示 を主操作として SVC10 を判定します。主経路との役割差への注意として「誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります」を SVC10 に残します。代替経路の確認を補助する モジュール所在 では CSV411I を補助値として SVC10 へ保存します。主判定の代替経路の確認では処理・テーブルの SVC表示 から ROUTINE を読み SVC10 へ残します。証跡照合の代替経路の確認では処理・テーブルの ROUTINE と CSV411I を SVC10 に保存します。記録対応の代替経路の確認では処理・テーブルの SVC番号とROUTINE の証跡へ SVC10 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で SVC処理 の SVC表示 と モジュール所在 の役割を分け 主経路との役割差 を調べます。SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みです。誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります。対象 SVC10 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. D PROG,SVCのコマンド文字列だけを記録する。ROUTINEを含む応答行は保存しない。</li><li>B. D PROG,SVCとD PROG,LPA,MODNAME=IGC0010の対象名をそろえる。前者のROUTINEをSVC番号とROUTINEの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. SVCテーブルの停止または再定義を実施する。その後にD PROG,SVCでROUTINEを採取する。</li><li>D. SVC処理のSVC番号とROUTINEを確認する。その値をSVC処理のSVC10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: BはSVC表示で ROUTINE を読みSVC番号とROUTINEの主値として代替手段の成立を確認しSVC10に残します。
運用上の背景: 代替経路の確認ではモジュール所在を補助操作としSVCテーブルの主経路との役割差をCSV411Iと対象SVC10で照合します。
候補別の検討: SVC表示とモジュール所在の役割を分けるとA: 入力記録だけではSVC番号とROUTINEを証明できない点で一次資料と一致しません、B: 同じ対象名のROUTINEを採用する点でSVC10を判定できます、C: 変更前のSVC番号とROUTINEを失う点でモジュール所在の範囲を越えます、D: SVC処理の値ではROUTINEを確認できない点でSVC10の値を示しません。結論として代替経路の確認の処理・テーブルで判定する対象は SVC10 です。
重要用語の定義: 代替経路の確認で使う SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みを表しSVC番号とROUTINEを判定する際にSVC10へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC処理 SVCテーブル 代替経路の確認 SVC10</strong></p><p>検証目的: SVC処理のSVCテーブルについて代替手段の成立を確認し、SVC10のSVC番号とROUTINEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SVC10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,SVCを指定し、SVC10のSVC表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,SVC
→ Enter を押す
［画面・出力］
CSV420I SVC TABLE ENTRY SVC=10 ROUTINE=IGC0010 TYPE=3 STATUS ACTIVE
画面・出力にあるROUTINEを読み、SVC番号とROUTINEと対象SVC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=IGC0010を指定し、SVC10のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=IGC0010
→ Enter を押す
［画面・出力］
CSV411I MODULE IGC0010 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、SVC番号とROUTINEと対象SVC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,APF,DSNAME=SYS1.LINKLIBを指定し、SVC10のAPF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,APF,DSNAME=SYS1.LINKLIB
→ Enter を押す
［画面・出力］
CSV450I APF DISPLAY FOR SYS1.LINKLIB VOLUME SMS STATUS AUTHORIZED
画面・出力にあるCSV450Iを読み、SVC番号とROUTINEと対象SVC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ROUTINE が画面・出力に表示されること
② ステップ2 の CSV411I が画面・出力に表示されること
③ ステップ3 の CSV450I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0185"><h3>SVC処理 SVCテーブル 変更前の確認 SVC02</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>変更前の確認では SVC処理 の モジュール所在 を主操作として SVC02 を判定します。変更対象と非対象の境界への注意として「誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります」を SVC02 に残します。変更前の確認を補助する APF確認 では CSV450I を補助値として SVC02 へ保存します。主判定の変更前の確認では処理・テーブルの モジュール所在 から CSV411I を読み SVC02 へ残します。証跡照合の変更前の確認では処理・テーブルの CSV411I と CSV450I を SVC02 に保存します。記録対応の変更前の確認では処理・テーブルの SVC番号とROUTINE の証跡へ SVC02 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で SVC処理 の モジュール所在 と APF確認 を照合し 変更対象と非対象の境界 を確かめます。SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みです。誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります。CSV411I を読む前に対象 SVC02 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. D PROG,LPA,MODNAME=IGC0002を対象名なしで実行する。一覧の先頭行をSVC02の結果として記録する。</li><li>B. 対象SVC02についてD PROG,LPA,MODNAME=IGC0002の応答からCSV411Iを確認する。D PROG,APF,DSNAME=SYS1.LINKLIBは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存したD PROG,LPA,MODNAME=IGC0002の結果を使う。今回のD PROG,APF,DSNAME=SYS1.LINKLIBの結果と同一時点の証跡として比較する。</li><li>D. 保存済みのSVC02の出力を再利用する。今回のD PROG,LPA,MODNAME=IGC0002とD PROG,APF,DSNAME=SYS1.LINKLIBは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Bはモジュール所在で CSV411I を読みSVC番号とROUTINEの主値として変更前の証跡を保存しSVC02に残します。
動作の背景: 変更前の確認ではAPF確認を補助操作としSVCテーブルの変更対象と非対象の境界をCSV450Iと対象SVC02で照合します。
各選択肢の検討: モジュール所在とAPF確認の役割を分けるとA: 先頭行はSVC02と確定できない点で変更前の確認に合いません、B: CSV411Iと補助証跡の時刻を合わせる点でモジュール所在に合います、C: 採取時刻が異なる点でSVC処理に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でSVCテーブルに使えません。結論として変更前の確認の処理・テーブルで判定する対象は SVC02 です。
初出用語の定義: 変更前の確認で使う SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みを表しSVC番号とROUTINEを判定する際にSVC02へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC処理 SVCテーブル 変更前の確認 SVC02</strong></p><p>検証目的: SVC処理のSVCテーブルについて変更前の証跡を保存し、SVC02のSVC番号とROUTINEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SVC02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=IGC0002を指定し、SVC02のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=IGC0002
→ Enter を押す
［画面・出力］
CSV411I MODULE IGC0002 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、SVC番号とROUTINEと対象SVC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,APF,DSNAME=SYS1.LINKLIBを指定し、SVC02のAPF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,APF,DSNAME=SYS1.LINKLIB
→ Enter を押す
［画面・出力］
CSV450I APF DISPLAY FOR SYS1.LINKLIB VOLUME SMS STATUS AUTHORIZED
画面・出力にあるCSV450Iを読み、SVC番号とROUTINEと対象SVC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,SVCを指定し、SVC02のSVC表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,SVC
→ Enter を押す
［画面・出力］
CSV420I SVC TABLE ENTRY SVC=02 ROUTINE=IGC0002 TYPE=3 STATUS ACTIVE
画面・出力にあるROUTINEを読み、SVC番号とROUTINEと対象SVC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV411I が画面・出力に表示されること
② ステップ2 の CSV450I が画面・出力に表示されること
③ ステップ3 の ROUTINE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0186"><h3>SVC処理 SVCテーブル 変更後の確認 SVC03</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>変更後の確認では SVC処理 の APF確認 を主操作として SVC03 を判定します。反映値と残存値への注意として「誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります」を SVC03 に残します。変更後の確認を補助する SVC表示 では ROUTINE を補助値として SVC03 へ保存します。主判定の変更後の確認では処理・テーブルの APF確認 から CSV450I を読み SVC03 へ残します。証跡照合の変更後の確認では処理・テーブルの CSV450I と ROUTINE を SVC03 に保存します。記録対応の変更後の確認では処理・テーブルの SVC番号とROUTINE の証跡へ SVC03 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で SVC処理 の APF確認 と SVC表示 を組み合わせる際は SVCテーブル が監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みという仕組みを前提にします。誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります。CSV450I と SVC番号とROUTINE を対象 SVC03 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. SVCテーブルの停止または再定義を実施する。その後にD PROG,APF,DSNAME=SYS1.LINKLIBでCSV450Iを採取する。</li><li>B. LNKLST管理のSET名とDATASET順序を確認する。その値をSVC処理のSVC03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。SVCテーブルの反映値と残存値は確認済みとして扱う。さらにD PROG,LPA,MODNAME=IGC0003のCSV411IをCSV450Iと同種の値として併記する。</li><li>C. D PROG,SVCで周辺状態を押さえる。その後にD PROG,APF,DSNAME=SYS1.LINKLIBでCSV450Iを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. D PROG,SVCが成功したためD PROG,APF,DSNAME=SYS1.LINKLIBのCSV450Iも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: CはAPF確認で CSV450I を読みSVC番号とROUTINEの主値として変更結果を検証しSVC03に残します。
内部の仕組み: 変更後の確認ではSVC表示を補助操作としSVCテーブルの反映値と残存値をROUTINEと対象SVC03で照合します。
誤答を含む比較: APF確認とSVC表示の役割を分けるとA: 変更前のSVC番号とROUTINEを失う点でSVC番号とROUTINEを確認できません、B: LNKLST管理の値ではCSV450Iを確認できないうえに追加前提も不正な点でSVC表示の範囲を越えます、C: 周辺状態の後にCSV450Iを確認する点で現在値を示します、D: 補助操作の成功ではCSV450Iを確定できない点で変更後の確認に合いません。結論として変更後の確認の処理・テーブルで判定する対象は SVC03 です。
用語定義: 変更後の確認で使う SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みを表しSVC番号とROUTINEを判定する際にSVC03へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC処理 SVCテーブル 変更後の確認 SVC03</strong></p><p>検証目的: SVC処理のSVCテーブルについて変更結果を検証し、SVC03のSVC番号とROUTINEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SVC03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,APF,DSNAME=SYS1.LINKLIBを指定し、SVC03のAPF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,APF,DSNAME=SYS1.LINKLIB
→ Enter を押す
［画面・出力］
CSV450I APF DISPLAY FOR SYS1.LINKLIB VOLUME SMS STATUS AUTHORIZED
画面・出力にあるCSV450Iを読み、SVC番号とROUTINEと対象SVC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,SVCを指定し、SVC03のSVC表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,SVC
→ Enter を押す
［画面・出力］
CSV420I SVC TABLE ENTRY SVC=03 ROUTINE=IGC0003 TYPE=3 STATUS ACTIVE
画面・出力にあるROUTINEを読み、SVC番号とROUTINEと対象SVC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=IGC0003を指定し、SVC03のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=IGC0003
→ Enter を押す
［画面・出力］
CSV411I MODULE IGC0003 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、SVC番号とROUTINEと対象SVC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV450I が画面・出力に表示されること
② ステップ2 の ROUTINE が画面・出力に表示されること
③ ステップ3 の CSV411I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0187"><h3>SVC処理 SVCテーブル 引継ぎ記録 SVC09</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>引継ぎ記録では SVC処理 の APF確認 を主操作として SVC09 を判定します。次担当者が追跡できる証跡への注意として「誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります」を SVC09 に残します。引継ぎ記録を補助する SVC表示 では ROUTINE を補助値として SVC09 へ保存します。主判定の引継ぎ記録では処理・テーブルの APF確認 から CSV450I を読み SVC09 へ残します。証跡照合の引継ぎ記録では処理・テーブルの CSV450I と ROUTINE を SVC09 に保存します。記録対応の引継ぎ記録では処理・テーブルの SVC番号とROUTINE の証跡へ SVC09 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で SVC処理 の APF確認 と SVC表示 を組み合わせる際は SVCテーブル が監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みという仕組みを前提にします。誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります。CSV450I と SVC番号とROUTINE を対象 SVC09 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 対象名SVC09を指定してD PROG,APF,DSNAME=SYS1.LINKLIBを実行する。応答中のCSV450Iと時刻を保存する。D PROG,SVCで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. D PROG,SVCが成功したためD PROG,APF,DSNAME=SYS1.LINKLIBのCSV450Iも正常だと推定する。主出力は保存しない。</li><li>C. D PROG,APF,DSNAME=SYS1.LINKLIBを対象名なしで実行する。一覧の先頭行をSVC09の結果として記録する。</li><li>D. 前回保存したD PROG,APF,DSNAME=SYS1.LINKLIBの結果を使う。今回のD PROG,SVCの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: AはAPF確認で CSV450I を読みSVC番号とROUTINEの主値として再現可能な記録を作成しSVC09に残します。
製品内の仕組み: 引継ぎ記録ではSVC表示を補助操作としSVCテーブルの次担当者が追跡できる証跡をROUTINEと対象SVC09で照合します。
選択肢別の説明: APF確認とSVC表示の役割を分けるとA: CSV450Iと時刻を保存する点で現在値を示します、B: 補助操作の成功ではCSV450Iを確定できない点で引継ぎ記録に合いません、C: 先頭行はSVC09と確定できない点でAPF確認を代替しません、D: 採取時刻が異なる点でSVC処理に使いません。結論として引継ぎ記録の処理・テーブルで判定する対象は SVC09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みを表しSVC番号とROUTINEを判定する際にSVC09へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC処理 SVCテーブル 引継ぎ記録 SVC09</strong></p><p>検証目的: SVC処理のSVCテーブルについて再現可能な記録を作成し、SVC09のSVC番号とROUTINEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SVC09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,APF,DSNAME=SYS1.LINKLIBを指定し、SVC09のAPF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,APF,DSNAME=SYS1.LINKLIB
→ Enter を押す
［画面・出力］
CSV450I APF DISPLAY FOR SYS1.LINKLIB VOLUME SMS STATUS AUTHORIZED
画面・出力にあるCSV450Iを読み、SVC番号とROUTINEと対象SVC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,SVCを指定し、SVC09のSVC表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,SVC
→ Enter を押す
［画面・出力］
CSV420I SVC TABLE ENTRY SVC=09 ROUTINE=IGC0009 TYPE=3 STATUS ACTIVE
画面・出力にあるROUTINEを読み、SVC番号とROUTINEと対象SVC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=IGC0009を指定し、SVC09のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=IGC0009
→ Enter を押す
［画面・出力］
CSV411I MODULE IGC0009 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、SVC番号とROUTINEと対象SVC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV450I が画面・出力に表示されること
② ステップ2 の ROUTINE が画面・出力に表示されること
③ ステップ3 の CSV411I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0188"><h3>SVC処理 SVCテーブル 復旧後の確認 SVC06</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>復旧後の確認では SVC処理 の APF確認 を主操作として SVC06 を判定します。再発していないことを示す値への注意として「誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります」を SVC06 に残します。復旧後の確認を補助する SVC表示 では ROUTINE を補助値として SVC06 へ保存します。主判定の復旧後の確認では処理・テーブルの APF確認 から CSV450I を読み SVC06 へ残します。証跡照合の復旧後の確認では処理・テーブルの CSV450I と ROUTINE を SVC06 に保存します。記録対応の復旧後の確認では処理・テーブルの SVC番号とROUTINE の証跡へ SVC06 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で SVC処理 の APF確認 と SVC表示 を実施し SVCテーブル の役割を確認します。誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります。対象 SVC06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. GRS資源直列化のSYSTEMとMODEを確認する。その値をSVC処理のSVC06にも適用する。</li><li>B. D PROG,APF,DSNAME=SYS1.LINKLIBでCSV450Iを取得してからD PROG,LPA,MODNAME=IGC0006でCSV411Iを照合する。SVC06のSVC番号とROUTINEを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D PROG,SVCが成功したためD PROG,APF,DSNAME=SYS1.LINKLIBのCSV450Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象SVC06へ引き継げるものとする。SVCテーブルの再発していないことを示す値は確認済みとして扱う。さらにD PROG,LPA,MODNAME=IGC0006のCSV411IをCSV450Iと同種の値として併記する。</li><li>D. D PROG,APF,DSNAME=SYS1.LINKLIBを対象名なしで実行する。一覧の先頭行をSVC06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: BはAPF確認で CSV450I を読みSVC番号とROUTINEの主値として復旧後の安定性を確認しSVC06に残します。
構成上の背景: 復旧後の確認ではSVC表示を補助操作としSVCテーブルの再発していないことを示す値をROUTINEと対象SVC06で照合します。
候補ごとの理由: APF確認とSVC表示の役割を分けるとA: GRS資源直列化の値ではCSV450Iを確認できない点でSVC表示の範囲を越えます、B: CSV450IとCSV411Iを順に照合する点で現在値を示します、C: 補助操作の成功ではCSV450Iを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はSVC06と確定できない点でAPF確認を代替しません。結論として復旧後の確認の処理・テーブルで判定する対象は SVC06 です。
初出用語: 復旧後の確認で使う SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みを表しSVC番号とROUTINEを判定する際にSVC06へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC処理 SVCテーブル 復旧後の確認 SVC06</strong></p><p>検証目的: SVC処理のSVCテーブルについて復旧後の安定性を確認し、SVC06のSVC番号とROUTINEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SVC06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,APF,DSNAME=SYS1.LINKLIBを指定し、SVC06のAPF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,APF,DSNAME=SYS1.LINKLIB
→ Enter を押す
［画面・出力］
CSV450I APF DISPLAY FOR SYS1.LINKLIB VOLUME SMS STATUS AUTHORIZED
画面・出力にあるCSV450Iを読み、SVC番号とROUTINEと対象SVC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,SVCを指定し、SVC06のSVC表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,SVC
→ Enter を押す
［画面・出力］
CSV420I SVC TABLE ENTRY SVC=06 ROUTINE=IGC0006 TYPE=3 STATUS ACTIVE
画面・出力にあるROUTINEを読み、SVC番号とROUTINEと対象SVC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=IGC0006を指定し、SVC06のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=IGC0006
→ Enter を押す
［画面・出力］
CSV411I MODULE IGC0006 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、SVC番号とROUTINEと対象SVC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV450I が画面・出力に表示されること
② ステップ2 の ROUTINE が画面・出力に表示されること
③ ステップ3 の CSV411I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0189"><h3>SVC処理 SVCテーブル 復旧準備 SVC05</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>復旧準備では SVC処理 の モジュール所在 を主操作として SVC05 を判定します。再開前に必要な整合性への注意として「誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります」を SVC05 に残します。復旧準備を補助する APF確認 では CSV450I を補助値として SVC05 へ保存します。主判定の復旧準備では処理・テーブルの モジュール所在 から CSV411I を読み SVC05 へ残します。証跡照合の復旧準備では処理・テーブルの CSV411I と CSV450I を SVC05 に保存します。記録対応の復旧準備では処理・テーブルの SVC番号とROUTINE の証跡へ SVC05 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で SVC処理 の モジュール所在 と APF確認 を使い 復旧条件を確認 します。SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みです。誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります。CSV411I を読み対象 SVC05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずD PROG,LPA,MODNAME=IGC0005を実行する。CSV411Iを保存する。差分はD PROG,APF,DSNAME=SYS1.LINKLIBの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したD PROG,LPA,MODNAME=IGC0005の結果を使う。今回のD PROG,APF,DSNAME=SYS1.LINKLIBの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのSVC05の出力を再利用する。今回のD PROG,LPA,MODNAME=IGC0005とD PROG,APF,DSNAME=SYS1.LINKLIBは実行済みとして扱う。</li><li>D. D PROG,APF,DSNAME=SYS1.LINKLIBのCSV450IをSVC番号とROUTINEの主判定に採用する。D PROG,LPA,MODNAME=IGC0005の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Aはモジュール所在で CSV411I を読みSVC番号とROUTINEの主値として復旧条件を確認しSVC05に残します。
処理の仕組み: 復旧準備ではAPF確認を補助操作としSVCテーブルの再開前に必要な整合性をCSV450Iと対象SVC05で照合します。
選択結果の内訳: モジュール所在とAPF確認の役割を分けるとA: 変更前のCSV411Iを保存する点でモジュール所在に合います、B: 採取時刻が異なる点でSVC処理に使いません、C: 過去出力では今回の復旧準備を示せない点でSVCテーブルに使えません、D: CSV450IはCSV411Iを代替しないうえに追加前提も不正な点でSVC05を採用できません。結論として復旧準備の処理・テーブルで判定する対象は SVC05 です。
用語の説明: 復旧準備で使う SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みを表しSVC番号とROUTINEを判定する際にSVC05へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC処理 SVCテーブル 復旧準備 SVC05</strong></p><p>検証目的: SVC処理のSVCテーブルについて復旧条件を確認し、SVC05のSVC番号とROUTINEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SVC05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=IGC0005を指定し、SVC05のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=IGC0005
→ Enter を押す
［画面・出力］
CSV411I MODULE IGC0005 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、SVC番号とROUTINEと対象SVC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,APF,DSNAME=SYS1.LINKLIBを指定し、SVC05のAPF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,APF,DSNAME=SYS1.LINKLIB
→ Enter を押す
［画面・出力］
CSV450I APF DISPLAY FOR SYS1.LINKLIB VOLUME SMS STATUS AUTHORIZED
画面・出力にあるCSV450Iを読み、SVC番号とROUTINEと対象SVC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,SVCを指定し、SVC05のSVC表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,SVC
→ Enter を押す
［画面・出力］
CSV420I SVC TABLE ENTRY SVC=05 ROUTINE=IGC0005 TYPE=3 STATUS ACTIVE
画面・出力にあるROUTINEを読み、SVC番号とROUTINEと対象SVC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV411I が画面・出力に表示されること
② ステップ2 の CSV450I が画面・出力に表示されること
③ ステップ3 の ROUTINE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0190"><h3>SVC処理 SVCテーブル 構成監査 SVC08</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>構成監査では SVC処理 の モジュール所在 を主操作として SVC08 を判定します。定義値と稼働値の一致への注意として「誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります」を SVC08 に残します。構成監査を補助する APF確認 では CSV450I を補助値として SVC08 へ保存します。主判定の構成監査では処理・テーブルの モジュール所在 から CSV411I を読み SVC08 へ残します。証跡照合の構成監査では処理・テーブルの CSV411I と CSV450I を SVC08 に保存します。記録対応の構成監査では処理・テーブルの SVC番号とROUTINE の証跡へ SVC08 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で SVC処理 の モジュール所在 と APF確認 を照合し 定義値と稼働値の一致 を確かめます。SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みです。誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります。CSV411I を読む前に対象 SVC08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのSVC08の出力を再利用する。今回のD PROG,LPA,MODNAME=IGC0008とD PROG,APF,DSNAME=SYS1.LINKLIBは実行済みとして扱う。</li><li>B. D PROG,APF,DSNAME=SYS1.LINKLIBのCSV450IをSVC番号とROUTINEの主判定に採用する。D PROG,LPA,MODNAME=IGC0008の応答は採取対象から外す。</li><li>C. D PROG,SVCのROUTINEをCSV411Iと同義の成功表示として扱う。D PROG,LPA,MODNAME=IGC0008は実行しない。</li><li>D. D PROG,APF,DSNAME=SYS1.LINKLIBの結果だけでは確定しない。D PROG,LPA,MODNAME=IGC0008のCSV411Iを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Dはモジュール所在で CSV411I を読みSVC番号とROUTINEの主値として構成差分を監査しSVC08に残します。
実行時の背景: 構成監査ではAPF確認を補助操作としSVCテーブルの定義値と稼働値の一致をCSV450Iと対象SVC08で照合します。
四つの候補の理由: モジュール所在とAPF確認の役割を分けるとA: 過去出力では今回の構成監査を示せない点でSVC処理に使いません、B: CSV450IはCSV411Iを代替しない点でSVCテーブルに使えません、C: ROUTINEとCSV411Iは確認項目が異なる点でSVC08を採用できません、D: CSV411Iを主証跡として区別する点で主証跡になります。結論として構成監査の処理・テーブルで判定する対象は SVC08 です。
初出語定義: 構成監査で使う SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みを表しSVC番号とROUTINEを判定する際にSVC08へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC処理 SVCテーブル 構成監査 SVC08</strong></p><p>検証目的: SVC処理のSVCテーブルについて構成差分を監査し、SVC08のSVC番号とROUTINEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SVC08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=IGC0008を指定し、SVC08のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=IGC0008
→ Enter を押す
［画面・出力］
CSV411I MODULE IGC0008 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、SVC番号とROUTINEと対象SVC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,APF,DSNAME=SYS1.LINKLIBを指定し、SVC08のAPF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,APF,DSNAME=SYS1.LINKLIB
→ Enter を押す
［画面・出力］
CSV450I APF DISPLAY FOR SYS1.LINKLIB VOLUME SMS STATUS AUTHORIZED
画面・出力にあるCSV450Iを読み、SVC番号とROUTINEと対象SVC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,SVCを指定し、SVC08のSVC表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,SVC
→ Enter を押す
［画面・出力］
CSV420I SVC TABLE ENTRY SVC=08 ROUTINE=IGC0008 TYPE=3 STATUS ACTIVE
画面・出力にあるROUTINEを読み、SVC番号とROUTINEと対象SVC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV411I が画面・出力に表示されること
② ステップ2 の CSV450I が画面・出力に表示されること
③ ステップ3 の ROUTINE が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0191"><h3>SVC処理 SVCテーブル 通常状態の確認 SVC01</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>通常状態の確認では SVC処理 の SVC表示 を主操作として SVC01 を判定します。基準値と現在値の差への注意として「誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります」を SVC01 に残します。通常状態の確認を補助する モジュール所在 では CSV411I を補助値として SVC01 へ保存します。主判定の通常状態の確認では処理・テーブルの SVC表示 から ROUTINE を読み SVC01 へ残します。証跡照合の通常状態の確認では処理・テーブルの ROUTINE と CSV411I を SVC01 に保存します。記録対応の通常状態の確認では処理・テーブルの SVC番号とROUTINE の証跡へ SVC01 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で SVC処理 の SVC表示 と モジュール所在 を用い 通常状態を確定 します。SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みです。誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります。ROUTINE で対象 SVC01 の SVC番号とROUTINE を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. D PROG,SVCを先に実行する。対象SVC01のROUTINEをSVC番号とROUTINEとして記録する。続いてD PROG,LPA,MODNAME=IGC0001で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. D PROG,LPA,MODNAME=IGC0001のCSV411IをSVC番号とROUTINEの主判定に採用する。D PROG,SVCの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. D PROG,APF,DSNAME=SYS1.LINKLIBのCSV450IをROUTINEと同義の成功表示として扱う。D PROG,SVCは実行しない。</li><li>D. D PROG,SVCが応答を返した時点で正常とする。応答中のROUTINEの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: AはSVC表示で ROUTINE を読みSVC番号とROUTINEの主値として通常状態を確定しSVC01に残します。
背景・仕組み: 通常状態の確認ではモジュール所在を補助操作としSVCテーブルの基準値と現在値の差をCSV411Iと対象SVC01で照合します。
選択肢の理由: SVC表示とモジュール所在の役割を分けるとA: ROUTINEを主値として補助結果と照合する点で正答です、B: CSV411IはROUTINEを代替しないうえに追加前提も不正な点でSVC01を採用できません、C: CSV450IとROUTINEは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではSVC番号とROUTINEを判定できない点で一次資料と一致しません。結論として通常状態の確認の処理・テーブルで判定する対象は SVC01 です。
用語の初出定義: 通常状態の確認で使う SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みを表しSVC番号とROUTINEを判定する際にSVC01へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC処理 SVCテーブル 通常状態の確認 SVC01</strong></p><p>検証目的: SVC処理のSVCテーブルについて通常状態を確定し、SVC01のSVC番号とROUTINEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SVC01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,SVCを指定し、SVC01のSVC表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,SVC
→ Enter を押す
［画面・出力］
CSV420I SVC TABLE ENTRY SVC=01 ROUTINE=IGC0001 TYPE=3 STATUS ACTIVE
画面・出力にあるROUTINEを読み、SVC番号とROUTINEと対象SVC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=IGC0001を指定し、SVC01のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=IGC0001
→ Enter を押す
［画面・出力］
CSV411I MODULE IGC0001 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、SVC番号とROUTINEと対象SVC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,APF,DSNAME=SYS1.LINKLIBを指定し、SVC01のAPF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,APF,DSNAME=SYS1.LINKLIB
→ Enter を押す
［画面・出力］
CSV450I APF DISPLAY FOR SYS1.LINKLIB VOLUME SMS STATUS AUTHORIZED
画面・出力にあるCSV450Iを読み、SVC番号とROUTINEと対象SVC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ROUTINE が画面・出力に表示されること
② ステップ2 の CSV411I が画面・出力に表示されること
③ ステップ3 の CSV450I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0192"><h3>SVC処理 SVCテーブル 障害切り分け SVC04</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>障害切り分けでは SVC処理 の SVC表示 を主操作として SVC04 を判定します。最初に失敗した処理への注意として「誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります」を SVC04 に残します。障害切り分けを補助する モジュール所在 では CSV411I を補助値として SVC04 へ保存します。主判定の障害切り分けでは処理・テーブルの SVC表示 から ROUTINE を読み SVC04 へ残します。証跡照合の障害切り分けでは処理・テーブルの ROUTINE と CSV411I を SVC04 に保存します。記録対応の障害切り分けでは処理・テーブルの SVC番号とROUTINE の証跡へ SVC04 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで SVC処理 の SVC表示 と モジュール所在 の役割を分け 最初に失敗した処理 を調べます。SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みです。誤ったSVC番号や旧入口モジュールを障害原因として見落とす危険があります。対象 SVC04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. D PROG,APF,DSNAME=SYS1.LINKLIBのCSV450IをROUTINEと同義の成功表示として扱う。D PROG,SVCは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. D PROG,SVCが応答を返した時点で正常とする。応答中のROUTINEの値は記録しない。</li><li>C. D PROG,SVCのコマンド文字列だけを記録する。ROUTINEを含む応答行は保存しない。</li><li>D. D PROG,SVCの出力でSVC04とROUTINEが同じ応答にあることを確認する。SVC番号とROUTINEをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: DはSVC表示で ROUTINE を読みSVC番号とROUTINEの主値として障害範囲を限定しSVC04に残します。
技術的背景: 障害切り分けではモジュール所在を補助操作としSVCテーブルの最初に失敗した処理をCSV411Iと対象SVC04で照合します。
四択の評価: SVC表示とモジュール所在の役割を分けるとA: CSV450IとROUTINEは確認項目が異なるうえに追加前提も不正な点でSVC04を採用できません、B: 応答の有無だけではSVC番号とROUTINEを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではSVC番号とROUTINEを証明できない点で一次資料と一致しません、D: SVC04とROUTINEを同じ応答で結ぶ点でSVC04を判定できます。結論として障害切り分けの処理・テーブルで判定する対象は SVC04 です。
初出語の意味: 障害切り分けで使う SVCテーブル は監視プログラム呼出し番号を入口モジュールと属性へ対応させ、システムサービスへ制御を渡す仕組みを表しSVC番号とROUTINEを判定する際にSVC04へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC処理 SVCテーブル 障害切り分け SVC04</strong></p><p>検証目的: SVC処理のSVCテーブルについて障害範囲を限定し、SVC04のSVC番号とROUTINEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SVC04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,SVCを指定し、SVC04のSVC表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,SVC
→ Enter を押す
［画面・出力］
CSV420I SVC TABLE ENTRY SVC=04 ROUTINE=IGC0004 TYPE=3 STATUS ACTIVE
画面・出力にあるROUTINEを読み、SVC番号とROUTINEと対象SVC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=IGC0004を指定し、SVC04のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=IGC0004
→ Enter を押す
［画面・出力］
CSV411I MODULE IGC0004 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、SVC番号とROUTINEと対象SVC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのSVC処理を確認する入力画面です。COMMAND入力口へD PROG,APF,DSNAME=SYS1.LINKLIBを指定し、SVC04のAPF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,APF,DSNAME=SYS1.LINKLIB
→ Enter を押す
［画面・出力］
CSV450I APF DISPLAY FOR SYS1.LINKLIB VOLUME SMS STATUS AUTHORIZED
画面・出力にあるCSV450Iを読み、SVC番号とROUTINEと対象SVC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ROUTINE が画面・出力に表示されること
② ステップ2 の CSV411I が画面・出力に表示されること
③ ステップ3 の CSV450I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0193"><h3>SVC割り込み 直列化確認 運用確認076</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>第七十六観点 z/OS System Programming の SVC処理 では SVC割り込み を障害調査で照合します（第七十六観点）。第七十六観点 資料上は 問題プログラムからz/OSサービスを要求し、監視プログラム状態へ制御として扱います（第七十六観点）。第七十六観点 ROUTCDE=ALL を起点に表示値を戻し、オペレーター応答漏れの防止を点検します（第七十六観点）。第七十六観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録076へ書きます（第七十六観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第七十六証跡です。運用確認076 の確認で SVC割り込み を見直します。確認観点は SVC割り込み、直列化確認、運用確認 です。オペレーター応答漏れの防止のために、D TRACE のIEE843I表示 を使った運用記録として最も適切な扱いはどれか。</p><ul class="kb-choices"><li>A. LPA管理 の一般メモを採り、ROUTCDE=ALL、メッセージID、時刻の対応を記録外に置き、zOSSP誤記076として調査範囲を狭める。</li><li>B. SVC割り込み の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延076として扱う。</li><li>C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在076として残す。</li><li>D. D TRACE のIEE843I表示 と ROUTCDE=ALL を同一票へ記録し、SVC割り込み を zOSSP正076で確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第七十六観点 照合結果: Dは ROUTCDE=ALL をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第七十六観点）。第七十六観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第七十六観点）。第七十六観点 誤答確認: Aは ROUTCDE=ALL 未追跡、Bはコマンド確認不足、Cは別システム混同が理由です（第七十六観点）。第七十六観点 用語説明: WTOは通知メッセージです（第七十六観点）。第七十六観点 WTORは応答を求めるメッセージです（第七十六観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC割り込み 直列化確認 運用確認076</strong></p><p>検証目的: SVC割り込み の 直列化確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SMF</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SVC割り込み の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D SMF,O
→ Enter を押す
［画面・出力］
IEE974I 11.01.04 SMF DATA SET STATUS
NAME       VOLSER  STATUS
SMF.MAN1   SMS001  ACTIVE
SMF.MAN2   SMS002  EMPTY
画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SVC割り込み の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SWITCH SMF
→ Enter を押す
［画面・出力］
IEE362A SMF ENTER DUMP FOR DATA SET SMF.MAN1
IEE360I SMF NOW RECORDING ON SMF.MAN2
画面・出力には IEE360I が含まれる。IEE360I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SVC割り込み の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
JES2 SDSF ST
COMMAND ===&gt; S IFASMFD04
→ Enter を押す
［画面・出力］
IEF403I IFASMFD04 - STARTED
IFASMFDP SYSPRINT
INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0194"><h3>SVC新PSW 直列化確認 運用確認026</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>第二十六観点 SVC新PSW は z/OS System Programming の SVC処理 で扱う管理項目です（第二十六観点）。第二十六観点 SVC割り込み後に使用され、FLIHが制御を受けるためのプログラム状という説明を操作結果と照合します（第二十六観点）。第二十六観点 RNAME=SYS1.PARMLIB、D TRACE のIEE843I表示、定義メンバーを照合し、オペレーター応答漏れの防止を確認します（第二十六観点）。第二十六観点 証跡には資料IDと確認値を併記し、zOSSP記録026として保存します（第二十六観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第二十六証跡です。運用確認026 の確認で SVC新PSW を見直します。確認観点は SVC新PSW、直列化確認、運用確認 です。メッセージID、定義メンバー、表示出力を同じ確認票に置く対応として適切なものはどれか。</p><ul class="kb-choices"><li>A. ディスパッチ制御 の一般メモを採り、RNAME=SYS1.PARMLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記026として調査範囲を狭める。</li><li>B. SVC新PSW の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延026として扱う。</li><li>C. D TRACE のIEE843I表示 と RNAME=SYS1.PARMLIB を同一票へ記録し、SVC新PSW を zOSSP正026で確定する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在026として残す。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第二十六観点 正答根拠: Cは D TRACE のIEE843I表示 と RNAME=SYS1.PARMLIB を結び付けるため、対象システムの取り違えを防げます（第二十六観点）。第二十六観点 操作背景: WTOとWTORはオペレーター通知と応答をコンソールログへ残します（第二十六観点）。第二十六観点 誤答点検: Aはシステム名欠落、Bは定義未確認、Dは時刻差の欠落が理由です（第二十六観点）。第二十六観点 用語補足: ENQは資源を直列化します（第二十六観点）。第二十六観点 DEQは取得した資源を解放します（第二十六観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC新PSW 直列化確認 運用確認026</strong></p><p>検証目的: SVC新PSW の 直列化確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / parmlib review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SVC新PSW の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(PROGSP)
→ Enter を押す
［画面・出力］
APF FORMAT(DYNAMIC)
APF ADD DSNAME(MYPROG.LOADLIB) VOLUME(MPRES3)
LPA ADD MODNAME(MOD02) DSNAME(SYS1.LPALIB)
画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SVC新PSW の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SET PROG=SP
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE252I が含まれる。IEE252I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SVC新PSW の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 06.10.02 PROG,APF DISPLAY 825
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
  12  MPRES3 MYPROG.LOADLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0195"><h3>SWITCH SMF 状態確認 運用確認060</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 中級</p><p>第六十観点 z/OS System Programming の SVC処理 では SWITCH SMF を障害調査で照合します（第六十観点）。第六十観点 資料上は SMF記録先の切替とバッファ書き出しを行い、ダンプ出口へ制御を渡す操として扱います（第六十観点）。第六十観点 SYS1.PARMLIB(GRSRNLSP) を起点に表示値を戻し、診断ログの再現性確保を点検します（第六十観点）。第六十観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録060へ書きます（第六十観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第六十証跡です。SWITCH SMF の表示とメッセージIDを比べます。確認観点は SWITCH SMF、状態確認、運用確認 です。診断ログの再現性確保を満たす記録方法として、表示値と定義を結ぶものはどれか。</p><ul class="kb-choices"><li>A. GRS資源直列化 の一般メモを採り、SYS1.PARMLIB(GRSRNLSP)、メッセージID、時刻の対応を記録外に置き、zOSSP誤記060として調査範囲を狭める。</li><li>B. SWITCH SMF の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延060として扱う。</li><li>C. SETPROG APF後のCSV410I表示 と SYS1.PARMLIB(GRSRNLSP) を同一票へ記録し、SWITCH SMF を zOSSP正060で確定する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在060として残す。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第六十観点 照合結果: Cは SYS1.PARMLIB(GRSRNLSP) をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第六十観点）。第六十観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第六十観点）。第六十観点 誤答確認: Aは SYS1.PARMLIB(GRSRNLSP) 未追跡、Bはコマンド確認不足、Dは別システム混同が理由です（第六十観点）。第六十観点 初出定義: PSWは実行状態を示す語です（第六十観点）。第六十観点 SVCは監視プログラム呼出しです（第六十観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SWITCH SMF 状態確認 運用確認060</strong></p><p>検証目的: SWITCH SMF の 状態確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SMF</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SWITCH SMF の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D SMF,O
→ Enter を押す
［画面・出力］
IEE974I 11.01.12 SMF DATA SET STATUS
NAME       VOLSER  STATUS
SMF.MAN1   SMS001  ACTIVE
SMF.MAN2   SMS002  EMPTY
画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SWITCH SMF の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SWITCH SMF
→ Enter を押す
［画面・出力］
IEE362A SMF ENTER DUMP FOR DATA SET SMF.MAN1
IEE360I SMF NOW RECORDING ON SMF.MAN2
画面・出力には IEE360I が含まれる。IEE360I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SWITCH SMF の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
JES2 SDSF ST
COMMAND ===&gt; S IFASMFD12
→ Enter を押す
［画面・出力］
IEF403I IFASMFD12 - STARTED
IFASMFDP SYSPRINT
INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0196"><h3>VERBX LOGDATA 表示確認 運用確認093</h3><p class="kb-meta">分類: SVC処理 ・ 難易度: 上級</p><p>第九十三観点 SVC処理 で VERBX LOGDATA は 表示確認 の対象です（第九十三観点）。第九十三観点 確認時には ダンプ内のLOGREC記録を整形し、EREP形式で確認するIPCS処という性質を前提にします（第九十三観点）。第九十三観点 DISPLAY R,ALL の未応答要求表示 と TCB=008F21A0 を同じ証跡に置き、共通ストレージ変更の記録を管理します（第九十三観点）。第九十三観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録093から再現します（第九十三観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第九十三証跡です。zOSSP記録093として TCB=008F21A0 の証跡を残します。確認観点は VERBX LOGDATA、表示確認、運用確認 です。DISPLAY R,ALL の未応答要求表示 と TCB=008F21A0 を合わせて読む時の採用方針として正しいものはどれか。</p><ul class="kb-choices"><li>A. トレース診断 の一般メモを採り、TCB=008F21A0、メッセージID、時刻の対応を記録外に置き、zOSSP誤記093として調査範囲を狭める。</li><li>B. DISPLAY R,ALL の未応答要求表示 と TCB=008F21A0 を同一票へ記録し、VERBX LOGDATA を zOSSP正093で確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. VERBX LOGDATA の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延093として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在093として残す。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 第九十三観点 正解確認: Bは VERBX LOGDATA と TCB=008F21A0 を同じ証跡で扱うため、後続の照合に使えます（第九十三観点）。第九十三観点 実行背景: SVC、TCB、SRB、PSWは割り込みとディスパッチの説明に使います（第九十三観点）。第九十三観点 誤答比較: Aは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第九十三観点）。第九十三観点 用語整理: SMFはシステム測定記録です（第九十三観点）。第九十三観点 IFASMFDPはSMFデータ退避に使います（第九十三観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>VERBX LOGDATA 表示確認 運用確認093</strong></p><p>検証目的: VERBX LOGDATA の 表示確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / operations</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により VERBX LOGDATA の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY R,ALL
→ Enter を押す
［画面・出力］
IEE112I 11.15.21 DISPLAY R 712
REPLY ID   MESSAGE TEXT
005        IEA793A SPECIFY DUMP OPTION FOR TCB=008F21A0
画面・出力には IEE112I が含まれる。IEE112I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により VERBX LOGDATA の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D C
→ Enter を押す
［画面・出力］
IEE889I 15.33.21 CONSOLE DISPLAY 522
MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
画面・出力には IEE889I が含まれる。IEE889I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により VERBX LOGDATA の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; R 005,INFO
→ Enter を押す
［画面・出力］
IEE600I REPLY TO 005 IS;INFO
IEA631I OPERATOR OPER21 NOW ACTIVE, SYSTEM=SC65
画面・出力には IEE600I が含まれる。IEE600I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


## TCB/SRB管理


<section class="kb-item" id="c38-i0197"><h3>D TRACE ログ確認 運用確認094</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 上級</p><p>第九十四観点 D TRACE は z/OS System Programming の TCB/SRB管理 で扱う管理項目です（第九十四観点）。第九十四観点 システムまたはコンポーネントのトレース状態を表示する診断コマンドという説明を操作結果と照合します（第九十四観点）。第九十四観点 SRB=00AF1100、SWITCH SMF後のSMF切替記録、定義メンバーを照合し、資源競合時の保有者確認を確認します（第九十四観点）。第九十四観点 証跡には資料IDと確認値を併記し、zOSSP記録094として保存します（第九十四観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第九十四証跡です。z/OS System Programming の TCB/SRB管理 で切分けを行います。確認観点は D TRACE、ログ確認、運用確認 です。資源競合時の保有者確認のために、SWITCH SMF後のSMF切替記録 を使った運用記録として最も適切な扱いはどれか。</p><ul class="kb-choices"><li>A. SWITCH SMF後のSMF切替記録 と SRB=00AF1100 を同一票へ記録し、D TRACE を zOSSP正094で確定する。 <span class="kb-ok">✅ 正解</span></li><li>B. APF管理 の一般メモを採り、SRB=00AF1100、メッセージID、時刻の対応を記録外に置き、zOSSP誤記094として調査範囲を狭める。</li><li>C. D TRACE の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延094として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在094として残す。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 第九十四観点 正答根拠: Aは SWITCH SMF後のSMF切替記録 と SRB=00AF1100 を結び付けるため、対象システムの取り違えを防げます（第九十四観点）。第九十四観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第九十四観点）。第九十四観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第九十四観点）。第九十四観点 用語説明: WTOは通知メッセージです（第九十四観点）。第九十四観点 WTORは応答を求めるメッセージです（第九十四観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D TRACE ログ確認 運用確認094</strong></p><p>検証目的: D TRACE の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: IPCS / dump analysis</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により D TRACE の値を確認し、対象の現在値を固定する。
［操作（入力）］
IPCS option 6
COMMAND ===&gt; VERBX LOGDATA
→ Enter を押す
［画面・出力］
LOGDATA VERBEXIT PROCESSING
LOGREC BUFFER RECORDS LOCATED
EREP DETAIL EDIT REPORT FOLLOWS
画面・出力には LOGDATA が含まれる。LOGDATA を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により D TRACE の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.30.22 TRACE DISPLAY 193
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON MT=(ON,024K)
画面・出力には IEE843I が含まれる。IEE843I を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により D TRACE の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
IPCS command line
COMMAND ===&gt; STATUS CPU
→ Enter を押す
［画面・出力］
IPCS STATUS CPU
PSW=070C1000 81234567  ASID=0010
CURRENT TCB ADDRESS SRB=00AF1100
画面・出力には ASID=0010 が含まれる。ASID=0010 を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LOGDATA が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE843I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ASID=0010 が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0198"><h3>FLIH処理 割り込み確認 運用確認027</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 中級</p><p>第二十七観点 TCB/SRB管理 の運用では FLIH処理 を表示、定義、証跡で確認します（第二十七観点）。第二十七観点 役割は 割り込みを受け、PSWやレジスター状態を保存して適切な処理へ渡す入口という範囲です（第二十七観点）。第二十七観点 IPCS VERBX LOGDATA出力 の値を SMF.MAN1 と合わせ、実行単位の優先順位確認を記録します（第二十七観点）。第二十七観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録027に残します（第二十七観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FLIH処理 割り込み確認 運用確認027</strong></p><p>検証目的: FLIH処理 の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / GRS</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により FLIH処理 の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS
→ Enter を押す
［画面・出力］
ISG343I 10.27.03 GRS STATUS 846
SYSTEM    STATE               SYSTEM    STATE
SC65      CONNECTED           SC63      CONNECTED
GRS STAR MODE INFORMATION
画面・出力には ISG343I が含まれる。ISG343I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により FLIH処理 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS,RNL=INCL
→ Enter を押す
［画面・出力］
ISG343I 10.28.03 GRS STATUS 856
RNL=INCL
QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により FLIH処理 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D XCF,STR,STRNAME=ISGLOCK
→ Enter を押す
［画面・出力］
IXC360I 10.29.03 DISPLAY XCF 866
STRUCTURE NAME: ISGLOCK
STATUS: ALLOCATED IN CFRM POLICY
画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0199"><h3>SVC新PSW 割り込み確認 運用確認077</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 中級</p><p>第七十七観点 TCB/SRB管理 で SVC新PSW は 割り込み確認 の対象です（第七十七観点）。第七十七観点 確認時には SVC割り込み後に使用され、FLIHが制御を受けるためのプログラム状という性質を前提にします（第七十七観点）。第七十七観点 IPCS VERBX LOGDATA出力 と AUTH=CMDS を同じ証跡に置き、実行単位の優先順位確認を管理します（第七十七観点）。第七十七観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録077から再現します（第七十七観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC新PSW 割り込み確認 運用確認077</strong></p><p>検証目的: SVC新PSW の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / operations</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SVC新PSW の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY R,ALL
→ Enter を押す
［画面・出力］
IEE112I 11.15.05 DISPLAY R 776
REPLY ID   MESSAGE TEXT
005        IEA793A SPECIFY DUMP OPTION FOR AUTH=CMDS
画面・出力には IEE112I が含まれる。IEE112I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SVC新PSW の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D C
→ Enter を押す
［画面・出力］
IEE889I 15.33.05 CONSOLE DISPLAY 506
MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
画面・出力には IEE889I が含まれる。IEE889I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SVC新PSW の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; R 005,INFO
→ Enter を押す
［画面・出力］
IEE600I REPLY TO 005 IS;INFO
IEA631I OPERATOR OPER05 NOW ACTIVE, SYSTEM=SC65
画面・出力には IEE600I が含まれる。IEE600I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0200"><h3>TCB/SRB管理 TCBとSRB ログとの照合 TCB07</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 上級</p><p>ログとの照合では TCB/SRB管理 の TCBサマリー を主操作として TCB07 を判定します。時刻と対象識別子への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB07 に残します。ログとの照合を補助する SRB情報 では SRB を補助値として TCB07 へ保存します。主判定のログとの照合では管理の TCBサマリー から TCB を読み TCB07 へ残します。証跡照合のログとの照合では管理の TCB と SRB を TCB07 に保存します。記録対応のログとの照合では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB07 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で TCB/SRB管理 の TCBサマリー と SRB情報 を組み合わせる際は TCBとSRB がタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックという仕組みを前提にします。SRB時間をアプリケーションTCB時間として評価する危険があります。TCB と TCB/SRB ADDRESSとWAIT を対象 TCB07 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. IP SUMMARY FORMAT ASID(X07)が応答を返した時点で正常とする。応答中のTCBの値は記録しない。CURRENTをTCBと同じ判定値とみなし対象TCB07の主証跡にする。TCBとSRBの時刻と対象識別子は確認済みとして扱う。さらにIP STATUS CPUのCURRENTをTCBと同種の値として併記する。</li><li>B. IP SUMMARY FORMAT ASID(X07)のコマンド文字列だけを記録する。TCBを含む応答行は保存しない。</li><li>C. TCBを含むTCBサマリーの応答行を保存する。その応答を得るためIP SUMMARY FORMAT ASID(X07)を使用する。対象TCB07のTCB/SRB ADDRESSとWAITとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. TCBとSRBの停止または再定義を実施する。その後にIP SUMMARY FORMAT ASID(X07)でTCBを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 適切な判定: CはTCBサマリーで TCB を読みTCB/SRB ADDRESSとWAITの主値として操作とログを対応しTCB07に残します。
機能の仕組み: ログとの照合ではSRB情報を補助操作としTCBとSRBの時刻と対象識別子をSRBと対象TCB07で照合します。
各候補の評価: TCBサマリーとSRB情報の役割を分けるとA: 応答の有無だけではTCB/SRB ADDRESSとWAITを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではTCB/SRB ADDRESSとWAITを証明できない点で一次資料と一致しません、C: TCBの実値を対象別に残す点でTCB07を判定できます、D: 変更前のTCB/SRB ADDRESSとWAITを失う点でSRB情報の範囲を越えます。結論としてログとの照合の管理で判定する対象は TCB07 です。
用語の定義: ログとの照合で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB07へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCB/SRB管理 TCBとSRB ログとの照合 TCB07</strong></p><p>検証目的: TCB/SRB管理のTCBとSRBについて操作とログを対応し、TCB07のTCB/SRB ADDRESSとWAITを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TCB07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X07)を指定し、TCB07のTCBサマリーを表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SUMMARY FORMAT ASID(X07)
→ Enter を押す
［画面・出力］
TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X07)を指定し、TCB07のSRB情報を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP VERBX SRMDATA ASID(X07)
→ Enter を押す
［画面・出力］
SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB07のCPU状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP STATUS CPU
→ Enter を押す
［画面・出力］
CPU 0000 CURRENT ASID 0007 TCB 008F21A0 PSW 078D1000
画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の F21A0 が画面・出力に表示されること
② ステップ2 の AF1100 が画面・出力に表示されること
③ ステップ3 の CURRENT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0201"><h3>TCB/SRB管理 TCBとSRB 代替経路の確認 TCB10</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 上級</p><p>代替経路の確認では TCB/SRB管理 の TCBサマリー を主操作として TCB10 を判定します。主経路との役割差への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB10 に残します。代替経路の確認を補助する SRB情報 では SRB を補助値として TCB10 へ保存します。主判定の代替経路の確認では管理の TCBサマリー から TCB を読み TCB10 へ残します。証跡照合の代替経路の確認では管理の TCB と SRB を TCB10 に保存します。記録対応の代替経路の確認では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB10 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で TCB/SRB管理 の TCBサマリー と SRB情報 を実施し TCBとSRB の役割を確認します。SRB時間をアプリケーションTCB時間として評価する危険があります。対象 TCB10 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. IP SUMMARY FORMAT ASID(X10)のコマンド文字列だけを記録する。TCBを含む応答行は保存しない。</li><li>B. IP SUMMARY FORMAT ASID(X10)とIP VERBX SRMDATA ASID(X10)の対象名をそろえる。前者のTCBをTCB/SRB ADDRESSとWAITの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. TCBとSRBの停止または再定義を実施する。その後にIP SUMMARY FORMAT ASID(X10)でTCBを採取する。</li><li>D. SVC処理のSVC番号とROUTINEを確認する。その値をTCB/SRB管理のTCB10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい判定結果: BはTCBサマリーで TCB を読みTCB/SRB ADDRESSとWAITの主値として代替手段の成立を確認しTCB10に残します。
運用上の背景: 代替経路の確認ではSRB情報を補助操作としTCBとSRBの主経路との役割差をSRBと対象TCB10で照合します。
候補別の検討: TCBサマリーとSRB情報の役割を分けるとA: 入力記録だけではTCB/SRB ADDRESSとWAITを証明できない点で一次資料と一致しません、B: 同じ対象名のTCBを採用する点でTCB10を判定できます、C: 変更前のTCB/SRB ADDRESSとWAITを失う点でSRB情報の範囲を越えます、D: SVC処理の値ではTCBを確認できない点でTCB10の値を示しません。結論として代替経路の確認の管理で判定する対象は TCB10 です。
重要用語の定義: 代替経路の確認で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB10へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCB/SRB管理 TCBとSRB 代替経路の確認 TCB10</strong></p><p>検証目的: TCB/SRB管理のTCBとSRBについて代替手段の成立を確認し、TCB10のTCB/SRB ADDRESSとWAITを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TCB10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X10)を指定し、TCB10のTCBサマリーを表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SUMMARY FORMAT ASID(X10)
→ Enter を押す
［画面・出力］
TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X10)を指定し、TCB10のSRB情報を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP VERBX SRMDATA ASID(X10)
→ Enter を押す
［画面・出力］
SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB10のCPU状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP STATUS CPU
→ Enter を押す
［画面・出力］
CPU 0000 CURRENT ASID 0010 TCB 008F21A0 PSW 078D1000
画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の F21A0 が画面・出力に表示されること
② ステップ2 の AF1100 が画面・出力に表示されること
③ ステップ3 の CURRENT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0202"><h3>TCB/SRB管理 TCBとSRB 変更前の確認 TCB02</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 上級</p><p>変更前の確認では TCB/SRB管理 の SRB情報 を主操作として TCB02 を判定します。変更対象と非対象の境界への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB02 に残します。変更前の確認を補助する CPU状態 では CURRENT を補助値として TCB02 へ保存します。主判定の変更前の確認では管理の SRB情報 から SRB を読み TCB02 へ残します。証跡照合の変更前の確認では管理の SRB と CURRENT を TCB02 に保存します。記録対応の変更前の確認では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB02 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で TCB/SRB管理 の SRB情報 と CPU状態 の役割を分け 変更対象と非対象の境界 を調べます。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。対象 TCB02 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. IP VERBX SRMDATA ASID(X02)を対象名なしで実行する。一覧の先頭行をTCB02の結果として記録する。</li><li>B. 対象TCB02についてIP VERBX SRMDATA ASID(X02)の応答からSRBを確認する。IP STATUS CPUは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存したIP VERBX SRMDATA ASID(X02)の結果を使う。今回のIP STATUS CPUの結果と同一時点の証跡として比較する。</li><li>D. 保存済みのTCB02の出力を再利用する。今回のIP VERBX SRMDATA ASID(X02)とIP STATUS CPUは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用理由: BはSRB情報で SRB を読みTCB/SRB ADDRESSとWAITの主値として変更前の証跡を保存しTCB02に残します。
動作の背景: 変更前の確認ではCPU状態を補助操作としTCBとSRBの変更対象と非対象の境界をCURRENTと対象TCB02で照合します。
各選択肢の検討: SRB情報とCPU状態の役割を分けるとA: 先頭行はTCB02と確定できない点で変更前の確認に合いません、B: SRBと補助証跡の時刻を合わせる点でSRB情報に合います、C: 採取時刻が異なる点でTCB/SRB管理に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でTCBとSRBに使えません。結論として変更前の確認の管理で判定する対象は TCB02 です。
初出用語の定義: 変更前の確認で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB02へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCB/SRB管理 TCBとSRB 変更前の確認 TCB02</strong></p><p>検証目的: TCB/SRB管理のTCBとSRBについて変更前の証跡を保存し、TCB02のTCB/SRB ADDRESSとWAITを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TCB02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X02)を指定し、TCB02のSRB情報を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP VERBX SRMDATA ASID(X02)
→ Enter を押す
［画面・出力］
SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB02のCPU状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP STATUS CPU
→ Enter を押す
［画面・出力］
CPU 0000 CURRENT ASID 0002 TCB 008F21A0 PSW 078D1000
画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X02)を指定し、TCB02のTCBサマリーを表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SUMMARY FORMAT ASID(X02)
→ Enter を押す
［画面・出力］
TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の AF1100 が画面・出力に表示されること
② ステップ2 の CURRENT が画面・出力に表示されること
③ ステップ3 の F21A0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0203"><h3>TCB/SRB管理 TCBとSRB 変更後の確認 TCB03</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 上級</p><p>変更後の確認では TCB/SRB管理 の CPU状態 を主操作として TCB03 を判定します。反映値と残存値への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB03 に残します。変更後の確認を補助する TCBサマリー では TCB を補助値として TCB03 へ保存します。主判定の変更後の確認では管理の CPU状態 から CURRENT を読み TCB03 へ残します。証跡照合の変更後の確認では管理の CURRENT と TCB を TCB03 に保存します。記録対応の変更後の確認では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB03 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で TCB/SRB管理 の CPU状態 と TCBサマリー を使い 変更結果を検証 します。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。CURRENT を読み対象 TCB03 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. TCBとSRBの停止または再定義を実施する。その後にIP STATUS CPUでCURRENTを採取する。</li><li>B. LNKLST管理のSET名とDATASET順序を確認する。その値をTCB/SRB管理のTCB03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>C. IP SUMMARY FORMAT ASID(X03)で周辺状態を押さえる。その後にIP STATUS CPUでCURRENTを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. IP SUMMARY FORMAT ASID(X03)が成功したためIP STATUS CPUのCURRENTも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答の根拠: CはCPU状態で CURRENT を読みTCB/SRB ADDRESSとWAITの主値として変更結果を検証しTCB03に残します。
内部の仕組み: 変更後の確認ではTCBサマリーを補助操作としTCBとSRBの反映値と残存値をTCBと対象TCB03で照合します。
誤答を含む比較: CPU状態とTCBサマリーの役割を分けるとA: 変更前のTCB/SRB ADDRESSとWAITを失う点でTCB/SRB ADDRESSとWAITを確認できません、B: LNKLST管理の値ではCURRENTを確認できないうえに追加前提も不正な点でTCBサマリーの範囲を越えます、C: 周辺状態の後にCURRENTを確認する点で現在値を示します、D: 補助操作の成功ではCURRENTを確定できない点で変更後の確認に合いません。結論として変更後の確認の管理で判定する対象は TCB03 です。
用語定義: 変更後の確認で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB03へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCB/SRB管理 TCBとSRB 変更後の確認 TCB03</strong></p><p>検証目的: TCB/SRB管理のTCBとSRBについて変更結果を検証し、TCB03のTCB/SRB ADDRESSとWAITを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TCB03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB03のCPU状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP STATUS CPU
→ Enter を押す
［画面・出力］
CPU 0000 CURRENT ASID 0003 TCB 008F21A0 PSW 078D1000
画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X03)を指定し、TCB03のTCBサマリーを表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SUMMARY FORMAT ASID(X03)
→ Enter を押す
［画面・出力］
TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X03)を指定し、TCB03のSRB情報を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP VERBX SRMDATA ASID(X03)
→ Enter を押す
［画面・出力］
SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CURRENT が画面・出力に表示されること
② ステップ2 の F21A0 が画面・出力に表示されること
③ ステップ3 の AF1100 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0204"><h3>TCB/SRB管理 TCBとSRB 引継ぎ記録 TCB09</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 上級</p><p>引継ぎ記録では TCB/SRB管理 の CPU状態 を主操作として TCB09 を判定します。次担当者が追跡できる証跡への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB09 に残します。引継ぎ記録を補助する TCBサマリー では TCB を補助値として TCB09 へ保存します。主判定の引継ぎ記録では管理の CPU状態 から CURRENT を読み TCB09 へ残します。証跡照合の引継ぎ記録では管理の CURRENT と TCB を TCB09 に保存します。記録対応の引継ぎ記録では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB09 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で TCB/SRB管理 の CPU状態 と TCBサマリー を使い 再現可能な記録を作成 します。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。CURRENT を読み対象 TCB09 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 対象名TCB09を指定してIP STATUS CPUを実行する。応答中のCURRENTと時刻を保存する。IP SUMMARY FORMAT ASID(X09)で周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. IP SUMMARY FORMAT ASID(X09)が成功したためIP STATUS CPUのCURRENTも正常だと推定する。主出力は保存しない。</li><li>C. IP STATUS CPUを対象名なしで実行する。一覧の先頭行をTCB09の結果として記録する。</li><li>D. 前回保存したIP STATUS CPUの結果を使う。今回のIP SUMMARY FORMAT ASID(X09)の結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用操作の理由: AはCPU状態で CURRENT を読みTCB/SRB ADDRESSとWAITの主値として再現可能な記録を作成しTCB09に残します。
製品内の仕組み: 引継ぎ記録ではTCBサマリーを補助操作としTCBとSRBの次担当者が追跡できる証跡をTCBと対象TCB09で照合します。
選択肢別の説明: CPU状態とTCBサマリーの役割を分けるとA: CURRENTと時刻を保存する点で現在値を示します、B: 補助操作の成功ではCURRENTを確定できない点で引継ぎ記録に合いません、C: 先頭行はTCB09と確定できない点でCPU状態を代替しません、D: 採取時刻が異なる点でTCB/SRB管理に使いません。結論として引継ぎ記録の管理で判定する対象は TCB09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB09へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCB/SRB管理 TCBとSRB 引継ぎ記録 TCB09</strong></p><p>検証目的: TCB/SRB管理のTCBとSRBについて再現可能な記録を作成し、TCB09のTCB/SRB ADDRESSとWAITを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TCB09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB09のCPU状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP STATUS CPU
→ Enter を押す
［画面・出力］
CPU 0000 CURRENT ASID 0009 TCB 008F21A0 PSW 078D1000
画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X09)を指定し、TCB09のTCBサマリーを表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SUMMARY FORMAT ASID(X09)
→ Enter を押す
［画面・出力］
TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X09)を指定し、TCB09のSRB情報を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP VERBX SRMDATA ASID(X09)
→ Enter を押す
［画面・出力］
SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CURRENT が画面・出力に表示されること
② ステップ2 の F21A0 が画面・出力に表示されること
③ ステップ3 の AF1100 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0205"><h3>TCB/SRB管理 TCBとSRB 復旧後の確認 TCB06</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 上級</p><p>復旧後の確認では TCB/SRB管理 の CPU状態 を主操作として TCB06 を判定します。再発していないことを示す値への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB06 に残します。復旧後の確認を補助する TCBサマリー では TCB を補助値として TCB06 へ保存します。主判定の復旧後の確認では管理の CPU状態 から CURRENT を読み TCB06 へ残します。証跡照合の復旧後の確認では管理の CURRENT と TCB を TCB06 に保存します。記録対応の復旧後の確認では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB06 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で TCB/SRB管理 の CPU状態 と TCBサマリー を照合し 再発していないことを示す値 を確かめます。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。CURRENT を読む前に対象 TCB06 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. GRS資源直列化のSYSTEMとMODEを確認する。その値をTCB/SRB管理のTCB06にも適用する。</li><li>B. IP STATUS CPUでCURRENTを取得してからIP VERBX SRMDATA ASID(X06)でSRBを照合する。TCB06のTCB/SRB ADDRESSとWAITを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. IP SUMMARY FORMAT ASID(X06)が成功したためIP STATUS CPUのCURRENTも正常だと推定する。主出力は保存しない。別資源で得た状態を対象TCB06へ引き継げるものとする。</li><li>D. IP STATUS CPUを対象名なしで実行する。一覧の先頭行をTCB06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答内容: BはCPU状態で CURRENT を読みTCB/SRB ADDRESSとWAITの主値として復旧後の安定性を確認しTCB06に残します。
構成上の背景: 復旧後の確認ではTCBサマリーを補助操作としTCBとSRBの再発していないことを示す値をTCBと対象TCB06で照合します。
候補ごとの理由: CPU状態とTCBサマリーの役割を分けるとA: GRS資源直列化の値ではCURRENTを確認できない点でTCBサマリーの範囲を越えます、B: CURRENTとSRBを順に照合する点で現在値を示します、C: 補助操作の成功ではCURRENTを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はTCB06と確定できない点でCPU状態を代替しません。結論として復旧後の確認の管理で判定する対象は TCB06 です。
初出用語: 復旧後の確認で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB06へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCB/SRB管理 TCBとSRB 復旧後の確認 TCB06</strong></p><p>検証目的: TCB/SRB管理のTCBとSRBについて復旧後の安定性を確認し、TCB06のTCB/SRB ADDRESSとWAITを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TCB06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB06のCPU状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP STATUS CPU
→ Enter を押す
［画面・出力］
CPU 0000 CURRENT ASID 0006 TCB 008F21A0 PSW 078D1000
画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X06)を指定し、TCB06のTCBサマリーを表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SUMMARY FORMAT ASID(X06)
→ Enter を押す
［画面・出力］
TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X06)を指定し、TCB06のSRB情報を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP VERBX SRMDATA ASID(X06)
→ Enter を押す
［画面・出力］
SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CURRENT が画面・出力に表示されること
② ステップ2 の F21A0 が画面・出力に表示されること
③ ステップ3 の AF1100 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0206"><h3>TCB/SRB管理 TCBとSRB 復旧準備 TCB05</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 上級</p><p>復旧準備では TCB/SRB管理 の SRB情報 を主操作として TCB05 を判定します。再開前に必要な整合性への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB05 に残します。復旧準備を補助する CPU状態 では CURRENT を補助値として TCB05 へ保存します。主判定の復旧準備では管理の SRB情報 から SRB を読み TCB05 へ残します。証跡照合の復旧準備では管理の SRB と CURRENT を TCB05 に保存します。記録対応の復旧準備では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB05 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で TCB/SRB管理 の SRB情報 と CPU状態 を用い 復旧条件を確認 します。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。SRB で対象 TCB05 の TCB/SRB ADDRESSとWAIT を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずIP VERBX SRMDATA ASID(X05)を実行する。SRBを保存する。差分はIP STATUS CPUの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したIP VERBX SRMDATA ASID(X05)の結果を使う。今回のIP STATUS CPUの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのTCB05の出力を再利用する。今回のIP VERBX SRMDATA ASID(X05)とIP STATUS CPUは実行済みとして扱う。</li><li>D. IP STATUS CPUのCURRENTをTCB/SRB ADDRESSとWAITの主判定に採用する。IP VERBX SRMDATA ASID(X05)の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 選定理由: AはSRB情報で SRB を読みTCB/SRB ADDRESSとWAITの主値として復旧条件を確認しTCB05に残します。
処理の仕組み: 復旧準備ではCPU状態を補助操作としTCBとSRBの再開前に必要な整合性をCURRENTと対象TCB05で照合します。
選択結果の内訳: SRB情報とCPU状態の役割を分けるとA: 変更前のSRBを保存する点でSRB情報に合います、B: 採取時刻が異なる点でTCB/SRB管理に使いません、C: 過去出力では今回の復旧準備を示せない点でTCBとSRBに使えません、D: CURRENTはSRBを代替しないうえに追加前提も不正な点でTCB05を採用できません。結論として復旧準備の管理で判定する対象は TCB05 です。
用語の説明: 復旧準備で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB05へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCB/SRB管理 TCBとSRB 復旧準備 TCB05</strong></p><p>検証目的: TCB/SRB管理のTCBとSRBについて復旧条件を確認し、TCB05のTCB/SRB ADDRESSとWAITを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TCB05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X05)を指定し、TCB05のSRB情報を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP VERBX SRMDATA ASID(X05)
→ Enter を押す
［画面・出力］
SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB05のCPU状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP STATUS CPU
→ Enter を押す
［画面・出力］
CPU 0000 CURRENT ASID 0005 TCB 008F21A0 PSW 078D1000
画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X05)を指定し、TCB05のTCBサマリーを表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SUMMARY FORMAT ASID(X05)
→ Enter を押す
［画面・出力］
TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の AF1100 が画面・出力に表示されること
② ステップ2 の CURRENT が画面・出力に表示されること
③ ステップ3 の F21A0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0207"><h3>TCB/SRB管理 TCBとSRB 構成監査 TCB08</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 上級</p><p>構成監査では TCB/SRB管理 の SRB情報 を主操作として TCB08 を判定します。定義値と稼働値の一致への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB08 に残します。構成監査を補助する CPU状態 では CURRENT を補助値として TCB08 へ保存します。主判定の構成監査では管理の SRB情報 から SRB を読み TCB08 へ残します。証跡照合の構成監査では管理の SRB と CURRENT を TCB08 に保存します。記録対応の構成監査では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB08 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で TCB/SRB管理 の SRB情報 と CPU状態 の役割を分け 定義値と稼働値の一致 を調べます。TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックです。SRB時間をアプリケーションTCB時間として評価する危険があります。対象 TCB08 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのTCB08の出力を再利用する。今回のIP VERBX SRMDATA ASID(X08)とIP STATUS CPUは実行済みとして扱う。</li><li>B. IP STATUS CPUのCURRENTをTCB/SRB ADDRESSとWAITの主判定に採用する。IP VERBX SRMDATA ASID(X08)の応答は採取対象から外す。</li><li>C. IP SUMMARY FORMAT ASID(X08)のTCBをSRBと同義の成功表示として扱う。IP VERBX SRMDATA ASID(X08)は実行しない。</li><li>D. IP STATUS CPUの結果だけでは確定しない。IP VERBX SRMDATA ASID(X08)のSRBを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 技術上の正答: DはSRB情報で SRB を読みTCB/SRB ADDRESSとWAITの主値として構成差分を監査しTCB08に残します。
実行時の背景: 構成監査ではCPU状態を補助操作としTCBとSRBの定義値と稼働値の一致をCURRENTと対象TCB08で照合します。
四つの候補の理由: SRB情報とCPU状態の役割を分けるとA: 過去出力では今回の構成監査を示せない点でTCB/SRB管理に使いません、B: CURRENTはSRBを代替しない点でTCBとSRBに使えません、C: TCBとSRBは確認項目が異なる点でTCB08を採用できません、D: SRBを主証跡として区別する点で主証跡になります。結論として構成監査の管理で判定する対象は TCB08 です。
初出語定義: 構成監査で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB08へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCB/SRB管理 TCBとSRB 構成監査 TCB08</strong></p><p>検証目的: TCB/SRB管理のTCBとSRBについて構成差分を監査し、TCB08のTCB/SRB ADDRESSとWAITを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TCB08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X08)を指定し、TCB08のSRB情報を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP VERBX SRMDATA ASID(X08)
→ Enter を押す
［画面・出力］
SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB08のCPU状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP STATUS CPU
→ Enter を押す
［画面・出力］
CPU 0000 CURRENT ASID 0008 TCB 008F21A0 PSW 078D1000
画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X08)を指定し、TCB08のTCBサマリーを表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SUMMARY FORMAT ASID(X08)
→ Enter を押す
［画面・出力］
TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の AF1100 が画面・出力に表示されること
② ステップ2 の CURRENT が画面・出力に表示されること
③ ステップ3 の F21A0 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0208"><h3>TCB/SRB管理 TCBとSRB 通常状態の確認 TCB01</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 上級</p><p>通常状態の確認では TCB/SRB管理 の TCBサマリー を主操作として TCB01 を判定します。基準値と現在値の差への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB01 に残します。通常状態の確認を補助する SRB情報 では SRB を補助値として TCB01 へ保存します。主判定の通常状態の確認では管理の TCBサマリー から TCB を読み TCB01 へ残します。証跡照合の通常状態の確認では管理の TCB と SRB を TCB01 に保存します。記録対応の通常状態の確認では管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB01 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で TCB/SRB管理 の TCBサマリー と SRB情報 を組み合わせる際は TCBとSRB がタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックという仕組みを前提にします。SRB時間をアプリケーションTCB時間として評価する危険があります。TCB と TCB/SRB ADDRESSとWAIT を対象 TCB01 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. IP SUMMARY FORMAT ASID(X01)を先に実行する。対象TCB01のTCBをTCB/SRB ADDRESSとWAITとして記録する。続いてIP VERBX SRMDATA ASID(X01)で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. IP VERBX SRMDATA ASID(X01)のSRBをTCB/SRB ADDRESSとWAITの主判定に採用する。IP SUMMARY FORMAT ASID(X01)の応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. IP STATUS CPUのCURRENTをTCBと同義の成功表示として扱う。IP SUMMARY FORMAT ASID(X01)は実行しない。</li><li>D. IP SUMMARY FORMAT ASID(X01)が応答を返した時点で正常とする。応答中のTCBの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正解の説明: AはTCBサマリーで TCB を読みTCB/SRB ADDRESSとWAITの主値として通常状態を確定しTCB01に残します。
背景・仕組み: 通常状態の確認ではSRB情報を補助操作としTCBとSRBの基準値と現在値の差をSRBと対象TCB01で照合します。
選択肢の理由: TCBサマリーとSRB情報の役割を分けるとA: TCBを主値として補助結果と照合する点で正答です、B: SRBはTCBを代替しないうえに追加前提も不正な点でTCB01を採用できません、C: CURRENTとTCBは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではTCB/SRB ADDRESSとWAITを判定できない点で一次資料と一致しません。結論として通常状態の確認の管理で判定する対象は TCB01 です。
用語の初出定義: 通常状態の確認で使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB01へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCB/SRB管理 TCBとSRB 通常状態の確認 TCB01</strong></p><p>検証目的: TCB/SRB管理のTCBとSRBについて通常状態を確定し、TCB01のTCB/SRB ADDRESSとWAITを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TCB01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X01)を指定し、TCB01のTCBサマリーを表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SUMMARY FORMAT ASID(X01)
→ Enter を押す
［画面・出力］
TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X01)を指定し、TCB01のSRB情報を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP VERBX SRMDATA ASID(X01)
→ Enter を押す
［画面・出力］
SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB01のCPU状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP STATUS CPU
→ Enter を押す
［画面・出力］
CPU 0000 CURRENT ASID 0001 TCB 008F21A0 PSW 078D1000
画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の F21A0 が画面・出力に表示されること
② ステップ2 の AF1100 が画面・出力に表示されること
③ ステップ3 の CURRENT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0209"><h3>TCB/SRB管理 TCBとSRB 障害切り分け TCB04</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 上級</p><p>障害切り分けでは TCB/SRB管理 の TCBサマリー を主操作として TCB04 を判定します。最初に失敗した処理への注意として「SRB時間をアプリケーションTCB時間として評価する危険があります」を TCB04 に残します。障害切り分けを補助する SRB情報 では SRB を補助値として TCB04 へ保存します。主判定の障害切り分けでは管理の TCBサマリー から TCB を読み TCB04 へ残します。証跡照合の障害切り分けでは管理の TCB と SRB を TCB04 に保存します。記録対応の障害切り分けでは管理の TCB/SRB ADDRESSとWAIT の証跡へ TCB04 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで TCB/SRB管理 の TCBサマリー と SRB情報 を実施し TCBとSRB の役割を確認します。SRB時間をアプリケーションTCB時間として評価する危険があります。対象 TCB04 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. IP STATUS CPUのCURRENTをTCBと同義の成功表示として扱う。IP SUMMARY FORMAT ASID(X04)は実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. IP SUMMARY FORMAT ASID(X04)が応答を返した時点で正常とする。応答中のTCBの値は記録しない。</li><li>C. IP SUMMARY FORMAT ASID(X04)のコマンド文字列だけを記録する。TCBを含む応答行は保存しない。</li><li>D. IP SUMMARY FORMAT ASID(X04)の出力でTCB04とTCBが同じ応答にあることを確認する。TCB/SRB ADDRESSとWAITをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい操作の説明: DはTCBサマリーで TCB を読みTCB/SRB ADDRESSとWAITの主値として障害範囲を限定しTCB04に残します。
技術的背景: 障害切り分けではSRB情報を補助操作としTCBとSRBの最初に失敗した処理をSRBと対象TCB04で照合します。
四択の評価: TCBサマリーとSRB情報の役割を分けるとA: CURRENTとTCBは確認項目が異なるうえに追加前提も不正な点でTCB04を採用できません、B: 応答の有無だけではTCB/SRB ADDRESSとWAITを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではTCB/SRB ADDRESSとWAITを証明できない点で一次資料と一致しません、D: TCB04とTCBを同じ応答で結ぶ点でTCB04を判定できます。結論として障害切り分けの管理で判定する対象は TCB04 です。
初出語の意味: 障害切り分けで使う TCBとSRB はタスク処理とシステム要求ブロックを区別し、ディスパッチ、待ち、CPU使用を追跡する制御ブロックを表しTCB/SRB ADDRESSとWAITを判定する際にTCB04へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCB/SRB管理 TCBとSRB 障害切り分け TCB04</strong></p><p>検証目的: TCB/SRB管理のTCBとSRBについて障害範囲を限定し、TCB04のTCB/SRB ADDRESSとWAITを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TCB04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP SUMMARY FORMAT ASID(X04)を指定し、TCB04のTCBサマリーを表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SUMMARY FORMAT ASID(X04)
→ Enter を押す
［画面・出力］
TCB 008F21A0 RB 00AF1100 WAIT ECB 7F000000
画面・出力にあるF21A0を読み、TCB/SRB ADDRESSとWAITと対象TCB04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP VERBX SRMDATA ASID(X04)を指定し、TCB04のSRB情報を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP VERBX SRMDATA ASID(X04)
→ Enter を押す
［画面・出力］
SRB 00AF1100 SERVICE CLASS SYSSTC CPU TIME 00:00:01.25
画面・出力にあるAF1100を読み、TCB/SRB ADDRESSとWAITと対象TCB04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのTCB/SRB管理を確認する入力画面です。COMMAND入力口へIP STATUS CPUを指定し、TCB04のCPU状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP STATUS CPU
→ Enter を押す
［画面・出力］
CPU 0000 CURRENT ASID 0004 TCB 008F21A0 PSW 078D1000
画面・出力にあるCURRENTを読み、TCB/SRB ADDRESSとWAITと対象TCB04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の F21A0 が画面・出力に表示されること
② ステップ2 の AF1100 が画面・出力に表示されること
③ ステップ3 の CURRENT が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0210"><h3>コンポーネントトレース ログ確認 運用確認044</h3><p class="kb-meta">分類: TCB/SRB管理 ・ 難易度: 中級</p><p>第四十四観点 z/OS System Programming の TCB/SRB管理 では コンポーネントトレース を障害調査で照合します（第四十四観点）。第四十四観点 資料上は 指定コンポーネントの内部事象を記録し、障害調査に使うトレース機構として扱います（第四十四観点）。第四十四観点 ISGLOCK を起点に表示値を戻し、資源競合時の保有者確認を点検します（第四十四観点）。第四十四観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録044へ書きます（第四十四観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第四十四証跡です。z/OS System Programming の TCB/SRB管理 で切分けを行います。確認観点は TRACE、ログ確認、運用確認 です。メッセージID、定義メンバー、表示出力を同じ確認票に置く対応として適切なものはどれか。</p><ul class="kb-choices"><li>A. SVC処理 の一般メモを採り、ISGLOCK、メッセージID、時刻の対応を記録外に置き、zOSSP誤記044として調査範囲を狭める。</li><li>B. SWITCH SMF後のSMF切替記録 と ISGLOCK を同一票へ記録し、TRACE を zOSSP正044で確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. コンポーネントトレース の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延044として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在044として残す。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第四十四観点 照合結果: Bは ISGLOCK をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第四十四観点）。第四十四観点 操作背景: WTOとWTORはオペレーター通知と応答をコンソールログへ残します（第四十四観点）。第四十四観点 誤答確認: Aは ISGLOCK 未追跡、Cはコマンド確認不足、Dは別システム混同が理由です（第四十四観点）。第四十四観点 用語補足: ENQは資源を直列化します（第四十四観点）。第四十四観点 DEQは取得した資源を解放します（第四十四観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コンポーネントトレース ログ確認 運用確認044</strong></p><p>検証目的: コンポーネントトレース の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SMF</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により コンポーネントトレース の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D SMF,O
→ Enter を押す
［画面・出力］
IEE974I 11.01.20 SMF DATA SET STATUS
NAME       VOLSER  STATUS
SMF.MAN1   SMS001  ACTIVE
SMF.MAN2   SMS002  EMPTY
画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により コンポーネントトレース の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SWITCH SMF
→ Enter を押す
［画面・出力］
IEE362A SMF ENTER DUMP FOR DATA SET SMF.MAN1
IEE360I SMF NOW RECORDING ON SMF.MAN2
画面・出力には IEE360I が含まれる。IEE360I を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により コンポーネントトレース の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
JES2 SDSF ST
COMMAND ===&gt; S IFASMFD20
→ Enter を押す
［画面・出力］
IEF403I IFASMFD20 - STARTED
IFASMFDP SYSPRINT
INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、資源競合時の保有者確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


## WTOR応答管理


<section class="kb-item" id="c38-i0211"><h3>LOGRECバッファ 権限確認 運用確認092</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 上級</p><p>第九十二観点 z/OS System Programming の WTOR応答管理 では LOGRECバッファ を障害調査で照合します（第九十二観点）。第九十二観点 資料上は エラー記録を保持し、IPCSやEREPの診断対象になる記録領域として扱います（第九十二観点）。第九十二観点 ASID=0010 を起点に表示値を戻し、許可ライブラリーの誤登録防止を点検します（第九十二観点）。第九十二観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録092へ書きます（第九十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第九十二証跡です。LOGRECバッファ に関する設定変更を扱います。確認観点は LOGRECバッファ、権限確認、運用確認 です。メッセージID、定義メンバー、表示出力を同じ確認票に置く対応として適切なものはどれか。</p><ul class="kb-choices"><li>A. LOGREC診断 の一般メモを採り、ASID=0010、メッセージID、時刻の対応を記録外に置き、zOSSP誤記092として調査範囲を狭める。</li><li>B. DISPLAY GRS のISG343I表示 と ASID=0010 を同一票へ記録し、LOGRECバッファ を zOSSP正092で確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. LOGRECバッファ の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延092として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在092として残す。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 第九十二観点 照合結果: Bは ASID=0010 をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第九十二観点）。第九十二観点 操作背景: WTOとWTORはオペレーター通知と応答をコンソールログへ残します（第九十二観点）。第九十二観点 誤答確認: Aは ASID=0010 未追跡、Cはコマンド確認不足、Dは別システム混同が理由です（第九十二観点）。第九十二観点 用語補足: ENQは資源を直列化します（第九十二観点）。第九十二観点 DEQは取得した資源を解放します（第九十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LOGRECバッファ 権限確認 運用確認092</strong></p><p>検証目的: LOGRECバッファ の 権限確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SMF</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により LOGRECバッファ の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D SMF,O
→ Enter を押す
［画面・出力］
IEE974I 11.01.20 SMF DATA SET STATUS
NAME       VOLSER  STATUS
SMF.MAN1   SMS001  ACTIVE
SMF.MAN2   SMS002  EMPTY
画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により LOGRECバッファ の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SWITCH SMF
→ Enter を押す
［画面・出力］
IEE362A SMF ENTER DUMP FOR DATA SET SMF.MAN1
IEE360I SMF NOW RECORDING ON SMF.MAN2
画面・出力には IEE360I が含まれる。IEE360I を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により LOGRECバッファ の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
JES2 SDSF ST
COMMAND ===&gt; S IFASMFD20
→ Enter を押す
［画面・出力］
IEF403I IFASMFD20 - STARTED
IFASMFDP SYSPRINT
INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0212"><h3>SMFPRMxx 優先順位確認 運用確認059</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>第五十九観点 WTOR応答管理 の運用では SMFPRMxx を表示、定義、証跡で確認します（第五十九観点）。第五十九観点 役割は SMF記録対象、バッファ、データセット、ログストリーム動作を定義するという範囲です（第五十九観点）。第五十九観点 D PROG,APF のCSV450I表示 の値を SYS1.PARMLIB(SMFSP) と合わせ、実行単位の優先順位確認を記録します（第五十九観点）。第五十九観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録059に残します（第五十九観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFPRMxx 優先順位確認 運用確認059</strong></p><p>検証目的: SMFPRMxx の 優先順位確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / GRS</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SMFPRMxx の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS
→ Enter を押す
［画面・出力］
ISG343I 10.27.11 GRS STATUS 878
SYSTEM    STATE               SYSTEM    STATE
SC65      CONNECTED           SC63      CONNECTED
GRS STAR MODE INFORMATION
画面・出力には ISG343I が含まれる。ISG343I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SMFPRMxx の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS,RNL=INCL
→ Enter を押す
［画面・出力］
ISG343I 10.28.11 GRS STATUS 888
RNL=INCL
QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SMFPRMxx の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D XCF,STR,STRNAME=ISGLOCK
→ Enter を押す
［画面・出力］
IXC360I 10.29.11 DISPLAY XCF 898
STRUCTURE NAME: ISGLOCK
STATUS: ALLOCATED IN CFRM POLICY
画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0213"><h3>SWITCH SMF 優先順位確認 運用確認009</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 初級</p><p>第九観点 WTOR応答管理 で SWITCH SMF は 優先順位確認 の対象です（第九観点）。第九観点 確認時には SMF記録先の切替とバッファ書き出しを行い、ダンプ出口へ制御を渡す操という性質を前提にします（第九観点）。第九観点 D PROG,APF のCSV450I表示 と DUMPIN を同じ証跡に置き、実行単位の優先順位確認を管理します（第九観点）。第九観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録009から再現します（第九観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SWITCH SMF 優先順位確認 運用確認009</strong></p><p>検証目的: SWITCH SMF の 優先順位確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SDSF LOG</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SWITCH SMF の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 05.18.09 PROG,APF DISPLAY 908
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   2  MPRES1 SYS1.SVCLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SWITCH SMF の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SETPROG APF,ADD,DSNAME=MYPROG.LOADLIB,VOLUME=MPRES3
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
画面・出力には CSV410I が含まれる。CSV410I を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SWITCH SMF の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF,ENTRY=(1-5)
→ Enter を押す
［画面・出力］
CSV450I 05.26.09 PROG,APF DISPLAY 958
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   5  MPRES1 ISF.SISFLPA
画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、実行単位の優先順位確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0214"><h3>VERBX LOGDATA 権限確認 運用確認042</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>第四十二観点 VERBX LOGDATA は z/OS System Programming の WTOR応答管理 で扱う管理項目です（第四十二観点）。第四十二観点 ダンプ内のLOGREC記録を整形し、EREP形式で確認するIPCS処という説明を操作結果と照合します（第四十二観点）。第四十二観点 SYS1.SVCLIB、DISPLAY GRS のISG343I表示、定義メンバーを照合し、許可ライブラリーの誤登録防止を確認します（第四十二観点）。第四十二観点 証跡には資料IDと確認値を併記し、zOSSP記録042として保存します（第四十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第四十二証跡です。VERBX LOGDATA に関する設定変更を扱います。確認観点は VERBX LOGDATA、権限確認、運用確認 です。許可ライブラリーの誤登録防止を満たす記録方法として、表示値と定義を結ぶものはどれか。</p><ul class="kb-choices"><li>A. WTOメッセージ の一般メモを採り、SYS1.SVCLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記042として調査範囲を狭める。</li><li>B. VERBX LOGDATA の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延042として扱う。</li><li>C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在042として残す。</li><li>D. DISPLAY GRS のISG343I表示 と SYS1.SVCLIB を同一票へ記録し、VERBX LOGDATA を zOSSP正042で確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第四十二観点 正答根拠: Dは DISPLAY GRS のISG343I表示 と SYS1.SVCLIB を結び付けるため、対象システムの取り違えを防げます（第四十二観点）。第四十二観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第四十二観点）。第四十二観点 誤答点検: Aはシステム名欠落、Bは定義未確認、Cは時刻差の欠落が理由です（第四十二観点）。第四十二観点 初出定義: PSWは実行状態を示す語です（第四十二観点）。第四十二観点 SVCは監視プログラム呼出しです（第四十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>VERBX LOGDATA 権限確認 運用確認042</strong></p><p>検証目的: VERBX LOGDATA の 権限確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / parmlib review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により VERBX LOGDATA の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(PROGSP)
→ Enter を押す
［画面・出力］
APF FORMAT(DYNAMIC)
APF ADD DSNAME(MYPROG.LOADLIB) VOLUME(MPRES3)
LPA ADD MODNAME(MOD18) DSNAME(SYS1.LPALIB)
画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により VERBX LOGDATA の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SET PROG=SP
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE252I が含まれる。IEE252I を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により VERBX LOGDATA の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 06.10.18 PROG,APF DISPLAY 841
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
  12  MPRES3 MYPROG.LOADLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、許可ライブラリーの誤登録防止のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0215"><h3>WTOR応答管理 未応答WTOR ログとの照合 WTOR07</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>ログとの照合では WTOR応答管理 の 未応答一覧 を主操作として WTOR07 を判定します。時刻と対象識別子への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR07 に残します。ログとの照合を補助する 発行元確認 では IEE115I を補助値として WTOR07 へ保存します。主判定のログとの照合では応答管理・未応答の 未応答一覧 から IEE112I を読み WTOR07 へ残します。証跡照合のログとの照合では応答管理・未応答の IEE112I と IEE115I を WTOR07 に保存します。記録対応のログとの照合では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR07 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で WTOR応答管理 の 未応答一覧 と 発行元確認 を組み合わせる際は 未応答WTOR が応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能という仕組みを前提にします。別WTORへ応答すると停止や再試行の対象を誤ります。IEE112I と REPLY IDと発行ジョブ を対象 WTOR07 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. IEE112Iを含む未応答一覧の応答行を保存する。その応答を得るためD R,Lを使用する。対象WTOR07のREPLY IDと発行ジョブとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. D R,Lが応答を返した時点で正常とする。応答中のIEE112Iの値は記録しない。IEE600IをIEE112Iと同じ判定値とみなし対象WTOR07の主証跡にする。</li><li>C. D R,Lのコマンド文字列だけを記録する。IEE112Iを含む応答行は保存しない。</li><li>D. 未応答WTORの停止または再定義を実施する。その後にD R,LでIEE112Iを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: Aは未応答一覧で IEE112I を読みREPLY IDと発行ジョブの主値として操作とログを対応しWTOR07に残します。
機能の仕組み: ログとの照合では発行元確認を補助操作とし未応答WTORの時刻と対象識別子をIEE115Iと対象WTOR07で照合します。
各候補の評価: 未応答一覧と発行元確認の役割を分けるとA: IEE112Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではREPLY IDと発行ジョブを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではREPLY IDと発行ジョブを証明できない点でREPLY IDと発行ジョブを確認できません、D: 変更前のREPLY IDと発行ジョブを失う点で発行元確認の範囲を越えます。結論としてログとの照合の応答管理・未応答で判定する対象は WTOR07 です。
用語の定義: ログとの照合で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR07へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOR応答管理 未応答WTOR ログとの照合 WTOR07</strong></p><p>検証目的: WTOR応答管理の未応答WTORについて操作とログを対応し、WTOR07のREPLY IDと発行ジョブを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR07の未応答一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D R,L
→ Enter を押す
［画面・出力］
IEE112I 12.20.10 DISPLAY R 123
001 R SYS1,REPLY U OR C
002 R JOB07,MOUNT VOLUME
画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB07を指定し、WTOR07の発行元確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB07
→ Enter を押す
［画面・出力］
IEE115I JOB07 ACTIVE ON SYSA ASID=0007
画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR07の応答記録を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND REPLY
→ Enter を押す
［画面・出力］
IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE112I が画面・出力に表示されること
② ステップ2 の IEE115I が画面・出力に表示されること
③ ステップ3 の IEE600I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0216"><h3>WTOR応答管理 未応答WTOR 代替経路の確認 WTOR10</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>代替経路の確認では WTOR応答管理 の 未応答一覧 を主操作として WTOR10 を判定します。主経路との役割差への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR10 に残します。代替経路の確認を補助する 発行元確認 では IEE115I を補助値として WTOR10 へ保存します。主判定の代替経路の確認では応答管理・未応答の 未応答一覧 から IEE112I を読み WTOR10 へ残します。証跡照合の代替経路の確認では応答管理・未応答の IEE112I と IEE115I を WTOR10 に保存します。記録対応の代替経路の確認では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR10 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で WTOR応答管理 の 未応答一覧 と 発行元確認 を実施し 未応答WTOR の役割を確認します。別WTORへ応答すると停止や再試行の対象を誤ります。対象 WTOR10 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. D R,Lのコマンド文字列だけを記録する。IEE112Iを含む応答行は保存しない。</li><li>B. 未応答WTORの停止または再定義を実施する。その後にD R,LでIEE112Iを採取する。</li><li>C. APF管理のDSNAMEとVOLSERを確認する。その値をWTOR応答管理のWTOR10にも適用する。</li><li>D. D R,LとD A,JOB10の対象名をそろえる。前者のIEE112IをREPLY IDと発行ジョブの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: Dは未応答一覧で IEE112I を読みREPLY IDと発行ジョブの主値として代替手段の成立を確認しWTOR10に残します。
運用上の背景: 代替経路の確認では発行元確認を補助操作とし未応答WTORの主経路との役割差をIEE115Iと対象WTOR10で照合します。
候補別の検討: 未応答一覧と発行元確認の役割を分けるとA: 入力記録だけではREPLY IDと発行ジョブを証明できない点で一次資料と一致しません、B: 変更前のREPLY IDと発行ジョブを失う点でREPLY IDと発行ジョブを確認できません、C: APF管理の値ではIEE112Iを確認できない点で発行元確認の範囲を越えます、D: 同じ対象名のIEE112Iを採用する点で現在値を示します。結論として代替経路の確認の応答管理・未応答で判定する対象は WTOR10 です。
重要用語の定義: 代替経路の確認で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR10へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOR応答管理 未応答WTOR 代替経路の確認 WTOR10</strong></p><p>検証目的: WTOR応答管理の未応答WTORについて代替手段の成立を確認し、WTOR10のREPLY IDと発行ジョブを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR10の未応答一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D R,L
→ Enter を押す
［画面・出力］
IEE112I 12.20.10 DISPLAY R 123
001 R SYS1,REPLY U OR C
002 R JOB10,MOUNT VOLUME
画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB10を指定し、WTOR10の発行元確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB10
→ Enter を押す
［画面・出力］
IEE115I JOB10 ACTIVE ON SYSA ASID=0010
画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR10の応答記録を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND REPLY
→ Enter を押す
［画面・出力］
IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE112I が画面・出力に表示されること
② ステップ2 の IEE115I が画面・出力に表示されること
③ ステップ3 の IEE600I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0217"><h3>WTOR応答管理 未応答WTOR 変更前の確認 WTOR02</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>変更前の確認では WTOR応答管理 の 発行元確認 を主操作として WTOR02 を判定します。変更対象と非対象の境界への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR02 に残します。変更前の確認を補助する 応答記録 では IEE600I を補助値として WTOR02 へ保存します。主判定の変更前の確認では応答管理・未応答の 発行元確認 から IEE115I を読み WTOR02 へ残します。証跡照合の変更前の確認では応答管理・未応答の IEE115I と IEE600I を WTOR02 に保存します。記録対応の変更前の確認では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR02 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で WTOR応答管理 の 発行元確認 と 応答記録 の役割を分け 変更対象と非対象の境界 を調べます。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。対象 WTOR02 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. D A,JOB02を対象名なしで実行する。一覧の先頭行をWTOR02の結果として記録する。</li><li>B. 前回保存したD A,JOB02の結果を使う。今回のSDSF LOG FIND REPLYの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのWTOR02の出力を再利用する。今回のD A,JOB02とSDSF LOG FIND REPLYは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象WTOR02についてD A,JOB02の応答からIEE115Iを確認する。SDSF LOG FIND REPLYは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Dは発行元確認で IEE115I を読みREPLY IDと発行ジョブの主値として変更前の証跡を保存しWTOR02に残します。
動作の背景: 変更前の確認では応答記録を補助操作とし未応答WTORの変更対象と非対象の境界をIEE600Iと対象WTOR02で照合します。
各選択肢の検討: 発行元確認と応答記録の役割を分けるとA: 先頭行はWTOR02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で発行元確認を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でWTOR応答管理に使いません、D: IEE115Iと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認の応答管理・未応答で判定する対象は WTOR02 です。
初出用語の定義: 変更前の確認で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR02へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOR応答管理 未応答WTOR 変更前の確認 WTOR02</strong></p><p>検証目的: WTOR応答管理の未応答WTORについて変更前の証跡を保存し、WTOR02のREPLY IDと発行ジョブを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB02を指定し、WTOR02の発行元確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB02
→ Enter を押す
［画面・出力］
IEE115I JOB02 ACTIVE ON SYSA ASID=0002
画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR02の応答記録を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND REPLY
→ Enter を押す
［画面・出力］
IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR02の未応答一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D R,L
→ Enter を押す
［画面・出力］
IEE112I 12.20.10 DISPLAY R 123
001 R SYS1,REPLY U OR C
002 R JOB02,MOUNT VOLUME
画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE115I が画面・出力に表示されること
② ステップ2 の IEE600I が画面・出力に表示されること
③ ステップ3 の IEE112I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0218"><h3>WTOR応答管理 未応答WTOR 変更後の確認 WTOR03</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>変更後の確認では WTOR応答管理 の 応答記録 を主操作として WTOR03 を判定します。反映値と残存値への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR03 に残します。変更後の確認を補助する 未応答一覧 では IEE112I を補助値として WTOR03 へ保存します。主判定の変更後の確認では応答管理・未応答の 応答記録 から IEE600I を読み WTOR03 へ残します。証跡照合の変更後の確認では応答管理・未応答の IEE600I と IEE112I を WTOR03 に保存します。記録対応の変更後の確認では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR03 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で WTOR応答管理 の 応答記録 と 未応答一覧 を使い 変更結果を検証 します。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。IEE600I を読み対象 WTOR03 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. D R,Lで周辺状態を押さえる。その後にSDSF LOG FIND REPLYでIEE600Iを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. 未応答WTORの停止または再定義を実施する。その後にSDSF LOG FIND REPLYでIEE600Iを採取する。</li><li>C. SAF連携のSAF RCとRACF RCを確認する。その値をWTOR応答管理のWTOR03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>D. D R,Lが成功したためSDSF LOG FIND REPLYのIEE600Iも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: Aは応答記録で IEE600I を読みREPLY IDと発行ジョブの主値として変更結果を検証しWTOR03に残します。
内部の仕組み: 変更後の確認では未応答一覧を補助操作とし未応答WTORの反映値と残存値をIEE112Iと対象WTOR03で照合します。
誤答を含む比較: 応答記録と未応答一覧の役割を分けるとA: 周辺状態の後にIEE600Iを確認する点でWTOR03を判定できます、B: 変更前のREPLY IDと発行ジョブを失う点で未応答一覧の範囲を越えます、C: SAF連携の値ではIEE600Iを確認できないうえに追加前提も不正な点でWTOR03の値を示しません、D: 補助操作の成功ではIEE600Iを確定できない点で変更後の確認に合いません。結論として変更後の確認の応答管理・未応答で判定する対象は WTOR03 です。
用語定義: 変更後の確認で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR03へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOR応答管理 未応答WTOR 変更後の確認 WTOR03</strong></p><p>検証目的: WTOR応答管理の未応答WTORについて変更結果を検証し、WTOR03のREPLY IDと発行ジョブを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR03の応答記録を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND REPLY
→ Enter を押す
［画面・出力］
IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR03の未応答一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D R,L
→ Enter を押す
［画面・出力］
IEE112I 12.20.10 DISPLAY R 123
001 R SYS1,REPLY U OR C
002 R JOB03,MOUNT VOLUME
画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB03を指定し、WTOR03の発行元確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB03
→ Enter を押す
［画面・出力］
IEE115I JOB03 ACTIVE ON SYSA ASID=0003
画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
② ステップ2 の IEE112I が画面・出力に表示されること
③ ステップ3 の IEE115I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0219"><h3>WTOR応答管理 未応答WTOR 引継ぎ記録 WTOR09</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>引継ぎ記録では WTOR応答管理 の 応答記録 を主操作として WTOR09 を判定します。次担当者が追跡できる証跡への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR09 に残します。引継ぎ記録を補助する 未応答一覧 では IEE112I を補助値として WTOR09 へ保存します。主判定の引継ぎ記録では応答管理・未応答の 応答記録 から IEE600I を読み WTOR09 へ残します。証跡照合の引継ぎ記録では応答管理・未応答の IEE600I と IEE112I を WTOR09 に保存します。記録対応の引継ぎ記録では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR09 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で WTOR応答管理 の 応答記録 と 未応答一覧 を使い 再現可能な記録を作成 します。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。IEE600I を読み対象 WTOR09 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. D R,Lが成功したためSDSF LOG FIND REPLYのIEE600Iも正常だと推定する。主出力は保存しない。</li><li>B. SDSF LOG FIND REPLYを対象名なしで実行する。一覧の先頭行をWTOR09の結果として記録する。</li><li>C. 対象名WTOR09を指定してSDSF LOG FIND REPLYを実行する。応答中のIEE600Iと時刻を保存する。D R,Lで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したSDSF LOG FIND REPLYの結果を使う。今回のD R,Lの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: Cは応答記録で IEE600I を読みREPLY IDと発行ジョブの主値として再現可能な記録を作成しWTOR09に残します。
製品内の仕組み: 引継ぎ記録では未応答一覧を補助操作とし未応答WTORの次担当者が追跡できる証跡をIEE112Iと対象WTOR09で照合します。
選択肢別の説明: 応答記録と未応答一覧の役割を分けるとA: 補助操作の成功ではIEE600Iを確定できない点でWTOR09の値を示しません、B: 先頭行はWTOR09と確定できない点で引継ぎ記録に合いません、C: IEE600Iと時刻を保存する点で応答記録に合います、D: 採取時刻が異なる点でWTOR応答管理に使いません。結論として引継ぎ記録の応答管理・未応答で判定する対象は WTOR09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR09へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOR応答管理 未応答WTOR 引継ぎ記録 WTOR09</strong></p><p>検証目的: WTOR応答管理の未応答WTORについて再現可能な記録を作成し、WTOR09のREPLY IDと発行ジョブを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR09の応答記録を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND REPLY
→ Enter を押す
［画面・出力］
IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR09の未応答一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D R,L
→ Enter を押す
［画面・出力］
IEE112I 12.20.10 DISPLAY R 123
001 R SYS1,REPLY U OR C
002 R JOB09,MOUNT VOLUME
画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB09を指定し、WTOR09の発行元確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB09
→ Enter を押す
［画面・出力］
IEE115I JOB09 ACTIVE ON SYSA ASID=0009
画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
② ステップ2 の IEE112I が画面・出力に表示されること
③ ステップ3 の IEE115I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0220"><h3>WTOR応答管理 未応答WTOR 復旧後の確認 WTOR06</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>復旧後の確認では WTOR応答管理 の 応答記録 を主操作として WTOR06 を判定します。再発していないことを示す値への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR06 に残します。復旧後の確認を補助する 未応答一覧 では IEE112I を補助値として WTOR06 へ保存します。主判定の復旧後の確認では応答管理・未応答の 応答記録 から IEE600I を読み WTOR06 へ残します。証跡照合の復旧後の確認では応答管理・未応答の IEE600I と IEE112I を WTOR06 に保存します。記録対応の復旧後の確認では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR06 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で WTOR応答管理 の 応答記録 と 未応答一覧 を照合し 再発していないことを示す値 を確かめます。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。IEE600I を読む前に対象 WTOR06 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. Cross MemoryのHOME ASIDとSECONDARY ASIDを確認する。その値をWTOR応答管理のWTOR06にも適用する。</li><li>B. D R,Lが成功したためSDSF LOG FIND REPLYのIEE600Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象WTOR06へ引き継げるものとする。未応答WTORの再発していないことを示す値は確認済みとして扱う。さらにD A,JOB06のIEE115IをIEE600Iと同種の値として併記する。</li><li>C. SDSF LOG FIND REPLYを対象名なしで実行する。一覧の先頭行をWTOR06の結果として記録する。</li><li>D. SDSF LOG FIND REPLYでIEE600Iを取得してからD A,JOB06でIEE115Iを照合する。WTOR06のREPLY IDと発行ジョブを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: Dは応答記録で IEE600I を読みREPLY IDと発行ジョブの主値として復旧後の安定性を確認しWTOR06に残します。
構成上の背景: 復旧後の確認では未応答一覧を補助操作とし未応答WTORの再発していないことを示す値をIEE112Iと対象WTOR06で照合します。
候補ごとの理由: 応答記録と未応答一覧の役割を分けるとA: Cross Memoryの値ではIEE600Iを確認できない点で未応答一覧の範囲を越えます、B: 補助操作の成功ではIEE600Iを確定できないうえに追加前提も不正な点でWTOR06の値を示しません、C: 先頭行はWTOR06と確定できない点で復旧後の確認に合いません、D: IEE600IとIEE115Iを順に照合する点で応答記録に合います。結論として復旧後の確認の応答管理・未応答で判定する対象は WTOR06 です。
初出用語: 復旧後の確認で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR06へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOR応答管理 未応答WTOR 復旧後の確認 WTOR06</strong></p><p>検証目的: WTOR応答管理の未応答WTORについて復旧後の安定性を確認し、WTOR06のREPLY IDと発行ジョブを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR06の応答記録を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND REPLY
→ Enter を押す
［画面・出力］
IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR06の未応答一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D R,L
→ Enter を押す
［画面・出力］
IEE112I 12.20.10 DISPLAY R 123
001 R SYS1,REPLY U OR C
002 R JOB06,MOUNT VOLUME
画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB06を指定し、WTOR06の発行元確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB06
→ Enter を押す
［画面・出力］
IEE115I JOB06 ACTIVE ON SYSA ASID=0006
画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
② ステップ2 の IEE112I が画面・出力に表示されること
③ ステップ3 の IEE115I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0221"><h3>WTOR応答管理 未応答WTOR 復旧準備 WTOR05</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>復旧準備では WTOR応答管理 の 発行元確認 を主操作として WTOR05 を判定します。再開前に必要な整合性への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR05 に残します。復旧準備を補助する 応答記録 では IEE600I を補助値として WTOR05 へ保存します。主判定の復旧準備では応答管理・未応答の 発行元確認 から IEE115I を読み WTOR05 へ残します。証跡照合の復旧準備では応答管理・未応答の IEE115I と IEE600I を WTOR05 に保存します。記録対応の復旧準備では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR05 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で WTOR応答管理 の 発行元確認 と 応答記録 を用い 復旧条件を確認 します。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。IEE115I で対象 WTOR05 の REPLY IDと発行ジョブ を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 前回保存したD A,JOB05の結果を使う。今回のSDSF LOG FIND REPLYの結果と同一時点の証跡として比較する。</li><li>B. 保存済みのWTOR05の出力を再利用する。今回のD A,JOB05とSDSF LOG FIND REPLYは実行済みとして扱う。</li><li>C. 変更を加えずD A,JOB05を実行する。IEE115Iを保存する。差分はSDSF LOG FIND REPLYの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. SDSF LOG FIND REPLYのIEE600IをREPLY IDと発行ジョブの主判定に採用する。D A,JOB05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Cは発行元確認で IEE115I を読みREPLY IDと発行ジョブの主値として復旧条件を確認しWTOR05に残します。
処理の仕組み: 復旧準備では応答記録を補助操作とし未応答WTORの再開前に必要な整合性をIEE600Iと対象WTOR05で照合します。
選択結果の内訳: 発行元確認と応答記録の役割を分けるとA: 採取時刻が異なる点で発行元確認を代替しません、B: 過去出力では今回の復旧準備を示せない点でWTOR応答管理に使いません、C: 変更前のIEE115Iを保存する点で正答です、D: IEE600IはIEE115Iを代替しないうえに追加前提も不正な点でWTOR05を採用できません。結論として復旧準備の応答管理・未応答で判定する対象は WTOR05 です。
用語の説明: 復旧準備で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR05へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOR応答管理 未応答WTOR 復旧準備 WTOR05</strong></p><p>検証目的: WTOR応答管理の未応答WTORについて復旧条件を確認し、WTOR05のREPLY IDと発行ジョブを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB05を指定し、WTOR05の発行元確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB05
→ Enter を押す
［画面・出力］
IEE115I JOB05 ACTIVE ON SYSA ASID=0005
画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR05の応答記録を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND REPLY
→ Enter を押す
［画面・出力］
IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR05の未応答一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D R,L
→ Enter を押す
［画面・出力］
IEE112I 12.20.10 DISPLAY R 123
001 R SYS1,REPLY U OR C
002 R JOB05,MOUNT VOLUME
画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE115I が画面・出力に表示されること
② ステップ2 の IEE600I が画面・出力に表示されること
③ ステップ3 の IEE112I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0222"><h3>WTOR応答管理 未応答WTOR 構成監査 WTOR08</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>構成監査では WTOR応答管理 の 発行元確認 を主操作として WTOR08 を判定します。定義値と稼働値の一致への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR08 に残します。構成監査を補助する 応答記録 では IEE600I を補助値として WTOR08 へ保存します。主判定の構成監査では応答管理・未応答の 発行元確認 から IEE115I を読み WTOR08 へ残します。証跡照合の構成監査では応答管理・未応答の IEE115I と IEE600I を WTOR08 に保存します。記録対応の構成監査では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR08 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で WTOR応答管理 の 発行元確認 と 応答記録 の役割を分け 定義値と稼働値の一致 を調べます。未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能です。別WTORへ応答すると停止や再試行の対象を誤ります。対象 WTOR08 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのWTOR08の出力を再利用する。今回のD A,JOB08とSDSF LOG FIND REPLYは実行済みとして扱う。</li><li>B. SDSF LOG FIND REPLYの結果だけでは確定しない。D A,JOB08のIEE115Iを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. SDSF LOG FIND REPLYのIEE600IをREPLY IDと発行ジョブの主判定に採用する。D A,JOB08の応答は採取対象から外す。</li><li>D. D R,LのIEE112IをIEE115Iと同義の成功表示として扱う。D A,JOB08は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Bは発行元確認で IEE115I を読みREPLY IDと発行ジョブの主値として構成差分を監査しWTOR08に残します。
実行時の背景: 構成監査では応答記録を補助操作とし未応答WTORの定義値と稼働値の一致をIEE600Iと対象WTOR08で照合します。
四つの候補の理由: 発行元確認と応答記録の役割を分けるとA: 過去出力では今回の構成監査を示せない点でWTOR応答管理に使いません、B: IEE115Iを主証跡として区別する点で正答です、C: IEE600IはIEE115Iを代替しない点でWTOR08を採用できません、D: IEE112IとIEE115Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査の応答管理・未応答で判定する対象は WTOR08 です。
初出語定義: 構成監査で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR08へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOR応答管理 未応答WTOR 構成監査 WTOR08</strong></p><p>検証目的: WTOR応答管理の未応答WTORについて構成差分を監査し、WTOR08のREPLY IDと発行ジョブを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB08を指定し、WTOR08の発行元確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB08
→ Enter を押す
［画面・出力］
IEE115I JOB08 ACTIVE ON SYSA ASID=0008
画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR08の応答記録を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND REPLY
→ Enter を押す
［画面・出力］
IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR08の未応答一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D R,L
→ Enter を押す
［画面・出力］
IEE112I 12.20.10 DISPLAY R 123
001 R SYS1,REPLY U OR C
002 R JOB08,MOUNT VOLUME
画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE115I が画面・出力に表示されること
② ステップ2 の IEE600I が画面・出力に表示されること
③ ステップ3 の IEE112I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0223"><h3>WTOR応答管理 未応答WTOR 通常状態の確認 WTOR01</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>通常状態の確認では WTOR応答管理 の 未応答一覧 を主操作として WTOR01 を判定します。基準値と現在値の差への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR01 に残します。通常状態の確認を補助する 発行元確認 では IEE115I を補助値として WTOR01 へ保存します。主判定の通常状態の確認では応答管理・未応答の 未応答一覧 から IEE112I を読み WTOR01 へ残します。証跡照合の通常状態の確認では応答管理・未応答の IEE112I と IEE115I を WTOR01 に保存します。記録対応の通常状態の確認では応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR01 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で WTOR応答管理 の 未応答一覧 と 発行元確認 を組み合わせる際は 未応答WTOR が応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能という仕組みを前提にします。別WTORへ応答すると停止や再試行の対象を誤ります。IEE112I と REPLY IDと発行ジョブ を対象 WTOR01 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. D A,JOB01のIEE115IをREPLY IDと発行ジョブの主判定に採用する。D R,Lの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. SDSF LOG FIND REPLYのIEE600IをIEE112Iと同義の成功表示として扱う。D R,Lは実行しない。</li><li>C. D R,Lを先に実行する。対象WTOR01のIEE112IをREPLY IDと発行ジョブとして記録する。続いてD A,JOB01で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. D R,Lが応答を返した時点で正常とする。応答中のIEE112Iの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Cは未応答一覧で IEE112I を読みREPLY IDと発行ジョブの主値として通常状態を確定しWTOR01に残します。
背景・仕組み: 通常状態の確認では発行元確認を補助操作とし未応答WTORの基準値と現在値の差をIEE115Iと対象WTOR01で照合します。
選択肢の理由: 未応答一覧と発行元確認の役割を分けるとA: IEE115IはIEE112Iを代替しないうえに追加前提も不正な点で未応答WTORに使えません、B: IEE600IとIEE112Iは確認項目が異なる点でWTOR01を採用できません、C: IEE112Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではREPLY IDと発行ジョブを判定できない点で一次資料と一致しません。結論として通常状態の確認の応答管理・未応答で判定する対象は WTOR01 です。
用語の初出定義: 通常状態の確認で使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR01へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOR応答管理 未応答WTOR 通常状態の確認 WTOR01</strong></p><p>検証目的: WTOR応答管理の未応答WTORについて通常状態を確定し、WTOR01のREPLY IDと発行ジョブを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR01の未応答一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D R,L
→ Enter を押す
［画面・出力］
IEE112I 12.20.10 DISPLAY R 123
001 R SYS1,REPLY U OR C
002 R JOB01,MOUNT VOLUME
画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB01を指定し、WTOR01の発行元確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB01
→ Enter を押す
［画面・出力］
IEE115I JOB01 ACTIVE ON SYSA ASID=0001
画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR01の応答記録を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND REPLY
→ Enter を押す
［画面・出力］
IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE112I が画面・出力に表示されること
② ステップ2 の IEE115I が画面・出力に表示されること
③ ステップ3 の IEE600I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0224"><h3>WTOR応答管理 未応答WTOR 障害切り分け WTOR04</h3><p class="kb-meta">分類: WTOR応答管理 ・ 難易度: 中級</p><p>障害切り分けでは WTOR応答管理 の 未応答一覧 を主操作として WTOR04 を判定します。最初に失敗した処理への注意として「別WTORへ応答すると停止や再試行の対象を誤ります」を WTOR04 に残します。障害切り分けを補助する 発行元確認 では IEE115I を補助値として WTOR04 へ保存します。主判定の障害切り分けでは応答管理・未応答の 未応答一覧 から IEE112I を読み WTOR04 へ残します。証跡照合の障害切り分けでは応答管理・未応答の IEE112I と IEE115I を WTOR04 に保存します。記録対応の障害切り分けでは応答管理・未応答の REPLY IDと発行ジョブ の証跡へ WTOR04 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで WTOR応答管理 の 未応答一覧 と 発行元確認 を実施し 未応答WTOR の役割を確認します。別WTORへ応答すると停止や再試行の対象を誤ります。対象 WTOR04 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. SDSF LOG FIND REPLYのIEE600IをIEE112Iと同義の成功表示として扱う。D R,Lは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. D R,Lの出力でWTOR04とIEE112Iが同じ応答にあることを確認する。REPLY IDと発行ジョブをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. D R,Lが応答を返した時点で正常とする。応答中のIEE112Iの値は記録しない。</li><li>D. D R,Lのコマンド文字列だけを記録する。IEE112Iを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Bは未応答一覧で IEE112I を読みREPLY IDと発行ジョブの主値として障害範囲を限定しWTOR04に残します。
技術的背景: 障害切り分けでは発行元確認を補助操作とし未応答WTORの最初に失敗した処理をIEE115Iと対象WTOR04で照合します。
四択の評価: 未応答一覧と発行元確認の役割を分けるとA: IEE600IとIEE112Iは確認項目が異なるうえに追加前提も不正な点でWTOR04を採用できません、B: WTOR04とIEE112Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではREPLY IDと発行ジョブを判定できない点で一次資料と一致しません、D: 入力記録だけではREPLY IDと発行ジョブを証明できない点でREPLY IDと発行ジョブを確認できません。結論として障害切り分けの応答管理・未応答で判定する対象は WTOR04 です。
初出語の意味: 障害切り分けで使う 未応答WTOR は応答待ちメッセージへ一意の応答番号を付け、オペレーター入力を発行元へ返すコンソール機能を表しREPLY IDと発行ジョブを判定する際にWTOR04へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOR応答管理 未応答WTOR 障害切り分け WTOR04</strong></p><p>検証目的: WTOR応答管理の未応答WTORについて障害範囲を限定し、WTOR04のREPLY IDと発行ジョブを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTOR04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD R,Lを指定し、WTOR04の未応答一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D R,L
→ Enter を押す
［画面・出力］
IEE112I 12.20.10 DISPLAY R 123
001 R SYS1,REPLY U OR C
002 R JOB04,MOUNT VOLUME
画面・出力にあるIEE112Iを読み、REPLY IDと発行ジョブと対象WTOR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へD A,JOB04を指定し、WTOR04の発行元確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB04
→ Enter を押す
［画面・出力］
IEE115I JOB04 ACTIVE ON SYSA ASID=0004
画面・出力にあるIEE115Iを読み、REPLY IDと発行ジョブと対象WTOR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOR応答管理を確認する入力画面です。COMMAND入力口へSDSF LOG FIND REPLYを指定し、WTOR04の応答記録を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND REPLY
→ Enter を押す
［画面・出力］
IEE600I REPLY 002 TEXT U ISSUED FROM CONSOLE CON1
画面・出力にあるIEE600Iを読み、REPLY IDと発行ジョブと対象WTOR04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE112I が画面・出力に表示されること
② ステップ2 の IEE115I が画面・出力に表示されること
③ ステップ3 の IEE600I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


## WTOメッセージ


<section class="kb-item" id="c38-i0225"><h3>CONSOLE表示 出口確認 運用確認075</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>第七十五観点 WTOメッセージ の運用では CONSOLE表示 を表示、定義、証跡で確認します（第七十五観点）。第七十五観点 役割は コンソールID、権限、経路コード、応答数などの運用情報を確認する表示という範囲です（第七十五観点）。第七十五観点 IFASMFDPジョブログのSYSPRINT の値を WTOR reply 005 と合わせ、共通ストレージ変更の記録を記録します（第七十五観点）。第七十五観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録075に残します（第七十五観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第七十五証跡です。IFASMFDPジョブログのSYSPRINT を採取した後の扱いを選びます。確認観点は CONSOLE表示、出口確認、運用確認 です。IFASMFDPジョブログのSYSPRINT と WTOR reply 005 を合わせて読む時の採用方針として正しいものはどれか。</p><ul class="kb-choices"><li>A. PROGxx運用 の一般メモを採り、WTOR reply 005、メッセージID、時刻の対応を記録外に置き、zOSSP誤記075として調査範囲を狭める。</li><li>B. IFASMFDPジョブログのSYSPRINT と WTOR reply 005 を同一票へ記録し、CONSOLE表示 を zOSSP正075で確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. CONSOLE表示 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延075として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在075として残す。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第七十五観点 採用理由: Bは CONSOLE表示 の状態を表示値と定義の両方から確認するため、記録として妥当です（第七十五観点）。第七十五観点 実行背景: SVC、TCB、SRB、PSWは割り込みとディスパッチの説明に使います（第七十五観点）。第七十五観点 誤答整理: Aは一般メモ偏重、Cはジョブログ除外、Dは再現性不足が理由です（第七十五観点）。第七十五観点 用語整理: SMFはシステム測定記録です（第七十五観点）。第七十五観点 IFASMFDPはSMFデータ退避に使います（第七十五観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CONSOLE表示 出口確認 運用確認075</strong></p><p>検証目的: CONSOLE表示 の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / GRS</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により CONSOLE表示 の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS
→ Enter を押す
［画面・出力］
ISG343I 10.27.03 GRS STATUS 824
SYSTEM    STATE               SYSTEM    STATE
SC65      CONNECTED           SC63      CONNECTED
GRS STAR MODE INFORMATION
画面・出力には ISG343I が含まれる。ISG343I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により CONSOLE表示 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS,RNL=INCL
→ Enter を押す
［画面・出力］
ISG343I 10.28.03 GRS STATUS 834
RNL=INCL
QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により CONSOLE表示 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D XCF,STR,STRNAME=ISGLOCK
→ Enter を押す
［画面・出力］
IXC360I 10.29.03 DISPLAY XCF 844
STRUCTURE NAME: ISGLOCK
STATUS: ALLOCATED IN CFRM POLICY
画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0226"><h3>IEFU84出口 定義照合 運用確認091</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 上級</p><p>第九十一観点 WTOメッセージ の運用では IEFU84出口 を表示、定義、証跡で確認します（第九十一観点）。第九十一観点 役割は SMFレコードの事後処理や選択に関わるインストール出口という範囲です（第九十一観点）。第九十一観点 SET PROG=xx後のIEE252I表示 の値を TRACE DISPLAY と合わせ、アドレス空間分離の確認を記録します（第九十一観点）。第九十一観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録091に残します（第九十一観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第九十一証跡です。WTOメッセージ の運用で IEFU84出口 を点検します。確認観点は IEFU84出口、定義照合、運用確認 です。TRACE DISPLAY を根拠として残す時、対象の取り違えを抑える対応はどれか。</p><ul class="kb-choices"><li>A. システム出口 の一般メモを採り、TRACE DISPLAY、メッセージID、時刻の対応を記録外に置き、zOSSP誤記091として調査範囲を狭める。</li><li>B. IEFU84出口 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延091として扱う。</li><li>C. SET PROG=xx後のIEE252I表示 と TRACE DISPLAY を同一票へ記録し、IEFU84出口 を zOSSP正091で確定する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在091として残す。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 第九十一観点 採用理由: Cは IEFU84出口 の状態を表示値と定義の両方から確認するため、記録として妥当です（第九十一観点）。第九十一観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第九十一観点）。第九十一観点 誤答整理: Aは一般メモ偏重、Bはジョブログ除外、Dは再現性不足が理由です（第九十一観点）。第九十一観点 用語確認: APFは許可ライブラリーの管理機能です（第九十一観点）。第九十一観点 PROGxxは動的なプログラム管理指定です（第九十一観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IEFU84出口 定義照合 運用確認091</strong></p><p>検証目的: IEFU84出口 の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / GRS</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IEFU84出口 の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS
→ Enter を押す
［画面・出力］
ISG343I 10.27.19 GRS STATUS 840
SYSTEM    STATE               SYSTEM    STATE
SC65      CONNECTED           SC63      CONNECTED
GRS STAR MODE INFORMATION
画面・出力には ISG343I が含まれる。ISG343I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IEFU84出口 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS,RNL=INCL
→ Enter を押す
［画面・出力］
ISG343I 10.28.19 GRS STATUS 850
RNL=INCL
QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IEFU84出口 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D XCF,STR,STRNAME=ISGLOCK
→ Enter を押す
［画面・出力］
IXC360I 10.29.19 DISPLAY XCF 860
STRUCTURE NAME: ISGLOCK
STATUS: ALLOCATED IN CFRM POLICY
画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0227"><h3>LNKAUTH指定 ストレージ確認 運用確認058</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>第五十八観点 LNKAUTH指定 は z/OS System Programming の WTOメッセージ で扱う管理項目です（第五十八観点）。第五十八観点 LNKLSTライブラリーをAPF許可とみなすかを制御するシステム指定という説明を操作結果と照合します（第五十八観点）。第五十八観点 SYS1.PARMLIB(PROGSP)、parmlibメンバーの該当ステートメント、定義メンバーを照合し、オペレーター応答漏れの防止を確認します（第五十八観点）。第五十八観点 証跡には資料IDと確認値を併記し、zOSSP記録058として保存します（第五十八観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第五十八証跡です。LNKAUTH指定 の記録を監査用に整えます。確認観点は LNKAUTH指定、ストレージ確認、運用確認 です。オペレーター応答漏れの防止のために、parmlibメンバーの該当ステートメント を使った運用記録として最も適切な扱いはどれか。</p><ul class="kb-choices"><li>A. parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を同一票へ記録し、LNKAUTH指定 を zOSSP正058で確定する。 <span class="kb-ok">✅ 正解</span></li><li>B. SMF記録 の一般メモを採り、SYS1.PARMLIB(PROGSP)、メッセージID、時刻の対応を記録外に置き、zOSSP誤記058として調査範囲を狭める。</li><li>C. LNKAUTH指定 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延058として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在058として残す。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第五十八観点 正答根拠: Aは parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を結び付けるため、対象システムの取り違えを防げます（第五十八観点）。第五十八観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第五十八観点）。第五十八観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第五十八観点）。第五十八観点 用語説明: WTOは通知メッセージです（第五十八観点）。第五十八観点 WTORは応答を求めるメッセージです（第五十八観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LNKAUTH指定 ストレージ確認 運用確認058</strong></p><p>検証目的: LNKAUTH指定 の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / parmlib review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により LNKAUTH指定 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(PROGSP)
→ Enter を押す
［画面・出力］
APF FORMAT(DYNAMIC)
APF ADD DSNAME(MYPROG.LOADLIB) VOLUME(MPRES3)
LPA ADD MODNAME(MOD10) DSNAME(SYS1.LPALIB)
画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により LNKAUTH指定 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SET PROG=SP
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE252I が含まれる。IEE252I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により LNKAUTH指定 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 06.10.10 PROG,APF DISPLAY 857
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
  12  MPRES3 MYPROG.LOADLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0228"><h3>LOGRECバッファ 定義照合 運用確認041</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>第四十一観点 WTOメッセージ で LOGRECバッファ は 定義照合 の対象です（第四十一観点）。第四十一観点 確認時には エラー記録を保持し、IPCSやEREPの診断対象になる記録領域という性質を前提にします（第四十一観点）。第四十一観点 SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同じ証跡に置き、アドレス空間分離の確認を管理します（第四十一観点）。第四十一観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録041から再現します（第四十一観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第四十一証跡です。WTOメッセージ の運用で LOGRECバッファ を点検します。確認観点は LOGRECバッファ、定義照合、運用確認 です。SET PROG=xx後のIEE252I表示 を証跡に残す判断として、あとから再確認しやすいものはどれか。</p><ul class="kb-choices"><li>A. SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同一票へ記録し、LOGRECバッファ を zOSSP正041で確定する。 <span class="kb-ok">✅ 正解</span></li><li>B. ENQ資源管理 の一般メモを採り、SYS1.LINKLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記041として調査範囲を狭める。</li><li>C. LOGRECバッファ の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延041として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在041として残す。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第四十一観点 正解確認: Aは LOGRECバッファ と SYS1.LINKLIB を同じ証跡で扱うため、後続の照合に使えます（第四十一観点）。第四十一観点 背景確認: APF、LPA、LNKLSTはプログラム取得と許可範囲に関係します（第四十一観点）。第四十一観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第四十一観点）。第四十一観点 用語メモ: TCBはタスクの制御ブロックです（第四十一観点）。第四十一観点 SRBは非同期作業の実行単位です（第四十一観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LOGRECバッファ 定義照合 運用確認041</strong></p><p>検証目的: LOGRECバッファ の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SDSF LOG</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により LOGRECバッファ の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 05.18.17 PROG,APF DISPLAY 940
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   2  MPRES1 SYS1.SVCLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により LOGRECバッファ の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SETPROG APF,ADD,DSNAME=MYPROG.LOADLIB,VOLUME=MPRES3
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
画面・出力には CSV410I が含まれる。CSV410I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により LOGRECバッファ の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF,ENTRY=(1-5)
→ Enter を押す
［画面・出力］
CSV450I 05.26.17 PROG,APF DISPLAY 950
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   5  MPRES1 ISF.SISFLPA
画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0229"><h3>SMFPRMxx ストレージ確認 運用確認008</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 初級</p><p>第八観点 z/OS System Programming の WTOメッセージ では SMFPRMxx を障害調査で照合します（第八観点）。第八観点 資料上は SMF記録対象、バッファ、データセット、ログストリーム動作を定義するとして扱います（第八観点）。第八観点 SMF.LOGSTREAM.SP を起点に表示値を戻し、オペレーター応答漏れの防止を点検します（第八観点）。第八観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録008へ書きます（第八観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFPRMxx ストレージ確認 運用確認008</strong></p><p>検証目的: SMFPRMxx の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: ISPF / SAF review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SMFPRMxx の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(IEASYS08)
→ Enter を押す
［画面・出力］
IEASYS08
PROG=SP
SMF=SP
GRSRNL=SP
LNKAUTH=LNKLST
画面・出力には LNKAUTH が含まれる。LNKAUTH を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SMFPRMxx の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX CSV
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
CSV450I PROG,APF DISPLAY
画面・出力には CSV410I が含まれる。CSV410I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SMFPRMxx の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX IEE
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE536I が含まれる。IEE536I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LNKAUTH が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE536I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0230"><h3>SVC割り込み 出口確認 運用確認025</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>第二十五観点 WTOメッセージ で SVC割り込み は 出口確認 の対象です（第二十五観点）。第二十五観点 確認時には 問題プログラムからz/OSサービスを要求し、監視プログラム状態へ制御という性質を前提にします（第二十五観点）。第二十五観点 IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を同じ証跡に置き、共通ストレージ変更の記録を管理します（第二十五観点）。第二十五観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録025から再現します（第二十五観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第二十五証跡です。IFASMFDPジョブログのSYSPRINT を採取した後の扱いを選びます。確認観点は SVC割り込み、出口確認、運用確認 です。QNAME=SYSDSN を根拠として残す時、対象の取り違えを抑える対応はどれか。</p><ul class="kb-choices"><li>A. IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を同一票へ記録し、SVC割り込み を zOSSP正025で確定する。 <span class="kb-ok">✅ 正解</span></li><li>B. TCB/SRB管理 の一般メモを採り、QNAME=SYSDSN、メッセージID、時刻の対応を記録外に置き、zOSSP誤記025として調査範囲を狭める。</li><li>C. SVC割り込み の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延025として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在025として残す。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第二十五観点 正解確認: Aは SVC割り込み と QNAME=SYSDSN を同じ証跡で扱うため、後続の照合に使えます（第二十五観点）。第二十五観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第二十五観点）。第二十五観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第二十五観点）。第二十五観点 用語確認: APFは許可ライブラリーの管理機能です（第二十五観点）。第二十五観点 PROGxxは動的なプログラム管理指定です（第二十五観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SVC割り込み 出口確認 運用確認025</strong></p><p>検証目的: SVC割り込み の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SDSF LOG</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SVC割り込み の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 05.18.01 PROG,APF DISPLAY 924
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   2  MPRES1 SYS1.SVCLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SVC割り込み の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SETPROG APF,ADD,DSNAME=MYPROG.LOADLIB,VOLUME=MPRES3
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
画面・出力には CSV410I が含まれる。CSV410I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SVC割り込み の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF,ENTRY=(1-5)
→ Enter を押す
［画面・出力］
CSV450I 05.26.01 PROG,APF DISPLAY 974
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   5  MPRES1 ISF.SISFLPA
画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0231"><h3>WTOメッセージ WTO経路コード ログとの照合 WTO07</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>ログとの照合では WTOメッセージ の MPF表示 を主操作として WTO07 を判定します。時刻と対象識別子への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO07 に残します。ログとの照合を補助する コンソール表示 では IEE889I を補助値として WTO07 へ保存します。主判定のログとの照合ではメッセージ・経路コードの MPF表示 から MPFLST を読み WTO07 へ残します。証跡照合のログとの照合ではメッセージ・経路コードの MPFLST と IEE889I を WTO07 に保存します。記録対応のログとの照合ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO07 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で WTOメッセージ の MPF表示 と コンソール表示 を使い 操作とログを対応 します。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。MPFLST を読み対象 WTO07 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. D MPFが応答を返した時点で正常とする。応答中のMPFLSTの値は記録しない。IEE600IをMPFLSTと同じ判定値とみなし対象WTO07の主証跡にする。</li><li>B. D MPFのコマンド文字列だけを記録する。MPFLSTを含む応答行は保存しない。</li><li>C. MPFLSTを含むMPF表示の応答行を保存する。その応答を得るためD MPFを使用する。対象WTO07のMESSAGE IDとROUTCDEとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. WTO経路コードの停止または再定義を実施する。その後にD MPFでMPFLSTを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: CはMPF表示で MPFLST を読みMESSAGE IDとROUTCDEの主値として操作とログを対応しWTO07に残します。
機能の仕組み: ログとの照合ではコンソール表示を補助操作としWTO経路コードの時刻と対象識別子をIEE889Iと対象WTO07で照合します。
各候補の評価: MPF表示とコンソール表示の役割を分けるとA: 応答の有無だけではMESSAGE IDとROUTCDEを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではMESSAGE IDとROUTCDEを証明できない点で一次資料と一致しません、C: MPFLSTの実値を対象別に残す点でWTO07を判定できます、D: 変更前のMESSAGE IDとROUTCDEを失う点でコンソール表示の範囲を越えます。結論としてログとの照合のメッセージ・経路コードで判定する対象は WTO07 です。
用語の定義: ログとの照合で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO07へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOメッセージ WTO経路コード ログとの照合 WTO07</strong></p><p>検証目的: WTOメッセージのWTO経路コードについて操作とログを対応し、WTO07のMESSAGE IDとROUTCDEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTO07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO07のMPF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D MPF
→ Enter を押す
［画面・出力］
IEE252I MEMBER MPFLST07 FOUND IN SYS1.PARMLIB MPF ACTIVE
画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO07のコンソール表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D CONSOLES
→ Enter を押す
［画面・出力］
IEE889I CONSOLes STATUS CONSOLE NAME=CON07 STATUS=ACTIVE AUTH=MASTER
画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO07のSYSLOG検索を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND IEE
→ Enter を押す
［画面・出力］
IEE600I REPLY TO MESSAGE IEE07 RECORDED IN SYSLOG
画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の MPFLST が画面・出力に表示されること
② ステップ2 の IEE889I が画面・出力に表示されること
③ ステップ3 の IEE600I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0232"><h3>WTOメッセージ WTO経路コード 代替経路の確認 WTO10</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>代替経路の確認では WTOメッセージ の MPF表示 を主操作として WTO10 を判定します。主経路との役割差への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO10 に残します。代替経路の確認を補助する コンソール表示 では IEE889I を補助値として WTO10 へ保存します。主判定の代替経路の確認ではメッセージ・経路コードの MPF表示 から MPFLST を読み WTO10 へ残します。証跡照合の代替経路の確認ではメッセージ・経路コードの MPFLST と IEE889I を WTO10 に保存します。記録対応の代替経路の確認ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO10 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で WTOメッセージ の MPF表示 と コンソール表示 を照合し 主経路との役割差 を確かめます。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。MPFLST を読む前に対象 WTO10 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. D MPFのコマンド文字列だけを記録する。MPFLSTを含む応答行は保存しない。</li><li>B. D MPFとD CONSOLESの対象名をそろえる。前者のMPFLSTをMESSAGE IDとROUTCDEの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. WTO経路コードの停止または再定義を実施する。その後にD MPFでMPFLSTを採取する。</li><li>D. SVC処理のSVC番号とROUTINEを確認する。その値をWTOメッセージのWTO10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: BはMPF表示で MPFLST を読みMESSAGE IDとROUTCDEの主値として代替手段の成立を確認しWTO10に残します。
運用上の背景: 代替経路の確認ではコンソール表示を補助操作としWTO経路コードの主経路との役割差をIEE889Iと対象WTO10で照合します。
候補別の検討: MPF表示とコンソール表示の役割を分けるとA: 入力記録だけではMESSAGE IDとROUTCDEを証明できない点で一次資料と一致しません、B: 同じ対象名のMPFLSTを採用する点でWTO10を判定できます、C: 変更前のMESSAGE IDとROUTCDEを失う点でコンソール表示の範囲を越えます、D: SVC処理の値ではMPFLSTを確認できない点でWTO10の値を示しません。結論として代替経路の確認のメッセージ・経路コードで判定する対象は WTO10 です。
重要用語の定義: 代替経路の確認で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO10へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOメッセージ WTO経路コード 代替経路の確認 WTO10</strong></p><p>検証目的: WTOメッセージのWTO経路コードについて代替手段の成立を確認し、WTO10のMESSAGE IDとROUTCDEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTO10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO10のMPF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D MPF
→ Enter を押す
［画面・出力］
IEE252I MEMBER MPFLST10 FOUND IN SYS1.PARMLIB MPF ACTIVE
画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO10のコンソール表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D CONSOLES
→ Enter を押す
［画面・出力］
IEE889I CONSOLes STATUS CONSOLE NAME=CON10 STATUS=ACTIVE AUTH=MASTER
画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO10のSYSLOG検索を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND IEE
→ Enter を押す
［画面・出力］
IEE600I REPLY TO MESSAGE IEE10 RECORDED IN SYSLOG
画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の MPFLST が画面・出力に表示されること
② ステップ2 の IEE889I が画面・出力に表示されること
③ ステップ3 の IEE600I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0233"><h3>WTOメッセージ WTO経路コード 変更前の確認 WTO02</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>変更前の確認では WTOメッセージ の コンソール表示 を主操作として WTO02 を判定します。変更対象と非対象の境界への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO02 に残します。変更前の確認を補助する SYSLOG検索 では IEE600I を補助値として WTO02 へ保存します。主判定の変更前の確認ではメッセージ・経路コードの コンソール表示 から IEE889I を読み WTO02 へ残します。証跡照合の変更前の確認ではメッセージ・経路コードの IEE889I と IEE600I を WTO02 に保存します。記録対応の変更前の確認ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO02 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で WTOメッセージ の コンソール表示 と SYSLOG検索 を実施し WTO経路コード の役割を確認します。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。対象 WTO02 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. D CONSOLESを対象名なしで実行する。一覧の先頭行をWTO02の結果として記録する。</li><li>B. 対象WTO02についてD CONSOLESの応答からIEE889Iを確認する。SDSF LOG FIND IEEは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存したD CONSOLESの結果を使う。今回のSDSF LOG FIND IEEの結果と同一時点の証跡として比較する。</li><li>D. 保存済みのWTO02の出力を再利用する。今回のD CONSOLESとSDSF LOG FIND IEEは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Bはコンソール表示で IEE889I を読みMESSAGE IDとROUTCDEの主値として変更前の証跡を保存しWTO02に残します。
動作の背景: 変更前の確認ではSYSLOG検索を補助操作としWTO経路コードの変更対象と非対象の境界をIEE600Iと対象WTO02で照合します。
各選択肢の検討: コンソール表示とSYSLOG検索の役割を分けるとA: 先頭行はWTO02と確定できない点で変更前の確認に合いません、B: IEE889Iと補助証跡の時刻を合わせる点でコンソール表示に合います、C: 採取時刻が異なる点でWTOメッセージに使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でWTO経路コードに使えません。結論として変更前の確認のメッセージ・経路コードで判定する対象は WTO02 です。
初出用語の定義: 変更前の確認で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO02へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOメッセージ WTO経路コード 変更前の確認 WTO02</strong></p><p>検証目的: WTOメッセージのWTO経路コードについて変更前の証跡を保存し、WTO02のMESSAGE IDとROUTCDEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTO02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO02のコンソール表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D CONSOLES
→ Enter を押す
［画面・出力］
IEE889I CONSOLes STATUS CONSOLE NAME=CON02 STATUS=ACTIVE AUTH=MASTER
画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO02のSYSLOG検索を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND IEE
→ Enter を押す
［画面・出力］
IEE600I REPLY TO MESSAGE IEE02 RECORDED IN SYSLOG
画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO02のMPF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D MPF
→ Enter を押す
［画面・出力］
IEE252I MEMBER MPFLST02 FOUND IN SYS1.PARMLIB MPF ACTIVE
画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE889I が画面・出力に表示されること
② ステップ2 の IEE600I が画面・出力に表示されること
③ ステップ3 の MPFLST が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0234"><h3>WTOメッセージ WTO経路コード 変更後の確認 WTO03</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>変更後の確認では WTOメッセージ の SYSLOG検索 を主操作として WTO03 を判定します。反映値と残存値への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO03 に残します。変更後の確認を補助する MPF表示 では MPFLST を補助値として WTO03 へ保存します。主判定の変更後の確認ではメッセージ・経路コードの SYSLOG検索 から IEE600I を読み WTO03 へ残します。証跡照合の変更後の確認ではメッセージ・経路コードの IEE600I と MPFLST を WTO03 に保存します。記録対応の変更後の確認ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO03 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で WTOメッセージ の SYSLOG検索 と MPF表示 を用い 変更結果を検証 します。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。IEE600I で対象 WTO03 の MESSAGE IDとROUTCDE を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. WTO経路コードの停止または再定義を実施する。その後にSDSF LOG FIND IEEでIEE600Iを採取する。</li><li>B. LNKLST管理のSET名とDATASET順序を確認する。その値をWTOメッセージのWTO03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>C. D MPFで周辺状態を押さえる。その後にSDSF LOG FIND IEEでIEE600Iを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. D MPFが成功したためSDSF LOG FIND IEEのIEE600Iも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: CはSYSLOG検索で IEE600I を読みMESSAGE IDとROUTCDEの主値として変更結果を検証しWTO03に残します。
内部の仕組み: 変更後の確認ではMPF表示を補助操作としWTO経路コードの反映値と残存値をMPFLSTと対象WTO03で照合します。
誤答を含む比較: SYSLOG検索とMPF表示の役割を分けるとA: 変更前のMESSAGE IDとROUTCDEを失う点でMESSAGE IDとROUTCDEを確認できません、B: LNKLST管理の値ではIEE600Iを確認できないうえに追加前提も不正な点でMPF表示の範囲を越えます、C: 周辺状態の後にIEE600Iを確認する点で現在値を示します、D: 補助操作の成功ではIEE600Iを確定できない点で変更後の確認に合いません。結論として変更後の確認のメッセージ・経路コードで判定する対象は WTO03 です。
用語定義: 変更後の確認で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO03へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOメッセージ WTO経路コード 変更後の確認 WTO03</strong></p><p>検証目的: WTOメッセージのWTO経路コードについて変更結果を検証し、WTO03のMESSAGE IDとROUTCDEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTO03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO03のSYSLOG検索を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND IEE
→ Enter を押す
［画面・出力］
IEE600I REPLY TO MESSAGE IEE03 RECORDED IN SYSLOG
画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO03のMPF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D MPF
→ Enter を押す
［画面・出力］
IEE252I MEMBER MPFLST03 FOUND IN SYS1.PARMLIB MPF ACTIVE
画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO03のコンソール表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D CONSOLES
→ Enter を押す
［画面・出力］
IEE889I CONSOLes STATUS CONSOLE NAME=CON03 STATUS=ACTIVE AUTH=MASTER
画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
② ステップ2 の MPFLST が画面・出力に表示されること
③ ステップ3 の IEE889I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0235"><h3>WTOメッセージ WTO経路コード 引継ぎ記録 WTO09</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>引継ぎ記録では WTOメッセージ の SYSLOG検索 を主操作として WTO09 を判定します。次担当者が追跡できる証跡への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO09 に残します。引継ぎ記録を補助する MPF表示 では MPFLST を補助値として WTO09 へ保存します。主判定の引継ぎ記録ではメッセージ・経路コードの SYSLOG検索 から IEE600I を読み WTO09 へ残します。証跡照合の引継ぎ記録ではメッセージ・経路コードの IEE600I と MPFLST を WTO09 に保存します。記録対応の引継ぎ記録ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO09 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で WTOメッセージ の SYSLOG検索 と MPF表示 を用い 再現可能な記録を作成 します。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。IEE600I で対象 WTO09 の MESSAGE IDとROUTCDE を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 対象名WTO09を指定してSDSF LOG FIND IEEを実行する。応答中のIEE600Iと時刻を保存する。D MPFで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. D MPFが成功したためSDSF LOG FIND IEEのIEE600Iも正常だと推定する。主出力は保存しない。</li><li>C. SDSF LOG FIND IEEを対象名なしで実行する。一覧の先頭行をWTO09の結果として記録する。</li><li>D. 前回保存したSDSF LOG FIND IEEの結果を使う。今回のD MPFの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: AはSYSLOG検索で IEE600I を読みMESSAGE IDとROUTCDEの主値として再現可能な記録を作成しWTO09に残します。
製品内の仕組み: 引継ぎ記録ではMPF表示を補助操作としWTO経路コードの次担当者が追跡できる証跡をMPFLSTと対象WTO09で照合します。
選択肢別の説明: SYSLOG検索とMPF表示の役割を分けるとA: IEE600Iと時刻を保存する点で現在値を示します、B: 補助操作の成功ではIEE600Iを確定できない点で引継ぎ記録に合いません、C: 先頭行はWTO09と確定できない点でSYSLOG検索を代替しません、D: 採取時刻が異なる点でWTOメッセージに使いません。結論として引継ぎ記録のメッセージ・経路コードで判定する対象は WTO09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO09へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOメッセージ WTO経路コード 引継ぎ記録 WTO09</strong></p><p>検証目的: WTOメッセージのWTO経路コードについて再現可能な記録を作成し、WTO09のMESSAGE IDとROUTCDEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTO09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO09のSYSLOG検索を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND IEE
→ Enter を押す
［画面・出力］
IEE600I REPLY TO MESSAGE IEE09 RECORDED IN SYSLOG
画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO09のMPF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D MPF
→ Enter を押す
［画面・出力］
IEE252I MEMBER MPFLST09 FOUND IN SYS1.PARMLIB MPF ACTIVE
画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO09のコンソール表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D CONSOLES
→ Enter を押す
［画面・出力］
IEE889I CONSOLes STATUS CONSOLE NAME=CON09 STATUS=ACTIVE AUTH=MASTER
画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
② ステップ2 の MPFLST が画面・出力に表示されること
③ ステップ3 の IEE889I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0236"><h3>WTOメッセージ WTO経路コード 復旧後の確認 WTO06</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>復旧後の確認では WTOメッセージ の SYSLOG検索 を主操作として WTO06 を判定します。再発していないことを示す値への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO06 に残します。復旧後の確認を補助する MPF表示 では MPFLST を補助値として WTO06 へ保存します。主判定の復旧後の確認ではメッセージ・経路コードの SYSLOG検索 から IEE600I を読み WTO06 へ残します。証跡照合の復旧後の確認ではメッセージ・経路コードの IEE600I と MPFLST を WTO06 に保存します。記録対応の復旧後の確認ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO06 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で WTOメッセージ の SYSLOG検索 と MPF表示 の役割を分け 再発していないことを示す値 を調べます。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。対象 WTO06 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. GRS資源直列化のSYSTEMとMODEを確認する。その値をWTOメッセージのWTO06にも適用する。</li><li>B. SDSF LOG FIND IEEでIEE600Iを取得してからD CONSOLESでIEE889Iを照合する。WTO06のMESSAGE IDとROUTCDEを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D MPFが成功したためSDSF LOG FIND IEEのIEE600Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象WTO06へ引き継げるものとする。WTO経路コードの再発していないことを示す値は確認済みとして扱う。さらにD CONSOLESのIEE889IをIEE600Iと同種の値として併記する。</li><li>D. SDSF LOG FIND IEEを対象名なしで実行する。一覧の先頭行をWTO06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: BはSYSLOG検索で IEE600I を読みMESSAGE IDとROUTCDEの主値として復旧後の安定性を確認しWTO06に残します。
構成上の背景: 復旧後の確認ではMPF表示を補助操作としWTO経路コードの再発していないことを示す値をMPFLSTと対象WTO06で照合します。
候補ごとの理由: SYSLOG検索とMPF表示の役割を分けるとA: GRS資源直列化の値ではIEE600Iを確認できない点でMPF表示の範囲を越えます、B: IEE600IとIEE889Iを順に照合する点で現在値を示します、C: 補助操作の成功ではIEE600Iを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はWTO06と確定できない点でSYSLOG検索を代替しません。結論として復旧後の確認のメッセージ・経路コードで判定する対象は WTO06 です。
初出用語: 復旧後の確認で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO06へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOメッセージ WTO経路コード 復旧後の確認 WTO06</strong></p><p>検証目的: WTOメッセージのWTO経路コードについて復旧後の安定性を確認し、WTO06のMESSAGE IDとROUTCDEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTO06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO06のSYSLOG検索を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND IEE
→ Enter を押す
［画面・出力］
IEE600I REPLY TO MESSAGE IEE06 RECORDED IN SYSLOG
画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO06のMPF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D MPF
→ Enter を押す
［画面・出力］
IEE252I MEMBER MPFLST06 FOUND IN SYS1.PARMLIB MPF ACTIVE
画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO06のコンソール表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D CONSOLES
→ Enter を押す
［画面・出力］
IEE889I CONSOLes STATUS CONSOLE NAME=CON06 STATUS=ACTIVE AUTH=MASTER
画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE600I が画面・出力に表示されること
② ステップ2 の MPFLST が画面・出力に表示されること
③ ステップ3 の IEE889I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0237"><h3>WTOメッセージ WTO経路コード 復旧準備 WTO05</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>復旧準備では WTOメッセージ の コンソール表示 を主操作として WTO05 を判定します。再開前に必要な整合性への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO05 に残します。復旧準備を補助する SYSLOG検索 では IEE600I を補助値として WTO05 へ保存します。主判定の復旧準備ではメッセージ・経路コードの コンソール表示 から IEE889I を読み WTO05 へ残します。証跡照合の復旧準備ではメッセージ・経路コードの IEE889I と IEE600I を WTO05 に保存します。記録対応の復旧準備ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO05 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で WTOメッセージ の コンソール表示 と SYSLOG検索 を組み合わせる際は WTO経路コード がシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みという仕組みを前提にします。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。IEE889I と MESSAGE IDとROUTCDE を対象 WTO05 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずD CONSOLESを実行する。IEE889Iを保存する。差分はSDSF LOG FIND IEEの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したD CONSOLESの結果を使う。今回のSDSF LOG FIND IEEの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのWTO05の出力を再利用する。今回のD CONSOLESとSDSF LOG FIND IEEは実行済みとして扱う。</li><li>D. SDSF LOG FIND IEEのIEE600IをMESSAGE IDとROUTCDEの主判定に採用する。D CONSOLESの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Aはコンソール表示で IEE889I を読みMESSAGE IDとROUTCDEの主値として復旧条件を確認しWTO05に残します。
処理の仕組み: 復旧準備ではSYSLOG検索を補助操作としWTO経路コードの再開前に必要な整合性をIEE600Iと対象WTO05で照合します。
選択結果の内訳: コンソール表示とSYSLOG検索の役割を分けるとA: 変更前のIEE889Iを保存する点でコンソール表示に合います、B: 採取時刻が異なる点でWTOメッセージに使いません、C: 過去出力では今回の復旧準備を示せない点でWTO経路コードに使えません、D: IEE600IはIEE889Iを代替しないうえに追加前提も不正な点でWTO05を採用できません。結論として復旧準備のメッセージ・経路コードで判定する対象は WTO05 です。
用語の説明: 復旧準備で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO05へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOメッセージ WTO経路コード 復旧準備 WTO05</strong></p><p>検証目的: WTOメッセージのWTO経路コードについて復旧条件を確認し、WTO05のMESSAGE IDとROUTCDEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTO05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO05のコンソール表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D CONSOLES
→ Enter を押す
［画面・出力］
IEE889I CONSOLes STATUS CONSOLE NAME=CON05 STATUS=ACTIVE AUTH=MASTER
画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO05のSYSLOG検索を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND IEE
→ Enter を押す
［画面・出力］
IEE600I REPLY TO MESSAGE IEE05 RECORDED IN SYSLOG
画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO05のMPF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D MPF
→ Enter を押す
［画面・出力］
IEE252I MEMBER MPFLST05 FOUND IN SYS1.PARMLIB MPF ACTIVE
画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE889I が画面・出力に表示されること
② ステップ2 の IEE600I が画面・出力に表示されること
③ ステップ3 の MPFLST が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0238"><h3>WTOメッセージ WTO経路コード 構成監査 WTO08</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>構成監査では WTOメッセージ の コンソール表示 を主操作として WTO08 を判定します。定義値と稼働値の一致への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO08 に残します。構成監査を補助する SYSLOG検索 では IEE600I を補助値として WTO08 へ保存します。主判定の構成監査ではメッセージ・経路コードの コンソール表示 から IEE889I を読み WTO08 へ残します。証跡照合の構成監査ではメッセージ・経路コードの IEE889I と IEE600I を WTO08 に保存します。記録対応の構成監査ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO08 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で WTOメッセージ の コンソール表示 と SYSLOG検索 を実施し WTO経路コード の役割を確認します。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。対象 WTO08 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのWTO08の出力を再利用する。今回のD CONSOLESとSDSF LOG FIND IEEは実行済みとして扱う。</li><li>B. SDSF LOG FIND IEEのIEE600IをMESSAGE IDとROUTCDEの主判定に採用する。D CONSOLESの応答は採取対象から外す。</li><li>C. D MPFのMPFLSTをIEE889Iと同義の成功表示として扱う。D CONSOLESは実行しない。</li><li>D. SDSF LOG FIND IEEの結果だけでは確定しない。D CONSOLESのIEE889Iを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Dはコンソール表示で IEE889I を読みMESSAGE IDとROUTCDEの主値として構成差分を監査しWTO08に残します。
実行時の背景: 構成監査ではSYSLOG検索を補助操作としWTO経路コードの定義値と稼働値の一致をIEE600Iと対象WTO08で照合します。
四つの候補の理由: コンソール表示とSYSLOG検索の役割を分けるとA: 過去出力では今回の構成監査を示せない点でWTOメッセージに使いません、B: IEE600IはIEE889Iを代替しない点でWTO経路コードに使えません、C: MPFLSTとIEE889Iは確認項目が異なる点でWTO08を採用できません、D: IEE889Iを主証跡として区別する点で主証跡になります。結論として構成監査のメッセージ・経路コードで判定する対象は WTO08 です。
初出語定義: 構成監査で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO08へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOメッセージ WTO経路コード 構成監査 WTO08</strong></p><p>検証目的: WTOメッセージのWTO経路コードについて構成差分を監査し、WTO08のMESSAGE IDとROUTCDEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTO08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO08のコンソール表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D CONSOLES
→ Enter を押す
［画面・出力］
IEE889I CONSOLes STATUS CONSOLE NAME=CON08 STATUS=ACTIVE AUTH=MASTER
画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO08のSYSLOG検索を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND IEE
→ Enter を押す
［画面・出力］
IEE600I REPLY TO MESSAGE IEE08 RECORDED IN SYSLOG
画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO08のMPF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D MPF
→ Enter を押す
［画面・出力］
IEE252I MEMBER MPFLST08 FOUND IN SYS1.PARMLIB MPF ACTIVE
画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE889I が画面・出力に表示されること
② ステップ2 の IEE600I が画面・出力に表示されること
③ ステップ3 の MPFLST が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0239"><h3>WTOメッセージ WTO経路コード 通常状態の確認 WTO01</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>通常状態の確認では WTOメッセージ の MPF表示 を主操作として WTO01 を判定します。基準値と現在値の差への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO01 に残します。通常状態の確認を補助する コンソール表示 では IEE889I を補助値として WTO01 へ保存します。主判定の通常状態の確認ではメッセージ・経路コードの MPF表示 から MPFLST を読み WTO01 へ残します。証跡照合の通常状態の確認ではメッセージ・経路コードの MPFLST と IEE889I を WTO01 に保存します。記録対応の通常状態の確認ではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO01 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で WTOメッセージ の MPF表示 と コンソール表示 を使い 通常状態を確定 します。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。MPFLST を読み対象 WTO01 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. D MPFを先に実行する。対象WTO01のMPFLSTをMESSAGE IDとROUTCDEとして記録する。続いてD CONSOLESで同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. D CONSOLESのIEE889IをMESSAGE IDとROUTCDEの主判定に採用する。D MPFの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. SDSF LOG FIND IEEのIEE600IをMPFLSTと同義の成功表示として扱う。D MPFは実行しない。</li><li>D. D MPFが応答を返した時点で正常とする。応答中のMPFLSTの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: AはMPF表示で MPFLST を読みMESSAGE IDとROUTCDEの主値として通常状態を確定しWTO01に残します。
背景・仕組み: 通常状態の確認ではコンソール表示を補助操作としWTO経路コードの基準値と現在値の差をIEE889Iと対象WTO01で照合します。
選択肢の理由: MPF表示とコンソール表示の役割を分けるとA: MPFLSTを主値として補助結果と照合する点で正答です、B: IEE889IはMPFLSTを代替しないうえに追加前提も不正な点でWTO01を採用できません、C: IEE600IとMPFLSTは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではMESSAGE IDとROUTCDEを判定できない点で一次資料と一致しません。結論として通常状態の確認のメッセージ・経路コードで判定する対象は WTO01 です。
用語の初出定義: 通常状態の確認で使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO01へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOメッセージ WTO経路コード 通常状態の確認 WTO01</strong></p><p>検証目的: WTOメッセージのWTO経路コードについて通常状態を確定し、WTO01のMESSAGE IDとROUTCDEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTO01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO01のMPF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D MPF
→ Enter を押す
［画面・出力］
IEE252I MEMBER MPFLST01 FOUND IN SYS1.PARMLIB MPF ACTIVE
画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO01のコンソール表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D CONSOLES
→ Enter を押す
［画面・出力］
IEE889I CONSOLes STATUS CONSOLE NAME=CON01 STATUS=ACTIVE AUTH=MASTER
画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO01のSYSLOG検索を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND IEE
→ Enter を押す
［画面・出力］
IEE600I REPLY TO MESSAGE IEE01 RECORDED IN SYSLOG
画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の MPFLST が画面・出力に表示されること
② ステップ2 の IEE889I が画面・出力に表示されること
③ ステップ3 の IEE600I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0240"><h3>WTOメッセージ WTO経路コード 障害切り分け WTO04</h3><p class="kb-meta">分類: WTOメッセージ ・ 難易度: 中級</p><p>障害切り分けでは WTOメッセージ の MPF表示 を主操作として WTO04 を判定します。最初に失敗した処理への注意として「抑止や経路変更によって必要な警告が運用者へ届かない危険があります」を WTO04 に残します。障害切り分けを補助する コンソール表示 では IEE889I を補助値として WTO04 へ保存します。主判定の障害切り分けではメッセージ・経路コードの MPF表示 から MPFLST を読み WTO04 へ残します。証跡照合の障害切り分けではメッセージ・経路コードの MPFLST と IEE889I を WTO04 に保存します。記録対応の障害切り分けではメッセージ・経路コードの MESSAGE IDとROUTCDE の証跡へ WTO04 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで WTOメッセージ の MPF表示 と コンソール表示 を照合し 最初に失敗した処理 を確かめます。WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みです。抑止や経路変更によって必要な警告が運用者へ届かない危険があります。MPFLST を読む前に対象 WTO04 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. SDSF LOG FIND IEEのIEE600IをMPFLSTと同義の成功表示として扱う。D MPFは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. D MPFが応答を返した時点で正常とする。応答中のMPFLSTの値は記録しない。</li><li>C. D MPFのコマンド文字列だけを記録する。MPFLSTを含む応答行は保存しない。</li><li>D. D MPFの出力でWTO04とMPFLSTが同じ応答にあることを確認する。MESSAGE IDとROUTCDEをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: DはMPF表示で MPFLST を読みMESSAGE IDとROUTCDEの主値として障害範囲を限定しWTO04に残します。
技術的背景: 障害切り分けではコンソール表示を補助操作としWTO経路コードの最初に失敗した処理をIEE889Iと対象WTO04で照合します。
四択の評価: MPF表示とコンソール表示の役割を分けるとA: IEE600IとMPFLSTは確認項目が異なるうえに追加前提も不正な点でWTO04を採用できません、B: 応答の有無だけではMESSAGE IDとROUTCDEを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではMESSAGE IDとROUTCDEを証明できない点で一次資料と一致しません、D: WTO04とMPFLSTを同じ応答で結ぶ点でWTO04を判定できます。結論として障害切り分けのメッセージ・経路コードで判定する対象は WTO04 です。
初出語の意味: 障害切り分けで使う WTO経路コード はシステムまたはアプリケーションメッセージをROUTCDEと記述子コードで適切なコンソールやログへ配布する仕組みを表しMESSAGE IDとROUTCDEを判定する際にWTO04へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOメッセージ WTO経路コード 障害切り分け WTO04</strong></p><p>検証目的: WTOメッセージのWTO経路コードについて障害範囲を限定し、WTO04のMESSAGE IDとROUTCDEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象WTO04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD MPFを指定し、WTO04のMPF表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D MPF
→ Enter を押す
［画面・出力］
IEE252I MEMBER MPFLST04 FOUND IN SYS1.PARMLIB MPF ACTIVE
画面・出力にあるMPFLSTを読み、MESSAGE IDとROUTCDEと対象WTO04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へD CONSOLESを指定し、WTO04のコンソール表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D CONSOLES
→ Enter を押す
［画面・出力］
IEE889I CONSOLes STATUS CONSOLE NAME=CON04 STATUS=ACTIVE AUTH=MASTER
画面・出力にあるIEE889Iを読み、MESSAGE IDとROUTCDEと対象WTO04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System ProgrammingのWTOメッセージを確認する入力画面です。COMMAND入力口へSDSF LOG FIND IEEを指定し、WTO04のSYSLOG検索を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF LOG FIND IEE
→ Enter を押す
［画面・出力］
IEE600I REPLY TO MESSAGE IEE04 RECORDED IN SYSLOG
画面・出力にあるIEE600Iを読み、MESSAGE IDとROUTCDEと対象WTO04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の MPFLST が画面・出力に表示されること
② ステップ2 の IEE889I が画面・出力に表示されること
③ ステップ3 の IEE600I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


## アドレス空間


<section class="kb-item" id="c38-i0241"><h3>GRSリング 表示確認 運用確認013</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 初級</p><p>第十三観点 アドレス空間 で GRSリング は 表示確認 の対象です（第十三観点）。第十三観点 確認時には 複数システム間の資源直列化状態を管理し、DISPLAY GRSで確認という性質を前提にします（第十三観点）。第十三観点 DISPLAY R,ALL の未応答要求表示 と TCB=008F21A0 を同じ証跡に置き、割り込み経路の説明性確保を管理します（第十三観点）。第十三観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録013から再現します（第十三観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第十三証跡です。zOSSP記録013として TCB=008F21A0 の証跡を残します。確認観点は GRS、表示確認、運用確認 です。TCB=008F21A0 を根拠として残す時、対象の取り違えを抑える対応はどれか。</p><ul class="kb-choices"><li>A. DISPLAY R,ALL の未応答要求表示 と TCB=008F21A0 を同一票へ記録し、GRS を zOSSP正013で確定する。 <span class="kb-ok">✅ 正解</span></li><li>B. トレース診断 の一般メモを採り、TCB=008F21A0、メッセージID、時刻の対応を記録外に置き、zOSSP誤記013として調査範囲を狭める。</li><li>C. GRSリング の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延013として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在013として残す。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 第十三観点 正解確認: Aは GRS と TCB=008F21A0 を同じ証跡で扱うため、後続の照合に使えます（第十三観点）。第十三観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第十三観点）。第十三観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第十三観点）。第十三観点 用語確認: APFは許可ライブラリーの管理機能です（第十三観点）。第十三観点 PROGxxは動的なプログラム管理指定です（第十三観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>GRSリング 表示確認 運用確認013</strong></p><p>検証目的: GRSリング の 表示確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / operations</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により GRSリング の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY R,ALL
→ Enter を押す
［画面・出力］
IEE112I 11.15.13 DISPLAY R 712
REPLY ID   MESSAGE TEXT
005        IEA793A SPECIFY DUMP OPTION FOR TCB=008F21A0
画面・出力には IEE112I が含まれる。IEE112I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により GRSリング の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D C
→ Enter を押す
［画面・出力］
IEE889I 15.33.13 CONSOLE DISPLAY 502
MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
画面・出力には IEE889I が含まれる。IEE889I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により GRSリング の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; R 005,INFO
→ Enter を押す
［画面・出力］
IEE600I REPLY TO 005 IS;INFO
IEA631I OPERATOR OPER13 NOW ACTIVE, SYSTEM=SC65
画面・出力には IEE600I が含まれる。IEE600I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0242"><h3>SET PROG=xx 直列化確認 運用確認046</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>第四十六観点 SET PROG=xx は z/OS System Programming の アドレス空間 で扱う管理項目です（第四十六観点）。第四十六観点 PROGxxメンバーを有効化し、APFやLPAなどの動的指定を反映すという説明を操作結果と照合します（第四十六観点）。第四十六観点 RNAME=SYS1.PARMLIB、D TRACE のIEE843I表示、定義メンバーを照合し、診断ログの再現性確保を確認します（第四十六観点）。第四十六観点 証跡には資料IDと確認値を併記し、zOSSP記録046として保存します（第四十六観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第四十六証跡です。運用確認046 の確認で SET PROG=xx を見直します。確認観点は SET PROG=xx、直列化確認、運用確認 です。診断ログの再現性確保のために、D TRACE のIEE843I表示 を使った運用記録として最も適切な扱いはどれか。</p><ul class="kb-choices"><li>A. D TRACE のIEE843I表示 と RNAME=SYS1.PARMLIB を同一票へ記録し、SET PROG=xx を zOSSP正046で確定する。 <span class="kb-ok">✅ 正解</span></li><li>B. ディスパッチ制御 の一般メモを採り、RNAME=SYS1.PARMLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記046として調査範囲を狭める。</li><li>C. SET PROG=xx の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延046として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在046として残す。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第四十六観点 正答根拠: Aは D TRACE のIEE843I表示 と RNAME=SYS1.PARMLIB を結び付けるため、対象システムの取り違えを防げます（第四十六観点）。第四十六観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第四十六観点）。第四十六観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第四十六観点）。第四十六観点 用語説明: WTOは通知メッセージです（第四十六観点）。第四十六観点 WTORは応答を求めるメッセージです（第四十六観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET PROG=xx 直列化確認 運用確認046</strong></p><p>検証目的: SET PROG=xx の 直列化確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: IPCS / dump analysis</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SET PROG=xx の値を確認し、対象の現在値を固定する。
［操作（入力）］
IPCS option 6
COMMAND ===&gt; VERBX LOGDATA
→ Enter を押す
［画面・出力］
LOGDATA VERBEXIT PROCESSING
LOGREC BUFFER RECORDS LOCATED
EREP DETAIL EDIT REPORT FOLLOWS
画面・出力には LOGDATA が含まれる。LOGDATA を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SET PROG=xx の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.30.22 TRACE DISPLAY 215
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON MT=(ON,024K)
画面・出力には IEE843I が含まれる。IEE843I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SET PROG=xx の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
IPCS command line
COMMAND ===&gt; STATUS CPU
→ Enter を押す
［画面・出力］
IPCS STATUS CPU
PSW=070C1000 81234567  ASID=0010
CURRENT TCB ADDRESS RNAME=SYS1.PARMLIB
画面・出力には ASID=0010 が含まれる。ASID=0010 を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LOGDATA が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE843I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ASID=0010 が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0243"><h3>SMFログストリーム 表示確認 運用確認063</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>第六十三観点 アドレス空間 の運用では SMFログストリーム を表示、定義、証跡で確認します（第六十三観点）。第六十三観点 役割は SMFレコードをシスプレックスロガー経由で記録する方式という範囲です（第六十三観点）。第六十三観点 DISPLAY R,ALL の未応答要求表示 の値を MYPROG.LOADLIB と合わせ、割り込み経路の説明性確保を記録します（第六十三観点）。第六十三観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録063に残します（第六十三観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第六十三証跡です。zOSSP記録063として MYPROG.LOADLIB の証跡を残します。確認観点は SMFログストリーム、表示確認、運用確認 です。DISPLAY R,ALL の未応答要求表示 と MYPROG.LOADLIB を合わせて読む時の採用方針として正しいものはどれか。</p><ul class="kb-choices"><li>A. WTOR応答管理 の一般メモを採り、MYPROG.LOADLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記063として調査範囲を狭める。</li><li>B. DISPLAY R,ALL の未応答要求表示 と MYPROG.LOADLIB を同一票へ記録し、SMFログストリーム を zOSSP正063で確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. SMFログストリーム の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延063として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在063として残す。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第六十三観点 採用理由: Bは SMFログストリーム の状態を表示値と定義の両方から確認するため、記録として妥当です（第六十三観点）。第六十三観点 実行背景: SVC、TCB、SRB、PSWは割り込みとディスパッチの説明に使います（第六十三観点）。第六十三観点 誤答整理: Aは一般メモ偏重、Cはジョブログ除外、Dは再現性不足が理由です（第六十三観点）。第六十三観点 用語整理: SMFはシステム測定記録です（第六十三観点）。第六十三観点 IFASMFDPはSMFデータ退避に使います（第六十三観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMFログストリーム 表示確認 運用確認063</strong></p><p>検証目的: SMFログストリーム の 表示確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / WLM dispatch</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SMFログストリーム の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.05.15 ACTIVE JOBS DISPLAY 662
JOBNAME  ASID  STATUS
WLM      000A  ACTIVE
JES2     0012  ACTIVE
画面・出力には IEE114I が含まれる。IEE114I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SMFログストリーム の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D WLM,SYSTEMS
→ Enter を押す
［画面・出力］
IWM026I 12.06.15 WLM DISPLAY 672
SYSTEM   MODE     POLICY
SC65     GOAL     POLSP15
画面・出力には GOAL が含まれる。GOAL を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SMFログストリーム の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
SDSF DA panel
COMMAND ===&gt; DA
→ Enter を押す
［画面・出力］
SDSF DA DISPLAY
JOBNAME  ASID  CPU%  DP
BATCH15 0015  02.1  245
画面・出力には JOBNAME が含まれる。JOBNAME を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE114I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: GOAL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: JOBNAME が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0244"><h3>SRB 状態確認 運用確認080</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>第八十観点 z/OS System Programming の アドレス空間 では SRB を障害調査で照合します（第八十観点）。第八十観点 資料上は サービス要求ブロックとして非同期のシステム作業を表すディスパッチ単位として扱います（第八十観点）。第八十観点 SYS1.PARMLIB(GRSRNLSP) を起点に表示値を戻し、SMF記録欠落の早期検出を点検します（第八十観点）。第八十観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録080へ書きます（第八十観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第八十証跡です。SRB の表示とメッセージIDを比べます。確認観点は SRB、状態確認、運用確認 です。メッセージID、定義メンバー、表示出力を同じ確認票に置く対応として適切なものはどれか。</p><ul class="kb-choices"><li>A. GRS資源直列化 の一般メモを採り、SYS1.PARMLIB(GRSRNLSP)、メッセージID、時刻の対応を記録外に置き、zOSSP誤記080として調査範囲を狭める。</li><li>B. SETPROG APF後のCSV410I表示 と SYS1.PARMLIB(GRSRNLSP) を同一票へ記録し、SRB を zOSSP正080で確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. SRB の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延080として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在080として残す。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第八十観点 照合結果: Bは SYS1.PARMLIB(GRSRNLSP) をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第八十観点）。第八十観点 操作背景: WTOとWTORはオペレーター通知と応答をコンソールログへ残します（第八十観点）。第八十観点 誤答確認: Aは SYS1.PARMLIB(GRSRNLSP) 未追跡、Cはコマンド確認不足、Dは別システム混同が理由です（第八十観点）。第八十観点 用語補足: ENQは資源を直列化します（第八十観点）。第八十観点 DEQは取得した資源を解放します（第八十観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SRB 状態確認 運用確認080</strong></p><p>検証目的: SRB の 状態確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: ISPF / SAF review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SRB の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(IEASYS08)
→ Enter を押す
［画面・出力］
IEASYS08
PROG=SP
SMF=SP
GRSRNL=SP
LNKAUTH=LNKLST
画面・出力には LNKAUTH が含まれる。LNKAUTH を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SRB の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX CSV
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
CSV450I PROG,APF DISPLAY
画面・出力には CSV410I が含まれる。CSV410I を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SRB の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX IEE
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE536I が含まれる。IEE536I を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LNKAUTH が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE536I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0245"><h3>SYS1.PARMLIB 直列化確認 運用確認096</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 上級</p><p>第九十六観点 z/OS System Programming の アドレス空間 では SYS1.PARMLIB を障害調査で照合します（第九十六観点）。第九十六観点 資料上は IEASYSxx、PROGxx、SMFPRMxx、GRSRNLxxなとして扱います（第九十六観点）。第九十六観点 ROUTCDE=ALL を起点に表示値を戻し、診断ログの再現性確保を点検します（第九十六観点）。第九十六観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録096へ書きます（第九十六観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第九十六証跡です。運用確認096 の確認で SYS1.PARMLIB を見直します。確認観点は SYS1.PARMLIB、直列化確認、運用確認 です。診断ログの再現性確保を満たす記録方法として、表示値と定義を結ぶものはどれか。</p><ul class="kb-choices"><li>A. LPA管理 の一般メモを採り、ROUTCDE=ALL、メッセージID、時刻の対応を記録外に置き、zOSSP誤記096として調査範囲を狭める。</li><li>B. SYS1.PARMLIB の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延096として扱う。</li><li>C. D TRACE のIEE843I表示 と ROUTCDE=ALL を同一票へ記録し、SYS1.PARMLIB を zOSSP正096で確定する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在096として残す。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 第九十六観点 照合結果: Cは ROUTCDE=ALL をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第九十六観点）。第九十六観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第九十六観点）。第九十六観点 誤答確認: Aは ROUTCDE=ALL 未追跡、Bはコマンド確認不足、Dは別システム混同が理由です（第九十六観点）。第九十六観点 初出定義: PSWは実行状態を示す語です（第九十六観点）。第九十六観点 SVCは監視プログラム呼出しです（第九十六観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SYS1.PARMLIB 直列化確認 運用確認096</strong></p><p>検証目的: SYS1.PARMLIB の 直列化確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: ISPF / SAF review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SYS1.PARMLIB の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(IEASYS24)
→ Enter を押す
［画面・出力］
IEASYS24
PROG=SP
SMF=SP
GRSRNL=SP
LNKAUTH=LNKLST
画面・出力には LNKAUTH が含まれる。LNKAUTH を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SYS1.PARMLIB の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX CSV
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
CSV450I PROG,APF DISPLAY
画面・出力には CSV410I が含まれる。CSV410I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SYS1.PARMLIB の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX IEE
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE536I が含まれる。IEE536I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LNKAUTH が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE536I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0246"><h3>アドレス空間 ASID管理 ログとの照合 ASID07</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>ログとの照合では アドレス空間 の 稼働一覧 を主操作として ASID07 を判定します。時刻と対象識別子への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID07 に残します。ログとの照合を補助する 個別表示 では ASID=00 を補助値として ASID07 へ保存します。主判定のログとの照合ではアドレス空間・管理の 稼働一覧 から IEE114I を読み ASID07 へ残します。証跡照合のログとの照合ではアドレス空間・管理の IEE114I と ASID=00 を ASID07 に保存します。記録対応のログとの照合ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID07 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で アドレス空間 の 稼働一覧 と 個別表示 を組み合わせる際は ASID管理 がジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みという仕組みを前提にします。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。IEE114I と JOBNAMEとASID を対象 ASID07 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. D A,Lが応答を返した時点で正常とする。応答中のIEE114Iの値は記録しない。JOBNAMEをIEE114Iと同じ判定値とみなし対象ASID07の主証跡にする。</li><li>B. D A,Lのコマンド文字列だけを記録する。IEE114Iを含む応答行は保存しない。</li><li>C. IEE114Iを含む稼働一覧の応答行を保存する。その応答を得るためD A,Lを使用する。対象ASID07のJOBNAMEとASIDとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>D. ASID管理の停止または再定義を実施する。その後にD A,LでIEE114Iを採取する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: Cは稼働一覧で IEE114I を読みJOBNAMEとASIDの主値として操作とログを対応しASID07に残します。
機能の仕組み: ログとの照合では個別表示を補助操作としASID管理の時刻と対象識別子をASID=00と対象ASID07で照合します。
各候補の評価: 稼働一覧と個別表示の役割を分けるとA: 応答の有無だけではJOBNAMEとASIDを判定できないうえに追加前提も不正な点で時刻と対象識別子を示せません、B: 入力記録だけではJOBNAMEとASIDを証明できない点で一次資料と一致しません、C: IEE114Iの実値を対象別に残す点でASID07を判定できます、D: 変更前のJOBNAMEとASIDを失う点で個別表示の範囲を越えます。結論としてログとの照合のアドレス空間・管理で判定する対象は ASID07 です。
用語の定義: ログとの照合で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID07へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アドレス空間 ASID管理 ログとの照合 ASID07</strong></p><p>検証目的: アドレス空間のASID管理について操作とログを対応し、ASID07のJOBNAMEとASIDを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象ASID07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID07の稼働一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB07
画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB07を指定し、ASID07の個別表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB07
→ Enter を押す
［画面・出力］
IEE115I JOB07 ACTIVE ON SYSA ASID=0007
画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB07を指定し、ASID07のSDSF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF DA PREFIX JOB07
→ Enter を押す
［画面・出力］
NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE114I が画面・出力に表示されること
② ステップ2 の ASID=00 が画面・出力に表示されること
③ ステップ3 の JOBNAME が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0247"><h3>アドレス空間 ASID管理 代替経路の確認 ASID10</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>代替経路の確認では アドレス空間 の 稼働一覧 を主操作として ASID10 を判定します。主経路との役割差への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID10 に残します。代替経路の確認を補助する 個別表示 では ASID=00 を補助値として ASID10 へ保存します。主判定の代替経路の確認ではアドレス空間・管理の 稼働一覧 から IEE114I を読み ASID10 へ残します。証跡照合の代替経路の確認ではアドレス空間・管理の IEE114I と ASID=00 を ASID10 に保存します。記録対応の代替経路の確認ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID10 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で アドレス空間 の 稼働一覧 と 個別表示 を実施し ASID管理 の役割を確認します。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。対象 ASID10 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. D A,Lのコマンド文字列だけを記録する。IEE114Iを含む応答行は保存しない。</li><li>B. D A,LとD A,JOB10の対象名をそろえる。前者のIEE114IをJOBNAMEとASIDの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li><li>C. ASID管理の停止または再定義を実施する。その後にD A,LでIEE114Iを採取する。</li><li>D. SVC処理のSVC番号とROUTINEを確認する。その値をアドレス空間のASID10にも適用する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: Bは稼働一覧で IEE114I を読みJOBNAMEとASIDの主値として代替手段の成立を確認しASID10に残します。
運用上の背景: 代替経路の確認では個別表示を補助操作としASID管理の主経路との役割差をASID=00と対象ASID10で照合します。
候補別の検討: 稼働一覧と個別表示の役割を分けるとA: 入力記録だけではJOBNAMEとASIDを証明できない点で一次資料と一致しません、B: 同じ対象名のIEE114Iを採用する点でASID10を判定できます、C: 変更前のJOBNAMEとASIDを失う点で個別表示の範囲を越えます、D: SVC処理の値ではIEE114Iを確認できない点でASID10の値を示しません。結論として代替経路の確認のアドレス空間・管理で判定する対象は ASID10 です。
重要用語の定義: 代替経路の確認で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID10へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アドレス空間 ASID管理 代替経路の確認 ASID10</strong></p><p>検証目的: アドレス空間のASID管理について代替手段の成立を確認し、ASID10のJOBNAMEとASIDを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象ASID10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID10の稼働一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB10
画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB10を指定し、ASID10の個別表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB10
→ Enter を押す
［画面・出力］
IEE115I JOB10 ACTIVE ON SYSA ASID=0010
画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB10を指定し、ASID10のSDSF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF DA PREFIX JOB10
→ Enter を押す
［画面・出力］
NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE114I が画面・出力に表示されること
② ステップ2 の ASID=00 が画面・出力に表示されること
③ ステップ3 の JOBNAME が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0248"><h3>アドレス空間 ASID管理 変更前の確認 ASID02</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>変更前の確認では アドレス空間 の 個別表示 を主操作として ASID02 を判定します。変更対象と非対象の境界への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID02 に残します。変更前の確認を補助する SDSF確認 では JOBNAME を補助値として ASID02 へ保存します。主判定の変更前の確認ではアドレス空間・管理の 個別表示 から ASID=00 を読み ASID02 へ残します。証跡照合の変更前の確認ではアドレス空間・管理の ASID=00 と JOBNAME を ASID02 に保存します。記録対応の変更前の確認ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID02 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で アドレス空間 の 個別表示 と SDSF確認 の役割を分け 変更対象と非対象の境界 を調べます。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。対象 ASID02 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. D A,JOB02を対象名なしで実行する。一覧の先頭行をASID02の結果として記録する。</li><li>B. 対象ASID02についてD A,JOB02の応答からASID=00を確認する。SDSF DA PREFIX JOB02は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 前回保存したD A,JOB02の結果を使う。今回のSDSF DA PREFIX JOB02の結果と同一時点の証跡として比較する。</li><li>D. 保存済みのASID02の出力を再利用する。今回のD A,JOB02とSDSF DA PREFIX JOB02は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: Bは個別表示で ASID=00 を読みJOBNAMEとASIDの主値として変更前の証跡を保存しASID02に残します。
動作の背景: 変更前の確認ではSDSF確認を補助操作としASID管理の変更対象と非対象の境界をJOBNAMEと対象ASID02で照合します。
各選択肢の検討: 個別表示とSDSF確認の役割を分けるとA: 先頭行はASID02と確定できない点で変更前の確認に合いません、B: ASID=00と補助証跡の時刻を合わせる点で個別表示に合います、C: 採取時刻が異なる点でアドレス空間に使いません、D: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でASID管理に使えません。結論として変更前の確認のアドレス空間・管理で判定する対象は ASID02 です。
初出用語の定義: 変更前の確認で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID02へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アドレス空間 ASID管理 変更前の確認 ASID02</strong></p><p>検証目的: アドレス空間のASID管理について変更前の証跡を保存し、ASID02のJOBNAMEとASIDを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象ASID02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB02を指定し、ASID02の個別表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB02
→ Enter を押す
［画面・出力］
IEE115I JOB02 ACTIVE ON SYSA ASID=0002
画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB02を指定し、ASID02のSDSF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF DA PREFIX JOB02
→ Enter を押す
［画面・出力］
NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID02の稼働一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB02
画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ASID=00 が画面・出力に表示されること
② ステップ2 の JOBNAME が画面・出力に表示されること
③ ステップ3 の IEE114I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0249"><h3>アドレス空間 ASID管理 変更後の確認 ASID03</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>変更後の確認では アドレス空間 の SDSF確認 を主操作として ASID03 を判定します。反映値と残存値への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID03 に残します。変更後の確認を補助する 稼働一覧 では IEE114I を補助値として ASID03 へ保存します。主判定の変更後の確認ではアドレス空間・管理の SDSF確認 から JOBNAME を読み ASID03 へ残します。証跡照合の変更後の確認ではアドレス空間・管理の JOBNAME と IEE114I を ASID03 に保存します。記録対応の変更後の確認ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID03 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で アドレス空間 の SDSF確認 と 稼働一覧 を使い 変更結果を検証 します。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。JOBNAME を読み対象 ASID03 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. ASID管理の停止または再定義を実施する。その後にSDSF DA PREFIX JOB03でJOBNAMEを採取する。</li><li>B. LNKLST管理のSET名とDATASET順序を確認する。その値をアドレス空間のASID03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>C. D A,Lで周辺状態を押さえる。その後にSDSF DA PREFIX JOB03でJOBNAMEを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>D. D A,Lが成功したためSDSF DA PREFIX JOB03のJOBNAMEも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: CはSDSF確認で JOBNAME を読みJOBNAMEとASIDの主値として変更結果を検証しASID03に残します。
内部の仕組み: 変更後の確認では稼働一覧を補助操作としASID管理の反映値と残存値をIEE114Iと対象ASID03で照合します。
誤答を含む比較: SDSF確認と稼働一覧の役割を分けるとA: 変更前のJOBNAMEとASIDを失う点でJOBNAMEとASIDを確認できません、B: LNKLST管理の値ではJOBNAMEを確認できないうえに追加前提も不正な点で稼働一覧の範囲を越えます、C: 周辺状態の後にJOBNAMEを確認する点で現在値を示します、D: 補助操作の成功ではJOBNAMEを確定できない点で変更後の確認に合いません。結論として変更後の確認のアドレス空間・管理で判定する対象は ASID03 です。
用語定義: 変更後の確認で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID03へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アドレス空間 ASID管理 変更後の確認 ASID03</strong></p><p>検証目的: アドレス空間のASID管理について変更結果を検証し、ASID03のJOBNAMEとASIDを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象ASID03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB03を指定し、ASID03のSDSF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF DA PREFIX JOB03
→ Enter を押す
［画面・出力］
NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID03の稼働一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB03
画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB03を指定し、ASID03の個別表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB03
→ Enter を押す
［画面・出力］
IEE115I JOB03 ACTIVE ON SYSA ASID=0003
画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の JOBNAME が画面・出力に表示されること
② ステップ2 の IEE114I が画面・出力に表示されること
③ ステップ3 の ASID=00 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0250"><h3>アドレス空間 ASID管理 引継ぎ記録 ASID09</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>引継ぎ記録では アドレス空間 の SDSF確認 を主操作として ASID09 を判定します。次担当者が追跡できる証跡への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID09 に残します。引継ぎ記録を補助する 稼働一覧 では IEE114I を補助値として ASID09 へ保存します。主判定の引継ぎ記録ではアドレス空間・管理の SDSF確認 から JOBNAME を読み ASID09 へ残します。証跡照合の引継ぎ記録ではアドレス空間・管理の JOBNAME と IEE114I を ASID09 に保存します。記録対応の引継ぎ記録ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID09 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で アドレス空間 の SDSF確認 と 稼働一覧 を使い 再現可能な記録を作成 します。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。JOBNAME を読み対象 ASID09 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 対象名ASID09を指定してSDSF DA PREFIX JOB09を実行する。応答中のJOBNAMEと時刻を保存する。D A,Lで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>B. D A,Lが成功したためSDSF DA PREFIX JOB09のJOBNAMEも正常だと推定する。主出力は保存しない。</li><li>C. SDSF DA PREFIX JOB09を対象名なしで実行する。一覧の先頭行をASID09の結果として記録する。</li><li>D. 前回保存したSDSF DA PREFIX JOB09の結果を使う。今回のD A,Lの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: AはSDSF確認で JOBNAME を読みJOBNAMEとASIDの主値として再現可能な記録を作成しASID09に残します。
製品内の仕組み: 引継ぎ記録では稼働一覧を補助操作としASID管理の次担当者が追跡できる証跡をIEE114Iと対象ASID09で照合します。
選択肢別の説明: SDSF確認と稼働一覧の役割を分けるとA: JOBNAMEと時刻を保存する点で現在値を示します、B: 補助操作の成功ではJOBNAMEを確定できない点で引継ぎ記録に合いません、C: 先頭行はASID09と確定できない点でSDSF確認を代替しません、D: 採取時刻が異なる点でアドレス空間に使いません。結論として引継ぎ記録のアドレス空間・管理で判定する対象は ASID09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID09へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アドレス空間 ASID管理 引継ぎ記録 ASID09</strong></p><p>検証目的: アドレス空間のASID管理について再現可能な記録を作成し、ASID09のJOBNAMEとASIDを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象ASID09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB09を指定し、ASID09のSDSF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF DA PREFIX JOB09
→ Enter を押す
［画面・出力］
NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID09の稼働一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB09
画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB09を指定し、ASID09の個別表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB09
→ Enter を押す
［画面・出力］
IEE115I JOB09 ACTIVE ON SYSA ASID=0009
画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の JOBNAME が画面・出力に表示されること
② ステップ2 の IEE114I が画面・出力に表示されること
③ ステップ3 の ASID=00 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0251"><h3>アドレス空間 ASID管理 復旧後の確認 ASID06</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>復旧後の確認では アドレス空間 の SDSF確認 を主操作として ASID06 を判定します。再発していないことを示す値への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID06 に残します。復旧後の確認を補助する 稼働一覧 では IEE114I を補助値として ASID06 へ保存します。主判定の復旧後の確認ではアドレス空間・管理の SDSF確認 から JOBNAME を読み ASID06 へ残します。証跡照合の復旧後の確認ではアドレス空間・管理の JOBNAME と IEE114I を ASID06 に保存します。記録対応の復旧後の確認ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID06 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で アドレス空間 の SDSF確認 と 稼働一覧 を照合し 再発していないことを示す値 を確かめます。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。JOBNAME を読む前に対象 ASID06 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. GRS資源直列化のSYSTEMとMODEを確認する。その値をアドレス空間のASID06にも適用する。</li><li>B. SDSF DA PREFIX JOB06でJOBNAMEを取得してからD A,JOB06でASID=00を照合する。ASID06のJOBNAMEとASIDを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,Lが成功したためSDSF DA PREFIX JOB06のJOBNAMEも正常だと推定する。主出力は保存しない。別資源で得た状態を対象ASID06へ引き継げるものとする。</li><li>D. SDSF DA PREFIX JOB06を対象名なしで実行する。一覧の先頭行をASID06の結果として記録する。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: BはSDSF確認で JOBNAME を読みJOBNAMEとASIDの主値として復旧後の安定性を確認しASID06に残します。
構成上の背景: 復旧後の確認では稼働一覧を補助操作としASID管理の再発していないことを示す値をIEE114Iと対象ASID06で照合します。
候補ごとの理由: SDSF確認と稼働一覧の役割を分けるとA: GRS資源直列化の値ではJOBNAMEを確認できない点で稼働一覧の範囲を越えます、B: JOBNAMEとASID=00を順に照合する点で現在値を示します、C: 補助操作の成功ではJOBNAMEを確定できないうえに追加前提も不正な点で復旧後の確認に合いません、D: 先頭行はASID06と確定できない点でSDSF確認を代替しません。結論として復旧後の確認のアドレス空間・管理で判定する対象は ASID06 です。
初出用語: 復旧後の確認で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID06へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アドレス空間 ASID管理 復旧後の確認 ASID06</strong></p><p>検証目的: アドレス空間のASID管理について復旧後の安定性を確認し、ASID06のJOBNAMEとASIDを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象ASID06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB06を指定し、ASID06のSDSF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF DA PREFIX JOB06
→ Enter を押す
［画面・出力］
NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID06の稼働一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB06
画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB06を指定し、ASID06の個別表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB06
→ Enter を押す
［画面・出力］
IEE115I JOB06 ACTIVE ON SYSA ASID=0006
画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の JOBNAME が画面・出力に表示されること
② ステップ2 の IEE114I が画面・出力に表示されること
③ ステップ3 の ASID=00 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0252"><h3>アドレス空間 ASID管理 復旧準備 ASID05</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>復旧準備では アドレス空間 の 個別表示 を主操作として ASID05 を判定します。再開前に必要な整合性への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID05 に残します。復旧準備を補助する SDSF確認 では JOBNAME を補助値として ASID05 へ保存します。主判定の復旧準備ではアドレス空間・管理の 個別表示 から ASID=00 を読み ASID05 へ残します。証跡照合の復旧準備ではアドレス空間・管理の ASID=00 と JOBNAME を ASID05 に保存します。記録対応の復旧準備ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID05 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で アドレス空間 の 個別表示 と SDSF確認 を用い 復旧条件を確認 します。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。ASID=00 で対象 ASID05 の JOBNAMEとASID を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. 変更を加えずD A,JOB05を実行する。ASID=00を保存する。差分はSDSF DA PREFIX JOB05の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>B. 前回保存したD A,JOB05の結果を使う。今回のSDSF DA PREFIX JOB05の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのASID05の出力を再利用する。今回のD A,JOB05とSDSF DA PREFIX JOB05は実行済みとして扱う。</li><li>D. SDSF DA PREFIX JOB05のJOBNAMEをJOBNAMEとASIDの主判定に採用する。D A,JOB05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: Aは個別表示で ASID=00 を読みJOBNAMEとASIDの主値として復旧条件を確認しASID05に残します。
処理の仕組み: 復旧準備ではSDSF確認を補助操作としASID管理の再開前に必要な整合性をJOBNAMEと対象ASID05で照合します。
選択結果の内訳: 個別表示とSDSF確認の役割を分けるとA: 変更前のASID=00を保存する点で個別表示に合います、B: 採取時刻が異なる点でアドレス空間に使いません、C: 過去出力では今回の復旧準備を示せない点でASID管理に使えません、D: JOBNAMEはASID=00を代替しないうえに追加前提も不正な点でASID05を採用できません。結論として復旧準備のアドレス空間・管理で判定する対象は ASID05 です。
用語の説明: 復旧準備で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID05へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アドレス空間 ASID管理 復旧準備 ASID05</strong></p><p>検証目的: アドレス空間のASID管理について復旧条件を確認し、ASID05のJOBNAMEとASIDを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象ASID05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB05を指定し、ASID05の個別表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB05
→ Enter を押す
［画面・出力］
IEE115I JOB05 ACTIVE ON SYSA ASID=0005
画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB05を指定し、ASID05のSDSF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF DA PREFIX JOB05
→ Enter を押す
［画面・出力］
NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID05の稼働一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB05
画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ASID=00 が画面・出力に表示されること
② ステップ2 の JOBNAME が画面・出力に表示されること
③ ステップ3 の IEE114I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0253"><h3>アドレス空間 ASID管理 構成監査 ASID08</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>構成監査では アドレス空間 の 個別表示 を主操作として ASID08 を判定します。定義値と稼働値の一致への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID08 に残します。構成監査を補助する SDSF確認 では JOBNAME を補助値として ASID08 へ保存します。主判定の構成監査ではアドレス空間・管理の 個別表示 から ASID=00 を読み ASID08 へ残します。証跡照合の構成監査ではアドレス空間・管理の ASID=00 と JOBNAME を ASID08 に保存します。記録対応の構成監査ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID08 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で アドレス空間 の 個別表示 と SDSF確認 の役割を分け 定義値と稼働値の一致 を調べます。ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みです。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。対象 ASID08 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのASID08の出力を再利用する。今回のD A,JOB08とSDSF DA PREFIX JOB08は実行済みとして扱う。</li><li>B. SDSF DA PREFIX JOB08のJOBNAMEをJOBNAMEとASIDの主判定に採用する。D A,JOB08の応答は採取対象から外す。</li><li>C. D A,LのIEE114IをASID=00と同義の成功表示として扱う。D A,JOB08は実行しない。</li><li>D. SDSF DA PREFIX JOB08の結果だけでは確定しない。D A,JOB08のASID=00を主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: Dは個別表示で ASID=00 を読みJOBNAMEとASIDの主値として構成差分を監査しASID08に残します。
実行時の背景: 構成監査ではSDSF確認を補助操作としASID管理の定義値と稼働値の一致をJOBNAMEと対象ASID08で照合します。
四つの候補の理由: 個別表示とSDSF確認の役割を分けるとA: 過去出力では今回の構成監査を示せない点でアドレス空間に使いません、B: JOBNAMEはASID=00を代替しない点でASID管理に使えません、C: IEE114IとASID=00は確認項目が異なる点でASID08を採用できません、D: ASID=00を主証跡として区別する点で主証跡になります。結論として構成監査のアドレス空間・管理で判定する対象は ASID08 です。
初出語定義: 構成監査で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID08へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アドレス空間 ASID管理 構成監査 ASID08</strong></p><p>検証目的: アドレス空間のASID管理について構成差分を監査し、ASID08のJOBNAMEとASIDを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象ASID08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB08を指定し、ASID08の個別表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB08
→ Enter を押す
［画面・出力］
IEE115I JOB08 ACTIVE ON SYSA ASID=0008
画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB08を指定し、ASID08のSDSF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF DA PREFIX JOB08
→ Enter を押す
［画面・出力］
NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID08の稼働一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB08
画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の ASID=00 が画面・出力に表示されること
② ステップ2 の JOBNAME が画面・出力に表示されること
③ ステップ3 の IEE114I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0254"><h3>アドレス空間 ASID管理 通常状態の確認 ASID01</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>通常状態の確認では アドレス空間 の 稼働一覧 を主操作として ASID01 を判定します。基準値と現在値の差への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID01 に残します。通常状態の確認を補助する 個別表示 では ASID=00 を補助値として ASID01 へ保存します。主判定の通常状態の確認ではアドレス空間・管理の 稼働一覧 から IEE114I を読み ASID01 へ残します。証跡照合の通常状態の確認ではアドレス空間・管理の IEE114I と ASID=00 を ASID01 に保存します。記録対応の通常状態の確認ではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID01 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で アドレス空間 の 稼働一覧 と 個別表示 を組み合わせる際は ASID管理 がジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みという仕組みを前提にします。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。IEE114I と JOBNAMEとASID を対象 ASID01 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. D A,Lを先に実行する。対象ASID01のIEE114IをJOBNAMEとASIDとして記録する。続いてD A,JOB01で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>B. D A,JOB01のASID=00をJOBNAMEとASIDの主判定に採用する。D A,Lの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>C. SDSF DA PREFIX JOB01のJOBNAMEをIEE114Iと同義の成功表示として扱う。D A,Lは実行しない。</li><li>D. D A,Lが応答を返した時点で正常とする。応答中のIEE114Iの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: Aは稼働一覧で IEE114I を読みJOBNAMEとASIDの主値として通常状態を確定しASID01に残します。
背景・仕組み: 通常状態の確認では個別表示を補助操作としASID管理の基準値と現在値の差をASID=00と対象ASID01で照合します。
選択肢の理由: 稼働一覧と個別表示の役割を分けるとA: IEE114Iを主値として補助結果と照合する点で正答です、B: ASID=00はIEE114Iを代替しないうえに追加前提も不正な点でASID01を採用できません、C: JOBNAMEとIEE114Iは確認項目が異なる点で基準値と現在値の差を示せません、D: 応答の有無だけではJOBNAMEとASIDを判定できない点で一次資料と一致しません。結論として通常状態の確認のアドレス空間・管理で判定する対象は ASID01 です。
用語の初出定義: 通常状態の確認で使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID01へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アドレス空間 ASID管理 通常状態の確認 ASID01</strong></p><p>検証目的: アドレス空間のASID管理について通常状態を確定し、ASID01のJOBNAMEとASIDを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象ASID01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID01の稼働一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB01
画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB01を指定し、ASID01の個別表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB01
→ Enter を押す
［画面・出力］
IEE115I JOB01 ACTIVE ON SYSA ASID=0001
画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB01を指定し、ASID01のSDSF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF DA PREFIX JOB01
→ Enter を押す
［画面・出力］
NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE114I が画面・出力に表示されること
② ステップ2 の ASID=00 が画面・出力に表示されること
③ ステップ3 の JOBNAME が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0255"><h3>アドレス空間 ASID管理 障害切り分け ASID04</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>障害切り分けでは アドレス空間 の 稼働一覧 を主操作として ASID04 を判定します。最初に失敗した処理への注意として「同名ジョブの旧実行や別システムを対象にしてしまう危険があります」を ASID04 に残します。障害切り分けを補助する 個別表示 では ASID=00 を補助値として ASID04 へ保存します。主判定の障害切り分けではアドレス空間・管理の 稼働一覧 から IEE114I を読み ASID04 へ残します。証跡照合の障害切り分けではアドレス空間・管理の IEE114I と ASID=00 を ASID04 に保存します。記録対応の障害切り分けではアドレス空間・管理の JOBNAMEとASID の証跡へ ASID04 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで アドレス空間 の 稼働一覧 と 個別表示 を実施し ASID管理 の役割を確認します。同名ジョブの旧実行や別システムを対象にしてしまう危険があります。対象 ASID04 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. SDSF DA PREFIX JOB04のJOBNAMEをIEE114Iと同義の成功表示として扱う。D A,Lは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. D A,Lが応答を返した時点で正常とする。応答中のIEE114Iの値は記録しない。</li><li>C. D A,Lのコマンド文字列だけを記録する。IEE114Iを含む応答行は保存しない。</li><li>D. D A,Lの出力でASID04とIEE114Iが同じ応答にあることを確認する。JOBNAMEとASIDをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: Dは稼働一覧で IEE114I を読みJOBNAMEとASIDの主値として障害範囲を限定しASID04に残します。
技術的背景: 障害切り分けでは個別表示を補助操作としASID管理の最初に失敗した処理をASID=00と対象ASID04で照合します。
四択の評価: 稼働一覧と個別表示の役割を分けるとA: JOBNAMEとIEE114Iは確認項目が異なるうえに追加前提も不正な点でASID04を採用できません、B: 応答の有無だけではJOBNAMEとASIDを判定できない点で最初に失敗した処理を示せません、C: 入力記録だけではJOBNAMEとASIDを証明できない点で一次資料と一致しません、D: ASID04とIEE114Iを同じ応答で結ぶ点でASID04を判定できます。結論として障害切り分けのアドレス空間・管理で判定する対象は ASID04 です。
初出語の意味: 障害切り分けで使う ASID管理 はジョブ名、ASID、開始タスク、サブシステム状態を結び付けて仮想アドレス空間を識別する仕組みを表しJOBNAMEとASIDを判定する際にASID04へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アドレス空間 ASID管理 障害切り分け ASID04</strong></p><p>検証目的: アドレス空間のASID管理について障害範囲を限定し、ASID04のJOBNAMEとASIDを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象ASID04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,Lを指定し、ASID04の稼働一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.22.00 ACTIVITY JOBS M/S TS USERS SYSAS JOB04
画面・出力にあるIEE114Iを読み、JOBNAMEとASIDと対象ASID04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へD A,JOB04を指定し、ASID04の個別表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D A,JOB04
→ Enter を押す
［画面・出力］
IEE115I JOB04 ACTIVE ON SYSA ASID=0004
画面・出力にあるASID=00を読み、JOBNAMEとASIDと対象ASID04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのアドレス空間を確認する入力画面です。COMMAND入力口へSDSF DA PREFIX JOB04を指定し、ASID04のSDSF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; SDSF DA PREFIX JOB04
→ Enter を押す
［画面・出力］
NP JOBNAME StepName ProcStep JobID Owner C Pos DP Real Paging SIO CPU% ASID
画面・出力にあるJOBNAMEを読み、JOBNAMEとASIDと対象ASID04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE114I が画面・出力に表示されること
② ステップ2 の ASID=00 が画面・出力に表示されること
③ ステップ3 の JOBNAME が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0256"><h3>ディスパッチ優先順位 状態確認 運用確認030</h3><p class="kb-meta">分類: アドレス空間 ・ 難易度: 中級</p><p>第三十観点 ディスパッチ優先順位 は z/OS System Programming の アドレス空間 で扱う管理項目です（第三十観点）。第三十観点 TCBやSRBなどの実行単位がCPUサービスを受ける順序を示す数値という説明を操作結果と照合します（第三十観点）。第三十観点 SYSPRINT、SETPROG APF後のCSV410I表示、定義メンバーを照合し、SMF記録欠落の早期検出を確認します（第三十観点）。第三十観点 証跡には資料IDと確認値を併記し、zOSSP記録030として保存します（第三十観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第三十証跡です。ディスパッチ優先順位 の表示とメッセージIDを比べます。確認観点は DP、状態確認、運用確認 です。SMF記録欠落の早期検出を満たす記録方法として、表示値と定義を結ぶものはどれか。</p><ul class="kb-choices"><li>A. SAF連携 の一般メモを採り、SYSPRINT、メッセージID、時刻の対応を記録外に置き、zOSSP誤記030として調査範囲を狭める。</li><li>B. ディスパッチ優先順位 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延030として扱う。</li><li>C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在030として残す。</li><li>D. SETPROG APF後のCSV410I表示 と SYSPRINT を同一票へ記録し、DP を zOSSP正030で確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第三十観点 正答根拠: Dは SETPROG APF後のCSV410I表示 と SYSPRINT を結び付けるため、対象システムの取り違えを防げます（第三十観点）。第三十観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第三十観点）。第三十観点 誤答点検: Aはシステム名欠落、Bは定義未確認、Cは時刻差の欠落が理由です（第三十観点）。第三十観点 初出定義: PSWは実行状態を示す語です（第三十観点）。第三十観点 SVCは監視プログラム呼出しです（第三十観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ディスパッチ優先順位 状態確認 運用確認030</strong></p><p>検証目的: ディスパッチ優先順位 の 状態確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: IPCS / dump analysis</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により ディスパッチ優先順位 の値を確認し、対象の現在値を固定する。
［操作（入力）］
IPCS option 6
COMMAND ===&gt; VERBX LOGDATA
→ Enter を押す
［画面・出力］
LOGDATA VERBEXIT PROCESSING
LOGREC BUFFER RECORDS LOCATED
EREP DETAIL EDIT REPORT FOLLOWS
画面・出力には LOGDATA が含まれる。LOGDATA を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により ディスパッチ優先順位 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.30.06 TRACE DISPLAY 199
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON MT=(ON,024K)
画面・出力には IEE843I が含まれる。IEE843I を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により ディスパッチ優先順位 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
IPCS command line
COMMAND ===&gt; STATUS CPU
→ Enter を押す
［画面・出力］
IPCS STATUS CPU
PSW=070C1000 81234567  ASID=0010
CURRENT TCB ADDRESS SYSPRINT
画面・出力には ASID=0010 が含まれる。ASID=0010 を読み取り、SMF記録欠落の早期検出のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LOGDATA が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE843I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ASID=0010 が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


## システム出口


<section class="kb-item" id="c38-i0257"><h3>CSV410I 優先順位確認 運用確認049</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 中級</p><p>第四十九観点 システム出口 で CSV410I は 優先順位確認 の対象です（第四十九観点）。第四十九観点 確認時には APFリストへデータセットを追加または削除したことを示すメッセージという性質を前提にします（第四十九観点）。第四十九観点 D PROG,APF のCSV450I表示 と DUMPIN を同じ証跡に置き、オペレーター応答漏れの防止を管理します（第四十九観点）。第四十九観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録049から再現します（第四十九観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第四十九証跡です。D PROG,APF のCSV450I表示 と DUMPIN の対応を確認します。確認観点は CSV410I、優先順位確認、運用確認 です。DUMPIN を根拠として残す時、対象の取り違えを抑える対応はどれか。</p><ul class="kb-choices"><li>A. D PROG,APF のCSV450I表示 と DUMPIN を同一票へ記録し、CSV410I を zOSSP正049で確定する。 <span class="kb-ok">✅ 正解</span></li><li>B. Cross Memory の一般メモを採り、DUMPIN、メッセージID、時刻の対応を記録外に置き、zOSSP誤記049として調査範囲を狭める。</li><li>C. CSV410I の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延049として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在049として残す。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第四十九観点 正解確認: Aは CSV410I と DUMPIN を同じ証跡で扱うため、後続の照合に使えます（第四十九観点）。第四十九観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第四十九観点）。第四十九観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第四十九観点）。第四十九観点 用語確認: APFは許可ライブラリーの管理機能です（第四十九観点）。第四十九観点 PROGxxは動的なプログラム管理指定です（第四十九観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CSV410I 優先順位確認 運用確認049</strong></p><p>検証目的: CSV410I の 優先順位確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SDSF LOG</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により CSV410I の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 05.18.01 PROG,APF DISPLAY 948
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   2  MPRES1 SYS1.SVCLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により CSV410I の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SETPROG APF,ADD,DSNAME=MYPROG.LOADLIB,VOLUME=MPRES3
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
画面・出力には CSV410I が含まれる。CSV410I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により CSV410I の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF,ENTRY=(1-5)
→ Enter を押す
［画面・出力］
CSV450I 05.26.01 PROG,APF DISPLAY 958
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   5  MPRES1 ISF.SISFLPA
画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0258"><h3>IEE252I 優先順位確認 運用確認099</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 上級</p><p>第九十九観点 システム出口 の運用では IEE252I を表示、定義、証跡で確認します（第九十九観点）。第九十九観点 役割は SETコマンドで指定したparmlibメンバーを検出したことを示すメという範囲です（第九十九観点）。第九十九観点 D PROG,APF のCSV450I表示 の値を SYS1.PARMLIB(SMFSP) と合わせ、オペレーター応答漏れの防止を記録します（第九十九観点）。第九十九観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録099に残します（第九十九観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IEE252I 優先順位確認 運用確認099</strong></p><p>検証目的: IEE252I の 優先順位確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / GRS</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IEE252I の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS
→ Enter を押す
［画面・出力］
ISG343I 10.27.03 GRS STATUS 848
SYSTEM    STATE               SYSTEM    STATE
SC65      CONNECTED           SC63      CONNECTED
GRS STAR MODE INFORMATION
画面・出力には ISG343I が含まれる。ISG343I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IEE252I の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS,RNL=INCL
→ Enter を押す
［画面・出力］
ISG343I 10.28.03 GRS STATUS 858
RNL=INCL
QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IEE252I の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D XCF,STR,STRNAME=ISGLOCK
→ Enter を押す
［画面・出力］
IXC360I 10.29.03 DISPLAY XCF 868
STRUCTURE NAME: ISGLOCK
STATUS: ALLOCATED IN CFRM POLICY
画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0259"><h3>WLMゴールモード 権限確認 運用確認082</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 中級</p><p>第八十二観点 WLMゴールモード は z/OS System Programming の システム出口 で扱う管理項目です（第八十二観点）。第八十二観点 サービスクラス目標に基づいて作業の優先度と資源配分を管理する運用方式という説明を操作結果と照合します（第八十二観点）。第八十二観点 SYS1.SVCLIB、DISPLAY GRS のISG343I表示、定義メンバーを照合し、アドレス空間分離の確認を確認します（第八十二観点）。第八十二観点 証跡には資料IDと確認値を併記し、zOSSP記録082として保存します（第八十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第八十二証跡です。WLMゴールモード に関する設定変更を扱います。確認観点は WLMゴールモード、権限確認、運用確認 です。アドレス空間分離の確認のために、DISPLAY GRS のISG343I表示 を使った運用記録として最も適切な扱いはどれか。</p><ul class="kb-choices"><li>A. DISPLAY GRS のISG343I表示 と SYS1.SVCLIB を同一票へ記録し、WLMゴールモード を zOSSP正082で確定する。 <span class="kb-ok">✅ 正解</span></li><li>B. WTOメッセージ の一般メモを採り、SYS1.SVCLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記082として調査範囲を狭める。</li><li>C. WLMゴールモード の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延082として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在082として残す。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第八十二観点 正答根拠: Aは DISPLAY GRS のISG343I表示 と SYS1.SVCLIB を結び付けるため、対象システムの取り違えを防げます（第八十二観点）。第八十二観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第八十二観点）。第八十二観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第八十二観点）。第八十二観点 用語説明: WTOは通知メッセージです（第八十二観点）。第八十二観点 WTORは応答を求めるメッセージです（第八十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WLMゴールモード 権限確認 運用確認082</strong></p><p>検証目的: WLMゴールモード の 権限確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / parmlib review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により WLMゴールモード の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(PROGSP)
→ Enter を押す
［画面・出力］
APF FORMAT(DYNAMIC)
APF ADD DSNAME(MYPROG.LOADLIB) VOLUME(MPRES3)
LPA ADD MODNAME(MOD10) DSNAME(SYS1.LPALIB)
画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により WLMゴールモード の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SET PROG=SP
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE252I が含まれる。IEE252I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により WLMゴールモード の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 06.10.10 PROG,APF DISPLAY 881
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
  12  MPRES3 MYPROG.LOADLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0260"><h3>アドレス空間 権限確認 運用確認032</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 中級</p><p>第三十二観点 z/OS System Programming の システム出口 では アドレス空間 を障害調査で照合します（第三十二観点）。第三十二観点 資料上は プログラムとデータを他の利用者領域から分離して管理する仮想記憶単位として扱います（第三十二観点）。第三十二観点 ASID=0010 を起点に表示値を戻し、アドレス空間分離の確認を点検します（第三十二観点）。第三十二観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録032へ書きます（第三十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第三十二証跡です。アドレス空間 に関する設定変更を扱います。確認観点は アドレス空間、権限確認、運用確認 です。メッセージID、定義メンバー、表示出力を同じ確認票に置く対応として適切なものはどれか。</p><ul class="kb-choices"><li>A. LOGREC診断 の一般メモを採り、ASID=0010、メッセージID、時刻の対応を記録外に置き、zOSSP誤記032として調査範囲を狭める。</li><li>B. DISPLAY GRS のISG343I表示 と ASID=0010 を同一票へ記録し、アドレス空間 を zOSSP正032で確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. アドレス空間 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延032として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在032として残す。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第三十二観点 照合結果: Bは ASID=0010 をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第三十二観点）。第三十二観点 操作背景: WTOとWTORはオペレーター通知と応答をコンソールログへ残します（第三十二観点）。第三十二観点 誤答確認: Aは ASID=0010 未追跡、Cはコマンド確認不足、Dは別システム混同が理由です（第三十二観点）。第三十二観点 用語補足: ENQは資源を直列化します（第三十二観点）。第三十二観点 DEQは取得した資源を解放します（第三十二観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>アドレス空間 権限確認 運用確認032</strong></p><p>検証目的: アドレス空間 の 権限確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: ISPF / SAF review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により アドレス空間 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(IEASYS08)
→ Enter を押す
［画面・出力］
IEASYS08
PROG=SP
SMF=SP
GRSRNL=SP
LNKAUTH=LNKLST
画面・出力には LNKAUTH が含まれる。LNKAUTH を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により アドレス空間 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX CSV
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
CSV450I PROG,APF DISPLAY
画面・出力には CSV410I が含まれる。CSV410I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により アドレス空間 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
SDSF LOG
COMMAND ===&gt; FILTER PREFIX IEE
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE536I が含まれる。IEE536I を読み取り、アドレス空間分離の確認のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LNKAUTH が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE536I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0261"><h3>システム出口 動的出口管理 ログとの照合 EXIT07</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 上級</p><p>ログとの照合では システム出口 の 出口一覧 を主操作として EXIT07 を判定します。時刻と対象識別子への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT07 に残します。ログとの照合を補助する 個別出口 では CSV463I を補助値として EXIT07 へ保存します。主判定のログとの照合ではシステム出口・動的出口管理の 出口一覧 から CSV460I を読み EXIT07 へ残します。証跡照合のログとの照合ではシステム出口・動的出口管理の CSV460I と CSV463I を EXIT07 に保存します。記録対応のログとの照合ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT07 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で システム出口 の 出口一覧 と 個別出口 を用い 操作とログを対応 します。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV460I で対象 EXIT07 の EXIT名とMODULE を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. CSV460Iを含む出口一覧の応答行を保存する。その応答を得るためD PROG,EXITを使用する。対象EXIT07のEXIT名とMODULEとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. D PROG,EXITが応答を返した時点で正常とする。応答中のCSV460Iの値は記録しない。CSV411IをCSV460Iと同じ判定値とみなし対象EXIT07の主証跡にする。</li><li>C. D PROG,EXITのコマンド文字列だけを記録する。CSV460Iを含む応答行は保存しない。</li><li>D. 動的出口管理の停止または再定義を実施する。その後にD PROG,EXITでCSV460Iを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 適切な判定: Aは出口一覧で CSV460I を読みEXIT名とMODULEの主値として操作とログを対応しEXIT07に残します。
機能の仕組み: ログとの照合では個別出口を補助操作とし動的出口管理の時刻と対象識別子をCSV463Iと対象EXIT07で照合します。
各候補の評価: 出口一覧と個別出口の役割を分けるとA: CSV460Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではEXIT名とMODULEを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではEXIT名とMODULEを証明できない点でEXIT名とMODULEを確認できません、D: 変更前のEXIT名とMODULEを失う点で個別出口の範囲を越えます。結論としてログとの照合のシステム出口・動的出口管理で判定する対象は EXIT07 です。
用語の定義: ログとの照合で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT07へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システム出口 動的出口管理 ログとの照合 EXIT07</strong></p><p>検証目的: システム出口の動的出口管理について操作とログを対応し、EXIT07のEXIT名とMODULEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT07の出口一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT
→ Enter を押す
［画面・出力］
CSV460I EXIT DISPLAY EXITNAME EXIT07 MODULE MOD07 STATE ACTIVE
画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT07を指定し、EXIT07の個別出口を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT,EX=EXIT07
→ Enter を押す
［画面・出力］
CSV463I EXIT EXIT07 MODULE MOD07 STATE ACTIVE ABENDNUM 0
画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD07を指定し、EXIT07のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=MOD07
→ Enter を押す
［画面・出力］
CSV411I MODULE MOD07 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV460I が画面・出力に表示されること
② ステップ2 の CSV463I が画面・出力に表示されること
③ ステップ3 の CSV411I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0262"><h3>システム出口 動的出口管理 代替経路の確認 EXIT10</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 上級</p><p>代替経路の確認では システム出口 の 出口一覧 を主操作として EXIT10 を判定します。主経路との役割差への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT10 に残します。代替経路の確認を補助する 個別出口 では CSV463I を補助値として EXIT10 へ保存します。主判定の代替経路の確認ではシステム出口・動的出口管理の 出口一覧 から CSV460I を読み EXIT10 へ残します。証跡照合の代替経路の確認ではシステム出口・動的出口管理の CSV460I と CSV463I を EXIT10 に保存します。記録対応の代替経路の確認ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT10 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で システム出口 の 出口一覧 と 個別出口 の役割を分け 主経路との役割差 を調べます。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。対象 EXIT10 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. D PROG,EXITのコマンド文字列だけを記録する。CSV460Iを含む応答行は保存しない。</li><li>B. 動的出口管理の停止または再定義を実施する。その後にD PROG,EXITでCSV460Iを採取する。</li><li>C. APF管理のDSNAMEとVOLSERを確認する。その値をシステム出口のEXIT10にも適用する。</li><li>D. D PROG,EXITとD PROG,EXIT,EX=EXIT10の対象名をそろえる。前者のCSV460IをEXIT名とMODULEの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい判定結果: Dは出口一覧で CSV460I を読みEXIT名とMODULEの主値として代替手段の成立を確認しEXIT10に残します。
運用上の背景: 代替経路の確認では個別出口を補助操作とし動的出口管理の主経路との役割差をCSV463Iと対象EXIT10で照合します。
候補別の検討: 出口一覧と個別出口の役割を分けるとA: 入力記録だけではEXIT名とMODULEを証明できない点で一次資料と一致しません、B: 変更前のEXIT名とMODULEを失う点でEXIT名とMODULEを確認できません、C: APF管理の値ではCSV460Iを確認できない点で個別出口の範囲を越えます、D: 同じ対象名のCSV460Iを採用する点で現在値を示します。結論として代替経路の確認のシステム出口・動的出口管理で判定する対象は EXIT10 です。
重要用語の定義: 代替経路の確認で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT10へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システム出口 動的出口管理 代替経路の確認 EXIT10</strong></p><p>検証目的: システム出口の動的出口管理について代替手段の成立を確認し、EXIT10のEXIT名とMODULEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT10の出口一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT
→ Enter を押す
［画面・出力］
CSV460I EXIT DISPLAY EXITNAME EXIT10 MODULE MOD10 STATE ACTIVE
画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT10を指定し、EXIT10の個別出口を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT,EX=EXIT10
→ Enter を押す
［画面・出力］
CSV463I EXIT EXIT10 MODULE MOD10 STATE ACTIVE ABENDNUM 0
画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD10を指定し、EXIT10のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=MOD10
→ Enter を押す
［画面・出力］
CSV411I MODULE MOD10 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV460I が画面・出力に表示されること
② ステップ2 の CSV463I が画面・出力に表示されること
③ ステップ3 の CSV411I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0263"><h3>システム出口 動的出口管理 変更前の確認 EXIT02</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 上級</p><p>変更前の確認では システム出口 の 個別出口 を主操作として EXIT02 を判定します。変更対象と非対象の境界への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT02 に残します。変更前の確認を補助する モジュール所在 では CSV411I を補助値として EXIT02 へ保存します。主判定の変更前の確認ではシステム出口・動的出口管理の 個別出口 から CSV463I を読み EXIT02 へ残します。証跡照合の変更前の確認ではシステム出口・動的出口管理の CSV463I と CSV411I を EXIT02 に保存します。記録対応の変更前の確認ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT02 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で システム出口 の 個別出口 と モジュール所在 を照合し 変更対象と非対象の境界 を確かめます。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV463I を読む前に対象 EXIT02 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. D PROG,EXIT,EX=EXIT02を対象名なしで実行する。一覧の先頭行をEXIT02の結果として記録する。</li><li>B. 前回保存したD PROG,EXIT,EX=EXIT02の結果を使う。今回のD PROG,LPA,MODNAME=MOD02の結果と同一時点の証跡として比較する。</li><li>C. 保存済みのEXIT02の出力を再利用する。今回のD PROG,EXIT,EX=EXIT02とD PROG,LPA,MODNAME=MOD02は実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象EXIT02についてD PROG,EXIT,EX=EXIT02の応答からCSV463Iを確認する。D PROG,LPA,MODNAME=MOD02は補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用理由: Dは個別出口で CSV463I を読みEXIT名とMODULEの主値として変更前の証跡を保存しEXIT02に残します。
動作の背景: 変更前の確認ではモジュール所在を補助操作とし動的出口管理の変更対象と非対象の境界をCSV411Iと対象EXIT02で照合します。
各選択肢の検討: 個別出口とモジュール所在の役割を分けるとA: 先頭行はEXIT02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点で個別出口を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でシステム出口に使いません、D: CSV463Iと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のシステム出口・動的出口管理で判定する対象は EXIT02 です。
初出用語の定義: 変更前の確認で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT02へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システム出口 動的出口管理 変更前の確認 EXIT02</strong></p><p>検証目的: システム出口の動的出口管理について変更前の証跡を保存し、EXIT02のEXIT名とMODULEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT02を指定し、EXIT02の個別出口を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT,EX=EXIT02
→ Enter を押す
［画面・出力］
CSV463I EXIT EXIT02 MODULE MOD02 STATE ACTIVE ABENDNUM 0
画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD02を指定し、EXIT02のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=MOD02
→ Enter を押す
［画面・出力］
CSV411I MODULE MOD02 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT02の出口一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT
→ Enter を押す
［画面・出力］
CSV460I EXIT DISPLAY EXITNAME EXIT02 MODULE MOD02 STATE ACTIVE
画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV463I が画面・出力に表示されること
② ステップ2 の CSV411I が画面・出力に表示されること
③ ステップ3 の CSV460I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0264"><h3>システム出口 動的出口管理 変更後の確認 EXIT03</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 上級</p><p>変更後の確認では システム出口 の モジュール所在 を主操作として EXIT03 を判定します。反映値と残存値への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT03 に残します。変更後の確認を補助する 出口一覧 では CSV460I を補助値として EXIT03 へ保存します。主判定の変更後の確認ではシステム出口・動的出口管理の モジュール所在 から CSV411I を読み EXIT03 へ残します。証跡照合の変更後の確認ではシステム出口・動的出口管理の CSV411I と CSV460I を EXIT03 に保存します。記録対応の変更後の確認ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT03 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で システム出口 の モジュール所在 と 出口一覧 を組み合わせる際は 動的出口管理 が出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能という仕組みを前提にします。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV411I と EXIT名とMODULE を対象 EXIT03 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. D PROG,EXITで周辺状態を押さえる。その後にD PROG,LPA,MODNAME=MOD03でCSV411Iを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. 動的出口管理の停止または再定義を実施する。その後にD PROG,LPA,MODNAME=MOD03でCSV411Iを採取する。</li><li>C. SAF連携のSAF RCとRACF RCを確認する。その値をシステム出口のEXIT03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>D. D PROG,EXITが成功したためD PROG,LPA,MODNAME=MOD03のCSV411Iも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答の根拠: Aはモジュール所在で CSV411I を読みEXIT名とMODULEの主値として変更結果を検証しEXIT03に残します。
内部の仕組み: 変更後の確認では出口一覧を補助操作とし動的出口管理の反映値と残存値をCSV460Iと対象EXIT03で照合します。
誤答を含む比較: モジュール所在と出口一覧の役割を分けるとA: 周辺状態の後にCSV411Iを確認する点でEXIT03を判定できます、B: 変更前のEXIT名とMODULEを失う点で出口一覧の範囲を越えます、C: SAF連携の値ではCSV411Iを確認できないうえに追加前提も不正な点でEXIT03の値を示しません、D: 補助操作の成功ではCSV411Iを確定できない点で変更後の確認に合いません。結論として変更後の確認のシステム出口・動的出口管理で判定する対象は EXIT03 です。
用語定義: 変更後の確認で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT03へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システム出口 動的出口管理 変更後の確認 EXIT03</strong></p><p>検証目的: システム出口の動的出口管理について変更結果を検証し、EXIT03のEXIT名とMODULEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD03を指定し、EXIT03のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=MOD03
→ Enter を押す
［画面・出力］
CSV411I MODULE MOD03 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT03の出口一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT
→ Enter を押す
［画面・出力］
CSV460I EXIT DISPLAY EXITNAME EXIT03 MODULE MOD03 STATE ACTIVE
画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT03を指定し、EXIT03の個別出口を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT,EX=EXIT03
→ Enter を押す
［画面・出力］
CSV463I EXIT EXIT03 MODULE MOD03 STATE ACTIVE ABENDNUM 0
画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV411I が画面・出力に表示されること
② ステップ2 の CSV460I が画面・出力に表示されること
③ ステップ3 の CSV463I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0265"><h3>システム出口 動的出口管理 引継ぎ記録 EXIT09</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 上級</p><p>引継ぎ記録では システム出口 の モジュール所在 を主操作として EXIT09 を判定します。次担当者が追跡できる証跡への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT09 に残します。引継ぎ記録を補助する 出口一覧 では CSV460I を補助値として EXIT09 へ保存します。主判定の引継ぎ記録ではシステム出口・動的出口管理の モジュール所在 から CSV411I を読み EXIT09 へ残します。証跡照合の引継ぎ記録ではシステム出口・動的出口管理の CSV411I と CSV460I を EXIT09 に保存します。記録対応の引継ぎ記録ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT09 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で システム出口 の モジュール所在 と 出口一覧 を組み合わせる際は 動的出口管理 が出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能という仕組みを前提にします。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV411I と EXIT名とMODULE を対象 EXIT09 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. D PROG,EXITが成功したためD PROG,LPA,MODNAME=MOD09のCSV411Iも正常だと推定する。主出力は保存しない。</li><li>B. D PROG,LPA,MODNAME=MOD09を対象名なしで実行する。一覧の先頭行をEXIT09の結果として記録する。</li><li>C. 対象名EXIT09を指定してD PROG,LPA,MODNAME=MOD09を実行する。応答中のCSV411Iと時刻を保存する。D PROG,EXITで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したD PROG,LPA,MODNAME=MOD09の結果を使う。今回のD PROG,EXITの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用操作の理由: Cはモジュール所在で CSV411I を読みEXIT名とMODULEの主値として再現可能な記録を作成しEXIT09に残します。
製品内の仕組み: 引継ぎ記録では出口一覧を補助操作とし動的出口管理の次担当者が追跡できる証跡をCSV460Iと対象EXIT09で照合します。
選択肢別の説明: モジュール所在と出口一覧の役割を分けるとA: 補助操作の成功ではCSV411Iを確定できない点でEXIT09の値を示しません、B: 先頭行はEXIT09と確定できない点で引継ぎ記録に合いません、C: CSV411Iと時刻を保存する点でモジュール所在に合います、D: 採取時刻が異なる点でシステム出口に使いません。結論として引継ぎ記録のシステム出口・動的出口管理で判定する対象は EXIT09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT09へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システム出口 動的出口管理 引継ぎ記録 EXIT09</strong></p><p>検証目的: システム出口の動的出口管理について再現可能な記録を作成し、EXIT09のEXIT名とMODULEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD09を指定し、EXIT09のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=MOD09
→ Enter を押す
［画面・出力］
CSV411I MODULE MOD09 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT09の出口一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT
→ Enter を押す
［画面・出力］
CSV460I EXIT DISPLAY EXITNAME EXIT09 MODULE MOD09 STATE ACTIVE
画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT09を指定し、EXIT09の個別出口を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT,EX=EXIT09
→ Enter を押す
［画面・出力］
CSV463I EXIT EXIT09 MODULE MOD09 STATE ACTIVE ABENDNUM 0
画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV411I が画面・出力に表示されること
② ステップ2 の CSV460I が画面・出力に表示されること
③ ステップ3 の CSV463I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0266"><h3>システム出口 動的出口管理 復旧後の確認 EXIT06</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 上級</p><p>復旧後の確認では システム出口 の モジュール所在 を主操作として EXIT06 を判定します。再発していないことを示す値への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT06 に残します。復旧後の確認を補助する 出口一覧 では CSV460I を補助値として EXIT06 へ保存します。主判定の復旧後の確認ではシステム出口・動的出口管理の モジュール所在 から CSV411I を読み EXIT06 へ残します。証跡照合の復旧後の確認ではシステム出口・動的出口管理の CSV411I と CSV460I を EXIT06 に保存します。記録対応の復旧後の確認ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT06 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で システム出口 の モジュール所在 と 出口一覧 を実施し 動的出口管理 の役割を確認します。旧出口を残したまま新版を追加して二重処理を起こす危険があります。対象 EXIT06 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. Cross MemoryのHOME ASIDとSECONDARY ASIDを確認する。その値をシステム出口のEXIT06にも適用する。</li><li>B. D PROG,EXITが成功したためD PROG,LPA,MODNAME=MOD06のCSV411Iも正常だと推定する。主出力は保存しない。別資源で得た状態を対象EXIT06へ引き継げるものとする。動的出口管理の再発していないことを示す値は確認済みとして扱う。さらにD PROG,EXIT,EX=EXIT06のCSV463IをCSV411Iと同種の値として併記する。</li><li>C. D PROG,LPA,MODNAME=MOD06を対象名なしで実行する。一覧の先頭行をEXIT06の結果として記録する。</li><li>D. D PROG,LPA,MODNAME=MOD06でCSV411Iを取得してからD PROG,EXIT,EX=EXIT06でCSV463Iを照合する。EXIT06のEXIT名とMODULEを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答内容: Dはモジュール所在で CSV411I を読みEXIT名とMODULEの主値として復旧後の安定性を確認しEXIT06に残します。
構成上の背景: 復旧後の確認では出口一覧を補助操作とし動的出口管理の再発していないことを示す値をCSV460Iと対象EXIT06で照合します。
候補ごとの理由: モジュール所在と出口一覧の役割を分けるとA: Cross Memoryの値ではCSV411Iを確認できない点で出口一覧の範囲を越えます、B: 補助操作の成功ではCSV411Iを確定できないうえに追加前提も不正な点でEXIT06の値を示しません、C: 先頭行はEXIT06と確定できない点で復旧後の確認に合いません、D: CSV411IとCSV463Iを順に照合する点でモジュール所在に合います。結論として復旧後の確認のシステム出口・動的出口管理で判定する対象は EXIT06 です。
初出用語: 復旧後の確認で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT06へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システム出口 動的出口管理 復旧後の確認 EXIT06</strong></p><p>検証目的: システム出口の動的出口管理について復旧後の安定性を確認し、EXIT06のEXIT名とMODULEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD06を指定し、EXIT06のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=MOD06
→ Enter を押す
［画面・出力］
CSV411I MODULE MOD06 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT06の出口一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT
→ Enter を押す
［画面・出力］
CSV460I EXIT DISPLAY EXITNAME EXIT06 MODULE MOD06 STATE ACTIVE
画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT06を指定し、EXIT06の個別出口を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT,EX=EXIT06
→ Enter を押す
［画面・出力］
CSV463I EXIT EXIT06 MODULE MOD06 STATE ACTIVE ABENDNUM 0
画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV411I が画面・出力に表示されること
② ステップ2 の CSV460I が画面・出力に表示されること
③ ステップ3 の CSV463I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0267"><h3>システム出口 動的出口管理 復旧準備 EXIT05</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 上級</p><p>復旧準備では システム出口 の 個別出口 を主操作として EXIT05 を判定します。再開前に必要な整合性への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT05 に残します。復旧準備を補助する モジュール所在 では CSV411I を補助値として EXIT05 へ保存します。主判定の復旧準備ではシステム出口・動的出口管理の 個別出口 から CSV463I を読み EXIT05 へ残します。証跡照合の復旧準備ではシステム出口・動的出口管理の CSV463I と CSV411I を EXIT05 に保存します。記録対応の復旧準備ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT05 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で システム出口 の 個別出口 と モジュール所在 を使い 復旧条件を確認 します。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV463I を読み対象 EXIT05 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. 前回保存したD PROG,EXIT,EX=EXIT05の結果を使う。今回のD PROG,LPA,MODNAME=MOD05の結果と同一時点の証跡として比較する。</li><li>B. 保存済みのEXIT05の出力を再利用する。今回のD PROG,EXIT,EX=EXIT05とD PROG,LPA,MODNAME=MOD05は実行済みとして扱う。</li><li>C. 変更を加えずD PROG,EXIT,EX=EXIT05を実行する。CSV463Iを保存する。差分はD PROG,LPA,MODNAME=MOD05の結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. D PROG,LPA,MODNAME=MOD05のCSV411IをEXIT名とMODULEの主判定に採用する。D PROG,EXIT,EX=EXIT05の応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 選定理由: Cは個別出口で CSV463I を読みEXIT名とMODULEの主値として復旧条件を確認しEXIT05に残します。
処理の仕組み: 復旧準備ではモジュール所在を補助操作とし動的出口管理の再開前に必要な整合性をCSV411Iと対象EXIT05で照合します。
選択結果の内訳: 個別出口とモジュール所在の役割を分けるとA: 採取時刻が異なる点で個別出口を代替しません、B: 過去出力では今回の復旧準備を示せない点でシステム出口に使いません、C: 変更前のCSV463Iを保存する点で正答です、D: CSV411IはCSV463Iを代替しないうえに追加前提も不正な点でEXIT05を採用できません。結論として復旧準備のシステム出口・動的出口管理で判定する対象は EXIT05 です。
用語の説明: 復旧準備で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT05へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システム出口 動的出口管理 復旧準備 EXIT05</strong></p><p>検証目的: システム出口の動的出口管理について復旧条件を確認し、EXIT05のEXIT名とMODULEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT05を指定し、EXIT05の個別出口を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT,EX=EXIT05
→ Enter を押す
［画面・出力］
CSV463I EXIT EXIT05 MODULE MOD05 STATE ACTIVE ABENDNUM 0
画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD05を指定し、EXIT05のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=MOD05
→ Enter を押す
［画面・出力］
CSV411I MODULE MOD05 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT05の出口一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT
→ Enter を押す
［画面・出力］
CSV460I EXIT DISPLAY EXITNAME EXIT05 MODULE MOD05 STATE ACTIVE
画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV463I が画面・出力に表示されること
② ステップ2 の CSV411I が画面・出力に表示されること
③ ステップ3 の CSV460I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0268"><h3>システム出口 動的出口管理 構成監査 EXIT08</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 上級</p><p>構成監査では システム出口 の 個別出口 を主操作として EXIT08 を判定します。定義値と稼働値の一致への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT08 に残します。構成監査を補助する モジュール所在 では CSV411I を補助値として EXIT08 へ保存します。主判定の構成監査ではシステム出口・動的出口管理の 個別出口 から CSV463I を読み EXIT08 へ残します。証跡照合の構成監査ではシステム出口・動的出口管理の CSV463I と CSV411I を EXIT08 に保存します。記録対応の構成監査ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT08 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で システム出口 の 個別出口 と モジュール所在 を照合し 定義値と稼働値の一致 を確かめます。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV463I を読む前に対象 EXIT08 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのEXIT08の出力を再利用する。今回のD PROG,EXIT,EX=EXIT08とD PROG,LPA,MODNAME=MOD08は実行済みとして扱う。</li><li>B. D PROG,LPA,MODNAME=MOD08の結果だけでは確定しない。D PROG,EXIT,EX=EXIT08のCSV463Iを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. D PROG,LPA,MODNAME=MOD08のCSV411IをEXIT名とMODULEの主判定に採用する。D PROG,EXIT,EX=EXIT08の応答は採取対象から外す。</li><li>D. D PROG,EXITのCSV460IをCSV463Iと同義の成功表示として扱う。D PROG,EXIT,EX=EXIT08は実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 技術上の正答: Bは個別出口で CSV463I を読みEXIT名とMODULEの主値として構成差分を監査しEXIT08に残します。
実行時の背景: 構成監査ではモジュール所在を補助操作とし動的出口管理の定義値と稼働値の一致をCSV411Iと対象EXIT08で照合します。
四つの候補の理由: 個別出口とモジュール所在の役割を分けるとA: 過去出力では今回の構成監査を示せない点でシステム出口に使いません、B: CSV463Iを主証跡として区別する点で正答です、C: CSV411IはCSV463Iを代替しない点でEXIT08を採用できません、D: CSV460IとCSV463Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のシステム出口・動的出口管理で判定する対象は EXIT08 です。
初出語定義: 構成監査で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT08へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システム出口 動的出口管理 構成監査 EXIT08</strong></p><p>検証目的: システム出口の動的出口管理について構成差分を監査し、EXIT08のEXIT名とMODULEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT08を指定し、EXIT08の個別出口を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT,EX=EXIT08
→ Enter を押す
［画面・出力］
CSV463I EXIT EXIT08 MODULE MOD08 STATE ACTIVE ABENDNUM 0
画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD08を指定し、EXIT08のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=MOD08
→ Enter を押す
［画面・出力］
CSV411I MODULE MOD08 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT08の出口一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT
→ Enter を押す
［画面・出力］
CSV460I EXIT DISPLAY EXITNAME EXIT08 MODULE MOD08 STATE ACTIVE
画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV463I が画面・出力に表示されること
② ステップ2 の CSV411I が画面・出力に表示されること
③ ステップ3 の CSV460I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0269"><h3>システム出口 動的出口管理 通常状態の確認 EXIT01</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 上級</p><p>通常状態の確認では システム出口 の 出口一覧 を主操作として EXIT01 を判定します。基準値と現在値の差への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT01 に残します。通常状態の確認を補助する 個別出口 では CSV463I を補助値として EXIT01 へ保存します。主判定の通常状態の確認ではシステム出口・動的出口管理の 出口一覧 から CSV460I を読み EXIT01 へ残します。証跡照合の通常状態の確認ではシステム出口・動的出口管理の CSV460I と CSV463I を EXIT01 に保存します。記録対応の通常状態の確認ではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT01 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で システム出口 の 出口一覧 と 個別出口 を用い 通常状態を確定 します。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。CSV460I で対象 EXIT01 の EXIT名とMODULE を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. D PROG,EXIT,EX=EXIT01のCSV463IをEXIT名とMODULEの主判定に採用する。D PROG,EXITの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. D PROG,LPA,MODNAME=MOD01のCSV411IをCSV460Iと同義の成功表示として扱う。D PROG,EXITは実行しない。</li><li>C. D PROG,EXITを先に実行する。対象EXIT01のCSV460IをEXIT名とMODULEとして記録する。続いてD PROG,EXIT,EX=EXIT01で同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. D PROG,EXITが応答を返した時点で正常とする。応答中のCSV460Iの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正解の説明: Cは出口一覧で CSV460I を読みEXIT名とMODULEの主値として通常状態を確定しEXIT01に残します。
背景・仕組み: 通常状態の確認では個別出口を補助操作とし動的出口管理の基準値と現在値の差をCSV463Iと対象EXIT01で照合します。
選択肢の理由: 出口一覧と個別出口の役割を分けるとA: CSV463IはCSV460Iを代替しないうえに追加前提も不正な点で動的出口管理に使えません、B: CSV411IとCSV460Iは確認項目が異なる点でEXIT01を採用できません、C: CSV460Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではEXIT名とMODULEを判定できない点で一次資料と一致しません。結論として通常状態の確認のシステム出口・動的出口管理で判定する対象は EXIT01 です。
用語の初出定義: 通常状態の確認で使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT01へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システム出口 動的出口管理 通常状態の確認 EXIT01</strong></p><p>検証目的: システム出口の動的出口管理について通常状態を確定し、EXIT01のEXIT名とMODULEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT01の出口一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT
→ Enter を押す
［画面・出力］
CSV460I EXIT DISPLAY EXITNAME EXIT01 MODULE MOD01 STATE ACTIVE
画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT01を指定し、EXIT01の個別出口を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT,EX=EXIT01
→ Enter を押す
［画面・出力］
CSV463I EXIT EXIT01 MODULE MOD01 STATE ACTIVE ABENDNUM 0
画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD01を指定し、EXIT01のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=MOD01
→ Enter を押す
［画面・出力］
CSV411I MODULE MOD01 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV460I が画面・出力に表示されること
② ステップ2 の CSV463I が画面・出力に表示されること
③ ステップ3 の CSV411I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0270"><h3>システム出口 動的出口管理 障害切り分け EXIT04</h3><p class="kb-meta">分類: システム出口 ・ 難易度: 上級</p><p>障害切り分けでは システム出口 の 出口一覧 を主操作として EXIT04 を判定します。最初に失敗した処理への注意として「旧出口を残したまま新版を追加して二重処理を起こす危険があります」を EXIT04 に残します。障害切り分けを補助する 個別出口 では CSV463I を補助値として EXIT04 へ保存します。主判定の障害切り分けではシステム出口・動的出口管理の 出口一覧 から CSV460I を読み EXIT04 へ残します。証跡照合の障害切り分けではシステム出口・動的出口管理の CSV460I と CSV463I を EXIT04 に保存します。記録対応の障害切り分けではシステム出口・動的出口管理の EXIT名とMODULE の証跡へ EXIT04 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで システム出口 の 出口一覧 と 個別出口 の役割を分け 最初に失敗した処理 を調べます。動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能です。旧出口を残したまま新版を追加して二重処理を起こす危険があります。対象 EXIT04 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. D PROG,LPA,MODNAME=MOD04のCSV411IをCSV460Iと同義の成功表示として扱う。D PROG,EXITは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. D PROG,EXITの出力でEXIT04とCSV460Iが同じ応答にあることを確認する。EXIT名とMODULEをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. D PROG,EXITが応答を返した時点で正常とする。応答中のCSV460Iの値は記録しない。</li><li>D. D PROG,EXITのコマンド文字列だけを記録する。CSV460Iを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい操作の説明: Bは出口一覧で CSV460I を読みEXIT名とMODULEの主値として障害範囲を限定しEXIT04に残します。
技術的背景: 障害切り分けでは個別出口を補助操作とし動的出口管理の最初に失敗した処理をCSV463Iと対象EXIT04で照合します。
四択の評価: 出口一覧と個別出口の役割を分けるとA: CSV411IとCSV460Iは確認項目が異なるうえに追加前提も不正な点でEXIT04を採用できません、B: EXIT04とCSV460Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではEXIT名とMODULEを判定できない点で一次資料と一致しません、D: 入力記録だけではEXIT名とMODULEを証明できない点でEXIT名とMODULEを確認できません。結論として障害切り分けのシステム出口・動的出口管理で判定する対象は EXIT04 です。
初出語の意味: 障害切り分けで使う 動的出口管理 は出口名と出口ルーチンをPROGxxまたはSETPROGで登録し、呼出し順と有効状態を管理する機能を表しEXIT名とMODULEを判定する際にEXIT04へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>システム出口 動的出口管理 障害切り分け EXIT04</strong></p><p>検証目的: システム出口の動的出口管理について障害範囲を限定し、EXIT04のEXIT名とMODULEを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象EXIT04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXITを指定し、EXIT04の出口一覧を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT
→ Enter を押す
［画面・出力］
CSV460I EXIT DISPLAY EXITNAME EXIT04 MODULE MOD04 STATE ACTIVE
画面・出力にあるCSV460Iを読み、EXIT名とMODULEと対象EXIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,EXIT,EX=EXIT04を指定し、EXIT04の個別出口を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,EXIT,EX=EXIT04
→ Enter を押す
［画面・出力］
CSV463I EXIT EXIT04 MODULE MOD04 STATE ACTIVE ABENDNUM 0
画面・出力にあるCSV463Iを読み、EXIT名とMODULEと対象EXIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのシステム出口を確認する入力画面です。COMMAND入力口へD PROG,LPA,MODNAME=MOD04を指定し、EXIT04のモジュール所在を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D PROG,LPA,MODNAME=MOD04
→ Enter を押す
［画面・出力］
CSV411I MODULE MOD04 FOUND IN LPA DATASET SYS1.LPALIB
画面・出力にあるCSV411Iを読み、EXIT名とMODULEと対象EXIT04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の CSV460I が画面・出力に表示されること
② ステップ2 の CSV463I が画面・出力に表示されること
③ ステップ3 の CSV411I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


## ディスパッチ制御


<section class="kb-item" id="c38-i0271"><h3>FLIH処理 ストレージ確認 運用確認078</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>第七十八観点 FLIH処理 は z/OS System Programming の ディスパッチ制御 で扱う管理項目です（第七十八観点）。第七十八観点 割り込みを受け、PSWやレジスター状態を保存して適切な処理へ渡す入口という説明を操作結果と照合します（第七十八観点）。第七十八観点 SYS1.PARMLIB(PROGSP)、parmlibメンバーの該当ステートメント、定義メンバーを照合し、診断ログの再現性確保を確認します（第七十八観点）。第七十八観点 証跡には資料IDと確認値を併記し、zOSSP記録078として保存します（第七十八観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第七十八証跡です。FLIH処理 の記録を監査用に整えます。確認観点は FLIH処理、ストレージ確認、運用確認 です。診断ログの再現性確保を満たす記録方法として、表示値と定義を結ぶものはどれか。</p><ul class="kb-choices"><li>A. SMF記録 の一般メモを採り、SYS1.PARMLIB(PROGSP)、メッセージID、時刻の対応を記録外に置き、zOSSP誤記078として調査範囲を狭める。</li><li>B. FLIH処理 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延078として扱う。</li><li>C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在078として残す。</li><li>D. parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を同一票へ記録し、FLIH処理 を zOSSP正078で確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第七十八観点 正答根拠: Dは parmlibメンバーの該当ステートメント と SYS1.PARMLIB(PROGSP) を結び付けるため、対象システムの取り違えを防げます（第七十八観点）。第七十八観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第七十八観点）。第七十八観点 誤答点検: Aはシステム名欠落、Bは定義未確認、Cは時刻差の欠落が理由です（第七十八観点）。第七十八観点 初出定義: PSWは実行状態を示す語です（第七十八観点）。第七十八観点 SVCは監視プログラム呼出しです（第七十八観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FLIH処理 ストレージ確認 運用確認078</strong></p><p>検証目的: FLIH処理 の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: IPCS / dump analysis</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により FLIH処理 の値を確認し、対象の現在値を固定する。
［操作（入力）］
IPCS option 6
COMMAND ===&gt; VERBX LOGDATA
→ Enter を押す
［画面・出力］
LOGDATA VERBEXIT PROCESSING
LOGREC BUFFER RECORDS LOCATED
EREP DETAIL EDIT REPORT FOLLOWS
画面・出力には LOGDATA が含まれる。LOGDATA を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により FLIH処理 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.30.06 TRACE DISPLAY 177
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON MT=(ON,024K)
画面・出力には IEE843I が含まれる。IEE843I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により FLIH処理 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
IPCS command line
COMMAND ===&gt; STATUS CPU
→ Enter を押す
［画面・出力］
IPCS STATUS CPU
PSW=070C1000 81234567  ASID=0010
CURRENT TCB ADDRESS SYS1.PARMLIB(PROGSP)
画面・出力には ASID=0010 が含まれる。ASID=0010 を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: LOGDATA が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE843I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ASID=0010 が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0272"><h3>IEFU29出口 定義照合 運用確認061</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>第六十一観点 ディスパッチ制御 で IEFU29出口 は 定義照合 の対象です（第六十一観点）。第六十一観点 確認時には SMF記録データセットが満杯になった時にダンプ処理へつなぐ出口という性質を前提にします（第六十一観点）。第六十一観点 SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同じ証跡に置き、共通ストレージ変更の記録を管理します（第六十一観点）。第六十一観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録061から再現します（第六十一観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第六十一証跡です。ディスパッチ制御 の運用で IEFU29出口 を点検します。確認観点は IEFU29出口、定義照合、運用確認 です。SYS1.LINKLIB を根拠として残す時、対象の取り違えを抑える対応はどれか。</p><ul class="kb-choices"><li>A. SET PROG=xx後のIEE252I表示 と SYS1.LINKLIB を同一票へ記録し、IEFU29出口 を zOSSP正061で確定する。 <span class="kb-ok">✅ 正解</span></li><li>B. ENQ資源管理 の一般メモを採り、SYS1.LINKLIB、メッセージID、時刻の対応を記録外に置き、zOSSP誤記061として調査範囲を狭める。</li><li>C. IEFU29出口 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延061として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在061として残す。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第六十一観点 正解確認: Aは IEFU29出口 と SYS1.LINKLIB を同じ証跡で扱うため、後続の照合に使えます（第六十一観点）。第六十一観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第六十一観点）。第六十一観点 誤答比較: Bは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第六十一観点）。第六十一観点 用語確認: APFは許可ライブラリーの管理機能です（第六十一観点）。第六十一観点 PROGxxは動的なプログラム管理指定です（第六十一観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IEFU29出口 定義照合 運用確認061</strong></p><p>検証目的: IEFU29出口 の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / operations</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IEFU29出口 の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY R,ALL
→ Enter を押す
［画面・出力］
IEE112I 11.15.13 DISPLAY R 760
REPLY ID   MESSAGE TEXT
005        IEA793A SPECIFY DUMP OPTION FOR SYS1.LINKLIB
画面・出力には IEE112I が含まれる。IEE112I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IEFU29出口 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D C
→ Enter を押す
［画面・出力］
IEE889I 15.33.13 CONSOLE DISPLAY 490
MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
画面・出力には IEE889I が含まれる。IEE889I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IEFU29出口 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; R 005,INFO
→ Enter を押す
［画面・出力］
IEE600I REPLY TO 005 IS;INFO
IEA631I OPERATOR OPER13 NOW ACTIVE, SYSTEM=SC65
画面・出力には IEE600I が含まれる。IEE600I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0273"><h3>IFASMFDP 定義照合 運用確認011</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 初級</p><p>第十一観点 ディスパッチ制御 の運用では IFASMFDP を表示、定義、証跡で確認します（第十一観点）。第十一観点 役割は SMFデータセットの内容を別データセットへ退避し、再利用できる状態へという範囲です（第十一観点）。第十一観点 SET PROG=xx後のIEE252I表示 の値を TRACE DISPLAY と合わせ、共通ストレージ変更の記録を記録します（第十一観点）。第十一観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録011に残します（第十一観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IFASMFDP 定義照合 運用確認011</strong></p><p>検証目的: IFASMFDP の 定義照合 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / GRS</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により IFASMFDP の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS
→ Enter を押す
［画面・出力］
ISG343I 10.27.11 GRS STATUS 830
SYSTEM    STATE               SYSTEM    STATE
SC65      CONNECTED           SC63      CONNECTED
GRS STAR MODE INFORMATION
画面・出力には ISG343I が含まれる。ISG343I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により IFASMFDP の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS,RNL=INCL
→ Enter を押す
［画面・出力］
ISG343I 10.28.11 GRS STATUS 840
RNL=INCL
QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により IFASMFDP の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D XCF,STR,STRNAME=ISGLOCK
→ Enter を押す
［画面・出力］
IXC360I 10.29.11 DISPLAY XCF 850
STRUCTURE NAME: ISGLOCK
STATUS: ALLOCATED IN CFRM POLICY
画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0274"><h3>SYS1.PARMLIB 出口確認 運用確認045</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>第四十五観点 ディスパッチ制御 で SYS1.PARMLIB は 出口確認 の対象です（第四十五観点）。第四十五観点 確認時には IEASYSxx、PROGxx、SMFPRMxx、GRSRNLxxなという性質を前提にします（第四十五観点）。第四十五観点 IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を同じ証跡に置き、割り込み経路の説明性確保を管理します（第四十五観点）。第四十五観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録045から再現します（第四十五観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第四十五証跡です。IFASMFDPジョブログのSYSPRINT を採取した後の扱いを選びます。確認観点は SYS1.PARMLIB、出口確認、運用確認 です。IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を合わせて読む時の採用方針として正しいものはどれか。</p><ul class="kb-choices"><li>A. TCB/SRB管理 の一般メモを採り、QNAME=SYSDSN、メッセージID、時刻の対応を記録外に置き、zOSSP誤記045として調査範囲を狭める。</li><li>B. IFASMFDPジョブログのSYSPRINT と QNAME=SYSDSN を同一票へ記録し、SYS1.PARMLIB を zOSSP正045で確定する。 <span class="kb-ok">✅ 正解</span></li><li>C. SYS1.PARMLIB の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延045として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在045として残す。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第四十五観点 正解確認: Bは SYS1.PARMLIB と QNAME=SYSDSN を同じ証跡で扱うため、後続の照合に使えます（第四十五観点）。第四十五観点 実行背景: SVC、TCB、SRB、PSWは割り込みとディスパッチの説明に使います（第四十五観点）。第四十五観点 誤答比較: Aは対象名不足、Cは表示差分不足、Dは前回証跡の混入が理由です（第四十五観点）。第四十五観点 用語整理: SMFはシステム測定記録です（第四十五観点）。第四十五観点 IFASMFDPはSMFデータ退避に使います（第四十五観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SYS1.PARMLIB 出口確認 運用確認045</strong></p><p>検証目的: SYS1.PARMLIB の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / operations</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により SYS1.PARMLIB の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY R,ALL
→ Enter を押す
［画面・出力］
IEE112I 11.15.21 DISPLAY R 744
REPLY ID   MESSAGE TEXT
005        IEA793A SPECIFY DUMP OPTION FOR QNAME=SYSDSN
画面・出力には IEE112I が含まれる。IEE112I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により SYS1.PARMLIB の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D C
→ Enter を押す
［画面・出力］
IEE889I 15.33.21 CONSOLE DISPLAY 534
MSG: CURR=0 LIM=1500  RPLY:CURR=2 LIM=999
CONSOLE ID  SPECIFICATIONS  AUTH=CMDS
画面・出力には IEE889I が含まれる。IEE889I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により SYS1.PARMLIB の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; R 005,INFO
→ Enter を押す
［画面・出力］
IEE600I REPLY TO 005 IS;INFO
IEA631I OPERATOR OPER21 NOW ACTIVE, SYSTEM=SC65
画面・出力には IEE600I が含まれる。IEE600I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE112I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE889I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IEE600I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0275"><h3>TCB ストレージ確認 運用確認028</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>第二十八観点 z/OS System Programming の ディスパッチ制御 では TCB を障害調査で照合します（第二十八観点）。第二十八観点 資料上は タスクの状態、保存情報、実行文脈を保持する制御ブロックとして扱います（第二十八観点）。第二十八観点 SMF.LOGSTREAM.SP を起点に表示値を戻し、診断ログの再現性確保を点検します（第二十八観点）。第二十八観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録028へ書きます（第二十八観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第二十八証跡です。TCB の記録を監査用に整えます。確認観点は TCB、ストレージ確認、運用確認 です。診断ログの再現性確保のために、parmlibメンバーの該当ステートメント を使った運用記録として最も適切な扱いはどれか。</p><ul class="kb-choices"><li>A. アドレス空間 の一般メモを採り、SMF.LOGSTREAM.SP、メッセージID、時刻の対応を記録外に置き、zOSSP誤記028として調査範囲を狭める。</li><li>B. TCB の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延028として扱う。</li><li>C. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在028として残す。</li><li>D. parmlibメンバーの該当ステートメント と SMF.LOGSTREAM.SP を同一票へ記録し、TCB を zOSSP正028で確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第二十八観点 照合結果: Dは SMF.LOGSTREAM.SP をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第二十八観点）。第二十八観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第二十八観点）。第二十八観点 誤答確認: Aは SMF.LOGSTREAM.SP 未追跡、Bはコマンド確認不足、Cは別システム混同が理由です（第二十八観点）。第二十八観点 用語説明: WTOは通知メッセージです（第二十八観点）。第二十八観点 WTORは応答を求めるメッセージです（第二十八観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TCB ストレージ確認 運用確認028</strong></p><p>検証目的: TCB の ストレージ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SMF</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により TCB の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D SMF,O
→ Enter を押す
［画面・出力］
IEE974I 11.01.04 SMF DATA SET STATUS
NAME       VOLSER  STATUS
SMF.MAN1   SMS001  ACTIVE
SMF.MAN2   SMS002  EMPTY
画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により TCB の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SWITCH SMF
→ Enter を押す
［画面・出力］
IEE362A SMF ENTER DUMP FOR DATA SET SMF.MAN1
IEE360I SMF NOW RECORDING ON SMF.MAN2
画面・出力には IEE360I が含まれる。IEE360I を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により TCB の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
JES2 SDSF ST
COMMAND ===&gt; S IFASMFD04
→ Enter を押す
［画面・出力］
IEF403I IFASMFD04 - STARTED
IFASMFDP SYSPRINT
INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、診断ログの再現性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0276"><h3>コンポーネントトレース 出口確認 運用確認095</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 上級</p><p>第九十五観点 ディスパッチ制御 の運用では コンポーネントトレース を表示、定義、証跡で確認します（第九十五観点）。第九十五観点 役割は 指定コンポーネントの内部事象を記録し、障害調査に使うトレース機構という範囲です（第九十五観点）。第九十五観点 IFASMFDPジョブログのSYSPRINT の値を WTOR reply 005 と合わせ、割り込み経路の説明性確保を記録します（第九十五観点）。第九十五観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録095に残します（第九十五観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>コンポーネントトレース 出口確認 運用確認095</strong></p><p>検証目的: コンポーネントトレース の 出口確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / WLM dispatch</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により コンポーネントトレース の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D A,L
→ Enter を押す
［画面・出力］
IEE114I 12.05.23 ACTIVE JOBS DISPLAY 614
JOBNAME  ASID  STATUS
WLM      000A  ACTIVE
JES2     0012  ACTIVE
画面・出力には IEE114I が含まれる。IEE114I を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により コンポーネントトレース の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; D WLM,SYSTEMS
→ Enter を押す
［画面・出力］
IWM026I 12.06.23 WLM DISPLAY 624
SYSTEM   MODE     POLICY
SC65     GOAL     POLSP23
画面・出力には GOAL が含まれる。GOAL を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により コンポーネントトレース の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
SDSF DA panel
COMMAND ===&gt; DA
→ Enter を押す
［画面・出力］
SDSF DA DISPLAY
JOBNAME  ASID  CPU%  DP
BATCH23 0023  02.1  245
画面・出力には JOBNAME が含まれる。JOBNAME を読み取り、割り込み経路の説明性確保のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: IEE114I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: GOAL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: JOBNAME が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0277"><h3>ディスパッチ制御 SRMディスパッチ状態 ログとの照合 SRM07</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>ログとの照合では ディスパッチ制御 の CPU表示 を主操作として SRM07 を判定します。時刻と対象識別子への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM07 に残します。ログとの照合を補助する SRM表示 では IRA200I を補助値として SRM07 へ保存します。主判定のログとの照合ではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM07 へ残します。証跡照合のログとの照合ではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM07 に保存します。記録対応のログとの照合ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM07 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で ディスパッチ制御 の CPU表示 と SRM表示 を使い 操作とログを対応 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読み対象 SRM07 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. IEE174Iを含むCPU表示の応答行を保存する。その応答を得るためD M=CPUを使用する。対象SRM07のCPU使用率と待ちとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. D M=CPUが応答を返した時点で正常とする。応答中のIEE174Iの値は記録しない。RMFをIEE174Iと同じ判定値とみなし対象SRM07の主証跡にする。</li><li>C. D M=CPUのコマンド文字列だけを記録する。IEE174Iを含む応答行は保存しない。</li><li>D. SRMディスパッチ状態の停止または再定義を実施する。その後にD M=CPUでIEE174Iを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 適切な判定: AはCPU表示で IEE174I を読みCPU使用率と待ちの主値として操作とログを対応しSRM07に残します。
機能の仕組み: ログとの照合ではSRM表示を補助操作としSRMディスパッチ状態の時刻と対象識別子をIRA200Iと対象SRM07で照合します。
各候補の評価: CPU表示とSRM表示の役割を分けるとA: IEE174Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではCPU使用率と待ちを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではCPU使用率と待ちを証明できない点でCPU使用率と待ちを確認できません、D: 変更前のCPU使用率と待ちを失う点でSRM表示の範囲を越えます。結論としてログとの照合のディスパッチ制御・ディスパッチ状態で判定する対象は SRM07 です。
用語の定義: ログとの照合で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM07へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ディスパッチ制御 SRMディスパッチ状態 ログとの照合 SRM07</strong></p><p>検証目的: ディスパッチ制御のSRMディスパッチ状態について操作とログを対応し、SRM07のCPU使用率と待ちを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SRM07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM07のCPU表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D M=CPU
→ Enter を押す
［画面・出力］
IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM07のSRM表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SRM
→ Enter を押す
［画面・出力］
IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM07のRMF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; RMF III DELAY
→ Enter を押す
［画面・出力］
RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
② ステップ2 の IRA200I が画面・出力に表示されること
③ ステップ3 の DELAY が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0278"><h3>ディスパッチ制御 SRMディスパッチ状態 代替経路の確認 SRM10</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>代替経路の確認では ディスパッチ制御 の CPU表示 を主操作として SRM10 を判定します。主経路との役割差への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM10 に残します。代替経路の確認を補助する SRM表示 では IRA200I を補助値として SRM10 へ保存します。主判定の代替経路の確認ではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM10 へ残します。証跡照合の代替経路の確認ではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM10 に保存します。記録対応の代替経路の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM10 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で ディスパッチ制御 の CPU表示 と SRM表示 を照合し 主経路との役割差 を確かめます。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読む前に対象 SRM10 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. D M=CPUのコマンド文字列だけを記録する。IEE174Iを含む応答行は保存しない。</li><li>B. SRMディスパッチ状態の停止または再定義を実施する。その後にD M=CPUでIEE174Iを採取する。</li><li>C. APF管理のDSNAMEとVOLSERを確認する。その値をディスパッチ制御のSRM10にも適用する。</li><li>D. D M=CPUとD SRMの対象名をそろえる。前者のIEE174IをCPU使用率と待ちの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい判定結果: DはCPU表示で IEE174I を読みCPU使用率と待ちの主値として代替手段の成立を確認しSRM10に残します。
運用上の背景: 代替経路の確認ではSRM表示を補助操作としSRMディスパッチ状態の主経路との役割差をIRA200Iと対象SRM10で照合します。
候補別の検討: CPU表示とSRM表示の役割を分けるとA: 入力記録だけではCPU使用率と待ちを証明できない点で一次資料と一致しません、B: 変更前のCPU使用率と待ちを失う点でCPU使用率と待ちを確認できません、C: APF管理の値ではIEE174Iを確認できない点でSRM表示の範囲を越えます、D: 同じ対象名のIEE174Iを採用する点で現在値を示します。結論として代替経路の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM10 です。
重要用語の定義: 代替経路の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM10へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ディスパッチ制御 SRMディスパッチ状態 代替経路の確認 SRM10</strong></p><p>検証目的: ディスパッチ制御のSRMディスパッチ状態について代替手段の成立を確認し、SRM10のCPU使用率と待ちを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SRM10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM10のCPU表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D M=CPU
→ Enter を押す
［画面・出力］
IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM10のSRM表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SRM
→ Enter を押す
［画面・出力］
IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM10のRMF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; RMF III DELAY
→ Enter を押す
［画面・出力］
RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
② ステップ2 の IRA200I が画面・出力に表示されること
③ ステップ3 の DELAY が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0279"><h3>ディスパッチ制御 SRMディスパッチ状態 変更前の確認 SRM02</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>変更前の確認では ディスパッチ制御 の SRM表示 を主操作として SRM02 を判定します。変更対象と非対象の境界への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM02 に残します。変更前の確認を補助する RMF確認 では RMF を補助値として SRM02 へ保存します。主判定の変更前の確認ではディスパッチ制御・ディスパッチ状態の SRM表示 から IRA200I を読み SRM02 へ残します。証跡照合の変更前の確認ではディスパッチ制御・ディスパッチ状態の IRA200I と RMF を SRM02 に保存します。記録対応の変更前の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM02 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で ディスパッチ制御 の SRM表示 と RMF確認 を実施し SRMディスパッチ状態 の役割を確認します。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。対象 SRM02 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. D SRMを対象名なしで実行する。一覧の先頭行をSRM02の結果として記録する。</li><li>B. 前回保存したD SRMの結果を使う。今回のRMF III DELAYの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのSRM02の出力を再利用する。今回のD SRMとRMF III DELAYは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象SRM02についてD SRMの応答からIRA200Iを確認する。RMF III DELAYは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用理由: DはSRM表示で IRA200I を読みCPU使用率と待ちの主値として変更前の証跡を保存しSRM02に残します。
動作の背景: 変更前の確認ではRMF確認を補助操作としSRMディスパッチ状態の変更対象と非対象の境界をRMFと対象SRM02で照合します。
各選択肢の検討: SRM表示とRMF確認の役割を分けるとA: 先頭行はSRM02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でSRM表示を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でディスパッチ制御に使いません、D: IRA200Iと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM02 です。
初出用語の定義: 変更前の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM02へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ディスパッチ制御 SRMディスパッチ状態 変更前の確認 SRM02</strong></p><p>検証目的: ディスパッチ制御のSRMディスパッチ状態について変更前の証跡を保存し、SRM02のCPU使用率と待ちを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SRM02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM02のSRM表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SRM
→ Enter を押す
［画面・出力］
IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM02のRMF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; RMF III DELAY
→ Enter を押す
［画面・出力］
RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM02のCPU表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D M=CPU
→ Enter を押す
［画面・出力］
IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IRA200I が画面・出力に表示されること
② ステップ2 の DELAY が画面・出力に表示されること
③ ステップ3 の IEE174I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0280"><h3>ディスパッチ制御 SRMディスパッチ状態 変更後の確認 SRM03</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>変更後の確認では ディスパッチ制御 の RMF確認 を主操作として SRM03 を判定します。反映値と残存値への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM03 に残します。変更後の確認を補助する CPU表示 では IEE174I を補助値として SRM03 へ保存します。主判定の変更後の確認ではディスパッチ制御・ディスパッチ状態の RMF確認 から RMF を読み SRM03 へ残します。証跡照合の変更後の確認ではディスパッチ制御・ディスパッチ状態の RMF と IEE174I を SRM03 に保存します。記録対応の変更後の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM03 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で ディスパッチ制御 の RMF確認 と CPU表示 を用い 変更結果を検証 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。RMF で対象 SRM03 の CPU使用率と待ち を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. D M=CPUで周辺状態を押さえる。その後にRMF III DELAYでRMFを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. SRMディスパッチ状態の停止または再定義を実施する。その後にRMF III DELAYでRMFを採取する。</li><li>C. SAF連携のSAF RCとRACF RCを確認する。その値をディスパッチ制御のSRM03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>D. D M=CPUが成功したためRMF III DELAYのRMFも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答の根拠: AはRMF確認で RMF を読みCPU使用率と待ちの主値として変更結果を検証しSRM03に残します。
内部の仕組み: 変更後の確認ではCPU表示を補助操作としSRMディスパッチ状態の反映値と残存値をIEE174Iと対象SRM03で照合します。
誤答を含む比較: RMF確認とCPU表示の役割を分けるとA: 周辺状態の後にRMFを確認する点でSRM03を判定できます、B: 変更前のCPU使用率と待ちを失う点でCPU表示の範囲を越えます、C: SAF連携の値ではRMFを確認できないうえに追加前提も不正な点でSRM03の値を示しません、D: 補助操作の成功ではRMFを確定できない点で変更後の確認に合いません。結論として変更後の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM03 です。
用語定義: 変更後の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM03へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ディスパッチ制御 SRMディスパッチ状態 変更後の確認 SRM03</strong></p><p>検証目的: ディスパッチ制御のSRMディスパッチ状態について変更結果を検証し、SRM03のCPU使用率と待ちを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SRM03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM03のRMF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; RMF III DELAY
→ Enter を押す
［画面・出力］
RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM03のCPU表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D M=CPU
→ Enter を押す
［画面・出力］
IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM03のSRM表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SRM
→ Enter を押す
［画面・出力］
IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DELAY が画面・出力に表示されること
② ステップ2 の IEE174I が画面・出力に表示されること
③ ステップ3 の IRA200I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0281"><h3>ディスパッチ制御 SRMディスパッチ状態 引継ぎ記録 SRM09</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>引継ぎ記録では ディスパッチ制御 の RMF確認 を主操作として SRM09 を判定します。次担当者が追跡できる証跡への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM09 に残します。引継ぎ記録を補助する CPU表示 では IEE174I を補助値として SRM09 へ保存します。主判定の引継ぎ記録ではディスパッチ制御・ディスパッチ状態の RMF確認 から RMF を読み SRM09 へ残します。証跡照合の引継ぎ記録ではディスパッチ制御・ディスパッチ状態の RMF と IEE174I を SRM09 に保存します。記録対応の引継ぎ記録ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM09 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で ディスパッチ制御 の RMF確認 と CPU表示 を用い 再現可能な記録を作成 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。RMF で対象 SRM09 の CPU使用率と待ち を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. D M=CPUが成功したためRMF III DELAYのRMFも正常だと推定する。主出力は保存しない。</li><li>B. RMF III DELAYを対象名なしで実行する。一覧の先頭行をSRM09の結果として記録する。</li><li>C. 対象名SRM09を指定してRMF III DELAYを実行する。応答中のRMFと時刻を保存する。D M=CPUで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したRMF III DELAYの結果を使う。今回のD M=CPUの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 採用操作の理由: CはRMF確認で RMF を読みCPU使用率と待ちの主値として再現可能な記録を作成しSRM09に残します。
製品内の仕組み: 引継ぎ記録ではCPU表示を補助操作としSRMディスパッチ状態の次担当者が追跡できる証跡をIEE174Iと対象SRM09で照合します。
選択肢別の説明: RMF確認とCPU表示の役割を分けるとA: 補助操作の成功ではRMFを確定できない点でSRM09の値を示しません、B: 先頭行はSRM09と確定できない点で引継ぎ記録に合いません、C: RMFと時刻を保存する点でRMF確認に合います、D: 採取時刻が異なる点でディスパッチ制御に使いません。結論として引継ぎ記録のディスパッチ制御・ディスパッチ状態で判定する対象は SRM09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM09へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ディスパッチ制御 SRMディスパッチ状態 引継ぎ記録 SRM09</strong></p><p>検証目的: ディスパッチ制御のSRMディスパッチ状態について再現可能な記録を作成し、SRM09のCPU使用率と待ちを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SRM09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM09のRMF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; RMF III DELAY
→ Enter を押す
［画面・出力］
RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM09のCPU表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D M=CPU
→ Enter を押す
［画面・出力］
IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM09のSRM表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SRM
→ Enter を押す
［画面・出力］
IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DELAY が画面・出力に表示されること
② ステップ2 の IEE174I が画面・出力に表示されること
③ ステップ3 の IRA200I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0282"><h3>ディスパッチ制御 SRMディスパッチ状態 復旧後の確認 SRM06</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>復旧後の確認では ディスパッチ制御 の RMF確認 を主操作として SRM06 を判定します。再発していないことを示す値への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM06 に残します。復旧後の確認を補助する CPU表示 では IEE174I を補助値として SRM06 へ保存します。主判定の復旧後の確認ではディスパッチ制御・ディスパッチ状態の RMF確認 から RMF を読み SRM06 へ残します。証跡照合の復旧後の確認ではディスパッチ制御・ディスパッチ状態の RMF と IEE174I を SRM06 に保存します。記録対応の復旧後の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM06 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で ディスパッチ制御 の RMF確認 と CPU表示 の役割を分け 再発していないことを示す値 を調べます。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。対象 SRM06 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. Cross MemoryのHOME ASIDとSECONDARY ASIDを確認する。その値をディスパッチ制御のSRM06にも適用する。</li><li>B. D M=CPUが成功したためRMF III DELAYのRMFも正常だと推定する。主出力は保存しない。別資源で得た状態を対象SRM06へ引き継げるものとする。</li><li>C. RMF III DELAYを対象名なしで実行する。一覧の先頭行をSRM06の結果として記録する。</li><li>D. RMF III DELAYでRMFを取得してからD SRMでIRA200Iを照合する。SRM06のCPU使用率と待ちを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正答内容: DはRMF確認で RMF を読みCPU使用率と待ちの主値として復旧後の安定性を確認しSRM06に残します。
構成上の背景: 復旧後の確認ではCPU表示を補助操作としSRMディスパッチ状態の再発していないことを示す値をIEE174Iと対象SRM06で照合します。
候補ごとの理由: RMF確認とCPU表示の役割を分けるとA: Cross Memoryの値ではRMFを確認できない点でCPU表示の範囲を越えます、B: 補助操作の成功ではRMFを確定できないうえに追加前提も不正な点でSRM06の値を示しません、C: 先頭行はSRM06と確定できない点で復旧後の確認に合いません、D: RMFとIRA200Iを順に照合する点でRMF確認に合います。結論として復旧後の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM06 です。
初出用語: 復旧後の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM06へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ディスパッチ制御 SRMディスパッチ状態 復旧後の確認 SRM06</strong></p><p>検証目的: ディスパッチ制御のSRMディスパッチ状態について復旧後の安定性を確認し、SRM06のCPU使用率と待ちを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SRM06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM06のRMF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; RMF III DELAY
→ Enter を押す
［画面・出力］
RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM06のCPU表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D M=CPU
→ Enter を押す
［画面・出力］
IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM06のSRM表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SRM
→ Enter を押す
［画面・出力］
IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の DELAY が画面・出力に表示されること
② ステップ2 の IEE174I が画面・出力に表示されること
③ ステップ3 の IRA200I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0283"><h3>ディスパッチ制御 SRMディスパッチ状態 復旧準備 SRM05</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>復旧準備では ディスパッチ制御 の SRM表示 を主操作として SRM05 を判定します。再開前に必要な整合性への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM05 に残します。復旧準備を補助する RMF確認 では RMF を補助値として SRM05 へ保存します。主判定の復旧準備ではディスパッチ制御・ディスパッチ状態の SRM表示 から IRA200I を読み SRM05 へ残します。証跡照合の復旧準備ではディスパッチ制御・ディスパッチ状態の IRA200I と RMF を SRM05 に保存します。記録対応の復旧準備ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM05 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で ディスパッチ制御 の SRM表示 と RMF確認 を組み合わせる際は SRMディスパッチ状態 がサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能という仕組みを前提にします。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IRA200I と CPU使用率と待ち を対象 SRM05 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 前回保存したD SRMの結果を使う。今回のRMF III DELAYの結果と同一時点の証跡として比較する。</li><li>B. 保存済みのSRM05の出力を再利用する。今回のD SRMとRMF III DELAYは実行済みとして扱う。</li><li>C. 変更を加えずD SRMを実行する。IRA200Iを保存する。差分はRMF III DELAYの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. RMF III DELAYのRMFをCPU使用率と待ちの主判定に採用する。D SRMの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 選定理由: CはSRM表示で IRA200I を読みCPU使用率と待ちの主値として復旧条件を確認しSRM05に残します。
処理の仕組み: 復旧準備ではRMF確認を補助操作としSRMディスパッチ状態の再開前に必要な整合性をRMFと対象SRM05で照合します。
選択結果の内訳: SRM表示とRMF確認の役割を分けるとA: 採取時刻が異なる点でSRM表示を代替しません、B: 過去出力では今回の復旧準備を示せない点でディスパッチ制御に使いません、C: 変更前のIRA200Iを保存する点で正答です、D: RMFはIRA200Iを代替しないうえに追加前提も不正な点でSRM05を採用できません。結論として復旧準備のディスパッチ制御・ディスパッチ状態で判定する対象は SRM05 です。
用語の説明: 復旧準備で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM05へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ディスパッチ制御 SRMディスパッチ状態 復旧準備 SRM05</strong></p><p>検証目的: ディスパッチ制御のSRMディスパッチ状態について復旧条件を確認し、SRM05のCPU使用率と待ちを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SRM05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM05のSRM表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SRM
→ Enter を押す
［画面・出力］
IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM05のRMF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; RMF III DELAY
→ Enter を押す
［画面・出力］
RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM05のCPU表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D M=CPU
→ Enter を押す
［画面・出力］
IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IRA200I が画面・出力に表示されること
② ステップ2 の DELAY が画面・出力に表示されること
③ ステップ3 の IEE174I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0284"><h3>ディスパッチ制御 SRMディスパッチ状態 構成監査 SRM08</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>構成監査では ディスパッチ制御 の SRM表示 を主操作として SRM08 を判定します。定義値と稼働値の一致への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM08 に残します。構成監査を補助する RMF確認 では RMF を補助値として SRM08 へ保存します。主判定の構成監査ではディスパッチ制御・ディスパッチ状態の SRM表示 から IRA200I を読み SRM08 へ残します。証跡照合の構成監査ではディスパッチ制御・ディスパッチ状態の IRA200I と RMF を SRM08 に保存します。記録対応の構成監査ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM08 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で ディスパッチ制御 の SRM表示 と RMF確認 を実施し SRMディスパッチ状態 の役割を確認します。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。対象 SRM08 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのSRM08の出力を再利用する。今回のD SRMとRMF III DELAYは実行済みとして扱う。</li><li>B. RMF III DELAYの結果だけでは確定しない。D SRMのIRA200Iを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. RMF III DELAYのRMFをCPU使用率と待ちの主判定に採用する。D SRMの応答は採取対象から外す。</li><li>D. D M=CPUのIEE174IをIRA200Iと同義の成功表示として扱う。D SRMは実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 技術上の正答: BはSRM表示で IRA200I を読みCPU使用率と待ちの主値として構成差分を監査しSRM08に残します。
実行時の背景: 構成監査ではRMF確認を補助操作としSRMディスパッチ状態の定義値と稼働値の一致をRMFと対象SRM08で照合します。
四つの候補の理由: SRM表示とRMF確認の役割を分けるとA: 過去出力では今回の構成監査を示せない点でディスパッチ制御に使いません、B: IRA200Iを主証跡として区別する点で正答です、C: RMFはIRA200Iを代替しない点でSRM08を採用できません、D: IEE174IとIRA200Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のディスパッチ制御・ディスパッチ状態で判定する対象は SRM08 です。
初出語定義: 構成監査で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM08へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ディスパッチ制御 SRMディスパッチ状態 構成監査 SRM08</strong></p><p>検証目的: ディスパッチ制御のSRMディスパッチ状態について構成差分を監査し、SRM08のCPU使用率と待ちを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SRM08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM08のSRM表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SRM
→ Enter を押す
［画面・出力］
IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM08のRMF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; RMF III DELAY
→ Enter を押す
［画面・出力］
RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM08のCPU表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D M=CPU
→ Enter を押す
［画面・出力］
IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IRA200I が画面・出力に表示されること
② ステップ2 の DELAY が画面・出力に表示されること
③ ステップ3 の IEE174I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0285"><h3>ディスパッチ制御 SRMディスパッチ状態 通常状態の確認 SRM01</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>通常状態の確認では ディスパッチ制御 の CPU表示 を主操作として SRM01 を判定します。基準値と現在値の差への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM01 に残します。通常状態の確認を補助する SRM表示 では IRA200I を補助値として SRM01 へ保存します。主判定の通常状態の確認ではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM01 へ残します。証跡照合の通常状態の確認ではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM01 に保存します。記録対応の通常状態の確認ではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM01 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で ディスパッチ制御 の CPU表示 と SRM表示 を使い 通常状態を確定 します。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読み対象 SRM01 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. D SRMのIRA200IをCPU使用率と待ちの主判定に採用する。D M=CPUの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. RMF III DELAYのRMFをIEE174Iと同義の成功表示として扱う。D M=CPUは実行しない。</li><li>C. D M=CPUを先に実行する。対象SRM01のIEE174IをCPU使用率と待ちとして記録する。続いてD SRMで同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. D M=CPUが応答を返した時点で正常とする。応答中のIEE174Iの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解の説明: CはCPU表示で IEE174I を読みCPU使用率と待ちの主値として通常状態を確定しSRM01に残します。
背景・仕組み: 通常状態の確認ではSRM表示を補助操作としSRMディスパッチ状態の基準値と現在値の差をIRA200Iと対象SRM01で照合します。
選択肢の理由: CPU表示とSRM表示の役割を分けるとA: IRA200IはIEE174Iを代替しないうえに追加前提も不正な点でSRMディスパッチ状態に使えません、B: RMFとIEE174Iは確認項目が異なる点でSRM01を採用できません、C: IEE174Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではCPU使用率と待ちを判定できない点で一次資料と一致しません。結論として通常状態の確認のディスパッチ制御・ディスパッチ状態で判定する対象は SRM01 です。
用語の初出定義: 通常状態の確認で使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM01へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ディスパッチ制御 SRMディスパッチ状態 通常状態の確認 SRM01</strong></p><p>検証目的: ディスパッチ制御のSRMディスパッチ状態について通常状態を確定し、SRM01のCPU使用率と待ちを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SRM01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM01のCPU表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D M=CPU
→ Enter を押す
［画面・出力］
IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM01のSRM表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SRM
→ Enter を押す
［画面・出力］
IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM01のRMF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; RMF III DELAY
→ Enter を押す
［画面・出力］
RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
② ステップ2 の IRA200I が画面・出力に表示されること
③ ステップ3 の DELAY が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0286"><h3>ディスパッチ制御 SRMディスパッチ状態 障害切り分け SRM04</h3><p class="kb-meta">分類: ディスパッチ制御 ・ 難易度: 中級</p><p>障害切り分けでは ディスパッチ制御 の CPU表示 を主操作として SRM04 を判定します。最初に失敗した処理への注意として「CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります」を SRM04 に残します。障害切り分けを補助する SRM表示 では IRA200I を補助値として SRM04 へ保存します。主判定の障害切り分けではディスパッチ制御・ディスパッチ状態の CPU表示 から IEE174I を読み SRM04 へ残します。証跡照合の障害切り分けではディスパッチ制御・ディスパッチ状態の IEE174I と IRA200I を SRM04 に保存します。記録対応の障害切り分けではディスパッチ制御・ディスパッチ状態の CPU使用率と待ち の証跡へ SRM04 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで ディスパッチ制御 の CPU表示 と SRM表示 を照合し 最初に失敗した処理 を確かめます。SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能です。CPU高騰だけを見てI/O待ちやエンクレーブ目標を見落とす危険があります。IEE174I を読む前に対象 SRM04 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. RMF III DELAYのRMFをIEE174Iと同義の成功表示として扱う。D M=CPUは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. D M=CPUの出力でSRM04とIEE174Iが同じ応答にあることを確認する。CPU使用率と待ちをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. D M=CPUが応答を返した時点で正常とする。応答中のIEE174Iの値は記録しない。</li><li>D. D M=CPUのコマンド文字列だけを記録する。IEE174Iを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正しい操作の説明: BはCPU表示で IEE174I を読みCPU使用率と待ちの主値として障害範囲を限定しSRM04に残します。
技術的背景: 障害切り分けではSRM表示を補助操作としSRMディスパッチ状態の最初に失敗した処理をIRA200Iと対象SRM04で照合します。
四択の評価: CPU表示とSRM表示の役割を分けるとA: RMFとIEE174Iは確認項目が異なるうえに追加前提も不正な点でSRM04を採用できません、B: SRM04とIEE174Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではCPU使用率と待ちを判定できない点で一次資料と一致しません、D: 入力記録だけではCPU使用率と待ちを証明できない点でCPU使用率と待ちを確認できません。結論として障害切り分けのディスパッチ制御・ディスパッチ状態で判定する対象は SRM04 です。
初出語の意味: 障害切り分けで使う SRMディスパッチ状態 はサービスクラス目標とCPU待ちに基づいてアドレス空間、TCB、SRBへ実行機会を配分する機能を表しCPU使用率と待ちを判定する際にSRM04へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ディスパッチ制御 SRMディスパッチ状態 障害切り分け SRM04</strong></p><p>検証目的: ディスパッチ制御のSRMディスパッチ状態について障害範囲を限定し、SRM04のCPU使用率と待ちを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象SRM04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD M=CPUを指定し、SRM04のCPU表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D M=CPU
→ Enter を押す
［画面・出力］
IEE174I 12.21.00 DISPLAY M 456 PROCESSOR STATUS CPU 00 ONLINE
画面・出力にあるIEE174Iを読み、CPU使用率と待ちと対象SRM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へD SRMを指定し、SRM04のSRM表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D SRM
→ Enter を押す
［画面・出力］
IRA200I SRM STATUS WLM POLICY ACTIVE ENCLAVE MANAGEMENT ACTIVE
画面・出力にあるIRA200Iを読み、CPU使用率と待ちと対象SRM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのディスパッチ制御を確認する入力画面です。COMMAND入力口へRMF III DELAYを指定し、SRM04のRMF確認を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; RMF III DELAY
→ Enter を押す
［画面・出力］
RMF DELAY REPORT SERVICE CLASS SYSSTC CPU USING 12.4% I/O DELAY 0.8%
画面・出力にあるDELAYを読み、CPU使用率と待ちと対象SRM04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE174I が画面・出力に表示されること
② ステップ2 の IRA200I が画面・出力に表示されること
③ ステップ3 の DELAY が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


## トレース診断


<section class="kb-item" id="c38-i0287"><h3>DEQマクロ 割り込み確認 運用確認067</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 中級</p><p>第六十七観点 トレース診断 の運用では DEQマクロ を表示、定義、証跡で確認します（第六十七観点）。第六十七観点 役割は ENQで取得した資源の直列化を解放し、後続処理へ資源を渡すマクロという範囲です（第六十七観点）。第六十七観点 IPCS VERBX LOGDATA出力 の値を SMF.MAN1 と合わせ、オペレーター応答漏れの防止を記録します（第六十七観点）。第六十七観点 確認経路は SDSF、コンソールログ、parmlib、IPCS の別を zOSSP記録067に残します（第六十七観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第六十七証跡です。トレース診断 の当日作業で SMF.MAN1 を追跡します。確認観点は DEQマクロ、割り込み確認、運用確認 です。SMF.MAN1 を根拠として残す時、対象の取り違えを抑える対応はどれか。</p><ul class="kb-choices"><li>A. PSW/割り込み の一般メモを採り、SMF.MAN1、メッセージID、時刻の対応を記録外に置き、zOSSP誤記067として調査範囲を狭める。</li><li>B. DEQマクロ の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延067として扱う。</li><li>C. IPCS VERBX LOGDATA出力 と SMF.MAN1 を同一票へ記録し、DEQマクロ を zOSSP正067で確定する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在067として残す。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第六十七観点 採用理由: Cは DEQマクロ の状態を表示値と定義の両方から確認するため、記録として妥当です（第六十七観点）。第六十七観点 記録背景: SMFはSMFPRMxxやSWITCH SMF、IFASMFDPで記録と退避を管理します（第六十七観点）。第六十七観点 誤答整理: Aは一般メモ偏重、Bはジョブログ除外、Dは再現性不足が理由です（第六十七観点）。第六十七観点 用語確認: APFは許可ライブラリーの管理機能です（第六十七観点）。第六十七観点 PROGxxは動的なプログラム管理指定です（第六十七観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEQマクロ 割り込み確認 運用確認067</strong></p><p>検証目的: DEQマクロ の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / GRS</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により DEQマクロ の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS
→ Enter を押す
［画面・出力］
ISG343I 10.27.19 GRS STATUS 886
SYSTEM    STATE               SYSTEM    STATE
SC65      CONNECTED           SC63      CONNECTED
GRS STAR MODE INFORMATION
画面・出力には ISG343I が含まれる。ISG343I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により DEQマクロ の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; DISPLAY GRS,RNL=INCL
→ Enter を押す
［画面・出力］
ISG343I 10.28.19 GRS STATUS 896
RNL=INCL
QNAME=SYSDSN  RNAME=SYS1.PARMLIB  SCOPE=SYSTEMS
画面・出力には RNL=INCL が含まれる。RNL=INCL を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により DEQマクロ の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D XCF,STR,STRNAME=ISGLOCK
→ Enter を押す
［画面・出力］
IXC360I 10.29.19 DISPLAY XCF 906
STRUCTURE NAME: ISGLOCK
STATUS: ALLOCATED IN CFRM POLICY
画面・出力には ISGLOCK が含まれる。ISGLOCK を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: ISG343I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: RNL=INCL が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ISGLOCK が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0288"><h3>ISGENQマクロ 割り込み確認 運用確認017</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 初級</p><p>第十七観点 トレース診断 で ISGENQマクロ は 割り込み確認 の対象です（第十七観点）。第十七観点 確認時には ENQ、DEQ、RESERVEの機能を統合し、31ビットと64ビットという性質を前提にします（第十七観点）。第十七観点 IPCS VERBX LOGDATA出力 と AUTH=CMDS を同じ証跡に置き、オペレーター応答漏れの防止を管理します（第十七観点）。第十七観点 後続確認ではシステム名、ASID、メンバー名、メッセージIDを zOSSP記録017から再現します（第十七観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ISGENQマクロ 割り込み確認 運用確認017</strong></p><p>検証目的: ISGENQマクロ の 割り込み確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SDSF LOG</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により ISGENQマクロ の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 05.18.17 PROG,APF DISPLAY 916
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   2  MPRES1 SYS1.SVCLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により ISGENQマクロ の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SETPROG APF,ADD,DSNAME=MYPROG.LOADLIB,VOLUME=MPRES3
→ Enter を押す
［画面・出力］
CSV410I DATA SET MYPROG.LOADLIB ON VOLUME MPRES3 ADDED TO APF LIST
画面・出力には CSV410I が含まれる。CSV410I を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により ISGENQマクロ の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF,ENTRY=(1-5)
→ Enter を押す
［画面・出力］
CSV450I 05.26.17 PROG,APF DISPLAY 966
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
   1  MPRES1 SYS1.LINKLIB
   5  MPRES1 ISF.SISFLPA
画面・出力には ENTRY VOLUME DSNAME が含まれる。ENTRY VOLUME DSNAME を読み取り、オペレーター応答漏れの防止のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: CSV450I が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: CSV410I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: ENTRY VOLUME DSNAME が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0289"><h3>トレース診断 システムトレース ログとの照合 TRC07</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 上級</p><p>ログとの照合では トレース診断 の トレース状態 を主操作として TRC07 を判定します。時刻と対象識別子への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC07 に残します。ログとの照合を補助する バッファ指定 では IEE839I を補助値として TRC07 へ保存します。主判定のログとの照合ではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC07 へ残します。証跡照合のログとの照合ではトレース診断・システムトレースの IEE843I と IEE839I を TRC07 に保存します。記録対応のログとの照合ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC07 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> ログとの照合で トレース診断 の トレース状態 と バッファ指定 を使い 操作とログを対応 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読み対象 TRC07 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. IEE843Iを含むトレース状態の応答行を保存する。その応答を得るためD TRACEを使用する。対象TRC07のTRACE STATUSとBUFFERとして記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. D TRACEが応答を返した時点で正常とする。応答中のIEE843Iの値は記録しない。SYSTEMをIEE843Iと同じ判定値とみなし対象TRC07の主証跡にする。システムトレースの時刻と対象識別子は確認済みとして扱う。さらにIP SYSTRACEのSYSTEMをIEE843Iと同種の値として併記する。</li><li>C. D TRACEのコマンド文字列だけを記録する。IEE843Iを含む応答行は保存しない。</li><li>D. システムトレースの停止または再定義を実施する。その後にD TRACEでIEE843Iを採取する。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 適切な判定: Aはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として操作とログを対応しTRC07に残します。
機能の仕組み: ログとの照合ではバッファ指定を補助操作としシステムトレースの時刻と対象識別子をIEE839Iと対象TRC07で照合します。
各候補の評価: トレース状態とバッファ指定の役割を分けるとA: IEE843Iの実値を対象別に残す点で主証跡になります、B: 応答の有無だけではTRACE STATUSとBUFFERを判定できないうえに追加前提も不正な点で一次資料と一致しません、C: 入力記録だけではTRACE STATUSとBUFFERを証明できない点でTRACE STATUSとBUFFERを確認できません、D: 変更前のTRACE STATUSとBUFFERを失う点でバッファ指定の範囲を越えます。結論としてログとの照合のトレース診断・システムトレースで判定する対象は TRC07 です。
用語の定義: ログとの照合で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC07へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>トレース診断 システムトレース ログとの照合 TRC07</strong></p><p>検証目的: トレース診断のシステムトレースについて操作とログを対応し、TRC07のTRACE STATUSとBUFFERを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TRC07と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC07のトレース状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.36.21 TRACE DISPLAY 490
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC07のバッファ指定を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; TRACE ST,2M
→ Enter を押す
［画面・出力］
IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC07のIPCS表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SYSTRACE
→ Enter を押す
［画面・出力］
SYSTEM TRACE TABLE CPU 0000 ASID 0007 EVENT SVC
画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC07の対応を確認します。時刻と対象識別子を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
② ステップ2 の IEE839I が画面・出力に表示されること
③ ステップ3 の SYSTEM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0290"><h3>トレース診断 システムトレース 代替経路の確認 TRC10</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 上級</p><p>代替経路の確認では トレース診断 の トレース状態 を主操作として TRC10 を判定します。主経路との役割差への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC10 に残します。代替経路の確認を補助する バッファ指定 では IEE839I を補助値として TRC10 へ保存します。主判定の代替経路の確認ではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC10 へ残します。証跡照合の代替経路の確認ではトレース診断・システムトレースの IEE843I と IEE839I を TRC10 に保存します。記録対応の代替経路の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC10 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 代替経路の確認で トレース診断 の トレース状態 と バッファ指定 を照合し 主経路との役割差 を確かめます。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読む前に対象 TRC10 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. D TRACEのコマンド文字列だけを記録する。IEE843Iを含む応答行は保存しない。</li><li>B. システムトレースの停止または再定義を実施する。その後にD TRACEでIEE843Iを採取する。</li><li>C. APF管理のDSNAMEとVOLSERを確認する。その値をトレース診断のTRC10にも適用する。</li><li>D. D TRACEとTRACE ST,2Mの対象名をそろえる。前者のIEE843IをTRACE STATUSとBUFFERの判定値として採用する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい判定結果: Dはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として代替手段の成立を確認しTRC10に残します。
運用上の背景: 代替経路の確認ではバッファ指定を補助操作としシステムトレースの主経路との役割差をIEE839Iと対象TRC10で照合します。
候補別の検討: トレース状態とバッファ指定の役割を分けるとA: 入力記録だけではTRACE STATUSとBUFFERを証明できない点で一次資料と一致しません、B: 変更前のTRACE STATUSとBUFFERを失う点でTRACE STATUSとBUFFERを確認できません、C: APF管理の値ではIEE843Iを確認できない点でバッファ指定の範囲を越えます、D: 同じ対象名のIEE843Iを採用する点で現在値を示します。結論として代替経路の確認のトレース診断・システムトレースで判定する対象は TRC10 です。
重要用語の定義: 代替経路の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC10へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>トレース診断 システムトレース 代替経路の確認 TRC10</strong></p><p>検証目的: トレース診断のシステムトレースについて代替手段の成立を確認し、TRC10のTRACE STATUSとBUFFERを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TRC10と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC10のトレース状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.36.21 TRACE DISPLAY 490
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC10のバッファ指定を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; TRACE ST,2M
→ Enter を押す
［画面・出力］
IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC10のIPCS表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SYSTRACE
→ Enter を押す
［画面・出力］
SYSTEM TRACE TABLE CPU 0000 ASID 0010 EVENT SVC
画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC10の対応を確認します。主経路との役割差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
② ステップ2 の IEE839I が画面・出力に表示されること
③ ステップ3 の SYSTEM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0291"><h3>トレース診断 システムトレース 変更前の確認 TRC02</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 上級</p><p>変更前の確認では トレース診断 の バッファ指定 を主操作として TRC02 を判定します。変更対象と非対象の境界への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC02 に残します。変更前の確認を補助する IPCS表示 では SYSTEM を補助値として TRC02 へ保存します。主判定の変更前の確認ではトレース診断・システムトレースの バッファ指定 から IEE839I を読み TRC02 へ残します。証跡照合の変更前の確認ではトレース診断・システムトレースの IEE839I と SYSTEM を TRC02 に保存します。記録対応の変更前の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC02 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更前の確認で トレース診断 の バッファ指定 と IPCS表示 を実施し システムトレース の役割を確認します。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。対象 TRC02 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. TRACE ST,2Mを対象名なしで実行する。一覧の先頭行をTRC02の結果として記録する。</li><li>B. 前回保存したTRACE ST,2Mの結果を使う。今回のIP SYSTRACEの結果と同一時点の証跡として比較する。</li><li>C. 保存済みのTRC02の出力を再利用する。今回のTRACE ST,2MとIP SYSTRACEは実行済みとして扱う。前回値との採取時刻の差も無視できるものとする。</li><li>D. 対象TRC02についてTRACE ST,2Mの応答からIEE839Iを確認する。IP SYSTRACEは補助証跡として時刻をそろえて保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用理由: Dはバッファ指定で IEE839I を読みTRACE STATUSとBUFFERの主値として変更前の証跡を保存しTRC02に残します。
動作の背景: 変更前の確認ではIPCS表示を補助操作としシステムトレースの変更対象と非対象の境界をSYSTEMと対象TRC02で照合します。
各選択肢の検討: バッファ指定とIPCS表示の役割を分けるとA: 先頭行はTRC02と確定できない点で変更前の確認に合いません、B: 採取時刻が異なる点でバッファ指定を代替しません、C: 過去出力では今回の変更前の確認を示せないうえに追加前提も不正な点でトレース診断に使いません、D: IEE839Iと補助証跡の時刻を合わせる点で正答です。結論として変更前の確認のトレース診断・システムトレースで判定する対象は TRC02 です。
初出用語の定義: 変更前の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC02へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>トレース診断 システムトレース 変更前の確認 TRC02</strong></p><p>検証目的: トレース診断のシステムトレースについて変更前の証跡を保存し、TRC02のTRACE STATUSとBUFFERを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TRC02と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC02のバッファ指定を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; TRACE ST,2M
→ Enter を押す
［画面・出力］
IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC02のIPCS表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SYSTRACE
→ Enter を押す
［画面・出力］
SYSTEM TRACE TABLE CPU 0000 ASID 0002 EVENT SVC
画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC02のトレース状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.36.21 TRACE DISPLAY 490
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC02の対応を確認します。変更対象と非対象の境界を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE839I が画面・出力に表示されること
② ステップ2 の SYSTEM が画面・出力に表示されること
③ ステップ3 の IEE843I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0292"><h3>トレース診断 システムトレース 変更後の確認 TRC03</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 上級</p><p>変更後の確認では トレース診断 の IPCS表示 を主操作として TRC03 を判定します。反映値と残存値への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC03 に残します。変更後の確認を補助する トレース状態 では IEE843I を補助値として TRC03 へ保存します。主判定の変更後の確認ではトレース診断・システムトレースの IPCS表示 から SYSTEM を読み TRC03 へ残します。証跡照合の変更後の確認ではトレース診断・システムトレースの SYSTEM と IEE843I を TRC03 に保存します。記録対応の変更後の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC03 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更後の確認で トレース診断 の IPCS表示 と トレース状態 を用い 変更結果を検証 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。SYSTEM で対象 TRC03 の TRACE STATUSとBUFFER を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. D TRACEで周辺状態を押さえる。その後にIP SYSTRACEでSYSTEMを確認して変更結果を検証する。 <span class="kb-ok">✅ 正解</span></li><li>B. システムトレースの停止または再定義を実施する。その後にIP SYSTRACEでSYSTEMを採取する。</li><li>C. SAF連携のSAF RCとRACF RCを確認する。その値をトレース診断のTRC03にも適用する。同じ製品内の表示なら確認項目の違いはないものとする。</li><li>D. D TRACEが成功したためIP SYSTRACEのSYSTEMも正常だと推定する。主出力は保存しない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答の根拠: AはIPCS表示で SYSTEM を読みTRACE STATUSとBUFFERの主値として変更結果を検証しTRC03に残します。
内部の仕組み: 変更後の確認ではトレース状態を補助操作としシステムトレースの反映値と残存値をIEE843Iと対象TRC03で照合します。
誤答を含む比較: IPCS表示とトレース状態の役割を分けるとA: 周辺状態の後にSYSTEMを確認する点でTRC03を判定できます、B: 変更前のTRACE STATUSとBUFFERを失う点でトレース状態の範囲を越えます、C: SAF連携の値ではSYSTEMを確認できないうえに追加前提も不正な点でTRC03の値を示しません、D: 補助操作の成功ではSYSTEMを確定できない点で変更後の確認に合いません。結論として変更後の確認のトレース診断・システムトレースで判定する対象は TRC03 です。
用語定義: 変更後の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC03へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>トレース診断 システムトレース 変更後の確認 TRC03</strong></p><p>検証目的: トレース診断のシステムトレースについて変更結果を検証し、TRC03のTRACE STATUSとBUFFERを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TRC03と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC03のIPCS表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SYSTRACE
→ Enter を押す
［画面・出力］
SYSTEM TRACE TABLE CPU 0000 ASID 0003 EVENT SVC
画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC03のトレース状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.36.21 TRACE DISPLAY 490
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC03のバッファ指定を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; TRACE ST,2M
→ Enter を押す
［画面・出力］
IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC03の対応を確認します。反映値と残存値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SYSTEM が画面・出力に表示されること
② ステップ2 の IEE843I が画面・出力に表示されること
③ ステップ3 の IEE839I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0293"><h3>トレース診断 システムトレース 引継ぎ記録 TRC09</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 上級</p><p>引継ぎ記録では トレース診断 の IPCS表示 を主操作として TRC09 を判定します。次担当者が追跡できる証跡への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC09 に残します。引継ぎ記録を補助する トレース状態 では IEE843I を補助値として TRC09 へ保存します。主判定の引継ぎ記録ではトレース診断・システムトレースの IPCS表示 から SYSTEM を読み TRC09 へ残します。証跡照合の引継ぎ記録ではトレース診断・システムトレースの SYSTEM と IEE843I を TRC09 に保存します。記録対応の引継ぎ記録ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC09 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 引継ぎ記録で トレース診断 の IPCS表示 と トレース状態 を用い 再現可能な記録を作成 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。SYSTEM で対象 TRC09 の TRACE STATUSとBUFFER を再現できる記録はどれですか。</p><ul class="kb-choices"><li>A. D TRACEが成功したためIP SYSTRACEのSYSTEMも正常だと推定する。主出力は保存しない。</li><li>B. IP SYSTRACEを対象名なしで実行する。一覧の先頭行をTRC09の結果として記録する。</li><li>C. 対象名TRC09を指定してIP SYSTRACEを実行する。応答中のSYSTEMと時刻を保存する。D TRACEで周辺状態を補完する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回保存したIP SYSTRACEの結果を使う。今回のD TRACEの結果と同一時点の証跡として比較する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 採用操作の理由: CはIPCS表示で SYSTEM を読みTRACE STATUSとBUFFERの主値として再現可能な記録を作成しTRC09に残します。
製品内の仕組み: 引継ぎ記録ではトレース状態を補助操作としシステムトレースの次担当者が追跡できる証跡をIEE843Iと対象TRC09で照合します。
選択肢別の説明: IPCS表示とトレース状態の役割を分けるとA: 補助操作の成功ではSYSTEMを確定できない点でTRC09の値を示しません、B: 先頭行はTRC09と確定できない点で引継ぎ記録に合いません、C: SYSTEMと時刻を保存する点でIPCS表示に合います、D: 採取時刻が異なる点でトレース診断に使いません。結論として引継ぎ記録のトレース診断・システムトレースで判定する対象は TRC09 です。
用語を初めて使う際の定義: 引継ぎ記録で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC09へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>トレース診断 システムトレース 引継ぎ記録 TRC09</strong></p><p>検証目的: トレース診断のシステムトレースについて再現可能な記録を作成し、TRC09のTRACE STATUSとBUFFERを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TRC09と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC09のIPCS表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SYSTRACE
→ Enter を押す
［画面・出力］
SYSTEM TRACE TABLE CPU 0000 ASID 0009 EVENT SVC
画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC09のトレース状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.36.21 TRACE DISPLAY 490
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC09のバッファ指定を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; TRACE ST,2M
→ Enter を押す
［画面・出力］
IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC09の対応を確認します。次担当者が追跡できる証跡を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SYSTEM が画面・出力に表示されること
② ステップ2 の IEE843I が画面・出力に表示されること
③ ステップ3 の IEE839I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0294"><h3>トレース診断 システムトレース 復旧後の確認 TRC06</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 上級</p><p>復旧後の確認では トレース診断 の IPCS表示 を主操作として TRC06 を判定します。再発していないことを示す値への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC06 に残します。復旧後の確認を補助する トレース状態 では IEE843I を補助値として TRC06 へ保存します。主判定の復旧後の確認ではトレース診断・システムトレースの IPCS表示 から SYSTEM を読み TRC06 へ残します。証跡照合の復旧後の確認ではトレース診断・システムトレースの SYSTEM と IEE843I を TRC06 に保存します。記録対応の復旧後の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC06 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧後の確認で トレース診断 の IPCS表示 と トレース状態 の役割を分け 再発していないことを示す値 を調べます。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。対象 TRC06 を誤判定しない進め方はどれですか。</p><ul class="kb-choices"><li>A. Cross MemoryのHOME ASIDとSECONDARY ASIDを確認する。その値をトレース診断のTRC06にも適用する。</li><li>B. D TRACEが成功したためIP SYSTRACEのSYSTEMも正常だと推定する。主出力は保存しない。別資源で得た状態を対象TRC06へ引き継げるものとする。システムトレースの再発していないことを示す値は確認済みとして扱う。さらにTRACE ST,2MのIEE839IをSYSTEMと同種の値として併記する。</li><li>C. IP SYSTRACEを対象名なしで実行する。一覧の先頭行をTRC06の結果として記録する。</li><li>D. IP SYSTRACEでSYSTEMを取得してからTRACE ST,2MでIEE839Iを照合する。TRC06のTRACE STATUSとBUFFERを両出力から確定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正答内容: DはIPCS表示で SYSTEM を読みTRACE STATUSとBUFFERの主値として復旧後の安定性を確認しTRC06に残します。
構成上の背景: 復旧後の確認ではトレース状態を補助操作としシステムトレースの再発していないことを示す値をIEE843Iと対象TRC06で照合します。
候補ごとの理由: IPCS表示とトレース状態の役割を分けるとA: Cross Memoryの値ではSYSTEMを確認できない点でトレース状態の範囲を越えます、B: 補助操作の成功ではSYSTEMを確定できないうえに追加前提も不正な点でTRC06の値を示しません、C: 先頭行はTRC06と確定できない点で復旧後の確認に合いません、D: SYSTEMとIEE839Iを順に照合する点でIPCS表示に合います。結論として復旧後の確認のトレース診断・システムトレースで判定する対象は TRC06 です。
初出用語: 復旧後の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC06へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>トレース診断 システムトレース 復旧後の確認 TRC06</strong></p><p>検証目的: トレース診断のシステムトレースについて復旧後の安定性を確認し、TRC06のTRACE STATUSとBUFFERを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TRC06と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC06のIPCS表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SYSTRACE
→ Enter を押す
［画面・出力］
SYSTEM TRACE TABLE CPU 0000 ASID 0006 EVENT SVC
画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC06のトレース状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.36.21 TRACE DISPLAY 490
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC06のバッファ指定を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; TRACE ST,2M
→ Enter を押す
［画面・出力］
IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC06の対応を確認します。再発していないことを示す値を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の SYSTEM が画面・出力に表示されること
② ステップ2 の IEE843I が画面・出力に表示されること
③ ステップ3 の IEE839I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0295"><h3>トレース診断 システムトレース 復旧準備 TRC05</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 上級</p><p>復旧準備では トレース診断 の バッファ指定 を主操作として TRC05 を判定します。再開前に必要な整合性への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC05 に残します。復旧準備を補助する IPCS表示 では SYSTEM を補助値として TRC05 へ保存します。主判定の復旧準備ではトレース診断・システムトレースの バッファ指定 から IEE839I を読み TRC05 へ残します。証跡照合の復旧準備ではトレース診断・システムトレースの IEE839I と SYSTEM を TRC05 に保存します。記録対応の復旧準備ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC05 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧準備で トレース診断 の バッファ指定 と IPCS表示 を組み合わせる際は システムトレース が割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能という仕組みを前提にします。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE839I と TRACE STATUSとBUFFER を対象 TRC05 で確認する組合せはどれですか。</p><ul class="kb-choices"><li>A. 前回保存したTRACE ST,2Mの結果を使う。今回のIP SYSTRACEの結果と同一時点の証跡として比較する。</li><li>B. 保存済みのTRC05の出力を再利用する。今回のTRACE ST,2MとIP SYSTRACEは実行済みとして扱う。</li><li>C. 変更を加えずTRACE ST,2Mを実行する。IEE839Iを保存する。差分はIP SYSTRACEの結果と対象名で対応させる。 <span class="kb-ok">✅ 正解</span></li><li>D. IP SYSTRACEのSYSTEMをTRACE STATUSとBUFFERの主判定に採用する。TRACE ST,2Mの応答は採取対象から外す。変更後の値を変更前の基準として記録してよいものとする。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 選定理由: Cはバッファ指定で IEE839I を読みTRACE STATUSとBUFFERの主値として復旧条件を確認しTRC05に残します。
処理の仕組み: 復旧準備ではIPCS表示を補助操作としシステムトレースの再開前に必要な整合性をSYSTEMと対象TRC05で照合します。
選択結果の内訳: バッファ指定とIPCS表示の役割を分けるとA: 採取時刻が異なる点でバッファ指定を代替しません、B: 過去出力では今回の復旧準備を示せない点でトレース診断に使いません、C: 変更前のIEE839Iを保存する点で正答です、D: SYSTEMはIEE839Iを代替しないうえに追加前提も不正な点でTRC05を採用できません。結論として復旧準備のトレース診断・システムトレースで判定する対象は TRC05 です。
用語の説明: 復旧準備で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC05へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>トレース診断 システムトレース 復旧準備 TRC05</strong></p><p>検証目的: トレース診断のシステムトレースについて復旧条件を確認し、TRC05のTRACE STATUSとBUFFERを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TRC05と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC05のバッファ指定を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; TRACE ST,2M
→ Enter を押す
［画面・出力］
IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC05のIPCS表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SYSTRACE
→ Enter を押す
［画面・出力］
SYSTEM TRACE TABLE CPU 0000 ASID 0005 EVENT SVC
画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC05のトレース状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.36.21 TRACE DISPLAY 490
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC05の対応を確認します。再開前に必要な整合性を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE839I が画面・出力に表示されること
② ステップ2 の SYSTEM が画面・出力に表示されること
③ ステップ3 の IEE843I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0296"><h3>トレース診断 システムトレース 構成監査 TRC08</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 上級</p><p>構成監査では トレース診断 の バッファ指定 を主操作として TRC08 を判定します。定義値と稼働値の一致への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC08 に残します。構成監査を補助する IPCS表示 では SYSTEM を補助値として TRC08 へ保存します。主判定の構成監査ではトレース診断・システムトレースの バッファ指定 から IEE839I を読み TRC08 へ残します。証跡照合の構成監査ではトレース診断・システムトレースの IEE839I と SYSTEM を TRC08 に保存します。記録対応の構成監査ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC08 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構成監査で トレース診断 の バッファ指定 と IPCS表示 を実施し システムトレース の役割を確認します。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。対象 TRC08 の証跡を取る方法はどれですか。</p><ul class="kb-choices"><li>A. 保存済みのTRC08の出力を再利用する。今回のTRACE ST,2MとIP SYSTRACEは実行済みとして扱う。</li><li>B. IP SYSTRACEの結果だけでは確定しない。TRACE ST,2MのIEE839Iを主証跡として構成差分を監査する。 <span class="kb-ok">✅ 正解</span></li><li>C. IP SYSTRACEのSYSTEMをTRACE STATUSとBUFFERの主判定に採用する。TRACE ST,2Mの応答は採取対象から外す。</li><li>D. D TRACEのIEE843IをIEE839Iと同義の成功表示として扱う。TRACE ST,2Mは実行しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 技術上の正答: Bはバッファ指定で IEE839I を読みTRACE STATUSとBUFFERの主値として構成差分を監査しTRC08に残します。
実行時の背景: 構成監査ではIPCS表示を補助操作としシステムトレースの定義値と稼働値の一致をSYSTEMと対象TRC08で照合します。
四つの候補の理由: バッファ指定とIPCS表示の役割を分けるとA: 過去出力では今回の構成監査を示せない点でトレース診断に使いません、B: IEE839Iを主証跡として区別する点で正答です、C: SYSTEMはIEE839Iを代替しない点でTRC08を採用できません、D: IEE843IとIEE839Iは確認項目が異なる点で定義値と稼働値の一致を示せません。結論として構成監査のトレース診断・システムトレースで判定する対象は TRC08 です。
初出語定義: 構成監査で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC08へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>トレース診断 システムトレース 構成監査 TRC08</strong></p><p>検証目的: トレース診断のシステムトレースについて構成差分を監査し、TRC08のTRACE STATUSとBUFFERを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TRC08と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC08のバッファ指定を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; TRACE ST,2M
→ Enter を押す
［画面・出力］
IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC08のIPCS表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SYSTRACE
→ Enter を押す
［画面・出力］
SYSTEM TRACE TABLE CPU 0000 ASID 0008 EVENT SVC
画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC08のトレース状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.36.21 TRACE DISPLAY 490
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC08の対応を確認します。定義値と稼働値の一致を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE839I が画面・出力に表示されること
② ステップ2 の SYSTEM が画面・出力に表示されること
③ ステップ3 の IEE843I が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0297"><h3>トレース診断 システムトレース 通常状態の確認 TRC01</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 上級</p><p>通常状態の確認では トレース診断 の トレース状態 を主操作として TRC01 を判定します。基準値と現在値の差への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC01 に残します。通常状態の確認を補助する バッファ指定 では IEE839I を補助値として TRC01 へ保存します。主判定の通常状態の確認ではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC01 へ残します。証跡照合の通常状態の確認ではトレース診断・システムトレースの IEE843I と IEE839I を TRC01 に保存します。記録対応の通常状態の確認ではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC01 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 通常状態の確認で トレース診断 の トレース状態 と バッファ指定 を使い 通常状態を確定 します。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読み対象 TRC01 を切り分ける確認方法はどれですか。</p><ul class="kb-choices"><li>A. TRACE ST,2MのIEE839IをTRACE STATUSとBUFFERの主判定に採用する。D TRACEの応答は採取対象から外す。対象名の差は判定へ影響しないものとする。</li><li>B. IP SYSTRACEのSYSTEMをIEE843Iと同義の成功表示として扱う。D TRACEは実行しない。</li><li>C. D TRACEを先に実行する。対象TRC01のIEE843IをTRACE STATUSとBUFFERとして記録する。続いてTRACE ST,2Mで同一対象を照合する。 <span class="kb-ok">✅ 正解</span></li><li>D. D TRACEが応答を返した時点で正常とする。応答中のIEE843Iの値は記録しない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正解の説明: Cはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として通常状態を確定しTRC01に残します。
背景・仕組み: 通常状態の確認ではバッファ指定を補助操作としシステムトレースの基準値と現在値の差をIEE839Iと対象TRC01で照合します。
選択肢の理由: トレース状態とバッファ指定の役割を分けるとA: IEE839IはIEE843Iを代替しないうえに追加前提も不正な点でシステムトレースに使えません、B: SYSTEMとIEE843Iは確認項目が異なる点でTRC01を採用できません、C: IEE843Iを主値として補助結果と照合する点で主証跡になります、D: 応答の有無だけではTRACE STATUSとBUFFERを判定できない点で一次資料と一致しません。結論として通常状態の確認のトレース診断・システムトレースで判定する対象は TRC01 です。
用語の初出定義: 通常状態の確認で使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC01へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>トレース診断 システムトレース 通常状態の確認 TRC01</strong></p><p>検証目的: トレース診断のシステムトレースについて通常状態を確定し、TRC01のTRACE STATUSとBUFFERを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TRC01と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC01のトレース状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.36.21 TRACE DISPLAY 490
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC01のバッファ指定を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; TRACE ST,2M
→ Enter を押す
［画面・出力］
IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC01のIPCS表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SYSTRACE
→ Enter を押す
［画面・出力］
SYSTEM TRACE TABLE CPU 0000 ASID 0001 EVENT SVC
画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC01の対応を確認します。基準値と現在値の差を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
② ステップ2 の IEE839I が画面・出力に表示されること
③ ステップ3 の SYSTEM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0298"><h3>トレース診断 システムトレース 障害切り分け TRC04</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 上級</p><p>障害切り分けでは トレース診断 の トレース状態 を主操作として TRC04 を判定します。最初に失敗した処理への注意として「必要な事象の前にバッファが上書きされ原因時点を失う危険があります」を TRC04 に残します。障害切り分けを補助する バッファ指定 では IEE839I を補助値として TRC04 へ保存します。主判定の障害切り分けではトレース診断・システムトレースの トレース状態 から IEE843I を読み TRC04 へ残します。証跡照合の障害切り分けではトレース診断・システムトレースの IEE843I と IEE839I を TRC04 に保存します。記録対応の障害切り分けではトレース診断・システムトレースの TRACE STATUSとBUFFER の証跡へ TRC04 を結びます。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 障害切り分けで トレース診断 の トレース状態 と バッファ指定 を照合し 最初に失敗した処理 を確かめます。システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能です。必要な事象の前にバッファが上書きされ原因時点を失う危険があります。IEE843I を読む前に対象 TRC04 へ行う確認はどれですか。</p><ul class="kb-choices"><li>A. IP SYSTRACEのSYSTEMをIEE843Iと同義の成功表示として扱う。D TRACEは実行しない。補助出力があれば主出力の未採取を補えるものとする。</li><li>B. D TRACEの出力でTRC04とIEE843Iが同じ応答にあることを確認する。TRACE STATUSとBUFFERをその応答から採取する。 <span class="kb-ok">✅ 正解</span></li><li>C. D TRACEが応答を返した時点で正常とする。応答中のIEE843Iの値は記録しない。</li><li>D. D TRACEのコマンド文字列だけを記録する。IEE843Iを含む応答行は保存しない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正しい操作の説明: Bはトレース状態で IEE843I を読みTRACE STATUSとBUFFERの主値として障害範囲を限定しTRC04に残します。
技術的背景: 障害切り分けではバッファ指定を補助操作としシステムトレースの最初に失敗した処理をIEE839Iと対象TRC04で照合します。
四択の評価: トレース状態とバッファ指定の役割を分けるとA: SYSTEMとIEE843Iは確認項目が異なるうえに追加前提も不正な点でTRC04を採用できません、B: TRC04とIEE843Iを同じ応答で結ぶ点で主証跡になります、C: 応答の有無だけではTRACE STATUSとBUFFERを判定できない点で一次資料と一致しません、D: 入力記録だけではTRACE STATUSとBUFFERを証明できない点でTRACE STATUSとBUFFERを確認できません。結論として障害切り分けのトレース診断・システムトレースで判定する対象は TRC04 です。
初出語の意味: 障害切り分けで使う システムトレース は割り込み、SVC、ディスパッチ、I/Oなどの直前イベントをCPU別トレース表へ記録する診断機能を表しTRACE STATUSとBUFFERを判定する際にTRC04へ適用します。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>トレース診断 システムトレース 障害切り分け TRC04</strong></p><p>検証目的: トレース診断のシステムトレースについて障害範囲を限定し、TRC04のTRACE STATUSとBUFFERを実出力で確認する。</p><p>前提条件: z/OS System Programmingの参照権限を持ち、対象TRC04と実行時刻を記録できること。変更操作は実施せず机上で確認する。</p><p>セッション環境: z/OS System Programmingの運用画面またはコマンド入力画面</p><pre class="kb-code">■ ステップ 1
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へD TRACEを指定し、TRC04のトレース状態を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; D TRACE
→ Enter を押す
［画面・出力］
IEE843I 19.36.21 TRACE DISPLAY 490
SYSTEM STATUS INFORMATION
ST=(ON,0256K,03584K) AS=ON BR=OFF EX=ON
画面・出力にあるIEE843Iを読み、TRACE STATUSとBUFFERと対象TRC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 2
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へTRACE ST,2Mを指定し、TRC04のバッファ指定を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; TRACE ST,2M
→ Enter を押す
［画面・出力］
IEE839I SYSTEM TRACE OPTIONS CHANGED ST=(ON,2048K)
画面・出力にあるIEE839Iを読み、TRACE STATUSとBUFFERと対象TRC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――
■ ステップ 3
現在の画面はz/OS System Programmingのトレース診断を確認する入力画面です。COMMAND入力口へIP SYSTRACEを指定し、TRC04のIPCS表示を表示します。
［操作（入力）］
z/OS System Programming 操作画面
COMMAND ===&gt; IP SYSTRACE
→ Enter を押す
［画面・出力］
SYSTEM TRACE TABLE CPU 0000 ASID 0004 EVENT SVC
画面・出力にあるSYSTEMを読み、TRACE STATUSとBUFFERと対象TRC04の対応を確認します。最初に失敗した処理を説明できるよう時刻も残します。
――――</pre><p>合格条件: ① ステップ1 の IEE843I が画面・出力に表示されること
② ステップ2 の IEE839I が画面・出力に表示されること
③ ステップ3 の SYSTEM が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol08 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12</p></div></details></section>


<section class="kb-item" id="c38-i0299"><h3>共通サービス域 ログ確認 運用確認084</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 上級</p><p>第八十四観点 z/OS System Programming の トレース診断 では 共通サービス域 を障害調査で照合します（第八十四観点）。第八十四観点 資料上は CSAなど複数アドレス空間から参照される共通ストレージ領域として扱います（第八十四観点）。第八十四観点 ISGLOCK を起点に表示値を戻し、共通ストレージ変更の記録を点検します（第八十四観点）。第八十四観点 記録ではコマンド、メッセージID、対象名、時刻を zOSSP記録084へ書きます（第八十四観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第八十四証跡です。z/OS System Programming の トレース診断 で切分けを行います。確認観点は 共通サービス域、ログ確認、運用確認 です。共通ストレージ変更の記録を満たす記録方法として、表示値と定義を結ぶものはどれか。</p><ul class="kb-choices"><li>A. SVC処理 の一般メモを採り、ISGLOCK、メッセージID、時刻の対応を記録外に置き、zOSSP誤記084として調査範囲を狭める。</li><li>B. 共通サービス域 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延084として扱う。</li><li>C. SWITCH SMF後のSMF切替記録 と ISGLOCK を同一票へ記録し、共通サービス域 を zOSSP正084で確定する。 <span class="kb-ok">✅ 正解</span></li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在084として残す。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 第八十四観点 照合結果: Cは ISGLOCK をメッセージIDや時刻と一緒に残すため、再確認時にも根拠を追えます（第八十四観点）。第八十四観点 仕組み要点: GRSはENQ、DEQ、ISGENQ、RESERVEで資源直列化を扱います（第八十四観点）。第八十四観点 誤答確認: Aは ISGLOCK 未追跡、Bはコマンド確認不足、Dは別システム混同が理由です（第八十四観点）。第八十四観点 初出定義: PSWは実行状態を示す語です（第八十四観点）。第八十四観点 SVCは監視プログラム呼出しです（第八十四観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>共通サービス域 ログ確認 運用確認084</strong></p><p>検証目的: 共通サービス域 の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / SMF</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により 共通サービス域 の値を確認し、対象の現在値を固定する。
［操作（入力）］
MVS console
COMMAND ===&gt; D SMF,O
→ Enter を押す
［画面・出力］
IEE974I 11.01.12 SMF DATA SET STATUS
NAME       VOLSER  STATUS
SMF.MAN1   SMS001  ACTIVE
SMF.MAN2   SMS002  EMPTY
画面・出力には SMF DATA SET STATUS が含まれる。SMF DATA SET STATUS を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により 共通サービス域 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SWITCH SMF
→ Enter を押す
［画面・出力］
IEE362A SMF ENTER DUMP FOR DATA SET SMF.MAN1
IEE360I SMF NOW RECORDING ON SMF.MAN2
画面・出力には IEE360I が含まれる。IEE360I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により 共通サービス域 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
JES2 SDSF ST
COMMAND ===&gt; S IFASMFD12
→ Enter を押す
［画面・出力］
IEF403I IFASMFD12 - STARTED
IFASMFDP SYSPRINT
INDD(DUMPIN,OPTIONS(ALL)) OUTDD(DUMPALL,TYPE(000:255))
画面・出力には IFASMFDP が含まれる。IFASMFDP を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: SMF DATA SET STATUS が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE360I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: IFASMFDP が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>


<section class="kb-item" id="c38-i0300"><h3>私用域 ログ確認 運用確認034</h3><p class="kb-meta">分類: トレース診断 ・ 難易度: 中級</p><p>第三十四観点 私用域 は z/OS System Programming の トレース診断 で扱う管理項目です（第三十四観点）。第三十四観点 各アドレス空間内で利用者プログラムが使う独立した仮想記憶領域という説明を操作結果と照合します（第三十四観点）。第三十四観点 SRB=00AF1100、SWITCH SMF後のSMF切替記録、定義メンバーを照合し、共通ストレージ変更の記録を確認します（第三十四観点）。第三十四観点 証跡には資料IDと確認値を併記し、zOSSP記録034として保存します（第三十四観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 運用第三十四証跡です。z/OS System Programming の トレース診断 で切分けを行います。確認観点は 私用域、ログ確認、運用確認 です。共通ストレージ変更の記録のために、SWITCH SMF後のSMF切替記録 を使った運用記録として最も適切な扱いはどれか。</p><ul class="kb-choices"><li>A. SWITCH SMF後のSMF切替記録 と SRB=00AF1100 を同一票へ記録し、私用域 を zOSSP正034で確定する。 <span class="kb-ok">✅ 正解</span></li><li>B. APF管理 の一般メモを採り、SRB=00AF1100、メッセージID、時刻の対応を記録外に置き、zOSSP誤記034として調査範囲を狭める。</li><li>C. 私用域 の名称確認を優先し、表示出力、parmlib、ジョブログの差分を後回しにして、zOSSP遅延034として扱う。</li><li>D. 前回の正常出力を今回値として採用し、システム名、ASID、メンバー名の差を記録せず、zOSSP混在034として残す。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 第三十四観点 正答根拠: Aは SWITCH SMF後のSMF切替記録 と SRB=00AF1100 を結び付けるため、対象システムの取り違えを防げます（第三十四観点）。第三十四観点 診断背景: LOGREC、D TRACE、IPCS出力は障害時の再現性を支えます（第三十四観点）。第三十四観点 誤答点検: Bはシステム名欠落、Cは定義未確認、Dは時刻差の欠落が理由です（第三十四観点）。第三十四観点 用語説明: WTOは通知メッセージです（第三十四観点）。第三十四観点 WTORは応答を求めるメッセージです（第三十四観点）。</p><p class="kb-src"><strong>出典:</strong> ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>私用域 ログ確認 運用確認034</strong></p><p>検証目的: 私用域 の ログ確認 を、一次資料で確認した操作・表示形式に基づいて机上検証する。</p><p>前提条件: z/OS System Programming の対象LPARで、SDSF、MVSコンソール、ISPF、IPCSのいずれかを利用できること。</p><p>セッション環境: MVS console / parmlib review</p><pre class="kb-code">■ ステップ 1
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。状態表示により 私用域 の値を確認し、対象の現在値を固定する。
［操作（入力）］
ISPF browse
COMMAND ===&gt; BROWSE SYS1.PARMLIB(PROGSP)
→ Enter を押す
［画面・出力］
APF FORMAT(DYNAMIC)
APF ADD DSNAME(MYPROG.LOADLIB) VOLUME(MPRES3)
LPA ADD MODNAME(MOD10) DSNAME(SYS1.LPALIB)
画面・出力には APF FORMAT(DYNAMIC) が含まれる。APF FORMAT(DYNAMIC) を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 2
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。定義照合により 私用域 の値を確認し、定義と資料上の項目を照合する。
［操作（入力）］
MVS console
COMMAND ===&gt; SET PROG=SP
→ Enter を押す
［画面・出力］
IEE252I MEMBER PROGSP FOUND IN SYS1.PARMLIB
IEE536I PROG VALUE SP NOW IN EFFECT
画面・出力には IEE252I が含まれる。IEE252I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――
■ ステップ 3
現在の画面は z/OS のコンソール、SDSF、ISPF、IPCS のいずれかである。ログ確認により 私用域 の値を確認し、同じ対象として記録できることを確認する。
［操作（入力）］
MVS console
COMMAND ===&gt; D PROG,APF
→ Enter を押す
［画面・出力］
CSV450I 06.10.10 PROG,APF DISPLAY 833
FORMAT=DYNAMIC
ENTRY VOLUME DSNAME
  12  MPRES3 MYPROG.LOADLIB
画面・出力には CSV450I が含まれる。CSV450I を読み取り、共通ストレージ変更の記録のため対象の現在値を記録する。
――――</pre><p>合格条件: ステップ1: APF FORMAT(DYNAMIC) が画面または出力に表示され、対象システムやメンバーが取り違えられていないこと。
ステップ2: IEE252I が画面または出力に表示され、定義、コマンド、ログの対応が確認できること。
ステップ3: CSV450I が画面または出力に表示され、記録に残す値と出典が一致すること。</p><p class="kb-meta">検証状態: 机上 ／ 出典: ABCs_of_zOS_System_Programming_Vol02 / ABCs_of_zOS_System_Programming_Vol05 / ABCs_of_zOS_System_Programming_Vol10 / ABCs_of_zOS_System_Programming_Vol11 / ABCs_of_zOS_System_Programming_Vol12 / ABCs_Vol02_zOS_Maintenance_JES_SMP-E p.154 / ABCs_Vol05_Sysplex_Logger_RRS_GRS_ARM_GDPS p.207 / ABCs_Vol10_zArchitecture_HW_LPAR_HCD p.48 / ABCs_Vol11_CapacityPlanning_WLM_RMF_SMF p.258 / ABCs_Vol12_WLM p.110</p></div></details></section>
