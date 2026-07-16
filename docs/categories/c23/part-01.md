---
search:
  exclude: true
---

# Netcool/OMNIbus V8.1 — 詳細 (1/1)

[← Netcool/OMNIbus V8.1 の概要へ戻る](index.md)


## Event List


<section class="kb-item" id="c23-i0001"><h3>accelerated events channel フィールド照合 統計値</h3><p class="kb-meta">分類: Event List ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Event List で扱う「accelerated events channel フィールド照合 統計値」は、特定の問題アラートを階層間で速く伝搬する仕組みをフィールド照合の観点で確認する技術項目です。accelerated_inserts triggerとalerts.status row 030を同じ記録で見比べることで、Identifier 生成不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>accelerated events channel フィールド照合 統計値</strong></p><p>検証目的: Event Listのaccelerated events channel フィールド照合 統計値について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Event Listの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。accelerated_inserts triggerを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE030:LINKDOWN    5         NODE030
NODE030:RECOVER     2         NODE030
画面・出力には Identifier が含まれ、accelerated events channel フィールド照合 統計値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Identifier 生成不備を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0002"><h3>accelerated events channel ルール確認 管理クラス</h3><p class="kb-meta">分類: Event List ・ 難易度: 上級</p><p>Netcool/OMNIbus V8.1 の Event List で扱う「accelerated events channel ルール確認 管理クラス」は、特定の問題アラートを階層間で速く伝搬する仕組みをルール確認の観点で確認する技術項目です。accelerated_inserts triggerとalerts.status row 050を同じ記録で見比べることで、Identifier 生成不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>accelerated events channel ルール確認 管理クラス</strong></p><p>検証目的: Event Listのaccelerated events channel ルール確認 管理クラスについて、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Event Listの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。accelerated_inserts triggerを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE050:LINKDOWN    5         NODE050
NODE050:RECOVER     2         NODE050
画面・出力には Identifier が含まれ、accelerated events channel ルール確認 管理クラスの証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Identifier 生成不備を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0003"><h3>accelerated events channel 伝搬確認 監査証跡</h3><p class="kb-meta">分類: Event List ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Event List で扱う「accelerated events channel 伝搬確認 監査証跡」は、特定の問題アラートを階層間で速く伝搬する仕組みを伝搬確認の観点で確認する技術項目です。accelerated_inserts triggerとalerts.status row 010を同じ記録で見比べることで、Identifier 生成不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>accelerated events channel 伝搬確認 監査証跡</strong></p><p>検証目的: Event Listのaccelerated events channel 伝搬確認 監査証跡について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Event Listの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。accelerated_inserts triggerを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE010:LINKDOWN    5         NODE010
NODE010:RECOVER     2         NODE010
画面・出力には Identifier が含まれ、accelerated events channel 伝搬確認 監査証跡の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Identifier 生成不備を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0004"><h3>accelerated events channel 状態確認 識別列</h3><p class="kb-meta">分類: Event List ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Event List で扱う「accelerated events channel 状態確認 識別列」は、特定の問題アラートを階層間で速く伝搬する仕組みを状態確認の観点で確認する技術項目です。accelerated_inserts triggerとalerts.status row 020を同じ記録で見比べることで、Identifier 生成不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>accelerated events channel 状態確認 識別列</strong></p><p>検証目的: Event Listのaccelerated events channel 状態確認 識別列について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Event Listの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。accelerated_inserts triggerを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE020:LINKDOWN    5         NODE020
NODE020:RECOVER     2         NODE020
画面・出力には Identifier が含まれ、accelerated events channel 状態確認 識別列の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Identifier 生成不備を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0005"><h3>accelerated events channel 重複排除確認 キュー状態</h3><p class="kb-meta">分類: Event List ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Event List で扱う「accelerated events channel 重複排除確認 キュー状態」は、特定の問題アラートを階層間で速く伝搬する仕組みを重複排除確認の観点で確認する技術項目です。accelerated_inserts triggerとalerts.status row 040を同じ記録で見比べることで、Identifier 生成不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>accelerated events channel 重複排除確認 キュー状態</strong></p><p>検証目的: Event Listのaccelerated events channel 重複排除確認 キュー状態について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Event Listの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。accelerated_inserts triggerを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE040:LINKDOWN    5         NODE040
NODE040:RECOVER     2         NODE040
画面・出力には Identifier が含まれ、accelerated events channel 重複排除確認 キュー状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Identifier 生成不備を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0006"><h3>gateway フィールド照合 キーマップ</h3><p class="kb-meta">分類: Event List ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Event List で扱う「gateway フィールド照合 キーマップ」は、ObjectServer 間または外部システムへイベントを受け渡す連携機能をフィールド照合の観点で確認する技術項目です。accelerated_inserts triggerとalerts.status row 025を同じ記録で見比べることで、Identifier 生成不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>gateway フィールド照合 キーマップ</strong></p><p>検証目的: Event Listのgateway フィールド照合 キーマップについて、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Event Listの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。accelerated_inserts triggerを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE025:LINKDOWN    5         NODE025
NODE025:RECOVER     2         NODE025
画面・出力には Identifier が含まれ、gateway フィールド照合 キーマップの証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Identifier 生成不備を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0007"><h3>gateway ルール確認 スケジュール</h3><p class="kb-meta">分類: Event List ・ 難易度: 上級</p><p>Netcool/OMNIbus V8.1 の Event List で扱う「gateway ルール確認 スケジュール」は、ObjectServer 間または外部システムへイベントを受け渡す連携機能をルール確認の観点で確認する技術項目です。accelerated_inserts triggerとalerts.status row 045を同じ記録で見比べることで、Identifier 生成不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>gateway ルール確認 スケジュール</strong></p><p>検証目的: Event Listのgateway ルール確認 スケジュールについて、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Event Listの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。accelerated_inserts triggerを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE045:LINKDOWN    5         NODE045
NODE045:RECOVER     2         NODE045
画面・出力には Identifier が含まれ、gateway ルール確認 スケジュールの証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Identifier 生成不備を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0008"><h3>gateway 伝搬確認 警告行</h3><p class="kb-meta">分類: Event List ・ 難易度: 初級</p><p>Netcool/OMNIbus V8.1 の Event List で扱う「gateway 伝搬確認 警告行」は、ObjectServer 間または外部システムへイベントを受け渡す連携機能を伝搬確認の観点で確認する技術項目です。accelerated_inserts triggerとalerts.status row 005を同じ記録で見比べることで、Identifier 生成不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>gateway 伝搬確認 警告行</strong></p><p>検証目的: Event Listのgateway 伝搬確認 警告行について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Event Listの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。accelerated_inserts triggerを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE005:LINKDOWN    5         NODE005
NODE005:RECOVER     2         NODE005
画面・出力には Identifier が含まれ、gateway 伝搬確認 警告行の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Identifier 生成不備を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0009"><h3>gateway 状態確認 接続状態</h3><p class="kb-meta">分類: Event List ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Event List で扱う「gateway 状態確認 接続状態」は、ObjectServer 間または外部システムへイベントを受け渡す連携機能を状態確認の観点で確認する技術項目です。accelerated_inserts triggerとalerts.status row 015を同じ記録で見比べることで、Identifier 生成不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>gateway 状態確認 接続状態</strong></p><p>検証目的: Event Listのgateway 状態確認 接続状態について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Event Listの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。accelerated_inserts triggerを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE015:LINKDOWN    5         NODE015
NODE015:RECOVER     2         NODE015
画面・出力には Identifier が含まれ、gateway 状態確認 接続状態の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Identifier 生成不備を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0010"><h3>gateway 重複排除確認 取得間隔</h3><p class="kb-meta">分類: Event List ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Event List で扱う「gateway 重複排除確認 取得間隔」は、ObjectServer 間または外部システムへイベントを受け渡す連携機能を重複排除確認の観点で確認する技術項目です。accelerated_inserts triggerとalerts.status row 035を同じ記録で見比べることで、Identifier 生成不備を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>gateway 重複排除確認 取得間隔</strong></p><p>検証目的: Event Listのgateway 重複排除確認 取得間隔について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Event Listの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。accelerated_inserts triggerを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE035:LINKDOWN    5         NODE035
NODE035:RECOVER     2         NODE035
画面・出力には Identifier が含まれ、gateway 重複排除確認 取得間隔の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Identifier 生成不備を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


