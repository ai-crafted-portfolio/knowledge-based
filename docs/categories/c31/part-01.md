---
search:
  exclude: true
---

# Tivoli Log File Agent 6.3 — 詳細 (1/1)

[← Tivoli Log File Agent 6.3 の概要へ戻る](index.md)


## EIF転送


<section class="kb-item" id="c31-i0001"><h3>Format file 一致確認 構成照合</h3><p class="kb-meta">分類: EIF転送 ・ 難易度: 上級</p><p>Tivoli Log File Agent 6.3 の EIF転送 で扱う「Format file 一致確認 構成照合」は、ログ行をイベントクラスへ割り当てる .fmt の照合定義を一致確認の観点で確認する技術項目です。END 行とitmcmd 053を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Format file 一致確認 構成照合</strong></p><p>検証目的: EIF転送のFormat file 一致確認 構成照合について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、EIF転送の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。END 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app053.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app053.log,/var/log/secure053.log
画面・出力には LogSources= が含まれ、Format file 一致確認 構成照合の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app053 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app053
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0002"><h3>Format file 再読込確認 起動確認</h3><p class="kb-meta">分類: EIF転送 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の EIF転送 で扱う「Format file 再読込確認 起動確認」は、ログ行をイベントクラスへ割り当てる .fmt の照合定義を再読込確認の観点で確認する技術項目です。Send EIF Events 値とitmcmd 013を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Format file 再読込確認 起動確認</strong></p><p>検証目的: EIF転送のFormat file 再読込確認 起動確認について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、EIF転送の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。Send EIF Events 値を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app013.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app013.log,/var/log/secure013.log
画面・出力には LogSources= が含まれ、Format file 再読込確認 起動確認の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app013 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app013
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0003"><h3>LogSources 障害切り分け 保持設定</h3><p class="kb-meta">分類: EIF転送 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の EIF転送 で扱う「LogSources 障害切り分け 保持設定」は、監視対象のテキストログファイルを指定する .conf の設定を障害切り分けの観点で確認する技術項目です。itmcmd agent 出力とREGEX class 021を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LogSources 障害切り分け 保持設定</strong></p><p>検証目的: EIF転送のLogSources 障害切り分け 保持設定について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、EIF転送の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。itmcmd agent 出力を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app021.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app021.log,/var/log/secure021.log
画面・出力には LogSources= が含まれ、LogSources 障害切り分け 保持設定の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app021 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app021
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0004"><h3>Send EIF Events 証跡確認 仮想化表示</h3><p class="kb-meta">分類: EIF転送 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の EIF転送 で扱う「Send EIF Events 証跡確認 仮想化表示」は、EIF受信側へイベントを送るかどうかを決める構成項目を証跡確認の観点で確認する技術項目です。RegexLogSources 行とUnmatchLog sample 037を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send EIF Events 証跡確認 仮想化表示</strong></p><p>検証目的: EIF転送のSend EIF Events 証跡確認 仮想化表示について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、EIF転送の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。RegexLogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app037.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app037.log,/var/log/secure037.log
画面・出力には LogSources= が含まれ、Send EIF Events 証跡確認 仮想化表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app037 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app037
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0005"><h3>itmcmd config 障害切り分け 性能値</h3><p class="kb-meta">分類: EIF転送 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の EIF転送 で扱う「itmcmd config 障害切り分け 性能値」は、UNIX で Log File Agent を対話構成するコマンドを障害切り分けの観点で確認する技術項目です。LogSources 行とLogSources 029を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd config 障害切り分け 性能値</strong></p><p>検証目的: EIF転送のitmcmd config 障害切り分け 性能値について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、EIF転送の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。LogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app029.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app029.log,/var/log/secure029.log
画面・出力には LogSources= が含まれ、itmcmd config 障害切り分け 性能値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app029 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app029
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0006"><h3>slot mapping 設定確認 監査証跡</h3><p class="kb-meta">分類: EIF転送 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の EIF転送 で扱う「slot mapping 設定確認 監査証跡」は、正規表現で捕捉した値をイベント属性へ割り当てる定義を設定確認の観点で確認する技術項目です。REGEX ブロックとRegexLogSources profile 045を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>slot mapping 設定確認 監査証跡</strong></p><p>検証目的: EIF転送のslot mapping 設定確認 監査証跡について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、EIF転送の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。REGEX ブロックを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app045.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app045.log,/var/log/secure045.log
画面・出力には LogSources= が含まれ、slot mapping 設定確認 監査証跡の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app045 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app045
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0007"><h3>slot mapping 転送確認 ログ採取</h3><p class="kb-meta">分類: EIF転送 ・ 難易度: 初級</p><p>Tivoli Log File Agent 6.3 の EIF転送 で扱う「slot mapping 転送確認 ログ採取」は、正規表現で捕捉した値をイベント属性へ割り当てる定義を転送確認の観点で確認する技術項目です。UnmatchLog ファイルとRegexLogSources profile 005を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>slot mapping 転送確認 ログ採取</strong></p><p>検証目的: EIF転送のslot mapping 転送確認 ログ採取について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、EIF転送の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。UnmatchLog ファイルを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app005.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app005.log,/var/log/secure005.log
画面・出力には LogSources= が含まれ、slot mapping 転送確認 ログ採取の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app005 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app005
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


## ITMイベント


