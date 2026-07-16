---
search:
  exclude: true
---

# RACF SETROPTS/RDEFINE/RACDCERT — 詳細 (2/2)

[← RACF SETROPTS/RDEFINE/RACDCERT の概要へ戻る](index.md)


## RDEFINE APPL


<section class="kb-item" id="c26-i0229"><h3>APPL クラス</h3><p class="kb-meta">分類: RDEFINE APPL ・ 難易度: 上級</p><p>APPL クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE APPLで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>APPL クラス</strong></p><p>検証目的: 出力判定のクラスについて、APPL クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE APPL で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020088の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、出力判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にAPPL クラスを指定し、OSKB020088の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND APPL クラス
CASE OSKB020088
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM APPL クラス
CASE OSKB020088
SOURCE RACF
APPL クラスとOSKB020088が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020088を同じ出力で読み、出力判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020088
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020088 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I APPL クラス INFORMATION LISTED
IRRD105IとOSKB020088が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の APPL クラス と OSKB020088 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020088 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE CONSOLE


<section class="kb-item" id="c26-i0230"><h3>CONSOLE クラス</h3><p class="kb-meta">分類: RDEFINE CONSOLE ・ 難易度: 上級</p><p>CONSOLE クラスは、コンソール デバイスのアクセス制御。「CONSOLE クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CONSOLE クラス</strong></p><p>検証目的: 条件判定のクラスについて、CONSOLE クラスは、コンソール デバイスのアクセス制御。「CONSOLE クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020089の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、条件判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にCONSOLE クラスを指定し、OSKB020089の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND CONSOLE クラス
CASE OSKB020089
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM CONSOLE クラス
CASE OSKB020089
SOURCE RACF
CONSOLE クラスとOSKB020089が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020089を同じ出力で読み、条件判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020089
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020089 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I CONSOLE クラス INFORMATION LISTED
IRRD105IとOSKB020089が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の CONSOLE クラス と OSKB020089 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020089 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE CSFKEYS


<section class="kb-item" id="c26-i0231"><h3>CSFKEYS クラス</h3><p class="kb-meta">分類: RDEFINE CSFKEYS ・ 難易度: 上級</p><p>CSFKEYS クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE CSFKEYSで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CSFKEYS クラス</strong></p><p>検証目的: 記録判定のクラスについて、CSFKEYS クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE CSFKEYS で認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020093の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、記録判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にCSFKEYS クラスを指定し、OSKB020093の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND CSFKEYS クラス
CASE OSKB020093
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM CSFKEYS クラス
CASE OSKB020093
SOURCE RACF
CSFKEYS クラスとOSKB020093が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020093を同じ出力で読み、記録判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020093
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020093 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I CSFKEYS クラス INFORMATION LISTED
IRRD105IとOSKB020093が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の CSFKEYS クラス と OSKB020093 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020093 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE CSFSERV


<section class="kb-item" id="c26-i0232"><h3>CSFSERV クラス</h3><p class="kb-meta">分類: RDEFINE CSFSERV ・ 難易度: 上級</p><p>CSFSERV クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE CSFSERVで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文確認のクラスに関係する CSFSERV クラスの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、構文確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. CSFSERV クラスの名称と担当者名のみを残して構文確認のクラスの表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で構文確認のクラスを確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず構文確認のクラスの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文確認のクラスにおいて選択記号 A を採用し、識別名は構文確認です。構文確認のクラスにおいて CSFSERV クラス は説明欄の「CSFSERV クラスの用途をセキュリティ設定の表示で確認する構文確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は構文確認です。構文確認のクラスに関連して、RACF では CSFSERV クラスの表示属性と IRRD105I を同じ証跡に残し、背景名は構文確認です。他の選択肢を確認します。 A: 構文確認のクラスは対象出力と項目説明を結び、根拠を残すので構文確認です。 B: 構文確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため構文確認ではありません。 C: 構文確認のクラスは別カテゴリの確認を流用しており、CSFSERV クラスの根拠にならないため構文確認ではありません。 D: 構文確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため構文確認ではありません。構文確認のクラスで使う CSFSERV クラスという用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は構文確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CSFSERV クラス</strong></p><p>検証目的: 比較判定のクラスについて、CSFSERV クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE CSFSERV で認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020094の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、比較判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にCSFSERV クラスを指定し、OSKB020094の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND CSFSERV クラス
CASE OSKB020094
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM CSFSERV クラス
CASE OSKB020094
SOURCE RACF
CSFSERV クラスとOSKB020094が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020094を同じ出力で読み、比較判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020094
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020094 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I CSFSERV クラス INFORMATION LISTED
IRRD105IとOSKB020094が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の CSFSERV クラス と OSKB020094 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020094 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE DIGTCERT


<section class="kb-item" id="c26-i0233"><h3>DIGTCERT クラス</h3><p class="kb-meta">分類: RDEFINE DIGTCERT ・ 難易度: 上級</p><p>DIGTCERT クラスは、デジタル証明書プロファイル (RACDCERT 管理)。「DIGTCERT クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開確認のクラスで DIGTCERT クラスの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. DIGTCERT クラスの出力を取らず展開確認のクラスの説明文と承認印のみを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、展開確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して展開確認のクラスの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開確認のクラスへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開確認のクラスにおいて選択記号 B を採用し、識別名は展開確認です。展開確認のクラスにおいて DIGTCERT クラス は説明欄の「展開確認のクラスに関係する定義値と表示行を照合する展開確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は展開確認です。展開確認のクラスの証跡を読む担当者は、DIGTCERT クラスの属性行と IRRD105I を合わせて追跡し、背景名は展開確認です。誤答側の問題点を分けます。 A: 展開確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため展開確認ではありません。 B: 展開確認のクラスは対象出力と項目説明を結び、根拠を残すので展開確認です。 C: 展開確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため展開確認ではありません。 D: 展開確認のクラスは別カテゴリの確認を流用しており、DIGTCERT クラスの根拠にならないため展開確認ではありません。展開確認のクラスに出る DIGTCERT クラスは RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は展開確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DIGTCERT クラス</strong></p><p>検証目的: 順序判定のクラスについて、DIGTCERT クラスは、デジタル証明書プロファイル (RACDCERT 管理)。「DIGTCERT クラス」を確認すると、SETROPTS、RDEFINE、RACDCEに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020095の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、順序判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にDIGTCERT クラスを指定し、OSKB020095の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND DIGTCERT クラス
CASE OSKB020095
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM DIGTCERT クラス
CASE OSKB020095
SOURCE RACF
DIGTCERT クラスとOSKB020095が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020095を同じ出力で読み、順序判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020095
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020095 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I DIGTCERT クラス INFORMATION LISTED
IRRD105IとOSKB020095が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の DIGTCERT クラス と OSKB020095 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020095 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE DIGTNMAP


<section class="kb-item" id="c26-i0234"><h3>DIGTNMAP クラス</h3><p class="kb-meta">分類: RDEFINE DIGTNMAP ・ 難易度: 上級</p><p>DIGTNMAP クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE DIGTNMAPで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換確認のクラスに関する DIGTNMAP クラスの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず置換確認のクラスの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換確認のクラスの証跡として保存して根拠にする。</li><li>C. DIGTNMAP クラスの変更点を出力本文から切り離して置換確認のクラスの承認欄のみ残す。</li><li>D. RACF の表示形式に沿って根拠行を採り、置換確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換確認のクラスにおいて選択記号 D を採用し、識別名は置換確認です。置換確認のクラスにおいて DIGTNMAP クラス は説明欄の「DIGTNMAP クラスの状態と出力メッセージを結び付ける置換確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は置換確認です。置換確認のクラスに関する記録は、DIGTNMAP クラスの出力行と IRRD105I を一緒に保存し、背景名は置換確認です。選択肢ごとの違いを示します。 A: 置換確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため置換確認ではありません。 B: 置換確認のクラスは別カテゴリの確認を流用しており、DIGTNMAP クラスの根拠にならないため置換確認ではありません。 C: 置換確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため置換確認ではありません。 D: 置換確認のクラスは対象出力と項目説明を結び、根拠を残すので置換確認です。置換確認のクラスで記録する DIGTNMAP クラスは RACF の確認記録に残す対象名であり、用語名は置換確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DIGTNMAP クラス</strong></p><p>検証目的: 警告判定のクラスについて、DIGTNMAP クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE DIGTNMAP で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020097の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、警告判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にDIGTNMAP クラスを指定し、OSKB020097の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND DIGTNMAP クラス
CASE OSKB020097
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM DIGTNMAP クラス
CASE OSKB020097
SOURCE RACF
DIGTNMAP クラスとOSKB020097が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020097を同じ出力で読み、警告判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020097
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020097 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I DIGTNMAP クラス INFORMATION LISTED
IRRD105IとOSKB020097が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の DIGTNMAP クラス と OSKB020097 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020097 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE DIGTRING


<section class="kb-item" id="c26-i0235"><h3>DIGTRING クラス</h3><p class="kb-meta">分類: RDEFINE DIGTRING ・ 難易度: 上級</p><p>DIGTRING クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE DIGTRINGで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出確認のクラスでセキュリティ設定の運用確認を行います。DIGTRING クラスの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で呼出確認のクラスを確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず呼出確認のクラスを正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. DIGTRING クラスの属性行を読まず呼出確認のクラスの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出確認のクラスにおいて選択記号 C を採用し、識別名は呼出確認です。呼出確認のクラスにおいて DIGTRING クラス は説明欄の「RACF で DIGTRING クラスの扱いを記録する呼出確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は呼出確認です。呼出確認のクラスを受け取る担当者は、DIGTRING クラスの表示結果と IRRD105I を同じ確認単位として扱い、背景名は呼出確認です。不適切な選択肢を整理します。 A: 呼出確認のクラスは別カテゴリの確認を流用しており、DIGTRING クラスの根拠にならないため呼出確認ではありません。 B: 呼出確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため呼出確認ではありません。 C: 呼出確認のクラスは対象出力と項目説明を結び、根拠を残すので呼出確認です。 D: 呼出確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出確認ではありません。呼出確認のクラスが示す DIGTRING クラスは出典欄の資料で使い方を追跡できる項目であり、用語名は呼出確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DIGTRING クラス</strong></p><p>検証目的: 値域判定のクラスについて、DIGTRING クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE DIGTRING で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020096の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、値域判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にDIGTRING クラスを指定し、OSKB020096の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND DIGTRING クラス
CASE OSKB020096
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM DIGTRING クラス
CASE OSKB020096
SOURCE RACF
DIGTRING クラスとOSKB020096が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020096を同じ出力で読み、値域判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020096
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020096 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I DIGTRING クラス INFORMATION LISTED
IRRD105IとOSKB020096が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の DIGTRING クラス と OSKB020096 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020096 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE FACILITY


<section class="kb-item" id="c26-i0236"><h3>BPX.* プロファイル</h3><p class="kb-meta">分類: RDEFINE FACILITY ・ 難易度: 上級</p><p>BPX.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE FACILITYで認証、権限、またはセキュリティ設定を確認する項目です。BPX.* プロファイルは、z/OS UNIX 関連権限 (BPX.SUPERUSER 等)。「BPX.* プロファイル」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>BPX.* プロファイル</strong></p><p>検証目的: 復旧照合の* プロファイルについて、BPX.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE FACILITY で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020038の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、復旧照合の* プロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にBPX.* プロファイルを指定し、OSKB020038の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND BPX.* プロファイル
CASE OSKB020038
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM BPX.* プロファイル
CASE OSKB020038
SOURCE RACF
BPX.* プロファイルとOSKB020038が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020038を同じ出力で読み、復旧照合の* プロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020038
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020038 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I BPX.* プロファイル INFORMATION LISTED
IRRD105IとOSKB020038が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の BPX.* プロファイル と OSKB020038 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020038 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0237"><h3>FACILITY クラスの用途</h3><p class="kb-meta">分類: RDEFINE FACILITY ・ 難易度: 上級</p><p>FACILITY クラスの用途は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE FACILITYで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FACILITY クラスの用途</strong></p><p>検証目的: 警告照合のクラスの用途について、FACILITY クラスの用途は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE FACILITY で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020037の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、警告照合のクラスの用途の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にFACILITY クラスの用途を指定し、OSKB020037の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND FACILITY クラスの用途
CASE OSKB020037
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM FACILITY クラスの用途
CASE OSKB020037
SOURCE RACF
FACILITY クラスの用途とOSKB020037が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020037を同じ出力で読み、警告照合のクラスの用途の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020037
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020037 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I FACILITY クラスの用途 INFORMATION LISTED
IRRD105IとOSKB020037が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の FACILITY クラスの用途 と OSKB020037 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020037 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0238"><h3>IRR.* プロファイル</h3><p class="kb-meta">分類: RDEFINE FACILITY ・ 難易度: 上級</p><p>IRR.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE FACILITYで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRR.* プロファイル</strong></p><p>検証目的: 監査照合の* プロファイルについて、IRR.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE FACILITY で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020039の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、監査照合の* プロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRR.* プロファイルを指定し、OSKB020039の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRR.* プロファイル
CASE OSKB020039
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRR.* プロファイル
CASE OSKB020039
SOURCE RACF
IRR.* プロファイルとOSKB020039が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020039を同じ出力で読み、監査照合の* プロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020039
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020039 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRR.* プロファイル INFORMATION LISTED
IRRD105IとOSKB020039が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRR.* プロファイル と OSKB020039 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020039 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0239"><h3>STGADMIN.* プロファイル</h3><p class="kb-meta">分類: RDEFINE FACILITY ・ 難易度: 上級</p><p>STGADMIN.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE FACILITYで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STGADMIN.* プロファイル</strong></p><p>検証目的: 変更照合の* プロファイルについて、STGADMIN.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE FACILITY で認証、権限、またはセキュリティ設定を確に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020040の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、変更照合の* プロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSTGADMIN.* プロファイルを指定し、OSKB020040の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND STGADMIN.* プロファイル
CASE OSKB020040
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM STGADMIN.* プロファイル
CASE OSKB020040
SOURCE RACF
STGADMIN.* プロファイルとOSKB020040が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020040を同じ出力で読み、変更照合の* プロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020040
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020040 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I STGADMIN.* プロファイル INFORMATION LISTED
IRRD105IとOSKB020040が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の STGADMIN.* プロファイル と OSKB020040 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020040 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE JES


<section class="kb-item" id="c26-i0240"><h3>JESINPUT クラス</h3><p class="kb-meta">分類: RDEFINE JES ・ 難易度: 上級</p><p>JESINPUT クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>JESINPUT クラス</strong></p><p>検証目的: 範囲追跡のクラスについて、JESINPUT クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020051の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、範囲追跡のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にJESINPUT クラスを指定し、OSKB020051の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND JESINPUT クラス
CASE OSKB020051
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM JESINPUT クラス
CASE OSKB020051
SOURCE RACF
JESINPUT クラスとOSKB020051が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020051を同じ出力で読み、範囲追跡のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020051
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020051 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I JESINPUT クラス INFORMATION LISTED
IRRD105IとOSKB020051が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の JESINPUT クラス と OSKB020051 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020051 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0241"><h3>JESJOBS CANCEL.nodeid.userid.jobname</h3><p class="kb-meta">分類: RDEFINE JES ・ 難易度: 上級</p><p>JESJOBS CANCEL.nodeid.userid.jobnameは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


<section class="kb-item" id="c26-i0242"><h3>JESJOBS SUBMIT.nodeid.jobname.owner</h3><p class="kb-meta">分類: RDEFINE JES ・ 難易度: 上級</p><p>JESJOBS SUBMIT.nodeid.jobname.ownerは、ジョブ サブミット権限プロファイル。「JESJOBS SUBMIT.nodeid.jobname.owner」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


<section class="kb-item" id="c26-i0243"><h3>JESJOBS クラス</h3><p class="kb-meta">分類: RDEFINE JES ・ 難易度: 上級</p><p>JESJOBS クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>JESJOBS クラス</strong></p><p>検証目的: 優先追跡のクラスについて、JESJOBS クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020052の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、優先追跡のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にJESJOBS クラスを指定し、OSKB020052の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND JESJOBS クラス
CASE OSKB020052
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM JESJOBS クラス
CASE OSKB020052
SOURCE RACF
JESJOBS クラスとOSKB020052が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020052を同じ出力で読み、優先追跡のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020052
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020052 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I JESJOBS クラス INFORMATION LISTED
IRRD105IとOSKB020052が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の JESJOBS クラス と OSKB020052 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020052 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0244"><h3>JESSPOOL クラス</h3><p class="kb-meta">分類: RDEFINE JES ・ 難易度: 上級</p><p>JESSPOOL クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>JESSPOOL クラス</strong></p><p>検証目的: 順序追跡のクラスについて、JESSPOOL クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020055の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、順序追跡のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にJESSPOOL クラスを指定し、OSKB020055の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND JESSPOOL クラス
CASE OSKB020055
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM JESSPOOL クラス
CASE OSKB020055
SOURCE RACF
JESSPOOL クラスとOSKB020055が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020055を同じ出力で読み、順序追跡のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020055
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020055 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I JESSPOOL クラス INFORMATION LISTED
IRRD105IとOSKB020055が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の JESSPOOL クラス と OSKB020055 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020055 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0245"><h3>JESSPOOL プロファイル形式</h3><p class="kb-meta">分類: RDEFINE JES ・ 難易度: 上級</p><p>JESSPOOL プロファイル形式は、nodeid.userid.jobname.jobid.dsid.dsname。「JESSPOOL プロファイル形式」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>JESSPOOL プロファイル形式</strong></p><p>検証目的: 値域追跡のプロファイル形式について、JESSPOOL プロファイル形式は、nodeid.userid.jobname.jobid.dsid.dsname。「JESSPOOL プロファイル形式」を確認すると、Sに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020056の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、値域追跡のプロファイル形式の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にJESSPOOL プロファイル形式を指定し、OSKB020056の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND JESSPOOL プロファイル形式
CASE OSKB020056
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM JESSPOOL プロファイル形式
CASE OSKB020056
SOURCE RACF
JESSPOOL プロファイル形式とOSKB020056が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020056を同じ出力で読み、値域追跡のプロファイル形式の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020056
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020056 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I JESSPOOL プロファイル形式 INFORMATION LISTED
IRRD105IとOSKB020056が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の JESSPOOL プロファイル形式 と OSKB020056 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020056 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0246"><h3>NODES クラス</h3><p class="kb-meta">分類: RDEFINE JES ・ 難易度: 上級</p><p>NODES クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>NODES クラス</strong></p><p>検証目的: 復旧追跡のクラスについて、NODES クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020058の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、復旧追跡のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にNODES クラスを指定し、OSKB020058の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND NODES クラス
CASE OSKB020058
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM NODES クラス
CASE OSKB020058
SOURCE RACF
NODES クラスとOSKB020058が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020058を同じ出力で読み、復旧追跡のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020058
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020058 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I NODES クラス INFORMATION LISTED
IRRD105IとOSKB020058が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の NODES クラス と OSKB020058 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020058 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0247"><h3>WRITER クラス</h3><p class="kb-meta">分類: RDEFINE JES ・ 難易度: 上級</p><p>WRITER クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE JESで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WRITER クラス</strong></p><p>検証目的: 警告追跡のクラスについて、WRITER クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020057の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、警告追跡のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にWRITER クラスを指定し、OSKB020057の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND WRITER クラス
CASE OSKB020057
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM WRITER クラス
CASE OSKB020057
SOURCE RACF
WRITER クラスとOSKB020057が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020057を同じ出力で読み、警告追跡のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020057
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020057 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I WRITER クラス INFORMATION LISTED
IRRD105IとOSKB020057が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の WRITER クラス と OSKB020057 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020057 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE OPERCMDS


<section class="kb-item" id="c26-i0248"><h3>JES2.* プロファイル</h3><p class="kb-meta">分類: RDEFINE OPERCMDS ・ 難易度: 上級</p><p>JES2.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE OPERCMDSで状態表示や操作を行うためのコマンド関連項目です。JES2.* プロファイルは、JES2 コマンド。「JES2.* プロファイル」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>JES2.* プロファイル</strong></p><p>検証目的: 展開検査の* プロファイルについて、JES2.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE OPERCMDS で状態表示や操作を行うためのコマンド関連項目ですに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020062の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、展開検査の* プロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にJES2.* プロファイルを指定し、OSKB020062の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND JES2.* プロファイル
CASE OSKB020062
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM JES2.* プロファイル
CASE OSKB020062
SOURCE RACF
JES2.* プロファイルとOSKB020062が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020062を同じ出力で読み、展開検査の* プロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020062
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020062 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I JES2.* プロファイル INFORMATION LISTED
IRRD105IとOSKB020062が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の JES2.* プロファイル と OSKB020062 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020062 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0249"><h3>JES3.* プロファイル</h3><p class="kb-meta">分類: RDEFINE OPERCMDS ・ 難易度: 上級</p><p>JES3.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE OPERCMDSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>JES3.* プロファイル</strong></p><p>検証目的: 呼出検査の* プロファイルについて、JES3.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE OPERCMDS で状態表示や操作を行うためのコマンド関連項目ですに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020063の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、呼出検査の* プロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にJES3.* プロファイルを指定し、OSKB020063の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND JES3.* プロファイル
CASE OSKB020063
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM JES3.* プロファイル
CASE OSKB020063
SOURCE RACF
JES3.* プロファイルとOSKB020063が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020063を同じ出力で読み、呼出検査の* プロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020063
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020063 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I JES3.* プロファイル INFORMATION LISTED
IRRD105IとOSKB020063が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の JES3.* プロファイル と OSKB020063 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020063 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0250"><h3>MVS.* プロファイル</h3><p class="kb-meta">分類: RDEFINE OPERCMDS ・ 難易度: 上級</p><p>MVS.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE OPERCMDSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MVS.* プロファイル</strong></p><p>検証目的: 構文検査の* プロファイルについて、MVS.* プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE OPERCMDS で状態表示や操作を行うためのコマンド関連項目です。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020061の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、構文検査の* プロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にMVS.* プロファイルを指定し、OSKB020061の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND MVS.* プロファイル
CASE OSKB020061
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM MVS.* プロファイル
CASE OSKB020061
SOURCE RACF
MVS.* プロファイルとOSKB020061が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020061を同じ出力で読み、構文検査の* プロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020061
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020061 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I MVS.* プロファイル INFORMATION LISTED
IRRD105IとOSKB020061が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の MVS.* プロファイル と OSKB020061 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020061 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0251"><h3>OPERCMDS クラス</h3><p class="kb-meta">分類: RDEFINE OPERCMDS ・ 難易度: 上級</p><p>OPERCMDS クラスは、コンソール オペレータ コマンドのアクセス制御。「OPERCMDS クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>OPERCMDS クラス</strong></p><p>検証目的: 監査追跡のクラスについて、OPERCMDS クラスは、コンソール オペレータ コマンドのアクセス制御。「OPERCMDS クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020059の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、監査追跡のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にOPERCMDS クラスを指定し、OSKB020059の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND OPERCMDS クラス
CASE OSKB020059
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM OPERCMDS クラス
CASE OSKB020059
SOURCE RACF
OPERCMDS クラスとOSKB020059が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020059を同じ出力で読み、監査追跡のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020059
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020059 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I OPERCMDS クラス INFORMATION LISTED
IRRD105IとOSKB020059が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の OPERCMDS クラス と OSKB020059 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020059 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0252"><h3>プロファイル形式</h3><p class="kb-meta">分類: RDEFINE OPERCMDS ・ 難易度: 上級</p><p>プロファイル形式は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE OPERCMDSで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プロファイル形式</strong></p><p>検証目的: 変更追跡のプロファイル形式について、プロファイル形式は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE OPERCMDS で状態表示や操作を行うためのコマンド関連項目です。実行対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020060の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、変更追跡のプロファイル形式の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にプロファイル形式を指定し、OSKB020060の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND プロファイル形式
CASE OSKB020060
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM プロファイル形式
CASE OSKB020060
SOURCE RACF
プロファイル形式とOSKB020060が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020060を同じ出力で読み、変更追跡のプロファイル形式の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020060
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020060 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I プロファイル形式 INFORMATION LISTED
IRRD105IとOSKB020060が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の プロファイル形式 と OSKB020060 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020060 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE PROGRAM


