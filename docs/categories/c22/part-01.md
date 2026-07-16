---
search:
  exclude: true
---

# MVS オペレータコマンド — 詳細 (1/2)

[← MVS オペレータコマンド の概要へ戻る](index.md)


## AUTO


<section class="kb-item" id="c22-i0001"><h3>AUTOR (Automatic Reply)</h3><p class="kb-meta">分類: AUTO ・ 難易度: 中級</p><p>AUTOR (Automatic Reply)は、MVS オペレータコマンドのAUTOで確認する項目です。z/OS 標準の自動応答機能。AUTORxx で WTOR メッセージに対する事前定義応答を記述する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切検査の操作コマンドで AUTOR (Automatic Reply)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. AUTOR (Automatic Reply)の出力を取らず区切検査の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切検査の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切検査の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切検査の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切検査の操作コマンドにおいて選択記号 B を採用し、識別名は区切検査です。区切検査の操作コマンドにおいて AUTOR (Automatic Reply) は説明欄の「区切検査の操作コマンドに関係する定義値と表示行を照合する区切検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切検査です。区切検査の操作コマンドの証跡を読む担当者は、AUTOR (Automatic Reply)の属性行と IEE115I を合わせて追跡し、背景名は区切検査です。誤答側の問題点を分けます。 A: 区切検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切検査ではありません。 B: 区切検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切検査です。 C: 区切検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切検査ではありません。 D: 区切検査の操作コマンドは別カテゴリの確認を流用しており、AUTOR (Automatic Reply)の根拠にならないため区切検査ではありません。区切検査の操作コマンドに出る AUTOR (Automatic Reply)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AUTOR (Automatic Reply)</strong></p><p>検証目的: 呼出追跡の操作コマンドについて、AUTOR (Automatic Reply)は、MVS オペレータコマンドの AUTO で確認する項目です。z/OS 標準の自動応答機能。AUTORxx で WTOR メッセに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030043の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にAUTOR (Automatic Rを指定し、OSKB030043の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND AUTOR (Automatic R
CASE OSKB030043
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM AUTOR (Automatic R
CASE OSKB030043
SOURCE z/OS MVS Operations
AUTOR (Automatic RとOSKB030043が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030043を同じ出力で読み、呼出追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030043
→ Enter を押す
［画面・出力］
IEE115I OSKB030043 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030043   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030043が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の AUTOR (Automatic R と OSKB030043 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030043 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0002"><h3>MPF 自動応答 (AUTO=YES)</h3><p class="kb-meta">分類: AUTO ・ 難易度: 中級</p><p>MPFLSTxx の AUTO=YES 指定で、メッセージを自動化製品 (SA, NetView 等) に通知。実応答はそちらの規則で行う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件検査の自動応答に関係する MPF 自動応答 (AUTO=YES)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件検査として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. MPF 自動応答 (AUTO=YES)の名称と担当者名のみを残して条件検査の自動応答の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件検査の自動応答を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件検査の自動応答の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件検査の自動応答において選択記号 A を採用し、識別名は条件検査です。条件検査の自動応答において MPF 自動応答 (AUTO=YES) は説明欄の「MPF 自動応答 (AUTO=YES)の用途を操作コマンドの表示で確認する条件検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件検査です。条件検査の自動応答に関連して、z/OS MVS Operationsでは MPF 自動応答 (AUTO=YES)の表示属性と IEE115I を同じ証跡に残し、背景名は条件検査です。他の選択肢を確認します。 A: 条件検査の自動応答は対象出力と項目説明を結び、根拠を残すので条件検査です。 B: 条件検査の自動応答は名称や説明のみに寄り、状態を示す出力本文が不足するため条件検査ではありません。 C: 条件検査の自動応答は別カテゴリの確認を流用しており、MPF 自動応答 (AUTO=YES)の根拠にならないため条件検査ではありません。 D: 条件検査の自動応答は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件検査ではありません。条件検査の自動応答で使う MPF 自動応答 (AUTO=YES)という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MPF 自動応答 (AUTO=YES)</strong></p><p>検証目的: 展開追跡の自動応答について、MPFLSTxx の AUTO=YES 指定で、メッセージを自動化製品 (SA, NetView 等) に通知。実応答はそちらの規則で行うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030042の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開追跡の自動応答の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にMPF 自動応答 (AUTO=YESを指定し、OSKB030042の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND MPF 自動応答 (AUTO=YES
CASE OSKB030042
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM MPF 自動応答 (AUTO=YES
CASE OSKB030042
SOURCE z/OS MVS Operations
MPF 自動応答 (AUTO=YESとOSKB030042が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030042を同じ出力で読み、展開追跡の自動応答の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030042
→ Enter を押す
［画面・出力］
IEE115I OSKB030042 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030042   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030042が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の MPF 自動応答 (AUTO=YES と OSKB030042 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030042 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0003"><h3>SETAUTOR コマンド</h3><p class="kb-meta">分類: AUTO ・ 難易度: 中級</p><p>SETAUTOR コマンドは、MVS オペレータコマンドのAUTOで確認する項目です。AUTORxx の動的活性化コマンド。SETAUTOR=xx で再 IPL なしに自動応答ルールを反映</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲検査のコマンドで操作コマンドの運用確認を行います。SETAUTOR コマンドの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲検査のコマンドを確認した扱いにする。</li><li>B. IEE457I の有無を確認せず範囲検査のコマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲検査の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. SETAUTOR コマンドの属性行を読まず範囲検査のコマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲検査のコマンドにおいて選択記号 C を採用し、識別名は範囲検査です。範囲検査のコマンドにおいて SETAUTOR コマンド は説明欄の「z/OS MVS Operationsで SETAUTOR コマンドの扱いを記録する範囲検査項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は範囲検査です。範囲検査のコマンドを受け取る担当者は、SETAUTOR コマンドの表示結果と IEE457I を同じ確認単位として扱い、背景名は範囲検査です。不適切な選択肢を整理します。 A: 範囲検査のコマンドは別カテゴリの確認を流用しており、SETAUTOR コマンドの根拠にならないため範囲検査ではありません。 B: 範囲検査のコマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため範囲検査ではありません。 C: 範囲検査のコマンドは対象出力と項目説明を結び、根拠を残すので範囲検査です。 D: 範囲検査のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲検査ではありません。範囲検査のコマンドが示す SETAUTOR コマンドは出典欄の資料で使い方を追跡できる項目であり、用語名は範囲検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>SETAUTOR コマンド</strong></p><p>検証目的: 条件追跡のコマンドについて、SETAUTOR コマンドは、MVS オペレータコマンドの AUTO で確認する項目です。AUTORxx の動的活性化コマンド。SETAUTOR=xx で再 IPL なしに自動に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040049の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、条件追跡のコマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D OPDATA
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D OPDATA
COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にSETAUTOR コマンドを指定し、OSKB040049の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SETAUTOR コマンド
CASE OSKB040049
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SETAUTOR コマンド
CASE OSKB040049
SOURCE z/OS MVS Operations
SETAUTOR コマンドとOSKB040049が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040049を同じ出力で読み、条件追跡のコマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB040049
→ Enter を押す
［画面・出力］
IEE457I OSKB040049 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040049   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB040049が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SETAUTOR コマンド と OSKB040049 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB040049 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>SETAUTOR コマンド</strong></p><p>検証目的: 置換追跡のコマンドについて、SETAUTOR コマンドは、MVS オペレータコマンドの AUTO で確認する項目です。AUTORxx の動的活性化コマンド。SETAUTOR=xx で再 IPL なしに自動に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030044の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、置換追跡のコマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D OPDATA
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D OPDATA
COMMAND INPUTにD OPDATAが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にSETAUTOR コマンドを指定し、OSKB030044の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SETAUTOR コマンド
CASE OSKB030044
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SETAUTOR コマンド
CASE OSKB030044
SOURCE z/OS MVS Operations
SETAUTOR コマンドとOSKB030044が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030044を同じ出力で読み、置換追跡のコマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB030044
→ Enter を押す
［画面・出力］
IEE457I OSKB030044 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030044   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB030044が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SETAUTOR コマンド と OSKB030044 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB030044 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## C


<section class="kb-item" id="c22-i0004"><h3>C U=userid TSU キャンセル</h3><p class="kb-meta">分類: C ・ 難易度: 中級</p><p>C U=userid TSU キャンセルは、MVS オペレータコマンドのCで確認する項目です。ログオン中の TSO/E ユーザ・セッションをキャンセルする形式</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端確認再のキャンセルに関係する C 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、終端確認再として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. C 属性の名称と担当者名だけを残して終端確認再のキャンセルの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端確認再のキャンセルを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端確認再のキャンセルの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端確認再正解では選択記号 A を採用し、正解名は終端確認再正解です。終端確認再根拠では C 属性 は「C 属性の用途を操作コマンドの表示で確認する終端確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は終端確認再根拠です。終端確認再背景ではz/OS MVS Operationsの C 属性と IEE115I を同じ証跡に残し、背景名は終端確認再背景です。他の選択肢を確認します。 A: 終端確認再正答は対象出力と項目説明を結び、根拠名は終端確認再正答です。 B: 終端確認再不足は名称や説明だけに寄り、判定名は終端確認再不足です。 C: 終端確認再流用は別カテゴリの確認であり、排除名は終端確認再流用です。 D: 終端確認再欠落は戻り値や記録番号に寄り、欠落名は終端確認再欠落です。終端確認再用語では C 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は終端確認再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>C U=userid TSU キャンセル</strong></p><p>検証目的: 順序照合のキャンセルについて、C U=userid TSU キャンセルは、MVS オペレータコマンドの C で確認する項目です。ログオン中の TSO/E ユーザ・セッションをキャンセルする形式に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040035の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序照合のキャンセルの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にC U=userid TSU キャンを指定し、OSKB040035の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND C U=userid TSU キャン
CASE OSKB040035
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM C U=userid TSU キャン
CASE OSKB040035
SOURCE z/OS MVS Operations
C U=userid TSU キャンとOSKB040035が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040035を同じ出力で読み、順序照合のキャンセルの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040035
→ Enter を押す
［画面・出力］
IEE115I OSKB040035 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040035   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040035が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の C U=userid TSU キャン と OSKB040035 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040035 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>C U=userid TSU キャンセル</strong></p><p>検証目的: 変更検査のキャンセルについて、C U=userid TSU キャンセルは、MVS オペレータコマンドの C で確認する項目です。ログオン中の TSO/E ユーザ・セッションをキャンセルする形式に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020080の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更検査のキャンセルの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にC U=userid TSU キャンを指定し、OSKB020080の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND C U=userid TSU キャン
CASE OSKB020080
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM C U=userid TSU キャン
CASE OSKB020080
SOURCE z/OS MVS Operations
C U=userid TSU キャンとOSKB020080が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020080を同じ出力で読み、変更検査のキャンセルの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020080
→ Enter を押す
［画面・出力］
IEE115I OSKB020080 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020080   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020080が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の C U=userid TSU キャン と OSKB020080 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020080 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0005"><h3>C jobname 通常キャンセル</h3><p class="kb-meta">分類: C ・ 難易度: 中級</p><p>C jobname 通常キャンセルは、MVS オペレータコマンドのCで確認する項目です。ジョブ / STC / TSU を強制終了する。EOJ クリーンアップは行われるが SVC ダンプは生成されない</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開確認再の通常キャンセルで C jobname 通常キャンセルの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. C jobname 通常キャンセルの出力を取らず展開確認再の通常キャンセルの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて展開確認再の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開確認再の通常キャンセルの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開確認再の通常キャンセルへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開確認再正解では選択記号 B を採用し、正解名は展開確認再正解です。展開確認再根拠では C jobname 通常キャンセル は「展開確認再の通常キャンセルに関係する定義値と表示行を照合する展開確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は展開確認再根拠です。展開確認再追跡では C jobname 通常キャンセルの属性行と IEE115I を合わせ、追跡名は展開確認再追跡です。誤答側の問題点を分けます。 A: 展開確認再不足は名称や説明だけに寄り、判定名は展開確認再不足です。 B: 展開確認再正答は対象出力と項目説明を結び、根拠名は展開確認再正答です。 C: 展開確認再欠落は戻り値や記録番号に寄り、欠落名は展開確認再欠落です。 D: 展開確認再流用は別カテゴリの確認であり、排除名は展開確認再流用です。展開確認再初出では C jobname 通常キャンセルを MVS オペレータコマンドの運用手順で確認し、初出名は展開確認再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>C jobname 通常キャンセル</strong></p><p>検証目的: 警告検査の通常キャンセルについて、C jobname 通常キャンセルは、MVS オペレータコマンドの C で確認する項目です。ジョブ / STC / TSU を強制終了する。EOJ クリーンアップは行われるがに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020077の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告検査の通常キャンセルの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にC jobname 通常キャンセルを指定し、OSKB020077の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND C jobname 通常キャンセル
CASE OSKB020077
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM C jobname 通常キャンセル
CASE OSKB020077
SOURCE z/OS MVS Operations
C jobname 通常キャンセルとOSKB020077が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020077を同じ出力で読み、警告検査の通常キャンセルの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020077
→ Enter を押す
［画面・出力］
IEE115I OSKB020077 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020077   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020077が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の C jobname 通常キャンセル と OSKB020077 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020077 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0006"><h3>C jobname,A=asid</h3><p class="kb-meta">分類: C ・ 難易度: 中級</p><p>C jobname,A=asidは、MVS オペレータコマンドのCで確認する項目です。同一名のジョブが複数アドレス・スペースで動いている場合、ASID で対象を特定してキャンセルする</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換確認再の操作コマンドに関する C jobname 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換確認再の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換確認再の操作コマンドの証跡として保存して根拠にする。</li><li>C. C jobname 命令の変更点を出力本文から切り離して置換確認再の操作コマンドの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、置換確認再の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換確認再正解では選択記号 D を採用し、正解名は置換確認再正解です。置換確認再根拠では C jobname 命令 は「C jobname 命令の状態と出力メッセージを結び付ける置換確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は置換確認再根拠です。置換確認再保存では C jobname 命令の出力行と IEE115I を一緒に残し、保存名は置換確認再保存です。選択肢ごとの違いを示します。 A: 置換確認再欠落は戻り値や記録番号に寄り、欠落名は置換確認再欠落です。 B: 置換確認再流用は別カテゴリの確認であり、排除名は置換確認再流用です。 C: 置換確認再不足は名称や説明だけに寄り、判定名は置換確認再不足です。 D: 置換確認再正答は対象出力と項目説明を結び、根拠名は置換確認再正答です。置換確認再対象では C jobname 命令をz/OS MVS Operationsの確認記録に残し、対象名は置換確認再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>C jobname,A=asid</strong></p><p>検証目的: 監査検査の操作コマンドについて、C jobname,A=asidは、MVS オペレータコマンドの C で確認する項目です。同一名のジョブが複数アドレス・スペースで動いている場合、ASID で対象を特定してキャに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020079の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にC jobname,A=asidを指定し、OSKB020079の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND C jobname,A=asid
CASE OSKB020079
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM C jobname,A=asid
CASE OSKB020079
SOURCE z/OS MVS Operations
C jobname,A=asidとOSKB020079が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020079を同じ出力で読み、監査検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020079
→ Enter を押す
［画面・出力］
IEE115I OSKB020079 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020079   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020079が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の C jobname,A=asid と OSKB020079 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020079 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0007"><h3>C jobname,A=asid,DUMP の併用</h3><p class="kb-meta">分類: C ・ 難易度: 中級</p><p>C jobname,A=asid,DUMP の併用は、MVS オペレータコマンドのCで確認する項目です。ASID 特定 + ダンプ取得の組合せ。複数インスタンス環境での確実な証拠取得形式</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書確認再の併で操作コマンドの運用確認を行います。C jobname 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書確認再の併を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書確認再の併を正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、上書確認再の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. C jobname 命令の属性行を読まず上書確認再の併の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書確認再正解では選択記号 C を採用し、正解名は上書確認再正解です。上書確認再根拠では C jobname 命令 は「z/OS MVS Operationsで C jobname 命令の扱いを記録する上書確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は上書確認再根拠です。上書確認再受渡では C jobname 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は上書確認再受渡です。不適切な選択肢を整理します。 A: 上書確認再流用は別カテゴリの確認であり、排除名は上書確認再流用です。 B: 上書確認再欠落は戻り値や記録番号に寄り、欠落名は上書確認再欠落です。 C: 上書確認再正答は対象出力と項目説明を結び、根拠名は上書確認再正答です。 D: 上書確認再不足は名称や説明だけに寄り、判定名は上書確認再不足です。上書確認再資料では C jobname 命令の使い方を出典欄から追跡し、資料名は上書確認再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>C jobname,A=asid,DUMP の併用</strong></p><p>検証目的: 展開判定のの併について、C jobname,A=asid,DUMP の併用は、MVS オペレータコマンドの C で確認する項目です。ASID 特定 + ダンプ取得の組合せ。複数インスタンス環境での確実に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020082の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開判定のの併の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にC jobname,A=asid,Dを指定し、OSKB020082の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND C jobname,A=asid,D
CASE OSKB020082
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM C jobname,A=asid,D
CASE OSKB020082
SOURCE z/OS MVS Operations
C jobname,A=asid,DとOSKB020082が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020082を同じ出力で読み、展開判定のの併の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020082
→ Enter を押す
［画面・出力］
IEE115I OSKB020082 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020082   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020082が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の C jobname,A=asid,D と OSKB020082 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020082 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0008"><h3>C jobname,DUMP</h3><p class="kb-meta">分類: C ・ 難易度: 中級</p><p>C jobname,DUMPは、MVS オペレータコマンドのCで確認する項目です。キャンセルと同時に SVC ダンプを取得する。プログラム異常の証拠保全用に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出確認再の操作コマンドで操作コマンドの運用確認を行います。C jobname,DUMP の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出確認再の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出確認再の操作コマンドを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、呼出確認再の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. C jobname,DUMP の属性行を読まず呼出確認再の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出確認再正解では選択記号 C を採用し、正解名は呼出確認再正解です。呼出確認再根拠では C jobname,DUMP は「z/OS MVS Operationsで C jobname,DUMP の扱いを記録する呼出確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出確認再根拠です。呼出確認再受渡では C jobname,DUMP の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出確認再受渡です。不適切な選択肢を整理します。 A: 呼出確認再流用は別カテゴリの確認であり、排除名は呼出確認再流用です。 B: 呼出確認再欠落は戻り値や記録番号に寄り、欠落名は呼出確認再欠落です。 C: 呼出確認再正答は対象出力と項目説明を結び、根拠名は呼出確認再正答です。 D: 呼出確認再不足は名称や説明だけに寄り、判定名は呼出確認再不足です。呼出確認再資料では C jobname,DUMP の使い方を出典欄から追跡し、資料名は呼出確認再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>C jobname,DUMP</strong></p><p>検証目的: 復旧検査の操作コマンドについて、C jobname,DUMP は、MVS オペレータコマンドの C で確認する項目です。キャンセルと同時に SVC ダンプを取得する。プログラム異常の証拠保全用に使うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020078の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にC jobname,DUMPを指定し、OSKB020078の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND C jobname,DUMP
CASE OSKB020078
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM C jobname,DUMP
CASE OSKB020078
SOURCE z/OS MVS Operations
C jobname,DUMPとOSKB020078が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020078を同じ出力で読み、復旧検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020078
→ Enter を押す
［画面・出力］
IEE115I OSKB020078 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020078   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020078が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の C jobname,DUMP と OSKB020078 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020078 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0009"><h3>C tsuname (TSU 直接指定)</h3><p class="kb-meta">分類: C ・ 難易度: 中級</p><p>C tsuname (TSU 直接指定)は、MVS オペレータコマンドのCで確認する項目です。TSU 名 (= ユーザ ID) を直接指定して TSO セッションを終了させる。U= 形式と等価</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索確認再の直接指定で C tsuname 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. C tsuname 属性の出力を取らず探索確認再の直接指定の説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索確認再の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索確認再の直接指定の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索確認再の直接指定へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索確認再正解では選択記号 B を採用し、正解名は探索確認再正解です。探索確認再根拠では C tsuname 属性 は「探索確認再の直接指定に関係する定義値と表示行を照合する探索確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は探索確認再根拠です。探索確認再追跡では C tsuname 属性の属性行と IEE115I を合わせ、追跡名は探索確認再追跡です。誤答側の問題点を分けます。 A: 探索確認再不足は名称や説明だけに寄り、判定名は探索確認再不足です。 B: 探索確認再正答は対象出力と項目説明を結び、根拠名は探索確認再正答です。 C: 探索確認再欠落は戻り値や記録番号に寄り、欠落名は探索確認再欠落です。 D: 探索確認再流用は別カテゴリの確認であり、排除名は探索確認再流用です。探索確認再初出では C tsuname 属性を MVS オペレータコマンドの運用手順で確認し、初出名は探索確認再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>C tsuname (TSU 直接指定)</strong></p><p>検証目的: 構文判定の直接指定について、C tsuname (TSU 直接指定)は、MVS オペレータコマンドの C で確認する項目です。TSU 名 (= ユーザ ID) を直接指定して TSO セッションを終了させに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020081の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文判定の直接指定の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にC tsuname (TSU 直接指を指定し、OSKB020081の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND C tsuname (TSU 直接指
CASE OSKB020081
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM C tsuname (TSU 直接指
CASE OSKB020081
SOURCE z/OS MVS Operations
C tsuname (TSU 直接指とOSKB020081が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020081を同じ出力で読み、構文判定の直接指定の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020081
→ Enter を押す
［画面・出力］
IEE115I OSKB020081 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020081   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020081が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の C tsuname (TSU 直接指 と OSKB020081 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020081 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## CONFIG


<section class="kb-item" id="c22-i0010"><h3>CONFIG CHP(chp),ONLINE</h3><p class="kb-meta">分類: CONFIG ・ 難易度: 中級</p><p>CONFIG CHP(chp),ONLINEは、MVS オペレータコマンドのCONFIGで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域追跡の操作コマンドに関する CONFIG CHP(chp),ONLINE の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域追跡の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域追跡の操作コマンドの証跡として保存して根拠にする。</li><li>C. CONFIG CHP(chp),ONLINE の変更点を出力本文から切り離して値域追跡の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、値域追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域追跡の操作コマンドにおいて選択記号 D を採用し、識別名は値域追跡です。値域追跡の操作コマンドにおいて CONFIG CHP(chp),ONLINE は説明欄の「CONFIG CHP(chp),ONLINE の状態と出力メッセージを結び付ける値域追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域追跡です。値域追跡の操作コマンドに関する記録は、CONFIG CHP(chp),ONLINE の出力行と IEE115I を一緒に保存し、背景名は値域追跡です。選択肢ごとの違いを示します。 A: 値域追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域追跡ではありません。 B: 値域追跡の操作コマンドは別カテゴリの確認を流用しており、CONFIG CHP(chp),ONLINE の根拠にならないため値域追跡ではありません。 C: 値域追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域追跡ではありません。 D: 値域追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので値域追跡です。値域追跡の操作コマンドで記録する CONFIG CHP(chp),ONLINE はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CONFIG CHP(chp),ONLINE</strong></p><p>検証目的: 条件照合の操作コマンドについて、CONFIG CHP(chp),ONLINE は、MVS オペレータコマンドの CONFIG で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030029の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCONFIG CHP(chp),ONを指定し、OSKB030029の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CONFIG CHP(chp),ON
CASE OSKB030029
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CONFIG CHP(chp),ON
CASE OSKB030029
SOURCE z/OS MVS Operations
CONFIG CHP(chp),ONとOSKB030029が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030029を同じ出力で読み、条件照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030029
→ Enter を押す
［画面・出力］
IEE115I OSKB030029 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030029   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030029が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の CONFIG CHP(chp),ON と OSKB030029 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030029 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0011"><h3>CONFIG CPU(n),OFFLINE</h3><p class="kb-meta">分類: CONFIG ・ 難易度: 中級</p><p>CONFIG CPU(n),OFFLINEは、MVS オペレータコマンドのCONFIGで確認する項目です。指定論理 CP をオフラインにする。キャパシティ調整・課金最適化用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録追跡の操作コマンドに関係する CONFIG CPU(n),OFFLINE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、記録追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. CONFIG CPU(n),OFFLINE の名称と担当者名のみを残して記録追跡の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で記録追跡の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録追跡の操作コマンドにおいて選択記号 A を採用し、識別名は記録追跡です。記録追跡の操作コマンドにおいて CONFIG CPU(n),OFFLINE は説明欄の「CONFIG CPU(n),OFFLINE の用途を操作コマンドの表示で確認する記録追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録追跡です。記録追跡の操作コマンドに関連して、z/OS MVS Operationsでは CONFIG CPU(n),OFFLINE の表示属性と IEE115I を同じ証跡に残し、背景名は記録追跡です。他の選択肢を確認します。 A: 記録追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録追跡です。 B: 記録追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録追跡ではありません。 C: 記録追跡の操作コマンドは別カテゴリの確認を流用しており、CONFIG CPU(n),OFFLINE の根拠にならないため記録追跡ではありません。 D: 記録追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録追跡ではありません。記録追跡の操作コマンドで使う CONFIG CPU(n),OFFLINE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>CONFIG CPU(n),OFFLINE</strong></p><p>検証目的: 探索追跡の操作コマンドについて、CONFIG CPU(n),OFFLINE は、MVS オペレータコマンドの CONFIG で確認する項目です。指定論理 CP をオフラインにする。キャパシティ調整・課金最適化用に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040046の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、探索追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCONFIG CPU(n),OFFLを指定し、OSKB040046の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CONFIG CPU(n),OFFL
CASE OSKB040046
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CONFIG CPU(n),OFFL
CASE OSKB040046
SOURCE z/OS MVS Operations
CONFIG CPU(n),OFFLとOSKB040046が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040046を同じ出力で読み、探索追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040046
→ Enter を押す
［画面・出力］
IEE115I OSKB040046 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040046   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040046が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の CONFIG CPU(n),OFFL と OSKB040046 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040046 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>CONFIG CPU(n),OFFLINE</strong></p><p>検証目的: 探索照合の操作コマンドについて、CONFIG CPU(n),OFFLINE は、MVS オペレータコマンドの CONFIG で確認する項目です。指定論理 CP をオフラインにする。キャパシティ調整・課金最適化用に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030026の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、探索照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCONFIG CPU(n),OFFLを指定し、OSKB030026の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CONFIG CPU(n),OFFL
CASE OSKB030026
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CONFIG CPU(n),OFFL
CASE OSKB030026
SOURCE z/OS MVS Operations
CONFIG CPU(n),OFFLとOSKB030026が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030026を同じ出力で読み、探索照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030026
→ Enter を押す
［画面・出力］
IEE115I OSKB030026 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030026   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030026が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の CONFIG CPU(n),OFFL と OSKB030026 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030026 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0012"><h3>CONFIG CPU(n),ONLINE</h3><p class="kb-meta">分類: CONFIG ・ 難易度: 中級</p><p>CONFIG CPU(n),ONLINEは、MVS オペレータコマンドのCONFIGで確認する項目です。指定論理 CP をオンライン化する。OOCoD・キャパシティ追加時の動的活性化手段</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先追跡の操作コマンドに関する CONFIG CPU(n),ONLINE の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先追跡の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先追跡の操作コマンドの証跡として保存して根拠にする。</li><li>C. CONFIG CPU(n),ONLINE の変更点を出力本文から切り離して優先追跡の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先追跡の操作コマンドにおいて選択記号 D を採用し、識別名は優先追跡です。優先追跡の操作コマンドにおいて CONFIG CPU(n),ONLINE は説明欄の「CONFIG CPU(n),ONLINE の状態と出力メッセージを結び付ける優先追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先追跡です。優先追跡の操作コマンドに関する記録は、CONFIG CPU(n),ONLINE の出力行と IEE115I を一緒に保存し、背景名は優先追跡です。選択肢ごとの違いを示します。 A: 優先追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先追跡ではありません。 B: 優先追跡の操作コマンドは別カテゴリの確認を流用しており、CONFIG CPU(n),ONLINE の根拠にならないため優先追跡ではありません。 C: 優先追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先追跡ではありません。 D: 優先追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので優先追跡です。優先追跡の操作コマンドで記録する CONFIG CPU(n),ONLINE はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CONFIG CPU(n),ONLINE</strong></p><p>検証目的: 終端照合の操作コマンドについて、CONFIG CPU(n),ONLINE は、MVS オペレータコマンドの CONFIG で確認する項目です。指定論理 CP をオンライン化する。OOCoD ・キャパシティ追加時のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030025の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCONFIG CPU(n),ONLIを指定し、OSKB030025の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CONFIG CPU(n),ONLI
CASE OSKB030025
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CONFIG CPU(n),ONLI
CASE OSKB030025
SOURCE z/OS MVS Operations
CONFIG CPU(n),ONLIとOSKB030025が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030025を同じ出力で読み、終端照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030025
→ Enter を押す
［画面・出力］
IEE115I OSKB030025 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030025   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030025が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の CONFIG CPU(n),ONLI と OSKB030025 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030025 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0013"><h3>CONFIG STOR(amount),OFFLINE</h3><p class="kb-meta">分類: CONFIG ・ 難易度: 中級</p><p>CONFIG STOR(amount),OFFLINEは、MVS オペレータコマンドのCONFIGで確認する項目です。実ストレージを動的にオフラインにする。LPAR 容量回収時に使用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序追跡の操作コマンドで操作コマンドの運用確認を行います。CONFIG STOR(amount),OFFL の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序追跡の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、順序追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. CONFIG STOR(amount),OFFL の属性行を読まず順序追跡の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序追跡の操作コマンドにおいて選択記号 C を採用し、識別名は順序追跡です。順序追跡の操作コマンドにおいて CONFIG STOR(amount),OFFL は説明欄の「z/OS MVS Operationsで CONFIG STOR(amount),OFFL の扱いを記録する順序追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は順序追跡です。順序追跡の操作コマンドを受け取る担当者は、CONFIG STOR(amount),OFFL の表示結果と IEE115I を同じ確認単位として扱い、背景名は順序追跡です。不適切な選択肢を整理します。 A: 順序追跡の操作コマンドは別カテゴリの確認を流用しており、CONFIG STOR(amount),OFFL の根拠にならないため順序追跡ではありません。 B: 順序追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため順序追跡ではありません。 C: 順序追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので順序追跡です。 D: 順序追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため順序追跡ではありません。順序追跡の操作コマンドが示す CONFIG STOR(amount),OFFL は出典欄の資料で使い方を追跡できる項目であり、用語名は順序追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CONFIG STOR(amount),OFFLINE</strong></p><p>検証目的: 出力照合の操作コマンドについて、CONFIG STOR(amount),OFFLINE は、MVS オペレータコマンドの CONFIG で確認する項目です。実ストレージを動的にオフラインにする。LPAR 容量回に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030028の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCONFIG STOR(amountを指定し、OSKB030028の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CONFIG STOR(amount
CASE OSKB030028
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CONFIG STOR(amount
CASE OSKB030028
SOURCE z/OS MVS Operations
CONFIG STOR(amountとOSKB030028が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030028を同じ出力で読み、出力照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030028
→ Enter を押す
［画面・出力］
IEE115I OSKB030028 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030028   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030028が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の CONFIG STOR(amount と OSKB030028 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030028 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0014"><h3>CONFIG STOR(amount),ONLINE</h3><p class="kb-meta">分類: CONFIG ・ 難易度: 中級</p><p>CONFIG STOR(amount),ONLINEは、MVS オペレータコマンドのCONFIGで確認する項目です。実ストレージを動的に追加オンライン化する。LPAR Reserved Storage の活性化</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較追跡の操作コマンドで CONFIG STOR(amount),ONLI の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. CONFIG STOR(amount),ONLI の出力を取らず比較追跡の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、比較追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較追跡の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較追跡の操作コマンドにおいて選択記号 B を採用し、識別名は比較追跡です。比較追跡の操作コマンドにおいて CONFIG STOR(amount),ONLI は説明欄の「比較追跡の操作コマンドに関係する定義値と表示行を照合する比較追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較追跡です。比較追跡の操作コマンドの証跡を読む担当者は、CONFIG STOR(amount),ONLI の属性行と IEE115I を合わせて追跡し、背景名は比較追跡です。誤答側の問題点を分けます。 A: 比較追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較追跡ではありません。 B: 比較追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較追跡です。 C: 比較追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較追跡ではありません。 D: 比較追跡の操作コマンドは別カテゴリの確認を流用しており、CONFIG STOR(amount),ONLI の根拠にならないため比較追跡ではありません。比較追跡の操作コマンドに出る CONFIG STOR(amount),ONLI は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CONFIG STOR(amount),ONLINE</strong></p><p>検証目的: 上書照合の操作コマンドについて、CONFIG STOR(amount),ONLINE は、MVS オペレータコマンドの CONFIG で確認する項目です。実ストレージを動的に追加オンライン化する。LPAR Reに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030027の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にCONFIG STOR(amountを指定し、OSKB030027の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CONFIG STOR(amount
CASE OSKB030027
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CONFIG STOR(amount
CASE OSKB030027
SOURCE z/OS MVS Operations
CONFIG STOR(amountとOSKB030027が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030027を同じ出力で読み、上書照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030027
→ Enter を押す
［画面・出力］
IEE115I OSKB030027 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030027   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030027が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の CONFIG STOR(amount と OSKB030027 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030027 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D A


<section class="kb-item" id="c22-i0015"><h3>D A 単独 (引数なし)</h3><p class="kb-meta">分類: D A ・ 難易度: 中級</p><p>D A 単独 (引数なし)は、MVS オペレータコマンドのD Aで確認する項目です。現在アクティブなアドレス・スペース数の集計サマリのみを 1 行で返す。詳細リストは出さない軽量形式</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力確認の単独 引数なしに関する D A 単独 (引数なし)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力確認の単独 引数なしの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力確認の単独 引数なしの証跡として保存して根拠にする。</li><li>C. D A 単独 (引数なし)の変更点を出力本文から切り離して出力確認の単独 引数なしの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、出力確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では D A 単独 (引数なし) は「D A 単独 (引数なし)の状態と出力メッセージを結び付ける出力確認項目」と D A,L または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では D A 単独 (引数なし)の出力行と IEE115I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明だけに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では D A 単独 (引数なし)をz/OS MVS Operationsの確認記録に残し、対象名は出力確認対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D A 単独 (引数なし)</strong></p><p>検証目的: 呼出確認の単独 引数なしについて、D A 単独 (引数なし)は、MVS オペレータコマンドの D A で確認する項目です。現在アクティブなアドレス・スペース数の集計サマリのみを 1 行で返す。詳細リストは出さなに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出確認の単独 引数なしの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD A 単独 (引数なし)を指定し、OSKB010003の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D A 単独 (引数なし)
CASE OSKB010003
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D A 単独 (引数なし)
CASE OSKB010003
SOURCE z/OS MVS Operations
D A 単独 (引数なし)とOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010003を同じ出力で読み、呼出確認の単独 引数なしの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010003
→ Enter を押す
［画面・出力］
IEE115I OSKB010003 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010003   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D A 単独 (引数なし) と OSKB010003 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0016"><h3>D A,ALL 全アドレス・スペース</h3><p class="kb-meta">分類: D A ・ 難易度: 中級</p><p>D A,ALL 全アドレス・スペースは、MVS オペレータコマンドのD Aで状態表示や操作を行うためのコマンド関連項目です。D A,ALL 全アドレス・スペースは、ジョブ/STC/TSU だけでなくシステムアドレス・スペース (MASTER, PCAUTH, RASP, GRS, CONSOLE 等) を含めて全て表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書確認の全アドレス・スペースで操作コマンドの運用確認を行います。D A 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書確認の全アドレス・スペースを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書確認の全アドレス・スペースを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を上書確認で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D A 命令の属性行を読まず上書確認の全アドレス・スペースの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では D A 命令 は「z/OS MVS Operationsで D A 命令の扱いを記録する上書確認項目」と D A,L または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では D A 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明だけに寄り、判定名は上書確認不足です。上書確認資料では D A 命令の使い方を出典欄から追跡し、資料名は上書確認資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D A,ALL 全アドレス・スペース</strong></p><p>検証目的: 展開確認の全アドレス・スペースについて、D A,ALL 全アドレス・スペースは、MVS オペレータコマンドの D A で状態表示や操作を行うためのコマンド関連項目です。D A,ALL 全アドレス・スペースは、ジョブ/に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040002の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開確認の全アドレス・スペースの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD A,ALL 全アドレス・スペースを指定し、OSKB040002の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D A,ALL 全アドレス・スペース
CASE OSKB040002
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D A,ALL 全アドレス・スペース
CASE OSKB040002
SOURCE z/OS MVS Operations
D A,ALL 全アドレス・スペースとOSKB040002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040002を同じ出力で読み、展開確認の全アドレス・スペースの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040002
→ Enter を押す
［画面・出力］
IEE115I OSKB040002 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040002   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D A,ALL 全アドレス・スペース と OSKB040002 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D A,ALL 全アドレス・スペース</strong></p><p>検証目的: 展開確認の全アドレス・スペースについて、D A,ALL 全アドレス・スペースは、MVS オペレータコマンドの D A で状態表示や操作を行うためのコマンド関連項目です。D A,ALL 全アドレス・スペースは、ジョブ/に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開確認の全アドレス・スペースの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD A,ALL 全アドレス・スペースを指定し、OSKB010002の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D A,ALL 全アドレス・スペース
CASE OSKB010002
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D A,ALL 全アドレス・スペース
CASE OSKB010002
SOURCE z/OS MVS Operations
D A,ALL 全アドレス・スペースとOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010002を同じ出力で読み、展開確認の全アドレス・スペースの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010002
→ Enter を押す
［画面・出力］
IEE115I OSKB010002 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010002   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D A,ALL 全アドレス・スペース と OSKB010002 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0017"><h3>D A,L 出力フォーマット</h3><p class="kb-meta">分類: D A ・ 難易度: 中級</p><p>D A,L 出力フォーマットは、MVS オペレータコマンドのD Aで状態表示や操作を行うためのコマンド関連項目です。JOBNAME / STEPNAME / PROCSTEP / JOBID / OWNER / A=ASID / PER=(CPU) などを 1 ジョブ 1 行で表示。先頭に IEE114I / IEE115I 等のメッセージ ID が付く</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開確認の出力フォーマットで D A,L 出力フォーマットの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L 出力フォーマットの出力を取らず展開確認の出力フォーマットの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開確認の出力フォーマットの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開確認の出力フォーマットへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では D A,L 出力フォーマット は「展開確認の出力フォーマットに関係する定義値と表示行を照合する展開確認項目」と D A,L または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では D A,L 出力フォーマットの属性行と IEE115I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明だけに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では D A,L 出力フォーマットを MVS オペレータコマンドの運用手順で確認し、初出名は展開確認初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details></section>


<section class="kb-item" id="c22-i0018"><h3>D A,L 目的</h3><p class="kb-meta">分類: D A ・ 難易度: 初級</p><p>D A,L 目的は、MVS オペレータコマンドのD Aで状態表示や操作を行うためのコマンド関連項目です。D A,L 目的は、システム上で現在アクティブな全てのジョブ・STC・TSU・APPC イニシエータ等を一覧表示する最も頻用の状態確認コマンド</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文確認の目的に関係する D A,L 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、構文確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D A,L 目的の名称と担当者名だけを残して構文確認の目的の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文確認の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文確認の目的の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では D A,L 目的 は「D A,L 目的の用途を操作コマンドの表示で確認する構文確認項目」と D A,L または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景ではz/OS MVS Operationsの D A,L 目的と IEE115I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明だけに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では D A,L 目的を MVS オペレータコマンドで扱う確認対象とし、用語名は構文確認用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D A,L 目的</strong></p><p>検証目的: 構文確認の目的について、D A,L 目的は、MVS オペレータコマンドの D A で状態表示や操作を行うためのコマンド関連項目です。D A,L 目的は、システム上で現在アクティブな全てのジョブ・ STCに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040001の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文確認の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD A,L 目的を指定し、OSKB040001の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D A,L 目的
CASE OSKB040001
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D A,L 目的
CASE OSKB040001
SOURCE z/OS MVS Operations
D A,L 目的とOSKB040001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040001を同じ出力で読み、構文確認の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040001
→ Enter を押す
［画面・出力］
IEE115I OSKB040001 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040001   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D A,L 目的 と OSKB040001 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0019"><h3>D A,L 表示種別の意味</h3><p class="kb-meta">分類: D A ・ 難易度: 中級</p><p>D A,L 表示種別の意味は、MVS オペレータコマンドのD Aで状態表示や操作を行うためのコマンド関連項目です。D A,L 表示種別の意味は、末尾に T=TSU、S=STC、J=JOB の種別が付与され、出力ジョブと TSU セッション、開始済みタスクを区別できる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出確認の表示種別の意味で操作コマンドの運用確認を行います。D A,L 表示種別の意味の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出確認の表示種別の意味を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出確認の表示種別の意味を正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、呼出確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D A,L 表示種別の意味の属性行を読まず呼出確認の表示種別の意味の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では D A,L 表示種別の意味 は「z/OS MVS Operationsで D A,L 表示種別の意味の扱いを記録する呼出確認項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では D A,L 表示種別の意味の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明だけに寄り、判定名は呼出確認不足です。呼出確認資料では D A,L 表示種別の意味の使い方を出典欄から追跡し、資料名は呼出確認資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details></section>


<section class="kb-item" id="c22-i0020"><h3>D A,STC のみ表示</h3><p class="kb-meta">分類: D A ・ 難易度: 中級</p><p>D A,STC のみ表示は、MVS オペレータコマンドのD Aで状態表示や操作を行うためのコマンド関連項目です。開始タスク (Started Task) のみに絞り込んで表示する。常駐サブシステム (TCP/IP, JES2, RACF, LLA 等) の稼働確認に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端確認のみ表示に関係する D A,STC のみ表示の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、終端確認の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D A,STC のみ表示の名称と担当者名だけを残して終端確認のみ表示の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端確認のみ表示を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端確認のみ表示の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では D A,STC のみ表示 は「D A,STC のみ表示の用途を操作コマンドの表示で確認する終端確認項目」と D A,L または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景ではz/OS MVS Operationsの D A,STC のみ表示と IEE115I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明だけに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では D A,STC のみ表示を MVS オペレータコマンドで扱う確認対象とし、用語名は終端確認用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details></section>


<section class="kb-item" id="c22-i0021"><h3>D A,TSU のみ表示</h3><p class="kb-meta">分類: D A ・ 難易度: 中級</p><p>D A,TSU のみ表示は、MVS オペレータコマンドのD Aで確認する項目です。TSO/E ユーザ・セッションだけを表示。誰がログオン中か、どのアドレス・スペースを使用しているか確認する典型用途</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索確認のみ表示で D A,TSU のみ表示の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D A,TSU のみ表示の出力を取らず探索確認のみ表示の説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて探索確認の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索確認のみ表示の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索確認のみ表示へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では D A,TSU のみ表示 は「探索確認のみ表示に関係する定義値と表示行を照合する探索確認項目」と D A,L または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では D A,TSU のみ表示の属性行と IEE115I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明だけに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では D A,TSU のみ表示を MVS オペレータコマンドの運用手順で確認し、初出名は探索確認初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D A,TSU のみ表示</strong></p><p>検証目的: 構文確認ののみ表示について、D A,TSU のみ表示は、MVS オペレータコマンドの D A で確認する項目です。TSO/E ユーザ・セッションだけを表示。誰がログオン中か、どのアドレス・スペースを使用しに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文確認ののみ表示の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD A,TSU のみ表示を指定し、OSKB010001の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D A,TSU のみ表示
CASE OSKB010001
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D A,TSU のみ表示
CASE OSKB010001
SOURCE z/OS MVS Operations
D A,TSU のみ表示とOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010001を同じ出力で読み、構文確認ののみ表示の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010001
→ Enter を押す
［画面・出力］
IEE115I OSKB010001 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010001   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D A,TSU のみ表示 と OSKB010001 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0022"><h3>D A,jobname 個別表示</h3><p class="kb-meta">分類: D A ・ 難易度: 中級</p><p>D A,jobname 個別表示は、MVS オペレータコマンドのD Aで確認する項目です。指定したジョブ 1 件のみの現状 (ASID、CPU 時間、現行ステップ、待ち状態) を表示。長時間ジョブの状況確認に多用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換確認の個別表示に関する D A 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換確認の個別表示の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換確認の個別表示の証跡として保存して根拠にする。</li><li>C. D A 命令の変更点を出力本文から切り離して置換確認の個別表示の承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換確認で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では D A 命令 は「D A 命令の状態と出力メッセージを結び付ける置換確認項目」と D A,L または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では D A 命令の出力行と IEE115I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明だけに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では D A 命令をz/OS MVS Operationsの確認記録に残し、対象名は置換確認対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details></section>


<section class="kb-item" id="c22-i0023"><h3>D JOBS 同義コマンド</h3><p class="kb-meta">分類: D A ・ 難易度: 中級</p><p>D JOBS 同義コマンドは、MVS オペレータコマンドのD Aで状態表示や操作を行うためのコマンド関連項目です。D JOBS は D A,JOBS と等価で、バッチジョブのみに絞った表示。D STCLIST / D TSULIST も同様にサブセットを取る</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件確認の同義コマンドに関係する D JOBS 同義コマンドの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、条件確認の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D JOBS 同義コマンドの名称と担当者名だけを残して条件確認の同義コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件確認の同義コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件確認の同義コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では D JOBS 同義コマンド は「D JOBS 同義コマンドの用途を操作コマンドの表示で確認する条件確認項目」と D A,L または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景ではz/OS MVS Operationsの D JOBS 同義コマンドと IEE115I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明だけに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では D JOBS 同義コマンドを MVS オペレータコマンドで扱う確認対象とし、用語名は条件確認用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D JOBS 同義コマンド</strong></p><p>検証目的: 置換確認の同義コマンドについて、D JOBS 同義コマンドは、MVS オペレータコマンドの D A で状態表示や操作を行うためのコマンド関連項目です。D JOBS は D A,JOBS と等価で、バッチジョブに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010004の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換確認の同義コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD JOBS 同義コマンドを指定し、OSKB010004の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D JOBS 同義コマンド
CASE OSKB010004
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D JOBS 同義コマンド
CASE OSKB010004
SOURCE z/OS MVS Operations
D JOBS 同義コマンドとOSKB010004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010004を同じ出力で読み、置換確認の同義コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010004
→ Enter を押す
［画面・出力］
IEE115I OSKB010004 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010004   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D JOBS 同義コマンド と OSKB010004 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D ALLOC


<section class="kb-item" id="c22-i0024"><h3>D ALLOC 目的</h3><p class="kb-meta">分類: D ALLOC ・ 難易度: 初級</p><p>ALLOCxx PARMLIB で設定された動的割り振りオプションの現行値を表示。SYSTEM ・テープ・SMS の許可レベルなどを確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域確認の目的に関する D ALLOC 目的の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域確認の目的の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域確認の目的の証跡として保存して根拠にする。</li><li>C. D ALLOC 目的の変更点を出力本文から切り離して値域確認の目的の承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域確認で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では D ALLOC 目的 は「D ALLOC 目的の状態と出力メッセージを結び付ける値域確認項目」と D A,L または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では D ALLOC 目的の出力行と IEE115I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明だけに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では D ALLOC 目的をz/OS MVS Operationsの確認記録に残し、対象名は値域確認対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ALLOC 目的</strong></p><p>検証目的: 範囲確認の目的について、ALLOCxx PARMLIB で設定された動的割り振りオプションの現行値を表示。SYSTEM ・テープ・ SMS の許可レベルなどを確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010011の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲確認の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ALLOC 目的を指定し、OSKB010011の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ALLOC 目的
CASE OSKB010011
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ALLOC 目的
CASE OSKB010011
SOURCE z/OS MVS Operations
D ALLOC 目的とOSKB010011が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010011を同じ出力で読み、範囲確認の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010011
→ Enter を押す
［画面・出力］
IEE115I OSKB010011 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010011   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010011が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ALLOC 目的 と OSKB010011 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010011 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0025"><h3>D ALLOC,OPTIONS</h3><p class="kb-meta">分類: D ALLOC ・ 難易度: 中級</p><p>D ALLOC,OPTIONSは、SYSTEM / TAPELIB_PREF / VERIFY_UNCAT / TEMPDSFORMAT などインストレーション・オプションを詳細表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告確認の操作コマンドに関係する D ALLOC,OPTIONS の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、警告確認の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D ALLOC,OPTIONS の名称と担当者名だけを残して警告確認の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告確認の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では D ALLOC,OPTIONS は「D ALLOC,OPTIONS の用途を操作コマンドの表示で確認する警告確認項目」と D A,L または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景ではz/OS MVS Operationsの D ALLOC,OPTIONS と IEE115I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明だけに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では D ALLOC,OPTIONS を MVS オペレータコマンドで扱う確認対象とし、用語名は警告確認用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ALLOC,OPTIONS</strong></p><p>検証目的: 優先確認の操作コマンドについて、D ALLOC,OPTIONS は、SYSTEM / TAPELIB_PREF / VERIFY_UNCAT / TEMPDSFORMAT などインストレーション・オプションに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010012の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ALLOC,OPTIONSを指定し、OSKB010012の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ALLOC,OPTIONS
CASE OSKB010012
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ALLOC,OPTIONS
CASE OSKB010012
SOURCE z/OS MVS Operations
D ALLOC,OPTIONSとOSKB010012が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010012を同じ出力で読み、優先確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010012
→ Enter を押す
［画面・出力］
IEE115I OSKB010012 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010012   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010012が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ALLOC,OPTIONS と OSKB010012 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010012 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0026"><h3>D ALLOC,POLICY</h3><p class="kb-meta">分類: D ALLOC ・ 難易度: 上級</p><p>D ALLOC,POLICYは、ALLOCxx の POLICY 句で定義した動的割り振り失敗時の自動再試行・代替候補ポリシーを表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧確認の操作コマンドで D ALLOC,POLICY の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D ALLOC,POLICY の出力を取らず復旧確認の操作コマンドの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて復旧確認の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧確認の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では D ALLOC,POLICY は「復旧確認の操作コマンドに関係する定義値と表示行を照合する復旧確認項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では D ALLOC,POLICY の属性行と IEE115I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明だけに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では D ALLOC,POLICY を MVS オペレータコマンドの運用手順で確認し、初出名は復旧確認初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ALLOC,POLICY</strong></p><p>検証目的: 記録確認の操作コマンドについて、D ALLOC,POLICY は、ALLOCxx の POLICY 句で定義した動的割り振り失敗時の自動再試行・代替候補ポリシーを表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010013の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ALLOC,POLICYを指定し、OSKB010013の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ALLOC,POLICY
CASE OSKB010013
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ALLOC,POLICY
CASE OSKB010013
SOURCE z/OS MVS Operations
D ALLOC,POLICYとOSKB010013が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010013を同じ出力で読み、記録確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010013
→ Enter を押す
［画面・出力］
IEE115I OSKB010013 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010013   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010013が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ALLOC,POLICY と OSKB010013 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010013 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D APPC


<section class="kb-item" id="c22-i0027"><h3>D APPC,LU</h3><p class="kb-meta">分類: D APPC ・ 難易度: 中級</p><p>D APPC,LUは、APPC/MVS 上で定義された LU (論理ユニット) の一覧と状態 (ACTIVE/INACTIVE/PENDING) を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査確認の操作コマンドで操作コマンドの運用確認を行います。D APPC,LU の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査確認の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査確認の操作コマンドを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を監査確認で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D APPC,LU の属性行を読まず監査確認の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では D APPC,LU は「z/OS MVS Operationsで D APPC,LU の扱いを記録する監査確認項目」と D A,L または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では D APPC,LU の表示結果と IEE115I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明だけに寄り、判定名は監査確認不足です。監査確認資料では D APPC,LU の使い方を出典欄から追跡し、資料名は監査確認資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文確認の操作コマンドに関係する D APPC,LU の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D APPC,LU の名称と担当者名のみを残して構文確認の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文確認の操作コマンドにおいて選択記号 A を採用し、識別名は構文確認です。構文確認の操作コマンドにおいて D APPC,LU は説明欄の「D APPC,LU の用途を操作コマンドの表示で確認する構文確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認の操作コマンドに関連して、z/OS MVS Operationsでは D APPC,LU の表示属性と IEE115I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認の操作コマンドは別カテゴリの確認を流用しており、D APPC,LU の根拠にならないため構文確認ではありません。 D: 構文確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文確認ではありません。構文確認の操作コマンドで使う D APPC,LU という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D APPC,LU</strong></p><p>検証目的: 置換確認の操作コマンドについて、D APPC,LU は、APPC/MVS 上で定義された LU (論理ユニット) の一覧と状態 (ACTIVE/INACTIVE/PENDING) を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040004の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD APPC,LUを指定し、OSKB040004の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D APPC,LU
CASE OSKB040004
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D APPC,LU
CASE OSKB040004
SOURCE z/OS MVS Operations
D APPC,LUとOSKB040004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040004を同じ出力で読み、置換確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040004
→ Enter を押す
［画面・出力］
IEE115I OSKB040004 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040004   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D APPC,LU と OSKB040004 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D APPC,LU</strong></p><p>検証目的: 比較確認の操作コマンドについて、D APPC,LU は、APPC/MVS 上で定義された LU (論理ユニット) の一覧と状態 (ACTIVE/INACTIVE/PENDING) を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010014の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD APPC,LUを指定し、OSKB010014の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D APPC,LU
CASE OSKB010014
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D APPC,LU
CASE OSKB010014
SOURCE z/OS MVS Operations
D APPC,LUとOSKB010014が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010014を同じ出力で読み、比較確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010014
→ Enter を押す
［画面・出力］
IEE115I OSKB010014 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010014   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010014が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D APPC,LU と OSKB010014 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010014 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0028"><h3>D APPC,TP</h3><p class="kb-meta">分類: D APPC ・ 難易度: 中級</p><p>D APPC,TPは、MVS オペレータコマンドのD APPCで確認する項目です。APPC トランザクション・プログラム (TP) プロファイル定義の一覧を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更確認の操作コマンドに関する D APPC,TP の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更確認の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. D APPC,TP の変更点を出力本文から切り離して変更確認の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、変更確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では D APPC,TP は「D APPC,TP の状態と出力メッセージを結び付ける変更確認項目」と D A,L または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では D APPC,TP の出力行と IEE115I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明だけに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では D APPC,TP をz/OS MVS Operationsの確認記録に残し、対象名は変更確認対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開確認の操作コマンドで D APPC,TP の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D APPC,TP の出力を取らず展開確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開確認の操作コマンドにおいて選択記号 B を採用し、識別名は展開確認です。展開確認の操作コマンドにおいて D APPC,TP は説明欄の「展開確認の操作コマンドに関係する定義値と表示行を照合する展開確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認の操作コマンドの証跡を読む担当者は、D APPC,TP の属性行と IEE115I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開確認ではありません。 D: 展開確認の操作コマンドは別カテゴリの確認を流用しており、D APPC,TP の根拠にならないため展開確認ではありません。展開確認の操作コマンドに出る D APPC,TP は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D APPC,TP</strong></p><p>検証目的: 順序確認の操作コマンドについて、D APPC,TP は、MVS オペレータコマンドの D APPC で確認する項目です。APPC トランザクション・プログラム (TP) プロファイル定義の一覧を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010015の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD APPC,TPを指定し、OSKB010015の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D APPC,TP
CASE OSKB010015
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D APPC,TP
CASE OSKB010015
SOURCE z/OS MVS Operations
D APPC,TPとOSKB010015が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010015を同じ出力で読み、順序確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010015
→ Enter を押す
［画面・出力］
IEE115I OSKB010015 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010015   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010015が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D APPC,TP と OSKB010015 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010015 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D ASCH


<section class="kb-item" id="c22-i0029"><h3>D ASCH,ALL</h3><p class="kb-meta">分類: D ASCH ・ 難易度: 中級</p><p>D ASCH,ALLは、ASCH (APPC スケジューラ) のクラス定義、稼動中の TP、待ちキューの状態を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文照合の操作コマンドに関係する D ASCH,ALL の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、構文照合の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D ASCH,ALL の名称と担当者名だけを残して構文照合の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文照合の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では D ASCH,ALL は「D ASCH,ALL の用途を操作コマンドの表示で確認する構文照合項目」と D A,L または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景ではz/OS MVS Operationsの D ASCH,ALL と IEE115I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明だけに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では D ASCH,ALL を MVS オペレータコマンドで扱う確認対象とし、用語名は構文照合用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出確認の操作コマンドで操作コマンドの運用確認を行います。D ASCH,ALL の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出確認の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出確認の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D ASCH,ALL の属性行を読まず呼出確認の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出確認の操作コマンドにおいて選択記号 C を採用し、識別名は呼出確認です。呼出確認の操作コマンドにおいて D ASCH,ALL は説明欄の「z/OS MVS Operationsで D ASCH,ALL の扱いを記録する呼出確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認の操作コマンドを受け取る担当者は、D ASCH,ALL の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認の操作コマンドは別カテゴリの確認を流用しており、D ASCH,ALL の根拠にならないため呼出確認ではありません。 B: 呼出確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認の操作コマンドが示す D ASCH,ALL は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ASCH,ALL</strong></p><p>検証目的: 値域確認の操作コマンドについて、D ASCH,ALL は、ASCH (APPC スケジューラ) のクラス定義、稼動中の TP、待ちキューの状態を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ASCH,ALLを指定し、OSKB010016の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ASCH,ALL
CASE OSKB010016
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ASCH,ALL
CASE OSKB010016
SOURCE z/OS MVS Operations
D ASCH,ALLとOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010016を同じ出力で読み、値域確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010016
→ Enter を押す
［画面・出力］
IEE115I OSKB010016 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010016   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ASCH,ALL と OSKB010016 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0030"><h3>D ASCH,CLASSES</h3><p class="kb-meta">分類: D ASCH ・ 難易度: 中級</p><p>D ASCH,CLASSESは、ASCH スケジューラに定義されたクラス (MIN/MAX イニシエータ数等) のみを一覧表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開照合の操作コマンドで D ASCH,CLASSES の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D ASCH,CLASSES の出力を取らず展開照合の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて展開照合の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開照合の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開照合正解では選択記号 B を採用し、正解名は展開照合正解です。展開照合根拠では D ASCH,CLASSES は「展開照合の操作コマンドに関係する定義値と表示行を照合する展開照合項目」と D A,L または該当パネルの出力を照合し、根拠名は展開照合根拠です。展開照合追跡では D ASCH,CLASSES の属性行と IEE115I を合わせ、追跡名は展開照合追跡です。誤答側の問題点を分けます。 A: 展開照合不足は名称や説明だけに寄り、判定名は展開照合不足です。 B: 展開照合正答は対象出力と項目説明を結び、根拠名は展開照合正答です。 C: 展開照合欠落は戻り値や記録番号に寄り、欠落名は展開照合欠落です。 D: 展開照合流用は別カテゴリの確認であり、排除名は展開照合流用です。展開照合初出では D ASCH,CLASSES を MVS オペレータコマンドの運用手順で確認し、初出名は展開照合初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換確認の操作コマンドに関する D ASCH,CLASSES の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換確認の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. D ASCH,CLASSES の変更点を出力本文から切り離して置換確認の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換確認の操作コマンドにおいて選択記号 D を採用し、識別名は置換確認です。置換確認の操作コマンドにおいて D ASCH,CLASSES は説明欄の「D ASCH,CLASSES の状態と出力メッセージを結び付ける置換確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認の操作コマンドに関する記録は、D ASCH,CLASSES の出力行と IEE115I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換確認ではありません。 B: 置換確認の操作コマンドは別カテゴリの確認を流用しており、D ASCH,CLASSES の根拠にならないため置換確認ではありません。 C: 置換確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認の操作コマンドで記録する D ASCH,CLASSES はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ASCH,CLASSES</strong></p><p>検証目的: 警告確認の操作コマンドについて、D ASCH,CLASSES は、ASCH スケジューラに定義されたクラス (MIN/MAX イニシエータ数等) のみを一覧表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ASCH,CLASSESを指定し、OSKB010017の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ASCH,CLASSES
CASE OSKB010017
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ASCH,CLASSES
CASE OSKB010017
SOURCE z/OS MVS Operations
D ASCH,CLASSESとOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010017を同じ出力で読み、警告確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010017
→ Enter を押す
［画面・出力］
IEE115I OSKB010017 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010017   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ASCH,CLASSES と OSKB010017 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D ASM


<section class="kb-item" id="c22-i0031"><h3>D ASM 全データセット表示</h3><p class="kb-meta">分類: D ASM ・ 難易度: 中級</p><p>D ASM 全データセット表示は、PLPA / COMMON / LOCAL の各ページ・データセットの DSN、使用率 (%)、状態 (FULL / OK / NOT FULL) を一覧で示す</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲確認の全データセット表示で操作コマンドの運用確認を行います。D ASM 全データセット表示の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲確認の全データセット表示を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲確認の全データセット表示を正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、範囲確認の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D ASM 全データセット表示の属性行を読まず範囲確認の全データセット表示の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では D ASM 全データセット表示 は「z/OS MVS Operationsで D ASM 全データセット表示の扱いを記録する範囲確認項目」と D A,L または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では D ASM 全データセット表示の表示結果と IEE115I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明だけに寄り、判定名は範囲確認不足です。範囲確認資料では D ASM 全データセット表示の使い方を出典欄から追跡し、資料名は範囲確認資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ASM 全データセット表示</strong></p><p>検証目的: 探索確認の全データセット表示について、D ASM 全データセット表示は、PLPA / COMMON / LOCAL の各ページ・データセットの DSN、使用率 (%)、状態 (FULL / OK / NOT Fに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010006の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、探索確認の全データセット表示の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ASM 全データセット表示を指定し、OSKB010006の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ASM 全データセット表示
CASE OSKB010006
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ASM 全データセット表示
CASE OSKB010006
SOURCE z/OS MVS Operations
D ASM 全データセット表示とOSKB010006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010006を同じ出力で読み、探索確認の全データセット表示の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010006
→ Enter を押す
［画面・出力］
IEE115I OSKB010006 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010006   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ASM 全データセット表示 と OSKB010006 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0032"><h3>D ASM 目的</h3><p class="kb-meta">分類: D ASM ・ 難易度: 初級</p><p>D ASM 目的は、MVS オペレータコマンドのD ASMで確認する項目です。ページ・データセットおよびスワップ・データセットの使用状況を表示。実メモリと補助記憶の関係を可視化する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切確認の目的で D ASM 目的の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D ASM 目的の出力を取らず区切確認の目的の説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて区切確認の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切確認の目的の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切確認の目的へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では D ASM 目的 は「区切確認の目的に関係する定義値と表示行を照合する区切確認項目」と D A,L または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では D ASM 目的の属性行と IEE115I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明だけに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では D ASM 目的を MVS オペレータコマンドの運用手順で確認し、初出名は区切確認初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ASM 目的</strong></p><p>検証目的: 終端確認の目的について、D ASM 目的は、MVS オペレータコマンドの D ASM で確認する項目です。ページ・データセットおよびスワップ・データセットの使用状況を表示。実メモリと補助記憶の関係を可に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010005の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端確認の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ASM 目的を指定し、OSKB010005の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ASM 目的
CASE OSKB010005
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ASM 目的
CASE OSKB010005
SOURCE z/OS MVS Operations
D ASM 目的とOSKB010005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010005を同じ出力で読み、終端確認の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010005
→ Enter を押す
［画面・出力］
IEE115I OSKB010005 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010005   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ASM 目的 と OSKB010005 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0033"><h3>D ASM,COMMON</h3><p class="kb-meta">分類: D ASM ・ 難易度: 中級</p><p>D ASM,COMMONは、COMMON ページ・データセット (CSA/SQA のページアウト先) の状態を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録確認の操作コマンドに関係する D ASM,COMMON の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、記録確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D ASM,COMMON の名称と担当者名だけを残して記録確認の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録確認の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では D ASM,COMMON は「D ASM,COMMON の用途を操作コマンドの表示で確認する記録確認項目」と D A,L または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景ではz/OS MVS Operationsの D ASM,COMMON と IEE115I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明だけに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では D ASM,COMMON を MVS オペレータコマンドで扱う確認対象とし、用語名は記録確認用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ASM,COMMON</strong></p><p>検証目的: 呼出確認の操作コマンドについて、D ASM,COMMON は、COMMON ページ・データセット (CSA/SQA のページアウト先) の状態を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040003の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ASM,COMMONを指定し、OSKB040003の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ASM,COMMON
CASE OSKB040003
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ASM,COMMON
CASE OSKB040003
SOURCE z/OS MVS Operations
D ASM,COMMONとOSKB040003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040003を同じ出力で読み、呼出確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040003
→ Enter を押す
［画面・出力］
IEE115I OSKB040003 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040003   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ASM,COMMON と OSKB040003 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D ASM,COMMON</strong></p><p>検証目的: 出力確認の操作コマンドについて、D ASM,COMMON は、COMMON ページ・データセット (CSA/SQA のページアウト先) の状態を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ASM,COMMONを指定し、OSKB010008の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ASM,COMMON
CASE OSKB010008
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ASM,COMMON
CASE OSKB010008
SOURCE z/OS MVS Operations
D ASM,COMMONとOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010008を同じ出力で読み、出力確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010008
→ Enter を押す
［画面・出力］
IEE115I OSKB010008 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010008   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ASM,COMMON と OSKB010008 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0034"><h3>D ASM,LOCAL</h3><p class="kb-meta">分類: D ASM ・ 難易度: 中級</p><p>D ASM,LOCALは、MVS オペレータコマンドのD ASMで確認する項目です。ローカル (プライベート) ページ・データセットの使用率を表示。LOCAL の枯渇は新規ジョブ起動失敗の前兆となる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較確認の操作コマンドで D ASM,LOCAL の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D ASM,LOCAL の出力を取らず比較確認の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較確認の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では D ASM,LOCAL は「比較確認の操作コマンドに関係する定義値と表示行を照合する比較確認項目」と D A,L または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では D ASM,LOCAL の属性行と IEE115I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明だけに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では D ASM,LOCAL を MVS オペレータコマンドの運用手順で確認し、初出名は比較確認初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ASM,LOCAL</strong></p><p>検証目的: 条件確認の操作コマンドについて、D ASM,LOCAL は、MVS オペレータコマンドの D ASM で確認する項目です。ローカル (プライベート) ページ・データセットの使用率を表示。LOCAL の枯渇は新規に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ASM,LOCALを指定し、OSKB010009の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ASM,LOCAL
CASE OSKB010009
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ASM,LOCAL
CASE OSKB010009
SOURCE z/OS MVS Operations
D ASM,LOCALとOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010009を同じ出力で読み、条件確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010009
→ Enter を押す
［画面・出力］
IEE115I OSKB010009 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010009   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ASM,LOCAL と OSKB010009 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0035"><h3>D ASM,PLPA</h3><p class="kb-meta">分類: D ASM ・ 難易度: 中級</p><p>D ASM,PLPAは、MVS オペレータコマンドのD ASMで確認する項目です。PLPA ページ・データセットの状態のみを表示。IPL CLPA 時の新規 PLPA 設定確認に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先確認の操作コマンドに関する D ASM,PLPA の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先確認の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. D ASM,PLPA の変更点を出力本文から切り離して優先確認の操作コマンドの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、優先確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では D ASM,PLPA は「D ASM,PLPA の状態と出力メッセージを結び付ける優先確認項目」と D A,L または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では D ASM,PLPA の出力行と IEE115I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明だけに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では D ASM,PLPA をz/OS MVS Operationsの確認記録に残し、対象名は優先確認対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ASM,PLPA</strong></p><p>検証目的: 上書確認の操作コマンドについて、D ASM,PLPA は、MVS オペレータコマンドの D ASM で確認する項目です。PLPA ページ・データセットの状態のみを表示。IPL CLPA 時の新規 PLPA 設定に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010007の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ASM,PLPAを指定し、OSKB010007の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ASM,PLPA
CASE OSKB010007
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ASM,PLPA
CASE OSKB010007
SOURCE z/OS MVS Operations
D ASM,PLPAとOSKB010007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010007を同じ出力で読み、上書確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010007
→ Enter を押す
［画面・出力］
IEE115I OSKB010007 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010007   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ASM,PLPA と OSKB010007 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0036"><h3>D ASM,SCM</h3><p class="kb-meta">分類: D ASM ・ 難易度: 中級</p><p>D ASM,SCMは、Storage Class Memory (フラッシュ) を補助記憶として使用している場合の使用状況を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序確認の操作コマンドで操作コマンドの運用確認を行います。D ASM,SCM の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序確認の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序確認の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、順序確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D ASM,SCM の属性行を読まず順序確認の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では D ASM,SCM は「z/OS MVS Operationsで D ASM,SCM の扱いを記録する順序確認項目」と D A,L または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では D ASM,SCM の表示結果と IEE115I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明だけに寄り、判定名は順序確認不足です。順序確認資料では D ASM,SCM の使い方を出典欄から追跡し、資料名は順序確認資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ASM,SCM</strong></p><p>検証目的: 区切確認の操作コマンドについて、D ASM,SCM は、Storage Class Memory (フラッシュ) を補助記憶として使用している場合の使用状況を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010010の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ASM,SCMを指定し、OSKB010010の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ASM,SCM
CASE OSKB010010
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ASM,SCM
CASE OSKB010010
SOURCE z/OS MVS Operations
D ASM,SCMとOSKB010010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010010を同じ出力で読み、区切確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010010
→ Enter を押す
［画面・出力］
IEE115I OSKB010010 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010010   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ASM,SCM と OSKB010010 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D C


<section class="kb-item" id="c22-i0037"><h3>D C,HC コピー一覧</h3><p class="kb-meta">分類: D C ・ 難易度: 中級</p><p>D C,HC コピー一覧は、MVS オペレータコマンドのD Cで確認する項目です。現在ハードコピー出力対象になっているコンソール / 出力先 (SYSLOG / OPERLOG) を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換照合のコピー一覧に関する D C,HC コピー一覧の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換照合のコピー一覧の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換照合のコピー一覧の証跡として保存して根拠にする。</li><li>C. D C,HC コピー一覧の変更点を出力本文から切り離して置換照合のコピー一覧の承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、置換照合の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では D C,HC コピー一覧 は「D C,HC コピー一覧の状態と出力メッセージを結び付ける置換照合項目」と D A,L または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では D C,HC コピー一覧の出力行と IEE115I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明だけに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では D C,HC コピー一覧をz/OS MVS Operationsの確認記録に残し、対象名は置換照合対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索確認のコピー一覧で D C,HC コピー一覧の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D C,HC コピー一覧の出力を取らず探索確認のコピー一覧の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索確認のコピー一覧の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索確認のコピー一覧へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索確認のコピー一覧において選択記号 B を採用し、識別名は探索確認です。探索確認のコピー一覧において D C,HC コピー一覧 は説明欄の「探索確認のコピー一覧に関係する定義値と表示行を照合する探索確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認のコピー一覧の証跡を読む担当者は、D C,HC コピー一覧の属性行と IEE115I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認のコピー一覧は名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認のコピー一覧は対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認のコピー一覧は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索確認ではありません。 D: 探索確認のコピー一覧は別カテゴリの確認を流用しており、D C,HC コピー一覧の根拠にならないため探索確認ではありません。探索確認のコピー一覧に出る D C,HC コピー一覧は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D C,HC コピー一覧</strong></p><p>検証目的: 監査確認のコピー一覧について、D C,HC コピー一覧は、MVS オペレータコマンドの D C で確認する項目です。現在ハードコピー出力対象になっているコンソール / 出力先 (SYSLOG / OPERLに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010019の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査確認のコピー一覧の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD C,HC コピー一覧を指定し、OSKB010019の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D C,HC コピー一覧
CASE OSKB010019
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D C,HC コピー一覧
CASE OSKB010019
SOURCE z/OS MVS Operations
D C,HC コピー一覧とOSKB010019が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010019を同じ出力で読み、監査確認のコピー一覧の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010019
→ Enter を押す
［画面・出力］
IEE115I OSKB010019 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010019   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010019が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D C,HC コピー一覧 と OSKB010019 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010019 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0038"><h3>D C,K 目的</h3><p class="kb-meta">分類: D C ・ 難易度: 初級</p><p>D C,K 目的は、MVS オペレータコマンドのD Cで確認する項目です。現在のコンソール K (制御) セッション設定 (出力面、ロール状態、PFK セットなど) を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出照合の目的で操作コマンドの運用確認を行います。D C,K 目的の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出照合の目的を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出照合の目的を正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、呼出照合の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D C,K 目的の属性行を読まず呼出照合の目的の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では D C,K 目的 は「z/OS MVS Operationsで D C,K 目的の扱いを記録する呼出照合項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では D C,K 目的の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明だけに寄り、判定名は呼出照合不足です。呼出照合資料では D C,K 目的の使い方を出典欄から追跡し、資料名は呼出照合資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端確認の目的に関係する D C,K 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D C,K 目的の名称と担当者名のみを残して終端確認の目的の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端確認の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端確認の目的の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 終端確認の目的において選択記号 A を採用し、識別名は終端確認です。終端確認の目的において D C,K 目的 は説明欄の「D C,K 目的の用途を操作コマンドの表示で確認する終端確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認の目的に関連して、z/OS MVS Operationsでは D C,K 目的の表示属性と IEE115I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認の目的は対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認の目的は別カテゴリの確認を流用しており、D C,K 目的の根拠にならないため終端確認ではありません。 D: 終端確認の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端確認ではありません。終端確認の目的で使う D C,K 目的という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D C,K 目的</strong></p><p>検証目的: 復旧確認の目的について、D C,K 目的は、MVS オペレータコマンドの D C で確認する項目です。現在のコンソール K (制御) セッション設定 (出力面、ロール状態、PFK セットなど) を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010018の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧確認の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD C,K 目的を指定し、OSKB010018の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D C,K 目的
CASE OSKB010018
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D C,K 目的
CASE OSKB010018
SOURCE z/OS MVS Operations
D C,K 目的とOSKB010018が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010018を同じ出力で読み、復旧確認の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010018
→ Enter を押す
［画面・出力］
IEE115I OSKB010018 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010018   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010018が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D C,K 目的 と OSKB010018 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010018 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D CN


<section class="kb-item" id="c22-i0039"><h3>D CN 目的</h3><p class="kb-meta">分類: D CN ・ 難易度: 初級</p><p>D CN 目的は、MCS / SMCS / EMCS で定義された全コンソールの一覧と現状 (ACTIVE / INACTIVE / DEFINED) を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端照合の目的に関係する D CN 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、終端照合として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D CN 目的の名称と担当者名だけを残して終端照合の目的の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端照合の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端照合の目的の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では D CN 目的 は「D CN 目的の用途を操作コマンドの表示で確認する終端照合項目」と D A,L または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景ではz/OS MVS Operationsの D CN 目的と IEE115I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明だけに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では D CN 目的を MVS オペレータコマンドで扱う確認対象とし、用語名は終端照合用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書確認の目的で操作コマンドの運用確認を行います。D CN 目的の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書確認の目的を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書確認の目的を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D CN 目的の属性行を読まず上書確認の目的の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 上書確認の目的において選択記号 C を採用し、識別名は上書確認です。上書確認の目的において D CN 目的 は説明欄の「z/OS MVS Operationsで D CN 目的の扱いを記録する上書確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認の目的を受け取る担当者は、D CN 目的の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認の目的は別カテゴリの確認を流用しており、D CN 目的の根拠にならないため上書確認ではありません。 B: 上書確認の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書確認ではありません。 C: 上書確認の目的は対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認の目的が示す D CN 目的は出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D CN 目的</strong></p><p>検証目的: 終端確認の目的について、D CN 目的は、MCS / SMCS / EMCS で定義された全コンソールの一覧と現状 (ACTIVE / INACTIVE / DEFINED) を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040005の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端確認の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD CN 目的を指定し、OSKB040005の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D CN 目的
CASE OSKB040005
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D CN 目的
CASE OSKB040005
SOURCE z/OS MVS Operations
D CN 目的とOSKB040005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040005を同じ出力で読み、終端確認の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040005
→ Enter を押す
［画面・出力］
IEE115I OSKB040005 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040005   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D CN 目的 と OSKB040005 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D CN 目的</strong></p><p>検証目的: 変更確認の目的について、D CN 目的は、MCS / SMCS / EMCS で定義された全コンソールの一覧と現状 (ACTIVE / INACTIVE / DEFINED) を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更確認の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD CN 目的を指定し、OSKB010020の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D CN 目的
CASE OSKB010020
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D CN 目的
CASE OSKB010020
SOURCE z/OS MVS Operations
D CN 目的とOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010020を同じ出力で読み、変更確認の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010020
→ Enter を押す
［画面・出力］
IEE115I OSKB010020 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010020   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D CN 目的 と OSKB010020 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0040"><h3>D CN,N=name 個別表示</h3><p class="kb-meta">分類: D CN ・ 難易度: 中級</p><p>D CN,N=name 個別表示は、指定したコンソール名の権限 (AUTH=)、ルート・コード、メッセージ・レベル、起動システム等を詳細表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索照合の個別表示で D CN 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D CN 命令の出力を取らず探索照合の個別表示の説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索照合の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索照合の個別表示の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索照合の個別表示へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では D CN 命令 は「探索照合の個別表示に関係する定義値と表示行を照合する探索照合項目」と D A,L または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では D CN 命令の属性行と IEE115I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明だけに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では D CN 命令を MVS オペレータコマンドの運用手順で確認し、初出名は探索照合初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力確認の個別表示に関する D CN,N=name 個別表示の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力確認の個別表示の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力確認の個別表示の証跡として保存して根拠にする。</li><li>C. D CN,N=name 個別表示の変更点を出力本文から切り離して出力確認の個別表示の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力確認の個別表示において選択記号 D を採用し、識別名は出力確認です。出力確認の個別表示において D CN,N=name 個別表示 は説明欄の「D CN,N=name 個別表示の状態と出力メッセージを結び付ける出力確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認の個別表示に関する記録は、D CN,N=name 個別表示の出力行と IEE115I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認の個別表示は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力確認ではありません。 B: 出力確認の個別表示は別カテゴリの確認を流用しており、D CN,N=name 個別表示の根拠にならないため出力確認ではありません。 C: 出力確認の個別表示は名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認の個別表示は対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認の個別表示で記録する D CN,N=name 個別表示はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D CN,N=name 個別表示</strong></p><p>検証目的: 構文照合の個別表示について、D CN,N=name 個別表示は、指定したコンソール名の権限 (AUTH=)、ルート・コード、メッセージ・レベル、起動システム等を詳細表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010021の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文照合の個別表示の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD CN,N=name 個別表示を指定し、OSKB010021の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D CN,N=name 個別表示
CASE OSKB010021
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D CN,N=name 個別表示
CASE OSKB010021
SOURCE z/OS MVS Operations
D CN,N=name 個別表示とOSKB010021が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010021を同じ出力で読み、構文照合の個別表示の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010021
→ Enter を押す
［画面・出力］
IEE115I OSKB010021 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010021   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010021が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D CN,N=name 個別表示 と OSKB010021 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010021 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D CONSOLES


<section class="kb-item" id="c22-i0041"><h3>D CONSOLES,A 起動済みのみ</h3><p class="kb-meta">分類: D CONSOLES ・ 難易度: 中級</p><p>D CONSOLES,A 起動済みのみは、MVS オペレータコマンドのD CONSOLESで確認する項目です。ACTIVE 状態のコンソールに絞って表示。実際にメッセージを受け取っている端末・プロセスを把握する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力照合の起動済みのみに関する D CONSOLES 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力照合の起動済みのみの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力照合の起動済みのみの証跡として保存して根拠にする。</li><li>C. D CONSOLES 命令の変更点を出力本文から切り離して出力照合の起動済みのみの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力照合で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力照合正解では選択記号 D を採用し、正解名は出力照合正解です。出力照合根拠では D CONSOLES 命令 は「D CONSOLES 命令の状態と出力メッセージを結び付ける出力照合項目」と D A,L または該当パネルの出力を照合し、根拠名は出力照合根拠です。出力照合保存では D CONSOLES 命令の出力行と IEE115I を一緒に残し、保存名は出力照合保存です。選択肢ごとの違いを示します。 A: 出力照合欠落は戻り値や記録番号に寄り、欠落名は出力照合欠落です。 B: 出力照合流用は別カテゴリの確認であり、排除名は出力照合流用です。 C: 出力照合不足は名称や説明だけに寄り、判定名は出力照合不足です。 D: 出力照合正答は対象出力と項目説明を結び、根拠名は出力照合正答です。出力照合対象では D CONSOLES 命令をz/OS MVS Operationsの確認記録に残し、対象名は出力照合対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切確認の起動済みのみで D CONSOLES,A 起動済みのみの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D CONSOLES,A 起動済みのみの出力を取らず区切確認の起動済みのみの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切確認の起動済みのみの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切確認の起動済みのみへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切確認の起動済みのみにおいて選択記号 B を採用し、識別名は区切確認です。区切確認の起動済みのみにおいて D CONSOLES,A 起動済みのみ は説明欄の「区切確認の起動済みのみに関係する定義値と表示行を照合する区切確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認の起動済みのみの証跡を読む担当者は、D CONSOLES,A 起動済みのみの属性行と IEE115I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認の起動済みのみは名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認の起動済みのみは対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認の起動済みのみは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切確認ではありません。 D: 区切確認の起動済みのみは別カテゴリの確認を流用しており、D CONSOLES,A 起動済みのみの根拠にならないため区切確認ではありません。区切確認の起動済みのみに出る D CONSOLES,A 起動済みのみは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D CONSOLES,A 起動済みのみ</strong></p><p>検証目的: 呼出照合の起動済みのみについて、D CONSOLES,A 起動済みのみは、MVS オペレータコマンドの D CONSOLES で確認する項目です。ACTIVE 状態のコンソールに絞って表示。実際にメッセージをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010023の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出照合の起動済みのみの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD CONSOLES,A 起動済みのを指定し、OSKB010023の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D CONSOLES,A 起動済みの
CASE OSKB010023
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D CONSOLES,A 起動済みの
CASE OSKB010023
SOURCE z/OS MVS Operations
D CONSOLES,A 起動済みのとOSKB010023が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010023を同じ出力で読み、呼出照合の起動済みのみの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010023
→ Enter を押す
［画面・出力］
IEE115I OSKB010023 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010023   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010023が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D CONSOLES,A 起動済みの と OSKB010023 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010023 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0042"><h3>D CONSOLES,L</h3><p class="kb-meta">分類: D CONSOLES ・ 難易度: 中級</p><p>D CONSOLES,Lは、MVS オペレータコマンドのD CONSOLESで確認する項目です。全コンソールの長形式一覧。MCS マスタ・コンソール、サブシステム・コンソール、SMCS 端末、EMCS API 利用者を一括把握</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書照合の操作コマンドで操作コマンドの運用確認を行います。D CONSOLES,L の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書照合の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書照合の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、上書照合の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D CONSOLES,L の属性行を読まず上書照合の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では D CONSOLES,L は「z/OS MVS Operationsで D CONSOLES,L の扱いを記録する上書照合項目」と D A,L または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では D CONSOLES,L の表示結果と IEE115I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明だけに寄り、判定名は上書照合不足です。上書照合資料では D CONSOLES,L の使い方を出典欄から追跡し、資料名は上書照合資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件確認の操作コマンドに関係する D CONSOLES,L の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D CONSOLES,L の名称と担当者名のみを残して条件確認の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件確認の操作コマンドにおいて選択記号 A を採用し、識別名は条件確認です。条件確認の操作コマンドにおいて D CONSOLES,L は説明欄の「D CONSOLES,L の用途を操作コマンドの表示で確認する条件確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認の操作コマンドに関連して、z/OS MVS Operationsでは D CONSOLES,L の表示属性と IEE115I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認の操作コマンドは別カテゴリの確認を流用しており、D CONSOLES,L の根拠にならないため条件確認ではありません。 D: 条件確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件確認ではありません。条件確認の操作コマンドで使う D CONSOLES,L という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D CONSOLES,L</strong></p><p>検証目的: 展開照合の操作コマンドについて、D CONSOLES,L は、MVS オペレータコマンドの D CONSOLES で確認する項目です。全コンソールの長形式一覧。MCS マスタ・コンソール、サブシステム・コンソーに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010022の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD CONSOLES,Lを指定し、OSKB010022の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D CONSOLES,L
CASE OSKB010022
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D CONSOLES,L
CASE OSKB010022
SOURCE z/OS MVS Operations
D CONSOLES,LとOSKB010022が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010022を同じ出力で読み、展開照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010022
→ Enter を押す
［画面・出力］
IEE115I OSKB010022 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010022   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010022が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D CONSOLES,L と OSKB010022 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0043"><h3>D CONSOLES,MASTER</h3><p class="kb-meta">分類: D CONSOLES ・ 難易度: 中級</p><p>D CONSOLES,MASTERは、MVS オペレータコマンドのD CONSOLESで確認する項目です。現行のマスタ・コンソールおよびマスタ権限を持つコンソールを表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件照合の操作コマンドに関係する D CONSOLES 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、条件照合の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D CONSOLES 命令の名称と担当者名だけを残して条件照合の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件照合の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では D CONSOLES 命令 は「D CONSOLES 命令の用途を操作コマンドの表示で確認する条件照合項目」と D A,L または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景ではz/OS MVS Operationsの D CONSOLES 命令と IEE115I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明だけに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では D CONSOLES 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は条件照合用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 範囲確認の操作コマンドで操作コマンドの運用確認を行います。D CONSOLES,MASTER の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲確認の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲確認の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D CONSOLES,MASTER の属性行を読まず範囲確認の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲確認の操作コマンドにおいて選択記号 C を採用し、識別名は範囲確認です。範囲確認の操作コマンドにおいて D CONSOLES,MASTER は説明欄の「z/OS MVS Operationsで D CONSOLES,MASTER の扱いを記録する範囲確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲確認です。範囲確認の操作コマンドを受け取る担当者は、D CONSOLES,MASTER の表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲確認です。不適切な選択肢を整理します。 A: 範囲確認の操作コマンドは別カテゴリの確認を流用しており、D CONSOLES,MASTER の根拠にならないため範囲確認ではありません。 B: 範囲確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲確認ではありません。 C: 範囲確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので範囲確認です。 D: 範囲確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲確認ではありません。範囲確認の操作コマンドが示す D CONSOLES,MASTER は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D CONSOLES,MASTER</strong></p><p>検証目的: 置換照合の操作コマンドについて、D CONSOLES,MASTER は、MVS オペレータコマンドの D CONSOLES で確認する項目です。現行のマスタ・コンソールおよびマスタ権限を持つコンソールを表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010024の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD CONSOLES,MASTERを指定し、OSKB010024の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D CONSOLES,MASTER
CASE OSKB010024
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D CONSOLES,MASTER
CASE OSKB010024
SOURCE z/OS MVS Operations
D CONSOLES,MASTERとOSKB010024が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010024を同じ出力で読み、置換照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010024
→ Enter を押す
［画面・出力］
IEE115I OSKB010024 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010024   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010024が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D CONSOLES,MASTER と OSKB010024 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D DLS


<section class="kb-item" id="c22-i0044"><h3>D DLS 目的</h3><p class="kb-meta">分類: D DLS ・ 難易度: 初級</p><p>D DLS 目的は、MVS オペレータコマンドのD DLSで確認する項目です。GRS 上で動的にエンキューされているデータセット名と保有 (EXCL / SHR) を表示する。データセット競合解析に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切照合の目的で D DLS 目的の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D DLS 目的の出力を取らず区切照合の目的の説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて区切照合の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切照合の目的の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切照合の目的へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠では D DLS 目的 は「区切照合の目的に関係する定義値と表示行を照合する区切照合項目」と D A,L または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡では D DLS 目的の属性行と IEE115I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明だけに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出では D DLS 目的を MVS オペレータコマンドの運用手順で確認し、初出名は区切照合初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 優先確認の目的に関する D DLS 目的の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先確認の目的の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先確認の目的の証跡として保存して根拠にする。</li><li>C. D DLS 目的の変更点を出力本文から切り離して優先確認の目的の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 優先確認の目的において選択記号 D を採用し、識別名は優先確認です。優先確認の目的において D DLS 目的 は説明欄の「D DLS 目的の状態と出力メッセージを結び付ける優先確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認の目的に関する記録は、D DLS 目的の出力行と IEE115I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先確認ではありません。 B: 優先確認の目的は別カテゴリの確認を流用しており、D DLS 目的の根拠にならないため優先確認ではありません。 C: 優先確認の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認の目的は対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認の目的で記録する D DLS 目的はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D DLS 目的</strong></p><p>検証目的: 終端照合の目的について、D DLS 目的は、MVS オペレータコマンドの D DLS で確認する項目です。GRS 上で動的にエンキューされているデータセット名と保有 (EXCL / SHR) を表示すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010025の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端照合の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD DLS 目的を指定し、OSKB010025の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D DLS 目的
CASE OSKB010025
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D DLS 目的
CASE OSKB010025
SOURCE z/OS MVS Operations
D DLS 目的とOSKB010025が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010025を同じ出力で読み、終端照合の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010025
→ Enter を押す
［画面・出力］
IEE115I OSKB010025 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010025   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010025が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D DLS 目的 と OSKB010025 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010025 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D DUMP


<section class="kb-item" id="c22-i0045"><h3>D DUMP,ERRDATA</h3><p class="kb-meta">分類: D DUMP ・ 難易度: 中級</p><p>D DUMP,ERRDATAは、MVS オペレータコマンドのD DUMPで確認する項目です。SADMP / SVC DUMP の関連エラーデータの保持状況を表示。診断資料収集の補助</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較照合の操作コマンドで D DUMP,ERRDATA の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D DUMP,ERRDATA の出力を取らず比較照合の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて比較照合の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較照合の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較照合正解では選択記号 B を採用し、正解名は比較照合正解です。比較照合根拠では D DUMP,ERRDATA は「比較照合の操作コマンドに関係する定義値と表示行を照合する比較照合項目」と D A,L または該当パネルの出力を照合し、根拠名は比較照合根拠です。比較照合追跡では D DUMP,ERRDATA の属性行と IEE115I を合わせ、追跡名は比較照合追跡です。誤答側の問題点を分けます。 A: 比較照合不足は名称や説明だけに寄り、判定名は比較照合不足です。 B: 比較照合正答は対象出力と項目説明を結び、根拠名は比較照合正答です。 C: 比較照合欠落は戻り値や記録番号に寄り、欠落名は比較照合欠落です。 D: 比較照合流用は別カテゴリの確認であり、排除名は比較照合流用です。比較照合初出では D DUMP,ERRDATA を MVS オペレータコマンドの運用手順で確認し、初出名は比較照合初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 値域確認の操作コマンドに関する D DUMP,ERRDATA の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域確認の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. D DUMP,ERRDATA の変更点を出力本文から切り離して値域確認の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、値域確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域確認の操作コマンドにおいて選択記号 D を採用し、識別名は値域確認です。値域確認の操作コマンドにおいて D DUMP,ERRDATA は説明欄の「D DUMP,ERRDATA の状態と出力メッセージを結び付ける値域確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認の操作コマンドに関する記録は、D DUMP,ERRDATA の出力行と IEE115I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域確認ではありません。 B: 値域確認の操作コマンドは別カテゴリの確認を流用しており、D DUMP,ERRDATA の根拠にならないため値域確認ではありません。 C: 値域確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認の操作コマンドで記録する D DUMP,ERRDATA はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D DUMP,ERRDATA</strong></p><p>検証目的: 条件照合の操作コマンドについて、D DUMP,ERRDATA は、MVS オペレータコマンドの D DUMP で確認する項目です。SADMP / SVC DUMP の関連エラーデータの保持状況を表示。診断資料収に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010029の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD DUMP,ERRDATAを指定し、OSKB010029の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D DUMP,ERRDATA
CASE OSKB010029
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D DUMP,ERRDATA
CASE OSKB010029
SOURCE z/OS MVS Operations
D DUMP,ERRDATAとOSKB010029が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010029を同じ出力で読み、条件照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010029
→ Enter を押す
［画面・出力］
IEE115I OSKB010029 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010029   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010029が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D DUMP,ERRDATA と OSKB010029 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010029 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0046"><h3>D DUMP,OPTIONS</h3><p class="kb-meta">分類: D DUMP ・ 難易度: 中級</p><p>D DUMP,OPTIONSは、現行 CHNGDUMP / SDUMP オプション (SDATA 種別、CSA, RGN, SUM 等) を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録照合の操作コマンドに関係する D DUMP,OPTIONS の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、記録照合の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D DUMP,OPTIONS の名称と担当者名だけを残して記録照合の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録照合の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録照合正解では選択記号 A を採用し、正解名は記録照合正解です。記録照合根拠では D DUMP,OPTIONS は「D DUMP,OPTIONS の用途を操作コマンドの表示で確認する記録照合項目」と D A,L または該当パネルの出力を照合し、根拠名は記録照合根拠です。記録照合背景ではz/OS MVS Operationsの D DUMP,OPTIONS と IEE115I を同じ証跡に残し、背景名は記録照合背景です。他の選択肢を確認します。 A: 記録照合正答は対象出力と項目説明を結び、根拠名は記録照合正答です。 B: 記録照合不足は名称や説明だけに寄り、判定名は記録照合不足です。 C: 記録照合流用は別カテゴリの確認であり、排除名は記録照合流用です。 D: 記録照合欠落は戻り値や記録番号に寄り、欠落名は記録照合欠落です。記録照合用語では D DUMP,OPTIONS を MVS オペレータコマンドで扱う確認対象とし、用語名は記録照合用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 順序確認の操作コマンドで操作コマンドの運用確認を行います。D DUMP,OPTIONS の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序確認の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序確認の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、順序確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D DUMP,OPTIONS の属性行を読まず順序確認の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序確認の操作コマンドにおいて選択記号 C を採用し、識別名は順序確認です。順序確認の操作コマンドにおいて D DUMP,OPTIONS は説明欄の「z/OS MVS Operationsで D DUMP,OPTIONS の扱いを記録する順序確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認の操作コマンドを受け取る担当者は、D DUMP,OPTIONS の表示結果と IEE115I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認の操作コマンドは別カテゴリの確認を流用しており、D DUMP,OPTIONS の根拠にならないため順序確認ではありません。 B: 順序確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため順序確認ではありません。 C: 順序確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認の操作コマンドが示す D DUMP,OPTIONS は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D DUMP,OPTIONS</strong></p><p>検証目的: 出力照合の操作コマンドについて、D DUMP,OPTIONS は、現行 CHNGDUMP / SDUMP オプション (SDATA 種別、CSA, RGN, SUM 等) を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010028の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD DUMP,OPTIONSを指定し、OSKB010028の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D DUMP,OPTIONS
CASE OSKB010028
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D DUMP,OPTIONS
CASE OSKB010028
SOURCE z/OS MVS Operations
D DUMP,OPTIONSとOSKB010028が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010028を同じ出力で読み、出力照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010028
→ Enter を押す
［画面・出力］
IEE115I OSKB010028 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010028   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010028が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D DUMP,OPTIONS と OSKB010028 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010028 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0047"><h3>D DUMP,STATUS</h3><p class="kb-meta">分類: D DUMP ・ 難易度: 中級</p><p>D DUMP,STATUSは、SVC ダンプ・データセット (SYS1.DUMPnn) の使用状況 (空き/フル) を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲照合の操作コマンドで操作コマンドの運用確認を行います。D DUMP,STATUS の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲照合の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲照合の操作コマンドを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を範囲照合で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D DUMP,STATUS の属性行を読まず範囲照合の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では D DUMP,STATUS は「z/OS MVS Operationsで D DUMP,STATUS の扱いを記録する範囲照合項目」と D A,L または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では D DUMP,STATUS の表示結果と IEE115I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明だけに寄り、判定名は範囲照合不足です。範囲照合資料では D DUMP,STATUS の使い方を出典欄から追跡し、資料名は範囲照合資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 記録確認の操作コマンドに関係する D DUMP,STATUS の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、記録確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D DUMP,STATUS の名称と担当者名のみを残して記録確認の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で記録確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録確認の操作コマンドにおいて選択記号 A を採用し、識別名は記録確認です。記録確認の操作コマンドにおいて D DUMP,STATUS は説明欄の「D DUMP,STATUS の用途を操作コマンドの表示で確認する記録確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認の操作コマンドに関連して、z/OS MVS Operationsでは D DUMP,STATUS の表示属性と IEE115I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認の操作コマンドは別カテゴリの確認を流用しており、D DUMP,STATUS の根拠にならないため記録確認ではありません。 D: 記録確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録確認ではありません。記録確認の操作コマンドで使う D DUMP,STATUS という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D DUMP,STATUS</strong></p><p>検証目的: 探索確認の操作コマンドについて、D DUMP,STATUS は、SVC ダンプ・データセット (SYS1.DUMPnn) の使用状況 (空き/フル) を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040006の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、探索確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD DUMP,STATUSを指定し、OSKB040006の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D DUMP,STATUS
CASE OSKB040006
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D DUMP,STATUS
CASE OSKB040006
SOURCE z/OS MVS Operations
D DUMP,STATUSとOSKB040006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040006を同じ出力で読み、探索確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040006
→ Enter を押す
［画面・出力］
IEE115I OSKB040006 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040006   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D DUMP,STATUS と OSKB040006 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D DUMP,STATUS</strong></p><p>検証目的: 探索照合の操作コマンドについて、D DUMP,STATUS は、SVC ダンプ・データセット (SYS1.DUMPnn) の使用状況 (空き/フル) を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010026の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、探索照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD DUMP,STATUSを指定し、OSKB010026の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D DUMP,STATUS
CASE OSKB010026
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D DUMP,STATUS
CASE OSKB010026
SOURCE z/OS MVS Operations
D DUMP,STATUSとOSKB010026が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010026を同じ出力で読み、探索照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010026
→ Enter を押す
［画面・出力］
IEE115I OSKB010026 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010026   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010026が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D DUMP,STATUS と OSKB010026 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010026 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0048"><h3>D DUMP,TITLE</h3><p class="kb-meta">分類: D DUMP ・ 難易度: 中級</p><p>D DUMP,TITLEは、現在書き出されている SVC ダンプのタイトルと保管先 DUMP データセット番号を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先照合の操作コマンドに関する D DUMP,TITLE の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先照合の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. D DUMP,TITLE の変更点を出力本文から切り離して優先照合の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、優先照合の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠では D DUMP,TITLE は「D DUMP,TITLE の状態と出力メッセージを結び付ける優先照合項目」と D A,L または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存では D DUMP,TITLE の出力行と IEE115I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明だけに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象では D DUMP,TITLE をz/OS MVS Operationsの確認記録に残し、対象名は優先照合対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 比較確認の操作コマンドで D DUMP,TITLE の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D DUMP,TITLE の出力を取らず比較確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、比較確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較確認の操作コマンドにおいて選択記号 B を採用し、識別名は比較確認です。比較確認の操作コマンドにおいて D DUMP,TITLE は説明欄の「比較確認の操作コマンドに関係する定義値と表示行を照合する比較確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較確認です。比較確認の操作コマンドの証跡を読む担当者は、D DUMP,TITLE の属性行と IEE115I を合わせて追跡し、背景名は比較確認です。誤答側の問題点を分けます。 A: 比較確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較確認ではありません。 B: 比較確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較確認です。 C: 比較確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較確認ではありません。 D: 比較確認の操作コマンドは別カテゴリの確認を流用しており、D DUMP,TITLE の根拠にならないため比較確認ではありません。比較確認の操作コマンドに出る D DUMP,TITLE は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D DUMP,TITLE</strong></p><p>検証目的: 上書照合の操作コマンドについて、D DUMP,TITLE は、現在書き出されている SVC ダンプのタイトルと保管先 DUMP データセット番号を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010027の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD DUMP,TITLEを指定し、OSKB010027の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D DUMP,TITLE
CASE OSKB010027
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D DUMP,TITLE
CASE OSKB010027
SOURCE z/OS MVS Operations
D DUMP,TITLEとOSKB010027が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010027を同じ出力で読み、上書照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010027
→ Enter を押す
［画面・出力］
IEE115I OSKB010027 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010027   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010027が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D DUMP,TITLE と OSKB010027 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010027 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D EMCS


<section class="kb-item" id="c22-i0049"><h3>D EMCS,F=name 個別</h3><p class="kb-meta">分類: D EMCS ・ 難易度: 中級</p><p>D EMCS,F=name 個別は、MVS オペレータコマンドのD EMCSで用いる指定の EMCS コンソール名の権限・ルート・コード・属性を詳細表示する。D EMCSでは、指定値と対象資源、実行時の出力を突き合わせて確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域照合の個別に関する D EMCS 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域照合の個別の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域照合の個別の証跡として保存して根拠にする。</li><li>C. D EMCS 命令の変更点を出力本文から切り離して値域照合の個別の承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、値域照合の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域照合正解では選択記号 D を採用し、正解名は値域照合正解です。値域照合根拠では D EMCS 命令 は「D EMCS 命令の状態と出力メッセージを結び付ける値域照合項目」と D A,L または該当パネルの出力を照合し、根拠名は値域照合根拠です。値域照合保存では D EMCS 命令の出力行と IEE115I を一緒に残し、保存名は値域照合保存です。選択肢ごとの違いを示します。 A: 値域照合欠落は戻り値や記録番号に寄り、欠落名は値域照合欠落です。 B: 値域照合流用は別カテゴリの確認であり、排除名は値域照合流用です。 C: 値域照合不足は名称や説明だけに寄り、判定名は値域照合不足です。 D: 値域照合正答は対象出力と項目説明を結び、根拠名は値域照合正答です。値域照合対象では D EMCS 命令をz/OS MVS Operationsの確認記録に残し、対象名は値域照合対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 復旧確認の個別で D EMCS,F=name 個別の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D EMCS,F=name 個別の出力を取らず復旧確認の個別の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、復旧確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧確認の個別の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧確認の個別へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧確認の個別において選択記号 B を採用し、識別名は復旧確認です。復旧確認の個別において D EMCS,F=name 個別 は説明欄の「復旧確認の個別に関係する定義値と表示行を照合する復旧確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認の個別の証跡を読む担当者は、D EMCS,F=name 個別の属性行と IEE115I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認の個別は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認の個別は対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認の個別は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認の個別は別カテゴリの確認を流用しており、D EMCS,F=name 個別の根拠にならないため復旧確認ではありません。復旧確認の個別に出る D EMCS,F=name 個別は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D EMCS,F=name 個別</strong></p><p>検証目的: 範囲照合の個別について、D EMCS,F=name 個別は、MVS オペレータコマンドの D EMCS で用いる指定の EMCS コンソール名の権限・ルート・コード・属性を詳細表示する。D EMCS でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010031の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲照合の個別の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD EMCS,F=name 個別を指定し、OSKB010031の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D EMCS,F=name 個別
CASE OSKB010031
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D EMCS,F=name 個別
CASE OSKB010031
SOURCE z/OS MVS Operations
D EMCS,F=name 個別とOSKB010031が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010031を同じ出力で読み、範囲照合の個別の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010031
→ Enter を押す
［画面・出力］
IEE115I OSKB010031 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010031   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010031が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D EMCS,F=name 個別 と OSKB010031 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010031 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0050"><h3>D EMCS,S 起動中</h3><p class="kb-meta">分類: D EMCS ・ 難易度: 中級</p><p>D EMCS,S 起動中は、EMCS (拡張 MCS) コンソールとして API でアクティブ化したアプリケーション (SDSF, ISPF SYSCMD 等) を一覧表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序照合の起動中で操作コマンドの運用確認を行います。D EMCS,S 起動中の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序照合の起動中を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序照合の起動中を正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、順序照合の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D EMCS,S 起動中の属性行を読まず順序照合の起動中の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序照合正解では選択記号 C を採用し、正解名は順序照合正解です。順序照合根拠では D EMCS,S 起動中 は「z/OS MVS Operationsで D EMCS,S 起動中の扱いを記録する順序照合項目」と D A,L または該当パネルの出力を照合し、根拠名は順序照合根拠です。順序照合受渡では D EMCS,S 起動中の表示結果と IEE115I を同じ確認単位にし、受渡名は順序照合受渡です。不適切な選択肢を整理します。 A: 順序照合流用は別カテゴリの確認であり、排除名は順序照合流用です。 B: 順序照合欠落は戻り値や記録番号に寄り、欠落名は順序照合欠落です。 C: 順序照合正答は対象出力と項目説明を結び、根拠名は順序照合正答です。 D: 順序照合不足は名称や説明だけに寄り、判定名は順序照合不足です。順序照合資料では D EMCS,S 起動中の使い方を出典欄から追跡し、資料名は順序照合資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 警告確認の起動中に関係する D EMCS,S 起動中の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、警告確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D EMCS,S 起動中の名称と担当者名のみを残して警告確認の起動中の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で警告確認の起動中を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告確認の起動中の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告確認の起動中において選択記号 A を採用し、識別名は警告確認です。警告確認の起動中において D EMCS,S 起動中 は説明欄の「D EMCS,S 起動中の用途を操作コマンドの表示で確認する警告確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認の起動中に関連して、z/OS MVS Operationsでは D EMCS,S 起動中の表示属性と IEE115I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認の起動中は対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認の起動中は名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認の起動中は別カテゴリの確認を流用しており、D EMCS,S 起動中の根拠にならないため警告確認ではありません。 D: 警告確認の起動中は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告確認ではありません。警告確認の起動中で使う D EMCS,S 起動中という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D EMCS,S 起動中</strong></p><p>検証目的: 区切照合の起動中について、D EMCS,S 起動中は、EMCS (拡張 MCS) コンソールとして API でアクティブ化したアプリケーション (SDSF, ISPF SYSCMD 等) を一覧表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010030の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切照合の起動中の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD EMCS,S 起動中を指定し、OSKB010030の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D EMCS,S 起動中
CASE OSKB010030
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D EMCS,S 起動中
CASE OSKB010030
SOURCE z/OS MVS Operations
D EMCS,S 起動中とOSKB010030が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010030を同じ出力で読み、区切照合の起動中の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010030
→ Enter を押す
［画面・出力］
IEE115I OSKB010030 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010030   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010030が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D EMCS,S 起動中 と OSKB010030 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D ETR


<section class="kb-item" id="c22-i0051"><h3>D ETR 目的</h3><p class="kb-meta">分類: D ETR ・ 難易度: 初級</p><p>D ETR 目的は、MVS オペレータコマンドのD ETRで確認する項目です。外部時刻参照 (Sysplex Timer / STP) の同期状態、ストラタム、CTN ID を表示。Sysplex 時刻整合性確認の基本</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告照合の目的に関係する D ETR 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、警告照合として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D ETR 目的の名称と担当者名だけを残して警告照合の目的の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告照合の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告照合の目的の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では D ETR 目的 は「D ETR 目的の用途を操作コマンドの表示で確認する警告照合項目」と D A,L または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景ではz/OS MVS Operationsの D ETR 目的と IEE115I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明だけに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では D ETR 目的を MVS オペレータコマンドで扱う確認対象とし、用語名は警告照合用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 監査確認の目的で操作コマンドの運用確認を行います。D ETR 目的の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査確認の目的を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査確認の目的を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、監査確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D ETR 目的の属性行を読まず監査確認の目的の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 監査確認の目的において選択記号 C を採用し、識別名は監査確認です。監査確認の目的において D ETR 目的 は説明欄の「z/OS MVS Operationsで D ETR 目的の扱いを記録する監査確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認の目的を受け取る担当者は、D ETR 目的の表示結果と IEE115I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認の目的は別カテゴリの確認を流用しており、D ETR 目的の根拠にならないため監査確認ではありません。 B: 監査確認の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査確認ではありません。 C: 監査確認の目的は対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認の目的が示す D ETR 目的は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ETR 目的</strong></p><p>検証目的: 上書確認の目的について、D ETR 目的は、MVS オペレータコマンドの D ETR で確認する項目です。外部時刻参照 (Sysplex Timer / STP) の同期状態、ストラタム、CTN IDに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040007の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書確認の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ETR 目的を指定し、OSKB040007の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ETR 目的
CASE OSKB040007
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ETR 目的
CASE OSKB040007
SOURCE z/OS MVS Operations
D ETR 目的とOSKB040007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040007を同じ出力で読み、上書確認の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040007
→ Enter を押す
［画面・出力］
IEE115I OSKB040007 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040007   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ETR 目的 と OSKB040007 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D ETR 目的</strong></p><p>検証目的: 優先照合の目的について、D ETR 目的は、MVS オペレータコマンドの D ETR で確認する項目です。外部時刻参照 (Sysplex Timer / STP) の同期状態、ストラタム、CTN IDに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010032の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先照合の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ETR 目的を指定し、OSKB010032の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ETR 目的
CASE OSKB010032
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ETR 目的
CASE OSKB010032
SOURCE z/OS MVS Operations
D ETR 目的とOSKB010032が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010032を同じ出力で読み、優先照合の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010032
→ Enter を押す
［画面・出力］
IEE115I OSKB010032 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010032   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010032が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ETR 目的 と OSKB010032 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010032 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0052"><h3>D ETR,DATA データ詳細</h3><p class="kb-meta">分類: D ETR ・ 難易度: 中級</p><p>D ETR,DATA データ詳細は、STP CTN 内のサーバ ID、ストラタム階層、リーフ/ルートの関係を詳しく表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧照合のデータ詳細で D ETR 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D ETR 命令の出力を取らず復旧照合のデータ詳細の説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧照合の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧照合のデータ詳細の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧照合のデータ詳細へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧照合正解では選択記号 B を採用し、正解名は復旧照合正解です。復旧照合根拠では D ETR 命令 は「復旧照合のデータ詳細に関係する定義値と表示行を照合する復旧照合項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧照合根拠です。復旧照合追跡では D ETR 命令の属性行と IEE115I を合わせ、追跡名は復旧照合追跡です。誤答側の問題点を分けます。 A: 復旧照合不足は名称や説明だけに寄り、判定名は復旧照合不足です。 B: 復旧照合正答は対象出力と項目説明を結び、根拠名は復旧照合正答です。 C: 復旧照合欠落は戻り値や記録番号に寄り、欠落名は復旧照合欠落です。 D: 復旧照合流用は別カテゴリの確認であり、排除名は復旧照合流用です。復旧照合初出では D ETR 命令を MVS オペレータコマンドの運用手順で確認し、初出名は復旧照合初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 変更確認のデータ詳細に関する D ETR,DATA データ詳細の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更確認のデータ詳細の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更確認のデータ詳細の証跡として保存して根拠にする。</li><li>C. D ETR,DATA データ詳細の変更点を出力本文から切り離して変更確認のデータ詳細の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、変更確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更確認のデータ詳細において選択記号 D を採用し、識別名は変更確認です。変更確認のデータ詳細において D ETR,DATA データ詳細 は説明欄の「D ETR,DATA データ詳細の状態と出力メッセージを結び付ける変更確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認のデータ詳細に関する記録は、D ETR,DATA データ詳細の出力行と IEE115I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認のデータ詳細は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更確認ではありません。 B: 変更確認のデータ詳細は別カテゴリの確認を流用しており、D ETR,DATA データ詳細の根拠にならないため変更確認ではありません。 C: 変更確認のデータ詳細は名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認のデータ詳細は対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認のデータ詳細で記録する D ETR,DATA データ詳細はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D ETR,DATA データ詳細</strong></p><p>検証目的: 記録照合のデータ詳細について、D ETR,DATA データ詳細は、STP CTN 内のサーバ ID、ストラタム階層、リーフ/ルートの関係を詳しく表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010033の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録照合のデータ詳細の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD ETR,DATA データ詳細を指定し、OSKB010033の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D ETR,DATA データ詳細
CASE OSKB010033
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D ETR,DATA データ詳細
CASE OSKB010033
SOURCE z/OS MVS Operations
D ETR,DATA データ詳細とOSKB010033が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010033を同じ出力で読み、記録照合のデータ詳細の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010033
→ Enter を押す
［画面・出力］
IEE115I OSKB010033 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010033   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010033が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D ETR,DATA データ詳細 と OSKB010033 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010033 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D GRS


<section class="kb-item" id="c22-i0053"><h3>D GRS 目的</h3><p class="kb-meta">分類: D GRS ・ 難易度: 初級</p><p>GRS (グローバル・リソース・シリアライゼーション) の構成・状態を表示。データセット競合 / ENQ 状態の調査入口</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査照合の目的で操作コマンドの運用確認を行います。D GRS 目的の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査照合の目的を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査照合の目的を正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、監査照合の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D GRS 目的の属性行を読まず監査照合の目的の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 監査照合正解では選択記号 C を採用し、正解名は監査照合正解です。監査照合根拠では D GRS 目的 は「z/OS MVS Operationsで D GRS 目的の扱いを記録する監査照合項目」と D A,L または該当パネルの出力を照合し、根拠名は監査照合根拠です。監査照合受渡では D GRS 目的の表示結果と IEE115I を同じ確認単位にし、受渡名は監査照合受渡です。不適切な選択肢を整理します。 A: 監査照合流用は別カテゴリの確認であり、排除名は監査照合流用です。 B: 監査照合欠落は戻り値や記録番号に寄り、欠落名は監査照合欠落です。 C: 監査照合正答は対象出力と項目説明を結び、根拠名は監査照合正答です。 D: 監査照合不足は名称や説明だけに寄り、判定名は監査照合不足です。監査照合資料では D GRS 目的の使い方を出典欄から追跡し、資料名は監査照合資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文照合の目的に関係する D GRS 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D GRS 目的の名称と担当者名のみを残して構文照合の目的の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文照合の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文照合の目的の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 構文照合の目的において選択記号 A を採用し、識別名は構文照合です。構文照合の目的において D GRS 目的 は説明欄の「D GRS 目的の用途を操作コマンドの表示で確認する構文照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合の目的に関連して、z/OS MVS Operationsでは D GRS 目的の表示属性と IEE115I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合の目的は対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合の目的は別カテゴリの確認を流用しており、D GRS 目的の根拠にならないため構文照合ではありません。 D: 構文照合の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文照合ではありません。構文照合の目的で使う D GRS 目的という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D GRS 目的</strong></p><p>検証目的: 比較照合の目的について、GRS (グローバル・リソース・シリアライゼーション) の構成・状態を表示。データセット競合 / ENQ 状態の調査入口に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010034の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較照合の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD GRS 目的を指定し、OSKB010034の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D GRS 目的
CASE OSKB010034
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D GRS 目的
CASE OSKB010034
SOURCE z/OS MVS Operations
D GRS 目的とOSKB010034が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010034を同じ出力で読み、比較照合の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010034
→ Enter を押す
［画面・出力］
IEE115I OSKB010034 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010034   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010034が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D GRS 目的 と OSKB010034 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010034 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0054"><h3>D GRS,ALL 全表示</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>D GRS,ALL 全表示は、MVS オペレータコマンドのD GRSで確認する項目です。GRS 複合体のメンバ全 ENQ 保持・要求を出力。大量のため通常はオフロード前提で使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更照合の全表示に関する D GRS,ALL 全表示の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更照合の全表示の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更照合の全表示の証跡として保存して根拠にする。</li><li>C. D GRS,ALL 全表示の変更点を出力本文から切り離して変更照合の全表示の承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更照合で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更照合正解では選択記号 D を採用し、正解名は変更照合正解です。変更照合根拠では D GRS,ALL 全表示 は「D GRS,ALL 全表示の状態と出力メッセージを結び付ける変更照合項目」と D A,L または該当パネルの出力を照合し、根拠名は変更照合根拠です。変更照合保存では D GRS,ALL 全表示の出力行と IEE115I を一緒に残し、保存名は変更照合保存です。選択肢ごとの違いを示します。 A: 変更照合欠落は戻り値や記録番号に寄り、欠落名は変更照合欠落です。 B: 変更照合流用は別カテゴリの確認であり、排除名は変更照合流用です。 C: 変更照合不足は名称や説明だけに寄り、判定名は変更照合不足です。 D: 変更照合正答は対象出力と項目説明を結び、根拠名は変更照合正答です。変更照合対象では D GRS,ALL 全表示をz/OS MVS Operationsの確認記録に残し、対象名は変更照合対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開照合の全表示で D GRS,ALL 全表示の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D GRS,ALL 全表示の出力を取らず展開照合の全表示の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開照合の全表示の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開照合の全表示へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開照合の全表示において選択記号 B を採用し、識別名は展開照合です。展開照合の全表示において D GRS,ALL 全表示 は説明欄の「展開照合の全表示に関係する定義値と表示行を照合する展開照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合の全表示の証跡を読む担当者は、D GRS,ALL 全表示の属性行と IEE115I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合の全表示は名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合の全表示は対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合の全表示は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開照合ではありません。 D: 展開照合の全表示は別カテゴリの確認を流用しており、D GRS,ALL 全表示の根拠にならないため展開照合ではありません。展開照合の全表示に出る D GRS,ALL 全表示は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D GRS,ALL 全表示</strong></p><p>検証目的: 順序照合の全表示について、D GRS,ALL 全表示は、MVS オペレータコマンドの D GRS で確認する項目です。GRS 複合体のメンバ全 ENQ 保持・要求を出力。大量のため通常はオフロード前提でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010035の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序照合の全表示の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD GRS,ALL 全表示を指定し、OSKB010035の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D GRS,ALL 全表示
CASE OSKB010035
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D GRS,ALL 全表示
CASE OSKB010035
SOURCE z/OS MVS Operations
D GRS,ALL 全表示とOSKB010035が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010035を同じ出力で読み、順序照合の全表示の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010035
→ Enter を押す
［画面・出力］
IEE115I OSKB010035 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010035   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010035が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D GRS,ALL 全表示 と OSKB010035 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010035 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0055"><h3>D GRS,C 競合 (CONTENTION)</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>D GRS,C 競合 (CONTENTION)は、MVS オペレータコマンドのD GRSで確認する項目です。現在他者を待たせている ENQ または待たされている ENQ のみを表示。デッドロック・遅延ジョブ調査の必須形式</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文追跡の競合に関係する D GRS,C 競合 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、構文追跡の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D GRS,C 競合 属性の名称と担当者名だけを残して構文追跡の競合の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文追跡の競合を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文追跡の競合の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文追跡正解では選択記号 A を採用し、正解名は構文追跡正解です。構文追跡根拠では D GRS,C 競合 属性 は「D GRS,C 競合 属性の用途を操作コマンドの表示で確認する構文追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は構文追跡根拠です。構文追跡背景ではz/OS MVS Operationsの D GRS,C 競合 属性と IEE115I を同じ証跡に残し、背景名は構文追跡背景です。他の選択肢を確認します。 A: 構文追跡正答は対象出力と項目説明を結び、根拠名は構文追跡正答です。 B: 構文追跡不足は名称や説明だけに寄り、判定名は構文追跡不足です。 C: 構文追跡流用は別カテゴリの確認であり、排除名は構文追跡流用です。 D: 構文追跡欠落は戻り値や記録番号に寄り、欠落名は構文追跡欠落です。構文追跡用語では D GRS,C 競合 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は構文追跡用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出照合の競合で操作コマンドの運用確認を行います。D GRS,C 競合 (CONTENTION)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出照合の競合を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出照合の競合を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D GRS,C 競合 (CONTENTION)の属性行を読まず呼出照合の競合の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出照合の競合において選択記号 C を採用し、識別名は呼出照合です。呼出照合の競合において D GRS,C 競合 (CONTENTION) は説明欄の「z/OS MVS Operationsで D GRS,C 競合 (CONTENTION)の扱いを記録する呼出照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合の競合を受け取る担当者は、D GRS,C 競合 (CONTENTION)の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合の競合は別カテゴリの確認を流用しており、D GRS,C 競合 (CONTENTION)の根拠にならないため呼出照合ではありません。 B: 呼出照合の競合は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合の競合は対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合の競合は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合の競合が示す D GRS,C 競合 (CONTENTION)は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D GRS,C 競合 (CONTENTION)</strong></p><p>検証目的: 値域照合の競合について、D GRS,C 競合 (CONTENTION)は、MVS オペレータコマンドの D GRS で確認する項目です。現在他者を待たせている ENQ または待たされている ENQ のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010036の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域照合の競合の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD GRS,C 競合 (CONTENを指定し、OSKB010036の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D GRS,C 競合 (CONTEN
CASE OSKB010036
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D GRS,C 競合 (CONTEN
CASE OSKB010036
SOURCE z/OS MVS Operations
D GRS,C 競合 (CONTENとOSKB010036が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010036を同じ出力で読み、値域照合の競合の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010036
→ Enter を押す
［画面・出力］
IEE115I OSKB010036 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010036   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010036が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D GRS,C 競合 (CONTEN と OSKB010036 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010036 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0056"><h3>D GRS,DELAY 遅延 ENQ</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>D GRS,DELAY 遅延 ENQは、MVS オペレータコマンドのD GRSで確認する項目です。GRSCNFxx で定義された遅延しきい値を超えた ENQ 要求のみを抽出。長時間ロック調査用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端追跡の遅延に関係する D GRS 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、終端追跡の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D GRS 命令の名称と担当者名だけを残して終端追跡の遅延の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端追跡の遅延を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端追跡の遅延の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端追跡正解では選択記号 A を採用し、正解名は終端追跡正解です。終端追跡根拠では D GRS 命令 は「D GRS 命令の用途を操作コマンドの表示で確認する終端追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は終端追跡根拠です。終端追跡背景ではz/OS MVS Operationsの D GRS 命令と IEE115I を同じ証跡に残し、背景名は終端追跡背景です。他の選択肢を確認します。 A: 終端追跡正答は対象出力と項目説明を結び、根拠名は終端追跡正答です。 B: 終端追跡不足は名称や説明だけに寄り、判定名は終端追跡不足です。 C: 終端追跡流用は別カテゴリの確認であり、排除名は終端追跡流用です。 D: 終端追跡欠落は戻り値や記録番号に寄り、欠落名は終端追跡欠落です。終端追跡用語では D GRS 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は終端追跡用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書照合の遅延で操作コマンドの運用確認を行います。D GRS,DELAY 遅延 ENQ の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書照合の遅延を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書照合の遅延を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D GRS,DELAY 遅延 ENQ の属性行を読まず上書照合の遅延の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書照合の遅延において選択記号 C を採用し、識別名は上書照合です。上書照合の遅延において D GRS,DELAY 遅延 ENQ は説明欄の「z/OS MVS Operationsで D GRS,DELAY 遅延 ENQ の扱いを記録する上書照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の遅延を受け取る担当者は、D GRS,DELAY 遅延 ENQ の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の遅延は別カテゴリの確認を流用しており、D GRS,DELAY 遅延 ENQ の根拠にならないため上書照合ではありません。 B: 上書照合の遅延は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書照合ではありません。 C: 上書照合の遅延は対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の遅延は名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の遅延が示す D GRS,DELAY 遅延 ENQ は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D GRS,DELAY 遅延 ENQ</strong></p><p>検証目的: 変更照合の遅延について、D GRS,DELAY 遅延 ENQ は、MVS オペレータコマンドの D GRS で確認する項目です。GRSCNFxx で定義された遅延しきい値を超えた ENQ 要求のみを抽出に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010040の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更照合の遅延の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD GRS,DELAY 遅延 ENQを指定し、OSKB010040の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D GRS,DELAY 遅延 ENQ
CASE OSKB010040
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D GRS,DELAY 遅延 ENQ
CASE OSKB010040
SOURCE z/OS MVS Operations
D GRS,DELAY 遅延 ENQとOSKB010040が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010040を同じ出力で読み、変更照合の遅延の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010040
→ Enter を押す
［画面・出力］
IEE115I OSKB010040 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010040   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010040が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D GRS,DELAY 遅延 ENQ と OSKB010040 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010040 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0057"><h3>D GRS,LINK</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>D GRS,LINKは、MVS オペレータコマンドのD GRSで用いるGRS STAR の CF 結合機構リンクおよびリング CTC 接続の状態を表示する。D GRSでは、指定値と対象資源、実行時の出力を突き合わせて確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換追跡の操作コマンドに関する D GRS,LINK の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換追跡の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換追跡の操作コマンドの証跡として保存して根拠にする。</li><li>C. D GRS,LINK の変更点を出力本文から切り離して置換追跡の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、置換追跡の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換追跡正解では選択記号 D を採用し、正解名は置換追跡正解です。置換追跡根拠では D GRS,LINK は「D GRS,LINK の状態と出力メッセージを結び付ける置換追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は置換追跡根拠です。置換追跡保存では D GRS,LINK の出力行と IEE115I を一緒に残し、保存名は置換追跡保存です。選択肢ごとの違いを示します。 A: 置換追跡欠落は戻り値や記録番号に寄り、欠落名は置換追跡欠落です。 B: 置換追跡流用は別カテゴリの確認であり、排除名は置換追跡流用です。 C: 置換追跡不足は名称や説明だけに寄り、判定名は置換追跡不足です。 D: 置換追跡正答は対象出力と項目説明を結び、根拠名は置換追跡正答です。置換追跡対象では D GRS,LINK をz/OS MVS Operationsの確認記録に残し、対象名は置換追跡対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索照合の操作コマンドで D GRS,LINK の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D GRS,LINK の出力を取らず探索照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索照合の操作コマンドにおいて選択記号 B を採用し、識別名は探索照合です。探索照合の操作コマンドにおいて D GRS,LINK は説明欄の「探索照合の操作コマンドに関係する定義値と表示行を照合する探索照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合の操作コマンドの証跡を読む担当者は、D GRS,LINK の属性行と IEE115I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索照合ではありません。 D: 探索照合の操作コマンドは別カテゴリの確認を流用しており、D GRS,LINK の根拠にならないため探索照合ではありません。探索照合の操作コマンドに出る D GRS,LINK は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D GRS,LINK</strong></p><p>検証目的: 監査照合の操作コマンドについて、D GRS,LINK は、MVS オペレータコマンドの D GRS で用いる GRS STAR の CF 結合機構リンクおよびリング CTC 接続の状態を表示する。D GRS では、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010039の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD GRS,LINKを指定し、OSKB010039の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D GRS,LINK
CASE OSKB010039
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D GRS,LINK
CASE OSKB010039
SOURCE z/OS MVS Operations
D GRS,LINKとOSKB010039が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010039を同じ出力で読み、監査照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010039
→ Enter を押す
［画面・出力］
IEE115I OSKB010039 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010039   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010039が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D GRS,LINK と OSKB010039 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010039 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0058"><h3>D GRS,RES=(qname,rname)</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>D GRS,RES=(qname,rname)は、メジャー名 / マイナ名を指定し、その特定リソースの保有者・待機者だけを抽出表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開追跡の操作コマンドで D GRS,RES= 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D GRS,RES= 属性の出力を取らず展開追跡の操作コマンドの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて展開追跡の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開追跡の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開追跡正解では選択記号 B を採用し、正解名は展開追跡正解です。展開追跡根拠では D GRS,RES= 属性 は「展開追跡の操作コマンドに関係する定義値と表示行を照合する展開追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は展開追跡根拠です。展開追跡追跡では D GRS,RES= 属性の属性行と IEE115I を合わせ、追跡名は展開追跡追跡です。誤答側の問題点を分けます。 A: 展開追跡不足は名称や説明だけに寄り、判定名は展開追跡不足です。 B: 展開追跡正答は対象出力と項目説明を結び、根拠名は展開追跡正答です。 C: 展開追跡欠落は戻り値や記録番号に寄り、欠落名は展開追跡欠落です。 D: 展開追跡流用は別カテゴリの確認であり、排除名は展開追跡流用です。展開追跡初出では D GRS,RES= 属性を MVS オペレータコマンドの運用手順で確認し、初出名は展開追跡初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換照合の操作コマンドに関する D GRS,RES=(qname,rname)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. D GRS,RES=(qname,rname)の変更点を出力本文から切り離して置換照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換照合の操作コマンドにおいて選択記号 D を採用し、識別名は置換照合です。置換照合の操作コマンドにおいて D GRS,RES=(qname,rname) は説明欄の「D GRS,RES=(qname,rname)の状態と出力メッセージを結び付ける置換照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合の操作コマンドに関する記録は、D GRS,RES=(qname,rname)の出力行と IEE115I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換照合ではありません。 B: 置換照合の操作コマンドは別カテゴリの確認を流用しており、D GRS,RES=(qname,rname)の根拠にならないため置換照合ではありません。 C: 置換照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合の操作コマンドで記録する D GRS,RES=(qname,rname)はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D GRS,RES=(qname,rname)</strong></p><p>検証目的: 警告照合の操作コマンドについて、D GRS,RES=(qname,rname)は、メジャー名 / マイナ名を指定し、その特定リソースの保有者・待機者だけを抽出表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010037の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD GRS,RES=(qname,rを指定し、OSKB010037の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D GRS,RES=(qname,r
CASE OSKB010037
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D GRS,RES=(qname,r
CASE OSKB010037
SOURCE z/OS MVS Operations
D GRS,RES=(qname,rとOSKB010037が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010037を同じ出力で読み、警告照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010037
→ Enter を押す
［画面・出力］
IEE115I OSKB010037 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010037   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010037が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D GRS,RES=(qname,r と OSKB010037 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010037 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0059"><h3>D GRS,SUSPEND サスペンド一覧</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>D GRS,SUSPEND サスペンド一覧は、GRS によりサスペンド中のジョブ・タスクを表示し、どのリソース待ちで止まっているか把握する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索追跡のサスペンド一覧で D GRS 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D GRS 命令の出力を取らず探索追跡のサスペンド一覧の説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて探索追跡の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索追跡のサスペンド一覧の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索追跡のサスペンド一覧へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索追跡正解では選択記号 B を採用し、正解名は探索追跡正解です。探索追跡根拠では D GRS 命令 は「探索追跡のサスペンド一覧に関係する定義値と表示行を照合する探索追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は探索追跡根拠です。探索追跡追跡では D GRS 命令の属性行と IEE115I を合わせ、追跡名は探索追跡追跡です。誤答側の問題点を分けます。 A: 探索追跡不足は名称や説明だけに寄り、判定名は探索追跡不足です。 B: 探索追跡正答は対象出力と項目説明を結び、根拠名は探索追跡正答です。 C: 探索追跡欠落は戻り値や記録番号に寄り、欠落名は探索追跡欠落です。 D: 探索追跡流用は別カテゴリの確認であり、排除名は探索追跡流用です。探索追跡初出では D GRS 命令を MVS オペレータコマンドの運用手順で確認し、初出名は探索追跡初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力照合のサスペンド一覧に関する D GRS,SUSPEND サスペンド一覧の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力照合のサスペンド一覧の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力照合のサスペンド一覧の証跡として保存して根拠にする。</li><li>C. D GRS,SUSPEND サスペンド一覧の変更点を出力本文から切り離して出力照合のサスペンド一覧の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力照合のサスペンド一覧において選択記号 D を採用し、識別名は出力照合です。出力照合のサスペンド一覧において D GRS,SUSPEND サスペンド一覧 は説明欄の「D GRS,SUSPEND サスペンド一覧の状態と出力メッセージを結び付ける出力照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合のサスペンド一覧に関する記録は、D GRS,SUSPEND サスペンド一覧の出力行と IEE115I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合のサスペンド一覧は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力照合ではありません。 B: 出力照合のサスペンド一覧は別カテゴリの確認を流用しており、D GRS,SUSPEND サスペンド一覧の根拠にならないため出力照合ではありません。 C: 出力照合のサスペンド一覧は名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合のサスペンド一覧は対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合のサスペンド一覧で記録する D GRS,SUSPEND サスペンド一覧はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D GRS,SUSPEND サスペンド一覧</strong></p><p>検証目的: 構文追跡のサスペンド一覧について、D GRS,SUSPEND サスペンド一覧は、GRS によりサスペンド中のジョブ・タスクを表示し、どのリソース待ちで止まっているか把握するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010041の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文追跡のサスペンド一覧の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD GRS,SUSPEND サスペンを指定し、OSKB010041の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D GRS,SUSPEND サスペン
CASE OSKB010041
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D GRS,SUSPEND サスペン
CASE OSKB010041
SOURCE z/OS MVS Operations
D GRS,SUSPEND サスペンとOSKB010041が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010041を同じ出力で読み、構文追跡のサスペンド一覧の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010041
→ Enter を押す
［画面・出力］
IEE115I OSKB010041 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010041   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010041が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D GRS,SUSPEND サスペン と OSKB010041 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010041 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0060"><h3>D GRS,SYSTEM</h3><p class="kb-meta">分類: D GRS ・ 難易度: 中級</p><p>D GRS,SYSTEMは、MVS オペレータコマンドのD GRSで確認する項目です。GRS 複合体に参加している全システムとリング/STAR モード上の状態を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出追跡の操作コマンドで操作コマンドの運用確認を行います。D GRS,SYSTEM の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出追跡の操作コマンドを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を呼出追跡で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D GRS,SYSTEM の属性行を読まず呼出追跡の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では D GRS,SYSTEM は「z/OS MVS Operationsで D GRS,SYSTEM の扱いを記録する呼出追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では D GRS,SYSTEM の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明だけに寄り、判定名は呼出追跡不足です。呼出追跡資料では D GRS,SYSTEM の使い方を出典欄から追跡し、資料名は呼出追跡資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端照合の操作コマンドに関係する D GRS,SYSTEM の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D GRS,SYSTEM の名称と担当者名のみを残して終端照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端照合の操作コマンドにおいて選択記号 A を採用し、識別名は終端照合です。終端照合の操作コマンドにおいて D GRS,SYSTEM は説明欄の「D GRS,SYSTEM の用途を操作コマンドの表示で確認する終端照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合の操作コマンドに関連して、z/OS MVS Operationsでは D GRS,SYSTEM の表示属性と IEE115I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合の操作コマンドは別カテゴリの確認を流用しており、D GRS,SYSTEM の根拠にならないため終端照合ではありません。 D: 終端照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端照合ではありません。終端照合の操作コマンドで使う D GRS,SYSTEM という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D GRS,SYSTEM</strong></p><p>検証目的: 出力確認の操作コマンドについて、D GRS,SYSTEM は、MVS オペレータコマンドの D GRS で確認する項目です。GRS 複合体に参加している全システムとリング/STAR モード上の状態を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040008の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD GRS,SYSTEMを指定し、OSKB040008の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D GRS,SYSTEM
CASE OSKB040008
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D GRS,SYSTEM
CASE OSKB040008
SOURCE z/OS MVS Operations
D GRS,SYSTEMとOSKB040008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040008を同じ出力で読み、出力確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040008
→ Enter を押す
［画面・出力］
IEE115I OSKB040008 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040008   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D GRS,SYSTEM と OSKB040008 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D GRS,SYSTEM</strong></p><p>検証目的: 復旧照合の操作コマンドについて、D GRS,SYSTEM は、MVS オペレータコマンドの D GRS で確認する項目です。GRS 複合体に参加している全システムとリング/STAR モード上の状態を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010038の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD GRS,SYSTEMを指定し、OSKB010038の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D GRS,SYSTEM
CASE OSKB010038
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D GRS,SYSTEM
CASE OSKB010038
SOURCE z/OS MVS Operations
D GRS,SYSTEMとOSKB010038が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010038を同じ出力で読み、復旧照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010038
→ Enter を押す
［画面・出力］
IEE115I OSKB010038 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010038   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010038が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D GRS,SYSTEM と OSKB010038 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010038 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D IOS


<section class="kb-item" id="c22-i0061"><h3>D IOS,CAPTUUCB</h3><p class="kb-meta">分類: D IOS ・ 難易度: 中級</p><p>D IOS,CAPTUUCBは、Captured UCB の利用状況 (24 bit 以下に取り込まれた UCB) を表示し、レガシー領域逼迫の有無を確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲追跡の操作コマンドで操作コマンドの運用確認を行います。D IOS,CAPTUUCB の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲追跡の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、範囲追跡の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D IOS,CAPTUUCB の属性行を読まず範囲追跡の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では D IOS,CAPTUUCB は「z/OS MVS Operationsで D IOS,CAPTUUCB の扱いを記録する範囲追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では D IOS,CAPTUUCB の表示結果と IEE115I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明だけに寄り、判定名は範囲追跡不足です。範囲追跡資料では D IOS,CAPTUUCB の使い方を出典欄から追跡し、資料名は範囲追跡資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 記録照合の操作コマンドに関係する D IOS,CAPTUUCB の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、記録照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D IOS,CAPTUUCB の名称と担当者名のみを残して記録照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で記録照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録照合の操作コマンドにおいて選択記号 A を採用し、識別名は記録照合です。記録照合の操作コマンドにおいて D IOS,CAPTUUCB は説明欄の「D IOS,CAPTUUCB の用途を操作コマンドの表示で確認する記録照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合の操作コマンドに関連して、z/OS MVS Operationsでは D IOS,CAPTUUCB の表示属性と IEE115I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合の操作コマンドは別カテゴリの確認を流用しており、D IOS,CAPTUUCB の根拠にならないため記録照合ではありません。 D: 記録照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録照合ではありません。記録照合の操作コマンドで使う D IOS,CAPTUUCB という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D IOS,CAPTUUCB</strong></p><p>検証目的: 探索追跡の操作コマンドについて、D IOS,CAPTUUCB は、Captured UCB の利用状況 (24 bit 以下に取り込まれた UCB) を表示し、レガシー領域逼迫の有無を確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010046の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、探索追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IOS,CAPTUUCBを指定し、OSKB010046の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IOS,CAPTUUCB
CASE OSKB010046
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IOS,CAPTUUCB
CASE OSKB010046
SOURCE z/OS MVS Operations
D IOS,CAPTUUCBとOSKB010046が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010046を同じ出力で読み、探索追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010046
→ Enter を押す
［画面・出力］
IEE115I OSKB010046 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010046   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010046が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IOS,CAPTUUCB と OSKB010046 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010046 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0062"><h3>D IOS,CONFIG ハードウェア構成</h3><p class="kb-meta">分類: D IOS ・ 難易度: 中級</p><p>D IOS,CONFIG ハードウェア構成は、IODF / HCD で活性化された I/O 構成のサマリ (チャネル数、CU 数、装置数、CONFIG TOKEN) を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書追跡のハードウェア構成で操作コマンドの運用確認を行います。D IOS 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書追跡のハードウェア構成を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書追跡のハードウェア構成を正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、上書追跡の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D IOS 命令の属性行を読まず上書追跡のハードウェア構成の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書追跡正解では選択記号 C を採用し、正解名は上書追跡正解です。上書追跡根拠では D IOS 命令 は「z/OS MVS Operationsで D IOS 命令の扱いを記録する上書追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は上書追跡根拠です。上書追跡受渡では D IOS 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は上書追跡受渡です。不適切な選択肢を整理します。 A: 上書追跡流用は別カテゴリの確認であり、排除名は上書追跡流用です。 B: 上書追跡欠落は戻り値や記録番号に寄り、欠落名は上書追跡欠落です。 C: 上書追跡正答は対象出力と項目説明を結び、根拠名は上書追跡正答です。 D: 上書追跡不足は名称や説明だけに寄り、判定名は上書追跡不足です。上書追跡資料では D IOS 命令の使い方を出典欄から追跡し、資料名は上書追跡資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件照合のハードウェア構成に関係する D IOS,CONFIG ハードウェア構成の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D IOS,CONFIG ハードウェア構成の名称と担当者名のみを残して条件照合のハードウェア構成の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件照合のハードウェア構成を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件照合のハードウェア構成の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件照合のハードウェア構成において選択記号 A を採用し、識別名は条件照合です。条件照合のハードウェア構成において D IOS,CONFIG ハードウェア構成 は説明欄の「D IOS,CONFIG ハードウェア構成の用途を操作コマンドの表示で確認する条件照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合のハードウェア構成に関連して、z/OS MVS Operationsでは D IOS,CONFIG ハードウェア構成の表示属性と IEE115I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合のハードウェア構成は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合のハードウェア構成は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合のハードウェア構成は別カテゴリの確認を流用しており、D IOS,CONFIG ハードウェア構成の根拠にならないため条件照合ではありません。 D: 条件照合のハードウェア構成は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件照合ではありません。条件照合のハードウェア構成で使う D IOS,CONFIG ハードウェア構成という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D IOS,CONFIG ハードウェア構成</strong></p><p>検証目的: 展開追跡のハードウェア構成について、D IOS,CONFIG ハードウェア構成は、IODF / HCD で活性化された I/O 構成のサマリ (チャネル数、CU 数、装置数、CONFIG TOKEN) を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010042の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開追跡のハードウェア構成の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IOS,CONFIG ハードウェを指定し、OSKB010042の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IOS,CONFIG ハードウェ
CASE OSKB010042
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IOS,CONFIG ハードウェ
CASE OSKB010042
SOURCE z/OS MVS Operations
D IOS,CONFIG ハードウェとOSKB010042が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010042を同じ出力で読み、展開追跡のハードウェア構成の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010042
→ Enter を押す
［画面・出力］
IEE115I OSKB010042 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010042   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010042が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IOS,CONFIG ハードウェ と OSKB010042 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010042 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0063"><h3>D IOS,DCM DCM 構成</h3><p class="kb-meta">分類: D IOS ・ 難易度: 中級</p><p>D IOS,DCM DCM 構成は、Dynamic Channel-path Management の活性状況、管理対象 LCU、現在のチャネルパス割当を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先追跡の構成に関する D IOS 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先追跡の構成の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先追跡の構成の証跡として保存して根拠にする。</li><li>C. D IOS 命令の変更点を出力本文から切り離して優先追跡の構成の承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先追跡で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では D IOS 命令 は「D IOS 命令の状態と出力メッセージを結び付ける優先追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では D IOS 命令の出力行と IEE115I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明だけに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では D IOS 命令をz/OS MVS Operationsの確認記録に残し、対象名は優先追跡対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 比較照合の構成で D IOS,DCM DCM 構成の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D IOS,DCM DCM 構成の出力を取らず比較照合の構成の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、比較照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較照合の構成の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較照合の構成へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較照合の構成において選択記号 B を採用し、識別名は比較照合です。比較照合の構成において D IOS,DCM DCM 構成 は説明欄の「比較照合の構成に関係する定義値と表示行を照合する比較照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合の構成の証跡を読む担当者は、D IOS,DCM DCM 構成の属性行と IEE115I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合の構成は名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合の構成は対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合の構成は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較照合ではありません。 D: 比較照合の構成は別カテゴリの確認を流用しており、D IOS,DCM DCM 構成の根拠にならないため比較照合ではありません。比較照合の構成に出る D IOS,DCM DCM 構成は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D IOS,DCM DCM 構成</strong></p><p>検証目的: 上書追跡の構成について、D IOS,DCM DCM 構成は、Dynamic Channel-path Management の活性状況、管理対象 LCU、現在のチャネルパス割当を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010047の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書追跡の構成の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IOS,DCM DCM 構成を指定し、OSKB010047の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IOS,DCM DCM 構成
CASE OSKB010047
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IOS,DCM DCM 構成
CASE OSKB010047
SOURCE z/OS MVS Operations
D IOS,DCM DCM 構成とOSKB010047が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010047を同じ出力で読み、上書追跡の構成の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010047
→ Enter を押す
［画面・出力］
IEE115I OSKB010047 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010047   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010047が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IOS,DCM DCM 構成 と OSKB010047 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010047 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0064"><h3>D IOS,GROUP=devnum</h3><p class="kb-meta">分類: D IOS ・ 難易度: 中級</p><p>D IOS,GROUP=devnumは、指定装置を含む I/O グループの構成、PAV エイリアス、状態を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切追跡の操作コマンドで D IOS 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D IOS 命令の出力を取らず区切追跡の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切追跡の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切追跡の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠では D IOS 命令 は「区切追跡の操作コマンドに関係する定義値と表示行を照合する区切追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡では D IOS 命令の属性行と IEE115I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明だけに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出では D IOS 命令を MVS オペレータコマンドの運用手順で確認し、初出名は区切追跡初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 優先照合の操作コマンドに関する D IOS,GROUP=devnumの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. D IOS,GROUP=devnumの変更点を出力本文から切り離して優先照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先照合の操作コマンドにおいて選択記号 D を採用し、識別名は優先照合です。優先照合の操作コマンドにおいて D IOS,GROUP=devnum は説明欄の「D IOS,GROUP=devnumの状態と出力メッセージを結び付ける優先照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合の操作コマンドに関する記録は、D IOS,GROUP=devnumの出力行と IEE115I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先照合ではありません。 B: 優先照合の操作コマンドは別カテゴリの確認を流用しており、D IOS,GROUP=devnumの根拠にならないため優先照合ではありません。 C: 優先照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合の操作コマンドで記録する D IOS,GROUP=devnumはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D IOS,GROUP=devnum</strong></p><p>検証目的: 終端追跡の操作コマンドについて、D IOS,GROUP=devnumは、指定装置を含む I/O グループの構成、PAV エイリアス、状態を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010045の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IOS,GROUP=devnumを指定し、OSKB010045の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IOS,GROUP=devnum
CASE OSKB010045
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IOS,GROUP=devnum
CASE OSKB010045
SOURCE z/OS MVS Operations
D IOS,GROUP=devnumとOSKB010045が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010045を同じ出力で読み、終端追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010045
→ Enter を押す
［画面・出力］
IEE115I OSKB010045 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010045   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010045が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IOS,GROUP=devnum と OSKB010045 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010045 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0065"><h3>D IOS,HYPERPAV</h3><p class="kb-meta">分類: D IOS ・ 難易度: 中級</p><p>D IOS,HYPERPAVは、MVS オペレータコマンドのD IOSで確認する項目です。HyperPAV のセッション数および割当状況を表示。DASD 性能チューニング時の主要参照点</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件追跡の操作コマンドに関係する D IOS,HYPERPAV の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、条件追跡として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D IOS,HYPERPAV の名称と担当者名だけを残して条件追跡の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件追跡の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件追跡の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では D IOS,HYPERPAV は「D IOS,HYPERPAV の用途を操作コマンドの表示で確認する条件追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景ではz/OS MVS Operationsの D IOS,HYPERPAV と IEE115I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明だけに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では D IOS,HYPERPAV を MVS オペレータコマンドで扱う確認対象とし、用語名は条件追跡用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 範囲照合の操作コマンドで操作コマンドの運用確認を行います。D IOS,HYPERPAV の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲照合の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲照合の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D IOS,HYPERPAV の属性行を読まず範囲照合の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲照合の操作コマンドにおいて選択記号 C を採用し、識別名は範囲照合です。範囲照合の操作コマンドにおいて D IOS,HYPERPAV は説明欄の「z/OS MVS Operationsで D IOS,HYPERPAV の扱いを記録する範囲照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合の操作コマンドを受け取る担当者は、D IOS,HYPERPAV の表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合の操作コマンドは別カテゴリの確認を流用しており、D IOS,HYPERPAV の根拠にならないため範囲照合ではありません。 B: 範囲照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合の操作コマンドが示す D IOS,HYPERPAV は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D IOS,HYPERPAV</strong></p><p>検証目的: 条件確認の操作コマンドについて、D IOS,HYPERPAV は、MVS オペレータコマンドの D IOS で確認する項目です。HyperPAV のセッション数および割当状況を表示。DASD 性能チューニング時に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040009の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IOS,HYPERPAVを指定し、OSKB040009の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IOS,HYPERPAV
CASE OSKB040009
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IOS,HYPERPAV
CASE OSKB040009
SOURCE z/OS MVS Operations
D IOS,HYPERPAVとOSKB040009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040009を同じ出力で読み、条件確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040009
→ Enter を押す
［画面・出力］
IEE115I OSKB040009 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040009   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IOS,HYPERPAV と OSKB040009 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D IOS,HYPERPAV</strong></p><p>検証目的: 置換追跡の操作コマンドについて、D IOS,HYPERPAV は、MVS オペレータコマンドの D IOS で確認する項目です。HyperPAV のセッション数および割当状況を表示。DASD 性能チューニング時に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010044の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IOS,HYPERPAVを指定し、OSKB010044の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IOS,HYPERPAV
CASE OSKB010044
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IOS,HYPERPAV
CASE OSKB010044
SOURCE z/OS MVS Operations
D IOS,HYPERPAVとOSKB010044が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010044を同じ出力で読み、置換追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010044
→ Enter を押す
［画面・出力］
IEE115I OSKB010044 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010044   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010044が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IOS,HYPERPAV と OSKB010044 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010044 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0066"><h3>D IOS,MIH 監視タイマ</h3><p class="kb-meta">分類: D IOS ・ 難易度: 中級</p><p>D IOS,MIH 監視タイマは、MVS オペレータコマンドのD IOSで確認する項目です。Missing Interrupt Handler の現行タイムアウト値 (装置種別ごと) を表示する。装置スタックの早期検知設定の確認</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力追跡の監視タイマに関する D IOS,MIH 監視タイマの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力追跡の監視タイマの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力追跡の監視タイマの証跡として保存して根拠にする。</li><li>C. D IOS,MIH 監視タイマの変更点を出力本文から切り離して出力追跡の監視タイマの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、出力追跡の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では D IOS,MIH 監視タイマ は「D IOS,MIH 監視タイマの状態と出力メッセージを結び付ける出力追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では D IOS,MIH 監視タイマの出力行と IEE115I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明だけに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では D IOS,MIH 監視タイマをz/OS MVS Operationsの確認記録に残し、対象名は出力追跡対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切照合の監視タイマで D IOS,MIH 監視タイマの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D IOS,MIH 監視タイマの出力を取らず区切照合の監視タイマの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切照合の監視タイマの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切照合の監視タイマへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切照合の監視タイマにおいて選択記号 B を採用し、識別名は区切照合です。区切照合の監視タイマにおいて D IOS,MIH 監視タイマ は説明欄の「区切照合の監視タイマに関係する定義値と表示行を照合する区切照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合の監視タイマの証跡を読む担当者は、D IOS,MIH 監視タイマの属性行と IEE115I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合の監視タイマは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合の監視タイマは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合の監視タイマは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切照合ではありません。 D: 区切照合の監視タイマは別カテゴリの確認を流用しており、D IOS,MIH 監視タイマの根拠にならないため区切照合ではありません。区切照合の監視タイマに出る D IOS,MIH 監視タイマは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D IOS,MIH 監視タイマ</strong></p><p>検証目的: 呼出追跡の監視タイマについて、D IOS,MIH 監視タイマは、MVS オペレータコマンドの D IOS で確認する項目です。Missing Interrupt Handler の現行タイムアウト値 (装置に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010043の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出追跡の監視タイマの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IOS,MIH 監視タイマを指定し、OSKB010043の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IOS,MIH 監視タイマ
CASE OSKB010043
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IOS,MIH 監視タイマ
CASE OSKB010043
SOURCE z/OS MVS Operations
D IOS,MIH 監視タイマとOSKB010043が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010043を同じ出力で読み、呼出追跡の監視タイマの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010043
→ Enter を押す
［画面・出力］
IEE115I OSKB010043 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010043   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010043が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IOS,MIH 監視タイマ と OSKB010043 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010043 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D IPLINFO


<section class="kb-item" id="c22-i0067"><h3>D IPLINFO 目的</h3><p class="kb-meta">分類: D IPLINFO ・ 難易度: 初級</p><p>D IPLINFO 目的は、直近 IPL の日時、LOAD パラメータ (suffix)、IODF DSN、CLPA 有無、SYS パラメータの組合せを表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録追跡の目的に関係する D IPLINFO 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、記録追跡の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D IPLINFO 目的の名称と担当者名だけを残して記録追跡の目的の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録追跡の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録追跡の目的の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では D IPLINFO 目的 は「D IPLINFO 目的の用途を操作コマンドの表示で確認する記録追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景ではz/OS MVS Operationsの D IPLINFO 目的と IEE115I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明だけに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では D IPLINFO 目的を MVS オペレータコマンドで扱う確認対象とし、用語名は記録追跡用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 順序照合の目的で操作コマンドの運用確認を行います。D IPLINFO 目的の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序照合の目的を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序照合の目的を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、順序照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D IPLINFO 目的の属性行を読まず順序照合の目的の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 順序照合の目的において選択記号 C を採用し、識別名は順序照合です。順序照合の目的において D IPLINFO 目的 は説明欄の「z/OS MVS Operationsで D IPLINFO 目的の扱いを記録する順序照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合の目的を受け取る担当者は、D IPLINFO 目的の表示結果と IEE115I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合の目的は別カテゴリの確認を流用しており、D IPLINFO 目的の根拠にならないため順序照合ではありません。 B: 順序照合の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため順序照合ではありません。 C: 順序照合の目的は対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合の目的が示す D IPLINFO 目的は出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D IPLINFO 目的</strong></p><p>検証目的: 出力追跡の目的について、D IPLINFO 目的は、直近 IPL の日時、LOAD パラメータ (suffix)、IODF DSN、CLPA 有無、SYS パラメータの組合せを表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010048の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力追跡の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IPLINFO 目的を指定し、OSKB010048の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IPLINFO 目的
CASE OSKB010048
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IPLINFO 目的
CASE OSKB010048
SOURCE z/OS MVS Operations
D IPLINFO 目的とOSKB010048が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010048を同じ出力で読み、出力追跡の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010048
→ Enter を押す
［画面・出力］
IEE115I OSKB010048 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010048   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010048が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IPLINFO 目的 と OSKB010048 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010048 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0068"><h3>D IPLINFO,FAMILY</h3><p class="kb-meta">分類: D IPLINFO ・ 難易度: 中級</p><p>D IPLINFO,FAMILYは、MVS オペレータコマンドのD IPLINFOで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較追跡の操作コマンドで D IPLINFO 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D IPLINFO 命令の出力を取らず比較追跡の操作コマンドの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて比較追跡の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較追跡の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では D IPLINFO 命令 は「比較追跡の操作コマンドに関係する定義値と表示行を照合する比較追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では D IPLINFO 命令の属性行と IEE115I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明だけに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では D IPLINFO 命令を MVS オペレータコマンドの運用手順で確認し、初出名は比較追跡初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 値域照合の操作コマンドに関する D IPLINFO,FAMILY の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. D IPLINFO,FAMILY の変更点を出力本文から切り離して値域照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、値域照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域照合の操作コマンドにおいて選択記号 D を採用し、識別名は値域照合です。値域照合の操作コマンドにおいて D IPLINFO,FAMILY は説明欄の「D IPLINFO,FAMILY の状態と出力メッセージを結び付ける値域照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の操作コマンドに関する記録は、D IPLINFO,FAMILY の出力行と IEE115I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域照合ではありません。 B: 値域照合の操作コマンドは別カテゴリの確認を流用しており、D IPLINFO,FAMILY の根拠にならないため値域照合ではありません。 C: 値域照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の操作コマンドで記録する D IPLINFO,FAMILY はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D IPLINFO,FAMILY</strong></p><p>検証目的: 条件追跡の操作コマンドについて、D IPLINFO,FAMILY は、MVS オペレータコマンドの D IPLINFO で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読みに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010049の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IPLINFO,FAMILYを指定し、OSKB010049の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IPLINFO,FAMILY
CASE OSKB010049
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IPLINFO,FAMILY
CASE OSKB010049
SOURCE z/OS MVS Operations
D IPLINFO,FAMILYとOSKB010049が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010049を同じ出力で読み、条件追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010049
→ Enter を押す
［画面・出力］
IEE115I OSKB010049 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010049   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010049が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IPLINFO,FAMILY と OSKB010049 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010049 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0069"><h3>D IPLINFO,SYSPARM</h3><p class="kb-meta">分類: D IPLINFO ・ 難易度: 中級</p><p>D IPLINFO,SYSPARMは、IEASYS パラメータの起動時組合せ (SUFFIX のチェーン順) を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序追跡の操作コマンドで操作コマンドの運用確認を行います。D IPLINFO 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序追跡の操作コマンドを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を順序追跡で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D IPLINFO 命令の属性行を読まず順序追跡の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では D IPLINFO 命令 は「z/OS MVS Operationsで D IPLINFO 命令の扱いを記録する順序追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では D IPLINFO 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明だけに寄り、判定名は順序追跡不足です。順序追跡資料では D IPLINFO 命令の使い方を出典欄から追跡し、資料名は順序追跡資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 警告照合の操作コマンドに関係する D IPLINFO,SYSPARM の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、警告照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D IPLINFO,SYSPARM の名称と担当者名のみを残して警告照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で警告照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告照合の操作コマンドにおいて選択記号 A を採用し、識別名は警告照合です。警告照合の操作コマンドにおいて D IPLINFO,SYSPARM は説明欄の「D IPLINFO,SYSPARM の用途を操作コマンドの表示で確認する警告照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の操作コマンドに関連して、z/OS MVS Operationsでは D IPLINFO,SYSPARM の表示属性と IEE115I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の操作コマンドは別カテゴリの確認を流用しており、D IPLINFO,SYSPARM の根拠にならないため警告照合ではありません。 D: 警告照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告照合ではありません。警告照合の操作コマンドで使う D IPLINFO,SYSPARM という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D IPLINFO,SYSPARM</strong></p><p>検証目的: 区切確認の操作コマンドについて、D IPLINFO,SYSPARM は、IEASYS パラメータの起動時組合せ (SUFFIX のチェーン順) を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040010の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IPLINFO,SYSPARMを指定し、OSKB040010の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IPLINFO,SYSPARM
CASE OSKB040010
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IPLINFO,SYSPARM
CASE OSKB040010
SOURCE z/OS MVS Operations
D IPLINFO,SYSPARMとOSKB040010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040010を同じ出力で読み、区切確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040010
→ Enter を押す
［画面・出力］
IEE115I OSKB040010 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040010   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IPLINFO,SYSPARM と OSKB040010 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D IPLINFO,SYSPARM</strong></p><p>検証目的: 区切追跡の操作コマンドについて、D IPLINFO,SYSPARM は、IEASYS パラメータの起動時組合せ (SUFFIX のチェーン順) を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010050の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IPLINFO,SYSPARMを指定し、OSKB010050の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IPLINFO,SYSPARM
CASE OSKB010050
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IPLINFO,SYSPARM
CASE OSKB010050
SOURCE z/OS MVS Operations
D IPLINFO,SYSPARMとOSKB010050が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010050を同じ出力で読み、区切追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010050
→ Enter を押す
［画面・出力］
IEE115I OSKB010050 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010050   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010050が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IPLINFO,SYSPARM と OSKB010050 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010050 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0070"><h3>D IPLINFO,VER</h3><p class="kb-meta">分類: D IPLINFO ・ 難易度: 中級</p><p>D IPLINFO,VERは、z/OS リリース・サービスレベル・FMID を表示し、稼働中バージョンを確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域追跡の操作コマンドに関する D IPLINFO,VER の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域追跡の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域追跡の操作コマンドの証跡として保存して根拠にする。</li><li>C. D IPLINFO,VER の変更点を出力本文から切り離して値域追跡の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、値域追跡の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域追跡正解では選択記号 D を採用し、正解名は値域追跡正解です。値域追跡根拠では D IPLINFO,VER は「D IPLINFO,VER の状態と出力メッセージを結び付ける値域追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は値域追跡根拠です。値域追跡保存では D IPLINFO,VER の出力行と IEE115I を一緒に残し、保存名は値域追跡保存です。選択肢ごとの違いを示します。 A: 値域追跡欠落は戻り値や記録番号に寄り、欠落名は値域追跡欠落です。 B: 値域追跡流用は別カテゴリの確認であり、排除名は値域追跡流用です。 C: 値域追跡不足は名称や説明だけに寄り、判定名は値域追跡不足です。 D: 値域追跡正答は対象出力と項目説明を結び、根拠名は値域追跡正答です。値域追跡対象では D IPLINFO,VER をz/OS MVS Operationsの確認記録に残し、対象名は値域追跡対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 復旧照合の操作コマンドで D IPLINFO,VER の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D IPLINFO,VER の出力を取らず復旧照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、復旧照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧照合の操作コマンドにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合の操作コマンドにおいて D IPLINFO,VER は説明欄の「復旧照合の操作コマンドに関係する定義値と表示行を照合する復旧照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の操作コマンドの証跡を読む担当者は、D IPLINFO,VER の属性行と IEE115I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の操作コマンドは別カテゴリの確認を流用しており、D IPLINFO,VER の根拠にならないため復旧照合ではありません。復旧照合の操作コマンドに出る D IPLINFO,VER は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D IPLINFO,VER</strong></p><p>検証目的: 範囲追跡の操作コマンドについて、D IPLINFO,VER は、z/OS リリース・サービスレベル・ FMID を表示し、稼働中バージョンを確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010051の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD IPLINFO,VERを指定し、OSKB010051の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D IPLINFO,VER
CASE OSKB010051
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D IPLINFO,VER
CASE OSKB010051
SOURCE z/OS MVS Operations
D IPLINFO,VERとOSKB010051が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010051を同じ出力で読み、範囲追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010051
→ Enter を押す
［画面・出力］
IEE115I OSKB010051 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010051   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010051が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D IPLINFO,VER と OSKB010051 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010051 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D LOGGER


<section class="kb-item" id="c22-i0071"><h3>D LOGGER,C=stream</h3><p class="kb-meta">分類: D LOGGER ・ 難易度: 中級</p><p>D LOGGER,C=streamは、ログ・ストリーム名指定で接続中の全システム、構造化ログ位置、オフロード状況を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧追跡の操作コマンドで D LOGGER 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D LOGGER 命令の出力を取らず復旧追跡の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて復旧追跡の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧追跡の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠では D LOGGER 命令 は「復旧追跡の操作コマンドに関係する定義値と表示行を照合する復旧追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡では D LOGGER 命令の属性行と IEE115I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明だけに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出では D LOGGER 命令を MVS オペレータコマンドの運用手順で確認し、初出名は復旧追跡初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 変更照合の操作コマンドに関する D LOGGER,C=streamの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. D LOGGER,C=streamの変更点を出力本文から切り離して変更照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、変更照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更照合の操作コマンドにおいて選択記号 D を採用し、識別名は変更照合です。変更照合の操作コマンドにおいて D LOGGER,C=stream は説明欄の「D LOGGER,C=streamの状態と出力メッセージを結び付ける変更照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合の操作コマンドに関する記録は、D LOGGER,C=streamの出力行と IEE115I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更照合ではありません。 B: 変更照合の操作コマンドは別カテゴリの確認を流用しており、D LOGGER,C=streamの根拠にならないため変更照合ではありません。 C: 変更照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合の操作コマンドで記録する D LOGGER,C=streamはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D LOGGER,C=stream</strong></p><p>検証目的: 記録追跡の操作コマンドについて、D LOGGER,C=streamは、ログ・ストリーム名指定で接続中の全システム、構造化ログ位置、オフロード状況を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010053の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD LOGGER,C=streamを指定し、OSKB010053の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D LOGGER,C=stream
CASE OSKB010053
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D LOGGER,C=stream
CASE OSKB010053
SOURCE z/OS MVS Operations
D LOGGER,C=streamとOSKB010053が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010053を同じ出力で読み、記録追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010053
→ Enter を押す
［画面・出力］
IEE115I OSKB010053 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010053   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010053が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D LOGGER,C=stream と OSKB010053 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010053 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0072"><h3>D LOGGER,L=ALL</h3><p class="kb-meta">分類: D LOGGER ・ 難易度: 中級</p><p>D LOGGER,L=ALLは、System Logger の全ログ・ストリームと現在の使用システム、ステージング DS 状態を一覧表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告追跡の操作コマンドに関係する D LOGGER,L=ALL の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、警告追跡の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D LOGGER,L=ALL の名称と担当者名だけを残して警告追跡の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告追跡の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告追跡の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では D LOGGER,L=ALL は「D LOGGER,L=ALL の用途を操作コマンドの表示で確認する警告追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景ではz/OS MVS Operationsの D LOGGER,L=ALL と IEE115I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明だけに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では D LOGGER,L=ALL を MVS オペレータコマンドで扱う確認対象とし、用語名は警告追跡用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 監査照合の操作コマンドで操作コマンドの運用確認を行います。D LOGGER,L=ALL の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査照合の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査照合の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、監査照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D LOGGER,L=ALL の属性行を読まず監査照合の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査照合の操作コマンドにおいて選択記号 C を採用し、識別名は監査照合です。監査照合の操作コマンドにおいて D LOGGER,L=ALL は説明欄の「z/OS MVS Operationsで D LOGGER,L=ALL の扱いを記録する監査照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の操作コマンドを受け取る担当者は、D LOGGER,L=ALL の表示結果と IEE115I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の操作コマンドは別カテゴリの確認を流用しており、D LOGGER,L=ALL の根拠にならないため監査照合ではありません。 B: 監査照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査照合ではありません。 C: 監査照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の操作コマンドが示す D LOGGER,L=ALL は出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D LOGGER,L=ALL</strong></p><p>検証目的: 優先追跡の操作コマンドについて、D LOGGER,L=ALL は、System Logger の全ログ・ストリームと現在の使用システム、ステージング DS 状態を一覧表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010052の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD LOGGER,L=ALLを指定し、OSKB010052の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D LOGGER,L=ALL
CASE OSKB010052
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D LOGGER,L=ALL
CASE OSKB010052
SOURCE z/OS MVS Operations
D LOGGER,L=ALLとOSKB010052が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010052を同じ出力で読み、優先追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010052
→ Enter を押す
［画面・出力］
IEE115I OSKB010052 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010052   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010052が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D LOGGER,L=ALL と OSKB010052 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010052 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0073"><h3>D LOGGER,STATUS</h3><p class="kb-meta">分類: D LOGGER ・ 難易度: 中級</p><p>D LOGGER,STATUSは、MVS オペレータコマンドのD LOGGERで確認する項目です。Logger サブシステム全体の稼動状態とログ・データセット枯渇予兆を表示。OPERLOG・LOGREC の前提</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査追跡の操作コマンドで操作コマンドの運用確認を行います。D LOGGER,STATUS の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査追跡の操作コマンドを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、監査追跡の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D LOGGER,STATUS の属性行を読まず監査追跡の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査追跡正解では選択記号 C を採用し、正解名は監査追跡正解です。監査追跡根拠では D LOGGER,STATUS は「z/OS MVS Operationsで D LOGGER,STATUS の扱いを記録する監査追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は監査追跡根拠です。監査追跡受渡では D LOGGER,STATUS の表示結果と IEE115I を同じ確認単位にし、受渡名は監査追跡受渡です。不適切な選択肢を整理します。 A: 監査追跡流用は別カテゴリの確認であり、排除名は監査追跡流用です。 B: 監査追跡欠落は戻り値や記録番号に寄り、欠落名は監査追跡欠落です。 C: 監査追跡正答は対象出力と項目説明を結び、根拠名は監査追跡正答です。 D: 監査追跡不足は名称や説明だけに寄り、判定名は監査追跡不足です。監査追跡資料では D LOGGER,STATUS の使い方を出典欄から追跡し、資料名は監査追跡資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文追跡の操作コマンドに関係する D LOGGER,STATUS の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D LOGGER,STATUS の名称と担当者名のみを残して構文追跡の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文追跡の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文追跡の操作コマンドにおいて選択記号 A を採用し、識別名は構文追跡です。構文追跡の操作コマンドにおいて D LOGGER,STATUS は説明欄の「D LOGGER,STATUS の用途を操作コマンドの表示で確認する構文追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡の操作コマンドに関連して、z/OS MVS Operationsでは D LOGGER,STATUS の表示属性と IEE115I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡の操作コマンドは別カテゴリの確認を流用しており、D LOGGER,STATUS の根拠にならないため構文追跡ではありません。 D: 構文追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文追跡ではありません。構文追跡の操作コマンドで使う D LOGGER,STATUS という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D LOGGER,STATUS</strong></p><p>検証目的: 比較追跡の操作コマンドについて、D LOGGER,STATUS は、MVS オペレータコマンドの D LOGGER で確認する項目です。Logger サブシステム全体の稼動状態とログ・データセット枯渇予兆を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010054の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD LOGGER,STATUSを指定し、OSKB010054の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D LOGGER,STATUS
CASE OSKB010054
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D LOGGER,STATUS
CASE OSKB010054
SOURCE z/OS MVS Operations
D LOGGER,STATUSとOSKB010054が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010054を同じ出力で読み、比較追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010054
→ Enter を押す
［画面・出力］
IEE115I OSKB010054 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010054   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010054が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D LOGGER,STATUS と OSKB010054 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010054 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D LOGREC


<section class="kb-item" id="c22-i0074"><h3>D LOGREC 目的</h3><p class="kb-meta">分類: D LOGREC ・ 難易度: 初級</p><p>D LOGREC 目的は、LOGREC データセット (SYS1.LOGREC) または Logger ストリームの現在の容量・記録モードを表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更追跡の目的に関する D LOGREC 目的の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更追跡の目的の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更追跡の目的の証跡として保存して根拠にする。</li><li>C. D LOGREC 目的の変更点を出力本文から切り離して変更追跡の目的の承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、変更追跡の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 変更追跡正解では選択記号 D を採用し、正解名は変更追跡正解です。変更追跡根拠では D LOGREC 目的 は「D LOGREC 目的の状態と出力メッセージを結び付ける変更追跡項目」と D A,L または該当パネルの出力を照合し、根拠名は変更追跡根拠です。変更追跡保存では D LOGREC 目的の出力行と IEE115I を一緒に残し、保存名は変更追跡保存です。選択肢ごとの違いを示します。 A: 変更追跡欠落は戻り値や記録番号に寄り、欠落名は変更追跡欠落です。 B: 変更追跡流用は別カテゴリの確認であり、排除名は変更追跡流用です。 C: 変更追跡不足は名称や説明だけに寄り、判定名は変更追跡不足です。 D: 変更追跡正答は対象出力と項目説明を結び、根拠名は変更追跡正答です。変更追跡対象では D LOGREC 目的をz/OS MVS Operationsの確認記録に残し、対象名は変更追跡対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開追跡の目的で D LOGREC 目的の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D LOGREC 目的の出力を取らず展開追跡の目的の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開追跡の目的の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開追跡の目的へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 展開追跡の目的において選択記号 B を採用し、識別名は展開追跡です。展開追跡の目的において D LOGREC 目的 は説明欄の「展開追跡の目的に関係する定義値と表示行を照合する展開追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡の目的の証跡を読む担当者は、D LOGREC 目的の属性行と IEE115I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡の目的は対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡の目的は別カテゴリの確認を流用しており、D LOGREC 目的の根拠にならないため展開追跡ではありません。展開追跡の目的に出る D LOGREC 目的は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D LOGREC 目的</strong></p><p>検証目的: 順序追跡の目的について、D LOGREC 目的は、LOGREC データセット (SYS1.LOGREC) または Logger ストリームの現在の容量・記録モードを表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010055の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序追跡の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD LOGREC 目的を指定し、OSKB010055の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D LOGREC 目的
CASE OSKB010055
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D LOGREC 目的
CASE OSKB010055
SOURCE z/OS MVS Operations
D LOGREC 目的とOSKB010055が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010055を同じ出力で読み、順序追跡の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010055
→ Enter を押す
［画面・出力］
IEE115I OSKB010055 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010055   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010055が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D LOGREC 目的 と OSKB010055 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010055 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D LPA


<section class="kb-item" id="c22-i0075"><h3>D LPA,ALL 全体表示</h3><p class="kb-meta">分類: D LPA ・ 難易度: 中級</p><p>D LPA,ALL 全体表示は、MVS オペレータコマンドのD LPAで確認する項目です。現行 LPA に登録されている全モジュールの一覧。大量のため通常は名前指定で使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開検査の全体表示で D LPA,ALL 全体表示の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D LPA,ALL 全体表示の出力を取らず展開検査の全体表示の説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開検査の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開検査の全体表示の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開検査の全体表示へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開検査正解では選択記号 B を採用し、正解名は展開検査正解です。展開検査根拠では D LPA,ALL 全体表示 は「展開検査の全体表示に関係する定義値と表示行を照合する展開検査項目」と D A,L または該当パネルの出力を照合し、根拠名は展開検査根拠です。展開検査追跡では D LPA,ALL 全体表示の属性行と IEE115I を合わせ、追跡名は展開検査追跡です。誤答側の問題点を分けます。 A: 展開検査不足は名称や説明だけに寄り、判定名は展開検査不足です。 B: 展開検査正答は対象出力と項目説明を結び、根拠名は展開検査正答です。 C: 展開検査欠落は戻り値や記録番号に寄り、欠落名は展開検査欠落です。 D: 展開検査流用は別カテゴリの確認であり、排除名は展開検査流用です。展開検査初出では D LPA,ALL 全体表示を MVS オペレータコマンドの運用手順で確認し、初出名は展開検査初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換追跡の全体表示に関する D LPA,ALL 全体表示の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換追跡の全体表示の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換追跡の全体表示の証跡として保存して根拠にする。</li><li>C. D LPA,ALL 全体表示の変更点を出力本文から切り離して置換追跡の全体表示の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換追跡の全体表示において選択記号 D を採用し、識別名は置換追跡です。置換追跡の全体表示において D LPA,ALL 全体表示 は説明欄の「D LPA,ALL 全体表示の状態と出力メッセージを結び付ける置換追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の全体表示に関する記録は、D LPA,ALL 全体表示の出力行と IEE115I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の全体表示は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の全体表示は別カテゴリの確認を流用しており、D LPA,ALL 全体表示の根拠にならないため置換追跡ではありません。 C: 置換追跡の全体表示は名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の全体表示は対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の全体表示で記録する D LPA,ALL 全体表示はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D LPA,ALL 全体表示</strong></p><p>検証目的: 警告追跡の全体表示について、D LPA,ALL 全体表示は、MVS オペレータコマンドの D LPA で確認する項目です。現行 LPA に登録されている全モジュールの一覧。大量のため通常は名前指定で使うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010057の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告追跡の全体表示の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD LPA,ALL 全体表示を指定し、OSKB010057の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D LPA,ALL 全体表示
CASE OSKB010057
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D LPA,ALL 全体表示
CASE OSKB010057
SOURCE z/OS MVS Operations
D LPA,ALL 全体表示とOSKB010057が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010057を同じ出力で読み、警告追跡の全体表示の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010057
→ Enter を押す
［画面・出力］
IEE115I OSKB010057 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010057   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010057が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D LPA,ALL 全体表示 と OSKB010057 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010057 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0076"><h3>D LPA,MODNAME=name</h3><p class="kb-meta">分類: D LPA ・ 難易度: 中級</p><p>D LPA,MODNAME=nameは、指定モジュールが PLPA / FLPA / MLPA / Dynamic LPA のどこに存在し、ロード元データセットは何かを表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文検査の操作コマンドに関係する D LPA 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、構文検査として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D LPA 命令の名称と担当者名だけを残して構文検査の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文検査の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文検査の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文検査正解では選択記号 A を採用し、正解名は構文検査正解です。構文検査根拠では D LPA 命令 は「D LPA 命令の用途を操作コマンドの表示で確認する構文検査項目」と D A,L または該当パネルの出力を照合し、根拠名は構文検査根拠です。構文検査背景ではz/OS MVS Operationsの D LPA 命令と IEE115I を同じ証跡に残し、背景名は構文検査背景です。他の選択肢を確認します。 A: 構文検査正答は対象出力と項目説明を結び、根拠名は構文検査正答です。 B: 構文検査不足は名称や説明だけに寄り、判定名は構文検査不足です。 C: 構文検査流用は別カテゴリの確認であり、排除名は構文検査流用です。 D: 構文検査欠落は戻り値や記録番号に寄り、欠落名は構文検査欠落です。構文検査用語では D LPA 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は構文検査用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出追跡の操作コマンドで操作コマンドの運用確認を行います。D LPA,MODNAME=nameの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出追跡の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D LPA,MODNAME=nameの属性行を読まず呼出追跡の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出追跡の操作コマンドにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡の操作コマンドにおいて D LPA,MODNAME=name は説明欄の「z/OS MVS Operationsで D LPA,MODNAME=nameの扱いを記録する呼出追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡の操作コマンドを受け取る担当者は、D LPA,MODNAME=nameの表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡の操作コマンドは別カテゴリの確認を流用しており、D LPA,MODNAME=nameの根拠にならないため呼出追跡ではありません。 B: 呼出追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡の操作コマンドが示す D LPA,MODNAME=nameは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D LPA,MODNAME=name</strong></p><p>検証目的: 範囲確認の操作コマンドについて、D LPA,MODNAME=nameは、指定モジュールが PLPA / FLPA / MLPA / Dynamic LPA のどこに存在し、ロード元データセットは何かを表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040011の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD LPA,MODNAME=nameを指定し、OSKB040011の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D LPA,MODNAME=name
CASE OSKB040011
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D LPA,MODNAME=name
CASE OSKB040011
SOURCE z/OS MVS Operations
D LPA,MODNAME=nameとOSKB040011が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040011を同じ出力で読み、範囲確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040011
→ Enter を押す
［画面・出力］
IEE115I OSKB040011 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040011   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040011が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D LPA,MODNAME=name と OSKB040011 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040011 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D LPA,MODNAME=name</strong></p><p>検証目的: 値域追跡の操作コマンドについて、D LPA,MODNAME=nameは、指定モジュールが PLPA / FLPA / MLPA / Dynamic LPA のどこに存在し、ロード元データセットは何かを表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010056の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD LPA,MODNAME=nameを指定し、OSKB010056の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D LPA,MODNAME=name
CASE OSKB010056
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D LPA,MODNAME=name
CASE OSKB010056
SOURCE z/OS MVS Operations
D LPA,MODNAME=nameとOSKB010056が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010056を同じ出力で読み、値域追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010056
→ Enter を押す
［画面・出力］
IEE115I OSKB010056 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010056   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010056が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D LPA,MODNAME=name と OSKB010056 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010056 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D M


<section class="kb-item" id="c22-i0077"><h3>D M=CONFIG</h3><p class="kb-meta">分類: D M ・ 難易度: 中級</p><p>D M=CONFIGは、MVS オペレータコマンドのD Mで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索検査の操作コマンドで D M=CONFIG の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D M=CONFIG の出力を取らず探索検査の操作コマンドの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて探索検査の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索検査の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索検査の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では D M=CONFIG は「探索検査の操作コマンドに関係する定義値と表示行を照合する探索検査項目」と D A,L または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では D M=CONFIG の属性行と IEE115I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明だけに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では D M=CONFIG を MVS オペレータコマンドの運用手順で確認し、初出名は探索検査初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力追跡の操作コマンドに関する D M=CONFIG の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力追跡の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力追跡の操作コマンドの証跡として保存して根拠にする。</li><li>C. D M=CONFIG の変更点を出力本文から切り離して出力追跡の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力追跡の操作コマンドにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡の操作コマンドにおいて D M=CONFIG は説明欄の「D M=CONFIG の状態と出力メッセージを結び付ける出力追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の操作コマンドに関する記録は、D M=CONFIG の出力行と IEE115I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の操作コマンドは別カテゴリの確認を流用しており、D M=CONFIG の根拠にならないため出力追跡ではありません。 C: 出力追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の操作コマンドで記録する D M=CONFIG はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D M=CONFIG</strong></p><p>検証目的: 構文検査の操作コマンドについて、D M=CONFIG は、MVS オペレータコマンドの D M で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。zに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010061の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD M=CONFIGを指定し、OSKB010061の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D M=CONFIG
CASE OSKB010061
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D M=CONFIG
CASE OSKB010061
SOURCE z/OS MVS Operations
D M=CONFIGとOSKB010061が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010061を同じ出力で読み、構文検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010061
→ Enter を押す
［画面・出力］
IEE115I OSKB010061 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010061   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010061が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D M=CONFIG と OSKB010061 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010061 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0078"><h3>D M=CPU</h3><p class="kb-meta">分類: D M ・ 難易度: 中級</p><p>D M=CPUは、MVS オペレータコマンドのD Mで確認する項目です。オンライン/オフラインの CP / zIIP / IFL の状態、論理 CP 数、装置構成サマリを表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出検査の操作コマンドで操作コマンドの運用確認を行います。D M=CPU の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出検査の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出検査の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、呼出検査の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D M=CPU の属性行を読まず呼出検査の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出検査正解では選択記号 C を採用し、正解名は呼出検査正解です。呼出検査根拠では D M=CPU は「z/OS MVS Operationsで D M=CPU の扱いを記録する呼出検査項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出検査根拠です。呼出検査受渡では D M=CPU の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出検査受渡です。不適切な選択肢を整理します。 A: 呼出検査流用は別カテゴリの確認であり、排除名は呼出検査流用です。 B: 呼出検査欠落は戻り値や記録番号に寄り、欠落名は呼出検査欠落です。 C: 呼出検査正答は対象出力と項目説明を結び、根拠名は呼出検査正答です。 D: 呼出検査不足は名称や説明だけに寄り、判定名は呼出検査不足です。呼出検査資料では D M=CPU の使い方を出典欄から追跡し、資料名は呼出検査資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端追跡の操作コマンドに関係する D M=CPU の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D M=CPU の名称と担当者名のみを残して終端追跡の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端追跡の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端追跡の操作コマンドにおいて選択記号 A を採用し、識別名は終端追跡です。終端追跡の操作コマンドにおいて D M=CPU は説明欄の「D M=CPU の用途を操作コマンドの表示で確認する終端追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡の操作コマンドに関連して、z/OS MVS Operationsでは D M=CPU の表示属性と IEE115I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡の操作コマンドは別カテゴリの確認を流用しており、D M=CPU の根拠にならないため終端追跡ではありません。 D: 終端追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端追跡ではありません。終端追跡の操作コマンドで使う D M=CPU という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D M=CPU</strong></p><p>検証目的: 復旧追跡の操作コマンドについて、D M=CPU は、MVS オペレータコマンドの D M で確認する項目です。オンライン/オフラインの CP / zIIP / IFL の状態、論理 CP 数、装置構成サマリを表に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010058の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD M=CPUを指定し、OSKB010058の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D M=CPU
CASE OSKB010058
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D M=CPU
CASE OSKB010058
SOURCE z/OS MVS Operations
D M=CPUとOSKB010058が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010058を同じ出力で読み、復旧追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010058
→ Enter を押す
［画面・出力］
IEE115I OSKB010058 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010058   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010058が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D M=CPU と OSKB010058 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010058 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0079"><h3>D M=DEV(devnum)</h3><p class="kb-meta">分類: D M ・ 難易度: 中級</p><p>D M=DEV(devnum)は、MVS オペレータコマンドのD Mで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端検査の操作コマンドに関係する D M=DEV(devnum)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、終端検査の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D M=DEV(devnum)の名称と担当者名だけを残して終端検査の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端検査の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端検査の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では D M=DEV(devnum) は「D M=DEV(devnum)の用途を操作コマンドの表示で確認する終端検査項目」と D A,L または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景ではz/OS MVS Operationsの D M=DEV(devnum)と IEE115I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明だけに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では D M=DEV(devnum)を MVS オペレータコマンドで扱う確認対象とし、用語名は終端検査用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書追跡の操作コマンドで操作コマンドの運用確認を行います。D M=DEV(devnum)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書追跡の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D M=DEV(devnum)の属性行を読まず上書追跡の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書追跡の操作コマンドにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡の操作コマンドにおいて D M=DEV(devnum) は説明欄の「z/OS MVS Operationsで D M=DEV(devnum)の扱いを記録する上書追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡の操作コマンドを受け取る担当者は、D M=DEV(devnum)の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡の操作コマンドは別カテゴリの確認を流用しており、D M=DEV(devnum)の根拠にならないため上書追跡ではありません。 B: 上書追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡の操作コマンドが示す D M=DEV(devnum)は出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D M=DEV(devnum)</strong></p><p>検証目的: 変更追跡の操作コマンドについて、D M=DEV(devnum)は、MVS オペレータコマンドの D M で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010060の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD M=DEV(devnum)を指定し、OSKB010060の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D M=DEV(devnum)
CASE OSKB010060
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D M=DEV(devnum)
CASE OSKB010060
SOURCE z/OS MVS Operations
D M=DEV(devnum)とOSKB010060が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010060を同じ出力で読み、変更追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010060
→ Enter を押す
［画面・出力］
IEE115I OSKB010060 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010060   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010060が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D M=DEV(devnum) と OSKB010060 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010060 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0080"><h3>D M=HIGH</h3><p class="kb-meta">分類: D M ・ 難易度: 中級</p><p>D M=HIGHは、MVS オペレータコマンドのD Mで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書検査の操作コマンドで操作コマンドの運用確認を行います。D M=HIGH の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書検査の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書検査の操作コマンドを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を上書検査で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D M=HIGH の属性行を読まず上書検査の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では D M=HIGH は「z/OS MVS Operationsで D M=HIGH の扱いを記録する上書検査項目」と D A,L または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では D M=HIGH の表示結果と IEE115I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明だけに寄り、判定名は上書検査不足です。上書検査資料では D M=HIGH の使い方を出典欄から追跡し、資料名は上書検査資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件追跡の操作コマンドに関係する D M=HIGH の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D M=HIGH の名称と担当者名のみを残して条件追跡の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件追跡の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件追跡の操作コマンドにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡の操作コマンドにおいて D M=HIGH は説明欄の「D M=HIGH の用途を操作コマンドの表示で確認する条件追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の操作コマンドに関連して、z/OS MVS Operationsでは D M=HIGH の表示属性と IEE115I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の操作コマンドは別カテゴリの確認を流用しており、D M=HIGH の根拠にならないため条件追跡ではありません。 D: 条件追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件追跡ではありません。条件追跡の操作コマンドで使う D M=HIGH という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D M=HIGH</strong></p><p>検証目的: 優先確認の操作コマンドについて、D M=HIGH は、MVS オペレータコマンドの D M で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/Oに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040012の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD M=HIGHを指定し、OSKB040012の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D M=HIGH
CASE OSKB040012
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D M=HIGH
CASE OSKB040012
SOURCE z/OS MVS Operations
D M=HIGHとOSKB040012が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040012を同じ出力で読み、優先確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040012
→ Enter を押す
［画面・出力］
IEE115I OSKB040012 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040012   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040012が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D M=HIGH と OSKB040012 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040012 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D M=HIGH</strong></p><p>検証目的: 展開検査の操作コマンドについて、D M=HIGH は、MVS オペレータコマンドの D M で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/Oに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010062の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD M=HIGHを指定し、OSKB010062の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D M=HIGH
CASE OSKB010062
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D M=HIGH
CASE OSKB010062
SOURCE z/OS MVS Operations
D M=HIGHとOSKB010062が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010062を同じ出力で読み、展開検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010062
→ Enter を押す
［画面・出力］
IEE115I OSKB010062 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010062   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010062が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D M=HIGH と OSKB010062 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010062 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0081"><h3>D M=STOR</h3><p class="kb-meta">分類: D M ・ 難易度: 中級</p><p>D M=STORは、MVS オペレータコマンドのD Mで確認する項目です。実ストレージのオンライン量、構成、フレーム数を表示。LPAR 動的拡張後の有効容量確認</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換検査の操作コマンドに関する D M=STOR の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換検査の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換検査の操作コマンドの証跡として保存して根拠にする。</li><li>C. D M=STOR の変更点を出力本文から切り離して置換検査の操作コマンドの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換検査で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠では D M=STOR は「D M=STOR の状態と出力メッセージを結び付ける置換検査項目」と D A,L または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存では D M=STOR の出力行と IEE115I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明だけに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象では D M=STOR をz/OS MVS Operationsの確認記録に残し、対象名は置換検査対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索追跡の操作コマンドで D M=STOR の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D M=STOR の出力を取らず探索追跡の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索追跡の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索追跡の操作コマンドにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡の操作コマンドにおいて D M=STOR は説明欄の「探索追跡の操作コマンドに関係する定義値と表示行を照合する探索追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の操作コマンドの証跡を読む担当者は、D M=STOR の属性行と IEE115I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の操作コマンドは別カテゴリの確認を流用しており、D M=STOR の根拠にならないため探索追跡ではありません。探索追跡の操作コマンドに出る D M=STOR は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D M=STOR</strong></p><p>検証目的: 監査追跡の操作コマンドについて、D M=STOR は、MVS オペレータコマンドの D M で確認する項目です。実ストレージのオンライン量、構成、フレーム数を表示。LPAR 動的拡張後の有効容量確認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010059の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査追跡の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD M=STORを指定し、OSKB010059の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D M=STOR
CASE OSKB010059
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D M=STOR
CASE OSKB010059
SOURCE z/OS MVS Operations
D M=STORとOSKB010059が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010059を同じ出力で読み、監査追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010059
→ Enter を押す
［画面・出力］
IEE115I OSKB010059 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010059   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010059が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D M=STOR と OSKB010059 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010059 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D MMS


<section class="kb-item" id="c22-i0082"><h3>D MMS,STATUS</h3><p class="kb-meta">分類: D MMS ・ 難易度: 中級</p><p>D MMS,STATUSは、MVS Message Service の活性状況、ロード済みメッセージ翻訳ファイル、現行言語を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力検査の操作コマンドに関する D MMS,STATUS の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力検査の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力検査の操作コマンドの証跡として保存して根拠にする。</li><li>C. D MMS,STATUS の変更点を出力本文から切り離して出力検査の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、出力検査の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では D MMS,STATUS は「D MMS,STATUS の状態と出力メッセージを結び付ける出力検査項目」と D A,L または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では D MMS,STATUS の出力行と IEE115I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明だけに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では D MMS,STATUS をz/OS MVS Operationsの確認記録に残し、対象名は出力検査対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切追跡の操作コマンドで D MMS,STATUS の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D MMS,STATUS の出力を取らず区切追跡の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切追跡の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切追跡の操作コマンドにおいて選択記号 B を採用し、識別名は区切追跡です。区切追跡の操作コマンドにおいて D MMS,STATUS は説明欄の「区切追跡の操作コマンドに関係する定義値と表示行を照合する区切追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の操作コマンドの証跡を読む担当者は、D MMS,STATUS の属性行と IEE115I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の操作コマンドは別カテゴリの確認を流用しており、D MMS,STATUS の根拠にならないため区切追跡ではありません。区切追跡の操作コマンドに出る D MMS,STATUS は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D MMS,STATUS</strong></p><p>検証目的: 呼出検査の操作コマンドについて、D MMS,STATUS は、MVS Message Service の活性状況、ロード済みメッセージ翻訳ファイル、現行言語を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010063の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD MMS,STATUSを指定し、OSKB010063の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D MMS,STATUS
CASE OSKB010063
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D MMS,STATUS
CASE OSKB010063
SOURCE z/OS MVS Operations
D MMS,STATUSとOSKB010063が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010063を同じ出力で読み、呼出検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010063
→ Enter を押す
［画面・出力］
IEE115I OSKB010063 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010063   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010063が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D MMS,STATUS と OSKB010063 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010063 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D MPF


<section class="kb-item" id="c22-i0083"><h3>D MPF 目的</h3><p class="kb-meta">分類: D MPF ・ 難易度: 初級</p><p>D MPF 目的は、MPFLSTxx で定義された Message Processing Facility (抑止 / 色付け / 自動化対象) の現行設定を一覧表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件検査の目的に関係する D MPF 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、条件検査の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D MPF 目的の名称と担当者名だけを残して条件検査の目的の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件検査の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件検査の目的の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では D MPF 目的 は「D MPF 目的の用途を操作コマンドの表示で確認する条件検査項目」と D A,L または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景ではz/OS MVS Operationsの D MPF 目的と IEE115I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明だけに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では D MPF 目的を MVS オペレータコマンドで扱う確認対象とし、用語名は条件検査用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文確認の目的に関係する D MPF 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D MPF 目的の名称と担当者名のみを残して構文確認の目的の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文確認の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文確認の目的の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 構文確認の目的において選択記号 A を採用し、識別名は構文確認です。構文確認の目的において D MPF 目的 は説明欄の「D MPF 目的の用途を操作コマンドの表示で確認する構文確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認の目的に関連して、z/OS MVS Operationsでは D MPF 目的の表示属性と IEE115I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認の目的は対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認の目的は別カテゴリの確認を流用しており、D MPF 目的の根拠にならないため構文確認ではありません。 D: 構文確認の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文確認ではありません。構文確認の目的で使う D MPF 目的という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D MPF 目的</strong></p><p>検証目的: 置換検査の目的について、D MPF 目的は、MPFLSTxx で定義された Message Processing Facility (抑止 / 色付け / 自動化対象) の現行設定を一覧表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010064の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換検査の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD MPF 目的を指定し、OSKB010064の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D MPF 目的
CASE OSKB010064
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D MPF 目的
CASE OSKB010064
SOURCE z/OS MVS Operations
D MPF 目的とOSKB010064が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010064を同じ出力で読み、置換検査の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010064
→ Enter を押す
［画面・出力］
IEE115I OSKB010064 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010064   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010064が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D MPF 目的 と OSKB010064 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010064 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0084"><h3>D MPF,CMD コマンド除外</h3><p class="kb-meta">分類: D MPF ・ 難易度: 中級</p><p>D MPF,CMD コマンド除外は、MVS オペレータコマンドのD MPFで確認する項目です。コマンド・インストレーション抑止 (CMD 句) の現行リストを表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲検査のコマンド除外で操作コマンドの運用確認を行います。D MPF 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲検査のコマンド除外を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲検査のコマンド除外を正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、範囲検査の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D MPF 命令の属性行を読まず範囲検査のコマンド除外の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では D MPF 命令 は「z/OS MVS Operationsで D MPF 命令の扱いを記録する範囲検査項目」と D A,L または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では D MPF 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明だけに寄り、判定名は範囲検査不足です。範囲検査資料では D MPF 命令の使い方を出典欄から追跡し、資料名は範囲検査資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出確認のコマンド除外で操作コマンドの運用確認を行います。D MPF,CMD コマンド除外の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出確認のコマンド除外を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出確認のコマンド除外を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D MPF,CMD コマンド除外の属性行を読まず呼出確認のコマンド除外の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出確認のコマンド除外において選択記号 C を採用し、識別名は呼出確認です。呼出確認のコマンド除外において D MPF,CMD コマンド除外 は説明欄の「z/OS MVS Operationsで D MPF,CMD コマンド除外の扱いを記録する呼出確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認のコマンド除外を受け取る担当者は、D MPF,CMD コマンド除外の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認のコマンド除外は別カテゴリの確認を流用しており、D MPF,CMD コマンド除外の根拠にならないため呼出確認ではありません。 B: 呼出確認のコマンド除外は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認のコマンド除外は対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認のコマンド除外は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認のコマンド除外が示す D MPF,CMD コマンド除外は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D MPF,CMD コマンド除外</strong></p><p>検証目的: 探索検査のコマンド除外について、D MPF,CMD コマンド除外は、MVS オペレータコマンドの D MPF で確認する項目です。コマンド・インストレーション抑止 (CMD 句) の現行リストを表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010066の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、探索検査のコマンド除外の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD MPF,CMD コマンド除外を指定し、OSKB010066の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D MPF,CMD コマンド除外
CASE OSKB010066
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D MPF,CMD コマンド除外
CASE OSKB010066
SOURCE z/OS MVS Operations
D MPF,CMD コマンド除外とOSKB010066が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010066を同じ出力で読み、探索検査のコマンド除外の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010066
→ Enter を押す
［画面・出力］
IEE115I OSKB010066 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010066   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010066が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D MPF,CMD コマンド除外 と OSKB010066 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010066 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0085"><h3>D MPF,MSGID=id</h3><p class="kb-meta">分類: D MPF ・ 難易度: 中級</p><p>D MPF,MSGID=idは、指定メッセージ ID に対する MPF 規則 (SUP, AUTO, USEREXIT, RETAIN) のみを抽出表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切検査の操作コマンドで D MPF,MSGID=idの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D MPF,MSGID=idの出力を取らず区切検査の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて区切検査の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切検査の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切検査の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では D MPF,MSGID=id は「区切検査の操作コマンドに関係する定義値と表示行を照合する区切検査項目」と D A,L または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では D MPF,MSGID=idの属性行と IEE115I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明だけに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では D MPF,MSGID=idを MVS オペレータコマンドの運用手順で確認し、初出名は区切検査初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開確認の操作コマンドで D MPF,MSGID=idの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D MPF,MSGID=idの出力を取らず展開確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開確認の操作コマンドにおいて選択記号 B を採用し、識別名は展開確認です。展開確認の操作コマンドにおいて D MPF,MSGID=id は説明欄の「展開確認の操作コマンドに関係する定義値と表示行を照合する展開確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認の操作コマンドの証跡を読む担当者は、D MPF,MSGID=idの属性行と IEE115I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開確認ではありません。 D: 展開確認の操作コマンドは別カテゴリの確認を流用しており、D MPF,MSGID=idの根拠にならないため展開確認ではありません。展開確認の操作コマンドに出る D MPF,MSGID=idは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D MPF,MSGID=id</strong></p><p>検証目的: 終端検査の操作コマンドについて、D MPF,MSGID=idは、指定メッセージ ID に対する MPF 規則 (SUP, AUTO, USEREXIT, RETAIN) のみを抽出表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010065の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD MPF,MSGID=idを指定し、OSKB010065の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D MPF,MSGID=id
CASE OSKB010065
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D MPF,MSGID=id
CASE OSKB010065
SOURCE z/OS MVS Operations
D MPF,MSGID=idとOSKB010065が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010065を同じ出力で読み、終端検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010065
→ Enter を押す
［画面・出力］
IEE115I OSKB010065 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010065   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010065が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D MPF,MSGID=id と OSKB010065 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010065 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D NET


<section class="kb-item" id="c22-i0086"><h3>D NET,APPLS</h3><p class="kb-meta">分類: D NET ・ 難易度: 中級</p><p>D NET,APPLSは、VTAM (Communications Server) の APPL 定義と現在の状態 (ACTIV / INACT / PENDING) を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先検査の操作コマンドに関する D NET,APPLS の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先検査の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先検査の操作コマンドの証跡として保存して根拠にする。</li><li>C. D NET,APPLS の変更点を出力本文から切り離して優先検査の操作コマンドの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、優先検査の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠では D NET,APPLS は「D NET,APPLS の状態と出力メッセージを結び付ける優先検査項目」と D A,L または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存では D NET,APPLS の出力行と IEE115I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明だけに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象では D NET,APPLS をz/OS MVS Operationsの確認記録に残し、対象名は優先検査対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換確認の操作コマンドに関する D NET,APPLS の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換確認の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. D NET,APPLS の変更点を出力本文から切り離して置換確認の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換確認の操作コマンドにおいて選択記号 D を採用し、識別名は置換確認です。置換確認の操作コマンドにおいて D NET,APPLS は説明欄の「D NET,APPLS の状態と出力メッセージを結び付ける置換確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認の操作コマンドに関する記録は、D NET,APPLS の出力行と IEE115I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換確認ではありません。 B: 置換確認の操作コマンドは別カテゴリの確認を流用しており、D NET,APPLS の根拠にならないため置換確認ではありません。 C: 置換確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認の操作コマンドで記録する D NET,APPLS はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D NET,APPLS</strong></p><p>検証目的: 上書検査の操作コマンドについて、D NET,APPLS は、VTAM (Communications Server) の APPL 定義と現在の状態 (ACTIV / INACT / PENDING) を表に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010067の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD NET,APPLSを指定し、OSKB010067の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D NET,APPLS
CASE OSKB010067
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D NET,APPLS
CASE OSKB010067
SOURCE z/OS MVS Operations
D NET,APPLSとOSKB010067が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010067を同じ出力で読み、上書検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010067
→ Enter を押す
［画面・出力］
IEE115I OSKB010067 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010067   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010067が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D NET,APPLS と OSKB010067 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010067 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0087"><h3>D NET,BFRUSE バッファ</h3><p class="kb-meta">分類: D NET ・ 難易度: 中級</p><p>D NET,BFRUSE バッファは、MVS オペレータコマンドのD NETで確認する項目です。VTAM の各種バッファプール使用率を表示。性能・容量チューニング用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序検査のバッファで操作コマンドの運用確認を行います。D NET 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序検査のバッファを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序検査のバッファを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、順序検査の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D NET 命令の属性行を読まず順序検査のバッファの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では D NET 命令 は「z/OS MVS Operationsで D NET 命令の扱いを記録する順序検査項目」と D A,L または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では D NET 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明だけに寄り、判定名は順序検査不足です。順序検査資料では D NET 命令の使い方を出典欄から追跡し、資料名は順序検査資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書確認のバッファで操作コマンドの運用確認を行います。D NET,BFRUSE バッファの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書確認のバッファを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書確認のバッファを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D NET,BFRUSE バッファの属性行を読まず上書確認のバッファの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書確認のバッファにおいて選択記号 C を採用し、識別名は上書確認です。上書確認のバッファにおいて D NET,BFRUSE バッファ は説明欄の「z/OS MVS Operationsで D NET,BFRUSE バッファの扱いを記録する上書確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認のバッファを受け取る担当者は、D NET,BFRUSE バッファの表示結果と IEE115I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認のバッファは別カテゴリの確認を流用しており、D NET,BFRUSE バッファの根拠にならないため上書確認ではありません。 B: 上書確認のバッファは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書確認ではありません。 C: 上書確認のバッファは対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認のバッファは名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認のバッファが示す D NET,BFRUSE バッファは出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D NET,BFRUSE バッファ</strong></p><p>検証目的: 区切検査のバッファについて、D NET,BFRUSE バッファは、MVS オペレータコマンドの D NET で確認する項目です。VTAM の各種バッファプール使用率を表示。性能・容量チューニング用に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010070の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切検査のバッファの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD NET,BFRUSE バッファを指定し、OSKB010070の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D NET,BFRUSE バッファ
CASE OSKB010070
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D NET,BFRUSE バッファ
CASE OSKB010070
SOURCE z/OS MVS Operations
D NET,BFRUSE バッファとOSKB010070が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010070を同じ出力で読み、区切検査のバッファの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010070
→ Enter を押す
［画面・出力］
IEE115I OSKB010070 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010070   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010070が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D NET,BFRUSE バッファ と OSKB010070 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010070 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0088"><h3>D NET,ID=name</h3><p class="kb-meta">分類: D NET ・ 難易度: 中級</p><p>D NET,ID=nameは、MVS オペレータコマンドのD NETで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較検査の操作コマンドで D NET,ID=nameの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D NET,ID=nameの出力を取らず比較検査の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較検査の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較検査の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較検査の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では D NET,ID=name は「比較検査の操作コマンドに関係する定義値と表示行を照合する比較検査項目」と D A,L または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では D NET,ID=nameの属性行と IEE115I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明だけに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では D NET,ID=nameを MVS オペレータコマンドの運用手順で確認し、初出名は比較検査初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索確認の操作コマンドで D NET,ID=nameの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D NET,ID=nameの出力を取らず探索確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索確認の操作コマンドにおいて選択記号 B を採用し、識別名は探索確認です。探索確認の操作コマンドにおいて D NET,ID=name は説明欄の「探索確認の操作コマンドに関係する定義値と表示行を照合する探索確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認の操作コマンドの証跡を読む担当者は、D NET,ID=nameの属性行と IEE115I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索確認ではありません。 D: 探索確認の操作コマンドは別カテゴリの確認を流用しており、D NET,ID=nameの根拠にならないため探索確認ではありません。探索確認の操作コマンドに出る D NET,ID=nameは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D NET,ID=name</strong></p><p>検証目的: 条件検査の操作コマンドについて、D NET,ID=nameは、MVS オペレータコマンドの D NET で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010069の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD NET,ID=nameを指定し、OSKB010069の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D NET,ID=name
CASE OSKB010069
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D NET,ID=name
CASE OSKB010069
SOURCE z/OS MVS Operations
D NET,ID=nameとOSKB010069が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010069を同じ出力で読み、条件検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010069
→ Enter を押す
［画面・出力］
IEE115I OSKB010069 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010069   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010069が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D NET,ID=name と OSKB010069 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010069 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0089"><h3>D NET,MAJNODES</h3><p class="kb-meta">分類: D NET ・ 難易度: 中級</p><p>D NET,MAJNODESは、MVS オペレータコマンドのD NETで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録検査の操作コマンドに関係する D NET,MAJNODES の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、記録検査として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D NET,MAJNODES の名称と担当者名だけを残して記録検査の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録検査の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録検査の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では D NET,MAJNODES は「D NET,MAJNODES の用途を操作コマンドの表示で確認する記録検査項目」と D A,L または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景ではz/OS MVS Operationsの D NET,MAJNODES と IEE115I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明だけに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では D NET,MAJNODES を MVS オペレータコマンドで扱う確認対象とし、用語名は記録検査用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端確認の操作コマンドに関係する D NET,MAJNODES の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D NET,MAJNODES の名称と担当者名のみを残して終端確認の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端確認の操作コマンドにおいて選択記号 A を採用し、識別名は終端確認です。終端確認の操作コマンドにおいて D NET,MAJNODES は説明欄の「D NET,MAJNODES の用途を操作コマンドの表示で確認する終端確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認の操作コマンドに関連して、z/OS MVS Operationsでは D NET,MAJNODES の表示属性と IEE115I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認の操作コマンドは別カテゴリの確認を流用しており、D NET,MAJNODES の根拠にならないため終端確認ではありません。 D: 終端確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端確認ではありません。終端確認の操作コマンドで使う D NET,MAJNODES という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D NET,MAJNODES</strong></p><p>検証目的: 記録確認の操作コマンドについて、D NET,MAJNODES は、MVS オペレータコマンドの D NET で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040013の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD NET,MAJNODESを指定し、OSKB040013の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D NET,MAJNODES
CASE OSKB040013
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D NET,MAJNODES
CASE OSKB040013
SOURCE z/OS MVS Operations
D NET,MAJNODESとOSKB040013が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040013を同じ出力で読み、記録確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040013
→ Enter を押す
［画面・出力］
IEE115I OSKB040013 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040013   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040013が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D NET,MAJNODES と OSKB040013 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040013 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D NET,MAJNODES</strong></p><p>検証目的: 出力検査の操作コマンドについて、D NET,MAJNODES は、MVS オペレータコマンドの D NET で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010068の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD NET,MAJNODESを指定し、OSKB010068の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D NET,MAJNODES
CASE OSKB010068
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D NET,MAJNODES
CASE OSKB010068
SOURCE z/OS MVS Operations
D NET,MAJNODESとOSKB010068が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010068を同じ出力で読み、出力検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010068
→ Enter を押す
［画面・出力］
IEE115I OSKB010068 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010068   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010068が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D NET,MAJNODES と OSKB010068 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010068 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0090"><h3>D NET,STATIONS</h3><p class="kb-meta">分類: D NET ・ 難易度: 中級</p><p>D NET,STATIONSは、MVS オペレータコマンドのD NETで確認する項目です。VTAM 接続端末/論理ステーションの状態。SNA 端末のセッション確認</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域検査の操作コマンドに関する D NET,STATIONS の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域検査の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域検査の操作コマンドの証跡として保存して根拠にする。</li><li>C. D NET,STATIONS の変更点を出力本文から切り離して値域検査の操作コマンドの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域検査で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠では D NET,STATIONS は「D NET,STATIONS の状態と出力メッセージを結び付ける値域検査項目」と D A,L または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存では D NET,STATIONS の出力行と IEE115I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明だけに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象では D NET,STATIONS をz/OS MVS Operationsの確認記録に残し、対象名は値域検査対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力確認の操作コマンドに関する D NET,STATIONS の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力確認の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. D NET,STATIONS の変更点を出力本文から切り離して出力確認の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力確認の操作コマンドにおいて選択記号 D を採用し、識別名は出力確認です。出力確認の操作コマンドにおいて D NET,STATIONS は説明欄の「D NET,STATIONS の状態と出力メッセージを結び付ける出力確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認の操作コマンドに関する記録は、D NET,STATIONS の出力行と IEE115I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力確認ではありません。 B: 出力確認の操作コマンドは別カテゴリの確認を流用しており、D NET,STATIONS の根拠にならないため出力確認ではありません。 C: 出力確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認の操作コマンドで記録する D NET,STATIONS はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D NET,STATIONS</strong></p><p>検証目的: 範囲検査の操作コマンドについて、D NET,STATIONS は、MVS オペレータコマンドの D NET で確認する項目です。VTAM 接続端末/論理ステーションの状態。SNA 端末のセッション確認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010071の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD NET,STATIONSを指定し、OSKB010071の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D NET,STATIONS
CASE OSKB010071
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D NET,STATIONS
CASE OSKB010071
SOURCE z/OS MVS Operations
D NET,STATIONSとOSKB010071が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010071を同じ出力で読み、範囲検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010071
→ Enter を押す
［画面・出力］
IEE115I OSKB010071 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010071   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010071が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D NET,STATIONS と OSKB010071 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010071 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D OMVS


<section class="kb-item" id="c22-i0091"><h3>D OMVS,A=ALL プロセス一覧</h3><p class="kb-meta">分類: D OMVS ・ 難易度: 中級</p><p>D OMVS,A=ALL プロセス一覧は、MVS オペレータコマンドのD OMVSで確認する項目です。全 z/OS UNIX プロセスの PID / PPID / STATE / コマンド名を表示。プロセス調査の中心コマンド</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査検査のプロセス一覧で操作コマンドの運用確認を行います。D OMVS 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査検査のプロセス一覧を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査検査のプロセス一覧を正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を監査検査で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D OMVS 命令の属性行を読まず監査検査のプロセス一覧の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では D OMVS 命令 は「z/OS MVS Operationsで D OMVS 命令の扱いを記録する監査検査項目」と D A,L または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では D OMVS 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明だけに寄り、判定名は監査検査不足です。監査検査資料では D OMVS 命令の使い方を出典欄から追跡し、資料名は監査検査資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 範囲確認のプロセス一覧で操作コマンドの運用確認を行います。D OMVS,A=ALL プロセス一覧の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲確認のプロセス一覧を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲確認のプロセス一覧を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D OMVS,A=ALL プロセス一覧の属性行を読まず範囲確認のプロセス一覧の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲確認のプロセス一覧において選択記号 C を採用し、識別名は範囲確認です。範囲確認のプロセス一覧において D OMVS,A=ALL プロセス一覧 は説明欄の「z/OS MVS Operationsで D OMVS,A=ALL プロセス一覧の扱いを記録する範囲確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲確認です。範囲確認のプロセス一覧を受け取る担当者は、D OMVS,A=ALL プロセス一覧の表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲確認です。不適切な選択肢を整理します。 A: 範囲確認のプロセス一覧は別カテゴリの確認を流用しており、D OMVS,A=ALL プロセス一覧の根拠にならないため範囲確認ではありません。 B: 範囲確認のプロセス一覧は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲確認ではありません。 C: 範囲確認のプロセス一覧は対象出力と項目説明を結び、根拠を残すので範囲確認です。 D: 範囲確認のプロセス一覧は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲確認ではありません。範囲確認のプロセス一覧が示す D OMVS,A=ALL プロセス一覧は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D OMVS,A=ALL プロセス一覧</strong></p><p>検証目的: 比較確認のプロセス一覧について、D OMVS,A=ALL プロセス一覧は、MVS オペレータコマンドの D OMVS で確認する項目です。全 z/OS UNIX プロセスの PID / PPID / STATに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040014の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較確認のプロセス一覧の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OMVS,A=ALL プロセス一を指定し、OSKB040014の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OMVS,A=ALL プロセス一
CASE OSKB040014
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OMVS,A=ALL プロセス一
CASE OSKB040014
SOURCE z/OS MVS Operations
D OMVS,A=ALL プロセス一とOSKB040014が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040014を同じ出力で読み、比較確認のプロセス一覧の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040014
→ Enter を押す
［画面・出力］
IEE115I OSKB040014 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040014   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040014が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OMVS,A=ALL プロセス一 と OSKB040014 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040014 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D OMVS,A=ALL プロセス一覧</strong></p><p>検証目的: 比較検査のプロセス一覧について、D OMVS,A=ALL プロセス一覧は、MVS オペレータコマンドの D OMVS で確認する項目です。全 z/OS UNIX プロセスの PID / PPID / STATに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010074の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較検査のプロセス一覧の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OMVS,A=ALL プロセス一を指定し、OSKB010074の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OMVS,A=ALL プロセス一
CASE OSKB010074
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OMVS,A=ALL プロセス一
CASE OSKB010074
SOURCE z/OS MVS Operations
D OMVS,A=ALL プロセス一とOSKB010074が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010074を同じ出力で読み、比較検査のプロセス一覧の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010074
→ Enter を押す
［画面・出力］
IEE115I OSKB010074 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010074   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010074が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OMVS,A=ALL プロセス一 と OSKB010074 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010074 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0092"><h3>D OMVS,B (BPXPRMxx)</h3><p class="kb-meta">分類: D OMVS ・ 難易度: 中級</p><p>D OMVS,B (BPXPRMxx)は、MVS オペレータコマンドのD OMVSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧検査の操作コマンドで D OMVS,B 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D OMVS,B 属性の出力を取らず復旧検査の操作コマンドの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて復旧検査の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧検査の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧検査の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では D OMVS,B 属性 は「復旧検査の操作コマンドに関係する定義値と表示行を照合する復旧検査項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では D OMVS,B 属性の属性行と IEE115I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明だけに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では D OMVS,B 属性を MVS オペレータコマンドの運用手順で確認し、初出名は復旧検査初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切確認の操作コマンドで D OMVS,B (BPXPRMxx)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D OMVS,B (BPXPRMxx)の出力を取らず区切確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切確認の操作コマンドにおいて選択記号 B を採用し、識別名は区切確認です。区切確認の操作コマンドにおいて D OMVS,B (BPXPRMxx) は説明欄の「区切確認の操作コマンドに関係する定義値と表示行を照合する区切確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認の操作コマンドの証跡を読む担当者は、D OMVS,B (BPXPRMxx)の属性行と IEE115I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切確認ではありません。 D: 区切確認の操作コマンドは別カテゴリの確認を流用しており、D OMVS,B (BPXPRMxx)の根拠にならないため区切確認ではありません。区切確認の操作コマンドに出る D OMVS,B (BPXPRMxx)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D OMVS,B (BPXPRMxx)</strong></p><p>検証目的: 記録検査の操作コマンドについて、D OMVS,B (BPXPRMxx)は、MVS オペレータコマンドの D OMVS で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読みに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010073の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OMVS,B (BPXPRMxxを指定し、OSKB010073の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OMVS,B (BPXPRMxx
CASE OSKB010073
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OMVS,B (BPXPRMxx
CASE OSKB010073
SOURCE z/OS MVS Operations
D OMVS,B (BPXPRMxxとOSKB010073が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010073を同じ出力で読み、記録検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010073
→ Enter を押す
［画面・出力］
IEE115I OSKB010073 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010073   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010073が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OMVS,B (BPXPRMxx と OSKB010073 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010073 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0093"><h3>D OMVS,F ファイルシステム</h3><p class="kb-meta">分類: D OMVS ・ 難易度: 中級</p><p>D OMVS,F ファイルシステムは、現在マウント中の HFS / zFS / NFS と MODE (RDWR/READ)、QUIESCE 状態を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更検査のファイルシステムに関する D OMVS 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更検査のファイルシステムの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更検査のファイルシステムの証跡として保存して根拠にする。</li><li>C. D OMVS 命令の変更点を出力本文から切り離して変更検査のファイルシステムの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、変更検査の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では D OMVS 命令 は「D OMVS 命令の状態と出力メッセージを結び付ける変更検査項目」と D A,L または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では D OMVS 命令の出力行と IEE115I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明だけに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では D OMVS 命令をz/OS MVS Operationsの確認記録に残し、対象名は変更検査対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 優先確認のファイルシステムに関する D OMVS,F ファイルシステムの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先確認のファイルシステムの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先確認のファイルシステムの証跡として保存して根拠にする。</li><li>C. D OMVS,F ファイルシステムの変更点を出力本文から切り離して優先確認のファイルシステムの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先確認のファイルシステムにおいて選択記号 D を採用し、識別名は優先確認です。優先確認のファイルシステムにおいて D OMVS,F ファイルシステム は説明欄の「D OMVS,F ファイルシステムの状態と出力メッセージを結び付ける優先確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認のファイルシステムに関する記録は、D OMVS,F ファイルシステムの出力行と IEE115I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認のファイルシステムは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先確認ではありません。 B: 優先確認のファイルシステムは別カテゴリの確認を流用しており、D OMVS,F ファイルシステムの根拠にならないため優先確認ではありません。 C: 優先確認のファイルシステムは名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認のファイルシステムは対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認のファイルシステムで記録する D OMVS,F ファイルシステムはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D OMVS,F ファイルシステム</strong></p><p>検証目的: 順序検査のファイルシステムについて、D OMVS,F ファイルシステムは、現在マウント中の HFS / zFS / NFS と MODE (RDWR/READ)、QUIESCE 状態を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010075の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序検査のファイルシステムの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OMVS,F ファイルシステムを指定し、OSKB010075の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OMVS,F ファイルシステム
CASE OSKB010075
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OMVS,F ファイルシステム
CASE OSKB010075
SOURCE z/OS MVS Operations
D OMVS,F ファイルシステムとOSKB010075が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010075を同じ出力で読み、順序検査のファイルシステムの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010075
→ Enter を押す
［画面・出力］
IEE115I OSKB010075 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010075   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010075が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OMVS,F ファイルシステム と OSKB010075 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010075 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0094"><h3>D OMVS,L 制限値と使用率</h3><p class="kb-meta">分類: D OMVS ・ 難易度: 中級</p><p>D OMVS,L 制限値と使用率は、MVS オペレータコマンドのD OMVSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文判定の制限値と使用率に関係する D OMVS 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、構文判定の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D OMVS 命令の名称と担当者名だけを残して構文判定の制限値と使用率の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文判定の制限値と使用率を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文判定の制限値と使用率の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では D OMVS 命令 は「D OMVS 命令の用途を操作コマンドの表示で確認する構文判定項目」と D A,L または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景ではz/OS MVS Operationsの D OMVS 命令と IEE115I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明だけに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では D OMVS 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は構文判定用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 記録確認の制限値と使用率に関係する D OMVS,L 制限値と使用率の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、記録確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D OMVS,L 制限値と使用率の名称と担当者名のみを残して記録確認の制限値と使用率の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で記録確認の制限値と使用率を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録確認の制限値と使用率の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録確認の制限値と使用率において選択記号 A を採用し、識別名は記録確認です。記録確認の制限値と使用率において D OMVS,L 制限値と使用率 は説明欄の「D OMVS,L 制限値と使用率の用途を操作コマンドの表示で確認する記録確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認の制限値と使用率に関連して、z/OS MVS Operationsでは D OMVS,L 制限値と使用率の表示属性と IEE115I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認の制限値と使用率は対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認の制限値と使用率は名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認の制限値と使用率は別カテゴリの確認を流用しており、D OMVS,L 制限値と使用率の根拠にならないため記録確認ではありません。 D: 記録確認の制限値と使用率は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録確認ではありません。記録確認の制限値と使用率で使う D OMVS,L 制限値と使用率という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D OMVS,L 制限値と使用率</strong></p><p>検証目的: 値域検査の制限値と使用率について、D OMVS,L 制限値と使用率は、MVS オペレータコマンドの D OMVS で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010076の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域検査の制限値と使用率の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OMVS,L 制限値と使用率を指定し、OSKB010076の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OMVS,L 制限値と使用率
CASE OSKB010076
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OMVS,L 制限値と使用率
CASE OSKB010076
SOURCE z/OS MVS Operations
D OMVS,L 制限値と使用率とOSKB010076が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010076を同じ出力で読み、値域検査の制限値と使用率の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010076
→ Enter を押す
［画面・出力］
IEE115I OSKB010076 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010076   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010076が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OMVS,L 制限値と使用率 と OSKB010076 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010076 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0095"><h3>D OMVS,O オプション</h3><p class="kb-meta">分類: D OMVS ・ 難易度: 中級</p><p>D OMVS,O オプションは、BPXPRMxx の現行有効値 (MAXPROCSYS, MAXFILEPROC, IPCMSGQBYTES 等) を一覧表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告検査のオプションに関係する D OMVS,O オプションの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、警告検査の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D OMVS,O オプションの名称と担当者名だけを残して警告検査のオプションの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告検査のオプションを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告検査のオプションの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では D OMVS,O オプション は「D OMVS,O オプションの用途を操作コマンドの表示で確認する警告検査項目」と D A,L または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景ではz/OS MVS Operationsの D OMVS,O オプションと IEE115I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明だけに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では D OMVS,O オプションを MVS オペレータコマンドで扱う確認対象とし、用語名は警告検査用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件確認のオプションに関係する D OMVS,O オプションの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D OMVS,O オプションの名称と担当者名のみを残して条件確認のオプションの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件確認のオプションを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件確認のオプションの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件確認のオプションにおいて選択記号 A を採用し、識別名は条件確認です。条件確認のオプションにおいて D OMVS,O オプション は説明欄の「D OMVS,O オプションの用途を操作コマンドの表示で確認する条件確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認のオプションに関連して、z/OS MVS Operationsでは D OMVS,O オプションの表示属性と IEE115I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認のオプションは対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認のオプションは名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認のオプションは別カテゴリの確認を流用しており、D OMVS,O オプションの根拠にならないため条件確認ではありません。 D: 条件確認のオプションは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件確認ではありません。条件確認のオプションで使う D OMVS,O オプションという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D OMVS,O オプション</strong></p><p>検証目的: 優先検査のオプションについて、D OMVS,O オプションは、BPXPRMxx の現行有効値 (MAXPROCSYS, MAXFILEPROC, IPCMSGQBYTES 等) を一覧表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010072の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先検査のオプションの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OMVS,O オプションを指定し、OSKB010072の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OMVS,O オプション
CASE OSKB010072
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OMVS,O オプション
CASE OSKB010072
SOURCE z/OS MVS Operations
D OMVS,O オプションとOSKB010072が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010072を同じ出力で読み、優先検査のオプションの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010072
→ Enter を押す
［画面・出力］
IEE115I OSKB010072 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010072   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010072が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OMVS,O オプション と OSKB010072 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010072 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0096"><h3>D OMVS,SERVER サーバ</h3><p class="kb-meta">分類: D OMVS ・ 難易度: 中級</p><p>D OMVS,SERVER サーバは、MVS オペレータコマンドのD OMVSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換判定のサーバに関する D OMVS 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換判定のサーバの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換判定のサーバの証跡として保存して根拠にする。</li><li>C. D OMVS 命令の変更点を出力本文から切り離して置換判定のサーバの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、置換判定の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では D OMVS 命令 は「D OMVS 命令の状態と出力メッセージを結び付ける置換判定項目」と D A,L または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では D OMVS 命令の出力行と IEE115I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明だけに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では D OMVS 命令をz/OS MVS Operationsの確認記録に残し、対象名は置換判定対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 値域確認のサーバに関する D OMVS,SERVER サーバの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域確認のサーバの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域確認のサーバの証跡として保存して根拠にする。</li><li>C. D OMVS,SERVER サーバの変更点を出力本文から切り離して値域確認のサーバの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、値域確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域確認のサーバにおいて選択記号 D を採用し、識別名は値域確認です。値域確認のサーバにおいて D OMVS,SERVER サーバ は説明欄の「D OMVS,SERVER サーバの状態と出力メッセージを結び付ける値域確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認のサーバに関する記録は、D OMVS,SERVER サーバの出力行と IEE115I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認のサーバは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域確認ではありません。 B: 値域確認のサーバは別カテゴリの確認を流用しており、D OMVS,SERVER サーバの根拠にならないため値域確認ではありません。 C: 値域確認のサーバは名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認のサーバは対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認のサーバで記録する D OMVS,SERVER サーバはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D OMVS,SERVER サーバ</strong></p><p>検証目的: 監査検査のサーバについて、D OMVS,SERVER サーバは、MVS オペレータコマンドの D OMVS で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010079の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査検査のサーバの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OMVS,SERVER サーバを指定し、OSKB010079の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OMVS,SERVER サーバ
CASE OSKB010079
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OMVS,SERVER サーバ
CASE OSKB010079
SOURCE z/OS MVS Operations
D OMVS,SERVER サーバとOSKB010079が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010079を同じ出力で読み、監査検査のサーバの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010079
→ Enter を押す
［画面・出力］
IEE115I OSKB010079 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010079   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010079が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OMVS,SERVER サーバ と OSKB010079 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010079 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0097"><h3>D OMVS,SOCKETS</h3><p class="kb-meta">分類: D OMVS ・ 難易度: 中級</p><p>D OMVS,SOCKETSは、AF_INET / AF_UNIX ソケットの使用状況とファイル記述子上限の使用率を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出判定の操作コマンドで操作コマンドの運用確認を行います。D OMVS,SOCKETS の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出判定の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出判定の操作コマンドを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、呼出判定の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D OMVS,SOCKETS の属性行を読まず呼出判定の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では D OMVS,SOCKETS は「z/OS MVS Operationsで D OMVS,SOCKETS の扱いを記録する呼出判定項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では D OMVS,SOCKETS の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明だけに寄り、判定名は呼出判定不足です。呼出判定資料では D OMVS,SOCKETS の使い方を出典欄から追跡し、資料名は呼出判定資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 順序確認の操作コマンドで操作コマンドの運用確認を行います。D OMVS,SOCKETS の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序確認の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序確認の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、順序確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D OMVS,SOCKETS の属性行を読まず順序確認の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序確認の操作コマンドにおいて選択記号 C を採用し、識別名は順序確認です。順序確認の操作コマンドにおいて D OMVS,SOCKETS は説明欄の「z/OS MVS Operationsで D OMVS,SOCKETS の扱いを記録する順序確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認の操作コマンドを受け取る担当者は、D OMVS,SOCKETS の表示結果と IEE115I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認の操作コマンドは別カテゴリの確認を流用しており、D OMVS,SOCKETS の根拠にならないため順序確認ではありません。 B: 順序確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため順序確認ではありません。 C: 順序確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認の操作コマンドが示す D OMVS,SOCKETS は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D OMVS,SOCKETS</strong></p><p>検証目的: 復旧検査の操作コマンドについて、D OMVS,SOCKETS は、AF_INET / AF_UNIX ソケットの使用状況とファイル記述子上限の使用率を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010078の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OMVS,SOCKETSを指定し、OSKB010078の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OMVS,SOCKETS
CASE OSKB010078
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OMVS,SOCKETS
CASE OSKB010078
SOURCE z/OS MVS Operations
D OMVS,SOCKETSとOSKB010078が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010078を同じ出力で読み、復旧検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010078
→ Enter を押す
［画面・出力］
IEE115I OSKB010078 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010078   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010078が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OMVS,SOCKETS と OSKB010078 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010078 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0098"><h3>D OMVS,U=user</h3><p class="kb-meta">分類: D OMVS ・ 難易度: 中級</p><p>D OMVS,U=userは、MVS オペレータコマンドのD OMVSで用いる指定ユーザ ID の z/OS UNIX 上の活動プロセス・スレッドのみを表示。D OMVSでは、指定値と対象資源、実行時の出力を突き合わせて確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開判定の操作コマンドで D OMVS,U=userの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D OMVS,U=userの出力を取らず展開判定の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて展開判定の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開判定の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開判定の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では D OMVS,U=user は「展開判定の操作コマンドに関係する定義値と表示行を照合する展開判定項目」と D A,L または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では D OMVS,U=userの属性行と IEE115I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明だけに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では D OMVS,U=userを MVS オペレータコマンドの運用手順で確認し、初出名は展開判定初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 比較確認の操作コマンドで D OMVS,U=userの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D OMVS,U=userの出力を取らず比較確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、比較確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較確認の操作コマンドにおいて選択記号 B を採用し、識別名は比較確認です。比較確認の操作コマンドにおいて D OMVS,U=user は説明欄の「比較確認の操作コマンドに関係する定義値と表示行を照合する比較確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較確認です。比較確認の操作コマンドの証跡を読む担当者は、D OMVS,U=userの属性行と IEE115I を合わせて追跡し、背景名は比較確認です。誤答側の問題点を分けます。 A: 比較確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較確認ではありません。 B: 比較確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較確認です。 C: 比較確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較確認ではありません。 D: 比較確認の操作コマンドは別カテゴリの確認を流用しており、D OMVS,U=userの根拠にならないため比較確認ではありません。比較確認の操作コマンドに出る D OMVS,U=userは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D OMVS,U=user</strong></p><p>検証目的: 警告検査の操作コマンドについて、D OMVS,U=userは、MVS オペレータコマンドの D OMVS で用いる指定ユーザ ID の z/OS UNIX 上の活動プロセス・スレッドのみを表示。D OMVS でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010077の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告検査の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OMVS,U=userを指定し、OSKB010077の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OMVS,U=user
CASE OSKB010077
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OMVS,U=user
CASE OSKB010077
SOURCE z/OS MVS Operations
D OMVS,U=userとOSKB010077が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010077を同じ出力で読み、警告検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010077
→ Enter を押す
［画面・出力］
IEE115I OSKB010077 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010077   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010077が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OMVS,U=user と OSKB010077 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010077 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0099"><h3>D OMVS,W=A 待ち状態</h3><p class="kb-meta">分類: D OMVS ・ 難易度: 中級</p><p>D OMVS,W=A 待ち状態は、BLOCKED / WAITING プロセスを抽出し、何で待っているかを表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端判定の待ち状態に関係する D OMVS,W=A 待ち状態の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、終端判定として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D OMVS,W=A 待ち状態の名称と担当者名だけを残して終端判定の待ち状態の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端判定の待ち状態を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端判定の待ち状態の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠では D OMVS,W=A 待ち状態 は「D OMVS,W=A 待ち状態の用途を操作コマンドの表示で確認する終端判定項目」と D A,L または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景ではz/OS MVS Operationsの D OMVS,W=A 待ち状態と IEE115I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明だけに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語では D OMVS,W=A 待ち状態を MVS オペレータコマンドで扱う確認対象とし、用語名は終端判定用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 警告確認の待ち状態に関係する D OMVS,W=A 待ち状態の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、警告確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D OMVS,W=A 待ち状態の名称と担当者名のみを残して警告確認の待ち状態の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で警告確認の待ち状態を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告確認の待ち状態の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告確認の待ち状態において選択記号 A を採用し、識別名は警告確認です。警告確認の待ち状態において D OMVS,W=A 待ち状態 は説明欄の「D OMVS,W=A 待ち状態の用途を操作コマンドの表示で確認する警告確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認の待ち状態に関連して、z/OS MVS Operationsでは D OMVS,W=A 待ち状態の表示属性と IEE115I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認の待ち状態は対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認の待ち状態は名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認の待ち状態は別カテゴリの確認を流用しており、D OMVS,W=A 待ち状態の根拠にならないため警告確認ではありません。 D: 警告確認の待ち状態は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告確認ではありません。警告確認の待ち状態で使う D OMVS,W=A 待ち状態という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D OMVS,W=A 待ち状態</strong></p><p>検証目的: 順序確認の待ち状態について、D OMVS,W=A 待ち状態は、BLOCKED / WAITING プロセスを抽出し、何で待っているかを表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040015の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序確認の待ち状態の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OMVS,W=A 待ち状態を指定し、OSKB040015の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OMVS,W=A 待ち状態
CASE OSKB040015
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OMVS,W=A 待ち状態
CASE OSKB040015
SOURCE z/OS MVS Operations
D OMVS,W=A 待ち状態とOSKB040015が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040015を同じ出力で読み、順序確認の待ち状態の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040015
→ Enter を押す
［画面・出力］
IEE115I OSKB040015 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040015   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040015が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OMVS,W=A 待ち状態 と OSKB040015 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040015 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D OMVS,W=A 待ち状態</strong></p><p>検証目的: 変更検査の待ち状態について、D OMVS,W=A 待ち状態は、BLOCKED / WAITING プロセスを抽出し、何で待っているかを表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010080の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更検査の待ち状態の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OMVS,W=A 待ち状態を指定し、OSKB010080の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OMVS,W=A 待ち状態
CASE OSKB010080
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OMVS,W=A 待ち状態
CASE OSKB010080
SOURCE z/OS MVS Operations
D OMVS,W=A 待ち状態とOSKB010080が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010080を同じ出力で読み、変更検査の待ち状態の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010080
→ Enter を押す
［画面・出力］
IEE115I OSKB010080 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010080   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010080が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OMVS,W=A 待ち状態 と OSKB010080 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010080 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D OPDATA


<section class="kb-item" id="c22-i0100"><h3>D OPDATA,INSTALL</h3><p class="kb-meta">分類: D OPDATA ・ 難易度: 中級</p><p>D OPDATA,INSTALLは、MPF / CMDS / RTLS 等インストレーション系オペレータ・データの全体構成を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書判定の操作コマンドで操作コマンドの運用確認を行います。D OPDATA 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書判定の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書判定の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、上書判定の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D OPDATA 命令の属性行を読まず上書判定の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では D OPDATA 命令 は「z/OS MVS Operationsで D OPDATA 命令の扱いを記録する上書判定項目」と D A,L または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では D OPDATA 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明だけに寄り、判定名は上書判定不足です。上書判定資料では D OPDATA 命令の使い方を出典欄から追跡し、資料名は上書判定資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 監査確認の操作コマンドで操作コマンドの運用確認を行います。D OPDATA,INSTALL の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査確認の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査確認の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、監査確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D OPDATA,INSTALL の属性行を読まず監査確認の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査確認の操作コマンドにおいて選択記号 C を採用し、識別名は監査確認です。監査確認の操作コマンドにおいて D OPDATA,INSTALL は説明欄の「z/OS MVS Operationsで D OPDATA,INSTALL の扱いを記録する監査確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認の操作コマンドを受け取る担当者は、D OPDATA,INSTALL の表示結果と IEE115I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認の操作コマンドは別カテゴリの確認を流用しており、D OPDATA,INSTALL の根拠にならないため監査確認ではありません。 B: 監査確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査確認ではありません。 C: 監査確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認の操作コマンドが示す D OPDATA,INSTALL は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D OPDATA,INSTALL</strong></p><p>検証目的: 展開判定の操作コマンドについて、D OPDATA,INSTALL は、MPF / CMDS / RTLS 等インストレーション系オペレータ・データの全体構成を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010082の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開判定の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OPDATA,INSTALLを指定し、OSKB010082の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OPDATA,INSTALL
CASE OSKB010082
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OPDATA,INSTALL
CASE OSKB010082
SOURCE z/OS MVS Operations
D OPDATA,INSTALLとOSKB010082が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010082を同じ出力で読み、展開判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010082
→ Enter を押す
［画面・出力］
IEE115I OSKB010082 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010082   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010082が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OPDATA,INSTALL と OSKB010082 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010082 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0101"><h3>D OPDATA,MSG メッセージ抑止</h3><p class="kb-meta">分類: D OPDATA ・ 難易度: 中級</p><p>D OPDATA,MSG メッセージ抑止は、オペレータ・データ (CMDS, MSGID 自動化, COLOR) の現行設定を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索判定のメッセージ抑止で D OPDATA 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA 命令の出力を取らず探索判定のメッセージ抑止の説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索判定の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索判定のメッセージ抑止の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索判定のメッセージ抑止へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では D OPDATA 命令 は「探索判定のメッセージ抑止に関係する定義値と表示行を照合する探索判定項目」と D A,L または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では D OPDATA 命令の属性行と IEE115I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明だけに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では D OPDATA 命令を MVS オペレータコマンドの運用手順で確認し、初出名は探索判定初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 復旧確認のメッセージ抑止で D OPDATA,MSG メッセージ抑止の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA,MSG メッセージ抑止の出力を取らず復旧確認のメッセージ抑止の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、復旧確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧確認のメッセージ抑止の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧確認のメッセージ抑止へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧確認のメッセージ抑止において選択記号 B を採用し、識別名は復旧確認です。復旧確認のメッセージ抑止において D OPDATA,MSG メッセージ抑止 は説明欄の「復旧確認のメッセージ抑止に関係する定義値と表示行を照合する復旧確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認のメッセージ抑止の証跡を読む担当者は、D OPDATA,MSG メッセージ抑止の属性行と IEE115I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認のメッセージ抑止は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認のメッセージ抑止は対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認のメッセージ抑止は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認のメッセージ抑止は別カテゴリの確認を流用しており、D OPDATA,MSG メッセージ抑止の根拠にならないため復旧確認ではありません。復旧確認のメッセージ抑止に出る D OPDATA,MSG メッセージ抑止は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D OPDATA,MSG メッセージ抑止</strong></p><p>検証目的: 構文判定のメッセージ抑止について、D OPDATA,MSG メッセージ抑止は、オペレータ・データ (CMDS, MSGID 自動化, COLOR) の現行設定を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010081の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文判定のメッセージ抑止の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD OPDATA,MSG メッセージを指定し、OSKB010081の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D OPDATA,MSG メッセージ
CASE OSKB010081
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D OPDATA,MSG メッセージ
CASE OSKB010081
SOURCE z/OS MVS Operations
D OPDATA,MSG メッセージとOSKB010081が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010081を同じ出力で読み、構文判定のメッセージ抑止の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010081
→ Enter を押す
［画面・出力］
IEE115I OSKB010081 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010081   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010081が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D OPDATA,MSG メッセージ と OSKB010081 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010081 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D PARMLIB


<section class="kb-item" id="c22-i0102"><h3>D PARMLIB 目的</h3><p class="kb-meta">分類: D PARMLIB ・ 難易度: 初級</p><p>現行で連結されている PARMLIB データセット (LOGICAL PARMLIB) のチェーンを表示。LOAD パラメータ・PARMLIB ADD で動的に追加した DS の確認に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力判定の目的に関する D PARMLIB 目的の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力判定の目的の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力判定の目的の証跡として保存して根拠にする。</li><li>C. D PARMLIB 目的の変更点を出力本文から切り離して出力判定の目的の承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力判定で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では D PARMLIB 目的 は「D PARMLIB 目的の状態と出力メッセージを結び付ける出力判定項目」と D A,L または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では D PARMLIB 目的の出力行と IEE115I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明だけに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では D PARMLIB 目的をz/OS MVS Operationsの確認記録に残し、対象名は出力判定対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 変更確認の目的に関する D PARMLIB 目的の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更確認の目的の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更確認の目的の証跡として保存して根拠にする。</li><li>C. D PARMLIB 目的の変更点を出力本文から切り離して変更確認の目的の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、変更確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 変更確認の目的において選択記号 D を採用し、識別名は変更確認です。変更確認の目的において D PARMLIB 目的 は説明欄の「D PARMLIB 目的の状態と出力メッセージを結び付ける変更確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認の目的に関する記録は、D PARMLIB 目的の出力行と IEE115I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更確認ではありません。 B: 変更確認の目的は別カテゴリの確認を流用しており、D PARMLIB 目的の根拠にならないため変更確認ではありません。 C: 変更確認の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認の目的は対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認の目的で記録する D PARMLIB 目的はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PARMLIB 目的</strong></p><p>検証目的: 呼出判定の目的について、現行で連結されている PARMLIB データセット (LOGICAL PARMLIB) のチェーンを表示。LOAD パラメータ・ PARMLIB ADD で動的に追加した Dに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010083の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出判定の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PARMLIB 目的を指定し、OSKB010083の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PARMLIB 目的
CASE OSKB010083
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PARMLIB 目的
CASE OSKB010083
SOURCE z/OS MVS Operations
D PARMLIB 目的とOSKB010083が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010083を同じ出力で読み、呼出判定の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010083
→ Enter を押す
［画面・出力］
IEE115I OSKB010083 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010083   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010083が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PARMLIB 目的 と OSKB010083 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010083 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D PCIE


<section class="kb-item" id="c22-i0103"><h3>D PCIE 目的</h3><p class="kb-meta">分類: D PCIE ・ 難易度: 初級</p><p>D PCIE 目的は、PCIe Express 機能 (RoCE, zEDC, etc.) のオンライン/オフライン状態と機能 ID を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件判定の目的に関係する D PCIE 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、条件判定の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D PCIE 目的の名称と担当者名だけを残して条件判定の目的の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件判定の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件判定の目的の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では D PCIE 目的 は「D PCIE 目的の用途を操作コマンドの表示で確認する条件判定項目」と D A,L または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景ではz/OS MVS Operationsの D PCIE 目的と IEE115I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明だけに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では D PCIE 目的を MVS オペレータコマンドで扱う確認対象とし、用語名は条件判定用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文照合の目的に関係する D PCIE 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D PCIE 目的の名称と担当者名のみを残して構文照合の目的の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文照合の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文照合の目的の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 構文照合の目的において選択記号 A を採用し、識別名は構文照合です。構文照合の目的において D PCIE 目的 は説明欄の「D PCIE 目的の用途を操作コマンドの表示で確認する構文照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合の目的に関連して、z/OS MVS Operationsでは D PCIE 目的の表示属性と IEE115I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合の目的は対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合の目的は別カテゴリの確認を流用しており、D PCIE 目的の根拠にならないため構文照合ではありません。 D: 構文照合の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文照合ではありません。構文照合の目的で使う D PCIE 目的という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PCIE 目的</strong></p><p>検証目的: 置換判定の目的について、D PCIE 目的は、PCIe Express 機能 (RoCE, zEDC, etc.) のオンライン/オフライン状態と機能 ID を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010084の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換判定の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PCIE 目的を指定し、OSKB010084の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PCIE 目的
CASE OSKB010084
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PCIE 目的
CASE OSKB010084
SOURCE z/OS MVS Operations
D PCIE 目的とOSKB010084が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010084を同じ出力で読み、置換判定の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010084
→ Enter を押す
［画面・出力］
IEE115I OSKB010084 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010084   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010084が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PCIE 目的 と OSKB010084 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010084 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D PFK


<section class="kb-item" id="c22-i0104"><h3>D PFK 目的</h3><p class="kb-meta">分類: D PFK ・ 難易度: 初級</p><p>D PFK 目的は、コンソールの PF キー定義 (PFKTABxx の SUFFIX に基づく) と現割当を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切判定の目的で D PFK 目的の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D PFK 目的の出力を取らず区切判定の目的の説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて区切判定の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切判定の目的の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切判定の目的へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では D PFK 目的 は「区切判定の目的に関係する定義値と表示行を照合する区切判定項目」と D A,L または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では D PFK 目的の属性行と IEE115I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明だけに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では D PFK 目的を MVS オペレータコマンドの運用手順で確認し、初出名は区切判定初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開照合の目的で D PFK 目的の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D PFK 目的の出力を取らず展開照合の目的の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開照合の目的の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開照合の目的へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 展開照合の目的において選択記号 B を採用し、識別名は展開照合です。展開照合の目的において D PFK 目的 は説明欄の「展開照合の目的に関係する定義値と表示行を照合する展開照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合の目的の証跡を読む担当者は、D PFK 目的の属性行と IEE115I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合の目的は対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開照合ではありません。 D: 展開照合の目的は別カテゴリの確認を流用しており、D PFK 目的の根拠にならないため展開照合ではありません。展開照合の目的に出る D PFK 目的は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PFK 目的</strong></p><p>検証目的: 終端判定の目的について、D PFK 目的は、コンソールの PF キー定義 (PFKTABxx の SUFFIX に基づく) と現割当を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010085の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端判定の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PFK 目的を指定し、OSKB010085の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PFK 目的
CASE OSKB010085
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PFK 目的
CASE OSKB010085
SOURCE z/OS MVS Operations
D PFK 目的とOSKB010085が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010085を同じ出力で読み、終端判定の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010085
→ Enter を押す
［画面・出力］
IEE115I OSKB010085 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010085   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010085が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PFK 目的 と OSKB010085 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010085 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D PROD


<section class="kb-item" id="c22-i0105"><h3>D PROD 目的</h3><p class="kb-meta">分類: D PROD ・ 難易度: 初級</p><p>D PROD 目的は、IFAPRDxx で登録された製品 (z/OS, RACF, DB2, CICS 等) のラベルと使用許諾状態を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲判定の目的で操作コマンドの運用確認を行います。D PROD 目的の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲判定の目的を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲判定の目的を正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を範囲判定で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D PROD 目的の属性行を読まず範囲判定の目的の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠では D PROD 目的 は「z/OS MVS Operationsで D PROD 目的の扱いを記録する範囲判定項目」と D A,L または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡では D PROD 目的の表示結果と IEE115I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明だけに寄り、判定名は範囲判定不足です。範囲判定資料では D PROD 目的の使い方を出典欄から追跡し、資料名は範囲判定資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出照合の目的で操作コマンドの運用確認を行います。D PROD 目的の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出照合の目的を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出照合の目的を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D PROD 目的の属性行を読まず呼出照合の目的の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 呼出照合の目的において選択記号 C を採用し、識別名は呼出照合です。呼出照合の目的において D PROD 目的 は説明欄の「z/OS MVS Operationsで D PROD 目的の扱いを記録する呼出照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合の目的を受け取る担当者は、D PROD 目的の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合の目的は別カテゴリの確認を流用しており、D PROD 目的の根拠にならないため呼出照合ではありません。 B: 呼出照合の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合の目的は対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合の目的が示す D PROD 目的は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PROD 目的</strong></p><p>検証目的: 値域確認の目的について、D PROD 目的は、IFAPRDxx で登録された製品 (z/OS, RACF, DB2, CICS 等) のラベルと使用許諾状態を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040016の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域確認の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PROD 目的を指定し、OSKB040016の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PROD 目的
CASE OSKB040016
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PROD 目的
CASE OSKB040016
SOURCE z/OS MVS Operations
D PROD 目的とOSKB040016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040016を同じ出力で読み、値域確認の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040016
→ Enter を押す
［画面・出力］
IEE115I OSKB040016 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040016   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PROD 目的 と OSKB040016 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D PROD 目的</strong></p><p>検証目的: 探索判定の目的について、D PROD 目的は、IFAPRDxx で登録された製品 (z/OS, RACF, DB2, CICS 等) のラベルと使用許諾状態を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010086の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、探索判定の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PROD 目的を指定し、OSKB010086の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PROD 目的
CASE OSKB010086
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PROD 目的
CASE OSKB010086
SOURCE z/OS MVS Operations
D PROD 目的とOSKB010086が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010086を同じ出力で読み、探索判定の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010086
→ Enter を押す
［画面・出力］
IEE115I OSKB010086 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010086   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010086が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PROD 目的 と OSKB010086 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010086 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0106"><h3>D PROD,STATE=ENABLED</h3><p class="kb-meta">分類: D PROD ・ 難易度: 中級</p><p>D PROD,STATE=ENABLEDは、現在 ENABLED で稼動許可されている製品のみを抽出して一覧表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先判定の操作コマンドに関する D PROD 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先判定の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先判定の操作コマンドの証跡として保存して根拠にする。</li><li>C. D PROD 命令の変更点を出力本文から切り離して優先判定の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、優先判定の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠では D PROD 命令 は「D PROD 命令の状態と出力メッセージを結び付ける優先判定項目」と D A,L または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存では D PROD 命令の出力行と IEE115I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明だけに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象では D PROD 命令をz/OS MVS Operationsの確認記録に残し、対象名は優先判定対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換照合の操作コマンドに関する D PROD,STATE=ENABLED の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. D PROD,STATE=ENABLED の変更点を出力本文から切り離して置換照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換照合の操作コマンドにおいて選択記号 D を採用し、識別名は置換照合です。置換照合の操作コマンドにおいて D PROD,STATE=ENABLED は説明欄の「D PROD,STATE=ENABLED の状態と出力メッセージを結び付ける置換照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合の操作コマンドに関する記録は、D PROD,STATE=ENABLED の出力行と IEE115I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換照合ではありません。 B: 置換照合の操作コマンドは別カテゴリの確認を流用しており、D PROD,STATE=ENABLED の根拠にならないため置換照合ではありません。 C: 置換照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合の操作コマンドで記録する D PROD,STATE=ENABLED はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PROD,STATE=ENABLED</strong></p><p>検証目的: 上書判定の操作コマンドについて、D PROD,STATE=ENABLED は、現在 ENABLED で稼動許可されている製品のみを抽出して一覧表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010087の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書判定の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PROD,STATE=ENABLを指定し、OSKB010087の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PROD,STATE=ENABL
CASE OSKB010087
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PROD,STATE=ENABL
CASE OSKB010087
SOURCE z/OS MVS Operations
D PROD,STATE=ENABLとOSKB010087が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010087を同じ出力で読み、上書判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010087
→ Enter を押す
［画面・出力］
IEE115I OSKB010087 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010087   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010087が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PROD,STATE=ENABL と OSKB010087 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010087 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D PROG


<section class="kb-item" id="c22-i0107"><h3>D PROG,APF 全リスト</h3><p class="kb-meta">分類: D PROG ・ 難易度: 中級</p><p>D PROG,APF 全リストは、MVS オペレータコマンドのD PROGで状態表示や操作を行うためのコマンド関連項目です。APF (Authorized Program Facility) 許可データセットとボリュームの現行リストを表示。SVA 経由の動的更新確認に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録判定の全リストに関係する D PROG,APF 全リストの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、記録判定の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D PROG,APF 全リストの名称と担当者名だけを残して記録判定の全リストの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録判定の全リストを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録判定の全リストの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠では D PROG,APF 全リスト は「D PROG,APF 全リストの用途を操作コマンドの表示で確認する記録判定項目」と D A,L または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景ではz/OS MVS Operationsの D PROG,APF 全リストと IEE115I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明だけに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語では D PROG,APF 全リストを MVS オペレータコマンドで扱う確認対象とし、用語名は記録判定用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端照合の全リストに関係する D PROG,APF 全リストの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D PROG,APF 全リストの名称と担当者名のみを残して終端照合の全リストの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端照合の全リストを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端照合の全リストの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端照合の全リストにおいて選択記号 A を採用し、識別名は終端照合です。終端照合の全リストにおいて D PROG,APF 全リスト は説明欄の「D PROG,APF 全リストの用途を操作コマンドの表示で確認する終端照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合の全リストに関連して、z/OS MVS Operationsでは D PROG,APF 全リストの表示属性と IEE115I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合の全リストは対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合の全リストは名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合の全リストは別カテゴリの確認を流用しており、D PROG,APF 全リストの根拠にならないため終端照合ではありません。 D: 終端照合の全リストは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端照合ではありません。終端照合の全リストで使う D PROG,APF 全リストという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PROG,APF 全リスト</strong></p><p>検証目的: 出力判定の全リストについて、D PROG,APF 全リストは、MVS オペレータコマンドの D PROG で状態表示や操作を行うためのコマンド関連項目です。APF (Authorized Programに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010088の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力判定の全リストの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PROG,APF 全リストを指定し、OSKB010088の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PROG,APF 全リスト
CASE OSKB010088
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PROG,APF 全リスト
CASE OSKB010088
SOURCE z/OS MVS Operations
D PROG,APF 全リストとOSKB010088が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010088を同じ出力で読み、出力判定の全リストの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010088
→ Enter を押す
［画面・出力］
IEE115I OSKB010088 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010088   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010088が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PROG,APF 全リスト と OSKB010088 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010088 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0108"><h3>D PROG,APF,DSNAME=dsn</h3><p class="kb-meta">分類: D PROG ・ 難易度: 中級</p><p>D PROG,APF,DSNAME=dsnは、MVS オペレータコマンドのD PROGで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較判定の操作コマンドで D PROG 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D PROG 命令の出力を取らず比較判定の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて比較判定の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較判定の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較判定の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較判定正解では選択記号 B を採用し、正解名は比較判定正解です。比較判定根拠では D PROG 命令 は「比較判定の操作コマンドに関係する定義値と表示行を照合する比較判定項目」と D A,L または該当パネルの出力を照合し、根拠名は比較判定根拠です。比較判定追跡では D PROG 命令の属性行と IEE115I を合わせ、追跡名は比較判定追跡です。誤答側の問題点を分けます。 A: 比較判定不足は名称や説明だけに寄り、判定名は比較判定不足です。 B: 比較判定正答は対象出力と項目説明を結び、根拠名は比較判定正答です。 C: 比較判定欠落は戻り値や記録番号に寄り、欠落名は比較判定欠落です。 D: 比較判定流用は別カテゴリの確認であり、排除名は比較判定流用です。比較判定初出では D PROG 命令を MVS オペレータコマンドの運用手順で確認し、初出名は比較判定初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索照合の操作コマンドで D PROG,APF,DSNAME=dsnの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D PROG,APF,DSNAME=dsnの出力を取らず探索照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索照合の操作コマンドにおいて選択記号 B を採用し、識別名は探索照合です。探索照合の操作コマンドにおいて D PROG,APF,DSNAME=dsn は説明欄の「探索照合の操作コマンドに関係する定義値と表示行を照合する探索照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合の操作コマンドの証跡を読む担当者は、D PROG,APF,DSNAME=dsnの属性行と IEE115I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索照合ではありません。 D: 探索照合の操作コマンドは別カテゴリの確認を流用しており、D PROG,APF,DSNAME=dsnの根拠にならないため探索照合ではありません。探索照合の操作コマンドに出る D PROG,APF,DSNAME=dsnは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PROG,APF,DSNAME=dsn</strong></p><p>検証目的: 条件判定の操作コマンドについて、D PROG,APF,DSNAME=dsnは、MVS オペレータコマンドの D PROG で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010089の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件判定の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PROG,APF,DSNAME=を指定し、OSKB010089の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PROG,APF,DSNAME=
CASE OSKB010089
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PROG,APF,DSNAME=
CASE OSKB010089
SOURCE z/OS MVS Operations
D PROG,APF,DSNAME=とOSKB010089が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010089を同じ出力で読み、条件判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010089
→ Enter を押す
［画面・出力］
IEE115I OSKB010089 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010089   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010089が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PROG,APF,DSNAME= と OSKB010089 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010089 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0109"><h3>D PROG,EXIT</h3><p class="kb-meta">分類: D PROG ・ 難易度: 上級</p><p>D PROG,EXITは、MVS オペレータコマンドのD PROGで確認する項目です。稼動中の動的出口 (Exit) と現在登録されている Exit ルーチンを表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧判定の操作コマンドで D PROG,EXIT の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D PROG,EXIT の出力を取らず復旧判定の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧判定の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧判定の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧判定の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧判定正解では選択記号 B を採用し、正解名は復旧判定正解です。復旧判定根拠では D PROG,EXIT は「復旧判定の操作コマンドに関係する定義値と表示行を照合する復旧判定項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧判定根拠です。復旧判定追跡では D PROG,EXIT の属性行と IEE115I を合わせ、追跡名は復旧判定追跡です。誤答側の問題点を分けます。 A: 復旧判定不足は名称や説明だけに寄り、判定名は復旧判定不足です。 B: 復旧判定正答は対象出力と項目説明を結び、根拠名は復旧判定正答です。 C: 復旧判定欠落は戻り値や記録番号に寄り、欠落名は復旧判定欠落です。 D: 復旧判定流用は別カテゴリの確認であり、排除名は復旧判定流用です。復旧判定初出では D PROG,EXIT を MVS オペレータコマンドの運用手順で確認し、初出名は復旧判定初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切照合の操作コマンドで D PROG,EXIT の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D PROG,EXIT の出力を取らず区切照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切照合の操作コマンドにおいて選択記号 B を採用し、識別名は区切照合です。区切照合の操作コマンドにおいて D PROG,EXIT は説明欄の「区切照合の操作コマンドに関係する定義値と表示行を照合する区切照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合の操作コマンドの証跡を読む担当者は、D PROG,EXIT の属性行と IEE115I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切照合ではありません。 D: 区切照合の操作コマンドは別カテゴリの確認を流用しており、D PROG,EXIT の根拠にならないため区切照合ではありません。区切照合の操作コマンドに出る D PROG,EXIT は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PROG,EXIT</strong></p><p>検証目的: 記録判定の操作コマンドについて、D PROG,EXIT は、MVS オペレータコマンドの D PROG で確認する項目です。稼動中の動的出口 (Exit) と現在登録されている Exit ルーチンを表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010093の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録判定の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PROG,EXITを指定し、OSKB010093の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PROG,EXIT
CASE OSKB010093
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PROG,EXIT
CASE OSKB010093
SOURCE z/OS MVS Operations
D PROG,EXITとOSKB010093が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010093を同じ出力で読み、記録判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010093
→ Enter を押す
［画面・出力］
IEE115I OSKB010093 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010093   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010093が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PROG,EXIT と OSKB010093 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010093 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0110"><h3>D PROG,EXIT,EX=name</h3><p class="kb-meta">分類: D PROG ・ 難易度: 上級</p><p>D PROG,EXIT,EX=nameは、特定の動的出口名 (例: SYSSTC.IEFUJV) に絞って登録ルーチン一覧を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査判定の操作コマンドで操作コマンドの運用確認を行います。D PROG 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査判定の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査判定の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、監査判定の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D PROG 命令の属性行を読まず監査判定の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では D PROG 命令 は「z/OS MVS Operationsで D PROG 命令の扱いを記録する監査判定項目」と D A,L または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では D PROG 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明だけに寄り、判定名は監査判定不足です。監査判定資料では D PROG 命令の使い方を出典欄から追跡し、資料名は監査判定資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 範囲照合の操作コマンドで操作コマンドの運用確認を行います。D PROG,EXIT,EX=nameの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲照合の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲照合の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D PROG,EXIT,EX=nameの属性行を読まず範囲照合の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲照合の操作コマンドにおいて選択記号 C を採用し、識別名は範囲照合です。範囲照合の操作コマンドにおいて D PROG,EXIT,EX=name は説明欄の「z/OS MVS Operationsで D PROG,EXIT,EX=nameの扱いを記録する範囲照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合の操作コマンドを受け取る担当者は、D PROG,EXIT,EX=nameの表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合の操作コマンドは別カテゴリの確認を流用しており、D PROG,EXIT,EX=nameの根拠にならないため範囲照合ではありません。 B: 範囲照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合の操作コマンドが示す D PROG,EXIT,EX=nameは出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PROG,EXIT,EX=name</strong></p><p>検証目的: 比較判定の操作コマンドについて、D PROG,EXIT,EX=nameは、特定の動的出口名 (例: SYSSTC.IEFUJV) に絞って登録ルーチン一覧を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010094の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較判定の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PROG,EXIT,EX=namを指定し、OSKB010094の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PROG,EXIT,EX=nam
CASE OSKB010094
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PROG,EXIT,EX=nam
CASE OSKB010094
SOURCE z/OS MVS Operations
D PROG,EXIT,EX=namとOSKB010094が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010094を同じ出力で読み、比較判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010094
→ Enter を押す
［画面・出力］
IEE115I OSKB010094 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010094   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010094が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PROG,EXIT,EX=nam と OSKB010094 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010094 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0111"><h3>D PROG,LNKLST 全リスト</h3><p class="kb-meta">分類: D PROG ・ 難易度: 中級</p><p>D PROG,LNKLST 全リストは、MVS オペレータコマンドのD PROGで確認する項目です。現行 LNKLST セットの名前と連結データセット順序を表示する。動的 LNKLST 切替確認の基本</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序判定の全リストで操作コマンドの運用確認を行います。D PROG 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序判定の全リストを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序判定の全リストを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、順序判定の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D PROG 命令の属性行を読まず順序判定の全リストの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序判定正解では選択記号 C を採用し、正解名は順序判定正解です。順序判定根拠では D PROG 命令 は「z/OS MVS Operationsで D PROG 命令の扱いを記録する順序判定項目」と D A,L または該当パネルの出力を照合し、根拠名は順序判定根拠です。順序判定受渡では D PROG 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は順序判定受渡です。不適切な選択肢を整理します。 A: 順序判定流用は別カテゴリの確認であり、排除名は順序判定流用です。 B: 順序判定欠落は戻り値や記録番号に寄り、欠落名は順序判定欠落です。 C: 順序判定正答は対象出力と項目説明を結び、根拠名は順序判定正答です。 D: 順序判定不足は名称や説明だけに寄り、判定名は順序判定不足です。順序判定資料では D PROG 命令の使い方を出典欄から追跡し、資料名は順序判定資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書照合の全リストで操作コマンドの運用確認を行います。D PROG,LNKLST 全リストの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書照合の全リストを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書照合の全リストを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D PROG,LNKLST 全リストの属性行を読まず上書照合の全リストの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書照合の全リストにおいて選択記号 C を採用し、識別名は上書照合です。上書照合の全リストにおいて D PROG,LNKLST 全リスト は説明欄の「z/OS MVS Operationsで D PROG,LNKLST 全リストの扱いを記録する上書照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の全リストを受け取る担当者は、D PROG,LNKLST 全リストの表示結果と IEE115I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の全リストは別カテゴリの確認を流用しており、D PROG,LNKLST 全リストの根拠にならないため上書照合ではありません。 B: 上書照合の全リストは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書照合ではありません。 C: 上書照合の全リストは対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の全リストは名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の全リストが示す D PROG,LNKLST 全リストは出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PROG,LNKLST 全リスト</strong></p><p>検証目的: 区切判定の全リストについて、D PROG,LNKLST 全リストは、MVS オペレータコマンドの D PROG で確認する項目です。現行 LNKLST セットの名前と連結データセット順序を表示する。動的に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010090の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切判定の全リストの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PROG,LNKLST 全リストを指定し、OSKB010090の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PROG,LNKLST 全リスト
CASE OSKB010090
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PROG,LNKLST 全リスト
CASE OSKB010090
SOURCE z/OS MVS Operations
D PROG,LNKLST 全リストとOSKB010090が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010090を同じ出力で読み、区切判定の全リストの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010090
→ Enter を押す
［画面・出力］
IEE115I OSKB010090 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010090   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010090が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PROG,LNKLST 全リスト と OSKB010090 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010090 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0112"><h3>D PROG,LNKLST,NAME=set</h3><p class="kb-meta">分類: D PROG ・ 難易度: 中級</p><p>D PROG,LNKLST,NAME=setは、指定 LNKLST セット (LNKLSTxx の SET 名) のメンバ DSN のみを抽出表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域判定の操作コマンドに関する D PROG 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域判定の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域判定の操作コマンドの証跡として保存して根拠にする。</li><li>C. D PROG 命令の変更点を出力本文から切り離して値域判定の操作コマンドの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、値域判定の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域判定正解では選択記号 D を採用し、正解名は値域判定正解です。値域判定根拠では D PROG 命令 は「D PROG 命令の状態と出力メッセージを結び付ける値域判定項目」と D A,L または該当パネルの出力を照合し、根拠名は値域判定根拠です。値域判定保存では D PROG 命令の出力行と IEE115I を一緒に残し、保存名は値域判定保存です。選択肢ごとの違いを示します。 A: 値域判定欠落は戻り値や記録番号に寄り、欠落名は値域判定欠落です。 B: 値域判定流用は別カテゴリの確認であり、排除名は値域判定流用です。 C: 値域判定不足は名称や説明だけに寄り、判定名は値域判定不足です。 D: 値域判定正答は対象出力と項目説明を結び、根拠名は値域判定正答です。値域判定対象では D PROG 命令をz/OS MVS Operationsの確認記録に残し、対象名は値域判定対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力照合の操作コマンドに関する D PROG,LNKLST,NAME=setの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. D PROG,LNKLST,NAME=setの変更点を出力本文から切り離して出力照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力照合の操作コマンドにおいて選択記号 D を採用し、識別名は出力照合です。出力照合の操作コマンドにおいて D PROG,LNKLST,NAME=set は説明欄の「D PROG,LNKLST,NAME=setの状態と出力メッセージを結び付ける出力照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合の操作コマンドに関する記録は、D PROG,LNKLST,NAME=setの出力行と IEE115I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力照合ではありません。 B: 出力照合の操作コマンドは別カテゴリの確認を流用しており、D PROG,LNKLST,NAME=setの根拠にならないため出力照合ではありません。 C: 出力照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合の操作コマンドで記録する D PROG,LNKLST,NAME=setはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PROG,LNKLST,NAME=set</strong></p><p>検証目的: 範囲判定の操作コマンドについて、D PROG,LNKLST,NAME=setは、指定 LNKLST セット (LNKLSTxx の SET 名) のメンバ DSN のみを抽出表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010091の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲判定の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PROG,LNKLST,NAMEを指定し、OSKB010091の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PROG,LNKLST,NAME
CASE OSKB010091
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PROG,LNKLST,NAME
CASE OSKB010091
SOURCE z/OS MVS Operations
D PROG,LNKLST,NAMEとOSKB010091が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010091を同じ出力で読み、範囲判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010091
→ Enter を押す
［画面・出力］
IEE115I OSKB010091 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010091   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010091が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PROG,LNKLST,NAME と OSKB010091 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010091 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0113"><h3>D PROG,LPA</h3><p class="kb-meta">分類: D PROG ・ 難易度: 中級</p><p>Dynamic LPA に追加されたモジュールの一覧。SETPROG LPA,ADD で動的にロードしたモジュールの確認に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告判定の操作コマンドに関係する D PROG,LPA の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、警告判定として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D PROG,LPA の名称と担当者名だけを残して警告判定の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告判定の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告判定の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では D PROG,LPA は「D PROG,LPA の用途を操作コマンドの表示で確認する警告判定項目」と D A,L または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景ではz/OS MVS Operationsの D PROG,LPA と IEE115I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明だけに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では D PROG,LPA を MVS オペレータコマンドで扱う確認対象とし、用語名は警告判定用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件照合の操作コマンドに関係する D PROG,LPA の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D PROG,LPA の名称と担当者名のみを残して条件照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件照合の操作コマンドにおいて選択記号 A を採用し、識別名は条件照合です。条件照合の操作コマンドにおいて D PROG,LPA は説明欄の「D PROG,LPA の用途を操作コマンドの表示で確認する条件照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の操作コマンドに関連して、z/OS MVS Operationsでは D PROG,LPA の表示属性と IEE115I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の操作コマンドは別カテゴリの確認を流用しており、D PROG,LPA の根拠にならないため条件照合ではありません。 D: 条件照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件照合ではありません。条件照合の操作コマンドで使う D PROG,LPA という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D PROG,LPA</strong></p><p>検証目的: 警告確認の操作コマンドについて、Dynamic LPA に追加されたモジュールの一覧。SETPROG LPA,ADD で動的にロードしたモジュールの確認に使うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040017の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PROG,LPAを指定し、OSKB040017の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PROG,LPA
CASE OSKB040017
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PROG,LPA
CASE OSKB040017
SOURCE z/OS MVS Operations
D PROG,LPAとOSKB040017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040017を同じ出力で読み、警告確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040017
→ Enter を押す
［画面・出力］
IEE115I OSKB040017 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040017   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PROG,LPA と OSKB040017 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D PROG,LPA</strong></p><p>検証目的: 優先判定の操作コマンドについて、Dynamic LPA に追加されたモジュールの一覧。SETPROG LPA,ADD で動的にロードしたモジュールの確認に使うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010092の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先判定の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD PROG,LPAを指定し、OSKB010092の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D PROG,LPA
CASE OSKB010092
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D PROG,LPA
CASE OSKB010092
SOURCE z/OS MVS Operations
D PROG,LPAとOSKB010092が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010092を同じ出力で読み、優先判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010092
→ Enter を押す
［画面・出力］
IEE115I OSKB010092 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010092   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010092が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D PROG,LPA と OSKB010092 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010092 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D R


<section class="kb-item" id="c22-i0114"><h3>D R,CE 該当コンソール</h3><p class="kb-meta">分類: D R ・ 難易度: 中級</p><p>D R,CE 該当コンソールは、MVS オペレータコマンドのD Rで確認する項目です。未応答 WTOR を受け取る権限を持つコンソール一覧を表示。マルチコンソール環境で応答可否を確認</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文整理の該当コンソールに関係する D R,CE 該当コンソールの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、構文整理の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D R,CE 該当コンソールの名称と担当者名だけを残して構文整理の該当コンソールの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文整理の該当コンソールを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文整理の該当コンソールの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文整理正解では選択記号 A を採用し、正解名は構文整理正解です。構文整理根拠では D R,CE 該当コンソール は「D R,CE 該当コンソールの用途を操作コマンドの表示で確認する構文整理項目」と D A,L または該当パネルの出力を照合し、根拠名は構文整理根拠です。構文整理背景ではz/OS MVS Operationsの D R,CE 該当コンソールと IEE115I を同じ証跡に残し、背景名は構文整理背景です。他の選択肢を確認します。 A: 構文整理正答は対象出力と項目説明を結び、根拠名は構文整理正答です。 B: 構文整理不足は名称や説明だけに寄り、判定名は構文整理不足です。 C: 構文整理流用は別カテゴリの確認であり、排除名は構文整理流用です。 D: 構文整理欠落は戻り値や記録番号に寄り、欠落名は構文整理欠落です。構文整理用語では D R,CE 該当コンソールを MVS オペレータコマンドで扱う確認対象とし、用語名は構文整理用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 記録照合の該当コンソールに関係する D R,CE 該当コンソールの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、記録照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D R,CE 該当コンソールの名称と担当者名のみを残して記録照合の該当コンソールの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で記録照合の該当コンソールを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録照合の該当コンソールの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録照合の該当コンソールにおいて選択記号 A を採用し、識別名は記録照合です。記録照合の該当コンソールにおいて D R,CE 該当コンソール は説明欄の「D R,CE 該当コンソールの用途を操作コマンドの表示で確認する記録照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合の該当コンソールに関連して、z/OS MVS Operationsでは D R,CE 該当コンソールの表示属性と IEE115I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合の該当コンソールは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合の該当コンソールは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合の該当コンソールは別カテゴリの確認を流用しており、D R,CE 該当コンソールの根拠にならないため記録照合ではありません。 D: 記録照合の該当コンソールは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録照合ではありません。記録照合の該当コンソールで使う D R,CE 該当コンソールという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D R,CE 該当コンソール</strong></p><p>検証目的: 値域判定の該当コンソールについて、D R,CE 該当コンソールは、MVS オペレータコマンドの D R で確認する項目です。未応答 WTOR を受け取る権限を持つコンソール一覧を表示。マルチコンソール環境で応答に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010096の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域判定の該当コンソールの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD R,CE 該当コンソールを指定し、OSKB010096の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D R,CE 該当コンソール
CASE OSKB010096
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D R,CE 該当コンソール
CASE OSKB010096
SOURCE z/OS MVS Operations
D R,CE 該当コンソールとOSKB010096が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010096を同じ出力で読み、値域判定の該当コンソールの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010096
→ Enter を押す
［画面・出力］
IEE115I OSKB010096 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010096   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010096が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D R,CE 該当コンソール と OSKB010096 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010096 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0115"><h3>D R,KEY=key キーで絞込</h3><p class="kb-meta">分類: D R ・ 難易度: 中級</p><p>D R,KEY=key キーで絞込は、MVS オペレータコマンドのD Rで状態表示や操作を行うためのコマンド関連項目です。D R,KEY=key キーで絞込は、WTOR メッセージのキー (例: IEF238D の DSN 名等) で未応答メッセージを絞って表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開整理のキーで絞込で D R 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D R 命令の出力を取らず展開整理のキーで絞込の説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて展開整理の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開整理のキーで絞込の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開整理のキーで絞込へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開整理正解では選択記号 B を採用し、正解名は展開整理正解です。展開整理根拠では D R 命令 は「展開整理のキーで絞込に関係する定義値と表示行を照合する展開整理項目」と D A,L または該当パネルの出力を照合し、根拠名は展開整理根拠です。展開整理追跡では D R 命令の属性行と IEE115I を合わせ、追跡名は展開整理追跡です。誤答側の問題点を分けます。 A: 展開整理不足は名称や説明だけに寄り、判定名は展開整理不足です。 B: 展開整理正答は対象出力と項目説明を結び、根拠名は展開整理正答です。 C: 展開整理欠落は戻り値や記録番号に寄り、欠落名は展開整理欠落です。 D: 展開整理流用は別カテゴリの確認であり、排除名は展開整理流用です。展開整理初出では D R 命令を MVS オペレータコマンドの運用手順で確認し、初出名は展開整理初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 比較照合のキーで絞込で D R,KEY=key キーで絞込の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D R,KEY=key キーで絞込の出力を取らず比較照合のキーで絞込の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、比較照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較照合のキーで絞込の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較照合のキーで絞込へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較照合のキーで絞込において選択記号 B を採用し、識別名は比較照合です。比較照合のキーで絞込において D R,KEY=key キーで絞込 は説明欄の「比較照合のキーで絞込に関係する定義値と表示行を照合する比較照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合のキーで絞込の証跡を読む担当者は、D R,KEY=key キーで絞込の属性行と IEE115I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合のキーで絞込は名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合のキーで絞込は対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合のキーで絞込は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較照合ではありません。 D: 比較照合のキーで絞込は別カテゴリの確認を流用しており、D R,KEY=key キーで絞込の根拠にならないため比較照合ではありません。比較照合のキーで絞込に出る D R,KEY=key キーで絞込は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D R,KEY=key キーで絞込</strong></p><p>検証目的: 警告判定のキーで絞込について、D R,KEY=key キーで絞込は、MVS オペレータコマンドの D R で状態表示や操作を行うためのコマンド関連項目です。D R,KEY=key キーで絞込は、WTOR メに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010097の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告判定のキーで絞込の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD R,KEY=key キーで絞込を指定し、OSKB010097の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D R,KEY=key キーで絞込
CASE OSKB010097
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D R,KEY=key キーで絞込
CASE OSKB010097
SOURCE z/OS MVS Operations
D R,KEY=key キーで絞込とOSKB010097が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010097を同じ出力で読み、警告判定のキーで絞込の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010097
→ Enter を押す
［画面・出力］
IEE115I OSKB010097 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010097   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010097が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D R,KEY=key キーで絞込 と OSKB010097 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010097 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0116"><h3>D R,L 未応答 WTOR 一覧</h3><p class="kb-meta">分類: D R ・ 難易度: 中級</p><p>D R,L 未応答 WTOR 一覧は、MVS オペレータコマンドのD Rで確認する項目です。応答待ち WTOR メッセージ (R 番号付き) の全件を一覧表示。応答漏れジョブの停滞検出に使う最頻出コマンド</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更判定の未応答 一覧に関する D R 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更判定の未応答 一覧の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更判定の未応答 一覧の証跡として保存して根拠にする。</li><li>C. D R 命令の変更点を出力本文から切り離して変更判定の未応答 一覧の承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更判定で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更判定正解では選択記号 D を採用し、正解名は変更判定正解です。変更判定根拠では D R 命令 は「D R 命令の状態と出力メッセージを結び付ける変更判定項目」と D A,L または該当パネルの出力を照合し、根拠名は変更判定根拠です。変更判定保存では D R 命令の出力行と IEE115I を一緒に残し、保存名は変更判定保存です。選択肢ごとの違いを示します。 A: 変更判定欠落は戻り値や記録番号に寄り、欠落名は変更判定欠落です。 B: 変更判定流用は別カテゴリの確認であり、排除名は変更判定流用です。 C: 変更判定不足は名称や説明だけに寄り、判定名は変更判定不足です。 D: 変更判定正答は対象出力と項目説明を結び、根拠名は変更判定正答です。変更判定対象では D R 命令をz/OS MVS Operationsの確認記録に残し、対象名は変更判定対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 優先照合の未応答 一覧に関する D R,L 未応答 WTOR 一覧の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先照合の未応答 一覧の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先照合の未応答 一覧の証跡として保存して根拠にする。</li><li>C. D R,L 未応答 WTOR 一覧の変更点を出力本文から切り離して優先照合の未応答 一覧の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先照合の未応答 一覧において選択記号 D を採用し、識別名は優先照合です。優先照合の未応答 一覧において D R,L 未応答 WTOR 一覧 は説明欄の「D R,L 未応答 WTOR 一覧の状態と出力メッセージを結び付ける優先照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合の未応答 一覧に関する記録は、D R,L 未応答 WTOR 一覧の出力行と IEE115I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合の未応答 一覧は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先照合ではありません。 B: 優先照合の未応答 一覧は別カテゴリの確認を流用しており、D R,L 未応答 WTOR 一覧の根拠にならないため優先照合ではありません。 C: 優先照合の未応答 一覧は名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合の未応答 一覧は対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合の未応答 一覧で記録する D R,L 未応答 WTOR 一覧はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D R,L 未応答 WTOR 一覧</strong></p><p>検証目的: 順序判定の未応答 一覧について、D R,L 未応答 WTOR 一覧は、MVS オペレータコマンドの D R で確認する項目です。応答待ち WTOR メッセージ (R 番号付き) の全件を一覧表示。応答漏れジョに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010095の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序判定の未応答 一覧の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD R,L 未応答 WTOR 一覧を指定し、OSKB010095の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D R,L 未応答 WTOR 一覧
CASE OSKB010095
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D R,L 未応答 WTOR 一覧
CASE OSKB010095
SOURCE z/OS MVS Operations
D R,L 未応答 WTOR 一覧とOSKB010095が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010095を同じ出力で読み、順序判定の未応答 一覧の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010095
→ Enter を押す
［画面・出力］
IEE115I OSKB010095 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010095   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010095が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D R,L 未応答 WTOR 一覧 と OSKB010095 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010095 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0117"><h3>D R,R,L 保持メッセージ</h3><p class="kb-meta">分類: D R ・ 難易度: 中級</p><p>D R,R,L 保持メッセージは、MVS オペレータコマンドのD Rで確認する項目です。MPF RETAIN 指定または明示的 K M,REF で保持されているメッセージを表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出整理の保持メッセージで操作コマンドの運用確認を行います。D R,R,L 保持メッセージの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出整理の保持メッセージを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出整理の保持メッセージを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を呼出整理で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D R,R,L 保持メッセージの属性行を読まず呼出整理の保持メッセージの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出整理正解では選択記号 C を採用し、正解名は呼出整理正解です。呼出整理根拠では D R,R,L 保持メッセージ は「z/OS MVS Operationsで D R,R,L 保持メッセージの扱いを記録する呼出整理項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出整理根拠です。呼出整理受渡では D R,R,L 保持メッセージの表示結果と IEE115I を同じ確認単位にし、受渡名は呼出整理受渡です。不適切な選択肢を整理します。 A: 呼出整理流用は別カテゴリの確認であり、排除名は呼出整理流用です。 B: 呼出整理欠落は戻り値や記録番号に寄り、欠落名は呼出整理欠落です。 C: 呼出整理正答は対象出力と項目説明を結び、根拠名は呼出整理正答です。 D: 呼出整理不足は名称や説明だけに寄り、判定名は呼出整理不足です。呼出整理資料では D R,R,L 保持メッセージの使い方を出典欄から追跡し、資料名は呼出整理資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 順序照合の保持メッセージで操作コマンドの運用確認を行います。D R,R,L 保持メッセージの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序照合の保持メッセージを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序照合の保持メッセージを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、順序照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D R,R,L 保持メッセージの属性行を読まず順序照合の保持メッセージの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序照合の保持メッセージにおいて選択記号 C を採用し、識別名は順序照合です。順序照合の保持メッセージにおいて D R,R,L 保持メッセージ は説明欄の「z/OS MVS Operationsで D R,R,L 保持メッセージの扱いを記録する順序照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合の保持メッセージを受け取る担当者は、D R,R,L 保持メッセージの表示結果と IEE115I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合の保持メッセージは別カテゴリの確認を流用しており、D R,R,L 保持メッセージの根拠にならないため順序照合ではありません。 B: 順序照合の保持メッセージは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため順序照合ではありません。 C: 順序照合の保持メッセージは対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合の保持メッセージは名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合の保持メッセージが示す D R,R,L 保持メッセージは出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D R,R,L 保持メッセージ</strong></p><p>検証目的: 復旧確認の保持メッセージについて、D R,R,L 保持メッセージは、MVS オペレータコマンドの D R で確認する項目です。MPF RETAIN 指定または明示的 K M,REF で保持されているメッセージをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040018の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧確認の保持メッセージの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD R,R,L 保持メッセージを指定し、OSKB040018の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D R,R,L 保持メッセージ
CASE OSKB040018
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D R,R,L 保持メッセージ
CASE OSKB040018
SOURCE z/OS MVS Operations
D R,R,L 保持メッセージとOSKB040018が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040018を同じ出力で読み、復旧確認の保持メッセージの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040018
→ Enter を押す
［画面・出力］
IEE115I OSKB040018 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040018   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040018が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D R,R,L 保持メッセージ と OSKB040018 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040018 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D R,R,L 保持メッセージ</strong></p><p>検証目的: 復旧判定の保持メッセージについて、D R,R,L 保持メッセージは、MVS オペレータコマンドの D R で確認する項目です。MPF RETAIN 指定または明示的 K M,REF で保持されているメッセージをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010098の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧判定の保持メッセージの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD R,R,L 保持メッセージを指定し、OSKB010098の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D R,R,L 保持メッセージ
CASE OSKB010098
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D R,R,L 保持メッセージ
CASE OSKB010098
SOURCE z/OS MVS Operations
D R,R,L 保持メッセージとOSKB010098が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010098を同じ出力で読み、復旧判定の保持メッセージの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010098
→ Enter を押す
［画面・出力］
IEE115I OSKB010098 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010098   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010098が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D R,R,L 保持メッセージ と OSKB010098 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010098 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D RTLS


<section class="kb-item" id="c22-i0118"><h3>D RTLS 目的</h3><p class="kb-meta">分類: D RTLS ・ 難易度: 初級</p><p>D RTLS 目的は、RTLSxx で定義した System REXX のランタイム・ライブラリ・サービス設定の現状を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換整理の目的に関する D RTLS 目的の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換整理の目的の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換整理の目的の証跡として保存して根拠にする。</li><li>C. D RTLS 目的の変更点を出力本文から切り離して置換整理の目的の承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、置換整理の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では D RTLS 目的 は「D RTLS 目的の状態と出力メッセージを結び付ける置換整理項目」と D A,L または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では D RTLS 目的の出力行と IEE115I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明だけに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では D RTLS 目的をz/OS MVS Operationsの確認記録に残し、対象名は置換整理対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 値域照合の目的に関する D RTLS 目的の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域照合の目的の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域照合の目的の証跡として保存して根拠にする。</li><li>C. D RTLS 目的の変更点を出力本文から切り離して値域照合の目的の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、値域照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 値域照合の目的において選択記号 D を採用し、識別名は値域照合です。値域照合の目的において D RTLS 目的 は説明欄の「D RTLS 目的の状態と出力メッセージを結び付ける値域照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の目的に関する記録は、D RTLS 目的の出力行と IEE115I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域照合ではありません。 B: 値域照合の目的は別カテゴリの確認を流用しており、D RTLS 目的の根拠にならないため値域照合ではありません。 C: 値域照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の目的は対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の目的で記録する D RTLS 目的はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D RTLS 目的</strong></p><p>検証目的: 監査判定の目的について、D RTLS 目的は、RTLSxx で定義した System REXX のランタイム・ライブラリ・サービス設定の現状を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010099の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査判定の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD RTLS 目的を指定し、OSKB010099の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D RTLS 目的
CASE OSKB010099
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D RTLS 目的
CASE OSKB010099
SOURCE z/OS MVS Operations
D RTLS 目的とOSKB010099が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010099を同じ出力で読み、監査判定の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010099
→ Enter を押す
［画面・出力］
IEE115I OSKB010099 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010099   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010099が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D RTLS 目的 と OSKB010099 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010099 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D SLIP


<section class="kb-item" id="c22-i0119"><h3>D SLIP 全件表示</h3><p class="kb-meta">分類: D SLIP ・ 難易度: 中級</p><p>D SLIP 全件表示は、現在 SLIP コマンドで設定されたトラップ (ID, EVENT, ACTION, STATE) の一覧を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端整理の全件表示に関係する D SLIP 全件表示の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、終端整理の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D SLIP 全件表示の名称と担当者名だけを残して終端整理の全件表示の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端整理の全件表示を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端整理の全件表示の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端整理正解では選択記号 A を採用し、正解名は終端整理正解です。終端整理根拠では D SLIP 全件表示 は「D SLIP 全件表示の用途を操作コマンドの表示で確認する終端整理項目」と D A,L または該当パネルの出力を照合し、根拠名は終端整理根拠です。終端整理背景ではz/OS MVS Operationsの D SLIP 全件表示と IEE115I を同じ証跡に残し、背景名は終端整理背景です。他の選択肢を確認します。 A: 終端整理正答は対象出力と項目説明を結び、根拠名は終端整理正答です。 B: 終端整理不足は名称や説明だけに寄り、判定名は終端整理不足です。 C: 終端整理流用は別カテゴリの確認であり、排除名は終端整理流用です。 D: 終端整理欠落は戻り値や記録番号に寄り、欠落名は終端整理欠落です。終端整理用語では D SLIP 全件表示を MVS オペレータコマンドで扱う確認対象とし、用語名は終端整理用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 警告照合の全件表示に関係する D SLIP 全件表示の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、警告照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D SLIP 全件表示の名称と担当者名のみを残して警告照合の全件表示の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で警告照合の全件表示を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告照合の全件表示の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告照合の全件表示において選択記号 A を採用し、識別名は警告照合です。警告照合の全件表示において D SLIP 全件表示 は説明欄の「D SLIP 全件表示の用途を操作コマンドの表示で確認する警告照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の全件表示に関連して、z/OS MVS Operationsでは D SLIP 全件表示の表示属性と IEE115I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の全件表示は対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の全件表示は名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の全件表示は別カテゴリの確認を流用しており、D SLIP 全件表示の根拠にならないため警告照合ではありません。 D: 警告照合の全件表示は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告照合ではありません。警告照合の全件表示で使う D SLIP 全件表示という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SLIP 全件表示</strong></p><p>検証目的: 変更判定の全件表示について、D SLIP 全件表示は、現在 SLIP コマンドで設定されたトラップ (ID, EVENT, ACTION, STATE) の一覧を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010100の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更判定の全件表示の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SLIP 全件表示を指定し、OSKB010100の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SLIP 全件表示
CASE OSKB010100
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SLIP 全件表示
CASE OSKB010100
SOURCE z/OS MVS Operations
D SLIP 全件表示とOSKB010100が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010100を同じ出力で読み、変更判定の全件表示の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010100
→ Enter を押す
［画面・出力］
IEE115I OSKB010100 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010100   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010100が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SLIP 全件表示 と OSKB010100 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010100 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0120"><h3>D SLIP,ENABLED 有効分のみ</h3><p class="kb-meta">分類: D SLIP ・ 難易度: 中級</p><p>D SLIP,ENABLED 有効分のみは、MVS オペレータコマンドのD SLIPで確認する項目です。STATE=ENABLED のトラップだけ抽出。長期に渡って残留する不要トラップの掃除に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書整理の有効分のみで操作コマンドの運用確認を行います。D SLIP 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書整理の有効分のみを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書整理の有効分のみを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、上書整理の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D SLIP 命令の属性行を読まず上書整理の有効分のみの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書整理正解では選択記号 C を採用し、正解名は上書整理正解です。上書整理根拠では D SLIP 命令 は「z/OS MVS Operationsで D SLIP 命令の扱いを記録する上書整理項目」と D A,L または該当パネルの出力を照合し、根拠名は上書整理根拠です。上書整理受渡では D SLIP 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は上書整理受渡です。不適切な選択肢を整理します。 A: 上書整理流用は別カテゴリの確認であり、排除名は上書整理流用です。 B: 上書整理欠落は戻り値や記録番号に寄り、欠落名は上書整理欠落です。 C: 上書整理正答は対象出力と項目説明を結び、根拠名は上書整理正答です。 D: 上書整理不足は名称や説明だけに寄り、判定名は上書整理不足です。上書整理資料では D SLIP 命令の使い方を出典欄から追跡し、資料名は上書整理資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 監査照合の有効分のみで操作コマンドの運用確認を行います。D SLIP,ENABLED 有効分のみの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査照合の有効分のみを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査照合の有効分のみを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、監査照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D SLIP,ENABLED 有効分のみの属性行を読まず監査照合の有効分のみの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査照合の有効分のみにおいて選択記号 C を採用し、識別名は監査照合です。監査照合の有効分のみにおいて D SLIP,ENABLED 有効分のみ は説明欄の「z/OS MVS Operationsで D SLIP,ENABLED 有効分のみの扱いを記録する監査照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の有効分のみを受け取る担当者は、D SLIP,ENABLED 有効分のみの表示結果と IEE115I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の有効分のみは別カテゴリの確認を流用しており、D SLIP,ENABLED 有効分のみの根拠にならないため監査照合ではありません。 B: 監査照合の有効分のみは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査照合ではありません。 C: 監査照合の有効分のみは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の有効分のみは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の有効分のみが示す D SLIP,ENABLED 有効分のみは出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SLIP,ENABLED 有効分のみ</strong></p><p>検証目的: 展開整理の有効分のみについて、D SLIP,ENABLED 有効分のみは、MVS オペレータコマンドの D SLIP で確認する項目です。STATE=ENABLED のトラップだけ抽出。長期に渡って残留するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010102の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開整理の有効分のみの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SLIP,ENABLED 有効分を指定し、OSKB010102の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SLIP,ENABLED 有効分
CASE OSKB010102
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SLIP,ENABLED 有効分
CASE OSKB010102
SOURCE z/OS MVS Operations
D SLIP,ENABLED 有効分とOSKB010102が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010102を同じ出力で読み、展開整理の有効分のみの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010102
→ Enter を押す
［画面・出力］
IEE115I OSKB010102 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010102   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010102が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SLIP,ENABLED 有効分 と OSKB010102 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010102 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0121"><h3>D SLIP=trapid 個別</h3><p class="kb-meta">分類: D SLIP ・ 難易度: 中級</p><p>D SLIP=trapid 個別は、指定 SLIP トラップ ID の詳細パラメータ (EVENT, COMP, REASON, ACTION, MATCHLIM 等) を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索整理の個別で D 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D 属性の出力を取らず探索整理の個別の説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて探索整理の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索整理の個別の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索整理の個別へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では D 属性 は「探索整理の個別に関係する定義値と表示行を照合する探索整理項目」と D A,L または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では D 属性の属性行と IEE115I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明だけに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では D 属性を MVS オペレータコマンドの運用手順で確認し、初出名は探索整理初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 復旧照合の個別で D SLIP=trapid 個別の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D SLIP=trapid 個別の出力を取らず復旧照合の個別の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、復旧照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧照合の個別の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧照合の個別へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧照合の個別において選択記号 B を採用し、識別名は復旧照合です。復旧照合の個別において D SLIP=trapid 個別 は説明欄の「復旧照合の個別に関係する定義値と表示行を照合する復旧照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の個別の証跡を読む担当者は、D SLIP=trapid 個別の属性行と IEE115I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の個別は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の個別は対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の個別は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の個別は別カテゴリの確認を流用しており、D SLIP=trapid 個別の根拠にならないため復旧照合ではありません。復旧照合の個別に出る D SLIP=trapid 個別は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SLIP=trapid 個別</strong></p><p>検証目的: 構文整理の個別について、D SLIP=trapid 個別は、指定 SLIP トラップ ID の詳細パラメータ (EVENT, COMP, REASON, ACTION, MATCHLIM 等) をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010101の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文整理の個別の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SLIP=trapid 個別を指定し、OSKB010101の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SLIP=trapid 個別
CASE OSKB010101
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SLIP=trapid 個別
CASE OSKB010101
SOURCE z/OS MVS Operations
D SLIP=trapid 個別とOSKB010101が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010101を同じ出力で読み、構文整理の個別の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010101
→ Enter を押す
［画面・出力］
IEE115I OSKB010101 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010101   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010101が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SLIP=trapid 個別 と OSKB010101 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010101 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D SMF


<section class="kb-item" id="c22-i0122"><h3>D SMF 全体状態</h3><p class="kb-meta">分類: D SMF ・ 難易度: 上級</p><p>D SMF 全体状態は、SMF の稼働モード (LOGSTREAM / MAN データセット) と現行アクティブ・データセット番号、書込み状況を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力整理の全体状態に関する D SMF 全体状態の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力整理の全体状態の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力整理の全体状態の証跡として保存して根拠にする。</li><li>C. D SMF 全体状態の変更点を出力本文から切り離して出力整理の全体状態の承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、出力整理の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力整理正解では選択記号 D を採用し、正解名は出力整理正解です。出力整理根拠では D SMF 全体状態 は「D SMF 全体状態の状態と出力メッセージを結び付ける出力整理項目」と D A,L または該当パネルの出力を照合し、根拠名は出力整理根拠です。出力整理保存では D SMF 全体状態の出力行と IEE115I を一緒に残し、保存名は出力整理保存です。選択肢ごとの違いを示します。 A: 出力整理欠落は戻り値や記録番号に寄り、欠落名は出力整理欠落です。 B: 出力整理流用は別カテゴリの確認であり、排除名は出力整理流用です。 C: 出力整理不足は名称や説明だけに寄り、判定名は出力整理不足です。 D: 出力整理正答は対象出力と項目説明を結び、根拠名は出力整理正答です。出力整理対象では D SMF 全体状態をz/OS MVS Operationsの確認記録に残し、対象名は出力整理対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 変更照合の全体状態に関する D SMF 全体状態の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更照合の全体状態の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更照合の全体状態の証跡として保存して根拠にする。</li><li>C. D SMF 全体状態の変更点を出力本文から切り離して変更照合の全体状態の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、変更照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更照合の全体状態において選択記号 D を採用し、識別名は変更照合です。変更照合の全体状態において D SMF 全体状態 は説明欄の「D SMF 全体状態の状態と出力メッセージを結び付ける変更照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合の全体状態に関する記録は、D SMF 全体状態の出力行と IEE115I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合の全体状態は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更照合ではありません。 B: 変更照合の全体状態は別カテゴリの確認を流用しており、D SMF 全体状態の根拠にならないため変更照合ではありません。 C: 変更照合の全体状態は名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合の全体状態は対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合の全体状態で記録する D SMF 全体状態はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SMF 全体状態</strong></p><p>検証目的: 呼出整理の全体状態について、D SMF 全体状態は、SMF の稼働モード (LOGSTREAM / MAN データセット) と現行アクティブ・データセット番号、書込み状況を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010103の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出整理の全体状態の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SMF 全体状態を指定し、OSKB010103の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SMF 全体状態
CASE OSKB010103
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SMF 全体状態
CASE OSKB010103
SOURCE z/OS MVS Operations
D SMF 全体状態とOSKB010103が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010103を同じ出力で読み、呼出整理の全体状態の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010103
→ Enter を押す
［画面・出力］
IEE115I OSKB010103 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010103   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010103が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SMF 全体状態 と OSKB010103 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010103 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0123"><h3>D SMF,LOGSTREAM</h3><p class="kb-meta">分類: D SMF ・ 難易度: 上級</p><p>D SMF,LOGSTREAMは、LOGSTREAM モードで稼働している SMF Logger ストリーム名・接続状況を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲整理の操作コマンドで操作コマンドの運用確認を行います。D SMF,LOGSTREAM の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲整理の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲整理の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、範囲整理の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D SMF,LOGSTREAM の属性行を読まず範囲整理の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲整理正解では選択記号 C を採用し、正解名は範囲整理正解です。範囲整理根拠では D SMF,LOGSTREAM は「z/OS MVS Operationsで D SMF,LOGSTREAM の扱いを記録する範囲整理項目」と D A,L または該当パネルの出力を照合し、根拠名は範囲整理根拠です。範囲整理受渡では D SMF,LOGSTREAM の表示結果と IEE115I を同じ確認単位にし、受渡名は範囲整理受渡です。不適切な選択肢を整理します。 A: 範囲整理流用は別カテゴリの確認であり、排除名は範囲整理流用です。 B: 範囲整理欠落は戻り値や記録番号に寄り、欠落名は範囲整理欠落です。 C: 範囲整理正答は対象出力と項目説明を結び、根拠名は範囲整理正答です。 D: 範囲整理不足は名称や説明だけに寄り、判定名は範囲整理不足です。範囲整理資料では D SMF,LOGSTREAM の使い方を出典欄から追跡し、資料名は範囲整理資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出追跡の操作コマンドで操作コマンドの運用確認を行います。D SMF,LOGSTREAM の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出追跡の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D SMF,LOGSTREAM の属性行を読まず呼出追跡の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出追跡の操作コマンドにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡の操作コマンドにおいて D SMF,LOGSTREAM は説明欄の「z/OS MVS Operationsで D SMF,LOGSTREAM の扱いを記録する呼出追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡の操作コマンドを受け取る担当者は、D SMF,LOGSTREAM の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡の操作コマンドは別カテゴリの確認を流用しており、D SMF,LOGSTREAM の根拠にならないため呼出追跡ではありません。 B: 呼出追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡の操作コマンドが示す D SMF,LOGSTREAM は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SMF,LOGSTREAM</strong></p><p>検証目的: 探索整理の操作コマンドについて、D SMF,LOGSTREAM は、LOGSTREAM モードで稼働している SMF Logger ストリーム名・接続状況を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010106の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、探索整理の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SMF,LOGSTREAMを指定し、OSKB010106の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SMF,LOGSTREAM
CASE OSKB010106
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SMF,LOGSTREAM
CASE OSKB010106
SOURCE z/OS MVS Operations
D SMF,LOGSTREAMとOSKB010106が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010106を同じ出力で読み、探索整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010106
→ Enter を押す
［画面・出力］
IEE115I OSKB010106 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010106   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010106が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SMF,LOGSTREAM と OSKB010106 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010106 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0124"><h3>D SMF,O オプション</h3><p class="kb-meta">分類: D SMF ・ 難易度: 上級</p><p>D SMF,O オプションは、SMFPRMxx の現有効値 (記録レコード番号, BUFUSEWARN, NOBUFFS 等) を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件整理のオプションに関係する D SMF,O オプションの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、条件整理として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D SMF,O オプションの名称と担当者名だけを残して条件整理のオプションの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件整理のオプションを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件整理のオプションの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件整理正解では選択記号 A を採用し、正解名は条件整理正解です。条件整理根拠では D SMF,O オプション は「D SMF,O オプションの用途を操作コマンドの表示で確認する条件整理項目」と D A,L または該当パネルの出力を照合し、根拠名は条件整理根拠です。条件整理背景ではz/OS MVS Operationsの D SMF,O オプションと IEE115I を同じ証跡に残し、背景名は条件整理背景です。他の選択肢を確認します。 A: 条件整理正答は対象出力と項目説明を結び、根拠名は条件整理正答です。 B: 条件整理不足は名称や説明だけに寄り、判定名は条件整理不足です。 C: 条件整理流用は別カテゴリの確認であり、排除名は条件整理流用です。 D: 条件整理欠落は戻り値や記録番号に寄り、欠落名は条件整理欠落です。条件整理用語では D SMF,O オプションを MVS オペレータコマンドで扱う確認対象とし、用語名は条件整理用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文追跡のオプションに関係する D SMF,O オプションの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D SMF,O オプションの名称と担当者名のみを残して構文追跡のオプションの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文追跡のオプションを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文追跡のオプションの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文追跡のオプションにおいて選択記号 A を採用し、識別名は構文追跡です。構文追跡のオプションにおいて D SMF,O オプション は説明欄の「D SMF,O オプションの用途を操作コマンドの表示で確認する構文追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡のオプションに関連して、z/OS MVS Operationsでは D SMF,O オプションの表示属性と IEE115I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡のオプションは対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡のオプションは名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡のオプションは別カテゴリの確認を流用しており、D SMF,O オプションの根拠にならないため構文追跡ではありません。 D: 構文追跡のオプションは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文追跡ではありません。構文追跡のオプションで使う D SMF,O オプションという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SMF,O オプション</strong></p><p>検証目的: 監査確認のオプションについて、D SMF,O オプションは、SMFPRMxx の現有効値 (記録レコード番号, BUFUSEWARN, NOBUFFS 等) を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040019の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査確認のオプションの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SMF,O オプションを指定し、OSKB040019の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SMF,O オプション
CASE OSKB040019
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SMF,O オプション
CASE OSKB040019
SOURCE z/OS MVS Operations
D SMF,O オプションとOSKB040019が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040019を同じ出力で読み、監査確認のオプションの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040019
→ Enter を押す
［画面・出力］
IEE115I OSKB040019 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040019   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040019が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SMF,O オプション と OSKB040019 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040019 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D SMF,O オプション</strong></p><p>検証目的: 置換整理のオプションについて、D SMF,O オプションは、SMFPRMxx の現有効値 (記録レコード番号, BUFUSEWARN, NOBUFFS 等) を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010104の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換整理のオプションの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SMF,O オプションを指定し、OSKB010104の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SMF,O オプション
CASE OSKB010104
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SMF,O オプション
CASE OSKB010104
SOURCE z/OS MVS Operations
D SMF,O オプションとOSKB010104が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010104を同じ出力で読み、置換整理のオプションの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010104
→ Enter を押す
［画面・出力］
IEE115I OSKB010104 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010104   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010104が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SMF,O オプション と OSKB010104 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010104 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0125"><h3>D SMF,S データセット</h3><p class="kb-meta">分類: D SMF ・ 難易度: 上級</p><p>MAN1〜MANn の状態 (ACTIVE/ALTERNATE/DUMP REQUIRED/EMPTY) と容量充足率を表示。SMF データ喪失検出に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切整理のデータセットで D SMF,S データセットの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D SMF,S データセットの出力を取らず区切整理のデータセットの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切整理の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切整理のデータセットの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切整理のデータセットへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切整理正解では選択記号 B を採用し、正解名は区切整理正解です。区切整理根拠では D SMF,S データセット は「区切整理のデータセットに関係する定義値と表示行を照合する区切整理項目」と D A,L または該当パネルの出力を照合し、根拠名は区切整理根拠です。区切整理追跡では D SMF,S データセットの属性行と IEE115I を合わせ、追跡名は区切整理追跡です。誤答側の問題点を分けます。 A: 区切整理不足は名称や説明だけに寄り、判定名は区切整理不足です。 B: 区切整理正答は対象出力と項目説明を結び、根拠名は区切整理正答です。 C: 区切整理欠落は戻り値や記録番号に寄り、欠落名は区切整理欠落です。 D: 区切整理流用は別カテゴリの確認であり、排除名は区切整理流用です。区切整理初出では D SMF,S データセットを MVS オペレータコマンドの運用手順で確認し、初出名は区切整理初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開追跡のデータセットで D SMF,S データセットの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D SMF,S データセットの出力を取らず展開追跡のデータセットの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開追跡のデータセットの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開追跡のデータセットへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開追跡のデータセットにおいて選択記号 B を採用し、識別名は展開追跡です。展開追跡のデータセットにおいて D SMF,S データセット は説明欄の「展開追跡のデータセットに関係する定義値と表示行を照合する展開追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡のデータセットの証跡を読む担当者は、D SMF,S データセットの属性行と IEE115I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡のデータセットは名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡のデータセットは対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡のデータセットは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡のデータセットは別カテゴリの確認を流用しており、D SMF,S データセットの根拠にならないため展開追跡ではありません。展開追跡のデータセットに出る D SMF,S データセットは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SMF,S データセット</strong></p><p>検証目的: 終端整理のデータセットについて、MAN1〜MANn の状態 (ACTIVE/ALTERNATE/DUMP REQUIRED/EMPTY) と容量充足率を表示。SMF データ喪失検出に使うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010105の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端整理のデータセットの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SMF,S データセットを指定し、OSKB010105の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SMF,S データセット
CASE OSKB010105
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SMF,S データセット
CASE OSKB010105
SOURCE z/OS MVS Operations
D SMF,S データセットとOSKB010105が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010105を同じ出力で読み、終端整理のデータセットの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010105
→ Enter を押す
［画面・出力］
IEE115I OSKB010105 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010105   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010105が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SMF,S データセット と OSKB010105 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010105 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D SMS


<section class="kb-item" id="c22-i0126"><h3>D SMS,CACHE キャッシュ</h3><p class="kb-meta">分類: D SMS ・ 難易度: 中級</p><p>D SMS,CACHE キャッシュは、MVS オペレータコマンドのD SMSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域整理のキャッシュに関する D SMS 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域整理のキャッシュの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域整理のキャッシュの証跡として保存して根拠にする。</li><li>C. D SMS 命令の変更点を出力本文から切り離して値域整理のキャッシュの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、値域整理の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域整理正解では選択記号 D を採用し、正解名は値域整理正解です。値域整理根拠では D SMS 命令 は「D SMS 命令の状態と出力メッセージを結び付ける値域整理項目」と D A,L または該当パネルの出力を照合し、根拠名は値域整理根拠です。値域整理保存では D SMS 命令の出力行と IEE115I を一緒に残し、保存名は値域整理保存です。選択肢ごとの違いを示します。 A: 値域整理欠落は戻り値や記録番号に寄り、欠落名は値域整理欠落です。 B: 値域整理流用は別カテゴリの確認であり、排除名は値域整理流用です。 C: 値域整理不足は名称や説明だけに寄り、判定名は値域整理不足です。 D: 値域整理正答は対象出力と項目説明を結び、根拠名は値域整理正答です。値域整理対象では D SMS 命令をz/OS MVS Operationsの確認記録に残し、対象名は値域整理対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力追跡のキャッシュに関する D SMS,CACHE キャッシュの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力追跡のキャッシュの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力追跡のキャッシュの証跡として保存して根拠にする。</li><li>C. D SMS,CACHE キャッシュの変更点を出力本文から切り離して出力追跡のキャッシュの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力追跡のキャッシュにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡のキャッシュにおいて D SMS,CACHE キャッシュ は説明欄の「D SMS,CACHE キャッシュの状態と出力メッセージを結び付ける出力追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡のキャッシュに関する記録は、D SMS,CACHE キャッシュの出力行と IEE115I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡のキャッシュは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡のキャッシュは別カテゴリの確認を流用しており、D SMS,CACHE キャッシュの根拠にならないため出力追跡ではありません。 C: 出力追跡のキャッシュは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡のキャッシュは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡のキャッシュで記録する D SMS,CACHE キャッシュはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SMS,CACHE キャッシュ</strong></p><p>検証目的: 範囲整理のキャッシュについて、D SMS,CACHE キャッシュは、MVS オペレータコマンドの D SMS で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010111の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲整理のキャッシュの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SMS,CACHE キャッシュを指定し、OSKB010111の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SMS,CACHE キャッシュ
CASE OSKB010111
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SMS,CACHE キャッシュ
CASE OSKB010111
SOURCE z/OS MVS Operations
D SMS,CACHE キャッシュとOSKB010111が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010111を同じ出力で読み、範囲整理のキャッシュの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010111
→ Enter を押す
［画面・出力］
IEE115I OSKB010111 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010111   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010111が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SMS,CACHE キャッシュ と OSKB010111 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010111 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0127"><h3>D SMS,OPTIONS</h3><p class="kb-meta">分類: D SMS ・ 難易度: 中級</p><p>D SMS,OPTIONSは、現行アクティブ SCDS、ACS ルーチンの活性レベル、TRACE 設定、ACSDEFAULTS を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先整理の操作コマンドに関する D SMS,OPTIONS の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先整理の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先整理の操作コマンドの証跡として保存して根拠にする。</li><li>C. D SMS,OPTIONS の変更点を出力本文から切り離して優先整理の操作コマンドの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先整理で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先整理正解では選択記号 D を採用し、正解名は優先整理正解です。優先整理根拠では D SMS,OPTIONS は「D SMS,OPTIONS の状態と出力メッセージを結び付ける優先整理項目」と D A,L または該当パネルの出力を照合し、根拠名は優先整理根拠です。優先整理保存では D SMS,OPTIONS の出力行と IEE115I を一緒に残し、保存名は優先整理保存です。選択肢ごとの違いを示します。 A: 優先整理欠落は戻り値や記録番号に寄り、欠落名は優先整理欠落です。 B: 優先整理流用は別カテゴリの確認であり、排除名は優先整理流用です。 C: 優先整理不足は名称や説明だけに寄り、判定名は優先整理不足です。 D: 優先整理正答は対象出力と項目説明を結び、根拠名は優先整理正答です。優先整理対象では D SMS,OPTIONS をz/OS MVS Operationsの確認記録に残し、対象名は優先整理対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換追跡の操作コマンドに関する D SMS,OPTIONS の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換追跡の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換追跡の操作コマンドの証跡として保存して根拠にする。</li><li>C. D SMS,OPTIONS の変更点を出力本文から切り離して置換追跡の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換追跡の操作コマンドにおいて選択記号 D を採用し、識別名は置換追跡です。置換追跡の操作コマンドにおいて D SMS,OPTIONS は説明欄の「D SMS,OPTIONS の状態と出力メッセージを結び付ける置換追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の操作コマンドに関する記録は、D SMS,OPTIONS の出力行と IEE115I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の操作コマンドは別カテゴリの確認を流用しており、D SMS,OPTIONS の根拠にならないため置換追跡ではありません。 C: 置換追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の操作コマンドで記録する D SMS,OPTIONS はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SMS,OPTIONS</strong></p><p>検証目的: 上書整理の操作コマンドについて、D SMS,OPTIONS は、現行アクティブ SCDS、ACS ルーチンの活性レベル、TRACE 設定、ACSDEFAULTS を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010107の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書整理の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SMS,OPTIONSを指定し、OSKB010107の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SMS,OPTIONS
CASE OSKB010107
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SMS,OPTIONS
CASE OSKB010107
SOURCE z/OS MVS Operations
D SMS,OPTIONSとOSKB010107が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010107を同じ出力で読み、上書整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010107
→ Enter を押す
［画面・出力］
IEE115I OSKB010107 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010107   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010107が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SMS,OPTIONS と OSKB010107 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010107 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0128"><h3>D SMS,SCDS</h3><p class="kb-meta">分類: D SMS ・ 難易度: 中級</p><p>D SMS,SCDSは、MVS オペレータコマンドのD SMSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録整理の操作コマンドに関係する D SMS,SCDS の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、記録整理の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D SMS,SCDS の名称と担当者名だけを残して記録整理の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録整理の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録整理の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録整理正解では選択記号 A を採用し、正解名は記録整理正解です。記録整理根拠では D SMS,SCDS は「D SMS,SCDS の用途を操作コマンドの表示で確認する記録整理項目」と D A,L または該当パネルの出力を照合し、根拠名は記録整理根拠です。記録整理背景ではz/OS MVS Operationsの D SMS,SCDS と IEE115I を同じ証跡に残し、背景名は記録整理背景です。他の選択肢を確認します。 A: 記録整理正答は対象出力と項目説明を結び、根拠名は記録整理正答です。 B: 記録整理不足は名称や説明だけに寄り、判定名は記録整理不足です。 C: 記録整理流用は別カテゴリの確認であり、排除名は記録整理流用です。 D: 記録整理欠落は戻り値や記録番号に寄り、欠落名は記録整理欠落です。記録整理用語では D SMS,SCDS を MVS オペレータコマンドで扱う確認対象とし、用語名は記録整理用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端追跡の操作コマンドに関係する D SMS,SCDS の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D SMS,SCDS の名称と担当者名のみを残して終端追跡の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端追跡の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端追跡の操作コマンドにおいて選択記号 A を採用し、識別名は終端追跡です。終端追跡の操作コマンドにおいて D SMS,SCDS は説明欄の「D SMS,SCDS の用途を操作コマンドの表示で確認する終端追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡の操作コマンドに関連して、z/OS MVS Operationsでは D SMS,SCDS の表示属性と IEE115I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡の操作コマンドは別カテゴリの確認を流用しており、D SMS,SCDS の根拠にならないため終端追跡ではありません。 D: 終端追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端追跡ではありません。終端追跡の操作コマンドで使う D SMS,SCDS という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SMS,SCDS</strong></p><p>検証目的: 出力整理の操作コマンドについて、D SMS,SCDS は、MVS オペレータコマンドの D SMS で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認しますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010108の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力整理の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SMS,SCDSを指定し、OSKB010108の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SMS,SCDS
CASE OSKB010108
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SMS,SCDS
CASE OSKB010108
SOURCE z/OS MVS Operations
D SMS,SCDSとOSKB010108が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010108を同じ出力で読み、出力整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010108
→ Enter を押す
［画面・出力］
IEE115I OSKB010108 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010108   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010108が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SMS,SCDS と OSKB010108 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010108 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0129"><h3>D SMS,SG ストレージグループ</h3><p class="kb-meta">分類: D SMS ・ 難易度: 中級</p><p>D SMS,SG ストレージグループは、全 SG の状態 (ENABLE/QUIESCE NEW/QUIESCE/DISABLE) と関連 VOLUME 数を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較整理のストレージグループで D SMS 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D SMS 命令の出力を取らず比較整理のストレージグループの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて比較整理の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較整理のストレージグループの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較整理のストレージグループへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較整理正解では選択記号 B を採用し、正解名は比較整理正解です。比較整理根拠では D SMS 命令 は「比較整理のストレージグループに関係する定義値と表示行を照合する比較整理項目」と D A,L または該当パネルの出力を照合し、根拠名は比較整理根拠です。比較整理追跡では D SMS 命令の属性行と IEE115I を合わせ、追跡名は比較整理追跡です。誤答側の問題点を分けます。 A: 比較整理不足は名称や説明だけに寄り、判定名は比較整理不足です。 B: 比較整理正答は対象出力と項目説明を結び、根拠名は比較整理正答です。 C: 比較整理欠落は戻り値や記録番号に寄り、欠落名は比較整理欠落です。 D: 比較整理流用は別カテゴリの確認であり、排除名は比較整理流用です。比較整理初出では D SMS 命令を MVS オペレータコマンドの運用手順で確認し、初出名は比較整理初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索追跡のストレージグループで D SMS,SG ストレージグループの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D SMS,SG ストレージグループの出力を取らず探索追跡のストレージグループの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索追跡のストレージグループの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索追跡のストレージグループへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索追跡のストレージグループにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡のストレージグループにおいて D SMS,SG ストレージグループ は説明欄の「探索追跡のストレージグループに関係する定義値と表示行を照合する探索追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡のストレージグループの証跡を読む担当者は、D SMS,SG ストレージグループの属性行と IEE115I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡のストレージグループは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡のストレージグループは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡のストレージグループは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡のストレージグループは別カテゴリの確認を流用しており、D SMS,SG ストレージグループの根拠にならないため探索追跡ではありません。探索追跡のストレージグループに出る D SMS,SG ストレージグループは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SMS,SG ストレージグループ</strong></p><p>検証目的: 条件整理のストレージグループについて、D SMS,SG ストレージグループは、全 SG の状態 (ENABLE/QUIESCE NEW/QUIESCE/DISABLE) と関連 VOLUME 数を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010109の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件整理のストレージグループの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SMS,SG ストレージグループを指定し、OSKB010109の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SMS,SG ストレージグループ
CASE OSKB010109
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SMS,SG ストレージグループ
CASE OSKB010109
SOURCE z/OS MVS Operations
D SMS,SG ストレージグループとOSKB010109が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010109を同じ出力で読み、条件整理のストレージグループの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010109
→ Enter を押す
［画面・出力］
IEE115I OSKB010109 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010109   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010109が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SMS,SG ストレージグループ と OSKB010109 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010109 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0130"><h3>D SMS,VOL=ser</h3><p class="kb-meta">分類: D SMS ・ 難易度: 中級</p><p>D SMS,VOL=serは、MVS オペレータコマンドのD SMSで確認する項目です。指定ボリュームの SMS 管理状態、SG 所属、フリースペースを表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序整理の操作コマンドで操作コマンドの運用確認を行います。D SMS,VOL=serの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序整理の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序整理の操作コマンドを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を順序整理で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D SMS,VOL=serの属性行を読まず順序整理の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序整理正解では選択記号 C を採用し、正解名は順序整理正解です。順序整理根拠では D SMS,VOL=ser は「z/OS MVS Operationsで D SMS,VOL=serの扱いを記録する順序整理項目」と D A,L または該当パネルの出力を照合し、根拠名は順序整理根拠です。順序整理受渡では D SMS,VOL=serの表示結果と IEE115I を同じ確認単位にし、受渡名は順序整理受渡です。不適切な選択肢を整理します。 A: 順序整理流用は別カテゴリの確認であり、排除名は順序整理流用です。 B: 順序整理欠落は戻り値や記録番号に寄り、欠落名は順序整理欠落です。 C: 順序整理正答は対象出力と項目説明を結び、根拠名は順序整理正答です。 D: 順序整理不足は名称や説明だけに寄り、判定名は順序整理不足です。順序整理資料では D SMS,VOL=serの使い方を出典欄から追跡し、資料名は順序整理資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書追跡の操作コマンドで操作コマンドの運用確認を行います。D SMS,VOL=serの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書追跡の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D SMS,VOL=serの属性行を読まず上書追跡の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書追跡の操作コマンドにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡の操作コマンドにおいて D SMS,VOL=ser は説明欄の「z/OS MVS Operationsで D SMS,VOL=serの扱いを記録する上書追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡の操作コマンドを受け取る担当者は、D SMS,VOL=serの表示結果と IEE115I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡の操作コマンドは別カテゴリの確認を流用しており、D SMS,VOL=serの根拠にならないため上書追跡ではありません。 B: 上書追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡の操作コマンドが示す D SMS,VOL=serは出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SMS,VOL=ser</strong></p><p>検証目的: 変更確認の操作コマンドについて、D SMS,VOL=serは、MVS オペレータコマンドの D SMS で確認する項目です。指定ボリュームの SMS 管理状態、SG 所属、フリースペースを表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040020の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SMS,VOL=serを指定し、OSKB040020の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SMS,VOL=ser
CASE OSKB040020
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SMS,VOL=ser
CASE OSKB040020
SOURCE z/OS MVS Operations
D SMS,VOL=serとOSKB040020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040020を同じ出力で読み、変更確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040020
→ Enter を押す
［画面・出力］
IEE115I OSKB040020 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040020   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SMS,VOL=ser と OSKB040020 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D SMS,VOL=ser</strong></p><p>検証目的: 区切整理の操作コマンドについて、D SMS,VOL=serは、MVS オペレータコマンドの D SMS で確認する項目です。指定ボリュームの SMS 管理状態、SG 所属、フリースペースを表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010110の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切整理の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SMS,VOL=serを指定し、OSKB010110の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SMS,VOL=ser
CASE OSKB010110
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SMS,VOL=ser
CASE OSKB010110
SOURCE z/OS MVS Operations
D SMS,VOL=serとOSKB010110が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010110を同じ出力で読み、区切整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010110
→ Enter を押す
［画面・出力］
IEE115I OSKB010110 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010110   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010110が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SMS,VOL=ser と OSKB010110 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010110 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D SQA


<section class="kb-item" id="c22-i0131"><h3>D SQA 目的</h3><p class="kb-meta">分類: D SQA ・ 難易度: 初級</p><p>SQA / ESQA の現使用量 (BYTES / 残量) を表示。CSA/SQA 枯渇調査の補助。D U,IPLPARM,SQA や RMF と組み合わせて分析する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告整理の目的に関係する D SQA 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、警告整理の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D SQA 目的の名称と担当者名だけを残して警告整理の目的の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告整理の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告整理の目的の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 警告整理正解では選択記号 A を採用し、正解名は警告整理正解です。警告整理根拠では D SQA 目的 は「D SQA 目的の用途を操作コマンドの表示で確認する警告整理項目」と D A,L または該当パネルの出力を照合し、根拠名は警告整理根拠です。警告整理背景ではz/OS MVS Operationsの D SQA 目的と IEE115I を同じ証跡に残し、背景名は警告整理背景です。他の選択肢を確認します。 A: 警告整理正答は対象出力と項目説明を結び、根拠名は警告整理正答です。 B: 警告整理不足は名称や説明だけに寄り、判定名は警告整理不足です。 C: 警告整理流用は別カテゴリの確認であり、排除名は警告整理流用です。 D: 警告整理欠落は戻り値や記録番号に寄り、欠落名は警告整理欠落です。警告整理用語では D SQA 目的を MVS オペレータコマンドで扱う確認対象とし、用語名は警告整理用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件追跡の目的に関係する D SQA 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D SQA 目的の名称と担当者名のみを残して条件追跡の目的の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件追跡の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件追跡の目的の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 条件追跡の目的において選択記号 A を採用し、識別名は条件追跡です。条件追跡の目的において D SQA 目的 は説明欄の「D SQA 目的の用途を操作コマンドの表示で確認する条件追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の目的に関連して、z/OS MVS Operationsでは D SQA 目的の表示属性と IEE115I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の目的は対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の目的は別カテゴリの確認を流用しており、D SQA 目的の根拠にならないため条件追跡ではありません。 D: 条件追跡の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件追跡ではありません。条件追跡の目的で使う D SQA 目的という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SQA 目的</strong></p><p>検証目的: 優先整理の目的について、SQA / ESQA の現使用量 (BYTES / 残量) を表示。CSA/SQA 枯渇調査の補助。D U,IPLPARM,SQA や RMF と組み合わせて分析するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010112の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先整理の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SQA 目的を指定し、OSKB010112の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SQA 目的
CASE OSKB010112
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SQA 目的
CASE OSKB010112
SOURCE z/OS MVS Operations
D SQA 目的とOSKB010112が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010112を同じ出力で読み、優先整理の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010112
→ Enter を押す
［画面・出力］
IEE115I OSKB010112 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010112   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010112が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SQA 目的 と OSKB010112 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010112 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D SSI


<section class="kb-item" id="c22-i0132"><h3>D SSI サブシステム一覧</h3><p class="kb-meta">分類: D SSI ・ 難易度: 中級</p><p>D SSI サブシステム一覧は、IEFSSNxx で定義されたサブシステム (JES2, RACF, DB2, CICS など) の SSI 状態を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧整理のサブシステム一覧で D SSI サブシステム一覧の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D SSI サブシステム一覧の出力を取らず復旧整理のサブシステム一覧の説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて復旧整理の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧整理のサブシステム一覧の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧整理のサブシステム一覧へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧整理正解では選択記号 B を採用し、正解名は復旧整理正解です。復旧整理根拠では D SSI サブシステム一覧 は「復旧整理のサブシステム一覧に関係する定義値と表示行を照合する復旧整理項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧整理根拠です。復旧整理追跡では D SSI サブシステム一覧の属性行と IEE115I を合わせ、追跡名は復旧整理追跡です。誤答側の問題点を分けます。 A: 復旧整理不足は名称や説明だけに寄り、判定名は復旧整理不足です。 B: 復旧整理正答は対象出力と項目説明を結び、根拠名は復旧整理正答です。 C: 復旧整理欠落は戻り値や記録番号に寄り、欠落名は復旧整理欠落です。 D: 復旧整理流用は別カテゴリの確認であり、排除名は復旧整理流用です。復旧整理初出では D SSI サブシステム一覧を MVS オペレータコマンドの運用手順で確認し、初出名は復旧整理初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切追跡のサブシステム一覧で D SSI サブシステム一覧の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D SSI サブシステム一覧の出力を取らず区切追跡のサブシステム一覧の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切追跡のサブシステム一覧の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切追跡のサブシステム一覧へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切追跡のサブシステム一覧において選択記号 B を採用し、識別名は区切追跡です。区切追跡のサブシステム一覧において D SSI サブシステム一覧 は説明欄の「区切追跡のサブシステム一覧に関係する定義値と表示行を照合する区切追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡のサブシステム一覧の証跡を読む担当者は、D SSI サブシステム一覧の属性行と IEE115I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡のサブシステム一覧は名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡のサブシステム一覧は対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡のサブシステム一覧は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡のサブシステム一覧は別カテゴリの確認を流用しており、D SSI サブシステム一覧の根拠にならないため区切追跡ではありません。区切追跡のサブシステム一覧に出る D SSI サブシステム一覧は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SSI サブシステム一覧</strong></p><p>検証目的: 記録整理のサブシステム一覧について、D SSI サブシステム一覧は、IEFSSNxx で定義されたサブシステム (JES2, RACF, DB2, CICS など) の SSI 状態を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010113の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録整理のサブシステム一覧の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SSI サブシステム一覧を指定し、OSKB010113の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SSI サブシステム一覧
CASE OSKB010113
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SSI サブシステム一覧
CASE OSKB010113
SOURCE z/OS MVS Operations
D SSI サブシステム一覧とOSKB010113が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010113を同じ出力で読み、記録整理のサブシステム一覧の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010113
→ Enter を押す
［画面・出力］
IEE115I OSKB010113 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010113   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010113が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SSI サブシステム一覧 と OSKB010113 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010113 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0133"><h3>D SSI,ALL,SUB=name</h3><p class="kb-meta">分類: D SSI ・ 難易度: 中級</p><p>D SSI,ALL,SUB=nameは、指定サブシステム名 (例: JES2) の SSI 関数番号、所有モジュールを詳細表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査整理の操作コマンドで操作コマンドの運用確認を行います。D SSI 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査整理の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査整理の操作コマンドを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、監査整理の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D SSI 命令の属性行を読まず監査整理の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査整理正解では選択記号 C を採用し、正解名は監査整理正解です。監査整理根拠では D SSI 命令 は「z/OS MVS Operationsで D SSI 命令の扱いを記録する監査整理項目」と D A,L または該当パネルの出力を照合し、根拠名は監査整理根拠です。監査整理受渡では D SSI 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は監査整理受渡です。不適切な選択肢を整理します。 A: 監査整理流用は別カテゴリの確認であり、排除名は監査整理流用です。 B: 監査整理欠落は戻り値や記録番号に寄り、欠落名は監査整理欠落です。 C: 監査整理正答は対象出力と項目説明を結び、根拠名は監査整理正答です。 D: 監査整理不足は名称や説明だけに寄り、判定名は監査整理不足です。監査整理資料では D SSI 命令の使い方を出典欄から追跡し、資料名は監査整理資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文確認の操作コマンドに関係する D SSI,ALL,SUB=nameの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D SSI,ALL,SUB=nameの名称と担当者名のみを残して構文確認の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文確認の操作コマンドにおいて選択記号 A を採用し、識別名は構文確認です。構文確認の操作コマンドにおいて D SSI,ALL,SUB=name は説明欄の「D SSI,ALL,SUB=nameの用途を操作コマンドの表示で確認する構文確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認の操作コマンドに関連して、z/OS MVS Operationsでは D SSI,ALL,SUB=nameの表示属性と IEE115I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認の操作コマンドは別カテゴリの確認を流用しており、D SSI,ALL,SUB=nameの根拠にならないため構文確認ではありません。 D: 構文確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文確認ではありません。構文確認の操作コマンドで使う D SSI,ALL,SUB=nameという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SSI,ALL,SUB=name</strong></p><p>検証目的: 比較整理の操作コマンドについて、D SSI,ALL,SUB=nameは、指定サブシステム名 (例: JES2) の SSI 関数番号、所有モジュールを詳細表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010114の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較整理の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD SSI,ALL,SUB=nameを指定し、OSKB010114の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SSI,ALL,SUB=name
CASE OSKB010114
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SSI,ALL,SUB=name
CASE OSKB010114
SOURCE z/OS MVS Operations
D SSI,ALL,SUB=nameとOSKB010114が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010114を同じ出力で読み、比較整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010114
→ Enter を押す
［画面・出力］
IEE115I OSKB010114 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010114   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010114が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SSI,ALL,SUB=name と OSKB010114 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010114 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D T


<section class="kb-item" id="c22-i0134"><h3>D T 現在時刻</h3><p class="kb-meta">分類: D T ・ 難易度: 中級</p><p>D T 現在時刻は、MVS オペレータコマンドのD Tで確認する項目です。システムの現在時刻、TOD クロック、ローカル時差を表示。最短記法 (1 字コマンド) で使用頻度が高い</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更整理の現在時刻に関する D T 現在時刻の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更整理の現在時刻の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更整理の現在時刻の証跡として保存して根拠にする。</li><li>C. D T 現在時刻の変更点を出力本文から切り離して変更整理の現在時刻の承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、変更整理の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更整理正解では選択記号 D を採用し、正解名は変更整理正解です。変更整理根拠では D T 現在時刻 は「D T 現在時刻の状態と出力メッセージを結び付ける変更整理項目」と D A,L または該当パネルの出力を照合し、根拠名は変更整理根拠です。変更整理保存では D T 現在時刻の出力行と IEE115I を一緒に残し、保存名は変更整理保存です。選択肢ごとの違いを示します。 A: 変更整理欠落は戻り値や記録番号に寄り、欠落名は変更整理欠落です。 B: 変更整理流用は別カテゴリの確認であり、排除名は変更整理流用です。 C: 変更整理不足は名称や説明だけに寄り、判定名は変更整理不足です。 D: 変更整理正答は対象出力と項目説明を結び、根拠名は変更整理正答です。変更整理対象では D T 現在時刻をz/OS MVS Operationsの確認記録に残し、対象名は変更整理対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開確認の現在時刻で D T 現在時刻の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D T 現在時刻の出力を取らず展開確認の現在時刻の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開確認の現在時刻の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開確認の現在時刻へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開確認の現在時刻において選択記号 B を採用し、識別名は展開確認です。展開確認の現在時刻において D T 現在時刻 は説明欄の「展開確認の現在時刻に関係する定義値と表示行を照合する展開確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認の現在時刻の証跡を読む担当者は、D T 現在時刻の属性行と IEE115I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認の現在時刻は名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認の現在時刻は対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認の現在時刻は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開確認ではありません。 D: 展開確認の現在時刻は別カテゴリの確認を流用しており、D T 現在時刻の根拠にならないため展開確認ではありません。展開確認の現在時刻に出る D T 現在時刻は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D T 現在時刻</strong></p><p>検証目的: 順序整理の現在時刻について、D T 現在時刻は、MVS オペレータコマンドの D T で確認する項目です。システムの現在時刻、TOD クロック、ローカル時差を表示。最短記法 (1 字コマンド) で使用頻度に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010115の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序整理の現在時刻の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD T 現在時刻を指定し、OSKB010115の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D T 現在時刻
CASE OSKB010115
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D T 現在時刻
CASE OSKB010115
SOURCE z/OS MVS Operations
D T 現在時刻とOSKB010115が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010115を同じ出力で読み、順序整理の現在時刻の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010115
→ Enter を押す
［画面・出力］
IEE115I OSKB010115 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010115   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010115が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D T 現在時刻 と OSKB010115 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010115 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D TRACE


<section class="kb-item" id="c22-i0135"><h3>D TRACE 目的</h3><p class="kb-meta">分類: D TRACE ・ 難易度: 上級</p><p>D TRACE 目的は、MVS オペレータコマンドのD TRACEで確認する項目です。システム・トレース、GTF、コンポーネント・トレースの稼動状況サマリを表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文記録の目的に関係する D TRACE 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、構文記録として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D TRACE 目的の名称と担当者名だけを残して構文記録の目的の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文記録の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文記録の目的の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文記録正解では選択記号 A を採用し、正解名は構文記録正解です。構文記録根拠では D TRACE 目的 は「D TRACE 目的の用途を操作コマンドの表示で確認する構文記録項目」と D A,L または該当パネルの出力を照合し、根拠名は構文記録根拠です。構文記録背景ではz/OS MVS Operationsの D TRACE 目的と IEE115I を同じ証跡に残し、背景名は構文記録背景です。他の選択肢を確認します。 A: 構文記録正答は対象出力と項目説明を結び、根拠名は構文記録正答です。 B: 構文記録不足は名称や説明だけに寄り、判定名は構文記録不足です。 C: 構文記録流用は別カテゴリの確認であり、排除名は構文記録流用です。 D: 構文記録欠落は戻り値や記録番号に寄り、欠落名は構文記録欠落です。構文記録用語では D TRACE 目的を MVS オペレータコマンドで扱う確認対象とし、用語名は構文記録用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出確認の目的で操作コマンドの運用確認を行います。D TRACE 目的の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出確認の目的を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出確認の目的を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D TRACE 目的の属性行を読まず呼出確認の目的の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出確認の目的において選択記号 C を採用し、識別名は呼出確認です。呼出確認の目的において D TRACE 目的 は説明欄の「z/OS MVS Operationsで D TRACE 目的の扱いを記録する呼出確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認の目的を受け取る担当者は、D TRACE 目的の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認の目的は別カテゴリの確認を流用しており、D TRACE 目的の根拠にならないため呼出確認ではありません。 B: 呼出確認の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認の目的は対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認の目的が示す D TRACE 目的は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D TRACE 目的</strong></p><p>検証目的: 構文照合の目的について、D TRACE 目的は、MVS オペレータコマンドの D TRACE で確認する項目です。システム・トレース、GTF、コンポーネント・トレースの稼動状況サマリを表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040021の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文照合の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD TRACE 目的を指定し、OSKB040021の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D TRACE 目的
CASE OSKB040021
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D TRACE 目的
CASE OSKB040021
SOURCE z/OS MVS Operations
D TRACE 目的とOSKB040021が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040021を同じ出力で読み、構文照合の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040021
→ Enter を押す
［画面・出力］
IEE115I OSKB040021 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040021   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040021が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D TRACE 目的 と OSKB040021 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040021 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D TRACE 目的</strong></p><p>検証目的: 値域整理の目的について、D TRACE 目的は、MVS オペレータコマンドの D TRACE で確認する項目です。システム・トレース、GTF、コンポーネント・トレースの稼動状況サマリを表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010116の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域整理の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD TRACE 目的を指定し、OSKB010116の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D TRACE 目的
CASE OSKB010116
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D TRACE 目的
CASE OSKB010116
SOURCE z/OS MVS Operations
D TRACE 目的とOSKB010116が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010116を同じ出力で読み、値域整理の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010116
→ Enter を押す
［画面・出力］
IEE115I OSKB010116 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010116   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010116が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D TRACE 目的 と OSKB010116 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010116 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0136"><h3>D TRACE,COMP=name</h3><p class="kb-meta">分類: D TRACE ・ 難易度: 上級</p><p>D TRACE,COMP=nameは、指定コンポーネント (XCF, GRS, CTRACE 等) のトレースモード、バッファサイズ、サブトレース・オプションを表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開記録の操作コマンドで D TRACE 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D TRACE 命令の出力を取らず展開記録の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開記録の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開記録の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開記録の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開記録正解では選択記号 B を採用し、正解名は展開記録正解です。展開記録根拠では D TRACE 命令 は「展開記録の操作コマンドに関係する定義値と表示行を照合する展開記録項目」と D A,L または該当パネルの出力を照合し、根拠名は展開記録根拠です。展開記録追跡では D TRACE 命令の属性行と IEE115I を合わせ、追跡名は展開記録追跡です。誤答側の問題点を分けます。 A: 展開記録不足は名称や説明だけに寄り、判定名は展開記録不足です。 B: 展開記録正答は対象出力と項目説明を結び、根拠名は展開記録正答です。 C: 展開記録欠落は戻り値や記録番号に寄り、欠落名は展開記録欠落です。 D: 展開記録流用は別カテゴリの確認であり、排除名は展開記録流用です。展開記録初出では D TRACE 命令を MVS オペレータコマンドの運用手順で確認し、初出名は展開記録初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換確認の操作コマンドに関する D TRACE,COMP=nameの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換確認の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. D TRACE,COMP=nameの変更点を出力本文から切り離して置換確認の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換確認の操作コマンドにおいて選択記号 D を採用し、識別名は置換確認です。置換確認の操作コマンドにおいて D TRACE,COMP=name は説明欄の「D TRACE,COMP=nameの状態と出力メッセージを結び付ける置換確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認の操作コマンドに関する記録は、D TRACE,COMP=nameの出力行と IEE115I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換確認ではありません。 B: 置換確認の操作コマンドは別カテゴリの確認を流用しており、D TRACE,COMP=nameの根拠にならないため置換確認ではありません。 C: 置換確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認の操作コマンドで記録する D TRACE,COMP=nameはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D TRACE,COMP=name</strong></p><p>検証目的: 警告整理の操作コマンドについて、D TRACE,COMP=nameは、指定コンポーネント (XCF, GRS, CTRACE 等) のトレースモード、バッファサイズ、サブトレース・オプションを表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010117の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告整理の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD TRACE,COMP=nameを指定し、OSKB010117の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D TRACE,COMP=name
CASE OSKB010117
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D TRACE,COMP=name
CASE OSKB010117
SOURCE z/OS MVS Operations
D TRACE,COMP=nameとOSKB010117が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010117を同じ出力で読み、警告整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010117
→ Enter を押す
［画面・出力］
IEE115I OSKB010117 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010117   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010117が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D TRACE,COMP=name と OSKB010117 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010117 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0137"><h3>D TRACE,ST システム・トレース</h3><p class="kb-meta">分類: D TRACE ・ 難易度: 上級</p><p>D TRACE,ST システム・トレースは、システム・トレースのバッファサイズ、MODE (ON/OFF)、ASIDS フィルタを表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換記録のシステム・トレースに関する D TRACE 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換記録のシステム・トレースの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換記録のシステム・トレースの証跡として保存して根拠にする。</li><li>C. D TRACE 命令の変更点を出力本文から切り離して置換記録のシステム・トレースの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換記録で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換記録正解では選択記号 D を採用し、正解名は置換記録正解です。置換記録根拠では D TRACE 命令 は「D TRACE 命令の状態と出力メッセージを結び付ける置換記録項目」と D A,L または該当パネルの出力を照合し、根拠名は置換記録根拠です。置換記録保存では D TRACE 命令の出力行と IEE115I を一緒に残し、保存名は置換記録保存です。選択肢ごとの違いを示します。 A: 置換記録欠落は戻り値や記録番号に寄り、欠落名は置換記録欠落です。 B: 置換記録流用は別カテゴリの確認であり、排除名は置換記録流用です。 C: 置換記録不足は名称や説明だけに寄り、判定名は置換記録不足です。 D: 置換記録正答は対象出力と項目説明を結び、根拠名は置換記録正答です。置換記録対象では D TRACE 命令をz/OS MVS Operationsの確認記録に残し、対象名は置換記録対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索確認のシステム・トレースで D TRACE,ST システム・トレースの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D TRACE,ST システム・トレースの出力を取らず探索確認のシステム・トレースの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索確認のシステム・トレースの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索確認のシステム・トレースへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索確認のシステム・トレースにおいて選択記号 B を採用し、識別名は探索確認です。探索確認のシステム・トレースにおいて D TRACE,ST システム・トレース は説明欄の「探索確認のシステム・トレースに関係する定義値と表示行を照合する探索確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認のシステム・トレースの証跡を読む担当者は、D TRACE,ST システム・トレースの属性行と IEE115I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認のシステム・トレースは名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認のシステム・トレースは対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認のシステム・トレースは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索確認ではありません。 D: 探索確認のシステム・トレースは別カテゴリの確認を流用しており、D TRACE,ST システム・トレースの根拠にならないため探索確認ではありません。探索確認のシステム・トレースに出る D TRACE,ST システム・トレースは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D TRACE,ST システム・トレース</strong></p><p>検証目的: 監査整理のシステム・トレースについて、D TRACE,ST システム・トレースは、システム・トレースのバッファサイズ、MODE (ON/OFF)、ASIDS フィルタを表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010119の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査整理のシステム・トレースの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD TRACE,ST システム・トレを指定し、OSKB010119の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D TRACE,ST システム・トレ
CASE OSKB010119
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D TRACE,ST システム・トレ
CASE OSKB010119
SOURCE z/OS MVS Operations
D TRACE,ST システム・トレとOSKB010119が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010119を同じ出力で読み、監査整理のシステム・トレースの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010119
→ Enter を押す
［画面・出力］
IEE115I OSKB010119 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010119   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010119が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D TRACE,ST システム・トレ と OSKB010119 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010119 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0138"><h3>D TRACE,WTRSTART=name</h3><p class="kb-meta">分類: D TRACE ・ 難易度: 上級</p><p>D TRACE,WTRSTART=nameは、トレース外部書き出しライター (CTWTR) の起動状態を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出記録の操作コマンドで操作コマンドの運用確認を行います。D TRACE 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出記録の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出記録の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、呼出記録の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D TRACE 命令の属性行を読まず呼出記録の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出記録正解では選択記号 C を採用し、正解名は呼出記録正解です。呼出記録根拠では D TRACE 命令 は「z/OS MVS Operationsで D TRACE 命令の扱いを記録する呼出記録項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出記録根拠です。呼出記録受渡では D TRACE 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出記録受渡です。不適切な選択肢を整理します。 A: 呼出記録流用は別カテゴリの確認であり、排除名は呼出記録流用です。 B: 呼出記録欠落は戻り値や記録番号に寄り、欠落名は呼出記録欠落です。 C: 呼出記録正答は対象出力と項目説明を結び、根拠名は呼出記録正答です。 D: 呼出記録不足は名称や説明だけに寄り、判定名は呼出記録不足です。呼出記録資料では D TRACE 命令の使い方を出典欄から追跡し、資料名は呼出記録資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端確認の操作コマンドに関係する D TRACE,WTRSTART=nameの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D TRACE,WTRSTART=nameの名称と担当者名のみを残して終端確認の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端確認の操作コマンドにおいて選択記号 A を採用し、識別名は終端確認です。終端確認の操作コマンドにおいて D TRACE,WTRSTART=name は説明欄の「D TRACE,WTRSTART=nameの用途を操作コマンドの表示で確認する終端確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認の操作コマンドに関連して、z/OS MVS Operationsでは D TRACE,WTRSTART=nameの表示属性と IEE115I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認の操作コマンドは別カテゴリの確認を流用しており、D TRACE,WTRSTART=nameの根拠にならないため終端確認ではありません。 D: 終端確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端確認ではありません。終端確認の操作コマンドで使う D TRACE,WTRSTART=nameという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D TRACE,WTRSTART=name</strong></p><p>検証目的: 復旧整理の操作コマンドについて、D TRACE,WTRSTART=nameは、トレース外部書き出しライター (CTWTR) の起動状態を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010118の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧整理の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD TRACE,WTRSTART=nを指定し、OSKB010118の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D TRACE,WTRSTART=n
CASE OSKB010118
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D TRACE,WTRSTART=n
CASE OSKB010118
SOURCE z/OS MVS Operations
D TRACE,WTRSTART=nとOSKB010118が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010118を同じ出力で読み、復旧整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010118
→ Enter を押す
［画面・出力］
IEE115I OSKB010118 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010118   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010118が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D TRACE,WTRSTART=n と OSKB010118 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010118 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D U


<section class="kb-item" id="c22-i0139"><h3>D U,,,devnum,count</h3><p class="kb-meta">分類: D U ・ 難易度: 中級</p><p>D U,,,devnum,countは、MVS オペレータコマンドのD Uで状態表示や操作を行うためのコマンド関連項目です。D U,,,devnum,countは、指定装置番号から count 台ぶんの状態 (ONLINE/OFFLINE, ALLOC, UCBTYPE, VOLSER) を 1 行ずつ表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端記録の操作コマンドに関係する D U 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、終端記録の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D U 命令の名称と担当者名だけを残して終端記録の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端記録の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端記録の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端記録正解では選択記号 A を採用し、正解名は終端記録正解です。終端記録根拠では D U 命令 は「D U 命令の用途を操作コマンドの表示で確認する終端記録項目」と D A,L または該当パネルの出力を照合し、根拠名は終端記録根拠です。終端記録背景ではz/OS MVS Operationsの D U 命令と IEE115I を同じ証跡に残し、背景名は終端記録背景です。他の選択肢を確認します。 A: 終端記録正答は対象出力と項目説明を結び、根拠名は終端記録正答です。 B: 終端記録不足は名称や説明だけに寄り、判定名は終端記録不足です。 C: 終端記録流用は別カテゴリの確認であり、排除名は終端記録流用です。 D: 終端記録欠落は戻り値や記録番号に寄り、欠落名は終端記録欠落です。終端記録用語では D U 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は終端記録用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書確認の操作コマンドで操作コマンドの運用確認を行います。D U,,,devnum,countの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書確認の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書確認の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D U,,,devnum,countの属性行を読まず上書確認の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書確認の操作コマンドにおいて選択記号 C を採用し、識別名は上書確認です。上書確認の操作コマンドにおいて D U,,,devnum,count は説明欄の「z/OS MVS Operationsで D U,,,devnum,countの扱いを記録する上書確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認の操作コマンドを受け取る担当者は、D U,,,devnum,countの表示結果と IEE115I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認の操作コマンドは別カテゴリの確認を流用しており、D U,,,devnum,countの根拠にならないため上書確認ではありません。 B: 上書確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書確認ではありません。 C: 上書確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認の操作コマンドが示す D U,,,devnum,countは出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D U,,,devnum,count</strong></p><p>検証目的: 変更整理の操作コマンドについて、D U,,,devnum,countは、MVS オペレータコマンドの D U で状態表示や操作を行うためのコマンド関連項目です。D U,,,devnum,countは、指定装置に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB010120の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更整理の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD U,,,devnum,countを指定し、OSKB010120の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D U,,,devnum,count
CASE OSKB010120
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D U,,,devnum,count
CASE OSKB010120
SOURCE z/OS MVS Operations
D U,,,devnum,countとOSKB010120が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB010120を同じ出力で読み、変更整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB010120
→ Enter を押す
［画面・出力］
IEE115I OSKB010120 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB010120   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB010120が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D U,,,devnum,count と OSKB010120 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB010120 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0140"><h3>D U,,ALLOC</h3><p class="kb-meta">分類: D U ・ 難易度: 中級</p><p>D U,,ALLOCは、MVS オペレータコマンドのD Uで確認する項目です。現在いずれかのジョブから割り振られている装置のみを一覧。装置リソース競合確認に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲記録の操作コマンドで操作コマンドの運用確認を行います。D U,,ALLOC の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲記録の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲記録の操作コマンドを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、範囲記録の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D U,,ALLOC の属性行を読まず範囲記録の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠では D U,,ALLOC は「z/OS MVS Operationsで D U,,ALLOC の扱いを記録する範囲記録項目」と D A,L または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡では D U,,ALLOC の表示結果と IEE115I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明だけに寄り、判定名は範囲記録不足です。範囲記録資料では D U,,ALLOC の使い方を出典欄から追跡し、資料名は範囲記録資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 記録確認の操作コマンドに関係する D U,,ALLOC の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、記録確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D U,,ALLOC の名称と担当者名のみを残して記録確認の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で記録確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録確認の操作コマンドにおいて選択記号 A を採用し、識別名は記録確認です。記録確認の操作コマンドにおいて D U,,ALLOC は説明欄の「D U,,ALLOC の用途を操作コマンドの表示で確認する記録確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認の操作コマンドに関連して、z/OS MVS Operationsでは D U,,ALLOC の表示属性と IEE115I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認の操作コマンドは別カテゴリの確認を流用しており、D U,,ALLOC の根拠にならないため記録確認ではありません。 D: 記録確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録確認ではありません。記録確認の操作コマンドで使う D U,,ALLOC という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D U,,ALLOC</strong></p><p>検証目的: 探索確認の操作コマンドについて、D U,,ALLOC は、MVS オペレータコマンドの D U で確認する項目です。現在いずれかのジョブから割り振られている装置のみを一覧。装置リソース競合確認に使うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020006の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、探索確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD U,,ALLOCを指定し、OSKB020006の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D U,,ALLOC
CASE OSKB020006
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D U,,ALLOC
CASE OSKB020006
SOURCE z/OS MVS Operations
D U,,ALLOCとOSKB020006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020006を同じ出力で読み、探索確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020006
→ Enter を押す
［画面・出力］
IEE115I OSKB020006 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020006   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D U,,ALLOC と OSKB020006 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0141"><h3>D U,DASD,OFFLINE</h3><p class="kb-meta">分類: D U ・ 難易度: 中級</p><p>D U,DASD,OFFLINEは、MVS オペレータコマンドのD Uで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力記録の操作コマンドに関する D U 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力記録の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力記録の操作コマンドの証跡として保存して根拠にする。</li><li>C. D U 命令の変更点を出力本文から切り離して出力記録の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、出力記録の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力記録正解では選択記号 D を採用し、正解名は出力記録正解です。出力記録根拠では D U 命令 は「D U 命令の状態と出力メッセージを結び付ける出力記録項目」と D A,L または該当パネルの出力を照合し、根拠名は出力記録根拠です。出力記録保存では D U 命令の出力行と IEE115I を一緒に残し、保存名は出力記録保存です。選択肢ごとの違いを示します。 A: 出力記録欠落は戻り値や記録番号に寄り、欠落名は出力記録欠落です。 B: 出力記録流用は別カテゴリの確認であり、排除名は出力記録流用です。 C: 出力記録不足は名称や説明だけに寄り、判定名は出力記録不足です。 D: 出力記録正答は対象出力と項目説明を結び、根拠名は出力記録正答です。出力記録対象では D U 命令をz/OS MVS Operationsの確認記録に残し、対象名は出力記録対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切確認の操作コマンドで D U,DASD,OFFLINE の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D U,DASD,OFFLINE の出力を取らず区切確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切確認の操作コマンドにおいて選択記号 B を採用し、識別名は区切確認です。区切確認の操作コマンドにおいて D U,DASD,OFFLINE は説明欄の「区切確認の操作コマンドに関係する定義値と表示行を照合する区切確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認の操作コマンドの証跡を読む担当者は、D U,DASD,OFFLINE の属性行と IEE115I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切確認ではありません。 D: 区切確認の操作コマンドは別カテゴリの確認を流用しており、D U,DASD,OFFLINE の根拠にならないため区切確認ではありません。区切確認の操作コマンドに出る D U,DASD,OFFLINE は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D U,DASD,OFFLINE</strong></p><p>検証目的: 呼出確認の操作コマンドについて、D U,DASD,OFFLINE は、MVS オペレータコマンドの D U で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020003の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD U,DASD,OFFLINEを指定し、OSKB020003の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D U,DASD,OFFLINE
CASE OSKB020003
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D U,DASD,OFFLINE
CASE OSKB020003
SOURCE z/OS MVS Operations
D U,DASD,OFFLINEとOSKB020003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020003を同じ出力で読み、呼出確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020003
→ Enter を押す
［画面・出力］
IEE115I OSKB020003 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020003   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D U,DASD,OFFLINE と OSKB020003 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0142"><h3>D U,DASD,ONLINE</h3><p class="kb-meta">分類: D U ・ 難易度: 中級</p><p>D U,DASD,ONLINEは、MVS オペレータコマンドのD Uで確認する項目です。オンラインの DASD のみを一覧表示。テープと混在せずに DASD 構成を確認する典型例</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書記録の操作コマンドで操作コマンドの運用確認を行います。D U,DASD,ONLINE の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書記録の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書記録の操作コマンドを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を上書記録で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D U,DASD,ONLINE の属性行を読まず上書記録の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書記録正解では選択記号 C を採用し、正解名は上書記録正解です。上書記録根拠では D U,DASD,ONLINE は「z/OS MVS Operationsで D U,DASD,ONLINE の扱いを記録する上書記録項目」と D A,L または該当パネルの出力を照合し、根拠名は上書記録根拠です。上書記録受渡では D U,DASD,ONLINE の表示結果と IEE115I を同じ確認単位にし、受渡名は上書記録受渡です。不適切な選択肢を整理します。 A: 上書記録流用は別カテゴリの確認であり、排除名は上書記録流用です。 B: 上書記録欠落は戻り値や記録番号に寄り、欠落名は上書記録欠落です。 C: 上書記録正答は対象出力と項目説明を結び、根拠名は上書記録正答です。 D: 上書記録不足は名称や説明だけに寄り、判定名は上書記録不足です。上書記録資料では D U,DASD,ONLINE の使い方を出典欄から追跡し、資料名は上書記録資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件確認の操作コマンドに関係する D U,DASD,ONLINE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D U,DASD,ONLINE の名称と担当者名のみを残して条件確認の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件確認の操作コマンドにおいて選択記号 A を採用し、識別名は条件確認です。条件確認の操作コマンドにおいて D U,DASD,ONLINE は説明欄の「D U,DASD,ONLINE の用途を操作コマンドの表示で確認する条件確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認の操作コマンドに関連して、z/OS MVS Operationsでは D U,DASD,ONLINE の表示属性と IEE115I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認の操作コマンドは別カテゴリの確認を流用しており、D U,DASD,ONLINE の根拠にならないため条件確認ではありません。 D: 条件確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件確認ではありません。条件確認の操作コマンドで使う D U,DASD,ONLINE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D U,DASD,ONLINE</strong></p><p>検証目的: 展開照合の操作コマンドについて、D U,DASD,ONLINE は、MVS オペレータコマンドの D U で確認する項目です。オンラインの DASD のみを一覧表示。テープと混在せずに DASD 構成を確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040022の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開照合の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD U,DASD,ONLINEを指定し、OSKB040022の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D U,DASD,ONLINE
CASE OSKB040022
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D U,DASD,ONLINE
CASE OSKB040022
SOURCE z/OS MVS Operations
D U,DASD,ONLINEとOSKB040022が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040022を同じ出力で読み、展開照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040022
→ Enter を押す
［画面・出力］
IEE115I OSKB040022 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040022   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040022が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D U,DASD,ONLINE と OSKB040022 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D U,DASD,ONLINE</strong></p><p>検証目的: 展開確認の操作コマンドについて、D U,DASD,ONLINE は、MVS オペレータコマンドの D U で確認する項目です。オンラインの DASD のみを一覧表示。テープと混在せずに DASD 構成を確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020002の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD U,DASD,ONLINEを指定し、OSKB020002の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D U,DASD,ONLINE
CASE OSKB020002
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D U,DASD,ONLINE
CASE OSKB020002
SOURCE z/OS MVS Operations
D U,DASD,ONLINEとOSKB020002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020002を同じ出力で読み、展開確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020002
→ Enter を押す
［画面・出力］
IEE115I OSKB020002 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020002   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D U,DASD,ONLINE と OSKB020002 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0143"><h3>D U,IPLVOL</h3><p class="kb-meta">分類: D U ・ 難易度: 中級</p><p>D U,IPLVOLは、MVS オペレータコマンドのD Uで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切記録の操作コマンドで D U,IPLVOL の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D U,IPLVOL の出力を取らず区切記録の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて区切記録の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切記録の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切記録の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では D U,IPLVOL は「区切記録の操作コマンドに関係する定義値と表示行を照合する区切記録項目」と D A,L または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では D U,IPLVOL の属性行と IEE115I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明だけに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では D U,IPLVOL を MVS オペレータコマンドの運用手順で確認し、初出名は区切記録初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 優先確認の操作コマンドに関する D U,IPLVOL の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先確認の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. D U,IPLVOL の変更点を出力本文から切り離して優先確認の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先確認の操作コマンドにおいて選択記号 D を採用し、識別名は優先確認です。優先確認の操作コマンドにおいて D U,IPLVOL は説明欄の「D U,IPLVOL の状態と出力メッセージを結び付ける優先確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認の操作コマンドに関する記録は、D U,IPLVOL の出力行と IEE115I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先確認ではありません。 B: 優先確認の操作コマンドは別カテゴリの確認を流用しており、D U,IPLVOL の根拠にならないため優先確認ではありません。 C: 優先確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認の操作コマンドで記録する D U,IPLVOL はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D U,IPLVOL</strong></p><p>検証目的: 終端確認の操作コマンドについて、D U,IPLVOL は、MVS オペレータコマンドの D U で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。zに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020005の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD U,IPLVOLを指定し、OSKB020005の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D U,IPLVOL
CASE OSKB020005
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D U,IPLVOL
CASE OSKB020005
SOURCE z/OS MVS Operations
D U,IPLVOLとOSKB020005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020005を同じ出力で読み、終端確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020005
→ Enter を押す
［画面・出力］
IEE115I OSKB020005 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020005   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D U,IPLVOL と OSKB020005 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0144"><h3>D U,TAPE,,devnum</h3><p class="kb-meta">分類: D U ・ 難易度: 中級</p><p>D U,TAPE,,devnumは、MVS オペレータコマンドのD Uで確認する項目です。テープ装置 (TAPE) に絞った状態表示。マウント有無、装置タイプ (3490/3592) を確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件記録の操作コマンドに関係する D U 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、条件記録の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D U 命令の名称と担当者名だけを残して条件記録の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件記録の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件記録の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では D U 命令 は「D U 命令の用途を操作コマンドの表示で確認する条件記録項目」と D A,L または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景ではz/OS MVS Operationsの D U 命令と IEE115I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明だけに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では D U 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は条件記録用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 範囲確認の操作コマンドで操作コマンドの運用確認を行います。D U,TAPE,,devnumの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲確認の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲確認の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D U,TAPE,,devnumの属性行を読まず範囲確認の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲確認の操作コマンドにおいて選択記号 C を採用し、識別名は範囲確認です。範囲確認の操作コマンドにおいて D U,TAPE,,devnum は説明欄の「z/OS MVS Operationsで D U,TAPE,,devnumの扱いを記録する範囲確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲確認です。範囲確認の操作コマンドを受け取る担当者は、D U,TAPE,,devnumの表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲確認です。不適切な選択肢を整理します。 A: 範囲確認の操作コマンドは別カテゴリの確認を流用しており、D U,TAPE,,devnumの根拠にならないため範囲確認ではありません。 B: 範囲確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲確認ではありません。 C: 範囲確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので範囲確認です。 D: 範囲確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲確認ではありません。範囲確認の操作コマンドが示す D U,TAPE,,devnumは出典欄の資料で使い方を追跡できる項目であり、用語名は範囲確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D U,TAPE,,devnum</strong></p><p>検証目的: 置換確認の操作コマンドについて、D U,TAPE,,devnumは、MVS オペレータコマンドの D U で確認する項目です。テープ装置 (TAPE) に絞った状態表示。マウント有無、装置タイプ (3490/に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020004の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD U,TAPE,,devnumを指定し、OSKB020004の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D U,TAPE,,devnum
CASE OSKB020004
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D U,TAPE,,devnum
CASE OSKB020004
SOURCE z/OS MVS Operations
D U,TAPE,,devnumとOSKB020004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020004を同じ出力で読み、置換確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020004
→ Enter を押す
［画面・出力］
IEE115I OSKB020004 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020004   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D U,TAPE,,devnum と OSKB020004 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0145"><h3>D U,VOL=volser</h3><p class="kb-meta">分類: D U ・ 難易度: 中級</p><p>D U,VOL=volserは、MVS オペレータコマンドのD Uで確認する項目です。指定ボリュームをマウントしている装置番号と ONLINE 状態を逆引きする</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索記録の操作コマンドで D U,VOL=volserの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D U,VOL=volserの出力を取らず探索記録の操作コマンドの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて探索記録の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索記録の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索記録の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索記録正解では選択記号 B を採用し、正解名は探索記録正解です。探索記録根拠では D U,VOL=volser は「探索記録の操作コマンドに関係する定義値と表示行を照合する探索記録項目」と D A,L または該当パネルの出力を照合し、根拠名は探索記録根拠です。探索記録追跡では D U,VOL=volserの属性行と IEE115I を合わせ、追跡名は探索記録追跡です。誤答側の問題点を分けます。 A: 探索記録不足は名称や説明だけに寄り、判定名は探索記録不足です。 B: 探索記録正答は対象出力と項目説明を結び、根拠名は探索記録正答です。 C: 探索記録欠落は戻り値や記録番号に寄り、欠落名は探索記録欠落です。 D: 探索記録流用は別カテゴリの確認であり、排除名は探索記録流用です。探索記録初出では D U,VOL=volserを MVS オペレータコマンドの運用手順で確認し、初出名は探索記録初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力確認の操作コマンドに関する D U,VOL=volserの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力確認の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. D U,VOL=volserの変更点を出力本文から切り離して出力確認の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力確認の操作コマンドにおいて選択記号 D を採用し、識別名は出力確認です。出力確認の操作コマンドにおいて D U,VOL=volser は説明欄の「D U,VOL=volserの状態と出力メッセージを結び付ける出力確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認の操作コマンドに関する記録は、D U,VOL=volserの出力行と IEE115I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力確認ではありません。 B: 出力確認の操作コマンドは別カテゴリの確認を流用しており、D U,VOL=volserの根拠にならないため出力確認ではありません。 C: 出力確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認の操作コマンドで記録する D U,VOL=volserはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D U,VOL=volser</strong></p><p>検証目的: 構文確認の操作コマンドについて、D U,VOL=volserは、MVS オペレータコマンドの D U で確認する項目です。指定ボリュームをマウントしている装置番号と ONLINE 状態を逆引きするに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020001の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD U,VOL=volserを指定し、OSKB020001の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D U,VOL=volser
CASE OSKB020001
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D U,VOL=volser
CASE OSKB020001
SOURCE z/OS MVS Operations
D U,VOL=volserとOSKB020001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020001を同じ出力で読み、構文確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020001
→ Enter を押す
［画面・出力］
IEE115I OSKB020001 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020001   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D U,VOL=volser と OSKB020001 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D UNI


<section class="kb-item" id="c22-i0146"><h3>D UNI 目的</h3><p class="kb-meta">分類: D UNI ・ 難易度: 初級</p><p>D UNI 目的は、Unicode 変換サービスの現行設定 (アクティブな CCSID 変換表、IMAGE 名) を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先記録の目的に関する D UNI 目的の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先記録の目的の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先記録の目的の証跡として保存して根拠にする。</li><li>C. D UNI 目的の変更点を出力本文から切り離して優先記録の目的の承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、優先記録の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では D UNI 目的 は「D UNI 目的の状態と出力メッセージを結び付ける優先記録項目」と D A,L または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では D UNI 目的の出力行と IEE115I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明だけに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では D UNI 目的をz/OS MVS Operationsの確認記録に残し、対象名は優先記録対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 比較確認の目的で D UNI 目的の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D UNI 目的の出力を取らず比較確認の目的の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、比較確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較確認の目的の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較確認の目的へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 比較確認の目的において選択記号 B を採用し、識別名は比較確認です。比較確認の目的において D UNI 目的 は説明欄の「比較確認の目的に関係する定義値と表示行を照合する比較確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較確認です。比較確認の目的の証跡を読む担当者は、D UNI 目的の属性行と IEE115I を合わせて追跡し、背景名は比較確認です。誤答側の問題点を分けます。 A: 比較確認の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため比較確認ではありません。 B: 比較確認の目的は対象出力と項目説明を結び、根拠を残すので比較確認です。 C: 比較確認の目的は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較確認ではありません。 D: 比較確認の目的は別カテゴリの確認を流用しており、D UNI 目的の根拠にならないため比較確認ではありません。比較確認の目的に出る D UNI 目的は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D UNI 目的</strong></p><p>検証目的: 上書確認の目的について、D UNI 目的は、Unicode 変換サービスの現行設定 (アクティブな CCSID 変換表、IMAGE 名) を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020007の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書確認の目的の確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD UNI 目的を指定し、OSKB020007の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D UNI 目的
CASE OSKB020007
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D UNI 目的
CASE OSKB020007
SOURCE z/OS MVS Operations
D UNI 目的とOSKB020007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020007を同じ出力で読み、上書確認の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020007
→ Enter を押す
［画面・出力］
IEE115I OSKB020007 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020007   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D UNI 目的 と OSKB020007 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D WLM


<section class="kb-item" id="c22-i0147"><h3>D WLM 現行ポリシー</h3><p class="kb-meta">分類: D WLM ・ 難易度: 上級</p><p>D WLM 現行ポリシーは、活性 WLM サービス・ポリシー名、活性化日時、利用 WLM モード (GOAL/COMPAT) を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録記録の現行ポリシーに関係する D WLM 現行ポリシーの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、記録記録として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D WLM 現行ポリシーの名称と担当者名だけを残して記録記録の現行ポリシーの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録記録の現行ポリシーを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録記録の現行ポリシーの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では D WLM 現行ポリシー は「D WLM 現行ポリシーの用途を操作コマンドの表示で確認する記録記録項目」と D A,L または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景ではz/OS MVS Operationsの D WLM 現行ポリシーと IEE115I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明だけに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では D WLM 現行ポリシーを MVS オペレータコマンドで扱う確認対象とし、用語名は記録記録用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 順序確認の現行ポリシーで操作コマンドの運用確認を行います。D WLM 現行ポリシーの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序確認の現行ポリシーを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序確認の現行ポリシーを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、順序確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D WLM 現行ポリシーの属性行を読まず順序確認の現行ポリシーの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序確認の現行ポリシーにおいて選択記号 C を採用し、識別名は順序確認です。順序確認の現行ポリシーにおいて D WLM 現行ポリシー は説明欄の「z/OS MVS Operationsで D WLM 現行ポリシーの扱いを記録する順序確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認の現行ポリシーを受け取る担当者は、D WLM 現行ポリシーの表示結果と IEE115I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認の現行ポリシーは別カテゴリの確認を流用しており、D WLM 現行ポリシーの根拠にならないため順序確認ではありません。 B: 順序確認の現行ポリシーは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため順序確認ではありません。 C: 順序確認の現行ポリシーは対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認の現行ポリシーは名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認の現行ポリシーが示す D WLM 現行ポリシーは出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D WLM 現行ポリシー</strong></p><p>検証目的: 呼出照合の現行ポリシーについて、D WLM 現行ポリシーは、活性 WLM サービス・ポリシー名、活性化日時、利用 WLM モード (GOAL/COMPAT) を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040023の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出照合の現行ポリシーの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD WLM 現行ポリシーを指定し、OSKB040023の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D WLM 現行ポリシー
CASE OSKB040023
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D WLM 現行ポリシー
CASE OSKB040023
SOURCE z/OS MVS Operations
D WLM 現行ポリシーとOSKB040023が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040023を同じ出力で読み、呼出照合の現行ポリシーの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040023
→ Enter を押す
［画面・出力］
IEE115I OSKB040023 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040023   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040023が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D WLM 現行ポリシー と OSKB040023 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040023 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D WLM 現行ポリシー</strong></p><p>検証目的: 出力確認の現行ポリシーについて、D WLM 現行ポリシーは、活性 WLM サービス・ポリシー名、活性化日時、利用 WLM モード (GOAL/COMPAT) を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020008の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力確認の現行ポリシーの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD WLM 現行ポリシーを指定し、OSKB020008の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D WLM 現行ポリシー
CASE OSKB020008
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D WLM 現行ポリシー
CASE OSKB020008
SOURCE z/OS MVS Operations
D WLM 現行ポリシーとOSKB020008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020008を同じ出力で読み、出力確認の現行ポリシーの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020008
→ Enter を押す
［画面・出力］
IEE115I OSKB020008 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020008   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D WLM 現行ポリシー と OSKB020008 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0148"><h3>D WLM,APPLENV=name</h3><p class="kb-meta">分類: D WLM ・ 難易度: 上級</p><p>D WLM,APPLENV=nameは、アプリケーション環境 (Stored Proc 等) の稼動状態とサーバ・アドレス・スペース数を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域記録の操作コマンドに関する D WLM 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域記録の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域記録の操作コマンドの証跡として保存して根拠にする。</li><li>C. D WLM 命令の変更点を出力本文から切り離して値域記録の操作コマンドの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域記録で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では D WLM 命令 は「D WLM 命令の状態と出力メッセージを結び付ける値域記録項目」と D A,L または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では D WLM 命令の出力行と IEE115I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明だけに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では D WLM 命令をz/OS MVS Operationsの確認記録に残し、対象名は値域記録対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 復旧確認の操作コマンドで D WLM,APPLENV=nameの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D WLM,APPLENV=nameの出力を取らず復旧確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、復旧確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧確認の操作コマンドにおいて選択記号 B を採用し、識別名は復旧確認です。復旧確認の操作コマンドにおいて D WLM,APPLENV=name は説明欄の「復旧確認の操作コマンドに関係する定義値と表示行を照合する復旧確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認の操作コマンドの証跡を読む担当者は、D WLM,APPLENV=nameの属性行と IEE115I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認の操作コマンドは別カテゴリの確認を流用しており、D WLM,APPLENV=nameの根拠にならないため復旧確認ではありません。復旧確認の操作コマンドに出る D WLM,APPLENV=nameは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D WLM,APPLENV=name</strong></p><p>検証目的: 範囲確認の操作コマンドについて、D WLM,APPLENV=nameは、アプリケーション環境 (Stored Proc 等) の稼動状態とサーバ・アドレス・スペース数を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020011の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD WLM,APPLENV=nameを指定し、OSKB020011の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D WLM,APPLENV=name
CASE OSKB020011
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D WLM,APPLENV=name
CASE OSKB020011
SOURCE z/OS MVS Operations
D WLM,APPLENV=nameとOSKB020011が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020011を同じ出力で読み、範囲確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020011
→ Enter を押す
［画面・出力］
IEE115I OSKB020011 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020011   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020011が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D WLM,APPLENV=name と OSKB020011 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020011 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0149"><h3>D WLM,DYNAPPL</h3><p class="kb-meta">分類: D WLM ・ 難易度: 上級</p><p>D WLM,DYNAPPLは、MVS オペレータコマンドのD WLMで確認する項目です。動的に作成された WLM 管理サーバ・アドレス・スペースの一覧を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告記録の操作コマンドに関係する D WLM,DYNAPPL の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、警告記録の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. D WLM,DYNAPPL の名称と担当者名だけを残して警告記録の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告記録の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告記録の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では D WLM,DYNAPPL は「D WLM,DYNAPPL の用途を操作コマンドの表示で確認する警告記録項目」と D A,L または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景ではz/OS MVS Operationsの D WLM,DYNAPPL と IEE115I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明だけに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では D WLM,DYNAPPL を MVS オペレータコマンドで扱う確認対象とし、用語名は警告記録用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 監査確認の操作コマンドで操作コマンドの運用確認を行います。D WLM,DYNAPPL の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査確認の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査確認の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、監査確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D WLM,DYNAPPL の属性行を読まず監査確認の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査確認の操作コマンドにおいて選択記号 C を採用し、識別名は監査確認です。監査確認の操作コマンドにおいて D WLM,DYNAPPL は説明欄の「z/OS MVS Operationsで D WLM,DYNAPPL の扱いを記録する監査確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認の操作コマンドを受け取る担当者は、D WLM,DYNAPPL の表示結果と IEE115I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認の操作コマンドは別カテゴリの確認を流用しており、D WLM,DYNAPPL の根拠にならないため監査確認ではありません。 B: 監査確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査確認ではありません。 C: 監査確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認の操作コマンドが示す D WLM,DYNAPPL は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D WLM,DYNAPPL</strong></p><p>検証目的: 優先確認の操作コマンドについて、D WLM,DYNAPPL は、MVS オペレータコマンドの D WLM で確認する項目です。動的に作成された WLM 管理サーバ・アドレス・スペースの一覧を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020012の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先確認の操作コマンドの確認表示へ進みます。
［操作（入力）］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
→ Enter を押す
［画面・出力］
(MVS Console)
COMMAND INPUT ===&gt; D A,L
COMMAND INPUTにD A,Lが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はMVS Consoleの表示結果です。FIND欄にD WLM,DYNAPPLを指定し、OSKB020012の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D WLM,DYNAPPL
CASE OSKB020012
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D WLM,DYNAPPL
CASE OSKB020012
SOURCE z/OS MVS Operations
D WLM,DYNAPPLとOSKB020012が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020012を同じ出力で読み、優先確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020012
→ Enter を押す
［画面・出力］
IEE115I OSKB020012 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020012   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020012が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D WLM,DYNAPPL と OSKB020012 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020012 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>