## Gateway


<section class="kb-item" id="c23-i0011"><h3>Identifier フィールド照合 復元前提</h3><p class="kb-meta">分類: Gateway ・ 難易度: 上級</p><p>Netcool/OMNIbus V8.1 の Gateway で扱う「Identifier フィールド照合 復元前提」は、問題発生源を一意に示し重複排除に使われるフィールドをフィールド照合の観点で確認する技術項目です。probe rules fileとNode NODE043を同じ記録で見比べることで、probe rules file の誤変換を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Identifier フィールド照合 復元前提</strong></p><p>検証目的: GatewayのIdentifier フィールド照合 復元前提について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Gatewayの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。probe rules fileを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE043:LINKDOWN    5         NODE043
NODE043:RECOVER     2         NODE043
画面・出力には Identifier が含まれ、Identifier フィールド照合 復元前提の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、probe rules file の誤変換を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0012"><h3>Identifier ルール確認 承認履歴</h3><p class="kb-meta">分類: Gateway ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Gateway で扱う「Identifier ルール確認 承認履歴」は、問題発生源を一意に示し重複排除に使われるフィールドをルール確認の観点で確認する技術項目です。probe rules fileとNode NODE013を同じ記録で見比べることで、probe rules file の誤変換を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Identifier ルール確認 承認履歴</strong></p><p>検証目的: GatewayのIdentifier ルール確認 承認履歴について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Gatewayの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。probe rules fileを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE013:LINKDOWN    5         NODE013
NODE013:RECOVER     2         NODE013
画面・出力には Identifier が含まれ、Identifier ルール確認 承認履歴の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、probe rules file の誤変換を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0013"><h3>Identifier 伝搬確認 文字変換</h3><p class="kb-meta">分類: Gateway ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Gateway で扱う「Identifier 伝搬確認 文字変換」は、問題発生源を一意に示し重複排除に使われるフィールドを伝搬確認の観点で確認する技術項目です。probe rules fileとNode NODE023を同じ記録で見比べることで、probe rules file の誤変換を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Identifier 伝搬確認 文字変換</strong></p><p>検証目的: GatewayのIdentifier 伝搬確認 文字変換について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Gatewayの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。probe rules fileを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE023:LINKDOWN    5         NODE023
NODE023:RECOVER     2         NODE023
画面・出力には Identifier が含まれ、Identifier 伝搬確認 文字変換の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、probe rules file の誤変換を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0014"><h3>Identifier 状態確認 再同期判断</h3><p class="kb-meta">分類: Gateway ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Gateway で扱う「Identifier 状態確認 再同期判断」は、問題発生源を一意に示し重複排除に使われるフィールドを状態確認の観点で確認する技術項目です。probe rules fileとNode NODE033を同じ記録で見比べることで、probe rules file の誤変換を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Identifier 状態確認 再同期判断</strong></p><p>検証目的: GatewayのIdentifier 状態確認 再同期判断について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Gatewayの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。probe rules fileを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE033:LINKDOWN    5         NODE033
NODE033:RECOVER     2         NODE033
画面・出力には Identifier が含まれ、Identifier 状態確認 再同期判断の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、probe rules file の誤変換を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0015"><h3>Identifier 重複排除確認 接続先</h3><p class="kb-meta">分類: Gateway ・ 難易度: 初級</p><p>Netcool/OMNIbus V8.1 の Gateway で扱う「Identifier 重複排除確認 接続先」は、問題発生源を一意に示し重複排除に使われるフィールドを重複排除確認の観点で確認する技術項目です。probe rules fileとNode NODE003を同じ記録で見比べることで、probe rules file の誤変換を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>Identifier 重複排除確認 接続先</strong></p><p>検証目的: GatewayのIdentifier 重複排除確認 接続先について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Gatewayの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。probe rules fileを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE003:LINKDOWN    5         NODE003
NODE003:RECOVER     2         NODE003
画面・出力には Identifier が含まれ、Identifier 重複排除確認 接続先の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、probe rules file の誤変換を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0016"><h3>event list フィールド照合 プール宛先</h3><p class="kb-meta">分類: Gateway ・ 難易度: 上級</p><p>Netcool/OMNIbus V8.1 の Gateway で扱う「event list フィールド照合 プール宛先」は、運用者がアラートを確認し詳細や履歴を追うクライアント画面をフィールド照合の観点で確認する技術項目です。probe rules fileとNode NODE048を同じ記録で見比べることで、probe rules file の誤変換を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>event list フィールド照合 プール宛先</strong></p><p>検証目的: Gatewayのevent list フィールド照合 プール宛先について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Gatewayの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。probe rules fileを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE048:LINKDOWN    5         NODE048
NODE048:RECOVER     2         NODE048
画面・出力には Identifier が含まれ、event list フィールド照合 プール宛先の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、probe rules file の誤変換を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0017"><h3>event list ルール確認 集約結果</h3><p class="kb-meta">分類: Gateway ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Gateway で扱う「event list ルール確認 集約結果」は、運用者がアラートを確認し詳細や履歴を追うクライアント画面をルール確認の観点で確認する技術項目です。probe rules fileとNode NODE018を同じ記録で見比べることで、probe rules file の誤変換を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>event list ルール確認 集約結果</strong></p><p>検証目的: Gatewayのevent list ルール確認 集約結果について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Gatewayの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。probe rules fileを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE018:LINKDOWN    5         NODE018
NODE018:RECOVER     2         NODE018
画面・出力には Identifier が含まれ、event list ルール確認 集約結果の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、probe rules file の誤変換を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0018"><h3>event list 伝搬確認 出力見出し</h3><p class="kb-meta">分類: Gateway ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Gateway で扱う「event list 伝搬確認 出力見出し」は、運用者がアラートを確認し詳細や履歴を追うクライアント画面を伝搬確認の観点で確認する技術項目です。probe rules fileとNode NODE028を同じ記録で見比べることで、probe rules file の誤変換を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>event list 伝搬確認 出力見出し</strong></p><p>検証目的: Gatewayのevent list 伝搬確認 出力見出しについて、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Gatewayの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。probe rules fileを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE028:LINKDOWN    5         NODE028
NODE028:RECOVER     2         NODE028
画面・出力には Identifier が含まれ、event list 伝搬確認 出力見出しの証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、probe rules file の誤変換を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0019"><h3>event list 状態確認 承認待ち</h3><p class="kb-meta">分類: Gateway ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Gateway で扱う「event list 状態確認 承認待ち」は、運用者がアラートを確認し詳細や履歴を追うクライアント画面を状態確認の観点で確認する技術項目です。probe rules fileとNode NODE038を同じ記録で見比べることで、probe rules file の誤変換を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>event list 状態確認 承認待ち</strong></p><p>検証目的: Gatewayのevent list 状態確認 承認待ちについて、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Gatewayの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。probe rules fileを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE038:LINKDOWN    5         NODE038
NODE038:RECOVER     2         NODE038
画面・出力には Identifier が含まれ、event list 状態確認 承認待ちの証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、probe rules file の誤変換を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0020"><h3>event list 重複排除確認 差分確認</h3><p class="kb-meta">分類: Gateway ・ 難易度: 初級</p><p>Netcool/OMNIbus V8.1 の Gateway で扱う「event list 重複排除確認 差分確認」は、運用者がアラートを確認し詳細や履歴を追うクライアント画面を重複排除確認の観点で確認する技術項目です。probe rules fileとNode NODE008を同じ記録で見比べることで、probe rules file の誤変換を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>event list 重複排除確認 差分確認</strong></p><p>検証目的: Gatewayのevent list 重複排除確認 差分確認について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Gatewayの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。probe rules fileを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE008:LINKDOWN    5         NODE008
NODE008:RECOVER     2         NODE008
画面・出力には Identifier が含まれ、event list 重複排除確認 差分確認の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、probe rules file の誤変換を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