<section class="kb-item" id="c31-i0008"><h3>REGEX 除外確認 属性確認</h3><p class="kb-meta">分類: ITMイベント ・ 難易度: 上級</p><p>Tivoli Log File Agent 6.3 の ITMイベント で扱う「REGEX 除外確認 属性確認」は、新しい正規表現形式のフォーマット仕様を開始するキーワードを除外確認の観点で確認する技術項目です。UnmatchLog ファイルとLogSources 054を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REGEX 除外確認 属性確認</strong></p><p>検証目的: ITMイベントのREGEX 除外確認 属性確認について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ITMイベントの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app054.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app054.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。UnmatchLog ファイルを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app054.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app054.unmatch
画面・出力には UnmatchLog= が含まれ、REGEX 除外確認 属性確認の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app054.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app054 unmatched sample record for regex tuning
画面・出力には app054 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app054 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0009"><h3>REGEX 障害切り分け 停止確認</h3><p class="kb-meta">分類: ITMイベント ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の ITMイベント で扱う「REGEX 障害切り分け 停止確認」は、新しい正規表現形式のフォーマット仕様を開始するキーワードを障害切り分けの観点で確認する技術項目です。itmcmd agent 出力とLogSources 014を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REGEX 障害切り分け 停止確認</strong></p><p>検証目的: ITMイベントのREGEX 障害切り分け 停止確認について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ITMイベントの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app014.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app014.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。itmcmd agent 出力を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app014.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app014.unmatch
画面・出力には UnmatchLog= が含まれ、REGEX 障害切り分け 停止確認の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app014.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app014 unmatched sample record for regex tuning
画面・出力には app014 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app014 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0010"><h3>RegexLogSources 証跡確認 再開位置</h3><p class="kb-meta">分類: ITMイベント ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の ITMイベント で扱う「RegexLogSources 証跡確認 再開位置」は、ファイル名に正規表現を使って複数ログを指定する .conf の設定を証跡確認の観点で確認する技術項目です。LogSources 行とUnmatchLog sample 022を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RegexLogSources 証跡確認 再開位置</strong></p><p>検証目的: ITMイベントのRegexLogSources 証跡確認 再開位置について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ITMイベントの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app022.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app022.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。LogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app022.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app022.unmatch
画面・出力には UnmatchLog= が含まれ、RegexLogSources 証跡確認 再開位置の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app022.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app022 unmatched sample record for regex tuning
画面・出力には app022 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app022 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0011"><h3>Send ITM Events 設定確認 LPAR表示</h3><p class="kb-meta">分類: ITMイベント ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の ITMイベント で扱う「Send ITM Events 設定確認 LPAR表示」は、Tivoli Enterprise Monitoring Server へイベントを送るかどうかを決める構成項目を設定確認の観点で確認する技術項目です。REGEX ブロックとitmcmd 038を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send ITM Events 設定確認 LPAR表示</strong></p><p>検証目的: ITMイベントのSend ITM Events 設定確認 LPAR表示について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ITMイベントの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app038.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app038.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。REGEX ブロックを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app038.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app038.unmatch
画面・出力には UnmatchLog= が含まれ、Send ITM Events 設定確認 LPAR表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app038.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app038 unmatched sample record for regex tuning
画面・出力には app038 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app038 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0012"><h3>UnmatchLog 一致確認 確認範囲</h3><p class="kb-meta">分類: ITMイベント ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の ITMイベント で扱う「UnmatchLog 一致確認 確認範囲」は、どの仕様にも一致しないログ行を保存する .conf の設定を一致確認の観点で確認する技術項目です。END 行とREGEX class 046を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UnmatchLog 一致確認 確認範囲</strong></p><p>検証目的: ITMイベントのUnmatchLog 一致確認 確認範囲について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ITMイベントの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app046.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app046.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。END 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app046.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app046.unmatch
画面・出力には UnmatchLog= が含まれ、UnmatchLog 一致確認 確認範囲の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app046.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app046 unmatched sample record for regex tuning
画面・出力には app046 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app046 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0013"><h3>UnmatchLog 再読込確認 実行結果</h3><p class="kb-meta">分類: ITMイベント ・ 難易度: 初級</p><p>Tivoli Log File Agent 6.3 の ITMイベント で扱う「UnmatchLog 再読込確認 実行結果」は、どの仕様にも一致しないログ行を保存する .conf の設定を再読込確認の観点で確認する技術項目です。Send EIF Events 値とREGEX class 006を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UnmatchLog 再読込確認 実行結果</strong></p><p>検証目的: ITMイベントのUnmatchLog 再読込確認 実行結果について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ITMイベントの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app006.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app006.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。Send EIF Events 値を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app006.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app006.unmatch
画面・出力には UnmatchLog= が含まれ、UnmatchLog 再読込確認 実行結果の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app006.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app006 unmatched sample record for regex tuning
画面・出力には app006 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app006 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0014"><h3>itmcmd agent start 証跡確認 キュー状態</h3><p class="kb-meta">分類: ITMイベント ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の ITMイベント で扱う「itmcmd agent start 証跡確認 キュー状態」は、構成済みインスタンスを起動するコマンドを証跡確認の観点で確認する技術項目です。RegexLogSources 行とRegexLogSources profile 030を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd agent start 証跡確認 キュー状態</strong></p><p>検証目的: ITMイベントのitmcmd agent start 証跡確認 キュー状態について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ITMイベントの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app030.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app030.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。RegexLogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app030.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app030.unmatch
画面・出力には UnmatchLog= が含まれ、itmcmd agent start 証跡確認 キュー状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app030.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app030 unmatched sample record for regex tuning
画面・出力には app030 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app030 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


## UnmatchLog


