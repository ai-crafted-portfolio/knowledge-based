---
search:
  exclude: true
---

# IBM Personal Communications 15.0 — 詳細 (1/1)

[← IBM Personal Communications 15.0 の概要へ戻る](index.md)


## 3270 セッション


<section class="kb-item" id="c13-i0001"><h3>SEND file transfer 文字変換確認 再同期判断</h3><p class="kb-meta">分類: 3270 セッション ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の 3270 セッション で扱う「SEND file transfer 文字変換確認 再同期判断」は、PC からホストへファイルを送る Personal Communications の転送機能を文字変換確認の観点で確認する技術項目です。Receive File from HostとRECEIVE transfer 033を同じ記録で見比べることで、キーマップの取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SEND file transfer 文字変換確認 再同期判断</strong></p><p>検証目的: 3270 セッションのSEND file transfer 文字変換確認 再同期判断について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、3270 セッションの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD033.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Receive File from Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE033 C:\TEMP\HOST033.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE033 C:\TEMP\HOST033.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、SEND file transfer 文字変換確認 再同期判断の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、キーマップの取り違えを切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0002"><h3>SEND file transfer 設定ファイル確認 承認履歴</h3><p class="kb-meta">分類: 3270 セッション ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の 3270 セッション で扱う「SEND file transfer 設定ファイル確認 承認履歴」は、PC からホストへファイルを送る Personal Communications の転送機能を設定ファイル確認の観点で確認する技術項目です。Receive File from HostとRECEIVE transfer 013を同じ記録で見比べることで、キーマップの取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SEND file transfer 設定ファイル確認 承認履歴</strong></p><p>検証目的: 3270 セッションのSEND file transfer 設定ファイル確認 承認履歴について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、3270 セッションの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD013.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Receive File from Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE013 C:\TEMP\HOST013.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE013 C:\TEMP\HOST013.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、SEND file transfer 設定ファイル確認 承認履歴の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、キーマップの取り違えを切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0003"><h3>Session Manager 状態確認 復旧手掛かり</h3><p class="kb-meta">分類: 3270 セッション ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の 3270 セッション で扱う「Session Manager 状態確認 復旧手掛かり」は、オンラインのエミュレーターセッションを開始し管理する画面を状態確認の観点で確認する技術項目です。.ws profileとZOS009.wsを同じ記録で見比べることで、プロファイル未保存を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Session Manager 状態確認 復旧手掛かり</strong></p><p>検証目的: 3270 セッションのSession Manager 状態確認 復旧手掛かりについて、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、3270 セッションの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD009.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。.ws profileを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE009 C:\TEMP\HOST009.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE009 C:\TEMP\HOST009.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、Session Manager 状態確認 復旧手掛かりの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、プロファイル未保存を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0004"><h3>Session Manager 転送条件確認 履歴行</h3><p class="kb-meta">分類: 3270 セッション ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の 3270 セッション で扱う「Session Manager 転送条件確認 履歴行」は、オンラインのエミュレーターセッションを開始し管理する画面を転送条件確認の観点で確認する技術項目です。.ws profileとZOS029.wsを同じ記録で見比べることで、プロファイル未保存を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Session Manager 転送条件確認 履歴行</strong></p><p>検証目的: 3270 セッションのSession Manager 転送条件確認 履歴行について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、3270 セッションの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD029.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。.ws profileを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE029 C:\TEMP\HOST029.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE029 C:\TEMP\HOST029.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、Session Manager 転送条件確認 履歴行の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、プロファイル未保存を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0005"><h3>keyboard map 状態確認 警告行</h3><p class="kb-meta">分類: 3270 セッション ・ 難易度: 初級</p><p>IBM Personal Communications 15.0 の 3270 セッション で扱う「keyboard map 状態確認 警告行」は、.kmp で保存されるキー割当の構成を状態確認の観点で確認する技術項目です。Host Certificate ValidationとKBD005.kmpを同じ記録で見比べることで、証明書検証の無効化を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>keyboard map 状態確認 警告行</strong></p><p>検証目的: 3270 セッションのkeyboard map 状態確認 警告行について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、3270 セッションの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD005.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Host Certificate Validationを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE005 C:\TEMP\HOST005.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE005 C:\TEMP\HOST005.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、keyboard map 状態確認 警告行の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、証明書検証の無効化を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0006"><h3>keyboard map 転送条件確認 キーマップ</h3><p class="kb-meta">分類: 3270 セッション ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の 3270 セッション で扱う「keyboard map 転送条件確認 キーマップ」は、.kmp で保存されるキー割当の構成を転送条件確認の観点で確認する技術項目です。Host Certificate ValidationとKBD025.kmpを同じ記録で見比べることで、証明書検証の無効化を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>keyboard map 転送条件確認 キーマップ</strong></p><p>検証目的: 3270 セッションのkeyboard map 転送条件確認 キーマップについて、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、3270 セッションの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD025.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Host Certificate Validationを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE025 C:\TEMP\HOST025.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE025 C:\TEMP\HOST025.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、keyboard map 転送条件確認 キーマップの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、証明書検証の無効化を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0007"><h3>translation table 文字変換確認 サインオフ</h3><p class="kb-meta">分類: 3270 セッション ・ 難易度: 上級</p><p>IBM Personal Communications 15.0 の 3270 セッション で扱う「translation table 文字変換確認 サインオフ」は、.xlt や DBCS translation table で扱う文字変換設定を文字変換確認の観点で確認する技術項目です。Send File to HostとSEND transfer 037を同じ記録で見比べることで、コードページ不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>translation table 文字変換確認 サインオフ</strong></p><p>検証目的: 3270 セッションのtranslation table 文字変換確認 サインオフについて、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、3270 セッションの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD037.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Send File to Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE037 C:\TEMP\HOST037.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE037 C:\TEMP\HOST037.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、translation table 文字変換確認 サインオフの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、コードページ不一致を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0008"><h3>translation table 設定ファイル確認 同期範囲</h3><p class="kb-meta">分類: 3270 セッション ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の 3270 セッション で扱う「translation table 設定ファイル確認 同期範囲」は、.xlt や DBCS translation table で扱う文字変換設定を設定ファイル確認の観点で確認する技術項目です。Send File to HostとSEND transfer 017を同じ記録で見比べることで、コードページ不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>translation table 設定ファイル確認 同期範囲</strong></p><p>検証目的: 3270 セッションのtranslation table 設定ファイル確認 同期範囲について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、3270 セッションの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD017.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Send File to Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE017 C:\TEMP\HOST017.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE017 C:\TEMP\HOST017.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、translation table 設定ファイル確認 同期範囲の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、コードページ不一致を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0009"><h3>workstation profile 状態確認 開始時刻</h3><p class="kb-meta">分類: 3270 セッション ・ 難易度: 初級</p><p>IBM Personal Communications 15.0 の 3270 セッション で扱う「workstation profile 状態確認 開始時刻」は、.ws で保存されるエミュレーター接続プロファイルを状態確認の観点で確認する技術項目です。Session Manager の Online tagとHOSTCERT 001を同じ記録で見比べることで、転送タイプの誤選択を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>workstation profile 状態確認 開始時刻</strong></p><p>検証目的: 3270 セッションのworkstation profile 状態確認 開始時刻について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、3270 セッションの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD001.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Session Manager の Online tagを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE001 C:\TEMP\HOST001.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE001 C:\TEMP\HOST001.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、workstation profile 状態確認 開始時刻の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、転送タイプの誤選択を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0010"><h3>workstation profile 転送条件確認 保護設定</h3><p class="kb-meta">分類: 3270 セッション ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の 3270 セッション で扱う「workstation profile 転送条件確認 保護設定」は、.ws で保存されるエミュレーター接続プロファイルを転送条件確認の観点で確認する技術項目です。Session Manager の Online tagとHOSTCERT 021を同じ記録で見比べることで、転送タイプの誤選択を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>workstation profile 転送条件確認 保護設定</strong></p><p>検証目的: 3270 セッションのworkstation profile 転送条件確認 保護設定について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、3270 セッションの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD021.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Session Manager の Online tagを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE021 C:\TEMP\HOST021.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE021 C:\TEMP\HOST021.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、workstation profile 転送条件確認 保護設定の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、転送タイプの誤選択を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