## ObjectServer


<section class="kb-item" id="c23-i0021"><h3>IDUC フィールド照合 構成配布</h3><p class="kb-meta">分類: ObjectServer ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の ObjectServer で扱う「IDUC フィールド照合 構成配布」は、デスクトップクライアントへ更新を配布する ObjectServer の更新機構をフィールド照合の観点で確認する技術項目です。alerts.status の IdentifierとIdentifier NODE016を同じ記録で見比べることで、Severity 変換漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IDUC フィールド照合 構成配布</strong></p><p>検証目的: ObjectServerのIDUC フィールド照合 構成配布について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ObjectServerの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。alerts.status の Identifierを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE016:LINKDOWN    5         NODE016
NODE016:RECOVER     2         NODE016
画面・出力には Identifier が含まれ、IDUC フィールド照合 構成配布の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Severity 変換漏れを切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0022"><h3>IDUC ルール確認 例外記録</h3><p class="kb-meta">分類: ObjectServer ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の ObjectServer で扱う「IDUC ルール確認 例外記録」は、デスクトップクライアントへ更新を配布する ObjectServer の更新機構をルール確認の観点で確認する技術項目です。alerts.status の IdentifierとIdentifier NODE036を同じ記録で見比べることで、Severity 変換漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IDUC ルール確認 例外記録</strong></p><p>検証目的: ObjectServerのIDUC ルール確認 例外記録について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ObjectServerの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。alerts.status の Identifierを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE036:LINKDOWN    5         NODE036
NODE036:RECOVER     2         NODE036
画面・出力には Identifier が含まれ、IDUC ルール確認 例外記録の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Severity 変換漏れを切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0023"><h3>IDUC 伝搬確認 活動ログ</h3><p class="kb-meta">分類: ObjectServer ・ 難易度: 上級</p><p>Netcool/OMNIbus V8.1 の ObjectServer で扱う「IDUC 伝搬確認 活動ログ」は、デスクトップクライアントへ更新を配布する ObjectServer の更新機構を伝搬確認の観点で確認する技術項目です。alerts.status の IdentifierとIdentifier NODE046を同じ記録で見比べることで、Severity 変換漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IDUC 伝搬確認 活動ログ</strong></p><p>検証目的: ObjectServerのIDUC 伝搬確認 活動ログについて、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ObjectServerの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。alerts.status の Identifierを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE046:LINKDOWN    5         NODE046
NODE046:RECOVER     2         NODE046
画面・出力には Identifier が含まれ、IDUC 伝搬確認 活動ログの証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Severity 変換漏れを切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0024"><h3>IDUC 状態確認 応答行</h3><p class="kb-meta">分類: ObjectServer ・ 難易度: 初級</p><p>Netcool/OMNIbus V8.1 の ObjectServer で扱う「IDUC 状態確認 応答行」は、デスクトップクライアントへ更新を配布する ObjectServer の更新機構を状態確認の観点で確認する技術項目です。alerts.status の IdentifierとIdentifier NODE006を同じ記録で見比べることで、Severity 変換漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IDUC 状態確認 応答行</strong></p><p>検証目的: ObjectServerのIDUC 状態確認 応答行について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ObjectServerの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。alerts.status の Identifierを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE006:LINKDOWN    5         NODE006
NODE006:RECOVER     2         NODE006
画面・出力には Identifier が含まれ、IDUC 状態確認 応答行の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Severity 変換漏れを切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0025"><h3>IDUC 重複排除確認 保存場所</h3><p class="kb-meta">分類: ObjectServer ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の ObjectServer で扱う「IDUC 重複排除確認 保存場所」は、デスクトップクライアントへ更新を配布する ObjectServer の更新機構を重複排除確認の観点で確認する技術項目です。alerts.status の IdentifierとIdentifier NODE026を同じ記録で見比べることで、Severity 変換漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>IDUC 重複排除確認 保存場所</strong></p><p>検証目的: ObjectServerのIDUC 重複排除確認 保存場所について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ObjectServerの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。alerts.status の Identifierを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE026:LINKDOWN    5         NODE026
NODE026:RECOVER     2         NODE026
画面・出力には Identifier が含まれ、IDUC 重複排除確認 保存場所の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Severity 変換漏れを切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0026"><h3>ObjectServer フィールド照合 保持期間</h3><p class="kb-meta">分類: ObjectServer ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の ObjectServer で扱う「ObjectServer フィールド照合 保持期間」は、アラート情報を保存し管理する Netcool/OMNIbus の中核サーバーをフィールド照合の観点で確認する技術項目です。alerts.status の IdentifierとIdentifier NODE011を同じ記録で見比べることで、Severity 変換漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ObjectServer フィールド照合 保持期間</strong></p><p>検証目的: ObjectServerのObjectServer フィールド照合 保持期間について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ObjectServerの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。alerts.status の Identifierを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE011:LINKDOWN    5         NODE011
NODE011:RECOVER     2         NODE011
画面・出力には Identifier が含まれ、ObjectServer フィールド照合 保持期間の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Severity 変換漏れを切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0027"><h3>ObjectServer ルール確認 遅延表示</h3><p class="kb-meta">分類: ObjectServer ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の ObjectServer で扱う「ObjectServer ルール確認 遅延表示」は、アラート情報を保存し管理する Netcool/OMNIbus の中核サーバーをルール確認の観点で確認する技術項目です。alerts.status の IdentifierとIdentifier NODE031を同じ記録で見比べることで、Severity 変換漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ObjectServer ルール確認 遅延表示</strong></p><p>検証目的: ObjectServerのObjectServer ルール確認 遅延表示について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ObjectServerの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。alerts.status の Identifierを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE031:LINKDOWN    5         NODE031
NODE031:RECOVER     2         NODE031
画面・出力には Identifier が含まれ、ObjectServer ルール確認 遅延表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Severity 変換漏れを切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0028"><h3>ObjectServer 伝搬確認 容量表示</h3><p class="kb-meta">分類: ObjectServer ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の ObjectServer で扱う「ObjectServer 伝搬確認 容量表示」は、アラート情報を保存し管理する Netcool/OMNIbus の中核サーバーを伝搬確認の観点で確認する技術項目です。alerts.status の IdentifierとIdentifier NODE041を同じ記録で見比べることで、Severity 変換漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ObjectServer 伝搬確認 容量表示</strong></p><p>検証目的: ObjectServerのObjectServer 伝搬確認 容量表示について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ObjectServerの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。alerts.status の Identifierを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE041:LINKDOWN    5         NODE041
NODE041:RECOVER     2         NODE041
画面・出力には Identifier が含まれ、ObjectServer 伝搬確認 容量表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Severity 変換漏れを切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0029"><h3>ObjectServer 状態確認 開始時刻</h3><p class="kb-meta">分類: ObjectServer ・ 難易度: 初級</p><p>Netcool/OMNIbus V8.1 の ObjectServer で扱う「ObjectServer 状態確認 開始時刻」は、アラート情報を保存し管理する Netcool/OMNIbus の中核サーバーを状態確認の観点で確認する技術項目です。alerts.status の IdentifierとIdentifier NODE001を同じ記録で見比べることで、Severity 変換漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ObjectServer 状態確認 開始時刻</strong></p><p>検証目的: ObjectServerのObjectServer 状態確認 開始時刻について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ObjectServerの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。alerts.status の Identifierを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE001:LINKDOWN    5         NODE001
NODE001:RECOVER     2         NODE001
画面・出力には Identifier が含まれ、ObjectServer 状態確認 開始時刻の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Severity 変換漏れを切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0030"><h3>ObjectServer 重複排除確認 保護設定</h3><p class="kb-meta">分類: ObjectServer ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の ObjectServer で扱う「ObjectServer 重複排除確認 保護設定」は、アラート情報を保存し管理する Netcool/OMNIbus の中核サーバーを重複排除確認の観点で確認する技術項目です。alerts.status の IdentifierとIdentifier NODE021を同じ記録で見比べることで、Severity 変換漏れを名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>ObjectServer 重複排除確認 保護設定</strong></p><p>検証目的: ObjectServerのObjectServer 重複排除確認 保護設定について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、ObjectServerの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。alerts.status の Identifierを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE021:LINKDOWN    5         NODE021
NODE021:RECOVER     2         NODE021
画面・出力には Identifier が含まれ、ObjectServer 重複排除確認 保護設定の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、Severity 変換漏れを切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