<section class="kb-item" id="c31-i0015"><h3>Format file 設定確認 サンプル採取</h3><p class="kb-meta">分類: UnmatchLog ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の UnmatchLog で扱う「Format file 設定確認 サンプル採取」は、ログ行をイベントクラスへ割り当てる .fmt の照合定義を設定確認の観点で確認する技術項目です。RegexLogSources 行とitmcmd 023を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Format file 設定確認 サンプル採取</strong></p><p>検証目的: UnmatchLogのFormat file 設定確認 サンプル採取について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、UnmatchLogの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App023/,/^END/p&#x27; app023.fmt
→ Enter を押す
［画面・出力］
REGEX App023Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。RegexLogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app023.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus023.example.com
ServerPort=5529
画面・出力には Send が含まれ、Format file 設定確認 サンプル採取の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app023.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0016"><h3>LogSources 一致確認 装置一覧</h3><p class="kb-meta">分類: UnmatchLog ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の UnmatchLog で扱う「LogSources 一致確認 装置一覧」は、監視対象のテキストログファイルを指定する .conf の設定を一致確認の観点で確認する技術項目です。REGEX ブロックとREGEX class 031を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LogSources 一致確認 装置一覧</strong></p><p>検証目的: UnmatchLogのLogSources 一致確認 装置一覧について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、UnmatchLogの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App031/,/^END/p&#x27; app031.fmt
→ Enter を押す
［画面・出力］
REGEX App031Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。REGEX ブロックを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app031.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus031.example.com
ServerPort=5529
画面・出力には Send が含まれ、LogSources 一致確認 装置一覧の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app031.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0017"><h3>Send EIF Events 除外確認 対象ノード</h3><p class="kb-meta">分類: UnmatchLog ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の UnmatchLog で扱う「Send EIF Events 除外確認 対象ノード」は、EIF受信側へイベントを送るかどうかを決める構成項目を除外確認の観点で確認する技術項目です。UnmatchLog ファイルとUnmatchLog sample 047を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send EIF Events 除外確認 対象ノード</strong></p><p>検証目的: UnmatchLogのSend EIF Events 除外確認 対象ノードについて、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、UnmatchLogの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App047/,/^END/p&#x27; app047.fmt
→ Enter を押す
［画面・出力］
REGEX App047Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。UnmatchLog ファイルを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app047.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus047.example.com
ServerPort=5529
画面・出力には Send が含まれ、Send EIF Events 除外確認 対象ノードの証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app047.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0018"><h3>Send EIF Events 障害切り分け 識別値</h3><p class="kb-meta">分類: UnmatchLog ・ 難易度: 初級</p><p>Tivoli Log File Agent 6.3 の UnmatchLog で扱う「Send EIF Events 障害切り分け 識別値」は、EIF受信側へイベントを送るかどうかを決める構成項目を障害切り分けの観点で確認する技術項目です。itmcmd agent 出力とUnmatchLog sample 007を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send EIF Events 障害切り分け 識別値</strong></p><p>検証目的: UnmatchLogのSend EIF Events 障害切り分け 識別値について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、UnmatchLogの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App007/,/^END/p&#x27; app007.fmt
→ Enter を押す
［画面・出力］
REGEX App007Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。itmcmd agent 出力を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app007.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus007.example.com
ServerPort=5529
画面・出力には Send が含まれ、Send EIF Events 障害切り分け 識別値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app007.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0019"><h3>itmcmd config 一致確認 サービス状態</h3><p class="kb-meta">分類: UnmatchLog ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の UnmatchLog で扱う「itmcmd config 一致確認 サービス状態」は、UNIX で Log File Agent を対話構成するコマンドを一致確認の観点で確認する技術項目です。END 行とLogSources 039を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd config 一致確認 サービス状態</strong></p><p>検証目的: UnmatchLogのitmcmd config 一致確認 サービス状態について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、UnmatchLogの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App039/,/^END/p&#x27; app039.fmt
→ Enter を押す
［画面・出力］
REGEX App039Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。END 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app039.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus039.example.com
ServerPort=5529
画面・出力には Send が含まれ、itmcmd config 一致確認 サービス状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app039.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0020"><h3>slot mapping 証跡確認 再読込</h3><p class="kb-meta">分類: UnmatchLog ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の UnmatchLog で扱う「slot mapping 証跡確認 再読込」は、正規表現で捕捉した値をイベント属性へ割り当てる定義を証跡確認の観点で確認する技術項目です。LogSources 行とRegexLogSources profile 015を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>slot mapping 証跡確認 再読込</strong></p><p>検証目的: UnmatchLogのslot mapping 証跡確認 再読込について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、UnmatchLogの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App015/,/^END/p&#x27; app015.fmt
→ Enter を押す
［画面・出力］
REGEX App015Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。LogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app015.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus015.example.com
ServerPort=5529
画面・出力には Send が含まれ、slot mapping 証跡確認 再読込の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app015.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0021"><h3>slot mapping 起動確認 ログ採取</h3><p class="kb-meta">分類: UnmatchLog ・ 難易度: 上級</p><p>Tivoli Log File Agent 6.3 の UnmatchLog で扱う「slot mapping 起動確認 ログ採取」は、正規表現で捕捉した値をイベント属性へ割り当てる定義を起動確認の観点で確認する技術項目です。Send EIF Events 値とRegexLogSources profile 055を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>slot mapping 起動確認 ログ採取</strong></p><p>検証目的: UnmatchLogのslot mapping 起動確認 ログ採取について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、UnmatchLogの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App055/,/^END/p&#x27; app055.fmt
→ Enter を押す
［画面・出力］
REGEX App055Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。Send EIF Events 値を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app055.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus055.example.com
ServerPort=5529
画面・出力には Send が含まれ、slot mapping 起動確認 ログ採取の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app055.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


## エージェント起動