## TLS 証明書


<section class="kb-item" id="c13-i0011"><h3>3270 session 状態確認 宛先定義</h3><p class="kb-meta">分類: TLS 証明書 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の TLS 証明書 で扱う「3270 session 状態確認 宛先定義」は、zSeries ホストへ接続する端末エミュレーターの画面を状態確認の観点で確認する技術項目です。Send File to HostとSEND transfer 012を同じ記録で見比べることで、コードページ不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>3270 session 状態確認 宛先定義</strong></p><p>検証目的: TLS 証明書の3270 session 状態確認 宛先定義について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、TLS 証明書の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD012.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Send File to Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE012 C:\TEMP\HOST012.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE012 C:\TEMP\HOST012.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、3270 session 状態確認 宛先定義の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、コードページ不一致を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0012"><h3>3270 session 転送条件確認 初期同期</h3><p class="kb-meta">分類: TLS 証明書 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の TLS 証明書 で扱う「3270 session 転送条件確認 初期同期」は、zSeries ホストへ接続する端末エミュレーターの画面を転送条件確認の観点で確認する技術項目です。Send File to HostとSEND transfer 032を同じ記録で見比べることで、コードページ不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>3270 session 転送条件確認 初期同期</strong></p><p>検証目的: TLS 証明書の3270 session 転送条件確認 初期同期について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、TLS 証明書の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD032.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Send File to Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE032 C:\TEMP\HOST032.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE032 C:\TEMP\HOST032.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、3270 session 転送条件確認 初期同期の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、コードページ不一致を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0013"><h3>EHLLAPI 状態確認 識別列</h3><p class="kb-meta">分類: TLS 証明書 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の TLS 証明書 で扱う「EHLLAPI 状態確認 識別列」は、外部プログラムから 3270 セッションを操作するインターフェースを状態確認の観点で確認する技術項目です。Host Certificate ValidationとKBD020.kmpを同じ記録で見比べることで、証明書検証の無効化を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EHLLAPI 状態確認 識別列</strong></p><p>検証目的: TLS 証明書のEHLLAPI 状態確認 識別列について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、TLS 証明書の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD020.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Host Certificate Validationを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE020 C:\TEMP\HOST020.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE020 C:\TEMP\HOST020.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、EHLLAPI 状態確認 識別列の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、証明書検証の無効化を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0014"><h3>EHLLAPI 転送条件確認 キュー状態</h3><p class="kb-meta">分類: TLS 証明書 ・ 難易度: 上級</p><p>IBM Personal Communications 15.0 の TLS 証明書 で扱う「EHLLAPI 転送条件確認 キュー状態」は、外部プログラムから 3270 セッションを操作するインターフェースを転送条件確認の観点で確認する技術項目です。Host Certificate ValidationとKBD040.kmpを同じ記録で見比べることで、証明書検証の無効化を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EHLLAPI 転送条件確認 キュー状態</strong></p><p>検証目的: TLS 証明書のEHLLAPI 転送条件確認 キュー状態について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、TLS 証明書の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD040.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Host Certificate Validationを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE040 C:\TEMP\HOST040.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE040 C:\TEMP\HOST040.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、EHLLAPI 転送条件確認 キュー状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、証明書検証の無効化を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0015"><h3>RECEIVE file transfer 文字変換確認 対象表</h3><p class="kb-meta">分類: TLS 証明書 ・ 難易度: 初級</p><p>IBM Personal Communications 15.0 の TLS 証明書 で扱う「RECEIVE file transfer 文字変換確認 対象表」は、ホストから PC へファイルを受け取る転送機能を文字変換確認の観点で確認する技術項目です。.ws profileとZOS004.wsを同じ記録で見比べることで、プロファイル未保存を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RECEIVE file transfer 文字変換確認 対象表</strong></p><p>検証目的: TLS 証明書のRECEIVE file transfer 文字変換確認 対象表について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、TLS 証明書の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD004.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。.ws profileを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE004 C:\TEMP\HOST004.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE004 C:\TEMP\HOST004.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、RECEIVE file transfer 文字変換確認 対象表の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、プロファイル未保存を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0016"><h3>RECEIVE file transfer 設定ファイル確認 証明書検査</h3><p class="kb-meta">分類: TLS 証明書 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の TLS 証明書 で扱う「RECEIVE file transfer 設定ファイル確認 証明書検査」は、ホストから PC へファイルを受け取る転送機能を設定ファイル確認の観点で確認する技術項目です。.ws profileとZOS024.wsを同じ記録で見比べることで、プロファイル未保存を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RECEIVE file transfer 設定ファイル確認 証明書検査</strong></p><p>検証目的: TLS 証明書のRECEIVE file transfer 設定ファイル確認 証明書検査について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、TLS 証明書の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD024.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。.ws profileを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE024 C:\TEMP\HOST024.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE024 C:\TEMP\HOST024.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、RECEIVE file transfer 設定ファイル確認 証明書検査の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、プロファイル未保存を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0017"><h3>certificate validation 文字変換確認 差分確認</h3><p class="kb-meta">分類: TLS 証明書 ・ 難易度: 初級</p><p>IBM Personal Communications 15.0 の TLS 証明書 で扱う「certificate validation 文字変換確認 差分確認」は、SSL/TLS handshake でホスト証明書を検査する設定を文字変換確認の観点で確認する技術項目です。Receive File from HostとRECEIVE transfer 008を同じ記録で見比べることで、キーマップの取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>certificate validation 文字変換確認 差分確認</strong></p><p>検証目的: TLS 証明書のcertificate validation 文字変換確認 差分確認について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、TLS 証明書の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD008.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Receive File from Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE008 C:\TEMP\HOST008.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE008 C:\TEMP\HOST008.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、certificate validation 文字変換確認 差分確認の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、キーマップの取り違えを切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0018"><h3>certificate validation 設定ファイル確認 出力見出し</h3><p class="kb-meta">分類: TLS 証明書 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の TLS 証明書 で扱う「certificate validation 設定ファイル確認 出力見出し」は、SSL/TLS handshake でホスト証明書を検査する設定を設定ファイル確認の観点で確認する技術項目です。Receive File from HostとRECEIVE transfer 028を同じ記録で見比べることで、キーマップの取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>certificate validation 設定ファイル確認 出力見出し</strong></p><p>検証目的: TLS 証明書のcertificate validation 設定ファイル確認 出力見出しについて、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、TLS 証明書の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD028.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Receive File from Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE028 C:\TEMP\HOST028.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE028 C:\TEMP\HOST028.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、certificate validation 設定ファイル確認 出力見出しの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、キーマップの取り違えを切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0019"><h3>macro 状態確認 構成配布</h3><p class="kb-meta">分類: TLS 証明書 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の TLS 証明書 で扱う「macro 状態確認 構成配布」は、.mac で保存される操作自動化スクリプトを状態確認の観点で確認する技術項目です。Session Manager の Online tagとHOSTCERT 016を同じ記録で見比べることで、転送タイプの誤選択を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>macro 状態確認 構成配布</strong></p><p>検証目的: TLS 証明書のmacro 状態確認 構成配布について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、TLS 証明書の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD016.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Session Manager の Online tagを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE016 C:\TEMP\HOST016.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE016 C:\TEMP\HOST016.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、macro 状態確認 構成配布の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、転送タイプの誤選択を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0020"><h3>macro 転送条件確認 例外記録</h3><p class="kb-meta">分類: TLS 証明書 ・ 難易度: 上級</p><p>IBM Personal Communications 15.0 の TLS 証明書 で扱う「macro 転送条件確認 例外記録」は、.mac で保存される操作自動化スクリプトを転送条件確認の観点で確認する技術項目です。Session Manager の Online tagとHOSTCERT 036を同じ記録で見比べることで、転送タイプの誤選択を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>macro 転送条件確認 例外記録</strong></p><p>検証目的: TLS 証明書のmacro 転送条件確認 例外記録について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、TLS 証明書の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD036.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Session Manager の Online tagを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE036 C:\TEMP\HOST036.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE036 C:\TEMP\HOST036.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、macro 転送条件確認 例外記録の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、転送タイプの誤選択を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