## Probe


<section class="kb-item" id="c23-i0031"><h3>alerts.status フィールド照合 停止時刻</h3><p class="kb-meta">分類: Probe ・ 難易度: 初級</p><p>Netcool/OMNIbus V8.1 の Probe で扱う「alerts.status フィールド照合 停止時刻」は、各アラートを行として保持する ObjectServer の主要テーブルをフィールド照合の観点で確認する技術項目です。Severity フィールドとSeverity 2を同じ記録で見比べることで、gateway 伝搬遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alerts.status フィールド照合 停止時刻</strong></p><p>検証目的: Probeのalerts.status フィールド照合 停止時刻について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Probeの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。Severity フィールドを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE002:LINKDOWN    5         NODE002
NODE002:RECOVER     2         NODE002
画面・出力には Identifier が含まれ、alerts.status フィールド照合 停止時刻の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、gateway 伝搬遅延を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0032"><h3>alerts.status ルール確認 転送条件</h3><p class="kb-meta">分類: Probe ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Probe で扱う「alerts.status ルール確認 転送条件」は、各アラートを行として保持する ObjectServer の主要テーブルをルール確認の観点で確認する技術項目です。Severity フィールドとSeverity 2を同じ記録で見比べることで、gateway 伝搬遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alerts.status ルール確認 転送条件</strong></p><p>検証目的: Probeのalerts.status ルール確認 転送条件について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Probeの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。Severity フィールドを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE022:LINKDOWN    5         NODE022
NODE022:RECOVER     2         NODE022
画面・出力には Identifier が含まれ、alerts.status ルール確認 転送条件の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、gateway 伝搬遅延を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0033"><h3>alerts.status 伝搬確認 初期同期</h3><p class="kb-meta">分類: Probe ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Probe で扱う「alerts.status 伝搬確認 初期同期」は、各アラートを行として保持する ObjectServer の主要テーブルを伝搬確認の観点で確認する技術項目です。Severity フィールドとSeverity 2を同じ記録で見比べることで、gateway 伝搬遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alerts.status 伝搬確認 初期同期</strong></p><p>検証目的: Probeのalerts.status 伝搬確認 初期同期について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Probeの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。Severity フィールドを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE032:LINKDOWN    5         NODE032
NODE032:RECOVER     2         NODE032
画面・出力には Identifier が含まれ、alerts.status 伝搬確認 初期同期の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、gateway 伝搬遅延を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0034"><h3>alerts.status 状態確認 期限切れ</h3><p class="kb-meta">分類: Probe ・ 難易度: 上級</p><p>Netcool/OMNIbus V8.1 の Probe で扱う「alerts.status 状態確認 期限切れ」は、各アラートを行として保持する ObjectServer の主要テーブルを状態確認の観点で確認する技術項目です。Severity フィールドとSeverity 2を同じ記録で見比べることで、gateway 伝搬遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alerts.status 状態確認 期限切れ</strong></p><p>検証目的: Probeのalerts.status 状態確認 期限切れについて、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Probeの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。Severity フィールドを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE042:LINKDOWN    5         NODE042
NODE042:RECOVER     2         NODE042
画面・出力には Identifier が含まれ、alerts.status 状態確認 期限切れの証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、gateway 伝搬遅延を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0035"><h3>alerts.status 重複排除確認 宛先定義</h3><p class="kb-meta">分類: Probe ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Probe で扱う「alerts.status 重複排除確認 宛先定義」は、各アラートを行として保持する ObjectServer の主要テーブルを重複排除確認の観点で確認する技術項目です。Severity フィールドとSeverity 2を同じ記録で見比べることで、gateway 伝搬遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>alerts.status 重複排除確認 宛先定義</strong></p><p>検証目的: Probeのalerts.status 重複排除確認 宛先定義について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Probeの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。Severity フィールドを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE012:LINKDOWN    5         NODE012
NODE012:RECOVER     2         NODE012
画面・出力には Identifier が含まれ、alerts.status 重複排除確認 宛先定義の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、gateway 伝搬遅延を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0036"><h3>trigger フィールド照合 詳細表示</h3><p class="kb-meta">分類: Probe ・ 難易度: 初級</p><p>Netcool/OMNIbus V8.1 の Probe で扱う「trigger フィールド照合 詳細表示」は、ObjectServer 内でイベントに応じて実行される自動処理をフィールド照合の観点で確認する技術項目です。Severity フィールドとSeverity 2を同じ記録で見比べることで、gateway 伝搬遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>trigger フィールド照合 詳細表示</strong></p><p>検証目的: Probeのtrigger フィールド照合 詳細表示について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Probeの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。Severity フィールドを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE007:LINKDOWN    5         NODE007
NODE007:RECOVER     2         NODE007
画面・出力には Identifier が含まれ、trigger フィールド照合 詳細表示の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、gateway 伝搬遅延を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0037"><h3>trigger ルール確認 入力欄</h3><p class="kb-meta">分類: Probe ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Probe で扱う「trigger ルール確認 入力欄」は、ObjectServer 内でイベントに応じて実行される自動処理をルール確認の観点で確認する技術項目です。Severity フィールドとSeverity 2を同じ記録で見比べることで、gateway 伝搬遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>trigger ルール確認 入力欄</strong></p><p>検証目的: Probeのtrigger ルール確認 入力欄について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Probeの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。Severity フィールドを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE027:LINKDOWN    5         NODE027
NODE027:RECOVER     2         NODE027
画面・出力には Identifier が含まれ、trigger ルール確認 入力欄の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、gateway 伝搬遅延を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0038"><h3>trigger 伝搬確認 サインオフ</h3><p class="kb-meta">分類: Probe ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Probe で扱う「trigger 伝搬確認 サインオフ」は、ObjectServer 内でイベントに応じて実行される自動処理を伝搬確認の観点で確認する技術項目です。Severity フィールドとSeverity 2を同じ記録で見比べることで、gateway 伝搬遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>trigger 伝搬確認 サインオフ</strong></p><p>検証目的: Probeのtrigger 伝搬確認 サインオフについて、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Probeの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。Severity フィールドを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE037:LINKDOWN    5         NODE037
NODE037:RECOVER     2         NODE037
画面・出力には Identifier が含まれ、trigger 伝搬確認 サインオフの証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、gateway 伝搬遅延を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0039"><h3>trigger 状態確認 ノード割当</h3><p class="kb-meta">分類: Probe ・ 難易度: 上級</p><p>Netcool/OMNIbus V8.1 の Probe で扱う「trigger 状態確認 ノード割当」は、ObjectServer 内でイベントに応じて実行される自動処理を状態確認の観点で確認する技術項目です。Severity フィールドとSeverity 2を同じ記録で見比べることで、gateway 伝搬遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>trigger 状態確認 ノード割当</strong></p><p>検証目的: Probeのtrigger 状態確認 ノード割当について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Probeの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。Severity フィールドを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE047:LINKDOWN    5         NODE047
NODE047:RECOVER     2         NODE047
画面・出力には Identifier が含まれ、trigger 状態確認 ノード割当の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、gateway 伝搬遅延を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0040"><h3>trigger 重複排除確認 同期範囲</h3><p class="kb-meta">分類: Probe ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の Probe で扱う「trigger 重複排除確認 同期範囲」は、ObjectServer 内でイベントに応じて実行される自動処理を重複排除確認の観点で確認する技術項目です。Severity フィールドとSeverity 2を同じ記録で見比べることで、gateway 伝搬遅延を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>trigger 重複排除確認 同期範囲</strong></p><p>検証目的: Probeのtrigger 重複排除確認 同期範囲について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、Probeの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。Severity フィールドを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE017:LINKDOWN    5         NODE017
NODE017:RECOVER     2         NODE017
画面・出力には Identifier が含まれ、trigger 重複排除確認 同期範囲の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、gateway 伝搬遅延を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