<section class="kb-item" id="c31-i0022"><h3>REGEX 一致確認 メッセージ行</h3><p class="kb-meta">分類: エージェント起動 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の エージェント起動 で扱う「REGEX 一致確認 メッセージ行」は、新しい正規表現形式のフォーマット仕様を開始するキーワードを一致確認の観点で確認する技術項目です。REGEX ブロックとLogSources 024を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REGEX 一致確認 メッセージ行</strong></p><p>検証目的: エージェント起動のREGEX 一致確認 メッセージ行について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エージェント起動の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app024.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。REGEX ブロックを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app024.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、REGEX 一致確認 メッセージ行の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app024.fmt
→ Enter を押す
［画面・出力］
File: app024.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0023"><h3>RegexLogSources 除外確認 製品レベル</h3><p class="kb-meta">分類: エージェント起動 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の エージェント起動 で扱う「RegexLogSources 除外確認 製品レベル」は、ファイル名に正規表現を使って複数ログを指定する .conf の設定を除外確認の観点で確認する技術項目です。END 行とUnmatchLog sample 032を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RegexLogSources 除外確認 製品レベル</strong></p><p>検証目的: エージェント起動のRegexLogSources 除外確認 製品レベルについて、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エージェント起動の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app032.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。END 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app032.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、RegexLogSources 除外確認 製品レベルの証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app032.fmt
→ Enter を押す
［画面・出力］
File: app032.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0024"><h3>Send ITM Events 証跡確認 障害記録</h3><p class="kb-meta">分類: エージェント起動 ・ 難易度: 初級</p><p>Tivoli Log File Agent 6.3 の エージェント起動 で扱う「Send ITM Events 証跡確認 障害記録」は、Tivoli Enterprise Monitoring Server へイベントを送るかどうかを決める構成項目を証跡確認の観点で確認する技術項目です。LogSources 行とitmcmd 008を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send ITM Events 証跡確認 障害記録</strong></p><p>検証目的: エージェント起動のSend ITM Events 証跡確認 障害記録について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エージェント起動の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app008.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。LogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app008.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、Send ITM Events 証跡確認 障害記録の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app008.fmt
→ Enter を押す
［画面・出力］
File: app008.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0025"><h3>Send ITM Events 起動確認 時刻情報</h3><p class="kb-meta">分類: エージェント起動 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の エージェント起動 で扱う「Send ITM Events 起動確認 時刻情報」は、Tivoli Enterprise Monitoring Server へイベントを送るかどうかを決める構成項目を起動確認の観点で確認する技術項目です。Send EIF Events 値とitmcmd 048を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send ITM Events 起動確認 時刻情報</strong></p><p>検証目的: エージェント起動のSend ITM Events 起動確認 時刻情報について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エージェント起動の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app048.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。Send EIF Events 値を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app048.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、Send ITM Events 起動確認 時刻情報の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app048.fmt
→ Enter を押す
［画面・出力］
File: app048.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0026"><h3>UnmatchLog 設定確認 対象ファイル</h3><p class="kb-meta">分類: エージェント起動 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の エージェント起動 で扱う「UnmatchLog 設定確認 対象ファイル」は、どの仕様にも一致しないログ行を保存する .conf の設定を設定確認の観点で確認する技術項目です。RegexLogSources 行とREGEX class 016を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UnmatchLog 設定確認 対象ファイル</strong></p><p>検証目的: エージェント起動のUnmatchLog 設定確認 対象ファイルについて、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エージェント起動の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app016.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。RegexLogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app016.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、UnmatchLog 設定確認 対象ファイルの証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app016.fmt
→ Enter を押す
［画面・出力］
File: app016.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0027"><h3>UnmatchLog 転送確認 実行結果</h3><p class="kb-meta">分類: エージェント起動 ・ 難易度: 上級</p><p>Tivoli Log File Agent 6.3 の エージェント起動 で扱う「UnmatchLog 転送確認 実行結果」は、どの仕様にも一致しないログ行を保存する .conf の設定を転送確認の観点で確認する技術項目です。itmcmd agent 出力とREGEX class 056を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UnmatchLog 転送確認 実行結果</strong></p><p>検証目的: エージェント起動のUnmatchLog 転送確認 実行結果について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エージェント起動の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app056.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。itmcmd agent 出力を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app056.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、UnmatchLog 転送確認 実行結果の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app056.fmt
→ Enter を押す
［画面・出力］
File: app056.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0028"><h3>itmcmd agent start 除外確認 変更証跡</h3><p class="kb-meta">分類: エージェント起動 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の エージェント起動 で扱う「itmcmd agent start 除外確認 変更証跡」は、構成済みインスタンスを起動するコマンドを除外確認の観点で確認する技術項目です。UnmatchLog ファイルとRegexLogSources profile 040を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd agent start 除外確認 変更証跡</strong></p><p>検証目的: エージェント起動のitmcmd agent start 除外確認 変更証跡について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、エージェント起動の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app040.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。UnmatchLog ファイルを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app040.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、itmcmd agent start 除外確認 変更証跡の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app040.fmt
→ Enter を押す
［画面・出力］
File: app040.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


## フォーマットファイル