## キーボードマップ


<section class="kb-item" id="c13-i0021"><h3>SEND file transfer 状態確認 文字変換</h3><p class="kb-meta">分類: キーボードマップ ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の キーボードマップ で扱う「SEND file transfer 状態確認 文字変換」は、PC からホストへファイルを送る Personal Communications の転送機能を状態確認の観点で確認する技術項目です。Receive File from HostとRECEIVE transfer 023を同じ記録で見比べることで、キーマップの取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SEND file transfer 状態確認 文字変換</strong></p><p>検証目的: キーボードマップのSEND file transfer 状態確認 文字変換について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、キーボードマップの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD023.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Receive File from Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE023 C:\TEMP\HOST023.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE023 C:\TEMP\HOST023.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、SEND file transfer 状態確認 文字変換の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、キーマップの取り違えを切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0022"><h3>SEND file transfer 転送条件確認 接続先</h3><p class="kb-meta">分類: キーボードマップ ・ 難易度: 初級</p><p>IBM Personal Communications 15.0 の キーボードマップ で扱う「SEND file transfer 転送条件確認 接続先」は、PC からホストへファイルを送る Personal Communications の転送機能を転送条件確認の観点で確認する技術項目です。Receive File from HostとRECEIVE transfer 003を同じ記録で見比べることで、キーマップの取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>SEND file transfer 転送条件確認 接続先</strong></p><p>検証目的: キーボードマップのSEND file transfer 転送条件確認 接続先について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、キーボードマップの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD003.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Receive File from Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE003 C:\TEMP\HOST003.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE003 C:\TEMP\HOST003.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、SEND file transfer 転送条件確認 接続先の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、キーマップの取り違えを切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0023"><h3>Session Manager 文字変換確認 変換規則</h3><p class="kb-meta">分類: キーボードマップ ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の キーボードマップ で扱う「Session Manager 文字変換確認 変換規則」は、オンラインのエミュレーターセッションを開始し管理する画面を文字変換確認の観点で確認する技術項目です。.ws profileとZOS019.wsを同じ記録で見比べることで、プロファイル未保存を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Session Manager 文字変換確認 変換規則</strong></p><p>検証目的: キーボードマップのSession Manager 文字変換確認 変換規則について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、キーボードマップの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD019.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。.ws profileを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE019 C:\TEMP\HOST019.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE019 C:\TEMP\HOST019.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、Session Manager 文字変換確認 変換規則の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、プロファイル未保存を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0024"><h3>Session Manager 設定ファイル確認 レビュー結果</h3><p class="kb-meta">分類: キーボードマップ ・ 難易度: 上級</p><p>IBM Personal Communications 15.0 の キーボードマップ で扱う「Session Manager 設定ファイル確認 レビュー結果」は、オンラインのエミュレーターセッションを開始し管理する画面を設定ファイル確認の観点で確認する技術項目です。.ws profileとZOS039.wsを同じ記録で見比べることで、プロファイル未保存を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Session Manager 設定ファイル確認 レビュー結果</strong></p><p>検証目的: キーボードマップのSession Manager 設定ファイル確認 レビュー結果について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、キーボードマップの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD039.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。.ws profileを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE039 C:\TEMP\HOST039.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE039 C:\TEMP\HOST039.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、Session Manager 設定ファイル確認 レビュー結果の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、プロファイル未保存を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0025"><h3>keyboard map 文字変換確認 接続状態</h3><p class="kb-meta">分類: キーボードマップ ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の キーボードマップ で扱う「keyboard map 文字変換確認 接続状態」は、.kmp で保存されるキー割当の構成を文字変換確認の観点で確認する技術項目です。Host Certificate ValidationとKBD015.kmpを同じ記録で見比べることで、証明書検証の無効化を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>keyboard map 文字変換確認 接続状態</strong></p><p>検証目的: キーボードマップのkeyboard map 文字変換確認 接続状態について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、キーボードマップの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD015.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Host Certificate Validationを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE015 C:\TEMP\HOST015.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE015 C:\TEMP\HOST015.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、keyboard map 文字変換確認 接続状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、証明書検証の無効化を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0026"><h3>keyboard map 設定ファイル確認 取得間隔</h3><p class="kb-meta">分類: キーボードマップ ・ 難易度: 上級</p><p>IBM Personal Communications 15.0 の キーボードマップ で扱う「keyboard map 設定ファイル確認 取得間隔」は、.kmp で保存されるキー割当の構成を設定ファイル確認の観点で確認する技術項目です。Host Certificate ValidationとKBD035.kmpを同じ記録で見比べることで、証明書検証の無効化を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>keyboard map 設定ファイル確認 取得間隔</strong></p><p>検証目的: キーボードマップのkeyboard map 設定ファイル確認 取得間隔について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、キーボードマップの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD035.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Host Certificate Validationを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE035 C:\TEMP\HOST035.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE035 C:\TEMP\HOST035.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、keyboard map 設定ファイル確認 取得間隔の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、証明書検証の無効化を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0027"><h3>translation table 状態確認 入力欄</h3><p class="kb-meta">分類: キーボードマップ ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の キーボードマップ で扱う「translation table 状態確認 入力欄」は、.xlt や DBCS translation table で扱う文字変換設定を状態確認の観点で確認する技術項目です。Send File to HostとSEND transfer 027を同じ記録で見比べることで、コードページ不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>translation table 状態確認 入力欄</strong></p><p>検証目的: キーボードマップのtranslation table 状態確認 入力欄について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、キーボードマップの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD027.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Send File to Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE027 C:\TEMP\HOST027.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE027 C:\TEMP\HOST027.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、translation table 状態確認 入力欄の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、コードページ不一致を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0028"><h3>translation table 転送条件確認 詳細表示</h3><p class="kb-meta">分類: キーボードマップ ・ 難易度: 初級</p><p>IBM Personal Communications 15.0 の キーボードマップ で扱う「translation table 転送条件確認 詳細表示」は、.xlt や DBCS translation table で扱う文字変換設定を転送条件確認の観点で確認する技術項目です。Send File to HostとSEND transfer 007を同じ記録で見比べることで、コードページ不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>translation table 転送条件確認 詳細表示</strong></p><p>検証目的: キーボードマップのtranslation table 転送条件確認 詳細表示について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、キーボードマップの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD007.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Send File to Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE007 C:\TEMP\HOST007.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE007 C:\TEMP\HOST007.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、translation table 転送条件確認 詳細表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、コードページ不一致を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0029"><h3>workstation profile 文字変換確認 保持期間</h3><p class="kb-meta">分類: キーボードマップ ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の キーボードマップ で扱う「workstation profile 文字変換確認 保持期間」は、.ws で保存されるエミュレーター接続プロファイルを文字変換確認の観点で確認する技術項目です。Session Manager の Online tagとHOSTCERT 011を同じ記録で見比べることで、転送タイプの誤選択を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>workstation profile 文字変換確認 保持期間</strong></p><p>検証目的: キーボードマップのworkstation profile 文字変換確認 保持期間について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、キーボードマップの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD011.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Session Manager の Online tagを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE011 C:\TEMP\HOST011.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE011 C:\TEMP\HOST011.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、workstation profile 文字変換確認 保持期間の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、転送タイプの誤選択を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0030"><h3>workstation profile 設定ファイル確認 遅延表示</h3><p class="kb-meta">分類: キーボードマップ ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の キーボードマップ で扱う「workstation profile 設定ファイル確認 遅延表示」は、.ws で保存されるエミュレーター接続プロファイルを設定ファイル確認の観点で確認する技術項目です。Session Manager の Online tagとHOSTCERT 031を同じ記録で見比べることで、転送タイプの誤選択を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>workstation profile 設定ファイル確認 遅延表示</strong></p><p>検証目的: キーボードマップのworkstation profile 設定ファイル確認 遅延表示について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、キーボードマップの対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD031.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Session Manager の Online tagを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE031 C:\TEMP\HOST031.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE031 C:\TEMP\HOST031.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、workstation profile 設定ファイル確認 遅延表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、転送タイプの誤選択を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


