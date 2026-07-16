---
search:
  exclude: true
---

# DFSMS / IDCAMS / VSAM — 詳細 (1/2)

[← DFSMS / IDCAMS / VSAM の概要へ戻る](index.md)


## ACS_ROUTINES


<section class="kb-item" id="c06-i0001"><h3>ACS TEST 機能</h3><p class="kb-meta">分類: ACS_ROUTINES ・ 難易度: 上級</p><p>ACS TEST 機能は、DFSMS / IDCAMS / VSAMのACS_ROUTINESで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdfp Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧検分の機能で ACS TEST 機能の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. ACS TEST 機能の出力を取らず復旧検分の機能の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、復旧検分の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して復旧検分の機能の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧検分の機能へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧検分正解では選択記号 B を採用し、正解名は復旧検分正解です。復旧検分根拠では ACS TEST 機能 は「復旧検分の機能に関係する定義値と表示行を照合する復旧検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は復旧検分根拠です。復旧検分追跡では ACS TEST 機能の属性行と IDC0001I を合わせ、追跡名は復旧検分追跡です。誤答側の問題点を分けます。 A: 復旧検分不足は名称や説明だけに寄り、判定名は復旧検分不足です。 B: 復旧検分正答は対象出力と項目説明を結び、根拠名は復旧検分正答です。 C: 復旧検分欠落は戻り値や記録番号に寄り、欠落名は復旧検分欠落です。 D: 復旧検分流用は別カテゴリの確認であり、排除名は復旧検分流用です。復旧検分初出では ACS TEST 機能を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧検分初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切照合の機能で ACS TEST 機能の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. ACS TEST 機能の出力を取らず区切照合の機能の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を省略して区切照合の機能の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切照合の機能へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切照合の機能において選択記号 B を採用し、識別名は区切照合です。区切照合の機能において ACS TEST 機能 は説明欄の「区切照合の機能に関係する定義値と表示行を照合する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は区切照合です。区切照合の機能の証跡を読む担当者は、ACS TEST 機能の属性行と IDC0001I を合わせて追跡し、背景名は区切照合です。誤答側の問題点を分けます。 A: 区切照合の機能は名称や説明のみに寄り、状態を示す出力本文が不足するため区切照合ではありません。 B: 区切照合の機能は対象出力と項目説明を結び、根拠を残すので区切照合です。 C: 区切照合の機能は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため区切照合ではありません。 D: 区切照合の機能は別カテゴリの確認を流用しており、ACS TEST 機能の根拠にならないため区切照合ではありません。区切照合の機能に出る ACS TEST 機能は DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は区切照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ACS TEST 機能</strong></p><p>検証目的: 記録検査の機能について、ACS TEST 機能は、DFSMS / IDCAMS / VSAM の ACS_ROUTINES で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020073の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、記録検査の機能の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にACS TEST 機能を指定し、OSKB020073の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ACS TEST 機能
CASE OSKB020073
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ACS TEST 機能
CASE OSKB020073
SOURCE DFSMS
ACS TEST 機能とOSKB020073が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020073を同じ出力で読み、記録検査の機能の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020073
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020073.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020073が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ACS TEST 機能 と OSKB020073 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020073 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdfp Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0002"><h3>ACS ルーチン概要</h3><p class="kb-meta">分類: ACS_ROUTINES ・ 難易度: 上級</p><p>ACS ルーチン概要は、DFSMS / IDCAMS / VSAMのACS_ROUTINESで機能名、見出し、または確認対象として参照する項目です。Automatic Class Selection ルーチン。割り振り要求時に DC/SC/MC/SG を順に決定する SMS 言語のスクリプト</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdfp Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲検分のルーチン概要でストレージ管理の運用確認を行います。ACS ルーチン概要の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で範囲検分のルーチン概要を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず範囲検分のルーチン概要を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて範囲検分の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. ACS ルーチン概要の属性行を読まず範囲検分のルーチン概要の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲検分正解では選択記号 C を採用し、正解名は範囲検分正解です。範囲検分根拠では ACS ルーチン概要 は「DFSMS で ACS ルーチン概要の扱いを記録する範囲検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は範囲検分根拠です。範囲検分受渡では ACS ルーチン概要の表示結果と IDC0001I を同じ確認単位にし、受渡名は範囲検分受渡です。不適切な選択肢を整理します。 A: 範囲検分流用は別カテゴリの確認であり、排除名は範囲検分流用です。 B: 範囲検分欠落は戻り値や記録番号に寄り、欠落名は範囲検分欠落です。 C: 範囲検分正答は対象出力と項目説明を結び、根拠名は範囲検分正答です。 D: 範囲検分不足は名称や説明だけに寄り、判定名は範囲検分不足です。範囲検分資料では ACS ルーチン概要の使い方を出典欄から追跡し、資料名は範囲検分資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出照合のルーチン概要でストレージ管理の運用確認を行います。ACS ルーチン概要の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で呼出照合のルーチン概要を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず呼出照合のルーチン概要を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. ACS ルーチン概要の属性行を読まず呼出照合のルーチン概要の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出照合のルーチン概要において選択記号 C を採用し、識別名は呼出照合です。呼出照合のルーチン概要において ACS ルーチン概要 は説明欄の「DFSMS で ACS ルーチン概要の扱いを記録する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は呼出照合です。呼出照合のルーチン概要を受け取る担当者は、ACS ルーチン概要の表示結果と IDC0001I を同じ確認単位として扱い、背景名は呼出照合です。不適切な選択肢を整理します。 A: 呼出照合のルーチン概要は別カテゴリの確認を流用しており、ACS ルーチン概要の根拠にならないため呼出照合ではありません。 B: 呼出照合のルーチン概要は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため呼出照合ではありません。 C: 呼出照合のルーチン概要は対象出力と項目説明を結び、根拠を残すので呼出照合です。 D: 呼出照合のルーチン概要は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出照合ではありません。呼出照合のルーチン概要が示す ACS ルーチン概要は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>ACS ルーチン概要</strong></p><p>検証目的: 監査照合のルーチン概要について、ACS ルーチン概要は、DFSMS / IDCAMS / VSAM の ACS_ROUTINES で機能名、見出し、または確認対象として参照する項目です。Automatic Clに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030039の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、監査照合のルーチン概要の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にACS ルーチン概要を指定し、OSKB030039の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ACS ルーチン概要
CASE OSKB030039
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ACS ルーチン概要
CASE OSKB030039
SOURCE DFSMS
ACS ルーチン概要とOSKB030039が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030039を同じ出力で読み、監査照合のルーチン概要の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030039
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030039.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030039が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ACS ルーチン概要 と OSKB030039 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030039 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdfp Storage Administration</p></div><div class="kb-p"><p class="kb-pname"><strong>ACS ルーチン概要</strong></p><p>検証目的: 探索検査のルーチン概要について、ACS ルーチン概要は、DFSMS / IDCAMS / VSAM の ACS_ROUTINES で機能名、見出し、または確認対象として参照する項目です。Automatic Clに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020066の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、探索検査のルーチン概要の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にACS ルーチン概要を指定し、OSKB020066の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ACS ルーチン概要
CASE OSKB020066
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ACS ルーチン概要
CASE OSKB020066
SOURCE DFSMS
ACS ルーチン概要とOSKB020066が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020066を同じ出力で読み、探索検査のルーチン概要の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020066
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020066.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020066が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ACS ルーチン概要 と OSKB020066 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020066 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdfp Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0003"><h3>ACS 変数 (&amp;DSN, &amp;USER, &amp;APPLIC など)</h3><p class="kb-meta">分類: ACS_ROUTINES ・ 難易度: 上級</p><p>ACS 変数 (&amp;DSN, &amp;USER, &amp;APPLIC など)は、DFSMS / IDCAMS / VSAMのACS_ROUTINESで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdfp Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告検分の変数に関係する ACS 変数 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告検分で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. ACS 変数 属性の名称と担当者名だけを残して警告検分の変数の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で警告検分の変数を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず警告検分の変数の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告検分正解では選択記号 A を採用し、正解名は警告検分正解です。警告検分根拠では ACS 変数 属性 は「ACS 変数 属性の用途をストレージ管理の表示で確認する警告検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は警告検分根拠です。警告検分背景では DFSMS の ACS 変数 属性と IDC0001I を同じ証跡に残し、背景名は警告検分背景です。他の選択肢を確認します。 A: 警告検分正答は対象出力と項目説明を結び、根拠名は警告検分正答です。 B: 警告検分不足は名称や説明だけに寄り、判定名は警告検分不足です。 C: 警告検分流用は別カテゴリの確認であり、排除名は警告検分流用です。 D: 警告検分欠落は戻り値や記録番号に寄り、欠落名は警告検分欠落です。警告検分用語では ACS 変数 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告検分用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件照合の変数に関係する ACS 変数 (&amp;DSN, &amp;USER, &amp;AP の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. ACS 変数 (&amp;DSN, &amp;USER, &amp;AP の名称と担当者名のみを残して条件照合の変数の表示本文を確認対象に含めない。</li><li>C. ストレージ管理以外の画面で条件照合の変数を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず条件照合の変数の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件照合の変数において選択記号 A を採用し、識別名は条件照合です。条件照合の変数において ACS 変数 (&amp;DSN, &amp;USER, &amp;AP は説明欄の「ACS 変数 (&amp;DSN, &amp;USER, &amp;AP の用途をストレージ管理の表示で確認する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は条件照合です。条件照合の変数に関連して、DFSMS では ACS 変数 (&amp;DSN, &amp;USER, &amp;AP の表示属性と IDC0001I を同じ証跡に残し、背景名は条件照合です。他の選択肢を確認します。 A: 条件照合の変数は対象出力と項目説明を結び、根拠を残すので条件照合です。 B: 条件照合の変数は名称や説明のみに寄り、状態を示す出力本文が不足するため条件照合ではありません。 C: 条件照合の変数は別カテゴリの確認を流用しており、ACS 変数 (&amp;DSN, &amp;USER, &amp;AP の根拠にならないため条件照合ではありません。 D: 条件照合の変数は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため条件照合ではありません。条件照合の変数で使う ACS 変数 (&amp;DSN, &amp;USER, &amp;AP という用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は条件照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ACS 変数 (&amp;DSN, &amp;USER, &amp;APPLIC など)</strong></p><p>検証目的: 優先検査の変数について、ACS 変数 (&amp;DSN, &amp;USER, &amp;APPLIC など)は、DFSMS / IDCAMS / VSAM の ACS_ROUTINES で機能名、見出し、または確認対象としに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020072の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、優先検査の変数の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にACS 変数 (&amp;DSN, &amp;USEを指定し、OSKB020072の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ACS 変数 (&amp;DSN, &amp;USE
CASE OSKB020072
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ACS 変数 (&amp;DSN, &amp;USE
CASE OSKB020072
SOURCE DFSMS
ACS 変数 (&amp;DSN, &amp;USEとOSKB020072が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020072を同じ出力で読み、優先検査の変数の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020072
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020072.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020072が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ACS 変数 (&amp;DSN, &amp;USE と OSKB020072 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020072 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdfp Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0004"><h3>DATACLAS ACS</h3><p class="kb-meta">分類: ACS_ROUTINES ・ 難易度: 上級</p><p>DATACLAS ACSは、DFSMS / IDCAMS / VSAMのACS_ROUTINESで確認する項目です。&amp;DSN, &amp;HLQ, &amp;RECORG, &amp;DSORG 等の変数に基づきデータクラスを決定。明示指定なしの場合の DC 自動付与</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdfp Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先検分のストレージ管理に関する DATACLAS ACS の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず優先検分のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先検分のストレージ管理の証跡として保存して根拠にする。</li><li>C. DATACLAS ACS の変更点を出力本文から切り離して優先検分のストレージ管理の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC0001I を読み、優先検分の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先検分正解では選択記号 D を採用し、正解名は優先検分正解です。優先検分根拠では DATACLAS ACS は「DATACLAS ACS の状態と出力メッセージを結び付ける優先検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は優先検分根拠です。優先検分保存では DATACLAS ACS の出力行と IDC0001I を一緒に残し、保存名は優先検分保存です。選択肢ごとの違いを示します。 A: 優先検分欠落は戻り値や記録番号に寄り、欠落名は優先検分欠落です。 B: 優先検分流用は別カテゴリの確認であり、排除名は優先検分流用です。 C: 優先検分不足は名称や説明だけに寄り、判定名は優先検分不足です。 D: 優先検分正答は対象出力と項目説明を結び、根拠名は優先検分正答です。優先検分対象では DATACLAS ACS を DFSMS の確認記録に残し、対象名は優先検分対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換照合のストレージ管理に関する DATACLAS ACS の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL の結果を残さず置換照合のストレージ管理の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換照合のストレージ管理の証跡として保存して根拠にする。</li><li>C. DATACLAS ACS の変更点を出力本文から切り離して置換照合のストレージ管理の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換照合のストレージ管理において選択記号 D を採用し、識別名は置換照合です。置換照合のストレージ管理において DATACLAS ACS は説明欄の「DATACLAS ACS の状態と出力メッセージを結び付ける項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は置換照合です。置換照合のストレージ管理に関する記録は、DATACLAS ACS の出力行と IDC0001I を一緒に保存し、背景名は置換照合です。選択肢ごとの違いを示します。 A: 置換照合のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため置換照合ではありません。 B: 置換照合のストレージ管理は別カテゴリの確認を流用しており、DATACLAS ACS の根拠にならないため置換照合ではありません。 C: 置換照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため置換照合ではありません。 D: 置換照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので置換照合です。置換照合のストレージ管理で記録する DATACLAS ACS は DFSMS の確認記録に残す対象名であり、用語名は置換照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DATACLAS ACS</strong></p><p>検証目的: 上書検査のストレージ管理について、DATACLAS ACS は、DFSMS / IDCAMS / VSAM の ACS_ROUTINES で確認する項目です。&amp;DSN, &amp;HLQ, &amp;RECORG, &amp;DSORGに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020067の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、上書検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDATACLAS ACSを指定し、OSKB020067の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DATACLAS ACS
CASE OSKB020067
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DATACLAS ACS
CASE OSKB020067
SOURCE DFSMS
DATACLAS ACSとOSKB020067が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020067を同じ出力で読み、上書検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020067
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020067.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020067が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の DATACLAS ACS と OSKB020067 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020067 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdfp Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0005"><h3>FILTLIST</h3><p class="kb-meta">分類: ACS_ROUTINES ・ 難易度: 上級</p><p>FILTLISTは、DFSMS / IDCAMS / VSAMのACS_ROUTINESで機能名、見出し、または確認対象として参照する項目です。ACS の前置フィルタリスト宣言。HLQ や DSN パターンの集合を変数化し、ルール群を読みやすくする。「FILTLIST」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdfp Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域検分のストレージ管理に関する FILTLIST の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず値域検分のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域検分のストレージ管理の証跡として保存して根拠にする。</li><li>C. FILTLIST の変更点を出力本文から切り離して値域検分のストレージ管理の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、値域検分の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域検分正解では選択記号 D を採用し、正解名は値域検分正解です。値域検分根拠では FILTLIST は「FILTLIST の状態と出力メッセージを結び付ける値域検分項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は値域検分根拠です。値域検分保存では FILTLIST の出力行と IDC3009I を一緒に残し、保存名は値域検分保存です。選択肢ごとの違いを示します。 A: 値域検分欠落は戻り値や記録番号に寄り、欠落名は値域検分欠落です。 B: 値域検分流用は別カテゴリの確認であり、排除名は値域検分流用です。 C: 値域検分不足は名称や説明だけに寄り、判定名は値域検分不足です。 D: 値域検分正答は対象出力と項目説明を結び、根拠名は値域検分正答です。値域検分対象では FILTLIST を DFSMS の確認記録に残し、対象名は値域検分対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力照合のストレージ管理に関する FILTLIST の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))の結果を残さず出力照合のストレージ管理の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力照合のストレージ管理の証跡として保存して根拠にする。</li><li>C. FILTLIST の変更点を出力本文から切り離して出力照合のストレージ管理の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力照合のストレージ管理において選択記号 D を採用し、識別名は出力照合です。出力照合のストレージ管理において FILTLIST は説明欄の「FILTLIST の状態と出力メッセージを結び付ける項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は出力照合です。出力照合のストレージ管理に関する記録は、FILTLIST の出力行と IDC3009I を一緒に保存し、背景名は出力照合です。選択肢ごとの違いを示します。 A: 出力照合のストレージ管理は戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため出力照合ではありません。 B: 出力照合のストレージ管理は別カテゴリの確認を流用しており、FILTLIST の根拠にならないため出力照合ではありません。 C: 出力照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため出力照合ではありません。 D: 出力照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので出力照合です。出力照合のストレージ管理で記録する FILTLIST は DFSMS の確認記録に残す対象名であり、用語名は出力照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>FILTLIST</strong></p><p>検証目的: 変更照合のストレージ管理について、FILTLIST は、DFSMS / IDCAMS / VSAM の ACS_ROUTINES で機能名、見出し、または確認対象として参照する項目です。ACS の前置フィルタリストに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030040の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、変更照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にFILTLISTを指定し、OSKB030040の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND FILTLIST
CASE OSKB030040
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM FILTLIST
CASE OSKB030040
SOURCE DFSMS
FILTLISTとOSKB030040が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030040を同じ出力で読み、変更照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030040
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030040.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030040が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の FILTLIST と OSKB030040 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030040 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdfp Storage Administration</p></div><div class="kb-p"><p class="kb-pname"><strong>FILTLIST</strong></p><p>検証目的: 範囲検査のストレージ管理について、FILTLIST は、DFSMS / IDCAMS / VSAM の ACS_ROUTINES で機能名、見出し、または確認対象として参照する項目です。ACS の前置フィルタリストに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020071の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、範囲検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にFILTLISTを指定し、OSKB020071の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND FILTLIST
CASE OSKB020071
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM FILTLIST
CASE OSKB020071
SOURCE DFSMS
FILTLISTとOSKB020071が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020071を同じ出力で読み、範囲検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020071
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020071.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020071が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の FILTLIST と OSKB020071 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020071 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdfp Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0006"><h3>MGMTCLAS ACS</h3><p class="kb-meta">分類: ACS_ROUTINES ・ 難易度: 上級</p><p>MGMTCLAS ACSは、DFSMS / IDCAMS / VSAMのACS_ROUTINESで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdfp Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較検分のストレージ管理で MGMTCLAS ACS の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. MGMTCLAS ACS の出力を取らず比較検分のストレージ管理の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、比較検分として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して比較検分のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較検分のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較検分正解では選択記号 B を採用し、正解名は比較検分正解です。比較検分根拠では MGMTCLAS ACS は「比較検分のストレージ管理に関係する定義値と表示行を照合する比較検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は比較検分根拠です。比較検分追跡では MGMTCLAS ACS の属性行と IDC0001I を合わせ、追跡名は比較検分追跡です。誤答側の問題点を分けます。 A: 比較検分不足は名称や説明だけに寄り、判定名は比較検分不足です。 B: 比較検分正答は対象出力と項目説明を結び、根拠名は比較検分正答です。 C: 比較検分欠落は戻り値や記録番号に寄り、欠落名は比較検分欠落です。 D: 比較検分流用は別カテゴリの確認であり、排除名は比較検分流用です。比較検分初出では MGMTCLAS ACS を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較検分初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索照合のストレージ管理で MGMTCLAS ACS の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. MGMTCLAS ACS の出力を取らず探索照合のストレージ管理の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を省略して探索照合のストレージ管理の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索照合のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索照合のストレージ管理において選択記号 B を採用し、識別名は探索照合です。探索照合のストレージ管理において MGMTCLAS ACS は説明欄の「探索照合のストレージ管理に関係する定義値と表示行を照合する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は探索照合です。探索照合のストレージ管理の証跡を読む担当者は、MGMTCLAS ACS の属性行と IDC0001I を合わせて追跡し、背景名は探索照合です。誤答側の問題点を分けます。 A: 探索照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため探索照合ではありません。 B: 探索照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので探索照合です。 C: 探索照合のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため探索照合ではありません。 D: 探索照合のストレージ管理は別カテゴリの確認を流用しており、MGMTCLAS ACS の根拠にならないため探索照合ではありません。探索照合のストレージ管理に出る MGMTCLAS ACS は DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は探索照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MGMTCLAS ACS</strong></p><p>検証目的: 条件検査のストレージ管理について、MGMTCLAS ACS は、DFSMS / IDCAMS / VSAM の ACS_ROUTINES で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020069の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、条件検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にMGMTCLAS ACSを指定し、OSKB020069の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND MGMTCLAS ACS
CASE OSKB020069
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM MGMTCLAS ACS
CASE OSKB020069
SOURCE DFSMS
MGMTCLAS ACSとOSKB020069が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020069を同じ出力で読み、条件検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020069
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020069.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020069が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の MGMTCLAS ACS と OSKB020069 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020069 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdfp Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0007"><h3>STORCLAS ACS</h3><p class="kb-meta">分類: ACS_ROUTINES ・ 難易度: 上級</p><p>STORCLAS ACSは、DFSMS / IDCAMS / VSAMのACS_ROUTINESで機能名、見出し、または確認対象として参照する項目です。DC 決定後にストレージクラスを決定。性能/可用性要件と HLQ/アプリ別ルールを表現。「STORCLAS ACS」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdfp Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録検分のストレージ管理に関係する STORCLAS ACS の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、記録検分の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. STORCLAS ACS の名称と担当者名だけを残して記録検分のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で記録検分のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず記録検分のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録検分正解では選択記号 A を採用し、正解名は記録検分正解です。記録検分根拠では STORCLAS ACS は「STORCLAS ACS の用途をストレージ管理の表示で確認する記録検分項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は記録検分根拠です。記録検分背景では DFSMS の STORCLAS ACS と IDC3009I を同じ証跡に残し、背景名は記録検分背景です。他の選択肢を確認します。 A: 記録検分正答は対象出力と項目説明を結び、根拠名は記録検分正答です。 B: 記録検分不足は名称や説明だけに寄り、判定名は記録検分不足です。 C: 記録検分流用は別カテゴリの確認であり、排除名は記録検分流用です。 D: 記録検分欠落は戻り値や記録番号に寄り、欠落名は記録検分欠落です。記録検分用語では STORCLAS ACS を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録検分用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端照合のストレージ管理に関係する STORCLAS ACS の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. STORCLAS ACS の名称と担当者名のみを残して終端照合のストレージ管理の表示本文を確認対象に含めない。</li><li>C. ストレージ管理以外の画面で終端照合のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず終端照合のストレージ管理の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端照合のストレージ管理において選択記号 A を採用し、識別名は終端照合です。終端照合のストレージ管理において STORCLAS ACS は説明欄の「STORCLAS ACS の用途をストレージ管理の表示で確認する項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は終端照合です。終端照合のストレージ管理に関連して、DFSMS では STORCLAS ACS の表示属性と IDC3009I を同じ証跡に残し、背景名は終端照合です。他の選択肢を確認します。 A: 終端照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので終端照合です。 B: 終端照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため終端照合ではありません。 C: 終端照合のストレージ管理は別カテゴリの確認を流用しており、STORCLAS ACS の根拠にならないため終端照合ではありません。 D: 終端照合のストレージ管理は戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため終端照合ではありません。終端照合のストレージ管理で使う STORCLAS ACS という用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は終端照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STORCLAS ACS</strong></p><p>検証目的: 出力検査のストレージ管理について、STORCLAS ACS は、DFSMS / IDCAMS / VSAM の ACS_ROUTINES で機能名、見出し、または確認対象として参照する項目です。DC 決定後にストレに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020068の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、出力検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSTORCLAS ACSを指定し、OSKB020068の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND STORCLAS ACS
CASE OSKB020068
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM STORCLAS ACS
CASE OSKB020068
SOURCE DFSMS
STORCLAS ACSとOSKB020068が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020068を同じ出力で読み、出力検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020068
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020068.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020068が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の STORCLAS ACS と OSKB020068 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020068 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdfp Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0008"><h3>STORGRP ACS</h3><p class="kb-meta">分類: ACS_ROUTINES ・ 難易度: 上級</p><p>STORGRP ACSは、DFSMS / IDCAMS / VSAMのACS_ROUTINESで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdfp Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序検分のストレージ管理でストレージ管理の運用確認を行います。STORGRP ACS の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で順序検分のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず順序検分のストレージ管理を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序検分の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. STORGRP ACS の属性行を読まず順序検分のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序検分正解では選択記号 C を採用し、正解名は順序検分正解です。順序検分根拠では STORGRP ACS は「DFSMS で STORGRP ACS の扱いを記録する順序検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は順序検分根拠です。順序検分受渡では STORGRP ACS の表示結果と IDC0001I を同じ確認単位にし、受渡名は順序検分受渡です。不適切な選択肢を整理します。 A: 順序検分流用は別カテゴリの確認であり、排除名は順序検分流用です。 B: 順序検分欠落は戻り値や記録番号に寄り、欠落名は順序検分欠落です。 C: 順序検分正答は対象出力と項目説明を結び、根拠名は順序検分正答です。 D: 順序検分不足は名称や説明だけに寄り、判定名は順序検分不足です。順序検分資料では STORGRP ACS の使い方を出典欄から追跡し、資料名は順序検分資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書照合のストレージ管理でストレージ管理の運用確認を行います。STORGRP ACS の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で上書照合のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず上書照合のストレージ管理を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. STORGRP ACS の属性行を読まず上書照合のストレージ管理の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書照合のストレージ管理において選択記号 C を採用し、識別名は上書照合です。上書照合のストレージ管理において STORGRP ACS は説明欄の「DFSMS で STORGRP ACS の扱いを記録する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は上書照合です。上書照合のストレージ管理を受け取る担当者は、STORGRP ACS の表示結果と IDC0001I を同じ確認単位として扱い、背景名は上書照合です。不適切な選択肢を整理します。 A: 上書照合のストレージ管理は別カテゴリの確認を流用しており、STORGRP ACS の根拠にならないため上書照合ではありません。 B: 上書照合のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため上書照合ではありません。 C: 上書照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので上書照合です。 D: 上書照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため上書照合ではありません。上書照合のストレージ管理が示す STORGRP ACS は出典欄の資料で使い方を追跡できる項目であり、用語名は上書照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STORGRP ACS</strong></p><p>検証目的: 区切検査のストレージ管理について、STORGRP ACS は、DFSMS / IDCAMS / VSAM の ACS_ROUTINES で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020070の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、区切検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSTORGRP ACSを指定し、OSKB020070の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND STORGRP ACS
CASE OSKB020070
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM STORGRP ACS
CASE OSKB020070
SOURCE DFSMS
STORGRP ACSとOSKB020070が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020070を同じ出力で読み、区切検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020070
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020070.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020070が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の STORGRP ACS と OSKB020070 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020070 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdfp Storage Administration</p></div></details></section>


## ALTER


<section class="kb-item" id="c06-i0009"><h3>ADDVOLUMES / REMOVEVOLUMES</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>ADDVOLUMES / REMOVEVOLUMESは、DFSMS / IDCAMS / VSAMのALTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲検査の・でストレージ管理の運用確認を行います。ADDVOLUMES 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で範囲検査の・を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず範囲検査の・を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて範囲検査の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. ADDVOLUMES 属性の属性行を読まず範囲検査の・の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲検査正解では選択記号 C を採用し、正解名は範囲検査正解です。範囲検査根拠では ADDVOLUMES 属性 は「DFSMS で ADDVOLUMES 属性の扱いを記録する範囲検査項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は範囲検査根拠です。範囲検査受渡では ADDVOLUMES 属性の表示結果と IDC0001I を同じ確認単位にし、受渡名は範囲検査受渡です。不適切な選択肢を整理します。 A: 範囲検査流用は別カテゴリの確認であり、排除名は範囲検査流用です。 B: 範囲検査欠落は戻り値や記録番号に寄り、欠落名は範囲検査欠落です。 C: 範囲検査正答は対象出力と項目説明を結び、根拠名は範囲検査正答です。 D: 範囲検査不足は名称や説明だけに寄り、判定名は範囲検査不足です。範囲検査資料では ADDVOLUMES 属性の使い方を出典欄から追跡し、資料名は範囲検査資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>ADDVOLUMES ・ REMOVEVOLUMES</strong></p><p>検証目的: 順序確認の・について、ADDVOLUMES / REMOVEVOLUMES は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030015の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、順序確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にADDVOLUMES ・ REMOVを指定し、OSKB030015の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ADDVOLUMES ・ REMOV
CASE OSKB030015
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ADDVOLUMES ・ REMOV
CASE OSKB030015
SOURCE DFSMS
ADDVOLUMES ・ REMOVとOSKB030015が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030015を同じ出力で読み、順序確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030015
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030015.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030015が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ADDVOLUMES ・ REMOV と OSKB030015 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030015 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>ADDVOLUMES ・ REMOVEVOLUMES</strong></p><p>検証目的: 探索検査の・について、ADDVOLUMES / REMOVEVOLUMES は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010066の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、探索検査の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にADDVOLUMES ・ REMOVを指定し、OSKB010066の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ADDVOLUMES ・ REMOV
CASE OSKB010066
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ADDVOLUMES ・ REMOV
CASE OSKB010066
SOURCE DFSMS
ADDVOLUMES ・ REMOVとOSKB010066が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010066を同じ出力で読み、探索検査の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010066
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010066.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010066が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ADDVOLUMES ・ REMOV と OSKB010066 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010066 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0010"><h3>ALTER NULLIFY</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>ALTER NULLIFYは、DFSMS / IDCAMS / VSAMのALTERで機能名、見出し、または確認対象として参照する項目です。属性値を NULL に戻す (OWNER, EXCEPTIONEXIT 等)。ATTEMPTS/AUTHORIZATION/CODE 等の旧属性除去に有効</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査検査のストレージ管理でストレージ管理の運用確認を行います。ALTER NULLIFY の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で監査検査のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず監査検査のストレージ管理を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて監査検査の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. ALTER NULLIFY の属性行を読まず監査検査のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査検査正解では選択記号 C を採用し、正解名は監査検査正解です。監査検査根拠では ALTER NULLIFY は「DFSMS で ALTER NULLIFY の扱いを記録する監査検査項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は監査検査根拠です。監査検査受渡では ALTER NULLIFY の表示結果と IDC0001I を同じ確認単位にし、受渡名は監査検査受渡です。不適切な選択肢を整理します。 A: 監査検査流用は別カテゴリの確認であり、排除名は監査検査流用です。 B: 監査検査欠落は戻り値や記録番号に寄り、欠落名は監査検査欠落です。 C: 監査検査正答は対象出力と項目説明を結び、根拠名は監査検査正答です。 D: 監査検査不足は名称や説明だけに寄り、判定名は監査検査不足です。監査検査資料では ALTER NULLIFY の使い方を出典欄から追跡し、資料名は監査検査資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ALTER NULLIFY</strong></p><p>検証目的: 比較検査のストレージ管理について、ALTER NULLIFY は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。属性値を NULL に戻す (Oに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010074の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、比較検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にALTER NULLIFYを指定し、OSKB010074の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ALTER NULLIFY
CASE OSKB010074
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ALTER NULLIFY
CASE OSKB010074
SOURCE DFSMS
ALTER NULLIFYとOSKB010074が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010074を同じ出力で読み、比較検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010074
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010074.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010074が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ALTER NULLIFY と OSKB010074 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010074 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0011"><h3>ALTER 基本</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>既存カタログエントリの属性を変更する IDCAMS コマンド。サイズ系は ALTER 不可で、再定義 + REPRO が必要なケースに注意</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件検査の基本に関係する ALTER 基本の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)の結果から対象行を抜き出し、条件検査の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. ALTER 基本の名称と担当者名だけを残して条件検査の基本の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で条件検査の基本を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0005I の有無を見ず条件検査の基本の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件検査正解では選択記号 A を採用し、正解名は条件検査正解です。条件検査根拠では ALTER 基本 は「ALTER 基本の用途をストレージ管理の表示で確認する条件検査項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は条件検査根拠です。条件検査背景では DFSMS の ALTER 基本と IDC0005I を同じ証跡に残し、背景名は条件検査背景です。他の選択肢を確認します。 A: 条件検査正答は対象出力と項目説明を結び、根拠名は条件検査正答です。 B: 条件検査不足は名称や説明だけに寄り、判定名は条件検査不足です。 C: 条件検査流用は別カテゴリの確認であり、排除名は条件検査流用です。 D: 条件検査欠落は戻り値や記録番号に寄り、欠落名は条件検査欠落です。条件検査用語では ALTER 基本を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件検査用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ALTER 基本</strong></p><p>検証目的: 置換検査の基本について、既存カタログエントリの属性を変更する IDCAMS コマンド。サイズ系は ALTER 不可で、再定義 + REPRO が必要なケースに注意に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010064の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、置換検査の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にALTER 基本を指定し、OSKB010064の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ALTER 基本
CASE OSKB010064
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ALTER 基本
CASE OSKB010064
SOURCE DFSMS
ALTER 基本とOSKB010064が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB010064を同じ出力で読み、置換検査の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
CASE OSKB010064
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
CLUSTER ------- OSKB010064.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0005IとOSKB010064が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
② ステップ2 の ALTER 基本 と OSKB010064 が画面・出力に表示されること
③ ステップ3 の IDC0005I と OSKB010064 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0012"><h3>BUFFERSPACE(n)</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>BUFFERSPACE(n)は、DFSMS / IDCAMS / VSAMのALTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p></section>


<section class="kb-item" id="c06-i0013"><h3>BWO (Backup-While-Open) 設定</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>BWO (Backup-While-Open) 設定は、DFSMS / IDCAMS / VSAMのALTERで構成値やオプションの意味を確認する項目です。指定場所、既定値、変更後に影響する機能を分けて確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更検査のストレージ管理に関する BWO 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず変更検査のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更検査のストレージ管理の証跡として保存して根拠にする。</li><li>C. BWO 属性の変更点を出力本文から切り離して変更検査のストレージ管理の承認欄だけ残す。</li><li>D. IDC0001I を含む表示を保存し、説明欄との差分を変更検査で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更検査正解では選択記号 D を採用し、正解名は変更検査正解です。変更検査根拠では BWO 属性 は「BWO 属性の状態と出力メッセージを結び付ける変更検査項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は変更検査根拠です。変更検査保存では BWO 属性の出力行と IDC0001I を一緒に残し、保存名は変更検査保存です。選択肢ごとの違いを示します。 A: 変更検査欠落は戻り値や記録番号に寄り、欠落名は変更検査欠落です。 B: 変更検査流用は別カテゴリの確認であり、排除名は変更検査流用です。 C: 変更検査不足は名称や説明だけに寄り、判定名は変更検査不足です。 D: 変更検査正答は対象出力と項目説明を結び、根拠名は変更検査正答です。変更検査対象では BWO 属性を DFSMS の確認記録に残し、対象名は変更検査対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>BWO (Backup-While-Open) 設定</strong></p><p>検証目的: 順序検査のストレージ管理について、BWO (Backup-While-Open) 設定は、DFSMS / IDCAMS / VSAM の ALTER で構成値やオプションの意味を確認する項目です。指定場所、既定値に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010075の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、順序検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にBWO (Backup-While-を指定し、OSKB010075の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND BWO (Backup-While-
CASE OSKB010075
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM BWO (Backup-While-
CASE OSKB010075
SOURCE DFSMS
BWO (Backup-While-とOSKB010075が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010075を同じ出力で読み、順序検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010075
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010075.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010075が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の BWO (Backup-While- と OSKB010075 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010075 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0014"><h3>FREESPACE(ci% ca%)</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>FREESPACE(ci% ca%)は、DFSMS / IDCAMS / VSAMのALTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p></section>


<section class="kb-item" id="c06-i0015"><h3>INHIBIT / UNINHIBIT</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>INHIBIT / UNINHIBITは、DFSMS / IDCAMS / VSAMのALTERで機能名、見出し、または確認対象として参照する項目です。更新を抑制 (読み取り専用) または解除。保守やバックアップ取得前の保護に有効。「INHIBIT / UNINHIBIT」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域検査の・に関する INHIBIT 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず値域検査の・の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域検査の・の証跡として保存して根拠にする。</li><li>C. INHIBIT 属性の変更点を出力本文から切り離して値域検査の・の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、値域検査の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域検査正解では選択記号 D を採用し、正解名は値域検査正解です。値域検査根拠では INHIBIT 属性 は「INHIBIT 属性の状態と出力メッセージを結び付ける値域検査項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は値域検査根拠です。値域検査保存では INHIBIT 属性の出力行と IDC3009I を一緒に残し、保存名は値域検査保存です。選択肢ごとの違いを示します。 A: 値域検査欠落は戻り値や記録番号に寄り、欠落名は値域検査欠落です。 B: 値域検査流用は別カテゴリの確認であり、排除名は値域検査流用です。 C: 値域検査不足は名称や説明だけに寄り、判定名は値域検査不足です。 D: 値域検査正答は対象出力と項目説明を結び、根拠名は値域検査正答です。値域検査対象では INHIBIT 属性を DFSMS の確認記録に残し、対象名は値域検査対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>INHIBIT ・ UNINHIBIT</strong></p><p>検証目的: 値域確認の・について、INHIBIT / UNINHIBIT は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。更新を抑制 (読み取に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030016の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、値域確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にINHIBIT ・ UNINHIBIを指定し、OSKB030016の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND INHIBIT ・ UNINHIBI
CASE OSKB030016
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM INHIBIT ・ UNINHIBI
CASE OSKB030016
SOURCE DFSMS
INHIBIT ・ UNINHIBIとOSKB030016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030016を同じ出力で読み、値域確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030016
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030016.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の INHIBIT ・ UNINHIBI と OSKB030016 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>INHIBIT ・ UNINHIBIT</strong></p><p>検証目的: 範囲検査の・について、INHIBIT / UNINHIBIT は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。更新を抑制 (読み取に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010071の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、範囲検査の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にINHIBIT ・ UNINHIBIを指定し、OSKB010071の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND INHIBIT ・ UNINHIBI
CASE OSKB010071
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM INHIBIT ・ UNINHIBI
CASE OSKB010071
SOURCE DFSMS
INHIBIT ・ UNINHIBIとOSKB010071が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010071を同じ出力で読み、範囲検査の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010071
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010071.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010071が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の INHIBIT ・ UNINHIBI と OSKB010071 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010071 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0016"><h3>LOCK / UNLOCK</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>LOCK / UNLOCKは、DFSMS / IDCAMS / VSAMのALTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告検査の・に関係する LOCK ・ UNLOCK の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告検査で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. LOCK ・ UNLOCK の名称と担当者名だけを残して警告検査の・の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で警告検査の・を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず警告検査の・の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告検査正解では選択記号 A を採用し、正解名は警告検査正解です。警告検査根拠では LOCK ・ UNLOCK は「LOCK ・ UNLOCK の用途をストレージ管理の表示で確認する警告検査項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は警告検査根拠です。警告検査背景では DFSMS の LOCK ・ UNLOCK と IDC0001I を同じ証跡に残し、背景名は警告検査背景です。他の選択肢を確認します。 A: 警告検査正答は対象出力と項目説明を結び、根拠名は警告検査正答です。 B: 警告検査不足は名称や説明だけに寄り、判定名は警告検査不足です。 C: 警告検査流用は別カテゴリの確認であり、排除名は警告検査流用です。 D: 警告検査欠落は戻り値や記録番号に寄り、欠落名は警告検査欠落です。警告検査用語では LOCK ・ UNLOCK を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告検査用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LOCK ・ UNLOCK</strong></p><p>検証目的: 優先検査の・について、LOCK / UNLOCK は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010072の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、優先検査の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にLOCK ・ UNLOCKを指定し、OSKB010072の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND LOCK ・ UNLOCK
CASE OSKB010072
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM LOCK ・ UNLOCK
CASE OSKB010072
SOURCE DFSMS
LOCK ・ UNLOCKとOSKB010072が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010072を同じ出力で読み、優先検査の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010072
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010072.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010072が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の LOCK ・ UNLOCK と OSKB010072 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010072 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0017"><h3>LOG / LOGSTREAMID (RLS/TVS)</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>LOG / LOGSTREAMID (RLS/TVS)は、DFSMS / IDCAMS / VSAMのALTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文判定の・ ・に関係する LOG 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、構文判定の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. LOG 属性の名称と担当者名だけを残して構文判定の・ ・の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で構文判定の・ ・を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず構文判定の・ ・の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文判定正解では選択記号 A を採用し、正解名は構文判定正解です。構文判定根拠では LOG 属性 は「LOG 属性の用途をストレージ管理の表示で確認する構文判定項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は構文判定根拠です。構文判定背景では DFSMS の LOG 属性と IDC0001I を同じ証跡に残し、背景名は構文判定背景です。他の選択肢を確認します。 A: 構文判定正答は対象出力と項目説明を結び、根拠名は構文判定正答です。 B: 構文判定不足は名称や説明だけに寄り、判定名は構文判定不足です。 C: 構文判定流用は別カテゴリの確認であり、排除名は構文判定流用です。 D: 構文判定欠落は戻り値や記録番号に寄り、欠落名は構文判定欠落です。構文判定用語では LOG 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文判定用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>LOG ・ LOGSTREAMID (RLS ・ TVS)</strong></p><p>検証目的: 警告確認の・ ・について、LOG / LOGSTREAMID (RLS/TVS)は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。関連に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030017の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、警告確認の・ ・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にLOG ・ LOGSTREAMID を指定し、OSKB030017の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND LOG ・ LOGSTREAMID 
CASE OSKB030017
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM LOG ・ LOGSTREAMID 
CASE OSKB030017
SOURCE DFSMS
LOG ・ LOGSTREAMID とOSKB030017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030017を同じ出力で読み、警告確認の・ ・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030017
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030017.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の LOG ・ LOGSTREAMID  と OSKB030017 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>LOG ・ LOGSTREAMID (RLS ・ TVS)</strong></p><p>検証目的: 値域検査の・ ・について、LOG / LOGSTREAMID (RLS/TVS)は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。関連に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010076の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、値域検査の・ ・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にLOG ・ LOGSTREAMID を指定し、OSKB010076の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND LOG ・ LOGSTREAMID 
CASE OSKB010076
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM LOG ・ LOGSTREAMID 
CASE OSKB010076
SOURCE DFSMS
LOG ・ LOGSTREAMID とOSKB010076が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010076を同じ出力で読み、値域検査の・ ・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010076
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010076.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010076が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の LOG ・ LOGSTREAMID  と OSKB010076 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010076 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0018"><h3>MGMTCLAS / STORCLAS / DATACLAS 変更</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>MGMTCLAS / STORCLAS / DATACLAS 変更は、DFSMS / IDCAMS / VSAMのALTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧検査の・ ・で MGMTCLAS 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. MGMTCLAS 属性の出力を取らず復旧検査の・ ・の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、復旧検査の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して復旧検査の・ ・の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧検査の・ ・へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧検査正解では選択記号 B を採用し、正解名は復旧検査正解です。復旧検査根拠では MGMTCLAS 属性 は「復旧検査の・ ・に関係する定義値と表示行を照合する復旧検査項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は復旧検査根拠です。復旧検査追跡では MGMTCLAS 属性の属性行と IDC0001I を合わせ、追跡名は復旧検査追跡です。誤答側の問題点を分けます。 A: 復旧検査不足は名称や説明だけに寄り、判定名は復旧検査不足です。 B: 復旧検査正答は対象出力と項目説明を結び、根拠名は復旧検査正答です。 C: 復旧検査欠落は戻り値や記録番号に寄り、欠落名は復旧検査欠落です。 D: 復旧検査流用は別カテゴリの確認であり、排除名は復旧検査流用です。復旧検査初出では MGMTCLAS 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧検査初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MGMTCLAS ・ STORCLAS ・ DATACLAS 変更</strong></p><p>検証目的: 記録検査の・ ・について、MGMTCLAS / STORCLAS / DATACLAS 変更は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010073の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、記録検査の・ ・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にMGMTCLAS ・ STORCLAを指定し、OSKB010073の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND MGMTCLAS ・ STORCLA
CASE OSKB010073
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM MGMTCLAS ・ STORCLA
CASE OSKB010073
SOURCE DFSMS
MGMTCLAS ・ STORCLAとOSKB010073が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010073を同じ出力で読み、記録検査の・ ・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010073
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010073.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010073が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の MGMTCLAS ・ STORCLA と OSKB010073 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010073 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0019"><h3>NEWNAME(newname)</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>NEWNAME(newname)は、DFSMS / IDCAMS / VSAMのALTERで機能名、見出し、または確認対象として参照する項目です。エントリ名を改名。DATA/INDEX コンポーネント名も対象。アクティブなオープン中は不可。「NEWNAME(newname)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切検査のストレージ管理で NEWNAME(newname)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. NEWNAME(newname)の出力を取らず区切検査のストレージ管理の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、区切検査の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して区切検査のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切検査のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切検査正解では選択記号 B を採用し、正解名は区切検査正解です。区切検査根拠では NEWNAME(newname) は「区切検査のストレージ管理に関係する定義値と表示行を照合する区切検査項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は区切検査根拠です。区切検査追跡では NEWNAME(newname)の属性行と IDC3009I を合わせ、追跡名は区切検査追跡です。誤答側の問題点を分けます。 A: 区切検査不足は名称や説明だけに寄り、判定名は区切検査不足です。 B: 区切検査正答は対象出力と項目説明を結び、根拠名は区切検査正答です。 C: 区切検査欠落は戻り値や記録番号に寄り、欠落名は区切検査欠落です。 D: 区切検査流用は別カテゴリの確認であり、排除名は区切検査流用です。区切検査初出では NEWNAME(newname)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切検査初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>NEWNAME(newname)</strong></p><p>検証目的: 終端検査のストレージ管理について、NEWNAME(newname)は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。エントリ名を改名。DATAに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010065の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、終端検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にNEWNAME(newname)を指定し、OSKB010065の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND NEWNAME(newname)
CASE OSKB010065
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM NEWNAME(newname)
CASE OSKB010065
SOURCE DFSMS
NEWNAME(newname)とOSKB010065が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010065を同じ出力で読み、終端検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010065
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010065.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010065が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の NEWNAME(newname) と OSKB010065 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010065 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0020"><h3>SHAREOPTIONS(cr cs)</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>SHAREOPTIONS(cr cs)は、DFSMS / IDCAMS / VSAMのALTERで構成値やオプションの意味を確認する項目です。共有オプションを変更。アプリ側のロック設計と合わせて慎重に行う。「SHAREOPTIONS(cr cs)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p></section>


<section class="kb-item" id="c06-i0021"><h3>TO(yyyyddd) / FOR(days)</h3><p class="kb-meta">分類: ALTER ・ 難易度: 上級</p><p>TO(yyyyddd) / FOR(days)は、DFSMS / IDCAMS / VSAMのALTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p></section>


## BLDINDEX


<section class="kb-item" id="c06-i0022"><h3>BLDINDEX 基本</h3><p class="kb-meta">分類: BLDINDEX ・ 難易度: 上級</p><p>BLDINDEX 基本は、DFSMS / IDCAMS / VSAMのBLDINDEXで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件記録の基本に関係する BLDINDEX 基本の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、条件記録の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. BLDINDEX 基本の名称と担当者名だけを残して条件記録の基本の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で条件記録の基本を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず条件記録の基本の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件記録正解では選択記号 A を採用し、正解名は条件記録正解です。条件記録根拠では BLDINDEX 基本 は「BLDINDEX 基本の用途をストレージ管理の表示で確認する条件記録項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は条件記録根拠です。条件記録背景では DFSMS の BLDINDEX 基本と IDC0001I を同じ証跡に残し、背景名は条件記録背景です。他の選択肢を確認します。 A: 条件記録正答は対象出力と項目説明を結び、根拠名は条件記録正答です。 B: 条件記録不足は名称や説明だけに寄り、判定名は条件記録不足です。 C: 条件記録流用は別カテゴリの確認であり、排除名は条件記録流用です。 D: 条件記録欠落は戻り値や記録番号に寄り、欠落名は条件記録欠落です。条件記録用語では BLDINDEX 基本を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件記録用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>BLDINDEX 基本</strong></p><p>検証目的: 置換確認の基本について、BLDINDEX 基本は、DFSMS / IDCAMS / VSAM の BLDINDEX で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020004の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、置換確認の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にBLDINDEX 基本を指定し、OSKB020004の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND BLDINDEX 基本
CASE OSKB020004
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM BLDINDEX 基本
CASE OSKB020004
SOURCE DFSMS
BLDINDEX 基本とOSKB020004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020004を同じ出力で読み、置換確認の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020004
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020004.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の BLDINDEX 基本 と OSKB020004 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0023"><h3>EXTERNALSORT / INTERNALSORT</h3><p class="kb-meta">分類: BLDINDEX ・ 難易度: 上級</p><p>EXTERNALSORT / INTERNALSORTは、DFSMS / IDCAMS / VSAMのBLDINDEXで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲記録の・でストレージ管理の運用確認を行います。EXTERNALSORT 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で範囲記録の・を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず範囲記録の・を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて範囲記録の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. EXTERNALSORT 属性の属性行を読まず範囲記録の・の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲記録正解では選択記号 C を採用し、正解名は範囲記録正解です。範囲記録根拠では EXTERNALSORT 属性 は「DFSMS で EXTERNALSORT 属性の扱いを記録する範囲記録項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は範囲記録根拠です。範囲記録受渡では EXTERNALSORT 属性の表示結果と IDC0001I を同じ確認単位にし、受渡名は範囲記録受渡です。不適切な選択肢を整理します。 A: 範囲記録流用は別カテゴリの確認であり、排除名は範囲記録流用です。 B: 範囲記録欠落は戻り値や記録番号に寄り、欠落名は範囲記録欠落です。 C: 範囲記録正答は対象出力と項目説明を結び、根拠名は範囲記録正答です。 D: 範囲記録不足は名称や説明だけに寄り、判定名は範囲記録不足です。範囲記録資料では EXTERNALSORT 属性の使い方を出典欄から追跡し、資料名は範囲記録資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>EXTERNALSORT ・ INTERNALSORT</strong></p><p>検証目的: 上書照合の・について、EXTERNALSORT / INTERNALSORT は、DFSMS / IDCAMS / VSAM の BLDINDEX で機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030027の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、上書照合の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にEXTERNALSORT ・ INTを指定し、OSKB030027の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND EXTERNALSORT ・ INT
CASE OSKB030027
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM EXTERNALSORT ・ INT
CASE OSKB030027
SOURCE DFSMS
EXTERNALSORT ・ INTとOSKB030027が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030027を同じ出力で読み、上書照合の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030027
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030027.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030027が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の EXTERNALSORT ・ INT と OSKB030027 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030027 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>EXTERNALSORT ・ INTERNALSORT</strong></p><p>検証目的: 探索確認の・について、EXTERNALSORT / INTERNALSORT は、DFSMS / IDCAMS / VSAM の BLDINDEX で機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020006の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、探索確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にEXTERNALSORT ・ INTを指定し、OSKB020006の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND EXTERNALSORT ・ INT
CASE OSKB020006
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM EXTERNALSORT ・ INT
CASE OSKB020006
SOURCE DFSMS
EXTERNALSORT ・ INTとOSKB020006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020006を同じ出力で読み、探索確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020006
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020006.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の EXTERNALSORT ・ INT と OSKB020006 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0024"><h3>INDATASET / OUTDATASET (BLDINDEX)</h3><p class="kb-meta">分類: BLDINDEX ・ 難易度: 上級</p><p>INDATASET / OUTDATASET (BLDINDEX)は、DFSMS / IDCAMS / VSAMのBLDINDEXで機能名、見出し、または確認対象として参照する項目です。INDATASET はベース、OUTDATASET は AIX を指定。SORTWK 系の DD も併せて確保。「INDATASET / OUTDATASET (BLDINDEX)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切記録の・で INDATASET 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. INDATASET 属性の出力を取らず区切記録の・の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、区切記録の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して区切記録の・の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切記録の・へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切記録正解では選択記号 B を採用し、正解名は区切記録正解です。区切記録根拠では INDATASET 属性 は「区切記録の・に関係する定義値と表示行を照合する区切記録項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は区切記録根拠です。区切記録追跡では INDATASET 属性の属性行と IDC3009I を合わせ、追跡名は区切記録追跡です。誤答側の問題点を分けます。 A: 区切記録不足は名称や説明だけに寄り、判定名は区切記録不足です。 B: 区切記録正答は対象出力と項目説明を結び、根拠名は区切記録正答です。 C: 区切記録欠落は戻り値や記録番号に寄り、欠落名は区切記録欠落です。 D: 区切記録流用は別カテゴリの確認であり、排除名は区切記録流用です。区切記録初出では INDATASET 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切記録初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>INDATASET ・ OUTDATASET (BLDINDEX)</strong></p><p>検証目的: 終端確認の・について、INDATASET / OUTDATASET (BLDINDEX)は、DFSMS / IDCAMS / VSAM の BLDINDEX で機能名、見出し、または確認対象として参照に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020005の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、終端確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にINDATASET ・ OUTDATを指定し、OSKB020005の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND INDATASET ・ OUTDAT
CASE OSKB020005
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM INDATASET ・ OUTDAT
CASE OSKB020005
SOURCE DFSMS
INDATASET ・ OUTDATとOSKB020005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020005を同じ出力で読み、終端確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020005
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020005.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の INDATASET ・ OUTDAT と OSKB020005 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0025"><h3>WORKFILES(dd1 dd2)</h3><p class="kb-meta">分類: BLDINDEX ・ 難易度: 上級</p><p>WORKFILES(dd1 dd2)は、DFSMS / IDCAMS / VSAMのBLDINDEXで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先記録のストレージ管理に関する WORKFILES(dd1 dd2)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず優先記録のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先記録のストレージ管理の証跡として保存して根拠にする。</li><li>C. WORKFILES(dd1 dd2)の変更点を出力本文から切り離して優先記録のストレージ管理の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC0001I を読み、優先記録の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先記録正解では選択記号 D を採用し、正解名は優先記録正解です。優先記録根拠では WORKFILES(dd1 dd2) は「WORKFILES(dd1 dd2)の状態と出力メッセージを結び付ける優先記録項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は優先記録根拠です。優先記録保存では WORKFILES(dd1 dd2)の出力行と IDC0001I を一緒に残し、保存名は優先記録保存です。選択肢ごとの違いを示します。 A: 優先記録欠落は戻り値や記録番号に寄り、欠落名は優先記録欠落です。 B: 優先記録流用は別カテゴリの確認であり、排除名は優先記録流用です。 C: 優先記録不足は名称や説明だけに寄り、判定名は優先記録不足です。 D: 優先記録正答は対象出力と項目説明を結び、根拠名は優先記録正答です。優先記録対象では WORKFILES(dd1 dd2)を DFSMS の確認記録に残し、対象名は優先記録対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>WORKFILES(dd1 dd2)</strong></p><p>検証目的: 上書確認のストレージ管理について、WORKFILES(dd1 dd2)は、DFSMS / IDCAMS / VSAM の BLDINDEX で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020007の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、上書確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にWORKFILES(dd1 dd2)を指定し、OSKB020007の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND WORKFILES(dd1 dd2)
CASE OSKB020007
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM WORKFILES(dd1 dd2)
CASE OSKB020007
SOURCE DFSMS
WORKFILES(dd1 dd2)とOSKB020007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020007を同じ出力で読み、上書確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020007
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020007.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の WORKFILES(dd1 dd2) と OSKB020007 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## DEFINE_AIX


<section class="kb-item" id="c06-i0026"><h3>DEFINE ALTERNATEINDEX 基本</h3><p class="kb-meta">分類: DEFINE_AIX ・ 難易度: 上級</p><p>DEFINE ALTERNATEINDEX 基本は、DFSMS / IDCAMS / VSAMのDEFINE_AIXで機能名、見出し、または確認対象として参照する項目です。ベース KSDS/ESDS の代替インデックスを定義。代替キーで KSDS と同じアクセス手段を提供する。「DEFINE ALTERNATEINDEX 基本」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更照合の基本に関する DEFINE 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず変更照合の基本の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更照合の基本の証跡として保存して根拠にする。</li><li>C. DEFINE 機能の変更点を出力本文から切り離して変更照合の基本の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、変更照合の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更照合正解では選択記号 D を採用し、正解名は変更照合正解です。変更照合根拠では DEFINE 機能 は「DEFINE 機能の状態と出力メッセージを結び付ける変更照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は変更照合根拠です。変更照合保存では DEFINE 機能の出力行と IDC3009I を一緒に残し、保存名は変更照合保存です。選択肢ごとの違いを示します。 A: 変更照合欠落は戻り値や記録番号に寄り、欠落名は変更照合欠落です。 B: 変更照合流用は別カテゴリの確認であり、排除名は変更照合流用です。 C: 変更照合不足は名称や説明だけに寄り、判定名は変更照合不足です。 D: 変更照合正答は対象出力と項目説明を結び、根拠名は変更照合正答です。変更照合対象では DEFINE 機能を DFSMS の確認記録に残し、対象名は変更照合対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEFINE ALTERNATEINDEX 基本</strong></p><p>検証目的: 順序照合の基本について、DEFINE ALTERNATEINDEX 基本は、DFSMS / IDCAMS / VSAM の DEFINE_AIX で機能名、見出し、または確認対象として参照する項目です。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010035の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、順序照合の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDEFINE ALTERNATEINを指定し、OSKB010035の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DEFINE ALTERNATEIN
CASE OSKB010035
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DEFINE ALTERNATEIN
CASE OSKB010035
SOURCE DFSMS
DEFINE ALTERNATEINとOSKB010035が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010035を同じ出力で読み、順序照合の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010035
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010035.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010035が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DEFINE ALTERNATEIN と OSKB010035 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010035 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0027"><h3>KEYS(len off) / RECORDSIZE</h3><p class="kb-meta">分類: DEFINE_AIX ・ 難易度: 上級</p><p>KEYS(len off) / RECORDSIZEは、DFSMS / IDCAMS / VSAMのDEFINE_AIXで確認する項目です。代替キーの長さとオフセット、AIX レコードのサイズ。NONUNIQUEKEY ではポインタリスト長を考慮した max を取る</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換追跡の・に関する KEYS 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず置換追跡の・の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換追跡の・の証跡として保存して根拠にする。</li><li>C. KEYS 属性の変更点を出力本文から切り離して置換追跡の・の承認欄だけ残す。</li><li>D. IDC3009I を含む表示を保存し、説明欄との差分を置換追跡で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換追跡正解では選択記号 D を採用し、正解名は置換追跡正解です。置換追跡根拠では KEYS 属性 は「KEYS 属性の状態と出力メッセージを結び付ける置換追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は置換追跡根拠です。置換追跡保存では KEYS 属性の出力行と IDC3009I を一緒に残し、保存名は置換追跡保存です。選択肢ごとの違いを示します。 A: 置換追跡欠落は戻り値や記録番号に寄り、欠落名は置換追跡欠落です。 B: 置換追跡流用は別カテゴリの確認であり、排除名は置換追跡流用です。 C: 置換追跡不足は名称や説明だけに寄り、判定名は置換追跡不足です。 D: 置換追跡正答は対象出力と項目説明を結び、根拠名は置換追跡正答です。置換追跡対象では KEYS 属性を DFSMS の確認記録に残し、対象名は置換追跡対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>KEYS(len off) ・ RECORDSIZE</strong></p><p>検証目的: 監査照合の・について、KEYS(len off) / RECORDSIZE は、DFSMS / IDCAMS / VSAM の DEFINE_AIX で確認する項目です。代替キーの長さとオフセット、AIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010039の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、監査照合の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にKEYS(len off) ・ REを指定し、OSKB010039の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND KEYS(len off) ・ RE
CASE OSKB010039
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM KEYS(len off) ・ RE
CASE OSKB010039
SOURCE DFSMS
KEYS(len off) ・ REとOSKB010039が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010039を同じ出力で読み、監査照合の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010039
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010039.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010039が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の KEYS(len off) ・ RE と OSKB010039 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010039 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0028"><h3>RELATE(basename)</h3><p class="kb-meta">分類: DEFINE_AIX ・ 難易度: 上級</p><p>RELATE(basename)は、DFSMS / IDCAMS / VSAMのDEFINE_AIXで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文追跡のストレージ管理に関係する RELATE(basename)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、構文追跡で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. RELATE(basename)の名称と担当者名だけを残して構文追跡のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で構文追跡のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず構文追跡のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文追跡正解では選択記号 A を採用し、正解名は構文追跡正解です。構文追跡根拠では RELATE(basename) は「RELATE(basename)の用途をストレージ管理の表示で確認する構文追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は構文追跡根拠です。構文追跡背景では DFSMS の RELATE(basename)と IDC3009I を同じ証跡に残し、背景名は構文追跡背景です。他の選択肢を確認します。 A: 構文追跡正答は対象出力と項目説明を結び、根拠名は構文追跡正答です。 B: 構文追跡不足は名称や説明だけに寄り、判定名は構文追跡不足です。 C: 構文追跡流用は別カテゴリの確認であり、排除名は構文追跡流用です。 D: 構文追跡欠落は戻り値や記録番号に寄り、欠落名は構文追跡欠落です。構文追跡用語では RELATE(basename)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文追跡用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>RELATE(basename)</strong></p><p>検証目的: 条件確認のストレージ管理について、RELATE(basename)は、DFSMS / IDCAMS / VSAM の DEFINE_AIX で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030009の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、条件確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にRELATE(basename)を指定し、OSKB030009の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND RELATE(basename)
CASE OSKB030009
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM RELATE(basename)
CASE OSKB030009
SOURCE DFSMS
RELATE(basename)とOSKB030009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030009を同じ出力で読み、条件確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030009
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030009.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の RELATE(basename) と OSKB030009 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>RELATE(basename)</strong></p><p>検証目的: 値域照合のストレージ管理について、RELATE(basename)は、DFSMS / IDCAMS / VSAM の DEFINE_AIX で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010036の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、値域照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にRELATE(basename)を指定し、OSKB010036の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND RELATE(basename)
CASE OSKB010036
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM RELATE(basename)
CASE OSKB010036
SOURCE DFSMS
RELATE(basename)とOSKB010036が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010036を同じ出力で読み、値域照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010036
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010036.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010036が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の RELATE(basename) と OSKB010036 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010036 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0029"><h3>UNIQUEKEY / NONUNIQUEKEY</h3><p class="kb-meta">分類: DEFINE_AIX ・ 難易度: 上級</p><p>UNIQUEKEY / NONUNIQUEKEYは、DFSMS / IDCAMS / VSAMのDEFINE_AIXで確認する項目です。代替キーが一意か否か。NONUNIQUEKEY ではキー重複時に複数レコードをポイントできるが、レコード長が増える</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開追跡の・で UNIQUEKEY 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. UNIQUEKEY 属性の出力を取らず展開追跡の・の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、展開追跡の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して展開追跡の・の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開追跡の・へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開追跡正解では選択記号 B を採用し、正解名は展開追跡正解です。展開追跡根拠では UNIQUEKEY 属性 は「展開追跡の・に関係する定義値と表示行を照合する展開追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は展開追跡根拠です。展開追跡追跡では UNIQUEKEY 属性の属性行と IDC3009I を合わせ、追跡名は展開追跡追跡です。誤答側の問題点を分けます。 A: 展開追跡不足は名称や説明だけに寄り、判定名は展開追跡不足です。 B: 展開追跡正答は対象出力と項目説明を結び、根拠名は展開追跡正答です。 C: 展開追跡欠落は戻り値や記録番号に寄り、欠落名は展開追跡欠落です。 D: 展開追跡流用は別カテゴリの確認であり、排除名は展開追跡流用です。展開追跡初出では UNIQUEKEY 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開追跡初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UNIQUEKEY ・ NONUNIQUEKEY</strong></p><p>検証目的: 警告照合の・について、UNIQUEKEY / NONUNIQUEKEY は、DFSMS / IDCAMS / VSAM の DEFINE_AIX で確認する項目です。代替キーが一意か否か。NONUNIQに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010037の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、警告照合の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にUNIQUEKEY ・ NONUNIを指定し、OSKB010037の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND UNIQUEKEY ・ NONUNI
CASE OSKB010037
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM UNIQUEKEY ・ NONUNI
CASE OSKB010037
SOURCE DFSMS
UNIQUEKEY ・ NONUNIとOSKB010037が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010037を同じ出力で読み、警告照合の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010037
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010037.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010037が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の UNIQUEKEY ・ NONUNI と OSKB010037 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010037 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0030"><h3>UPGRADE / NOUPGRADE</h3><p class="kb-meta">分類: DEFINE_AIX ・ 難易度: 上級</p><p>UPGRADE / NOUPGRADEは、DFSMS / IDCAMS / VSAMのDEFINE_AIXで機能名、見出し、または確認対象として参照する項目です。ベース更新時に AIX を自動同期するか。UPGRADE 指定の AIX はベースの UPGRADE SET に含められ、書込み性能と引き替えに整合性を維持する</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出追跡の・でストレージ管理の運用確認を行います。UPGRADE 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で呼出追跡の・を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず呼出追跡の・を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて呼出追跡の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. UPGRADE 属性の属性行を読まず呼出追跡の・の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出追跡正解では選択記号 C を採用し、正解名は呼出追跡正解です。呼出追跡根拠では UPGRADE 属性 は「DFSMS で UPGRADE 属性の扱いを記録する呼出追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は呼出追跡根拠です。呼出追跡受渡では UPGRADE 属性の表示結果と IDC3009I を同じ確認単位にし、受渡名は呼出追跡受渡です。不適切な選択肢を整理します。 A: 呼出追跡流用は別カテゴリの確認であり、排除名は呼出追跡流用です。 B: 呼出追跡欠落は戻り値や記録番号に寄り、欠落名は呼出追跡欠落です。 C: 呼出追跡正答は対象出力と項目説明を結び、根拠名は呼出追跡正答です。 D: 呼出追跡不足は名称や説明だけに寄り、判定名は呼出追跡不足です。呼出追跡資料では UPGRADE 属性の使い方を出典欄から追跡し、資料名は呼出追跡資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UPGRADE ・ NOUPGRADE</strong></p><p>検証目的: 復旧照合の・について、UPGRADE / NOUPGRADE は、DFSMS / IDCAMS / VSAM の DEFINE_AIX で機能名、見出し、または確認対象として参照する項目です。ベース更新に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010038の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、復旧照合の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にUPGRADE ・ NOUPGRADを指定し、OSKB010038の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND UPGRADE ・ NOUPGRAD
CASE OSKB010038
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM UPGRADE ・ NOUPGRAD
CASE OSKB010038
SOURCE DFSMS
UPGRADE ・ NOUPGRADとOSKB010038が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010038を同じ出力で読み、復旧照合の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010038
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010038.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010038が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の UPGRADE ・ NOUPGRAD と OSKB010038 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010038 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## DEFINE_ALIAS


<section class="kb-item" id="c06-i0031"><h3>DEFINE ALIAS 基本</h3><p class="kb-meta">分類: DEFINE_ALIAS ・ 難易度: 上級</p><p>DEFINE ALIAS 基本は、DFSMS / IDCAMS / VSAMのDEFINE_ALIASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索検査の基本で DEFINE ALIAS 基本の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE ALIAS 基本の出力を取らず探索検査の基本の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、探索検査の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して探索検査の基本の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索検査の基本へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索検査正解では選択記号 B を採用し、正解名は探索検査正解です。探索検査根拠では DEFINE ALIAS 基本 は「探索検査の基本に関係する定義値と表示行を照合する探索検査項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は探索検査根拠です。探索検査追跡では DEFINE ALIAS 基本の属性行と IDC3009I を合わせ、追跡名は探索検査追跡です。誤答側の問題点を分けます。 A: 探索検査不足は名称や説明だけに寄り、判定名は探索検査不足です。 B: 探索検査正答は対象出力と項目説明を結び、根拠名は探索検査正答です。 C: 探索検査欠落は戻り値や記録番号に寄り、欠落名は探索検査欠落です。 D: 探索検査流用は別カテゴリの確認であり、排除名は探索検査流用です。探索検査初出では DEFINE ALIAS 基本を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索検査初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEFINE ALIAS 基本</strong></p><p>検証目的: 比較確認の基本について、DEFINE ALIAS 基本は、DFSMS / IDCAMS / VSAM の DEFINE_ALIAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030014の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、比較確認の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDEFINE ALIAS 基本を指定し、OSKB030014の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DEFINE ALIAS 基本
CASE OSKB030014
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DEFINE ALIAS 基本
CASE OSKB030014
SOURCE DFSMS
DEFINE ALIAS 基本とOSKB030014が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030014を同じ出力で読み、比較確認の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030014
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030014.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030014が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DEFINE ALIAS 基本 と OSKB030014 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030014 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>DEFINE ALIAS 基本</strong></p><p>検証目的: 構文検査の基本について、DEFINE ALIAS 基本は、DFSMS / IDCAMS / VSAM の DEFINE_ALIAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010061の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、構文検査の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDEFINE ALIAS 基本を指定し、OSKB010061の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DEFINE ALIAS 基本
CASE OSKB010061
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DEFINE ALIAS 基本
CASE OSKB010061
SOURCE DFSMS
DEFINE ALIAS 基本とOSKB010061が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010061を同じ出力で読み、構文検査の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010061
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010061.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010061が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DEFINE ALIAS 基本 と OSKB010061 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010061 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0032"><h3>RELATE(usercatname)</h3><p class="kb-meta">分類: DEFINE_ALIAS ・ 難易度: 上級</p><p>RELATE(usercatname)は、DFSMS / IDCAMS / VSAMのDEFINE_ALIASで機能名、見出し、または確認対象として参照する項目です。ALIAS が指す先のユーザカタログ名。ALIAS が示す HLQ で始まる新規データセットはこのカタログに登録される。「RELATE(usercatname)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書検査のストレージ管理でストレージ管理の運用確認を行います。RELATE 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で上書検査のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず上書検査のストレージ管理を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて上書検査の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. RELATE 属性の属性行を読まず上書検査のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書検査正解では選択記号 C を採用し、正解名は上書検査正解です。上書検査根拠では RELATE 属性 は「DFSMS で RELATE 属性の扱いを記録する上書検査項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は上書検査根拠です。上書検査受渡では RELATE 属性の表示結果と IDC3009I を同じ確認単位にし、受渡名は上書検査受渡です。不適切な選択肢を整理します。 A: 上書検査流用は別カテゴリの確認であり、排除名は上書検査流用です。 B: 上書検査欠落は戻り値や記録番号に寄り、欠落名は上書検査欠落です。 C: 上書検査正答は対象出力と項目説明を結び、根拠名は上書検査正答です。 D: 上書検査不足は名称や説明だけに寄り、判定名は上書検査不足です。上書検査資料では RELATE 属性の使い方を出典欄から追跡し、資料名は上書検査資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RELATE(usercatname)</strong></p><p>検証目的: 展開検査のストレージ管理について、RELATE(usercatname)は、DFSMS / IDCAMS / VSAM の DEFINE_ALIAS で機能名、見出し、または確認対象として参照する項目です。ALIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010062の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、展開検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にRELATE(usercatnameを指定し、OSKB010062の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND RELATE(usercatname
CASE OSKB010062
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM RELATE(usercatname
CASE OSKB010062
SOURCE DFSMS
RELATE(usercatnameとOSKB010062が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010062を同じ出力で読み、展開検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010062
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010062.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010062が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の RELATE(usercatname と OSKB010062 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010062 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0033"><h3>SYMBOLICRELATE</h3><p class="kb-meta">分類: DEFINE_ALIAS ・ 難易度: 上級</p><p>SYMBOLICRELATEは、DFSMS / IDCAMS / VSAMのDEFINE_ALIASで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力検査のストレージ管理に関する SYMBOLICRELATE の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず出力検査のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力検査のストレージ管理の証跡として保存して根拠にする。</li><li>C. SYMBOLICRELATE の変更点を出力本文から切り離して出力検査のストレージ管理の承認欄だけ残す。</li><li>D. IDC3009I を含む表示を保存し、説明欄との差分を出力検査で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力検査正解では選択記号 D を採用し、正解名は出力検査正解です。出力検査根拠では SYMBOLICRELATE は「SYMBOLICRELATE の状態と出力メッセージを結び付ける出力検査項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は出力検査根拠です。出力検査保存では SYMBOLICRELATE の出力行と IDC3009I を一緒に残し、保存名は出力検査保存です。選択肢ごとの違いを示します。 A: 出力検査欠落は戻り値や記録番号に寄り、欠落名は出力検査欠落です。 B: 出力検査流用は別カテゴリの確認であり、排除名は出力検査流用です。 C: 出力検査不足は名称や説明だけに寄り、判定名は出力検査不足です。 D: 出力検査正答は対象出力と項目説明を結び、根拠名は出力検査正答です。出力検査対象では SYMBOLICRELATE を DFSMS の確認記録に残し、対象名は出力検査対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SYMBOLICRELATE</strong></p><p>検証目的: 呼出検査のストレージ管理について、SYMBOLICRELATE は、DFSMS / IDCAMS / VSAM の DEFINE_ALIAS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010063の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、呼出検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSYMBOLICRELATEを指定し、OSKB010063の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND SYMBOLICRELATE
CASE OSKB010063
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM SYMBOLICRELATE
CASE OSKB010063
SOURCE DFSMS
SYMBOLICRELATEとOSKB010063が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010063を同じ出力で読み、呼出検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010063
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010063.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010063が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の SYMBOLICRELATE と OSKB010063 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010063 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## DEFINE_CATALOG


<section class="kb-item" id="c06-i0034"><h3>DEFINE MASTERCATALOG</h3><p class="kb-meta">分類: DEFINE_CATALOG ・ 難易度: 上級</p><p>DEFINE MASTERCATALOGは、DFSMS / IDCAMS / VSAMのDEFINE_CATALOGで確認する項目です。マスターカタログ初期化用コマンド。システム初期セットアップ時 1 回のみ実行し、IPL パラメータ (LOADxx) で参照される</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更追跡のストレージ管理に関する DEFINE 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず変更追跡のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更追跡のストレージ管理の証跡として保存して根拠にする。</li><li>C. DEFINE 機能の変更点を出力本文から切り離して変更追跡のストレージ管理の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC3009I を読み、変更追跡の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更追跡正解では選択記号 D を採用し、正解名は変更追跡正解です。変更追跡根拠では DEFINE 機能 は「DEFINE 機能の状態と出力メッセージを結び付ける変更追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は変更追跡根拠です。変更追跡保存では DEFINE 機能の出力行と IDC3009I を一緒に残し、保存名は変更追跡保存です。選択肢ごとの違いを示します。 A: 変更追跡欠落は戻り値や記録番号に寄り、欠落名は変更追跡欠落です。 B: 変更追跡流用は別カテゴリの確認であり、排除名は変更追跡流用です。 C: 変更追跡不足は名称や説明だけに寄り、判定名は変更追跡不足です。 D: 変更追跡正答は対象出力と項目説明を結び、根拠名は変更追跡正答です。変更追跡対象では DEFINE 機能を DFSMS の確認記録に残し、対象名は変更追跡対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEFINE MASTERCATALOG</strong></p><p>検証目的: 順序追跡のストレージ管理について、DEFINE MASTERCATALOG は、DFSMS / IDCAMS / VSAM の DEFINE_CATALOG で確認する項目です。マスターカタログ初期化用コマンド。シに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010055の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、順序追跡のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDEFINE MASTERCATALを指定し、OSKB010055の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DEFINE MASTERCATAL
CASE OSKB010055
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DEFINE MASTERCATAL
CASE OSKB010055
SOURCE DFSMS
DEFINE MASTERCATALとOSKB010055が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010055を同じ出力で読み、順序追跡のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010055
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010055.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010055が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DEFINE MASTERCATAL と OSKB010055 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010055 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0035"><h3>DEFINE USERCATALOG</h3><p class="kb-meta">分類: DEFINE_CATALOG ・ 難易度: 上級</p><p>ユーザカタログ (ICF/BCS) を作成。VSAM クラスターとして実装される。高エイリアス修飾子で分担されるカタログのインスタンス</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査追跡のストレージ管理でストレージ管理の運用確認を行います。DEFINE USERCATALOG の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で監査追跡のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず監査追跡のストレージ管理を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて監査追跡の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. DEFINE USERCATALOG の属性行を読まず監査追跡のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査追跡正解では選択記号 C を採用し、正解名は監査追跡正解です。監査追跡根拠では DEFINE USERCATALOG は「DFSMS で DEFINE USERCATALOG の扱いを記録する監査追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は監査追跡根拠です。監査追跡受渡では DEFINE USERCATALOG の表示結果と IDC3009I を同じ確認単位にし、受渡名は監査追跡受渡です。不適切な選択肢を整理します。 A: 監査追跡流用は別カテゴリの確認であり、排除名は監査追跡流用です。 B: 監査追跡欠落は戻り値や記録番号に寄り、欠落名は監査追跡欠落です。 C: 監査追跡正答は対象出力と項目説明を結び、根拠名は監査追跡正答です。 D: 監査追跡不足は名称や説明だけに寄り、判定名は監査追跡不足です。監査追跡資料では DEFINE USERCATALOG の使い方を出典欄から追跡し、資料名は監査追跡資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEFINE USERCATALOG</strong></p><p>検証目的: 比較追跡のストレージ管理について、ユーザカタログ (ICF/BCS) を作成。VSAM クラスターとして実装される。高エイリアス修飾子で分担されるカタログのインスタンスに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010054の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、比較追跡のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDEFINE USERCATALOGを指定し、OSKB010054の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DEFINE USERCATALOG
CASE OSKB010054
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DEFINE USERCATALOG
CASE OSKB010054
SOURCE DFSMS
DEFINE USERCATALOGとOSKB010054が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010054を同じ出力で読み、比較追跡のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010054
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010054.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010054が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DEFINE USERCATALOG と OSKB010054 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010054 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0036"><h3>ICFCATALOG</h3><p class="kb-meta">分類: DEFINE_CATALOG ・ 難易度: 上級</p><p>ICF 形式カタログ (現行標準) を指定。旧 VSAM カタログ (VCAT) は廃止済み。「ICFCATALOG」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文検査のストレージ管理に関係する ICFCATALOG の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、構文検査の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. ICFCATALOG の名称と担当者名だけを残して構文検査のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で構文検査のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず構文検査のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文検査正解では選択記号 A を採用し、正解名は構文検査正解です。構文検査根拠では ICFCATALOG は「ICFCATALOG の用途をストレージ管理の表示で確認する構文検査項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は構文検査根拠です。構文検査背景では DFSMS の ICFCATALOG と IDC3009I を同じ証跡に残し、背景名は構文検査背景です。他の選択肢を確認します。 A: 構文検査正答は対象出力と項目説明を結び、根拠名は構文検査正答です。 B: 構文検査不足は名称や説明だけに寄り、判定名は構文検査不足です。 C: 構文検査流用は別カテゴリの確認であり、排除名は構文検査流用です。 D: 構文検査欠落は戻り値や記録番号に寄り、欠落名は構文検査欠落です。構文検査用語では ICFCATALOG を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文検査用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>ICFCATALOG</strong></p><p>検証目的: 記録確認のストレージ管理について、ICF 形式カタログ (現行標準) を指定。旧 VSAM カタログ (VCAT) は廃止済み。「ICFCATALOG」を読むと、DEFINE、ALTER、DELETE、LIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030013の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、記録確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にICFCATALOGを指定し、OSKB030013の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ICFCATALOG
CASE OSKB030013
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ICFCATALOG
CASE OSKB030013
SOURCE DFSMS
ICFCATALOGとOSKB030013が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030013を同じ出力で読み、記録確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030013
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030013.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030013が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の ICFCATALOG と OSKB030013 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030013 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>ICFCATALOG</strong></p><p>検証目的: 値域追跡のストレージ管理について、ICF 形式カタログ (現行標準) を指定。旧 VSAM カタログ (VCAT) は廃止済み。「ICFCATALOG」を読むと、DEFINE、ALTER、DELETE、LIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010056の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、値域追跡のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にICFCATALOGを指定し、OSKB010056の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ICFCATALOG
CASE OSKB010056
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ICFCATALOG
CASE OSKB010056
SOURCE DFSMS
ICFCATALOGとOSKB010056が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010056を同じ出力で読み、値域追跡のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010056
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010056.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010056が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の ICFCATALOG と OSKB010056 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010056 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0037"><h3>STRNO(n) (カタログ性能)</h3><p class="kb-meta">分類: DEFINE_CATALOG ・ 難易度: 上級</p><p>STRNO(n) (カタログ性能)は、DFSMS / IDCAMS / VSAMのDEFINE_CATALOGで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出検査のカタログ性能でストレージ管理の運用確認を行います。STRNO(n) (カタログ性能)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で呼出検査のカタログ性能を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず呼出検査のカタログ性能を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出検査の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. STRNO(n) (カタログ性能)の属性行を読まず呼出検査のカタログ性能の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出検査正解では選択記号 C を採用し、正解名は呼出検査正解です。呼出検査根拠では STRNO(n) (カタログ性能) は「DFSMS で STRNO(n) (カタログ性能)の扱いを記録する呼出検査項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は呼出検査根拠です。呼出検査受渡では STRNO(n) (カタログ性能)の表示結果と IDC3009I を同じ確認単位にし、受渡名は呼出検査受渡です。不適切な選択肢を整理します。 A: 呼出検査流用は別カテゴリの確認であり、排除名は呼出検査流用です。 B: 呼出検査欠落は戻り値や記録番号に寄り、欠落名は呼出検査欠落です。 C: 呼出検査正答は対象出力と項目説明を結び、根拠名は呼出検査正答です。 D: 呼出検査不足は名称や説明だけに寄り、判定名は呼出検査不足です。呼出検査資料では STRNO(n) (カタログ性能)の使い方を出典欄から追跡し、資料名は呼出検査資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>STRNO(n) (カタログ性能)</strong></p><p>検証目的: 復旧追跡のカタログ性能について、STRNO(n) (カタログ性能)は、DFSMS / IDCAMS / VSAM の DEFINE_CATALOG で機能名、見出し、または確認対象として参照する項目です。関連すに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010058の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、復旧追跡のカタログ性能の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSTRNO(n) (カタログ性能)を指定し、OSKB010058の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND STRNO(n) (カタログ性能)
CASE OSKB010058
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM STRNO(n) (カタログ性能)
CASE OSKB010058
SOURCE DFSMS
STRNO(n) (カタログ性能)とOSKB010058が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010058を同じ出力で読み、復旧追跡のカタログ性能の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010058
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010058.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010058が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の STRNO(n) (カタログ性能) と OSKB010058 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010058 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0038"><h3>VOLCATALOG (テープ)</h3><p class="kb-meta">分類: DEFINE_CATALOG ・ 難易度: 上級</p><p>VOLCATALOG (テープ)は、DFSMS / IDCAMS / VSAMのDEFINE_CATALOGで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開検査のテープで VOLCATALOG (テープ)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. VOLCATALOG (テープ)の出力を取らず展開検査のテープの説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、展開検査として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して展開検査のテープの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開検査のテープへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開検査正解では選択記号 B を採用し、正解名は展開検査正解です。展開検査根拠では VOLCATALOG (テープ) は「展開検査のテープに関係する定義値と表示行を照合する展開検査項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は展開検査根拠です。展開検査追跡では VOLCATALOG (テープ)の属性行と IDC3009I を合わせ、追跡名は展開検査追跡です。誤答側の問題点を分けます。 A: 展開検査不足は名称や説明だけに寄り、判定名は展開検査不足です。 B: 展開検査正答は対象出力と項目説明を結び、根拠名は展開検査正答です。 C: 展開検査欠落は戻り値や記録番号に寄り、欠落名は展開検査欠落です。 D: 展開検査流用は別カテゴリの確認であり、排除名は展開検査流用です。展開検査初出では VOLCATALOG (テープ)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開検査初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>VOLCATALOG (テープ)</strong></p><p>検証目的: 警告追跡のテープについて、VOLCATALOG (テープ)は、DFSMS / IDCAMS / VSAM の DEFINE_CATALOG で機能名、見出し、または確認対象として参照する項目です。関連するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010057の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、警告追跡のテープの確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にVOLCATALOG (テープ)を指定し、OSKB010057の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND VOLCATALOG (テープ)
CASE OSKB010057
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM VOLCATALOG (テープ)
CASE OSKB010057
SOURCE DFSMS
VOLCATALOG (テープ)とOSKB010057が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010057を同じ出力で読み、警告追跡のテープの根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010057
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010057.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010057が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の VOLCATALOG (テープ) と OSKB010057 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010057 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## DEFINE_CLUSTER


<section class="kb-item" id="c06-i0039"><h3>ATTEMPTS(n)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>ATTEMPTS(n)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域照合のストレージ管理に関する ATTEMPTS(n)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず値域照合のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域照合のストレージ管理の証跡として保存して根拠にする。</li><li>C. ATTEMPTS(n)の変更点を出力本文から切り離して値域照合のストレージ管理の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC3009I を読み、値域照合の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域照合正解では選択記号 D を採用し、正解名は値域照合正解です。値域照合根拠では ATTEMPTS(n) は「ATTEMPTS(n)の状態と出力メッセージを結び付ける値域照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は値域照合根拠です。値域照合保存では ATTEMPTS(n)の出力行と IDC3009I を一緒に残し、保存名は値域照合保存です。選択肢ごとの違いを示します。 A: 値域照合欠落は戻り値や記録番号に寄り、欠落名は値域照合欠落です。 B: 値域照合流用は別カテゴリの確認であり、排除名は値域照合流用です。 C: 値域照合不足は名称や説明だけに寄り、判定名は値域照合不足です。 D: 値域照合正答は対象出力と項目説明を結び、根拠名は値域照合正答です。値域照合対象では ATTEMPTS(n)を DFSMS の確認記録に残し、対象名は値域照合対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>ATTEMPTS(n)</strong></p><p>検証目的: 出力確認のストレージ管理について、ATTEMPTS(n)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030008の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、出力確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にATTEMPTS(n)を指定し、OSKB030008の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ATTEMPTS(n)
CASE OSKB030008
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ATTEMPTS(n)
CASE OSKB030008
SOURCE DFSMS
ATTEMPTS(n)とOSKB030008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030008を同じ出力で読み、出力確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030008
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030008.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の ATTEMPTS(n) と OSKB030008 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>ATTEMPTS(n)</strong></p><p>検証目的: 範囲照合のストレージ管理について、ATTEMPTS(n)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010031の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、範囲照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にATTEMPTS(n)を指定し、OSKB010031の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ATTEMPTS(n)
CASE OSKB010031
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ATTEMPTS(n)
CASE OSKB010031
SOURCE DFSMS
ATTEMPTS(n)とOSKB010031が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010031を同じ出力で読み、範囲照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010031
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010031.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010031が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の ATTEMPTS(n) と OSKB010031 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010031 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0040"><h3>AUTHORIZATION(modname [str])</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>AUTHORIZATION(modname [str])は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで認証、権限、またはセキュリティ設定を確認する項目です。ユーザ認可ルーチン名と任意の文字列パラメータ。旧式の独自認可機構で SAF/RACF に置換済み。「AUTHORIZATION(modname [str])」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告照合の[に関係する AUTHORIZATION 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、警告照合の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. AUTHORIZATION 属性の名称と担当者名だけを残して警告照合の[の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で警告照合の[を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず警告照合の[の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告照合正解では選択記号 A を採用し、正解名は警告照合正解です。警告照合根拠では AUTHORIZATION 属性 は「AUTHORIZATION 属性の用途をストレージ管理の表示で確認する警告照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は警告照合根拠です。警告照合背景では DFSMS の AUTHORIZATION 属性と IDC3009I を同じ証跡に残し、背景名は警告照合背景です。他の選択肢を確認します。 A: 警告照合正答は対象出力と項目説明を結び、根拠名は警告照合正答です。 B: 警告照合不足は名称や説明だけに寄り、判定名は警告照合不足です。 C: 警告照合流用は別カテゴリの確認であり、排除名は警告照合流用です。 D: 警告照合欠落は戻り値や記録番号に寄り、欠落名は警告照合欠落です。警告照合用語では AUTHORIZATION 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告照合用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AUTHORIZATION(modname [str])</strong></p><p>検証目的: 優先照合の[について、AUTHORIZATION(modname [str])は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で認証、権限、またはセキュリティ設定を確に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010032の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、優先照合の[の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にAUTHORIZATION(modnを指定し、OSKB010032の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND AUTHORIZATION(modn
CASE OSKB010032
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM AUTHORIZATION(modn
CASE OSKB010032
SOURCE DFSMS
AUTHORIZATION(modnとOSKB010032が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010032を同じ出力で読み、優先照合の[の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010032
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010032.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010032が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の AUTHORIZATION(modn と OSKB010032 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010032 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0041"><h3>BUFFERSPACE(n)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>BUFFERSPACE(n)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序確認のストレージ管理でストレージ管理の運用確認を行います。BUFFERSPACE(n)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で順序確認のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず順序確認のストレージ管理を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. BUFFERSPACE(n)の属性行を読まず順序確認のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序確認正解では選択記号 C を採用し、正解名は順序確認正解です。順序確認根拠では BUFFERSPACE(n) は「DFSMS で BUFFERSPACE(n)の扱いを記録する順序確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は順序確認根拠です。順序確認受渡では BUFFERSPACE(n)の表示結果と IDC3009I を同じ確認単位にし、受渡名は順序確認受渡です。不適切な選択肢を整理します。 A: 順序確認流用は別カテゴリの確認であり、排除名は順序確認流用です。 B: 順序確認欠落は戻り値や記録番号に寄り、欠落名は順序確認欠落です。 C: 順序確認正答は対象出力と項目説明を結び、根拠名は順序確認正答です。 D: 順序確認不足は名称や説明だけに寄り、判定名は順序確認不足です。順序確認資料では BUFFERSPACE(n)の使い方を出典欄から追跡し、資料名は順序確認資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 比較検査のストレージ管理で BUFFERSPACE(n)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. BUFFERSPACE(n)の出力を取らず比較検査のストレージ管理の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、比較検査として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して比較検査のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較検査のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較検査正解では選択記号 B を採用し、正解名は比較検査正解です。比較検査根拠では BUFFERSPACE(n) は「比較検査のストレージ管理に関係する定義値と表示行を照合する比較検査項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は比較検査根拠です。比較検査追跡では BUFFERSPACE(n)の属性行と IDC0001I を合わせ、追跡名は比較検査追跡です。誤答側の問題点を分けます。 A: 比較検査不足は名称や説明だけに寄り、判定名は比較検査不足です。 B: 比較検査正答は対象出力と項目説明を結び、根拠名は比較検査正答です。 C: 比較検査欠落は戻り値や記録番号に寄り、欠落名は比較検査欠落です。 D: 比較検査流用は別カテゴリの確認であり、排除名は比較検査流用です。比較検査初出では BUFFERSPACE(n)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較検査初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>BUFFERSPACE(n)</strong></p><p>検証目的: 区切確認のストレージ管理について、BUFFERSPACE(n)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010010の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、区切確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にBUFFERSPACE(n)を指定し、OSKB010010の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND BUFFERSPACE(n)
CASE OSKB010010
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM BUFFERSPACE(n)
CASE OSKB010010
SOURCE DFSMS
BUFFERSPACE(n)とOSKB010010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010010を同じ出力で読み、区切確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010010
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010010.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の BUFFERSPACE(n) と OSKB010010 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>BUFFERSPACE(n)</strong></p><p>検証目的: 条件検査のストレージ管理について、BUFFERSPACE(n)は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010069の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、条件検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にBUFFERSPACE(n)を指定し、OSKB010069の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND BUFFERSPACE(n)
CASE OSKB010069
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM BUFFERSPACE(n)
CASE OSKB010069
SOURCE DFSMS
BUFFERSPACE(n)とOSKB010069が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010069を同じ出力で読み、条件検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010069
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010069.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010069が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の BUFFERSPACE(n) と OSKB010069 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010069 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0042"><h3>CATALOG(catname)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>CATALOG(catname)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで確認する項目です。登録先カタログを明示指定。省略時は STEPCAT/JOBCAT/マスターまたは ICF カタログ環境の標準解決順</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序照合のストレージ管理でストレージ管理の運用確認を行います。CATALOG(catname)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で順序照合のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず順序照合のストレージ管理を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて順序照合の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. CATALOG(catname)の属性行を読まず順序照合のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序照合正解では選択記号 C を採用し、正解名は順序照合正解です。順序照合根拠では CATALOG(catname) は「DFSMS で CATALOG(catname)の扱いを記録する順序照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は順序照合根拠です。順序照合受渡では CATALOG(catname)の表示結果と IDC3009I を同じ確認単位にし、受渡名は順序照合受渡です。不適切な選択肢を整理します。 A: 順序照合流用は別カテゴリの確認であり、排除名は順序照合流用です。 B: 順序照合欠落は戻り値や記録番号に寄り、欠落名は順序照合欠落です。 C: 順序照合正答は対象出力と項目説明を結び、根拠名は順序照合正答です。 D: 順序照合不足は名称や説明だけに寄り、判定名は順序照合不足です。順序照合資料では CATALOG(catname)の使い方を出典欄から追跡し、資料名は順序照合資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索整理のストレージ管理で CATALOG(catname)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. CATALOG(catname)の出力を取らず探索整理のストレージ管理の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、探索整理の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して探索整理のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索整理のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索整理正解では選択記号 B を採用し、正解名は探索整理正解です。探索整理根拠では CATALOG(catname) は「探索整理のストレージ管理に関係する定義値と表示行を照合する探索整理項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は探索整理根拠です。探索整理追跡では CATALOG(catname)の属性行と IDC3009I を合わせ、追跡名は探索整理追跡です。誤答側の問題点を分けます。 A: 探索整理不足は名称や説明だけに寄り、判定名は探索整理不足です。 B: 探索整理正答は対象出力と項目説明を結び、根拠名は探索整理正答です。 C: 探索整理欠落は戻り値や記録番号に寄り、欠落名は探索整理欠落です。 D: 探索整理流用は別カテゴリの確認であり、排除名は探索整理流用です。探索整理初出では CATALOG(catname)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索整理初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（3件）</summary><div class="kb-p"><p class="kb-pname"><strong>CATALOG(catname)</strong></p><p>検証目的: 展開照合のストレージ管理について、CATALOG(catname)は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。問い合わせ先カタログをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030022の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、展開照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCATALOG(catname)を指定し、OSKB030022の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND CATALOG(catname)
CASE OSKB030022
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM CATALOG(catname)
CASE OSKB030022
SOURCE DFSMS
CATALOG(catname)とOSKB030022が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030022を同じ出力で読み、展開照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030022
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030022.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030022が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の CATALOG(catname) と OSKB030022 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>CATALOG(catname)</strong></p><p>検証目的: 区切照合のストレージ管理について、CATALOG(catname)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で確認する項目です。登録先カタログを明示指定。省略時は STEPに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010030の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、区切照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCATALOG(catname)を指定し、OSKB010030の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND CATALOG(catname)
CASE OSKB010030
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM CATALOG(catname)
CASE OSKB010030
SOURCE DFSMS
CATALOG(catname)とOSKB010030が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010030を同じ出力で読み、区切照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010030
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010030.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010030が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の CATALOG(catname) と OSKB010030 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>CATALOG(catname)</strong></p><p>検証目的: 構文整理のストレージ管理について、CATALOG(catname)は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。問い合わせ先カタログをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010101の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、構文整理のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCATALOG(catname)を指定し、OSKB010101の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND CATALOG(catname)
CASE OSKB010101
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM CATALOG(catname)
CASE OSKB010101
SOURCE DFSMS
CATALOG(catname)とOSKB010101が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010101を同じ出力で読み、構文整理のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010101
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010101.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010101が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の CATALOG(catname) と OSKB010101 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010101 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0043"><h3>CISZ の選択指針</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>CISZ の選択指針は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで確認する項目です。ランダム多用なら小さめ (バッファ多めに乗る)、順次多用なら大きめ (I/O 回数削減)。一般に 4KB〜18KB が現実的</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較確認の選択指針で CISZ の選択指針の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. CISZ の選択指針の出力を取らず比較確認の選択指針の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、比較確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して比較確認の選択指針の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較確認の選択指針へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較確認正解では選択記号 B を採用し、正解名は比較確認正解です。比較確認根拠では CISZ の選択指針 は「比較確認の選択指針に関係する定義値と表示行を照合する比較確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は比較確認根拠です。比較確認追跡では CISZ の選択指針の属性行と IDC3009I を合わせ、追跡名は比較確認追跡です。誤答側の問題点を分けます。 A: 比較確認不足は名称や説明だけに寄り、判定名は比較確認不足です。 B: 比較確認正答は対象出力と項目説明を結び、根拠名は比較確認正答です。 C: 比較確認欠落は戻り値や記録番号に寄り、欠落名は比較確認欠落です。 D: 比較確認流用は別カテゴリの確認であり、排除名は比較確認流用です。比較確認初出では CISZ の選択指針を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較確認初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CISZ の選択指針</strong></p><p>検証目的: 条件確認のの選択指針について、CISZ の選択指針は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で確認する項目です。ランダム多用なら小さめ (バッファ多めに乗る)、順次多用に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010009の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、条件確認のの選択指針の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCISZ の選択指針を指定し、OSKB010009の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND CISZ の選択指針
CASE OSKB010009
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM CISZ の選択指針
CASE OSKB010009
SOURCE DFSMS
CISZ の選択指針とOSKB010009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010009を同じ出力で読み、条件確認のの選択指針の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010009
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010009.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の CISZ の選択指針 と OSKB010009 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0044"><h3>CODE(code)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>CODE(code)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧照合のストレージ管理で CODE(code)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. CODE(code)の出力を取らず復旧照合のストレージ管理の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、復旧照合として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して復旧照合のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧照合のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧照合正解では選択記号 B を採用し、正解名は復旧照合正解です。復旧照合根拠では CODE(code) は「復旧照合のストレージ管理に関係する定義値と表示行を照合する復旧照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は復旧照合根拠です。復旧照合追跡では CODE(code)の属性行と IDC3009I を合わせ、追跡名は復旧照合追跡です。誤答側の問題点を分けます。 A: 復旧照合不足は名称や説明だけに寄り、判定名は復旧照合不足です。 B: 復旧照合正答は対象出力と項目説明を結び、根拠名は復旧照合正答です。 C: 復旧照合欠落は戻り値や記録番号に寄り、欠落名は復旧照合欠落です。 D: 復旧照合流用は別カテゴリの確認であり、排除名は復旧照合流用です。復旧照合初出では CODE(code)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧照合初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CODE(code)</strong></p><p>検証目的: 記録照合のストレージ管理について、CODE(code)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010033の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、記録照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCODE(code)を指定し、OSKB010033の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND CODE(code)
CASE OSKB010033
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM CODE(code)
CASE OSKB010033
SOURCE DFSMS
CODE(code)とOSKB010033が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010033を同じ出力で読み、記録照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010033
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010033.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010033が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の CODE(code) と OSKB010033 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010033 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0045"><h3>CONTROLINTERVALSIZE / CISZ(n)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>CONTROLINTERVALSIZE / CISZ(n)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。制御区間サイズ (バイト)。512 の倍数 (≤8KB) または 2KB の倍数 (≤32KB)。LDS は 4096 固定。省略時はシステム最適化</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録確認の・に関係する CONTROLINTERVALSIZE 機能の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、記録確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. CONTROLINTERVALSIZE 機能の名称と担当者名だけを残して記録確認の・の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で記録確認の・を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず記録確認の・の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録確認正解では選択記号 A を採用し、正解名は記録確認正解です。記録確認根拠では CONTROLINTERVALSIZE 機能 は「CONTROLINTERVALSIZE 機能の用途をストレージ管理の表示で確認する記録確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は記録確認根拠です。記録確認背景では DFSMS の CONTROLINTERVALSIZE 機能と IDC3009I を同じ証跡に残し、背景名は記録確認背景です。他の選択肢を確認します。 A: 記録確認正答は対象出力と項目説明を結び、根拠名は記録確認正答です。 B: 記録確認不足は名称や説明だけに寄り、判定名は記録確認不足です。 C: 記録確認流用は別カテゴリの確認であり、排除名は記録確認流用です。 D: 記録確認欠落は戻り値や記録番号に寄り、欠落名は記録確認欠落です。記録確認用語では CONTROLINTERVALSIZE 機能を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録確認用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CONTROLINTERVALSIZE ・ CISZ(n)</strong></p><p>検証目的: 出力確認の・について、CONTROLINTERVALSIZE / CISZ(n)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象としてに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010008の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、出力確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCONTROLINTERVALSIZを指定し、OSKB010008の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND CONTROLINTERVALSIZ
CASE OSKB010008
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM CONTROLINTERVALSIZ
CASE OSKB010008
SOURCE DFSMS
CONTROLINTERVALSIZとOSKB010008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010008を同じ出力で読み、出力確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010008
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010008.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の CONTROLINTERVALSIZ と OSKB010008 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0046"><h3>CONTROLPW / MASTERPW / UPDATEPW / READPW</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>CONTROLPW / MASTERPW / UPDATEPW / READPWは、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで確認する項目です。操作レベル別の旧式パスワード (制御/マスター/更新/読取)。RACF データセットプロファイルに完全置換され、現行では使用しない</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査照合の・ ・でストレージ管理の運用確認を行います。CONTROLPW 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で監査照合の・ ・を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず監査照合の・ ・を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査照合の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. CONTROLPW 属性の属性行を読まず監査照合の・ ・の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査照合正解では選択記号 C を採用し、正解名は監査照合正解です。監査照合根拠では CONTROLPW 属性 は「DFSMS で CONTROLPW 属性の扱いを記録する監査照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は監査照合根拠です。監査照合受渡では CONTROLPW 属性の表示結果と IDC3009I を同じ確認単位にし、受渡名は監査照合受渡です。不適切な選択肢を整理します。 A: 監査照合流用は別カテゴリの確認であり、排除名は監査照合流用です。 B: 監査照合欠落は戻り値や記録番号に寄り、欠落名は監査照合欠落です。 C: 監査照合正答は対象出力と項目説明を結び、根拠名は監査照合正答です。 D: 監査照合不足は名称や説明だけに寄り、判定名は監査照合不足です。監査照合資料では CONTROLPW 属性の使い方を出典欄から追跡し、資料名は監査照合資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details></section>


<section class="kb-item" id="c06-i0047"><h3>CYLINDERS(p s)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>CYLINDERS(p s)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換照合のストレージ管理に関する CYLINDERS(p s)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず置換照合のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換照合のストレージ管理の証跡として保存して根拠にする。</li><li>C. CYLINDERS(p s)の変更点を出力本文から切り離して置換照合のストレージ管理の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC3009I を読み、置換照合の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換照合正解では選択記号 D を採用し、正解名は置換照合正解です。置換照合根拠では CYLINDERS(p s) は「CYLINDERS(p s)の状態と出力メッセージを結び付ける置換照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は置換照合根拠です。置換照合保存では CYLINDERS(p s)の出力行と IDC3009I を一緒に残し、保存名は置換照合保存です。選択肢ごとの違いを示します。 A: 置換照合欠落は戻り値や記録番号に寄り、欠落名は置換照合欠落です。 B: 置換照合流用は別カテゴリの確認であり、排除名は置換照合流用です。 C: 置換照合不足は名称や説明だけに寄り、判定名は置換照合不足です。 D: 置換照合正答は対象出力と項目説明を結び、根拠名は置換照合正答です。置換照合対象では CYLINDERS(p s)を DFSMS の確認記録に残し、対象名は置換照合対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CYLINDERS(p s)</strong></p><p>検証目的: 監査確認のストレージ管理について、CYLINDERS(p s)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010019の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、監査確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCYLINDERS(p s)を指定し、OSKB010019の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND CYLINDERS(p s)
CASE OSKB010019
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM CYLINDERS(p s)
CASE OSKB010019
SOURCE DFSMS
CYLINDERS(p s)とOSKB010019が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010019を同じ出力で読み、監査確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010019
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010019.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010019が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の CYLINDERS(p s) と OSKB010019 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010019 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0048"><h3>DATACLAS(name)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>SMS データクラスを明示指定。RECFM/LRECL/SPACE/VSAM 属性のテンプレート。明示属性指定はデータクラスを上書きする</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先照合のストレージ管理に関する DATACLAS(name)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず優先照合のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先照合のストレージ管理の証跡として保存して根拠にする。</li><li>C. DATACLAS(name)の変更点を出力本文から切り離して優先照合のストレージ管理の承認欄だけ残す。</li><li>D. IDC3009I を含む表示を保存し、説明欄との差分を優先照合で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先照合正解では選択記号 D を採用し、正解名は優先照合正解です。優先照合根拠では DATACLAS(name) は「DATACLAS(name)の状態と出力メッセージを結び付ける優先照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は優先照合根拠です。優先照合保存では DATACLAS(name)の出力行と IDC3009I を一緒に残し、保存名は優先照合保存です。選択肢ごとの違いを示します。 A: 優先照合欠落は戻り値や記録番号に寄り、欠落名は優先照合欠落です。 B: 優先照合流用は別カテゴリの確認であり、排除名は優先照合流用です。 C: 優先照合不足は名称や説明だけに寄り、判定名は優先照合不足です。 D: 優先照合正答は対象出力と項目説明を結び、根拠名は優先照合正答です。優先照合対象では DATACLAS(name)を DFSMS の確認記録に残し、対象名は優先照合対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DATACLAS(name)</strong></p><p>検証目的: 上書照合のストレージ管理について、SMS データクラスを明示指定。RECFM/LRECL/SPACE/VSAM 属性のテンプレート。明示属性指定はデータクラスを上書きするに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010027の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、上書照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDATACLAS(name)を指定し、OSKB010027の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DATACLAS(name)
CASE OSKB010027
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DATACLAS(name)
CASE OSKB010027
SOURCE DFSMS
DATACLAS(name)とOSKB010027が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010027を同じ出力で読み、上書照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010027
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010027.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010027が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DATACLAS(name) と OSKB010027 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010027 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0049"><h3>DEFINE CLUSTER 基本構文</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>VSAM クラスター (DATA/INDEX の論理単位) を ICF カタログに登録する IDCAMS コマンド。CLUSTER, DATA, INDEX の 3 レベルで属性を指定する</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文確認の基本構文に関係する DEFINE CLUSTER 基本構文の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、構文確認の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. DEFINE CLUSTER 基本構文の名称と担当者名だけを残して構文確認の基本構文の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で構文確認の基本構文を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず構文確認の基本構文の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文確認正解では選択記号 A を採用し、正解名は構文確認正解です。構文確認根拠では DEFINE CLUSTER 基本構文 は「DEFINE CLUSTER 基本構文の用途をストレージ管理の表示で確認する構文確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は構文確認根拠です。構文確認背景では DFSMS の DEFINE CLUSTER 基本構文と IDC3009I を同じ証跡に残し、背景名は構文確認背景です。他の選択肢を確認します。 A: 構文確認正答は対象出力と項目説明を結び、根拠名は構文確認正答です。 B: 構文確認不足は名称や説明だけに寄り、判定名は構文確認不足です。 C: 構文確認流用は別カテゴリの確認であり、排除名は構文確認流用です。 D: 構文確認欠落は戻り値や記録番号に寄り、欠落名は構文確認欠落です。構文確認用語では DEFINE CLUSTER 基本構文を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文確認用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEFINE CLUSTER 基本構文</strong></p><p>検証目的: 構文確認の基本構文について、VSAM クラスター (DATA/INDEX の論理単位) を ICF カタログに登録する IDCAMS コマンド。CLUSTER, DATA, INDEX の 3 レベルに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030001の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、構文確認の基本構文の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDEFINE CLUSTER 基本構を指定し、OSKB030001の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DEFINE CLUSTER 基本構
CASE OSKB030001
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DEFINE CLUSTER 基本構
CASE OSKB030001
SOURCE DFSMS
DEFINE CLUSTER 基本構とOSKB030001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030001を同じ出力で読み、構文確認の基本構文の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030001
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030001.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DEFINE CLUSTER 基本構 と OSKB030001 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0050"><h3>EXCEPTIONEXIT(modname)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>EXCEPTIONEXIT(modname)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出照合のストレージ管理でストレージ管理の運用確認を行います。EXCEPTIONEXIT 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で呼出照合のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず呼出照合のストレージ管理を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて呼出照合の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. EXCEPTIONEXIT 属性の属性行を読まず呼出照合のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出照合正解では選択記号 C を採用し、正解名は呼出照合正解です。呼出照合根拠では EXCEPTIONEXIT 属性 は「DFSMS で EXCEPTIONEXIT 属性の扱いを記録する呼出照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は呼出照合根拠です。呼出照合受渡では EXCEPTIONEXIT 属性の表示結果と IDC3009I を同じ確認単位にし、受渡名は呼出照合受渡です。不適切な選択肢を整理します。 A: 呼出照合流用は別カテゴリの確認であり、排除名は呼出照合流用です。 B: 呼出照合欠落は戻り値や記録番号に寄り、欠落名は呼出照合欠落です。 C: 呼出照合正答は対象出力と項目説明を結び、根拠名は呼出照合正答です。 D: 呼出照合不足は名称や説明だけに寄り、判定名は呼出照合不足です。呼出照合資料では EXCEPTIONEXIT 属性の使い方を出典欄から追跡し、資料名は呼出照合資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EXCEPTIONEXIT(modname)</strong></p><p>検証目的: 復旧確認のストレージ管理について、EXCEPTIONEXIT(modname)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目でに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010018の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、復旧確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にEXCEPTIONEXIT(modnを指定し、OSKB010018の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND EXCEPTIONEXIT(modn
CASE OSKB010018
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM EXCEPTIONEXIT(modn
CASE OSKB010018
SOURCE DFSMS
EXCEPTIONEXIT(modnとOSKB010018が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010018を同じ出力で読み、復旧確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010018
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010018.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010018が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の EXCEPTIONEXIT(modn と OSKB010018 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010018 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0051"><h3>FREESPACE(ci% ca%)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>FREESPACE(ci% ca%)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。CI 内および CA 内に確保する空き率 (%)。挿入を見込む KSDS では 10〜20% 程度が典型。両方 0 は静的データ向け。「FREESPACE(ci% ca%)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域確認の% %に関する FREESPACE(ci% ca%)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず値域確認の% %の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域確認の% %の証跡として保存して根拠にする。</li><li>C. FREESPACE(ci% ca%)の変更点を出力本文から切り離して値域確認の% %の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、値域確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域確認正解では選択記号 D を採用し、正解名は値域確認正解です。値域確認根拠では FREESPACE(ci% ca%) は「FREESPACE(ci% ca%)の状態と出力メッセージを結び付ける値域確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は値域確認根拠です。値域確認保存では FREESPACE(ci% ca%)の出力行と IDC3009I を一緒に残し、保存名は値域確認保存です。選択肢ごとの違いを示します。 A: 値域確認欠落は戻り値や記録番号に寄り、欠落名は値域確認欠落です。 B: 値域確認流用は別カテゴリの確認であり、排除名は値域確認流用です。 C: 値域確認不足は名称や説明だけに寄り、判定名は値域確認不足です。 D: 値域確認正答は対象出力と項目説明を結び、根拠名は値域確認正答です。値域確認対象では FREESPACE(ci% ca%)を DFSMS の確認記録に残し、対象名は値域確認対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 優先検査の% %に関する FREESPACE(ci% ca%)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず優先検査の% %の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先検査の% %の証跡として保存して根拠にする。</li><li>C. FREESPACE(ci% ca%)の変更点を出力本文から切り離して優先検査の% %の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC0001I を読み、優先検査の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先検査正解では選択記号 D を採用し、正解名は優先検査正解です。優先検査根拠では FREESPACE(ci% ca%) は「FREESPACE(ci% ca%)の状態と出力メッセージを結び付ける優先検査項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は優先検査根拠です。優先検査保存では FREESPACE(ci% ca%)の出力行と IDC0001I を一緒に残し、保存名は優先検査保存です。選択肢ごとの違いを示します。 A: 優先検査欠落は戻り値や記録番号に寄り、欠落名は優先検査欠落です。 B: 優先検査流用は別カテゴリの確認であり、排除名は優先検査流用です。 C: 優先検査不足は名称や説明だけに寄り、判定名は優先検査不足です。 D: 優先検査正答は対象出力と項目説明を結び、根拠名は優先検査正答です。優先検査対象では FREESPACE(ci% ca%)を DFSMS の確認記録に残し、対象名は優先検査対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（3件）</summary><div class="kb-p"><p class="kb-pname"><strong>FREESPACE(ci% ca%)</strong></p><p>検証目的: 置換確認の% %について、FREESPACE(ci% ca%)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。CIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030004の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、置換確認の% %の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にFREESPACE(ci% ca%)を指定し、OSKB030004の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND FREESPACE(ci% ca%)
CASE OSKB030004
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM FREESPACE(ci% ca%)
CASE OSKB030004
SOURCE DFSMS
FREESPACE(ci% ca%)とOSKB030004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030004を同じ出力で読み、置換確認の% %の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030004
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030004.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の FREESPACE(ci% ca%) と OSKB030004 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>FREESPACE(ci% ca%)</strong></p><p>検証目的: 範囲確認の% %について、FREESPACE(ci% ca%)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。CIに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010011の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、範囲確認の% %の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にFREESPACE(ci% ca%)を指定し、OSKB010011の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND FREESPACE(ci% ca%)
CASE OSKB010011
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM FREESPACE(ci% ca%)
CASE OSKB010011
SOURCE DFSMS
FREESPACE(ci% ca%)とOSKB010011が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010011を同じ出力で読み、範囲確認の% %の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010011
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010011.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010011が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の FREESPACE(ci% ca%) と OSKB010011 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010011 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>FREESPACE(ci% ca%)</strong></p><p>検証目的: 上書検査の% %について、FREESPACE(ci% ca%)は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010067の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、上書検査の% %の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にFREESPACE(ci% ca%)を指定し、OSKB010067の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND FREESPACE(ci% ca%)
CASE OSKB010067
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM FREESPACE(ci% ca%)
CASE OSKB010067
SOURCE DFSMS
FREESPACE(ci% ca%)とOSKB010067が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010067を同じ出力で読み、上書検査の% %の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010067
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010067.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010067が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の FREESPACE(ci% ca%) と OSKB010067 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010067 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0052"><h3>IMBED (廃止)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>IMBED (廃止)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更確認の廃止に関する IMBED (廃止)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず変更確認の廃止の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更確認の廃止の証跡として保存して根拠にする。</li><li>C. IMBED (廃止)の変更点を出力本文から切り離して変更確認の廃止の承認欄だけ残す。</li><li>D. IDC3009I を含む表示を保存し、説明欄との差分を変更確認で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更確認正解では選択記号 D を採用し、正解名は変更確認正解です。変更確認根拠では IMBED (廃止) は「IMBED (廃止)の状態と出力メッセージを結び付ける変更確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は変更確認根拠です。変更確認保存では IMBED (廃止)の出力行と IDC3009I を一緒に残し、保存名は変更確認保存です。選択肢ごとの違いを示します。 A: 変更確認欠落は戻り値や記録番号に寄り、欠落名は変更確認欠落です。 B: 変更確認流用は別カテゴリの確認であり、排除名は変更確認流用です。 C: 変更確認不足は名称や説明だけに寄り、判定名は変更確認不足です。 D: 変更確認正答は対象出力と項目説明を結び、根拠名は変更確認正答です。変更確認対象では IMBED (廃止)を DFSMS の確認記録に残し、対象名は変更確認対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMBED (廃止)</strong></p><p>検証目的: 順序確認の廃止について、IMBED (廃止)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010015の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、順序確認の廃止の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にIMBED (廃止)を指定し、OSKB010015の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND IMBED (廃止)
CASE OSKB010015
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM IMBED (廃止)
CASE OSKB010015
SOURCE DFSMS
IMBED (廃止)とOSKB010015が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010015を同じ出力で読み、順序確認の廃止の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010015
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010015.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010015が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の IMBED (廃止) と OSKB010015 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010015 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0053"><h3>INDEXED (KSDS)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>INDEXED (KSDS)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。Key-Sequenced Data Set を指定。キー順インデックス + データの構成で、ランダム/順次アクセス両対応。VSAM 既定。「INDEXED (KSDS)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換確認のストレージ管理に関する INDEXED (KSDS)の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず置換確認のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換確認のストレージ管理の証跡として保存して根拠にする。</li><li>C. INDEXED (KSDS)の変更点を出力本文から切り離して置換確認のストレージ管理の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、置換確認の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換確認正解では選択記号 D を採用し、正解名は置換確認正解です。置換確認根拠では INDEXED (KSDS) は「INDEXED (KSDS)の状態と出力メッセージを結び付ける置換確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は置換確認根拠です。置換確認保存では INDEXED (KSDS)の出力行と IDC3009I を一緒に残し、保存名は置換確認保存です。選択肢ごとの違いを示します。 A: 置換確認欠落は戻り値や記録番号に寄り、欠落名は置換確認欠落です。 B: 置換確認流用は別カテゴリの確認であり、排除名は置換確認流用です。 C: 置換確認不足は名称や説明だけに寄り、判定名は置換確認不足です。 D: 置換確認正答は対象出力と項目説明を結び、根拠名は置換確認正答です。置換確認対象では INDEXED (KSDS)を DFSMS の確認記録に残し、対象名は置換確認対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details></section>


<section class="kb-item" id="c06-i0054"><h3>KEYS(length offset)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>KEYS(length offset)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。KSDS / AIX のキー長と、レコード先頭からのオフセットを指定。length+offset は RECORDSIZE 最小値以下である必要</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先確認のストレージ管理に関する KEYS 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず優先確認のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先確認のストレージ管理の証跡として保存して根拠にする。</li><li>C. KEYS 属性の変更点を出力本文から切り離して優先確認のストレージ管理の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC3009I を読み、優先確認の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先確認正解では選択記号 D を採用し、正解名は優先確認正解です。優先確認根拠では KEYS 属性 は「KEYS 属性の状態と出力メッセージを結び付ける優先確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は優先確認根拠です。優先確認保存では KEYS 属性の出力行と IDC3009I を一緒に残し、保存名は優先確認保存です。選択肢ごとの違いを示します。 A: 優先確認欠落は戻り値や記録番号に寄り、欠落名は優先確認欠落です。 B: 優先確認流用は別カテゴリの確認であり、排除名は優先確認流用です。 C: 優先確認不足は名称や説明だけに寄り、判定名は優先確認不足です。 D: 優先確認正答は対象出力と項目説明を結び、根拠名は優先確認正答です。優先確認対象では KEYS 属性を DFSMS の確認記録に残し、対象名は優先確認対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>KEYS(length offset)</strong></p><p>検証目的: 上書確認のストレージ管理について、KEYS(length offset)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。Kに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010007の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、上書確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にKEYS(length offsetを指定し、OSKB010007の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND KEYS(length offset
CASE OSKB010007
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM KEYS(length offset
CASE OSKB010007
SOURCE DFSMS
KEYS(length offsetとOSKB010007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010007を同じ出力で読み、上書確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010007
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010007.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の KEYS(length offset と OSKB010007 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0055"><h3>LINEAR (LDS)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>LINEAR (LDS)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。Linear Data Set。レコード境界を持たない 4KB CI のバイト列。Data-in-Virtual (DIV) や DB2 表領域で使用</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書確認のストレージ管理でストレージ管理の運用確認を行います。LINEAR (LDS)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で上書確認のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず上書確認のストレージ管理を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて上書確認の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. LINEAR (LDS)の属性行を読まず上書確認のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書確認正解では選択記号 C を採用し、正解名は上書確認正解です。上書確認根拠では LINEAR (LDS) は「DFSMS で LINEAR (LDS)の扱いを記録する上書確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は上書確認根拠です。上書確認受渡では LINEAR (LDS)の表示結果と IDC3009I を同じ確認単位にし、受渡名は上書確認受渡です。不適切な選択肢を整理します。 A: 上書確認流用は別カテゴリの確認であり、排除名は上書確認流用です。 B: 上書確認欠落は戻り値や記録番号に寄り、欠落名は上書確認欠落です。 C: 上書確認正答は対象出力と項目説明を結び、根拠名は上書確認正答です。 D: 上書確認不足は名称や説明だけに寄り、判定名は上書確認不足です。上書確認資料では LINEAR (LDS)の使い方を出典欄から追跡し、資料名は上書確認資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LINEAR (LDS)</strong></p><p>検証目的: 展開確認のストレージ管理について、LINEAR (LDS)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。Linear Dに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010002の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、展開確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にLINEAR (LDS)を指定し、OSKB010002の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND LINEAR (LDS)
CASE OSKB010002
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM LINEAR (LDS)
CASE OSKB010002
SOURCE DFSMS
LINEAR (LDS)とOSKB010002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010002を同じ出力で読み、展開確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010002
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010002.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の LINEAR (LDS) と OSKB010002 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0056"><h3>MGMTCLAS(name)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>MGMTCLAS(name)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切照合のストレージ管理で MGMTCLAS(name)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. MGMTCLAS(name)の出力を取らず区切照合のストレージ管理の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、区切照合の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して区切照合のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切照合のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切照合正解では選択記号 B を採用し、正解名は区切照合正解です。区切照合根拠では MGMTCLAS(name) は「区切照合のストレージ管理に関係する定義値と表示行を照合する区切照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は区切照合根拠です。区切照合追跡では MGMTCLAS(name)の属性行と IDC3009I を合わせ、追跡名は区切照合追跡です。誤答側の問題点を分けます。 A: 区切照合不足は名称や説明だけに寄り、判定名は区切照合不足です。 B: 区切照合正答は対象出力と項目説明を結び、根拠名は区切照合正答です。 C: 区切照合欠落は戻り値や記録番号に寄り、欠落名は区切照合欠落です。 D: 区切照合流用は別カテゴリの確認であり、排除名は区切照合流用です。区切照合初出では MGMTCLAS(name)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切照合初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MGMTCLAS(name)</strong></p><p>検証目的: 終端照合のストレージ管理について、MGMTCLAS(name)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010025の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、終端照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にMGMTCLAS(name)を指定し、OSKB010025の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND MGMTCLAS(name)
CASE OSKB010025
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM MGMTCLAS(name)
CASE OSKB010025
SOURCE DFSMS
MGMTCLAS(name)とOSKB010025が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010025を同じ出力で読み、終端照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010025
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010025.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010025が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の MGMTCLAS(name) と OSKB010025 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010025 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0057"><h3>MODEL(entryname)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>MODEL(entryname)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERでリソース定義、モデル、またはポリシーを読むための項目です。対象リソース、依存関係、変更が反映される範囲を確認してから扱います。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書照合のストレージ管理でストレージ管理の運用確認を行います。MODEL(entryname)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で上書照合のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず上書照合のストレージ管理を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書照合の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. MODEL(entryname)の属性行を読まず上書照合のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書照合正解では選択記号 C を採用し、正解名は上書照合正解です。上書照合根拠では MODEL(entryname) は「DFSMS で MODEL(entryname)の扱いを記録する上書照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は上書照合根拠です。上書照合受渡では MODEL(entryname)の表示結果と IDC3009I を同じ確認単位にし、受渡名は上書照合受渡です。不適切な選択肢を整理します。 A: 上書照合流用は別カテゴリの確認であり、排除名は上書照合流用です。 B: 上書照合欠落は戻り値や記録番号に寄り、欠落名は上書照合欠落です。 C: 上書照合正答は対象出力と項目説明を結び、根拠名は上書照合正答です。 D: 上書照合不足は名称や説明だけに寄り、判定名は上書照合不足です。上書照合資料では MODEL(entryname)の使い方を出典欄から追跡し、資料名は上書照合資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MODEL(entryname)</strong></p><p>検証目的: 展開照合のストレージ管理について、MODEL(entryname)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER でリソース定義、モデル、またはポリシーを読むための項目です。対象に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010022の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、展開照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にMODEL(entryname)を指定し、OSKB010022の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND MODEL(entryname)
CASE OSKB010022
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM MODEL(entryname)
CASE OSKB010022
SOURCE DFSMS
MODEL(entryname)とOSKB010022が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010022を同じ出力で読み、展開照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010022
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010022.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010022が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の MODEL(entryname) と OSKB010022 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0058"><h3>NAME(entryname)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>NAME(entryname)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで確認する項目です。クラスターのエントリ名 (最大 44 文字)。DATA/INDEX レベルにも個別に NAME 指定可能。省略時はシステムが派生名を生成する</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開確認のストレージ管理で NAME(entryname)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. NAME(entryname)の出力を取らず展開確認のストレージ管理の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、展開確認として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して展開確認のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開確認のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開確認正解では選択記号 B を採用し、正解名は展開確認正解です。展開確認根拠では NAME(entryname) は「展開確認のストレージ管理に関係する定義値と表示行を照合する展開確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は展開確認根拠です。展開確認追跡では NAME(entryname)の属性行と IDC3009I を合わせ、追跡名は展開確認追跡です。誤答側の問題点を分けます。 A: 展開確認不足は名称や説明だけに寄り、判定名は展開確認不足です。 B: 展開確認正答は対象出力と項目説明を結び、根拠名は展開確認正答です。 C: 展開確認欠落は戻り値や記録番号に寄り、欠落名は展開確認欠落です。 D: 展開確認流用は別カテゴリの確認であり、排除名は展開確認流用です。展開確認初出では NAME(entryname)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開確認初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details></section>


<section class="kb-item" id="c06-i0059"><h3>NONINDEXED (ESDS)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>NONINDEXED (ESDS)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端確認のストレージ管理に関係する NONINDEXED (ESDS)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端確認で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. NONINDEXED (ESDS)の名称と担当者名だけを残して終端確認のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で終端確認のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず終端確認のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端確認正解では選択記号 A を採用し、正解名は終端確認正解です。終端確認根拠では NONINDEXED (ESDS) は「NONINDEXED (ESDS)の用途をストレージ管理の表示で確認する終端確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は終端確認根拠です。終端確認背景では DFSMS の NONINDEXED (ESDS)と IDC3009I を同じ証跡に残し、背景名は終端確認背景です。他の選択肢を確認します。 A: 終端確認正答は対象出力と項目説明を結び、根拠名は終端確認正答です。 B: 終端確認不足は名称や説明だけに寄り、判定名は終端確認不足です。 C: 終端確認流用は別カテゴリの確認であり、排除名は終端確認流用です。 D: 終端確認欠落は戻り値や記録番号に寄り、欠落名は終端確認欠落です。終端確認用語では NONINDEXED (ESDS)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端確認用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details></section>


<section class="kb-item" id="c06-i0060"><h3>NUMBERED (RRDS)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>NUMBERED (RRDS)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索確認のストレージ管理で NUMBERED (RRDS)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. NUMBERED (RRDS)の出力を取らず探索確認のストレージ管理の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、探索確認の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して探索確認のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索確認のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索確認正解では選択記号 B を採用し、正解名は探索確認正解です。探索確認根拠では NUMBERED (RRDS) は「探索確認のストレージ管理に関係する定義値と表示行を照合する探索確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は探索確認根拠です。探索確認追跡では NUMBERED (RRDS)の属性行と IDC3009I を合わせ、追跡名は探索確認追跡です。誤答側の問題点を分けます。 A: 探索確認不足は名称や説明だけに寄り、判定名は探索確認不足です。 B: 探索確認正答は対象出力と項目説明を結び、根拠名は探索確認正答です。 C: 探索確認欠落は戻り値や記録番号に寄り、欠落名は探索確認欠落です。 D: 探索確認流用は別カテゴリの確認であり、排除名は探索確認流用です。探索確認初出では NUMBERED (RRDS)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索確認初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>NUMBERED (RRDS)</strong></p><p>検証目的: 展開確認のストレージ管理について、NUMBERED (RRDS)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030002の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、展開確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にNUMBERED (RRDS)を指定し、OSKB030002の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND NUMBERED (RRDS)
CASE OSKB030002
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM NUMBERED (RRDS)
CASE OSKB030002
SOURCE DFSMS
NUMBERED (RRDS)とOSKB030002が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030002を同じ出力で読み、展開確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030002
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030002.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030002が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の NUMBERED (RRDS) と OSKB030002 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>NUMBERED (RRDS)</strong></p><p>検証目的: 構文確認のストレージ管理について、NUMBERED (RRDS)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010001の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、構文確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にNUMBERED (RRDS)を指定し、OSKB010001の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND NUMBERED (RRDS)
CASE OSKB010001
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM NUMBERED (RRDS)
CASE OSKB010001
SOURCE DFSMS
NUMBERED (RRDS)とOSKB010001が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010001を同じ出力で読み、構文確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010001
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010001.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010001が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の NUMBERED (RRDS) と OSKB010001 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010001 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0061"><h3>OWNER(ownerid)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>OWNER(ownerid)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出確認のストレージ管理でストレージ管理の運用確認を行います。OWNER(ownerid)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で呼出確認のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず呼出確認のストレージ管理を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、呼出確認の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. OWNER(ownerid)の属性行を読まず呼出確認のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出確認正解では選択記号 C を採用し、正解名は呼出確認正解です。呼出確認根拠では OWNER(ownerid) は「DFSMS で OWNER(ownerid)の扱いを記録する呼出確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は呼出確認根拠です。呼出確認受渡では OWNER(ownerid)の表示結果と IDC3009I を同じ確認単位にし、受渡名は呼出確認受渡です。不適切な選択肢を整理します。 A: 呼出確認流用は別カテゴリの確認であり、排除名は呼出確認流用です。 B: 呼出確認欠落は戻り値や記録番号に寄り、欠落名は呼出確認欠落です。 C: 呼出確認正答は対象出力と項目説明を結び、根拠名は呼出確認正答です。 D: 呼出確認不足は名称や説明だけに寄り、判定名は呼出確認不足です。呼出確認資料では OWNER(ownerid)の使い方を出典欄から追跡し、資料名は呼出確認資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details></section>


<section class="kb-item" id="c06-i0062"><h3>RECORDS(p s)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>RECORDS(p s)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで確認する項目です。見込みレコード数で割り振り。VSAM が RECORDSIZE と CISZ から必要シリンダー数を計算する。サイズ感に自信がない時に有用</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索照合のストレージ管理で RECORDS(p s)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. RECORDS(p s)の出力を取らず探索照合のストレージ管理の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、探索照合として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して探索照合のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索照合のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索照合正解では選択記号 B を採用し、正解名は探索照合正解です。探索照合根拠では RECORDS(p s) は「探索照合のストレージ管理に関係する定義値と表示行を照合する探索照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は探索照合根拠です。探索照合追跡では RECORDS(p s)の属性行と IDC3009I を合わせ、追跡名は探索照合追跡です。誤答側の問題点を分けます。 A: 探索照合不足は名称や説明だけに寄り、判定名は探索照合不足です。 B: 探索照合正答は対象出力と項目説明を結び、根拠名は探索照合正答です。 C: 探索照合欠落は戻り値や記録番号に寄り、欠落名は探索照合欠落です。 D: 探索照合流用は別カテゴリの確認であり、排除名は探索照合流用です。探索照合初出では RECORDS(p s)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索照合初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>RECORDS(p s)</strong></p><p>検証目的: 探索確認のストレージ管理について、RECORDS(p s)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で確認する項目です。見込みレコード数で割り振り。VSAM が RECORに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030006の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、探索確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にRECORDS(p s)を指定し、OSKB030006の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND RECORDS(p s)
CASE OSKB030006
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM RECORDS(p s)
CASE OSKB030006
SOURCE DFSMS
RECORDS(p s)とOSKB030006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030006を同じ出力で読み、探索確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030006
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030006.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の RECORDS(p s) と OSKB030006 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>RECORDS(p s)</strong></p><p>検証目的: 構文照合のストレージ管理について、RECORDS(p s)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で確認する項目です。見込みレコード数で割り振り。VSAM が RECORに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010021の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、構文照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にRECORDS(p s)を指定し、OSKB010021の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND RECORDS(p s)
CASE OSKB010021
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM RECORDS(p s)
CASE OSKB010021
SOURCE DFSMS
RECORDS(p s)とOSKB010021が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010021を同じ出力で読み、構文照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010021
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010021.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010021が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の RECORDS(p s) と OSKB010021 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010021 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0063"><h3>RECORDSIZE(avg max)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>RECORDSIZE(avg max)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。平均レコード長と最大レコード長 (バイト) を指定。可変長なら avg&lt;max、固定長なら avg=max。SPANNED 時は CI を超えうる</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲確認のストレージ管理でストレージ管理の運用確認を行います。RECORDSIZE 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で範囲確認のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず範囲確認のストレージ管理を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて範囲確認の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. RECORDSIZE 属性の属性行を読まず範囲確認のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲確認正解では選択記号 C を採用し、正解名は範囲確認正解です。範囲確認根拠では RECORDSIZE 属性 は「DFSMS で RECORDSIZE 属性の扱いを記録する範囲確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は範囲確認根拠です。範囲確認受渡では RECORDSIZE 属性の表示結果と IDC3009I を同じ確認単位にし、受渡名は範囲確認受渡です。不適切な選択肢を整理します。 A: 範囲確認流用は別カテゴリの確認であり、排除名は範囲確認流用です。 B: 範囲確認欠落は戻り値や記録番号に寄り、欠落名は範囲確認欠落です。 C: 範囲確認正答は対象出力と項目説明を結び、根拠名は範囲確認正答です。 D: 範囲確認不足は名称や説明だけに寄り、判定名は範囲確認不足です。範囲確認資料では RECORDSIZE 属性の使い方を出典欄から追跡し、資料名は範囲確認資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>RECORDSIZE(avg max)</strong></p><p>検証目的: 呼出確認のストレージ管理について、RECORDSIZE(avg max)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。平に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030003の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、呼出確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にRECORDSIZE(avg maxを指定し、OSKB030003の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND RECORDSIZE(avg max
CASE OSKB030003
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM RECORDSIZE(avg max
CASE OSKB030003
SOURCE DFSMS
RECORDSIZE(avg maxとOSKB030003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030003を同じ出力で読み、呼出確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030003
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030003.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の RECORDSIZE(avg max と OSKB030003 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>RECORDSIZE(avg max)</strong></p><p>検証目的: 探索確認のストレージ管理について、RECORDSIZE(avg max)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。平に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010006の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、探索確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にRECORDSIZE(avg maxを指定し、OSKB010006の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND RECORDSIZE(avg max
CASE OSKB010006
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM RECORDSIZE(avg max
CASE OSKB010006
SOURCE DFSMS
RECORDSIZE(avg maxとOSKB010006が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010006を同じ出力で読み、探索確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010006
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010006.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010006が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の RECORDSIZE(avg max と OSKB010006 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0064"><h3>RECOVERY (既定)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>RECOVERY (既定)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで自動化処理や復旧動作を確認する項目です。初期ロード前に CI を事前フォーマット。中断しても途中までの結果は保全されるが、ロード時間は長い。「RECOVERY (既定)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切確認の既定で RECOVERY (既定)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. RECOVERY (既定)の出力を取らず区切確認の既定の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、区切確認の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して区切確認の既定の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切確認の既定へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切確認正解では選択記号 B を採用し、正解名は区切確認正解です。区切確認根拠では RECOVERY (既定) は「区切確認の既定に関係する定義値と表示行を照合する区切確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は区切確認根拠です。区切確認追跡では RECOVERY (既定)の属性行と IDC3009I を合わせ、追跡名は区切確認追跡です。誤答側の問題点を分けます。 A: 区切確認不足は名称や説明だけに寄り、判定名は区切確認不足です。 B: 区切確認正答は対象出力と項目説明を結び、根拠名は区切確認正答です。 C: 区切確認欠落は戻り値や記録番号に寄り、欠落名は区切確認欠落です。 D: 区切確認流用は別カテゴリの確認であり、排除名は区切確認流用です。区切確認初出では RECOVERY (既定)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切確認初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RECOVERY (既定)</strong></p><p>検証目的: 終端確認の既定について、RECOVERY (既定)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で自動化処理や復旧動作を確認する項目です。初期ロード前に CI を事前に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010005の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、終端確認の既定の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にRECOVERY (既定)を指定し、OSKB010005の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND RECOVERY (既定)
CASE OSKB010005
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM RECOVERY (既定)
CASE OSKB010005
SOURCE DFSMS
RECOVERY (既定)とOSKB010005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010005を同じ出力で読み、終端確認の既定の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010005
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010005.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の RECOVERY (既定) と OSKB010005 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0065"><h3>REPLICATE (廃止)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>REPLICATE (廃止)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文照合の廃止に関係する REPLICATE (廃止)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果から対象行を抜き出し、構文照合の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. REPLICATE (廃止)の名称と担当者名だけを残して構文照合の廃止の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で構文照合の廃止を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず構文照合の廃止の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文照合正解では選択記号 A を採用し、正解名は構文照合正解です。構文照合根拠では REPLICATE (廃止) は「REPLICATE (廃止)の用途をストレージ管理の表示で確認する構文照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は構文照合根拠です。構文照合背景では DFSMS の REPLICATE (廃止)と IDC3009I を同じ証跡に残し、背景名は構文照合背景です。他の選択肢を確認します。 A: 構文照合正答は対象出力と項目説明を結び、根拠名は構文照合正答です。 B: 構文照合不足は名称や説明だけに寄り、判定名は構文照合不足です。 C: 構文照合流用は別カテゴリの確認であり、排除名は構文照合流用です。 D: 構文照合欠落は戻り値や記録番号に寄り、欠落名は構文照合欠落です。構文照合用語では REPLICATE (廃止)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文照合用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>REPLICATE (廃止)</strong></p><p>検証目的: 終端確認の廃止について、REPLICATE (廃止)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030005の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、終端確認の廃止の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にREPLICATE (廃止)を指定し、OSKB030005の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND REPLICATE (廃止)
CASE OSKB030005
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM REPLICATE (廃止)
CASE OSKB030005
SOURCE DFSMS
REPLICATE (廃止)とOSKB030005が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030005を同じ出力で読み、終端確認の廃止の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030005
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030005.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030005が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の REPLICATE (廃止) と OSKB030005 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030005 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>REPLICATE (廃止)</strong></p><p>検証目的: 値域確認の廃止について、REPLICATE (廃止)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010016の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、値域確認の廃止の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にREPLICATE (廃止)を指定し、OSKB010016の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND REPLICATE (廃止)
CASE OSKB010016
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM REPLICATE (廃止)
CASE OSKB010016
SOURCE DFSMS
REPLICATE (廃止)とOSKB010016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010016を同じ出力で読み、値域確認の廃止の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010016
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010016.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の REPLICATE (廃止) と OSKB010016 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0066"><h3>REUSE / NOREUSE</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>REUSE / NOREUSEは、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで確認する項目です。REUSE はクラスターを再利用可能にする。OPEN OUTPUT/RESET で内容を初期化して再使用できる。バッチ作業用領域に好適</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力確認の・に関する REUSE ・ NOREUSE の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず出力確認の・の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力確認の・の証跡として保存して根拠にする。</li><li>C. REUSE ・ NOREUSE の変更点を出力本文から切り離して出力確認の・の承認欄だけ残す。</li><li>D. IDC3009I を含む表示を保存し、説明欄との差分を出力確認で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力確認正解では選択記号 D を採用し、正解名は出力確認正解です。出力確認根拠では REUSE ・ NOREUSE は「REUSE ・ NOREUSE の状態と出力メッセージを結び付ける出力確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は出力確認根拠です。出力確認保存では REUSE ・ NOREUSE の出力行と IDC3009I を一緒に残し、保存名は出力確認保存です。選択肢ごとの違いを示します。 A: 出力確認欠落は戻り値や記録番号に寄り、欠落名は出力確認欠落です。 B: 出力確認流用は別カテゴリの確認であり、排除名は出力確認流用です。 C: 出力確認不足は名称や説明だけに寄り、判定名は出力確認不足です。 D: 出力確認正答は対象出力と項目説明を結び、根拠名は出力確認正答です。出力確認対象では REUSE ・ NOREUSE を DFSMS の確認記録に残し、対象名は出力確認対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REUSE ・ NOREUSE</strong></p><p>検証目的: 呼出確認の・について、REUSE / NOREUSE は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で確認する項目です。REUSE はクラスターを再利用可能にする。Oに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010003の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、呼出確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にREUSE ・ NOREUSEを指定し、OSKB010003の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND REUSE ・ NOREUSE
CASE OSKB010003
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM REUSE ・ NOREUSE
CASE OSKB010003
SOURCE DFSMS
REUSE ・ NOREUSEとOSKB010003が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010003を同じ出力で読み、呼出確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010003
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010003.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010003が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の REUSE ・ NOREUSE と OSKB010003 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010003 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0067"><h3>SHAREOPTIONS(3,3) の注意</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>SHAREOPTIONS(3,3) の注意は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで確認する項目です。整合性は完全にユーザ責任。VSAM はバッファ無効化を保証しない。RLS や DB2 経由なしで複数更新を許す唯一の運用は危険</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧確認の注意で SHAREOPTIONS 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SHAREOPTIONS 属性の出力を取らず復旧確認の注意の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、復旧確認の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して復旧確認の注意の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧確認の注意へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧確認正解では選択記号 B を採用し、正解名は復旧確認正解です。復旧確認根拠では SHAREOPTIONS 属性 は「復旧確認の注意に関係する定義値と表示行を照合する復旧確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は復旧確認根拠です。復旧確認追跡では SHAREOPTIONS 属性の属性行と IDC3009I を合わせ、追跡名は復旧確認追跡です。誤答側の問題点を分けます。 A: 復旧確認不足は名称や説明だけに寄り、判定名は復旧確認不足です。 B: 復旧確認正答は対象出力と項目説明を結び、根拠名は復旧確認正答です。 C: 復旧確認欠落は戻り値や記録番号に寄り、欠落名は復旧確認欠落です。 D: 復旧確認流用は別カテゴリの確認であり、排除名は復旧確認流用です。復旧確認初出では SHAREOPTIONS 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧確認初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SHAREOPTIONS(3,3) の注意</strong></p><p>検証目的: 記録確認のの注意について、SHAREOPTIONS(3,3) の注意は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で確認する項目です。整合性は完全にユーザ責任。VSAMに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010013の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、記録確認のの注意の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSHAREOPTIONS(3,3) を指定し、OSKB010013の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND SHAREOPTIONS(3,3) 
CASE OSKB010013
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM SHAREOPTIONS(3,3) 
CASE OSKB010013
SOURCE DFSMS
SHAREOPTIONS(3,3) とOSKB010013が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010013を同じ出力で読み、記録確認のの注意の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010013
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010013.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010013が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の SHAREOPTIONS(3,3)  と OSKB010013 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010013 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0068"><h3>SHAREOPTIONS(4,4) と RLS</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>SHAREOPTIONS(4,4) と RLSは、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで構成値やオプションの意味を確認する項目です。(4,4) は読み取りごとにバッファをリフレッシュ。RLS (Record Level Sharing) は CF 上のロック管理で本格的な共有更新を実現する</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査確認のストレージ管理でストレージ管理の運用確認を行います。SHAREOPTIONS 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で監査確認のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず監査確認のストレージ管理を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて監査確認の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. SHAREOPTIONS 属性の属性行を読まず監査確認のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査確認正解では選択記号 C を採用し、正解名は監査確認正解です。監査確認根拠では SHAREOPTIONS 属性 は「DFSMS で SHAREOPTIONS 属性の扱いを記録する監査確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は監査確認根拠です。監査確認受渡では SHAREOPTIONS 属性の表示結果と IDC3009I を同じ確認単位にし、受渡名は監査確認受渡です。不適切な選択肢を整理します。 A: 監査確認流用は別カテゴリの確認であり、排除名は監査確認流用です。 B: 監査確認欠落は戻り値や記録番号に寄り、欠落名は監査確認欠落です。 C: 監査確認正答は対象出力と項目説明を結び、根拠名は監査確認正答です。 D: 監査確認不足は名称や説明だけに寄り、判定名は監査確認不足です。監査確認資料では SHAREOPTIONS 属性の使い方を出典欄から追跡し、資料名は監査確認資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SHAREOPTIONS(4,4) と RLS</strong></p><p>検証目的: 比較確認のとについて、SHAREOPTIONS(4,4) と RLS は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で構成値やオプションの意味を確認する項目です。(4に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010014の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、比較確認のとの確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSHAREOPTIONS(4,4) を指定し、OSKB010014の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND SHAREOPTIONS(4,4) 
CASE OSKB010014
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM SHAREOPTIONS(4,4) 
CASE OSKB010014
SOURCE DFSMS
SHAREOPTIONS(4,4) とOSKB010014が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010014を同じ出力で読み、比較確認のとの根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010014
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010014.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010014が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の SHAREOPTIONS(4,4)  と OSKB010014 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010014 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0069"><h3>SHAREOPTIONS(cr cs)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>SHAREOPTIONS(cr cs)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで構成値やオプションの意味を確認する項目です。クロスリージョン共有 (cr) とクロスシステム共有 (cs) のレベル。(1,3)=読取多重/書込排他、(2,3)=読書混在、(3,3)=全責任ユーザ、(4,4)=フル共有</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告確認のストレージ管理に関係する SHAREOPTIONS 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告確認で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. SHAREOPTIONS 属性の名称と担当者名だけを残して警告確認のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で警告確認のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず警告確認のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告確認正解では選択記号 A を採用し、正解名は警告確認正解です。警告確認根拠では SHAREOPTIONS 属性 は「SHAREOPTIONS 属性の用途をストレージ管理の表示で確認する警告確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は警告確認根拠です。警告確認背景では DFSMS の SHAREOPTIONS 属性と IDC3009I を同じ証跡に残し、背景名は警告確認背景です。他の選択肢を確認します。 A: 警告確認正答は対象出力と項目説明を結び、根拠名は警告確認正答です。 B: 警告確認不足は名称や説明だけに寄り、判定名は警告確認不足です。 C: 警告確認流用は別カテゴリの確認であり、排除名は警告確認流用です。 D: 警告確認欠落は戻り値や記録番号に寄り、欠落名は警告確認欠落です。警告確認用語では SHAREOPTIONS 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告確認用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 記録検査のストレージ管理に関係する SHAREOPTIONS 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、記録検査の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. SHAREOPTIONS 属性の名称と担当者名だけを残して記録検査のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で記録検査のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず記録検査のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録検査正解では選択記号 A を採用し、正解名は記録検査正解です。記録検査根拠では SHAREOPTIONS 属性 は「SHAREOPTIONS 属性の用途をストレージ管理の表示で確認する記録検査項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は記録検査根拠です。記録検査背景では DFSMS の SHAREOPTIONS 属性と IDC3009I を同じ証跡に残し、背景名は記録検査背景です。他の選択肢を確認します。 A: 記録検査正答は対象出力と項目説明を結び、根拠名は記録検査正答です。 B: 記録検査不足は名称や説明だけに寄り、判定名は記録検査不足です。 C: 記録検査流用は別カテゴリの確認であり、排除名は記録検査流用です。 D: 記録検査欠落は戻り値や記録番号に寄り、欠落名は記録検査欠落です。記録検査用語では SHAREOPTIONS 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録検査用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>SHAREOPTIONS(cr cs)</strong></p><p>検証目的: 優先確認のストレージ管理について、SHAREOPTIONS(cr cs)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で構成値やオプションの意味を確認する項目です。クロスリージに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010012の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、優先確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSHAREOPTIONS(cr csを指定し、OSKB010012の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND SHAREOPTIONS(cr cs
CASE OSKB010012
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM SHAREOPTIONS(cr cs
CASE OSKB010012
SOURCE DFSMS
SHAREOPTIONS(cr csとOSKB010012が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010012を同じ出力で読み、優先確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010012
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010012.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010012が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の SHAREOPTIONS(cr cs と OSKB010012 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010012 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>SHAREOPTIONS(cr cs)</strong></p><p>検証目的: 出力検査のストレージ管理について、SHAREOPTIONS(cr cs)は、DFSMS / IDCAMS / VSAM の ALTER で構成値やオプションの意味を確認する項目です。共有オプションを変更。アプリ側に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010068の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、出力検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSHAREOPTIONS(cr csを指定し、OSKB010068の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND SHAREOPTIONS(cr cs
CASE OSKB010068
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM SHAREOPTIONS(cr cs
CASE OSKB010068
SOURCE DFSMS
SHAREOPTIONS(cr csとOSKB010068が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010068を同じ出力で読み、出力検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010068
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010068.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010068が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の SHAREOPTIONS(cr cs と OSKB010068 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010068 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0070"><h3>SPANNED</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>SPANNEDは、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで確認する項目です。レコードが複数 CI にまたがって格納可能。RECORDSIZE が CISZ より大きいケースを許容する。インデックス CI は対象外</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録照合のストレージ管理に関係する SPANNED の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果から対象行を抜き出し、記録照合の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. SPANNED の名称と担当者名だけを残して記録照合のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で記録照合のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず記録照合のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録照合正解では選択記号 A を採用し、正解名は記録照合正解です。記録照合根拠では SPANNED は「SPANNED の用途をストレージ管理の表示で確認する記録照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は記録照合根拠です。記録照合背景では DFSMS の SPANNED と IDC3009I を同じ証跡に残し、背景名は記録照合背景です。他の選択肢を確認します。 A: 記録照合正答は対象出力と項目説明を結び、根拠名は記録照合正答です。 B: 記録照合不足は名称や説明だけに寄り、判定名は記録照合不足です。 C: 記録照合流用は別カテゴリの確認であり、排除名は記録照合流用です。 D: 記録照合欠落は戻り値や記録番号に寄り、欠落名は記録照合欠落です。記録照合用語では SPANNED を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録照合用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SPANNED</strong></p><p>検証目的: 出力照合のストレージ管理について、SPANNED は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で確認する項目です。レコードが複数 CI にまたがって格納可能。RECORDSIZに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010028の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、出力照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSPANNEDを指定し、OSKB010028の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND SPANNED
CASE OSKB010028
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM SPANNED
CASE OSKB010028
SOURCE DFSMS
SPANNEDとOSKB010028が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010028を同じ出力で読み、出力照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010028
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010028.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010028が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の SPANNED と OSKB010028 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010028 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0071"><h3>SPEED</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>SPEEDは、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件確認のストレージ管理に関係する SPEED の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果から対象行を抜き出し、条件確認の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. SPEED の名称と担当者名だけを残して条件確認のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で条件確認のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず条件確認のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件確認正解では選択記号 A を採用し、正解名は条件確認正解です。条件確認根拠では SPEED は「SPEED の用途をストレージ管理の表示で確認する条件確認項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は条件確認根拠です。条件確認背景では DFSMS の SPEED と IDC3009I を同じ証跡に残し、背景名は条件確認背景です。他の選択肢を確認します。 A: 条件確認正答は対象出力と項目説明を結び、根拠名は条件確認正答です。 B: 条件確認不足は名称や説明だけに寄り、判定名は条件確認不足です。 C: 条件確認流用は別カテゴリの確認であり、排除名は条件確認流用です。 D: 条件確認欠落は戻り値や記録番号に寄り、欠落名は条件確認欠落です。条件確認用語では SPEED を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件確認用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SPEED</strong></p><p>検証目的: 置換確認のストレージ管理について、SPEED は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010004の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、置換確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSPEEDを指定し、OSKB010004の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND SPEED
CASE OSKB010004
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM SPEED
CASE OSKB010004
SOURCE DFSMS
SPEEDとOSKB010004が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010004を同じ出力で読み、置換確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010004
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010004.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010004が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の SPEED と OSKB010004 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010004 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0072"><h3>STORCLAS(name)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>STORCLAS(name)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。SMS ストレージクラスを明示指定。性能/可用性/配置要件を表現し、ACS と組み合わせて配置先プールを決定する。「STORCLAS(name)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲照合のストレージ管理でストレージ管理の運用確認を行います。STORCLAS(name)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で範囲照合のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず範囲照合のストレージ管理を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて範囲照合の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. STORCLAS(name)の属性行を読まず範囲照合のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲照合正解では選択記号 C を採用し、正解名は範囲照合正解です。範囲照合根拠では STORCLAS(name) は「DFSMS で STORCLAS(name)の扱いを記録する範囲照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は範囲照合根拠です。範囲照合受渡では STORCLAS(name)の表示結果と IDC3009I を同じ確認単位にし、受渡名は範囲照合受渡です。不適切な選択肢を整理します。 A: 範囲照合流用は別カテゴリの確認であり、排除名は範囲照合流用です。 B: 範囲照合欠落は戻り値や記録番号に寄り、欠落名は範囲照合欠落です。 C: 範囲照合正答は対象出力と項目説明を結び、根拠名は範囲照合正答です。 D: 範囲照合不足は名称や説明だけに寄り、判定名は範囲照合不足です。範囲照合資料では STORCLAS(name)の使い方を出典欄から追跡し、資料名は範囲照合資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>STORCLAS(name)</strong></p><p>検証目的: 上書確認のストレージ管理について、STORCLAS(name)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。SMS ストに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030007の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、上書確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSTORCLAS(name)を指定し、OSKB030007の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND STORCLAS(name)
CASE OSKB030007
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM STORCLAS(name)
CASE OSKB030007
SOURCE DFSMS
STORCLAS(name)とOSKB030007が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030007を同じ出力で読み、上書確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030007
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030007.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030007が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の STORCLAS(name) と OSKB030007 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030007 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>STORCLAS(name)</strong></p><p>検証目的: 探索照合のストレージ管理について、STORCLAS(name)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。SMS ストに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010026の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、探索照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSTORCLAS(name)を指定し、OSKB010026の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND STORCLAS(name)
CASE OSKB010026
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM STORCLAS(name)
CASE OSKB010026
SOURCE DFSMS
STORCLAS(name)とOSKB010026が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010026を同じ出力で読み、探索照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010026
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010026.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010026が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の STORCLAS(name) と OSKB010026 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010026 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0073"><h3>TO(yyyyddd) / FOR(days)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>TO(yyyyddd) / FOR(days)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。保持期限の指定。TO は絶対日付 (ユリウス)、FOR は登録日からの日数。期限内の削除は PURGE 指定が必要。「TO(yyyyddd) / FOR(days)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較照合の・で TO 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. TO 属性の出力を取らず比較照合の・の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、比較照合の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して比較照合の・の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較照合の・へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較照合正解では選択記号 B を採用し、正解名は比較照合正解です。比較照合根拠では TO 属性 は「比較照合の・に関係する定義値と表示行を照合する比較照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は比較照合根拠です。比較照合追跡では TO 属性の属性行と IDC3009I を合わせ、追跡名は比較照合追跡です。誤答側の問題点を分けます。 A: 比較照合不足は名称や説明だけに寄り、判定名は比較照合不足です。 B: 比較照合正答は対象出力と項目説明を結び、根拠名は比較照合正答です。 C: 比較照合欠落は戻り値や記録番号に寄り、欠落名は比較照合欠落です。 D: 比較照合流用は別カテゴリの確認であり、排除名は比較照合流用です。比較照合初出では TO 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較照合初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 順序検査の・でストレージ管理の運用確認を行います。TO 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で順序検査の・を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず順序検査の・を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序検査の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. TO 属性の属性行を読まず順序検査の・の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序検査正解では選択記号 C を採用し、正解名は順序検査正解です。順序検査根拠では TO 属性 は「DFSMS で TO 属性の扱いを記録する順序検査項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は順序検査根拠です。順序検査受渡では TO 属性の表示結果と IDC0001I を同じ確認単位にし、受渡名は順序検査受渡です。不適切な選択肢を整理します。 A: 順序検査流用は別カテゴリの確認であり、排除名は順序検査流用です。 B: 順序検査欠落は戻り値や記録番号に寄り、欠落名は順序検査欠落です。 C: 順序検査正答は対象出力と項目説明を結び、根拠名は順序検査正答です。 D: 順序検査不足は名称や説明だけに寄り、判定名は順序検査不足です。順序検査資料では TO 属性の使い方を出典欄から追跡し、資料名は順序検査資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>TO(yyyyddd) ・ FOR(days)</strong></p><p>検証目的: 条件照合の・について、TO(yyyyddd) / FOR(days)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010029の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、条件照合の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にTO(yyyyddd) ・ FOR(を指定し、OSKB010029の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND TO(yyyyddd) ・ FOR(
CASE OSKB010029
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM TO(yyyyddd) ・ FOR(
CASE OSKB010029
SOURCE DFSMS
TO(yyyyddd) ・ FOR(とOSKB010029が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010029を同じ出力で読み、条件照合の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010029
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010029.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010029が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の TO(yyyyddd) ・ FOR( と OSKB010029 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010029 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>TO(yyyyddd) ・ FOR(days)</strong></p><p>検証目的: 区切検査の・について、TO(yyyyddd) / FOR(days)は、DFSMS / IDCAMS / VSAM の ALTER で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010070の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、区切検査の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にTO(yyyyddd) ・ FOR(を指定し、OSKB010070の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND TO(yyyyddd) ・ FOR(
CASE OSKB010070
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM TO(yyyyddd) ・ FOR(
CASE OSKB010070
SOURCE DFSMS
TO(yyyyddd) ・ FOR(とOSKB010070が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010070を同じ出力で読み、区切検査の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010070
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010070.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010070が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の TO(yyyyddd) ・ FOR( と OSKB010070 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010070 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0074"><h3>TRACKS(p s)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>TRACKS(p s)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。1 次/2 次割り振りをトラック単位で指定。小規模クラスター向け。「TRACKS(p s)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端照合のストレージ管理に関係する TRACKS(p s)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、終端照合の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. TRACKS(p s)の名称と担当者名だけを残して終端照合のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で終端照合のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず終端照合のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端照合正解では選択記号 A を採用し、正解名は終端照合正解です。終端照合根拠では TRACKS(p s) は「TRACKS(p s)の用途をストレージ管理の表示で確認する終端照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は終端照合根拠です。終端照合背景では DFSMS の TRACKS(p s)と IDC3009I を同じ証跡に残し、背景名は終端照合背景です。他の選択肢を確認します。 A: 終端照合正答は対象出力と項目説明を結び、根拠名は終端照合正答です。 B: 終端照合不足は名称や説明だけに寄り、判定名は終端照合不足です。 C: 終端照合流用は別カテゴリの確認であり、排除名は終端照合流用です。 D: 終端照合欠落は戻り値や記録番号に寄り、欠落名は終端照合欠落です。終端照合用語では TRACKS(p s)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端照合用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TRACKS(p s)</strong></p><p>検証目的: 変更確認のストレージ管理について、TRACKS(p s)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。1 次/2 次割りに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010020の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、変更確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にTRACKS(p s)を指定し、OSKB010020の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND TRACKS(p s)
CASE OSKB010020
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM TRACKS(p s)
CASE OSKB010020
SOURCE DFSMS
TRACKS(p s)とOSKB010020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010020を同じ出力で読み、変更確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010020
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010020.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の TRACKS(p s) と OSKB010020 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0075"><h3>UNIQUE / SUBALLOCATION (廃止)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>SMS 以前の VSAM データスペース管理方式。SMS 管理ボリュームでは指定不可、非 SMS でも非推奨。「UNIQUE / SUBALLOCATION (廃止)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開照合の・で UNIQUE 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. UNIQUE 属性の出力を取らず展開照合の・の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、展開照合の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して展開照合の・の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開照合の・へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開照合正解では選択記号 B を採用し、正解名は展開照合正解です。展開照合根拠では UNIQUE 属性 は「展開照合の・に関係する定義値と表示行を照合する展開照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は展開照合根拠です。展開照合追跡では UNIQUE 属性の属性行と IDC3009I を合わせ、追跡名は展開照合追跡です。誤答側の問題点を分けます。 A: 展開照合不足は名称や説明だけに寄り、判定名は展開照合不足です。 B: 展開照合正答は対象出力と項目説明を結び、根拠名は展開照合正答です。 C: 展開照合欠落は戻り値や記録番号に寄り、欠落名は展開照合欠落です。 D: 展開照合流用は別カテゴリの確認であり、排除名は展開照合流用です。展開照合初出では UNIQUE 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開照合初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UNIQUE ・ SUBALLOCATION (廃止)</strong></p><p>検証目的: 警告確認の・について、SMS 以前の VSAM データスペース管理方式。SMS 管理ボリュームでは指定不可、非 SMS でも非推奨。「UNIQUE / SUBALLOCATION (廃止)」を読に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010017の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、警告確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にUNIQUE ・ SUBALLOCAを指定し、OSKB010017の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND UNIQUE ・ SUBALLOCA
CASE OSKB010017
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM UNIQUE ・ SUBALLOCA
CASE OSKB010017
SOURCE DFSMS
UNIQUE ・ SUBALLOCAとOSKB010017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010017を同じ出力で読み、警告確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010017
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010017.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の UNIQUE ・ SUBALLOCA と OSKB010017 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0076"><h3>UNIT(unittype)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>UNIT(unittype)は、DFSMS / IDCAMS / VSAMのDEFINE_CLUSTERで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件照合のストレージ管理に関係する UNIT(unittype)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件照合で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. UNIT(unittype)の名称と担当者名だけを残して条件照合のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で条件照合のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず条件照合のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件照合正解では選択記号 A を採用し、正解名は条件照合正解です。条件照合根拠では UNIT(unittype) は「UNIT(unittype)の用途をストレージ管理の表示で確認する条件照合項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は条件照合根拠です。条件照合背景では DFSMS の UNIT(unittype)と IDC3009I を同じ証跡に残し、背景名は条件照合背景です。他の選択肢を確認します。 A: 条件照合正答は対象出力と項目説明を結び、根拠名は条件照合正答です。 B: 条件照合不足は名称や説明だけに寄り、判定名は条件照合不足です。 C: 条件照合流用は別カテゴリの確認であり、排除名は条件照合流用です。 D: 条件照合欠落は戻り値や記録番号に寄り、欠落名は条件照合欠落です。条件照合用語では UNIT(unittype)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件照合用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UNIT(unittype)</strong></p><p>検証目的: 置換照合のストレージ管理について、UNIT(unittype)は、DFSMS / IDCAMS / VSAM の DEFINE_CLUSTER で機能名、見出し、または確認対象として参照する項目です。関連する操作に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010024の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、置換照合のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にUNIT(unittype)を指定し、OSKB010024の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND UNIT(unittype)
CASE OSKB010024
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM UNIT(unittype)
CASE OSKB010024
SOURCE DFSMS
UNIT(unittype)とOSKB010024が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010024を同じ出力で読み、置換照合のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010024
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010024.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010024が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の UNIT(unittype) と OSKB010024 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0077"><h3>VOLUMES(volser ...)</h3><p class="kb-meta">分類: DEFINE_CLUSTER ・ 難易度: 上級</p><p>DFSMS IDCAMS VSAMのDEFINE_CLUSTERでは、データセット定義、属性、AMS出力を対応付けて確認します。DEFINE_CLUSTERは、DFSMS IDCAMS VSAMの運用で指定値、構文上の位置、反映後の出力を読み分ける項目です。出典欄のマニュアルで、VOLUMES(volser ...)の表記と許可される値を確認します。</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p></section>


## DEFINE_GDG


<section class="kb-item" id="c06-i0078"><h3>DEFINE GDG 基本</h3><p class="kb-meta">分類: DEFINE_GDG ・ 難易度: 上級</p><p>DEFINE GDG 基本は、DFSMS / IDCAMS / VSAMのDEFINE_GDGで確認する項目です。Generation Data Group のベースエントリを ICF カタログに作成。世代データセットの命名・管理単位となる</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力追跡の基本に関する DEFINE GDG 基本の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず出力追跡の基本の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力追跡の基本の証跡として保存して根拠にする。</li><li>C. DEFINE GDG 基本の変更点を出力本文から切り離して出力追跡の基本の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC3009I を読み、出力追跡の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力追跡正解では選択記号 D を採用し、正解名は出力追跡正解です。出力追跡根拠では DEFINE GDG 基本 は「DEFINE GDG 基本の状態と出力メッセージを結び付ける出力追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は出力追跡根拠です。出力追跡保存では DEFINE GDG 基本の出力行と IDC3009I を一緒に残し、保存名は出力追跡保存です。選択肢ごとの違いを示します。 A: 出力追跡欠落は戻り値や記録番号に寄り、欠落名は出力追跡欠落です。 B: 出力追跡流用は別カテゴリの確認であり、排除名は出力追跡流用です。 C: 出力追跡不足は名称や説明だけに寄り、判定名は出力追跡不足です。 D: 出力追跡正答は対象出力と項目説明を結び、根拠名は出力追跡正答です。出力追跡対象では DEFINE GDG 基本を DFSMS の確認記録に残し、対象名は出力追跡対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEFINE GDG 基本</strong></p><p>検証目的: 呼出追跡の基本について、DEFINE GDG 基本は、DFSMS / IDCAMS / VSAM の DEFINE_GDG で確認する項目です。Generation Data Group のベースエントに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010043の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、呼出追跡の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDEFINE GDG 基本を指定し、OSKB010043の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DEFINE GDG 基本
CASE OSKB010043
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DEFINE GDG 基本
CASE OSKB010043
SOURCE DFSMS
DEFINE GDG 基本とOSKB010043が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010043を同じ出力で読み、呼出追跡の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010043
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010043.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010043が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DEFINE GDG 基本 と OSKB010043 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010043 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0079"><h3>EMPTY / NOEMPTY</h3><p class="kb-meta">分類: DEFINE_GDG ・ 難易度: 上級</p><p>EMPTY / NOEMPTYは、DFSMS / IDCAMS / VSAMのDEFINE_GDGで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲追跡の・でストレージ管理の運用確認を行います。EMPTY ・ NOEMPTY の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で範囲追跡の・を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず範囲追跡の・を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲追跡の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. EMPTY ・ NOEMPTY の属性行を読まず範囲追跡の・の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲追跡正解では選択記号 C を採用し、正解名は範囲追跡正解です。範囲追跡根拠では EMPTY ・ NOEMPTY は「DFSMS で EMPTY ・ NOEMPTY の扱いを記録する範囲追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は範囲追跡根拠です。範囲追跡受渡では EMPTY ・ NOEMPTY の表示結果と IDC3009I を同じ確認単位にし、受渡名は範囲追跡受渡です。不適切な選択肢を整理します。 A: 範囲追跡流用は別カテゴリの確認であり、排除名は範囲追跡流用です。 B: 範囲追跡欠落は戻り値や記録番号に寄り、欠落名は範囲追跡欠落です。 C: 範囲追跡正答は対象出力と項目説明を結び、根拠名は範囲追跡正答です。 D: 範囲追跡不足は名称や説明だけに寄り、判定名は範囲追跡不足です。範囲追跡資料では EMPTY ・ NOEMPTY の使い方を出典欄から追跡し、資料名は範囲追跡資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>EMPTY ・ NOEMPTY</strong></p><p>検証目的: 範囲確認の・について、EMPTY / NOEMPTY は、DFSMS / IDCAMS / VSAM の DEFINE_GDG で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030011の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、範囲確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にEMPTY ・ NOEMPTYを指定し、OSKB030011の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND EMPTY ・ NOEMPTY
CASE OSKB030011
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM EMPTY ・ NOEMPTY
CASE OSKB030011
SOURCE DFSMS
EMPTY ・ NOEMPTYとOSKB030011が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030011を同じ出力で読み、範囲確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030011
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030011.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030011が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の EMPTY ・ NOEMPTY と OSKB030011 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030011 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>EMPTY ・ NOEMPTY</strong></p><p>検証目的: 探索追跡の・について、EMPTY / NOEMPTY は、DFSMS / IDCAMS / VSAM の DEFINE_GDG で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010046の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、探索追跡の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にEMPTY ・ NOEMPTYを指定し、OSKB010046の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND EMPTY ・ NOEMPTY
CASE OSKB010046
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM EMPTY ・ NOEMPTY
CASE OSKB010046
SOURCE DFSMS
EMPTY ・ NOEMPTYとOSKB010046が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010046を同じ出力で読み、探索追跡の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010046
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010046.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010046が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の EMPTY ・ NOEMPTY と OSKB010046 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010046 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0080"><h3>EXTENDED</h3><p class="kb-meta">分類: DEFINE_GDG ・ 難易度: 上級</p><p>EXTENDEDは、DFSMS / IDCAMS / VSAMのDEFINE_GDGで機能名、見出し、または確認対象として参照する項目です。GDG 世代数上限を 255 から 999 に拡張する z/OS V1R12 以降の属性。既存 GDG を ALTER で EXTENDED 化することも可能</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先追跡のストレージ管理に関する EXTENDED の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず優先追跡のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先追跡のストレージ管理の証跡として保存して根拠にする。</li><li>C. EXTENDED の変更点を出力本文から切り離して優先追跡のストレージ管理の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、優先追跡の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先追跡正解では選択記号 D を採用し、正解名は優先追跡正解です。優先追跡根拠では EXTENDED は「EXTENDED の状態と出力メッセージを結び付ける優先追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は優先追跡根拠です。優先追跡保存では EXTENDED の出力行と IDC3009I を一緒に残し、保存名は優先追跡保存です。選択肢ごとの違いを示します。 A: 優先追跡欠落は戻り値や記録番号に寄り、欠落名は優先追跡欠落です。 B: 優先追跡流用は別カテゴリの確認であり、排除名は優先追跡流用です。 C: 優先追跡不足は名称や説明だけに寄り、判定名は優先追跡不足です。 D: 優先追跡正答は対象出力と項目説明を結び、根拠名は優先追跡正答です。優先追跡対象では EXTENDED を DFSMS の確認記録に残し、対象名は優先追跡対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EXTENDED</strong></p><p>検証目的: 上書追跡のストレージ管理について、EXTENDED は、DFSMS / IDCAMS / VSAM の DEFINE_GDG で機能名、見出し、または確認対象として参照する項目です。GDG 世代数上限を 255 かに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010047の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、上書追跡のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にEXTENDEDを指定し、OSKB010047の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND EXTENDED
CASE OSKB010047
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM EXTENDED
CASE OSKB010047
SOURCE DFSMS
EXTENDEDとOSKB010047が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010047を同じ出力で読み、上書追跡のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010047
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010047.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010047が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の EXTENDED と OSKB010047 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010047 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0081"><h3>LIMIT(n)</h3><p class="kb-meta">分類: DEFINE_GDG ・ 難易度: 上級</p><p>LIMIT(n)は、DFSMS / IDCAMS / VSAMのDEFINE_GDGで機能名、見出し、または確認対象として参照する項目です。GDG が保持する世代数の上限 (1〜255、EXTENDED 時 999)。超過すると最古世代が NOEMPTY 時は単独、EMPTY 時は全てロールオフ</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件追跡のストレージ管理に関係する LIMIT(n)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、条件追跡の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. LIMIT(n)の名称と担当者名だけを残して条件追跡のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で条件追跡のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず条件追跡のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件追跡正解では選択記号 A を採用し、正解名は条件追跡正解です。条件追跡根拠では LIMIT(n) は「LIMIT(n)の用途をストレージ管理の表示で確認する条件追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は条件追跡根拠です。条件追跡背景では DFSMS の LIMIT(n)と IDC3009I を同じ証跡に残し、背景名は条件追跡背景です。他の選択肢を確認します。 A: 条件追跡正答は対象出力と項目説明を結び、根拠名は条件追跡正答です。 B: 条件追跡不足は名称や説明だけに寄り、判定名は条件追跡不足です。 C: 条件追跡流用は別カテゴリの確認であり、排除名は条件追跡流用です。 D: 条件追跡欠落は戻り値や記録番号に寄り、欠落名は条件追跡欠落です。条件追跡用語では LIMIT(n)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件追跡用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LIMIT(n)</strong></p><p>検証目的: 置換追跡のストレージ管理について、LIMIT(n)は、DFSMS / IDCAMS / VSAM の DEFINE_GDG で機能名、見出し、または確認対象として参照する項目です。GDG が保持する世代数の上限に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010044の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、置換追跡のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にLIMIT(n)を指定し、OSKB010044の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND LIMIT(n)
CASE OSKB010044
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM LIMIT(n)
CASE OSKB010044
SOURCE DFSMS
LIMIT(n)とOSKB010044が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010044を同じ出力で読み、置換追跡のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010044
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010044.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010044が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の LIMIT(n) と OSKB010044 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010044 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0082"><h3>OWNER(id)</h3><p class="kb-meta">分類: DEFINE_GDG ・ 難易度: 上級</p><p>OWNER(id)は、DFSMS / IDCAMS / VSAMのDEFINE_GDGで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録追跡のストレージ管理に関係する OWNER(id)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録追跡で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. OWNER(id)の名称と担当者名だけを残して記録追跡のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で記録追跡のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず記録追跡のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録追跡正解では選択記号 A を採用し、正解名は記録追跡正解です。記録追跡根拠では OWNER(id) は「OWNER(id)の用途をストレージ管理の表示で確認する記録追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は記録追跡根拠です。記録追跡背景では DFSMS の OWNER(id)と IDC3009I を同じ証跡に残し、背景名は記録追跡背景です。他の選択肢を確認します。 A: 記録追跡正答は対象出力と項目説明を結び、根拠名は記録追跡正答です。 B: 記録追跡不足は名称や説明だけに寄り、判定名は記録追跡不足です。 C: 記録追跡流用は別カテゴリの確認であり、排除名は記録追跡流用です。 D: 記録追跡欠落は戻り値や記録番号に寄り、欠落名は記録追跡欠落です。記録追跡用語では OWNER(id)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録追跡用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>OWNER(id)</strong></p><p>検証目的: 出力追跡のストレージ管理について、OWNER(id)は、DFSMS / IDCAMS / VSAM の DEFINE_GDG で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010048の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、出力追跡のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にOWNER(id)を指定し、OSKB010048の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND OWNER(id)
CASE OSKB010048
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM OWNER(id)
CASE OSKB010048
SOURCE DFSMS
OWNER(id)とOSKB010048が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010048を同じ出力で読み、出力追跡のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010048
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010048.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010048が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の OWNER(id) と OSKB010048 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010048 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0083"><h3>PURGE / NOPURGE</h3><p class="kb-meta">分類: DEFINE_GDG ・ 難易度: 上級</p><p>PURGE / NOPURGEは、DFSMS / IDCAMS / VSAMのDEFINE_GDGで機能名、見出し、または確認対象として参照する項目です。DELETE 時に期限内世代も削除するか。PURGE は期限を無視、NOPURGE は期限内エラーとする。「PURGE / NOPURGE」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序追跡の・でストレージ管理の運用確認を行います。PURGE ・ NOPURGE の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で順序追跡の・を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず順序追跡の・を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて順序追跡の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. PURGE ・ NOPURGE の属性行を読まず順序追跡の・の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序追跡正解では選択記号 C を採用し、正解名は順序追跡正解です。順序追跡根拠では PURGE ・ NOPURGE は「DFSMS で PURGE ・ NOPURGE の扱いを記録する順序追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は順序追跡根拠です。順序追跡受渡では PURGE ・ NOPURGE の表示結果と IDC3009I を同じ確認単位にし、受渡名は順序追跡受渡です。不適切な選択肢を整理します。 A: 順序追跡流用は別カテゴリの確認であり、排除名は順序追跡流用です。 B: 順序追跡欠落は戻り値や記録番号に寄り、欠落名は順序追跡欠落です。 C: 順序追跡正答は対象出力と項目説明を結び、根拠名は順序追跡正答です。 D: 順序追跡不足は名称や説明だけに寄り、判定名は順序追跡不足です。順序追跡資料では PURGE ・ NOPURGE の使い方を出典欄から追跡し、資料名は順序追跡資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 範囲判定の・でストレージ管理の運用確認を行います。PURGE ・ NOPURGE の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で範囲判定の・を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず範囲判定の・を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて範囲判定の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. PURGE ・ NOPURGE の属性行を読まず範囲判定の・の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲判定正解では選択記号 C を採用し、正解名は範囲判定正解です。範囲判定根拠では PURGE ・ NOPURGE は「DFSMS で PURGE ・ NOPURGE の扱いを記録する範囲判定項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は範囲判定根拠です。範囲判定受渡では PURGE ・ NOPURGE の表示結果と IDC3009I を同じ確認単位にし、受渡名は範囲判定受渡です。不適切な選択肢を整理します。 A: 範囲判定流用は別カテゴリの確認であり、排除名は範囲判定流用です。 B: 範囲判定欠落は戻り値や記録番号に寄り、欠落名は範囲判定欠落です。 C: 範囲判定正答は対象出力と項目説明を結び、根拠名は範囲判定正答です。 D: 範囲判定不足は名称や説明だけに寄り、判定名は範囲判定不足です。範囲判定資料では PURGE ・ NOPURGE の使い方を出典欄から追跡し、資料名は範囲判定資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（3件）</summary><div class="kb-p"><p class="kb-pname"><strong>PURGE ・ NOPURGE</strong></p><p>検証目的: 監査確認の・について、保持期限内のエントリを強制削除 (PURGE) するか、エラーで止める (NOPURGE、既定) か。「PURGE / NOPURGE」を読むと、DEFINE、ALTER、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030019の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、監査確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にPURGE ・ NOPURGEを指定し、OSKB030019の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND PURGE ・ NOPURGE
CASE OSKB030019
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM PURGE ・ NOPURGE
CASE OSKB030019
SOURCE DFSMS
PURGE ・ NOPURGEとOSKB030019が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030019を同じ出力で読み、監査確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030019
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030019.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030019が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の PURGE ・ NOPURGE と OSKB030019 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030019 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>PURGE ・ NOPURGE</strong></p><p>検証目的: 区切追跡の・について、PURGE / NOPURGE は、DFSMS / IDCAMS / VSAM の DEFINE_GDG で機能名、見出し、または確認対象として参照する項目です。DELETE 時にに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010050の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、区切追跡の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にPURGE ・ NOPURGEを指定し、OSKB010050の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND PURGE ・ NOPURGE
CASE OSKB010050
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM PURGE ・ NOPURGE
CASE OSKB010050
SOURCE DFSMS
PURGE ・ NOPURGEとOSKB010050が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010050を同じ出力で読み、区切追跡の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010050
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010050.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010050が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の PURGE ・ NOPURGE と OSKB010050 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010050 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>PURGE ・ NOPURGE</strong></p><p>検証目的: 探索判定の・について、保持期限内のエントリを強制削除 (PURGE) するか、エラーで止める (NOPURGE、既定) か。「PURGE / NOPURGE」を読むと、DEFINE、ALTER、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010086の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、探索判定の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にPURGE ・ NOPURGEを指定し、OSKB010086の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND PURGE ・ NOPURGE
CASE OSKB010086
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM PURGE ・ NOPURGE
CASE OSKB010086
SOURCE DFSMS
PURGE ・ NOPURGEとOSKB010086が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010086を同じ出力で読み、探索判定の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010086
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010086.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010086が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の PURGE ・ NOPURGE と OSKB010086 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010086 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0084"><h3>SCRATCH / NOSCRATCH</h3><p class="kb-meta">分類: DEFINE_GDG ・ 難易度: 上級</p><p>SCRATCH / NOSCRATCHは、DFSMS / IDCAMS / VSAMのDEFINE_GDGで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切追跡の・で SCRATCH 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SCRATCH 属性の出力を取らず区切追跡の・の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、区切追跡として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して区切追跡の・の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切追跡の・へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切追跡正解では選択記号 B を採用し、正解名は区切追跡正解です。区切追跡根拠では SCRATCH 属性 は「区切追跡の・に関係する定義値と表示行を照合する区切追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は区切追跡根拠です。区切追跡追跡では SCRATCH 属性の属性行と IDC3009I を合わせ、追跡名は区切追跡追跡です。誤答側の問題点を分けます。 A: 区切追跡不足は名称や説明だけに寄り、判定名は区切追跡不足です。 B: 区切追跡正答は対象出力と項目説明を結び、根拠名は区切追跡正答です。 C: 区切追跡欠落は戻り値や記録番号に寄り、欠落名は区切追跡欠落です。 D: 区切追跡流用は別カテゴリの確認であり、排除名は区切追跡流用です。区切追跡初出では SCRATCH 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切追跡初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SCRATCH ・ NOSCRATCH</strong></p><p>検証目的: 終端追跡の・について、SCRATCH / NOSCRATCH は、DFSMS / IDCAMS / VSAM の DEFINE_GDG で機能名、見出し、または確認対象として参照する項目です。関連する操に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010045の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、終端追跡の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSCRATCH ・ NOSCRATCを指定し、OSKB010045の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND SCRATCH ・ NOSCRATC
CASE OSKB010045
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM SCRATCH ・ NOSCRATC
CASE OSKB010045
SOURCE DFSMS
SCRATCH ・ NOSCRATCとOSKB010045が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010045を同じ出力で読み、終端追跡の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010045
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010045.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010045が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の SCRATCH ・ NOSCRATC と OSKB010045 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010045 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0085"><h3>TO / FOR (GDG)</h3><p class="kb-meta">分類: DEFINE_GDG ・ 難易度: 上級</p><p>TO / FOR (GDG)は、DFSMS / IDCAMS / VSAMのDEFINE_GDGで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較追跡の・で TO ・ FOR (GDG)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. TO ・ FOR (GDG)の出力を取らず比較追跡の・の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、比較追跡の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して比較追跡の・の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較追跡の・へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較追跡正解では選択記号 B を採用し、正解名は比較追跡正解です。比較追跡根拠では TO ・ FOR (GDG) は「比較追跡の・に関係する定義値と表示行を照合する比較追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は比較追跡根拠です。比較追跡追跡では TO ・ FOR (GDG)の属性行と IDC3009I を合わせ、追跡名は比較追跡追跡です。誤答側の問題点を分けます。 A: 比較追跡不足は名称や説明だけに寄り、判定名は比較追跡不足です。 B: 比較追跡正答は対象出力と項目説明を結び、根拠名は比較追跡正答です。 C: 比較追跡欠落は戻り値や記録番号に寄り、欠落名は比較追跡欠落です。 D: 比較追跡流用は別カテゴリの確認であり、排除名は比較追跡流用です。比較追跡初出では TO ・ FOR (GDG)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較追跡初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>TO ・ FOR (GDG)</strong></p><p>検証目的: 条件追跡の・について、TO / FOR (GDG)は、DFSMS / IDCAMS / VSAM の DEFINE_GDG で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010049の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、条件追跡の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にTO ・ FOR (GDG)を指定し、OSKB010049の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND TO ・ FOR (GDG)
CASE OSKB010049
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM TO ・ FOR (GDG)
CASE OSKB010049
SOURCE DFSMS
TO ・ FOR (GDG)とOSKB010049が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010049を同じ出力で読み、条件追跡の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010049
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010049.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010049が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の TO ・ FOR (GDG) と OSKB010049 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010049 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## DEFINE_NONVSAM


<section class="kb-item" id="c06-i0086"><h3>DEFINE NONVSAM 基本</h3><p class="kb-meta">分類: DEFINE_NONVSAM ・ 難易度: 上級</p><p>VSAM 以外のデータセット (PS/PO/PDSE 等) を既存カタログにエントリとして登録する。通常は DISP=(NEW,CATLG) で自動登録される</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域追跡の基本に関する DEFINE NONVSAM 基本の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず値域追跡の基本の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域追跡の基本の証跡として保存して根拠にする。</li><li>C. DEFINE NONVSAM 基本の変更点を出力本文から切り離して値域追跡の基本の承認欄だけ残す。</li><li>D. IDC3009I を含む表示を保存し、説明欄との差分を値域追跡で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域追跡正解では選択記号 D を採用し、正解名は値域追跡正解です。値域追跡根拠では DEFINE NONVSAM 基本 は「DEFINE NONVSAM 基本の状態と出力メッセージを結び付ける値域追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は値域追跡根拠です。値域追跡保存では DEFINE NONVSAM 基本の出力行と IDC3009I を一緒に残し、保存名は値域追跡保存です。選択肢ごとの違いを示します。 A: 値域追跡欠落は戻り値や記録番号に寄り、欠落名は値域追跡欠落です。 B: 値域追跡流用は別カテゴリの確認であり、排除名は値域追跡流用です。 C: 値域追跡不足は名称や説明だけに寄り、判定名は値域追跡不足です。 D: 値域追跡正答は対象出力と項目説明を結び、根拠名は値域追跡正答です。値域追跡対象では DEFINE NONVSAM 基本を DFSMS の確認記録に残し、対象名は値域追跡対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEFINE NONVSAM 基本</strong></p><p>検証目的: 優先確認の基本について、VSAM 以外のデータセット (PS/PO/PDSE 等) を既存カタログにエントリとして登録する。通常は DISP=(NEW,CATLG) で自動登録されるに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030012の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、優先確認の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDEFINE NONVSAM 基本を指定し、OSKB030012の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DEFINE NONVSAM 基本
CASE OSKB030012
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DEFINE NONVSAM 基本
CASE OSKB030012
SOURCE DFSMS
DEFINE NONVSAM 基本とOSKB030012が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030012を同じ出力で読み、優先確認の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030012
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030012.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030012が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DEFINE NONVSAM 基本 と OSKB030012 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030012 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>DEFINE NONVSAM 基本</strong></p><p>検証目的: 範囲追跡の基本について、VSAM 以外のデータセット (PS/PO/PDSE 等) を既存カタログにエントリとして登録する。通常は DISP=(NEW,CATLG) で自動登録されるに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010051の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、範囲追跡の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDEFINE NONVSAM 基本を指定し、OSKB010051の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DEFINE NONVSAM 基本
CASE OSKB010051
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DEFINE NONVSAM 基本
CASE OSKB010051
SOURCE DFSMS
DEFINE NONVSAM 基本とOSKB010051が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010051を同じ出力で読み、範囲追跡の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010051
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010051.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010051が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DEFINE NONVSAM 基本 と OSKB010051 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010051 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0087"><h3>FILESEQUENCENUMBERS (テープ)</h3><p class="kb-meta">分類: DEFINE_NONVSAM ・ 難易度: 上級</p><p>FILESEQUENCENUMBERS (テープ)は、DFSMS / IDCAMS / VSAMのDEFINE_NONVSAMで機能名、見出し、または確認対象として参照する項目です。テープ上ファイル位置 (相対番号) のリスト。マルチファイルテープのカタログ化に使用。「FILESEQUENCENUMBERS (テープ)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧追跡のテープで FILESEQUENCENUMBERS 機能の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. FILESEQUENCENUMBERS 機能の出力を取らず復旧追跡のテープの説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、復旧追跡の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して復旧追跡のテープの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧追跡のテープへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧追跡正解では選択記号 B を採用し、正解名は復旧追跡正解です。復旧追跡根拠では FILESEQUENCENUMBERS 機能 は「復旧追跡のテープに関係する定義値と表示行を照合する復旧追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は復旧追跡根拠です。復旧追跡追跡では FILESEQUENCENUMBERS 機能の属性行と IDC3009I を合わせ、追跡名は復旧追跡追跡です。誤答側の問題点を分けます。 A: 復旧追跡不足は名称や説明だけに寄り、判定名は復旧追跡不足です。 B: 復旧追跡正答は対象出力と項目説明を結び、根拠名は復旧追跡正答です。 C: 復旧追跡欠落は戻り値や記録番号に寄り、欠落名は復旧追跡欠落です。 D: 復旧追跡流用は別カテゴリの確認であり、排除名は復旧追跡流用です。復旧追跡初出では FILESEQUENCENUMBERS 機能を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧追跡初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FILESEQUENCENUMBERS (テープ)</strong></p><p>検証目的: 記録追跡のテープについて、FILESEQUENCENUMBERS (テープ)は、DFSMS / IDCAMS / VSAM の DEFINE_NONVSAM で機能名、見出し、または確認対象として参照するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010053の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、記録追跡のテープの確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にFILESEQUENCENUMBERを指定し、OSKB010053の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND FILESEQUENCENUMBER
CASE OSKB010053
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM FILESEQUENCENUMBER
CASE OSKB010053
SOURCE DFSMS
FILESEQUENCENUMBERとOSKB010053が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010053を同じ出力で読み、記録追跡のテープの根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010053
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010053.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010053が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の FILESEQUENCENUMBER と OSKB010053 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010053 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0088"><h3>VOLUMES(volser) と DEVICETYPES</h3><p class="kb-meta">分類: DEFINE_NONVSAM ・ 難易度: 上級</p><p>非 VSAM カタログエントリの所在ボリュームと装置型 (3390 等)。多巻データセットでは複数 volser 並べる</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告追跡のストレージ管理に関係する VOLUMES 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果から対象行を抜き出し、警告追跡の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. VOLUMES 属性の名称と担当者名だけを残して警告追跡のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で警告追跡のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず警告追跡のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告追跡正解では選択記号 A を採用し、正解名は警告追跡正解です。警告追跡根拠では VOLUMES 属性 は「VOLUMES 属性の用途をストレージ管理の表示で確認する警告追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は警告追跡根拠です。警告追跡背景では DFSMS の VOLUMES 属性と IDC3009I を同じ証跡に残し、背景名は警告追跡背景です。他の選択肢を確認します。 A: 警告追跡正答は対象出力と項目説明を結び、根拠名は警告追跡正答です。 B: 警告追跡不足は名称や説明だけに寄り、判定名は警告追跡不足です。 C: 警告追跡流用は別カテゴリの確認であり、排除名は警告追跡流用です。 D: 警告追跡欠落は戻り値や記録番号に寄り、欠落名は警告追跡欠落です。警告追跡用語では VOLUMES 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告追跡用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>VOLUMES(volser) と DEVICETYPES</strong></p><p>検証目的: 優先追跡のとについて、非 VSAM カタログエントリの所在ボリュームと装置型 (3390 等)。多巻データセットでは複数 volser 並べるに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010052の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、優先追跡のとの確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にVOLUMES(volser) と を指定し、OSKB010052の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND VOLUMES(volser) と 
CASE OSKB010052
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM VOLUMES(volser) と 
CASE OSKB010052
SOURCE DFSMS
VOLUMES(volser) と とOSKB010052が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010052を同じ出力で読み、優先追跡のとの根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010052
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010052.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010052が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の VOLUMES(volser) と  と OSKB010052 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010052 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## DEFINE_PAGESPACE


<section class="kb-item" id="c06-i0089"><h3>DEFINE PAGESPACE 基本</h3><p class="kb-meta">分類: DEFINE_PAGESPACE ・ 難易度: 上級</p><p>DEFINE PAGESPACE 基本は、DFSMS / IDCAMS / VSAMのDEFINE_PAGESPACEで機能名、見出し、または確認対象として参照する項目です。ローカル/共通ページデータセット (PLPA/COMMON/LOCAL) を割り当てるコマンド。RSU IPL 後に PAGEADD で組み込む</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換検査の基本に関する DEFINE 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず置換検査の基本の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換検査の基本の証跡として保存して根拠にする。</li><li>C. DEFINE 機能の変更点を出力本文から切り離して置換検査の基本の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、置換検査の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換検査正解では選択記号 D を採用し、正解名は置換検査正解です。置換検査根拠では DEFINE 機能 は「DEFINE 機能の状態と出力メッセージを結び付ける置換検査項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は置換検査根拠です。置換検査保存では DEFINE 機能の出力行と IDC3009I を一緒に残し、保存名は置換検査保存です。選択肢ごとの違いを示します。 A: 置換検査欠落は戻り値や記録番号に寄り、欠落名は置換検査欠落です。 B: 置換検査流用は別カテゴリの確認であり、排除名は置換検査流用です。 C: 置換検査不足は名称や説明だけに寄り、判定名は置換検査不足です。 D: 置換検査正答は対象出力と項目説明を結び、根拠名は置換検査正答です。置換検査対象では DEFINE 機能を DFSMS の確認記録に残し、対象名は置換検査対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEFINE PAGESPACE 基本</strong></p><p>検証目的: 監査追跡の基本について、DEFINE PAGESPACE 基本は、DFSMS / IDCAMS / VSAM の DEFINE_PAGESPACE で機能名、見出し、または確認対象として参照する項目ですに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010059の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、監査追跡の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDEFINE PAGESPACE 基を指定し、OSKB010059の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DEFINE PAGESPACE 基
CASE OSKB010059
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DEFINE PAGESPACE 基
CASE OSKB010059
SOURCE DFSMS
DEFINE PAGESPACE 基とOSKB010059が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010059を同じ出力で読み、監査追跡の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010059
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010059.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010059が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DEFINE PAGESPACE 基 と OSKB010059 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010059 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0090"><h3>SWAP (廃止)</h3><p class="kb-meta">分類: DEFINE_PAGESPACE ・ 難易度: 上級</p><p>SWAP (廃止)は、DFSMS / IDCAMS / VSAMのDEFINE_PAGESPACEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端検査の廃止に関係する SWAP (廃止)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、終端検査で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. SWAP (廃止)の名称と担当者名だけを残して終端検査の廃止の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で終端検査の廃止を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず終端検査の廃止の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端検査正解では選択記号 A を採用し、正解名は終端検査正解です。終端検査根拠では SWAP (廃止) は「SWAP (廃止)の用途をストレージ管理の表示で確認する終端検査項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は終端検査根拠です。終端検査背景では DFSMS の SWAP (廃止)と IDC3009I を同じ証跡に残し、背景名は終端検査背景です。他の選択肢を確認します。 A: 終端検査正答は対象出力と項目説明を結び、根拠名は終端検査正答です。 B: 終端検査不足は名称や説明だけに寄り、判定名は終端検査不足です。 C: 終端検査流用は別カテゴリの確認であり、排除名は終端検査流用です。 D: 終端検査欠落は戻り値や記録番号に寄り、欠落名は終端検査欠落です。終端検査用語では SWAP (廃止)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端検査用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SWAP (廃止)</strong></p><p>検証目的: 変更追跡の廃止について、SWAP (廃止)は、DFSMS / IDCAMS / VSAM の DEFINE_PAGESPACE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010060の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、変更追跡の廃止の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSWAP (廃止)を指定し、OSKB010060の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND SWAP (廃止)
CASE OSKB010060
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM SWAP (廃止)
CASE OSKB010060
SOURCE DFSMS
SWAP (廃止)とOSKB010060が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010060を同じ出力で読み、変更追跡の廃止の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010060
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010060.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010060が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の SWAP (廃止) と OSKB010060 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010060 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## DEFINE_PATH


<section class="kb-item" id="c06-i0091"><h3>DEFINE PATH 基本</h3><p class="kb-meta">分類: DEFINE_PATH ・ 難易度: 上級</p><p>DEFINE PATH 基本は、DFSMS / IDCAMS / VSAMのDEFINE_PATHで確認する項目です。AIX 経由でベースクラスターにアクセスするための論理エントリ。アプリは PATH 名を OPEN するだけで AIX 経由のアクセスが可能</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端追跡の基本に関係する DEFINE PATH 基本の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果から対象行を抜き出し、終端追跡の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. DEFINE PATH 基本の名称と担当者名だけを残して終端追跡の基本の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で終端追跡の基本を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず終端追跡の基本の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端追跡正解では選択記号 A を採用し、正解名は終端追跡正解です。終端追跡根拠では DEFINE PATH 基本 は「DEFINE PATH 基本の用途をストレージ管理の表示で確認する終端追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は終端追跡根拠です。終端追跡背景では DFSMS の DEFINE PATH 基本と IDC3009I を同じ証跡に残し、背景名は終端追跡背景です。他の選択肢を確認します。 A: 終端追跡正答は対象出力と項目説明を結び、根拠名は終端追跡正答です。 B: 終端追跡不足は名称や説明だけに寄り、判定名は終端追跡不足です。 C: 終端追跡流用は別カテゴリの確認であり、排除名は終端追跡流用です。 D: 終端追跡欠落は戻り値や記録番号に寄り、欠落名は終端追跡欠落です。終端追跡用語では DEFINE PATH 基本を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端追跡用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DEFINE PATH 基本</strong></p><p>検証目的: 変更照合の基本について、DEFINE PATH 基本は、DFSMS / IDCAMS / VSAM の DEFINE_PATH で確認する項目です。AIX 経由でベースクラスターにアクセスするための論理に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010040の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、変更照合の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDEFINE PATH 基本を指定し、OSKB010040の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DEFINE PATH 基本
CASE OSKB010040
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DEFINE PATH 基本
CASE OSKB010040
SOURCE DFSMS
DEFINE PATH 基本とOSKB010040が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010040を同じ出力で読み、変更照合の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010040
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010040.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010040が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DEFINE PATH 基本 と OSKB010040 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010040 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0092"><h3>PATHENTRY(aixname)</h3><p class="kb-meta">分類: DEFINE_PATH ・ 難易度: 上級</p><p>PATHENTRY(aixname)は、DFSMS / IDCAMS / VSAMのDEFINE_PATHで機能名、見出し、または確認対象として参照する項目です。PATH が紐付く代替インデックス (AIX) 名。AIX から ベース の経路を確立する。PATH が紐付く代替インデックス (AIX) 名。AIX → ベース の経路を確立する</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索追跡のストレージ管理で PATHENTRY(aixname)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. PATHENTRY(aixname)の出力を取らず探索追跡のストレージ管理の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、探索追跡の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して探索追跡のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索追跡のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索追跡正解では選択記号 B を採用し、正解名は探索追跡正解です。探索追跡根拠では PATHENTRY(aixname) は「探索追跡のストレージ管理に関係する定義値と表示行を照合する探索追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は探索追跡根拠です。探索追跡追跡では PATHENTRY(aixname)の属性行と IDC3009I を合わせ、追跡名は探索追跡追跡です。誤答側の問題点を分けます。 A: 探索追跡不足は名称や説明だけに寄り、判定名は探索追跡不足です。 B: 探索追跡正答は対象出力と項目説明を結び、根拠名は探索追跡正答です。 C: 探索追跡欠落は戻り値や記録番号に寄り、欠落名は探索追跡欠落です。 D: 探索追跡流用は別カテゴリの確認であり、排除名は探索追跡流用です。探索追跡初出では PATHENTRY(aixname)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索追跡初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>PATHENTRY(aixname)</strong></p><p>検証目的: 区切確認のストレージ管理について、PATHENTRY(aixname)は、DFSMS / IDCAMS / VSAM の DEFINE_PATH で機能名、見出し、または確認対象として参照する項目です。PATHに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030010の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、区切確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にPATHENTRY(aixname)を指定し、OSKB030010の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND PATHENTRY(aixname)
CASE OSKB030010
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM PATHENTRY(aixname)
CASE OSKB030010
SOURCE DFSMS
PATHENTRY(aixname)とOSKB030010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030010を同じ出力で読み、区切確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030010
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030010.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の PATHENTRY(aixname) と OSKB030010 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>PATHENTRY(aixname)</strong></p><p>検証目的: 構文追跡のストレージ管理について、PATHENTRY(aixname)は、DFSMS / IDCAMS / VSAM の DEFINE_PATH で機能名、見出し、または確認対象として参照する項目です。PATHに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010041の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、構文追跡のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にPATHENTRY(aixname)を指定し、OSKB010041の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND PATHENTRY(aixname)
CASE OSKB010041
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM PATHENTRY(aixname)
CASE OSKB010041
SOURCE DFSMS
PATHENTRY(aixname)とOSKB010041が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010041を同じ出力で読み、構文追跡のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010041
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010041.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010041が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の PATHENTRY(aixname) と OSKB010041 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010041 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0093"><h3>UPDATE / NOUPDATE (PATH)</h3><p class="kb-meta">分類: DEFINE_PATH ・ 難易度: 上級</p><p>UPDATE / NOUPDATE (PATH)は、DFSMS / IDCAMS / VSAMのDEFINE_PATHで確認する項目です。PATH 経由更新時にベースおよび UPGRADE AIX を自動更新するか。NOUPDATE は読み取り専用パスとして軽量</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書追跡の・でストレージ管理の運用確認を行います。UPDATE 属性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で上書追跡の・を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず上書追跡の・を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて上書追跡の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. UPDATE 属性の属性行を読まず上書追跡の・の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書追跡正解では選択記号 C を採用し、正解名は上書追跡正解です。上書追跡根拠では UPDATE 属性 は「DFSMS で UPDATE 属性の扱いを記録する上書追跡項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は上書追跡根拠です。上書追跡受渡では UPDATE 属性の表示結果と IDC3009I を同じ確認単位にし、受渡名は上書追跡受渡です。不適切な選択肢を整理します。 A: 上書追跡流用は別カテゴリの確認であり、排除名は上書追跡流用です。 B: 上書追跡欠落は戻り値や記録番号に寄り、欠落名は上書追跡欠落です。 C: 上書追跡正答は対象出力と項目説明を結び、根拠名は上書追跡正答です。 D: 上書追跡不足は名称や説明だけに寄り、判定名は上書追跡不足です。上書追跡資料では UPDATE 属性の使い方を出典欄から追跡し、資料名は上書追跡資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UPDATE ・ NOUPDATE (PATH)</strong></p><p>検証目的: 展開追跡の・について、UPDATE / NOUPDATE (PATH)は、DFSMS / IDCAMS / VSAM の DEFINE_PATH で確認する項目です。PATH 経由更新時にベースおよびに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010042の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、展開追跡の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にUPDATE ・ NOUPDATE を指定し、OSKB010042の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND UPDATE ・ NOUPDATE 
CASE OSKB010042
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM UPDATE ・ NOUPDATE 
CASE OSKB010042
SOURCE DFSMS
UPDATE ・ NOUPDATE とOSKB010042が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010042を同じ出力で読み、展開追跡の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010042
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010042.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010042が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の UPDATE ・ NOUPDATE  と OSKB010042 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010042 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## DELETE


<section class="kb-item" id="c06-i0094"><h3>AIX (ALTERNATEINDEX)</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>AIX (ALTERNATEINDEX)は、DFSMS / IDCAMS / VSAMのDELETEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換判定のストレージ管理に関する AIX 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず置換判定のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換判定のストレージ管理の証跡として保存して根拠にする。</li><li>C. AIX 属性の変更点を出力本文から切り離して置換判定のストレージ管理の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC3009I を読み、置換判定の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換判定正解では選択記号 D を採用し、正解名は置換判定正解です。置換判定根拠では AIX 属性 は「AIX 属性の状態と出力メッセージを結び付ける置換判定項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は置換判定根拠です。置換判定保存では AIX 属性の出力行と IDC3009I を一緒に残し、保存名は置換判定保存です。選択肢ごとの違いを示します。 A: 置換判定欠落は戻り値や記録番号に寄り、欠落名は置換判定欠落です。 B: 置換判定流用は別カテゴリの確認であり、排除名は置換判定流用です。 C: 置換判定不足は名称や説明だけに寄り、判定名は置換判定不足です。 D: 置換判定正答は対象出力と項目説明を結び、根拠名は置換判定正答です。置換判定対象では AIX 属性を DFSMS の確認記録に残し、対象名は置換判定対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>AIX (ALTERNATEINDEX)</strong></p><p>検証目的: 監査検査のストレージ管理について、AIX (ALTERNATEINDEX)は、DFSMS / IDCAMS / VSAM の DELETE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010079の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、監査検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にAIX (ALTERNATEINDEを指定し、OSKB010079の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND AIX (ALTERNATEINDE
CASE OSKB010079
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM AIX (ALTERNATEINDE
CASE OSKB010079
SOURCE DFSMS
AIX (ALTERNATEINDEとOSKB010079が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010079を同じ出力で読み、監査検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010079
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010079.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010079が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の AIX (ALTERNATEINDE と OSKB010079 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010079 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0095"><h3>ALIAS</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>ALIASは、DFSMS / IDCAMS / VSAMのDELETEで機能名、見出し、または確認対象として参照する項目です。ALIAS エントリの削除。ALIAS 配下に登録済みの実データセットがあるとカタログ解決不能になるため要注意</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切判定のストレージ管理で ALIAS の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. ALIAS の出力を取らず区切判定のストレージ管理の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、区切判定の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して区切判定のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切判定のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切判定正解では選択記号 B を採用し、正解名は区切判定正解です。区切判定根拠では ALIAS は「区切判定のストレージ管理に関係する定義値と表示行を照合する区切判定項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は区切判定根拠です。区切判定追跡では ALIAS の属性行と IDC0001I を合わせ、追跡名は区切判定追跡です。誤答側の問題点を分けます。 A: 区切判定不足は名称や説明だけに寄り、判定名は区切判定不足です。 B: 区切判定正答は対象出力と項目説明を結び、根拠名は区切判定正答です。 C: 区切判定欠落は戻り値や記録番号に寄り、欠落名は区切判定欠落です。 D: 区切判定流用は別カテゴリの確認であり、排除名は区切判定流用です。区切判定初出では ALIAS を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切判定初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ALIAS</strong></p><p>検証目的: 終端判定のストレージ管理について、ALIAS は、DFSMS / IDCAMS / VSAM の DELETE で機能名、見出し、または確認対象として参照する項目です。ALIAS エントリの削除。ALIAS 配下にに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010085の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、終端判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にALIASを指定し、OSKB010085の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ALIAS
CASE OSKB010085
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ALIAS
CASE OSKB010085
SOURCE DFSMS
ALIASとOSKB010085が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010085を同じ出力で読み、終端判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010085
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010085.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010085が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ALIAS と OSKB010085 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010085 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0096"><h3>CLUSTER</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>CLUSTERは、DFSMS / IDCAMS / VSAMのDELETEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出判定のストレージ管理でストレージ管理の運用確認を行います。CLUSTER の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で呼出判定のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず呼出判定のストレージ管理を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて呼出判定の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. CLUSTER の属性行を読まず呼出判定のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出判定正解では選択記号 C を採用し、正解名は呼出判定正解です。呼出判定根拠では CLUSTER は「DFSMS で CLUSTER の扱いを記録する呼出判定項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は呼出判定根拠です。呼出判定受渡では CLUSTER の表示結果と IDC3009I を同じ確認単位にし、受渡名は呼出判定受渡です。不適切な選択肢を整理します。 A: 呼出判定流用は別カテゴリの確認であり、排除名は呼出判定流用です。 B: 呼出判定欠落は戻り値や記録番号に寄り、欠落名は呼出判定欠落です。 C: 呼出判定正答は対象出力と項目説明を結び、根拠名は呼出判定正答です。 D: 呼出判定不足は名称や説明だけに寄り、判定名は呼出判定不足です。呼出判定資料では CLUSTER の使い方を出典欄から追跡し、資料名は呼出判定資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CLUSTER</strong></p><p>検証目的: 復旧検査のストレージ管理について、CLUSTER は、DFSMS / IDCAMS / VSAM の DELETE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010078の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、復旧検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCLUSTERを指定し、OSKB010078の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND CLUSTER
CASE OSKB010078
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM CLUSTER
CASE OSKB010078
SOURCE DFSMS
CLUSTERとOSKB010078が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010078を同じ出力で読み、復旧検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010078
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010078.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010078が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の CLUSTER と OSKB010078 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010078 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0097"><h3>DELETE 基本</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>カタログエントリと (適用可能なら) 物理データセットを削除する IDCAMS コマンド。「DELETE 基本」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開判定の基本で DELETE 基本の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. DELETE 基本の出力を取らず展開判定の基本の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、展開判定の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して展開判定の基本の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開判定の基本へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開判定正解では選択記号 B を採用し、正解名は展開判定正解です。展開判定根拠では DELETE 基本 は「展開判定の基本に関係する定義値と表示行を照合する展開判定項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は展開判定根拠です。展開判定追跡では DELETE 基本の属性行と IDC3009I を合わせ、追跡名は展開判定追跡です。誤答側の問題点を分けます。 A: 展開判定不足は名称や説明だけに寄り、判定名は展開判定不足です。 B: 展開判定正答は対象出力と項目説明を結び、根拠名は展開判定正答です。 C: 展開判定欠落は戻り値や記録番号に寄り、欠落名は展開判定欠落です。 D: 展開判定流用は別カテゴリの確認であり、排除名は展開判定流用です。展開判定初出では DELETE 基本を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開判定初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DELETE 基本</strong></p><p>検証目的: 警告検査の基本について、カタログエントリと (適用可能なら) 物理データセットを削除する IDCAMS コマンド。「DELETE 基本」を読むと、DEFINE、ALTER、DELETE、LISTCに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010077の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、警告検査の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDELETE 基本を指定し、OSKB010077の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DELETE 基本
CASE OSKB010077
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DELETE 基本
CASE OSKB010077
SOURCE DFSMS
DELETE 基本とOSKB010077が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010077を同じ出力で読み、警告検査の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010077
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010077.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010077が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DELETE 基本 と OSKB010077 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010077 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0098"><h3>ERASE / NOERASE</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>ERASE / NOERASEは、DFSMS / IDCAMS / VSAMのDELETEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先判定の・に関する ERASE ・ NOERASE の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず優先判定の・の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先判定の・の証跡として保存して根拠にする。</li><li>C. ERASE ・ NOERASE の変更点を出力本文から切り離して優先判定の・の承認欄だけ残す。</li><li>D. IDC0001I を含む表示を保存し、説明欄との差分を優先判定で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先判定正解では選択記号 D を採用し、正解名は優先判定正解です。優先判定根拠では ERASE ・ NOERASE は「ERASE ・ NOERASE の状態と出力メッセージを結び付ける優先判定項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は優先判定根拠です。優先判定保存では ERASE ・ NOERASE の出力行と IDC0001I を一緒に残し、保存名は優先判定保存です。選択肢ごとの違いを示します。 A: 優先判定欠落は戻り値や記録番号に寄り、欠落名は優先判定欠落です。 B: 優先判定流用は別カテゴリの確認であり、排除名は優先判定流用です。 C: 優先判定不足は名称や説明だけに寄り、判定名は優先判定不足です。 D: 優先判定正答は対象出力と項目説明を結び、根拠名は優先判定正答です。優先判定対象では ERASE ・ NOERASE を DFSMS の確認記録に残し、対象名は優先判定対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ERASE ・ NOERASE</strong></p><p>検証目的: 上書判定の・について、ERASE / NOERASE は、DFSMS / IDCAMS / VSAM の DELETE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010087の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、上書判定の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にERASE ・ NOERASEを指定し、OSKB010087の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ERASE ・ NOERASE
CASE OSKB010087
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ERASE ・ NOERASE
CASE OSKB010087
SOURCE DFSMS
ERASE ・ NOERASEとOSKB010087が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010087を同じ出力で読み、上書判定の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010087
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010087.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010087が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ERASE ・ NOERASE と OSKB010087 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010087 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0099"><h3>FORCE</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>FORCEは、DFSMS / IDCAMS / VSAMのDELETEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録判定のストレージ管理に関係する FORCE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、記録判定の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. FORCE の名称と担当者名だけを残して記録判定のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で記録判定のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず記録判定のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録判定正解では選択記号 A を採用し、正解名は記録判定正解です。記録判定根拠では FORCE は「FORCE の用途をストレージ管理の表示で確認する記録判定項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は記録判定根拠です。記録判定背景では DFSMS の FORCE と IDC0001I を同じ証跡に残し、背景名は記録判定背景です。他の選択肢を確認します。 A: 記録判定正答は対象出力と項目説明を結び、根拠名は記録判定正答です。 B: 記録判定不足は名称や説明だけに寄り、判定名は記録判定不足です。 C: 記録判定流用は別カテゴリの確認であり、排除名は記録判定流用です。 D: 記録判定欠落は戻り値や記録番号に寄り、欠落名は記録判定欠落です。記録判定用語では FORCE を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録判定用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>FORCE</strong></p><p>検証目的: 出力判定のストレージ管理について、FORCE は、DFSMS / IDCAMS / VSAM の DELETE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010088の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、出力判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にFORCEを指定し、OSKB010088の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND FORCE
CASE OSKB010088
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM FORCE
CASE OSKB010088
SOURCE DFSMS
FORCEとOSKB010088が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010088を同じ出力で読み、出力判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010088
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010088.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010088が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の FORCE と OSKB010088 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010088 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0100"><h3>GDG</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>GDGは、DFSMS / IDCAMS / VSAMのDELETEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索判定のストレージ管理で GDG の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. GDG の出力を取らず探索判定のストレージ管理の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、探索判定として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して探索判定のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索判定のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索判定正解では選択記号 B を採用し、正解名は探索判定正解です。探索判定根拠では GDG は「探索判定のストレージ管理に関係する定義値と表示行を照合する探索判定項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は探索判定根拠です。探索判定追跡では GDG の属性行と IDC3009I を合わせ、追跡名は探索判定追跡です。誤答側の問題点を分けます。 A: 探索判定不足は名称や説明だけに寄り、判定名は探索判定不足です。 B: 探索判定正答は対象出力と項目説明を結び、根拠名は探索判定正答です。 C: 探索判定欠落は戻り値や記録番号に寄り、欠落名は探索判定欠落です。 D: 探索判定流用は別カテゴリの確認であり、排除名は探索判定流用です。探索判定初出では GDG を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索判定初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>GDG</strong></p><p>検証目的: 復旧確認のストレージ管理について、GDG は、DFSMS / IDCAMS / VSAM の DELETE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030018の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、復旧確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にGDGを指定し、OSKB030018の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND GDG
CASE OSKB030018
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM GDG
CASE OSKB030018
SOURCE DFSMS
GDGとOSKB030018が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030018を同じ出力で読み、復旧確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030018
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030018.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030018が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の GDG と OSKB030018 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030018 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>GDG</strong></p><p>検証目的: 構文判定のストレージ管理について、GDG は、DFSMS / IDCAMS / VSAM の DELETE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010081の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、構文判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にGDGを指定し、OSKB010081の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND GDG
CASE OSKB010081
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM GDG
CASE OSKB010081
SOURCE DFSMS
GDGとOSKB010081が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010081を同じ出力で読み、構文判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010081
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010081.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010081が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の GDG と OSKB010081 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010081 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0101"><h3>NONVSAM</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>非 VSAM カタログエントリの削除。物理削除は VOLUMES 指定とそのボリューム上の VTOC 操作を伴う</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書判定のストレージ管理でストレージ管理の運用確認を行います。NONVSAM の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で上書判定のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず上書判定のストレージ管理を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書判定の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. NONVSAM の属性行を読まず上書判定のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書判定正解では選択記号 C を採用し、正解名は上書判定正解です。上書判定根拠では NONVSAM は「DFSMS で NONVSAM の扱いを記録する上書判定項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は上書判定根拠です。上書判定受渡では NONVSAM の表示結果と IDC0001I を同じ確認単位にし、受渡名は上書判定受渡です。不適切な選択肢を整理します。 A: 上書判定流用は別カテゴリの確認であり、排除名は上書判定流用です。 B: 上書判定欠落は戻り値や記録番号に寄り、欠落名は上書判定欠落です。 C: 上書判定正答は対象出力と項目説明を結び、根拠名は上書判定正答です。 D: 上書判定不足は名称や説明だけに寄り、判定名は上書判定不足です。上書判定資料では NONVSAM の使い方を出典欄から追跡し、資料名は上書判定資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>NONVSAM</strong></p><p>検証目的: 展開判定のストレージ管理について、非 VSAM カタログエントリの削除。物理削除は VOLUMES 指定とそのボリューム上の VTOC 操作を伴うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010082の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、展開判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にNONVSAMを指定し、OSKB010082の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND NONVSAM
CASE OSKB010082
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM NONVSAM
CASE OSKB010082
SOURCE DFSMS
NONVSAMとOSKB010082が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010082を同じ出力で読み、展開判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010082
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010082.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010082が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の NONVSAM と OSKB010082 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010082 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0102"><h3>PAGESPACE</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>PAGESPACEは、DFSMS / IDCAMS / VSAMのDELETEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件判定のストレージ管理に関係する PAGESPACE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件判定で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. PAGESPACE の名称と担当者名だけを残して条件判定のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で条件判定のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず条件判定のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件判定正解では選択記号 A を採用し、正解名は条件判定正解です。条件判定根拠では PAGESPACE は「PAGESPACE の用途をストレージ管理の表示で確認する条件判定項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は条件判定根拠です。条件判定背景では DFSMS の PAGESPACE と IDC0001I を同じ証跡に残し、背景名は条件判定背景です。他の選択肢を確認します。 A: 条件判定正答は対象出力と項目説明を結び、根拠名は条件判定正答です。 B: 条件判定不足は名称や説明だけに寄り、判定名は条件判定不足です。 C: 条件判定流用は別カテゴリの確認であり、排除名は条件判定流用です。 D: 条件判定欠落は戻り値や記録番号に寄り、欠落名は条件判定欠落です。条件判定用語では PAGESPACE を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件判定用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PAGESPACE</strong></p><p>検証目的: 置換判定のストレージ管理について、PAGESPACE は、DFSMS / IDCAMS / VSAM の DELETE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010084の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、置換判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にPAGESPACEを指定し、OSKB010084の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND PAGESPACE
CASE OSKB010084
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM PAGESPACE
CASE OSKB010084
SOURCE DFSMS
PAGESPACEとOSKB010084が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010084を同じ出力で読み、置換判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010084
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010084.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010084が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の PAGESPACE と OSKB010084 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010084 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0103"><h3>PATH</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>PATHは、DFSMS / IDCAMS / VSAMのDELETEで機能名、見出し、または確認対象として参照する項目です。PATH エントリのみ削除。ベース/AIX 自体は残る。「PATH」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端判定のストレージ管理に関係する PATH の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、終端判定の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. PATH の名称と担当者名だけを残して終端判定のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で終端判定のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず終端判定のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端判定正解では選択記号 A を採用し、正解名は終端判定正解です。終端判定根拠では PATH は「PATH の用途をストレージ管理の表示で確認する終端判定項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は終端判定根拠です。終端判定背景では DFSMS の PATH と IDC3009I を同じ証跡に残し、背景名は終端判定背景です。他の選択肢を確認します。 A: 終端判定正答は対象出力と項目説明を結び、根拠名は終端判定正答です。 B: 終端判定不足は名称や説明だけに寄り、判定名は終端判定不足です。 C: 終端判定流用は別カテゴリの確認であり、排除名は終端判定流用です。 D: 終端判定欠落は戻り値や記録番号に寄り、欠落名は終端判定欠落です。終端判定用語では PATH を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端判定用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PATH</strong></p><p>検証目的: 変更検査のストレージ管理について、PATH は、DFSMS / IDCAMS / VSAM の DELETE で機能名、見出し、または確認対象として参照する項目です。PATH エントリのみ削除。ベース/AIX 自体に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010080の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、変更検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にPATHを指定し、OSKB010080の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND PATH
CASE OSKB010080
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM PATH
CASE OSKB010080
SOURCE DFSMS
PATHとOSKB010080が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010080を同じ出力で読み、変更検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010080
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010080.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010080が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の PATH と OSKB010080 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010080 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0104"><h3>PURGE / NOPURGE</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>保持期限内のエントリを強制削除 (PURGE) するか、エラーで止める (NOPURGE、既定) か。「PURGE / NOPURGE」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p></section>


<section class="kb-item" id="c06-i0105"><h3>SCRATCH / NOSCRATCH (DELETE)</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>物理削除を伴うか (SCRATCH) カタログ解除のみか (NOSCRATCH)。非 VSAM や GDG 世代で意味を持つ。「SCRATCH / NOSCRATCH (DELETE)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較判定の・で SCRATCH 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. SCRATCH 属性の出力を取らず比較判定の・の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、比較判定の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して比較判定の・の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較判定の・へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較判定正解では選択記号 B を採用し、正解名は比較判定正解です。比較判定根拠では SCRATCH 属性 は「比較判定の・に関係する定義値と表示行を照合する比較判定項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は比較判定根拠です。比較判定追跡では SCRATCH 属性の属性行と IDC3009I を合わせ、追跡名は比較判定追跡です。誤答側の問題点を分けます。 A: 比較判定不足は名称や説明だけに寄り、判定名は比較判定不足です。 B: 比較判定正答は対象出力と項目説明を結び、根拠名は比較判定正答です。 C: 比較判定欠落は戻り値や記録番号に寄り、欠落名は比較判定欠落です。 D: 比較判定流用は別カテゴリの確認であり、排除名は比較判定流用です。比較判定初出では SCRATCH 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較判定初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SCRATCH ・ NOSCRATCH (DELETE)</strong></p><p>検証目的: 条件判定の・について、物理削除を伴うか (SCRATCH) カタログ解除のみか (NOSCRATCH)。非 VSAM や GDG 世代で意味を持つ。「SCRATCH / NOSCRATCH (Dに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010089の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、条件判定の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にSCRATCH ・ NOSCRATCを指定し、OSKB010089の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND SCRATCH ・ NOSCRATC
CASE OSKB010089
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM SCRATCH ・ NOSCRATC
CASE OSKB010089
SOURCE DFSMS
SCRATCH ・ NOSCRATCとOSKB010089が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010089を同じ出力で読み、条件判定の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010089
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010089.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010089が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の SCRATCH ・ NOSCRATC と OSKB010089 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010089 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0106"><h3>USERCATALOG</h3><p class="kb-meta">分類: DELETE ・ 難易度: 上級</p><p>USERCATALOGは、DFSMS / IDCAMS / VSAMのDELETEで機能名、見出し、または確認対象として参照する項目です。ユーザカタログ削除。FORCE 不可。先に内部エントリを空にしてから RECOVERY 用に EXPORT 推奨。「USERCATALOG」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力判定のストレージ管理に関する USERCATALOG の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず出力判定のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力判定のストレージ管理の証跡として保存して根拠にする。</li><li>C. USERCATALOG の変更点を出力本文から切り離して出力判定のストレージ管理の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、出力判定の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力判定正解では選択記号 D を採用し、正解名は出力判定正解です。出力判定根拠では USERCATALOG は「USERCATALOG の状態と出力メッセージを結び付ける出力判定項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は出力判定根拠です。出力判定保存では USERCATALOG の出力行と IDC3009I を一緒に残し、保存名は出力判定保存です。選択肢ごとの違いを示します。 A: 出力判定欠落は戻り値や記録番号に寄り、欠落名は出力判定欠落です。 B: 出力判定流用は別カテゴリの確認であり、排除名は出力判定流用です。 C: 出力判定不足は名称や説明だけに寄り、判定名は出力判定不足です。 D: 出力判定正答は対象出力と項目説明を結び、根拠名は出力判定正答です。出力判定対象では USERCATALOG を DFSMS の確認記録に残し、対象名は出力判定対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>USERCATALOG</strong></p><p>検証目的: 呼出判定のストレージ管理について、USERCATALOG は、DFSMS / IDCAMS / VSAM の DELETE で機能名、見出し、または確認対象として参照する項目です。ユーザカタログ削除。FORCE 不に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010083の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、呼出判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にUSERCATALOGを指定し、OSKB010083の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND USERCATALOG
CASE OSKB010083
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM USERCATALOG
CASE OSKB010083
SOURCE DFSMS
USERCATALOGとOSKB010083が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB010083を同じ出力で読み、呼出判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB010083
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB010083.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB010083が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の USERCATALOG と OSKB010083 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB010083 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## DIAGNOSE


<section class="kb-item" id="c06-i0107"><h3>COMPAREDD</h3><p class="kb-meta">分類: DIAGNOSE ・ 難易度: 上級</p><p>COMPAREDDは、DFSMS / IDCAMS / VSAMのDIAGNOSEで機能名、見出し、または確認対象として参照する項目です。BCS と VVDS の相互参照を比較。エントリ不整合 (片側のみ存在等) を炙り出す。「COMPAREDD」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査記録のストレージ管理でストレージ管理の運用確認を行います。COMPAREDD の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で監査記録のストレージ管理を確認した扱いにする。</li><li>B. IDC3009I の有無を確認せず監査記録のストレージ管理を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて監査記録の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. COMPAREDD の属性行を読まず監査記録のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査記録正解では選択記号 C を採用し、正解名は監査記録正解です。監査記録根拠では COMPAREDD は「DFSMS で COMPAREDD の扱いを記録する監査記録項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は監査記録根拠です。監査記録受渡では COMPAREDD の表示結果と IDC3009I を同じ確認単位にし、受渡名は監査記録受渡です。不適切な選択肢を整理します。 A: 監査記録流用は別カテゴリの確認であり、排除名は監査記録流用です。 B: 監査記録欠落は戻り値や記録番号に寄り、欠落名は監査記録欠落です。 C: 監査記録正答は対象出力と項目説明を結び、根拠名は監査記録正答です。 D: 監査記録不足は名称や説明だけに寄り、判定名は監査記録不足です。監査記録資料では COMPAREDD の使い方を出典欄から追跡し、資料名は監査記録資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>COMPAREDD</strong></p><p>検証目的: 比較確認のストレージ管理について、COMPAREDD は、DFSMS / IDCAMS / VSAM の DIAGNOSE で機能名、見出し、または確認対象として参照する項目です。BCS と VVDS の相互参照をに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020014の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、比較確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCOMPAREDDを指定し、OSKB020014の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND COMPAREDD
CASE OSKB020014
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM COMPAREDD
CASE OSKB020014
SOURCE DFSMS
COMPAREDDとOSKB020014が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020014を同じ出力で読み、比較確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020014
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020014.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020014が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の COMPAREDD と OSKB020014 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020014 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0108"><h3>DIAGNOSE 基本</h3><p class="kb-meta">分類: DIAGNOSE ・ 難易度: 上級</p><p>DIAGNOSE 基本は、DFSMS / IDCAMS / VSAMのDIAGNOSEで機能名、見出し、または確認対象として参照する項目です。カタログ (BCS) または VVDS の構造を診断。ICF カタログ整合性検査の中核コマンド。「DIAGNOSE 基本」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域記録の基本に関する DIAGNOSE 基本の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず値域記録の基本の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域記録の基本の証跡として保存して根拠にする。</li><li>C. DIAGNOSE 基本の変更点を出力本文から切り離して値域記録の基本の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、値域記録の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域記録正解では選択記号 D を採用し、正解名は値域記録正解です。値域記録根拠では DIAGNOSE 基本 は「DIAGNOSE 基本の状態と出力メッセージを結び付ける値域記録項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は値域記録根拠です。値域記録保存では DIAGNOSE 基本の出力行と IDC3009I を一緒に残し、保存名は値域記録保存です。選択肢ごとの違いを示します。 A: 値域記録欠落は戻り値や記録番号に寄り、欠落名は値域記録欠落です。 B: 値域記録流用は別カテゴリの確認であり、排除名は値域記録流用です。 C: 値域記録不足は名称や説明だけに寄り、判定名は値域記録不足です。 D: 値域記録正答は対象出力と項目説明を結び、根拠名は値域記録正答です。値域記録対象では DIAGNOSE 基本を DFSMS の確認記録に残し、対象名は値域記録対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>DIAGNOSE 基本</strong></p><p>検証目的: 出力照合の基本について、DIAGNOSE 基本は、DFSMS / IDCAMS / VSAM の DIAGNOSE で機能名、見出し、または確認対象として参照する項目です。カタログ (BCS) またはに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030028の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、出力照合の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDIAGNOSE 基本を指定し、OSKB030028の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DIAGNOSE 基本
CASE OSKB030028
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DIAGNOSE 基本
CASE OSKB030028
SOURCE DFSMS
DIAGNOSE 基本とOSKB030028が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB030028を同じ出力で読み、出力照合の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB030028
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB030028.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB030028が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DIAGNOSE 基本 と OSKB030028 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB030028 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>DIAGNOSE 基本</strong></p><p>検証目的: 範囲確認の基本について、DIAGNOSE 基本は、DFSMS / IDCAMS / VSAM の DIAGNOSE で機能名、見出し、または確認対象として参照する項目です。カタログ (BCS) またはに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020011の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、範囲確認の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDIAGNOSE 基本を指定し、OSKB020011の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DIAGNOSE 基本
CASE OSKB020011
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DIAGNOSE 基本
CASE OSKB020011
SOURCE DFSMS
DIAGNOSE 基本とOSKB020011が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020011を同じ出力で読み、範囲確認の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020011
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020011.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020011が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の DIAGNOSE 基本 と OSKB020011 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020011 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0109"><h3>ICFCATALOG / VVDS</h3><p class="kb-meta">分類: DIAGNOSE ・ 難易度: 上級</p><p>DIAGNOSE 対象を BCS (ICFCATALOG) または VVDS で指定。両者の関係を別個に検査する</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告記録の・に関係する ICFCATALOG ・ VVDS の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、警告記録で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. ICFCATALOG ・ VVDS の名称と担当者名だけを残して警告記録の・の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で警告記録の・を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず警告記録の・の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告記録正解では選択記号 A を採用し、正解名は警告記録正解です。警告記録根拠では ICFCATALOG ・ VVDS は「ICFCATALOG ・ VVDS の用途をストレージ管理の表示で確認する警告記録項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は警告記録根拠です。警告記録背景では DFSMS の ICFCATALOG ・ VVDS と IDC0001I を同じ証跡に残し、背景名は警告記録背景です。他の選択肢を確認します。 A: 警告記録正答は対象出力と項目説明を結び、根拠名は警告記録正答です。 B: 警告記録不足は名称や説明だけに寄り、判定名は警告記録不足です。 C: 警告記録流用は別カテゴリの確認であり、排除名は警告記録流用です。 D: 警告記録欠落は戻り値や記録番号に寄り、欠落名は警告記録欠落です。警告記録用語では ICFCATALOG ・ VVDS を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告記録用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ICFCATALOG ・ VVDS</strong></p><p>検証目的: 優先確認の・について、DIAGNOSE 対象を BCS (ICFCATALOG) または VVDS で指定。両者の関係を別個に検査するに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020012の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、優先確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にICFCATALOG ・ VVDSを指定し、OSKB020012の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ICFCATALOG ・ VVDS
CASE OSKB020012
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ICFCATALOG ・ VVDS
CASE OSKB020012
SOURCE DFSMS
ICFCATALOG ・ VVDSとOSKB020012が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020012を同じ出力で読み、優先確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020012
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020012.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020012が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ICFCATALOG ・ VVDS と OSKB020012 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020012 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0110"><h3>INCLUDE / EXCLUDE</h3><p class="kb-meta">分類: DIAGNOSE ・ 難易度: 上級</p><p>INCLUDE / EXCLUDEは、DFSMS / IDCAMS / VSAMのDIAGNOSEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧記録の・で INCLUDE ・ EXCLUDE の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. INCLUDE ・ EXCLUDE の出力を取らず復旧記録の・の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、復旧記録の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して復旧記録の・の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧記録の・へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧記録正解では選択記号 B を採用し、正解名は復旧記録正解です。復旧記録根拠では INCLUDE ・ EXCLUDE は「復旧記録の・に関係する定義値と表示行を照合する復旧記録項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は復旧記録根拠です。復旧記録追跡では INCLUDE ・ EXCLUDE の属性行と IDC0001I を合わせ、追跡名は復旧記録追跡です。誤答側の問題点を分けます。 A: 復旧記録不足は名称や説明だけに寄り、判定名は復旧記録不足です。 B: 復旧記録正答は対象出力と項目説明を結び、根拠名は復旧記録正答です。 C: 復旧記録欠落は戻り値や記録番号に寄り、欠落名は復旧記録欠落です。 D: 復旧記録流用は別カテゴリの確認であり、排除名は復旧記録流用です。復旧記録初出では INCLUDE ・ EXCLUDE を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧記録初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>INCLUDE ・ EXCLUDE</strong></p><p>検証目的: 記録確認の・について、INCLUDE / EXCLUDE は、DFSMS / IDCAMS / VSAM の DIAGNOSE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020013の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、記録確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にINCLUDE ・ EXCLUDEを指定し、OSKB020013の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND INCLUDE ・ EXCLUDE
CASE OSKB020013
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM INCLUDE ・ EXCLUDE
CASE OSKB020013
SOURCE DFSMS
INCLUDE ・ EXCLUDEとOSKB020013が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020013を同じ出力で読み、記録確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020013
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020013.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020013が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の INCLUDE ・ EXCLUDE と OSKB020013 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020013 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## DSS


<section class="kb-item" id="c06-i0111"><h3>BUILDSA</h3><p class="kb-meta">分類: DSS ・ 難易度: 上級</p><p>BUILDSAは、DFSMS / IDCAMS / VSAMのDSSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdss Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査確認再のストレージ管理でストレージ管理の運用確認を行います。BUILDSA の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で監査確認再のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず監査確認再のストレージ管理を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査確認再の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. BUILDSA の属性行を読まず監査確認再のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査確認再正解では選択記号 C を採用し、正解名は監査確認再正解です。監査確認再根拠では BUILDSA は「DFSMS で BUILDSA の扱いを記録する監査確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は監査確認再根拠です。監査確認再受渡では BUILDSA の表示結果と IDC0001I を同じ確認単位にし、受渡名は監査確認再受渡です。不適切な選択肢を整理します。 A: 監査確認再流用は別カテゴリの確認であり、排除名は監査確認再流用です。 B: 監査確認再欠落は戻り値や記録番号に寄り、欠落名は監査確認再欠落です。 C: 監査確認再正答は対象出力と項目説明を結び、根拠名は監査確認再正答です。 D: 監査確認再不足は名称や説明だけに寄り、判定名は監査確認再不足です。監査確認再資料では BUILDSA の使い方を出典欄から追跡し、資料名は監査確認再資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 範囲追跡のストレージ管理でストレージ管理の運用確認を行います。BUILDSA の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で範囲追跡のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず範囲追跡のストレージ管理を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. BUILDSA の属性行を読まず範囲追跡のストレージ管理の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲追跡のストレージ管理において選択記号 C を採用し、識別名は範囲追跡です。範囲追跡のストレージ管理において BUILDSA は説明欄の「DFSMS で BUILDSA の扱いを記録する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は範囲追跡です。範囲追跡のストレージ管理を受け取る担当者は、BUILDSA の表示結果と IDC0001I を同じ確認単位として扱い、背景名は範囲追跡です。不適切な選択肢を整理します。 A: 範囲追跡のストレージ管理は別カテゴリの確認を流用しており、BUILDSA の根拠にならないため範囲追跡ではありません。 B: 範囲追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため範囲追跡ではありません。 C: 範囲追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので範囲追跡です。 D: 範囲追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲追跡ではありません。範囲追跡のストレージ管理が示す BUILDSA は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>BUILDSA</strong></p><p>検証目的: 比較判定のストレージ管理について、BUILDSA は、DFSMS / IDCAMS / VSAM の DSS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020094の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、比較判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にBUILDSAを指定し、OSKB020094の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND BUILDSA
CASE OSKB020094
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM BUILDSA
CASE OSKB020094
SOURCE DFSMS
BUILDSAとOSKB020094が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020094を同じ出力で読み、比較判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020094
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020094.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020094が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の BUILDSA と OSKB020094 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020094 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0112"><h3>COMPRESS</h3><p class="kb-meta">分類: DSS ・ 難易度: 上級</p><p>COMPRESSは、DFSMS / IDCAMS / VSAMのDSSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdss Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域確認再のストレージ管理に関する COMPRESS の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず値域確認再のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域確認再のストレージ管理の証跡として保存して根拠にする。</li><li>C. COMPRESS の変更点を出力本文から切り離して値域確認再のストレージ管理の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC0001I を読み、値域確認再の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域確認再正解では選択記号 D を採用し、正解名は値域確認再正解です。値域確認再根拠では COMPRESS は「COMPRESS の状態と出力メッセージを結び付ける値域確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は値域確認再根拠です。値域確認再保存では COMPRESS の出力行と IDC0001I を一緒に残し、保存名は値域確認再保存です。選択肢ごとの違いを示します。 A: 値域確認再欠落は戻り値や記録番号に寄り、欠落名は値域確認再欠落です。 B: 値域確認再流用は別カテゴリの確認であり、排除名は値域確認再流用です。 C: 値域確認再不足は名称や説明だけに寄り、判定名は値域確認再不足です。 D: 値域確認再正答は対象出力と項目説明を結び、根拠名は値域確認再正答です。値域確認再対象では COMPRESS を DFSMS の確認記録に残し、対象名は値域確認再対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力追跡のストレージ管理に関する COMPRESS の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL の結果を残さず出力追跡のストレージ管理の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力追跡のストレージ管理の証跡として保存して根拠にする。</li><li>C. COMPRESS の変更点を出力本文から切り離して出力追跡のストレージ管理の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力追跡のストレージ管理において選択記号 D を採用し、識別名は出力追跡です。出力追跡のストレージ管理において COMPRESS は説明欄の「COMPRESS の状態と出力メッセージを結び付ける項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は出力追跡です。出力追跡のストレージ管理に関する記録は、COMPRESS の出力行と IDC0001I を一緒に保存し、背景名は出力追跡です。選択肢ごとの違いを示します。 A: 出力追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため出力追跡ではありません。 B: 出力追跡のストレージ管理は別カテゴリの確認を流用しており、COMPRESS の根拠にならないため出力追跡ではありません。 C: 出力追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため出力追跡ではありません。 D: 出力追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので出力追跡です。出力追跡のストレージ管理で記録する COMPRESS は DFSMS の確認記録に残す対象名であり、用語名は出力追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>COMPRESS</strong></p><p>検証目的: 置換追跡のストレージ管理について、COMPRESS は、DFSMS / IDCAMS / VSAM の DSS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030044の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、置換追跡のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCOMPRESSを指定し、OSKB030044の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND COMPRESS
CASE OSKB030044
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM COMPRESS
CASE OSKB030044
SOURCE DFSMS
COMPRESSとOSKB030044が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030044を同じ出力で読み、置換追跡のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030044
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030044.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030044が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の COMPRESS と OSKB030044 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030044 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div><div class="kb-p"><p class="kb-pname"><strong>COMPRESS</strong></p><p>検証目的: 範囲判定のストレージ管理について、COMPRESS は、DFSMS / IDCAMS / VSAM の DSS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020091の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、範囲判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCOMPRESSを指定し、OSKB020091の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND COMPRESS
CASE OSKB020091
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM COMPRESS
CASE OSKB020091
SOURCE DFSMS
COMPRESSとOSKB020091が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020091を同じ出力で読み、範囲判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020091
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020091.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020091が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の COMPRESS と OSKB020091 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020091 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0113"><h3>CONVERTV</h3><p class="kb-meta">分類: DSS ・ 難易度: 上級</p><p>CONVERTVは、DFSMS / IDCAMS / VSAMのDSSで機能名、見出し、または確認対象として参照する項目です。ボリュームを SMS 管理化/非管理化に変換。データセットを動かさず属性のみ切替。「CONVERTV」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdss Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告確認再のストレージ管理に関係する CONVERTV の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、警告確認再の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. CONVERTV の名称と担当者名だけを残して警告確認再のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で警告確認再のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず警告確認再のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告確認再正解では選択記号 A を採用し、正解名は警告確認再正解です。警告確認再根拠では CONVERTV は「CONVERTV の用途をストレージ管理の表示で確認する警告確認再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は警告確認再根拠です。警告確認再背景では DFSMS の CONVERTV と IDC3009I を同じ証跡に残し、背景名は警告確認再背景です。他の選択肢を確認します。 A: 警告確認再正答は対象出力と項目説明を結び、根拠名は警告確認再正答です。 B: 警告確認再不足は名称や説明だけに寄り、判定名は警告確認再不足です。 C: 警告確認再流用は別カテゴリの確認であり、排除名は警告確認再流用です。 D: 警告確認再欠落は戻り値や記録番号に寄り、欠落名は警告確認再欠落です。警告確認再用語では CONVERTV を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告確認再用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 条件追跡のストレージ管理に関係する CONVERTV の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、条件追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. CONVERTV の名称と担当者名のみを残して条件追跡のストレージ管理の表示本文を確認対象に含めない。</li><li>C. ストレージ管理以外の画面で条件追跡のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず条件追跡のストレージ管理の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件追跡のストレージ管理において選択記号 A を採用し、識別名は条件追跡です。条件追跡のストレージ管理において CONVERTV は説明欄の「CONVERTV の用途をストレージ管理の表示で確認する項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は条件追跡です。条件追跡のストレージ管理に関連して、DFSMS では CONVERTV の表示属性と IDC3009I を同じ証跡に残し、背景名は条件追跡です。他の選択肢を確認します。 A: 条件追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので条件追跡です。 B: 条件追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため条件追跡ではありません。 C: 条件追跡のストレージ管理は別カテゴリの確認を流用しており、CONVERTV の根拠にならないため条件追跡ではありません。 D: 条件追跡のストレージ管理は戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため条件追跡ではありません。条件追跡のストレージ管理で使う CONVERTV という用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は条件追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>CONVERTV</strong></p><p>検証目的: 優先判定のストレージ管理について、CONVERTV は、DFSMS / IDCAMS / VSAM の DSS で機能名、見出し、または確認対象として参照する項目です。ボリュームを SMS 管理化/非管理化に変換。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020092の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、優先判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCONVERTVを指定し、OSKB020092の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND CONVERTV
CASE OSKB020092
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM CONVERTV
CASE OSKB020092
SOURCE DFSMS
CONVERTVとOSKB020092が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020092を同じ出力で読み、優先判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020092
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020092.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020092が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の CONVERTV と OSKB020092 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020092 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0114"><h3>COPY</h3><p class="kb-meta">分類: DSS ・ 難易度: 上級</p><p>COPYは、DFSMS / IDCAMS / VSAMのDSSで機能名、見出し、または確認対象として参照する項目です。DUMP/RESTORE を経ずに直接コピー (FlashCopy/PPRC 連携時は瞬時)。VOLUME COPY や DS COPY 両形態</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdss Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較確認再のストレージ管理で COPY の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. COPY の出力を取らず比較確認再のストレージ管理の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、比較確認再の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して比較確認再のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較確認再のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較確認再正解では選択記号 B を採用し、正解名は比較確認再正解です。比較確認再根拠では COPY は「比較確認再のストレージ管理に関係する定義値と表示行を照合する比較確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は比較確認再根拠です。比較確認再追跡では COPY の属性行と IDC0001I を合わせ、追跡名は比較確認再追跡です。誤答側の問題点を分けます。 A: 比較確認再不足は名称や説明だけに寄り、判定名は比較確認再不足です。 B: 比較確認再正答は対象出力と項目説明を結び、根拠名は比較確認再正答です。 C: 比較確認再欠落は戻り値や記録番号に寄り、欠落名は比較確認再欠落です。 D: 比較確認再流用は別カテゴリの確認であり、排除名は比較確認再流用です。比較確認再初出では COPY を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較確認再初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索追跡のストレージ管理で COPY の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. COPY の出力を取らず探索追跡のストレージ管理の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を省略して探索追跡のストレージ管理の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索追跡のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索追跡のストレージ管理において選択記号 B を採用し、識別名は探索追跡です。探索追跡のストレージ管理において COPY は説明欄の「探索追跡のストレージ管理に関係する定義値と表示行を照合する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は探索追跡です。探索追跡のストレージ管理の証跡を読む担当者は、COPY の属性行と IDC0001I を合わせて追跡し、背景名は探索追跡です。誤答側の問題点を分けます。 A: 探索追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため探索追跡ではありません。 B: 探索追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので探索追跡です。 C: 探索追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため探索追跡ではありません。 D: 探索追跡のストレージ管理は別カテゴリの確認を流用しており、COPY の根拠にならないため探索追跡ではありません。探索追跡のストレージ管理に出る COPY は DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は探索追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>COPY</strong></p><p>検証目的: 条件判定のストレージ管理について、COPY は、DFSMS / IDCAMS / VSAM の DSS で機能名、見出し、または確認対象として参照する項目です。DUMP/RESTORE を経ずに直接コピー (Flaに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020089の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、条件判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCOPYを指定し、OSKB020089の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND COPY
CASE OSKB020089
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM COPY
CASE OSKB020089
SOURCE DFSMS
COPYとOSKB020089が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020089を同じ出力で読み、条件判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020089
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020089.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020089が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の COPY と OSKB020089 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020089 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0115"><h3>DFSMSdss 概要</h3><p class="kb-meta">分類: DSS ・ 難易度: 上級</p><p>ボリューム/データセット単位のバックアップ・コピー・移動・圧縮を行う DFSMS コンポーネント。FlashCopy 連携も担う</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdss Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲確認再の概要でストレージ管理の運用確認を行います。DFSMSdss 概要の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で範囲確認再の概要を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず範囲確認再の概要を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて範囲確認再の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. DFSMSdss 概要の属性行を読まず範囲確認再の概要の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲確認再正解では選択記号 C を採用し、正解名は範囲確認再正解です。範囲確認再根拠では DFSMSdss 概要 は「DFSMS で DFSMSdss 概要の扱いを記録する範囲確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は範囲確認再根拠です。範囲確認再受渡では DFSMSdss 概要の表示結果と IDC0001I を同じ確認単位にし、受渡名は範囲確認再受渡です。不適切な選択肢を整理します。 A: 範囲確認再流用は別カテゴリの確認であり、排除名は範囲確認再流用です。 B: 範囲確認再欠落は戻り値や記録番号に寄り、欠落名は範囲確認再欠落です。 C: 範囲確認再正答は対象出力と項目説明を結び、根拠名は範囲確認再正答です。 D: 範囲確認再不足は名称や説明だけに寄り、判定名は範囲確認再不足です。範囲確認再資料では DFSMSdss 概要の使い方を出典欄から追跡し、資料名は範囲確認再資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出追跡の概要でストレージ管理の運用確認を行います。DFSMSdss 概要の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で呼出追跡の概要を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず呼出追跡の概要を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. DFSMSdss 概要の属性行を読まず呼出追跡の概要の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出追跡の概要において選択記号 C を採用し、識別名は呼出追跡です。呼出追跡の概要において DFSMSdss 概要 は説明欄の「ボリューム/データセット単位のバックアップ・コピー・移動・圧縮を行う DFSMS コンポーネント。FlashCopy 連携も担う」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は呼出追跡です。呼出追跡の概要を受け取る担当者は、DFSMSdss 概要の表示結果と IDC0001I を同じ確認単位として扱い、背景名は呼出追跡です。不適切な選択肢を整理します。 A: 呼出追跡の概要は別カテゴリの確認を流用しており、DFSMSdss 概要の根拠にならないため呼出追跡ではありません。 B: 呼出追跡の概要は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため呼出追跡ではありません。 C: 呼出追跡の概要は対象出力と項目説明を結び、根拠を残すので呼出追跡です。 D: 呼出追跡の概要は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出追跡ではありません。呼出追跡の概要が示す DFSMSdss 概要は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSMSdss 概要</strong></p><p>検証目的: 呼出追跡の概要について、ボリューム/データセット単位のバックアップ・コピー・移動・圧縮を行う DFSMS コンポーネント。FlashCopy 連携も担うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030043の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、呼出追跡の概要の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDFSMSdss 概要を指定し、OSKB030043の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DFSMSdss 概要
CASE OSKB030043
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DFSMSdss 概要
CASE OSKB030043
SOURCE DFSMS
DFSMSdss 概要とOSKB030043が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030043を同じ出力で読み、呼出追跡の概要の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030043
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030043.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030043が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の DFSMSdss 概要 と OSKB030043 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030043 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div><div class="kb-p"><p class="kb-pname"><strong>DFSMSdss 概要</strong></p><p>検証目的: 探索判定の概要について、ボリューム/データセット単位のバックアップ・コピー・移動・圧縮を行う DFSMS コンポーネント。FlashCopy 連携も担うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020086の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、探索判定の概要の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDFSMSdss 概要を指定し、OSKB020086の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DFSMSdss 概要
CASE OSKB020086
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DFSMSdss 概要
CASE OSKB020086
SOURCE DFSMS
DFSMSdss 概要とOSKB020086が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020086を同じ出力で読み、探索判定の概要の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020086
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020086.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020086が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の DFSMSdss 概要 と OSKB020086 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020086 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0116"><h3>DUMP</h3><p class="kb-meta">分類: DSS ・ 難易度: 上級</p><p>DUMPは、DFSMS / IDCAMS / VSAMのDSSで機能名、見出し、または確認対象として参照する項目です。データセットまたはフルボリュームのバックアップを取得 (テープ/DASD 出力)。HSM 自動 DUMP の実体でもある</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdss Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先確認再のストレージ管理に関する DUMP の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず優先確認再のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先確認再のストレージ管理の証跡として保存して根拠にする。</li><li>C. DUMP の変更点を出力本文から切り離して優先確認再のストレージ管理の承認欄だけ残す。</li><li>D. IDC0001I を含む表示を保存し、説明欄との差分を優先確認再で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先確認再正解では選択記号 D を採用し、正解名は優先確認再正解です。優先確認再根拠では DUMP は「DUMP の状態と出力メッセージを結び付ける優先確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は優先確認再根拠です。優先確認再保存では DUMP の出力行と IDC0001I を一緒に残し、保存名は優先確認再保存です。選択肢ごとの違いを示します。 A: 優先確認再欠落は戻り値や記録番号に寄り、欠落名は優先確認再欠落です。 B: 優先確認再流用は別カテゴリの確認であり、排除名は優先確認再流用です。 C: 優先確認再不足は名称や説明だけに寄り、判定名は優先確認再不足です。 D: 優先確認再正答は対象出力と項目説明を結び、根拠名は優先確認再正答です。優先確認再対象では DUMP を DFSMS の確認記録に残し、対象名は優先確認再対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 置換追跡のストレージ管理に関する DUMP の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL の結果を残さず置換追跡のストレージ管理の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを置換追跡のストレージ管理の証跡として保存して根拠にする。</li><li>C. DUMP の変更点を出力本文から切り離して置換追跡のストレージ管理の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、置換追跡の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換追跡のストレージ管理において選択記号 D を採用し、識別名は置換追跡です。置換追跡のストレージ管理において DUMP は説明欄の「DUMP の状態と出力メッセージを結び付ける項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は置換追跡です。置換追跡のストレージ管理に関する記録は、DUMP の出力行と IDC0001I を一緒に保存し、背景名は置換追跡です。選択肢ごとの違いを示します。 A: 置換追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため置換追跡ではありません。 B: 置換追跡のストレージ管理は別カテゴリの確認を流用しており、DUMP の根拠にならないため置換追跡ではありません。 C: 置換追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため置換追跡ではありません。 D: 置換追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので置換追跡です。置換追跡のストレージ管理で記録する DUMP は DFSMS の確認記録に残す対象名であり、用語名は置換追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DUMP</strong></p><p>検証目的: 上書判定のストレージ管理について、DUMP は、DFSMS / IDCAMS / VSAM の DSS で機能名、見出し、または確認対象として参照する項目です。データセットまたはフルボリュームのバックアップを取得に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020087の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、上書判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDUMPを指定し、OSKB020087の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DUMP
CASE OSKB020087
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DUMP
CASE OSKB020087
SOURCE DFSMS
DUMPとOSKB020087が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020087を同じ出力で読み、上書判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020087
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020087.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020087が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の DUMP と OSKB020087 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020087 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0117"><h3>PHYSINDD / LOGINDD</h3><p class="kb-meta">分類: DSS ・ 難易度: 上級</p><p>PHYSINDD / LOGINDDは、DFSMS / IDCAMS / VSAMのDSSで機能名、見出し、または確認対象として参照する項目です。DUMP/RESTORE で物理/論理処理のスコープ DD を指定。DASD/テープ位置の使い分け。「PHYSINDD / LOGINDD」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdss Storage Administration</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更確認再の・に関する PHYSINDD ・ LOGINDD の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず変更確認再の・の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更確認再の・の証跡として保存して根拠にする。</li><li>C. PHYSINDD ・ LOGINDD の変更点を出力本文から切り離して変更確認再の・の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、変更確認再の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更確認再正解では選択記号 D を採用し、正解名は変更確認再正解です。変更確認再根拠では PHYSINDD ・ LOGINDD は「PHYSINDD ・ LOGINDD の状態と出力メッセージを結び付ける変更確認再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は変更確認再根拠です。変更確認再保存では PHYSINDD ・ LOGINDD の出力行と IDC3009I を一緒に残し、保存名は変更確認再保存です。選択肢ごとの違いを示します。 A: 変更確認再欠落は戻り値や記録番号に寄り、欠落名は変更確認再欠落です。 B: 変更確認再流用は別カテゴリの確認であり、排除名は変更確認再流用です。 C: 変更確認再不足は名称や説明だけに寄り、判定名は変更確認再不足です。 D: 変更確認再正答は対象出力と項目説明を結び、根拠名は変更確認再正答です。変更確認再対象では PHYSINDD ・ LOGINDD を DFSMS の確認記録に残し、対象名は変更確認再対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PHYSINDD ・ LOGINDD</strong></p><p>検証目的: 順序判定の・について、PHYSINDD / LOGINDD は、DFSMS / IDCAMS / VSAM の DSS で機能名、見出し、または確認対象として参照する項目です。DUMP/RESTOREに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020095の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、順序判定の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にPHYSINDD ・ LOGINDDを指定し、OSKB020095の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND PHYSINDD ・ LOGINDD
CASE OSKB020095
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM PHYSINDD ・ LOGINDD
CASE OSKB020095
SOURCE DFSMS
PHYSINDD ・ LOGINDDとOSKB020095が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020095を同じ出力で読み、順序判定の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020095
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020095.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020095が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の PHYSINDD ・ LOGINDD と OSKB020095 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020095 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0118"><h3>PRINT (DSS)</h3><p class="kb-meta">分類: DSS ・ 難易度: 上級</p><p>PRINT (DSS)は、DFSMS / IDCAMS / VSAMのDSSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdss Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧確認再のストレージ管理で PRINT (DSS)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. PRINT (DSS)の出力を取らず復旧確認再のストレージ管理の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、復旧確認再として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)を省略して復旧確認再のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧確認再のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧確認再正解では選択記号 B を採用し、正解名は復旧確認再正解です。復旧確認再根拠では PRINT (DSS) は「復旧確認再のストレージ管理に関係する定義値と表示行を照合する復旧確認再項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は復旧確認再根拠です。復旧確認再追跡では PRINT (DSS)の属性行と IDC0005I を合わせ、追跡名は復旧確認再追跡です。誤答側の問題点を分けます。 A: 復旧確認再不足は名称や説明だけに寄り、判定名は復旧確認再不足です。 B: 復旧確認再正答は対象出力と項目説明を結び、根拠名は復旧確認再正答です。 C: 復旧確認再欠落は戻り値や記録番号に寄り、欠落名は復旧確認再欠落です。 D: 復旧確認再流用は別カテゴリの確認であり、排除名は復旧確認再流用です。復旧確認再初出では PRINT (DSS)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧確認再初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切追跡のストレージ管理で PRINT (DSS)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. PRINT (DSS)の出力を取らず区切追跡のストレージ管理の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を省略して区切追跡のストレージ管理の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切追跡のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切追跡のストレージ管理において選択記号 B を採用し、識別名は区切追跡です。区切追跡のストレージ管理において PRINT (DSS) は説明欄の「区切追跡のストレージ管理に関係する定義値と表示行を照合する項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合する対象で、答え名は区切追跡です。区切追跡のストレージ管理の証跡を読む担当者は、PRINT (DSS)の属性行と IDC0005I を合わせて追跡し、背景名は区切追跡です。誤答側の問題点を分けます。 A: 区切追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため区切追跡ではありません。 B: 区切追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので区切追跡です。 C: 区切追跡のストレージ管理は戻り値や記録番号に寄り、IDC0005I や属性表示を落とすため区切追跡ではありません。 D: 区切追跡のストレージ管理は別カテゴリの確認を流用しており、PRINT (DSS)の根拠にならないため区切追跡ではありません。区切追跡のストレージ管理に出る PRINT (DSS)は DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は区切追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>PRINT (DSS)</strong></p><p>検証目的: 記録判定のストレージ管理について、PRINT (DSS)は、DFSMS / IDCAMS / VSAM の DSS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020093の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、記録判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にPRINT (DSS)を指定し、OSKB020093の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND PRINT (DSS)
CASE OSKB020093
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM PRINT (DSS)
CASE OSKB020093
SOURCE DFSMS
PRINT (DSS)とOSKB020093が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB020093を同じ出力で読み、記録判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
CASE OSKB020093
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
CLUSTER ------- OSKB020093.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0005IとOSKB020093が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
② ステップ2 の PRINT (DSS) と OSKB020093 が画面・出力に表示されること
③ ステップ3 の IDC0005I と OSKB020093 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0119"><h3>RELEASE</h3><p class="kb-meta">分類: DSS ・ 難易度: 上級</p><p>RELEASEは、DFSMS / IDCAMS / VSAMのDSSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdss Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序確認再のストレージ管理でストレージ管理の運用確認を行います。RELEASE の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で順序確認再のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず順序確認再のストレージ管理を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて順序確認再の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. RELEASE の属性行を読まず順序確認再のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序確認再正解では選択記号 C を採用し、正解名は順序確認再正解です。順序確認再根拠では RELEASE は「DFSMS で RELEASE の扱いを記録する順序確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は順序確認再根拠です。順序確認再受渡では RELEASE の表示結果と IDC0001I を同じ確認単位にし、受渡名は順序確認再受渡です。不適切な選択肢を整理します。 A: 順序確認再流用は別カテゴリの確認であり、排除名は順序確認再流用です。 B: 順序確認再欠落は戻り値や記録番号に寄り、欠落名は順序確認再欠落です。 C: 順序確認再正答は対象出力と項目説明を結び、根拠名は順序確認再正答です。 D: 順序確認再不足は名称や説明だけに寄り、判定名は順序確認再不足です。順序確認再資料では RELEASE の使い方を出典欄から追跡し、資料名は順序確認再資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書追跡のストレージ管理でストレージ管理の運用確認を行います。RELEASE の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で上書追跡のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず上書追跡のストレージ管理を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書追跡の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. RELEASE の属性行を読まず上書追跡のストレージ管理の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書追跡のストレージ管理において選択記号 C を採用し、識別名は上書追跡です。上書追跡のストレージ管理において RELEASE は説明欄の「DFSMS で RELEASE の扱いを記録する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は上書追跡です。上書追跡のストレージ管理を受け取る担当者は、RELEASE の表示結果と IDC0001I を同じ確認単位として扱い、背景名は上書追跡です。不適切な選択肢を整理します。 A: 上書追跡のストレージ管理は別カテゴリの確認を流用しており、RELEASE の根拠にならないため上書追跡ではありません。 B: 上書追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため上書追跡ではありません。 C: 上書追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので上書追跡です。 D: 上書追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため上書追跡ではありません。上書追跡のストレージ管理が示す RELEASE は出典欄の資料で使い方を追跡できる項目であり、用語名は上書追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RELEASE</strong></p><p>検証目的: 区切判定のストレージ管理について、RELEASE は、DFSMS / IDCAMS / VSAM の DSS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020090の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、区切判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にRELEASEを指定し、OSKB020090の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND RELEASE
CASE OSKB020090
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM RELEASE
CASE OSKB020090
SOURCE DFSMS
RELEASEとOSKB020090が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020090を同じ出力で読み、区切判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020090
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020090.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020090が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の RELEASE と OSKB020090 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020090 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div></details></section>


<section class="kb-item" id="c06-i0120"><h3>RESTORE</h3><p class="kb-meta">分類: DSS ・ 難易度: 上級</p><p>RESTOREは、DFSMS / IDCAMS / VSAMのDSSで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMSdss Storage Administration</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録確認再のストレージ管理に関係する RESTORE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、記録確認再の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. RESTORE の名称と担当者名だけを残して記録確認再のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で記録確認再のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず記録確認再のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録確認再正解では選択記号 A を採用し、正解名は記録確認再正解です。記録確認再根拠では RESTORE は「RESTORE の用途をストレージ管理の表示で確認する記録確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は記録確認再根拠です。記録確認再背景では DFSMS の RESTORE と IDC0001I を同じ証跡に残し、背景名は記録確認再背景です。他の選択肢を確認します。 A: 記録確認再正答は対象出力と項目説明を結び、根拠名は記録確認再正答です。 B: 記録確認再不足は名称や説明だけに寄り、判定名は記録確認再不足です。 C: 記録確認再流用は別カテゴリの確認であり、排除名は記録確認再流用です。 D: 記録確認再欠落は戻り値や記録番号に寄り、欠落名は記録確認再欠落です。記録確認再用語では RESTORE を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録確認再用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 終端追跡のストレージ管理に関係する RESTORE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、終端追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. RESTORE の名称と担当者名のみを残して終端追跡のストレージ管理の表示本文を確認対象に含めない。</li><li>C. ストレージ管理以外の画面で終端追跡のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず終端追跡のストレージ管理の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端追跡のストレージ管理において選択記号 A を採用し、識別名は終端追跡です。終端追跡のストレージ管理において RESTORE は説明欄の「RESTORE の用途をストレージ管理の表示で確認する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は終端追跡です。終端追跡のストレージ管理に関連して、DFSMS では RESTORE の表示属性と IDC0001I を同じ証跡に残し、背景名は終端追跡です。他の選択肢を確認します。 A: 終端追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので終端追跡です。 B: 終端追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため終端追跡ではありません。 C: 終端追跡のストレージ管理は別カテゴリの確認を流用しており、RESTORE の根拠にならないため終端追跡ではありません。 D: 終端追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため終端追跡ではありません。終端追跡のストレージ管理で使う RESTORE という用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は終端追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RESTORE</strong></p><p>検証目的: 出力判定のストレージ管理について、RESTORE は、DFSMS / IDCAMS / VSAM の DSS で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020088の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、出力判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にRESTOREを指定し、OSKB020088の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND RESTORE
CASE OSKB020088
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM RESTORE
CASE OSKB020088
SOURCE DFSMS
RESTOREとOSKB020088が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020088を同じ出力で読み、出力判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020088
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020088.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020088が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の RESTORE と OSKB020088 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020088 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMSdss Storage Administration</p></div></details></section>


## EXAMINE


<section class="kb-item" id="c06-i0121"><h3>ERRORLIMIT(n)</h3><p class="kb-meta">分類: EXAMINE ・ 難易度: 上級</p><p>ERRORLIMIT(n)は、DFSMS / IDCAMS / VSAMのEXAMINEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序記録のストレージ管理でストレージ管理の運用確認を行います。ERRORLIMIT(n)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で順序記録のストレージ管理を確認した扱いにする。</li><li>B. IDC0005I の有無を確認せず順序記録のストレージ管理を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、順序記録の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. ERRORLIMIT(n)の属性行を読まず順序記録のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序記録正解では選択記号 C を採用し、正解名は順序記録正解です。順序記録根拠では ERRORLIMIT(n) は「DFSMS で ERRORLIMIT(n)の扱いを記録する順序記録項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は順序記録根拠です。順序記録受渡では ERRORLIMIT(n)の表示結果と IDC0005I を同じ確認単位にし、受渡名は順序記録受渡です。不適切な選択肢を整理します。 A: 順序記録流用は別カテゴリの確認であり、排除名は順序記録流用です。 B: 順序記録欠落は戻り値や記録番号に寄り、欠落名は順序記録欠落です。 C: 順序記録正答は対象出力と項目説明を結び、根拠名は順序記録正答です。 D: 順序記録不足は名称や説明だけに寄り、判定名は順序記録不足です。順序記録資料では ERRORLIMIT(n)の使い方を出典欄から追跡し、資料名は順序記録資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ERRORLIMIT(n)</strong></p><p>検証目的: 区切確認のストレージ管理について、ERRORLIMIT(n)は、DFSMS / IDCAMS / VSAM の EXAMINE で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020010の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、区切確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にERRORLIMIT(n)を指定し、OSKB020010の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ERRORLIMIT(n)
CASE OSKB020010
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ERRORLIMIT(n)
CASE OSKB020010
SOURCE DFSMS
ERRORLIMIT(n)とOSKB020010が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB020010を同じ出力で読み、区切確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
CASE OSKB020010
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
CLUSTER ------- OSKB020010.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0005IとOSKB020010が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
② ステップ2 の ERRORLIMIT(n) と OSKB020010 が画面・出力に表示されること
③ ステップ3 の IDC0005I と OSKB020010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0122"><h3>EXAMINE 基本</h3><p class="kb-meta">分類: EXAMINE ・ 難易度: 上級</p><p>EXAMINE 基本は、DFSMS / IDCAMS / VSAMのEXAMINEで機能名、見出し、または確認対象として参照する項目です。KSDS インデックス/データの構造整合性を検査。トラブル時に物理破損や論理不整合を診断する。「EXAMINE 基本」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録記録の基本に関係する EXAMINE 基本の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、記録記録の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. EXAMINE 基本の名称と担当者名だけを残して記録記録の基本の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で記録記録の基本を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず記録記録の基本の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録記録正解では選択記号 A を採用し、正解名は記録記録正解です。記録記録根拠では EXAMINE 基本 は「EXAMINE 基本の用途をストレージ管理の表示で確認する記録記録項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は記録記録根拠です。記録記録背景では DFSMS の EXAMINE 基本と IDC3009I を同じ証跡に残し、背景名は記録記録背景です。他の選択肢を確認します。 A: 記録記録正答は対象出力と項目説明を結び、根拠名は記録記録正答です。 B: 記録記録不足は名称や説明だけに寄り、判定名は記録記録不足です。 C: 記録記録流用は別カテゴリの確認であり、排除名は記録記録流用です。 D: 記録記録欠落は戻り値や記録番号に寄り、欠落名は記録記録欠落です。記録記録用語では EXAMINE 基本を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録記録用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EXAMINE 基本</strong></p><p>検証目的: 出力確認の基本について、EXAMINE 基本は、DFSMS / IDCAMS / VSAM の EXAMINE で機能名、見出し、または確認対象として参照する項目です。KSDS インデックス/データの構に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020008の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、出力確認の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にEXAMINE 基本を指定し、OSKB020008の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND EXAMINE 基本
CASE OSKB020008
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM EXAMINE 基本
CASE OSKB020008
SOURCE DFSMS
EXAMINE 基本とOSKB020008が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020008を同じ出力で読み、出力確認の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020008
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020008.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020008が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の EXAMINE 基本 と OSKB020008 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020008 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0123"><h3>INDEXTEST / DATATEST</h3><p class="kb-meta">分類: EXAMINE ・ 難易度: 上級</p><p>INDEXTEST / DATATESTは、DFSMS / IDCAMS / VSAMのEXAMINEで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較記録の・で INDEXTEST 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. INDEXTEST 属性の出力を取らず比較記録の・の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、比較記録として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. REPRO INDATASET(OSKBSRC) OUTDATASET(OSKBTGT)を省略して比較記録の・の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較記録の・へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較記録正解では選択記号 B を採用し、正解名は比較記録正解です。比較記録根拠では INDEXTEST 属性 は「比較記録の・に関係する定義値と表示行を照合する比較記録項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は比較記録根拠です。比較記録追跡では INDEXTEST 属性の属性行と IDC0005I を合わせ、追跡名は比較記録追跡です。誤答側の問題点を分けます。 A: 比較記録不足は名称や説明だけに寄り、判定名は比較記録不足です。 B: 比較記録正答は対象出力と項目説明を結び、根拠名は比較記録正答です。 C: 比較記録欠落は戻り値や記録番号に寄り、欠落名は比較記録欠落です。 D: 比較記録流用は別カテゴリの確認であり、排除名は比較記録流用です。比較記録初出では INDEXTEST 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較記録初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>INDEXTEST ・ DATATEST</strong></p><p>検証目的: 条件確認の・について、INDEXTEST / DATATEST は、DFSMS / IDCAMS / VSAM の EXAMINE で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020009の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、条件確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にINDEXTEST ・ DATATEを指定し、OSKB020009の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND INDEXTEST ・ DATATE
CASE OSKB020009
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM INDEXTEST ・ DATATE
CASE OSKB020009
SOURCE DFSMS
INDEXTEST ・ DATATEとOSKB020009が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB020009を同じ出力で読み、条件確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
CASE OSKB020009
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
CLUSTER ------- OSKB020009.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0005IとOSKB020009が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
② ステップ2 の INDEXTEST ・ DATATE と OSKB020009 が画面・出力に表示されること
③ ステップ3 の IDC0005I と OSKB020009 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## EXPORT


<section class="kb-item" id="c06-i0124"><h3>EXPORT 基本</h3><p class="kb-meta">分類: EXPORT ・ 難易度: 上級</p><p>VSAM クラスターやユーザカタログをポータブル形式でアンロード。バックアップ・他システム転送・カタログ移行に使う</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更記録の基本に関する EXPORT 基本の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず変更記録の基本の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更記録の基本の証跡として保存して根拠にする。</li><li>C. EXPORT 基本の変更点を出力本文から切り離して変更記録の基本の承認欄だけ残す。</li><li>D. IDC0001I を含む表示を保存し、説明欄との差分を変更記録で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更記録正解では選択記号 D を採用し、正解名は変更記録正解です。変更記録根拠では EXPORT 基本 は「EXPORT 基本の状態と出力メッセージを結び付ける変更記録項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は変更記録根拠です。変更記録保存では EXPORT 基本の出力行と IDC0001I を一緒に残し、保存名は変更記録保存です。選択肢ごとの違いを示します。 A: 変更記録欠落は戻り値や記録番号に寄り、欠落名は変更記録欠落です。 B: 変更記録流用は別カテゴリの確認であり、排除名は変更記録流用です。 C: 変更記録不足は名称や説明だけに寄り、判定名は変更記録不足です。 D: 変更記録正答は対象出力と項目説明を結び、根拠名は変更記録正答です。変更記録対象では EXPORT 基本を DFSMS の確認記録に残し、対象名は変更記録対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EXPORT 基本</strong></p><p>検証目的: 順序確認の基本について、VSAM クラスターやユーザカタログをポータブル形式でアンロード。バックアップ・他システム転送・カタログ移行に使うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020015の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、順序確認の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にEXPORT 基本を指定し、OSKB020015の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND EXPORT 基本
CASE OSKB020015
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM EXPORT 基本
CASE OSKB020015
SOURCE DFSMS
EXPORT 基本とOSKB020015が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020015を同じ出力で読み、順序確認の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020015
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020015.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020015が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の EXPORT 基本 と OSKB020015 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020015 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0125"><h3>INFILE / OUTFILE (EXPORT)</h3><p class="kb-meta">分類: EXPORT ・ 難易度: 上級</p><p>EXPORT 出力先 DD/データセット名。テープがよく使われるが DASD でも可。「INFILE / OUTFILE (EXPORT)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開分離の・で INFILE 属性の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. INFILE 属性の出力を取らず展開分離の・の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、展開分離の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して展開分離の・の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開分離の・へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開分離正解では選択記号 B を採用し、正解名は展開分離正解です。展開分離根拠では INFILE 属性 は「展開分離の・に関係する定義値と表示行を照合する展開分離項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は展開分離根拠です。展開分離追跡では INFILE 属性の属性行と IDC3009I を合わせ、追跡名は展開分離追跡です。誤答側の問題点を分けます。 A: 展開分離不足は名称や説明だけに寄り、判定名は展開分離不足です。 B: 展開分離正答は対象出力と項目説明を結び、根拠名は展開分離正答です。 C: 展開分離欠落は戻り値や記録番号に寄り、欠落名は展開分離欠落です。 D: 展開分離流用は別カテゴリの確認であり、排除名は展開分離流用です。展開分離初出では INFILE 属性を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開分離初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>INFILE ・ OUTFILE (EXPORT)</strong></p><p>検証目的: 警告確認の・について、EXPORT 出力先 DD/ データセット名。テープがよく使われるが DASD でも可。「INFILE / OUTFILE (EXPORT)」を読むと、DEFINE、ALTEに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020017の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、警告確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にINFILE ・ OUTFILE (を指定し、OSKB020017の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND INFILE ・ OUTFILE (
CASE OSKB020017
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM INFILE ・ OUTFILE (
CASE OSKB020017
SOURCE DFSMS
INFILE ・ OUTFILE (とOSKB020017が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020017を同じ出力で読み、警告確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020017
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020017.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020017が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の INFILE ・ OUTFILE ( と OSKB020017 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020017 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0126"><h3>TEMPORARY / PERMANENT</h3><p class="kb-meta">分類: EXPORT ・ 難易度: 上級</p><p>TEMPORARY / PERMANENTは、DFSMS / IDCAMS / VSAMのEXPORTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文分離の・に関係する TEMPORARY 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、構文分離の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. TEMPORARY 属性の名称と担当者名だけを残して構文分離の・の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で構文分離の・を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず構文分離の・の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文分離正解では選択記号 A を採用し、正解名は構文分離正解です。構文分離根拠では TEMPORARY 属性 は「TEMPORARY 属性の用途をストレージ管理の表示で確認する構文分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は構文分離根拠です。構文分離背景では DFSMS の TEMPORARY 属性と IDC0001I を同じ証跡に残し、背景名は構文分離背景です。他の選択肢を確認します。 A: 構文分離正答は対象出力と項目説明を結び、根拠名は構文分離正答です。 B: 構文分離不足は名称や説明だけに寄り、判定名は構文分離不足です。 C: 構文分離流用は別カテゴリの確認であり、排除名は構文分離流用です。 D: 構文分離欠落は戻り値や記録番号に寄り、欠落名は構文分離欠落です。構文分離用語では TEMPORARY 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文分離用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>TEMPORARY ・ PERMANENT</strong></p><p>検証目的: 条件照合の・について、TEMPORARY / PERMANENT は、DFSMS / IDCAMS / VSAM の EXPORT で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030029の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、条件照合の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にTEMPORARY ・ PERMANを指定し、OSKB030029の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND TEMPORARY ・ PERMAN
CASE OSKB030029
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM TEMPORARY ・ PERMAN
CASE OSKB030029
SOURCE DFSMS
TEMPORARY ・ PERMANとOSKB030029が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030029を同じ出力で読み、条件照合の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030029
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030029.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030029が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の TEMPORARY ・ PERMAN と OSKB030029 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030029 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>TEMPORARY ・ PERMANENT</strong></p><p>検証目的: 値域確認の・について、TEMPORARY / PERMANENT は、DFSMS / IDCAMS / VSAM の EXPORT で機能名、見出し、または確認対象として参照する項目です。関連する操作、に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020016の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、値域確認の・の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にTEMPORARY ・ PERMANを指定し、OSKB020016の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND TEMPORARY ・ PERMAN
CASE OSKB020016
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM TEMPORARY ・ PERMAN
CASE OSKB020016
SOURCE DFSMS
TEMPORARY ・ PERMANとOSKB020016が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020016を同じ出力で読み、値域確認の・の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020016
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020016.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020016が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の TEMPORARY ・ PERMAN と OSKB020016 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020016 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## EXPORTRA


<section class="kb-item" id="c06-i0127"><h3>EXPORTRA (リカバリ用)</h3><p class="kb-meta">分類: EXPORTRA ・ 難易度: 上級</p><p>VSAM カタログリカバリ用の特殊エクスポート。AMS リカバリエリア (RA) からカタログを救出する旧手段</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索分離のリカバリ用で EXPORTRA (リカバリ用)の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. EXPORTRA (リカバリ用)の出力を取らず探索分離のリカバリ用の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、探索分離として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して探索分離のリカバリ用の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索分離のリカバリ用へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索分離正解では選択記号 B を採用し、正解名は探索分離正解です。探索分離根拠では EXPORTRA (リカバリ用) は「探索分離のリカバリ用に関係する定義値と表示行を照合する探索分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は探索分離根拠です。探索分離追跡では EXPORTRA (リカバリ用)の属性行と IDC0001I を合わせ、追跡名は探索分離追跡です。誤答側の問題点を分けます。 A: 探索分離不足は名称や説明だけに寄り、判定名は探索分離不足です。 B: 探索分離正答は対象出力と項目説明を結び、根拠名は探索分離正答です。 C: 探索分離欠落は戻り値や記録番号に寄り、欠落名は探索分離欠落です。 D: 探索分離流用は別カテゴリの確認であり、排除名は探索分離流用です。探索分離初出では EXPORTRA (リカバリ用)を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索分離初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>EXPORTRA (リカバリ用)</strong></p><p>検証目的: 区切照合のリカバリ用について、VSAM カタログリカバリ用の特殊エクスポート。AMS リカバリエリア (RA) からカタログを救出する旧手段に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030030の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、区切照合のリカバリ用の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にEXPORTRA (リカバリ用)を指定し、OSKB030030の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND EXPORTRA (リカバリ用)
CASE OSKB030030
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM EXPORTRA (リカバリ用)
CASE OSKB030030
SOURCE DFSMS
EXPORTRA (リカバリ用)とOSKB030030が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030030を同じ出力で読み、区切照合のリカバリ用の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030030
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030030.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030030が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の EXPORTRA (リカバリ用) と OSKB030030 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>EXPORTRA (リカバリ用)</strong></p><p>検証目的: 構文照合のリカバリ用について、VSAM カタログリカバリ用の特殊エクスポート。AMS リカバリエリア (RA) からカタログを救出する旧手段に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020021の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、構文照合のリカバリ用の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にEXPORTRA (リカバリ用)を指定し、OSKB020021の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND EXPORTRA (リカバリ用)
CASE OSKB020021
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM EXPORTRA (リカバリ用)
CASE OSKB020021
SOURCE DFSMS
EXPORTRA (リカバリ用)とOSKB020021が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020021を同じ出力で読み、構文照合のリカバリ用の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020021
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020021.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020021が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の EXPORTRA (リカバリ用) と OSKB020021 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020021 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## HSM


<section class="kb-item" id="c06-i0128"><h3>Automatic Backup</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>Automatic Backupは、DFSMS / IDCAMS / VSAMのHSMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件確認再のストレージ管理に関係する Automatic Backupの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、条件確認再で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. Automatic Backupの名称と担当者名だけを残して条件確認再のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で条件確認再のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず条件確認再のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件確認再正解では選択記号 A を採用し、正解名は条件確認再正解です。条件確認再根拠では Automatic Backup は「Automatic Backupの用途をストレージ管理の表示で確認する条件確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は条件確認再根拠です。条件確認再背景では DFSMS の Automatic Backupと IDC0001I を同じ証跡に残し、背景名は条件確認再背景です。他の選択肢を確認します。 A: 条件確認再正答は対象出力と項目説明を結び、根拠名は条件確認再正答です。 B: 条件確認再不足は名称や説明だけに寄り、判定名は条件確認再不足です。 C: 条件確認再流用は別カテゴリの確認であり、排除名は条件確認再流用です。 D: 条件確認再欠落は戻り値や記録番号に寄り、欠落名は条件確認再欠落です。条件確認再用語では Automatic Backupを DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件確認再用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文追跡のストレージ管理に関係する Automatic Backupの設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文追跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. Automatic Backupの名称と担当者名のみを残して構文追跡のストレージ管理の表示本文を確認対象に含めない。</li><li>C. ストレージ管理以外の画面で構文追跡のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず構文追跡のストレージ管理の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文追跡のストレージ管理において選択記号 A を採用し、識別名は構文追跡です。構文追跡のストレージ管理において Automatic Backup は説明欄の「Automatic Backupの用途をストレージ管理の表示で確認する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は構文追跡です。構文追跡のストレージ管理に関連して、DFSMS では Automatic Backupの表示属性と IDC0001I を同じ証跡に残し、背景名は構文追跡です。他の選択肢を確認します。 A: 構文追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので構文追跡です。 B: 構文追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため構文追跡ではありません。 C: 構文追跡のストレージ管理は別カテゴリの確認を流用しており、Automatic Backupの根拠にならないため構文追跡ではありません。 D: 構文追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため構文追跡ではありません。構文追跡のストレージ管理で使う Automatic Backupという用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は構文追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Automatic Backup</strong></p><p>検証目的: 置換判定のストレージ管理について、Automatic Backupは、DFSMS / IDCAMS / VSAM の HSM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020084の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、置換判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にAutomatic Backupを指定し、OSKB020084の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND Automatic Backup
CASE OSKB020084
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM Automatic Backup
CASE OSKB020084
SOURCE DFSMS
Automatic BackupとOSKB020084が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020084を同じ出力で読み、置換判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020084
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020084.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020084が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の Automatic Backup と OSKB020084 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020084 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


<section class="kb-item" id="c06-i0129"><h3>Automatic Dump</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>Automatic Dumpは、DFSMS / IDCAMS / VSAMのHSMで機能名、見出し、または確認対象として参照する項目です。ボリューム単位の Full Volume Dump。Storage Group の Auto Dump で有効化、DUMP CLASS で出力先制御</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切確認再のストレージ管理で Automatic Dumpの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. Automatic Dumpの出力を取らず区切確認再のストレージ管理の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、区切確認再の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して区切確認再のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切確認再のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切確認再正解では選択記号 B を採用し、正解名は区切確認再正解です。区切確認再根拠では Automatic Dump は「区切確認再のストレージ管理に関係する定義値と表示行を照合する区切確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は区切確認再根拠です。区切確認再追跡では Automatic Dumpの属性行と IDC0001I を合わせ、追跡名は区切確認再追跡です。誤答側の問題点を分けます。 A: 区切確認再不足は名称や説明だけに寄り、判定名は区切確認再不足です。 B: 区切確認再正答は対象出力と項目説明を結び、根拠名は区切確認再正答です。 C: 区切確認再欠落は戻り値や記録番号に寄り、欠落名は区切確認再欠落です。 D: 区切確認再流用は別カテゴリの確認であり、排除名は区切確認再流用です。区切確認再初出では Automatic Dumpを DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切確認再初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開追跡のストレージ管理で Automatic Dumpの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. Automatic Dumpの出力を取らず展開追跡のストレージ管理の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開追跡の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を省略して展開追跡のストレージ管理の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開追跡のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開追跡のストレージ管理において選択記号 B を採用し、識別名は展開追跡です。展開追跡のストレージ管理において Automatic Dump は説明欄の「展開追跡のストレージ管理に関係する定義値と表示行を照合する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は展開追跡です。展開追跡のストレージ管理の証跡を読む担当者は、Automatic Dumpの属性行と IDC0001I を合わせて追跡し、背景名は展開追跡です。誤答側の問題点を分けます。 A: 展開追跡のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため展開追跡ではありません。 B: 展開追跡のストレージ管理は対象出力と項目説明を結び、根拠を残すので展開追跡です。 C: 展開追跡のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため展開追跡ではありません。 D: 展開追跡のストレージ管理は別カテゴリの確認を流用しており、Automatic Dumpの根拠にならないため展開追跡ではありません。展開追跡のストレージ管理に出る Automatic Dumpは DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は展開追跡です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Automatic Dump</strong></p><p>検証目的: 終端判定のストレージ管理について、Automatic Dumpは、DFSMS / IDCAMS / VSAM の HSM で機能名、見出し、または確認対象として参照する項目です。ボリューム単位の Full Volに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020085の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、終端判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にAutomatic Dumpを指定し、OSKB020085の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND Automatic Dump
CASE OSKB020085
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM Automatic Dump
CASE OSKB020085
SOURCE DFSMS
Automatic DumpとOSKB020085が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020085を同じ出力で読み、終端判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020085
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020085.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020085が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の Automatic Dump と OSKB020085 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020085 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


<section class="kb-item" id="c06-i0130"><h3>DFSMShsm 概要</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>DFSMShsm 概要は、DFSMS / IDCAMS / VSAMのHSMで確認する項目です。階層型ストレージ管理 (HSM) サブシステム。Primary から ML1 から ML2 のマイグレーション、自動バックアップ、ダンプを担う</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査検分の概要でストレージ管理の運用確認を行います。DFSMShsm 概要の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で監査検分の概要を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず監査検分の概要を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて監査検分の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. DFSMShsm 概要の属性行を読まず監査検分の概要の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査検分正解では選択記号 C を採用し、正解名は監査検分正解です。監査検分根拠では DFSMShsm 概要 は「DFSMS で DFSMShsm 概要の扱いを記録する監査検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は監査検分根拠です。監査検分受渡では DFSMShsm 概要の表示結果と IDC0001I を同じ確認単位にし、受渡名は監査検分受渡です。不適切な選択肢を整理します。 A: 監査検分流用は別カテゴリの確認であり、排除名は監査検分流用です。 B: 監査検分欠落は戻り値や記録番号に寄り、欠落名は監査検分欠落です。 C: 監査検分正答は対象出力と項目説明を結び、根拠名は監査検分正答です。 D: 監査検分不足は名称や説明だけに寄り、判定名は監査検分不足です。監査検分資料では DFSMShsm 概要の使い方を出典欄から追跡し、資料名は監査検分資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 範囲照合の概要でストレージ管理の運用確認を行います。DFSMShsm 概要の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で範囲照合の概要を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず範囲照合の概要を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、範囲照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. DFSMShsm 概要の属性行を読まず範囲照合の概要の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲照合の概要において選択記号 C を採用し、識別名は範囲照合です。範囲照合の概要において DFSMShsm 概要 は説明欄の「DFSMS で DFSMShsm 概要の扱いを記録する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は範囲照合です。範囲照合の概要を受け取る担当者は、DFSMShsm 概要の表示結果と IDC0001I を同じ確認単位として扱い、背景名は範囲照合です。不適切な選択肢を整理します。 A: 範囲照合の概要は別カテゴリの確認を流用しており、DFSMShsm 概要の根拠にならないため範囲照合ではありません。 B: 範囲照合の概要は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため範囲照合ではありません。 C: 範囲照合の概要は対象出力と項目説明を結び、根拠を残すので範囲照合です。 D: 範囲照合の概要は名称や説明のみに寄り、状態を示す出力本文が不足するため範囲照合ではありません。範囲照合の概要が示す DFSMShsm 概要は出典欄の資料で使い方を追跡できる項目であり、用語名は範囲照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>DFSMShsm 概要</strong></p><p>検証目的: 比較検査の概要について、DFSMShsm 概要は、DFSMS / IDCAMS / VSAM の HSM で確認する項目です。階層型ストレージ管理 (HSM) サブシステム。Primary から ML1に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020074の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、比較検査の概要の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にDFSMShsm 概要を指定し、OSKB020074の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND DFSMShsm 概要
CASE OSKB020074
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM DFSMShsm 概要
CASE OSKB020074
SOURCE DFSMS
DFSMShsm 概要とOSKB020074が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020074を同じ出力で読み、比較検査の概要の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020074
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020074.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020074が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の DFSMShsm 概要 と OSKB020074 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020074 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


<section class="kb-item" id="c06-i0131"><h3>HALTERDS</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>HALTERDSは、DFSMS / IDCAMS / VSAMのHSMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 探索確認再のストレージ管理で HALTERDS の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. HALTERDS の出力を取らず探索確認再のストレージ管理の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、探索確認再として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して探索確認再のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を探索確認再のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索確認再正解では選択記号 B を採用し、正解名は探索確認再正解です。探索確認再根拠では HALTERDS は「探索確認再のストレージ管理に関係する定義値と表示行を照合する探索確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は探索確認再根拠です。探索確認再追跡では HALTERDS の属性行と IDC0001I を合わせ、追跡名は探索確認再追跡です。誤答側の問題点を分けます。 A: 探索確認再不足は名称や説明だけに寄り、判定名は探索確認再不足です。 B: 探索確認再正答は対象出力と項目説明を結び、根拠名は探索確認再正答です。 C: 探索確認再欠落は戻り値や記録番号に寄り、欠落名は探索確認再欠落です。 D: 探索確認再流用は別カテゴリの確認であり、排除名は探索確認再流用です。探索確認再初出では HALTERDS を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は探索確認再初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 復旧照合のストレージ管理で HALTERDS の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. HALTERDS の出力を取らず復旧照合のストレージ管理の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、復旧照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を省略して復旧照合のストレージ管理の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を復旧照合のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧照合のストレージ管理において選択記号 B を採用し、識別名は復旧照合です。復旧照合のストレージ管理において HALTERDS は説明欄の「復旧照合のストレージ管理に関係する定義値と表示行を照合する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は復旧照合です。復旧照合のストレージ管理の証跡を読む担当者は、HALTERDS の属性行と IDC0001I を合わせて追跡し、背景名は復旧照合です。誤答側の問題点を分けます。 A: 復旧照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため復旧照合ではありません。 B: 復旧照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので復旧照合です。 C: 復旧照合のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため復旧照合ではありません。 D: 復旧照合のストレージ管理は別カテゴリの確認を流用しており、HALTERDS の根拠にならないため復旧照合ではありません。復旧照合のストレージ管理に出る HALTERDS は DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は復旧照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>HALTERDS</strong></p><p>検証目的: 展開追跡のストレージ管理について、HALTERDS は、DFSMS / IDCAMS / VSAM の HSM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030042の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、展開追跡のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にHALTERDSを指定し、OSKB030042の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND HALTERDS
CASE OSKB030042
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM HALTERDS
CASE OSKB030042
SOURCE DFSMS
HALTERDSとOSKB030042が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030042を同じ出力で読み、展開追跡のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030042
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030042.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030042が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の HALTERDS と OSKB030042 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030042 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div><div class="kb-p"><p class="kb-pname"><strong>HALTERDS</strong></p><p>検証目的: 構文判定のストレージ管理について、HALTERDS は、DFSMS / IDCAMS / VSAM の HSM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020081の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、構文判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にHALTERDSを指定し、OSKB020081の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND HALTERDS
CASE OSKB020081
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM HALTERDS
CASE OSKB020081
SOURCE DFSMS
HALTERDSとOSKB020081が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020081を同じ出力で読み、構文判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020081
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020081.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020081が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の HALTERDS と OSKB020081 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020081 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


<section class="kb-item" id="c06-i0132"><h3>HBACKDS</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>HBACKDSは、DFSMS / IDCAMS / VSAMのHSMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出確認再のストレージ管理でストレージ管理の運用確認を行います。HBACKDS の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で呼出確認再のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず呼出確認再のストレージ管理を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて呼出確認再の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. HBACKDS の属性行を読まず呼出確認再のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出確認再正解では選択記号 C を採用し、正解名は呼出確認再正解です。呼出確認再根拠では HBACKDS は「DFSMS で HBACKDS の扱いを記録する呼出確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は呼出確認再根拠です。呼出確認再受渡では HBACKDS の表示結果と IDC0001I を同じ確認単位にし、受渡名は呼出確認再受渡です。不適切な選択肢を整理します。 A: 呼出確認再流用は別カテゴリの確認であり、排除名は呼出確認再流用です。 B: 呼出確認再欠落は戻り値や記録番号に寄り、欠落名は呼出確認再欠落です。 C: 呼出確認再正答は対象出力と項目説明を結び、根拠名は呼出確認再正答です。 D: 呼出確認再不足は名称や説明だけに寄り、判定名は呼出確認再不足です。呼出確認再資料では HBACKDS の使い方を出典欄から追跡し、資料名は呼出確認再資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 順序照合のストレージ管理でストレージ管理の運用確認を行います。HBACKDS の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で順序照合のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず順序照合のストレージ管理を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、順序照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. HBACKDS の属性行を読まず順序照合のストレージ管理の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序照合のストレージ管理において選択記号 C を採用し、識別名は順序照合です。順序照合のストレージ管理において HBACKDS は説明欄の「DFSMS で HBACKDS の扱いを記録する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は順序照合です。順序照合のストレージ管理を受け取る担当者は、HBACKDS の表示結果と IDC0001I を同じ確認単位として扱い、背景名は順序照合です。不適切な選択肢を整理します。 A: 順序照合のストレージ管理は別カテゴリの確認を流用しており、HBACKDS の根拠にならないため順序照合ではありません。 B: 順序照合のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため順序照合ではありません。 C: 順序照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので順序照合です。 D: 順序照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため順序照合ではありません。順序照合のストレージ管理が示す HBACKDS は出典欄の資料で使い方を追跡できる項目であり、用語名は順序照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HBACKDS</strong></p><p>検証目的: 復旧検査のストレージ管理について、HBACKDS は、DFSMS / IDCAMS / VSAM の HSM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020078の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、復旧検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にHBACKDSを指定し、OSKB020078の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND HBACKDS
CASE OSKB020078
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM HBACKDS
CASE OSKB020078
SOURCE DFSMS
HBACKDSとOSKB020078が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020078を同じ出力で読み、復旧検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020078
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020078.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020078が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の HBACKDS と OSKB020078 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020078 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


<section class="kb-item" id="c06-i0133"><h3>HDELETE</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>HDELETEは、DFSMS / IDCAMS / VSAMのHSMで機能名、見出し、または確認対象として参照する項目です。マイグレート/バックアップカタログ上のデータセット情報を削除。物理データセット削除と整合させる。「HDELETE」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端確認再のストレージ管理に関係する HDELETE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、終端確認再の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. HDELETE の名称と担当者名だけを残して終端確認再のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で終端確認再のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず終端確認再のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端確認再正解では選択記号 A を採用し、正解名は終端確認再正解です。終端確認再根拠では HDELETE は「HDELETE の用途をストレージ管理の表示で確認する終端確認再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は終端確認再根拠です。終端確認再背景では DFSMS の HDELETE と IDC3009I を同じ証跡に残し、背景名は終端確認再背景です。他の選択肢を確認します。 A: 終端確認再正答は対象出力と項目説明を結び、根拠名は終端確認再正答です。 B: 終端確認再不足は名称や説明だけに寄り、判定名は終端確認再不足です。 C: 終端確認再流用は別カテゴリの確認であり、排除名は終端確認再流用です。 D: 終端確認再欠落は戻り値や記録番号に寄り、欠落名は終端確認再欠落です。終端確認再用語では HDELETE を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端確認再用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 警告照合のストレージ管理に関係する HDELETE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、警告照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. HDELETE の名称と担当者名のみを残して警告照合のストレージ管理の表示本文を確認対象に含めない。</li><li>C. ストレージ管理以外の画面で警告照合のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず警告照合のストレージ管理の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告照合のストレージ管理において選択記号 A を採用し、識別名は警告照合です。警告照合のストレージ管理において HDELETE は説明欄の「HDELETE の用途をストレージ管理の表示で確認する項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は警告照合です。警告照合のストレージ管理に関連して、DFSMS では HDELETE の表示属性と IDC3009I を同じ証跡に残し、背景名は警告照合です。他の選択肢を確認します。 A: 警告照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので警告照合です。 B: 警告照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため警告照合ではありません。 C: 警告照合のストレージ管理は別カテゴリの確認を流用しており、HDELETE の根拠にならないため警告照合ではありません。 D: 警告照合のストレージ管理は戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため警告照合ではありません。警告照合のストレージ管理で使う HDELETE という用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は警告照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HDELETE</strong></p><p>検証目的: 変更検査のストレージ管理について、HDELETE は、DFSMS / IDCAMS / VSAM の HSM で機能名、見出し、または確認対象として参照する項目です。マイグレート/バックアップカタログ上のデータセッに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020080の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、変更検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にHDELETEを指定し、OSKB020080の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND HDELETE
CASE OSKB020080
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM HDELETE
CASE OSKB020080
SOURCE DFSMS
HDELETEとOSKB020080が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020080を同じ出力で読み、変更検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020080
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020080.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020080が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の HDELETE と OSKB020080 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020080 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


<section class="kb-item" id="c06-i0134"><h3>HMIGRATE</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>HMIGRATEは、DFSMS / IDCAMS / VSAMのHSMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 構文確認再のストレージ管理に関係する HMIGRATE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、構文確認再の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. HMIGRATE の名称と担当者名だけを残して構文確認再のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で構文確認再のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず構文確認再のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文確認再正解では選択記号 A を採用し、正解名は構文確認再正解です。構文確認再根拠では HMIGRATE は「HMIGRATE の用途をストレージ管理の表示で確認する構文確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は構文確認再根拠です。構文確認再背景では DFSMS の HMIGRATE と IDC0001I を同じ証跡に残し、背景名は構文確認再背景です。他の選択肢を確認します。 A: 構文確認再正答は対象出力と項目説明を結び、根拠名は構文確認再正答です。 B: 構文確認再不足は名称や説明だけに寄り、判定名は構文確認再不足です。 C: 構文確認再流用は別カテゴリの確認であり、排除名は構文確認再流用です。 D: 構文確認再欠落は戻り値や記録番号に寄り、欠落名は構文確認再欠落です。構文確認再用語では HMIGRATE を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は構文確認再用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 記録照合のストレージ管理に関係する HMIGRATE の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、記録照合として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. HMIGRATE の名称と担当者名のみを残して記録照合のストレージ管理の表示本文を確認対象に含めない。</li><li>C. ストレージ管理以外の画面で記録照合のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず記録照合のストレージ管理の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録照合のストレージ管理において選択記号 A を採用し、識別名は記録照合です。記録照合のストレージ管理において HMIGRATE は説明欄の「HMIGRATE の用途をストレージ管理の表示で確認する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は記録照合です。記録照合のストレージ管理に関連して、DFSMS では HMIGRATE の表示属性と IDC0001I を同じ証跡に残し、背景名は記録照合です。他の選択肢を確認します。 A: 記録照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので記録照合です。 B: 記録照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため記録照合ではありません。 C: 記録照合のストレージ管理は別カテゴリの確認を流用しており、HMIGRATE の根拠にならないため記録照合ではありません。 D: 記録照合のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため記録照合ではありません。記録照合のストレージ管理で使う HMIGRATE という用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は記録照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>HMIGRATE</strong></p><p>検証目的: 構文追跡のストレージ管理について、HMIGRATE は、DFSMS / IDCAMS / VSAM の HSM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030041の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、構文追跡のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にHMIGRATEを指定し、OSKB030041の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND HMIGRATE
CASE OSKB030041
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM HMIGRATE
CASE OSKB030041
SOURCE DFSMS
HMIGRATEとOSKB030041が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030041を同じ出力で読み、構文追跡のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030041
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030041.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030041が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の HMIGRATE と OSKB030041 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030041 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div><div class="kb-p"><p class="kb-pname"><strong>HMIGRATE</strong></p><p>検証目的: 値域検査のストレージ管理について、HMIGRATE は、DFSMS / IDCAMS / VSAM の HSM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020076の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、値域検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にHMIGRATEを指定し、OSKB020076の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND HMIGRATE
CASE OSKB020076
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM HMIGRATE
CASE OSKB020076
SOURCE DFSMS
HMIGRATEとOSKB020076が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020076を同じ出力で読み、値域検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020076
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020076.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020076が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の HMIGRATE と OSKB020076 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020076 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


<section class="kb-item" id="c06-i0135"><h3>HQUERY</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>HQUERYは、DFSMS / IDCAMS / VSAMのHSMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書確認再のストレージ管理でストレージ管理の運用確認を行います。HQUERY の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で上書確認再のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず上書確認再のストレージ管理を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書確認再の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. HQUERY の属性行を読まず上書確認再のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書確認再正解では選択記号 C を採用し、正解名は上書確認再正解です。上書確認再根拠では HQUERY は「DFSMS で HQUERY の扱いを記録する上書確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は上書確認再根拠です。上書確認再受渡では HQUERY の表示結果と IDC0001I を同じ確認単位にし、受渡名は上書確認再受渡です。不適切な選択肢を整理します。 A: 上書確認再流用は別カテゴリの確認であり、排除名は上書確認再流用です。 B: 上書確認再欠落は戻り値や記録番号に寄り、欠落名は上書確認再欠落です。 C: 上書確認再正答は対象出力と項目説明を結び、根拠名は上書確認再正答です。 D: 上書確認再不足は名称や説明だけに寄り、判定名は上書確認再不足です。上書確認再資料では HQUERY の使い方を出典欄から追跡し、資料名は上書確認再資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 監査照合のストレージ管理でストレージ管理の運用確認を行います。HQUERY の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で監査照合のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず監査照合のストレージ管理を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、監査照合の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. HQUERY の属性行を読まず監査照合のストレージ管理の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査照合のストレージ管理において選択記号 C を採用し、識別名は監査照合です。監査照合のストレージ管理において HQUERY は説明欄の「DFSMS で HQUERY の扱いを記録する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は監査照合です。監査照合のストレージ管理を受け取る担当者は、HQUERY の表示結果と IDC0001I を同じ確認単位として扱い、背景名は監査照合です。不適切な選択肢を整理します。 A: 監査照合のストレージ管理は別カテゴリの確認を流用しており、HQUERY の根拠にならないため監査照合ではありません。 B: 監査照合のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため監査照合ではありません。 C: 監査照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので監査照合です。 D: 監査照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため監査照合ではありません。監査照合のストレージ管理が示す HQUERY は出典欄の資料で使い方を追跡できる項目であり、用語名は監査照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HQUERY</strong></p><p>検証目的: 展開判定のストレージ管理について、HQUERY は、DFSMS / IDCAMS / VSAM の HSM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020082の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、展開判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にHQUERYを指定し、OSKB020082の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND HQUERY
CASE OSKB020082
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM HQUERY
CASE OSKB020082
SOURCE DFSMS
HQUERYとOSKB020082が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020082を同じ出力で読み、展開判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020082
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020082.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020082が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の HQUERY と OSKB020082 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020082 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


<section class="kb-item" id="c06-i0136"><h3>HRECALL</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>マイグレート済データセットを Primary に呼び戻し。透過リコールも HSM が自動実行する。「HRECALL」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 展開確認再のストレージ管理で HRECALL の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. HRECALL の出力を取らず展開確認再のストレージ管理の説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、展開確認再の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKBVSAMCASE))を省略して展開確認再のストレージ管理の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を展開確認再のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開確認再正解では選択記号 B を採用し、正解名は展開確認再正解です。展開確認再根拠では HRECALL は「展開確認再のストレージ管理に関係する定義値と表示行を照合する展開確認再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は展開確認再根拠です。展開確認再追跡では HRECALL の属性行と IDC3009I を合わせ、追跡名は展開確認再追跡です。誤答側の問題点を分けます。 A: 展開確認再不足は名称や説明だけに寄り、判定名は展開確認再不足です。 B: 展開確認再正答は対象出力と項目説明を結び、根拠名は展開確認再正答です。 C: 展開確認再欠落は戻り値や記録番号に寄り、欠落名は展開確認再欠落です。 D: 展開確認再流用は別カテゴリの確認であり、排除名は展開確認再流用です。展開確認再初出では HRECALL を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は展開確認再初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 比較照合のストレージ管理で HRECALL の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. HRECALL の出力を取らず比較照合のストレージ管理の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、比較照合の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を省略して比較照合のストレージ管理の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を比較照合のストレージ管理へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較照合のストレージ管理において選択記号 B を採用し、識別名は比較照合です。比較照合のストレージ管理において HRECALL は説明欄の「比較照合のストレージ管理に関係する定義値と表示行を照合する項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合する対象で、答え名は比較照合です。比較照合のストレージ管理の証跡を読む担当者は、HRECALL の属性行と IDC3009I を合わせて追跡し、背景名は比較照合です。誤答側の問題点を分けます。 A: 比較照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため比較照合ではありません。 B: 比較照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので比較照合です。 C: 比較照合のストレージ管理は戻り値や記録番号に寄り、IDC3009I や属性表示を落とすため比較照合ではありません。 D: 比較照合のストレージ管理は別カテゴリの確認を流用しており、HRECALL の根拠にならないため比較照合ではありません。比較照合のストレージ管理に出る HRECALL は DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は比較照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HRECALL</strong></p><p>検証目的: 警告検査のストレージ管理について、マイグレート済データセットを Primary に呼び戻し。透過リコールも HSM が自動実行する。「HRECALL」を読むと、DEFINE、ALTER、DELETE、LISに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020077の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、警告検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にHRECALLを指定し、OSKB020077の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND HRECALL
CASE OSKB020077
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM HRECALL
CASE OSKB020077
SOURCE DFSMS
HRECALLとOSKB020077が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020077を同じ出力で読み、警告検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020077
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020077.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020077が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の HRECALL と OSKB020077 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020077 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


<section class="kb-item" id="c06-i0137"><h3>HRECOVER</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>HRECOVERは、DFSMS / IDCAMS / VSAMのHSMで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換確認再のストレージ管理に関する HRECOVER の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず置換確認再のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換確認再のストレージ管理の証跡として保存して根拠にする。</li><li>C. HRECOVER の変更点を出力本文から切り離して置換確認再のストレージ管理の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC0001I を読み、置換確認再の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換確認再正解では選択記号 D を採用し、正解名は置換確認再正解です。置換確認再根拠では HRECOVER は「HRECOVER の状態と出力メッセージを結び付ける置換確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は置換確認再根拠です。置換確認再保存では HRECOVER の出力行と IDC0001I を一緒に残し、保存名は置換確認再保存です。選択肢ごとの違いを示します。 A: 置換確認再欠落は戻り値や記録番号に寄り、欠落名は置換確認再欠落です。 B: 置換確認再流用は別カテゴリの確認であり、排除名は置換確認再流用です。 C: 置換確認再不足は名称や説明だけに寄り、判定名は置換確認再不足です。 D: 置換確認再正答は対象出力と項目説明を結び、根拠名は置換確認再正答です。置換確認再対象では HRECOVER を DFSMS の確認記録に残し、対象名は置換確認再対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 値域照合のストレージ管理に関する HRECOVER の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL の結果を残さず値域照合のストレージ管理の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを値域照合のストレージ管理の証跡として保存して根拠にする。</li><li>C. HRECOVER の変更点を出力本文から切り離して値域照合のストレージ管理の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、値域照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域照合のストレージ管理において選択記号 D を採用し、識別名は値域照合です。値域照合のストレージ管理において HRECOVER は説明欄の「HRECOVER の状態と出力メッセージを結び付ける項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は値域照合です。値域照合のストレージ管理に関する記録は、HRECOVER の出力行と IDC0001I を一緒に保存し、背景名は値域照合です。選択肢ごとの違いを示します。 A: 値域照合のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため値域照合ではありません。 B: 値域照合のストレージ管理は別カテゴリの確認を流用しており、HRECOVER の根拠にならないため値域照合ではありません。 C: 値域照合のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため値域照合ではありません。 D: 値域照合のストレージ管理は対象出力と項目説明を結び、根拠を残すので値域照合です。値域照合のストレージ管理で記録する HRECOVER は DFSMS の確認記録に残す対象名であり、用語名は値域照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HRECOVER</strong></p><p>検証目的: 監査検査のストレージ管理について、HRECOVER は、DFSMS / IDCAMS / VSAM の HSM で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかをに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020079の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、監査検査のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にHRECOVERを指定し、OSKB020079の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND HRECOVER
CASE OSKB020079
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM HRECOVER
CASE OSKB020079
SOURCE DFSMS
HRECOVERとOSKB020079が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020079を同じ出力で読み、監査検査のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020079
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020079.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020079が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の HRECOVER と OSKB020079 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020079 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


<section class="kb-item" id="c06-i0138"><h3>HSEND コマンド</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>HSEND コマンドは、DFSMS / IDCAMS / VSAMのHSMで状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けて確認します。z を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 変更検分のコマンドに関する HSEND コマンドの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず変更検分のコマンドの担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを変更検分のコマンドの証跡として保存して根拠にする。</li><li>C. HSEND コマンドの変更点を出力本文から切り離して変更検分のコマンドの承認欄だけ残す。</li><li>D. IDC0001I を含む表示を保存し、説明欄との差分を変更検分で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 変更検分正解では選択記号 D を採用し、正解名は変更検分正解です。変更検分根拠では HSEND コマンド は「HSEND コマンドの状態と出力メッセージを結び付ける変更検分項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は変更検分根拠です。変更検分保存では HSEND コマンドの出力行と IDC0001I を一緒に残し、保存名は変更検分保存です。選択肢ごとの違いを示します。 A: 変更検分欠落は戻り値や記録番号に寄り、欠落名は変更検分欠落です。 B: 変更検分流用は別カテゴリの確認であり、排除名は変更検分流用です。 C: 変更検分不足は名称や説明だけに寄り、判定名は変更検分不足です。 D: 変更検分正答は対象出力と項目説明を結び、根拠名は変更検分正答です。変更検分対象では HSEND コマンドを DFSMS の確認記録に残し、対象名は変更検分対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 優先照合のコマンドに関する HSEND コマンドの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL の結果を残さず優先照合のコマンドの担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを優先照合のコマンドの証跡として保存して根拠にする。</li><li>C. HSEND コマンドの変更点を出力本文から切り離して優先照合のコマンドの承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、優先照合の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先照合のコマンドにおいて選択記号 D を採用し、識別名は優先照合です。優先照合のコマンドにおいて HSEND コマンド は説明欄の「HSEND コマンドの状態と出力メッセージを結び付ける項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は優先照合です。優先照合のコマンドに関する記録は、HSEND コマンドの出力行と IDC0001I を一緒に保存し、背景名は優先照合です。選択肢ごとの違いを示します。 A: 優先照合のコマンドは戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため優先照合ではありません。 B: 優先照合のコマンドは別カテゴリの確認を流用しており、HSEND コマンドの根拠にならないため優先照合ではありません。 C: 優先照合のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため優先照合ではありません。 D: 優先照合のコマンドは対象出力と項目説明を結び、根拠を残すので優先照合です。優先照合のコマンドで記録する HSEND コマンドは DFSMS の確認記録に残す対象名であり、用語名は優先照合です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>HSEND コマンド</strong></p><p>検証目的: 順序検査のコマンドについて、HSEND コマンドは、DFSMS / IDCAMS / VSAM の HSM で状態表示や操作を行うためのコマンド関連項目です。実行対象、必要権限、表示される状態の読み方を分けに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020075の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、順序検査のコマンドの確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にHSEND コマンドを指定し、OSKB020075の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND HSEND コマンド
CASE OSKB020075
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM HSEND コマンド
CASE OSKB020075
SOURCE DFSMS
HSEND コマンドとOSKB020075が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020075を同じ出力で読み、順序検査のコマンドの根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020075
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020075.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020075が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の HSEND コマンド と OSKB020075 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020075 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


<section class="kb-item" id="c06-i0139"><h3>Primary Space Management (PSM)</h3><p class="kb-meta">分類: HSM ・ 難易度: 上級</p><p>Migrate Threshold 超過時に HSM が自動的に古いデータをマイグレートするバックグラウンド処理</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 出力確認再のストレージ管理に関する Primary 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず出力確認再のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを出力確認再のストレージ管理の証跡として保存して根拠にする。</li><li>C. Primary 機能の変更点を出力本文から切り離して出力確認再のストレージ管理の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、出力確認再の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力確認再正解では選択記号 D を採用し、正解名は出力確認再正解です。出力確認再根拠では Primary 機能 は「Primary 機能の状態と出力メッセージを結び付ける出力確認再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は出力確認再根拠です。出力確認再保存では Primary 機能の出力行と IDC0001I を一緒に残し、保存名は出力確認再保存です。選択肢ごとの違いを示します。 A: 出力確認再欠落は戻り値や記録番号に寄り、欠落名は出力確認再欠落です。 B: 出力確認再流用は別カテゴリの確認であり、排除名は出力確認再流用です。 C: 出力確認再不足は名称や説明だけに寄り、判定名は出力確認再不足です。 D: 出力確認再正答は対象出力と項目説明を結び、根拠名は出力確認再正答です。出力確認再対象では Primary 機能を DFSMS の確認記録に残し、対象名は出力確認再対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Primary Space Management (PSM)</strong></p><p>検証目的: 呼出判定のストレージ管理について、Migrate Threshold 超過時に HSM が自動的に古いデータをマイグレートするバックグラウンド処理に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020083の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、呼出判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にPrimary Space Manaを指定し、OSKB020083の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND Primary Space Mana
CASE OSKB020083
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM Primary Space Mana
CASE OSKB020083
SOURCE DFSMS
Primary Space ManaとOSKB020083が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020083を同じ出力で読み、呼出判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020083
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020083.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020083が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の Primary Space Mana と OSKB020083 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020083 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMShsm Storage Administration / OS DFSMShsm Managing Your Own Data</p></div></details></section>


## ICF


<section class="kb-item" id="c06-i0140"><h3>BCS と VVDS の整合性</h3><p class="kb-meta">分類: ICF ・ 難易度: 上級</p><p>DIAGNOSE ICFCATALOG / DIAGNOSE VVDS で相互参照を検証。片側破損時は IDCAMS EXPORT/IMPORT または DELETE RECOVERY で修復</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 順序照合再のの整合性でストレージ管理の運用確認を行います。BCS と VVDS の整合性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で順序照合再のの整合性を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず順序照合再のの整合性を正常終了として記録する。</li><li>C. 参照資料名、表示行、メッセージをそろえて順序照合再の根拠を固定する。 <span class="kb-ok">✅ 正解</span></li><li>D. BCS と VVDS の整合性の属性行を読まず順序照合再のの整合性の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 順序照合再正解では選択記号 C を採用し、正解名は順序照合再正解です。順序照合再根拠では BCS と VVDS の整合性 は「DFSMS で BCS と VVDS の整合性の扱いを記録する順序照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は順序照合再根拠です。順序照合再受渡では BCS と VVDS の整合性の表示結果と IDC0001I を同じ確認単位にし、受渡名は順序照合再受渡です。不適切な選択肢を整理します。 A: 順序照合再流用は別カテゴリの確認であり、排除名は順序照合再流用です。 B: 順序照合再欠落は戻り値や記録番号に寄り、欠落名は順序照合再欠落です。 C: 順序照合再正答は対象出力と項目説明を結び、根拠名は順序照合再正答です。 D: 順序照合再不足は名称や説明だけに寄り、判定名は順序照合再不足です。順序照合再資料では BCS と VVDS の整合性の使い方を出典欄から追跡し、資料名は順序照合再資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 上書検査のと の整合性でストレージ管理の運用確認を行います。BCS と VVDS の整合性の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で上書検査のと の整合性を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず上書検査のと の整合性を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、上書検査の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. BCS と VVDS の整合性の属性行を読まず上書検査のと の整合性の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書検査のと の整合性において選択記号 C を採用し、識別名は上書検査です。上書検査のと の整合性において BCS と VVDS の整合性 は説明欄の「DFSMS で BCS と VVDS の整合性の扱いを記録する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は上書検査です。上書検査のと の整合性を受け取る担当者は、BCS と VVDS の整合性の表示結果と IDC0001I を同じ確認単位として扱い、背景名は上書検査です。不適切な選択肢を整理します。 A: 上書検査のと の整合性は別カテゴリの確認を流用しており、BCS と VVDS の整合性の根拠にならないため上書検査ではありません。 B: 上書検査のと の整合性は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため上書検査ではありません。 C: 上書検査のと の整合性は対象出力と項目説明を結び、根拠を残すので上書検査です。 D: 上書検査のと の整合性は名称や説明のみに寄り、状態を示す出力本文が不足するため上書検査ではありません。上書検査のと の整合性が示す BCS と VVDS の整合性は出典欄の資料で使い方を追跡できる項目であり、用語名は上書検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>BCS と VVDS の整合性</strong></p><p>検証目的: 区切整理のと の整合性について、DIAGNOSE ICFCATALOG / DIAGNOSE VVDS で相互参照を検証。片側破損時は IDCAMS EXPORT/IMPORT または DELETE REに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020110の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、区切整理のと の整合性の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にBCS と VVDS の整合性を指定し、OSKB020110の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND BCS と VVDS の整合性
CASE OSKB020110
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM BCS と VVDS の整合性
CASE OSKB020110
SOURCE DFSMS
BCS と VVDS の整合性とOSKB020110が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020110を同じ出力で読み、区切整理のと の整合性の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020110
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020110.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020110が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の BCS と VVDS の整合性 と OSKB020110 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020110 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0141"><h3>BCS の役割</h3><p class="kb-meta">分類: ICF ・ 難易度: 上級</p><p>DSN から 所在ボリューム・属性のメタ情報を保持。VSAM クラスターとして実装され、ALIAS/USERCATALOG/MASTERCATALOG 階層で構成される。DSN→所在ボリューム・属性のメタ情報を保持。VSAM クラスターとして実装され、ALIAS/USERCATALOG/MASTERCATALOG 階層で構成される</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 区切照合再の役割で BCS の役割の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. BCS の役割の出力を取らず区切照合再の役割の説明文と承認印だけを残す。</li><li>B. 資料上の説明と画面上の表示行を突き合わせ、区切照合再として引き継ぐ。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して区切照合再の役割の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を区切照合再の役割へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切照合再正解では選択記号 B を採用し、正解名は区切照合再正解です。区切照合再根拠では BCS の役割 は「区切照合再の役割に関係する定義値と表示行を照合する区切照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は区切照合再根拠です。区切照合再追跡では BCS の役割の属性行と IDC0001I を合わせ、追跡名は区切照合再追跡です。誤答側の問題点を分けます。 A: 区切照合再不足は名称や説明だけに寄り、判定名は区切照合再不足です。 B: 区切照合再正答は対象出力と項目説明を結び、根拠名は区切照合再正答です。 C: 区切照合再欠落は戻り値や記録番号に寄り、欠落名は区切照合再欠落です。 D: 区切照合再流用は別カテゴリの確認であり、排除名は区切照合再流用です。区切照合再初出では BCS の役割を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は区切照合再初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 展開検査のの役割で BCS の役割の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. BCS の役割の出力を取らず展開検査のの役割の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、展開検査の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を省略して展開検査のの役割の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を展開検査のの役割へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 展開検査のの役割において選択記号 B を採用し、識別名は展開検査です。展開検査のの役割において BCS の役割 は説明欄の「展開検査のの役割に関係する定義値と表示行を照合する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は展開検査です。展開検査のの役割の証跡を読む担当者は、BCS の役割の属性行と IDC0001I を合わせて追跡し、背景名は展開検査です。誤答側の問題点を分けます。 A: 展開検査のの役割は名称や説明のみに寄り、状態を示す出力本文が不足するため展開検査ではありません。 B: 展開検査のの役割は対象出力と項目説明を結び、根拠を残すので展開検査です。 C: 展開検査のの役割は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため展開検査ではありません。 D: 展開検査のの役割は別カテゴリの確認を流用しており、BCS の役割の根拠にならないため展開検査ではありません。展開検査のの役割に出る BCS の役割は DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は展開検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>BCS の役割</strong></p><p>検証目的: 終端整理のの役割について、DSN から 所在ボリューム・属性のメタ情報を保持。VSAM クラスターとして実装され、ALIAS/USERCATALOG/MASTERCATALOG 階層で構成される。Dに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020105の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、終端整理のの役割の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にBCS の役割を指定し、OSKB020105の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND BCS の役割
CASE OSKB020105
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM BCS の役割
CASE OSKB020105
SOURCE DFSMS
BCS の役割とOSKB020105が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020105を同じ出力で読み、終端整理のの役割の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020105
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020105.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020105が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の BCS の役割 と OSKB020105 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020105 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0142"><h3>Catalog Address Space (CAS)</h3><p class="kb-meta">分類: ICF ・ 難易度: 上級</p><p>Catalog Address Space (CAS)は、DFSMS / IDCAMS / VSAMのICFで確認する項目です。カタログサービスを担うシステムアドレス空間。MODIFY CATALOG コマンドで状態確認・再構成・性能解析を行う</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告照合再のストレージ管理に関係する Catalog 機能の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果から対象行を抜き出し、警告照合再の証跡として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. Catalog 機能の名称と担当者名だけを残して警告照合再のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で警告照合再のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず警告照合再のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告照合再正解では選択記号 A を採用し、正解名は警告照合再正解です。警告照合再根拠では Catalog 機能 は「Catalog 機能の用途をストレージ管理の表示で確認する警告照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は警告照合再根拠です。警告照合再背景では DFSMS の Catalog 機能と IDC0001I を同じ証跡に残し、背景名は警告照合再背景です。他の選択肢を確認します。 A: 警告照合再正答は対象出力と項目説明を結び、根拠名は警告照合再正答です。 B: 警告照合再不足は名称や説明だけに寄り、判定名は警告照合再不足です。 C: 警告照合再流用は別カテゴリの確認であり、排除名は警告照合再流用です。 D: 警告照合再欠落は戻り値や記録番号に寄り、欠落名は警告照合再欠落です。警告照合再用語では Catalog 機能を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告照合再用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Catalog Address Space (CAS)</strong></p><p>検証目的: 優先整理のストレージ管理について、Catalog Address Space (CAS)は、DFSMS / IDCAMS / VSAM の ICF で確認する項目です。カタログサービスを担うシステムアドレス空間。に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020112の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、優先整理のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCatalog Address Spを指定し、OSKB020112の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND Catalog Address Sp
CASE OSKB020112
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM Catalog Address Sp
CASE OSKB020112
SOURCE DFSMS
Catalog Address SpとOSKB020112が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020112を同じ出力で読み、優先整理のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020112
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020112.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020112が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の Catalog Address Sp と OSKB020112 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020112 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0143"><h3>Catalog Search Order</h3><p class="kb-meta">分類: ICF ・ 難易度: 上級</p><p>Catalog Search Orderは、DFSMS / IDCAMS / VSAMのICFで機能名、見出し、または確認対象として参照する項目です。DSN の HLQ から ALIAS から USERCATALOG の順で BCS が決定される。マスターカタログは最後の解決手段。DSN の HLQ → ALIAS → USERCATALOG の順で BCS が決定される。マスターカタログは最後の解決手段</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 値域照合再のストレージ管理に関する Catalog 機能の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず値域照合再のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを値域照合再のストレージ管理の証跡として保存して根拠にする。</li><li>C. Catalog 機能の変更点を出力本文から切り離して値域照合再のストレージ管理の承認欄だけ残す。</li><li>D. IDC0001I を含む表示を保存し、説明欄との差分を値域照合再で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 値域照合再正解では選択記号 D を採用し、正解名は値域照合再正解です。値域照合再根拠では Catalog 機能 は「Catalog 機能の状態と出力メッセージを結び付ける値域照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は値域照合再根拠です。値域照合再保存では Catalog 機能の出力行と IDC0001I を一緒に残し、保存名は値域照合再保存です。選択肢ごとの違いを示します。 A: 値域照合再欠落は戻り値や記録番号に寄り、欠落名は値域照合再欠落です。 B: 値域照合再流用は別カテゴリの確認であり、排除名は値域照合再流用です。 C: 値域照合再不足は名称や説明だけに寄り、判定名は値域照合再不足です。 D: 値域照合再正答は対象出力と項目説明を結び、根拠名は値域照合再正答です。値域照合再対象では Catalog 機能を DFSMS の確認記録に残し、対象名は値域照合再対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 出力検査のストレージ管理に関する Catalog Search Orderの引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL の結果を残さず出力検査のストレージ管理の担当者名と日時のみを記録する。</li><li>B. 別製品のメッセージを出力検査のストレージ管理の証跡として保存して根拠にする。</li><li>C. Catalog Search Orderの変更点を出力本文から切り離して出力検査のストレージ管理の承認欄のみ残す。</li><li>D. 属性行と出力見出しを合わせ、出力検査の証跡にする。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 出力検査のストレージ管理において選択記号 D を採用し、識別名は出力検査です。出力検査のストレージ管理において Catalog Search Order は説明欄の「Catalog Search Orderの状態と出力メッセージを結び付ける項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は出力検査です。出力検査のストレージ管理に関する記録は、Catalog Search Orderの出力行と IDC0001I を一緒に保存し、背景名は出力検査です。選択肢ごとの違いを示します。 A: 出力検査のストレージ管理は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため出力検査ではありません。 B: 出力検査のストレージ管理は別カテゴリの確認を流用しており、Catalog Search Orderの根拠にならないため出力検査ではありません。 C: 出力検査のストレージ管理は名称や説明のみに寄り、状態を示す出力本文が不足するため出力検査ではありません。 D: 出力検査のストレージ管理は対象出力と項目説明を結び、根拠を残すので出力検査です。出力検査のストレージ管理で記録する Catalog Search Orderは DFSMS の確認記録に残す対象名であり、用語名は出力検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>Catalog Search Order</strong></p><p>検証目的: 出力追跡のストレージ管理について、Catalog Search Orderは、DFSMS / IDCAMS / VSAM の ICF で機能名、見出し、または確認対象として参照する項目です。DSN の HLQ かに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030048の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、出力追跡のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCatalog Search Ordを指定し、OSKB030048の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND Catalog Search Ord
CASE OSKB030048
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM Catalog Search Ord
CASE OSKB030048
SOURCE DFSMS
Catalog Search OrdとOSKB030048が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030048を同じ出力で読み、出力追跡のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030048
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030048.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030048が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の Catalog Search Ord と OSKB030048 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030048 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>Catalog Search Order</strong></p><p>検証目的: 範囲整理のストレージ管理について、Catalog Search Orderは、DFSMS / IDCAMS / VSAM の ICF で機能名、見出し、または確認対象として参照する項目です。DSN の HLQ かに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020111の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、範囲整理のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にCatalog Search Ordを指定し、OSKB020111の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND Catalog Search Ord
CASE OSKB020111
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM Catalog Search Ord
CASE OSKB020111
SOURCE DFSMS
Catalog Search OrdとOSKB020111が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020111を同じ出力で読み、範囲整理のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020111
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020111.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020111が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の Catalog Search Ord と OSKB020111 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020111 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0144"><h3>ICF カタログ概要</h3><p class="kb-meta">分類: ICF ・ 難易度: 上級</p><p>Integrated Catalog Facility。BCS (Basic Catalog Structure, データセット名 から 属性/位置) と VVDS (VSAM Volume Data Set, 各ボリューム上の VSAM/SMS データセット情報) の 2 層構造。Integrated Catalog Facility。BCS (Basic Catalog Structure, データセット名→属性/位置) と VVDS (VSAM Volume Data Set, 各ボリューム上の VSAM/SMS データセット情報) の 2 層構造</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 条件照合再のカタログ概要に関係する ICF カタログ概要の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL で得た表示本文を使い、条件照合再の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. ICF カタログ概要の名称と担当者名だけを残して条件照合再のカタログ概要の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で条件照合再のカタログ概要を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず条件照合再のカタログ概要の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 条件照合再正解では選択記号 A を採用し、正解名は条件照合再正解です。条件照合再根拠では ICF カタログ概要 は「ICF カタログ概要の用途をストレージ管理の表示で確認する条件照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は条件照合再根拠です。条件照合再背景では DFSMS の ICF カタログ概要と IDC0001I を同じ証跡に残し、背景名は条件照合再背景です。他の選択肢を確認します。 A: 条件照合再正答は対象出力と項目説明を結び、根拠名は条件照合再正答です。 B: 条件照合再不足は名称や説明だけに寄り、判定名は条件照合再不足です。 C: 条件照合再流用は別カテゴリの確認であり、排除名は条件照合再流用です。 D: 条件照合再欠落は戻り値や記録番号に寄り、欠落名は条件照合再欠落です。条件照合再用語では ICF カタログ概要を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は条件照合再用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 構文検査のカタログ概要に関係する ICF カタログ概要の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 表示属性とメッセージを同じ証跡で読み、構文検査として残す。 <span class="kb-ok">✅ 正解</span></li><li>B. ICF カタログ概要の名称と担当者名のみを残して構文検査のカタログ概要の表示本文を確認対象に含めない。</li><li>C. ストレージ管理以外の画面で構文検査のカタログ概要を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず構文検査のカタログ概要の戻り値と時刻を主な根拠にして完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 構文検査のカタログ概要において選択記号 A を採用し、識別名は構文検査です。構文検査のカタログ概要において ICF カタログ概要 は説明欄の「ICF カタログ概要の用途をストレージ管理の表示で確認する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は構文検査です。構文検査のカタログ概要に関連して、DFSMS では ICF カタログ概要の表示属性と IDC0001I を同じ証跡に残し、背景名は構文検査です。他の選択肢を確認します。 A: 構文検査のカタログ概要は対象出力と項目説明を結び、根拠を残すので構文検査です。 B: 構文検査のカタログ概要は名称や説明のみに寄り、状態を示す出力本文が不足するため構文検査ではありません。 C: 構文検査のカタログ概要は別カテゴリの確認を流用しており、ICF カタログ概要の根拠にならないため構文検査ではありません。 D: 構文検査のカタログ概要は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため構文検査ではありません。構文検査のカタログ概要で使う ICF カタログ概要という用語は DFSMS / IDCAMS / VSAM で扱う確認対象であり、用語名は構文検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ICF カタログ概要</strong></p><p>検証目的: 置換整理のカタログ概要について、Integrated Catalog Facility。BCS (Basic Catalog Structure, データセット名 から 属性/位置) と VVDS (VSに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020104の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、置換整理のカタログ概要の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にICF カタログ概要を指定し、OSKB020104の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ICF カタログ概要
CASE OSKB020104
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ICF カタログ概要
CASE OSKB020104
SOURCE DFSMS
ICF カタログ概要とOSKB020104が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020104を同じ出力で読み、置換整理のカタログ概要の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020104
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020104.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020104が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ICF カタログ概要 と OSKB020104 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020104 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0145"><h3>MODIFY CATALOG コマンド</h3><p class="kb-meta">分類: ICF ・ 難易度: 上級</p><p>MODIFY CATALOG コマンドは、DFSMS / IDCAMS / VSAMのICFで状態表示や操作を行うためのコマンド関連項目です。F CATALOG,REPORT / F CATALOG,LIST / F CATALOG,ALLOCATED 等。カタログ性能やオープン状況の運用診断に使う</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 復旧照合再のコマンドで MODIFY CATALOG コマンドの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. MODIFY CATALOG コマンドの出力を取らず復旧照合再のコマンドの説明文と承認印だけを残す。</li><li>B. 出典欄の説明と運用出力を照合し、復旧照合再の確認記録にまとめる。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して復旧照合再のコマンドの記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を復旧照合再のコマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 復旧照合再正解では選択記号 B を採用し、正解名は復旧照合再正解です。復旧照合再根拠では MODIFY CATALOG コマンド は「復旧照合再のコマンドに関係する定義値と表示行を照合する復旧照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は復旧照合再根拠です。復旧照合再追跡では MODIFY CATALOG コマンドの属性行と IDC0001I を合わせ、追跡名は復旧照合再追跡です。誤答側の問題点を分けます。 A: 復旧照合再不足は名称や説明だけに寄り、判定名は復旧照合再不足です。 B: 復旧照合再正答は対象出力と項目説明を結び、根拠名は復旧照合再正答です。 C: 復旧照合再欠落は戻り値や記録番号に寄り、欠落名は復旧照合再欠落です。 D: 復旧照合再流用は別カテゴリの確認であり、排除名は復旧照合再流用です。復旧照合再初出では MODIFY CATALOG コマンドを DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は復旧照合再初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 区切検査のコマンドで MODIFY CATALOG コマンドの点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. MODIFY CATALOG コマンドの出力を取らず区切検査のコマンドの説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、区切検査の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を省略して区切検査のコマンドの記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を区切検査のコマンドへ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 区切検査のコマンドにおいて選択記号 B を採用し、識別名は区切検査です。区切検査のコマンドにおいて MODIFY CATALOG コマンド は説明欄の「区切検査のコマンドに関係する定義値と表示行を照合する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は区切検査です。区切検査のコマンドの証跡を読む担当者は、MODIFY CATALOG コマンドの属性行と IDC0001I を合わせて追跡し、背景名は区切検査です。誤答側の問題点を分けます。 A: 区切検査のコマンドは名称や説明のみに寄り、状態を示す出力本文が不足するため区切検査ではありません。 B: 区切検査のコマンドは対象出力と項目説明を結び、根拠を残すので区切検査です。 C: 区切検査のコマンドは戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため区切検査ではありません。 D: 区切検査のコマンドは別カテゴリの確認を流用しており、MODIFY CATALOG コマンドの根拠にならないため区切検査ではありません。区切検査のコマンドに出る MODIFY CATALOG コマンドは DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は区切検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>MODIFY CATALOG コマンド</strong></p><p>検証目的: 記録整理のコマンドについて、MODIFY CATALOG コマンドは、DFSMS / IDCAMS / VSAM の ICF で状態表示や操作を行うためのコマンド関連項目です。F CATALOG,REPORに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020113の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、記録整理のコマンドの確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にMODIFY CATALOG コマンを指定し、OSKB020113の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND MODIFY CATALOG コマン
CASE OSKB020113
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM MODIFY CATALOG コマン
CASE OSKB020113
SOURCE DFSMS
MODIFY CATALOG コマンとOSKB020113が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020113を同じ出力で読み、記録整理のコマンドの根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020113
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020113.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020113が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の MODIFY CATALOG コマン と OSKB020113 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020113 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0146"><h3>NVR (Non-VSAM Volume Record)</h3><p class="kb-meta">分類: ICF ・ 難易度: 上級</p><p>SMS 管理の非 VSAM データセットを VVDS に記録するレコード。SMS 属性 (DC/SC/MC) の VVDS 側コピー</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 記録照合再のストレージ管理に関係する NVR 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. 対象の出力行とメッセージ接頭辞を同時に記録し、記録照合再で再確認できる形にする。 <span class="kb-ok">✅ 正解</span></li><li>B. NVR 属性の名称と担当者名だけを残して記録照合再のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で記録照合再のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC0001I の有無を見ず記録照合再のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 記録照合再正解では選択記号 A を採用し、正解名は記録照合再正解です。記録照合再根拠では NVR 属性 は「NVR 属性の用途をストレージ管理の表示で確認する記録照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は記録照合再根拠です。記録照合再背景では DFSMS の NVR 属性と IDC0001I を同じ証跡に残し、背景名は記録照合再背景です。他の選択肢を確認します。 A: 記録照合再正答は対象出力と項目説明を結び、根拠名は記録照合再正答です。 B: 記録照合再不足は名称や説明だけに寄り、判定名は記録照合再不足です。 C: 記録照合再流用は別カテゴリの確認であり、排除名は記録照合再流用です。 D: 記録照合再欠落は戻り値や記録番号に寄り、欠落名は記録照合再欠落です。記録照合再用語では NVR 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は記録照合再用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>NVR (Non-VSAM Volume Record)</strong></p><p>検証目的: 出力整理のストレージ管理について、SMS 管理の非 VSAM データセットを VVDS に記録するレコード。SMS 属性 (DC/SC/MC) の VVDS 側コピーに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020108の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、出力整理のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にNVR (Non-VSAM Voluを指定し、OSKB020108の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND NVR (Non-VSAM Volu
CASE OSKB020108
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM NVR (Non-VSAM Volu
CASE OSKB020108
SOURCE DFSMS
NVR (Non-VSAM VoluとOSKB020108が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020108を同じ出力で読み、出力整理のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020108
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020108.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020108が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の NVR (Non-VSAM Volu と OSKB020108 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020108 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0147"><h3>VVDS の役割</h3><p class="kb-meta">分類: ICF ・ 難易度: 上級</p><p>各ボリュームに 1 つ存在し、そのボリューム上の VSAM データ (VVR) と SMS 管理データセット情報 (NVR) を保持する。BCS と二重に参照される</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 範囲照合再の役割でストレージ管理の運用確認を行います。VVDS の役割の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で範囲照合再の役割を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず範囲照合再の役割を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、範囲照合再の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. VVDS の役割の属性行を読まず範囲照合再の役割の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 範囲照合再正解では選択記号 C を採用し、正解名は範囲照合再正解です。範囲照合再根拠では VVDS の役割 は「DFSMS で VVDS の役割の扱いを記録する範囲照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は範囲照合再根拠です。範囲照合再受渡では VVDS の役割の表示結果と IDC0001I を同じ確認単位にし、受渡名は範囲照合再受渡です。不適切な選択肢を整理します。 A: 範囲照合再流用は別カテゴリの確認であり、排除名は範囲照合再流用です。 B: 範囲照合再欠落は戻り値や記録番号に寄り、欠落名は範囲照合再欠落です。 C: 範囲照合再正答は対象出力と項目説明を結び、根拠名は範囲照合再正答です。 D: 範囲照合再不足は名称や説明だけに寄り、判定名は範囲照合再不足です。範囲照合再資料では VVDS の役割の使い方を出典欄から追跡し、資料名は範囲照合再資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 呼出検査のの役割でストレージ管理の運用確認を行います。VVDS の役割の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で呼出検査のの役割を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず呼出検査のの役割を正常終了として記録する。</li><li>C. 説明欄と実出力を照合し、呼出検査の記録として扱う。 <span class="kb-ok">✅ 正解</span></li><li>D. VVDS の役割の属性行を読まず呼出検査のの役割の画面名と利用者名のみを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出検査のの役割において選択記号 C を採用し、識別名は呼出検査です。呼出検査のの役割において VVDS の役割 は説明欄の「各ボリュームに 1 つ存在し、そのボリューム上の VSAM データ (VVR) と SMS 管理データセット情報 (NVR) を保持する。B」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は呼出検査です。呼出検査のの役割を受け取る担当者は、VVDS の役割の表示結果と IDC0001I を同じ確認単位として扱い、背景名は呼出検査です。不適切な選択肢を整理します。 A: 呼出検査のの役割は別カテゴリの確認を流用しており、VVDS の役割の根拠にならないため呼出検査ではありません。 B: 呼出検査のの役割は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため呼出検査ではありません。 C: 呼出検査のの役割は対象出力と項目説明を結び、根拠を残すので呼出検査です。 D: 呼出検査のの役割は名称や説明のみに寄り、状態を示す出力本文が不足するため呼出検査ではありません。呼出検査のの役割が示す VVDS の役割は出典欄の資料で使い方を追跡できる項目であり、用語名は呼出検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（2件）</summary><div class="kb-p"><p class="kb-pname"><strong>VVDS の役割</strong></p><p>検証目的: 上書追跡の役割について、各ボリュームに 1 つ存在し、そのボリューム上の VSAM データ (VVR) と SMS 管理データセット情報 (NVR) を保持する。BCS と二重に参照されるに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB030047の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、上書追跡の役割の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にVVDS の役割を指定し、OSKB030047の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND VVDS の役割
CASE OSKB030047
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM VVDS の役割
CASE OSKB030047
SOURCE DFSMS
VVDS の役割とOSKB030047が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB030047を同じ出力で読み、上書追跡の役割の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB030047
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB030047.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB030047が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の VVDS の役割 と OSKB030047 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB030047 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div><div class="kb-p"><p class="kb-pname"><strong>VVDS の役割</strong></p><p>検証目的: 探索整理のの役割について、各ボリュームに 1 つ存在し、そのボリューム上の VSAM データ (VVR) と SMS 管理データセット情報 (NVR) を保持する。BCS と二重に参照されるに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020106の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、探索整理のの役割の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にVVDS の役割を指定し、OSKB020106の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND VVDS の役割
CASE OSKB020106
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM VVDS の役割
CASE OSKB020106
SOURCE DFSMS
VVDS の役割とOSKB020106が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020106を同じ出力で読み、探索整理のの役割の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020106
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020106.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020106が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の VVDS の役割 と OSKB020106 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020106 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0148"><h3>VVDS 名規則</h3><p class="kb-meta">分類: ICF ・ 難易度: 上級</p><p>VVDS 名規則は、DFSMS / IDCAMS / VSAMのICFで確認する項目です。SYS1.VVDS.Vvolser 形式。volser とボリューム上 VVDS 名が一致しないとカタログ整合性を維持できない</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（2問）</summary><div class="kb-q"><p><strong>問題.</strong> 比較照合再の名規則で VVDS 名規則の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. VVDS 名規則の出力を取らず比較照合再の名規則の説明文と承認印だけを残す。</li><li>B. 机上確認でも実出力の見出しに合わせ、比較照合再の確認値として扱う。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKBVSAMCASE) ALL を省略して比較照合再の名規則の記録番号と時刻だけを残す。</li><li>D. 隣接項目の結果を比較照合再の名規則へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 比較照合再正解では選択記号 B を採用し、正解名は比較照合再正解です。比較照合再根拠では VVDS 名規則 は「比較照合再の名規則に関係する定義値と表示行を照合する比較照合再項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は比較照合再根拠です。比較照合再追跡では VVDS 名規則の属性行と IDC0001I を合わせ、追跡名は比較照合再追跡です。誤答側の問題点を分けます。 A: 比較照合再不足は名称や説明だけに寄り、判定名は比較照合再不足です。 B: 比較照合再正答は対象出力と項目説明を結び、根拠名は比較照合再正答です。 C: 比較照合再欠落は戻り値や記録番号に寄り、欠落名は比較照合再欠落です。 D: 比較照合再流用は別カテゴリの確認であり、排除名は比較照合再流用です。比較照合再初出では VVDS 名規則を DFSMS / IDCAMS / VSAM の運用手順で確認し、初出名は比較照合再初出です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div><div class="kb-q"><p><strong>問題.</strong> 探索検査の名規則で VVDS 名規則の点検記録を作ります。証跡として扱える確認はどれですか。</p><ul class="kb-choices"><li>A. VVDS 名規則の出力を取らず探索検査の名規則の説明文と承認印のみを残す。</li><li>B. 運用画面の根拠行を保存し、探索検査の確認結果にする。 <span class="kb-ok">✅ 正解</span></li><li>C. LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を省略して探索検査の名規則の記録番号と時刻のみを残す。</li><li>D. 隣接項目の結果を探索検査の名規則へ転記して同じ結果として扱う。</li></ul><p class="kb-meta">正解: <strong>B</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 探索検査の名規則において選択記号 B を採用し、識別名は探索検査です。探索検査の名規則において VVDS 名規則 は説明欄の「探索検査の名規則に関係する定義値と表示行を照合する項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合する対象で、答え名は探索検査です。探索検査の名規則の証跡を読む担当者は、VVDS 名規則の属性行と IDC0001I を合わせて追跡し、背景名は探索検査です。誤答側の問題点を分けます。 A: 探索検査の名規則は名称や説明のみに寄り、状態を示す出力本文が不足するため探索検査ではありません。 B: 探索検査の名規則は対象出力と項目説明を結び、根拠を残すので探索検査です。 C: 探索検査の名規則は戻り値や記録番号に寄り、IDC0001I や属性表示を落とすため探索検査ではありません。 D: 探索検査の名規則は別カテゴリの確認を流用しており、VVDS 名規則の根拠にならないため探索検査ではありません。探索検査の名規則に出る VVDS 名規則は DFSMS / IDCAMS / VSAM の運用手順で意味を確認する対象であり、用語名は探索検査です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>VVDS 名規則</strong></p><p>検証目的: 条件整理の名規則について、VVDS 名規則は、DFSMS / IDCAMS / VSAM の ICF で確認する項目です。SYS1.VVDS.Vvolser 形式。volser とボリューム上 VVDSに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020109の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、条件整理の名規則の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にVVDS 名規則を指定し、OSKB020109の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND VVDS 名規則
CASE OSKB020109
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM VVDS 名規則
CASE OSKB020109
SOURCE DFSMS
VVDS 名規則とOSKB020109が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020109を同じ出力で読み、条件整理の名規則の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020109
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020109.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020109が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の VVDS 名規則 と OSKB020109 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020109 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0149"><h3>VVR (VSAM Volume Record)</h3><p class="kb-meta">分類: ICF ・ 難易度: 上級</p><p>VVR (VSAM Volume Record)は、DFSMS / IDCAMS / VSAMのICFで機能名、見出し、または確認対象として参照する項目です。VVDS 内の VSAM ボリュームレコード。CISZ, FREESPACE, HURBA, HARBA, 統計を保持する。「VVR (VSAM Volume Record)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 優先照合再のストレージ管理に関する VVR 属性の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))の結果を残さず優先照合再のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを優先照合再のストレージ管理の証跡として保存して根拠にする。</li><li>C. VVR 属性の変更点を出力本文から切り離して優先照合再のストレージ管理の承認欄だけ残す。</li><li>D. DFSMS の表示形式に沿って根拠行を採り、優先照合再の点検結果を残す。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 優先照合再正解では選択記号 D を採用し、正解名は優先照合再正解です。優先照合再根拠では VVR 属性 は「VVR 属性の状態と出力メッセージを結び付ける優先照合再項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は優先照合再根拠です。優先照合再保存では VVR 属性の出力行と IDC3009I を一緒に残し、保存名は優先照合再保存です。選択肢ごとの違いを示します。 A: 優先照合再欠落は戻り値や記録番号に寄り、欠落名は優先照合再欠落です。 B: 優先照合再流用は別カテゴリの確認であり、排除名は優先照合再流用です。 C: 優先照合再不足は名称や説明だけに寄り、判定名は優先照合再不足です。 D: 優先照合再正答は対象出力と項目説明を結び、根拠名は優先照合再正答です。優先照合再対象では VVR 属性を DFSMS の確認記録に残し、対象名は優先照合再対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>VVR (VSAM Volume Record)</strong></p><p>検証目的: 上書整理のストレージ管理について、VVR (VSAM Volume Record)は、DFSMS / IDCAMS / VSAM の ICF で機能名、見出し、または確認対象として参照する項目です。VVDS 内のに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020107の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、上書整理のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にVVR (VSAM Volume Rを指定し、OSKB020107の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND VVR (VSAM Volume R
CASE OSKB020107
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM VVR (VSAM Volume R
CASE OSKB020107
SOURCE DFSMS
VVR (VSAM Volume RとOSKB020107が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020107を同じ出力で読み、上書整理のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020107
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020107.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020107が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の VVR (VSAM Volume R と OSKB020107 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020107 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## IMPORT


<section class="kb-item" id="c06-i0150"><h3>IMPORT 基本</h3><p class="kb-meta">分類: IMPORT ・ 難易度: 上級</p><p>IMPORT 基本は、DFSMS / IDCAMS / VSAMのIMPORTで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 呼出分離の基本でストレージ管理の運用確認を行います。IMPORT 基本の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で呼出分離の基本を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず呼出分離の基本を正常終了として記録する。</li><li>C. 属性行、戻り表示、メッセージ見出しを合わせて呼出分離の根拠にする。 <span class="kb-ok">✅ 正解</span></li><li>D. IMPORT 基本の属性行を読まず呼出分離の基本の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 呼出分離正解では選択記号 C を採用し、正解名は呼出分離正解です。呼出分離根拠では IMPORT 基本 は「DFSMS で IMPORT 基本の扱いを記録する呼出分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は呼出分離根拠です。呼出分離受渡では IMPORT 基本の表示結果と IDC0001I を同じ確認単位にし、受渡名は呼出分離受渡です。不適切な選択肢を整理します。 A: 呼出分離流用は別カテゴリの確認であり、排除名は呼出分離流用です。 B: 呼出分離欠落は戻り値や記録番号に寄り、欠落名は呼出分離欠落です。 C: 呼出分離正答は対象出力と項目説明を結び、根拠名は呼出分離正答です。 D: 呼出分離不足は名称や説明だけに寄り、判定名は呼出分離不足です。呼出分離資料では IMPORT 基本の使い方を出典欄から追跡し、資料名は呼出分離資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMPORT 基本</strong></p><p>検証目的: 復旧確認の基本について、IMPORT 基本は、DFSMS / IDCAMS / VSAM の IMPORT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020018の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、復旧確認の基本の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にIMPORT 基本を指定し、OSKB020018の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND IMPORT 基本
CASE OSKB020018
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM IMPORT 基本
CASE OSKB020018
SOURCE DFSMS
IMPORT 基本とOSKB020018が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020018を同じ出力で読み、復旧確認の基本の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020018
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020018.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020018が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の IMPORT 基本 と OSKB020018 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020018 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0151"><h3>INTOEMPTY</h3><p class="kb-meta">分類: IMPORT ・ 難易度: 上級</p><p>事前に空のクラスターを準備し、その属性で IMPORT する。属性を IMPORT 元から維持したくない場合に使う</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換分離のストレージ管理に関する INTOEMPTY の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず置換分離のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換分離のストレージ管理の証跡として保存して根拠にする。</li><li>C. INTOEMPTY の変更点を出力本文から切り離して置換分離のストレージ管理の承認欄だけ残す。</li><li>D. 同じ画面で対象行と IDC0001I を読み、置換分離の結果として保存する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換分離正解では選択記号 D を採用し、正解名は置換分離正解です。置換分離根拠では INTOEMPTY は「INTOEMPTY の状態と出力メッセージを結び付ける置換分離項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は置換分離根拠です。置換分離保存では INTOEMPTY の出力行と IDC0001I を一緒に残し、保存名は置換分離保存です。選択肢ごとの違いを示します。 A: 置換分離欠落は戻り値や記録番号に寄り、欠落名は置換分離欠落です。 B: 置換分離流用は別カテゴリの確認であり、排除名は置換分離流用です。 C: 置換分離不足は名称や説明だけに寄り、判定名は置換分離不足です。 D: 置換分離正答は対象出力と項目説明を結び、根拠名は置換分離正答です。置換分離対象では INTOEMPTY を DFSMS の確認記録に残し、対象名は置換分離対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>INTOEMPTY</strong></p><p>検証目的: 監査確認のストレージ管理について、事前に空のクラスターを準備し、その属性で IMPORT する。属性を IMPORT 元から維持したくない場合に使うに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020019の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、監査確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にINTOEMPTYを指定し、OSKB020019の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND INTOEMPTY
CASE OSKB020019
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM INTOEMPTY
CASE OSKB020019
SOURCE DFSMS
INTOEMPTYとOSKB020019が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB020019を同じ出力で読み、監査確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB020019
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB020019.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB020019が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の INTOEMPTY と OSKB020019 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB020019 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0152"><h3>OBJECTS (IMPORT)</h3><p class="kb-meta">分類: IMPORT ・ 難易度: 上級</p><p>OBJECTS (IMPORT)は、DFSMS / IDCAMS / VSAMのIMPORTで機能名、見出し、または確認対象として参照する項目です。再構築時の個別属性上書き。NEWNAME, VOLUMES, FILE, KEYRANGES 等を指定可能。「OBJECTS (IMPORT)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 終端分離のストレージ管理に関係する OBJECTS (IMPORT)の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、終端分離の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. OBJECTS (IMPORT)の名称と担当者名だけを残して終端分離のストレージ管理の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で終端分離のストレージ管理を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず終端分離のストレージ管理の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 終端分離正解では選択記号 A を採用し、正解名は終端分離正解です。終端分離根拠では OBJECTS (IMPORT) は「OBJECTS (IMPORT)の用途をストレージ管理の表示で確認する終端分離項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は終端分離根拠です。終端分離背景では DFSMS の OBJECTS (IMPORT)と IDC3009I を同じ証跡に残し、背景名は終端分離背景です。他の選択肢を確認します。 A: 終端分離正答は対象出力と項目説明を結び、根拠名は終端分離正答です。 B: 終端分離不足は名称や説明だけに寄り、判定名は終端分離不足です。 C: 終端分離流用は別カテゴリの確認であり、排除名は終端分離流用です。 D: 終端分離欠落は戻り値や記録番号に寄り、欠落名は終端分離欠落です。終端分離用語では OBJECTS (IMPORT)を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は終端分離用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>OBJECTS (IMPORT)</strong></p><p>検証目的: 変更確認のストレージ管理について、OBJECTS (IMPORT)は、DFSMS / IDCAMS / VSAM の IMPORT で機能名、見出し、または確認対象として参照する項目です。再構築時の個別属性上書きに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020020の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))を実行し、IDC3009Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) を入力し、変更確認のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
COMMAND INPUTにDEFINE CLUSTER(NAME(OSKB.VSAM.CASE))が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にOBJECTS (IMPORT)を指定し、OSKB020020の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND OBJECTS (IMPORT)
CASE OSKB020020
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM OBJECTS (IMPORT)
CASE OSKB020020
SOURCE DFSMS
OBJECTS (IMPORT)とOSKB020020が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC3009IとOSKB020020を同じ出力で読み、変更確認のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CASE OSKB020020
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))
CLUSTER ------- OSKB020020.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC3009I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC3009IとOSKB020020が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; DEFINE CLUSTER(NAME(OSKB.VSAM.CASE)) が画面・出力に表示されること
② ステップ2 の OBJECTS (IMPORT) と OSKB020020 が画面・出力に表示されること
③ ステップ3 の IDC3009I と OSKB020020 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## IMPORTRA


<section class="kb-item" id="c06-i0153"><h3>IMPORTRA (リカバリ用)</h3><p class="kb-meta">分類: IMPORTRA ・ 難易度: 上級</p><p>EXPORTRA で取得した RA データからカタログを再構築する旧 IDCAMS コマンド。現行は ICF DIAGNOSE/REPRO で代替されることが多い</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 上書分離のリカバリ用でストレージ管理の運用確認を行います。IMPORTRA (リカバリ用)の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で上書分離のリカバリ用を確認した扱いにする。</li><li>B. IDC0005I の有無を確認せず上書分離のリカバリ用を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、上書分離の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. IMPORTRA (リカバリ用)の属性行を読まず上書分離のリカバリ用の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 上書分離正解では選択記号 C を採用し、正解名は上書分離正解です。上書分離根拠では IMPORTRA (リカバリ用) は「DFSMS で IMPORTRA (リカバリ用)の扱いを記録する上書分離項目」と REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)または該当パネルの出力を照合し、根拠名は上書分離根拠です。上書分離受渡では IMPORTRA (リカバリ用)の表示結果と IDC0005I を同じ確認単位にし、受渡名は上書分離受渡です。不適切な選択肢を整理します。 A: 上書分離流用は別カテゴリの確認であり、排除名は上書分離流用です。 B: 上書分離欠落は戻り値や記録番号に寄り、欠落名は上書分離欠落です。 C: 上書分離正答は対象出力と項目説明を結び、根拠名は上書分離正答です。 D: 上書分離不足は名称や説明だけに寄り、判定名は上書分離不足です。上書分離資料では IMPORTRA (リカバリ用)の使い方を出典欄から追跡し、資料名は上書分離資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IMPORTRA (リカバリ用)</strong></p><p>検証目的: 展開照合のリカバリ用について、EXPORTRA で取得した RA データからカタログを再構築する旧 IDCAMS コマンド。現行は ICF DIAGNOSE/REPRO で代替されることが多いに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB020022の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)を実行し、IDC0005Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) を入力し、展開照合のリカバリ用の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
COMMAND INPUTにREPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)が表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にIMPORTRA (リカバリ用)を指定し、OSKB020022の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND IMPORTRA (リカバリ用)
CASE OSKB020022
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM IMPORTRA (リカバリ用)
CASE OSKB020022
SOURCE DFSMS
IMPORTRA (リカバリ用)とOSKB020022が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0005IとOSKB020022を同じ出力で読み、展開照合のリカバリ用の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
CASE OSKB020022
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT)
CLUSTER ------- OSKB020022.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0005I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0005IとOSKB020022が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; REPRO INDATASET(OSKB.SRC) OUTDATASET(OSKB.TGT) が画面・出力に表示されること
② ステップ2 の IMPORTRA (リカバリ用) と OSKB020022 が画面・出力に表示されること
③ ステップ3 の IDC0005I と OSKB020022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


## LISTCAT


<section class="kb-item" id="c06-i0154"><h3>ALL</h3><p class="kb-meta">分類: LISTCAT ・ 難易度: 上級</p><p>ALLは、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 置換整理のストレージ管理に関する ALL の引き継ぎです。後続担当者へ残すべき確認はどれですか。</p><ul class="kb-choices"><li>A. LISTCAT ENTRIES(OSKBVSAMCASE) ALL の結果を残さず置換整理のストレージ管理の担当者名と日時だけを記録する。</li><li>B. 別製品のメッセージを置換整理のストレージ管理の証跡として保存して根拠にする。</li><li>C. ALL の変更点を出力本文から切り離して置換整理のストレージ管理の承認欄だけ残す。</li><li>D. IDC0001I を含む表示を保存し、説明欄との差分を置換整理で確認する。 <span class="kb-ok">✅ 正解</span></li></ul><p class="kb-meta">正解: <strong>D</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 置換整理正解では選択記号 D を採用し、正解名は置換整理正解です。置換整理根拠では ALL は「ALL の状態と出力メッセージを結び付ける置換整理項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は置換整理根拠です。置換整理保存では ALL の出力行と IDC0001I を一緒に残し、保存名は置換整理保存です。選択肢ごとの違いを示します。 A: 置換整理欠落は戻り値や記録番号に寄り、欠落名は置換整理欠落です。 B: 置換整理流用は別カテゴリの確認であり、排除名は置換整理流用です。 C: 置換整理不足は名称や説明だけに寄り、判定名は置換整理不足です。 D: 置換整理正答は対象出力と項目説明を結び、根拠名は置換整理正答です。置換整理対象では ALL を DFSMS の確認記録に残し、対象名は置換整理対象です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ALL</strong></p><p>検証目的: 監査判定のストレージ管理について、ALL は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出に関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010099の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、監査判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にALLを指定し、OSKB010099の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ALL
CASE OSKB010099
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ALL
CASE OSKB010099
SOURCE DFSMS
ALLとOSKB010099が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010099を同じ出力で読み、監査判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010099
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010099.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010099が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ALL と OSKB010099 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010099 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0155"><h3>ALLOCATION</h3><p class="kb-meta">分類: LISTCAT ・ 難易度: 上級</p><p>ALLOCATIONは、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わるかを出典マニュアルの節で確認します。z/OS DFSMS Access Method Services Commands を参照し、用語だけでなく対象機能と確認すべき状態を結び付けます</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 監査判定のストレージ管理でストレージ管理の運用確認を行います。ALLOCATION の根拠にできる作業はどれですか。</p><ul class="kb-choices"><li>A. DFSMS と無関係な一覧で監査判定のストレージ管理を確認した扱いにする。</li><li>B. IDC0001I の有無を確認せず監査判定のストレージ管理を正常終了として記録する。</li><li>C. 操作結果の本文、対象行、時刻を同じ証跡に入れ、監査判定の確認にする。 <span class="kb-ok">✅ 正解</span></li><li>D. ALLOCATION の属性行を読まず監査判定のストレージ管理の画面名と利用者名だけを保存する。</li></ul><p class="kb-meta">正解: <strong>C</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 監査判定正解では選択記号 C を採用し、正解名は監査判定正解です。監査判定根拠では ALLOCATION は「DFSMS で ALLOCATION の扱いを記録する監査判定項目」と LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL または該当パネルの出力を照合し、根拠名は監査判定根拠です。監査判定受渡では ALLOCATION の表示結果と IDC0001I を同じ確認単位にし、受渡名は監査判定受渡です。不適切な選択肢を整理します。 A: 監査判定流用は別カテゴリの確認であり、排除名は監査判定流用です。 B: 監査判定欠落は戻り値や記録番号に寄り、欠落名は監査判定欠落です。 C: 監査判定正答は対象出力と項目説明を結び、根拠名は監査判定正答です。 D: 監査判定不足は名称や説明だけに寄り、判定名は監査判定不足です。監査判定資料では ALLOCATION の使い方を出典欄から追跡し、資料名は監査判定資料です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ALLOCATION</strong></p><p>検証目的: 比較判定のストレージ管理について、ALLOCATION は、DFSMS / IDCAMS / VSAM の LISTCAT で機能名、見出し、または確認対象として参照する項目です。関連する操作、設定、表示結果のどこに関わる状態・定義・メッセージを机上で照合する。</p><p>前提条件: IDCAMSまたは関連TSO/コンソールを参照でき、OSKB010094の検証用出力を記録できる。</p><p>セッション環境: IDCAMSでLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLを実行し、IDC0001Iを含む表示を確認する。</p><pre class="kb-code">■ ステップ 1
現在の画面はIDCAMSのコマンド入力画面です。COMMAND INPUT ===&gt; に LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL を入力し、比較判定のストレージ管理の確認表示へ進みます。
［操作（入力）］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
→ Enter を押す
［画面・出力］
(IDCAMS)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
COMMAND INPUTにLISTCAT ENTRIES(OSKB.VSAM.CASE) ALLが表示され、対象コマンドを実行する準備ができています。
――――
■ ステップ 2
現在の画面はIDCAMSの表示結果です。FIND欄にALLOCATIONを指定し、OSKB010094の対象行を見つけます。
［操作（入力）］
(IDCAMS Result)
COMMAND INPUT ===&gt; FIND ALLOCATION
CASE OSKB010094
→ Enter を押す
［画面・出力］
(IDCAMS Result)
ITEM ALLOCATION
CASE OSKB010094
SOURCE DFSMS
ALLOCATIONとOSKB010094が同じ表示に現れるため、対象項目の表示範囲を特定できます。
――――
■ ステップ 3
現在の画面はIDCAMSの詳細表示です。IDC0001IとOSKB010094を同じ出力で読み、比較判定のストレージ管理の根拠を記録します。
［操作（入力）］
(IDCAMS Detail)
COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CASE OSKB010094
→ Enter を押す
［画面・出力］
IDCAMS  SYSTEM SERVICES
/* IDCAMS COMMAND */
   LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL
CLUSTER ------- OSKB010094.CLUSTER
IN-CAT --- SYS1.MASTER.CATALOG
IDC0001I FUNCTION COMPLETED, HIGHEST CONDITION CODE WAS 0
IDC0001IとOSKB010094が同じ出力に現れるため、対象項目の確認値として記録できます。
――――</pre><p>合格条件: ① ステップ1 の COMMAND INPUT ===&gt; LISTCAT ENTRIES(OSKB.VSAM.CASE) ALL が画面・出力に表示されること
② ステップ2 の ALLOCATION と OSKB010094 が画面・出力に表示されること
③ ステップ3 の IDC0001I と OSKB010094 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: z / OS DFSMS Access Method Services Commands</p></div></details></section>


<section class="kb-item" id="c06-i0156"><h3>CATALOG(catname)</h3><p class="kb-meta">分類: LISTCAT ・ 難易度: 上級</p><p>CATALOG(catname)は、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。問い合わせ先カタログを明示。エイリアス解決を経ずに特定カタログを直接見たいときに使用。「CATALOG(catname)」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p></section>


<section class="kb-item" id="c06-i0157"><h3>CLUSTER / AIX / PATH / GDG / NONVSAM / USERCATALOG / PAGESPACE / ALIAS</h3><p class="kb-meta">分類: LISTCAT ・ 難易度: 上級</p><p>CLUSTER / AIX / PATH / GDG / NONVSAM / USERCATALOG / PAGESPACE / ALIASは、DFSMS / IDCAMS / VSAMのLISTCATで機能名、見出し、または確認対象として参照する項目です。対象タイプを限定するフィルタ。複数並べて指定可能。「CLUSTER / AIX / PATH / GDG / NONVSAM / USERCATALOG / PAGESPACE / ALIAS」を読むと、DEFINE、ALTER、DELETE、LISTCAT などの操作がカタログ項目と実データのどちらに作用するかを確認しやすい</p><p class="kb-src"><strong>出典:</strong> z / OS DFSMS Access Method Services Commands</p><details class="kb-block"><summary>確認問題（1問）</summary><div class="kb-q"><p><strong>問題.</strong> 警告判定の・ ・ ・に関係する CLUSTER 属性の設問です。一次資料に沿って採るべき確認はどれですか。</p><ul class="kb-choices"><li>A. DEFINE CLUSTER(NAME(OSKBVSAMCASE))で得た表示本文を使い、警告判定の採否を説明欄に結び付ける。 <span class="kb-ok">✅ 正解</span></li><li>B. CLUSTER 属性の名称と担当者名だけを残して警告判定の・ ・ ・の表示本文を対象から外す。</li><li>C. ストレージ管理以外の画面で警告判定の・ ・ ・を確認し同じ証跡として扱ったことにする。</li><li>D. IDC3009I の有無を見ず警告判定の・ ・ ・の戻り値と時刻だけで完了にする。</li></ul><p class="kb-meta">正解: <strong>A</strong> ／ 難易度: 上級</p><p><strong>解説:</strong> 警告判定正解では選択記号 A を採用し、正解名は警告判定正解です。警告判定根拠では CLUSTER 属性 は「CLUSTER 属性の用途をストレージ管理の表示で確認する警告判定項目」と DEFINE CLUSTER(NAME(OSKB.VSAM.CASE))または該当パネルの出力を照合し、根拠名は警告判定根拠です。警告判定背景では DFSMS の CLUSTER 属性と IDC3009I を同じ証跡に残し、背景名は警告判定背景です。他の選択肢を確認します。 A: 警告判定正答は対象出力と項目説明を結び、根拠名は警告判定正答です。 B: 警告判定不足は名称や説明だけに寄り、判定名は警告判定不足です。 C: 警告判定流用は別カテゴリの確認であり、排除名は警告判定流用です。 D: 警告判定欠落は戻り値や記録番号に寄り、欠落名は警告判定欠落です。警告判定用語では CLUSTER 属性を DFSMS / IDCAMS / VSAM で扱う確認対象とし、用語名は警告判定用語です。</p><p class="kb-src"><strong>出典:</strong> zOS31_idak100 / zOS31_ieav200 / zOS31_f54u200</p></div></details></section>
