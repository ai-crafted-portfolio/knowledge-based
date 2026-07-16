---
search:
  exclude: true
---

# Assembler / システム・プログラミング — 詳細 (4/4)

[← Assembler / システム・プログラミング の概要へ戻る](index.md)


## 命令: 比較


<section class="kb-item" id="c03-i0554"><h3>CL R1,addr</h3><p class="kb-meta">分類: 命令: 比較 ・ 難易度: 上級</p><p>CL R1,addrは、Assembler / システム・プログラミングの命令: 比較で確認する項目です。Compare Logical。論理 (符号なし) 比較 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_csfb400_icsf_apg_hcr77e0]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出照合の命令: 比較でアセンブラーの運用確認を行います。CL R1,addrの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. HLASM and z/OS System Programmingと無関係な一覧で呼出照合の命令: 比較を確認した扱いにする。</li><li>B. ASMA90I の有無を確認せず呼出照合の命令: 比較を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて呼出照合の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. CL R1,addrの属性行を読まず呼出照合の命令: 比較の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出照合の命令: 比較において選択記号 C を採用し、識別名は呼出照合です。呼出照合の命令: 比較において CL R1,addr は説明欄の「HLASM and z/OS System Programmingで CL R1,addrの扱いを記録する呼出照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合の命令: 比較を受け取る担当者は、CL R1,addrの表示結果と ASMA90I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合の命令: 比較は別カテゴリの確認を流用しており、CL R1,addrの根拠にならないため呼出照合ではありません。 B: 呼出照合の命令: 比較は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合の命令: 比較は対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合の命令: 比較は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合の命令: 比較が示す CL R1,addrは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CL R1,addr</strong></p><p>検証目的: 値域照合の命令: 比較について、CL R1,addrは、Assembler / システム・プログラミングの命令: 比較で確認する項目です。Compare Logical。論理 (符号なし) 比較 (メインに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010036の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、値域照合の命令: 比較の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にCL R1,addrを指定し、OSKB010036の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND CL R1,addr
CASE OSKB010036
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM CL R1,addr
CASE OSKB010036
SOURCE HLASM and z/OS System Programming
CL R1,addrとOSKB010036が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010036を同じ出力で読み、値域照合の命令: 比較の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010036
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010036
ASMA90I CL R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010036が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の CL R1,addr と OSKB010036 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010036 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_csfb400_icsf_apg_hcr77e0]</p></div></details></section>


<section class="kb-item" id="c03-i0555"><h3>CLR R1,R2</h3><p class="kb-meta">分類: 命令: 比較 ・ 難易度: 上級</p><p>Compare Logical Register。32bit 符号なし比較 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_csfb400_icsf_apg_hcr77e0]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換照合の命令: 比較に関する CLR R1,R2 の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. ST OSKBASM の結果を残さず置換照合の命令: 比較の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換照合の命令: 比較の証跡として保存して根拠にする。</li><li>C. CLR R1,R2 の変更点を出力本文から切り離して置換照合の命令: 比較の承認欄のみ残す。</li><li>D. ASMA90I を含む表示を保存し、説明欄との差分を置換照合で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換照合の命令: 比較において選択記号 D を採用し、識別名は置換照合です。置換照合の命令: 比較において CLR R1,R2 は説明欄の「CLR R1,R2 の状態と出力メッセージを結び付ける置換照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合の命令: 比較に関する記録は、CLR R1,R2 の出力行と ASMA90I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合の命令: 比較は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため置換照合ではありません。 B: 置換照合の命令: 比較は別カテゴリの確認を流用しており、CLR R1,R2 の根拠にならないため置換照合ではありません。 C: 置換照合の命令: 比較は名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合の命令: 比較は対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合の命令: 比較で記録する CLR R1,R2 は HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は置換照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CLR R1,R2</strong></p><p>検証目的: 警告照合の命令: 比較について、Compare Logical Register。32bit 符号なし比較 (メインフレーム実践 (神居俊哉)、MFOS 入門 (アルテシード) 由来 + 出典: HLASMに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010037の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、警告照合の命令: 比較の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にCLR R1,R2を指定し、OSKB010037の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND CLR R1,R2
CASE OSKB010037
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM CLR R1,R2
CASE OSKB010037
SOURCE HLASM and z/OS System Programming
CLR R1,R2とOSKB010037が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010037を同じ出力で読み、警告照合の命令: 比較の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010037
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010037
ASMA90I CLR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010037が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の CLR R1,R2 と OSKB010037 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010037 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_csfb400_icsf_apg_hcr77e0]</p></div></details></section>


<section class="kb-item" id="c03-i0556"><h3>CR R1,R2</h3><p class="kb-meta">分類: 命令: 比較 ・ 難易度: 上級</p><p>CR R1,R2は、Assembler / システム・プログラミングの命令: 比較で確認する項目です。Compare Register。R1 と R2 を符号付き比較 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_csfb400_icsf_apg_hcr77e0]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文照合の命令: 比較に関係する CR R1,R2 の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文照合で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. CR R1,R2 の名称と担当者名のみを残して構文照合の命令: 比較の表示本文を確認対象に含めない。</li><li>C. アセンブラー以外の画面で構文照合の命令: 比較を確認し同じ証跡として扱ったことにする。</li><li>D. ASMA90I の有無を見ず構文照合の命令: 比較の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文照合の命令: 比較において選択記号 A を採用し、識別名は構文照合です。構文照合の命令: 比較において CR R1,R2 は説明欄の「CR R1,R2 の用途をアセンブラーの表示で確認する構文照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合の命令: 比較に関連して、HLASM and z/OS System Programmingでは CR R1,R2 の表示属性と ASMA90I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合の命令: 比較は対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合の命令: 比較は名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合の命令: 比較は別カテゴリの確認を流用しており、CR R1,R2 の根拠にならないため構文照合ではありません。 D: 構文照合の命令: 比較は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため構文照合ではありません。構文照合の命令: 比較で使う CR R1,R2 という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は構文照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CR R1,R2</strong></p><p>検証目的: 比較照合の命令: 比較について、CR R1,R2 は、Assembler / システム・プログラミングの命令: 比較で確認する項目です。Compare Register。R1 と R2 を符号付き比較 (メに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010034の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、比較照合の命令: 比較の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にCR R1,R2を指定し、OSKB010034の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND CR R1,R2
CASE OSKB010034
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM CR R1,R2
CASE OSKB010034
SOURCE HLASM and z/OS System Programming
CR R1,R2とOSKB010034が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010034を同じ出力で読み、比較照合の命令: 比較の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010034
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010034
ASMA90I CR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010034が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の CR R1,R2 と OSKB010034 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010034 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_csfb400_icsf_apg_hcr77e0]</p></div></details></section>


## 命令: 移動