## alerts status table


<section class="kb-item" id="c23-i0041"><h3>probe rules file フィールド照合 適用位置</h3><p class="kb-meta">分類: alerts status table ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の alerts status table で扱う「probe rules file フィールド照合 適用位置」は、イベント要素を alert fields へ変換するプローブの規則ファイルをフィールド照合の観点で確認する技術項目です。ObjectServer propertiesとNCOMS 034を同じ記録で見比べることで、secure mode の接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>probe rules file フィールド照合 適用位置</strong></p><p>検証目的: alerts status tableのprobe rules file フィールド照合 適用位置について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、alerts status tableの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。ObjectServer propertiesを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE034:LINKDOWN    5         NODE034
NODE034:RECOVER     2         NODE034
画面・出力には Identifier が含まれ、probe rules file フィールド照合 適用位置の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、secure mode の接続失敗を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0042"><h3>probe rules file ルール確認 対象表</h3><p class="kb-meta">分類: alerts status table ・ 難易度: 初級</p><p>Netcool/OMNIbus V8.1 の alerts status table で扱う「probe rules file ルール確認 対象表」は、イベント要素を alert fields へ変換するプローブの規則ファイルをルール確認の観点で確認する技術項目です。ObjectServer propertiesとNCOMS 004を同じ記録で見比べることで、secure mode の接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>probe rules file ルール確認 対象表</strong></p><p>検証目的: alerts status tableのprobe rules file ルール確認 対象表について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、alerts status tableの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。ObjectServer propertiesを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE004:LINKDOWN    5         NODE004
NODE004:RECOVER     2         NODE004
画面・出力には Identifier が含まれ、probe rules file ルール確認 対象表の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、secure mode の接続失敗を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0043"><h3>probe rules file 伝搬確認 実行結果</h3><p class="kb-meta">分類: alerts status table ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の alerts status table で扱う「probe rules file 伝搬確認 実行結果」は、イベント要素を alert fields へ変換するプローブの規則ファイルを伝搬確認の観点で確認する技術項目です。ObjectServer propertiesとNCOMS 014を同じ記録で見比べることで、secure mode の接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>probe rules file 伝搬確認 実行結果</strong></p><p>検証目的: alerts status tableのprobe rules file 伝搬確認 実行結果について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、alerts status tableの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。ObjectServer propertiesを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE014:LINKDOWN    5         NODE014
NODE014:RECOVER     2         NODE014
画面・出力には Identifier が含まれ、probe rules file 伝搬確認 実行結果の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、secure mode の接続失敗を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0044"><h3>probe rules file 状態確認 証明書検査</h3><p class="kb-meta">分類: alerts status table ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の alerts status table で扱う「probe rules file 状態確認 証明書検査」は、イベント要素を alert fields へ変換するプローブの規則ファイルを状態確認の観点で確認する技術項目です。ObjectServer propertiesとNCOMS 024を同じ記録で見比べることで、secure mode の接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>probe rules file 状態確認 証明書検査</strong></p><p>検証目的: alerts status tableのprobe rules file 状態確認 証明書検査について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、alerts status tableの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。ObjectServer propertiesを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE024:LINKDOWN    5         NODE024
NODE024:RECOVER     2         NODE024
画面・出力には Identifier が含まれ、probe rules file 状態確認 証明書検査の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、secure mode の接続失敗を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0045"><h3>probe rules file 重複排除確認 回収対象</h3><p class="kb-meta">分類: alerts status table ・ 難易度: 上級</p><p>Netcool/OMNIbus V8.1 の alerts status table で扱う「probe rules file 重複排除確認 回収対象」は、イベント要素を alert fields へ変換するプローブの規則ファイルを重複排除確認の観点で確認する技術項目です。ObjectServer propertiesとNCOMS 044を同じ記録で見比べることで、secure mode の接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>probe rules file 重複排除確認 回収対象</strong></p><p>検証目的: alerts status tableのprobe rules file 重複排除確認 回収対象について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、alerts status tableの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。ObjectServer propertiesを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE044:LINKDOWN    5         NODE044
NODE044:RECOVER     2         NODE044
画面・出力には Identifier が含まれ、probe rules file 重複排除確認 回収対象の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、secure mode の接続失敗を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0046"><h3>secure mode フィールド照合 レビュー結果</h3><p class="kb-meta">分類: alerts status table ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の alerts status table で扱う「secure mode フィールド照合 レビュー結果」は、probe や gateway の接続にユーザー名とパスワードを要求する動作をフィールド照合の観点で確認する技術項目です。ObjectServer propertiesとNCOMS 039を同じ記録で見比べることで、secure mode の接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>secure mode フィールド照合 レビュー結果</strong></p><p>検証目的: alerts status tableのsecure mode フィールド照合 レビュー結果について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、alerts status tableの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。ObjectServer propertiesを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE039:LINKDOWN    5         NODE039
NODE039:RECOVER     2         NODE039
画面・出力には Identifier が含まれ、secure mode フィールド照合 レビュー結果の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、secure mode の接続失敗を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0047"><h3>secure mode ルール確認 復旧手掛かり</h3><p class="kb-meta">分類: alerts status table ・ 難易度: 初級</p><p>Netcool/OMNIbus V8.1 の alerts status table で扱う「secure mode ルール確認 復旧手掛かり」は、probe や gateway の接続にユーザー名とパスワードを要求する動作をルール確認の観点で確認する技術項目です。ObjectServer propertiesとNCOMS 009を同じ記録で見比べることで、secure mode の接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>secure mode ルール確認 復旧手掛かり</strong></p><p>検証目的: alerts status tableのsecure mode ルール確認 復旧手掛かりについて、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、alerts status tableの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。ObjectServer propertiesを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE009:LINKDOWN    5         NODE009
NODE009:RECOVER     2         NODE009
画面・出力には Identifier が含まれ、secure mode ルール確認 復旧手掛かりの証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、secure mode の接続失敗を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0048"><h3>secure mode 伝搬確認 変換規則</h3><p class="kb-meta">分類: alerts status table ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の alerts status table で扱う「secure mode 伝搬確認 変換規則」は、probe や gateway の接続にユーザー名とパスワードを要求する動作を伝搬確認の観点で確認する技術項目です。ObjectServer propertiesとNCOMS 019を同じ記録で見比べることで、secure mode の接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>secure mode 伝搬確認 変換規則</strong></p><p>検証目的: alerts status tableのsecure mode 伝搬確認 変換規則について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、alerts status tableの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。ObjectServer propertiesを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE019:LINKDOWN    5         NODE019
NODE019:RECOVER     2         NODE019
画面・出力には Identifier が含まれ、secure mode 伝搬確認 変換規則の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、secure mode の接続失敗を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0049"><h3>secure mode 状態確認 履歴行</h3><p class="kb-meta">分類: alerts status table ・ 難易度: 中級</p><p>Netcool/OMNIbus V8.1 の alerts status table で扱う「secure mode 状態確認 履歴行」は、probe や gateway の接続にユーザー名とパスワードを要求する動作を状態確認の観点で確認する技術項目です。ObjectServer propertiesとNCOMS 029を同じ記録で見比べることで、secure mode の接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>secure mode 状態確認 履歴行</strong></p><p>検証目的: alerts status tableのsecure mode 状態確認 履歴行について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、alerts status tableの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。ObjectServer propertiesを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE029:LINKDOWN    5         NODE029
NODE029:RECOVER     2         NODE029
画面・出力には Identifier が含まれ、secure mode 状態確認 履歴行の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、secure mode の接続失敗を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>