## ファイル転送


<section class="kb-item" id="c13-i0031"><h3>3270 session 文字変換確認 転送条件</h3><p class="kb-meta">分類: ファイル転送 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の ファイル転送 で扱う「3270 session 文字変換確認 転送条件」は、zSeries ホストへ接続する端末エミュレーターの画面を文字変換確認の観点で確認する技術項目です。Send File to HostとSEND transfer 022を同じ記録で見比べることで、コードページ不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>3270 session 文字変換確認 転送条件</strong></p><p>検証目的: ファイル転送の3270 session 文字変換確認 転送条件について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ファイル転送の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD022.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Send File to Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE022 C:\TEMP\HOST022.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE022 C:\TEMP\HOST022.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、3270 session 文字変換確認 転送条件の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、コードページ不一致を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0032"><h3>3270 session 設定ファイル確認 停止時刻</h3><p class="kb-meta">分類: ファイル転送 ・ 難易度: 初級</p><p>IBM Personal Communications 15.0 の ファイル転送 で扱う「3270 session 設定ファイル確認 停止時刻」は、zSeries ホストへ接続する端末エミュレーターの画面を設定ファイル確認の観点で確認する技術項目です。Send File to HostとSEND transfer 002を同じ記録で見比べることで、コードページ不一致を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>3270 session 設定ファイル確認 停止時刻</strong></p><p>検証目的: ファイル転送の3270 session 設定ファイル確認 停止時刻について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ファイル転送の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD002.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Send File to Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE002 C:\TEMP\HOST002.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE002 C:\TEMP\HOST002.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、3270 session 設定ファイル確認 停止時刻の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、コードページ不一致を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0033"><h3>EHLLAPI 文字変換確認 統計値</h3><p class="kb-meta">分類: ファイル転送 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の ファイル転送 で扱う「EHLLAPI 文字変換確認 統計値」は、外部プログラムから 3270 セッションを操作するインターフェースを文字変換確認の観点で確認する技術項目です。Host Certificate ValidationとKBD030.kmpを同じ記録で見比べることで、証明書検証の無効化を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EHLLAPI 文字変換確認 統計値</strong></p><p>検証目的: ファイル転送のEHLLAPI 文字変換確認 統計値について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ファイル転送の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD030.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Host Certificate Validationを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE030 C:\TEMP\HOST030.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE030 C:\TEMP\HOST030.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、EHLLAPI 文字変換確認 統計値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、証明書検証の無効化を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0034"><h3>EHLLAPI 設定ファイル確認 監査証跡</h3><p class="kb-meta">分類: ファイル転送 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の ファイル転送 で扱う「EHLLAPI 設定ファイル確認 監査証跡」は、外部プログラムから 3270 セッションを操作するインターフェースを設定ファイル確認の観点で確認する技術項目です。Host Certificate ValidationとKBD010.kmpを同じ記録で見比べることで、証明書検証の無効化を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>EHLLAPI 設定ファイル確認 監査証跡</strong></p><p>検証目的: ファイル転送のEHLLAPI 設定ファイル確認 監査証跡について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ファイル転送の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD010.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Host Certificate Validationを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE010 C:\TEMP\HOST010.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE010 C:\TEMP\HOST010.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、EHLLAPI 設定ファイル確認 監査証跡の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、証明書検証の無効化を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0035"><h3>RECEIVE file transfer 状態確認 適用位置</h3><p class="kb-meta">分類: ファイル転送 ・ 難易度: 上級</p><p>IBM Personal Communications 15.0 の ファイル転送 で扱う「RECEIVE file transfer 状態確認 適用位置」は、ホストから PC へファイルを受け取る転送機能を状態確認の観点で確認する技術項目です。.ws profileとZOS034.wsを同じ記録で見比べることで、プロファイル未保存を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RECEIVE file transfer 状態確認 適用位置</strong></p><p>検証目的: ファイル転送のRECEIVE file transfer 状態確認 適用位置について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ファイル転送の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD034.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。.ws profileを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE034 C:\TEMP\HOST034.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE034 C:\TEMP\HOST034.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、RECEIVE file transfer 状態確認 適用位置の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、プロファイル未保存を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0036"><h3>RECEIVE file transfer 転送条件確認 実行結果</h3><p class="kb-meta">分類: ファイル転送 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の ファイル転送 で扱う「RECEIVE file transfer 転送条件確認 実行結果」は、ホストから PC へファイルを受け取る転送機能を転送条件確認の観点で確認する技術項目です。.ws profileとZOS014.wsを同じ記録で見比べることで、プロファイル未保存を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RECEIVE file transfer 転送条件確認 実行結果</strong></p><p>検証目的: ファイル転送のRECEIVE file transfer 転送条件確認 実行結果について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ファイル転送の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD014.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。.ws profileを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE014 C:\TEMP\HOST014.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE014 C:\TEMP\HOST014.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、RECEIVE file transfer 転送条件確認 実行結果の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、プロファイル未保存を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0037"><h3>certificate validation 状態確認 承認待ち</h3><p class="kb-meta">分類: ファイル転送 ・ 難易度: 上級</p><p>IBM Personal Communications 15.0 の ファイル転送 で扱う「certificate validation 状態確認 承認待ち」は、SSL/TLS handshake でホスト証明書を検査する設定を状態確認の観点で確認する技術項目です。Receive File from HostとRECEIVE transfer 038を同じ記録で見比べることで、キーマップの取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>certificate validation 状態確認 承認待ち</strong></p><p>検証目的: ファイル転送のcertificate validation 状態確認 承認待ちについて、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ファイル転送の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD038.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Receive File from Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE038 C:\TEMP\HOST038.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE038 C:\TEMP\HOST038.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、certificate validation 状態確認 承認待ちの証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、キーマップの取り違えを切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0038"><h3>certificate validation 転送条件確認 集約結果</h3><p class="kb-meta">分類: ファイル転送 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の ファイル転送 で扱う「certificate validation 転送条件確認 集約結果」は、SSL/TLS handshake でホスト証明書を検査する設定を転送条件確認の観点で確認する技術項目です。Receive File from HostとRECEIVE transfer 018を同じ記録で見比べることで、キーマップの取り違えを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>certificate validation 転送条件確認 集約結果</strong></p><p>検証目的: ファイル転送のcertificate validation 転送条件確認 集約結果について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ファイル転送の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD018.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Receive File from Hostを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE018 C:\TEMP\HOST018.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE018 C:\TEMP\HOST018.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、certificate validation 転送条件確認 集約結果の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、キーマップの取り違えを切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0039"><h3>macro 文字変換確認 保存場所</h3><p class="kb-meta">分類: ファイル転送 ・ 難易度: 中級</p><p>IBM Personal Communications 15.0 の ファイル転送 で扱う「macro 文字変換確認 保存場所」は、.mac で保存される操作自動化スクリプトを文字変換確認の観点で確認する技術項目です。Session Manager の Online tagとHOSTCERT 026を同じ記録で見比べることで、転送タイプの誤選択を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>macro 文字変換確認 保存場所</strong></p><p>検証目的: ファイル転送のmacro 文字変換確認 保存場所について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ファイル転送の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD026.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Session Manager の Online tagを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE026 C:\TEMP\HOST026.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE026 C:\TEMP\HOST026.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、macro 文字変換確認 保存場所の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、転送タイプの誤選択を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>


