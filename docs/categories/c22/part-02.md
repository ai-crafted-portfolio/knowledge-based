---
search:
  exclude: true
---

# MVS オペレータコマンド — 詳細 (2/2)

[← MVS オペレータコマンド の概要へ戻る](index.md)


## D WLM


<section class="kb-item" id="c22-i0150"><h3>D WLM,RESOURCES</h3><p class="kb-meta">分類: D WLM ・ 難易度: 上級</p><p>D WLM,RESOURCESは、MVS オペレータコマンドのD WLMで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較記録の操作コマンドで D WLM,RESOURCES の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D WLM,RESOURCES の出力を取らず比較記録の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較記録の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較記録の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較記録の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では D WLM,RESOURCES は「比較記録の操作コマンドに関係する定義値と表示行を照合する比較記録項目」と D A,L または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では D WLM,RESOURCES の属性行と IEE115I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明だけに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では D WLM,RESOURCES を MVS オペレータコマンドの運用手順で確認し、初出名は比較記録初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 値域確認の操作コマンドに関する D WLM,RESOURCES の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域確認の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. D WLM,RESOURCES の変更点を出力本文から切り離して値域確認の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、値域確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域確認の操作コマンドにおいて選択記号 D を採用し、識別名は値域確認です。値域確認の操作コマンドにおいて D WLM,RESOURCES は説明欄の「D WLM,RESOURCES の状態と出力メッセージを結び付ける値域確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認の操作コマンドに関する記録は、D WLM,RESOURCES の出力行と IEE115I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域確認ではありません。 B: 値域確認の操作コマンドは別カテゴリの確認を流用しており、D WLM,RESOURCES の根拠にならないため値域確認ではありません。 C: 値域確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認の操作コマンドで記録する D WLM,RESOURCES はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D WLM,RESOURCES</strong></p><p>検証目的: 条件確認の操作コマンドについて、D WLM,RESOURCES は、MVS オペレータコマンドの D WLM で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けてに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020009の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD WLM,RESOURCESを指定し、OSKB020009の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D WLM,RESOURCES
CASE OSKB020009
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D WLM,RESOURCES
CASE OSKB020009
SOURCE z/OS MVS Operations
D WLM,RESOURCESとOSKB020009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020009を同じ出力で読み、条件確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020009
→ Enter を押す
［画面・出力］
IEE115I OSKB020009 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020009   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D WLM,RESOURCES と OSKB020009 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0151"><h3>D WLM,SCHENV=name</h3><p class="kb-meta">分類: D WLM ・ 難易度: 上級</p><p>D WLM,SCHENV=nameは、MVS オペレータコマンドのD WLMで確認する項目です。スケジューリング環境 (SCHENV) の現状 (AVAILABLE/UNAVAILABLE) を表示。バッチ配置調整時に必須</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序記録の操作コマンドで操作コマンドの運用確認を行います。D WLM 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序記録の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序記録の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、順序記録の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. D WLM 命令の属性行を読まず順序記録の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では D WLM 命令 は「z/OS MVS Operationsで D WLM 命令の扱いを記録する順序記録項目」と D A,L または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では D WLM 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明だけに寄り、判定名は順序記録不足です。順序記録資料では D WLM 命令の使い方を出典欄から追跡し、資料名は順序記録資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 警告確認の操作コマンドに関係する D WLM,SCHENV=nameの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、警告確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D WLM,SCHENV=nameの名称と担当者名のみを残して警告確認の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で警告確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告確認の操作コマンドにおいて選択記号 A を採用し、識別名は警告確認です。警告確認の操作コマンドにおいて D WLM,SCHENV=name は説明欄の「D WLM,SCHENV=nameの用途を操作コマンドの表示で確認する警告確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認の操作コマンドに関連して、z/OS MVS Operationsでは D WLM,SCHENV=nameの表示属性と IEE115I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認の操作コマンドは別カテゴリの確認を流用しており、D WLM,SCHENV=nameの根拠にならないため警告確認ではありません。 D: 警告確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告確認ではありません。警告確認の操作コマンドで使う D WLM,SCHENV=nameという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D WLM,SCHENV=name</strong></p><p>検証目的: 区切確認の操作コマンドについて、D WLM,SCHENV=nameは、MVS オペレータコマンドの D WLM で確認する項目です。スケジューリング環境 (SCHENV) の現状 (AVAILABLE/UNAに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020010の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD WLM,SCHENV=nameを指定し、OSKB020010の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D WLM,SCHENV=name
CASE OSKB020010
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D WLM,SCHENV=name
CASE OSKB020010
SOURCE z/OS MVS Operations
D WLM,SCHENV=nameとOSKB020010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020010を同じ出力で読み、区切確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020010
→ Enter を押す
［画面・出力］
IEE115I OSKB020010 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020010   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D WLM,SCHENV=name と OSKB020010 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## D XCF


<section class="kb-item" id="c22-i0152"><h3>D XCF 単独 (Sysplex メンバ)</h3><p class="kb-meta">分類: D XCF ・ 難易度: 中級</p><p>D XCF 単独 (Sysplex メンバ)は、MVS オペレータコマンドのD XCFで確認する項目です。Sysplex の全メンバ・システムと状態 (ACTIVE/SYSGONE/UNKNOWN) を表示。Sysplex 健全性確認の起点</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧記録の単独 メンバで D XCF 単独 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D XCF 単独 属性の出力を取らず復旧記録の単独 メンバの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて復旧記録の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧記録の単独 メンバの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧記録の単独 メンバへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では D XCF 単独 属性 は「復旧記録の単独 メンバに関係する定義値と表示行を照合する復旧記録項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では D XCF 単独 属性の属性行と IEE115I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明だけに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では D XCF 単独 属性を MVS オペレータコマンドの運用手順で確認し、初出名は復旧記録初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 変更確認の単独 メンバに関する D XCF 単独 (Sysplex メンバ)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更確認の単独 メンバの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更確認の単独 メンバの証跡として保存して根拠にする。</li><li>C. D XCF 単独 (Sysplex メンバ)の変更点を出力本文から切り離して変更確認の単独 メンバの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、変更確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更確認の単独 メンバにおいて選択記号 D を採用し、識別名は変更確認です。変更確認の単独 メンバにおいて D XCF 単独 (Sysplex メンバ) は説明欄の「D XCF 単独 (Sysplex メンバ)の状態と出力メッセージを結び付ける変更確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認の単独 メンバに関する記録は、D XCF 単独 (Sysplex メンバ)の出力行と IEE115I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認の単独 メンバは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更確認ではありません。 B: 変更確認の単独 メンバは別カテゴリの確認を流用しており、D XCF 単独 (Sysplex メンバ)の根拠にならないため変更確認ではありません。 C: 変更確認の単独 メンバは名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認の単独 メンバは対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認の単独 メンバで記録する D XCF 単独 (Sysplex メンバ)はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D XCF 単独 (Sysplex メンバ)</strong></p><p>検証目的: 記録確認の単独 メンバについて、D XCF 単独 (Sysplex メンバ)は、MVS オペレータコマンドの D XCF で確認する項目です。Sysplex の全メンバ・システムと状態 (ACTIVE/SYSに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020013の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録確認の単独 メンバの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD XCF 単独 (Sysplex を指定し、OSKB020013の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D XCF 単独 (Sysplex 
CASE OSKB020013
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D XCF 単独 (Sysplex 
CASE OSKB020013
SOURCE z/OS MVS Operations
D XCF 単独 (Sysplex とOSKB020013が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020013を同じ出力で読み、記録確認の単独 メンバの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020013
→ Enter を押す
［画面・出力］
IEE115I OSKB020013 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020013   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020013が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D XCF 単独 (Sysplex  と OSKB020013 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020013 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0153"><h3>D XCF,CF</h3><p class="kb-meta">分類: D XCF ・ 難易度: 中級</p><p>D XCF,CFは、MVS オペレータコマンドのD XCFで確認する項目です。Sysplex 内のすべての結合機構 (CF) の名前・状態・所有構造数・占有率を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端分離の操作コマンドに関係する D XCF,CF の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、終端分離として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. D XCF,CF の名称と担当者名だけを残して終端分離の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端分離の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端分離の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では D XCF,CF は「D XCF,CF の用途を操作コマンドの表示で確認する終端分離項目」と D A,L または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景ではz/OS MVS Operationsの D XCF,CF と IEE115I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明だけに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では D XCF,CF を MVS オペレータコマンドで扱う確認対象とし、用語名は終端分離用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書照合の操作コマンドで操作コマンドの運用確認を行います。D XCF,CF の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書照合の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書照合の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D XCF,CF の属性行を読まず上書照合の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書照合の操作コマンドにおいて選択記号 C を採用し、識別名は上書照合です。上書照合の操作コマンドにおいて D XCF,CF は説明欄の「z/OS MVS Operationsで D XCF,CF の扱いを記録する上書照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の操作コマンドを受け取る担当者は、D XCF,CF の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の操作コマンドは別カテゴリの確認を流用しており、D XCF,CF の根拠にならないため上書照合ではありません。 B: 上書照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書照合ではありません。 C: 上書照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の操作コマンドが示す D XCF,CF は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D XCF,CF</strong></p><p>検証目的: 終端照合の操作コマンドについて、D XCF,CF は、MVS オペレータコマンドの D XCF で確認する項目です。Sysplex 内のすべての結合機構 (CF) の名前・状態・所有構造数・占有率を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040025の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD XCF,CFを指定し、OSKB040025の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D XCF,CF
CASE OSKB040025
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D XCF,CF
CASE OSKB040025
SOURCE z/OS MVS Operations
D XCF,CFとOSKB040025が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040025を同じ出力で読み、終端照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040025
→ Enter を押す
［画面・出力］
IEE115I OSKB040025 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040025   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040025が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D XCF,CF と OSKB040025 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040025 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D XCF,CF</strong></p><p>検証目的: 変更確認の操作コマンドについて、D XCF,CF は、MVS オペレータコマンドの D XCF で確認する項目です。Sysplex 内のすべての結合機構 (CF) の名前・状態・所有構造数・占有率を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020020の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD XCF,CFを指定し、OSKB020020の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D XCF,CF
CASE OSKB020020
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D XCF,CF
CASE OSKB020020
SOURCE z/OS MVS Operations
D XCF,CFとOSKB020020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020020を同じ出力で読み、変更確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020020
→ Enter を押す
［画面・出力］
IEE115I OSKB020020 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020020   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D XCF,CF と OSKB020020 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0154"><h3>D XCF,COUPLE</h3><p class="kb-meta">分類: D XCF ・ 難易度: 中級</p><p>D XCF,COUPLEは、COUPLExx で指定された Sysplex Couple DS、CFRM/SFM/LOGR/ARM Couple DS の現状を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査記録の操作コマンドで操作コマンドの運用確認を行います。D XCF,COUPLE の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査記録の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査記録の操作コマンドを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を監査記録で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. D XCF,COUPLE の属性行を読まず監査記録の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では D XCF,COUPLE は「z/OS MVS Operationsで D XCF,COUPLE の扱いを記録する監査記録項目」と D A,L または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では D XCF,COUPLE の表示結果と IEE115I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明だけに寄り、判定名は監査記録不足です。監査記録資料では D XCF,COUPLE の使い方を出典欄から追跡し、資料名は監査記録資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文照合の操作コマンドに関係する D XCF,COUPLE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D XCF,COUPLE の名称と担当者名のみを残して構文照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文照合の操作コマンドにおいて選択記号 A を採用し、識別名は構文照合です。構文照合の操作コマンドにおいて D XCF,COUPLE は説明欄の「D XCF,COUPLE の用途を操作コマンドの表示で確認する構文照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合の操作コマンドに関連して、z/OS MVS Operationsでは D XCF,COUPLE の表示属性と IEE115I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合の操作コマンドは別カテゴリの確認を流用しており、D XCF,COUPLE の根拠にならないため構文照合ではありません。 D: 構文照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文照合ではありません。構文照合の操作コマンドで使う D XCF,COUPLE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>D XCF,COUPLE</strong></p><p>検証目的: 置換照合の操作コマンドについて、D XCF,COUPLE は、COUPLExx で指定された Sysplex Couple DS、CFRM/SFM/LOGR/ARM Couple DS の現状を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040024の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD XCF,COUPLEを指定し、OSKB040024の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D XCF,COUPLE
CASE OSKB040024
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D XCF,COUPLE
CASE OSKB040024
SOURCE z/OS MVS Operations
D XCF,COUPLEとOSKB040024が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040024を同じ出力で読み、置換照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040024
→ Enter を押す
［画面・出力］
IEE115I OSKB040024 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040024   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040024が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D XCF,COUPLE と OSKB040024 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>D XCF,COUPLE</strong></p><p>検証目的: 比較確認の操作コマンドについて、D XCF,COUPLE は、COUPLExx で指定された Sysplex Couple DS、CFRM/SFM/LOGR/ARM Couple DS の現状を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020014の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD XCF,COUPLEを指定し、OSKB020014の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D XCF,COUPLE
CASE OSKB020014
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D XCF,COUPLE
CASE OSKB020014
SOURCE z/OS MVS Operations
D XCF,COUPLEとOSKB020014が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020014を同じ出力で読み、比較確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020014
→ Enter を押す
［画面・出力］
IEE115I OSKB020014 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020014   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020014が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D XCF,COUPLE と OSKB020014 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020014 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0155"><h3>D XCF,GROUP,name</h3><p class="kb-meta">分類: D XCF ・ 難易度: 中級</p><p>D XCF,GROUP,nameは、XCF グループ (例: IXCLO00x, SYSGRS) の現メンバ・システム別状態を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索分離の操作コマンドで D XCF 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D XCF 命令の出力を取らず探索分離の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索分離の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索分離の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索分離の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では D XCF 命令 は「探索分離の操作コマンドに関係する定義値と表示行を照合する探索分離項目」と D A,L または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では D XCF 命令の属性行と IEE115I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明だけに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では D XCF 命令を MVS オペレータコマンドの運用手順で確認し、初出名は探索分離初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力照合の操作コマンドに関する D XCF,GROUP,nameの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. D XCF,GROUP,nameの変更点を出力本文から切り離して出力照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力照合の操作コマンドにおいて選択記号 D を採用し、識別名は出力照合です。出力照合の操作コマンドにおいて D XCF,GROUP,name は説明欄の「D XCF,GROUP,nameの状態と出力メッセージを結び付ける出力照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合の操作コマンドに関する記録は、D XCF,GROUP,nameの出力行と IEE115I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力照合ではありません。 B: 出力照合の操作コマンドは別カテゴリの確認を流用しており、D XCF,GROUP,nameの根拠にならないため出力照合ではありません。 C: 出力照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合の操作コマンドで記録する D XCF,GROUP,nameはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D XCF,GROUP,name</strong></p><p>検証目的: 構文照合の操作コマンドについて、D XCF,GROUP,nameは、XCF グループ (例: IXCLO00x, SYSGRS) の現メンバ・システム別状態を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020021の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD XCF,GROUP,nameを指定し、OSKB020021の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D XCF,GROUP,name
CASE OSKB020021
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D XCF,GROUP,name
CASE OSKB020021
SOURCE z/OS MVS Operations
D XCF,GROUP,nameとOSKB020021が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020021を同じ出力で読み、構文照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020021
→ Enter を押す
［画面・出力］
IEE115I OSKB020021 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020021   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020021が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D XCF,GROUP,name と OSKB020021 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020021 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0156"><h3>D XCF,PATHIN</h3><p class="kb-meta">分類: D XCF ・ 難易度: 中級</p><p>D XCF,PATHINは、Sysplex の受信 (PATHIN) シグナリング・パスの状態 (XCF メッセージング経路) を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開分離の操作コマンドで D XCF,PATHIN の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D XCF,PATHIN の出力を取らず展開分離の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて展開分離の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開分離の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開分離の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では D XCF,PATHIN は「展開分離の操作コマンドに関係する定義値と表示行を照合する展開分離項目」と D A,L または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では D XCF,PATHIN の属性行と IEE115I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明だけに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では D XCF,PATHIN を MVS オペレータコマンドの運用手順で確認し、初出名は展開分離初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換照合の操作コマンドに関する D XCF,PATHIN の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. D XCF,PATHIN の変更点を出力本文から切り離して置換照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換照合の操作コマンドにおいて選択記号 D を採用し、識別名は置換照合です。置換照合の操作コマンドにおいて D XCF,PATHIN は説明欄の「D XCF,PATHIN の状態と出力メッセージを結び付ける置換照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合の操作コマンドに関する記録は、D XCF,PATHIN の出力行と IEE115I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換照合ではありません。 B: 置換照合の操作コマンドは別カテゴリの確認を流用しており、D XCF,PATHIN の根拠にならないため置換照合ではありません。 C: 置換照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合の操作コマンドで記録する D XCF,PATHIN はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D XCF,PATHIN</strong></p><p>検証目的: 警告確認の操作コマンドについて、D XCF,PATHIN は、Sysplex の受信 (PATHIN) シグナリング・パスの状態 (XCF メッセージング経路) を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020017の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD XCF,PATHINを指定し、OSKB020017の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D XCF,PATHIN
CASE OSKB020017
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D XCF,PATHIN
CASE OSKB020017
SOURCE z/OS MVS Operations
D XCF,PATHINとOSKB020017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020017を同じ出力で読み、警告確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020017
→ Enter を押す
［画面・出力］
IEE115I OSKB020017 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020017   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D XCF,PATHIN と OSKB020017 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0157"><h3>D XCF,PATHOUT</h3><p class="kb-meta">分類: D XCF ・ 難易度: 中級</p><p>D XCF,PATHOUTは、MVS オペレータコマンドのD XCFで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出分離の操作コマンドで操作コマンドの運用確認を行います。D XCF,PATHOUT の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出分離の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出分離の操作コマンドを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、呼出分離の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. D XCF,PATHOUT の属性行を読まず呼出分離の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では D XCF,PATHOUT は「z/OS MVS Operationsで D XCF,PATHOUT の扱いを記録する呼出分離項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では D XCF,PATHOUT の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明だけに寄り、判定名は呼出分離不足です。呼出分離資料では D XCF,PATHOUT の使い方を出典欄から追跡し、資料名は呼出分離資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端照合の操作コマンドに関係する D XCF,PATHOUT の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. D XCF,PATHOUT の名称と担当者名のみを残して終端照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端照合の操作コマンドにおいて選択記号 A を採用し、識別名は終端照合です。終端照合の操作コマンドにおいて D XCF,PATHOUT は説明欄の「D XCF,PATHOUT の用途を操作コマンドの表示で確認する終端照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合の操作コマンドに関連して、z/OS MVS Operationsでは D XCF,PATHOUT の表示属性と IEE115I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合の操作コマンドは別カテゴリの確認を流用しており、D XCF,PATHOUT の根拠にならないため終端照合ではありません。 D: 終端照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端照合ではありません。終端照合の操作コマンドで使う D XCF,PATHOUT という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D XCF,PATHOUT</strong></p><p>検証目的: 復旧確認の操作コマンドについて、D XCF,PATHOUT は、MVS オペレータコマンドの D XCF で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020018の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧確認の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD XCF,PATHOUTを指定し、OSKB020018の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D XCF,PATHOUT
CASE OSKB020018
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D XCF,PATHOUT
CASE OSKB020018
SOURCE z/OS MVS Operations
D XCF,PATHOUTとOSKB020018が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020018を同じ出力で読み、復旧確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020018
→ Enter を押す
［画面・出力］
IEE115I OSKB020018 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020018   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020018が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D XCF,PATHOUT と OSKB020018 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020018 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0158"><h3>D XCF,POLICY,TYPE=type</h3><p class="kb-meta">分類: D XCF ・ 難易度: 上級</p><p>D XCF,POLICY,TYPE=typeは、CFRM/SFM/LOGR/ARM の各ポリシー (TYPE 指定) の現行アクティブ・ポリシー名と内容を表示</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換分離の操作コマンドに関する D XCF 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換分離の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換分離の操作コマンドの証跡として保存して根拠にする。</li><li>C. D XCF 命令の変更点を出力本文から切り離して置換分離の操作コマンドの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、置換分離の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では D XCF 命令 は「D XCF 命令の状態と出力メッセージを結び付ける置換分離項目」と D A,L または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では D XCF 命令の出力行と IEE115I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明だけに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では D XCF 命令をz/OS MVS Operationsの確認記録に残し、対象名は置換分離対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索照合の操作コマンドで D XCF,POLICY,TYPE=typeの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D XCF,POLICY,TYPE=typeの出力を取らず探索照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索照合の操作コマンドにおいて選択記号 B を採用し、識別名は探索照合です。探索照合の操作コマンドにおいて D XCF,POLICY,TYPE=type は説明欄の「探索照合の操作コマンドに関係する定義値と表示行を照合する探索照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合の操作コマンドの証跡を読む担当者は、D XCF,POLICY,TYPE=typeの属性行と IEE115I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索照合ではありません。 D: 探索照合の操作コマンドは別カテゴリの確認を流用しており、D XCF,POLICY,TYPE=typeの根拠にならないため探索照合ではありません。探索照合の操作コマンドに出る D XCF,POLICY,TYPE=typeは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D XCF,POLICY,TYPE=type</strong></p><p>検証目的: 監査確認の操作コマンドについて、D XCF,POLICY,TYPE=typeは、CFRM/SFM/LOGR/ARM の各ポリシー (TYPE 指定) の現行アクティブ・ポリシー名と内容を表示に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020019の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査確認の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD XCF,POLICY,TYPE=を指定し、OSKB020019の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D XCF,POLICY,TYPE=
CASE OSKB020019
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D XCF,POLICY,TYPE=
CASE OSKB020019
SOURCE z/OS MVS Operations
D XCF,POLICY,TYPE=とOSKB020019が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020019を同じ出力で読み、監査確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020019
→ Enter を押す
［画面・出力］
IEE115I OSKB020019 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020019   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020019が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D XCF,POLICY,TYPE= と OSKB020019 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020019 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0159"><h3>D XCF,STR 全構造化リソース</h3><p class="kb-meta">分類: D XCF ・ 難易度: 中級</p><p>D XCF,STR 全構造化リソースは、MVS オペレータコマンドのD XCFで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更記録の全構造化リソースに関する D XCF 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更記録の全構造化リソースの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更記録の全構造化リソースの証跡として保存して根拠にする。</li><li>C. D XCF 命令の変更点を出力本文から切り離して変更記録の全構造化リソースの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、変更記録の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では D XCF 命令 は「D XCF 命令の状態と出力メッセージを結び付ける変更記録項目」と D A,L または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では D XCF 命令の出力行と IEE115I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明だけに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では D XCF 命令をz/OS MVS Operationsの確認記録に残し、対象名は変更記録対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開照合の全構造化リソースで D XCF,STR 全構造化リソースの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. D XCF,STR 全構造化リソースの出力を取らず展開照合の全構造化リソースの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開照合の全構造化リソースの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開照合の全構造化リソースへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開照合の全構造化リソースにおいて選択記号 B を採用し、識別名は展開照合です。展開照合の全構造化リソースにおいて D XCF,STR 全構造化リソース は説明欄の「展開照合の全構造化リソースに関係する定義値と表示行を照合する展開照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合の全構造化リソースの証跡を読む担当者は、D XCF,STR 全構造化リソースの属性行と IEE115I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合の全構造化リソースは名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合の全構造化リソースは対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合の全構造化リソースは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開照合ではありません。 D: 展開照合の全構造化リソースは別カテゴリの確認を流用しており、D XCF,STR 全構造化リソースの根拠にならないため展開照合ではありません。展開照合の全構造化リソースに出る D XCF,STR 全構造化リソースは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D XCF,STR 全構造化リソース</strong></p><p>検証目的: 順序確認の全構造化リソースについて、D XCF,STR 全構造化リソースは、MVS オペレータコマンドの D XCF で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020015の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序確認の全構造化リソースの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD XCF,STR 全構造化リソースを指定し、OSKB020015の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D XCF,STR 全構造化リソース
CASE OSKB020015
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D XCF,STR 全構造化リソース
CASE OSKB020015
SOURCE z/OS MVS Operations
D XCF,STR 全構造化リソースとOSKB020015が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020015を同じ出力で読み、順序確認の全構造化リソースの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020015
→ Enter を押す
［画面・出力］
IEE115I OSKB020015 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020015   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020015が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D XCF,STR 全構造化リソース と OSKB020015 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020015 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0160"><h3>D XCF,STR,STRNAME=name</h3><p class="kb-meta">分類: D XCF ・ 難易度: 中級</p><p>D XCF,STR,STRNAME=nameは、指定構造の詳細 (サイズ、コネクタ、リビルド状態、容量自動拡張設定) を表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文分離の操作コマンドに関係する D XCF 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、構文分離の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. D XCF 命令の名称と担当者名だけを残して構文分離の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文分離の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文分離の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では D XCF 命令 は「D XCF 命令の用途を操作コマンドの表示で確認する構文分離項目」と D A,L または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景ではz/OS MVS Operationsの D XCF 命令と IEE115I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明だけに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では D XCF 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は構文分離用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出照合の操作コマンドで操作コマンドの運用確認を行います。D XCF,STR,STRNAME=nameの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出照合の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出照合の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. D XCF,STR,STRNAME=nameの属性行を読まず呼出照合の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出照合の操作コマンドにおいて選択記号 C を採用し、識別名は呼出照合です。呼出照合の操作コマンドにおいて D XCF,STR,STRNAME=name は説明欄の「z/OS MVS Operationsで D XCF,STR,STRNAME=nameの扱いを記録する呼出照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合の操作コマンドを受け取る担当者は、D XCF,STR,STRNAME=nameの表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合の操作コマンドは別カテゴリの確認を流用しており、D XCF,STR,STRNAME=nameの根拠にならないため呼出照合ではありません。 B: 呼出照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合の操作コマンドが示す D XCF,STR,STRNAME=nameは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D XCF,STR,STRNAME=name</strong></p><p>検証目的: 値域確認の操作コマンドについて、D XCF,STR,STRNAME=nameは、指定構造の詳細 (サイズ、コネクタ、リビルド状態、容量自動拡張設定) を表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020016の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD XCF,STR,STRNAME=を指定し、OSKB020016の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D XCF,STR,STRNAME=
CASE OSKB020016
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D XCF,STR,STRNAME=
CASE OSKB020016
SOURCE z/OS MVS Operations
D XCF,STR,STRNAME=とOSKB020016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020016を同じ出力で読み、値域確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020016
→ Enter を押す
［画面・出力］
IEE115I OSKB020016 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020016   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D XCF,STR,STRNAME= と OSKB020016 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## F


<section class="kb-item" id="c22-i0161"><h3>F jobname,APPL=&#x27;string&#x27;</h3><p class="kb-meta">分類: F ・ 難易度: 中級</p><p>F jobname,APPL=&#x27;string&#x27;は、MVS オペレータコマンドのFで状態表示や操作を行うためのコマンド関連項目です。F jobname,APPL=&#x27;string&#x27;は、VTAM APPL や CICS など、サブシステムが APPL=&#x27;...&#x27; 形式の引数を受ける汎用形</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先確認再の操作コマンドに関する F jobname 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先確認再の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先確認再の操作コマンドの証跡として保存して根拠にする。</li><li>C. F jobname 命令の変更点を出力本文から切り離して優先確認再の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、優先確認再の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先確認再正解では選択記号 D を採用し、正解名は優先確認再正解です。優先確認再根拠では F jobname 命令 は「F jobname 命令の状態と出力メッセージを結び付ける優先確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は優先確認再根拠です。優先確認再保存では F jobname 命令の出力行と IEE115I を一緒に残し、保存名は優先確認再保存です。選択肢ごとの違いを示します。 A: 優先確認再欠落は戻り値や記録番号に寄り、欠落名は優先確認再欠落です。 B: 優先確認再流用は別カテゴリの確認であり、排除名は優先確認再流用です。 C: 優先確認再不足は名称や説明だけに寄り、判定名は優先確認再不足です。 D: 優先確認再正答は対象出力と項目説明を結び、根拠名は優先確認再正答です。優先確認再対象では F jobname 命令をz/OS MVS Operationsの確認記録に残し、対象名は優先確認再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>F jobname,APPL=&#x27;string&#x27;</strong></p><p>検証目的: 上書判定の操作コマンドについて、F jobname,APPL=&#x27;string&#x27;は、MVS オペレータコマンドの F で状態表示や操作を行うためのコマンド関連項目です。F jobname,APPL=&#x27;strinに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020087の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF jobname,APPL=&#x27;stを指定し、OSKB020087の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F jobname,APPL=&#x27;st
CASE OSKB020087
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F jobname,APPL=&#x27;st
CASE OSKB020087
SOURCE z/OS MVS Operations
F jobname,APPL=&#x27;stとOSKB020087が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020087を同じ出力で読み、上書判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020087
→ Enter を押す
［画面・出力］
IEE115I OSKB020087 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020087   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020087が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F jobname,APPL=&#x27;st と OSKB020087 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020087 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0162"><h3>F コマンド基本構文</h3><p class="kb-meta">分類: F ・ 難易度: 初級</p><p>F コマンド基本構文は、MVS オペレータコマンドのFで確認する項目です。F jobname,subcommand で稼動中アドレス・スペースに動的指示を渡す。サブシステムごとに固有のサブコマンドが定義される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲確認再のコマンド基本構文で操作コマンドの運用確認を行います。F コマンド基本構文の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲確認再のコマンド基本構文を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲確認再のコマンド基本構文を正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を範囲確認再で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. F コマンド基本構文の属性行を読まず範囲確認再のコマンド基本構文の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 範囲確認再正解では選択記号 C を採用し、正解名は範囲確認再正解です。範囲確認再根拠では F コマンド基本構文 は「z/OS MVS Operationsで F コマンド基本構文の扱いを記録する範囲確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は範囲確認再根拠です。範囲確認再受渡では F コマンド基本構文の表示結果と IEE115I を同じ確認単位にし、受渡名は範囲確認再受渡です。不適切な選択肢を整理します。 A: 範囲確認再流用は別カテゴリの確認であり、排除名は範囲確認再流用です。 B: 範囲確認再欠落は戻り値や記録番号に寄り、欠落名は範囲確認再欠落です。 C: 範囲確認再正答は対象出力と項目説明を結び、根拠名は範囲確認再正答です。 D: 範囲確認再不足は名称や説明だけに寄り、判定名は範囲確認再不足です。範囲確認再資料では F コマンド基本構文の使い方を出典欄から追跡し、資料名は範囲確認再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>F コマンド基本構文</strong></p><p>検証目的: 値域照合のコマンド基本構文について、F コマンド基本構文は、MVS オペレータコマンドの F で確認する項目です。F jobname,subcommand で稼動中アドレス・スペースに動的指示を渡す。サブシステムに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040036の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域照合のコマンド基本構文の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF コマンド基本構文を指定し、OSKB040036の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F コマンド基本構文
CASE OSKB040036
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F コマンド基本構文
CASE OSKB040036
SOURCE z/OS MVS Operations
F コマンド基本構文とOSKB040036が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040036を同じ出力で読み、値域照合のコマンド基本構文の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040036
→ Enter を押す
［画面・出力］
IEE115I OSKB040036 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040036   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040036が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F コマンド基本構文 と OSKB040036 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040036 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>F コマンド基本構文</strong></p><p>検証目的: 探索判定のコマンド基本構文について、F コマンド基本構文は、MVS オペレータコマンドの F で確認する項目です。F jobname,subcommand で稼動中アドレス・スペースに動的指示を渡す。サブシステムに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020086の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、探索判定のコマンド基本構文の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF コマンド基本構文を指定し、OSKB020086の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F コマンド基本構文
CASE OSKB020086
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F コマンド基本構文
CASE OSKB020086
SOURCE z/OS MVS Operations
F コマンド基本構文とOSKB020086が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020086を同じ出力で読み、探索判定のコマンド基本構文の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020086
→ Enter を押す
［画面・出力］
IEE115I OSKB020086 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020086   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020086が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F コマンド基本構文 と OSKB020086 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020086 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## F BPXOINIT


<section class="kb-item" id="c22-i0163"><h3>F BPXOINIT,FILESYS=...</h3><p class="kb-meta">分類: F BPXOINIT ・ 難易度: 中級</p><p>F BPXOINIT,FILESYS=...は、USS ファイルシステムに対する個別操作 (DISPLAY/UNMOUNT/MOVE) を行う MODIFY サブコマンド群</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文確認のなどに関係する F BPXOINIT,FILESYS= などの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. F BPXOINIT,FILESYS= などの名称と担当者名のみを残して構文確認のなどの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文確認のなどを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文確認のなどの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文確認のなどにおいて選択記号 A を採用し、識別名は構文確認です。構文確認のなどにおいて F BPXOINIT,FILESYS= など は説明欄の「F BPXOINIT,FILESYS= などの用途を操作コマンドの表示で確認する構文確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認のなどに関連して、z/OS MVS Operationsでは F BPXOINIT,FILESYS= などの表示属性と IEE115I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認のなどは対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認のなどは別カテゴリの確認を流用しており、F BPXOINIT,FILESYS= などの根拠にならないため構文確認ではありません。 D: 構文確認のなどは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文確認ではありません。構文確認のなどで使う F BPXOINIT,FILESYS= などという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details></section>


<section class="kb-item" id="c22-i0164"><h3>F BPXOINIT,SHUTDOWN=FORKINIT</h3><p class="kb-meta">分類: F BPXOINIT ・ 難易度: 中級</p><p>z/OS UNIX の初期化空間に対し、fork/exec サブシステムの停止を指示する。OMVS シャットダウン手順の中で使用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告確認再の操作コマンドに関係する F BPXOINIT 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、警告確認再として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. F BPXOINIT 命令の名称と担当者名だけを残して警告確認再の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告確認再の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告確認再の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告確認再正解では選択記号 A を採用し、正解名は警告確認再正解です。警告確認再根拠では F BPXOINIT 命令 は「F BPXOINIT 命令の用途を操作コマンドの表示で確認する警告確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は警告確認再根拠です。警告確認再背景ではz/OS MVS Operationsの F BPXOINIT 命令と IEE115I を同じ証跡に残し、背景名は警告確認再背景です。他の選択肢を確認します。 A: 警告確認再正答は対象出力と項目説明を結び、根拠名は警告確認再正答です。 B: 警告確認再不足は名称や説明だけに寄り、判定名は警告確認再不足です。 C: 警告確認再流用は別カテゴリの確認であり、排除名は警告確認再流用です。 D: 警告確認再欠落は戻り値や記録番号に寄り、欠落名は警告確認再欠落です。警告確認再用語では F BPXOINIT 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は警告確認再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>F BPXOINIT,SHUTDOWN=FORKINIT</strong></p><p>検証目的: 警告照合の操作コマンドについて、z/OS UNIX の初期化空間に対し、fork/exec サブシステムの停止を指示する。OMVS シャットダウン手順の中で使用に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040037の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF BPXOINIT,SHUTDOWを指定し、OSKB040037の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F BPXOINIT,SHUTDOW
CASE OSKB040037
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F BPXOINIT,SHUTDOW
CASE OSKB040037
SOURCE z/OS MVS Operations
F BPXOINIT,SHUTDOWとOSKB040037が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040037を同じ出力で読み、警告照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040037
→ Enter を押す
［画面・出力］
IEE115I OSKB040037 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040037   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040037が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F BPXOINIT,SHUTDOW と OSKB040037 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040037 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>F BPXOINIT,SHUTDOWN=FORKINIT</strong></p><p>検証目的: 優先判定の操作コマンドについて、z/OS UNIX の初期化空間に対し、fork/exec サブシステムの停止を指示する。OMVS シャットダウン手順の中で使用に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020092の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF BPXOINIT,SHUTDOWを指定し、OSKB020092の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F BPXOINIT,SHUTDOW
CASE OSKB020092
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F BPXOINIT,SHUTDOW
CASE OSKB020092
SOURCE z/OS MVS Operations
F BPXOINIT,SHUTDOWとOSKB020092が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020092を同じ出力で読み、優先判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020092
→ Enter を押す
［画面・出力］
IEE115I OSKB020092 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020092   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020092が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F BPXOINIT,SHUTDOW と OSKB020092 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020092 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0165"><h3>F BPXOINIT,SHUTDOWN=FORKS</h3><p class="kb-meta">分類: F BPXOINIT ・ 難易度: 中級</p><p>F BPXOINIT,SHUTDOWN=FORKSは、MVS オペレータコマンドのF BPXOINITで確認する項目です。全 z/OS UNIX プロセスを終了させる完全シャットダウン形式。USS 系サブシステム停止前の準備</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧確認再の操作コマンドで F BPXOINIT 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. F BPXOINIT 命令の出力を取らず復旧確認再の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧確認再の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧確認再の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧確認再の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧確認再正解では選択記号 B を採用し、正解名は復旧確認再正解です。復旧確認再根拠では F BPXOINIT 命令 は「復旧確認再の操作コマンドに関係する定義値と表示行を照合する復旧確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧確認再根拠です。復旧確認再追跡では F BPXOINIT 命令の属性行と IEE115I を合わせ、追跡名は復旧確認再追跡です。誤答側の問題点を分けます。 A: 復旧確認再不足は名称や説明だけに寄り、判定名は復旧確認再不足です。 B: 復旧確認再正答は対象出力と項目説明を結び、根拠名は復旧確認再正答です。 C: 復旧確認再欠落は戻り値や記録番号に寄り、欠落名は復旧確認再欠落です。 D: 復旧確認再流用は別カテゴリの確認であり、排除名は復旧確認再流用です。復旧確認再初出では F BPXOINIT 命令を MVS オペレータコマンドの運用手順で確認し、初出名は復旧確認再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>F BPXOINIT,SHUTDOWN=FORKS</strong></p><p>検証目的: 記録判定の操作コマンドについて、F BPXOINIT,SHUTDOWN=FORKS は、MVS オペレータコマンドの F BPXOINIT で確認する項目です。全 z/OS UNIX プロセスを終了させる完全シに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020093の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF BPXOINIT,SHUTDOWを指定し、OSKB020093の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F BPXOINIT,SHUTDOW
CASE OSKB020093
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F BPXOINIT,SHUTDOW
CASE OSKB020093
SOURCE z/OS MVS Operations
F BPXOINIT,SHUTDOWとOSKB020093が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020093を同じ出力で読み、記録判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020093
→ Enter を押す
［画面・出力］
IEE115I OSKB020093 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020093   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020093が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F BPXOINIT,SHUTDOW と OSKB020093 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020093 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## F CATALOG


<section class="kb-item" id="c22-i0166"><h3>F CATALOG,REPORT</h3><p class="kb-meta">分類: F CATALOG ・ 難易度: 中級</p><p>F CATALOG,REPORTは、Catalog Address Space (CAS) の状態・現行設定を表示する MODIFY サブコマンド</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更確認再の操作コマンドに関する F CATALOG 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更確認再の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更確認再の操作コマンドの証跡として保存して根拠にする。</li><li>C. F CATALOG 命令の変更点を出力本文から切り離して変更確認再の操作コマンドの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更確認再で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更確認再正解では選択記号 D を採用し、正解名は変更確認再正解です。変更確認再根拠では F CATALOG 命令 は「F CATALOG 命令の状態と出力メッセージを結び付ける変更確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は変更確認再根拠です。変更確認再保存では F CATALOG 命令の出力行と IEE115I を一緒に残し、保存名は変更確認再保存です。選択肢ごとの違いを示します。 A: 変更確認再欠落は戻り値や記録番号に寄り、欠落名は変更確認再欠落です。 B: 変更確認再流用は別カテゴリの確認であり、排除名は変更確認再流用です。 C: 変更確認再不足は名称や説明だけに寄り、判定名は変更確認再不足です。 D: 変更確認再正答は対象出力と項目説明を結び、根拠名は変更確認再正答です。変更確認再対象では F CATALOG 命令をz/OS MVS Operationsの確認記録に残し、対象名は変更確認再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開確認の操作コマンドで F CATALOG,REPORT の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. F CATALOG,REPORT の出力を取らず展開確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開確認の操作コマンドにおいて選択記号 B を採用し、識別名は展開確認です。展開確認の操作コマンドにおいて F CATALOG,REPORT は説明欄の「展開確認の操作コマンドに関係する定義値と表示行を照合する展開確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認の操作コマンドの証跡を読む担当者は、F CATALOG,REPORT の属性行と IEE115I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開確認ではありません。 D: 展開確認の操作コマンドは別カテゴリの確認を流用しており、F CATALOG,REPORT の根拠にならないため展開確認ではありません。展開確認の操作コマンドに出る F CATALOG,REPORT は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>F CATALOG,REPORT</strong></p><p>検証目的: 順序判定の操作コマンドについて、F CATALOG,REPORT は、Catalog Address Space (CAS) の状態・現行設定を表示する MODIFY サブコマンドに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020095の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序判定の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF CATALOG,REPORTを指定し、OSKB020095の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F CATALOG,REPORT
CASE OSKB020095
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F CATALOG,REPORT
CASE OSKB020095
SOURCE z/OS MVS Operations
F CATALOG,REPORTとOSKB020095が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020095を同じ出力で読み、順序判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020095
→ Enter を押す
［画面・出力］
IEE115I OSKB020095 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020095   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020095が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F CATALOG,REPORT と OSKB020095 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020095 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0167"><h3>F CATALOG,RESTART</h3><p class="kb-meta">分類: F CATALOG ・ 難易度: 中級</p><p>F CATALOG,RESTARTは、MVS オペレータコマンドのF CATALOGで確認する項目です。CAS を再起動する。カタログ・ロック解消や CAS 異常時のリカバリ手段</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文照合再の操作コマンドに関係する F CATALOG 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、構文照合再の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. F CATALOG 命令の名称と担当者名だけを残して構文照合再の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文照合再の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず構文照合再の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文照合再正解では選択記号 A を採用し、正解名は構文照合再正解です。構文照合再根拠では F CATALOG 命令 は「F CATALOG 命令の用途を操作コマンドの表示で確認する構文照合再項目」と D OPDATA または該当パネルの出力を照合し、根拠名は構文照合再根拠です。構文照合再背景ではz/OS MVS Operationsの F CATALOG 命令と IEE457I を同じ証跡に残し、背景名は構文照合再背景です。他の選択肢を確認します。 A: 構文照合再正答は対象出力と項目説明を結び、根拠名は構文照合再正答です。 B: 構文照合再不足は名称や説明だけに寄り、判定名は構文照合再不足です。 C: 構文照合再流用は別カテゴリの確認であり、排除名は構文照合再流用です。 D: 構文照合再欠落は戻り値や記録番号に寄り、欠落名は構文照合再欠落です。構文照合再用語では F CATALOG 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は構文照合再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出確認の操作コマンドで操作コマンドの運用確認を行います。F CATALOG,RESTART の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出確認の操作コマンドを確認した扱いにする。</li><li>B. IEE457I の有無を確認せず呼出確認の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. F CATALOG,RESTART の属性行を読まず呼出確認の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出確認の操作コマンドにおいて選択記号 C を採用し、識別名は呼出確認です。呼出確認の操作コマンドにおいて F CATALOG,RESTART は説明欄の「z/OS MVS Operationsで F CATALOG,RESTART の扱いを記録する呼出確認項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認の操作コマンドを受け取る担当者は、F CATALOG,RESTART の表示結果と IEE457I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認の操作コマンドは別カテゴリの確認を流用しており、F CATALOG,RESTART の根拠にならないため呼出確認ではありません。 B: 呼出確認の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認の操作コマンドが示す F CATALOG,RESTART は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>F CATALOG,RESTART</strong></p><p>検証目的: 値域判定の操作コマンドについて、F CATALOG,RESTART は、MVS オペレータコマンドの F CATALOG で確認する項目です。CAS を再起動する。カタログ・ロック解消や CAS 異常時のリカバに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020096の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、値域判定の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF CATALOG,RESTARTを指定し、OSKB020096の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F CATALOG,RESTART
CASE OSKB020096
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F CATALOG,RESTART
CASE OSKB020096
SOURCE z/OS MVS Operations
F CATALOG,RESTARTとOSKB020096が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020096を同じ出力で読み、値域判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020096
→ Enter を押す
［画面・出力］
IEE457I OSKB020096 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020096   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020096が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の F CATALOG,RESTART と OSKB020096 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020096 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0168"><h3>F CATALOG,UNALLOCATE</h3><p class="kb-meta">分類: F CATALOG ・ 難易度: 中級</p><p>F CATALOG,UNALLOCATEは、MVS オペレータコマンドのF CATALOGで確認する項目です。CAS が保持中の特定カタログ DSN を解放する。ALTER 等の前処理で使用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開照合再の操作コマンドで F CATALOG 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. F CATALOG 命令の出力を取らず展開照合再の操作コマンドの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて展開照合再の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開照合再の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開照合再の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開照合再正解では選択記号 B を採用し、正解名は展開照合再正解です。展開照合再根拠では F CATALOG 命令 は「展開照合再の操作コマンドに関係する定義値と表示行を照合する展開照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は展開照合再根拠です。展開照合再追跡では F CATALOG 命令の属性行と IEE115I を合わせ、追跡名は展開照合再追跡です。誤答側の問題点を分けます。 A: 展開照合再不足は名称や説明だけに寄り、判定名は展開照合再不足です。 B: 展開照合再正答は対象出力と項目説明を結び、根拠名は展開照合再正答です。 C: 展開照合再欠落は戻り値や記録番号に寄り、欠落名は展開照合再欠落です。 D: 展開照合再流用は別カテゴリの確認であり、排除名は展開照合再流用です。展開照合再初出では F CATALOG 命令を MVS オペレータコマンドの運用手順で確認し、初出名は展開照合再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換確認の操作コマンドに関する F CATALOG,UNALLOCATE の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換確認の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. F CATALOG,UNALLOCATE の変更点を出力本文から切り離して置換確認の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換確認の操作コマンドにおいて選択記号 D を採用し、識別名は置換確認です。置換確認の操作コマンドにおいて F CATALOG,UNALLOCATE は説明欄の「F CATALOG,UNALLOCATE の状態と出力メッセージを結び付ける置換確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認の操作コマンドに関する記録は、F CATALOG,UNALLOCATE の出力行と IEE115I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換確認ではありません。 B: 置換確認の操作コマンドは別カテゴリの確認を流用しており、F CATALOG,UNALLOCATE の根拠にならないため置換確認ではありません。 C: 置換確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認の操作コマンドで記録する F CATALOG,UNALLOCATE はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>F CATALOG,UNALLOCATE</strong></p><p>検証目的: 警告判定の操作コマンドについて、F CATALOG,UNALLOCATE は、MVS オペレータコマンドの F CATALOG で確認する項目です。CAS が保持中の特定カタログ DSN を解放する。ALTERに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020097の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告判定の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF CATALOG,UNALLOCAを指定し、OSKB020097の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F CATALOG,UNALLOCA
CASE OSKB020097
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F CATALOG,UNALLOCA
CASE OSKB020097
SOURCE z/OS MVS Operations
F CATALOG,UNALLOCAとOSKB020097が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020097を同じ出力で読み、警告判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020097
→ Enter を押す
［画面・出力］
IEE115I OSKB020097 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020097   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020097が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F CATALOG,UNALLOCA と OSKB020097 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020097 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## F LLA


<section class="kb-item" id="c22-i0169"><h3>F LLA,REFRESH</h3><p class="kb-meta">分類: F LLA ・ 難易度: 中級</p><p>F LLA,REFRESHは、MVS オペレータコマンドのF LLAで確認する項目です。LLA に LNKLST 内のモジュール変更を反映させる必須コマンド。これを実行しないと旧版が使われ続ける</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序確認再の操作コマンドで操作コマンドの運用確認を行います。F LLA,REFRESH の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序確認再の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序確認再の操作コマンドを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、順序確認再の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. F LLA,REFRESH の属性行を読まず順序確認再の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序確認再正解では選択記号 C を採用し、正解名は順序確認再正解です。順序確認再根拠では F LLA,REFRESH は「z/OS MVS Operationsで F LLA,REFRESH の扱いを記録する順序確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は順序確認再根拠です。順序確認再受渡では F LLA,REFRESH の表示結果と IEE115I を同じ確認単位にし、受渡名は順序確認再受渡です。不適切な選択肢を整理します。 A: 順序確認再流用は別カテゴリの確認であり、排除名は順序確認再流用です。 B: 順序確認再欠落は戻り値や記録番号に寄り、欠落名は順序確認再欠落です。 C: 順序確認再正答は対象出力と項目説明を結び、根拠名は順序確認再正答です。 D: 順序確認再不足は名称や説明だけに寄り、判定名は順序確認再不足です。順序確認再資料では F LLA,REFRESH の使い方を出典欄から追跡し、資料名は順序確認再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>F LLA,REFRESH</strong></p><p>検証目的: 区切判定の操作コマンドについて、F LLA,REFRESH は、MVS オペレータコマンドの F LLA で確認する項目です。LLA に LNKLST 内のモジュール変更を反映させる必須コマンド。これを実行しなに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020090の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切判定の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF LLA,REFRESHを指定し、OSKB020090の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F LLA,REFRESH
CASE OSKB020090
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F LLA,REFRESH
CASE OSKB020090
SOURCE z/OS MVS Operations
F LLA,REFRESHとOSKB020090が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020090を同じ出力で読み、区切判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020090
→ Enter を押す
［画面・出力］
IEE115I OSKB020090 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020090   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020090が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F LLA,REFRESH と OSKB020090 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020090 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0170"><h3>F LLA,UPDATE=xx</h3><p class="kb-meta">分類: F LLA ・ 難易度: 中級</p><p>F LLA,UPDATE=xxは、CSVLLAxx を活性化し、特定データセット / モジュールのみ更新対象とする選択リフレッシュ形式</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域確認再の操作コマンドに関する F LLA,UPDATE=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域確認再の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域確認再の操作コマンドの証跡として保存して根拠にする。</li><li>C. F LLA,UPDATE=xxの変更点を出力本文から切り離して値域確認再の操作コマンドの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、値域確認再の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域確認再正解では選択記号 D を採用し、正解名は値域確認再正解です。値域確認再根拠では F LLA,UPDATE=xx は「F LLA,UPDATE=xxの状態と出力メッセージを結び付ける値域確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は値域確認再根拠です。値域確認再保存では F LLA,UPDATE=xxの出力行と IEE115I を一緒に残し、保存名は値域確認再保存です。選択肢ごとの違いを示します。 A: 値域確認再欠落は戻り値や記録番号に寄り、欠落名は値域確認再欠落です。 B: 値域確認再流用は別カテゴリの確認であり、排除名は値域確認再流用です。 C: 値域確認再不足は名称や説明だけに寄り、判定名は値域確認再不足です。 D: 値域確認再正答は対象出力と項目説明を結び、根拠名は値域確認再正答です。値域確認再対象では F LLA,UPDATE=xxをz/OS MVS Operationsの確認記録に残し、対象名は値域確認再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>F LLA,UPDATE=xx</strong></p><p>検証目的: 範囲判定の操作コマンドについて、F LLA,UPDATE=xxは、CSVLLAxx を活性化し、特定データセット / モジュールのみ更新対象とする選択リフレッシュ形式に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020091の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF LLA,UPDATE=xxを指定し、OSKB020091の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F LLA,UPDATE=xx
CASE OSKB020091
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F LLA,UPDATE=xx
CASE OSKB020091
SOURCE z/OS MVS Operations
F LLA,UPDATE=xxとOSKB020091が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020091を同じ出力で読み、範囲判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020091
→ Enter を押す
［画面・出力］
IEE115I OSKB020091 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020091   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020091が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F LLA,UPDATE=xx と OSKB020091 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020091 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## F NET


<section class="kb-item" id="c22-i0171"><h3>F NET,USER,... VTAM 管理</h3><p class="kb-meta">分類: F NET ・ 難易度: 上級</p><p>F NET,USER,... VTAM 管理は、VTAM に対する SNA リソース個別制御 (例: F NET,USER,ID=name,ACT)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p></section>


<section class="kb-item" id="c22-i0172"><h3>F NET,VTAMOPTS</h3><p class="kb-meta">分類: F NET ・ 難易度: 上級</p><p>F NET,VTAMOPTSは、MVS オペレータコマンドのF NETで確認する項目です。VTAM の現行オプションを再定義する MODIFY 形式。VTAM 起動パラメータを動的変更する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較確認再の操作コマンドで F NET,VTAMOPTS の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. F NET,VTAMOPTS の出力を取らず比較確認再の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて比較確認再の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較確認再の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較確認再の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較確認再正解では選択記号 B を採用し、正解名は比較確認再正解です。比較確認再根拠では F NET,VTAMOPTS は「比較確認再の操作コマンドに関係する定義値と表示行を照合する比較確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は比較確認再根拠です。比較確認再追跡では F NET,VTAMOPTS の属性行と IEE115I を合わせ、追跡名は比較確認再追跡です。誤答側の問題点を分けます。 A: 比較確認再不足は名称や説明だけに寄り、判定名は比較確認再不足です。 B: 比較確認再正答は対象出力と項目説明を結び、根拠名は比較確認再正答です。 C: 比較確認再欠落は戻り値や記録番号に寄り、欠落名は比較確認再欠落です。 D: 比較確認再流用は別カテゴリの確認であり、排除名は比較確認再流用です。比較確認再初出では F NET,VTAMOPTS を MVS オペレータコマンドの運用手順で確認し、初出名は比較確認再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>F NET,VTAMOPTS</strong></p><p>検証目的: 条件判定の操作コマンドについて、F NET,VTAMOPTS は、MVS オペレータコマンドの F NET で確認する項目です。VTAM の現行オプションを再定義する MODIFY 形式。VTAM 起動パラメーに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020089の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF NET,VTAMOPTSを指定し、OSKB020089の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F NET,VTAMOPTS
CASE OSKB020089
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F NET,VTAMOPTS
CASE OSKB020089
SOURCE z/OS MVS Operations
F NET,VTAMOPTSとOSKB020089が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020089を同じ出力で読み、条件判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020089
→ Enter を押す
［画面・出力］
IEE115I OSKB020089 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020089   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020089が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F NET,VTAMOPTS と OSKB020089 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020089 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## F SDSF


<section class="kb-item" id="c22-i0173"><h3>F SDSF サブコマンド</h3><p class="kb-meta">分類: F SDSF ・ 難易度: 中級</p><p>F SDSF サブコマンドは、SDSF サーバ (SDSFAUX 等) に対するパラメータ変更・状態確認サブコマンド</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出照合再のサブコマンドで操作コマンドの運用確認を行います。F SDSF サブコマンドの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出照合再のサブコマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出照合再のサブコマンドを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を呼出照合再で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. F SDSF サブコマンドの属性行を読まず呼出照合再のサブコマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出照合再正解では選択記号 C を採用し、正解名は呼出照合再正解です。呼出照合再根拠では F SDSF サブコマンド は「z/OS MVS Operationsで F SDSF サブコマンドの扱いを記録する呼出照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出照合再根拠です。呼出照合再受渡では F SDSF サブコマンドの表示結果と IEE115I を同じ確認単位にし、受渡名は呼出照合再受渡です。不適切な選択肢を整理します。 A: 呼出照合再流用は別カテゴリの確認であり、排除名は呼出照合再流用です。 B: 呼出照合再欠落は戻り値や記録番号に寄り、欠落名は呼出照合再欠落です。 C: 呼出照合再正答は対象出力と項目説明を結び、根拠名は呼出照合再正答です。 D: 呼出照合再不足は名称や説明だけに寄り、判定名は呼出照合再不足です。呼出照合再資料では F SDSF サブコマンドの使い方を出典欄から追跡し、資料名は呼出照合再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端確認のサブコマンドに関係する F SDSF サブコマンドの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. F SDSF サブコマンドの名称と担当者名のみを残して終端確認のサブコマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端確認のサブコマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端確認のサブコマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端確認のサブコマンドにおいて選択記号 A を採用し、識別名は終端確認です。終端確認のサブコマンドにおいて F SDSF サブコマンド は説明欄の「F SDSF サブコマンドの用途を操作コマンドの表示で確認する終端確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認のサブコマンドに関連して、z/OS MVS Operationsでは F SDSF サブコマンドの表示属性と IEE115I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認のサブコマンドは対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認のサブコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認のサブコマンドは別カテゴリの確認を流用しており、F SDSF サブコマンドの根拠にならないため終端確認ではありません。 D: 終端確認のサブコマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端確認ではありません。終端確認のサブコマンドで使う F SDSF サブコマンドという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>F SDSF サブコマンド</strong></p><p>検証目的: 復旧照合のサブコマンドについて、F SDSF サブコマンドは、SDSF サーバ (SDSFAUX 等) に対するパラメータ変更・状態確認サブコマンドに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040038の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧照合のサブコマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF SDSF サブコマンドを指定し、OSKB040038の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F SDSF サブコマンド
CASE OSKB040038
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F SDSF サブコマンド
CASE OSKB040038
SOURCE z/OS MVS Operations
F SDSF サブコマンドとOSKB040038が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040038を同じ出力で読み、復旧照合のサブコマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040038
→ Enter を押す
［画面・出力］
IEE115I OSKB040038 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040038   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040038が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F SDSF サブコマンド と OSKB040038 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040038 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>F SDSF サブコマンド</strong></p><p>検証目的: 復旧判定のサブコマンドについて、F SDSF サブコマンドは、SDSF サーバ (SDSFAUX 等) に対するパラメータ変更・状態確認サブコマンドに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020098の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧判定のサブコマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF SDSF サブコマンドを指定し、OSKB020098の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F SDSF サブコマンド
CASE OSKB020098
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F SDSF サブコマンド
CASE OSKB020098
SOURCE z/OS MVS Operations
F SDSF サブコマンドとOSKB020098が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020098を同じ出力で読み、復旧判定のサブコマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020098
→ Enter を押す
［画面・出力］
IEE115I OSKB020098 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020098   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020098が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F SDSF サブコマンド と OSKB020098 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020098 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## F TSO


<section class="kb-item" id="c22-i0174"><h3>F TSO,USERMAX=n</h3><p class="kb-meta">分類: F TSO ・ 難易度: 中級</p><p>F TSO,USERMAX=nは、MVS オペレータコマンドのF TSOで確認する項目です。TSO/E サブシステムの最大同時 LOGON 数を動的変更する。負荷制御の応急処置</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換照合再の操作コマンドに関する F TSO,USERMAX=nの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換照合再の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換照合再の操作コマンドの証跡として保存して根拠にする。</li><li>C. F TSO,USERMAX=nの変更点を出力本文から切り離して置換照合再の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、置換照合再の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換照合再正解では選択記号 D を採用し、正解名は置換照合再正解です。置換照合再根拠では F TSO,USERMAX=n は「F TSO,USERMAX=nの状態と出力メッセージを結び付ける置換照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は置換照合再根拠です。置換照合再保存では F TSO,USERMAX=nの出力行と IEE115I を一緒に残し、保存名は置換照合再保存です。選択肢ごとの違いを示します。 A: 置換照合再欠落は戻り値や記録番号に寄り、欠落名は置換照合再欠落です。 B: 置換照合再流用は別カテゴリの確認であり、排除名は置換照合再流用です。 C: 置換照合再不足は名称や説明だけに寄り、判定名は置換照合再不足です。 D: 置換照合再正答は対象出力と項目説明を結び、根拠名は置換照合再正答です。置換照合再対象では F TSO,USERMAX=nをz/OS MVS Operationsの確認記録に残し、対象名は置換照合再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索確認の操作コマンドで F TSO,USERMAX=nの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. F TSO,USERMAX=nの出力を取らず探索確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索確認の操作コマンドにおいて選択記号 B を採用し、識別名は探索確認です。探索確認の操作コマンドにおいて F TSO,USERMAX=n は説明欄の「探索確認の操作コマンドに関係する定義値と表示行を照合する探索確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認の操作コマンドの証跡を読む担当者は、F TSO,USERMAX=nの属性行と IEE115I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索確認ではありません。 D: 探索確認の操作コマンドは別カテゴリの確認を流用しており、F TSO,USERMAX=nの根拠にならないため探索確認ではありません。探索確認の操作コマンドに出る F TSO,USERMAX=nは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>F TSO,USERMAX=n</strong></p><p>検証目的: 監査判定の操作コマンドについて、F TSO,USERMAX=nは、MVS オペレータコマンドの F TSO で確認する項目です。TSO/E サブシステムの最大同時 LOGON 数を動的変更する。負荷制御の応急に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020099の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査判定の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF TSO,USERMAX=nを指定し、OSKB020099の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F TSO,USERMAX=n
CASE OSKB020099
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F TSO,USERMAX=n
CASE OSKB020099
SOURCE z/OS MVS Operations
F TSO,USERMAX=nとOSKB020099が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020099を同じ出力で読み、監査判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020099
→ Enter を押す
［画面・出力］
IEE115I OSKB020099 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020099   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020099が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F TSO,USERMAX=n と OSKB020099 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020099 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## FORCE


<section class="kb-item" id="c22-i0175"><h3>FORCE jobname 目的</h3><p class="kb-meta">分類: FORCE ・ 難易度: 初級</p><p>FORCE jobname 目的は、MVS オペレータコマンドのFORCEで確認する項目です。CANCEL でも応答しないアドレス・スペースを強制的にメモリから除去する最終手段。クリーンアップは行われない</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力確認再の目的に関する FORCE jobname 目的の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力確認再の目的の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力確認再の目的の証跡として保存して根拠にする。</li><li>C. FORCE jobname 目的の変更点を出力本文から切り離して出力確認再の目的の承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力確認再で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 出力確認再正解では選択記号 D を採用し、正解名は出力確認再正解です。出力確認再根拠では FORCE jobname 目的 は「FORCE jobname 目的の状態と出力メッセージを結び付ける出力確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は出力確認再根拠です。出力確認再保存では FORCE jobname 目的の出力行と IEE115I を一緒に残し、保存名は出力確認再保存です。選択肢ごとの違いを示します。 A: 出力確認再欠落は戻り値や記録番号に寄り、欠落名は出力確認再欠落です。 B: 出力確認再流用は別カテゴリの確認であり、排除名は出力確認再流用です。 C: 出力確認再不足は名称や説明だけに寄り、判定名は出力確認再不足です。 D: 出力確認再正答は対象出力と項目説明を結び、根拠名は出力確認再正答です。出力確認再対象では FORCE jobname 目的をz/OS MVS Operationsの確認記録に残し、対象名は出力確認再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FORCE jobname 目的</strong></p><p>検証目的: 呼出判定の目的について、FORCE jobname 目的は、MVS オペレータコマンドの FORCE で確認する項目です。CANCEL でも応答しないアドレス・スペースを強制的にメモリから除去する最終に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020083の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にFORCE jobname 目的を指定し、OSKB020083の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND FORCE jobname 目的
CASE OSKB020083
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM FORCE jobname 目的
CASE OSKB020083
SOURCE z/OS MVS Operations
FORCE jobname 目的とOSKB020083が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020083を同じ出力で読み、呼出判定の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020083
→ Enter を押す
［画面・出力］
IEE115I OSKB020083 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020083   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020083が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の FORCE jobname 目的 と OSKB020083 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020083 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0176"><h3>FORCE jobname,ARM</h3><p class="kb-meta">分類: FORCE ・ 難易度: 中級</p><p>FORCE jobname,ARMは、MVS オペレータコマンドのFORCEで確認する項目です。ARM (Automatic Restart Manager) 連携を考慮した強制終了。ARM 再起動規則を尊重する形式</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件確認再の操作コマンドに関係する FORCE jobname 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、条件確認再の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. FORCE jobname 命令の名称と担当者名だけを残して条件確認再の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件確認再の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず条件確認再の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件確認再正解では選択記号 A を採用し、正解名は条件確認再正解です。条件確認再根拠では FORCE jobname 命令 は「FORCE jobname 命令の用途を操作コマンドの表示で確認する条件確認再項目」と D OPDATA または該当パネルの出力を照合し、根拠名は条件確認再根拠です。条件確認再背景ではz/OS MVS Operationsの FORCE jobname 命令と IEE457I を同じ証跡に残し、背景名は条件確認再背景です。他の選択肢を確認します。 A: 条件確認再正答は対象出力と項目説明を結び、根拠名は条件確認再正答です。 B: 条件確認再不足は名称や説明だけに寄り、判定名は条件確認再不足です。 C: 条件確認再流用は別カテゴリの確認であり、排除名は条件確認再流用です。 D: 条件確認再欠落は戻り値や記録番号に寄り、欠落名は条件確認再欠落です。条件確認再用語では FORCE jobname 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は条件確認再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FORCE jobname,ARM</strong></p><p>検証目的: 置換判定の操作コマンドについて、FORCE jobname,ARM は、MVS オペレータコマンドの FORCE で確認する項目です。ARM (Automatic Restart Manager) 連携を考慮しに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020084の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、置換判定の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にFORCE jobname,ARMを指定し、OSKB020084の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND FORCE jobname,ARM
CASE OSKB020084
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM FORCE jobname,ARM
CASE OSKB020084
SOURCE z/OS MVS Operations
FORCE jobname,ARMとOSKB020084が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020084を同じ出力で読み、置換判定の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020084
→ Enter を押す
［画面・出力］
IEE457I OSKB020084 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020084   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020084が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の FORCE jobname,ARM と OSKB020084 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020084 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0177"><h3>FORCE 実行前の禁止事項</h3><p class="kb-meta">分類: FORCE ・ 難易度: 中級</p><p>システムタスク (MASTER, GRS, CONSOLE 等) の FORCE は禁止。実行すると Sysplex がダウンする</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切確認再の実行前の禁止事項で FORCE 実行前の禁止事項の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. FORCE 実行前の禁止事項の出力を取らず区切確認再の実行前の禁止事項の説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて区切確認再の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切確認再の実行前の禁止事項の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切確認再の実行前の禁止事項へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切確認再正解では選択記号 B を採用し、正解名は区切確認再正解です。区切確認再根拠では FORCE 実行前の禁止事項 は「区切確認再の実行前の禁止事項に関係する定義値と表示行を照合する区切確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は区切確認再根拠です。区切確認再追跡では FORCE 実行前の禁止事項の属性行と IEE115I を合わせ、追跡名は区切確認再追跡です。誤答側の問題点を分けます。 A: 区切確認再不足は名称や説明だけに寄り、判定名は区切確認再不足です。 B: 区切確認再正答は対象出力と項目説明を結び、根拠名は区切確認再正答です。 C: 区切確認再欠落は戻り値や記録番号に寄り、欠落名は区切確認再欠落です。 D: 区切確認再流用は別カテゴリの確認であり、排除名は区切確認再流用です。区切確認再初出では FORCE 実行前の禁止事項を MVS オペレータコマンドの運用手順で確認し、初出名は区切確認再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FORCE 実行前の禁止事項</strong></p><p>検証目的: 終端判定の実行前の禁止事項について、システムタスク (MASTER, GRS, CONSOLE 等) の FORCE は禁止。実行すると Sysplex がダウンするに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020085の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端判定の実行前の禁止事項の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にFORCE 実行前の禁止事項を指定し、OSKB020085の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND FORCE 実行前の禁止事項
CASE OSKB020085
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM FORCE 実行前の禁止事項
CASE OSKB020085
SOURCE z/OS MVS Operations
FORCE 実行前の禁止事項とOSKB020085が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020085を同じ出力で読み、終端判定の実行前の禁止事項の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020085
→ Enter を押す
［画面・出力］
IEE115I OSKB020085 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020085   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020085が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の FORCE 実行前の禁止事項 と OSKB020085 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020085 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## INIT


<section class="kb-item" id="c22-i0178"><h3>$P I1 イニシエータ停止</h3><p class="kb-meta">分類: INIT ・ 難易度: 中級</p><p>$P I1 イニシエータ停止は、MVS オペレータコマンドのINITで確認する項目です。指定イニシエータを停止する。ドレイン後に停止する DRAIN モード</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換検査の$ イニシエータ停止に関する$P I1 イニシエータ停止の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換検査の$ イニシエータ停止の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換検査の$ イニシエータ停止の証跡として保存して根拠にする。</li><li>C. $P I1 イニシエータ停止の変更点を出力本文から切り離して置換検査の$ イニシエータ停止の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換検査の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換検査の$ イニシエータ停止において選択記号 D を採用し、識別名は置換検査です。置換検査の$ イニシエータ停止において$P I1 イニシエータ停止 は説明欄の「$P I1 イニシエータ停止の状態と出力メッセージを結び付ける置換検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換検査です。置換検査の$ イニシエータ停止に関する記録は、$P I1 イニシエータ停止の出力行と IEE115I を一緒に保存し、背景名は置換検査です。選択肢ごとの違いを示します。 A: 置換検査の$ イニシエータ停止は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換検査ではありません。 B: 置換検査の$ イニシエータ停止は別カテゴリの確認を流用しており、$P I1 イニシエータ停止の根拠にならないため置換検査ではありません。 C: 置換検査の$ イニシエータ停止は名称や説明のみに寄り、状態を示す出力本文が不足するため置換検査ではありません。 D: 置換検査の$ イニシエータ停止は対象出力と項目説明を結び、根拠を残すので置換検査です。置換検査の$ イニシエータ停止で記録する$P I1 イニシエータ停止はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>$P I1 イニシエータ停止</strong></p><p>検証目的: 警告照合の$ イニシエータ停止について、$P I1 イニシエータ停止は、MVS オペレータコマンドの INIT で確認する項目です。指定イニシエータを停止する。ドレイン後に停止する DRAIN モードに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030037の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告照合の$ イニシエータ停止の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に$P I1 イニシエータ停止を指定し、OSKB030037の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND $P I1 イニシエータ停止
CASE OSKB030037
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM $P I1 イニシエータ停止
CASE OSKB030037
SOURCE z/OS MVS Operations
$P I1 イニシエータ停止とOSKB030037が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030037を同じ出力で読み、警告照合の$ イニシエータ停止の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030037
→ Enter を押す
［画面・出力］
IEE115I OSKB030037 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030037   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030037が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の $P I1 イニシエータ停止 と OSKB030037 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030037 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0179"><h3>$S I1-n (JES2 イニシエータ起動)</h3><p class="kb-meta">分類: INIT ・ 難易度: 中級</p><p>$S I1-n (JES2 イニシエータ起動)は、MVS オペレータコマンドのINITで確認する項目です。JES2 イニシエータ番号 1〜n を一括起動する。バッチ処理能力の制御</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>$S I1-n (JES2 イニシエータ起動)</strong></p><p>検証目的: 値域照合の$ イニシエータ起動について、$S I1-n (JES2 イニシエータ起動)は、MVS オペレータコマンドの INIT で確認する項目です。JES2 イニシエータ番号 1〜n を一括起動する。バッチ処理能力に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030036の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域照合の$ イニシエータ起動の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に$S I1-n (JES2 イニシエを指定し、OSKB030036の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND $S I1-n (JES2 イニシエ
CASE OSKB030036
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM $S I1-n (JES2 イニシエ
CASE OSKB030036
SOURCE z/OS MVS Operations
$S I1-n (JES2 イニシエとOSKB030036が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030036を同じ出力で読み、値域照合の$ イニシエータ起動の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030036
→ Enter を押す
［画面・出力］
IEE115I OSKB030036 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030036   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030036が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の $S I1-n (JES2 イニシエ と OSKB030036 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030036 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0180"><h3>$T INITDEF (JES2)</h3><p class="kb-meta">分類: INIT ・ 難易度: 中級</p><p>$T INITDEF (JES2)は、JES2 イニシエータ定義を動的に変更する $T INITDEF コマンド (実体は JES2 コマンド)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開検査の$で$T INITDEF (JES2)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. $T INITDEF (JES2)の出力を取らず展開検査の$の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開検査の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開検査の$の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開検査の$へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開検査の$において選択記号 B を採用し、識別名は展開検査です。展開検査の$において$T INITDEF (JES2) は説明欄の「展開検査の$に関係する定義値と表示行を照合する展開検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開検査です。展開検査の$の証跡を読む担当者は、$T INITDEF (JES2)の属性行と IEE115I を合わせて追跡し、背景名は展開検査です。誤答側の問題点を分けます。 A: 展開検査の$は名称や説明のみに寄り、状態を示す出力本文が不足するため展開検査ではありません。 B: 展開検査の$は対象出力と項目説明を結び、根拠を残すので展開検査です。 C: 展開検査の$は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開検査ではありません。 D: 展開検査の$は別カテゴリの確認を流用しており、$T INITDEF (JES2)の根拠にならないため展開検査ではありません。展開検査の$に出る$T INITDEF (JES2)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>$T INITDEF (JES2)</strong></p><p>検証目的: 順序照合の$について、$T INITDEF (JES2)は、JES2 イニシエータ定義を動的に変更する $T INITDEF コマンド (実体は JES2 コマンド)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030035の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序照合の$の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に$T INITDEF (JES2)を指定し、OSKB030035の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND $T INITDEF (JES2)
CASE OSKB030035
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM $T INITDEF (JES2)
CASE OSKB030035
SOURCE z/OS MVS Operations
$T INITDEF (JES2)とOSKB030035が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030035を同じ出力で読み、順序照合の$の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030035
→ Enter を押す
［画面・出力］
IEE115I OSKB030035 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030035   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030035が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の $T INITDEF (JES2) と OSKB030035 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030035 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## IPL


<section class="kb-item" id="c22-i0181"><h3>CLPA 指定</h3><p class="kb-meta">分類: IPL ・ 難易度: 中級</p><p>IPL 時に LOAD パラメータまたは応答プロンプトで CLPA を指定し PLPA を再構築する。LPALSTxx 更新後の必須手順</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文追跡の指定に関係する CLPA 指定の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. CLPA 指定の名称と担当者名のみを残して構文追跡の指定の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文追跡の指定を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文追跡の指定の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文追跡の指定において選択記号 A を採用し、識別名は構文追跡です。構文追跡の指定において CLPA 指定 は説明欄の「CLPA 指定の用途を操作コマンドの表示で確認する構文追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡の指定に関連して、z/OS MVS Operationsでは CLPA 指定の表示属性と IEE115I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡の指定は対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡の指定は名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡の指定は別カテゴリの確認を流用しており、CLPA 指定の根拠にならないため構文追跡ではありません。 D: 構文追跡の指定は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文追跡ではありません。構文追跡の指定で使う CLPA 指定という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>CLPA 指定</strong></p><p>検証目的: 置換追跡の指定について、IPL 時に LOAD パラメータまたは応答プロンプトで CLPA を指定し PLPA を再構築する。LPALSTxx 更新後の必須手順に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040044の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換追跡の指定の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にCLPA 指定を指定し、OSKB040044の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CLPA 指定
CASE OSKB040044
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CLPA 指定
CASE OSKB040044
SOURCE z/OS MVS Operations
CLPA 指定とOSKB040044が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040044を同じ出力で読み、置換追跡の指定の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040044
→ Enter を押す
［画面・出力］
IEE115I OSKB040044 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040044   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040044が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の CLPA 指定 と OSKB040044 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040044 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>CLPA 指定</strong></p><p>検証目的: 比較確認の指定について、IPL 時に LOAD パラメータまたは応答プロンプトで CLPA を指定し PLPA を再構築する。LPALSTxx 更新後の必須手順に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030014の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較確認の指定の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にCLPA 指定を指定し、OSKB030014の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CLPA 指定
CASE OSKB030014
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CLPA 指定
CASE OSKB030014
SOURCE z/OS MVS Operations
CLPA 指定とOSKB030014が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030014を同じ出力で読み、比較確認の指定の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030014
→ Enter を押す
［画面・出力］
IEE115I OSKB030014 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030014   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030014が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の CLPA 指定 と OSKB030014 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030014 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0182"><h3>CVIO 指定</h3><p class="kb-meta">分類: IPL ・ 難易度: 中級</p><p>CVIO 指定は、MVS オペレータコマンドのIPLで確認する項目です。IPL 時に VIO データセットをクリアする指定。前回 IPL 時の残骸を消去する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開追跡の指定で CVIO 指定の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. CVIO 指定の出力を取らず展開追跡の指定の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開追跡の指定の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開追跡の指定へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開追跡の指定において選択記号 B を採用し、識別名は展開追跡です。展開追跡の指定において CVIO 指定 は説明欄の「展開追跡の指定に関係する定義値と表示行を照合する展開追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡の指定の証跡を読む担当者は、CVIO 指定の属性行と IEE115I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡の指定は名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡の指定は対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡の指定は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡の指定は別カテゴリの確認を流用しており、CVIO 指定の根拠にならないため展開追跡ではありません。展開追跡の指定に出る CVIO 指定は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CVIO 指定</strong></p><p>検証目的: 順序確認の指定について、CVIO 指定は、MVS オペレータコマンドの IPL で確認する項目です。IPL 時に VIO データセットをクリアする指定。前回 IPL 時の残骸を消去するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030015の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序確認の指定の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にCVIO 指定を指定し、OSKB030015の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND CVIO 指定
CASE OSKB030015
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM CVIO 指定
CASE OSKB030015
SOURCE z/OS MVS Operations
CVIO 指定とOSKB030015が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030015を同じ出力で読み、順序確認の指定の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030015
→ Enter を押す
［画面・出力］
IEE115I OSKB030015 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030015   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030015が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の CVIO 指定 と OSKB030015 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030015 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0183"><h3>LOAD パラメータ 4 桁</h3><p class="kb-meta">分類: IPL ・ 難易度: 中級</p><p>LOAD パラメータ 4 桁は、MVS オペレータコマンドのIPLで状態表示や操作を行うためのコマンド関連項目です。HMC LOAD 画面で指定する 8 桁のうち末尾 4 桁。先頭 2 桁が IODF SUFFIX、3 桁目が IEASYM SUFFIX、4 桁目が IEASYS SUFFIX のチェーン基点</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更照合のパラメータ 桁に関する LOAD パラメータ 4 桁の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更照合のパラメータ 桁の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更照合のパラメータ 桁の証跡として保存して根拠にする。</li><li>C. LOAD パラメータ 4 桁の変更点を出力本文から切り離して変更照合のパラメータ 桁の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、変更照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更照合のパラメータ 桁において選択記号 D を採用し、識別名は変更照合です。変更照合のパラメータ 桁において LOAD パラメータ 4 桁 は説明欄の「LOAD パラメータ 4 桁の状態と出力メッセージを結び付ける変更照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合のパラメータ 桁に関する記録は、LOAD パラメータ 4 桁の出力行と IEE115I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合のパラメータ 桁は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更照合ではありません。 B: 変更照合のパラメータ 桁は別カテゴリの確認を流用しており、LOAD パラメータ 4 桁の根拠にならないため変更照合ではありません。 C: 変更照合のパラメータ 桁は名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合のパラメータ 桁は対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合のパラメータ 桁で記録する LOAD パラメータ 4 桁はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LOAD パラメータ 4 桁</strong></p><p>検証目的: 記録確認のパラメータ 桁について、LOAD パラメータ 4 桁は、MVS オペレータコマンドの IPL で状態表示や操作を行うためのコマンド関連項目です。HMC LOAD 画面で指定する 8 桁のうち末尾 4に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030013の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録確認のパラメータ 桁の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にLOAD パラメータ 4 桁を指定し、OSKB030013の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND LOAD パラメータ 4 桁
CASE OSKB030013
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM LOAD パラメータ 4 桁
CASE OSKB030013
SOURCE z/OS MVS Operations
LOAD パラメータ 4 桁とOSKB030013が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030013を同じ出力で読み、記録確認のパラメータ 桁の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030013
→ Enter を押す
［画面・出力］
IEE115I OSKB030013 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030013   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030013が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の LOAD パラメータ 4 桁 と OSKB030013 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030013 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0184"><h3>PARMLIB SUFFIX 指定</h3><p class="kb-meta">分類: IPL ・ 難易度: 中級</p><p>PARMLIB SUFFIX 指定は、MVS オペレータコマンドのIPLで確認する項目です。IEASYSxx の SUFFIX で連結する PARMLIB メンバの組合せを決定する。本番/災対で使い分ける典型</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端追跡の指定に関係する PARMLIB SUFFIX 指定の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. PARMLIB SUFFIX 指定の名称と担当者名のみを残して終端追跡の指定の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端追跡の指定を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端追跡の指定の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端追跡の指定において選択記号 A を採用し、識別名は終端追跡です。終端追跡の指定において PARMLIB SUFFIX 指定 は説明欄の「PARMLIB SUFFIX 指定の用途を操作コマンドの表示で確認する終端追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡の指定に関連して、z/OS MVS Operationsでは PARMLIB SUFFIX 指定の表示属性と IEE115I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡の指定は対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡の指定は名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡の指定は別カテゴリの確認を流用しており、PARMLIB SUFFIX 指定の根拠にならないため終端追跡ではありません。 D: 終端追跡の指定は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端追跡ではありません。終端追跡の指定で使う PARMLIB SUFFIX 指定という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PARMLIB SUFFIX 指定</strong></p><p>検証目的: 復旧確認の指定について、PARMLIB SUFFIX 指定は、MVS オペレータコマンドの IPL で確認する項目です。IEASYSxx の SUFFIX で連結する PARMLIB メンバの組合せをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030018の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧確認の指定の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にPARMLIB SUFFIX 指定を指定し、OSKB030018の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND PARMLIB SUFFIX 指定
CASE OSKB030018
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM PARMLIB SUFFIX 指定
CASE OSKB030018
SOURCE z/OS MVS Operations
PARMLIB SUFFIX 指定とOSKB030018が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030018を同じ出力で読み、復旧確認の指定の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030018
→ Enter を押す
［画面・出力］
IEE115I OSKB030018 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030018   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030018が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の PARMLIB SUFFIX 指定 と OSKB030018 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030018 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0185"><h3>PARMLIB プロンプト (IEA101A)</h3><p class="kb-meta">分類: IPL ・ 難易度: 中級</p><p>PARMLIB プロンプト (IEA101A)は、MVS オペレータコマンドのIPLで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換追跡のプロンプトに関する PARMLIB プロンプト (IEA101A)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換追跡のプロンプトの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換追跡のプロンプトの証跡として保存して根拠にする。</li><li>C. PARMLIB プロンプト (IEA101A)の変更点を出力本文から切り離して置換追跡のプロンプトの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換追跡のプロンプトにおいて選択記号 D を採用し、識別名は置換追跡です。置換追跡のプロンプトにおいて PARMLIB プロンプト (IEA101A) は説明欄の「PARMLIB プロンプト (IEA101A)の状態と出力メッセージを結び付ける置換追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡のプロンプトに関する記録は、PARMLIB プロンプト (IEA101A)の出力行と IEE115I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡のプロンプトは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡のプロンプトは別カテゴリの確認を流用しており、PARMLIB プロンプト (IEA101A)の根拠にならないため置換追跡ではありません。 C: 置換追跡のプロンプトは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡のプロンプトは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡のプロンプトで記録する PARMLIB プロンプト (IEA101A)はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PARMLIB プロンプト (IEA101A)</strong></p><p>検証目的: 警告確認のプロンプトについて、PARMLIB プロンプト (IEA101A)は、MVS オペレータコマンドの IPL で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030017の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告確認のプロンプトの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にPARMLIB プロンプト (IEAを指定し、OSKB030017の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND PARMLIB プロンプト (IEA
CASE OSKB030017
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM PARMLIB プロンプト (IEA
CASE OSKB030017
SOURCE z/OS MVS Operations
PARMLIB プロンプト (IEAとOSKB030017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030017を同じ出力で読み、警告確認のプロンプトの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030017
→ Enter を押す
［画面・出力］
IEE115I OSKB030017 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030017   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の PARMLIB プロンプト (IEA と OSKB030017 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0186"><h3>SYSP プロンプト</h3><p class="kb-meta">分類: IPL ・ 難易度: 中級</p><p>IPL 時の SYSP= プロンプトに対し IEASYS SUFFIX のチェーンを指定する。例: SYSP=(P1,SS,..)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出追跡のプロンプトで操作コマンドの運用確認を行います。SYSP プロンプトの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出追跡のプロンプトを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出追跡のプロンプトを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. SYSP プロンプトの属性行を読まず呼出追跡のプロンプトの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出追跡のプロンプトにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のプロンプトにおいて SYSP プロンプト は説明欄の「z/OS MVS Operationsで SYSP プロンプトの扱いを記録する呼出追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のプロンプトを受け取る担当者は、SYSP プロンプトの表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のプロンプトは別カテゴリの確認を流用しており、SYSP プロンプトの根拠にならないため呼出追跡ではありません。 B: 呼出追跡のプロンプトは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のプロンプトは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のプロンプトは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のプロンプトが示す SYSP プロンプトは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SYSP プロンプト</strong></p><p>検証目的: 値域確認のプロンプトについて、IPL 時の SYSP= プロンプトに対し IEASYS SUFFIX のチェーンを指定する。例: SYSP=(P1,SS,..)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030016の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域確認のプロンプトの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSYSP プロンプトを指定し、OSKB030016の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SYSP プロンプト
CASE OSKB030016
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SYSP プロンプト
CASE OSKB030016
SOURCE z/OS MVS Operations
SYSP プロンプトとOSKB030016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030016を同じ出力で読み、値域確認のプロンプトの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030016
→ Enter を押す
［画面・出力］
IEE115I OSKB030016 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030016   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の SYSP プロンプト と OSKB030016 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## JES2


<section class="kb-item" id="c22-i0187"><h3>$D A 活動状況</h3><p class="kb-meta">分類: JES2 ・ 難易度: 中級</p><p>$D A 活動状況は、JES2 イニシエータの活動状況、各クラスの稼動ジョブ一覧を表示する JES2 コマンド (MVS コマンドではなく JES2 サブコマンド)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切判定の$ 活動状況で$D A 活動状況の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. $D A 活動状況の出力を取らず区切判定の$ 活動状況の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切判定の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切判定の$ 活動状況の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切判定の$ 活動状況へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切判定の$ 活動状況において選択記号 B を採用し、識別名は区切判定です。区切判定の$ 活動状況において$D A 活動状況 は説明欄の「区切判定の$ 活動状況に関係する定義値と表示行を照合する区切判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切判定です。区切判定の$ 活動状況の証跡を読む担当者は、$D A 活動状況の属性行と IEE115I を合わせて追跡し、背景名は区切判定です。誤答側の問題点を分けます。 A: 区切判定の$ 活動状況は名称や説明のみに寄り、状態を示す出力本文が不足するため区切判定ではありません。 B: 区切判定の$ 活動状況は対象出力と項目説明を結び、根拠を残すので区切判定です。 C: 区切判定の$ 活動状況は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切判定ではありません。 D: 区切判定の$ 活動状況は別カテゴリの確認を流用しており、$D A 活動状況の根拠にならないため区切判定ではありません。区切判定の$ 活動状況に出る$D A 活動状況は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>$D A 活動状況</strong></p><p>検証目的: 呼出検査の$ 活動状況について、$D A 活動状況は、JES2 イニシエータの活動状況、各クラスの稼動ジョブ一覧を表示する JES2 コマンド (MVS コマンドではなく JES2 サブコマンド)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030063の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出検査の$ 活動状況の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に$D A 活動状況を指定し、OSKB030063の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND $D A 活動状況
CASE OSKB030063
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM $D A 活動状況
CASE OSKB030063
SOURCE z/OS MVS Operations
$D A 活動状況とOSKB030063が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030063を同じ出力で読み、呼出検査の$ 活動状況の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030063
→ Enter を押す
［画面・出力］
IEE115I OSKB030063 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030063   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030063が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の $D A 活動状況 と OSKB030063 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030063 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0188"><h3>$D Q キュー状況</h3><p class="kb-meta">分類: JES2 ・ 難易度: 中級</p><p>$D Q キュー状況は、MVS オペレータコマンドのJES2で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲判定の$ キュー状況で操作コマンドの運用確認を行います。$D Q キュー状況の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲判定の$ キュー状況を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲判定の$ キュー状況を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲判定の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. $D Q キュー状況の属性行を読まず範囲判定の$ キュー状況の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲判定の$ キュー状況において選択記号 C を採用し、識別名は範囲判定です。範囲判定の$ キュー状況において$D Q キュー状況 は説明欄の「z/OS MVS Operationsで$D Q キュー状況の扱いを記録する範囲判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲判定です。範囲判定の$ キュー状況を受け取る担当者は、$D Q キュー状況の表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲判定です。不適切な選択肢を整理します。 A: 範囲判定の$ キュー状況は別カテゴリの確認を流用しており、$D Q キュー状況の根拠にならないため範囲判定ではありません。 B: 範囲判定の$ キュー状況は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲判定ではありません。 C: 範囲判定の$ キュー状況は対象出力と項目説明を結び、根拠を残すので範囲判定です。 D: 範囲判定の$ キュー状況は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲判定ではありません。範囲判定の$ キュー状況が示す$D Q キュー状況は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>$D Q キュー状況</strong></p><p>検証目的: 置換検査の$ キュー状況について、$D Q キュー状況は、MVS オペレータコマンドの JES2 で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030064の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換検査の$ キュー状況の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に$D Q キュー状況を指定し、OSKB030064の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND $D Q キュー状況
CASE OSKB030064
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM $D Q キュー状況
CASE OSKB030064
SOURCE z/OS MVS Operations
$D Q キュー状況とOSKB030064が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030064を同じ出力で読み、置換検査の$ キュー状況の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030064
→ Enter を押す
［画面・出力］
IEE115I OSKB030064 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030064   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030064が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の $D Q キュー状況 と OSKB030064 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030064 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0189"><h3>$P JES2 ドレイン</h3><p class="kb-meta">分類: JES2 ・ 難易度: 中級</p><p>$P JES2 ドレインは、MVS オペレータコマンドのJES2で確認する項目です。JES2 の新規受付を停止しドレインさせる。Z EOD 前に投入する典型シーケンス</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先判定の$ ドレインに関する$P JES2 ドレインの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先判定の$ ドレインの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先判定の$ ドレインの証跡として保存して根拠にする。</li><li>C. $P JES2 ドレインの変更点を出力本文から切り離して優先判定の$ ドレインの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先判定の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先判定の$ ドレインにおいて選択記号 D を採用し、識別名は優先判定です。優先判定の$ ドレインにおいて$P JES2 ドレイン は説明欄の「$P JES2 ドレインの状態と出力メッセージを結び付ける優先判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先判定です。優先判定の$ ドレインに関する記録は、$P JES2 ドレインの出力行と IEE115I を一緒に保存し、背景名は優先判定です。選択肢ごとの違いを示します。 A: 優先判定の$ ドレインは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先判定ではありません。 B: 優先判定の$ ドレインは別カテゴリの確認を流用しており、$P JES2 ドレインの根拠にならないため優先判定ではありません。 C: 優先判定の$ ドレインは名称や説明のみに寄り、状態を示す出力本文が不足するため優先判定ではありません。 D: 優先判定の$ ドレインは対象出力と項目説明を結び、根拠を残すので優先判定です。優先判定の$ ドレインで記録する$P JES2 ドレインはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>$P JES2 ドレイン</strong></p><p>検証目的: 終端検査の$ ドレインについて、$P JES2 ドレインは、MVS オペレータコマンドの JES2 で確認する項目です。JES2 の新規受付を停止しドレインさせる。Z EOD 前に投入する典型シーケンスに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030065の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端検査の$ ドレインの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に$P JES2 ドレインを指定し、OSKB030065の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND $P JES2 ドレイン
CASE OSKB030065
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM $P JES2 ドレイン
CASE OSKB030065
SOURCE z/OS MVS Operations
$P JES2 ドレインとOSKB030065が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030065を同じ出力で読み、終端検査の$ ドレインの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030065
→ Enter を押す
［画面・出力］
IEE115I OSKB030065 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030065   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030065が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の $P JES2 ドレイン と OSKB030065 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030065 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## K


<section class="kb-item" id="c22-i0190"><h3>K A,NONE ロール解除</h3><p class="kb-meta">分類: K ・ 難易度: 中級</p><p>K A,NONE ロール解除は、MVS オペレータコマンドのKで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出判定のロール解除で操作コマンドの運用確認を行います。K A,NONE ロール解除の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出判定のロール解除を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出判定のロール解除を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出判定の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. K A,NONE ロール解除の属性行を読まず呼出判定のロール解除の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出判定のロール解除において選択記号 C を採用し、識別名は呼出判定です。呼出判定のロール解除において K A,NONE ロール解除 は説明欄の「z/OS MVS Operationsで K A,NONE ロール解除の扱いを記録する呼出判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出判定です。呼出判定のロール解除を受け取る担当者は、K A,NONE ロール解除の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出判定です。不適切な選択肢を整理します。 A: 呼出判定のロール解除は別カテゴリの確認を流用しており、K A,NONE ロール解除の根拠にならないため呼出判定ではありません。 B: 呼出判定のロール解除は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出判定ではありません。 C: 呼出判定のロール解除は対象出力と項目説明を結び、根拠を残すので呼出判定です。 D: 呼出判定のロール解除は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出判定ではありません。呼出判定のロール解除が示す K A,NONE ロール解除は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>K A,NONE ロール解除</strong></p><p>検証目的: 値域追跡のロール解除について、K A,NONE ロール解除は、MVS オペレータコマンドの K で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認しますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030056の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域追跡のロール解除の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にK A,NONE ロール解除を指定し、OSKB030056の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND K A,NONE ロール解除
CASE OSKB030056
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM K A,NONE ロール解除
CASE OSKB030056
SOURCE z/OS MVS Operations
K A,NONE ロール解除とOSKB030056が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030056を同じ出力で読み、値域追跡のロール解除の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030056
→ Enter を押す
［画面・出力］
IEE115I OSKB030056 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030056   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030056が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の K A,NONE ロール解除 と OSKB030056 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030056 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0191"><h3>K E,D 削除</h3><p class="kb-meta">分類: K ・ 難易度: 中級</p><p>K E,D 削除は、MVS オペレータコマンドのKで確認する項目です。K E,D で表示メッセージを消去 (Erase) する形式。視認性を上げるための運用補助</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文判定の削除に関係する K E,D 削除の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文判定として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. K E,D 削除の名称と担当者名のみを残して構文判定の削除の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文判定の削除を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文判定の削除の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文判定の削除において選択記号 A を採用し、識別名は構文判定です。構文判定の削除において K E,D 削除 は説明欄の「K E,D 削除の用途を操作コマンドの表示で確認する構文判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文判定です。構文判定の削除に関連して、z/OS MVS Operationsでは K E,D 削除の表示属性と IEE115I を同じ証跡に残し、背景名は構文判定です。他の選択肢を確認します。 A: 構文判定の削除は対象出力と項目説明を結び、根拠を残すので構文判定です。 B: 構文判定の削除は名称や説明のみに寄り、状態を示す出力本文が不足するため構文判定ではありません。 C: 構文判定の削除は別カテゴリの確認を流用しており、K E,D 削除の根拠にならないため構文判定ではありません。 D: 構文判定の削除は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文判定ではありません。構文判定の削除で使う K E,D 削除という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>K E,D 削除</strong></p><p>検証目的: 比較追跡の削除について、K E,D 削除は、MVS オペレータコマンドの K で確認する項目です。K E,D で表示メッセージを消去 (Erase) する形式。視認性を上げるための運用補助に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030054の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較追跡の削除の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にK E,D 削除を指定し、OSKB030054の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND K E,D 削除
CASE OSKB030054
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM K E,D 削除
CASE OSKB030054
SOURCE z/OS MVS Operations
K E,D 削除とOSKB030054が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030054を同じ出力で読み、比較追跡の削除の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030054
→ Enter を押す
［画面・出力］
IEE115I OSKB030054 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030054   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030054が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の K E,D 削除 と OSKB030054 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030054 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0192"><h3>K M,REF メッセージ再表示</h3><p class="kb-meta">分類: K ・ 難易度: 中級</p><p>K M,REF メッセージ再表示は、MVS オペレータコマンドのKで確認する項目です。K M,REF で未応答 WTOR / アクション・メッセージを再描画する。流れ去ったメッセージの確認に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更検査のメッセージ再表示に関する K M,REF メッセージ再表示の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更検査のメッセージ再表示の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更検査のメッセージ再表示の証跡として保存して根拠にする。</li><li>C. K M,REF メッセージ再表示の変更点を出力本文から切り離して変更検査のメッセージ再表示の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、変更検査の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更検査のメッセージ再表示において選択記号 D を採用し、識別名は変更検査です。変更検査のメッセージ再表示において K M,REF メッセージ再表示 は説明欄の「K M,REF メッセージ再表示の状態と出力メッセージを結び付ける変更検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更検査です。変更検査のメッセージ再表示に関する記録は、K M,REF メッセージ再表示の出力行と IEE115I を一緒に保存し、背景名は変更検査です。選択肢ごとの違いを示します。 A: 変更検査のメッセージ再表示は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更検査ではありません。 B: 変更検査のメッセージ再表示は別カテゴリの確認を流用しており、K M,REF メッセージ再表示の根拠にならないため変更検査ではありません。 C: 変更検査のメッセージ再表示は名称や説明のみに寄り、状態を示す出力本文が不足するため変更検査ではありません。 D: 変更検査のメッセージ再表示は対象出力と項目説明を結び、根拠を残すので変更検査です。変更検査のメッセージ再表示で記録する K M,REF メッセージ再表示はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>K M,REF メッセージ再表示</strong></p><p>検証目的: 記録追跡のメッセージ再表示について、K M,REF メッセージ再表示は、MVS オペレータコマンドの K で確認する項目です。K M,REF で未応答 WTOR / アクション・メッセージを再描画する。流れ去ったに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030053の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録追跡のメッセージ再表示の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にK M,REF メッセージ再表示を指定し、OSKB030053の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND K M,REF メッセージ再表示
CASE OSKB030053
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM K M,REF メッセージ再表示
CASE OSKB030053
SOURCE z/OS MVS Operations
K M,REF メッセージ再表示とOSKB030053が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030053を同じ出力で読み、記録追跡のメッセージ再表示の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030053
→ Enter を押す
［画面・出力］
IEE115I OSKB030053 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030053   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030053が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の K M,REF メッセージ再表示 と OSKB030053 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030053 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0193"><h3>K N,PFK=(xx) PFK 切替</h3><p class="kb-meta">分類: K ・ 難易度: 中級</p><p>K N,PFK=(xx) PFK 切替は、MVS オペレータコマンドのKで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開判定の切替で K N,PFK=(xx) PFK 切替の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. K N,PFK=(xx) PFK 切替の出力を取らず展開判定の切替の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開判定の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開判定の切替の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開判定の切替へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開判定の切替において選択記号 B を採用し、識別名は展開判定です。展開判定の切替において K N,PFK=(xx) PFK 切替 は説明欄の「展開判定の切替に関係する定義値と表示行を照合する展開判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開判定です。展開判定の切替の証跡を読む担当者は、K N,PFK=(xx) PFK 切替の属性行と IEE115I を合わせて追跡し、背景名は展開判定です。誤答側の問題点を分けます。 A: 展開判定の切替は名称や説明のみに寄り、状態を示す出力本文が不足するため展開判定ではありません。 B: 展開判定の切替は対象出力と項目説明を結び、根拠を残すので展開判定です。 C: 展開判定の切替は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開判定ではありません。 D: 展開判定の切替は別カテゴリの確認を流用しており、K N,PFK=(xx) PFK 切替の根拠にならないため展開判定ではありません。展開判定の切替に出る K N,PFK=(xx) PFK 切替は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>K N,PFK=(xx) PFK 切替</strong></p><p>検証目的: 順序追跡の切替について、K N,PFK=(xx) PFK 切替は、MVS オペレータコマンドの K で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けてに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030055の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序追跡の切替の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にK N,PFK=(xx) PFK 切を指定し、OSKB030055の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND K N,PFK=(xx) PFK 切
CASE OSKB030055
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM K N,PFK=(xx) PFK 切
CASE OSKB030055
SOURCE z/OS MVS Operations
K N,PFK=(xx) PFK 切とOSKB030055が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030055を同じ出力で読み、順序追跡の切替の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030055
→ Enter を押す
［画面・出力］
IEE115I OSKB030055 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030055   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030055が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の K N,PFK=(xx) PFK 切 と OSKB030055 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030055 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0194"><h3>K S,DEL=...</h3><p class="kb-meta">分類: K ・ 難易度: 中級</p><p>MVS オペレータコマンドのKでは、対象資源、指定値、実行時の出力を対応付けて確認します。Kは、MVS オペレータコマンドの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、K S,DEL=...の表記と許可される値を確認します。</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査検査のなどで操作コマンドの運用確認を行います。K S,DEL= などの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査検査のなどを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査検査のなどを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、監査検査の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. K S,DEL= などの属性行を読まず監査検査のなどの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査検査のなどにおいて選択記号 C を採用し、識別名は監査検査です。監査検査のなどにおいて K S,DEL= など は説明欄の「z/OS MVS Operationsで K S,DEL= などの扱いを記録する監査検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査検査です。監査検査のなどを受け取る担当者は、K S,DEL= などの表示結果と IEE115I を同じ確認単位として扱い、背景名は監査検査です。不適切な選択肢を整理します。 A: 監査検査のなどは別カテゴリの確認を流用しており、K S,DEL= などの根拠にならないため監査検査ではありません。 B: 監査検査のなどは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査検査ではありません。 C: 監査検査のなどは対象出力と項目説明を結び、根拠を残すので監査検査です。 D: 監査検査のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため監査検査ではありません。監査検査のなどが示す K S,DEL= などは出典欄の資料で使い方を追跡できる項目であり、用語名は監査検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details></section>


<section class="kb-item" id="c22-i0195"><h3>K コマンド基本</h3><p class="kb-meta">分類: K ・ 難易度: 初級</p><p>K コマンド基本は、MVS オペレータコマンドのKで確認する項目です。CONTROL コマンドの 1 字省略形。コンソール属性の動的変更 (PFK、ROLL、RNUM、M REF 等) に用いる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧検査のコマンド基本で K コマンド基本の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. K コマンド基本の出力を取らず復旧検査のコマンド基本の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、復旧検査の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧検査のコマンド基本の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧検査のコマンド基本へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 復旧検査のコマンド基本において選択記号 B を採用し、識別名は復旧検査です。復旧検査のコマンド基本において K コマンド基本 は説明欄の「復旧検査のコマンド基本に関係する定義値と表示行を照合する復旧検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧検査です。復旧検査のコマンド基本の証跡を読む担当者は、K コマンド基本の属性行と IEE115I を合わせて追跡し、背景名は復旧検査です。誤答側の問題点を分けます。 A: 復旧検査のコマンド基本は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧検査ではありません。 B: 復旧検査のコマンド基本は対象出力と項目説明を結び、根拠を残すので復旧検査です。 C: 復旧検査のコマンド基本は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧検査ではありません。 D: 復旧検査のコマンド基本は別カテゴリの確認を流用しており、K コマンド基本の根拠にならないため復旧検査ではありません。復旧検査のコマンド基本に出る K コマンド基本は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>K コマンド基本</strong></p><p>検証目的: 範囲追跡のコマンド基本について、K コマンド基本は、MVS オペレータコマンドの K で確認する項目です。CONTROL コマンドの 1 字省略形。コンソール属性の動的変更 (PFK、ROLL、RNUM、Mに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030051の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲追跡のコマンド基本の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にK コマンド基本を指定し、OSKB030051の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND K コマンド基本
CASE OSKB030051
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM K コマンド基本
CASE OSKB030051
SOURCE z/OS MVS Operations
K コマンド基本とOSKB030051が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030051を同じ出力で読み、範囲追跡のコマンド基本の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030051
→ Enter を押す
［画面・出力］
IEE115I OSKB030051 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030051   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030051が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の K コマンド基本 と OSKB030051 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030051 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## LOG


<section class="kb-item" id="c22-i0196"><h3>LOG OPERLOG (LOG &#x27;text&#x27;)</h3><p class="kb-meta">分類: LOG ・ 難易度: 中級</p><p>LOG &#x27;text&#x27; で SYSLOG / OPERLOG に任意コメントを記録する。運用作業ログを残す目的で使用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索追跡の操作コマンドで LOG OPERLOG (LOG &#x27;text&#x27;)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. LOG OPERLOG (LOG &#x27;text&#x27;)の出力を取らず探索追跡の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索追跡の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索追跡の操作コマンドにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡の操作コマンドにおいて LOG OPERLOG (LOG &#x27;text&#x27;) は説明欄の「探索追跡の操作コマンドに関係する定義値と表示行を照合する探索追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の操作コマンドの証跡を読む担当者は、LOG OPERLOG (LOG &#x27;text&#x27;)の属性行と IEE115I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の操作コマンドは別カテゴリの確認を流用しており、LOG OPERLOG (LOG &#x27;text&#x27;)の根拠にならないため探索追跡ではありません。探索追跡の操作コマンドに出る LOG OPERLOG (LOG &#x27;text&#x27;)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LOG OPERLOG (LOG &#x27;text&#x27;)</strong></p><p>検証目的: 監査確認の操作コマンドについて、LOG &#x27;text&#x27; で SYSLOG / OPERLOG に任意コメントを記録する。運用作業ログを残す目的で使用に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030019の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査確認の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にLOG OPERLOG (LOG &#x27;を指定し、OSKB030019の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND LOG OPERLOG (LOG &#x27;
CASE OSKB030019
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM LOG OPERLOG (LOG &#x27;
CASE OSKB030019
SOURCE z/OS MVS Operations
LOG OPERLOG (LOG &#x27;とOSKB030019が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030019を同じ出力で読み、監査確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030019
→ Enter を押す
［画面・出力］
IEE115I OSKB030019 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030019   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030019が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の LOG OPERLOG (LOG &#x27; と OSKB030019 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030019 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0197"><h3>LOG コマンドの権限</h3><p class="kb-meta">分類: LOG ・ 難易度: 中級</p><p>発行コンソールの AUTH レベルに依存。LOG 自体はマスタ権限不要だが SYSLOG/OPERLOG の保護対象設定を確認すべき</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書追跡のコマンドの権限で操作コマンドの運用確認を行います。LOG コマンドの権限の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書追跡のコマンドの権限を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書追跡のコマンドの権限を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. LOG コマンドの権限の属性行を読まず上書追跡のコマンドの権限の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書追跡のコマンドの権限において選択記号 C を採用し、識別名は上書追跡です。上書追跡のコマンドの権限において LOG コマンドの権限 は説明欄の「z/OS MVS Operationsで LOG コマンドの権限の扱いを記録する上書追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のコマンドの権限を受け取る担当者は、LOG コマンドの権限の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のコマンドの権限は別カテゴリの確認を流用しており、LOG コマンドの権限の根拠にならないため上書追跡ではありません。 B: 上書追跡のコマンドの権限は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のコマンドの権限は対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のコマンドの権限は名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のコマンドの権限が示す LOG コマンドの権限は出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>LOG コマンドの権限</strong></p><p>検証目的: 終端追跡のコマンドの権限について、発行コンソールの AUTH レベルに依存。LOG 自体はマスタ権限不要だが SYSLOG/OPERLOG の保護対象設定を確認すべきに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040045の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端追跡のコマンドの権限の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にLOG コマンドの権限を指定し、OSKB040045の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND LOG コマンドの権限
CASE OSKB040045
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM LOG コマンドの権限
CASE OSKB040045
SOURCE z/OS MVS Operations
LOG コマンドの権限とOSKB040045が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040045を同じ出力で読み、終端追跡のコマンドの権限の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040045
→ Enter を押す
［画面・出力］
IEE115I OSKB040045 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040045   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040045が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の LOG コマンドの権限 と OSKB040045 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040045 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>LOG コマンドの権限</strong></p><p>検証目的: 変更確認のコマンドの権限について、発行コンソールの AUTH レベルに依存。LOG 自体はマスタ権限不要だが SYSLOG/OPERLOG の保護対象設定を確認すべきに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030020の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更確認のコマンドの権限の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にLOG コマンドの権限を指定し、OSKB030020の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND LOG コマンドの権限
CASE OSKB030020
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM LOG コマンドの権限
CASE OSKB030020
SOURCE z/OS MVS Operations
LOG コマンドの権限とOSKB030020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030020を同じ出力で読み、変更確認のコマンドの権限の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030020
→ Enter を押す
［画面・出力］
IEE115I OSKB030020 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030020   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の LOG コマンドの権限 と OSKB030020 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## MN


<section class="kb-item" id="c22-i0198"><h3>MN JOBNAMES</h3><p class="kb-meta">分類: MN ・ 難易度: 中級</p><p>MN JOBNAMESは、MVS オペレータコマンドのMNで確認する項目です。全ジョブの開始・終了時にメッセージを生成。ジョブ流れの自動化前提として活用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端判定の操作コマンドに関係する MN JOBNAMES の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端判定として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. MN JOBNAMES の名称と担当者名のみを残して終端判定の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端判定の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端判定の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端判定の操作コマンドにおいて選択記号 A を採用し、識別名は終端判定です。終端判定の操作コマンドにおいて MN JOBNAMES は説明欄の「MN JOBNAMES の用途を操作コマンドの表示で確認する終端判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端判定です。終端判定の操作コマンドに関連して、z/OS MVS Operationsでは MN JOBNAMES の表示属性と IEE115I を同じ証跡に残し、背景名は終端判定です。他の選択肢を確認します。 A: 終端判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端判定です。 B: 終端判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端判定ではありません。 C: 終端判定の操作コマンドは別カテゴリの確認を流用しており、MN JOBNAMES の根拠にならないため終端判定ではありません。 D: 終端判定の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端判定ではありません。終端判定の操作コマンドで使う MN JOBNAMES という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MN JOBNAMES</strong></p><p>検証目的: 復旧追跡の操作コマンドについて、MN JOBNAMES は、MVS オペレータコマンドの MN で確認する項目です。全ジョブの開始・終了時にメッセージを生成。ジョブ流れの自動化前提として活用に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030058の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にMN JOBNAMESを指定し、OSKB030058の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND MN JOBNAMES
CASE OSKB030058
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM MN JOBNAMES
CASE OSKB030058
SOURCE z/OS MVS Operations
MN JOBNAMESとOSKB030058が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030058を同じ出力で読み、復旧追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030058
→ Enter を押す
［画面・出力］
IEE115I OSKB030058 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030058   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030058が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の MN JOBNAMES と OSKB030058 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030058 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0199"><h3>MN SESS</h3><p class="kb-meta">分類: MN ・ 難易度: 中級</p><p>MN SESSは、MVS オペレータコマンドのMNで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書判定の操作コマンドで操作コマンドの運用確認を行います。MN SESS の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書判定の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書判定の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書判定の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. MN SESS の属性行を読まず上書判定の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書判定の操作コマンドにおいて選択記号 C を採用し、識別名は上書判定です。上書判定の操作コマンドにおいて MN SESS は説明欄の「z/OS MVS Operationsで MN SESS の扱いを記録する上書判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書判定です。上書判定の操作コマンドを受け取る担当者は、MN SESS の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書判定です。不適切な選択肢を整理します。 A: 上書判定の操作コマンドは別カテゴリの確認を流用しており、MN SESS の根拠にならないため上書判定ではありません。 B: 上書判定の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書判定ではありません。 C: 上書判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので上書判定です。 D: 上書判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書判定ではありません。上書判定の操作コマンドが示す MN SESS は出典欄の資料で使い方を追跡できる項目であり、用語名は上書判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MN SESS</strong></p><p>検証目的: 変更追跡の操作コマンドについて、MN SESS は、MVS オペレータコマンドの MN で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OSに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030060の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にMN SESSを指定し、OSKB030060の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND MN SESS
CASE OSKB030060
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM MN SESS
CASE OSKB030060
SOURCE z/OS MVS Operations
MN SESSとOSKB030060が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030060を同じ出力で読み、変更追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030060
→ Enter を押す
［画面・出力］
IEE115I OSKB030060 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030060   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030060が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の MN SESS と OSKB030060 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030060 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0200"><h3>MN STATUS</h3><p class="kb-meta">分類: MN ・ 難易度: 中級</p><p>MN STATUSは、MVS オペレータコマンドのMNで確認する項目です。DD 文割当のたびに DSN を SYSLOG に記録する形式。データセット流出調査などで一時的に有効化</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索判定の操作コマンドで MN STATUS の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. MN STATUS の出力を取らず探索判定の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索判定の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索判定の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索判定の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索判定の操作コマンドにおいて選択記号 B を採用し、識別名は探索判定です。探索判定の操作コマンドにおいて MN STATUS は説明欄の「探索判定の操作コマンドに関係する定義値と表示行を照合する探索判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索判定です。探索判定の操作コマンドの証跡を読む担当者は、MN STATUS の属性行と IEE115I を合わせて追跡し、背景名は探索判定です。誤答側の問題点を分けます。 A: 探索判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索判定ではありません。 B: 探索判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索判定です。 C: 探索判定の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索判定ではありません。 D: 探索判定の操作コマンドは別カテゴリの確認を流用しており、MN STATUS の根拠にならないため探索判定ではありません。探索判定の操作コマンドに出る MN STATUS は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MN STATUS</strong></p><p>検証目的: 監査追跡の操作コマンドについて、MN STATUS は、MVS オペレータコマンドの MN で確認する項目です。DD 文割当のたびに DSN を SYSLOG に記録する形式。データセット流出調査などで一時的にに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030059の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にMN STATUSを指定し、OSKB030059の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND MN STATUS
CASE OSKB030059
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM MN STATUS
CASE OSKB030059
SOURCE z/OS MVS Operations
MN STATUSとOSKB030059が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030059を同じ出力で読み、監査追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030059
→ Enter を押す
［画面・出力］
IEE115I OSKB030059 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030059   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030059が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の MN STATUS と OSKB030059 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030059 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0201"><h3>MONITOR コマンド (MN)</h3><p class="kb-meta">分類: MN ・ 難易度: 中級</p><p>MN コマンドは TSU LOGON/LOGOFF、JOB 開始/終了、データセット名表示などの監視メッセージ生成を切替える</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換判定のコマンドに関する MONITOR コマンド (MN)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換判定のコマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換判定のコマンドの証跡として保存して根拠にする。</li><li>C. MONITOR コマンド (MN)の変更点を出力本文から切り離して置換判定のコマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換判定の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換判定のコマンドにおいて選択記号 D を採用し、識別名は置換判定です。置換判定のコマンドにおいて MONITOR コマンド (MN) は説明欄の「MONITOR コマンド (MN)の状態と出力メッセージを結び付ける置換判定項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換判定です。置換判定のコマンドに関する記録は、MONITOR コマンド (MN)の出力行と IEE115I を一緒に保存し、背景名は置換判定です。選択肢ごとの違いを示します。 A: 置換判定のコマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換判定ではありません。 B: 置換判定のコマンドは別カテゴリの確認を流用しており、MONITOR コマンド (MN)の根拠にならないため置換判定ではありません。 C: 置換判定のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換判定ではありません。 D: 置換判定のコマンドは対象出力と項目説明を結び、根拠を残すので置換判定です。置換判定のコマンドで記録する MONITOR コマンド (MN)はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MONITOR コマンド (MN)</strong></p><p>検証目的: 警告追跡のコマンドについて、MN コマンドは TSU LOGON/LOGOFF、JOB 開始/終了、データセット名表示などの監視メッセージ生成を切替えるに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030057の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告追跡のコマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にMONITOR コマンド (MN)を指定し、OSKB030057の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND MONITOR コマンド (MN)
CASE OSKB030057
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM MONITOR コマンド (MN)
CASE OSKB030057
SOURCE z/OS MVS Operations
MONITOR コマンド (MN)とOSKB030057が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030057を同じ出力で読み、警告追跡のコマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030057
→ Enter を押す
［画面・出力］
IEE115I OSKB030057 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030057   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030057が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の MONITOR コマンド (MN) と OSKB030057 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030057 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## P


<section class="kb-item" id="c22-i0202"><h3>P コマンド基本構文</h3><p class="kb-meta">分類: P ・ 難易度: 初級</p><p>P コマンド基本構文は、MVS オペレータコマンドのPで状態表示や操作を行うためのコマンド関連項目です。P jobname または P identifier で STC を停止する。実体はサブシステムへの STOP 要求でサブシステム側がクリーンアップを行う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録検分のコマンド基本構文に関係する P コマンド基本構文の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、記録検分として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. P コマンド基本構文の名称と担当者名だけを残して記録検分のコマンド基本構文の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録検分のコマンド基本構文を確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず記録検分のコマンド基本構文の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では P コマンド基本構文 は「P コマンド基本構文の用途を操作コマンドの表示で確認する記録検分項目」と D OPDATA または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景ではz/OS MVS Operationsの P コマンド基本構文と IEE457I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明だけに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では P コマンド基本構文を MVS オペレータコマンドで扱う確認対象とし、用語名は記録検分用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>P コマンド基本構文</strong></p><p>検証目的: 記録照合のコマンド基本構文について、P コマンド基本構文は、MVS オペレータコマンドの P で状態表示や操作を行うためのコマンド関連項目です。P jobname または P identifier で STC をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040033の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、記録照合のコマンド基本構文の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にP コマンド基本構文を指定し、OSKB040033の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND P コマンド基本構文
CASE OSKB040033
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM P コマンド基本構文
CASE OSKB040033
SOURCE z/OS MVS Operations
P コマンド基本構文とOSKB040033が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040033を同じ出力で読み、記録照合のコマンド基本構文の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB040033
→ Enter を押す
［画面・出力］
IEE457I OSKB040033 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040033   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB040033が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の P コマンド基本構文 と OSKB040033 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB040033 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>P コマンド基本構文</strong></p><p>検証目的: 出力検査のコマンド基本構文について、P コマンド基本構文は、MVS オペレータコマンドの P で状態表示や操作を行うためのコマンド関連項目です。P jobname または P identifier で STC をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020068の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、出力検査のコマンド基本構文の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にP コマンド基本構文を指定し、OSKB020068の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND P コマンド基本構文
CASE OSKB020068
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM P コマンド基本構文
CASE OSKB020068
SOURCE z/OS MVS Operations
P コマンド基本構文とOSKB020068が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020068を同じ出力で読み、出力検査のコマンド基本構文の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020068
→ Enter を押す
［画面・出力］
IEE457I OSKB020068 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020068   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020068が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の P コマンド基本構文 と OSKB020068 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020068 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## P APPC


<section class="kb-item" id="c22-i0203"><h3>P APPC APPC/MVS 停止</h3><p class="kb-meta">分類: P APPC ・ 難易度: 中級</p><p>P APPC APPC/MVS 停止は、MVS オペレータコマンドのP APPCで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査検分の・ 停止で操作コマンドの運用確認を行います。P APPC APPC 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査検分の・ 停止を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査検分の・ 停止を正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を監査検分で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. P APPC APPC 属性の属性行を読まず監査検分の・ 停止の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では P APPC APPC 属性 は「z/OS MVS Operationsで P APPC APPC 属性の扱いを記録する監査検分項目」と D A,L または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では P APPC APPC 属性の表示結果と IEE115I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明だけに寄り、判定名は監査検分不足です。監査検分資料では P APPC APPC 属性の使い方を出典欄から追跡し、資料名は監査検分資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>P APPC APPC ・ MVS 停止</strong></p><p>検証目的: 比較照合の・ 停止について、P APPC APPC/MVS 停止は、MVS オペレータコマンドの P APPC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040034の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較照合の・ 停止の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にP APPC APPC ・ MVS を指定し、OSKB040034の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND P APPC APPC ・ MVS 
CASE OSKB040034
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM P APPC APPC ・ MVS 
CASE OSKB040034
SOURCE z/OS MVS Operations
P APPC APPC ・ MVS とOSKB040034が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040034を同じ出力で読み、比較照合の・ 停止の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040034
→ Enter を押す
［画面・出力］
IEE115I OSKB040034 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040034   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040034が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の P APPC APPC ・ MVS  と OSKB040034 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040034 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>P APPC APPC ・ MVS 停止</strong></p><p>検証目的: 比較検査の・ 停止について、P APPC APPC/MVS 停止は、MVS オペレータコマンドの P APPC で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020074の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較検査の・ 停止の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にP APPC APPC ・ MVS を指定し、OSKB020074の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND P APPC APPC ・ MVS 
CASE OSKB020074
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM P APPC APPC ・ MVS 
CASE OSKB020074
SOURCE z/OS MVS Operations
P APPC APPC ・ MVS とOSKB020074が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020074を同じ出力で読み、比較検査の・ 停止の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020074
→ Enter を押す
［画面・出力］
IEE115I OSKB020074 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020074   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020074が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の P APPC APPC ・ MVS  と OSKB020074 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020074 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## P CICS


<section class="kb-item" id="c22-i0204"><h3>P CICS リージョン停止</h3><p class="kb-meta">分類: P CICS ・ 難易度: 上級</p><p>P CICS リージョン停止は、MVS オペレータコマンドのP CICSで用いるCICS リージョンを停止する。実体は CEMT 経由 PERFORM SHUTDOWN を呼び出す内部処理。P CICSでは、指定値と対象資源、実行時の出力を突き合わせて確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域検分のリージョン停止に関する P CICS リージョン停止の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域検分のリージョン停止の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域検分のリージョン停止の証跡として保存して根拠にする。</li><li>C. P CICS リージョン停止の変更点を出力本文から切り離して値域検分のリージョン停止の承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、値域検分で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では P CICS リージョン停止 は「P CICS リージョン停止の状態と出力メッセージを結び付ける値域検分項目」と D A,L または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では P CICS リージョン停止の出力行と IEE115I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明だけに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では P CICS リージョン停止をz/OS MVS Operationsの確認記録に残し、対象名は値域検分対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>P CICS リージョン停止</strong></p><p>検証目的: 範囲検査のリージョン停止について、P CICS リージョン停止は、MVS オペレータコマンドの P CICS で用いる CICS リージョンを停止する。実体は CEMT 経由 PERFORM SHUTDOWN をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020071の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲検査のリージョン停止の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にP CICS リージョン停止を指定し、OSKB020071の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND P CICS リージョン停止
CASE OSKB020071
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM P CICS リージョン停止
CASE OSKB020071
SOURCE z/OS MVS Operations
P CICS リージョン停止とOSKB020071が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020071を同じ出力で読み、範囲検査のリージョン停止の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020071
→ Enter を押す
［画面・出力］
IEE115I OSKB020071 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020071   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020071が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の P CICS リージョン停止 と OSKB020071 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020071 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## P JES2


<section class="kb-item" id="c22-i0205"><h3>P JES2 停止</h3><p class="kb-meta">分類: P JES2 ・ 難易度: 中級</p><p>P JES2 停止は、MVS オペレータコマンドのP JES2で用いるJES2 サブシステムを停止する。スプール上の活性ジョブが残ると拒否されるため $P JES2 等で先に流す。P JES2では、指定値と対象資源、実行時の出力を突き合わせて確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較検分の停止で P JES2 停止の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. P JES2 停止の出力を取らず比較検分の停止の説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、比較検分の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較検分の停止の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較検分の停止へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では P JES2 停止 は「比較検分の停止に関係する定義値と表示行を照合する比較検分項目」と D A,L または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では P JES2 停止の属性行と IEE115I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明だけに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では P JES2 停止を MVS オペレータコマンドの運用手順で確認し、初出名は比較検分初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>P JES2 停止</strong></p><p>検証目的: 条件検査の停止について、P JES2 停止は、MVS オペレータコマンドの P JES2 で用いる JES2 サブシステムを停止する。スプール上の活性ジョブが残ると拒否されるため $P JES2 等で先に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020069の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件検査の停止の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にP JES2 停止を指定し、OSKB020069の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND P JES2 停止
CASE OSKB020069
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM P JES2 停止
CASE OSKB020069
SOURCE z/OS MVS Operations
P JES2 停止とOSKB020069が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020069を同じ出力で読み、条件検査の停止の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020069
→ Enter を押す
［画面・出力］
IEE115I OSKB020069 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020069   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020069が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の P JES2 停止 と OSKB020069 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020069 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## P LLA


<section class="kb-item" id="c22-i0206"><h3>P LLA 停止</h3><p class="kb-meta">分類: P LLA ・ 難易度: 中級</p><p>LLA を停止する。LNKLST ロード時に LLA 経由のメモリ・コピーが使われなくなる影響を理解した上で実施</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更検分の停止に関する P LLA 停止の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更検分の停止の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更検分の停止の証跡として保存して根拠にする。</li><li>C. P LLA 停止の変更点を出力本文から切り離して変更検分の停止の承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、変更検分の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では P LLA 停止 は「P LLA 停止の状態と出力メッセージを結び付ける変更検分項目」と D A,L または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では P LLA 停止の出力行と IEE115I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明だけに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では P LLA 停止をz/OS MVS Operationsの確認記録に残し、対象名は変更検分対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>P LLA 停止</strong></p><p>検証目的: 順序検査の停止について、LLA を停止する。LNKLST ロード時に LLA 経由のメモリ・コピーが使われなくなる影響を理解した上で実施に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020075の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序検査の停止の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にP LLA 停止を指定し、OSKB020075の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND P LLA 停止
CASE OSKB020075
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM P LLA 停止
CASE OSKB020075
SOURCE z/OS MVS Operations
P LLA 停止とOSKB020075が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020075を同じ出力で読み、順序検査の停止の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020075
→ Enter を押す
［画面・出力］
IEE115I OSKB020075 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020075   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020075が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の P LLA 停止 と OSKB020075 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020075 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## P NET


<section class="kb-item" id="c22-i0207"><h3>P NET VTAM 停止</h3><p class="kb-meta">分類: P NET ・ 難易度: 上級</p><p>P NET VTAM 停止は、MVS オペレータコマンドのP NETで確認する項目です。VTAM を停止する。Z NET,QUICK と異なり、未完セッションのクリーンアップを待つ標準停止</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序検分の停止で操作コマンドの運用確認を行います。P NET VTAM 停止の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序検分の停止を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序検分の停止を正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、順序検分の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. P NET VTAM 停止の属性行を読まず順序検分の停止の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では P NET VTAM 停止 は「z/OS MVS Operationsで P NET VTAM 停止の扱いを記録する順序検分項目」と D A,L または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では P NET VTAM 停止の表示結果と IEE115I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明だけに寄り、判定名は順序検分不足です。順序検分資料では P NET VTAM 停止の使い方を出典欄から追跡し、資料名は順序検分資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>P NET VTAM 停止</strong></p><p>検証目的: 区切検査の停止について、P NET VTAM 停止は、MVS オペレータコマンドの P NET で確認する項目です。VTAM を停止する。Z NET,QUICK と異なり、未完セッションのクリーンアッに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020070の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切検査の停止の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にP NET VTAM 停止を指定し、OSKB020070の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND P NET VTAM 停止
CASE OSKB020070
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM P NET VTAM 停止
CASE OSKB020070
SOURCE z/OS MVS Operations
P NET VTAM 停止とOSKB020070が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020070を同じ出力で読み、区切検査の停止の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020070
→ Enter を押す
［画面・出力］
IEE115I OSKB020070 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020070   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020070が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の P NET VTAM 停止 と OSKB020070 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020070 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## P SCH


<section class="kb-item" id="c22-i0208"><h3>P ASCH スケジューラ停止</h3><p class="kb-meta">分類: P SCH ・ 難易度: 中級</p><p>P ASCH スケジューラ停止は、MVS オペレータコマンドのP SCHで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文確認再のスケジューラ停止に関係する P ASCH スケジューラ停止の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、構文確認再の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. P ASCH スケジューラ停止の名称と担当者名だけを残して構文確認再のスケジューラ停止の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文確認再のスケジューラ停止を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文確認再のスケジューラ停止の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文確認再正解では選択記号 A を採用し、正解名は構文確認再正解です。構文確認再根拠では P ASCH スケジューラ停止 は「P ASCH スケジューラ停止の用途を操作コマンドの表示で確認する構文確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は構文確認再根拠です。構文確認再背景ではz/OS MVS Operationsの P ASCH スケジューラ停止と IEE115I を同じ証跡に残し、背景名は構文確認再背景です。他の選択肢を確認します。 A: 構文確認再正答は対象出力と項目説明を結び、根拠名は構文確認再正答です。 B: 構文確認再不足は名称や説明だけに寄り、判定名は構文確認再不足です。 C: 構文確認再流用は別カテゴリの確認であり、排除名は構文確認再流用です。 D: 構文確認再欠落は戻り値や記録番号に寄り、欠落名は構文確認再欠落です。構文確認再用語では P ASCH スケジューラ停止を MVS オペレータコマンドで扱う確認対象とし、用語名は構文確認再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>P ASCH スケジューラ停止</strong></p><p>検証目的: 値域検査のスケジューラ停止について、P ASCH スケジューラ停止は、MVS オペレータコマンドの P SCH で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けてに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020076の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域検査のスケジューラ停止の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にP ASCH スケジューラ停止を指定し、OSKB020076の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND P ASCH スケジューラ停止
CASE OSKB020076
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM P ASCH スケジューラ停止
CASE OSKB020076
SOURCE z/OS MVS Operations
P ASCH スケジューラ停止とOSKB020076が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020076を同じ出力で読み、値域検査のスケジューラ停止の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020076
→ Enter を押す
［画面・出力］
IEE115I OSKB020076 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020076   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020076が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の P ASCH スケジューラ停止 と OSKB020076 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020076 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## P TRACE


<section class="kb-item" id="c22-i0209"><h3>P TRACE = TRACE CT,OFF</h3><p class="kb-meta">分類: P TRACE ・ 難易度: 上級</p><p>コンポーネント・トレースを停止する場合は TRACE CT,OFF,COMP=name を使う (P TRACE は使わない)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧検分の操作コマンドで P 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. P 属性の出力を取らず復旧検分の操作コマンドの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて復旧検分の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧検分の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧検分の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では P 属性 は「復旧検分の操作コマンドに関係する定義値と表示行を照合する復旧検分項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では P 属性の属性行と IEE115I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明だけに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では P 属性を MVS オペレータコマンドの運用手順で確認し、初出名は復旧検分初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>P TRACE = TRACE CT,OFF</strong></p><p>検証目的: 記録検査の操作コマンドについて、コンポーネント・トレースを停止する場合は TRACE CT,OFF,COMP=name を使う (P TRACE は使わない)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020073の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にP TRACE = TRACE CTを指定し、OSKB020073の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND P TRACE = TRACE CT
CASE OSKB020073
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM P TRACE = TRACE CT
CASE OSKB020073
SOURCE z/OS MVS Operations
P TRACE = TRACE CTとOSKB020073が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020073を同じ出力で読み、記録検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020073
→ Enter を押す
［画面・出力］
IEE115I OSKB020073 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020073   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020073が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の P TRACE = TRACE CT と OSKB020073 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020073 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## P TSO


<section class="kb-item" id="c22-i0210"><h3>P TSO サブシステム停止</h3><p class="kb-meta">分類: P TSO ・ 難易度: 中級</p><p>P TSO サブシステム停止は、MVS オペレータコマンドのP TSOで確認する項目です。TSO/E サブシステムを停止し、新規 LOGON を拒否する。既存ユーザに事前通知が必要</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告検分のサブシステム停止に関係する P TSO サブシステム停止の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、警告検分の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. P TSO サブシステム停止の名称と担当者名だけを残して警告検分のサブシステム停止の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告検分のサブシステム停止を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告検分のサブシステム停止の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では P TSO サブシステム停止 は「P TSO サブシステム停止の用途を操作コマンドの表示で確認する警告検分項目」と D A,L または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景ではz/OS MVS Operationsの P TSO サブシステム停止と IEE115I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明だけに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では P TSO サブシステム停止を MVS オペレータコマンドで扱う確認対象とし、用語名は警告検分用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>P TSO サブシステム停止</strong></p><p>検証目的: 優先検査のサブシステム停止について、P TSO サブシステム停止は、MVS オペレータコマンドの P TSO で確認する項目です。TSO/E サブシステムを停止し、新規 LOGON を拒否する。既存ユーザに事前通に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020072の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先検査のサブシステム停止の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にP TSO サブシステム停止を指定し、OSKB020072の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND P TSO サブシステム停止
CASE OSKB020072
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM P TSO サブシステム停止
CASE OSKB020072
SOURCE z/OS MVS Operations
P TSO サブシステム停止とOSKB020072が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020072を同じ出力で読み、優先検査のサブシステム停止の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020072
→ Enter を押す
［画面・出力］
IEE115I OSKB020072 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020072   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020072が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の P TSO サブシステム停止 と OSKB020072 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020072 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## R


<section class="kb-item" id="c22-i0211"><h3>R nn,CANCEL (DUMP)</h3><p class="kb-meta">分類: R ・ 難易度: 中級</p><p>R nn,CANCEL (DUMP)は、MVS オペレータコマンドのRで状態表示や操作を行うためのコマンド関連項目です。R nn,CANCEL (DUMP)は、WTOR を出している側のジョブの規約により CANCEL や DUMP を指示できる典型応答 (例: IEA911E ダンプ続行)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力照合再の操作コマンドに関する R nn 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力照合再の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力照合再の操作コマンドの証跡として保存して根拠にする。</li><li>C. R nn 命令の変更点を出力本文から切り離して出力照合再の操作コマンドの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、出力照合再の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力照合再正解では選択記号 D を採用し、正解名は出力照合再正解です。出力照合再根拠では R nn 命令 は「R nn 命令の状態と出力メッセージを結び付ける出力照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は出力照合再根拠です。出力照合再保存では R nn 命令の出力行と IEE115I を一緒に残し、保存名は出力照合再保存です。選択肢ごとの違いを示します。 A: 出力照合再欠落は戻り値や記録番号に寄り、欠落名は出力照合再欠落です。 B: 出力照合再流用は別カテゴリの確認であり、排除名は出力照合再流用です。 C: 出力照合再不足は名称や説明だけに寄り、判定名は出力照合再不足です。 D: 出力照合再正答は対象出力と項目説明を結び、根拠名は出力照合再正答です。出力照合再対象では R nn 命令をz/OS MVS Operationsの確認記録に残し、対象名は出力照合再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切確認の操作コマンドで R nn,CANCEL (DUMP)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. R nn,CANCEL (DUMP)の出力を取らず区切確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切確認の操作コマンドにおいて選択記号 B を採用し、識別名は区切確認です。区切確認の操作コマンドにおいて R nn,CANCEL (DUMP) は説明欄の「区切確認の操作コマンドに関係する定義値と表示行を照合する区切確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認の操作コマンドの証跡を読む担当者は、R nn,CANCEL (DUMP)の属性行と IEE115I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切確認ではありません。 D: 区切確認の操作コマンドは別カテゴリの確認を流用しており、R nn,CANCEL (DUMP)の根拠にならないため区切確認ではありません。区切確認の操作コマンドに出る R nn,CANCEL (DUMP)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>R nn,CANCEL (DUMP)</strong></p><p>検証目的: 呼出整理の操作コマンドについて、R nn,CANCEL (DUMP)は、MVS オペレータコマンドの R で状態表示や操作を行うためのコマンド関連項目です。R nn,CANCEL (DUMP)は、WTOR をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020103の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出整理の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にR nn,CANCEL (DUMP)を指定し、OSKB020103の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND R nn,CANCEL (DUMP)
CASE OSKB020103
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM R nn,CANCEL (DUMP)
CASE OSKB020103
SOURCE z/OS MVS Operations
R nn,CANCEL (DUMP)とOSKB020103が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020103を同じ出力で読み、呼出整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020103
→ Enter を押す
［画面・出力］
IEE115I OSKB020103 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020103   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020103が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の R nn,CANCEL (DUMP) と OSKB020103 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020103 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0212"><h3>R nn,U / R nn,&#x27;U&#x27; (Continue)</h3><p class="kb-meta">分類: R ・ 難易度: 中級</p><p>R nn,U / R nn,&#x27;U&#x27; (Continue)は、MVS オペレータコマンドのRで確認する項目です。U や RETRY などの 1 文字応答が多い。アクション・メッセージの規約に従う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件照合再の・に関係する R nn,U 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、条件照合再として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. R nn,U 属性の名称と担当者名だけを残して条件照合再の・の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件照合再の・を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件照合再の・の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件照合再正解では選択記号 A を採用し、正解名は条件照合再正解です。条件照合再根拠では R nn,U 属性 は「R nn,U 属性の用途を操作コマンドの表示で確認する条件照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は条件照合再根拠です。条件照合再背景ではz/OS MVS Operationsの R nn,U 属性と IEE115I を同じ証跡に残し、背景名は条件照合再背景です。他の選択肢を確認します。 A: 条件照合再正答は対象出力と項目説明を結び、根拠名は条件照合再正答です。 B: 条件照合再不足は名称や説明だけに寄り、判定名は条件照合再不足です。 C: 条件照合再流用は別カテゴリの確認であり、排除名は条件照合再流用です。 D: 条件照合再欠落は戻り値や記録番号に寄り、欠落名は条件照合再欠落です。条件照合再用語では R nn,U 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は条件照合再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文照合保守の構文照合として R nn,U / R nn,&#x27;U&#x27; (Continue) を確認するとき、後続担当者へ残すべき証跡はどれですか。</p><ul class="kb-choices"><li>A. 名称と担当者名を保存して表示本文を確認しない。</li><li>B. 別分類の結果を流用して同じ証跡として扱う。</li><li>C. 構文照合の確認結果を出典名と表示本文に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>D. 戻り値と時刻を主な根拠にして表示行を読まない。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 正解はCです。構文照合保守で扱う R nn,U / R nn,&#x27;U&#x27; (Continue) は MVS オペレータコマンド の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として R nn,U / R nn,&#x27;U&#x27; (Continue) を扱い、分類内の確認名として保存します（構文照合保守終点）。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>R nn,U ・ R nn,&#x27;U&#x27; (Continue)</strong></p><p>検証目的: 監査照合の・について、R nn,U / R nn,&#x27;U&#x27; (Continue)は、MVS オペレータコマンドの R で確認する項目です。U や RETRY などの 1 文字応答が多い。アクション・メに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040039の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査照合の・の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にR nn,U ・ R nn,&#x27;U&#x27; を指定し、OSKB040039の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND R nn,U ・ R nn,&#x27;U&#x27; 
CASE OSKB040039
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM R nn,U ・ R nn,&#x27;U&#x27; 
CASE OSKB040039
SOURCE z/OS MVS Operations
R nn,U ・ R nn,&#x27;U&#x27; とOSKB040039が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040039を同じ出力で読み、監査照合の・の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040039
→ Enter を押す
［画面・出力］
IEE115I OSKB040039 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040039   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040039が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の R nn,U ・ R nn,&#x27;U&#x27;  と OSKB040039 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040039 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>R nn,U ・ R nn,&#x27;U&#x27; (Continue)</strong></p><p>検証目的: 置換整理の・について、R nn,U / R nn,&#x27;U&#x27; (Continue)は、MVS オペレータコマンドの R で確認する項目です。U や RETRY などの 1 文字応答が多い。アクション・メに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020104の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換整理の・の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にR nn,U ・ R nn,&#x27;U&#x27; を指定し、OSKB020104の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND R nn,U ・ R nn,&#x27;U&#x27; 
CASE OSKB020104
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM R nn,U ・ R nn,&#x27;U&#x27; 
CASE OSKB020104
SOURCE z/OS MVS Operations
R nn,U ・ R nn,&#x27;U&#x27; とOSKB020104が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020104を同じ出力で読み、置換整理の・の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020104
→ Enter を押す
［画面・出力］
IEE115I OSKB020104 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020104   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020104が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の R nn,U ・ R nn,&#x27;U&#x27;  と OSKB020104 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020104 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0213"><h3>R 基本構文 R nn,&#x27;text&#x27;</h3><p class="kb-meta">分類: R ・ 難易度: 初級</p><p>R 基本構文 R nn,&#x27;text&#x27;は、MVS オペレータコマンドのRで確認する項目です。未応答 WTOR (D R,L で取れた応答番号 nn) に対しテキスト応答を返す。MVS オペレーションの基本動作</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端照合再の基本構文に関係する R 基本構文 R nn 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、終端照合再の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. R 基本構文 R nn 命令の名称と担当者名だけを残して終端照合再の基本構文の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端照合再の基本構文を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端照合再の基本構文の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 終端照合再正解では選択記号 A を採用し、正解名は終端照合再正解です。終端照合再根拠では R 基本構文 R nn 命令 は「R 基本構文 R nn 命令の用途を操作コマンドの表示で確認する終端照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は終端照合再根拠です。終端照合再背景ではz/OS MVS Operationsの R 基本構文 R nn 命令と IEE115I を同じ証跡に残し、背景名は終端照合再背景です。他の選択肢を確認します。 A: 終端照合再正答は対象出力と項目説明を結び、根拠名は終端照合再正答です。 B: 終端照合再不足は名称や説明だけに寄り、判定名は終端照合再不足です。 C: 終端照合再流用は別カテゴリの確認であり、排除名は終端照合再流用です。 D: 終端照合再欠落は戻り値や記録番号に寄り、欠落名は終端照合再欠落です。終端照合再用語では R 基本構文 R nn 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は終端照合再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書確認の基本構文で操作コマンドの運用確認を行います。R 基本構文 R nn,&#x27;text&#x27;の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書確認の基本構文を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書確認の基本構文を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. R 基本構文 R nn,&#x27;text&#x27;の属性行を読まず上書確認の基本構文の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 上書確認の基本構文において選択記号 C を採用し、識別名は上書確認です。上書確認の基本構文において R 基本構文 R nn,&#x27;text&#x27; は説明欄の「z/OS MVS Operationsで R 基本構文 R nn,&#x27;text&#x27;の扱いを記録する上書確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認の基本構文を受け取る担当者は、R 基本構文 R nn,&#x27;text&#x27;の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認の基本構文は別カテゴリの確認を流用しており、R 基本構文 R nn,&#x27;text&#x27;の根拠にならないため上書確認ではありません。 B: 上書確認の基本構文は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書確認ではありません。 C: 上書確認の基本構文は対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認の基本構文は名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認の基本構文が示す R 基本構文 R nn,&#x27;text&#x27;は出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>R 基本構文 R nn,&#x27;text&#x27;</strong></p><p>検証目的: 変更判定の基本構文について、R 基本構文 R nn,&#x27;text&#x27;は、MVS オペレータコマンドの R で確認する項目です。未応答 WTOR (D R,L で取れた応答番号 nn) に対しテキスト応答を返すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020100の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更判定の基本構文の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にR 基本構文 R nn,&#x27;text&#x27;を指定し、OSKB020100の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND R 基本構文 R nn,&#x27;text&#x27;
CASE OSKB020100
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM R 基本構文 R nn,&#x27;text&#x27;
CASE OSKB020100
SOURCE z/OS MVS Operations
R 基本構文 R nn,&#x27;text&#x27;とOSKB020100が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020100を同じ出力で読み、変更判定の基本構文の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020100
→ Enter を押す
［画面・出力］
IEE115I OSKB020100 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020100   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020100が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の R 基本構文 R nn,&#x27;text&#x27; と OSKB020100 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020100 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0214"><h3>応答テキストの引用符</h3><p class="kb-meta">分類: R ・ 難易度: 中級</p><p>応答テキストの引用符は、MVS オペレータコマンドのRで確認する項目です。空白・カンマ等を含む応答は単一引用符で囲む。引用符内の引用符は二重指定でエスケープ</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書照合再の応答テキストの引用符で操作コマンドの運用確認を行います。応答テキストの引用符の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書照合再の応答テキストの引用符を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書照合再の応答テキストの引用符を正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、上書照合再の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. 応答テキストの引用符の属性行を読まず上書照合再の応答テキストの引用符の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書照合再正解では選択記号 C を採用し、正解名は上書照合再正解です。上書照合再根拠では応答テキストの引用符は「z/OS MVS Operationsで応答テキストの引用符の扱いを記録する上書照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は上書照合再根拠です。上書照合再受渡では応答テキストの引用符の表示結果と IEE115I を同じ確認単位にし、受渡名は上書照合再受渡です。不適切な選択肢を整理します。 A: 上書照合再流用は別カテゴリの確認であり、排除名は上書照合再流用です。 B: 上書照合再欠落は戻り値や記録番号に寄り、欠落名は上書照合再欠落です。 C: 上書照合再正答は対象出力と項目説明を結び、根拠名は上書照合再正答です。 D: 上書照合再不足は名称や説明だけに寄り、判定名は上書照合再不足です。上書照合再資料では応答テキストの引用符の使い方を出典欄から追跡し、資料名は上書照合再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件確認の応答テキストの引用符に関係する応答テキストの引用符の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. 応答テキストの引用符の名称と担当者名のみを残して条件確認の応答テキストの引用符の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件確認の応答テキストの引用符を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件確認の応答テキストの引用符の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件確認の応答テキストの引用符において選択記号 A を採用し、識別名は条件確認です。条件確認の応答テキストの引用符において応答テキストの引用符は説明欄の「応答テキストの引用符の用途を操作コマンドの表示で確認する条件確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認の応答テキストの引用符に関連して、z/OS MVS Operationsでは応答テキストの引用符の表示属性と IEE115I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認の応答テキストの引用符は対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認の応答テキストの引用符は名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認の応答テキストの引用符は別カテゴリの確認を流用しており、応答テキストの引用符の根拠にならないため条件確認ではありません。 D: 条件確認の応答テキストの引用符は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件確認ではありません。条件確認の応答テキストの引用符で使う応答テキストの引用符という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>応答テキストの引用符</strong></p><p>検証目的: 展開整理の応答テキストの引用符について、応答テキストの引用符は、MVS オペレータコマンドの R で確認する項目です。空白・カンマ等を含む応答は単一引用符で囲む。引用符内の引用符は二重指定でエスケープに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020102の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開整理の応答テキストの引用符の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に応答テキストの引用符を指定し、OSKB020102の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND 応答テキストの引用符
CASE OSKB020102
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM 応答テキストの引用符
CASE OSKB020102
SOURCE z/OS MVS Operations
応答テキストの引用符とOSKB020102が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020102を同じ出力で読み、展開整理の応答テキストの引用符の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020102
→ Enter を押す
［画面・出力］
IEE115I OSKB020102 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020102   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020102が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の 応答テキストの引用符 と OSKB020102 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020102 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0215"><h3>応答番号 nn の形式</h3><p class="kb-meta">分類: R ・ 難易度: 中級</p><p>応答番号 nn の形式は、MVS オペレータコマンドのRで確認する項目です。nn は 00〜99 (1, 2 桁) を表示時の番号で指定する。番号は WTOR 単位に動的割当てされ、応答後は再利用される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索照合再の応答番号 の形式で応答番号 nn の形式の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. 応答番号 nn の形式の出力を取らず探索照合再の応答番号 の形式の説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて探索照合再の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索照合再の応答番号 の形式の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索照合再の応答番号 の形式へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索照合再正解では選択記号 B を採用し、正解名は探索照合再正解です。探索照合再根拠では応答番号 nn の形式 は「探索照合再の応答番号 の形式に関係する定義値と表示行を照合する探索照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は探索照合再根拠です。探索照合再追跡では応答番号 nn の形式の属性行と IEE115I を合わせ、追跡名は探索照合再追跡です。誤答側の問題点を分けます。 A: 探索照合再不足は名称や説明だけに寄り、判定名は探索照合再不足です。 B: 探索照合再正答は対象出力と項目説明を結び、根拠名は探索照合再正答です。 C: 探索照合再欠落は戻り値や記録番号に寄り、欠落名は探索照合再欠落です。 D: 探索照合再流用は別カテゴリの確認であり、排除名は探索照合再流用です。探索照合再初出では応答番号 nn の形式を MVS オペレータコマンドの運用手順で確認し、初出名は探索照合再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力確認の応答番号 の形式に関する応答番号 nn の形式の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力確認の応答番号 の形式の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力確認の応答番号 の形式の証跡として保存して根拠にする。</li><li>C. 応答番号 nn の形式の変更点を出力本文から切り離して出力確認の応答番号 の形式の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力確認の応答番号 の形式において選択記号 D を採用し、識別名は出力確認です。出力確認の応答番号 の形式において応答番号 nn の形式 は説明欄の「応答番号 nn の形式の状態と出力メッセージを結び付ける出力確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認の応答番号 の形式に関する記録は、応答番号 nn の形式の出力行と IEE115I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認の応答番号 の形式は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力確認ではありません。 B: 出力確認の応答番号 の形式は別カテゴリの確認を流用しており、応答番号 nn の形式の根拠にならないため出力確認ではありません。 C: 出力確認の応答番号 の形式は名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認の応答番号 の形式は対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認の応答番号 の形式で記録する応答番号 nn の形式はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>応答番号 nn の形式</strong></p><p>検証目的: 構文整理の応答番号 の形式について、応答番号 nn の形式は、MVS オペレータコマンドの R で確認する項目です。nn は 00〜99 (1, 2 桁) を表示時の番号で指定する。番号は WTOR 単位に動的割に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020101の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文整理の応答番号 の形式の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に応答番号 nn の形式を指定し、OSKB020101の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND 応答番号 nn の形式
CASE OSKB020101
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM 応答番号 nn の形式
CASE OSKB020101
SOURCE z/OS MVS Operations
応答番号 nn の形式とOSKB020101が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020101を同じ出力で読み、構文整理の応答番号 の形式の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020101
→ Enter を押す
［画面・出力］
IEE115I OSKB020101 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020101   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020101が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の 応答番号 nn の形式 と OSKB020101 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020101 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## ROUTE


<section class="kb-item" id="c22-i0216"><h3>ROUTE (sys1,sys2),cmd</h3><p class="kb-meta">分類: ROUTE ・ 難易度: 中級</p><p>ROUTE (sys1,sys2),cmdは、MVS オペレータコマンドのROUTEで確認する項目です。複数システムのリストを指定して一斉発行する。サブセットへの送信</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査追跡の操作コマンドで操作コマンドの運用確認を行います。ROUTE (sys1,sys2),cmdの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査追跡の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、監査追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. ROUTE (sys1,sys2),cmdの属性行を読まず監査追跡の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査追跡の操作コマンドにおいて選択記号 C を採用し、識別名は監査追跡です。監査追跡の操作コマンドにおいて ROUTE (sys1,sys2),cmd は説明欄の「z/OS MVS Operationsで ROUTE (sys1,sys2),cmdの扱いを記録する監査追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査追跡です。監査追跡の操作コマンドを受け取る担当者は、ROUTE (sys1,sys2),cmdの表示結果と IEE115I を同じ確認単位として扱い、背景名は監査追跡です。不適切な選択肢を整理します。 A: 監査追跡の操作コマンドは別カテゴリの確認を流用しており、ROUTE (sys1,sys2),cmdの根拠にならないため監査追跡ではありません。 B: 監査追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査追跡ではありません。 C: 監査追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので監査追跡です。 D: 監査追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査追跡ではありません。監査追跡の操作コマンドが示す ROUTE (sys1,sys2),cmdは出典欄の資料で使い方を追跡できる項目であり、用語名は監査追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>ROUTE (sys1,sys2),cmd</strong></p><p>検証目的: 上書追跡の操作コマンドについて、ROUTE (sys1,sys2),cmdは、MVS オペレータコマンドの ROUTE で確認する項目です。複数システムのリストを指定して一斉発行する。サブセットへの送信に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040047の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE (sys1,sys2),を指定し、OSKB040047の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND ROUTE (sys1,sys2),
CASE OSKB040047
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM ROUTE (sys1,sys2),
CASE OSKB040047
SOURCE z/OS MVS Operations
ROUTE (sys1,sys2),とOSKB040047が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040047を同じ出力で読み、上書追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040047
→ Enter を押す
［画面・出力］
IEE115I OSKB040047 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040047   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040047が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の ROUTE (sys1,sys2), と OSKB040047 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040047 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>ROUTE (sys1,sys2),cmd</strong></p><p>検証目的: 優先照合の操作コマンドについて、ROUTE (sys1,sys2),cmdは、MVS オペレータコマンドの ROUTE で確認する項目です。複数システムのリストを指定して一斉発行する。サブセットへの送信に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030032の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE (sys1,sys2),を指定し、OSKB030032の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND ROUTE (sys1,sys2),
CASE OSKB030032
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM ROUTE (sys1,sys2),
CASE OSKB030032
SOURCE z/OS MVS Operations
ROUTE (sys1,sys2),とOSKB030032が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030032を同じ出力で読み、優先照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030032
→ Enter を押す
［画面・出力］
IEE115I OSKB030032 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030032   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030032が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の ROUTE (sys1,sys2), と OSKB030032 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030032 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0217"><h3>ROUTE *ALL,cmd</h3><p class="kb-meta">分類: ROUTE ・ 難易度: 中級</p><p>ROUTE *ALL,cmdは、MVS オペレータコマンドのROUTEで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告追跡の*に関係する ROUTE *ALL,cmdの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、警告追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. ROUTE *ALL,cmdの名称と担当者名のみを残して警告追跡の*の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で警告追跡の*を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告追跡の*の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告追跡の*において選択記号 A を採用し、識別名は警告追跡です。警告追跡の*において ROUTE *ALL,cmd は説明欄の「ROUTE *ALL,cmdの用途を操作コマンドの表示で確認する警告追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告追跡です。警告追跡の*に関連して、z/OS MVS Operationsでは ROUTE *ALL,cmdの表示属性と IEE115I を同じ証跡に残し、背景名は警告追跡です。他の選択肢を確認します。 A: 警告追跡の*は対象出力と項目説明を結び、根拠を残すので警告追跡です。 B: 警告追跡の*は名称や説明のみに寄り、状態を示す出力本文が不足するため警告追跡ではありません。 C: 警告追跡の*は別カテゴリの確認を流用しており、ROUTE *ALL,cmdの根拠にならないため警告追跡ではありません。 D: 警告追跡の*は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告追跡ではありません。警告追跡の*で使う ROUTE *ALL,cmdという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ROUTE *ALL,cmd</strong></p><p>検証目的: 区切照合の*について、ROUTE *ALL,cmdは、MVS オペレータコマンドの ROUTE で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030030の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切照合の*の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE *ALL,cmdを指定し、OSKB030030の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND ROUTE *ALL,cmd
CASE OSKB030030
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM ROUTE *ALL,cmd
CASE OSKB030030
SOURCE z/OS MVS Operations
ROUTE *ALL,cmdとOSKB030030が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030030を同じ出力で読み、区切照合の*の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030030
→ Enter を押す
［画面・出力］
IEE115I OSKB030030 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030030   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030030が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の ROUTE *ALL,cmd と OSKB030030 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0218"><h3>ROUTE T=seconds,...</h3><p class="kb-meta">分類: ROUTE ・ 難易度: 中級</p><p>ROUTE T=seconds,...は、MVS オペレータコマンドのROUTEで確認する項目です。応答待ちタイムアウトを指定。Sysplex 内応答が揃わない場合の待ち時間制御</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更追跡のなどに関する ROUTE T=seconds,などの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更追跡のなどの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更追跡のなどの証跡として保存して根拠にする。</li><li>C. ROUTE T=seconds,などの変更点を出力本文から切り離して変更追跡のなどの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、変更追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更追跡のなどにおいて選択記号 D を採用し、識別名は変更追跡です。変更追跡のなどにおいて ROUTE T=seconds,など は説明欄の「ROUTE T=seconds,などの状態と出力メッセージを結び付ける変更追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更追跡です。変更追跡のなどに関する記録は、ROUTE T=seconds,などの出力行と IEE115I を一緒に保存し、背景名は変更追跡です。選択肢ごとの違いを示します。 A: 変更追跡のなどは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更追跡ではありません。 B: 変更追跡のなどは別カテゴリの確認を流用しており、ROUTE T=seconds,などの根拠にならないため変更追跡ではありません。 C: 変更追跡のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため変更追跡ではありません。 D: 変更追跡のなどは対象出力と項目説明を結び、根拠を残すので変更追跡です。変更追跡のなどで記録する ROUTE T=seconds,などはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details></section>


<section class="kb-item" id="c22-i0219"><h3>ROUTE sysname,cmd</h3><p class="kb-meta">分類: ROUTE ・ 難易度: 中級</p><p>ROUTE sysname,cmdは、特定の Sysplex メンバ・システムにコマンドをルーティングする形式</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧追跡の操作コマンドで ROUTE sysname,cmdの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. ROUTE sysname,cmdの出力を取らず復旧追跡の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、復旧追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧追跡の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧追跡の操作コマンドにおいて選択記号 B を採用し、識別名は復旧追跡です。復旧追跡の操作コマンドにおいて ROUTE sysname,cmd は説明欄の「復旧追跡の操作コマンドに関係する定義値と表示行を照合する復旧追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧追跡です。復旧追跡の操作コマンドの証跡を読む担当者は、ROUTE sysname,cmdの属性行と IEE115I を合わせて追跡し、背景名は復旧追跡です。誤答側の問題点を分けます。 A: 復旧追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧追跡ではありません。 B: 復旧追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧追跡です。 C: 復旧追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧追跡ではありません。 D: 復旧追跡の操作コマンドは別カテゴリの確認を流用しており、ROUTE sysname,cmdの根拠にならないため復旧追跡ではありません。復旧追跡の操作コマンドに出る ROUTE sysname,cmdは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ROUTE sysname,cmd</strong></p><p>検証目的: 範囲照合の操作コマンドについて、ROUTE sysname,cmdは、特定の Sysplex メンバ・システムにコマンドをルーティングする形式に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030031の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE sysname,cmdを指定し、OSKB030031の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND ROUTE sysname,cmd
CASE OSKB030031
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM ROUTE sysname,cmd
CASE OSKB030031
SOURCE z/OS MVS Operations
ROUTE sysname,cmdとOSKB030031が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030031を同じ出力で読み、範囲照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030031
→ Enter を押す
［画面・出力］
IEE115I OSKB030031 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030031   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030031が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の ROUTE sysname,cmd と OSKB030031 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030031 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S


<section class="kb-item" id="c22-i0220"><h3>JOBNAME= 指定</h3><p class="kb-meta">分類: S ・ 難易度: 中級</p><p>JOBNAME= 指定は、MVS オペレータコマンドのSで確認する項目です。STC のジョブ名を明示的に指定する。同一プロシージャで複数インスタンスを区別する典型用途</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告読解の指定に関係する JOBNAME= 指定の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、警告読解の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. JOBNAME= 指定の名称と担当者名だけを残して警告読解の指定の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告読解の指定を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告読解の指定の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告読解正解では選択記号 A を採用し、正解名は警告読解正解です。警告読解根拠では JOBNAME= 指定 は「JOBNAME= 指定の用途を操作コマンドの表示で確認する警告読解項目」と D A,L または該当パネルの出力を照合し、根拠名は警告読解根拠です。警告読解背景ではz/OS MVS Operationsの JOBNAME= 指定と IEE115I を同じ証跡に残し、背景名は警告読解背景です。他の選択肢を確認します。 A: 警告読解正答は対象出力と項目説明を結び、根拠名は警告読解正答です。 B: 警告読解不足は名称や説明だけに寄り、判定名は警告読解不足です。 C: 警告読解流用は別カテゴリの確認であり、排除名は警告読解流用です。 D: 警告読解欠落は戻り値や記録番号に寄り、欠落名は警告読解欠落です。警告読解用語では JOBNAME= 指定を MVS オペレータコマンドで扱う確認対象とし、用語名は警告読解用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>JOBNAME= 指定</strong></p><p>検証目的: 優先追跡の指定について、JOBNAME= 指定は、MVS オペレータコマンドの S で確認する項目です。STC のジョブ名を明示的に指定する。同一プロシージャで複数インスタンスを区別する典型用途に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020052の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先追跡の指定の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にJOBNAME= 指定を指定し、OSKB020052の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND JOBNAME= 指定
CASE OSKB020052
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM JOBNAME= 指定
CASE OSKB020052
SOURCE z/OS MVS Operations
JOBNAME= 指定とOSKB020052が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020052を同じ出力で読み、優先追跡の指定の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020052
→ Enter を押す
［画面・出力］
IEE115I OSKB020052 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020052   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020052が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の JOBNAME= 指定 と OSKB020052 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020052 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0221"><h3>REUSASID=YES 指定</h3><p class="kb-meta">分類: S ・ 難易度: 中級</p><p>REUSASID=YES 指定は、MVS オペレータコマンドのSで確認する項目です。新規 STC 起動時に再利用可能 ASID を割り当てる。ASID 枯渇対策時に使用する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域読解の指定に関する REUSASID=YES 指定の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域読解の指定の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域読解の指定の証跡として保存して根拠にする。</li><li>C. REUSASID=YES 指定の変更点を出力本文から切り離して値域読解の指定の承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、値域読解の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域読解正解では選択記号 D を採用し、正解名は値域読解正解です。値域読解根拠では REUSASID=YES 指定 は「REUSASID=YES 指定の状態と出力メッセージを結び付ける値域読解項目」と D A,L または該当パネルの出力を照合し、根拠名は値域読解根拠です。値域読解保存では REUSASID=YES 指定の出力行と IEE115I を一緒に残し、保存名は値域読解保存です。選択肢ごとの違いを示します。 A: 値域読解欠落は戻り値や記録番号に寄り、欠落名は値域読解欠落です。 B: 値域読解流用は別カテゴリの確認であり、排除名は値域読解流用です。 C: 値域読解不足は名称や説明だけに寄り、判定名は値域読解不足です。 D: 値域読解正答は対象出力と項目説明を結び、根拠名は値域読解正答です。値域読解対象では REUSASID=YES 指定をz/OS MVS Operationsの確認記録に残し、対象名は値域読解対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REUSASID=YES 指定</strong></p><p>検証目的: 範囲追跡の指定について、REUSASID=YES 指定は、MVS オペレータコマンドの S で確認する項目です。新規 STC 起動時に再利用可能 ASID を割り当てる。ASID 枯渇対策時に使用するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020051の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲追跡の指定の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にREUSASID=YES 指定を指定し、OSKB020051の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND REUSASID=YES 指定
CASE OSKB020051
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM REUSASID=YES 指定
CASE OSKB020051
SOURCE z/OS MVS Operations
REUSASID=YES 指定とOSKB020051が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020051を同じ出力で読み、範囲追跡の指定の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020051
→ Enter を押す
［画面・出力］
IEE115I OSKB020051 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020051   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020051が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の REUSASID=YES 指定 と OSKB020051 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020051 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0222"><h3>S コマンド基本構文</h3><p class="kb-meta">分類: S ・ 難易度: 初級</p><p>S コマンド基本構文は、MVS オペレータコマンドのSで状態表示や操作を行うためのコマンド関連項目です。S procname.identifier,parm=value の形でカタログ・プロシージャを起動する。短縮形 S。実行は新規アドレス・スペースで行われる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較読解のコマンド基本構文で S コマンド基本構文の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. S コマンド基本構文の出力を取らず比較読解のコマンド基本構文の説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて比較読解の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較読解のコマンド基本構文の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較読解のコマンド基本構文へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 比較読解正解では選択記号 B を採用し、正解名は比較読解正解です。比較読解根拠では S コマンド基本構文 は「比較読解のコマンド基本構文に関係する定義値と表示行を照合する比較読解項目」と D A,L または該当パネルの出力を照合し、根拠名は比較読解根拠です。比較読解追跡では S コマンド基本構文の属性行と IEE115I を合わせ、追跡名は比較読解追跡です。誤答側の問題点を分けます。 A: 比較読解不足は名称や説明だけに寄り、判定名は比較読解不足です。 B: 比較読解正答は対象出力と項目説明を結び、根拠名は比較読解正答です。 C: 比較読解欠落は戻り値や記録番号に寄り、欠落名は比較読解欠落です。 D: 比較読解流用は別カテゴリの確認であり、排除名は比較読解流用です。比較読解初出では S コマンド基本構文を MVS オペレータコマンドの運用手順で確認し、初出名は比較読解初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S コマンド基本構文</strong></p><p>検証目的: 条件追跡のコマンド基本構文について、S コマンド基本構文は、MVS オペレータコマンドの S で状態表示や操作を行うためのコマンド関連項目です。S procname.identifier,parm=value のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020049の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件追跡のコマンド基本構文の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS コマンド基本構文を指定し、OSKB020049の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S コマンド基本構文
CASE OSKB020049
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S コマンド基本構文
CASE OSKB020049
SOURCE z/OS MVS Operations
S コマンド基本構文とOSKB020049が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020049を同じ出力で読み、条件追跡のコマンド基本構文の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020049
→ Enter を押す
［画面・出力］
IEE115I OSKB020049 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020049   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020049が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S コマンド基本構文 と OSKB020049 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020049 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0223"><h3>識別子 (identifier) の役割</h3><p class="kb-meta">分類: S ・ 難易度: 中級</p><p>識別子 (identifier) の役割は、MVS オペレータコマンドのSで確認する項目です。S TSO.TSO01 のように同一プロシージャを複数同時起動する場合に区別する。MODIFY/STOP の対象指定にも使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序読解の識別子 の役割で操作コマンドの運用確認を行います。識別子 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序読解の識別子 の役割を確認した扱いにする。</li><li>B. IEE457I の有無を確認せず順序読解の識別子 の役割を正常終了として記録する。</li><li>C. IEE457I を含む表示を保存し、説明欄との差分を順序読解で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. 識別子 属性の属性行を読まず順序読解の識別子 の役割の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序読解正解では選択記号 C を採用し、正解名は順序読解正解です。順序読解根拠では識別子 属性は「z/OS MVS Operationsで識別子 属性の扱いを記録する順序読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は順序読解根拠です。順序読解受渡では識別子 属性の表示結果と IEE457I を同じ確認単位にし、受渡名は順序読解受渡です。不適切な選択肢を整理します。 A: 順序読解流用は別カテゴリの確認であり、排除名は順序読解流用です。 B: 順序読解欠落は戻り値や記録番号に寄り、欠落名は順序読解欠落です。 C: 順序読解正答は対象出力と項目説明を結び、根拠名は順序読解正答です。 D: 順序読解不足は名称や説明だけに寄り、判定名は順序読解不足です。順序読解資料では識別子 属性の使い方を出典欄から追跡し、資料名は順序読解資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>識別子 (identifier) の役割</strong></p><p>検証目的: 区切照合の識別子 の役割について、識別子 (identifier) の役割は、MVS オペレータコマンドの S で確認する項目です。S TSO.TSO01 のように同一プロシージャを複数同時起動する場合に区別すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040030の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、区切照合の識別子 の役割の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に識別子 (identifier) のを指定し、OSKB040030の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND 識別子 (identifier) の
CASE OSKB040030
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM 識別子 (identifier) の
CASE OSKB040030
SOURCE z/OS MVS Operations
識別子 (identifier) のとOSKB040030が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040030を同じ出力で読み、区切照合の識別子 の役割の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB040030
→ Enter を押す
［画面・出力］
IEE457I OSKB040030 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040030   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB040030が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の 識別子 (identifier) の と OSKB040030 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB040030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>識別子 (identifier) の役割</strong></p><p>検証目的: 区切追跡の識別子 の役割について、識別子 (identifier) の役割は、MVS オペレータコマンドの S で確認する項目です。S TSO.TSO01 のように同一プロシージャを複数同時起動する場合に区別すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020050の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、区切追跡の識別子 の役割の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に識別子 (identifier) のを指定し、OSKB020050の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND 識別子 (identifier) の
CASE OSKB020050
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM 識別子 (identifier) の
CASE OSKB020050
SOURCE z/OS MVS Operations
識別子 (identifier) のとOSKB020050が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020050を同じ出力で読み、区切追跡の識別子 の役割の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020050
→ Enter を押す
［画面・出力］
IEE457I OSKB020050 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020050   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020050が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の 識別子 (identifier) の と OSKB020050 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020050 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S APPC


<section class="kb-item" id="c22-i0224"><h3>S APPC APPC/MVS 起動</h3><p class="kb-meta">分類: S APPC ・ 難易度: 中級</p><p>APPC/MVS サブシステムを起動する。続けて S ASCH で ASCH スケジューラを起動する手順が標準</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書検分の・ 起動で操作コマンドの運用確認を行います。S APPC APPC 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書検分の・ 起動を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書検分の・ 起動を正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を上書検分で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. S APPC APPC 属性の属性行を読まず上書検分の・ 起動の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書検分正解では選択記号 C を採用し、正解名は上書検分正解です。上書検分根拠では S APPC APPC 属性 は「z/OS MVS Operationsで S APPC APPC 属性の扱いを記録する上書検分項目」と D A,L または該当パネルの出力を照合し、根拠名は上書検分根拠です。上書検分受渡では S APPC APPC 属性の表示結果と IEE115I を同じ確認単位にし、受渡名は上書検分受渡です。不適切な選択肢を整理します。 A: 上書検分流用は別カテゴリの確認であり、排除名は上書検分流用です。 B: 上書検分欠落は戻り値や記録番号に寄り、欠落名は上書検分欠落です。 C: 上書検分正答は対象出力と項目説明を結び、根拠名は上書検分正答です。 D: 上書検分不足は名称や説明だけに寄り、判定名は上書検分不足です。上書検分資料では S APPC APPC 属性の使い方を出典欄から追跡し、資料名は上書検分資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>S APPC APPC ・ MVS 起動</strong></p><p>検証目的: 優先照合の・ 起動について、APPC/MVS サブシステムを起動する。続けて S ASCH で ASCH スケジューラを起動する手順が標準に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040032の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先照合の・ 起動の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS APPC APPC ・ MVS を指定し、OSKB040032の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S APPC APPC ・ MVS 
CASE OSKB040032
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S APPC APPC ・ MVS 
CASE OSKB040032
SOURCE z/OS MVS Operations
S APPC APPC ・ MVS とOSKB040032が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040032を同じ出力で読み、優先照合の・ 起動の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040032
→ Enter を押す
［画面・出力］
IEE115I OSKB040032 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040032   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040032が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S APPC APPC ・ MVS  と OSKB040032 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040032 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>S APPC APPC ・ MVS 起動</strong></p><p>検証目的: 展開検査の・ 起動について、APPC/MVS サブシステムを起動する。続けて S ASCH で ASCH スケジューラを起動する手順が標準に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020062の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開検査の・ 起動の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS APPC APPC ・ MVS を指定し、OSKB020062の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S APPC APPC ・ MVS 
CASE OSKB020062
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S APPC APPC ・ MVS 
CASE OSKB020062
SOURCE z/OS MVS Operations
S APPC APPC ・ MVS とOSKB020062が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020062を同じ出力で読み、展開検査の・ 起動の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020062
→ Enter を押す
［画面・出力］
IEE115I OSKB020062 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020062   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020062が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S APPC APPC ・ MVS  と OSKB020062 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020062 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S CICS


<section class="kb-item" id="c22-i0225"><h3>S CICS リージョン起動</h3><p class="kb-meta">分類: S CICS ・ 難易度: 上級</p><p>CICS Transaction Server のリージョンを起動。S CICSPROD.CICSPROD のように識別子で本番/開発を区別する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更読解のリージョン起動に関する S CICS リージョン起動の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更読解のリージョン起動の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更読解のリージョン起動の証跡として保存して根拠にする。</li><li>C. S CICS リージョン起動の変更点を出力本文から切り離して変更読解のリージョン起動の承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、変更読解の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更読解正解では選択記号 D を採用し、正解名は変更読解正解です。変更読解根拠では S CICS リージョン起動 は「S CICS リージョン起動の状態と出力メッセージを結び付ける変更読解項目」と D A,L または該当パネルの出力を照合し、根拠名は変更読解根拠です。変更読解保存では S CICS リージョン起動の出力行と IEE115I を一緒に残し、保存名は変更読解保存です。選択肢ごとの違いを示します。 A: 変更読解欠落は戻り値や記録番号に寄り、欠落名は変更読解欠落です。 B: 変更読解流用は別カテゴリの確認であり、排除名は変更読解流用です。 C: 変更読解不足は名称や説明だけに寄り、判定名は変更読解不足です。 D: 変更読解正答は対象出力と項目説明を結び、根拠名は変更読解正答です。変更読解対象では S CICS リージョン起動をz/OS MVS Operationsの確認記録に残し、対象名は変更読解対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S CICS リージョン起動</strong></p><p>検証目的: 順序追跡のリージョン起動について、CICS Transaction Server のリージョンを起動。S CICSPROD.CICSPROD のように識別子で本番/開発を区別するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020055の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序追跡のリージョン起動の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS CICS リージョン起動を指定し、OSKB020055の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S CICS リージョン起動
CASE OSKB020055
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S CICS リージョン起動
CASE OSKB020055
SOURCE z/OS MVS Operations
S CICS リージョン起動とOSKB020055が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020055を同じ出力で読み、順序追跡のリージョン起動の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020055
→ Enter を押す
［画面・出力］
IEE115I OSKB020055 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020055   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020055が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S CICS リージョン起動 と OSKB020055 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020055 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S DB2


<section class="kb-item" id="c22-i0226"><h3>S DB2 サブシステム起動</h3><p class="kb-meta">分類: S DB2 ・ 難易度: 中級</p><p>S DB2 サブシステム起動は、Db2 for z/OS の制御アドレス・スペース (xxxxMSTR / xxxxDBM1 / xxxxDIST) を起動する S コマンド</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文検分のサブシステム起動に関係する S DB2 サブシステム起動の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、構文検分として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. S DB2 サブシステム起動の名称と担当者名だけを残して構文検分のサブシステム起動の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文検分のサブシステム起動を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文検分のサブシステム起動の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文検分正解では選択記号 A を採用し、正解名は構文検分正解です。構文検分根拠では S DB2 サブシステム起動 は「S DB2 サブシステム起動の用途を操作コマンドの表示で確認する構文検分項目」と D A,L または該当パネルの出力を照合し、根拠名は構文検分根拠です。構文検分背景ではz/OS MVS Operationsの S DB2 サブシステム起動と IEE115I を同じ証跡に残し、背景名は構文検分背景です。他の選択肢を確認します。 A: 構文検分正答は対象出力と項目説明を結び、根拠名は構文検分正答です。 B: 構文検分不足は名称や説明だけに寄り、判定名は構文検分不足です。 C: 構文検分流用は別カテゴリの確認であり、排除名は構文検分流用です。 D: 構文検分欠落は戻り値や記録番号に寄り、欠落名は構文検分欠落です。構文検分用語では S DB2 サブシステム起動を MVS オペレータコマンドで扱う確認対象とし、用語名は構文検分用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>S DB2 サブシステム起動</strong></p><p>検証目的: 範囲照合のサブシステム起動について、S DB2 サブシステム起動は、Db2 for z/OS の制御アドレス・スペース (xxxxMSTR / xxxxDBM1 / xxxxDIST) を起動する S コマンに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040031の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲照合のサブシステム起動の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS DB2 サブシステム起動を指定し、OSKB040031の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S DB2 サブシステム起動
CASE OSKB040031
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S DB2 サブシステム起動
CASE OSKB040031
SOURCE z/OS MVS Operations
S DB2 サブシステム起動とOSKB040031が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040031を同じ出力で読み、範囲照合のサブシステム起動の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040031
→ Enter を押す
［画面・出力］
IEE115I OSKB040031 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040031   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040031が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S DB2 サブシステム起動 と OSKB040031 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040031 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>S DB2 サブシステム起動</strong></p><p>検証目的: 値域追跡のサブシステム起動について、S DB2 サブシステム起動は、Db2 for z/OS の制御アドレス・スペース (xxxxMSTR / xxxxDBM1 / xxxxDIST) を起動する S コマンに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020056の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域追跡のサブシステム起動の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS DB2 サブシステム起動を指定し、OSKB020056の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S DB2 サブシステム起動
CASE OSKB020056
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S DB2 サブシステム起動
CASE OSKB020056
SOURCE z/OS MVS Operations
S DB2 サブシステム起動とOSKB020056が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020056を同じ出力で読み、値域追跡のサブシステム起動の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020056
→ Enter を押す
［画面・出力］
IEE115I OSKB020056 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020056   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020056が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S DB2 サブシステム起動 と OSKB020056 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020056 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S DLF


<section class="kb-item" id="c22-i0227"><h3>S DLF Hiperbatch 起動</h3><p class="kb-meta">分類: S DLF ・ 難易度: 中級</p><p>S DLF Hiperbatch 起動は、MVS オペレータコマンドのS DLFで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索検分の起動で S DLF Hiperbatch 起動の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. S DLF Hiperbatch 起動の出力を取らず探索検分の起動の説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて探索検分の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索検分の起動の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索検分の起動へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索検分正解では選択記号 B を採用し、正解名は探索検分正解です。探索検分根拠では S DLF Hiperbatch 起動 は「探索検分の起動に関係する定義値と表示行を照合する探索検分項目」と D A,L または該当パネルの出力を照合し、根拠名は探索検分根拠です。探索検分追跡では S DLF Hiperbatch 起動の属性行と IEE115I を合わせ、追跡名は探索検分追跡です。誤答側の問題点を分けます。 A: 探索検分不足は名称や説明だけに寄り、判定名は探索検分不足です。 B: 探索検分正答は対象出力と項目説明を結び、根拠名は探索検分正答です。 C: 探索検分欠落は戻り値や記録番号に寄り、欠落名は探索検分欠落です。 D: 探索検分流用は別カテゴリの確認であり、排除名は探索検分流用です。探索検分初出では S DLF Hiperbatch 起動を MVS オペレータコマンドの運用手順で確認し、初出名は探索検分初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S DLF Hiperbatch 起動</strong></p><p>検証目的: 構文検査の起動について、S DLF Hiperbatch 起動は、MVS オペレータコマンドの S DLF で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020061の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文検査の起動の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS DLF Hiperbatch 起を指定し、OSKB020061の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S DLF Hiperbatch 起
CASE OSKB020061
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S DLF Hiperbatch 起
CASE OSKB020061
SOURCE z/OS MVS Operations
S DLF Hiperbatch 起とOSKB020061が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020061を同じ出力で読み、構文検査の起動の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020061
→ Enter を押す
［画面・出力］
IEE115I OSKB020061 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020061   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020061が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S DLF Hiperbatch 起 と OSKB020061 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020061 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S DUMPSRV


<section class="kb-item" id="c22-i0228"><h3>S DUMPSRV SVC ダンプ・サービス</h3><p class="kb-meta">分類: S DUMPSRV ・ 難易度: 中級</p><p>S DUMPSRV SVC ダンプ・サービスは、MVS オペレータコマンドのS DUMPSRVで確認する項目です。DUMPSRV (SVC ダンプ・サービス) を起動する。通常 IPL 時自動起動で手動の再起動用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先検分のダンプ・サービスに関する S DUMPSRV SVC ダンプ 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先検分のダンプ・サービスの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先検分のダンプ・サービスの証跡として保存して根拠にする。</li><li>C. S DUMPSRV SVC ダンプ 属性の変更点を出力本文から切り離して優先検分のダンプ・サービスの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、優先検分の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では S DUMPSRV SVC ダンプ 属性 は「S DUMPSRV SVC ダンプ 属性の状態と出力メッセージを結び付ける優先検分項目」と D A,L または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では S DUMPSRV SVC ダンプ 属性の出力行と IEE115I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明だけに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では S DUMPSRV SVC ダンプ 属性をz/OS MVS Operationsの確認記録に残し、対象名は優先検分対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S DUMPSRV SVC ダンプ・サービス</strong></p><p>検証目的: 上書検査のダンプ・サービスについて、S DUMPSRV SVC ダンプ・サービスは、MVS オペレータコマンドの S DUMPSRV で確認する項目です。DUMPSRV (SVC ダンプ・サービス) を起動する。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020067の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書検査のダンプ・サービスの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS DUMPSRV SVC ダンプ・を指定し、OSKB020067の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S DUMPSRV SVC ダンプ・
CASE OSKB020067
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S DUMPSRV SVC ダンプ・
CASE OSKB020067
SOURCE z/OS MVS Operations
S DUMPSRV SVC ダンプ・とOSKB020067が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020067を同じ出力で読み、上書検査のダンプ・サービスの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020067
→ Enter を押す
［画面・出力］
IEE115I OSKB020067 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020067   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020067が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S DUMPSRV SVC ダンプ・ と OSKB020067 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020067 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S JES2


<section class="kb-item" id="c22-i0229"><h3>S JES2 起動</h3><p class="kb-meta">分類: S JES2 ・ 難易度: 中級</p><p>S JES2 起動は、MVS オペレータコマンドのS JES2で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換検分の起動に関する S JES2 起動の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換検分の起動の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換検分の起動の証跡として保存して根拠にする。</li><li>C. S JES2 起動の変更点を出力本文から切り離して置換検分の起動の承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換検分で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換検分正解では選択記号 D を採用し、正解名は置換検分正解です。置換検分根拠では S JES2 起動 は「S JES2 起動の状態と出力メッセージを結び付ける置換検分項目」と D A,L または該当パネルの出力を照合し、根拠名は置換検分根拠です。置換検分保存では S JES2 起動の出力行と IEE115I を一緒に残し、保存名は置換検分保存です。選択肢ごとの違いを示します。 A: 置換検分欠落は戻り値や記録番号に寄り、欠落名は置換検分欠落です。 B: 置換検分流用は別カテゴリの確認であり、排除名は置換検分流用です。 C: 置換検分不足は名称や説明だけに寄り、判定名は置換検分不足です。 D: 置換検分正答は対象出力と項目説明を結び、根拠名は置換検分正答です。置換検分対象では S JES2 起動をz/OS MVS Operationsの確認記録に残し、対象名は置換検分対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S JES2 起動</strong></p><p>検証目的: 監査追跡の起動について、S JES2 起動は、MVS オペレータコマンドの S JES2 で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認しますに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020059の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査追跡の起動の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS JES2 起動を指定し、OSKB020059の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S JES2 起動
CASE OSKB020059
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S JES2 起動
CASE OSKB020059
SOURCE z/OS MVS Operations
S JES2 起動とOSKB020059が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020059を同じ出力で読み、監査追跡の起動の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020059
→ Enter を押す
［画面・出力］
IEE115I OSKB020059 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020059   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020059が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S JES2 起動 と OSKB020059 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020059 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0230"><h3>S JES2,PARM=&#x27;WARM,NOREQ&#x27;</h3><p class="kb-meta">分類: S JES2 ・ 難易度: 中級</p><p>S JES2,PARM=&#x27;WARM,NOREQ&#x27;は、MVS オペレータコマンドのS JES2で確認する項目です。通常起動 (WARM) で対話プロンプトなし。運用自動化での標準形</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端検分の操作コマンドに関係する S JES2 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、終端検分の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. S JES2 命令の名称と担当者名だけを残して終端検分の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端検分の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端検分の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端検分正解では選択記号 A を採用し、正解名は終端検分正解です。終端検分根拠では S JES2 命令 は「S JES2 命令の用途を操作コマンドの表示で確認する終端検分項目」と D A,L または該当パネルの出力を照合し、根拠名は終端検分根拠です。終端検分背景ではz/OS MVS Operationsの S JES2 命令と IEE115I を同じ証跡に残し、背景名は終端検分背景です。他の選択肢を確認します。 A: 終端検分正答は対象出力と項目説明を結び、根拠名は終端検分正答です。 B: 終端検分不足は名称や説明だけに寄り、判定名は終端検分不足です。 C: 終端検分流用は別カテゴリの確認であり、排除名は終端検分流用です。 D: 終端検分欠落は戻り値や記録番号に寄り、欠落名は終端検分欠落です。終端検分用語では S JES2 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は終端検分用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S JES2,PARM=&#x27;WARM,NOREQ&#x27;</strong></p><p>検証目的: 変更追跡の操作コマンドについて、S JES2,PARM=&#x27;WARM,NOREQ&#x27;は、MVS オペレータコマンドの S JES2 で確認する項目です。通常起動 (WARM) で対話プロンプトなし。運用自動化でのに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020060の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS JES2,PARM=&#x27;WARM,を指定し、OSKB020060の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S JES2,PARM=&#x27;WARM,
CASE OSKB020060
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S JES2,PARM=&#x27;WARM,
CASE OSKB020060
SOURCE z/OS MVS Operations
S JES2,PARM=&#x27;WARM,とOSKB020060が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020060を同じ出力で読み、変更追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020060
→ Enter を押す
［画面・出力］
IEE115I OSKB020060 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020060   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020060が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S JES2,PARM=&#x27;WARM, と OSKB020060 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020060 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S LLA


<section class="kb-item" id="c22-i0231"><h3>S LLA Library Lookaside</h3><p class="kb-meta">分類: S LLA ・ 難易度: 中級</p><p>S LLA Library Lookasideは、MVS オペレータコマンドのS LLAで用いるLLA (Library Lookaside) を起動する。LNKLST ロード性能改善の前提コンポーネント。S LLAでは、指定値と対象資源、実行時の出力を突き合わせて確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力検分の操作コマンドに関する S 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力検分の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力検分の操作コマンドの証跡として保存して根拠にする。</li><li>C. S 機能の変更点を出力本文から切り離して出力検分の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、出力検分の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力検分正解では選択記号 D を採用し、正解名は出力検分正解です。出力検分根拠では S 機能 は「S 機能の状態と出力メッセージを結び付ける出力検分項目」と D A,L または該当パネルの出力を照合し、根拠名は出力検分根拠です。出力検分保存では S 機能の出力行と IEE115I を一緒に残し、保存名は出力検分保存です。選択肢ごとの違いを示します。 A: 出力検分欠落は戻り値や記録番号に寄り、欠落名は出力検分欠落です。 B: 出力検分流用は別カテゴリの確認であり、排除名は出力検分流用です。 C: 出力検分不足は名称や説明だけに寄り、判定名は出力検分不足です。 D: 出力検分正答は対象出力と項目説明を結び、根拠名は出力検分正答です。出力検分対象では S 機能をz/OS MVS Operationsの確認記録に残し、対象名は出力検分対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S LLA Library Lookaside</strong></p><p>検証目的: 呼出検査の操作コマンドについて、S LLA Library Lookasideは、MVS オペレータコマンドの S LLA で用いる LLA (Library Lookaside) を起動する。LNKLST ロに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020063の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS LLA Library Lookを指定し、OSKB020063の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S LLA Library Look
CASE OSKB020063
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S LLA Library Look
CASE OSKB020063
SOURCE z/OS MVS Operations
S LLA Library LookとOSKB020063が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020063を同じ出力で読み、呼出検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020063
→ Enter を押す
［画面・出力］
IEE115I OSKB020063 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020063   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020063が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S LLA Library Look と OSKB020063 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020063 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S NET


<section class="kb-item" id="c22-i0232"><h3>S NET VTAM 起動</h3><p class="kb-meta">分類: S NET ・ 難易度: 上級</p><p>S NET VTAM 起動は、MVS オペレータコマンドのS NETで状態表示や操作を行うためのコマンド関連項目です。VTAM (Communications Server) を起動する。SNA / TCP/IP のうち SNA 側および APPL 配下の前提となる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査読解の起動で操作コマンドの運用確認を行います。S NET VTAM 起動の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査読解の起動を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査読解の起動を正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、監査読解の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. S NET VTAM 起動の属性行を読まず監査読解の起動の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査読解正解では選択記号 C を採用し、正解名は監査読解正解です。監査読解根拠では S NET VTAM 起動 は「z/OS MVS Operationsで S NET VTAM 起動の扱いを記録する監査読解項目」と D A,L または該当パネルの出力を照合し、根拠名は監査読解根拠です。監査読解受渡では S NET VTAM 起動の表示結果と IEE115I を同じ確認単位にし、受渡名は監査読解受渡です。不適切な選択肢を整理します。 A: 監査読解流用は別カテゴリの確認であり、排除名は監査読解流用です。 B: 監査読解欠落は戻り値や記録番号に寄り、欠落名は監査読解欠落です。 C: 監査読解正答は対象出力と項目説明を結び、根拠名は監査読解正答です。 D: 監査読解不足は名称や説明だけに寄り、判定名は監査読解不足です。監査読解資料では S NET VTAM 起動の使い方を出典欄から追跡し、資料名は監査読解資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S NET VTAM 起動</strong></p><p>検証目的: 比較追跡の起動について、S NET VTAM 起動は、MVS オペレータコマンドの S NET で状態表示や操作を行うためのコマンド関連項目です。VTAM (Communications Serverに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020054の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較追跡の起動の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS NET VTAM 起動を指定し、OSKB020054の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S NET VTAM 起動
CASE OSKB020054
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S NET VTAM 起動
CASE OSKB020054
SOURCE z/OS MVS Operations
S NET VTAM 起動とOSKB020054が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020054を同じ出力で読み、比較追跡の起動の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020054
→ Enter を押す
［画面・出力］
IEE115I OSKB020054 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020054   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020054が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S NET VTAM 起動 と OSKB020054 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020054 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S OMVS


<section class="kb-item" id="c22-i0233"><h3>S OMVS=xx</h3><p class="kb-meta">分類: S OMVS ・ 難易度: 中級</p><p>S OMVS=xxは、MVS オペレータコマンドのS OMVSで確認する項目です。z/OS UNIX を BPXPRMxx 指定で初期化または再初期化する。F BPXOINIT,SHUTDOWN 後の再起動でも使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開検分の操作コマンドで S OMVS=xxの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. S OMVS=xxの出力を取らず展開検分の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開検分の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開検分の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開検分の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開検分正解では選択記号 B を採用し、正解名は展開検分正解です。展開検分根拠では S OMVS=xx は「展開検分の操作コマンドに関係する定義値と表示行を照合する展開検分項目」と D A,L または該当パネルの出力を照合し、根拠名は展開検分根拠です。展開検分追跡では S OMVS=xxの属性行と IEE115I を合わせ、追跡名は展開検分追跡です。誤答側の問題点を分けます。 A: 展開検分不足は名称や説明だけに寄り、判定名は展開検分不足です。 B: 展開検分正答は対象出力と項目説明を結び、根拠名は展開検分正答です。 C: 展開検分欠落は戻り値や記録番号に寄り、欠落名は展開検分欠落です。 D: 展開検分流用は別カテゴリの確認であり、排除名は展開検分流用です。展開検分初出では S OMVS=xxを MVS オペレータコマンドの運用手順で確認し、初出名は展開検分初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S OMVS=xx</strong></p><p>検証目的: 警告追跡の操作コマンドについて、S OMVS=xxは、MVS オペレータコマンドの S OMVS で確認する項目です。z/OS UNIX を BPXPRMxx 指定で初期化または再初期化する。F BPXOINに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020057の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、警告追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS OMVS=xxを指定し、OSKB020057の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S OMVS=xx
CASE OSKB020057
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S OMVS=xx
CASE OSKB020057
SOURCE z/OS MVS Operations
S OMVS=xxとOSKB020057が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020057を同じ出力で読み、警告追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020057
→ Enter を押す
［画面・出力］
IEE115I OSKB020057 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020057   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020057が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S OMVS=xx と OSKB020057 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020057 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S RACF


<section class="kb-item" id="c22-i0234"><h3>S RACF/ICHRDSNT 関連</h3><p class="kb-meta">分類: S RACF ・ 難易度: 中級</p><p>RACF サブシステム・アドレス・スペース (RACF SUBSYS) を起動する。RACF コマンド・プレフィックス利用の前提</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出検分の・ 関連で操作コマンドの運用確認を行います。S RACF 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出検分の・ 関連を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出検分の・ 関連を正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、呼出検分の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. S RACF 属性の属性行を読まず呼出検分の・ 関連の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 呼出検分正解では選択記号 C を採用し、正解名は呼出検分正解です。呼出検分根拠では S RACF 属性 は「z/OS MVS Operationsで S RACF 属性の扱いを記録する呼出検分項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出検分根拠です。呼出検分受渡では S RACF 属性の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出検分受渡です。不適切な選択肢を整理します。 A: 呼出検分流用は別カテゴリの確認であり、排除名は呼出検分流用です。 B: 呼出検分欠落は戻り値や記録番号に寄り、欠落名は呼出検分欠落です。 C: 呼出検分正答は対象出力と項目説明を結び、根拠名は呼出検分正答です。 D: 呼出検分不足は名称や説明だけに寄り、判定名は呼出検分不足です。呼出検分資料では S RACF 属性の使い方を出典欄から追跡し、資料名は呼出検分資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S RACF ・ ICHRDSNT 関連</strong></p><p>検証目的: 復旧追跡の・ 関連について、RACF サブシステム・アドレス・スペース (RACF SUBSYS) を起動する。RACF コマンド・プレフィックス利用の前提に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020058の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧追跡の・ 関連の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS RACF ・ ICHRDSNT を指定し、OSKB020058の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S RACF ・ ICHRDSNT 
CASE OSKB020058
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S RACF ・ ICHRDSNT 
CASE OSKB020058
SOURCE z/OS MVS Operations
S RACF ・ ICHRDSNT とOSKB020058が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020058を同じ出力で読み、復旧追跡の・ 関連の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020058
→ Enter を押す
［画面・出力］
IEE115I OSKB020058 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020058   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020058が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S RACF ・ ICHRDSNT  と OSKB020058 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020058 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S SCH


<section class="kb-item" id="c22-i0235"><h3>S ASCH スケジューラ</h3><p class="kb-meta">分類: S SCH ・ 難易度: 中級</p><p>S ASCH スケジューラは、MVS オペレータコマンドのS SCHで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切検分のスケジューラで S ASCH スケジューラの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. S ASCH スケジューラの出力を取らず区切検分のスケジューラの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて区切検分の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切検分のスケジューラの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切検分のスケジューラへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切検分正解では選択記号 B を採用し、正解名は区切検分正解です。区切検分根拠では S ASCH スケジューラ は「区切検分のスケジューラに関係する定義値と表示行を照合する区切検分項目」と D A,L または該当パネルの出力を照合し、根拠名は区切検分根拠です。区切検分追跡では S ASCH スケジューラの属性行と IEE115I を合わせ、追跡名は区切検分追跡です。誤答側の問題点を分けます。 A: 区切検分不足は名称や説明だけに寄り、判定名は区切検分不足です。 B: 区切検分正答は対象出力と項目説明を結び、根拠名は区切検分正答です。 C: 区切検分欠落は戻り値や記録番号に寄り、欠落名は区切検分欠落です。 D: 区切検分流用は別カテゴリの確認であり、排除名は区切検分流用です。区切検分初出では S ASCH スケジューラを MVS オペレータコマンドの運用手順で確認し、初出名は区切検分初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S ASCH スケジューラ</strong></p><p>検証目的: 終端検査のスケジューラについて、S ASCH スケジューラは、MVS オペレータコマンドの S SCH で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020065の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端検査のスケジューラの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS ASCH スケジューラを指定し、OSKB020065の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S ASCH スケジューラ
CASE OSKB020065
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S ASCH スケジューラ
CASE OSKB020065
SOURCE z/OS MVS Operations
S ASCH スケジューラとOSKB020065が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020065を同じ出力で読み、終端検査のスケジューラの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020065
→ Enter を押す
［画面・出力］
IEE115I OSKB020065 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020065   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020065が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S ASCH スケジューラ と OSKB020065 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020065 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S TRACE


<section class="kb-item" id="c22-i0236"><h3>S TRACE,...の不在</h3><p class="kb-meta">分類: S TRACE ・ 難易度: 上級</p><p>トレースは S ではなく TRACE CT,ON / SET TRACE で開始する点に注意。S は使用しない</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p></section>


## S TSO


<section class="kb-item" id="c22-i0237"><h3>S TSO TSO/E 起動</h3><p class="kb-meta">分類: S TSO ・ 難易度: 中級</p><p>S TSO TSO/E 起動は、MVS オペレータコマンドのS TSOで確認する項目です。TSO/E サブシステム (TSO サブシステム・アドレス・スペース) を起動する。LOGON 受付の前提</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧読解の・ 起動で S TSO TSO ・ E 起動の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. S TSO TSO ・ E 起動の出力を取らず復旧読解の・ 起動の説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて復旧読解の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧読解の・ 起動の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧読解の・ 起動へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧読解正解では選択記号 B を採用し、正解名は復旧読解正解です。復旧読解根拠では S TSO TSO ・ E 起動 は「復旧読解の・ 起動に関係する定義値と表示行を照合する復旧読解項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧読解根拠です。復旧読解追跡では S TSO TSO ・ E 起動の属性行と IEE115I を合わせ、追跡名は復旧読解追跡です。誤答側の問題点を分けます。 A: 復旧読解不足は名称や説明だけに寄り、判定名は復旧読解不足です。 B: 復旧読解正答は対象出力と項目説明を結び、根拠名は復旧読解正答です。 C: 復旧読解欠落は戻り値や記録番号に寄り、欠落名は復旧読解欠落です。 D: 復旧読解流用は別カテゴリの確認であり、排除名は復旧読解流用です。復旧読解初出では S TSO TSO ・ E 起動を MVS オペレータコマンドの運用手順で確認し、初出名は復旧読解初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S TSO TSO ・ E 起動</strong></p><p>検証目的: 記録追跡の・ 起動について、S TSO TSO/E 起動は、MVS オペレータコマンドの S TSO で確認する項目です。TSO/E サブシステム (TSO サブシステム・アドレス・スペース) を起動するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020053の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録追跡の・ 起動の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS TSO TSO ・ E 起動を指定し、OSKB020053の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S TSO TSO ・ E 起動
CASE OSKB020053
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S TSO TSO ・ E 起動
CASE OSKB020053
SOURCE z/OS MVS Operations
S TSO TSO ・ E 起動とOSKB020053が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020053を同じ出力で読み、記録追跡の・ 起動の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020053
→ Enter を押す
［画面・出力］
IEE115I OSKB020053 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020053   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020053が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S TSO TSO ・ E 起動 と OSKB020053 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020053 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## S VLF


<section class="kb-item" id="c22-i0238"><h3>S VLF Virtual Lookaside</h3><p class="kb-meta">分類: S VLF ・ 難易度: 中級</p><p>VLF (Virtual Lookaside Facility) を起動する。CSVLLA・キャタログ・RACF の各キャッシュの前提</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件検分の操作コマンドに関係する S 機能の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、条件検分の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. S 機能の名称と担当者名だけを残して条件検分の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件検分の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件検分の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件検分正解では選択記号 A を採用し、正解名は条件検分正解です。条件検分根拠では S 機能 は「S 機能の用途を操作コマンドの表示で確認する条件検分項目」と D A,L または該当パネルの出力を照合し、根拠名は条件検分根拠です。条件検分背景ではz/OS MVS Operationsの S 機能と IEE115I を同じ証跡に残し、背景名は条件検分背景です。他の選択肢を確認します。 A: 条件検分正答は対象出力と項目説明を結び、根拠名は条件検分正答です。 B: 条件検分不足は名称や説明だけに寄り、判定名は条件検分不足です。 C: 条件検分流用は別カテゴリの確認であり、排除名は条件検分流用です。 D: 条件検分欠落は戻り値や記録番号に寄り、欠落名は条件検分欠落です。条件検分用語では S 機能を MVS オペレータコマンドで扱う確認対象とし、用語名は条件検分用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>S VLF Virtual Lookaside</strong></p><p>検証目的: 置換検査の操作コマンドについて、VLF (Virtual Lookaside Facility) を起動する。CSVLLA ・キャタログ・ RACF の各キャッシュの前提に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020064の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、置換検査の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS VLF Virtual Lookを指定し、OSKB020064の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S VLF Virtual Look
CASE OSKB020064
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S VLF Virtual Look
CASE OSKB020064
SOURCE z/OS MVS Operations
S VLF Virtual LookとOSKB020064が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020064を同じ出力で読み、置換検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020064
→ Enter を押す
［画面・出力］
IEE115I OSKB020064 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020064   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020064が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の S VLF Virtual Look と OSKB020064 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020064 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SEND


<section class="kb-item" id="c22-i0239"><h3>SEND &#x27;text&#x27;,CN=(*ALL)</h3><p class="kb-meta">分類: SEND ・ 難易度: 中級</p><p>SEND &#x27;text&#x27;,CN=(*ALL)は、MVS オペレータコマンドのSENDで確認する項目です。Sysplex 全コンソールに一斉送信する形式。停止予告など全員告知に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切追跡の*で SEND &#x27;text&#x27;,CN=(*ALL)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SEND &#x27;text&#x27;,CN=(*ALL)の出力を取らず区切追跡の*の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切追跡の*の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切追跡の*へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切追跡の*において選択記号 B を採用し、識別名は区切追跡です。区切追跡の*において SEND &#x27;text&#x27;,CN=(*ALL) は説明欄の「区切追跡の*に関係する定義値と表示行を照合する区切追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の*の証跡を読む担当者は、SEND &#x27;text&#x27;,CN=(*ALL)の属性行と IEE115I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の*は名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の*は対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の*は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の*は別カテゴリの確認を流用しており、SEND &#x27;text&#x27;,CN=(*ALL)の根拠にならないため区切追跡ではありません。区切追跡の*に出る SEND &#x27;text&#x27;,CN=(*ALL)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SEND &#x27;text&#x27;,CN=(*ALL)</strong></p><p>検証目的: 呼出照合の*について、SEND &#x27;text&#x27;,CN=(*ALL)は、MVS オペレータコマンドの SEND で確認する項目です。Sysplex 全コンソールに一斉送信する形式。停止予告など全員告知にに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030023の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、呼出照合の*の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSEND &#x27;text&#x27;,CN=(*Aを指定し、OSKB030023の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SEND &#x27;text&#x27;,CN=(*A
CASE OSKB030023
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SEND &#x27;text&#x27;,CN=(*A
CASE OSKB030023
SOURCE z/OS MVS Operations
SEND &#x27;text&#x27;,CN=(*AとOSKB030023が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030023を同じ出力で読み、呼出照合の*の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030023
→ Enter を押す
［画面・出力］
IEE115I OSKB030023 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030023   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030023が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の SEND &#x27;text&#x27;,CN=(*A と OSKB030023 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030023 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0240"><h3>SEND &#x27;text&#x27;,CN=name</h3><p class="kb-meta">分類: SEND ・ 難易度: 中級</p><p>SEND &#x27;text&#x27;,CN=nameは、MVS オペレータコマンドのSENDで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件追跡の操作コマンドに関係する SEND &#x27;text&#x27;,CN=nameの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. SEND &#x27;text&#x27;,CN=nameの名称と担当者名のみを残して条件追跡の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件追跡の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件追跡の操作コマンドにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡の操作コマンドにおいて SEND &#x27;text&#x27;,CN=name は説明欄の「SEND &#x27;text&#x27;,CN=nameの用途を操作コマンドの表示で確認する条件追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の操作コマンドに関連して、z/OS MVS Operationsでは SEND &#x27;text&#x27;,CN=nameの表示属性と IEE115I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の操作コマンドは別カテゴリの確認を流用しており、SEND &#x27;text&#x27;,CN=nameの根拠にならないため条件追跡ではありません。 D: 条件追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件追跡ではありません。条件追跡の操作コマンドで使う SEND &#x27;text&#x27;,CN=nameという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SEND &#x27;text&#x27;,CN=name</strong></p><p>検証目的: 展開照合の操作コマンドについて、SEND &#x27;text&#x27;,CN=nameは、MVS オペレータコマンドの SEND で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030022の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSEND &#x27;text&#x27;,CN=namを指定し、OSKB030022の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SEND &#x27;text&#x27;,CN=nam
CASE OSKB030022
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SEND &#x27;text&#x27;,CN=nam
CASE OSKB030022
SOURCE z/OS MVS Operations
SEND &#x27;text&#x27;,CN=namとOSKB030022が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030022を同じ出力で読み、展開照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030022
→ Enter を押す
［画面・出力］
IEE115I OSKB030022 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030022   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030022が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の SEND &#x27;text&#x27;,CN=nam と OSKB030022 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0241"><h3>SEND &#x27;text&#x27;,NOW</h3><p class="kb-meta">分類: SEND ・ 難易度: 中級</p><p>SEND &#x27;text&#x27;,NOWは、MVS オペレータコマンドのSENDで確認する項目です。即時表示モード。受信側で SAVE モードを設定しても無視して直ちに表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲追跡の操作コマンドで操作コマンドの運用確認を行います。SEND &#x27;text&#x27;,NOW の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲追跡の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. SEND &#x27;text&#x27;,NOW の属性行を読まず範囲追跡の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲追跡の操作コマンドにおいて選択記号 C を採用し、識別名は範囲追跡です。範囲追跡の操作コマンドにおいて SEND &#x27;text&#x27;,NOW は説明欄の「z/OS MVS Operationsで SEND &#x27;text&#x27;,NOW の扱いを記録する範囲追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲追跡です。範囲追跡の操作コマンドを受け取る担当者は、SEND &#x27;text&#x27;,NOW の表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲追跡です。不適切な選択肢を整理します。 A: 範囲追跡の操作コマンドは別カテゴリの確認を流用しており、SEND &#x27;text&#x27;,NOW の根拠にならないため範囲追跡ではありません。 B: 範囲追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲追跡ではありません。 C: 範囲追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので範囲追跡です。 D: 範囲追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲追跡ではありません。範囲追跡の操作コマンドが示す SEND &#x27;text&#x27;,NOW は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SEND &#x27;text&#x27;,NOW</strong></p><p>検証目的: 置換照合の操作コマンドについて、SEND &#x27;text&#x27;,NOW は、MVS オペレータコマンドの SEND で確認する項目です。即時表示モード。受信側で SAVE モードを設定しても無視して直ちに表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030024の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSEND &#x27;text&#x27;,NOWを指定し、OSKB030024の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SEND &#x27;text&#x27;,NOW
CASE OSKB030024
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SEND &#x27;text&#x27;,NOW
CASE OSKB030024
SOURCE z/OS MVS Operations
SEND &#x27;text&#x27;,NOWとOSKB030024が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030024を同じ出力で読み、置換照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030024
→ Enter を押す
［画面・出力］
IEE115I OSKB030024 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030024   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030024が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の SEND &#x27;text&#x27;,NOW と OSKB030024 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0242"><h3>SEND &#x27;text&#x27;,USER=userid</h3><p class="kb-meta">分類: SEND ・ 難易度: 中級</p><p>SEND &#x27;text&#x27;,USER=useridは、MVS オペレータコマンドのSENDで確認する項目です。TSO ユーザに即時メッセージを送る形式。受信ユーザ側で M / N コマンドの設定が必要な点に注意</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力追跡の操作コマンドに関する SEND &#x27;text&#x27;,USER=useridの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力追跡の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力追跡の操作コマンドの証跡として保存して根拠にする。</li><li>C. SEND &#x27;text&#x27;,USER=useridの変更点を出力本文から切り離して出力追跡の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力追跡の操作コマンドにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡の操作コマンドにおいて SEND &#x27;text&#x27;,USER=userid は説明欄の「SEND &#x27;text&#x27;,USER=useridの状態と出力メッセージを結び付ける出力追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の操作コマンドに関する記録は、SEND &#x27;text&#x27;,USER=useridの出力行と IEE115I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の操作コマンドは別カテゴリの確認を流用しており、SEND &#x27;text&#x27;,USER=useridの根拠にならないため出力追跡ではありません。 C: 出力追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の操作コマンドで記録する SEND &#x27;text&#x27;,USER=useridはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SEND &#x27;text&#x27;,USER=userid</strong></p><p>検証目的: 構文照合の操作コマンドについて、SEND &#x27;text&#x27;,USER=useridは、MVS オペレータコマンドの SEND で確認する項目です。TSO ユーザに即時メッセージを送る形式。受信ユーザ側で M /に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030021の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSEND &#x27;text&#x27;,USER=uを指定し、OSKB030021の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SEND &#x27;text&#x27;,USER=u
CASE OSKB030021
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SEND &#x27;text&#x27;,USER=u
CASE OSKB030021
SOURCE z/OS MVS Operations
SEND &#x27;text&#x27;,USER=uとOSKB030021が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030021を同じ出力で読み、構文照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030021
→ Enter を押す
［画面・出力］
IEE115I OSKB030021 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030021   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030021が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の SEND &#x27;text&#x27;,USER=u と OSKB030021 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030021 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET DAE


<section class="kb-item" id="c22-i0243"><h3>SET DAE=00 リセット</h3><p class="kb-meta">分類: SET DAE ・ 難易度: 中級</p><p>SET DAE=00 リセットは、MVS オペレータコマンドのSET DAEで確認する項目です。ADYSET00 にて DAE をデフォルト状態に戻す典型的な用法。テスト中の調整から本番値に戻す際に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力分離のリセットに関する SET DAE=00 リセットの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA の結果を残さず出力分離のリセットの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力分離のリセットの証跡として保存して根拠にする。</li><li>C. SET DAE=00 リセットの変更点を出力本文から切り離して出力分離のリセットの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、出力分離で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力分離正解では選択記号 D を採用し、正解名は出力分離正解です。出力分離根拠では SET DAE=00 リセット は「SET DAE=00 リセットの状態と出力メッセージを結び付ける出力分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は出力分離根拠です。出力分離保存では SET DAE=00 リセットの出力行と IEE457I を一緒に残し、保存名は出力分離保存です。選択肢ごとの違いを示します。 A: 出力分離欠落は戻り値や記録番号に寄り、欠落名は出力分離欠落です。 B: 出力分離流用は別カテゴリの確認であり、排除名は出力分離流用です。 C: 出力分離不足は名称や説明だけに寄り、判定名は出力分離不足です。 D: 出力分離正答は対象出力と項目説明を結び、根拠名は出力分離正答です。出力分離対象では SET DAE=00 リセットをz/OS MVS Operationsの確認記録に残し、対象名は出力分離対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切照合のリセットで SET DAE=00 リセットの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SET DAE=00 リセットの出力を取らず区切照合のリセットの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D OPDATA を省略して区切照合のリセットの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切照合のリセットへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切照合のリセットにおいて選択記号 B を採用し、識別名は区切照合です。区切照合のリセットにおいて SET DAE=00 リセット は説明欄の「区切照合のリセットに関係する定義値と表示行を照合する区切照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合のリセットの証跡を読む担当者は、SET DAE=00 リセットの属性行と IEE457I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合のリセットは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合のリセットは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合のリセットは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため区切照合ではありません。 D: 区切照合のリセットは別カテゴリの確認を流用しており、SET DAE=00 リセットの根拠にならないため区切照合ではありません。区切照合のリセットに出る SET DAE=00 リセットは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET DAE=00 リセット</strong></p><p>検証目的: 呼出照合のリセットについて、SET DAE=00 リセットは、MVS オペレータコマンドの SET DAE で確認する項目です。ADYSET00 にて DAE をデフォルト状態に戻す典型的な用法。テスト中に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020023の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、呼出照合のリセットの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET DAE=00 リセットを指定し、OSKB020023の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET DAE=00 リセット
CASE OSKB020023
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET DAE=00 リセット
CASE OSKB020023
SOURCE z/OS MVS Operations
SET DAE=00 リセットとOSKB020023が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020023を同じ出力で読み、呼出照合のリセットの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020023
→ Enter を押す
［画面・出力］
IEE457I OSKB020023 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020023   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020023が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET DAE=00 リセット と OSKB020023 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020023 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0244"><h3>SET DAE=xx 目的</h3><p class="kb-meta">分類: SET DAE ・ 難易度: 初級</p><p>ADYSETxx PARMLIB メンバを動的に再活性化し、重複ダンプ抑止 (DAE) の規則を変更する。再 IPL なしで運用変更可能</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書分離の目的で操作コマンドの運用確認を行います。SET DAE=xx 目的の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書分離の目的を確認した扱いにする。</li><li>B. IEE457I の有無を確認せず上書分離の目的を正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、上書分離の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. SET DAE=xx 目的の属性行を読まず上書分離の目的の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では SET DAE=xx 目的 は「z/OS MVS Operationsで SET DAE=xx 目的の扱いを記録する上書分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では SET DAE=xx 目的の表示結果と IEE457I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明だけに寄り、判定名は上書分離不足です。上書分離資料では SET DAE=xx 目的の使い方を出典欄から追跡し、資料名は上書分離資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件照合の目的に関係する SET DAE=xx 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. SET DAE=xx 目的の名称と担当者名のみを残して条件照合の目的の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件照合の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず条件照合の目的の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 条件照合の目的において選択記号 A を採用し、識別名は条件照合です。条件照合の目的において SET DAE=xx 目的 は説明欄の「SET DAE=xx 目的の用途を操作コマンドの表示で確認する条件照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の目的に関連して、z/OS MVS Operationsでは SET DAE=xx 目的の表示属性と IEE457I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の目的は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の目的は別カテゴリの確認を流用しており、SET DAE=xx 目的の根拠にならないため条件照合ではありません。 D: 条件照合の目的は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため条件照合ではありません。条件照合の目的で使う SET DAE=xx 目的という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET DAE=xx 目的</strong></p><p>検証目的: 展開照合の目的について、ADYSETxx PARMLIB メンバを動的に再活性化し、重複ダンプ抑止 (DAE) の規則を変更する。再 IPL なしで運用変更可能に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020022の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、展開照合の目的の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET DAE=xx 目的を指定し、OSKB020022の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET DAE=xx 目的
CASE OSKB020022
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET DAE=xx 目的
CASE OSKB020022
SOURCE z/OS MVS Operations
SET DAE=xx 目的とOSKB020022が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020022を同じ出力で読み、展開照合の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020022
→ Enter を押す
［画面・出力］
IEE457I OSKB020022 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020022   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020022が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET DAE=xx 目的 と OSKB020022 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET DUMP


<section class="kb-item" id="c22-i0245"><h3>SET DUMP=NODUMP 緊急停止</h3><p class="kb-meta">分類: SET DUMP ・ 難易度: 中級</p><p>SET DUMP=NODUMP 緊急停止は、MVS オペレータコマンドのSET DUMPで確認する項目です。ダンプ生成を一時的に止める用途。容量逼迫時に応急処置として使うが、原因分析資料を失うリスクを併記</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切分離の緊急停止で SET 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SET 属性の出力を取らず区切分離の緊急停止の説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて区切分離の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D OPDATA を省略して区切分離の緊急停止の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切分離の緊急停止へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切分離正解では選択記号 B を採用し、正解名は区切分離正解です。区切分離根拠では SET 属性 は「区切分離の緊急停止に関係する定義値と表示行を照合する区切分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は区切分離根拠です。区切分離追跡では SET 属性の属性行と IEE457I を合わせ、追跡名は区切分離追跡です。誤答側の問題点を分けます。 A: 区切分離不足は名称や説明だけに寄り、判定名は区切分離不足です。 B: 区切分離正答は対象出力と項目説明を結び、根拠名は区切分離正答です。 C: 区切分離欠落は戻り値や記録番号に寄り、欠落名は区切分離欠落です。 D: 区切分離流用は別カテゴリの確認であり、排除名は区切分離流用です。区切分離初出では SET 属性を MVS オペレータコマンドの運用手順で確認し、初出名は区切分離初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 優先照合の緊急停止に関する SET DUMP=NODUMP 緊急停止の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA の結果を残さず優先照合の緊急停止の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先照合の緊急停止の証跡として保存して根拠にする。</li><li>C. SET DUMP=NODUMP 緊急停止の変更点を出力本文から切り離して優先照合の緊急停止の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先照合の緊急停止において選択記号 D を採用し、識別名は優先照合です。優先照合の緊急停止において SET DUMP=NODUMP 緊急停止 は説明欄の「SET DUMP=NODUMP 緊急停止の状態と出力メッセージを結び付ける優先照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合の緊急停止に関する記録は、SET DUMP=NODUMP 緊急停止の出力行と IEE457I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合の緊急停止は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため優先照合ではありません。 B: 優先照合の緊急停止は別カテゴリの確認を流用しており、SET DUMP=NODUMP 緊急停止の根拠にならないため優先照合ではありません。 C: 優先照合の緊急停止は名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合の緊急停止は対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合の緊急停止で記録する SET DUMP=NODUMP 緊急停止はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET DUMP=NODUMP 緊急停止</strong></p><p>検証目的: 終端照合の緊急停止について、SET DUMP=NODUMP 緊急停止は、MVS オペレータコマンドの SET DUMP で確認する項目です。ダンプ生成を一時的に止める用途。容量逼迫時に応急処置として使うがに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020025の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、終端照合の緊急停止の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET DUMP=NODUMP 緊急を指定し、OSKB020025の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET DUMP=NODUMP 緊急
CASE OSKB020025
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET DUMP=NODUMP 緊急
CASE OSKB020025
SOURCE z/OS MVS Operations
SET DUMP=NODUMP 緊急とOSKB020025が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020025を同じ出力で読み、終端照合の緊急停止の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020025
→ Enter を押す
［画面・出力］
IEE457I OSKB020025 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020025   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020025が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET DUMP=NODUMP 緊急 と OSKB020025 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020025 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0246"><h3>SET DUMP=xx 目的</h3><p class="kb-meta">分類: SET DUMP ・ 難易度: 初級</p><p>SET DUMP=xx 目的は、DIAGxx などダンプ関連 PARMLIB メンバを動的活性化し、SVC ダンプの SDATA 既定や CHNGDUMP オプションを反映する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件分離の目的に関係する SET DUMP=xx 目的の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、条件分離の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. SET DUMP=xx 目的の名称と担当者名だけを残して条件分離の目的の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件分離の目的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず条件分離の目的の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 条件分離正解では選択記号 A を採用し、正解名は条件分離正解です。条件分離根拠では SET DUMP=xx 目的 は「SET DUMP=xx 目的の用途を操作コマンドの表示で確認する条件分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は条件分離根拠です。条件分離背景ではz/OS MVS Operationsの SET DUMP=xx 目的と IEE457I を同じ証跡に残し、背景名は条件分離背景です。他の選択肢を確認します。 A: 条件分離正答は対象出力と項目説明を結び、根拠名は条件分離正答です。 B: 条件分離不足は名称や説明だけに寄り、判定名は条件分離不足です。 C: 条件分離流用は別カテゴリの確認であり、排除名は条件分離流用です。 D: 条件分離欠落は戻り値や記録番号に寄り、欠落名は条件分離欠落です。条件分離用語では SET DUMP=xx 目的を MVS オペレータコマンドで扱う確認対象とし、用語名は条件分離用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 範囲照合の目的で操作コマンドの運用確認を行います。SET DUMP=xx 目的の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲照合の目的を確認した扱いにする。</li><li>B. IEE457I の有無を確認せず範囲照合の目的を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. SET DUMP=xx 目的の属性行を読まず範囲照合の目的の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 初級</p><p><strong>解説:</strong> 範囲照合の目的において選択記号 C を採用し、識別名は範囲照合です。範囲照合の目的において SET DUMP=xx 目的 は説明欄の「z/OS MVS Operationsで SET DUMP=xx 目的の扱いを記録する範囲照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合の目的を受け取る担当者は、SET DUMP=xx 目的の表示結果と IEE457I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合の目的は別カテゴリの確認を流用しており、SET DUMP=xx 目的の根拠にならないため範囲照合ではありません。 B: 範囲照合の目的は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合の目的は対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合の目的は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合の目的が示す SET DUMP=xx 目的は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET DUMP=xx 目的</strong></p><p>検証目的: 置換照合の目的について、SET DUMP=xx 目的は、DIAGxx などダンプ関連 PARMLIB メンバを動的活性化し、SVC ダンプの SDATA 既定や CHNGDUMP オプションを反映に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020024の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、置換照合の目的の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET DUMP=xx 目的を指定し、OSKB020024の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET DUMP=xx 目的
CASE OSKB020024
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET DUMP=xx 目的
CASE OSKB020024
SOURCE z/OS MVS Operations
SET DUMP=xx 目的とOSKB020024が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020024を同じ出力で読み、置換照合の目的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020024
→ Enter を押す
［画面・出力］
IEE457I OSKB020024 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020024   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020024が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET DUMP=xx 目的 と OSKB020024 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET IEASYS


<section class="kb-item" id="c22-i0247"><h3>SET IEASYS=xx</h3><p class="kb-meta">分類: SET IEASYS ・ 難易度: 中級</p><p>IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多い</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲分離の操作コマンドで操作コマンドの運用確認を行います。SET IEASYS=xxの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲分離の操作コマンドを確認した扱いにする。</li><li>B. IEE457I の有無を確認せず範囲分離の操作コマンドを正常終了として記録する。</li><li>C. IEE457I を含む表示を保存し、説明欄との差分を範囲分離で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. SET IEASYS=xxの属性行を読まず範囲分離の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲分離正解では選択記号 C を採用し、正解名は範囲分離正解です。範囲分離根拠では SET IEASYS=xx は「z/OS MVS Operationsで SET IEASYS=xxの扱いを記録する範囲分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は範囲分離根拠です。範囲分離受渡では SET IEASYS=xxの表示結果と IEE457I を同じ確認単位にし、受渡名は範囲分離受渡です。不適切な選択肢を整理します。 A: 範囲分離流用は別カテゴリの確認であり、排除名は範囲分離流用です。 B: 範囲分離欠落は戻り値や記録番号に寄り、欠落名は範囲分離欠落です。 C: 範囲分離正答は対象出力と項目説明を結び、根拠名は範囲分離正答です。 D: 範囲分離不足は名称や説明だけに寄り、判定名は範囲分離不足です。範囲分離資料では SET IEASYS=xxの使い方を出典欄から追跡し、資料名は範囲分離資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 記録照合の操作コマンドに関係する SET IEASYS=xxの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、記録照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. SET IEASYS=xxの名称と担当者名のみを残して記録照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で記録照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず記録照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録照合の操作コマンドにおいて選択記号 A を採用し、識別名は記録照合です。記録照合の操作コマンドにおいて SET IEASYS=xx は説明欄の「IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多い」と D OPDATA または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合の操作コマンドに関連して、z/OS MVS Operationsでは SET IEASYS=xxの表示属性と IEE457I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合の操作コマンドは別カテゴリの確認を流用しており、SET IEASYS=xxの根拠にならないため記録照合ではありません。 D: 記録照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため記録照合ではありません。記録照合の操作コマンドで使う SET IEASYS=xxという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET IEASYS=xx</strong></p><p>検証目的: 探索照合の操作コマンドについて、IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多いに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040026の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、探索照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET IEASYS=xxを指定し、OSKB040026の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET IEASYS=xx
CASE OSKB040026
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET IEASYS=xx
CASE OSKB040026
SOURCE z/OS MVS Operations
SET IEASYS=xxとOSKB040026が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040026を同じ出力で読み、探索照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB040026
→ Enter を押す
［画面・出力］
IEE457I OSKB040026 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040026   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB040026が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET IEASYS=xx と OSKB040026 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB040026 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>SET IEASYS=xx</strong></p><p>検証目的: 探索照合の操作コマンドについて、IEASYSxx 自体を動的にチェーンに加えて起動値を再評価する。実際の効果はパラメータごとに対応 SET コマンドが必要な点が多いに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020026の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、探索照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET IEASYS=xxを指定し、OSKB020026の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET IEASYS=xx
CASE OSKB020026
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET IEASYS=xx
CASE OSKB020026
SOURCE z/OS MVS Operations
SET IEASYS=xxとOSKB020026が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020026を同じ出力で読み、探索照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020026
→ Enter を押す
［画面・出力］
IEE457I OSKB020026 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020026   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020026が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET IEASYS=xx と OSKB020026 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020026 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET MPF


<section class="kb-item" id="c22-i0248"><h3>SET MPF=(xx,yy) 連結</h3><p class="kb-meta">分類: SET MPF ・ 難易度: 中級</p><p>SET MPF=(xx,yy) 連結は、MVS オペレータコマンドのSET MPFで確認する項目です。複数 MPF メンバを連結指定。基本規則 + サイト追加分という二重構造で運用する典型形</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録分離の連結に関係する SET MPF=(xx 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、記録分離の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. SET MPF=(xx 命令の名称と担当者名だけを残して記録分離の連結の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録分離の連結を確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず記録分離の連結の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録分離正解では選択記号 A を採用し、正解名は記録分離正解です。記録分離根拠では SET MPF=(xx 命令 は「SET MPF=(xx 命令の用途を操作コマンドの表示で確認する記録分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は記録分離根拠です。記録分離背景ではz/OS MVS Operationsの SET MPF=(xx 命令と IEE457I を同じ証跡に残し、背景名は記録分離背景です。他の選択肢を確認します。 A: 記録分離正答は対象出力と項目説明を結び、根拠名は記録分離正答です。 B: 記録分離不足は名称や説明だけに寄り、判定名は記録分離不足です。 C: 記録分離流用は別カテゴリの確認であり、排除名は記録分離流用です。 D: 記録分離欠落は戻り値や記録番号に寄り、欠落名は記録分離欠落です。記録分離用語では SET MPF=(xx 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は記録分離用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 順序照合の連結で操作コマンドの運用確認を行います。SET MPF=(xx,yy) 連結の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序照合の連結を確認した扱いにする。</li><li>B. IEE457I の有無を確認せず順序照合の連結を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、順序照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. SET MPF=(xx,yy) 連結の属性行を読まず順序照合の連結の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序照合の連結において選択記号 C を採用し、識別名は順序照合です。順序照合の連結において SET MPF=(xx,yy) 連結 は説明欄の「z/OS MVS Operationsで SET MPF=(xx,yy) 連結の扱いを記録する順序照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合の連結を受け取る担当者は、SET MPF=(xx,yy) 連結の表示結果と IEE457I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合の連結は別カテゴリの確認を流用しており、SET MPF=(xx,yy) 連結の根拠にならないため順序照合ではありません。 B: 順序照合の連結は戻り値や記録番号に寄り、IEE457I や属性表示を落とすため順序照合ではありません。 C: 順序照合の連結は対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合の連結は名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合の連結が示す SET MPF=(xx,yy) 連結は出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET MPF=(xx,yy) 連結</strong></p><p>検証目的: 出力照合の連結について、SET MPF=(xx,yy) 連結は、MVS オペレータコマンドの SET MPF で確認する項目です。複数 MPF メンバを連結指定。基本規則 + サイト追加分という二重構に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020028の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、出力照合の連結の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET MPF=(xx,yy) 連結を指定し、OSKB020028の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET MPF=(xx,yy) 連結
CASE OSKB020028
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET MPF=(xx,yy) 連結
CASE OSKB020028
SOURCE z/OS MVS Operations
SET MPF=(xx,yy) 連結とOSKB020028が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020028を同じ出力で読み、出力照合の連結の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020028
→ Enter を押す
［画面・出力］
IEE457I OSKB020028 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020028   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020028が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET MPF=(xx,yy) 連結 と OSKB020028 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020028 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0249"><h3>SET MPF=xx</h3><p class="kb-meta">分類: SET MPF ・ 難易度: 中級</p><p>SET MPF=xxは、MVS オペレータコマンドのSET MPFで用いるMPFLSTxx を動的活性化し、抑止メッセージ・自動化対象・色付け規則を更新する。最頻出 SET 系の一つ。SET MPFでは、指定値と対象資源、実行時の出力を突き合わせて確認する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先分離の操作コマンドに関する SET MPF=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA の結果を残さず優先分離の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先分離の操作コマンドの証跡として保存して根拠にする。</li><li>C. SET MPF=xxの変更点を出力本文から切り離して優先分離の操作コマンドの承認欄だけ残す。</li><li>D. D OPDATA の結果から対象行を抜き出し、優先分離の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先分離正解では選択記号 D を採用し、正解名は優先分離正解です。優先分離根拠では SET MPF=xx は「SET MPF=xxの状態と出力メッセージを結び付ける優先分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は優先分離根拠です。優先分離保存では SET MPF=xxの出力行と IEE457I を一緒に残し、保存名は優先分離保存です。選択肢ごとの違いを示します。 A: 優先分離欠落は戻り値や記録番号に寄り、欠落名は優先分離欠落です。 B: 優先分離流用は別カテゴリの確認であり、排除名は優先分離流用です。 C: 優先分離不足は名称や説明だけに寄り、判定名は優先分離不足です。 D: 優先分離正答は対象出力と項目説明を結び、根拠名は優先分離正答です。優先分離対象では SET MPF=xxをz/OS MVS Operationsの確認記録に残し、対象名は優先分離対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 比較照合の操作コマンドで SET MPF=xxの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SET MPF=xxの出力を取らず比較照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、比較照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D OPDATA を省略して比較照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較照合の操作コマンドにおいて選択記号 B を採用し、識別名は比較照合です。比較照合の操作コマンドにおいて SET MPF=xx は説明欄の「比較照合の操作コマンドに関係する定義値と表示行を照合する比較照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合の操作コマンドの証跡を読む担当者は、SET MPF=xxの属性行と IEE457I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため比較照合ではありません。 D: 比較照合の操作コマンドは別カテゴリの確認を流用しており、SET MPF=xxの根拠にならないため比較照合ではありません。比較照合の操作コマンドに出る SET MPF=xxは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET MPF=xx</strong></p><p>検証目的: 上書照合の操作コマンドについて、SET MPF=xxは、MVS オペレータコマンドの SET MPF で用いる MPFLSTxx を動的活性化し、抑止メッセージ・自動化対象・色付け規則を更新する。最頻出 SETに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020027の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、上書照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET MPF=xxを指定し、OSKB020027の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET MPF=xx
CASE OSKB020027
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET MPF=xx
CASE OSKB020027
SOURCE z/OS MVS Operations
SET MPF=xxとOSKB020027が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020027を同じ出力で読み、上書照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020027
→ Enter を押す
［画面・出力］
IEE457I OSKB020027 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020027   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020027が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET MPF=xx と OSKB020027 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020027 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET OMVS


<section class="kb-item" id="c22-i0250"><h3>SET OMVS RESET=xx</h3><p class="kb-meta">分類: SET OMVS ・ 難易度: 中級</p><p>SET OMVS RESET=xxは、MVS オペレータコマンドのSET OMVSで確認する項目です。現行設定を破棄して指定 BPXPRMxx 値で完全置換する形式。マウント情報には影響しない注意点を併記</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序分離の操作コマンドで操作コマンドの運用確認を行います。SET 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序分離の操作コマンドを確認した扱いにする。</li><li>B. IEE457I の有無を確認せず順序分離の操作コマンドを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE457I を読み、順序分離の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. SET 属性の属性行を読まず順序分離の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序分離正解では選択記号 C を採用し、正解名は順序分離正解です。順序分離根拠では SET 属性 は「z/OS MVS Operationsで SET 属性の扱いを記録する順序分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は順序分離根拠です。順序分離受渡では SET 属性の表示結果と IEE457I を同じ確認単位にし、受渡名は順序分離受渡です。不適切な選択肢を整理します。 A: 順序分離流用は別カテゴリの確認であり、排除名は順序分離流用です。 B: 順序分離欠落は戻り値や記録番号に寄り、欠落名は順序分離欠落です。 C: 順序分離正答は対象出力と項目説明を結び、根拠名は順序分離正答です。 D: 順序分離不足は名称や説明だけに寄り、判定名は順序分離不足です。順序分離資料では SET 属性の使い方を出典欄から追跡し、資料名は順序分離資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 警告照合の操作コマンドに関係する SET OMVS RESET=xxの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、警告照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. SET OMVS RESET=xxの名称と担当者名のみを残して警告照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で警告照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず警告照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告照合の操作コマンドにおいて選択記号 A を採用し、識別名は警告照合です。警告照合の操作コマンドにおいて SET OMVS RESET=xx は説明欄の「SET OMVS RESET=xxの用途を操作コマンドの表示で確認する警告照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の操作コマンドに関連して、z/OS MVS Operationsでは SET OMVS RESET=xxの表示属性と IEE457I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の操作コマンドは別カテゴリの確認を流用しており、SET OMVS RESET=xxの根拠にならないため警告照合ではありません。 D: 警告照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため警告照合ではありません。警告照合の操作コマンドで使う SET OMVS RESET=xxという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET OMVS RESET=xx</strong></p><p>検証目的: 区切照合の操作コマンドについて、SET OMVS RESET=xxは、MVS オペレータコマンドの SET OMVS で確認する項目です。現行設定を破棄して指定 BPXPRMxx 値で完全置換する形式。マウンに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020030の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、区切照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET OMVS RESET=xxを指定し、OSKB020030の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET OMVS RESET=xx
CASE OSKB020030
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET OMVS RESET=xx
CASE OSKB020030
SOURCE z/OS MVS Operations
SET OMVS RESET=xxとOSKB020030が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020030を同じ出力で読み、区切照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020030
→ Enter を押す
［画面・出力］
IEE457I OSKB020030 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020030   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020030が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET OMVS RESET=xx と OSKB020030 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0251"><h3>SET OMVS=xx</h3><p class="kb-meta">分類: SET OMVS ・ 難易度: 中級</p><p>SET OMVS=xxは、BPXPRMxx を動的活性化し、MAXPROCSYS など多くの z/OS UNIX 上限値を再 IPL なしで変更する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較分離の操作コマンドで SET OMVS=xxの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SET OMVS=xxの出力を取らず比較分離の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて比較分離の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D OPDATA を省略して比較分離の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較分離の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較分離正解では選択記号 B を採用し、正解名は比較分離正解です。比較分離根拠では SET OMVS=xx は「比較分離の操作コマンドに関係する定義値と表示行を照合する比較分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は比較分離根拠です。比較分離追跡では SET OMVS=xxの属性行と IEE457I を合わせ、追跡名は比較分離追跡です。誤答側の問題点を分けます。 A: 比較分離不足は名称や説明だけに寄り、判定名は比較分離不足です。 B: 比較分離正答は対象出力と項目説明を結び、根拠名は比較分離正答です。 C: 比較分離欠落は戻り値や記録番号に寄り、欠落名は比較分離欠落です。 D: 比較分離流用は別カテゴリの確認であり、排除名は比較分離流用です。比較分離初出では SET OMVS=xxを MVS オペレータコマンドの運用手順で確認し、初出名は比較分離初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 値域照合の操作コマンドに関する SET OMVS=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA の結果を残さず値域照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. SET OMVS=xxの変更点を出力本文から切り離して値域照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、値域照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域照合の操作コマンドにおいて選択記号 D を採用し、識別名は値域照合です。値域照合の操作コマンドにおいて SET OMVS=xx は説明欄の「SET OMVS=xxの状態と出力メッセージを結び付ける値域照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の操作コマンドに関する記録は、SET OMVS=xxの出力行と IEE457I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため値域照合ではありません。 B: 値域照合の操作コマンドは別カテゴリの確認を流用しており、SET OMVS=xxの根拠にならないため値域照合ではありません。 C: 値域照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の操作コマンドで記録する SET OMVS=xxはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET OMVS=xx</strong></p><p>検証目的: 条件照合の操作コマンドについて、SET OMVS=xxは、BPXPRMxx を動的活性化し、MAXPROCSYS など多くの z/OS UNIX 上限値を再 IPL なしで変更するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020029の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、条件照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET OMVS=xxを指定し、OSKB020029の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET OMVS=xx
CASE OSKB020029
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET OMVS=xx
CASE OSKB020029
SOURCE z/OS MVS Operations
SET OMVS=xxとOSKB020029が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020029を同じ出力で読み、条件照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020029
→ Enter を押す
［画面・出力］
IEE457I OSKB020029 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020029   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020029が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET OMVS=xx と OSKB020029 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020029 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET PFK


<section class="kb-item" id="c22-i0252"><h3>SET PFK=xx</h3><p class="kb-meta">分類: SET PFK ・ 難易度: 中級</p><p>SET PFK=xxは、MVS オペレータコマンドのSET PFKで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域分離の操作コマンドに関する SET PFK=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA の結果を残さず値域分離の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域分離の操作コマンドの証跡として保存して根拠にする。</li><li>C. SET PFK=xxの変更点を出力本文から切り離して値域分離の操作コマンドの承認欄だけ残す。</li><li>D. D OPDATA で得た表示本文を使い、値域分離の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域分離正解では選択記号 D を採用し、正解名は値域分離正解です。値域分離根拠では SET PFK=xx は「SET PFK=xxの状態と出力メッセージを結び付ける値域分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は値域分離根拠です。値域分離保存では SET PFK=xxの出力行と IEE457I を一緒に残し、保存名は値域分離保存です。選択肢ごとの違いを示します。 A: 値域分離欠落は戻り値や記録番号に寄り、欠落名は値域分離欠落です。 B: 値域分離流用は別カテゴリの確認であり、排除名は値域分離流用です。 C: 値域分離不足は名称や説明だけに寄り、判定名は値域分離不足です。 D: 値域分離正答は対象出力と項目説明を結び、根拠名は値域分離正答です。値域分離対象では SET PFK=xxをz/OS MVS Operationsの確認記録に残し、対象名は値域分離対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 復旧照合の操作コマンドで SET PFK=xxの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SET PFK=xxの出力を取らず復旧照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、復旧照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D OPDATA を省略して復旧照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧照合の操作コマンドにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合の操作コマンドにおいて SET PFK=xx は説明欄の「復旧照合の操作コマンドに関係する定義値と表示行を照合する復旧照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の操作コマンドの証跡を読む担当者は、SET PFK=xxの属性行と IEE457I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の操作コマンドは別カテゴリの確認を流用しており、SET PFK=xxの根拠にならないため復旧照合ではありません。復旧照合の操作コマンドに出る SET PFK=xxは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET PFK=xx</strong></p><p>検証目的: 範囲照合の操作コマンドについて、SET PFK=xxは、MVS オペレータコマンドの SET PFK で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認しに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020031の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、範囲照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET PFK=xxを指定し、OSKB020031の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET PFK=xx
CASE OSKB020031
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET PFK=xx
CASE OSKB020031
SOURCE z/OS MVS Operations
SET PFK=xxとOSKB020031が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020031を同じ出力で読み、範囲照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020031
→ Enter を押す
［画面・出力］
IEE457I OSKB020031 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020031   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020031が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET PFK=xx と OSKB020031 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020031 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET PROG


<section class="kb-item" id="c22-i0253"><h3>SET PROG=xx</h3><p class="kb-meta">分類: SET PROG ・ 難易度: 中級</p><p>SET PROG=xxは、PROGxx を動的活性化し、APF / LNKLST / LPA / EXIT 一括変更を再 IPL なしで反映する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告分離の操作コマンドに関係する SET PROG=xxの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、警告分離として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. SET PROG=xxの名称と担当者名だけを残して警告分離の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告分離の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず警告分離の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告分離正解では選択記号 A を採用し、正解名は警告分離正解です。警告分離根拠では SET PROG=xx は「SET PROG=xxの用途を操作コマンドの表示で確認する警告分離項目」と D OPDATA または該当パネルの出力を照合し、根拠名は警告分離根拠です。警告分離背景ではz/OS MVS Operationsの SET PROG=xxと IEE457I を同じ証跡に残し、背景名は警告分離背景です。他の選択肢を確認します。 A: 警告分離正答は対象出力と項目説明を結び、根拠名は警告分離正答です。 B: 警告分離不足は名称や説明だけに寄り、判定名は警告分離不足です。 C: 警告分離流用は別カテゴリの確認であり、排除名は警告分離流用です。 D: 警告分離欠落は戻り値や記録番号に寄り、欠落名は警告分離欠落です。警告分離用語では SET PROG=xxを MVS オペレータコマンドで扱う確認対象とし、用語名は警告分離用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 監査照合の操作コマンドで操作コマンドの運用確認を行います。SET PROG=xxの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査照合の操作コマンドを確認した扱いにする。</li><li>B. IEE457I の有無を確認せず監査照合の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、監査照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. SET PROG=xxの属性行を読まず監査照合の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査照合の操作コマンドにおいて選択記号 C を採用し、識別名は監査照合です。監査照合の操作コマンドにおいて SET PROG=xx は説明欄の「z/OS MVS Operationsで SET PROG=xxの扱いを記録する監査照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の操作コマンドを受け取る担当者は、SET PROG=xxの表示結果と IEE457I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の操作コマンドは別カテゴリの確認を流用しており、SET PROG=xxの根拠にならないため監査照合ではありません。 B: 監査照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため監査照合ではありません。 C: 監査照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の操作コマンドが示す SET PROG=xxは出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET PROG=xx</strong></p><p>検証目的: 上書照合の操作コマンドについて、SET PROG=xxは、PROGxx を動的活性化し、APF / LNKLST / LPA / EXIT 一括変更を再 IPL なしで反映するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040027の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、上書照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET PROG=xxを指定し、OSKB040027の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET PROG=xx
CASE OSKB040027
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET PROG=xx
CASE OSKB040027
SOURCE z/OS MVS Operations
SET PROG=xxとOSKB040027が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040027を同じ出力で読み、上書照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB040027
→ Enter を押す
［画面・出力］
IEE457I OSKB040027 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040027   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB040027が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET PROG=xx と OSKB040027 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB040027 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>SET PROG=xx</strong></p><p>検証目的: 優先照合の操作コマンドについて、SET PROG=xxは、PROGxx を動的活性化し、APF / LNKLST / LPA / EXIT 一括変更を再 IPL なしで反映するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020032の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、優先照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET PROG=xxを指定し、OSKB020032の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET PROG=xx
CASE OSKB020032
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET PROG=xx
CASE OSKB020032
SOURCE z/OS MVS Operations
SET PROG=xxとOSKB020032が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020032を同じ出力で読み、優先照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020032
→ Enter を押す
［画面・出力］
IEE457I OSKB020032 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020032   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020032が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET PROG=xx と OSKB020032 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020032 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0254"><h3>SETPROG APF,ADD</h3><p class="kb-meta">分類: SET PROG ・ 難易度: 中級</p><p>SETPROG APF,ADDは、MVS オペレータコマンドのSET PROGで確認する項目です。個別データセットを動的に APF 許可リストへ追加するサブコマンド。緊急のソフトウェア導入時に多用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧分離の操作コマンドで SETPROG APF,ADD の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SETPROG APF,ADD の出力を取らず復旧分離の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、復旧分離の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧分離の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧分離の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧分離正解では選択記号 B を採用し、正解名は復旧分離正解です。復旧分離根拠では SETPROG APF,ADD は「復旧分離の操作コマンドに関係する定義値と表示行を照合する復旧分離項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧分離根拠です。復旧分離追跡では SETPROG APF,ADD の属性行と IEE115I を合わせ、追跡名は復旧分離追跡です。誤答側の問題点を分けます。 A: 復旧分離不足は名称や説明だけに寄り、判定名は復旧分離不足です。 B: 復旧分離正答は対象出力と項目説明を結び、根拠名は復旧分離正答です。 C: 復旧分離欠落は戻り値や記録番号に寄り、欠落名は復旧分離欠落です。 D: 復旧分離流用は別カテゴリの確認であり、排除名は復旧分離流用です。復旧分離初出では SETPROG APF,ADD を MVS オペレータコマンドの運用手順で確認し、初出名は復旧分離初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 変更照合の操作コマンドに関する SETPROG APF,ADD の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. SETPROG APF,ADD の変更点を出力本文から切り離して変更照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、変更照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更照合の操作コマンドにおいて選択記号 D を採用し、識別名は変更照合です。変更照合の操作コマンドにおいて SETPROG APF,ADD は説明欄の「SETPROG APF,ADD の状態と出力メッセージを結び付ける変更照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合の操作コマンドに関する記録は、SETPROG APF,ADD の出力行と IEE115I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更照合ではありません。 B: 変更照合の操作コマンドは別カテゴリの確認を流用しており、SETPROG APF,ADD の根拠にならないため変更照合ではありません。 C: 変更照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合の操作コマンドで記録する SETPROG APF,ADD はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SETPROG APF,ADD</strong></p><p>検証目的: 記録照合の操作コマンドについて、SETPROG APF,ADD は、MVS オペレータコマンドの SET PROG で確認する項目です。個別データセットを動的に APF 許可リストへ追加するサブコマンド。緊急のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020033の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG APF,ADDを指定し、OSKB020033の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SETPROG APF,ADD
CASE OSKB020033
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SETPROG APF,ADD
CASE OSKB020033
SOURCE z/OS MVS Operations
SETPROG APF,ADDとOSKB020033が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020033を同じ出力で読み、記録照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020033
→ Enter を押す
［画面・出力］
IEE115I OSKB020033 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020033   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020033が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の SETPROG APF,ADD と OSKB020033 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020033 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0255"><h3>SETPROG EXIT,ADD</h3><p class="kb-meta">分類: SET PROG ・ 難易度: 上級</p><p>SETPROG EXIT,ADDは、MVS オペレータコマンドのSET PROGで確認する項目です。動的出口にルーチンを動的に登録する。OS の振る舞いを再 IPL なしで拡張・差替する手段</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文読解の操作コマンドに関係する SETPROG EXIT 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、構文読解の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. SETPROG EXIT 命令の名称と担当者名だけを残して構文読解の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文読解の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文読解の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文読解正解では選択記号 A を採用し、正解名は構文読解正解です。構文読解根拠では SETPROG EXIT 命令 は「SETPROG EXIT 命令の用途を操作コマンドの表示で確認する構文読解項目」と D A,L または該当パネルの出力を照合し、根拠名は構文読解根拠です。構文読解背景ではz/OS MVS Operationsの SETPROG EXIT 命令と IEE115I を同じ証跡に残し、背景名は構文読解背景です。他の選択肢を確認します。 A: 構文読解正答は対象出力と項目説明を結び、根拠名は構文読解正答です。 B: 構文読解不足は名称や説明だけに寄り、判定名は構文読解不足です。 C: 構文読解流用は別カテゴリの確認であり、排除名は構文読解流用です。 D: 構文読解欠落は戻り値や記録番号に寄り、欠落名は構文読解欠落です。構文読解用語では SETPROG EXIT 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は構文読解用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出追跡の操作コマンドで操作コマンドの運用確認を行います。SETPROG EXIT,ADD の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出追跡の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出追跡の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. SETPROG EXIT,ADD の属性行を読まず呼出追跡の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出追跡の操作コマンドにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡の操作コマンドにおいて SETPROG EXIT,ADD は説明欄の「z/OS MVS Operationsで SETPROG EXIT,ADD の扱いを記録する呼出追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡の操作コマンドを受け取る担当者は、SETPROG EXIT,ADD の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡の操作コマンドは別カテゴリの確認を流用しており、SETPROG EXIT,ADD の根拠にならないため呼出追跡ではありません。 B: 呼出追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡の操作コマンドが示す SETPROG EXIT,ADD は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SETPROG EXIT,ADD</strong></p><p>検証目的: 値域照合の操作コマンドについて、SETPROG EXIT,ADD は、MVS オペレータコマンドの SET PROG で確認する項目です。動的出口にルーチンを動的に登録する。OS の振る舞いを再 IPL なしでに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020036の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG EXIT,ADDを指定し、OSKB020036の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SETPROG EXIT,ADD
CASE OSKB020036
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SETPROG EXIT,ADD
CASE OSKB020036
SOURCE z/OS MVS Operations
SETPROG EXIT,ADDとOSKB020036が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020036を同じ出力で読み、値域照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020036
→ Enter を押す
［画面・出力］
IEE115I OSKB020036 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020036   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020036が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の SETPROG EXIT,ADD と OSKB020036 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020036 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0256"><h3>SETPROG LNKLST,DEFINE</h3><p class="kb-meta">分類: SET PROG ・ 難易度: 中級</p><p>SETPROG LNKLST,DEFINEは、新しい LNKLST セットを定義 / ADD / ACTIVATE の動的入替手順を構成するサブコマンド。新しい LNKLST セットを定義 → ADD → ACTIVATE の動的入替手順を構成するサブコマンド</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査分離の操作コマンドで操作コマンドの運用確認を行います。SETPROG LNKLST 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査分離の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査分離の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、監査分離の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. SETPROG LNKLST 命令の属性行を読まず監査分離の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査分離正解では選択記号 C を採用し、正解名は監査分離正解です。監査分離根拠では SETPROG LNKLST 命令 は「z/OS MVS Operationsで SETPROG LNKLST 命令の扱いを記録する監査分離項目」と D A,L または該当パネルの出力を照合し、根拠名は監査分離根拠です。監査分離受渡では SETPROG LNKLST 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は監査分離受渡です。不適切な選択肢を整理します。 A: 監査分離流用は別カテゴリの確認であり、排除名は監査分離流用です。 B: 監査分離欠落は戻り値や記録番号に寄り、欠落名は監査分離欠落です。 C: 監査分離正答は対象出力と項目説明を結び、根拠名は監査分離正答です。 D: 監査分離不足は名称や説明だけに寄り、判定名は監査分離不足です。監査分離資料では SETPROG LNKLST 命令の使い方を出典欄から追跡し、資料名は監査分離資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文追跡の操作コマンドに関係する SETPROG LNKLST,DEFINE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. SETPROG LNKLST,DEFINE の名称と担当者名のみを残して構文追跡の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文追跡の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文追跡の操作コマンドにおいて選択記号 A を採用し、識別名は構文追跡です。構文追跡の操作コマンドにおいて SETPROG LNKLST,DEFINE は説明欄の「SETPROG LNKLST,DEFINE の用途を操作コマンドの表示で確認する構文追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡の操作コマンドに関連して、z/OS MVS Operationsでは SETPROG LNKLST,DEFINE の表示属性と IEE115I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡の操作コマンドは別カテゴリの確認を流用しており、SETPROG LNKLST,DEFINE の根拠にならないため構文追跡ではありません。 D: 構文追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文追跡ではありません。構文追跡の操作コマンドで使う SETPROG LNKLST,DEFINE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SETPROG LNKLST,DEFINE</strong></p><p>検証目的: 比較照合の操作コマンドについて、SETPROG LNKLST,DEFINE は、新しい LNKLST セットを定義 / ADD / ACTIVATE の動的入替手順を構成するサブコマンド。新しい LNKLSに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020034の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG LNKLST,DEFを指定し、OSKB020034の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SETPROG LNKLST,DEF
CASE OSKB020034
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SETPROG LNKLST,DEF
CASE OSKB020034
SOURCE z/OS MVS Operations
SETPROG LNKLST,DEFとOSKB020034が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020034を同じ出力で読み、比較照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020034
→ Enter を押す
［画面・出力］
IEE115I OSKB020034 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020034   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020034が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の SETPROG LNKLST,DEF と OSKB020034 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020034 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0257"><h3>SETPROG LPA,ADD</h3><p class="kb-meta">分類: SET PROG ・ 難易度: 中級</p><p>SETPROG LPA,ADDは、Dynamic LPA に個別モジュール / データセット内モジュールを動的追加する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更分離の操作コマンドに関する SETPROG LPA,ADD の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更分離の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更分離の操作コマンドの証跡として保存して根拠にする。</li><li>C. SETPROG LPA,ADD の変更点を出力本文から切り離して変更分離の操作コマンドの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、変更分離で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更分離正解では選択記号 D を採用し、正解名は変更分離正解です。変更分離根拠では SETPROG LPA,ADD は「SETPROG LPA,ADD の状態と出力メッセージを結び付ける変更分離項目」と D A,L または該当パネルの出力を照合し、根拠名は変更分離根拠です。変更分離保存では SETPROG LPA,ADD の出力行と IEE115I を一緒に残し、保存名は変更分離保存です。選択肢ごとの違いを示します。 A: 変更分離欠落は戻り値や記録番号に寄り、欠落名は変更分離欠落です。 B: 変更分離流用は別カテゴリの確認であり、排除名は変更分離流用です。 C: 変更分離不足は名称や説明だけに寄り、判定名は変更分離不足です。 D: 変更分離正答は対象出力と項目説明を結び、根拠名は変更分離正答です。変更分離対象では SETPROG LPA,ADD をz/OS MVS Operationsの確認記録に残し、対象名は変更分離対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開追跡の操作コマンドで SETPROG LPA,ADD の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SETPROG LPA,ADD の出力を取らず展開追跡の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開追跡の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開追跡の操作コマンドにおいて選択記号 B を採用し、識別名は展開追跡です。展開追跡の操作コマンドにおいて SETPROG LPA,ADD は説明欄の「展開追跡の操作コマンドに関係する定義値と表示行を照合する展開追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡の操作コマンドの証跡を読む担当者は、SETPROG LPA,ADD の属性行と IEE115I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡の操作コマンドは別カテゴリの確認を流用しており、SETPROG LPA,ADD の根拠にならないため展開追跡ではありません。展開追跡の操作コマンドに出る SETPROG LPA,ADD は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SETPROG LPA,ADD</strong></p><p>検証目的: 順序照合の操作コマンドについて、SETPROG LPA,ADD は、Dynamic LPA に個別モジュール / データセット内モジュールを動的追加するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020035の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSETPROG LPA,ADDを指定し、OSKB020035の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SETPROG LPA,ADD
CASE OSKB020035
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SETPROG LPA,ADD
CASE OSKB020035
SOURCE z/OS MVS Operations
SETPROG LPA,ADDとOSKB020035が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020035を同じ出力で読み、順序照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020035
→ Enter を押す
［画面・出力］
IEE115I OSKB020035 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020035   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020035が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の SETPROG LPA,ADD と OSKB020035 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020035 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET SCH


<section class="kb-item" id="c22-i0258"><h3>SET SCH=xx</h3><p class="kb-meta">分類: SET SCH ・ 難易度: 中級</p><p>SCHEDxx を活性化し、プログラム特性テーブル (PPT) を更新する。AUTH/SYSTEM/NOSWAP 等の属性変更</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開読解の操作コマンドで SET SCH=xxの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SET SCH=xxの出力を取らず展開読解の操作コマンドの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて展開読解の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D OPDATA を省略して展開読解の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開読解の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 展開読解正解では選択記号 B を採用し、正解名は展開読解正解です。展開読解根拠では SET SCH=xx は「展開読解の操作コマンドに関係する定義値と表示行を照合する展開読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は展開読解根拠です。展開読解追跡では SET SCH=xxの属性行と IEE457I を合わせ、追跡名は展開読解追跡です。誤答側の問題点を分けます。 A: 展開読解不足は名称や説明だけに寄り、判定名は展開読解不足です。 B: 展開読解正答は対象出力と項目説明を結び、根拠名は展開読解正答です。 C: 展開読解欠落は戻り値や記録番号に寄り、欠落名は展開読解欠落です。 D: 展開読解流用は別カテゴリの確認であり、排除名は展開読解流用です。展開読解初出では SET SCH=xxを MVS オペレータコマンドの運用手順で確認し、初出名は展開読解初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換追跡の操作コマンドに関する SET SCH=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA の結果を残さず置換追跡の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換追跡の操作コマンドの証跡として保存して根拠にする。</li><li>C. SET SCH=xxの変更点を出力本文から切り離して置換追跡の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換追跡の操作コマンドにおいて選択記号 D を採用し、識別名は置換追跡です。置換追跡の操作コマンドにおいて SET SCH=xx は説明欄の「SET SCH=xxの状態と出力メッセージを結び付ける置換追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡の操作コマンドに関する記録は、SET SCH=xxの出力行と IEE457I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡の操作コマンドは別カテゴリの確認を流用しており、SET SCH=xxの根拠にならないため置換追跡ではありません。 C: 置換追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡の操作コマンドで記録する SET SCH=xxはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET SCH=xx</strong></p><p>検証目的: 警告照合の操作コマンドについて、SCHEDxx を活性化し、プログラム特性テーブル (PPT) を更新する。AUTH/SYSTEM/NOSWAP 等の属性変更に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020037の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、警告照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET SCH=xxを指定し、OSKB020037の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET SCH=xx
CASE OSKB020037
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET SCH=xx
CASE OSKB020037
SOURCE z/OS MVS Operations
SET SCH=xxとOSKB020037が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020037を同じ出力で読み、警告照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020037
→ Enter を押す
［画面・出力］
IEE457I OSKB020037 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020037   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020037が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET SCH=xx と OSKB020037 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020037 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET SLIP


<section class="kb-item" id="c22-i0259"><h3>SLIP コマンド (SET SLIP=xx)</h3><p class="kb-meta">分類: SET SLIP ・ 難易度: 中級</p><p>SLIP コマンド (SET SLIP=xx)は、IEASLPxx を動的活性化し、定義済み SLIP トラップ群を一括導入する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端読解のコマンドに関係する SLIP コマンド 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、終端読解の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. SLIP コマンド 属性の名称と担当者名だけを残して終端読解のコマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端読解のコマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず終端読解のコマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端読解正解では選択記号 A を採用し、正解名は終端読解正解です。終端読解根拠では SLIP コマンド 属性 は「SLIP コマンド 属性の用途を操作コマンドの表示で確認する終端読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は終端読解根拠です。終端読解背景ではz/OS MVS Operationsの SLIP コマンド 属性と IEE457I を同じ証跡に残し、背景名は終端読解背景です。他の選択肢を確認します。 A: 終端読解正答は対象出力と項目説明を結び、根拠名は終端読解正答です。 B: 終端読解不足は名称や説明だけに寄り、判定名は終端読解不足です。 C: 終端読解流用は別カテゴリの確認であり、排除名は終端読解流用です。 D: 終端読解欠落は戻り値や記録番号に寄り、欠落名は終端読解欠落です。終端読解用語では SLIP コマンド 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は終端読解用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書追跡のコマンドで操作コマンドの運用確認を行います。SLIP コマンド (SET SLIP=xx)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書追跡のコマンドを確認した扱いにする。</li><li>B. IEE457I の有無を確認せず上書追跡のコマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. SLIP コマンド (SET SLIP=xx)の属性行を読まず上書追跡のコマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書追跡のコマンドにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡のコマンドにおいて SLIP コマンド (SET SLIP=xx) は説明欄の「z/OS MVS Operationsで SLIP コマンド (SET SLIP=xx)の扱いを記録する上書追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のコマンドを受け取る担当者は、SLIP コマンド (SET SLIP=xx)の表示結果と IEE457I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のコマンドは別カテゴリの確認を流用しており、SLIP コマンド (SET SLIP=xx)の根拠にならないため上書追跡ではありません。 B: 上書追跡のコマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のコマンドは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のコマンドが示す SLIP コマンド (SET SLIP=xx)は出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SLIP コマンド (SET SLIP=xx)</strong></p><p>検証目的: 変更照合のコマンドについて、SLIP コマンド (SET SLIP=xx)は、IEASLPxx を動的活性化し、定義済み SLIP トラップ群を一括導入するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020040の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、変更照合のコマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSLIP コマンド (SET SLIを指定し、OSKB020040の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SLIP コマンド (SET SLI
CASE OSKB020040
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SLIP コマンド (SET SLI
CASE OSKB020040
SOURCE z/OS MVS Operations
SLIP コマンド (SET SLIとOSKB020040が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020040を同じ出力で読み、変更照合のコマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020040
→ Enter を押す
［画面・出力］
IEE457I OSKB020040 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020040   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020040が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SLIP コマンド (SET SLI と OSKB020040 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020040 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET SMF


<section class="kb-item" id="c22-i0260"><h3>SET SMF=xx</h3><p class="kb-meta">分類: SET SMF ・ 難易度: 上級</p><p>SET SMF=xxは、SMFPRMxx を動的活性化し、SMF レコード・タイプ取得対象、データセット/LOGSTREAM 切替を反映する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出読解の操作コマンドで操作コマンドの運用確認を行います。SET SMF=xxの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出読解の操作コマンドを確認した扱いにする。</li><li>B. IEE457I の有無を確認せず呼出読解の操作コマンドを正常終了として記録する。</li><li>C. IEE457I を含む表示を保存し、説明欄との差分を呼出読解で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. SET SMF=xxの属性行を読まず呼出読解の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出読解正解では選択記号 C を採用し、正解名は呼出読解正解です。呼出読解根拠では SET SMF=xx は「z/OS MVS Operationsで SET SMF=xxの扱いを記録する呼出読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は呼出読解根拠です。呼出読解受渡では SET SMF=xxの表示結果と IEE457I を同じ確認単位にし、受渡名は呼出読解受渡です。不適切な選択肢を整理します。 A: 呼出読解流用は別カテゴリの確認であり、排除名は呼出読解流用です。 B: 呼出読解欠落は戻り値や記録番号に寄り、欠落名は呼出読解欠落です。 C: 呼出読解正答は対象出力と項目説明を結び、根拠名は呼出読解正答です。 D: 呼出読解不足は名称や説明だけに寄り、判定名は呼出読解不足です。呼出読解資料では SET SMF=xxの使い方を出典欄から追跡し、資料名は呼出読解資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端追跡の操作コマンドに関係する SET SMF=xxの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. SET SMF=xxの名称と担当者名のみを残して終端追跡の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端追跡の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず終端追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端追跡の操作コマンドにおいて選択記号 A を採用し、識別名は終端追跡です。終端追跡の操作コマンドにおいて SET SMF=xx は説明欄の「SET SMF=xxの用途を操作コマンドの表示で確認する終端追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡の操作コマンドに関連して、z/OS MVS Operationsでは SET SMF=xxの表示属性と IEE457I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡の操作コマンドは別カテゴリの確認を流用しており、SET SMF=xxの根拠にならないため終端追跡ではありません。 D: 終端追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため終端追跡ではありません。終端追跡の操作コマンドで使う SET SMF=xxという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET SMF=xx</strong></p><p>検証目的: 出力照合の操作コマンドについて、SET SMF=xxは、SMFPRMxx を動的活性化し、SMF レコード・タイプ取得対象、データセット/LOGSTREAM 切替を反映するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040028の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、出力照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET SMF=xxを指定し、OSKB040028の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET SMF=xx
CASE OSKB040028
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET SMF=xx
CASE OSKB040028
SOURCE z/OS MVS Operations
SET SMF=xxとOSKB040028が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040028を同じ出力で読み、出力照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB040028
→ Enter を押す
［画面・出力］
IEE457I OSKB040028 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040028   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB040028が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET SMF=xx と OSKB040028 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB040028 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>SET SMF=xx</strong></p><p>検証目的: 復旧照合の操作コマンドについて、SET SMF=xxは、SMFPRMxx を動的活性化し、SMF レコード・タイプ取得対象、データセット/LOGSTREAM 切替を反映するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020038の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、復旧照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET SMF=xxを指定し、OSKB020038の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET SMF=xx
CASE OSKB020038
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET SMF=xx
CASE OSKB020038
SOURCE z/OS MVS Operations
SET SMF=xxとOSKB020038が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020038を同じ出力で読み、復旧照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020038
→ Enter を押す
［画面・出力］
IEE457I OSKB020038 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020038   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020038が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET SMF=xx と OSKB020038 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020038 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET SMS


<section class="kb-item" id="c22-i0261"><h3>SET SMS=xx</h3><p class="kb-meta">分類: SET SMS ・ 難易度: 中級</p><p>SET SMS=xxは、IGDSMSxx を活性化し、ACS ルーチン・トレース、ACDS 切替などを反映する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換読解の操作コマンドに関する SET SMS=xxの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA の結果を残さず置換読解の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換読解の操作コマンドの証跡として保存して根拠にする。</li><li>C. SET SMS=xxの変更点を出力本文から切り離して置換読解の操作コマンドの承認欄だけ残す。</li><li>D. D OPDATA の結果から対象行を抜き出し、置換読解の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換読解正解では選択記号 D を採用し、正解名は置換読解正解です。置換読解根拠では SET SMS=xx は「SET SMS=xxの状態と出力メッセージを結び付ける置換読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は置換読解根拠です。置換読解保存では SET SMS=xxの出力行と IEE457I を一緒に残し、保存名は置換読解保存です。選択肢ごとの違いを示します。 A: 置換読解欠落は戻り値や記録番号に寄り、欠落名は置換読解欠落です。 B: 置換読解流用は別カテゴリの確認であり、排除名は置換読解流用です。 C: 置換読解不足は名称や説明だけに寄り、判定名は置換読解不足です。 D: 置換読解正答は対象出力と項目説明を結び、根拠名は置換読解正答です。置換読解対象では SET SMS=xxをz/OS MVS Operationsの確認記録に残し、対象名は置換読解対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索追跡の操作コマンドで SET SMS=xxの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SET SMS=xxの出力を取らず探索追跡の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D OPDATA を省略して探索追跡の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索追跡の操作コマンドにおいて選択記号 B を採用し、識別名は探索追跡です。探索追跡の操作コマンドにおいて SET SMS=xx は説明欄の「探索追跡の操作コマンドに関係する定義値と表示行を照合する探索追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の操作コマンドの証跡を読む担当者は、SET SMS=xxの属性行と IEE457I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の操作コマンドは別カテゴリの確認を流用しており、SET SMS=xxの根拠にならないため探索追跡ではありません。探索追跡の操作コマンドに出る SET SMS=xxは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET SMS=xx</strong></p><p>検証目的: 監査照合の操作コマンドについて、SET SMS=xxは、IGDSMSxx を活性化し、ACS ルーチン・トレース、ACDS 切替などを反映するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020039の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、監査照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET SMS=xxを指定し、OSKB020039の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET SMS=xx
CASE OSKB020039
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET SMS=xx
CASE OSKB020039
SOURCE z/OS MVS Operations
SET SMS=xxとOSKB020039が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020039を同じ出力で読み、監査照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020039
→ Enter を押す
［画面・出力］
IEE457I OSKB020039 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020039   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020039が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET SMS=xx と OSKB020039 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020039 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET TIME


<section class="kb-item" id="c22-i0262"><h3>SET DATE=yyyy.ddd</h3><p class="kb-meta">分類: SET TIME ・ 難易度: 中級</p><p>SET DATE=yyyy.dddは、MVS オペレータコマンドのSET TIMEで確認する項目です。ユリウス日形式でシステム日付を更新する。SET TIME と組み合わせて使用される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書読解の操作コマンドで操作コマンドの運用確認を行います。SET 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書読解の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書読解の操作コマンドを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、上書読解の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. SET 属性の属性行を読まず上書読解の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書読解正解では選択記号 C を採用し、正解名は上書読解正解です。上書読解根拠では SET 属性 は「z/OS MVS Operationsで SET 属性の扱いを記録する上書読解項目」と D A,L または該当パネルの出力を照合し、根拠名は上書読解根拠です。上書読解受渡では SET 属性の表示結果と IEE115I を同じ確認単位にし、受渡名は上書読解受渡です。不適切な選択肢を整理します。 A: 上書読解流用は別カテゴリの確認であり、排除名は上書読解流用です。 B: 上書読解欠落は戻り値や記録番号に寄り、欠落名は上書読解欠落です。 C: 上書読解正答は対象出力と項目説明を結び、根拠名は上書読解正答です。 D: 上書読解不足は名称や説明だけに寄り、判定名は上書読解不足です。上書読解資料では SET 属性の使い方を出典欄から追跡し、資料名は上書読解資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件追跡の操作コマンドに関係する SET DATE=yyyy.dddの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. SET DATE=yyyy.dddの名称と担当者名のみを残して条件追跡の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件追跡の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件追跡の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件追跡の操作コマンドにおいて選択記号 A を採用し、識別名は条件追跡です。条件追跡の操作コマンドにおいて SET DATE=yyyy.ddd は説明欄の「SET DATE=yyyy.dddの用途を操作コマンドの表示で確認する条件追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡の操作コマンドに関連して、z/OS MVS Operationsでは SET DATE=yyyy.dddの表示属性と IEE115I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡の操作コマンドは別カテゴリの確認を流用しており、SET DATE=yyyy.dddの根拠にならないため条件追跡ではありません。 D: 条件追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件追跡ではありません。条件追跡の操作コマンドで使う SET DATE=yyyy.dddという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET DATE=yyyy.ddd</strong></p><p>検証目的: 展開追跡の操作コマンドについて、SET DATE=yyyy.dddは、MVS オペレータコマンドの SET TIME で確認する項目です。ユリウス日形式でシステム日付を更新する。SET TIME と組み合わせに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020042の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET DATE=yyyy.dddを指定し、OSKB020042の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET DATE=yyyy.ddd
CASE OSKB020042
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET DATE=yyyy.ddd
CASE OSKB020042
SOURCE z/OS MVS Operations
SET DATE=yyyy.dddとOSKB020042が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020042を同じ出力で読み、展開追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020042
→ Enter を押す
［画面・出力］
IEE115I OSKB020042 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020042   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020042が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の SET DATE=yyyy.ddd と OSKB020042 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020042 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0263"><h3>SET TIME=hh.mm.ss</h3><p class="kb-meta">分類: SET TIME ・ 難易度: 中級</p><p>SET TIME=hh.mm.ssは、MVS オペレータコマンドのSET TIMEで確認する項目です。システム時刻の手動更新。STP/Sysplex Timer 配下では通常使用せず、独立システムでの矯正に限定する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索読解の操作コマンドで SET 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SET 属性の出力を取らず探索読解の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて探索読解の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D OPDATA を省略して探索読解の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索読解の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索読解正解では選択記号 B を採用し、正解名は探索読解正解です。探索読解根拠では SET 属性 は「探索読解の操作コマンドに関係する定義値と表示行を照合する探索読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は探索読解根拠です。探索読解追跡では SET 属性の属性行と IEE457I を合わせ、追跡名は探索読解追跡です。誤答側の問題点を分けます。 A: 探索読解不足は名称や説明だけに寄り、判定名は探索読解不足です。 B: 探索読解正答は対象出力と項目説明を結び、根拠名は探索読解正答です。 C: 探索読解欠落は戻り値や記録番号に寄り、欠落名は探索読解欠落です。 D: 探索読解流用は別カテゴリの確認であり、排除名は探索読解流用です。探索読解初出では SET 属性を MVS オペレータコマンドの運用手順で確認し、初出名は探索読解初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力追跡の操作コマンドに関する SET TIME=hh.mm.ssの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA の結果を残さず出力追跡の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力追跡の操作コマンドの証跡として保存して根拠にする。</li><li>C. SET TIME=hh.mm.ssの変更点を出力本文から切り離して出力追跡の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力追跡の操作コマンドにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡の操作コマンドにおいて SET TIME=hh.mm.ss は説明欄の「SET TIME=hh.mm.ssの状態と出力メッセージを結び付ける出力追跡項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡の操作コマンドに関する記録は、SET TIME=hh.mm.ssの出力行と IEE457I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡の操作コマンドは別カテゴリの確認を流用しており、SET TIME=hh.mm.ssの根拠にならないため出力追跡ではありません。 C: 出力追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡の操作コマンドで記録する SET TIME=hh.mm.ssはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET TIME=hh.mm.ss</strong></p><p>検証目的: 構文追跡の操作コマンドについて、SET TIME=hh.mm.ssは、MVS オペレータコマンドの SET TIME で確認する項目です。システム時刻の手動更新。STP/Sysplex Timer 配下では通に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020041の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、構文追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET TIME=hh.mm.ssを指定し、OSKB020041の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET TIME=hh.mm.ss
CASE OSKB020041
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET TIME=hh.mm.ss
CASE OSKB020041
SOURCE z/OS MVS Operations
SET TIME=hh.mm.ssとOSKB020041が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020041を同じ出力で読み、構文追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020041
→ Enter を押す
［画面・出力］
IEE457I OSKB020041 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020041   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020041が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET TIME=hh.mm.ss と OSKB020041 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020041 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET TRACE


<section class="kb-item" id="c22-i0264"><h3>SET TRACE,ON</h3><p class="kb-meta">分類: SET TRACE ・ 難易度: 上級</p><p>SET TRACE,ONは、MVS オペレータコマンドのSET TRACEで確認する項目です。システム・トレースを動的に有効化する基本形。バッファサイズ・対象 ASID も同時に指定可能</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力読解の操作コマンドに関する SET TRACE,ON の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力読解の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力読解の操作コマンドの証跡として保存して根拠にする。</li><li>C. SET TRACE,ON の変更点を出力本文から切り離して出力読解の操作コマンドの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、出力読解の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力読解正解では選択記号 D を採用し、正解名は出力読解正解です。出力読解根拠では SET TRACE,ON は「SET TRACE,ON の状態と出力メッセージを結び付ける出力読解項目」と D A,L または該当パネルの出力を照合し、根拠名は出力読解根拠です。出力読解保存では SET TRACE,ON の出力行と IEE115I を一緒に残し、保存名は出力読解保存です。選択肢ごとの違いを示します。 A: 出力読解欠落は戻り値や記録番号に寄り、欠落名は出力読解欠落です。 B: 出力読解流用は別カテゴリの確認であり、排除名は出力読解流用です。 C: 出力読解不足は名称や説明だけに寄り、判定名は出力読解不足です。 D: 出力読解正答は対象出力と項目説明を結び、根拠名は出力読解正答です。出力読解対象では SET TRACE,ON をz/OS MVS Operationsの確認記録に残し、対象名は出力読解対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切追跡の操作コマンドで SET TRACE,ON の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SET TRACE,ON の出力を取らず区切追跡の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切追跡の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切追跡の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切追跡の操作コマンドにおいて選択記号 B を採用し、識別名は区切追跡です。区切追跡の操作コマンドにおいて SET TRACE,ON は説明欄の「区切追跡の操作コマンドに関係する定義値と表示行を照合する区切追跡項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡の操作コマンドの証跡を読む担当者は、SET TRACE,ON の属性行と IEE115I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡の操作コマンドは別カテゴリの確認を流用しており、SET TRACE,ON の根拠にならないため区切追跡ではありません。区切追跡の操作コマンドに出る SET TRACE,ON は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切追跡です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET TRACE,ON</strong></p><p>検証目的: 呼出追跡の操作コマンドについて、SET TRACE,ON は、MVS オペレータコマンドの SET TRACE で確認する項目です。システム・トレースを動的に有効化する基本形。バッファサイズ・対象 ASID もに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020043の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET TRACE,ONを指定し、OSKB020043の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET TRACE,ON
CASE OSKB020043
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET TRACE,ON
CASE OSKB020043
SOURCE z/OS MVS Operations
SET TRACE,ONとOSKB020043が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020043を同じ出力で読み、呼出追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020043
→ Enter を押す
［画面・出力］
IEE115I OSKB020043 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020043   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020043が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の SET TRACE,ON と OSKB020043 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020043 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0265"><h3>TRACE CT (CTRACE 動的)</h3><p class="kb-meta">分類: SET TRACE ・ 難易度: 上級</p><p>TRACE CT (CTRACE 動的)は、コンポーネント・トレースを動的に開始 / 停止する形式 (TRACE CT,ON,COMP=XCF 等)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件読解の動的に関係する TRACE CT 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、条件読解として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. TRACE CT 属性の名称と担当者名だけを残して条件読解の動的の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件読解の動的を確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず条件読解の動的の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件読解正解では選択記号 A を採用し、正解名は条件読解正解です。条件読解根拠では TRACE CT 属性 は「TRACE CT 属性の用途を操作コマンドの表示で確認する条件読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は条件読解根拠です。条件読解背景ではz/OS MVS Operationsの TRACE CT 属性と IEE457I を同じ証跡に残し、背景名は条件読解背景です。他の選択肢を確認します。 A: 条件読解正答は対象出力と項目説明を結び、根拠名は条件読解正答です。 B: 条件読解不足は名称や説明だけに寄り、判定名は条件読解不足です。 C: 条件読解流用は別カテゴリの確認であり、排除名は条件読解流用です。 D: 条件読解欠落は戻り値や記録番号に寄り、欠落名は条件読解欠落です。条件読解用語では TRACE CT 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は条件読解用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>TRACE CT (CTRACE 動的)</strong></p><p>検証目的: 条件照合の動的について、TRACE CT (CTRACE 動的)は、コンポーネント・トレースを動的に開始 / 停止する形式 (TRACE CT,ON,COMP=XCF 等)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040029の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、条件照合の動的の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にTRACE CT (CTRACE 動を指定し、OSKB040029の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND TRACE CT (CTRACE 動
CASE OSKB040029
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM TRACE CT (CTRACE 動
CASE OSKB040029
SOURCE z/OS MVS Operations
TRACE CT (CTRACE 動とOSKB040029が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040029を同じ出力で読み、条件照合の動的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB040029
→ Enter を押す
［画面・出力］
IEE457I OSKB040029 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040029   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB040029が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の TRACE CT (CTRACE 動 と OSKB040029 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB040029 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>TRACE CT (CTRACE 動的)</strong></p><p>検証目的: 置換追跡の動的について、TRACE CT (CTRACE 動的)は、コンポーネント・トレースを動的に開始 / 停止する形式 (TRACE CT,ON,COMP=XCF 等)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020044の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、置換追跡の動的の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にTRACE CT (CTRACE 動を指定し、OSKB020044の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND TRACE CT (CTRACE 動
CASE OSKB020044
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM TRACE CT (CTRACE 動
CASE OSKB020044
SOURCE z/OS MVS Operations
TRACE CT (CTRACE 動とOSKB020044が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020044を同じ出力で読み、置換追跡の動的の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020044
→ Enter を押す
［画面・出力］
IEE457I OSKB020044 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020044   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020044が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の TRACE CT (CTRACE 動 と OSKB020044 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020044 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SET XCF


<section class="kb-item" id="c22-i0266"><h3>SET XCF=xx</h3><p class="kb-meta">分類: SET XCF ・ 難易度: 中級</p><p>SET XCF=xxは、COUPLExx を再活性化し、Sysplex の Couple DS 設定や SFM/CFRM ポリシー名の動的入替を行う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切読解の操作コマンドで SET XCF=xxの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SET XCF=xxの出力を取らず区切読解の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切読解の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D OPDATA を省略して区切読解の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切読解の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切読解正解では選択記号 B を採用し、正解名は区切読解正解です。区切読解根拠では SET XCF=xx は「区切読解の操作コマンドに関係する定義値と表示行を照合する区切読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は区切読解根拠です。区切読解追跡では SET XCF=xxの属性行と IEE457I を合わせ、追跡名は区切読解追跡です。誤答側の問題点を分けます。 A: 区切読解不足は名称や説明だけに寄り、判定名は区切読解不足です。 B: 区切読解正答は対象出力と項目説明を結び、根拠名は区切読解正答です。 C: 区切読解欠落は戻り値や記録番号に寄り、欠落名は区切読解欠落です。 D: 区切読解流用は別カテゴリの確認であり、排除名は区切読解流用です。区切読解初出では SET XCF=xxを MVS オペレータコマンドの運用手順で確認し、初出名は区切読解初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SET XCF=xx</strong></p><p>検証目的: 終端追跡の操作コマンドについて、SET XCF=xxは、COUPLExx を再活性化し、Sysplex の Couple DS 設定や SFM/CFRM ポリシー名の動的入替を行うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020045の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、終端追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSET XCF=xxを指定し、OSKB020045の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SET XCF=xx
CASE OSKB020045
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SET XCF=xx
CASE OSKB020045
SOURCE z/OS MVS Operations
SET XCF=xxとOSKB020045が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020045を同じ出力で読み、終端追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020045
→ Enter を押す
［画面・出力］
IEE457I OSKB020045 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020045   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020045が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SET XCF=xx と OSKB020045 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020045 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0267"><h3>SETXCF COUPLE,ACOUPLE=dsn</h3><p class="kb-meta">分類: SET XCF ・ 難易度: 中級</p><p>SETXCF COUPLE,ACOUPLE=dsnは、予備 Couple DS を動的に追加し、PSWITCH で本番側に昇格させる無停止切替手順を構成する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録読解の操作コマンドに関係する SETXCF COUPLE 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、記録読解の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. SETXCF COUPLE 命令の名称と担当者名だけを残して記録読解の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録読解の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず記録読解の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録読解正解では選択記号 A を採用し、正解名は記録読解正解です。記録読解根拠では SETXCF COUPLE 命令 は「SETXCF COUPLE 命令の用途を操作コマンドの表示で確認する記録読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は記録読解根拠です。記録読解背景ではz/OS MVS Operationsの SETXCF COUPLE 命令と IEE457I を同じ証跡に残し、背景名は記録読解背景です。他の選択肢を確認します。 A: 記録読解正答は対象出力と項目説明を結び、根拠名は記録読解正答です。 B: 記録読解不足は名称や説明だけに寄り、判定名は記録読解不足です。 C: 記録読解流用は別カテゴリの確認であり、排除名は記録読解流用です。 D: 記録読解欠落は戻り値や記録番号に寄り、欠落名は記録読解欠落です。記録読解用語では SETXCF COUPLE 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は記録読解用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SETXCF COUPLE,ACOUPLE=dsn</strong></p><p>検証目的: 出力追跡の操作コマンドについて、SETXCF COUPLE,ACOUPLE=dsnは、予備 Couple DS を動的に追加し、PSWITCH で本番側に昇格させる無停止切替手順を構成するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020048の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、出力追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSETXCF COUPLE,ACOUを指定し、OSKB020048の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SETXCF COUPLE,ACOU
CASE OSKB020048
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SETXCF COUPLE,ACOU
CASE OSKB020048
SOURCE z/OS MVS Operations
SETXCF COUPLE,ACOUとOSKB020048が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020048を同じ出力で読み、出力追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020048
→ Enter を押す
［画面・出力］
IEE457I OSKB020048 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020048   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020048が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SETXCF COUPLE,ACOU と OSKB020048 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020048 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0268"><h3>SETXCF MODIFY,STRNAME=name</h3><p class="kb-meta">分類: SET XCF ・ 難易度: 中級</p><p>SETXCF MODIFY,STRNAME=nameは、CF 構造のサイズ・配置を動的に変更する (リビルド要因)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先読解の操作コマンドに関する SETXCF MODIFY 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA の結果を残さず優先読解の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先読解の操作コマンドの証跡として保存して根拠にする。</li><li>C. SETXCF MODIFY 命令の変更点を出力本文から切り離して優先読解の操作コマンドの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先読解で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先読解正解では選択記号 D を採用し、正解名は優先読解正解です。優先読解根拠では SETXCF MODIFY 命令 は「SETXCF MODIFY 命令の状態と出力メッセージを結び付ける優先読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は優先読解根拠です。優先読解保存では SETXCF MODIFY 命令の出力行と IEE457I を一緒に残し、保存名は優先読解保存です。選択肢ごとの違いを示します。 A: 優先読解欠落は戻り値や記録番号に寄り、欠落名は優先読解欠落です。 B: 優先読解流用は別カテゴリの確認であり、排除名は優先読解流用です。 C: 優先読解不足は名称や説明だけに寄り、判定名は優先読解不足です。 D: 優先読解正答は対象出力と項目説明を結び、根拠名は優先読解正答です。優先読解対象では SETXCF MODIFY 命令をz/OS MVS Operationsの確認記録に残し、対象名は優先読解対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SETXCF MODIFY,STRNAME=name</strong></p><p>検証目的: 上書追跡の操作コマンドについて、SETXCF MODIFY,STRNAME=nameは、CF 構造のサイズ・配置を動的に変更する (リビルド要因)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020047の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、上書追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSETXCF MODIFY,STRNを指定し、OSKB020047の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SETXCF MODIFY,STRN
CASE OSKB020047
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SETXCF MODIFY,STRN
CASE OSKB020047
SOURCE z/OS MVS Operations
SETXCF MODIFY,STRNとOSKB020047が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020047を同じ出力で読み、上書追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020047
→ Enter を押す
［画面・出力］
IEE457I OSKB020047 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020047   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020047が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SETXCF MODIFY,STRN と OSKB020047 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020047 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0269"><h3>SETXCF START,POLICY,TYPE=type</h3><p class="kb-meta">分類: SET XCF ・ 難易度: 上級</p><p>CFRM/SFM/LOGR/ARM の新規ポリシーを活性化する動的コマンド。SET XCF とは別系統だがセットで使われる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲読解の操作コマンドで操作コマンドの運用確認を行います。SETXCF START 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲読解の操作コマンドを確認した扱いにする。</li><li>B. IEE457I の有無を確認せず範囲読解の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、範囲読解の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. SETXCF START 命令の属性行を読まず範囲読解の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲読解正解では選択記号 C を採用し、正解名は範囲読解正解です。範囲読解根拠では SETXCF START 命令 は「z/OS MVS Operationsで SETXCF START 命令の扱いを記録する範囲読解項目」と D OPDATA または該当パネルの出力を照合し、根拠名は範囲読解根拠です。範囲読解受渡では SETXCF START 命令の表示結果と IEE457I を同じ確認単位にし、受渡名は範囲読解受渡です。不適切な選択肢を整理します。 A: 範囲読解流用は別カテゴリの確認であり、排除名は範囲読解流用です。 B: 範囲読解欠落は戻り値や記録番号に寄り、欠落名は範囲読解欠落です。 C: 範囲読解正答は対象出力と項目説明を結び、根拠名は範囲読解正答です。 D: 範囲読解不足は名称や説明だけに寄り、判定名は範囲読解不足です。範囲読解資料では SETXCF START 命令の使い方を出典欄から追跡し、資料名は範囲読解資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SETXCF START,POLICY,TYPE=type</strong></p><p>検証目的: 探索追跡の操作コマンドについて、CFRM/SFM/LOGR/ARM の新規ポリシーを活性化する動的コマンド。SET XCF とは別系統だがセットで使われるに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020046の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、探索追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSETXCF START,POLICを指定し、OSKB020046の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND SETXCF START,POLIC
CASE OSKB020046
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM SETXCF START,POLIC
CASE OSKB020046
SOURCE z/OS MVS Operations
SETXCF START,POLICとOSKB020046が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020046を同じ出力で読み、探索追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020046
→ Enter を押す
［画面・出力］
IEE457I OSKB020046 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020046   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020046が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の SETXCF START,POLIC と OSKB020046 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020046 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## STOPMN


<section class="kb-item" id="c22-i0270"><h3>STOPMN JOBNAMES</h3><p class="kb-meta">分類: STOPMN ・ 難易度: 中級</p><p>STOPMN JOBNAMESは、MVS オペレータコマンドのSTOPMNで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力判定の操作コマンドに関する STOPMN JOBNAMES の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA の結果を残さず出力判定の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力判定の操作コマンドの証跡として保存して根拠にする。</li><li>C. STOPMN JOBNAMES の変更点を出力本文から切り離して出力判定の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力判定の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力判定の操作コマンドにおいて選択記号 D を採用し、識別名は出力判定です。出力判定の操作コマンドにおいて STOPMN JOBNAMES は説明欄の「STOPMN JOBNAMES の状態と出力メッセージを結び付ける出力判定項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は出力判定です。出力判定の操作コマンドに関する記録は、STOPMN JOBNAMES の出力行と IEE457I を一緒に保存し、背景名は出力判定です。選択肢ごとの違いを示します。 A: 出力判定の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため出力判定ではありません。 B: 出力判定の操作コマンドは別カテゴリの確認を流用しており、STOPMN JOBNAMES の根拠にならないため出力判定ではありません。 C: 出力判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力判定ではありません。 D: 出力判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力判定です。出力判定の操作コマンドで記録する STOPMN JOBNAMES はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STOPMN JOBNAMES</strong></p><p>検証目的: 構文検査の操作コマンドについて、STOPMN JOBNAMES は、MVS オペレータコマンドの STOPMN で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030061の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、構文検査の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSTOPMN JOBNAMESを指定し、OSKB030061の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND STOPMN JOBNAMES
CASE OSKB030061
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM STOPMN JOBNAMES
CASE OSKB030061
SOURCE z/OS MVS Operations
STOPMN JOBNAMESとOSKB030061が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030061を同じ出力で読み、構文検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB030061
→ Enter を押す
［画面・出力］
IEE457I OSKB030061 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030061   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB030061が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の STOPMN JOBNAMES と OSKB030061 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB030061 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0271"><h3>STOPMN STATUS</h3><p class="kb-meta">分類: STOPMN ・ 難易度: 中級</p><p>STOPMN STATUSは、MVS オペレータコマンドのSTOPMNで確認する項目です。MN STATUS を停止する。継続使用は SYSLOG 肥大化のため必要に応じてオフにする</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件判定の操作コマンドに関係する STOPMN STATUS の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件判定として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. STOPMN STATUS の名称と担当者名のみを残して条件判定の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件判定の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず条件判定の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件判定の操作コマンドにおいて選択記号 A を採用し、識別名は条件判定です。条件判定の操作コマンドにおいて STOPMN STATUS は説明欄の「STOPMN STATUS の用途を操作コマンドの表示で確認する条件判定項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は条件判定です。条件判定の操作コマンドに関連して、z/OS MVS Operationsでは STOPMN STATUS の表示属性と IEE457I を同じ証跡に残し、背景名は条件判定です。他の選択肢を確認します。 A: 条件判定の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件判定です。 B: 条件判定の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件判定ではありません。 C: 条件判定の操作コマンドは別カテゴリの確認を流用しており、STOPMN STATUS の根拠にならないため条件判定ではありません。 D: 条件判定の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため条件判定ではありません。条件判定の操作コマンドで使う STOPMN STATUS という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件判定です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STOPMN STATUS</strong></p><p>検証目的: 展開検査の操作コマンドについて、STOPMN STATUS は、MVS オペレータコマンドの STOPMN で確認する項目です。MN STATUS を停止する。継続使用は SYSLOG 肥大化のため必要に応じてに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030062の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、展開検査の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にSTOPMN STATUSを指定し、OSKB030062の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND STOPMN STATUS
CASE OSKB030062
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM STOPMN STATUS
CASE OSKB030062
SOURCE z/OS MVS Operations
STOPMN STATUSとOSKB030062が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030062を同じ出力で読み、展開検査の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB030062
→ Enter を押す
［画面・出力］
IEE457I OSKB030062 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030062   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB030062が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の STOPMN STATUS と OSKB030062 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB030062 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## SYMBOL


<section class="kb-item" id="c22-i0272"><h3>&amp;SYSCLONE</h3><p class="kb-meta">分類: SYMBOL ・ 難易度: 中級</p><p>&amp;SYSCLONEは、MVS オペレータコマンドのSYMBOLで確認する項目です。SYSNAME の 2 桁短縮 (CLONE) を返すシステム・シンボル。DSN プレフィックス分離などに使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較検査の操作コマンドで&amp;SYSCLONE の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. &amp;SYSCLONE の出力を取らず比較検査の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、比較検査の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較検査の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較検査の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較検査の操作コマンドにおいて選択記号 B を採用し、識別名は比較検査です。比較検査の操作コマンドにおいて&amp;SYSCLONE は説明欄の「比較検査の操作コマンドに関係する定義値と表示行を照合する比較検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較検査です。比較検査の操作コマンドの証跡を読む担当者は、&amp;SYSCLONE の属性行と IEE115I を合わせて追跡し、背景名は比較検査です。誤答側の問題点を分けます。 A: 比較検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較検査ではありません。 B: 比較検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較検査です。 C: 比較検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較検査ではありません。 D: 比較検査の操作コマンドは別カテゴリの確認を流用しており、&amp;SYSCLONE の根拠にならないため比較検査ではありません。比較検査の操作コマンドに出る&amp;SYSCLONE は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>&amp;SYSCLONE</strong></p><p>検証目的: 上書追跡の操作コマンドについて、&amp;SYSCLONE は、MVS オペレータコマンドの SYMBOL で確認する項目です。SYSNAME の 2 桁短縮 (CLONE) を返すシステム・シンボル。DSN プレフィに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030047の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、上書追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に&amp;SYSCLONEを指定し、OSKB030047の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND &amp;SYSCLONE
CASE OSKB030047
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM &amp;SYSCLONE
CASE OSKB030047
SOURCE z/OS MVS Operations
&amp;SYSCLONEとOSKB030047が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030047を同じ出力で読み、上書追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030047
→ Enter を押す
［画面・出力］
IEE115I OSKB030047 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030047   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030047が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の &amp;SYSCLONE と OSKB030047 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030047 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0273"><h3>&amp;SYSNAME</h3><p class="kb-meta">分類: SYMBOL ・ 難易度: 中級</p><p>&amp;SYSNAMEは、MVS オペレータコマンドのSYMBOLで確認する項目です。Sysplex システム名を返すシステム・シンボル。PARMLIB / JCL / EXEC の汎用化に最頻出</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先検査の操作コマンドに関する&amp;SYSNAME の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先検査の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先検査の操作コマンドの証跡として保存して根拠にする。</li><li>C. &amp;SYSNAME の変更点を出力本文から切り離して優先検査の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先検査の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先検査の操作コマンドにおいて選択記号 D を採用し、識別名は優先検査です。優先検査の操作コマンドにおいて&amp;SYSNAME は説明欄の「&amp;SYSNAME の状態と出力メッセージを結び付ける優先検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先検査です。優先検査の操作コマンドに関する記録は、&amp;SYSNAME の出力行と IEE115I を一緒に保存し、背景名は優先検査です。選択肢ごとの違いを示します。 A: 優先検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先検査ではありません。 B: 優先検査の操作コマンドは別カテゴリの確認を流用しており、&amp;SYSNAME の根拠にならないため優先検査ではありません。 C: 優先検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先検査ではありません。 D: 優先検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので優先検査です。優先検査の操作コマンドで記録する&amp;SYSNAME はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>&amp;SYSNAME</strong></p><p>検証目的: 終端追跡の操作コマンドについて、&amp;SYSNAME は、MVS オペレータコマンドの SYMBOL で確認する項目です。Sysplex システム名を返すシステム・シンボル。PARMLIB / JCL / EXECに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030045の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄に&amp;SYSNAMEを指定し、OSKB030045の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND &amp;SYSNAME
CASE OSKB030045
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM &amp;SYSNAME
CASE OSKB030045
SOURCE z/OS MVS Operations
&amp;SYSNAMEとOSKB030045が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030045を同じ出力で読み、終端追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030045
→ Enter を押す
［画面・出力］
IEE115I OSKB030045 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030045   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030045が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の &amp;SYSNAME と OSKB030045 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030045 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0274"><h3>&amp;SYSPLEX</h3><p class="kb-meta">分類: SYMBOL ・ 難易度: 中級</p><p>&amp;SYSPLEXは、MVS オペレータコマンドのSYMBOLで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録検査の操作コマンドに関係する&amp;SYSPLEX の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、記録検査として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. &amp;SYSPLEX の名称と担当者名のみを残して記録検査の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で記録検査の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録検査の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録検査の操作コマンドにおいて選択記号 A を採用し、識別名は記録検査です。記録検査の操作コマンドにおいて&amp;SYSPLEX は説明欄の「&amp;SYSPLEX の用途を操作コマンドの表示で確認する記録検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録検査です。記録検査の操作コマンドに関連して、z/OS MVS Operationsでは&amp;SYSPLEX の表示属性と IEE115I を同じ証跡に残し、背景名は記録検査です。他の選択肢を確認します。 A: 記録検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録検査です。 B: 記録検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録検査ではありません。 C: 記録検査の操作コマンドは別カテゴリの確認を流用しており、&amp;SYSPLEX の根拠にならないため記録検査ではありません。 D: 記録検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録検査ではありません。記録検査の操作コマンドで使う&amp;SYSPLEX という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>&amp;SYSPLEX</strong></p><p>検証目的: 探索追跡の操作コマンドについて、&amp;SYSPLEX は、MVS オペレータコマンドの SYMBOL で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030046の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄に&amp;SYSPLEXを指定し、OSKB030046の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND &amp;SYSPLEX
CASE OSKB030046
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM &amp;SYSPLEX
CASE OSKB030046
SOURCE z/OS MVS Operations
&amp;SYSPLEXとOSKB030046が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030046を同じ出力で読み、探索追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030046
→ Enter を押す
［画面・出力］
IEE115I OSKB030046 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030046   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030046が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の &amp;SYSPLEX と OSKB030046 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030046 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0275"><h3>&amp;SYSR1</h3><p class="kb-meta">分類: SYMBOL ・ 難易度: 中級</p><p>&amp;SYSR1は、MVS オペレータコマンドのSYMBOLで確認する項目です。IPL 装置のボリュームシリアル (SYSRES) を返すシステム・シンボル。PARMLIB 直接参照時に使う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序検査の操作コマンドで操作コマンドの運用確認を行います。&amp;SYSR1 の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序検査の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序検査の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、順序検査の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. &amp;SYSR1 の属性行を読まず順序検査の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序検査の操作コマンドにおいて選択記号 C を採用し、識別名は順序検査です。順序検査の操作コマンドにおいて&amp;SYSR1 は説明欄の「z/OS MVS Operationsで&amp;SYSR1 の扱いを記録する順序検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は順序検査です。順序検査の操作コマンドを受け取る担当者は、&amp;SYSR1 の表示結果と IEE115I を同じ確認単位として扱い、背景名は順序検査です。不適切な選択肢を整理します。 A: 順序検査の操作コマンドは別カテゴリの確認を流用しており、&amp;SYSR1 の根拠にならないため順序検査ではありません。 B: 順序検査の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため順序検査ではありません。 C: 順序検査の操作コマンドは対象出力と項目説明を結び、根拠を残すので順序検査です。 D: 順序検査の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため順序検査ではありません。順序検査の操作コマンドが示す&amp;SYSR1 は出典欄の資料で使い方を追跡できる項目であり、用語名は順序検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>&amp;SYSR1</strong></p><p>検証目的: 出力追跡の操作コマンドについて、&amp;SYSR1 は、MVS オペレータコマンドの SYMBOL で確認する項目です。IPL 装置のボリュームシリアル (SYSRES) を返すシステム・シンボル。PARMLIB 直に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030048の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に&amp;SYSR1を指定し、OSKB030048の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND &amp;SYSR1
CASE OSKB030048
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM &amp;SYSR1
CASE OSKB030048
SOURCE z/OS MVS Operations
&amp;SYSR1とOSKB030048が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030048を同じ出力で読み、出力追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030048
→ Enter を押す
［画面・出力］
IEE115I OSKB030048 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030048   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030048が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の &amp;SYSR1 と OSKB030048 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030048 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0276"><h3>D SYMBOLS 表示</h3><p class="kb-meta">分類: SYMBOL ・ 難易度: 中級</p><p>D SYMBOLS 表示は、MVS オペレータコマンドのSYMBOLで確認する項目です。現在解決可能なシステム・シンボルとその値を一覧表示するコマンド。PARMLIB の汎用化チェックに必須</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域検査の表示に関する D SYMBOLS 表示の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域検査の表示の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域検査の表示の証跡として保存して根拠にする。</li><li>C. D SYMBOLS 表示の変更点を出力本文から切り離して値域検査の表示の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、値域検査の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域検査の表示において選択記号 D を採用し、識別名は値域検査です。値域検査の表示において D SYMBOLS 表示 は説明欄の「D SYMBOLS 表示の状態と出力メッセージを結び付ける値域検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域検査です。値域検査の表示に関する記録は、D SYMBOLS 表示の出力行と IEE115I を一緒に保存し、背景名は値域検査です。選択肢ごとの違いを示します。 A: 値域検査の表示は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域検査ではありません。 B: 値域検査の表示は別カテゴリの確認を流用しており、D SYMBOLS 表示の根拠にならないため値域検査ではありません。 C: 値域検査の表示は名称や説明のみに寄り、状態を示す出力本文が不足するため値域検査ではありません。 D: 値域検査の表示は対象出力と項目説明を結び、根拠を残すので値域検査です。値域検査の表示で記録する D SYMBOLS 表示はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D SYMBOLS 表示</strong></p><p>検証目的: 条件追跡の表示について、D SYMBOLS 表示は、MVS オペレータコマンドの SYMBOL で確認する項目です。現在解決可能なシステム・シンボルとその値を一覧表示するコマンド。PARMLIB の汎に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030049の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件追跡の表示の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にD SYMBOLS 表示を指定し、OSKB030049の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND D SYMBOLS 表示
CASE OSKB030049
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM D SYMBOLS 表示
CASE OSKB030049
SOURCE z/OS MVS Operations
D SYMBOLS 表示とOSKB030049が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030049を同じ出力で読み、条件追跡の表示の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030049
→ Enter を押す
［画面・出力］
IEE115I OSKB030049 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030049   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030049が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の D SYMBOLS 表示 と OSKB030049 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030049 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0277"><h3>IEASYMxx での定義</h3><p class="kb-meta">分類: SYMBOL ・ 難易度: 中級</p><p>IEASYMxx での定義は、MVS オペレータコマンドのSYMBOLで確認する項目です。ユーザ・シンボル (&amp;USRSYM 等) は IEASYMxx で定義する。LOAD パラメータの 3 桁目で SUFFIX を選ぶ</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告検査のでの定義に関係する IEASYMxx での定義の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、警告検査として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. IEASYMxx での定義の名称と担当者名のみを残して警告検査のでの定義の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で警告検査のでの定義を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告検査のでの定義の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告検査のでの定義において選択記号 A を採用し、識別名は警告検査です。警告検査のでの定義において IEASYMxx での定義 は説明欄の「IEASYMxx での定義の用途を操作コマンドの表示で確認する警告検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告検査です。警告検査のでの定義に関連して、z/OS MVS Operationsでは IEASYMxx での定義の表示属性と IEE115I を同じ証跡に残し、背景名は警告検査です。他の選択肢を確認します。 A: 警告検査のでの定義は対象出力と項目説明を結び、根拠を残すので警告検査です。 B: 警告検査のでの定義は名称や説明のみに寄り、状態を示す出力本文が不足するため警告検査ではありません。 C: 警告検査のでの定義は別カテゴリの確認を流用しており、IEASYMxx での定義の根拠にならないため警告検査ではありません。 D: 警告検査のでの定義は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告検査ではありません。警告検査のでの定義で使う IEASYMxx での定義という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>IEASYMxx での定義</strong></p><p>検証目的: 区切追跡のの定義について、IEASYMxx での定義は、MVS オペレータコマンドの SYMBOL で確認する項目です。ユーザ・シンボル (&amp;USRSYM 等) は IEASYMxx で定義する。LOAに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040050の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切追跡のの定義の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にIEASYMxx での定義を指定し、OSKB040050の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND IEASYMxx での定義
CASE OSKB040050
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM IEASYMxx での定義
CASE OSKB040050
SOURCE z/OS MVS Operations
IEASYMxx での定義とOSKB040050が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040050を同じ出力で読み、区切追跡のの定義の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040050
→ Enter を押す
［画面・出力］
IEE115I OSKB040050 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040050   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040050が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の IEASYMxx での定義 と OSKB040050 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040050 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>IEASYMxx での定義</strong></p><p>検証目的: 区切追跡のでの定義について、IEASYMxx での定義は、MVS オペレータコマンドの SYMBOL で確認する項目です。ユーザ・シンボル (&amp;USRSYM 等) は IEASYMxx で定義する。LOAに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030050の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、区切追跡のでの定義の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にIEASYMxx での定義を指定し、OSKB030050の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND IEASYMxx での定義
CASE OSKB030050
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM IEASYMxx での定義
CASE OSKB030050
SOURCE z/OS MVS Operations
IEASYMxx での定義とOSKB030050が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030050を同じ出力で読み、区切追跡のでの定義の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030050
→ Enter を押す
［画面・出力］
IEE115I OSKB030050 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030050   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030050が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の IEASYMxx での定義 と OSKB030050 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030050 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## TRACK


<section class="kb-item" id="c22-i0278"><h3>TRACK 全体</h3><p class="kb-meta">分類: TRACK ・ 難易度: 中級</p><p>TRACK 全体は、TRACK コマンドで現在稼働中のアドレス・スペース活動とハードウェア利用状況を 1 行ずつ追跡表示する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文検査の全体に関係する TRACK 全体の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文検査として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. TRACK 全体の名称と担当者名のみを残して構文検査の全体の表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文検査の全体を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文検査の全体の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 構文検査の全体において選択記号 A を採用し、識別名は構文検査です。構文検査の全体において TRACK 全体 は説明欄の「TRACK 全体の用途を操作コマンドの表示で確認する構文検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文検査です。構文検査の全体に関連して、z/OS MVS Operationsでは TRACK 全体の表示属性と IEE115I を同じ証跡に残し、背景名は構文検査です。他の選択肢を確認します。 A: 構文検査の全体は対象出力と項目説明を結び、根拠を残すので構文検査です。 B: 構文検査の全体は名称や説明のみに寄り、状態を示す出力本文が不足するため構文検査ではありません。 C: 構文検査の全体は別カテゴリの確認を流用しており、TRACK 全体の根拠にならないため構文検査ではありません。 D: 構文検査の全体は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文検査ではありません。構文検査の全体で使う TRACK 全体という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TRACK 全体</strong></p><p>検証目的: 比較照合の全体について、TRACK 全体は、TRACK コマンドで現在稼働中のアドレス・スペース活動とハードウェア利用状況を 1 行ずつ追跡表示するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030034の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較照合の全体の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にTRACK 全体を指定し、OSKB030034の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND TRACK 全体
CASE OSKB030034
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM TRACK 全体
CASE OSKB030034
SOURCE z/OS MVS Operations
TRACK 全体とOSKB030034が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030034を同じ出力で読み、比較照合の全体の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030034
→ Enter を押す
［画面・出力］
IEE115I OSKB030034 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030034   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030034が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の TRACK 全体 と OSKB030034 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030034 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## V CN


<section class="kb-item" id="c22-i0279"><h3>V CN(*),ACTIVATE</h3><p class="kb-meta">分類: V CN ・ 難易度: 中級</p><p>V CN(*),ACTIVATEは、全ての該当コンソールを一括処理する形式 (発行コンソール側で扱える対象に限定)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告照合再の*に関係する V CN(*) 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、警告照合再の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. V CN(*) 命令の名称と担当者名だけを残して警告照合再の*の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で警告照合再の*を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告照合再の*の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告照合再正解では選択記号 A を採用し、正解名は警告照合再正解です。警告照合再根拠では V CN(*) 命令 は「V CN(*) 命令の用途を操作コマンドの表示で確認する警告照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は警告照合再根拠です。警告照合再背景ではz/OS MVS Operationsの V CN(*) 命令と IEE115I を同じ証跡に残し、背景名は警告照合再背景です。他の選択肢を確認します。 A: 警告照合再正答は対象出力と項目説明を結び、根拠名は警告照合再正答です。 B: 警告照合再不足は名称や説明だけに寄り、判定名は警告照合再不足です。 C: 警告照合再流用は別カテゴリの確認であり、排除名は警告照合再流用です。 D: 警告照合再欠落は戻り値や記録番号に寄り、欠落名は警告照合再欠落です。警告照合再用語では V CN(*) 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は警告照合再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 監査確認の*で操作コマンドの運用確認を行います。V CN(*),ACTIVATE の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査確認の*を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査確認の*を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、監査確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. V CN(*),ACTIVATE の属性行を読まず監査確認の*の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査確認の*において選択記号 C を採用し、識別名は監査確認です。監査確認の*において V CN(*),ACTIVATE は説明欄の「z/OS MVS Operationsで V CN(*),ACTIVATE の扱いを記録する監査確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認の*を受け取る担当者は、V CN(*),ACTIVATE の表示結果と IEE115I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認の*は別カテゴリの確認を流用しており、V CN(*),ACTIVATE の根拠にならないため監査確認ではありません。 B: 監査確認の*は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査確認ではありません。 C: 監査確認の*は対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認の*は名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認の*が示す V CN(*),ACTIVATE は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V CN(*),ACTIVATE</strong></p><p>検証目的: 優先整理の*について、V CN(*),ACTIVATE は、全ての該当コンソールを一括処理する形式 (発行コンソール側で扱える対象に限定)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020112の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先整理の*の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(*),ACTIVATEを指定し、OSKB020112の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V CN(*),ACTIVATE
CASE OSKB020112
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V CN(*),ACTIVATE
CASE OSKB020112
SOURCE z/OS MVS Operations
V CN(*),ACTIVATEとOSKB020112が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020112を同じ出力で読み、優先整理の*の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020112
→ Enter を押す
［画面・出力］
IEE115I OSKB020112 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020112   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020112が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V CN(*),ACTIVATE と OSKB020112 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020112 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0280"><h3>V CN(name),ACTIVE</h3><p class="kb-meta">分類: V CN ・ 難易度: 中級</p><p>V CN(name),ACTIVEは、指定コンソールを活性化し、メッセージ・ストリームを再受信できるようにする</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序照合再の操作コマンドで操作コマンドの運用確認を行います。V CN(name) 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序照合再の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序照合再の操作コマンドを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を順序照合再で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. V CN(name) 命令の属性行を読まず順序照合再の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序照合再正解では選択記号 C を採用し、正解名は順序照合再正解です。順序照合再根拠では V CN(name) 命令 は「z/OS MVS Operationsで V CN(name) 命令の扱いを記録する順序照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は順序照合再根拠です。順序照合再受渡では V CN(name) 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は順序照合再受渡です。不適切な選択肢を整理します。 A: 順序照合再流用は別カテゴリの確認であり、排除名は順序照合再流用です。 B: 順序照合再欠落は戻り値や記録番号に寄り、欠落名は順序照合再欠落です。 C: 順序照合再正答は対象出力と項目説明を結び、根拠名は順序照合再正答です。 D: 順序照合再不足は名称や説明だけに寄り、判定名は順序照合再不足です。順序照合再資料では V CN(name) 命令の使い方を出典欄から追跡し、資料名は順序照合再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 警告確認の操作コマンドに関係する V CN(name),ACTIVE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、警告確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. V CN(name),ACTIVE の名称と担当者名のみを残して警告確認の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で警告確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告確認の操作コマンドにおいて選択記号 A を採用し、識別名は警告確認です。警告確認の操作コマンドにおいて V CN(name),ACTIVE は説明欄の「V CN(name),ACTIVE の用途を操作コマンドの表示で確認する警告確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認の操作コマンドに関連して、z/OS MVS Operationsでは V CN(name),ACTIVE の表示属性と IEE115I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認の操作コマンドは別カテゴリの確認を流用しており、V CN(name),ACTIVE の根拠にならないため警告確認ではありません。 D: 警告確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告確認ではありません。警告確認の操作コマンドで使う V CN(name),ACTIVE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>V CN(name),ACTIVE</strong></p><p>検証目的: 変更照合の操作コマンドについて、V CN(name),ACTIVE は、指定コンソールを活性化し、メッセージ・ストリームを再受信できるようにするに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040040の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更照合の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),ACTIVEを指定し、OSKB040040の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V CN(name),ACTIVE
CASE OSKB040040
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V CN(name),ACTIVE
CASE OSKB040040
SOURCE z/OS MVS Operations
V CN(name),ACTIVEとOSKB040040が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040040を同じ出力で読み、変更照合の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040040
→ Enter を押す
［画面・出力］
IEE115I OSKB040040 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040040   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040040が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V CN(name),ACTIVE と OSKB040040 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040040 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>V CN(name),ACTIVE</strong></p><p>検証目的: 区切整理の操作コマンドについて、V CN(name),ACTIVE は、指定コンソールを活性化し、メッセージ・ストリームを再受信できるようにするに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020110の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),ACTIVEを指定し、OSKB020110の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V CN(name),ACTIVE
CASE OSKB020110
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V CN(name),ACTIVE
CASE OSKB020110
SOURCE z/OS MVS Operations
V CN(name),ACTIVEとOSKB020110が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020110を同じ出力で読み、区切整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020110
→ Enter を押す
［画面・出力］
IEE115I OSKB020110 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020110   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020110が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V CN(name),ACTIVE と OSKB020110 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020110 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0281"><h3>V CN(name),AUTH=MASTER</h3><p class="kb-meta">分類: V CN ・ 難易度: 中級</p><p>V CN(name),AUTH=MASTERは、MVS オペレータコマンドのV CNで確認する項目です。コンソール権限をマスタ・コンソールに昇格させる動的変更</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域照合再の操作コマンドに関する V CN 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域照合再の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域照合再の操作コマンドの証跡として保存して根拠にする。</li><li>C. V CN 属性の変更点を出力本文から切り離して値域照合再の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、値域照合再の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域照合再正解では選択記号 D を採用し、正解名は値域照合再正解です。値域照合再根拠では V CN 属性 は「V CN 属性の状態と出力メッセージを結び付ける値域照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は値域照合再根拠です。値域照合再保存では V CN 属性の出力行と IEE115I を一緒に残し、保存名は値域照合再保存です。選択肢ごとの違いを示します。 A: 値域照合再欠落は戻り値や記録番号に寄り、欠落名は値域照合再欠落です。 B: 値域照合再流用は別カテゴリの確認であり、排除名は値域照合再流用です。 C: 値域照合再不足は名称や説明だけに寄り、判定名は値域照合再不足です。 D: 値域照合再正答は対象出力と項目説明を結び、根拠名は値域照合再正答です。値域照合再対象では V CN 属性をz/OS MVS Operationsの確認記録に残し、対象名は値域照合再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 復旧確認の操作コマンドで V CN(name),AUTH=MASTER の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V CN(name),AUTH=MASTER の出力を取らず復旧確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、復旧確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧確認の操作コマンドにおいて選択記号 B を採用し、識別名は復旧確認です。復旧確認の操作コマンドにおいて V CN(name),AUTH=MASTER は説明欄の「復旧確認の操作コマンドに関係する定義値と表示行を照合する復旧確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認の操作コマンドの証跡を読む担当者は、V CN(name),AUTH=MASTER の属性行と IEE115I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認の操作コマンドは別カテゴリの確認を流用しており、V CN(name),AUTH=MASTER の根拠にならないため復旧確認ではありません。復旧確認の操作コマンドに出る V CN(name),AUTH=MASTER は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V CN(name),AUTH=MASTER</strong></p><p>検証目的: 範囲整理の操作コマンドについて、V CN(name),AUTH=MASTER は、MVS オペレータコマンドの V CN で確認する項目です。コンソール権限をマスタ・コンソールに昇格させる動的変更に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020111の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、範囲整理の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),AUTH=MAを指定し、OSKB020111の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V CN(name),AUTH=MA
CASE OSKB020111
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V CN(name),AUTH=MA
CASE OSKB020111
SOURCE z/OS MVS Operations
V CN(name),AUTH=MAとOSKB020111が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020111を同じ出力で読み、範囲整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020111
→ Enter を押す
［画面・出力］
IEE115I OSKB020111 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020111   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020111が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V CN(name),AUTH=MA と OSKB020111 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020111 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0282"><h3>V CN(name),LU=lu</h3><p class="kb-meta">分類: V CN ・ 難易度: 中級</p><p>V CN(name),LU=luは、MVS オペレータコマンドのV CNで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧照合再の操作コマンドで V CN(name) 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V CN(name) 命令の出力を取らず復旧照合再の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて復旧照合再の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧照合再の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧照合再の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧照合再正解では選択記号 B を採用し、正解名は復旧照合再正解です。復旧照合再根拠では V CN(name) 命令 は「復旧照合再の操作コマンドに関係する定義値と表示行を照合する復旧照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は復旧照合再根拠です。復旧照合再追跡では V CN(name) 命令の属性行と IEE115I を合わせ、追跡名は復旧照合再追跡です。誤答側の問題点を分けます。 A: 復旧照合再不足は名称や説明だけに寄り、判定名は復旧照合再不足です。 B: 復旧照合再正答は対象出力と項目説明を結び、根拠名は復旧照合再正答です。 C: 復旧照合再欠落は戻り値や記録番号に寄り、欠落名は復旧照合再欠落です。 D: 復旧照合再流用は別カテゴリの確認であり、排除名は復旧照合再流用です。復旧照合再初出では V CN(name) 命令を MVS オペレータコマンドの運用手順で確認し、初出名は復旧照合再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 変更確認の操作コマンドに関する V CN(name),LU=luの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更確認の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. V CN(name),LU=luの変更点を出力本文から切り離して変更確認の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、変更確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 変更確認の操作コマンドにおいて選択記号 D を採用し、識別名は変更確認です。変更確認の操作コマンドにおいて V CN(name),LU=lu は説明欄の「V CN(name),LU=luの状態と出力メッセージを結び付ける変更確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認の操作コマンドに関する記録は、V CN(name),LU=luの出力行と IEE115I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため変更確認ではありません。 B: 変更確認の操作コマンドは別カテゴリの確認を流用しており、V CN(name),LU=luの根拠にならないため変更確認ではありません。 C: 変更確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認の操作コマンドで記録する V CN(name),LU=luはz/OS MVS Operationsの確認記録に残す対象名であり、用語名は変更確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V CN(name),LU=lu</strong></p><p>検証目的: 記録整理の操作コマンドについて、V CN(name),LU=luは、MVS オペレータコマンドの V CN で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けてに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020113の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録整理の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV CN(name),LU=luを指定し、OSKB020113の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V CN(name),LU=lu
CASE OSKB020113
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V CN(name),LU=lu
CASE OSKB020113
SOURCE z/OS MVS Operations
V CN(name),LU=luとOSKB020113が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020113を同じ出力で読み、記録整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020113
→ Enter を押す
［画面・出力］
IEE115I OSKB020113 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020113   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020113が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V CN(name),LU=lu と OSKB020113 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020113 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## V CONSOLE


<section class="kb-item" id="c22-i0283"><h3>V CONSOLE,name,ALT=name2</h3><p class="kb-meta">分類: V CONSOLE ・ 難易度: 中級</p><p>V CONSOLE,name,ALT=name2は、コンソールの代替コンソール (障害時切替先) を動的に変更する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切追跡再の操作コマンドで V CONSOLE 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V CONSOLE 命令の出力を取らず区切追跡再の操作コマンドの説明文と承認印だけを残す。</li><li>B. 属性行、戻り表示、メッセージ見出しを合わせて区切追跡再の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切追跡再の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切追跡再の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切追跡再正解では選択記号 B を採用し、正解名は区切追跡再正解です。区切追跡再根拠では V CONSOLE 命令 は「区切追跡再の操作コマンドに関係する定義値と表示行を照合する区切追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は区切追跡再根拠です。区切追跡再追跡では V CONSOLE 命令の属性行と IEE115I を合わせ、追跡名は区切追跡再追跡です。誤答側の問題点を分けます。 A: 区切追跡再不足は名称や説明だけに寄り、判定名は区切追跡再不足です。 B: 区切追跡再正答は対象出力と項目説明を結び、根拠名は区切追跡再正答です。 C: 区切追跡再欠落は戻り値や記録番号に寄り、欠落名は区切追跡再欠落です。 D: 区切追跡再流用は別カテゴリの確認であり、排除名は区切追跡再流用です。区切追跡再初出では V CONSOLE 命令を MVS オペレータコマンドの運用手順で確認し、初出名は区切追跡再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 優先照合の操作コマンドに関する V CONSOLE,name,ALT=name2の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. V CONSOLE,name,ALT=name2の変更点を出力本文から切り離して優先照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先照合の操作コマンドにおいて選択記号 D を採用し、識別名は優先照合です。優先照合の操作コマンドにおいて V CONSOLE,name,ALT=name2 は説明欄の「V CONSOLE,name,ALT=name2の状態と出力メッセージを結び付ける優先照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合の操作コマンドに関する記録は、V CONSOLE,name,ALT=name2の出力行と IEE115I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先照合ではありません。 B: 優先照合の操作コマンドは別カテゴリの確認を流用しており、V CONSOLE,name,ALT=name2の根拠にならないため優先照合ではありません。 C: 優先照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合の操作コマンドで記録する V CONSOLE,name,ALT=name2はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V CONSOLE,name,ALT=name2</strong></p><p>検証目的: 終端確認の操作コマンドについて、V CONSOLE,name,ALT=name2は、コンソールの代替コンソール (障害時切替先) を動的に変更するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030005の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV CONSOLE,name,ALTを指定し、OSKB030005の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V CONSOLE,name,ALT
CASE OSKB030005
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V CONSOLE,name,ALT
CASE OSKB030005
SOURCE z/OS MVS Operations
V CONSOLE,name,ALTとOSKB030005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030005を同じ出力で読み、終端確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030005
→ Enter を押す
［画面・出力］
IEE115I OSKB030005 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030005   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V CONSOLE,name,ALT と OSKB030005 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## V GRS


<section class="kb-item" id="c22-i0284"><h3>V GRS(ALL),RESTART</h3><p class="kb-meta">分類: V GRS ・ 難易度: 中級</p><p>V GRS(ALL),RESTARTは、MVS オペレータコマンドのV GRSで確認する項目です。Sysplex 全体の GRS を一括復帰させる。リング再構成のリカバリ手段</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索追跡再の操作コマンドで V GRS(ALL) 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V GRS(ALL) 命令の出力を取らず探索追跡再の操作コマンドの説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて探索追跡再の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D OPDATA を省略して探索追跡再の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索追跡再の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索追跡再正解では選択記号 B を採用し、正解名は探索追跡再正解です。探索追跡再根拠では V GRS(ALL) 命令 は「探索追跡再の操作コマンドに関係する定義値と表示行を照合する探索追跡再項目」と D OPDATA または該当パネルの出力を照合し、根拠名は探索追跡再根拠です。探索追跡再追跡では V GRS(ALL) 命令の属性行と IEE457I を合わせ、追跡名は探索追跡再追跡です。誤答側の問題点を分けます。 A: 探索追跡再不足は名称や説明だけに寄り、判定名は探索追跡再不足です。 B: 探索追跡再正答は対象出力と項目説明を結び、根拠名は探索追跡再正答です。 C: 探索追跡再欠落は戻り値や記録番号に寄り、欠落名は探索追跡再欠落です。 D: 探索追跡再流用は別カテゴリの確認であり、排除名は探索追跡再流用です。探索追跡再初出では V GRS(ALL) 命令を MVS オペレータコマンドの運用手順で確認し、初出名は探索追跡再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力照合の操作コマンドに関する V GRS(ALL),RESTART の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D OPDATA の結果を残さず出力照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. V GRS(ALL),RESTART の変更点を出力本文から切り離して出力照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力照合の操作コマンドにおいて選択記号 D を採用し、識別名は出力照合です。出力照合の操作コマンドにおいて V GRS(ALL),RESTART は説明欄の「V GRS(ALL),RESTART の状態と出力メッセージを結び付ける出力照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合の操作コマンドに関する記録は、V GRS(ALL),RESTART の出力行と IEE457I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため出力照合ではありません。 B: 出力照合の操作コマンドは別カテゴリの確認を流用しており、V GRS(ALL),RESTART の根拠にならないため出力照合ではありません。 C: 出力照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合の操作コマンドで記録する V GRS(ALL),RESTART はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V GRS(ALL),RESTART</strong></p><p>検証目的: 構文確認の操作コマンドについて、V GRS(ALL),RESTART は、MVS オペレータコマンドの V GRS で確認する項目です。Sysplex 全体の GRS を一括復帰させる。リング再構成のリカバリ手に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030001の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、構文確認の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV GRS(ALL),RESTARTを指定し、OSKB030001の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V GRS(ALL),RESTART
CASE OSKB030001
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V GRS(ALL),RESTART
CASE OSKB030001
SOURCE z/OS MVS Operations
V GRS(ALL),RESTARTとOSKB030001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030001を同じ出力で読み、構文確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB030001
→ Enter を押す
［画面・出力］
IEE457I OSKB030001 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030001   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB030001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の V GRS(ALL),RESTART と OSKB030001 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB030001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0285"><h3>V GRS(sysname),QUIESCE</h3><p class="kb-meta">分類: V GRS ・ 難易度: 中級</p><p>V GRS(sysname),QUIESCEは、MVS オペレータコマンドのV GRSで確認する項目です。指定システムを GRS 複合体から切り離す前段階。ENQ 要求が拒否される状態に遷移</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換追跡再の操作コマンドに関する V GRS 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換追跡再の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換追跡再の操作コマンドの証跡として保存して根拠にする。</li><li>C. V GRS 属性の変更点を出力本文から切り離して置換追跡再の操作コマンドの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、置換追跡再で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 置換追跡再正解では選択記号 D を採用し、正解名は置換追跡再正解です。置換追跡再根拠では V GRS 属性 は「V GRS 属性の状態と出力メッセージを結び付ける置換追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は置換追跡再根拠です。置換追跡再保存では V GRS 属性の出力行と IEE115I を一緒に残し、保存名は置換追跡再保存です。選択肢ごとの違いを示します。 A: 置換追跡再欠落は戻り値や記録番号に寄り、欠落名は置換追跡再欠落です。 B: 置換追跡再流用は別カテゴリの確認であり、排除名は置換追跡再流用です。 C: 置換追跡再不足は名称や説明だけに寄り、判定名は置換追跡再不足です。 D: 置換追跡再正答は対象出力と項目説明を結び、根拠名は置換追跡再正答です。置換追跡再対象では V GRS 属性をz/OS MVS Operationsの確認記録に残し、対象名は置換追跡再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索照合の操作コマンドで V GRS(sysname),QUIESCE の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V GRS(sysname),QUIESCE の出力を取らず探索照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索照合の操作コマンドにおいて選択記号 B を採用し、識別名は探索照合です。探索照合の操作コマンドにおいて V GRS(sysname),QUIESCE は説明欄の「探索照合の操作コマンドに関係する定義値と表示行を照合する探索照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合の操作コマンドの証跡を読む担当者は、V GRS(sysname),QUIESCE の属性行と IEE115I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索照合ではありません。 D: 探索照合の操作コマンドは別カテゴリの確認を流用しており、V GRS(sysname),QUIESCE の根拠にならないため探索照合ではありません。探索照合の操作コマンドに出る V GRS(sysname),QUIESCE は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V GRS(sysname),QUIESCE</strong></p><p>検証目的: 監査整理の操作コマンドについて、V GRS(sysname),QUIESCE は、MVS オペレータコマンドの V GRS で確認する項目です。指定システムを GRS 複合体から切り離す前段階。ENQ 要求が拒に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020119の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査整理の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV GRS(sysname),QUIを指定し、OSKB020119の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V GRS(sysname),QUI
CASE OSKB020119
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V GRS(sysname),QUI
CASE OSKB020119
SOURCE z/OS MVS Operations
V GRS(sysname),QUIとOSKB020119が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020119を同じ出力で読み、監査整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020119
→ Enter を押す
［画面・出力］
IEE115I OSKB020119 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020119   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020119が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V GRS(sysname),QUI と OSKB020119 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020119 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0286"><h3>V GRS(sysname),RESTART</h3><p class="kb-meta">分類: V GRS ・ 難易度: 中級</p><p>V GRS(sysname),RESTARTは、MVS オペレータコマンドのV GRSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端追跡再の操作コマンドに関係する V GRS 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、終端追跡再の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. V GRS 属性の名称と担当者名だけを残して終端追跡再の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で終端追跡再の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE457I の有無を見ず終端追跡再の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端追跡再正解では選択記号 A を採用し、正解名は終端追跡再正解です。終端追跡再根拠では V GRS 属性 は「V GRS 属性の用途を操作コマンドの表示で確認する終端追跡再項目」と D OPDATA または該当パネルの出力を照合し、根拠名は終端追跡再根拠です。終端追跡再背景ではz/OS MVS Operationsの V GRS 属性と IEE457I を同じ証跡に残し、背景名は終端追跡再背景です。他の選択肢を確認します。 A: 終端追跡再正答は対象出力と項目説明を結び、根拠名は終端追跡再正答です。 B: 終端追跡再不足は名称や説明だけに寄り、判定名は終端追跡再不足です。 C: 終端追跡再流用は別カテゴリの確認であり、排除名は終端追跡再流用です。 D: 終端追跡再欠落は戻り値や記録番号に寄り、欠落名は終端追跡再欠落です。終端追跡再用語では V GRS 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は終端追跡再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書照合の操作コマンドで操作コマンドの運用確認を行います。V GRS(sysname),RESTART の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書照合の操作コマンドを確認した扱いにする。</li><li>B. IEE457I の有無を確認せず上書照合の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. V GRS(sysname),RESTART の属性行を読まず上書照合の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書照合の操作コマンドにおいて選択記号 C を採用し、識別名は上書照合です。上書照合の操作コマンドにおいて V GRS(sysname),RESTART は説明欄の「z/OS MVS Operationsで V GRS(sysname),RESTART の扱いを記録する上書照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の操作コマンドを受け取る担当者は、V GRS(sysname),RESTART の表示結果と IEE457I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の操作コマンドは別カテゴリの確認を流用しており、V GRS(sysname),RESTART の根拠にならないため上書照合ではありません。 B: 上書照合の操作コマンドは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため上書照合ではありません。 C: 上書照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の操作コマンドが示す V GRS(sysname),RESTART は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V GRS(sysname),RESTART</strong></p><p>検証目的: 変更整理の操作コマンドについて、V GRS(sysname),RESTART は、MVS オペレータコマンドの V GRS で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020120の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、変更整理の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV GRS(sysname),RESを指定し、OSKB020120の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V GRS(sysname),RES
CASE OSKB020120
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V GRS(sysname),RES
CASE OSKB020120
SOURCE z/OS MVS Operations
V GRS(sysname),RESとOSKB020120が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020120を同じ出力で読み、変更整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020120
→ Enter を押す
［画面・出力］
IEE457I OSKB020120 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020120   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020120が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の V GRS(sysname),RES と OSKB020120 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020120 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## V PATH


<section class="kb-item" id="c22-i0287"><h3>V PATH(devnum,chp),OFFLINE</h3><p class="kb-meta">分類: V PATH ・ 難易度: 中級</p><p>V PATH(devnum,chp),OFFLINEは、MVS オペレータコマンドのV PATHで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件追跡再の操作コマンドに関係する V PATH 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、条件追跡再の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. V PATH 属性の名称と担当者名だけを残して条件追跡再の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で条件追跡再の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件追跡再の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件追跡再正解では選択記号 A を採用し、正解名は条件追跡再正解です。条件追跡再根拠では V PATH 属性 は「V PATH 属性の用途を操作コマンドの表示で確認する条件追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は条件追跡再根拠です。条件追跡再背景ではz/OS MVS Operationsの V PATH 属性と IEE115I を同じ証跡に残し、背景名は条件追跡再背景です。他の選択肢を確認します。 A: 条件追跡再正答は対象出力と項目説明を結び、根拠名は条件追跡再正答です。 B: 条件追跡再不足は名称や説明だけに寄り、判定名は条件追跡再不足です。 C: 条件追跡再流用は別カテゴリの確認であり、排除名は条件追跡再流用です。 D: 条件追跡再欠落は戻り値や記録番号に寄り、欠落名は条件追跡再欠落です。条件追跡再用語では V PATH 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は条件追跡再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 範囲照合の操作コマンドで操作コマンドの運用確認を行います。V PATH(devnum,chp),OFFLI の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲照合の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲照合の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. V PATH(devnum,chp),OFFLI の属性行を読まず範囲照合の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲照合の操作コマンドにおいて選択記号 C を採用し、識別名は範囲照合です。範囲照合の操作コマンドにおいて V PATH(devnum,chp),OFFLI は説明欄の「z/OS MVS Operationsで V PATH(devnum,chp),OFFLI の扱いを記録する範囲照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合の操作コマンドを受け取る担当者は、V PATH(devnum,chp),OFFLI の表示結果と IEE115I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合の操作コマンドは別カテゴリの確認を流用しており、V PATH(devnum,chp),OFFLI の根拠にならないため範囲照合ではありません。 B: 範囲照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合の操作コマンドが示す V PATH(devnum,chp),OFFLI は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V PATH(devnum,chp),OFFLINE</strong></p><p>検証目的: 置換確認の操作コマンドについて、V PATH(devnum,chp),OFFLINE は、MVS オペレータコマンドの V PATH で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示さに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030004の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV PATH(devnum,chp)を指定し、OSKB030004の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V PATH(devnum,chp)
CASE OSKB030004
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V PATH(devnum,chp)
CASE OSKB030004
SOURCE z/OS MVS Operations
V PATH(devnum,chp)とOSKB030004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030004を同じ出力で読み、置換確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030004
→ Enter を押す
［画面・出力］
IEE115I OSKB030004 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030004   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V PATH(devnum,chp) と OSKB030004 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0288"><h3>V PATH(devnum,chp),ONLINE</h3><p class="kb-meta">分類: V PATH ・ 難易度: 中級</p><p>V PATH(devnum,chp),ONLINEは、MVS オペレータコマンドのV PATHで確認する項目です。指定装置の特定チャネル・パス (CHPID) をオンライン化する。装置レベルではなく経路レベルの制御</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力追跡再の操作コマンドに関する V PATH 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力追跡再の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力追跡再の操作コマンドの証跡として保存して根拠にする。</li><li>C. V PATH 属性の変更点を出力本文から切り離して出力追跡再の操作コマンドの承認欄だけ残す。</li><li>D. D A,L の結果から対象行を抜き出し、出力追跡再の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力追跡再正解では選択記号 D を採用し、正解名は出力追跡再正解です。出力追跡再根拠では V PATH 属性 は「V PATH 属性の状態と出力メッセージを結び付ける出力追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は出力追跡再根拠です。出力追跡再保存では V PATH 属性の出力行と IEE115I を一緒に残し、保存名は出力追跡再保存です。選択肢ごとの違いを示します。 A: 出力追跡再欠落は戻り値や記録番号に寄り、欠落名は出力追跡再欠落です。 B: 出力追跡再流用は別カテゴリの確認であり、排除名は出力追跡再流用です。 C: 出力追跡再不足は名称や説明だけに寄り、判定名は出力追跡再不足です。 D: 出力追跡再正答は対象出力と項目説明を結び、根拠名は出力追跡再正答です。出力追跡再対象では V PATH 属性をz/OS MVS Operationsの確認記録に残し、対象名は出力追跡再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切照合の操作コマンドで V PATH(devnum,chp),ONLIN の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V PATH(devnum,chp),ONLIN の出力を取らず区切照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切照合の操作コマンドにおいて選択記号 B を採用し、識別名は区切照合です。区切照合の操作コマンドにおいて V PATH(devnum,chp),ONLIN は説明欄の「区切照合の操作コマンドに関係する定義値と表示行を照合する区切照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合の操作コマンドの証跡を読む担当者は、V PATH(devnum,chp),ONLIN の属性行と IEE115I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため区切照合ではありません。 D: 区切照合の操作コマンドは別カテゴリの確認を流用しており、V PATH(devnum,chp),ONLIN の根拠にならないため区切照合ではありません。区切照合の操作コマンドに出る V PATH(devnum,chp),ONLIN は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は区切照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V PATH(devnum,chp),ONLINE</strong></p><p>検証目的: 呼出確認の操作コマンドについて、V PATH(devnum,chp),ONLINE は、MVS オペレータコマンドの V PATH で確認する項目です。指定装置の特定チャネル・パス (CHPID) をオンラインに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030003の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV PATH(devnum,chp)を指定し、OSKB030003の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V PATH(devnum,chp)
CASE OSKB030003
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V PATH(devnum,chp)
CASE OSKB030003
SOURCE z/OS MVS Operations
V PATH(devnum,chp)とOSKB030003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030003を同じ出力で読み、呼出確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030003
→ Enter を押す
［画面・出力］
IEE115I OSKB030003 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030003   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V PATH(devnum,chp) と OSKB030003 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## V TCPIP


<section class="kb-item" id="c22-i0289"><h3>V TCPIP,,OBEY,dsn</h3><p class="kb-meta">分類: V TCPIP ・ 難易度: 上級</p><p>V TCPIP,,OBEY,dsnは、MVS オペレータコマンドのV TCPIPで確認する項目です。TCP/IP の動的構成変更 (OBEYFILE) 指示。プロファイル PROFILE.TCPIP を OBEY 形式で取り込む</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録照合の操作コマンドに関係する V TCPIP,,OBEY,dsnの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、記録照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. V TCPIP,,OBEY,dsnの名称と担当者名のみを残して記録照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で記録照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録照合の操作コマンドにおいて選択記号 A を採用し、識別名は記録照合です。記録照合の操作コマンドにおいて V TCPIP,,OBEY,dsn は説明欄の「V TCPIP,,OBEY,dsnの用途を操作コマンドの表示で確認する記録照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合の操作コマンドに関連して、z/OS MVS Operationsでは V TCPIP,,OBEY,dsnの表示属性と IEE115I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合の操作コマンドは別カテゴリの確認を流用しており、V TCPIP,,OBEY,dsnの根拠にならないため記録照合ではありません。 D: 記録照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録照合ではありません。記録照合の操作コマンドで使う V TCPIP,,OBEY,dsnという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V TCPIP,,OBEY,dsn</strong></p><p>検証目的: 探索確認の操作コマンドについて、V TCPIP,,OBEY,dsnは、MVS オペレータコマンドの V TCPIP で確認する項目です。TCP/IP の動的構成変更 (OBEYFILE) 指示。プロファイルに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030006の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV TCPIP,,OBEY,dsnを指定し、OSKB030006の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V TCPIP,,OBEY,dsn
CASE OSKB030006
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V TCPIP,,OBEY,dsn
CASE OSKB030006
SOURCE z/OS MVS Operations
V TCPIP,,OBEY,dsnとOSKB030006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030006を同じ出力で読み、探索確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030006
→ Enter を押す
［画面・出力］
IEE115I OSKB030006 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030006   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V TCPIP,,OBEY,dsn と OSKB030006 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0290"><h3>V TCPIP,,SYNTAXCHECK,dsn</h3><p class="kb-meta">分類: V TCPIP ・ 難易度: 上級</p><p>V TCPIP,,SYNTAXCHECK,dsnは、OBEYFILE の構文検査のみを実行し、活性化はしないドライラン形式</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較照合の操作コマンドで V TCPIP,,SYNTAXCHECK,dsnの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V TCPIP,,SYNTAXCHECK,dsnの出力を取らず比較照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、比較照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較照合の操作コマンドにおいて選択記号 B を採用し、識別名は比較照合です。比較照合の操作コマンドにおいて V TCPIP,,SYNTAXCHECK,dsn は説明欄の「比較照合の操作コマンドに関係する定義値と表示行を照合する比較照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合の操作コマンドの証跡を読む担当者は、V TCPIP,,SYNTAXCHECK,dsnの属性行と IEE115I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較照合ではありません。 D: 比較照合の操作コマンドは別カテゴリの確認を流用しており、V TCPIP,,SYNTAXCHECK,dsnの根拠にならないため比較照合ではありません。比較照合の操作コマンドに出る V TCPIP,,SYNTAXCHECK,dsnは MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V TCPIP,,SYNTAXCHECK,dsn</strong></p><p>検証目的: 上書確認の操作コマンドについて、V TCPIP,,SYNTAXCHECK,dsnは、OBEYFILE の構文検査のみを実行し、活性化はしないドライラン形式に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030007の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV TCPIP,,SYNTAXCHEを指定し、OSKB030007の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V TCPIP,,SYNTAXCHE
CASE OSKB030007
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V TCPIP,,SYNTAXCHE
CASE OSKB030007
SOURCE z/OS MVS Operations
V TCPIP,,SYNTAXCHEとOSKB030007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030007を同じ出力で読み、上書確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030007
→ Enter を押す
［画面・出力］
IEE115I OSKB030007 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030007   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V TCPIP,,SYNTAXCHE と OSKB030007 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0291"><h3>V TCPIP,,VARY,nnnn,...</h3><p class="kb-meta">分類: V TCPIP ・ 難易度: 上級</p><p>V TCPIP,,VARY,nnnn,...は、MVS オペレータコマンドのV TCPIPで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序照合のなどで操作コマンドの運用確認を行います。V TCPIP,,VARY,nnnn,などの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序照合のなどを確認した扱いにする。</li><li>B. IEE457I の有無を確認せず順序照合のなどを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、順序照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. V TCPIP,,VARY,nnnn,などの属性行を読まず順序照合のなどの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序照合のなどにおいて選択記号 C を採用し、識別名は順序照合です。順序照合のなどにおいて V TCPIP,,VARY,nnnn,など は説明欄の「z/OS MVS Operationsで V TCPIP,,VARY,nnnn,などの扱いを記録する順序照合項目」と D OPDATA または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合のなどを受け取る担当者は、V TCPIP,,VARY,nnnn,などの表示結果と IEE457I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合のなどは別カテゴリの確認を流用しており、V TCPIP,,VARY,nnnn,などの根拠にならないため順序照合ではありません。 B: 順序照合のなどは戻り値や記録番号に寄り、IEE457I や属性表示を落とすため順序照合ではありません。 C: 順序照合のなどは対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合のなどが示す V TCPIP,,VARY,nnnn,などは出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details></section>


## V WLM


<section class="kb-item" id="c22-i0292"><h3>V WLM,APPLENV=name,QUIESCE</h3><p class="kb-meta">分類: V WLM ・ 難易度: 上級</p><p>V WLM,APPLENV=name,QUIESCEは、MVS オペレータコマンドのV WLMで確認する項目です。WLM アプリケーション環境を停止状態 (QUIESCE) にする。サーバ・アドレス・スペースは整理される</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文追跡再の操作コマンドに関係する V WLM 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、構文追跡再として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. V WLM 命令の名称と担当者名だけを残して構文追跡再の操作コマンドの表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で構文追跡再の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文追跡再の操作コマンドの戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文追跡再正解では選択記号 A を採用し、正解名は構文追跡再正解です。構文追跡再根拠では V WLM 命令 は「V WLM 命令の用途を操作コマンドの表示で確認する構文追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は構文追跡再根拠です。構文追跡再背景ではz/OS MVS Operationsの V WLM 命令と IEE115I を同じ証跡に残し、背景名は構文追跡再背景です。他の選択肢を確認します。 A: 構文追跡再正答は対象出力と項目説明を結び、根拠名は構文追跡再正答です。 B: 構文追跡再不足は名称や説明だけに寄り、判定名は構文追跡再不足です。 C: 構文追跡再流用は別カテゴリの確認であり、排除名は構文追跡再流用です。 D: 構文追跡再欠落は戻り値や記録番号に寄り、欠落名は構文追跡再欠落です。構文追跡再用語では V WLM 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は構文追跡再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出照合の操作コマンドで操作コマンドの運用確認を行います。V WLM,APPLENV=name,QUIES の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出照合の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出照合の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. V WLM,APPLENV=name,QUIES の属性行を読まず呼出照合の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出照合の操作コマンドにおいて選択記号 C を採用し、識別名は呼出照合です。呼出照合の操作コマンドにおいて V WLM,APPLENV=name,QUIES は説明欄の「z/OS MVS Operationsで V WLM,APPLENV=name,QUIES の扱いを記録する呼出照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合の操作コマンドを受け取る担当者は、V WLM,APPLENV=name,QUIES の表示結果と IEE115I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合の操作コマンドは別カテゴリの確認を流用しており、V WLM,APPLENV=name,QUIES の根拠にならないため呼出照合ではありません。 B: 呼出照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合の操作コマンドが示す V WLM,APPLENV=name,QUIES は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>V WLM,APPLENV=name,QUIESCE</strong></p><p>検証目的: 構文追跡の操作コマンドについて、V WLM,APPLENV=name,QUIESCE は、MVS オペレータコマンドの V WLM で確認する項目です。WLM アプリケーション環境を停止状態 (QUIESCE)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040041の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,APPLENV=nameを指定し、OSKB040041の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V WLM,APPLENV=name
CASE OSKB040041
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V WLM,APPLENV=name
CASE OSKB040041
SOURCE z/OS MVS Operations
V WLM,APPLENV=nameとOSKB040041が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040041を同じ出力で読み、構文追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040041
→ Enter を押す
［画面・出力］
IEE115I OSKB040041 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040041   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040041が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V WLM,APPLENV=name と OSKB040041 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040041 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>V WLM,APPLENV=name,QUIESCE</strong></p><p>検証目的: 値域整理の操作コマンドについて、V WLM,APPLENV=name,QUIESCE は、MVS オペレータコマンドの V WLM で確認する項目です。WLM アプリケーション環境を停止状態 (QUIESCE)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020116の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、値域整理の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,APPLENV=nameを指定し、OSKB020116の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V WLM,APPLENV=name
CASE OSKB020116
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V WLM,APPLENV=name
CASE OSKB020116
SOURCE z/OS MVS Operations
V WLM,APPLENV=nameとOSKB020116が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020116を同じ出力で読み、値域整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020116
→ Enter を押す
［画面・出力］
IEE115I OSKB020116 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020116   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020116が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V WLM,APPLENV=name と OSKB020116 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020116 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0293"><h3>V WLM,APPLENV=name,RESUME</h3><p class="kb-meta">分類: V WLM ・ 難易度: 上級</p><p>V WLM,APPLENV=name,RESUMEは、MVS オペレータコマンドのV WLMで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS MVS System Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更照合再の操作コマンドに関する V WLM 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず変更照合再の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更照合再の操作コマンドの証跡として保存して根拠にする。</li><li>C. V WLM 命令の変更点を出力本文から切り離して変更照合再の操作コマンドの承認欄だけ残す。</li><li>D. D A,L で得た表示本文を使い、変更照合再の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更照合再正解では選択記号 D を採用し、正解名は変更照合再正解です。変更照合再根拠では V WLM 命令 は「V WLM 命令の状態と出力メッセージを結び付ける変更照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は変更照合再根拠です。変更照合再保存では V WLM 命令の出力行と IEE115I を一緒に残し、保存名は変更照合再保存です。選択肢ごとの違いを示します。 A: 変更照合再欠落は戻り値や記録番号に寄り、欠落名は変更照合再欠落です。 B: 変更照合再流用は別カテゴリの確認であり、排除名は変更照合再流用です。 C: 変更照合再不足は名称や説明だけに寄り、判定名は変更照合再不足です。 D: 変更照合再正答は対象出力と項目説明を結び、根拠名は変更照合再正答です。変更照合再対象では V WLM 命令をz/OS MVS Operationsの確認記録に残し、対象名は変更照合再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開照合の操作コマンドで V WLM,APPLENV=name,RESUM の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V WLM,APPLENV=name,RESUM の出力を取らず展開照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開照合の操作コマンドにおいて選択記号 B を採用し、識別名は展開照合です。展開照合の操作コマンドにおいて V WLM,APPLENV=name,RESUM は説明欄の「展開照合の操作コマンドに関係する定義値と表示行を照合する展開照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合の操作コマンドの証跡を読む担当者は、V WLM,APPLENV=name,RESUM の属性行と IEE115I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため展開照合ではありません。 D: 展開照合の操作コマンドは別カテゴリの確認を流用しており、V WLM,APPLENV=name,RESUM の根拠にならないため展開照合ではありません。展開照合の操作コマンドに出る V WLM,APPLENV=name,RESUM は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は展開照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V WLM,APPLENV=name,RESUME</strong></p><p>検証目的: 順序整理の操作コマンドについて、V WLM,APPLENV=name,RESUME は、MVS オペレータコマンドの V WLM で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示されるに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020115の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、順序整理の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,APPLENV=nameを指定し、OSKB020115の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V WLM,APPLENV=name
CASE OSKB020115
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V WLM,APPLENV=name
CASE OSKB020115
SOURCE z/OS MVS Operations
V WLM,APPLENV=nameとOSKB020115が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020115を同じ出力で読み、順序整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020115
→ Enter を押す
［画面・出力］
IEE115I OSKB020115 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020115   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020115が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V WLM,APPLENV=name と OSKB020115 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020115 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0294"><h3>V WLM,POLICY=name</h3><p class="kb-meta">分類: V WLM ・ 難易度: 上級</p><p>V WLM,POLICY=nameは、MVS オペレータコマンドのV WLMで確認する項目です。WLM サービス・ポリシーを動的に切り替える。日中/夜間プロファイル切替の典型</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査照合再の操作コマンドで操作コマンドの運用確認を行います。V WLM 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査照合再の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査照合再の操作コマンドを正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE115I を読み、監査照合再の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. V WLM 命令の属性行を読まず監査照合再の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査照合再正解では選択記号 C を採用し、正解名は監査照合再正解です。監査照合再根拠では V WLM 命令 は「z/OS MVS Operationsで V WLM 命令の扱いを記録する監査照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は監査照合再根拠です。監査照合再受渡では V WLM 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は監査照合再受渡です。不適切な選択肢を整理します。 A: 監査照合再流用は別カテゴリの確認であり、排除名は監査照合再流用です。 B: 監査照合再欠落は戻り値や記録番号に寄り、欠落名は監査照合再欠落です。 C: 監査照合再正答は対象出力と項目説明を結び、根拠名は監査照合再正答です。 D: 監査照合再不足は名称や説明だけに寄り、判定名は監査照合再不足です。監査照合再資料では V WLM 命令の使い方を出典欄から追跡し、資料名は監査照合再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文照合の操作コマンドに関係する V WLM,POLICY=nameの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. V WLM,POLICY=nameの名称と担当者名のみを残して構文照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で構文照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず構文照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文照合の操作コマンドにおいて選択記号 A を採用し、識別名は構文照合です。構文照合の操作コマンドにおいて V WLM,POLICY=name は説明欄の「V WLM,POLICY=nameの用途を操作コマンドの表示で確認する構文照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合の操作コマンドに関連して、z/OS MVS Operationsでは V WLM,POLICY=nameの表示属性と IEE115I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合の操作コマンドは別カテゴリの確認を流用しており、V WLM,POLICY=nameの根拠にならないため構文照合ではありません。 D: 構文照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため構文照合ではありません。構文照合の操作コマンドで使う V WLM,POLICY=nameという用語は MVS オペレータコマンドで扱う確認対象であり、用語名は構文照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V WLM,POLICY=name</strong></p><p>検証目的: 比較整理の操作コマンドについて、V WLM,POLICY=nameは、MVS オペレータコマンドの V WLM で確認する項目です。WLM サービス・ポリシーを動的に切り替える。日中/夜間プロファイル切替の典に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020114の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,POLICY=nameを指定し、OSKB020114の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V WLM,POLICY=name
CASE OSKB020114
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V WLM,POLICY=name
CASE OSKB020114
SOURCE z/OS MVS Operations
V WLM,POLICY=nameとOSKB020114が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020114を同じ出力で読み、比較整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020114
→ Enter を押す
［画面・出力］
IEE115I OSKB020114 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020114   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020114が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V WLM,POLICY=name と OSKB020114 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020114 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0295"><h3>V WLM,SCHENV=name,OFF</h3><p class="kb-meta">分類: V WLM ・ 難易度: 上級</p><p>V WLM,SCHENV=name,OFFは、スケジューリング環境をオフにし、新規ジョブの実行を抑止する (Quiesce)</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出追跡再の操作コマンドで操作コマンドの運用確認を行います。V WLM 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で呼出追跡再の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず呼出追跡再の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、呼出追跡再の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. V WLM 命令の属性行を読まず呼出追跡再の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出追跡再正解では選択記号 C を採用し、正解名は呼出追跡再正解です。呼出追跡再根拠では V WLM 命令 は「z/OS MVS Operationsで V WLM 命令の扱いを記録する呼出追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は呼出追跡再根拠です。呼出追跡再受渡では V WLM 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は呼出追跡再受渡です。不適切な選択肢を整理します。 A: 呼出追跡再流用は別カテゴリの確認であり、排除名は呼出追跡再流用です。 B: 呼出追跡再欠落は戻り値や記録番号に寄り、欠落名は呼出追跡再欠落です。 C: 呼出追跡再正答は対象出力と項目説明を結び、根拠名は呼出追跡再正答です。 D: 呼出追跡再不足は名称や説明だけに寄り、判定名は呼出追跡再不足です。呼出追跡再資料では V WLM 命令の使い方を出典欄から追跡し、資料名は呼出追跡再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端照合の操作コマンドに関係する V WLM,SCHENV=name,OFF の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. V WLM,SCHENV=name,OFF の名称と担当者名のみを残して終端照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端照合の操作コマンドにおいて選択記号 A を採用し、識別名は終端照合です。終端照合の操作コマンドにおいて V WLM,SCHENV=name,OFF は説明欄の「V WLM,SCHENV=name,OFF の用途を操作コマンドの表示で確認する終端照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合の操作コマンドに関連して、z/OS MVS Operationsでは V WLM,SCHENV=name,OFF の表示属性と IEE115I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合の操作コマンドは別カテゴリの確認を流用しており、V WLM,SCHENV=name,OFF の根拠にならないため終端照合ではありません。 D: 終端照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端照合ではありません。終端照合の操作コマンドで使う V WLM,SCHENV=name,OFF という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V WLM,SCHENV=name,OFF</strong></p><p>検証目的: 復旧整理の操作コマンドについて、V WLM,SCHENV=name,OFF は、スケジューリング環境をオフにし、新規ジョブの実行を抑止する (Quiesce)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020118の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,SCHENV=name,を指定し、OSKB020118の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V WLM,SCHENV=name,
CASE OSKB020118
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V WLM,SCHENV=name,
CASE OSKB020118
SOURCE z/OS MVS Operations
V WLM,SCHENV=name,とOSKB020118が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020118を同じ出力で読み、復旧整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020118
→ Enter を押す
［画面・出力］
IEE115I OSKB020118 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020118   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020118が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V WLM,SCHENV=name, と OSKB020118 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020118 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0296"><h3>V WLM,SCHENV=name,ON</h3><p class="kb-meta">分類: V WLM ・ 難易度: 上級</p><p>V WLM,SCHENV=name,ONは、スケジューリング環境をオン状態 (リソース利用可能) にし、待機ジョブを実行可能化する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開追跡再の操作コマンドで V WLM 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V WLM 命令の出力を取らず展開追跡再の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、展開追跡再の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して展開追跡再の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開追跡再の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開追跡再正解では選択記号 B を採用し、正解名は展開追跡再正解です。展開追跡再根拠では V WLM 命令 は「展開追跡再の操作コマンドに関係する定義値と表示行を照合する展開追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は展開追跡再根拠です。展開追跡再追跡では V WLM 命令の属性行と IEE115I を合わせ、追跡名は展開追跡再追跡です。誤答側の問題点を分けます。 A: 展開追跡再不足は名称や説明だけに寄り、判定名は展開追跡再不足です。 B: 展開追跡再正答は対象出力と項目説明を結び、根拠名は展開追跡再正答です。 C: 展開追跡再欠落は戻り値や記録番号に寄り、欠落名は展開追跡再欠落です。 D: 展開追跡再流用は別カテゴリの確認であり、排除名は展開追跡再流用です。展開追跡再初出では V WLM 命令を MVS オペレータコマンドの運用手順で確認し、初出名は展開追跡再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換照合の操作コマンドに関する V WLM,SCHENV=name,ON の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず置換照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. V WLM,SCHENV=name,ON の変更点を出力本文から切り離して置換照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換照合の操作コマンドにおいて選択記号 D を採用し、識別名は置換照合です。置換照合の操作コマンドにおいて V WLM,SCHENV=name,ON は説明欄の「V WLM,SCHENV=name,ON の状態と出力メッセージを結び付ける置換照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合の操作コマンドに関する記録は、V WLM,SCHENV=name,ON の出力行と IEE115I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため置換照合ではありません。 B: 置換照合の操作コマンドは別カテゴリの確認を流用しており、V WLM,SCHENV=name,ON の根拠にならないため置換照合ではありません。 C: 置換照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合の操作コマンドで記録する V WLM,SCHENV=name,ON はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は置換照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V WLM,SCHENV=name,ON</strong></p><p>検証目的: 警告整理の操作コマンドについて、V WLM,SCHENV=name,ON は、スケジューリング環境をオン状態 (リソース利用可能) にし、待機ジョブを実行可能化するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020117の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV WLM,SCHENV=name,を指定し、OSKB020117の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V WLM,SCHENV=name,
CASE OSKB020117
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V WLM,SCHENV=name,
CASE OSKB020117
SOURCE z/OS MVS Operations
V WLM,SCHENV=name,とOSKB020117が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020117を同じ出力で読み、警告整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020117
→ Enter を押す
［画面・出力］
IEE115I OSKB020117 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020117   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020117が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V WLM,SCHENV=name, と OSKB020117 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020117 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## V XCF


<section class="kb-item" id="c22-i0297"><h3>V XCF,sysname,OFFLINE</h3><p class="kb-meta">分類: V XCF ・ 難易度: 中級</p><p>V XCF,sysname,OFFLINEは、MVS オペレータコマンドのV XCFで確認する項目です。Sysplex から指定システムを除外する。SYSGONE 状態へ遷移し、Couple DS の再構成が走る</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書追跡再の操作コマンドで操作コマンドの運用確認を行います。V XCF 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書追跡再の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書追跡再の操作コマンドを正常終了として記録する。</li><li>C. IEE115I を含む表示を保存し、説明欄との差分を上書追跡再で確認する。 <span class="kb-ok">✅ 正解</span></li><li>D. V XCF 命令の属性行を読まず上書追跡再の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書追跡再正解では選択記号 C を採用し、正解名は上書追跡再正解です。上書追跡再根拠では V XCF 命令 は「z/OS MVS Operationsで V XCF 命令の扱いを記録する上書追跡再項目」と D A,L または該当パネルの出力を照合し、根拠名は上書追跡再根拠です。上書追跡再受渡では V XCF 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は上書追跡再受渡です。不適切な選択肢を整理します。 A: 上書追跡再流用は別カテゴリの確認であり、排除名は上書追跡再流用です。 B: 上書追跡再欠落は戻り値や記録番号に寄り、欠落名は上書追跡再欠落です。 C: 上書追跡再正答は対象出力と項目説明を結び、根拠名は上書追跡再正答です。 D: 上書追跡再不足は名称や説明だけに寄り、判定名は上書追跡再不足です。上書追跡再資料では V XCF 命令の使い方を出典欄から追跡し、資料名は上書追跡再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件照合の操作コマンドに関係する V XCF,sysname,OFFLINE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. V XCF,sysname,OFFLINE の名称と担当者名のみを残して条件照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で条件照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず条件照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 条件照合の操作コマンドにおいて選択記号 A を採用し、識別名は条件照合です。条件照合の操作コマンドにおいて V XCF,sysname,OFFLINE は説明欄の「V XCF,sysname,OFFLINE の用途を操作コマンドの表示で確認する条件照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の操作コマンドに関連して、z/OS MVS Operationsでは V XCF,sysname,OFFLINE の表示属性と IEE115I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の操作コマンドは別カテゴリの確認を流用しており、V XCF,sysname,OFFLINE の根拠にならないため条件照合ではありません。 D: 条件照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため条件照合ではありません。条件照合の操作コマンドで使う V XCF,sysname,OFFLINE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は条件照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>V XCF,sysname,OFFLINE</strong></p><p>検証目的: 展開追跡の操作コマンドについて、V XCF,sysname,OFFLINE は、MVS オペレータコマンドの V XCF で確認する項目です。Sysplex から指定システムを除外する。SYSGONE 状態へ遷に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040042の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、展開追跡の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV XCF,sysname,OFFLを指定し、OSKB040042の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V XCF,sysname,OFFL
CASE OSKB040042
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V XCF,sysname,OFFL
CASE OSKB040042
SOURCE z/OS MVS Operations
V XCF,sysname,OFFLとOSKB040042が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040042を同じ出力で読み、展開追跡の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040042
→ Enter を押す
［画面・出力］
IEE115I OSKB040042 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040042   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040042が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V XCF,sysname,OFFL と OSKB040042 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040042 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>V XCF,sysname,OFFLINE</strong></p><p>検証目的: 展開確認の操作コマンドについて、V XCF,sysname,OFFLINE は、MVS オペレータコマンドの V XCF で確認する項目です。Sysplex から指定システムを除外する。SYSGONE 状態へ遷に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030002の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV XCF,sysname,OFFLを指定し、OSKB030002の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V XCF,sysname,OFFL
CASE OSKB030002
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V XCF,sysname,OFFL
CASE OSKB030002
SOURCE z/OS MVS Operations
V XCF,sysname,OFFLとOSKB030002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030002を同じ出力で読み、展開確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030002
→ Enter を押す
［画面・出力］
IEE115I OSKB030002 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030002   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V XCF,sysname,OFFL と OSKB030002 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## V dev


<section class="kb-item" id="c22-i0298"><h3>V (devnum1,devnum2,...) 複数指定</h3><p class="kb-meta">分類: V dev ・ 難易度: 中級</p><p>V (devnum1,devnum2,...) 複数指定は、MVS オペレータコマンドのV devで確認する項目です。複数装置を 1 コマンドで同時に状態変更する形式。範囲指定はカッコ内のリストで行う</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序確認のなど 複で操作コマンドの運用確認を行います。V (devnum1,devnum2,など) 複の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で順序確認のなど 複を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず順序確認のなど 複を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、順序確認の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. V (devnum1,devnum2,など) 複の属性行を読まず順序確認のなど 複の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 順序確認のなど 複において選択記号 C を採用し、識別名は順序確認です。順序確認のなど 複において V (devnum1,devnum2,など) 複 は説明欄の「z/OS MVS Operationsで V (devnum1,devnum2,など) 複の扱いを記録する順序確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認のなど 複を受け取る担当者は、V (devnum1,devnum2,など) 複の表示結果と IEE115I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認のなど 複は別カテゴリの確認を流用しており、V (devnum1,devnum2,など) 複の根拠にならないため順序確認ではありません。 B: 順序確認のなど 複は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため順序確認ではありません。 C: 順序確認のなど 複は対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認のなど 複は名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認のなど 複が示す V (devnum1,devnum2,など) 複は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details></section>


<section class="kb-item" id="c22-i0299"><h3>V devnum,OFFLINE</h3><p class="kb-meta">分類: V dev ・ 難易度: 中級</p><p>V devnum,OFFLINEは、MVS オペレータコマンドのV devで確認する項目です。指定装置をオフラインにする。ALLOC 中の装置はオフライン保留状態 (BOX) となる場合あり</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲照合再の操作コマンドで操作コマンドの運用確認を行います。V devnum 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲照合再の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず範囲照合再の操作コマンドを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、範囲照合再の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. V devnum 命令の属性行を読まず範囲照合再の操作コマンドの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 範囲照合再正解では選択記号 C を採用し、正解名は範囲照合再正解です。範囲照合再根拠では V devnum 命令 は「z/OS MVS Operationsで V devnum 命令の扱いを記録する範囲照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は範囲照合再根拠です。範囲照合再受渡では V devnum 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は範囲照合再受渡です。不適切な選択肢を整理します。 A: 範囲照合再流用は別カテゴリの確認であり、排除名は範囲照合再流用です。 B: 範囲照合再欠落は戻り値や記録番号に寄り、欠落名は範囲照合再欠落です。 C: 範囲照合再正答は対象出力と項目説明を結び、根拠名は範囲照合再正答です。 D: 範囲照合再不足は名称や説明だけに寄り、判定名は範囲照合再不足です。範囲照合再資料では V devnum 命令の使い方を出典欄から追跡し、資料名は範囲照合再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 記録確認の操作コマンドに関係する V devnum,OFFLINE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、記録確認として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. V devnum,OFFLINE の名称と担当者名のみを残して記録確認の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で記録確認の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録確認の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録確認の操作コマンドにおいて選択記号 A を採用し、識別名は記録確認です。記録確認の操作コマンドにおいて V devnum,OFFLINE は説明欄の「V devnum,OFFLINE の用途を操作コマンドの表示で確認する記録確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認の操作コマンドに関連して、z/OS MVS Operationsでは V devnum,OFFLINE の表示属性と IEE115I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認の操作コマンドは別カテゴリの確認を流用しており、V devnum,OFFLINE の根拠にならないため記録確認ではありません。 D: 記録確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため記録確認ではありません。記録確認の操作コマンドで使う V devnum,OFFLINE という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は記録確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V devnum,OFFLINE</strong></p><p>検証目的: 探索整理の操作コマンドについて、V devnum,OFFLINE は、MVS オペレータコマンドの V devで確認する項目です。指定装置をオフラインにする。ALLOC 中の装置はオフライン保留状態 (BOXに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020106の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV devnum,OFFLINEを指定し、OSKB020106の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V devnum,OFFLINE
CASE OSKB020106
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V devnum,OFFLINE
CASE OSKB020106
SOURCE z/OS MVS Operations
V devnum,OFFLINEとOSKB020106が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020106を同じ出力で読み、探索整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020106
→ Enter を押す
［画面・出力］
IEE115I OSKB020106 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020106   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020106が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V devnum,OFFLINE と OSKB020106 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020106 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0300"><h3>V devnum,OFFLINE,FORCE</h3><p class="kb-meta">分類: V dev ・ 難易度: 中級</p><p>V devnum,OFFLINE,FORCEは、MVS オペレータコマンドのV devで確認する項目です。ALLOC 中でも強制オフライン化する。データセット破損リスクがあるため緊急時に限定</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先照合再の操作コマンドに関する V devnum 命令の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先照合再の操作コマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先照合再の操作コマンドの証跡として保存して根拠にする。</li><li>C. V devnum 命令の変更点を出力本文から切り離して優先照合再の操作コマンドの承認欄だけ残す。</li><li>D. 対象の出力行とメッセージ接頭辞を同時に記録し、優先照合再で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先照合再正解では選択記号 D を採用し、正解名は優先照合再正解です。優先照合再根拠では V devnum 命令 は「V devnum 命令の状態と出力メッセージを結び付ける優先照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は優先照合再根拠です。優先照合再保存では V devnum 命令の出力行と IEE115I を一緒に残し、保存名は優先照合再保存です。選択肢ごとの違いを示します。 A: 優先照合再欠落は戻り値や記録番号に寄り、欠落名は優先照合再欠落です。 B: 優先照合再流用は別カテゴリの確認であり、排除名は優先照合再流用です。 C: 優先照合再不足は名称や説明だけに寄り、判定名は優先照合再不足です。 D: 優先照合再正答は対象出力と項目説明を結び、根拠名は優先照合再正答です。優先照合再対象では V devnum 命令をz/OS MVS Operationsの確認記録に残し、対象名は優先照合再対象です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 比較確認の操作コマンドで V devnum,OFFLINE,FORCE の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V devnum,OFFLINE,FORCE の出力を取らず比較確認の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、比較確認の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較確認の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較確認の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較確認の操作コマンドにおいて選択記号 B を採用し、識別名は比較確認です。比較確認の操作コマンドにおいて V devnum,OFFLINE,FORCE は説明欄の「比較確認の操作コマンドに関係する定義値と表示行を照合する比較確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は比較確認です。比較確認の操作コマンドの証跡を読む担当者は、V devnum,OFFLINE,FORCE の属性行と IEE115I を合わせて追跡し、背景名は比較確認です。誤答側の問題点を分けます。 A: 比較確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため比較確認ではありません。 B: 比較確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので比較確認です。 C: 比較確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため比較確認ではありません。 D: 比較確認の操作コマンドは別カテゴリの確認を流用しており、V devnum,OFFLINE,FORCE の根拠にならないため比較確認ではありません。比較確認の操作コマンドに出る V devnum,OFFLINE,FORCE は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は比較確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V devnum,OFFLINE,FORCE</strong></p><p>検証目的: 上書整理の操作コマンドについて、V devnum,OFFLINE,FORCE は、MVS オペレータコマンドの V devで確認する項目です。ALLOC 中でも強制オフライン化する。データセット破損リスクがあに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020107の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV devnum,OFFLINE,Fを指定し、OSKB020107の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V devnum,OFFLINE,F
CASE OSKB020107
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V devnum,OFFLINE,F
CASE OSKB020107
SOURCE z/OS MVS Operations
V devnum,OFFLINE,FとOSKB020107が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020107を同じ出力で読み、上書整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020107
→ Enter を押す
［画面・出力］
IEE115I OSKB020107 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020107   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020107が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V devnum,OFFLINE,F と OSKB020107 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020107 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0301"><h3>V devnum,ONLINE</h3><p class="kb-meta">分類: V dev ・ 難易度: 中級</p><p>V devnum,ONLINEは、MVS オペレータコマンドのV devで確認する項目です。指定装置 (DASD / TAPE / 端末 / プリンタ) をオンライン化する。VOLSER 認識と UCB 状態の正常化が同時に走る</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切照合再の操作コマンドで V devnum,ONLINE の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V devnum,ONLINE の出力を取らず区切照合再の操作コマンドの説明文と承認印だけを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、区切照合再の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して区切照合再の操作コマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切照合再の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 区切照合再正解では選択記号 B を採用し、正解名は区切照合再正解です。区切照合再根拠では V devnum,ONLINE は「区切照合再の操作コマンドに関係する定義値と表示行を照合する区切照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は区切照合再根拠です。区切照合再追跡では V devnum,ONLINE の属性行と IEE115I を合わせ、追跡名は区切照合再追跡です。誤答側の問題点を分けます。 A: 区切照合再不足は名称や説明だけに寄り、判定名は区切照合再不足です。 B: 区切照合再正答は対象出力と項目説明を結び、根拠名は区切照合再正答です。 C: 区切照合再欠落は戻り値や記録番号に寄り、欠落名は区切照合再欠落です。 D: 区切照合再流用は別カテゴリの確認であり、排除名は区切照合再流用です。区切照合再初出では V devnum,ONLINE を MVS オペレータコマンドの運用手順で確認し、初出名は区切照合再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 優先確認の操作コマンドに関する V devnum,ONLINE の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず優先確認の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先確認の操作コマンドの証跡として保存して根拠にする。</li><li>C. V devnum,ONLINE の変更点を出力本文から切り離して優先確認の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 優先確認の操作コマンドにおいて選択記号 D を採用し、識別名は優先確認です。優先確認の操作コマンドにおいて V devnum,ONLINE は説明欄の「V devnum,ONLINE の状態と出力メッセージを結び付ける優先確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認の操作コマンドに関する記録は、V devnum,ONLINE の出力行と IEE115I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため優先確認ではありません。 B: 優先確認の操作コマンドは別カテゴリの確認を流用しており、V devnum,ONLINE の根拠にならないため優先確認ではありません。 C: 優先確認の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認の操作コマンドは対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認の操作コマンドで記録する V devnum,ONLINE はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は優先確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V devnum,ONLINE</strong></p><p>検証目的: 終端整理の操作コマンドについて、V devnum,ONLINE は、MVS オペレータコマンドの V devで確認する項目です。指定装置 (DASD / TAPE / 端末 / プリンタ) をオンライン化するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020105の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、終端整理の操作コマンドの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV devnum,ONLINEを指定し、OSKB020105の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V devnum,ONLINE
CASE OSKB020105
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V devnum,ONLINE
CASE OSKB020105
SOURCE z/OS MVS Operations
V devnum,ONLINEとOSKB020105が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020105を同じ出力で読み、終端整理の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020105
→ Enter を押す
［画面・出力］
IEE115I OSKB020105 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020105   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020105が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V devnum,ONLINE と OSKB020105 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020105 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0302"><h3>V devnum-devnum,ONLINE 範囲</h3><p class="kb-meta">分類: V dev ・ 難易度: 中級</p><p>V devnum-devnum,ONLINE 範囲は、MVS オペレータコマンドのV devで確認する項目です。ハイフン区切りで連続装置範囲を一括オンライン化する</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較照合再の範で V devnum-devnum 命令の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. V devnum-devnum 命令の出力を取らず比較照合再の範の説明文と承認印だけを残す。</li><li>B. 参照資料名、表示行、メッセージをそろえて比較照合再の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して比較照合再の範の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較照合再の範へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 比較照合再正解では選択記号 B を採用し、正解名は比較照合再正解です。比較照合再根拠では V devnum-devnum 命令 は「比較照合再の範に関係する定義値と表示行を照合する比較照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は比較照合再根拠です。比較照合再追跡では V devnum-devnum 命令の属性行と IEE115I を合わせ、追跡名は比較照合再追跡です。誤答側の問題点を分けます。 A: 比較照合再不足は名称や説明だけに寄り、判定名は比較照合再不足です。 B: 比較照合再正答は対象出力と項目説明を結び、根拠名は比較照合再正答です。 C: 比較照合再欠落は戻り値や記録番号に寄り、欠落名は比較照合再欠落です。 D: 比較照合再流用は別カテゴリの確認であり、排除名は比較照合再流用です。比較照合再初出では V devnum-devnum 命令を MVS オペレータコマンドの運用手順で確認し、初出名は比較照合再初出です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 値域確認の範に関する V devnum-devnum,ONLINE 範の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域確認の範の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域確認の範の証跡として保存して根拠にする。</li><li>C. V devnum-devnum,ONLINE 範の変更点を出力本文から切り離して値域確認の範の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、値域確認の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域確認の範において選択記号 D を採用し、識別名は値域確認です。値域確認の範において V devnum-devnum,ONLINE 範 は説明欄の「V devnum-devnum,ONLINE 範の状態と出力メッセージを結び付ける値域確認項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認の範に関する記録は、V devnum-devnum,ONLINE 範の出力行と IEE115I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認の範は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域確認ではありません。 B: 値域確認の範は別カテゴリの確認を流用しており、V devnum-devnum,ONLINE 範の根拠にならないため値域確認ではありません。 C: 値域確認の範は名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認の範は対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認の範で記録する V devnum-devnum,ONLINE 範はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域確認です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>V devnum-devnum,ONLINE 範囲</strong></p><p>検証目的: 条件整理の範について、V devnum-devnum,ONLINE 範囲は、MVS オペレータコマンドの V devで確認する項目です。ハイフン区切りで連続装置範囲を一括オンライン化するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020109の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、条件整理の範の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV devnum-devnum,ONを指定し、OSKB020109の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V devnum-devnum,ON
CASE OSKB020109
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V devnum-devnum,ON
CASE OSKB020109
SOURCE z/OS MVS Operations
V devnum-devnum,ONとOSKB020109が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020109を同じ出力で読み、条件整理の範の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020109
→ Enter を押す
［画面・出力］
IEE115I OSKB020109 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020109   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020109が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V devnum-devnum,ON と OSKB020109 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020109 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## WTOR


<section class="kb-item" id="c22-i0303"><h3>DESC コード (Descriptor)</h3><p class="kb-meta">分類: WTOR ・ 難易度: 中級</p><p>WTO/WTOR メッセージの DESC=(n,...) は意味分類 (アクション要請、エラー、ジョブ状況等) を表す。MPF 自動化条件に使用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端検査のコードに関係する DESC コード (Descriptor)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端検査として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. DESC コード (Descriptor)の名称と担当者名のみを残して終端検査のコードの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で終端検査のコードを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず終端検査のコードの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 終端検査のコードにおいて選択記号 A を採用し、識別名は終端検査です。終端検査のコードにおいて DESC コード (Descriptor) は説明欄の「WTO/WTOR メッセージの DESC=(n,など) は意味分類 (アクション要請、エラー、ジョブ状況等) を表す。MPF 自動化条件に使」と D A,L または該当パネルの出力を照合する対象で、答え名は終端検査です。終端検査のコードに関連して、z/OS MVS Operationsでは DESC コード (Descriptor)の表示属性と IEE115I を同じ証跡に残し、背景名は終端検査です。他の選択肢を確認します。 A: 終端検査のコードは対象出力と項目説明を結び、根拠を残すので終端検査です。 B: 終端検査のコードは名称や説明のみに寄り、状態を示す出力本文が不足するため終端検査ではありません。 C: 終端検査のコードは別カテゴリの確認を流用しており、DESC コード (Descriptor)の根拠にならないため終端検査ではありません。 D: 終端検査のコードは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため終端検査ではありません。終端検査のコードで使う DESC コード (Descriptor)という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は終端検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>DESC コード (Descriptor)</strong></p><p>検証目的: 出力追跡のコードについて、WTO/WTOR メッセージの DESC=(n,など) は意味分類 (アクション要請、エラー、ジョブ状況等) を表す。MPF 自動化条件に使用に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040048の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力追跡のコードの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にDESC コード (Descriptを指定し、OSKB040048の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND DESC コード (Descript
CASE OSKB040048
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM DESC コード (Descript
CASE OSKB040048
SOURCE z/OS MVS Operations
DESC コード (DescriptとOSKB040048が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB040048を同じ出力で読み、出力追跡のコードの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB040048
→ Enter を押す
［画面・出力］
IEE115I OSKB040048 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040048   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB040048が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の DESC コード (Descript と OSKB040048 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB040048 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>DESC コード (Descriptor)</strong></p><p>検証目的: 復旧照合のコードについて、WTO/WTOR メッセージの DESC=(n,など) は意味分類 (アクション要請、エラー、ジョブ状況等) を表す。MPF 自動化条件に使用に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030038の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、復旧照合のコードの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にDESC コード (Descriptを指定し、OSKB030038の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND DESC コード (Descript
CASE OSKB030038
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM DESC コード (Descript
CASE OSKB030038
SOURCE z/OS MVS Operations
DESC コード (DescriptとOSKB030038が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030038を同じ出力で読み、復旧照合のコードの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030038
→ Enter を押す
［画面・出力］
IEE115I OSKB030038 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030038   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030038が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の DESC コード (Descript と OSKB030038 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030038 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0304"><h3>ROUTCDE (ルート・コード)</h3><p class="kb-meta">分類: WTOR ・ 難易度: 中級</p><p>WTO/WTOR の配信先カテゴリ (MASTER, TAPE LIB, PROD CONTROL 等)。コンソールの ROUTCDE と一致したものを受信</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索検査のルート・コードで ROUTCDE (ルート・コード)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. ROUTCDE (ルート・コード)の出力を取らず探索検査のルート・コードの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索検査の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して探索検査のルート・コードの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索検査のルート・コードへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 探索検査のルート・コードにおいて選択記号 B を採用し、識別名は探索検査です。探索検査のルート・コードにおいて ROUTCDE (ルート・コード) は説明欄の「探索検査のルート・コードに関係する定義値と表示行を照合する探索検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は探索検査です。探索検査のルート・コードの証跡を読む担当者は、ROUTCDE (ルート・コード)の属性行と IEE115I を合わせて追跡し、背景名は探索検査です。誤答側の問題点を分けます。 A: 探索検査のルート・コードは名称や説明のみに寄り、状態を示す出力本文が不足するため探索検査ではありません。 B: 探索検査のルート・コードは対象出力と項目説明を結び、根拠を残すので探索検査です。 C: 探索検査のルート・コードは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため探索検査ではありません。 D: 探索検査のルート・コードは別カテゴリの確認を流用しており、ROUTCDE (ルート・コード)の根拠にならないため探索検査ではありません。探索検査のルート・コードに出る ROUTCDE (ルート・コード)は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は探索検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ROUTCDE (ルート・コード)</strong></p><p>検証目的: 監査照合のルート・コードについて、WTO/WTOR の配信先カテゴリ (MASTER, TAPE LIB, PROD CONTROL 等)。コンソールの ROUTCDE と一致したものを受信に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030039の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、監査照合のルート・コードの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にROUTCDE (ルート・コード)を指定し、OSKB030039の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND ROUTCDE (ルート・コード)
CASE OSKB030039
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM ROUTCDE (ルート・コード)
CASE OSKB030039
SOURCE z/OS MVS Operations
ROUTCDE (ルート・コード)とOSKB030039が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030039を同じ出力で読み、監査照合のルート・コードの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030039
→ Enter を押す
［画面・出力］
IEE115I OSKB030039 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030039   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030039が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の ROUTCDE (ルート・コード) と OSKB030039 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030039 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0305"><h3>WTOR メッセージの保持</h3><p class="kb-meta">分類: WTOR ・ 難易度: 中級</p><p>WTOR メッセージの保持は、MVS オペレータコマンドのWTORで確認する項目です。WTOR は応答が来るまで OS 内に保持され、再表示要求 (K M,REF) で再描画できる</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力検査のメッセージの保持に関する WTOR メッセージの保持の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず出力検査のメッセージの保持の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力検査のメッセージの保持の証跡として保存して根拠にする。</li><li>C. WTOR メッセージの保持の変更点を出力本文から切り離して出力検査のメッセージの保持の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力検査の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 出力検査のメッセージの保持において選択記号 D を採用し、識別名は出力検査です。出力検査のメッセージの保持において WTOR メッセージの保持 は説明欄の「WTOR メッセージの保持の状態と出力メッセージを結び付ける出力検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は出力検査です。出力検査のメッセージの保持に関する記録は、WTOR メッセージの保持の出力行と IEE115I を一緒に保存し、背景名は出力検査です。選択肢ごとの違いを示します。 A: 出力検査のメッセージの保持は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため出力検査ではありません。 B: 出力検査のメッセージの保持は別カテゴリの確認を流用しており、WTOR メッセージの保持の根拠にならないため出力検査ではありません。 C: 出力検査のメッセージの保持は名称や説明のみに寄り、状態を示す出力本文が不足するため出力検査ではありません。 D: 出力検査のメッセージの保持は対象出力と項目説明を結び、根拠を残すので出力検査です。出力検査のメッセージの保持で記録する WTOR メッセージの保持はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は出力検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WTOR メッセージの保持</strong></p><p>検証目的: 構文追跡のメッセージの保持について、WTOR メッセージの保持は、MVS オペレータコマンドの WTOR で確認する項目です。WTOR は応答が来るまで OS 内に保持され、再表示要求 (K M,REF) で再描に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030041の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、構文追跡のメッセージの保持の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にWTOR メッセージの保持を指定し、OSKB030041の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND WTOR メッセージの保持
CASE OSKB030041
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM WTOR メッセージの保持
CASE OSKB030041
SOURCE z/OS MVS Operations
WTOR メッセージの保持とOSKB030041が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030041を同じ出力で読み、構文追跡のメッセージの保持の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030041
→ Enter を押す
［画面・出力］
IEE115I OSKB030041 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030041   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030041が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の WTOR メッセージの保持 と OSKB030041 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030041 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0306"><h3>応答番号 (reply ID) の上限</h3><p class="kb-meta">分類: WTOR ・ 難易度: 中級</p><p>未応答 WTOR の同時保持上限は IEACMD/CONSOLxx の REPLY 制限に依存。閾値超えはシステム障害化のリスク</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書検査の応答番号 の上限で操作コマンドの運用確認を行います。応答番号 (reply ID) の上限の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で上書検査の応答番号 の上限を確認した扱いにする。</li><li>B. IEE115I の有無を確認せず上書検査の応答番号 の上限を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書検査の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. 応答番号 (reply ID) の上限の属性行を読まず上書検査の応答番号 の上限の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 上書検査の応答番号 の上限において選択記号 C を採用し、識別名は上書検査です。上書検査の応答番号 の上限において応答番号 (reply ID) の上限 は説明欄の「z/OS MVS Operationsで応答番号 (reply ID) の上限の扱いを記録する上書検査項目」と D A,L または該当パネルの出力を照合する対象で、答え名は上書検査です。上書検査の応答番号 の上限を受け取る担当者は、応答番号 (reply ID) の上限の表示結果と IEE115I を同じ確認単位として扱い、背景名は上書検査です。不適切な選択肢を整理します。 A: 上書検査の応答番号 の上限は別カテゴリの確認を流用しており、応答番号 (reply ID) の上限の根拠にならないため上書検査ではありません。 B: 上書検査の応答番号 の上限は戻り値や記録番号に寄り、IEE115I や属性表示を落とすため上書検査ではありません。 C: 上書検査の応答番号 の上限は対象出力と項目説明を結び、根拠を残すので上書検査です。 D: 上書検査の応答番号 の上限は名称や説明のみに寄り、状態を示す出力本文が不足するため上書検査ではありません。上書検査の応答番号 の上限が示す応答番号 (reply ID) の上限は出典欄の資料で使い方を追跡できる項目であり、用語名は上書検査です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>応答番号 (reply ID) の上限</strong></p><p>検証目的: 変更照合の応答番号 の上限について、未応答 WTOR の同時保持上限は IEACMD/CONSOLxx の REPLY 制限に依存。閾値超えはシステム障害化のリスクに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030040の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、変更照合の応答番号 の上限の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄に応答番号 (reply ID) の上を指定し、OSKB030040の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND 応答番号 (reply ID) の上
CASE OSKB030040
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM 応答番号 (reply ID) の上
CASE OSKB030040
SOURCE z/OS MVS Operations
応答番号 (reply ID) の上とOSKB030040が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030040を同じ出力で読み、変更照合の応答番号 の上限の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030040
→ Enter を押す
［画面・出力］
IEE115I OSKB030040 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030040   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030040が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の 応答番号 (reply ID) の上 と OSKB030040 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030040 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## Z


<section class="kb-item" id="c22-i0307"><h3>Z EOD</h3><p class="kb-meta">分類: Z ・ 難易度: 中級</p><p>Z EODは、MVS オペレータコマンドのZで状態表示や操作を行うためのコマンド関連項目です。End-Of-Day の意で、SMF / LOGREC / SYSLOG / ハードコピーのデータをフラッシュし、停止前の整合性を取る。IPL 前に必須</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域照合の操作コマンドに関する Z EOD の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. D A,L の結果を残さず値域照合の操作コマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域照合の操作コマンドの証跡として保存して根拠にする。</li><li>C. Z EOD の変更点を出力本文から切り離して値域照合の操作コマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、値域照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 値域照合の操作コマンドにおいて選択記号 D を採用し、識別名は値域照合です。値域照合の操作コマンドにおいて Z EOD は説明欄の「Z EOD の状態と出力メッセージを結び付ける値域照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の操作コマンドに関する記録は、Z EOD の出力行と IEE115I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため値域照合ではありません。 B: 値域照合の操作コマンドは別カテゴリの確認を流用しており、Z EOD の根拠にならないため値域照合ではありません。 C: 値域照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の操作コマンドで記録する Z EOD はz/OS MVS Operationsの確認記録に残す対象名であり、用語名は値域照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Z EOD</strong></p><p>検証目的: 条件確認の操作コマンドについて、Z EOD は、MVS オペレータコマンドの Z で状態表示や操作を行うためのコマンド関連項目です。End-Of-Day の意で、SMF / LOGREC / SYSLOG /に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030009の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にZ EODを指定し、OSKB030009の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND Z EOD
CASE OSKB030009
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM Z EOD
CASE OSKB030009
SOURCE z/OS MVS Operations
Z EODとOSKB030009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030009を同じ出力で読み、条件確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030009
→ Enter を押す
［画面・出力］
IEE115I OSKB030009 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030009   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の Z EOD と OSKB030009 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0308"><h3>Z NET</h3><p class="kb-meta">分類: Z ・ 難易度: 中級</p><p>Z NETは、MVS オペレータコマンドのZで確認する項目です。VTAM を停止する標準形式。すべてのセッション・APPL を正常クローズしてから停止</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告照合の操作コマンドに関係する Z NET の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、警告照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. Z NET の名称と担当者名のみを残して警告照合の操作コマンドの表示本文を確認対象に含めない。</li><li>C. 操作コマンド以外の画面で警告照合の操作コマンドを確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず警告照合の操作コマンドの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 警告照合の操作コマンドにおいて選択記号 A を採用し、識別名は警告照合です。警告照合の操作コマンドにおいて Z NET は説明欄の「Z NET の用途を操作コマンドの表示で確認する警告照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合の操作コマンドに関連して、z/OS MVS Operationsでは Z NET の表示属性と IEE115I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合の操作コマンドは別カテゴリの確認を流用しており、Z NET の根拠にならないため警告照合ではありません。 D: 警告照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため警告照合ではありません。警告照合の操作コマンドで使う Z NET という用語は MVS オペレータコマンドで扱う確認対象であり、用語名は警告照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Z NET</strong></p><p>検証目的: 区切確認の操作コマンドについて、Z NET は、MVS オペレータコマンドの Z で確認する項目です。VTAM を停止する標準形式。すべてのセッション・ APPL を正常クローズしてから停止に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030010の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にZ NETを指定し、OSKB030010の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND Z NET
CASE OSKB030010
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM Z NET
CASE OSKB030010
SOURCE z/OS MVS Operations
Z NETとOSKB030010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030010を同じ出力で読み、区切確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030010
→ Enter を押す
［画面・出力］
IEE115I OSKB030010 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030010   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の Z NET と OSKB030010 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0309"><h3>Z NET,CANCEL</h3><p class="kb-meta">分類: Z ・ 難易度: 中級</p><p>Z NET,CANCELは、MVS オペレータコマンドのZで確認する項目です。VTAM の全セッションを即時キャンセルして停止する最も強い形式</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査照合の操作コマンドで操作コマンドの運用確認を行います。Z NET,CANCEL の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査照合の操作コマンドを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査照合の操作コマンドを正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、監査照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. Z NET,CANCEL の属性行を読まず監査照合の操作コマンドの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査照合の操作コマンドにおいて選択記号 C を採用し、識別名は監査照合です。監査照合の操作コマンドにおいて Z NET,CANCEL は説明欄の「z/OS MVS Operationsで Z NET,CANCEL の扱いを記録する監査照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合の操作コマンドを受け取る担当者は、Z NET,CANCEL の表示結果と IEE115I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合の操作コマンドは別カテゴリの確認を流用しており、Z NET,CANCEL の根拠にならないため監査照合ではありません。 B: 監査照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため監査照合ではありません。 C: 監査照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合の操作コマンドが示す Z NET,CANCEL は出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Z NET,CANCEL</strong></p><p>検証目的: 優先確認の操作コマンドについて、Z NET,CANCEL は、MVS オペレータコマンドの Z で確認する項目です。VTAM の全セッションを即時キャンセルして停止する最も強い形式に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030012の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にZ NET,CANCELを指定し、OSKB030012の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND Z NET,CANCEL
CASE OSKB030012
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM Z NET,CANCEL
CASE OSKB030012
SOURCE z/OS MVS Operations
Z NET,CANCELとOSKB030012が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030012を同じ出力で読み、優先確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030012
→ Enter を押す
［画面・出力］
IEE115I OSKB030012 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030012   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030012が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の Z NET,CANCEL と OSKB030012 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030012 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


<section class="kb-item" id="c22-i0310"><h3>Z NET,QUICK</h3><p class="kb-meta">分類: Z ・ 難易度: 中級</p><p>Z NET,QUICKは、MVS オペレータコマンドのZで確認する項目です。VTAM を即時停止 (セッション正常クローズなし) する形式。緊急時のみ使用</p><p class="kb-src"><strong>出典:</strong> z / OS MVS System Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧照合の操作コマンドで Z NET,QUICK の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. Z NET,QUICK の出力を取らず復旧照合の操作コマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、復旧照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. D A,L を省略して復旧照合の操作コマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧照合の操作コマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 復旧照合の操作コマンドにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合の操作コマンドにおいて Z NET,QUICK は説明欄の「復旧照合の操作コマンドに関係する定義値と表示行を照合する復旧照合項目」と D A,L または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合の操作コマンドの証跡を読む担当者は、Z NET,QUICK の属性行と IEE115I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合の操作コマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合の操作コマンドは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合の操作コマンドは戻り値や記録番号に寄り、IEE115I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合の操作コマンドは別カテゴリの確認を流用しており、Z NET,QUICK の根拠にならないため復旧照合ではありません。復旧照合の操作コマンドに出る Z NET,QUICK は MVS オペレータコマンドの運用手順で意味を確認する対象であり、用語名は復旧照合です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Z NET,QUICK</strong></p><p>検証目的: 範囲確認の操作コマンドについて、Z NET,QUICK は、MVS オペレータコマンドの Z で確認する項目です。VTAM を即時停止 (セッション正常クローズなし) する形式。緊急時のみ使用に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030011の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
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
現在の画面はMVS Consoleの表示結果です。FIND欄にZ NET,QUICKを指定し、OSKB030011の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND Z NET,QUICK
CASE OSKB030011
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM Z NET,QUICK
CASE OSKB030011
SOURCE z/OS MVS Operations
Z NET,QUICKとOSKB030011が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030011を同じ出力で読み、範囲確認の操作コマンドの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030011
→ Enter を押す
［画面・出力］
IEE115I OSKB030011 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030011   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030011が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の Z NET,QUICK と OSKB030011 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030011 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>


## その他


<section class="kb-item" id="c22-other"><h3>その他（特定項目に紐づかないQA・手順）</h3><p class="kb-meta">項目名が個別の技術項目に一致しなかったQA・手順です。</p><details class="kb-block"><summary>確認問題（4問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲検分のなどの不在で操作コマンドの運用確認を行います。S TRACE,などの不在の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で範囲検分のなどの不在を確認した扱いにする。</li><li>B. IEE457I の有無を確認せず範囲検分のなどの不在を正常終了として記録する。</li><li>C. 同じ画面で対象行と IEE457I を読み、範囲検分の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>D. S TRACE,などの不在の属性行を読まず範囲検分のなどの不在の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では S TRACE,などの不在 は「z/OS MVS Operationsで S TRACE,などの不在の扱いを記録する範囲検分項目」と D OPDATA または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では S TRACE,などの不在の表示結果と IEE457I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明だけに寄り、判定名は範囲検分不足です。範囲検分資料では S TRACE,などの不在の使い方を出典欄から追跡し、資料名は範囲検分資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 記録確認再のなど 管理に関係する F NET 命令の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 出典欄の説明と運用出力を照合し、記録確認再の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>B. F NET 命令の名称と担当者名だけを残して記録確認再のなど 管理の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録確認再のなど 管理を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録確認再のなど 管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録確認再正解では選択記号 A を採用し、正解名は記録確認再正解です。記録確認再根拠では F NET 命令 は「F NET 命令の用途を操作コマンドの表示で確認する記録確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は記録確認再根拠です。記録確認再背景ではz/OS MVS Operationsの F NET 命令と IEE115I を同じ証跡に残し、背景名は記録確認再背景です。他の選択肢を確認します。 A: 記録確認再正答は対象出力と項目説明を結び、根拠名は記録確認再正答です。 B: 記録確認再不足は名称や説明だけに寄り、判定名は記録確認再不足です。 C: 記録確認再流用は別カテゴリの確認であり、排除名は記録確認再流用です。 D: 記録確認再欠落は戻り値や記録番号に寄り、欠落名は記録確認再欠落です。記録確認再用語では F NET 命令を MVS オペレータコマンドで扱う確認対象とし、用語名は記録確認再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 監査確認再のなどで操作コマンドの運用確認を行います。F BPXOINIT 命令の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. z/OS MVS Operationsと無関係な一覧で監査確認再のなどを確認した扱いにする。</li><li>B. IEE115I の有無を確認せず監査確認再のなどを正常終了として記録する。</li><li>C. z/OS MVS Operationsの表示形式に沿って根拠行を採り、監査確認再の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. F BPXOINIT 命令の属性行を読まず監査確認再のなどの画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 監査確認再正解では選択記号 C を採用し、正解名は監査確認再正解です。監査確認再根拠では F BPXOINIT 命令 は「z/OS MVS Operationsで F BPXOINIT 命令の扱いを記録する監査確認再項目」と D A,L または該当パネルの出力を照合し、根拠名は監査確認再根拠です。監査確認再受渡では F BPXOINIT 命令の表示結果と IEE115I を同じ確認単位にし、受渡名は監査確認再受渡です。不適切な選択肢を整理します。 A: 監査確認再流用は別カテゴリの確認であり、排除名は監査確認再流用です。 B: 監査確認再欠落は戻り値や記録番号に寄り、欠落名は監査確認再欠落です。 C: 監査確認再正答は対象出力と項目説明を結び、根拠名は監査確認再正答です。 D: 監査確認再不足は名称や説明だけに寄り、判定名は監査確認再不足です。監査確認再資料では F BPXOINIT 命令の使い方を出典欄から追跡し、資料名は監査確認再資料です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div><div class="kb-q"><p><strong>問題.</strong> 記録照合再のなど 複に関係する V 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 机上確認でも実出力の見出しに合わせ、記録照合再の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>B. V 属性の名称と担当者名だけを残して記録照合再のなど 複の表示本文を対象から外す。</li><li>C. 操作コマンド以外の画面で記録照合再のなど 複を確認し同じ証跡として扱ったことにする。</li><li>D. IEE115I の有無を見ず記録照合再のなど 複の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 中級</p><p><strong>解説:</strong> 記録照合再正解では選択記号 A を採用し、正解名は記録照合再正解です。記録照合再根拠では V 属性 は「V 属性の用途を操作コマンドの表示で確認する記録照合再項目」と D A,L または該当パネルの出力を照合し、根拠名は記録照合再根拠です。記録照合再背景ではz/OS MVS Operationsの V 属性と IEE115I を同じ証跡に残し、背景名は記録照合再背景です。他の選択肢を確認します。 A: 記録照合再正答は対象出力と項目説明を結び、根拠名は記録照合再正答です。 B: 記録照合再不足は名称や説明だけに寄り、判定名は記録照合再不足です。 C: 記録照合再流用は別カテゴリの確認であり、排除名は記録照合再流用です。 D: 記録照合再欠落は戻り値や記録番号に寄り、欠落名は記録照合再欠落です。記録照合再用語では V 属性を MVS オペレータコマンドで扱う確認対象とし、用語名は記録照合再用語です。</p><p class="kb-src"><strong>出典:</strong> OS MVS System Commands（zOS31_ieag100） / zOS31_ieam200</p></div></details><details class="kb-block"><summary>検証手順（8件）</summary><div class="kb-p"><p class="kb-pname"><strong>V TCPIP,,VARY,nnnn,など</strong></p><p>検証目的: 呼出追跡のなどについて、V TCPIP,,VARY,nnnn,などは、MVS オペレータコマンドの V TCPIP で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB040043の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、呼出追跡のなどの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV TCPIP,,VARY,nnnnを指定し、OSKB040043の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V TCPIP,,VARY,nnnn
CASE OSKB040043
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V TCPIP,,VARY,nnnn
CASE OSKB040043
SOURCE z/OS MVS Operations
V TCPIP,,VARY,nnnnとOSKB040043が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB040043を同じ出力で読み、呼出追跡のなどの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB040043
→ Enter を押す
［画面・出力］
IEE457I OSKB040043 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB040043   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB040043が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の V TCPIP,,VARY,nnnn と OSKB040043 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB040043 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>S TRACE,などの不在</strong></p><p>検証目的: 探索検査のなどの不在について、トレースは S ではなく TRACE CT,ON / SET TRACE で開始する点に注意。S は使用しないに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020066の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、探索検査のなどの不在の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にS TRACE,などの不在を指定し、OSKB020066の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND S TRACE,などの不在
CASE OSKB020066
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM S TRACE,などの不在
CASE OSKB020066
SOURCE z/OS MVS Operations
S TRACE,などの不在とOSKB020066が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB020066を同じ出力で読み、探索検査のなどの不在の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB020066
→ Enter を押す
［画面・出力］
IEE457I OSKB020066 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020066   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB020066が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の S TRACE,などの不在 と OSKB020066 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB020066 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>F NET,USER,など VTAM 管理</strong></p><p>検証目的: 出力判定のなど 管理について、F NET,USER,など VTAM 管理は、VTAM に対する SNA リソース個別制御 (例: F NET,USER,ID=name,ACT)に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020088の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力判定のなど 管理の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF NET,USER,など VTAMを指定し、OSKB020088の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F NET,USER,など VTAM
CASE OSKB020088
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F NET,USER,など VTAM
CASE OSKB020088
SOURCE z/OS MVS Operations
F NET,USER,など VTAMとOSKB020088が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020088を同じ出力で読み、出力判定のなど 管理の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020088
→ Enter を押す
［画面・出力］
IEE115I OSKB020088 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020088   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020088が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F NET,USER,など VTAM と OSKB020088 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020088 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>F BPXOINIT,FILESYS= など</strong></p><p>検証目的: 比較判定のなどについて、F BPXOINIT,FILESYS= などは、USS ファイルシステムに対する個別操作 (DISPLAY/UNMOUNT/MOVE) を行う MODIFY サブコマンド群に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020094の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、比較判定のなどの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にF BPXOINIT,FILESYSを指定し、OSKB020094の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND F BPXOINIT,FILESYS
CASE OSKB020094
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM F BPXOINIT,FILESYS
CASE OSKB020094
SOURCE z/OS MVS Operations
F BPXOINIT,FILESYSとOSKB020094が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020094を同じ出力で読み、比較判定のなどの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020094
→ Enter を押す
［画面・出力］
IEE115I OSKB020094 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020094   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020094が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の F BPXOINIT,FILESYS と OSKB020094 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020094 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>V (devnum1,devnum2,など) 複数指定</strong></p><p>検証目的: 出力整理のなど 複について、V (devnum1,devnum2,など) 複数指定は、MVS オペレータコマンドの V devで確認する項目です。複数装置を 1 コマンドで同時に状態変更する形式。範囲指に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB020108の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、出力整理のなど 複の確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV (devnum1,devnum2を指定し、OSKB020108の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V (devnum1,devnum2
CASE OSKB020108
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V (devnum1,devnum2
CASE OSKB020108
SOURCE z/OS MVS Operations
V (devnum1,devnum2とOSKB020108が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB020108を同じ出力で読み、出力整理のなど 複の根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB020108
→ Enter を押す
［画面・出力］
IEE115I OSKB020108 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB020108   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB020108が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の V (devnum1,devnum2 と OSKB020108 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB020108 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>V TCPIP,,VARY,nnnn,など</strong></p><p>検証目的: 出力確認のなどについて、V TCPIP,,VARY,nnnn,などは、MVS オペレータコマンドの V TCPIP で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030008の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD OPDATAを実行し、IEE457Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D OPDATA を入力し、出力確認のなどの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にV TCPIP,,VARY,nnnnを指定し、OSKB030008の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND V TCPIP,,VARY,nnnn
CASE OSKB030008
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM V TCPIP,,VARY,nnnn
CASE OSKB030008
SOURCE z/OS MVS Operations
V TCPIP,,VARY,nnnnとOSKB030008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE457IとOSKB030008を同じ出力で読み、出力確認のなどの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D OPDATA
CASE OSKB030008
→ Enter を押す
［画面・出力］
IEE457I OSKB030008 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030008   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE457IとOSKB030008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D OPDATA が画面・出力に表示されること
② ステップ2 の V TCPIP,,VARY,nnnn と OSKB030008 が画面・出力に表示されること
③ ステップ3 の IEE457I と OSKB030008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>ROUTE T=seconds,など</strong></p><p>検証目的: 記録照合のなどについて、ROUTE T=seconds,などは、MVS オペレータコマンドの ROUTE で確認する項目です。応答待ちタイムアウトを指定。Sysplex 内応答が揃わない場合の待ち時間に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030033の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、記録照合のなどの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にROUTE T=seconds,などを指定し、OSKB030033の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND ROUTE T=seconds,など
CASE OSKB030033
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM ROUTE T=seconds,など
CASE OSKB030033
SOURCE z/OS MVS Operations
ROUTE T=seconds,などとOSKB030033が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030033を同じ出力で読み、記録照合のなどの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030033
→ Enter を押す
［画面・出力］
IEE115I OSKB030033 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030033   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030033が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の ROUTE T=seconds,など と OSKB030033 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030033 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>K S,DEL= など</strong></p><p>検証目的: 優先追跡のなどについて、MVS オペレータコマンドの K では、対象資源、指定値、実行時の出力を対応付けて確認します。K は、MVS オペレータコマンドの運用で指定値、構文上の位置、反映後の出力を読み分に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: MVS Consoleまたは関連TSO/コンソールを参照でき、OSKB030052の検証用出力を記録できる。</p><p>セッション環境: MVS ConsoleでD A,Lを実行し、IEE115Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はMVS Consoleのコマンド入力画面です。COMMAND INPUT ===&gt; に D A,L を入力し、優先追跡のなどの確認表示へ進みます。
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
現在の画面はMVS Consoleの表示結果です。FIND欄にK S,DEL= などを指定し、OSKB030052の対象行を見つけます。
［操作（入力）］
(MVS Console Result)
COMMAND INPUT ===&gt; FIND K S,DEL= など
CASE OSKB030052
→ Enter を押す
［画面・出力］
(MVS Console Result)
ITEM K S,DEL= など
CASE OSKB030052
SOURCE z/OS MVS Operations
K S,DEL= などとOSKB030052が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はMVS Consoleの詳細表示です。IEE115IとOSKB030052を同じ出力で読み、優先追跡のなどの根拠を記録します。
［操作（入力）］
(MVS Console Detail)
COMMAND INPUT ===&gt; D A,L
CASE OSKB030052
→ Enter を押す
［画面・出力］
IEE115I OSKB030052 DISPLAY ACTIVITY
JOBNAME  STEPNAME PROCSTEP ASID  STATUS
OSKB030052   STEP1            003C  ACTIVE
IEE457I 00.00.00 UNIT STATUS DISPLAY
IEE115IとOSKB030052が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; D A,L が画面・出力に表示されること
② ステップ2 の K S,DEL= など と OSKB030052 が画面・出力に表示されること
③ ステップ3 の IEE115I と OSKB030052 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS MVS System Commands</p></div></details></section>