<section class="kb-item" id="c31-i0029"><h3>REGEX 転送確認 ファイルセット</h3><p class="kb-meta">分類: フォーマットファイル ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の フォーマットファイル で扱う「REGEX 転送確認 ファイルセット」は、新しい正規表現形式のフォーマット仕様を開始するキーワードを転送確認の観点で確認する技術項目です。Send EIF Events 値とLogSources 034を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REGEX 転送確認 ファイルセット</strong></p><p>検証目的: フォーマットファイルのREGEX 転送確認 ファイルセットについて、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、フォーマットファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app034.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app034.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。Send EIF Events 値を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app034.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app034.unmatch
画面・出力には UnmatchLog= が含まれ、REGEX 転送確認 ファイルセットの証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app034.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app034 unmatched sample record for regex tuning
画面・出力には app034 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app034 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0030"><h3>RegexLogSources 一致確認 詳細表示</h3><p class="kb-meta">分類: フォーマットファイル ・ 難易度: 初級</p><p>Tivoli Log File Agent 6.3 の フォーマットファイル で扱う「RegexLogSources 一致確認 詳細表示」は、ファイル名に正規表現を使って複数ログを指定する .conf の設定を一致確認の観点で確認する技術項目です。RegexLogSources 行とUnmatchLog sample 002を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RegexLogSources 一致確認 詳細表示</strong></p><p>検証目的: フォーマットファイルのRegexLogSources 一致確認 詳細表示について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、フォーマットファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app002.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app002.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。RegexLogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app002.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app002.unmatch
画面・出力には UnmatchLog= が含まれ、RegexLogSources 一致確認 詳細表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app002.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app002 unmatched sample record for regex tuning
画面・出力には app002 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app002 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0031"><h3>RegexLogSources 再読込確認 資料見出し</h3><p class="kb-meta">分類: フォーマットファイル ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の フォーマットファイル で扱う「RegexLogSources 再読込確認 資料見出し」は、ファイル名に正規表現を使って複数ログを指定する .conf の設定を再読込確認の観点で確認する技術項目です。itmcmd agent 出力とUnmatchLog sample 042を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RegexLogSources 再読込確認 資料見出し</strong></p><p>検証目的: フォーマットファイルのRegexLogSources 再読込確認 資料見出しについて、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、フォーマットファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app042.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app042.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。itmcmd agent 出力を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app042.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app042.unmatch
画面・出力には UnmatchLog= が含まれ、RegexLogSources 再読込確認 資料見出しの証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app042.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app042 unmatched sample record for regex tuning
画面・出力には app042 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app042 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0032"><h3>Send ITM Events 除外確認 除外条件</h3><p class="kb-meta">分類: フォーマットファイル ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の フォーマットファイル で扱う「Send ITM Events 除外確認 除外条件」は、Tivoli Enterprise Monitoring Server へイベントを送るかどうかを決める構成項目を除外確認の観点で確認する技術項目です。END 行とitmcmd 018を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send ITM Events 除外確認 除外条件</strong></p><p>検証目的: フォーマットファイルのSend ITM Events 除外確認 除外条件について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、フォーマットファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app018.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app018.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。END 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app018.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app018.unmatch
画面・出力には UnmatchLog= が含まれ、Send ITM Events 除外確認 除外条件の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app018.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app018 unmatched sample record for regex tuning
画面・出力には app018 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app018 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0033"><h3>Send ITM Events 障害切り分け 障害記録</h3><p class="kb-meta">分類: フォーマットファイル ・ 難易度: 上級</p><p>Tivoli Log File Agent 6.3 の フォーマットファイル で扱う「Send ITM Events 障害切り分け 障害記録」は、Tivoli Enterprise Monitoring Server へイベントを送るかどうかを決める構成項目を障害切り分けの観点で確認する技術項目です。RegexLogSources 行とitmcmd 058を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send ITM Events 障害切り分け 障害記録</strong></p><p>検証目的: フォーマットファイルのSend ITM Events 障害切り分け 障害記録について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、フォーマットファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app058.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app058.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。RegexLogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app058.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app058.unmatch
画面・出力には UnmatchLog= が含まれ、Send ITM Events 障害切り分け 障害記録の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app058.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app058 unmatched sample record for regex tuning
画面・出力には app058 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app058 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0034"><h3>UnmatchLog 起動確認 ディスク状態</h3><p class="kb-meta">分類: フォーマットファイル ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の フォーマットファイル で扱う「UnmatchLog 起動確認 ディスク状態」は、どの仕様にも一致しないログ行を保存する .conf の設定を起動確認の観点で確認する技術項目です。UnmatchLog ファイルとREGEX class 026を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UnmatchLog 起動確認 ディスク状態</strong></p><p>検証目的: フォーマットファイルのUnmatchLog 起動確認 ディスク状態について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、フォーマットファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app026.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app026.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。UnmatchLog ファイルを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app026.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app026.unmatch
画面・出力には UnmatchLog= が含まれ、UnmatchLog 起動確認 ディスク状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app026.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app026 unmatched sample record for regex tuning
画面・出力には app026 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app026 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0035"><h3>itmcmd agent start 一致確認 保存場所</h3><p class="kb-meta">分類: フォーマットファイル ・ 難易度: 初級</p><p>Tivoli Log File Agent 6.3 の フォーマットファイル で扱う「itmcmd agent start 一致確認 保存場所」は、構成済みインスタンスを起動するコマンドを一致確認の観点で確認する技術項目です。REGEX ブロックとRegexLogSources profile 010を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd agent start 一致確認 保存場所</strong></p><p>検証目的: フォーマットファイルのitmcmd agent start 一致確認 保存場所について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、フォーマットファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app010.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app010.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。REGEX ブロックを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app010.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app010.unmatch
画面・出力には UnmatchLog= が含まれ、itmcmd agent start 一致確認 保存場所の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app010.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app010 unmatched sample record for regex tuning
画面・出力には app010 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app010 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0036"><h3>itmcmd agent start 再読込確認 警告行</h3><p class="kb-meta">分類: フォーマットファイル ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の フォーマットファイル で扱う「itmcmd agent start 再読込確認 警告行」は、構成済みインスタンスを起動するコマンドを再読込確認の観点で確認する技術項目です。LogSources 行とRegexLogSources profile 050を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd agent start 再読込確認 警告行</strong></p><p>検証目的: フォーマットファイルのitmcmd agent start 再読込確認 警告行について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、フォーマットファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^RegexLogSources&#x27; app050.conf
→ Enter を押す
［画面・出力］
RegexLogSources=/var/log/app050.*\.log,/other/logs/[a-z]{0\,3}\.log
画面・出力には RegexLogSources= が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。LogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^UnmatchLog&#x27; app050.conf
→ Enter を押す
［画面・出力］
UnmatchLog=/var/log/lfa/app050.unmatch
画面・出力には UnmatchLog= が含まれ、itmcmd agent start 再読込確認 警告行の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; tail /var/log/lfa/app050.unmatch
→ Enter を押す
［画面・出力］
2026-07-14 09:00:00 app050 unmatched sample record for regex tuning
画面・出力には app050 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の RegexLogSources= が画面・出力に表示されること
② ステップ2 の UnmatchLog= が画面・出力に表示されること
③ ステップ3 の app050 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


## ログソース