<section class="kb-item" id="c13-i0040"><h3>macro 設定ファイル確認 応答行</h3><p class="kb-meta">分類: ファイル転送 ・ 難易度: 初級</p><p>IBM Personal Communications 15.0 の ファイル転送 で扱う「macro 設定ファイル確認 応答行」は、.mac で保存される操作自動化スクリプトを設定ファイル確認の観点で確認する技術項目です。Session Manager の Online tagとHOSTCERT 006を同じ記録で見比べることで、転送タイプの誤選択を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>macro 設定ファイル確認 応答行</strong></p><p>検証目的: ファイル転送のmacro 設定ファイル確認 応答行について、IBM Personal Communications 15.0の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: IBM Personal Communications 15.0の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はIBM Personal Communications 15.0の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ファイル転送の対象へ進みます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Start Session &gt; ZOS3270.ws
→ Enter を押す
［画面・出力］
Session Manager
ZOS3270.ws Online
Host Code Page 1390
Keyboard Map KBD006.kmp
画面・出力には Session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はIBM Personal Communications 15.0の確認画面です。Session Manager の Online tagを読むため、対象名を含む操作を入力します。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; RECEIVE HOST.FILE006 C:\TEMP\HOST006.TXT ASCII CRLF
→ Enter を押す
［画面・出力］
Personal Communications File Transfer
RECEIVE HOST.FILE006 C:\TEMP\HOST006.TXT ASCII CRLF
Transfer complete
画面・出力には Personal が含まれ、macro 設定ファイル確認 応答行の証跡を確認できます。
――――
■ ステップ 3
現在の画面はIBM Personal Communications 15.0の詳細確認画面です。表示名とメッセージ形式を照合し、転送タイプの誤選択を切り分けます。
［操作（入力）］
IBM Personal Communications 15.0 操作画面
COMMAND ===&gt; ?S Settings &gt; Security &gt; Host Certificate Validation
→ Enter を押す
［画面・出力］
SSL/TLS Host Certificate Validation
Provider Microsoft schannel
Validation Enabled
画面・出力には Host が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Session が画面・出力に表示されること
② ステップ2 の Personal が画面・出力に表示されること
③ ステップ3 の Host が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: PCOMM15-QB_quick_beginnings / PCOMM15-SMP_system_management / Personal Communications 15.0 file transfer and SSL-TLS settings</p></div></details></section>