<section class="kb-item" id="c23-i0050"><h3>secure mode 重複排除確認 ドメイン値</h3><p class="kb-meta">分類: alerts status table ・ 難易度: 上級</p><p>Netcool/OMNIbus V8.1 の alerts status table で扱う「secure mode 重複排除確認 ドメイン値」は、probe や gateway の接続にユーザー名とパスワードを要求する動作を重複排除確認の観点で確認する技術項目です。ObjectServer propertiesとNCOMS 049を同じ記録で見比べることで、secure mode の接続失敗を名前だけの確認にせず、処理結果・表名・メッセージの対応まで追跡します。</p><p class="kb-src"><strong>出典:</strong> Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p><details class="kb-block"><summary>検証手順（1件）</summary><div class="kb-p"><p class="kb-pname"><strong>secure mode 重複排除確認 ドメイン値</strong></p><p>検証目的: alerts status tableのsecure mode 重複排除確認 ドメイン値について、Netcool/OMNIbus V8.1の資料に出る操作名・表名・メッセージ形式を机上で照合する。</p><p>前提条件: Netcool/OMNIbus V8.1の資料確認ができ、対象環境の表示例を机上証跡として記録できる。</p><p>セッション環境: 机上検証。製品資料に記載されたコマンド、メニュー、表名、メッセージ形式を使う。</p><pre class="kb-code">■ ステップ 1
現在の画面はNetcool/OMNIbus V8.1の入力画面です。COMMAND ===&gt; または ?S に最初の確認操作を入れ、alerts status tableの対象へ進みます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
COMMAND ===&gt; nco_sql -server NCOMS -user root
→ Enter を押す
［画面・出力］
nco_sql session connected to ObjectServer NCOMS.
画面・出力には session が表示され、最初の到達点を確認できます。
――――
■ ステップ 2
現在の画面はNetcool/OMNIbus V8.1の確認画面です。ObjectServer propertiesを読むため、対象名を含む操作を入力します。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; select Identifier, Severity, Node from alerts.status;
→ Enter を押す
［画面・出力］
Identifier        Severity  Node
NODE049:LINKDOWN    5         NODE049
NODE049:RECOVER     2         NODE049
画面・出力には Identifier が含まれ、secure mode 重複排除確認 ドメイン値の証跡を確認できます。
――――
■ ステップ 3
現在の画面はNetcool/OMNIbus V8.1の詳細確認画面です。表示名とメッセージ形式を照合し、secure mode の接続失敗を切り分けます。
［操作（入力）］
Netcool/OMNIbus V8.1 操作画面
SQL ===&gt; describe alerts.status;
→ Enter を押す
［画面・出力］
Table alerts.status
Column Identifier
Column Severity
Column Node
画面・出力には Table が現れ、判定材料を記録できます。
――――</pre><p>合格条件: ① ステップ1 の session が画面・出力に表示されること
② ステップ2 の Identifier が画面・出力に表示されること
③ ステップ3 の Table が画面・出力に表示されること</p><p class="kb-meta">検証状態: 机上 ／ 出典: Netcool_OMNIbus_BestPractices_v1.3 / Netcool OMNIbus V8.1 Administration Guide / Command Reference</p></div></details></section>