<section class="kb-item" id="c31-i0037"><h3>Format file 除外確認 構成照合</h3><p class="kb-meta">分類: ログソース ・ 難易度: 初級</p><p>Tivoli Log File Agent 6.3 の ログソース で扱う「Format file 除外確認 構成照合」は、ログ行をイベントクラスへ割り当てる .fmt の照合定義を除外確認の観点で確認する技術項目です。REGEX ブロックとitmcmd 003を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Format file 除外確認 構成照合</strong></p><p>検証目的: ログソースのFormat file 除外確認 構成照合について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ログソースの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App003/,/^END/p&#x27; app003.fmt
→ Enter を押す
［画面・出力］
REGEX App003Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。REGEX ブロックを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app003.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus003.example.com
ServerPort=5529
画面・出力には Send が含まれ、Format file 除外確認 構成照合の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app003.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0038"><h3>Format file 障害切り分け 運用記録</h3><p class="kb-meta">分類: ログソース ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の ログソース で扱う「Format file 障害切り分け 運用記録」は、ログ行をイベントクラスへ割り当てる .fmt の照合定義を障害切り分けの観点で確認する技術項目です。LogSources 行とitmcmd 043を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Format file 障害切り分け 運用記録</strong></p><p>検証目的: ログソースのFormat file 障害切り分け 運用記録について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ログソースの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App043/,/^END/p&#x27; app043.fmt
→ Enter を押す
［画面・出力］
REGEX App043Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。LogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app043.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus043.example.com
ServerPort=5529
画面・出力には Send が含まれ、Format file 障害切り分け 運用記録の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app043.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0039"><h3>LogSources 証跡確認 状態確認</h3><p class="kb-meta">分類: ログソース ・ 難易度: 上級</p><p>Tivoli Log File Agent 6.3 の ログソース で扱う「LogSources 証跡確認 状態確認」は、監視対象のテキストログファイルを指定する .conf の設定を証跡確認の観点で確認する技術項目です。RegexLogSources 行とREGEX class 051を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LogSources 証跡確認 状態確認</strong></p><p>検証目的: ログソースのLogSources 証跡確認 状態確認について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ログソースの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App051/,/^END/p&#x27; app051.fmt
→ Enter を押す
［画面・出力］
REGEX App051Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。RegexLogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app051.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus051.example.com
ServerPort=5529
画面・出力には Send が含まれ、LogSources 証跡確認 状態確認の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app051.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0040"><h3>LogSources 起動確認 照合単位</h3><p class="kb-meta">分類: ログソース ・ 難易度: 初級</p><p>Tivoli Log File Agent 6.3 の ログソース で扱う「LogSources 起動確認 照合単位」は、監視対象のテキストログファイルを指定する .conf の設定を起動確認の観点で確認する技術項目です。END 行とREGEX class 011を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LogSources 起動確認 照合単位</strong></p><p>検証目的: ログソースのLogSources 起動確認 照合単位について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ログソースの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App011/,/^END/p&#x27; app011.fmt
→ Enter を押す
［画面・出力］
REGEX App011Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。END 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app011.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus011.example.com
ServerPort=5529
画面・出力には Send が含まれ、LogSources 起動確認 照合単位の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app011.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0041"><h3>Send EIF Events 転送確認 ボリューム状態</h3><p class="kb-meta">分類: ログソース ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の ログソース で扱う「Send EIF Events 転送確認 ボリューム状態」は、EIF受信側へイベントを送るかどうかを決める構成項目を転送確認の観点で確認する技術項目です。Send EIF Events 値とUnmatchLog sample 027を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send EIF Events 転送確認 ボリューム状態</strong></p><p>検証目的: ログソースのSend EIF Events 転送確認 ボリューム状態について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ログソースの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App027/,/^END/p&#x27; app027.fmt
→ Enter を押す
［画面・出力］
REGEX App027Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。Send EIF Events 値を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app027.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus027.example.com
ServerPort=5529
画面・出力には Send が含まれ、Send EIF Events 転送確認 ボリューム状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app027.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0042"><h3>itmcmd config 証跡確認 出力見出し</h3><p class="kb-meta">分類: ログソース ・ 難易度: 上級</p><p>Tivoli Log File Agent 6.3 の ログソース で扱う「itmcmd config 証跡確認 出力見出し」は、UNIX で Log File Agent を対話構成するコマンドを証跡確認の観点で確認する技術項目です。REGEX ブロックとLogSources 059を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd config 証跡確認 出力見出し</strong></p><p>検証目的: ログソースのitmcmd config 証跡確認 出力見出しについて、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ログソースの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App059/,/^END/p&#x27; app059.fmt
→ Enter を押す
［画面・出力］
REGEX App059Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。REGEX ブロックを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app059.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus059.example.com
ServerPort=5529
画面・出力には Send が含まれ、itmcmd config 証跡確認 出力見出しの証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app059.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0043"><h3>itmcmd config 起動確認 イベント転送</h3><p class="kb-meta">分類: ログソース ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の ログソース で扱う「itmcmd config 起動確認 イベント転送」は、UNIX で Log File Agent を対話構成するコマンドを起動確認の観点で確認する技術項目です。UnmatchLog ファイルとLogSources 019を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd config 起動確認 イベント転送</strong></p><p>検証目的: ログソースのitmcmd config 起動確認 イベント転送について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ログソースの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App019/,/^END/p&#x27; app019.fmt
→ Enter を押す
［画面・出力］
REGEX App019Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。UnmatchLog ファイルを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app019.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus019.example.com
ServerPort=5529
画面・出力には Send が含まれ、itmcmd config 起動確認 イベント転送の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app019.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0044"><h3>slot mapping 再読込確認 チューニング値</h3><p class="kb-meta">分類: ログソース ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の ログソース で扱う「slot mapping 再読込確認 チューニング値」は、正規表現で捕捉した値をイベント属性へ割り当てる定義を再読込確認の観点で確認する技術項目です。itmcmd agent 出力とRegexLogSources profile 035を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>slot mapping 再読込確認 チューニング値</strong></p><p>検証目的: ログソースのslot mapping 再読込確認 チューニング値について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、ログソースの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; sed -n &#x27;/^REGEX App035/,/^END/p&#x27; app035.fmt
→ Enter を押す
［画面・出力］
REGEX App035Alert
ERROR ([0-9]+) (.*)
msg $2
END
画面・出力には REGEX が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。itmcmd agent 出力を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^Send EIF Events&#x27; app035.conf
→ Enter を押す
［画面・出力］
Send EIF Events=Yes
ServerLocation=omnibus035.example.com
ServerPort=5529
画面・出力には Send が含まれ、slot mapping 再読込確認 チューニング値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^BufEvtMaxSize&#x27; app035.conf
→ Enter を押す
［画面・出力］
BufEvtMaxSize=1024
画面・出力には BufEvtMaxSize=1024 が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の REGEX が画面・出力に表示されること
② ステップ2 の Send が画面・出力に表示されること
③ ステップ3 の BufEvtMaxSize=1024 が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


## 構成ファイル