<section class="kb-item" id="c03-i0557"><h3>MVC addr1(len),addr2</h3><p class="kb-meta">分類: 命令: 移動 ・ 難易度: 上級</p><p>MVC addr1(len),addr2は、Assembler / システム・プログラミングの命令: 移動で確認する項目です。Move Character。最大 256 バイトの連続文字移動 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ikjb700] [zOS31_icei100]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端確認の命令: 移動に関係する MVC addr1 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 資料上の説明と画面上の表示行を突き合わせ、終端確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>B. MVC addr1 属性の名称と担当者名のみを残して終端確認の命令: 移動の表示本文を確認対象に含めない。</li><li>C. アセンブラー以外の画面で終端確認の命令: 移動を確認し同じ証跡として扱ったことにする。</li><li>D. ASMA90I の有無を見ず終端確認の命令: 移動の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端確認の命令: 移動において選択記号 A を採用し、識別名は終端確認です。終端確認の命令: 移動において MVC addr1 属性 は説明欄の「MVC addr1 属性の用途をアセンブラーの表示で確認する終端確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認の命令: 移動に関連して、HLASM and z/OS System Programmingでは MVC addr1 属性の表示属性と ASMA90I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認の命令: 移動は対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認の命令: 移動は名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認の命令: 移動は別カテゴリの確認を流用しており、MVC addr1 属性の根拠にならないため終端確認ではありません。 D: 終端確認の命令: 移動は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため終端確認ではありません。終端確認の命令: 移動で使う MVC addr1 属性という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は終端確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MVC addr1(len),addr2</strong></p><p>検証目的: 出力検査の命令: 移動について、MVC addr1(len),addr2は、Assembler / システム・プログラミングの命令: 移動で確認する項目です。Move Character。最大 256 バに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010068の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、出力検査の命令: 移動の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にMVC addr1(len),addを指定し、OSKB010068の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND MVC addr1(len),add
CASE OSKB010068
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM MVC addr1(len),add
CASE OSKB010068
SOURCE HLASM and z/OS System Programming
MVC addr1(len),addとOSKB010068が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010068を同じ出力で読み、出力検査の命令: 移動の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010068
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010068
ASMA90I MVC addr1(len),addr2 ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010068が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の MVC addr1(len),add と OSKB010068 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010068 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ikjb700] [zOS31_icei100]</p></div></details></section>


<section class="kb-item" id="c03-i0558"><h3>MVC 重複ストア</h3><p class="kb-meta">分類: 命令: 移動 ・ 難易度: 上級</p><p>MVC 重複ストアは、Assembler / システム・プログラミングの命令: 移動で確認する項目です。addr1 と addr2 が 1 バイトずれると伝播ストア (パディング テクニック) (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ikjb700] [zOS31_icei100]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索確認の重複ストアで MVC 重複ストアの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. MVC 重複ストアの出力を取らず探索確認の重複ストアの説明文と承認印のみを残す。</li><li>B. 操作結果の本文、対象行、時刻を同じ証跡に入れ、探索確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>C. ST OSKBASM を省略して探索確認の重複ストアの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索確認の重複ストアへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索確認の重複ストアにおいて選択記号 B を採用し、識別名は探索確認です。探索確認の重複ストアにおいて MVC 重複ストア は説明欄の「探索確認の重複ストアに関係する定義値と表示行を照合する探索確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認の重複ストアの証跡を読む担当者は、MVC 重複ストアの属性行と ASMA90I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認の重複ストアは名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認の重複ストアは対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認の重複ストアは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため探索確認ではありません。 D: 探索確認の重複ストアは別カテゴリの確認を流用しており、MVC 重複ストアの根拠にならないため探索確認ではありません。探索確認の重複ストアに出る MVC 重複ストアは Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は探索確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MVC 重複ストア</strong></p><p>検証目的: 条件検査の重複ストアについて、MVC 重複ストアは、Assembler / システム・プログラミングの命令: 移動で確認する項目です。addr1 と addr2 が 1 バイトずれると伝播ストア (パデに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010069の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、条件検査の重複ストアの確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にMVC 重複ストアを指定し、OSKB010069の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND MVC 重複ストア
CASE OSKB010069
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM MVC 重複ストア
CASE OSKB010069
SOURCE HLASM and z/OS System Programming
MVC 重複ストアとOSKB010069が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010069を同じ出力で読み、条件検査の重複ストアの根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010069
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010069
ASMA90I MVC 重複ストア ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010069が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の MVC 重複ストア と OSKB010069 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010069 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ikjb700] [zOS31_icei100]</p></div></details></section>


<section class="kb-item" id="c03-i0559"><h3>MVI addr,imm</h3><p class="kb-meta">分類: 命令: 移動 ・ 難易度: 上級</p><p>MVI addr,immは、Assembler / システム・プログラミングの命令: 移動で確認する項目です。Move Immediate。1 バイト即値を主記憶に格納 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ikjb700] [zOS31_icei100]</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件追跡の命令: 移動に関係する MVI addr,immの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. ASMA90I を含む表示を保存し、説明欄との差分を条件追跡で確認する。 <span class="kb-ok">✅ 正解</span></li><li>B. MVI addr,immの名称と担当者名だけを残して条件追跡の命令: 移動の表示本文を対象から外す。</li><li>C. アセンブラー以外の画面で条件追跡の命令: 移動を確認し同じ証跡として扱ったことにする。</li><li>D. ASMA90I の有無を見ず条件追跡の命令: 移動の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では MVI addr,imm は「MVI addr,immの用途をアセンブラーの表示で確認する条件追跡項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では HLASM and z/OS System Programmingの MVI addr,immと ASMA90I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明だけに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では MVI addr,immを Assembler / システム・プログラミングで扱う確認対象とし、用語名は条件追跡用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div><div class="kb-q"><p><strong>問題.</strong> 置換確認の命令: 移動に関する MVI addr,immの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. ST OSKBASM の結果を残さず置換確認の命令: 移動の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換確認の命令: 移動の証跡として保存して根拠にする。</li><li>C. MVI addr,immの変更点を出力本文から切り離して置換確認の命令: 移動の承認欄のみ残す。</li><li>D. ST OSKBASM で得た表示本文を使い、置換確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換確認の命令: 移動において選択記号 D を採用し、識別名は置換確認です。置換確認の命令: 移動において MVI addr,imm は説明欄の「MVI addr,immの状態と出力メッセージを結び付ける置換確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認の命令: 移動に関する記録は、MVI addr,immの出力行と ASMA90I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認の命令: 移動は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため置換確認ではありません。 B: 置換確認の命令: 移動は別カテゴリの確認を流用しており、MVI addr,immの根拠にならないため置換確認ではありません。 C: 置換確認の命令: 移動は名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認の命令: 移動は対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認の命令: 移動で記録する MVI addr,immは HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は置換確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MVI addr,imm</strong></p><p>検証目的: 上書検査の命令: 移動について、MVI addr,immは、Assembler / システム・プログラミングの命令: 移動で確認する項目です。Move Immediate。1 バイト即値を主記憶に格納 (に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010067の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、上書検査の命令: 移動の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にMVI addr,immを指定し、OSKB010067の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND MVI addr,imm
CASE OSKB010067
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM MVI addr,imm
CASE OSKB010067
SOURCE HLASM and z/OS System Programming
MVI addr,immとOSKB010067が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010067を同じ出力で読み、上書検査の命令: 移動の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010067
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010067
ASMA90I MVI addr,imm ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010067が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の MVI addr,imm と OSKB010067 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010067 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_ikjb700] [zOS31_icei100]</p></div></details></section>