<section class="kb-item" id="c26-i0253"><h3>ADDMEM(library/volser/PADCHK)</h3><p class="kb-meta">分類: RDEFINE PROGRAM ・ 難易度: 上級</p><p>ADDMEM(library/volser/PADCHK)は、対象ライブラリ・ボリューム・PADS チェック有無。「ADDMEM(library/volser/PADCHK)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ADDMEM(library・volser・ PADCHK)</strong></p><p>検証目的: 終端検査の・ ・について、ADDMEM(library/volser/PADCHK)は、対象ライブラリ・ボリューム・ PADS チェック有無。「ADDMEM(library/volser/PADCHKに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020065の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、終端検査の・ ・の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にADDMEM(library・volを指定し、OSKB020065の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND ADDMEM(library・vol
CASE OSKB020065
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM ADDMEM(library・vol
CASE OSKB020065
SOURCE RACF
ADDMEM(library・volとOSKB020065が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020065を同じ出力で読み、終端検査の・ ・の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020065
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020065 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I ADDMEM(library・volser・ PA INFORMATION LISTED
IRRD105IとOSKB020065が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の ADDMEM(library・vol と OSKB020065 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020065 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0254"><h3>PADCHK/NOPADCHK</h3><p class="kb-meta">分類: RDEFINE PROGRAM ・ 難易度: 上級</p><p>PADCHK/NOPADCHKは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE PROGRAMで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PADCHK ・ NOPADCHK</strong></p><p>検証目的: 探索検査の・について、PADCHK/NOPADCHK は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE PROGRAM で認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020066の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、探索検査の・の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にPADCHK ・ NOPADCHKを指定し、OSKB020066の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND PADCHK ・ NOPADCHK
CASE OSKB020066
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM PADCHK ・ NOPADCHK
CASE OSKB020066
SOURCE RACF
PADCHK ・ NOPADCHKとOSKB020066が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020066を同じ出力で読み、探索検査の・の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020066
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020066 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I PADCHK ・ NOPADCHK INFORMATION LISTED
IRRD105IとOSKB020066が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の PADCHK ・ NOPADCHK と OSKB020066 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020066 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0255"><h3>PROGRAM クラス</h3><p class="kb-meta">分類: RDEFINE PROGRAM ・ 難易度: 上級</p><p>PROGRAM クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE PROGRAMで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PROGRAM クラス</strong></p><p>検証目的: 置換検査のクラスについて、PROGRAM クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE PROGRAM で認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020064の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、置換検査のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にPROGRAM クラスを指定し、OSKB020064の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND PROGRAM クラス
CASE OSKB020064
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM PROGRAM クラス
CASE OSKB020064
SOURCE RACF
PROGRAM クラスとOSKB020064が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020064を同じ出力で読み、置換検査のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020064
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020064 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I PROGRAM クラス INFORMATION LISTED
IRRD105IとOSKB020064が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の PROGRAM クラス と OSKB020064 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020064 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0256"><h3>WHEN(PROGRAM) 連携</h3><p class="kb-meta">分類: RDEFINE PROGRAM ・ 難易度: 上級</p><p>WHEN(PROGRAM) 連携は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE PROGRAMで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WHEN(PROGRAM) 連携</strong></p><p>検証目的: 上書検査の連携について、WHEN(PROGRAM) 連携は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE PROGRAM で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020067の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、上書検査の連携の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にWHEN(PROGRAM) 連携を指定し、OSKB020067の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND WHEN(PROGRAM) 連携
CASE OSKB020067
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM WHEN(PROGRAM) 連携
CASE OSKB020067
SOURCE RACF
WHEN(PROGRAM) 連携とOSKB020067が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020067を同じ出力で読み、上書検査の連携の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020067
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020067 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I WHEN(PROGRAM) 連携 INFORMATION LISTED
IRRD105IとOSKB020067が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の WHEN(PROGRAM) 連携 と OSKB020067 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020067 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE SDSF


<section class="kb-item" id="c26-i0257"><h3>ISFAUTH プロファイル</h3><p class="kb-meta">分類: RDEFINE SDSF ・ 難易度: 上級</p><p>ISFAUTH プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SDSFで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ISFAUTH プロファイル</strong></p><p>検証目的: 区切検査のプロファイルについて、ISFAUTH プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SDSF で認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020070の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、区切検査のプロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にISFAUTH プロファイルを指定し、OSKB020070の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND ISFAUTH プロファイル
CASE OSKB020070
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM ISFAUTH プロファイル
CASE OSKB020070
SOURCE RACF
ISFAUTH プロファイルとOSKB020070が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020070を同じ出力で読み、区切検査のプロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020070
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020070 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I ISFAUTH プロファイル INFORMATION LISTED
IRRD105IとOSKB020070が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の ISFAUTH プロファイル と OSKB020070 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020070 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0258"><h3>ISFCMD プロファイル</h3><p class="kb-meta">分類: RDEFINE SDSF ・ 難易度: 上級</p><p>ISFCMD プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SDSFで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ISFCMD プロファイル</strong></p><p>検証目的: 条件検査のプロファイルについて、ISFCMD プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SDSF で状態表示や操作を行うためのコマンド関連項目です。実行対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020069の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、条件検査のプロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にISFCMD プロファイルを指定し、OSKB020069の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND ISFCMD プロファイル
CASE OSKB020069
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM ISFCMD プロファイル
CASE OSKB020069
SOURCE RACF
ISFCMD プロファイルとOSKB020069が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020069を同じ出力で読み、条件検査のプロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020069
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020069 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I ISFCMD プロファイル INFORMATION LISTED
IRRD105IとOSKB020069が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の ISFCMD プロファイル と OSKB020069 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020069 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0259"><h3>ISFOPER プロファイル</h3><p class="kb-meta">分類: RDEFINE SDSF ・ 難易度: 上級</p><p>ISFOPER プロファイルは、オペレータ コマンド権限。「ISFOPER プロファイル」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ISFOPER プロファイル</strong></p><p>検証目的: 範囲検査のプロファイルについて、ISFOPER プロファイルは、オペレータ コマンド権限。「ISFOPER プロファイル」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020071の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、範囲検査のプロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にISFOPER プロファイルを指定し、OSKB020071の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND ISFOPER プロファイル
CASE OSKB020071
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM ISFOPER プロファイル
CASE OSKB020071
SOURCE RACF
ISFOPER プロファイルとOSKB020071が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020071を同じ出力で読み、範囲検査のプロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020071
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020071 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I ISFOPER プロファイル INFORMATION LISTED
IRRD105IとOSKB020071が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の ISFOPER プロファイル と OSKB020071 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020071 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0260"><h3>SDSF クラス</h3><p class="kb-meta">分類: RDEFINE SDSF ・ 難易度: 上級</p><p>SDSF クラスは、SDSF パネル/コマンド/カラムのアクセス制御。「SDSF クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SDSF クラス</strong></p><p>検証目的: 出力検査のクラスについて、SDSF クラスは、SDSF パネル/コマンド/カラムのアクセス制御。「SDSF クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020068の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、出力検査のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSDSF クラスを指定し、OSKB020068の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SDSF クラス
CASE OSKB020068
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SDSF クラス
CASE OSKB020068
SOURCE RACF
SDSF クラスとOSKB020068が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020068を同じ出力で読み、出力検査のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020068
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020068 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SDSF クラス INFORMATION LISTED
IRRD105IとOSKB020068が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SDSF クラス と OSKB020068 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020068 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE SECDATA


<section class="kb-item" id="c26-i0261"><h3>CATEGORY プロファイル</h3><p class="kb-meta">分類: RDEFINE SECDATA ・ 難易度: 上級</p><p>CATEGORY プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SECDATAで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CATEGORY プロファイル</strong></p><p>検証目的: 終端判定のプロファイルについて、CATEGORY プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SECDATA で認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020085の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、終端判定のプロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にCATEGORY プロファイルを指定し、OSKB020085の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND CATEGORY プロファイル
CASE OSKB020085
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM CATEGORY プロファイル
CASE OSKB020085
SOURCE RACF
CATEGORY プロファイルとOSKB020085が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020085を同じ出力で読み、終端判定のプロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020085
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020085 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I CATEGORY プロファイル INFORMATION LISTED
IRRD105IとOSKB020085が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の CATEGORY プロファイル と OSKB020085 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020085 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0262"><h3>SECDATA クラス</h3><p class="kb-meta">分類: RDEFINE SECDATA ・ 難易度: 上級</p><p>SECDATA クラスは、SECLEVEL/CATEGORY 定義用。「SECDATA クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SECDATA クラス</strong></p><p>検証目的: 呼出判定のクラスについて、SECDATA クラスは、SECLEVEL/CATEGORY 定義用。「SECDATA クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020083の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、呼出判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSECDATA クラスを指定し、OSKB020083の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SECDATA クラス
CASE OSKB020083
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SECDATA クラス
CASE OSKB020083
SOURCE RACF
SECDATA クラスとOSKB020083が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020083を同じ出力で読み、呼出判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020083
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020083 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SECDATA クラス INFORMATION LISTED
IRRD105IとOSKB020083が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SECDATA クラス と OSKB020083 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020083 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0263"><h3>SECLEVEL プロファイル</h3><p class="kb-meta">分類: RDEFINE SECDATA ・ 難易度: 上級</p><p>SECLEVEL プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SECDATAで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SECLEVEL プロファイル</strong></p><p>検証目的: 置換判定のプロファイルについて、SECLEVEL プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SECDATA で認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020084の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、置換判定のプロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSECLEVEL プロファイルを指定し、OSKB020084の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SECLEVEL プロファイル
CASE OSKB020084
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SECLEVEL プロファイル
CASE OSKB020084
SOURCE RACF
SECLEVEL プロファイルとOSKB020084が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020084を同じ出力で読み、置換判定のプロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020084
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020084 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SECLEVEL プロファイル INFORMATION LISTED
IRRD105IとOSKB020084が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SECLEVEL プロファイル と OSKB020084 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020084 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE SECLABEL


<section class="kb-item" id="c26-i0264"><h3>SECLABEL クラス</h3><p class="kb-meta">分類: RDEFINE SECLABEL ・ 難易度: 上級</p><p>SECLABEL クラスは、MLS 環境のセキュリティ ラベル。「SECLABEL クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SECLABEL クラス</strong></p><p>検証目的: 探索判定のクラスについて、SECLABEL クラスは、MLS 環境のセキュリティ ラベル。「SECLABEL クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020086の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、探索判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSECLABEL クラスを指定し、OSKB020086の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SECLABEL クラス
CASE OSKB020086
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SECLABEL クラス
CASE OSKB020086
SOURCE RACF
SECLABEL クラスとOSKB020086が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020086を同じ出力で読み、探索判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020086
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020086 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SECLABEL クラス INFORMATION LISTED
IRRD105IとOSKB020086が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SECLABEL クラス と OSKB020086 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020086 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0265"><h3>SECLABEL システムラベル</h3><p class="kb-meta">分類: RDEFINE SECLABEL ・ 難易度: 上級</p><p>SECLABEL システムラベルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SECLABELで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SECLABEL システムラベル</strong></p><p>検証目的: 上書判定のシステムラベルについて、SECLABEL システムラベルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SECLABEL で認証、権限、またはセキュリティ設定を確認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020087の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、上書判定のシステムラベルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSECLABEL システムラベルを指定し、OSKB020087の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SECLABEL システムラベル
CASE OSKB020087
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SECLABEL システムラベル
CASE OSKB020087
SOURCE RACF
SECLABEL システムラベルとOSKB020087が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020087を同じ出力で読み、上書判定のシステムラベルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020087
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020087 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SECLABEL システムラベル INFORMATION LISTED
IRRD105IとOSKB020087が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SECLABEL システムラベル と OSKB020087 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020087 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE SERVAUTH


<section class="kb-item" id="c26-i0266"><h3>EZB.PORTACCESS</h3><p class="kb-meta">分類: RDEFINE SERVAUTH ・ 難易度: 上級</p><p>EZB.PORTACCESSは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SERVAUTHで認証、権限、またはセキュリティ設定を確認する項目です。EZB.PORTACCESSは、予約ポート使用権。「EZB.PORTACCESS」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EZB.PORTACCESS</strong></p><p>検証目的: 優先判定のセキュリティ設定について、EZB.PORTACCESS は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SERVAUTH で認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020092の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、優先判定のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にEZB.PORTACCESSを指定し、OSKB020092の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND EZB.PORTACCESS
CASE OSKB020092
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM EZB.PORTACCESS
CASE OSKB020092
SOURCE RACF
EZB.PORTACCESSとOSKB020092が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020092を同じ出力で読み、優先判定のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020092
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020092 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I EZB.PORTACCESS INFORMATION LISTED
IRRD105IとOSKB020092が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の EZB.PORTACCESS と OSKB020092 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020092 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0267"><h3>EZB.STACKACCESS</h3><p class="kb-meta">分類: RDEFINE SERVAUTH ・ 難易度: 上級</p><p>EZB.STACKACCESSは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SERVAUTHで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EZB.STACKACCESS</strong></p><p>検証目的: 範囲判定のセキュリティ設定について、EZB.STACKACCESS は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SERVAUTH で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020091の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、範囲判定のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にEZB.STACKACCESSを指定し、OSKB020091の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND EZB.STACKACCESS
CASE OSKB020091
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM EZB.STACKACCESS
CASE OSKB020091
SOURCE RACF
EZB.STACKACCESSとOSKB020091が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020091を同じ出力で読み、範囲判定のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020091
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020091 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I EZB.STACKACCESS INFORMATION LISTED
IRRD105IとOSKB020091が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の EZB.STACKACCESS と OSKB020091 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020091 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0268"><h3>SERVAUTH クラス</h3><p class="kb-meta">分類: RDEFINE SERVAUTH ・ 難易度: 上級</p><p>SERVAUTH クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SERVAUTHで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SERVAUTH クラス</strong></p><p>検証目的: 区切判定のクラスについて、SERVAUTH クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SERVAUTH で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020090の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、区切判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSERVAUTH クラスを指定し、OSKB020090の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SERVAUTH クラス
CASE OSKB020090
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SERVAUTH クラス
CASE OSKB020090
SOURCE RACF
SERVAUTH クラスとOSKB020090が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020090を同じ出力で読み、区切判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020090
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020090 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SERVAUTH クラス INFORMATION LISTED
IRRD105IとOSKB020090が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SERVAUTH クラス と OSKB020090 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020090 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE STARTED


<section class="kb-item" id="c26-i0269"><h3>STARTED と ICHRIN03 の関係</h3><p class="kb-meta">分類: RDEFINE STARTED ・ 難易度: 上級</p><p>STARTED クラスは ICHRIN03 テーブルの動的版。「STARTED と ICHRIN03 の関係」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STARTED と ICHRIN03 の関係</strong></p><p>検証目的: 上書追跡のと の関係について、STARTED クラスは ICHRIN03 テーブルの動的版。「STARTED と ICHRIN03 の関係」を確認すると、SETROPTS、RDEFINE、RACDCERに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020047の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、上書追跡のと の関係の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSTARTED と ICHRIN03を指定し、OSKB020047の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND STARTED と ICHRIN03
CASE OSKB020047
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM STARTED と ICHRIN03
CASE OSKB020047
SOURCE RACF
STARTED と ICHRIN03とOSKB020047が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020047を同じ出力で読み、上書追跡のと の関係の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020047
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020047 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I STARTED と ICHRIN03 の関係 INFORMATION LISTED
IRRD105IとOSKB020047が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の STARTED と ICHRIN03 と OSKB020047 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020047 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0270"><h3>STARTED クラスの用途</h3><p class="kb-meta">分類: RDEFINE STARTED ・ 難易度: 上級</p><p>STARTED クラスの用途は、STC (Started Task) にユーザ/グループ ID を割当。「STARTED クラスの用途」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STARTED クラスの用途</strong></p><p>検証目的: 構文追跡のクラスの用途について、STARTED クラスの用途は、STC (Started Task) にユーザ/グループ ID を割当。「STARTED クラスの用途」を確認すると、SETROPTS、RDに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020041の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、構文追跡のクラスの用途の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSTARTED クラスの用途を指定し、OSKB020041の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND STARTED クラスの用途
CASE OSKB020041
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM STARTED クラスの用途
CASE OSKB020041
SOURCE RACF
STARTED クラスの用途とOSKB020041が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020041を同じ出力で読み、構文追跡のクラスの用途の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020041
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020041 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I STARTED クラスの用途 INFORMATION LISTED
IRRD105IとOSKB020041が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の STARTED クラスの用途 と OSKB020041 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020041 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0271"><h3>STDATA セグメント</h3><p class="kb-meta">分類: RDEFINE STARTED ・ 難易度: 上級</p><p>STDATA セグメントは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE STARTEDで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STDATA セグメント</strong></p><p>検証目的: 展開追跡のセグメントについて、STDATA セグメントは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE STARTED で認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020042の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、展開追跡のセグメントの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSTDATA セグメントを指定し、OSKB020042の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND STDATA セグメント
CASE OSKB020042
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM STDATA セグメント
CASE OSKB020042
SOURCE RACF
STDATA セグメントとOSKB020042が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020042を同じ出力で読み、展開追跡のセグメントの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020042
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020042 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I STDATA セグメント INFORMATION LISTED
IRRD105IとOSKB020042が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の STDATA セグメント と OSKB020042 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020042 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0272"><h3>STDATA(GROUP(id))</h3><p class="kb-meta">分類: RDEFINE STARTED ・ 難易度: 上級</p><p>STDATA(GROUP(id))は、STC グループ ID。「STDATA(GROUP(id))」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STDATA(GROUP(id))</strong></p><p>検証目的: 置換追跡のセキュリティ設定について、STDATA(GROUP(id))は、STC グループ ID。「STDATA(GROUP(id))」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020044の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、置換追跡のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSTDATA(GROUP(id))を指定し、OSKB020044の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND STDATA(GROUP(id))
CASE OSKB020044
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM STDATA(GROUP(id))
CASE OSKB020044
SOURCE RACF
STDATA(GROUP(id))とOSKB020044が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020044を同じ出力で読み、置換追跡のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020044
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020044 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I STDATA(GROUP(id)) INFORMATION LISTED
IRRD105IとOSKB020044が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の STDATA(GROUP(id)) と OSKB020044 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020044 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0273"><h3>STDATA(PRIVILEGED(YES))</h3><p class="kb-meta">分類: RDEFINE STARTED ・ 難易度: 上級</p><p>STDATA(PRIVILEGED(YES))は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE STARTEDで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STDATA(PRIVILEGED(YES))</strong></p><p>検証目的: 探索追跡のセキュリティ設定について、STDATA(PRIVILEGED(YES))は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE STARTED で認証、権限、またはセキュリテに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020046の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、探索追跡のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSTDATA(PRIVILEGED(を指定し、OSKB020046の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND STDATA(PRIVILEGED(
CASE OSKB020046
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM STDATA(PRIVILEGED(
CASE OSKB020046
SOURCE RACF
STDATA(PRIVILEGED(とOSKB020046が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020046を同じ出力で読み、探索追跡のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020046
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020046 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I STDATA(PRIVILEGED(YES)) INFORMATION LISTED
IRRD105IとOSKB020046が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の STDATA(PRIVILEGED( と OSKB020046 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020046 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0274"><h3>STDATA(TRUSTED(YES))</h3><p class="kb-meta">分類: RDEFINE STARTED ・ 難易度: 上級</p><p>STDATA(TRUSTED(YES))は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE STARTEDで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STDATA(TRUSTED(YES))</strong></p><p>検証目的: 終端追跡のセキュリティ設定について、STDATA(TRUSTED(YES))は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE STARTED で認証、権限、またはセキュリティ設定に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020045の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、終端追跡のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSTDATA(TRUSTED(YESを指定し、OSKB020045の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND STDATA(TRUSTED(YES
CASE OSKB020045
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM STDATA(TRUSTED(YES
CASE OSKB020045
SOURCE RACF
STDATA(TRUSTED(YESとOSKB020045が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020045を同じ出力で読み、終端追跡のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020045
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020045 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I STDATA(TRUSTED(YES)) INFORMATION LISTED
IRRD105IとOSKB020045が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の STDATA(TRUSTED(YES と OSKB020045 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020045 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0275"><h3>STDATA(USER(id))</h3><p class="kb-meta">分類: RDEFINE STARTED ・ 難易度: 上級</p><p>STDATA(USER(id))は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE STARTEDで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STDATA(USER(id))</strong></p><p>検証目的: 呼出追跡のセキュリティ設定について、STDATA(USER(id))は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE STARTED で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020043の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、呼出追跡のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSTDATA(USER(id))を指定し、OSKB020043の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND STDATA(USER(id))
CASE OSKB020043
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM STDATA(USER(id))
CASE OSKB020043
SOURCE RACF
STDATA(USER(id))とOSKB020043が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020043を同じ出力で読み、呼出追跡のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020043
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020043 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I STDATA(USER(id)) INFORMATION LISTED
IRRD105IとOSKB020043が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の STDATA(USER(id)) と OSKB020043 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020043 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE SURROGAT


<section class="kb-item" id="c26-i0276"><h3>BPX.SRV.userid プロファイル</h3><p class="kb-meta">分類: RDEFINE SURROGAT ・ 難易度: 上級</p><p>RACF SETROPTS RDEFINE RACDCERTのRDEFINE SURROGATでは、RACFプロファイル、権限、クラス定義を対応付けて確認します。RDEFINE SURROGATは、RACF SETROPTS RDEFINE RACDCERTの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、BPX.SRV.userid プロファイルの表記と許可される値を確認します。</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>BPX.SRV.userid プロファイル</strong></p><p>検証目的: 区切追跡のプロファイルについて、RACF SETROPTS RDEFINE RACDCERT の RDEFINE SURROGAT では、RACF プロファイル、権限、クラス定義を対応付けて確認します。RDEFIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020050の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、区切追跡のプロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にBPX.SRV.userid プロフを指定し、OSKB020050の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND BPX.SRV.userid プロフ
CASE OSKB020050
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM BPX.SRV.userid プロフ
CASE OSKB020050
SOURCE RACF
BPX.SRV.userid プロフとOSKB020050が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020050を同じ出力で読み、区切追跡のプロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020050
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020050 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I BPX.SRV.userid プロファイル INFORMATION LISTED
IRRD105IとOSKB020050が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の BPX.SRV.userid プロフ と OSKB020050 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020050 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0277"><h3>SURROGAT クラスの用途</h3><p class="kb-meta">分類: RDEFINE SURROGAT ・ 難易度: 上級</p><p>SURROGAT クラスの用途は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SURROGATで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SURROGAT クラスの用途</strong></p><p>検証目的: 出力追跡のクラスの用途について、SURROGAT クラスの用途は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SURROGAT で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020048の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、出力追跡のクラスの用途の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSURROGAT クラスの用途を指定し、OSKB020048の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SURROGAT クラスの用途
CASE OSKB020048
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SURROGAT クラスの用途
CASE OSKB020048
SOURCE RACF
SURROGAT クラスの用途とOSKB020048が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020048を同じ出力で読み、出力追跡のクラスの用途の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020048
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020048 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SURROGAT クラスの用途 INFORMATION LISTED
IRRD105IとOSKB020048が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SURROGAT クラスの用途 と OSKB020048 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020048 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0278"><h3>userid.SUBMIT プロファイル</h3><p class="kb-meta">分類: RDEFINE SURROGAT ・ 難易度: 上級</p><p>userid.SUBMIT プロファイルは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE SURROGATで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>userid.SUBMIT プロファイル</strong></p><p>検証目的: 条件追跡のプロファイルについて、userid.SUBMIT プロファイルは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE SURROGAT で認証、権限、またはセキュリティ設に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020049の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、条件追跡のプロファイルの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にuserid.SUBMIT プロファを指定し、OSKB020049の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND userid.SUBMIT プロファ
CASE OSKB020049
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM userid.SUBMIT プロファ
CASE OSKB020049
SOURCE RACF
userid.SUBMIT プロファとOSKB020049が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020049を同じ出力で読み、条件追跡のプロファイルの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020049
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020049 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I userid.SUBMIT プロファイル INFORMATION LISTED
IRRD105IとOSKB020049が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の userid.SUBMIT プロファ と OSKB020049 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020049 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE TSO


<section class="kb-item" id="c26-i0279"><h3>ACCTNUM クラス</h3><p class="kb-meta">分類: RDEFINE TSO ・ 難易度: 上級</p><p>ACCTNUM クラスは、TSO アカウント番号制御。「ACCTNUM クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ACCTNUM クラス</strong></p><p>検証目的: 比較検査のクラスについて、ACCTNUM クラスは、TSO アカウント番号制御。「ACCTNUM クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020074の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、比較検査のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にACCTNUM クラスを指定し、OSKB020074の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND ACCTNUM クラス
CASE OSKB020074
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM ACCTNUM クラス
CASE OSKB020074
SOURCE RACF
ACCTNUM クラスとOSKB020074が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020074を同じ出力で読み、比較検査のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020074
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020074 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I ACCTNUM クラス INFORMATION LISTED
IRRD105IとOSKB020074が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の ACCTNUM クラス と OSKB020074 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020074 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0280"><h3>PERFGRP クラス</h3><p class="kb-meta">分類: RDEFINE TSO ・ 難易度: 上級</p><p>PERFGRP クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE TSOで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PERFGRP クラス</strong></p><p>検証目的: 順序検査のクラスについて、PERFGRP クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE TSO で認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020075の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、順序検査のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にPERFGRP クラスを指定し、OSKB020075の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND PERFGRP クラス
CASE OSKB020075
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM PERFGRP クラス
CASE OSKB020075
SOURCE RACF
PERFGRP クラスとOSKB020075が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020075を同じ出力で読み、順序検査のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020075
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020075 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I PERFGRP クラス INFORMATION LISTED
IRRD105IとOSKB020075が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の PERFGRP クラス と OSKB020075 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020075 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0281"><h3>TSOAUTH クラス</h3><p class="kb-meta">分類: RDEFINE TSO ・ 難易度: 上級</p><p>TSOAUTH クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE TSOで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TSOAUTH クラス</strong></p><p>検証目的: 記録検査のクラスについて、TSOAUTH クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE TSO で認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020073の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、記録検査のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にTSOAUTH クラスを指定し、OSKB020073の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND TSOAUTH クラス
CASE OSKB020073
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM TSOAUTH クラス
CASE OSKB020073
SOURCE RACF
TSOAUTH クラスとOSKB020073が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020073を同じ出力で読み、記録検査のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020073
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020073 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I TSOAUTH クラス INFORMATION LISTED
IRRD105IとOSKB020073が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の TSOAUTH クラス と OSKB020073 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020073 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0282"><h3>TSOPROC クラス</h3><p class="kb-meta">分類: RDEFINE TSO ・ 難易度: 上級</p><p>TSOPROC クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE TSOで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TSOPROC クラス</strong></p><p>検証目的: 優先検査のクラスについて、TSOPROC クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE TSO で認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020072の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、優先検査のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にTSOPROC クラスを指定し、OSKB020072の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND TSOPROC クラス
CASE OSKB020072
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM TSOPROC クラス
CASE OSKB020072
SOURCE RACF
TSOPROC クラスとOSKB020072が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020072を同じ出力で読み、優先検査のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020072
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020072 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I TSOPROC クラス INFORMATION LISTED
IRRD105IとOSKB020072が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の TSOPROC クラス と OSKB020072 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020072 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE UNIXPRIV


<section class="kb-item" id="c26-i0283"><h3>CHOWN.UNRESTRICTED</h3><p class="kb-meta">分類: RDEFINE UNIXPRIV ・ 難易度: 上級</p><p>CHOWN.UNRESTRICTEDは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE UNIXPRIVで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CHOWN.UNRESTRICTED</strong></p><p>検証目的: 構文判定のセキュリティ設定について、CHOWN.UNRESTRICTED は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE UNIXPRIV で認証、権限、またはセキュリティ設定をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020081の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、構文判定のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にCHOWN.UNRESTRICTEDを指定し、OSKB020081の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND CHOWN.UNRESTRICTED
CASE OSKB020081
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM CHOWN.UNRESTRICTED
CASE OSKB020081
SOURCE RACF
CHOWN.UNRESTRICTEDとOSKB020081が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020081を同じ出力で読み、構文判定のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020081
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020081 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I CHOWN.UNRESTRICTED INFORMATION LISTED
IRRD105IとOSKB020081が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の CHOWN.UNRESTRICTED と OSKB020081 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020081 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0284"><h3>RESTRICTED.FILESYS.ACCESS</h3><p class="kb-meta">分類: RDEFINE UNIXPRIV ・ 難易度: 上級</p><p>RACF SETROPTS RDEFINE RACDCERTのRDEFINE UNIXPRIVでは、RACFプロファイル、権限、クラス定義を対応付けて確認します。RDEFINE UNIXPRIVは、RACF SETROPTS RDEFINE RACDCERTの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、RESTRICTED.FILESYS.ACCESSの表記と許可される値を確認します。</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RESTRICTED.FILESYS.ACCESS</strong></p><p>検証目的: 展開判定のセキュリティ設定について、RACF SETROPTS RDEFINE RACDCERT の RDEFINE UNIXPRIV では、RACF プロファイル、権限、クラス定義を対応付けて確認します。RDEFIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020082の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、展開判定のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRESTRICTED.FILESYSを指定し、OSKB020082の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RESTRICTED.FILESYS
CASE OSKB020082
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RESTRICTED.FILESYS
CASE OSKB020082
SOURCE RACF
RESTRICTED.FILESYSとOSKB020082が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020082を同じ出力で読み、展開判定のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020082
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020082 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RESTRICTED.FILESYS.ACCES INFORMATION LISTED
IRRD105IとOSKB020082が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RESTRICTED.FILESYS と OSKB020082 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020082 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0285"><h3>SUPERUSER.FILESYS</h3><p class="kb-meta">分類: RDEFINE UNIXPRIV ・ 難易度: 上級</p><p>SUPERUSER.FILESYSは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE UNIXPRIVで認証、権限、またはセキュリティ設定を確認する項目です。SUPERUSER.FILESYSは、ファイルシステム特権アクセス。「SUPERUSER.FILESYS」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SUPERUSER.FILESYS</strong></p><p>検証目的: 警告検査のセキュリティ設定について、SUPERUSER.FILESYS は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE UNIXPRIV で認証、権限、またはセキュリティ設定を確に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020077の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、警告検査のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSUPERUSER.FILESYSを指定し、OSKB020077の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SUPERUSER.FILESYS
CASE OSKB020077
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SUPERUSER.FILESYS
CASE OSKB020077
SOURCE RACF
SUPERUSER.FILESYSとOSKB020077が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020077を同じ出力で読み、警告検査のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020077
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020077 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SUPERUSER.FILESYS INFORMATION LISTED
IRRD105IとOSKB020077が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SUPERUSER.FILESYS と OSKB020077 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020077 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0286"><h3>SUPERUSER.FILESYS.CHOWN</h3><p class="kb-meta">分類: RDEFINE UNIXPRIV ・ 難易度: 上級</p><p>RACF SETROPTS RDEFINE RACDCERTのRDEFINE UNIXPRIVでは、RACFプロファイル、権限、クラス定義を対応付けて確認します。RDEFINE UNIXPRIVは、RACF SETROPTS RDEFINE RACDCERTの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、SUPERUSER.FILESYS.CHOWNの表記と許可される値を確認します。</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SUPERUSER.FILESYS.CHOWN</strong></p><p>検証目的: 監査検査のセキュリティ設定について、RACF SETROPTS RDEFINE RACDCERT の RDEFINE UNIXPRIV では、RACF プロファイル、権限、クラス定義を対応付けて確認します。RDEFIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020079の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、監査検査のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSUPERUSER.FILESYS.を指定し、OSKB020079の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SUPERUSER.FILESYS.
CASE OSKB020079
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SUPERUSER.FILESYS.
CASE OSKB020079
SOURCE RACF
SUPERUSER.FILESYS.とOSKB020079が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020079を同じ出力で読み、監査検査のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020079
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020079 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SUPERUSER.FILESYS.CHOWN INFORMATION LISTED
IRRD105IとOSKB020079が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SUPERUSER.FILESYS. と OSKB020079 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020079 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0287"><h3>SUPERUSER.FILESYS.MOUNT</h3><p class="kb-meta">分類: RDEFINE UNIXPRIV ・ 難易度: 上級</p><p>RACF SETROPTS RDEFINE RACDCERTのRDEFINE UNIXPRIVでは、RACFプロファイル、権限、クラス定義を対応付けて確認します。RDEFINE UNIXPRIVは、RACF SETROPTS RDEFINE RACDCERTの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、SUPERUSER.FILESYS.MOUNTの表記と許可される値を確認します。</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SUPERUSER.FILESYS.MOUNT</strong></p><p>検証目的: 復旧検査のセキュリティ設定について、RACF SETROPTS RDEFINE RACDCERT の RDEFINE UNIXPRIV では、RACF プロファイル、権限、クラス定義を対応付けて確認します。RDEFIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020078の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、復旧検査のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSUPERUSER.FILESYS.を指定し、OSKB020078の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SUPERUSER.FILESYS.
CASE OSKB020078
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SUPERUSER.FILESYS.
CASE OSKB020078
SOURCE RACF
SUPERUSER.FILESYS.とOSKB020078が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020078を同じ出力で読み、復旧検査のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020078
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020078 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SUPERUSER.FILESYS.MOUNT INFORMATION LISTED
IRRD105IとOSKB020078が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SUPERUSER.FILESYS. と OSKB020078 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020078 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0288"><h3>SUPERUSER.PROCESS.KILL</h3><p class="kb-meta">分類: RDEFINE UNIXPRIV ・ 難易度: 上級</p><p>RACF SETROPTS RDEFINE RACDCERTのRDEFINE UNIXPRIVでは、RACFプロファイル、権限、クラス定義を対応付けて確認します。RDEFINE UNIXPRIVは、RACF SETROPTS RDEFINE RACDCERTの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、SUPERUSER.PROCESS.KILLの表記と許可される値を確認します。</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SUPERUSER.PROCESS.KILL</strong></p><p>検証目的: 変更検査のセキュリティ設定について、RACF SETROPTS RDEFINE RACDCERT の RDEFINE UNIXPRIV では、RACF プロファイル、権限、クラス定義を対応付けて確認します。RDEFIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020080の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、変更検査のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSUPERUSER.PROCESS.を指定し、OSKB020080の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SUPERUSER.PROCESS.
CASE OSKB020080
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SUPERUSER.PROCESS.
CASE OSKB020080
SOURCE RACF
SUPERUSER.PROCESS.とOSKB020080が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020080を同じ出力で読み、変更検査のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020080
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020080 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SUPERUSER.PROCESS.KILL INFORMATION LISTED
IRRD105IとOSKB020080が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SUPERUSER.PROCESS. と OSKB020080 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020080 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0289"><h3>UNIXPRIV クラス</h3><p class="kb-meta">分類: RDEFINE UNIXPRIV ・ 難易度: 上級</p><p>UNIXPRIV クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE UNIXPRIVで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UNIXPRIV クラス</strong></p><p>検証目的: 値域検査のクラスについて、UNIXPRIV クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE UNIXPRIV で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020076の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、値域検査のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にUNIXPRIV クラスを指定し、OSKB020076の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND UNIXPRIV クラス
CASE OSKB020076
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM UNIXPRIV クラス
CASE OSKB020076
SOURCE RACF
UNIXPRIV クラスとOSKB020076が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020076を同じ出力で読み、値域検査のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020076
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020076 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I UNIXPRIV クラス INFORMATION LISTED
IRRD105IとOSKB020076が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の UNIXPRIV クラス と OSKB020076 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020076 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE その他


<section class="kb-item" id="c26-i0290"><h3>DLFCLASS クラス</h3><p class="kb-meta">分類: RDEFINE その他 ・ 難易度: 上級</p><p>DLFCLASS クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索確認のクラスで DLFCLASS クラスの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. DLFCLASS クラスの出力を取らず探索確認のクラスの説明文と承認印のみを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、探索確認の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して探索確認のクラスの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索確認のクラスへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索確認のクラスにおいて選択記号 B を採用し、識別名は探索確認です。探索確認のクラスにおいて DLFCLASS クラス は説明欄の「探索確認のクラスに関係する定義値と表示行を照合する探索確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は探索確認です。探索確認のクラスの証跡を読む担当者は、DLFCLASS クラスの属性行と IRRD105I を合わせて追跡し、背景名は探索確認です。誤答側の問題点を分けます。 A: 探索確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため探索確認ではありません。 B: 探索確認のクラスは対象出力と項目説明を結び、根拠を残すので探索確認です。 C: 探索確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため探索確認ではありません。 D: 探索確認のクラスは別カテゴリの確認を流用しており、DLFCLASS クラスの根拠にならないため探索確認ではありません。探索確認のクラスに出る DLFCLASS クラスは RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は探索確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DLFCLASS クラス</strong></p><p>検証目的: 監査判定のクラスについて、DLFCLASS クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020099の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、監査判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にDLFCLASS クラスを指定し、OSKB020099の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND DLFCLASS クラス
CASE OSKB020099
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM DLFCLASS クラス
CASE OSKB020099
SOURCE RACF
DLFCLASS クラスとOSKB020099が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020099を同じ出力で読み、監査判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020099
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020099 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I DLFCLASS クラス INFORMATION LISTED
IRRD105IとOSKB020099が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の DLFCLASS クラス と OSKB020099 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020099 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0291"><h3>DSNR クラス</h3><p class="kb-meta">分類: RDEFINE その他 ・ 難易度: 上級</p><p>DSNR クラスは、Db2 サブシステム アクセス制御。「DSNR クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端確認のクラスに関係する DSNR クラスの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端確認で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. DSNR クラスの名称と担当者名のみを残して終端確認のクラスの表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で終端確認のクラスを確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず終端確認のクラスの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端確認のクラスにおいて選択記号 A を採用し、識別名は終端確認です。終端確認のクラスにおいて DSNR クラス は説明欄の「DSNR クラスの用途をセキュリティ設定の表示で確認する終端確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は終端確認です。終端確認のクラスに関連して、RACF では DSNR クラスの表示属性と IRRD105I を同じ証跡に残し、背景名は終端確認です。他の選択肢を確認します。 A: 終端確認のクラスは対象出力と項目説明を結び、根拠を残すので終端確認です。 B: 終端確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため終端確認ではありません。 C: 終端確認のクラスは別カテゴリの確認を流用しており、DSNR クラスの根拠にならないため終端確認ではありません。 D: 終端確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため終端確認ではありません。終端確認のクラスで使う DSNR クラスという用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は終端確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DSNR クラス</strong></p><p>検証目的: 復旧判定のクラスについて、DSNR クラスは、Db2 サブシステム アクセス制御。「DSNR クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020098の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、復旧判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にDSNR クラスを指定し、OSKB020098の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND DSNR クラス
CASE OSKB020098
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM DSNR クラス
CASE OSKB020098
SOURCE RACF
DSNR クラスとOSKB020098が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020098を同じ出力で読み、復旧判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020098
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020098 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I DSNR クラス INFORMATION LISTED
IRRD105IとOSKB020098が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の DSNR クラス と OSKB020098 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020098 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0292"><h3>GLOBAL クラス</h3><p class="kb-meta">分類: RDEFINE その他 ・ 難易度: 上級</p><p>GLOBAL クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書確認のクラスでセキュリティ設定の運用確認を行います。GLOBAL クラスの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で上書確認のクラスを確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず上書確認のクラスを正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて上書確認の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. GLOBAL クラスの属性行を読まず上書確認のクラスの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書確認のクラスにおいて選択記号 C を採用し、識別名は上書確認です。上書確認のクラスにおいて GLOBAL クラス は説明欄の「RACF で GLOBAL クラスの扱いを記録する上書確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は上書確認です。上書確認のクラスを受け取る担当者は、GLOBAL クラスの表示結果と IRRD105I を同じ確認単位として扱い、背景名は上書確認です。不適切な選択肢を整理します。 A: 上書確認のクラスは別カテゴリの確認を流用しており、GLOBAL クラスの根拠にならないため上書確認ではありません。 B: 上書確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため上書確認ではありません。 C: 上書確認のクラスは対象出力と項目説明を結び、根拠を残すので上書確認です。 D: 上書確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため上書確認ではありません。上書確認のクラスが示す GLOBAL クラスは出典欄の資料で使い方を追跡できる項目であり、用語名は上書確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>GLOBAL クラス</strong></p><p>検証目的: 変更判定のクラスについて、GLOBAL クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020100の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、変更判定のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にGLOBAL クラスを指定し、OSKB020100の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND GLOBAL クラス
CASE OSKB020100
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM GLOBAL クラス
CASE OSKB020100
SOURCE RACF
GLOBAL クラスとOSKB020100が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020100を同じ出力で読み、変更判定のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020100
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020100 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I GLOBAL クラス INFORMATION LISTED
IRRD105IとOSKB020100が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の GLOBAL クラス と OSKB020100 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020100 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0293"><h3>IDIDMAP クラス</h3><p class="kb-meta">分類: RDEFINE その他 ・ 難易度: 上級</p><p>IDIDMAP クラスは、分散 ID マッピング。「IDIDMAP クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力確認のクラスに関する IDIDMAP クラスの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず出力確認のクラスの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力確認のクラスの証跡として保存して根拠にする。</li><li>C. IDIDMAP クラスの変更点を出力本文から切り離して出力確認のクラスの承認欄のみ残す。</li><li>D. IRRD105I を含む表示を保存し、説明欄との差分を出力確認で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力確認のクラスにおいて選択記号 D を採用し、識別名は出力確認です。出力確認のクラスにおいて IDIDMAP クラス は説明欄の「IDIDMAP クラスの状態と出力メッセージを結び付ける出力確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は出力確認です。出力確認のクラスに関する記録は、IDIDMAP クラスの出力行と IRRD105I を一緒に保存し、背景名は出力確認です。選択肢ごとの違いを示します。 A: 出力確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため出力確認ではありません。 B: 出力確認のクラスは別カテゴリの確認を流用しており、IDIDMAP クラスの根拠にならないため出力確認ではありません。 C: 出力確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため出力確認ではありません。 D: 出力確認のクラスは対象出力と項目説明を結び、根拠を残すので出力確認です。出力確認のクラスで記録する IDIDMAP クラスは RACF の確認記録に残す対象名であり、用語名は出力確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IDIDMAP クラス</strong></p><p>検証目的: 構文整理のクラスについて、IDIDMAP クラスは、分散 ID マッピング。「IDIDMAP クラス」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020101の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、構文整理のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIDIDMAP クラスを指定し、OSKB020101の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IDIDMAP クラス
CASE OSKB020101
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IDIDMAP クラス
CASE OSKB020101
SOURCE RACF
IDIDMAP クラスとOSKB020101が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020101を同じ出力で読み、構文整理のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020101
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020101 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IDIDMAP クラス INFORMATION LISTED
IRRD105IとOSKB020101が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IDIDMAP クラス と OSKB020101 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020101 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0294"><h3>SOMDOBJS クラス</h3><p class="kb-meta">分類: RDEFINE その他 ・ 難易度: 上級</p><p>SOMDOBJS クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件確認のクラスに関係する SOMDOBJS クラスの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、条件確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. SOMDOBJS クラスの名称と担当者名のみを残して条件確認のクラスの表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で条件確認のクラスを確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず条件確認のクラスの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件確認のクラスにおいて選択記号 A を採用し、識別名は条件確認です。条件確認のクラスにおいて SOMDOBJS クラス は説明欄の「SOMDOBJS クラスの用途をセキュリティ設定の表示で確認する条件確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認のクラスに関連して、RACF では SOMDOBJS クラスの表示属性と IRRD105I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認のクラスは対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認のクラスは名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認のクラスは別カテゴリの確認を流用しており、SOMDOBJS クラスの根拠にならないため条件確認ではありません。 D: 条件確認のクラスは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため条件確認ではありません。条件確認のクラスで使う SOMDOBJS クラスという用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は条件確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SOMDOBJS クラス</strong></p><p>検証目的: 展開整理のクラスについて、SOMDOBJS クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE その他で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020102の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、展開整理のクラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSOMDOBJS クラスを指定し、OSKB020102の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SOMDOBJS クラス
CASE OSKB020102
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SOMDOBJS クラス
CASE OSKB020102
SOURCE RACF
SOMDOBJS クラスとOSKB020102が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020102を同じ出力で読み、展開整理のクラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020102
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020102 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SOMDOBJS クラス INFORMATION LISTED
IRRD105IとOSKB020102が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SOMDOBJS クラス と OSKB020102 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020102 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDEFINE オペランド


<section class="kb-item" id="c26-i0295"><h3>ADDCATEGORY(category)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>ADDCATEGORY(category)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ADDCATEGORY(category)</strong></p><p>検証目的: 比較照合のオペランドについて、ADDCATEGORY(category)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020034の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、比較照合のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にADDCATEGORY(categoを指定し、OSKB020034の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND ADDCATEGORY(catego
CASE OSKB020034
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM ADDCATEGORY(catego
CASE OSKB020034
SOURCE RACF
ADDCATEGORY(categoとOSKB020034が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020034を同じ出力で読み、比較照合のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020034
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020034 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I ADDCATEGORY(category) INFORMATION LISTED
IRRD105IとOSKB020034が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の ADDCATEGORY(catego と OSKB020034 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020034 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0296"><h3>ADDMEM(member1,member2,…)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>ADDMEM(member1,member2,…)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


<section class="kb-item" id="c26-i0297"><h3>APPLDATA(&#x27;text&#x27;)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>APPLDATA(&#x27;text&#x27;)は、アプリケーション用データ 255 文字。「APPLDATA(&#x27;text&#x27;)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>APPLDATA(&#x27;text&#x27;)</strong></p><p>検証目的: 呼出照合のオペランドについて、APPLDATA(&#x27;text&#x27;)は、アプリケーション用データ 255 文字。「APPLDATA(&#x27;text&#x27;)」を確認すると、SETROPTS、RDEFINE、RACDCEに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020023の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、呼出照合のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にAPPLDATA(&#x27;text&#x27;)を指定し、OSKB020023の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND APPLDATA(&#x27;text&#x27;)
CASE OSKB020023
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM APPLDATA(&#x27;text&#x27;)
CASE OSKB020023
SOURCE RACF
APPLDATA(&#x27;text&#x27;)とOSKB020023が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020023を同じ出力で読み、呼出照合のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020023
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020023 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I APPLDATA(&#x27;text&#x27;) INFORMATION LISTED
IRRD105IとOSKB020023が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の APPLDATA(&#x27;text&#x27;) と OSKB020023 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020023 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0298"><h3>AUDIT(ALL(READ))</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>AUDIT(ALL(READ))は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AUDIT(ALL(READ))</strong></p><p>検証目的: 順序確認のオペランドについて、AUDIT(ALL(READ))は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020015の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、順序確認のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にAUDIT(ALL(READ))を指定し、OSKB020015の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND AUDIT(ALL(READ))
CASE OSKB020015
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM AUDIT(ALL(READ))
CASE OSKB020015
SOURCE RACF
AUDIT(ALL(READ))とOSKB020015が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020015を同じ出力で読み、順序確認のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020015
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020015 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I AUDIT(ALL(READ)) INFORMATION LISTED
IRRD105IとOSKB020015が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の AUDIT(ALL(READ)) と OSKB020015 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020015 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0299"><h3>AUDIT(ALL|SUCCESS|FAILURES|NONE)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>AUDIT(ALL|SUCCESS|FAILURES|NONE)は、アクセス監査レベル指定。「AUDIT(ALL|SUCCESS|FAILURES|NONE)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AUDIT(ALL|SUCCESS|FAILURES|NONE)</strong></p><p>検証目的: 比較確認の| |について、AUDIT(ALL|SUCCESS|FAILURES|NONE)は、アクセス監査レベル指定。「AUDIT(ALL|SUCCESS|FAILURES|NONE)」を確認するとに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020014の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、比較確認の| |の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にAUDIT(ALL|SUCCESS|を指定し、OSKB020014の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND AUDIT(ALL|SUCCESS|
CASE OSKB020014
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM AUDIT(ALL|SUCCESS|
CASE OSKB020014
SOURCE RACF
AUDIT(ALL|SUCCESS|とOSKB020014が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020014を同じ出力で読み、比較確認の| |の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020014
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020014 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I AUDIT(ALL|SUCCESS|FAILUR INFORMATION LISTED
IRRD105IとOSKB020014が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の AUDIT(ALL|SUCCESS| と OSKB020014 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020014 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0300"><h3>AUDIT(FAILURES(UPDATE))</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>AUDIT(FAILURES(UPDATE))は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AUDIT(FAILURES(UPDATE))</strong></p><p>検証目的: 値域確認のオペランドについて、AUDIT(FAILURES(UPDATE))は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020016の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、値域確認のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にAUDIT(FAILURES(UPDを指定し、OSKB020016の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND AUDIT(FAILURES(UPD
CASE OSKB020016
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM AUDIT(FAILURES(UPD
CASE OSKB020016
SOURCE RACF
AUDIT(FAILURES(UPDとOSKB020016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020016を同じ出力で読み、値域確認のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020016
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020016 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I AUDIT(FAILURES(UPDATE)) INFORMATION LISTED
IRRD105IとOSKB020016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の AUDIT(FAILURES(UPD と OSKB020016 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0301"><h3>CATEGORY(name1,name2,…)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>CATEGORY(name1,name2,…)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


<section class="kb-item" id="c26-i0302"><h3>DATA(&#x27;text&#x27;)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>DATA(&#x27;text&#x27;)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DATA(&#x27;text&#x27;)</strong></p><p>検証目的: 展開照合のオペランドについて、DATA(&#x27;text&#x27;)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020022の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、展開照合のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にDATA(&#x27;text&#x27;)を指定し、OSKB020022の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND DATA(&#x27;text&#x27;)
CASE OSKB020022
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM DATA(&#x27;text&#x27;)
CASE OSKB020022
SOURCE RACF
DATA(&#x27;text&#x27;)とOSKB020022が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020022を同じ出力で読み、展開照合のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020022
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020022 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I DATA(&#x27;text&#x27;) INFORMATION LISTED
IRRD105IとOSKB020022が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の DATA(&#x27;text&#x27;) と OSKB020022 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0303"><h3>FCLASS(クラス名)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>FCLASS(クラス名)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FCLASS(クラス名)</strong></p><p>検証目的: 上書照合のクラス名について、FCLASS(クラス名)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020027の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、上書照合のクラス名の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にFCLASS(クラス名)を指定し、OSKB020027の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND FCLASS(クラス名)
CASE OSKB020027
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM FCLASS(クラス名)
CASE OSKB020027
SOURCE RACF
FCLASS(クラス名)とOSKB020027が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020027を同じ出力で読み、上書照合のクラス名の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020027
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020027 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I FCLASS(クラス名) INFORMATION LISTED
IRRD105IとOSKB020027が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の FCLASS(クラス名) と OSKB020027 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020027 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0304"><h3>FGENERIC</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>FGENERICは、FROM の汎用プロファイル指定。「FGENERIC」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FGENERIC</strong></p><p>検証目的: 条件照合のオペランドについて、FGENERIC は、FROM の汎用プロファイル指定。「FGENERIC」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020029の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、条件照合のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にFGENERICを指定し、OSKB020029の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND FGENERIC
CASE OSKB020029
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM FGENERIC
CASE OSKB020029
SOURCE RACF
FGENERICとOSKB020029が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020029を同じ出力で読み、条件照合のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020029
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020029 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I FGENERIC INFORMATION LISTED
IRRD105IとOSKB020029が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の FGENERIC と OSKB020029 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020029 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0305"><h3>FROM(プロファイル名)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>FROM(プロファイル名)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FROM(プロファイル名)</strong></p><p>検証目的: 出力照合のプロファイル名について、FROM(プロファイル名)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020028の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、出力照合のプロファイル名の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にFROM(プロファイル名)を指定し、OSKB020028の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND FROM(プロファイル名)
CASE OSKB020028
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM FROM(プロファイル名)
CASE OSKB020028
SOURCE RACF
FROM(プロファイル名)とOSKB020028が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020028を同じ出力で読み、出力照合のプロファイル名の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020028
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020028 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I FROM(プロファイル名) INFORMATION LISTED
IRRD105IとOSKB020028が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の FROM(プロファイル名) と OSKB020028 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020028 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0306"><h3>LEVEL(n)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>LEVEL(n)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LEVEL(n)</strong></p><p>検証目的: 構文照合のオペランドについて、LEVEL(n)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020021の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、構文照合のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にLEVEL(n)を指定し、OSKB020021の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND LEVEL(n)
CASE OSKB020021
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM LEVEL(n)
CASE OSKB020021
SOURCE RACF
LEVEL(n)とOSKB020021が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020021を同じ出力で読み、構文照合のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020021
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020021 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I LEVEL(n) INFORMATION LISTED
IRRD105IとOSKB020021が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の LEVEL(n) と OSKB020021 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020021 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0307"><h3>MODEL(profile)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>MODEL(profile)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MODEL(profile)</strong></p><p>検証目的: 区切照合のオペランドについて、MODEL(profile)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020030の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、区切照合のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にMODEL(profile)を指定し、OSKB020030の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND MODEL(profile)
CASE OSKB020030
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM MODEL(profile)
CASE OSKB020030
SOURCE RACF
MODEL(profile)とOSKB020030が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020030を同じ出力で読み、区切照合のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020030
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020030 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I MODEL(profile) INFORMATION LISTED
IRRD105IとOSKB020030が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の MODEL(profile) と OSKB020030 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0308"><h3>NONOTIFY</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>NONOTIFYは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>NONOTIFY</strong></p><p>検証目的: 復旧確認のオペランドについて、NONOTIFY は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020018の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、復旧確認のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にNONOTIFYを指定し、OSKB020018の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND NONOTIFY
CASE OSKB020018
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM NONOTIFY
CASE OSKB020018
SOURCE RACF
NONOTIFYとOSKB020018が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020018を同じ出力で読み、復旧確認のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020018
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020018 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I NONOTIFY INFORMATION LISTED
IRRD105IとOSKB020018が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の NONOTIFY と OSKB020018 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020018 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0309"><h3>NOTIFY(userid)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>NOTIFY(userid)は、アクセス違反時に通知するユーザ ID。「NOTIFY(userid)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>NOTIFY(userid)</strong></p><p>検証目的: 警告確認のオペランドについて、NOTIFY(userid)は、アクセス違反時に通知するユーザ ID。「NOTIFY(userid)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020017の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、警告確認のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にNOTIFY(userid)を指定し、OSKB020017の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND NOTIFY(userid)
CASE OSKB020017
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM NOTIFY(userid)
CASE OSKB020017
SOURCE RACF
NOTIFY(userid)とOSKB020017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020017を同じ出力で読み、警告確認のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020017
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020017 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I NOTIFY(userid) INFORMATION LISTED
IRRD105IとOSKB020017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の NOTIFY(userid) と OSKB020017 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0310"><h3>NOWARNING</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>NOWARNINGは、WARNING モード解除。「NOWARNING」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>NOWARNING</strong></p><p>検証目的: 変更確認のオペランドについて、NOWARNING は、WARNING モード解除。「NOWARNING」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020020の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、変更確認のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にNOWARNINGを指定し、OSKB020020の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND NOWARNING
CASE OSKB020020
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM NOWARNING
CASE OSKB020020
SOURCE RACF
NOWARNINGとOSKB020020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020020を同じ出力で読み、変更確認のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020020
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020020 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I NOWARNING INFORMATION LISTED
IRRD105IとOSKB020020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の NOWARNING と OSKB020020 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0311"><h3>OWNER(userid|group)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>OWNER(userid|group)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>OWNER(userid|group)</strong></p><p>検証目的: 記録確認の|について、OWNER(userid|group)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020013の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、記録確認の|の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にOWNER(userid|groupを指定し、OSKB020013の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND OWNER(userid|group
CASE OSKB020013
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM OWNER(userid|group
CASE OSKB020013
SOURCE RACF
OWNER(userid|groupとOSKB020013が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020013を同じ出力で読み、記録確認の|の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020013
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020013 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I OWNER(userid|group) INFORMATION LISTED
IRRD105IとOSKB020013が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の OWNER(userid|group と OSKB020013 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020013 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0312"><h3>SECLABEL(label)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>SECLABEL(label)は、セキュリティ ラベル (MLS 環境用)。「SECLABEL(label)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SECLABEL(label)</strong></p><p>検証目的: 探索照合のオペランドについて、SECLABEL(label)は、セキュリティ ラベル (MLS 環境用)。「SECLABEL(label)」を確認すると、SETROPTS、RDEFINE、RACDCERに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020026の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、探索照合のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSECLABEL(label)を指定し、OSKB020026の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SECLABEL(label)
CASE OSKB020026
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SECLABEL(label)
CASE OSKB020026
SOURCE RACF
SECLABEL(label)とOSKB020026が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020026を同じ出力で読み、探索照合のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020026
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020026 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SECLABEL(label) INFORMATION LISTED
IRRD105IとOSKB020026が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SECLABEL(label) と OSKB020026 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020026 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0313"><h3>SECLEVEL(name)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>SECLEVEL(name)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SECLEVEL(name)</strong></p><p>検証目的: 置換照合のオペランドについて、SECLEVEL(name)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020024の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、置換照合のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSECLEVEL(name)を指定し、OSKB020024の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SECLEVEL(name)
CASE OSKB020024
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SECLEVEL(name)
CASE OSKB020024
SOURCE RACF
SECLEVEL(name)とOSKB020024が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020024を同じ出力で読み、置換照合のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020024
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020024 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SECLEVEL(name) INFORMATION LISTED
IRRD105IとOSKB020024が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SECLEVEL(name) と OSKB020024 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0314"><h3>SINGLEDSN</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>SINGLEDSNは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SINGLEDSN</strong></p><p>検証目的: 値域照合のオペランドについて、SINGLEDSN は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020036の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、値域照合のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSINGLEDSNを指定し、OSKB020036の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SINGLEDSN
CASE OSKB020036
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SINGLEDSN
CASE OSKB020036
SOURCE RACF
SINGLEDSNとOSKB020036が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020036を同じ出力で読み、値域照合のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020036
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020036 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SINGLEDSN INFORMATION LISTED
IRRD105IとOSKB020036が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SINGLEDSN と OSKB020036 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020036 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0315"><h3>TIMEZONE(±hh:mm)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>TIMEZONE(±hh:mm)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TIMEZONE(±hh:mm)</strong></p><p>検証目的: 範囲照合の± :について、TIMEZONE(±hh:mm)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020031の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、範囲照合の± :の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にTIMEZONE(±hh:mm)を指定し、OSKB020031の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND TIMEZONE(±hh:mm)
CASE OSKB020031
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM TIMEZONE(±hh:mm)
CASE OSKB020031
SOURCE RACF
TIMEZONE(±hh:mm)とOSKB020031が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020031を同じ出力で読み、範囲照合の± :の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020031
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020031 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I TIMEZONE(±hh:mm) INFORMATION LISTED
IRRD105IとOSKB020031が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の TIMEZONE(±hh:mm) と OSKB020031 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020031 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0316"><h3>UACC(READ|UPDATE|CONTROL|ALTER|NONE)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>UACC(READ|UPDATE|CONTROL|ALTER|NONE)は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


<section class="kb-item" id="c26-i0317"><h3>VOLUME(volser)</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>VOLUME(volser)は、TAPEVOL/DASDVOL のボリューム名。「VOLUME(volser)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>VOLUME(volser)</strong></p><p>検証目的: 順序照合のオペランドについて、VOLUME(volser)は、TAPEVOL/DASDVOL のボリューム名。「VOLUME(volser)」を確認すると、SETROPTS、RDEFINE、RACDCEに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020035の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、順序照合のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にVOLUME(volser)を指定し、OSKB020035の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND VOLUME(volser)
CASE OSKB020035
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM VOLUME(volser)
CASE OSKB020035
SOURCE RACF
VOLUME(volser)とOSKB020035が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020035を同じ出力で読み、順序照合のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020035
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020035 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I VOLUME(volser) INFORMATION LISTED
IRRD105IとOSKB020035が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の VOLUME(volser) と OSKB020035 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020035 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0318"><h3>WARNING</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>WARNINGは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WARNING</strong></p><p>検証目的: 監査確認のオペランドについて、WARNING は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020019の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、監査確認のオペランドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にWARNINGを指定し、OSKB020019の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND WARNING
CASE OSKB020019
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM WARNING
CASE OSKB020019
SOURCE RACF
WARNINGとOSKB020019が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020019を同じ出力で読み、監査確認のオペランドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020019
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020019 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I WARNING INFORMATION LISTED
IRRD105IとOSKB020019が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の WARNING と OSKB020019 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020019 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0319"><h3>WHEN(DAYS(…)|TIME(…))</h3><p class="kb-meta">分類: RDEFINE オペランド ・ 難易度: 上級</p><p>WHEN(DAYS(…)|TIME(…))は、アクセス可能な曜日/時間帯。「WHEN(DAYS(…)|TIME(…))」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


## RDEFINE 基本


<section class="kb-item" id="c26-i0320"><h3>GENERIC キーワード</h3><p class="kb-meta">分類: RDEFINE 基本 ・ 難易度: 上級</p><p>GENERIC キーワードは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>GENERIC キーワード</strong></p><p>検証目的: 区切確認のキーワードについて、GENERIC キーワードは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020010の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、区切確認のキーワードの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にGENERIC キーワードを指定し、OSKB020010の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND GENERIC キーワード
CASE OSKB020010
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM GENERIC キーワード
CASE OSKB020010
SOURCE RACF
GENERIC キーワードとOSKB020010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020010を同じ出力で読み、区切確認のキーワードの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020010
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020010 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I GENERIC キーワード INFORMATION LISTED
IRRD105IとOSKB020010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の GENERIC キーワード と OSKB020010 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0321"><h3>RDEFINE の目的</h3><p class="kb-meta">分類: RDEFINE 基本 ・ 難易度: 上級</p><p>RDEFINE の目的は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RDEFINE の目的</strong></p><p>検証目的: 置換確認のの目的について、RDEFINE の目的は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020004の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、置換確認のの目的の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRDEFINE の目的を指定し、OSKB020004の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RDEFINE の目的
CASE OSKB020004
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RDEFINE の目的
CASE OSKB020004
SOURCE RACF
RDEFINE の目的とOSKB020004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020004を同じ出力で読み、置換確認のの目的の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020004
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020004 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RDEFINE の目的 INFORMATION LISTED
IRRD105IとOSKB020004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RDEFINE の目的 と OSKB020004 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0322"><h3>RDEFINE 構文</h3><p class="kb-meta">分類: RDEFINE 基本 ・ 難易度: 上級</p><p>RDEFINE 構文は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RDEFINE 構文</strong></p><p>検証目的: 探索確認の構文について、RDEFINE 構文は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020006の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、探索確認の構文の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRDEFINE 構文を指定し、OSKB020006の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RDEFINE 構文
CASE OSKB020006
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RDEFINE 構文
CASE OSKB020006
SOURCE RACF
RDEFINE 構文とOSKB020006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020006を同じ出力で読み、探索確認の構文の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020006
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020006 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RDEFINE 構文 INFORMATION LISTED
IRRD105IとOSKB020006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RDEFINE 構文 と OSKB020006 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0323"><h3>RDEFINE 短縮形 RDEF</h3><p class="kb-meta">分類: RDEFINE 基本 ・ 難易度: 上級</p><p>RDEFINE は RDEF と省略可。「RDEFINE 短縮形 RDEF」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RDEFINE 短縮形 RDEF</strong></p><p>検証目的: 終端確認の短縮形について、RDEFINE は RDEF と省略可。「RDEFINE 短縮形 RDEF」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020005の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、終端確認の短縮形の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRDEFINE 短縮形 RDEFを指定し、OSKB020005の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RDEFINE 短縮形 RDEF
CASE OSKB020005
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RDEFINE 短縮形 RDEF
CASE OSKB020005
SOURCE RACF
RDEFINE 短縮形 RDEFとOSKB020005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020005を同じ出力で読み、終端確認の短縮形の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020005
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020005 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RDEFINE 短縮形 RDEF INFORMATION LISTED
IRRD105IとOSKB020005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RDEFINE 短縮形 RDEF と OSKB020005 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0324"><h3>クラス名指定</h3><p class="kb-meta">分類: RDEFINE 基本 ・ 難易度: 上級</p><p>クラス名指定は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>クラス名指定</strong></p><p>検証目的: 上書確認のクラス名指定について、クラス名指定は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020007の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、上書確認のクラス名指定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にクラス名指定を指定し、OSKB020007の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND クラス名指定
CASE OSKB020007
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM クラス名指定
CASE OSKB020007
SOURCE RACF
クラス名指定とOSKB020007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020007を同じ出力で読み、上書確認のクラス名指定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020007
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020007 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I クラス名指定 INFORMATION LISTED
IRRD105IとOSKB020007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の クラス名指定 と OSKB020007 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0325"><h3>プロファイル名長</h3><p class="kb-meta">分類: RDEFINE 基本 ・ 難易度: 上級</p><p>プロファイル名長は、クラスごとに最大長が CDT で定義 (通常 246 文字)。「プロファイル名長」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>プロファイル名長</strong></p><p>検証目的: 出力確認のプロファイル名長について、プロファイル名長は、クラスごとに最大長が CDT で定義 (通常 246 文字)。「プロファイル名長」を確認すると、SETROPTS、RDEFINE、RACDCERT の変に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020008の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、出力確認のプロファイル名長の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にプロファイル名長を指定し、OSKB020008の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND プロファイル名長
CASE OSKB020008
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM プロファイル名長
CASE OSKB020008
SOURCE RACF
プロファイル名長とOSKB020008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020008を同じ出力で読み、出力確認のプロファイル名長の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020008
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020008 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I プロファイル名長 INFORMATION LISTED
IRRD105IとOSKB020008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の プロファイル名長 と OSKB020008 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0326"><h3>メンバ クラス vs グルーピング クラス</h3><p class="kb-meta">分類: RDEFINE 基本 ・ 難易度: 上級</p><p>メンバ クラス vs グルーピング クラスは、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。メンバ クラス vs グルーピング クラスは、メンバ クラス (FACILITY 等) と GROUP クラス (GFACILIT 等) の対</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>メンバ クラス vs グルーピング クラス</strong></p><p>検証目的: 範囲確認のメンバ クラス グルーピング クラスについて、メンバ クラス vs グルーピング クラスは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020011の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、範囲確認のメンバ クラス グルーピング クラスの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にメンバ クラス vs グルーピング を指定し、OSKB020011の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND メンバ クラス vs グルーピング 
CASE OSKB020011
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM メンバ クラス vs グルーピング 
CASE OSKB020011
SOURCE RACF
メンバ クラス vs グルーピング とOSKB020011が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020011を同じ出力で読み、範囲確認のメンバ クラス グルーピング クラスの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020011
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020011 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I メンバ クラス vs グルーピング クラス INFORMATION LISTED
IRRD105IとOSKB020011が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の メンバ クラス vs グルーピング  と OSKB020011 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020011 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0327"><h3>汎用プロファイル指定</h3><p class="kb-meta">分類: RDEFINE 基本 ・ 難易度: 上級</p><p>汎用プロファイル指定は、RACF SETROPTS/RDEFINE/RACDCERTのRDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>汎用プロファイル指定</strong></p><p>検証目的: 条件確認の汎用プロファイル指定について、汎用プロファイル指定は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020009の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、条件確認の汎用プロファイル指定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄に汎用プロファイル指定を指定し、OSKB020009の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND 汎用プロファイル指定
CASE OSKB020009
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM 汎用プロファイル指定
CASE OSKB020009
SOURCE RACF
汎用プロファイル指定とOSKB020009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020009を同じ出力で読み、条件確認の汎用プロファイル指定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020009
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020009 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I 汎用プロファイル指定 INFORMATION LISTED
IRRD105IとOSKB020009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の 汎用プロファイル指定 と OSKB020009 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RDELETE


<section class="kb-item" id="c26-i0328"><h3>RDELETE GENERIC</h3><p class="kb-meta">分類: RDELETE ・ 難易度: 上級</p><p>RDELETE GENERICは、汎用プロファイルを明示削除。「RDELETE GENERIC」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出照合のセキュリティ設定でセキュリティ設定の運用確認を行います。RDELETE GENERIC の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で呼出照合のセキュリティ設定を確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず呼出照合のセキュリティ設定を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて呼出照合の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. RDELETE GENERIC の属性行を読まず呼出照合のセキュリティ設定の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出照合のセキュリティ設定において選択記号 C を採用し、識別名は呼出照合です。呼出照合のセキュリティ設定において RDELETE GENERIC は説明欄の「RACF で RDELETE GENERIC の扱いを記録する呼出照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合のセキュリティ設定を受け取る担当者は、RDELETE GENERIC の表示結果と IRRD105I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合のセキュリティ設定は別カテゴリの確認を流用しており、RDELETE GENERIC の根拠にならないため呼出照合ではありません。 B: 呼出照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合のセキュリティ設定が示す RDELETE GENERIC は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RDELETE GENERIC</strong></p><p>検証目的: 値域整理のセキュリティ設定について、RDELETE GENERIC は、汎用プロファイルを明示削除。「RDELETE GENERIC」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020116の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、値域整理のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE GENERICを指定し、OSKB020116の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RDELETE GENERIC
CASE OSKB020116
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RDELETE GENERIC
CASE OSKB020116
SOURCE RACF
RDELETE GENERICとOSKB020116が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020116を同じ出力で読み、値域整理のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020116
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020116 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RDELETE GENERIC INFORMATION LISTED
IRRD105IとOSKB020116が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RDELETE GENERIC と OSKB020116 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020116 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0329"><h3>RDELETE の権限</h3><p class="kb-meta">分類: RDELETE ・ 難易度: 上級</p><p>RDELETE の権限は、RACF SETROPTS/RDEFINE/RACDCERTのRDELETEで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換照合のの権限に関する RDELETE の権限の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず置換照合のの権限の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換照合のの権限の証跡として保存して根拠にする。</li><li>C. RDELETE の権限の変更点を出力本文から切り離して置換照合のの権限の承認欄のみ残す。</li><li>D. 同じ画面で対象行と IRRD105I を読み、置換照合の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換照合のの権限において選択記号 D を採用し、識別名は置換照合です。置換照合のの権限において RDELETE の権限 は説明欄の「RDELETE の権限の状態と出力メッセージを結び付ける置換照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合のの権限に関する記録は、RDELETE の権限の出力行と IRRD105I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合のの権限は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため置換照合ではありません。 B: 置換照合のの権限は別カテゴリの確認を流用しており、RDELETE の権限の根拠にならないため置換照合ではありません。 C: 置換照合のの権限は名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合のの権限は対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合のの権限で記録する RDELETE の権限は RACF の確認記録に残す対象名であり、用語名は置換照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RDELETE の権限</strong></p><p>検証目的: 警告整理のの権限について、RDELETE の権限は、RACF SETROPTS/RDEFINE/RACDCERT の RDELETE で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020117の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、警告整理のの権限の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE の権限を指定し、OSKB020117の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RDELETE の権限
CASE OSKB020117
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RDELETE の権限
CASE OSKB020117
SOURCE RACF
RDELETE の権限とOSKB020117が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020117を同じ出力で読み、警告整理のの権限の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020117
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020117 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RDELETE の権限 INFORMATION LISTED
IRRD105IとOSKB020117が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RDELETE の権限 と OSKB020117 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020117 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0330"><h3>RDELETE の目的</h3><p class="kb-meta">分類: RDELETE ・ 難易度: 上級</p><p>RDELETE の目的は、一般リソース プロファイルを削除。「RDELETE の目的」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更確認のの目的に関する RDELETE の目的の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず変更確認のの目的の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更確認のの目的の証跡として保存して根拠にする。</li><li>C. RDELETE の目的の変更点を出力本文から切り離して変更確認のの目的の承認欄のみ残す。</li><li>D. IRRD105I を含む表示を保存し、説明欄との差分を変更確認で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更確認のの目的において選択記号 D を採用し、識別名は変更確認です。変更確認のの目的において RDELETE の目的 は説明欄の「RDELETE の目的の状態と出力メッセージを結び付ける変更確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認のの目的に関する記録は、RDELETE の目的の出力行と IRRD105I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認のの目的は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため変更確認ではありません。 B: 変更確認のの目的は別カテゴリの確認を流用しており、RDELETE の目的の根拠にならないため変更確認ではありません。 C: 変更確認のの目的は名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認のの目的は対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認のの目的で記録する RDELETE の目的は RACF の確認記録に残す対象名であり、用語名は変更確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RDELETE の目的</strong></p><p>検証目的: 記録整理のの目的について、RDELETE の目的は、一般リソース プロファイルを削除。「RDELETE の目的」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020113の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、記録整理のの目的の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE の目的を指定し、OSKB020113の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RDELETE の目的
CASE OSKB020113
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RDELETE の目的
CASE OSKB020113
SOURCE RACF
RDELETE の目的とOSKB020113が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020113を同じ出力で読み、記録整理のの目的の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020113
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020113 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RDELETE の目的 INFORMATION LISTED
IRRD105IとOSKB020113が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RDELETE の目的 と OSKB020113 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020113 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0331"><h3>RDELETE 後の REFRESH</h3><p class="kb-meta">分類: RDELETE ・ 難易度: 上級</p><p>RDELETE 後の REFRESHは、RACF SETROPTS/RDEFINE/RACDCERTのRDELETEで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端照合の後のに関係する RDELETE 後の REFRESH の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、終端照合の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. RDELETE 後の REFRESH の名称と担当者名のみを残して終端照合の後のの表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で終端照合の後のを確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず終端照合の後のの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端照合の後のにおいて選択記号 A を採用し、識別名は終端照合です。終端照合の後のにおいて RDELETE 後の REFRESH は説明欄の「RDELETE 後の REFRESH の用途をセキュリティ設定の表示で確認する終端照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合の後のに関連して、RACF では RDELETE 後の REFRESH の表示属性と IRRD105I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合の後のは対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合の後のは名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合の後のは別カテゴリの確認を流用しており、RDELETE 後の REFRESH の根拠にならないため終端照合ではありません。 D: 終端照合の後のは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため終端照合ではありません。終端照合の後ので使う RDELETE 後の REFRESH という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は終端照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RDELETE 後の REFRESH</strong></p><p>検証目的: 復旧整理の後のについて、RDELETE 後の REFRESH は、RACF SETROPTS/RDEFINE/RACDCERT の RDELETE で認証、権限、またはセキュリティ設定を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020118の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、復旧整理の後のの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE 後の REFRESHを指定し、OSKB020118の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RDELETE 後の REFRESH
CASE OSKB020118
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RDELETE 後の REFRESH
CASE OSKB020118
SOURCE RACF
RDELETE 後の REFRESHとOSKB020118が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020118を同じ出力で読み、復旧整理の後のの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020118
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020118 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RDELETE 後の REFRESH INFORMATION LISTED
IRRD105IとOSKB020118が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RDELETE 後の REFRESH と OSKB020118 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020118 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0332"><h3>RDELETE 構文</h3><p class="kb-meta">分類: RDELETE ・ 難易度: 上級</p><p>RDELETE 構文は、RACF SETROPTS/RDEFINE/RACDCERTのRDELETEで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開照合の構文で RDELETE 構文の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. RDELETE 構文の出力を取らず展開照合の構文の説明文と承認印のみを残す。</li><li>B. 出典欄の説明と運用出力を照合し、展開照合の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して展開照合の構文の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開照合の構文へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開照合の構文において選択記号 B を採用し、識別名は展開照合です。展開照合の構文において RDELETE 構文 は説明欄の「展開照合の構文に関係する定義値と表示行を照合する展開照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合の構文の証跡を読む担当者は、RDELETE 構文の属性行と IRRD105I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合の構文は名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合の構文は対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合の構文は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため展開照合ではありません。 D: 展開照合の構文は別カテゴリの確認を流用しており、RDELETE 構文の根拠にならないため展開照合ではありません。展開照合の構文に出る RDELETE 構文は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は展開照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RDELETE 構文</strong></p><p>検証目的: 順序整理の構文について、RDELETE 構文は、RACF SETROPTS/RDEFINE/RACDCERT の RDELETE で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020115の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、順序整理の構文の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE 構文を指定し、OSKB020115の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RDELETE 構文
CASE OSKB020115
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RDELETE 構文
CASE OSKB020115
SOURCE RACF
RDELETE 構文とOSKB020115が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020115を同じ出力で読み、順序整理の構文の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020115
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020115 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RDELETE 構文 INFORMATION LISTED
IRRD105IとOSKB020115が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RDELETE 構文 と OSKB020115 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020115 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0333"><h3>RDELETE 短縮形 RDEL</h3><p class="kb-meta">分類: RDELETE ・ 難易度: 上級</p><p>RDELETE 短縮形 RDELは、RACF SETROPTS/RDEFINE/RACDCERTのRDELETEで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文照合の短縮形に関係する RDELETE 短縮形 RDEL の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、構文照合の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. RDELETE 短縮形 RDEL の名称と担当者名のみを残して構文照合の短縮形の表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で構文照合の短縮形を確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず構文照合の短縮形の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文照合の短縮形において選択記号 A を採用し、識別名は構文照合です。構文照合の短縮形において RDELETE 短縮形 RDEL は説明欄の「RDELETE 短縮形 RDEL の用途をセキュリティ設定の表示で確認する構文照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合の短縮形に関連して、RACF では RDELETE 短縮形 RDEL の表示属性と IRRD105I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合の短縮形は対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合の短縮形は名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合の短縮形は別カテゴリの確認を流用しており、RDELETE 短縮形 RDEL の根拠にならないため構文照合ではありません。 D: 構文照合の短縮形は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため構文照合ではありません。構文照合の短縮形で使う RDELETE 短縮形 RDEL という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は構文照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RDELETE 短縮形 RDEL</strong></p><p>検証目的: 比較整理の短縮形について、RDELETE 短縮形 RDEL は、RACF SETROPTS/RDEFINE/RACDCERT の RDELETE で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020114の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、比較整理の短縮形の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRDELETE 短縮形 RDELを指定し、OSKB020114の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RDELETE 短縮形 RDEL
CASE OSKB020114
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RDELETE 短縮形 RDEL
CASE OSKB020114
SOURCE RACF
RDELETE 短縮形 RDELとOSKB020114が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020114を同じ出力で読み、比較整理の短縮形の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020114
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020114 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RDELETE 短縮形 RDEL INFORMATION LISTED
IRRD105IとOSKB020114が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RDELETE 短縮形 RDEL と OSKB020114 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020114 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## REFRESH


<section class="kb-item" id="c26-i0334"><h3>GENERIC(クラス名) REFRESH</h3><p class="kb-meta">分類: REFRESH ・ 難易度: 上級</p><p>GENERIC(クラス名) REFRESHは、RACF SETROPTS/RDEFINE/RACDCERTのREFRESHで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件確認のクラス名に関係する GENERIC 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. GENERIC 属性の名称と担当者名のみを残して条件確認のクラス名の表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で条件確認のクラス名を確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず条件確認のクラス名の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件確認のクラス名において選択記号 A を採用し、識別名は条件確認です。条件確認のクラス名において GENERIC 属性 は説明欄の「GENERIC 属性の用途をセキュリティ設定の表示で確認する条件確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は条件確認です。条件確認のクラス名に関連して、RACF では GENERIC 属性の表示属性と IRRD105I を同じ証跡に残し、背景名は条件確認です。他の選択肢を確認します。 A: 条件確認のクラス名は対象出力と項目説明を結び、根拠を残すので条件確認です。 B: 条件確認のクラス名は名称や説明のみに寄り、状態を示す出力本文が不足するため条件確認ではありません。 C: 条件確認のクラス名は別カテゴリの確認を流用しており、GENERIC 属性の根拠にならないため条件確認ではありません。 D: 条件確認のクラス名は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため条件確認ではありません。条件確認のクラス名で使う GENERIC 属性という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は条件確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>GENERIC(クラス名) REFRESH</strong></p><p>検証目的: 展開照合のクラス名について、GENERIC(クラス名) REFRESH は、RACF SETROPTS/RDEFINE/RACDCERT の REFRESH で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010022の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、展開照合のクラス名の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にGENERIC(クラス名) REFRを指定し、OSKB010022の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND GENERIC(クラス名) REFR
CASE OSKB010022
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM GENERIC(クラス名) REFR
CASE OSKB010022
SOURCE RACF
GENERIC(クラス名) REFRとOSKB010022が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010022を同じ出力で読み、展開照合のクラス名の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010022
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010022 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I GENERIC(クラス名) REFRESH INFORMATION LISTED
IRRD105IとOSKB010022が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の GENERIC(クラス名) REFR と OSKB010022 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0335"><h3>GLOBAL(クラス名) REFRESH</h3><p class="kb-meta">分類: REFRESH ・ 難易度: 上級</p><p>GLOBAL(クラス名) REFRESHは、RACF SETROPTS/RDEFINE/RACDCERTのREFRESHで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先確認のクラス名に関する GLOBAL 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず優先確認のクラス名の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先確認のクラス名の証跡として保存して根拠にする。</li><li>C. GLOBAL 属性の変更点を出力本文から切り離して優先確認のクラス名の承認欄のみ残す。</li><li>D. IRRD105I を含む表示を保存し、説明欄との差分を優先確認で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先確認のクラス名において選択記号 D を採用し、識別名は優先確認です。優先確認のクラス名において GLOBAL 属性 は説明欄の「GLOBAL 属性の状態と出力メッセージを結び付ける優先確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は優先確認です。優先確認のクラス名に関する記録は、GLOBAL 属性の出力行と IRRD105I を一緒に保存し、背景名は優先確認です。選択肢ごとの違いを示します。 A: 優先確認のクラス名は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため優先確認ではありません。 B: 優先確認のクラス名は別カテゴリの確認を流用しており、GLOBAL 属性の根拠にならないため優先確認ではありません。 C: 優先確認のクラス名は名称や説明のみに寄り、状態を示す出力本文が不足するため優先確認ではありません。 D: 優先確認のクラス名は対象出力と項目説明を結び、根拠を残すので優先確認です。優先確認のクラス名で記録する GLOBAL 属性は RACF の確認記録に残す対象名であり、用語名は優先確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>GLOBAL(クラス名) REFRESH</strong></p><p>検証目的: 終端照合のクラス名について、GLOBAL(クラス名) REFRESH は、RACF SETROPTS/RDEFINE/RACDCERT の REFRESH で認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010025の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、終端照合のクラス名の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にGLOBAL(クラス名) REFREを指定し、OSKB010025の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND GLOBAL(クラス名) REFRE
CASE OSKB010025
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM GLOBAL(クラス名) REFRE
CASE OSKB010025
SOURCE RACF
GLOBAL(クラス名) REFREとOSKB010025が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010025を同じ出力で読み、終端照合のクラス名の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010025
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010025 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I GLOBAL(クラス名) REFRESH INFORMATION LISTED
IRRD105IとOSKB010025が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の GLOBAL(クラス名) REFRE と OSKB010025 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010025 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0336"><h3>RACLIST(クラス名) REFRESH</h3><p class="kb-meta">分類: REFRESH ・ 難易度: 上級</p><p>RACLIST(クラス名) REFRESHは、RACLIST 済プロファイル変更後の再ロード。「RACLIST(クラス名) REFRESH」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


<section class="kb-item" id="c26-i0337"><h3>REFRESH の RRSF 伝播</h3><p class="kb-meta">分類: REFRESH ・ 難易度: 上級</p><p>REFRESH の RRSF 伝播は、RRSF 接続先ノードに自動伝播される。「REFRESH の RRSF 伝播」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録確認のの 伝播に関係する REFRESH の RRSF 伝播の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、記録確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. REFRESH の RRSF 伝播の名称と担当者名のみを残して記録確認のの 伝播の表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で記録確認のの 伝播を確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず記録確認のの 伝播の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録確認のの 伝播において選択記号 A を採用し、識別名は記録確認です。記録確認のの 伝播において REFRESH の RRSF 伝播 は説明欄の「REFRESH の RRSF 伝播の用途をセキュリティ設定の表示で確認する記録確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認のの 伝播に関連して、RACF では REFRESH の RRSF 伝播の表示属性と IRRD105I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認のの 伝播は対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認のの 伝播は名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認のの 伝播は別カテゴリの確認を流用しており、REFRESH の RRSF 伝播の根拠にならないため記録確認ではありません。 D: 記録確認のの 伝播は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため記録確認ではありません。記録確認のの 伝播で使う REFRESH の RRSF 伝播という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は記録確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REFRESH の RRSF 伝播</strong></p><p>検証目的: 探索照合のの 伝播について、REFRESH の RRSF 伝播は、RRSF 接続先ノードに自動伝播される。「REFRESH の RRSF 伝播」を確認すると、SETROPTS、RDEFINE、RACDに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010026の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、探索照合のの 伝播の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にREFRESH の RRSF 伝播を指定し、OSKB010026の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND REFRESH の RRSF 伝播
CASE OSKB010026
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM REFRESH の RRSF 伝播
CASE OSKB010026
SOURCE RACF
REFRESH の RRSF 伝播とOSKB010026が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010026を同じ出力で読み、探索照合のの 伝播の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010026
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010026 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I REFRESH の RRSF 伝播 INFORMATION LISTED
IRRD105IとOSKB010026が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の REFRESH の RRSF 伝播 と OSKB010026 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010026 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0338"><h3>WHEN(PROGRAM) REFRESH</h3><p class="kb-meta">分類: REFRESH ・ 難易度: 上級</p><p>WHEN(PROGRAM) REFRESHは、RACF SETROPTS/RDEFINE/RACDCERTのREFRESHで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲確認のセキュリティ設定でセキュリティ設定の運用確認を行います。WHEN 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で範囲確認のセキュリティ設定を確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず範囲確認のセキュリティ設定を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて範囲確認の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. WHEN 属性の属性行を読まず範囲確認のセキュリティ設定の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲確認のセキュリティ設定において選択記号 C を採用し、識別名は範囲確認です。範囲確認のセキュリティ設定において WHEN 属性 は説明欄の「RACF で WHEN 属性の扱いを記録する範囲確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は範囲確認です。範囲確認のセキュリティ設定を受け取る担当者は、WHEN 属性の表示結果と IRRD105I を同じ確認単位として扱い、背景名は範囲確認です。不適切な選択肢を整理します。 A: 範囲確認のセキュリティ設定は別カテゴリの確認を流用しており、WHEN 属性の根拠にならないため範囲確認ではありません。 B: 範囲確認のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため範囲確認ではありません。 C: 範囲確認のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので範囲確認です。 D: 範囲確認のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲確認ではありません。範囲確認のセキュリティ設定が示す WHEN 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WHEN(PROGRAM) REFRESH</strong></p><p>検証目的: 置換照合のセキュリティ設定について、WHEN(PROGRAM) REFRESH は、RACF SETROPTS/RDEFINE/RACDCERT の REFRESH で認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010024の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、置換照合のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にWHEN(PROGRAM) REFRを指定し、OSKB010024の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND WHEN(PROGRAM) REFR
CASE OSKB010024
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM WHEN(PROGRAM) REFR
CASE OSKB010024
SOURCE RACF
WHEN(PROGRAM) REFRとOSKB010024が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010024を同じ出力で読み、置換照合のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010024
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010024 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I WHEN(PROGRAM) REFRESH INFORMATION LISTED
IRRD105IとOSKB010024が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の WHEN(PROGRAM) REFR と OSKB010024 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## RLIST


<section class="kb-item" id="c26-i0339"><h3>RLIST * (ワイルドカード)</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST * (ワイルドカード)は、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域照合の* ワイルドカードに関する RLIST * (ワイルドカード)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず値域照合の* ワイルドカードの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域照合の* ワイルドカードの証跡として保存して根拠にする。</li><li>C. RLIST * (ワイルドカード)の変更点を出力本文から切り離して値域照合の* ワイルドカードの承認欄のみ残す。</li><li>D. 同じ画面で対象行と IRRD105I を読み、値域照合の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域照合の* ワイルドカードにおいて選択記号 D を採用し、識別名は値域照合です。値域照合の* ワイルドカードにおいて RLIST * (ワイルドカード) は説明欄の「RLIST * (ワイルドカード)の状態と出力メッセージを結び付ける値域照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合の* ワイルドカードに関する記録は、RLIST * (ワイルドカード)の出力行と IRRD105I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合の* ワイルドカードは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため値域照合ではありません。 B: 値域照合の* ワイルドカードは別カテゴリの確認を流用しており、RLIST * (ワイルドカード)の根拠にならないため値域照合ではありません。 C: 値域照合の* ワイルドカードは名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合の* ワイルドカードは対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合の* ワイルドカードで記録する RLIST * (ワイルドカード)は RACF の確認記録に残す対象名であり、用語名は値域照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST * (ワイルドカード)</strong></p><p>検証目的: 条件確認の* ワイルドカードについて、RLIST * (ワイルドカード)は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030009の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、条件確認の* ワイルドカードの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST * (ワイルドカード)を指定し、OSKB030009の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST * (ワイルドカード)
CASE OSKB030009
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST * (ワイルドカード)
CASE OSKB030009
SOURCE RACF
RLIST * (ワイルドカード)とOSKB030009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030009を同じ出力で読み、条件確認の* ワイルドカードの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030009
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030009 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST * (ワイルドカード) INFORMATION LISTED
IRRD105IとOSKB030009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST * (ワイルドカード) と OSKB030009 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0340"><h3>RLIST ALL</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST ALLは、全属性・全セグメント・統計を出力。「RLIST ALL」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件照合のセキュリティ設定に関係する RLIST ALL の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件照合で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. RLIST ALL の名称と担当者名のみを残して条件照合のセキュリティ設定の表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で条件照合のセキュリティ設定を確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず条件照合のセキュリティ設定の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件照合のセキュリティ設定において選択記号 A を採用し、識別名は条件照合です。条件照合のセキュリティ設定において RLIST ALL は説明欄の「RLIST ALL の用途をセキュリティ設定の表示で確認する条件照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合のセキュリティ設定に関連して、RACF では RLIST ALL の表示属性と IRRD105I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST ALL の根拠にならないため条件照合ではありません。 D: 条件照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため条件照合ではありません。条件照合のセキュリティ設定で使う RLIST ALL という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は条件照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST ALL</strong></p><p>検証目的: 展開確認のセキュリティ設定について、RLIST ALL は、全属性・全セグメント・統計を出力。「RLIST ALL」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030002の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、展開確認のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST ALLを指定し、OSKB030002の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST ALL
CASE OSKB030002
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST ALL
CASE OSKB030002
SOURCE RACF
RLIST ALLとOSKB030002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030002を同じ出力で読み、展開確認のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030002
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030002 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST ALL INFORMATION LISTED
IRRD105IとOSKB030002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST ALL と OSKB030002 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0341"><h3>RLIST AUTHUSER</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST AUTHUSERは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録照合のセキュリティ設定に関係する RLIST AUTHUSER の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、記録照合の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. RLIST AUTHUSER の名称と担当者名のみを残して記録照合のセキュリティ設定の表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で記録照合のセキュリティ設定を確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず記録照合のセキュリティ設定の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録照合のセキュリティ設定において選択記号 A を採用し、識別名は記録照合です。記録照合のセキュリティ設定において RLIST AUTHUSER は説明欄の「RLIST AUTHUSER の用途をセキュリティ設定の表示で確認する記録照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合のセキュリティ設定に関連して、RACF では RLIST AUTHUSER の表示属性と IRRD105I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST AUTHUSER の根拠にならないため記録照合ではありません。 D: 記録照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため記録照合ではありません。記録照合のセキュリティ設定で使う RLIST AUTHUSER という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は記録照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST AUTHUSER</strong></p><p>検証目的: 探索確認のセキュリティ設定について、RLIST AUTHUSER は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030006の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、探索確認のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST AUTHUSERを指定し、OSKB030006の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST AUTHUSER
CASE OSKB030006
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST AUTHUSER
CASE OSKB030006
SOURCE RACF
RLIST AUTHUSERとOSKB030006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030006を同じ出力で読み、探索確認のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030006
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030006 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST AUTHUSER INFORMATION LISTED
IRRD105IとOSKB030006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST AUTHUSER と OSKB030006 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0342"><h3>RLIST GENERIC</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST GENERICは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較照合のセキュリティ設定で RLIST GENERIC の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. RLIST GENERIC の出力を取らず比較照合のセキュリティ設定の説明文と承認印のみを残す。</li><li>B. 出典欄の説明と運用出力を照合し、比較照合の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して比較照合のセキュリティ設定の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較照合のセキュリティ設定へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較照合のセキュリティ設定において選択記号 B を採用し、識別名は比較照合です。比較照合のセキュリティ設定において RLIST GENERIC は説明欄の「比較照合のセキュリティ設定に関係する定義値と表示行を照合する比較照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合のセキュリティ設定の証跡を読む担当者は、RLIST GENERIC の属性行と IRRD105I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため比較照合ではありません。 D: 比較照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST GENERIC の根拠にならないため比較照合ではありません。比較照合のセキュリティ設定に出る RLIST GENERIC は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は比較照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST GENERIC</strong></p><p>検証目的: 上書確認のセキュリティ設定について、RLIST GENERIC は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030007の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、上書確認のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST GENERICを指定し、OSKB030007の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST GENERIC
CASE OSKB030007
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST GENERIC
CASE OSKB030007
SOURCE RACF
RLIST GENERICとOSKB030007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030007を同じ出力で読み、上書確認のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030007
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030007 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST GENERIC INFORMATION LISTED
IRRD105IとOSKB030007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST GENERIC と OSKB030007 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0343"><h3>RLIST HISTORY</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST HISTORYは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切照合のセキュリティ設定で RLIST HISTORY の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. RLIST HISTORY の出力を取らず区切照合のセキュリティ設定の説明文と承認印のみを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、区切照合の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して区切照合のセキュリティ設定の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切照合のセキュリティ設定へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切照合のセキュリティ設定において選択記号 B を採用し、識別名は区切照合です。区切照合のセキュリティ設定において RLIST HISTORY は説明欄の「区切照合のセキュリティ設定に関係する定義値と表示行を照合する区切照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合のセキュリティ設定の証跡を読む担当者は、RLIST HISTORY の属性行と IRRD105I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため区切照合ではありません。 D: 区切照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST HISTORY の根拠にならないため区切照合ではありません。区切照合のセキュリティ設定に出る RLIST HISTORY は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は区切照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST HISTORY</strong></p><p>検証目的: 呼出確認のセキュリティ設定について、RLIST HISTORY は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030003の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、呼出確認のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST HISTORYを指定し、OSKB030003の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST HISTORY
CASE OSKB030003
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST HISTORY
CASE OSKB030003
SOURCE RACF
RLIST HISTORYとOSKB030003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030003を同じ出力で読み、呼出確認のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030003
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030003 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST HISTORY INFORMATION LISTED
IRRD105IとOSKB030003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST HISTORY と OSKB030003 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0344"><h3>RLIST NORACF</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST NORACFは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力照合のセキュリティ設定に関する RLIST NORACF の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず出力照合のセキュリティ設定の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力照合のセキュリティ設定の証跡として保存して根拠にする。</li><li>C. RLIST NORACF の変更点を出力本文から切り離して出力照合のセキュリティ設定の承認欄のみ残す。</li><li>D. RACF の表示形式に沿って根拠行を採り、出力照合の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力照合のセキュリティ設定において選択記号 D を採用し、識別名は出力照合です。出力照合のセキュリティ設定において RLIST NORACF は説明欄の「RLIST NORACF の状態と出力メッセージを結び付ける出力照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合のセキュリティ設定に関する記録は、RLIST NORACF の出力行と IRRD105I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため出力照合ではありません。 B: 出力照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST NORACF の根拠にならないため出力照合ではありません。 C: 出力照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合のセキュリティ設定で記録する RLIST NORACF は RACF の確認記録に残す対象名であり、用語名は出力照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST NORACF</strong></p><p>検証目的: 構文確認のセキュリティ設定について、RLIST NORACF は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030001の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、構文確認のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST NORACFを指定し、OSKB030001の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST NORACF
CASE OSKB030001
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST NORACF
CASE OSKB030001
SOURCE RACF
RLIST NORACFとOSKB030001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030001を同じ出力で読み、構文確認のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030001
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030001 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST NORACF INFORMATION LISTED
IRRD105IとOSKB030001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST NORACF と OSKB030001 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0345"><h3>RLIST RESGROUP</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST RESGROUPは、メンバが属する GROUP プロファイルを表示。「RLIST RESGROUP」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先照合のセキュリティ設定に関する RLIST RESGROUP の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず優先照合のセキュリティ設定の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先照合のセキュリティ設定の証跡として保存して根拠にする。</li><li>C. RLIST RESGROUP の変更点を出力本文から切り離して優先照合のセキュリティ設定の承認欄のみ残す。</li><li>D. IRRD105I を含む表示を保存し、説明欄との差分を優先照合で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先照合のセキュリティ設定において選択記号 D を採用し、識別名は優先照合です。優先照合のセキュリティ設定において RLIST RESGROUP は説明欄の「RLIST RESGROUP の状態と出力メッセージを結び付ける優先照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合のセキュリティ設定に関する記録は、RLIST RESGROUP の出力行と IRRD105I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため優先照合ではありません。 B: 優先照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST RESGROUP の根拠にならないため優先照合ではありません。 C: 優先照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合のセキュリティ設定で記録する RLIST RESGROUP は RACF の確認記録に残す対象名であり、用語名は優先照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST RESGROUP</strong></p><p>検証目的: 終端確認のセキュリティ設定について、RLIST RESGROUP は、メンバが属する GROUP プロファイルを表示。「RLIST RESGROUP」を確認すると、SETROPTS、RDEFINE、RACDCEに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030005の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、終端確認のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST RESGROUPを指定し、OSKB030005の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST RESGROUP
CASE OSKB030005
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST RESGROUP
CASE OSKB030005
SOURCE RACF
RLIST RESGROUPとOSKB030005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030005を同じ出力で読み、終端確認のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030005
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030005 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST RESGROUP INFORMATION LISTED
IRRD105IとOSKB030005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST RESGROUP と OSKB030005 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0346"><h3>RLIST STATISTICS</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST STATISTICSは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲照合のセキュリティ設定でセキュリティ設定の運用確認を行います。RLIST STATISTICS の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で範囲照合のセキュリティ設定を確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず範囲照合のセキュリティ設定を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて範囲照合の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. RLIST STATISTICS の属性行を読まず範囲照合のセキュリティ設定の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲照合のセキュリティ設定において選択記号 C を採用し、識別名は範囲照合です。範囲照合のセキュリティ設定において RLIST STATISTICS は説明欄の「RACF で RLIST STATISTICS の扱いを記録する範囲照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合のセキュリティ設定を受け取る担当者は、RLIST STATISTICS の表示結果と IRRD105I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合のセキュリティ設定は別カテゴリの確認を流用しており、RLIST STATISTICS の根拠にならないため範囲照合ではありません。 B: 範囲照合のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合のセキュリティ設定が示す RLIST STATISTICS は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST STATISTICS</strong></p><p>検証目的: 置換確認のセキュリティ設定について、RLIST STATISTICS は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030004の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、置換確認のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST STATISTICSを指定し、OSKB030004の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST STATISTICS
CASE OSKB030004
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST STATISTICS
CASE OSKB030004
SOURCE RACF
RLIST STATISTICSとOSKB030004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030004を同じ出力で読み、置換確認のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030004
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030004 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST STATISTICS INFORMATION LISTED
IRRD105IとOSKB030004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST STATISTICS と OSKB030004 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0347"><h3>RLIST STDATA/TME/SSIGNON 等セグメント</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST STDATA/TME/SSIGNON 等セグメントは、クラス特有のセグメントを表示。「RLIST STDATA/TME/SSIGNON 等セグメント」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 属性照合通知の属性照合として RLIST を確認するとき、後続担当者へ残すべき証跡はどれですか。</p><ul class="kb-choices"><li>A. 承認欄の記入を優先して出力メッセージを保存しない。</li><li>B. 名称と担当者名を保存して表示本文を確認しない。</li><li>C. 属性照合の確認結果を出典名と表示本文に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>D. 別分類の結果を流用して同じ証跡として扱う。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正解はCです。属性照合通知で扱う RLIST は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（属性照合通知用語）。属性照合通知の担当者は属性照合として、表示本文とメッセージを照合します（属性照合通知照合）。属性照合通知の対応を残すと、後続担当者は同じ出典に戻って確認できます（属性照合通知出典）。A: 属性照合通知で表示とメッセージを結ぶ場合に根拠になります（属性照合通知A）。B: 属性照合通知で定義と出力の関係がない場合は追跡できません（属性照合通知B）。C: 属性照合通知で出典名のみでは実際の表示を説明できません（属性照合通知C）。D: 属性照合通知で操作記録のみでは値や状態の確認が不足します（属性照合通知D）。属性照合通知の初出用語として RLIST を扱い、分類内の確認名として保存します（属性照合通知終点）。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST STDATA ・ TME ・ SSIGNON 等セグメント</strong></p><p>検証目的: 出力確認の・ ・について、RLIST STDATA/TME/SSIGNON 等セグメントは、クラス特有のセグメントを表示。「RLIST STDATA/TME/SSIGNON 等セグメント」を確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030008の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、出力確認の・ ・の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST STDATA ・ TMEを指定し、OSKB030008の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST STDATA ・ TME
CASE OSKB030008
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST STDATA ・ TME
CASE OSKB030008
SOURCE RACF
RLIST STDATA ・ TMEとOSKB030008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030008を同じ出力で読み、出力確認の・ ・の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030008
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030008 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST STDATA ・ TME ・ SSIGNON INFORMATION LISTED
IRRD105IとOSKB030008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST STDATA ・ TME と OSKB030008 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0348"><h3>RLIST と AUDITOR</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST と AUDITORは、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告照合のとに関係する RLIST と AUDITOR の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、警告照合の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. RLIST と AUDITOR の名称と担当者名のみを残して警告照合のとの表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で警告照合のとを確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず警告照合のとの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告照合のとにおいて選択記号 A を採用し、識別名は警告照合です。警告照合のとにおいて RLIST と AUDITOR は説明欄の「RLIST と AUDITOR の用途をセキュリティ設定の表示で確認する警告照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合のとに関連して、RACF では RLIST と AUDITOR の表示属性と IRRD105I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合のとは対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合のとは名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合のとは別カテゴリの確認を流用しており、RLIST と AUDITOR の根拠にならないため警告照合ではありません。 D: 警告照合のとは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため警告照合ではありません。警告照合のとで使う RLIST と AUDITOR という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は警告照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST と AUDITOR</strong></p><p>検証目的: 区切確認のとについて、RLIST と AUDITOR は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030010の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、区切確認のとの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST と AUDITORを指定し、OSKB030010の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST と AUDITOR
CASE OSKB030010
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST と AUDITOR
CASE OSKB030010
SOURCE RACF
RLIST と AUDITORとOSKB030010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030010を同じ出力で読み、区切確認のとの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030010
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030010 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST と AUDITOR INFORMATION LISTED
IRRD105IとOSKB030010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST と AUDITOR と OSKB030010 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0349"><h3>RLIST の目的</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST の目的は、一般リソース プロファイルの属性表示。「RLIST の目的」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索照合のの目的で RLIST の目的の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. RLIST の目的の出力を取らず探索照合のの目的の説明文と承認印のみを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、探索照合として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して探索照合のの目的の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索照合のの目的へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索照合のの目的において選択記号 B を採用し、識別名は探索照合です。探索照合のの目的において RLIST の目的 は説明欄の「探索照合のの目的に関係する定義値と表示行を照合する探索照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合のの目的の証跡を読む担当者は、RLIST の目的の属性行と IRRD105I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合のの目的は名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合のの目的は対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合のの目的は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため探索照合ではありません。 D: 探索照合のの目的は別カテゴリの確認を流用しており、RLIST の目的の根拠にならないため探索照合ではありません。探索照合のの目的に出る RLIST の目的は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は探索照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST の目的</strong></p><p>検証目的: 監査整理のの目的について、RLIST の目的は、一般リソース プロファイルの属性表示。「RLIST の目的」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020119の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、監査整理のの目的の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST の目的を指定し、OSKB020119の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST の目的
CASE OSKB020119
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST の目的
CASE OSKB020119
SOURCE RACF
RLIST の目的とOSKB020119が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020119を同じ出力で読み、監査整理のの目的の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020119
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020119 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST の目的 INFORMATION LISTED
IRRD105IとOSKB020119が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST の目的 と OSKB020119 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020119 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0350"><h3>RLIST 構文</h3><p class="kb-meta">分類: RLIST ・ 難易度: 上級</p><p>RLIST 構文は、RACF SETROPTS/RDEFINE/RACDCERTのRLISTで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書照合の構文でセキュリティ設定の運用確認を行います。RLIST 構文の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で上書照合の構文を確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず上書照合の構文を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書照合の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. RLIST 構文の属性行を読まず上書照合の構文の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書照合の構文において選択記号 C を採用し、識別名は上書照合です。上書照合の構文において RLIST 構文 は説明欄の「RACF で RLIST 構文の扱いを記録する上書照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合の構文を受け取る担当者は、RLIST 構文の表示結果と IRRD105I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合の構文は別カテゴリの確認を流用しており、RLIST 構文の根拠にならないため上書照合ではありません。 B: 上書照合の構文は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため上書照合ではありません。 C: 上書照合の構文は対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合の構文は名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合の構文が示す RLIST 構文は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RLIST 構文</strong></p><p>検証目的: 変更整理の構文について、RLIST 構文は、RACF SETROPTS/RDEFINE/RACDCERT の RLIST で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020120の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、変更整理の構文の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRLIST 構文を指定し、OSKB020120の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RLIST 構文
CASE OSKB020120
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RLIST 構文
CASE OSKB020120
SOURCE RACF
RLIST 構文とOSKB020120が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020120を同じ出力で読み、変更整理の構文の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020120
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020120 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RLIST 構文 INFORMATION LISTED
IRRD105IとOSKB020120が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RLIST 構文 と OSKB020120 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020120 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## SECLABEL


<section class="kb-item" id="c26-i0351"><h3>COMPATMODE</h3><p class="kb-meta">分類: SECLABEL ・ 難易度: 上級</p><p>COMPATMODEは、古い MLS 互換モード (CC EAL 評価用)。「COMPATMODE」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>COMPATMODE</strong></p><p>検証目的: 呼出判定のセキュリティ設定について、COMPATMODE は、古い MLS 互換モード (CC EAL 評価用)。「COMPATMODE」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010083の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、呼出判定のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にCOMPATMODEを指定し、OSKB010083の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND COMPATMODE
CASE OSKB010083
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM COMPATMODE
CASE OSKB010083
SOURCE RACF
COMPATMODEとOSKB010083が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010083を同じ出力で読み、呼出判定のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010083
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010083 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I COMPATMODE INFORMATION LISTED
IRRD105IとOSKB010083が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の COMPATMODE と OSKB010083 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010083 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0352"><h3>NOCOMPATMODE</h3><p class="kb-meta">分類: SECLABEL ・ 難易度: 上級</p><p>NOCOMPATMODEは、RACF SETROPTS/RDEFINE/RACDCERTのSECLABELで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>NOCOMPATMODE</strong></p><p>検証目的: 置換判定のセキュリティ設定について、NOCOMPATMODE は、RACF SETROPTS/RDEFINE/RACDCERT の SECLABEL で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010084の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、置換判定のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にNOCOMPATMODEを指定し、OSKB010084の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND NOCOMPATMODE
CASE OSKB010084
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM NOCOMPATMODE
CASE OSKB010084
SOURCE RACF
NOCOMPATMODEとOSKB010084が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010084を同じ出力で読み、置換判定のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010084
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010084 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I NOCOMPATMODE INFORMATION LISTED
IRRD105IとOSKB010084が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の NOCOMPATMODE と OSKB010084 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010084 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0353"><h3>NOSECLABELCONTROL</h3><p class="kb-meta">分類: SECLABEL ・ 難易度: 上級</p><p>NOSECLABELCONTROLは、RACF SETROPTS/RDEFINE/RACDCERTのSECLABELで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>NOSECLABELCONTROL</strong></p><p>検証目的: 展開判定のセキュリティ設定について、NOSECLABELCONTROL は、RACF SETROPTS/RDEFINE/RACDCERT の SECLABEL で認証、権限、またはセキュリティ設定を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010082の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、展開判定のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にNOSECLABELCONTROLを指定し、OSKB010082の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND NOSECLABELCONTROL
CASE OSKB010082
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM NOSECLABELCONTROL
CASE OSKB010082
SOURCE RACF
NOSECLABELCONTROLとOSKB010082が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010082を同じ出力で読み、展開判定のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010082
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010082 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I NOSECLABELCONTROL INFORMATION LISTED
IRRD105IとOSKB010082が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の NOSECLABELCONTROL と OSKB010082 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010082 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0354"><h3>SECLABELAUDIT</h3><p class="kb-meta">分類: SECLABEL ・ 難易度: 上級</p><p>SECLABELAUDITは、RACF SETROPTS/RDEFINE/RACDCERTのSECLABELで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SECLABELAUDIT</strong></p><p>検証目的: 終端判定のセキュリティ設定について、SECLABELAUDIT は、RACF SETROPTS/RDEFINE/RACDCERT の SECLABEL で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010085の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、終端判定のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSECLABELAUDITを指定し、OSKB010085の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SECLABELAUDIT
CASE OSKB010085
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SECLABELAUDIT
CASE OSKB010085
SOURCE RACF
SECLABELAUDITとOSKB010085が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010085を同じ出力で読み、終端判定のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010085
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010085 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SECLABELAUDIT INFORMATION LISTED
IRRD105IとOSKB010085が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SECLABELAUDIT と OSKB010085 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010085 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0355"><h3>SECLABELCONTROL</h3><p class="kb-meta">分類: SECLABEL ・ 難易度: 上級</p><p>SECLABELCONTROLは、RACF SETROPTS/RDEFINE/RACDCERTのSECLABELで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SECLABELCONTROL</strong></p><p>検証目的: 構文判定のセキュリティ設定について、SECLABELCONTROL は、RACF SETROPTS/RDEFINE/RACDCERT の SECLABEL で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010081の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、構文判定のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSECLABELCONTROLを指定し、OSKB010081の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SECLABELCONTROL
CASE OSKB010081
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SECLABELCONTROL
CASE OSKB010081
SOURCE RACF
SECLABELCONTROLとOSKB010081が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010081を同じ出力で読み、構文判定のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010081
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010081 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SECLABELCONTROL INFORMATION LISTED
IRRD105IとOSKB010081が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SECLABELCONTROL と OSKB010081 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010081 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## SETROPTS 基本


<section class="kb-item" id="c26-i0356"><h3>SETROPTS LIST</h3><p class="kb-meta">分類: SETROPTS 基本 ・ 難易度: 上級</p><p>現行 RACF オプション設定を全件表示。AUDITOR でも可。「SETROPTS LIST」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


<section class="kb-item" id="c26-i0357"><h3>SETROPTS と RACF データベース</h3><p class="kb-meta">分類: SETROPTS 基本 ・ 難易度: 上級</p><p>SETROPTS と RACF データベースは、DB が読み専用の場合 SETROPTS の更新系は失敗。「SETROPTS と RACF データベース」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SETROPTS と RACF データベース</strong></p><p>検証目的: 展開確認のと データベースについて、SETROPTS と RACF データベースは、DB が読み専用の場合 SETROPTS の更新系は失敗。「SETROPTS と RACF データベース」を確認すると、SEに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、展開確認のと データベースの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSETROPTS と RACF デーを指定し、OSKB010002の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SETROPTS と RACF デー
CASE OSKB010002
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SETROPTS と RACF デー
CASE OSKB010002
SOURCE RACF
SETROPTS と RACF デーとOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010002を同じ出力で読み、展開確認のと データベースの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010002
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010002 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SETROPTS と RACF データベース INFORMATION LISTED
IRRD105IとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SETROPTS と RACF デー と OSKB010002 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0358"><h3>SETROPTS の伝播</h3><p class="kb-meta">分類: SETROPTS 基本 ・ 難易度: 上級</p><p>SETROPTS の伝播は、RACF SETROPTS/RDEFINE/RACDCERTのSETROPTS 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SETROPTS の伝播</strong></p><p>検証目的: 構文確認のの伝播について、SETROPTS の伝播は、RACF SETROPTS/RDEFINE/RACDCERT の SETROPTS 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、構文確認のの伝播の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSETROPTS の伝播を指定し、OSKB010001の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SETROPTS の伝播
CASE OSKB010001
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SETROPTS の伝播
CASE OSKB010001
SOURCE RACF
SETROPTS の伝播とOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010001を同じ出力で読み、構文確認のの伝播の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010001
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010001 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SETROPTS の伝播 INFORMATION LISTED
IRRD105IとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SETROPTS の伝播 と OSKB010001 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0359"><h3>SETROPTS の永続性</h3><p class="kb-meta">分類: SETROPTS 基本 ・ 難易度: 上級</p><p>SETROPTS の永続性は、RACF SETROPTS/RDEFINE/RACDCERTのSETROPTS 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


<section class="kb-item" id="c26-i0360"><h3>SETROPTS の目的</h3><p class="kb-meta">分類: SETROPTS 基本 ・ 難易度: 上級</p><p>SETROPTS の目的は、RACF システム全体のオプションを動的に変更するコマンド。「SETROPTS の目的」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


<section class="kb-item" id="c26-i0361"><h3>SETROPTS 実行権限</h3><p class="kb-meta">分類: SETROPTS 基本 ・ 難易度: 上級</p><p>SETROPTS 実行権限は、RACF SETROPTS/RDEFINE/RACDCERTのSETROPTS 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


<section class="kb-item" id="c26-i0362"><h3>SETROPTS 短縮形 SETR</h3><p class="kb-meta">分類: SETROPTS 基本 ・ 難易度: 上級</p><p>SETROPTS 短縮形 SETRは、RACF SETROPTS/RDEFINE/RACDCERTのSETROPTS 基本で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></section>


## SMF 80


<section class="kb-item" id="c26-i0363"><h3>IRRADU00 と DB2 LOAD</h3><p class="kb-meta">分類: SMF 80 ・ 難易度: 上級</p><p>IRRADU00 と DB2 LOADは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開追跡のとで IRRADU00 と DB2 LOAD の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. IRRADU00 と DB2 LOAD の出力を取らず展開追跡のとの説明文と承認印のみを残す。</li><li>B. IRRD105I を含む表示を保存し、説明欄との差分を展開追跡で確認する。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して展開追跡のとの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開追跡のとへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開追跡のとにおいて選択記号 B を採用し、識別名は展開追跡です。展開追跡のとにおいて IRRADU00 と DB2 LOAD は説明欄の「展開追跡のとに関係する定義値と表示行を照合する展開追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡のとの証跡を読む担当者は、IRRADU00 と DB2 LOAD の属性行と IRRD105I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡のとは名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡のとは対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡のとは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡のとは別カテゴリの確認を流用しており、IRRADU00 と DB2 LOAD の根拠にならないため展開追跡ではありません。展開追跡のとに出る IRRADU00 と DB2 LOAD は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は展開追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRADU00 と DB2 LOAD</strong></p><p>検証目的: 順序整理のとについて、IRRADU00 と DB2 LOAD は、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030115の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、順序整理のとの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRADU00 と DB2 LOAを指定し、OSKB030115の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRADU00 と DB2 LOA
CASE OSKB030115
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRADU00 と DB2 LOA
CASE OSKB030115
SOURCE RACF
IRRADU00 と DB2 LOAとOSKB030115が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030115を同じ出力で読み、順序整理のとの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030115
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030115 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRADU00 と DB2 LOAD INFORMATION LISTED
IRRD105IとOSKB030115が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRADU00 と DB2 LOA と OSKB030115 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030115 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0364"><h3>RACFRW (RACF Report Writer)</h3><p class="kb-meta">分類: SMF 80 ・ 難易度: 上級</p><p>RACFRW (RACF Report Writer)は、古い SMF 80 レポート ツール (非推奨)。「RACFRW (RACF Report Writer)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出追跡のセキュリティ設定でセキュリティ設定の運用確認を行います。RACFRW 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で呼出追跡のセキュリティ設定を確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず呼出追跡のセキュリティ設定を正常終了として記録する。</li><li>C. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、呼出追跡の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>D. RACFRW 属性の属性行を読まず呼出追跡のセキュリティ設定の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出追跡のセキュリティ設定において選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のセキュリティ設定において RACFRW 属性 は説明欄の「RACF で RACFRW 属性の扱いを記録する呼出追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のセキュリティ設定を受け取る担当者は、RACFRW 属性の表示結果と IRRD105I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のセキュリティ設定は別カテゴリの確認を流用しており、RACFRW 属性の根拠にならないため呼出追跡ではありません。 B: 呼出追跡のセキュリティ設定は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のセキュリティ設定は対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のセキュリティ設定は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のセキュリティ設定が示す RACFRW 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RACFRW (RACF Report Writer)</strong></p><p>検証目的: 値域整理のセキュリティ設定について、RACFRW (RACF Report Writer)は、古い SMF 80 レポート ツール (非推奨)。「RACFRW (RACF Report Writer)」を確認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030116の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、値域整理のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRACFRW (RACF Reporを指定し、OSKB030116の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RACFRW (RACF Repor
CASE OSKB030116
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RACFRW (RACF Repor
CASE OSKB030116
SOURCE RACF
RACFRW (RACF ReporとOSKB030116が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030116を同じ出力で読み、値域整理のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030116
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030116 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RACFRW (RACF Report Writ INFORMATION LISTED
IRRD105IとOSKB030116が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RACFRW (RACF Repor と OSKB030116 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030116 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0365"><h3>SMF 80 と IRRADU00</h3><p class="kb-meta">分類: SMF 80 ・ 難易度: 上級</p><p>SMF 80 と IRRADU00は、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文追跡のとに関係する SMF 80 と IRRADU00 の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 参照資料名、表示行、メッセージをそろえて構文追跡の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>B. SMF 80 と IRRADU00 の名称と担当者名のみを残して構文追跡のとの表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で構文追跡のとを確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず構文追跡のとの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文追跡のとにおいて選択記号 A を採用し、識別名は構文追跡です。構文追跡のとにおいて SMF 80 と IRRADU00 は説明欄の「SMF 80 と IRRADU00 の用途をセキュリティ設定の表示で確認する構文追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡のとに関連して、RACF では SMF 80 と IRRADU00 の表示属性と IRRD105I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡のとは対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡のとは名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡のとは別カテゴリの確認を流用しており、SMF 80 と IRRADU00 の根拠にならないため構文追跡ではありません。 D: 構文追跡のとは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため構文追跡ではありません。構文追跡のとで使う SMF 80 と IRRADU00 という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は構文追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF 80 と IRRADU00</strong></p><p>検証目的: 比較整理のとについて、SMF 80 と IRRADU00 は、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030114の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、比較整理のとの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 と IRRADU00を指定し、OSKB030114の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SMF 80 と IRRADU00
CASE OSKB030114
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SMF 80 と IRRADU00
CASE OSKB030114
SOURCE RACF
SMF 80 と IRRADU00とOSKB030114が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030114を同じ出力で読み、比較整理のとの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030114
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030114 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SMF 80 と IRRADU00 INFORMATION LISTED
IRRD105IとOSKB030114が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SMF 80 と IRRADU00 と OSKB030114 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030114 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0366"><h3>SMF 80 と OMEGAMON/zSecure</h3><p class="kb-meta">分類: SMF 80 ・ 難易度: 上級</p><p>SMF 80 と OMEGAMON/zSecureは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲照合入力の範囲照合として SMF を確認するとき、後続担当者へ残すべき証跡はどれですか。</p><ul class="kb-choices"><li>A. 範囲照合の表示本文とメッセージを照合して記録する。 <span class="kb-ok">✅ 正解</span></li><li>B. 名称と担当者名を保存して表示本文を確認しない。</li><li>C. 別分類の結果を流用して同じ証跡として扱う。</li><li>D. 戻り値と時刻を主な根拠にして表示行を読まない。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正解はAです。範囲照合入力で扱う SMF は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（範囲照合入力用語）。範囲照合入力の担当者は範囲照合として、表示本文とメッセージを照合します（範囲照合入力照合）。範囲照合入力の対応を残すと、後続担当者は同じ出典に戻って確認できます（範囲照合入力出典）。A: 範囲照合入力で表示とメッセージを結ぶ場合に根拠になります（範囲照合入力A）。B: 範囲照合入力で定義と出力の関係がない場合は追跡できません（範囲照合入力B）。C: 範囲照合入力で出典名のみでは実際の表示を説明できません（範囲照合入力C）。D: 範囲照合入力で操作記録のみでは値や状態の確認が不足します（範囲照合入力D）。範囲照合入力の初出用語として SMF を扱い、分類内の確認名として保存します（範囲照合入力終点）。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF 80 と OMEGAMON ・zSecure</strong></p><p>検証目的: 復旧整理のと ・について、SMF 80 と OMEGAMON/zSecureは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030118の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、復旧整理のと ・の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 と OMEGAMON を指定し、OSKB030118の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SMF 80 と OMEGAMON 
CASE OSKB030118
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SMF 80 と OMEGAMON 
CASE OSKB030118
SOURCE RACF
SMF 80 と OMEGAMON とOSKB030118が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030118を同じ出力で読み、復旧整理のと ・の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030118
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030118 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SMF 80 と OMEGAMON ・zSecur INFORMATION LISTED
IRRD105IとOSKB030118が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SMF 80 と OMEGAMON  と OSKB030118 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030118 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0367"><h3>SMF 80 イベント コード</h3><p class="kb-meta">分類: SMF 80 ・ 難易度: 上級</p><p>SMF 80 イベント コードは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査照合のイベント コードでセキュリティ設定の運用確認を行います。SMF 80 イベント コードの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で監査照合のイベント コードを確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず監査照合のイベント コードを正常終了として記録する。</li><li>C. 対象の出力行とメッセージ接頭辞を同時に記録し、監査照合で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>D. SMF 80 イベント コードの属性行を読まず監査照合のイベント コードの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査照合のイベント コードにおいて選択記号 C を採用し、識別名は監査照合です。監査照合のイベント コードにおいて SMF 80 イベント コード は説明欄の「RACF で SMF 80 イベント コードの扱いを記録する監査照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合のイベント コードを受け取る担当者は、SMF 80 イベント コードの表示結果と IRRD105I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合のイベント コードは別カテゴリの確認を流用しており、SMF 80 イベント コードの根拠にならないため監査照合ではありません。 B: 監査照合のイベント コードは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため監査照合ではありません。 C: 監査照合のイベント コードは対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合のイベント コードは名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合のイベント コードが示す SMF 80 イベント コードは出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF 80 イベント コード</strong></p><p>検証目的: 優先整理のイベント コードについて、SMF 80 イベント コードは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030112の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、優先整理のイベント コードの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 イベント コードを指定し、OSKB030112の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SMF 80 イベント コード
CASE OSKB030112
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SMF 80 イベント コード
CASE OSKB030112
SOURCE RACF
SMF 80 イベント コードとOSKB030112が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030112を同じ出力で読み、優先整理のイベント コードの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030112
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030112 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SMF 80 イベント コード INFORMATION LISTED
IRRD105IとOSKB030112が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SMF 80 イベント コード と OSKB030112 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030112 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0368"><h3>SMF 80 サブタイプ</h3><p class="kb-meta">分類: SMF 80 ・ 難易度: 上級</p><p>SMF 80 サブタイプは、イベントの詳細分類。「SMF 80 サブタイプ」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更照合のサブタイプに関する SMF 80 サブタイプの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず変更照合のサブタイプの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更照合のサブタイプの証跡として保存して根拠にする。</li><li>C. SMF 80 サブタイプの変更点を出力本文から切り離して変更照合のサブタイプの承認欄のみ残す。</li><li>D. 机上確認でも実出力の見出しに合わせ、変更照合の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更照合のサブタイプにおいて選択記号 D を採用し、識別名は変更照合です。変更照合のサブタイプにおいて SMF 80 サブタイプ は説明欄の「SMF 80 サブタイプの状態と出力メッセージを結び付ける変更照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は変更照合です。変更照合のサブタイプに関する記録は、SMF 80 サブタイプの出力行と IRRD105I を一緒に保存し、背景名は変更照合です。選択肢ごとの違いを示します。 A: 変更照合のサブタイプは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため変更照合ではありません。 B: 変更照合のサブタイプは別カテゴリの確認を流用しており、SMF 80 サブタイプの根拠にならないため変更照合ではありません。 C: 変更照合のサブタイプは名称や説明のみに寄り、状態を示す出力本文が不足するため変更照合ではありません。 D: 変更照合のサブタイプは対象出力と項目説明を結び、根拠を残すので変更照合です。変更照合のサブタイプで記録する SMF 80 サブタイプは RACF の確認記録に残す対象名であり、用語名は変更照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF 80 サブタイプ</strong></p><p>検証目的: 記録整理のサブタイプについて、SMF 80 サブタイプは、イベントの詳細分類。「SMF 80 サブタイプ」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030113の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、記録整理のサブタイプの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 サブタイプを指定し、OSKB030113の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SMF 80 サブタイプ
CASE OSKB030113
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SMF 80 サブタイプ
CASE OSKB030113
SOURCE RACF
SMF 80 サブタイプとOSKB030113が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030113を同じ出力で読み、記録整理のサブタイプの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030113
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030113 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SMF 80 サブタイプ INFORMATION LISTED
IRRD105IとOSKB030113が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SMF 80 サブタイプ と OSKB030113 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030113 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0369"><h3>SMF 80 フィールド</h3><p class="kb-meta">分類: SMF 80 ・ 難易度: 上級</p><p>SMF 80 フィールドは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換追跡のフィールドに関する SMF 80 フィールドの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず置換追跡のフィールドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換追跡のフィールドの証跡として保存して根拠にする。</li><li>C. SMF 80 フィールドの変更点を出力本文から切り離して置換追跡のフィールドの承認欄のみ残す。</li><li>D. 出典欄の説明と運用出力を照合し、置換追跡の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換追跡のフィールドにおいて選択記号 D を採用し、識別名は置換追跡です。置換追跡のフィールドにおいて SMF 80 フィールド は説明欄の「SMF 80 フィールドの状態と出力メッセージを結び付ける置換追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡のフィールドに関する記録は、SMF 80 フィールドの出力行と IRRD105I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡のフィールドは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡のフィールドは別カテゴリの確認を流用しており、SMF 80 フィールドの根拠にならないため置換追跡ではありません。 C: 置換追跡のフィールドは名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡のフィールドは対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡のフィールドで記録する SMF 80 フィールドは RACF の確認記録に残す対象名であり、用語名は置換追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF 80 フィールド</strong></p><p>検証目的: 警告整理のフィールドについて、SMF 80 フィールドは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030117の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、警告整理のフィールドの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 フィールドを指定し、OSKB030117の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SMF 80 フィールド
CASE OSKB030117
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SMF 80 フィールド
CASE OSKB030117
SOURCE RACF
SMF 80 フィールドとOSKB030117が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030117を同じ出力で読み、警告整理のフィールドの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030117
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030117 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SMF 80 フィールド INFORMATION LISTED
IRRD105IとOSKB030117が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SMF 80 フィールド と OSKB030117 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030117 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0370"><h3>SMF 80 生成制御</h3><p class="kb-meta">分類: SMF 80 ・ 難易度: 上級</p><p>SMF 80 生成制御は、SETROPTS AUDIT/SAUDIT/OPERAUDIT/LOGOPTIONS 等で制御。「SMF 80 生成制御」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索追跡の生成制御で SMF 80 生成制御の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SMF 80 生成制御の出力を取らず探索追跡の生成制御の説明文と承認印のみを残す。</li><li>B. 同じ画面で対象行と IRRD105I を読み、探索追跡の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して探索追跡の生成制御の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索追跡の生成制御へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索追跡の生成制御において選択記号 B を採用し、識別名は探索追跡です。探索追跡の生成制御において SMF 80 生成制御 は説明欄の「探索追跡の生成制御に関係する定義値と表示行を照合する探索追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡の生成制御の証跡を読む担当者は、SMF 80 生成制御の属性行と IRRD105I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡の生成制御は名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡の生成制御は対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡の生成制御は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡の生成制御は別カテゴリの確認を流用しており、SMF 80 生成制御の根拠にならないため探索追跡ではありません。探索追跡の生成制御に出る SMF 80 生成制御は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は探索追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF 80 生成制御</strong></p><p>検証目的: 監査整理の生成制御について、SMF 80 生成制御は、SETROPTS AUDIT/SAUDIT/OPERAUDIT/LOGOPTIONS 等で制御。「SMF 80 生成制御」を確認すると、SETROに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030119の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、監査整理の生成制御の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSMF 80 生成制御を指定し、OSKB030119の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SMF 80 生成制御
CASE OSKB030119
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SMF 80 生成制御
CASE OSKB030119
SOURCE RACF
SMF 80 生成制御とOSKB030119が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030119を同じ出力で読み、監査整理の生成制御の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030119
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030119 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SMF 80 生成制御 INFORMATION LISTED
IRRD105IとOSKB030119が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SMF 80 生成制御 と OSKB030119 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030119 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0371"><h3>SMF 81 レコード</h3><p class="kb-meta">分類: SMF 80 ・ 難易度: 上級</p><p>SMF 81 レコードは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書追跡のレコードでセキュリティ設定の運用確認を行います。SMF 81 レコードの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で上書追跡のレコードを確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず上書追跡のレコードを正常終了として記録する。</li><li>C. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、上書追跡の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>D. SMF 81 レコードの属性行を読まず上書追跡のレコードの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書追跡のレコードにおいて選択記号 C を採用し、識別名は上書追跡です。上書追跡のレコードにおいて SMF 81 レコード は説明欄の「RACF で SMF 81 レコードの扱いを記録する上書追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のレコードを受け取る担当者は、SMF 81 レコードの表示結果と IRRD105I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のレコードは別カテゴリの確認を流用しており、SMF 81 レコードの根拠にならないため上書追跡ではありません。 B: 上書追跡のレコードは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のレコードは対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のレコードは名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のレコードが示す SMF 81 レコードは出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF 81 レコード</strong></p><p>検証目的: 変更整理のレコードについて、SMF 81 レコードは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030120の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、変更整理のレコードの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSMF 81 レコードを指定し、OSKB030120の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SMF 81 レコード
CASE OSKB030120
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SMF 81 レコード
CASE OSKB030120
SOURCE RACF
SMF 81 レコードとOSKB030120が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030120を同じ出力で読み、変更整理のレコードの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030120
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030120 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SMF 81 レコード INFORMATION LISTED
IRRD105IとOSKB030120が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SMF 81 レコード と OSKB030120 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030120 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0372"><h3>SMF 83 レコード</h3><p class="kb-meta">分類: SMF 80 ・ 難易度: 上級</p><p>SMF 83 レコードは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力追跡のレコードに関する SMF 83 レコードの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず出力追跡のレコードの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力追跡のレコードの証跡として保存して根拠にする。</li><li>C. SMF 83 レコードの変更点を出力本文から切り離して出力追跡のレコードの承認欄のみ残す。</li><li>D. 資料上の説明と画面上の表示行を突き合わせ、出力追跡として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力追跡のレコードにおいて選択記号 D を採用し、識別名は出力追跡です。出力追跡のレコードにおいて SMF 83 レコード は説明欄の「SMF 83 レコードの状態と出力メッセージを結び付ける出力追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡のレコードに関する記録は、SMF 83 レコードの出力行と IRRD105I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡のレコードは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡のレコードは別カテゴリの確認を流用しており、SMF 83 レコードの根拠にならないため出力追跡ではありません。 C: 出力追跡のレコードは名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡のレコードは対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡のレコードで記録する SMF 83 レコードは RACF の確認記録に残す対象名であり、用語名は出力追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF 83 レコード</strong></p><p>検証目的: 構文記録のレコードについて、SMF 83 レコードは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030121の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、構文記録のレコードの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSMF 83 レコードを指定し、OSKB030121の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SMF 83 レコード
CASE OSKB030121
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SMF 83 レコード
CASE OSKB030121
SOURCE RACF
SMF 83 レコードとOSKB030121が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030121を同じ出力で読み、構文記録のレコードの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030121
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030121 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SMF 83 レコード INFORMATION LISTED
IRRD105IとOSKB030121が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SMF 83 レコード と OSKB030121 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030121 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0373"><h3>SMF Type 80 とは</h3><p class="kb-meta">分類: SMF 80 ・ 難易度: 上級</p><p>SMF Type 80 とはは、RACF SETROPTS/RDEFINE/RACDCERTのSMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SMF Type 80 とは</strong></p><p>検証目的: 範囲整理のとはについて、SMF Type 80 とはは、RACF SETROPTS/RDEFINE/RACDCERT の SMF 80で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030111の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、範囲整理のとはの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSMF Type 80 とはを指定し、OSKB030111の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SMF Type 80 とは
CASE OSKB030111
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SMF Type 80 とは
CASE OSKB030111
SOURCE RACF
SMF Type 80 とはとOSKB030111が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030111を同じ出力で読み、範囲整理のとはの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030111
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030111 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SMF Type 80 とは INFORMATION LISTED
IRRD105IとOSKB030111が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SMF Type 80 とは と OSKB030111 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030111 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## z/OS 3.1


<section class="kb-item" id="c26-i0374"><h3>MFA ポリシー拡張</h3><p class="kb-meta">分類: z/OS 3.1 ・ 難易度: 上級</p><p>MFA ポリシー拡張は、MFADEF クラスでの細粒度ポリシー。「MFA ポリシー拡張」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切検査のポリシー拡張で MFA ポリシー拡張の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. MFA ポリシー拡張の出力を取らず区切検査のポリシー拡張の説明文と承認印のみを残す。</li><li>B. 同じ画面で対象行と IRRD105I を読み、区切検査の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して区切検査のポリシー拡張の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切検査のポリシー拡張へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切検査のポリシー拡張において選択記号 B を採用し、識別名は区切検査です。区切検査のポリシー拡張において MFA ポリシー拡張 は説明欄の「区切検査のポリシー拡張に関係する定義値と表示行を照合する区切検査項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は区切検査です。区切検査のポリシー拡張の証跡を読む担当者は、MFA ポリシー拡張の属性行と IRRD105I を合わせて追跡し、背景名は区切検査です。誤答側の問題点を分けます。 A: 区切検査のポリシー拡張は名称や説明のみに寄り、状態を示す出力本文が不足するため区切検査ではありません。 B: 区切検査のポリシー拡張は対象出力と項目説明を結び、根拠を残すので区切検査です。 C: 区切検査のポリシー拡張は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため区切検査ではありません。 D: 区切検査のポリシー拡張は別カテゴリの確認を流用しており、MFA ポリシー拡張の根拠にならないため区切検査ではありません。区切検査のポリシー拡張に出る MFA ポリシー拡張は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は区切検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MFA ポリシー拡張</strong></p><p>検証目的: 呼出分離のポリシー拡張について、MFA ポリシー拡張は、MFADEF クラスでの細粒度ポリシー。「MFA ポリシー拡張」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030143の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、呼出分離のポリシー拡張の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にMFA ポリシー拡張を指定し、OSKB030143の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND MFA ポリシー拡張
CASE OSKB030143
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM MFA ポリシー拡張
CASE OSKB030143
SOURCE RACF
MFA ポリシー拡張とOSKB030143が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030143を同じ出力で読み、呼出分離のポリシー拡張の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030143
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030143 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I MFA ポリシー拡張 INFORMATION LISTED
IRRD105IとOSKB030143が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の MFA ポリシー拡張 と OSKB030143 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030143 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0375"><h3>PASSWORD ALGORITHM デフォルト KDFAES</h3><p class="kb-meta">分類: z/OS 3.1 ・ 難易度: 上級</p><p>PASSWORD ALGORITHM デフォルト KDFAESは、RACF SETROPTS/RDEFINE/RACDCERTのz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力検査のデフォルトに関する PASSWORD ALGORITHM デフォルトの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず出力検査のデフォルトの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力検査のデフォルトの証跡として保存して根拠にする。</li><li>C. PASSWORD ALGORITHM デフォルトの変更点を出力本文から切り離して出力検査のデフォルトの承認欄のみ残す。</li><li>D. 出典欄の説明と運用出力を照合し、出力検査の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力検査のデフォルトにおいて選択記号 D を採用し、識別名は出力検査です。出力検査のデフォルトにおいて PASSWORD ALGORITHM デフォルト は説明欄の「PASSWORD ALGORITHM デフォルトの状態と出力メッセージを結び付ける出力検査項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は出力検査です。出力検査のデフォルトに関する記録は、PASSWORD ALGORITHM デフォルトの出力行と IRRD105I を一緒に保存し、背景名は出力検査です。選択肢ごとの違いを示します。 A: 出力検査のデフォルトは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため出力検査ではありません。 B: 出力検査のデフォルトは別カテゴリの確認を流用しており、PASSWORD ALGORITHM デフォルトの根拠にならないため出力検査ではありません。 C: 出力検査のデフォルトは名称や説明のみに寄り、状態を示す出力本文が不足するため出力検査ではありません。 D: 出力検査のデフォルトは対象出力と項目説明を結び、根拠を残すので出力検査です。出力検査のデフォルトで記録する PASSWORD ALGORITHM デフォルトは RACF の確認記録に残す対象名であり、用語名は出力検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PASSWORD ALGORITHM デフォルト KDFAES</strong></p><p>検証目的: 構文分離のデフォルトについて、PASSWORD ALGORITHM デフォルト KDFAES は、RACF SETROPTS/RDEFINE/RACDCERT のz/OS 3.1で認証、権限、またはセキュリに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030141の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、構文分離のデフォルトの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にPASSWORD ALGORITHMを指定し、OSKB030141の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND PASSWORD ALGORITHM
CASE OSKB030141
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM PASSWORD ALGORITHM
CASE OSKB030141
SOURCE RACF
PASSWORD ALGORITHMとOSKB030141が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030141を同じ出力で読み、構文分離のデフォルトの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030141
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030141 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I PASSWORD ALGORITHM デフォルト INFORMATION LISTED
IRRD105IとOSKB030141が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の PASSWORD ALGORITHM と OSKB030141 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030141 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0376"><h3>RACF 健全性チェック</h3><p class="kb-meta">分類: z/OS 3.1 ・ 難易度: 上級</p><p>RACF 健全性チェックは、RACF SETROPTS/RDEFINE/RACDCERTのz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲検査の健全性チェックでセキュリティ設定の運用確認を行います。RACF 健全性チェックの根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で範囲検査の健全性チェックを確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず範囲検査の健全性チェックを正常終了として記録する。</li><li>C. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、範囲検査の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>D. RACF 健全性チェックの属性行を読まず範囲検査の健全性チェックの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲検査の健全性チェックにおいて選択記号 C を採用し、識別名は範囲検査です。範囲検査の健全性チェックにおいて RACF 健全性チェック は説明欄の「RACF で RACF 健全性チェックの扱いを記録する範囲検査項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は範囲検査です。範囲検査の健全性チェックを受け取る担当者は、RACF 健全性チェックの表示結果と IRRD105I を同じ確認単位として扱い、背景名は範囲検査です。不適切な選択肢を整理します。 A: 範囲検査の健全性チェックは別カテゴリの確認を流用しており、RACF 健全性チェックの根拠にならないため範囲検査ではありません。 B: 範囲検査の健全性チェックは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため範囲検査ではありません。 C: 範囲検査の健全性チェックは対象出力と項目説明を結び、根拠を残すので範囲検査です。 D: 範囲検査の健全性チェックは名称や説明のみに寄り、状態を示す出力本文が不足するため範囲検査ではありません。範囲検査の健全性チェックが示す RACF 健全性チェックは出典欄の資料で使い方を追跡できる項目であり、用語名は範囲検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RACF 健全性チェック</strong></p><p>検証目的: 置換分離の健全性チェックについて、RACF 健全性チェックは、RACF SETROPTS/RDEFINE/RACDCERT のz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030144の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、置換分離の健全性チェックの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRACF 健全性チェックを指定し、OSKB030144の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RACF 健全性チェック
CASE OSKB030144
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RACF 健全性チェック
CASE OSKB030144
SOURCE RACF
RACF 健全性チェックとOSKB030144が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030144を同じ出力で読み、置換分離の健全性チェックの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030144
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030144 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RACF 健全性チェック INFORMATION LISTED
IRRD105IとOSKB030144が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RACF 健全性チェック と OSKB030144 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030144 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0377"><h3>RRSF 拡張</h3><p class="kb-meta">分類: z/OS 3.1 ・ 難易度: 上級</p><p>RRSF 拡張は、RACF SETROPTS/RDEFINE/RACDCERTのz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先検査の拡張に関する RRSF 拡張の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず優先検査の拡張の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先検査の拡張の証跡として保存して根拠にする。</li><li>C. RRSF 拡張の変更点を出力本文から切り離して優先検査の拡張の承認欄のみ残す。</li><li>D. 資料上の説明と画面上の表示行を突き合わせ、優先検査として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先検査の拡張において選択記号 D を採用し、識別名は優先検査です。優先検査の拡張において RRSF 拡張 は説明欄の「RRSF 拡張の状態と出力メッセージを結び付ける優先検査項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は優先検査です。優先検査の拡張に関する記録は、RRSF 拡張の出力行と IRRD105I を一緒に保存し、背景名は優先検査です。選択肢ごとの違いを示します。 A: 優先検査の拡張は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため優先検査ではありません。 B: 優先検査の拡張は別カテゴリの確認を流用しており、RRSF 拡張の根拠にならないため優先検査ではありません。 C: 優先検査の拡張は名称や説明のみに寄り、状態を示す出力本文が不足するため優先検査ではありません。 D: 優先検査の拡張は対象出力と項目説明を結び、根拠を残すので優先検査です。優先検査の拡張で記録する RRSF 拡張は RACF の確認記録に残す対象名であり、用語名は優先検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RRSF 拡張</strong></p><p>検証目的: 終端分離の拡張について、RRSF 拡張は、RACF SETROPTS/RDEFINE/RACDCERT のz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030145の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、終端分離の拡張の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRRSF 拡張を指定し、OSKB030145の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RRSF 拡張
CASE OSKB030145
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RRSF 拡張
CASE OSKB030145
SOURCE RACF
RRSF 拡張とOSKB030145が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030145を同じ出力で読み、終端分離の拡張の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030145
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030145 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RRSF 拡張 INFORMATION LISTED
IRRD105IとOSKB030145が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RRSF 拡張 と OSKB030145 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030145 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0378"><h3>TLS 1.3 用 RACDCERT サポート</h3><p class="kb-meta">分類: z/OS 3.1 ・ 難易度: 上級</p><p>TLS 1.3 用 RACDCERT サポートは、RACF SETROPTS/RDEFINE/RACDCERTのz/OS 3.1で認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件検査の用 サポートに関係する TLS 1 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 属性行、戻り表示、メッセージ見出しを合わせて条件検査の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>B. TLS 1 属性の名称と担当者名のみを残して条件検査の用 サポートの表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で条件検査の用 サポートを確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず条件検査の用 サポートの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件検査の用 サポートにおいて選択記号 A を採用し、識別名は条件検査です。条件検査の用 サポートにおいて TLS 1 属性 は説明欄の「TLS 1 属性の用途をセキュリティ設定の表示で確認する条件検査項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は条件検査です。条件検査の用 サポートに関連して、RACF では TLS 1 属性の表示属性と IRRD105I を同じ証跡に残し、背景名は条件検査です。他の選択肢を確認します。 A: 条件検査の用 サポートは対象出力と項目説明を結び、根拠を残すので条件検査です。 B: 条件検査の用 サポートは名称や説明のみに寄り、状態を示す出力本文が不足するため条件検査ではありません。 C: 条件検査の用 サポートは別カテゴリの確認を流用しており、TLS 1 属性の根拠にならないため条件検査ではありません。 D: 条件検査の用 サポートは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため条件検査ではありません。条件検査の用 サポートで使う TLS 1 属性という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は条件検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TLS 1.3 用 RACDCERT サポート</strong></p><p>検証目的: 展開分離の用 サポートについて、TLS 1.3 用 RACDCERT サポートは、RACF SETROPTS/RDEFINE/RACDCERT のz/OS 3.1で認証、権限、またはセキュリティ設定を確認すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030142の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、展開分離の用 サポートの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にTLS 1.3 用 RACDCERTを指定し、OSKB030142の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND TLS 1.3 用 RACDCERT
CASE OSKB030142
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM TLS 1.3 用 RACDCERT
CASE OSKB030142
SOURCE RACF
TLS 1.3 用 RACDCERTとOSKB030142が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030142を同じ出力で読み、展開分離の用 サポートの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030142
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030142 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I TLS 1.3 用 RACDCERT サポート INFORMATION LISTED
IRRD105IとOSKB030142が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の TLS 1.3 用 RACDCERT と OSKB030142 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030142 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## ユーティリティ


<section class="kb-item" id="c26-i0379"><h3>IRRDBU00</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>IRRDBU00は、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告確認のユーティリティに関係する IRRDBU00 の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 参照資料名、表示行、メッセージをそろえて警告確認の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>B. IRRDBU00 の名称と担当者名のみを残して警告確認のユーティリティの表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で警告確認のユーティリティを確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず警告確認のユーティリティの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告確認のユーティリティにおいて選択記号 A を採用し、識別名は警告確認です。警告確認のユーティリティにおいて IRRDBU00 は説明欄の「IRRDBU00 の用途をセキュリティ設定の表示で確認する警告確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は警告確認です。警告確認のユーティリティに関連して、RACF では IRRDBU00 の表示属性と IRRD105I を同じ証跡に残し、背景名は警告確認です。他の選択肢を確認します。 A: 警告確認のユーティリティは対象出力と項目説明を結び、根拠を残すので警告確認です。 B: 警告確認のユーティリティは名称や説明のみに寄り、状態を示す出力本文が不足するため警告確認ではありません。 C: 警告確認のユーティリティは別カテゴリの確認を流用しており、IRRDBU00 の根拠にならないため警告確認ではありません。 D: 警告確認のユーティリティは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため警告確認ではありません。警告確認のユーティリティで使う IRRDBU00 という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は警告確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRDBU00</strong></p><p>検証目的: 区切判定のユーティリティについて、IRRDBU00 は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030090の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、区切判定のユーティリティの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRDBU00を指定し、OSKB030090の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRDBU00
CASE OSKB030090
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRDBU00
CASE OSKB030090
SOURCE RACF
IRRDBU00とOSKB030090が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030090を同じ出力で読み、区切判定のユーティリティの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030090
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030090 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRDBU00 INFORMATION LISTED
IRRD105IとOSKB030090が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRDBU00 と OSKB030090 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030090 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0380"><h3>IRRDBU00 と DB2 LOAD</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>IRRDBU00 と DB2 LOADは、アンロード結果を Db2 にロードして分析。「IRRDBU00 と DB2 LOAD」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査確認のとでセキュリティ設定の運用確認を行います。IRRDBU00 と DB2 LOAD の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で監査確認のとを確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず監査確認のとを正常終了として記録する。</li><li>C. RACDCERT ID(OSKBUSR) LIST の結果から対象行を抜き出し、監査確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>D. IRRDBU00 と DB2 LOAD の属性行を読まず監査確認のとの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査確認のとにおいて選択記号 C を採用し、識別名は監査確認です。監査確認のとにおいて IRRDBU00 と DB2 LOAD は説明欄の「RACF で IRRDBU00 と DB2 LOAD の扱いを記録する監査確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は監査確認です。監査確認のとを受け取る担当者は、IRRDBU00 と DB2 LOAD の表示結果と IRRD105I を同じ確認単位として扱い、背景名は監査確認です。不適切な選択肢を整理します。 A: 監査確認のとは別カテゴリの確認を流用しており、IRRDBU00 と DB2 LOAD の根拠にならないため監査確認ではありません。 B: 監査確認のとは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため監査確認ではありません。 C: 監査確認のとは対象出力と項目説明を結び、根拠を残すので監査確認です。 D: 監査確認のとは名称や説明のみに寄り、状態を示す出力本文が不足するため監査確認ではありません。監査確認のとが示す IRRDBU00 と DB2 LOAD は出典欄の資料で使い方を追跡できる項目であり、用語名は監査確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRDBU00 と DB2 LOAD</strong></p><p>検証目的: 優先判定のとについて、IRRDBU00 と DB2 LOAD は、アンロード結果を Db2 にロードして分析。「IRRDBU00 と DB2 LOAD」を確認すると、SETROPTS、RDEFINに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030092の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、優先判定のとの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRDBU00 と DB2 LOAを指定し、OSKB030092の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRDBU00 と DB2 LOA
CASE OSKB030092
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRDBU00 と DB2 LOA
CASE OSKB030092
SOURCE RACF
IRRDBU00 と DB2 LOAとOSKB030092が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030092を同じ出力で読み、優先判定のとの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030092
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030092 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRDBU00 と DB2 LOAD INFORMATION LISTED
IRRD105IとOSKB030092が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRDBU00 と DB2 LOA と OSKB030092 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030092 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0381"><h3>IRRDBU00 出力レコード タイプ</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>IRRDBU00 出力レコード タイプは、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRDBU00 出力レコード タイプ</strong></p><p>検証目的: 範囲判定の出力レコード タイプについて、IRRDBU00 出力レコード タイプは、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目ですに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030091の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、範囲判定の出力レコード タイプの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRDBU00 出力レコード タイを指定し、OSKB030091の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRDBU00 出力レコード タイ
CASE OSKB030091
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRDBU00 出力レコード タイ
CASE OSKB030091
SOURCE RACF
IRRDBU00 出力レコード タイとOSKB030091が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030091を同じ出力で読み、範囲判定の出力レコード タイプの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030091
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030091 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRDBU00 出力レコード タイプ INFORMATION LISTED
IRRD105IとOSKB030091が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRDBU00 出力レコード タイ と OSKB030091 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030091 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0382"><h3>IRRRID00</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>IRRRID00は、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更確認のユーティリティに関する IRRRID00 の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. RACDCERT ID(OSKBUSR) LIST の結果を残さず変更確認のユーティリティの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを変更確認のユーティリティの証跡として保存して根拠にする。</li><li>C. IRRRID00 の変更点を出力本文から切り離して変更確認のユーティリティの承認欄のみ残す。</li><li>D. 出典欄の説明と運用出力を照合し、変更確認の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更確認のユーティリティにおいて選択記号 D を採用し、識別名は変更確認です。変更確認のユーティリティにおいて IRRRID00 は説明欄の「IRRRID00 の状態と出力メッセージを結び付ける変更確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は変更確認です。変更確認のユーティリティに関する記録は、IRRRID00 の出力行と IRRD105I を一緒に保存し、背景名は変更確認です。選択肢ごとの違いを示します。 A: 変更確認のユーティリティは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため変更確認ではありません。 B: 変更確認のユーティリティは別カテゴリの確認を流用しており、IRRRID00 の根拠にならないため変更確認ではありません。 C: 変更確認のユーティリティは名称や説明のみに寄り、状態を示す出力本文が不足するため変更確認ではありません。 D: 変更確認のユーティリティは対象出力と項目説明を結び、根拠を残すので変更確認です。変更確認のユーティリティで記録する IRRRID00 は RACF の確認記録に残す対象名であり、用語名は変更確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRRID00</strong></p><p>検証目的: 記録判定のユーティリティについて、IRRRID00 は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030093の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、記録判定のユーティリティの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRRID00を指定し、OSKB030093の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRRID00
CASE OSKB030093
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRRID00
CASE OSKB030093
SOURCE RACF
IRRRID00とOSKB030093が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030093を同じ出力で読み、記録判定のユーティリティの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030093
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030093 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRRID00 INFORMATION LISTED
IRRD105IとOSKB030093が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRRID00 と OSKB030093 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030093 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0383"><h3>IRRRID00 と remove ID</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>IRRRID00 と remove IDは、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文照合のとに関係する IRRRID00 と remove ID の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 属性行、戻り表示、メッセージ見出しを合わせて構文照合の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>B. IRRRID00 と remove ID の名称と担当者名のみを残して構文照合のとの表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で構文照合のとを確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず構文照合のとの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文照合のとにおいて選択記号 A を採用し、識別名は構文照合です。構文照合のとにおいて IRRRID00 と remove ID は説明欄の「IRRRID00 と remove ID の用途をセキュリティ設定の表示で確認する構文照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は構文照合です。構文照合のとに関連して、RACF では IRRRID00 と remove ID の表示属性と IRRD105I を同じ証跡に残し、背景名は構文照合です。他の選択肢を確認します。 A: 構文照合のとは対象出力と項目説明を結び、根拠を残すので構文照合です。 B: 構文照合のとは名称や説明のみに寄り、状態を示す出力本文が不足するため構文照合ではありません。 C: 構文照合のとは別カテゴリの確認を流用しており、IRRRID00 と remove ID の根拠にならないため構文照合ではありません。 D: 構文照合のとは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため構文照合ではありません。構文照合のとで使う IRRRID00 と remove ID という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は構文照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRRID00 と remove ID</strong></p><p>検証目的: 比較判定のとについて、IRRRID00 と remove ID は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030094の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、比較判定のとの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRRID00 と remove を指定し、OSKB030094の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRRID00 と remove 
CASE OSKB030094
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRRID00 と remove 
CASE OSKB030094
SOURCE RACF
IRRRID00 と remove とOSKB030094が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030094を同じ出力で読み、比較判定のとの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030094
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030094 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRRID00 と remove ID INFORMATION LISTED
IRRD105IとOSKB030094が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRRID00 と remove  と OSKB030094 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030094 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0384"><h3>IRRRID00 出力 CLIST</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>IRRRID00 出力 CLISTは、残存参照を削除する RACF コマンド CLIST を生成。「IRRRID00 出力 CLIST」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開照合の出力で IRRRID00 出力 CLIST の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. IRRRID00 出力 CLIST の出力を取らず展開照合の出力の説明文と承認印のみを残す。</li><li>B. 同じ画面で対象行と IRRD105I を読み、展開照合の結果として保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して展開照合の出力の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開照合の出力へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開照合の出力において選択記号 B を採用し、識別名は展開照合です。展開照合の出力において IRRRID00 出力 CLIST は説明欄の「展開照合の出力に関係する定義値と表示行を照合する展開照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は展開照合です。展開照合の出力の証跡を読む担当者は、IRRRID00 出力 CLIST の属性行と IRRD105I を合わせて追跡し、背景名は展開照合です。誤答側の問題点を分けます。 A: 展開照合の出力は名称や説明のみに寄り、状態を示す出力本文が不足するため展開照合ではありません。 B: 展開照合の出力は対象出力と項目説明を結び、根拠を残すので展開照合です。 C: 展開照合の出力は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため展開照合ではありません。 D: 展開照合の出力は別カテゴリの確認を流用しており、IRRRID00 出力 CLIST の根拠にならないため展開照合ではありません。展開照合の出力に出る IRRRID00 出力 CLIST は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は展開照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRRID00 出力 CLIST</strong></p><p>検証目的: 順序判定の出力について、IRRRID00 出力 CLIST は、残存参照を削除する RACF コマンド CLIST を生成。「IRRRID00 出力 CLIST」を確認すると、SETROPTS、RDに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030095の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、順序判定の出力の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRRID00 出力 CLISTを指定し、OSKB030095の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRRID00 出力 CLIST
CASE OSKB030095
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRRID00 出力 CLIST
CASE OSKB030095
SOURCE RACF
IRRRID00 出力 CLISTとOSKB030095が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030095を同じ出力で読み、順序判定の出力の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030095
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030095 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRRID00 出力 CLIST INFORMATION LISTED
IRRD105IとOSKB030095が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRRID00 出力 CLIST と OSKB030095 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030095 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0385"><h3>IRRUT100</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>IRRUT100は、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出照合のユーティリティでセキュリティ設定の運用確認を行います。IRRUT100 の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で呼出照合のユーティリティを確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず呼出照合のユーティリティを正常終了として記録する。</li><li>C. RACDCERT ID(OSKBUSR) LIST で得た表示本文を使い、呼出照合の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>D. IRRUT100 の属性行を読まず呼出照合のユーティリティの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出照合のユーティリティにおいて選択記号 C を採用し、識別名は呼出照合です。呼出照合のユーティリティにおいて IRRUT100 は説明欄の「RACF で IRRUT100 の扱いを記録する呼出照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合のユーティリティを受け取る担当者は、IRRUT100 の表示結果と IRRD105I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合のユーティリティは別カテゴリの確認を流用しており、IRRUT100 の根拠にならないため呼出照合ではありません。 B: 呼出照合のユーティリティは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合のユーティリティは対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合のユーティリティは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合のユーティリティが示す IRRUT100 は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRUT100</strong></p><p>検証目的: 値域判定のユーティリティについて、IRRUT100 は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030096の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、値域判定のユーティリティの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRUT100を指定し、OSKB030096の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRUT100
CASE OSKB030096
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRUT100
CASE OSKB030096
SOURCE RACF
IRRUT100とOSKB030096が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030096を同じ出力で読み、値域判定のユーティリティの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030096
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030096 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRUT100 INFORMATION LISTED
IRRD105IとOSKB030096が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRUT100 と OSKB030096 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030096 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0386"><h3>IRRUT200</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>IRRUT200は、RACF DB のステータス・統計・索引整合性チェック。「IRRUT200」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録確認のユーティリティに関係する IRRUT200 の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 操作結果の本文、対象行、時刻を同じ証跡に入れ、記録確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>B. IRRUT200 の名称と担当者名のみを残して記録確認のユーティリティの表示本文を確認対象に含めない。</li><li>C. セキュリティ設定以外の画面で記録確認のユーティリティを確認し同じ証跡として扱ったことにする。</li><li>D. IRRD105I の有無を見ず記録確認のユーティリティの戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録確認のユーティリティにおいて選択記号 A を採用し、識別名は記録確認です。記録確認のユーティリティにおいて IRRUT200 は説明欄の「IRRUT200 の用途をセキュリティ設定の表示で確認する記録確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は記録確認です。記録確認のユーティリティに関連して、RACF では IRRUT200 の表示属性と IRRD105I を同じ証跡に残し、背景名は記録確認です。他の選択肢を確認します。 A: 記録確認のユーティリティは対象出力と項目説明を結び、根拠を残すので記録確認です。 B: 記録確認のユーティリティは名称や説明のみに寄り、状態を示す出力本文が不足するため記録確認ではありません。 C: 記録確認のユーティリティは別カテゴリの確認を流用しており、IRRUT200 の根拠にならないため記録確認ではありません。 D: 記録確認のユーティリティは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため記録確認ではありません。記録確認のユーティリティで使う IRRUT200 という用語は RACF SETROPTS/RDEFINE/RACDCERT で扱う確認対象であり、用語名は記録確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRUT200</strong></p><p>検証目的: 探索判定のユーティリティについて、IRRUT200 は、RACF DB のステータス・統計・索引整合性チェック。「IRRUT200」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030086の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、探索判定のユーティリティの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRUT200を指定し、OSKB030086の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRUT200
CASE OSKB030086
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRUT200
CASE OSKB030086
SOURCE RACF
IRRUT200とOSKB030086が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030086を同じ出力で読み、探索判定のユーティリティの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030086
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030086 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRUT200 INFORMATION LISTED
IRRD105IとOSKB030086が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRUT200 と OSKB030086 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030086 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0387"><h3>IRRUT200 PARM=INDEX/MAP</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>IRRUT200 PARM=INDEX/MAPは、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文照合保守の構文照合として IRRUT200 を確認するとき、後続担当者へ残すべき証跡はどれですか。</p><ul class="kb-choices"><li>A. 名称と担当者名を保存して表示本文を確認しない。</li><li>B. 構文照合の定義行と出力行を同じ証跡として保存する。 <span class="kb-ok">✅ 正解</span></li><li>C. 別分類の結果を流用して同じ証跡として扱う。</li><li>D. 戻り値と時刻を主な根拠にして表示行を読まない。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正解はBです。構文照合保守で扱う IRRUT200 は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（構文照合保守用語）。構文照合保守の担当者は構文照合として、表示本文とメッセージを照合します（構文照合保守照合）。構文照合保守の対応を残すと、後続担当者は同じ出典に戻って確認できます（構文照合保守出典）。A: 構文照合保守で表示とメッセージを結ぶ場合に根拠になります（構文照合保守A）。B: 構文照合保守で定義と出力の関係がない場合は追跡できません（構文照合保守B）。C: 構文照合保守で出典名のみでは実際の表示を説明できません（構文照合保守C）。D: 構文照合保守で操作記録のみでは値や状態の確認が不足します（構文照合保守D）。構文照合保守の初出用語として IRRUT200 を扱い、分類内の確認名として保存します（構文照合保守終点）。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRUT200 PARM=INDEX ・ MAP</strong></p><p>検証目的: 上書判定の・について、IRRUT200 PARM=INDEX/MAP は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030087の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、上書判定の・の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRUT200 PARM=INDEを指定し、OSKB030087の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRUT200 PARM=INDE
CASE OSKB030087
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRUT200 PARM=INDE
CASE OSKB030087
SOURCE RACF
IRRUT200 PARM=INDEとOSKB030087が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030087を同じ出力で読み、上書判定の・の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030087
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030087 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRUT200 PARM=INDEX ・ MAP INFORMATION LISTED
IRRD105IとOSKB030087が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRUT200 PARM=INDE と OSKB030087 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030087 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0388"><h3>IRRUT400</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>IRRUT400は、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序確認のユーティリティでセキュリティ設定の運用確認を行います。IRRUT400 の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で順序確認のユーティリティを確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず順序確認のユーティリティを正常終了として記録する。</li><li>C. 対象の出力行とメッセージ接頭辞を同時に記録し、順序確認で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>D. IRRUT400 の属性行を読まず順序確認のユーティリティの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序確認のユーティリティにおいて選択記号 C を採用し、識別名は順序確認です。順序確認のユーティリティにおいて IRRUT400 は説明欄の「RACF で IRRUT400 の扱いを記録する順序確認項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は順序確認です。順序確認のユーティリティを受け取る担当者は、IRRUT400 の表示結果と IRRD105I を同じ確認単位として扱い、背景名は順序確認です。不適切な選択肢を整理します。 A: 順序確認のユーティリティは別カテゴリの確認を流用しており、IRRUT400 の根拠にならないため順序確認ではありません。 B: 順序確認のユーティリティは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため順序確認ではありません。 C: 順序確認のユーティリティは対象出力と項目説明を結び、根拠を残すので順序確認です。 D: 順序確認のユーティリティは名称や説明のみに寄り、状態を示す出力本文が不足するため順序確認ではありません。順序確認のユーティリティが示す IRRUT400 は出典欄の資料で使い方を追跡できる項目であり、用語名は順序確認です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRUT400</strong></p><p>検証目的: 出力判定のユーティリティについて、IRRUT400 は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030088の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、出力判定のユーティリティの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRUT400を指定し、OSKB030088の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRUT400
CASE OSKB030088
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRUT400
CASE OSKB030088
SOURCE RACF
IRRUT400とOSKB030088が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030088を同じ出力で読み、出力判定のユーティリティの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030088
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030088 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRUT400 INFORMATION LISTED
IRRD105IとOSKB030088が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRUT400 と OSKB030088 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030088 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0389"><h3>IRRUT400 PARM=ALLOCATE/NOLOCKINPUT</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>IRRUT400 PARM=ALLOCATE/NOLOCKINPUTは、出力 DB 割振/排他制御指定。「IRRUT400 PARM=ALLOCATE/NOLOCKINPUT」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更が認証判定、監査、鍵管理のどこへ影響するかを追いやすい</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開照合権限の展開照合として IRRUT400 を確認するとき、後続担当者へ残すべき証跡はどれですか。</p><ul class="kb-choices"><li>A. 別分類の結果を流用して同じ証跡として扱う。</li><li>B. 戻り値と時刻を主な根拠にして表示行を読まない。</li><li>C. 承認欄の記入を優先して出力メッセージを保存しない。</li><li>D. 展開照合の操作記録とメッセージを対応させて残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正解はDです。展開照合権限で扱う IRRUT400 は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（展開照合権限用語）。展開照合権限の担当者は展開照合として、表示本文とメッセージを照合します（展開照合権限照合）。展開照合権限の対応を残すと、後続担当者は同じ出典に戻って確認できます（展開照合権限出典）。A: 展開照合権限で表示とメッセージを結ぶ場合に根拠になります（展開照合権限A）。B: 展開照合権限で定義と出力の関係がない場合は追跡できません（展開照合権限B）。C: 展開照合権限で出典名のみでは実際の表示を説明できません（展開照合権限C）。D: 展開照合権限で操作記録のみでは値や状態の確認が不足します（展開照合権限D）。展開照合権限の初出用語として IRRUT400 を扱い、分類内の確認名として保存します（展開照合権限終点）。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IRRUT400 PARM=ALLOCATE ・ NOLOCKINPUT</strong></p><p>検証目的: 条件判定の・について、IRRUT400 PARM=ALLOCATE/NOLOCKINPUT は、出力 DB 割振/排他制御指定。「IRRUT400 PARM=ALLOCATE/NOLOCKINPUに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030089の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、条件判定の・の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIRRUT400 PARM=ALLOを指定し、OSKB030089の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IRRUT400 PARM=ALLO
CASE OSKB030089
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IRRUT400 PARM=ALLO
CASE OSKB030089
SOURCE RACF
IRRUT400 PARM=ALLOとOSKB030089が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030089を同じ出力で読み、条件判定の・の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030089
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030089 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IRRUT400 PARM=ALLOCATE ・ N INFORMATION LISTED
IRRD105IとOSKB030089が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IRRUT400 PARM=ALLO と OSKB030089 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030089 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


<section class="kb-item" id="c26-i0390"><h3>RACUT200/RACUT400 JCL</h3><p class="kb-meta">分類: ユーティリティ ・ 難易度: 上級</p><p>RACUT200/RACUT400 JCLは、RACF SETROPTS/RDEFINE/RACDCERTのユーティリティで認証、権限、またはセキュリティ設定を確認する項目です。許可対象、保護対象、監査上の証跡を別々に見て、過剰な権限を残さないようにします。z/OS Security Server RACF Command Language Reference (z/OS 3.1) を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力照合照合の出力照合として RACUT200/RACUT400 を確認するとき、後続担当者へ残すべき証跡はどれですか。</p><ul class="kb-choices"><li>A. 戻り値と時刻を主な根拠にして表示行を読まない。</li><li>B. 承認欄の記入を優先して出力メッセージを保存しない。</li><li>C. 名称と担当者名を保存して表示本文を確認しない。</li><li>D. 出力照合の操作記録とメッセージを対応させて残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 正解はDです。出力照合照合で扱う RACUT200/RACUT400 は RACF SETROPTS/RDEFINE/RACDCERT の確認対象です（出力照合照合用語）。出力照合照合の担当者は出力照合として、表示本文とメッセージを照合します（出力照合照合照合）。出力照合照合の対応を残すと、後続担当者は同じ出典に戻って確認できます（出力照合照合出典）。A: 出力照合照合で表示とメッセージを結ぶ場合に根拠になります（出力照合照合A）。B: 出力照合照合で定義と出力の関係がない場合は追跡できません（出力照合照合B）。C: 出力照合照合で出典名のみでは実際の表示を説明できません（出力照合照合C）。D: 出力照合照合で操作記録のみでは値や状態の確認が不足します（出力照合照合D）。出力照合照合の初出用語として RACUT200/RACUT400 を扱い、分類内の確認名として保存します（出力照合照合終点）。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RACUT200 ・ RACUT400 JCL</strong></p><p>検証目的: 警告判定の・について、RACUT200/RACUT400 JCL は、RACF SETROPTS/RDEFINE/RACDCERT のユーティリティで認証、権限、またはセキュリティ設定を確認する項目に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030097の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、警告判定の・の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にRACUT200 ・ RACUT40を指定し、OSKB030097の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND RACUT200 ・ RACUT40
CASE OSKB030097
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM RACUT200 ・ RACUT40
CASE OSKB030097
SOURCE RACF
RACUT200 ・ RACUT40とOSKB030097が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030097を同じ出力で読み、警告判定の・の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030097
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030097 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I RACUT200 ・ RACUT400 JCL INFORMATION LISTED
IRRD105IとOSKB030097が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の RACUT200 ・ RACUT40 と OSKB030097 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030097 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>


## その他


<section class="kb-item" id="c26-other"><h3>その他（特定項目に紐づかないQA・手順）</h3><p class="kb-meta">項目名が個別の技術項目に一致しなかったQA・手順です。</p><details class="kb-block"><summary>確認問題（3問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開追跡の:で PASSWORD 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. PASSWORD 属性の出力を取らず展開追跡の:の説明文と承認印のみを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、展開追跡として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して展開追跡の:の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開追跡の:へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開追跡の:において選択記号 B を採用し、識別名は展開追跡です。展開追跡の:において PASSWORD 属性 は説明欄の「展開追跡の:に関係する定義値と表示行を照合する展開追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡の:の証跡を読む担当者は、PASSWORD 属性の属性行と IRRD105I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡の:は名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡の:は対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡の:は戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡の:は別カテゴリの確認を流用しており、PASSWORD 属性の根拠にならないため展開追跡ではありません。展開追跡の:に出る PASSWORD 属性は RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は展開追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出追跡のなどでセキュリティ設定の運用確認を行います。PASSWORD 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. RACF と無関係な一覧で呼出追跡のなどを確認した扱いにする。</li><li>B. IRRD105I の有無を確認せず呼出追跡のなどを正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出追跡の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. PASSWORD 属性の属性行を読まず呼出追跡のなどの画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出追跡のなどにおいて選択記号 C を採用し、識別名は呼出追跡です。呼出追跡のなどにおいて PASSWORD 属性 は説明欄の「RACF で PASSWORD 属性の扱いを記録する呼出追跡項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡のなどを受け取る担当者は、PASSWORD 属性の表示結果と IRRD105I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡のなどは別カテゴリの確認を流用しており、PASSWORD 属性の根拠にならないため呼出追跡ではありません。 B: 呼出追跡のなどは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡のなどは対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡のなどは名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡のなどが示す PASSWORD 属性は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div><div class="kb-q"><p><strong>問題.</strong> 復旧照合のとはで SMF Type 80 とはの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SMF Type 80 とはの出力を取らず復旧照合のとはの説明文と承認印のみを残す。</li><li>B. RACF の表示形式に沿って根拠行を採り、復旧照合の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li><li>C. RACDCERT ID(OSKBUSR) LIST を省略して復旧照合のとはの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧照合のとはへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧照合のとはにおいて選択記号 B を採用し、識別名は復旧照合です。復旧照合のとはにおいて SMF Type 80 とは は説明欄の「復旧照合のとはに関係する定義値と表示行を照合する復旧照合項目」と RACDCERT ID(OSKBUSR) LIST または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合のとはの証跡を読む担当者は、SMF Type 80 とはの属性行と IRRD105I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合のとはは名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合のとはは対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合のとはは戻り値や記録番号に寄り、IRRD105I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合のとはは別カテゴリの確認を流用しており、SMF Type 80 とはの根拠にならないため復旧照合ではありません。復旧照合のとはに出る SMF Type 80 とはは RACF SETROPTS/RDEFINE/RACDCERT の運用手順で意味を確認する対象であり、用語名は復旧照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_icha400 / Db2_zOS_RACF_ACM</p></div></details><details class="kb-block"><summary>検証手順（18件）</summary><div class="kb-p"><p class="kb-pname"><strong>PASSWORD(RULE1(LENGTH(m:n)など))</strong></p><p>検証目的: 順序追跡の:について、PASSWORD(RULE1(LENGTH(m:n)など))は、RACF SETROPTS/RDEFINE/RACDCERT の PASSWORD で認証、権限、またはセキュリテに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010055の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、順序追跡の:の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にPASSWORD(RULE1(LENを指定し、OSKB010055の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND PASSWORD(RULE1(LEN
CASE OSKB010055
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM PASSWORD(RULE1(LEN
CASE OSKB010055
SOURCE RACF
PASSWORD(RULE1(LENとOSKB010055が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010055を同じ出力で読み、順序追跡の:の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010055
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010055 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I PASSWORD(RULE1(LENGTH(m: INFORMATION LISTED
IRRD105IとOSKB010055が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の PASSWORD(RULE1(LEN と OSKB010055 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010055 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>PASSWORD(RULE2)など RULE8</strong></p><p>検証目的: 値域追跡のなどについて、PASSWORD(RULE2)など RULE8 は、最大 8 種類のパスワード書式ルールを定義可。「PASSWORD(RULE2)など RULE8」を確認すると、SETROPTSに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010056の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、値域追跡のなどの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にPASSWORD(RULE2)など を指定し、OSKB010056の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND PASSWORD(RULE2)など 
CASE OSKB010056
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM PASSWORD(RULE2)など 
CASE OSKB010056
SOURCE RACF
PASSWORD(RULE2)など とOSKB010056が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010056を同じ出力で読み、値域追跡のなどの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010056
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010056 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I PASSWORD(RULE2)など RULE8 INFORMATION LISTED
IRRD105IとOSKB010056が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の PASSWORD(RULE2)など  と OSKB010056 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010056 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>LOGOPTIONS(SUCCESSES|FAILURES(clas</strong></p><p>検証目的: 優先判定の|について、LOGOPTIONS(SUCCESSES|FAILURES(class))は、成功のみ/失敗のみを記録。「LOGOPTIONS(SUCCESSES|FAILURES(claに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB010092の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、優先判定の|の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にLOGOPTIONS(SUCCESSを指定し、OSKB010092の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND LOGOPTIONS(SUCCESS
CASE OSKB010092
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM LOGOPTIONS(SUCCESS
CASE OSKB010092
SOURCE RACF
LOGOPTIONS(SUCCESSとOSKB010092が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB010092を同じ出力で読み、優先判定の|の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB010092
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB010092 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I LOGOPTIONS(SUCCESSES|FAI INFORMATION LISTED
IRRD105IとOSKB010092が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の LOGOPTIONS(SUCCESS と OSKB010092 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB010092 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>UACC(READ|UPDATE|CONTROL|ALTER|NON</strong></p><p>検証目的: 優先確認の| |について、UACC(READ|UPDATE|CONTROL|ALTER|NONE)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020012の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、優先確認の| |の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にUACC(READ|UPDATE|Cを指定し、OSKB020012の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND UACC(READ|UPDATE|C
CASE OSKB020012
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM UACC(READ|UPDATE|C
CASE OSKB020012
SOURCE RACF
UACC(READ|UPDATE|CとOSKB020012が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020012を同じ出力で読み、優先確認の| |の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020012
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020012 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I UACC(READ|UPDATE|CONTROL INFORMATION LISTED
IRRD105IとOSKB020012が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の UACC(READ|UPDATE|C と OSKB020012 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020012 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>CATEGORY(name1,name2,など)</strong></p><p>検証目的: 終端照合のなどについて、CATEGORY(name1,name2,など)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリティに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020025の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、終端照合のなどの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にCATEGORY(name1,namを指定し、OSKB020025の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND CATEGORY(name1,nam
CASE OSKB020025
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM CATEGORY(name1,nam
CASE OSKB020025
SOURCE RACF
CATEGORY(name1,namとOSKB020025が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020025を同じ出力で読み、終端照合のなどの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020025
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020025 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I CATEGORY(name1,name2,など) INFORMATION LISTED
IRRD105IとOSKB020025が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の CATEGORY(name1,nam と OSKB020025 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020025 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>WHEN(DAYS(など)|TIME(など))</strong></p><p>検証目的: 優先照合のなど | などについて、WHEN(DAYS(など)|TIME(など))は、アクセス可能な曜日/時間帯。「WHEN(DAYS(など)|TIME(など))」を確認すると、SETROPTS、RDEFINに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020032の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、優先照合のなど | などの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にWHEN(DAYS(など)|TIMEを指定し、OSKB020032の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND WHEN(DAYS(など)|TIME
CASE OSKB020032
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM WHEN(DAYS(など)|TIME
CASE OSKB020032
SOURCE RACF
WHEN(DAYS(など)|TIMEとOSKB020032が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020032を同じ出力で読み、優先照合のなど | などの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020032
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020032 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I WHEN(DAYS(など)|TIME(など)) INFORMATION LISTED
IRRD105IとOSKB020032が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の WHEN(DAYS(など)|TIME と OSKB020032 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020032 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>ADDMEM(member1,member2,など)</strong></p><p>検証目的: 記録照合のなについて、ADDMEM(member1,member2,など)は、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE オペランドで認証、権限、またはセキュリに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020033の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、記録照合のなの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にADDMEM(member1,memを指定し、OSKB020033の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND ADDMEM(member1,mem
CASE OSKB020033
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM ADDMEM(member1,mem
CASE OSKB020033
SOURCE RACF
ADDMEM(member1,memとOSKB020033が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020033を同じ出力で読み、記録照合のなの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020033
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020033 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I ADDMEM(member1,member2,な INFORMATION LISTED
IRRD105IとOSKB020033が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の ADDMEM(member1,mem と OSKB020033 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020033 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>JESJOBS SUBMIT.nodeid.jobname.owne</strong></p><p>検証目的: 記録追跡のセキュリティ設定について、JESJOBS SUBMIT.nodeid.jobname.ownerは、ジョブ サブミット権限プロファイル。「JESJOBS SUBMIT.nodeid.jobname.に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020053の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、記録追跡のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にJESJOBS SUBMIT.nodを指定し、OSKB020053の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND JESJOBS SUBMIT.nod
CASE OSKB020053
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM JESJOBS SUBMIT.nod
CASE OSKB020053
SOURCE RACF
JESJOBS SUBMIT.nodとOSKB020053が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020053を同じ出力で読み、記録追跡のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020053
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020053 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I JESJOBS SUBMIT.nodeid.jo INFORMATION LISTED
IRRD105IとOSKB020053が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の JESJOBS SUBMIT.nod と OSKB020053 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020053 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>JESJOBS CANCEL.nodeid.userid.jobna</strong></p><p>検証目的: 比較追跡のセキュリティ設定について、JESJOBS CANCEL.nodeid.userid.jobnameは、RACF SETROPTS/RDEFINE/RACDCERT の RDEFINE JES で認証、権限に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB020054の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、比較追跡のセキュリティ設定の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にJESJOBS CANCEL.nodを指定し、OSKB020054の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND JESJOBS CANCEL.nod
CASE OSKB020054
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM JESJOBS CANCEL.nod
CASE OSKB020054
SOURCE RACF
JESJOBS CANCEL.nodとOSKB020054が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB020054を同じ出力で読み、比較追跡のセキュリティ設定の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB020054
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB020054 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I JESJOBS CANCEL.nodeid.us INFORMATION LISTED
IRRD105IとOSKB020054が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の JESJOBS CANCEL.nod と OSKB020054 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB020054 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>SIGNWITH(SITE LABEL(など))</strong></p><p>検証目的: 区切照合のなどについて、SIGNWITH(SITE LABEL(など))は、RACF SETROPTS/RDEFINE/RACDCERT の RACDCERT GENCERT で認証、権限、またはセキュに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030030の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、区切照合のなどの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSIGNWITH(SITE LABEを指定し、OSKB030030の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SIGNWITH(SITE LABE
CASE OSKB030030
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SIGNWITH(SITE LABE
CASE OSKB030030
SOURCE RACF
SIGNWITH(SITE LABEとOSKB030030が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030030を同じ出力で読み、区切照合のなどの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030030
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030030 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SIGNWITH(SITE LABEL(など)) INFORMATION LISTED
IRRD105IとOSKB030030が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SIGNWITH(SITE LABE と OSKB030030 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>KEYUSAGE(HANDSHAKE|DATAENCRYPT|CER</strong></p><p>検証目的: 範囲照合の|について、KEYUSAGE(HANDSHAKE|DATAENCRYPT|CERTSIGN など)は、RACF SETROPTS/RDEFINE/RACDCERT の RACDCERT GEに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030031の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、範囲照合の|の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にKEYUSAGE(HANDSHAKEを指定し、OSKB030031の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND KEYUSAGE(HANDSHAKE
CASE OSKB030031
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM KEYUSAGE(HANDSHAKE
CASE OSKB030031
SOURCE RACF
KEYUSAGE(HANDSHAKEとOSKB030031が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030031を同じ出力で読み、範囲照合の|の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030031
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030031 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I KEYUSAGE(HANDSHAKE|DATAE INFORMATION LISTED
IRRD105IとOSKB030031が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の KEYUSAGE(HANDSHAKE と OSKB030031 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030031 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>ALTNAME(IP(など)|DOMAIN(など)|EMAIL(など</strong></p><p>検証目的: 優先照合のなど | などについて、ALTNAME(IP(など)|DOMAIN(など)|EMAIL(など)|URI(など))は、サブジェクト代替名 (SAN)。「ALTNAME(IP(など)|DOMAIN(なに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030032の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、優先照合のなど | などの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にALTNAME(IP(など)|DOMを指定し、OSKB030032の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND ALTNAME(IP(など)|DOM
CASE OSKB030032
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM ALTNAME(IP(など)|DOM
CASE OSKB030032
SOURCE RACF
ALTNAME(IP(など)|DOMとOSKB030032が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030032を同じ出力で読み、優先照合のなど | などの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030032
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030032 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I ALTNAME(IP(など)|DOMAIN(など INFORMATION LISTED
IRRD105IとOSKB030032が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の ALTNAME(IP(など)|DOM と OSKB030032 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030032 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>LIST(LABEL(&#x27;など&#x27;))</strong></p><p>検証目的: 比較追跡のなどについて、LIST(LABEL(&#x27;など&#x27;))は、RACF SETROPTS/RDEFINE/RACDCERT の RACDCERT LIST で認証、権限、またはセキュリティ設定を確認するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030054の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、比較追跡のなどの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にLIST(LABEL(&#x27;など&#x27;))を指定し、OSKB030054の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND LIST(LABEL(&#x27;など&#x27;))
CASE OSKB030054
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM LIST(LABEL(&#x27;など&#x27;))
CASE OSKB030054
SOURCE RACF
LIST(LABEL(&#x27;など&#x27;))とOSKB030054が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030054を同じ出力で読み、比較追跡のなどの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030054
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030054 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I LIST(LABEL(&#x27;など&#x27;)) INFORMATION LISTED
IRRD105IとOSKB030054が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の LIST(LABEL(&#x27;など&#x27;)) と OSKB030054 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030054 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>LIST(SERIALNUMBER(など) ISSUERSDN(など</strong></p><p>検証目的: 順序追跡のなどについて、LIST(SERIALNUMBER(など) ISSUERSDN(など))は、RACF SETROPTS/RDEFINE/RACDCERT の RACDCERT LIST で認証、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030055の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、順序追跡のなどの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にLIST(SERIALNUMBER(を指定し、OSKB030055の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND LIST(SERIALNUMBER(
CASE OSKB030055
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM LIST(SERIALNUMBER(
CASE OSKB030055
SOURCE RACF
LIST(SERIALNUMBER(とOSKB030055が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030055を同じ出力で読み、順序追跡のなどの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030055
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030055 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I LIST(SERIALNUMBER(など) IS INFORMATION LISTED
IRRD105IとOSKB030055が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の LIST(SERIALNUMBER( と OSKB030055 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030055 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>SDNFILTER(&#x27;など&#x27;)</strong></p><p>検証目的: 展開検査のなどについて、SDNFILTER(&#x27;など&#x27;)は、Subject DN フィルタ。「SDNFILTER(&#x27;など&#x27;)」を確認すると、SETROPTS、RDEFINE、RACDCERT の変更に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030062の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、展開検査のなどの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にSDNFILTER(&#x27;など&#x27;)を指定し、OSKB030062の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND SDNFILTER(&#x27;など&#x27;)
CASE OSKB030062
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM SDNFILTER(&#x27;など&#x27;)
CASE OSKB030062
SOURCE RACF
SDNFILTER(&#x27;など&#x27;)とOSKB030062が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030062を同じ出力で読み、展開検査のなどの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030062
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030062 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I SDNFILTER(&#x27;など&#x27;) INFORMATION LISTED
IRRD105IとOSKB030062が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の SDNFILTER(&#x27;など&#x27;) と OSKB030062 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030062 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>IDNFILTER(&#x27;など&#x27;)</strong></p><p>検証目的: 呼出検査のなどについて、IDNFILTER(&#x27;など&#x27;)は、RACF SETROPTS/RDEFINE/RACDCERT の RACDCERT MAP で認証、権限、またはセキュリティ設定を確認する項目でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030063の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、呼出検査のなどの確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にIDNFILTER(&#x27;など&#x27;)を指定し、OSKB030063の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND IDNFILTER(&#x27;など&#x27;)
CASE OSKB030063
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM IDNFILTER(&#x27;など&#x27;)
CASE OSKB030063
SOURCE RACF
IDNFILTER(&#x27;など&#x27;)とOSKB030063が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030063を同じ出力で読み、呼出検査のなどの根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030063
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030063 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I IDNFILTER(&#x27;など&#x27;) INFORMATION LISTED
IRRD105IとOSKB030063が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の IDNFILTER(&#x27;など&#x27;) と OSKB030063 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030063 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>DEFAULT ・ PERSONAL ・ CERTAUTH ・ SITE USA</strong></p><p>検証目的: 範囲検査の・ ・について、DEFAULT/PERSONAL/CERTAUTH/SITE USAGE は、Key Ring 内の用途指定。「DEFAULT/PERSONAL/CERTAUTH/SITEに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030071の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、範囲検査の・ ・の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にDEFAULT ・ PERSONALを指定し、OSKB030071の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND DEFAULT ・ PERSONAL
CASE OSKB030071
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM DEFAULT ・ PERSONAL
CASE OSKB030071
SOURCE RACF
DEFAULT ・ PERSONALとOSKB030071が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030071を同じ出力で読み、範囲検査の・ ・の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030071
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030071 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I DEFAULT ・ PERSONAL ・ CERTAUT INFORMATION LISTED
IRRD105IとOSKB030071が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の DEFAULT ・ PERSONAL と OSKB030071 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030071 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div><div class="kb-p"><p class="kb-pname"><strong>LISTUSER など AUDITOR 専用</strong></p><p>検証目的: 復旧検査のなど 専用について、LISTUSER など AUDITOR 専用は、RACF SETROPTS/RDEFINE/RACDCERT の AUDITOR コマンドで状態表示や操作を行うためのコマンド関に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: TSO RACFまたは関連TSO/コンソールを参照でき、OSKB030078の検証用出力を記録できる。</p><p>セッション環境: TSO RACFでRACDCERT ID(OSKBUSR) LISTを実行し、IRRD105Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はTSO RACFのコマンド入力画面です。COMMAND INPUT ===&gt; に RACDCERT ID(OSKBUSR) LIST を入力し、復旧検査のなど 専用の確認表示へ進みます。
［操作（入力）］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
→ Enter を押す
［画面・出力］
(TSO RACF)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
COMMAND INPUTにRACDCERT ID(OSKBUSR) LISTが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はTSO RACFの表示結果です。FIND欄にLISTUSER など AUDITOを指定し、OSKB030078の対象行を見つけます。
［操作（入力）］
(TSO RACF Result)
COMMAND INPUT ===&gt; FIND LISTUSER など AUDITO
CASE OSKB030078
→ Enter を押す
［画面・出力］
(TSO RACF Result)
ITEM LISTUSER など AUDITO
CASE OSKB030078
SOURCE RACF
LISTUSER など AUDITOとOSKB030078が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はTSO RACFの詳細表示です。IRRD105IとOSKB030078を同じ出力で読み、復旧検査のなど 専用の根拠を記録します。
［操作（入力）］
(TSO RACF Detail)
COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST
CASE OSKB030078
→ Enter を押す
［画面・出力］
TSO RACF COMMAND RESPONSE
RACDCERT ID(OSKBUSR) LIST
USER=OSKB030078 OWNER=SYS1 DEFAULT-GROUP=SYS1
IRRD105I LISTUSER など AUDITOR 専用 INFORMATION LISTED
IRRD105IとOSKB030078が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; RACDCERT ID(OSKBUSR) LIST が画面・出力に表示されること
② ステップ2 の LISTUSER など AUDITO と OSKB030078 が画面・出力に表示されること
③ ステップ3 の IRRD105I と OSKB030078 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS Security Server RACF Command Language Reference (z / OS 3.1)</p></div></details></section>