<section class="kb-item" id="c31-i0045"><h3>Format file 起動確認 エラー詳細</h3><p class="kb-meta">分類: 構成ファイル ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の 構成ファイル で扱う「Format file 起動確認 エラー詳細」は、ログ行をイベントクラスへ割り当てる .fmt の照合定義を起動確認の観点で確認する技術項目です。UnmatchLog ファイルとitmcmd 033を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Format file 起動確認 エラー詳細</strong></p><p>検証目的: 構成ファイルのFormat file 起動確認 エラー詳細について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、構成ファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。UnmatchLog ファイルを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app033.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app033.log,/var/log/secure033.log
画面・出力には LogSources= が含まれ、Format file 起動確認 エラー詳細の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app033 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app033
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0046"><h3>LogSources 設定確認 状態確認</h3><p class="kb-meta">分類: 構成ファイル ・ 難易度: 初級</p><p>Tivoli Log File Agent 6.3 の 構成ファイル で扱う「LogSources 設定確認 状態確認」は、監視対象のテキストログファイルを指定する .conf の設定を設定確認の観点で確認する技術項目です。LogSources 行とREGEX class 001を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LogSources 設定確認 状態確認</strong></p><p>検証目的: 構成ファイルのLogSources 設定確認 状態確認について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、構成ファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。LogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app001.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app001.log,/var/log/secure001.log
画面・出力には LogSources= が含まれ、LogSources 設定確認 状態確認の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app001 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app001
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0047"><h3>LogSources 転送確認 出力比較</h3><p class="kb-meta">分類: 構成ファイル ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の 構成ファイル で扱う「LogSources 転送確認 出力比較」は、監視対象のテキストログファイルを指定する .conf の設定を転送確認の観点で確認する技術項目です。Send EIF Events 値とREGEX class 041を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>LogSources 転送確認 出力比較</strong></p><p>検証目的: 構成ファイルのLogSources 転送確認 出力比較について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、構成ファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。Send EIF Events 値を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app041.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app041.log,/var/log/secure041.log
画面・出力には LogSources= が含まれ、LogSources 転送確認 出力比較の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app041 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app041
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0048"><h3>Send EIF Events 一致確認 一致条件</h3><p class="kb-meta">分類: 構成ファイル ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の 構成ファイル で扱う「Send EIF Events 一致確認 一致条件」は、EIF受信側へイベントを送るかどうかを決める構成項目を一致確認の観点で確認する技術項目です。REGEX ブロックとUnmatchLog sample 017を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send EIF Events 一致確認 一致条件</strong></p><p>検証目的: 構成ファイルのSend EIF Events 一致確認 一致条件について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、構成ファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。REGEX ブロックを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app017.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app017.log,/var/log/secure017.log
画面・出力には LogSources= が含まれ、Send EIF Events 一致確認 一致条件の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app017 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app017
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0049"><h3>Send EIF Events 再読込確認 識別値</h3><p class="kb-meta">分類: 構成ファイル ・ 難易度: 上級</p><p>Tivoli Log File Agent 6.3 の 構成ファイル で扱う「Send EIF Events 再読込確認 識別値」は、EIF受信側へイベントを送るかどうかを決める構成項目を再読込確認の観点で確認する技術項目です。LogSources 行とUnmatchLog sample 057を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send EIF Events 再読込確認 識別値</strong></p><p>検証目的: 構成ファイルのSend EIF Events 再読込確認 識別値について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、構成ファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。LogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app057.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app057.log,/var/log/secure057.log
画面・出力には LogSources= が含まれ、Send EIF Events 再読込確認 識別値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app057 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app057
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0050"><h3>itmcmd config 設定確認 出力見出し</h3><p class="kb-meta">分類: 構成ファイル ・ 難易度: 初級</p><p>Tivoli Log File Agent 6.3 の 構成ファイル で扱う「itmcmd config 設定確認 出力見出し」は、UNIX で Log File Agent を対話構成するコマンドを設定確認の観点で確認する技術項目です。RegexLogSources 行とLogSources 009を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd config 設定確認 出力見出し</strong></p><p>検証目的: 構成ファイルのitmcmd config 設定確認 出力見出しについて、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、構成ファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。RegexLogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app009.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app009.log,/var/log/secure009.log
画面・出力には LogSources= が含まれ、itmcmd config 設定確認 出力見出しの証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app009 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app009
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0051"><h3>itmcmd config 転送確認 統計値</h3><p class="kb-meta">分類: 構成ファイル ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の 構成ファイル で扱う「itmcmd config 転送確認 統計値」は、UNIX で Log File Agent を対話構成するコマンドを転送確認の観点で確認する技術項目です。itmcmd agent 出力とLogSources 049を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd config 転送確認 統計値</strong></p><p>検証目的: 構成ファイルのitmcmd config 転送確認 統計値について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、構成ファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。itmcmd agent 出力を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app049.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app049.log,/var/log/secure049.log
画面・出力には LogSources= が含まれ、itmcmd config 転送確認 統計値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app049 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app049
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0052"><h3>slot mapping 除外確認 表形式</h3><p class="kb-meta">分類: 構成ファイル ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の 構成ファイル で扱う「slot mapping 除外確認 表形式」は、正規表現で捕捉した値をイベント属性へ割り当てる定義を除外確認の観点で確認する技術項目です。END 行とRegexLogSources profile 025を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>slot mapping 除外確認 表形式</strong></p><p>検証目的: 構成ファイルのslot mapping 除外確認 表形式について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、構成ファイルの対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd config -A lo
→ Enter を押す
［画面・出力］
Agent configuration: lo
Configuration file path accepted
Format file path accepted
画面・出力には Agent が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。END 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^LogSources&#x27; app025.conf
→ Enter を押す
［画面・出力］
LogSources=/var/log/app025.log,/var/log/secure025.log
画面・出力には LogSources= が含まれ、slot mapping 除外確認 表形式の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; itmcmd agent -o app025 start lo
→ Enter を押す
［画面・出力］
Starting Tivoli Log File Agent instance app025
Agent lo started
画面・出力には Starting が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の Agent が画面・出力に表示されること
② ステップ2 の LogSources= が画面・出力に表示されること
③ ステップ3 の Starting が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


## 正規表現