## 命令: 算術


<section class="kb-item" id="c03-i0560"><h3>A R1,addr</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>A R1,addrは、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Add。主記憶 4 バイトを R1 に符号付き加算。CC 設定 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書確認の命令: 算術でアセンブラーの運用確認を行います。A R1,addrの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. HLASM and z/OS System Programmingと無関係な一覧で上書確認の命令: 算術を確認した扱いにする。</li><li>B. ASMA90I の有無を確認せず上書確認の命令: 算術を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. A R1,addrの属性行を読まず上書確認の命令: 算術の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書確認の命令: 算術において選択記号 C を採用し、識別名は上書確認です。上書確認の命令: 算術において A R1,addr は説明欄の「HLASM and z/OS System Programmingで A R1,addrの扱いを記録する上書確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認の命令: 算術を受け取る担当者は、A R1,addrの表示結果と ASMA90I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認の命令: 算術は別カテゴリの確認を流用しており、A R1,addrの根拠にならないため上書確認ではありません。 B: 上書確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため上書確認ではありません。 C: 上書確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認の命令: 算術が示す A R1,addrは出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>A R1,addr</strong></p><p>検証目的: 変更確認の命令: 算術について、A R1,addrは、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Add。主記憶 4 バイトを R1 に符号付き加算。CC 設定 (メに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、変更確認の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にA R1,addrを指定し、OSKB010020の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND A R1,addr
CASE OSKB010020
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM A R1,addr
CASE OSKB010020
SOURCE HLASM and z/OS System Programming
A R1,addrとOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010020を同じ出力で読み、変更確認の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010020
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010020
ASMA90I A R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の A R1,addr と OSKB010020 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0561"><h3>AGR R1,R2</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>AGR R1,R2は、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Add Grande Register (64bit 符号付き) (メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉/髙尾司) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧確認の命令: 算術で AGR R1,R2 の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. AGR R1,R2 の出力を取らず復旧確認の命令: 算術の説明文と承認印のみを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、復旧確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. ST OSKBASM を省略して復旧確認の命令: 算術の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧確認の命令: 算術へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧確認の命令: 算術において選択記号 B を採用し、識別名は復旧確認です。復旧確認の命令: 算術において AGR R1,R2 は説明欄の「復旧確認の命令: 算術に関係する定義値と表示行を照合する復旧確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は復旧確認です。復旧確認の命令: 算術の証跡を読む担当者は、AGR R1,R2 の属性行と ASMA90I を合わせて追跡し、背景名は復旧確認です。誤答側の問題点を分けます。 A: 復旧確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧確認ではありません。 B: 復旧確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので復旧確認です。 C: 復旧確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため復旧確認ではありません。 D: 復旧確認の命令: 算術は別カテゴリの確認を流用しており、AGR R1,R2 の根拠にならないため復旧確認ではありません。復旧確認の命令: 算術に出る AGR R1,R2 は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は復旧確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AGR R1,R2</strong></p><p>検証目的: 範囲照合の命令: 算術について、AGR R1,R2 は、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Add Grande Register (64bit 符号付き) (に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010031の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、範囲照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にAGR R1,R2を指定し、OSKB010031の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND AGR R1,R2
CASE OSKB010031
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM AGR R1,R2
CASE OSKB010031
SOURCE HLASM and z/OS System Programming
AGR R1,R2とOSKB010031が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010031を同じ出力で読み、範囲照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010031
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010031
ASMA90I AGR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010031が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の AGR R1,R2 と OSKB010031 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010031 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0562"><h3>AH R1,addr</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>AH R1,addrは、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Add Halfword。半語を符号拡張して R1 に加算 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件確認の命令: 算術に関係する AH R1,addrの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. AH R1,addrの名称と担当者名のみを残して条件確認の命令: 算術の表示本文を確認対象に含めない。</li><li>C. アセンブラー以外の画面で条件確認の命令: 算術を確認し同じ証跡として扱ったことにする。</li><li>D. ASMA90I の有無を見ず条件確認の命令: 算術の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件確認の命令: 算術において選択記号 A を採用し、識別名は条件確認です。条件確認の命令: 算術において AH R1,addr は説明欄の「AH R1,addrの用途をアセンブラーの表示で確認する条件確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認の命令: 算術に関連して、HLASM and z/OS System Programmingでは AH R1,addrの表示属性と ASMA90I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認の命令: 算術は別カテゴリの確認を流用しており、AH R1,addrの根拠にならないため条件確認ではありません。 D: 条件確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため条件確認ではありません。条件確認の命令: 算術で使う AH R1,addrという用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は条件確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AH R1,addr</strong></p><p>検証目的: 展開照合の命令: 算術について、AH R1,addrは、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Add Halfword。半語を符号拡張して R1 に加算 (メイに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010022の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、展開照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にAH R1,addrを指定し、OSKB010022の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND AH R1,addr
CASE OSKB010022
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM AH R1,addr
CASE OSKB010022
SOURCE HLASM and z/OS System Programming
AH R1,addrとOSKB010022が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010022を同じ出力で読み、展開照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010022
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010022
ASMA90I AH R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010022が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の AH R1,addr と OSKB010022 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0563"><h3>AHI R1,imm</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>AHI R1,immは、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Add Halfword Immediate。16bit 即値加算 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査確認の命令: 算術でアセンブラーの運用確認を行います。AHI R1,immの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. HLASM and z/OS System Programmingと無関係な一覧で監査確認の命令: 算術を確認した扱いにする。</li><li>B. ASMA90I の有無を確認せず監査確認の命令: 算術を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. AHI R1,immの属性行を読まず監査確認の命令: 算術の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査確認の命令: 算術において選択記号 C を採用し、識別名は監査確認です。監査確認の命令: 算術において AHI R1,imm は説明欄の「HLASM and z/OS System Programmingで AHI R1,immの扱いを記録する監査確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認の命令: 算術を受け取る担当者は、AHI R1,immの表示結果と ASMA90I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認の命令: 算術は別カテゴリの確認を流用しており、AHI R1,immの根拠にならないため監査確認ではありません。 B: 監査確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため監査確認ではありません。 C: 監査確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認の命令: 算術が示す AHI R1,immは出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AHI R1,imm</strong></p><p>検証目的: 優先照合の命令: 算術について、AHI R1,immは、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Add Halfword Imに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010032の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、優先照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にAHI R1,immを指定し、OSKB010032の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND AHI R1,imm
CASE OSKB010032
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM AHI R1,imm
CASE OSKB010032
SOURCE HLASM and z/OS System Programming
AHI R1,immとOSKB010032が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010032を同じ出力で読み、優先照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010032
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010032
ASMA90I AHI R1,imm ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010032が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の AHI R1,imm と OSKB010032 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010032 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0564"><h3>AL R1,addr</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>AL R1,addrは、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Add Logical。論理 (符号なし) 加算。キャリーで CC=2,3 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切確認の命令: 算術で AL R1,addrの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. AL R1,addrの出力を取らず区切確認の命令: 算術の説明文と承認印のみを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、区切確認の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. ST OSKBASM を省略して区切確認の命令: 算術の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切確認の命令: 算術へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切確認の命令: 算術において選択記号 B を採用し、識別名は区切確認です。区切確認の命令: 算術において AL R1,addr は説明欄の「区切確認の命令: 算術に関係する定義値と表示行を照合する区切確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は区切確認です。区切確認の命令: 算術の証跡を読む担当者は、AL R1,addrの属性行と ASMA90I を合わせて追跡し、背景名は区切確認です。誤答側の問題点を分けます。 A: 区切確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため区切確認ではありません。 B: 区切確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので区切確認です。 C: 区切確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため区切確認ではありません。 D: 区切確認の命令: 算術は別カテゴリの確認を流用しており、AL R1,addrの根拠にならないため区切確認ではありません。区切確認の命令: 算術に出る AL R1,addrは Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は区切確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AL R1,addr</strong></p><p>検証目的: 呼出照合の命令: 算術について、AL R1,addrは、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Add Logical。論理 (符号なし) 加算。キャリーで CCに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010023の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、呼出照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にAL R1,addrを指定し、OSKB010023の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND AL R1,addr
CASE OSKB010023
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM AL R1,addr
CASE OSKB010023
SOURCE HLASM and z/OS System Programming
AL R1,addrとOSKB010023が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010023を同じ出力で読み、呼出照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010023
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010023
ASMA90I AL R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010023が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の AL R1,addr と OSKB010023 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010023 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0565"><h3>ALR R1,R2</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>ALR R1,R2は、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Add Logical Register。32bit 論理加算 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲確認の命令: 算術でアセンブラーの運用確認を行います。ALR R1,R2 の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. HLASM and z/OS System Programmingと無関係な一覧で範囲確認の命令: 算術を確認した扱いにする。</li><li>B. ASMA90I の有無を確認せず範囲確認の命令: 算術を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて範囲確認の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. ALR R1,R2 の属性行を読まず範囲確認の命令: 算術の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲確認の命令: 算術において選択記号 C を採用し、識別名は範囲確認です。範囲確認の命令: 算術において ALR R1,R2 は説明欄の「HLASM and z/OS System Programmingで ALR R1,R2 の扱いを記録する範囲確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は範囲確認です。範囲確認の命令: 算術を受け取る担当者は、ALR R1,R2 の表示結果と ASMA90I を同じ確認単位として扱い、背景名は範囲確認です。不適切な選択肢を整理します。 A: 範囲確認の命令: 算術は別カテゴリの確認を流用しており、ALR R1,R2 の根拠にならないため範囲確認ではありません。 B: 範囲確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため範囲確認ではありません。 C: 範囲確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので範囲確認です。 D: 範囲確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲確認ではありません。範囲確認の命令: 算術が示す ALR R1,R2 は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ALR R1,R2</strong></p><p>検証目的: 置換照合の命令: 算術について、ALR R1,R2 は、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Add Logical Regiに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010024の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、置換照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にALR R1,R2を指定し、OSKB010024の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND ALR R1,R2
CASE OSKB010024
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM ALR R1,R2
CASE OSKB010024
SOURCE HLASM and z/OS System Programming
ALR R1,R2とOSKB010024が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010024を同じ出力で読み、置換照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010024
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010024
ASMA90I ALR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010024が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の ALR R1,R2 と OSKB010024 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0566"><h3>AR R1,R2</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>AR R1,R2は、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Add Register。R2 を R1 に加算 (32bit 符号付き) (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力確認の命令: 算術に関する AR R1,R2 の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. ST OSKBASM の結果を残さず出力確認の命令: 算術の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力確認の命令: 算術の証跡として保存して根拠にする。</li><li>C. AR R1,R2 の変更点を出力本文から切り離して出力確認の命令: 算術の承認欄のみ残す。</li><li>D. HLASM and z/OS System Programmingの表示形式に沿って根拠行を採り、出力確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力確認の命令: 算術において選択記号 D を採用し、識別名は出力確認です。出力確認の命令: 算術において AR R1,R2 は説明欄の「AR R1,R2 の状態と出力メッセージを結び付ける出力確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認の命令: 算術に関する記録は、AR R1,R2 の出力行と ASMA90I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため出力確認ではありません。 B: 出力確認の命令: 算術は別カテゴリの確認を流用しており、AR R1,R2 の根拠にならないため出力確認ではありません。 C: 出力確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認の命令: 算術で記録する AR R1,R2 は HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は出力確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AR R1,R2</strong></p><p>検証目的: 構文照合の命令: 算術について、AR R1,R2 は、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Add Register。R2 を R1 に加算 (32bit 符号付に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010021の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、構文照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にAR R1,R2を指定し、OSKB010021の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND AR R1,R2
CASE OSKB010021
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM AR R1,R2
CASE OSKB010021
SOURCE HLASM and z/OS System Programming
AR R1,R2とOSKB010021が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010021を同じ出力で読み、構文照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010021
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010021
ASMA90I AR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010021が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の AR R1,R2 と OSKB010021 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010021 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0567"><h3>D R1,addr</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>D R1,addrは、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Divide。R1:R1+1 64bit を 32bit 除数で除算。商 R1+1, 剰余 R1 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域確認の命令: 算術に関する D R1,addrの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. ST OSKBASM の結果を残さず値域確認の命令: 算術の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域確認の命令: 算術の証跡として保存して根拠にする。</li><li>C. D R1,addrの変更点を出力本文から切り離して値域確認の命令: 算術の承認欄のみ残す。</li><li>D. 同じ画面で対象行と ASMA90I を読み、値域確認の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域確認の命令: 算術において選択記号 D を採用し、識別名は値域確認です。値域確認の命令: 算術において D R1,addr は説明欄の「D R1,addrの状態と出力メッセージを結び付ける値域確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は値域確認です。値域確認の命令: 算術に関する記録は、D R1,addrの出力行と ASMA90I を一緒に保存し、背景名は値域確認です。選択肢ごとの違いを示します。 A: 値域確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため値域確認ではありません。 B: 値域確認の命令: 算術は別カテゴリの確認を流用しており、D R1,addrの根拠にならないため値域確認ではありません。 C: 値域確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため値域確認ではありません。 D: 値域確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので値域確認です。値域確認の命令: 算術で記録する D R1,addrは HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は値域確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>D R1,addr</strong></p><p>検証目的: 条件照合の命令: 算術について、D R1,addrは、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Divide。R1:R1+1 64bit を 32bit 除数で除算に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010029の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、条件照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にD R1,addrを指定し、OSKB010029の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND D R1,addr
CASE OSKB010029
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM D R1,addr
CASE OSKB010029
SOURCE HLASM and z/OS System Programming
D R1,addrとOSKB010029が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010029を同じ出力で読み、条件照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010029
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010029
ASMA90I D R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010029が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の D R1,addr と OSKB010029 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010029 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0568"><h3>DR R1,R2</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>DR R1,R2は、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Divide Register。32bit 除算 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力追跡の命令: 算術に関する DR R1,R2 の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. ST OSKBASM の結果を残さず出力追跡の命令: 算術の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力追跡の命令: 算術の証跡として保存して根拠にする。</li><li>C. DR R1,R2 の変更点を出力本文から切り離して出力追跡の命令: 算術の承認欄だけ残す。</li><li>D. 参照資料名、表示行、メッセージをそろえて出力追跡の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では DR R1,R2 は「DR R1,R2 の状態と出力メッセージを結び付ける出力追跡項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では DR R1,R2 の出力行と ASMA90I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明だけに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では DR R1,R2 を HLASM and z/OS System Programmingの確認記録に残し、対象名は出力追跡対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div><div class="kb-q"><p><strong>問題.</strong> 警告確認の命令: 算術に関係する DR R1,R2 の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. ST OSKBASM で得た表示本文を使い、警告確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. DR R1,R2 の名称と担当者名のみを残して警告確認の命令: 算術の表示本文を確認対象に含めない。</li><li>C. アセンブラー以外の画面で警告確認の命令: 算術を確認し同じ証跡として扱ったことにする。</li><li>D. ASMA90I の有無を見ず警告確認の命令: 算術の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告確認の命令: 算術において選択記号 A を採用し、識別名は警告確認です。警告確認の命令: 算術において DR R1,R2 は説明欄の「DR R1,R2 の用途をアセンブラーの表示で確認する警告確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認の命令: 算術に関連して、HLASM and z/OS System Programmingでは DR R1,R2 の表示属性と ASMA90I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認の命令: 算術は別カテゴリの確認を流用しており、DR R1,R2 の根拠にならないため警告確認ではありません。 D: 警告確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため警告確認ではありません。警告確認の命令: 算術で使う DR R1,R2 という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は警告確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DR R1,R2</strong></p><p>検証目的: 区切照合の命令: 算術について、DR R1,R2 は、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Divide Register。3に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010030の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、区切照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にDR R1,R2を指定し、OSKB010030の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND DR R1,R2
CASE OSKB010030
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM DR R1,R2
CASE OSKB010030
SOURCE HLASM and z/OS System Programming
DR R1,R2とOSKB010030が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010030を同じ出力で読み、区切照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010030
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010030
ASMA90I DR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010030が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の DR R1,R2 と OSKB010030 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0569"><h3>M R1,addr</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>M R1,addrは、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Multiply。R1+1 と主記憶を 32bit 符号付き乗算。結果は R1:R1+1 64bit (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告確認の命令: 算術に関係する M R1,addrの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 同じ画面で対象行と ASMA90I を読み、警告確認の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>B. M R1,addrの名称と担当者名だけを残して警告確認の命令: 算術の表示本文を対象から外す。</li><li>C. アセンブラー以外の画面で警告確認の命令: 算術を確認し同じ証跡として扱ったことにする。</li><li>D. ASMA90I の有無を見ず警告確認の命令: 算術の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では M R1,addr は「M R1,addrの用途をアセンブラーの表示で確認する警告確認項目」と ST OSKBASM または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では HLASM and z/OS System Programmingの M R1,addrと ASMA90I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明だけに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では M R1,addrを Assembler / システム・プログラミングで扱う確認対象とし、用語名は警告確認用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div><div class="kb-q"><p><strong>問題.</strong> 比較確認の命令: 算術で M R1,addrの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. M R1,addrの出力を取らず比較確認の命令: 算術の説明文と承認印のみを残す。</li><li>B. 出典欄の説明と運用出力を照合し、比較確認の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. ST OSKBASM を省略して比較確認の命令: 算術の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較確認の命令: 算術へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較確認の命令: 算術において選択記号 B を採用し、識別名は比較確認です。比較確認の命令: 算術において M R1,addr は説明欄の「比較確認の命令: 算術に関係する定義値と表示行を照合する比較確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は比較確認です。比較確認の命令: 算術の証跡を読む担当者は、M R1,addrの属性行と ASMA90I を合わせて追跡し、背景名は比較確認です。誤答側の問題点を分けます。 A: 比較確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため比較確認ではありません。 B: 比較確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので比較確認です。 C: 比較確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため比較確認ではありません。 D: 比較確認の命令: 算術は別カテゴリの確認を流用しており、M R1,addrの根拠にならないため比較確認ではありません。比較確認の命令: 算術に出る M R1,addrは Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は比較確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>M R1,addr</strong></p><p>検証目的: 上書照合の命令: 算術について、M R1,addrは、Assembler / システム・プログラミングの命令: 算術で確認する項目です。Multiply。R1+1 と主記憶を 32bit 符号付き乗算。結に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010027の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、上書照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にM R1,addrを指定し、OSKB010027の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND M R1,addr
CASE OSKB010027
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM M R1,addr
CASE OSKB010027
SOURCE HLASM and z/OS System Programming
M R1,addrとOSKB010027が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010027を同じ出力で読み、上書照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010027
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010027
ASMA90I M R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010027が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の M R1,addr と OSKB010027 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010027 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0570"><h3>MR R1,R2</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>MR R1,R2は、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Multiply Register。R1+1 と R2 の 32bit 乗算 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序確認の命令: 算術でアセンブラーの運用確認を行います。MR R1,R2 の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. HLASM and z/OS System Programmingと無関係な一覧で順序確認の命令: 算術を確認した扱いにする。</li><li>B. ASMA90I の有無を確認せず順序確認の命令: 算術を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて順序確認の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. MR R1,R2 の属性行を読まず順序確認の命令: 算術の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序確認の命令: 算術において選択記号 C を採用し、識別名は順序確認です。順序確認の命令: 算術において MR R1,R2 は説明欄の「HLASM and z/OS System Programmingで MR R1,R2 の扱いを記録する順序確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認の命令: 算術を受け取る担当者は、MR R1,R2 の表示結果と ASMA90I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認の命令: 算術は別カテゴリの確認を流用しており、MR R1,R2 の根拠にならないため順序確認ではありません。 B: 順序確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため順序確認ではありません。 C: 順序確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認の命令: 算術が示す MR R1,R2 は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>MR R1,R2</strong></p><p>検証目的: 優先照合の命令: 算術について、MR R1,R2 は、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Multiply Registerに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB060032の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、優先照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にMR R1,R2を指定し、OSKB060032の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND MR R1,R2
CASE OSKB060032
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM MR R1,R2
CASE OSKB060032
SOURCE HLASM and z/OS System Programming
MR R1,R2とOSKB060032が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB060032を同じ出力で読み、優先照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB060032
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB060032
ASMA90I MR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB060032が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の MR R1,R2 と OSKB060032 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB060032 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div><div class="kb-p"><p class="kb-pname"><strong>MR R1,R2</strong></p><p>検証目的: 出力照合の命令: 算術について、MR R1,R2 は、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Multiply Registerに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010028の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、出力照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にMR R1,R2を指定し、OSKB010028の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND MR R1,R2
CASE OSKB010028
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM MR R1,R2
CASE OSKB010028
SOURCE HLASM and z/OS System Programming
MR R1,R2とOSKB010028が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010028を同じ出力で読み、出力照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010028
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010028
ASMA90I MR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010028が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の MR R1,R2 と OSKB010028 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010028 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0571"><h3>S R1,addr</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>S R1,addrは、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Subtract。32bit 符号付き減算 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先確認の命令: 算術に関する S R1,addrの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. ST OSKBASM の結果を残さず優先確認の命令: 算術の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先確認の命令: 算術の証跡として保存して根拠にする。</li><li>C. S R1,addrの変更点を出力本文から切り離して優先確認の命令: 算術の承認欄のみ残す。</li><li>D. ASMA90I を含む表示を保存し、説明欄との差分を優先確認で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先確認の命令: 算術において選択記号 D を採用し、識別名は優先確認です。優先確認の命令: 算術において S R1,addr は説明欄の「S R1,addrの状態と出力メッセージを結び付ける優先確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認の命令: 算術に関する記録は、S R1,addrの出力行と ASMA90I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため優先確認ではありません。 B: 優先確認の命令: 算術は別カテゴリの確認を流用しており、S R1,addrの根拠にならないため優先確認ではありません。 C: 優先確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認の命令: 算術で記録する S R1,addrは HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は優先確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>S R1,addr</strong></p><p>検証目的: 構文確認の命令: 算術について、S R1,addrは、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Subtract。32bit 符に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB060001の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、構文確認の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にS R1,addrを指定し、OSKB060001の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND S R1,addr
CASE OSKB060001
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM S R1,addr
CASE OSKB060001
SOURCE HLASM and z/OS System Programming
S R1,addrとOSKB060001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB060001を同じ出力で読み、構文確認の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB060001
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB060001
ASMA90I S R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB060001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の S R1,addr と OSKB060001 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB060001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div><div class="kb-p"><p class="kb-pname"><strong>S R1,addr</strong></p><p>検証目的: 終端照合の命令: 算術について、S R1,addrは、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Subtract。32bit 符に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010025の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、終端照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にS R1,addrを指定し、OSKB010025の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND S R1,addr
CASE OSKB010025
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM S R1,addr
CASE OSKB010025
SOURCE HLASM and z/OS System Programming
S R1,addrとOSKB010025が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010025を同じ出力で読み、終端照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010025
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010025
ASMA90I S R1,addr ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010025が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の S R1,addr と OSKB010025 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010025 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


<section class="kb-item" id="c03-i0572"><h3>SR R1,R2</h3><p class="kb-meta">分類: 命令: 算術 ・ 難易度: 上級</p><p>SR R1,R2は、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Subtract Register。R1 = R1 - R2 (メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) 由来 + 出典: HLASM Language Reference / z/OS MVS Assembler Services、)</p><p class="kb-src"><strong>出典:</strong> メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録確認の命令: 算術に関係する SR R1,R2 の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. ST OSKBASM の結果から対象行を抜き出し、記録確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. SR R1,R2 の名称と担当者名のみを残して記録確認の命令: 算術の表示本文を確認対象に含めない。</li><li>C. アセンブラー以外の画面で記録確認の命令: 算術を確認し同じ証跡として扱ったことにする。</li><li>D. ASMA90I の有無を見ず記録確認の命令: 算術の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録確認の命令: 算術において選択記号 A を採用し、識別名は記録確認です。記録確認の命令: 算術において SR R1,R2 は説明欄の「SR R1,R2 の用途をアセンブラーの表示で確認する記録確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認の命令: 算術に関連して、HLASM and z/OS System Programmingでは SR R1,R2 の表示属性と ASMA90I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認の命令: 算術は対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認の命令: 算術は名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認の命令: 算術は別カテゴリの確認を流用しており、SR R1,R2 の根拠にならないため記録確認ではありません。 D: 記録確認の命令: 算術は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため記録確認ではありません。記録確認の命令: 算術で使う SR R1,R2 という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は記録確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SR R1,R2</strong></p><p>検証目的: 探索照合の命令: 算術について、SR R1,R2 は、Assembler / システム・プログラミングの命令: 算術で機能名、見出し、または確認対象として参照する項目です。Subtract Registerに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB010026の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、探索照合の命令: 算術の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にSR R1,R2を指定し、OSKB010026の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND SR R1,R2
CASE OSKB010026
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM SR R1,R2
CASE OSKB010026
SOURCE HLASM and z/OS System Programming
SR R1,R2とOSKB010026が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB010026を同じ出力で読み、探索照合の命令: 算術の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB010026
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB010026
ASMA90I SR R1,R2 ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB010026が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の SR R1,R2 と OSKB010026 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB010026 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、MFOS入門 (アルテシード) [zOS31_cbcpg01]</p></div></details></section>