<section class="kb-item" id="c31-i0053"><h3>REGEX 証跡確認 復旧手掛かり</h3><p class="kb-meta">分類: 正規表現 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の 正規表現 で扱う「REGEX 証跡確認 復旧手掛かり」は、新しい正規表現形式のフォーマット仕様を開始するキーワードを証跡確認の観点で確認する技術項目です。RegexLogSources 行とLogSources 044を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REGEX 証跡確認 復旧手掛かり</strong></p><p>検証目的: 正規表現のREGEX 証跡確認 復旧手掛かりについて、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、正規表現の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app044.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。RegexLogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app044.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、REGEX 証跡確認 復旧手掛かりの証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app044.fmt
→ Enter を押す
［画面・出力］
File: app044.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0054"><h3>REGEX 起動確認 属性確認</h3><p class="kb-meta">分類: 正規表現 ・ 難易度: 初級</p><p>Tivoli Log File Agent 6.3 の 正規表現 で扱う「REGEX 起動確認 属性確認」は、新しい正規表現形式のフォーマット仕様を開始するキーワードを起動確認の観点で確認する技術項目です。END 行とLogSources 004を同じ記録で見比べることで、インスタンス名の誤指定を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>REGEX 起動確認 属性確認</strong></p><p>検証目的: 正規表現のREGEX 起動確認 属性確認について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、正規表現の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app004.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。END 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app004.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、REGEX 起動確認 属性確認の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、インスタンス名の誤指定を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app004.fmt
→ Enter を押す
［画面・出力］
File: app004.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0055"><h3>RegexLogSources 設定確認 詳細表示</h3><p class="kb-meta">分類: 正規表現 ・ 難易度: 上級</p><p>Tivoli Log File Agent 6.3 の 正規表現 で扱う「RegexLogSources 設定確認 詳細表示」は、ファイル名に正規表現を使って複数ログを指定する .conf の設定を設定確認の観点で確認する技術項目です。REGEX ブロックとUnmatchLog sample 052を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RegexLogSources 設定確認 詳細表示</strong></p><p>検証目的: 正規表現のRegexLogSources 設定確認 詳細表示について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、正規表現の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app052.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。REGEX ブロックを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app052.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、RegexLogSources 設定確認 詳細表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app052.fmt
→ Enter を押す
［画面・出力］
File: app052.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0056"><h3>RegexLogSources 転送確認 設定値</h3><p class="kb-meta">分類: 正規表現 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の 正規表現 で扱う「RegexLogSources 転送確認 設定値」は、ファイル名に正規表現を使って複数ログを指定する .conf の設定を転送確認の観点で確認する技術項目です。UnmatchLog ファイルとUnmatchLog sample 012を同じ記録で見比べることで、UnmatchLog 未定義を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>RegexLogSources 転送確認 設定値</strong></p><p>検証目的: 正規表現のRegexLogSources 転送確認 設定値について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、正規表現の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app012.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。UnmatchLog ファイルを読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app012.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、RegexLogSources 転送確認 設定値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、UnmatchLog 未定義を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app012.fmt
→ Enter を押す
［画面・出力］
File: app012.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0057"><h3>Send ITM Events 再読込確認 ページング状態</h3><p class="kb-meta">分類: 正規表現 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の 正規表現 で扱う「Send ITM Events 再読込確認 ページング状態」は、Tivoli Enterprise Monitoring Server へイベントを送るかどうかを決める構成項目を再読込確認の観点で確認する技術項目です。itmcmd agent 出力とitmcmd 028を同じ記録で見比べることで、EIF受信側停止時の滞留を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Send ITM Events 再読込確認 ページング状態</strong></p><p>検証目的: 正規表現のSend ITM Events 再読込確認 ページング状態について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、正規表現の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app028.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。itmcmd agent 出力を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app028.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、Send ITM Events 再読込確認 ページング状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、EIF受信側停止時の滞留を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app028.fmt
→ Enter を押す
［画面・出力］
File: app028.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0058"><h3>UnmatchLog 障害切り分け パス状態</h3><p class="kb-meta">分類: 正規表現 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の 正規表現 で扱う「UnmatchLog 障害切り分け パス状態」は、どの仕様にも一致しないログ行を保存する .conf の設定を障害切り分けの観点で確認する技術項目です。LogSources 行とREGEX class 036を同じ記録で見比べることで、正規表現の過剰一致を名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>UnmatchLog 障害切り分け パス状態</strong></p><p>検証目的: 正規表現のUnmatchLog 障害切り分け パス状態について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、正規表現の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app036.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。LogSources 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app036.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、UnmatchLog 障害切り分け パス状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、正規表現の過剰一致を切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app036.fmt
→ Enter を押す
［画面・出力］
File: app036.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0059"><h3>itmcmd agent start 設定確認 保存場所</h3><p class="kb-meta">分類: 正規表現 ・ 難易度: 上級</p><p>Tivoli Log File Agent 6.3 の 正規表現 で扱う「itmcmd agent start 設定確認 保存場所」は、構成済みインスタンスを起動するコマンドを設定確認の観点で確認する技術項目です。END 行とRegexLogSources profile 060を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd agent start 設定確認 保存場所</strong></p><p>検証目的: 正規表現のitmcmd agent start 設定確認 保存場所について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、正規表現の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app060.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。END 行を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app060.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、itmcmd agent start 設定確認 保存場所の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app060.fmt
→ Enter を押す
［画面・出力］
File: app060.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>


<section class="kb-item" id="c31-i0060"><h3>itmcmd agent start 転送確認 受信先</h3><p class="kb-meta">分類: 正規表現 ・ 難易度: 中級</p><p>Tivoli Log File Agent 6.3 の 正規表現 で扱う「itmcmd agent start 転送確認 受信先」は、構成済みインスタンスを起動するコマンドを転送確認の観点で確認する技術項目です。Send EIF Events 値とRegexLogSources profile 020を同じ記録で見比べることで、監視対象ログの指定漏れを名前だけの確認にせず、処理結果・設定値・出力見出しの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>itmcmd agent start 転送確認 受信先</strong></p><p>検証目的: 正規表現のitmcmd agent start 転送確認 受信先について、Tivoli Log File Agent 6.3の資料に出る操作名・設定名・出力形式を机上で照合する。</p><p>前提条件: Tivoli Log File Agent 6.3の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、構成ファイル、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はTivoli Log File Agent 6.3の入力画面です。COMMAND ===&gt; に最初の確認操作を入れ、正規表現の対象へ進みます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^NumEventsToCatchUp&#x27; app020.conf
→ Enter を押す
［画面・出力］
NumEventsToCatchUp=-1
画面・出力には NumEventsToCatchUp=-1 が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はTivoli Log File Agent 6.3の確認画面です。Send EIF Events 値を読むため、対象名を含む操作を入力します。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; grep &#x27;^PollInterval&#x27; app020.conf
→ Enter を押す
［画面・出力］
PollInterval=5
画面・出力には PollInterval=5 が含まれ、itmcmd agent start 転送確認 受信先の証跡を確認できます。
――――
■ ステップ 3
現在の画面はTivoli Log File Agent 6.3の詳細確認画面です。表示名とメッセージ形式を照合し、監視対象ログの指定漏れを切り分けます。
［操作（入力）］
Tivoli Log File Agent 6.3 操作画面
COMMAND ===&gt; stat app020.fmt
→ Enter を押す
［画面・出力］
File: app020.fmt
Modify: 2026-07-14 09:15:00
Format file timestamp checked for dynamic reload
画面・出力には File が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の NumEventsToCatchUp=-1 が画面・出力に表示されること
② ステップ2 の PollInterval=5 が画面・出力に表示されること
③ ステップ3 の File が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: LFA63_UserGuide_EN / ITM63_InstallGuide_EN / Tivoli Log File Agent configuration and format file reference</p></div></details></section>