## その他


<section class="kb-item" id="c03-other"><h3>その他（特定項目に紐づかないQA・手順）</h3><p class="kb-meta">項目名が個別の技術項目に一致しなかったQA・手順です。</p><details class="kb-block"><summary>確認問題（6問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切照合のなどで RESERVE 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. RESERVE 属性の出力を取らず区切照合のなどの説明文と承認印のみを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、区切照合の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. ST OSKBASM を省略して区切照合のなどの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切照合のなどへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切照合のなどにおいて選択記号 B を採用し、識別名は区切照合です。区切照合のなどにおいて RESERVE 属性 は説明欄の「区切照合のなどに関係する定義値と表示行を照合する区切照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合のなどの証跡を読む担当者は、RESERVE 属性の属性行と ASMA90I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合のなどは対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合のなどは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため区切照合ではありません。 D: 区切照合のなどは別カテゴリの確認を流用しており、RESERVE 属性の根拠にならないため区切照合ではありません。区切照合のなどに出る RESERVE 属性は Assembler / システム・プログラミングの運用手順で意味を確認する対象であり、用語名は区切照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div><div class="kb-q"><p><strong>問題.</strong> 順序確認のなどでアセンブラーの運用確認を行います。STIMERM SET,などの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. HLASM and z/OS System Programmingと無関係な一覧で順序確認のなどを確認した扱いにする。</li><li>B. ASMA90I の有無を確認せず順序確認のなどを正常終了として記録する。</li><li>C. HLASM and z/OS System Programmingの表示形式に沿って根拠行を採り、順序確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>D. STIMERM SET,などの属性行を読まず順序確認のなどの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序確認のなどにおいて選択記号 C を採用し、識別名は順序確認です。順序確認のなどにおいて STIMERM SET,など は説明欄の「HLASM and z/OS System Programmingで STIMERM SET,などの扱いを記録する順序確認項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認のなどを受け取る担当者は、STIMERM SET,などの表示結果と ASMA90I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認のなどは別カテゴリの確認を流用しており、STIMERM SET,などの根拠にならないため順序確認ではありません。 B: 順序確認のなどは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため順序確認ではありません。 C: 順序確認のなどは対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認のなどが示す STIMERM SET,などは出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div><div class="kb-q"><p><strong>問題.</strong> 条件照合のから 不可に関係する JSCBAUTH 0 から 1 不可の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. ST OSKBASM の結果から対象行を抜き出し、条件照合の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. JSCBAUTH 0 から 1 不可の名称と担当者名のみを残して条件照合のから 不可の表示本文を確認対象に含めない。</li><li>C. アセンブラー以外の画面で条件照合のから 不可を確認し同じ証跡として扱ったことにする。</li><li>D. ASMA90I の有無を見ず条件照合のから 不可の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件照合のから 不可において選択記号 A を採用し、識別名は条件照合です。条件照合のから 不可において JSCBAUTH 0 から 1 不可 は説明欄の「JSCBAUTH 0 から 1 不可の用途をアセンブラーの表示で確認する条件照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合のから 不可に関連して、HLASM and z/OS System Programmingでは JSCBAUTH 0 から 1 不可の表示属性と ASMA90I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合のから 不可は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合のから 不可は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合のから 不可は別カテゴリの確認を流用しており、JSCBAUTH 0 から 1 不可の根拠にならないため条件照合ではありません。 D: 条件照合のから 不可は戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため条件照合ではありません。条件照合のから 不可で使う JSCBAUTH 0 から 1 不可という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は条件照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div><div class="kb-q"><p><strong>問題.</strong> 値域照合のなどに関する APF 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. ST OSKBASM の結果を残さず値域照合のなどの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域照合のなどの証跡として保存して根拠にする。</li><li>C. APF 属性の変更点を出力本文から切り離して値域照合のなどの承認欄のみ残す。</li><li>D. HLASM and z/OS System Programmingの表示形式に沿って根拠行を採り、値域照合の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域照合のなどにおいて選択記号 D を採用し、識別名は値域照合です。値域照合のなどにおいて APF 属性 は説明欄の「APF 属性の状態と出力メッセージを結び付ける値域照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合のなどに関する記録は、APF 属性の出力行と ASMA90I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合のなどは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため値域照合ではありません。 B: 値域照合のなどは別カテゴリの確認を流用しており、APF 属性の根拠にならないため値域照合ではありません。 C: 値域照合のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合のなどは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合のなどで記録する APF 属性は HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は値域照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div><div class="kb-q"><p><strong>問題.</strong> 警告照合のなどに関係する APF 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告照合で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. APF 属性の名称と担当者名のみを残して警告照合のなどの表示本文を確認対象に含めない。</li><li>C. アセンブラー以外の画面で警告照合のなどを確認し同じ証跡として扱ったことにする。</li><li>D. ASMA90I の有無を見ず警告照合のなどの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告照合のなどにおいて選択記号 A を採用し、識別名は警告照合です。警告照合のなどにおいて APF 属性 は説明欄の「APF 属性の用途をアセンブラーの表示で確認する警告照合項目」と ST OSKBASM または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合のなどに関連して、HLASM and z/OS System Programmingでは APF 属性の表示属性と ASMA90I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合のなどは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合のなどは別カテゴリの確認を流用しており、APF 属性の根拠にならないため警告照合ではありません。 D: 警告照合のなどは戻り値や記録番号に寄り、ASMA90I や属性表示を落とすため警告照合ではありません。警告照合のなどで使う APF 属性という用語は Assembler / システム・プログラミングで扱う確認対象であり、用語名は警告照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div><div class="kb-q"><p><strong>問題.</strong> 置換確認のはに関する LPA とはの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. ST OSKBBIND の結果を残さず置換確認のはの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換確認のはの証跡として保存して根拠にする。</li><li>C. LPA とはの変更点を出力本文から切り離して置換確認のはの承認欄のみ残す。</li><li>D. ST OSKBBIND の結果から対象行を抜き出し、置換確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換確認のはにおいて選択記号 D を採用し、識別名は置換確認です。置換確認のはにおいて LPA とは は説明欄の「LPA とはの状態と出力メッセージを結び付ける置換確認項目」と ST OSKBBIND または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認のはに関する記録は、LPA とはの出力行と IEW2456I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認のはは戻り値や記録番号に寄り、IEW2456I や属性表示を落とすため置換確認ではありません。 B: 置換確認のはは別カテゴリの確認を流用しており、LPA とはの根拠にならないため置換確認ではありません。 C: 置換確認のはは名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認のはは対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認のはで記録する LPA とはは HLASM and z/OS System Programmingの確認記録に残す対象名であり、用語名は置換確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_asma90 / zOS31_ieav100 / zOS31_ieam400</p></div></details><details class="kb-block"><summary>検証手順（6件）</summary><div class="kb-p"><p class="kb-pname"><strong>RESERVE (qname,rname,など,UCB=)</strong></p><p>検証目的: 呼出確認のなどについて、Assembler システム・プログラミングのマクロ: 同期では、対象資源、指定値、実行時の出力を対応付けて確認します。マクロ: 同期は、Assembler システム・プロに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030003の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、呼出確認のなどの確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にRESERVE (qname,rnaを指定し、OSKB030003の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND RESERVE (qname,rna
CASE OSKB030003
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM RESERVE (qname,rna
CASE OSKB030003
SOURCE HLASM and z/OS System Programming
RESERVE (qname,rnaとOSKB030003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB030003を同じ出力で読み、呼出確認のなどの根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB030003
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB030003
ASMA90I RESERVE (qname,rname,など, ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB030003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の RESERVE (qname,rna と OSKB030003 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB030003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.1 (神居俊哉 / 髙尾司) [zOS31_ieaa700]</p></div><div class="kb-p"><p class="kb-pname"><strong>STIMERM SET,など</strong></p><p>検証目的: 復旧照合のなどについて、Assembler システム・プログラミングのマクロ: 時刻では、対象資源、指定値、実行時の出力を対応付けて確認します。マクロ: 時刻は、Assembler システム・プロに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB030038の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、復旧照合のなどの確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にSTIMERM SET,などを指定し、OSKB030038の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND STIMERM SET,など
CASE OSKB030038
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM STIMERM SET,など
CASE OSKB030038
SOURCE HLASM and z/OS System Programming
STIMERM SET,などとOSKB030038が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB030038を同じ出力で読み、復旧照合のなどの根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB030038
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB030038
ASMA90I STIMERM SET,など ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB030038が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の STIMERM SET,など と OSKB030038 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB030038 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.2 (神居俊哉 / 髙尾司) [zOS31_ieaa900] [zOS31_ieaa900]</p></div><div class="kb-p"><p class="kb-pname"><strong>JSCBAUTH 0 から 1 不可</strong></p><p>検証目的: 展開判定のから 不可について、JSCBAUTH 0 から 1 不可は、Assembler / システム・プログラミングの APF で確認する項目です。実行中に APF 取得は不可 (起動前のみ) (メインフに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB040082の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、展開判定のから 不可の確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にJSCBAUTH 0 から 1 不可を指定し、OSKB040082の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND JSCBAUTH 0 から 1 不可
CASE OSKB040082
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM JSCBAUTH 0 から 1 不可
CASE OSKB040082
SOURCE HLASM and z/OS System Programming
JSCBAUTH 0 から 1 不可とOSKB040082が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB040082を同じ出力で読み、展開判定のから 不可の根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB040082
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB040082
ASMA90I JSCBAUTH 0 から 1 不可 ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB040082が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の JSCBAUTH 0 から 1 不可 と OSKB040082 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB040082 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.2 (神居俊哉 / 髙尾司) [zOS31_ieaa800] [zOS31_ieaa800]</p></div><div class="kb-p"><p class="kb-pname"><strong>APF ADD DSNAME= など</strong></p><p>検証目的: 条件判定のなどについて、Assembler システム・プログラミングの PROGxxでは、対象資源、指定値、実行時の出力を対応付けて確認します。PROGxxは、Assembler システム・プログラに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB040089の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、条件判定のなどの確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にAPF ADD DSNAME= などを指定し、OSKB040089の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND APF ADD DSNAME= など
CASE OSKB040089
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM APF ADD DSNAME= など
CASE OSKB040089
SOURCE HLASM and z/OS System Programming
APF ADD DSNAME= などとOSKB040089が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB040089を同じ出力で読み、条件判定のなどの根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB040089
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB040089
ASMA90I APF ADD DSNAME= など ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB040089が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の APF ADD DSNAME= など と OSKB040089 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB040089 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.2 (神居俊哉 / 髙尾司) [zOS31_ieag100] [zOS31_ieae200]</p></div><div class="kb-p"><p class="kb-pname"><strong>APF DELETE DSNAME= など</strong></p><p>検証目的: 区切判定のなどについて、Assembler システム・プログラミングの PROGxxでは、対象資源、指定値、実行時の出力を対応付けて確認します。PROGxxは、Assembler システム・プログラに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB040090の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、区切判定のなどの確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にAPF DELETE DSNAME=を指定し、OSKB040090の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND APF DELETE DSNAME=
CASE OSKB040090
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM APF DELETE DSNAME=
CASE OSKB040090
SOURCE HLASM and z/OS System Programming
APF DELETE DSNAME=とOSKB040090が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB040090を同じ出力で読み、区切判定のなどの根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB040090
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB040090
ASMA90I APF DELETE DSNAME= など ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB040090が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の APF DELETE DSNAME= と OSKB040090 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB040090 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.2 (神居俊哉 / 髙尾司) [zOS31_ieag100] [zOS31_ieae200]</p></div><div class="kb-p"><p class="kb-pname"><strong>RIM (Resource Initialization Modul</strong></p><p>検証目的: 復旧整理のアセンブラーについて、RIM (Resource Initialization Module)は、Assembler / システム・プログラミングの LPA で確認する項目です。IPL 時の各種初期に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: SDSFまたは関連TSO/コンソールを参照でき、OSKB040118の検証用出力を記録できる。</p><p>セッション環境: SDSFでST OSKBASMを実行し、ASMA90Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はSDSFのコマンド入力画面です。COMMAND INPUT ===&gt; に ST OSKBASM を入力し、復旧整理のアセンブラーの確認表示へ進みます。
［操作（入力）］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
→ Enter を押す
［画面・出力］
(SDSF)
COMMAND INPUT ===&gt; ST OSKBASM
COMMAND INPUTにST OSKBASMが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はSDSFの表示結果です。FIND欄にRIM (Resource Initを指定し、OSKB040118の対象行を見つけます。
［操作（入力）］
(SDSF Result)
COMMAND INPUT ===&gt; FIND RIM (Resource Init
CASE OSKB040118
→ Enter を押す
［画面・出力］
(SDSF Result)
ITEM RIM (Resource Init
CASE OSKB040118
SOURCE HLASM and z/OS System Programming
RIM (Resource InitとOSKB040118が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はSDSFの詳細表示です。ASMA90IとOSKB040118を同じ出力で読み、復旧整理のアセンブラーの根拠を記録します。
［操作（入力）］
(SDSF Detail)
COMMAND INPUT ===&gt; ST OSKBASM
CASE OSKB040118
→ Enter を押す
［画面・出力］
SDSF OUTPUT FOR OSKB040118
ASMA90I RIM (Resource Initializa ASSEMBLY OR BINDER DIAGNOSTIC
IEW2646I 4 ESD/XSD PROCESSING COMPLETED
IEW2456I 0 SYMBOL RESOLUTION COMPLETED
ASMA90IとOSKB040118が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; ST OSKBASM が画面・出力に表示されること
② ステップ2 の RIM (Resource Init と OSKB040118 が画面・出力に表示されること
③ ステップ3 の ASMA90I と OSKB040118 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: メインフレーム実践 (神居俊哉)、アドバンスドスキル Vol.2 (神居俊哉 / 髙尾司) [zOS31_ieae200] [zOS31_ieam400]</p></div></details></section>
